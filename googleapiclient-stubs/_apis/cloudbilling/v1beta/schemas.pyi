import typing

_list = list

@typing.type_check_only
class AgenticQueryInfo(typing.TypedDict, total=False):
    columns: str
    filter: str
    groupBy: str
    limit: int
    orderBy: str
    parents: _list[str]
    view: str

@typing.type_check_only
class Array(typing.TypedDict, total=False):
    element: _list[ValueProto]

@typing.type_check_only
class BillingData(typing.TypedDict, total=False):
    columnInfo: _list[ColumnInfo]
    rows: _list[Row]

@typing.type_check_only
class BillingDataResource(typing.TypedDict, total=False):
    billingAccount: str
    resource: str

@typing.type_check_only
class ColumnInfo(typing.TypedDict, total=False):
    column: str

@typing.type_check_only
class DataSet(typing.TypedDict, total=False):
    billingData: BillingData
    queryInfo: AgenticQueryInfo
    suggestedChart: SuggestedChart

@typing.type_check_only
class Datetime(typing.TypedDict, total=False):
    bitFieldDatetimeSeconds: str
    nanos: int

@typing.type_check_only
class Decimal(typing.TypedDict, total=False):
    value: str

@typing.type_check_only
class FinalResult(typing.TypedDict, total=False):
    dataSets: _list[DataSet]
    fullAnalysis: str
    insights: _list[Insight]
    interopLinks: _list[InteropLink]
    suggestedQueries: _list[SuggestedQuery]
    summary: str

@typing.type_check_only
class GenerateInsightsRequest(typing.TypedDict, total=False):
    filter: str
    overriddenMaxIterationCounts: int
    parents: _list[BillingDataResource]
    prompt: str
    userContext: UserContext

@typing.type_check_only
class GenerateInsightsResponse(typing.TypedDict, total=False):
    finalResult: FinalResult
    rejection: Rejection
    summaryChunk: str
    thoughtChunk: str

@typing.type_check_only
class GoogleCloudBillingBillingaccountpricesV1betaAggregationInfo(
    typing.TypedDict, total=False
):
    interval: typing.Literal[
        "INTERVAL_UNSPECIFIED", "INTERVAL_MONTHLY", "INTERVAL_DAILY"
    ]
    level: typing.Literal["LEVEL_UNSPECIFIED", "LEVEL_ACCOUNT", "LEVEL_PROJECT"]

@typing.type_check_only
class GoogleCloudBillingBillingaccountpricesV1betaBillingAccountPrice(
    typing.TypedDict, total=False
):
    currencyCode: str
    name: str
    priceReason: GoogleCloudBillingBillingaccountpricesV1betaPriceReason
    rate: GoogleCloudBillingBillingaccountpricesV1betaRate
    valueType: str

