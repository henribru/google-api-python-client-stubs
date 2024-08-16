import typing

import typing_extensions

_list = list

@typing.type_check_only
class AccessRestrictions(typing_extensions.TypedDict, total=False):
    allowedServices: _list[ServiceConfig]
    disableProgrammaticSignin: bool

@typing.type_check_only
class AdminAuditData(typing_extensions.TypedDict, total=False):
    permissionDelta: PermissionDelta

@typing.type_check_only
class AuditConfig(typing_extensions.TypedDict, total=False):
    auditLogConfigs: _list[AuditLogConfig]
    service: str

@typing.type_check_only
class AuditData(typing_extensions.TypedDict, total=False):
    policyDelta: PolicyDelta

@typing.type_check_only
class AuditLogConfig(typing_extensions.TypedDict, total=False):
    exemptedMembers: _list[str]
    logType: typing_extensions.Literal[
        "LOG_TYPE_UNSPECIFIED", "ADMIN_READ", "DATA_WRITE", "DATA_READ"
    ]

@typing.type_check_only
class AuditableService(typing_extensions.TypedDict, total=False):
    name: str

@typing.type_check_only
class Aws(typing_extensions.TypedDict, total=False):
    accountId: str

@typing.type_check_only
class Binding(typing_extensions.TypedDict, total=False):
    condition: Expr
    members: _list[str]
    role: str

@typing.type_check_only
class BindingDelta(typing_extensions.TypedDict, total=False):
    action: typing_extensions.Literal["ACTION_UNSPECIFIED", "ADD", "REMOVE"]
    condition: Expr
    member: str
    role: str

@typing.type_check_only
class CreateRoleRequest(typing_extensions.TypedDict, total=False):
    role: Role
    roleId: str

@typing.type_check_only
class CreateServiceAccountKeyRequest(typing_extensions.TypedDict, total=False):
    keyAlgorithm: typing_extensions.Literal[
        "KEY_ALG_UNSPECIFIED", "KEY_ALG_RSA_1024", "KEY_ALG_RSA_2048"
    ]
    privateKeyType: typing_extensions.Literal[
        "TYPE_UNSPECIFIED", "TYPE_PKCS12_FILE", "TYPE_GOOGLE_CREDENTIALS_FILE"
    ]

@typing.type_check_only
class CreateServiceAccountRequest(typing_extensions.TypedDict, total=False):
    accountId: str
    serviceAccount: ServiceAccount

@typing.type_check_only
class DisableServiceAccountKeyRequest(typing_extensions.TypedDict, total=False):
    extendedStatusMessage: str
    serviceAccountKeyDisableReason: typing_extensions.Literal[
        "SERVICE_ACCOUNT_KEY_DISABLE_REASON_UNSPECIFIED",
        "SERVICE_ACCOUNT_KEY_DISABLE_REASON_USER_INITIATED",
        "SERVICE_ACCOUNT_KEY_DISABLE_REASON_EXPOSED",
        "SERVICE_ACCOUNT_KEY_DISABLE_REASON_COMPROMISE_DETECTED",
    ]

