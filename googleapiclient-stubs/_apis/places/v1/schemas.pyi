import typing

import typing_extensions

_list = list

@typing.type_check_only
class GoogleGeoTypeViewport(typing_extensions.TypedDict, total=False):
    high: GoogleTypeLatLng
    low: GoogleTypeLatLng

@typing.type_check_only
class GoogleMapsPlacesV1AuthorAttribution(typing_extensions.TypedDict, total=False):
    displayName: str
    photoUri: str
    uri: str

@typing.type_check_only
class GoogleMapsPlacesV1Circle(typing_extensions.TypedDict, total=False):
    center: GoogleTypeLatLng
    radius: float

@typing.type_check_only
class GoogleMapsPlacesV1EVChargeOptions(typing_extensions.TypedDict, total=False):
    connectorAggregation: _list[GoogleMapsPlacesV1EVChargeOptionsConnectorAggregation]
    connectorCount: int

@typing.type_check_only
class GoogleMapsPlacesV1EVChargeOptionsConnectorAggregation(
    typing_extensions.TypedDict, total=False
):
    availabilityLastUpdateTime: str
    availableCount: int
    count: int
    maxChargeRateKw: float
    outOfServiceCount: int
    type: typing_extensions.Literal[
        "EV_CONNECTOR_TYPE_UNSPECIFIED",
        "EV_CONNECTOR_TYPE_OTHER",
        "EV_CONNECTOR_TYPE_J1772",
        "EV_CONNECTOR_TYPE_TYPE_2",
        "EV_CONNECTOR_TYPE_CHADEMO",
        "EV_CONNECTOR_TYPE_CCS_COMBO_1",
        "EV_CONNECTOR_TYPE_CCS_COMBO_2",
        "EV_CONNECTOR_TYPE_TESLA",
        "EV_CONNECTOR_TYPE_UNSPECIFIED_GB_T",
        "EV_CONNECTOR_TYPE_UNSPECIFIED_WALL_OUTLET",
    ]

@typing.type_check_only
class GoogleMapsPlacesV1FuelOptions(typing_extensions.TypedDict, total=False):
    fuelPrices: _list[GoogleMapsPlacesV1FuelOptionsFuelPrice]

@typing.type_check_only
class GoogleMapsPlacesV1FuelOptionsFuelPrice(typing_extensions.TypedDict, total=False):
    price: GoogleTypeMoney
    type: typing_extensions.Literal[
        "FUEL_TYPE_UNSPECIFIED",
        "DIESEL",
        "REGULAR_UNLEADED",
        "MIDGRADE",
        "PREMIUM",
        "SP91",
        "SP91_E10",
        "SP92",
        "SP95",
        "SP95_E10",
        "SP98",
        "SP99",
        "SP100",
        "LPG",
        "E80",
        "E85",
        "METHANE",
        "BIO_DIESEL",
        "TRUCK_DIESEL",
    ]
    updateTime: str

@typing.type_check_only
class GoogleMapsPlacesV1Photo(typing_extensions.TypedDict, total=False):
    authorAttributions: _list[GoogleMapsPlacesV1AuthorAttribution]
    heightPx: int
    name: str
    widthPx: int

@typing.type_check_only
class GoogleMapsPlacesV1PhotoMedia(typing_extensions.TypedDict, total=False):
    name: str
    photoUri: str

