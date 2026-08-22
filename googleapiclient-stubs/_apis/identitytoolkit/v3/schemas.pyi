import typing

_list = list

@typing.type_check_only
class CreateAuthUriResponse(typing.TypedDict, total=False):
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
class DeleteAccountResponse(typing.TypedDict, total=False):
    kind: str

@typing.type_check_only
class DownloadAccountResponse(typing.TypedDict, total=False):
    kind: str
    nextPageToken: str
    users: _list[UserInfo]

@typing.type_check_only
class EmailLinkSigninResponse(typing.TypedDict, total=False):
    email: str
    expiresIn: str
    idToken: str
    isNewUser: bool
    kind: str
    localId: str
    refreshToken: str

AlternativeEmailTemplate = typing.TypedDict(
    "AlternativeEmailTemplate",
    {
        "body": str,
        "format": str,
        "from": str,
        "fromDisplayName": str,
        "replyTo": str,
        "subject": str,
    },
    total=False,
)

@typing.type_check_only
class EmailTemplate(AlternativeEmailTemplate): ...

@typing.type_check_only
class GetAccountInfoResponse(typing.TypedDict, total=False):
    kind: str
    users: _list[UserInfo]

@typing.type_check_only
class GetOobConfirmationCodeResponse(typing.TypedDict, total=False):
    email: str
    kind: str
    oobCode: str

@typing.type_check_only
class GetRecaptchaParamResponse(typing.TypedDict, total=False):
    kind: str
    recaptchaSiteKey: str
    recaptchaStoken: str

@typing.type_check_only
class IdentitytoolkitRelyingpartyCreateAuthUriRequest(typing.TypedDict, total=False):
    appId: str
    authFlowType: str
    clientId: str
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
    tenantProjectNumber: str

@typing.type_check_only
class IdentitytoolkitRelyingpartyDeleteAccountRequest(typing.TypedDict, total=False):
    delegatedProjectNumber: str
    idToken: str
    localId: str

@typing.type_check_only
class IdentitytoolkitRelyingpartyDownloadAccountRequest(typing.TypedDict, total=False):
    delegatedProjectNumber: str
    maxResults: int
    nextPageToken: str
    targetProjectId: str

@typing.type_check_only
class IdentitytoolkitRelyingpartyEmailLinkSigninRequest(typing.TypedDict, total=False):
    email: str
    idToken: str
    oobCode: str

@typing.type_check_only
class IdentitytoolkitRelyingpartyGetAccountInfoRequest(typing.TypedDict, total=False):
    delegatedProjectNumber: str
    email: _list[str]
    idToken: str
    localId: _list[str]
    phoneNumber: _list[str]

@typing.type_check_only
class IdentitytoolkitRelyingpartyGetProjectConfigResponse(
    typing.TypedDict, total=False
):
    allowPasswordUser: bool
    apiKey: str
    authorizedDomains: _list[str]
    changeEmailTemplate: EmailTemplate
    dynamicLinksDomain: str
    enableAnonymousUser: bool
    idpConfig: _list[IdpConfig]
    legacyResetPasswordTemplate: EmailTemplate
    projectId: str
    resetPasswordTemplate: EmailTemplate
    useEmailSending: bool
    verifyEmailTemplate: EmailTemplate

@typing.type_check_only
class IdentitytoolkitRelyingpartyGetPublicKeysResponse(dict[str, typing.Any]): ...

@typing.type_check_only
class IdentitytoolkitRelyingpartyResetPasswordRequest(typing.TypedDict, total=False):
    email: str
    newPassword: str
    oldPassword: str
    oobCode: str

@typing.type_check_only
class IdentitytoolkitRelyingpartySendVerificationCodeRequest(
    typing.TypedDict, total=False
):
    iosReceipt: str
    iosSecret: str
    phoneNumber: str
    recaptchaToken: str

@typing.type_check_only
class IdentitytoolkitRelyingpartySendVerificationCodeResponse(
    typing.TypedDict, total=False
):
    sessionInfo: str

@typing.type_check_only
class IdentitytoolkitRelyingpartySetAccountInfoRequest(typing.TypedDict, total=False):
    captchaChallenge: str
    captchaResponse: str
    createdAt: str
    customAttributes: str
    delegatedProjectNumber: str
    deleteAttribute: _list[str]
    deleteProvider: _list[str]
    disableUser: bool
    displayName: str
    email: str
    emailVerified: bool
    idToken: str
    instanceId: str
    lastLoginAt: str
    localId: str
    oobCode: str
    password: str
    phoneNumber: str
    photoUrl: str
    provider: _list[str]
    returnSecureToken: bool
    upgradeToFederatedLogin: bool
    validSince: str

@typing.type_check_only
class IdentitytoolkitRelyingpartySetProjectConfigRequest(typing.TypedDict, total=False):
    allowPasswordUser: bool
    apiKey: str
    authorizedDomains: _list[str]
    changeEmailTemplate: EmailTemplate
    delegatedProjectNumber: str
    enableAnonymousUser: bool
    idpConfig: _list[IdpConfig]
    legacyResetPasswordTemplate: EmailTemplate
    resetPasswordTemplate: EmailTemplate
    useEmailSending: bool
    verifyEmailTemplate: EmailTemplate

@typing.type_check_only
class IdentitytoolkitRelyingpartySetProjectConfigResponse(
    typing.TypedDict, total=False
):
    projectId: str

@typing.type_check_only
class IdentitytoolkitRelyingpartySignOutUserRequest(typing.TypedDict, total=False):
    instanceId: str
    localId: str

