import typing

import typing_extensions

_list = list

@typing.type_check_only
class PublishUrlNotificationResponse(typing_extensions.TypedDict, total=False):
    urlNotificationMetadata: UrlNotificationMetadata

@typing.type_check_only
class UrlNotification(typing_extensions.TypedDict, total=False):
    notifyTime: str
    type: typing_extensions.Literal[
        "URL_NOTIFICATION_TYPE_UNSPECIFIED", "URL_UPDATED", "URL_DELETED"
    ]
    url: str

@typing.type_check_only
class UrlNotificationMetadata(typing_extensions.TypedDict, total=False):
    latestRemove: UrlNotification
    latestUpdate: UrlNotification
    url: str