@typing.type_check_only
class GoogleMapsPlacesV1Place(typing_extensions.TypedDict, total=False):
    accessibilityOptions: GoogleMapsPlacesV1PlaceAccessibilityOptions
    addressComponents: _list[GoogleMapsPlacesV1PlaceAddressComponent]
    adrFormatAddress: str
    allowsDogs: bool
    attributions: _list[GoogleMapsPlacesV1PlaceAttribution]
    businessStatus: typing_extensions.Literal[
        "BUSINESS_STATUS_UNSPECIFIED",
        "OPERATIONAL",
        "CLOSED_TEMPORARILY",
        "CLOSED_PERMANENTLY",
    ]
    curbsidePickup: bool
    currentOpeningHours: GoogleMapsPlacesV1PlaceOpeningHours
    currentSecondaryOpeningHours: _list[GoogleMapsPlacesV1PlaceOpeningHours]
    delivery: bool
    dineIn: bool
    displayName: GoogleTypeLocalizedText
    editorialSummary: GoogleTypeLocalizedText
    evChargeOptions: GoogleMapsPlacesV1EVChargeOptions
    formattedAddress: str
    fuelOptions: GoogleMapsPlacesV1FuelOptions
    goodForChildren: bool
    goodForGroups: bool
    goodForWatchingSports: bool
    googleMapsUri: str
    iconBackgroundColor: str
    iconMaskBaseUri: str
    id: str
    internationalPhoneNumber: str
    liveMusic: bool
    location: GoogleTypeLatLng
    menuForChildren: bool
    name: str
    nationalPhoneNumber: str
    outdoorSeating: bool
    parkingOptions: GoogleMapsPlacesV1PlaceParkingOptions
    paymentOptions: GoogleMapsPlacesV1PlacePaymentOptions
    photos: _list[GoogleMapsPlacesV1Photo]
    plusCode: GoogleMapsPlacesV1PlacePlusCode
    priceLevel: typing_extensions.Literal[
        "PRICE_LEVEL_UNSPECIFIED",
        "PRICE_LEVEL_FREE",
        "PRICE_LEVEL_INEXPENSIVE",
        "PRICE_LEVEL_MODERATE",
        "PRICE_LEVEL_EXPENSIVE",
        "PRICE_LEVEL_VERY_EXPENSIVE",
    ]
    primaryType: str
    primaryTypeDisplayName: GoogleTypeLocalizedText
    rating: float
    regularOpeningHours: GoogleMapsPlacesV1PlaceOpeningHours
    regularSecondaryOpeningHours: _list[GoogleMapsPlacesV1PlaceOpeningHours]
    reservable: bool
    restroom: bool
    reviews: _list[GoogleMapsPlacesV1Review]
    servesBeer: bool
    servesBreakfast: bool
    servesBrunch: bool
    servesCocktails: bool
    servesCoffee: bool
    servesDessert: bool
    servesDinner: bool
    servesLunch: bool
    servesVegetarianFood: bool
    servesWine: bool
    shortFormattedAddress: str
    subDestinations: _list[GoogleMapsPlacesV1PlaceSubDestination]
    takeout: bool
    types: _list[str]
    userRatingCount: int
    utcOffsetMinutes: int
    viewport: GoogleGeoTypeViewport
    websiteUri: str

@typing.type_check_only
class GoogleMapsPlacesV1PlaceAccessibilityOptions(
    typing_extensions.TypedDict, total=False
):
    wheelchairAccessibleEntrance: bool
    wheelchairAccessibleParking: bool
    wheelchairAccessibleRestroom: bool
    wheelchairAccessibleSeating: bool

@typing.type_check_only
class GoogleMapsPlacesV1PlaceAddressComponent(typing_extensions.TypedDict, total=False):
    languageCode: str
    longText: str
    shortText: str
    types: _list[str]

@typing.type_check_only
class GoogleMapsPlacesV1PlaceAttribution(typing_extensions.TypedDict, total=False):
    provider: str
    providerUri: str

@typing.type_check_only
class GoogleMapsPlacesV1PlaceOpeningHours(typing_extensions.TypedDict, total=False):
    openNow: bool
    periods: _list[GoogleMapsPlacesV1PlaceOpeningHoursPeriod]
    secondaryHoursType: typing_extensions.Literal[
        "SECONDARY_HOURS_TYPE_UNSPECIFIED",
        "DRIVE_THROUGH",
        "HAPPY_HOUR",
        "DELIVERY",
        "TAKEOUT",
        "KITCHEN",
        "BREAKFAST",
        "LUNCH",
        "DINNER",
        "BRUNCH",
        "PICKUP",
        "ACCESS",
        "SENIOR_HOURS",
        "ONLINE_SERVICE_HOURS",
    ]
    specialDays: _list[GoogleMapsPlacesV1PlaceOpeningHoursSpecialDay]
    weekdayDescriptions: _list[str]

@typing.type_check_only
class GoogleMapsPlacesV1PlaceOpeningHoursPeriod(
    typing_extensions.TypedDict, total=False
):
    close: GoogleMapsPlacesV1PlaceOpeningHoursPeriodPoint
    open: GoogleMapsPlacesV1PlaceOpeningHoursPeriodPoint

@typing.type_check_only
class GoogleMapsPlacesV1PlaceOpeningHoursPeriodPoint(
    typing_extensions.TypedDict, total=False
):
    date: GoogleTypeDate
    day: int
    hour: int
    minute: int
    truncated: bool

