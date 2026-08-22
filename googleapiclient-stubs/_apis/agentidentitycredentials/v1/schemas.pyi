import typing

_list = list

@typing.type_check_only
class GoogleCloudAgentidentitycredentialsV1_ConsentRejected(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAgentidentitycredentialsV1_FinalizeCredentialsRequest(
    typing.TypedDict, total=False
):
    consentNonce: str
    userId: str
    userIdValidationState: str

@typing.type_check_only
class GoogleCloudAgentidentitycredentialsV1_FinalizeCredentialsResponse(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAgentidentitycredentialsV1_Pending(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleCloudAgentidentitycredentialsV1_RetrieveCredentialsRequest(
    typing.TypedDict, total=False
):
    continueUri: str
    forceRefreshToken: str
    scopes: _list[str]
    userId: str

@typing.type_check_only
class GoogleCloudAgentidentitycredentialsV1_RetrieveCredentialsResponse(
    typing.TypedDict, total=False
):
    consentRejected: GoogleCloudAgentidentitycredentialsV1_ConsentRejected
    pending: GoogleCloudAgentidentitycredentialsV1_Pending
    success: GoogleCloudAgentidentitycredentialsV1_Success
    uriConsentRequired: GoogleCloudAgentidentitycredentialsV1_UriConsentRequired

@typing.type_check_only
class GoogleCloudAgentidentitycredentialsV1_Success(typing.TypedDict, total=False):
    expireTime: str
    header: str
    scopes: _list[str]
    token: str

@typing.type_check_only
class GoogleCloudAgentidentitycredentialsV1_UriConsentRequired(
    typing.TypedDict, total=False
):
    authorizationUri: str
    consentNonce: str
    uid: str
