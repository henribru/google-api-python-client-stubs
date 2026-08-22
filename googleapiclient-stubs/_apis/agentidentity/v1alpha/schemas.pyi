import typing

_list = list

@typing.type_check_only
class AccessSummary(typing.TypedDict, total=False):
    authProvider: str
    authProviderType: typing.Literal[
        "AUTH_PROVIDER_TYPE_UNSPECIFIED",
        "AUTH_PROVIDER_TYPE_THREE_LEGGED_OAUTH",
        "AUTH_PROVIDER_TYPE_TWO_LEGGED_OAUTH",
        "AUTH_PROVIDER_TYPE_API_KEY",
        "AUTH_PROVIDER_TYPE_GEMINI_ENTERPRISE",
    ]
    firstAccessTime: str
    labels: dict[str, typing.Any]
    lastAccessTime: str
    name: str
    purgeTime: str
    scopes: _list[str]
    tokenUrl: str
    userId: str
    workloadId: str

@typing.type_check_only
class ApiKeyParams(typing.TypedDict, total=False):
    apiKey: str

@typing.type_check_only
class AuditConfig(typing.TypedDict, total=False):
    auditLogConfigs: _list[AuditLogConfig]
    service: str

@typing.type_check_only
class AuditLogConfig(typing.TypedDict, total=False):
    exemptedMembers: _list[str]
    logType: typing.Literal[
        "LOG_TYPE_UNSPECIFIED", "ADMIN_READ", "DATA_WRITE", "DATA_READ"
    ]

@typing.type_check_only
class AuthProvider(typing.TypedDict, total=False):
    allowedScopes: _list[str]
    authProviderTypeParams: AuthProviderTypeParams
    blockedScopes: _list[str]
    createTime: str
    deleted: bool
    description: str
    expireTime: str
    labels: dict[str, typing.Any]
    name: str
    state: typing.Literal["STATE_UNSPECIFIED", "ENABLED", "DISABLED"]
    updateTime: str
    workloadIds: _list[str]

@typing.type_check_only
class AuthProviderTypeParams(typing.TypedDict, total=False):
    apiKey: ApiKeyParams
    geAuthProvider: GeminiEnterpriseAuthProviderParams
    threeLeggedOauth: ThreeLeggedOAuth
    twoLeggedOauth: TwoLeggedOAuth

@typing.type_check_only
class Authorization(typing.TypedDict, total=False):
    clientUserId: str
    createTime: str
    name: str
    scopes: _list[str]
    state: typing.Literal["STATE_UNSPECIFIED", "ACTIVE", "SUSPENDED"]
    updateTime: str

@typing.type_check_only
class Binding(typing.TypedDict, total=False):
    condition: Expr
    members: _list[str]
    role: str

@typing.type_check_only
class DisableAuthProviderRequest(typing.TypedDict, total=False):
    requestId: str

@typing.type_check_only
class Empty(typing.TypedDict, total=False): ...

@typing.type_check_only
class EnableAuthProviderRequest(typing.TypedDict, total=False):
    requestId: str

@typing.type_check_only
class Expr(typing.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str

@typing.type_check_only
class GeminiEnterpriseAuthProviderParams(typing.TypedDict, total=False): ...

@typing.type_check_only
class ListAccessSummariesResponse(typing.TypedDict, total=False):
    accessSummaries: _list[AccessSummary]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListAuthProvidersResponse(typing.TypedDict, total=False):
    authProviders: _list[AuthProvider]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListAuthorizationsResponse(typing.TypedDict, total=False):
    authorizations: _list[Authorization]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListLocationsResponse(typing.TypedDict, total=False):
    locations: _list[Location]
    nextPageToken: str

@typing.type_check_only
class Location(typing.TypedDict, total=False):
    displayName: str
    labels: dict[str, typing.Any]
    locationId: str
    metadata: dict[str, typing.Any]
    name: str

@typing.type_check_only
class Policy(typing.TypedDict, total=False):
    auditConfigs: _list[AuditConfig]
    bindings: _list[Binding]
    etag: str
    version: int

@typing.type_check_only
class QueryAuthProvidersResponse(typing.TypedDict, total=False):
    authProviderNames: _list[str]
    nextPageToken: str

@typing.type_check_only
class QueryWorkloadsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    workloadIds: _list[str]

@typing.type_check_only
class RevokeAuthorizationRequest(typing.TypedDict, total=False):
    userId: str

@typing.type_check_only
class RevokeAuthorizationResponse(typing.TypedDict, total=False): ...

@typing.type_check_only
class SetIamPolicyRequest(typing.TypedDict, total=False):
    policy: Policy
    updateMask: str

@typing.type_check_only
class TestIamPermissionsRequest(typing.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class TestIamPermissionsResponse(typing.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class ThreeLeggedOAuth(typing.TypedDict, total=False):
    authorizationUrl: str
    clientId: str
    clientSecret: str
    defaultContinueUri: str
    enablePkce: bool
    redirectUrl: str
    tokenUrl: str

@typing.type_check_only
class TwoLeggedOAuth(typing.TypedDict, total=False):
    clientId: str
    clientSecret: str
    tokenUrl: str

@typing.type_check_only
class UndeleteAuthProviderRequest(typing.TypedDict, total=False):
    requestId: str
