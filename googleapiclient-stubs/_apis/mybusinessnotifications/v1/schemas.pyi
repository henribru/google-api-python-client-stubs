import typing

import typing_extensions

_list = list

@typing.type_check_only
class NotificationSetting(typing_extensions.TypedDict, total=False):
    name: str
    notificationTypes: _list[str]
    pubsubTopic: str
