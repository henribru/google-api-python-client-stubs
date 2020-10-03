import typing

import typing_extensions

class IdentitytoolkitRelyingpartyDeleteAccountRequest(
    typing_extensions.TypedDict, total=False
):
    idToken: str
    delegatedProjectNumber: str
    localId: str

class IdentitytoolkitRelyingpartyVerifyCustomTokenRequest(
    typing_extensions.TypedDict, total=False
):
    token: str
    delegatedProjectNumber: str
    returnSecureToken: bool
    instanceId: str

class IdentitytoolkitRelyingpartySendVerificationCodeResponse(
    typing_extensions.TypedDict, total=False
):
    sessionInfo: str

class VerifyAssertionResponse(typing_extensions.TypedDict, total=False):
    oauthRequestToken: str
    firstName: str
    fullName: str
    federatedId: str
    providerId: str
    kind: str
    oauthExpireIn: int
    photoUrl: str
    displayName: str
    oauthTokenSecret: str
    appScheme: str
    oauthAuthorizationCode: str
    errorMessage: str
    action: str
    appInstallationUrl: str
    oauthAccessToken: str
    timeZone: str
    expiresIn: str
    emailRecycled: bool
    verifiedProvider: typing.List[str]
    oauthScope: str
    nickName: str
    rawUserInfo: str
    localId: str
    lastName: str
    emailVerified: bool
    oauthIdToken: str
    originalEmail: str
    dateOfBirth: str
    context: str
    idToken: str
    needConfirmation: bool
    screenName: str
    inputEmail: str
    refreshToken: str
    language: str
    needEmail: bool
    email: str
    isNewUser: bool

class SetAccountInfoResponse(typing_extensions.TypedDict, total=False):
    displayName: str
    refreshToken: str
    newEmail: str
    email: str
    passwordHash: str
    providerUserInfo: typing.List[typing.Dict[str, typing.Any]]
    kind: str
    expiresIn: str
    photoUrl: str
    idToken: str
    emailVerified: bool
    localId: str

class IdentitytoolkitRelyingpartySendVerificationCodeRequest(
    typing_extensions.TypedDict, total=False
):
    iosSecret: str
    recaptchaToken: str
    phoneNumber: str
    iosReceipt: str

class GetOobConfirmationCodeResponse(typing_extensions.TypedDict, total=False):
    email: str
    oobCode: str
    kind: str

class UploadAccountResponse(typing_extensions.TypedDict, total=False):
    kind: str
    error: typing.List[typing.Dict[str, typing.Any]]

class ResetPasswordResponse(typing_extensions.TypedDict, total=False):
    kind: str
    requestType: str
    newEmail: str
    email: str

class VerifyCustomTokenResponse(typing_extensions.TypedDict, total=False):
    kind: str
    isNewUser: bool
    refreshToken: str
    idToken: str
    expiresIn: str

class IdentitytoolkitRelyingpartyEmailLinkSigninRequest(
    typing_extensions.TypedDict, total=False
):
    oobCode: str
    email: str
    idToken: str

class IdentitytoolkitRelyingpartyGetProjectConfigResponse(
    typing_extensions.TypedDict, total=False
):
    legacyResetPasswordTemplate: EmailTemplate
    enableAnonymousUser: bool
    authorizedDomains: typing.List[str]
    projectId: str
    apiKey: str
    useEmailSending: bool
    allowPasswordUser: bool
    idpConfig: typing.List[IdpConfig]
    verifyEmailTemplate: EmailTemplate
    resetPasswordTemplate: EmailTemplate
    changeEmailTemplate: EmailTemplate
    dynamicLinksDomain: str

class IdentitytoolkitRelyingpartySignOutUserResponse(
    typing_extensions.TypedDict, total=False
):
    localId: str

class SignupNewUserResponse(typing_extensions.TypedDict, total=False):
    refreshToken: str
    email: str
    displayName: str
    localId: str
    idToken: str
    kind: str
    expiresIn: str

