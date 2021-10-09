import typing

import typing_extensions

_list = list

@typing.type_check_only
class GoogleCloudEssentialcontactsV1ComputeContactsResponse(
    typing_extensions.TypedDict, total=False
):
    contacts: _list[GoogleCloudEssentialcontactsV1Contact]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudEssentialcontactsV1Contact(typing_extensions.TypedDict, total=False):
    email: str
    languageTag: str
    name: str
    notificationCategorySubscriptions: _list[str]
    validateTime: str
    validationState: typing_extensions.Literal[
        "VALIDATION_STATE_UNSPECIFIED", "VALID", "INVALID"
    ]

@typing.type_check_only
class GoogleCloudEssentialcontactsV1ListContactsResponse(
    typing_extensions.TypedDict, total=False
):
    contacts: _list[GoogleCloudEssentialcontactsV1Contact]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudEssentialcontactsV1SendTestMessageRequest(
    typing_extensions.TypedDict, total=False
):
    contacts: _list[str]
    notificationCategory: typing_extensions.Literal[
        "NOTIFICATION_CATEGORY_UNSPECIFIED",
        "ALL",
        "SUSPENSION",
        "SECURITY",
        "TECHNICAL",
        "BILLING",
        "LEGAL",
        "PRODUCT_UPDATES",
        "TECHNICAL_INCIDENTS",
    ]

@typing.type_check_only
class GoogleProtobufEmpty(typing_extensions.TypedDict, total=False): ...
