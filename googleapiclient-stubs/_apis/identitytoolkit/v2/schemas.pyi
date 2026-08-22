import typing

_list = list

@typing.type_check_only
class GoogleCloudIdentitytoolkitAdminV2AllowByDefault(typing.TypedDict, total=False):
    disallowedRegions: _list[str]

@typing.type_check_only
class GoogleCloudIdentitytoolkitAdminV2AllowlistOnly(typing.TypedDict, total=False):
    allowedRegions: _list[str]

@typing.type_check_only
class GoogleCloudIdentitytoolkitAdminV2Anonymous(typing.TypedDict, total=False):
    enabled: bool

@typing.type_check_only
class GoogleCloudIdentitytoolkitAdminV2AppleSignInConfig(typing.TypedDict, total=False):
    bundleIds: _list[str]
    codeFlowConfig: GoogleCloudIdentitytoolkitAdminV2CodeFlowConfig

@typing.type_check_only
class GoogleCloudIdentitytoolkitAdminV2BlockingFunctionsConfig(
    typing.TypedDict, total=False
):
    forwardInboundCredentials: (
        GoogleCloudIdentitytoolkitAdminV2ForwardInboundCredentials
    )
    triggers: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudIdentitytoolkitAdminV2ClientConfig(typing.TypedDict, total=False):
    apiKey: str
    firebaseSubdomain: str
    permissions: GoogleCloudIdentitytoolkitAdminV2Permissions

@typing.type_check_only
class GoogleCloudIdentitytoolkitAdminV2ClientPermissionConfig(
    typing.TypedDict, total=False
):
    permissions: GoogleCloudIdentitytoolkitAdminV2ClientPermissions

@typing.type_check_only
class GoogleCloudIdentitytoolkitAdminV2ClientPermissions(typing.TypedDict, total=False):
    disabledUserDeletion: bool
    disabledUserSignup: bool

@typing.type_check_only
class GoogleCloudIdentitytoolkitAdminV2CodeFlowConfig(typing.TypedDict, total=False):
    keyId: str
    privateKey: str
    teamId: str

@typing.type_check_only
class GoogleCloudIdentitytoolkitAdminV2Config(typing.TypedDict, total=False):
    authorizedDomains: _list[str]
    autodeleteAnonymousUsers: bool
    blockingFunctions: GoogleCloudIdentitytoolkitAdminV2BlockingFunctionsConfig
    client: GoogleCloudIdentitytoolkitAdminV2ClientConfig
    defaultHostingSite: str
    emailPrivacyConfig: GoogleCloudIdentitytoolkitAdminV2EmailPrivacyConfig
    mfa: GoogleCloudIdentitytoolkitAdminV2MultiFactorAuthConfig
    mobileLinksConfig: GoogleCloudIdentitytoolkitAdminV2MobileLinksConfig
    monitoring: GoogleCloudIdentitytoolkitAdminV2MonitoringConfig
    multiTenant: GoogleCloudIdentitytoolkitAdminV2MultiTenantConfig
    name: str
    notification: GoogleCloudIdentitytoolkitAdminV2NotificationConfig
    passwordPolicyConfig: GoogleCloudIdentitytoolkitAdminV2PasswordPolicyConfig
    quota: GoogleCloudIdentitytoolkitAdminV2QuotaConfig
    recaptchaConfig: GoogleCloudIdentitytoolkitAdminV2RecaptchaConfig
    signIn: GoogleCloudIdentitytoolkitAdminV2SignInConfig
    smsRegionConfig: GoogleCloudIdentitytoolkitAdminV2SmsRegionConfig
    subtype: typing.Literal["SUBTYPE_UNSPECIFIED", "IDENTITY_PLATFORM", "FIREBASE_AUTH"]

@typing.type_check_only
class GoogleCloudIdentitytoolkitAdminV2CustomStrengthOptions(
    typing.TypedDict, total=False
):
    containsLowercaseCharacter: bool
    containsNonAlphanumericCharacter: bool
    containsNumericCharacter: bool
    containsUppercaseCharacter: bool
    maxPasswordLength: int
    minPasswordLength: int

@typing.type_check_only
class GoogleCloudIdentitytoolkitAdminV2DefaultSupportedIdp(
    typing.TypedDict, total=False
):
    description: str
    idpId: str

