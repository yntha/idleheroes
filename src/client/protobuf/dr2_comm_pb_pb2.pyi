from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class pb_player(_message.Message):
    __slots__ = ("name", "logo", "gid", "gname", "border", "glv", "country", "sds", "city")
    NAME_FIELD_NUMBER: _ClassVar[int]
    LOGO_FIELD_NUMBER: _ClassVar[int]
    GID_FIELD_NUMBER: _ClassVar[int]
    GNAME_FIELD_NUMBER: _ClassVar[int]
    BORDER_FIELD_NUMBER: _ClassVar[int]
    GLV_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_FIELD_NUMBER: _ClassVar[int]
    SDS_FIELD_NUMBER: _ClassVar[int]
    CITY_FIELD_NUMBER: _ClassVar[int]
    name: str
    logo: int
    gid: int
    gname: str
    border: int
    glv: int
    country: str
    sds: str
    city: str
    def __init__(self, name: _Optional[str] = ..., logo: _Optional[int] = ..., gid: _Optional[int] = ..., gname: _Optional[str] = ..., border: _Optional[int] = ..., glv: _Optional[int] = ..., country: _Optional[str] = ..., sds: _Optional[str] = ..., city: _Optional[str] = ...) -> None: ...

class pb_server(_message.Message):
    __slots__ = ("sid", "sname", "pname", "plogo", "plv", "flag", "uid", "border", "login_cd")
    SID_FIELD_NUMBER: _ClassVar[int]
    SNAME_FIELD_NUMBER: _ClassVar[int]
    PNAME_FIELD_NUMBER: _ClassVar[int]
    PLOGO_FIELD_NUMBER: _ClassVar[int]
    PLV_FIELD_NUMBER: _ClassVar[int]
    FLAG_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    BORDER_FIELD_NUMBER: _ClassVar[int]
    LOGIN_CD_FIELD_NUMBER: _ClassVar[int]
    sid: int
    sname: str
    pname: str
    plogo: int
    plv: int
    flag: int
    uid: int
    border: int
    login_cd: int
    def __init__(self, sid: _Optional[int] = ..., sname: _Optional[str] = ..., pname: _Optional[str] = ..., plogo: _Optional[int] = ..., plv: _Optional[int] = ..., flag: _Optional[int] = ..., uid: _Optional[int] = ..., border: _Optional[int] = ..., login_cd: _Optional[int] = ...) -> None: ...

class pb_item(_message.Message):
    __slots__ = ("id", "num")
    ID_FIELD_NUMBER: _ClassVar[int]
    NUM_FIELD_NUMBER: _ClassVar[int]
    id: int
    num: int
    def __init__(self, id: _Optional[int] = ..., num: _Optional[int] = ...) -> None: ...

class pb_equip(_message.Message):
    __slots__ = ("id", "num", "eid", "hid")
    ID_FIELD_NUMBER: _ClassVar[int]
    NUM_FIELD_NUMBER: _ClassVar[int]
    EID_FIELD_NUMBER: _ClassVar[int]
    HID_FIELD_NUMBER: _ClassVar[int]
    id: int
    num: int
    eid: int
    hid: int
    def __init__(self, id: _Optional[int] = ..., num: _Optional[int] = ..., eid: _Optional[int] = ..., hid: _Optional[int] = ...) -> None: ...

class pb_bag(_message.Message):
    __slots__ = ("items", "equips")
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    EQUIPS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[pb_item]
    equips: _containers.RepeatedCompositeFieldContainer[pb_equip]
    def __init__(self, items: _Optional[_Iterable[_Union[pb_item, _Mapping]]] = ..., equips: _Optional[_Iterable[_Union[pb_equip, _Mapping]]] = ...) -> None: ...

class pb_hero_qlc(_message.Message):
    __slots__ = ("lv", "atk", "hp", "spd", "attr_idx", "time", "cd", "exp", "energy", "qbit")
    LV_FIELD_NUMBER: _ClassVar[int]
    ATK_FIELD_NUMBER: _ClassVar[int]
    HP_FIELD_NUMBER: _ClassVar[int]
    SPD_FIELD_NUMBER: _ClassVar[int]
    ATTR_IDX_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    CD_FIELD_NUMBER: _ClassVar[int]
    EXP_FIELD_NUMBER: _ClassVar[int]
    ENERGY_FIELD_NUMBER: _ClassVar[int]
    QBIT_FIELD_NUMBER: _ClassVar[int]
    lv: int
    atk: int
    hp: int
    spd: int
    attr_idx: int
    time: int
    cd: int
    exp: int
    energy: int
    qbit: int
    def __init__(self, lv: _Optional[int] = ..., atk: _Optional[int] = ..., hp: _Optional[int] = ..., spd: _Optional[int] = ..., attr_idx: _Optional[int] = ..., time: _Optional[int] = ..., cd: _Optional[int] = ..., exp: _Optional[int] = ..., energy: _Optional[int] = ..., qbit: _Optional[int] = ...) -> None: ...

class pb_hero_qlt(_message.Message):
    __slots__ = ("qlc", "qlcs", "attr_idx")
    QLC_FIELD_NUMBER: _ClassVar[int]
    QLCS_FIELD_NUMBER: _ClassVar[int]
    ATTR_IDX_FIELD_NUMBER: _ClassVar[int]
    qlc: pb_hero_qlc
    qlcs: _containers.RepeatedCompositeFieldContainer[pb_hero_qlc]
    attr_idx: int
    def __init__(self, qlc: _Optional[_Union[pb_hero_qlc, _Mapping]] = ..., qlcs: _Optional[_Iterable[_Union[pb_hero_qlc, _Mapping]]] = ..., attr_idx: _Optional[int] = ...) -> None: ...

class pb_tree(_message.Message):
    __slots__ = ("lv", "blv", "bra")
    LV_FIELD_NUMBER: _ClassVar[int]
    BLV_FIELD_NUMBER: _ClassVar[int]
    BRA_FIELD_NUMBER: _ClassVar[int]
    lv: int
    blv: int
    bra: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, lv: _Optional[int] = ..., blv: _Optional[int] = ..., bra: _Optional[_Iterable[int]] = ...) -> None: ...

class pb_hero(_message.Message):
    __slots__ = ("hid", "id", "lv", "star", "flag", "equips", "wake", "jade", "visit", "skill_id", "sattrs", "qlt", "tree", "faith")
    HID_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    LV_FIELD_NUMBER: _ClassVar[int]
    STAR_FIELD_NUMBER: _ClassVar[int]
    FLAG_FIELD_NUMBER: _ClassVar[int]
    EQUIPS_FIELD_NUMBER: _ClassVar[int]
    WAKE_FIELD_NUMBER: _ClassVar[int]
    JADE_FIELD_NUMBER: _ClassVar[int]
    VISIT_FIELD_NUMBER: _ClassVar[int]
    SKILL_ID_FIELD_NUMBER: _ClassVar[int]
    SATTRS_FIELD_NUMBER: _ClassVar[int]
    QLT_FIELD_NUMBER: _ClassVar[int]
    TREE_FIELD_NUMBER: _ClassVar[int]
    FAITH_FIELD_NUMBER: _ClassVar[int]
    hid: int
    id: int
    lv: int
    star: int
    flag: int
    equips: _containers.RepeatedCompositeFieldContainer[pb_equip]
    wake: int
    jade: _containers.RepeatedScalarFieldContainer[int]
    visit: bool
    skill_id: _containers.RepeatedScalarFieldContainer[int]
    sattrs: _containers.RepeatedCompositeFieldContainer[pb_sattr]
    qlt: pb_hero_qlt
    tree: pb_tree
    faith: pb_faith
    def __init__(self, hid: _Optional[int] = ..., id: _Optional[int] = ..., lv: _Optional[int] = ..., star: _Optional[int] = ..., flag: _Optional[int] = ..., equips: _Optional[_Iterable[_Union[pb_equip, _Mapping]]] = ..., wake: _Optional[int] = ..., jade: _Optional[_Iterable[int]] = ..., visit: _Optional[bool] = ..., skill_id: _Optional[_Iterable[int]] = ..., sattrs: _Optional[_Iterable[_Union[pb_sattr, _Mapping]]] = ..., qlt: _Optional[_Union[pb_hero_qlt, _Mapping]] = ..., tree: _Optional[_Union[pb_tree, _Mapping]] = ..., faith: _Optional[_Union[pb_faith, _Mapping]] = ...) -> None: ...

class pb_faith(_message.Message):
    __slots__ = ("lv", "skill")
    LV_FIELD_NUMBER: _ClassVar[int]
    SKILL_FIELD_NUMBER: _ClassVar[int]
    lv: int
    skill: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, lv: _Optional[int] = ..., skill: _Optional[_Iterable[int]] = ...) -> None: ...

class pb_sattr(_message.Message):
    __slots__ = ("id", "attr", "value")
    ID_FIELD_NUMBER: _ClassVar[int]
    ATTR_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    id: int
    attr: int
    value: int
    def __init__(self, id: _Optional[int] = ..., attr: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...

class pb_dup(_message.Message):
    __slots__ = ("id", "bids", "sts", "mid", "rid", "skip")
    ID_FIELD_NUMBER: _ClassVar[int]
    BIDS_FIELD_NUMBER: _ClassVar[int]
    STS_FIELD_NUMBER: _ClassVar[int]
    MID_FIELD_NUMBER: _ClassVar[int]
    RID_FIELD_NUMBER: _ClassVar[int]
    SKIP_FIELD_NUMBER: _ClassVar[int]
    id: int
    bids: _containers.RepeatedScalarFieldContainer[int]
    sts: int
    mid: int
    rid: int
    skip: int
    def __init__(self, id: _Optional[int] = ..., bids: _Optional[_Iterable[int]] = ..., sts: _Optional[int] = ..., mid: _Optional[int] = ..., rid: _Optional[int] = ..., skip: _Optional[int] = ...) -> None: ...

class pb_embr(_message.Message):
    __slots__ = ("uid", "lv", "status", "stime", "logo", "name", "border", "id")
    UID_FIELD_NUMBER: _ClassVar[int]
    LV_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    STIME_FIELD_NUMBER: _ClassVar[int]
    LOGO_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    BORDER_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    uid: int
    lv: int
    status: int
    stime: str
    logo: int
    name: str
    border: int
    id: int
    def __init__(self, uid: _Optional[int] = ..., lv: _Optional[int] = ..., status: _Optional[int] = ..., stime: _Optional[str] = ..., logo: _Optional[int] = ..., name: _Optional[str] = ..., border: _Optional[int] = ..., id: _Optional[int] = ...) -> None: ...

class pb_scell(_message.Message):
    __slots__ = ("pos", "status", "id", "ids1", "ids2")
    POS_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    IDS1_FIELD_NUMBER: _ClassVar[int]
    IDS2_FIELD_NUMBER: _ClassVar[int]
    pos: int
    status: int
    id: int
    ids1: _containers.RepeatedScalarFieldContainer[int]
    ids2: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, pos: _Optional[int] = ..., status: _Optional[int] = ..., id: _Optional[int] = ..., ids1: _Optional[_Iterable[int]] = ..., ids2: _Optional[_Iterable[int]] = ...) -> None: ...

class pb_sbuilding(_message.Message):
    __slots__ = ("lv", "cd", "num")
    LV_FIELD_NUMBER: _ClassVar[int]
    CD_FIELD_NUMBER: _ClassVar[int]
    NUM_FIELD_NUMBER: _ClassVar[int]
    lv: int
    cd: int
    num: int
    def __init__(self, lv: _Optional[int] = ..., cd: _Optional[int] = ..., num: _Optional[int] = ...) -> None: ...

class pb_sscell(_message.Message):
    __slots__ = ("pos", "status", "id", "boss_id", "boss_hp", "mbr", "hid", "cd", "lv", "add", "times", "rid", "wake", "rlv", "rqlv")
    POS_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    BOSS_ID_FIELD_NUMBER: _ClassVar[int]
    BOSS_HP_FIELD_NUMBER: _ClassVar[int]
    MBR_FIELD_NUMBER: _ClassVar[int]
    HID_FIELD_NUMBER: _ClassVar[int]
    CD_FIELD_NUMBER: _ClassVar[int]
    LV_FIELD_NUMBER: _ClassVar[int]
    ADD_FIELD_NUMBER: _ClassVar[int]
    TIMES_FIELD_NUMBER: _ClassVar[int]
    RID_FIELD_NUMBER: _ClassVar[int]
    WAKE_FIELD_NUMBER: _ClassVar[int]
    RLV_FIELD_NUMBER: _ClassVar[int]
    RQLV_FIELD_NUMBER: _ClassVar[int]
    pos: int
    status: int
    id: int
    boss_id: int
    boss_hp: _containers.RepeatedScalarFieldContainer[int]
    mbr: pb_pmbr
    hid: int
    cd: int
    lv: int
    add: int
    times: int
    rid: int
    wake: int
    rlv: int
    rqlv: int
    def __init__(self, pos: _Optional[int] = ..., status: _Optional[int] = ..., id: _Optional[int] = ..., boss_id: _Optional[int] = ..., boss_hp: _Optional[_Iterable[int]] = ..., mbr: _Optional[_Union[pb_pmbr, _Mapping]] = ..., hid: _Optional[int] = ..., cd: _Optional[int] = ..., lv: _Optional[int] = ..., add: _Optional[int] = ..., times: _Optional[int] = ..., rid: _Optional[int] = ..., wake: _Optional[int] = ..., rlv: _Optional[int] = ..., rqlv: _Optional[int] = ...) -> None: ...

class pb_ssevent(_message.Message):
    __slots__ = ("id", "num", "lv_item", "score", "num2", "reward")
    ID_FIELD_NUMBER: _ClassVar[int]
    NUM_FIELD_NUMBER: _ClassVar[int]
    LV_ITEM_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    NUM2_FIELD_NUMBER: _ClassVar[int]
    REWARD_FIELD_NUMBER: _ClassVar[int]
    id: int
    num: int
    lv_item: int
    score: int
    num2: int
    reward: _containers.RepeatedCompositeFieldContainer[pb_bag]
    def __init__(self, id: _Optional[int] = ..., num: _Optional[int] = ..., lv_item: _Optional[int] = ..., score: _Optional[int] = ..., num2: _Optional[int] = ..., reward: _Optional[_Iterable[_Union[pb_bag, _Mapping]]] = ...) -> None: ...

class pb_sssweep(_message.Message):
    __slots__ = ("pos", "hid")
    POS_FIELD_NUMBER: _ClassVar[int]
    HID_FIELD_NUMBER: _ClassVar[int]
    pos: int
    hid: int
    def __init__(self, pos: _Optional[int] = ..., hid: _Optional[int] = ...) -> None: ...

class pb_gacha(_message.Message):
    __slots__ = ("item", "gem", "id", "act", "cd")
    ITEM_FIELD_NUMBER: _ClassVar[int]
    GEM_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    ACT_FIELD_NUMBER: _ClassVar[int]
    CD_FIELD_NUMBER: _ClassVar[int]
    item: int
    gem: int
    id: int
    act: int
    cd: int
    def __init__(self, item: _Optional[int] = ..., gem: _Optional[int] = ..., id: _Optional[int] = ..., act: _Optional[int] = ..., cd: _Optional[int] = ...) -> None: ...

class pb_mail(_message.Message):
    __slots__ = ("mid", "id", "uid", "flag", "send_time", "title", "content", "content_o", "affix")
    MID_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    FLAG_FIELD_NUMBER: _ClassVar[int]
    SEND_TIME_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    FROM_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    CONTENT_O_FIELD_NUMBER: _ClassVar[int]
    AFFIX_FIELD_NUMBER: _ClassVar[int]
    mid: int
    id: int
    uid: int
    flag: int
    send_time: int
    title: str
    content: str
    content_o: str
    affix: pb_bag
    def __init__(self, mid: _Optional[int] = ..., id: _Optional[int] = ..., uid: _Optional[int] = ..., flag: _Optional[int] = ..., send_time: _Optional[int] = ..., title: _Optional[str] = ..., content: _Optional[str] = ..., content_o: _Optional[str] = ..., affix: _Optional[_Union[pb_bag, _Mapping]] = ..., **kwargs) -> None: ...

class pb_cunit(_message.Message):
    __slots__ = ("id", "lv", "star", "power", "hp", "atk", "armor", "spd", "wake", "skin", "stl", "qlv", "tree", "core", "faith_lv")
    ID_FIELD_NUMBER: _ClassVar[int]
    LV_FIELD_NUMBER: _ClassVar[int]
    STAR_FIELD_NUMBER: _ClassVar[int]
    POWER_FIELD_NUMBER: _ClassVar[int]
    HP_FIELD_NUMBER: _ClassVar[int]
    ATK_FIELD_NUMBER: _ClassVar[int]
    ARMOR_FIELD_NUMBER: _ClassVar[int]
    SPD_FIELD_NUMBER: _ClassVar[int]
    WAKE_FIELD_NUMBER: _ClassVar[int]
    SKIN_FIELD_NUMBER: _ClassVar[int]
    STL_FIELD_NUMBER: _ClassVar[int]
    QLV_FIELD_NUMBER: _ClassVar[int]
    TREE_FIELD_NUMBER: _ClassVar[int]
    CORE_FIELD_NUMBER: _ClassVar[int]
    FAITH_LV_FIELD_NUMBER: _ClassVar[int]
    id: int
    lv: int
    star: int
    power: int
    hp: int
    atk: int
    armor: int
    spd: int
    wake: int
    skin: int
    stl: int
    qlv: int
    tree: pb_tree
    core: int
    faith_lv: int
    def __init__(self, id: _Optional[int] = ..., lv: _Optional[int] = ..., star: _Optional[int] = ..., power: _Optional[int] = ..., hp: _Optional[int] = ..., atk: _Optional[int] = ..., armor: _Optional[int] = ..., spd: _Optional[int] = ..., wake: _Optional[int] = ..., skin: _Optional[int] = ..., stl: _Optional[int] = ..., qlv: _Optional[int] = ..., tree: _Optional[_Union[pb_tree, _Mapping]] = ..., core: _Optional[int] = ..., faith_lv: _Optional[int] = ...) -> None: ...

class pb_chat(_message.Message):
    __slots__ = ("uid", "logo", "lv", "vip", "name", "type", "text", "time", "share_id", "hero_id", "final_rank", "gid", "gname", "glv", "gmsg", "gFight", "border", "hteam", "country", "sds", "city", "emblem")
    UID_FIELD_NUMBER: _ClassVar[int]
    LOGO_FIELD_NUMBER: _ClassVar[int]
    LV_FIELD_NUMBER: _ClassVar[int]
    VIP_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    SHARE_ID_FIELD_NUMBER: _ClassVar[int]
    HERO_ID_FIELD_NUMBER: _ClassVar[int]
    FINAL_RANK_FIELD_NUMBER: _ClassVar[int]
    GID_FIELD_NUMBER: _ClassVar[int]
    GNAME_FIELD_NUMBER: _ClassVar[int]
    GLV_FIELD_NUMBER: _ClassVar[int]
    GMSG_FIELD_NUMBER: _ClassVar[int]
    GFIGHT_FIELD_NUMBER: _ClassVar[int]
    BORDER_FIELD_NUMBER: _ClassVar[int]
    HTEAM_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_FIELD_NUMBER: _ClassVar[int]
    SDS_FIELD_NUMBER: _ClassVar[int]
    CITY_FIELD_NUMBER: _ClassVar[int]
    EMBLEM_FIELD_NUMBER: _ClassVar[int]
    uid: int
    logo: int
    lv: int
    vip: int
    name: str
    type: int
    text: str
    time: int
    share_id: int
    hero_id: int
    final_rank: int
    gid: int
    gname: str
    glv: int
    gmsg: str
    gFight: int
    border: int
    hteam: pb_hteam
    country: str
    sds: str
    city: str
    emblem: int
    def __init__(self, uid: _Optional[int] = ..., logo: _Optional[int] = ..., lv: _Optional[int] = ..., vip: _Optional[int] = ..., name: _Optional[str] = ..., type: _Optional[int] = ..., text: _Optional[str] = ..., time: _Optional[int] = ..., share_id: _Optional[int] = ..., hero_id: _Optional[int] = ..., final_rank: _Optional[int] = ..., gid: _Optional[int] = ..., gname: _Optional[str] = ..., glv: _Optional[int] = ..., gmsg: _Optional[str] = ..., gFight: _Optional[int] = ..., border: _Optional[int] = ..., hteam: _Optional[_Union[pb_hteam, _Mapping]] = ..., country: _Optional[str] = ..., sds: _Optional[str] = ..., city: _Optional[str] = ..., emblem: _Optional[int] = ...) -> None: ...

