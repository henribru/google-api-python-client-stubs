import typing

import typing_extensions

_list = list

@typing.type_check_only
class BestSellersBrandView(typing_extensions.TypedDict, total=False):
    brand: str
    previousRank: str
    previousRelativeDemand: typing_extensions.Literal[
        "RELATIVE_DEMAND_ENUM_UNSPECIFIED",
        "VERY_LOW",
        "LOW",
        "MEDIUM",
        "HIGH",
        "VERY_HIGH",
    ]
    rank: str
    relativeDemand: typing_extensions.Literal[
        "RELATIVE_DEMAND_ENUM_UNSPECIFIED",
        "VERY_LOW",
        "LOW",
        "MEDIUM",
        "HIGH",
        "VERY_HIGH",
    ]
    relativeDemandChange: typing_extensions.Literal[
        "RELATIVE_DEMAND_CHANGE_TYPE_ENUM_UNSPECIFIED", "SINKER", "FLAT", "RISER"
    ]
    reportCategoryId: str
    reportCountryCode: str
    reportDate: Date
    reportGranularity: typing_extensions.Literal[
        "REPORT_GRANULARITY_ENUM_UNSPECIFIED", "WEEKLY", "MONTHLY"
    ]

@typing.type_check_only
class BestSellersProductClusterView(typing_extensions.TypedDict, total=False):
    brand: str
    brandInventoryStatus: typing_extensions.Literal[
        "INVENTORY_STATUS_UNSPECIFIED", "IN_STOCK", "OUT_OF_STOCK", "NOT_IN_INVENTORY"
    ]
    categoryL1: str
    categoryL2: str
    categoryL3: str
    categoryL4: str
    categoryL5: str
    inventoryStatus: typing_extensions.Literal[
        "INVENTORY_STATUS_UNSPECIFIED", "IN_STOCK", "OUT_OF_STOCK", "NOT_IN_INVENTORY"
    ]
    previousRank: str
    previousRelativeDemand: typing_extensions.Literal[
        "RELATIVE_DEMAND_ENUM_UNSPECIFIED",
        "VERY_LOW",
        "LOW",
        "MEDIUM",
        "HIGH",
        "VERY_HIGH",
    ]
    rank: str
    relativeDemand: typing_extensions.Literal[
        "RELATIVE_DEMAND_ENUM_UNSPECIFIED",
        "VERY_LOW",
        "LOW",
        "MEDIUM",
        "HIGH",
        "VERY_HIGH",
    ]
    relativeDemandChange: typing_extensions.Literal[
        "RELATIVE_DEMAND_CHANGE_TYPE_ENUM_UNSPECIFIED", "SINKER", "FLAT", "RISER"
    ]
    reportCategoryId: str
    reportCountryCode: str
    reportDate: Date
    reportGranularity: typing_extensions.Literal[
        "REPORT_GRANULARITY_ENUM_UNSPECIFIED", "WEEKLY", "MONTHLY"
    ]
    title: str
    variantGtins: _list[str]

@typing.type_check_only
class CompetitiveVisibilityBenchmarkView(typing_extensions.TypedDict, total=False):
    categoryBenchmarkVisibilityTrend: float
    date: Date
    reportCategoryId: str
    reportCountryCode: str
    trafficSource: typing_extensions.Literal[
        "TRAFFIC_SOURCE_ENUM_UNSPECIFIED", "ORGANIC", "ADS", "ALL"
    ]
    yourDomainVisibilityTrend: float

@typing.type_check_only
class CompetitiveVisibilityCompetitorView(typing_extensions.TypedDict, total=False):
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
    trafficSource: typing_extensions.Literal[
        "TRAFFIC_SOURCE_ENUM_UNSPECIFIED", "ORGANIC", "ADS", "ALL"
    ]

@typing.type_check_only
class CompetitiveVisibilityTopMerchantView(typing_extensions.TypedDict, total=False):
    adsOrganicRatio: float
    date: Date
    domain: str
    higherPositionRate: float
    isYourDomain: bool
    pageOverlapRate: float
    rank: str
    reportCategoryId: str
    reportCountryCode: str
    trafficSource: typing_extensions.Literal[
        "TRAFFIC_SOURCE_ENUM_UNSPECIFIED", "ORGANIC", "ADS", "ALL"
    ]

@typing.type_check_only
class Date(typing_extensions.TypedDict, total=False):
    day: int
    month: int
    year: int