@typing.type_check_only
class GoogleCloudIdentitytoolkitAdminV2DefaultSupportedIdpConfig(
    typing.TypedDict, total=False
):
    appleSignInConfig: GoogleCloudIdentitytoolkitAdminV2AppleSignInConfig
    clientId: str
    clientSecret: str
    enabled: bool
    name: str

@typing.type_check_only
class GoogleCloudIdentitytoolkitAdminV2DnsInfo(typing.TypedDict, total=False):
    customDomain: str
    customDomainState: typing.Literal[
        "VERIFICATION_STATE_UNSPECIFIED",
        "NOT_STARTED",
        "IN_PROGRESS",
        "FAILED",
        "SUCCEEDED",
    ]
    domainVerificationRequestTime: str
    pendingCustomDomain: str
    useCustomDomain: bool

@typing.type_check_only
class GoogleCloudIdentitytoolkitAdminV2Email(typing.TypedDict, total=False):
    enabled: bool
    passwordRequired: bool

@typing.type_check_only
class GoogleCloudIdentitytoolkitAdminV2EmailPrivacyConfig(
    typing.TypedDict, total=False
):
    enableImprovedEmailPrivacy: bool

@typing.type_check_only
class GoogleCloudIdentitytoolkitAdminV2EmailTemplate(typing.TypedDict, total=False):
    body: str
    bodyFormat: typing.Literal["BODY_FORMAT_UNSPECIFIED", "PLAIN_TEXT", "HTML"]
    customized: bool
    replyTo: str
    senderDisplayName: str
    senderLocalPart: str
    subject: str

@typing.type_check_only
class GoogleCloudIdentitytoolkitAdminV2ForwardInboundCredentials(
    typing.TypedDict, total=False
):
    accessToken: bool
    idToken: bool
    refreshToken: bool

@typing.type_check_only
class GoogleCloudIdentitytoolkitAdminV2HashConfig(typing.TypedDict, total=False):
    algorithm: typing.Literal[
        "HASH_ALGORITHM_UNSPECIFIED",
        "HMAC_SHA256",
        "HMAC_SHA1",
        "HMAC_MD5",
        "SCRYPT",
        "PBKDF_SHA1",
        "MD5",
        "HMAC_SHA512",
        "SHA1",
        "BCRYPT",
        "PBKDF2_SHA256",
        "SHA256",
        "SHA512",
        "STANDARD_SCRYPT",
    ]
    memoryCost: int
    rounds: int
    saltSeparator: str
    signerKey: str

@typing.type_check_only
class GoogleCloudIdentitytoolkitAdminV2IdpCertificate(typing.TypedDict, total=False):
    x509Certificate: str

@typing.type_check_only
class GoogleCloudIdentitytoolkitAdminV2IdpConfig(typing.TypedDict, total=False):
    idpCertificates: _list[GoogleCloudIdentitytoolkitAdminV2IdpCertificate]
    idpEntityId: str
    signRequest: bool
    ssoUrl: str

@typing.type_check_only
class GoogleCloudIdentitytoolkitAdminV2InboundSamlConfig(typing.TypedDict, total=False):
    displayName: str
    enabled: bool
    idpConfig: GoogleCloudIdentitytoolkitAdminV2IdpConfig
    name: str
    spConfig: GoogleCloudIdentitytoolkitAdminV2SpConfig

@typing.type_check_only
class GoogleCloudIdentitytoolkitAdminV2Inheritance(typing.TypedDict, total=False):
    emailSendingConfig: bool

