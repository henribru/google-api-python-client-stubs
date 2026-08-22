import typing

_list = list

@typing.type_check_only
class AdEvent(typing.TypedDict, total=False):
    adFormat: typing.Literal[
        "AD_FORMAT_UNSPECIFIED",
        "AD_FORMAT_AR",
        "AD_FORMAT_AUDIO",
        "AD_FORMAT_BANNER",
        "AD_FORMAT_BUMPER",
        "AD_FORMAT_CAROUSEL",
        "AD_FORMAT_COLLECTION",
        "AD_FORMAT_IMAGE",
        "AD_FORMAT_INTERACTIVE",
        "AD_FORMAT_INTERSTITIAL",
        "AD_FORMAT_IN_FEED",
        "AD_FORMAT_IN_STREAM",
        "AD_FORMAT_IN_STREAM_SKIPPABLE",
        "AD_FORMAT_IN_STREAM_NON_SKIPPABLE",
        "AD_FORMAT_NATIVE",
        "AD_FORMAT_SHORTS",
        "AD_FORMAT_STORY",
        "AD_FORMAT_SPONSORED",
        "AD_FORMAT_VIDEO",
    ]
    adFormatString: str
    adGroupId: str
    adHeight: int
    adId: str
    adPlacement: typing.Literal[
        "AD_PLACEMENT_UNSPECIFIED",
        "AD_PLACEMENT_DISCOVER",
        "AD_PLACEMENT_FEED",
        "AD_PLACEMENT_FOOTER",
        "AD_PLACEMENT_HEADER",
        "AD_PLACEMENT_HOME",
        "AD_PLACEMENT_IN_CONTENT",
        "AD_PLACEMENT_PROMOTED",
        "AD_PLACEMENT_SEARCH",
        "AD_PLACEMENT_STORY",
    ]
    adPlacementString: str
    adType: typing.Literal[
        "AD_TYPE_UNSPECIFIED",
        "AD_TYPE_DISPLAY",
        "AD_TYPE_TEXT",
        "AD_TYPE_IMAGE",
        "AD_TYPE_RICH_MEDIA",
        "AD_TYPE_HTML",
        "AD_TYPE_AUDIO",
        "AD_TYPE_VIDEO",
    ]
    adTypeString: str
    adWidth: int
    advertiserId: str
    attributionHint: typing.Literal[
        "ATTRIBUTION_HINT_UNSPECIFIED",
        "ATTRIBUTION_HINT_CONVERTED",
        "ATTRIBUTION_HINT_NOT_CONVERTED",
    ]
    campaignId: str
    campaignName: str
    deviceInfo: DeviceInfo
    eventId: str
    eventSubtype: typing.Literal[
        "EVENT_SUBTYPE_UNSPECIFIED",
        "EVENT_SUBTYPE_IMPRESSION",
        "EVENT_SUBTYPE_ENGAGED_VIEW",
        "EVENT_SUBTYPE_ONSITE_CLICK",
        "EVENT_SUBTYPE_OUTBOUND_CLICK",
    ]
    eventSubtypeString: str
    eventType: typing.Literal[
        "EVENT_TYPE_UNSPECIFIED", "EVENT_TYPE_VIEW", "EVENT_TYPE_CLICK"
    ]
    measurementAllowed: bool
    medium: str
    mobileDeviceId: str
    platform: typing.Literal[
        "PLATFORM_UNSPECIFIED", "PLATFORM_IOS", "PLATFORM_ANDROID", "PLATFORM_WEB"
    ]
    platformString: str
    platformType: typing.Literal[
        "PLATFORM_TYPE_UNSPECIFIED",
        "PLATFORM_TYPE_MOBILE",
        "PLATFORM_TYPE_DESKTOP",
        "PLATFORM_TYPE_CTV",
        "PLATFORM_TYPE_PHONE",
        "PLATFORM_TYPE_TABLET",
    ]
    platformTypeString: str
    regionCode: str
    source: str
    targetingType: typing.Literal[
        "TARGETING_TYPE_UNSPECIFIED",
        "TARGETING_TYPE_AUDIENCE",
        "TARGETING_TYPE_CONTEXTUAL",
        "TARGETING_TYPE_DEMOGRAPHIC",
        "TARGETING_TYPE_DEVICE",
        "TARGETING_TYPE_GEO",
        "TARGETING_TYPE_INTEREST",
        "TARGETING_TYPE_PURCHASE_INTENT",
        "TARGETING_TYPE_REMARKETING",
    ]
    targetingTypeString: str
    timestamp: str
    userData: UserData
    viewabilityInfo: ViewabilityInfo

@typing.type_check_only
class AdIdentifiers(typing.TypedDict, total=False):
    dclid: str
    encryptedUserIds: _list[EncryptedUserId]
    gbraid: str
    gclid: str
    impressionId: str
    landingPageDeviceInfo: DeviceInfo
    matchId: str
    mobileDeviceId: str
    sessionAttributes: str
    wbraid: str

@typing.type_check_only
class AddressInfo(typing.TypedDict, total=False):
    addressLine: str
    administrativeArea: str
    city: str
    familyName: str
    givenName: str
    postalCode: str
    regionCode: str

@typing.type_check_only
class AudienceMember(typing.TypedDict, total=False):
    compositeData: CompositeData
    consent: Consent
    destinationReferences: _list[str]
    googleUserIdData: GoogleUserIdData
    mobileData: MobileData
    pairData: PairData
    partnerProvidedIdData: PartnerProvidedIdData
    ppidData: PpidData
    userData: UserData
    userIdData: UserIdData

