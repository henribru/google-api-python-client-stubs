import typing

import typing_extensions

_list = list

@typing.type_check_only
class GoogleCloudIdentitytoolkitV1Argon2Parameters(
    typing_extensions.TypedDict, total=False
):
    associatedData: str
    hashLengthBytes: int
    hashType: typing_extensions.Literal[
        "HASH_TYPE_UNSPECIFIED", "ARGON2_D", "ARGON2_ID", "ARGON2_I"
    ]
    iterations: int
    memoryCostKib: int
    parallelism: int
    version: typing_extensions.Literal[
        "VERSION_UNSPECIFIED", "VERSION_10", "VERSION_13"
    ]

@typing.type_check_only
class GoogleCloudIdentitytoolkitV1AutoRetrievalInfo(
    typing_extensions.TypedDict, total=False
):
    appSignatureHash: str

@typing.type_check_only
class GoogleCloudIdentitytoolkitV1BatchDeleteAccountsRequest(
    typing_extensions.TypedDict, total=False
):
    force: bool
    localIds: _list[str]
    tenantId: str

@typing.type_check_only
class GoogleCloudIdentitytoolkitV1BatchDeleteAccountsResponse(
    typing_extensions.TypedDict, total=False
):
    errors: _list[GoogleCloudIdentitytoolkitV1BatchDeleteErrorInfo]

@typing.type_check_only
class GoogleCloudIdentitytoolkitV1BatchDeleteErrorInfo(
    typing_extensions.TypedDict, total=False
):
    index: int
    localId: str
    message: str

@typing.type_check_only
class GoogleCloudIdentitytoolkitV1CreateAuthUriRequest(
    typing_extensions.TypedDict, total=False
):
    appId: str
    authFlowType: str
    context: str
    continueUri: str
    customParameter: dict[str, typing.Any]
    hostedDomain: str
    identifier: str
    oauthConsumerKey: str
    oauthScope: str
    openidRealm: str
    otaApp: str
    providerId: str
    sessionId: str
    tenantId: str

@typing.type_check_only
class GoogleCloudIdentitytoolkitV1CreateAuthUriResponse(
    typing_extensions.TypedDict, total=False
):
    allProviders: _list[str]
    authUri: str
    captchaRequired: bool
    forExistingProvider: bool
    kind: str
    providerId: str
    registered: bool
    sessionId: str
    signinMethods: _list[str]

@typing.type_check_only
class GoogleCloudIdentitytoolkitV1CreateSessionCookieRequest(
    typing_extensions.TypedDict, total=False
):
    idToken: str
    tenantId: str
    validDuration: str

@typing.type_check_only
class GoogleCloudIdentitytoolkitV1CreateSessionCookieResponse(
    typing_extensions.TypedDict, total=False
):
    sessionCookie: str

@typing.type_check_only
class GoogleCloudIdentitytoolkitV1DeleteAccountRequest(
    typing_extensions.TypedDict, total=False
):
    delegatedProjectNumber: str
    idToken: str
    localId: str
    targetProjectId: str
    tenantId: str

@typing.type_check_only
class GoogleCloudIdentitytoolkitV1DeleteAccountResponse(
    typing_extensions.TypedDict, total=False
):
    kind: str

@typing.type_check_only
class GoogleCloudIdentitytoolkitV1DownloadAccountResponse(
    typing_extensions.TypedDict, total=False
):
    kind: str
    nextPageToken: str
    users: _list[GoogleCloudIdentitytoolkitV1UserInfo]

@typing.type_check_only
class GoogleCloudIdentitytoolkitV1EmailInfo(typing_extensions.TypedDict, total=False):
    emailAddress: str

AlternativeGoogleCloudIdentitytoolkitV1EmailTemplate = typing_extensions.TypedDict(
    "AlternativeGoogleCloudIdentitytoolkitV1EmailTemplate",
    {
        "body": str,
        "customized": bool,
        "disabled": bool,
        "format": typing_extensions.Literal[
            "EMAIL_BODY_FORMAT_UNSPECIFIED", "PLAINTEXT", "HTML"
        ],
        "from": str,
        "fromDisplayName": str,
        "fromLocalPart": str,
        "locale": str,
        "replyTo": str,
        "subject": str,
    },
    total=False,
)

@typing.type_check_only
class GoogleCloudIdentitytoolkitV1EmailTemplate(
    AlternativeGoogleCloudIdentitytoolkitV1EmailTemplate
): ...

