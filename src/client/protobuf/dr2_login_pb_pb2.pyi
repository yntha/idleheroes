from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class pb_server(_message.Message):
    __slots__ = ("id", "ip", "port", "name", "status", "language", "nickname")
    ID_FIELD_NUMBER: _ClassVar[int]
    IP_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    NICKNAME_FIELD_NUMBER: _ClassVar[int]
    id: int
    ip: str
    port: int
    name: str
    status: int
    language: str
    nickname: str
    def __init__(self, id: _Optional[int] = ..., ip: _Optional[str] = ..., port: _Optional[int] = ..., name: _Optional[str] = ..., status: _Optional[int] = ..., language: _Optional[str] = ..., nickname: _Optional[str] = ...) -> None: ...

class pb_server_login(_message.Message):
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

class pbreq_echo(_message.Message):
    __slots__ = ("echo",)
    ECHO_FIELD_NUMBER: _ClassVar[int]
    echo: int
    def __init__(self, echo: _Optional[int] = ...) -> None: ...

class pbrsp_echo(_message.Message):
    __slots__ = ("echo",)
    ECHO_FIELD_NUMBER: _ClassVar[int]
    echo: int
    def __init__(self, echo: _Optional[int] = ...) -> None: ...

class pbreq_pub(_message.Message):
    __slots__ = ("language", "vsn")
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    VSN_FIELD_NUMBER: _ClassVar[int]
    language: int
    vsn: int
    def __init__(self, language: _Optional[int] = ..., vsn: _Optional[int] = ...) -> None: ...

class pbrsp_pub(_message.Message):
    __slots__ = ("status", "language", "vsn", "pub")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    VSN_FIELD_NUMBER: _ClassVar[int]
    PUB_FIELD_NUMBER: _ClassVar[int]
    status: int
    language: int
    vsn: int
    pub: str
    def __init__(self, status: _Optional[int] = ..., language: _Optional[int] = ..., vsn: _Optional[int] = ..., pub: _Optional[str] = ...) -> None: ...

class pbreq_reg(_message.Message):
    __slots__ = ("rdid", "appversion", "osversion", "env")
    RDID_FIELD_NUMBER: _ClassVar[int]
    APPVERSION_FIELD_NUMBER: _ClassVar[int]
    OSVERSION_FIELD_NUMBER: _ClassVar[int]
    ENV_FIELD_NUMBER: _ClassVar[int]
    rdid: str
    appversion: str
    osversion: str
    env: str
    def __init__(self, rdid: _Optional[str] = ..., appversion: _Optional[str] = ..., osversion: _Optional[str] = ..., env: _Optional[str] = ...) -> None: ...

class pbrsp_reg(_message.Message):
    __slots__ = ("status", "uid", "account", "password")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    status: int
    uid: int
    account: str
    password: str
    def __init__(self, status: _Optional[int] = ..., uid: _Optional[int] = ..., account: _Optional[str] = ..., password: _Optional[str] = ...) -> None: ...

class pbreq_salt(_message.Message):
    __slots__ = ("account",)
    ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    account: str
    def __init__(self, account: _Optional[str] = ...) -> None: ...

class pbrsp_salt(_message.Message):
    __slots__ = ("status", "salt", "uid", "flag", "cd")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    SALT_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    FLAG_FIELD_NUMBER: _ClassVar[int]
    CD_FIELD_NUMBER: _ClassVar[int]
    status: int
    salt: str
    uid: int
    flag: int
    cd: int
    def __init__(self, status: _Optional[int] = ..., salt: _Optional[str] = ..., uid: _Optional[int] = ..., flag: _Optional[int] = ..., cd: _Optional[int] = ...) -> None: ...

class pbreq_login(_message.Message):
    __slots__ = ("checksum", "idfa", "keychain", "idfv", "env")
    CHECKSUM_FIELD_NUMBER: _ClassVar[int]
    IDFA_FIELD_NUMBER: _ClassVar[int]
    KEYCHAIN_FIELD_NUMBER: _ClassVar[int]
    IDFV_FIELD_NUMBER: _ClassVar[int]
    ENV_FIELD_NUMBER: _ClassVar[int]
    checksum: str
    idfa: str
    keychain: str
    idfv: str
    env: str
    def __init__(self, checksum: _Optional[str] = ..., idfa: _Optional[str] = ..., keychain: _Optional[str] = ..., idfv: _Optional[str] = ..., env: _Optional[str] = ...) -> None: ...

class pbrsp_login(_message.Message):
    __slots__ = ("status", "session", "sid", "is_formal", "uid", "createTs")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    SESSION_FIELD_NUMBER: _ClassVar[int]
    SID_FIELD_NUMBER: _ClassVar[int]
    IS_FORMAL_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    CREATETS_FIELD_NUMBER: _ClassVar[int]
    status: int
    session: str
    sid: int
    is_formal: bool
    uid: int
    createTs: str
    def __init__(self, status: _Optional[int] = ..., session: _Optional[str] = ..., sid: _Optional[int] = ..., is_formal: _Optional[bool] = ..., uid: _Optional[int] = ..., createTs: _Optional[str] = ...) -> None: ...

