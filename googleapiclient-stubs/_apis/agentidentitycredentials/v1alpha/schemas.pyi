import typing

import typing_extensions

_list = list

@typing.type_check_only
class GoogleCloudAgentidentitycredentialsV1alpha_ConsentRejected(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAgentidentitycredentialsV1alpha_FinalizeCredentialsRequest(
    typing_extensions.TypedDict, total=False
):
    consentNonce: str
    userId: str
    userIdValidationState: str

@typing.type_check_only
class GoogleCloudAgentidentitycredentialsV1alpha_FinalizeCredentialsResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAgentidentitycredentialsV1alpha_Pending(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAgentidentitycredentialsV1alpha_RetrieveCredentialsRequest(
    typing_extensions.TypedDict, total=False
):
    continueUri: str
    forceRefreshToken: str
    scopes: _list[str]
    userId: str

@typing.type_check_only
class GoogleCloudAgentidentitycredentialsV1alpha_RetrieveCredentialsResponse(
    typing_extensions.TypedDict, total=False
):
    consentRejected: GoogleCloudAgentidentitycredentialsV1alpha_ConsentRejected
    pending: GoogleCloudAgentidentitycredentialsV1alpha_Pending
    success: GoogleCloudAgentidentitycredentialsV1alpha_Success
    uriConsentRequired: GoogleCloudAgentidentitycredentialsV1alpha_UriConsentRequired

@typing.type_check_only
class GoogleCloudAgentidentitycredentialsV1alpha_Success(
    typing_extensions.TypedDict, total=False
):
    expireTime: str
    header: str
    scopes: _list[str]
    token: str

@typing.type_check_only
class GoogleCloudAgentidentitycredentialsV1alpha_UriConsentRequired(
    typing_extensions.TypedDict, total=False
):
    authorizationUri: str
    consentNonce: str
    uid: str
