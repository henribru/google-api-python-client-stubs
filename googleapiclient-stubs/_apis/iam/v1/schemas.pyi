import typing

import typing_extensions

class UploadServiceAccountKeyRequest(typing_extensions.TypedDict, total=False):
    publicKeyData: str

class PolicyDelta(typing_extensions.TypedDict, total=False):
    bindingDeltas: typing.List[BindingDelta]

class CreateRoleRequest(typing_extensions.TypedDict, total=False):
    roleId: str
    role: Role

class ServiceAccountKey(typing_extensions.TypedDict, total=False):
    name: str
    privateKeyType: typing_extensions.Literal[
        "TYPE_UNSPECIFIED", "TYPE_PKCS12_FILE", "TYPE_GOOGLE_CREDENTIALS_FILE"
    ]
    keyAlgorithm: typing_extensions.Literal[
        "KEY_ALG_UNSPECIFIED", "KEY_ALG_RSA_1024", "KEY_ALG_RSA_2048"
    ]
    privateKeyData: str
    validBeforeTime: str
    keyOrigin: typing_extensions.Literal[
        "ORIGIN_UNSPECIFIED", "USER_PROVIDED", "GOOGLE_PROVIDED"
    ]
    publicKeyData: str
    validAfterTime: str
    keyType: typing_extensions.Literal[
        "KEY_TYPE_UNSPECIFIED", "USER_MANAGED", "SYSTEM_MANAGED"
    ]

class SignJwtResponse(typing_extensions.TypedDict, total=False):
    signedJwt: str
    keyId: str

class LintPolicyResponse(typing_extensions.TypedDict, total=False):
    lintResults: typing.List[LintResult]

class QueryGrantableRolesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    roles: typing.List[Role]

class CreateServiceAccountRequest(typing_extensions.TypedDict, total=False):
    serviceAccount: ServiceAccount
    accountId: str

class BindingDelta(typing_extensions.TypedDict, total=False):
    member: str
    condition: Expr
    action: typing_extensions.Literal["ACTION_UNSPECIFIED", "ADD", "REMOVE"]
    role: str

class QueryGrantableRolesRequest(typing_extensions.TypedDict, total=False):
    pageToken: str
    view: typing_extensions.Literal["BASIC", "FULL"]
    fullResourceName: str
    pageSize: int

class QueryTestablePermissionsRequest(typing_extensions.TypedDict, total=False):
    pageSize: int
    pageToken: str
    fullResourceName: str

class AdminAuditData(typing_extensions.TypedDict, total=False):
    permissionDelta: PermissionDelta

class LintPolicyRequest(typing_extensions.TypedDict, total=False):
    condition: Expr
    fullResourceName: str

class SignJwtRequest(typing_extensions.TypedDict, total=False):
    payload: str

class DisableServiceAccountRequest(typing_extensions.TypedDict, total=False): ...

class LintResult(typing_extensions.TypedDict, total=False):
    level: typing_extensions.Literal["LEVEL_UNSPECIFIED", "CONDITION"]
    validationUnitName: str
    debugMessage: str
    locationOffset: int
    severity: typing_extensions.Literal[
        "SEVERITY_UNSPECIFIED", "ERROR", "WARNING", "NOTICE", "INFO", "DEPRECATED"
    ]
    fieldName: str

class AuditData(typing_extensions.TypedDict, total=False):
    policyDelta: PolicyDelta

class ListRolesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    roles: typing.List[Role]

class UndeleteRoleRequest(typing_extensions.TypedDict, total=False):
    etag: str

class QueryAuditableServicesResponse(typing_extensions.TypedDict, total=False):
    services: typing.List[AuditableService]

class AuditLogConfig(typing_extensions.TypedDict, total=False):
    logType: typing_extensions.Literal[
        "LOG_TYPE_UNSPECIFIED", "ADMIN_READ", "DATA_WRITE", "DATA_READ"
    ]
    exemptedMembers: typing.List[str]

class EnableServiceAccountRequest(typing_extensions.TypedDict, total=False): ...

class SignBlobResponse(typing_extensions.TypedDict, total=False):
    keyId: str
    signature: str

class AuditConfig(typing_extensions.TypedDict, total=False):
    auditLogConfigs: typing.List[AuditLogConfig]
    service: str

class Expr(typing_extensions.TypedDict, total=False):
    description: str
    title: str
    expression: str
    location: str

class SetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    policy: Policy
    updateMask: str

class QueryAuditableServicesRequest(typing_extensions.TypedDict, total=False):
    fullResourceName: str

class Empty(typing_extensions.TypedDict, total=False): ...

class ListServiceAccountKeysResponse(typing_extensions.TypedDict, total=False):
    keys: typing.List[ServiceAccountKey]

class SignBlobRequest(typing_extensions.TypedDict, total=False):
    bytesToSign: str

class QueryTestablePermissionsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    permissions: typing.List[Permission]

class Role(typing_extensions.TypedDict, total=False):
    deleted: bool
    stage: typing_extensions.Literal[
        "ALPHA", "BETA", "GA", "DEPRECATED", "DISABLED", "EAP"
    ]
    name: str
    etag: str
    includedPermissions: typing.List[str]
    description: str
    title: str

class TestIamPermissionsRequest(typing_extensions.TypedDict, total=False):
    permissions: typing.List[str]

class Binding(typing_extensions.TypedDict, total=False):
    condition: Expr
    role: str
    members: typing.List[str]
    bindingId: str

class PermissionDelta(typing_extensions.TypedDict, total=False):
    removedPermissions: typing.List[str]
    addedPermissions: typing.List[str]

class UndeleteServiceAccountRequest(typing_extensions.TypedDict, total=False): ...

class AuditableService(typing_extensions.TypedDict, total=False):
    name: str

class PatchServiceAccountRequest(typing_extensions.TypedDict, total=False):
    updateMask: str
    serviceAccount: ServiceAccount

class ListServiceAccountsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    accounts: typing.List[ServiceAccount]

class UndeleteServiceAccountResponse(typing_extensions.TypedDict, total=False):
    restoredAccount: ServiceAccount

class Policy(typing_extensions.TypedDict, total=False):
    etag: str
    bindings: typing.List[Binding]
    version: int
    auditConfigs: typing.List[AuditConfig]

class Permission(typing_extensions.TypedDict, total=False):
    onlyInPredefinedRoles: bool
    title: str
    primaryPermission: str
    description: str
    name: str
    customRolesSupportLevel: typing_extensions.Literal[
        "SUPPORTED", "TESTING", "NOT_SUPPORTED"
    ]
    stage: typing_extensions.Literal["ALPHA", "BETA", "GA", "DEPRECATED"]
    apiDisabled: bool

class CreateServiceAccountKeyRequest(typing_extensions.TypedDict, total=False):
    keyAlgorithm: typing_extensions.Literal[
        "KEY_ALG_UNSPECIFIED", "KEY_ALG_RSA_1024", "KEY_ALG_RSA_2048"
    ]
    privateKeyType: typing_extensions.Literal[
        "TYPE_UNSPECIFIED", "TYPE_PKCS12_FILE", "TYPE_GOOGLE_CREDENTIALS_FILE"
    ]

class TestIamPermissionsResponse(typing_extensions.TypedDict, total=False):
    permissions: typing.List[str]

class ServiceAccount(typing_extensions.TypedDict, total=False):
    displayName: str
    oauth2ClientId: str
    description: str
    disabled: bool
    uniqueId: str
    projectId: str
    etag: str
    email: str
    name: str
