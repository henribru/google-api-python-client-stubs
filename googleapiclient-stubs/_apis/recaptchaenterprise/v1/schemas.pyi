import typing

import typing_extensions

_list = list

@typing.type_check_only
class GoogleCloudRecaptchaenterpriseV1AccountDefenderAssessment(
    typing_extensions.TypedDict, total=False
):
    labels: _list[str]

@typing.type_check_only
class GoogleCloudRecaptchaenterpriseV1AccountVerificationInfo(
    typing_extensions.TypedDict, total=False
):
    endpoints: _list[GoogleCloudRecaptchaenterpriseV1EndpointVerificationInfo]
    languageCode: str
    latestVerificationResult: typing_extensions.Literal[
        "RESULT_UNSPECIFIED",
        "SUCCESS_USER_VERIFIED",
        "ERROR_USER_NOT_VERIFIED",
        "ERROR_SITE_ONBOARDING_INCOMPLETE",
        "ERROR_RECIPIENT_NOT_ALLOWED",
        "ERROR_RECIPIENT_ABUSE_LIMIT_EXHAUSTED",
        "ERROR_CRITICAL_INTERNAL",
        "ERROR_CUSTOMER_QUOTA_EXHAUSTED",
        "ERROR_VERIFICATION_BYPASSED",
        "ERROR_VERDICT_MISMATCH",
    ]
    username: str

@typing.type_check_only
class GoogleCloudRecaptchaenterpriseV1AndroidKeySettings(
    typing_extensions.TypedDict, total=False
):
    allowAllPackageNames: bool
    allowedPackageNames: _list[str]

@typing.type_check_only
class GoogleCloudRecaptchaenterpriseV1AnnotateAssessmentRequest(
    typing_extensions.TypedDict, total=False
):
    annotation: typing_extensions.Literal[
        "ANNOTATION_UNSPECIFIED",
        "LEGITIMATE",
        "FRAUDULENT",
        "PASSWORD_CORRECT",
        "PASSWORD_INCORRECT",
    ]
    hashedAccountId: str
    reasons: _list[str]
    transactionEvent: GoogleCloudRecaptchaenterpriseV1TransactionEvent

@typing.type_check_only
class GoogleCloudRecaptchaenterpriseV1AnnotateAssessmentResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudRecaptchaenterpriseV1Assessment(
    typing_extensions.TypedDict, total=False
):
    accountDefenderAssessment: GoogleCloudRecaptchaenterpriseV1AccountDefenderAssessment
    accountVerification: GoogleCloudRecaptchaenterpriseV1AccountVerificationInfo
    event: GoogleCloudRecaptchaenterpriseV1Event
    fraudPreventionAssessment: GoogleCloudRecaptchaenterpriseV1FraudPreventionAssessment
    name: str
    privatePasswordLeakVerification: GoogleCloudRecaptchaenterpriseV1PrivatePasswordLeakVerification
    riskAnalysis: GoogleCloudRecaptchaenterpriseV1RiskAnalysis
    tokenProperties: GoogleCloudRecaptchaenterpriseV1TokenProperties

@typing.type_check_only
class GoogleCloudRecaptchaenterpriseV1ChallengeMetrics(
    typing_extensions.TypedDict, total=False
):
    failedCount: str
    nocaptchaCount: str
    pageloadCount: str
    passedCount: str

@typing.type_check_only
class GoogleCloudRecaptchaenterpriseV1EndpointVerificationInfo(
    typing_extensions.TypedDict, total=False
):
    emailAddress: str
    lastVerificationTime: str
    phoneNumber: str
    requestToken: str

@typing.type_check_only
class GoogleCloudRecaptchaenterpriseV1Event(typing_extensions.TypedDict, total=False):
    expectedAction: str
    hashedAccountId: str
    siteKey: str
    token: str
    transactionData: GoogleCloudRecaptchaenterpriseV1TransactionData
    userAgent: str
    userIpAddress: str

@typing.type_check_only
class GoogleCloudRecaptchaenterpriseV1FraudPreventionAssessment(
    typing_extensions.TypedDict, total=False
):
    cardTestingVerdict: GoogleCloudRecaptchaenterpriseV1FraudPreventionAssessmentCardTestingVerdict
    stolenInstrumentVerdict: GoogleCloudRecaptchaenterpriseV1FraudPreventionAssessmentStolenInstrumentVerdict
    transactionRisk: float

@typing.type_check_only
class GoogleCloudRecaptchaenterpriseV1FraudPreventionAssessmentCardTestingVerdict(
    typing_extensions.TypedDict, total=False
):
    risk: float

@typing.type_check_only
class GoogleCloudRecaptchaenterpriseV1FraudPreventionAssessmentStolenInstrumentVerdict(
    typing_extensions.TypedDict, total=False
):
    risk: float