@typing.type_check_only
class IssueSeverityPerReportingContext(typing_extensions.TypedDict, total=False):
    demotedCountries: _list[str]
    disapprovedCountries: _list[str]
    reportingContext: typing_extensions.Literal[
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
        "FREE_LOCAL_LISTINGS",
        "FREE_LOCAL_VEHICLE_LISTINGS",
        "YOUTUBE_SHOPPING",
        "CLOUD_RETAIL",
        "LOCAL_CLOUD_RETAIL",
        "PRODUCT_REVIEWS",
        "MERCHANT_REVIEWS",
        "YOUTUBE_CHECKOUT",
    ]

@typing.type_check_only
class ItemIssue(typing_extensions.TypedDict, total=False):
    resolution: typing_extensions.Literal[
        "ITEM_ISSUE_RESOLUTION_UNSPECIFIED", "MERCHANT_ACTION", "PENDING_PROCESSING"
    ]
    severity: ItemIssueSeverity
    type: ItemIssueType

@typing.type_check_only
class ItemIssueSeverity(typing_extensions.TypedDict, total=False):
    aggregatedSeverity: typing_extensions.Literal[
        "AGGREGATED_ISSUE_SEVERITY_UNSPECIFIED", "DISAPPROVED", "DEMOTED", "PENDING"
    ]
    severityPerReportingContext: _list[IssueSeverityPerReportingContext]

@typing.type_check_only
class ItemIssueType(typing_extensions.TypedDict, total=False):
    canonicalAttribute: str
    code: str

@typing.type_check_only
class NonProductPerformanceView(typing_extensions.TypedDict, total=False):
    clickThroughRate: float
    clicks: str
    date: Date
    impressions: str
    week: Date

@typing.type_check_only
class Price(typing_extensions.TypedDict, total=False):
    amountMicros: str
    currencyCode: str

@typing.type_check_only
class PriceCompetitivenessProductView(typing_extensions.TypedDict, total=False):
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
class PriceInsightsProductView(typing_extensions.TypedDict, total=False):
    brand: str
    categoryL1: str
    categoryL2: str
    categoryL3: str
    categoryL4: str
    categoryL5: str
    effectiveness: typing_extensions.Literal[
        "EFFECTIVENESS_UNSPECIFIED", "LOW", "MEDIUM", "HIGH"
    ]
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
class ProductChange(typing_extensions.TypedDict, total=False):
    newValue: str
    oldValue: str
    regionCode: str
    reportingContext: typing_extensions.Literal[
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
        "FREE_LOCAL_LISTINGS",
        "FREE_LOCAL_VEHICLE_LISTINGS",
        "YOUTUBE_SHOPPING",
        "CLOUD_RETAIL",
        "LOCAL_CLOUD_RETAIL",
        "PRODUCT_REVIEWS",
        "MERCHANT_REVIEWS",
        "YOUTUBE_CHECKOUT",
    ]

@typing.type_check_only
class ProductPerformanceView(typing_extensions.TypedDict, total=False):
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
    marketingMethod: typing_extensions.Literal[
        "MARKETING_METHOD_ENUM_UNSPECIFIED", "ORGANIC", "ADS"
    ]
    offerId: str
    productTypeL1: str
    productTypeL2: str
    productTypeL3: str
    productTypeL4: str
    productTypeL5: str
    title: str
    week: Date

@typing.type_check_only
class ProductStatusChangeMessage(typing_extensions.TypedDict, total=False):
    account: str
    attribute: typing_extensions.Literal["ATTRIBUTE_UNSPECIFIED", "STATUS"]
    changes: _list[ProductChange]
    expirationTime: str
    managingAccount: str
    resource: str
    resourceId: str
    resourceType: typing_extensions.Literal["RESOURCE_UNSPECIFIED", "PRODUCT"]

@typing.type_check_only
class ProductView(typing_extensions.TypedDict, total=False):
    aggregatedReportingContextStatus: typing_extensions.Literal[
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
    channel: typing_extensions.Literal["CHANNEL_ENUM_UNSPECIFIED", "ONLINE", "LOCAL"]
    clickPotential: typing_extensions.Literal[
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
    shippingLabel: str
    thumbnailLink: str
    title: str

@typing.type_check_only
class ReportRow(typing_extensions.TypedDict, total=False):
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
class SearchRequest(typing_extensions.TypedDict, total=False):
    pageSize: int
    pageToken: str
    query: str

@typing.type_check_only
class SearchResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    results: _list[ReportRow]