@typing.type_check_only
class AwsWrappedKeyInfo(typing.TypedDict, total=False):
    encryptedDek: str
    kekUri: str
    keyType: typing.Literal["KEY_TYPE_UNSPECIFIED", "XCHACHA20_POLY1305"]
    roleArn: str

@typing.type_check_only
class Baseline(typing.TypedDict, total=False):
    baselineLocation: Location
    locationAutoDetectionEnabled: bool

@typing.type_check_only
class CartData(typing.TypedDict, total=False):
    couponCodes: _list[str]
    items: _list[Item]
    merchantFeedLabel: str
    merchantFeedLanguageCode: str
    merchantId: str
    transactionDiscount: float

@typing.type_check_only
class CompositeData(typing.TypedDict, total=False):
    ipData: _list[IpData]
    userData: UserData

@typing.type_check_only
class Consent(typing.TypedDict, total=False):
    adPersonalization: typing.Literal[
        "CONSENT_STATUS_UNSPECIFIED", "CONSENT_GRANTED", "CONSENT_DENIED"
    ]
    adUserData: typing.Literal[
        "CONSENT_STATUS_UNSPECIFIED", "CONSENT_GRANTED", "CONSENT_DENIED"
    ]

@typing.type_check_only
class ContactIdInfo(typing.TypedDict, total=False):
    dataSourceType: typing.Literal[
        "DATA_SOURCE_TYPE_UNSPECIFIED",
        "DATA_SOURCE_TYPE_FIRST_PARTY",
        "DATA_SOURCE_TYPE_THIRD_PARTY_CREDIT_BUREAU",
        "DATA_SOURCE_TYPE_THIRD_PARTY_VOTER_FILE",
        "DATA_SOURCE_TYPE_THIRD_PARTY_PARTNER_DATA",
    ]
    matchRatePercentage: int

@typing.type_check_only
class CoordinatorKeyInfo(typing.TypedDict, total=False):
    keyId: str

@typing.type_check_only
class CustomVariable(typing.TypedDict, total=False):
    destinationReferences: _list[str]
    value: str
    variable: str

@typing.type_check_only
class DataTypeCount(typing.TypedDict, total=False):
    count: str
    type: typing.Literal[
        "DATA_TYPE_UNSPECIFIED", "EMAIL", "PHONE_NUMBER", "ADDRESS", "IP_ADDRESS"
    ]

@typing.type_check_only
class Destination(typing.TypedDict, total=False):
    linkedAccount: ProductAccount
    loginAccount: ProductAccount
    operatingAccount: ProductAccount
    productDestinationId: str
    reference: str

@typing.type_check_only
class DeviceInfo(typing.TypedDict, total=False):
    brand: str
    browser: str
    browserVersion: str
    category: str
    ipAddress: str
    languageCode: str
    model: str
    operatingSystem: str
    operatingSystemVersion: str
    screenHeight: int
    screenWidth: int
    userAgent: str

@typing.type_check_only
class Empty(typing.TypedDict, total=False): ...

@typing.type_check_only
class EncryptedUserId(typing.TypedDict, total=False):
    encryptedId: str
    entityId: str
    entityType: typing.Literal[
        "ENCRYPTION_ENTITY_TYPE_UNSPECIFIED",
        "CAMPAIGN_MANAGER_ACCOUNT",
        "CAMPAIGN_MANAGER_ADVERTISER",
        "DISPLAY_VIDEO_PARTNER",
        "DISPLAY_VIDEO_ADVERTISER",
        "GOOGLE_ADS_CUSTOMER",
        "GOOGLE_AD_MANAGER_NETWORK_CODE",
    ]
    source: typing.Literal[
        "ENCRYPTION_SOURCE_UNSPECIFIED", "AD_SERVING", "DATA_TRANSFER"
    ]

@typing.type_check_only
class EncryptionInfo(typing.TypedDict, total=False):
    awsWrappedKeyInfo: AwsWrappedKeyInfo
    coordinatorKeyInfo: CoordinatorKeyInfo
    gcpWrappedKeyInfo: GcpWrappedKeyInfo