@typing.type_check_only
class GoogleMapsPlacesV1PlaceOpeningHoursSpecialDay(
    typing_extensions.TypedDict, total=False
):
    date: GoogleTypeDate

@typing.type_check_only
class GoogleMapsPlacesV1PlaceParkingOptions(typing_extensions.TypedDict, total=False):
    freeGarageParking: bool
    freeParkingLot: bool
    freeStreetParking: bool
    paidGarageParking: bool
    paidParkingLot: bool
    paidStreetParking: bool
    valetParking: bool

@typing.type_check_only
class GoogleMapsPlacesV1PlacePaymentOptions(typing_extensions.TypedDict, total=False):
    acceptsCashOnly: bool
    acceptsCreditCards: bool
    acceptsDebitCards: bool
    acceptsNfc: bool

@typing.type_check_only
class GoogleMapsPlacesV1PlacePlusCode(typing_extensions.TypedDict, total=False):
    compoundCode: str
    globalCode: str

@typing.type_check_only
class GoogleMapsPlacesV1PlaceSubDestination(typing_extensions.TypedDict, total=False):
    id: str
    name: str

@typing.type_check_only
class GoogleMapsPlacesV1Review(typing_extensions.TypedDict, total=False):
    authorAttribution: GoogleMapsPlacesV1AuthorAttribution
    name: str
    originalText: GoogleTypeLocalizedText
    publishTime: str
    rating: float
    relativePublishTimeDescription: str
    text: GoogleTypeLocalizedText

@typing.type_check_only
class GoogleMapsPlacesV1SearchNearbyRequest(typing_extensions.TypedDict, total=False):
    excludedPrimaryTypes: _list[str]
    excludedTypes: _list[str]
    includedPrimaryTypes: _list[str]
    includedTypes: _list[str]
    languageCode: str
    locationRestriction: GoogleMapsPlacesV1SearchNearbyRequestLocationRestriction
    maxResultCount: int
    rankPreference: typing_extensions.Literal[
        "RANK_PREFERENCE_UNSPECIFIED", "DISTANCE", "POPULARITY"
    ]
    regionCode: str

@typing.type_check_only
class GoogleMapsPlacesV1SearchNearbyRequestLocationRestriction(
    typing_extensions.TypedDict, total=False
):
    circle: GoogleMapsPlacesV1Circle

@typing.type_check_only
class GoogleMapsPlacesV1SearchNearbyResponse(typing_extensions.TypedDict, total=False):
    places: _list[GoogleMapsPlacesV1Place]

@typing.type_check_only
class GoogleMapsPlacesV1SearchTextRequest(typing_extensions.TypedDict, total=False):
    includedType: str
    languageCode: str
    locationBias: GoogleMapsPlacesV1SearchTextRequestLocationBias
    locationRestriction: GoogleMapsPlacesV1SearchTextRequestLocationRestriction
    maxResultCount: int
    minRating: float
    openNow: bool
    priceLevels: _list[str]
    rankPreference: typing_extensions.Literal[
        "RANK_PREFERENCE_UNSPECIFIED", "DISTANCE", "RELEVANCE"
    ]
    regionCode: str
    strictTypeFiltering: bool
    textQuery: str

@typing.type_check_only
class GoogleMapsPlacesV1SearchTextRequestLocationBias(
    typing_extensions.TypedDict, total=False
):
    circle: GoogleMapsPlacesV1Circle
    rectangle: GoogleGeoTypeViewport

@typing.type_check_only
class GoogleMapsPlacesV1SearchTextRequestLocationRestriction(
    typing_extensions.TypedDict, total=False
):
    rectangle: GoogleGeoTypeViewport

@typing.type_check_only
class GoogleMapsPlacesV1SearchTextResponse(typing_extensions.TypedDict, total=False):
    places: _list[GoogleMapsPlacesV1Place]

@typing.type_check_only
class GoogleTypeDate(typing_extensions.TypedDict, total=False):
    day: int
    month: int
    year: int

@typing.type_check_only
class GoogleTypeLatLng(typing_extensions.TypedDict, total=False):
    latitude: float
    longitude: float

@typing.type_check_only
class GoogleTypeLocalizedText(typing_extensions.TypedDict, total=False):
    languageCode: str
    text: str

@typing.type_check_only
class GoogleTypeMoney(typing_extensions.TypedDict, total=False):
    currencyCode: str
    nanos: int
    units: str
