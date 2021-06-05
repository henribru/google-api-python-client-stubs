import typing

import typing_extensions

@typing.type_check_only
class GoogleCloudEssentialcontactsV1ComputeContactsResponse(
    typing_extensions.TypedDict, total=False
):
    contacts: typing.List[GoogleCloudEssentialcontactsV1Contact]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudEssentialcontactsV1Contact(typing_extensions.TypedDict, total=False):
    email: str
    languageTag: str
    name: str
    notificationCategorySubscriptions: typing.List[str]
    validateTime: str
    validationState: typing_extensions.Literal[
        "VALIDATION_STATE_UNSPECIFIED", "VALID", "INVALID"
    ]

@typing.type_check_only
class GoogleCloudEssentialcontactsV1ListContactsResponse(
    typing_extensions.TypedDict, total=False
):
    contacts: typing.List[GoogleCloudEssentialcontactsV1Contact]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudEssentialcontactsV1SendTestMessageRequest(
    typing_extensions.TypedDict, total=False
):
    contacts: typing.List[str]
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
