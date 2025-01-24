import typing

import typing_extensions

_list = list

@typing.type_check_only
class ActivationOptions(typing_extensions.TypedDict, total=False):
    activationUrl: str
    allowReactivation: bool

@typing.type_check_only
class ActivationStatus(typing_extensions.TypedDict, total=False):
    state: typing_extensions.Literal[
        "UNKNOWN_STATE", "NOT_ACTIVATED", "not_activated", "ACTIVATED", "activated"
    ]

@typing.type_check_only
class AddMessageRequest(typing_extensions.TypedDict, total=False):
    message: Message

@typing.type_check_only
class AirportInfo(typing_extensions.TypedDict, total=False):
    airportIataCode: str
    airportNameOverride: LocalizedString
    gate: str
    kind: str
    terminal: str

@typing.type_check_only
class AppLinkData(typing_extensions.TypedDict, total=False):
    androidAppLinkInfo: AppLinkDataAppLinkInfo
    displayText: LocalizedString
    iosAppLinkInfo: AppLinkDataAppLinkInfo
    webAppLinkInfo: AppLinkDataAppLinkInfo

@typing.type_check_only
class AppLinkDataAppLinkInfo(typing_extensions.TypedDict, total=False):
    appLogoImage: Image
    appTarget: AppLinkDataAppLinkInfoAppTarget
    description: LocalizedString
    title: LocalizedString

@typing.type_check_only
class AppLinkDataAppLinkInfoAppTarget(typing_extensions.TypedDict, total=False):
    packageName: str
    targetUri: Uri

@typing.type_check_only
class AuthenticationKey(typing_extensions.TypedDict, total=False):
    id: int
    publicKeyPem: str

@typing.type_check_only
class Barcode(typing_extensions.TypedDict, total=False):
    alternateText: str
    kind: str
    renderEncoding: typing_extensions.Literal["RENDER_ENCODING_UNSPECIFIED", "UTF_8"]
    showCodeText: LocalizedString
    type: typing_extensions.Literal[
        "BARCODE_TYPE_UNSPECIFIED",
        "AZTEC",
        "aztec",
        "CODE_39",
        "code39",
        "CODE_128",
        "code128",
        "CODABAR",
        "codabar",
        "DATA_MATRIX",
        "dataMatrix",
        "EAN_8",
        "ean8",
        "EAN_13",
        "ean13",
        "EAN13",
        "ITF_14",
        "itf14",
        "PDF_417",
        "pdf417",
        "PDF417",
        "QR_CODE",
        "qrCode",
        "qrcode",
        "UPC_A",
        "upcA",
        "TEXT_ONLY",
        "textOnly",
    ]
    value: str

@typing.type_check_only
class BarcodeSectionDetail(typing_extensions.TypedDict, total=False):
    fieldSelector: FieldSelector

@typing.type_check_only
class Blobstore2Info(typing_extensions.TypedDict, total=False):
    blobGeneration: str
    blobId: str
    downloadReadHandle: str
    readToken: str
    uploadMetadataContainer: str

@typing.type_check_only
class BoardingAndSeatingInfo(typing_extensions.TypedDict, total=False):
    boardingDoor: typing_extensions.Literal[
        "BOARDING_DOOR_UNSPECIFIED", "FRONT", "front", "BACK", "back"
    ]
    boardingGroup: str
    boardingPosition: str
    boardingPrivilegeImage: Image
    kind: str
    seatAssignment: LocalizedString
    seatClass: str
    seatNumber: str
    sequenceNumber: str

@typing.type_check_only
class BoardingAndSeatingPolicy(typing_extensions.TypedDict, total=False):
    boardingPolicy: typing_extensions.Literal[
        "BOARDING_POLICY_UNSPECIFIED",
        "ZONE_BASED",
        "zoneBased",
        "GROUP_BASED",
        "groupBased",
        "BOARDING_POLICY_OTHER",
        "boardingPolicyOther",
    ]
    kind: str
    seatClassPolicy: typing_extensions.Literal[
        "SEAT_CLASS_POLICY_UNSPECIFIED",
        "CABIN_BASED",
        "cabinBased",
        "CLASS_BASED",
        "classBased",
        "TIER_BASED",
        "tierBased",
        "SEAT_CLASS_POLICY_OTHER",
        "seatClassPolicyOther",
    ]

@typing.type_check_only
class CallbackOptions(typing_extensions.TypedDict, total=False):
    updateRequestUrl: str
    url: str

@typing.type_check_only
class CardBarcodeSectionDetails(typing_extensions.TypedDict, total=False):
    firstBottomDetail: BarcodeSectionDetail
    firstTopDetail: BarcodeSectionDetail
    secondTopDetail: BarcodeSectionDetail

@typing.type_check_only
class CardRowOneItem(typing_extensions.TypedDict, total=False):
    item: TemplateItem

@typing.type_check_only
class CardRowTemplateInfo(typing_extensions.TypedDict, total=False):
    oneItem: CardRowOneItem
    threeItems: CardRowThreeItems
    twoItems: CardRowTwoItems

@typing.type_check_only
class CardRowThreeItems(typing_extensions.TypedDict, total=False):
    endItem: TemplateItem
    middleItem: TemplateItem
    startItem: TemplateItem

@typing.type_check_only
class CardRowTwoItems(typing_extensions.TypedDict, total=False):
    endItem: TemplateItem
    startItem: TemplateItem

@typing.type_check_only
class CardTemplateOverride(typing_extensions.TypedDict, total=False):
    cardRowTemplateInfos: _list[CardRowTemplateInfo]

@typing.type_check_only
class ClassTemplateInfo(typing_extensions.TypedDict, total=False):
    cardBarcodeSectionDetails: CardBarcodeSectionDetails
    cardTemplateOverride: CardTemplateOverride
    detailsTemplateOverride: DetailsTemplateOverride
    listTemplateOverride: ListTemplateOverride

@typing.type_check_only
class CompositeMedia(typing_extensions.TypedDict, total=False):
    blobRef: str
    blobstore2Info: Blobstore2Info
    cosmoBinaryReference: str
    crc32cHash: int
    inline: str
    length: str
    md5Hash: str
    objectId: ObjectId
    path: str
    referenceType: typing_extensions.Literal[
        "PATH", "BLOB_REF", "INLINE", "BIGSTORE_REF", "COSMO_BINARY_REFERENCE"
    ]
    sha1Hash: str

@typing.type_check_only
class ContentTypeInfo(typing_extensions.TypedDict, total=False):
    bestGuess: str
    fromBytes: str
    fromFileName: str
    fromHeader: str
    fromUrlPath: str

@typing.type_check_only
class DateTime(typing_extensions.TypedDict, total=False):
    date: str

@typing.type_check_only
class DetailsItemInfo(typing_extensions.TypedDict, total=False):
    item: TemplateItem

@typing.type_check_only
class DetailsTemplateOverride(typing_extensions.TypedDict, total=False):
    detailsItemInfos: _list[DetailsItemInfo]

@typing.type_check_only
class DeviceContext(typing_extensions.TypedDict, total=False):
    deviceToken: str

@typing.type_check_only
class DiffChecksumsResponse(typing_extensions.TypedDict, total=False):
    checksumsLocation: CompositeMedia
    chunkSizeBytes: str
    objectLocation: CompositeMedia
    objectSizeBytes: str
    objectVersion: str

@typing.type_check_only
class DiffDownloadResponse(typing_extensions.TypedDict, total=False):
    objectLocation: CompositeMedia

@typing.type_check_only
class DiffUploadRequest(typing_extensions.TypedDict, total=False):
    checksumsInfo: CompositeMedia
    objectInfo: CompositeMedia
    objectVersion: str

@typing.type_check_only
class DiffUploadResponse(typing_extensions.TypedDict, total=False):
    objectVersion: str
    originalObject: CompositeMedia

