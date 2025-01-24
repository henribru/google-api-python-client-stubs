import typing

import typing_extensions

_list = list

@typing.type_check_only
class Attributes(typing_extensions.TypedDict, total=False):
    additionalImageLinks: _list[str]
    adsGrouping: str
    adsLabels: _list[str]
    adsRedirect: str
    adult: bool
    ageGroup: str
    autoPricingMinPrice: Price
    availability: str
    availabilityDate: str
    brand: str
    canonicalLink: str
    certifications: _list[Certification]
    cloudExportAdditionalProperties: _list[CloudExportAdditionalProperties]
    color: str
    condition: str
    costOfGoodsSold: Price
    customLabel0: str
    customLabel1: str
    customLabel2: str
    customLabel3: str
    customLabel4: str
    description: str
    disclosureDate: str
    displayAdsId: str
    displayAdsLink: str
    displayAdsSimilarIds: _list[str]
    displayAdsTitle: str
    displayAdsValue: float
    energyEfficiencyClass: str
    excludedDestinations: _list[str]
    expirationDate: str
    externalSellerId: str
    freeShippingThreshold: _list[FreeShippingThreshold]
    gender: str
    googleProductCategory: str
    gtin: _list[str]
    identifierExists: bool
    imageLink: str
    includedDestinations: _list[str]
    installment: Installment
    isBundle: bool
    itemGroupId: str
    lifestyleImageLinks: _list[str]
    link: str
    linkTemplate: str
    loyaltyPoints: LoyaltyPoints
    loyaltyPrograms: _list[LoyaltyProgram]
    material: str
    maxEnergyEfficiencyClass: str
    maxHandlingTime: str
    minEnergyEfficiencyClass: str
    minHandlingTime: str
    mobileLink: str
    mobileLinkTemplate: str
    mpn: str
    multipack: str
    pattern: str
    pause: str
    pickupMethod: str
    pickupSla: str
    price: Price
    productDetails: _list[ProductDetail]
    productHeight: ProductDimension
    productHighlights: _list[str]
    productLength: ProductDimension
    productTypes: _list[str]
    productWeight: ProductWeight
    productWidth: ProductDimension
    promotionIds: _list[str]
    salePrice: Price
    salePriceEffectiveDate: Interval
    sellOnGoogleQuantity: str
    shipping: _list[Shipping]
    shippingHeight: ShippingDimension
    shippingLabel: str
    shippingLength: ShippingDimension
    shippingWeight: ShippingWeight
    shippingWidth: ShippingDimension
    shoppingAdsExcludedCountries: _list[str]
    size: str
    sizeSystem: str
    sizeTypes: _list[str]
    structuredDescription: ProductStructuredDescription
    structuredTitle: ProductStructuredTitle
    subscriptionCost: SubscriptionCost
    sustainabilityIncentives: _list[ProductSustainabilityIncentive]
    taxCategory: str
    taxes: _list[Tax]
    title: str
    transitTimeLabel: str
    unitPricingBaseMeasure: UnitPricingBaseMeasure
    unitPricingMeasure: UnitPricingMeasure
    virtualModelLink: str

@typing.type_check_only
class Certification(typing_extensions.TypedDict, total=False):
    certificationAuthority: str
    certificationCode: str
    certificationName: str
    certificationValue: str

@typing.type_check_only
class CloudExportAdditionalProperties(typing_extensions.TypedDict, total=False):
    boolValue: bool
    floatValue: _list[float]
    intValue: _list[str]
    maxValue: float
    minValue: float
    propertyName: str
    textValue: _list[str]
    unitCode: str

@typing.type_check_only
class CustomAttribute(typing_extensions.TypedDict, total=False):
    groupValues: _list[CustomAttribute]
    name: str
    value: str

@typing.type_check_only
class DestinationStatus(typing_extensions.TypedDict, total=False):
    approvedCountries: _list[str]
    disapprovedCountries: _list[str]
    pendingCountries: _list[str]
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
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class FreeShippingThreshold(typing_extensions.TypedDict, total=False):
    country: str
    priceThreshold: Price

@typing.type_check_only
class Installment(typing_extensions.TypedDict, total=False):
    amount: Price
    creditType: str
    downpayment: Price
    months: str

@typing.type_check_only
class Interval(typing_extensions.TypedDict, total=False):
    endTime: str
    startTime: str

