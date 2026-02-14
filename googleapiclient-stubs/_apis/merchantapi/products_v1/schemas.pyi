import typing

import typing_extensions

_list = list

@typing.type_check_only
class AutomatedDiscounts(typing_extensions.TypedDict, total=False):
    gadPrice: Price
    priorPrice: Price
    priorPriceProgressive: Price

@typing.type_check_only
class CarrierShipping(typing_extensions.TypedDict, total=False):
    carrierPrice: typing_extensions.Literal[
        "CARRIER_PRICE_OPTION_UNSPECIFIED",
        "AUSTRALIA_POST_REGULAR",
        "AUSTRALIA_POST_EXPRESS",
        "AUSTRALIA_POST_REGULAR_S",
        "AUSTRALIA_POST_REGULAR_M",
        "AUSTRALIA_POST_REGULAR_L",
        "AUSTRALIA_POST_REGULAR_XL",
        "AUSTRALIA_POST_EXPRESS_S",
        "AUSTRALIA_POST_EXPRESS_M",
        "AUSTRALIA_POST_EXPRESS_L",
        "AUSTRALIA_POST_EXPRESS_XL",
        "TNT_ROAD_EXPRESS",
        "TNT_OVERNIGHT_EXPRESS",
        "TOLL_ROAD_DELIVERY",
        "TOLL_OVERNIGHT_PRIORITY",
        "DHL_PAKET",
        "DHL_PACKCHEN",
        "DPD_EXPRESS_12",
        "DPD_EXPRESS",
        "DPD_CLASSIC_PARCEL",
        "HERMES_PACKCHEN",
        "HERMES_PAKETKLASSE_S",
        "HERMES_PAKETKLASSE_M",
        "HERMES_PAKETKLASSE_L",
        "UPS_EXPRESS",
        "UPS_EXPRESS_SAVER",
        "UPS_EXPRESS_STANDARD",
        "DHL_EXPRESS",
        "DHL_EXPRESS_12",
        "DPD_NEXT_DAY",
        "DPD_STANDARD_NEXT_DAY",
        "DPD_STANDARD_TWO_DAY",
        "RMG_1ST_CLASS_SMALL",
        "RMG_1ST_CLASS_MEDIUM",
        "RMG_2ND_CLASS_SMALL",
        "RMG_2ND_CLASS_MEDIUM",
        "TNT_EXPRESS",
        "TNT_EXPRESS_10",
        "TNT_EXPRESS_12",
        "YODEL_B2C_48HR",
        "YODEL_B2C_72HR",
        "YODEL_B2C_PACKET",
        "FEDEX_GROUND",
        "FEDEX_HOME_DELIVERY",
        "FEDEX_EXPRESS_SAVER",
        "FEDEX_FIRST_OVERNIGHT",
        "FEDEX_PRIORITY_OVERNIGHT",
        "FEDEX_STANDARD_OVERNIGHT",
        "FEDEX_2DAY",
        "UPS_STANDARD",
        "UPS_2ND_DAY_AIR",
        "UPS_2ND_DAY_AM",
        "UPS_3_DAY_SELECT",
        "UPS_GROUND",
        "UPS_NEXT_DAY_AIR",
        "UPS_NEXT_DAY_AIR_EARLY_AM",
        "UPS_NEXT_DAY_AIR_SAVER",
        "USPS_PRIORITY_MAIL_EXPRESS",
        "USPS_MEDIA_MAIL",
        "USPS_GROUND_ADVANTAGE_RETAIL",
        "USPS_PRIORITY_MAIL",
        "USPS_GROUND_ADVANTAGE_COMMERCIAL",
    ]
    carrierPriceFlatAdjustment: Price
    carrierPricePercentageAdjustment: float
    carrierTransitTime: typing_extensions.Literal[
        "CARRIER_TRANSIT_TIME_OPTION_UNSPECIFIED",
        "DHL_PAKET",
        "DHL_PACKCHEN",
        "DHL_EXPRESSEASY",
        "DPD_EXPRESS",
        "DPD_CLASSIC_PARCEL",
        "HERMES_HAUSTUR",
        "HERMES_PAKETSHOP",
        "GLS_BUSINESS",
        "GLS_EXPRESS",
        "GLS_PRIVATE",
        "COLISSIMO_DOMICILE",
        "DHL_EXPRESS_12AM",
        "DHL_EXPRESS_9AM",
        "GEODIS_EXPRESS",
        "GEODIS_PACK_30",
        "GEODIS_SAME_DAY",
        "GEODIS_TOP_24",
        "TNT_ESSENTIEL_24H",
        "TNT_ESSENTIEL_FLEXIBILITE",
        "FEDEX_GROUND",
        "FEDEX_HOME_DELIVERY",
        "FEDEX_EXPRESS_SAVER",
        "FEDEX_FIRST_OVERNIGHT",
        "FEDEX_PRIORITY_OVERNIGHT",
        "FEDEX_STANDARD_OVERNIGHT",
        "FEDEX_2DAY",
        "UPS_2ND_DAY_AIR",
        "UPS_2ND_DAY_AM",
        "UPS_3_DAY_SELECT",
        "UPS_GROUND",
        "UPS_NEXT_DAY_AIR",
        "UPS_NEXT_DAY_AIR_EARLY_AM",
        "UPS_NEXT_DAY_AIR_SAVER",
        "USPS_PRIORITY_MAIL_EXPRESS",
        "USPS_MEDIA_MAIL",
        "USPS_GROUND_ADVANTAGE_RETAIL",
        "USPS_PRIORITY_MAIL",
        "USPS_GROUND_ADVANTAGE_COMMERCIAL",
        "USPS_FIRST_CLASS_MAIL",
    ]
    country: str
    fixedMaxTransitTime: str
    fixedMinTransitTime: str
    flatPrice: Price
    maxHandlingTime: str
    minHandlingTime: str
    originPostalCode: str
    postalCode: str
    region: str

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
        "YOUTUBE_AFFILIATE",
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
class HandlingCutoffTime(typing_extensions.TypedDict, total=False):
    country: str
    cutoffTime: str
    cutoffTimezone: str
    disableDeliveryAfterCutoff: bool

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
        "YOUTUBE_AFFILIATE",
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
    automatedDiscounts: AutomatedDiscounts
    contentLanguage: str
    customAttributes: _list[CustomAttribute]
    dataSource: str
    feedLabel: str
    legacyLocal: bool
    name: str
    offerId: str
    productAttributes: ProductAttributes
    productStatus: ProductStatus
    versionNumber: str