@typing.type_check_only
class DiffVersionResponse(typing_extensions.TypedDict, total=False):
    objectSizeBytes: str
    objectVersion: str

@typing.type_check_only
class DiscoverableProgram(typing_extensions.TypedDict, total=False):
    merchantSigninInfo: DiscoverableProgramMerchantSigninInfo
    merchantSignupInfo: DiscoverableProgramMerchantSignupInfo
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "TRUSTED_TESTERS",
        "trustedTesters",
        "LIVE",
        "live",
        "DISABLED",
        "disabled",
    ]

@typing.type_check_only
class DiscoverableProgramMerchantSigninInfo(typing_extensions.TypedDict, total=False):
    signinWebsite: Uri

@typing.type_check_only
class DiscoverableProgramMerchantSignupInfo(typing_extensions.TypedDict, total=False):
    signupSharedDatas: _list[
        typing_extensions.Literal[
            "SHARED_DATA_TYPE_UNSPECIFIED",
            "FIRST_NAME",
            "LAST_NAME",
            "STREET_ADDRESS",
            "ADDRESS_LINE_1",
            "ADDRESS_LINE_2",
            "ADDRESS_LINE_3",
            "CITY",
            "STATE",
            "ZIPCODE",
            "COUNTRY",
            "EMAIL",
            "PHONE",
        ]
    ]
    signupWebsite: Uri

@typing.type_check_only
class DownloadParameters(typing_extensions.TypedDict, total=False):
    allowGzipCompression: bool
    ignoreRange: bool

@typing.type_check_only
class EventDateTime(typing_extensions.TypedDict, total=False):
    customDoorsOpenLabel: LocalizedString
    doorsOpen: str
    doorsOpenLabel: typing_extensions.Literal[
        "DOORS_OPEN_LABEL_UNSPECIFIED",
        "DOORS_OPEN",
        "doorsOpen",
        "GATES_OPEN",
        "gatesOpen",
    ]
    end: str
    kind: str
    start: str

@typing.type_check_only
class EventReservationInfo(typing_extensions.TypedDict, total=False):
    confirmationCode: str
    kind: str

@typing.type_check_only
class EventSeat(typing_extensions.TypedDict, total=False):
    gate: LocalizedString
    kind: str
    row: LocalizedString
    seat: LocalizedString
    section: LocalizedString

@typing.type_check_only
class EventTicketClass(typing_extensions.TypedDict, total=False):
    allowMultipleUsersPerObject: bool
    appLinkData: AppLinkData
    callbackOptions: CallbackOptions
    classTemplateInfo: ClassTemplateInfo
    confirmationCodeLabel: typing_extensions.Literal[
        "CONFIRMATION_CODE_LABEL_UNSPECIFIED",
        "CONFIRMATION_CODE",
        "confirmationCode",
        "CONFIRMATION_NUMBER",
        "confirmationNumber",
        "ORDER_NUMBER",
        "orderNumber",
        "RESERVATION_NUMBER",
        "reservationNumber",
    ]
    countryCode: str
    customConfirmationCodeLabel: LocalizedString
    customGateLabel: LocalizedString
    customRowLabel: LocalizedString
    customSeatLabel: LocalizedString
    customSectionLabel: LocalizedString
    dateTime: EventDateTime
    enableSmartTap: bool
    eventId: str
    eventName: LocalizedString
    finePrint: LocalizedString
    gateLabel: typing_extensions.Literal[
        "GATE_LABEL_UNSPECIFIED", "GATE", "gate", "DOOR", "door", "ENTRANCE", "entrance"
    ]
    heroImage: Image
    hexBackgroundColor: str
    homepageUri: Uri
    id: str
    imageModulesData: _list[ImageModuleData]
    infoModuleData: InfoModuleData
    issuerName: str
    kind: str
    linksModuleData: LinksModuleData
    localizedIssuerName: LocalizedString
    locations: _list[LatLongPoint]
    logo: Image
    merchantLocations: _list[MerchantLocation]
    messages: _list[Message]
    multipleDevicesAndHoldersAllowedStatus: typing_extensions.Literal[
        "STATUS_UNSPECIFIED",
        "MULTIPLE_HOLDERS",
        "ONE_USER_ALL_DEVICES",
        "ONE_USER_ONE_DEVICE",
        "multipleHolders",
        "oneUserAllDevices",
        "oneUserOneDevice",
    ]
    notifyPreference: typing_extensions.Literal[
        "NOTIFICATION_SETTINGS_FOR_UPDATES_UNSPECIFIED", "NOTIFY_ON_UPDATE"
    ]
    redemptionIssuers: _list[str]
    review: Review
    reviewStatus: typing_extensions.Literal[
        "REVIEW_STATUS_UNSPECIFIED",
        "UNDER_REVIEW",
        "underReview",
        "APPROVED",
        "approved",
        "REJECTED",
        "rejected",
        "DRAFT",
        "draft",
    ]
    rowLabel: typing_extensions.Literal["ROW_LABEL_UNSPECIFIED", "ROW", "row"]
    seatLabel: typing_extensions.Literal["SEAT_LABEL_UNSPECIFIED", "SEAT", "seat"]
    sectionLabel: typing_extensions.Literal[
        "SECTION_LABEL_UNSPECIFIED", "SECTION", "section", "THEATER", "theater"
    ]
    securityAnimation: SecurityAnimation
    textModulesData: _list[TextModuleData]
    valueAddedModuleData: _list[ValueAddedModuleData]
    venue: EventVenue
    version: str
    viewUnlockRequirement: typing_extensions.Literal[
        "VIEW_UNLOCK_REQUIREMENT_UNSPECIFIED",
        "UNLOCK_NOT_REQUIRED",
        "UNLOCK_REQUIRED_TO_VIEW",
    ]
    wideLogo: Image
    wordMark: Image

@typing.type_check_only
class EventTicketClassAddMessageResponse(typing_extensions.TypedDict, total=False):
    resource: EventTicketClass

@typing.type_check_only
class EventTicketClassListResponse(typing_extensions.TypedDict, total=False):
    pagination: Pagination
    resources: _list[EventTicketClass]

@typing.type_check_only
class EventTicketObject(typing_extensions.TypedDict, total=False):
    appLinkData: AppLinkData
    barcode: Barcode
    classId: str
    classReference: EventTicketClass
    disableExpirationNotification: bool
    faceValue: Money
    groupingInfo: GroupingInfo
    hasLinkedDevice: bool
    hasUsers: bool
    heroImage: Image
    hexBackgroundColor: str
    id: str
    imageModulesData: _list[ImageModuleData]
    infoModuleData: InfoModuleData
    kind: str
    linkedObjectIds: _list[str]
    linkedOfferIds: _list[str]
    linksModuleData: LinksModuleData
    locations: _list[LatLongPoint]
    merchantLocations: _list[MerchantLocation]
    messages: _list[Message]
    notifyPreference: typing_extensions.Literal[
        "NOTIFICATION_SETTINGS_FOR_UPDATES_UNSPECIFIED", "NOTIFY_ON_UPDATE"
    ]
    passConstraints: PassConstraints
    reservationInfo: EventReservationInfo
    rotatingBarcode: RotatingBarcode
    saveRestrictions: SaveRestrictions
    seatInfo: EventSeat
    smartTapRedemptionValue: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "ACTIVE",
        "active",
        "COMPLETED",
        "completed",
        "EXPIRED",
        "expired",
        "INACTIVE",
        "inactive",
    ]
    textModulesData: _list[TextModuleData]
    ticketHolderName: str
    ticketNumber: str
    ticketType: LocalizedString
    validTimeInterval: TimeInterval
    valueAddedModuleData: _list[ValueAddedModuleData]
    version: str

@typing.type_check_only
class EventTicketObjectAddMessageResponse(typing_extensions.TypedDict, total=False):
    resource: EventTicketObject