@typing.type_check_only
class ErrorCount(typing.TypedDict, total=False):
    reason: typing.Literal[
        "PROCESSING_ERROR_REASON_UNSPECIFIED",
        "PROCESSING_ERROR_REASON_INVALID_CUSTOM_VARIABLE",
        "PROCESSING_ERROR_REASON_CUSTOM_VARIABLE_NOT_ENABLED",
        "PROCESSING_ERROR_REASON_EVENT_TOO_OLD",
        "PROCESSING_ERROR_REASON_DENIED_CONSENT",
        "PROCESSING_ERROR_REASON_NO_CONSENT",
        "PROCESSING_ERROR_REASON_UNKNOWN_CONSENT",
        "PROCESSING_ERROR_REASON_DUPLICATE_GCLID",
        "PROCESSING_ERROR_REASON_DUPLICATE_TRANSACTION_ID",
        "PROCESSING_ERROR_REASON_INVALID_GBRAID",
        "PROCESSING_ERROR_REASON_INVALID_GCLID",
        "PROCESSING_ERROR_REASON_INVALID_MERCHANT_ID",
        "PROCESSING_ERROR_REASON_INVALID_WBRAID",
        "PROCESSING_ERROR_REASON_INTERNAL_ERROR",
        "PROCESSING_ERROR_REASON_DESTINATION_ACCOUNT_ENHANCED_CONVERSIONS_TERMS_NOT_SIGNED",
        "PROCESSING_ERROR_REASON_INVALID_EVENT",
        "PROCESSING_ERROR_REASON_INSUFFICIENT_MATCHED_TRANSACTIONS",
        "PROCESSING_ERROR_REASON_INSUFFICIENT_TRANSACTIONS",
        "PROCESSING_ERROR_REASON_INVALID_FORMAT",
        "PROCESSING_ERROR_REASON_DECRYPTION_ERROR",
        "PROCESSING_ERROR_REASON_DEK_DECRYPTION_ERROR",
        "PROCESSING_ERROR_REASON_INVALID_WIP",
        "PROCESSING_ERROR_REASON_INVALID_KEK",
        "PROCESSING_ERROR_REASON_WIP_AUTH_FAILED",
        "PROCESSING_ERROR_REASON_KEK_PERMISSION_DENIED",
        "PROCESSING_ERROR_REASON_AWS_AUTH_FAILED",
        "PROCESSING_ERROR_REASON_USER_IDENTIFIER_DECRYPTION_ERROR",
        "PROCESSING_ERROR_OPERATING_ACCOUNT_MISMATCH_FOR_AD_IDENTIFIER",
        "PROCESSING_ERROR_REASON_ONE_PER_CLICK_CONVERSION_ACTION_NOT_PERMITTED_WITH_BRAID",
        "PROCESSING_ERROR_REASON_MATCH_ID_NOT_FOUND",
        "PROCESSING_ERROR_REASON_USER_ID_NOT_FOUND_FOR_MATCH_ID",
        "PROCESSING_ERROR_REASON_USER_ID_NOT_FOUND_FOR_GCLID",
        "PROCESSING_ERROR_REASON_USER_ID_NOT_FOUND_FOR_DCLID",
        "PROCESSING_ERROR_REASON_INVALID_AD_IDENTIFIERS",
        "PROCESSING_ERROR_REASON_INVALID_MOBILE_ID_FORMAT",
        "PROCESSING_ERROR_REASON_ORIGINAL_CONVERSIONS_NOT_FOUND",
        "PROCESSING_ERROR_REASON_EVENT_ID_DECODE_ERROR",
        "PROCESSING_ERROR_REASON_USER_ID_NOT_FOUND_FOR_IMPRESSION_ID",
        "PROCESSING_ERROR_REASON_USER_ID_NOT_FOUND",
        "PROCESSING_ERROR_REASON_CONVERSION_PRECEDES_CLICK",
        "PROCESSING_ERROR_REASON_TOO_RECENT_CLICK",
        "PROCESSING_ERROR_REASON_INVALID_CLICK",
        "PROCESSING_ERROR_REASON_INVALID_OPERATING_ACCOUNT_FOR_CLICK",
        "PROCESSING_ERROR_REASON_CLICK_NOT_FOUND",
        "PROCESSING_ERROR_REASON_EXTERNAL_ATTRIBUTION_DATA_MISSING",
    ]
    recordCount: str

@typing.type_check_only
class ErrorInfo(typing.TypedDict, total=False):
    errorCounts: _list[ErrorCount]

@typing.type_check_only
class Event(typing.TypedDict, total=False):
    adIdentifiers: AdIdentifiers
    additionalEventParameters: _list[EventParameter]
    appInstanceId: str
    cartData: CartData
    clientId: str
    consent: Consent
    conversionCount: float
    conversionValue: float
    currency: str
    customVariables: _list[CustomVariable]
    destinationReferences: _list[str]
    eventDeviceInfo: DeviceInfo
    eventLocation: EventLocation
    eventName: str
    eventSource: typing.Literal[
        "EVENT_SOURCE_UNSPECIFIED",
        "WEB",
        "APP",
        "IN_STORE",
        "PHONE",
        "MESSAGE",
        "OTHER",
    ]
    eventTimestamp: str
    experimentalFields: _list[ExperimentalField]
    lastUpdatedTimestamp: str
    thirdPartyUserData: UserData
    transactionId: str
    userData: UserData
    userId: str
    userProperties: UserProperties

@typing.type_check_only
class EventLocation(typing.TypedDict, total=False):
    city: str
    continentCode: str
    regionCode: str
    storeId: str
    subcontinentCode: str
    subdivisionCode: str

@typing.type_check_only
class EventParameter(typing.TypedDict, total=False):
    parameterName: str
    value: str

@typing.type_check_only
class ExperimentalField(typing.TypedDict, total=False):
    field: str
    value: str

@typing.type_check_only
class FieldWarning(typing.TypedDict, total=False):
    description: str
    field: str
    reason: typing.Literal[
        "WARNING_REASON_UNSPECIFIED",
        "WARNING_REASON_CUSTOM_VARIABLE_NOT_ENABLED",
        "WARNING_REASON_CUSTOM_VARIABLE_NOT_PREDEFINED",
        "WARNING_REASON_CART_DATA_NOT_SUPPORTED_WITH_GBRAID_OR_WBRAID",
        "WARNING_REASON_CART_DATA_ITEM_MERCHANT_PRODUCT_ID_MISSING",
        "WARNING_REASON_CART_DATA_ITEM_UNIT_PRICE_MISSING",
        "WARNING_REASON_GENERIC",
        "WARNING_REASON_INVALID_CLIENT_ID",
        "WARNING_REASON_INVALID_SUBDIVISION_CODE",
        "WARNING_REASON_INVALID_REGION_CODE",
        "WARNING_REASON_INVALID_SUBCONTINENT_CODE",
        "WARNING_REASON_INVALID_CONTINENT_CODE",
        "WARNING_REASON_INVALID_DEVICE_CATEGORY",
        "WARNING_REASON_INVALID_DEVICE_SCREEN_RESOLUTION",
        "WARNING_REASON_INVALID_MERCHANT_ID",
    ]

