import typing

import typing_extensions

class CorsSettings(typing_extensions.TypedDict, total=False):
    allowHttpOptions: bool

class GcipSettings(typing_extensions.TypedDict, total=False):
    loginPageUri: str
    tenantIds: typing.List[str]

class GetPolicyOptions(typing_extensions.TypedDict, total=False):
    requestedPolicyVersion: int

class ApplicationSettings(typing_extensions.TypedDict, total=False):
    csmSettings: CsmSettings
    cookieDomain: str
    accessDeniedPageSettings: AccessDeniedPageSettings

class Empty(typing_extensions.TypedDict, total=False): ...

class PolicyName(typing_extensions.TypedDict, total=False):
    id: str
    type: str
    region: str

class OAuthSettings(typing_extensions.TypedDict, total=False):
    clientId: str
    loginHint: str

class ListIdentityAwareProxyClientsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    identityAwareProxyClients: typing.List[IdentityAwareProxyClient]

class IapSettings(typing_extensions.TypedDict, total=False):
    applicationSettings: ApplicationSettings
    accessSettings: AccessSettings
    name: str

class SetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    policy: Policy

class CsmSettings(typing_extensions.TypedDict, total=False):
    rctokenAud: str

class IdentityAwareProxyClient(typing_extensions.TypedDict, total=False):
    displayName: str
    name: str
    secret: str

class PolicyDelegationSettings(typing_extensions.TypedDict, total=False):
    iamPermission: str
    policyName: PolicyName
    iamServiceName: str
    resource: Resource

class Expr(typing_extensions.TypedDict, total=False):
    description: str
    location: str
    title: str
    expression: str

class Policy(typing_extensions.TypedDict, total=False):
    etag: str
    bindings: typing.List[Binding]
    version: int

class Resource(typing_extensions.TypedDict, total=False):
    type: str
    labels: typing.Dict[str, typing.Any]
    service: str
    name: str

class AccessDeniedPageSettings(typing_extensions.TypedDict, total=False):
    accessDeniedPageUri: str

class TestIamPermissionsResponse(typing_extensions.TypedDict, total=False):
    permissions: typing.List[str]

class TestIamPermissionsRequest(typing_extensions.TypedDict, total=False):
    permissions: typing.List[str]

class GetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    options: GetPolicyOptions

class Brand(typing_extensions.TypedDict, total=False):
    orgInternalOnly: bool
    name: str
    applicationTitle: str
    supportEmail: str

class Binding(typing_extensions.TypedDict, total=False):
    bindingId: str
    members: typing.List[str]
    condition: Expr
    role: str

class ListBrandsResponse(typing_extensions.TypedDict, total=False):
    brands: typing.List[Brand]

class AccessSettings(typing_extensions.TypedDict, total=False):
    policyDelegationSettings: PolicyDelegationSettings
    corsSettings: CorsSettings
    oauthSettings: OAuthSettings
    gcipSettings: GcipSettings

class ResetIdentityAwareProxyClientSecretRequest(
    typing_extensions.TypedDict, total=False
): ...
