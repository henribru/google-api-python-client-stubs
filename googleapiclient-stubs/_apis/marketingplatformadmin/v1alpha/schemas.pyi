import typing

_list = list

@typing.type_check_only
class AnalyticsAccountLink(typing.TypedDict, total=False):
    analyticsAccount: str
    displayName: str
    linkVerificationState: typing.Literal[
        "LINK_VERIFICATION_STATE_UNSPECIFIED",
        "LINK_VERIFICATION_STATE_VERIFIED",
        "LINK_VERIFICATION_STATE_NOT_VERIFIED",
    ]
    name: str

@typing.type_check_only
class BillInfo(typing.TypedDict, total=False):
    baseFee: Money
    eventFee: Money
    priceProtectionCredit: Money
    total: Money

@typing.type_check_only
class ClientData(typing.TypedDict, total=False):
    endDate: Date
    organization: Organization
    startDate: Date

@typing.type_check_only
class Date(typing.TypedDict, total=False):
    day: int
    month: int
    year: int

@typing.type_check_only
class Empty(typing.TypedDict, total=False): ...

@typing.type_check_only
class FindSalesPartnerManagedClientsRequest(typing.TypedDict, total=False):
    isActive: bool

@typing.type_check_only
class FindSalesPartnerManagedClientsResponse(typing.TypedDict, total=False):
    clientData: _list[ClientData]

@typing.type_check_only
class ListAnalyticsAccountLinksResponse(typing.TypedDict, total=False):
    analyticsAccountLinks: _list[AnalyticsAccountLink]
    nextPageToken: str

@typing.type_check_only
class ListOrganizationsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    organizations: _list[Organization]

@typing.type_check_only
class Money(typing.TypedDict, total=False):
    currencyCode: str
    nanos: int
    units: str

@typing.type_check_only
class Organization(typing.TypedDict, total=False):
    displayName: str
    name: str

@typing.type_check_only
class PropertyUsage(typing.TypedDict, total=False):
    accountId: str
    billableEventCount: str
    displayName: str
    property: str
    propertyType: typing.Literal[
        "ANALYTICS_PROPERTY_TYPE_UNSPECIFIED",
        "ANALYTICS_PROPERTY_TYPE_ORDINARY",
        "ANALYTICS_PROPERTY_TYPE_SUBPROPERTY",
        "ANALYTICS_PROPERTY_TYPE_ROLLUP",
    ]
    serviceLevel: typing.Literal[
        "ANALYTICS_SERVICE_LEVEL_UNSPECIFIED",
        "ANALYTICS_SERVICE_LEVEL_STANDARD",
        "ANALYTICS_SERVICE_LEVEL_360",
    ]
    totalEventCount: str

@typing.type_check_only
class ReportPropertyUsageRequest(typing.TypedDict, total=False):
    month: str

@typing.type_check_only
class ReportPropertyUsageResponse(typing.TypedDict, total=False):
    billInfo: BillInfo
    propertyUsages: _list[PropertyUsage]

@typing.type_check_only
class SetPropertyServiceLevelRequest(typing.TypedDict, total=False):
    analyticsProperty: str
    serviceLevel: typing.Literal[
        "ANALYTICS_SERVICE_LEVEL_UNSPECIFIED",
        "ANALYTICS_SERVICE_LEVEL_STANDARD",
        "ANALYTICS_SERVICE_LEVEL_360",
    ]

@typing.type_check_only
class SetPropertyServiceLevelResponse(typing.TypedDict, total=False): ...
