import typing

_list = list

@typing.type_check_only
class GoogleCloudAgentidentitycredentialsV1beta_ConsentRejected(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAgentidentitycredentialsV1beta_FinalizeCredentialsRequest(
    typing.TypedDict, total=False
):
    consentNonce: str
    userId: str
    userIdValidationState: str

@typing.type_check_only
class GoogleCloudAgentidentitycredentialsV1beta_FinalizeCredentialsResponse(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAgentidentitycredentialsV1beta_Pending(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAgentidentitycredentialsV1beta_RetrieveCredentialsRequest(
    typing.TypedDict, total=False
):
    continueUri: str
    forceRefreshToken: str
    scopes: _list[str]
    userId: str

@typing.type_check_only
class GoogleCloudAgentidentitycredentialsV1beta_RetrieveCredentialsResponse(
    typing.TypedDict, total=False
):
    consentRejected: GoogleCloudAgentidentitycredentialsV1beta_ConsentRejected
    pending: GoogleCloudAgentidentitycredentialsV1beta_Pending
    success: GoogleCloudAgentidentitycredentialsV1beta_Success
    uriConsentRequired: GoogleCloudAgentidentitycredentialsV1beta_UriConsentRequired

@typing.type_check_only
class GoogleCloudAgentidentitycredentialsV1beta_Success(typing.TypedDict, total=False):
    expireTime: str
    header: str
    scopes: _list[str]
    token: str

@typing.type_check_only
class GoogleCloudAgentidentitycredentialsV1beta_UriConsentRequired(
    typing.TypedDict, total=False
):
    authorizationUri: str
    consentNonce: str
    uid: str