@typing.type_check_only
class GcpWrappedKeyInfo(typing.TypedDict, total=False):
    encryptedDek: str
    kekUri: str
    keyType: typing.Literal["KEY_TYPE_UNSPECIFIED", "XCHACHA20_POLY1305"]
    wipProvider: str

@typing.type_check_only
class GoogleUserIdData(typing.TypedDict, total=False):
    googleUserIds: _list[str]

@typing.type_check_only
class IngestAdEventsRequest(typing.TypedDict, total=False):
    adEvents: _list[AdEvent]
    encryptionInfo: EncryptionInfo
    validateOnly: bool

@typing.type_check_only
class IngestAdEventsResponse(typing.TypedDict, total=False): ...

@typing.type_check_only
class IngestAudienceMembersRequest(typing.TypedDict, total=False):
    audienceMembers: _list[AudienceMember]
    consent: Consent
    destinations: _list[Destination]
    encoding: typing.Literal["ENCODING_UNSPECIFIED", "HEX", "BASE64"]
    encryptionInfo: EncryptionInfo
    termsOfService: TermsOfService
    validateOnly: bool

@typing.type_check_only
class IngestAudienceMembersResponse(typing.TypedDict, total=False):
    fieldWarnings: _list[FieldWarning]
    requestId: str

@typing.type_check_only
class IngestAudienceMembersStatus(typing.TypedDict, total=False):
    compositeDataIngestionStatus: IngestCompositeDataStatus
    googleUserIdDataIngestionStatus: IngestGoogleUserIdDataStatus
    mobileDataIngestionStatus: IngestMobileDataStatus
    pairDataIngestionStatus: IngestPairDataStatus
    partnerProvidedIdDataIngestionStatus: IngestPartnerProvidedIdDataStatus
    ppidDataIngestionStatus: IngestPpidDataStatus
    userDataIngestionStatus: IngestUserDataStatus
    userIdDataIngestionStatus: IngestUserIdDataStatus

@typing.type_check_only
class IngestCompositeDataStatus(typing.TypedDict, total=False):
    dataTypeCounts: _list[DataTypeCount]
    recordCount: str
    uploadMatchRateRange: typing.Literal[
        "MATCH_RATE_RANGE_UNKNOWN",
        "MATCH_RATE_RANGE_NOT_ELIGIBLE",
        "MATCH_RATE_RANGE_LESS_THAN_20",
        "MATCH_RATE_RANGE_20_TO_30",
        "MATCH_RATE_RANGE_31_TO_40",
        "MATCH_RATE_RANGE_41_TO_50",
        "MATCH_RATE_RANGE_51_TO_60",
        "MATCH_RATE_RANGE_61_TO_70",
        "MATCH_RATE_RANGE_71_TO_80",
        "MATCH_RATE_RANGE_81_TO_90",
        "MATCH_RATE_RANGE_91_TO_100",
    ]

@typing.type_check_only
class IngestEventsRequest(typing.TypedDict, total=False):
    consent: Consent
    destinations: _list[Destination]
    encoding: typing.Literal["ENCODING_UNSPECIFIED", "HEX", "BASE64"]
    encryptionInfo: EncryptionInfo
    events: _list[Event]
    validateOnly: bool

@typing.type_check_only
class IngestEventsResponse(typing.TypedDict, total=False):
    fieldWarnings: _list[FieldWarning]
    requestId: str

@typing.type_check_only
class IngestEventsStatus(typing.TypedDict, total=False):
    recordCount: str

@typing.type_check_only
class IngestGoogleUserIdDataStatus(typing.TypedDict, total=False):
    googleUserIdCount: str
    recordCount: str

@typing.type_check_only
class IngestMobileDataStatus(typing.TypedDict, total=False):
    mobileIdCount: str
    recordCount: str

@typing.type_check_only
class IngestPairDataStatus(typing.TypedDict, total=False):
    pairIdCount: str
    recordCount: str

@typing.type_check_only
class IngestPartnerProvidedIdDataStatus(typing.TypedDict, total=False):
    partnerProvidedIdCount: str
    recordCount: str

@typing.type_check_only
class IngestPpidDataStatus(typing.TypedDict, total=False):
    ppidCount: str
    recordCount: str

@typing.type_check_only
class IngestUserDataStatus(typing.TypedDict, total=False):
    recordCount: str
    uploadMatchRateRange: typing.Literal[
        "MATCH_RATE_RANGE_UNKNOWN",
        "MATCH_RATE_RANGE_NOT_ELIGIBLE",
        "MATCH_RATE_RANGE_LESS_THAN_20",
        "MATCH_RATE_RANGE_20_TO_30",
        "MATCH_RATE_RANGE_31_TO_40",
        "MATCH_RATE_RANGE_41_TO_50",
        "MATCH_RATE_RANGE_51_TO_60",
        "MATCH_RATE_RANGE_61_TO_70",
        "MATCH_RATE_RANGE_71_TO_80",
        "MATCH_RATE_RANGE_81_TO_90",
        "MATCH_RATE_RANGE_91_TO_100",
    ]
    userIdentifierCount: str

