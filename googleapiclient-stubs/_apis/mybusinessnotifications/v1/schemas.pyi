import typing

import typing_extensions

_list = list

@typing.type_check_only
class NotificationSetting(typing_extensions.TypedDict, total=False):
    name: str
    notificationTypes: _list[
        typing_extensions.Literal[
            "NOTIFICATION_TYPE_UNSPECIFIED",
            "GOOGLE_UPDATE",
            "NEW_REVIEW",
            "UPDATED_REVIEW",
            "NEW_CUSTOMER_MEDIA",
            "NEW_QUESTION",
            "UPDATED_QUESTION",
            "NEW_ANSWER",
            "UPDATED_ANSWER",
            "DUPLICATE_LOCATION",
            "LOSS_OF_VOICE_OF_MERCHANT",
            "VOICE_OF_MERCHANT_UPDATED",
        ]
    ]
    pubsubTopic: str
