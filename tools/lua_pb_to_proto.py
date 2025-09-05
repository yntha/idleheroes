import argparse
import pathlib
import re
from collections import defaultdict, OrderedDict

LABEL_MAP = {
    1: "optional",
    2: "required",
    3: "repeated",
}

TYPE_MAP = {
    1: "double",
    2: "float",
    3: "int64",
    4: "uint64",
    5: "int32",
    6: "fixed64",
    7: "fixed32",
    8: "bool",
    9: "string",
    10: "group",
    11: "message",
    12: "bytes",
    13: "uint32",
    14: "enum",  # mapped to int32
    15: "sfixed32",
    16: "sfixed64",
    17: "sint32",
    18: "sint64",
}

FIELD_DECL_RE = re.compile(r'^([A-Z0-9_]+)\s*=\s*protobuf\.FieldDescriptor\(\)\s*$', re.M)
MSG_DECL_RE   = re.compile(r'^([A-Z0-9_]+)\s*=\s*protobuf\.Descriptor\(\)\s*$', re.M)
ASSIGN_STR_RE = re.compile(r'^([A-Z0-9_]+)\.([a-z_]+)\s*=\s*"([^"]*)"\s*$', re.M)
ASSIGN_INT_RE = re.compile(r'^([A-Z0-9_]+)\.([a-z_]+)\s*=\s*([0-9]+)\s*$', re.M)
ASSIGN_BOOL_RE= re.compile(r'^([A-Z0-9_]+)\.([a-z_]+)\s*=\s*(true|false)\s*$', re.M)
ASSIGN_MSGTYPE_RE = re.compile(r'^([A-Z0-9_]+)\.message_type\s*=\s*([A-Z0-9_]+)\s*$', re.M)
REQUIRE_RE = re.compile(r'^\s*local\s+([A-Z0-9_]+)\s*=\s*require\("([^"]+)"\)\s*$', re.M)
ASSIGN_MSGTYPE_XMODULE_RE = re.compile(  # for cross-module references
    r'^([A-Z0-9_]+)\.message_type\s*=\s*([A-Z0-9_]+)\.([A-Z0-9_]+)\s*$', re.M
)
MSG_NAME_RE = re.compile(r'^([A-Z0-9_]+)\.name\s*=\s*"([^"]+)"\s*$', re.M)
INSTANTIATE_RE = re.compile(r'^([a-z0-9_]+)\s*=\s*protobuf\.Message\(([A-Z0-9_]+)\)\s*$', re.M)
FIELDS_LIST_RE = re.compile(
    r'^([A-Z0-9_]+)\.fields\s*=\s*\{\s*([^}]*)\s*\}\s*$',
    re.M | re.S
)
MODULE_RE = re.compile(r'module\("([^"]+)"\)')


def parse_requires(lua_text: str):
    return {m.group(1): m.group(2) for m in REQUIRE_RE.finditer(lua_text)}


def guess_message_name_from_symbol(sym: str) -> str:
    return sym.lower()


def parse_lua(lua_text: str):
    m = MODULE_RE.search(lua_text)
    package = m.group(1) if m else "default_pkg"

    msg_vars = [m.group(1) for m in MSG_DECL_RE.finditer(lua_text)]
    val = ""

    msg_var_to_name = {}
    for m in MSG_NAME_RE.finditer(lua_text):
        msg_var_to_name[m.group(1)] = m.group(2)

    field_attrs = defaultdict(dict)
    for m in ASSIGN_STR_RE.finditer(lua_text):
        var, attr, val = m.group(1), m.group(2), m.group(3)
        field_attrs[var][attr] = val
    for m in ASSIGN_INT_RE.finditer(lua_text):
        var, attr, val = m.group(1), m.group(2), int(m.group(3))
        field_attrs[var][attr] = val
    for m in ASSIGN_BOOL_RE.finditer(lua_text):
        var, attr, val = m.group(1), m.group(2), (val == "true")
        field_attrs[var][attr] = val
    for m in ASSIGN_MSGTYPE_RE.finditer(lua_text):
        var, msgtype_var = m.group(1), m.group(2)
        field_attrs[var]["message_type_var"] = msgtype_var
    for m in ASSIGN_MSGTYPE_XMODULE_RE.finditer(lua_text):
        fv, alias, sym = m.group(1), m.group(2), m.group(3)
        field_attrs[fv]["message_type_external"] = (alias, sym)

    msg_fields_order = OrderedDict()
    for m in FIELDS_LIST_RE.finditer(lua_text):
        msg_var = m.group(1)
        inner = m.group(2)
        names = [s.strip() for s in inner.split(",") if s.strip()]
        msg_fields_order[msg_var] = names

    require_map = parse_requires(lua_text)

    return package, msg_vars, msg_var_to_name, field_attrs, msg_fields_order, require_map


