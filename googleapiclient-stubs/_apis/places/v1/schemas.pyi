import typing

_list = list

@typing.type_check_only
class GoogleGeoTypeViewport(typing.TypedDict, total=False):
    high: GoogleTypeLatLng
    low: GoogleTypeLatLng

@typing.type_check_only
class GoogleMapsPlacesV1AddressDescriptor(typing.TypedDict, total=False):
    areas: _list[GoogleMapsPlacesV1AddressDescriptorArea]
    landmarks: _list[GoogleMapsPlacesV1AddressDescriptorLandmark]

@typing.type_check_only
class GoogleMapsPlacesV1AddressDescriptorArea(typing.TypedDict, total=False):
    containment: typing.Literal[
        "CONTAINMENT_UNSPECIFIED", "WITHIN", "OUTSKIRTS", "NEAR"
    ]
    displayName: GoogleTypeLocalizedText
    name: str
    placeId: str

@typing.type_check_only
class GoogleMapsPlacesV1AddressDescriptorLandmark(typing.TypedDict, total=False):
    displayName: GoogleTypeLocalizedText
    name: str
    placeId: str
    spatialRelationship: typing.Literal[
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
class GoogleMapsPlacesV1AuthorAttribution(typing.TypedDict, total=False):
    displayName: str
    photoUri: str
    uri: str

@typing.type_check_only
class GoogleMapsPlacesV1AutocompletePlacesRequest(typing.TypedDict, total=False):
    includeFutureOpeningBusinesses: bool
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
    typing.TypedDict, total=False
):
    circle: GoogleMapsPlacesV1Circle
    rectangle: GoogleGeoTypeViewport

@typing.type_check_only
class GoogleMapsPlacesV1AutocompletePlacesRequestLocationRestriction(
    typing.TypedDict, total=False
):
    circle: GoogleMapsPlacesV1Circle
    rectangle: GoogleGeoTypeViewport

@typing.type_check_only
class GoogleMapsPlacesV1AutocompletePlacesResponse(typing.TypedDict, total=False):
    suggestions: _list[GoogleMapsPlacesV1AutocompletePlacesResponseSuggestion]

@typing.type_check_only
class GoogleMapsPlacesV1AutocompletePlacesResponseSuggestion(
    typing.TypedDict, total=False
):
    placePrediction: (
        GoogleMapsPlacesV1AutocompletePlacesResponseSuggestionPlacePrediction
    )
    queryPrediction: (
        GoogleMapsPlacesV1AutocompletePlacesResponseSuggestionQueryPrediction
    )

@typing.type_check_only
class GoogleMapsPlacesV1AutocompletePlacesResponseSuggestionFormattableText(
    typing.TypedDict, total=False
):
    matches: _list[GoogleMapsPlacesV1AutocompletePlacesResponseSuggestionStringRange]
    text: str

@typing.type_check_only
class GoogleMapsPlacesV1AutocompletePlacesResponseSuggestionPlacePrediction(
    typing.TypedDict, total=False
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
    typing.TypedDict, total=False
):
    structuredFormat: (
        GoogleMapsPlacesV1AutocompletePlacesResponseSuggestionStructuredFormat
    )
    text: GoogleMapsPlacesV1AutocompletePlacesResponseSuggestionFormattableText

@typing.type_check_only
class GoogleMapsPlacesV1AutocompletePlacesResponseSuggestionStringRange(
    typing.TypedDict, total=False
):
    endOffset: int
    startOffset: int

@typing.type_check_only
class GoogleMapsPlacesV1AutocompletePlacesResponseSuggestionStructuredFormat(
    typing.TypedDict, total=False
):
    mainText: GoogleMapsPlacesV1AutocompletePlacesResponseSuggestionFormattableText
    secondaryText: GoogleMapsPlacesV1AutocompletePlacesResponseSuggestionFormattableText

@typing.type_check_only
class GoogleMapsPlacesV1Circle(typing.TypedDict, total=False):
    center: GoogleTypeLatLng
    radius: float

@typing.type_check_only
class GoogleMapsPlacesV1ContentBlock(typing.TypedDict, total=False):
    content: GoogleTypeLocalizedText
    referencedPlaces: _list[str]

