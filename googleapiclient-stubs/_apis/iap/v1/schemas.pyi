import typing

import typing_extensions
@typing.type_check_only
class AccessDeniedPageSettings(typing_extensions.TypedDict, total=False):
    accessDeniedPageUri: str

@typing.type_check_only
class AccessSettings(typing_extensions.TypedDict, total=False):
    corsSettings: CorsSettings
    gcipSettings: GcipSettings
    oauthSettings: OAuthSettings
    policyDelegationSettings: PolicyDelegationSettings

@typing.type_check_only
class ApplicationSettings(typing_extensions.TypedDict, total=False):
    accessDeniedPageSettings: AccessDeniedPageSettings
    cookieDomain: str
    csmSettings: CsmSettings

@typing.type_check_only
class Binding(typing_extensions.TypedDict, total=False):
    condition: Expr
    members: typing.List[str]
    role: str

@typing.type_check_only
class Brand(typing_extensions.TypedDict, total=False):
    applicationTitle: str
    name: str
    orgInternalOnly: bool
    supportEmail: str

@typing.type_check_only
class CorsSettings(typing_extensions.TypedDict, total=False):
    allowHttpOptions: bool

@typing.type_check_only
class CsmSettings(typing_extensions.TypedDict, total=False):
    rctokenAud: str

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Expr(typing_extensions.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str

@typing.type_check_only
class GcipSettings(typing_extensions.TypedDict, total=False):
    loginPageUri: str
    tenantIds: typing.List[str]

@typing.type_check_only
class GetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    options: GetPolicyOptions

@typing.type_check_only
class GetPolicyOptions(typing_extensions.TypedDict, total=False):
    requestedPolicyVersion: int

@typing.type_check_only
class IapSettings(typing_extensions.TypedDict, total=False):
    accessSettings: AccessSettings
    applicationSettings: ApplicationSettings
    name: str

@typing.type_check_only
class IdentityAwareProxyClient(typing_extensions.TypedDict, total=False):
    displayName: str
    name: str
    secret: str

@typing.type_check_only
class ListBrandsResponse(typing_extensions.TypedDict, total=False):
    brands: typing.List[Brand]

@typing.type_check_only
class ListIdentityAwareProxyClientsResponse(typing_extensions.TypedDict, total=False):
    identityAwareProxyClients: typing.List[IdentityAwareProxyClient]
    nextPageToken: str

@typing.type_check_only
class OAuthSettings(typing_extensions.TypedDict, total=False):
    loginHint: str

@typing.type_check_only
class Policy(typing_extensions.TypedDict, total=False):
    bindings: typing.List[Binding]
    etag: str
    version: int

@typing.type_check_only
class PolicyDelegationSettings(typing_extensions.TypedDict, total=False):
    iamPermission: str
    iamServiceName: str
    policyName: PolicyName
    resource: Resource

@typing.type_check_only
class PolicyName(typing_extensions.TypedDict, total=False):
    id: str
    region: str
    type: str

@typing.type_check_only
class ResetIdentityAwareProxyClientSecretRequest(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class Resource(typing_extensions.TypedDict, total=False):
    labels: typing.Dict[str, typing.Any]
    name: str
    service: str
    type: str

@typing.type_check_only
class SetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    policy: Policy

@typing.type_check_only
class TestIamPermissionsRequest(typing_extensions.TypedDict, total=False):
    permissions: typing.List[str]

@typing.type_check_only
class TestIamPermissionsResponse(typing_extensions.TypedDict, total=False):
    permissions: typing.List[str]
