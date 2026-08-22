import typing

_list = list

@typing.type_check_only
class BestSellersBrandView(typing.TypedDict, total=False):
    brand: str
    previousRank: str
    previousRelativeDemand: typing.Literal[
        "RELATIVE_DEMAND_ENUM_UNSPECIFIED",
        "VERY_LOW",
        "LOW",
        "MEDIUM",
        "HIGH",
        "VERY_HIGH",
    ]
    rank: str
    relativeDemand: typing.Literal[
        "RELATIVE_DEMAND_ENUM_UNSPECIFIED",
        "VERY_LOW",
        "LOW",
        "MEDIUM",
        "HIGH",
        "VERY_HIGH",
    ]
    relativeDemandChange: typing.Literal[
        "RELATIVE_DEMAND_CHANGE_TYPE_ENUM_UNSPECIFIED", "SINKER", "FLAT", "RISER"
    ]
    reportCategoryId: str
    reportCountryCode: str
    reportDate: Date
    reportGranularity: typing.Literal[
        "REPORT_GRANULARITY_ENUM_UNSPECIFIED", "WEEKLY", "MONTHLY"
    ]

@typing.type_check_only
class BestSellersProductClusterView(typing.TypedDict, total=False):
    brand: str
    brandInventoryStatus: typing.Literal[
        "INVENTORY_STATUS_UNSPECIFIED", "IN_STOCK", "OUT_OF_STOCK", "NOT_IN_INVENTORY"
    ]
    categoryL1: str
    categoryL2: str
    categoryL3: str
    categoryL4: str
    categoryL5: str
    inventoryStatus: typing.Literal[
        "INVENTORY_STATUS_UNSPECIFIED", "IN_STOCK", "OUT_OF_STOCK", "NOT_IN_INVENTORY"
    ]
    previousRank: str
    previousRelativeDemand: typing.Literal[
        "RELATIVE_DEMAND_ENUM_UNSPECIFIED",
        "VERY_LOW",
        "LOW",
        "MEDIUM",
        "HIGH",
        "VERY_HIGH",
    ]
    rank: str
    relativeDemand: typing.Literal[
        "RELATIVE_DEMAND_ENUM_UNSPECIFIED",
        "VERY_LOW",
        "LOW",
        "MEDIUM",
        "HIGH",
        "VERY_HIGH",
    ]
    relativeDemandChange: typing.Literal[
        "RELATIVE_DEMAND_CHANGE_TYPE_ENUM_UNSPECIFIED", "SINKER", "FLAT", "RISER"
    ]
    reportCategoryId: str
    reportCountryCode: str
    reportDate: Date
    reportGranularity: typing.Literal[
        "REPORT_GRANULARITY_ENUM_UNSPECIFIED", "WEEKLY", "MONTHLY"
    ]
    title: str
    variantGtins: _list[str]

@typing.type_check_only
class CompetitiveVisibilityBenchmarkView(typing.TypedDict, total=False):
    categoryBenchmarkVisibilityTrend: float
    date: Date
    reportCategoryId: str
    reportCountryCode: str
    trafficSource: typing.Literal[
        "TRAFFIC_SOURCE_ENUM_UNSPECIFIED", "ORGANIC", "ADS", "ALL"
    ]
    yourDomainVisibilityTrend: float

@typing.type_check_only
class CompetitiveVisibilityCompetitorView(typing.TypedDict, total=False):
    adsOrganicRatio: float
    date: Date
    domain: str
    higherPositionRate: float
    isYourDomain: bool
    pageOverlapRate: float
    rank: str
    relativeVisibility: float
    reportCategoryId: str
    reportCountryCode: str
    trafficSource: typing.Literal[
        "TRAFFIC_SOURCE_ENUM_UNSPECIFIED", "ORGANIC", "ADS", "ALL"
    ]

@typing.type_check_only
class CompetitiveVisibilityTopMerchantView(typing.TypedDict, total=False):
    adsOrganicRatio: float
    date: Date
    domain: str
    higherPositionRate: float
    isYourDomain: bool
    pageOverlapRate: float
    rank: str
    reportCategoryId: str
    reportCountryCode: str
    trafficSource: typing.Literal[
        "TRAFFIC_SOURCE_ENUM_UNSPECIFIED", "ORGANIC", "ADS", "ALL"
    ]

@typing.type_check_only
class Date(typing.TypedDict, total=False):
    day: int
    month: int
    year: int

@typing.type_check_only
class IssueSeverityPerReportingContext(typing.TypedDict, total=False):
    demotedCountries: _list[str]
    disapprovedCountries: _list[str]
    reportingContext: typing.Literal[
        "REPORTING_CONTEXT_ENUM_UNSPECIFIED",
        "SHOPPING_ADS",
        "DISCOVERY_ADS",
        "DEMAND_GEN_ADS",
        "DEMAND_GEN_ADS_DISCOVER_SURFACE",
        "VIDEO_ADS",
        "DISPLAY_ADS",
        "LOCAL_INVENTORY_ADS",
        "VEHICLE_INVENTORY_ADS",
        "FREE_LISTINGS",
        "FREE_LISTINGS_UCP_CHECKOUT",
        "FREE_LOCAL_LISTINGS",
        "FREE_LOCAL_VEHICLE_LISTINGS",
        "YOUTUBE_AFFILIATE",
        "YOUTUBE_SHOPPING",
        "CLOUD_RETAIL",
        "LOCAL_CLOUD_RETAIL",
        "PRODUCT_REVIEWS",
        "MERCHANT_REVIEWS",
        "YOUTUBE_CHECKOUT",
    ]

