import typing

import typing_extensions

@typing.type_check_only
class NotificationSetting(typing_extensions.TypedDict, total=False):
    name: str
    notificationTypes: typing.List[str]
    pubsubTopic: str
