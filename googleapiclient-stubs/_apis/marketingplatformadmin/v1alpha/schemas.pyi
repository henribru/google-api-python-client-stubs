import typing

import typing_extensions

_list = list

@typing.type_check_only
class AnalyticsAccountLink(typing_extensions.TypedDict, total=False):
    analyticsAccount: str
    displayName: str
    linkVerificationState: typing_extensions.Literal[
        "LINK_VERIFICATION_STATE_UNSPECIFIED",
        "LINK_VERIFICATION_STATE_VERIFIED",
        "LINK_VERIFICATION_STATE_NOT_VERIFIED",
    ]
    name: str

@typing.type_check_only
class BillInfo(typing_extensions.TypedDict, total=False):
    baseFee: Money
    eventFee: Money
    priceProtectionCredit: Money
    total: Money

@typing.type_check_only
class ClientData(typing_extensions.TypedDict, total=False):
    endDate: Date
    organization: Organization
    startDate: Date

@typing.type_check_only
class Date(typing_extensions.TypedDict, total=False):
    day: int
    month: int
    year: int

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class FindSalesPartnerManagedClientsRequest(typing_extensions.TypedDict, total=False):
    isActive: bool

@typing.type_check_only
class FindSalesPartnerManagedClientsResponse(typing_extensions.TypedDict, total=False):
    clientData: _list[ClientData]

@typing.type_check_only
class ListAnalyticsAccountLinksResponse(typing_extensions.TypedDict, total=False):
    analyticsAccountLinks: _list[AnalyticsAccountLink]
    nextPageToken: str

@typing.type_check_only
class ListOrganizationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    organizations: _list[Organization]

@typing.type_check_only
class Money(typing_extensions.TypedDict, total=False):
    currencyCode: str
    nanos: int
    units: str

@typing.type_check_only
class Organization(typing_extensions.TypedDict, total=False):
    displayName: str
    name: str

@typing.type_check_only
class PropertyUsage(typing_extensions.TypedDict, total=False):
    accountId: str
    billableEventCount: str
    displayName: str
    property: str
    propertyType: typing_extensions.Literal[
        "ANALYTICS_PROPERTY_TYPE_UNSPECIFIED",
        "ANALYTICS_PROPERTY_TYPE_ORDINARY",
        "ANALYTICS_PROPERTY_TYPE_SUBPROPERTY",
        "ANALYTICS_PROPERTY_TYPE_ROLLUP",
    ]
    serviceLevel: typing_extensions.Literal[
        "ANALYTICS_SERVICE_LEVEL_UNSPECIFIED",
        "ANALYTICS_SERVICE_LEVEL_STANDARD",
        "ANALYTICS_SERVICE_LEVEL_360",
    ]
    totalEventCount: str

@typing.type_check_only
class ReportPropertyUsageRequest(typing_extensions.TypedDict, total=False):
    month: str

@typing.type_check_only
class ReportPropertyUsageResponse(typing_extensions.TypedDict, total=False):
    billInfo: BillInfo
    propertyUsages: _list[PropertyUsage]

@typing.type_check_only
class SetPropertyServiceLevelRequest(typing_extensions.TypedDict, total=False):
    analyticsProperty: str
    serviceLevel: typing_extensions.Literal[
        "ANALYTICS_SERVICE_LEVEL_UNSPECIFIED",
        "ANALYTICS_SERVICE_LEVEL_STANDARD",
        "ANALYTICS_SERVICE_LEVEL_360",
    ]

@typing.type_check_only
class SetPropertyServiceLevelResponse(typing_extensions.TypedDict, total=False): ...
