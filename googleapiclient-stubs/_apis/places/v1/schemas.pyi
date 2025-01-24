import typing

import typing_extensions

_list = list

@typing.type_check_only
class GoogleGeoTypeViewport(typing_extensions.TypedDict, total=False):
    high: GoogleTypeLatLng
    low: GoogleTypeLatLng

@typing.type_check_only
class GoogleMapsPlacesV1AddressDescriptor(typing_extensions.TypedDict, total=False):
    areas: _list[GoogleMapsPlacesV1AddressDescriptorArea]
    landmarks: _list[GoogleMapsPlacesV1AddressDescriptorLandmark]

@typing.type_check_only
class GoogleMapsPlacesV1AddressDescriptorArea(typing_extensions.TypedDict, total=False):
    containment: typing_extensions.Literal[
        "CONTAINMENT_UNSPECIFIED", "WITHIN", "OUTSKIRTS", "NEAR"
    ]
    displayName: GoogleTypeLocalizedText
    name: str
    placeId: str

@typing.type_check_only
class GoogleMapsPlacesV1AddressDescriptorLandmark(
    typing_extensions.TypedDict, total=False
):
    displayName: GoogleTypeLocalizedText
    name: str
    placeId: str
    spatialRelationship: typing_extensions.Literal[
        "NEAR",
        "WITHIN",
        "BESIDE",
        "ACROSS_THE_ROAD",
        "DOWN_THE_ROAD",
        "AROUND_THE_CORNER",
        "BEHIND",
    ]
    straightLineDistanceMeters: float
    travelDistanceMeters: float
    types: _list[str]

@typing.type_check_only
class GoogleMapsPlacesV1AuthorAttribution(typing_extensions.TypedDict, total=False):
    displayName: str
    photoUri: str
    uri: str

@typing.type_check_only
class GoogleMapsPlacesV1AutocompletePlacesRequest(
    typing_extensions.TypedDict, total=False
):
    includePureServiceAreaBusinesses: bool
    includeQueryPredictions: bool
    includedPrimaryTypes: _list[str]
    includedRegionCodes: _list[str]
    input: str
    inputOffset: int
    languageCode: str
    locationBias: GoogleMapsPlacesV1AutocompletePlacesRequestLocationBias
    locationRestriction: GoogleMapsPlacesV1AutocompletePlacesRequestLocationRestriction
    origin: GoogleTypeLatLng
    regionCode: str
    sessionToken: str

@typing.type_check_only
class GoogleMapsPlacesV1AutocompletePlacesRequestLocationBias(
    typing_extensions.TypedDict, total=False
):
    circle: GoogleMapsPlacesV1Circle
    rectangle: GoogleGeoTypeViewport

@typing.type_check_only
class GoogleMapsPlacesV1AutocompletePlacesRequestLocationRestriction(
    typing_extensions.TypedDict, total=False
):
    circle: GoogleMapsPlacesV1Circle
    rectangle: GoogleGeoTypeViewport

@typing.type_check_only
class GoogleMapsPlacesV1AutocompletePlacesResponse(
    typing_extensions.TypedDict, total=False
):
    suggestions: _list[GoogleMapsPlacesV1AutocompletePlacesResponseSuggestion]

@typing.type_check_only
class GoogleMapsPlacesV1AutocompletePlacesResponseSuggestion(
    typing_extensions.TypedDict, total=False
):
    placePrediction: (
        GoogleMapsPlacesV1AutocompletePlacesResponseSuggestionPlacePrediction
    )
    queryPrediction: (
        GoogleMapsPlacesV1AutocompletePlacesResponseSuggestionQueryPrediction
    )

@typing.type_check_only
class GoogleMapsPlacesV1AutocompletePlacesResponseSuggestionFormattableText(
    typing_extensions.TypedDict, total=False
):
    matches: _list[GoogleMapsPlacesV1AutocompletePlacesResponseSuggestionStringRange]
    text: str