@typing.type_check_only
class GoogleCloudIdentitytoolkitV1ErrorInfo(typing_extensions.TypedDict, total=False):
    index: int
    message: str

@typing.type_check_only
class GoogleCloudIdentitytoolkitV1FederatedUserIdentifier(
    typing_extensions.TypedDict, total=False
):
    providerId: str
    rawId: str

@typing.type_check_only
class GoogleCloudIdentitytoolkitV1GetAccountInfoRequest(
    typing_extensions.TypedDict, total=False
):
    delegatedProjectNumber: str
    email: _list[str]
    federatedUserId: _list[GoogleCloudIdentitytoolkitV1FederatedUserIdentifier]
    idToken: str
    initialEmail: _list[str]
    localId: _list[str]
    phoneNumber: _list[str]
    targetProjectId: str
    tenantId: str

@typing.type_check_only
class GoogleCloudIdentitytoolkitV1GetAccountInfoResponse(
    typing_extensions.TypedDict, total=False
):
    kind: str
    users: _list[GoogleCloudIdentitytoolkitV1UserInfo]

@typing.type_check_only
class GoogleCloudIdentitytoolkitV1GetOobCodeRequest(
    typing_extensions.TypedDict, total=False
):
    androidInstallApp: bool
    androidMinimumVersion: str
    androidPackageName: str
    canHandleCodeInApp: bool
    captchaResp: str
    challenge: str
    clientType: typing_extensions.Literal[
        "CLIENT_TYPE_UNSPECIFIED",
        "CLIENT_TYPE_WEB",
        "CLIENT_TYPE_ANDROID",
        "CLIENT_TYPE_IOS",
    ]
    continueUrl: str
    dynamicLinkDomain: str
    email: str
    iOSAppStoreId: str
    iOSBundleId: str
    idToken: str
    newEmail: str
    recaptchaVersion: typing_extensions.Literal[
        "RECAPTCHA_VERSION_UNSPECIFIED", "RECAPTCHA_ENTERPRISE"
    ]
    requestType: typing_extensions.Literal[
        "OOB_REQ_TYPE_UNSPECIFIED",
        "PASSWORD_RESET",
        "OLD_EMAIL_AGREE",
        "NEW_EMAIL_ACCEPT",
        "VERIFY_EMAIL",
        "RECOVER_EMAIL",
        "EMAIL_SIGNIN",
        "VERIFY_AND_CHANGE_EMAIL",
        "REVERT_SECOND_FACTOR_ADDITION",
    ]
    returnOobLink: bool
    targetProjectId: str
    tenantId: str
    userIp: str

@typing.type_check_only
class GoogleCloudIdentitytoolkitV1GetOobCodeResponse(
    typing_extensions.TypedDict, total=False
):
    email: str
    kind: str
    oobCode: str
    oobLink: str

@typing.type_check_only
class GoogleCloudIdentitytoolkitV1GetProjectConfigResponse(
    typing_extensions.TypedDict, total=False
):
    allowPasswordUser: bool
    apiKey: str
    authorizedDomains: _list[str]
    changeEmailTemplate: GoogleCloudIdentitytoolkitV1EmailTemplate
    dynamicLinksDomain: str
    enableAnonymousUser: bool
    idpConfig: _list[GoogleCloudIdentitytoolkitV1IdpConfig]
    legacyResetPasswordTemplate: GoogleCloudIdentitytoolkitV1EmailTemplate
    projectId: str
    resetPasswordTemplate: GoogleCloudIdentitytoolkitV1EmailTemplate
    revertSecondFactorAdditionTemplate: GoogleCloudIdentitytoolkitV1EmailTemplate
    useEmailSending: bool
    verifyEmailTemplate: GoogleCloudIdentitytoolkitV1EmailTemplate

@typing.type_check_only
class GoogleCloudIdentitytoolkitV1GetRecaptchaParamResponse(
    typing_extensions.TypedDict, total=False
):
    kind: str
    producerProjectNumber: str
    recaptchaSiteKey: str
    recaptchaStoken: str

@typing.type_check_only
class GoogleCloudIdentitytoolkitV1GetSessionCookiePublicKeysResponse(
    typing_extensions.TypedDict, total=False
):
    keys: _list[GoogleCloudIdentitytoolkitV1OpenIdConnectKey]

