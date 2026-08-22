import typing

_list = list

@typing.type_check_only
class PublishUrlNotificationResponse(typing.TypedDict, total=False):
    urlNotificationMetadata: UrlNotificationMetadata

@typing.type_check_only
class UrlNotification(typing.TypedDict, total=False):
    notifyTime: str
    type: typing.Literal[
        "URL_NOTIFICATION_TYPE_UNSPECIFIED", "URL_UPDATED", "URL_DELETED"
    ]
    url: str

@typing.type_check_only
class UrlNotificationMetadata(typing.TypedDict, total=False):
    latestRemove: UrlNotification
    latestUpdate: UrlNotification
    url: str