@typing.type_check_only
class EventTicketObjectListResponse(typing_extensions.TypedDict, total=False):
    pagination: Pagination
    resources: _list[EventTicketObject]

@typing.type_check_only
class EventVenue(typing_extensions.TypedDict, total=False):
    address: LocalizedString
    kind: str
    name: LocalizedString

@typing.type_check_only
class ExpiryNotification(typing_extensions.TypedDict, total=False):
    enableNotification: bool

@typing.type_check_only
class FieldReference(typing_extensions.TypedDict, total=False):
    dateFormat: typing_extensions.Literal[
        "DATE_FORMAT_UNSPECIFIED",
        "DATE_TIME",
        "dateTime",
        "DATE_ONLY",
        "dateOnly",
        "TIME_ONLY",
        "timeOnly",
        "DATE_TIME_YEAR",
        "dateTimeYear",
        "DATE_YEAR",
        "dateYear",
        "YEAR_MONTH",
        "YEAR_MONTH_DAY",
    ]
    fieldPath: str

@typing.type_check_only
class FieldSelector(typing_extensions.TypedDict, total=False):
    fields: _list[FieldReference]

@typing.type_check_only
class FirstRowOption(typing_extensions.TypedDict, total=False):
    fieldOption: FieldSelector
    transitOption: typing_extensions.Literal[
        "TRANSIT_OPTION_UNSPECIFIED",
        "ORIGIN_AND_DESTINATION_NAMES",
        "originAndDestinationNames",
        "ORIGIN_AND_DESTINATION_CODES",
        "originAndDestinationCodes",
        "ORIGIN_NAME",
        "originName",
    ]

@typing.type_check_only
class FlightCarrier(typing_extensions.TypedDict, total=False):
    airlineAllianceLogo: Image
    airlineLogo: Image
    airlineName: LocalizedString
    carrierIataCode: str
    carrierIcaoCode: str
    kind: str
    wideAirlineLogo: Image

@typing.type_check_only
class FlightClass(typing_extensions.TypedDict, total=False):
    allowMultipleUsersPerObject: bool
    appLinkData: AppLinkData
    boardingAndSeatingPolicy: BoardingAndSeatingPolicy
    callbackOptions: CallbackOptions
    classTemplateInfo: ClassTemplateInfo
    countryCode: str
    destination: AirportInfo
    enableSmartTap: bool
    flightHeader: FlightHeader
    flightStatus: typing_extensions.Literal[
        "FLIGHT_STATUS_UNSPECIFIED",
        "SCHEDULED",
        "scheduled",
        "ACTIVE",
        "active",
        "LANDED",
        "landed",
        "CANCELLED",
        "cancelled",
        "REDIRECTED",
        "redirected",
        "DIVERTED",
        "diverted",
    ]
    heroImage: Image
    hexBackgroundColor: str
    homepageUri: Uri
    id: str
    imageModulesData: _list[ImageModuleData]
    infoModuleData: InfoModuleData
    issuerName: str
    kind: str
    languageOverride: str
    linksModuleData: LinksModuleData
    localBoardingDateTime: str
    localEstimatedOrActualArrivalDateTime: str
    localEstimatedOrActualDepartureDateTime: str
    localGateClosingDateTime: str
    localScheduledArrivalDateTime: str
    localScheduledDepartureDateTime: str
    localizedIssuerName: LocalizedString
    locations: _list[LatLongPoint]
    merchantLocations: _list[MerchantLocation]
    messages: _list[Message]
    multipleDevicesAndHoldersAllowedStatus: typing_extensions.Literal[
        "STATUS_UNSPECIFIED",
        "MULTIPLE_HOLDERS",
        "ONE_USER_ALL_DEVICES",
        "ONE_USER_ONE_DEVICE",
        "multipleHolders",
        "oneUserAllDevices",
        "oneUserOneDevice",
    ]
    notifyPreference: typing_extensions.Literal[
        "NOTIFICATION_SETTINGS_FOR_UPDATES_UNSPECIFIED", "NOTIFY_ON_UPDATE"
    ]
    origin: AirportInfo
    redemptionIssuers: _list[str]
    review: Review
    reviewStatus: typing_extensions.Literal[
        "REVIEW_STATUS_UNSPECIFIED",
        "UNDER_REVIEW",
        "underReview",
        "APPROVED",
        "approved",
        "REJECTED",
        "rejected",
        "DRAFT",
        "draft",
    ]
    securityAnimation: SecurityAnimation
    textModulesData: _list[TextModuleData]
    valueAddedModuleData: _list[ValueAddedModuleData]
    version: str
    viewUnlockRequirement: typing_extensions.Literal[
        "VIEW_UNLOCK_REQUIREMENT_UNSPECIFIED",
        "UNLOCK_NOT_REQUIRED",
        "UNLOCK_REQUIRED_TO_VIEW",
    ]
    wordMark: Image

@typing.type_check_only
class FlightClassAddMessageResponse(typing_extensions.TypedDict, total=False):
    resource: FlightClass

@typing.type_check_only
class FlightClassListResponse(typing_extensions.TypedDict, total=False):
    pagination: Pagination
    resources: _list[FlightClass]

@typing.type_check_only
class FlightHeader(typing_extensions.TypedDict, total=False):
    carrier: FlightCarrier
    flightNumber: str
    flightNumberDisplayOverride: str
    kind: str
    operatingCarrier: FlightCarrier
    operatingFlightNumber: str

@typing.type_check_only
class FlightObject(typing_extensions.TypedDict, total=False):
    appLinkData: AppLinkData
    barcode: Barcode
    boardingAndSeatingInfo: BoardingAndSeatingInfo
    classId: str
    classReference: FlightClass
    disableExpirationNotification: bool
    groupingInfo: GroupingInfo
    hasLinkedDevice: bool
    hasUsers: bool
    heroImage: Image
    hexBackgroundColor: str
    id: str
    imageModulesData: _list[ImageModuleData]
    infoModuleData: InfoModuleData
    kind: str
    linkedObjectIds: _list[str]
    linksModuleData: LinksModuleData
    locations: _list[LatLongPoint]
    merchantLocations: _list[MerchantLocation]
    messages: _list[Message]
    notifyPreference: typing_extensions.Literal[
        "NOTIFICATION_SETTINGS_FOR_UPDATES_UNSPECIFIED", "NOTIFY_ON_UPDATE"
    ]
    passConstraints: PassConstraints
    passengerName: str
    reservationInfo: ReservationInfo
    rotatingBarcode: RotatingBarcode
    saveRestrictions: SaveRestrictions
    securityProgramLogo: Image
    smartTapRedemptionValue: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "ACTIVE",
        "active",
        "COMPLETED",
        "completed",
        "EXPIRED",
        "expired",
        "INACTIVE",
        "inactive",
    ]
    textModulesData: _list[TextModuleData]
    validTimeInterval: TimeInterval
    valueAddedModuleData: _list[ValueAddedModuleData]
    version: str

@typing.type_check_only
class FlightObjectAddMessageResponse(typing_extensions.TypedDict, total=False):
    resource: FlightObject

@typing.type_check_only
class FlightObjectListResponse(typing_extensions.TypedDict, total=False):
    pagination: Pagination
    resources: _list[FlightObject]

@typing.type_check_only
class FrequentFlyerInfo(typing_extensions.TypedDict, total=False):
    frequentFlyerNumber: str
    frequentFlyerProgramName: LocalizedString
    kind: str

