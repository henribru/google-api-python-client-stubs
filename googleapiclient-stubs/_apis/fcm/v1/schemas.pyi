import typing

import typing_extensions

class WebpushConfig(typing_extensions.TypedDict, total=False):
    fcmOptions: WebpushFcmOptions
    headers: typing.Dict[str, typing.Any]
    data: typing.Dict[str, typing.Any]
    notification: typing.Dict[str, typing.Any]

class ApnsFcmOptions(typing_extensions.TypedDict, total=False):
    image: str
    analyticsLabel: str

class FcmOptions(typing_extensions.TypedDict, total=False):
    analyticsLabel: str

class Color(typing_extensions.TypedDict, total=False):
    red: float
    green: float
    blue: float
    alpha: float

class Message(typing_extensions.TypedDict, total=False):
    topic: str
    condition: str
    apns: ApnsConfig
    webpush: WebpushConfig
    name: str
    fcmOptions: FcmOptions
    notification: Notification
    data: typing.Dict[str, typing.Any]
    android: AndroidConfig
    token: str

class LightSettings(typing_extensions.TypedDict, total=False):
    lightOffDuration: str
    lightOnDuration: str
    color: Color

class ApnsConfig(typing_extensions.TypedDict, total=False):
    headers: typing.Dict[str, typing.Any]
    fcmOptions: ApnsFcmOptions
    payload: typing.Dict[str, typing.Any]

class WebpushFcmOptions(typing_extensions.TypedDict, total=False):
    analyticsLabel: str
    link: str

class AndroidNotification(typing_extensions.TypedDict, total=False):
    bodyLocKey: str
    channelId: str
    lightSettings: LightSettings
    titleLocArgs: typing.List[str]
    clickAction: str
    localOnly: bool
    defaultVibrateTimings: bool
    title: str
    bodyLocArgs: typing.List[str]
    image: str
    vibrateTimings: typing.List[str]
    icon: str
    eventTime: str
    body: str
    sound: str
    sticky: bool
    ticker: str
    titleLocKey: str
    color: str
    notificationCount: int
    visibility: typing_extensions.Literal[
        "VISIBILITY_UNSPECIFIED", "PRIVATE", "PUBLIC", "SECRET"
    ]
    defaultSound: bool
    defaultLightSettings: bool
    tag: str
    notificationPriority: typing_extensions.Literal[
        "PRIORITY_UNSPECIFIED",
        "PRIORITY_MIN",
        "PRIORITY_LOW",
        "PRIORITY_DEFAULT",
        "PRIORITY_HIGH",
        "PRIORITY_MAX",
    ]

class AndroidFcmOptions(typing_extensions.TypedDict, total=False):
    analyticsLabel: str

class SendMessageRequest(typing_extensions.TypedDict, total=False):
    message: Message
    validateOnly: bool

class AndroidConfig(typing_extensions.TypedDict, total=False):
    restrictedPackageName: str
    data: typing.Dict[str, typing.Any]
    priority: typing_extensions.Literal["NORMAL", "HIGH"]
    ttl: str
    notification: AndroidNotification
    collapseKey: str
    directBootOk: bool
    fcmOptions: AndroidFcmOptions

class Notification(typing_extensions.TypedDict, total=False):
    title: str
    body: str
    image: str