@typing.type_check_only
class ItemLevelIssue(typing_extensions.TypedDict, total=False):
    applicableCountries: _list[str]
    attribute: str
    code: str
    description: str
    detail: str
    documentation: str
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
    resolution: str
    severity: typing_extensions.Literal[
        "SEVERITY_UNSPECIFIED", "NOT_IMPACTED", "DEMOTED", "DISAPPROVED"
    ]

@typing.type_check_only
class ListProductsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    products: _list[Product]

@typing.type_check_only
class LoyaltyPoints(typing_extensions.TypedDict, total=False):
    name: str
    pointsValue: str
    ratio: float

@typing.type_check_only
class LoyaltyProgram(typing_extensions.TypedDict, total=False):
    cashbackForFutureUse: Price
    loyaltyPoints: str
    memberPriceEffectiveDate: Interval
    price: Price
    programLabel: str
    shippingLabel: str
    tierLabel: str

@typing.type_check_only
class Price(typing_extensions.TypedDict, total=False):
    amountMicros: str
    currencyCode: str

@typing.type_check_only
class Product(typing_extensions.TypedDict, total=False):
    attributes: Attributes
    channel: typing_extensions.Literal["CHANNEL_ENUM_UNSPECIFIED", "ONLINE", "LOCAL"]
    contentLanguage: str
    customAttributes: _list[CustomAttribute]
    dataSource: str
    feedLabel: str
    name: str
    offerId: str
    productStatus: ProductStatus
    versionNumber: str

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
class ProductDetail(typing_extensions.TypedDict, total=False):
    attributeName: str
    attributeValue: str
    sectionName: str

@typing.type_check_only
class ProductDimension(typing_extensions.TypedDict, total=False):
    unit: str
    value: float

@typing.type_check_only
class ProductInput(typing_extensions.TypedDict, total=False):
    attributes: Attributes
    channel: typing_extensions.Literal["CHANNEL_ENUM_UNSPECIFIED", "ONLINE", "LOCAL"]
    contentLanguage: str
    customAttributes: _list[CustomAttribute]
    feedLabel: str
    name: str
    offerId: str
    product: str
    versionNumber: str

@typing.type_check_only
class ProductStatus(typing_extensions.TypedDict, total=False):
    creationDate: str
    destinationStatuses: _list[DestinationStatus]
    googleExpirationDate: str
    itemLevelIssues: _list[ItemLevelIssue]
    lastUpdateDate: str

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
class ProductStructuredDescription(typing_extensions.TypedDict, total=False):
    content: str
    digitalSourceType: str

@typing.type_check_only
class ProductStructuredTitle(typing_extensions.TypedDict, total=False):
    content: str
    digitalSourceType: str

@typing.type_check_only
class ProductSustainabilityIncentive(typing_extensions.TypedDict, total=False):
    amount: Price
    percentage: float
    type: typing_extensions.Literal[
        "TYPE_UNSPECIFIED", "EV_TAX_CREDIT", "EV_PRICE_DISCOUNT"
    ]

@typing.type_check_only
class ProductWeight(typing_extensions.TypedDict, total=False):
    unit: str
    value: float

@typing.type_check_only
class Shipping(typing_extensions.TypedDict, total=False):
    country: str
    locationGroupName: str
    locationId: str
    maxHandlingTime: str
    maxTransitTime: str
    minHandlingTime: str
    minTransitTime: str
    postalCode: str
    price: Price
    region: str
    service: str

@typing.type_check_only
class ShippingDimension(typing_extensions.TypedDict, total=False):
    unit: str
    value: float

@typing.type_check_only
class ShippingWeight(typing_extensions.TypedDict, total=False):
    unit: str
    value: float

@typing.type_check_only
class SubscriptionCost(typing_extensions.TypedDict, total=False):
    amount: Price
    period: typing_extensions.Literal[
        "SUBSCRIPTION_PERIOD_UNSPECIFIED", "MONTH", "YEAR"
    ]
    periodLength: str

@typing.type_check_only
class Tax(typing_extensions.TypedDict, total=False):
    country: str
    locationId: str
    postalCode: str
    rate: float
    region: str
    taxShip: bool

@typing.type_check_only
class UnitPricingBaseMeasure(typing_extensions.TypedDict, total=False):
    unit: str
    value: str

@typing.type_check_only
class UnitPricingMeasure(typing_extensions.TypedDict, total=False):
    unit: str
    value: float