@typing.type_check_only
class GenericClass(typing_extensions.TypedDict, total=False):
    appLinkData: AppLinkData
    callbackOptions: CallbackOptions
    classTemplateInfo: ClassTemplateInfo
    enableSmartTap: bool
    id: str
    imageModulesData: _list[ImageModuleData]
    linksModuleData: LinksModuleData
    merchantLocations: _list[MerchantLocation]
    messages: _list[Message]
    multipleDevicesAndHoldersAllowedStatus: typing_extensions.Literal[
        "STATUS_UNSPECIFIED",
        "MULTIPLE_HOLDERS",
        "ONE_USER_ALL_DEVICES",
        "ONE_USER_ONE_DEVICE",
        "multipleHolders",
        "oneUserAllDevices",
        "oneUserOneDevice",
    ]
    redemptionIssuers: _list[str]
    securityAnimation: SecurityAnimation
    textModulesData: _list[TextModuleData]
    valueAddedModuleData: _list[ValueAddedModuleData]
    viewUnlockRequirement: typing_extensions.Literal[
        "VIEW_UNLOCK_REQUIREMENT_UNSPECIFIED",
        "UNLOCK_NOT_REQUIRED",
        "UNLOCK_REQUIRED_TO_VIEW",
    ]

@typing.type_check_only
class GenericClassAddMessageResponse(typing_extensions.TypedDict, total=False):
    resource: GenericClass

@typing.type_check_only
class GenericClassListResponse(typing_extensions.TypedDict, total=False):
    pagination: Pagination
    resources: _list[GenericClass]

@typing.type_check_only
class GenericObject(typing_extensions.TypedDict, total=False):
    appLinkData: AppLinkData
    barcode: Barcode
    cardTitle: LocalizedString
    classId: str
    genericType: typing_extensions.Literal[
        "GENERIC_TYPE_UNSPECIFIED",
        "GENERIC_SEASON_PASS",
        "GENERIC_UTILITY_BILLS",
        "GENERIC_PARKING_PASS",
        "GENERIC_VOUCHER",
        "GENERIC_GYM_MEMBERSHIP",
        "GENERIC_LIBRARY_MEMBERSHIP",
        "GENERIC_RESERVATIONS",
        "GENERIC_AUTO_INSURANCE",
        "GENERIC_HOME_INSURANCE",
        "GENERIC_ENTRY_TICKET",
        "GENERIC_RECEIPT",
        "GENERIC_LOYALTY_CARD",
        "GENERIC_OTHER",
    ]
    groupingInfo: GroupingInfo
    hasUsers: bool
    header: LocalizedString
    heroImage: Image
    hexBackgroundColor: str
    id: str
    imageModulesData: _list[ImageModuleData]
    linkedObjectIds: _list[str]
    linksModuleData: LinksModuleData
    logo: Image
    merchantLocations: _list[MerchantLocation]
    messages: _list[Message]
    notifications: Notifications
    passConstraints: PassConstraints
    rotatingBarcode: RotatingBarcode
    saveRestrictions: SaveRestrictions
    smartTapRedemptionValue: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "ACTIVE",
        "active",
        "COMPLETED",
        "completed",
        "EXPIRED",
        "expired",
        "INACTIVE",
        "inactive",
    ]
    subheader: LocalizedString
    textModulesData: _list[TextModuleData]
    validTimeInterval: TimeInterval
    valueAddedModuleData: _list[ValueAddedModuleData]
    wideLogo: Image

@typing.type_check_only
class GenericObjectAddMessageResponse(typing_extensions.TypedDict, total=False):
    resource: GenericObject

@typing.type_check_only
class GenericObjectListResponse(typing_extensions.TypedDict, total=False):
    pagination: Pagination
    resources: _list[GenericObject]

@typing.type_check_only
class GiftCardClass(typing_extensions.TypedDict, total=False):
    allowBarcodeRedemption: bool
    allowMultipleUsersPerObject: bool
    appLinkData: AppLinkData
    callbackOptions: CallbackOptions
    cardNumberLabel: str
    classTemplateInfo: ClassTemplateInfo
    countryCode: str
    enableSmartTap: bool
    eventNumberLabel: str
    heroImage: Image
    hexBackgroundColor: str
    homepageUri: Uri
    id: str
    imageModulesData: _list[ImageModuleData]
    infoModuleData: InfoModuleData
    issuerName: str
    kind: str
    linksModuleData: LinksModuleData
    localizedCardNumberLabel: LocalizedString
    localizedEventNumberLabel: LocalizedString
    localizedIssuerName: LocalizedString
    localizedMerchantName: LocalizedString
    localizedPinLabel: LocalizedString
    locations: _list[LatLongPoint]
    merchantLocations: _list[MerchantLocation]
    merchantName: str
    messages: _list[Message]
    multipleDevicesAndHoldersAllowedStatus: typing_extensions.Literal[
        "STATUS_UNSPECIFIED",
        "MULTIPLE_HOLDERS",
        "ONE_USER_ALL_DEVICES",
        "ONE_USER_ONE_DEVICE",
        "multipleHolders",
        "oneUserAllDevices",
        "oneUserOneDevice",
    ]
    notifyPreference: typing_extensions.Literal[
        "NOTIFICATION_SETTINGS_FOR_UPDATES_UNSPECIFIED", "NOTIFY_ON_UPDATE"
    ]
    pinLabel: str
    programLogo: Image
    redemptionIssuers: _list[str]
    review: Review
    reviewStatus: typing_extensions.Literal[
        "REVIEW_STATUS_UNSPECIFIED",
        "UNDER_REVIEW",
        "underReview",
        "APPROVED",
        "approved",
        "REJECTED",
        "rejected",
        "DRAFT",
        "draft",
    ]
    securityAnimation: SecurityAnimation
    textModulesData: _list[TextModuleData]
    valueAddedModuleData: _list[ValueAddedModuleData]
    version: str
    viewUnlockRequirement: typing_extensions.Literal[
        "VIEW_UNLOCK_REQUIREMENT_UNSPECIFIED",
        "UNLOCK_NOT_REQUIRED",
        "UNLOCK_REQUIRED_TO_VIEW",
    ]
    wideProgramLogo: Image
    wordMark: Image

@typing.type_check_only
class GiftCardClassAddMessageResponse(typing_extensions.TypedDict, total=False):
    resource: GiftCardClass

@typing.type_check_only
class GiftCardClassListResponse(typing_extensions.TypedDict, total=False):
    pagination: Pagination
    resources: _list[GiftCardClass]

@typing.type_check_only
class GiftCardObject(typing_extensions.TypedDict, total=False):
    appLinkData: AppLinkData
    balance: Money
    balanceUpdateTime: DateTime
    barcode: Barcode
    cardNumber: str
    classId: str
    classReference: GiftCardClass
    disableExpirationNotification: bool
    eventNumber: str
    groupingInfo: GroupingInfo
    hasLinkedDevice: bool
    hasUsers: bool
    heroImage: Image
    id: str
    imageModulesData: _list[ImageModuleData]
    infoModuleData: InfoModuleData
    kind: str
    linkedObjectIds: _list[str]
    linksModuleData: LinksModuleData
    locations: _list[LatLongPoint]
    merchantLocations: _list[MerchantLocation]
    messages: _list[Message]
    notifyPreference: typing_extensions.Literal[
        "NOTIFICATION_SETTINGS_FOR_UPDATES_UNSPECIFIED", "NOTIFY_ON_UPDATE"
    ]
    passConstraints: PassConstraints
    pin: str
    rotatingBarcode: RotatingBarcode
    saveRestrictions: SaveRestrictions
    smartTapRedemptionValue: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "ACTIVE",
        "active",
        "COMPLETED",
        "completed",
        "EXPIRED",
        "expired",
        "INACTIVE",
        "inactive",
    ]
    textModulesData: _list[TextModuleData]
    validTimeInterval: TimeInterval
    valueAddedModuleData: _list[ValueAddedModuleData]
    version: str

@typing.type_check_only
class GiftCardObjectAddMessageResponse(typing_extensions.TypedDict, total=False):
    resource: GiftCardObject

@typing.type_check_only
class GiftCardObjectListResponse(typing_extensions.TypedDict, total=False):
    pagination: Pagination
    resources: _list[GiftCardObject]

