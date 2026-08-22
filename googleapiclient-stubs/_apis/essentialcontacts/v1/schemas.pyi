import typing

_list = list

@typing.type_check_only
class GoogleCloudEssentialcontactsV1ComputeContactsResponse(
    typing.TypedDict, total=False
):
    contacts: _list[GoogleCloudEssentialcontactsV1Contact]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudEssentialcontactsV1Contact(typing.TypedDict, total=False):
    email: str
    languageTag: str
    name: str
    notificationCategorySubscriptions: _list[
        typing.Literal[
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
    ]
    validateTime: str
    validationState: typing.Literal["VALIDATION_STATE_UNSPECIFIED", "VALID", "INVALID"]

@typing.type_check_only
class GoogleCloudEssentialcontactsV1ListContactsResponse(typing.TypedDict, total=False):
    contacts: _list[GoogleCloudEssentialcontactsV1Contact]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudEssentialcontactsV1SendTestMessageRequest(
    typing.TypedDict, total=False
):
    contacts: _list[str]
    notificationCategory: typing.Literal[
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
class GoogleProtobufEmpty(typing.TypedDict, total=False): ...