@typing.type_check_only
class GoogleCloudIdentitytoolkitV1IdpConfig(typing_extensions.TypedDict, total=False):
    clientId: str
    enabled: bool
    experimentPercent: int
    provider: typing_extensions.Literal[
        "PROVIDER_UNSPECIFIED",
        "MSLIVE",
        "GOOGLE",
        "FACEBOOK",
        "PAYPAL",
        "TWITTER",
        "YAHOO",
        "AOL",
        "GITHUB",
        "GOOGLE_PLAY_GAMES",
        "LINKEDIN",
        "IOS_GAME_CENTER",
    ]
    secret: str
    whitelistedAudiences: _list[str]

@typing.type_check_only
class GoogleCloudIdentitytoolkitV1IssueSamlResponseRequest(
    typing_extensions.TypedDict, total=False
):
    idToken: str
    rpId: str
    samlAppEntityId: str

@typing.type_check_only
class GoogleCloudIdentitytoolkitV1IssueSamlResponseResponse(
    typing_extensions.TypedDict, total=False
):
    acsEndpoint: str
    email: str
    firstName: str
    isNewUser: bool
    lastName: str
    relayState: str
    samlResponse: str

@typing.type_check_only
class GoogleCloudIdentitytoolkitV1MfaEnrollment(
    typing_extensions.TypedDict, total=False
):
    displayName: str
    emailInfo: GoogleCloudIdentitytoolkitV1EmailInfo
    enrolledAt: str
    mfaEnrollmentId: str
    phoneInfo: str
    totpInfo: GoogleCloudIdentitytoolkitV1TotpInfo
    unobfuscatedPhoneInfo: str

@typing.type_check_only
class GoogleCloudIdentitytoolkitV1MfaFactor(typing_extensions.TypedDict, total=False):
    displayName: str
    phoneInfo: str

@typing.type_check_only
class GoogleCloudIdentitytoolkitV1MfaInfo(typing_extensions.TypedDict, total=False):
    enrollments: _list[GoogleCloudIdentitytoolkitV1MfaEnrollment]

@typing.type_check_only
class GoogleCloudIdentitytoolkitV1OpenIdConnectKey(
    typing_extensions.TypedDict, total=False
):
    alg: str
    e: str
    kid: str
    kty: str
    n: str
    use: str

@typing.type_check_only
class GoogleCloudIdentitytoolkitV1ProviderUserInfo(
    typing_extensions.TypedDict, total=False
):
    displayName: str
    email: str
    federatedId: str
    phoneNumber: str
    photoUrl: str
    providerId: str
    rawId: str
    screenName: str

@typing.type_check_only
class GoogleCloudIdentitytoolkitV1QueryUserInfoRequest(
    typing_extensions.TypedDict, total=False
):
    expression: _list[GoogleCloudIdentitytoolkitV1SqlExpression]
    limit: str
    offset: str
    order: typing_extensions.Literal["ORDER_UNSPECIFIED", "ASC", "DESC"]
    returnUserInfo: bool
    sortBy: typing_extensions.Literal[
        "SORT_BY_FIELD_UNSPECIFIED",
        "USER_ID",
        "NAME",
        "CREATED_AT",
        "LAST_LOGIN_AT",
        "USER_EMAIL",
    ]
    tenantId: str

@typing.type_check_only
class GoogleCloudIdentitytoolkitV1QueryUserInfoResponse(
    typing_extensions.TypedDict, total=False
):
    recordsCount: str
    userInfo: _list[GoogleCloudIdentitytoolkitV1UserInfo]

@typing.type_check_only
class GoogleCloudIdentitytoolkitV1ResetPasswordRequest(
    typing_extensions.TypedDict, total=False
):
    email: str
    newPassword: str
    oldPassword: str
    oobCode: str
    tenantId: str

@typing.type_check_only
class GoogleCloudIdentitytoolkitV1ResetPasswordResponse(
    typing_extensions.TypedDict, total=False
):
    email: str
    kind: str
    mfaInfo: GoogleCloudIdentitytoolkitV1MfaEnrollment
    newEmail: str
    requestType: typing_extensions.Literal[
        "OOB_REQ_TYPE_UNSPECIFIED",
        "PASSWORD_RESET",
        "OLD_EMAIL_AGREE",
        "NEW_EMAIL_ACCEPT",
        "VERIFY_EMAIL",
        "RECOVER_EMAIL",
        "EMAIL_SIGNIN",
        "VERIFY_AND_CHANGE_EMAIL",
        "REVERT_SECOND_FACTOR_ADDITION",
    ]