class pb_upfile(_message.Message):
    __slots__ = ("md5", "path")
    MD5_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    md5: str
    path: str
    def __init__(self, md5: _Optional[str] = ..., path: _Optional[str] = ...) -> None: ...

class pb_good(_message.Message):
    __slots__ = ("id", "type", "count", "excel_id", "bought")
    ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    EXCEL_ID_FIELD_NUMBER: _ClassVar[int]
    BOUGHT_FIELD_NUMBER: _ClassVar[int]
    id: int
    type: int
    count: int
    excel_id: int
    bought: int
    def __init__(self, id: _Optional[int] = ..., type: _Optional[int] = ..., count: _Optional[int] = ..., excel_id: _Optional[int] = ..., bought: _Optional[int] = ...) -> None: ...

class pb_onepay(_message.Message):
    __slots__ = ("tid", "txid", "tdate")
    TID_FIELD_NUMBER: _ClassVar[int]
    TXID_FIELD_NUMBER: _ClassVar[int]
    TDATE_FIELD_NUMBER: _ClassVar[int]
    tid: str
    txid: str
    tdate: str
    def __init__(self, tid: _Optional[str] = ..., txid: _Optional[str] = ..., tdate: _Optional[str] = ...) -> None: ...

class pb_hook(_message.Message):
    __slots__ = ("status", "hook_stage", "boss_cd", "poker_cd", "reward", "pve_stage", "extra", "ids", "hard_stage")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    HOOK_STAGE_FIELD_NUMBER: _ClassVar[int]
    BOSS_CD_FIELD_NUMBER: _ClassVar[int]
    POKER_CD_FIELD_NUMBER: _ClassVar[int]
    REWARD_FIELD_NUMBER: _ClassVar[int]
    PVE_STAGE_FIELD_NUMBER: _ClassVar[int]
    EXTRA_FIELD_NUMBER: _ClassVar[int]
    IDS_FIELD_NUMBER: _ClassVar[int]
    HARD_STAGE_FIELD_NUMBER: _ClassVar[int]
    status: int
    hook_stage: int
    boss_cd: int
    poker_cd: int
    reward: pb_bag
    pve_stage: int
    extra: pb_bag
    ids: _containers.RepeatedCompositeFieldContainer[pb_item]
    hard_stage: int
    def __init__(self, status: _Optional[int] = ..., hook_stage: _Optional[int] = ..., boss_cd: _Optional[int] = ..., poker_cd: _Optional[int] = ..., reward: _Optional[_Union[pb_bag, _Mapping]] = ..., pve_stage: _Optional[int] = ..., extra: _Optional[_Union[pb_bag, _Mapping]] = ..., ids: _Optional[_Iterable[_Union[pb_item, _Mapping]]] = ..., hard_stage: _Optional[int] = ...) -> None: ...

class pb_frd(_message.Message):
    __slots__ = ("logo", "name", "lv", "flag", "uid", "last", "power", "border", "country", "sds", "city", "emblem", "mgame")
    LOGO_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    LV_FIELD_NUMBER: _ClassVar[int]
    FLAG_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    LAST_FIELD_NUMBER: _ClassVar[int]
    POWER_FIELD_NUMBER: _ClassVar[int]
    BORDER_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_FIELD_NUMBER: _ClassVar[int]
    SDS_FIELD_NUMBER: _ClassVar[int]
    CITY_FIELD_NUMBER: _ClassVar[int]
    EMBLEM_FIELD_NUMBER: _ClassVar[int]
    MGAME_FIELD_NUMBER: _ClassVar[int]
    logo: int
    name: str
    lv: int
    flag: int
    uid: int
    last: int
    power: int
    border: int
    country: str
    sds: str
    city: str
    emblem: int
    mgame: int
    def __init__(self, logo: _Optional[int] = ..., name: _Optional[str] = ..., lv: _Optional[int] = ..., flag: _Optional[int] = ..., uid: _Optional[int] = ..., last: _Optional[int] = ..., power: _Optional[int] = ..., border: _Optional[int] = ..., country: _Optional[str] = ..., sds: _Optional[str] = ..., city: _Optional[str] = ..., emblem: _Optional[int] = ..., mgame: _Optional[int] = ...) -> None: ...

class pb_friend(_message.Message):
    __slots__ = ("friends", "love", "cd", "apply", "recmd")
    FRIENDS_FIELD_NUMBER: _ClassVar[int]
    LOVE_FIELD_NUMBER: _ClassVar[int]
    CD_FIELD_NUMBER: _ClassVar[int]
    APPLY_FIELD_NUMBER: _ClassVar[int]
    RECMD_FIELD_NUMBER: _ClassVar[int]
    friends: _containers.RepeatedCompositeFieldContainer[pb_frd]
    love: int
    cd: int
    apply: _containers.RepeatedCompositeFieldContainer[pb_frd]
    recmd: _containers.RepeatedCompositeFieldContainer[pb_frd]
    def __init__(self, friends: _Optional[_Iterable[_Union[pb_frd, _Mapping]]] = ..., love: _Optional[int] = ..., cd: _Optional[int] = ..., apply: _Optional[_Iterable[_Union[pb_frd, _Mapping]]] = ..., recmd: _Optional[_Iterable[_Union[pb_frd, _Mapping]]] = ...) -> None: ...

class pb_casino_item(_message.Message):
    __slots__ = ("type", "id", "count", "cool", "limitBuy", "weight")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    COOL_FIELD_NUMBER: _ClassVar[int]
    LIMITBUY_FIELD_NUMBER: _ClassVar[int]
    WEIGHT_FIELD_NUMBER: _ClassVar[int]
    type: int
    id: int
    count: int
    cool: int
    limitBuy: int
    weight: int
    def __init__(self, type: _Optional[int] = ..., id: _Optional[int] = ..., count: _Optional[int] = ..., cool: _Optional[int] = ..., limitBuy: _Optional[int] = ..., weight: _Optional[int] = ...) -> None: ...

class pb_casino_msg(_message.Message):
    __slots__ = ("name", "type", "id", "count")
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    name: str
    type: int
    id: int
    count: int
    def __init__(self, name: _Optional[str] = ..., type: _Optional[int] = ..., id: _Optional[int] = ..., count: _Optional[int] = ...) -> None: ...

class pb_gmember(_message.Message):
    __slots__ = ("uid", "name", "lv", "logo", "last", "title", "power", "gfight", "border", "cwar", "country", "sds", "city", "emblem", "cur_live", "last_live", "mgame")
    UID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    LV_FIELD_NUMBER: _ClassVar[int]
    LOGO_FIELD_NUMBER: _ClassVar[int]
    LAST_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    POWER_FIELD_NUMBER: _ClassVar[int]
    GFIGHT_FIELD_NUMBER: _ClassVar[int]
    BORDER_FIELD_NUMBER: _ClassVar[int]
    CWAR_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_FIELD_NUMBER: _ClassVar[int]
    SDS_FIELD_NUMBER: _ClassVar[int]
    CITY_FIELD_NUMBER: _ClassVar[int]
    EMBLEM_FIELD_NUMBER: _ClassVar[int]
    CUR_LIVE_FIELD_NUMBER: _ClassVar[int]
    LAST_LIVE_FIELD_NUMBER: _ClassVar[int]
    MGAME_FIELD_NUMBER: _ClassVar[int]
    uid: int
    name: str
    lv: int
    logo: int
    last: int
    title: int
    power: int
    gfight: int
    border: int
    cwar: int
    country: str
    sds: str
    city: str
    emblem: int
    cur_live: int
    last_live: int
    mgame: int
    def __init__(self, uid: _Optional[int] = ..., name: _Optional[str] = ..., lv: _Optional[int] = ..., logo: _Optional[int] = ..., last: _Optional[int] = ..., title: _Optional[int] = ..., power: _Optional[int] = ..., gfight: _Optional[int] = ..., border: _Optional[int] = ..., cwar: _Optional[int] = ..., country: _Optional[str] = ..., sds: _Optional[str] = ..., city: _Optional[str] = ..., emblem: _Optional[int] = ..., cur_live: _Optional[int] = ..., last_live: _Optional[int] = ..., mgame: _Optional[int] = ...) -> None: ...

class pb_guild(_message.Message):
    __slots__ = ("id", "name", "logo", "exp", "notice", "power", "rank", "members", "pname", "dismiss_cd", "flag")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    LOGO_FIELD_NUMBER: _ClassVar[int]
    EXP_FIELD_NUMBER: _ClassVar[int]
    NOTICE_FIELD_NUMBER: _ClassVar[int]
    POWER_FIELD_NUMBER: _ClassVar[int]
    RANK_FIELD_NUMBER: _ClassVar[int]
    MEMBERS_FIELD_NUMBER: _ClassVar[int]
    PNAME_FIELD_NUMBER: _ClassVar[int]
    DISMISS_CD_FIELD_NUMBER: _ClassVar[int]
    FLAG_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    logo: int
    exp: int
    notice: str
    power: int
    rank: int
    members: int
    pname: str
    dismiss_cd: int
    flag: int
    def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ..., logo: _Optional[int] = ..., exp: _Optional[int] = ..., notice: _Optional[str] = ..., power: _Optional[int] = ..., rank: _Optional[int] = ..., members: _Optional[int] = ..., pname: _Optional[str] = ..., dismiss_cd: _Optional[int] = ..., flag: _Optional[int] = ...) -> None: ...

class pb_glog(_message.Message):
    __slots__ = ("type", "time", "obj_name", "do_name")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    OBJ_NAME_FIELD_NUMBER: _ClassVar[int]
    DO_NAME_FIELD_NUMBER: _ClassVar[int]
    type: int
    time: int
    obj_name: str
    do_name: str
    def __init__(self, type: _Optional[int] = ..., time: _Optional[int] = ..., obj_name: _Optional[str] = ..., do_name: _Optional[str] = ...) -> None: ...

class pb_unit(_message.Message):
    __slots__ = ("hid", "id", "pos", "lv", "star", "energy", "hpp", "wake", "skin", "stl", "flag", "ex2", "core", "cele", "bra", "faith_lv")
    HID_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    POS_FIELD_NUMBER: _ClassVar[int]
    LV_FIELD_NUMBER: _ClassVar[int]
    STAR_FIELD_NUMBER: _ClassVar[int]
    ENERGY_FIELD_NUMBER: _ClassVar[int]
    HPP_FIELD_NUMBER: _ClassVar[int]
    WAKE_FIELD_NUMBER: _ClassVar[int]
    SKIN_FIELD_NUMBER: _ClassVar[int]
    STL_FIELD_NUMBER: _ClassVar[int]
    FLAG_FIELD_NUMBER: _ClassVar[int]
    EX2_FIELD_NUMBER: _ClassVar[int]
    CORE_FIELD_NUMBER: _ClassVar[int]
    CELE_FIELD_NUMBER: _ClassVar[int]
    BRA_FIELD_NUMBER: _ClassVar[int]
    FAITH_LV_FIELD_NUMBER: _ClassVar[int]
    hid: int
    id: int
    pos: int
    lv: int
    star: int
    energy: int
    hpp: int
    wake: int
    skin: int
    stl: int
    flag: int
    ex2: int
    core: int
    cele: int
    bra: _containers.RepeatedScalarFieldContainer[int]
    faith_lv: int
    def __init__(self, hid: _Optional[int] = ..., id: _Optional[int] = ..., pos: _Optional[int] = ..., lv: _Optional[int] = ..., star: _Optional[int] = ..., energy: _Optional[int] = ..., hpp: _Optional[int] = ..., wake: _Optional[int] = ..., skin: _Optional[int] = ..., stl: _Optional[int] = ..., flag: _Optional[int] = ..., ex2: _Optional[int] = ..., core: _Optional[int] = ..., cele: _Optional[int] = ..., bra: _Optional[_Iterable[int]] = ..., faith_lv: _Optional[int] = ...) -> None: ...

class pb_strial(_message.Message):
    __slots__ = ("id", "tl", "cd")
    ID_FIELD_NUMBER: _ClassVar[int]
    TL_FIELD_NUMBER: _ClassVar[int]
    CD_FIELD_NUMBER: _ClassVar[int]
    id: int
    tl: int
    cd: int
    def __init__(self, id: _Optional[int] = ..., tl: _Optional[int] = ..., cd: _Optional[int] = ...) -> None: ...

class pb_trial(_message.Message):
    __slots__ = ("logo", "lv", "name", "power", "stage", "video", "border", "uid")
    LOGO_FIELD_NUMBER: _ClassVar[int]
    LV_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    POWER_FIELD_NUMBER: _ClassVar[int]
    STAGE_FIELD_NUMBER: _ClassVar[int]
    VIDEO_FIELD_NUMBER: _ClassVar[int]
    BORDER_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    logo: int
    lv: int
    name: str
    power: int
    stage: int
    video: pb_evideo
    border: int
    uid: int
    def __init__(self, logo: _Optional[int] = ..., lv: _Optional[int] = ..., name: _Optional[str] = ..., power: _Optional[int] = ..., stage: _Optional[int] = ..., video: _Optional[_Union[pb_evideo, _Mapping]] = ..., border: _Optional[int] = ..., uid: _Optional[int] = ...) -> None: ...

class pb_plog(_message.Message):
    __slots__ = ("rival", "atk", "win", "vid", "time", "score", "wins")
    RIVAL_FIELD_NUMBER: _ClassVar[int]
    ATK_FIELD_NUMBER: _ClassVar[int]
    WIN_FIELD_NUMBER: _ClassVar[int]
    VID_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    WINS_FIELD_NUMBER: _ClassVar[int]
    rival: pb_pmbr
    atk: bool
    win: bool
    vid: _containers.RepeatedScalarFieldContainer[int]
    time: int
    score: int
    wins: _containers.RepeatedScalarFieldContainer[bool]
    def __init__(self, rival: _Optional[_Union[pb_pmbr, _Mapping]] = ..., atk: _Optional[bool] = ..., win: _Optional[bool] = ..., vid: _Optional[_Iterable[int]] = ..., time: _Optional[int] = ..., score: _Optional[int] = ..., wins: _Optional[_Iterable[bool]] = ...) -> None: ...

class pb_p3plog(_message.Message):
    __slots__ = ("atk", "win", "vid", "time", "score")
    DEF_FIELD_NUMBER: _ClassVar[int]
    ATK_FIELD_NUMBER: _ClassVar[int]
    WIN_FIELD_NUMBER: _ClassVar[int]
    VID_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    atk: bool
    win: bool
    vid: int
    time: int
    score: int
    def __init__(self, atk: _Optional[bool] = ..., win: _Optional[bool] = ..., vid: _Optional[int] = ..., time: _Optional[int] = ..., score: _Optional[int] = ..., **kwargs) -> None: ...

class pb_pmbr(_message.Message):
    __slots__ = ("name", "uid", "lv", "logo", "score", "power", "rank", "gname", "trank", "tscore", "camp", "win", "fight", "sid", "border", "ptype", "emblem")
    NAME_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    LV_FIELD_NUMBER: _ClassVar[int]
    LOGO_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    POWER_FIELD_NUMBER: _ClassVar[int]
    RANK_FIELD_NUMBER: _ClassVar[int]
    GNAME_FIELD_NUMBER: _ClassVar[int]
    TRANK_FIELD_NUMBER: _ClassVar[int]
    TSCORE_FIELD_NUMBER: _ClassVar[int]
    CAMP_FIELD_NUMBER: _ClassVar[int]
    WIN_FIELD_NUMBER: _ClassVar[int]
    FIGHT_FIELD_NUMBER: _ClassVar[int]
    SID_FIELD_NUMBER: _ClassVar[int]
    BORDER_FIELD_NUMBER: _ClassVar[int]
    PTYPE_FIELD_NUMBER: _ClassVar[int]
    EMBLEM_FIELD_NUMBER: _ClassVar[int]
    name: str
    uid: int
    lv: int
    logo: int
    score: int
    power: int
    rank: int
    gname: str
    trank: int
    tscore: int
    camp: _containers.RepeatedCompositeFieldContainer[pb_unit]
    win: int
    fight: int
    sid: int
    border: int
    ptype: int
    emblem: int
    def __init__(self, name: _Optional[str] = ..., uid: _Optional[int] = ..., lv: _Optional[int] = ..., logo: _Optional[int] = ..., score: _Optional[int] = ..., power: _Optional[int] = ..., rank: _Optional[int] = ..., gname: _Optional[str] = ..., trank: _Optional[int] = ..., tscore: _Optional[int] = ..., camp: _Optional[_Iterable[_Union[pb_unit, _Mapping]]] = ..., win: _Optional[int] = ..., fight: _Optional[int] = ..., sid: _Optional[int] = ..., border: _Optional[int] = ..., ptype: _Optional[int] = ..., emblem: _Optional[int] = ...) -> None: ...

class pb_p3pmbr(_message.Message):
    __slots__ = ("name", "uid", "lv", "logo", "lbox", "power", "rank", "score", "camp", "emblem")
    NAME_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    LV_FIELD_NUMBER: _ClassVar[int]
    LOGO_FIELD_NUMBER: _ClassVar[int]
    LBOX_FIELD_NUMBER: _ClassVar[int]
    POWER_FIELD_NUMBER: _ClassVar[int]
    RANK_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    CAMP_FIELD_NUMBER: _ClassVar[int]
    EMBLEM_FIELD_NUMBER: _ClassVar[int]
    name: str
    uid: int
    lv: int
    logo: int
    lbox: int
    power: int
    rank: int
    score: int
    camp: _containers.RepeatedCompositeFieldContainer[pb_unit]
    emblem: int
    def __init__(self, name: _Optional[str] = ..., uid: _Optional[int] = ..., lv: _Optional[int] = ..., logo: _Optional[int] = ..., lbox: _Optional[int] = ..., power: _Optional[int] = ..., rank: _Optional[int] = ..., score: _Optional[int] = ..., camp: _Optional[_Iterable[_Union[pb_unit, _Mapping]]] = ..., emblem: _Optional[int] = ...) -> None: ...

class pb_smbr(_message.Message):
    __slots__ = ("name", "uid", "lv", "logo", "lbox", "score", "like", "cluster", "udk", "gname", "camp", "skls", "power", "hide", "emblem", "fire")
    NAME_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    LV_FIELD_NUMBER: _ClassVar[int]
    LOGO_FIELD_NUMBER: _ClassVar[int]
    LBOX_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    LIKE_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_FIELD_NUMBER: _ClassVar[int]
    UDK_FIELD_NUMBER: _ClassVar[int]
    GNAME_FIELD_NUMBER: _ClassVar[int]
    CAMP_FIELD_NUMBER: _ClassVar[int]
    SKLS_FIELD_NUMBER: _ClassVar[int]
    POWER_FIELD_NUMBER: _ClassVar[int]
    HIDE_FIELD_NUMBER: _ClassVar[int]
    EMBLEM_FIELD_NUMBER: _ClassVar[int]
    FIRE_FIELD_NUMBER: _ClassVar[int]
    name: str
    uid: int
    lv: int
    logo: int
    lbox: int
    score: int
    like: int
    cluster: str
    udk: str
    gname: str
    camp: _containers.RepeatedCompositeFieldContainer[pb_unit]
    skls: _containers.RepeatedScalarFieldContainer[int]
    power: int
    hide: _containers.RepeatedScalarFieldContainer[int]
    emblem: int
    fire: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, name: _Optional[str] = ..., uid: _Optional[int] = ..., lv: _Optional[int] = ..., logo: _Optional[int] = ..., lbox: _Optional[int] = ..., score: _Optional[int] = ..., like: _Optional[int] = ..., cluster: _Optional[str] = ..., udk: _Optional[str] = ..., gname: _Optional[str] = ..., camp: _Optional[_Iterable[_Union[pb_unit, _Mapping]]] = ..., skls: _Optional[_Iterable[int]] = ..., power: _Optional[int] = ..., hide: _Optional[_Iterable[int]] = ..., emblem: _Optional[int] = ..., fire: _Optional[_Iterable[int]] = ...) -> None: ...

class pb_smbrs(_message.Message):
    __slots__ = ("mbrs", "score", "rank", "like")
    MBRS_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    RANK_FIELD_NUMBER: _ClassVar[int]
    LIKE_FIELD_NUMBER: _ClassVar[int]
    mbrs: _containers.RepeatedCompositeFieldContainer[pb_smbr]
    score: int
    rank: int
    like: int
    def __init__(self, mbrs: _Optional[_Iterable[_Union[pb_smbr, _Mapping]]] = ..., score: _Optional[int] = ..., rank: _Optional[int] = ..., like: _Optional[int] = ...) -> None: ...

