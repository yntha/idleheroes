from . import dr2_comm_pb_pb2 as _dr2_comm_pb_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class pbreq_auth(_message.Message):
    __slots__ = ("session", "uid", "env", "ids", "support_zip")
    SESSION_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    ENV_FIELD_NUMBER: _ClassVar[int]
    IDS_FIELD_NUMBER: _ClassVar[int]
    SUPPORT_ZIP_FIELD_NUMBER: _ClassVar[int]
    session: str
    uid: int
    env: str
    ids: str
    support_zip: int
    def __init__(self, session: _Optional[str] = ..., uid: _Optional[int] = ..., env: _Optional[str] = ..., ids: _Optional[str] = ..., support_zip: _Optional[int] = ...) -> None: ...

class pbrsp_auth(_message.Message):
    __slots__ = ("status", "createTs", "ban_time", "capt")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    CREATETS_FIELD_NUMBER: _ClassVar[int]
    BAN_TIME_FIELD_NUMBER: _ClassVar[int]
    CAPT_FIELD_NUMBER: _ClassVar[int]
    status: int
    createTs: str
    ban_time: int
    capt: bytes
    def __init__(self, status: _Optional[int] = ..., createTs: _Optional[str] = ..., ban_time: _Optional[int] = ..., capt: _Optional[bytes] = ...) -> None: ...

class pbreq_sync(_message.Message):
    __slots__ = ("idfa", "keychain", "idfv")
    IDFA_FIELD_NUMBER: _ClassVar[int]
    KEYCHAIN_FIELD_NUMBER: _ClassVar[int]
    IDFV_FIELD_NUMBER: _ClassVar[int]
    idfa: str
    keychain: str
    idfv: str
    def __init__(self, idfa: _Optional[str] = ..., keychain: _Optional[str] = ..., idfv: _Optional[str] = ...) -> None: ...

class pbreq_trash(_message.Message):
    __slots__ = ("pwd",)
    PWD_FIELD_NUMBER: _ClassVar[int]
    pwd: str
    def __init__(self, pwd: _Optional[str] = ...) -> None: ...

class pbrsp_trash(_message.Message):
    __slots__ = ("status", "flag", "cd")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    FLAG_FIELD_NUMBER: _ClassVar[int]
    CD_FIELD_NUMBER: _ClassVar[int]
    status: int
    flag: int
    cd: int
    def __init__(self, status: _Optional[int] = ..., flag: _Optional[int] = ..., cd: _Optional[int] = ...) -> None: ...

class pbreq_resume(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class pbrsp_resume(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbrsp_sync(_message.Message):
    __slots__ = ("status", "player", "bag", "heroes", "gacha", "hero_ids", "mails", "midas_cd", "hook", "midas_crstcd", "pay_num", "tutorial", "friends", "trial", "alogin", "acts", "achieve", "tasks", "task_cd", "online", "midas_flag", "web_flag", "video_ad", "limitacts", "htask", "buy_hlimit", "space_gacha", "cds", "final_rank", "hide_vip", "tutorial2", "pets", "reddot", "gskls", "subscribed", "skin", "gsklcode", "chatblocks", "locale", "mact", "audit", "sact", "off_card", "video_cd", "ract", "use_hitem", "re_sync", "new_midas", "stele", "token", "stower_lv", "spet_ids", "skin_ids", "home_heroes", "coll_lv", "like", "care", "hteam_bag", "qlt_tasks", "give", "qscore", "mall_pwd", "qlt_pvp_market", "stower_lucky", "coll", "brave", "transform_num", "transform_choose", "god_lv", "energy", "gt_over", "cele", "ret")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    PLAYER_FIELD_NUMBER: _ClassVar[int]
    BAG_FIELD_NUMBER: _ClassVar[int]
    HEROES_FIELD_NUMBER: _ClassVar[int]
    GACHA_FIELD_NUMBER: _ClassVar[int]
    HERO_IDS_FIELD_NUMBER: _ClassVar[int]
    MAILS_FIELD_NUMBER: _ClassVar[int]
    MIDAS_CD_FIELD_NUMBER: _ClassVar[int]
    HOOK_FIELD_NUMBER: _ClassVar[int]
    MIDAS_CRSTCD_FIELD_NUMBER: _ClassVar[int]
    PAY_NUM_FIELD_NUMBER: _ClassVar[int]
    TUTORIAL_FIELD_NUMBER: _ClassVar[int]
    FRIENDS_FIELD_NUMBER: _ClassVar[int]
    TRIAL_FIELD_NUMBER: _ClassVar[int]
    ALOGIN_FIELD_NUMBER: _ClassVar[int]
    ACTS_FIELD_NUMBER: _ClassVar[int]
    ACHIEVE_FIELD_NUMBER: _ClassVar[int]
    TASKS_FIELD_NUMBER: _ClassVar[int]
    TASK_CD_FIELD_NUMBER: _ClassVar[int]
    ONLINE_FIELD_NUMBER: _ClassVar[int]
    MIDAS_FLAG_FIELD_NUMBER: _ClassVar[int]
    WEB_FLAG_FIELD_NUMBER: _ClassVar[int]
    VIDEO_AD_FIELD_NUMBER: _ClassVar[int]
    LIMITACTS_FIELD_NUMBER: _ClassVar[int]
    HTASK_FIELD_NUMBER: _ClassVar[int]
    BUY_HLIMIT_FIELD_NUMBER: _ClassVar[int]
    SPACE_GACHA_FIELD_NUMBER: _ClassVar[int]
    CDS_FIELD_NUMBER: _ClassVar[int]
    FINAL_RANK_FIELD_NUMBER: _ClassVar[int]
    HIDE_VIP_FIELD_NUMBER: _ClassVar[int]
    TUTORIAL2_FIELD_NUMBER: _ClassVar[int]
    PETS_FIELD_NUMBER: _ClassVar[int]
    REDDOT_FIELD_NUMBER: _ClassVar[int]
    GSKLS_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIBED_FIELD_NUMBER: _ClassVar[int]
    SKIN_FIELD_NUMBER: _ClassVar[int]
    GSKLCODE_FIELD_NUMBER: _ClassVar[int]
    CHATBLOCKS_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    MACT_FIELD_NUMBER: _ClassVar[int]
    AUDIT_FIELD_NUMBER: _ClassVar[int]
    SACT_FIELD_NUMBER: _ClassVar[int]
    OFF_CARD_FIELD_NUMBER: _ClassVar[int]
    VIDEO_CD_FIELD_NUMBER: _ClassVar[int]
    RACT_FIELD_NUMBER: _ClassVar[int]
    USE_HITEM_FIELD_NUMBER: _ClassVar[int]
    RE_SYNC_FIELD_NUMBER: _ClassVar[int]
    NEW_MIDAS_FIELD_NUMBER: _ClassVar[int]
    STELE_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    STOWER_LV_FIELD_NUMBER: _ClassVar[int]
    SPET_IDS_FIELD_NUMBER: _ClassVar[int]
    SKIN_IDS_FIELD_NUMBER: _ClassVar[int]
    HOME_HEROES_FIELD_NUMBER: _ClassVar[int]
    COLL_LV_FIELD_NUMBER: _ClassVar[int]
    LIKE_FIELD_NUMBER: _ClassVar[int]
    CARE_FIELD_NUMBER: _ClassVar[int]
    HTEAM_BAG_FIELD_NUMBER: _ClassVar[int]
    QLT_TASKS_FIELD_NUMBER: _ClassVar[int]
    GIVE_FIELD_NUMBER: _ClassVar[int]
    QSCORE_FIELD_NUMBER: _ClassVar[int]
    MALL_PWD_FIELD_NUMBER: _ClassVar[int]
    QLT_PVP_MARKET_FIELD_NUMBER: _ClassVar[int]
    STOWER_LUCKY_FIELD_NUMBER: _ClassVar[int]
    COLL_FIELD_NUMBER: _ClassVar[int]
    BRAVE_FIELD_NUMBER: _ClassVar[int]
    TRANSFORM_NUM_FIELD_NUMBER: _ClassVar[int]
    TRANSFORM_CHOOSE_FIELD_NUMBER: _ClassVar[int]
    GOD_LV_FIELD_NUMBER: _ClassVar[int]
    ENERGY_FIELD_NUMBER: _ClassVar[int]
    GT_OVER_FIELD_NUMBER: _ClassVar[int]
    CELE_FIELD_NUMBER: _ClassVar[int]
    RET_FIELD_NUMBER: _ClassVar[int]
    status: int
    player: _dr2_comm_pb_pb2.pb_player
    bag: _dr2_comm_pb_pb2.pb_bag
    heroes: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_hero]
    gacha: _dr2_comm_pb_pb2.pb_gacha
    hero_ids: _containers.RepeatedScalarFieldContainer[int]
    mails: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_mail]
    midas_cd: int
    hook: _dr2_comm_pb_pb2.pb_hook
    midas_crstcd: int
    pay_num: _containers.RepeatedScalarFieldContainer[int]
    tutorial: int
    friends: _dr2_comm_pb_pb2.pb_friend
    trial: _dr2_comm_pb_pb2.pb_strial
    alogin: _dr2_comm_pb_pb2.pb_alogin
    acts: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_act]
    achieve: _dr2_comm_pb_pb2.pb_sachieve
    tasks: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_task]
    task_cd: int
    online: _dr2_comm_pb_pb2.pb_online
    midas_flag: int
    web_flag: int
    video_ad: int
    limitacts: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_act]
    htask: _dr2_comm_pb_pb2.pb_htask_sync
    buy_hlimit: int
    space_gacha: int
    cds: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_cd]
    final_rank: int
    hide_vip: bool
    tutorial2: int
    pets: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_pet]
    reddot: int
    gskls: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_gskl]
    subscribed: int
    skin: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_item]
    gsklcode: int
    chatblocks: int
    locale: _dr2_comm_pb_pb2.pb_locale
    mact: _dr2_comm_pb_pb2.pb_mact
    audit: int
    sact: _dr2_comm_pb_pb2.pb_sact
    off_card: int
    video_cd: int
    ract: _dr2_comm_pb_pb2.pb_ract
    use_hitem: int
    re_sync: _dr2_comm_pb_pb2.pb_re_sync
    new_midas: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_midas]
    stele: _dr2_comm_pb_pb2.pb_stele
    token: str
    stower_lv: int
    spet_ids: _containers.RepeatedScalarFieldContainer[int]
    skin_ids: _containers.RepeatedScalarFieldContainer[int]
    home_heroes: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_home_heroes]
    coll_lv: _containers.RepeatedScalarFieldContainer[int]
    like: _containers.RepeatedScalarFieldContainer[int]
    care: _containers.RepeatedScalarFieldContainer[int]
    hteam_bag: _containers.RepeatedScalarFieldContainer[int]
    qlt_tasks: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_task]
    give: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_give_order]
    qscore: int
    mall_pwd: int
    qlt_pvp_market: int
    stower_lucky: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.stower_lucky]
    coll: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_kv]
    brave: int
    transform_num: int
    transform_choose: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_kv]
    god_lv: int
    energy: int
    gt_over: bool
    cele: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_cele]
    ret: _dr2_comm_pb_pb2.pb_ret
    def __init__(self, status: _Optional[int] = ..., player: _Optional[_Union[_dr2_comm_pb_pb2.pb_player, _Mapping]] = ..., bag: _Optional[_Union[_dr2_comm_pb_pb2.pb_bag, _Mapping]] = ..., heroes: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_hero, _Mapping]]] = ..., gacha: _Optional[_Union[_dr2_comm_pb_pb2.pb_gacha, _Mapping]] = ..., hero_ids: _Optional[_Iterable[int]] = ..., mails: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_mail, _Mapping]]] = ..., midas_cd: _Optional[int] = ..., hook: _Optional[_Union[_dr2_comm_pb_pb2.pb_hook, _Mapping]] = ..., midas_crstcd: _Optional[int] = ..., pay_num: _Optional[_Iterable[int]] = ..., tutorial: _Optional[int] = ..., friends: _Optional[_Union[_dr2_comm_pb_pb2.pb_friend, _Mapping]] = ..., trial: _Optional[_Union[_dr2_comm_pb_pb2.pb_strial, _Mapping]] = ..., alogin: _Optional[_Union[_dr2_comm_pb_pb2.pb_alogin, _Mapping]] = ..., acts: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_act, _Mapping]]] = ..., achieve: _Optional[_Union[_dr2_comm_pb_pb2.pb_sachieve, _Mapping]] = ..., tasks: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_task, _Mapping]]] = ..., task_cd: _Optional[int] = ..., online: _Optional[_Union[_dr2_comm_pb_pb2.pb_online, _Mapping]] = ..., midas_flag: _Optional[int] = ..., web_flag: _Optional[int] = ..., video_ad: _Optional[int] = ..., limitacts: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_act, _Mapping]]] = ..., htask: _Optional[_Union[_dr2_comm_pb_pb2.pb_htask_sync, _Mapping]] = ..., buy_hlimit: _Optional[int] = ..., space_gacha: _Optional[int] = ..., cds: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_cd, _Mapping]]] = ..., final_rank: _Optional[int] = ..., hide_vip: _Optional[bool] = ..., tutorial2: _Optional[int] = ..., pets: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_pet, _Mapping]]] = ..., reddot: _Optional[int] = ..., gskls: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_gskl, _Mapping]]] = ..., subscribed: _Optional[int] = ..., skin: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_item, _Mapping]]] = ..., gsklcode: _Optional[int] = ..., chatblocks: _Optional[int] = ..., locale: _Optional[_Union[_dr2_comm_pb_pb2.pb_locale, _Mapping]] = ..., mact: _Optional[_Union[_dr2_comm_pb_pb2.pb_mact, _Mapping]] = ..., audit: _Optional[int] = ..., sact: _Optional[_Union[_dr2_comm_pb_pb2.pb_sact, _Mapping]] = ..., off_card: _Optional[int] = ..., video_cd: _Optional[int] = ..., ract: _Optional[_Union[_dr2_comm_pb_pb2.pb_ract, _Mapping]] = ..., use_hitem: _Optional[int] = ..., re_sync: _Optional[_Union[_dr2_comm_pb_pb2.pb_re_sync, _Mapping]] = ..., new_midas: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_midas, _Mapping]]] = ..., stele: _Optional[_Union[_dr2_comm_pb_pb2.pb_stele, _Mapping]] = ..., token: _Optional[str] = ..., stower_lv: _Optional[int] = ..., spet_ids: _Optional[_Iterable[int]] = ..., skin_ids: _Optional[_Iterable[int]] = ..., home_heroes: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_home_heroes, _Mapping]]] = ..., coll_lv: _Optional[_Iterable[int]] = ..., like: _Optional[_Iterable[int]] = ..., care: _Optional[_Iterable[int]] = ..., hteam_bag: _Optional[_Iterable[int]] = ..., qlt_tasks: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_task, _Mapping]]] = ..., give: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_give_order, _Mapping]]] = ..., qscore: _Optional[int] = ..., mall_pwd: _Optional[int] = ..., qlt_pvp_market: _Optional[int] = ..., stower_lucky: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.stower_lucky, _Mapping]]] = ..., coll: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_kv, _Mapping]]] = ..., brave: _Optional[int] = ..., transform_num: _Optional[int] = ..., transform_choose: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_kv, _Mapping]]] = ..., god_lv: _Optional[int] = ..., energy: _Optional[int] = ..., gt_over: _Optional[bool] = ..., cele: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_cele, _Mapping]]] = ..., ret: _Optional[_Union[_dr2_comm_pb_pb2.pb_ret, _Mapping]] = ...) -> None: ...

class pbreq_up(_message.Message):
    __slots__ = ("vsn", "packagename")
    VSN_FIELD_NUMBER: _ClassVar[int]
    PACKAGENAME_FIELD_NUMBER: _ClassVar[int]
    vsn: str
    packagename: str
    def __init__(self, vsn: _Optional[str] = ..., packagename: _Optional[str] = ...) -> None: ...

class pbrsp_up(_message.Message):
    __slots__ = ("status", "vsn", "lv", "prefix", "files", "upList", "thcount", "appurl", "upurl")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    VSN_FIELD_NUMBER: _ClassVar[int]
    LV_FIELD_NUMBER: _ClassVar[int]
    PREFIX_FIELD_NUMBER: _ClassVar[int]
    FILES_FIELD_NUMBER: _ClassVar[int]
    UPLIST_FIELD_NUMBER: _ClassVar[int]
    THCOUNT_FIELD_NUMBER: _ClassVar[int]
    APPURL_FIELD_NUMBER: _ClassVar[int]
    UPURL_FIELD_NUMBER: _ClassVar[int]
    status: int
    vsn: str
    lv: int
    prefix: str
    files: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_upfile]
    upList: str
    thcount: int
    appurl: str
    upurl: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, status: _Optional[int] = ..., vsn: _Optional[str] = ..., lv: _Optional[int] = ..., prefix: _Optional[str] = ..., files: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_upfile, _Mapping]]] = ..., upList: _Optional[str] = ..., thcount: _Optional[int] = ..., appurl: _Optional[str] = ..., upurl: _Optional[_Iterable[str]] = ...) -> None: ...

class pbreq_bind(_message.Message):
    __slots__ = ("account", "password")
    ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    account: str
    password: str
    def __init__(self, account: _Optional[str] = ..., password: _Optional[str] = ...) -> None: ...

class pbrsp_bind(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_change_password(_message.Message):
    __slots__ = ("old", "new")
    OLD_FIELD_NUMBER: _ClassVar[int]
    NEW_FIELD_NUMBER: _ClassVar[int]
    old: str
    new: str
    def __init__(self, old: _Optional[str] = ..., new: _Optional[str] = ...) -> None: ...

class pbrsp_change_password(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_servers(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class pbrsp_servers(_message.Message):
    __slots__ = ("servers", "mid")
    SERVERS_FIELD_NUMBER: _ClassVar[int]
    MID_FIELD_NUMBER: _ClassVar[int]
    servers: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_server]
    mid: int
    def __init__(self, servers: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_server, _Mapping]]] = ..., mid: _Optional[int] = ...) -> None: ...

class pbreq_player(_message.Message):
    __slots__ = ("uid", "kind")
    UID_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    uid: int
    kind: int
    def __init__(self, uid: _Optional[int] = ..., kind: _Optional[int] = ...) -> None: ...

class pbrsp_player(_message.Message):
    __slots__ = ("gid", "gname", "heroes", "power", "report")
    GID_FIELD_NUMBER: _ClassVar[int]
    GNAME_FIELD_NUMBER: _ClassVar[int]
    HEROES_FIELD_NUMBER: _ClassVar[int]
    POWER_FIELD_NUMBER: _ClassVar[int]
    REPORT_FIELD_NUMBER: _ClassVar[int]
    gid: int
    gname: str
    heroes: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_unit]
    power: int
    report: int
    def __init__(self, gid: _Optional[int] = ..., gname: _Optional[str] = ..., heroes: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_unit, _Mapping]]] = ..., power: _Optional[int] = ..., report: _Optional[int] = ...) -> None: ...

class pbreq_change_name(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class pbrsp_change_name(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_change_logo(_message.Message):
    __slots__ = ("logo",)
    LOGO_FIELD_NUMBER: _ClassVar[int]
    logo: int
    def __init__(self, logo: _Optional[int] = ...) -> None: ...

class pbrsp_change_logo(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_rate_us(_message.Message):
    __slots__ = ("action",)
    ACTION_FIELD_NUMBER: _ClassVar[int]
    action: int
    def __init__(self, action: _Optional[int] = ...) -> None: ...

class pbrsp_rate_us(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_cdkey(_message.Message):
    __slots__ = ("key",)
    KEY_FIELD_NUMBER: _ClassVar[int]
    key: str
    def __init__(self, key: _Optional[str] = ...) -> None: ...

class pbrsp_cdkey(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_lpub(_message.Message):
    __slots__ = ("language", "vsn")
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    VSN_FIELD_NUMBER: _ClassVar[int]
    language: int
    vsn: int
    def __init__(self, language: _Optional[int] = ..., vsn: _Optional[int] = ...) -> None: ...

class pbrsp_lpub(_message.Message):
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

class pbreq_change_head_border(_message.Message):
    __slots__ = ("op", "border")
    OP_FIELD_NUMBER: _ClassVar[int]
    BORDER_FIELD_NUMBER: _ClassVar[int]
    op: int
    border: int
    def __init__(self, op: _Optional[int] = ..., border: _Optional[int] = ...) -> None: ...

class pbrsp_change_head_border(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_upgrade_head_border(_message.Message):
    __slots__ = ("border", "num", "equips")
    BORDER_FIELD_NUMBER: _ClassVar[int]
    NUM_FIELD_NUMBER: _ClassVar[int]
    EQUIPS_FIELD_NUMBER: _ClassVar[int]
    border: int
    num: int
    equips: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_equip]
    def __init__(self, border: _Optional[int] = ..., num: _Optional[int] = ..., equips: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_equip, _Mapping]]] = ...) -> None: ...

class pbrsp_upgrade_head_border(_message.Message):
    __slots__ = ("status", "num", "equip")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    NUM_FIELD_NUMBER: _ClassVar[int]
    EQUIP_FIELD_NUMBER: _ClassVar[int]
    status: int
    num: int
    equip: _dr2_comm_pb_pb2.pb_equip
    def __init__(self, status: _Optional[int] = ..., num: _Optional[int] = ..., equip: _Optional[_Union[_dr2_comm_pb_pb2.pb_equip, _Mapping]] = ...) -> None: ...

class pbreq_flag_webgame(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class pbrsp_flag_webgame(_message.Message):
    __slots__ = ("status", "flag", "reward")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    FLAG_FIELD_NUMBER: _ClassVar[int]
    REWARD_FIELD_NUMBER: _ClassVar[int]
    status: int
    flag: int
    reward: _dr2_comm_pb_pb2.pb_bag
    def __init__(self, status: _Optional[int] = ..., flag: _Optional[int] = ..., reward: _Optional[_Union[_dr2_comm_pb_pb2.pb_bag, _Mapping]] = ...) -> None: ...

class pbreq_smsg(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class pbrsp_smsg(_message.Message):
    __slots__ = ("msg",)
    MSG_FIELD_NUMBER: _ClassVar[int]
    msg: str
    def __init__(self, msg: _Optional[str] = ...) -> None: ...

class pbreq_audit(_message.Message):
    __slots__ = ("id", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class pbrsp_audit(_message.Message):
    __slots__ = ("status", "audit", "each_pay", "left_pay", "left_game_time")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    AUDIT_FIELD_NUMBER: _ClassVar[int]
    EACH_PAY_FIELD_NUMBER: _ClassVar[int]
    LEFT_PAY_FIELD_NUMBER: _ClassVar[int]
    LEFT_GAME_TIME_FIELD_NUMBER: _ClassVar[int]
    status: int
    audit: int
    each_pay: int
    left_pay: int
    left_game_time: int
    def __init__(self, status: _Optional[int] = ..., audit: _Optional[int] = ..., each_pay: _Optional[int] = ..., left_pay: _Optional[int] = ..., left_game_time: _Optional[int] = ...) -> None: ...

class pbreq_change_birthday(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class pbrsp_change_birthday(_message.Message):
    __slots__ = ("status", "cd", "read", "next", "loop")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    CD_FIELD_NUMBER: _ClassVar[int]
    READ_FIELD_NUMBER: _ClassVar[int]
    NEXT_FIELD_NUMBER: _ClassVar[int]
    LOOP_FIELD_NUMBER: _ClassVar[int]
    status: int
    cd: int
    read: int
    next: int
    loop: int
    def __init__(self, status: _Optional[int] = ..., cd: _Optional[int] = ..., read: _Optional[int] = ..., next: _Optional[int] = ..., loop: _Optional[int] = ...) -> None: ...

class pbreq_one_click(_message.Message):
    __slots__ = ("reqs",)
    REQS_FIELD_NUMBER: _ClassVar[int]
    reqs: str
    def __init__(self, reqs: _Optional[str] = ...) -> None: ...

class pbrsp_one_click(_message.Message):
    __slots__ = ("status", "rsps")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    RSPS_FIELD_NUMBER: _ClassVar[int]
    status: int
    rsps: str
    def __init__(self, status: _Optional[int] = ..., rsps: _Optional[str] = ...) -> None: ...

class pbreq_one_click_sync(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class pbrsp_one_click_sync(_message.Message):
    __slots__ = ("status", "rsps")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    RSPS_FIELD_NUMBER: _ClassVar[int]
    status: int
    rsps: str
    def __init__(self, status: _Optional[int] = ..., rsps: _Optional[str] = ...) -> None: ...

class pbreq_one_click_store(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class pbrsp_one_click_store(_message.Message):
    __slots__ = ("status", "rsps")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    RSPS_FIELD_NUMBER: _ClassVar[int]
    status: int
    rsps: str
    def __init__(self, status: _Optional[int] = ..., rsps: _Optional[str] = ...) -> None: ...

class pbrsp_json(_message.Message):
    __slots__ = ("json",)
    JSON_FIELD_NUMBER: _ClassVar[int]
    json: str
    def __init__(self, json: _Optional[str] = ...) -> None: ...

class pbreq_captcha(_message.Message):
    __slots__ = ("code",)
    CODE_FIELD_NUMBER: _ClassVar[int]
    code: str
    def __init__(self, code: _Optional[str] = ...) -> None: ...

class pbrsp_captcha(_message.Message):
    __slots__ = ("status", "png")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    PNG_FIELD_NUMBER: _ClassVar[int]
    status: int
    png: bytes
    def __init__(self, status: _Optional[int] = ..., png: _Optional[bytes] = ...) -> None: ...

class pbreq_gacha(_message.Message):
    __slots__ = ("type",)
    TYPE_FIELD_NUMBER: _ClassVar[int]
    type: int
    def __init__(self, type: _Optional[int] = ...) -> None: ...

class pbrsp_gacha(_message.Message):
    __slots__ = ("status", "heroes", "items", "gem")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    HEROES_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    GEM_FIELD_NUMBER: _ClassVar[int]
    status: int
    heroes: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_hero]
    items: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_item]
    gem: int
    def __init__(self, status: _Optional[int] = ..., heroes: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_hero, _Mapping]]] = ..., items: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_item, _Mapping]]] = ..., gem: _Optional[int] = ...) -> None: ...

class pbreq_wear(_message.Message):
    __slots__ = ("hid", "equips")
    HID_FIELD_NUMBER: _ClassVar[int]
    EQUIPS_FIELD_NUMBER: _ClassVar[int]
    hid: int
    equips: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_equip]
    def __init__(self, hid: _Optional[int] = ..., equips: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_equip, _Mapping]]] = ...) -> None: ...

class pbrsp_wear(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_hero_decompose(_message.Message):
    __slots__ = ("hid",)
    HID_FIELD_NUMBER: _ClassVar[int]
    hid: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, hid: _Optional[_Iterable[int]] = ...) -> None: ...

class pbrsp_hero_decompose(_message.Message):
    __slots__ = ("status", "items")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    status: int
    items: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_item]
    def __init__(self, status: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_item, _Mapping]]] = ...) -> None: ...

class pbreq_hero_merge(_message.Message):
    __slots__ = ("item",)
    ITEM_FIELD_NUMBER: _ClassVar[int]
    item: _dr2_comm_pb_pb2.pb_item
    def __init__(self, item: _Optional[_Union[_dr2_comm_pb_pb2.pb_item, _Mapping]] = ...) -> None: ...

class pbrsp_hero_merge(_message.Message):
    __slots__ = ("status", "heroes")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    HEROES_FIELD_NUMBER: _ClassVar[int]
    status: int
    heroes: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_hero]
    def __init__(self, status: _Optional[int] = ..., heroes: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_hero, _Mapping]]] = ...) -> None: ...

class pbreq_hero_up(_message.Message):
    __slots__ = ("hid", "type", "lv")
    HID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    LV_FIELD_NUMBER: _ClassVar[int]
    hid: int
    type: int
    lv: int
    def __init__(self, hid: _Optional[int] = ..., type: _Optional[int] = ..., lv: _Optional[int] = ...) -> None: ...

class pbrsp_hero_up(_message.Message):
    __slots__ = ("status", "lv")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    LV_FIELD_NUMBER: _ClassVar[int]
    status: int
    lv: int
    def __init__(self, status: _Optional[int] = ..., lv: _Optional[int] = ...) -> None: ...

class pbreq_hero_lock(_message.Message):
    __slots__ = ("hid", "lock")
    HID_FIELD_NUMBER: _ClassVar[int]
    LOCK_FIELD_NUMBER: _ClassVar[int]
    hid: int
    lock: int
    def __init__(self, hid: _Optional[int] = ..., lock: _Optional[int] = ...) -> None: ...

class pbrsp_hero_lock(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_hero_mix(_message.Message):
    __slots__ = ("id", "hids")
    ID_FIELD_NUMBER: _ClassVar[int]
    HIDS_FIELD_NUMBER: _ClassVar[int]
    id: int
    hids: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, id: _Optional[int] = ..., hids: _Optional[_Iterable[int]] = ...) -> None: ...

class pbrsp_hero_mix(_message.Message):
    __slots__ = ("status", "hero")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    HERO_FIELD_NUMBER: _ClassVar[int]
    status: int
    hero: _dr2_comm_pb_pb2.pb_hero
    def __init__(self, status: _Optional[int] = ..., hero: _Optional[_Union[_dr2_comm_pb_pb2.pb_hero, _Mapping]] = ...) -> None: ...

class pbreq_jade_on(_message.Message):
    __slots__ = ("hid",)
    HID_FIELD_NUMBER: _ClassVar[int]
    hid: int
    def __init__(self, hid: _Optional[int] = ...) -> None: ...

class pbrsp_jade_on(_message.Message):
    __slots__ = ("status", "jade")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    JADE_FIELD_NUMBER: _ClassVar[int]
    status: int
    jade: int
    def __init__(self, status: _Optional[int] = ..., jade: _Optional[int] = ...) -> None: ...

class pbreq_jade_up(_message.Message):
    __slots__ = ("hid", "gem", "qlt", "star")
    HID_FIELD_NUMBER: _ClassVar[int]
    GEM_FIELD_NUMBER: _ClassVar[int]
    QLT_FIELD_NUMBER: _ClassVar[int]
    STAR_FIELD_NUMBER: _ClassVar[int]
    hid: int
    gem: bool
    qlt: int
    star: int
    def __init__(self, hid: _Optional[int] = ..., gem: _Optional[bool] = ..., qlt: _Optional[int] = ..., star: _Optional[int] = ...) -> None: ...

class pbrsp_jade_up(_message.Message):
    __slots__ = ("status", "jade")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    JADE_FIELD_NUMBER: _ClassVar[int]
    status: int
    jade: int
    def __init__(self, status: _Optional[int] = ..., jade: _Optional[int] = ...) -> None: ...

class pbreq_jade_change(_message.Message):
    __slots__ = ("hid",)
    HID_FIELD_NUMBER: _ClassVar[int]
    hid: int
    def __init__(self, hid: _Optional[int] = ...) -> None: ...

class pbrsp_jade_change(_message.Message):
    __slots__ = ("status", "jade")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    JADE_FIELD_NUMBER: _ClassVar[int]
    status: int
    jade: int
    def __init__(self, status: _Optional[int] = ..., jade: _Optional[int] = ...) -> None: ...

class pbreq_jade_ok(_message.Message):
    __slots__ = ("hid", "pos")
    HID_FIELD_NUMBER: _ClassVar[int]
    POS_FIELD_NUMBER: _ClassVar[int]
    hid: int
    pos: int
    def __init__(self, hid: _Optional[int] = ..., pos: _Optional[int] = ...) -> None: ...

class pbrsp_jade_ok(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_buy_hlimit(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class pbrsp_buy_hlimit(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_transform_hero(_message.Message):
    __slots__ = ("hid",)
    HID_FIELD_NUMBER: _ClassVar[int]
    hid: int
    def __init__(self, hid: _Optional[int] = ...) -> None: ...

class pbrsp_transform_hero(_message.Message):
    __slots__ = ("status", "hero_id")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    HERO_ID_FIELD_NUMBER: _ClassVar[int]
    status: int
    hero_id: int
    def __init__(self, status: _Optional[int] = ..., hero_id: _Optional[int] = ...) -> None: ...

class pbreq_transform_ok(_message.Message):
    __slots__ = ("type",)
    TYPE_FIELD_NUMBER: _ClassVar[int]
    type: int
    def __init__(self, type: _Optional[int] = ...) -> None: ...

class pbrsp_transform_ok(_message.Message):
    __slots__ = ("status", "jade")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    JADE_FIELD_NUMBER: _ClassVar[int]
    status: int
    jade: int
    def __init__(self, status: _Optional[int] = ..., jade: _Optional[int] = ...) -> None: ...

class pbreq_hero_wake(_message.Message):
    __slots__ = ("hid", "source")
    HID_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    hid: int
    source: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, hid: _Optional[int] = ..., source: _Optional[_Iterable[int]] = ...) -> None: ...

class pbrsp_hero_wake(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_hero_change(_message.Message):
    __slots__ = ("hostHid", "hids")
    HOSTHID_FIELD_NUMBER: _ClassVar[int]
    HIDS_FIELD_NUMBER: _ClassVar[int]
    hostHid: int
    hids: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, hostHid: _Optional[int] = ..., hids: _Optional[_Iterable[int]] = ...) -> None: ...

class pbrsp_hero_change(_message.Message):
    __slots__ = ("status", "heroes", "items")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    HEROES_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    status: int
    heroes: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_hero]
    items: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_item]
    def __init__(self, status: _Optional[int] = ..., heroes: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_hero, _Mapping]]] = ..., items: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_item, _Mapping]]] = ...) -> None: ...

class pbreq_hero_skin_mix(_message.Message):
    __slots__ = ("item_id", "num")
    ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    NUM_FIELD_NUMBER: _ClassVar[int]
    item_id: int
    num: int
    def __init__(self, item_id: _Optional[int] = ..., num: _Optional[int] = ...) -> None: ...

class pbrsp_hero_skin_mix(_message.Message):
    __slots__ = ("status", "skin")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    SKIN_FIELD_NUMBER: _ClassVar[int]
    status: int
    skin: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_equip]
    def __init__(self, status: _Optional[int] = ..., skin: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_equip, _Mapping]]] = ...) -> None: ...

class pbreq_hero_skin_wear(_message.Message):
    __slots__ = ("hid", "skinid")
    HID_FIELD_NUMBER: _ClassVar[int]
    SKINID_FIELD_NUMBER: _ClassVar[int]
    hid: int
    skinid: int
    def __init__(self, hid: _Optional[int] = ..., skinid: _Optional[int] = ...) -> None: ...

class pbrsp_hero_skin_wear(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_hero_skin_off(_message.Message):
    __slots__ = ("hid",)
    HID_FIELD_NUMBER: _ClassVar[int]
    hid: int
    def __init__(self, hid: _Optional[int] = ...) -> None: ...

class pbrsp_hero_skin_off(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_shield_change(_message.Message):
    __slots__ = ("id", "hids")
    ID_FIELD_NUMBER: _ClassVar[int]
    HIDS_FIELD_NUMBER: _ClassVar[int]
    id: int
    hids: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, id: _Optional[int] = ..., hids: _Optional[_Iterable[int]] = ...) -> None: ...

class pbrsp_shield_change(_message.Message):
    __slots__ = ("status", "reward")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    REWARD_FIELD_NUMBER: _ClassVar[int]
    status: int
    reward: _dr2_comm_pb_pb2.pb_bag
    def __init__(self, status: _Optional[int] = ..., reward: _Optional[_Union[_dr2_comm_pb_pb2.pb_bag, _Mapping]] = ...) -> None: ...

class pbreq_hero_skin_visit(_message.Message):
    __slots__ = ("hid",)
    HID_FIELD_NUMBER: _ClassVar[int]
    hid: int
    def __init__(self, hid: _Optional[int] = ...) -> None: ...

class pbrsp_hero_skin_visit(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_hero_skin_breakdown(_message.Message):
    __slots__ = ("skin_id",)
    SKIN_ID_FIELD_NUMBER: _ClassVar[int]
    skin_id: int
    def __init__(self, skin_id: _Optional[int] = ...) -> None: ...

class pbrsp_hero_skin_breakdown(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_hero_talen(_message.Message):
    __slots__ = ("hid", "source", "skill_id")
    HID_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    SKILL_ID_FIELD_NUMBER: _ClassVar[int]
    hid: int
    source: _containers.RepeatedScalarFieldContainer[int]
    skill_id: int
    def __init__(self, hid: _Optional[int] = ..., source: _Optional[_Iterable[int]] = ..., skill_id: _Optional[int] = ...) -> None: ...

class pbrsp_hero_talen(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_hero_talenop(_message.Message):
    __slots__ = ("hid", "skill_id")
    HID_FIELD_NUMBER: _ClassVar[int]
    SKILL_ID_FIELD_NUMBER: _ClassVar[int]
    hid: int
    skill_id: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, hid: _Optional[int] = ..., skill_id: _Optional[_Iterable[int]] = ...) -> None: ...

class pbrsp_hero_talenop(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_hero_return(_message.Message):
    __slots__ = ("hid",)
    HID_FIELD_NUMBER: _ClassVar[int]
    hid: int
    def __init__(self, hid: _Optional[int] = ...) -> None: ...

class pbrsp_hero_return(_message.Message):
    __slots__ = ("status", "heroes", "items")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    HEROES_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    status: int
    heroes: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_hero]
    items: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_item]
    def __init__(self, status: _Optional[int] = ..., heroes: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_hero, _Mapping]]] = ..., items: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_item, _Mapping]]] = ...) -> None: ...

class pbreq_hero_skin_limitmix(_message.Message):
    __slots__ = ("skin_id",)
    SKIN_ID_FIELD_NUMBER: _ClassVar[int]
    skin_id: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, skin_id: _Optional[_Iterable[int]] = ...) -> None: ...

class pbrsp_hero_skin_limitmix(_message.Message):
    __slots__ = ("status", "skin_id")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    SKIN_ID_FIELD_NUMBER: _ClassVar[int]
    status: int
    skin_id: int
    def __init__(self, status: _Optional[int] = ..., skin_id: _Optional[int] = ...) -> None: ...

class pbreq_hero_skin_up(_message.Message):
    __slots__ = ("hid", "id", "skin_id")
    HID_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    SKIN_ID_FIELD_NUMBER: _ClassVar[int]
    hid: int
    id: int
    skin_id: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, hid: _Optional[int] = ..., id: _Optional[int] = ..., skin_id: _Optional[_Iterable[int]] = ...) -> None: ...

class pbrsp_hero_skin_up(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_hero_ticket(_message.Message):
    __slots__ = ("type", "count")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    type: int
    count: int
    def __init__(self, type: _Optional[int] = ..., count: _Optional[int] = ...) -> None: ...

class pbrsp_hero_ticket(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_jade_unlock(_message.Message):
    __slots__ = ("hid",)
    HID_FIELD_NUMBER: _ClassVar[int]
    hid: int
    def __init__(self, hid: _Optional[int] = ...) -> None: ...

class pbrsp_jade_unlock(_message.Message):
    __slots__ = ("status", "num")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    NUM_FIELD_NUMBER: _ClassVar[int]
    status: int
    num: int
    def __init__(self, status: _Optional[int] = ..., num: _Optional[int] = ...) -> None: ...

class pbreq_jade_used(_message.Message):
    __slots__ = ("hid", "pos")
    HID_FIELD_NUMBER: _ClassVar[int]
    POS_FIELD_NUMBER: _ClassVar[int]
    hid: int
    pos: int
    def __init__(self, hid: _Optional[int] = ..., pos: _Optional[int] = ...) -> None: ...

class pbrsp_jade_used(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_auto_lvup(_message.Message):
    __slots__ = ("type", "id", "lv", "sklid")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    LV_FIELD_NUMBER: _ClassVar[int]
    SKLID_FIELD_NUMBER: _ClassVar[int]
    type: int
    id: int
    lv: int
    sklid: int
    def __init__(self, type: _Optional[int] = ..., id: _Optional[int] = ..., lv: _Optional[int] = ..., sklid: _Optional[int] = ...) -> None: ...

class pbrsp_auto_lvup(_message.Message):
    __slots__ = ("status", "costs")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    COSTS_FIELD_NUMBER: _ClassVar[int]
    status: int
    costs: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_item]
    def __init__(self, status: _Optional[int] = ..., costs: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_item, _Mapping]]] = ...) -> None: ...

class pbreq_up_star(_message.Message):
    __slots__ = ("up", "star")
    UP_FIELD_NUMBER: _ClassVar[int]
    STAR_FIELD_NUMBER: _ClassVar[int]
    up: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_up_star]
    star: int
    def __init__(self, up: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_up_star, _Mapping]]] = ..., star: _Optional[int] = ...) -> None: ...

class pbrsp_up_star(_message.Message):
    __slots__ = ("status", "rewards")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    REWARDS_FIELD_NUMBER: _ClassVar[int]
    status: int
    rewards: _dr2_comm_pb_pb2.pb_bag
    def __init__(self, status: _Optional[int] = ..., rewards: _Optional[_Union[_dr2_comm_pb_pb2.pb_bag, _Mapping]] = ...) -> None: ...

class pbreq_gacha_choose(_message.Message):
    __slots__ = ("heroid",)
    HEROID_FIELD_NUMBER: _ClassVar[int]
    heroid: int
    def __init__(self, heroid: _Optional[int] = ...) -> None: ...

class pbrsp_gacha_choose(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_qlt_star(_message.Message):
    __slots__ = ("hid", "cost_id")
    HID_FIELD_NUMBER: _ClassVar[int]
    COST_ID_FIELD_NUMBER: _ClassVar[int]
    hid: int
    cost_id: int
    def __init__(self, hid: _Optional[int] = ..., cost_id: _Optional[int] = ...) -> None: ...

class pbrsp_qlt_star(_message.Message):
    __slots__ = ("status", "qlc")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    QLC_FIELD_NUMBER: _ClassVar[int]
    status: int
    qlc: _dr2_comm_pb_pb2.pb_hero_qlc
    def __init__(self, status: _Optional[int] = ..., qlc: _Optional[_Union[_dr2_comm_pb_pb2.pb_hero_qlc, _Mapping]] = ...) -> None: ...

class pbreq_qlt_change(_message.Message):
    __slots__ = ("hid", "qlc", "self_hid")
    HID_FIELD_NUMBER: _ClassVar[int]
    QLC_FIELD_NUMBER: _ClassVar[int]
    SELF_HID_FIELD_NUMBER: _ClassVar[int]
    hid: int
    qlc: _dr2_comm_pb_pb2.pb_hero_qlc
    self_hid: int
    def __init__(self, hid: _Optional[int] = ..., qlc: _Optional[_Union[_dr2_comm_pb_pb2.pb_hero_qlc, _Mapping]] = ..., self_hid: _Optional[int] = ...) -> None: ...

class pbrsp_qlt_change(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_qlt_refresh(_message.Message):
    __slots__ = ("hid",)
    HID_FIELD_NUMBER: _ClassVar[int]
    hid: int
    def __init__(self, hid: _Optional[int] = ...) -> None: ...

class pbrsp_qlt_reresh(_message.Message):
    __slots__ = ("status", "attr_idx")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ATTR_IDX_FIELD_NUMBER: _ClassVar[int]
    status: int
    attr_idx: int
    def __init__(self, status: _Optional[int] = ..., attr_idx: _Optional[int] = ...) -> None: ...

class pbreq_qlt_refresh_ok(_message.Message):
    __slots__ = ("ok",)
    OK_FIELD_NUMBER: _ClassVar[int]
    ok: int
    def __init__(self, ok: _Optional[int] = ...) -> None: ...

class pbrsp_qlt_refresh_ok(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_qlt_claim(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class pbrsp_qlt_claim(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_qlt_sync(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class pbrsp_qlt_sync(_message.Message):
    __slots__ = ("cd",)
    CD_FIELD_NUMBER: _ClassVar[int]
    cd: int
    def __init__(self, cd: _Optional[int] = ...) -> None: ...

class pbreq_qlt_up(_message.Message):
    __slots__ = ("hid", "qlc", "type", "hids", "is_cur")
    HID_FIELD_NUMBER: _ClassVar[int]
    QLC_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    HIDS_FIELD_NUMBER: _ClassVar[int]
    IS_CUR_FIELD_NUMBER: _ClassVar[int]
    hid: int
    qlc: _dr2_comm_pb_pb2.pb_hero_qlc
    type: int
    hids: _containers.RepeatedScalarFieldContainer[int]
    is_cur: bool
    def __init__(self, hid: _Optional[int] = ..., qlc: _Optional[_Union[_dr2_comm_pb_pb2.pb_hero_qlc, _Mapping]] = ..., type: _Optional[int] = ..., hids: _Optional[_Iterable[int]] = ..., is_cur: _Optional[bool] = ...) -> None: ...

class pbrsp_qlt_up(_message.Message):
    __slots__ = ("status", "qlc", "item")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    QLC_FIELD_NUMBER: _ClassVar[int]
    ITEM_FIELD_NUMBER: _ClassVar[int]
    status: int
    qlc: _dr2_comm_pb_pb2.pb_hero_qlc
    item: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_item]
    def __init__(self, status: _Optional[int] = ..., qlc: _Optional[_Union[_dr2_comm_pb_pb2.pb_hero_qlc, _Mapping]] = ..., item: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_item, _Mapping]]] = ...) -> None: ...

class pbreq_batch_qlt_star(_message.Message):
    __slots__ = ("hids", "cost_id")
    HIDS_FIELD_NUMBER: _ClassVar[int]
    COST_ID_FIELD_NUMBER: _ClassVar[int]
    hids: _containers.RepeatedScalarFieldContainer[int]
    cost_id: int
    def __init__(self, hids: _Optional[_Iterable[int]] = ..., cost_id: _Optional[int] = ...) -> None: ...

class pbrsp_batch_qlt_star(_message.Message):
    __slots__ = ("status", "qlcs")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    QLCS_FIELD_NUMBER: _ClassVar[int]
    status: int
    qlcs: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_hero_qlc]
    def __init__(self, status: _Optional[int] = ..., qlcs: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_hero_qlc, _Mapping]]] = ...) -> None: ...

class pbreq_tree_up(_message.Message):
    __slots__ = ("hid", "src", "type", "lv")
    HID_FIELD_NUMBER: _ClassVar[int]
    SRC_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    LV_FIELD_NUMBER: _ClassVar[int]
    hid: int
    src: _containers.RepeatedScalarFieldContainer[int]
    type: int
    lv: int
    def __init__(self, hid: _Optional[int] = ..., src: _Optional[_Iterable[int]] = ..., type: _Optional[int] = ..., lv: _Optional[int] = ...) -> None: ...

class pbrsp_tree_up(_message.Message):
    __slots__ = ("status", "reward")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    REWARD_FIELD_NUMBER: _ClassVar[int]
    status: int
    reward: _dr2_comm_pb_pb2.pb_bag
    def __init__(self, status: _Optional[int] = ..., reward: _Optional[_Union[_dr2_comm_pb_pb2.pb_bag, _Mapping]] = ...) -> None: ...

class pbreq_merge_tequip(_message.Message):
    __slots__ = ("id", "num")
    ID_FIELD_NUMBER: _ClassVar[int]
    NUM_FIELD_NUMBER: _ClassVar[int]
    id: int
    num: int
    def __init__(self, id: _Optional[int] = ..., num: _Optional[int] = ...) -> None: ...

class pbrsp_merge_tequip(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_up_tequip(_message.Message):
    __slots__ = ("id", "hid", "src")
    ID_FIELD_NUMBER: _ClassVar[int]
    HID_FIELD_NUMBER: _ClassVar[int]
    SRC_FIELD_NUMBER: _ClassVar[int]
    id: int
    hid: int
    src: int
    def __init__(self, id: _Optional[int] = ..., hid: _Optional[int] = ..., src: _Optional[int] = ...) -> None: ...

class pbrsp_up_tequip(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_tequip_wear(_message.Message):
    __slots__ = ("hid", "id")
    HID_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    hid: int
    id: int
    def __init__(self, hid: _Optional[int] = ..., id: _Optional[int] = ...) -> None: ...

class pbrsp_tequip_wear(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_tequip_off(_message.Message):
    __slots__ = ("hid",)
    HID_FIELD_NUMBER: _ClassVar[int]
    hid: int
    def __init__(self, hid: _Optional[int] = ...) -> None: ...

class pbrsp_tequip_off(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_hero_sbreak(_message.Message):
    __slots__ = ("hid",)
    HID_FIELD_NUMBER: _ClassVar[int]
    hid: int
    def __init__(self, hid: _Optional[int] = ...) -> None: ...

class pbrsp_hero_sbreak(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_transform_choose(_message.Message):
    __slots__ = ("choose",)
    CHOOSE_FIELD_NUMBER: _ClassVar[int]
    choose: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_kv]
    def __init__(self, choose: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_kv, _Mapping]]] = ...) -> None: ...

class pbrsp_transform_choose(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_faith_up(_message.Message):
    __slots__ = ("hid", "lv")
    HID_FIELD_NUMBER: _ClassVar[int]
    LV_FIELD_NUMBER: _ClassVar[int]
    hid: int
    lv: int
    def __init__(self, hid: _Optional[int] = ..., lv: _Optional[int] = ...) -> None: ...

class pbrsp_faith_up(_message.Message):
    __slots__ = ("status", "faith")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    FAITH_FIELD_NUMBER: _ClassVar[int]
    status: int
    faith: _dr2_comm_pb_pb2.pb_faith
    def __init__(self, status: _Optional[int] = ..., faith: _Optional[_Union[_dr2_comm_pb_pb2.pb_faith, _Mapping]] = ...) -> None: ...

class pbreq_faith_lv(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class pbrsp_faith_lv(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_faith_skill(_message.Message):
    __slots__ = ("hid", "skill")
    HID_FIELD_NUMBER: _ClassVar[int]
    SKILL_FIELD_NUMBER: _ClassVar[int]
    hid: int
    skill: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, hid: _Optional[int] = ..., skill: _Optional[_Iterable[int]] = ...) -> None: ...

class pbrsp_faith_skill(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_faith_return(_message.Message):
    __slots__ = ("hid",)
    HID_FIELD_NUMBER: _ClassVar[int]
    hid: int
    def __init__(self, hid: _Optional[int] = ...) -> None: ...

class pbrsp_faith_return(_message.Message):
    __slots__ = ("status", "item")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ITEM_FIELD_NUMBER: _ClassVar[int]
    status: int
    item: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_item]
    def __init__(self, status: _Optional[int] = ..., item: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_item, _Mapping]]] = ...) -> None: ...

class pbreq_energy_resolve(_message.Message):
    __slots__ = ("hid",)
    HID_FIELD_NUMBER: _ClassVar[int]
    hid: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, hid: _Optional[_Iterable[int]] = ...) -> None: ...

class pbrsp_energy_resolve(_message.Message):
    __slots__ = ("status", "item", "energy")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ITEM_FIELD_NUMBER: _ClassVar[int]
    ENERGY_FIELD_NUMBER: _ClassVar[int]
    status: int
    item: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_item]
    energy: int
    def __init__(self, status: _Optional[int] = ..., item: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_item, _Mapping]]] = ..., energy: _Optional[int] = ...) -> None: ...

class pbreq_energy_hero(_message.Message):
    __slots__ = ("hid", "qlc", "energy")
    HID_FIELD_NUMBER: _ClassVar[int]
    QLC_FIELD_NUMBER: _ClassVar[int]
    ENERGY_FIELD_NUMBER: _ClassVar[int]
    hid: int
    qlc: _dr2_comm_pb_pb2.pb_hero_qlc
    energy: int
    def __init__(self, hid: _Optional[int] = ..., qlc: _Optional[_Union[_dr2_comm_pb_pb2.pb_hero_qlc, _Mapping]] = ..., energy: _Optional[int] = ...) -> None: ...

class pbrsp_energy_hero(_message.Message):
    __slots__ = ("status", "energy")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ENERGY_FIELD_NUMBER: _ClassVar[int]
    status: int
    energy: int
    def __init__(self, status: _Optional[int] = ..., energy: _Optional[int] = ...) -> None: ...

class pbreq_op_mail(_message.Message):
    __slots__ = ("reads", "deletes", "affixs", "blocks")
    READS_FIELD_NUMBER: _ClassVar[int]
    DELETES_FIELD_NUMBER: _ClassVar[int]
    AFFIXS_FIELD_NUMBER: _ClassVar[int]
    BLOCKS_FIELD_NUMBER: _ClassVar[int]
    reads: _containers.RepeatedScalarFieldContainer[int]
    deletes: _containers.RepeatedScalarFieldContainer[int]
    affixs: _containers.RepeatedScalarFieldContainer[int]
    blocks: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, reads: _Optional[_Iterable[int]] = ..., deletes: _Optional[_Iterable[int]] = ..., affixs: _Optional[_Iterable[int]] = ..., blocks: _Optional[_Iterable[int]] = ...) -> None: ...

class pbrsp_op_mail(_message.Message):
    __slots__ = ("status", "affix")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    AFFIX_FIELD_NUMBER: _ClassVar[int]
    status: int
    affix: _dr2_comm_pb_pb2.pb_bag
    def __init__(self, status: _Optional[int] = ..., affix: _Optional[_Union[_dr2_comm_pb_pb2.pb_bag, _Mapping]] = ...) -> None: ...

class pbreq_send_mail(_message.Message):
    __slots__ = ("uid", "pname", "content", "mid")
    UID_FIELD_NUMBER: _ClassVar[int]
    PNAME_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    MID_FIELD_NUMBER: _ClassVar[int]
    uid: int
    pname: str
    content: str
    mid: int
    def __init__(self, uid: _Optional[int] = ..., pname: _Optional[str] = ..., content: _Optional[str] = ..., mid: _Optional[int] = ...) -> None: ...

class pbrsp_send_mail(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_sell(_message.Message):
    __slots__ = ("items", "equips")
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    EQUIPS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_item]
    equips: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_equip]
    def __init__(self, items: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_item, _Mapping]]] = ..., equips: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_equip, _Mapping]]] = ...) -> None: ...

class pbrsp_sell(_message.Message):
    __slots__ = ("status", "item")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ITEM_FIELD_NUMBER: _ClassVar[int]
    status: int
    item: _dr2_comm_pb_pb2.pb_item
    def __init__(self, status: _Optional[int] = ..., item: _Optional[_Union[_dr2_comm_pb_pb2.pb_item, _Mapping]] = ...) -> None: ...

class pbreq_midas(_message.Message):
    __slots__ = ("type",)
    TYPE_FIELD_NUMBER: _ClassVar[int]
    type: int
    def __init__(self, type: _Optional[int] = ...) -> None: ...

class pbrsp_midas(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_merge_treasure(_message.Message):
    __slots__ = ("item",)
    ITEM_FIELD_NUMBER: _ClassVar[int]
    item: _dr2_comm_pb_pb2.pb_item
    def __init__(self, item: _Optional[_Union[_dr2_comm_pb_pb2.pb_item, _Mapping]] = ...) -> None: ...

class pbrsp_merge_treasure(_message.Message):
    __slots__ = ("status", "equip")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    EQUIP_FIELD_NUMBER: _ClassVar[int]
    status: int
    equip: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_equip]
    def __init__(self, status: _Optional[int] = ..., equip: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_equip, _Mapping]]] = ...) -> None: ...

class pbreq_up_treasure(_message.Message):
    __slots__ = ("id", "source", "hid")
    ID_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    HID_FIELD_NUMBER: _ClassVar[int]
    id: int
    source: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_item]
    hid: int
    def __init__(self, id: _Optional[int] = ..., source: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_item, _Mapping]]] = ..., hid: _Optional[int] = ...) -> None: ...

class pbrsp_up_treasure(_message.Message):
    __slots__ = ("status", "over")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    OVER_FIELD_NUMBER: _ClassVar[int]
    status: int
    over: int
    def __init__(self, status: _Optional[int] = ..., over: _Optional[int] = ...) -> None: ...

class pbreq_equip_merge(_message.Message):
    __slots__ = ("id", "num")
    ID_FIELD_NUMBER: _ClassVar[int]
    NUM_FIELD_NUMBER: _ClassVar[int]
    id: int
    num: int
    def __init__(self, id: _Optional[int] = ..., num: _Optional[int] = ...) -> None: ...

class pbrsp_equip_merge(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_exchange_act(_message.Message):
    __slots__ = ("id", "num", "sub")
    ID_FIELD_NUMBER: _ClassVar[int]
    NUM_FIELD_NUMBER: _ClassVar[int]
    SUB_FIELD_NUMBER: _ClassVar[int]
    id: int
    num: int
    sub: int
    def __init__(self, id: _Optional[int] = ..., num: _Optional[int] = ..., sub: _Optional[int] = ...) -> None: ...

class pbrsp_exchange_act(_message.Message):
    __slots__ = ("status", "affix")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    AFFIX_FIELD_NUMBER: _ClassVar[int]
    status: int
    affix: _dr2_comm_pb_pb2.pb_bag
    def __init__(self, status: _Optional[int] = ..., affix: _Optional[_Union[_dr2_comm_pb_pb2.pb_bag, _Mapping]] = ...) -> None: ...

class pbreq_open_gift(_message.Message):
    __slots__ = ("item", "num", "dest")
    ITEM_FIELD_NUMBER: _ClassVar[int]
    NUM_FIELD_NUMBER: _ClassVar[int]
    DEST_FIELD_NUMBER: _ClassVar[int]
    item: int
    num: int
    dest: int
    def __init__(self, item: _Optional[int] = ..., num: _Optional[int] = ..., dest: _Optional[int] = ...) -> None: ...

class pbrsp_open_gift(_message.Message):
    __slots__ = ("status", "reward")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    REWARD_FIELD_NUMBER: _ClassVar[int]
    status: int
    reward: _dr2_comm_pb_pb2.pb_bag
    def __init__(self, status: _Optional[int] = ..., reward: _Optional[_Union[_dr2_comm_pb_pb2.pb_bag, _Mapping]] = ...) -> None: ...

class pbreq_dwarf(_message.Message):
    __slots__ = ("id", "reward", "eids")
    ID_FIELD_NUMBER: _ClassVar[int]
    REWARD_FIELD_NUMBER: _ClassVar[int]
    EIDS_FIELD_NUMBER: _ClassVar[int]
    id: int
    reward: int
    eids: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, id: _Optional[int] = ..., reward: _Optional[int] = ..., eids: _Optional[_Iterable[int]] = ...) -> None: ...

class pbrsp_dwarf(_message.Message):
    __slots__ = ("status", "reward")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    REWARD_FIELD_NUMBER: _ClassVar[int]
    status: int
    reward: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_equip]
    def __init__(self, status: _Optional[int] = ..., reward: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_equip, _Mapping]]] = ...) -> None: ...

class pbreq_equip_resolve(_message.Message):
    __slots__ = ("equips",)
    EQUIPS_FIELD_NUMBER: _ClassVar[int]
    equips: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_equip]
    def __init__(self, equips: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_equip, _Mapping]]] = ...) -> None: ...

class pbrsp_equip_resolve(_message.Message):
    __slots__ = ("status", "reward")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    REWARD_FIELD_NUMBER: _ClassVar[int]
    status: int
    reward: _dr2_comm_pb_pb2.pb_item
    def __init__(self, status: _Optional[int] = ..., reward: _Optional[_Union[_dr2_comm_pb_pb2.pb_item, _Mapping]] = ...) -> None: ...

class pbreq_equip_soul(_message.Message):
    __slots__ = ("eid", "type", "hid", "hero_id")
    EID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    HID_FIELD_NUMBER: _ClassVar[int]
    HERO_ID_FIELD_NUMBER: _ClassVar[int]
    eid: int
    type: int
    hid: int
    hero_id: int
    def __init__(self, eid: _Optional[int] = ..., type: _Optional[int] = ..., hid: _Optional[int] = ..., hero_id: _Optional[int] = ...) -> None: ...

class pbrsp_equip_soul(_message.Message):
    __slots__ = ("status", "hid")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    HID_FIELD_NUMBER: _ClassVar[int]
    status: int
    hid: int
    def __init__(self, status: _Optional[int] = ..., hid: _Optional[int] = ...) -> None: ...

class pbreq_equip_soul_ok(_message.Message):
    __slots__ = ("flag",)
    FLAG_FIELD_NUMBER: _ClassVar[int]
    flag: int
    def __init__(self, flag: _Optional[int] = ...) -> None: ...

class pbrsp_equip_soul_ok(_message.Message):
    __slots__ = ("status", "equip")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    EQUIP_FIELD_NUMBER: _ClassVar[int]
    status: int
    equip: _dr2_comm_pb_pb2.pb_equip
    def __init__(self, status: _Optional[int] = ..., equip: _Optional[_Union[_dr2_comm_pb_pb2.pb_equip, _Mapping]] = ...) -> None: ...

class pbreq_equip_soul_sync(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class pbrsp_equip_soul_sync(_message.Message):
    __slots__ = ("status", "eid", "hid", "times", "hero_id")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    EID_FIELD_NUMBER: _ClassVar[int]
    HID_FIELD_NUMBER: _ClassVar[int]
    TIMES_FIELD_NUMBER: _ClassVar[int]
    HERO_ID_FIELD_NUMBER: _ClassVar[int]
    status: int
    eid: int
    hid: int
    times: int
    hero_id: int
    def __init__(self, status: _Optional[int] = ..., eid: _Optional[int] = ..., hid: _Optional[int] = ..., times: _Optional[int] = ..., hero_id: _Optional[int] = ...) -> None: ...

class pbreq_dwarf_change(_message.Message):
    __slots__ = ("id", "src", "dst")
    ID_FIELD_NUMBER: _ClassVar[int]
    SRC_FIELD_NUMBER: _ClassVar[int]
    DST_FIELD_NUMBER: _ClassVar[int]
    id: int
    src: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_equip]
    dst: int
    def __init__(self, id: _Optional[int] = ..., src: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_equip, _Mapping]]] = ..., dst: _Optional[int] = ...) -> None: ...

class pbrsp_dwarf_change(_message.Message):
    __slots__ = ("status", "reward")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    REWARD_FIELD_NUMBER: _ClassVar[int]
    status: int
    reward: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_equip]
    def __init__(self, status: _Optional[int] = ..., reward: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_equip, _Mapping]]] = ...) -> None: ...

class pbreq_exchange_skin(_message.Message):
    __slots__ = ("src", "con", "dst")
    SRC_FIELD_NUMBER: _ClassVar[int]
    CON_FIELD_NUMBER: _ClassVar[int]
    DST_FIELD_NUMBER: _ClassVar[int]
    src: int
    con: _containers.RepeatedScalarFieldContainer[int]
    dst: int
    def __init__(self, src: _Optional[int] = ..., con: _Optional[_Iterable[int]] = ..., dst: _Optional[int] = ...) -> None: ...

class pbrsp_exchange_skin(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_collect_sync(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class pbrsp_collect_sync(_message.Message):
    __slots__ = ("status", "data", "bag", "summon", "emblem")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    BAG_FIELD_NUMBER: _ClassVar[int]
    SUMMON_FIELD_NUMBER: _ClassVar[int]
    EMBLEM_FIELD_NUMBER: _ClassVar[int]
    status: int
    data: _dr2_comm_pb_pb2.pb_kvs
    bag: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_kv]
    summon: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_kv2]
    emblem: int
    def __init__(self, status: _Optional[int] = ..., data: _Optional[_Union[_dr2_comm_pb_pb2.pb_kvs, _Mapping]] = ..., bag: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_kv, _Mapping]]] = ..., summon: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_kv2, _Mapping]]] = ..., emblem: _Optional[int] = ...) -> None: ...

class pbreq_collect_summon(_message.Message):
    __slots__ = ("type", "id")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    type: int
    id: int
    def __init__(self, type: _Optional[int] = ..., id: _Optional[int] = ...) -> None: ...

class pbrsp_collect_summon(_message.Message):
    __slots__ = ("status", "reward", "count")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    REWARD_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    status: int
    reward: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_kv2]
    count: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, status: _Optional[int] = ..., reward: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_kv2, _Mapping]]] = ..., count: _Optional[_Iterable[int]] = ...) -> None: ...

class pbreq_collect_up(_message.Message):
    __slots__ = ("id_lv",)
    ID_LV_FIELD_NUMBER: _ClassVar[int]
    id_lv: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_kv]
    def __init__(self, id_lv: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_kv, _Mapping]]] = ...) -> None: ...

class pbrsp_collect_up(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_collect_handler(_message.Message):
    __slots__ = ("coll", "type")
    COLL_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    coll: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_item]
    type: int
    def __init__(self, coll: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_item, _Mapping]]] = ..., type: _Optional[int] = ...) -> None: ...

class pbrsp_collect_handler(_message.Message):
    __slots__ = ("status", "reward")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    REWARD_FIELD_NUMBER: _ClassVar[int]
    status: int
    reward: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_item]
    def __init__(self, status: _Optional[int] = ..., reward: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_item, _Mapping]]] = ...) -> None: ...

class pbreq_collect_reward(_message.Message):
    __slots__ = ("ids", "type")
    IDS_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ids: _containers.RepeatedScalarFieldContainer[int]
    type: int
    def __init__(self, ids: _Optional[_Iterable[int]] = ..., type: _Optional[int] = ...) -> None: ...

class pbrsp_collect_reward(_message.Message):
    __slots__ = ("status", "rewards")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    REWARDS_FIELD_NUMBER: _ClassVar[int]
    status: int
    rewards: _dr2_comm_pb_pb2.pb_bag
    def __init__(self, status: _Optional[int] = ..., rewards: _Optional[_Union[_dr2_comm_pb_pb2.pb_bag, _Mapping]] = ...) -> None: ...

class pbreq_collect_goods_rank(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class pbrsp_collect_goods_rank(_message.Message):
    __slots__ = ("status", "rank")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    RANK_FIELD_NUMBER: _ClassVar[int]
    status: int
    rank: _dr2_comm_pb_pb2.pb_smbrs
    def __init__(self, status: _Optional[int] = ..., rank: _Optional[_Union[_dr2_comm_pb_pb2.pb_smbrs, _Mapping]] = ...) -> None: ...

class pbreq_collect_select(_message.Message):
    __slots__ = ("id", "type")
    ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    id: int
    type: int
    def __init__(self, id: _Optional[int] = ..., type: _Optional[int] = ...) -> None: ...

class pbrsp_collect_select(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_collect_set_show(_message.Message):
    __slots__ = ("emblem",)
    EMBLEM_FIELD_NUMBER: _ClassVar[int]
    emblem: int
    def __init__(self, emblem: _Optional[int] = ...) -> None: ...

class pbrsp_collect_set_show(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_items_exchange(_message.Message):
    __slots__ = ("type", "num", "id")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    NUM_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    type: int
    num: int
    id: int
    def __init__(self, type: _Optional[int] = ..., num: _Optional[int] = ..., id: _Optional[int] = ...) -> None: ...

class pbrsp_items_exchange(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_sync_chat(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class pbrsp_sync_chat(_message.Message):
    __slots__ = ("msgs",)
    MSGS_FIELD_NUMBER: _ClassVar[int]
    msgs: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_chat]
    def __init__(self, msgs: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_chat, _Mapping]]] = ...) -> None: ...

class pbreq_chat(_message.Message):
    __slots__ = ("type", "text", "hid", "gud_imsg")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    HID_FIELD_NUMBER: _ClassVar[int]
    GUD_IMSG_FIELD_NUMBER: _ClassVar[int]
    type: int
    text: str
    hid: int
    gud_imsg: str
    def __init__(self, type: _Optional[int] = ..., text: _Optional[str] = ..., hid: _Optional[int] = ..., gud_imsg: _Optional[str] = ...) -> None: ...

class pbrsp_chat(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_cunit(_message.Message):
    __slots__ = ("share_id",)
    SHARE_ID_FIELD_NUMBER: _ClassVar[int]
    share_id: int
    def __init__(self, share_id: _Optional[int] = ...) -> None: ...

class pbrsp_cunit(_message.Message):
    __slots__ = ("status", "unit")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    UNIT_FIELD_NUMBER: _ClassVar[int]
    status: int
    unit: _dr2_comm_pb_pb2.pb_cunit
    def __init__(self, status: _Optional[int] = ..., unit: _Optional[_Union[_dr2_comm_pb_pb2.pb_cunit, _Mapping]] = ...) -> None: ...

class pbreq_block_chat(_message.Message):
    __slots__ = ("uid",)
    UID_FIELD_NUMBER: _ClassVar[int]
    uid: int
    def __init__(self, uid: _Optional[int] = ...) -> None: ...

class pbrsp_block_chat(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_hide_vip(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class pbrsp_hide_vip(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_translate(_message.Message):
    __slots__ = ("sentence", "target", "encode")
    SENTENCE_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    ENCODE_FIELD_NUMBER: _ClassVar[int]
    sentence: str
    target: str
    encode: int
    def __init__(self, sentence: _Optional[str] = ..., target: _Optional[str] = ..., encode: _Optional[int] = ...) -> None: ...

class pbrsp_translate(_message.Message):
    __slots__ = ("status", "sentence")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    SENTENCE_FIELD_NUMBER: _ClassVar[int]
    status: int
    sentence: str
    def __init__(self, status: _Optional[int] = ..., sentence: _Optional[str] = ...) -> None: ...

class pbreq_chat_setting(_message.Message):
    __slots__ = ("chatblocks",)
    CHATBLOCKS_FIELD_NUMBER: _ClassVar[int]
    chatblocks: int
    def __init__(self, chatblocks: _Optional[int] = ...) -> None: ...

class pbrsp_chat_setting(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_resolve_block_chat(_message.Message):
    __slots__ = ("uid",)
    UID_FIELD_NUMBER: _ClassVar[int]
    uid: int
    def __init__(self, uid: _Optional[int] = ...) -> None: ...

class pbrsp_resolve_block_chat(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_get_block_chat(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class pbrsp_get_block_chat(_message.Message):
    __slots__ = ("status", "frds")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    FRDS_FIELD_NUMBER: _ClassVar[int]
    status: int
    frds: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_frd]
    def __init__(self, status: _Optional[int] = ..., frds: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_frd, _Mapping]]] = ...) -> None: ...

class pbreq_sync_recruit(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class pbrsp_sync_recruit(_message.Message):
    __slots__ = ("msgs",)
    MSGS_FIELD_NUMBER: _ClassVar[int]
    msgs: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_chat]
    def __init__(self, msgs: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_chat, _Mapping]]] = ...) -> None: ...

class pbreq_report(_message.Message):
    __slots__ = ("uid", "type", "content")
    UID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    uid: int
    type: int
    content: str
    def __init__(self, uid: _Optional[int] = ..., type: _Optional[int] = ..., content: _Optional[str] = ...) -> None: ...

class pbrsp_report(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_bmarket_pull(_message.Message):
    __slots__ = ("type",)
    TYPE_FIELD_NUMBER: _ClassVar[int]
    type: int
    def __init__(self, type: _Optional[int] = ...) -> None: ...

class pbrsp_bmarket_pull(_message.Message):
    __slots__ = ("status", "cd", "buy", "good")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    CD_FIELD_NUMBER: _ClassVar[int]
    BUY_FIELD_NUMBER: _ClassVar[int]
    GOOD_FIELD_NUMBER: _ClassVar[int]
    status: int
    cd: int
    buy: _containers.RepeatedScalarFieldContainer[int]
    good: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_good]
    def __init__(self, status: _Optional[int] = ..., cd: _Optional[int] = ..., buy: _Optional[_Iterable[int]] = ..., good: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_good, _Mapping]]] = ...) -> None: ...

class pbreq_bmarket_buy(_message.Message):
    __slots__ = ("index",)
    INDEX_FIELD_NUMBER: _ClassVar[int]
    index: int
    def __init__(self, index: _Optional[int] = ...) -> None: ...

class pbrsp_bmarket_buy(_message.Message):
    __slots__ = ("status", "bag")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    BAG_FIELD_NUMBER: _ClassVar[int]
    status: int
    bag: _dr2_comm_pb_pb2.pb_bag
    def __init__(self, status: _Optional[int] = ..., bag: _Optional[_Union[_dr2_comm_pb_pb2.pb_bag, _Mapping]] = ...) -> None: ...

class pbreq_hook_init(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class pbrsp_hook_init(_message.Message):
    __slots__ = ("hook",)
    HOOK_FIELD_NUMBER: _ClassVar[int]
    hook: _dr2_comm_pb_pb2.pb_hook
    def __init__(self, hook: _Optional[_Union[_dr2_comm_pb_pb2.pb_hook, _Mapping]] = ...) -> None: ...

class pbreq_hook_change(_message.Message):
    __slots__ = ("stage",)
    STAGE_FIELD_NUMBER: _ClassVar[int]
    stage: int
    def __init__(self, stage: _Optional[int] = ...) -> None: ...

class pbrsp_hook_change(_message.Message):
    __slots__ = ("status", "reward", "boss_cd")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    REWARD_FIELD_NUMBER: _ClassVar[int]
    BOSS_CD_FIELD_NUMBER: _ClassVar[int]
    status: int
    reward: _dr2_comm_pb_pb2.pb_bag
    boss_cd: int
    def __init__(self, status: _Optional[int] = ..., reward: _Optional[_Union[_dr2_comm_pb_pb2.pb_bag, _Mapping]] = ..., boss_cd: _Optional[int] = ...) -> None: ...

class pbreq_hook_ask(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class pbrsp_hook_ask(_message.Message):
    __slots__ = ("status", "reward")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    REWARD_FIELD_NUMBER: _ClassVar[int]
    status: int
    reward: _dr2_comm_pb_pb2.pb_bag
    def __init__(self, status: _Optional[int] = ..., reward: _Optional[_Union[_dr2_comm_pb_pb2.pb_bag, _Mapping]] = ...) -> None: ...

class pbreq_hook_reward(_message.Message):
    __slots__ = ("type",)
    TYPE_FIELD_NUMBER: _ClassVar[int]
    type: int
    def __init__(self, type: _Optional[int] = ...) -> None: ...

class pbrsp_hook_reward(_message.Message):
    __slots__ = ("status", "reward")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    REWARD_FIELD_NUMBER: _ClassVar[int]
    status: int
    reward: _dr2_comm_pb_pb2.pb_bag
    def __init__(self, status: _Optional[int] = ..., reward: _Optional[_Union[_dr2_comm_pb_pb2.pb_bag, _Mapping]] = ...) -> None: ...

class pbreq_test_fight(_message.Message):
    __slots__ = ("camp",)
    CAMP_FIELD_NUMBER: _ClassVar[int]
    camp: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_unit]
    def __init__(self, camp: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_unit, _Mapping]]] = ...) -> None: ...

class pbrsp_test_fight(_message.Message):
    __slots__ = ("frames", "win")
    FRAMES_FIELD_NUMBER: _ClassVar[int]
    WIN_FIELD_NUMBER: _ClassVar[int]
    frames: _containers.RepeatedScalarFieldContainer[bytes]
    win: bool
    def __init__(self, frames: _Optional[_Iterable[bytes]] = ..., win: _Optional[bool] = ...) -> None: ...

class pbreq_pve(_message.Message):
    __slots__ = ("camp", "tid", "auto")
    CAMP_FIELD_NUMBER: _ClassVar[int]
    TID_FIELD_NUMBER: _ClassVar[int]
    AUTO_FIELD_NUMBER: _ClassVar[int]
    camp: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_unit]
    tid: int
    auto: int
    def __init__(self, camp: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_unit, _Mapping]]] = ..., tid: _Optional[int] = ..., auto: _Optional[int] = ...) -> None: ...

class pbrsp_pve(_message.Message):
    __slots__ = ("status", "video")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    VIDEO_FIELD_NUMBER: _ClassVar[int]
    status: int
    video: _dr2_comm_pb_pb2.pb_evideo
    def __init__(self, status: _Optional[int] = ..., video: _Optional[_Union[_dr2_comm_pb_pb2.pb_evideo, _Mapping]] = ...) -> None: ...

class pbreq_st_pve(_message.Message):
    __slots__ = ("camp", "auto")
    CAMP_FIELD_NUMBER: _ClassVar[int]
    AUTO_FIELD_NUMBER: _ClassVar[int]
    camp: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_unit]
    auto: int
    def __init__(self, camp: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_unit, _Mapping]]] = ..., auto: _Optional[int] = ...) -> None: ...

class pbrsp_st_pve(_message.Message):
    __slots__ = ("status", "video")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    VIDEO_FIELD_NUMBER: _ClassVar[int]
    status: int
    video: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_evideo]
    def __init__(self, status: _Optional[int] = ..., video: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_evideo, _Mapping]]] = ...) -> None: ...

class pbreq_hook_select_item(_message.Message):
    __slots__ = ("ids",)
    IDS_FIELD_NUMBER: _ClassVar[int]
    ids: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_item]
    def __init__(self, ids: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_item, _Mapping]]] = ...) -> None: ...

class pbrsp_hook_select_item(_message.Message):
    __slots__ = ("status", "reward")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    REWARD_FIELD_NUMBER: _ClassVar[int]
    status: int
    reward: _dr2_comm_pb_pb2.pb_bag
    def __init__(self, status: _Optional[int] = ..., reward: _Optional[_Union[_dr2_comm_pb_pb2.pb_bag, _Mapping]] = ...) -> None: ...

class pbreq_sync_brave(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class pbrsp_sync_brave(_message.Message):
    __slots__ = ("status", "id", "stage", "team", "cd", "enemy", "nodes", "boxes", "buffs", "energy", "times", "spe", "enemy_buffs", "day_times", "night_times", "sweep_stage")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    STAGE_FIELD_NUMBER: _ClassVar[int]
    TEAM_FIELD_NUMBER: _ClassVar[int]
    CD_FIELD_NUMBER: _ClassVar[int]
    ENEMY_FIELD_NUMBER: _ClassVar[int]
    NODES_FIELD_NUMBER: _ClassVar[int]
    BOXES_FIELD_NUMBER: _ClassVar[int]
    BUFFS_FIELD_NUMBER: _ClassVar[int]
    ENERGY_FIELD_NUMBER: _ClassVar[int]
    TIMES_FIELD_NUMBER: _ClassVar[int]
    SPE_FIELD_NUMBER: _ClassVar[int]
    ENEMY_BUFFS_FIELD_NUMBER: _ClassVar[int]
    DAY_TIMES_FIELD_NUMBER: _ClassVar[int]
    NIGHT_TIMES_FIELD_NUMBER: _ClassVar[int]
    SWEEP_STAGE_FIELD_NUMBER: _ClassVar[int]
    status: int
    id: int
    stage: int
    team: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_bunit]
    cd: int
    enemy: _dr2_comm_pb_pb2.pb_benemy
    nodes: _containers.RepeatedScalarFieldContainer[int]
    boxes: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_brave_box]
    buffs: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_brave_buff]
    energy: int
    times: _containers.RepeatedScalarFieldContainer[int]
    spe: int
    enemy_buffs: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_brave_buff]
    day_times: int
    night_times: int
    sweep_stage: int
    def __init__(self, status: _Optional[int] = ..., id: _Optional[int] = ..., stage: _Optional[int] = ..., team: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_bunit, _Mapping]]] = ..., cd: _Optional[int] = ..., enemy: _Optional[_Union[_dr2_comm_pb_pb2.pb_benemy, _Mapping]] = ..., nodes: _Optional[_Iterable[int]] = ..., boxes: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_brave_box, _Mapping]]] = ..., buffs: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_brave_buff, _Mapping]]] = ..., energy: _Optional[int] = ..., times: _Optional[_Iterable[int]] = ..., spe: _Optional[int] = ..., enemy_buffs: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_brave_buff, _Mapping]]] = ..., day_times: _Optional[int] = ..., night_times: _Optional[int] = ..., sweep_stage: _Optional[int] = ...) -> None: ...

class pbreq_brave_fight(_message.Message):
    __slots__ = ("camp",)
    CAMP_FIELD_NUMBER: _ClassVar[int]
    camp: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_unit]
    def __init__(self, camp: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_unit, _Mapping]]] = ...) -> None: ...

class pbrsp_brave_fight(_message.Message):
    __slots__ = ("status", "stage", "win", "frames", "hurts", "enemy", "mhpp", "ehpp", "rewards", "select", "boxes", "spe", "enemy_buffs")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    STAGE_FIELD_NUMBER: _ClassVar[int]
    WIN_FIELD_NUMBER: _ClassVar[int]
    FRAMES_FIELD_NUMBER: _ClassVar[int]
    HURTS_FIELD_NUMBER: _ClassVar[int]
    ENEMY_FIELD_NUMBER: _ClassVar[int]
    MHPP_FIELD_NUMBER: _ClassVar[int]
    EHPP_FIELD_NUMBER: _ClassVar[int]
    REWARDS_FIELD_NUMBER: _ClassVar[int]
    SELECT_FIELD_NUMBER: _ClassVar[int]
    BOXES_FIELD_NUMBER: _ClassVar[int]
    SPE_FIELD_NUMBER: _ClassVar[int]
    ENEMY_BUFFS_FIELD_NUMBER: _ClassVar[int]
    status: int
    stage: int
    win: bool
    frames: _containers.RepeatedScalarFieldContainer[bytes]
    hurts: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_hurts]
    enemy: _dr2_comm_pb_pb2.pb_benemy
    mhpp: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_bunit]
    ehpp: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_bunit]
    rewards: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_bag]
    select: int
    boxes: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_brave_box]
    spe: int
    enemy_buffs: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_brave_buff]
    def __init__(self, status: _Optional[int] = ..., stage: _Optional[int] = ..., win: _Optional[bool] = ..., frames: _Optional[_Iterable[bytes]] = ..., hurts: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_hurts, _Mapping]]] = ..., enemy: _Optional[_Union[_dr2_comm_pb_pb2.pb_benemy, _Mapping]] = ..., mhpp: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_bunit, _Mapping]]] = ..., ehpp: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_bunit, _Mapping]]] = ..., rewards: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_bag, _Mapping]]] = ..., select: _Optional[int] = ..., boxes: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_brave_box, _Mapping]]] = ..., spe: _Optional[int] = ..., enemy_buffs: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_brave_buff, _Mapping]]] = ...) -> None: ...

class pbreq_brave_pull(_message.Message):
    __slots__ = ("stage",)
    STAGE_FIELD_NUMBER: _ClassVar[int]
    stage: int
    def __init__(self, stage: _Optional[int] = ...) -> None: ...

class pbrsp_brave_pull(_message.Message):
    __slots__ = ("enemy", "spe", "enemy_buffs")
    ENEMY_FIELD_NUMBER: _ClassVar[int]
    SPE_FIELD_NUMBER: _ClassVar[int]
    ENEMY_BUFFS_FIELD_NUMBER: _ClassVar[int]
    enemy: _dr2_comm_pb_pb2.pb_benemy
    spe: int
    enemy_buffs: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_brave_buff]
    def __init__(self, enemy: _Optional[_Union[_dr2_comm_pb_pb2.pb_benemy, _Mapping]] = ..., spe: _Optional[int] = ..., enemy_buffs: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_brave_buff, _Mapping]]] = ...) -> None: ...

class pbreq_brave_node(_message.Message):
    __slots__ = ("stage",)
    STAGE_FIELD_NUMBER: _ClassVar[int]
    stage: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, stage: _Optional[_Iterable[int]] = ...) -> None: ...

class pbrsp_brave_node(_message.Message):
    __slots__ = ("status", "reward")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    REWARD_FIELD_NUMBER: _ClassVar[int]
    status: int
    reward: _dr2_comm_pb_pb2.pb_bag
    def __init__(self, status: _Optional[int] = ..., reward: _Optional[_Union[_dr2_comm_pb_pb2.pb_bag, _Mapping]] = ...) -> None: ...

class pbreq_iboss_sync1(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class pbrsp_iboss_sync1(_message.Message):
    __slots__ = ("status", "bossids", "nodes")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    BOSSIDS_FIELD_NUMBER: _ClassVar[int]
    NODES_FIELD_NUMBER: _ClassVar[int]
    status: int
    bossids: _containers.RepeatedScalarFieldContainer[int]
    nodes: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_iboss]
    def __init__(self, status: _Optional[int] = ..., bossids: _Optional[_Iterable[int]] = ..., nodes: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_iboss, _Mapping]]] = ...) -> None: ...

class pbreq_iboss_sync2(_message.Message):
    __slots__ = ("island_id",)
    ISLAND_ID_FIELD_NUMBER: _ClassVar[int]
    island_id: int
    def __init__(self, island_id: _Optional[int] = ...) -> None: ...

class pbrsp_iboss_sync2(_message.Message):
    __slots__ = ("status", "nodes", "count")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    NODES_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    status: int
    nodes: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_iboss]
    count: int
    def __init__(self, status: _Optional[int] = ..., nodes: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_iboss, _Mapping]]] = ..., count: _Optional[int] = ...) -> None: ...

class pbreq_iboss_rank(_message.Message):
    __slots__ = ("island_id",)
    ISLAND_ID_FIELD_NUMBER: _ClassVar[int]
    island_id: int
    def __init__(self, island_id: _Optional[int] = ...) -> None: ...

class pbrsp_iboss_rank(_message.Message):
    __slots__ = ("status", "ranklist", "rank", "score", "rank_cd")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    RANKLIST_FIELD_NUMBER: _ClassVar[int]
    RANK_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    RANK_CD_FIELD_NUMBER: _ClassVar[int]
    status: int
    ranklist: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_iboss_rank]
    rank: int
    score: int
    rank_cd: int
    def __init__(self, status: _Optional[int] = ..., ranklist: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_iboss_rank, _Mapping]]] = ..., rank: _Optional[int] = ..., score: _Optional[int] = ..., rank_cd: _Optional[int] = ...) -> None: ...

class pbreq_iboss_start(_message.Message):
    __slots__ = ("bossid",)
    BOSSID_FIELD_NUMBER: _ClassVar[int]
    bossid: int
    def __init__(self, bossid: _Optional[int] = ...) -> None: ...

class pbrsp_iboss_start(_message.Message):
    __slots__ = ("status", "cd")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    CD_FIELD_NUMBER: _ClassVar[int]
    status: int
    cd: int
    def __init__(self, status: _Optional[int] = ..., cd: _Optional[int] = ...) -> None: ...

class pbreq_iboss_fight(_message.Message):
    __slots__ = ("bossid", "camp")
    BOSSID_FIELD_NUMBER: _ClassVar[int]
    CAMP_FIELD_NUMBER: _ClassVar[int]
    bossid: int
    camp: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_unit]
    def __init__(self, bossid: _Optional[int] = ..., camp: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_unit, _Mapping]]] = ...) -> None: ...

class pbrsp_iboss_fight(_message.Message):
    __slots__ = ("status", "video", "hp", "hpps", "score", "full")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    VIDEO_FIELD_NUMBER: _ClassVar[int]
    HP_FIELD_NUMBER: _ClassVar[int]
    HPPS_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    FULL_FIELD_NUMBER: _ClassVar[int]
    status: int
    video: _dr2_comm_pb_pb2.pb_evideo
    hp: int
    hpps: _containers.RepeatedScalarFieldContainer[int]
    score: int
    full: bool
    def __init__(self, status: _Optional[int] = ..., video: _Optional[_Union[_dr2_comm_pb_pb2.pb_evideo, _Mapping]] = ..., hp: _Optional[int] = ..., hpps: _Optional[_Iterable[int]] = ..., score: _Optional[int] = ..., full: _Optional[bool] = ...) -> None: ...

class pbreq_iboss_settle(_message.Message):
    __slots__ = ("bossid",)
    BOSSID_FIELD_NUMBER: _ClassVar[int]
    bossid: int
    def __init__(self, bossid: _Optional[int] = ...) -> None: ...

class pbrsp_iboss_settle(_message.Message):
    __slots__ = ("status", "score")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    status: int
    score: int
    def __init__(self, status: _Optional[int] = ..., score: _Optional[int] = ...) -> None: ...

class pbreq_gt_sync1(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class pbrsp_gt_sync1(_message.Message):
    __slots__ = ("status", "id", "type")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    status: int
    id: int
    type: int
    def __init__(self, status: _Optional[int] = ..., id: _Optional[int] = ..., type: _Optional[int] = ...) -> None: ...

class pbreq_gt_sync2(_message.Message):
    __slots__ = ("lv", "refresh")
    LV_FIELD_NUMBER: _ClassVar[int]
    REFRESH_FIELD_NUMBER: _ClassVar[int]
    lv: int
    refresh: bool
    def __init__(self, lv: _Optional[int] = ..., refresh: _Optional[bool] = ...) -> None: ...

class pbrsp_gt_sync2(_message.Message):
    __slots__ = ("status", "lv", "gt_nodes", "prog", "vit", "buy")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    LV_FIELD_NUMBER: _ClassVar[int]
    GT_NODES_FIELD_NUMBER: _ClassVar[int]
    PROG_FIELD_NUMBER: _ClassVar[int]
    VIT_FIELD_NUMBER: _ClassVar[int]
    BUY_FIELD_NUMBER: _ClassVar[int]
    status: int
    lv: int
    gt_nodes: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_gt_node]
    prog: int
    vit: int
    buy: int
    def __init__(self, status: _Optional[int] = ..., lv: _Optional[int] = ..., gt_nodes: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_gt_node, _Mapping]]] = ..., prog: _Optional[int] = ..., vit: _Optional[int] = ..., buy: _Optional[int] = ...) -> None: ...

class pbreq_gt_node(_message.Message):
    __slots__ = ("udk",)
    UDK_FIELD_NUMBER: _ClassVar[int]
    udk: str
    def __init__(self, udk: _Optional[str] = ...) -> None: ...

class pbrsp_gt_node(_message.Message):
    __slots__ = ("status", "pbcamp", "msgid")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    PBCAMP_FIELD_NUMBER: _ClassVar[int]
    MSGID_FIELD_NUMBER: _ClassVar[int]
    status: int
    pbcamp: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_unit]
    msgid: int
    def __init__(self, status: _Optional[int] = ..., pbcamp: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_unit, _Mapping]]] = ..., msgid: _Optional[int] = ...) -> None: ...

class pbreq_gt_fight(_message.Message):
    __slots__ = ("udk", "msgid", "teamid", "pitid", "pbcamp", "tid")
    UDK_FIELD_NUMBER: _ClassVar[int]
    MSGID_FIELD_NUMBER: _ClassVar[int]
    TEAMID_FIELD_NUMBER: _ClassVar[int]
    PITID_FIELD_NUMBER: _ClassVar[int]
    PBCAMP_FIELD_NUMBER: _ClassVar[int]
    TID_FIELD_NUMBER: _ClassVar[int]
    udk: str
    msgid: int
    teamid: int
    pitid: int
    pbcamp: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_unit]
    tid: int
    def __init__(self, udk: _Optional[str] = ..., msgid: _Optional[int] = ..., teamid: _Optional[int] = ..., pitid: _Optional[int] = ..., pbcamp: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_unit, _Mapping]]] = ..., tid: _Optional[int] = ...) -> None: ...

class pbrsp_gt_fight(_message.Message):
    __slots__ = ("status", "video")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    VIDEO_FIELD_NUMBER: _ClassVar[int]
    status: int
    video: _dr2_comm_pb_pb2.pb_gvideo
    def __init__(self, status: _Optional[int] = ..., video: _Optional[_Union[_dr2_comm_pb_pb2.pb_gvideo, _Mapping]] = ...) -> None: ...

class pbreq_gt_logs(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class pbrsp_gt_logs(_message.Message):
    __slots__ = ("status", "logs")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    LOGS_FIELD_NUMBER: _ClassVar[int]
    status: int
    logs: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_gt_log]
    def __init__(self, status: _Optional[int] = ..., logs: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_gt_log, _Mapping]]] = ...) -> None: ...

class pbreq_gt_video(_message.Message):
    __slots__ = ("videoid",)
    VIDEOID_FIELD_NUMBER: _ClassVar[int]
    videoid: int
    def __init__(self, videoid: _Optional[int] = ...) -> None: ...

class pbrsp_gt_video(_message.Message):
    __slots__ = ("status", "video")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    VIDEO_FIELD_NUMBER: _ClassVar[int]
    status: int
    video: _dr2_comm_pb_pb2.pb_gvideo
    def __init__(self, status: _Optional[int] = ..., video: _Optional[_Union[_dr2_comm_pb_pb2.pb_gvideo, _Mapping]] = ...) -> None: ...

class pbreq_gt_ask(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class pbrsp_gt_ask(_message.Message):
    __slots__ = ("status", "reward", "lv", "secs", "mapid")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    REWARD_FIELD_NUMBER: _ClassVar[int]
    LV_FIELD_NUMBER: _ClassVar[int]
    SECS_FIELD_NUMBER: _ClassVar[int]
    MAPID_FIELD_NUMBER: _ClassVar[int]
    status: int
    reward: _dr2_comm_pb_pb2.pb_bag
    lv: int
    secs: int
    mapid: int
    def __init__(self, status: _Optional[int] = ..., reward: _Optional[_Union[_dr2_comm_pb_pb2.pb_bag, _Mapping]] = ..., lv: _Optional[int] = ..., secs: _Optional[int] = ..., mapid: _Optional[int] = ...) -> None: ...

class pbreq_gt_reward(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class pbrsp_gt_reward(_message.Message):
    __slots__ = ("status", "reward", "finish")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    REWARD_FIELD_NUMBER: _ClassVar[int]
    FINISH_FIELD_NUMBER: _ClassVar[int]
    status: int
    reward: _dr2_comm_pb_pb2.pb_bag
    finish: bool
    def __init__(self, status: _Optional[int] = ..., reward: _Optional[_Union[_dr2_comm_pb_pb2.pb_bag, _Mapping]] = ..., finish: _Optional[bool] = ...) -> None: ...

class pbreq_gt_buy(_message.Message):
    __slots__ = ("buy",)
    BUY_FIELD_NUMBER: _ClassVar[int]
    buy: int
    def __init__(self, buy: _Optional[int] = ...) -> None: ...

class pbrsp_gt_buy(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_brave_open(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class pbrsp_brave_open(_message.Message):
    __slots__ = ("status", "reward")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    REWARD_FIELD_NUMBER: _ClassVar[int]
    status: int
    reward: _dr2_comm_pb_pb2.pb_bag
    def __init__(self, status: _Optional[int] = ..., reward: _Optional[_Union[_dr2_comm_pb_pb2.pb_bag, _Mapping]] = ...) -> None: ...

class pbreq_brave_altar(_message.Message):
    __slots__ = ("type", "hero_id")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    HERO_ID_FIELD_NUMBER: _ClassVar[int]
    type: int
    hero_id: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, type: _Optional[int] = ..., hero_id: _Optional[_Iterable[int]] = ...) -> None: ...

class pbrsp_brave_altar(_message.Message):
    __slots__ = ("status", "buff")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    BUFF_FIELD_NUMBER: _ClassVar[int]
    status: int
    buff: _dr2_comm_pb_pb2.pb_brave_buff
    def __init__(self, status: _Optional[int] = ..., buff: _Optional[_Union[_dr2_comm_pb_pb2.pb_brave_buff, _Mapping]] = ...) -> None: ...

class pbreq_brave_buy(_message.Message):
    __slots__ = ("num",)
    NUM_FIELD_NUMBER: _ClassVar[int]
    num: int
    def __init__(self, num: _Optional[int] = ...) -> None: ...

class pbrsp_brave_buy(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_brave_shop(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class pbrsp_brave_shop(_message.Message):
    __slots__ = ("status", "goods", "cd")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    GOODS_FIELD_NUMBER: _ClassVar[int]
    CD_FIELD_NUMBER: _ClassVar[int]
    status: int
    goods: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_kv]
    cd: int
    def __init__(self, status: _Optional[int] = ..., goods: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_kv, _Mapping]]] = ..., cd: _Optional[int] = ...) -> None: ...

class pbreq_brave_shop_buy(_message.Message):
    __slots__ = ("id", "num")
    ID_FIELD_NUMBER: _ClassVar[int]
    NUM_FIELD_NUMBER: _ClassVar[int]
    id: int
    num: int
    def __init__(self, id: _Optional[int] = ..., num: _Optional[int] = ...) -> None: ...

class pbrsp_brave_shop_buy(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_pve_rank(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class pbrsp_pve_rank(_message.Message):
    __slots__ = ("mbrs", "rank")
    MBRS_FIELD_NUMBER: _ClassVar[int]
    RANK_FIELD_NUMBER: _ClassVar[int]
    mbrs: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_trial]
    rank: int
    def __init__(self, mbrs: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_trial, _Mapping]]] = ..., rank: _Optional[int] = ...) -> None: ...

class pbreq_sealand_sync(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class pbrsp_sealand_sync(_message.Message):
    __slots__ = ("status", "cd", "lose", "challenge_buy", "sweep_buy", "sweep_times", "stages", "free_sweep", "goods")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    CD_FIELD_NUMBER: _ClassVar[int]
    LOSE_FIELD_NUMBER: _ClassVar[int]
    CHALLENGE_BUY_FIELD_NUMBER: _ClassVar[int]
    SWEEP_BUY_FIELD_NUMBER: _ClassVar[int]
    SWEEP_TIMES_FIELD_NUMBER: _ClassVar[int]
    STAGES_FIELD_NUMBER: _ClassVar[int]
    FREE_SWEEP_FIELD_NUMBER: _ClassVar[int]
    GOODS_FIELD_NUMBER: _ClassVar[int]
    status: int
    cd: int
    lose: int
    challenge_buy: int
    sweep_buy: int
    sweep_times: int
    stages: _containers.RepeatedScalarFieldContainer[int]
    free_sweep: int
    goods: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_hmarket]
    def __init__(self, status: _Optional[int] = ..., cd: _Optional[int] = ..., lose: _Optional[int] = ..., challenge_buy: _Optional[int] = ..., sweep_buy: _Optional[int] = ..., sweep_times: _Optional[int] = ..., stages: _Optional[_Iterable[int]] = ..., free_sweep: _Optional[int] = ..., goods: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_hmarket, _Mapping]]] = ...) -> None: ...

class pbreq_sealand_challenge_buy(_message.Message):
    __slots__ = ("num",)
    NUM_FIELD_NUMBER: _ClassVar[int]
    num: int
    def __init__(self, num: _Optional[int] = ...) -> None: ...

class pbrsp_sealand_challenge_buy(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_sealand_fight(_message.Message):
    __slots__ = ("id", "camp")
    ID_FIELD_NUMBER: _ClassVar[int]
    CAMP_FIELD_NUMBER: _ClassVar[int]
    id: int
    camp: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_unit]
    def __init__(self, id: _Optional[int] = ..., camp: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_unit, _Mapping]]] = ...) -> None: ...

class pbrsp_sealand_fight(_message.Message):
    __slots__ = ("status", "stage", "win", "frames", "hurts")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    STAGE_FIELD_NUMBER: _ClassVar[int]
    WIN_FIELD_NUMBER: _ClassVar[int]
    FRAMES_FIELD_NUMBER: _ClassVar[int]
    HURTS_FIELD_NUMBER: _ClassVar[int]
    status: int
    stage: int
    win: bool
    frames: _containers.RepeatedScalarFieldContainer[bytes]
    hurts: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_hurts]
    def __init__(self, status: _Optional[int] = ..., stage: _Optional[int] = ..., win: _Optional[bool] = ..., frames: _Optional[_Iterable[bytes]] = ..., hurts: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_hurts, _Mapping]]] = ...) -> None: ...

class pbreq_sealand_reward(_message.Message):
    __slots__ = ("id", "num")
    ID_FIELD_NUMBER: _ClassVar[int]
    NUM_FIELD_NUMBER: _ClassVar[int]
    id: int
    num: int
    def __init__(self, id: _Optional[int] = ..., num: _Optional[int] = ...) -> None: ...

class pbrsp_sealand_reward(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_sealand_sweep_buy(_message.Message):
    __slots__ = ("num",)
    NUM_FIELD_NUMBER: _ClassVar[int]
    num: int
    def __init__(self, num: _Optional[int] = ...) -> None: ...

class pbrsp_sealand_sweep_buy(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_sealand_market_buy(_message.Message):
    __slots__ = ("id", "num")
    ID_FIELD_NUMBER: _ClassVar[int]
    NUM_FIELD_NUMBER: _ClassVar[int]
    id: int
    num: int
    def __init__(self, id: _Optional[int] = ..., num: _Optional[int] = ...) -> None: ...

class pbrsp_sealand_market_buy(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_brave_sweep(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class pbrsp_brave_sweep(_message.Message):
    __slots__ = ("status", "reward")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    REWARD_FIELD_NUMBER: _ClassVar[int]
    status: int
    reward: _dr2_comm_pb_pb2.pb_bag
    def __init__(self, status: _Optional[int] = ..., reward: _Optional[_Union[_dr2_comm_pb_pb2.pb_bag, _Mapping]] = ...) -> None: ...

class pbreq_st_hard_fight(_message.Message):
    __slots__ = ("camp", "index")
    CAMP_FIELD_NUMBER: _ClassVar[int]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    camp: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_unit]
    index: int
    def __init__(self, camp: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_unit, _Mapping]]] = ..., index: _Optional[int] = ...) -> None: ...

class pbrsp_st_hard_fight(_message.Message):
    __slots__ = ("status", "video")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    VIDEO_FIELD_NUMBER: _ClassVar[int]
    status: int
    video: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_evideo]
    def __init__(self, status: _Optional[int] = ..., video: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_evideo, _Mapping]]] = ...) -> None: ...

class pbreq_st_hard_ranklist(_message.Message):
    __slots__ = ("fortid",)
    FORTID_FIELD_NUMBER: _ClassVar[int]
    fortid: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, fortid: _Optional[_Iterable[int]] = ...) -> None: ...

class pbrsp_st_hard_ranklist(_message.Message):
    __slots__ = ("status", "ranklist")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    RANKLIST_FIELD_NUMBER: _ClassVar[int]
    status: int
    ranklist: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_wmbr]
    def __init__(self, status: _Optional[int] = ..., ranklist: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_wmbr, _Mapping]]] = ...) -> None: ...

class pbreq_st_hard_clean(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class pbrsp_st_hard_clean(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_frd_sync(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class pbrsp_frd_sync(_message.Message):
    __slots__ = ("friends", "love", "cd", "apply", "recmd")
    FRIENDS_FIELD_NUMBER: _ClassVar[int]
    LOVE_FIELD_NUMBER: _ClassVar[int]
    CD_FIELD_NUMBER: _ClassVar[int]
    APPLY_FIELD_NUMBER: _ClassVar[int]
    RECMD_FIELD_NUMBER: _ClassVar[int]
    friends: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_frd]
    love: int
    cd: int
    apply: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_frd]
    recmd: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_frd]
    def __init__(self, friends: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_frd, _Mapping]]] = ..., love: _Optional[int] = ..., cd: _Optional[int] = ..., apply: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_frd, _Mapping]]] = ..., recmd: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_frd, _Mapping]]] = ...) -> None: ...

class pbreq_frd_op(_message.Message):
    __slots__ = ("apply", "rm", "agree", "disagree")
    APPLY_FIELD_NUMBER: _ClassVar[int]
    RM_FIELD_NUMBER: _ClassVar[int]
    AGREE_FIELD_NUMBER: _ClassVar[int]
    DISAGREE_FIELD_NUMBER: _ClassVar[int]
    apply: int
    rm: int
    agree: int
    disagree: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, apply: _Optional[int] = ..., rm: _Optional[int] = ..., agree: _Optional[int] = ..., disagree: _Optional[_Iterable[int]] = ...) -> None: ...

class pbrsp_frd_op(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_frd_love(_message.Message):
    __slots__ = ("send", "recv")
    SEND_FIELD_NUMBER: _ClassVar[int]
    RECV_FIELD_NUMBER: _ClassVar[int]
    send: int
    recv: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, send: _Optional[int] = ..., recv: _Optional[_Iterable[int]] = ...) -> None: ...

class pbrsp_frd_love(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbrsp_frd_notify(_message.Message):
    __slots__ = ("love", "add", "apply")
    LOVE_FIELD_NUMBER: _ClassVar[int]
    DEL_FIELD_NUMBER: _ClassVar[int]
    ADD_FIELD_NUMBER: _ClassVar[int]
    APPLY_FIELD_NUMBER: _ClassVar[int]
    love: int
    add: _dr2_comm_pb_pb2.pb_frd
    apply: _dr2_comm_pb_pb2.pb_frd
    def __init__(self, love: _Optional[int] = ..., add: _Optional[_Union[_dr2_comm_pb_pb2.pb_frd, _Mapping]] = ..., apply: _Optional[_Union[_dr2_comm_pb_pb2.pb_frd, _Mapping]] = ..., **kwargs) -> None: ...

class pbreq_frd_pk(_message.Message):
    __slots__ = ("uid", "camp", "tid")
    UID_FIELD_NUMBER: _ClassVar[int]
    CAMP_FIELD_NUMBER: _ClassVar[int]
    TID_FIELD_NUMBER: _ClassVar[int]
    uid: int
    camp: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_unit]
    tid: int
    def __init__(self, uid: _Optional[int] = ..., camp: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_unit, _Mapping]]] = ..., tid: _Optional[int] = ...) -> None: ...

class pbrsp_frd_pk(_message.Message):
    __slots__ = ("status", "video")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    VIDEO_FIELD_NUMBER: _ClassVar[int]
    status: int
    video: _dr2_comm_pb_pb2.pb_pvideo
    def __init__(self, status: _Optional[int] = ..., video: _Optional[_Union[_dr2_comm_pb_pb2.pb_pvideo, _Mapping]] = ...) -> None: ...

class pbreq_frd_advise(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class pbrsp_frd_advise(_message.Message):
    __slots__ = ("status", "frds")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    FRDS_FIELD_NUMBER: _ClassVar[int]
    status: int
    frds: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_frd]
    def __init__(self, status: _Optional[int] = ..., frds: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_frd, _Mapping]]] = ...) -> None: ...

class pbreq_pull_casino(_message.Message):
    __slots__ = ("type", "up")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    UP_FIELD_NUMBER: _ClassVar[int]
    type: int
    up: bool
    def __init__(self, type: _Optional[int] = ..., up: _Optional[bool] = ...) -> None: ...

class pbrsp_pull_casino(_message.Message):
    __slots__ = ("status", "items", "cd", "msgs", "force_cd")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    CD_FIELD_NUMBER: _ClassVar[int]
    MSGS_FIELD_NUMBER: _ClassVar[int]
    FORCE_CD_FIELD_NUMBER: _ClassVar[int]
    status: int
    items: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_casino_item]
    cd: int
    msgs: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_casino_msg]
    force_cd: int
    def __init__(self, status: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_casino_item, _Mapping]]] = ..., cd: _Optional[int] = ..., msgs: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_casino_msg, _Mapping]]] = ..., force_cd: _Optional[int] = ...) -> None: ...

class pbreq_casino_msg(_message.Message):
    __slots__ = ("count", "up")
    COUNT_FIELD_NUMBER: _ClassVar[int]
    UP_FIELD_NUMBER: _ClassVar[int]
    count: int
    up: bool
    def __init__(self, count: _Optional[int] = ..., up: _Optional[bool] = ...) -> None: ...

class pbrsp_casino_msg(_message.Message):
    __slots__ = ("status", "msgs")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MSGS_FIELD_NUMBER: _ClassVar[int]
    status: int
    msgs: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_casino_msg]
    def __init__(self, status: _Optional[int] = ..., msgs: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_casino_msg, _Mapping]]] = ...) -> None: ...

class pbreq_casino_draw(_message.Message):
    __slots__ = ("type", "up")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    UP_FIELD_NUMBER: _ClassVar[int]
    type: int
    up: bool
    def __init__(self, type: _Optional[int] = ..., up: _Optional[bool] = ...) -> None: ...

class pbrsp_casino_draw(_message.Message):
    __slots__ = ("status", "ids", "bag", "lucky_coin")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    IDS_FIELD_NUMBER: _ClassVar[int]
    BAG_FIELD_NUMBER: _ClassVar[int]
    LUCKY_COIN_FIELD_NUMBER: _ClassVar[int]
    status: int
    ids: _containers.RepeatedScalarFieldContainer[int]
    bag: _dr2_comm_pb_pb2.pb_bag
    lucky_coin: int
    def __init__(self, status: _Optional[int] = ..., ids: _Optional[_Iterable[int]] = ..., bag: _Optional[_Union[_dr2_comm_pb_pb2.pb_bag, _Mapping]] = ..., lucky_coin: _Optional[int] = ...) -> None: ...

class pbreq_casino_buy(_message.Message):
    __slots__ = ("count",)
    COUNT_FIELD_NUMBER: _ClassVar[int]
    count: int
    def __init__(self, count: _Optional[int] = ...) -> None: ...

class pbrsp_casino_buy(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_lmarket_pull(_message.Message):
    __slots__ = ("type",)
    TYPE_FIELD_NUMBER: _ClassVar[int]
    type: int
    def __init__(self, type: _Optional[int] = ...) -> None: ...

class pbrsp_lmarket_pull(_message.Message):
    __slots__ = ("status", "cd", "goods")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    CD_FIELD_NUMBER: _ClassVar[int]
    GOODS_FIELD_NUMBER: _ClassVar[int]
    status: int
    cd: int
    goods: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_good]
    def __init__(self, status: _Optional[int] = ..., cd: _Optional[int] = ..., goods: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_good, _Mapping]]] = ...) -> None: ...

class pbreq_lmarket_buy(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class pbrsp_lmarket_buy(_message.Message):
    __slots__ = ("status", "bag")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    BAG_FIELD_NUMBER: _ClassVar[int]
    status: int
    bag: _dr2_comm_pb_pb2.pb_bag
    def __init__(self, status: _Optional[int] = ..., bag: _Optional[_Union[_dr2_comm_pb_pb2.pb_bag, _Mapping]] = ...) -> None: ...

class pbreq_guild_sync(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class pbrsp_guild_sync(_message.Message):
    __slots__ = ("status", "guild", "members", "sign_cd", "appliers_count", "invite", "free_name", "invite_cd")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    GUILD_FIELD_NUMBER: _ClassVar[int]
    MEMBERS_FIELD_NUMBER: _ClassVar[int]
    SIGN_CD_FIELD_NUMBER: _ClassVar[int]
    APPLIERS_COUNT_FIELD_NUMBER: _ClassVar[int]
    INVITE_FIELD_NUMBER: _ClassVar[int]
    FREE_NAME_FIELD_NUMBER: _ClassVar[int]
    INVITE_CD_FIELD_NUMBER: _ClassVar[int]
    status: int
    guild: _dr2_comm_pb_pb2.pb_guild
    members: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_gmember]
    sign_cd: int
    appliers_count: int
    invite: int
    free_name: bool
    invite_cd: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, status: _Optional[int] = ..., guild: _Optional[_Union[_dr2_comm_pb_pb2.pb_guild, _Mapping]] = ..., members: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_gmember, _Mapping]]] = ..., sign_cd: _Optional[int] = ..., appliers_count: _Optional[int] = ..., invite: _Optional[int] = ..., free_name: _Optional[bool] = ..., invite_cd: _Optional[_Iterable[int]] = ...) -> None: ...

class pbreq_guild_rank(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class pbrsp_guild_rank(_message.Message):
    __slots__ = ("guilds", "self")
    GUILDS_FIELD_NUMBER: _ClassVar[int]
    SELF_FIELD_NUMBER: _ClassVar[int]
    guilds: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_guild]
    self: int
    def __init__(self_, guilds: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_guild, _Mapping]]] = ..., self: _Optional[int] = ...) -> None: ...

class pbreq_glog(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class pbrsp_glog(_message.Message):
    __slots__ = ("logs",)
    LOGS_FIELD_NUMBER: _ClassVar[int]
    logs: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_glog]
    def __init__(self, logs: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_glog, _Mapping]]] = ...) -> None: ...

class pbreq_guild_create(_message.Message):
    __slots__ = ("name", "logo", "notice")
    NAME_FIELD_NUMBER: _ClassVar[int]
    LOGO_FIELD_NUMBER: _ClassVar[int]
    NOTICE_FIELD_NUMBER: _ClassVar[int]
    name: str
    logo: int
    notice: str
    def __init__(self, name: _Optional[str] = ..., logo: _Optional[int] = ..., notice: _Optional[str] = ...) -> None: ...

class pbrsp_guild_create(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_guild_notice(_message.Message):
    __slots__ = ("notice",)
    NOTICE_FIELD_NUMBER: _ClassVar[int]
    notice: str
    def __init__(self, notice: _Optional[str] = ...) -> None: ...

class pbrsp_guild_notice(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_guild_flag(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class pbrsp_guild_flag(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_guild_name(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class pbrsp_guild_name(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_guild_dismiss(_message.Message):
    __slots__ = ("dismiss", "nodismiss")
    DISMISS_FIELD_NUMBER: _ClassVar[int]
    NODISMISS_FIELD_NUMBER: _ClassVar[int]
    dismiss: int
    nodismiss: int
    def __init__(self, dismiss: _Optional[int] = ..., nodismiss: _Optional[int] = ...) -> None: ...

class pbrsp_guild_dismiss(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_guild_apply(_message.Message):
    __slots__ = ("gid",)
    GID_FIELD_NUMBER: _ClassVar[int]
    gid: int
    def __init__(self, gid: _Optional[int] = ...) -> None: ...

class pbrsp_guild_apply(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_guild_leave(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class pbrsp_guild_leave(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_guild_sign(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class pbrsp_guild_sign(_message.Message):
    __slots__ = ("status", "item", "cd")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ITEM_FIELD_NUMBER: _ClassVar[int]
    CD_FIELD_NUMBER: _ClassVar[int]
    status: int
    item: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_item]
    cd: int
    def __init__(self, status: _Optional[int] = ..., item: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_item, _Mapping]]] = ..., cd: _Optional[int] = ...) -> None: ...

class pbreq_guild_recommend(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class pbrsp_guild_recommend(_message.Message):
    __slots__ = ("guilds",)
    GUILDS_FIELD_NUMBER: _ClassVar[int]
    guilds: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_guild]
    def __init__(self, guilds: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_guild, _Mapping]]] = ...) -> None: ...

class pbreq_guild_search(_message.Message):
    __slots__ = ("word",)
    WORD_FIELD_NUMBER: _ClassVar[int]
    word: str
    def __init__(self, word: _Optional[str] = ...) -> None: ...

class pbrsp_guild_search(_message.Message):
    __slots__ = ("guilds",)
    GUILDS_FIELD_NUMBER: _ClassVar[int]
    guilds: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_guild]
    def __init__(self, guilds: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_guild, _Mapping]]] = ...) -> None: ...

class pbreq_guild_appliers(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class pbrsp_guild_appliers(_message.Message):
    __slots__ = ("mems",)
    MEMS_FIELD_NUMBER: _ClassVar[int]
    mems: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_gmember]
    def __init__(self, mems: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_gmember, _Mapping]]] = ...) -> None: ...

class pbreq_gmember_opt(_message.Message):
    __slots__ = ("type", "muid")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    MUID_FIELD_NUMBER: _ClassVar[int]
    type: int
    muid: int
    def __init__(self, type: _Optional[int] = ..., muid: _Optional[int] = ...) -> None: ...

class pbrsp_gmember_opt(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbrsp_guild_notify(_message.Message):
    __slots__ = ("type", "uid")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    type: int
    uid: int
    def __init__(self, type: _Optional[int] = ..., uid: _Optional[int] = ...) -> None: ...

class pbreq_gboss_sync(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class pbrsp_gboss_sync(_message.Message):
    __slots__ = ("id", "cd", "hpp", "fights")
    ID_FIELD_NUMBER: _ClassVar[int]
    CD_FIELD_NUMBER: _ClassVar[int]
    HPP_FIELD_NUMBER: _ClassVar[int]
    FIGHTS_FIELD_NUMBER: _ClassVar[int]
    id: int
    cd: int
    hpp: int
    fights: int
    def __init__(self, id: _Optional[int] = ..., cd: _Optional[int] = ..., hpp: _Optional[int] = ..., fights: _Optional[int] = ...) -> None: ...

class pbreq_gboss_rank(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class pbrsp_gboss_rank(_message.Message):
    __slots__ = ("ranks",)
    RANKS_FIELD_NUMBER: _ClassVar[int]
    ranks: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_gvrank]
    def __init__(self, ranks: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_gvrank, _Mapping]]] = ...) -> None: ...

class pbreq_gboss_fight(_message.Message):
    __slots__ = ("id", "camp", "tid")
    ID_FIELD_NUMBER: _ClassVar[int]
    CAMP_FIELD_NUMBER: _ClassVar[int]
    TID_FIELD_NUMBER: _ClassVar[int]
    id: int
    camp: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_unit]
    tid: int
    def __init__(self, id: _Optional[int] = ..., camp: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_unit, _Mapping]]] = ..., tid: _Optional[int] = ...) -> None: ...

class pbrsp_gboss_fight(_message.Message):
    __slots__ = ("status", "win", "frames", "hurts", "hpps", "exp")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    WIN_FIELD_NUMBER: _ClassVar[int]
    FRAMES_FIELD_NUMBER: _ClassVar[int]
    HURTS_FIELD_NUMBER: _ClassVar[int]
    HPPS_FIELD_NUMBER: _ClassVar[int]
    EXP_FIELD_NUMBER: _ClassVar[int]
    status: int
    win: bool
    frames: _containers.RepeatedScalarFieldContainer[bytes]
    hurts: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_hurts]
    hpps: _containers.RepeatedScalarFieldContainer[int]
    exp: int
    def __init__(self, status: _Optional[int] = ..., win: _Optional[bool] = ..., frames: _Optional[_Iterable[bytes]] = ..., hurts: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_hurts, _Mapping]]] = ..., hpps: _Optional[_Iterable[int]] = ..., exp: _Optional[int] = ...) -> None: ...

class pbreq_gskl_sync(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class pbrsp_gskl_sync(_message.Message):
    __slots__ = ("skls",)
    SKLS_FIELD_NUMBER: _ClassVar[int]
    skls: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_gskl]
    def __init__(self, skls: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_gskl, _Mapping]]] = ...) -> None: ...

class pbreq_gskl_up(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class pbrsp_gskl_up(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_gskl_reset(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class pbrsp_gskl_reset(_message.Message):
    __slots__ = ("status", "reward")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    REWARD_FIELD_NUMBER: _ClassVar[int]
    status: int
    reward: _dr2_comm_pb_pb2.pb_bag
    def __init__(self, status: _Optional[int] = ..., reward: _Optional[_Union[_dr2_comm_pb_pb2.pb_bag, _Mapping]] = ...) -> None: ...

class pbreq_gfire_sync(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class pbrsp_gfire_sync(_message.Message):
    __slots__ = ("status", "id", "num", "count", "cd", "bossid", "rcd", "hurts")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NUM_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    CD_FIELD_NUMBER: _ClassVar[int]
    BOSSID_FIELD_NUMBER: _ClassVar[int]
    RCD_FIELD_NUMBER: _ClassVar[int]
    HURTS_FIELD_NUMBER: _ClassVar[int]
    status: int
    id: int
    num: int
    count: int
    cd: int
    bossid: int
    rcd: int
    hurts: int
    def __init__(self, status: _Optional[int] = ..., id: _Optional[int] = ..., num: _Optional[int] = ..., count: _Optional[int] = ..., cd: _Optional[int] = ..., bossid: _Optional[int] = ..., rcd: _Optional[int] = ..., hurts: _Optional[int] = ...) -> None: ...

class pbreq_gfire_reg(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class pbrsp_gfire_reg(_message.Message):
    __slots__ = ("status", "cd")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    CD_FIELD_NUMBER: _ClassVar[int]
    status: int
    cd: int
    def __init__(self, status: _Optional[int] = ..., cd: _Optional[int] = ...) -> None: ...

class pbreq_gfire_fight(_message.Message):
    __slots__ = ("camp", "tid")
    CAMP_FIELD_NUMBER: _ClassVar[int]
    TID_FIELD_NUMBER: _ClassVar[int]
    camp: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_unit]
    tid: int
    def __init__(self, camp: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_unit, _Mapping]]] = ..., tid: _Optional[int] = ...) -> None: ...

class pbrsp_gfire_fight(_message.Message):
    __slots__ = ("status", "win", "frames", "hurts", "hpps")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    WIN_FIELD_NUMBER: _ClassVar[int]
    FRAMES_FIELD_NUMBER: _ClassVar[int]
    HURTS_FIELD_NUMBER: _ClassVar[int]
    HPPS_FIELD_NUMBER: _ClassVar[int]
    status: int
    win: bool
    frames: _containers.RepeatedScalarFieldContainer[bytes]
    hurts: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_hurts]
    hpps: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, status: _Optional[int] = ..., win: _Optional[bool] = ..., frames: _Optional[_Iterable[bytes]] = ..., hurts: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_hurts, _Mapping]]] = ..., hpps: _Optional[_Iterable[int]] = ...) -> None: ...

class pbreq_gfire_rank(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class pbrsp_gfire_rank(_message.Message):
    __slots__ = ("ranks", "hurts")
    RANKS_FIELD_NUMBER: _ClassVar[int]
    HURTS_FIELD_NUMBER: _ClassVar[int]
    ranks: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_gvrank]
    hurts: int
    def __init__(self, ranks: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_gvrank, _Mapping]]] = ..., hurts: _Optional[int] = ...) -> None: ...

class pbreq_gve_sync(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class pbrsp_gve_sync(_message.Message):
    __slots__ = ("status", "maps_exp", "maps_lv", "boss", "claim", "task", "gold", "cd", "claim2")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MAPS_EXP_FIELD_NUMBER: _ClassVar[int]
    MAPS_LV_FIELD_NUMBER: _ClassVar[int]
    BOSS_FIELD_NUMBER: _ClassVar[int]
    CLAIM_FIELD_NUMBER: _ClassVar[int]
    TASK_FIELD_NUMBER: _ClassVar[int]
    GOLD_FIELD_NUMBER: _ClassVar[int]
    CD_FIELD_NUMBER: _ClassVar[int]
    CLAIM2_FIELD_NUMBER: _ClassVar[int]
    status: int
    maps_exp: _containers.RepeatedScalarFieldContainer[int]
    maps_lv: _containers.RepeatedScalarFieldContainer[int]
    boss: _containers.RepeatedScalarFieldContainer[int]
    claim: _containers.RepeatedScalarFieldContainer[int]
    task: int
    gold: int
    cd: int
    claim2: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, status: _Optional[int] = ..., maps_exp: _Optional[_Iterable[int]] = ..., maps_lv: _Optional[_Iterable[int]] = ..., boss: _Optional[_Iterable[int]] = ..., claim: _Optional[_Iterable[int]] = ..., task: _Optional[int] = ..., gold: _Optional[int] = ..., cd: _Optional[int] = ..., claim2: _Optional[_Iterable[int]] = ...) -> None: ...

class pbreq_gve_rank(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class pbrsp_gve_rank(_message.Message):
    __slots__ = ("status", "rank", "maps_exp")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    RANK_FIELD_NUMBER: _ClassVar[int]
    MAPS_EXP_FIELD_NUMBER: _ClassVar[int]
    status: int
    rank: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_gve_rank]
    maps_exp: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, status: _Optional[int] = ..., rank: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_gve_rank, _Mapping]]] = ..., maps_exp: _Optional[_Iterable[int]] = ...) -> None: ...

class pbreq_gve_fight(_message.Message):
    __slots__ = ("mapid", "hid")
    MAPID_FIELD_NUMBER: _ClassVar[int]
    HID_FIELD_NUMBER: _ClassVar[int]
    mapid: int
    hid: int
    def __init__(self, mapid: _Optional[int] = ..., hid: _Optional[int] = ...) -> None: ...

class pbrsp_gve_fight(_message.Message):
    __slots__ = ("status", "video")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    VIDEO_FIELD_NUMBER: _ClassVar[int]
    status: int
    video: _dr2_comm_pb_pb2.pb_evideo
    def __init__(self, status: _Optional[int] = ..., video: _Optional[_Union[_dr2_comm_pb_pb2.pb_evideo, _Mapping]] = ...) -> None: ...

class pbreq_gve_task(_message.Message):
    __slots__ = ("taskid", "hids")
    TASKID_FIELD_NUMBER: _ClassVar[int]
    HIDS_FIELD_NUMBER: _ClassVar[int]
    taskid: int
    hids: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, taskid: _Optional[int] = ..., hids: _Optional[_Iterable[int]] = ...) -> None: ...

class pbrsp_gve_task(_message.Message):
    __slots__ = ("status", "reward")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    REWARD_FIELD_NUMBER: _ClassVar[int]
    status: int
    reward: _dr2_comm_pb_pb2.pb_bag
    def __init__(self, status: _Optional[int] = ..., reward: _Optional[_Union[_dr2_comm_pb_pb2.pb_bag, _Mapping]] = ...) -> None: ...

class pbreq_gve_claim(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class pbrsp_gve_claim(_message.Message):
    __slots__ = ("status", "reward")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    REWARD_FIELD_NUMBER: _ClassVar[int]
    status: int
    reward: _dr2_comm_pb_pb2.pb_bag
    def __init__(self, status: _Optional[int] = ..., reward: _Optional[_Union[_dr2_comm_pb_pb2.pb_bag, _Mapping]] = ...) -> None: ...

class pbreq_gve_map_claim(_message.Message):
    __slots__ = ("id", "lv")
    ID_FIELD_NUMBER: _ClassVar[int]
    LV_FIELD_NUMBER: _ClassVar[int]
    id: int
    lv: int
    def __init__(self, id: _Optional[int] = ..., lv: _Optional[int] = ...) -> None: ...

class pbrsp_gve_map_claim(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_gvm_sync_world(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class pbrsp_gvm_sync_world(_message.Message):
    __slots__ = ("status", "gud_score", "gud_rank", "cd", "maps_info", "xnum", "bt_cd", "bnum", "tasks", "bag", "unselect", "up_heros", "pass_id", "map_id", "show", "boss_id")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    GUD_SCORE_FIELD_NUMBER: _ClassVar[int]
    GUD_RANK_FIELD_NUMBER: _ClassVar[int]
    CD_FIELD_NUMBER: _ClassVar[int]
    MAPS_INFO_FIELD_NUMBER: _ClassVar[int]
    XNUM_FIELD_NUMBER: _ClassVar[int]
    BT_CD_FIELD_NUMBER: _ClassVar[int]
    BNUM_FIELD_NUMBER: _ClassVar[int]
    TASKS_FIELD_NUMBER: _ClassVar[int]
    BAG_FIELD_NUMBER: _ClassVar[int]
    UNSELECT_FIELD_NUMBER: _ClassVar[int]
    UP_HEROS_FIELD_NUMBER: _ClassVar[int]
    PASS_ID_FIELD_NUMBER: _ClassVar[int]
    MAP_ID_FIELD_NUMBER: _ClassVar[int]
    SHOW_FIELD_NUMBER: _ClassVar[int]
    BOSS_ID_FIELD_NUMBER: _ClassVar[int]
    status: int
    gud_score: int
    gud_rank: int
    cd: int
    maps_info: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_gvm_map]
    xnum: int
    bt_cd: int
    bnum: int
    tasks: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_task]
    bag: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_gvm_stone]
    unselect: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_gvm_stone]
    up_heros: _containers.RepeatedScalarFieldContainer[int]
    pass_id: _containers.RepeatedScalarFieldContainer[int]
    map_id: int
    show: bool
    boss_id: int
    def __init__(self, status: _Optional[int] = ..., gud_score: _Optional[int] = ..., gud_rank: _Optional[int] = ..., cd: _Optional[int] = ..., maps_info: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_gvm_map, _Mapping]]] = ..., xnum: _Optional[int] = ..., bt_cd: _Optional[int] = ..., bnum: _Optional[int] = ..., tasks: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_task, _Mapping]]] = ..., bag: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_gvm_stone, _Mapping]]] = ..., unselect: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_gvm_stone, _Mapping]]] = ..., up_heros: _Optional[_Iterable[int]] = ..., pass_id: _Optional[_Iterable[int]] = ..., map_id: _Optional[int] = ..., show: _Optional[bool] = ..., boss_id: _Optional[int] = ...) -> None: ...

class pbreq_gvm_fight_sync(_message.Message):
    __slots__ = ("mapid",)
    MAPID_FIELD_NUMBER: _ClassVar[int]
    mapid: int
    def __init__(self, mapid: _Optional[int] = ...) -> None: ...

class pbrsp_gvm_fight_sync(_message.Message):
    __slots__ = ("status", "value1", "value2", "mbrs", "buff_num", "boss_id", "per_hp")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    VALUE1_FIELD_NUMBER: _ClassVar[int]
    VALUE2_FIELD_NUMBER: _ClassVar[int]
    MBRS_FIELD_NUMBER: _ClassVar[int]
    BUFF_NUM_FIELD_NUMBER: _ClassVar[int]
    BOSS_ID_FIELD_NUMBER: _ClassVar[int]
    PER_HP_FIELD_NUMBER: _ClassVar[int]
    status: int
    value1: int
    value2: int
    mbrs: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_gvm_mbr]
    buff_num: _containers.RepeatedScalarFieldContainer[int]
    boss_id: int
    per_hp: int
    def __init__(self, status: _Optional[int] = ..., value1: _Optional[int] = ..., value2: _Optional[int] = ..., mbrs: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_gvm_mbr, _Mapping]]] = ..., buff_num: _Optional[_Iterable[int]] = ..., boss_id: _Optional[int] = ..., per_hp: _Optional[int] = ...) -> None: ...

class pbreq_gvm_fight(_message.Message):
    __slots__ = ("id", "boss", "camp", "tid")
    ID_FIELD_NUMBER: _ClassVar[int]
    BOSS_FIELD_NUMBER: _ClassVar[int]
    CAMP_FIELD_NUMBER: _ClassVar[int]
    TID_FIELD_NUMBER: _ClassVar[int]
    id: int
    boss: int
    camp: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_unit]
    tid: int
    def __init__(self, id: _Optional[int] = ..., boss: _Optional[int] = ..., camp: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_unit, _Mapping]]] = ..., tid: _Optional[int] = ...) -> None: ...

class pbrsp_gvm_fight(_message.Message):
    __slots__ = ("status", "video", "stones", "score", "boss_id", "per_hp", "nodes", "hurt_boss", "sweep", "show")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    VIDEO_FIELD_NUMBER: _ClassVar[int]
    STONES_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    BOSS_ID_FIELD_NUMBER: _ClassVar[int]
    PER_HP_FIELD_NUMBER: _ClassVar[int]
    NODES_FIELD_NUMBER: _ClassVar[int]
    HURT_BOSS_FIELD_NUMBER: _ClassVar[int]
    SWEEP_FIELD_NUMBER: _ClassVar[int]
    SHOW_FIELD_NUMBER: _ClassVar[int]
    status: int
    video: _dr2_comm_pb_pb2.pb_evideo
    stones: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_gvm_stone]
    score: str
    boss_id: int
    per_hp: _containers.RepeatedScalarFieldContainer[int]
    nodes: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_gvm_map_node]
    hurt_boss: str
    sweep: bool
    show: bool
    def __init__(self, status: _Optional[int] = ..., video: _Optional[_Union[_dr2_comm_pb_pb2.pb_evideo, _Mapping]] = ..., stones: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_gvm_stone, _Mapping]]] = ..., score: _Optional[str] = ..., boss_id: _Optional[int] = ..., per_hp: _Optional[_Iterable[int]] = ..., nodes: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_gvm_map_node, _Mapping]]] = ..., hurt_boss: _Optional[str] = ..., sweep: _Optional[bool] = ..., show: _Optional[bool] = ...) -> None: ...

class pbreq_gvm_select(_message.Message):
    __slots__ = ("idx",)
    IDX_FIELD_NUMBER: _ClassVar[int]
    idx: int
    def __init__(self, idx: _Optional[int] = ...) -> None: ...

class pbrsp_gvm_select(_message.Message):
    __slots__ = ("status", "bid")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    BID_FIELD_NUMBER: _ClassVar[int]
    status: int
    bid: int
    def __init__(self, status: _Optional[int] = ..., bid: _Optional[int] = ...) -> None: ...

class pbreq_gvm_map_sync(_message.Message):
    __slots__ = ("mapid",)
    MAPID_FIELD_NUMBER: _ClassVar[int]
    mapid: int
    def __init__(self, mapid: _Optional[int] = ...) -> None: ...

class pbrsp_gvm_map_sync(_message.Message):
    __slots__ = ("status", "node", "sweep")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    NODE_FIELD_NUMBER: _ClassVar[int]
    SWEEP_FIELD_NUMBER: _ClassVar[int]
    status: int
    node: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_gvm_map_node]
    sweep: bool
    def __init__(self, status: _Optional[int] = ..., node: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_gvm_map_node, _Mapping]]] = ..., sweep: _Optional[bool] = ...) -> None: ...

class pbreq_gvm_task_claim(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class pbrsp_gvm_task_claim(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_gvm_up_stone(_message.Message):
    __slots__ = ("stone",)
    STONE_FIELD_NUMBER: _ClassVar[int]
    stone: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, stone: _Optional[_Iterable[int]] = ...) -> None: ...

class pbrsp_gvm_up_stone(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_gvm_sell_stone(_message.Message):
    __slots__ = ("stone",)
    STONE_FIELD_NUMBER: _ClassVar[int]
    stone: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, stone: _Optional[_Iterable[int]] = ...) -> None: ...

class pbrsp_gvm_sell_stone(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_gvm_up_hero(_message.Message):
    __slots__ = ("hids",)
    HIDS_FIELD_NUMBER: _ClassVar[int]
    hids: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, hids: _Optional[_Iterable[int]] = ...) -> None: ...

class pbrsp_gvm_up_hero(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_gvm_rank(_message.Message):
    __slots__ = ("type",)
    TYPE_FIELD_NUMBER: _ClassVar[int]
    type: int
    def __init__(self, type: _Optional[int] = ...) -> None: ...

class pbrsp_gvm_rank(_message.Message):
    __slots__ = ("status", "guds", "mbrs", "rank_self", "score_self")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    GUDS_FIELD_NUMBER: _ClassVar[int]
    MBRS_FIELD_NUMBER: _ClassVar[int]
    RANK_SELF_FIELD_NUMBER: _ClassVar[int]
    SCORE_SELF_FIELD_NUMBER: _ClassVar[int]
    status: int
    guds: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_gvm_rank]
    mbrs: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_gvm_mbr]
    rank_self: int
    score_self: int
    def __init__(self, status: _Optional[int] = ..., guds: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_gvm_rank, _Mapping]]] = ..., mbrs: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_gvm_mbr, _Mapping]]] = ..., rank_self: _Optional[int] = ..., score_self: _Optional[int] = ...) -> None: ...

class pbreq_gvm_reset_map(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class pbrsp_gvm_reset_map(_message.Message):
    __slots__ = ("status", "nodes")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    NODES_FIELD_NUMBER: _ClassVar[int]
    status: int
    nodes: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_gvm_map_node]
    def __init__(self, status: _Optional[int] = ..., nodes: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_gvm_map_node, _Mapping]]] = ...) -> None: ...

class pbreq_gvm_sweep(_message.Message):
    __slots__ = ("times", "id")
    TIMES_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    times: int
    id: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, times: _Optional[int] = ..., id: _Optional[_Iterable[int]] = ...) -> None: ...

class pbrsp_gvm_sweep(_message.Message):
    __slots__ = ("status", "stone", "buff", "tasks", "nodes")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    STONE_FIELD_NUMBER: _ClassVar[int]
    BUFF_FIELD_NUMBER: _ClassVar[int]
    TASKS_FIELD_NUMBER: _ClassVar[int]
    NODES_FIELD_NUMBER: _ClassVar[int]
    status: int
    stone: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_gvm_stone]
    buff: int
    tasks: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_task]
    nodes: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_gvm_map_node]
    def __init__(self, status: _Optional[int] = ..., stone: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_gvm_stone, _Mapping]]] = ..., buff: _Optional[int] = ..., tasks: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_task, _Mapping]]] = ..., nodes: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_gvm_map_node, _Mapping]]] = ...) -> None: ...

class pbreq_trial(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class pbrsp_trial(_message.Message):
    __slots__ = ("status", "id", "tl", "cd")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    TL_FIELD_NUMBER: _ClassVar[int]
    CD_FIELD_NUMBER: _ClassVar[int]
    status: int
    id: int
    tl: int
    cd: int
    def __init__(self, status: _Optional[int] = ..., id: _Optional[int] = ..., tl: _Optional[int] = ..., cd: _Optional[int] = ...) -> None: ...

class pbreq_trial_rank(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class pbrsp_trial_rank(_message.Message):
    __slots__ = ("rank",)
    RANK_FIELD_NUMBER: _ClassVar[int]
    rank: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_trial]
    def __init__(self, rank: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_trial, _Mapping]]] = ...) -> None: ...

class pbreq_trial_fight(_message.Message):
    __slots__ = ("camp", "tid")
    CAMP_FIELD_NUMBER: _ClassVar[int]
    TID_FIELD_NUMBER: _ClassVar[int]
    camp: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_unit]
    tid: int
    def __init__(self, camp: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_unit, _Mapping]]] = ..., tid: _Optional[int] = ...) -> None: ...

class pbrsp_trial_fight(_message.Message):
    __slots__ = ("status", "video")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    VIDEO_FIELD_NUMBER: _ClassVar[int]
    status: int
    video: _dr2_comm_pb_pb2.pb_evideo
    def __init__(self, status: _Optional[int] = ..., video: _Optional[_Union[_dr2_comm_pb_pb2.pb_evideo, _Mapping]] = ...) -> None: ...

class pbreq_trial_video(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class pbrsp_trial_video(_message.Message):
    __slots__ = ("status", "videos")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    VIDEOS_FIELD_NUMBER: _ClassVar[int]
    status: int
    videos: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_trial]
    def __init__(self, status: _Optional[int] = ..., videos: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_trial, _Mapping]]] = ...) -> None: ...

class pbreq_trial_tl(_message.Message):
    __slots__ = ("num",)
    NUM_FIELD_NUMBER: _ClassVar[int]
    num: int
    def __init__(self, num: _Optional[int] = ...) -> None: ...

class pbrsp_trial_tl(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_dream_fight(_message.Message):
    __slots__ = ("id", "camp", "tid")
    ID_FIELD_NUMBER: _ClassVar[int]
    CAMP_FIELD_NUMBER: _ClassVar[int]
    TID_FIELD_NUMBER: _ClassVar[int]
    id: int
    camp: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_unit]
    tid: int
    def __init__(self, id: _Optional[int] = ..., camp: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_unit, _Mapping]]] = ..., tid: _Optional[int] = ...) -> None: ...

class pbrsp_dream_fight(_message.Message):
    __slots__ = ("status", "video")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    VIDEO_FIELD_NUMBER: _ClassVar[int]
    status: int
    video: _dr2_comm_pb_pb2.pb_evideo
    def __init__(self, status: _Optional[int] = ..., video: _Optional[_Union[_dr2_comm_pb_pb2.pb_evideo, _Mapping]] = ...) -> None: ...

class pbreq_dream_rank(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class pbrsp_dream_rank(_message.Message):
    __slots__ = ("status", "rank")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    RANK_FIELD_NUMBER: _ClassVar[int]
    status: int
    rank: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_trial]
    def __init__(self, status: _Optional[int] = ..., rank: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_trial, _Mapping]]] = ...) -> None: ...

class pbreq_dream_diff(_message.Message):
    __slots__ = ("diff",)
    DIFF_FIELD_NUMBER: _ClassVar[int]
    diff: int
    def __init__(self, diff: _Optional[int] = ...) -> None: ...

class pbrsp_dream_diff(_message.Message):
    __slots__ = ("status", "monsters", "bufs")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MONSTERS_FIELD_NUMBER: _ClassVar[int]
    BUFS_FIELD_NUMBER: _ClassVar[int]
    status: int
    monsters: _containers.RepeatedScalarFieldContainer[int]
    bufs: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_kv]
    def __init__(self, status: _Optional[int] = ..., monsters: _Optional[_Iterable[int]] = ..., bufs: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_kv, _Mapping]]] = ...) -> None: ...

class pbreq_dream_reward(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class pbrsp_dream_reward(_message.Message):
    __slots__ = ("status", "reward")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    REWARD_FIELD_NUMBER: _ClassVar[int]
    status: int
    reward: _dr2_comm_pb_pb2.pb_bag
    def __init__(self, status: _Optional[int] = ..., reward: _Optional[_Union[_dr2_comm_pb_pb2.pb_bag, _Mapping]] = ...) -> None: ...

class pbreq_dream_buy(_message.Message):
    __slots__ = ("num",)
    NUM_FIELD_NUMBER: _ClassVar[int]
    num: int
    def __init__(self, num: _Optional[int] = ...) -> None: ...

class pbrsp_dream_buy(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_dream_sync(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class pbrsp_dream_sync(_message.Message):
    __slots__ = ("next", "status", "id", "ids", "diff", "reset", "reward", "season", "water", "cd", "monsters", "bufs")
    NEXT_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    IDS_FIELD_NUMBER: _ClassVar[int]
    DIFF_FIELD_NUMBER: _ClassVar[int]
    RESET_FIELD_NUMBER: _ClassVar[int]
    REWARD_FIELD_NUMBER: _ClassVar[int]
    SEASON_FIELD_NUMBER: _ClassVar[int]
    WATER_FIELD_NUMBER: _ClassVar[int]
    CD_FIELD_NUMBER: _ClassVar[int]
    MONSTERS_FIELD_NUMBER: _ClassVar[int]
    BUFS_FIELD_NUMBER: _ClassVar[int]
    next: int
    status: int
    id: int
    ids: _containers.RepeatedScalarFieldContainer[int]
    diff: _containers.RepeatedScalarFieldContainer[int]
    reset: int
    reward: _dr2_comm_pb_pb2.pb_bag
    season: int
    water: int
    cd: int
    monsters: _containers.RepeatedScalarFieldContainer[int]
    bufs: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_kv]
    def __init__(self, next: _Optional[int] = ..., status: _Optional[int] = ..., id: _Optional[int] = ..., ids: _Optional[_Iterable[int]] = ..., diff: _Optional[_Iterable[int]] = ..., reset: _Optional[int] = ..., reward: _Optional[_Union[_dr2_comm_pb_pb2.pb_bag, _Mapping]] = ..., season: _Optional[int] = ..., water: _Optional[int] = ..., cd: _Optional[int] = ..., monsters: _Optional[_Iterable[int]] = ..., bufs: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_kv, _Mapping]]] = ...) -> None: ...

class pbreq_dream_sel_buf(_message.Message):
    __slots__ = ("id", "discard")
    ID_FIELD_NUMBER: _ClassVar[int]
    DISCARD_FIELD_NUMBER: _ClassVar[int]
    id: int
    discard: int
    def __init__(self, id: _Optional[int] = ..., discard: _Optional[int] = ...) -> None: ...

class pbrsp_dream_sel_buf(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_pvp_sync(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class pbrsp_pvp_sync(_message.Message):
    __slots__ = ("infos", "wpvp")
    INFOS_FIELD_NUMBER: _ClassVar[int]
    WPVP_FIELD_NUMBER: _ClassVar[int]
    infos: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_pvp]
    wpvp: _dr2_comm_pb_pb2.pb_wpvp
    def __init__(self, infos: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_pvp, _Mapping]]] = ..., wpvp: _Optional[_Union[_dr2_comm_pb_pb2.pb_wpvp, _Mapping]] = ...) -> None: ...

class pbreq_pvp_camp(_message.Message):
    __slots__ = ("id", "camp")
    ID_FIELD_NUMBER: _ClassVar[int]
    CAMP_FIELD_NUMBER: _ClassVar[int]
    id: int
    camp: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_unit]
    def __init__(self, id: _Optional[int] = ..., camp: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_unit, _Mapping]]] = ...) -> None: ...

class pbrsp_pvp_camp(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_pvp_refresh(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class pbrsp_pvp_refresh(_message.Message):
    __slots__ = ("status", "rivals")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    RIVALS_FIELD_NUMBER: _ClassVar[int]
    status: int
    rivals: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_pmbr]
    def __init__(self, status: _Optional[int] = ..., rivals: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_pmbr, _Mapping]]] = ...) -> None: ...

class pbreq_pvp_fight(_message.Message):
    __slots__ = ("id", "uid", "camp", "svr_id", "tid")
    ID_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    CAMP_FIELD_NUMBER: _ClassVar[int]
    SVR_ID_FIELD_NUMBER: _ClassVar[int]
    TID_FIELD_NUMBER: _ClassVar[int]
    id: int
    uid: int
    camp: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_unit]
    svr_id: int
    tid: int
    def __init__(self, id: _Optional[int] = ..., uid: _Optional[int] = ..., camp: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_unit, _Mapping]]] = ..., svr_id: _Optional[int] = ..., tid: _Optional[int] = ...) -> None: ...

class pbrsp_pvp_fight(_message.Message):
    __slots__ = ("status", "video", "videos", "cd")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    VIDEO_FIELD_NUMBER: _ClassVar[int]
    VIDEOS_FIELD_NUMBER: _ClassVar[int]
    CD_FIELD_NUMBER: _ClassVar[int]
    status: int
    video: _dr2_comm_pb_pb2.pb_pvideo
    videos: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_pvideo]
    cd: int
    def __init__(self, status: _Optional[int] = ..., video: _Optional[_Union[_dr2_comm_pb_pb2.pb_pvideo, _Mapping]] = ..., videos: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_pvideo, _Mapping]]] = ..., cd: _Optional[int] = ...) -> None: ...

class pbreq_plogs(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class pbrsp_plogs(_message.Message):
    __slots__ = ("status", "logs")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    LOGS_FIELD_NUMBER: _ClassVar[int]
    status: int
    logs: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_plog]
    def __init__(self, status: _Optional[int] = ..., logs: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_plog, _Mapping]]] = ...) -> None: ...

class pbreq_pvp_rank(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class pbrsp_pvp_rank(_message.Message):
    __slots__ = ("status", "members")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MEMBERS_FIELD_NUMBER: _ClassVar[int]
    status: int
    members: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_pmbr]
    def __init__(self, status: _Optional[int] = ..., members: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_pmbr, _Mapping]]] = ...) -> None: ...

class pbreq_video(_message.Message):
    __slots__ = ("id", "vid")
    ID_FIELD_NUMBER: _ClassVar[int]
    VID_FIELD_NUMBER: _ClassVar[int]
    id: int
    vid: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, id: _Optional[int] = ..., vid: _Optional[_Iterable[int]] = ...) -> None: ...

class pbrsp_video(_message.Message):
    __slots__ = ("status", "video")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    VIDEO_FIELD_NUMBER: _ClassVar[int]
    status: int
    video: _dr2_comm_pb_pb2.pb_pvideo
    def __init__(self, status: _Optional[int] = ..., video: _Optional[_Union[_dr2_comm_pb_pb2.pb_pvideo, _Mapping]] = ...) -> None: ...

class pbreq_pvp_ticket(_message.Message):
    __slots__ = ("num",)
    NUM_FIELD_NUMBER: _ClassVar[int]
    num: int
    def __init__(self, num: _Optional[int] = ...) -> None: ...

class pbrsp_pvp_ticket(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_pmarket(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class pbrsp_pmarket(_message.Message):
    __slots__ = ("status", "item")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ITEM_FIELD_NUMBER: _ClassVar[int]
    status: int
    item: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_hmarket]
    def __init__(self, status: _Optional[int] = ..., item: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_hmarket, _Mapping]]] = ...) -> None: ...

class pbreq_pmarket_buy(_message.Message):
    __slots__ = ("id", "num")
    ID_FIELD_NUMBER: _ClassVar[int]
    NUM_FIELD_NUMBER: _ClassVar[int]
    id: int
    num: int
    def __init__(self, id: _Optional[int] = ..., num: _Optional[int] = ...) -> None: ...

class pbrsp_pmarket_buy(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_joinpvp_sync(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class pbrsp_joinpvp_sync(_message.Message):
    __slots__ = ("status", "self")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    SELF_FIELD_NUMBER: _ClassVar[int]
    status: int
    self: _dr2_comm_pb_pb2.pb_pmbr
    def __init__(self_, status: _Optional[int] = ..., self: _Optional[_Union[_dr2_comm_pb_pb2.pb_pmbr, _Mapping]] = ...) -> None: ...

class pbreq_p3p_sync(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class pbrsp_p3p_sync(_message.Message):
    __slots__ = ("status", "self", "members", "wid")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    SELF_FIELD_NUMBER: _ClassVar[int]
    MEMBERS_FIELD_NUMBER: _ClassVar[int]
    WID_FIELD_NUMBER: _ClassVar[int]
    status: int
    self: _dr2_comm_pb_pb2.pb_p3pmbr
    members: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_p3pmbr]
    wid: int
    def __init__(self_, status: _Optional[int] = ..., self: _Optional[_Union[_dr2_comm_pb_pb2.pb_p3pmbr, _Mapping]] = ..., members: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_p3pmbr, _Mapping]]] = ..., wid: _Optional[int] = ...) -> None: ...

class pbreq_p3p_camp(_message.Message):
    __slots__ = ("camp",)
    CAMP_FIELD_NUMBER: _ClassVar[int]
    camp: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_unit]
    def __init__(self, camp: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_unit, _Mapping]]] = ...) -> None: ...

class pbrsp_p3p_camp(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_p3p_match(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class pbrsp_p3p_match(_message.Message):
    __slots__ = ("status", "def1", "def2", "def3")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    DEF1_FIELD_NUMBER: _ClassVar[int]
    DEF2_FIELD_NUMBER: _ClassVar[int]
    DEF3_FIELD_NUMBER: _ClassVar[int]
    status: int
    def1: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_p3pmbr]
    def2: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_p3pmbr]
    def3: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_p3pmbr]
    def __init__(self, status: _Optional[int] = ..., def1: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_p3pmbr, _Mapping]]] = ..., def2: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_p3pmbr, _Mapping]]] = ..., def3: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_p3pmbr, _Mapping]]] = ...) -> None: ...

class pbreq_p3p_fight(_message.Message):
    __slots__ = ("uid", "camp")
    UID_FIELD_NUMBER: _ClassVar[int]
    CAMP_FIELD_NUMBER: _ClassVar[int]
    uid: int
    camp: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_unit]
    def __init__(self, uid: _Optional[int] = ..., camp: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_unit, _Mapping]]] = ...) -> None: ...

class pbrsp_p3p_fight(_message.Message):
    __slots__ = ("status", "video")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    VIDEO_FIELD_NUMBER: _ClassVar[int]
    status: int
    video: _dr2_comm_pb_pb2.pb_p3pvideo
    def __init__(self, status: _Optional[int] = ..., video: _Optional[_Union[_dr2_comm_pb_pb2.pb_p3pvideo, _Mapping]] = ...) -> None: ...

class pbreq_p3p_honor(_message.Message):
    __slots__ = ("wid",)
    WID_FIELD_NUMBER: _ClassVar[int]
    wid: int
    def __init__(self, wid: _Optional[int] = ...) -> None: ...

class pbrsp_p3p_honor(_message.Message):
    __slots__ = ("status", "mbrs")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MBRS_FIELD_NUMBER: _ClassVar[int]
    status: int
    mbrs: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_p3pmbr]
    def __init__(self, status: _Optional[int] = ..., mbrs: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_p3pmbr, _Mapping]]] = ...) -> None: ...

class pbreq_p3p_logs(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class pbrsp_p3p_logs(_message.Message):
    __slots__ = ("status", "logs")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    LOGS_FIELD_NUMBER: _ClassVar[int]
    status: int
    logs: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_p3plog]
    def __init__(self, status: _Optional[int] = ..., logs: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_p3plog, _Mapping]]] = ...) -> None: ...

class pbreq_p3p_video(_message.Message):
    __slots__ = ("vid",)
    VID_FIELD_NUMBER: _ClassVar[int]
    vid: int
    def __init__(self, vid: _Optional[int] = ...) -> None: ...

class pbrsp_p3p_video(_message.Message):
    __slots__ = ("status", "video")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    VIDEO_FIELD_NUMBER: _ClassVar[int]
    status: int
    video: _dr2_comm_pb_pb2.pb_p3pvideo
    def __init__(self, status: _Optional[int] = ..., video: _Optional[_Union[_dr2_comm_pb_pb2.pb_p3pvideo, _Mapping]] = ...) -> None: ...

class pbreq_p3p_info(_message.Message):
    __slots__ = ("uid",)
    UID_FIELD_NUMBER: _ClassVar[int]
    uid: int
    def __init__(self, uid: _Optional[int] = ...) -> None: ...

class pbrsp_p3p_info(_message.Message):
    __slots__ = ("status", "unit")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    UNIT_FIELD_NUMBER: _ClassVar[int]
    status: int
    unit: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_unit]
    def __init__(self, status: _Optional[int] = ..., unit: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_unit, _Mapping]]] = ...) -> None: ...

class pbreq_fpk_camp(_message.Message):
    __slots__ = ("camp", "tid")
    CAMP_FIELD_NUMBER: _ClassVar[int]
    TID_FIELD_NUMBER: _ClassVar[int]
    camp: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_unit]
    tid: int
    def __init__(self, camp: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_unit, _Mapping]]] = ..., tid: _Optional[int] = ...) -> None: ...

class pbrsp_fpk_camp(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_spvp_sync(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class pbrsp_spvp_sync(_message.Message):
    __slots__ = ("status", "first", "flag", "cd", "score", "win_times", "cur_times", "def_score", "season", "camp", "power", "match", "h_bag")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    FIRST_FIELD_NUMBER: _ClassVar[int]
    FLAG_FIELD_NUMBER: _ClassVar[int]
    CD_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    WIN_TIMES_FIELD_NUMBER: _ClassVar[int]
    CUR_TIMES_FIELD_NUMBER: _ClassVar[int]
    DEF_SCORE_FIELD_NUMBER: _ClassVar[int]
    SEASON_FIELD_NUMBER: _ClassVar[int]
    CAMP_FIELD_NUMBER: _ClassVar[int]
    POWER_FIELD_NUMBER: _ClassVar[int]
    MATCH_FIELD_NUMBER: _ClassVar[int]
    H_BAG_FIELD_NUMBER: _ClassVar[int]
    status: int
    first: int
    flag: int
    cd: int
    score: int
    win_times: int
    cur_times: int
    def_score: int
    season: int
    camp: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_unit]
    power: int
    match: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_match]
    h_bag: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_match_hero]
    def __init__(self, status: _Optional[int] = ..., first: _Optional[int] = ..., flag: _Optional[int] = ..., cd: _Optional[int] = ..., score: _Optional[int] = ..., win_times: _Optional[int] = ..., cur_times: _Optional[int] = ..., def_score: _Optional[int] = ..., season: _Optional[int] = ..., camp: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_unit, _Mapping]]] = ..., power: _Optional[int] = ..., match: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_match, _Mapping]]] = ..., h_bag: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_match_hero, _Mapping]]] = ...) -> None: ...

class pbreq_spvp_camp(_message.Message):
    __slots__ = ("camp",)
    CAMP_FIELD_NUMBER: _ClassVar[int]
    camp: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_unit]
    def __init__(self, camp: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_unit, _Mapping]]] = ...) -> None: ...

class pbrsp_spvp_camp(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_spvp_rank(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class pbrsp_spvp_rank(_message.Message):
    __slots__ = ("status", "rank", "last_rank", "score")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    RANK_FIELD_NUMBER: _ClassVar[int]
    LAST_RANK_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    status: int
    rank: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_smbrs]
    last_rank: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_smbrs]
    score: int
    def __init__(self, status: _Optional[int] = ..., rank: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_smbrs, _Mapping]]] = ..., last_rank: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_smbrs, _Mapping]]] = ..., score: _Optional[int] = ...) -> None: ...

class pbreq_spvp_fight(_message.Message):
    __slots__ = ("camp", "pos", "d_idx")
    CAMP_FIELD_NUMBER: _ClassVar[int]
    POS_FIELD_NUMBER: _ClassVar[int]
    D_IDX_FIELD_NUMBER: _ClassVar[int]
    camp: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_unit]
    pos: _containers.RepeatedScalarFieldContainer[int]
    d_idx: int
    def __init__(self, camp: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_unit, _Mapping]]] = ..., pos: _Optional[_Iterable[int]] = ..., d_idx: _Optional[int] = ...) -> None: ...

class pbrsp_spvp_fight(_message.Message):
    __slots__ = ("status", "video")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    VIDEO_FIELD_NUMBER: _ClassVar[int]
    status: int
    video: _dr2_comm_pb_pb2.pb_pvideo
    def __init__(self, status: _Optional[int] = ..., video: _Optional[_Union[_dr2_comm_pb_pb2.pb_pvideo, _Mapping]] = ...) -> None: ...

class pbreq_spvp_match(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class pbrsp_spvp_match(_message.Message):
    __slots__ = ("status", "match")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MATCH_FIELD_NUMBER: _ClassVar[int]
    status: int
    match: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_match]
    def __init__(self, status: _Optional[int] = ..., match: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_match, _Mapping]]] = ...) -> None: ...

class pbreq_spvp_plunder(_message.Message):
    __slots__ = ("pos", "o_pos")
    POS_FIELD_NUMBER: _ClassVar[int]
    O_POS_FIELD_NUMBER: _ClassVar[int]
    pos: _containers.RepeatedScalarFieldContainer[int]
    o_pos: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, pos: _Optional[_Iterable[int]] = ..., o_pos: _Optional[_Iterable[int]] = ...) -> None: ...

class pbrsp_spvp_plunder(_message.Message):
    __slots__ = ("status", "accounts")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ACCOUNTS_FIELD_NUMBER: _ClassVar[int]
    status: int
    accounts: _dr2_comm_pb_pb2.pb_pvp_accounts
    def __init__(self, status: _Optional[int] = ..., accounts: _Optional[_Union[_dr2_comm_pb_pb2.pb_pvp_accounts, _Mapping]] = ...) -> None: ...

class pbreq_spvp_def(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class pbrsp_spvp_def(_message.Message):
    __slots__ = ("status", "score", "count", "total")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    DEF_FIELD_NUMBER: _ClassVar[int]
    status: int
    score: int
    count: int
    total: int
    def __init__(self, status: _Optional[int] = ..., score: _Optional[int] = ..., count: _Optional[int] = ..., total: _Optional[int] = ..., **kwargs) -> None: ...

class pbreq_spvp_last_rank(_message.Message):
    __slots__ = ("type",)
    TYPE_FIELD_NUMBER: _ClassVar[int]
    type: int
    def __init__(self, type: _Optional[int] = ...) -> None: ...

class pbrsp_spvp_last_rank(_message.Message):
    __slots__ = ("status", "rank")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    RANK_FIELD_NUMBER: _ClassVar[int]
    status: int
    rank: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_smbr]
    def __init__(self, status: _Optional[int] = ..., rank: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_smbr, _Mapping]]] = ...) -> None: ...

class pbreq_spvp_info(_message.Message):
    __slots__ = ("uid",)
    UID_FIELD_NUMBER: _ClassVar[int]
    uid: int
    def __init__(self, uid: _Optional[int] = ...) -> None: ...

class pbrsp_spvp_info(_message.Message):
    __slots__ = ("status", "unit", "power")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    UNIT_FIELD_NUMBER: _ClassVar[int]
    POWER_FIELD_NUMBER: _ClassVar[int]
    status: int
    unit: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_unit]
    power: int
    def __init__(self, status: _Optional[int] = ..., unit: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_unit, _Mapping]]] = ..., power: _Optional[int] = ...) -> None: ...

class pbreq_htask(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class pbrsp_htask(_message.Message):
    __slots__ = ("cd", "tasks", "heads", "reward", "task_ids")
    CD_FIELD_NUMBER: _ClassVar[int]
    TASKS_FIELD_NUMBER: _ClassVar[int]
    HEADS_FIELD_NUMBER: _ClassVar[int]
    REWARD_FIELD_NUMBER: _ClassVar[int]
    TASK_IDS_FIELD_NUMBER: _ClassVar[int]
    cd: int
    tasks: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_htask]
    heads: _containers.RepeatedScalarFieldContainer[int]
    reward: _dr2_comm_pb_pb2.pb_bag
    task_ids: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, cd: _Optional[int] = ..., tasks: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_htask, _Mapping]]] = ..., heads: _Optional[_Iterable[int]] = ..., reward: _Optional[_Union[_dr2_comm_pb_pb2.pb_bag, _Mapping]] = ..., task_ids: _Optional[_Iterable[int]] = ...) -> None: ...

class pbreq_htask_start(_message.Message):
    __slots__ = ("tid", "hids", "heads")
    TID_FIELD_NUMBER: _ClassVar[int]
    HIDS_FIELD_NUMBER: _ClassVar[int]
    HEADS_FIELD_NUMBER: _ClassVar[int]
    tid: int
    hids: _containers.RepeatedScalarFieldContainer[int]
    heads: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, tid: _Optional[int] = ..., hids: _Optional[_Iterable[int]] = ..., heads: _Optional[_Iterable[int]] = ...) -> None: ...

class pbrsp_htask_start(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_htask_speedup(_message.Message):
    __slots__ = ("tid",)
    TID_FIELD_NUMBER: _ClassVar[int]
    tid: int
    def __init__(self, tid: _Optional[int] = ...) -> None: ...

class pbrsp_htask_speedup(_message.Message):
    __slots__ = ("status", "reward")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    REWARD_FIELD_NUMBER: _ClassVar[int]
    status: int
    reward: _dr2_comm_pb_pb2.pb_bag
    def __init__(self, status: _Optional[int] = ..., reward: _Optional[_Union[_dr2_comm_pb_pb2.pb_bag, _Mapping]] = ...) -> None: ...

class pbreq_htask_rec(_message.Message):
    __slots__ = ("tid",)
    TID_FIELD_NUMBER: _ClassVar[int]
    tid: int
    def __init__(self, tid: _Optional[int] = ...) -> None: ...

class pbrsp_htask_rec(_message.Message):
    __slots__ = ("status", "reward")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    REWARD_FIELD_NUMBER: _ClassVar[int]
    status: int
    reward: _dr2_comm_pb_pb2.pb_bag
    def __init__(self, status: _Optional[int] = ..., reward: _Optional[_Union[_dr2_comm_pb_pb2.pb_bag, _Mapping]] = ...) -> None: ...

class pbreq_htask_gem(_message.Message):
    __slots__ = ("star", "type")
    STAR_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    star: int
    type: int
    def __init__(self, star: _Optional[int] = ..., type: _Optional[int] = ...) -> None: ...

class pbrsp_htask_gem(_message.Message):
    __slots__ = ("status", "tasks")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    TASKS_FIELD_NUMBER: _ClassVar[int]
    status: int
    tasks: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_htask]
    def __init__(self, status: _Optional[int] = ..., tasks: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_htask, _Mapping]]] = ...) -> None: ...

class pbreq_htask_add(_message.Message):
    __slots__ = ("ntype", "type")
    NTYPE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ntype: int
    type: int
    def __init__(self, ntype: _Optional[int] = ..., type: _Optional[int] = ...) -> None: ...

class pbrsp_htask_add(_message.Message):
    __slots__ = ("status", "task")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    TASK_FIELD_NUMBER: _ClassVar[int]
    status: int
    task: _dr2_comm_pb_pb2.pb_htask
    def __init__(self, status: _Optional[int] = ..., task: _Optional[_Union[_dr2_comm_pb_pb2.pb_htask, _Mapping]] = ...) -> None: ...

class pbreq_htask_auto(_message.Message):
    __slots__ = ("type", "info")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    INFO_FIELD_NUMBER: _ClassVar[int]
    type: int
    info: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_htask_info]
    def __init__(self, type: _Optional[int] = ..., info: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_htask_info, _Mapping]]] = ...) -> None: ...

class pbrsp_htask_auto(_message.Message):
    __slots__ = ("status", "tids")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    TIDS_FIELD_NUMBER: _ClassVar[int]
    status: int
    tids: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, status: _Optional[int] = ..., tids: _Optional[_Iterable[int]] = ...) -> None: ...

class pbreq_achieve(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class pbrsp_achieve(_message.Message):
    __slots__ = ("num", "id")
    NUM_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    num: _containers.RepeatedScalarFieldContainer[int]
    id: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, num: _Optional[_Iterable[int]] = ..., id: _Optional[_Iterable[int]] = ...) -> None: ...

class pbreq_achieve_claim(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class pbrsp_achieve_claim(_message.Message):
    __slots__ = ("status", "reward")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    REWARD_FIELD_NUMBER: _ClassVar[int]
    status: int
    reward: _dr2_comm_pb_pb2.pb_bag
    def __init__(self, status: _Optional[int] = ..., reward: _Optional[_Union[_dr2_comm_pb_pb2.pb_bag, _Mapping]] = ...) -> None: ...

class pbreq_achievie_attention(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class pbrsp_achievie_attention(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_pay(_message.Message):
    __slots__ = ("order", "id", "platform", "package", "token", "appsflyer", "advertising", "vsn", "store_currency", "local_price", "gz_token")
    ORDER_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    PLATFORM_FIELD_NUMBER: _ClassVar[int]
    PACKAGE_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    APPSFLYER_FIELD_NUMBER: _ClassVar[int]
    ADVERTISING_FIELD_NUMBER: _ClassVar[int]
    VSN_FIELD_NUMBER: _ClassVar[int]
    STORE_CURRENCY_FIELD_NUMBER: _ClassVar[int]
    LOCAL_PRICE_FIELD_NUMBER: _ClassVar[int]
    GZ_TOKEN_FIELD_NUMBER: _ClassVar[int]
    order: _containers.RepeatedScalarFieldContainer[str]
    id: _containers.RepeatedScalarFieldContainer[int]
    platform: str
    package: str
    token: _containers.RepeatedScalarFieldContainer[str]
    appsflyer: str
    advertising: str
    vsn: int
    store_currency: _containers.RepeatedScalarFieldContainer[str]
    local_price: _containers.RepeatedScalarFieldContainer[str]
    gz_token: _containers.RepeatedScalarFieldContainer[bytes]
    def __init__(self, order: _Optional[_Iterable[str]] = ..., id: _Optional[_Iterable[int]] = ..., platform: _Optional[str] = ..., package: _Optional[str] = ..., token: _Optional[_Iterable[str]] = ..., appsflyer: _Optional[str] = ..., advertising: _Optional[str] = ..., vsn: _Optional[int] = ..., store_currency: _Optional[_Iterable[str]] = ..., local_price: _Optional[_Iterable[str]] = ..., gz_token: _Optional[_Iterable[bytes]] = ...) -> None: ...

class pbrsp_pay(_message.Message):
    __slots__ = ("status", "reward")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    REWARD_FIELD_NUMBER: _ClassVar[int]
    status: int
    reward: _dr2_comm_pb_pb2.pb_bag
    def __init__(self, status: _Optional[int] = ..., reward: _Optional[_Union[_dr2_comm_pb_pb2.pb_bag, _Mapping]] = ...) -> None: ...

class pbreq_fpay(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class pbrsp_fpay(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_pay2(_message.Message):
    __slots__ = ("data", "left", "size")
    DATA_FIELD_NUMBER: _ClassVar[int]
    LEFT_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    data: bytes
    left: int
    size: int
    def __init__(self, data: _Optional[bytes] = ..., left: _Optional[int] = ..., size: _Optional[int] = ...) -> None: ...

class pbrsp_pay2(_message.Message):
    __slots__ = ("status", "reward")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    REWARD_FIELD_NUMBER: _ClassVar[int]
    status: int
    reward: _dr2_comm_pb_pb2.pb_bag
    def __init__(self, status: _Optional[int] = ..., reward: _Optional[_Union[_dr2_comm_pb_pb2.pb_bag, _Mapping]] = ...) -> None: ...

class pbreq_gorder(_message.Message):
    __slots__ = ("storeid", "type", "device_info", "body", "subject", "extInfo")
    STOREID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    DEVICE_INFO_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    SUBJECT_FIELD_NUMBER: _ClassVar[int]
    EXTINFO_FIELD_NUMBER: _ClassVar[int]
    storeid: int
    type: int
    device_info: str
    body: str
    subject: str
    extInfo: str
    def __init__(self, storeid: _Optional[int] = ..., type: _Optional[int] = ..., device_info: _Optional[str] = ..., body: _Optional[str] = ..., subject: _Optional[str] = ..., extInfo: _Optional[str] = ...) -> None: ...

class pbrsp_gorder(_message.Message):
    __slots__ = ("status", "order_info")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ORDER_INFO_FIELD_NUMBER: _ClassVar[int]
    status: int
    order_info: str
    def __init__(self, status: _Optional[int] = ..., order_info: _Optional[str] = ...) -> None: ...

class pbreq_gpay(_message.Message):
    __slots__ = ("orderid", "appsflyer", "advertising", "userid", "productid", "txid")
    ORDERID_FIELD_NUMBER: _ClassVar[int]
    APPSFLYER_FIELD_NUMBER: _ClassVar[int]
    ADVERTISING_FIELD_NUMBER: _ClassVar[int]
    USERID_FIELD_NUMBER: _ClassVar[int]
    PRODUCTID_FIELD_NUMBER: _ClassVar[int]
    TXID_FIELD_NUMBER: _ClassVar[int]
    orderid: str
    appsflyer: str
    advertising: str
    userid: str
    productid: str
    txid: str
    def __init__(self, orderid: _Optional[str] = ..., appsflyer: _Optional[str] = ..., advertising: _Optional[str] = ..., userid: _Optional[str] = ..., productid: _Optional[str] = ..., txid: _Optional[str] = ...) -> None: ...

class pbrsp_gpay(_message.Message):
    __slots__ = ("status", "reward")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    REWARD_FIELD_NUMBER: _ClassVar[int]
    status: int
    reward: _dr2_comm_pb_pb2.pb_bag
    def __init__(self, status: _Optional[int] = ..., reward: _Optional[_Union[_dr2_comm_pb_pb2.pb_bag, _Mapping]] = ...) -> None: ...

class pbreq_chpay(_message.Message):
    __slots__ = ("storeid", "store_country", "store_currency")
    STOREID_FIELD_NUMBER: _ClassVar[int]
    STORE_COUNTRY_FIELD_NUMBER: _ClassVar[int]
    STORE_CURRENCY_FIELD_NUMBER: _ClassVar[int]
    storeid: int
    store_country: str
    store_currency: str
    def __init__(self, storeid: _Optional[int] = ..., store_country: _Optional[str] = ..., store_currency: _Optional[str] = ...) -> None: ...

class pbrsp_chpay(_message.Message):
    __slots__ = ("status", "token", "productid")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    PRODUCTID_FIELD_NUMBER: _ClassVar[int]
    status: int
    token: str
    productid: str
    def __init__(self, status: _Optional[int] = ..., token: _Optional[str] = ..., productid: _Optional[str] = ...) -> None: ...

class pbreq_amznpay(_message.Message):
    __slots__ = ("receiptid", "userid")
    RECEIPTID_FIELD_NUMBER: _ClassVar[int]
    USERID_FIELD_NUMBER: _ClassVar[int]
    receiptid: _containers.RepeatedScalarFieldContainer[str]
    userid: str
    def __init__(self, receiptid: _Optional[_Iterable[str]] = ..., userid: _Optional[str] = ...) -> None: ...

class pbrsp_amznpay(_message.Message):
    __slots__ = ("status", "reward", "money")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    REWARD_FIELD_NUMBER: _ClassVar[int]
    MONEY_FIELD_NUMBER: _ClassVar[int]
    status: int
    reward: _dr2_comm_pb_pb2.pb_bag
    money: str
    def __init__(self, status: _Optional[int] = ..., reward: _Optional[_Union[_dr2_comm_pb_pb2.pb_bag, _Mapping]] = ..., money: _Optional[str] = ...) -> None: ...

class pbreq_onepay(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_onepay]
    def __init__(self, items: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_onepay, _Mapping]]] = ...) -> None: ...

class pbrsp_onepay(_message.Message):
    __slots__ = ("status", "reward", "money")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    REWARD_FIELD_NUMBER: _ClassVar[int]
    MONEY_FIELD_NUMBER: _ClassVar[int]
    status: int
    reward: _dr2_comm_pb_pb2.pb_bag
    money: str
    def __init__(self, status: _Optional[int] = ..., reward: _Optional[_Union[_dr2_comm_pb_pb2.pb_bag, _Mapping]] = ..., money: _Optional[str] = ...) -> None: ...

class pbreq_oneforum(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class pbrsp_oneforum(_message.Message):
    __slots__ = ("status", "reward")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    REWARD_FIELD_NUMBER: _ClassVar[int]
    status: int
    reward: _dr2_comm_pb_pb2.pb_bag
    def __init__(self, status: _Optional[int] = ..., reward: _Optional[_Union[_dr2_comm_pb_pb2.pb_bag, _Mapping]] = ...) -> None: ...

class pbreq_gpay2(_message.Message):
    __slots__ = ("order", "token", "id", "platform", "ext")
    ORDER_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    PLATFORM_FIELD_NUMBER: _ClassVar[int]
    EXT_FIELD_NUMBER: _ClassVar[int]
    order: _containers.RepeatedScalarFieldContainer[str]
    token: _containers.RepeatedScalarFieldContainer[str]
    id: _containers.RepeatedScalarFieldContainer[str]
    platform: str
    ext: str
    def __init__(self, order: _Optional[_Iterable[str]] = ..., token: _Optional[_Iterable[str]] = ..., id: _Optional[_Iterable[str]] = ..., platform: _Optional[str] = ..., ext: _Optional[str] = ...) -> None: ...

class pbrsp_gpay2(_message.Message):
    __slots__ = ("status", "reward")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    REWARD_FIELD_NUMBER: _ClassVar[int]
    status: int
    reward: _dr2_comm_pb_pb2.pb_bag
    def __init__(self, status: _Optional[int] = ..., reward: _Optional[_Union[_dr2_comm_pb_pb2.pb_bag, _Mapping]] = ...) -> None: ...

class pbreq_voucher(_message.Message):
    __slots__ = ("storeid", "type")
    STOREID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    storeid: int
    type: int
    def __init__(self, storeid: _Optional[int] = ..., type: _Optional[int] = ...) -> None: ...

class pbrsp_voucher(_message.Message):
    __slots__ = ("status", "reward")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    REWARD_FIELD_NUMBER: _ClassVar[int]
    status: int
    reward: _dr2_comm_pb_pb2.pb_bag
    def __init__(self, status: _Optional[int] = ..., reward: _Optional[_Union[_dr2_comm_pb_pb2.pb_bag, _Mapping]] = ...) -> None: ...

class pbreq_storeinfo(_message.Message):
    __slots__ = ("store_country", "store_currency")
    STORE_COUNTRY_FIELD_NUMBER: _ClassVar[int]
    STORE_CURRENCY_FIELD_NUMBER: _ClassVar[int]
    store_country: str
    store_currency: str
    def __init__(self, store_country: _Optional[str] = ..., store_currency: _Optional[str] = ...) -> None: ...

class pbrsp_storeinfo(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class pbreq_hmarket_buy(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class pbrsp_hmarket_buy(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_hmarket_sync(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class pbrsp_hmarket_sync(_message.Message):
    __slots__ = ("status", "item")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ITEM_FIELD_NUMBER: _ClassVar[int]
    status: int
    item: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_hmarket]
    def __init__(self, status: _Optional[int] = ..., item: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_hmarket, _Mapping]]] = ...) -> None: ...

class pbreq_brave_market_buy(_message.Message):
    __slots__ = ("id", "num")
    ID_FIELD_NUMBER: _ClassVar[int]
    NUM_FIELD_NUMBER: _ClassVar[int]
    id: int
    num: int
    def __init__(self, id: _Optional[int] = ..., num: _Optional[int] = ...) -> None: ...

class pbrsp_brave_market_buy(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_brave_market_sync(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class pbrsp_brave_market_sync(_message.Message):
    __slots__ = ("status", "item")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ITEM_FIELD_NUMBER: _ClassVar[int]
    status: int
    item: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_hmarket]
    def __init__(self, status: _Optional[int] = ..., item: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_hmarket, _Mapping]]] = ...) -> None: ...

class pbreq_hmarket_refresh(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class pbrsp_hmarket_refresh(_message.Message):
    __slots__ = ("status", "item")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ITEM_FIELD_NUMBER: _ClassVar[int]
    status: int
    item: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_hmarket]
    def __init__(self, status: _Optional[int] = ..., item: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_hmarket, _Mapping]]] = ...) -> None: ...

class pbreq_alogin(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class pbrsp_alogin(_message.Message):
    __slots__ = ("status", "bag")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    BAG_FIELD_NUMBER: _ClassVar[int]
    status: int
    bag: _dr2_comm_pb_pb2.pb_bag
    def __init__(self, status: _Optional[int] = ..., bag: _Optional[_Union[_dr2_comm_pb_pb2.pb_bag, _Mapping]] = ...) -> None: ...

class pbreq_task_claim(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class pbrsp_task_claim(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_online_claim(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class pbrsp_online_claim(_message.Message):
    __slots__ = ("status", "online")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ONLINE_FIELD_NUMBER: _ClassVar[int]
    status: int
    online: _dr2_comm_pb_pb2.pb_online
    def __init__(self, status: _Optional[int] = ..., online: _Optional[_Union[_dr2_comm_pb_pb2.pb_online, _Mapping]] = ...) -> None: ...

class pbreq_task_convert(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class pbrsp_task_convert(_message.Message):
    __slots__ = ("status", "reward")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    REWARD_FIELD_NUMBER: _ClassVar[int]
    status: int
    reward: _dr2_comm_pb_pb2.pb_bag
    def __init__(self, status: _Optional[int] = ..., reward: _Optional[_Union[_dr2_comm_pb_pb2.pb_bag, _Mapping]] = ...) -> None: ...

class pbreq_fun_info(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class pbrsp_fun_info(_message.Message):
    __slots__ = ("infos",)
    INFOS_FIELD_NUMBER: _ClassVar[int]
    infos: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_fun]
    def __init__(self, infos: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_fun, _Mapping]]] = ...) -> None: ...

class pbreq_puz_sync(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class pbrsp_puz_sync(_message.Message):
    __slots__ = ("status", "puz", "mall", "buy", "siz")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    PUZ_FIELD_NUMBER: _ClassVar[int]
    MALL_FIELD_NUMBER: _ClassVar[int]
    BUY_FIELD_NUMBER: _ClassVar[int]
    DEL_FIELD_NUMBER: _ClassVar[int]
    SIZ_FIELD_NUMBER: _ClassVar[int]
    status: int
    puz: _dr2_comm_pb_pb2.pb_puzzle
    mall: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_kv]
    buy: int
    siz: int
    def __init__(self, status: _Optional[int] = ..., puz: _Optional[_Union[_dr2_comm_pb_pb2.pb_puzzle, _Mapping]] = ..., mall: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_kv, _Mapping]]] = ..., buy: _Optional[int] = ..., siz: _Optional[int] = ..., **kwargs) -> None: ...

class pbreq_puz_buy(_message.Message):
    __slots__ = ("id", "num")
    ID_FIELD_NUMBER: _ClassVar[int]
    NUM_FIELD_NUMBER: _ClassVar[int]
    id: int
    num: int
    def __init__(self, id: _Optional[int] = ..., num: _Optional[int] = ...) -> None: ...

class pbrsp_puz_buy(_message.Message):
    __slots__ = ("status", "bag")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    BAG_FIELD_NUMBER: _ClassVar[int]
    status: int
    bag: _dr2_comm_pb_pb2.pb_bag
    def __init__(self, status: _Optional[int] = ..., bag: _Optional[_Union[_dr2_comm_pb_pb2.pb_bag, _Mapping]] = ...) -> None: ...

class pbreq_puz_fill(_message.Message):
    __slots__ = ("pos", "id")
    POS_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    pos: int
    id: int
    def __init__(self, pos: _Optional[int] = ..., id: _Optional[int] = ...) -> None: ...

class pbrsp_puz_fill(_message.Message):
    __slots__ = ("status", "puz", "pos", "num", "next")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    PUZ_FIELD_NUMBER: _ClassVar[int]
    POS_FIELD_NUMBER: _ClassVar[int]
    NUM_FIELD_NUMBER: _ClassVar[int]
    NEXT_FIELD_NUMBER: _ClassVar[int]
    status: int
    puz: _dr2_comm_pb_pb2.pb_puzzle
    pos: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_kv]
    num: int
    next: int
    def __init__(self, status: _Optional[int] = ..., puz: _Optional[_Union[_dr2_comm_pb_pb2.pb_puzzle, _Mapping]] = ..., pos: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_kv, _Mapping]]] = ..., num: _Optional[int] = ..., next: _Optional[int] = ...) -> None: ...

class pbreq_puz_tear(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class pbrsp_puz_tear(_message.Message):
    __slots__ = ("status", "pos")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    POS_FIELD_NUMBER: _ClassVar[int]
    status: int
    pos: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_kv]
    def __init__(self, status: _Optional[int] = ..., pos: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_kv, _Mapping]]] = ...) -> None: ...

class pbreq_puz_sure(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class pbrsp_puz_sure(_message.Message):
    __slots__ = ("status", "puz", "num")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    PUZ_FIELD_NUMBER: _ClassVar[int]
    NUM_FIELD_NUMBER: _ClassVar[int]
    status: int
    puz: _dr2_comm_pb_pb2.pb_puzzle
    num: int
    def __init__(self, status: _Optional[int] = ..., puz: _Optional[_Union[_dr2_comm_pb_pb2.pb_puzzle, _Mapping]] = ..., num: _Optional[int] = ...) -> None: ...

class pbreq_puz_coin(_message.Message):
    __slots__ = ("num",)
    NUM_FIELD_NUMBER: _ClassVar[int]
    num: int
    def __init__(self, num: _Optional[int] = ...) -> None: ...

class pbrsp_puz_coin(_message.Message):
    __slots__ = ("status", "bag", "next")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    BAG_FIELD_NUMBER: _ClassVar[int]
    NEXT_FIELD_NUMBER: _ClassVar[int]
    status: int
    bag: _dr2_comm_pb_pb2.pb_bag
    next: int
    def __init__(self, status: _Optional[int] = ..., bag: _Optional[_Union[_dr2_comm_pb_pb2.pb_bag, _Mapping]] = ..., next: _Optional[int] = ...) -> None: ...

class pbreq_puz_wipe(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class pbrsp_puz_wipe(_message.Message):
    __slots__ = ("status", "puz", "item")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    PUZ_FIELD_NUMBER: _ClassVar[int]
    ITEM_FIELD_NUMBER: _ClassVar[int]
    status: int
    puz: _dr2_comm_pb_pb2.pb_puzzle
    item: _dr2_comm_pb_pb2.pb_item
    def __init__(self, status: _Optional[int] = ..., puz: _Optional[_Union[_dr2_comm_pb_pb2.pb_puzzle, _Mapping]] = ..., item: _Optional[_Union[_dr2_comm_pb_pb2.pb_item, _Mapping]] = ...) -> None: ...

class pbreq_gmarket_buy(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class pbrsp_gmarket_buy(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_gmarket_sync(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class pbrsp_gmarket_sync(_message.Message):
    __slots__ = ("status", "item", "cd")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ITEM_FIELD_NUMBER: _ClassVar[int]
    CD_FIELD_NUMBER: _ClassVar[int]
    status: int
    item: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_gmarket]
    cd: int
    def __init__(self, status: _Optional[int] = ..., item: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_gmarket, _Mapping]]] = ..., cd: _Optional[int] = ...) -> None: ...

class pbreq_gmarket_refresh(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class pbrsp_gmarket_refresh(_message.Message):
    __slots__ = ("status", "item")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ITEM_FIELD_NUMBER: _ClassVar[int]
    status: int
    item: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_gmarket]
    def __init__(self, status: _Optional[int] = ..., item: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_gmarket, _Mapping]]] = ...) -> None: ...

class pbreq_gmarket_exchange(_message.Message):
    __slots__ = ("num",)
    NUM_FIELD_NUMBER: _ClassVar[int]
    num: int
    def __init__(self, num: _Optional[int] = ...) -> None: ...

class pbrsp_gmarket_exchange(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_ngw_sync(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class pbrsp_ngw_sync(_message.Message):
    __slots__ = ("status", "cd", "sholds", "seg", "mid", "aflag", "hids", "rank", "defcamp", "vary")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    CD_FIELD_NUMBER: _ClassVar[int]
    SHOLDS_FIELD_NUMBER: _ClassVar[int]
    SEG_FIELD_NUMBER: _ClassVar[int]
    MID_FIELD_NUMBER: _ClassVar[int]
    AFLAG_FIELD_NUMBER: _ClassVar[int]
    HIDS_FIELD_NUMBER: _ClassVar[int]
    RANK_FIELD_NUMBER: _ClassVar[int]
    DEFCAMP_FIELD_NUMBER: _ClassVar[int]
    VARY_FIELD_NUMBER: _ClassVar[int]
    status: int
    cd: int
    sholds: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_ngwshold]
    seg: int
    mid: int
    aflag: int
    hids: _containers.RepeatedScalarFieldContainer[int]
    rank: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_ngwrank]
    defcamp: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_unit]
    vary: int
    def __init__(self, status: _Optional[int] = ..., cd: _Optional[int] = ..., sholds: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_ngwshold, _Mapping]]] = ..., seg: _Optional[int] = ..., mid: _Optional[int] = ..., aflag: _Optional[int] = ..., hids: _Optional[_Iterable[int]] = ..., rank: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_ngwrank, _Mapping]]] = ..., defcamp: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_unit, _Mapping]]] = ..., vary: _Optional[int] = ...) -> None: ...

class pbreq_ngw_rank(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class pbrsp_ngw_rank(_message.Message):
    __slots__ = ("status", "grank", "prank")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    GRANK_FIELD_NUMBER: _ClassVar[int]
    PRANK_FIELD_NUMBER: _ClassVar[int]
    status: int
    grank: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_ngwrank]
    prank: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_ngwprank]
    def __init__(self, status: _Optional[int] = ..., grank: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_ngwrank, _Mapping]]] = ..., prank: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_ngwprank, _Mapping]]] = ...) -> None: ...

class pbreq_ngw_camp(_message.Message):
    __slots__ = ("id", "camp")
    ID_FIELD_NUMBER: _ClassVar[int]
    CAMP_FIELD_NUMBER: _ClassVar[int]
    id: int
    camp: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_unit]
    def __init__(self, id: _Optional[int] = ..., camp: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_unit, _Mapping]]] = ...) -> None: ...

class pbrsp_ngw_camp(_message.Message):
    __slots__ = ("status", "sholds")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    SHOLDS_FIELD_NUMBER: _ClassVar[int]
    status: int
    sholds: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_ngwshold]
    def __init__(self, status: _Optional[int] = ..., sholds: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_ngwshold, _Mapping]]] = ...) -> None: ...

class pbreq_ngw_shold(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class pbrsp_ngw_shold(_message.Message):
    __slots__ = ("status", "mbrs", "sholds", "mid")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MBRS_FIELD_NUMBER: _ClassVar[int]
    SHOLDS_FIELD_NUMBER: _ClassVar[int]
    MID_FIELD_NUMBER: _ClassVar[int]
    status: int
    mbrs: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_ngwmbr]
    sholds: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_ngwshold]
    mid: int
    def __init__(self, status: _Optional[int] = ..., mbrs: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_ngwmbr, _Mapping]]] = ..., sholds: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_ngwshold, _Mapping]]] = ..., mid: _Optional[int] = ...) -> None: ...

class pbreq_ngw_fight(_message.Message):
    __slots__ = ("id", "camp")
    ID_FIELD_NUMBER: _ClassVar[int]
    CAMP_FIELD_NUMBER: _ClassVar[int]
    id: int
    camp: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_unit]
    def __init__(self, id: _Optional[int] = ..., camp: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_unit, _Mapping]]] = ...) -> None: ...

class pbrsp_ngw_fight(_message.Message):
    __slots__ = ("status", "destroy")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    DESTROY_FIELD_NUMBER: _ClassVar[int]
    status: int
    destroy: int
    def __init__(self, status: _Optional[int] = ..., destroy: _Optional[int] = ...) -> None: ...

class pbreq_ngw_lup(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class pbrsp_ngw_lup(_message.Message):
    __slots__ = ("uids", "powers")
    UIDS_FIELD_NUMBER: _ClassVar[int]
    POWERS_FIELD_NUMBER: _ClassVar[int]
    uids: _containers.RepeatedScalarFieldContainer[int]
    powers: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, uids: _Optional[_Iterable[int]] = ..., powers: _Optional[_Iterable[int]] = ...) -> None: ...

class pbreq_ngw_setup(_message.Message):
    __slots__ = ("uids",)
    UIDS_FIELD_NUMBER: _ClassVar[int]
    uids: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, uids: _Optional[_Iterable[int]] = ...) -> None: ...

class pbrsp_ngw_setup(_message.Message):
    __slots__ = ("status", "cd")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    CD_FIELD_NUMBER: _ClassVar[int]
    status: int
    cd: int
    def __init__(self, status: _Optional[int] = ..., cd: _Optional[int] = ...) -> None: ...

class pbreq_ngw_buy(_message.Message):
    __slots__ = ("id", "bid")
    ID_FIELD_NUMBER: _ClassVar[int]
    BID_FIELD_NUMBER: _ClassVar[int]
    id: int
    bid: int
    def __init__(self, id: _Optional[int] = ..., bid: _Optional[int] = ...) -> None: ...

class pbrsp_ngw_buy(_message.Message):
    __slots__ = ("status", "aflag", "sholds")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    AFLAG_FIELD_NUMBER: _ClassVar[int]
    SHOLDS_FIELD_NUMBER: _ClassVar[int]
    status: int
    aflag: int
    sholds: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_ngwshold]
    def __init__(self, status: _Optional[int] = ..., aflag: _Optional[int] = ..., sholds: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_ngwshold, _Mapping]]] = ...) -> None: ...

class pbreq_ngw_info(_message.Message):
    __slots__ = ("uid",)
    UID_FIELD_NUMBER: _ClassVar[int]
    uid: int
    def __init__(self, uid: _Optional[int] = ...) -> None: ...

class pbrsp_ngw_info(_message.Message):
    __slots__ = ("status", "unit")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    UNIT_FIELD_NUMBER: _ClassVar[int]
    status: int
    unit: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_unit]
    def __init__(self, status: _Optional[int] = ..., unit: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_unit, _Mapping]]] = ...) -> None: ...

class pbreq_ngw_video(_message.Message):
    __slots__ = ("vid",)
    VID_FIELD_NUMBER: _ClassVar[int]
    vid: int
    def __init__(self, vid: _Optional[int] = ...) -> None: ...

class pbrsp_ngw_video(_message.Message):
    __slots__ = ("status", "video")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    VIDEO_FIELD_NUMBER: _ClassVar[int]
    status: int
    video: _dr2_comm_pb_pb2.pb_pvideo
    def __init__(self, status: _Optional[int] = ..., video: _Optional[_Union[_dr2_comm_pb_pb2.pb_pvideo, _Mapping]] = ...) -> None: ...

class pbreq_ngw_sweep(_message.Message):
    __slots__ = ("camp",)
    CAMP_FIELD_NUMBER: _ClassVar[int]
    camp: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_unit]
    def __init__(self, camp: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_unit, _Mapping]]] = ...) -> None: ...

class pbrsp_ngw_sweep(_message.Message):
    __slots__ = ("status", "s_info")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    S_INFO_FIELD_NUMBER: _ClassVar[int]
    status: int
    s_info: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_ngw_sweep]
    def __init__(self, status: _Optional[int] = ..., s_info: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_ngw_sweep, _Mapping]]] = ...) -> None: ...

class pbreq_cgw_sync(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class pbrsp_cgw_sync(_message.Message):
    __slots__ = ("status", "cd", "wid", "pnum", "reg", "info", "camp", "sdate", "flag")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    CD_FIELD_NUMBER: _ClassVar[int]
    WID_FIELD_NUMBER: _ClassVar[int]
    PNUM_FIELD_NUMBER: _ClassVar[int]
    REG_FIELD_NUMBER: _ClassVar[int]
    INFO_FIELD_NUMBER: _ClassVar[int]
    CAMP_FIELD_NUMBER: _ClassVar[int]
    SDATE_FIELD_NUMBER: _ClassVar[int]
    FLAG_FIELD_NUMBER: _ClassVar[int]
    status: int
    cd: int
    wid: int
    pnum: int
    reg: bool
    info: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_cgw_info]
    camp: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_unit]
    sdate: str
    flag: int
    def __init__(self, status: _Optional[int] = ..., cd: _Optional[int] = ..., wid: _Optional[int] = ..., pnum: _Optional[int] = ..., reg: _Optional[bool] = ..., info: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_cgw_info, _Mapping]]] = ..., camp: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_unit, _Mapping]]] = ..., sdate: _Optional[str] = ..., flag: _Optional[int] = ...) -> None: ...

class pbreq_cgw_team(_message.Message):
    __slots__ = ("camp",)
    CAMP_FIELD_NUMBER: _ClassVar[int]
    camp: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_unit]
    def __init__(self, camp: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_unit, _Mapping]]] = ...) -> None: ...

class pbrsp_cgw_team(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_cgw_reg(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class pbrsp_cgw_reg(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_cgw_honor(_message.Message):
    __slots__ = ("wid",)
    WID_FIELD_NUMBER: _ClassVar[int]
    wid: int
    def __init__(self, wid: _Optional[int] = ...) -> None: ...

class pbrsp_cgw_honor(_message.Message):
    __slots__ = ("status", "info")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    INFO_FIELD_NUMBER: _ClassVar[int]
    status: int
    info: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_cgw_info]
    def __init__(self, status: _Optional[int] = ..., info: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_cgw_info, _Mapping]]] = ...) -> None: ...

class pbreq_cgw_record(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class pbrsp_cgw_record(_message.Message):
    __slots__ = ("status", "recs")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    RECS_FIELD_NUMBER: _ClassVar[int]
    status: int
    recs: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_cgw_record]
    def __init__(self, status: _Optional[int] = ..., recs: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_cgw_record, _Mapping]]] = ...) -> None: ...

class pbreq_cgw_race(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class pbrsp_cgw_race(_message.Message):
    __slots__ = ("status", "flag", "mbrs", "link")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    FLAG_FIELD_NUMBER: _ClassVar[int]
    MBRS_FIELD_NUMBER: _ClassVar[int]
    LINK_FIELD_NUMBER: _ClassVar[int]
    status: int
    flag: int
    mbrs: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_cgw_info]
    link: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_clink]
    def __init__(self, status: _Optional[int] = ..., flag: _Optional[int] = ..., mbrs: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_cgw_info, _Mapping]]] = ..., link: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_clink, _Mapping]]] = ...) -> None: ...

class pbreq_cgw_log(_message.Message):
    __slots__ = ("vid",)
    VID_FIELD_NUMBER: _ClassVar[int]
    vid: int
    def __init__(self, vid: _Optional[int] = ...) -> None: ...

class pbrsp_cgw_log(_message.Message):
    __slots__ = ("status", "log")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    LOG_FIELD_NUMBER: _ClassVar[int]
    status: int
    log: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_cgw_log]
    def __init__(self, status: _Optional[int] = ..., log: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_cgw_log, _Mapping]]] = ...) -> None: ...

class pbreq_gpvp_sync(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class pbrsp_gpvp_sync(_message.Message):
    __slots__ = ("team", "camp")
    TEAM_FIELD_NUMBER: _ClassVar[int]
    CAMP_FIELD_NUMBER: _ClassVar[int]
    team: _dr2_comm_pb_pb2.pb_gpvpteam
    camp: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_unit]
    def __init__(self, team: _Optional[_Union[_dr2_comm_pb_pb2.pb_gpvpteam, _Mapping]] = ..., camp: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_unit, _Mapping]]] = ...) -> None: ...

class pbreq_gpvp_set_camp(_message.Message):
    __slots__ = ("camp", "tid")
    CAMP_FIELD_NUMBER: _ClassVar[int]
    TID_FIELD_NUMBER: _ClassVar[int]
    camp: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_unit]
    tid: int
    def __init__(self, camp: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_unit, _Mapping]]] = ..., tid: _Optional[int] = ...) -> None: ...

class pbrsp_gpvp_set_camp(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_create_gpvpteam(_message.Message):
    __slots__ = ("name", "need_power")
    NAME_FIELD_NUMBER: _ClassVar[int]
    NEED_POWER_FIELD_NUMBER: _ClassVar[int]
    name: str
    need_power: int
    def __init__(self, name: _Optional[str] = ..., need_power: _Optional[int] = ...) -> None: ...

class pbrsp_create_gpvpteam(_message.Message):
    __slots__ = ("status", "id")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    status: int
    id: int
    def __init__(self, status: _Optional[int] = ..., id: _Optional[int] = ...) -> None: ...

class pbreq_dismiss_gpvpteam(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class pbrsp_dismiss_gpvpteam(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_gpvp_match(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class pbrsp_gpvp_match(_message.Message):
    __slots__ = ("teams",)
    TEAMS_FIELD_NUMBER: _ClassVar[int]
    teams: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_gpvpteam]
    def __init__(self, teams: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_gpvpteam, _Mapping]]] = ...) -> None: ...

class pbreq_submit_gpvpteam(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class pbrsp_submit_gpvpteam(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_gpvp_leaderop(_message.Message):
    __slots__ = ("type", "uid")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    type: int
    uid: int
    def __init__(self, type: _Optional[int] = ..., uid: _Optional[int] = ...) -> None: ...

class pbrsp_gpvp_leaderop(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_gpvp_friendslist(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class pbrsp_gpvp_friendslist(_message.Message):
    __slots__ = ("friends",)
    FRIENDS_FIELD_NUMBER: _ClassVar[int]
    friends: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_frd]
    def __init__(self, friends: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_frd, _Mapping]]] = ...) -> None: ...

class pbrsp_gpvpteam_notify(_message.Message):
    __slots__ = ("invited", "agree_invite", "leave", "apply", "agreed", "kicked", "submit", "dismiss", "owner")
    INVITED_FIELD_NUMBER: _ClassVar[int]
    AGREE_INVITE_FIELD_NUMBER: _ClassVar[int]
    LEAVE_FIELD_NUMBER: _ClassVar[int]
    APPLY_FIELD_NUMBER: _ClassVar[int]
    AGREED_FIELD_NUMBER: _ClassVar[int]
    KICKED_FIELD_NUMBER: _ClassVar[int]
    SUBMIT_FIELD_NUMBER: _ClassVar[int]
    DISMISS_FIELD_NUMBER: _ClassVar[int]
    OWNER_FIELD_NUMBER: _ClassVar[int]
    invited: int
    agree_invite: int
    leave: int
    apply: int
    agreed: int
    kicked: int
    submit: int
    dismiss: int
    owner: int
    def __init__(self, invited: _Optional[int] = ..., agree_invite: _Optional[int] = ..., leave: _Optional[int] = ..., apply: _Optional[int] = ..., agreed: _Optional[int] = ..., kicked: _Optional[int] = ..., submit: _Optional[int] = ..., dismiss: _Optional[int] = ..., owner: _Optional[int] = ...) -> None: ...

class pbreq_gpvp_invitelist(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class pbrsp_gpvp_invitelist(_message.Message):
    __slots__ = ("team",)
    TEAM_FIELD_NUMBER: _ClassVar[int]
    team: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_gpvpteam]
    def __init__(self, team: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_gpvpteam, _Mapping]]] = ...) -> None: ...

class pbreq_gpvp_refresh(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class pbrsp_gpvp_refresh(_message.Message):
    __slots__ = ("team",)
    TEAM_FIELD_NUMBER: _ClassVar[int]
    team: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_gpvpteam]
    def __init__(self, team: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_gpvpteam, _Mapping]]] = ...) -> None: ...

class pbreq_gpvp_mbrop(_message.Message):
    __slots__ = ("type", "teamid")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    TEAMID_FIELD_NUMBER: _ClassVar[int]
    type: int
    teamid: int
    def __init__(self, type: _Optional[int] = ..., teamid: _Optional[int] = ...) -> None: ...

class pbrsp_gpvp_mbrop(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_gpvp_ranklist(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class pbrsp_gpvp_ranklist(_message.Message):
    __slots__ = ("status", "team")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    TEAM_FIELD_NUMBER: _ClassVar[int]
    status: int
    team: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_gpvpteam]
    def __init__(self, status: _Optional[int] = ..., team: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_gpvpteam, _Mapping]]] = ...) -> None: ...

class pbreq_change_gpvpteam(_message.Message):
    __slots__ = ("team",)
    TEAM_FIELD_NUMBER: _ClassVar[int]
    team: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, team: _Optional[_Iterable[int]] = ...) -> None: ...

class pbrsp_change_gpvpteam(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_gpvp_applylist(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class pbrsp_gpvp_applylist(_message.Message):
    __slots__ = ("mbrs",)
    MBRS_FIELD_NUMBER: _ClassVar[int]
    mbrs: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_pmbr]
    def __init__(self, mbrs: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_pmbr, _Mapping]]] = ...) -> None: ...

class pbreq_gpvp_mbr(_message.Message):
    __slots__ = ("uid",)
    UID_FIELD_NUMBER: _ClassVar[int]
    uid: int
    def __init__(self, uid: _Optional[int] = ...) -> None: ...

class pbrsp_gpvp_mbr(_message.Message):
    __slots__ = ("status", "mbr")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MBR_FIELD_NUMBER: _ClassVar[int]
    status: int
    mbr: _dr2_comm_pb_pb2.pb_pmbr
    def __init__(self, status: _Optional[int] = ..., mbr: _Optional[_Union[_dr2_comm_pb_pb2.pb_pmbr, _Mapping]] = ...) -> None: ...

class pbreq_gpvp_grp(_message.Message):
    __slots__ = ("grp_id",)
    GRP_ID_FIELD_NUMBER: _ClassVar[int]
    grp_id: int
    def __init__(self, grp_id: _Optional[int] = ...) -> None: ...

class pbrsp_gpvp_grp(_message.Message):
    __slots__ = ("status", "grp")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    GRP_FIELD_NUMBER: _ClassVar[int]
    status: int
    grp: _dr2_comm_pb_pb2.pb_gpvpteam
    def __init__(self, status: _Optional[int] = ..., grp: _Optional[_Union[_dr2_comm_pb_pb2.pb_gpvpteam, _Mapping]] = ...) -> None: ...

class pbreq_gpvp_fight(_message.Message):
    __slots__ = ("grp_id",)
    GRP_ID_FIELD_NUMBER: _ClassVar[int]
    grp_id: int
    def __init__(self, grp_id: _Optional[int] = ...) -> None: ...

class pbrsp_gpvp_fight(_message.Message):
    __slots__ = ("status", "atk", "wins", "frames1", "frames2", "frames3", "hurts1", "hurts2", "hurts3", "ascore", "dscore", "adelta", "ddelta")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ATK_FIELD_NUMBER: _ClassVar[int]
    DEF_FIELD_NUMBER: _ClassVar[int]
    WINS_FIELD_NUMBER: _ClassVar[int]
    FRAMES1_FIELD_NUMBER: _ClassVar[int]
    FRAMES2_FIELD_NUMBER: _ClassVar[int]
    FRAMES3_FIELD_NUMBER: _ClassVar[int]
    HURTS1_FIELD_NUMBER: _ClassVar[int]
    HURTS2_FIELD_NUMBER: _ClassVar[int]
    HURTS3_FIELD_NUMBER: _ClassVar[int]
    ASCORE_FIELD_NUMBER: _ClassVar[int]
    DSCORE_FIELD_NUMBER: _ClassVar[int]
    ADELTA_FIELD_NUMBER: _ClassVar[int]
    DDELTA_FIELD_NUMBER: _ClassVar[int]
    status: int
    atk: _dr2_comm_pb_pb2.pb_gpvpteam
    wins: _containers.RepeatedScalarFieldContainer[bool]
    frames1: _containers.RepeatedScalarFieldContainer[bytes]
    frames2: _containers.RepeatedScalarFieldContainer[bytes]
    frames3: _containers.RepeatedScalarFieldContainer[bytes]
    hurts1: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_hurts]
    hurts2: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_hurts]
    hurts3: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_hurts]
    ascore: int
    dscore: int
    adelta: int
    ddelta: int
    def __init__(self, status: _Optional[int] = ..., atk: _Optional[_Union[_dr2_comm_pb_pb2.pb_gpvpteam, _Mapping]] = ..., wins: _Optional[_Iterable[bool]] = ..., frames1: _Optional[_Iterable[bytes]] = ..., frames2: _Optional[_Iterable[bytes]] = ..., frames3: _Optional[_Iterable[bytes]] = ..., hurts1: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_hurts, _Mapping]]] = ..., hurts2: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_hurts, _Mapping]]] = ..., hurts3: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_hurts, _Mapping]]] = ..., ascore: _Optional[int] = ..., dscore: _Optional[int] = ..., adelta: _Optional[int] = ..., ddelta: _Optional[int] = ..., **kwargs) -> None: ...

class pbreq_gpvp_logs(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class pbrsp_gpvp_logs(_message.Message):
    __slots__ = ("logs",)
    LOGS_FIELD_NUMBER: _ClassVar[int]
    logs: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_gpvplog]
    def __init__(self, logs: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_gpvplog, _Mapping]]] = ...) -> None: ...

class pbreq_gpvp_wlog(_message.Message):
    __slots__ = ("log_id",)
    LOG_ID_FIELD_NUMBER: _ClassVar[int]
    log_id: int
    def __init__(self, log_id: _Optional[int] = ...) -> None: ...

class pbrsp_gpvp_wlog(_message.Message):
    __slots__ = ("status", "log")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    LOG_FIELD_NUMBER: _ClassVar[int]
    status: int
    log: _dr2_comm_pb_pb2.pb_gpvp_wlog
    def __init__(self, status: _Optional[int] = ..., log: _Optional[_Union[_dr2_comm_pb_pb2.pb_gpvp_wlog, _Mapping]] = ...) -> None: ...

class pbreq_gpvp_video(_message.Message):
    __slots__ = ("vid",)
    VID_FIELD_NUMBER: _ClassVar[int]
    vid: int
    def __init__(self, vid: _Optional[int] = ...) -> None: ...

class pbrsp_gpvp_video(_message.Message):
    __slots__ = ("status", "frames", "hurts")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    FRAMES_FIELD_NUMBER: _ClassVar[int]
    HURTS_FIELD_NUMBER: _ClassVar[int]
    status: int
    frames: _containers.RepeatedScalarFieldContainer[bytes]
    hurts: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_hurts]
    def __init__(self, status: _Optional[int] = ..., frames: _Optional[_Iterable[bytes]] = ..., hurts: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_hurts, _Mapping]]] = ...) -> None: ...

class pbreq_pet_op(_message.Message):
    __slots__ = ("id", "opcode", "skl")
    ID_FIELD_NUMBER: _ClassVar[int]
    OPCODE_FIELD_NUMBER: _ClassVar[int]
    SKL_FIELD_NUMBER: _ClassVar[int]
    id: int
    opcode: int
    skl: int
    def __init__(self, id: _Optional[int] = ..., opcode: _Optional[int] = ..., skl: _Optional[int] = ...) -> None: ...

class pbrsp_pet_op(_message.Message):
    __slots__ = ("status", "reward")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    REWARD_FIELD_NUMBER: _ClassVar[int]
    status: int
    reward: _dr2_comm_pb_pb2.pb_bag
    def __init__(self, status: _Optional[int] = ..., reward: _Optional[_Union[_dr2_comm_pb_pb2.pb_bag, _Mapping]] = ...) -> None: ...

class pbreq_spk_sync(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class pbrsp_spk_sync(_message.Message):
    __slots__ = ("status", "cd", "camp", "estage", "ehpp", "seller", "wave", "sellers", "bufs", "qlt")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    CD_FIELD_NUMBER: _ClassVar[int]
    CAMP_FIELD_NUMBER: _ClassVar[int]
    ESTAGE_FIELD_NUMBER: _ClassVar[int]
    EHPP_FIELD_NUMBER: _ClassVar[int]
    SELLER_FIELD_NUMBER: _ClassVar[int]
    WAVE_FIELD_NUMBER: _ClassVar[int]
    SELLERS_FIELD_NUMBER: _ClassVar[int]
    BUFS_FIELD_NUMBER: _ClassVar[int]
    QLT_FIELD_NUMBER: _ClassVar[int]
    status: int
    cd: int
    camp: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_spkunit]
    estage: int
    ehpp: _containers.RepeatedScalarFieldContainer[int]
    seller: int
    wave: int
    sellers: _containers.RepeatedScalarFieldContainer[int]
    bufs: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_item]
    qlt: bool
    def __init__(self, status: _Optional[int] = ..., cd: _Optional[int] = ..., camp: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_spkunit, _Mapping]]] = ..., estage: _Optional[int] = ..., ehpp: _Optional[_Iterable[int]] = ..., seller: _Optional[int] = ..., wave: _Optional[int] = ..., sellers: _Optional[_Iterable[int]] = ..., bufs: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_item, _Mapping]]] = ..., qlt: _Optional[bool] = ...) -> None: ...

class pbreq_spk_camp(_message.Message):
    __slots__ = ("hids",)
    HIDS_FIELD_NUMBER: _ClassVar[int]
    hids: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, hids: _Optional[_Iterable[int]] = ...) -> None: ...

class pbrsp_spk_camp(_message.Message):
    __slots__ = ("status", "nstage", "wave", "bufs", "sellers", "reward")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    NSTAGE_FIELD_NUMBER: _ClassVar[int]
    WAVE_FIELD_NUMBER: _ClassVar[int]
    BUFS_FIELD_NUMBER: _ClassVar[int]
    SELLERS_FIELD_NUMBER: _ClassVar[int]
    REWARD_FIELD_NUMBER: _ClassVar[int]
    status: int
    nstage: int
    wave: int
    bufs: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_item]
    sellers: _containers.RepeatedScalarFieldContainer[int]
    reward: _dr2_comm_pb_pb2.pb_bag
    def __init__(self, status: _Optional[int] = ..., nstage: _Optional[int] = ..., wave: _Optional[int] = ..., bufs: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_item, _Mapping]]] = ..., sellers: _Optional[_Iterable[int]] = ..., reward: _Optional[_Union[_dr2_comm_pb_pb2.pb_bag, _Mapping]] = ...) -> None: ...

class pbreq_spk_fight(_message.Message):
    __slots__ = ("hid",)
    HID_FIELD_NUMBER: _ClassVar[int]
    hid: int
    def __init__(self, hid: _Optional[int] = ...) -> None: ...

class pbrsp_spk_fight(_message.Message):
    __slots__ = ("status", "win", "frames", "mhpp", "menergy", "ehpp", "reward", "buf", "seller", "nstage", "qlt")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    WIN_FIELD_NUMBER: _ClassVar[int]
    FRAMES_FIELD_NUMBER: _ClassVar[int]
    MHPP_FIELD_NUMBER: _ClassVar[int]
    MENERGY_FIELD_NUMBER: _ClassVar[int]
    EHPP_FIELD_NUMBER: _ClassVar[int]
    REWARD_FIELD_NUMBER: _ClassVar[int]
    BUF_FIELD_NUMBER: _ClassVar[int]
    SELLER_FIELD_NUMBER: _ClassVar[int]
    NSTAGE_FIELD_NUMBER: _ClassVar[int]
    QLT_FIELD_NUMBER: _ClassVar[int]
    status: int
    win: bool
    frames: _containers.RepeatedScalarFieldContainer[bytes]
    mhpp: int
    menergy: int
    ehpp: _containers.RepeatedScalarFieldContainer[int]
    reward: _dr2_comm_pb_pb2.pb_bag
    buf: int
    seller: int
    nstage: int
    qlt: bool
    def __init__(self, status: _Optional[int] = ..., win: _Optional[bool] = ..., frames: _Optional[_Iterable[bytes]] = ..., mhpp: _Optional[int] = ..., menergy: _Optional[int] = ..., ehpp: _Optional[_Iterable[int]] = ..., reward: _Optional[_Union[_dr2_comm_pb_pb2.pb_bag, _Mapping]] = ..., buf: _Optional[int] = ..., seller: _Optional[int] = ..., nstage: _Optional[int] = ..., qlt: _Optional[bool] = ...) -> None: ...

class pbreq_spk_buf(_message.Message):
    __slots__ = ("buf", "hid", "save")
    BUF_FIELD_NUMBER: _ClassVar[int]
    HID_FIELD_NUMBER: _ClassVar[int]
    SAVE_FIELD_NUMBER: _ClassVar[int]
    buf: int
    hid: int
    save: int
    def __init__(self, buf: _Optional[int] = ..., hid: _Optional[int] = ..., save: _Optional[int] = ...) -> None: ...

class pbrsp_spk_buf(_message.Message):
    __slots__ = ("status", "nstage")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    NSTAGE_FIELD_NUMBER: _ClassVar[int]
    status: int
    nstage: int
    def __init__(self, status: _Optional[int] = ..., nstage: _Optional[int] = ...) -> None: ...

class pbreq_spk_rank(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class pbrsp_spk_rank(_message.Message):
    __slots__ = ("rank", "mbr", "wave", "time")
    RANK_FIELD_NUMBER: _ClassVar[int]
    MBR_FIELD_NUMBER: _ClassVar[int]
    WAVE_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    rank: int
    mbr: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_spkmbr]
    wave: int
    time: int
    def __init__(self, rank: _Optional[int] = ..., mbr: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_spkmbr, _Mapping]]] = ..., wave: _Optional[int] = ..., time: _Optional[int] = ...) -> None: ...

class pbreq_spk_buy(_message.Message):
    __slots__ = ("id", "count", "skip", "variety")
    ID_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    SKIP_FIELD_NUMBER: _ClassVar[int]
    VARIETY_FIELD_NUMBER: _ClassVar[int]
    id: int
    count: int
    skip: int
    variety: int
    def __init__(self, id: _Optional[int] = ..., count: _Optional[int] = ..., skip: _Optional[int] = ..., variety: _Optional[int] = ...) -> None: ...

class pbrsp_spk_buy(_message.Message):
    __slots__ = ("status", "nstage")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    NSTAGE_FIELD_NUMBER: _ClassVar[int]
    status: int
    nstage: int
    def __init__(self, status: _Optional[int] = ..., nstage: _Optional[int] = ...) -> None: ...

class pbreq_spk_save(_message.Message):
    __slots__ = ("buf",)
    BUF_FIELD_NUMBER: _ClassVar[int]
    buf: int
    def __init__(self, buf: _Optional[int] = ...) -> None: ...

class pbrsp_spk_save(_message.Message):
    __slots__ = ("status", "nstage")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    NSTAGE_FIELD_NUMBER: _ClassVar[int]
    status: int
    nstage: int
    def __init__(self, status: _Optional[int] = ..., nstage: _Optional[int] = ...) -> None: ...

class pbreq_bboss_syn(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class pbrsp_bboss_syn(_message.Message):
    __slots__ = ("status", "id", "hp")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    HP_FIELD_NUMBER: _ClassVar[int]
    status: int
    id: int
    hp: int
    def __init__(self, status: _Optional[int] = ..., id: _Optional[int] = ..., hp: _Optional[int] = ...) -> None: ...

class pbreq_bboss_buy(_message.Message):
    __slots__ = ("num",)
    NUM_FIELD_NUMBER: _ClassVar[int]
    num: int
    def __init__(self, num: _Optional[int] = ...) -> None: ...

class pbrsp_bboss_buy(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_bboss_fight(_message.Message):
    __slots__ = ("camp", "id", "tid")
    CAMP_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    TID_FIELD_NUMBER: _ClassVar[int]
    camp: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_unit]
    id: int
    tid: int
    def __init__(self, camp: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_unit, _Mapping]]] = ..., id: _Optional[int] = ..., tid: _Optional[int] = ...) -> None: ...

class pbrsp_bboss_fight(_message.Message):
    __slots__ = ("status", "win", "frames", "hpps", "rewards", "hurts", "select")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    WIN_FIELD_NUMBER: _ClassVar[int]
    FRAMES_FIELD_NUMBER: _ClassVar[int]
    HPPS_FIELD_NUMBER: _ClassVar[int]
    REWARDS_FIELD_NUMBER: _ClassVar[int]
    HURTS_FIELD_NUMBER: _ClassVar[int]
    SELECT_FIELD_NUMBER: _ClassVar[int]
    status: int
    win: bool
    frames: _containers.RepeatedScalarFieldContainer[bytes]
    hpps: _containers.RepeatedScalarFieldContainer[int]
    rewards: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_bag]
    hurts: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_hurts]
    select: int
    def __init__(self, status: _Optional[int] = ..., win: _Optional[bool] = ..., frames: _Optional[_Iterable[bytes]] = ..., hpps: _Optional[_Iterable[int]] = ..., rewards: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_bag, _Mapping]]] = ..., hurts: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_hurts, _Mapping]]] = ..., select: _Optional[int] = ...) -> None: ...

class pbreq_bboss_batch(_message.Message):
    __slots__ = ("camp", "id", "num", "tid")
    CAMP_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NUM_FIELD_NUMBER: _ClassVar[int]
    TID_FIELD_NUMBER: _ClassVar[int]
    camp: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_unit]
    id: int
    num: int
    tid: int
    def __init__(self, camp: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_unit, _Mapping]]] = ..., id: _Optional[int] = ..., num: _Optional[int] = ..., tid: _Optional[int] = ...) -> None: ...

class pbrsp_bboss_batch(_message.Message):
    __slots__ = ("status", "win", "hpps", "reward", "num")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    WIN_FIELD_NUMBER: _ClassVar[int]
    HPPS_FIELD_NUMBER: _ClassVar[int]
    REWARD_FIELD_NUMBER: _ClassVar[int]
    NUM_FIELD_NUMBER: _ClassVar[int]
    status: int
    win: bool
    hpps: _containers.RepeatedScalarFieldContainer[int]
    reward: _dr2_comm_pb_pb2.pb_bag
    num: int
    def __init__(self, status: _Optional[int] = ..., win: _Optional[bool] = ..., hpps: _Optional[_Iterable[int]] = ..., reward: _Optional[_Union[_dr2_comm_pb_pb2.pb_bag, _Mapping]] = ..., num: _Optional[int] = ...) -> None: ...

class pbreq_iboat_sync(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class pbrsp_iboat_sync(_message.Message):
    __slots__ = ("status", "adt", "rts", "boat", "camp", "reward", "evtids", "num")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ADT_FIELD_NUMBER: _ClassVar[int]
    RTS_FIELD_NUMBER: _ClassVar[int]
    BOAT_FIELD_NUMBER: _ClassVar[int]
    CAMP_FIELD_NUMBER: _ClassVar[int]
    REWARD_FIELD_NUMBER: _ClassVar[int]
    EVTIDS_FIELD_NUMBER: _ClassVar[int]
    NUM_FIELD_NUMBER: _ClassVar[int]
    status: int
    adt: _dr2_comm_pb_pb2.pb_iadt
    rts: _containers.RepeatedScalarFieldContainer[int]
    boat: _dr2_comm_pb_pb2.pb_iboat
    camp: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_unit]
    reward: _dr2_comm_pb_pb2.pb_bag
    evtids: _containers.RepeatedScalarFieldContainer[int]
    num: int
    def __init__(self, status: _Optional[int] = ..., adt: _Optional[_Union[_dr2_comm_pb_pb2.pb_iadt, _Mapping]] = ..., rts: _Optional[_Iterable[int]] = ..., boat: _Optional[_Union[_dr2_comm_pb_pb2.pb_iboat, _Mapping]] = ..., camp: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_unit, _Mapping]]] = ..., reward: _Optional[_Union[_dr2_comm_pb_pb2.pb_bag, _Mapping]] = ..., evtids: _Optional[_Iterable[int]] = ..., num: _Optional[int] = ...) -> None: ...

class pbreq_iboat_start(_message.Message):
    __slots__ = ("rt", "camp")
    RT_FIELD_NUMBER: _ClassVar[int]
    CAMP_FIELD_NUMBER: _ClassVar[int]
    rt: int
    camp: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_unit]
    def __init__(self, rt: _Optional[int] = ..., camp: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_unit, _Mapping]]] = ...) -> None: ...

class pbrsp_iboat_start(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_iboat_xp(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class pbrsp_iboat_xp(_message.Message):
    __slots__ = ("status", "mevt", "item")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MEVT_FIELD_NUMBER: _ClassVar[int]
    ITEM_FIELD_NUMBER: _ClassVar[int]
    status: int
    mevt: _dr2_comm_pb_pb2.pb_ievent
    item: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, status: _Optional[int] = ..., mevt: _Optional[_Union[_dr2_comm_pb_pb2.pb_ievent, _Mapping]] = ..., item: _Optional[_Iterable[int]] = ...) -> None: ...

class pbreq_iboat_xpop(_message.Message):
    __slots__ = ("type", "camp", "atkid", "tid")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    CAMP_FIELD_NUMBER: _ClassVar[int]
    ATKID_FIELD_NUMBER: _ClassVar[int]
    TID_FIELD_NUMBER: _ClassVar[int]
    type: int
    camp: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_unit]
    atkid: int
    tid: int
    def __init__(self, type: _Optional[int] = ..., camp: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_unit, _Mapping]]] = ..., atkid: _Optional[int] = ..., tid: _Optional[int] = ...) -> None: ...

class pbrsp_iboat_xpop(_message.Message):
    __slots__ = ("status", "reward", "video")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    REWARD_FIELD_NUMBER: _ClassVar[int]
    VIDEO_FIELD_NUMBER: _ClassVar[int]
    status: int
    reward: _dr2_comm_pb_pb2.pb_bag
    video: _dr2_comm_pb_pb2.pb_pvideo
    def __init__(self, status: _Optional[int] = ..., reward: _Optional[_Union[_dr2_comm_pb_pb2.pb_bag, _Mapping]] = ..., video: _Optional[_Union[_dr2_comm_pb_pb2.pb_pvideo, _Mapping]] = ...) -> None: ...

class pbreq_iboat_shop(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class pbrsp_iboat_shop(_message.Message):
    __slots__ = ("status", "good")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    GOOD_FIELD_NUMBER: _ClassVar[int]
    status: int
    good: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_good]
    def __init__(self, status: _Optional[int] = ..., good: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_good, _Mapping]]] = ...) -> None: ...

class pbreq_iboat_buy(_message.Message):
    __slots__ = ("id", "num")
    ID_FIELD_NUMBER: _ClassVar[int]
    NUM_FIELD_NUMBER: _ClassVar[int]
    id: int
    num: int
    def __init__(self, id: _Optional[int] = ..., num: _Optional[int] = ...) -> None: ...

class pbrsp_iboat_buy(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_iboat_arm(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class pbrsp_iboat_arm(_message.Message):
    __slots__ = ("status", "arm")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ARM_FIELD_NUMBER: _ClassVar[int]
    status: int
    arm: int
    def __init__(self, status: _Optional[int] = ..., arm: _Optional[int] = ...) -> None: ...

class pbreq_iboat_skl(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class pbrsp_iboat_skl(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_iboat_name(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class pbrsp_iboat_name(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_iboat_fsync(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class pbrsp_iboat_fsync(_message.Message):
    __slots__ = ("status", "info")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    INFO_FIELD_NUMBER: _ClassVar[int]
    status: int
    info: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_ipro]
    def __init__(self, status: _Optional[int] = ..., info: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_ipro, _Mapping]]] = ...) -> None: ...

class pbreq_iboat_fpro(_message.Message):
    __slots__ = ("id", "num")
    ID_FIELD_NUMBER: _ClassVar[int]
    NUM_FIELD_NUMBER: _ClassVar[int]
    id: int
    num: int
    def __init__(self, id: _Optional[int] = ..., num: _Optional[int] = ...) -> None: ...

class pbrsp_iboat_fpro(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_iboat_use(_message.Message):
    __slots__ = ("id", "num")
    ID_FIELD_NUMBER: _ClassVar[int]
    NUM_FIELD_NUMBER: _ClassVar[int]
    id: int
    num: int
    def __init__(self, id: _Optional[int] = ..., num: _Optional[int] = ...) -> None: ...

class pbrsp_iboat_use(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_live_sync(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class pbrsp_live_sync(_message.Message):
    __slots__ = ("status", "exps", "lands", "bag")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    EXPS_FIELD_NUMBER: _ClassVar[int]
    LANDS_FIELD_NUMBER: _ClassVar[int]
    BAG_FIELD_NUMBER: _ClassVar[int]
    status: int
    exps: _containers.RepeatedScalarFieldContainer[int]
    lands: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_home_land]
    bag: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_item]
    def __init__(self, status: _Optional[int] = ..., exps: _Optional[_Iterable[int]] = ..., lands: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_home_land, _Mapping]]] = ..., bag: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_item, _Mapping]]] = ...) -> None: ...

class pbreq_op_block(_message.Message):
    __slots__ = ("land_id", "operations")
    LAND_ID_FIELD_NUMBER: _ClassVar[int]
    OPERATIONS_FIELD_NUMBER: _ClassVar[int]
    land_id: int
    operations: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_block]
    def __init__(self, land_id: _Optional[int] = ..., operations: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_block, _Mapping]]] = ...) -> None: ...

class pbrsp_op_block(_message.Message):
    __slots__ = ("status", "reward")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    REWARD_FIELD_NUMBER: _ClassVar[int]
    status: int
    reward: _dr2_comm_pb_pb2.pb_bag
    def __init__(self, status: _Optional[int] = ..., reward: _Optional[_Union[_dr2_comm_pb_pb2.pb_bag, _Mapping]] = ...) -> None: ...

class pbreq_op_build(_message.Message):
    __slots__ = ("land_id", "type", "pos", "skin", "name", "id")
    LAND_ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    POS_FIELD_NUMBER: _ClassVar[int]
    SKIN_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    land_id: int
    type: int
    pos: int
    skin: int
    name: str
    id: int
    def __init__(self, land_id: _Optional[int] = ..., type: _Optional[int] = ..., pos: _Optional[int] = ..., skin: _Optional[int] = ..., name: _Optional[str] = ..., id: _Optional[int] = ...) -> None: ...

class pbrsp_op_build(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_living(_message.Message):
    __slots__ = ("land_id", "live")
    LAND_ID_FIELD_NUMBER: _ClassVar[int]
    LIVE_FIELD_NUMBER: _ClassVar[int]
    land_id: int
    live: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_living]
    def __init__(self, land_id: _Optional[int] = ..., live: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_living, _Mapping]]] = ...) -> None: ...

class pbrsp_living(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_sync_buildings(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class pbrsp_sync_buildings(_message.Message):
    __slots__ = ("status", "buildings", "skin", "skill", "stove", "coll", "like", "tasks", "flag", "care", "stove_buy")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    BUILDINGS_FIELD_NUMBER: _ClassVar[int]
    SKIN_FIELD_NUMBER: _ClassVar[int]
    SKILL_FIELD_NUMBER: _ClassVar[int]
    STOVE_FIELD_NUMBER: _ClassVar[int]
    COLL_FIELD_NUMBER: _ClassVar[int]
    LIKE_FIELD_NUMBER: _ClassVar[int]
    TASKS_FIELD_NUMBER: _ClassVar[int]
    FLAG_FIELD_NUMBER: _ClassVar[int]
    CARE_FIELD_NUMBER: _ClassVar[int]
    STOVE_BUY_FIELD_NUMBER: _ClassVar[int]
    status: int
    buildings: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_buildings]
    skin: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_item]
    skill: _containers.RepeatedScalarFieldContainer[int]
    stove: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_stove]
    coll: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_coll]
    like: int
    tasks: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_task]
    flag: int
    care: int
    stove_buy: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_stove_buy]
    def __init__(self, status: _Optional[int] = ..., buildings: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_buildings, _Mapping]]] = ..., skin: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_item, _Mapping]]] = ..., skill: _Optional[_Iterable[int]] = ..., stove: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_stove, _Mapping]]] = ..., coll: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_coll, _Mapping]]] = ..., like: _Optional[int] = ..., tasks: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_task, _Mapping]]] = ..., flag: _Optional[int] = ..., care: _Optional[int] = ..., stove_buy: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_stove_buy, _Mapping]]] = ...) -> None: ...

class pbreq_hland_build(_message.Message):
    __slots__ = ("operations",)
    OPERATIONS_FIELD_NUMBER: _ClassVar[int]
    operations: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_block]
    def __init__(self, operations: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_block, _Mapping]]] = ...) -> None: ...

class pbrsp_hland_build(_message.Message):
    __slots__ = ("status", "reward", "score")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    REWARD_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    status: int
    reward: _dr2_comm_pb_pb2.pb_bag
    score: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_coll]
    def __init__(self, status: _Optional[int] = ..., reward: _Optional[_Union[_dr2_comm_pb_pb2.pb_bag, _Mapping]] = ..., score: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_coll, _Mapping]]] = ...) -> None: ...

class pbreq_building_up(_message.Message):
    __slots__ = ("pos",)
    POS_FIELD_NUMBER: _ClassVar[int]
    pos: int
    def __init__(self, pos: _Optional[int] = ...) -> None: ...

class pbrsp_building_up(_message.Message):
    __slots__ = ("status", "stove")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    STOVE_FIELD_NUMBER: _ClassVar[int]
    status: int
    stove: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_stove]
    def __init__(self, status: _Optional[int] = ..., stove: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_stove, _Mapping]]] = ...) -> None: ...

class pbreq_building_change_skin(_message.Message):
    __slots__ = ("change",)
    CHANGE_FIELD_NUMBER: _ClassVar[int]
    change: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.hland_change_skin]
    def __init__(self, change: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.hland_change_skin, _Mapping]]] = ...) -> None: ...

class pbrsp_building_change_skin(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_fun_collect(_message.Message):
    __slots__ = ("pos", "idx")
    POS_FIELD_NUMBER: _ClassVar[int]
    IDX_FIELD_NUMBER: _ClassVar[int]
    pos: _containers.RepeatedScalarFieldContainer[int]
    idx: int
    def __init__(self, pos: _Optional[_Iterable[int]] = ..., idx: _Optional[int] = ...) -> None: ...

class pbrsp_fun_collect(_message.Message):
    __slots__ = ("status", "reward")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    REWARD_FIELD_NUMBER: _ClassVar[int]
    status: int
    reward: _dr2_comm_pb_pb2.pb_bag
    def __init__(self, status: _Optional[int] = ..., reward: _Optional[_Union[_dr2_comm_pb_pb2.pb_bag, _Mapping]] = ...) -> None: ...

class pbreq_fun_up_skill(_message.Message):
    __slots__ = ("skill",)
    SKILL_FIELD_NUMBER: _ClassVar[int]
    skill: int
    def __init__(self, skill: _Optional[int] = ...) -> None: ...

class pbrsp_fun_up_skill(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_open_land(_message.Message):
    __slots__ = ("mapid",)
    MAPID_FIELD_NUMBER: _ClassVar[int]
    mapid: int
    def __init__(self, mapid: _Optional[int] = ...) -> None: ...

class pbrsp_open_land(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_stove_harvest(_message.Message):
    __slots__ = ("pos",)
    POS_FIELD_NUMBER: _ClassVar[int]
    pos: int
    def __init__(self, pos: _Optional[int] = ...) -> None: ...

class pbrsp_stove_harvest(_message.Message):
    __slots__ = ("status", "reward")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    REWARD_FIELD_NUMBER: _ClassVar[int]
    status: int
    reward: _dr2_comm_pb_pb2.pb_bag
    def __init__(self, status: _Optional[int] = ..., reward: _Optional[_Union[_dr2_comm_pb_pb2.pb_bag, _Mapping]] = ...) -> None: ...

class pbrsp_collect_notify(_message.Message):
    __slots__ = ("info",)
    INFO_FIELD_NUMBER: _ClassVar[int]
    info: _dr2_comm_pb_pb2.pb_coll
    def __init__(self, info: _Optional[_Union[_dr2_comm_pb_pb2.pb_coll, _Mapping]] = ...) -> None: ...

class pbreq_collect_rank(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class pbrsp_collect_rank(_message.Message):
    __slots__ = ("status", "mbrs")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MBRS_FIELD_NUMBER: _ClassVar[int]
    status: int
    mbrs: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_smbrs]
    def __init__(self, status: _Optional[int] = ..., mbrs: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_smbrs, _Mapping]]] = ...) -> None: ...

class pbreq_collect_lv(_message.Message):
    __slots__ = ("id", "lv")
    ID_FIELD_NUMBER: _ClassVar[int]
    LV_FIELD_NUMBER: _ClassVar[int]
    id: int
    lv: int
    def __init__(self, id: _Optional[int] = ..., lv: _Optional[int] = ...) -> None: ...

class pbrsp_collect_lv(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_stove_buy(_message.Message):
    __slots__ = ("id", "pos", "num")
    ID_FIELD_NUMBER: _ClassVar[int]
    POS_FIELD_NUMBER: _ClassVar[int]
    NUM_FIELD_NUMBER: _ClassVar[int]
    id: int
    pos: int
    num: int
    def __init__(self, id: _Optional[int] = ..., pos: _Optional[int] = ..., num: _Optional[int] = ...) -> None: ...

class pbrsp_stove_buy(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_reset_skill(_message.Message):
    __slots__ = ("pos",)
    POS_FIELD_NUMBER: _ClassVar[int]
    pos: int
    def __init__(self, pos: _Optional[int] = ...) -> None: ...

class pbrsp_reset_skill(_message.Message):
    __slots__ = ("status", "rewards")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    REWARDS_FIELD_NUMBER: _ClassVar[int]
    status: int
    rewards: _dr2_comm_pb_pb2.pb_bag
    def __init__(self, status: _Optional[int] = ..., rewards: _Optional[_Union[_dr2_comm_pb_pb2.pb_bag, _Mapping]] = ...) -> None: ...

class pbreq_hland_visit(_message.Message):
    __slots__ = ("uid",)
    UID_FIELD_NUMBER: _ClassVar[int]
    uid: int
    def __init__(self, uid: _Optional[int] = ...) -> None: ...

class pbrsp_hland_visit(_message.Message):
    __slots__ = ("status", "flag", "buildings", "skill", "coll", "bag", "exps", "lands", "like")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    FLAG_FIELD_NUMBER: _ClassVar[int]
    BUILDINGS_FIELD_NUMBER: _ClassVar[int]
    SKILL_FIELD_NUMBER: _ClassVar[int]
    COLL_FIELD_NUMBER: _ClassVar[int]
    BAG_FIELD_NUMBER: _ClassVar[int]
    EXPS_FIELD_NUMBER: _ClassVar[int]
    LANDS_FIELD_NUMBER: _ClassVar[int]
    LIKE_FIELD_NUMBER: _ClassVar[int]
    status: int
    flag: int
    buildings: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_buildings]
    skill: _containers.RepeatedScalarFieldContainer[int]
    coll: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_coll]
    bag: _dr2_comm_pb_pb2.pb_bag
    exps: _containers.RepeatedScalarFieldContainer[int]
    lands: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_home_land]
    like: int
    def __init__(self, status: _Optional[int] = ..., flag: _Optional[int] = ..., buildings: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_buildings, _Mapping]]] = ..., skill: _Optional[_Iterable[int]] = ..., coll: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_coll, _Mapping]]] = ..., bag: _Optional[_Union[_dr2_comm_pb_pb2.pb_bag, _Mapping]] = ..., exps: _Optional[_Iterable[int]] = ..., lands: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_home_land, _Mapping]]] = ..., like: _Optional[int] = ...) -> None: ...

class pbreq_hland_search(_message.Message):
    __slots__ = ("uid",)
    UID_FIELD_NUMBER: _ClassVar[int]
    uid: int
    def __init__(self, uid: _Optional[int] = ...) -> None: ...

class pbrsp_hland_search(_message.Message):
    __slots__ = ("status", "info")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    INFO_FIELD_NUMBER: _ClassVar[int]
    status: int
    info: _dr2_comm_pb_pb2.pb_smbr
    def __init__(self, status: _Optional[int] = ..., info: _Optional[_Union[_dr2_comm_pb_pb2.pb_smbr, _Mapping]] = ...) -> None: ...

class pbreq_hland_rec(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class pbrsp_hland_rec(_message.Message):
    __slots__ = ("status", "rewards")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    REWARDS_FIELD_NUMBER: _ClassVar[int]
    status: int
    rewards: _dr2_comm_pb_pb2.pb_bag
    def __init__(self, status: _Optional[int] = ..., rewards: _Optional[_Union[_dr2_comm_pb_pb2.pb_bag, _Mapping]] = ...) -> None: ...

class pbreq_hland_like(_message.Message):
    __slots__ = ("uid", "type")
    UID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    uid: int
    type: int
    def __init__(self, uid: _Optional[int] = ..., type: _Optional[int] = ...) -> None: ...

class pbrsp_hland_like(_message.Message):
    __slots__ = ("status", "rewards")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    REWARDS_FIELD_NUMBER: _ClassVar[int]
    status: int
    rewards: _dr2_comm_pb_pb2.pb_bag
    def __init__(self, status: _Optional[int] = ..., rewards: _Optional[_Union[_dr2_comm_pb_pb2.pb_bag, _Mapping]] = ...) -> None: ...

class pbreq_hland_rank(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class pbrsp_hland_rank(_message.Message):
    __slots__ = ("status", "mbrs")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MBRS_FIELD_NUMBER: _ClassVar[int]
    status: int
    mbrs: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_smbrs]
    def __init__(self, status: _Optional[int] = ..., mbrs: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_smbrs, _Mapping]]] = ...) -> None: ...

class pbreq_hland_log(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class pbrsp_hland_log(_message.Message):
    __slots__ = ("status", "log")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    LOG_FIELD_NUMBER: _ClassVar[int]
    status: int
    log: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_hland_log]
    def __init__(self, status: _Optional[int] = ..., log: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_hland_log, _Mapping]]] = ...) -> None: ...

class pbreq_hland_template_sync(_message.Message):
    __slots__ = ("type",)
    TYPE_FIELD_NUMBER: _ClassVar[int]
    type: int
    def __init__(self, type: _Optional[int] = ...) -> None: ...

class pbrsp_hland_template_sync(_message.Message):
    __slots__ = ("status", "template")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    status: int
    template: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_template]
    def __init__(self, status: _Optional[int] = ..., template: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_template, _Mapping]]] = ...) -> None: ...

class pbreq_hland_template_save(_message.Message):
    __slots__ = ("my", "type", "id", "land_id")
    MY_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    LAND_ID_FIELD_NUMBER: _ClassVar[int]
    my: int
    type: int
    id: int
    land_id: int
    def __init__(self, my: _Optional[int] = ..., type: _Optional[int] = ..., id: _Optional[int] = ..., land_id: _Optional[int] = ...) -> None: ...

class pbrsp_hland_template_save(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_hland_template_rename(_message.Message):
    __slots__ = ("type", "id", "name")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    type: int
    id: int
    name: str
    def __init__(self, type: _Optional[int] = ..., id: _Optional[int] = ..., name: _Optional[str] = ...) -> None: ...

class pbrsp_hland_template_rename(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_hland_template_use(_message.Message):
    __slots__ = ("id", "land_id")
    ID_FIELD_NUMBER: _ClassVar[int]
    LAND_ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    land_id: int
    def __init__(self, id: _Optional[int] = ..., land_id: _Optional[int] = ...) -> None: ...

class pbrsp_hland_template_use(_message.Message):
    __slots__ = ("status", "bag", "exps", "lands")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    BAG_FIELD_NUMBER: _ClassVar[int]
    EXPS_FIELD_NUMBER: _ClassVar[int]
    LANDS_FIELD_NUMBER: _ClassVar[int]
    status: int
    bag: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_item]
    exps: _containers.RepeatedScalarFieldContainer[int]
    lands: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_home_land]
    def __init__(self, status: _Optional[int] = ..., bag: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_item, _Mapping]]] = ..., exps: _Optional[_Iterable[int]] = ..., lands: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_home_land, _Mapping]]] = ...) -> None: ...

class pbreq_hland_visible(_message.Message):
    __slots__ = ("flag",)
    FLAG_FIELD_NUMBER: _ClassVar[int]
    flag: int
    def __init__(self, flag: _Optional[int] = ...) -> None: ...

class pbrsp_hland_visible(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_hland_recmd(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class pbrsp_hland_recmd(_message.Message):
    __slots__ = ("status", "recmd")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    RECMD_FIELD_NUMBER: _ClassVar[int]
    status: int
    recmd: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_frd]
    def __init__(self, status: _Optional[int] = ..., recmd: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_frd, _Mapping]]] = ...) -> None: ...

class pbreq_hteam_sync(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class pbrsp_hteam_sync(_message.Message):
    __slots__ = ("status", "bag", "teams", "invite", "mbrs", "reward")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    BAG_FIELD_NUMBER: _ClassVar[int]
    TEAMS_FIELD_NUMBER: _ClassVar[int]
    INVITE_FIELD_NUMBER: _ClassVar[int]
    MBRS_FIELD_NUMBER: _ClassVar[int]
    REWARD_FIELD_NUMBER: _ClassVar[int]
    status: int
    bag: _containers.RepeatedScalarFieldContainer[int]
    teams: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_hteam]
    invite: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_hteam]
    mbrs: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_hmbr]
    reward: _dr2_comm_pb_pb2.pb_bag
    def __init__(self, status: _Optional[int] = ..., bag: _Optional[_Iterable[int]] = ..., teams: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_hteam, _Mapping]]] = ..., invite: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_hteam, _Mapping]]] = ..., mbrs: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_hmbr, _Mapping]]] = ..., reward: _Optional[_Union[_dr2_comm_pb_pb2.pb_bag, _Mapping]] = ...) -> None: ...

class pbreq_refresh_hteam(_message.Message):
    __slots__ = ("type",)
    TYPE_FIELD_NUMBER: _ClassVar[int]
    type: int
    def __init__(self, type: _Optional[int] = ...) -> None: ...

class pbrsp_refresh_hteam(_message.Message):
    __slots__ = ("status", "hteam1", "hteam2")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    HTEAM1_FIELD_NUMBER: _ClassVar[int]
    HTEAM2_FIELD_NUMBER: _ClassVar[int]
    status: int
    hteam1: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_hteam]
    hteam2: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_hteam]
    def __init__(self, status: _Optional[int] = ..., hteam1: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_hteam, _Mapping]]] = ..., hteam2: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_hteam, _Mapping]]] = ...) -> None: ...

class pbreq_create_hteam(_message.Message):
    __slots__ = ("type", "item_ids")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ITEM_IDS_FIELD_NUMBER: _ClassVar[int]
    type: int
    item_ids: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, type: _Optional[int] = ..., item_ids: _Optional[_Iterable[int]] = ...) -> None: ...

class pbrsp_create_hteam(_message.Message):
    __slots__ = ("status", "id")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    status: int
    id: str
    def __init__(self, status: _Optional[int] = ..., id: _Optional[str] = ...) -> None: ...

class pbreq_dismiss_hteam(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class pbrsp_dismiss_hteam(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_join_hteam(_message.Message):
    __slots__ = ("id", "item_ids", "type")
    ID_FIELD_NUMBER: _ClassVar[int]
    ITEM_IDS_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    id: str
    item_ids: _containers.RepeatedScalarFieldContainer[int]
    type: int
    def __init__(self, id: _Optional[str] = ..., item_ids: _Optional[_Iterable[int]] = ..., type: _Optional[int] = ...) -> None: ...

class pbrsp_join_hteam(_message.Message):
    __slots__ = ("status", "hteam")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    HTEAM_FIELD_NUMBER: _ClassVar[int]
    status: int
    hteam: _dr2_comm_pb_pb2.pb_hteam
    def __init__(self, status: _Optional[int] = ..., hteam: _Optional[_Union[_dr2_comm_pb_pb2.pb_hteam, _Mapping]] = ...) -> None: ...

class pbreq_bjoin_hteam(_message.Message):
    __slots__ = ("id", "type", "item_ids")
    ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ITEM_IDS_FIELD_NUMBER: _ClassVar[int]
    id: _containers.RepeatedScalarFieldContainer[str]
    type: _containers.RepeatedScalarFieldContainer[int]
    item_ids: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, id: _Optional[_Iterable[str]] = ..., type: _Optional[_Iterable[int]] = ..., item_ids: _Optional[_Iterable[int]] = ...) -> None: ...

class pbrsp_bjoin_hteam(_message.Message):
    __slots__ = ("status", "hteam")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    HTEAM_FIELD_NUMBER: _ClassVar[int]
    status: int
    hteam: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_hteam]
    def __init__(self, status: _Optional[int] = ..., hteam: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_hteam, _Mapping]]] = ...) -> None: ...

class pbreq_quit_hteam(_message.Message):
    __slots__ = ("id", "uid")
    ID_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    id: str
    uid: int
    def __init__(self, id: _Optional[str] = ..., uid: _Optional[int] = ...) -> None: ...

class pbrsp_quit_hteam(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_invite_hteam(_message.Message):
    __slots__ = ("uid", "id")
    UID_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    uid: _containers.RepeatedScalarFieldContainer[int]
    id: str
    def __init__(self, uid: _Optional[_Iterable[int]] = ..., id: _Optional[str] = ...) -> None: ...

class pbrsp_invite_hteam(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_search_hteam(_message.Message):
    __slots__ = ("ids",)
    IDS_FIELD_NUMBER: _ClassVar[int]
    ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, ids: _Optional[_Iterable[str]] = ...) -> None: ...

class pbrsp_search_hteam(_message.Message):
    __slots__ = ("status", "hteam")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    HTEAM_FIELD_NUMBER: _ClassVar[int]
    status: int
    hteam: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_hteam]
    def __init__(self, status: _Optional[int] = ..., hteam: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_hteam, _Mapping]]] = ...) -> None: ...

class pbreq_hteam_clear_invite(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class pbrsp_hteam_clear_invite(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_home_skin_exchange(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _dr2_comm_pb_pb2.pb_item
    def __init__(self, items: _Optional[_Union[_dr2_comm_pb_pb2.pb_item, _Mapping]] = ...) -> None: ...

class pbrsp_home_skin_exchange(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_home_one_skin(_message.Message):
    __slots__ = ("land_id", "pos", "skin")
    LAND_ID_FIELD_NUMBER: _ClassVar[int]
    POS_FIELD_NUMBER: _ClassVar[int]
    SKIN_FIELD_NUMBER: _ClassVar[int]
    land_id: int
    pos: _containers.RepeatedScalarFieldContainer[int]
    skin: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, land_id: _Optional[int] = ..., pos: _Optional[_Iterable[int]] = ..., skin: _Optional[_Iterable[int]] = ...) -> None: ...

class pbrsp_home_one_skin(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbrsp_hteam_notify(_message.Message):
    __slots__ = ("type", "id", "mbr")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    MBR_FIELD_NUMBER: _ClassVar[int]
    type: int
    id: str
    mbr: _dr2_comm_pb_pb2.pb_hmbr
    def __init__(self, type: _Optional[int] = ..., id: _Optional[str] = ..., mbr: _Optional[_Union[_dr2_comm_pb_pb2.pb_hmbr, _Mapping]] = ...) -> None: ...

class pbreq_pull_stove(_message.Message):
    __slots__ = ("pos",)
    POS_FIELD_NUMBER: _ClassVar[int]
    pos: int
    def __init__(self, pos: _Optional[int] = ...) -> None: ...

class pbrsp_pull_stove(_message.Message):
    __slots__ = ("status", "stove", "stove_buy", "lv")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    STOVE_FIELD_NUMBER: _ClassVar[int]
    STOVE_BUY_FIELD_NUMBER: _ClassVar[int]
    LV_FIELD_NUMBER: _ClassVar[int]
    status: int
    stove: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_stove]
    stove_buy: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_stove_buy]
    lv: int
    def __init__(self, status: _Optional[int] = ..., stove: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_stove, _Mapping]]] = ..., stove_buy: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_stove_buy, _Mapping]]] = ..., lv: _Optional[int] = ...) -> None: ...

class pbreq_beat_nien(_message.Message):
    __slots__ = ("id", "key")
    ID_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    id: int
    key: int
    def __init__(self, id: _Optional[int] = ..., key: _Optional[int] = ...) -> None: ...

class pbrsp_beat_nien(_message.Message):
    __slots__ = ("status", "reward", "hpp")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    REWARD_FIELD_NUMBER: _ClassVar[int]
    HPP_FIELD_NUMBER: _ClassVar[int]
    status: int
    reward: _dr2_comm_pb_pb2.pb_bag
    hpp: int
    def __init__(self, status: _Optional[int] = ..., reward: _Optional[_Union[_dr2_comm_pb_pb2.pb_bag, _Mapping]] = ..., hpp: _Optional[int] = ...) -> None: ...

class pbreq_activity(_message.Message):
    __slots__ = ("ids",)
    IDS_FIELD_NUMBER: _ClassVar[int]
    ids: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, ids: _Optional[_Iterable[int]] = ...) -> None: ...

class pbrsp_activity(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_activity_sign(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class pbrsp_activity_sign(_message.Message):
    __slots__ = ("status", "days", "reward")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    DAYS_FIELD_NUMBER: _ClassVar[int]
    REWARD_FIELD_NUMBER: _ClassVar[int]
    status: int
    days: int
    reward: _dr2_comm_pb_pb2.pb_bag
    def __init__(self, status: _Optional[int] = ..., days: _Optional[int] = ..., reward: _Optional[_Union[_dr2_comm_pb_pb2.pb_bag, _Mapping]] = ...) -> None: ...

class pbreq_fetch_activity(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class pbrsp_fetch_activity(_message.Message):
    __slots__ = ("status", "act")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ACT_FIELD_NUMBER: _ClassVar[int]
    status: int
    act: _dr2_comm_pb_pb2.pb_act
    def __init__(self, status: _Optional[int] = ..., act: _Optional[_Union[_dr2_comm_pb_pb2.pb_act, _Mapping]] = ...) -> None: ...

class pbreq_star_store(_message.Message):
    __slots__ = ("actid", "num")
    ACTID_FIELD_NUMBER: _ClassVar[int]
    NUM_FIELD_NUMBER: _ClassVar[int]
    actid: int
    num: int
    def __init__(self, actid: _Optional[int] = ..., num: _Optional[int] = ...) -> None: ...

class pbrsp_star_store(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_forge_artifact(_message.Message):
    __slots__ = ("id", "mid", "eid")
    ID_FIELD_NUMBER: _ClassVar[int]
    MID_FIELD_NUMBER: _ClassVar[int]
    EID_FIELD_NUMBER: _ClassVar[int]
    id: int
    mid: int
    eid: int
    def __init__(self, id: _Optional[int] = ..., mid: _Optional[int] = ..., eid: _Optional[int] = ...) -> None: ...

class pbrsp_forge_artifact(_message.Message):
    __slots__ = ("status", "reward")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    REWARD_FIELD_NUMBER: _ClassVar[int]
    status: int
    reward: _dr2_comm_pb_pb2.pb_bag
    def __init__(self, status: _Optional[int] = ..., reward: _Optional[_Union[_dr2_comm_pb_pb2.pb_bag, _Mapping]] = ...) -> None: ...

class pbreq_crack_artifact(_message.Message):
    __slots__ = ("ids",)
    IDS_FIELD_NUMBER: _ClassVar[int]
    ids: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_equip]
    def __init__(self, ids: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_equip, _Mapping]]] = ...) -> None: ...

class pbrsp_crack_artifact(_message.Message):
    __slots__ = ("status", "reward")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    REWARD_FIELD_NUMBER: _ClassVar[int]
    status: int
    reward: _dr2_comm_pb_pb2.pb_bag
    def __init__(self, status: _Optional[int] = ..., reward: _Optional[_Union[_dr2_comm_pb_pb2.pb_bag, _Mapping]] = ...) -> None: ...

class pbreq_monopoly_dice(_message.Message):
    __slots__ = ("type", "num")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    NUM_FIELD_NUMBER: _ClassVar[int]
    type: int
    num: int
    def __init__(self, type: _Optional[int] = ..., num: _Optional[int] = ...) -> None: ...

class pbrsp_monopoly_dice(_message.Message):
    __slots__ = ("status", "steps", "num1", "num2")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    STEPS_FIELD_NUMBER: _ClassVar[int]
    NUM1_FIELD_NUMBER: _ClassVar[int]
    NUM2_FIELD_NUMBER: _ClassVar[int]
    status: int
    steps: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_monopoly_step]
    num1: int
    num2: int
    def __init__(self, status: _Optional[int] = ..., steps: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_monopoly_step, _Mapping]]] = ..., num1: _Optional[int] = ..., num2: _Optional[int] = ...) -> None: ...

class pbreq_buy_dice(_message.Message):
    __slots__ = ("num",)
    NUM_FIELD_NUMBER: _ClassVar[int]
    num: int
    def __init__(self, num: _Optional[int] = ...) -> None: ...

class pbrsp_buy_dice(_message.Message):
    __slots__ = ("status", "rewards")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    REWARDS_FIELD_NUMBER: _ClassVar[int]
    status: int
    rewards: _dr2_comm_pb_pb2.pb_bag
    def __init__(self, status: _Optional[int] = ..., rewards: _Optional[_Union[_dr2_comm_pb_pb2.pb_bag, _Mapping]] = ...) -> None: ...

class pbreq_hero_forever(_message.Message):
    __slots__ = ("id", "actid")
    ID_FIELD_NUMBER: _ClassVar[int]
    ACTID_FIELD_NUMBER: _ClassVar[int]
    id: int
    actid: int
    def __init__(self, id: _Optional[int] = ..., actid: _Optional[int] = ...) -> None: ...

class pbrsp_hero_forever(_message.Message):
    __slots__ = ("status", "id", "heroes", "items")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    HEROES_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    status: int
    id: int
    heroes: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_hero]
    items: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_item]
    def __init__(self, status: _Optional[int] = ..., id: _Optional[int] = ..., heroes: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_hero, _Mapping]]] = ..., items: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_item, _Mapping]]] = ...) -> None: ...

class pbreq_dice_sweep(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class pbrsp_dice_sweep(_message.Message):
    __slots__ = ("status", "ds")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    DS_FIELD_NUMBER: _ClassVar[int]
    status: int
    ds: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_dice_sweep]
    def __init__(self, status: _Optional[int] = ..., ds: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_dice_sweep, _Mapping]]] = ...) -> None: ...

class pbreq_forge_back(_message.Message):
    __slots__ = ("id", "mid")
    ID_FIELD_NUMBER: _ClassVar[int]
    MID_FIELD_NUMBER: _ClassVar[int]
    id: int
    mid: int
    def __init__(self, id: _Optional[int] = ..., mid: _Optional[int] = ...) -> None: ...

class pbrsp_forge_back(_message.Message):
    __slots__ = ("status", "reward")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    REWARD_FIELD_NUMBER: _ClassVar[int]
    status: int
    reward: _dr2_comm_pb_pb2.pb_bag
    def __init__(self, status: _Optional[int] = ..., reward: _Optional[_Union[_dr2_comm_pb_pb2.pb_bag, _Mapping]] = ...) -> None: ...

class pbreq_gold_card(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class pbrsp_gold_card(_message.Message):
    __slots__ = ("status", "reward")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    REWARD_FIELD_NUMBER: _ClassVar[int]
    status: int
    reward: _dr2_comm_pb_pb2.pb_bag
    def __init__(self, status: _Optional[int] = ..., reward: _Optional[_Union[_dr2_comm_pb_pb2.pb_bag, _Mapping]] = ...) -> None: ...

class pbreq_limit_gift_activate(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class pbrsp_limit_gift_activate(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_maze_open(_message.Message):
    __slots__ = ("pos", "reward")
    POS_FIELD_NUMBER: _ClassVar[int]
    REWARD_FIELD_NUMBER: _ClassVar[int]
    pos: int
    reward: int
    def __init__(self, pos: _Optional[int] = ..., reward: _Optional[int] = ...) -> None: ...

class pbrsp_maze_open(_message.Message):
    __slots__ = ("status", "maze", "event", "reward")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MAZE_FIELD_NUMBER: _ClassVar[int]
    EVENT_FIELD_NUMBER: _ClassVar[int]
    REWARD_FIELD_NUMBER: _ClassVar[int]
    status: int
    maze: _dr2_comm_pb_pb2.pb_act_maze
    event: _dr2_comm_pb_pb2.pb_act_block
    reward: _dr2_comm_pb_pb2.pb_bag
    def __init__(self, status: _Optional[int] = ..., maze: _Optional[_Union[_dr2_comm_pb_pb2.pb_act_maze, _Mapping]] = ..., event: _Optional[_Union[_dr2_comm_pb_pb2.pb_act_block, _Mapping]] = ..., reward: _Optional[_Union[_dr2_comm_pb_pb2.pb_bag, _Mapping]] = ...) -> None: ...

class pbreq_maze_change_hero(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class pbrsp_maze_change_hero(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_maze_open2(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class pbrsp_maze_open2(_message.Message):
    __slots__ = ("status", "reward")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    REWARD_FIELD_NUMBER: _ClassVar[int]
    status: int
    reward: _dr2_comm_pb_pb2.pb_bag
    def __init__(self, status: _Optional[int] = ..., reward: _Optional[_Union[_dr2_comm_pb_pb2.pb_bag, _Mapping]] = ...) -> None: ...

class pbreq_maze_buy(_message.Message):
    __slots__ = ("num",)
    NUM_FIELD_NUMBER: _ClassVar[int]
    num: int
    def __init__(self, num: _Optional[int] = ...) -> None: ...

class pbrsp_maze_buy(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_maze_sync(_message.Message):
    __slots__ = ("actid",)
    ACTID_FIELD_NUMBER: _ClassVar[int]
    actid: int
    def __init__(self, actid: _Optional[int] = ...) -> None: ...

class pbrsp_maze_sync(_message.Message):
    __slots__ = ("status", "maze")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MAZE_FIELD_NUMBER: _ClassVar[int]
    status: int
    maze: _dr2_comm_pb_pb2.pb_act_maze
    def __init__(self, status: _Optional[int] = ..., maze: _Optional[_Union[_dr2_comm_pb_pb2.pb_act_maze, _Mapping]] = ...) -> None: ...

class pbreq_maze_break(_message.Message):
    __slots__ = ("type", "pos")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    POS_FIELD_NUMBER: _ClassVar[int]
    type: int
    pos: int
    def __init__(self, type: _Optional[int] = ..., pos: _Optional[int] = ...) -> None: ...

class pbrsp_maze_break(_message.Message):
    __slots__ = ("status", "events")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    EVENTS_FIELD_NUMBER: _ClassVar[int]
    status: int
    events: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_act_block]
    def __init__(self, status: _Optional[int] = ..., events: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_act_block, _Mapping]]] = ...) -> None: ...

class pbreq_maze_batch(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class pbrsp_maze_batch(_message.Message):
    __slots__ = ("status", "num", "maze", "rewards_base")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    NUM_FIELD_NUMBER: _ClassVar[int]
    MAZE_FIELD_NUMBER: _ClassVar[int]
    REWARDS_BASE_FIELD_NUMBER: _ClassVar[int]
    status: int
    num: int
    maze: _dr2_comm_pb_pb2.pb_act_maze
    rewards_base: _dr2_comm_pb_pb2.pb_bag
    def __init__(self, status: _Optional[int] = ..., num: _Optional[int] = ..., maze: _Optional[_Union[_dr2_comm_pb_pb2.pb_act_maze, _Mapping]] = ..., rewards_base: _Optional[_Union[_dr2_comm_pb_pb2.pb_bag, _Mapping]] = ...) -> None: ...

class pbreq_fetch_sact(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class pbrsp_fetch_sact(_message.Message):
    __slots__ = ("status", "sact")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    SACT_FIELD_NUMBER: _ClassVar[int]
    status: int
    sact: _dr2_comm_pb_pb2.pb_sact_item
    def __init__(self, status: _Optional[int] = ..., sact: _Optional[_Union[_dr2_comm_pb_pb2.pb_sact_item, _Mapping]] = ...) -> None: ...

class pbreq_htask_commit(_message.Message):
    __slots__ = ("id", "num")
    ID_FIELD_NUMBER: _ClassVar[int]
    NUM_FIELD_NUMBER: _ClassVar[int]
    id: int
    num: int
    def __init__(self, id: _Optional[int] = ..., num: _Optional[int] = ...) -> None: ...

class pbrsp_htask_commit(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_birthday_gift(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class pbrsp_birthday_gift(_message.Message):
    __slots__ = ("status", "rewards")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    REWARDS_FIELD_NUMBER: _ClassVar[int]
    status: int
    rewards: _dr2_comm_pb_pb2.pb_bag
    def __init__(self, status: _Optional[int] = ..., rewards: _Optional[_Union[_dr2_comm_pb_pb2.pb_bag, _Mapping]] = ...) -> None: ...

class pbreq_extra_spring(_message.Message):
    __slots__ = ("id", "num")
    ID_FIELD_NUMBER: _ClassVar[int]
    NUM_FIELD_NUMBER: _ClassVar[int]
    id: int
    num: int
    def __init__(self, id: _Optional[int] = ..., num: _Optional[int] = ...) -> None: ...

class pbrsp_extra_spring(_message.Message):
    __slots__ = ("status", "rewards", "id")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    REWARDS_FIELD_NUMBER: _ClassVar[int]
    DEL_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    status: int
    rewards: _dr2_comm_pb_pb2.pb_bag
    id: int
    def __init__(self, status: _Optional[int] = ..., rewards: _Optional[_Union[_dr2_comm_pb_pb2.pb_bag, _Mapping]] = ..., id: _Optional[int] = ..., **kwargs) -> None: ...

class pbreq_extra_relay_pkg(_message.Message):
    __slots__ = ("actid",)
    ACTID_FIELD_NUMBER: _ClassVar[int]
    actid: int
    def __init__(self, actid: _Optional[int] = ...) -> None: ...

class pbrsp_extra_relay_pkg(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_growup_buy(_message.Message):
    __slots__ = ("actid",)
    ACTID_FIELD_NUMBER: _ClassVar[int]
    actid: int
    def __init__(self, actid: _Optional[int] = ...) -> None: ...

class pbrsp_growup_buy(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_growup_choose(_message.Message):
    __slots__ = ("actid1", "actid2", "index")
    ACTID1_FIELD_NUMBER: _ClassVar[int]
    ACTID2_FIELD_NUMBER: _ClassVar[int]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    actid1: int
    actid2: int
    index: int
    def __init__(self, actid1: _Optional[int] = ..., actid2: _Optional[int] = ..., index: _Optional[int] = ...) -> None: ...

class pbrsp_growup_choose(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_growup_claim(_message.Message):
    __slots__ = ("actid",)
    ACTID_FIELD_NUMBER: _ClassVar[int]
    actid: int
    def __init__(self, actid: _Optional[int] = ...) -> None: ...

class pbrsp_growup_claim(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_act_choose(_message.Message):
    __slots__ = ("id", "sub")
    ID_FIELD_NUMBER: _ClassVar[int]
    SUB_FIELD_NUMBER: _ClassVar[int]
    id: int
    sub: int
    def __init__(self, id: _Optional[int] = ..., sub: _Optional[int] = ...) -> None: ...

class pbrsp_act_choose(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_act_reward(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, id: _Optional[_Iterable[int]] = ...) -> None: ...

class pbrsp_act_reward(_message.Message):
    __slots__ = ("status", "bag")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    BAG_FIELD_NUMBER: _ClassVar[int]
    status: int
    bag: _dr2_comm_pb_pb2.pb_bag
    def __init__(self, status: _Optional[int] = ..., bag: _Optional[_Union[_dr2_comm_pb_pb2.pb_bag, _Mapping]] = ...) -> None: ...

class pbreq_act_qstar(_message.Message):
    __slots__ = ("actid",)
    ACTID_FIELD_NUMBER: _ClassVar[int]
    actid: int
    def __init__(self, actid: _Optional[int] = ...) -> None: ...

class pbrsp_act_qstar(_message.Message):
    __slots__ = ("status", "rank_list", "uid")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    RANK_LIST_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    status: int
    rank_list: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_qstar]
    uid: int
    def __init__(self, status: _Optional[int] = ..., rank_list: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_qstar, _Mapping]]] = ..., uid: _Optional[int] = ...) -> None: ...

class pbreq_act_reward2(_message.Message):
    __slots__ = ("actid", "sub")
    ACTID_FIELD_NUMBER: _ClassVar[int]
    SUB_FIELD_NUMBER: _ClassVar[int]
    actid: int
    sub: int
    def __init__(self, actid: _Optional[int] = ..., sub: _Optional[int] = ...) -> None: ...

class pbrsp_act_reward2(_message.Message):
    __slots__ = ("status", "bag")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    BAG_FIELD_NUMBER: _ClassVar[int]
    status: int
    bag: _dr2_comm_pb_pb2.pb_bag
    def __init__(self, status: _Optional[int] = ..., bag: _Optional[_Union[_dr2_comm_pb_pb2.pb_bag, _Mapping]] = ...) -> None: ...

class pbreq_art_merge(_message.Message):
    __slots__ = ("mid", "eid1", "eid2")
    MID_FIELD_NUMBER: _ClassVar[int]
    EID1_FIELD_NUMBER: _ClassVar[int]
    EID2_FIELD_NUMBER: _ClassVar[int]
    mid: int
    eid1: int
    eid2: int
    def __init__(self, mid: _Optional[int] = ..., eid1: _Optional[int] = ..., eid2: _Optional[int] = ...) -> None: ...

class pbrsp_art_merge(_message.Message):
    __slots__ = ("status", "reward")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    REWARD_FIELD_NUMBER: _ClassVar[int]
    status: int
    reward: _dr2_comm_pb_pb2.pb_bag
    def __init__(self, status: _Optional[int] = ..., reward: _Optional[_Union[_dr2_comm_pb_pb2.pb_bag, _Mapping]] = ...) -> None: ...

class pbreq_activity_remove(_message.Message):
    __slots__ = ("act_id", "id")
    ACT_ID_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    act_id: int
    id: int
    def __init__(self, act_id: _Optional[int] = ..., id: _Optional[int] = ...) -> None: ...

class pbrsp_activity_remove(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_activity_desk_sync(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class pbrsp_activity_desk_sync(_message.Message):
    __slots__ = ("status", "id", "blood", "hlist", "flist", "cflist", "cd", "demage", "chlist", "act_id", "get")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    BLOOD_FIELD_NUMBER: _ClassVar[int]
    HLIST_FIELD_NUMBER: _ClassVar[int]
    FLIST_FIELD_NUMBER: _ClassVar[int]
    CFLIST_FIELD_NUMBER: _ClassVar[int]
    CD_FIELD_NUMBER: _ClassVar[int]
    DEMAGE_FIELD_NUMBER: _ClassVar[int]
    CHLIST_FIELD_NUMBER: _ClassVar[int]
    ACT_ID_FIELD_NUMBER: _ClassVar[int]
    GET_FIELD_NUMBER: _ClassVar[int]
    status: int
    id: int
    blood: int
    hlist: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_desk_hero]
    flist: _containers.RepeatedScalarFieldContainer[int]
    cflist: _containers.RepeatedScalarFieldContainer[int]
    cd: int
    demage: int
    chlist: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_desk_hero]
    act_id: int
    get: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, status: _Optional[int] = ..., id: _Optional[int] = ..., blood: _Optional[int] = ..., hlist: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_desk_hero, _Mapping]]] = ..., flist: _Optional[_Iterable[int]] = ..., cflist: _Optional[_Iterable[int]] = ..., cd: _Optional[int] = ..., demage: _Optional[int] = ..., chlist: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_desk_hero, _Mapping]]] = ..., act_id: _Optional[int] = ..., get: _Optional[_Iterable[int]] = ...) -> None: ...

class pbreq_activity_desk_draw(_message.Message):
    __slots__ = ("num",)
    NUM_FIELD_NUMBER: _ClassVar[int]
    num: int
    def __init__(self, num: _Optional[int] = ...) -> None: ...

class pbrsp_activity_desk_draw(_message.Message):
    __slots__ = ("status", "hero", "fid")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    HERO_FIELD_NUMBER: _ClassVar[int]
    FID_FIELD_NUMBER: _ClassVar[int]
    status: int
    hero: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_kv2]
    fid: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, status: _Optional[int] = ..., hero: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_kv2, _Mapping]]] = ..., fid: _Optional[_Iterable[int]] = ...) -> None: ...

class pbreq_activity_desk_fight(_message.Message):
    __slots__ = ("id", "type")
    ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    id: int
    type: int
    def __init__(self, id: _Optional[int] = ..., type: _Optional[int] = ...) -> None: ...

class pbrsp_activity_desk_fight(_message.Message):
    __slots__ = ("status", "blood", "hero", "clist", "reward", "win", "get")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    BLOOD_FIELD_NUMBER: _ClassVar[int]
    HERO_FIELD_NUMBER: _ClassVar[int]
    CLIST_FIELD_NUMBER: _ClassVar[int]
    REWARD_FIELD_NUMBER: _ClassVar[int]
    WIN_FIELD_NUMBER: _ClassVar[int]
    GET_FIELD_NUMBER: _ClassVar[int]
    status: int
    blood: int
    hero: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_kv2]
    clist: _containers.RepeatedScalarFieldContainer[int]
    reward: _dr2_comm_pb_pb2.pb_bag
    win: int
    get: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, status: _Optional[int] = ..., blood: _Optional[int] = ..., hero: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_kv2, _Mapping]]] = ..., clist: _Optional[_Iterable[int]] = ..., reward: _Optional[_Union[_dr2_comm_pb_pb2.pb_bag, _Mapping]] = ..., win: _Optional[int] = ..., get: _Optional[_Iterable[int]] = ...) -> None: ...

class pbreq_activity_desk_rank(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class pbrsp_activity_desk_rank(_message.Message):
    __slots__ = ("status", "list", "uid", "score")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    LIST_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    status: int
    list: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_qstar]
    uid: int
    score: int
    def __init__(self, status: _Optional[int] = ..., list: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_qstar, _Mapping]]] = ..., uid: _Optional[int] = ..., score: _Optional[int] = ...) -> None: ...

class pbreq_activity_desk_fun(_message.Message):
    __slots__ = ("id", "fid", "index", "type", "boss")
    ID_FIELD_NUMBER: _ClassVar[int]
    FID_FIELD_NUMBER: _ClassVar[int]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    BOSS_FIELD_NUMBER: _ClassVar[int]
    id: int
    fid: int
    index: int
    type: int
    boss: int
    def __init__(self, id: _Optional[int] = ..., fid: _Optional[int] = ..., index: _Optional[int] = ..., type: _Optional[int] = ..., boss: _Optional[int] = ...) -> None: ...

class pbrsp_activity_desk_fun(_message.Message):
    __slots__ = ("status", "heros", "card")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    HEROS_FIELD_NUMBER: _ClassVar[int]
    CARD_FIELD_NUMBER: _ClassVar[int]
    status: int
    heros: _dr2_comm_pb_pb2.pb_desk_hero
    card: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, status: _Optional[int] = ..., heros: _Optional[_Union[_dr2_comm_pb_pb2.pb_desk_hero, _Mapping]] = ..., card: _Optional[_Iterable[int]] = ...) -> None: ...

class pbreq_activity_desk_sweep(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class pbrsp_activity_desk_sweep(_message.Message):
    __slots__ = ("status", "blood", "hlist", "clist", "reward", "id")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    BLOOD_FIELD_NUMBER: _ClassVar[int]
    HLIST_FIELD_NUMBER: _ClassVar[int]
    CLIST_FIELD_NUMBER: _ClassVar[int]
    REWARD_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    DEL_FIELD_NUMBER: _ClassVar[int]
    status: int
    blood: int
    hlist: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_kv2]
    clist: _containers.RepeatedScalarFieldContainer[int]
    reward: _dr2_comm_pb_pb2.pb_bag
    id: int
    def __init__(self, status: _Optional[int] = ..., blood: _Optional[int] = ..., hlist: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_kv2, _Mapping]]] = ..., clist: _Optional[_Iterable[int]] = ..., reward: _Optional[_Union[_dr2_comm_pb_pb2.pb_bag, _Mapping]] = ..., id: _Optional[int] = ..., **kwargs) -> None: ...

class pbreq_monthmarket_buy(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class pbrsp_monthmarket_buy(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_monthmarket_sync(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class pbrsp_monthmarket_sync(_message.Message):
    __slots__ = ("status", "mpiece", "mequip", "mskin", "mlimit")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MPIECE_FIELD_NUMBER: _ClassVar[int]
    MEQUIP_FIELD_NUMBER: _ClassVar[int]
    MSKIN_FIELD_NUMBER: _ClassVar[int]
    MLIMIT_FIELD_NUMBER: _ClassVar[int]
    status: int
    mpiece: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_hmarket]
    mequip: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_hmarket]
    mskin: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_hmarket]
    mlimit: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_hmarket]
    def __init__(self, status: _Optional[int] = ..., mpiece: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_hmarket, _Mapping]]] = ..., mequip: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_hmarket, _Mapping]]] = ..., mskin: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_hmarket, _Mapping]]] = ..., mlimit: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_hmarket, _Mapping]]] = ...) -> None: ...

class pbreq_re_sync(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class pbrsp_re_sync(_message.Message):
    __slots__ = ("status", "re_sync")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    RE_SYNC_FIELD_NUMBER: _ClassVar[int]
    status: int
    re_sync: _dr2_comm_pb_pb2.pb_re_sync
    def __init__(self, status: _Optional[int] = ..., re_sync: _Optional[_Union[_dr2_comm_pb_pb2.pb_re_sync, _Mapping]] = ...) -> None: ...

class pbreq_re_code(_message.Message):
    __slots__ = ("code",)
    CODE_FIELD_NUMBER: _ClassVar[int]
    code: str
    def __init__(self, code: _Optional[str] = ...) -> None: ...

class pbrsp_re_code(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_re_bind(_message.Message):
    __slots__ = ("uid", "type")
    UID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    uid: int
    type: int
    def __init__(self, uid: _Optional[int] = ..., type: _Optional[int] = ...) -> None: ...

class pbrsp_re_bind(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_re_claim(_message.Message):
    __slots__ = ("type",)
    TYPE_FIELD_NUMBER: _ClassVar[int]
    type: int
    def __init__(self, type: _Optional[int] = ...) -> None: ...

class pbrsp_re_claim(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_sact_exchange(_message.Message):
    __slots__ = ("id", "num", "index", "hids")
    ID_FIELD_NUMBER: _ClassVar[int]
    NUM_FIELD_NUMBER: _ClassVar[int]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    HIDS_FIELD_NUMBER: _ClassVar[int]
    id: int
    num: int
    index: int
    hids: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, id: _Optional[int] = ..., num: _Optional[int] = ..., index: _Optional[int] = ..., hids: _Optional[_Iterable[int]] = ...) -> None: ...

class pbrsp_sact_exchange(_message.Message):
    __slots__ = ("status", "rewards", "bomb", "ghost", "hero", "fish")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    REWARDS_FIELD_NUMBER: _ClassVar[int]
    BOMB_FIELD_NUMBER: _ClassVar[int]
    GHOST_FIELD_NUMBER: _ClassVar[int]
    HERO_FIELD_NUMBER: _ClassVar[int]
    FISH_FIELD_NUMBER: _ClassVar[int]
    status: int
    rewards: _dr2_comm_pb_pb2.pb_bag
    bomb: int
    ghost: _containers.RepeatedScalarFieldContainer[int]
    hero: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_hero]
    fish: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_kv2]
    def __init__(self, status: _Optional[int] = ..., rewards: _Optional[_Union[_dr2_comm_pb_pb2.pb_bag, _Mapping]] = ..., bomb: _Optional[int] = ..., ghost: _Optional[_Iterable[int]] = ..., hero: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_hero, _Mapping]]] = ..., fish: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_kv2, _Mapping]]] = ...) -> None: ...

class pbreq_sact_open(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class pbrsp_sact_open(_message.Message):
    __slots__ = ("status", "cd")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    CD_FIELD_NUMBER: _ClassVar[int]
    status: int
    cd: int
    def __init__(self, status: _Optional[int] = ..., cd: _Optional[int] = ...) -> None: ...

class pbreq_sact_buy_score(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class pbrsp_sact_buy_score(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_sact_choose(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class pbrsp_sact_choose(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_sact_topic(_message.Message):
    __slots__ = ("actid", "tid", "ans")
    ACTID_FIELD_NUMBER: _ClassVar[int]
    TID_FIELD_NUMBER: _ClassVar[int]
    ANS_FIELD_NUMBER: _ClassVar[int]
    actid: int
    tid: int
    ans: int
    def __init__(self, actid: _Optional[int] = ..., tid: _Optional[int] = ..., ans: _Optional[int] = ...) -> None: ...

class pbrsp_sact_topic(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_sact_get_reward(_message.Message):
    __slots__ = ("actids", "index")
    ACTIDS_FIELD_NUMBER: _ClassVar[int]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    actids: _containers.RepeatedScalarFieldContainer[int]
    index: int
    def __init__(self, actids: _Optional[_Iterable[int]] = ..., index: _Optional[int] = ...) -> None: ...

class pbrsp_sact_get_reward(_message.Message):
    __slots__ = ("status", "reward", "num")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    REWARD_FIELD_NUMBER: _ClassVar[int]
    NUM_FIELD_NUMBER: _ClassVar[int]
    status: int
    reward: _dr2_comm_pb_pb2.pb_bag
    num: int
    def __init__(self, status: _Optional[int] = ..., reward: _Optional[_Union[_dr2_comm_pb_pb2.pb_bag, _Mapping]] = ..., num: _Optional[int] = ...) -> None: ...

class pbreq_sact_choose_reward(_message.Message):
    __slots__ = ("actid", "index")
    ACTID_FIELD_NUMBER: _ClassVar[int]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    actid: int
    index: int
    def __init__(self, actid: _Optional[int] = ..., index: _Optional[int] = ...) -> None: ...

class pbrsp_sact_choose_reward(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_sact_hero_star(_message.Message):
    __slots__ = ("actid",)
    ACTID_FIELD_NUMBER: _ClassVar[int]
    actid: int
    def __init__(self, actid: _Optional[int] = ...) -> None: ...

class pbrsp_sact_hero_star(_message.Message):
    __slots__ = ("status", "rank_list", "uid", "score", "total_score", "rank")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    RANK_LIST_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SCORE_FIELD_NUMBER: _ClassVar[int]
    RANK_FIELD_NUMBER: _ClassVar[int]
    status: int
    rank_list: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_hstar]
    uid: int
    score: int
    total_score: int
    rank: int
    def __init__(self, status: _Optional[int] = ..., rank_list: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_hstar, _Mapping]]] = ..., uid: _Optional[int] = ..., score: _Optional[int] = ..., total_score: _Optional[int] = ..., rank: _Optional[int] = ...) -> None: ...

class pbreq_sact_plant(_message.Message):
    __slots__ = ("actid",)
    ACTID_FIELD_NUMBER: _ClassVar[int]
    actid: int
    def __init__(self, actid: _Optional[int] = ...) -> None: ...

class pbrsp_sact_plant(_message.Message):
    __slots__ = ("status", "maze")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MAZE_FIELD_NUMBER: _ClassVar[int]
    status: int
    maze: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_sact_maze]
    def __init__(self, status: _Optional[int] = ..., maze: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_sact_maze, _Mapping]]] = ...) -> None: ...

class pbreq_hero_log(_message.Message):
    __slots__ = ("type",)
    TYPE_FIELD_NUMBER: _ClassVar[int]
    type: int
    def __init__(self, type: _Optional[int] = ...) -> None: ...

class pbrsp_hero_log(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_casino_item]
    def __init__(self, items: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_casino_item, _Mapping]]] = ...) -> None: ...

class pbreq_tutorial(_message.Message):
    __slots__ = ("type",)
    TYPE_FIELD_NUMBER: _ClassVar[int]
    type: int
    def __init__(self, type: _Optional[int] = ...) -> None: ...

class pbrsp_tutorial(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_ract_receive(_message.Message):
    __slots__ = ("type", "id")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    type: int
    id: int
    def __init__(self, type: _Optional[int] = ..., id: _Optional[int] = ...) -> None: ...

class pbrsp_ract_receive(_message.Message):
    __slots__ = ("status", "reward")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    REWARD_FIELD_NUMBER: _ClassVar[int]
    status: int
    reward: _dr2_comm_pb_pb2.pb_bag
    def __init__(self, status: _Optional[int] = ..., reward: _Optional[_Union[_dr2_comm_pb_pb2.pb_bag, _Mapping]] = ...) -> None: ...

class pbreq_ract_power(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class pbrsp_ract_power(_message.Message):
    __slots__ = ("status", "power")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    POWER_FIELD_NUMBER: _ClassVar[int]
    status: int
    power: int
    def __init__(self, status: _Optional[int] = ..., power: _Optional[int] = ...) -> None: ...

class pbreq_wsync(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class pbrsp_wsync(_message.Message):
    __slots__ = ("status", "power", "score", "rank1", "num", "zid", "top_score", "mbr1", "mbr2", "task_nums", "ids", "camp", "enemy_unit", "enemy_def", "enemy_cd", "king", "top_king", "znum", "enemy_num", "rank2", "sdate")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    POWER_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    RANK1_FIELD_NUMBER: _ClassVar[int]
    NUM_FIELD_NUMBER: _ClassVar[int]
    ZID_FIELD_NUMBER: _ClassVar[int]
    TOP_SCORE_FIELD_NUMBER: _ClassVar[int]
    MBR1_FIELD_NUMBER: _ClassVar[int]
    MBR2_FIELD_NUMBER: _ClassVar[int]
    TASK_NUMS_FIELD_NUMBER: _ClassVar[int]
    IDS_FIELD_NUMBER: _ClassVar[int]
    CAMP_FIELD_NUMBER: _ClassVar[int]
    ENEMY_UNIT_FIELD_NUMBER: _ClassVar[int]
    ENEMY_DEF_FIELD_NUMBER: _ClassVar[int]
    ENEMY_CD_FIELD_NUMBER: _ClassVar[int]
    KING_FIELD_NUMBER: _ClassVar[int]
    TOP_KING_FIELD_NUMBER: _ClassVar[int]
    ZNUM_FIELD_NUMBER: _ClassVar[int]
    ENEMY_NUM_FIELD_NUMBER: _ClassVar[int]
    RANK2_FIELD_NUMBER: _ClassVar[int]
    SDATE_FIELD_NUMBER: _ClassVar[int]
    status: int
    power: int
    score: int
    rank1: int
    num: int
    zid: int
    top_score: int
    mbr1: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_wmbr]
    mbr2: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_wmbr]
    task_nums: _containers.RepeatedScalarFieldContainer[int]
    ids: _containers.RepeatedScalarFieldContainer[int]
    camp: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_unit]
    enemy_unit: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_unit]
    enemy_def: _dr2_comm_pb_pb2.pb_wmbr
    enemy_cd: int
    king: bool
    top_king: bool
    znum: int
    enemy_num: int
    rank2: int
    sdate: str
    def __init__(self, status: _Optional[int] = ..., power: _Optional[int] = ..., score: _Optional[int] = ..., rank1: _Optional[int] = ..., num: _Optional[int] = ..., zid: _Optional[int] = ..., top_score: _Optional[int] = ..., mbr1: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_wmbr, _Mapping]]] = ..., mbr2: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_wmbr, _Mapping]]] = ..., task_nums: _Optional[_Iterable[int]] = ..., ids: _Optional[_Iterable[int]] = ..., camp: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_unit, _Mapping]]] = ..., enemy_unit: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_unit, _Mapping]]] = ..., enemy_def: _Optional[_Union[_dr2_comm_pb_pb2.pb_wmbr, _Mapping]] = ..., enemy_cd: _Optional[int] = ..., king: _Optional[bool] = ..., top_king: _Optional[bool] = ..., znum: _Optional[int] = ..., enemy_num: _Optional[int] = ..., rank2: _Optional[int] = ..., sdate: _Optional[str] = ...) -> None: ...

class pbreq_whonor(_message.Message):
    __slots__ = ("wid",)
    WID_FIELD_NUMBER: _ClassVar[int]
    wid: int
    def __init__(self, wid: _Optional[int] = ...) -> None: ...

class pbrsp_whonor(_message.Message):
    __slots__ = ("status", "mbrs", "camp", "link")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MBRS_FIELD_NUMBER: _ClassVar[int]
    CAMP_FIELD_NUMBER: _ClassVar[int]
    LINK_FIELD_NUMBER: _ClassVar[int]
    status: int
    mbrs: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_wmbr]
    camp: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_wcamp]
    link: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_link]
    def __init__(self, status: _Optional[int] = ..., mbrs: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_wmbr, _Mapping]]] = ..., camp: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_wcamp, _Mapping]]] = ..., link: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_link, _Mapping]]] = ...) -> None: ...

class pbreq_wdaily(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class pbrsp_wdaily(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_wmatch(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class pbrsp_wmatch(_message.Message):
    __slots__ = ("status", "unit", "cd", "num")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    UNIT_FIELD_NUMBER: _ClassVar[int]
    DEF_FIELD_NUMBER: _ClassVar[int]
    CD_FIELD_NUMBER: _ClassVar[int]
    NUM_FIELD_NUMBER: _ClassVar[int]
    status: int
    unit: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_unit]
    cd: int
    num: int
    def __init__(self, status: _Optional[int] = ..., unit: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_unit, _Mapping]]] = ..., cd: _Optional[int] = ..., num: _Optional[int] = ..., **kwargs) -> None: ...

class pbreq_wcamp(_message.Message):
    __slots__ = ("camp",)
    CAMP_FIELD_NUMBER: _ClassVar[int]
    camp: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_unit]
    def __init__(self, camp: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_unit, _Mapping]]] = ...) -> None: ...

class pbrsp_wcamp(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_wfight(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class pbrsp_wfight(_message.Message):
    __slots__ = ("status", "mbr", "video", "atk", "wins", "select", "rewards")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MBR_FIELD_NUMBER: _ClassVar[int]
    VIDEO_FIELD_NUMBER: _ClassVar[int]
    ATK_FIELD_NUMBER: _ClassVar[int]
    WINS_FIELD_NUMBER: _ClassVar[int]
    SELECT_FIELD_NUMBER: _ClassVar[int]
    REWARDS_FIELD_NUMBER: _ClassVar[int]
    status: int
    mbr: _dr2_comm_pb_pb2.pb_wmbr
    video: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_wvideo]
    atk: _dr2_comm_pb_pb2.pb_wscore
    wins: _containers.RepeatedScalarFieldContainer[bool]
    select: int
    rewards: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_bag]
    def __init__(self, status: _Optional[int] = ..., mbr: _Optional[_Union[_dr2_comm_pb_pb2.pb_wmbr, _Mapping]] = ..., video: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_wvideo, _Mapping]]] = ..., atk: _Optional[_Union[_dr2_comm_pb_pb2.pb_wscore, _Mapping]] = ..., wins: _Optional[_Iterable[bool]] = ..., select: _Optional[int] = ..., rewards: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_bag, _Mapping]]] = ...) -> None: ...

class pbreq_wlike(_message.Message):
    __slots__ = ("uid",)
    UID_FIELD_NUMBER: _ClassVar[int]
    uid: int
    def __init__(self, uid: _Optional[int] = ...) -> None: ...

class pbrsp_wlike(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_winfo(_message.Message):
    __slots__ = ("uid",)
    UID_FIELD_NUMBER: _ClassVar[int]
    uid: int
    def __init__(self, uid: _Optional[int] = ...) -> None: ...

class pbrsp_winfo(_message.Message):
    __slots__ = ("status", "unit")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    UNIT_FIELD_NUMBER: _ClassVar[int]
    status: int
    unit: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_unit]
    def __init__(self, status: _Optional[int] = ..., unit: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_unit, _Mapping]]] = ...) -> None: ...

class pbreq_wzone(_message.Message):
    __slots__ = ("zid", "link")
    ZID_FIELD_NUMBER: _ClassVar[int]
    LINK_FIELD_NUMBER: _ClassVar[int]
    zid: int
    link: int
    def __init__(self, zid: _Optional[int] = ..., link: _Optional[int] = ...) -> None: ...

class pbrsp_wzone(_message.Message):
    __slots__ = ("status", "flag", "num", "mbrs", "link")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    FLAG_FIELD_NUMBER: _ClassVar[int]
    NUM_FIELD_NUMBER: _ClassVar[int]
    MBRS_FIELD_NUMBER: _ClassVar[int]
    LINK_FIELD_NUMBER: _ClassVar[int]
    status: int
    flag: int
    num: int
    mbrs: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_wmbr]
    link: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_link]
    def __init__(self, status: _Optional[int] = ..., flag: _Optional[int] = ..., num: _Optional[int] = ..., mbrs: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_wmbr, _Mapping]]] = ..., link: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_link, _Mapping]]] = ...) -> None: ...

class pbreq_wloger1(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class pbrsp_wloger1(_message.Message):
    __slots__ = ("status", "logs")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    LOGS_FIELD_NUMBER: _ClassVar[int]
    status: int
    logs: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_wloger]
    def __init__(self, status: _Optional[int] = ..., logs: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_wloger, _Mapping]]] = ...) -> None: ...

class pbreq_wlog1(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class pbrsp_wlog1(_message.Message):
    __slots__ = ("status", "logs")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    LOGS_FIELD_NUMBER: _ClassVar[int]
    status: int
    logs: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_wlog]
    def __init__(self, status: _Optional[int] = ..., logs: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_wlog, _Mapping]]] = ...) -> None: ...

class pbreq_wvideo1(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class pbrsp_wvideo1(_message.Message):
    __slots__ = ("status", "video")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    VIDEO_FIELD_NUMBER: _ClassVar[int]
    status: int
    video: _dr2_comm_pb_pb2.pb_wvideo
    def __init__(self, status: _Optional[int] = ..., video: _Optional[_Union[_dr2_comm_pb_pb2.pb_wvideo, _Mapping]] = ...) -> None: ...

class pbreq_wlog2(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class pbrsp_wlog2(_message.Message):
    __slots__ = ("status", "atk", "logs")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ATK_FIELD_NUMBER: _ClassVar[int]
    DEF_FIELD_NUMBER: _ClassVar[int]
    LOGS_FIELD_NUMBER: _ClassVar[int]
    status: int
    atk: int
    logs: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_wlog]
    def __init__(self, status: _Optional[int] = ..., atk: _Optional[int] = ..., logs: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_wlog, _Mapping]]] = ..., **kwargs) -> None: ...

class pbreq_wvideo2(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class pbrsp_wvideo2(_message.Message):
    __slots__ = ("status", "video")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    VIDEO_FIELD_NUMBER: _ClassVar[int]
    status: int
    video: _dr2_comm_pb_pb2.pb_wvideo
    def __init__(self, status: _Optional[int] = ..., video: _Optional[_Union[_dr2_comm_pb_pb2.pb_wvideo, _Mapping]] = ...) -> None: ...

class pbreq_st_sync(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class pbrsp_st_sync(_message.Message):
    __slots__ = ("rates", "id1", "id2", "times", "flag")
    RATES_FIELD_NUMBER: _ClassVar[int]
    ID1_FIELD_NUMBER: _ClassVar[int]
    ID2_FIELD_NUMBER: _ClassVar[int]
    TIMES_FIELD_NUMBER: _ClassVar[int]
    FLAG_FIELD_NUMBER: _ClassVar[int]
    rates: _containers.RepeatedScalarFieldContainer[int]
    id1: int
    id2: int
    times: int
    flag: int
    def __init__(self, rates: _Optional[_Iterable[int]] = ..., id1: _Optional[int] = ..., id2: _Optional[int] = ..., times: _Optional[int] = ..., flag: _Optional[int] = ...) -> None: ...

class pbreq_st_summon(_message.Message):
    __slots__ = ("type",)
    TYPE_FIELD_NUMBER: _ClassVar[int]
    type: int
    def __init__(self, type: _Optional[int] = ...) -> None: ...

class pbrsp_st_summon(_message.Message):
    __slots__ = ("status", "heroes", "items", "rates", "times")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    HEROES_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    RATES_FIELD_NUMBER: _ClassVar[int]
    TIMES_FIELD_NUMBER: _ClassVar[int]
    status: int
    heroes: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_hero]
    items: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_item]
    rates: _containers.RepeatedScalarFieldContainer[int]
    times: int
    def __init__(self, status: _Optional[int] = ..., heroes: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_hero, _Mapping]]] = ..., items: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_item, _Mapping]]] = ..., rates: _Optional[_Iterable[int]] = ..., times: _Optional[int] = ...) -> None: ...

class pbreq_st_schange(_message.Message):
    __slots__ = ("id1", "id2")
    ID1_FIELD_NUMBER: _ClassVar[int]
    ID2_FIELD_NUMBER: _ClassVar[int]
    id1: int
    id2: int
    def __init__(self, id1: _Optional[int] = ..., id2: _Optional[int] = ...) -> None: ...

class pbrsp_st_schange(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_st_rank(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class pbrsp_st_rank(_message.Message):
    __slots__ = ("status", "mbrs")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MBRS_FIELD_NUMBER: _ClassVar[int]
    status: int
    mbrs: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_smbrs]
    def __init__(self, status: _Optional[int] = ..., mbrs: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_smbrs, _Mapping]]] = ...) -> None: ...

class pbreq_st_hforge(_message.Message):
    __slots__ = ("hids", "hero_id", "type")
    HIDS_FIELD_NUMBER: _ClassVar[int]
    HERO_ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    hids: _containers.RepeatedScalarFieldContainer[int]
    hero_id: int
    type: int
    def __init__(self, hids: _Optional[_Iterable[int]] = ..., hero_id: _Optional[int] = ..., type: _Optional[int] = ...) -> None: ...

class pbrsp_st_hforge(_message.Message):
    __slots__ = ("status", "heroes")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    HEROES_FIELD_NUMBER: _ClassVar[int]
    status: int
    heroes: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_hero]
    def __init__(self, status: _Optional[int] = ..., heroes: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_hero, _Mapping]]] = ...) -> None: ...

class pbreq_st_hattrup(_message.Message):
    __slots__ = ("hid", "id")
    HID_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    hid: int
    id: int
    def __init__(self, hid: _Optional[int] = ..., id: _Optional[int] = ...) -> None: ...

class pbrsp_st_hattrup(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_st_hattrchange(_message.Message):
    __slots__ = ("hid", "id", "attr_id")
    HID_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    ATTR_ID_FIELD_NUMBER: _ClassVar[int]
    hid: int
    id: int
    attr_id: int
    def __init__(self, hid: _Optional[int] = ..., id: _Optional[int] = ..., attr_id: _Optional[int] = ...) -> None: ...

class pbrsp_st_hattrchange(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_st_hattractivate(_message.Message):
    __slots__ = ("hid", "id", "src_hid")
    HID_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    SRC_HID_FIELD_NUMBER: _ClassVar[int]
    hid: int
    id: int
    src_hid: int
    def __init__(self, hid: _Optional[int] = ..., id: _Optional[int] = ..., src_hid: _Optional[int] = ...) -> None: ...

class pbrsp_st_hattractivate(_message.Message):
    __slots__ = ("status", "items")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    status: int
    items: _dr2_comm_pb_pb2.pb_bag
    def __init__(self, status: _Optional[int] = ..., items: _Optional[_Union[_dr2_comm_pb_pb2.pb_bag, _Mapping]] = ...) -> None: ...

class pbreq_st_vsync(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class pbrsp_st_vsync(_message.Message):
    __slots__ = ("status", "floor", "dty", "cd", "reward1", "buf1", "buf2", "reward2", "hids", "cells", "vit", "mid", "old_cells", "jw", "mdty", "cd2", "first", "svit", "mcard", "ps_dty", "ps_floor")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    FLOOR_FIELD_NUMBER: _ClassVar[int]
    DTY_FIELD_NUMBER: _ClassVar[int]
    CD_FIELD_NUMBER: _ClassVar[int]
    REWARD1_FIELD_NUMBER: _ClassVar[int]
    BUF1_FIELD_NUMBER: _ClassVar[int]
    BUF2_FIELD_NUMBER: _ClassVar[int]
    REWARD2_FIELD_NUMBER: _ClassVar[int]
    HIDS_FIELD_NUMBER: _ClassVar[int]
    CELLS_FIELD_NUMBER: _ClassVar[int]
    VIT_FIELD_NUMBER: _ClassVar[int]
    MID_FIELD_NUMBER: _ClassVar[int]
    OLD_CELLS_FIELD_NUMBER: _ClassVar[int]
    JW_FIELD_NUMBER: _ClassVar[int]
    MDTY_FIELD_NUMBER: _ClassVar[int]
    CD2_FIELD_NUMBER: _ClassVar[int]
    FIRST_FIELD_NUMBER: _ClassVar[int]
    SVIT_FIELD_NUMBER: _ClassVar[int]
    MCARD_FIELD_NUMBER: _ClassVar[int]
    PS_DTY_FIELD_NUMBER: _ClassVar[int]
    PS_FLOOR_FIELD_NUMBER: _ClassVar[int]
    status: int
    floor: int
    dty: int
    cd: int
    reward1: _dr2_comm_pb_pb2.pb_bag
    buf1: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_vbuff]
    buf2: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_vbuff]
    reward2: _dr2_comm_pb_pb2.pb_bag
    hids: _containers.RepeatedScalarFieldContainer[int]
    cells: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_scell]
    vit: int
    mid: int
    old_cells: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_scell]
    jw: _containers.RepeatedScalarFieldContainer[int]
    mdty: int
    cd2: int
    first: bool
    svit: int
    mcard: int
    ps_dty: int
    ps_floor: int
    def __init__(self, status: _Optional[int] = ..., floor: _Optional[int] = ..., dty: _Optional[int] = ..., cd: _Optional[int] = ..., reward1: _Optional[_Union[_dr2_comm_pb_pb2.pb_bag, _Mapping]] = ..., buf1: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_vbuff, _Mapping]]] = ..., buf2: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_vbuff, _Mapping]]] = ..., reward2: _Optional[_Union[_dr2_comm_pb_pb2.pb_bag, _Mapping]] = ..., hids: _Optional[_Iterable[int]] = ..., cells: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_scell, _Mapping]]] = ..., vit: _Optional[int] = ..., mid: _Optional[int] = ..., old_cells: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_scell, _Mapping]]] = ..., jw: _Optional[_Iterable[int]] = ..., mdty: _Optional[int] = ..., cd2: _Optional[int] = ..., first: _Optional[bool] = ..., svit: _Optional[int] = ..., mcard: _Optional[int] = ..., ps_dty: _Optional[int] = ..., ps_floor: _Optional[int] = ...) -> None: ...

class pbreq_st_vsync2(_message.Message):
    __slots__ = ("pos",)
    POS_FIELD_NUMBER: _ClassVar[int]
    pos: int
    def __init__(self, pos: _Optional[int] = ...) -> None: ...

class pbrsp_st_vsync2(_message.Message):
    __slots__ = ("status", "id", "events", "old_evts")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    EVENTS_FIELD_NUMBER: _ClassVar[int]
    OLD_EVTS_FIELD_NUMBER: _ClassVar[int]
    status: int
    id: int
    events: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_scell]
    old_evts: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_scell]
    def __init__(self, status: _Optional[int] = ..., id: _Optional[int] = ..., events: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_scell, _Mapping]]] = ..., old_evts: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_scell, _Mapping]]] = ...) -> None: ...

class pbreq_st_vevent(_message.Message):
    __slots__ = ("pos", "ids", "camp", "tid")
    POS_FIELD_NUMBER: _ClassVar[int]
    IDS_FIELD_NUMBER: _ClassVar[int]
    CAMP_FIELD_NUMBER: _ClassVar[int]
    TID_FIELD_NUMBER: _ClassVar[int]
    pos: int
    ids: _containers.RepeatedScalarFieldContainer[int]
    camp: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_unit]
    tid: int
    def __init__(self, pos: _Optional[int] = ..., ids: _Optional[_Iterable[int]] = ..., camp: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_unit, _Mapping]]] = ..., tid: _Optional[int] = ...) -> None: ...

class pbrsp_st_vevent(_message.Message):
    __slots__ = ("status", "video", "ids", "hps", "new_evt", "flag")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    VIDEO_FIELD_NUMBER: _ClassVar[int]
    IDS_FIELD_NUMBER: _ClassVar[int]
    HPS_FIELD_NUMBER: _ClassVar[int]
    NEW_EVT_FIELD_NUMBER: _ClassVar[int]
    FLAG_FIELD_NUMBER: _ClassVar[int]
    status: int
    video: _dr2_comm_pb_pb2.pb_evideo
    ids: _containers.RepeatedScalarFieldContainer[int]
    hps: _containers.RepeatedScalarFieldContainer[int]
    new_evt: _dr2_comm_pb_pb2.pb_scell
    flag: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, status: _Optional[int] = ..., video: _Optional[_Union[_dr2_comm_pb_pb2.pb_evideo, _Mapping]] = ..., ids: _Optional[_Iterable[int]] = ..., hps: _Optional[_Iterable[int]] = ..., new_evt: _Optional[_Union[_dr2_comm_pb_pb2.pb_scell, _Mapping]] = ..., flag: _Optional[_Iterable[int]] = ...) -> None: ...

class pbreq_st_vdiff(_message.Message):
    __slots__ = ("diff",)
    DIFF_FIELD_NUMBER: _ClassVar[int]
    diff: int
    def __init__(self, diff: _Optional[int] = ...) -> None: ...

class pbrsp_st_vdiff(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_st_heartresolve(_message.Message):
    __slots__ = ("ids",)
    IDS_FIELD_NUMBER: _ClassVar[int]
    ids: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, ids: _Optional[_Iterable[int]] = ...) -> None: ...

class pbrsp_st_heartresolve(_message.Message):
    __slots__ = ("status", "items")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    status: int
    items: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_item]
    def __init__(self, status: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_item, _Mapping]]] = ...) -> None: ...

class pbreq_st_vwipe(_message.Message):
    __slots__ = ("poslist", "camp", "tid", "hids")
    POSLIST_FIELD_NUMBER: _ClassVar[int]
    CAMP_FIELD_NUMBER: _ClassVar[int]
    TID_FIELD_NUMBER: _ClassVar[int]
    HIDS_FIELD_NUMBER: _ClassVar[int]
    poslist: _containers.RepeatedScalarFieldContainer[int]
    camp: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_unit]
    tid: int
    hids: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, poslist: _Optional[_Iterable[int]] = ..., camp: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_unit, _Mapping]]] = ..., tid: _Optional[int] = ..., hids: _Optional[_Iterable[int]] = ...) -> None: ...

class pbrsp_st_vwipe(_message.Message):
    __slots__ = ("status", "cd", "qtask", "reward", "buf1", "svit", "flag")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    CD_FIELD_NUMBER: _ClassVar[int]
    QTASK_FIELD_NUMBER: _ClassVar[int]
    REWARD_FIELD_NUMBER: _ClassVar[int]
    BUF1_FIELD_NUMBER: _ClassVar[int]
    SVIT_FIELD_NUMBER: _ClassVar[int]
    FLAG_FIELD_NUMBER: _ClassVar[int]
    status: int
    cd: int
    qtask: int
    reward: _dr2_comm_pb_pb2.pb_bag
    buf1: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_vbuff]
    svit: int
    flag: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, status: _Optional[int] = ..., cd: _Optional[int] = ..., qtask: _Optional[int] = ..., reward: _Optional[_Union[_dr2_comm_pb_pb2.pb_bag, _Mapping]] = ..., buf1: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_vbuff, _Mapping]]] = ..., svit: _Optional[int] = ..., flag: _Optional[_Iterable[int]] = ...) -> None: ...

class pbreq_st_vuseitem(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class pbrsp_st_vuseitem(_message.Message):
    __slots__ = ("status", "pos")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    POS_FIELD_NUMBER: _ClassVar[int]
    status: int
    pos: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, status: _Optional[int] = ..., pos: _Optional[_Iterable[int]] = ...) -> None: ...

class pbreq_st_esync(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class pbrsp_st_esync(_message.Message):
    __slots__ = ("status", "cd", "dups", "vit", "vit_num", "vit_cd", "buy_num", "item_bnum", "item_rnum", "red_dot", "reward", "sweep_time")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    CD_FIELD_NUMBER: _ClassVar[int]
    DUPS_FIELD_NUMBER: _ClassVar[int]
    VIT_FIELD_NUMBER: _ClassVar[int]
    VIT_NUM_FIELD_NUMBER: _ClassVar[int]
    VIT_CD_FIELD_NUMBER: _ClassVar[int]
    BUY_NUM_FIELD_NUMBER: _ClassVar[int]
    ITEM_BNUM_FIELD_NUMBER: _ClassVar[int]
    ITEM_RNUM_FIELD_NUMBER: _ClassVar[int]
    RED_DOT_FIELD_NUMBER: _ClassVar[int]
    REWARD_FIELD_NUMBER: _ClassVar[int]
    SWEEP_TIME_FIELD_NUMBER: _ClassVar[int]
    status: int
    cd: int
    dups: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_dup]
    vit: int
    vit_num: int
    vit_cd: int
    buy_num: int
    item_bnum: int
    item_rnum: int
    red_dot: int
    reward: _dr2_comm_pb_pb2.pb_bag
    sweep_time: int
    def __init__(self, status: _Optional[int] = ..., cd: _Optional[int] = ..., dups: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_dup, _Mapping]]] = ..., vit: _Optional[int] = ..., vit_num: _Optional[int] = ..., vit_cd: _Optional[int] = ..., buy_num: _Optional[int] = ..., item_bnum: _Optional[int] = ..., item_rnum: _Optional[int] = ..., red_dot: _Optional[int] = ..., reward: _Optional[_Union[_dr2_comm_pb_pb2.pb_bag, _Mapping]] = ..., sweep_time: _Optional[int] = ...) -> None: ...

class pbreq_st_ebuy(_message.Message):
    __slots__ = ("id", "num")
    ID_FIELD_NUMBER: _ClassVar[int]
    NUM_FIELD_NUMBER: _ClassVar[int]
    id: int
    num: int
    def __init__(self, id: _Optional[int] = ..., num: _Optional[int] = ...) -> None: ...

class pbrsp_st_ebuy(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_st_euse(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class pbrsp_st_euse(_message.Message):
    __slots__ = ("status", "id")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    status: int
    id: int
    def __init__(self, status: _Optional[int] = ..., id: _Optional[int] = ...) -> None: ...

class pbreq_st_efight(_message.Message):
    __slots__ = ("camp", "id", "tid")
    CAMP_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    TID_FIELD_NUMBER: _ClassVar[int]
    camp: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_unit]
    id: int
    tid: int
    def __init__(self, camp: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_unit, _Mapping]]] = ..., id: _Optional[int] = ..., tid: _Optional[int] = ...) -> None: ...

class pbrsp_st_efight(_message.Message):
    __slots__ = ("status", "video", "num")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    VIDEO_FIELD_NUMBER: _ClassVar[int]
    NUM_FIELD_NUMBER: _ClassVar[int]
    status: int
    video: _dr2_comm_pb_pb2.pb_evideo
    num: int
    def __init__(self, status: _Optional[int] = ..., video: _Optional[_Union[_dr2_comm_pb_pb2.pb_evideo, _Mapping]] = ..., num: _Optional[int] = ...) -> None: ...

class pbreq_st_erank1(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class pbrsp_st_erank1(_message.Message):
    __slots__ = ("status", "mbrs")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MBRS_FIELD_NUMBER: _ClassVar[int]
    status: int
    mbrs: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_embr]
    def __init__(self, status: _Optional[int] = ..., mbrs: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_embr, _Mapping]]] = ...) -> None: ...

class pbreq_st_erank2(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class pbrsp_st_erank2(_message.Message):
    __slots__ = ("status", "mbrs")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MBRS_FIELD_NUMBER: _ClassVar[int]
    status: int
    mbrs: _dr2_comm_pb_pb2.pb_smbrs
    def __init__(self, status: _Optional[int] = ..., mbrs: _Optional[_Union[_dr2_comm_pb_pb2.pb_smbrs, _Mapping]] = ...) -> None: ...

class pbreq_st_eget(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class pbrsp_st_eget(_message.Message):
    __slots__ = ("status", "reward")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    REWARD_FIELD_NUMBER: _ClassVar[int]
    status: int
    reward: _dr2_comm_pb_pb2.pb_bag
    def __init__(self, status: _Optional[int] = ..., reward: _Optional[_Union[_dr2_comm_pb_pb2.pb_bag, _Mapping]] = ...) -> None: ...

class pbreq_st_eopen(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class pbrsp_st_eopen(_message.Message):
    __slots__ = ("status", "dups")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    DUPS_FIELD_NUMBER: _ClassVar[int]
    status: int
    dups: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_dup]
    def __init__(self, status: _Optional[int] = ..., dups: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_dup, _Mapping]]] = ...) -> None: ...

class pbreq_st_async(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class pbrsp_st_async(_message.Message):
    __slots__ = ("status", "vdot", "edot", "eopen", "tdot", "sdot")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    VDOT_FIELD_NUMBER: _ClassVar[int]
    EDOT_FIELD_NUMBER: _ClassVar[int]
    EOPEN_FIELD_NUMBER: _ClassVar[int]
    TDOT_FIELD_NUMBER: _ClassVar[int]
    SDOT_FIELD_NUMBER: _ClassVar[int]
    status: int
    vdot: int
    edot: int
    eopen: int
    tdot: int
    sdot: int
    def __init__(self, status: _Optional[int] = ..., vdot: _Optional[int] = ..., edot: _Optional[int] = ..., eopen: _Optional[int] = ..., tdot: _Optional[int] = ..., sdot: _Optional[int] = ...) -> None: ...

class pbreq_st_erefresh(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class pbrsp_st_erefresh(_message.Message):
    __slots__ = ("status", "dup")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    DUP_FIELD_NUMBER: _ClassVar[int]
    status: int
    dup: _dr2_comm_pb_pb2.pb_dup
    def __init__(self, status: _Optional[int] = ..., dup: _Optional[_Union[_dr2_comm_pb_pb2.pb_dup, _Mapping]] = ...) -> None: ...

class pbreq_st_hattrreset(_message.Message):
    __slots__ = ("hid",)
    HID_FIELD_NUMBER: _ClassVar[int]
    hid: int
    def __init__(self, hid: _Optional[int] = ...) -> None: ...

class pbrsp_st_hattrreset(_message.Message):
    __slots__ = ("status", "heroes", "items")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    HEROES_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    status: int
    heroes: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_hero]
    items: _dr2_comm_pb_pb2.pb_bag
    def __init__(self, status: _Optional[int] = ..., heroes: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_hero, _Mapping]]] = ..., items: _Optional[_Union[_dr2_comm_pb_pb2.pb_bag, _Mapping]] = ...) -> None: ...

class pbreq_st_tback(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class pbrsp_st_tback(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_st_changenight(_message.Message):
    __slots__ = ("flag",)
    FLAG_FIELD_NUMBER: _ClassVar[int]
    flag: int
    def __init__(self, flag: _Optional[int] = ...) -> None: ...

class pbrsp_st_changenight(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_st_starresolve(_message.Message):
    __slots__ = ("num", "flag")
    NUM_FIELD_NUMBER: _ClassVar[int]
    FLAG_FIELD_NUMBER: _ClassVar[int]
    num: int
    flag: int
    def __init__(self, num: _Optional[int] = ..., flag: _Optional[int] = ...) -> None: ...

class pbrsp_st_starresolve(_message.Message):
    __slots__ = ("status", "items")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    status: int
    items: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_item]
    def __init__(self, status: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_item, _Mapping]]] = ...) -> None: ...

class pbreq_stower_sync(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class pbrsp_stower_sync(_message.Message):
    __slots__ = ("status", "hatch", "egg_id", "count", "breed", "pcount", "pic")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    HATCH_FIELD_NUMBER: _ClassVar[int]
    EGG_ID_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    BREED_FIELD_NUMBER: _ClassVar[int]
    PCOUNT_FIELD_NUMBER: _ClassVar[int]
    PIC_FIELD_NUMBER: _ClassVar[int]
    status: int
    hatch: int
    egg_id: int
    count: int
    breed: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.stower_breed]
    pcount: int
    pic: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, status: _Optional[int] = ..., hatch: _Optional[int] = ..., egg_id: _Optional[int] = ..., count: _Optional[int] = ..., breed: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.stower_breed, _Mapping]]] = ..., pcount: _Optional[int] = ..., pic: _Optional[_Iterable[int]] = ...) -> None: ...

class pbreq_stower_up(_message.Message):
    __slots__ = ("lv",)
    LV_FIELD_NUMBER: _ClassVar[int]
    lv: int
    def __init__(self, lv: _Optional[int] = ...) -> None: ...

class pbrsp_stower_up(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_stower_hatch(_message.Message):
    __slots__ = ("egg_id",)
    EGG_ID_FIELD_NUMBER: _ClassVar[int]
    egg_id: int
    def __init__(self, egg_id: _Optional[int] = ...) -> None: ...

class pbrsp_stower_hatch(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_stower_hover(_message.Message):
    __slots__ = ("type", "rmb")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    RMB_FIELD_NUMBER: _ClassVar[int]
    type: int
    rmb: int
    def __init__(self, type: _Optional[int] = ..., rmb: _Optional[int] = ...) -> None: ...

class pbrsp_stower_hover(_message.Message):
    __slots__ = ("status", "id", "reward")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    REWARD_FIELD_NUMBER: _ClassVar[int]
    status: int
    id: int
    reward: _dr2_comm_pb_pb2.pb_bag
    def __init__(self, status: _Optional[int] = ..., id: _Optional[int] = ..., reward: _Optional[_Union[_dr2_comm_pb_pb2.pb_bag, _Mapping]] = ...) -> None: ...

class pbreq_spet_up(_message.Message):
    __slots__ = ("id", "type")
    ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    id: int
    type: int
    def __init__(self, id: _Optional[int] = ..., type: _Optional[int] = ...) -> None: ...

class pbrsp_spet_up(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_st_ssync(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class pbrsp_st_ssync(_message.Message):
    __slots__ = ("status", "cd", "g_num", "lv_item", "map_id", "map_lv", "collect", "vit", "skl", "map_cur_lv", "rank", "flag", "map_dot", "reward_lv_item")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    CD_FIELD_NUMBER: _ClassVar[int]
    G_NUM_FIELD_NUMBER: _ClassVar[int]
    LV_ITEM_FIELD_NUMBER: _ClassVar[int]
    MAP_ID_FIELD_NUMBER: _ClassVar[int]
    MAP_LV_FIELD_NUMBER: _ClassVar[int]
    COLLECT_FIELD_NUMBER: _ClassVar[int]
    VIT_FIELD_NUMBER: _ClassVar[int]
    SKL_FIELD_NUMBER: _ClassVar[int]
    MAP_CUR_LV_FIELD_NUMBER: _ClassVar[int]
    RANK_FIELD_NUMBER: _ClassVar[int]
    FLAG_FIELD_NUMBER: _ClassVar[int]
    MAP_DOT_FIELD_NUMBER: _ClassVar[int]
    REWARD_LV_ITEM_FIELD_NUMBER: _ClassVar[int]
    status: int
    cd: int
    g_num: int
    lv_item: int
    map_id: int
    map_lv: int
    collect: _dr2_comm_pb_pb2.pb_sbuilding
    vit: _dr2_comm_pb_pb2.pb_sbuilding
    skl: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_gskl]
    map_cur_lv: int
    rank: int
    flag: bool
    map_dot: int
    reward_lv_item: int
    def __init__(self, status: _Optional[int] = ..., cd: _Optional[int] = ..., g_num: _Optional[int] = ..., lv_item: _Optional[int] = ..., map_id: _Optional[int] = ..., map_lv: _Optional[int] = ..., collect: _Optional[_Union[_dr2_comm_pb_pb2.pb_sbuilding, _Mapping]] = ..., vit: _Optional[_Union[_dr2_comm_pb_pb2.pb_sbuilding, _Mapping]] = ..., skl: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_gskl, _Mapping]]] = ..., map_cur_lv: _Optional[int] = ..., rank: _Optional[int] = ..., flag: _Optional[bool] = ..., map_dot: _Optional[int] = ..., reward_lv_item: _Optional[int] = ...) -> None: ...

class pbreq_st_slvup(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class pbrsp_st_slvup(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_st_ssweep(_message.Message):
    __slots__ = ("list", "camp", "flag", "tid")
    LIST_FIELD_NUMBER: _ClassVar[int]
    CAMP_FIELD_NUMBER: _ClassVar[int]
    FLAG_FIELD_NUMBER: _ClassVar[int]
    TID_FIELD_NUMBER: _ClassVar[int]
    list: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_sssweep]
    camp: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_unit]
    flag: bool
    tid: int
    def __init__(self, list: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_sssweep, _Mapping]]] = ..., camp: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_unit, _Mapping]]] = ..., flag: _Optional[bool] = ..., tid: _Optional[int] = ...) -> None: ...

class pbrsp_st_ssweep(_message.Message):
    __slots__ = ("status", "reward", "event")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    REWARD_FIELD_NUMBER: _ClassVar[int]
    EVENT_FIELD_NUMBER: _ClassVar[int]
    status: int
    reward: _dr2_comm_pb_pb2.pb_bag
    event: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_ssevent]
    def __init__(self, status: _Optional[int] = ..., reward: _Optional[_Union[_dr2_comm_pb_pb2.pb_bag, _Mapping]] = ..., event: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_ssevent, _Mapping]]] = ...) -> None: ...

class pbreq_st_ssklup(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class pbrsp_st_ssklup(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_st_sstore(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class pbrsp_st_sstore(_message.Message):
    __slots__ = ("status", "good")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    GOOD_FIELD_NUMBER: _ClassVar[int]
    status: int
    good: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_gmarket]
    def __init__(self, status: _Optional[int] = ..., good: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_gmarket, _Mapping]]] = ...) -> None: ...

class pbreq_st_sbuy(_message.Message):
    __slots__ = ("id", "num")
    ID_FIELD_NUMBER: _ClassVar[int]
    NUM_FIELD_NUMBER: _ClassVar[int]
    id: int
    num: int
    def __init__(self, id: _Optional[int] = ..., num: _Optional[int] = ...) -> None: ...

class pbrsp_st_sbuy(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_st_smap_unlock(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class pbrsp_st_smap_unlock(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_st_smap_sync(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class pbrsp_st_smap_sync(_message.Message):
    __slots__ = ("status", "line_id", "lv_item", "hids", "reward", "cells", "team", "event", "rob_num", "mcard")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    LINE_ID_FIELD_NUMBER: _ClassVar[int]
    LV_ITEM_FIELD_NUMBER: _ClassVar[int]
    HIDS_FIELD_NUMBER: _ClassVar[int]
    REWARD_FIELD_NUMBER: _ClassVar[int]
    CELLS_FIELD_NUMBER: _ClassVar[int]
    TEAM_FIELD_NUMBER: _ClassVar[int]
    EVENT_FIELD_NUMBER: _ClassVar[int]
    ROB_NUM_FIELD_NUMBER: _ClassVar[int]
    MCARD_FIELD_NUMBER: _ClassVar[int]
    status: int
    line_id: int
    lv_item: int
    hids: _containers.RepeatedScalarFieldContainer[int]
    reward: _dr2_comm_pb_pb2.pb_bag
    cells: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_sscell]
    team: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_unit]
    event: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_ssevent]
    rob_num: int
    mcard: int
    def __init__(self, status: _Optional[int] = ..., line_id: _Optional[int] = ..., lv_item: _Optional[int] = ..., hids: _Optional[_Iterable[int]] = ..., reward: _Optional[_Union[_dr2_comm_pb_pb2.pb_bag, _Mapping]] = ..., cells: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_sscell, _Mapping]]] = ..., team: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_unit, _Mapping]]] = ..., event: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_ssevent, _Mapping]]] = ..., rob_num: _Optional[int] = ..., mcard: _Optional[int] = ...) -> None: ...

class pbreq_st_scell_unlock(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class pbrsp_st_scell_unlock(_message.Message):
    __slots__ = ("status", "lv_item", "cell", "reward")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    LV_ITEM_FIELD_NUMBER: _ClassVar[int]
    CELL_FIELD_NUMBER: _ClassVar[int]
    REWARD_FIELD_NUMBER: _ClassVar[int]
    status: int
    lv_item: int
    cell: _dr2_comm_pb_pb2.pb_sscell
    reward: _dr2_comm_pb_pb2.pb_bag
    def __init__(self, status: _Optional[int] = ..., lv_item: _Optional[int] = ..., cell: _Optional[_Union[_dr2_comm_pb_pb2.pb_sscell, _Mapping]] = ..., reward: _Optional[_Union[_dr2_comm_pb_pb2.pb_bag, _Mapping]] = ...) -> None: ...

class pbreq_st_scell_disp(_message.Message):
    __slots__ = ("id", "hid")
    ID_FIELD_NUMBER: _ClassVar[int]
    HID_FIELD_NUMBER: _ClassVar[int]
    id: int
    hid: int
    def __init__(self, id: _Optional[int] = ..., hid: _Optional[int] = ...) -> None: ...

class pbrsp_st_scell_disp(_message.Message):
    __slots__ = ("status", "cd")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    CD_FIELD_NUMBER: _ClassVar[int]
    status: int
    cd: int
    def __init__(self, status: _Optional[int] = ..., cd: _Optional[int] = ...) -> None: ...

class pbreq_st_scell_fight(_message.Message):
    __slots__ = ("id", "camp", "tid")
    ID_FIELD_NUMBER: _ClassVar[int]
    CAMP_FIELD_NUMBER: _ClassVar[int]
    TID_FIELD_NUMBER: _ClassVar[int]
    id: int
    camp: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_unit]
    tid: int
    def __init__(self, id: _Optional[int] = ..., camp: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_unit, _Mapping]]] = ..., tid: _Optional[int] = ...) -> None: ...

class pbrsp_st_scell_fight(_message.Message):
    __slots__ = ("status", "cd", "lv_item", "boss_hp", "video")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    CD_FIELD_NUMBER: _ClassVar[int]
    LV_ITEM_FIELD_NUMBER: _ClassVar[int]
    BOSS_HP_FIELD_NUMBER: _ClassVar[int]
    VIDEO_FIELD_NUMBER: _ClassVar[int]
    status: int
    cd: int
    lv_item: int
    boss_hp: _containers.RepeatedScalarFieldContainer[int]
    video: _dr2_comm_pb_pb2.pb_pvideo
    def __init__(self, status: _Optional[int] = ..., cd: _Optional[int] = ..., lv_item: _Optional[int] = ..., boss_hp: _Optional[_Iterable[int]] = ..., video: _Optional[_Union[_dr2_comm_pb_pb2.pb_pvideo, _Mapping]] = ...) -> None: ...

class pbreq_st_smap_sett(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class pbrsp_st_smap_sett(_message.Message):
    __slots__ = ("status", "event", "sett")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    EVENT_FIELD_NUMBER: _ClassVar[int]
    SETT_FIELD_NUMBER: _ClassVar[int]
    status: int
    event: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_ssevent]
    sett: int
    def __init__(self, status: _Optional[int] = ..., event: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_ssevent, _Mapping]]] = ..., sett: _Optional[int] = ...) -> None: ...

class pbreq_st_smap_team(_message.Message):
    __slots__ = ("camp", "tid")
    CAMP_FIELD_NUMBER: _ClassVar[int]
    TID_FIELD_NUMBER: _ClassVar[int]
    camp: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_unit]
    tid: int
    def __init__(self, camp: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_unit, _Mapping]]] = ..., tid: _Optional[int] = ...) -> None: ...

class pbrsp_st_smap_team(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_st_smap_rank(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class pbrsp_st_smap_rank(_message.Message):
    __slots__ = ("status", "rank", "score", "members")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    RANK_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    MEMBERS_FIELD_NUMBER: _ClassVar[int]
    status: int
    rank: int
    score: int
    members: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_p3pmbr]
    def __init__(self, status: _Optional[int] = ..., rank: _Optional[int] = ..., score: _Optional[int] = ..., members: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_p3pmbr, _Mapping]]] = ...) -> None: ...

class pbreq_st_smap_mbr(_message.Message):
    __slots__ = ("uid",)
    UID_FIELD_NUMBER: _ClassVar[int]
    uid: int
    def __init__(self, uid: _Optional[int] = ...) -> None: ...

class pbrsp_st_smap_mbr(_message.Message):
    __slots__ = ("status", "mbr")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MBR_FIELD_NUMBER: _ClassVar[int]
    status: int
    mbr: _dr2_comm_pb_pb2.pb_pmbr
    def __init__(self, status: _Optional[int] = ..., mbr: _Optional[_Union[_dr2_comm_pb_pb2.pb_pmbr, _Mapping]] = ...) -> None: ...

class pbreq_st_sclick(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class pbrsp_st_sclick(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_st_hchange(_message.Message):
    __slots__ = ("hostHid", "hid")
    HOSTHID_FIELD_NUMBER: _ClassVar[int]
    HID_FIELD_NUMBER: _ClassVar[int]
    hostHid: int
    hid: int
    def __init__(self, hostHid: _Optional[int] = ..., hid: _Optional[int] = ...) -> None: ...

class pbrsp_st_hchange(_message.Message):
    __slots__ = ("status", "heroes", "items")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    HEROES_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    status: int
    heroes: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_hero]
    items: _dr2_comm_pb_pb2.pb_bag
    def __init__(self, status: _Optional[int] = ..., heroes: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_hero, _Mapping]]] = ..., items: _Optional[_Union[_dr2_comm_pb_pb2.pb_bag, _Mapping]] = ...) -> None: ...

class pbreq_spet_reset(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class pbrsp_spet_reset(_message.Message):
    __slots__ = ("status", "reward")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    REWARD_FIELD_NUMBER: _ClassVar[int]
    status: int
    reward: _dr2_comm_pb_pb2.pb_bag
    def __init__(self, status: _Optional[int] = ..., reward: _Optional[_Union[_dr2_comm_pb_pb2.pb_bag, _Mapping]] = ...) -> None: ...

class pbreq_spet_breed(_message.Message):
    __slots__ = ("pid1", "pid2", "egg", "id")
    PID1_FIELD_NUMBER: _ClassVar[int]
    PID2_FIELD_NUMBER: _ClassVar[int]
    EGG_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    pid1: int
    pid2: int
    egg: int
    id: int
    def __init__(self, pid1: _Optional[int] = ..., pid2: _Optional[int] = ..., egg: _Optional[int] = ..., id: _Optional[int] = ...) -> None: ...

class pbrsp_spet_breed(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_stower_bover(_message.Message):
    __slots__ = ("type", "rmb", "id")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    RMB_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    type: int
    rmb: int
    id: int
    def __init__(self, type: _Optional[int] = ..., rmb: _Optional[int] = ..., id: _Optional[int] = ...) -> None: ...

class pbrsp_stower_bover(_message.Message):
    __slots__ = ("status", "id", "reward", "pic")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    REWARD_FIELD_NUMBER: _ClassVar[int]
    PIC_FIELD_NUMBER: _ClassVar[int]
    status: int
    id: int
    reward: _dr2_comm_pb_pb2.pb_bag
    pic: int
    def __init__(self, status: _Optional[int] = ..., id: _Optional[int] = ..., reward: _Optional[_Union[_dr2_comm_pb_pb2.pb_bag, _Mapping]] = ..., pic: _Optional[int] = ...) -> None: ...

class pbreq_stower_lucky(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class pbrsp_stower_lucky(_message.Message):
    __slots__ = ("status", "ratio")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    RATIO_FIELD_NUMBER: _ClassVar[int]
    status: int
    ratio: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, status: _Optional[int] = ..., ratio: _Optional[_Iterable[int]] = ...) -> None: ...

class pbreq_stower_sure(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class pbrsp_stower_sure(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_stower_cookie(_message.Message):
    __slots__ = ("num", "item")
    NUM_FIELD_NUMBER: _ClassVar[int]
    ITEM_FIELD_NUMBER: _ClassVar[int]
    num: int
    item: int
    def __init__(self, num: _Optional[int] = ..., item: _Optional[int] = ...) -> None: ...

class pbrsp_stower_cookie(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_ntask_sync(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class pbrsp_ntask_sync(_message.Message):
    __slots__ = ("status", "tasks", "data")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    TASKS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    status: int
    tasks: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_ntask]
    data: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_nt_sync]
    def __init__(self, status: _Optional[int] = ..., tasks: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_ntask, _Mapping]]] = ..., data: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_nt_sync, _Mapping]]] = ...) -> None: ...

class pbreq_ntask_claim(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class pbrsp_ntask_claim(_message.Message):
    __slots__ = ("status", "items")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    status: int
    items: _dr2_comm_pb_pb2.pb_bag
    def __init__(self, status: _Optional[int] = ..., items: _Optional[_Union[_dr2_comm_pb_pb2.pb_bag, _Mapping]] = ...) -> None: ...

class pbreq_ntask_market(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class pbrsp_ntask_market(_message.Message):
    __slots__ = ("status", "kv")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    KV_FIELD_NUMBER: _ClassVar[int]
    status: int
    kv: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_kv]
    def __init__(self, status: _Optional[int] = ..., kv: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_kv, _Mapping]]] = ...) -> None: ...

class pbreq_ntask_market_buy(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class pbrsp_ntask_market_buy(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_team_info(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class pbrsp_team_info(_message.Message):
    __slots__ = ("status", "infos", "mid")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    INFOS_FIELD_NUMBER: _ClassVar[int]
    MID_FIELD_NUMBER: _ClassVar[int]
    status: int
    infos: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_team_info]
    mid: int
    def __init__(self, status: _Optional[int] = ..., infos: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_team_info, _Mapping]]] = ..., mid: _Optional[int] = ...) -> None: ...

class pbreq_team_change_name(_message.Message):
    __slots__ = ("id", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ...) -> None: ...

class pbrsp_team_change_name(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_team_unlock(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class pbrsp_team_unlock(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_team_save(_message.Message):
    __slots__ = ("id", "heroes", "petid")
    ID_FIELD_NUMBER: _ClassVar[int]
    HEROES_FIELD_NUMBER: _ClassVar[int]
    PETID_FIELD_NUMBER: _ClassVar[int]
    id: int
    heroes: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_team_hero]
    petid: int
    def __init__(self, id: _Optional[int] = ..., heroes: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_team_hero, _Mapping]]] = ..., petid: _Optional[int] = ...) -> None: ...

class pbrsp_team_save(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_shop_sync(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class pbrsp_shop_sync(_message.Message):
    __slots__ = ("status", "top", "join_hot", "price_hot", "boom", "give_cd", "sell_cd", "buy_cd")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    TOP_FIELD_NUMBER: _ClassVar[int]
    JOIN_HOT_FIELD_NUMBER: _ClassVar[int]
    PRICE_HOT_FIELD_NUMBER: _ClassVar[int]
    BOOM_FIELD_NUMBER: _ClassVar[int]
    GIVE_CD_FIELD_NUMBER: _ClassVar[int]
    SELL_CD_FIELD_NUMBER: _ClassVar[int]
    BUY_CD_FIELD_NUMBER: _ClassVar[int]
    status: int
    top: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.good]
    join_hot: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.good]
    price_hot: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.good]
    boom: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.mall_log]
    give_cd: int
    sell_cd: int
    buy_cd: int
    def __init__(self, status: _Optional[int] = ..., top: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.good, _Mapping]]] = ..., join_hot: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.good, _Mapping]]] = ..., price_hot: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.good, _Mapping]]] = ..., boom: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.mall_log, _Mapping]]] = ..., give_cd: _Optional[int] = ..., sell_cd: _Optional[int] = ..., buy_cd: _Optional[int] = ...) -> None: ...

class pbreq_shop_show_sync(_message.Message):
    __slots__ = ("type", "condition_camp", "condition_qlt", "condition_price_min", "condition_price_max", "condition_hero_id", "sort")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    CONDITION_CAMP_FIELD_NUMBER: _ClassVar[int]
    CONDITION_QLT_FIELD_NUMBER: _ClassVar[int]
    CONDITION_PRICE_MIN_FIELD_NUMBER: _ClassVar[int]
    CONDITION_PRICE_MAX_FIELD_NUMBER: _ClassVar[int]
    CONDITION_HERO_ID_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    type: int
    condition_camp: _containers.RepeatedScalarFieldContainer[int]
    condition_qlt: _containers.RepeatedScalarFieldContainer[int]
    condition_price_min: int
    condition_price_max: int
    condition_hero_id: _containers.RepeatedScalarFieldContainer[int]
    sort: int
    def __init__(self, type: _Optional[int] = ..., condition_camp: _Optional[_Iterable[int]] = ..., condition_qlt: _Optional[_Iterable[int]] = ..., condition_price_min: _Optional[int] = ..., condition_price_max: _Optional[int] = ..., condition_hero_id: _Optional[_Iterable[int]] = ..., sort: _Optional[int] = ...) -> None: ...

class pbrsp_shop_show_sync(_message.Message):
    __slots__ = ("status", "goods", "booth")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    GOODS_FIELD_NUMBER: _ClassVar[int]
    BOOTH_FIELD_NUMBER: _ClassVar[int]
    status: int
    goods: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.good]
    booth: int
    def __init__(self, status: _Optional[int] = ..., goods: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.good, _Mapping]]] = ..., booth: _Optional[int] = ...) -> None: ...

class pbreq_shop_update_cart(_message.Message):
    __slots__ = ("op_type", "goodid", "price", "del_price", "heroid", "hide")
    OP_TYPE_FIELD_NUMBER: _ClassVar[int]
    GOODID_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    DEL_PRICE_FIELD_NUMBER: _ClassVar[int]
    HEROID_FIELD_NUMBER: _ClassVar[int]
    HIDE_FIELD_NUMBER: _ClassVar[int]
    op_type: int
    goodid: int
    price: int
    del_price: int
    heroid: int
    hide: int
    def __init__(self, op_type: _Optional[int] = ..., goodid: _Optional[int] = ..., price: _Optional[int] = ..., del_price: _Optional[int] = ..., heroid: _Optional[int] = ..., hide: _Optional[int] = ...) -> None: ...

class pbrsp_shop_update_cart(_message.Message):
    __slots__ = ("status", "general", "hero", "rewards", "sell_cd", "buy_cd")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    GENERAL_FIELD_NUMBER: _ClassVar[int]
    HERO_FIELD_NUMBER: _ClassVar[int]
    REWARDS_FIELD_NUMBER: _ClassVar[int]
    SELL_CD_FIELD_NUMBER: _ClassVar[int]
    BUY_CD_FIELD_NUMBER: _ClassVar[int]
    status: int
    general: int
    hero: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_hero]
    rewards: _dr2_comm_pb_pb2.pb_bag
    sell_cd: int
    buy_cd: int
    def __init__(self, status: _Optional[int] = ..., general: _Optional[int] = ..., hero: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_hero, _Mapping]]] = ..., rewards: _Optional[_Union[_dr2_comm_pb_pb2.pb_bag, _Mapping]] = ..., sell_cd: _Optional[int] = ..., buy_cd: _Optional[int] = ...) -> None: ...

class pbreq_shop_get_price(_message.Message):
    __slots__ = ("hero_id", "qlt")
    HERO_ID_FIELD_NUMBER: _ClassVar[int]
    QLT_FIELD_NUMBER: _ClassVar[int]
    hero_id: int
    qlt: _dr2_comm_pb_pb2.pb_hero_qlc
    def __init__(self, hero_id: _Optional[int] = ..., qlt: _Optional[_Union[_dr2_comm_pb_pb2.pb_hero_qlc, _Mapping]] = ...) -> None: ...

class pbrsp_shop_get_price(_message.Message):
    __slots__ = ("status", "price", "history")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    HISTORY_FIELD_NUMBER: _ClassVar[int]
    status: int
    price: int
    history: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, status: _Optional[int] = ..., price: _Optional[int] = ..., history: _Optional[_Iterable[int]] = ...) -> None: ...

class pbreq_shop_update_status(_message.Message):
    __slots__ = ("good_id",)
    GOOD_ID_FIELD_NUMBER: _ClassVar[int]
    good_id: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, good_id: _Optional[_Iterable[int]] = ...) -> None: ...

class pbrsp_shop_update_status(_message.Message):
    __slots__ = ("status", "good", "history")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    GOOD_FIELD_NUMBER: _ClassVar[int]
    HISTORY_FIELD_NUMBER: _ClassVar[int]
    status: int
    good: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.good]
    history: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, status: _Optional[int] = ..., good: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.good, _Mapping]]] = ..., history: _Optional[_Iterable[int]] = ...) -> None: ...

class pbreq_shop_history(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class pbrsp_shop_history(_message.Message):
    __slots__ = ("status", "log")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    LOG_FIELD_NUMBER: _ClassVar[int]
    status: int
    log: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.mall_log]
    def __init__(self, status: _Optional[int] = ..., log: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.mall_log, _Mapping]]] = ...) -> None: ...

class pbreq_shop_red_dot(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class pbrsp_shop_red_dot(_message.Message):
    __slots__ = ("status", "log")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    LOG_FIELD_NUMBER: _ClassVar[int]
    status: int
    log: _dr2_comm_pb_pb2.mall_log
    def __init__(self, status: _Optional[int] = ..., log: _Optional[_Union[_dr2_comm_pb_pb2.mall_log, _Mapping]] = ...) -> None: ...

class pbreq_shop_finish_good(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class pbrsp_shop_finish_good(_message.Message):
    __slots__ = ("status", "reward", "heroreward")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    REWARD_FIELD_NUMBER: _ClassVar[int]
    HEROREWARD_FIELD_NUMBER: _ClassVar[int]
    status: int
    reward: _dr2_comm_pb_pb2.pb_bag
    heroreward: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_hero]
    def __init__(self, status: _Optional[int] = ..., reward: _Optional[_Union[_dr2_comm_pb_pb2.pb_bag, _Mapping]] = ..., heroreward: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_hero, _Mapping]]] = ...) -> None: ...

class pbreq_give_sync(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class pbrsp_give_sync(_message.Message):
    __slots__ = ("status", "give", "channel", "give_cd", "search_cd")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    GIVE_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_FIELD_NUMBER: _ClassVar[int]
    GIVE_CD_FIELD_NUMBER: _ClassVar[int]
    SEARCH_CD_FIELD_NUMBER: _ClassVar[int]
    status: int
    give: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_give_order]
    channel: str
    give_cd: int
    search_cd: int
    def __init__(self, status: _Optional[int] = ..., give: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_give_order, _Mapping]]] = ..., channel: _Optional[str] = ..., give_cd: _Optional[int] = ..., search_cd: _Optional[int] = ...) -> None: ...

class pbreq_give_search(_message.Message):
    __slots__ = ("cid", "uid64")
    CID_FIELD_NUMBER: _ClassVar[int]
    UID64_FIELD_NUMBER: _ClassVar[int]
    cid: str
    uid64: int
    def __init__(self, cid: _Optional[str] = ..., uid64: _Optional[int] = ...) -> None: ...

class pbrsp_give_search(_message.Message):
    __slots__ = ("status", "role")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    status: int
    role: _dr2_comm_pb_pb2.pb_give_role
    def __init__(self, status: _Optional[int] = ..., role: _Optional[_Union[_dr2_comm_pb_pb2.pb_give_role, _Mapping]] = ...) -> None: ...

class pbreq_give_link(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class pbrsp_give_link(_message.Message):
    __slots__ = ("status", "id")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    status: int
    id: int
    def __init__(self, status: _Optional[int] = ..., id: _Optional[int] = ...) -> None: ...

class pbreq_give_response_link(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbrsp_give_response_link(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_give_send(_message.Message):
    __slots__ = ("num",)
    NUM_FIELD_NUMBER: _ClassVar[int]
    num: int
    def __init__(self, num: _Optional[int] = ...) -> None: ...

class pbrsp_give_send(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_give_response_give(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbrsp_give_response_give(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_give_log(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class pbrsp_give_log(_message.Message):
    __slots__ = ("status", "give_log", "rec_log")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    GIVE_LOG_FIELD_NUMBER: _ClassVar[int]
    REC_LOG_FIELD_NUMBER: _ClassVar[int]
    status: int
    give_log: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_give_log]
    rec_log: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_give_log]
    def __init__(self, status: _Optional[int] = ..., give_log: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_give_log, _Mapping]]] = ..., rec_log: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_give_log, _Mapping]]] = ...) -> None: ...

class pbreq_qlt_return(_message.Message):
    __slots__ = ("hid",)
    HID_FIELD_NUMBER: _ClassVar[int]
    hid: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, hid: _Optional[_Iterable[int]] = ...) -> None: ...

class pbrsp_qlt_return(_message.Message):
    __slots__ = ("status", "items", "items2")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    ITEMS2_FIELD_NUMBER: _ClassVar[int]
    status: int
    items: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_item]
    items2: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_item]
    def __init__(self, status: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_item, _Mapping]]] = ..., items2: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_item, _Mapping]]] = ...) -> None: ...

class pbreq_mall_booth_open(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class pbrsp_mall_booth_open(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_mall_change_pwd(_message.Message):
    __slots__ = ("old", "new")
    OLD_FIELD_NUMBER: _ClassVar[int]
    NEW_FIELD_NUMBER: _ClassVar[int]
    old: str
    new: str
    def __init__(self, old: _Optional[str] = ..., new: _Optional[str] = ...) -> None: ...

class pbrsp_mall_change_pwd(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_mall_pwd_auth(_message.Message):
    __slots__ = ("pwd",)
    PWD_FIELD_NUMBER: _ClassVar[int]
    pwd: str
    def __init__(self, pwd: _Optional[str] = ...) -> None: ...

class pbrsp_mall_pwd_auth(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_mall_grade(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class pbrsp_mall_grade(_message.Message):
    __slots__ = ("status", "limit", "num")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    NUM_FIELD_NUMBER: _ClassVar[int]
    status: int
    limit: int
    num: int
    def __init__(self, status: _Optional[int] = ..., limit: _Optional[int] = ..., num: _Optional[int] = ...) -> None: ...

class pbreq_mall_exchange(_message.Message):
    __slots__ = ("num",)
    NUM_FIELD_NUMBER: _ClassVar[int]
    num: int
    def __init__(self, num: _Optional[int] = ...) -> None: ...

class pbrsp_mall_exchange(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_qlt_pvp_camp(_message.Message):
    __slots__ = ("camp", "skls", "hide", "enemy")
    CAMP_FIELD_NUMBER: _ClassVar[int]
    SKLS_FIELD_NUMBER: _ClassVar[int]
    HIDE_FIELD_NUMBER: _ClassVar[int]
    ENEMY_FIELD_NUMBER: _ClassVar[int]
    camp: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_unit]
    skls: _containers.RepeatedScalarFieldContainer[int]
    hide: _containers.RepeatedScalarFieldContainer[int]
    enemy: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_qlt_pvp_enemy]
    def __init__(self, camp: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_unit, _Mapping]]] = ..., skls: _Optional[_Iterable[int]] = ..., hide: _Optional[_Iterable[int]] = ..., enemy: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_qlt_pvp_enemy, _Mapping]]] = ...) -> None: ...

class pbrsp_qlt_pvp_camp(_message.Message):
    __slots__ = ("status", "enemy")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ENEMY_FIELD_NUMBER: _ClassVar[int]
    status: int
    enemy: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_qlt_pvp_enemy]
    def __init__(self, status: _Optional[int] = ..., enemy: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_qlt_pvp_enemy, _Mapping]]] = ...) -> None: ...

class pbreq_qlt_pvp_sync(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class pbrsp_qlt_pvp_sync(_message.Message):
    __slots__ = ("status", "flag", "camp", "skls", "hide", "cd", "rank", "enemy", "vit", "vit_cd", "vit_buy", "refresh", "skills", "skills2", "like_uids", "like_cd", "season", "top_rank", "camp_cd")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    FLAG_FIELD_NUMBER: _ClassVar[int]
    CAMP_FIELD_NUMBER: _ClassVar[int]
    SKLS_FIELD_NUMBER: _ClassVar[int]
    HIDE_FIELD_NUMBER: _ClassVar[int]
    CD_FIELD_NUMBER: _ClassVar[int]
    RANK_FIELD_NUMBER: _ClassVar[int]
    ENEMY_FIELD_NUMBER: _ClassVar[int]
    VIT_FIELD_NUMBER: _ClassVar[int]
    VIT_CD_FIELD_NUMBER: _ClassVar[int]
    VIT_BUY_FIELD_NUMBER: _ClassVar[int]
    REFRESH_FIELD_NUMBER: _ClassVar[int]
    SKILLS_FIELD_NUMBER: _ClassVar[int]
    SKILLS2_FIELD_NUMBER: _ClassVar[int]
    LIKE_UIDS_FIELD_NUMBER: _ClassVar[int]
    LIKE_CD_FIELD_NUMBER: _ClassVar[int]
    SEASON_FIELD_NUMBER: _ClassVar[int]
    TOP_RANK_FIELD_NUMBER: _ClassVar[int]
    CAMP_CD_FIELD_NUMBER: _ClassVar[int]
    status: int
    flag: int
    camp: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_unit]
    skls: _containers.RepeatedScalarFieldContainer[int]
    hide: _containers.RepeatedScalarFieldContainer[int]
    cd: int
    rank: _dr2_comm_pb_pb2.pb_smbrs
    enemy: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_qlt_pvp_enemy]
    vit: int
    vit_cd: int
    vit_buy: int
    refresh: int
    skills: _containers.RepeatedScalarFieldContainer[int]
    skills2: _containers.RepeatedScalarFieldContainer[int]
    like_uids: _containers.RepeatedScalarFieldContainer[str]
    like_cd: int
    season: int
    top_rank: int
    camp_cd: int
    def __init__(self, status: _Optional[int] = ..., flag: _Optional[int] = ..., camp: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_unit, _Mapping]]] = ..., skls: _Optional[_Iterable[int]] = ..., hide: _Optional[_Iterable[int]] = ..., cd: _Optional[int] = ..., rank: _Optional[_Union[_dr2_comm_pb_pb2.pb_smbrs, _Mapping]] = ..., enemy: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_qlt_pvp_enemy, _Mapping]]] = ..., vit: _Optional[int] = ..., vit_cd: _Optional[int] = ..., vit_buy: _Optional[int] = ..., refresh: _Optional[int] = ..., skills: _Optional[_Iterable[int]] = ..., skills2: _Optional[_Iterable[int]] = ..., like_uids: _Optional[_Iterable[str]] = ..., like_cd: _Optional[int] = ..., season: _Optional[int] = ..., top_rank: _Optional[int] = ..., camp_cd: _Optional[int] = ...) -> None: ...

class pbreq_qlt_pvp_refresh(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class pbrsp_qlt_pvp_refresh(_message.Message):
    __slots__ = ("status", "enemy")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ENEMY_FIELD_NUMBER: _ClassVar[int]
    status: int
    enemy: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_qlt_pvp_enemy]
    def __init__(self, status: _Optional[int] = ..., enemy: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_qlt_pvp_enemy, _Mapping]]] = ...) -> None: ...

class pbreq_qlt_pvp_select_skill(_message.Message):
    __slots__ = ("skills",)
    SKILLS_FIELD_NUMBER: _ClassVar[int]
    skills: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, skills: _Optional[_Iterable[int]] = ...) -> None: ...

class pbrsp_qlt_pvp_select_skill(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_qlt_pvp_shop_sync(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class pbrsp_qlt_pvp_shop_sync(_message.Message):
    __slots__ = ("status", "goods", "cd")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    GOODS_FIELD_NUMBER: _ClassVar[int]
    CD_FIELD_NUMBER: _ClassVar[int]
    status: int
    goods: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_item]
    cd: int
    def __init__(self, status: _Optional[int] = ..., goods: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_item, _Mapping]]] = ..., cd: _Optional[int] = ...) -> None: ...

class pbreq_qlt_pvp_shop_buy(_message.Message):
    __slots__ = ("id", "num")
    ID_FIELD_NUMBER: _ClassVar[int]
    NUM_FIELD_NUMBER: _ClassVar[int]
    id: int
    num: int
    def __init__(self, id: _Optional[int] = ..., num: _Optional[int] = ...) -> None: ...

class pbrsp_qlt_pvp_shop_buy(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_qlt_pvp_rank(_message.Message):
    __slots__ = ("idx",)
    IDX_FIELD_NUMBER: _ClassVar[int]
    idx: int
    def __init__(self, idx: _Optional[int] = ...) -> None: ...

class pbrsp_qlt_pvp_rank(_message.Message):
    __slots__ = ("status", "rank")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    RANK_FIELD_NUMBER: _ClassVar[int]
    status: int
    rank: _dr2_comm_pb_pb2.pb_smbrs
    def __init__(self, status: _Optional[int] = ..., rank: _Optional[_Union[_dr2_comm_pb_pb2.pb_smbrs, _Mapping]] = ...) -> None: ...

class pbreq_qlt_pvp_vit_buy(_message.Message):
    __slots__ = ("num",)
    NUM_FIELD_NUMBER: _ClassVar[int]
    num: int
    def __init__(self, num: _Optional[int] = ...) -> None: ...

class pbrsp_qlt_pvp_vit_buy(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_qlt_pvp_fight(_message.Message):
    __slots__ = ("camp", "id", "skls")
    CAMP_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    SKLS_FIELD_NUMBER: _ClassVar[int]
    camp: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_unit]
    id: int
    skls: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, camp: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_unit, _Mapping]]] = ..., id: _Optional[int] = ..., skls: _Optional[_Iterable[int]] = ...) -> None: ...

class pbrsp_qlt_pvp_fight(_message.Message):
    __slots__ = ("status", "video", "enemy", "top_rank", "rank")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    VIDEO_FIELD_NUMBER: _ClassVar[int]
    ENEMY_FIELD_NUMBER: _ClassVar[int]
    TOP_RANK_FIELD_NUMBER: _ClassVar[int]
    RANK_FIELD_NUMBER: _ClassVar[int]
    status: int
    video: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_wvideo]
    enemy: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_qlt_pvp_enemy]
    top_rank: int
    rank: int
    def __init__(self, status: _Optional[int] = ..., video: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_wvideo, _Mapping]]] = ..., enemy: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_qlt_pvp_enemy, _Mapping]]] = ..., top_rank: _Optional[int] = ..., rank: _Optional[int] = ...) -> None: ...

class pbreq_qlt_pvp_like(_message.Message):
    __slots__ = ("udk",)
    UDK_FIELD_NUMBER: _ClassVar[int]
    udk: str
    def __init__(self, udk: _Optional[str] = ...) -> None: ...

class pbrsp_qlt_pvp_like(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_qlt_pvp_logs(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class pbrsp_qlt_pvp_logs(_message.Message):
    __slots__ = ("status", "fight", "defence")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    FIGHT_FIELD_NUMBER: _ClassVar[int]
    DEFENCE_FIELD_NUMBER: _ClassVar[int]
    status: int
    fight: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_qloger]
    defence: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_qloger]
    def __init__(self, status: _Optional[int] = ..., fight: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_qloger, _Mapping]]] = ..., defence: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_qloger, _Mapping]]] = ...) -> None: ...

class pbreq_qlt_pvp_video(_message.Message):
    __slots__ = ("id", "type")
    ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    id: int
    type: int
    def __init__(self, id: _Optional[int] = ..., type: _Optional[int] = ...) -> None: ...

class pbrsp_qlt_pvp_video(_message.Message):
    __slots__ = ("status", "video")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    VIDEO_FIELD_NUMBER: _ClassVar[int]
    status: int
    video: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_qvideo]
    def __init__(self, status: _Optional[int] = ..., video: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_qvideo, _Mapping]]] = ...) -> None: ...

class pbreq_power_pve_sync(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class pbrsp_power_pve_sync(_message.Message):
    __slots__ = ("status", "season", "state", "cd", "enroll", "num", "first", "id", "task", "source_lv", "source", "stime", "exp", "look_times", "notice", "look_id", "day_cd", "job", "ranks1", "ranks2", "reward_flag", "leader", "items_num", "vit_cd", "lv_factor", "original_id", "power_num", "channel", "achi")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    SEASON_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    CD_FIELD_NUMBER: _ClassVar[int]
    ENROLL_FIELD_NUMBER: _ClassVar[int]
    NUM_FIELD_NUMBER: _ClassVar[int]
    FIRST_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    TASK_FIELD_NUMBER: _ClassVar[int]
    SOURCE_LV_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    STIME_FIELD_NUMBER: _ClassVar[int]
    EXP_FIELD_NUMBER: _ClassVar[int]
    LOOK_TIMES_FIELD_NUMBER: _ClassVar[int]
    NOTICE_FIELD_NUMBER: _ClassVar[int]
    LOOK_ID_FIELD_NUMBER: _ClassVar[int]
    DAY_CD_FIELD_NUMBER: _ClassVar[int]
    JOB_FIELD_NUMBER: _ClassVar[int]
    RANKS1_FIELD_NUMBER: _ClassVar[int]
    RANKS2_FIELD_NUMBER: _ClassVar[int]
    REWARD_FLAG_FIELD_NUMBER: _ClassVar[int]
    LEADER_FIELD_NUMBER: _ClassVar[int]
    ITEMS_NUM_FIELD_NUMBER: _ClassVar[int]
    VIT_CD_FIELD_NUMBER: _ClassVar[int]
    LV_FACTOR_FIELD_NUMBER: _ClassVar[int]
    ORIGINAL_ID_FIELD_NUMBER: _ClassVar[int]
    POWER_NUM_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_FIELD_NUMBER: _ClassVar[int]
    ACHI_FIELD_NUMBER: _ClassVar[int]
    status: int
    season: int
    state: int
    cd: int
    enroll: int
    num: int
    first: int
    id: int
    task: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.power_task]
    source_lv: int
    source: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_item]
    stime: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_item]
    exp: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_item]
    look_times: int
    notice: str
    look_id: int
    day_cd: int
    job: int
    ranks1: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.power_rank]
    ranks2: _dr2_comm_pb_pb2.pb_smbrs
    reward_flag: int
    leader: _dr2_comm_pb_pb2.pb_give_role
    items_num: _containers.RepeatedScalarFieldContainer[int]
    vit_cd: int
    lv_factor: int
    original_id: int
    power_num: int
    channel: str
    achi: int
    def __init__(self, status: _Optional[int] = ..., season: _Optional[int] = ..., state: _Optional[int] = ..., cd: _Optional[int] = ..., enroll: _Optional[int] = ..., num: _Optional[int] = ..., first: _Optional[int] = ..., id: _Optional[int] = ..., task: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.power_task, _Mapping]]] = ..., source_lv: _Optional[int] = ..., source: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_item, _Mapping]]] = ..., stime: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_item, _Mapping]]] = ..., exp: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_item, _Mapping]]] = ..., look_times: _Optional[int] = ..., notice: _Optional[str] = ..., look_id: _Optional[int] = ..., day_cd: _Optional[int] = ..., job: _Optional[int] = ..., ranks1: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.power_rank, _Mapping]]] = ..., ranks2: _Optional[_Union[_dr2_comm_pb_pb2.pb_smbrs, _Mapping]] = ..., reward_flag: _Optional[int] = ..., leader: _Optional[_Union[_dr2_comm_pb_pb2.pb_give_role, _Mapping]] = ..., items_num: _Optional[_Iterable[int]] = ..., vit_cd: _Optional[int] = ..., lv_factor: _Optional[int] = ..., original_id: _Optional[int] = ..., power_num: _Optional[int] = ..., channel: _Optional[str] = ..., achi: _Optional[int] = ...) -> None: ...

class pbreq_power_pve_last_rank(_message.Message):
    __slots__ = ("season",)
    SEASON_FIELD_NUMBER: _ClassVar[int]
    season: int
    def __init__(self, season: _Optional[int] = ...) -> None: ...

class pbrsp_power_pve_last_rank(_message.Message):
    __slots__ = ("status", "power_rank", "role_rank")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    POWER_RANK_FIELD_NUMBER: _ClassVar[int]
    ROLE_RANK_FIELD_NUMBER: _ClassVar[int]
    status: int
    power_rank: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.power_rank]
    role_rank: _dr2_comm_pb_pb2.pb_smbrs
    def __init__(self, status: _Optional[int] = ..., power_rank: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.power_rank, _Mapping]]] = ..., role_rank: _Optional[_Union[_dr2_comm_pb_pb2.pb_smbrs, _Mapping]] = ...) -> None: ...

class pbreq_power_pve_role_rank(_message.Message):
    __slots__ = ("type", "id")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    type: int
    id: int
    def __init__(self, type: _Optional[int] = ..., id: _Optional[int] = ...) -> None: ...

class pbrsp_power_pve_role_rank(_message.Message):
    __slots__ = ("status", "rank", "exp", "job_list", "rewards")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    RANK_FIELD_NUMBER: _ClassVar[int]
    EXP_FIELD_NUMBER: _ClassVar[int]
    JOB_LIST_FIELD_NUMBER: _ClassVar[int]
    REWARDS_FIELD_NUMBER: _ClassVar[int]
    status: int
    rank: _dr2_comm_pb_pb2.pb_smbrs
    exp: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_item]
    job_list: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_smbr]
    rewards: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_bag]
    def __init__(self, status: _Optional[int] = ..., rank: _Optional[_Union[_dr2_comm_pb_pb2.pb_smbrs, _Mapping]] = ..., exp: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_item, _Mapping]]] = ..., job_list: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_smbr, _Mapping]]] = ..., rewards: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_bag, _Mapping]]] = ...) -> None: ...

class pbreq_power_pve_power_rank(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class pbrsp_power_pve_power_rank(_message.Message):
    __slots__ = ("status", "rank")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    RANK_FIELD_NUMBER: _ClassVar[int]
    status: int
    rank: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.power_rank]
    def __init__(self, status: _Optional[int] = ..., rank: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.power_rank, _Mapping]]] = ...) -> None: ...

class pbreq_power_pve_sync2(_message.Message):
    __slots__ = ("ids",)
    IDS_FIELD_NUMBER: _ClassVar[int]
    ids: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, ids: _Optional[_Iterable[int]] = ...) -> None: ...

class pbrsp_power_pve_sync2(_message.Message):
    __slots__ = ("status", "dot", "buff", "num", "dot_num", "flag_times")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    DOT_FIELD_NUMBER: _ClassVar[int]
    BUFF_FIELD_NUMBER: _ClassVar[int]
    NUM_FIELD_NUMBER: _ClassVar[int]
    DOT_NUM_FIELD_NUMBER: _ClassVar[int]
    FLAG_TIMES_FIELD_NUMBER: _ClassVar[int]
    status: int
    dot: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.dot_info]
    buff: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_item]
    num: int
    dot_num: int
    flag_times: int
    def __init__(self, status: _Optional[int] = ..., dot: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.dot_info, _Mapping]]] = ..., buff: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_item, _Mapping]]] = ..., num: _Optional[int] = ..., dot_num: _Optional[int] = ..., flag_times: _Optional[int] = ...) -> None: ...

class pbreq_power_pve_dot_degree_log(_message.Message):
    __slots__ = ("dot_id",)
    DOT_ID_FIELD_NUMBER: _ClassVar[int]
    dot_id: int
    def __init__(self, dot_id: _Optional[int] = ...) -> None: ...

class pbrsp_power_pve_dot_degree_log(_message.Message):
    __slots__ = ("status", "log")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    LOG_FIELD_NUMBER: _ClassVar[int]
    status: int
    log: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.dot_log]
    def __init__(self, status: _Optional[int] = ..., log: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.dot_log, _Mapping]]] = ...) -> None: ...

class pbreq_power_pve_fight(_message.Message):
    __slots__ = ("type", "monster_id", "camp", "buff", "tid", "idx")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    MONSTER_ID_FIELD_NUMBER: _ClassVar[int]
    CAMP_FIELD_NUMBER: _ClassVar[int]
    BUFF_FIELD_NUMBER: _ClassVar[int]
    TID_FIELD_NUMBER: _ClassVar[int]
    IDX_FIELD_NUMBER: _ClassVar[int]
    type: int
    monster_id: int
    camp: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_unit]
    buff: _containers.RepeatedScalarFieldContainer[int]
    tid: int
    idx: int
    def __init__(self, type: _Optional[int] = ..., monster_id: _Optional[int] = ..., camp: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_unit, _Mapping]]] = ..., buff: _Optional[_Iterable[int]] = ..., tid: _Optional[int] = ..., idx: _Optional[int] = ...) -> None: ...

class pbrsp_power_pve_fight(_message.Message):
    __slots__ = ("status", "video", "reward", "hp", "enemy", "monster", "reward2")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    VIDEO_FIELD_NUMBER: _ClassVar[int]
    REWARD_FIELD_NUMBER: _ClassVar[int]
    HP_FIELD_NUMBER: _ClassVar[int]
    ENEMY_FIELD_NUMBER: _ClassVar[int]
    MONSTER_FIELD_NUMBER: _ClassVar[int]
    REWARD2_FIELD_NUMBER: _ClassVar[int]
    status: int
    video: _dr2_comm_pb_pb2.pb_evideo
    reward: _dr2_comm_pb_pb2.pb_bag
    hp: int
    enemy: _dr2_comm_pb_pb2.pb_give_role
    monster: int
    reward2: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_item]
    def __init__(self, status: _Optional[int] = ..., video: _Optional[_Union[_dr2_comm_pb_pb2.pb_evideo, _Mapping]] = ..., reward: _Optional[_Union[_dr2_comm_pb_pb2.pb_bag, _Mapping]] = ..., hp: _Optional[int] = ..., enemy: _Optional[_Union[_dr2_comm_pb_pb2.pb_give_role, _Mapping]] = ..., monster: _Optional[int] = ..., reward2: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_item, _Mapping]]] = ...) -> None: ...

class pbreq_power_pve_buy(_message.Message):
    __slots__ = ("type", "id", "num", "dot")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NUM_FIELD_NUMBER: _ClassVar[int]
    DOT_FIELD_NUMBER: _ClassVar[int]
    type: int
    id: int
    num: int
    dot: int
    def __init__(self, type: _Optional[int] = ..., id: _Optional[int] = ..., num: _Optional[int] = ..., dot: _Optional[int] = ...) -> None: ...

class pbrsp_power_pve_buy(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_power_pve_apply(_message.Message):
    __slots__ = ("type",)
    TYPE_FIELD_NUMBER: _ClassVar[int]
    type: int
    def __init__(self, type: _Optional[int] = ...) -> None: ...

class pbrsp_power_pve_apply(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_power_pve_look(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class pbrsp_power_pve_look(_message.Message):
    __slots__ = ("status", "id", "reward", "reward2", "cd")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    REWARD_FIELD_NUMBER: _ClassVar[int]
    REWARD2_FIELD_NUMBER: _ClassVar[int]
    CD_FIELD_NUMBER: _ClassVar[int]
    status: int
    id: int
    reward: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_item]
    reward2: _dr2_comm_pb_pb2.pb_bag
    cd: int
    def __init__(self, status: _Optional[int] = ..., id: _Optional[int] = ..., reward: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_item, _Mapping]]] = ..., reward2: _Optional[_Union[_dr2_comm_pb_pb2.pb_bag, _Mapping]] = ..., cd: _Optional[int] = ...) -> None: ...

class pbreq_power_pve_donate(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class pbrsp_power_pve_donate(_message.Message):
    __slots__ = ("status", "num", "exp", "reward")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    NUM_FIELD_NUMBER: _ClassVar[int]
    EXP_FIELD_NUMBER: _ClassVar[int]
    REWARD_FIELD_NUMBER: _ClassVar[int]
    status: int
    num: int
    exp: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_item]
    reward: _dr2_comm_pb_pb2.pb_bag
    def __init__(self, status: _Optional[int] = ..., num: _Optional[int] = ..., exp: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_item, _Mapping]]] = ..., reward: _Optional[_Union[_dr2_comm_pb_pb2.pb_bag, _Mapping]] = ...) -> None: ...

class pbreq_power_pve_source_lv(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class pbrsp_power_pve_source_lv(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_power_pve_source_get(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class pbrsp_power_pve_source_get(_message.Message):
    __slots__ = ("status", "reward")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    REWARD_FIELD_NUMBER: _ClassVar[int]
    status: int
    reward: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_kv]
    def __init__(self, status: _Optional[int] = ..., reward: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_kv, _Mapping]]] = ...) -> None: ...

class pbreq_power_pve_tmp_save(_message.Message):
    __slots__ = ("tmp_id", "skill", "name")
    TMP_ID_FIELD_NUMBER: _ClassVar[int]
    SKILL_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    tmp_id: int
    skill: _containers.RepeatedScalarFieldContainer[int]
    name: str
    def __init__(self, tmp_id: _Optional[int] = ..., skill: _Optional[_Iterable[int]] = ..., name: _Optional[str] = ...) -> None: ...

class pbrsp_power_pve_tmp_save(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_power_pve_tmp_use(_message.Message):
    __slots__ = ("tmp_id", "dot_ids")
    TMP_ID_FIELD_NUMBER: _ClassVar[int]
    DOT_IDS_FIELD_NUMBER: _ClassVar[int]
    tmp_id: int
    dot_ids: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, tmp_id: _Optional[int] = ..., dot_ids: _Optional[_Iterable[int]] = ...) -> None: ...

class pbrsp_power_pve_tmp_use(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_power_pve_season_reward(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class pbrsp_power_pve_season_reward(_message.Message):
    __slots__ = ("status", "reward")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    REWARD_FIELD_NUMBER: _ClassVar[int]
    status: int
    reward: _dr2_comm_pb_pb2.pb_bag
    def __init__(self, status: _Optional[int] = ..., reward: _Optional[_Union[_dr2_comm_pb_pb2.pb_bag, _Mapping]] = ...) -> None: ...

class pbreq_power_pve_claim(_message.Message):
    __slots__ = ("id", "type", "task_type", "excel_id")
    ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    TASK_TYPE_FIELD_NUMBER: _ClassVar[int]
    EXCEL_ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    type: int
    task_type: int
    excel_id: int
    def __init__(self, id: _Optional[int] = ..., type: _Optional[int] = ..., task_type: _Optional[int] = ..., excel_id: _Optional[int] = ...) -> None: ...

class pbrsp_power_pve_claim(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_power_pve_monster(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class pbrsp_power_pve_monster(_message.Message):
    __slots__ = ("status", "claim", "monster", "affix")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    CLAIM_FIELD_NUMBER: _ClassVar[int]
    MONSTER_FIELD_NUMBER: _ClassVar[int]
    AFFIX_FIELD_NUMBER: _ClassVar[int]
    status: int
    claim: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_item]
    monster: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.power_monster]
    affix: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, status: _Optional[int] = ..., claim: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_item, _Mapping]]] = ..., monster: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.power_monster, _Mapping]]] = ..., affix: _Optional[_Iterable[int]] = ...) -> None: ...

class pbreq_power_pve_dot(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class pbrsp_power_pve_dot(_message.Message):
    __slots__ = ("status", "rank", "dot")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    RANK_FIELD_NUMBER: _ClassVar[int]
    DOT_FIELD_NUMBER: _ClassVar[int]
    status: int
    rank: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.power_rank]
    dot: _dr2_comm_pb_pb2.dot_info
    def __init__(self, status: _Optional[int] = ..., rank: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.power_rank, _Mapping]]] = ..., dot: _Optional[_Union[_dr2_comm_pb_pb2.dot_info, _Mapping]] = ...) -> None: ...

class pbreq_power_pve_skill(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class pbrsp_power_pve_skill(_message.Message):
    __slots__ = ("status", "skill", "exp")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    SKILL_FIELD_NUMBER: _ClassVar[int]
    EXP_FIELD_NUMBER: _ClassVar[int]
    status: int
    skill: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.power_skill]
    exp: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_item]
    def __init__(self, status: _Optional[int] = ..., skill: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.power_skill, _Mapping]]] = ..., exp: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_item, _Mapping]]] = ...) -> None: ...

class pbreq_power_pve_look_down(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class pbrsp_power_pve_look_down(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_power_pve_task(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class pbrsp_power_pve_task(_message.Message):
    __slots__ = ("status", "task")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    TASK_FIELD_NUMBER: _ClassVar[int]
    status: int
    task: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.power_task]
    def __init__(self, status: _Optional[int] = ..., task: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.power_task, _Mapping]]] = ...) -> None: ...

class pbreq_power_pve_dot_reward(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class pbrsp_power_pve_dot_reward(_message.Message):
    __slots__ = ("status", "num")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    NUM_FIELD_NUMBER: _ClassVar[int]
    status: int
    num: int
    def __init__(self, status: _Optional[int] = ..., num: _Optional[int] = ...) -> None: ...

class pbreq_power_pve_defence_info(_message.Message):
    __slots__ = ("dot_id",)
    DOT_ID_FIELD_NUMBER: _ClassVar[int]
    dot_id: int
    def __init__(self, dot_id: _Optional[int] = ...) -> None: ...

class pbrsp_power_pve_defence_info(_message.Message):
    __slots__ = ("status", "skills")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    SKILLS_FIELD_NUMBER: _ClassVar[int]
    status: int
    skills: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, status: _Optional[int] = ..., skills: _Optional[_Iterable[int]] = ...) -> None: ...

class pbreq_power_pve_manager(_message.Message):
    __slots__ = ("type", "manager")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    MANAGER_FIELD_NUMBER: _ClassVar[int]
    type: int
    manager: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.power_manager]
    def __init__(self, type: _Optional[int] = ..., manager: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.power_manager, _Mapping]]] = ...) -> None: ...

class pbrsp_power_pve_manager(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_power_pve_power_log(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class pbrsp_power_pve_power_log(_message.Message):
    __slots__ = ("status", "log", "chat")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    LOG_FIELD_NUMBER: _ClassVar[int]
    CHAT_FIELD_NUMBER: _ClassVar[int]
    status: int
    log: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.power_log]
    chat: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_chat]
    def __init__(self, status: _Optional[int] = ..., log: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.power_log, _Mapping]]] = ..., chat: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_chat, _Mapping]]] = ...) -> None: ...

class pbreq_power_pve_notice(_message.Message):
    __slots__ = ("notice",)
    NOTICE_FIELD_NUMBER: _ClassVar[int]
    notice: str
    def __init__(self, notice: _Optional[str] = ...) -> None: ...

class pbrsp_power_pve_notice(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_power_pve_chat(_message.Message):
    __slots__ = ("text",)
    TEXT_FIELD_NUMBER: _ClassVar[int]
    text: str
    def __init__(self, text: _Optional[str] = ...) -> None: ...

class pbrsp_power_pve_chat(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_sgame_sync(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class pbrsp_sgame_sync(_message.Message):
    __slots__ = ("status", "items", "ids", "num", "cd")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    IDS_FIELD_NUMBER: _ClassVar[int]
    NUM_FIELD_NUMBER: _ClassVar[int]
    CD_FIELD_NUMBER: _ClassVar[int]
    status: int
    items: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_kv]
    ids: _containers.RepeatedScalarFieldContainer[int]
    num: int
    cd: int
    def __init__(self, status: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_kv, _Mapping]]] = ..., ids: _Optional[_Iterable[int]] = ..., num: _Optional[int] = ..., cd: _Optional[int] = ...) -> None: ...

class pbreq_sgame_play_start(_message.Message):
    __slots__ = ("id", "v")
    ID_FIELD_NUMBER: _ClassVar[int]
    V_FIELD_NUMBER: _ClassVar[int]
    id: int
    v: int
    def __init__(self, id: _Optional[int] = ..., v: _Optional[int] = ...) -> None: ...

class pbrsp_sgame_play_start(_message.Message):
    __slots__ = ("status", "free_ids")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    FREE_IDS_FIELD_NUMBER: _ClassVar[int]
    status: int
    free_ids: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, status: _Optional[int] = ..., free_ids: _Optional[_Iterable[int]] = ...) -> None: ...

class pbreq_sgame_play_end(_message.Message):
    __slots__ = ("id", "score", "stage", "wave", "hp", "cd", "hero", "skip", "flag")
    ID_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    STAGE_FIELD_NUMBER: _ClassVar[int]
    WAVE_FIELD_NUMBER: _ClassVar[int]
    HP_FIELD_NUMBER: _ClassVar[int]
    CD_FIELD_NUMBER: _ClassVar[int]
    HERO_FIELD_NUMBER: _ClassVar[int]
    SKIP_FIELD_NUMBER: _ClassVar[int]
    FLAG_FIELD_NUMBER: _ClassVar[int]
    id: int
    score: int
    stage: int
    wave: int
    hp: int
    cd: int
    hero: _containers.RepeatedScalarFieldContainer[int]
    skip: int
    flag: int
    def __init__(self, id: _Optional[int] = ..., score: _Optional[int] = ..., stage: _Optional[int] = ..., wave: _Optional[int] = ..., hp: _Optional[int] = ..., cd: _Optional[int] = ..., hero: _Optional[_Iterable[int]] = ..., skip: _Optional[int] = ..., flag: _Optional[int] = ...) -> None: ...

class pbrsp_sgame_play_end(_message.Message):
    __slots__ = ("status", "reward", "reward2", "reward3", "reward4", "reward5", "reward6", "star")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    REWARD_FIELD_NUMBER: _ClassVar[int]
    REWARD2_FIELD_NUMBER: _ClassVar[int]
    REWARD3_FIELD_NUMBER: _ClassVar[int]
    REWARD4_FIELD_NUMBER: _ClassVar[int]
    REWARD5_FIELD_NUMBER: _ClassVar[int]
    REWARD6_FIELD_NUMBER: _ClassVar[int]
    STAR_FIELD_NUMBER: _ClassVar[int]
    status: int
    reward: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_item]
    reward2: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_item]
    reward3: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_kv]
    reward4: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_kv]
    reward5: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_kv]
    reward6: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_kv]
    star: int
    def __init__(self, status: _Optional[int] = ..., reward: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_item, _Mapping]]] = ..., reward2: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_item, _Mapping]]] = ..., reward3: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_kv, _Mapping]]] = ..., reward4: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_kv, _Mapping]]] = ..., reward5: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_kv, _Mapping]]] = ..., reward6: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_kv, _Mapping]]] = ..., star: _Optional[int] = ...) -> None: ...

class pbreq_sgame_reward(_message.Message):
    __slots__ = ("ids",)
    IDS_FIELD_NUMBER: _ClassVar[int]
    ids: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, ids: _Optional[_Iterable[int]] = ...) -> None: ...

class pbrsp_sgame_reward(_message.Message):
    __slots__ = ("status", "reward")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    REWARD_FIELD_NUMBER: _ClassVar[int]
    status: int
    reward: _dr2_comm_pb_pb2.pb_bag
    def __init__(self, status: _Optional[int] = ..., reward: _Optional[_Union[_dr2_comm_pb_pb2.pb_bag, _Mapping]] = ...) -> None: ...

class pbreq_sgame_rank(_message.Message):
    __slots__ = ("id", "stage")
    ID_FIELD_NUMBER: _ClassVar[int]
    STAGE_FIELD_NUMBER: _ClassVar[int]
    id: int
    stage: int
    def __init__(self, id: _Optional[int] = ..., stage: _Optional[int] = ...) -> None: ...

class pbrsp_sgame_rank(_message.Message):
    __slots__ = ("status", "rank")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    RANK_FIELD_NUMBER: _ClassVar[int]
    status: int
    rank: _dr2_comm_pb_pb2.pb_smbrs
    def __init__(self, status: _Optional[int] = ..., rank: _Optional[_Union[_dr2_comm_pb_pb2.pb_smbrs, _Mapping]] = ...) -> None: ...

class pbreq_sgame_skl(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class pbrsp_sgame_skl(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_sgame_skl_reset(_message.Message):
    __slots__ = ("type",)
    TYPE_FIELD_NUMBER: _ClassVar[int]
    type: int
    def __init__(self, type: _Optional[int] = ...) -> None: ...

class pbrsp_sgame_skl_reset(_message.Message):
    __slots__ = ("status", "items", "skills")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    SKILLS_FIELD_NUMBER: _ClassVar[int]
    status: int
    items: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_kv]
    skills: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_kv]
    def __init__(self, status: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_kv, _Mapping]]] = ..., skills: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_kv, _Mapping]]] = ...) -> None: ...

class pbreq_sgame_defend_sync(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class pbrsp_sgame_defend_sync(_message.Message):
    __slots__ = ("status", "ids", "heroes", "skills", "free_ids", "items", "reward", "reward2", "reward3", "reward4", "reward5", "reward6", "wave", "vit", "type")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    IDS_FIELD_NUMBER: _ClassVar[int]
    HEROES_FIELD_NUMBER: _ClassVar[int]
    SKILLS_FIELD_NUMBER: _ClassVar[int]
    FREE_IDS_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    REWARD_FIELD_NUMBER: _ClassVar[int]
    REWARD2_FIELD_NUMBER: _ClassVar[int]
    REWARD3_FIELD_NUMBER: _ClassVar[int]
    REWARD4_FIELD_NUMBER: _ClassVar[int]
    REWARD5_FIELD_NUMBER: _ClassVar[int]
    REWARD6_FIELD_NUMBER: _ClassVar[int]
    WAVE_FIELD_NUMBER: _ClassVar[int]
    VIT_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    status: int
    ids: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_kv2]
    heroes: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_kv]
    skills: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_kv]
    free_ids: _containers.RepeatedScalarFieldContainer[int]
    items: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_kv]
    reward: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_item]
    reward2: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_item]
    reward3: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_kv]
    reward4: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_kv]
    reward5: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_kv]
    reward6: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_kv]
    wave: int
    vit: int
    type: int
    def __init__(self, status: _Optional[int] = ..., ids: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_kv2, _Mapping]]] = ..., heroes: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_kv, _Mapping]]] = ..., skills: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_kv, _Mapping]]] = ..., free_ids: _Optional[_Iterable[int]] = ..., items: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_kv, _Mapping]]] = ..., reward: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_item, _Mapping]]] = ..., reward2: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_item, _Mapping]]] = ..., reward3: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_kv, _Mapping]]] = ..., reward4: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_kv, _Mapping]]] = ..., reward5: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_kv, _Mapping]]] = ..., reward6: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_kv, _Mapping]]] = ..., wave: _Optional[int] = ..., vit: _Optional[int] = ..., type: _Optional[int] = ...) -> None: ...

class pbreq_sgame_exchange(_message.Message):
    __slots__ = ("type", "num")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    NUM_FIELD_NUMBER: _ClassVar[int]
    type: int
    num: int
    def __init__(self, type: _Optional[int] = ..., num: _Optional[int] = ...) -> None: ...

class pbrsp_sgame_exchange(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_mgame_sync(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class pbrsp_mgame_sync(_message.Message):
    __slots__ = ("status", "map", "bag", "props", "task1", "task2", "task3", "cd", "shop", "bag_num", "item", "love", "vit_buy", "house_max", "vit_cd", "flag")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MAP_FIELD_NUMBER: _ClassVar[int]
    BAG_FIELD_NUMBER: _ClassVar[int]
    PROPS_FIELD_NUMBER: _ClassVar[int]
    TASK1_FIELD_NUMBER: _ClassVar[int]
    TASK2_FIELD_NUMBER: _ClassVar[int]
    TASK3_FIELD_NUMBER: _ClassVar[int]
    CD_FIELD_NUMBER: _ClassVar[int]
    SHOP_FIELD_NUMBER: _ClassVar[int]
    BAG_NUM_FIELD_NUMBER: _ClassVar[int]
    ITEM_FIELD_NUMBER: _ClassVar[int]
    LOVE_FIELD_NUMBER: _ClassVar[int]
    VIT_BUY_FIELD_NUMBER: _ClassVar[int]
    HOUSE_MAX_FIELD_NUMBER: _ClassVar[int]
    VIT_CD_FIELD_NUMBER: _ClassVar[int]
    FLAG_FIELD_NUMBER: _ClassVar[int]
    status: int
    map: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_mgame_map]
    bag: _containers.RepeatedScalarFieldContainer[int]
    props: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_mgame_prop]
    task1: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_kv]
    task2: _containers.RepeatedScalarFieldContainer[int]
    task3: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_kv]
    cd: int
    shop: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_kv]
    bag_num: int
    item: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_kv]
    love: int
    vit_buy: int
    house_max: int
    vit_cd: int
    flag: int
    def __init__(self, status: _Optional[int] = ..., map: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_mgame_map, _Mapping]]] = ..., bag: _Optional[_Iterable[int]] = ..., props: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_mgame_prop, _Mapping]]] = ..., task1: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_kv, _Mapping]]] = ..., task2: _Optional[_Iterable[int]] = ..., task3: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_kv, _Mapping]]] = ..., cd: _Optional[int] = ..., shop: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_kv, _Mapping]]] = ..., bag_num: _Optional[int] = ..., item: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_kv, _Mapping]]] = ..., love: _Optional[int] = ..., vit_buy: _Optional[int] = ..., house_max: _Optional[int] = ..., vit_cd: _Optional[int] = ..., flag: _Optional[int] = ...) -> None: ...

class pbreq_mgame_move(_message.Message):
    __slots__ = ("map_id1", "map_id2", "type", "prop_id")
    MAP_ID1_FIELD_NUMBER: _ClassVar[int]
    MAP_ID2_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    PROP_ID_FIELD_NUMBER: _ClassVar[int]
    map_id1: int
    map_id2: int
    type: int
    prop_id: int
    def __init__(self, map_id1: _Optional[int] = ..., map_id2: _Optional[int] = ..., type: _Optional[int] = ..., prop_id: _Optional[int] = ...) -> None: ...

class pbrsp_mgame_move(_message.Message):
    __slots__ = ("status", "prop")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    PROP_FIELD_NUMBER: _ClassVar[int]
    status: int
    prop: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_mgame_prop]
    def __init__(self, status: _Optional[int] = ..., prop: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_mgame_prop, _Mapping]]] = ...) -> None: ...

class pbreq_mgame_sell(_message.Message):
    __slots__ = ("map_id",)
    MAP_ID_FIELD_NUMBER: _ClassVar[int]
    map_id: int
    def __init__(self, map_id: _Optional[int] = ...) -> None: ...

class pbrsp_mgame_sell(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_mgame_buy_bag(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class pbrsp_mgame_buy_bag(_message.Message):
    __slots__ = ("status", "num", "money", "diamond")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    NUM_FIELD_NUMBER: _ClassVar[int]
    MONEY_FIELD_NUMBER: _ClassVar[int]
    DIAMOND_FIELD_NUMBER: _ClassVar[int]
    status: int
    num: int
    money: int
    diamond: int
    def __init__(self, status: _Optional[int] = ..., num: _Optional[int] = ..., money: _Optional[int] = ..., diamond: _Optional[int] = ...) -> None: ...

class pbreq_mgame_use(_message.Message):
    __slots__ = ("map_id",)
    MAP_ID_FIELD_NUMBER: _ClassVar[int]
    map_id: int
    def __init__(self, map_id: _Optional[int] = ...) -> None: ...

class pbrsp_mgame_use(_message.Message):
    __slots__ = ("status", "new_prop", "old_prop", "reward")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    NEW_PROP_FIELD_NUMBER: _ClassVar[int]
    OLD_PROP_FIELD_NUMBER: _ClassVar[int]
    REWARD_FIELD_NUMBER: _ClassVar[int]
    status: int
    new_prop: _dr2_comm_pb_pb2.pb_mgame_prop
    old_prop: _dr2_comm_pb_pb2.pb_mgame_prop
    reward: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_kv]
    def __init__(self, status: _Optional[int] = ..., new_prop: _Optional[_Union[_dr2_comm_pb_pb2.pb_mgame_prop, _Mapping]] = ..., old_prop: _Optional[_Union[_dr2_comm_pb_pb2.pb_mgame_prop, _Mapping]] = ..., reward: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_kv, _Mapping]]] = ...) -> None: ...

class pbreq_mgame_vit_buy(_message.Message):
    __slots__ = ("num",)
    NUM_FIELD_NUMBER: _ClassVar[int]
    num: int
    def __init__(self, num: _Optional[int] = ...) -> None: ...

class pbrsp_mgame_vit_buy(_message.Message):
    __slots__ = ("status", "money", "diamond")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MONEY_FIELD_NUMBER: _ClassVar[int]
    DIAMOND_FIELD_NUMBER: _ClassVar[int]
    status: int
    money: int
    diamond: int
    def __init__(self, status: _Optional[int] = ..., money: _Optional[int] = ..., diamond: _Optional[int] = ...) -> None: ...

class pbreq_mgame_task(_message.Message):
    __slots__ = ("task_id", "map_id")
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    MAP_ID_FIELD_NUMBER: _ClassVar[int]
    task_id: int
    map_id: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, task_id: _Optional[int] = ..., map_id: _Optional[_Iterable[int]] = ...) -> None: ...

class pbrsp_mgame_task(_message.Message):
    __slots__ = ("status", "name")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    status: int
    name: int
    def __init__(self, status: _Optional[int] = ..., name: _Optional[int] = ...) -> None: ...

class pbreq_mgame_exchange(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class pbrsp_mgame_exchange(_message.Message):
    __slots__ = ("status", "star")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    STAR_FIELD_NUMBER: _ClassVar[int]
    status: int
    star: int
    def __init__(self, status: _Optional[int] = ..., star: _Optional[int] = ...) -> None: ...

class pbreq_mgame_match(_message.Message):
    __slots__ = ("type", "enemy", "enemy_type")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ENEMY_FIELD_NUMBER: _ClassVar[int]
    ENEMY_TYPE_FIELD_NUMBER: _ClassVar[int]
    type: int
    enemy: int
    enemy_type: int
    def __init__(self, type: _Optional[int] = ..., enemy: _Optional[int] = ..., enemy_type: _Optional[int] = ...) -> None: ...

class pbrsp_mgame_match(_message.Message):
    __slots__ = ("status", "house", "enemy")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    HOUSE_FIELD_NUMBER: _ClassVar[int]
    ENEMY_FIELD_NUMBER: _ClassVar[int]
    status: int
    house: int
    enemy: _dr2_comm_pb_pb2.pb_qlt_pvp_enemy
    def __init__(self, status: _Optional[int] = ..., house: _Optional[int] = ..., enemy: _Optional[_Union[_dr2_comm_pb_pb2.pb_qlt_pvp_enemy, _Mapping]] = ...) -> None: ...

class pbreq_mgame_play(_message.Message):
    __slots__ = ("type", "score", "pos")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    POS_FIELD_NUMBER: _ClassVar[int]
    type: int
    score: int
    pos: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, type: _Optional[int] = ..., score: _Optional[int] = ..., pos: _Optional[_Iterable[int]] = ...) -> None: ...

class pbrsp_mgame_play(_message.Message):
    __slots__ = ("status", "prop", "add_prop")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    PROP_FIELD_NUMBER: _ClassVar[int]
    ADD_PROP_FIELD_NUMBER: _ClassVar[int]
    status: int
    prop: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_mgame_prop]
    add_prop: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_mgame_prop]
    def __init__(self, status: _Optional[int] = ..., prop: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_mgame_prop, _Mapping]]] = ..., add_prop: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_mgame_prop, _Mapping]]] = ...) -> None: ...

class pbreq_mgame_up(_message.Message):
    __slots__ = ("map_id",)
    MAP_ID_FIELD_NUMBER: _ClassVar[int]
    map_id: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, map_id: _Optional[_Iterable[int]] = ...) -> None: ...

class pbrsp_mgame_up(_message.Message):
    __slots__ = ("status", "money", "diamond")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MONEY_FIELD_NUMBER: _ClassVar[int]
    DIAMOND_FIELD_NUMBER: _ClassVar[int]
    status: int
    money: int
    diamond: int
    def __init__(self, status: _Optional[int] = ..., money: _Optional[int] = ..., diamond: _Optional[int] = ...) -> None: ...

class pbreq_mgame_thaw(_message.Message):
    __slots__ = ("map_id",)
    MAP_ID_FIELD_NUMBER: _ClassVar[int]
    map_id: int
    def __init__(self, map_id: _Optional[int] = ...) -> None: ...

class pbrsp_mgame_thaw(_message.Message):
    __slots__ = ("status", "prop", "money", "diamond")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    PROP_FIELD_NUMBER: _ClassVar[int]
    MONEY_FIELD_NUMBER: _ClassVar[int]
    DIAMOND_FIELD_NUMBER: _ClassVar[int]
    status: int
    prop: _dr2_comm_pb_pb2.pb_mgame_prop
    money: int
    diamond: int
    def __init__(self, status: _Optional[int] = ..., prop: _Optional[_Union[_dr2_comm_pb_pb2.pb_mgame_prop, _Mapping]] = ..., money: _Optional[int] = ..., diamond: _Optional[int] = ...) -> None: ...

class pbreq_mgame_love(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class pbrsp_mgame_love(_message.Message):
    __slots__ = ("status", "num", "props")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    NUM_FIELD_NUMBER: _ClassVar[int]
    PROPS_FIELD_NUMBER: _ClassVar[int]
    status: int
    num: int
    props: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, status: _Optional[int] = ..., num: _Optional[int] = ..., props: _Optional[_Iterable[int]] = ...) -> None: ...

class pbreq_mgame_love_out(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class pbrsp_mgame_love_out(_message.Message):
    __slots__ = ("status", "num", "props", "house_out")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    NUM_FIELD_NUMBER: _ClassVar[int]
    PROPS_FIELD_NUMBER: _ClassVar[int]
    HOUSE_OUT_FIELD_NUMBER: _ClassVar[int]
    status: int
    num: int
    props: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_mgame_prop]
    house_out: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, status: _Optional[int] = ..., num: _Optional[int] = ..., props: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_mgame_prop, _Mapping]]] = ..., house_out: _Optional[_Iterable[int]] = ...) -> None: ...

class pbreq_flora_sync(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class pbrsp_flora_sync(_message.Message):
    __slots__ = ("status", "stage", "space_num", "reward", "num")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    STAGE_FIELD_NUMBER: _ClassVar[int]
    SPACE_NUM_FIELD_NUMBER: _ClassVar[int]
    REWARD_FIELD_NUMBER: _ClassVar[int]
    NUM_FIELD_NUMBER: _ClassVar[int]
    status: int
    stage: int
    space_num: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_kv]
    reward: _containers.RepeatedScalarFieldContainer[int]
    num: int
    def __init__(self, status: _Optional[int] = ..., stage: _Optional[int] = ..., space_num: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_kv, _Mapping]]] = ..., reward: _Optional[_Iterable[int]] = ..., num: _Optional[int] = ...) -> None: ...

class pbreq_flora_space(_message.Message):
    __slots__ = ("stage", "pos", "space", "type")
    STAGE_FIELD_NUMBER: _ClassVar[int]
    POS_FIELD_NUMBER: _ClassVar[int]
    SPACE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    stage: int
    pos: int
    space: int
    type: int
    def __init__(self, stage: _Optional[int] = ..., pos: _Optional[int] = ..., space: _Optional[int] = ..., type: _Optional[int] = ...) -> None: ...

class pbrsp_flora_space(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_flora_play(_message.Message):
    __slots__ = ("stage",)
    STAGE_FIELD_NUMBER: _ClassVar[int]
    stage: int
    def __init__(self, stage: _Optional[int] = ...) -> None: ...

class pbrsp_flora_play(_message.Message):
    __slots__ = ("status", "reward", "reward2")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    REWARD_FIELD_NUMBER: _ClassVar[int]
    REWARD2_FIELD_NUMBER: _ClassVar[int]
    status: int
    reward: _dr2_comm_pb_pb2.pb_bag
    reward2: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_kv]
    def __init__(self, status: _Optional[int] = ..., reward: _Optional[_Union[_dr2_comm_pb_pb2.pb_bag, _Mapping]] = ..., reward2: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_kv, _Mapping]]] = ...) -> None: ...

class pbreq_flora_space_exchange(_message.Message):
    __slots__ = ("id", "num")
    ID_FIELD_NUMBER: _ClassVar[int]
    NUM_FIELD_NUMBER: _ClassVar[int]
    id: int
    num: int
    def __init__(self, id: _Optional[int] = ..., num: _Optional[int] = ...) -> None: ...

class pbrsp_flora_space_exchange(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_flora_map(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class pbrsp_flora_map(_message.Message):
    __slots__ = ("status", "map")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MAP_FIELD_NUMBER: _ClassVar[int]
    status: int
    map: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, status: _Optional[int] = ..., map: _Optional[_Iterable[int]] = ...) -> None: ...

class pbreq_flora_reward(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class pbrsp_flora_reward(_message.Message):
    __slots__ = ("status", "reward")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    REWARD_FIELD_NUMBER: _ClassVar[int]
    status: int
    reward: _dr2_comm_pb_pb2.pb_bag
    def __init__(self, status: _Optional[int] = ..., reward: _Optional[_Union[_dr2_comm_pb_pb2.pb_bag, _Mapping]] = ...) -> None: ...

class pbreq_world_sync(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class pbrsp_world_sync(_message.Message):
    __slots__ = ("status", "builds", "job", "cd", "apply", "udk", "reward", "start_cd")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    BUILDS_FIELD_NUMBER: _ClassVar[int]
    JOB_FIELD_NUMBER: _ClassVar[int]
    CD_FIELD_NUMBER: _ClassVar[int]
    APPLY_FIELD_NUMBER: _ClassVar[int]
    UDK_FIELD_NUMBER: _ClassVar[int]
    REWARD_FIELD_NUMBER: _ClassVar[int]
    START_CD_FIELD_NUMBER: _ClassVar[int]
    status: int
    builds: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_world_build]
    job: int
    cd: int
    apply: int
    udk: str
    reward: _dr2_comm_pb_pb2.pb_bag
    start_cd: int
    def __init__(self, status: _Optional[int] = ..., builds: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_world_build, _Mapping]]] = ..., job: _Optional[int] = ..., cd: _Optional[int] = ..., apply: _Optional[int] = ..., udk: _Optional[str] = ..., reward: _Optional[_Union[_dr2_comm_pb_pb2.pb_bag, _Mapping]] = ..., start_cd: _Optional[int] = ...) -> None: ...

class pbreq_world_op(_message.Message):
    __slots__ = ("id", "type")
    ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    id: int
    type: int
    def __init__(self, id: _Optional[int] = ..., type: _Optional[int] = ...) -> None: ...

class pbrsp_world_op(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_world_apply(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class pbrsp_world_apply(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_world_collect(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class pbrsp_world_collect(_message.Message):
    __slots__ = ("status", "reward", "adds", "res")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    REWARD_FIELD_NUMBER: _ClassVar[int]
    ADDS_FIELD_NUMBER: _ClassVar[int]
    RES_FIELD_NUMBER: _ClassVar[int]
    status: int
    reward: _dr2_comm_pb_pb2.pb_bag
    adds: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_kv]
    res: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_kv2]
    def __init__(self, status: _Optional[int] = ..., reward: _Optional[_Union[_dr2_comm_pb_pb2.pb_bag, _Mapping]] = ..., adds: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_kv, _Mapping]]] = ..., res: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_kv2, _Mapping]]] = ...) -> None: ...

class pbreq_world_product(_message.Message):
    __slots__ = ("id", "items", "num")
    ID_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    NUM_FIELD_NUMBER: _ClassVar[int]
    id: int
    items: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_item]
    num: int
    def __init__(self, id: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_item, _Mapping]]] = ..., num: _Optional[int] = ...) -> None: ...

class pbrsp_world_product(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_world_product_grid(_message.Message):
    __slots__ = ("id", "num")
    ID_FIELD_NUMBER: _ClassVar[int]
    NUM_FIELD_NUMBER: _ClassVar[int]
    id: int
    num: int
    def __init__(self, id: _Optional[int] = ..., num: _Optional[int] = ...) -> None: ...

class pbrsp_world_product_grid(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_world_mall_sync(_message.Message):
    __slots__ = ("id", "refresh", "offset", "itemid")
    ID_FIELD_NUMBER: _ClassVar[int]
    REFRESH_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    ITEMID_FIELD_NUMBER: _ClassVar[int]
    id: int
    refresh: int
    offset: int
    itemid: int
    def __init__(self, id: _Optional[int] = ..., refresh: _Optional[int] = ..., offset: _Optional[int] = ..., itemid: _Optional[int] = ...) -> None: ...

class pbrsp_world_mall_sync(_message.Message):
    __slots__ = ("status", "my_orders", "orders", "publish", "accepted", "buy")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MY_ORDERS_FIELD_NUMBER: _ClassVar[int]
    ORDERS_FIELD_NUMBER: _ClassVar[int]
    PUBLISH_FIELD_NUMBER: _ClassVar[int]
    ACCEPTED_FIELD_NUMBER: _ClassVar[int]
    BUY_FIELD_NUMBER: _ClassVar[int]
    status: int
    my_orders: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_world_mall_item]
    orders: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_world_mall_item]
    publish: int
    accepted: int
    buy: int
    def __init__(self, status: _Optional[int] = ..., my_orders: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_world_mall_item, _Mapping]]] = ..., orders: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_world_mall_item, _Mapping]]] = ..., publish: _Optional[int] = ..., accepted: _Optional[int] = ..., buy: _Optional[int] = ...) -> None: ...

class pbreq_world_mall_up(_message.Message):
    __slots__ = ("id", "cost", "reward")
    ID_FIELD_NUMBER: _ClassVar[int]
    COST_FIELD_NUMBER: _ClassVar[int]
    REWARD_FIELD_NUMBER: _ClassVar[int]
    id: int
    cost: _dr2_comm_pb_pb2.pb_item
    reward: _dr2_comm_pb_pb2.pb_item
    def __init__(self, id: _Optional[int] = ..., cost: _Optional[_Union[_dr2_comm_pb_pb2.pb_item, _Mapping]] = ..., reward: _Optional[_Union[_dr2_comm_pb_pb2.pb_item, _Mapping]] = ...) -> None: ...

class pbrsp_world_mall_up(_message.Message):
    __slots__ = ("status", "orderid")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ORDERID_FIELD_NUMBER: _ClassVar[int]
    status: int
    orderid: str
    def __init__(self, status: _Optional[int] = ..., orderid: _Optional[str] = ...) -> None: ...

class pbreq_world_mall_down(_message.Message):
    __slots__ = ("id", "orderid", "type")
    ID_FIELD_NUMBER: _ClassVar[int]
    ORDERID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    id: int
    orderid: str
    type: int
    def __init__(self, id: _Optional[int] = ..., orderid: _Optional[str] = ..., type: _Optional[int] = ...) -> None: ...

class pbrsp_world_mall_down(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_world_mall_grid(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class pbrsp_world_mall_grid(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_world_pk_match(_message.Message):
    __slots__ = ("type",)
    TYPE_FIELD_NUMBER: _ClassVar[int]
    type: int
    def __init__(self, type: _Optional[int] = ...) -> None: ...

class pbrsp_world_pk_match(_message.Message):
    __slots__ = ("status", "enemy")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ENEMY_FIELD_NUMBER: _ClassVar[int]
    status: int
    enemy: _dr2_comm_pb_pb2.pb_smbr
    def __init__(self, status: _Optional[int] = ..., enemy: _Optional[_Union[_dr2_comm_pb_pb2.pb_smbr, _Mapping]] = ...) -> None: ...

class pbreq_world_pk(_message.Message):
    __slots__ = ("udk", "type", "camp", "tid")
    UDK_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    CAMP_FIELD_NUMBER: _ClassVar[int]
    TID_FIELD_NUMBER: _ClassVar[int]
    udk: str
    type: int
    camp: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_unit]
    tid: int
    def __init__(self, udk: _Optional[str] = ..., type: _Optional[int] = ..., camp: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_unit, _Mapping]]] = ..., tid: _Optional[int] = ...) -> None: ...

class pbrsp_world_pk(_message.Message):
    __slots__ = ("status", "log")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    LOG_FIELD_NUMBER: _ClassVar[int]
    status: int
    log: _dr2_comm_pb_pb2.pb_qlog
    def __init__(self, status: _Optional[int] = ..., log: _Optional[_Union[_dr2_comm_pb_pb2.pb_qlog, _Mapping]] = ...) -> None: ...

class pbreq_world_pk_log(_message.Message):
    __slots__ = ("type",)
    TYPE_FIELD_NUMBER: _ClassVar[int]
    type: int
    def __init__(self, type: _Optional[int] = ...) -> None: ...

class pbrsp_world_pk_log(_message.Message):
    __slots__ = ("status", "log")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    LOG_FIELD_NUMBER: _ClassVar[int]
    status: int
    log: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_qlog]
    def __init__(self, status: _Optional[int] = ..., log: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_qlog, _Mapping]]] = ...) -> None: ...

class pbreq_world_pk_rank(_message.Message):
    __slots__ = ("type",)
    TYPE_FIELD_NUMBER: _ClassVar[int]
    type: int
    def __init__(self, type: _Optional[int] = ...) -> None: ...

class pbrsp_world_pk_rank(_message.Message):
    __slots__ = ("status", "rank", "camp", "power", "bomb")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    RANK_FIELD_NUMBER: _ClassVar[int]
    CAMP_FIELD_NUMBER: _ClassVar[int]
    POWER_FIELD_NUMBER: _ClassVar[int]
    BOMB_FIELD_NUMBER: _ClassVar[int]
    status: int
    rank: _dr2_comm_pb_pb2.pb_smbrs
    camp: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_unit]
    power: int
    bomb: bool
    def __init__(self, status: _Optional[int] = ..., rank: _Optional[_Union[_dr2_comm_pb_pb2.pb_smbrs, _Mapping]] = ..., camp: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_unit, _Mapping]]] = ..., power: _Optional[int] = ..., bomb: _Optional[bool] = ...) -> None: ...

class pbreq_world_cele_sync(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class pbrsp_world_cele_sync(_message.Message):
    __slots__ = ("status", "reward", "cele")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    REWARD_FIELD_NUMBER: _ClassVar[int]
    CELE_FIELD_NUMBER: _ClassVar[int]
    status: int
    reward: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_item]
    cele: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_cele]
    def __init__(self, status: _Optional[int] = ..., reward: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_item, _Mapping]]] = ..., cele: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_cele, _Mapping]]] = ...) -> None: ...

class pbreq_world_cele_op(_message.Message):
    __slots__ = ("type", "id", "hid")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    HID_FIELD_NUMBER: _ClassVar[int]
    type: int
    id: int
    hid: int
    def __init__(self, type: _Optional[int] = ..., id: _Optional[int] = ..., hid: _Optional[int] = ...) -> None: ...

class pbrsp_world_cele_op(_message.Message):
    __slots__ = ("status", "reward", "cele")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    REWARD_FIELD_NUMBER: _ClassVar[int]
    CELE_FIELD_NUMBER: _ClassVar[int]
    status: int
    reward: _dr2_comm_pb_pb2.pb_bag
    cele: _dr2_comm_pb_pb2.pb_cele
    def __init__(self, status: _Optional[int] = ..., reward: _Optional[_Union[_dr2_comm_pb_pb2.pb_bag, _Mapping]] = ..., cele: _Optional[_Union[_dr2_comm_pb_pb2.pb_cele, _Mapping]] = ...) -> None: ...

class pbreq_bworld_sync(_message.Message):
    __slots__ = ("world_id", "type", "lv")
    WORLD_ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    LV_FIELD_NUMBER: _ClassVar[int]
    world_id: int
    type: int
    lv: int
    def __init__(self, world_id: _Optional[int] = ..., type: _Optional[int] = ..., lv: _Optional[int] = ...) -> None: ...

class pbrsp_bworld_sync(_message.Message):
    __slots__ = ("status", "bworld", "teams", "hps", "cd", "group_id", "udk", "fire_ids", "vits", "day_cd", "color", "samples", "skill_count")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    BWORLD_FIELD_NUMBER: _ClassVar[int]
    TEAMS_FIELD_NUMBER: _ClassVar[int]
    HPS_FIELD_NUMBER: _ClassVar[int]
    CD_FIELD_NUMBER: _ClassVar[int]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    UDK_FIELD_NUMBER: _ClassVar[int]
    FIRE_IDS_FIELD_NUMBER: _ClassVar[int]
    VITS_FIELD_NUMBER: _ClassVar[int]
    DAY_CD_FIELD_NUMBER: _ClassVar[int]
    COLOR_FIELD_NUMBER: _ClassVar[int]
    SAMPLES_FIELD_NUMBER: _ClassVar[int]
    SKILL_COUNT_FIELD_NUMBER: _ClassVar[int]
    status: int
    bworld: _dr2_comm_pb_pb2.pb_bworld
    teams: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_bworld_team]
    hps: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_kv2]
    cd: int
    group_id: int
    udk: str
    fire_ids: _containers.RepeatedScalarFieldContainer[int]
    vits: _containers.RepeatedScalarFieldContainer[int]
    day_cd: int
    color: int
    samples: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_kv2]
    skill_count: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_kv2]
    def __init__(self, status: _Optional[int] = ..., bworld: _Optional[_Union[_dr2_comm_pb_pb2.pb_bworld, _Mapping]] = ..., teams: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_bworld_team, _Mapping]]] = ..., hps: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_kv2, _Mapping]]] = ..., cd: _Optional[int] = ..., group_id: _Optional[int] = ..., udk: _Optional[str] = ..., fire_ids: _Optional[_Iterable[int]] = ..., vits: _Optional[_Iterable[int]] = ..., day_cd: _Optional[int] = ..., color: _Optional[int] = ..., samples: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_kv2, _Mapping]]] = ..., skill_count: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_kv2, _Mapping]]] = ...) -> None: ...

class pbreq_bworld_set_team(_message.Message):
    __slots__ = ("teamid", "camp", "type", "soldiers")
    TEAMID_FIELD_NUMBER: _ClassVar[int]
    CAMP_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    SOLDIERS_FIELD_NUMBER: _ClassVar[int]
    teamid: int
    camp: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_unit]
    type: int
    soldiers: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, teamid: _Optional[int] = ..., camp: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_unit, _Mapping]]] = ..., type: _Optional[int] = ..., soldiers: _Optional[_Iterable[int]] = ...) -> None: ...

class pbrsp_bworld_set_team(_message.Message):
    __slots__ = ("status", "power")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    POWER_FIELD_NUMBER: _ClassVar[int]
    status: int
    power: int
    def __init__(self, status: _Optional[int] = ..., power: _Optional[int] = ...) -> None: ...

class pbreq_bworld_build_op(_message.Message):
    __slots__ = ("op_type", "world_id", "key", "ship_key", "material", "id_cfg")
    OP_TYPE_FIELD_NUMBER: _ClassVar[int]
    WORLD_ID_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    SHIP_KEY_FIELD_NUMBER: _ClassVar[int]
    MATERIAL_FIELD_NUMBER: _ClassVar[int]
    ID_CFG_FIELD_NUMBER: _ClassVar[int]
    op_type: int
    world_id: int
    key: int
    ship_key: int
    material: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_item]
    id_cfg: int
    def __init__(self, op_type: _Optional[int] = ..., world_id: _Optional[int] = ..., key: _Optional[int] = ..., ship_key: _Optional[int] = ..., material: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_item, _Mapping]]] = ..., id_cfg: _Optional[int] = ...) -> None: ...

class pbrsp_bworld_build_op(_message.Message):
    __slots__ = ("status", "moudle", "reward")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MOUDLE_FIELD_NUMBER: _ClassVar[int]
    REWARD_FIELD_NUMBER: _ClassVar[int]
    status: int
    moudle: _dr2_comm_pb_pb2.pb_bworld_moudle
    reward: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_item]
    def __init__(self, status: _Optional[int] = ..., moudle: _Optional[_Union[_dr2_comm_pb_pb2.pb_bworld_moudle, _Mapping]] = ..., reward: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_item, _Mapping]]] = ...) -> None: ...

class pbreq_bworld_build_move(_message.Message):
    __slots__ = ("key",)
    KEY_FIELD_NUMBER: _ClassVar[int]
    key: int
    def __init__(self, key: _Optional[int] = ...) -> None: ...

class pbrsp_bworld_build_move(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_bworld_resource(_message.Message):
    __slots__ = ("type", "world_id", "path", "teamid", "target_key")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    WORLD_ID_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    TEAMID_FIELD_NUMBER: _ClassVar[int]
    TARGET_KEY_FIELD_NUMBER: _ClassVar[int]
    type: int
    world_id: int
    path: _containers.RepeatedScalarFieldContainer[int]
    teamid: int
    target_key: int
    def __init__(self, type: _Optional[int] = ..., world_id: _Optional[int] = ..., path: _Optional[_Iterable[int]] = ..., teamid: _Optional[int] = ..., target_key: _Optional[int] = ...) -> None: ...

class pbrsp_bworld_resource(_message.Message):
    __slots__ = ("status", "reward")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    REWARD_FIELD_NUMBER: _ClassVar[int]
    status: int
    reward: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_item]
    def __init__(self, status: _Optional[int] = ..., reward: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_item, _Mapping]]] = ...) -> None: ...

class pbreq_bworld_op(_message.Message):
    __slots__ = ("type", "udk", "world_id", "txt", "key", "moudle_id", "call_type")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    UDK_FIELD_NUMBER: _ClassVar[int]
    WORLD_ID_FIELD_NUMBER: _ClassVar[int]
    TXT_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    MOUDLE_ID_FIELD_NUMBER: _ClassVar[int]
    CALL_TYPE_FIELD_NUMBER: _ClassVar[int]
    type: int
    udk: str
    world_id: int
    txt: str
    key: int
    moudle_id: int
    call_type: int
    def __init__(self, type: _Optional[int] = ..., udk: _Optional[str] = ..., world_id: _Optional[int] = ..., txt: _Optional[str] = ..., key: _Optional[int] = ..., moudle_id: _Optional[int] = ..., call_type: _Optional[int] = ...) -> None: ...

class pbrsp_bworld_op(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_bworld_small_sync(_message.Message):
    __slots__ = ("type",)
    TYPE_FIELD_NUMBER: _ClassVar[int]
    type: int
    def __init__(self, type: _Optional[int] = ...) -> None: ...

class pbrsp_bworld_small_sync(_message.Message):
    __slots__ = ("status", "cd", "fog", "existing", "worlds")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    CD_FIELD_NUMBER: _ClassVar[int]
    FOG_FIELD_NUMBER: _ClassVar[int]
    EXISTING_FIELD_NUMBER: _ClassVar[int]
    WORLDS_FIELD_NUMBER: _ClassVar[int]
    status: int
    cd: int
    fog: int
    existing: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_kv2]
    worlds: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_kv2]
    def __init__(self, status: _Optional[int] = ..., cd: _Optional[int] = ..., fog: _Optional[int] = ..., existing: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_kv2, _Mapping]]] = ..., worlds: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_kv2, _Mapping]]] = ...) -> None: ...

class pbreq_bworld_video(_message.Message):
    __slots__ = ("type", "index")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    type: int
    index: int
    def __init__(self, type: _Optional[int] = ..., index: _Optional[int] = ...) -> None: ...

class pbrsp_bworld_video(_message.Message):
    __slots__ = ("status", "v1", "v2")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    V1_FIELD_NUMBER: _ClassVar[int]
    V2_FIELD_NUMBER: _ClassVar[int]
    status: int
    v1: _dr2_comm_pb_pb2.pb_qlog
    v2: _dr2_comm_pb_pb2.pb_bworld_video
    def __init__(self, status: _Optional[int] = ..., v1: _Optional[_Union[_dr2_comm_pb_pb2.pb_qlog, _Mapping]] = ..., v2: _Optional[_Union[_dr2_comm_pb_pb2.pb_bworld_video, _Mapping]] = ...) -> None: ...

class pbreq_bworld_station(_message.Message):
    __slots__ = ("world_id", "key", "teamid", "id_cfg")
    WORLD_ID_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    TEAMID_FIELD_NUMBER: _ClassVar[int]
    ID_CFG_FIELD_NUMBER: _ClassVar[int]
    world_id: int
    key: int
    teamid: int
    id_cfg: int
    def __init__(self, world_id: _Optional[int] = ..., key: _Optional[int] = ..., teamid: _Optional[int] = ..., id_cfg: _Optional[int] = ...) -> None: ...

class pbrsp_bworld_station(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_bworld_chat(_message.Message):
    __slots__ = ("chat", "world_id")
    CHAT_FIELD_NUMBER: _ClassVar[int]
    WORLD_ID_FIELD_NUMBER: _ClassVar[int]
    chat: str
    world_id: int
    def __init__(self, chat: _Optional[str] = ..., world_id: _Optional[int] = ...) -> None: ...

class pbrsp_bworld_chat(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_bworld_chat_log(_message.Message):
    __slots__ = ("world_id",)
    WORLD_ID_FIELD_NUMBER: _ClassVar[int]
    world_id: int
    def __init__(self, world_id: _Optional[int] = ...) -> None: ...

class pbrsp_bworld_chat_log(_message.Message):
    __slots__ = ("status", "chat")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    CHAT_FIELD_NUMBER: _ClassVar[int]
    status: int
    chat: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_chat]
    def __init__(self, status: _Optional[int] = ..., chat: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_chat, _Mapping]]] = ...) -> None: ...

class pbreq_bworld_walk(_message.Message):
    __slots__ = ("world_id", "path", "teamid", "target_key", "ship_key", "moudle_id")
    WORLD_ID_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    TEAMID_FIELD_NUMBER: _ClassVar[int]
    TARGET_KEY_FIELD_NUMBER: _ClassVar[int]
    SHIP_KEY_FIELD_NUMBER: _ClassVar[int]
    MOUDLE_ID_FIELD_NUMBER: _ClassVar[int]
    world_id: int
    path: _containers.RepeatedScalarFieldContainer[int]
    teamid: int
    target_key: int
    ship_key: int
    moudle_id: int
    def __init__(self, world_id: _Optional[int] = ..., path: _Optional[_Iterable[int]] = ..., teamid: _Optional[int] = ..., target_key: _Optional[int] = ..., ship_key: _Optional[int] = ..., moudle_id: _Optional[int] = ...) -> None: ...

class pbrsp_bworld_walk(_message.Message):
    __slots__ = ("status", "video", "team", "reward")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    VIDEO_FIELD_NUMBER: _ClassVar[int]
    TEAM_FIELD_NUMBER: _ClassVar[int]
    REWARD_FIELD_NUMBER: _ClassVar[int]
    status: int
    video: _dr2_comm_pb_pb2.pb_bworld_video
    team: _dr2_comm_pb_pb2.pb_bworld_team
    reward: _dr2_comm_pb_pb2.pb_bag
    def __init__(self, status: _Optional[int] = ..., video: _Optional[_Union[_dr2_comm_pb_pb2.pb_bworld_video, _Mapping]] = ..., team: _Optional[_Union[_dr2_comm_pb_pb2.pb_bworld_team, _Mapping]] = ..., reward: _Optional[_Union[_dr2_comm_pb_pb2.pb_bag, _Mapping]] = ...) -> None: ...

class pbreq_bworld_pinfo(_message.Message):
    __slots__ = ("key", "world_id")
    KEY_FIELD_NUMBER: _ClassVar[int]
    WORLD_ID_FIELD_NUMBER: _ClassVar[int]
    key: int
    world_id: int
    def __init__(self, key: _Optional[int] = ..., world_id: _Optional[int] = ...) -> None: ...

class pbrsp_bworld_pinfo(_message.Message):
    __slots__ = ("status", "ship", "build", "monster", "moudle", "station")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    SHIP_FIELD_NUMBER: _ClassVar[int]
    BUILD_FIELD_NUMBER: _ClassVar[int]
    MONSTER_FIELD_NUMBER: _ClassVar[int]
    MOUDLE_FIELD_NUMBER: _ClassVar[int]
    STATION_FIELD_NUMBER: _ClassVar[int]
    status: int
    ship: _dr2_comm_pb_pb2.pb_smbr
    build: _dr2_comm_pb_pb2.pb_bworld_build
    monster: _dr2_comm_pb_pb2.pb_bworld_monster
    moudle: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_bworld_moudle]
    station: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_kv]
    def __init__(self, status: _Optional[int] = ..., ship: _Optional[_Union[_dr2_comm_pb_pb2.pb_smbr, _Mapping]] = ..., build: _Optional[_Union[_dr2_comm_pb_pb2.pb_bworld_build, _Mapping]] = ..., monster: _Optional[_Union[_dr2_comm_pb_pb2.pb_bworld_monster, _Mapping]] = ..., moudle: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_bworld_moudle, _Mapping]]] = ..., station: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_kv, _Mapping]]] = ...) -> None: ...

class pbreq_bworld_ship_back(_message.Message):
    __slots__ = ("teamid",)
    TEAMID_FIELD_NUMBER: _ClassVar[int]
    teamid: int
    def __init__(self, teamid: _Optional[int] = ...) -> None: ...

class pbrsp_bworld_ship_back(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_bworld_buy_act(_message.Message):
    __slots__ = ("num", "teamid", "type")
    NUM_FIELD_NUMBER: _ClassVar[int]
    TEAMID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    num: int
    teamid: int
    type: int
    def __init__(self, num: _Optional[int] = ..., teamid: _Optional[int] = ..., type: _Optional[int] = ...) -> None: ...

class pbrsp_bworld_buy_act(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_bworld_member(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class pbrsp_bworld_member(_message.Message):
    __slots__ = ("status", "members", "flag", "invite", "state")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MEMBERS_FIELD_NUMBER: _ClassVar[int]
    FLAG_FIELD_NUMBER: _ClassVar[int]
    INVITE_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    status: int
    members: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_smbr]
    flag: int
    invite: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_smbr]
    state: int
    def __init__(self, status: _Optional[int] = ..., members: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_smbr, _Mapping]]] = ..., flag: _Optional[int] = ..., invite: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_smbr, _Mapping]]] = ..., state: _Optional[int] = ...) -> None: ...

class pbreq_bworld_exit(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class pbrsp_bworld_exit(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class pbreq_bworld_use_item(_message.Message):
    __slots__ = ("item", "hids")
    ITEM_FIELD_NUMBER: _ClassVar[int]
    HIDS_FIELD_NUMBER: _ClassVar[int]
    item: _dr2_comm_pb_pb2.pb_item
    hids: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, item: _Optional[_Union[_dr2_comm_pb_pb2.pb_item, _Mapping]] = ..., hids: _Optional[_Iterable[int]] = ...) -> None: ...

class pbrsp_bworld_use_item(_message.Message):
    __slots__ = ("status", "hps")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    HPS_FIELD_NUMBER: _ClassVar[int]
    status: int
    hps: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_kv2]
    def __init__(self, status: _Optional[int] = ..., hps: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_kv2, _Mapping]]] = ...) -> None: ...

class pbreq_bworld_sinfo(_message.Message):
    __slots__ = ("keys", "world_id")
    KEYS_FIELD_NUMBER: _ClassVar[int]
    WORLD_ID_FIELD_NUMBER: _ClassVar[int]
    keys: _containers.RepeatedScalarFieldContainer[int]
    world_id: int
    def __init__(self, keys: _Optional[_Iterable[int]] = ..., world_id: _Optional[int] = ...) -> None: ...

class pbrsp_bworld_sinfo(_message.Message):
    __slots__ = ("status", "ships")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    SHIPS_FIELD_NUMBER: _ClassVar[int]
    status: int
    ships: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_smbr]
    def __init__(self, status: _Optional[int] = ..., ships: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_smbr, _Mapping]]] = ...) -> None: ...

class pbreq_bworld_chat_sync(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class pbrsp_bworld_chat_sync(_message.Message):
    __slots__ = ("status", "show", "world_id", "chat", "recruit", "log")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    SHOW_FIELD_NUMBER: _ClassVar[int]
    WORLD_ID_FIELD_NUMBER: _ClassVar[int]
    CHAT_FIELD_NUMBER: _ClassVar[int]
    RECRUIT_FIELD_NUMBER: _ClassVar[int]
    LOG_FIELD_NUMBER: _ClassVar[int]
    status: int
    show: int
    world_id: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_kv]
    chat: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_chat]
    recruit: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_chat]
    log: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_bworld_log]
    def __init__(self, status: _Optional[int] = ..., show: _Optional[int] = ..., world_id: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_kv, _Mapping]]] = ..., chat: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_chat, _Mapping]]] = ..., recruit: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_chat, _Mapping]]] = ..., log: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_bworld_log, _Mapping]]] = ...) -> None: ...

class pbreq_bworld_hps(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class pbrsp_bworld_hps(_message.Message):
    __slots__ = ("status", "hps")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    HPS_FIELD_NUMBER: _ClassVar[int]
    status: int
    hps: _containers.RepeatedCompositeFieldContainer[_dr2_comm_pb_pb2.pb_kv2]
    def __init__(self, status: _Optional[int] = ..., hps: _Optional[_Iterable[_Union[_dr2_comm_pb_pb2.pb_kv2, _Mapping]]] = ...) -> None: ...

class pbreq_bworld_skill(_message.Message):
    __slots__ = ("world_id", "teamid", "target_key", "id_god", "id_skill", "keys")
    WORLD_ID_FIELD_NUMBER: _ClassVar[int]
    TEAMID_FIELD_NUMBER: _ClassVar[int]
    TARGET_KEY_FIELD_NUMBER: _ClassVar[int]
    ID_GOD_FIELD_NUMBER: _ClassVar[int]
    ID_SKILL_FIELD_NUMBER: _ClassVar[int]
    KEYS_FIELD_NUMBER: _ClassVar[int]
    world_id: int
    teamid: int
    target_key: int
    id_god: int
    id_skill: int
    keys: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, world_id: _Optional[int] = ..., teamid: _Optional[int] = ..., target_key: _Optional[int] = ..., id_god: _Optional[int] = ..., id_skill: _Optional[int] = ..., keys: _Optional[_Iterable[int]] = ...) -> None: ...

class pbrsp_bworld_skill(_message.Message):
    __slots__ = ("status", "reward")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    REWARD_FIELD_NUMBER: _ClassVar[int]
    status: int
    reward: _dr2_comm_pb_pb2.pb_bag
    def __init__(self, status: _Optional[int] = ..., reward: _Optional[_Union[_dr2_comm_pb_pb2.pb_bag, _Mapping]] = ...) -> None: ...
