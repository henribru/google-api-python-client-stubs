import typing

_list = list

@typing.type_check_only
class AccessRestrictions(typing.TypedDict, total=False):
    allowedServices: _list[ServiceConfig]
    disableProgrammaticSignin: bool

@typing.type_check_only
class AddAttestationRuleRequest(typing.TypedDict, total=False):
    attestationRule: AttestationRule

@typing.type_check_only
class AdminAuditData(typing.TypedDict, total=False):
    permissionDelta: PermissionDelta

@typing.type_check_only
class AttestationRule(typing.TypedDict, total=False):
    googleCloudResource: str

@typing.type_check_only
class AuditConfig(typing.TypedDict, total=False):
    auditLogConfigs: _list[AuditLogConfig]
    service: str

@typing.type_check_only
class AuditData(typing.TypedDict, total=False):
    policyDelta: PolicyDelta

@typing.type_check_only
class AuditLogConfig(typing.TypedDict, total=False):
    exemptedMembers: _list[str]
    logType: typing.Literal[
        "LOG_TYPE_UNSPECIFIED", "ADMIN_READ", "DATA_WRITE", "DATA_READ"
    ]

@typing.type_check_only
class AuditableService(typing.TypedDict, total=False):
    name: str

@typing.type_check_only
class Aws(typing.TypedDict, total=False):
    accountId: str

@typing.type_check_only
class Binding(typing.TypedDict, total=False):
    condition: Expr
    members: _list[str]
    role: str

@typing.type_check_only
class BindingDelta(typing.TypedDict, total=False):
    action: typing.Literal["ACTION_UNSPECIFIED", "ADD", "REMOVE"]
    condition: Expr
    member: str
    role: str

@typing.type_check_only
class CreateRoleRequest(typing.TypedDict, total=False):
    role: Role
    roleId: str

@typing.type_check_only
class CreateServiceAccountKeyRequest(typing.TypedDict, total=False):
    keyAlgorithm: typing.Literal[
        "KEY_ALG_UNSPECIFIED", "KEY_ALG_RSA_1024", "KEY_ALG_RSA_2048"
    ]
    privateKeyType: typing.Literal[
        "TYPE_UNSPECIFIED", "TYPE_PKCS12_FILE", "TYPE_GOOGLE_CREDENTIALS_FILE"
    ]

@typing.type_check_only
class CreateServiceAccountRequest(typing.TypedDict, total=False):
    accountId: str
    serviceAccount: ServiceAccount

@typing.type_check_only
class DisableServiceAccountKeyRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class DisableServiceAccountRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class Empty(typing.TypedDict, total=False): ...

