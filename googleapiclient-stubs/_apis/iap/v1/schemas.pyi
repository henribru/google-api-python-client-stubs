import typing

import typing_extensions

_list = list

@typing.type_check_only
class AccessDeniedPageSettings(typing_extensions.TypedDict, total=False):
    accessDeniedPageUri: str
    generateTroubleshootingUri: bool
    remediationTokenGenerationEnabled: bool

@typing.type_check_only
class AccessSettings(typing_extensions.TypedDict, total=False):
    allowedDomainsSettings: AllowedDomainsSettings
    corsSettings: CorsSettings
    gcipSettings: GcipSettings
    identitySources: _list[
        typing_extensions.Literal[
            "IDENTITY_SOURCE_UNSPECIFIED", "WORKFORCE_IDENTITY_FEDERATION"
        ]
    ]
    oauthSettings: OAuthSettings
    policyDelegationSettings: PolicyDelegationSettings
    reauthSettings: ReauthSettings
    workforceIdentitySettings: WorkforceIdentitySettings

@typing.type_check_only
class AllowedDomainsSettings(typing_extensions.TypedDict, total=False):
    domains: _list[str]
    enable: bool

@typing.type_check_only
class ApplicationSettings(typing_extensions.TypedDict, total=False):
    accessDeniedPageSettings: AccessDeniedPageSettings
    attributePropagationSettings: AttributePropagationSettings
    cookieDomain: str
    csmSettings: CsmSettings

@typing.type_check_only
class AttributePropagationSettings(typing_extensions.TypedDict, total=False):
    enable: bool
    expression: str
    outputCredentials: _list[
        typing_extensions.Literal[
            "OUTPUT_CREDENTIALS_UNSPECIFIED", "HEADER", "JWT", "RCTOKEN"
        ]
    ]

@typing.type_check_only
class Binding(typing_extensions.TypedDict, total=False):
    condition: Expr
    members: _list[str]
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
    tenantIds: _list[str]

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
    brands: _list[Brand]

@typing.type_check_only
class ListIdentityAwareProxyClientsResponse(typing_extensions.TypedDict, total=False):
    identityAwareProxyClients: _list[IdentityAwareProxyClient]
    nextPageToken: str

@typing.type_check_only
class ListTunnelDestGroupsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    tunnelDestGroups: _list[TunnelDestGroup]

@typing.type_check_only
class NextStateOfTags(typing_extensions.TypedDict, total=False):
    tagsFullState: TagsFullState
    tagsFullStateForChildResource: TagsFullStateForChildResource
    tagsPartialState: TagsPartialState

@typing.type_check_only
class OAuth2(typing_extensions.TypedDict, total=False):
    clientId: str
    clientSecret: str
    clientSecretSha256: str

@typing.type_check_only
class OAuthSettings(typing_extensions.TypedDict, total=False):
    loginHint: str
    programmaticClients: _list[str]

@typing.type_check_only
class Policy(typing_extensions.TypedDict, total=False):
    bindings: _list[Binding]
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
class ReauthSettings(typing_extensions.TypedDict, total=False):
    maxAge: str
    method: typing_extensions.Literal[
        "METHOD_UNSPECIFIED",
        "LOGIN",
        "PASSWORD",
        "SECURE_KEY",
        "ENROLLED_SECOND_FACTORS",
    ]
    policyType: typing_extensions.Literal[
        "POLICY_TYPE_UNSPECIFIED", "MINIMUM", "DEFAULT"
    ]

@typing.type_check_only
class ResetIdentityAwareProxyClientSecretRequest(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class Resource(typing_extensions.TypedDict, total=False):
    expectedNextState: dict[str, typing.Any]
    labels: dict[str, typing.Any]
    locations: _list[str]
    name: str
    nextStateOfTags: NextStateOfTags
    service: str
    type: str

@typing.type_check_only
class SetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    policy: Policy

@typing.type_check_only
class TagsFullState(typing_extensions.TypedDict, total=False):
    tags: dict[str, typing.Any]

@typing.type_check_only
class TagsFullStateForChildResource(typing_extensions.TypedDict, total=False):
    tags: dict[str, typing.Any]

@typing.type_check_only
class TagsPartialState(typing_extensions.TypedDict, total=False):
    tagKeysToRemove: _list[str]
    tagsToUpsert: dict[str, typing.Any]

@typing.type_check_only
class TestIamPermissionsRequest(typing_extensions.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class TestIamPermissionsResponse(typing_extensions.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class TunnelDestGroup(typing_extensions.TypedDict, total=False):
    cidrs: _list[str]
    fqdns: _list[str]
    name: str

@typing.type_check_only
class ValidateIapAttributeExpressionResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class WorkforceIdentitySettings(typing_extensions.TypedDict, total=False):
    oauth2: OAuth2
    workforcePools: _list[str]