class pb_template(_message.Message):
    __slots__ = ("id", "name", "buildings", "rooms")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    BUILDINGS_FIELD_NUMBER: _ClassVar[int]
    ROOMS_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    buildings: _containers.RepeatedCompositeFieldContainer[pb_buildings]
    rooms: _containers.RepeatedCompositeFieldContainer[pb_room]
    def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ..., buildings: _Optional[_Iterable[_Union[pb_buildings, _Mapping]]] = ..., rooms: _Optional[_Iterable[_Union[pb_room, _Mapping]]] = ...) -> None: ...

class pb_pvp(_message.Message):
    __slots__ = ("id", "status", "self", "season_cd", "daily_cd")
    ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    SELF_FIELD_NUMBER: _ClassVar[int]
    SEASON_CD_FIELD_NUMBER: _ClassVar[int]
    DAILY_CD_FIELD_NUMBER: _ClassVar[int]
    id: int
    status: int
    self: pb_pmbr
    season_cd: int
    daily_cd: int
    def __init__(self_, id: _Optional[int] = ..., status: _Optional[int] = ..., self: _Optional[_Union[pb_pmbr, _Mapping]] = ..., season_cd: _Optional[int] = ..., daily_cd: _Optional[int] = ...) -> None: ...

class pb_wpvp(_message.Message):
    __slots__ = ("wid", "flag", "cd")
    WID_FIELD_NUMBER: _ClassVar[int]
    FLAG_FIELD_NUMBER: _ClassVar[int]
    CD_FIELD_NUMBER: _ClassVar[int]
    wid: int
    flag: int
    cd: int
    def __init__(self, wid: _Optional[int] = ..., flag: _Optional[int] = ..., cd: _Optional[int] = ...) -> None: ...

class pb_wmbr(_message.Message):
    __slots__ = ("uid", "gname", "score", "name", "logo", "lv", "power", "lbox", "like", "king", "num", "emblem")
    UID_FIELD_NUMBER: _ClassVar[int]
    GNAME_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    LOGO_FIELD_NUMBER: _ClassVar[int]
    LV_FIELD_NUMBER: _ClassVar[int]
    POWER_FIELD_NUMBER: _ClassVar[int]
    LBOX_FIELD_NUMBER: _ClassVar[int]
    LIKE_FIELD_NUMBER: _ClassVar[int]
    KING_FIELD_NUMBER: _ClassVar[int]
    NUM_FIELD_NUMBER: _ClassVar[int]
    EMBLEM_FIELD_NUMBER: _ClassVar[int]
    uid: int
    gname: str
    score: int
    name: str
    logo: int
    lv: int
    power: int
    lbox: int
    like: int
    king: bool
    num: int
    emblem: int
    def __init__(self, uid: _Optional[int] = ..., gname: _Optional[str] = ..., score: _Optional[int] = ..., name: _Optional[str] = ..., logo: _Optional[int] = ..., lv: _Optional[int] = ..., power: _Optional[int] = ..., lbox: _Optional[int] = ..., like: _Optional[int] = ..., king: _Optional[bool] = ..., num: _Optional[int] = ..., emblem: _Optional[int] = ...) -> None: ...

class pb_link(_message.Message):
    __slots__ = ("cd", "win", "vid")
    CD_FIELD_NUMBER: _ClassVar[int]
    WIN_FIELD_NUMBER: _ClassVar[int]
    VID_FIELD_NUMBER: _ClassVar[int]
    cd: int
    win: int
    vid: int
    def __init__(self, cd: _Optional[int] = ..., win: _Optional[int] = ..., vid: _Optional[int] = ...) -> None: ...

class pb_wlog(_message.Message):
    __slots__ = ("vid", "atk", "win")
    VID_FIELD_NUMBER: _ClassVar[int]
    ATK_FIELD_NUMBER: _ClassVar[int]
    DEF_FIELD_NUMBER: _ClassVar[int]
    WIN_FIELD_NUMBER: _ClassVar[int]
    vid: int
    atk: _containers.RepeatedCompositeFieldContainer[pb_unit]
    win: bool
    def __init__(self, vid: _Optional[int] = ..., atk: _Optional[_Iterable[_Union[pb_unit, _Mapping]]] = ..., win: _Optional[bool] = ..., **kwargs) -> None: ...

class pb_wvideo(_message.Message):
    __slots__ = ("atk", "frames", "hurts", "win")
    ATK_FIELD_NUMBER: _ClassVar[int]
    DEF_FIELD_NUMBER: _ClassVar[int]
    FRAMES_FIELD_NUMBER: _ClassVar[int]
    HURTS_FIELD_NUMBER: _ClassVar[int]
    WIN_FIELD_NUMBER: _ClassVar[int]
    atk: _containers.RepeatedCompositeFieldContainer[pb_unit]
    frames: _containers.RepeatedScalarFieldContainer[bytes]
    hurts: _containers.RepeatedCompositeFieldContainer[pb_hurts]
    win: bool
    def __init__(self, atk: _Optional[_Iterable[_Union[pb_unit, _Mapping]]] = ..., frames: _Optional[_Iterable[bytes]] = ..., hurts: _Optional[_Iterable[_Union[pb_hurts, _Mapping]]] = ..., win: _Optional[bool] = ..., **kwargs) -> None: ...

class pb_wscore(_message.Message):
    __slots__ = ("score", "delta", "king")
    SCORE_FIELD_NUMBER: _ClassVar[int]
    DELTA_FIELD_NUMBER: _ClassVar[int]
    KING_FIELD_NUMBER: _ClassVar[int]
    score: int
    delta: int
    king: bool
    def __init__(self, score: _Optional[int] = ..., delta: _Optional[int] = ..., king: _Optional[bool] = ...) -> None: ...

class pb_wcamp(_message.Message):
    __slots__ = ("camp",)
    CAMP_FIELD_NUMBER: _ClassVar[int]
    camp: _containers.RepeatedCompositeFieldContainer[pb_unit]
    def __init__(self, camp: _Optional[_Iterable[_Union[pb_unit, _Mapping]]] = ...) -> None: ...

class pb_wloger(_message.Message):
    __slots__ = ("vid", "mbr", "time", "atk", "win", "delta")
    VID_FIELD_NUMBER: _ClassVar[int]
    MBR_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    ATK_FIELD_NUMBER: _ClassVar[int]
    WIN_FIELD_NUMBER: _ClassVar[int]
    DELTA_FIELD_NUMBER: _ClassVar[int]
    vid: int
    mbr: pb_wmbr
    time: int
    atk: bool
    win: bool
    delta: int
    def __init__(self, vid: _Optional[int] = ..., mbr: _Optional[_Union[pb_wmbr, _Mapping]] = ..., time: _Optional[int] = ..., atk: _Optional[bool] = ..., win: _Optional[bool] = ..., delta: _Optional[int] = ...) -> None: ...

class pb_pvideo(_message.Message):
    __slots__ = ("id", "atk", "win", "frames", "ascore", "dscore", "adelta", "ddelta", "hurts", "rewards", "select")
    ID_FIELD_NUMBER: _ClassVar[int]
    ATK_FIELD_NUMBER: _ClassVar[int]
    DEF_FIELD_NUMBER: _ClassVar[int]
    WIN_FIELD_NUMBER: _ClassVar[int]
    FRAMES_FIELD_NUMBER: _ClassVar[int]
    ASCORE_FIELD_NUMBER: _ClassVar[int]
    DSCORE_FIELD_NUMBER: _ClassVar[int]
    ADELTA_FIELD_NUMBER: _ClassVar[int]
    DDELTA_FIELD_NUMBER: _ClassVar[int]
    HURTS_FIELD_NUMBER: _ClassVar[int]
    REWARDS_FIELD_NUMBER: _ClassVar[int]
    SELECT_FIELD_NUMBER: _ClassVar[int]
    id: int
    atk: pb_pmbr
    win: bool
    frames: _containers.RepeatedScalarFieldContainer[bytes]
    ascore: int
    dscore: int
    adelta: int
    ddelta: int
    hurts: _containers.RepeatedCompositeFieldContainer[pb_hurts]
    rewards: _containers.RepeatedCompositeFieldContainer[pb_bag]
    select: int
    def __init__(self, id: _Optional[int] = ..., atk: _Optional[_Union[pb_pmbr, _Mapping]] = ..., win: _Optional[bool] = ..., frames: _Optional[_Iterable[bytes]] = ..., ascore: _Optional[int] = ..., dscore: _Optional[int] = ..., adelta: _Optional[int] = ..., ddelta: _Optional[int] = ..., hurts: _Optional[_Iterable[_Union[pb_hurts, _Mapping]]] = ..., rewards: _Optional[_Iterable[_Union[pb_bag, _Mapping]]] = ..., select: _Optional[int] = ..., **kwargs) -> None: ...

class pb_p3pvideo(_message.Message):
    __slots__ = ("atk", "win", "frames", "hurts", "ascore", "dscore", "adelta", "ddelta", "rewards", "select")
    ATK_FIELD_NUMBER: _ClassVar[int]
    DEF_FIELD_NUMBER: _ClassVar[int]
    WIN_FIELD_NUMBER: _ClassVar[int]
    FRAMES_FIELD_NUMBER: _ClassVar[int]
    HURTS_FIELD_NUMBER: _ClassVar[int]
    ASCORE_FIELD_NUMBER: _ClassVar[int]
    DSCORE_FIELD_NUMBER: _ClassVar[int]
    ADELTA_FIELD_NUMBER: _ClassVar[int]
    DDELTA_FIELD_NUMBER: _ClassVar[int]
    REWARDS_FIELD_NUMBER: _ClassVar[int]
    SELECT_FIELD_NUMBER: _ClassVar[int]
    atk: pb_p3pmbr
    win: bool
    frames: _containers.RepeatedScalarFieldContainer[bytes]
    hurts: _containers.RepeatedCompositeFieldContainer[pb_hurts]
    ascore: int
    dscore: int
    adelta: int
    ddelta: int
    rewards: _containers.RepeatedCompositeFieldContainer[pb_bag]
    select: int
    def __init__(self, atk: _Optional[_Union[pb_p3pmbr, _Mapping]] = ..., win: _Optional[bool] = ..., frames: _Optional[_Iterable[bytes]] = ..., hurts: _Optional[_Iterable[_Union[pb_hurts, _Mapping]]] = ..., ascore: _Optional[int] = ..., dscore: _Optional[int] = ..., adelta: _Optional[int] = ..., ddelta: _Optional[int] = ..., rewards: _Optional[_Iterable[_Union[pb_bag, _Mapping]]] = ..., select: _Optional[int] = ..., **kwargs) -> None: ...

class pb_htask_info(_message.Message):
    __slots__ = ("tid", "hids", "heads")
    TID_FIELD_NUMBER: _ClassVar[int]
    HIDS_FIELD_NUMBER: _ClassVar[int]
    HEADS_FIELD_NUMBER: _ClassVar[int]
    tid: int
    hids: _containers.RepeatedScalarFieldContainer[int]
    heads: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, tid: _Optional[int] = ..., hids: _Optional[_Iterable[int]] = ..., heads: _Optional[_Iterable[int]] = ...) -> None: ...

class pb_htask_cond(_message.Message):
    __slots__ = ("type", "faction")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    FACTION_FIELD_NUMBER: _ClassVar[int]
    type: int
    faction: int
    def __init__(self, type: _Optional[int] = ..., faction: _Optional[int] = ...) -> None: ...

class pb_htask_sync(_message.Message):
    __slots__ = ("cd", "tasks")
    CD_FIELD_NUMBER: _ClassVar[int]
    TASKS_FIELD_NUMBER: _ClassVar[int]
    cd: int
    tasks: _containers.RepeatedCompositeFieldContainer[pb_htask]
    def __init__(self, cd: _Optional[int] = ..., tasks: _Optional[_Iterable[_Union[pb_htask, _Mapping]]] = ...) -> None: ...

class pb_htask(_message.Message):
    __slots__ = ("tid", "id", "cd", "heroes", "reward", "conds", "power", "lock", "nameid", "heads")
    TID_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    CD_FIELD_NUMBER: _ClassVar[int]
    HEROES_FIELD_NUMBER: _ClassVar[int]
    REWARD_FIELD_NUMBER: _ClassVar[int]
    CONDS_FIELD_NUMBER: _ClassVar[int]
    POWER_FIELD_NUMBER: _ClassVar[int]
    LOCK_FIELD_NUMBER: _ClassVar[int]
    NAMEID_FIELD_NUMBER: _ClassVar[int]
    HEADS_FIELD_NUMBER: _ClassVar[int]
    tid: int
    id: int
    cd: int
    heroes: _containers.RepeatedCompositeFieldContainer[pb_unit]
    reward: pb_bag
    conds: _containers.RepeatedCompositeFieldContainer[pb_htask_cond]
    power: int
    lock: int
    nameid: int
    heads: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, tid: _Optional[int] = ..., id: _Optional[int] = ..., cd: _Optional[int] = ..., heroes: _Optional[_Iterable[_Union[pb_unit, _Mapping]]] = ..., reward: _Optional[_Union[pb_bag, _Mapping]] = ..., conds: _Optional[_Iterable[_Union[pb_htask_cond, _Mapping]]] = ..., power: _Optional[int] = ..., lock: _Optional[int] = ..., nameid: _Optional[int] = ..., heads: _Optional[_Iterable[int]] = ...) -> None: ...

class pb_evideo(_message.Message):
    __slots__ = ("frames", "win", "reward", "camp", "hurts")
    FRAMES_FIELD_NUMBER: _ClassVar[int]
    WIN_FIELD_NUMBER: _ClassVar[int]
    REWARD_FIELD_NUMBER: _ClassVar[int]
    CAMP_FIELD_NUMBER: _ClassVar[int]
    HURTS_FIELD_NUMBER: _ClassVar[int]
    frames: _containers.RepeatedScalarFieldContainer[bytes]
    win: bool
    reward: pb_bag
    camp: _containers.RepeatedCompositeFieldContainer[pb_unit]
    hurts: _containers.RepeatedCompositeFieldContainer[pb_hurts]
    def __init__(self, frames: _Optional[_Iterable[bytes]] = ..., win: _Optional[bool] = ..., reward: _Optional[_Union[pb_bag, _Mapping]] = ..., camp: _Optional[_Iterable[_Union[pb_unit, _Mapping]]] = ..., hurts: _Optional[_Iterable[_Union[pb_hurts, _Mapping]]] = ...) -> None: ...

class pb_hurts(_message.Message):
    __slots__ = ("pos", "value", "heal", "alive")
    POS_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    HEAL_FIELD_NUMBER: _ClassVar[int]
    ALIVE_FIELD_NUMBER: _ClassVar[int]
    pos: int
    value: int
    heal: int
    alive: bool
    def __init__(self, pos: _Optional[int] = ..., value: _Optional[int] = ..., heal: _Optional[int] = ..., alive: _Optional[bool] = ...) -> None: ...

class pb_alogin(_message.Message):
    __slots__ = ("flag", "cd", "idx", "num", "cd2", "first")
    FLAG_FIELD_NUMBER: _ClassVar[int]
    CD_FIELD_NUMBER: _ClassVar[int]
    IDX_FIELD_NUMBER: _ClassVar[int]
    NUM_FIELD_NUMBER: _ClassVar[int]
    CD2_FIELD_NUMBER: _ClassVar[int]
    FIRST_FIELD_NUMBER: _ClassVar[int]
    flag: str
    cd: int
    idx: int
    num: int
    cd2: int
    first: int
    def __init__(self, flag: _Optional[str] = ..., cd: _Optional[int] = ..., idx: _Optional[int] = ..., num: _Optional[int] = ..., cd2: _Optional[int] = ..., first: _Optional[int] = ...) -> None: ...

class pb_act(_message.Message):
    __slots__ = ("id", "status", "cd", "limits", "read", "next", "loop", "bomb", "monopoly", "code", "limits2", "bir", "kv", "grow", "remove")
    ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    CD_FIELD_NUMBER: _ClassVar[int]
    LIMITS_FIELD_NUMBER: _ClassVar[int]
    READ_FIELD_NUMBER: _ClassVar[int]
    NEXT_FIELD_NUMBER: _ClassVar[int]
    LOOP_FIELD_NUMBER: _ClassVar[int]
    BOMB_FIELD_NUMBER: _ClassVar[int]
    MONOPOLY_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    LIMITS2_FIELD_NUMBER: _ClassVar[int]
    BIR_FIELD_NUMBER: _ClassVar[int]
    KV_FIELD_NUMBER: _ClassVar[int]
    GROW_FIELD_NUMBER: _ClassVar[int]
    REMOVE_FIELD_NUMBER: _ClassVar[int]
    id: int
    status: int
    cd: int
    limits: int
    read: int
    next: int
    loop: int
    bomb: int
    monopoly: pb_monopoly
    code: str
    limits2: int
    bir: int
    kv: pb_kvs
    grow: _containers.RepeatedCompositeFieldContainer[pb_growup]
    remove: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, id: _Optional[int] = ..., status: _Optional[int] = ..., cd: _Optional[int] = ..., limits: _Optional[int] = ..., read: _Optional[int] = ..., next: _Optional[int] = ..., loop: _Optional[int] = ..., bomb: _Optional[int] = ..., monopoly: _Optional[_Union[pb_monopoly, _Mapping]] = ..., code: _Optional[str] = ..., limits2: _Optional[int] = ..., bir: _Optional[int] = ..., kv: _Optional[_Union[pb_kvs, _Mapping]] = ..., grow: _Optional[_Iterable[_Union[pb_growup, _Mapping]]] = ..., remove: _Optional[_Iterable[int]] = ...) -> None: ...

class pb_qstar(_message.Message):
    __slots__ = ("uid", "name", "logo", "score")
    UID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    LOGO_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    uid: int
    name: str
    logo: int
    score: int
    def __init__(self, uid: _Optional[int] = ..., name: _Optional[str] = ..., logo: _Optional[int] = ..., score: _Optional[int] = ...) -> None: ...

class pb_monopoly(_message.Message):
    __slots__ = ("pos", "lv", "next_event", "star")
    POS_FIELD_NUMBER: _ClassVar[int]
    LV_FIELD_NUMBER: _ClassVar[int]
    NEXT_EVENT_FIELD_NUMBER: _ClassVar[int]
    STAR_FIELD_NUMBER: _ClassVar[int]
    pos: int
    lv: _containers.RepeatedScalarFieldContainer[int]
    next_event: int
    star: int
    def __init__(self, pos: _Optional[int] = ..., lv: _Optional[_Iterable[int]] = ..., next_event: _Optional[int] = ..., star: _Optional[int] = ...) -> None: ...

class pb_monopoly_step(_message.Message):
    __slots__ = ("id", "reward", "star", "event", "cards", "op_id")
    ID_FIELD_NUMBER: _ClassVar[int]
    REWARD_FIELD_NUMBER: _ClassVar[int]
    STAR_FIELD_NUMBER: _ClassVar[int]
    EVENT_FIELD_NUMBER: _ClassVar[int]
    CARDS_FIELD_NUMBER: _ClassVar[int]
    OP_ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    reward: _containers.RepeatedCompositeFieldContainer[pb_item]
    star: int
    event: int
    cards: _containers.RepeatedScalarFieldContainer[int]
    op_id: int
    def __init__(self, id: _Optional[int] = ..., reward: _Optional[_Iterable[_Union[pb_item, _Mapping]]] = ..., star: _Optional[int] = ..., event: _Optional[int] = ..., cards: _Optional[_Iterable[int]] = ..., op_id: _Optional[int] = ...) -> None: ...

class pb_dice_sweep(_message.Message):
    __slots__ = ("type", "steps", "num1", "num2")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    STEPS_FIELD_NUMBER: _ClassVar[int]
    NUM1_FIELD_NUMBER: _ClassVar[int]
    NUM2_FIELD_NUMBER: _ClassVar[int]
    type: int
    steps: _containers.RepeatedCompositeFieldContainer[pb_monopoly_step]
    num1: int
    num2: int
    def __init__(self, type: _Optional[int] = ..., steps: _Optional[_Iterable[_Union[pb_monopoly_step, _Mapping]]] = ..., num1: _Optional[int] = ..., num2: _Optional[int] = ...) -> None: ...