@typing.type_check_only
class GoogleCloudBillingBillingaccountpricesV1betaDefaultPrice(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudBillingBillingaccountpricesV1betaFixedDiscount(
    typing.TypedDict, total=False
):
    discountPercent: Decimal
    discountScopeType: str
    fixTime: str
    skuGroup: str

@typing.type_check_only
class GoogleCloudBillingBillingaccountpricesV1betaFixedPrice(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudBillingBillingaccountpricesV1betaFloatingDiscount(
    typing.TypedDict, total=False
):
    discountPercent: Decimal
    discountScopeType: str
    skuGroup: str

@typing.type_check_only
class GoogleCloudBillingBillingaccountpricesV1betaListBillingAccountPricesResponse(
    typing.TypedDict, total=False
):
    billingAccountPrices: _list[
        GoogleCloudBillingBillingaccountpricesV1betaBillingAccountPrice
    ]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudBillingBillingaccountpricesV1betaListPriceAsCeiling(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudBillingBillingaccountpricesV1betaMergedPrice(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudBillingBillingaccountpricesV1betaMigratedPrice(
    typing.TypedDict, total=False
):
    sourceSku: str

@typing.type_check_only
class GoogleCloudBillingBillingaccountpricesV1betaPriceReason(
    typing.TypedDict, total=False
):
    defaultPrice: GoogleCloudBillingBillingaccountpricesV1betaDefaultPrice
    fixedDiscount: GoogleCloudBillingBillingaccountpricesV1betaFixedDiscount
    fixedPrice: GoogleCloudBillingBillingaccountpricesV1betaFixedPrice
    floatingDiscount: GoogleCloudBillingBillingaccountpricesV1betaFloatingDiscount
    listPriceAsCeiling: GoogleCloudBillingBillingaccountpricesV1betaListPriceAsCeiling
    mergedPrice: GoogleCloudBillingBillingaccountpricesV1betaMergedPrice
    migratedPrice: GoogleCloudBillingBillingaccountpricesV1betaMigratedPrice
    type: str

@typing.type_check_only
class GoogleCloudBillingBillingaccountpricesV1betaRate(typing.TypedDict, total=False):
    aggregationInfo: GoogleCloudBillingBillingaccountpricesV1betaAggregationInfo
    tiers: _list[GoogleCloudBillingBillingaccountpricesV1betaRateTier]
    unitInfo: GoogleCloudBillingBillingaccountpricesV1betaUnitInfo

@typing.type_check_only
class GoogleCloudBillingBillingaccountpricesV1betaRateTier(
    typing.TypedDict, total=False
):
    contractPrice: Money
    effectiveDiscountPercent: Decimal
    listPrice: Money
    startAmount: Decimal

@typing.type_check_only
class GoogleCloudBillingBillingaccountpricesV1betaUnitInfo(
    typing.TypedDict, total=False
):
    unit: str
    unitDescription: str
    unitQuantity: Decimal

@typing.type_check_only
class GoogleCloudBillingBillingaccountservicesV1betaBillingAccountService(
    typing.TypedDict, total=False
):
    displayName: str
    name: str
    serviceId: str

@typing.type_check_only
class GoogleCloudBillingBillingaccountservicesV1betaListBillingAccountServicesResponse(
    typing.TypedDict, total=False
):
    billingAccountServices: _list[
        GoogleCloudBillingBillingaccountservicesV1betaBillingAccountService
    ]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudBillingBillingaccountskugroupsV1betaBillingAccountSkuGroup(
    typing.TypedDict, total=False
):
    displayName: str
    name: str

@typing.type_check_only
class GoogleCloudBillingBillingaccountskugroupsV1betaListBillingAccountSkuGroupsResponse(
    typing.TypedDict, total=False
):
    billingAccountSkuGroups: _list[
        GoogleCloudBillingBillingaccountskugroupsV1betaBillingAccountSkuGroup
    ]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudBillingBillingaccountskugroupskusV1betaBillingAccountSkuGroupSku(
    typing.TypedDict, total=False
):
    billingAccountService: str
    displayName: str
    geoTaxonomy: GoogleCloudBillingBillingaccountskugroupskusV1betaGeoTaxonomy
    name: str
    productTaxonomy: GoogleCloudBillingBillingaccountskugroupskusV1betaProductTaxonomy
    skuId: str

@typing.type_check_only
class GoogleCloudBillingBillingaccountskugroupskusV1betaGeoTaxonomy(
    typing.TypedDict, total=False
):
    globalMetadata: GoogleCloudBillingBillingaccountskugroupskusV1betaGeoTaxonomyGlobal
    multiRegionalMetadata: (
        GoogleCloudBillingBillingaccountskugroupskusV1betaGeoTaxonomyMultiRegional
    )
    regionalMetadata: (
        GoogleCloudBillingBillingaccountskugroupskusV1betaGeoTaxonomyRegional
    )
    type: typing.Literal[
        "TYPE_UNSPECIFIED", "TYPE_GLOBAL", "TYPE_REGIONAL", "TYPE_MULTI_REGIONAL"
    ]

@typing.type_check_only
class GoogleCloudBillingBillingaccountskugroupskusV1betaGeoTaxonomyGlobal(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudBillingBillingaccountskugroupskusV1betaGeoTaxonomyMultiRegional(
    typing.TypedDict, total=False
):
    regions: _list[GoogleCloudBillingBillingaccountskugroupskusV1betaGeoTaxonomyRegion]

@typing.type_check_only
class GoogleCloudBillingBillingaccountskugroupskusV1betaGeoTaxonomyRegion(
    typing.TypedDict, total=False
):
    region: str

@typing.type_check_only
class GoogleCloudBillingBillingaccountskugroupskusV1betaGeoTaxonomyRegional(
    typing.TypedDict, total=False
):
    region: GoogleCloudBillingBillingaccountskugroupskusV1betaGeoTaxonomyRegion

@typing.type_check_only
class GoogleCloudBillingBillingaccountskugroupskusV1betaListBillingAccountSkuGroupSkusResponse(
    typing.TypedDict, total=False
):
    billingAccountSkuGroupSkus: _list[
        GoogleCloudBillingBillingaccountskugroupskusV1betaBillingAccountSkuGroupSku
    ]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudBillingBillingaccountskugroupskusV1betaProductTaxonomy(
    typing.TypedDict, total=False
):
    taxonomyCategories: _list[
        GoogleCloudBillingBillingaccountskugroupskusV1betaTaxonomyCategory
    ]

@typing.type_check_only
class GoogleCloudBillingBillingaccountskugroupskusV1betaTaxonomyCategory(
    typing.TypedDict, total=False
):
    category: str

@typing.type_check_only
class GoogleCloudBillingBillingaccountskusV1betaBillingAccountSku(
    typing.TypedDict, total=False
):
    billingAccountService: str
    displayName: str
    geoTaxonomy: GoogleCloudBillingBillingaccountskusV1betaGeoTaxonomy
    name: str
    productTaxonomy: GoogleCloudBillingBillingaccountskusV1betaProductTaxonomy
    skuId: str

@typing.type_check_only
class GoogleCloudBillingBillingaccountskusV1betaGeoTaxonomy(
    typing.TypedDict, total=False
):
    globalMetadata: GoogleCloudBillingBillingaccountskusV1betaGeoTaxonomyGlobal
    multiRegionalMetadata: (
        GoogleCloudBillingBillingaccountskusV1betaGeoTaxonomyMultiRegional
    )
    regionalMetadata: GoogleCloudBillingBillingaccountskusV1betaGeoTaxonomyRegional
    type: typing.Literal[
        "TYPE_UNSPECIFIED", "TYPE_GLOBAL", "TYPE_REGIONAL", "TYPE_MULTI_REGIONAL"
    ]

@typing.type_check_only
class GoogleCloudBillingBillingaccountskusV1betaGeoTaxonomyGlobal(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudBillingBillingaccountskusV1betaGeoTaxonomyMultiRegional(
    typing.TypedDict, total=False
):
    regions: _list[GoogleCloudBillingBillingaccountskusV1betaGeoTaxonomyRegion]

@typing.type_check_only
class GoogleCloudBillingBillingaccountskusV1betaGeoTaxonomyRegion(
    typing.TypedDict, total=False
):
    region: str

@typing.type_check_only
class GoogleCloudBillingBillingaccountskusV1betaGeoTaxonomyRegional(
    typing.TypedDict, total=False
):
    region: GoogleCloudBillingBillingaccountskusV1betaGeoTaxonomyRegion

@typing.type_check_only
class GoogleCloudBillingBillingaccountskusV1betaListBillingAccountSkusResponse(
    typing.TypedDict, total=False
):
    billingAccountSkus: _list[
        GoogleCloudBillingBillingaccountskusV1betaBillingAccountSku
    ]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudBillingBillingaccountskusV1betaProductTaxonomy(
    typing.TypedDict, total=False
):
    taxonomyCategories: _list[
        GoogleCloudBillingBillingaccountskusV1betaTaxonomyCategory
    ]

@typing.type_check_only
class GoogleCloudBillingBillingaccountskusV1betaTaxonomyCategory(
    typing.TypedDict, total=False
):
    category: str

@typing.type_check_only
class GoogleCloudBillingPricesV1betaAggregationInfo(typing.TypedDict, total=False):
    interval: typing.Literal[
        "INTERVAL_UNSPECIFIED", "INTERVAL_MONTHLY", "INTERVAL_DAILY"
    ]
    level: typing.Literal["LEVEL_UNSPECIFIED", "LEVEL_ACCOUNT", "LEVEL_PROJECT"]

@typing.type_check_only
class GoogleCloudBillingPricesV1betaListPricesResponse(typing.TypedDict, total=False):
    nextPageToken: str
    prices: _list[GoogleCloudBillingPricesV1betaPrice]

@typing.type_check_only
class GoogleCloudBillingPricesV1betaPrice(typing.TypedDict, total=False):
    currencyCode: str
    name: str
    rate: GoogleCloudBillingPricesV1betaRate
    valueType: str

@typing.type_check_only
class GoogleCloudBillingPricesV1betaRate(typing.TypedDict, total=False):
    aggregationInfo: GoogleCloudBillingPricesV1betaAggregationInfo
    tiers: _list[GoogleCloudBillingPricesV1betaRateTier]
    unitInfo: GoogleCloudBillingPricesV1betaUnitInfo

@typing.type_check_only
class GoogleCloudBillingPricesV1betaRateTier(typing.TypedDict, total=False):
    listPrice: Money
    startAmount: Decimal

@typing.type_check_only
class GoogleCloudBillingPricesV1betaUnitInfo(typing.TypedDict, total=False):
    unit: str
    unitDescription: str
    unitQuantity: Decimal

@typing.type_check_only
class GoogleCloudBillingSkugroupsV1betaListSkuGroupsResponse(
    typing.TypedDict, total=False
):
    nextPageToken: str
    skuGroups: _list[GoogleCloudBillingSkugroupsV1betaSkuGroup]

@typing.type_check_only
class GoogleCloudBillingSkugroupsV1betaSkuGroup(typing.TypedDict, total=False):
    displayName: str
    name: str

@typing.type_check_only
class GoogleCloudBillingSkugroupskusV1betaGeoTaxonomy(typing.TypedDict, total=False):
    globalMetadata: GoogleCloudBillingSkugroupskusV1betaGeoTaxonomyGlobal
    multiRegionalMetadata: GoogleCloudBillingSkugroupskusV1betaGeoTaxonomyMultiRegional
    regionalMetadata: GoogleCloudBillingSkugroupskusV1betaGeoTaxonomyRegional
    type: typing.Literal[
        "TYPE_UNSPECIFIED", "TYPE_GLOBAL", "TYPE_REGIONAL", "TYPE_MULTI_REGIONAL"
    ]

@typing.type_check_only
class GoogleCloudBillingSkugroupskusV1betaGeoTaxonomyGlobal(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudBillingSkugroupskusV1betaGeoTaxonomyMultiRegional(
    typing.TypedDict, total=False
):
    regions: _list[GoogleCloudBillingSkugroupskusV1betaGeoTaxonomyRegion]

@typing.type_check_only
class GoogleCloudBillingSkugroupskusV1betaGeoTaxonomyRegion(
    typing.TypedDict, total=False
):
    region: str

@typing.type_check_only
class GoogleCloudBillingSkugroupskusV1betaGeoTaxonomyRegional(
    typing.TypedDict, total=False
):
    region: GoogleCloudBillingSkugroupskusV1betaGeoTaxonomyRegion

@typing.type_check_only
class GoogleCloudBillingSkugroupskusV1betaListSkuGroupSkusResponse(
    typing.TypedDict, total=False
):
    nextPageToken: str
    skuGroupSkus: _list[GoogleCloudBillingSkugroupskusV1betaSkuGroupSku]

@typing.type_check_only
class GoogleCloudBillingSkugroupskusV1betaProductTaxonomy(
    typing.TypedDict, total=False
):
    taxonomyCategories: _list[GoogleCloudBillingSkugroupskusV1betaTaxonomyCategory]

@typing.type_check_only
class GoogleCloudBillingSkugroupskusV1betaSkuGroupSku(typing.TypedDict, total=False):
    displayName: str
    geoTaxonomy: GoogleCloudBillingSkugroupskusV1betaGeoTaxonomy
    name: str
    productTaxonomy: GoogleCloudBillingSkugroupskusV1betaProductTaxonomy
    service: str
    skuId: str

@typing.type_check_only
class GoogleCloudBillingSkugroupskusV1betaTaxonomyCategory(
    typing.TypedDict, total=False
):
    category: str

@typing.type_check_only
class Insight(typing.TypedDict, total=False):
    description: str
    severity: typing.Literal["SEVERITY_UNSPECIFIED", "INFO", "WARNING", "CRITICAL"]
    title: str

@typing.type_check_only
class InteropLink(typing.TypedDict, total=False):
    label: str
    linkType: typing.Literal[
        "LINK_TYPE_UNSPECIFIED", "COST_REPORT", "BQE_QUERY", "FINOPS_HUB"
    ]
    url: str

@typing.type_check_only
class Map(typing.TypedDict, total=False):
    entry: _list[MapEntry]

@typing.type_check_only
class MapEntry(typing.TypedDict, total=False):
    key: ValueProto
    value: ValueProto

@typing.type_check_only
class Money(typing.TypedDict, total=False):
    currencyCode: str
    nanos: int
    units: str

@typing.type_check_only
class Range(typing.TypedDict, total=False):
    end: ValueProto
    start: ValueProto

@typing.type_check_only
class Rejection(typing.TypedDict, total=False):
    displayMessage: str
    reason: typing.Literal["REASON_UNSPECIFIED", "EXPLICIT_OUT_OF_SCOPE"]

@typing.type_check_only
class Row(typing.TypedDict, total=False):
    values: _list[ValueProto]

@typing.type_check_only
class Struct(typing.TypedDict, total=False):
    field: _list[ValueProto]

@typing.type_check_only
class SuggestedChart(typing.TypedDict, total=False):
    chartTitle: str
    chartType: typing.Literal[
        "CHART_TYPE_UNSPECIFIED", "BAR_CHART", "UNCHARTABLE", "LINE_CHART", "AREA_CHART"
    ]
    seriesField: str
    xAxisField: str
    xAxisLabel: str
    yAxisField: str
    yAxisLabel: str

@typing.type_check_only
class SuggestedQuery(typing.TypedDict, total=False):
    query: str

@typing.type_check_only
class UserContext(typing.TypedDict, total=False):
    persona: typing.Literal["PERSONA_UNSPECIFIED", "FINOPS_MANAGER", "DEVELOPER"]
    role: str

@typing.type_check_only
class ValueProto(typing.TypedDict, total=False):
    ValueProtoSwitchMustHaveADefault: bool
    arrayValue: Array
    bignumericValue: str
    boolValue: bool
    bytesValue: str
    dateValue: int
    datetimeValue: Datetime
    doubleValue: float
    enumValue: int
    floatValue: float
    geographyValue: str
    int32Value: int
    int64Value: str
    intervalValue: str
    jsonValue: str
    mapValue: Map
    numericValue: str
    protoValue: str
    rangeValue: Range
    stringValue: str
    structValue: Struct
    timeValue: str
    timestampPicoValue: str
    timestampValue: str
    tokenlistValue: str
    uint32Value: int
    uint64Value: str
    uuidValue: str
