import typing

import typing_extensions

_list = list

@typing.type_check_only
class Decimal(typing_extensions.TypedDict, total=False):
    value: str

@typing.type_check_only
class GoogleCloudBillingBillingaccountpricesV1betaAggregationInfo(
    typing_extensions.TypedDict, total=False
):
    interval: typing_extensions.Literal[
        "INTERVAL_UNSPECIFIED", "INTERVAL_MONTHLY", "INTERVAL_DAILY"
    ]
    level: typing_extensions.Literal[
        "LEVEL_UNSPECIFIED", "LEVEL_ACCOUNT", "LEVEL_PROJECT"
    ]

@typing.type_check_only
class GoogleCloudBillingBillingaccountpricesV1betaBillingAccountPrice(
    typing_extensions.TypedDict, total=False
):
    currencyCode: str
    name: str
    priceReason: GoogleCloudBillingBillingaccountpricesV1betaPriceReason
    rate: GoogleCloudBillingBillingaccountpricesV1betaRate
    valueType: str

@typing.type_check_only
class GoogleCloudBillingBillingaccountpricesV1betaDefaultPrice(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudBillingBillingaccountpricesV1betaFixedDiscount(
    typing_extensions.TypedDict, total=False
):
    discountPercent: Decimal
    discountScopeType: str
    fixTime: str
    skuGroup: str

@typing.type_check_only
class GoogleCloudBillingBillingaccountpricesV1betaFixedPrice(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudBillingBillingaccountpricesV1betaFloatingDiscount(
    typing_extensions.TypedDict, total=False
):
    discountPercent: Decimal
    discountScopeType: str
    skuGroup: str

@typing.type_check_only
class GoogleCloudBillingBillingaccountpricesV1betaListBillingAccountPricesResponse(
    typing_extensions.TypedDict, total=False
):
    billingAccountPrices: _list[
        GoogleCloudBillingBillingaccountpricesV1betaBillingAccountPrice
    ]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudBillingBillingaccountpricesV1betaListPriceAsCeiling(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudBillingBillingaccountpricesV1betaMergedPrice(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudBillingBillingaccountpricesV1betaMigratedPrice(
    typing_extensions.TypedDict, total=False
):
    sourceSku: str

@typing.type_check_only
class GoogleCloudBillingBillingaccountpricesV1betaPriceReason(
    typing_extensions.TypedDict, total=False
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
class GoogleCloudBillingBillingaccountpricesV1betaRate(
    typing_extensions.TypedDict, total=False
):
    aggregationInfo: GoogleCloudBillingBillingaccountpricesV1betaAggregationInfo
    tiers: _list[GoogleCloudBillingBillingaccountpricesV1betaRateTier]
    unitInfo: GoogleCloudBillingBillingaccountpricesV1betaUnitInfo

@typing.type_check_only
class GoogleCloudBillingBillingaccountpricesV1betaRateTier(
    typing_extensions.TypedDict, total=False
):
    contractPrice: Money
    effectiveDiscountPercent: Decimal
    listPrice: Money
    startAmount: Decimal

@typing.type_check_only
class GoogleCloudBillingBillingaccountpricesV1betaUnitInfo(
    typing_extensions.TypedDict, total=False
):
    unit: str
    unitDescription: str
    unitQuantity: Decimal

@typing.type_check_only
class GoogleCloudBillingBillingaccountservicesV1betaBillingAccountService(
    typing_extensions.TypedDict, total=False
):
    displayName: str
    name: str
    serviceId: str

@typing.type_check_only
class GoogleCloudBillingBillingaccountservicesV1betaListBillingAccountServicesResponse(
    typing_extensions.TypedDict, total=False
):
    billingAccountServices: _list[
        GoogleCloudBillingBillingaccountservicesV1betaBillingAccountService
    ]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudBillingBillingaccountskugroupsV1betaBillingAccountSkuGroup(
    typing_extensions.TypedDict, total=False
):
    displayName: str
    name: str

@typing.type_check_only
class GoogleCloudBillingBillingaccountskugroupsV1betaListBillingAccountSkuGroupsResponse(
    typing_extensions.TypedDict, total=False
):
    billingAccountSkuGroups: _list[
        GoogleCloudBillingBillingaccountskugroupsV1betaBillingAccountSkuGroup
    ]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudBillingBillingaccountskugroupskusV1betaBillingAccountSkuGroupSku(
    typing_extensions.TypedDict, total=False
):
    billingAccountService: str
    displayName: str
    geoTaxonomy: GoogleCloudBillingBillingaccountskugroupskusV1betaGeoTaxonomy
    name: str
    productTaxonomy: GoogleCloudBillingBillingaccountskugroupskusV1betaProductTaxonomy
    skuId: str

@typing.type_check_only
class GoogleCloudBillingBillingaccountskugroupskusV1betaGeoTaxonomy(
    typing_extensions.TypedDict, total=False
):
    globalMetadata: GoogleCloudBillingBillingaccountskugroupskusV1betaGeoTaxonomyGlobal
    multiRegionalMetadata: (
        GoogleCloudBillingBillingaccountskugroupskusV1betaGeoTaxonomyMultiRegional
    )
    regionalMetadata: (
        GoogleCloudBillingBillingaccountskugroupskusV1betaGeoTaxonomyRegional
    )
    type: typing_extensions.Literal[
        "TYPE_UNSPECIFIED", "TYPE_GLOBAL", "TYPE_REGIONAL", "TYPE_MULTI_REGIONAL"
    ]

@typing.type_check_only
class GoogleCloudBillingBillingaccountskugroupskusV1betaGeoTaxonomyGlobal(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudBillingBillingaccountskugroupskusV1betaGeoTaxonomyMultiRegional(
    typing_extensions.TypedDict, total=False
):
    regions: _list[GoogleCloudBillingBillingaccountskugroupskusV1betaGeoTaxonomyRegion]

@typing.type_check_only
class GoogleCloudBillingBillingaccountskugroupskusV1betaGeoTaxonomyRegion(
    typing_extensions.TypedDict, total=False
):
    region: str

@typing.type_check_only
class GoogleCloudBillingBillingaccountskugroupskusV1betaGeoTaxonomyRegional(
    typing_extensions.TypedDict, total=False
):
    region: GoogleCloudBillingBillingaccountskugroupskusV1betaGeoTaxonomyRegion

@typing.type_check_only
class GoogleCloudBillingBillingaccountskugroupskusV1betaListBillingAccountSkuGroupSkusResponse(
    typing_extensions.TypedDict, total=False
):
    billingAccountSkuGroupSkus: _list[
        GoogleCloudBillingBillingaccountskugroupskusV1betaBillingAccountSkuGroupSku
    ]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudBillingBillingaccountskugroupskusV1betaProductTaxonomy(
    typing_extensions.TypedDict, total=False
):
    taxonomyCategories: _list[
        GoogleCloudBillingBillingaccountskugroupskusV1betaTaxonomyCategory
    ]

@typing.type_check_only
class GoogleCloudBillingBillingaccountskugroupskusV1betaTaxonomyCategory(
    typing_extensions.TypedDict, total=False
):
    category: str

@typing.type_check_only
class GoogleCloudBillingBillingaccountskusV1betaBillingAccountSku(
    typing_extensions.TypedDict, total=False
):
    billingAccountService: str
    displayName: str
    geoTaxonomy: GoogleCloudBillingBillingaccountskusV1betaGeoTaxonomy
    name: str
    productTaxonomy: GoogleCloudBillingBillingaccountskusV1betaProductTaxonomy
    skuId: str

@typing.type_check_only
class GoogleCloudBillingBillingaccountskusV1betaGeoTaxonomy(
    typing_extensions.TypedDict, total=False
):
    globalMetadata: GoogleCloudBillingBillingaccountskusV1betaGeoTaxonomyGlobal
    multiRegionalMetadata: (
        GoogleCloudBillingBillingaccountskusV1betaGeoTaxonomyMultiRegional
    )
    regionalMetadata: GoogleCloudBillingBillingaccountskusV1betaGeoTaxonomyRegional
    type: typing_extensions.Literal[
        "TYPE_UNSPECIFIED", "TYPE_GLOBAL", "TYPE_REGIONAL", "TYPE_MULTI_REGIONAL"
    ]

@typing.type_check_only
class GoogleCloudBillingBillingaccountskusV1betaGeoTaxonomyGlobal(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudBillingBillingaccountskusV1betaGeoTaxonomyMultiRegional(
    typing_extensions.TypedDict, total=False
):
    regions: _list[GoogleCloudBillingBillingaccountskusV1betaGeoTaxonomyRegion]

@typing.type_check_only
class GoogleCloudBillingBillingaccountskusV1betaGeoTaxonomyRegion(
    typing_extensions.TypedDict, total=False
):
    region: str

@typing.type_check_only
class GoogleCloudBillingBillingaccountskusV1betaGeoTaxonomyRegional(
    typing_extensions.TypedDict, total=False
):
    region: GoogleCloudBillingBillingaccountskusV1betaGeoTaxonomyRegion

@typing.type_check_only
class GoogleCloudBillingBillingaccountskusV1betaListBillingAccountSkusResponse(
    typing_extensions.TypedDict, total=False
):
    billingAccountSkus: _list[
        GoogleCloudBillingBillingaccountskusV1betaBillingAccountSku
    ]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudBillingBillingaccountskusV1betaProductTaxonomy(
    typing_extensions.TypedDict, total=False
):
    taxonomyCategories: _list[
        GoogleCloudBillingBillingaccountskusV1betaTaxonomyCategory
    ]

@typing.type_check_only
class GoogleCloudBillingBillingaccountskusV1betaTaxonomyCategory(
    typing_extensions.TypedDict, total=False
):
    category: str

@typing.type_check_only
class GoogleCloudBillingPricesV1betaAggregationInfo(
    typing_extensions.TypedDict, total=False
):
    interval: typing_extensions.Literal[
        "INTERVAL_UNSPECIFIED", "INTERVAL_MONTHLY", "INTERVAL_DAILY"
    ]
    level: typing_extensions.Literal[
        "LEVEL_UNSPECIFIED", "LEVEL_ACCOUNT", "LEVEL_PROJECT"
    ]

@typing.type_check_only
class GoogleCloudBillingPricesV1betaListPricesResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    prices: _list[GoogleCloudBillingPricesV1betaPrice]

@typing.type_check_only
class GoogleCloudBillingPricesV1betaPrice(typing_extensions.TypedDict, total=False):
    currencyCode: str
    name: str
    rate: GoogleCloudBillingPricesV1betaRate
    valueType: str

@typing.type_check_only
class GoogleCloudBillingPricesV1betaRate(typing_extensions.TypedDict, total=False):
    aggregationInfo: GoogleCloudBillingPricesV1betaAggregationInfo
    tiers: _list[GoogleCloudBillingPricesV1betaRateTier]
    unitInfo: GoogleCloudBillingPricesV1betaUnitInfo

@typing.type_check_only
class GoogleCloudBillingPricesV1betaRateTier(typing_extensions.TypedDict, total=False):
    listPrice: Money
    startAmount: Decimal

@typing.type_check_only
class GoogleCloudBillingPricesV1betaUnitInfo(typing_extensions.TypedDict, total=False):
    unit: str
    unitDescription: str
    unitQuantity: Decimal

@typing.type_check_only
class GoogleCloudBillingSkugroupsV1betaListSkuGroupsResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    skuGroups: _list[GoogleCloudBillingSkugroupsV1betaSkuGroup]

@typing.type_check_only
class GoogleCloudBillingSkugroupsV1betaSkuGroup(
    typing_extensions.TypedDict, total=False
):
    displayName: str
    name: str

@typing.type_check_only
class GoogleCloudBillingSkugroupskusV1betaGeoTaxonomy(
    typing_extensions.TypedDict, total=False
):
    globalMetadata: GoogleCloudBillingSkugroupskusV1betaGeoTaxonomyGlobal
    multiRegionalMetadata: GoogleCloudBillingSkugroupskusV1betaGeoTaxonomyMultiRegional
    regionalMetadata: GoogleCloudBillingSkugroupskusV1betaGeoTaxonomyRegional
    type: typing_extensions.Literal[
        "TYPE_UNSPECIFIED", "TYPE_GLOBAL", "TYPE_REGIONAL", "TYPE_MULTI_REGIONAL"
    ]

@typing.type_check_only
class GoogleCloudBillingSkugroupskusV1betaGeoTaxonomyGlobal(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudBillingSkugroupskusV1betaGeoTaxonomyMultiRegional(
    typing_extensions.TypedDict, total=False
):
    regions: _list[GoogleCloudBillingSkugroupskusV1betaGeoTaxonomyRegion]

@typing.type_check_only
class GoogleCloudBillingSkugroupskusV1betaGeoTaxonomyRegion(
    typing_extensions.TypedDict, total=False
):
    region: str

@typing.type_check_only
class GoogleCloudBillingSkugroupskusV1betaGeoTaxonomyRegional(
    typing_extensions.TypedDict, total=False
):
    region: GoogleCloudBillingSkugroupskusV1betaGeoTaxonomyRegion

@typing.type_check_only
class GoogleCloudBillingSkugroupskusV1betaListSkuGroupSkusResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    skuGroupSkus: _list[GoogleCloudBillingSkugroupskusV1betaSkuGroupSku]

@typing.type_check_only
class GoogleCloudBillingSkugroupskusV1betaProductTaxonomy(
    typing_extensions.TypedDict, total=False
):
    taxonomyCategories: _list[GoogleCloudBillingSkugroupskusV1betaTaxonomyCategory]

@typing.type_check_only
class GoogleCloudBillingSkugroupskusV1betaSkuGroupSku(
    typing_extensions.TypedDict, total=False
):
    displayName: str
    geoTaxonomy: GoogleCloudBillingSkugroupskusV1betaGeoTaxonomy
    name: str
    productTaxonomy: GoogleCloudBillingSkugroupskusV1betaProductTaxonomy
    service: str
    skuId: str

@typing.type_check_only
class GoogleCloudBillingSkugroupskusV1betaTaxonomyCategory(
    typing_extensions.TypedDict, total=False
):
    category: str

@typing.type_check_only
class Money(typing_extensions.TypedDict, total=False):
    currencyCode: str
    nanos: int
    units: str