@typing.type_check_only
class IngestUserIdDataStatus(typing.TypedDict, total=False):
    recordCount: str
    userIdCount: str

@typing.type_check_only
class IngestedUserListInfo(typing.TypedDict, total=False):
    contactIdInfo: ContactIdInfo
    mobileIdInfo: MobileIdInfo
    pairIdInfo: PairIdInfo
    partnerAudienceInfo: PartnerAudienceInfo
    pseudonymousIdInfo: PseudonymousIdInfo
    uploadKeyTypes: _list[
        typing.Literal[
            "UPLOAD_KEY_TYPE_UNSPECIFIED",
            "CONTACT_ID",
            "MOBILE_ID",
            "USER_ID",
            "PAIR_ID",
            "PSEUDONYMOUS_ID",
        ]
    ]
    userIdInfo: UserIdInfo

@typing.type_check_only
class IpData(typing.TypedDict, total=False):
    ipAddress: str
    observeEndTime: str
    observeStartTime: str

@typing.type_check_only
class Item(typing.TypedDict, total=False):
    additionalItemParameters: _list[ItemParameter]
    conversionValue: float
    customVariables: _list[ItemCustomVariable]
    itemId: str
    merchantFeedLabel: str
    merchantFeedLanguageCode: str
    merchantId: str
    merchantProductId: str
    quantity: str
    unitPrice: float

@typing.type_check_only
class ItemCustomVariable(typing.TypedDict, total=False):
    destinationReferences: _list[str]
    value: str
    variable: str

@typing.type_check_only
class ItemParameter(typing.TypedDict, total=False):
    parameterName: str
    value: str

@typing.type_check_only
class ListUserListDirectLicensesResponse(typing.TypedDict, total=False):
    nextPageToken: str
    userListDirectLicenses: _list[UserListDirectLicense]

@typing.type_check_only
class ListUserListGlobalLicenseCustomerInfosResponse(typing.TypedDict, total=False):
    nextPageToken: str
    userListGlobalLicenseCustomerInfos: _list[UserListGlobalLicenseCustomerInfo]

@typing.type_check_only
class ListUserListGlobalLicensesResponse(typing.TypedDict, total=False):
    nextPageToken: str
    userListGlobalLicenses: _list[UserListGlobalLicense]

@typing.type_check_only
class ListUserListsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    userLists: _list[UserList]

@typing.type_check_only
class Location(typing.TypedDict, total=False):
    regionCodes: _list[str]

@typing.type_check_only
class MarketingDataInsight(typing.TypedDict, total=False):
    attributes: _list[MarketingDataInsightsAttribute]
    dimension: typing.Literal[
        "AUDIENCE_INSIGHTS_DIMENSION_UNSPECIFIED",
        "AUDIENCE_INSIGHTS_DIMENSION_UNKNOWN",
        "AFFINITY_USER_INTEREST",
        "IN_MARKET_USER_INTEREST",
        "AGE_RANGE",
        "GENDER",
    ]

@typing.type_check_only
class MarketingDataInsightsAttribute(typing.TypedDict, total=False):
    ageRange: typing.Literal[
        "AGE_RANGE_UNSPECIFIED",
        "AGE_RANGE_UNKNOWN",
        "AGE_RANGE_18_24",
        "AGE_RANGE_25_34",
        "AGE_RANGE_35_44",
        "AGE_RANGE_45_54",
        "AGE_RANGE_55_64",
        "AGE_RANGE_65_UP",
    ]
    gender: typing.Literal[
        "GENDER_UNSPECIFIED", "GENDER_UNKNOWN", "GENDER_MALE", "GENDER_FEMALE"
    ]
    lift: float
    userInterestId: str

@typing.type_check_only
class MobileData(typing.TypedDict, total=False):
    mobileIds: _list[str]

@typing.type_check_only
class MobileIdInfo(typing.TypedDict, total=False):
    appId: str
    dataSourceType: typing.Literal[
        "DATA_SOURCE_TYPE_UNSPECIFIED",
        "DATA_SOURCE_TYPE_FIRST_PARTY",
        "DATA_SOURCE_TYPE_THIRD_PARTY_CREDIT_BUREAU",
        "DATA_SOURCE_TYPE_THIRD_PARTY_VOTER_FILE",
        "DATA_SOURCE_TYPE_THIRD_PARTY_PARTNER_DATA",
    ]
    keySpace: typing.Literal["KEY_SPACE_UNSPECIFIED", "IOS", "ANDROID"]

@typing.type_check_only
class PairData(typing.TypedDict, total=False):
    pairIds: _list[str]

@typing.type_check_only
class PairIdInfo(typing.TypedDict, total=False):
    advertiserIdentifierCount: str
    cleanRoomIdentifier: str
    matchRatePercentage: int
    publisherId: str
    publisherName: str

@typing.type_check_only
class PartnerAudienceInfo(typing.TypedDict, total=False):
    commercePartner: str
    partnerAudienceSource: typing.Literal[
        "PARTNER_AUDIENCE_SOURCE_UNSPECIFIED",
        "COMMERCE_AUDIENCE",
        "LINEAR_TV_AUDIENCE",
        "AGENCY_PROVIDER_AUDIENCE",
    ]