class pb_sact_item(_message.Message):
    __slots__ = ("id", "cd", "bomb", "limits", "next", "maze", "spec", "log", "reward")
    ID_FIELD_NUMBER: _ClassVar[int]
    CD_FIELD_NUMBER: _ClassVar[int]
    BOMB_FIELD_NUMBER: _ClassVar[int]
    LIMITS_FIELD_NUMBER: _ClassVar[int]
    NEXT_FIELD_NUMBER: _ClassVar[int]
    MAZE_FIELD_NUMBER: _ClassVar[int]
    SPEC_FIELD_NUMBER: _ClassVar[int]
    LOG_FIELD_NUMBER: _ClassVar[int]
    REWARD_FIELD_NUMBER: _ClassVar[int]
    id: int
    cd: int
    bomb: int
    limits: int
    next: int
    maze: _containers.RepeatedCompositeFieldContainer[pb_sact_maze]
    spec: int
    log: _containers.RepeatedCompositeFieldContainer[pb_kv]
    reward: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, id: _Optional[int] = ..., cd: _Optional[int] = ..., bomb: _Optional[int] = ..., limits: _Optional[int] = ..., next: _Optional[int] = ..., maze: _Optional[_Iterable[_Union[pb_sact_maze, _Mapping]]] = ..., spec: _Optional[int] = ..., log: _Optional[_Iterable[_Union[pb_kv, _Mapping]]] = ..., reward: _Optional[_Iterable[int]] = ...) -> None: ...

class pb_rabbit(_message.Message):
    __slots__ = ("type", "poses")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    POSES_FIELD_NUMBER: _ClassVar[int]
    type: int
    poses: _containers.RepeatedCompositeFieldContainer[pb_kv]
    def __init__(self, type: _Optional[int] = ..., poses: _Optional[_Iterable[_Union[pb_kv, _Mapping]]] = ...) -> None: ...

class pb_ract_item(_message.Message):
    __slots__ = ("id", "rewards", "item", "day", "cd")
    ID_FIELD_NUMBER: _ClassVar[int]
    REWARDS_FIELD_NUMBER: _ClassVar[int]
    ITEM_FIELD_NUMBER: _ClassVar[int]
    DAY_FIELD_NUMBER: _ClassVar[int]
    CD_FIELD_NUMBER: _ClassVar[int]
    id: int
    rewards: _containers.RepeatedScalarFieldContainer[int]
    item: _containers.RepeatedCompositeFieldContainer[pb_item]
    day: int
    cd: int
    def __init__(self, id: _Optional[int] = ..., rewards: _Optional[_Iterable[int]] = ..., item: _Optional[_Iterable[_Union[pb_item, _Mapping]]] = ..., day: _Optional[int] = ..., cd: _Optional[int] = ...) -> None: ...

class pb_sact_maze(_message.Message):
    __slots__ = ("pos", "id", "rewards", "num", "ceils")
    POS_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    REWARDS_FIELD_NUMBER: _ClassVar[int]
    NUM_FIELD_NUMBER: _ClassVar[int]
    CEILS_FIELD_NUMBER: _ClassVar[int]
    pos: int
    id: int
    rewards: pb_bag
    num: int
    ceils: _containers.RepeatedCompositeFieldContainer[pb_ceil]
    def __init__(self, pos: _Optional[int] = ..., id: _Optional[int] = ..., rewards: _Optional[_Union[pb_bag, _Mapping]] = ..., num: _Optional[int] = ..., ceils: _Optional[_Iterable[_Union[pb_ceil, _Mapping]]] = ...) -> None: ...

class pb_sact_log(_message.Message):
    __slots__ = ("time", "result")
    TIME_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    time: int
    result: int
    def __init__(self, time: _Optional[int] = ..., result: _Optional[int] = ...) -> None: ...

class pb_ceil(_message.Message):
    __slots__ = ("id", "type", "rewards", "cd")
    ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    REWARDS_FIELD_NUMBER: _ClassVar[int]
    CD_FIELD_NUMBER: _ClassVar[int]
    id: int
    type: int
    rewards: pb_bag
    cd: int
    def __init__(self, id: _Optional[int] = ..., type: _Optional[int] = ..., rewards: _Optional[_Union[pb_bag, _Mapping]] = ..., cd: _Optional[int] = ...) -> None: ...

class pb_mact(_message.Message):
    __slots__ = ("cd", "war", "htask", "hmerge", "space_st", "brave", "status", "hmerge2", "high_casino")
    CD_FIELD_NUMBER: _ClassVar[int]
    WAR_FIELD_NUMBER: _ClassVar[int]
    HTASK_FIELD_NUMBER: _ClassVar[int]
    HMERGE_FIELD_NUMBER: _ClassVar[int]
    SPACE_ST_FIELD_NUMBER: _ClassVar[int]
    BRAVE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    HMERGE2_FIELD_NUMBER: _ClassVar[int]
    HIGH_CASINO_FIELD_NUMBER: _ClassVar[int]
    cd: int
    war: _containers.RepeatedCompositeFieldContainer[pb_item]
    htask: _containers.RepeatedCompositeFieldContainer[pb_item]
    hmerge: _containers.RepeatedCompositeFieldContainer[pb_item]
    space_st: int
    brave: _containers.RepeatedCompositeFieldContainer[pb_item]
    status: int
    hmerge2: _containers.RepeatedCompositeFieldContainer[pb_item]
    high_casino: _containers.RepeatedCompositeFieldContainer[pb_item]
    def __init__(self, cd: _Optional[int] = ..., war: _Optional[_Iterable[_Union[pb_item, _Mapping]]] = ..., htask: _Optional[_Iterable[_Union[pb_item, _Mapping]]] = ..., hmerge: _Optional[_Iterable[_Union[pb_item, _Mapping]]] = ..., space_st: _Optional[int] = ..., brave: _Optional[_Iterable[_Union[pb_item, _Mapping]]] = ..., status: _Optional[int] = ..., hmerge2: _Optional[_Iterable[_Union[pb_item, _Mapping]]] = ..., high_casino: _Optional[_Iterable[_Union[pb_item, _Mapping]]] = ...) -> None: ...

class pb_task(_message.Message):
    __slots__ = ("id", "count", "is_claim")
    ID_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    IS_CLAIM_FIELD_NUMBER: _ClassVar[int]
    id: int
    count: int
    is_claim: int
    def __init__(self, id: _Optional[int] = ..., count: _Optional[int] = ..., is_claim: _Optional[int] = ...) -> None: ...

class pb_online(_message.Message):
    __slots__ = ("id", "cd")
    ID_FIELD_NUMBER: _ClassVar[int]
    CD_FIELD_NUMBER: _ClassVar[int]
    id: int
    cd: int
    def __init__(self, id: _Optional[int] = ..., cd: _Optional[int] = ...) -> None: ...

class pb_sachieve(_message.Message):
    __slots__ = ("num", "id", "curnum")
    NUM_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    CURNUM_FIELD_NUMBER: _ClassVar[int]
    num: _containers.RepeatedScalarFieldContainer[int]
    id: _containers.RepeatedScalarFieldContainer[int]
    curnum: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, num: _Optional[_Iterable[int]] = ..., id: _Optional[_Iterable[int]] = ..., curnum: _Optional[_Iterable[int]] = ...) -> None: ...

class pb_hmarket(_message.Message):
    __slots__ = ("id", "num", "cd")
    ID_FIELD_NUMBER: _ClassVar[int]
    NUM_FIELD_NUMBER: _ClassVar[int]
    CD_FIELD_NUMBER: _ClassVar[int]
    id: int
    num: int
    cd: int
    def __init__(self, id: _Optional[int] = ..., num: _Optional[int] = ..., cd: _Optional[int] = ...) -> None: ...

class pb_gmarket(_message.Message):
    __slots__ = ("id", "num", "gid")
    ID_FIELD_NUMBER: _ClassVar[int]
    NUM_FIELD_NUMBER: _ClassVar[int]
    GID_FIELD_NUMBER: _ClassVar[int]
    id: int
    num: int
    gid: int
    def __init__(self, id: _Optional[int] = ..., num: _Optional[int] = ..., gid: _Optional[int] = ...) -> None: ...

class pb_gvrank(_message.Message):
    __slots__ = ("uid", "name", "lv", "logo", "hurt", "reward", "border")
    UID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    LV_FIELD_NUMBER: _ClassVar[int]
    LOGO_FIELD_NUMBER: _ClassVar[int]
    HURT_FIELD_NUMBER: _ClassVar[int]
    REWARD_FIELD_NUMBER: _ClassVar[int]
    BORDER_FIELD_NUMBER: _ClassVar[int]
    uid: int
    name: str
    lv: int
    logo: int
    hurt: int
    reward: pb_bag
    border: int
    def __init__(self, uid: _Optional[int] = ..., name: _Optional[str] = ..., lv: _Optional[int] = ..., logo: _Optional[int] = ..., hurt: _Optional[int] = ..., reward: _Optional[_Union[pb_bag, _Mapping]] = ..., border: _Optional[int] = ...) -> None: ...

class pb_gvrank_donate(_message.Message):
    __slots__ = ("name", "lv", "logo", "num")
    NAME_FIELD_NUMBER: _ClassVar[int]
    LV_FIELD_NUMBER: _ClassVar[int]
    LOGO_FIELD_NUMBER: _ClassVar[int]
    NUM_FIELD_NUMBER: _ClassVar[int]
    name: str
    lv: int
    logo: int
    num: int
    def __init__(self, name: _Optional[str] = ..., lv: _Optional[int] = ..., logo: _Optional[int] = ..., num: _Optional[int] = ...) -> None: ...

class pb_bboss(_message.Message):
    __slots__ = ("uid", "name", "lv", "logo", "hurt", "sid")
    UID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    LV_FIELD_NUMBER: _ClassVar[int]
    LOGO_FIELD_NUMBER: _ClassVar[int]
    HURT_FIELD_NUMBER: _ClassVar[int]
    SID_FIELD_NUMBER: _ClassVar[int]
    uid: int
    name: str
    lv: int
    logo: int
    hurt: int
    sid: int
    def __init__(self, uid: _Optional[int] = ..., name: _Optional[str] = ..., lv: _Optional[int] = ..., logo: _Optional[int] = ..., hurt: _Optional[int] = ..., sid: _Optional[int] = ...) -> None: ...

class pb_gskl(_message.Message):
    __slots__ = ("id", "lv")
    ID_FIELD_NUMBER: _ClassVar[int]
    LV_FIELD_NUMBER: _ClassVar[int]
    id: int
    lv: int
    def __init__(self, id: _Optional[int] = ..., lv: _Optional[int] = ...) -> None: ...

class pb_bunit(_message.Message):
    __slots__ = ("hid", "id", "lv", "star", "hpp", "pos", "wake", "revive", "skin", "flag", "qlv", "core", "faith_lv")
    HID_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    LV_FIELD_NUMBER: _ClassVar[int]
    STAR_FIELD_NUMBER: _ClassVar[int]
    HPP_FIELD_NUMBER: _ClassVar[int]
    POS_FIELD_NUMBER: _ClassVar[int]
    WAKE_FIELD_NUMBER: _ClassVar[int]
    REVIVE_FIELD_NUMBER: _ClassVar[int]
    SKIN_FIELD_NUMBER: _ClassVar[int]
    FLAG_FIELD_NUMBER: _ClassVar[int]
    QLV_FIELD_NUMBER: _ClassVar[int]
    CORE_FIELD_NUMBER: _ClassVar[int]
    FAITH_LV_FIELD_NUMBER: _ClassVar[int]
    hid: int
    id: int
    lv: int
    star: int
    hpp: int
    pos: int
    wake: int
    revive: int
    skin: int
    flag: int
    qlv: int
    core: int
    faith_lv: int
    def __init__(self, hid: _Optional[int] = ..., id: _Optional[int] = ..., lv: _Optional[int] = ..., star: _Optional[int] = ..., hpp: _Optional[int] = ..., pos: _Optional[int] = ..., wake: _Optional[int] = ..., revive: _Optional[int] = ..., skin: _Optional[int] = ..., flag: _Optional[int] = ..., qlv: _Optional[int] = ..., core: _Optional[int] = ..., faith_lv: _Optional[int] = ...) -> None: ...

class pb_benemy(_message.Message):
    __slots__ = ("logo", "lv", "name", "power", "sid", "camp", "border")
    LOGO_FIELD_NUMBER: _ClassVar[int]
    LV_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    POWER_FIELD_NUMBER: _ClassVar[int]
    SID_FIELD_NUMBER: _ClassVar[int]
    CAMP_FIELD_NUMBER: _ClassVar[int]
    BORDER_FIELD_NUMBER: _ClassVar[int]
    logo: int
    lv: int
    name: str
    power: int
    sid: int
    camp: _containers.RepeatedCompositeFieldContainer[pb_bunit]
    border: int
    def __init__(self, logo: _Optional[int] = ..., lv: _Optional[int] = ..., name: _Optional[str] = ..., power: _Optional[int] = ..., sid: _Optional[int] = ..., camp: _Optional[_Iterable[_Union[pb_bunit, _Mapping]]] = ..., border: _Optional[int] = ...) -> None: ...

class pb_ngwshold(_message.Message):
    __slots__ = ("left", "total", "buffs", "power")
    LEFT_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    BUFFS_FIELD_NUMBER: _ClassVar[int]
    POWER_FIELD_NUMBER: _ClassVar[int]
    left: int
    total: int
    buffs: _containers.RepeatedCompositeFieldContainer[pb_ngwbuff]
    power: int
    def __init__(self, left: _Optional[int] = ..., total: _Optional[int] = ..., buffs: _Optional[_Iterable[_Union[pb_ngwbuff, _Mapping]]] = ..., power: _Optional[int] = ...) -> None: ...

class pb_ngwrank(_message.Message):
    __slots__ = ("gid", "score", "seg", "time", "logo", "name", "power")
    GID_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    SEG_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    LOGO_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    POWER_FIELD_NUMBER: _ClassVar[int]
    gid: int
    score: int
    seg: int
    time: int
    logo: int
    name: str
    power: int
    def __init__(self, gid: _Optional[int] = ..., score: _Optional[int] = ..., seg: _Optional[int] = ..., time: _Optional[int] = ..., logo: _Optional[int] = ..., name: _Optional[str] = ..., power: _Optional[int] = ...) -> None: ...

class pb_ngwprank(_message.Message):
    __slots__ = ("uid", "name", "lv", "logo", "lbox", "gname", "score", "time", "power", "daily")
    UID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    LV_FIELD_NUMBER: _ClassVar[int]
    LOGO_FIELD_NUMBER: _ClassVar[int]
    LBOX_FIELD_NUMBER: _ClassVar[int]
    GNAME_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    POWER_FIELD_NUMBER: _ClassVar[int]
    DAILY_FIELD_NUMBER: _ClassVar[int]
    uid: int
    name: str
    lv: int
    logo: int
    lbox: int
    gname: str
    score: int
    time: int
    power: int
    daily: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, uid: _Optional[int] = ..., name: _Optional[str] = ..., lv: _Optional[int] = ..., logo: _Optional[int] = ..., lbox: _Optional[int] = ..., gname: _Optional[str] = ..., score: _Optional[int] = ..., time: _Optional[int] = ..., power: _Optional[int] = ..., daily: _Optional[_Iterable[int]] = ...) -> None: ...

class pb_ngwbuff(_message.Message):
    __slots__ = ("id", "num")
    ID_FIELD_NUMBER: _ClassVar[int]
    NUM_FIELD_NUMBER: _ClassVar[int]
    id: int
    num: int
    def __init__(self, id: _Optional[int] = ..., num: _Optional[int] = ...) -> None: ...

class pb_ngwmbr(_message.Message):
    __slots__ = ("idx", "logo", "gname", "power", "lv", "lbox", "unit", "uid", "gid", "win")
    IDX_FIELD_NUMBER: _ClassVar[int]
    LOGO_FIELD_NUMBER: _ClassVar[int]
    GNAME_FIELD_NUMBER: _ClassVar[int]
    POWER_FIELD_NUMBER: _ClassVar[int]
    LV_FIELD_NUMBER: _ClassVar[int]
    LBOX_FIELD_NUMBER: _ClassVar[int]
    UNIT_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    GID_FIELD_NUMBER: _ClassVar[int]
    WIN_FIELD_NUMBER: _ClassVar[int]
    idx: int
    logo: int
    gname: str
    power: int
    lv: int
    lbox: int
    unit: _containers.RepeatedCompositeFieldContainer[pb_unit]
    uid: int
    gid: int
    win: int
    def __init__(self, idx: _Optional[int] = ..., logo: _Optional[int] = ..., gname: _Optional[str] = ..., power: _Optional[int] = ..., lv: _Optional[int] = ..., lbox: _Optional[int] = ..., unit: _Optional[_Iterable[_Union[pb_unit, _Mapping]]] = ..., uid: _Optional[int] = ..., gid: _Optional[int] = ..., win: _Optional[int] = ...) -> None: ...

class pb_clink(_message.Message):
    __slots__ = ("cd", "atk", "win", "vid")
    CD_FIELD_NUMBER: _ClassVar[int]
    ATK_FIELD_NUMBER: _ClassVar[int]
    DEF_FIELD_NUMBER: _ClassVar[int]
    WIN_FIELD_NUMBER: _ClassVar[int]
    VID_FIELD_NUMBER: _ClassVar[int]
    cd: int
    atk: int
    win: int
    vid: int
    def __init__(self, cd: _Optional[int] = ..., atk: _Optional[int] = ..., win: _Optional[int] = ..., vid: _Optional[int] = ..., **kwargs) -> None: ...

class pb_cgw_info(_message.Message):
    __slots__ = ("id", "logo", "power", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    LOGO_FIELD_NUMBER: _ClassVar[int]
    POWER_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: int
    logo: int
    power: int
    name: str
    def __init__(self, id: _Optional[int] = ..., logo: _Optional[int] = ..., power: _Optional[int] = ..., name: _Optional[str] = ...) -> None: ...

class pb_cgw_mbr(_message.Message):
    __slots__ = ("uid", "logo", "lv", "lbox", "name", "camp")
    UID_FIELD_NUMBER: _ClassVar[int]
    LOGO_FIELD_NUMBER: _ClassVar[int]
    LV_FIELD_NUMBER: _ClassVar[int]
    LBOX_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CAMP_FIELD_NUMBER: _ClassVar[int]
    uid: int
    logo: int
    lv: int
    lbox: int
    name: str
    camp: _containers.RepeatedCompositeFieldContainer[pb_unit]
    def __init__(self, uid: _Optional[int] = ..., logo: _Optional[int] = ..., lv: _Optional[int] = ..., lbox: _Optional[int] = ..., name: _Optional[str] = ..., camp: _Optional[_Iterable[_Union[pb_unit, _Mapping]]] = ...) -> None: ...

class pb_cgw_record(_message.Message):
    __slots__ = ("gid", "logo", "vid", "cd", "flag", "power", "name", "atk", "win", "spower")
    GID_FIELD_NUMBER: _ClassVar[int]
    LOGO_FIELD_NUMBER: _ClassVar[int]
    VID_FIELD_NUMBER: _ClassVar[int]
    CD_FIELD_NUMBER: _ClassVar[int]
    FLAG_FIELD_NUMBER: _ClassVar[int]
    POWER_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ATK_FIELD_NUMBER: _ClassVar[int]
    WIN_FIELD_NUMBER: _ClassVar[int]
    SPOWER_FIELD_NUMBER: _ClassVar[int]
    gid: int
    logo: int
    vid: int
    cd: int
    flag: int
    power: int
    name: str
    atk: bool
    win: bool
    spower: int
    def __init__(self, gid: _Optional[int] = ..., logo: _Optional[int] = ..., vid: _Optional[int] = ..., cd: _Optional[int] = ..., flag: _Optional[int] = ..., power: _Optional[int] = ..., name: _Optional[str] = ..., atk: _Optional[bool] = ..., win: _Optional[bool] = ..., spower: _Optional[int] = ...) -> None: ...

class pb_cgw_log(_message.Message):
    __slots__ = ("atk", "win")
    ATK_FIELD_NUMBER: _ClassVar[int]
    DEF_FIELD_NUMBER: _ClassVar[int]
    WIN_FIELD_NUMBER: _ClassVar[int]
    atk: pb_cgw_mbr
    win: bool
    def __init__(self, atk: _Optional[_Union[pb_cgw_mbr, _Mapping]] = ..., win: _Optional[bool] = ..., **kwargs) -> None: ...

class pb_ngw_sweep(_message.Message):
    __slots__ = ("status", "id", "destroy")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    DESTROY_FIELD_NUMBER: _ClassVar[int]
    status: int
    id: int
    destroy: int
    def __init__(self, status: _Optional[int] = ..., id: _Optional[int] = ..., destroy: _Optional[int] = ...) -> None: ...

class pb_cd(_message.Message):
    __slots__ = ("id", "cd")
    ID_FIELD_NUMBER: _ClassVar[int]
    CD_FIELD_NUMBER: _ClassVar[int]
    id: int
    cd: int
    def __init__(self, id: _Optional[int] = ..., cd: _Optional[int] = ...) -> None: ...

class pb_gpvpteam(_message.Message):
    __slots__ = ("leader", "mbrs", "sid", "score", "rank", "power", "name", "need_power", "password", "id", "reg", "enegy", "enggy_cd")
    LEADER_FIELD_NUMBER: _ClassVar[int]
    MBRS_FIELD_NUMBER: _ClassVar[int]
    SID_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    RANK_FIELD_NUMBER: _ClassVar[int]
    POWER_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    NEED_POWER_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    REG_FIELD_NUMBER: _ClassVar[int]
    ENEGY_FIELD_NUMBER: _ClassVar[int]
    ENGGY_CD_FIELD_NUMBER: _ClassVar[int]
    leader: int
    mbrs: _containers.RepeatedCompositeFieldContainer[pb_pmbr]
    sid: int
    score: int
    rank: int
    power: int
    name: str
    need_power: int
    password: str
    id: int
    reg: bool
    enegy: int
    enggy_cd: int
    def __init__(self, leader: _Optional[int] = ..., mbrs: _Optional[_Iterable[_Union[pb_pmbr, _Mapping]]] = ..., sid: _Optional[int] = ..., score: _Optional[int] = ..., rank: _Optional[int] = ..., power: _Optional[int] = ..., name: _Optional[str] = ..., need_power: _Optional[int] = ..., password: _Optional[str] = ..., id: _Optional[int] = ..., reg: _Optional[bool] = ..., enegy: _Optional[int] = ..., enggy_cd: _Optional[int] = ...) -> None: ...

class pb_gpvplog(_message.Message):
    __slots__ = ("log_id", "enemy", "score", "win", "time")
    LOG_ID_FIELD_NUMBER: _ClassVar[int]
    ENEMY_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    WIN_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    log_id: int
    enemy: pb_gpvpteam
    score: int
    win: bool
    time: int
    def __init__(self, log_id: _Optional[int] = ..., enemy: _Optional[_Union[pb_gpvpteam, _Mapping]] = ..., score: _Optional[int] = ..., win: _Optional[bool] = ..., time: _Optional[int] = ...) -> None: ...

class pb_gpvp_wlog(_message.Message):
    __slots__ = ("atk", "wins", "vids")
    ATK_FIELD_NUMBER: _ClassVar[int]
    DEF_FIELD_NUMBER: _ClassVar[int]
    WINS_FIELD_NUMBER: _ClassVar[int]
    VIDS_FIELD_NUMBER: _ClassVar[int]
    atk: pb_gpvpteam
    wins: _containers.RepeatedScalarFieldContainer[bool]
    vids: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, atk: _Optional[_Union[pb_gpvpteam, _Mapping]] = ..., wins: _Optional[_Iterable[bool]] = ..., vids: _Optional[_Iterable[int]] = ..., **kwargs) -> None: ...