@typing.type_check_only
class GoogleMapsPlacesV1ContextualContent(typing.TypedDict, total=False):
    justifications: _list[GoogleMapsPlacesV1ContextualContentJustification]
    photos: _list[GoogleMapsPlacesV1Photo]
    reviews: _list[GoogleMapsPlacesV1Review]

@typing.type_check_only
class GoogleMapsPlacesV1ContextualContentJustification(typing.TypedDict, total=False):
    businessAvailabilityAttributesJustification: GoogleMapsPlacesV1ContextualContentJustificationBusinessAvailabilityAttributesJustification
    reviewJustification: (
        GoogleMapsPlacesV1ContextualContentJustificationReviewJustification
    )

@typing.type_check_only
class GoogleMapsPlacesV1ContextualContentJustificationBusinessAvailabilityAttributesJustification(
    typing.TypedDict, total=False
):
    delivery: bool
    dineIn: bool
    takeout: bool

@typing.type_check_only
class GoogleMapsPlacesV1ContextualContentJustificationReviewJustification(
    typing.TypedDict, total=False
):
    highlightedText: GoogleMapsPlacesV1ContextualContentJustificationReviewJustificationHighlightedText
    review: GoogleMapsPlacesV1Review

@typing.type_check_only
class GoogleMapsPlacesV1ContextualContentJustificationReviewJustificationHighlightedText(
    typing.TypedDict, total=False
):
    highlightedTextRanges: _list[
        GoogleMapsPlacesV1ContextualContentJustificationReviewJustificationHighlightedTextHighlightedTextRange
    ]
    text: str

@typing.type_check_only
class GoogleMapsPlacesV1ContextualContentJustificationReviewJustificationHighlightedTextHighlightedTextRange(
    typing.TypedDict, total=False
):
    endIndex: int
    startIndex: int

@typing.type_check_only
class GoogleMapsPlacesV1EVChargeOptions(typing.TypedDict, total=False):
    connectorAggregation: _list[GoogleMapsPlacesV1EVChargeOptionsConnectorAggregation]
    connectorCount: int

@typing.type_check_only
class GoogleMapsPlacesV1EVChargeOptionsConnectorAggregation(
    typing.TypedDict, total=False
):
    availabilityLastUpdateTime: str
    availableCount: int
    count: int
    maxChargeRateKw: float
    outOfServiceCount: int
    type: typing.Literal[
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
        "EV_CONNECTOR_TYPE_NACS",
    ]

@typing.type_check_only
class GoogleMapsPlacesV1FuelOptions(typing.TypedDict, total=False):
    fuelPrices: _list[GoogleMapsPlacesV1FuelOptionsFuelPrice]