@typing.type_check_only
class GoogleMapsPlacesV1AutocompletePlacesResponseSuggestionPlacePrediction(
    typing_extensions.TypedDict, total=False
):
    distanceMeters: int
    place: str
    placeId: str
    structuredFormat: (
        GoogleMapsPlacesV1AutocompletePlacesResponseSuggestionStructuredFormat
    )
    text: GoogleMapsPlacesV1AutocompletePlacesResponseSuggestionFormattableText
    types: _list[str]

@typing.type_check_only
class GoogleMapsPlacesV1AutocompletePlacesResponseSuggestionQueryPrediction(
    typing_extensions.TypedDict, total=False
):
    structuredFormat: (
        GoogleMapsPlacesV1AutocompletePlacesResponseSuggestionStructuredFormat
    )
    text: GoogleMapsPlacesV1AutocompletePlacesResponseSuggestionFormattableText

@typing.type_check_only
class GoogleMapsPlacesV1AutocompletePlacesResponseSuggestionStringRange(
    typing_extensions.TypedDict, total=False
):
    endOffset: int
    startOffset: int

@typing.type_check_only
class GoogleMapsPlacesV1AutocompletePlacesResponseSuggestionStructuredFormat(
    typing_extensions.TypedDict, total=False
):
    mainText: GoogleMapsPlacesV1AutocompletePlacesResponseSuggestionFormattableText
    secondaryText: GoogleMapsPlacesV1AutocompletePlacesResponseSuggestionFormattableText

@typing.type_check_only
class GoogleMapsPlacesV1Circle(typing_extensions.TypedDict, total=False):
    center: GoogleTypeLatLng
    radius: float

@typing.type_check_only
class GoogleMapsPlacesV1ContentBlock(typing_extensions.TypedDict, total=False):
    content: GoogleTypeLocalizedText
    references: GoogleMapsPlacesV1References
    topic: str

@typing.type_check_only
class GoogleMapsPlacesV1ContextualContent(typing_extensions.TypedDict, total=False):
    justifications: _list[GoogleMapsPlacesV1ContextualContentJustification]
    photos: _list[GoogleMapsPlacesV1Photo]
    reviews: _list[GoogleMapsPlacesV1Review]

@typing.type_check_only
class GoogleMapsPlacesV1ContextualContentJustification(
    typing_extensions.TypedDict, total=False
):
    businessAvailabilityAttributesJustification: GoogleMapsPlacesV1ContextualContentJustificationBusinessAvailabilityAttributesJustification
    reviewJustification: (
        GoogleMapsPlacesV1ContextualContentJustificationReviewJustification
    )

@typing.type_check_only
class GoogleMapsPlacesV1ContextualContentJustificationBusinessAvailabilityAttributesJustification(
    typing_extensions.TypedDict, total=False
):
    delivery: bool
    dineIn: bool
    takeout: bool

@typing.type_check_only
class GoogleMapsPlacesV1ContextualContentJustificationReviewJustification(
    typing_extensions.TypedDict, total=False
):
    highlightedText: GoogleMapsPlacesV1ContextualContentJustificationReviewJustificationHighlightedText
    review: GoogleMapsPlacesV1Review

@typing.type_check_only
class GoogleMapsPlacesV1ContextualContentJustificationReviewJustificationHighlightedText(
    typing_extensions.TypedDict, total=False
):
    highlightedTextRanges: _list[
        GoogleMapsPlacesV1ContextualContentJustificationReviewJustificationHighlightedTextHighlightedTextRange
    ]
    text: str

@typing.type_check_only
class GoogleMapsPlacesV1ContextualContentJustificationReviewJustificationHighlightedTextHighlightedTextRange(
    typing_extensions.TypedDict, total=False
):
    endIndex: int
    startIndex: int

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
        "DIESEL_PLUS",
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
        "E100",
        "METHANE",
        "BIO_DIESEL",
        "TRUCK_DIESEL",
    ]
    updateTime: str

