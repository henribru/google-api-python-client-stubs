import typing

import typing_extensions

_list = list

@typing.type_check_only
class AccessSummary(typing_extensions.TypedDict, total=False):
    authProvider: str
    authProviderType: typing_extensions.Literal[
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
class ApiKeyParams(typing_extensions.TypedDict, total=False):
    apiKey: str

@typing.type_check_only
class AuditConfig(typing_extensions.TypedDict, total=False):
    auditLogConfigs: _list[AuditLogConfig]
    service: str

@typing.type_check_only
class AuditLogConfig(typing_extensions.TypedDict, total=False):
    exemptedMembers: _list[str]
    logType: typing_extensions.Literal[
        "LOG_TYPE_UNSPECIFIED", "ADMIN_READ", "DATA_WRITE", "DATA_READ"
    ]

@typing.type_check_only
class AuthProvider(typing_extensions.TypedDict, total=False):
    allowedScopes: _list[str]
    authProviderTypeParams: AuthProviderTypeParams
    blockedScopes: _list[str]
    createTime: str
    deleted: bool
    description: str
    expireTime: str
    labels: dict[str, typing.Any]
    name: str
    state: typing_extensions.Literal["STATE_UNSPECIFIED", "ENABLED", "DISABLED"]
    updateTime: str
    workloadIds: _list[str]

@typing.type_check_only
class AuthProviderTypeParams(typing_extensions.TypedDict, total=False):
    apiKey: ApiKeyParams
    geAuthProvider: GeminiEnterpriseAuthProviderParams
    threeLeggedOauth: ThreeLeggedOAuth
    twoLeggedOauth: TwoLeggedOAuth

@typing.type_check_only
class Authorization(typing_extensions.TypedDict, total=False):
    clientUserId: str
    createTime: str
    name: str
    scopes: _list[str]
    state: typing_extensions.Literal["STATE_UNSPECIFIED", "ACTIVE", "SUSPENDED"]
    updateTime: str

@typing.type_check_only
class Binding(typing_extensions.TypedDict, total=False):
    condition: Expr
    members: _list[str]
    role: str

@typing.type_check_only
class DisableAuthProviderRequest(typing_extensions.TypedDict, total=False):
    requestId: str

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class EnableAuthProviderRequest(typing_extensions.TypedDict, total=False):
    requestId: str

@typing.type_check_only
class Expr(typing_extensions.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str

@typing.type_check_only
class GeminiEnterpriseAuthProviderParams(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class ListAccessSummariesResponse(typing_extensions.TypedDict, total=False):
    accessSummaries: _list[AccessSummary]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListAuthProvidersResponse(typing_extensions.TypedDict, total=False):
    authProviders: _list[AuthProvider]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListAuthorizationsResponse(typing_extensions.TypedDict, total=False):
    authorizations: _list[Authorization]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListLocationsResponse(typing_extensions.TypedDict, total=False):
    locations: _list[Location]
    nextPageToken: str

@typing.type_check_only
class Location(typing_extensions.TypedDict, total=False):
    displayName: str
    labels: dict[str, typing.Any]
    locationId: str
    metadata: dict[str, typing.Any]
    name: str

@typing.type_check_only
class Policy(typing_extensions.TypedDict, total=False):
    auditConfigs: _list[AuditConfig]
    bindings: _list[Binding]
    etag: str
    version: int

@typing.type_check_only
class QueryAuthProvidersResponse(typing_extensions.TypedDict, total=False):
    authProviderNames: _list[str]
    nextPageToken: str

@typing.type_check_only
class QueryWorkloadsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    workloadIds: _list[str]

@typing.type_check_only
class RevokeAuthorizationRequest(typing_extensions.TypedDict, total=False):
    userId: str

@typing.type_check_only
class RevokeAuthorizationResponse(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class SetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    policy: Policy
    updateMask: str

@typing.type_check_only
class TestIamPermissionsRequest(typing_extensions.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class TestIamPermissionsResponse(typing_extensions.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class ThreeLeggedOAuth(typing_extensions.TypedDict, total=False):
    authorizationUrl: str
    clientId: str
    clientSecret: str
    defaultContinueUri: str
    enablePkce: bool
    redirectUrl: str
    tokenUrl: str

@typing.type_check_only
class TwoLeggedOAuth(typing_extensions.TypedDict, total=False):
    clientId: str
    clientSecret: str
    tokenUrl: str

@typing.type_check_only
class UndeleteAuthProviderRequest(typing_extensions.TypedDict, total=False):
    requestId: str