@typing.type_check_only
class IdentitytoolkitRelyingpartySignOutUserResponse(typing.TypedDict, total=False):
    localId: str

@typing.type_check_only
class IdentitytoolkitRelyingpartySignupNewUserRequest(typing.TypedDict, total=False):
    captchaChallenge: str
    captchaResponse: str
    disabled: bool
    displayName: str
    email: str
    emailVerified: bool
    idToken: str
    instanceId: str
    localId: str
    password: str
    phoneNumber: str
    photoUrl: str
    tenantId: str
    tenantProjectNumber: str

@typing.type_check_only
class IdentitytoolkitRelyingpartyUploadAccountRequest(typing.TypedDict, total=False):
    allowOverwrite: bool
    blockSize: int
    cpuMemCost: int
    delegatedProjectNumber: str
    dkLen: int
    hashAlgorithm: str
    memoryCost: int
    parallelization: int
    rounds: int
    saltSeparator: str
    sanityCheck: bool
    signerKey: str
    targetProjectId: str
    users: _list[UserInfo]

@typing.type_check_only
class IdentitytoolkitRelyingpartyVerifyAssertionRequest(typing.TypedDict, total=False):
    autoCreate: bool
    delegatedProjectNumber: str
    idToken: str
    instanceId: str
    pendingIdToken: str
    postBody: str
    requestUri: str
    returnIdpCredential: bool
    returnRefreshToken: bool
    returnSecureToken: bool
    sessionId: str
    tenantId: str
    tenantProjectNumber: str

@typing.type_check_only
class IdentitytoolkitRelyingpartyVerifyCustomTokenRequest(
    typing.TypedDict, total=False
):
    delegatedProjectNumber: str
    instanceId: str
    returnSecureToken: bool
    token: str

@typing.type_check_only
class IdentitytoolkitRelyingpartyVerifyPasswordRequest(typing.TypedDict, total=False):
    captchaChallenge: str
    captchaResponse: str
    delegatedProjectNumber: str
    email: str
    idToken: str
    instanceId: str
    password: str
    pendingIdToken: str
    returnSecureToken: bool
    tenantId: str
    tenantProjectNumber: str

@typing.type_check_only
class IdentitytoolkitRelyingpartyVerifyPhoneNumberRequest(
    typing.TypedDict, total=False
):
    code: str
    idToken: str
    operation: str
    phoneNumber: str
    sessionInfo: str
    temporaryProof: str
    verificationProof: str

@typing.type_check_only
class IdentitytoolkitRelyingpartyVerifyPhoneNumberResponse(
    typing.TypedDict, total=False
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
class IdpConfig(typing.TypedDict, total=False):
    clientId: str
    enabled: bool
    experimentPercent: int
    provider: str
    secret: str
    whitelistedAudiences: _list[str]

@typing.type_check_only
class Relyingparty(typing.TypedDict, total=False):
    androidInstallApp: bool
    androidMinimumVersion: str
    androidPackageName: str
    canHandleCodeInApp: bool
    captchaResp: str
    challenge: str
    continueUrl: str
    email: str
    iOSAppStoreId: str
    iOSBundleId: str
    idToken: str
    kind: str
    newEmail: str
    requestType: str
    userIp: str

@typing.type_check_only
class ResetPasswordResponse(typing.TypedDict, total=False):
    email: str
    kind: str
    newEmail: str
    requestType: str

@typing.type_check_only
class SetAccountInfoResponse(typing.TypedDict, total=False):
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
    providerUserInfo: _list[dict[str, typing.Any]]
    refreshToken: str

@typing.type_check_only
class SignupNewUserResponse(typing.TypedDict, total=False):
    displayName: str
    email: str
    expiresIn: str
    idToken: str
    kind: str
    localId: str
    refreshToken: str

@typing.type_check_only
class UploadAccountResponse(typing.TypedDict, total=False):
    error: _list[dict[str, typing.Any]]
    kind: str

@typing.type_check_only
class UserInfo(typing.TypedDict, total=False):
    createdAt: str
    customAttributes: str
    customAuth: bool
    disabled: bool
    displayName: str
    email: str
    emailVerified: bool
    lastLoginAt: str
    localId: str
    passwordHash: str
    passwordUpdatedAt: float
    phoneNumber: str
    photoUrl: str
    providerUserInfo: _list[dict[str, typing.Any]]
    rawPassword: str
    salt: str
    screenName: str
    validSince: str
    version: int

@typing.type_check_only
class VerifyAssertionResponse(typing.TypedDict, total=False):
    action: str
    appInstallationUrl: str
    appScheme: str
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
    needConfirmation: bool
    needEmail: bool
    nickName: str
    oauthAccessToken: str
    oauthAuthorizationCode: str
    oauthExpireIn: int
    oauthIdToken: str
    oauthRequestToken: str
    oauthScope: str
    oauthTokenSecret: str
    originalEmail: str
    photoUrl: str
    providerId: str
    rawUserInfo: str
    refreshToken: str
    screenName: str
    timeZone: str
    verifiedProvider: _list[str]

@typing.type_check_only
class VerifyCustomTokenResponse(typing.TypedDict, total=False):
    expiresIn: str
    idToken: str
    isNewUser: bool
    kind: str
    refreshToken: str

@typing.type_check_only
class VerifyPasswordResponse(typing.TypedDict, total=False):
    displayName: str
    email: str
    expiresIn: str
    idToken: str
    kind: str
    localId: str
    oauthAccessToken: str
    oauthAuthorizationCode: str
    oauthExpireIn: int
    photoUrl: str
    refreshToken: str
    registered: bool
