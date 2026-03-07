import typing

import typing_extensions

_list = list

@typing.type_check_only
class AdIdentifiers(typing_extensions.TypedDict, total=False):
    gbraid: str
    gclid: str
    landingPageDeviceInfo: DeviceInfo
    sessionAttributes: str
    wbraid: str

@typing.type_check_only
class AddressInfo(typing_extensions.TypedDict, total=False):
    familyName: str
    givenName: str
    postalCode: str
    regionCode: str

@typing.type_check_only
class AudienceMember(typing_extensions.TypedDict, total=False):
    consent: Consent
    destinationReferences: _list[str]
    mobileData: MobileData
    pairData: PairData
    ppidData: PpidData
    userData: UserData
    userIdData: UserIdData

@typing.type_check_only
class AwsWrappedKeyInfo(typing_extensions.TypedDict, total=False):
    encryptedDek: str
    kekUri: str
    keyType: typing_extensions.Literal["KEY_TYPE_UNSPECIFIED", "XCHACHA20_POLY1305"]
    roleArn: str

@typing.type_check_only
class Baseline(typing_extensions.TypedDict, total=False):
    baselineLocation: Location
    locationAutoDetectionEnabled: bool

@typing.type_check_only
class CartData(typing_extensions.TypedDict, total=False):
    items: _list[Item]
    merchantFeedLabel: str
    merchantFeedLanguageCode: str
    merchantId: str
    transactionDiscount: float

@typing.type_check_only
class Consent(typing_extensions.TypedDict, total=False):
    adPersonalization: typing_extensions.Literal[
        "CONSENT_STATUS_UNSPECIFIED", "CONSENT_GRANTED", "CONSENT_DENIED"
    ]
    adUserData: typing_extensions.Literal[
        "CONSENT_STATUS_UNSPECIFIED", "CONSENT_GRANTED", "CONSENT_DENIED"
    ]

@typing.type_check_only
class ContactIdInfo(typing_extensions.TypedDict, total=False):
    dataSourceType: typing_extensions.Literal[
        "DATA_SOURCE_TYPE_UNSPECIFIED",
        "DATA_SOURCE_TYPE_FIRST_PARTY",
        "DATA_SOURCE_TYPE_THIRD_PARTY_CREDIT_BUREAU",
        "DATA_SOURCE_TYPE_THIRD_PARTY_VOTER_FILE",
        "DATA_SOURCE_TYPE_THIRD_PARTY_PARTNER_DATA",
    ]
    matchRatePercentage: int

@typing.type_check_only
class CustomVariable(typing_extensions.TypedDict, total=False):
    destinationReferences: _list[str]
    value: str
    variable: str

@typing.type_check_only
class Destination(typing_extensions.TypedDict, total=False):
    linkedAccount: ProductAccount
    loginAccount: ProductAccount
    operatingAccount: ProductAccount
    productDestinationId: str
    reference: str

@typing.type_check_only
class DeviceInfo(typing_extensions.TypedDict, total=False):
    ipAddress: str
    userAgent: str

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class EncryptionInfo(typing_extensions.TypedDict, total=False):
    awsWrappedKeyInfo: AwsWrappedKeyInfo
    gcpWrappedKeyInfo: GcpWrappedKeyInfo

@typing.type_check_only
class ErrorCount(typing_extensions.TypedDict, total=False):
    reason: typing_extensions.Literal[
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
    ]
    recordCount: str

@typing.type_check_only
class ErrorInfo(typing_extensions.TypedDict, total=False):
    errorCounts: _list[ErrorCount]