class IdentitytoolkitRelyingpartySignOutUserRequest(
    typing_extensions.TypedDict, total=False
):
    localId: str
    instanceId: str

class IdentitytoolkitRelyingpartySignupNewUserRequest(
    typing_extensions.TypedDict, total=False
):
    tenantId: str
    captchaResponse: str
    email: str
    disabled: bool
    emailVerified: bool
    phoneNumber: str
    localId: str
    tenantProjectNumber: str
    instanceId: str
    password: str
    captchaChallenge: str
    photoUrl: str
    idToken: str
    displayName: str

class IdentitytoolkitRelyingpartyGetPublicKeysResponse(
    typing.Dict[str, typing.Any]
): ...

class IdentitytoolkitRelyingpartyVerifyAssertionRequest(
    typing_extensions.TypedDict, total=False
):
    pendingIdToken: str
    returnRefreshToken: bool
    returnIdpCredential: bool
    idToken: str
    requestUri: str
    delegatedProjectNumber: str
    autoCreate: bool
    tenantProjectNumber: str
    sessionId: str
    instanceId: str
    postBody: str
    tenantId: str
    returnSecureToken: bool

class IdentitytoolkitRelyingpartyGetAccountInfoRequest(
    typing_extensions.TypedDict, total=False
):
    idToken: str
    email: typing.List[str]
    localId: typing.List[str]
    delegatedProjectNumber: str
    phoneNumber: typing.List[str]

class IdentitytoolkitRelyingpartySetAccountInfoRequest(
    typing_extensions.TypedDict, total=False
):
    disableUser: bool
    upgradeToFederatedLogin: bool
    returnSecureToken: bool
    oobCode: str
    instanceId: str
    captchaResponse: str
    phoneNumber: str
    password: str
    captchaChallenge: str
    provider: typing.List[str]
    createdAt: str
    deleteAttribute: typing.List[str]
    localId: str
    deleteProvider: typing.List[str]
    photoUrl: str
    lastLoginAt: str
    validSince: str
    delegatedProjectNumber: str
    customAttributes: str
    idToken: str
    email: str
    emailVerified: bool
    displayName: str

class CreateAuthUriResponse(typing_extensions.TypedDict, total=False):
    forExistingProvider: bool
    kind: str
    providerId: str
    registered: bool
    captchaRequired: bool
    sessionId: str
    allProviders: typing.List[str]
    signinMethods: typing.List[str]
    authUri: str

class Relyingparty(typing_extensions.TypedDict, total=False):
    androidInstallApp: bool
    continueUrl: str
    challenge: str
    androidPackageName: str
    userIp: str
    email: str
    iOSBundleId: str
    iOSAppStoreId: str
    requestType: str
    idToken: str
    newEmail: str
    canHandleCodeInApp: bool
    androidMinimumVersion: str
    kind: str
    captchaResp: str

class GetRecaptchaParamResponse(typing_extensions.TypedDict, total=False):
    recaptchaStoken: str
    recaptchaSiteKey: str
    kind: str

class IdentitytoolkitRelyingpartyCreateAuthUriRequest(
    typing_extensions.TypedDict, total=False
):
    customParameter: typing.Dict[str, typing.Any]
    oauthConsumerKey: str
    identifier: str
    sessionId: str
    tenantId: str
    context: str
    hostedDomain: str
    providerId: str
    otaApp: str
    oauthScope: str
    tenantProjectNumber: str
    authFlowType: str
    continueUri: str
    openidRealm: str
    appId: str
    clientId: str

class IdentitytoolkitRelyingpartySetProjectConfigRequest(
    typing_extensions.TypedDict, total=False
):
    authorizedDomains: typing.List[str]
    delegatedProjectNumber: str
    apiKey: str
    allowPasswordUser: bool
    enableAnonymousUser: bool
    verifyEmailTemplate: EmailTemplate
    useEmailSending: bool
    changeEmailTemplate: EmailTemplate
    legacyResetPasswordTemplate: EmailTemplate
    resetPasswordTemplate: EmailTemplate
    idpConfig: typing.List[IdpConfig]