@typing.type_check_only
class GroupingInfo(typing_extensions.TypedDict, total=False):
    groupingId: str
    sortIndex: int

@typing.type_check_only
class Image(typing_extensions.TypedDict, total=False):
    contentDescription: LocalizedString
    kind: str
    sourceUri: ImageUri

@typing.type_check_only
class ImageModuleData(typing_extensions.TypedDict, total=False):
    id: str
    mainImage: Image

@typing.type_check_only
class ImageUri(typing_extensions.TypedDict, total=False):
    description: str
    localizedDescription: LocalizedString
    uri: str

@typing.type_check_only
class InfoModuleData(typing_extensions.TypedDict, total=False):
    labelValueRows: _list[LabelValueRow]
    showLastUpdateTime: bool

@typing.type_check_only
class Issuer(typing_extensions.TypedDict, total=False):
    callbackOptions: CallbackOptions
    contactInfo: IssuerContactInfo
    homepageUrl: str
    issuerId: str
    name: str
    smartTapMerchantData: SmartTapMerchantData

@typing.type_check_only
class IssuerContactInfo(typing_extensions.TypedDict, total=False):
    alertsEmails: _list[str]
    email: str
    name: str
    phone: str

@typing.type_check_only
class IssuerListResponse(typing_extensions.TypedDict, total=False):
    resources: _list[Issuer]

@typing.type_check_only
class IssuerToUserInfo(typing_extensions.TypedDict, total=False):
    action: typing_extensions.Literal[
        "ACTION_UNSPECIFIED", "S2AP", "s2ap", "SIGN_UP", "signUp"
    ]
    signUpInfo: SignUpInfo
    url: str
    value: str

@typing.type_check_only
class JwtInsertResponse(typing_extensions.TypedDict, total=False):
    resources: Resources
    saveUri: str

@typing.type_check_only
class JwtResource(typing_extensions.TypedDict, total=False):
    jwt: str

@typing.type_check_only
class LabelValue(typing_extensions.TypedDict, total=False):
    label: str
    localizedLabel: LocalizedString
    localizedValue: LocalizedString
    value: str

@typing.type_check_only
class LabelValueRow(typing_extensions.TypedDict, total=False):
    columns: _list[LabelValue]

@typing.type_check_only
class LatLongPoint(typing_extensions.TypedDict, total=False):
    kind: str
    latitude: float
    longitude: float

@typing.type_check_only
class LinksModuleData(typing_extensions.TypedDict, total=False):
    uris: _list[Uri]

@typing.type_check_only
class ListTemplateOverride(typing_extensions.TypedDict, total=False):
    firstRowOption: FirstRowOption
    secondRowOption: FieldSelector
    thirdRowOption: FieldSelector

@typing.type_check_only
class LocalizedString(typing_extensions.TypedDict, total=False):
    defaultValue: TranslatedString
    kind: str
    translatedValues: _list[TranslatedString]

@typing.type_check_only
class LoyaltyClass(typing_extensions.TypedDict, total=False):
    accountIdLabel: str
    accountNameLabel: str
    allowMultipleUsersPerObject: bool
    appLinkData: AppLinkData
    callbackOptions: CallbackOptions
    classTemplateInfo: ClassTemplateInfo
    countryCode: str
    discoverableProgram: DiscoverableProgram
    enableSmartTap: bool
    heroImage: Image
    hexBackgroundColor: str
    homepageUri: Uri
    id: str
    imageModulesData: _list[ImageModuleData]
    infoModuleData: InfoModuleData
    issuerName: str
    kind: str
    linksModuleData: LinksModuleData
    localizedAccountIdLabel: LocalizedString
    localizedAccountNameLabel: LocalizedString
    localizedIssuerName: LocalizedString
    localizedProgramName: LocalizedString
    localizedRewardsTier: LocalizedString
    localizedRewardsTierLabel: LocalizedString
    localizedSecondaryRewardsTier: LocalizedString
    localizedSecondaryRewardsTierLabel: LocalizedString
    locations: _list[LatLongPoint]
    merchantLocations: _list[MerchantLocation]
    messages: _list[Message]
    multipleDevicesAndHoldersAllowedStatus: typing_extensions.Literal[
        "STATUS_UNSPECIFIED",
        "MULTIPLE_HOLDERS",
        "ONE_USER_ALL_DEVICES",
        "ONE_USER_ONE_DEVICE",
        "multipleHolders",
        "oneUserAllDevices",
        "oneUserOneDevice",
    ]
    notifyPreference: typing_extensions.Literal[
        "NOTIFICATION_SETTINGS_FOR_UPDATES_UNSPECIFIED", "NOTIFY_ON_UPDATE"
    ]
    programLogo: Image
    programName: str
    redemptionIssuers: _list[str]
    review: Review
    reviewStatus: typing_extensions.Literal[
        "REVIEW_STATUS_UNSPECIFIED",
        "UNDER_REVIEW",
        "underReview",
        "APPROVED",
        "approved",
        "REJECTED",
        "rejected",
        "DRAFT",
        "draft",
    ]
    rewardsTier: str
    rewardsTierLabel: str
    secondaryRewardsTier: str
    secondaryRewardsTierLabel: str
    securityAnimation: SecurityAnimation
    textModulesData: _list[TextModuleData]
    valueAddedModuleData: _list[ValueAddedModuleData]
    version: str
    viewUnlockRequirement: typing_extensions.Literal[
        "VIEW_UNLOCK_REQUIREMENT_UNSPECIFIED",
        "UNLOCK_NOT_REQUIRED",
        "UNLOCK_REQUIRED_TO_VIEW",
    ]
    wideProgramLogo: Image
    wordMark: Image

@typing.type_check_only
class LoyaltyClassAddMessageResponse(typing_extensions.TypedDict, total=False):
    resource: LoyaltyClass

@typing.type_check_only
class LoyaltyClassListResponse(typing_extensions.TypedDict, total=False):
    pagination: Pagination
    resources: _list[LoyaltyClass]

@typing.type_check_only
class LoyaltyObject(typing_extensions.TypedDict, total=False):
    accountId: str
    accountName: str
    appLinkData: AppLinkData
    barcode: Barcode
    classId: str
    classReference: LoyaltyClass
    disableExpirationNotification: bool
    groupingInfo: GroupingInfo
    hasLinkedDevice: bool
    hasUsers: bool
    heroImage: Image
    id: str
    imageModulesData: _list[ImageModuleData]
    infoModuleData: InfoModuleData
    kind: str
    linkedObjectIds: _list[str]
    linkedOfferIds: _list[str]
    linksModuleData: LinksModuleData
    locations: _list[LatLongPoint]
    loyaltyPoints: LoyaltyPoints
    merchantLocations: _list[MerchantLocation]
    messages: _list[Message]
    notifyPreference: typing_extensions.Literal[
        "NOTIFICATION_SETTINGS_FOR_UPDATES_UNSPECIFIED", "NOTIFY_ON_UPDATE"
    ]
    passConstraints: PassConstraints
    rotatingBarcode: RotatingBarcode
    saveRestrictions: SaveRestrictions
    secondaryLoyaltyPoints: LoyaltyPoints
    smartTapRedemptionValue: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "ACTIVE",
        "active",
        "COMPLETED",
        "completed",
        "EXPIRED",
        "expired",
        "INACTIVE",
        "inactive",
    ]
    textModulesData: _list[TextModuleData]
    validTimeInterval: TimeInterval
    valueAddedModuleData: _list[ValueAddedModuleData]
    version: str

@typing.type_check_only
class LoyaltyObjectAddMessageResponse(typing_extensions.TypedDict, total=False):
    resource: LoyaltyObject

@typing.type_check_only
class LoyaltyObjectListResponse(typing_extensions.TypedDict, total=False):
    pagination: Pagination
    resources: _list[LoyaltyObject]

