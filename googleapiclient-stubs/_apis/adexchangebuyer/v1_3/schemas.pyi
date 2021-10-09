import typing

import typing_extensions

_list = list

@typing.type_check_only
class Account(typing_extensions.TypedDict, total=False):
    bidderLocation: _list[dict[str, typing.Any]]
    cookieMatchingNid: str
    cookieMatchingUrl: str
    id: int
    kind: str
    maximumActiveCreatives: int
    maximumTotalQps: int
    numberActiveCreatives: int

@typing.type_check_only
class AccountsList(typing_extensions.TypedDict, total=False):
    items: _list[Account]
    kind: str

@typing.type_check_only
class BillingInfo(typing_extensions.TypedDict, total=False):
    accountId: int
    accountName: str
    billingId: _list[str]
    kind: str

@typing.type_check_only
class BillingInfoList(typing_extensions.TypedDict, total=False):
    items: _list[BillingInfo]
    kind: str

@typing.type_check_only
class Budget(typing_extensions.TypedDict, total=False):
    accountId: str
    billingId: str
    budgetAmount: str
    currencyCode: str
    id: str
    kind: str

@typing.type_check_only
class Creative(typing_extensions.TypedDict, total=False):
    HTMLSnippet: str
    accountId: int
    adTechnologyProviders: dict[str, typing.Any]
    advertiserId: _list[str]
    advertiserName: str
    agencyId: str
    apiUploadTimestamp: str
    attribute: _list[int]
    buyerCreativeId: str
    clickThroughUrl: _list[str]
    corrections: _list[dict[str, typing.Any]]
    disapprovalReasons: _list[dict[str, typing.Any]]
    filteringReasons: dict[str, typing.Any]
    height: int
    impressionTrackingUrl: _list[str]
    kind: str
    nativeAd: dict[str, typing.Any]
    productCategories: _list[int]
    restrictedCategories: _list[int]
    sensitiveCategories: _list[int]
    status: str
    vendorType: _list[int]
    version: int
    videoURL: str
    width: int

@typing.type_check_only
class CreativesList(typing_extensions.TypedDict, total=False):
    items: _list[Creative]
    kind: str
    nextPageToken: str

@typing.type_check_only
class DirectDeal(typing_extensions.TypedDict, total=False):
    accountId: int
    advertiser: str
    allowsAlcohol: bool
    buyerAccountId: str
    currencyCode: str
    dealTier: str
    endTime: str
    fixedCpm: str
    id: str
    kind: str
    name: str
    privateExchangeMinCpm: str
    publisherBlocksOverriden: bool
    sellerNetwork: str
    startTime: str

@typing.type_check_only
class DirectDealsList(typing_extensions.TypedDict, total=False):
    directDeals: _list[DirectDeal]
    kind: str

@typing.type_check_only
class PerformanceReport(typing_extensions.TypedDict, total=False):
    bidRate: float
    bidRequestRate: float
    calloutStatusRate: _list[typing.Any]
    cookieMatcherStatusRate: _list[typing.Any]
    creativeStatusRate: _list[typing.Any]
    filteredBidRate: float
    hostedMatchStatusRate: _list[typing.Any]
    inventoryMatchRate: float
    kind: str
    latency50thPercentile: float
    latency85thPercentile: float
    latency95thPercentile: float
    noQuotaInRegion: float
    outOfQuota: float
    pixelMatchRequests: float
    pixelMatchResponses: float
    quotaConfiguredLimit: float
    quotaThrottledLimit: float
    region: str
    successfulRequestRate: float
    timestamp: str
    unsuccessfulRequestRate: float

@typing.type_check_only
class PerformanceReportList(typing_extensions.TypedDict, total=False):
    kind: str
    performanceReport: _list[PerformanceReport]

@typing.type_check_only
class PretargetingConfig(typing_extensions.TypedDict, total=False):
    billingId: str
    configId: str
    configName: str
    creativeType: _list[str]
    dimensions: _list[dict[str, typing.Any]]
    excludedContentLabels: _list[str]
    excludedGeoCriteriaIds: _list[str]
    excludedPlacements: _list[dict[str, typing.Any]]
    excludedUserLists: _list[str]
    excludedVerticals: _list[str]
    geoCriteriaIds: _list[str]
    isActive: bool
    kind: str
    languages: _list[str]
    maximumQps: str
    mobileCarriers: _list[str]
    mobileDevices: _list[str]
    mobileOperatingSystemVersions: _list[str]
    placements: _list[dict[str, typing.Any]]
    platforms: _list[str]
    supportedCreativeAttributes: _list[str]
    userLists: _list[str]
    vendorTypes: _list[str]
    verticals: _list[str]

@typing.type_check_only
class PretargetingConfigList(typing_extensions.TypedDict, total=False):
    items: _list[PretargetingConfig]
    kind: str