def lua_to_proto(package, msg_vars, msg_var_to_name, field_attrs, msg_fields_order, require_map):
    out = []
    out.append('syntax = "proto2";')
    out.append(f'package {package};\n')

    imports_needed = set()
    for msg_var, field_var_list in msg_fields_order.items():
        for fv in field_var_list:
            attrs = field_attrs.get(fv, {})
            if attrs.get("type") == 11 and "message_type_external" in attrs:
                alias, _ = attrs["message_type_external"]
                pkg = require_map.get(alias)
                if pkg:
                    imports_needed.add(pkg)

    for pkg in sorted(imports_needed):
        out.append(f'import "{pkg}.proto";')
    if imports_needed:
        out.append("")

    def msg_canonical_name(msg_var):
        return msg_var_to_name.get(msg_var, msg_var.lower())

    for msg_var, field_var_list in msg_fields_order.items():
        msg_name = msg_canonical_name(msg_var)
        out.append(f"message {msg_name} {{")
        for fv in field_var_list:
            attrs = field_attrs.get(fv, {})
            label_num = attrs.get("label", 1)  # default optional
            label = LABEL_MAP.get(label_num, "optional")

            fnum = attrs.get("number")
            if fnum is None:
                # some real funky shit happening
                raise ValueError(f"Field {fv} missing 'number' attribute")

            fname = attrs.get("name", fv.lower())

            ftype_num = attrs.get("type")
            if ftype_num is None:
                base_type = "string"  # default to string
            else:
                base = TYPE_MAP.get(ftype_num, "string")
                if base == "message":
                    xref = attrs.get("message_type_external")
                    if xref:
                        alias, sym = xref
                        ext_pkg = require_map.get(alias)
                        if ext_pkg:
                            base_type = f"{ext_pkg}.{guess_message_name_from_symbol(sym)}"
                        else:
                            base_type = guess_message_name_from_symbol(sym)
                    else:
                        mt_var = attrs.get("message_type_var")
                        if mt_var:
                            base_type = msg_canonical_name(mt_var)
                        else:
                            base_type = "bytes"
                elif base == "enum":
                    base_type = "int32"
                else:
                    base_type = base

            out.append(f"  {label} {base_type} {fname} = {fnum};")
        out.append("}\n")
    return "\n".join(out)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("lua_file", help="Path to Lua file with protobuf descriptors")
    ap.add_argument("-o", "--out", default=None, help="Output .proto path")
    args = ap.parse_args()

    lua_path = pathlib.Path(args.lua_file)
    lua_text = lua_path.read_text(encoding="utf-8", errors="ignore")

    package, msg_vars, msg_var_to_name, field_attrs, msg_fields_order, require_map = parse_lua(lua_text)
    proto_text = lua_to_proto(package, msg_vars, msg_var_to_name, field_attrs, msg_fields_order, require_map)

    out_path = pathlib.Path(args.out) if args.out else lua_path.with_suffix(".proto")
    out_path.write_text(proto_text, encoding="utf-8")
    print(f"Wrote {out_path}")


if __name__ == "__main__":
    main()