@typing.type_check_only
class ProductAttributes(typing_extensions.TypedDict, total=False):
    additionalImageLinks: _list[str]
    adsGrouping: str
    adsLabels: _list[str]
    adsRedirect: str
    adult: bool
    ageGroup: typing_extensions.Literal[
        "AGE_GROUP_UNSPECIFIED", "ADULT", "KIDS", "TODDLER", "INFANT", "NEWBORN"
    ]
    autoPricingMinPrice: Price
    availability: typing_extensions.Literal[
        "AVAILABILITY_UNSPECIFIED",
        "IN_STOCK",
        "OUT_OF_STOCK",
        "PREORDER",
        "LIMITED_AVAILABILITY",
        "BACKORDER",
    ]
    availabilityDate: str
    brand: str
    canonicalLink: str
    carrierShipping: _list[CarrierShipping]
    certifications: _list[ProductCertification]
    cloudExportAdditionalProperties: _list[CloudExportAdditionalProperties]
    color: str
    condition: typing_extensions.Literal[
        "CONDITION_UNSPECIFIED", "NEW", "USED", "REFURBISHED"
    ]
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
    energyEfficiencyClass: typing_extensions.Literal[
        "ENERGY_EFFICIENCY_CLASS_UNSPECIFIED",
        "APPP",
        "APP",
        "AP",
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
    ]
    excludedDestinations: _list[
        typing_extensions.Literal[
            "DESTINATION_ENUM_UNSPECIFIED",
            "SHOPPING_ADS",
            "DISPLAY_ADS",
            "LOCAL_INVENTORY_ADS",
            "FREE_LISTINGS",
            "FREE_LOCAL_LISTINGS",
            "YOUTUBE_SHOPPING",
            "YOUTUBE_SHOPPING_CHECKOUT",
            "YOUTUBE_AFFILIATE",
            "FREE_VEHICLE_LISTINGS",
            "VEHICLE_ADS",
            "CLOUD_RETAIL",
            "LOCAL_CLOUD_RETAIL",
        ]
    ]
    expirationDate: str
    externalSellerId: str
    freeShippingThreshold: _list[FreeShippingThreshold]
    gender: typing_extensions.Literal["GENDER_UNSPECIFIED", "MALE", "FEMALE", "UNISEX"]
    googleProductCategory: str
    gtins: _list[str]
    handlingCutoffTimes: _list[HandlingCutoffTime]
    identifierExists: bool
    imageLink: str
    includedDestinations: _list[
        typing_extensions.Literal[
            "DESTINATION_ENUM_UNSPECIFIED",
            "SHOPPING_ADS",
            "DISPLAY_ADS",
            "LOCAL_INVENTORY_ADS",
            "FREE_LISTINGS",
            "FREE_LOCAL_LISTINGS",
            "YOUTUBE_SHOPPING",
            "YOUTUBE_SHOPPING_CHECKOUT",
            "YOUTUBE_AFFILIATE",
            "FREE_VEHICLE_LISTINGS",
            "VEHICLE_ADS",
            "CLOUD_RETAIL",
            "LOCAL_CLOUD_RETAIL",
        ]
    ]
    installment: ProductInstallment
    isBundle: bool
    itemGroupId: str
    lifestyleImageLinks: _list[str]
    link: str
    linkTemplate: str
    loyaltyPoints: LoyaltyPoints
    loyaltyPrograms: _list[LoyaltyProgram]
    material: str
    maxEnergyEfficiencyClass: typing_extensions.Literal[
        "ENERGY_EFFICIENCY_CLASS_UNSPECIFIED",
        "APPP",
        "APP",
        "AP",
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
    ]
    maxHandlingTime: str
    maximumRetailPrice: Price
    minEnergyEfficiencyClass: typing_extensions.Literal[
        "ENERGY_EFFICIENCY_CLASS_UNSPECIFIED",
        "APPP",
        "APP",
        "AP",
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
    ]
    minHandlingTime: str
    mobileLink: str
    mobileLinkTemplate: str
    mpn: str
    multipack: str
    pattern: str
    pause: typing_extensions.Literal["PAUSE_UNSPECIFIED", "ADS", "ALL"]
    pickupMethod: typing_extensions.Literal[
        "PICKUP_METHOD_UNSPECIFIED", "NOT_SUPPORTED", "BUY", "RESERVE", "SHIP_TO_STORE"
    ]
    pickupSla: typing_extensions.Literal[
        "PICKUP_SLA_UNSPECIFIED",
        "SAME_DAY",
        "NEXT_DAY",
        "TWO_DAY",
        "THREE_DAY",
        "FOUR_DAY",
        "FIVE_DAY",
        "SIX_DAY",
        "MULTI_WEEK",
    ]
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
    shippingHandlingBusinessDays: _list[ShippingBusinessDaysConfig]
    shippingHeight: ShippingDimension
    shippingLabel: str
    shippingLength: ShippingDimension
    shippingTransitBusinessDays: _list[ShippingBusinessDaysConfig]
    shippingWeight: ShippingWeight
    shippingWidth: ShippingDimension
    shoppingAdsExcludedCountries: _list[str]
    size: str
    sizeSystem: typing_extensions.Literal[
        "SIZE_SYSTEM_UNSPECIFIED",
        "AU",
        "BR",
        "CN",
        "DE",
        "EU",
        "FR",
        "IT",
        "JP",
        "MEX",
        "UK",
        "US",
    ]
    sizeTypes: _list[
        typing_extensions.Literal[
            "SIZE_TYPE_UNSPECIFIED",
            "REGULAR",
            "PETITE",
            "MATERNITY",
            "BIG",
            "TALL",
            "PLUS",
        ]
    ]
    structuredDescription: StructuredDescription
    structuredTitle: StructuredTitle
    subscriptionCost: SubscriptionCost
    sustainabilityIncentives: _list[ProductSustainabilityIncentive]
    title: str
    transitTimeLabel: str
    unitPricingBaseMeasure: UnitPricingBaseMeasure
    unitPricingMeasure: UnitPricingMeasure
    virtualModelLink: str