@typing.type_check_only
class GoogleCloudIdentitytoolkitV1SendVerificationCodeRequest(
    typing_extensions.TypedDict, total=False
):
    autoRetrievalInfo: GoogleCloudIdentitytoolkitV1AutoRetrievalInfo
    captchaResponse: str
    clientType: typing_extensions.Literal[
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
    recaptchaVersion: typing_extensions.Literal[
        "RECAPTCHA_VERSION_UNSPECIFIED", "RECAPTCHA_ENTERPRISE"
    ]
    safetyNetToken: str
    tenantId: str

@typing.type_check_only
class GoogleCloudIdentitytoolkitV1SendVerificationCodeResponse(
    typing_extensions.TypedDict, total=False
):
    sessionInfo: str

@typing.type_check_only
class GoogleCloudIdentitytoolkitV1SetAccountInfoRequest(
    typing_extensions.TypedDict, total=False
):
    captchaChallenge: str
    captchaResponse: str
    createdAt: str
    customAttributes: str
    delegatedProjectNumber: str
    deleteAttribute: _list[
        typing_extensions.Literal[
            "USER_ATTRIBUTE_NAME_UNSPECIFIED",
            "EMAIL",
            "DISPLAY_NAME",
            "PROVIDER",
            "PHOTO_URL",
            "PASSWORD",
            "RAW_USER_INFO",
        ]
    ]
    deleteProvider: _list[str]
    disableUser: bool
    displayName: str
    email: str
    emailVerified: bool
    idToken: str
    instanceId: str
    lastLoginAt: str
    linkProviderUserInfo: GoogleCloudIdentitytoolkitV1ProviderUserInfo
    localId: str
    mfa: GoogleCloudIdentitytoolkitV1MfaInfo
    oobCode: str
    password: str
    phoneNumber: str
    photoUrl: str
    provider: _list[str]
    returnSecureToken: bool
    targetProjectId: str
    tenantId: str
    upgradeToFederatedLogin: bool
    validSince: str

@typing.type_check_only
class GoogleCloudIdentitytoolkitV1SetAccountInfoResponse(
    typing_extensions.TypedDict, total=False
):
    displayName: str
    email: str
    emailVerified: bool
    expiresIn: str
    idToken: str
    kind: str
    localId: str
    newEmail: str
    passwordHash: str
    photoUrl: str
    providerUserInfo: _list[GoogleCloudIdentitytoolkitV1ProviderUserInfo]
    refreshToken: str

@typing.type_check_only
class GoogleCloudIdentitytoolkitV1SignInWithCustomTokenRequest(
    typing_extensions.TypedDict, total=False
):
    delegatedProjectNumber: str
    instanceId: str
    returnSecureToken: bool
    tenantId: str
    token: str

@typing.type_check_only
class GoogleCloudIdentitytoolkitV1SignInWithCustomTokenResponse(
    typing_extensions.TypedDict, total=False
):
    expiresIn: str
    idToken: str
    isNewUser: bool
    kind: str
    refreshToken: str

@typing.type_check_only
class GoogleCloudIdentitytoolkitV1SignInWithEmailLinkRequest(
    typing_extensions.TypedDict, total=False
):
    email: str
    idToken: str
    oobCode: str
    tenantId: str

@typing.type_check_only
class GoogleCloudIdentitytoolkitV1SignInWithEmailLinkResponse(
    typing_extensions.TypedDict, total=False
):
    email: str
    expiresIn: str
    idToken: str
    isNewUser: bool
    kind: str
    localId: str
    mfaInfo: _list[GoogleCloudIdentitytoolkitV1MfaEnrollment]
    mfaPendingCredential: str
    refreshToken: str

@typing.type_check_only
class GoogleCloudIdentitytoolkitV1SignInWithGameCenterRequest(
    typing_extensions.TypedDict, total=False
):
    displayName: str
    gamePlayerId: str
    idToken: str
    playerId: str
    publicKeyUrl: str
    salt: str
    signature: str
    teamPlayerId: str
    tenantId: str
    timestamp: str

@typing.type_check_only
class GoogleCloudIdentitytoolkitV1SignInWithGameCenterResponse(
    typing_extensions.TypedDict, total=False
):
    displayName: str
    expiresIn: str
    gamePlayerId: str
    idToken: str
    isNewUser: bool
    localId: str
    playerId: str
    refreshToken: str
    teamPlayerId: str

@typing.type_check_only
class GoogleCloudIdentitytoolkitV1SignInWithIdpRequest(
    typing_extensions.TypedDict, total=False
):
    autoCreate: bool
    delegatedProjectNumber: str
    idToken: str
    pendingIdToken: str
    pendingToken: str
    postBody: str
    requestUri: str
    returnIdpCredential: bool
    returnRefreshToken: bool
    returnSecureToken: bool
    sessionId: str
    tenantId: str

@typing.type_check_only
class GoogleCloudIdentitytoolkitV1SignInWithIdpResponse(
    typing_extensions.TypedDict, total=False
):
    context: str
    dateOfBirth: str
    displayName: str
    email: str
    emailRecycled: bool
    emailVerified: bool
    errorMessage: str
    expiresIn: str
    federatedId: str
    firstName: str
    fullName: str
    idToken: str
    inputEmail: str
    isNewUser: bool
    kind: str
    language: str
    lastName: str
    localId: str
    mfaInfo: _list[GoogleCloudIdentitytoolkitV1MfaEnrollment]
    mfaPendingCredential: str
    needConfirmation: bool
    needEmail: bool
    nickName: str
    oauthAccessToken: str
    oauthAuthorizationCode: str
    oauthExpireIn: int
    oauthIdToken: str
    oauthRefreshToken: str
    oauthTokenSecret: str
    originalEmail: str
    pendingToken: str
    photoUrl: str
    providerId: str
    rawUserInfo: str
    refreshToken: str
    screenName: str
    tenantId: str
    timeZone: str
    verifiedProvider: _list[str]

@typing.type_check_only
class GoogleCloudIdentitytoolkitV1SignInWithPasswordRequest(
    typing_extensions.TypedDict, total=False
):
    captchaChallenge: str
    captchaResponse: str
    clientType: typing_extensions.Literal[
        "CLIENT_TYPE_UNSPECIFIED",
        "CLIENT_TYPE_WEB",
        "CLIENT_TYPE_ANDROID",
        "CLIENT_TYPE_IOS",
    ]
    delegatedProjectNumber: str
    email: str
    idToken: str
    instanceId: str
    password: str
    pendingIdToken: str
    recaptchaVersion: typing_extensions.Literal[
        "RECAPTCHA_VERSION_UNSPECIFIED", "RECAPTCHA_ENTERPRISE"
    ]
    returnSecureToken: bool
    tenantId: str

@typing.type_check_only
class GoogleCloudIdentitytoolkitV1SignInWithPasswordResponse(
    typing_extensions.TypedDict, total=False
):
    displayName: str
    email: str
    expiresIn: str
    idToken: str
    kind: str
    localId: str
    mfaInfo: _list[GoogleCloudIdentitytoolkitV1MfaEnrollment]
    mfaPendingCredential: str
    oauthAccessToken: str
    oauthAuthorizationCode: str
    oauthExpireIn: int
    profilePicture: str
    refreshToken: str
    registered: bool
    userNotifications: _list[GoogleCloudIdentitytoolkitV1UserNotification]

@typing.type_check_only
class GoogleCloudIdentitytoolkitV1SignInWithPhoneNumberRequest(
    typing_extensions.TypedDict, total=False
):
    code: str
    idToken: str
    operation: typing_extensions.Literal[
        "VERIFY_OP_UNSPECIFIED", "SIGN_UP_OR_IN", "REAUTH", "UPDATE", "LINK"
    ]
    phoneNumber: str
    sessionInfo: str
    temporaryProof: str
    tenantId: str
    verificationProof: str

@typing.type_check_only
class GoogleCloudIdentitytoolkitV1SignInWithPhoneNumberResponse(
    typing_extensions.TypedDict, total=False
):
    expiresIn: str
    idToken: str
    isNewUser: bool
    localId: str
    phoneNumber: str
    refreshToken: str
    temporaryProof: str
    temporaryProofExpiresIn: str
    verificationProof: str
    verificationProofExpiresIn: str

@typing.type_check_only
class GoogleCloudIdentitytoolkitV1SignUpRequest(
    typing_extensions.TypedDict, total=False
):
    captchaChallenge: str
    captchaResponse: str
    clientType: typing_extensions.Literal[
        "CLIENT_TYPE_UNSPECIFIED",
        "CLIENT_TYPE_WEB",
        "CLIENT_TYPE_ANDROID",
        "CLIENT_TYPE_IOS",
    ]
    disabled: bool
    displayName: str
    email: str
    emailVerified: bool
    idToken: str
    instanceId: str
    localId: str
    mfaInfo: _list[GoogleCloudIdentitytoolkitV1MfaFactor]
    password: str
    phoneNumber: str
    photoUrl: str
    recaptchaVersion: typing_extensions.Literal[
        "RECAPTCHA_VERSION_UNSPECIFIED", "RECAPTCHA_ENTERPRISE"
    ]
    targetProjectId: str
    tenantId: str

@typing.type_check_only
class GoogleCloudIdentitytoolkitV1SignUpResponse(
    typing_extensions.TypedDict, total=False
):
    displayName: str
    email: str
    expiresIn: str
    idToken: str
    kind: str
    localId: str
    refreshToken: str

@typing.type_check_only
class GoogleCloudIdentitytoolkitV1SqlExpression(
    typing_extensions.TypedDict, total=False
):
    email: str
    phoneNumber: str
    userId: str

@typing.type_check_only
class GoogleCloudIdentitytoolkitV1TotpInfo(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudIdentitytoolkitV1UploadAccountRequest(
    typing_extensions.TypedDict, total=False
):
    allowOverwrite: bool
    argon2Parameters: GoogleCloudIdentitytoolkitV1Argon2Parameters
    blockSize: int
    cpuMemCost: int
    delegatedProjectNumber: str
    dkLen: int
    hashAlgorithm: str
    memoryCost: int
    parallelization: int
    passwordHashOrder: typing_extensions.Literal[
        "UNSPECIFIED_ORDER", "SALT_AND_PASSWORD", "PASSWORD_AND_SALT"
    ]
    rounds: int
    saltSeparator: str
    sanityCheck: bool
    signerKey: str
    tenantId: str
    users: _list[GoogleCloudIdentitytoolkitV1UserInfo]

@typing.type_check_only
class GoogleCloudIdentitytoolkitV1UploadAccountResponse(
    typing_extensions.TypedDict, total=False
):
    error: _list[GoogleCloudIdentitytoolkitV1ErrorInfo]
    kind: str

@typing.type_check_only
class GoogleCloudIdentitytoolkitV1UserInfo(typing_extensions.TypedDict, total=False):
    createdAt: str
    customAttributes: str
    customAuth: bool
    dateOfBirth: str
    disabled: bool
    displayName: str
    email: str
    emailLinkSignin: bool
    emailVerified: bool
    initialEmail: str
    language: str
    lastLoginAt: str
    lastRefreshAt: str
    localId: str
    mfaInfo: _list[GoogleCloudIdentitytoolkitV1MfaEnrollment]
    passwordHash: str
    passwordUpdatedAt: float
    phoneNumber: str
    photoUrl: str
    providerUserInfo: _list[GoogleCloudIdentitytoolkitV1ProviderUserInfo]
    rawPassword: str
    salt: str
    screenName: str
    tenantId: str
    timeZone: str
    validSince: str
    version: int

@typing.type_check_only
class GoogleCloudIdentitytoolkitV1UserNotification(
    typing_extensions.TypedDict, total=False
):
    notificationCode: typing_extensions.Literal[
        "NOTIFICATION_CODE_UNSPECIFIED",
        "MISSING_LOWERCASE_CHARACTER",
        "MISSING_UPPERCASE_CHARACTER",
        "MISSING_NUMERIC_CHARACTER",
        "MISSING_NON_ALPHANUMERIC_CHARACTER",
        "MINIMUM_PASSWORD_LENGTH",
        "MAXIMUM_PASSWORD_LENGTH",
    ]
    notificationMessage: str

@typing.type_check_only
class GoogleCloudIdentitytoolkitV1VerifyIosClientRequest(
    typing_extensions.TypedDict, total=False
):
    appToken: str
    isSandbox: bool

@typing.type_check_only
class GoogleCloudIdentitytoolkitV1VerifyIosClientResponse(
    typing_extensions.TypedDict, total=False
):
    receipt: str
    suggestedTimeout: str