@typing.type_check_only
class LoyaltyPoints(typing_extensions.TypedDict, total=False):
    balance: LoyaltyPointsBalance
    label: str
    localizedLabel: LocalizedString

@typing.type_check_only
class LoyaltyPointsBalance(typing_extensions.TypedDict, total=False):
    double: float
    int: int
    money: Money
    string: str

@typing.type_check_only
class Media(typing_extensions.TypedDict, total=False):
    algorithm: str
    bigstoreObjectRef: str
    blobRef: str
    blobstore2Info: Blobstore2Info
    compositeMedia: _list[CompositeMedia]
    contentType: str
    contentTypeInfo: ContentTypeInfo
    cosmoBinaryReference: str
    crc32cHash: int
    diffChecksumsResponse: DiffChecksumsResponse
    diffDownloadResponse: DiffDownloadResponse
    diffUploadRequest: DiffUploadRequest
    diffUploadResponse: DiffUploadResponse
    diffVersionResponse: DiffVersionResponse
    downloadParameters: DownloadParameters
    filename: str
    hash: str
    hashVerified: bool
    inline: str
    isPotentialRetry: bool
    length: str
    md5Hash: str
    mediaId: str
    objectId: ObjectId
    path: str
    referenceType: typing_extensions.Literal[
        "PATH",
        "BLOB_REF",
        "INLINE",
        "GET_MEDIA",
        "COMPOSITE_MEDIA",
        "BIGSTORE_REF",
        "DIFF_VERSION_RESPONSE",
        "DIFF_CHECKSUMS_RESPONSE",
        "DIFF_DOWNLOAD_RESPONSE",
        "DIFF_UPLOAD_REQUEST",
        "DIFF_UPLOAD_RESPONSE",
        "COSMO_BINARY_REFERENCE",
        "ARBITRARY_BYTES",
    ]
    sha1Hash: str
    sha256Hash: str
    timestamp: str
    token: str

@typing.type_check_only
class MediaRequestInfo(typing_extensions.TypedDict, total=False):
    currentBytes: str
    customData: str
    diffObjectVersion: str
    finalStatus: int
    notificationType: typing_extensions.Literal[
        "START", "PROGRESS", "END", "RESPONSE_SENT", "ERROR"
    ]
    requestId: str
    requestReceivedParamsServingInfo: str
    totalBytes: str
    totalBytesIsEstimated: bool

@typing.type_check_only
class MerchantLocation(typing_extensions.TypedDict, total=False):
    latitude: float
    longitude: float

@typing.type_check_only
class Message(typing_extensions.TypedDict, total=False):
    body: str
    displayInterval: TimeInterval
    header: str
    id: str
    kind: str
    localizedBody: LocalizedString
    localizedHeader: LocalizedString
    messageType: typing_extensions.Literal[
        "MESSAGE_TYPE_UNSPECIFIED",
        "TEXT",
        "text",
        "EXPIRATION_NOTIFICATION",
        "expirationNotification",
        "TEXT_AND_NOTIFY",
    ]

@typing.type_check_only
class ModifyLinkedOfferObjects(typing_extensions.TypedDict, total=False):
    addLinkedOfferObjectIds: _list[str]
    removeLinkedOfferObjectIds: _list[str]

@typing.type_check_only
class ModifyLinkedOfferObjectsRequest(typing_extensions.TypedDict, total=False):
    linkedOfferObjectIds: ModifyLinkedOfferObjects

@typing.type_check_only
class ModuleViewConstraints(typing_extensions.TypedDict, total=False):
    displayInterval: TimeInterval

@typing.type_check_only
class Money(typing_extensions.TypedDict, total=False):
    currencyCode: str
    kind: str
    micros: str

@typing.type_check_only
class Notifications(typing_extensions.TypedDict, total=False):
    expiryNotification: ExpiryNotification
    upcomingNotification: UpcomingNotification

@typing.type_check_only
class ObjectId(typing_extensions.TypedDict, total=False):
    bucketName: str
    generation: str
    objectName: str

@typing.type_check_only
class OfferClass(typing_extensions.TypedDict, total=False):
    allowMultipleUsersPerObject: bool
    appLinkData: AppLinkData
    callbackOptions: CallbackOptions
    classTemplateInfo: ClassTemplateInfo
    countryCode: str
    details: str
    enableSmartTap: bool
    finePrint: str
    helpUri: Uri
    heroImage: Image
    hexBackgroundColor: str
    homepageUri: Uri
    id: str
    imageModulesData: _list[ImageModuleData]
    infoModuleData: InfoModuleData
    issuerName: str
    kind: str
    linksModuleData: LinksModuleData
    localizedDetails: LocalizedString
    localizedFinePrint: LocalizedString
    localizedIssuerName: LocalizedString
    localizedProvider: LocalizedString
    localizedShortTitle: LocalizedString
    localizedTitle: LocalizedString
    locations: _list[LatLongPoint]
    merchantLocations: _list[MerchantLocation]
    messages: _list[Message]
    multipleDevicesAndHoldersAllowedStatus: typing_extensions.Literal[
        "STATUS_UNSPECIFIED",
        "MULTIPLE_HOLDERS",
        "ONE_USER_ALL_DEVICES",
        "ONE_USER_ONE_DEVICE",
        "multipleHolders",
        "oneUserAllDevices",
        "oneUserOneDevice",
    ]
    notifyPreference: typing_extensions.Literal[
        "NOTIFICATION_SETTINGS_FOR_UPDATES_UNSPECIFIED", "NOTIFY_ON_UPDATE"
    ]
    provider: str
    redemptionChannel: typing_extensions.Literal[
        "REDEMPTION_CHANNEL_UNSPECIFIED",
        "INSTORE",
        "instore",
        "ONLINE",
        "online",
        "BOTH",
        "both",
        "TEMPORARY_PRICE_REDUCTION",
        "temporaryPriceReduction",
    ]
    redemptionIssuers: _list[str]
    review: Review
    reviewStatus: typing_extensions.Literal[
        "REVIEW_STATUS_UNSPECIFIED",
        "UNDER_REVIEW",
        "underReview",
        "APPROVED",
        "approved",
        "REJECTED",
        "rejected",
        "DRAFT",
        "draft",
    ]
    securityAnimation: SecurityAnimation
    shortTitle: str
    textModulesData: _list[TextModuleData]
    title: str
    titleImage: Image
    valueAddedModuleData: _list[ValueAddedModuleData]
    version: str
    viewUnlockRequirement: typing_extensions.Literal[
        "VIEW_UNLOCK_REQUIREMENT_UNSPECIFIED",
        "UNLOCK_NOT_REQUIRED",
        "UNLOCK_REQUIRED_TO_VIEW",
    ]
    wideTitleImage: Image
    wordMark: Image

@typing.type_check_only
class OfferClassAddMessageResponse(typing_extensions.TypedDict, total=False):
    resource: OfferClass

@typing.type_check_only
class OfferClassListResponse(typing_extensions.TypedDict, total=False):
    pagination: Pagination
    resources: _list[OfferClass]

@typing.type_check_only
class OfferObject(typing_extensions.TypedDict, total=False):
    appLinkData: AppLinkData
    barcode: Barcode
    classId: str
    classReference: OfferClass
    disableExpirationNotification: bool
    groupingInfo: GroupingInfo
    hasLinkedDevice: bool
    hasUsers: bool
    heroImage: Image
    id: str
    imageModulesData: _list[ImageModuleData]
    infoModuleData: InfoModuleData
    kind: str
    linkedObjectIds: _list[str]
    linksModuleData: LinksModuleData
    locations: _list[LatLongPoint]
    merchantLocations: _list[MerchantLocation]
    messages: _list[Message]
    notifyPreference: typing_extensions.Literal[
        "NOTIFICATION_SETTINGS_FOR_UPDATES_UNSPECIFIED", "NOTIFY_ON_UPDATE"
    ]
    passConstraints: PassConstraints
    rotatingBarcode: RotatingBarcode
    saveRestrictions: SaveRestrictions
    smartTapRedemptionValue: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "ACTIVE",
        "active",
        "COMPLETED",
        "completed",
        "EXPIRED",
        "expired",
        "INACTIVE",
        "inactive",
    ]
    textModulesData: _list[TextModuleData]
    validTimeInterval: TimeInterval
    valueAddedModuleData: _list[ValueAddedModuleData]
    version: str

