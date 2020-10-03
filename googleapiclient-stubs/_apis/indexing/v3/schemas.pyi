import typing

import typing_extensions

class UrlNotification(typing_extensions.TypedDict, total=False):
    type: typing_extensions.Literal[
        "URL_NOTIFICATION_TYPE_UNSPECIFIED", "URL_UPDATED", "URL_DELETED"
    ]
    url: str
    notifyTime: str

class UrlNotificationMetadata(typing_extensions.TypedDict, total=False):
    latestRemove: UrlNotification
    url: str
    latestUpdate: UrlNotification

class PublishUrlNotificationResponse(typing_extensions.TypedDict, total=False):
    urlNotificationMetadata: UrlNotificationMetadata