@typing.type_check_only
class ItemIssue(typing.TypedDict, total=False):
    resolution: typing.Literal[
        "ITEM_ISSUE_RESOLUTION_UNSPECIFIED", "MERCHANT_ACTION", "PENDING_PROCESSING"
    ]
    severity: ItemIssueSeverity
    type: ItemIssueType

@typing.type_check_only
class ItemIssueSeverity(typing.TypedDict, total=False):
    aggregatedSeverity: typing.Literal[
        "AGGREGATED_ISSUE_SEVERITY_UNSPECIFIED", "DISAPPROVED", "DEMOTED", "PENDING"
    ]
    severityPerReportingContext: _list[IssueSeverityPerReportingContext]

@typing.type_check_only
class ItemIssueType(typing.TypedDict, total=False):
    canonicalAttribute: str
    code: str

@typing.type_check_only
class NonProductPerformanceView(typing.TypedDict, total=False):
    clickThroughRate: float
    clicks: str
    date: Date
    impressions: str
    week: Date

@typing.type_check_only
class Price(typing.TypedDict, total=False):
    amountMicros: str
    currencyCode: str

@typing.type_check_only
class PriceCompetitivenessProductView(typing.TypedDict, total=False):
    benchmarkPrice: Price
    brand: str
    categoryL1: str
    categoryL2: str
    categoryL3: str
    categoryL4: str
    categoryL5: str
    id: str
    offerId: str
    price: Price
    productTypeL1: str
    productTypeL2: str
    productTypeL3: str
    productTypeL4: str
    productTypeL5: str
    reportCountryCode: str
    title: str

@typing.type_check_only
class PriceInsightsProductView(typing.TypedDict, total=False):
    brand: str
    categoryL1: str
    categoryL2: str
    categoryL3: str
    categoryL4: str
    categoryL5: str
    effectiveness: typing.Literal["EFFECTIVENESS_UNSPECIFIED", "LOW", "MEDIUM", "HIGH"]
    id: str
    offerId: str
    predictedClicksChangeFraction: float
    predictedConversionsChangeFraction: float
    predictedImpressionsChangeFraction: float
    price: Price
    productTypeL1: str
    productTypeL2: str
    productTypeL3: str
    productTypeL4: str
    productTypeL5: str
    suggestedPrice: Price
    title: str

@typing.type_check_only
class ProductChange(typing.TypedDict, total=False):
    newValue: str
    oldValue: str
    regionCode: str
    reportingContext: typing.Literal[
        "REPORTING_CONTEXT_ENUM_UNSPECIFIED",
        "SHOPPING_ADS",
        "DISCOVERY_ADS",
        "DEMAND_GEN_ADS",
        "DEMAND_GEN_ADS_DISCOVER_SURFACE",
        "VIDEO_ADS",
        "DISPLAY_ADS",
        "LOCAL_INVENTORY_ADS",
        "VEHICLE_INVENTORY_ADS",
        "FREE_LISTINGS",
        "FREE_LISTINGS_UCP_CHECKOUT",
        "FREE_LOCAL_LISTINGS",
        "FREE_LOCAL_VEHICLE_LISTINGS",
        "YOUTUBE_AFFILIATE",
        "YOUTUBE_SHOPPING",
        "CLOUD_RETAIL",
        "LOCAL_CLOUD_RETAIL",
        "PRODUCT_REVIEWS",
        "MERCHANT_REVIEWS",
        "YOUTUBE_CHECKOUT",
    ]

@typing.type_check_only
class ProductPerformanceView(typing.TypedDict, total=False):
    brand: str
    categoryL1: str
    categoryL2: str
    categoryL3: str
    categoryL4: str
    categoryL5: str
    clickThroughRate: float
    clicks: str
    conversionRate: float
    conversionValue: Price
    conversions: float
    customLabel0: str
    customLabel1: str
    customLabel2: str
    customLabel3: str
    customLabel4: str
    customerCountryCode: str
    date: Date
    impressions: str
    marketingMethod: typing.Literal[
        "MARKETING_METHOD_ENUM_UNSPECIFIED", "ORGANIC", "ADS"
    ]
    offerId: str
    productTypeL1: str
    productTypeL2: str
    productTypeL3: str
    productTypeL4: str
    productTypeL5: str
    storeType: typing.Literal[
        "STORE_TYPE_ENUM_UNSPECIFIED", "ONLINE_STORE", "LOCAL_STORES"
    ]
    title: str
    week: Date