@typing.type_check_only
class GoogleCloudRecaptchaenterpriseV1IOSKeySettings(
    typing_extensions.TypedDict, total=False
):
    allowAllBundleIds: bool
    allowedBundleIds: _list[str]

@typing.type_check_only
class GoogleCloudRecaptchaenterpriseV1Key(typing_extensions.TypedDict, total=False):
    androidSettings: GoogleCloudRecaptchaenterpriseV1AndroidKeySettings
    createTime: str
    displayName: str
    iosSettings: GoogleCloudRecaptchaenterpriseV1IOSKeySettings
    labels: dict[str, typing.Any]
    name: str
    testingOptions: GoogleCloudRecaptchaenterpriseV1TestingOptions
    wafSettings: GoogleCloudRecaptchaenterpriseV1WafSettings
    webSettings: GoogleCloudRecaptchaenterpriseV1WebKeySettings

@typing.type_check_only
class GoogleCloudRecaptchaenterpriseV1ListKeysResponse(
    typing_extensions.TypedDict, total=False
):
    keys: _list[GoogleCloudRecaptchaenterpriseV1Key]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudRecaptchaenterpriseV1ListRelatedAccountGroupMembershipsResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    relatedAccountGroupMemberships: _list[
        GoogleCloudRecaptchaenterpriseV1RelatedAccountGroupMembership
    ]

@typing.type_check_only
class GoogleCloudRecaptchaenterpriseV1ListRelatedAccountGroupsResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    relatedAccountGroups: _list[GoogleCloudRecaptchaenterpriseV1RelatedAccountGroup]

@typing.type_check_only
class GoogleCloudRecaptchaenterpriseV1Metrics(typing_extensions.TypedDict, total=False):
    challengeMetrics: _list[GoogleCloudRecaptchaenterpriseV1ChallengeMetrics]
    name: str
    scoreMetrics: _list[GoogleCloudRecaptchaenterpriseV1ScoreMetrics]
    startTime: str

@typing.type_check_only
class GoogleCloudRecaptchaenterpriseV1MigrateKeyRequest(
    typing_extensions.TypedDict, total=False
):
    skipBillingCheck: bool

@typing.type_check_only
class GoogleCloudRecaptchaenterpriseV1PrivatePasswordLeakVerification(
    typing_extensions.TypedDict, total=False
):
    encryptedLeakMatchPrefixes: _list[str]
    encryptedUserCredentialsHash: str
    lookupHashPrefix: str
    reencryptedUserCredentialsHash: str

@typing.type_check_only
class GoogleCloudRecaptchaenterpriseV1RelatedAccountGroup(
    typing_extensions.TypedDict, total=False
):
    name: str

@typing.type_check_only
class GoogleCloudRecaptchaenterpriseV1RelatedAccountGroupMembership(
    typing_extensions.TypedDict, total=False
):
    hashedAccountId: str
    name: str

@typing.type_check_only
class GoogleCloudRecaptchaenterpriseV1RetrieveLegacySecretKeyResponse(
    typing_extensions.TypedDict, total=False
):
    legacySecretKey: str

@typing.type_check_only
class GoogleCloudRecaptchaenterpriseV1RiskAnalysis(
    typing_extensions.TypedDict, total=False
):
    reasons: _list[str]
    score: float

@typing.type_check_only
class GoogleCloudRecaptchaenterpriseV1ScoreDistribution(
    typing_extensions.TypedDict, total=False
):
    scoreBuckets: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudRecaptchaenterpriseV1ScoreMetrics(
    typing_extensions.TypedDict, total=False
):
    actionMetrics: dict[str, typing.Any]
    overallMetrics: GoogleCloudRecaptchaenterpriseV1ScoreDistribution

@typing.type_check_only
class GoogleCloudRecaptchaenterpriseV1SearchRelatedAccountGroupMembershipsRequest(
    typing_extensions.TypedDict, total=False
):
    hashedAccountId: str
    pageSize: int
    pageToken: str

@typing.type_check_only
class GoogleCloudRecaptchaenterpriseV1SearchRelatedAccountGroupMembershipsResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    relatedAccountGroupMemberships: _list[
        GoogleCloudRecaptchaenterpriseV1RelatedAccountGroupMembership
    ]

@typing.type_check_only
class GoogleCloudRecaptchaenterpriseV1TestingOptions(
    typing_extensions.TypedDict, total=False
):
    testingChallenge: typing_extensions.Literal[
        "TESTING_CHALLENGE_UNSPECIFIED", "NOCAPTCHA", "UNSOLVABLE_CHALLENGE"
    ]
    testingScore: float

