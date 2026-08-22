import typing

_list = list

@typing.type_check_only
class GoogleCloudRecaptchaenterpriseV1AccountDefenderAssessment(
    typing.TypedDict, total=False
):
    accountTakeoverVerdict: (
        GoogleCloudRecaptchaenterpriseV1AccountDefenderAssessmentAccountTakeoverVerdict
    )
    labels: _list[
        typing.Literal[
            "ACCOUNT_DEFENDER_LABEL_UNSPECIFIED",
            "PROFILE_MATCH",
            "SUSPICIOUS_LOGIN_ACTIVITY",
            "SUSPICIOUS_ACCOUNT_CREATION",
            "RELATED_ACCOUNTS_NUMBER_HIGH",
        ]
    ]

@typing.type_check_only
class GoogleCloudRecaptchaenterpriseV1AccountDefenderAssessmentAccountRiskReason(
    typing.TypedDict, total=False
):
    reason: typing.Literal[
        "RISK_REASON_UNSPECIFIED",
        "CLIENT_HISTORICAL_BOT_ACTIVITY",
        "ACCOUNT_IN_LARGE_RELATED_GROUP",
        "CLIENT_ACCESSED_MANY_ACCOUNTS",
        "DISPOSABLE_EMAIL_DOMAIN",
    ]

@typing.type_check_only
class GoogleCloudRecaptchaenterpriseV1AccountDefenderAssessmentAccountTakeoverVerdict(
    typing.TypedDict, total=False
):
    risk: float
    riskReasons: _list[
        GoogleCloudRecaptchaenterpriseV1AccountDefenderAssessmentAccountRiskReason
    ]
    trustReasons: _list[
        GoogleCloudRecaptchaenterpriseV1AccountDefenderAssessmentAccountTrustReason
    ]

@typing.type_check_only
class GoogleCloudRecaptchaenterpriseV1AccountDefenderAssessmentAccountTrustReason(
    typing.TypedDict, total=False
):
    reason: typing.Literal[
        "TRUST_REASON_UNSPECIFIED",
        "PROFILE_MATCH",
        "ACCOUNT_HISTORY_REPUTABLE",
        "IDENTITY_GLOBAL_ACTIVITY_REPUTABLE",
        "IDENTITY_HISTORY_REPUTABLE",
    ]