@typing.type_check_only
class ProductCertification(typing_extensions.TypedDict, total=False):
    certificationAuthority: typing_extensions.Literal[
        "CERTIFICATION_AUTHORITY_UNSPECIFIED", "ADEME", "BMWK", "EPA", "EC"
    ]
    certificationCode: str
    certificationName: typing_extensions.Literal[
        "CERTIFICATION_NAME_UNSPECIFIED",
        "ENERGY_STAR",
        "ENERGY_STAR_MOST_EFFICIENT",
        "EPREL",
        "EU_ECOLABEL",
        "VEHICLE_ENERGY_EFFICIENCY",
        "VEHICLE_ENERGY_EFFICIENCY_DISCHARGED_BATTERY",
    ]
    certificationValue: str

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
        "YOUTUBE_AFFILIATE",
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
    contentLanguage: str
    customAttributes: _list[CustomAttribute]
    feedLabel: str
    legacyLocal: bool
    name: str
    offerId: str
    product: str
    productAttributes: ProductAttributes
    versionNumber: str

@typing.type_check_only
class ProductInstallment(typing_extensions.TypedDict, total=False):
    amount: Price
    creditType: typing_extensions.Literal["CREDIT_TYPE_UNSPECIFIED", "FINANCE", "LEASE"]
    downpayment: Price
    months: str

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
    eventTime: str
    expirationTime: str
    managingAccount: str
    resource: str
    resourceId: str
    resourceType: typing_extensions.Literal["RESOURCE_UNSPECIFIED", "PRODUCT"]

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
    handlingCutoffTime: str
    handlingCutoffTimezone: str
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
class ShippingBusinessDaysConfig(typing_extensions.TypedDict, total=False):
    businessDays: str
    country: str