@typing.type_check_only
class ProductStatusChangeMessage(typing.TypedDict, total=False):
    account: str
    attribute: typing.Literal["ATTRIBUTE_UNSPECIFIED", "STATUS"]
    changes: _list[ProductChange]
    eventTime: str
    expirationTime: str
    managingAccount: str
    resource: str
    resourceId: str
    resourceType: typing.Literal["RESOURCE_UNSPECIFIED", "PRODUCT", "ACCOUNT_SERVICE"]

@typing.type_check_only
class ProductView(typing.TypedDict, total=False):
    aggregatedReportingContextStatus: typing.Literal[
        "AGGREGATED_REPORTING_CONTEXT_STATUS_UNSPECIFIED",
        "NOT_ELIGIBLE_OR_DISAPPROVED",
        "PENDING",
        "ELIGIBLE_LIMITED",
        "ELIGIBLE",
    ]
    availability: str
    brand: str
    categoryL1: str
    categoryL2: str
    categoryL3: str
    categoryL4: str
    categoryL5: str
    channel: typing.Literal["CHANNEL_ENUM_UNSPECIFIED", "ONLINE", "LOCAL"]
    clickPotential: typing.Literal[
        "CLICK_POTENTIAL_UNSPECIFIED", "LOW", "MEDIUM", "HIGH"
    ]
    clickPotentialRank: str
    condition: str
    creationTime: str
    expirationDate: Date
    feedLabel: str
    gtin: _list[str]
    id: str
    itemGroupId: str
    itemIssues: _list[ItemIssue]
    languageCode: str
    offerId: str
    price: Price
    productTypeL1: str
    productTypeL2: str
    productTypeL3: str
    productTypeL4: str
    productTypeL5: str
    reportingContext: typing.Literal[
        "REPORTING_CONTEXT_ENUM_UNSPECIFIED",
        "SHOPPING_ADS",
        "DISCOVERY_ADS",
        "DEMAND_GEN_ADS",
        "DEMAND_GEN_ADS_DISCOVER_SURFACE",
        "VIDEO_ADS",
        "DISPLAY_ADS",
        "LOCAL_INVENTORY_ADS",
        "VEHICLE_INVENTORY_ADS",
        "FREE_LISTINGS",
        "FREE_LISTINGS_UCP_CHECKOUT",
        "FREE_LOCAL_LISTINGS",
        "FREE_LOCAL_VEHICLE_LISTINGS",
        "YOUTUBE_AFFILIATE",
        "YOUTUBE_SHOPPING",
        "CLOUD_RETAIL",
        "LOCAL_CLOUD_RETAIL",
        "PRODUCT_REVIEWS",
        "MERCHANT_REVIEWS",
        "YOUTUBE_CHECKOUT",
    ]
    shippingLabel: str
    statusPerReportingContext: _list[StatusPerReportingContext]
    thumbnailLink: str
    title: str

@typing.type_check_only
class ReportRow(typing.TypedDict, total=False):
    bestSellersBrandView: BestSellersBrandView
    bestSellersProductClusterView: BestSellersProductClusterView
    competitiveVisibilityBenchmarkView: CompetitiveVisibilityBenchmarkView
    competitiveVisibilityCompetitorView: CompetitiveVisibilityCompetitorView
    competitiveVisibilityTopMerchantView: CompetitiveVisibilityTopMerchantView
    nonProductPerformanceView: NonProductPerformanceView
    priceCompetitivenessProductView: PriceCompetitivenessProductView
    priceInsightsProductView: PriceInsightsProductView
    productPerformanceView: ProductPerformanceView
    productView: ProductView

@typing.type_check_only
class SearchRequest(typing.TypedDict, total=False):
    pageSize: int
    pageToken: str
    query: str

@typing.type_check_only
class SearchResponse(typing.TypedDict, total=False):
    nextPageToken: str
    results: _list[ReportRow]

@typing.type_check_only
class StatusPerReportingContext(typing.TypedDict, total=False):
    approvedCountries: _list[str]
    disapprovedCountries: _list[str]
    pendingCountries: _list[str]
    reportingContext: typing.Literal[
        "REPORTING_CONTEXT_ENUM_UNSPECIFIED",
        "SHOPPING_ADS",
        "DISCOVERY_ADS",
        "DEMAND_GEN_ADS",
        "DEMAND_GEN_ADS_DISCOVER_SURFACE",
        "VIDEO_ADS",
        "DISPLAY_ADS",
        "LOCAL_INVENTORY_ADS",
        "VEHICLE_INVENTORY_ADS",
        "FREE_LISTINGS",
        "FREE_LISTINGS_UCP_CHECKOUT",
        "FREE_LOCAL_LISTINGS",
        "FREE_LOCAL_VEHICLE_LISTINGS",
        "YOUTUBE_AFFILIATE",
        "YOUTUBE_SHOPPING",
        "CLOUD_RETAIL",
        "LOCAL_CLOUD_RETAIL",
        "PRODUCT_REVIEWS",
        "MERCHANT_REVIEWS",
        "YOUTUBE_CHECKOUT",
    ]