@typing.type_check_only
class GoogleMapsPlacesV1FuelOptionsFuelPrice(typing.TypedDict, total=False):
    price: GoogleTypeMoney
    type: typing.Literal[
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
class GoogleMapsPlacesV1Photo(typing.TypedDict, total=False):
    authorAttributions: _list[GoogleMapsPlacesV1AuthorAttribution]
    flagContentUri: str
    googleMapsUri: str
    heightPx: int
    name: str
    widthPx: int

@typing.type_check_only
class GoogleMapsPlacesV1PhotoMedia(typing.TypedDict, total=False):
    name: str
    photoUri: str

@typing.type_check_only
class GoogleMapsPlacesV1Place(typing.TypedDict, total=False):
    accessibilityOptions: GoogleMapsPlacesV1PlaceAccessibilityOptions
    addressComponents: _list[GoogleMapsPlacesV1PlaceAddressComponent]
    addressDescriptor: GoogleMapsPlacesV1AddressDescriptor
    adrFormatAddress: str
    allowsDogs: bool
    attributions: _list[GoogleMapsPlacesV1PlaceAttribution]
    businessStatus: typing.Literal[
        "BUSINESS_STATUS_UNSPECIFIED",
        "OPERATIONAL",
        "CLOSED_TEMPORARILY",
        "CLOSED_PERMANENTLY",
        "FUTURE_OPENING",
    ]
    consumerAlert: GoogleMapsPlacesV1PlaceConsumerAlert
    containingPlaces: _list[GoogleMapsPlacesV1PlaceContainingPlace]
    curbsidePickup: bool
    currentOpeningHours: GoogleMapsPlacesV1PlaceOpeningHours
    currentSecondaryOpeningHours: _list[GoogleMapsPlacesV1PlaceOpeningHours]
    delivery: bool
    dineIn: bool
    displayName: GoogleTypeLocalizedText
    editorialSummary: GoogleTypeLocalizedText
    entrances: _list[GoogleMapsPlacesV1PlaceEntrance]
    evChargeAmenitySummary: GoogleMapsPlacesV1PlaceEvChargeAmenitySummary
    evChargeOptions: GoogleMapsPlacesV1EVChargeOptions
    formattedAddress: str
    fuelOptions: GoogleMapsPlacesV1FuelOptions
    generativeSummary: GoogleMapsPlacesV1PlaceGenerativeSummary
    goodForChildren: bool
    goodForGroups: bool
    goodForWatchingSports: bool
    googleMapsLinks: GoogleMapsPlacesV1PlaceGoogleMapsLinks
    googleMapsTypeLabel: GoogleTypeLocalizedText
    googleMapsUri: str
    iconBackgroundColor: str
    iconMaskBaseUri: str
    id: str
    internationalPhoneNumber: str
    liveMusic: bool
    location: GoogleTypeLatLng
    menuForChildren: bool
    movedPlace: str
    movedPlaceId: str
    name: str
    nationalPhoneNumber: str
    navigationPoints: _list[GoogleMapsPlacesV1PlaceNavigationPoint]
    neighborhoodSummary: GoogleMapsPlacesV1PlaceNeighborhoodSummary
    openingDate: GoogleTypeDate
    outdoorSeating: bool
    parkingOptions: GoogleMapsPlacesV1PlaceParkingOptions
    paymentOptions: GoogleMapsPlacesV1PlacePaymentOptions
    photos: _list[GoogleMapsPlacesV1Photo]
    plusCode: GoogleMapsPlacesV1PlacePlusCode
    postalAddress: GoogleTypePostalAddress
    priceLevel: typing.Literal[
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
    reviewSummary: GoogleMapsPlacesV1PlaceReviewSummary
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
    timeZone: GoogleTypeTimeZone
    transitStation: GoogleMapsPlacesV1TransitStation
    types: _list[str]
    userRatingCount: int
    utcOffsetMinutes: int
    viewport: GoogleGeoTypeViewport
    websiteUri: str

@typing.type_check_only
class GoogleMapsPlacesV1PlaceAccessibilityOptions(typing.TypedDict, total=False):
    wheelchairAccessibleEntrance: bool
    wheelchairAccessibleParking: bool
    wheelchairAccessibleRestroom: bool
    wheelchairAccessibleSeating: bool

@typing.type_check_only
class GoogleMapsPlacesV1PlaceAddressComponent(typing.TypedDict, total=False):
    languageCode: str
    longText: str
    shortText: str
    types: _list[str]

@typing.type_check_only
class GoogleMapsPlacesV1PlaceAttribution(typing.TypedDict, total=False):
    provider: str
    providerUri: str

@typing.type_check_only
class GoogleMapsPlacesV1PlaceConsumerAlert(typing.TypedDict, total=False):
    details: GoogleMapsPlacesV1PlaceConsumerAlertDetails
    languageCode: str
    overview: str

@typing.type_check_only
class GoogleMapsPlacesV1PlaceConsumerAlertDetails(typing.TypedDict, total=False):
    aboutLink: GoogleMapsPlacesV1PlaceConsumerAlertDetailsLink
    description: str
    title: str

@typing.type_check_only
class GoogleMapsPlacesV1PlaceConsumerAlertDetailsLink(typing.TypedDict, total=False):
    title: str
    uri: str

@typing.type_check_only
class GoogleMapsPlacesV1PlaceContainingPlace(typing.TypedDict, total=False):
    id: str
    name: str

@typing.type_check_only
class GoogleMapsPlacesV1PlaceEntrance(typing.TypedDict, total=False):
    location: GoogleTypeLatLng
    tags: _list[typing.Literal["TAG_UNSPECIFIED", "PREFERRED"]]

@typing.type_check_only
class GoogleMapsPlacesV1PlaceEvChargeAmenitySummary(typing.TypedDict, total=False):
    coffee: GoogleMapsPlacesV1ContentBlock
    disclosureText: GoogleTypeLocalizedText
    flagContentUri: str
    overview: GoogleMapsPlacesV1ContentBlock
    restaurant: GoogleMapsPlacesV1ContentBlock
    store: GoogleMapsPlacesV1ContentBlock

@typing.type_check_only
class GoogleMapsPlacesV1PlaceGenerativeSummary(typing.TypedDict, total=False):
    disclosureText: GoogleTypeLocalizedText
    overview: GoogleTypeLocalizedText
    overviewFlagContentUri: str

@typing.type_check_only
class GoogleMapsPlacesV1PlaceGoogleMapsLinks(typing.TypedDict, total=False):
    directionsUri: str
    photosUri: str
    placeUri: str
    reviewsUri: str
    writeAReviewUri: str

@typing.type_check_only
class GoogleMapsPlacesV1PlaceNavigationPoint(typing.TypedDict, total=False):
    displayName: GoogleTypeLocalizedText
    location: GoogleTypeLatLng
    navigationPointToken: str
    travelModes: _list[typing.Literal["TRAVEL_MODE_UNSPECIFIED", "DRIVE", "WALK"]]
    usages: _list[typing.Literal["USAGE_UNSPECIFIED", "DROPOFF", "PICKUP", "PARKING"]]

@typing.type_check_only
class GoogleMapsPlacesV1PlaceNeighborhoodSummary(typing.TypedDict, total=False):
    description: GoogleMapsPlacesV1ContentBlock
    disclosureText: GoogleTypeLocalizedText
    flagContentUri: str
    overview: GoogleMapsPlacesV1ContentBlock

@typing.type_check_only
class GoogleMapsPlacesV1PlaceOpeningHours(typing.TypedDict, total=False):
    nextCloseTime: str
    nextOpenTime: str
    openNow: bool
    periods: _list[GoogleMapsPlacesV1PlaceOpeningHoursPeriod]
    secondaryHoursType: typing.Literal[
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
class GoogleMapsPlacesV1PlaceOpeningHoursPeriod(typing.TypedDict, total=False):
    close: GoogleMapsPlacesV1PlaceOpeningHoursPeriodPoint
    open: GoogleMapsPlacesV1PlaceOpeningHoursPeriodPoint

@typing.type_check_only
class GoogleMapsPlacesV1PlaceOpeningHoursPeriodPoint(typing.TypedDict, total=False):
    date: GoogleTypeDate
    day: int
    hour: int
    minute: int
    truncated: bool

@typing.type_check_only
class GoogleMapsPlacesV1PlaceOpeningHoursSpecialDay(typing.TypedDict, total=False):
    date: GoogleTypeDate

@typing.type_check_only
class GoogleMapsPlacesV1PlaceParkingOptions(typing.TypedDict, total=False):
    freeGarageParking: bool
    freeParkingLot: bool
    freeStreetParking: bool
    paidGarageParking: bool
    paidParkingLot: bool
    paidStreetParking: bool
    valetParking: bool

@typing.type_check_only
class GoogleMapsPlacesV1PlacePaymentOptions(typing.TypedDict, total=False):
    acceptsCashOnly: bool
    acceptsCreditCards: bool
    acceptsDebitCards: bool
    acceptsNfc: bool

@typing.type_check_only
class GoogleMapsPlacesV1PlacePlusCode(typing.TypedDict, total=False):
    compoundCode: str
    globalCode: str

@typing.type_check_only
class GoogleMapsPlacesV1PlaceReviewSummary(typing.TypedDict, total=False):
    disclosureText: GoogleTypeLocalizedText
    flagContentUri: str
    reviewsUri: str
    text: GoogleTypeLocalizedText

@typing.type_check_only
class GoogleMapsPlacesV1PlaceSubDestination(typing.TypedDict, total=False):
    id: str
    name: str

@typing.type_check_only
class GoogleMapsPlacesV1Polyline(typing.TypedDict, total=False):
    encodedPolyline: str

@typing.type_check_only
class GoogleMapsPlacesV1PriceRange(typing.TypedDict, total=False):
    endPrice: GoogleTypeMoney
    startPrice: GoogleTypeMoney

@typing.type_check_only
class GoogleMapsPlacesV1Review(typing.TypedDict, total=False):
    authorAttribution: GoogleMapsPlacesV1AuthorAttribution
    flagContentUri: str
    googleMapsUri: str
    name: str
    originalText: GoogleTypeLocalizedText
    publishTime: str
    rating: float
    relativePublishTimeDescription: str
    text: GoogleTypeLocalizedText
    visitDate: GoogleTypeDate

@typing.type_check_only
class GoogleMapsPlacesV1RouteModifiers(typing.TypedDict, total=False):
    avoidFerries: bool
    avoidHighways: bool
    avoidIndoor: bool
    avoidTolls: bool

@typing.type_check_only
class GoogleMapsPlacesV1RoutingParameters(typing.TypedDict, total=False):
    origin: GoogleTypeLatLng
    routeModifiers: GoogleMapsPlacesV1RouteModifiers
    routingPreference: typing.Literal[
        "ROUTING_PREFERENCE_UNSPECIFIED",
        "TRAFFIC_UNAWARE",
        "TRAFFIC_AWARE",
        "TRAFFIC_AWARE_OPTIMAL",
    ]
    travelMode: typing.Literal[
        "TRAVEL_MODE_UNSPECIFIED", "DRIVE", "BICYCLE", "WALK", "TWO_WHEELER"
    ]

@typing.type_check_only
class GoogleMapsPlacesV1RoutingSummary(typing.TypedDict, total=False):
    directionsUri: str
    legs: _list[GoogleMapsPlacesV1RoutingSummaryLeg]

@typing.type_check_only
class GoogleMapsPlacesV1RoutingSummaryLeg(typing.TypedDict, total=False):
    distanceMeters: int
    duration: str

@typing.type_check_only
class GoogleMapsPlacesV1SearchNearbyRequest(typing.TypedDict, total=False):
    excludedPrimaryTypes: _list[str]
    excludedTypes: _list[str]
    includeFutureOpeningBusinesses: bool
    includedPrimaryTypes: _list[str]
    includedTypes: _list[str]
    languageCode: str
    locationRestriction: GoogleMapsPlacesV1SearchNearbyRequestLocationRestriction
    maxResultCount: int
    rankPreference: typing.Literal[
        "RANK_PREFERENCE_UNSPECIFIED", "DISTANCE", "POPULARITY"
    ]
    regionCode: str
    routingParameters: GoogleMapsPlacesV1RoutingParameters

@typing.type_check_only
class GoogleMapsPlacesV1SearchNearbyRequestLocationRestriction(
    typing.TypedDict, total=False
):
    circle: GoogleMapsPlacesV1Circle

@typing.type_check_only
class GoogleMapsPlacesV1SearchNearbyResponse(typing.TypedDict, total=False):
    places: _list[GoogleMapsPlacesV1Place]
    routingSummaries: _list[GoogleMapsPlacesV1RoutingSummary]

@typing.type_check_only
class GoogleMapsPlacesV1SearchTextRequest(typing.TypedDict, total=False):
    evOptions: GoogleMapsPlacesV1SearchTextRequestEVOptions
    includeFutureOpeningBusinesses: bool
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
        typing.Literal[
            "PRICE_LEVEL_UNSPECIFIED",
            "PRICE_LEVEL_FREE",
            "PRICE_LEVEL_INEXPENSIVE",
            "PRICE_LEVEL_MODERATE",
            "PRICE_LEVEL_EXPENSIVE",
            "PRICE_LEVEL_VERY_EXPENSIVE",
        ]
    ]
    rankPreference: typing.Literal[
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
class GoogleMapsPlacesV1SearchTextRequestEVOptions(typing.TypedDict, total=False):
    connectorTypes: _list[
        typing.Literal[
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
            "EV_CONNECTOR_TYPE_NACS",
        ]
    ]
    minimumChargingRateKw: float

@typing.type_check_only
class GoogleMapsPlacesV1SearchTextRequestLocationBias(typing.TypedDict, total=False):
    circle: GoogleMapsPlacesV1Circle
    rectangle: GoogleGeoTypeViewport

@typing.type_check_only
class GoogleMapsPlacesV1SearchTextRequestLocationRestriction(
    typing.TypedDict, total=False
):
    rectangle: GoogleGeoTypeViewport

@typing.type_check_only
class GoogleMapsPlacesV1SearchTextRequestSearchAlongRouteParameters(
    typing.TypedDict, total=False
):
    polyline: GoogleMapsPlacesV1Polyline

@typing.type_check_only
class GoogleMapsPlacesV1SearchTextResponse(typing.TypedDict, total=False):
    contextualContents: _list[GoogleMapsPlacesV1ContextualContent]
    nextPageToken: str
    places: _list[GoogleMapsPlacesV1Place]
    routingSummaries: _list[GoogleMapsPlacesV1RoutingSummary]
    searchUri: str

@typing.type_check_only
class GoogleMapsPlacesV1TransitAgency(typing.TypedDict, total=False):
    displayName: GoogleTypeLocalizedText
    fareUrl: str
    icon: GoogleMapsPlacesV1TransitIcon
    lines: _list[GoogleMapsPlacesV1TransitLine]
    url: str

@typing.type_check_only
class GoogleMapsPlacesV1TransitIcon(typing.TypedDict, total=False):
    nameIncluded: bool
    url: str

@typing.type_check_only
class GoogleMapsPlacesV1TransitLine(typing.TypedDict, total=False):
    backgroundColor: str
    displayName: GoogleTypeLocalizedText
    icon: GoogleMapsPlacesV1TransitIcon
    id: str
    shortDisplayName: GoogleTypeLocalizedText
    textColor: str
    url: str
    vehicleIcon: GoogleMapsPlacesV1TransitIcon
    vehicleType: typing.Literal[
        "VEHICLE_TYPE_UNSPECIFIED",
        "RAIL",
        "METRO_RAIL",
        "SUBWAY",
        "TRAM",
        "MONORAIL",
        "HEAVY_RAIL",
        "COMMUTER_TRAIN",
        "HIGH_SPEED_TRAIN",
        "LONG_DISTANCE_TRAIN",
        "BUS",
        "INTERCITY_BUS",
        "TROLLEYBUS",
        "SHARE_TAXI",
        "COACH",
        "FERRY",
        "CABLE_CAR",
        "GONDOLA_LIFT",
        "FUNICULAR",
        "SPECIAL",
        "HORSE_CARRIAGE",
        "AIRPLANE",
    ]

@typing.type_check_only
class GoogleMapsPlacesV1TransitStation(typing.TypedDict, total=False):
    agencies: _list[GoogleMapsPlacesV1TransitAgency]
    displayName: GoogleTypeLocalizedText
    stops: _list[GoogleMapsPlacesV1TransitStop]

@typing.type_check_only
class GoogleMapsPlacesV1TransitStop(typing.TypedDict, total=False):
    displayName: GoogleTypeLocalizedText
    id: str
    location: GoogleTypeLatLng
    platformCode: GoogleTypeLocalizedText
    signageText: GoogleTypeLocalizedText
    stopCode: GoogleTypeLocalizedText
    wheelchairAccessibleEntrance: bool

@typing.type_check_only
class GoogleTypeDate(typing.TypedDict, total=False):
    day: int
    month: int
    year: int

@typing.type_check_only
class GoogleTypeLatLng(typing.TypedDict, total=False):
    latitude: float
    longitude: float

@typing.type_check_only
class GoogleTypeLocalizedText(typing.TypedDict, total=False):
    languageCode: str
    text: str

@typing.type_check_only
class GoogleTypeMoney(typing.TypedDict, total=False):
    currencyCode: str
    nanos: int
    units: str

@typing.type_check_only
class GoogleTypePostalAddress(typing.TypedDict, total=False):
    addressLines: _list[str]
    administrativeArea: str
    languageCode: str
    locality: str
    organization: str
    postalCode: str
    recipients: _list[str]
    regionCode: str
    revision: int
    sortingCode: str
    sublocality: str

@typing.type_check_only
class GoogleTypeTimeZone(typing.TypedDict, total=False):
    id: str
    version: str