class pb_pet(_message.Message):
    __slots__ = ("id", "lv", "star", "skl")
    ID_FIELD_NUMBER: _ClassVar[int]
    LV_FIELD_NUMBER: _ClassVar[int]
    STAR_FIELD_NUMBER: _ClassVar[int]
    SKL_FIELD_NUMBER: _ClassVar[int]
    id: int
    lv: int
    star: int
    skl: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, id: _Optional[int] = ..., lv: _Optional[int] = ..., star: _Optional[int] = ..., skl: _Optional[_Iterable[int]] = ...) -> None: ...

class pb_spkunit(_message.Message):
    __slots__ = ("base", "buf")
    BASE_FIELD_NUMBER: _ClassVar[int]
    BUF_FIELD_NUMBER: _ClassVar[int]
    base: pb_unit
    buf: _containers.RepeatedCompositeFieldContainer[pb_item]
    def __init__(self, base: _Optional[_Union[pb_unit, _Mapping]] = ..., buf: _Optional[_Iterable[_Union[pb_item, _Mapping]]] = ...) -> None: ...

class pb_spkmbr(_message.Message):
    __slots__ = ("uid", "lv", "wave", "time", "logo", "name", "border")
    UID_FIELD_NUMBER: _ClassVar[int]
    LV_FIELD_NUMBER: _ClassVar[int]
    WAVE_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    LOGO_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    BORDER_FIELD_NUMBER: _ClassVar[int]
    uid: int
    lv: int
    wave: int
    time: int
    logo: int
    name: str
    border: int
    def __init__(self, uid: _Optional[int] = ..., lv: _Optional[int] = ..., wave: _Optional[int] = ..., time: _Optional[int] = ..., logo: _Optional[int] = ..., name: _Optional[str] = ..., border: _Optional[int] = ...) -> None: ...

class pb_holy(_message.Message):
    __slots__ = ("id", "pos", "val")
    ID_FIELD_NUMBER: _ClassVar[int]
    POS_FIELD_NUMBER: _ClassVar[int]
    VAL_FIELD_NUMBER: _ClassVar[int]
    id: int
    pos: int
    val: int
    def __init__(self, id: _Optional[int] = ..., pos: _Optional[int] = ..., val: _Optional[int] = ...) -> None: ...

class pb_mine(_message.Message):
    __slots__ = ("id", "pos", "val")
    ID_FIELD_NUMBER: _ClassVar[int]
    POS_FIELD_NUMBER: _ClassVar[int]
    VAL_FIELD_NUMBER: _ClassVar[int]
    id: int
    pos: int
    val: int
    def __init__(self, id: _Optional[int] = ..., pos: _Optional[int] = ..., val: _Optional[int] = ...) -> None: ...

class pb_land(_message.Message):
    __slots__ = ("id", "pos", "cd", "cdk", "dead")
    ID_FIELD_NUMBER: _ClassVar[int]
    POS_FIELD_NUMBER: _ClassVar[int]
    CD_FIELD_NUMBER: _ClassVar[int]
    CDK_FIELD_NUMBER: _ClassVar[int]
    DEAD_FIELD_NUMBER: _ClassVar[int]
    id: int
    pos: int
    cd: int
    cdk: int
    dead: bool
    def __init__(self, id: _Optional[int] = ..., pos: _Optional[int] = ..., cd: _Optional[int] = ..., cdk: _Optional[int] = ..., dead: _Optional[bool] = ...) -> None: ...

class pb_vit(_message.Message):
    __slots__ = ("vit", "buy")
    VIT_FIELD_NUMBER: _ClassVar[int]
    BUY_FIELD_NUMBER: _ClassVar[int]
    vit: int
    buy: int
    def __init__(self, vit: _Optional[int] = ..., buy: _Optional[int] = ...) -> None: ...

class pb_ievent(_message.Message):
    __slots__ = ("id", "cd", "ext", "sid", "reward")
    ID_FIELD_NUMBER: _ClassVar[int]
    CD_FIELD_NUMBER: _ClassVar[int]
    EXT_FIELD_NUMBER: _ClassVar[int]
    SID_FIELD_NUMBER: _ClassVar[int]
    REWARD_FIELD_NUMBER: _ClassVar[int]
    id: int
    cd: int
    ext: str
    sid: int
    reward: pb_bag
    def __init__(self, id: _Optional[int] = ..., cd: _Optional[int] = ..., ext: _Optional[str] = ..., sid: _Optional[int] = ..., reward: _Optional[_Union[pb_bag, _Mapping]] = ...) -> None: ...

class pb_iadt(_message.Message):
    __slots__ = ("dist", "mevts", "pevts", "vit", "vitcd", "reward", "rt", "num")
    DIST_FIELD_NUMBER: _ClassVar[int]
    MEVTS_FIELD_NUMBER: _ClassVar[int]
    PEVTS_FIELD_NUMBER: _ClassVar[int]
    VIT_FIELD_NUMBER: _ClassVar[int]
    VITCD_FIELD_NUMBER: _ClassVar[int]
    REWARD_FIELD_NUMBER: _ClassVar[int]
    RT_FIELD_NUMBER: _ClassVar[int]
    NUM_FIELD_NUMBER: _ClassVar[int]
    dist: int
    mevts: _containers.RepeatedCompositeFieldContainer[pb_ievent]
    pevts: _containers.RepeatedCompositeFieldContainer[pb_ievent]
    vit: int
    vitcd: int
    reward: pb_bag
    rt: int
    num: int
    def __init__(self, dist: _Optional[int] = ..., mevts: _Optional[_Iterable[_Union[pb_ievent, _Mapping]]] = ..., pevts: _Optional[_Iterable[_Union[pb_ievent, _Mapping]]] = ..., vit: _Optional[int] = ..., vitcd: _Optional[int] = ..., reward: _Optional[_Union[pb_bag, _Mapping]] = ..., rt: _Optional[int] = ..., num: _Optional[int] = ...) -> None: ...

class pb_iboat(_message.Message):
    __slots__ = ("name", "exp", "arm", "spd", "skls")
    NAME_FIELD_NUMBER: _ClassVar[int]
    EXP_FIELD_NUMBER: _ClassVar[int]
    ARM_FIELD_NUMBER: _ClassVar[int]
    SPD_FIELD_NUMBER: _ClassVar[int]
    SKLS_FIELD_NUMBER: _ClassVar[int]
    name: str
    exp: int
    arm: int
    spd: int
    skls: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, name: _Optional[str] = ..., exp: _Optional[int] = ..., arm: _Optional[int] = ..., spd: _Optional[int] = ..., skls: _Optional[_Iterable[int]] = ...) -> None: ...

class pb_ipro(_message.Message):
    __slots__ = ("id", "num", "cd")
    ID_FIELD_NUMBER: _ClassVar[int]
    NUM_FIELD_NUMBER: _ClassVar[int]
    CD_FIELD_NUMBER: _ClassVar[int]
    id: int
    num: int
    cd: int
    def __init__(self, id: _Optional[int] = ..., num: _Optional[int] = ..., cd: _Optional[int] = ...) -> None: ...

class pb_locale(_message.Message):
    __slots__ = ("country", "iso", "city")
    COUNTRY_FIELD_NUMBER: _ClassVar[int]
    ISO_FIELD_NUMBER: _ClassVar[int]
    CITY_FIELD_NUMBER: _ClassVar[int]
    country: str
    iso: str
    city: str
    def __init__(self, country: _Optional[str] = ..., iso: _Optional[str] = ..., city: _Optional[str] = ...) -> None: ...

class pb_sact(_message.Message):
    __slots__ = ("acts",)
    ACTS_FIELD_NUMBER: _ClassVar[int]
    acts: _containers.RepeatedCompositeFieldContainer[pb_sact_item]
    def __init__(self, acts: _Optional[_Iterable[_Union[pb_sact_item, _Mapping]]] = ...) -> None: ...

class pb_ract(_message.Message):
    __slots__ = ("acts", "show")
    ACTS_FIELD_NUMBER: _ClassVar[int]
    SHOW_FIELD_NUMBER: _ClassVar[int]
    acts: _containers.RepeatedCompositeFieldContainer[pb_ract_item]
    show: int
    def __init__(self, acts: _Optional[_Iterable[_Union[pb_ract_item, _Mapping]]] = ..., show: _Optional[int] = ...) -> None: ...

class pb_brave_box(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class pb_brave_buff(_message.Message):
    __slots__ = ("id", "num")
    ID_FIELD_NUMBER: _ClassVar[int]
    NUM_FIELD_NUMBER: _ClassVar[int]
    id: int
    num: int
    def __init__(self, id: _Optional[int] = ..., num: _Optional[int] = ...) -> None: ...

class pb_re_sync(_message.Message):
    __slots__ = ("role", "gift_id", "back_gift", "bind_times", "help_times", "back_cd", "bind", "s_tasks", "h_tasks", "cd", "cd2", "applys", "code", "players")
    ROLE_FIELD_NUMBER: _ClassVar[int]
    GIFT_ID_FIELD_NUMBER: _ClassVar[int]
    BACK_GIFT_FIELD_NUMBER: _ClassVar[int]
    BIND_TIMES_FIELD_NUMBER: _ClassVar[int]
    HELP_TIMES_FIELD_NUMBER: _ClassVar[int]
    BACK_CD_FIELD_NUMBER: _ClassVar[int]
    BIND_FIELD_NUMBER: _ClassVar[int]
    S_TASKS_FIELD_NUMBER: _ClassVar[int]
    H_TASKS_FIELD_NUMBER: _ClassVar[int]
    CD_FIELD_NUMBER: _ClassVar[int]
    CD2_FIELD_NUMBER: _ClassVar[int]
    APPLYS_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    PLAYERS_FIELD_NUMBER: _ClassVar[int]
    role: int
    gift_id: int
    back_gift: int
    bind_times: int
    help_times: int
    back_cd: int
    bind: int
    s_tasks: _containers.RepeatedCompositeFieldContainer[pb_re_task]
    h_tasks: _containers.RepeatedCompositeFieldContainer[pb_re_task]
    cd: int
    cd2: int
    applys: _containers.RepeatedCompositeFieldContainer[pb_re_apply]
    code: str
    players: _containers.RepeatedCompositeFieldContainer[pb_re_bind_player]
    def __init__(self, role: _Optional[int] = ..., gift_id: _Optional[int] = ..., back_gift: _Optional[int] = ..., bind_times: _Optional[int] = ..., help_times: _Optional[int] = ..., back_cd: _Optional[int] = ..., bind: _Optional[int] = ..., s_tasks: _Optional[_Iterable[_Union[pb_re_task, _Mapping]]] = ..., h_tasks: _Optional[_Iterable[_Union[pb_re_task, _Mapping]]] = ..., cd: _Optional[int] = ..., cd2: _Optional[int] = ..., applys: _Optional[_Iterable[_Union[pb_re_apply, _Mapping]]] = ..., code: _Optional[str] = ..., players: _Optional[_Iterable[_Union[pb_re_bind_player, _Mapping]]] = ...) -> None: ...

class pb_re_bind_player(_message.Message):
    __slots__ = ("logo", "uid", "name", "bind")
    LOGO_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    BIND_FIELD_NUMBER: _ClassVar[int]
    logo: int
    uid: int
    name: str
    bind: int
    def __init__(self, logo: _Optional[int] = ..., uid: _Optional[int] = ..., name: _Optional[str] = ..., bind: _Optional[int] = ...) -> None: ...

class pb_re_apply(_message.Message):
    __slots__ = ("logo", "uid", "name", "cd")
    LOGO_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CD_FIELD_NUMBER: _ClassVar[int]
    logo: int
    uid: int
    name: str
    cd: int
    def __init__(self, logo: _Optional[int] = ..., uid: _Optional[int] = ..., name: _Optional[str] = ..., cd: _Optional[int] = ...) -> None: ...

class pb_re_task(_message.Message):
    __slots__ = ("id", "num1", "num2")
    ID_FIELD_NUMBER: _ClassVar[int]
    NUM1_FIELD_NUMBER: _ClassVar[int]
    NUM2_FIELD_NUMBER: _ClassVar[int]
    id: int
    num1: int
    num2: int
    def __init__(self, id: _Optional[int] = ..., num1: _Optional[int] = ..., num2: _Optional[int] = ...) -> None: ...

class pb_vbuff(_message.Message):
    __slots__ = ("id", "type")
    ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    id: int
    type: int
    def __init__(self, id: _Optional[int] = ..., type: _Optional[int] = ...) -> None: ...

class pb_stele(_message.Message):
    __slots__ = ("hook", "solo", "crush", "tower", "sealland", "st")
    HOOK_FIELD_NUMBER: _ClassVar[int]
    SOLO_FIELD_NUMBER: _ClassVar[int]
    CRUSH_FIELD_NUMBER: _ClassVar[int]
    TOWER_FIELD_NUMBER: _ClassVar[int]
    SEALLAND_FIELD_NUMBER: _ClassVar[int]
    ST_FIELD_NUMBER: _ClassVar[int]
    hook: int
    solo: int
    crush: int
    tower: int
    sealland: _containers.RepeatedScalarFieldContainer[int]
    st: int
    def __init__(self, hook: _Optional[int] = ..., solo: _Optional[int] = ..., crush: _Optional[int] = ..., tower: _Optional[int] = ..., sealland: _Optional[_Iterable[int]] = ..., st: _Optional[int] = ...) -> None: ...

class pb_midas(_message.Message):
    __slots__ = ("type", "cd", "index")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    CD_FIELD_NUMBER: _ClassVar[int]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    type: int
    cd: int
    index: int
    def __init__(self, type: _Optional[int] = ..., cd: _Optional[int] = ..., index: _Optional[int] = ...) -> None: ...

class pb_gve(_message.Message):
    __slots__ = ("id", "exp", "record", "fight")
    ID_FIELD_NUMBER: _ClassVar[int]
    EXP_FIELD_NUMBER: _ClassVar[int]
    RECORD_FIELD_NUMBER: _ClassVar[int]
    FIGHT_FIELD_NUMBER: _ClassVar[int]
    id: int
    exp: int
    record: _containers.RepeatedScalarFieldContainer[int]
    fight: int
    def __init__(self, id: _Optional[int] = ..., exp: _Optional[int] = ..., record: _Optional[_Iterable[int]] = ..., fight: _Optional[int] = ...) -> None: ...

class pb_gve_rank(_message.Message):
    __slots__ = ("id", "name", "exp", "texp")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    EXP_FIELD_NUMBER: _ClassVar[int]
    TEXP_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    exp: int
    texp: int
    def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ..., exp: _Optional[int] = ..., texp: _Optional[int] = ...) -> None: ...

class pb_act_block(_message.Message):
    __slots__ = ("pos", "eventid")
    POS_FIELD_NUMBER: _ClassVar[int]
    EVENTID_FIELD_NUMBER: _ClassVar[int]
    pos: int
    eventid: int
    def __init__(self, pos: _Optional[int] = ..., eventid: _Optional[int] = ...) -> None: ...

class pb_act_maze(_message.Message):
    __slots__ = ("floor", "events", "heroid", "skill", "skill_lv", "change", "treasures", "buff", "type", "pos", "buy_num", "get_frag")
    FLOOR_FIELD_NUMBER: _ClassVar[int]
    EVENTS_FIELD_NUMBER: _ClassVar[int]
    HEROID_FIELD_NUMBER: _ClassVar[int]
    SKILL_FIELD_NUMBER: _ClassVar[int]
    SKILL_LV_FIELD_NUMBER: _ClassVar[int]
    CHANGE_FIELD_NUMBER: _ClassVar[int]
    TREASURES_FIELD_NUMBER: _ClassVar[int]
    BUFF_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    POS_FIELD_NUMBER: _ClassVar[int]
    BUY_NUM_FIELD_NUMBER: _ClassVar[int]
    GET_FRAG_FIELD_NUMBER: _ClassVar[int]
    floor: int
    events: _containers.RepeatedCompositeFieldContainer[pb_act_block]
    heroid: int
    skill: int
    skill_lv: int
    change: int
    treasures: int
    buff: int
    type: int
    pos: int
    buy_num: int
    get_frag: bool
    def __init__(self, floor: _Optional[int] = ..., events: _Optional[_Iterable[_Union[pb_act_block, _Mapping]]] = ..., heroid: _Optional[int] = ..., skill: _Optional[int] = ..., skill_lv: _Optional[int] = ..., change: _Optional[int] = ..., treasures: _Optional[int] = ..., buff: _Optional[int] = ..., type: _Optional[int] = ..., pos: _Optional[int] = ..., buy_num: _Optional[int] = ..., get_frag: _Optional[bool] = ...) -> None: ...

class pb_ntask(_message.Message):
    __slots__ = ("id", "count", "status", "extra")
    ID_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    EXTRA_FIELD_NUMBER: _ClassVar[int]
    id: int
    count: int
    status: int
    extra: _containers.RepeatedCompositeFieldContainer[pb_nextra]
    def __init__(self, id: _Optional[int] = ..., count: _Optional[int] = ..., status: _Optional[int] = ..., extra: _Optional[_Iterable[_Union[pb_nextra, _Mapping]]] = ...) -> None: ...

class pb_nextra(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, id: _Optional[_Iterable[int]] = ...) -> None: ...

class pb_nt_sync(_message.Message):
    __slots__ = ("type", "value")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    type: int
    value: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, type: _Optional[int] = ..., value: _Optional[_Iterable[int]] = ...) -> None: ...