@typing.type_check_only
class GoogleCloudRecaptchaenterpriseV1AccountVerificationInfo(
    typing.TypedDict, total=False
):
    endpoints: _list[GoogleCloudRecaptchaenterpriseV1EndpointVerificationInfo]
    languageCode: str
    latestVerificationResult: typing.Literal[
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
class GoogleCloudRecaptchaenterpriseV1AddIpOverrideRequest(
    typing.TypedDict, total=False
):
    ipOverrideData: GoogleCloudRecaptchaenterpriseV1IpOverrideData

@typing.type_check_only
class GoogleCloudRecaptchaenterpriseV1AddIpOverrideResponse(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudRecaptchaenterpriseV1AndroidKeySettings(typing.TypedDict, total=False):
    allowAllPackageNames: bool
    allowedPackageNames: _list[str]
    supportNonGoogleAppStoreDistribution: bool

@typing.type_check_only
class GoogleCloudRecaptchaenterpriseV1AnnotateAssessmentRequest(
    typing.TypedDict, total=False
):
    accountId: str
    annotation: typing.Literal[
        "ANNOTATION_UNSPECIFIED",
        "LEGITIMATE",
        "FRAUDULENT",
        "PASSWORD_CORRECT",
        "PASSWORD_INCORRECT",
    ]
    hashedAccountId: str
    phoneAuthenticationEvent: GoogleCloudRecaptchaenterpriseV1PhoneAuthenticationEvent
    reasons: _list[
        typing.Literal[
            "REASON_UNSPECIFIED",
            "CHARGEBACK",
            "CHARGEBACK_FRAUD",
            "CHARGEBACK_DISPUTE",
            "REFUND",
            "REFUND_FRAUD",
            "TRANSACTION_ACCEPTED",
            "TRANSACTION_DECLINED",
            "PAYMENT_HEURISTICS",
            "INITIATED_TWO_FACTOR",
            "PASSED_TWO_FACTOR",
            "FAILED_TWO_FACTOR",
            "CORRECT_PASSWORD",
            "INCORRECT_PASSWORD",
            "SOCIAL_SPAM",
        ]
    ]
    transactionEvent: GoogleCloudRecaptchaenterpriseV1TransactionEvent

@typing.type_check_only
class GoogleCloudRecaptchaenterpriseV1AnnotateAssessmentResponse(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudRecaptchaenterpriseV1AppleDeveloperId(typing.TypedDict, total=False):
    keyId: str
    privateKey: str
    teamId: str

@typing.type_check_only
class GoogleCloudRecaptchaenterpriseV1Assessment(typing.TypedDict, total=False):
    accountDefenderAssessment: GoogleCloudRecaptchaenterpriseV1AccountDefenderAssessment
    accountVerification: GoogleCloudRecaptchaenterpriseV1AccountVerificationInfo
    assessmentEnvironment: GoogleCloudRecaptchaenterpriseV1AssessmentEnvironment
    event: GoogleCloudRecaptchaenterpriseV1Event
    firewallPolicyAssessment: GoogleCloudRecaptchaenterpriseV1FirewallPolicyAssessment
    fraudPreventionAssessment: GoogleCloudRecaptchaenterpriseV1FraudPreventionAssessment
    fraudSignals: GoogleCloudRecaptchaenterpriseV1FraudSignals
    name: str
    phoneFraudAssessment: GoogleCloudRecaptchaenterpriseV1PhoneFraudAssessment
    policyEvaluation: GoogleCloudRecaptchaenterpriseV1PolicyEvaluation
    privatePasswordLeakVerification: (
        GoogleCloudRecaptchaenterpriseV1PrivatePasswordLeakVerification
    )
    riskAnalysis: GoogleCloudRecaptchaenterpriseV1RiskAnalysis
    tokenProperties: GoogleCloudRecaptchaenterpriseV1TokenProperties

@typing.type_check_only
class GoogleCloudRecaptchaenterpriseV1AssessmentEnvironment(
    typing.TypedDict, total=False
):
    client: str
    version: str

@typing.type_check_only
class GoogleCloudRecaptchaenterpriseV1Bot(typing.TypedDict, total=False):
    botType: typing.Literal[
        "BOT_TYPE_UNSPECIFIED", "AI_AGENT", "CONTENT_SCRAPER", "SEARCH_INDEXER"
    ]
    name: str

@typing.type_check_only
class GoogleCloudRecaptchaenterpriseV1ChallengeMetrics(typing.TypedDict, total=False):
    failedCount: str
    nocaptchaCount: str
    pageloadCount: str
    passedCount: str

@typing.type_check_only
class GoogleCloudRecaptchaenterpriseV1ChallengeRule(typing.TypedDict, total=False):
    challenge: GoogleCloudRecaptchaenterpriseV1ChallengeRuleChallengeOutcome
    condition: str
    noChallenge: GoogleCloudRecaptchaenterpriseV1ChallengeRuleNoChallengeOutcome

@typing.type_check_only
class GoogleCloudRecaptchaenterpriseV1ChallengeRuleChallengeOutcome(
    typing.TypedDict, total=False
):
    difficulty: typing.Literal[
        "CHALLENGE_SECURITY_PREFERENCE_UNSPECIFIED", "USABILITY", "BALANCE", "SECURITY"
    ]

@typing.type_check_only
class GoogleCloudRecaptchaenterpriseV1ChallengeRuleEvaluation(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudRecaptchaenterpriseV1ChallengeRuleGroup(typing.TypedDict, total=False):
    actions: _list[str]
    challengeRules: _list[GoogleCloudRecaptchaenterpriseV1ChallengeRule]

@typing.type_check_only
class GoogleCloudRecaptchaenterpriseV1ChallengeRuleNoChallengeOutcome(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudRecaptchaenterpriseV1ClientSettings(typing.TypedDict, total=False):
    allowAllDomains: bool
    allowedDomains: _list[str]
    protectedEndpointGroup: GoogleCloudRecaptchaenterpriseV1ProtectedEndpointGroup

@typing.type_check_only
class GoogleCloudRecaptchaenterpriseV1EndpointVerificationInfo(
    typing.TypedDict, total=False
):
    emailAddress: str
    lastVerificationTime: str
    phoneNumber: str
    requestToken: str

@typing.type_check_only
class GoogleCloudRecaptchaenterpriseV1Event(typing.TypedDict, total=False):
    expectedAction: str
    express: bool
    firewallPolicyEvaluation: bool
    fraudPrevention: typing.Literal[
        "FRAUD_PREVENTION_UNSPECIFIED", "ENABLED", "DISABLED"
    ]
    hashedAccountId: str
    headers: _list[str]
    ja3: str
    ja4: str
    requestedUri: str
    siteKey: str
    token: str
    transactionData: GoogleCloudRecaptchaenterpriseV1TransactionData
    userAgent: str
    userInfo: GoogleCloudRecaptchaenterpriseV1UserInfo
    userIpAddress: str
    wafTokenAssessment: bool

@typing.type_check_only
class GoogleCloudRecaptchaenterpriseV1ExpressKeySettings(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudRecaptchaenterpriseV1FirewallAction(typing.TypedDict, total=False):
    allow: GoogleCloudRecaptchaenterpriseV1FirewallActionAllowAction
    block: GoogleCloudRecaptchaenterpriseV1FirewallActionBlockAction
    includeRecaptchaScript: (
        GoogleCloudRecaptchaenterpriseV1FirewallActionIncludeRecaptchaScriptAction
    )
    redirect: GoogleCloudRecaptchaenterpriseV1FirewallActionRedirectAction
    setHeader: GoogleCloudRecaptchaenterpriseV1FirewallActionSetHeaderAction
    substitute: GoogleCloudRecaptchaenterpriseV1FirewallActionSubstituteAction

@typing.type_check_only
class GoogleCloudRecaptchaenterpriseV1FirewallActionAllowAction(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudRecaptchaenterpriseV1FirewallActionBlockAction(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudRecaptchaenterpriseV1FirewallActionIncludeRecaptchaScriptAction(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudRecaptchaenterpriseV1FirewallActionRedirectAction(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudRecaptchaenterpriseV1FirewallActionSetHeaderAction(
    typing.TypedDict, total=False
):
    key: str
    value: str

@typing.type_check_only
class GoogleCloudRecaptchaenterpriseV1FirewallActionSubstituteAction(
    typing.TypedDict, total=False
):
    path: str

@typing.type_check_only
class GoogleCloudRecaptchaenterpriseV1FirewallPolicy(typing.TypedDict, total=False):
    actions: _list[GoogleCloudRecaptchaenterpriseV1FirewallAction]
    condition: str
    description: str
    name: str
    path: str

@typing.type_check_only
class GoogleCloudRecaptchaenterpriseV1FirewallPolicyAssessment(
    typing.TypedDict, total=False
):
    error: GoogleRpcStatus
    firewallPolicy: GoogleCloudRecaptchaenterpriseV1FirewallPolicy

@typing.type_check_only
class GoogleCloudRecaptchaenterpriseV1FraudPreventionAssessment(
    typing.TypedDict, total=False
):
    behavioralTrustVerdict: (
        GoogleCloudRecaptchaenterpriseV1FraudPreventionAssessmentBehavioralTrustVerdict
    )
    cardTestingVerdict: (
        GoogleCloudRecaptchaenterpriseV1FraudPreventionAssessmentCardTestingVerdict
    )
    riskReasons: _list[
        GoogleCloudRecaptchaenterpriseV1FraudPreventionAssessmentRiskReason
    ]
    stolenInstrumentVerdict: (
        GoogleCloudRecaptchaenterpriseV1FraudPreventionAssessmentStolenInstrumentVerdict
    )
    transactionRisk: float

@typing.type_check_only
class GoogleCloudRecaptchaenterpriseV1FraudPreventionAssessmentBehavioralTrustVerdict(
    typing.TypedDict, total=False
):
    trust: float

@typing.type_check_only
class GoogleCloudRecaptchaenterpriseV1FraudPreventionAssessmentCardTestingVerdict(
    typing.TypedDict, total=False
):
    risk: float

@typing.type_check_only
class GoogleCloudRecaptchaenterpriseV1FraudPreventionAssessmentRiskReason(
    typing.TypedDict, total=False
):
    reason: typing.Literal[
        "REASON_UNSPECIFIED",
        "HIGH_TRANSACTION_VELOCITY",
        "EXCESSIVE_ENUMERATION_PATTERN",
        "SHORT_IDENTITY_HISTORY",
        "GEOLOCATION_DISCREPANCY",
        "ASSOCIATED_WITH_FRAUD_CLUSTER",
    ]

@typing.type_check_only
class GoogleCloudRecaptchaenterpriseV1FraudPreventionAssessmentStolenInstrumentVerdict(
    typing.TypedDict, total=False
):
    risk: float

@typing.type_check_only
class GoogleCloudRecaptchaenterpriseV1FraudSignals(typing.TypedDict, total=False):
    cardSignals: GoogleCloudRecaptchaenterpriseV1FraudSignalsCardSignals
    userSignals: GoogleCloudRecaptchaenterpriseV1FraudSignalsUserSignals

@typing.type_check_only
class GoogleCloudRecaptchaenterpriseV1FraudSignalsCardSignals(
    typing.TypedDict, total=False
):
    cardLabels: _list[
        typing.Literal[
            "CARD_LABEL_UNSPECIFIED", "PREPAID", "VIRTUAL", "UNEXPECTED_LOCATION"
        ]
    ]

@typing.type_check_only
class GoogleCloudRecaptchaenterpriseV1FraudSignalsUserSignals(
    typing.TypedDict, total=False
):
    activeDaysLowerBound: int
    syntheticRisk: float

@typing.type_check_only
class GoogleCloudRecaptchaenterpriseV1IOSKeySettings(typing.TypedDict, total=False):
    allowAllBundleIds: bool
    allowedBundleIds: _list[str]
    appleDeveloperId: GoogleCloudRecaptchaenterpriseV1AppleDeveloperId

@typing.type_check_only
class GoogleCloudRecaptchaenterpriseV1IpOverrideData(typing.TypedDict, total=False):
    ip: str
    overrideType: typing.Literal["OVERRIDE_TYPE_UNSPECIFIED", "ALLOW"]

@typing.type_check_only
class GoogleCloudRecaptchaenterpriseV1Key(typing.TypedDict, total=False):
    androidSettings: GoogleCloudRecaptchaenterpriseV1AndroidKeySettings
    createTime: str
    displayName: str
    expressSettings: GoogleCloudRecaptchaenterpriseV1ExpressKeySettings
    iosSettings: GoogleCloudRecaptchaenterpriseV1IOSKeySettings
    labels: dict[str, typing.Any]
    name: str
    testingOptions: GoogleCloudRecaptchaenterpriseV1TestingOptions
    universalSettings: GoogleCloudRecaptchaenterpriseV1UniversalKeySettings
    wafSettings: GoogleCloudRecaptchaenterpriseV1WafSettings
    webSettings: GoogleCloudRecaptchaenterpriseV1WebKeySettings

@typing.type_check_only
class GoogleCloudRecaptchaenterpriseV1ListFirewallPoliciesResponse(
    typing.TypedDict, total=False
):
    firewallPolicies: _list[GoogleCloudRecaptchaenterpriseV1FirewallPolicy]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudRecaptchaenterpriseV1ListIpOverridesResponse(
    typing.TypedDict, total=False
):
    ipOverrides: _list[GoogleCloudRecaptchaenterpriseV1IpOverrideData]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudRecaptchaenterpriseV1ListKeysResponse(typing.TypedDict, total=False):
    keys: _list[GoogleCloudRecaptchaenterpriseV1Key]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudRecaptchaenterpriseV1ListRelatedAccountGroupMembershipsResponse(
    typing.TypedDict, total=False
):
    nextPageToken: str
    relatedAccountGroupMemberships: _list[
        GoogleCloudRecaptchaenterpriseV1RelatedAccountGroupMembership
    ]

@typing.type_check_only
class GoogleCloudRecaptchaenterpriseV1ListRelatedAccountGroupsResponse(
    typing.TypedDict, total=False
):
    nextPageToken: str
    relatedAccountGroups: _list[GoogleCloudRecaptchaenterpriseV1RelatedAccountGroup]

@typing.type_check_only
class GoogleCloudRecaptchaenterpriseV1Metrics(typing.TypedDict, total=False):
    challengeMetrics: _list[GoogleCloudRecaptchaenterpriseV1ChallengeMetrics]
    name: str
    scoreMetrics: _list[GoogleCloudRecaptchaenterpriseV1ScoreMetrics]
    startTime: str

@typing.type_check_only
class GoogleCloudRecaptchaenterpriseV1MigrateKeyRequest(typing.TypedDict, total=False):
    skipBillingCheck: bool

@typing.type_check_only
class GoogleCloudRecaptchaenterpriseV1PhoneAuthenticationEvent(
    typing.TypedDict, total=False
):
    eventTime: str
    phoneNumber: str

@typing.type_check_only
class GoogleCloudRecaptchaenterpriseV1PhoneFraudAssessment(
    typing.TypedDict, total=False
):
    smsTollFraudVerdict: GoogleCloudRecaptchaenterpriseV1SmsTollFraudVerdict

@typing.type_check_only
class GoogleCloudRecaptchaenterpriseV1Policy(typing.TypedDict, total=False):
    challengeRuleGroups: _list[GoogleCloudRecaptchaenterpriseV1ChallengeRuleGroup]
    clientSettings: GoogleCloudRecaptchaenterpriseV1ClientSettings
    name: str

@typing.type_check_only
class GoogleCloudRecaptchaenterpriseV1PolicyEvaluation(typing.TypedDict, total=False):
    challengeRuleEvaluation: GoogleCloudRecaptchaenterpriseV1ChallengeRuleEvaluation

@typing.type_check_only
class GoogleCloudRecaptchaenterpriseV1PrivatePasswordLeakVerification(
    typing.TypedDict, total=False
):
    encryptedLeakMatchPrefixes: _list[str]
    encryptedUserCredentialsHash: str
    lookupHashPrefix: str
    reencryptedUserCredentialsHash: str

@typing.type_check_only
class GoogleCloudRecaptchaenterpriseV1ProtectedEndpoint(typing.TypedDict, total=False):
    action: str
    path: str

@typing.type_check_only
class GoogleCloudRecaptchaenterpriseV1ProtectedEndpointGroup(
    typing.TypedDict, total=False
):
    protectedEndpoints: _list[GoogleCloudRecaptchaenterpriseV1ProtectedEndpoint]

@typing.type_check_only
class GoogleCloudRecaptchaenterpriseV1RelatedAccountGroup(
    typing.TypedDict, total=False
):
    name: str

@typing.type_check_only
class GoogleCloudRecaptchaenterpriseV1RelatedAccountGroupMembership(
    typing.TypedDict, total=False
):
    accountId: str
    hashedAccountId: str
    name: str

@typing.type_check_only
class GoogleCloudRecaptchaenterpriseV1RemoveIpOverrideRequest(
    typing.TypedDict, total=False
):
    ipOverrideData: GoogleCloudRecaptchaenterpriseV1IpOverrideData

@typing.type_check_only
class GoogleCloudRecaptchaenterpriseV1RemoveIpOverrideResponse(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudRecaptchaenterpriseV1ReorderFirewallPoliciesRequest(
    typing.TypedDict, total=False
):
    names: _list[str]

@typing.type_check_only
class GoogleCloudRecaptchaenterpriseV1ReorderFirewallPoliciesResponse(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudRecaptchaenterpriseV1RetrieveLegacySecretKeyResponse(
    typing.TypedDict, total=False
):
    legacySecretKey: str

@typing.type_check_only
class GoogleCloudRecaptchaenterpriseV1RiskAnalysis(typing.TypedDict, total=False):
    challenge: typing.Literal["CHALLENGE_UNSPECIFIED", "NOCAPTCHA", "PASSED", "FAILED"]
    extendedVerdictReasons: _list[str]
    lastChallengeType: typing.Literal[
        "CHALLENGE_TYPE_UNSPECIFIED", "CHALLENGE_TYPE_VISUAL", "CHALLENGE_TYPE_AUDIO"
    ]
    reasons: _list[
        typing.Literal[
            "CLASSIFICATION_REASON_UNSPECIFIED",
            "AUTOMATION",
            "UNEXPECTED_ENVIRONMENT",
            "TOO_MUCH_TRAFFIC",
            "UNEXPECTED_USAGE_PATTERNS",
            "LOW_CONFIDENCE_SCORE",
            "SUSPECTED_CARDING",
            "SUSPECTED_CHARGEBACK",
        ]
    ]
    score: float
    verifiedBots: _list[GoogleCloudRecaptchaenterpriseV1Bot]

@typing.type_check_only
class GoogleCloudRecaptchaenterpriseV1ScoreDistribution(typing.TypedDict, total=False):
    scoreBuckets: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudRecaptchaenterpriseV1ScoreMetrics(typing.TypedDict, total=False):
    actionMetrics: dict[str, typing.Any]
    overallMetrics: GoogleCloudRecaptchaenterpriseV1ScoreDistribution

@typing.type_check_only
class GoogleCloudRecaptchaenterpriseV1SearchRelatedAccountGroupMembershipsRequest(
    typing.TypedDict, total=False
):
    accountId: str
    hashedAccountId: str
    pageSize: int
    pageToken: str

@typing.type_check_only
class GoogleCloudRecaptchaenterpriseV1SearchRelatedAccountGroupMembershipsResponse(
    typing.TypedDict, total=False
):
    nextPageToken: str
    relatedAccountGroupMemberships: _list[
        GoogleCloudRecaptchaenterpriseV1RelatedAccountGroupMembership
    ]

@typing.type_check_only
class GoogleCloudRecaptchaenterpriseV1SmsTollFraudVerdict(
    typing.TypedDict, total=False
):
    reasons: _list[
        typing.Literal["SMS_TOLL_FRAUD_REASON_UNSPECIFIED", "INVALID_PHONE_NUMBER"]
    ]
    risk: float

@typing.type_check_only
class GoogleCloudRecaptchaenterpriseV1TestingOptions(typing.TypedDict, total=False):
    testingChallenge: typing.Literal[
        "TESTING_CHALLENGE_UNSPECIFIED", "NOCAPTCHA", "UNSOLVABLE_CHALLENGE"
    ]
    testingScore: float

@typing.type_check_only
class GoogleCloudRecaptchaenterpriseV1TokenProperties(typing.TypedDict, total=False):
    action: str
    androidPackageName: str
    createTime: str
    hostname: str
    invalidReason: typing.Literal[
        "INVALID_REASON_UNSPECIFIED",
        "UNKNOWN_INVALID_REASON",
        "MALFORMED",
        "EXPIRED",
        "DUPE",
        "MISSING",
        "BROWSER_ERROR",
        "UNEXPECTED_ACTION",
        "KEY_MISMATCH",
        "DOMAIN_MISMATCH",
    ]
    iosBundleId: str
    valid: bool

@typing.type_check_only
class GoogleCloudRecaptchaenterpriseV1TransactionData(typing.TypedDict, total=False):
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
    typing.TypedDict, total=False
):
    address: _list[str]
    administrativeArea: str
    locality: str
    postalCode: str
    recipient: str
    regionCode: str

@typing.type_check_only
class GoogleCloudRecaptchaenterpriseV1TransactionDataGatewayInfo(
    typing.TypedDict, total=False
):
    avsResponseCode: str
    cvvResponseCode: str
    gatewayResponseCode: str
    name: str

@typing.type_check_only
class GoogleCloudRecaptchaenterpriseV1TransactionDataItem(
    typing.TypedDict, total=False
):
    merchantAccountId: str
    name: str
    quantity: str
    value: float

@typing.type_check_only
class GoogleCloudRecaptchaenterpriseV1TransactionDataUser(
    typing.TypedDict, total=False
):
    accountId: str
    creationMs: str
    email: str
    emailVerified: bool
    phoneNumber: str
    phoneVerified: bool

@typing.type_check_only
class GoogleCloudRecaptchaenterpriseV1TransactionEvent(typing.TypedDict, total=False):
    eventTime: str
    eventType: typing.Literal[
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
class GoogleCloudRecaptchaenterpriseV1UniversalKeySettings(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudRecaptchaenterpriseV1UserId(typing.TypedDict, total=False):
    email: str
    phoneNumber: str
    username: str

@typing.type_check_only
class GoogleCloudRecaptchaenterpriseV1UserInfo(typing.TypedDict, total=False):
    accountId: str
    createAccountTime: str
    userIds: _list[GoogleCloudRecaptchaenterpriseV1UserId]

@typing.type_check_only
class GoogleCloudRecaptchaenterpriseV1WafSettings(typing.TypedDict, total=False):
    wafFeature: typing.Literal[
        "WAF_FEATURE_UNSPECIFIED",
        "CHALLENGE_PAGE",
        "SESSION_TOKEN",
        "ACTION_TOKEN",
        "EXPRESS",
    ]
    wafService: typing.Literal[
        "WAF_SERVICE_UNSPECIFIED", "CA", "FASTLY", "CLOUDFLARE", "AKAMAI"
    ]

@typing.type_check_only
class GoogleCloudRecaptchaenterpriseV1WebKeySettings(typing.TypedDict, total=False):
    allowAllDomains: bool
    allowAmpTraffic: bool
    allowedDomains: _list[str]
    challengeSecurityPreference: typing.Literal[
        "CHALLENGE_SECURITY_PREFERENCE_UNSPECIFIED", "USABILITY", "BALANCE", "SECURITY"
    ]
    challengeSettings: GoogleCloudRecaptchaenterpriseV1WebKeySettingsChallengeSettings
    integrationType: typing.Literal[
        "INTEGRATION_TYPE_UNSPECIFIED",
        "SCORE",
        "CHECKBOX",
        "INVISIBLE",
        "POLICY_BASED_CHALLENGE",
    ]

@typing.type_check_only
class GoogleCloudRecaptchaenterpriseV1WebKeySettingsActionSettings(
    typing.TypedDict, total=False
):
    scoreThreshold: float

@typing.type_check_only
class GoogleCloudRecaptchaenterpriseV1WebKeySettingsChallengeSettings(
    typing.TypedDict, total=False
):
    actionSettings: dict[str, typing.Any]
    defaultSettings: GoogleCloudRecaptchaenterpriseV1WebKeySettingsActionSettings

@typing.type_check_only
class GoogleProtobufEmpty(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleRpcStatus(typing.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str