@typing.type_check_only
class GoogleCloudIdentitytoolkitAdminV2InitializeIdentityPlatformRequest(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudIdentitytoolkitAdminV2InitializeIdentityPlatformResponse(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudIdentitytoolkitAdminV2ListDefaultSupportedIdpConfigsResponse(
    typing.TypedDict, total=False
):
    defaultSupportedIdpConfigs: _list[
        GoogleCloudIdentitytoolkitAdminV2DefaultSupportedIdpConfig
    ]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudIdentitytoolkitAdminV2ListDefaultSupportedIdpsResponse(
    typing.TypedDict, total=False
):
    defaultSupportedIdps: _list[GoogleCloudIdentitytoolkitAdminV2DefaultSupportedIdp]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudIdentitytoolkitAdminV2ListInboundSamlConfigsResponse(
    typing.TypedDict, total=False
):
    inboundSamlConfigs: _list[GoogleCloudIdentitytoolkitAdminV2InboundSamlConfig]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudIdentitytoolkitAdminV2ListOAuthIdpConfigsResponse(
    typing.TypedDict, total=False
):
    nextPageToken: str
    oauthIdpConfigs: _list[GoogleCloudIdentitytoolkitAdminV2OAuthIdpConfig]

@typing.type_check_only
class GoogleCloudIdentitytoolkitAdminV2ListTenantsResponse(
    typing.TypedDict, total=False
):
    nextPageToken: str
    tenants: _list[GoogleCloudIdentitytoolkitAdminV2Tenant]

@typing.type_check_only
class GoogleCloudIdentitytoolkitAdminV2MobileLinksConfig(typing.TypedDict, total=False):
    domain: typing.Literal[
        "DOMAIN_UNSPECIFIED", "FIREBASE_DYNAMIC_LINK_DOMAIN", "HOSTING_DOMAIN"
    ]

@typing.type_check_only
class GoogleCloudIdentitytoolkitAdminV2MonitoringConfig(typing.TypedDict, total=False):
    requestLogging: GoogleCloudIdentitytoolkitAdminV2RequestLogging

@typing.type_check_only
class GoogleCloudIdentitytoolkitAdminV2MultiFactorAuthConfig(
    typing.TypedDict, total=False
):
    enabledProviders: _list[typing.Literal["PROVIDER_UNSPECIFIED", "PHONE_SMS"]]
    providerConfigs: _list[GoogleCloudIdentitytoolkitAdminV2ProviderConfig]
    state: typing.Literal["STATE_UNSPECIFIED", "DISABLED", "ENABLED", "MANDATORY"]

@typing.type_check_only
class GoogleCloudIdentitytoolkitAdminV2MultiTenantConfig(typing.TypedDict, total=False):
    allowTenants: bool
    defaultTenantLocation: str

@typing.type_check_only
class GoogleCloudIdentitytoolkitAdminV2NotificationConfig(
    typing.TypedDict, total=False
):
    defaultLocale: str
    sendEmail: GoogleCloudIdentitytoolkitAdminV2SendEmail
    sendSms: GoogleCloudIdentitytoolkitAdminV2SendSms

@typing.type_check_only
class GoogleCloudIdentitytoolkitAdminV2OAuthIdpConfig(typing.TypedDict, total=False):
    clientId: str
    clientSecret: str
    displayName: str
    enabled: bool
    issuer: str
    name: str
    responseType: GoogleCloudIdentitytoolkitAdminV2OAuthResponseType

@typing.type_check_only
class GoogleCloudIdentitytoolkitAdminV2OAuthResponseType(typing.TypedDict, total=False):
    code: bool
    idToken: bool
    token: bool

@typing.type_check_only
class GoogleCloudIdentitytoolkitAdminV2PasswordPolicyConfig(
    typing.TypedDict, total=False
):
    forceUpgradeOnSignin: bool
    lastUpdateTime: str
    passwordPolicyEnforcementState: typing.Literal[
        "PASSWORD_POLICY_ENFORCEMENT_STATE_UNSPECIFIED", "OFF", "ENFORCE"
    ]
    passwordPolicyVersions: _list[
        GoogleCloudIdentitytoolkitAdminV2PasswordPolicyVersion
    ]

@typing.type_check_only
class GoogleCloudIdentitytoolkitAdminV2PasswordPolicyVersion(
    typing.TypedDict, total=False
):
    customStrengthOptions: GoogleCloudIdentitytoolkitAdminV2CustomStrengthOptions
    schemaVersion: int

@typing.type_check_only
class GoogleCloudIdentitytoolkitAdminV2Permissions(typing.TypedDict, total=False):
    disabledUserDeletion: bool
    disabledUserSignup: bool

@typing.type_check_only
class GoogleCloudIdentitytoolkitAdminV2PhoneNumber(typing.TypedDict, total=False):
    enabled: bool
    testPhoneNumbers: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudIdentitytoolkitAdminV2ProviderConfig(typing.TypedDict, total=False):
    state: typing.Literal["MFA_STATE_UNSPECIFIED", "DISABLED", "ENABLED", "MANDATORY"]
    totpProviderConfig: GoogleCloudIdentitytoolkitAdminV2TotpMfaProviderConfig

@typing.type_check_only
class GoogleCloudIdentitytoolkitAdminV2QuotaConfig(typing.TypedDict, total=False):
    signUpQuotaConfig: GoogleCloudIdentitytoolkitAdminV2TemporaryQuota

@typing.type_check_only
class GoogleCloudIdentitytoolkitAdminV2RecaptchaConfig(typing.TypedDict, total=False):
    emailPasswordEnforcementState: typing.Literal[
        "RECAPTCHA_PROVIDER_ENFORCEMENT_STATE_UNSPECIFIED", "OFF", "AUDIT", "ENFORCE"
    ]
    managedRules: _list[GoogleCloudIdentitytoolkitAdminV2RecaptchaManagedRule]
    phoneEnforcementState: typing.Literal[
        "RECAPTCHA_PROVIDER_ENFORCEMENT_STATE_UNSPECIFIED", "OFF", "AUDIT", "ENFORCE"
    ]
    recaptchaKeys: _list[GoogleCloudIdentitytoolkitAdminV2RecaptchaKey]
    tollFraudManagedRules: _list[
        GoogleCloudIdentitytoolkitAdminV2RecaptchaTollFraudManagedRule
    ]
    useAccountDefender: bool
    useSmsBotScore: bool
    useSmsTollFraudProtection: bool

@typing.type_check_only
class GoogleCloudIdentitytoolkitAdminV2RecaptchaKey(typing.TypedDict, total=False):
    key: str
    type: typing.Literal["CLIENT_TYPE_UNSPECIFIED", "WEB", "IOS", "ANDROID"]

@typing.type_check_only
class GoogleCloudIdentitytoolkitAdminV2RecaptchaManagedRule(
    typing.TypedDict, total=False
):
    action: typing.Literal["RECAPTCHA_ACTION_UNSPECIFIED", "BLOCK"]
    endScore: float

@typing.type_check_only
class GoogleCloudIdentitytoolkitAdminV2RecaptchaTollFraudManagedRule(
    typing.TypedDict, total=False
):
    action: typing.Literal["RECAPTCHA_ACTION_UNSPECIFIED", "BLOCK"]
    startScore: float

@typing.type_check_only
class GoogleCloudIdentitytoolkitAdminV2RequestLogging(typing.TypedDict, total=False):
    enabled: bool

@typing.type_check_only
class GoogleCloudIdentitytoolkitAdminV2SendEmail(typing.TypedDict, total=False):
    callbackUri: str
    changeEmailTemplate: GoogleCloudIdentitytoolkitAdminV2EmailTemplate
    dnsInfo: GoogleCloudIdentitytoolkitAdminV2DnsInfo
    legacyResetPasswordTemplate: GoogleCloudIdentitytoolkitAdminV2EmailTemplate
    method: typing.Literal["METHOD_UNSPECIFIED", "DEFAULT", "CUSTOM_SMTP"]
    resetPasswordTemplate: GoogleCloudIdentitytoolkitAdminV2EmailTemplate
    revertSecondFactorAdditionTemplate: GoogleCloudIdentitytoolkitAdminV2EmailTemplate
    smtp: GoogleCloudIdentitytoolkitAdminV2Smtp
    verifyEmailTemplate: GoogleCloudIdentitytoolkitAdminV2EmailTemplate

@typing.type_check_only
class GoogleCloudIdentitytoolkitAdminV2SendSms(typing.TypedDict, total=False):
    smsTemplate: GoogleCloudIdentitytoolkitAdminV2SmsTemplate
    useDeviceLocale: bool

@typing.type_check_only
class GoogleCloudIdentitytoolkitAdminV2SignInConfig(typing.TypedDict, total=False):
    allowDuplicateEmails: bool
    anonymous: GoogleCloudIdentitytoolkitAdminV2Anonymous
    email: GoogleCloudIdentitytoolkitAdminV2Email
    hashConfig: GoogleCloudIdentitytoolkitAdminV2HashConfig
    phoneNumber: GoogleCloudIdentitytoolkitAdminV2PhoneNumber

@typing.type_check_only
class GoogleCloudIdentitytoolkitAdminV2SmsRegionConfig(typing.TypedDict, total=False):
    allowByDefault: GoogleCloudIdentitytoolkitAdminV2AllowByDefault
    allowlistOnly: GoogleCloudIdentitytoolkitAdminV2AllowlistOnly

@typing.type_check_only
class GoogleCloudIdentitytoolkitAdminV2SmsTemplate(typing.TypedDict, total=False):
    content: str

@typing.type_check_only
class GoogleCloudIdentitytoolkitAdminV2Smtp(typing.TypedDict, total=False):
    host: str
    password: str
    port: int
    securityMode: typing.Literal["SECURITY_MODE_UNSPECIFIED", "SSL", "START_TLS"]
    senderEmail: str
    username: str

@typing.type_check_only
class GoogleCloudIdentitytoolkitAdminV2SpCertificate(typing.TypedDict, total=False):
    expiresAt: str
    x509Certificate: str

@typing.type_check_only
class GoogleCloudIdentitytoolkitAdminV2SpConfig(typing.TypedDict, total=False):
    callbackUri: str
    spCertificates: _list[GoogleCloudIdentitytoolkitAdminV2SpCertificate]
    spEntityId: str

@typing.type_check_only
class GoogleCloudIdentitytoolkitAdminV2TemporaryQuota(typing.TypedDict, total=False):
    quota: str
    quotaDuration: str
    startTime: str

@typing.type_check_only
class GoogleCloudIdentitytoolkitAdminV2Tenant(typing.TypedDict, total=False):
    allowPasswordSignup: bool
    autodeleteAnonymousUsers: bool
    client: GoogleCloudIdentitytoolkitAdminV2ClientPermissionConfig
    disableAuth: bool
    displayName: str
    emailPrivacyConfig: GoogleCloudIdentitytoolkitAdminV2EmailPrivacyConfig
    enableAnonymousUser: bool
    enableEmailLinkSignin: bool
    hashConfig: GoogleCloudIdentitytoolkitAdminV2HashConfig
    inheritance: GoogleCloudIdentitytoolkitAdminV2Inheritance
    mfaConfig: GoogleCloudIdentitytoolkitAdminV2MultiFactorAuthConfig
    mobileLinksConfig: GoogleCloudIdentitytoolkitAdminV2MobileLinksConfig
    monitoring: GoogleCloudIdentitytoolkitAdminV2MonitoringConfig
    name: str
    passwordPolicyConfig: GoogleCloudIdentitytoolkitAdminV2PasswordPolicyConfig
    recaptchaConfig: GoogleCloudIdentitytoolkitAdminV2RecaptchaConfig
    smsRegionConfig: GoogleCloudIdentitytoolkitAdminV2SmsRegionConfig
    testPhoneNumbers: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudIdentitytoolkitAdminV2TotpMfaProviderConfig(
    typing.TypedDict, total=False
):
    adjacentIntervals: int

@typing.type_check_only
class GoogleCloudIdentitytoolkitAdminV2Trigger(typing.TypedDict, total=False):
    functionUri: str
    updateTime: str

@typing.type_check_only
class GoogleCloudIdentitytoolkitV2AutoRetrievalInfo(typing.TypedDict, total=False):
    appSignatureHash: str

@typing.type_check_only
class GoogleCloudIdentitytoolkitV2CustomStrengthOptions(typing.TypedDict, total=False):
    containsLowercaseCharacter: bool
    containsNonAlphanumericCharacter: bool
    containsNumericCharacter: bool
    containsUppercaseCharacter: bool
    maxPasswordLength: int
    minPasswordLength: int

@typing.type_check_only
class GoogleCloudIdentitytoolkitV2FinalizeMfaEnrollmentRequest(
    typing.TypedDict, total=False
):
    displayName: str
    idToken: str
    phoneVerificationInfo: GoogleCloudIdentitytoolkitV2FinalizeMfaPhoneRequestInfo
    tenantId: str
    totpVerificationInfo: (
        GoogleCloudIdentitytoolkitV2FinalizeMfaTotpEnrollmentRequestInfo
    )

@typing.type_check_only
class GoogleCloudIdentitytoolkitV2FinalizeMfaEnrollmentResponse(
    typing.TypedDict, total=False
):
    idToken: str
    phoneAuthInfo: GoogleCloudIdentitytoolkitV2FinalizeMfaPhoneResponseInfo
    refreshToken: str
    totpAuthInfo: GoogleCloudIdentitytoolkitV2FinalizeMfaTotpEnrollmentResponseInfo

@typing.type_check_only
class GoogleCloudIdentitytoolkitV2FinalizeMfaPhoneRequestInfo(
    typing.TypedDict, total=False
):
    androidVerificationProof: str
    code: str
    phoneNumber: str
    sessionInfo: str

@typing.type_check_only
class GoogleCloudIdentitytoolkitV2FinalizeMfaPhoneResponseInfo(
    typing.TypedDict, total=False
):
    androidVerificationProof: str
    androidVerificationProofExpireTime: str
    phoneNumber: str

@typing.type_check_only
class GoogleCloudIdentitytoolkitV2FinalizeMfaSignInRequest(
    typing.TypedDict, total=False
):
    mfaEnrollmentId: str
    mfaPendingCredential: str
    phoneVerificationInfo: GoogleCloudIdentitytoolkitV2FinalizeMfaPhoneRequestInfo
    tenantId: str
    totpVerificationInfo: GoogleCloudIdentitytoolkitV2MfaTotpSignInRequestInfo

@typing.type_check_only
class GoogleCloudIdentitytoolkitV2FinalizeMfaSignInResponse(
    typing.TypedDict, total=False
):
    idToken: str
    phoneAuthInfo: GoogleCloudIdentitytoolkitV2FinalizeMfaPhoneResponseInfo
    refreshToken: str

@typing.type_check_only
class GoogleCloudIdentitytoolkitV2FinalizeMfaTotpEnrollmentRequestInfo(
    typing.TypedDict, total=False
):
    sessionInfo: str
    verificationCode: str

@typing.type_check_only
class GoogleCloudIdentitytoolkitV2FinalizeMfaTotpEnrollmentResponseInfo(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudIdentitytoolkitV2MfaTotpSignInRequestInfo(
    typing.TypedDict, total=False
):
    verificationCode: str

@typing.type_check_only
class GoogleCloudIdentitytoolkitV2PasswordPolicy(typing.TypedDict, total=False):
    allowedNonAlphanumericCharacters: _list[str]
    customStrengthOptions: GoogleCloudIdentitytoolkitV2CustomStrengthOptions
    enforcementState: typing.Literal["ENFORCEMENT_STATE_UNSPECIFIED", "OFF", "ENFORCE"]
    forceUpgradeOnSignin: bool
    schemaVersion: int

@typing.type_check_only
class GoogleCloudIdentitytoolkitV2RecaptchaConfig(typing.TypedDict, total=False):
    recaptchaEnforcementState: _list[
        GoogleCloudIdentitytoolkitV2RecaptchaEnforcementState
    ]
    recaptchaKey: str
    useSmsBotScore: bool
    useSmsTollFraudProtection: bool

@typing.type_check_only
class GoogleCloudIdentitytoolkitV2RecaptchaEnforcementState(
    typing.TypedDict, total=False
):
    enforcementState: typing.Literal[
        "ENFORCEMENT_STATE_UNSPECIFIED", "OFF", "AUDIT", "ENFORCE"
    ]
    provider: typing.Literal[
        "RECAPTCHA_PROVIDER_UNSPECIFIED", "EMAIL_PASSWORD_PROVIDER", "PHONE_PROVIDER"
    ]

@typing.type_check_only
class GoogleCloudIdentitytoolkitV2RevokeTokenRequest(typing.TypedDict, total=False):
    idToken: str
    providerId: str
    redirectUri: str
    tenantId: str
    token: str
    tokenType: typing.Literal[
        "TOKEN_TYPE_UNSPECIFIED", "REFRESH_TOKEN", "ACCESS_TOKEN", "CODE"
    ]

@typing.type_check_only
class GoogleCloudIdentitytoolkitV2RevokeTokenResponse(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudIdentitytoolkitV2StartMfaEnrollmentRequest(
    typing.TypedDict, total=False
):
    idToken: str
    phoneEnrollmentInfo: GoogleCloudIdentitytoolkitV2StartMfaPhoneRequestInfo
    tenantId: str
    totpEnrollmentInfo: GoogleCloudIdentitytoolkitV2StartMfaTotpEnrollmentRequestInfo

@typing.type_check_only
class GoogleCloudIdentitytoolkitV2StartMfaEnrollmentResponse(
    typing.TypedDict, total=False
):
    phoneSessionInfo: GoogleCloudIdentitytoolkitV2StartMfaPhoneResponseInfo
    totpSessionInfo: GoogleCloudIdentitytoolkitV2StartMfaTotpEnrollmentResponseInfo

@typing.type_check_only
class GoogleCloudIdentitytoolkitV2StartMfaPhoneRequestInfo(
    typing.TypedDict, total=False
):
    autoRetrievalInfo: GoogleCloudIdentitytoolkitV2AutoRetrievalInfo
    captchaResponse: str
    clientType: typing.Literal[
        "CLIENT_TYPE_UNSPECIFIED",
        "CLIENT_TYPE_WEB",
        "CLIENT_TYPE_ANDROID",
        "CLIENT_TYPE_IOS",
    ]
    iosReceipt: str
    iosSecret: str
    phoneNumber: str
    playIntegrityToken: str
    recaptchaToken: str
    recaptchaVersion: typing.Literal[
        "RECAPTCHA_VERSION_UNSPECIFIED", "RECAPTCHA_ENTERPRISE"
    ]
    safetyNetToken: str

@typing.type_check_only
class GoogleCloudIdentitytoolkitV2StartMfaPhoneResponseInfo(
    typing.TypedDict, total=False
):
    sessionInfo: str

@typing.type_check_only
class GoogleCloudIdentitytoolkitV2StartMfaSignInRequest(typing.TypedDict, total=False):
    mfaEnrollmentId: str
    mfaPendingCredential: str
    phoneSignInInfo: GoogleCloudIdentitytoolkitV2StartMfaPhoneRequestInfo
    tenantId: str

@typing.type_check_only
class GoogleCloudIdentitytoolkitV2StartMfaSignInResponse(typing.TypedDict, total=False):
    phoneResponseInfo: GoogleCloudIdentitytoolkitV2StartMfaPhoneResponseInfo

@typing.type_check_only
class GoogleCloudIdentitytoolkitV2StartMfaTotpEnrollmentRequestInfo(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudIdentitytoolkitV2StartMfaTotpEnrollmentResponseInfo(
    typing.TypedDict, total=False
):
    finalizeEnrollmentTime: str
    hashingAlgorithm: str
    periodSec: int
    sessionInfo: str
    sharedSecretKey: str
    verificationCodeLength: int

@typing.type_check_only
class GoogleCloudIdentitytoolkitV2WithdrawMfaRequest(typing.TypedDict, total=False):
    idToken: str
    mfaEnrollmentId: str
    tenantId: str

@typing.type_check_only
class GoogleCloudIdentitytoolkitV2WithdrawMfaResponse(typing.TypedDict, total=False):
    idToken: str
    refreshToken: str

@typing.type_check_only
class GoogleIamV1AuditConfig(typing.TypedDict, total=False):
    auditLogConfigs: _list[GoogleIamV1AuditLogConfig]
    service: str

@typing.type_check_only
class GoogleIamV1AuditLogConfig(typing.TypedDict, total=False):
    exemptedMembers: _list[str]
    logType: typing.Literal[
        "LOG_TYPE_UNSPECIFIED", "ADMIN_READ", "DATA_WRITE", "DATA_READ"
    ]

@typing.type_check_only
class GoogleIamV1Binding(typing.TypedDict, total=False):
    condition: GoogleTypeExpr
    members: _list[str]
    role: str

@typing.type_check_only
class GoogleIamV1GetIamPolicyRequest(typing.TypedDict, total=False):
    options: GoogleIamV1GetPolicyOptions

@typing.type_check_only
class GoogleIamV1GetPolicyOptions(typing.TypedDict, total=False):
    requestedPolicyVersion: int

@typing.type_check_only
class GoogleIamV1Policy(typing.TypedDict, total=False):
    auditConfigs: _list[GoogleIamV1AuditConfig]
    bindings: _list[GoogleIamV1Binding]
    etag: str
    version: int

@typing.type_check_only
class GoogleIamV1SetIamPolicyRequest(typing.TypedDict, total=False):
    policy: GoogleIamV1Policy
    updateMask: str

@typing.type_check_only
class GoogleIamV1TestIamPermissionsRequest(typing.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class GoogleIamV1TestIamPermissionsResponse(typing.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class GoogleProtobufEmpty(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleTypeExpr(typing.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str