class IdentitytoolkitRelyingpartyVerifyPasswordRequest(
    typing_extensions.TypedDict, total=False
):
    captchaResponse: str
    delegatedProjectNumber: str
    tenantProjectNumber: str
    password: str
    email: str
    idToken: str
    instanceId: str
    tenantId: str
    pendingIdToken: str
    returnSecureToken: bool
    captchaChallenge: str

class VerifyPasswordResponse(typing_extensions.TypedDict, total=False):
    registered: bool
    oauthExpireIn: int
    oauthAuthorizationCode: str
    displayName: str
    email: str
    idToken: str
    refreshToken: str
    expiresIn: str
    kind: str
    photoUrl: str
    oauthAccessToken: str
    localId: str

class IdentitytoolkitRelyingpartyVerifyPhoneNumberResponse(
    typing_extensions.TypedDict, total=False
):
    localId: str
    isNewUser: bool
    temporaryProofExpiresIn: str
    verificationProof: str
    refreshToken: str
    phoneNumber: str
    temporaryProof: str
    expiresIn: str
    verificationProofExpiresIn: str
    idToken: str

class GetAccountInfoResponse(typing_extensions.TypedDict, total=False):
    kind: str
    users: typing.List[UserInfo]

class IdentitytoolkitRelyingpartyUploadAccountRequest(
    typing_extensions.TypedDict, total=False
):
    targetProjectId: str
    dkLen: int
    users: typing.List[UserInfo]
    saltSeparator: str
    delegatedProjectNumber: str
    sanityCheck: bool
    parallelization: int
    blockSize: int
    allowOverwrite: bool
    signerKey: str
    hashAlgorithm: str
    rounds: int
    memoryCost: int
    cpuMemCost: int

class IdentitytoolkitRelyingpartyDownloadAccountRequest(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    targetProjectId: str
    delegatedProjectNumber: str
    maxResults: int

EmailTemplate = typing_extensions.TypedDict(
    "EmailTemplate",
    {
        "format": str,
        "from": str,
        "replyTo": str,
        "subject": str,
        "fromDisplayName": str,
        "body": str,
    },
    total=False,
)

class EmailLinkSigninResponse(typing_extensions.TypedDict, total=False):
    idToken: str
    refreshToken: str
    email: str
    expiresIn: str
    kind: str
    isNewUser: bool
    localId: str

class IdentitytoolkitRelyingpartyResetPasswordRequest(
    typing_extensions.TypedDict, total=False
):
    email: str
    oobCode: str
    newPassword: str
    oldPassword: str

class UserInfo(typing_extensions.TypedDict, total=False):
    screenName: str
    customAttributes: str
    passwordHash: str
    emailVerified: bool
    createdAt: str
    photoUrl: str
    displayName: str
    lastLoginAt: str
    version: int
    localId: str
    validSince: str
    disabled: bool
    passwordUpdatedAt: float
    customAuth: bool
    phoneNumber: str
    email: str
    salt: str
    rawPassword: str
    providerUserInfo: typing.List[typing.Dict[str, typing.Any]]

class IdpConfig(typing_extensions.TypedDict, total=False):
    whitelistedAudiences: typing.List[str]
    experimentPercent: int
    clientId: str
    provider: str
    secret: str
    enabled: bool

class DeleteAccountResponse(typing_extensions.TypedDict, total=False):
    kind: str

class IdentitytoolkitRelyingpartyVerifyPhoneNumberRequest(
    typing_extensions.TypedDict, total=False
):
    temporaryProof: str
    code: str
    verificationProof: str
    operation: str
    sessionInfo: str
    idToken: str
    phoneNumber: str

class IdentitytoolkitRelyingpartySetProjectConfigResponse(
    typing_extensions.TypedDict, total=False
):
    projectId: str

class DownloadAccountResponse(typing_extensions.TypedDict, total=False):
    kind: str
    nextPageToken: str
    users: typing.List[UserInfo]