@typing.type_check_only
class GoogleMapsPlacesV1Photo(typing_extensions.TypedDict, total=False):
    authorAttributions: _list[GoogleMapsPlacesV1AuthorAttribution]
    flagContentUri: str
    googleMapsUri: str
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
    addressDescriptor: GoogleMapsPlacesV1AddressDescriptor
    adrFormatAddress: str
    allowsDogs: bool
    areaSummary: GoogleMapsPlacesV1PlaceAreaSummary
    attributions: _list[GoogleMapsPlacesV1PlaceAttribution]
    businessStatus: typing_extensions.Literal[
        "BUSINESS_STATUS_UNSPECIFIED",
        "OPERATIONAL",
        "CLOSED_TEMPORARILY",
        "CLOSED_PERMANENTLY",
    ]
    containingPlaces: _list[GoogleMapsPlacesV1PlaceContainingPlace]
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
    generativeSummary: GoogleMapsPlacesV1PlaceGenerativeSummary
    goodForChildren: bool
    goodForGroups: bool
    goodForWatchingSports: bool
    googleMapsLinks: GoogleMapsPlacesV1PlaceGoogleMapsLinks
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
    priceRange: GoogleMapsPlacesV1PriceRange
    primaryType: str
    primaryTypeDisplayName: GoogleTypeLocalizedText
    pureServiceAreaBusiness: bool
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
class GoogleMapsPlacesV1PlaceAreaSummary(typing_extensions.TypedDict, total=False):
    contentBlocks: _list[GoogleMapsPlacesV1ContentBlock]
    flagContentUri: str

@typing.type_check_only
class GoogleMapsPlacesV1PlaceAttribution(typing_extensions.TypedDict, total=False):
    provider: str
    providerUri: str

@typing.type_check_only
class GoogleMapsPlacesV1PlaceContainingPlace(typing_extensions.TypedDict, total=False):
    id: str
    name: str

@typing.type_check_only
class GoogleMapsPlacesV1PlaceGenerativeSummary(
    typing_extensions.TypedDict, total=False
):
    description: GoogleTypeLocalizedText
    descriptionFlagContentUri: str
    overview: GoogleTypeLocalizedText
    overviewFlagContentUri: str
    references: GoogleMapsPlacesV1References

@typing.type_check_only
class GoogleMapsPlacesV1PlaceGoogleMapsLinks(typing_extensions.TypedDict, total=False):
    directionsUri: str
    photosUri: str
    placeUri: str
    reviewsUri: str
    writeAReviewUri: str

@typing.type_check_only
class GoogleMapsPlacesV1PlaceOpeningHours(typing_extensions.TypedDict, total=False):
    nextCloseTime: str
    nextOpenTime: str
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
class GoogleMapsPlacesV1Polyline(typing_extensions.TypedDict, total=False):
    encodedPolyline: str

@typing.type_check_only
class GoogleMapsPlacesV1PriceRange(typing_extensions.TypedDict, total=False):
    endPrice: GoogleTypeMoney
    startPrice: GoogleTypeMoney

@typing.type_check_only
class GoogleMapsPlacesV1References(typing_extensions.TypedDict, total=False):
    places: _list[str]
    reviews: _list[GoogleMapsPlacesV1Review]

@typing.type_check_only
class GoogleMapsPlacesV1Review(typing_extensions.TypedDict, total=False):
    authorAttribution: GoogleMapsPlacesV1AuthorAttribution
    flagContentUri: str
    googleMapsUri: str
    name: str
    originalText: GoogleTypeLocalizedText
    publishTime: str
    rating: float
    relativePublishTimeDescription: str
    text: GoogleTypeLocalizedText

@typing.type_check_only
class GoogleMapsPlacesV1RouteModifiers(typing_extensions.TypedDict, total=False):
    avoidFerries: bool
    avoidHighways: bool
    avoidIndoor: bool
    avoidTolls: bool