@typing.type_check_only
class OfferObjectAddMessageResponse(typing_extensions.TypedDict, total=False):
    resource: OfferObject

@typing.type_check_only
class OfferObjectListResponse(typing_extensions.TypedDict, total=False):
    pagination: Pagination
    resources: _list[OfferObject]

@typing.type_check_only
class Pagination(typing_extensions.TypedDict, total=False):
    kind: str
    nextPageToken: str
    resultsPerPage: int

@typing.type_check_only
class PassConstraints(typing_extensions.TypedDict, total=False):
    nfcConstraint: _list[
        typing_extensions.Literal[
            "NFC_CONSTRAINT_UNSPECIFIED", "BLOCK_PAYMENT", "BLOCK_CLOSED_LOOP_TRANSIT"
        ]
    ]
    screenshotEligibility: typing_extensions.Literal[
        "SCREENSHOT_ELIGIBILITY_UNSPECIFIED", "ELIGIBLE", "INELIGIBLE"
    ]

@typing.type_check_only
class Permission(typing_extensions.TypedDict, total=False):
    emailAddress: str
    role: typing_extensions.Literal[
        "ROLE_UNSPECIFIED", "OWNER", "owner", "READER", "reader", "WRITER", "writer"
    ]

@typing.type_check_only
class Permissions(typing_extensions.TypedDict, total=False):
    issuerId: str
    permissions: _list[Permission]

@typing.type_check_only
class PurchaseDetails(typing_extensions.TypedDict, total=False):
    accountId: str
    confirmationCode: str
    purchaseDateTime: str
    purchaseReceiptNumber: str
    ticketCost: TicketCost

@typing.type_check_only
class ReservationInfo(typing_extensions.TypedDict, total=False):
    confirmationCode: str
    eticketNumber: str
    frequentFlyerInfo: FrequentFlyerInfo
    kind: str

@typing.type_check_only
class Resources(typing_extensions.TypedDict, total=False):
    eventTicketClasses: _list[EventTicketClass]
    eventTicketObjects: _list[EventTicketObject]
    flightClasses: _list[FlightClass]
    flightObjects: _list[FlightObject]
    genericClasses: _list[GenericClass]
    genericObjects: _list[GenericObject]
    giftCardClasses: _list[GiftCardClass]
    giftCardObjects: _list[GiftCardObject]
    loyaltyClasses: _list[LoyaltyClass]
    loyaltyObjects: _list[LoyaltyObject]
    offerClasses: _list[OfferClass]
    offerObjects: _list[OfferObject]
    transitClasses: _list[TransitClass]
    transitObjects: _list[TransitObject]

@typing.type_check_only
class Review(typing_extensions.TypedDict, total=False):
    comments: str

@typing.type_check_only
class RotatingBarcode(typing_extensions.TypedDict, total=False):
    alternateText: str
    initialRotatingBarcodeValues: RotatingBarcodeValues
    renderEncoding: typing_extensions.Literal["RENDER_ENCODING_UNSPECIFIED", "UTF_8"]
    showCodeText: LocalizedString
    totpDetails: RotatingBarcodeTotpDetails
    type: typing_extensions.Literal[
        "BARCODE_TYPE_UNSPECIFIED",
        "AZTEC",
        "aztec",
        "CODE_39",
        "code39",
        "CODE_128",
        "code128",
        "CODABAR",
        "codabar",
        "DATA_MATRIX",
        "dataMatrix",
        "EAN_8",
        "ean8",
        "EAN_13",
        "ean13",
        "EAN13",
        "ITF_14",
        "itf14",
        "PDF_417",
        "pdf417",
        "PDF417",
        "QR_CODE",
        "qrCode",
        "qrcode",
        "UPC_A",
        "upcA",
        "TEXT_ONLY",
        "textOnly",
    ]
    valuePattern: str

@typing.type_check_only
class RotatingBarcodeTotpDetails(typing_extensions.TypedDict, total=False):
    algorithm: typing_extensions.Literal["TOTP_ALGORITHM_UNSPECIFIED", "TOTP_SHA1"]
    parameters: _list[RotatingBarcodeTotpDetailsTotpParameters]
    periodMillis: str

@typing.type_check_only
class RotatingBarcodeTotpDetailsTotpParameters(
    typing_extensions.TypedDict, total=False
):
    key: str
    valueLength: int

@typing.type_check_only
class RotatingBarcodeValues(typing_extensions.TypedDict, total=False):
    periodMillis: str
    startDateTime: str
    values: _list[str]

@typing.type_check_only
class SaveRestrictions(typing_extensions.TypedDict, total=False):
    restrictToEmailSha256: str

@typing.type_check_only
class SecurityAnimation(typing_extensions.TypedDict, total=False):
    animationType: typing_extensions.Literal[
        "ANIMATION_UNSPECIFIED", "FOIL_SHIMMER", "foilShimmer"
    ]

@typing.type_check_only
class SignUpInfo(typing_extensions.TypedDict, total=False):
    classId: str

@typing.type_check_only
class SmartTap(typing_extensions.TypedDict, total=False):
    id: str
    infos: _list[IssuerToUserInfo]
    kind: str
    merchantId: str

@typing.type_check_only
class SmartTapMerchantData(typing_extensions.TypedDict, total=False):
    authenticationKeys: _list[AuthenticationKey]
    smartTapMerchantId: str

@typing.type_check_only
class TemplateItem(typing_extensions.TypedDict, total=False):
    firstValue: FieldSelector
    predefinedItem: typing_extensions.Literal[
        "PREDEFINED_ITEM_UNSPECIFIED",
        "FREQUENT_FLYER_PROGRAM_NAME_AND_NUMBER",
        "frequentFlyerProgramNameAndNumber",
        "FLIGHT_NUMBER_AND_OPERATING_FLIGHT_NUMBER",
        "flightNumberAndOperatingFlightNumber",
    ]
    secondValue: FieldSelector

@typing.type_check_only
class TextModuleData(typing_extensions.TypedDict, total=False):
    body: str
    header: str
    id: str
    localizedBody: LocalizedString
    localizedHeader: LocalizedString

@typing.type_check_only
class TicketCost(typing_extensions.TypedDict, total=False):
    discountMessage: LocalizedString
    faceValue: Money
    purchasePrice: Money

@typing.type_check_only
class TicketLeg(typing_extensions.TypedDict, total=False):
    arrivalDateTime: str
    carriage: str
    departureDateTime: str
    destinationName: LocalizedString
    destinationStationCode: str
    fareName: LocalizedString
    originName: LocalizedString
    originStationCode: str
    platform: str
    ticketSeat: TicketSeat
    ticketSeats: _list[TicketSeat]
    transitOperatorName: LocalizedString
    transitTerminusName: LocalizedString
    zone: str

@typing.type_check_only
class TicketRestrictions(typing_extensions.TypedDict, total=False):
    otherRestrictions: LocalizedString
    routeRestrictions: LocalizedString
    routeRestrictionsDetails: LocalizedString
    timeRestrictions: LocalizedString

@typing.type_check_only
class TicketSeat(typing_extensions.TypedDict, total=False):
    coach: str
    customFareClass: LocalizedString
    fareClass: typing_extensions.Literal[
        "FARE_CLASS_UNSPECIFIED",
        "ECONOMY",
        "economy",
        "FIRST",
        "first",
        "BUSINESS",
        "business",
    ]
    seat: str
    seatAssignment: LocalizedString