@typing.type_check_only
class EnableServiceAccountKeyRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class EnableServiceAccountRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class Expr(typing.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str

@typing.type_check_only
class ExtendedStatus(typing.TypedDict, total=False):
    key: typing.Literal[
        "SERVICE_ACCOUNT_KEY_EXTENDED_STATUS_KEY_UNSPECIFIED",
        "SERVICE_ACCOUNT_KEY_EXTENDED_STATUS_KEY_EXPOSED",
        "SERVICE_ACCOUNT_KEY_EXTENDED_STATUS_KEY_COMPROMISE_DETECTED",
    ]
    value: str

@typing.type_check_only
class GetIamPolicyRequest(typing.TypedDict, total=False):
    options: GetPolicyOptions

@typing.type_check_only
class GetPolicyOptions(typing.TypedDict, total=False):
    requestedPolicyVersion: int

@typing.type_check_only
class GoogleIamAdminV1WorkforcePoolProviderExtraAttributesOAuth2Client(
    typing.TypedDict, total=False
):
    attributesType: typing.Literal[
        "ATTRIBUTES_TYPE_UNSPECIFIED",
        "AZURE_AD_GROUPS_MAIL",
        "AZURE_AD_GROUPS_ID",
        "AZURE_AD_GROUPS_DISPLAY_NAME",
    ]
    clientId: str
    clientSecret: GoogleIamAdminV1WorkforcePoolProviderOidcClientSecret
    issuerUri: str
    queryParameters: (
        GoogleIamAdminV1WorkforcePoolProviderExtraAttributesOAuth2ClientQueryParameters
    )

@typing.type_check_only
class GoogleIamAdminV1WorkforcePoolProviderExtraAttributesOAuth2ClientQueryParameters(
    typing.TypedDict, total=False
):
    filter: str

@typing.type_check_only
class GoogleIamAdminV1WorkforcePoolProviderOidc(typing.TypedDict, total=False):
    clientId: str
    clientSecret: GoogleIamAdminV1WorkforcePoolProviderOidcClientSecret
    issuerUri: str
    jwksJson: str
    webSsoConfig: GoogleIamAdminV1WorkforcePoolProviderOidcWebSsoConfig

@typing.type_check_only
class GoogleIamAdminV1WorkforcePoolProviderOidcClientSecret(
    typing.TypedDict, total=False
):
    value: GoogleIamAdminV1WorkforcePoolProviderOidcClientSecretValue

@typing.type_check_only
class GoogleIamAdminV1WorkforcePoolProviderOidcClientSecretValue(
    typing.TypedDict, total=False
):
    plainText: str
    thumbprint: str

@typing.type_check_only
class GoogleIamAdminV1WorkforcePoolProviderOidcWebSsoConfig(
    typing.TypedDict, total=False
):
    additionalScopes: _list[str]
    assertionClaimsBehavior: typing.Literal[
        "ASSERTION_CLAIMS_BEHAVIOR_UNSPECIFIED",
        "MERGE_USER_INFO_OVER_ID_TOKEN_CLAIMS",
        "ONLY_ID_TOKEN_CLAIMS",
    ]
    responseType: typing.Literal["RESPONSE_TYPE_UNSPECIFIED", "CODE", "ID_TOKEN"]

@typing.type_check_only
class GoogleIamAdminV1WorkforcePoolProviderSaml(typing.TypedDict, total=False):
    idpMetadataXml: str

@typing.type_check_only
class InlineCertificateIssuanceConfig(typing.TypedDict, total=False):
    caPools: dict[str, typing.Any]
    keyAlgorithm: typing.Literal[
        "KEY_ALGORITHM_UNSPECIFIED",
        "RSA_2048",
        "RSA_3072",
        "RSA_4096",
        "ECDSA_P256",
        "ECDSA_P384",
    ]
    lifetime: str
    rotationWindowPercentage: int
    useDefaultSharedCa: bool

@typing.type_check_only
class InlineTrustConfig(typing.TypedDict, total=False):
    additionalTrustBundles: dict[str, typing.Any]

@typing.type_check_only
class IntermediateCA(typing.TypedDict, total=False):
    pemCertificate: str

@typing.type_check_only
class KeyData(typing.TypedDict, total=False):
    format: typing.Literal["KEY_FORMAT_UNSPECIFIED", "RSA_X509_PEM"]
    key: str
    keySpec: typing.Literal["KEY_SPEC_UNSPECIFIED", "RSA_2048", "RSA_3072", "RSA_4096"]
    notAfterTime: str
    notBeforeTime: str

@typing.type_check_only
class LintPolicyRequest(typing.TypedDict, total=False):
    condition: Expr
    fullResourceName: str

@typing.type_check_only
class LintPolicyResponse(typing.TypedDict, total=False):
    lintResults: _list[LintResult]

@typing.type_check_only
class LintResult(typing.TypedDict, total=False):
    debugMessage: str
    fieldName: str
    level: typing.Literal["LEVEL_UNSPECIFIED", "CONDITION"]
    locationOffset: int
    severity: typing.Literal[
        "SEVERITY_UNSPECIFIED", "ERROR", "WARNING", "NOTICE", "INFO", "DEPRECATED"
    ]
    validationUnitName: str

@typing.type_check_only
class ListAttestationRulesResponse(typing.TypedDict, total=False):
    attestationRules: _list[AttestationRule]
    nextPageToken: str

@typing.type_check_only
class ListOauthClientCredentialsResponse(typing.TypedDict, total=False):
    oauthClientCredentials: _list[OauthClientCredential]

@typing.type_check_only
class ListOauthClientsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    oauthClients: _list[OauthClient]

@typing.type_check_only
class ListRolesResponse(typing.TypedDict, total=False):
    nextPageToken: str
    roles: _list[Role]

@typing.type_check_only
class ListServiceAccountKeysResponse(typing.TypedDict, total=False):
    keys: _list[ServiceAccountKey]

@typing.type_check_only
class ListServiceAccountsResponse(typing.TypedDict, total=False):
    accounts: _list[ServiceAccount]
    nextPageToken: str

@typing.type_check_only
class ListWorkforcePoolProviderKeysResponse(typing.TypedDict, total=False):
    nextPageToken: str
    workforcePoolProviderKeys: _list[WorkforcePoolProviderKey]

@typing.type_check_only
class ListWorkforcePoolProviderScimTenantsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    workforcePoolProviderScimTenants: _list[WorkforcePoolProviderScimTenant]

@typing.type_check_only
class ListWorkforcePoolProviderScimTokensResponse(typing.TypedDict, total=False):
    nextPageToken: str
    workforcePoolProviderScimTokens: _list[WorkforcePoolProviderScimToken]

@typing.type_check_only
class ListWorkforcePoolProvidersResponse(typing.TypedDict, total=False):
    nextPageToken: str
    workforcePoolProviders: _list[WorkforcePoolProvider]

@typing.type_check_only
class ListWorkforcePoolsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    workforcePools: _list[WorkforcePool]

@typing.type_check_only
class ListWorkloadIdentityPoolManagedIdentitiesResponse(typing.TypedDict, total=False):
    nextPageToken: str
    workloadIdentityPoolManagedIdentities: _list[WorkloadIdentityPoolManagedIdentity]

@typing.type_check_only
class ListWorkloadIdentityPoolNamespacesResponse(typing.TypedDict, total=False):
    nextPageToken: str
    workloadIdentityPoolNamespaces: _list[WorkloadIdentityPoolNamespace]

@typing.type_check_only
class ListWorkloadIdentityPoolProviderKeysResponse(typing.TypedDict, total=False):
    nextPageToken: str
    workloadIdentityPoolProviderKeys: _list[WorkloadIdentityPoolProviderKey]

@typing.type_check_only
class ListWorkloadIdentityPoolProvidersResponse(typing.TypedDict, total=False):
    nextPageToken: str
    workloadIdentityPoolProviders: _list[WorkloadIdentityPoolProvider]

@typing.type_check_only
class ListWorkloadIdentityPoolsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    workloadIdentityPools: _list[WorkloadIdentityPool]

@typing.type_check_only
class OauthClient(typing.TypedDict, total=False):
    allowedGrantTypes: _list[
        typing.Literal[
            "GRANT_TYPE_UNSPECIFIED", "AUTHORIZATION_CODE_GRANT", "REFRESH_TOKEN_GRANT"
        ]
    ]
    allowedRedirectUris: _list[str]
    allowedScopes: _list[str]
    clientId: str
    clientType: typing.Literal[
        "CLIENT_TYPE_UNSPECIFIED", "PUBLIC_CLIENT", "CONFIDENTIAL_CLIENT"
    ]
    description: str
    disabled: bool
    displayName: str
    expireTime: str
    name: str
    state: typing.Literal["STATE_UNSPECIFIED", "ACTIVE", "DELETED"]

@typing.type_check_only
class OauthClientCredential(typing.TypedDict, total=False):
    clientSecret: str
    disabled: bool
    displayName: str
    name: str

@typing.type_check_only
class Oidc(typing.TypedDict, total=False):
    allowedAudiences: _list[str]
    issuerUri: str
    jwksJson: str

@typing.type_check_only
class Operation(typing.TypedDict, total=False):
    done: bool
    error: Status
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class OperationMetadata(typing.TypedDict, total=False):
    apiVersion: str
    cancelRequested: bool
    createTime: str
    endTime: str
    statusDetail: str
    target: str
    verb: str

@typing.type_check_only
class OwnerService(typing.TypedDict, total=False):
    principalSubject: str

@typing.type_check_only
class PatchServiceAccountRequest(typing.TypedDict, total=False):
    serviceAccount: ServiceAccount
    updateMask: str

@typing.type_check_only
class Permission(typing.TypedDict, total=False):
    apiDisabled: bool
    customRolesSupportLevel: typing.Literal["SUPPORTED", "TESTING", "NOT_SUPPORTED"]
    description: str
    name: str
    onlyInPredefinedRoles: bool
    primaryPermission: str
    stage: typing.Literal["ALPHA", "BETA", "GA", "DEPRECATED"]
    title: str

@typing.type_check_only
class PermissionDelta(typing.TypedDict, total=False):
    addedPermissions: _list[str]
    removedPermissions: _list[str]

@typing.type_check_only
class Policy(typing.TypedDict, total=False):
    auditConfigs: _list[AuditConfig]
    bindings: _list[Binding]
    etag: str
    version: int

@typing.type_check_only
class PolicyDelta(typing.TypedDict, total=False):
    bindingDeltas: _list[BindingDelta]

@typing.type_check_only
class QueryAuditableServicesRequest(typing.TypedDict, total=False):
    fullResourceName: str

@typing.type_check_only
class QueryAuditableServicesResponse(typing.TypedDict, total=False):
    services: _list[AuditableService]

@typing.type_check_only
class QueryGrantableRolesRequest(typing.TypedDict, total=False):
    fullResourceName: str
    pageSize: int
    pageToken: str
    view: typing.Literal["BASIC", "FULL"]

@typing.type_check_only
class QueryGrantableRolesResponse(typing.TypedDict, total=False):
    nextPageToken: str
    roles: _list[Role]

@typing.type_check_only
class QueryTestablePermissionsRequest(typing.TypedDict, total=False):
    fullResourceName: str
    pageSize: int
    pageToken: str

@typing.type_check_only
class QueryTestablePermissionsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    permissions: _list[Permission]

@typing.type_check_only
class ReconciliationOperationMetadata(typing.TypedDict, total=False):
    deleteResource: bool
    exclusiveAction: typing.Literal["UNKNOWN_REPAIR_ACTION", "DELETE", "RETRY"]

@typing.type_check_only
class RemoveAttestationRuleRequest(typing.TypedDict, total=False):
    attestationRule: AttestationRule

@typing.type_check_only
class Role(typing.TypedDict, total=False):
    deleted: bool
    description: str
    etag: str
    includedPermissions: _list[str]
    name: str
    stage: typing.Literal["ALPHA", "BETA", "GA", "DEPRECATED", "DISABLED", "EAP"]
    title: str

@typing.type_check_only
class Saml(typing.TypedDict, total=False):
    idpMetadataXml: str

@typing.type_check_only
class ServiceAccount(typing.TypedDict, total=False):
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
class ServiceAccountKey(typing.TypedDict, total=False):
    disableReason: typing.Literal[
        "SERVICE_ACCOUNT_KEY_DISABLE_REASON_UNSPECIFIED",
        "SERVICE_ACCOUNT_KEY_DISABLE_REASON_USER_INITIATED",
        "SERVICE_ACCOUNT_KEY_DISABLE_REASON_EXPOSED",
        "SERVICE_ACCOUNT_KEY_DISABLE_REASON_COMPROMISE_DETECTED",
    ]
    disabled: bool
    extendedStatus: _list[ExtendedStatus]
    keyAlgorithm: typing.Literal[
        "KEY_ALG_UNSPECIFIED", "KEY_ALG_RSA_1024", "KEY_ALG_RSA_2048"
    ]
    keyOrigin: typing.Literal["ORIGIN_UNSPECIFIED", "USER_PROVIDED", "GOOGLE_PROVIDED"]
    keyType: typing.Literal["KEY_TYPE_UNSPECIFIED", "USER_MANAGED", "SYSTEM_MANAGED"]
    name: str
    privateKeyData: str
    privateKeyType: typing.Literal[
        "TYPE_UNSPECIFIED", "TYPE_PKCS12_FILE", "TYPE_GOOGLE_CREDENTIALS_FILE"
    ]
    publicKeyData: str
    validAfterTime: str
    validBeforeTime: str

@typing.type_check_only
class ServiceConfig(typing.TypedDict, total=False):
    domain: str

@typing.type_check_only
class SetAttestationRulesRequest(typing.TypedDict, total=False):
    attestationRules: _list[AttestationRule]

@typing.type_check_only
class SetIamPolicyRequest(typing.TypedDict, total=False):
    policy: Policy
    updateMask: str

@typing.type_check_only
class SignBlobRequest(typing.TypedDict, total=False):
    bytesToSign: str

@typing.type_check_only
class SignBlobResponse(typing.TypedDict, total=False):
    keyId: str
    signature: str

@typing.type_check_only
class SignJwtRequest(typing.TypedDict, total=False):
    payload: str

@typing.type_check_only
class SignJwtResponse(typing.TypedDict, total=False):
    keyId: str
    signedJwt: str

@typing.type_check_only
class Status(typing.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class TestIamPermissionsRequest(typing.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class TestIamPermissionsResponse(typing.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class TrustAnchor(typing.TypedDict, total=False):
    pemCertificate: str

@typing.type_check_only
class TrustStore(typing.TypedDict, total=False):
    intermediateCas: _list[IntermediateCA]
    trustAnchors: _list[TrustAnchor]
    trustDefaultSharedCa: bool

@typing.type_check_only
class UndeleteOauthClientRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class UndeleteRoleRequest(typing.TypedDict, total=False):
    etag: str

@typing.type_check_only
class UndeleteServiceAccountRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class UndeleteServiceAccountResponse(typing.TypedDict, total=False):
    restoredAccount: ServiceAccount

@typing.type_check_only
class UndeleteWorkforcePoolProviderKeyRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class UndeleteWorkforcePoolProviderRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class UndeleteWorkforcePoolProviderScimTenantRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class UndeleteWorkforcePoolRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class UndeleteWorkforcePoolSubjectRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class UndeleteWorkloadIdentityPoolManagedIdentityRequest(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class UndeleteWorkloadIdentityPoolNamespaceRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class UndeleteWorkloadIdentityPoolProviderKeyRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class UndeleteWorkloadIdentityPoolProviderRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class UndeleteWorkloadIdentityPoolRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class UploadServiceAccountKeyRequest(typing.TypedDict, total=False):
    publicKeyData: str

@typing.type_check_only
class WorkforcePool(typing.TypedDict, total=False):
    accessRestrictions: AccessRestrictions
    description: str
    disabled: bool
    displayName: str
    expireTime: str
    name: str
    parent: str
    sessionDuration: str
    state: typing.Literal["STATE_UNSPECIFIED", "ACTIVE", "DELETED"]

@typing.type_check_only
class WorkforcePoolProvider(typing.TypedDict, total=False):
    attributeCondition: str
    attributeMapping: dict[str, typing.Any]
    description: str
    detailedAuditLogging: bool
    disabled: bool
    displayName: str
    expireTime: str
    extendedAttributesOauth2Client: (
        GoogleIamAdminV1WorkforcePoolProviderExtraAttributesOAuth2Client
    )
    extraAttributesOauth2Client: (
        GoogleIamAdminV1WorkforcePoolProviderExtraAttributesOAuth2Client
    )
    name: str
    oidc: GoogleIamAdminV1WorkforcePoolProviderOidc
    saml: GoogleIamAdminV1WorkforcePoolProviderSaml
    scimUsage: typing.Literal["SCIM_USAGE_UNSPECIFIED", "ENABLED_FOR_GROUPS"]
    state: typing.Literal["STATE_UNSPECIFIED", "ACTIVE", "DELETED"]

@typing.type_check_only
class WorkforcePoolProviderKey(typing.TypedDict, total=False):
    expireTime: str
    keyData: KeyData
    name: str
    state: typing.Literal["STATE_UNSPECIFIED", "ACTIVE", "DELETED"]
    use: typing.Literal["KEY_USE_UNSPECIFIED", "ENCRYPTION"]

@typing.type_check_only
class WorkforcePoolProviderScimTenant(typing.TypedDict, total=False):
    baseUri: str
    claimMapping: dict[str, typing.Any]
    description: str
    displayName: str
    name: str
    purgeTime: str
    serviceAgent: str
    state: typing.Literal["STATE_UNSPECIFIED", "ACTIVE", "DELETED"]

@typing.type_check_only
class WorkforcePoolProviderScimToken(typing.TypedDict, total=False):
    displayName: str
    name: str
    securityToken: str
    state: typing.Literal["STATE_UNSPECIFIED", "ACTIVE", "DELETED"]

@typing.type_check_only
class WorkloadIdentityPool(typing.TypedDict, total=False):
    description: str
    disabled: bool
    displayName: str
    expireTime: str
    inlineCertificateIssuanceConfig: InlineCertificateIssuanceConfig
    inlineTrustConfig: InlineTrustConfig
    mode: typing.Literal[
        "MODE_UNSPECIFIED", "FEDERATION_ONLY", "TRUST_DOMAIN", "SYSTEM_TRUST_DOMAIN"
    ]
    name: str
    state: typing.Literal["STATE_UNSPECIFIED", "ACTIVE", "DELETED"]

@typing.type_check_only
class WorkloadIdentityPoolManagedIdentity(typing.TypedDict, total=False):
    description: str
    disabled: bool
    expireTime: str
    name: str
    state: typing.Literal["STATE_UNSPECIFIED", "ACTIVE", "DELETED"]

@typing.type_check_only
class WorkloadIdentityPoolNamespace(typing.TypedDict, total=False):
    description: str
    disabled: bool
    expireTime: str
    name: str
    ownerService: OwnerService
    state: typing.Literal["STATE_UNSPECIFIED", "ACTIVE", "DELETED"]

@typing.type_check_only
class WorkloadIdentityPoolOperationMetadata(typing.TypedDict, total=False): ...

@typing.type_check_only
class WorkloadIdentityPoolProvider(typing.TypedDict, total=False):
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
    state: typing.Literal["STATE_UNSPECIFIED", "ACTIVE", "DELETED"]
    x509: X509

@typing.type_check_only
class WorkloadIdentityPoolProviderKey(typing.TypedDict, total=False):
    expireTime: str
    keyData: KeyData
    name: str
    state: typing.Literal["STATE_UNSPECIFIED", "ACTIVE", "DELETED"]
    use: typing.Literal["KEY_USE_UNSPECIFIED", "ENCRYPTION"]

@typing.type_check_only
class X509(typing.TypedDict, total=False):
    trustStore: TrustStore
