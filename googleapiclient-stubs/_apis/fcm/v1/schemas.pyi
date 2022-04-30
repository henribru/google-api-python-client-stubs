import typing

import typing_extensions

_list = list

@typing.type_check_only
class AndroidConfig(typing_extensions.TypedDict, total=False):
    collapseKey: str
    data: dict[str, typing.Any]
    directBootOk: bool
    fcmOptions: AndroidFcmOptions
    notification: AndroidNotification
    priority: typing_extensions.Literal["NORMAL", "HIGH"]
    restrictedPackageName: str
    ttl: str

@typing.type_check_only
class AndroidFcmOptions(typing_extensions.TypedDict, total=False):
    analyticsLabel: str

@typing.type_check_only
class AndroidNotification(typing_extensions.TypedDict, total=False):
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
    notificationPriority: typing_extensions.Literal[
        "PRIORITY_UNSPECIFIED",
        "PRIORITY_MIN",
        "PRIORITY_LOW",
        "PRIORITY_DEFAULT",
        "PRIORITY_HIGH",
        "PRIORITY_MAX",
    ]
    sound: str
    sticky: bool
    tag: str
    ticker: str
    title: str
    titleLocArgs: _list[str]
    titleLocKey: str
    vibrateTimings: _list[str]
    visibility: typing_extensions.Literal[
        "VISIBILITY_UNSPECIFIED", "PRIVATE", "PUBLIC", "SECRET"
    ]

@typing.type_check_only
class ApnsConfig(typing_extensions.TypedDict, total=False):
    fcmOptions: ApnsFcmOptions
    headers: dict[str, typing.Any]
    payload: dict[str, typing.Any]

@typing.type_check_only
class ApnsFcmOptions(typing_extensions.TypedDict, total=False):
    analyticsLabel: str
    image: str

@typing.type_check_only
class Color(typing_extensions.TypedDict, total=False):
    alpha: float
    blue: float
    green: float
    red: float

@typing.type_check_only
class FcmOptions(typing_extensions.TypedDict, total=False):
    analyticsLabel: str

@typing.type_check_only
class LightSettings(typing_extensions.TypedDict, total=False):
    color: Color
    lightOffDuration: str
    lightOnDuration: str

@typing.type_check_only
class Message(typing_extensions.TypedDict, total=False):
    android: AndroidConfig
    apns: ApnsConfig
    condition: str
    data: dict[str, typing.Any]
    fcmOptions: FcmOptions
    name: str
    notification: Notification
    token: str
    topic: str
    webpush: WebpushConfig

@typing.type_check_only
class Notification(typing_extensions.TypedDict, total=False):
    body: str
    image: str
    title: str

@typing.type_check_only
class SendMessageRequest(typing_extensions.TypedDict, total=False):
    message: Message
    validateOnly: bool

@typing.type_check_only
class WebpushConfig(typing_extensions.TypedDict, total=False):
    data: dict[str, typing.Any]
    fcmOptions: WebpushFcmOptions
    headers: dict[str, typing.Any]
    notification: dict[str, typing.Any]

@typing.type_check_only
class WebpushFcmOptions(typing_extensions.TypedDict, total=False):
    analyticsLabel: str
    link: str