@typing.type_check_only
class TimeInterval(typing_extensions.TypedDict, total=False):
    end: DateTime
    kind: str
    start: DateTime

@typing.type_check_only
class TransitClass(typing_extensions.TypedDict, total=False):
    activationOptions: ActivationOptions
    allowMultipleUsersPerObject: bool
    appLinkData: AppLinkData
    callbackOptions: CallbackOptions
    classTemplateInfo: ClassTemplateInfo
    countryCode: str
    customCarriageLabel: LocalizedString
    customCoachLabel: LocalizedString
    customConcessionCategoryLabel: LocalizedString
    customConfirmationCodeLabel: LocalizedString
    customDiscountMessageLabel: LocalizedString
    customFareClassLabel: LocalizedString
    customFareNameLabel: LocalizedString
    customOtherRestrictionsLabel: LocalizedString
    customPlatformLabel: LocalizedString
    customPurchaseFaceValueLabel: LocalizedString
    customPurchasePriceLabel: LocalizedString
    customPurchaseReceiptNumberLabel: LocalizedString
    customRouteRestrictionsDetailsLabel: LocalizedString
    customRouteRestrictionsLabel: LocalizedString
    customSeatLabel: LocalizedString
    customTicketNumberLabel: LocalizedString
    customTimeRestrictionsLabel: LocalizedString
    customTransitTerminusNameLabel: LocalizedString
    customZoneLabel: LocalizedString
    enableSingleLegItinerary: bool
    enableSmartTap: bool
    heroImage: Image
    hexBackgroundColor: str
    homepageUri: Uri
    id: str
    imageModulesData: _list[ImageModuleData]
    infoModuleData: InfoModuleData
    issuerName: str
    languageOverride: str
    linksModuleData: LinksModuleData
    localizedIssuerName: LocalizedString
    locations: _list[LatLongPoint]
    logo: Image
    merchantLocations: _list[MerchantLocation]
    messages: _list[Message]
    multipleDevicesAndHoldersAllowedStatus: typing_extensions.Literal[
        "STATUS_UNSPECIFIED",
        "MULTIPLE_HOLDERS",
        "ONE_USER_ALL_DEVICES",
        "ONE_USER_ONE_DEVICE",
        "multipleHolders",
        "oneUserAllDevices",
        "oneUserOneDevice",
    ]
    notifyPreference: typing_extensions.Literal[
        "NOTIFICATION_SETTINGS_FOR_UPDATES_UNSPECIFIED", "NOTIFY_ON_UPDATE"
    ]
    redemptionIssuers: _list[str]
    review: Review
    reviewStatus: typing_extensions.Literal[
        "REVIEW_STATUS_UNSPECIFIED",
        "UNDER_REVIEW",
        "underReview",
        "APPROVED",
        "approved",
        "REJECTED",
        "rejected",
        "DRAFT",
        "draft",
    ]
    securityAnimation: SecurityAnimation
    textModulesData: _list[TextModuleData]
    transitOperatorName: LocalizedString
    transitType: typing_extensions.Literal[
        "TRANSIT_TYPE_UNSPECIFIED",
        "BUS",
        "bus",
        "RAIL",
        "rail",
        "TRAM",
        "tram",
        "FERRY",
        "ferry",
        "OTHER",
        "other",
    ]
    valueAddedModuleData: _list[ValueAddedModuleData]
    version: str
    viewUnlockRequirement: typing_extensions.Literal[
        "VIEW_UNLOCK_REQUIREMENT_UNSPECIFIED",
        "UNLOCK_NOT_REQUIRED",
        "UNLOCK_REQUIRED_TO_VIEW",
    ]
    watermark: Image
    wideLogo: Image
    wordMark: Image

@typing.type_check_only
class TransitClassAddMessageResponse(typing_extensions.TypedDict, total=False):
    resource: TransitClass

@typing.type_check_only
class TransitClassListResponse(typing_extensions.TypedDict, total=False):
    pagination: Pagination
    resources: _list[TransitClass]

@typing.type_check_only
class TransitObject(typing_extensions.TypedDict, total=False):
    activationStatus: ActivationStatus
    appLinkData: AppLinkData
    barcode: Barcode
    classId: str
    classReference: TransitClass
    concessionCategory: typing_extensions.Literal[
        "CONCESSION_CATEGORY_UNSPECIFIED",
        "ADULT",
        "adult",
        "CHILD",
        "child",
        "SENIOR",
        "senior",
    ]
    customConcessionCategory: LocalizedString
    customTicketStatus: LocalizedString
    deviceContext: DeviceContext
    disableExpirationNotification: bool
    groupingInfo: GroupingInfo
    hasLinkedDevice: bool
    hasUsers: bool
    heroImage: Image
    hexBackgroundColor: str
    id: str
    imageModulesData: _list[ImageModuleData]
    infoModuleData: InfoModuleData
    linkedObjectIds: _list[str]
    linksModuleData: LinksModuleData
    locations: _list[LatLongPoint]
    merchantLocations: _list[MerchantLocation]
    messages: _list[Message]
    notifyPreference: typing_extensions.Literal[
        "NOTIFICATION_SETTINGS_FOR_UPDATES_UNSPECIFIED", "NOTIFY_ON_UPDATE"
    ]
    passConstraints: PassConstraints
    passengerNames: str
    passengerType: typing_extensions.Literal[
        "PASSENGER_TYPE_UNSPECIFIED",
        "SINGLE_PASSENGER",
        "singlePassenger",
        "MULTIPLE_PASSENGERS",
        "multiplePassengers",
    ]
    purchaseDetails: PurchaseDetails
    rotatingBarcode: RotatingBarcode
    saveRestrictions: SaveRestrictions
    smartTapRedemptionValue: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "ACTIVE",
        "active",
        "COMPLETED",
        "completed",
        "EXPIRED",
        "expired",
        "INACTIVE",
        "inactive",
    ]
    textModulesData: _list[TextModuleData]
    ticketLeg: TicketLeg
    ticketLegs: _list[TicketLeg]
    ticketNumber: str
    ticketRestrictions: TicketRestrictions
    ticketStatus: typing_extensions.Literal[
        "TICKET_STATUS_UNSPECIFIED",
        "USED",
        "used",
        "REFUNDED",
        "refunded",
        "EXCHANGED",
        "exchanged",
    ]
    tripId: str
    tripType: typing_extensions.Literal[
        "TRIP_TYPE_UNSPECIFIED", "ROUND_TRIP", "roundTrip", "ONE_WAY", "oneWay"
    ]
    validTimeInterval: TimeInterval
    valueAddedModuleData: _list[ValueAddedModuleData]
    version: str

@typing.type_check_only
class TransitObjectAddMessageResponse(typing_extensions.TypedDict, total=False):
    resource: TransitObject

@typing.type_check_only
class TransitObjectListResponse(typing_extensions.TypedDict, total=False):
    pagination: Pagination
    resources: _list[TransitObject]

@typing.type_check_only
class TransitObjectUploadRotatingBarcodeValuesRequest(
    typing_extensions.TypedDict, total=False
):
    blob: Media
    mediaRequestInfo: MediaRequestInfo

@typing.type_check_only
class TransitObjectUploadRotatingBarcodeValuesResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class TranslatedString(typing_extensions.TypedDict, total=False):
    kind: str
    language: str
    value: str

@typing.type_check_only
class UpcomingNotification(typing_extensions.TypedDict, total=False):
    enableNotification: bool

@typing.type_check_only
class Uri(typing_extensions.TypedDict, total=False):
    description: str
    id: str
    kind: str
    localizedDescription: LocalizedString
    uri: str

@typing.type_check_only
class ValueAddedModuleData(typing_extensions.TypedDict, total=False):
    body: LocalizedString
    header: LocalizedString
    image: Image
    sortIndex: int
    uri: str
    viewConstraints: ModuleViewConstraints