@typing.type_check_only
class DisableServiceAccountRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class EnableServiceAccountKeyRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class EnableServiceAccountRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Expr(typing_extensions.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str

@typing.type_check_only
class ExtendedStatus(typing_extensions.TypedDict, total=False):
    key: typing_extensions.Literal[
        "SERVICE_ACCOUNT_KEY_EXTENDED_STATUS_KEY_UNSPECIFIED",
        "SERVICE_ACCOUNT_KEY_EXTENDED_STATUS_KEY_EXPOSED",
        "SERVICE_ACCOUNT_KEY_EXTENDED_STATUS_KEY_COMPROMISE_DETECTED",
    ]
    value: str

@typing.type_check_only
class GetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    options: GetPolicyOptions

@typing.type_check_only
class GetPolicyOptions(typing_extensions.TypedDict, total=False):
    requestedPolicyVersion: int

@typing.type_check_only
class GoogleIamAdminV1WorkforcePoolProviderExtraAttributesOAuth2Client(
    typing_extensions.TypedDict, total=False
):
    attributesType: typing_extensions.Literal[
        "ATTRIBUTES_TYPE_UNSPECIFIED", "AZURE_AD_GROUPS_MAIL"
    ]
    clientId: str
    clientSecret: GoogleIamAdminV1WorkforcePoolProviderOidcClientSecret
    issuerUri: str
    queryParameters: (
        GoogleIamAdminV1WorkforcePoolProviderExtraAttributesOAuth2ClientQueryParameters
    )

@typing.type_check_only
class GoogleIamAdminV1WorkforcePoolProviderExtraAttributesOAuth2ClientQueryParameters(
    typing_extensions.TypedDict, total=False
):
    filter: str

@typing.type_check_only
class GoogleIamAdminV1WorkforcePoolProviderOidc(
    typing_extensions.TypedDict, total=False
):
    clientId: str
    clientSecret: GoogleIamAdminV1WorkforcePoolProviderOidcClientSecret
    issuerUri: str
    jwksJson: str
    webSsoConfig: GoogleIamAdminV1WorkforcePoolProviderOidcWebSsoConfig

@typing.type_check_only
class GoogleIamAdminV1WorkforcePoolProviderOidcClientSecret(
    typing_extensions.TypedDict, total=False
):
    value: GoogleIamAdminV1WorkforcePoolProviderOidcClientSecretValue

@typing.type_check_only
class GoogleIamAdminV1WorkforcePoolProviderOidcClientSecretValue(
    typing_extensions.TypedDict, total=False
):
    plainText: str
    thumbprint: str

@typing.type_check_only
class GoogleIamAdminV1WorkforcePoolProviderOidcWebSsoConfig(
    typing_extensions.TypedDict, total=False
):
    additionalScopes: _list[str]
    assertionClaimsBehavior: typing_extensions.Literal[
        "ASSERTION_CLAIMS_BEHAVIOR_UNSPECIFIED",
        "MERGE_USER_INFO_OVER_ID_TOKEN_CLAIMS",
        "ONLY_ID_TOKEN_CLAIMS",
    ]
    responseType: typing_extensions.Literal[
        "RESPONSE_TYPE_UNSPECIFIED", "CODE", "ID_TOKEN"
    ]

@typing.type_check_only
class GoogleIamAdminV1WorkforcePoolProviderSaml(
    typing_extensions.TypedDict, total=False
):
    idpMetadataXml: str

@typing.type_check_only
class KeyData(typing_extensions.TypedDict, total=False):
    format: typing_extensions.Literal["KEY_FORMAT_UNSPECIFIED", "RSA_X509_PEM"]
    key: str
    keySpec: typing_extensions.Literal[
        "KEY_SPEC_UNSPECIFIED", "RSA_2048", "RSA_3072", "RSA_4096"
    ]
    notAfterTime: str
    notBeforeTime: str

@typing.type_check_only
class LintPolicyRequest(typing_extensions.TypedDict, total=False):
    condition: Expr
    fullResourceName: str

@typing.type_check_only
class LintPolicyResponse(typing_extensions.TypedDict, total=False):
    lintResults: _list[LintResult]

@typing.type_check_only
class LintResult(typing_extensions.TypedDict, total=False):
    debugMessage: str
    fieldName: str
    level: typing_extensions.Literal["LEVEL_UNSPECIFIED", "CONDITION"]
    locationOffset: int
    severity: typing_extensions.Literal[
        "SEVERITY_UNSPECIFIED", "ERROR", "WARNING", "NOTICE", "INFO", "DEPRECATED"
    ]
    validationUnitName: str

@typing.type_check_only
class ListOauthClientCredentialsResponse(typing_extensions.TypedDict, total=False):
    oauthClientCredentials: _list[OauthClientCredential]

@typing.type_check_only
class ListOauthClientsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    oauthClients: _list[OauthClient]

@typing.type_check_only
class ListRolesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    roles: _list[Role]

@typing.type_check_only
class ListServiceAccountKeysResponse(typing_extensions.TypedDict, total=False):
    keys: _list[ServiceAccountKey]

@typing.type_check_only
class ListServiceAccountsResponse(typing_extensions.TypedDict, total=False):
    accounts: _list[ServiceAccount]
    nextPageToken: str

@typing.type_check_only
class ListWorkforcePoolProviderKeysResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    workforcePoolProviderKeys: _list[WorkforcePoolProviderKey]

@typing.type_check_only
class ListWorkforcePoolProvidersResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    workforcePoolProviders: _list[WorkforcePoolProvider]

@typing.type_check_only
class ListWorkforcePoolsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    workforcePools: _list[WorkforcePool]

@typing.type_check_only
class ListWorkloadIdentityPoolProviderKeysResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    workloadIdentityPoolProviderKeys: _list[WorkloadIdentityPoolProviderKey]

@typing.type_check_only
class ListWorkloadIdentityPoolProvidersResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    workloadIdentityPoolProviders: _list[WorkloadIdentityPoolProvider]

@typing.type_check_only
class ListWorkloadIdentityPoolsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    workloadIdentityPools: _list[WorkloadIdentityPool]

@typing.type_check_only
class OauthClient(typing_extensions.TypedDict, total=False):
    allowedGrantTypes: _list[
        typing_extensions.Literal[
            "GRANT_TYPE_UNSPECIFIED", "AUTHORIZATION_CODE_GRANT", "REFRESH_TOKEN_GRANT"
        ]
    ]
    allowedRedirectUris: _list[str]
    allowedScopes: _list[str]
    clientId: str
    clientType: typing_extensions.Literal[
        "CLIENT_TYPE_UNSPECIFIED", "PUBLIC_CLIENT", "CONFIDENTIAL_CLIENT"
    ]
    description: str
    disabled: bool
    displayName: str
    expireTime: str
    name: str
    state: typing_extensions.Literal["STATE_UNSPECIFIED", "ACTIVE", "DELETED"]

@typing.type_check_only
class OauthClientCredential(typing_extensions.TypedDict, total=False):
    clientSecret: str
    disabled: bool
    displayName: str
    name: str

@typing.type_check_only
class Oidc(typing_extensions.TypedDict, total=False):
    allowedAudiences: _list[str]
    issuerUri: str
    jwksJson: str

@typing.type_check_only
class Operation(typing_extensions.TypedDict, total=False):
    done: bool
    error: Status
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class OperationMetadata(typing_extensions.TypedDict, total=False):
    apiVersion: str
    cancelRequested: bool
    createTime: str
    endTime: str
    statusDetail: str
    target: str
    verb: str

@typing.type_check_only
class PatchServiceAccountRequest(typing_extensions.TypedDict, total=False):
    serviceAccount: ServiceAccount
    updateMask: str

@typing.type_check_only
class Permission(typing_extensions.TypedDict, total=False):
    apiDisabled: bool
    customRolesSupportLevel: typing_extensions.Literal[
        "SUPPORTED", "TESTING", "NOT_SUPPORTED"
    ]
    description: str
    name: str
    onlyInPredefinedRoles: bool
    primaryPermission: str
    stage: typing_extensions.Literal["ALPHA", "BETA", "GA", "DEPRECATED"]
    title: str

@typing.type_check_only
class PermissionDelta(typing_extensions.TypedDict, total=False):
    addedPermissions: _list[str]
    removedPermissions: _list[str]

@typing.type_check_only
class Policy(typing_extensions.TypedDict, total=False):
    auditConfigs: _list[AuditConfig]
    bindings: _list[Binding]
    etag: str
    version: int

@typing.type_check_only
class PolicyDelta(typing_extensions.TypedDict, total=False):
    bindingDeltas: _list[BindingDelta]

@typing.type_check_only
class QueryAuditableServicesRequest(typing_extensions.TypedDict, total=False):
    fullResourceName: str

@typing.type_check_only
class QueryAuditableServicesResponse(typing_extensions.TypedDict, total=False):
    services: _list[AuditableService]

@typing.type_check_only
class QueryGrantableRolesRequest(typing_extensions.TypedDict, total=False):
    fullResourceName: str
    pageSize: int
    pageToken: str
    view: typing_extensions.Literal["BASIC", "FULL"]

@typing.type_check_only
class QueryGrantableRolesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    roles: _list[Role]

@typing.type_check_only
class QueryTestablePermissionsRequest(typing_extensions.TypedDict, total=False):
    fullResourceName: str
    pageSize: int
    pageToken: str

@typing.type_check_only
class QueryTestablePermissionsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    permissions: _list[Permission]

@typing.type_check_only
class ReconciliationOperationMetadata(typing_extensions.TypedDict, total=False):
    deleteResource: bool
    exclusiveAction: typing_extensions.Literal[
        "UNKNOWN_REPAIR_ACTION", "DELETE", "RETRY"
    ]

@typing.type_check_only
class Role(typing_extensions.TypedDict, total=False):
    deleted: bool
    description: str
    etag: str
    includedPermissions: _list[str]
    name: str
    stage: typing_extensions.Literal[
        "ALPHA", "BETA", "GA", "DEPRECATED", "DISABLED", "EAP"
    ]
    title: str

@typing.type_check_only
class Saml(typing_extensions.TypedDict, total=False):
    idpMetadataXml: str

@typing.type_check_only
class ServiceAccount(typing_extensions.TypedDict, total=False):
    description: str
    disabled: bool
    displayName: str
    email: str
    etag: str
    name: str
    oauth2ClientId: str
    projectId: str
    uniqueId: str

@typing.type_check_only
class ServiceAccountKey(typing_extensions.TypedDict, total=False):
    disableReason: typing_extensions.Literal[
        "SERVICE_ACCOUNT_KEY_DISABLE_REASON_UNSPECIFIED",
        "SERVICE_ACCOUNT_KEY_DISABLE_REASON_USER_INITIATED",
        "SERVICE_ACCOUNT_KEY_DISABLE_REASON_EXPOSED",
        "SERVICE_ACCOUNT_KEY_DISABLE_REASON_COMPROMISE_DETECTED",
    ]
    disabled: bool
    extendedStatus: _list[ExtendedStatus]
    keyAlgorithm: typing_extensions.Literal[
        "KEY_ALG_UNSPECIFIED", "KEY_ALG_RSA_1024", "KEY_ALG_RSA_2048"
    ]
    keyOrigin: typing_extensions.Literal[
        "ORIGIN_UNSPECIFIED", "USER_PROVIDED", "GOOGLE_PROVIDED"
    ]
    keyType: typing_extensions.Literal[
        "KEY_TYPE_UNSPECIFIED", "USER_MANAGED", "SYSTEM_MANAGED"
    ]
    name: str
    privateKeyData: str
    privateKeyType: typing_extensions.Literal[
        "TYPE_UNSPECIFIED", "TYPE_PKCS12_FILE", "TYPE_GOOGLE_CREDENTIALS_FILE"
    ]
    publicKeyData: str
    validAfterTime: str
    validBeforeTime: str

@typing.type_check_only
class ServiceConfig(typing_extensions.TypedDict, total=False):
    domain: str

@typing.type_check_only
class SetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    policy: Policy
    updateMask: str

@typing.type_check_only
class SignBlobRequest(typing_extensions.TypedDict, total=False):
    bytesToSign: str

@typing.type_check_only
class SignBlobResponse(typing_extensions.TypedDict, total=False):
    keyId: str
    signature: str

@typing.type_check_only
class SignJwtRequest(typing_extensions.TypedDict, total=False):
    payload: str

@typing.type_check_only
class SignJwtResponse(typing_extensions.TypedDict, total=False):
    keyId: str
    signedJwt: str

@typing.type_check_only
class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class TestIamPermissionsRequest(typing_extensions.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class TestIamPermissionsResponse(typing_extensions.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class UndeleteOauthClientRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class UndeleteRoleRequest(typing_extensions.TypedDict, total=False):
    etag: str

@typing.type_check_only
class UndeleteServiceAccountRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class UndeleteServiceAccountResponse(typing_extensions.TypedDict, total=False):
    restoredAccount: ServiceAccount

@typing.type_check_only
class UndeleteWorkforcePoolProviderKeyRequest(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class UndeleteWorkforcePoolProviderRequest(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class UndeleteWorkforcePoolRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class UndeleteWorkforcePoolSubjectRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class UndeleteWorkloadIdentityPoolProviderKeyRequest(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class UndeleteWorkloadIdentityPoolProviderRequest(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class UndeleteWorkloadIdentityPoolRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class UploadServiceAccountKeyRequest(typing_extensions.TypedDict, total=False):
    publicKeyData: str

@typing.type_check_only
class WorkforcePool(typing_extensions.TypedDict, total=False):
    accessRestrictions: AccessRestrictions
    description: str
    disabled: bool
    displayName: str
    expireTime: str
    name: str
    parent: str
    sessionDuration: str
    state: typing_extensions.Literal["STATE_UNSPECIFIED", "ACTIVE", "DELETED"]

@typing.type_check_only
class WorkforcePoolProvider(typing_extensions.TypedDict, total=False):
    attributeCondition: str
    attributeMapping: dict[str, typing.Any]
    description: str
    disabled: bool
    displayName: str
    expireTime: str
    extraAttributesOauth2Client: (
        GoogleIamAdminV1WorkforcePoolProviderExtraAttributesOAuth2Client
    )
    name: str
    oidc: GoogleIamAdminV1WorkforcePoolProviderOidc
    saml: GoogleIamAdminV1WorkforcePoolProviderSaml
    state: typing_extensions.Literal["STATE_UNSPECIFIED", "ACTIVE", "DELETED"]

@typing.type_check_only
class WorkforcePoolProviderKey(typing_extensions.TypedDict, total=False):
    expireTime: str
    keyData: KeyData
    name: str
    state: typing_extensions.Literal["STATE_UNSPECIFIED", "ACTIVE", "DELETED"]
    use: typing_extensions.Literal["KEY_USE_UNSPECIFIED", "ENCRYPTION"]

@typing.type_check_only
class WorkloadIdentityPool(typing_extensions.TypedDict, total=False):
    description: str
    disabled: bool
    displayName: str
    expireTime: str
    name: str
    state: typing_extensions.Literal["STATE_UNSPECIFIED", "ACTIVE", "DELETED"]

@typing.type_check_only
class WorkloadIdentityPoolOperationMetadata(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class WorkloadIdentityPoolProvider(typing_extensions.TypedDict, total=False):
    attributeCondition: str
    attributeMapping: dict[str, typing.Any]
    aws: Aws
    description: str
    disabled: bool
    displayName: str
    expireTime: str
    name: str
    oidc: Oidc
    saml: Saml
    state: typing_extensions.Literal["STATE_UNSPECIFIED", "ACTIVE", "DELETED"]

@typing.type_check_only
class WorkloadIdentityPoolProviderKey(typing_extensions.TypedDict, total=False):
    expireTime: str
    keyData: KeyData
    name: str
    state: typing_extensions.Literal["STATE_UNSPECIFIED", "ACTIVE", "DELETED"]
    use: typing_extensions.Literal["KEY_USE_UNSPECIFIED", "ENCRYPTION"]
