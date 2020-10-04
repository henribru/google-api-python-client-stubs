import typing

import typing_extensions
@typing.type_check_only
class Account(typing_extensions.TypedDict, total=False):
    bidderLocation: typing.List[typing.Dict[str, typing.Any]]
    cookieMatchingNid: str
    cookieMatchingUrl: str
    id: int
    kind: str
    maximumActiveCreatives: int
    maximumTotalQps: int
    numberActiveCreatives: int

@typing.type_check_only
class AccountsList(typing_extensions.TypedDict, total=False):
    items: typing.List[Account]
    kind: str

@typing.type_check_only
class BillingInfo(typing_extensions.TypedDict, total=False):
    accountId: int
    accountName: str
    billingId: typing.List[str]
    kind: str

@typing.type_check_only
class BillingInfoList(typing_extensions.TypedDict, total=False):
    items: typing.List[BillingInfo]
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
    adTechnologyProviders: typing.Dict[str, typing.Any]
    advertiserId: typing.List[str]
    advertiserName: str
    agencyId: str
    apiUploadTimestamp: str
    attribute: typing.List[int]
    buyerCreativeId: str
    clickThroughUrl: typing.List[str]
    corrections: typing.List[typing.Dict[str, typing.Any]]
    disapprovalReasons: typing.List[typing.Dict[str, typing.Any]]
    filteringReasons: typing.Dict[str, typing.Any]
    height: int
    impressionTrackingUrl: typing.List[str]
    kind: str
    nativeAd: typing.Dict[str, typing.Any]
    productCategories: typing.List[int]
    restrictedCategories: typing.List[int]
    sensitiveCategories: typing.List[int]
    status: str
    vendorType: typing.List[int]
    version: int
    videoURL: str
    width: int

@typing.type_check_only
class CreativesList(typing_extensions.TypedDict, total=False):
    items: typing.List[Creative]
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
    directDeals: typing.List[DirectDeal]
    kind: str

@typing.type_check_only
class PerformanceReport(typing_extensions.TypedDict, total=False):
    bidRate: float
    bidRequestRate: float
    calloutStatusRate: typing.List[typing.Any]
    cookieMatcherStatusRate: typing.List[typing.Any]
    creativeStatusRate: typing.List[typing.Any]
    filteredBidRate: float
    hostedMatchStatusRate: typing.List[typing.Any]
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
    performanceReport: typing.List[PerformanceReport]

@typing.type_check_only
class PretargetingConfig(typing_extensions.TypedDict, total=False):
    billingId: str
    configId: str
    configName: str
    creativeType: typing.List[str]
    dimensions: typing.List[typing.Dict[str, typing.Any]]
    excludedContentLabels: typing.List[str]
    excludedGeoCriteriaIds: typing.List[str]
    excludedPlacements: typing.List[typing.Dict[str, typing.Any]]
    excludedUserLists: typing.List[str]
    excludedVerticals: typing.List[str]
    geoCriteriaIds: typing.List[str]
    isActive: bool
    kind: str
    languages: typing.List[str]
    maximumQps: str
    mobileCarriers: typing.List[str]
    mobileDevices: typing.List[str]
    mobileOperatingSystemVersions: typing.List[str]
    placements: typing.List[typing.Dict[str, typing.Any]]
    platforms: typing.List[str]
    supportedCreativeAttributes: typing.List[str]
    userLists: typing.List[str]
    vendorTypes: typing.List[str]
    verticals: typing.List[str]

@typing.type_check_only
class PretargetingConfigList(typing_extensions.TypedDict, total=False):
    items: typing.List[PretargetingConfig]
    kind: str
