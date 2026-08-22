import typing

_list = list

@typing.type_check_only
class AutomatedDiscounts(typing.TypedDict, total=False):
    gadPrice: Price
    priorPrice: Price
    priorPriceProgressive: Price

@typing.type_check_only
class CarrierShipping(typing.TypedDict, total=False):
    carrierPrice: typing.Literal[
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
    carrierTransitTime: typing.Literal[
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
class CloudExportAdditionalProperties(typing.TypedDict, total=False):
    boolValue: bool
    floatValue: _list[float]
    intValue: _list[str]
    maxValue: float
    minValue: float
    propertyName: str
    textValue: _list[str]
    unitCode: str

@typing.type_check_only
class Co2Emissions(typing.TypedDict, total=False):
    unit: typing.Literal["UNIT_UNSPECIFIED", "GPERKM"]
    value: str

@typing.type_check_only
class CustomAttribute(typing.TypedDict, total=False):
    groupValues: _list[CustomAttribute]
    name: str
    value: str

@typing.type_check_only
class DestinationStatus(typing.TypedDict, total=False):
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

@typing.type_check_only
class DisplayAddress(typing.TypedDict, total=False):
    city: str
    postalCode: str
    region: str
    streetName: str
    streetNumber: str

@typing.type_check_only
class Empty(typing.TypedDict, total=False): ...

@typing.type_check_only
class EnergyConsumption(typing.TypedDict, total=False):
    unit: typing.Literal["UNIT_UNSPECIFIED", "KWHPER100KM"]
    value: float

@typing.type_check_only
class FreeShippingThreshold(typing.TypedDict, total=False):
    country: str
    priceThreshold: Price

@typing.type_check_only
class FuelConsumption(typing.TypedDict, total=False):
    unit: typing.Literal["UNIT_UNSPECIFIED", "LPER100KM", "KGPER100KM"]
    value: float

@typing.type_check_only
class HandlingCutoffTime(typing.TypedDict, total=False):
    country: str
    cutoffTime: str
    cutoffTimezone: str
    disableDeliveryAfterCutoff: bool

@typing.type_check_only
class Interval(typing.TypedDict, total=False):
    endTime: str
    startTime: str

@typing.type_check_only
class ItemLevelIssue(typing.TypedDict, total=False):
    applicableCountries: _list[str]
    attribute: str
    code: str
    description: str
    detail: str
    documentation: str
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
    resolution: str
    severity: typing.Literal[
        "SEVERITY_UNSPECIFIED", "NOT_IMPACTED", "DEMOTED", "DISAPPROVED"
    ]

@typing.type_check_only
class LeaseTerm(typing.TypedDict, total=False):
    durationUnit: typing.Literal["DURATION_UNIT_UNSPECIFIED", "MONTHS", "WEEKS"]
    durationValue: str
    type: typing.Literal["LEASE_TERM_TYPE_UNSPECIFIED", "FIXED_TERM"]

@typing.type_check_only
class ListProductsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    products: _list[Product]

@typing.type_check_only
class LoyaltyPoints(typing.TypedDict, total=False):
    name: str
    pointsValue: str
    ratio: float

@typing.type_check_only
class LoyaltyProgram(typing.TypedDict, total=False):
    cashbackForFutureUse: Price
    loyaltyPoints: str
    memberPriceEffectiveDate: Interval
    price: Price
    programLabel: str
    shippingLabel: str
    tierLabel: str

@typing.type_check_only
class Mileage(typing.TypedDict, total=False):
    unit: typing.Literal["UNIT_UNSPECIFIED", "MILES", "KM"]
    value: str

@typing.type_check_only
class PetPolicy(typing.TypedDict, total=False):
    petTypes: _list[
        typing.Literal["PET_TYPE_UNSPECIFIED", "CATS", "LARGE_DOGS", "SMALL_DOGS"]
    ]
    petsAllowed: bool

@typing.type_check_only
class PickupCost(typing.TypedDict, total=False):
    flatRate: Price
    freeThreshold: Price

@typing.type_check_only
class Price(typing.TypedDict, total=False):
    amountMicros: str
    currencyCode: str

@typing.type_check_only
class Product(typing.TypedDict, total=False):
    archived: bool
    automatedDiscounts: AutomatedDiscounts
    base64EncodedName: str
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
class ProductAttributes(typing.TypedDict, total=False):
    additionalImageLinks: _list[str]
    adsGrouping: str
    adsLabels: _list[str]
    adsRedirect: str
    adult: bool
    ageGroup: typing.Literal[
        "AGE_GROUP_UNSPECIFIED", "ADULT", "KIDS", "TODDLER", "INFANT", "NEWBORN"
    ]
    amenityFeature: _list[
        typing.Literal[
            "AMENITY_FEATURE_UNSPECIFIED",
            "BALCONY",
            "BASEMENT",
            "BASKETBALL_COURT",
            "BIKE_STORAGE",
            "CENTRAL_AC",
            "DISHWASHER",
            "DOG_PARK",
            "ELEVATOR",
            "EV_CHARGING",
            "FENCED_LOT",
            "FIREPLACE",
            "FITNESS_CENTER",
            "FORCED_AIR_HEATING",
            "FULLY_FURNISHED",
            "GARAGE",
            "GATED_COMMUNITY",
            "HARDWOOD_FLOORS",
            "HIGH_SPEED_INTERNET",
            "INTERCOM",
            "IN_UNIT_WASHER_DRYER",
            "KITCHEN",
            "LARGE_CLOSETS",
            "MULTISPORT_COURT",
            "ONSITE_LAUNDRY",
            "OUTDOOR_LOUNGE",
            "PARKING",
            "PATIO",
            "PICKLEBALL_COURT",
            "POOL",
            "REFRIGERATOR",
            "SOCCER_FIELD",
            "TENNIS_COURT",
            "WALK_IN_CLOSETS",
            "WHEELCHAIR_ACCESS",
        ]
    ]
    autoPricingMinPrice: Price
    availability: typing.Literal[
        "AVAILABILITY_UNSPECIFIED",
        "IN_STOCK",
        "OUT_OF_STOCK",
        "PREORDER",
        "LIMITED_AVAILABILITY",
        "BACKORDER",
    ]
    availabilityDate: str
    bodyStyle: typing.Literal[
        "VEHICLE_BODY_STYLE_UNSPECIFIED",
        "ATV_SPORT",
        "ATV_TOURING",
        "ATV_UTILITY",
        "ATV_YOUTH",
        "CITY_CAR",
        "CLASS_A_MOTORHOME",
        "CLASS_B_MOTORHOME",
        "CLASS_C_MOTORHOME",
        "COMPACT_SUV",
        "CONVERTIBLE",
        "COUPE",
        "CROSSOVER",
        "FIFTH_WHEEL",
        "FULL_SIZE_VAN",
        "HATCHBACK",
        "LIMOUSINE",
        "MINIVAN",
        "NOTCHBACK",
        "POP_UP_CAMPER",
        "SEDAN",
        "SIDE_BY_SIDE",
        "STATION_WAGON",
        "SUV",
        "TRAVEL_TRAILER",
        "TRUCK",
        "TRUCK_CAMPER",
        "UTE",
        "UTV_RECREATIONAL_UTILITY",
        "UTV_SPORT",
        "UTV_UTILITY",
        "UTV_YOUTH",
    ]
    brand: str
    canonicalLink: str
    carrierShipping: _list[CarrierShipping]
    certifications: _list[ProductCertification]
    certifiedPreOwned: bool
    cloudExportAdditionalProperties: _list[CloudExportAdditionalProperties]
    co2Emissions: Co2Emissions
    color: str
    condition: typing.Literal["CONDITION_UNSPECIFIED", "NEW", "USED", "REFURBISHED"]
    costOfGoodsSold: Price
    customLabel0: str
    customLabel1: str
    customLabel2: str
    customLabel3: str
    customLabel4: str
    dateFirstRegistered: str
    description: str
    disclosureDate: str
    displayAddress: DisplayAddress
    displayAdsId: str
    displayAdsLink: str
    displayAdsSimilarIds: _list[str]
    displayAdsTitle: str
    displayAdsValue: float
    documentLinks: _list[str]
    electricRange: Mileage
    emissionsStandard: typing.Literal[
        "EMISSIONS_STANDARD_UNSPECIFIED",
        "ZERO_EMISSIONS",
        "EURO1",
        "EURO2",
        "EURO3",
        "EURO4",
        "EURO5",
        "EURO5B",
        "EURO6",
        "EURO6C",
        "EURO6D",
        "EURO6D_TEMP",
        "EURO6E",
    ]
    energyConsumption: EnergyConsumption
    energyEfficiencyClass: typing.Literal[
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
    engine: typing.Literal[
        "ENGINE_TYPE_UNSPECIFIED",
        "GASOLINE",
        "DIESEL",
        "ELECTRIC",
        "HYBRID",
        "PLUG_IN_HYBRID",
        "NATURAL_GAS",
        "LPG",
        "METHANE",
        "OTHER",
    ]
    excludedDestinations: _list[
        typing.Literal[
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
    fuelConsumption: FuelConsumption
    fuelConsumptionDischargedBattery: FuelConsumption
    gender: typing.Literal["GENDER_UNSPECIFIED", "MALE", "FEMALE", "UNISEX"]
    googleProductCategory: str
    gtins: _list[str]
    handlingCutoffTimes: _list[HandlingCutoffTime]
    identifierExists: bool
    imageLink: str
    includedDestinations: _list[
        typing.Literal[
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
    itemGroupTitle: str
    latitude: float
    leaseTerm: LeaseTerm
    lifestyleImageLinks: _list[str]
    link: str
    linkTemplate: str
    longitude: float
    loyaltyPoints: LoyaltyPoints
    loyaltyPrograms: _list[LoyaltyProgram]
    material: str
    maxEnergyEfficiencyClass: typing.Literal[
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
    mileage: Mileage
    minEnergyEfficiencyClass: typing.Literal[
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
    minimumOrderValues: _list[ProductMinimumOrderValue]
    mobileLink: str
    mobileLinkTemplate: str
    model: str
    mpn: str
    multipack: str
    neighborhood: str
    numberOfBathrooms: float
    numberOfBedrooms: float
    numberOfUnits: str
    pattern: str
    pause: typing.Literal["PAUSE_UNSPECIFIED", "ADS", "ALL"]
    petPolicy: PetPolicy
    pickupCost: PickupCost
    pickupMethod: typing.Literal[
        "PICKUP_METHOD_UNSPECIFIED", "NOT_SUPPORTED", "BUY", "RESERVE", "SHIP_TO_STORE"
    ]
    pickupSla: typing.Literal[
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
    popularityRank: float
    price: Price
    productDetails: _list[ProductDetail]
    productFee: _list[ProductFee]
    productHeight: ProductDimension
    productHighlights: _list[str]
    productLength: ProductDimension
    productTypes: _list[str]
    productWeight: ProductWeight
    productWidth: ProductDimension
    promotionIds: _list[str]
    propertyName: str
    propertyType: typing.Literal[
        "PROPERTY_TYPE_UNSPECIFIED",
        "APARTMENT",
        "CONDO",
        "LOFT",
        "MULTI_FAMILY_HOME",
        "PENTHOUSE",
        "ROOM",
        "SINGLE_FAMILY_HOME",
        "STUDIO",
        "TOWNHOUSE",
    ]
    questionsAndAnswers: _list[QuestionAndAnswer]
    relatedProducts: _list[RelatedProduct]
    returnPolicyLabel: str
    returns: _list[Returns]
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
    shortTitle: str
    size: str
    sizeSystem: typing.Literal[
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
        typing.Literal[
            "SIZE_TYPE_UNSPECIFIED",
            "REGULAR",
            "PETITE",
            "MATERNITY",
            "BIG",
            "TALL",
            "PLUS",
        ]
    ]
    specialtyHousingType: typing.Literal[
        "SPECIALTY_HOUSING_TYPE_UNSPECIFIED",
        "CORPORATE",
        "LOW_INCOME",
        "MILITARY",
        "SENIOR",
        "SHORT_TERM",
        "STUDENT",
    ]
    structuredDescription: StructuredDescription
    structuredTitle: StructuredTitle
    subscriptionCost: SubscriptionCost
    sustainabilityIncentives: _list[ProductSustainabilityIncentive]
    title: str
    transitTimeLabel: str
    trim: str
    unitArea: UnitArea
    unitPricingBaseMeasure: UnitPricingBaseMeasure
    unitPricingMeasure: UnitPricingMeasure
    utilitiesIncluded: _list[
        typing.Literal[
            "UTILITIES_INCLUDED_UNSPECIFIED",
            "ELECTRICITY",
            "GAS",
            "INTERNET",
            "TRASH",
            "WATER",
        ]
    ]
    variantOptions: _list[VariantOption]
    vehicleAllInPrice: Price
    vehicleExpenses: Price
    vehicleMandatoryInspectionIncluded: bool
    vehicleMsrp: Price
    vehiclePriceType: typing.Literal[
        "VEHICLE_PRICE_TYPE_UNSPECIFIED",
        "ALL_IN_PRICE",
        "DRIVE_AWAY_PRICE",
        "ESTIMATED_DRIVE_AWAY_PRICE",
        "EXCLUDING_GOVERNMENT_CHARGES_PRICE",
        "VEHICLE_BASE_PRICE",
    ]
    videoLinks: _list[str]
    vin: str
    virtualModelLink: str
    warranty: Warranty
    year: str

@typing.type_check_only
class ProductCertification(typing.TypedDict, total=False):
    certificationAuthority: typing.Literal[
        "CERTIFICATION_AUTHORITY_UNSPECIFIED", "ADEME", "BMWK", "EPA", "EC"
    ]
    certificationCode: str
    certificationName: typing.Literal[
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
class ProductDetail(typing.TypedDict, total=False):
    attributeName: str
    attributeValue: str
    sectionName: str

@typing.type_check_only
class ProductDimension(typing.TypedDict, total=False):
    unit: str
    value: float

@typing.type_check_only
class ProductFee(typing.TypedDict, total=False):
    amount: Price
    type: typing.Literal[
        "FEE_TYPE_UNSPECIFIED", "ADMIN_FEE", "APPLICATION_FEE", "SECURITY_DEPOSIT"
    ]

@typing.type_check_only
class ProductInput(typing.TypedDict, total=False):
    base64EncodedName: str
    base64EncodedProduct: str
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
class ProductInstallment(typing.TypedDict, total=False):
    amount: Price
    annualPercentageRate: float
    creditType: typing.Literal["CREDIT_TYPE_UNSPECIFIED", "FINANCE", "LEASE"]
    downpayment: Price
    months: str
    totalAmount: Price

@typing.type_check_only
class ProductMinimumOrderValue(typing.TypedDict, total=False):
    country: str
    price: Price
    service: str
    surface: typing.Literal["SURFACE_UNSPECIFIED", "ONLINE", "LOCAL", "ONLINE_LOCAL"]

@typing.type_check_only
class ProductStatus(typing.TypedDict, total=False):
    creationDate: str
    destinationStatuses: _list[DestinationStatus]
    googleExpirationDate: str
    itemLevelIssues: _list[ItemLevelIssue]
    lastUpdateDate: str

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
class ProductSustainabilityIncentive(typing.TypedDict, total=False):
    amount: Price
    percentage: float
    type: typing.Literal["TYPE_UNSPECIFIED", "EV_TAX_CREDIT", "EV_PRICE_DISCOUNT"]

@typing.type_check_only
class ProductWeight(typing.TypedDict, total=False):
    unit: str
    value: float

@typing.type_check_only
class QuestionAndAnswer(typing.TypedDict, total=False):
    answer: str
    question: str

@typing.type_check_only
class RelatedProduct(typing.TypedDict, total=False):
    id: str
    idType: typing.Literal["ID_TYPE_UNSPECIFIED", "GTIN", "ID"]
    relationshipType: typing.Literal[
        "RELATIONSHIP_TYPE_UNSPECIFIED",
        "PART_OF_SET",
        "REQUIRED_PART",
        "OFTEN_BOUGHT_WITH",
        "SUBSTITUTE",
        "DIFFERENT_BRAND",
        "ACCESSORY",
    ]

@typing.type_check_only
class Returns(typing.TypedDict, total=False):
    countries: _list[str]
    itemConditions: _list[
        typing.Literal[
            "ITEM_CONDITION_UNSPECIFIED", "NEW", "LIKE_NEW", "USED", "DEFECTIVE_ONLY"
        ]
    ]
    methods: _list[
        typing.Literal[
            "RETURN_METHOD_UNSPECIFIED",
            "BY_MAIL",
            "IN_STORE",
            "AT_A_KIOSK",
            "DROP_OFF_LOCATION",
        ]
    ]
    outcomes: _list[
        typing.Literal[
            "RETURN_OUTCOME_UNSPECIFIED", "REFUND", "EXCHANGE", "STORE_CREDIT"
        ]
    ]
    policyUrl: str
    restockingFee: Price
    restockingPercentageFee: float
    shippingFee: Price
    shippingFeeType: typing.Literal[
        "RETURN_SHIPPING_FEE_TYPE_UNSPECIFIED",
        "CUSTOMER_RESPONSIBILITY",
        "DEDUCTED_FROM_REFUND",
    ]
    windowDays: str
    windowType: typing.Literal[
        "RETURN_WINDOW_TYPE_UNSPECIFIED",
        "FINITE_RETURN_WINDOW",
        "NO_RETURNS",
        "LIFETIME",
    ]

@typing.type_check_only
class Shipping(typing.TypedDict, total=False):
    country: str
    handlingCutoffTime: str
    handlingCutoffTimezone: str
    locationGroupName: str
    locationId: str
    loyaltyProgramLabel: str
    loyaltyTierLabel: str
    maxHandlingTime: str
    maxTransitTime: str
    minHandlingTime: str
    minTransitTime: str
    postalCode: str
    price: Price
    region: str
    service: str

@typing.type_check_only
class ShippingBusinessDaysConfig(typing.TypedDict, total=False):
    businessDays: str
    country: str

@typing.type_check_only
class ShippingDimension(typing.TypedDict, total=False):
    unit: str
    value: float

@typing.type_check_only
class ShippingWeight(typing.TypedDict, total=False):
    unit: str
    value: float

@typing.type_check_only
class StructuredDescription(typing.TypedDict, total=False):
    content: str
    digitalSourceType: typing.Literal[
        "DIGITAL_SOURCE_TYPE_UNSPECIFIED", "TRAINED_ALGORITHMIC_MEDIA", "DEFAULT"
    ]

@typing.type_check_only
class StructuredTitle(typing.TypedDict, total=False):
    content: str
    digitalSourceType: typing.Literal[
        "DIGITAL_SOURCE_TYPE_UNSPECIFIED", "TRAINED_ALGORITHMIC_MEDIA", "DEFAULT"
    ]

@typing.type_check_only
class SubscriptionCost(typing.TypedDict, total=False):
    amount: Price
    period: typing.Literal["SUBSCRIPTION_PERIOD_UNSPECIFIED", "MONTH", "YEAR", "WEEK"]
    periodLength: str

@typing.type_check_only
class UnitArea(typing.TypedDict, total=False):
    unit: typing.Literal["UNIT_UNSPECIFIED", "SQM", "SQFT"]
    value: float

@typing.type_check_only
class UnitPricingBaseMeasure(typing.TypedDict, total=False):
    unit: str
    value: str

@typing.type_check_only
class UnitPricingMeasure(typing.TypedDict, total=False):
    unit: str
    value: float

@typing.type_check_only
class VariantOption(typing.TypedDict, total=False):
    name: str
    value: str

@typing.type_check_only
class Warranty(typing.TypedDict, total=False):
    duration: str
    mileage: Mileage