@typing.type_check_only
class GoogleCloudRecaptchaenterpriseV1TokenProperties(
    typing_extensions.TypedDict, total=False
):
    action: str
    androidPackageName: str
    createTime: str
    hostname: str
    invalidReason: typing_extensions.Literal[
        "INVALID_REASON_UNSPECIFIED",
        "UNKNOWN_INVALID_REASON",
        "MALFORMED",
        "EXPIRED",
        "DUPE",
        "MISSING",
        "BROWSER_ERROR",
    ]
    iosBundleId: str
    valid: bool

@typing.type_check_only
class GoogleCloudRecaptchaenterpriseV1TransactionData(
    typing_extensions.TypedDict, total=False
):
    billingAddress: GoogleCloudRecaptchaenterpriseV1TransactionDataAddress
    cardBin: str
    cardLastFour: str
    currencyCode: str
    gatewayInfo: GoogleCloudRecaptchaenterpriseV1TransactionDataGatewayInfo
    items: _list[GoogleCloudRecaptchaenterpriseV1TransactionDataItem]
    merchants: _list[GoogleCloudRecaptchaenterpriseV1TransactionDataUser]
    paymentMethod: str
    shippingAddress: GoogleCloudRecaptchaenterpriseV1TransactionDataAddress
    shippingValue: float
    transactionId: str
    user: GoogleCloudRecaptchaenterpriseV1TransactionDataUser
    value: float

@typing.type_check_only
class GoogleCloudRecaptchaenterpriseV1TransactionDataAddress(
    typing_extensions.TypedDict, total=False
):
    address: _list[str]
    administrativeArea: str
    locality: str
    postalCode: str
    recipient: str
    regionCode: str

@typing.type_check_only
class GoogleCloudRecaptchaenterpriseV1TransactionDataGatewayInfo(
    typing_extensions.TypedDict, total=False
):
    avsResponseCode: str
    cvvResponseCode: str
    gatewayResponseCode: str
    name: str

@typing.type_check_only
class GoogleCloudRecaptchaenterpriseV1TransactionDataItem(
    typing_extensions.TypedDict, total=False
):
    merchantAccountId: str
    name: str
    quantity: str
    value: float

@typing.type_check_only
class GoogleCloudRecaptchaenterpriseV1TransactionDataUser(
    typing_extensions.TypedDict, total=False
):
    accountId: str
    creationMs: str
    email: str
    emailVerified: bool
    phoneNumber: str
    phoneVerified: bool

@typing.type_check_only
class GoogleCloudRecaptchaenterpriseV1TransactionEvent(
    typing_extensions.TypedDict, total=False
):
    eventTime: str
    eventType: typing_extensions.Literal[
        "TRANSACTION_EVENT_TYPE_UNSPECIFIED",
        "MERCHANT_APPROVE",
        "MERCHANT_DENY",
        "MANUAL_REVIEW",
        "AUTHORIZATION",
        "AUTHORIZATION_DECLINE",
        "PAYMENT_CAPTURE",
        "PAYMENT_CAPTURE_DECLINE",
        "CANCEL",
        "CHARGEBACK_INQUIRY",
        "CHARGEBACK_ALERT",
        "FRAUD_NOTIFICATION",
        "CHARGEBACK",
        "CHARGEBACK_REPRESENTMENT",
        "CHARGEBACK_REVERSE",
        "REFUND_REQUEST",
        "REFUND_DECLINE",
        "REFUND",
        "REFUND_REVERSE",
    ]
    reason: str
    value: float

@typing.type_check_only
class GoogleCloudRecaptchaenterpriseV1WafSettings(
    typing_extensions.TypedDict, total=False
):
    wafFeature: typing_extensions.Literal[
        "WAF_FEATURE_UNSPECIFIED", "CHALLENGE_PAGE", "SESSION_TOKEN", "ACTION_TOKEN"
    ]
    wafService: typing_extensions.Literal["WAF_SERVICE_UNSPECIFIED", "CA", "FASTLY"]

@typing.type_check_only
class GoogleCloudRecaptchaenterpriseV1WebKeySettings(
    typing_extensions.TypedDict, total=False
):
    allowAllDomains: bool
    allowAmpTraffic: bool
    allowedDomains: _list[str]
    challengeSecurityPreference: typing_extensions.Literal[
        "CHALLENGE_SECURITY_PREFERENCE_UNSPECIFIED", "USABILITY", "BALANCE", "SECURITY"
    ]
    integrationType: typing_extensions.Literal[
        "INTEGRATION_TYPE_UNSPECIFIED", "SCORE", "CHECKBOX", "INVISIBLE"
    ]

@typing.type_check_only
class GoogleProtobufEmpty(typing_extensions.TypedDict, total=False): ...