class pb_room(_message.Message):
    __slots__ = ("id", "pos", "skinid", "hid")
    ID_FIELD_NUMBER: _ClassVar[int]
    POS_FIELD_NUMBER: _ClassVar[int]
    SKINID_FIELD_NUMBER: _ClassVar[int]
    HID_FIELD_NUMBER: _ClassVar[int]
    id: int
    pos: int
    skinid: int
    hid: int
    def __init__(self, id: _Optional[int] = ..., pos: _Optional[int] = ..., skinid: _Optional[int] = ..., hid: _Optional[int] = ...) -> None: ...

class pb_home_land(_message.Message):
    __slots__ = ("land_id", "name", "rooms", "owner")
    LAND_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ROOMS_FIELD_NUMBER: _ClassVar[int]
    OWNER_FIELD_NUMBER: _ClassVar[int]
    land_id: int
    name: str
    rooms: _containers.RepeatedCompositeFieldContainer[pb_room]
    owner: int
    def __init__(self, land_id: _Optional[int] = ..., name: _Optional[str] = ..., rooms: _Optional[_Iterable[_Union[pb_room, _Mapping]]] = ..., owner: _Optional[int] = ...) -> None: ...

class pb_block(_message.Message):
    __slots__ = ("type", "to")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    FROM_FIELD_NUMBER: _ClassVar[int]
    TO_FIELD_NUMBER: _ClassVar[int]
    type: int
    to: int
    def __init__(self, type: _Optional[int] = ..., to: _Optional[int] = ..., **kwargs) -> None: ...

class pb_living(_message.Message):
    __slots__ = ("type", "hid")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    HID_FIELD_NUMBER: _ClassVar[int]
    type: int
    hid: int
    def __init__(self, type: _Optional[int] = ..., hid: _Optional[int] = ...) -> None: ...

class pb_buildings(_message.Message):
    __slots__ = ("id", "pos", "skinid", "collect_time", "store")
    ID_FIELD_NUMBER: _ClassVar[int]
    POS_FIELD_NUMBER: _ClassVar[int]
    SKINID_FIELD_NUMBER: _ClassVar[int]
    COLLECT_TIME_FIELD_NUMBER: _ClassVar[int]
    STORE_FIELD_NUMBER: _ClassVar[int]
    id: int
    pos: int
    skinid: int
    collect_time: int
    store: int
    def __init__(self, id: _Optional[int] = ..., pos: _Optional[int] = ..., skinid: _Optional[int] = ..., collect_time: _Optional[int] = ..., store: _Optional[int] = ...) -> None: ...

class pb_home_roomer(_message.Message):
    __slots__ = ("room_id", "hid", "skinid")
    ROOM_ID_FIELD_NUMBER: _ClassVar[int]
    HID_FIELD_NUMBER: _ClassVar[int]
    SKINID_FIELD_NUMBER: _ClassVar[int]
    room_id: int
    hid: int
    skinid: int
    def __init__(self, room_id: _Optional[int] = ..., hid: _Optional[int] = ..., skinid: _Optional[int] = ...) -> None: ...

class pb_home_heroes(_message.Message):
    __slots__ = ("hid", "land_id", "roomers")
    HID_FIELD_NUMBER: _ClassVar[int]
    LAND_ID_FIELD_NUMBER: _ClassVar[int]
    ROOMERS_FIELD_NUMBER: _ClassVar[int]
    hid: int
    land_id: int
    roomers: _containers.RepeatedCompositeFieldContainer[pb_home_roomer]
    def __init__(self, hid: _Optional[int] = ..., land_id: _Optional[int] = ..., roomers: _Optional[_Iterable[_Union[pb_home_roomer, _Mapping]]] = ...) -> None: ...

class pb_coll(_message.Message):
    __slots__ = ("type", "score", "lv")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    LV_FIELD_NUMBER: _ClassVar[int]
    type: int
    score: int
    lv: int
    def __init__(self, type: _Optional[int] = ..., score: _Optional[int] = ..., lv: _Optional[int] = ...) -> None: ...

class pb_stove(_message.Message):
    __slots__ = ("id", "num", "cd", "qid")
    ID_FIELD_NUMBER: _ClassVar[int]
    NUM_FIELD_NUMBER: _ClassVar[int]
    CD_FIELD_NUMBER: _ClassVar[int]
    QID_FIELD_NUMBER: _ClassVar[int]
    id: int
    num: int
    cd: int
    qid: int
    def __init__(self, id: _Optional[int] = ..., num: _Optional[int] = ..., cd: _Optional[int] = ..., qid: _Optional[int] = ...) -> None: ...

class pb_stove_buy(_message.Message):
    __slots__ = ("id", "num")
    ID_FIELD_NUMBER: _ClassVar[int]
    NUM_FIELD_NUMBER: _ClassVar[int]
    id: int
    num: int
    def __init__(self, id: _Optional[int] = ..., num: _Optional[int] = ...) -> None: ...

class pb_gvm_stone(_message.Message):
    __slots__ = ("bid", "id", "num", "pos")
    BID_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NUM_FIELD_NUMBER: _ClassVar[int]
    POS_FIELD_NUMBER: _ClassVar[int]
    bid: int
    id: int
    num: _containers.RepeatedScalarFieldContainer[int]
    pos: int
    def __init__(self, bid: _Optional[int] = ..., id: _Optional[int] = ..., num: _Optional[_Iterable[int]] = ..., pos: _Optional[int] = ...) -> None: ...

class pb_gvm_map(_message.Message):
    __slots__ = ("id", "buff_num")
    ID_FIELD_NUMBER: _ClassVar[int]
    BUFF_NUM_FIELD_NUMBER: _ClassVar[int]
    id: int
    buff_num: int
    def __init__(self, id: _Optional[int] = ..., buff_num: _Optional[int] = ...) -> None: ...

class pb_gvm_map_node(_message.Message):
    __slots__ = ("id", "state", "cfg_id", "hps")
    ID_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    CFG_ID_FIELD_NUMBER: _ClassVar[int]
    HPS_FIELD_NUMBER: _ClassVar[int]
    id: int
    state: int
    cfg_id: int
    hps: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, id: _Optional[int] = ..., state: _Optional[int] = ..., cfg_id: _Optional[int] = ..., hps: _Optional[_Iterable[int]] = ...) -> None: ...

class pb_gvm_rank(_message.Message):
    __slots__ = ("gid", "score", "time", "logo", "name", "member", "exp")
    GID_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    LOGO_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    MEMBER_FIELD_NUMBER: _ClassVar[int]
    EXP_FIELD_NUMBER: _ClassVar[int]
    gid: int
    score: int
    time: int
    logo: int
    name: str
    member: int
    exp: int
    def __init__(self, gid: _Optional[int] = ..., score: _Optional[int] = ..., time: _Optional[int] = ..., logo: _Optional[int] = ..., name: _Optional[str] = ..., member: _Optional[int] = ..., exp: _Optional[int] = ...) -> None: ...

class pb_match(_message.Message):
    __slots__ = ("idx", "name", "uid", "lv", "logo", "lbox", "win", "heroes", "power")
    IDX_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    LV_FIELD_NUMBER: _ClassVar[int]
    LOGO_FIELD_NUMBER: _ClassVar[int]
    LBOX_FIELD_NUMBER: _ClassVar[int]
    WIN_FIELD_NUMBER: _ClassVar[int]
    HEROES_FIELD_NUMBER: _ClassVar[int]
    POWER_FIELD_NUMBER: _ClassVar[int]
    idx: int
    name: str
    uid: int
    lv: int
    logo: int
    lbox: int
    win: int
    heroes: _containers.RepeatedCompositeFieldContainer[pb_match_hero]
    power: int
    def __init__(self, idx: _Optional[int] = ..., name: _Optional[str] = ..., uid: _Optional[int] = ..., lv: _Optional[int] = ..., logo: _Optional[int] = ..., lbox: _Optional[int] = ..., win: _Optional[int] = ..., heroes: _Optional[_Iterable[_Union[pb_match_hero, _Mapping]]] = ..., power: _Optional[int] = ...) -> None: ...

class pb_match_hero(_message.Message):
    __slots__ = ("pos", "id", "lv", "stl", "flag", "equips", "wake", "skill_id", "attr", "skin", "qlv", "tree_flag", "core", "times", "use", "faith_lv")
    POS_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    LV_FIELD_NUMBER: _ClassVar[int]
    STL_FIELD_NUMBER: _ClassVar[int]
    FLAG_FIELD_NUMBER: _ClassVar[int]
    EQUIPS_FIELD_NUMBER: _ClassVar[int]
    WAKE_FIELD_NUMBER: _ClassVar[int]
    SKILL_ID_FIELD_NUMBER: _ClassVar[int]
    ATTR_FIELD_NUMBER: _ClassVar[int]
    SKIN_FIELD_NUMBER: _ClassVar[int]
    QLV_FIELD_NUMBER: _ClassVar[int]
    TREE_FLAG_FIELD_NUMBER: _ClassVar[int]
    CORE_FIELD_NUMBER: _ClassVar[int]
    TIMES_FIELD_NUMBER: _ClassVar[int]
    USE_FIELD_NUMBER: _ClassVar[int]
    FAITH_LV_FIELD_NUMBER: _ClassVar[int]
    pos: int
    id: int
    lv: int
    stl: int
    flag: int
    equips: _containers.RepeatedCompositeFieldContainer[pb_equip]
    wake: int
    skill_id: _containers.RepeatedScalarFieldContainer[int]
    attr: pb_attr
    skin: int
    qlv: int
    tree_flag: int
    core: int
    times: int
    use: int
    faith_lv: int
    def __init__(self, pos: _Optional[int] = ..., id: _Optional[int] = ..., lv: _Optional[int] = ..., stl: _Optional[int] = ..., flag: _Optional[int] = ..., equips: _Optional[_Iterable[_Union[pb_equip, _Mapping]]] = ..., wake: _Optional[int] = ..., skill_id: _Optional[_Iterable[int]] = ..., attr: _Optional[_Union[pb_attr, _Mapping]] = ..., skin: _Optional[int] = ..., qlv: _Optional[int] = ..., tree_flag: _Optional[int] = ..., core: _Optional[int] = ..., times: _Optional[int] = ..., use: _Optional[int] = ..., faith_lv: _Optional[int] = ...) -> None: ...

class pb_pvp_accounts(_message.Message):
    __slots__ = ("score", "win")
    SCORE_FIELD_NUMBER: _ClassVar[int]
    WIN_FIELD_NUMBER: _ClassVar[int]
    score: int
    win: int
    def __init__(self, score: _Optional[int] = ..., win: _Optional[int] = ...) -> None: ...

class pb_attr(_message.Message):
    __slots__ = ("atk", "hp", "arm", "spd", "sklP", "hit", "miss", "crit", "critTime", "brk", "free", "decDmg", "trueAtk")
    ATK_FIELD_NUMBER: _ClassVar[int]
    HP_FIELD_NUMBER: _ClassVar[int]
    ARM_FIELD_NUMBER: _ClassVar[int]
    SPD_FIELD_NUMBER: _ClassVar[int]
    SKLP_FIELD_NUMBER: _ClassVar[int]
    HIT_FIELD_NUMBER: _ClassVar[int]
    MISS_FIELD_NUMBER: _ClassVar[int]
    CRIT_FIELD_NUMBER: _ClassVar[int]
    CRITTIME_FIELD_NUMBER: _ClassVar[int]
    BRK_FIELD_NUMBER: _ClassVar[int]
    FREE_FIELD_NUMBER: _ClassVar[int]
    DECDMG_FIELD_NUMBER: _ClassVar[int]
    TRUEATK_FIELD_NUMBER: _ClassVar[int]
    atk: int
    hp: int
    arm: int
    spd: int
    sklP: int
    hit: int
    miss: int
    crit: int
    critTime: int
    brk: int
    free: int
    decDmg: int
    trueAtk: int
    def __init__(self, atk: _Optional[int] = ..., hp: _Optional[int] = ..., arm: _Optional[int] = ..., spd: _Optional[int] = ..., sklP: _Optional[int] = ..., hit: _Optional[int] = ..., miss: _Optional[int] = ..., crit: _Optional[int] = ..., critTime: _Optional[int] = ..., brk: _Optional[int] = ..., free: _Optional[int] = ..., decDmg: _Optional[int] = ..., trueAtk: _Optional[int] = ...) -> None: ...

class pb_gvm_mbr(_message.Message):
    __slots__ = ("name", "uid", "lv", "logo", "lbox", "scores", "score")
    NAME_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    LV_FIELD_NUMBER: _ClassVar[int]
    LOGO_FIELD_NUMBER: _ClassVar[int]
    LBOX_FIELD_NUMBER: _ClassVar[int]
    SCORES_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    name: str
    uid: int
    lv: int
    logo: int
    lbox: int
    scores: _containers.RepeatedScalarFieldContainer[str]
    score: int
    def __init__(self, name: _Optional[str] = ..., uid: _Optional[int] = ..., lv: _Optional[int] = ..., logo: _Optional[int] = ..., lbox: _Optional[int] = ..., scores: _Optional[_Iterable[str]] = ..., score: _Optional[int] = ...) -> None: ...

class pb_up_star(_message.Message):
    __slots__ = ("id", "hid")
    ID_FIELD_NUMBER: _ClassVar[int]
    HID_FIELD_NUMBER: _ClassVar[int]
    id: int
    hid: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, id: _Optional[int] = ..., hid: _Optional[_Iterable[int]] = ...) -> None: ...

class pb_fun(_message.Message):
    __slots__ = ("open", "cd", "id")
    OPEN_FIELD_NUMBER: _ClassVar[int]
    CD_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    open: int
    cd: int
    id: int
    def __init__(self, open: _Optional[int] = ..., cd: _Optional[int] = ..., id: _Optional[int] = ...) -> None: ...

class hland_change_skin(_message.Message):
    __slots__ = ("skin", "pos")
    SKIN_FIELD_NUMBER: _ClassVar[int]
    POS_FIELD_NUMBER: _ClassVar[int]
    skin: int
    pos: int
    def __init__(self, skin: _Optional[int] = ..., pos: _Optional[int] = ...) -> None: ...

class pb_hland_log(_message.Message):
    __slots__ = ("name", "uid", "lv", "logo", "lbox", "type", "time")
    NAME_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    LV_FIELD_NUMBER: _ClassVar[int]
    LOGO_FIELD_NUMBER: _ClassVar[int]
    LBOX_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    name: str
    uid: int
    lv: int
    logo: int
    lbox: int
    type: int
    time: int
    def __init__(self, name: _Optional[str] = ..., uid: _Optional[int] = ..., lv: _Optional[int] = ..., logo: _Optional[int] = ..., lbox: _Optional[int] = ..., type: _Optional[int] = ..., time: _Optional[int] = ...) -> None: ...

class pb_hmbr(_message.Message):
    __slots__ = ("name", "uid", "lv", "logo", "lbox", "item_ids")
    NAME_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    LV_FIELD_NUMBER: _ClassVar[int]
    LOGO_FIELD_NUMBER: _ClassVar[int]
    LBOX_FIELD_NUMBER: _ClassVar[int]
    ITEM_IDS_FIELD_NUMBER: _ClassVar[int]
    name: str
    uid: int
    lv: int
    logo: int
    lbox: int
    item_ids: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, name: _Optional[str] = ..., uid: _Optional[int] = ..., lv: _Optional[int] = ..., logo: _Optional[int] = ..., lbox: _Optional[int] = ..., item_ids: _Optional[_Iterable[int]] = ...) -> None: ...

class pb_hteam(_message.Message):
    __slots__ = ("id", "leader", "type", "mbr", "cd", "shape", "invites")
    ID_FIELD_NUMBER: _ClassVar[int]
    LEADER_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    MBR_FIELD_NUMBER: _ClassVar[int]
    CD_FIELD_NUMBER: _ClassVar[int]
    SHAPE_FIELD_NUMBER: _ClassVar[int]
    INVITES_FIELD_NUMBER: _ClassVar[int]
    id: str
    leader: int
    type: int
    mbr: _containers.RepeatedCompositeFieldContainer[pb_hmbr]
    cd: int
    shape: bool
    invites: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, id: _Optional[str] = ..., leader: _Optional[int] = ..., type: _Optional[int] = ..., mbr: _Optional[_Iterable[_Union[pb_hmbr, _Mapping]]] = ..., cd: _Optional[int] = ..., shape: _Optional[bool] = ..., invites: _Optional[_Iterable[int]] = ...) -> None: ...

class pb_team_info(_message.Message):
    __slots__ = ("id", "name", "heroes", "petid", "flag")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    HEROES_FIELD_NUMBER: _ClassVar[int]
    PETID_FIELD_NUMBER: _ClassVar[int]
    FLAG_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    heroes: _containers.RepeatedCompositeFieldContainer[pb_team_hero]
    petid: int
    flag: int
    def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ..., heroes: _Optional[_Iterable[_Union[pb_team_hero, _Mapping]]] = ..., petid: _Optional[int] = ..., flag: _Optional[int] = ...) -> None: ...

class pb_team_hero(_message.Message):
    __slots__ = ("pos", "hid", "equips", "skill_id", "sattrs", "flag", "faith_skill")
    POS_FIELD_NUMBER: _ClassVar[int]
    HID_FIELD_NUMBER: _ClassVar[int]
    EQUIPS_FIELD_NUMBER: _ClassVar[int]
    SKILL_ID_FIELD_NUMBER: _ClassVar[int]
    SATTRS_FIELD_NUMBER: _ClassVar[int]
    FLAG_FIELD_NUMBER: _ClassVar[int]
    FAITH_SKILL_FIELD_NUMBER: _ClassVar[int]
    pos: int
    hid: int
    equips: _containers.RepeatedCompositeFieldContainer[pb_equip]
    skill_id: _containers.RepeatedScalarFieldContainer[int]
    sattrs: _containers.RepeatedCompositeFieldContainer[pb_sattr]
    flag: int
    faith_skill: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, pos: _Optional[int] = ..., hid: _Optional[int] = ..., equips: _Optional[_Iterable[_Union[pb_equip, _Mapping]]] = ..., skill_id: _Optional[_Iterable[int]] = ..., sattrs: _Optional[_Iterable[_Union[pb_sattr, _Mapping]]] = ..., flag: _Optional[int] = ..., faith_skill: _Optional[_Iterable[int]] = ...) -> None: ...

class good(_message.Message):
    __slots__ = ("good_id", "hero_id", "qlt", "price", "del_price", "state", "cd", "rprice", "seller", "buyer")
    GOOD_ID_FIELD_NUMBER: _ClassVar[int]
    HERO_ID_FIELD_NUMBER: _ClassVar[int]
    QLT_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    DEL_PRICE_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    CD_FIELD_NUMBER: _ClassVar[int]
    RPRICE_FIELD_NUMBER: _ClassVar[int]
    SELLER_FIELD_NUMBER: _ClassVar[int]
    BUYER_FIELD_NUMBER: _ClassVar[int]
    good_id: int
    hero_id: int
    qlt: pb_hero_qlc
    price: int
    del_price: int
    state: int
    cd: int
    rprice: int
    seller: pb_give_role
    buyer: pb_give_role
    def __init__(self, good_id: _Optional[int] = ..., hero_id: _Optional[int] = ..., qlt: _Optional[_Union[pb_hero_qlc, _Mapping]] = ..., price: _Optional[int] = ..., del_price: _Optional[int] = ..., state: _Optional[int] = ..., cd: _Optional[int] = ..., rprice: _Optional[int] = ..., seller: _Optional[_Union[pb_give_role, _Mapping]] = ..., buyer: _Optional[_Union[pb_give_role, _Mapping]] = ...) -> None: ...

class mall_log(_message.Message):
    __slots__ = ("time", "heroid", "qlt", "price", "type", "status", "goodid", "user")
    TIME_FIELD_NUMBER: _ClassVar[int]
    HEROID_FIELD_NUMBER: _ClassVar[int]
    QLT_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    GOODID_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    time: int
    heroid: int
    qlt: pb_hero_qlc
    price: int
    type: int
    status: int
    goodid: int
    user: pb_give_role
    def __init__(self, time: _Optional[int] = ..., heroid: _Optional[int] = ..., qlt: _Optional[_Union[pb_hero_qlc, _Mapping]] = ..., price: _Optional[int] = ..., type: _Optional[int] = ..., status: _Optional[int] = ..., goodid: _Optional[int] = ..., user: _Optional[_Union[pb_give_role, _Mapping]] = ...) -> None: ...