class pbreq_thirdlogin(_message.Message):
    __slots__ = ("platform", "jsonStr")
    PLATFORM_FIELD_NUMBER: _ClassVar[int]
    JSONSTR_FIELD_NUMBER: _ClassVar[int]
    platform: str
    jsonStr: str
    def __init__(self, platform: _Optional[str] = ..., jsonStr: _Optional[str] = ...) -> None: ...

class pbrsp_thirdlogin(_message.Message):
    __slots__ = ("status", "session", "sid", "uid", "createTs", "ext", "mid", "flag", "cd")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    SESSION_FIELD_NUMBER: _ClassVar[int]
    SID_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    CREATETS_FIELD_NUMBER: _ClassVar[int]
    EXT_FIELD_NUMBER: _ClassVar[int]
    MID_FIELD_NUMBER: _ClassVar[int]
    FLAG_FIELD_NUMBER: _ClassVar[int]
    CD_FIELD_NUMBER: _ClassVar[int]
    status: int
    session: str
    sid: int
    uid: int
    createTs: str
    ext: str
    mid: int
    flag: int
    cd: int
    def __init__(self, status: _Optional[int] = ..., session: _Optional[str] = ..., sid: _Optional[int] = ..., uid: _Optional[int] = ..., createTs: _Optional[str] = ..., ext: _Optional[str] = ..., mid: _Optional[int] = ..., flag: _Optional[int] = ..., cd: _Optional[int] = ...) -> None: ...

class pbreq_servers_login(_message.Message):
    __slots__ = ("uid", "authcode")
    UID_FIELD_NUMBER: _ClassVar[int]
    AUTHCODE_FIELD_NUMBER: _ClassVar[int]
    uid: int
    authcode: str
    def __init__(self, uid: _Optional[int] = ..., authcode: _Optional[str] = ...) -> None: ...

class pbrsp_servers_login(_message.Message):
    __slots__ = ("servers", "recent_sid", "status", "g_servers", "g_recent_sid", "uid", "account", "password", "is_formal")
    SERVERS_FIELD_NUMBER: _ClassVar[int]
    RECENT_SID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    G_SERVERS_FIELD_NUMBER: _ClassVar[int]
    G_RECENT_SID_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    IS_FORMAL_FIELD_NUMBER: _ClassVar[int]
    servers: _containers.RepeatedCompositeFieldContainer[pb_server_login]
    recent_sid: int
    status: int
    g_servers: _containers.RepeatedCompositeFieldContainer[pb_server_login]
    g_recent_sid: int
    uid: int
    account: str
    password: str
    is_formal: bool
    def __init__(self, servers: _Optional[_Iterable[_Union[pb_server_login, _Mapping]]] = ..., recent_sid: _Optional[int] = ..., status: _Optional[int] = ..., g_servers: _Optional[_Iterable[_Union[pb_server_login, _Mapping]]] = ..., g_recent_sid: _Optional[int] = ..., uid: _Optional[int] = ..., account: _Optional[str] = ..., password: _Optional[str] = ..., is_formal: _Optional[bool] = ...) -> None: ...

class pbreq_pgs_login(_message.Message):
    __slots__ = ("authcode", "idfa", "keychain", "idfv", "env")
    AUTHCODE_FIELD_NUMBER: _ClassVar[int]
    IDFA_FIELD_NUMBER: _ClassVar[int]
    KEYCHAIN_FIELD_NUMBER: _ClassVar[int]
    IDFV_FIELD_NUMBER: _ClassVar[int]
    ENV_FIELD_NUMBER: _ClassVar[int]
    authcode: str
    idfa: str
    keychain: str
    idfv: str
    env: str
    def __init__(self, authcode: _Optional[str] = ..., idfa: _Optional[str] = ..., keychain: _Optional[str] = ..., idfv: _Optional[str] = ..., env: _Optional[str] = ...) -> None: ...

class pbrsp_pgs_login(_message.Message):
    __slots__ = ("status", "session", "sid", "is_formal", "uid", "createTs")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    SESSION_FIELD_NUMBER: _ClassVar[int]
    SID_FIELD_NUMBER: _ClassVar[int]
    IS_FORMAL_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    CREATETS_FIELD_NUMBER: _ClassVar[int]
    status: int
    session: str
    sid: int
    is_formal: bool
    uid: int
    createTs: str
    def __init__(self, status: _Optional[int] = ..., session: _Optional[str] = ..., sid: _Optional[int] = ..., is_formal: _Optional[bool] = ..., uid: _Optional[int] = ..., createTs: _Optional[str] = ...) -> None: ...