@typing.type_check_only
class PartnerCustomerAccount(typing.TypedDict, total=False):
    accountId: str
    accountName: str
    accountType: str

@typing.type_check_only
class PartnerLink(typing.TypedDict, total=False):
    featureSet: typing.Literal[
        "FEATURE_SET_UNSPECIFIED",
        "FEATURE_SET_AUDIENCE_AND_EVENT_MANAGEMENT",
        "FEATURE_SET_AD_EVENT_MANAGEMENT",
    ]
    name: str
    owningAccount: ProductAccount
    partnerAccount: ProductAccount
    partnerCustomerAccount: PartnerCustomerAccount
    partnerLinkId: str
    partnerLinkMetadata: PartnerLinkMetadata

@typing.type_check_only
class PartnerLinkMetadata(typing.TypedDict, total=False):
    implicitAccounts: _list[PartnerCustomerAccount]

@typing.type_check_only
class PartnerProvidedIdData(typing.TypedDict, total=False):
    partnerProvidedIds: _list[str]

@typing.type_check_only
class PpidData(typing.TypedDict, total=False):
    ppids: _list[str]

@typing.type_check_only
class ProductAccount(typing.TypedDict, total=False):
    accountId: str
    accountType: typing.Literal[
        "ACCOUNT_TYPE_UNSPECIFIED",
        "GOOGLE_ADS",
        "DISPLAY_VIDEO_PARTNER",
        "DISPLAY_VIDEO_ADVERTISER",
        "DATA_PARTNER",
        "GOOGLE_ANALYTICS_PROPERTY",
        "GOOGLE_AD_MANAGER_AUDIENCE_LINK",
        "FLOODLIGHT_CONFIG",
    ]
    product: typing.Literal[
        "PRODUCT_UNSPECIFIED",
        "GOOGLE_ADS",
        "DISPLAY_VIDEO_PARTNER",
        "DISPLAY_VIDEO_ADVERTISER",
        "DATA_PARTNER",
    ]

@typing.type_check_only
class PseudonymousIdInfo(typing.TypedDict, total=False):
    billableRecordCount: str
    syncStatus: typing.Literal[
        "SYNC_STATUS_UNSPECIFIED", "CREATED", "READY_FOR_USE", "FAILED"
    ]

@typing.type_check_only
class RemoveAllAudienceMembersRequest(typing.TypedDict, total=False):
    destinations: _list[Destination]
    removeAsOfTime: str
    validateOnly: bool

@typing.type_check_only
class RemoveAllAudienceMembersResponse(typing.TypedDict, total=False):
    requestId: str

@typing.type_check_only
class RemoveAllAudienceMembersStatus(typing.TypedDict, total=False): ...

@typing.type_check_only
class RemoveAudienceMembersRequest(typing.TypedDict, total=False):
    audienceMembers: _list[AudienceMember]
    destinations: _list[Destination]
    encoding: typing.Literal["ENCODING_UNSPECIFIED", "HEX", "BASE64"]
    encryptionInfo: EncryptionInfo
    validateOnly: bool

@typing.type_check_only
class RemoveAudienceMembersResponse(typing.TypedDict, total=False):
    requestId: str

@typing.type_check_only
class RemoveAudienceMembersStatus(typing.TypedDict, total=False):
    compositeDataRemovalStatus: RemoveCompositeDataStatus
    googleUserIdDataRemovalStatus: RemoveGoogleUserIdDataStatus
    mobileDataRemovalStatus: RemoveMobileDataStatus
    pairDataRemovalStatus: RemovePairDataStatus
    partnerProvidedIdDataRemovalStatus: RemovePartnerProvidedIdDataStatus
    ppidDataRemovalStatus: RemovePpidDataStatus
    userDataRemovalStatus: RemoveUserDataStatus
    userIdDataRemovalStatus: RemoveUserIdDataStatus

@typing.type_check_only
class RemoveCompositeDataStatus(typing.TypedDict, total=False):
    dataTypeCounts: _list[DataTypeCount]
    recordCount: str

@typing.type_check_only
class RemoveGoogleUserIdDataStatus(typing.TypedDict, total=False):
    googleUserIdCount: str
    recordCount: str

@typing.type_check_only
class RemoveMobileDataStatus(typing.TypedDict, total=False):
    mobileIdCount: str
    recordCount: str

@typing.type_check_only
class RemovePairDataStatus(typing.TypedDict, total=False):
    pairIdCount: str
    recordCount: str

@typing.type_check_only
class RemovePartnerProvidedIdDataStatus(typing.TypedDict, total=False):
    partnerProvidedIdCount: str
    recordCount: str

@typing.type_check_only
class RemovePpidDataStatus(typing.TypedDict, total=False):
    ppidCount: str
    recordCount: str

@typing.type_check_only
class RemoveUserDataStatus(typing.TypedDict, total=False):
    recordCount: str
    userIdentifierCount: str

@typing.type_check_only
class RemoveUserIdDataStatus(typing.TypedDict, total=False):
    recordCount: str
    userIdCount: str

@typing.type_check_only
class RequestStatusPerDestination(typing.TypedDict, total=False):
    audienceMembersIngestionStatus: IngestAudienceMembersStatus
    audienceMembersRemovalStatus: RemoveAudienceMembersStatus
    destination: Destination
    errorInfo: ErrorInfo
    eventsIngestionStatus: IngestEventsStatus
    removeAllAudienceMembersStatus: RemoveAllAudienceMembersStatus
    requestStatus: typing.Literal[
        "REQUEST_STATUS_UNKNOWN", "SUCCESS", "PROCESSING", "FAILED", "PARTIAL_SUCCESS"
    ]
    warningInfo: WarningInfo