@typing.type_check_only
class Event(typing_extensions.TypedDict, total=False):
    adIdentifiers: AdIdentifiers
    additionalEventParameters: _list[EventParameter]
    cartData: CartData
    clientId: str
    consent: Consent
    conversionValue: float
    currency: str
    customVariables: _list[CustomVariable]
    destinationReferences: _list[str]
    eventDeviceInfo: DeviceInfo
    eventName: str
    eventSource: typing_extensions.Literal[
        "EVENT_SOURCE_UNSPECIFIED", "WEB", "APP", "IN_STORE", "PHONE", "OTHER"
    ]
    eventTimestamp: str
    experimentalFields: _list[ExperimentalField]
    lastUpdatedTimestamp: str
    transactionId: str
    userData: UserData
    userId: str
    userProperties: UserProperties

@typing.type_check_only
class EventParameter(typing_extensions.TypedDict, total=False):
    parameterName: str
    value: str

@typing.type_check_only
class ExperimentalField(typing_extensions.TypedDict, total=False):
    field: str
    value: str

@typing.type_check_only
class GcpWrappedKeyInfo(typing_extensions.TypedDict, total=False):
    encryptedDek: str
    kekUri: str
    keyType: typing_extensions.Literal["KEY_TYPE_UNSPECIFIED", "XCHACHA20_POLY1305"]
    wipProvider: str

@typing.type_check_only
class IngestAudienceMembersRequest(typing_extensions.TypedDict, total=False):
    audienceMembers: _list[AudienceMember]
    consent: Consent
    destinations: _list[Destination]
    encoding: typing_extensions.Literal["ENCODING_UNSPECIFIED", "HEX", "BASE64"]
    encryptionInfo: EncryptionInfo
    termsOfService: TermsOfService
    validateOnly: bool

@typing.type_check_only
class IngestAudienceMembersResponse(typing_extensions.TypedDict, total=False):
    requestId: str

@typing.type_check_only
class IngestAudienceMembersStatus(typing_extensions.TypedDict, total=False):
    mobileDataIngestionStatus: IngestMobileDataStatus
    pairDataIngestionStatus: IngestPairDataStatus
    ppidDataIngestionStatus: IngestPpidDataStatus
    userDataIngestionStatus: IngestUserDataStatus
    userIdDataIngestionStatus: IngestUserIdDataStatus

@typing.type_check_only
class IngestEventsRequest(typing_extensions.TypedDict, total=False):
    consent: Consent
    destinations: _list[Destination]
    encoding: typing_extensions.Literal["ENCODING_UNSPECIFIED", "HEX", "BASE64"]
    encryptionInfo: EncryptionInfo
    events: _list[Event]
    validateOnly: bool

@typing.type_check_only
class IngestEventsResponse(typing_extensions.TypedDict, total=False):
    requestId: str

@typing.type_check_only
class IngestEventsStatus(typing_extensions.TypedDict, total=False):
    recordCount: str

@typing.type_check_only
class IngestMobileDataStatus(typing_extensions.TypedDict, total=False):
    mobileIdCount: str
    recordCount: str

@typing.type_check_only
class IngestPairDataStatus(typing_extensions.TypedDict, total=False):
    pairIdCount: str
    recordCount: str

@typing.type_check_only
class IngestPpidDataStatus(typing_extensions.TypedDict, total=False):
    ppidCount: str
    recordCount: str