class pb_kv(_message.Message):
    __slots__ = ("k", "v")
    K_FIELD_NUMBER: _ClassVar[int]
    V_FIELD_NUMBER: _ClassVar[int]
    k: int
    v: int
    def __init__(self, k: _Optional[int] = ..., v: _Optional[int] = ...) -> None: ...

class pb_kvs(_message.Message):
    __slots__ = ("k", "v", "v2", "v3")
    K_FIELD_NUMBER: _ClassVar[int]
    V_FIELD_NUMBER: _ClassVar[int]
    V2_FIELD_NUMBER: _ClassVar[int]
    V3_FIELD_NUMBER: _ClassVar[int]
    k: _containers.RepeatedScalarFieldContainer[int]
    v: _containers.RepeatedScalarFieldContainer[int]
    v2: _containers.RepeatedScalarFieldContainer[int]
    v3: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, k: _Optional[_Iterable[int]] = ..., v: _Optional[_Iterable[int]] = ..., v2: _Optional[_Iterable[int]] = ..., v3: _Optional[_Iterable[int]] = ...) -> None: ...

class pb_kv2(_message.Message):
    __slots__ = ("k", "v", "v2", "v3", "v4", "v5")
    K_FIELD_NUMBER: _ClassVar[int]
    V_FIELD_NUMBER: _ClassVar[int]
    V2_FIELD_NUMBER: _ClassVar[int]
    V3_FIELD_NUMBER: _ClassVar[int]
    V4_FIELD_NUMBER: _ClassVar[int]
    V5_FIELD_NUMBER: _ClassVar[int]
    k: int
    v: int
    v2: int
    v3: int
    v4: int
    v5: int
    def __init__(self, k: _Optional[int] = ..., v: _Optional[int] = ..., v2: _Optional[int] = ..., v3: _Optional[int] = ..., v4: _Optional[int] = ..., v5: _Optional[int] = ...) -> None: ...

class pb_growup(_message.Message):
    __slots__ = ("id", "index", "claim")
    ID_FIELD_NUMBER: _ClassVar[int]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    CLAIM_FIELD_NUMBER: _ClassVar[int]
    id: int
    index: int
    claim: int
    def __init__(self, id: _Optional[int] = ..., index: _Optional[int] = ..., claim: _Optional[int] = ...) -> None: ...

class pb_puzzle(_message.Message):
    __slots__ = ("id", "next", "cur", "pos", "bag", "num", "ring", "siz")
    ID_FIELD_NUMBER: _ClassVar[int]
    NEXT_FIELD_NUMBER: _ClassVar[int]
    CUR_FIELD_NUMBER: _ClassVar[int]
    POS_FIELD_NUMBER: _ClassVar[int]
    BAG_FIELD_NUMBER: _ClassVar[int]
    NUM_FIELD_NUMBER: _ClassVar[int]
    RING_FIELD_NUMBER: _ClassVar[int]
    SIZ_FIELD_NUMBER: _ClassVar[int]
    id: int
    next: int
    cur: int
    pos: _containers.RepeatedCompositeFieldContainer[pb_kv]
    bag: _containers.RepeatedScalarFieldContainer[int]
    num: int
    ring: int
    siz: int
    def __init__(self, id: _Optional[int] = ..., next: _Optional[int] = ..., cur: _Optional[int] = ..., pos: _Optional[_Iterable[_Union[pb_kv, _Mapping]]] = ..., bag: _Optional[_Iterable[int]] = ..., num: _Optional[int] = ..., ring: _Optional[int] = ..., siz: _Optional[int] = ...) -> None: ...

class pb_give_role(_message.Message):
    __slots__ = ("uid64", "channel", "lv", "lbox", "name", "logo")
    UID64_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_FIELD_NUMBER: _ClassVar[int]
    LV_FIELD_NUMBER: _ClassVar[int]
    LBOX_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    LOGO_FIELD_NUMBER: _ClassVar[int]
    uid64: int
    channel: str
    lv: int
    lbox: int
    name: str
    logo: int
    def __init__(self, uid64: _Optional[int] = ..., channel: _Optional[str] = ..., lv: _Optional[int] = ..., lbox: _Optional[int] = ..., name: _Optional[str] = ..., logo: _Optional[int] = ...) -> None: ...

class pb_give_order(_message.Message):
    __slots__ = ("id", "type", "num", "status", "role", "cd")
    ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    NUM_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    CD_FIELD_NUMBER: _ClassVar[int]
    id: int
    type: int
    num: int
    status: int
    role: pb_give_role
    cd: int
    def __init__(self, id: _Optional[int] = ..., type: _Optional[int] = ..., num: _Optional[int] = ..., status: _Optional[int] = ..., role: _Optional[_Union[pb_give_role, _Mapping]] = ..., cd: _Optional[int] = ...) -> None: ...

class pb_give_log(_message.Message):
    __slots__ = ("name", "num", "tax", "time")
    NAME_FIELD_NUMBER: _ClassVar[int]
    NUM_FIELD_NUMBER: _ClassVar[int]
    TAX_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    name: str
    num: int
    tax: int
    time: int
    def __init__(self, name: _Optional[str] = ..., num: _Optional[int] = ..., tax: _Optional[int] = ..., time: _Optional[int] = ...) -> None: ...

class pb_qlt_pvp_enemy(_message.Message):
    __slots__ = ("idx", "logo", "name", "cluster", "lv", "lbox", "camp", "skls", "hide", "uid", "power", "is_fight", "gname")
    IDX_FIELD_NUMBER: _ClassVar[int]
    LOGO_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_FIELD_NUMBER: _ClassVar[int]
    LV_FIELD_NUMBER: _ClassVar[int]
    LBOX_FIELD_NUMBER: _ClassVar[int]
    CAMP_FIELD_NUMBER: _ClassVar[int]
    SKLS_FIELD_NUMBER: _ClassVar[int]
    HIDE_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    POWER_FIELD_NUMBER: _ClassVar[int]
    IS_FIGHT_FIELD_NUMBER: _ClassVar[int]
    GNAME_FIELD_NUMBER: _ClassVar[int]
    idx: int
    logo: int
    name: str
    cluster: str
    lv: int
    lbox: int
    camp: _containers.RepeatedCompositeFieldContainer[pb_unit]
    skls: _containers.RepeatedScalarFieldContainer[int]
    hide: _containers.RepeatedScalarFieldContainer[int]
    uid: int
    power: int
    is_fight: int
    gname: str
    def __init__(self, idx: _Optional[int] = ..., logo: _Optional[int] = ..., name: _Optional[str] = ..., cluster: _Optional[str] = ..., lv: _Optional[int] = ..., lbox: _Optional[int] = ..., camp: _Optional[_Iterable[_Union[pb_unit, _Mapping]]] = ..., skls: _Optional[_Iterable[int]] = ..., hide: _Optional[_Iterable[int]] = ..., uid: _Optional[int] = ..., power: _Optional[int] = ..., is_fight: _Optional[int] = ..., gname: _Optional[str] = ...) -> None: ...

class pb_qloger(_message.Message):
    __slots__ = ("vid", "a_mbr", "d_mbr", "time", "win", "delta", "a_skls", "d_skls")
    VID_FIELD_NUMBER: _ClassVar[int]
    A_MBR_FIELD_NUMBER: _ClassVar[int]
    D_MBR_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    WIN_FIELD_NUMBER: _ClassVar[int]
    DELTA_FIELD_NUMBER: _ClassVar[int]
    A_SKLS_FIELD_NUMBER: _ClassVar[int]
    D_SKLS_FIELD_NUMBER: _ClassVar[int]
    vid: int
    a_mbr: pb_smbr
    d_mbr: pb_smbr
    time: int
    win: bool
    delta: int
    a_skls: _containers.RepeatedScalarFieldContainer[int]
    d_skls: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, vid: _Optional[int] = ..., a_mbr: _Optional[_Union[pb_smbr, _Mapping]] = ..., d_mbr: _Optional[_Union[pb_smbr, _Mapping]] = ..., time: _Optional[int] = ..., win: _Optional[bool] = ..., delta: _Optional[int] = ..., a_skls: _Optional[_Iterable[int]] = ..., d_skls: _Optional[_Iterable[int]] = ...) -> None: ...

class pb_qvideo(_message.Message):
    __slots__ = ("atk", "frames", "hurts", "win")
    ATK_FIELD_NUMBER: _ClassVar[int]
    DEF_FIELD_NUMBER: _ClassVar[int]
    FRAMES_FIELD_NUMBER: _ClassVar[int]
    HURTS_FIELD_NUMBER: _ClassVar[int]
    WIN_FIELD_NUMBER: _ClassVar[int]
    atk: _containers.RepeatedCompositeFieldContainer[pb_unit]
    frames: _containers.RepeatedScalarFieldContainer[bytes]
    hurts: _containers.RepeatedCompositeFieldContainer[pb_hurts]
    win: bool
    def __init__(self, atk: _Optional[_Iterable[_Union[pb_unit, _Mapping]]] = ..., frames: _Optional[_Iterable[bytes]] = ..., hurts: _Optional[_Iterable[_Union[pb_hurts, _Mapping]]] = ..., win: _Optional[bool] = ..., **kwargs) -> None: ...

class pb_qlog(_message.Message):
    __slots__ = ("video", "a_mbr", "d_mbr", "time", "win", "delta", "a_skls", "d_skls")
    VIDEO_FIELD_NUMBER: _ClassVar[int]
    A_MBR_FIELD_NUMBER: _ClassVar[int]
    D_MBR_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    WIN_FIELD_NUMBER: _ClassVar[int]
    DELTA_FIELD_NUMBER: _ClassVar[int]
    A_SKLS_FIELD_NUMBER: _ClassVar[int]
    D_SKLS_FIELD_NUMBER: _ClassVar[int]
    video: _containers.RepeatedCompositeFieldContainer[pb_qvideo]
    a_mbr: pb_smbr
    d_mbr: pb_smbr
    time: int
    win: bool
    delta: int
    a_skls: _containers.RepeatedScalarFieldContainer[int]
    d_skls: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, video: _Optional[_Iterable[_Union[pb_qvideo, _Mapping]]] = ..., a_mbr: _Optional[_Union[pb_smbr, _Mapping]] = ..., d_mbr: _Optional[_Union[pb_smbr, _Mapping]] = ..., time: _Optional[int] = ..., win: _Optional[bool] = ..., delta: _Optional[int] = ..., a_skls: _Optional[_Iterable[int]] = ..., d_skls: _Optional[_Iterable[int]] = ...) -> None: ...

class power_rank(_message.Message):
    __slots__ = ("id", "player", "score", "live")
    ID_FIELD_NUMBER: _ClassVar[int]
    PLAYER_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    LIVE_FIELD_NUMBER: _ClassVar[int]
    id: int
    player: pb_give_role
    score: int
    live: int
    def __init__(self, id: _Optional[int] = ..., player: _Optional[_Union[pb_give_role, _Mapping]] = ..., score: _Optional[int] = ..., live: _Optional[int] = ...) -> None: ...

class power_task(_message.Message):
    __slots__ = ("id", "type", "cd", "num", "dot_id", "flag", "excel_id")
    ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    CD_FIELD_NUMBER: _ClassVar[int]
    NUM_FIELD_NUMBER: _ClassVar[int]
    DOT_ID_FIELD_NUMBER: _ClassVar[int]
    FLAG_FIELD_NUMBER: _ClassVar[int]
    EXCEL_ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    type: int
    cd: int
    num: int
    dot_id: int
    flag: int
    excel_id: int
    def __init__(self, id: _Optional[int] = ..., type: _Optional[int] = ..., cd: _Optional[int] = ..., num: _Optional[int] = ..., dot_id: _Optional[int] = ..., flag: _Optional[int] = ..., excel_id: _Optional[int] = ...) -> None: ...

class dot_info(_message.Message):
    __slots__ = ("id", "power_id", "degree", "max", "status", "item", "buff", "tmp_id", "skill", "cd", "cd2", "cd3", "cd4", "cd5", "dot")
    ID_FIELD_NUMBER: _ClassVar[int]
    POWER_ID_FIELD_NUMBER: _ClassVar[int]
    DEGREE_FIELD_NUMBER: _ClassVar[int]
    MAX_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ITEM_FIELD_NUMBER: _ClassVar[int]
    BUFF_FIELD_NUMBER: _ClassVar[int]
    TMP_ID_FIELD_NUMBER: _ClassVar[int]
    SKILL_FIELD_NUMBER: _ClassVar[int]
    CD_FIELD_NUMBER: _ClassVar[int]
    CD2_FIELD_NUMBER: _ClassVar[int]
    CD3_FIELD_NUMBER: _ClassVar[int]
    CD4_FIELD_NUMBER: _ClassVar[int]
    CD5_FIELD_NUMBER: _ClassVar[int]
    DOT_FIELD_NUMBER: _ClassVar[int]
    id: int
    power_id: int
    degree: int
    max: int
    status: int
    item: int
    buff: _containers.RepeatedCompositeFieldContainer[pb_item]
    tmp_id: int
    skill: _containers.RepeatedScalarFieldContainer[int]
    cd: int
    cd2: int
    cd3: int
    cd4: int
    cd5: int
    dot: pb_kvs
    def __init__(self, id: _Optional[int] = ..., power_id: _Optional[int] = ..., degree: _Optional[int] = ..., max: _Optional[int] = ..., status: _Optional[int] = ..., item: _Optional[int] = ..., buff: _Optional[_Iterable[_Union[pb_item, _Mapping]]] = ..., tmp_id: _Optional[int] = ..., skill: _Optional[_Iterable[int]] = ..., cd: _Optional[int] = ..., cd2: _Optional[int] = ..., cd3: _Optional[int] = ..., cd4: _Optional[int] = ..., cd5: _Optional[int] = ..., dot: _Optional[_Union[pb_kvs, _Mapping]] = ...) -> None: ...

class dot_log(_message.Message):
    __slots__ = ("type", "degree", "time", "id", "add")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    DEGREE_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    ADD_FIELD_NUMBER: _ClassVar[int]
    type: int
    degree: int
    time: str
    id: int
    add: int
    def __init__(self, type: _Optional[int] = ..., degree: _Optional[int] = ..., time: _Optional[str] = ..., id: _Optional[int] = ..., add: _Optional[int] = ...) -> None: ...

class power_monster(_message.Message):
    __slots__ = ("id", "camp", "buff")
    ID_FIELD_NUMBER: _ClassVar[int]
    CAMP_FIELD_NUMBER: _ClassVar[int]
    BUFF_FIELD_NUMBER: _ClassVar[int]
    id: int
    camp: _containers.RepeatedCompositeFieldContainer[pb_unit]
    buff: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, id: _Optional[int] = ..., camp: _Optional[_Iterable[_Union[pb_unit, _Mapping]]] = ..., buff: _Optional[_Iterable[int]] = ...) -> None: ...

class power_skill(_message.Message):
    __slots__ = ("id", "name", "skill", "cd")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SKILL_FIELD_NUMBER: _ClassVar[int]
    CD_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    skill: _containers.RepeatedScalarFieldContainer[int]
    cd: int
    def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ..., skill: _Optional[_Iterable[int]] = ..., cd: _Optional[int] = ...) -> None: ...

class power_manager(_message.Message):
    __slots__ = ("udk", "cluster", "uid")
    UDK_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    udk: str
    cluster: str
    uid: int
    def __init__(self, udk: _Optional[str] = ..., cluster: _Optional[str] = ..., uid: _Optional[int] = ...) -> None: ...

class stower_breed(_message.Message):
    __slots__ = ("id", "pid1", "pid2", "cd", "egg")
    ID_FIELD_NUMBER: _ClassVar[int]
    PID1_FIELD_NUMBER: _ClassVar[int]
    PID2_FIELD_NUMBER: _ClassVar[int]
    CD_FIELD_NUMBER: _ClassVar[int]
    EGG_FIELD_NUMBER: _ClassVar[int]
    id: int
    pid1: int
    pid2: int
    cd: int
    egg: int
    def __init__(self, id: _Optional[int] = ..., pid1: _Optional[int] = ..., pid2: _Optional[int] = ..., cd: _Optional[int] = ..., egg: _Optional[int] = ...) -> None: ...

class stower_lucky(_message.Message):
    __slots__ = ("id", "ratio")
    ID_FIELD_NUMBER: _ClassVar[int]
    RATIO_FIELD_NUMBER: _ClassVar[int]
    id: int
    ratio: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, id: _Optional[int] = ..., ratio: _Optional[_Iterable[int]] = ...) -> None: ...

class power_log(_message.Message):
    __slots__ = ("type", "job", "time", "name", "point", "buff")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    JOB_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    POINT_FIELD_NUMBER: _ClassVar[int]
    BUFF_FIELD_NUMBER: _ClassVar[int]
    type: int
    job: int
    time: str
    name: str
    point: int
    buff: int
    def __init__(self, type: _Optional[int] = ..., job: _Optional[int] = ..., time: _Optional[str] = ..., name: _Optional[str] = ..., point: _Optional[int] = ..., buff: _Optional[int] = ...) -> None: ...

class pb_iboss(_message.Message):
    __slots__ = ("bossid", "tscore", "cd", "score", "hp", "full")
    BOSSID_FIELD_NUMBER: _ClassVar[int]
    TSCORE_FIELD_NUMBER: _ClassVar[int]
    CD_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    HP_FIELD_NUMBER: _ClassVar[int]
    FULL_FIELD_NUMBER: _ClassVar[int]
    bossid: int
    tscore: int
    cd: int
    score: int
    hp: int
    full: bool
    def __init__(self, bossid: _Optional[int] = ..., tscore: _Optional[int] = ..., cd: _Optional[int] = ..., score: _Optional[int] = ..., hp: _Optional[int] = ..., full: _Optional[bool] = ...) -> None: ...

class pb_iboss_rank(_message.Message):
    __slots__ = ("logo", "uid", "score", "name", "lbox")
    LOGO_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    LBOX_FIELD_NUMBER: _ClassVar[int]
    logo: int
    uid: int
    score: int
    name: str
    lbox: int
    def __init__(self, logo: _Optional[int] = ..., uid: _Optional[int] = ..., score: _Optional[int] = ..., name: _Optional[str] = ..., lbox: _Optional[int] = ...) -> None: ...

class pb_mgame_map(_message.Message):
    __slots__ = ("id", "status", "prop_id")
    ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    PROP_ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    status: int
    prop_id: int
    def __init__(self, id: _Optional[int] = ..., status: _Optional[int] = ..., prop_id: _Optional[int] = ...) -> None: ...

class pb_mgame_prop(_message.Message):
    __slots__ = ("id", "cfg_id", "cd", "num", "time", "map_id", "map_status")
    ID_FIELD_NUMBER: _ClassVar[int]
    CFG_ID_FIELD_NUMBER: _ClassVar[int]
    CD_FIELD_NUMBER: _ClassVar[int]
    NUM_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    MAP_ID_FIELD_NUMBER: _ClassVar[int]
    MAP_STATUS_FIELD_NUMBER: _ClassVar[int]
    id: int
    cfg_id: int
    cd: int
    num: int
    time: int
    map_id: int
    map_status: int
    def __init__(self, id: _Optional[int] = ..., cfg_id: _Optional[int] = ..., cd: _Optional[int] = ..., num: _Optional[int] = ..., time: _Optional[int] = ..., map_id: _Optional[int] = ..., map_status: _Optional[int] = ...) -> None: ...

class pb_gt_node(_message.Message):
    __slots__ = ("mbr", "cd", "power")
    MBR_FIELD_NUMBER: _ClassVar[int]
    CD_FIELD_NUMBER: _ClassVar[int]
    POWER_FIELD_NUMBER: _ClassVar[int]
    mbr: pb_smbr
    cd: int
    power: int
    def __init__(self, mbr: _Optional[_Union[pb_smbr, _Mapping]] = ..., cd: _Optional[int] = ..., power: _Optional[int] = ...) -> None: ...

class pb_gt_mbr(_message.Message):
    __slots__ = ("logo", "mlogo", "lv")
    LOGO_FIELD_NUMBER: _ClassVar[int]
    MLOGO_FIELD_NUMBER: _ClassVar[int]
    LV_FIELD_NUMBER: _ClassVar[int]
    logo: int
    mlogo: int
    lv: int
    def __init__(self, logo: _Optional[int] = ..., mlogo: _Optional[int] = ..., lv: _Optional[int] = ...) -> None: ...

