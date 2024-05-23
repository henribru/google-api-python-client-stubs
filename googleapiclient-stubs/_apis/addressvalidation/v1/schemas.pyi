import typing

import typing_extensions

_list = list

@typing.type_check_only
class GoogleGeoTypeViewport(typing_extensions.TypedDict, total=False):
    high: GoogleTypeLatLng
    low: GoogleTypeLatLng

@typing.type_check_only
class GoogleMapsAddressvalidationV1Address(typing_extensions.TypedDict, total=False):
    addressComponents: _list[GoogleMapsAddressvalidationV1AddressComponent]
    formattedAddress: str
    missingComponentTypes: _list[str]
    postalAddress: GoogleTypePostalAddress
    unconfirmedComponentTypes: _list[str]
    unresolvedTokens: _list[str]

@typing.type_check_only
class GoogleMapsAddressvalidationV1AddressComponent(
    typing_extensions.TypedDict, total=False
):
    componentName: GoogleMapsAddressvalidationV1ComponentName
    componentType: str
    confirmationLevel: typing_extensions.Literal[
        "CONFIRMATION_LEVEL_UNSPECIFIED",
        "CONFIRMED",
        "UNCONFIRMED_BUT_PLAUSIBLE",
        "UNCONFIRMED_AND_SUSPICIOUS",
    ]
    inferred: bool
    replaced: bool
    spellCorrected: bool
    unexpected: bool

@typing.type_check_only
class GoogleMapsAddressvalidationV1AddressMetadata(
    typing_extensions.TypedDict, total=False
):
    business: bool
    poBox: bool
    residential: bool

@typing.type_check_only
class GoogleMapsAddressvalidationV1ComponentName(
    typing_extensions.TypedDict, total=False
):
    languageCode: str
    text: str

@typing.type_check_only
class GoogleMapsAddressvalidationV1Geocode(typing_extensions.TypedDict, total=False):
    bounds: GoogleGeoTypeViewport
    featureSizeMeters: float
    location: GoogleTypeLatLng
    placeId: str
    placeTypes: _list[str]
    plusCode: GoogleMapsAddressvalidationV1PlusCode

@typing.type_check_only
class GoogleMapsAddressvalidationV1LanguageOptions(
    typing_extensions.TypedDict, total=False
):
    returnEnglishLatinAddress: bool

@typing.type_check_only
class GoogleMapsAddressvalidationV1PlusCode(typing_extensions.TypedDict, total=False):
    compoundCode: str
    globalCode: str

@typing.type_check_only
class GoogleMapsAddressvalidationV1ProvideValidationFeedbackRequest(
    typing_extensions.TypedDict, total=False
):
    conclusion: typing_extensions.Literal[
        "VALIDATION_CONCLUSION_UNSPECIFIED",
        "VALIDATED_VERSION_USED",
        "USER_VERSION_USED",
        "UNVALIDATED_VERSION_USED",
        "UNUSED",
    ]
    responseId: str

@typing.type_check_only
class GoogleMapsAddressvalidationV1ProvideValidationFeedbackResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleMapsAddressvalidationV1UspsAddress(
    typing_extensions.TypedDict, total=False
):
    city: str
    cityStateZipAddressLine: str
    firm: str
    firstAddressLine: str
    secondAddressLine: str
    state: str
    urbanization: str
    zipCode: str
    zipCodeExtension: str

@typing.type_check_only
class GoogleMapsAddressvalidationV1UspsData(typing_extensions.TypedDict, total=False):
    abbreviatedCity: str
    addressRecordType: str
    carrierRoute: str
    carrierRouteIndicator: str
    cassProcessed: bool
    county: str
    defaultAddress: bool
    deliveryPointCheckDigit: str
    deliveryPointCode: str
    dpvCmra: str
    dpvConfirmation: str
    dpvDoorNotAccessible: str
    dpvDrop: str
    dpvEnhancedDeliveryCode: str
    dpvFootnote: str
    dpvNoSecureLocation: str
    dpvNoStat: str
    dpvNoStatReasonCode: int
    dpvNonDeliveryDays: str
    dpvNonDeliveryDaysValues: int
    dpvPbsa: str
    dpvThrowback: str
    dpvVacant: str
    elotFlag: str
    elotNumber: str
    errorMessage: str
    ewsNoMatch: bool
    fipsCountyCode: str
    lacsLinkIndicator: str
    lacsLinkReturnCode: str
    pmbDesignator: str
    pmbNumber: str
    poBoxOnlyPostalCode: bool
    postOfficeCity: str
    postOfficeState: str
    standardizedAddress: GoogleMapsAddressvalidationV1UspsAddress
    suitelinkFootnote: str

@typing.type_check_only
class GoogleMapsAddressvalidationV1ValidateAddressRequest(
    typing_extensions.TypedDict, total=False
):
    address: GoogleTypePostalAddress
    enableUspsCass: bool
    languageOptions: GoogleMapsAddressvalidationV1LanguageOptions
    previousResponseId: str
    sessionToken: str

@typing.type_check_only
class GoogleMapsAddressvalidationV1ValidateAddressResponse(
    typing_extensions.TypedDict, total=False
):
    responseId: str
    result: GoogleMapsAddressvalidationV1ValidationResult

@typing.type_check_only
class GoogleMapsAddressvalidationV1ValidationResult(
    typing_extensions.TypedDict, total=False
):
    address: GoogleMapsAddressvalidationV1Address
    englishLatinAddress: GoogleMapsAddressvalidationV1Address
    geocode: GoogleMapsAddressvalidationV1Geocode
    metadata: GoogleMapsAddressvalidationV1AddressMetadata
    uspsData: GoogleMapsAddressvalidationV1UspsData
    verdict: GoogleMapsAddressvalidationV1Verdict

@typing.type_check_only
class GoogleMapsAddressvalidationV1Verdict(typing_extensions.TypedDict, total=False):
    addressComplete: bool
    geocodeGranularity: typing_extensions.Literal[
        "GRANULARITY_UNSPECIFIED",
        "SUB_PREMISE",
        "PREMISE",
        "PREMISE_PROXIMITY",
        "BLOCK",
        "ROUTE",
        "OTHER",
    ]
    hasInferredComponents: bool
    hasReplacedComponents: bool
    hasUnconfirmedComponents: bool
    inputGranularity: typing_extensions.Literal[
        "GRANULARITY_UNSPECIFIED",
        "SUB_PREMISE",
        "PREMISE",
        "PREMISE_PROXIMITY",
        "BLOCK",
        "ROUTE",
        "OTHER",
    ]
    validationGranularity: typing_extensions.Literal[
        "GRANULARITY_UNSPECIFIED",
        "SUB_PREMISE",
        "PREMISE",
        "PREMISE_PROXIMITY",
        "BLOCK",
        "ROUTE",
        "OTHER",
    ]

@typing.type_check_only
class GoogleTypeLatLng(typing_extensions.TypedDict, total=False):
    latitude: float
    longitude: float

@typing.type_check_only
class GoogleTypePostalAddress(typing_extensions.TypedDict, total=False):
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