@typing.type_check_only
class GoogleMapsPlacesV1RoutingParameters(typing_extensions.TypedDict, total=False):
    origin: GoogleTypeLatLng
    routeModifiers: GoogleMapsPlacesV1RouteModifiers
    routingPreference: typing_extensions.Literal[
        "ROUTING_PREFERENCE_UNSPECIFIED",
        "TRAFFIC_UNAWARE",
        "TRAFFIC_AWARE",
        "TRAFFIC_AWARE_OPTIMAL",
    ]
    travelMode: typing_extensions.Literal[
        "TRAVEL_MODE_UNSPECIFIED", "DRIVE", "BICYCLE", "WALK", "TWO_WHEELER"
    ]

@typing.type_check_only
class GoogleMapsPlacesV1RoutingSummary(typing_extensions.TypedDict, total=False):
    directionsUri: str
    legs: _list[GoogleMapsPlacesV1RoutingSummaryLeg]

@typing.type_check_only
class GoogleMapsPlacesV1RoutingSummaryLeg(typing_extensions.TypedDict, total=False):
    distanceMeters: int
    duration: str

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
    routingParameters: GoogleMapsPlacesV1RoutingParameters

@typing.type_check_only
class GoogleMapsPlacesV1SearchNearbyRequestLocationRestriction(
    typing_extensions.TypedDict, total=False
):
    circle: GoogleMapsPlacesV1Circle

@typing.type_check_only
class GoogleMapsPlacesV1SearchNearbyResponse(typing_extensions.TypedDict, total=False):
    places: _list[GoogleMapsPlacesV1Place]
    routingSummaries: _list[GoogleMapsPlacesV1RoutingSummary]

@typing.type_check_only
class GoogleMapsPlacesV1SearchTextRequest(typing_extensions.TypedDict, total=False):
    evOptions: GoogleMapsPlacesV1SearchTextRequestEVOptions
    includePureServiceAreaBusinesses: bool
    includedType: str
    languageCode: str
    locationBias: GoogleMapsPlacesV1SearchTextRequestLocationBias
    locationRestriction: GoogleMapsPlacesV1SearchTextRequestLocationRestriction
    maxResultCount: int
    minRating: float
    openNow: bool
    pageSize: int
    pageToken: str
    priceLevels: _list[
        typing_extensions.Literal[
            "PRICE_LEVEL_UNSPECIFIED",
            "PRICE_LEVEL_FREE",
            "PRICE_LEVEL_INEXPENSIVE",
            "PRICE_LEVEL_MODERATE",
            "PRICE_LEVEL_EXPENSIVE",
            "PRICE_LEVEL_VERY_EXPENSIVE",
        ]
    ]
    rankPreference: typing_extensions.Literal[
        "RANK_PREFERENCE_UNSPECIFIED", "DISTANCE", "RELEVANCE"
    ]
    regionCode: str
    routingParameters: GoogleMapsPlacesV1RoutingParameters
    searchAlongRouteParameters: (
        GoogleMapsPlacesV1SearchTextRequestSearchAlongRouteParameters
    )
    strictTypeFiltering: bool
    textQuery: str

@typing.type_check_only
class GoogleMapsPlacesV1SearchTextRequestEVOptions(
    typing_extensions.TypedDict, total=False
):
    connectorTypes: _list[
        typing_extensions.Literal[
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
    ]
    minimumChargingRateKw: float

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
class GoogleMapsPlacesV1SearchTextRequestSearchAlongRouteParameters(
    typing_extensions.TypedDict, total=False
):
    polyline: GoogleMapsPlacesV1Polyline

@typing.type_check_only
class GoogleMapsPlacesV1SearchTextResponse(typing_extensions.TypedDict, total=False):
    contextualContents: _list[GoogleMapsPlacesV1ContextualContent]
    nextPageToken: str
    places: _list[GoogleMapsPlacesV1Place]
    routingSummaries: _list[GoogleMapsPlacesV1RoutingSummary]
    searchUri: str

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