class pb_gt_log(_message.Message):
    __slots__ = ("left", "right", "atk", "win", "vid", "cd", "mapid")
    LEFT_FIELD_NUMBER: _ClassVar[int]
    RIGHT_FIELD_NUMBER: _ClassVar[int]
    ATK_FIELD_NUMBER: _ClassVar[int]
    WIN_FIELD_NUMBER: _ClassVar[int]
    VID_FIELD_NUMBER: _ClassVar[int]
    CD_FIELD_NUMBER: _ClassVar[int]
    MAPID_FIELD_NUMBER: _ClassVar[int]
    left: pb_gt_mbr
    right: pb_gt_mbr
    atk: bool
    win: bool
    vid: int
    cd: int
    mapid: int
    def __init__(self, left: _Optional[_Union[pb_gt_mbr, _Mapping]] = ..., right: _Optional[_Union[pb_gt_mbr, _Mapping]] = ..., atk: _Optional[bool] = ..., win: _Optional[bool] = ..., vid: _Optional[int] = ..., cd: _Optional[int] = ..., mapid: _Optional[int] = ...) -> None: ...

class pb_gvideo(_message.Message):
    __slots__ = ("atk", "frames", "hurts", "win", "teamid")
    ATK_FIELD_NUMBER: _ClassVar[int]
    DEF_FIELD_NUMBER: _ClassVar[int]
    FRAMES_FIELD_NUMBER: _ClassVar[int]
    HURTS_FIELD_NUMBER: _ClassVar[int]
    WIN_FIELD_NUMBER: _ClassVar[int]
    TEAMID_FIELD_NUMBER: _ClassVar[int]
    atk: _containers.RepeatedCompositeFieldContainer[pb_unit]
    frames: _containers.RepeatedScalarFieldContainer[bytes]
    hurts: _containers.RepeatedCompositeFieldContainer[pb_hurts]
    win: bool
    teamid: int
    def __init__(self, atk: _Optional[_Iterable[_Union[pb_unit, _Mapping]]] = ..., frames: _Optional[_Iterable[bytes]] = ..., hurts: _Optional[_Iterable[_Union[pb_hurts, _Mapping]]] = ..., win: _Optional[bool] = ..., teamid: _Optional[int] = ..., **kwargs) -> None: ...

class pb_hstar(_message.Message):
    __slots__ = ("uid", "name", "logo", "score")
    UID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    LOGO_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    uid: int
    name: str
    logo: int
    score: int
    def __init__(self, uid: _Optional[int] = ..., name: _Optional[str] = ..., logo: _Optional[int] = ..., score: _Optional[int] = ...) -> None: ...

class pb_world_build(_message.Message):
    __slots__ = ("id", "bid", "state", "res", "buy_num")
    ID_FIELD_NUMBER: _ClassVar[int]
    BID_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    RES_FIELD_NUMBER: _ClassVar[int]
    BUY_NUM_FIELD_NUMBER: _ClassVar[int]
    id: int
    bid: int
    state: int
    res: _containers.RepeatedCompositeFieldContainer[pb_kv2]
    buy_num: int
    def __init__(self, id: _Optional[int] = ..., bid: _Optional[int] = ..., state: _Optional[int] = ..., res: _Optional[_Iterable[_Union[pb_kv2, _Mapping]]] = ..., buy_num: _Optional[int] = ...) -> None: ...

class pb_world_mall_item(_message.Message):
    __slots__ = ("orderid", "cost", "item", "state", "cd")
    ORDERID_FIELD_NUMBER: _ClassVar[int]
    COST_FIELD_NUMBER: _ClassVar[int]
    ITEM_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    CD_FIELD_NUMBER: _ClassVar[int]
    orderid: str
    cost: pb_item
    item: pb_item
    state: int
    cd: int
    def __init__(self, orderid: _Optional[str] = ..., cost: _Optional[_Union[pb_item, _Mapping]] = ..., item: _Optional[_Union[pb_item, _Mapping]] = ..., state: _Optional[int] = ..., cd: _Optional[int] = ...) -> None: ...

class pb_bworld_brief(_message.Message):
    __slots__ = ("key", "name", "group_id", "id_cfg", "teamid", "hps", "udk", "color", "monster_id", "bufs")
    KEY_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    ID_CFG_FIELD_NUMBER: _ClassVar[int]
    TEAMID_FIELD_NUMBER: _ClassVar[int]
    HPS_FIELD_NUMBER: _ClassVar[int]
    UDK_FIELD_NUMBER: _ClassVar[int]
    COLOR_FIELD_NUMBER: _ClassVar[int]
    MONSTER_ID_FIELD_NUMBER: _ClassVar[int]
    BUFS_FIELD_NUMBER: _ClassVar[int]
    key: int
    name: str
    group_id: int
    id_cfg: int
    teamid: int
    hps: _containers.RepeatedScalarFieldContainer[int]
    udk: str
    color: int
    monster_id: int
    bufs: _containers.RepeatedCompositeFieldContainer[pb_cele_buf]
    def __init__(self, key: _Optional[int] = ..., name: _Optional[str] = ..., group_id: _Optional[int] = ..., id_cfg: _Optional[int] = ..., teamid: _Optional[int] = ..., hps: _Optional[_Iterable[int]] = ..., udk: _Optional[str] = ..., color: _Optional[int] = ..., monster_id: _Optional[int] = ..., bufs: _Optional[_Iterable[_Union[pb_cele_buf, _Mapping]]] = ...) -> None: ...

class pb_bworld_moudle(_message.Message):
    __slots__ = ("key", "id_cfg", "cd", "count", "mbr_num", "material", "monster", "bufs")
    KEY_FIELD_NUMBER: _ClassVar[int]
    ID_CFG_FIELD_NUMBER: _ClassVar[int]
    CD_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    MBR_NUM_FIELD_NUMBER: _ClassVar[int]
    MATERIAL_FIELD_NUMBER: _ClassVar[int]
    MONSTER_FIELD_NUMBER: _ClassVar[int]
    BUFS_FIELD_NUMBER: _ClassVar[int]
    key: int
    id_cfg: int
    cd: int
    count: int
    mbr_num: int
    material: _containers.RepeatedCompositeFieldContainer[pb_item]
    monster: pb_bworld_monster
    bufs: _containers.RepeatedCompositeFieldContainer[pb_cele_buf]
    def __init__(self, key: _Optional[int] = ..., id_cfg: _Optional[int] = ..., cd: _Optional[int] = ..., count: _Optional[int] = ..., mbr_num: _Optional[int] = ..., material: _Optional[_Iterable[_Union[pb_item, _Mapping]]] = ..., monster: _Optional[_Union[pb_bworld_monster, _Mapping]] = ..., bufs: _Optional[_Iterable[_Union[pb_cele_buf, _Mapping]]] = ...) -> None: ...

class pb_bworld_build(_message.Message):
    __slots__ = ("count", "miner", "cd", "rewards", "id_cfg", "rewards2")
    COUNT_FIELD_NUMBER: _ClassVar[int]
    MINER_FIELD_NUMBER: _ClassVar[int]
    CD_FIELD_NUMBER: _ClassVar[int]
    REWARDS_FIELD_NUMBER: _ClassVar[int]
    ID_CFG_FIELD_NUMBER: _ClassVar[int]
    REWARDS2_FIELD_NUMBER: _ClassVar[int]
    count: int
    miner: _containers.RepeatedCompositeFieldContainer[pb_smbr]
    cd: int
    rewards: _containers.RepeatedCompositeFieldContainer[pb_item]
    id_cfg: int
    rewards2: _containers.RepeatedCompositeFieldContainer[pb_item]
    def __init__(self, count: _Optional[int] = ..., miner: _Optional[_Iterable[_Union[pb_smbr, _Mapping]]] = ..., cd: _Optional[int] = ..., rewards: _Optional[_Iterable[_Union[pb_item, _Mapping]]] = ..., id_cfg: _Optional[int] = ..., rewards2: _Optional[_Iterable[_Union[pb_item, _Mapping]]] = ...) -> None: ...

class pb_bworld_monster(_message.Message):
    __slots__ = ("hpp", "cd", "rank", "soldiers", "buff_idx", "monster_id")
    HPP_FIELD_NUMBER: _ClassVar[int]
    CD_FIELD_NUMBER: _ClassVar[int]
    RANK_FIELD_NUMBER: _ClassVar[int]
    SOLDIERS_FIELD_NUMBER: _ClassVar[int]
    BUFF_IDX_FIELD_NUMBER: _ClassVar[int]
    MONSTER_ID_FIELD_NUMBER: _ClassVar[int]
    hpp: int
    cd: int
    rank: _containers.RepeatedCompositeFieldContainer[pb_smbr]
    soldiers: _containers.RepeatedScalarFieldContainer[int]
    buff_idx: int
    monster_id: int
    def __init__(self, hpp: _Optional[int] = ..., cd: _Optional[int] = ..., rank: _Optional[_Iterable[_Union[pb_smbr, _Mapping]]] = ..., soldiers: _Optional[_Iterable[int]] = ..., buff_idx: _Optional[int] = ..., monster_id: _Optional[int] = ...) -> None: ...

class pb_bworld_team(_message.Message):
    __slots__ = ("teamid", "camp", "vits", "key", "world_id", "soldiers", "back_soldiers", "skill_count")
    TEAMID_FIELD_NUMBER: _ClassVar[int]
    CAMP_FIELD_NUMBER: _ClassVar[int]
    VITS_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    WORLD_ID_FIELD_NUMBER: _ClassVar[int]
    SOLDIERS_FIELD_NUMBER: _ClassVar[int]
    BACK_SOLDIERS_FIELD_NUMBER: _ClassVar[int]
    SKILL_COUNT_FIELD_NUMBER: _ClassVar[int]
    teamid: int
    camp: _containers.RepeatedCompositeFieldContainer[pb_unit]
    vits: _containers.RepeatedScalarFieldContainer[int]
    key: int
    world_id: int
    soldiers: _containers.RepeatedScalarFieldContainer[int]
    back_soldiers: _containers.RepeatedScalarFieldContainer[int]
    skill_count: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, teamid: _Optional[int] = ..., camp: _Optional[_Iterable[_Union[pb_unit, _Mapping]]] = ..., vits: _Optional[_Iterable[int]] = ..., key: _Optional[int] = ..., world_id: _Optional[int] = ..., soldiers: _Optional[_Iterable[int]] = ..., back_soldiers: _Optional[_Iterable[int]] = ..., skill_count: _Optional[_Iterable[int]] = ...) -> None: ...

class pb_bworld(_message.Message):
    __slots__ = ("world_id", "id_cfg", "briefs", "key", "idx", "world_lv", "complete", "boss_id", "team_cd", "tag", "bufs")
    WORLD_ID_FIELD_NUMBER: _ClassVar[int]
    ID_CFG_FIELD_NUMBER: _ClassVar[int]
    BRIEFS_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    IDX_FIELD_NUMBER: _ClassVar[int]
    WORLD_LV_FIELD_NUMBER: _ClassVar[int]
    COMPLETE_FIELD_NUMBER: _ClassVar[int]
    BOSS_ID_FIELD_NUMBER: _ClassVar[int]
    TEAM_CD_FIELD_NUMBER: _ClassVar[int]
    TAG_FIELD_NUMBER: _ClassVar[int]
    BUFS_FIELD_NUMBER: _ClassVar[int]
    world_id: int
    id_cfg: int
    briefs: _containers.RepeatedCompositeFieldContainer[pb_bworld_brief]
    key: int
    idx: int
    world_lv: int
    complete: int
    boss_id: int
    team_cd: _containers.RepeatedScalarFieldContainer[int]
    tag: bytes
    bufs: _containers.RepeatedCompositeFieldContainer[pb_cele_buf]
    def __init__(self, world_id: _Optional[int] = ..., id_cfg: _Optional[int] = ..., briefs: _Optional[_Iterable[_Union[pb_bworld_brief, _Mapping]]] = ..., key: _Optional[int] = ..., idx: _Optional[int] = ..., world_lv: _Optional[int] = ..., complete: _Optional[int] = ..., boss_id: _Optional[int] = ..., team_cd: _Optional[_Iterable[int]] = ..., tag: _Optional[bytes] = ..., bufs: _Optional[_Iterable[_Union[pb_cele_buf, _Mapping]]] = ...) -> None: ...

class pb_bworld_log(_message.Message):
    __slots__ = ("type", "logo", "border", "lv", "name", "time", "win", "bid", "mid", "reward", "map_id", "monster_id", "gname", "uid", "rank")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    LOGO_FIELD_NUMBER: _ClassVar[int]
    BORDER_FIELD_NUMBER: _ClassVar[int]
    LV_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    WIN_FIELD_NUMBER: _ClassVar[int]
    BID_FIELD_NUMBER: _ClassVar[int]
    MID_FIELD_NUMBER: _ClassVar[int]
    REWARD_FIELD_NUMBER: _ClassVar[int]
    MAP_ID_FIELD_NUMBER: _ClassVar[int]
    MONSTER_ID_FIELD_NUMBER: _ClassVar[int]
    GNAME_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    RANK_FIELD_NUMBER: _ClassVar[int]
    type: int
    logo: int
    border: int
    lv: int
    name: str
    time: int
    win: bool
    bid: int
    mid: int
    reward: pb_bag
    map_id: int
    monster_id: int
    gname: str
    uid: int
    rank: int
    def __init__(self, type: _Optional[int] = ..., logo: _Optional[int] = ..., border: _Optional[int] = ..., lv: _Optional[int] = ..., name: _Optional[str] = ..., time: _Optional[int] = ..., win: _Optional[bool] = ..., bid: _Optional[int] = ..., mid: _Optional[int] = ..., reward: _Optional[_Union[pb_bag, _Mapping]] = ..., map_id: _Optional[int] = ..., monster_id: _Optional[int] = ..., gname: _Optional[str] = ..., uid: _Optional[int] = ..., rank: _Optional[int] = ...) -> None: ...

class pb_bworld_video(_message.Message):
    __slots__ = ("frames", "win", "reward", "atk", "hurts", "hpps", "stage", "result")
    FRAMES_FIELD_NUMBER: _ClassVar[int]
    WIN_FIELD_NUMBER: _ClassVar[int]
    REWARD_FIELD_NUMBER: _ClassVar[int]
    ATK_FIELD_NUMBER: _ClassVar[int]
    DEF_FIELD_NUMBER: _ClassVar[int]
    HURTS_FIELD_NUMBER: _ClassVar[int]
    HPPS_FIELD_NUMBER: _ClassVar[int]
    STAGE_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    frames: _containers.RepeatedScalarFieldContainer[bytes]
    win: bool
    reward: pb_bag
    atk: _containers.RepeatedCompositeFieldContainer[pb_unit]
    hurts: _containers.RepeatedCompositeFieldContainer[pb_hurts]
    hpps: _containers.RepeatedScalarFieldContainer[int]
    stage: int
    result: pb_bworld_result
    def __init__(self, frames: _Optional[_Iterable[bytes]] = ..., win: _Optional[bool] = ..., reward: _Optional[_Union[pb_bag, _Mapping]] = ..., atk: _Optional[_Iterable[_Union[pb_unit, _Mapping]]] = ..., hurts: _Optional[_Iterable[_Union[pb_hurts, _Mapping]]] = ..., hpps: _Optional[_Iterable[int]] = ..., stage: _Optional[int] = ..., result: _Optional[_Union[pb_bworld_result, _Mapping]] = ..., **kwargs) -> None: ...

class pb_bworld_result(_message.Message):
    __slots__ = ("num", "cost", "score", "progress", "boss_hp")
    NUM_FIELD_NUMBER: _ClassVar[int]
    COST_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_FIELD_NUMBER: _ClassVar[int]
    BOSS_HP_FIELD_NUMBER: _ClassVar[int]
    num: _containers.RepeatedScalarFieldContainer[int]
    cost: _containers.RepeatedScalarFieldContainer[int]
    score: int
    progress: int
    boss_hp: int
    def __init__(self, num: _Optional[_Iterable[int]] = ..., cost: _Optional[_Iterable[int]] = ..., score: _Optional[int] = ..., progress: _Optional[int] = ..., boss_hp: _Optional[int] = ...) -> None: ...

class pb_cele(_message.Message):
    __slots__ = ("id_god", "id_way", "task_up", "task_trans", "hid", "hid_map", "task_world", "skill_count")
    ID_GOD_FIELD_NUMBER: _ClassVar[int]
    ID_WAY_FIELD_NUMBER: _ClassVar[int]
    TASK_UP_FIELD_NUMBER: _ClassVar[int]
    TASK_TRANS_FIELD_NUMBER: _ClassVar[int]
    HID_FIELD_NUMBER: _ClassVar[int]
    HID_MAP_FIELD_NUMBER: _ClassVar[int]
    TASK_WORLD_FIELD_NUMBER: _ClassVar[int]
    SKILL_COUNT_FIELD_NUMBER: _ClassVar[int]
    id_god: int
    id_way: int
    task_up: _containers.RepeatedCompositeFieldContainer[pb_kv2]
    task_trans: _containers.RepeatedCompositeFieldContainer[pb_kv2]
    hid: int
    hid_map: _containers.RepeatedCompositeFieldContainer[pb_kv2]
    task_world: _containers.RepeatedScalarFieldContainer[int]
    skill_count: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, id_god: _Optional[int] = ..., id_way: _Optional[int] = ..., task_up: _Optional[_Iterable[_Union[pb_kv2, _Mapping]]] = ..., task_trans: _Optional[_Iterable[_Union[pb_kv2, _Mapping]]] = ..., hid: _Optional[int] = ..., hid_map: _Optional[_Iterable[_Union[pb_kv2, _Mapping]]] = ..., task_world: _Optional[_Iterable[int]] = ..., skill_count: _Optional[_Iterable[int]] = ...) -> None: ...

class pb_desk_hero(_message.Message):
    __slots__ = ("id", "hero", "back", "log")
    ID_FIELD_NUMBER: _ClassVar[int]
    HERO_FIELD_NUMBER: _ClassVar[int]
    BACK_FIELD_NUMBER: _ClassVar[int]
    LOG_FIELD_NUMBER: _ClassVar[int]
    id: int
    hero: _containers.RepeatedScalarFieldContainer[int]
    back: _containers.RepeatedScalarFieldContainer[int]
    log: _containers.RepeatedCompositeFieldContainer[pb_desk_log]
    def __init__(self, id: _Optional[int] = ..., hero: _Optional[_Iterable[int]] = ..., back: _Optional[_Iterable[int]] = ..., log: _Optional[_Iterable[_Union[pb_desk_log, _Mapping]]] = ...) -> None: ...

class pb_desk_log(_message.Message):
    __slots__ = ("id", "hero", "new", "index")
    ID_FIELD_NUMBER: _ClassVar[int]
    HERO_FIELD_NUMBER: _ClassVar[int]
    NEW_FIELD_NUMBER: _ClassVar[int]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    id: int
    hero: _containers.RepeatedCompositeFieldContainer[pb_kv]
    new: int
    index: int
    def __init__(self, id: _Optional[int] = ..., hero: _Optional[_Iterable[_Union[pb_kv, _Mapping]]] = ..., new: _Optional[int] = ..., index: _Optional[int] = ...) -> None: ...

class pb_cele_buf(_message.Message):
    __slots__ = ("id", "cd", "cd_shield", "color", "count", "key", "lv")
    ID_FIELD_NUMBER: _ClassVar[int]
    CD_FIELD_NUMBER: _ClassVar[int]
    CD_SHIELD_FIELD_NUMBER: _ClassVar[int]
    COLOR_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    LV_FIELD_NUMBER: _ClassVar[int]
    id: int
    cd: int
    cd_shield: int
    color: int
    count: int
    key: int
    lv: int
    def __init__(self, id: _Optional[int] = ..., cd: _Optional[int] = ..., cd_shield: _Optional[int] = ..., color: _Optional[int] = ..., count: _Optional[int] = ..., key: _Optional[int] = ..., lv: _Optional[int] = ...) -> None: ...

class pb_ret(_message.Message):
    __slots__ = ("num", "cd", "ids", "rewards")
    NUM_FIELD_NUMBER: _ClassVar[int]
    CD_FIELD_NUMBER: _ClassVar[int]
    IDS_FIELD_NUMBER: _ClassVar[int]
    REWARDS_FIELD_NUMBER: _ClassVar[int]
    num: _containers.RepeatedScalarFieldContainer[int]
    cd: int
    ids: _containers.RepeatedScalarFieldContainer[int]
    rewards: _containers.RepeatedCompositeFieldContainer[pb_bag]
    def __init__(self, num: _Optional[_Iterable[int]] = ..., cd: _Optional[int] = ..., ids: _Optional[_Iterable[int]] = ..., rewards: _Optional[_Iterable[_Union[pb_bag, _Mapping]]] = ...) -> None: ...