@typing.type_check_only
class IngestUserDataStatus(typing_extensions.TypedDict, total=False):
    recordCount: str
    uploadMatchRateRange: typing_extensions.Literal[
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
class IngestUserIdDataStatus(typing_extensions.TypedDict, total=False):
    recordCount: str
    userIdCount: str

@typing.type_check_only
class IngestedUserListInfo(typing_extensions.TypedDict, total=False):
    contactIdInfo: ContactIdInfo
    mobileIdInfo: MobileIdInfo
    pairIdInfo: PairIdInfo
    partnerAudienceInfo: PartnerAudienceInfo
    pseudonymousIdInfo: PseudonymousIdInfo
    uploadKeyTypes: _list[
        typing_extensions.Literal[
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
class Item(typing_extensions.TypedDict, total=False):
    additionalItemParameters: _list[ItemParameter]
    itemId: str
    merchantProductId: str
    quantity: str
    unitPrice: float

@typing.type_check_only
class ItemParameter(typing_extensions.TypedDict, total=False):
    parameterName: str
    value: str

@typing.type_check_only
class ListUserListDirectLicensesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    userListDirectLicenses: _list[UserListDirectLicense]

@typing.type_check_only
class ListUserListGlobalLicenseCustomerInfosResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    userListGlobalLicenseCustomerInfos: _list[UserListGlobalLicenseCustomerInfo]

@typing.type_check_only
class ListUserListGlobalLicensesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    userListGlobalLicenses: _list[UserListGlobalLicense]

@typing.type_check_only
class ListUserListsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    userLists: _list[UserList]

@typing.type_check_only
class Location(typing_extensions.TypedDict, total=False):
    regionCodes: _list[str]

@typing.type_check_only
class MarketingDataInsight(typing_extensions.TypedDict, total=False):
    attributes: _list[MarketingDataInsightsAttribute]
    dimension: typing_extensions.Literal[
        "AUDIENCE_INSIGHTS_DIMENSION_UNSPECIFIED",
        "AUDIENCE_INSIGHTS_DIMENSION_UNKNOWN",
        "AFFINITY_USER_INTEREST",
        "IN_MARKET_USER_INTEREST",
        "AGE_RANGE",
        "GENDER",
    ]

@typing.type_check_only
class MarketingDataInsightsAttribute(typing_extensions.TypedDict, total=False):
    ageRange: typing_extensions.Literal[
        "AGE_RANGE_UNSPECIFIED",
        "AGE_RANGE_UNKNOWN",
        "AGE_RANGE_18_24",
        "AGE_RANGE_25_34",
        "AGE_RANGE_35_44",
        "AGE_RANGE_45_54",
        "AGE_RANGE_55_64",
        "AGE_RANGE_65_UP",
    ]
    gender: typing_extensions.Literal[
        "GENDER_UNSPECIFIED", "GENDER_UNKNOWN", "GENDER_MALE", "GENDER_FEMALE"
    ]
    lift: float
    userInterestId: str

@typing.type_check_only
class MobileData(typing_extensions.TypedDict, total=False):
    mobileIds: _list[str]

@typing.type_check_only
class MobileIdInfo(typing_extensions.TypedDict, total=False):
    appId: str
    dataSourceType: typing_extensions.Literal[
        "DATA_SOURCE_TYPE_UNSPECIFIED",
        "DATA_SOURCE_TYPE_FIRST_PARTY",
        "DATA_SOURCE_TYPE_THIRD_PARTY_CREDIT_BUREAU",
        "DATA_SOURCE_TYPE_THIRD_PARTY_VOTER_FILE",
        "DATA_SOURCE_TYPE_THIRD_PARTY_PARTNER_DATA",
    ]
    keySpace: typing_extensions.Literal["KEY_SPACE_UNSPECIFIED", "IOS", "ANDROID"]

@typing.type_check_only
class PairData(typing_extensions.TypedDict, total=False):
    pairIds: _list[str]

@typing.type_check_only
class PairIdInfo(typing_extensions.TypedDict, total=False):
    advertiserIdentifierCount: str
    cleanRoomIdentifier: str
    matchRatePercentage: int
    publisherId: str
    publisherName: str

@typing.type_check_only
class PartnerAudienceInfo(typing_extensions.TypedDict, total=False):
    commercePartner: str
    partnerAudienceSource: typing_extensions.Literal[
        "PARTNER_AUDIENCE_SOURCE_UNSPECIFIED",
        "COMMERCE_AUDIENCE",
        "LINEAR_TV_AUDIENCE",
        "AGENCY_PROVIDER_AUDIENCE",
    ]

@typing.type_check_only
class PartnerLink(typing_extensions.TypedDict, total=False):
    name: str
    owningAccount: ProductAccount
    partnerAccount: ProductAccount
    partnerLinkId: str

@typing.type_check_only
class PpidData(typing_extensions.TypedDict, total=False):
    ppids: _list[str]

@typing.type_check_only
class ProductAccount(typing_extensions.TypedDict, total=False):
    accountId: str
    accountType: typing_extensions.Literal[
        "ACCOUNT_TYPE_UNSPECIFIED",
        "GOOGLE_ADS",
        "DISPLAY_VIDEO_PARTNER",
        "DISPLAY_VIDEO_ADVERTISER",
        "DATA_PARTNER",
        "GOOGLE_ANALYTICS_PROPERTY",
        "GOOGLE_AD_MANAGER_AUDIENCE_LINK",
    ]
    product: typing_extensions.Literal[
        "PRODUCT_UNSPECIFIED",
        "GOOGLE_ADS",
        "DISPLAY_VIDEO_PARTNER",
        "DISPLAY_VIDEO_ADVERTISER",
        "DATA_PARTNER",
    ]

@typing.type_check_only
class PseudonymousIdInfo(typing_extensions.TypedDict, total=False):
    billableRecordCount: str
    syncStatus: typing_extensions.Literal[
        "SYNC_STATUS_UNSPECIFIED", "CREATED", "READY_FOR_USE", "FAILED"
    ]

@typing.type_check_only
class RemoveAudienceMembersRequest(typing_extensions.TypedDict, total=False):
    audienceMembers: _list[AudienceMember]
    destinations: _list[Destination]
    encoding: typing_extensions.Literal["ENCODING_UNSPECIFIED", "HEX", "BASE64"]
    encryptionInfo: EncryptionInfo
    validateOnly: bool

@typing.type_check_only
class RemoveAudienceMembersResponse(typing_extensions.TypedDict, total=False):
    requestId: str

@typing.type_check_only
class RemoveAudienceMembersStatus(typing_extensions.TypedDict, total=False):
    mobileDataRemovalStatus: RemoveMobileDataStatus
    pairDataRemovalStatus: RemovePairDataStatus
    ppidDataRemovalStatus: RemovePpidDataStatus
    userDataRemovalStatus: RemoveUserDataStatus
    userIdDataRemovalStatus: RemoveUserIdDataStatus

@typing.type_check_only
class RemoveMobileDataStatus(typing_extensions.TypedDict, total=False):
    mobileIdCount: str
    recordCount: str

@typing.type_check_only
class RemovePairDataStatus(typing_extensions.TypedDict, total=False):
    pairIdCount: str
    recordCount: str

@typing.type_check_only
class RemovePpidDataStatus(typing_extensions.TypedDict, total=False):
    ppidCount: str
    recordCount: str

@typing.type_check_only
class RemoveUserDataStatus(typing_extensions.TypedDict, total=False):
    recordCount: str
    userIdentifierCount: str

@typing.type_check_only
class RemoveUserIdDataStatus(typing_extensions.TypedDict, total=False):
    recordCount: str
    userIdCount: str

@typing.type_check_only
class RequestStatusPerDestination(typing_extensions.TypedDict, total=False):
    audienceMembersIngestionStatus: IngestAudienceMembersStatus
    audienceMembersRemovalStatus: RemoveAudienceMembersStatus
    destination: Destination
    errorInfo: ErrorInfo
    eventsIngestionStatus: IngestEventsStatus
    requestStatus: typing_extensions.Literal[
        "REQUEST_STATUS_UNKNOWN", "SUCCESS", "PROCESSING", "FAILED", "PARTIAL_SUCCESS"
    ]
    warningInfo: WarningInfo

@typing.type_check_only
class RetrieveInsightsRequest(typing_extensions.TypedDict, total=False):
    baseline: Baseline
    userListId: str

@typing.type_check_only
class RetrieveInsightsResponse(typing_extensions.TypedDict, total=False):
    marketingDataInsights: _list[MarketingDataInsight]

@typing.type_check_only
class RetrieveRequestStatusResponse(typing_extensions.TypedDict, total=False):
    requestStatusPerDestination: _list[RequestStatusPerDestination]

@typing.type_check_only
class SearchPartnerLinksResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    partnerLinks: _list[PartnerLink]

@typing.type_check_only
class SizeInfo(typing_extensions.TypedDict, total=False):
    displayNetworkMembersCount: str
    searchNetworkMembersCount: str

@typing.type_check_only
class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class TargetNetworkInfo(typing_extensions.TypedDict, total=False):
    eligibleForDisplay: bool
    eligibleForSearch: bool

@typing.type_check_only
class TermsOfService(typing_extensions.TypedDict, total=False):
    customerMatchTermsOfServiceStatus: typing_extensions.Literal[
        "TERMS_OF_SERVICE_STATUS_UNSPECIFIED", "ACCEPTED", "REJECTED"
    ]

@typing.type_check_only
class UserData(typing_extensions.TypedDict, total=False):
    userIdentifiers: _list[UserIdentifier]

@typing.type_check_only
class UserIdData(typing_extensions.TypedDict, total=False):
    userId: str

@typing.type_check_only
class UserIdInfo(typing_extensions.TypedDict, total=False):
    dataSourceType: typing_extensions.Literal[
        "DATA_SOURCE_TYPE_UNSPECIFIED",
        "DATA_SOURCE_TYPE_FIRST_PARTY",
        "DATA_SOURCE_TYPE_THIRD_PARTY_CREDIT_BUREAU",
        "DATA_SOURCE_TYPE_THIRD_PARTY_VOTER_FILE",
        "DATA_SOURCE_TYPE_THIRD_PARTY_PARTNER_DATA",
    ]

@typing.type_check_only
class UserIdentifier(typing_extensions.TypedDict, total=False):
    address: AddressInfo
    emailAddress: str
    phoneNumber: str

@typing.type_check_only
class UserList(typing_extensions.TypedDict, total=False):
    accessReason: typing_extensions.Literal[
        "ACCESS_REASON_UNSPECIFIED",
        "OWNED",
        "SHARED",
        "LICENSED",
        "SUBSCRIBED",
        "AFFILIATED",
    ]
    accountAccessStatus: typing_extensions.Literal[
        "ACCESS_STATUS_UNSPECIFIED", "ENABLED", "DISABLED"
    ]
    closingReason: typing_extensions.Literal["CLOSING_REASON_UNSPECIFIED", "UNUSED"]
    description: str
    displayName: str
    id: str
    ingestedUserListInfo: IngestedUserListInfo
    integrationCode: str
    membershipDuration: str
    membershipStatus: typing_extensions.Literal[
        "MEMBERSHIP_STATUS_UNSPECIFIED", "OPEN", "CLOSED"
    ]
    name: str
    readOnly: bool
    sizeInfo: SizeInfo
    targetNetworkInfo: TargetNetworkInfo

@typing.type_check_only
class UserListDirectLicense(typing_extensions.TypedDict, total=False):
    clientAccountDisplayName: str
    clientAccountId: str
    clientAccountType: typing_extensions.Literal[
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
    status: typing_extensions.Literal[
        "USER_LIST_LICENSE_STATUS_UNSPECIFIED",
        "USER_LIST_LICENSE_STATUS_ENABLED",
        "USER_LIST_LICENSE_STATUS_DISABLED",
    ]
    userListDisplayName: str
    userListId: str

@typing.type_check_only
class UserListGlobalLicense(typing_extensions.TypedDict, total=False):
    historicalPricings: _list[UserListLicensePricing]
    licenseType: typing_extensions.Literal[
        "USER_LIST_GLOBAL_LICENSE_TYPE_UNSPECIFIED",
        "USER_LIST_GLOBAL_LICENSE_TYPE_RESELLER",
        "USER_LIST_GLOBAL_LICENSE_TYPE_DATA_MART_SELL_SIDE",
        "USER_LIST_GLOBAL_LICENSE_TYPE_DATA_MART_BUY_SIDE",
    ]
    metrics: UserListLicenseMetrics
    name: str
    pricing: UserListLicensePricing
    status: typing_extensions.Literal[
        "USER_LIST_LICENSE_STATUS_UNSPECIFIED",
        "USER_LIST_LICENSE_STATUS_ENABLED",
        "USER_LIST_LICENSE_STATUS_DISABLED",
    ]
    userListDisplayName: str
    userListId: str

@typing.type_check_only
class UserListGlobalLicenseCustomerInfo(typing_extensions.TypedDict, total=False):
    clientAccountDisplayName: str
    clientAccountId: str
    clientAccountType: typing_extensions.Literal[
        "USER_LIST_LICENSE_CLIENT_ACCOUNT_TYPE_UNKNOWN",
        "USER_LIST_LICENSE_CLIENT_ACCOUNT_TYPE_GOOGLE_ADS",
        "USER_LIST_LICENSE_CLIENT_ACCOUNT_TYPE_DISPLAY_VIDEO_PARTNER",
        "USER_LIST_LICENSE_CLIENT_ACCOUNT_TYPE_DISPLAY_VIDEO_ADVERTISER",
        "USER_LIST_LICENSE_CLIENT_ACCOUNT_TYPE_GOOGLE_AD_MANAGER_AUDIENCE_LINK",
    ]
    historicalPricings: _list[UserListLicensePricing]
    licenseType: typing_extensions.Literal[
        "USER_LIST_GLOBAL_LICENSE_TYPE_UNSPECIFIED",
        "USER_LIST_GLOBAL_LICENSE_TYPE_RESELLER",
        "USER_LIST_GLOBAL_LICENSE_TYPE_DATA_MART_SELL_SIDE",
        "USER_LIST_GLOBAL_LICENSE_TYPE_DATA_MART_BUY_SIDE",
    ]
    metrics: UserListLicenseMetrics
    name: str
    pricing: UserListLicensePricing
    status: typing_extensions.Literal[
        "USER_LIST_LICENSE_STATUS_UNSPECIFIED",
        "USER_LIST_LICENSE_STATUS_ENABLED",
        "USER_LIST_LICENSE_STATUS_DISABLED",
    ]
    userListDisplayName: str
    userListId: str

@typing.type_check_only
class UserListLicenseMetrics(typing_extensions.TypedDict, total=False):
    clickCount: str
    endDate: str
    impressionCount: str
    revenueUsdMicros: str
    startDate: str

@typing.type_check_only
class UserListLicensePricing(typing_extensions.TypedDict, total=False):
    buyerApprovalState: typing_extensions.Literal[
        "USER_LIST_PRICING_BUYER_APPROVAL_STATE_UNSPECIFIED",
        "PENDING",
        "APPROVED",
        "REJECTED",
    ]
    costMicros: str
    costType: typing_extensions.Literal[
        "USER_LIST_PRICING_COST_TYPE_UNSPECIFIED", "CPC", "CPM", "MEDIA_SHARE"
    ]
    currencyCode: str
    endTime: str
    maxCostMicros: str
    pricingActive: bool
    pricingId: str
    startTime: str

@typing.type_check_only
class UserProperties(typing_extensions.TypedDict, total=False):
    additionalUserProperties: _list[UserProperty]
    customerType: typing_extensions.Literal[
        "CUSTOMER_TYPE_UNSPECIFIED", "NEW", "RETURNING", "REENGAGED"
    ]
    customerValueBucket: typing_extensions.Literal[
        "CUSTOMER_VALUE_BUCKET_UNSPECIFIED", "LOW", "MEDIUM", "HIGH"
    ]

@typing.type_check_only
class UserProperty(typing_extensions.TypedDict, total=False):
    propertyName: str
    value: str

@typing.type_check_only
class WarningCount(typing_extensions.TypedDict, total=False):
    reason: typing_extensions.Literal[
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
class WarningInfo(typing_extensions.TypedDict, total=False):
    warningCounts: _list[WarningCount]