@typing.type_check_only
class RetrieveInsightsRequest(typing.TypedDict, total=False):
    baseline: Baseline
    userListId: str

@typing.type_check_only
class RetrieveInsightsResponse(typing.TypedDict, total=False):
    marketingDataInsights: _list[MarketingDataInsight]

@typing.type_check_only
class RetrieveRequestStatusResponse(typing.TypedDict, total=False):
    requestStatusPerDestination: _list[RequestStatusPerDestination]

@typing.type_check_only
class SearchPartnerLinksResponse(typing.TypedDict, total=False):
    nextPageToken: str
    partnerLinks: _list[PartnerLink]

@typing.type_check_only
class SizeInfo(typing.TypedDict, total=False):
    displayNetworkMembersCount: str
    gmailMembersCount: str
    searchNetworkMembersCount: str
    youtubeMembersCount: str

@typing.type_check_only
class Status(typing.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class TargetNetworkInfo(typing.TypedDict, total=False):
    eligibleForDisplay: bool
    eligibleForSearch: bool

@typing.type_check_only
class TermsOfService(typing.TypedDict, total=False):
    customerMatchTermsOfServiceStatus: typing.Literal[
        "TERMS_OF_SERVICE_STATUS_UNSPECIFIED", "ACCEPTED", "REJECTED"
    ]

@typing.type_check_only
class UserData(typing.TypedDict, total=False):
    userIdentifiers: _list[UserIdentifier]

@typing.type_check_only
class UserIdData(typing.TypedDict, total=False):
    userId: str

@typing.type_check_only
class UserIdInfo(typing.TypedDict, total=False):
    dataSourceType: typing.Literal[
        "DATA_SOURCE_TYPE_UNSPECIFIED",
        "DATA_SOURCE_TYPE_FIRST_PARTY",
        "DATA_SOURCE_TYPE_THIRD_PARTY_CREDIT_BUREAU",
        "DATA_SOURCE_TYPE_THIRD_PARTY_VOTER_FILE",
        "DATA_SOURCE_TYPE_THIRD_PARTY_PARTNER_DATA",
    ]

@typing.type_check_only
class UserIdentifier(typing.TypedDict, total=False):
    address: AddressInfo
    emailAddress: str
    phoneNumber: str

@typing.type_check_only
class UserList(typing.TypedDict, total=False):
    accessReason: typing.Literal[
        "ACCESS_REASON_UNSPECIFIED",
        "OWNED",
        "SHARED",
        "LICENSED",
        "SUBSCRIBED",
        "AFFILIATED",
    ]
    accountAccessStatus: typing.Literal[
        "ACCESS_STATUS_UNSPECIFIED", "ENABLED", "DISABLED"
    ]
    closingReason: typing.Literal["CLOSING_REASON_UNSPECIFIED", "UNUSED"]
    description: str
    displayName: str
    id: str
    ingestedUserListInfo: IngestedUserListInfo
    integrationCode: str
    membershipDuration: str
    membershipStatus: typing.Literal["MEMBERSHIP_STATUS_UNSPECIFIED", "OPEN", "CLOSED"]
    name: str
    readOnly: bool
    sizeInfo: SizeInfo
    targetNetworkInfo: TargetNetworkInfo

@typing.type_check_only
class UserListDirectLicense(typing.TypedDict, total=False):
    clientAccountDisplayName: str
    clientAccountId: str
    clientAccountType: typing.Literal[
        "USER_LIST_LICENSE_CLIENT_ACCOUNT_TYPE_UNKNOWN",
        "USER_LIST_LICENSE_CLIENT_ACCOUNT_TYPE_GOOGLE_ADS",
        "USER_LIST_LICENSE_CLIENT_ACCOUNT_TYPE_DISPLAY_VIDEO_PARTNER",
        "USER_LIST_LICENSE_CLIENT_ACCOUNT_TYPE_DISPLAY_VIDEO_ADVERTISER",
        "USER_LIST_LICENSE_CLIENT_ACCOUNT_TYPE_GOOGLE_AD_MANAGER_AUDIENCE_LINK",
    ]
    historicalPricings: _list[UserListLicensePricing]
    metrics: UserListLicenseMetrics
    name: str
    pricing: UserListLicensePricing
    status: typing.Literal[
        "USER_LIST_LICENSE_STATUS_UNSPECIFIED",
        "USER_LIST_LICENSE_STATUS_ENABLED",
        "USER_LIST_LICENSE_STATUS_DISABLED",
    ]
    userListDisplayName: str
    userListId: str

@typing.type_check_only
class UserListGlobalLicense(typing.TypedDict, total=False):
    historicalPricings: _list[UserListLicensePricing]
    licenseType: typing.Literal[
        "USER_LIST_GLOBAL_LICENSE_TYPE_UNSPECIFIED",
        "USER_LIST_GLOBAL_LICENSE_TYPE_RESELLER",
        "USER_LIST_GLOBAL_LICENSE_TYPE_DATA_MART_SELL_SIDE",
        "USER_LIST_GLOBAL_LICENSE_TYPE_DATA_MART_BUY_SIDE",
    ]
    metrics: UserListLicenseMetrics
    name: str
    pricing: UserListLicensePricing
    status: typing.Literal[
        "USER_LIST_LICENSE_STATUS_UNSPECIFIED",
        "USER_LIST_LICENSE_STATUS_ENABLED",
        "USER_LIST_LICENSE_STATUS_DISABLED",
    ]
    userListDisplayName: str
    userListId: str

@typing.type_check_only
class UserListGlobalLicenseCustomerInfo(typing.TypedDict, total=False):
    clientAccountDisplayName: str
    clientAccountId: str
    clientAccountType: typing.Literal[
        "USER_LIST_LICENSE_CLIENT_ACCOUNT_TYPE_UNKNOWN",
        "USER_LIST_LICENSE_CLIENT_ACCOUNT_TYPE_GOOGLE_ADS",
        "USER_LIST_LICENSE_CLIENT_ACCOUNT_TYPE_DISPLAY_VIDEO_PARTNER",
        "USER_LIST_LICENSE_CLIENT_ACCOUNT_TYPE_DISPLAY_VIDEO_ADVERTISER",
        "USER_LIST_LICENSE_CLIENT_ACCOUNT_TYPE_GOOGLE_AD_MANAGER_AUDIENCE_LINK",
    ]
    historicalPricings: _list[UserListLicensePricing]
    licenseType: typing.Literal[
        "USER_LIST_GLOBAL_LICENSE_TYPE_UNSPECIFIED",
        "USER_LIST_GLOBAL_LICENSE_TYPE_RESELLER",
        "USER_LIST_GLOBAL_LICENSE_TYPE_DATA_MART_SELL_SIDE",
        "USER_LIST_GLOBAL_LICENSE_TYPE_DATA_MART_BUY_SIDE",
    ]
    metrics: UserListLicenseMetrics
    name: str
    pricing: UserListLicensePricing
    status: typing.Literal[
        "USER_LIST_LICENSE_STATUS_UNSPECIFIED",
        "USER_LIST_LICENSE_STATUS_ENABLED",
        "USER_LIST_LICENSE_STATUS_DISABLED",
    ]
    userListDisplayName: str
    userListId: str

@typing.type_check_only
class UserListLicenseMetrics(typing.TypedDict, total=False):
    clickCount: str
    endDate: str
    impressionCount: str
    revenueUsdMicros: str
    startDate: str

@typing.type_check_only
class UserListLicensePricing(typing.TypedDict, total=False):
    buyerApprovalState: typing.Literal[
        "USER_LIST_PRICING_BUYER_APPROVAL_STATE_UNSPECIFIED",
        "PENDING",
        "APPROVED",
        "REJECTED",
    ]
    costMicros: str
    costType: typing.Literal[
        "USER_LIST_PRICING_COST_TYPE_UNSPECIFIED", "CPC", "CPM", "MEDIA_SHARE"
    ]
    currencyCode: str
    endTime: str
    maxCostMicros: str
    pricingActive: bool
    pricingId: str
    startTime: str

@typing.type_check_only
class UserProperties(typing.TypedDict, total=False):
    additionalUserProperties: _list[UserProperty]
    customerType: typing.Literal[
        "CUSTOMER_TYPE_UNSPECIFIED", "NEW", "RETURNING", "REENGAGED"
    ]
    customerValueBucket: typing.Literal[
        "CUSTOMER_VALUE_BUCKET_UNSPECIFIED", "LOW", "MEDIUM", "HIGH"
    ]

@typing.type_check_only
class UserProperty(typing.TypedDict, total=False):
    propertyName: str
    value: str

@typing.type_check_only
class ViewabilityInfo(typing.TypedDict, total=False):
    mediaDuration: str
    mediaQuartile: typing.Literal[
        "MEDIA_QUARTILE_UNSPECIFIED",
        "MEDIA_QUARTILE_START",
        "MEDIA_QUARTILE_FIRST_QUARTILE",
        "MEDIA_QUARTILE_MIDPOINT",
        "MEDIA_QUARTILE_THIRD_QUARTILE",
        "MEDIA_QUARTILE_COMPLETE",
    ]
    mediaSkippable: bool
    mediaVolumePercent: int
    playbackDuration: str
    viewType: typing.Literal[
        "VIEW_TYPE_UNSPECIFIED", "VIEW_TYPE_MRC_VIEWED", "VIEW_TYPE_MRC_RENDERED"
    ]
    viewableDuration: str
    viewablePercent: int

@typing.type_check_only
class WarningCount(typing.TypedDict, total=False):
    reason: typing.Literal[
        "PROCESSING_WARNING_REASON_UNSPECIFIED",
        "PROCESSING_WARNING_REASON_KEK_PERMISSION_DENIED",
        "PROCESSING_WARNING_REASON_DEK_DECRYPTION_ERROR",
        "PROCESSING_WARNING_REASON_DECRYPTION_ERROR",
        "PROCESSING_WARNING_REASON_WIP_AUTH_FAILED",
        "PROCESSING_WARNING_REASON_INVALID_WIP",
        "PROCESSING_WARNING_REASON_INVALID_KEK",
        "PROCESSING_WARNING_REASON_USER_IDENTIFIER_DECRYPTION_ERROR",
        "PROCESSING_WARNING_REASON_INTERNAL_ERROR",
        "PROCESSING_WARNING_REASON_AWS_AUTH_FAILED",
    ]
    recordCount: str

@typing.type_check_only
class WarningInfo(typing.TypedDict, total=False):
    warningCounts: _list[WarningCount]