@typing.type_check_only
class ShippingDimension(typing_extensions.TypedDict, total=False):
    unit: str
    value: float

@typing.type_check_only
class ShippingWeight(typing_extensions.TypedDict, total=False):
    unit: str
    value: float

@typing.type_check_only
class StructuredDescription(typing_extensions.TypedDict, total=False):
    content: str
    digitalSourceType: typing_extensions.Literal[
        "DIGITAL_SOURCE_TYPE_UNSPECIFIED", "TRAINED_ALGORITHMIC_MEDIA", "DEFAULT"
    ]

@typing.type_check_only
class StructuredTitle(typing_extensions.TypedDict, total=False):
    content: str
    digitalSourceType: typing_extensions.Literal[
        "DIGITAL_SOURCE_TYPE_UNSPECIFIED", "TRAINED_ALGORITHMIC_MEDIA", "DEFAULT"
    ]

@typing.type_check_only
class SubscriptionCost(typing_extensions.TypedDict, total=False):
    amount: Price
    period: typing_extensions.Literal[
        "SUBSCRIPTION_PERIOD_UNSPECIFIED", "MONTH", "YEAR", "WEEK"
    ]
    periodLength: str

@typing.type_check_only
class UnitPricingBaseMeasure(typing_extensions.TypedDict, total=False):
    unit: str
    value: str

@typing.type_check_only
class UnitPricingMeasure(typing_extensions.TypedDict, total=False):
    unit: str
    value: float
