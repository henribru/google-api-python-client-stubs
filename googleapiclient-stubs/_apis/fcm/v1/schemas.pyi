import typing

_list = list

@typing.type_check_only
class AndroidConfig(typing.TypedDict, total=False):
    bandwidthConstrainedOk: bool
    collapseKey: str
    data: dict[str, typing.Any]
    directBootOk: bool
    fcmOptions: AndroidFcmOptions
    notification: AndroidNotification
    priority: typing.Literal["NORMAL", "HIGH"]
    restrictedPackageName: str
    restrictedSatelliteOk: bool
    ttl: str

@typing.type_check_only
class AndroidFcmOptions(typing.TypedDict, total=False):
    analyticsLabel: str

@typing.type_check_only
class AndroidNotification(typing.TypedDict, total=False):
    body: str
    bodyLocArgs: _list[str]
    bodyLocKey: str
    bypassProxyNotification: bool
    channelId: str
    clickAction: str
    color: str
    defaultLightSettings: bool
    defaultSound: bool
    defaultVibrateTimings: bool
    eventTime: str
    icon: str
    image: str
    lightSettings: LightSettings
    localOnly: bool
    notificationCount: int
    notificationPriority: typing.Literal[
        "PRIORITY_UNSPECIFIED",
        "PRIORITY_MIN",
        "PRIORITY_LOW",
        "PRIORITY_DEFAULT",
        "PRIORITY_HIGH",
        "PRIORITY_MAX",
    ]
    proxy: typing.Literal["PROXY_UNSPECIFIED", "ALLOW", "DENY", "IF_PRIORITY_LOWERED"]
    sound: str
    sticky: bool
    tag: str
    ticker: str
    title: str
    titleLocArgs: _list[str]
    titleLocKey: str
    vibrateTimings: _list[str]
    visibility: typing.Literal["VISIBILITY_UNSPECIFIED", "PRIVATE", "PUBLIC", "SECRET"]

@typing.type_check_only
class ApnsConfig(typing.TypedDict, total=False):
    fcmOptions: ApnsFcmOptions
    headers: dict[str, typing.Any]
    liveActivityToken: str
    payload: dict[str, typing.Any]

@typing.type_check_only
class ApnsFcmOptions(typing.TypedDict, total=False):
    analyticsLabel: str
    image: str

@typing.type_check_only
class Color(typing.TypedDict, total=False):
    alpha: float
    blue: float
    green: float
    red: float

@typing.type_check_only
class FcmOptions(typing.TypedDict, total=False):
    analyticsLabel: str

@typing.type_check_only
class LightSettings(typing.TypedDict, total=False):
    color: Color
    lightOffDuration: str
    lightOnDuration: str

@typing.type_check_only
class Message(typing.TypedDict, total=False):
    android: AndroidConfig
    apns: ApnsConfig
    condition: str
    data: dict[str, typing.Any]
    fcmOptions: FcmOptions
    fid: str
    name: str
    notification: Notification
    token: str
    topic: str
    webpush: WebpushConfig

@typing.type_check_only
class Notification(typing.TypedDict, total=False):
    body: str
    image: str
    title: str

@typing.type_check_only
class SendMessageRequest(typing.TypedDict, total=False):
    message: Message
    validateOnly: bool

@typing.type_check_only
class WebpushConfig(typing.TypedDict, total=False):
    data: dict[str, typing.Any]
    fcmOptions: WebpushFcmOptions
    headers: dict[str, typing.Any]
    notification: dict[str, typing.Any]

@typing.type_check_only
class WebpushFcmOptions(typing.TypedDict, total=False):
    analyticsLabel: str
    link: str
