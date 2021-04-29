import typing

import typing_extensions

@typing.type_check_only
class AccessUrls(typing_extensions.TypedDict, total=False):
    caCertificateAccessUrl: str
    crlAccessUrl: str

@typing.type_check_only
class ActivateCertificateAuthorityRequest(typing_extensions.TypedDict, total=False):
    pemCaCertificate: str
    requestId: str
    subordinateConfig: SubordinateConfig

@typing.type_check_only
class AllowedConfigList(typing_extensions.TypedDict, total=False):
    allowedConfigValues: typing.List[ReusableConfigWrapper]

@typing.type_check_only
class AllowedSubjectAltNames(typing_extensions.TypedDict, total=False):
    allowCustomSans: bool
    allowGlobbingDnsWildcards: bool
    allowedDnsNames: typing.List[str]
    allowedEmailAddresses: typing.List[str]
    allowedIps: typing.List[str]
    allowedUris: typing.List[str]

@typing.type_check_only
class AuditConfig(typing_extensions.TypedDict, total=False):
    auditLogConfigs: typing.List[AuditLogConfig]
    service: str

@typing.type_check_only
class AuditLogConfig(typing_extensions.TypedDict, total=False):
    exemptedMembers: typing.List[str]
    logType: typing_extensions.Literal[
        "LOG_TYPE_UNSPECIFIED", "ADMIN_READ", "DATA_WRITE", "DATA_READ"
    ]

@typing.type_check_only
class Binding(typing_extensions.TypedDict, total=False):
    condition: Expr
    members: typing.List[str]
    role: str

@typing.type_check_only
class CaOptions(typing_extensions.TypedDict, total=False):
    isCa: bool
    maxIssuerPathLength: int

@typing.type_check_only
class CancelOperationRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Certificate(typing_extensions.TypedDict, total=False):
    certificateDescription: CertificateDescription
    config: CertificateConfig
    createTime: str
    labels: typing.Dict[str, typing.Any]
    lifetime: str
    name: str
    pemCertificate: str
    pemCertificateChain: typing.List[str]
    pemCsr: str
    revocationDetails: RevocationDetails
    updateTime: str

@typing.type_check_only
class CertificateAuthority(typing_extensions.TypedDict, total=False):
    accessUrls: AccessUrls
    caCertificateDescriptions: typing.List[CertificateDescription]
    certificatePolicy: CertificateAuthorityPolicy
    config: CertificateConfig
    createTime: str
    deleteTime: str
    gcsBucket: str
    issuingOptions: IssuingOptions
    keySpec: KeyVersionSpec
    labels: typing.Dict[str, typing.Any]
    lifetime: str
    name: str
    pemCaCertificates: typing.List[str]
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "ENABLED",
        "DISABLED",
        "PENDING_ACTIVATION",
        "PENDING_DELETION",
    ]
    subordinateConfig: SubordinateConfig
    tier: typing_extensions.Literal["TIER_UNSPECIFIED", "ENTERPRISE", "DEVOPS"]
    type: typing_extensions.Literal["TYPE_UNSPECIFIED", "SELF_SIGNED", "SUBORDINATE"]
    updateTime: str

@typing.type_check_only
class CertificateAuthorityPolicy(typing_extensions.TypedDict, total=False):
    allowedCommonNames: typing.List[str]
    allowedConfigList: AllowedConfigList
    allowedIssuanceModes: IssuanceModes
    allowedLocationsAndOrganizations: typing.List[Subject]
    allowedSans: AllowedSubjectAltNames
    maximumLifetime: str
    overwriteConfigValues: ReusableConfigWrapper

@typing.type_check_only
class CertificateConfig(typing_extensions.TypedDict, total=False):
    publicKey: PublicKey
    reusableConfig: ReusableConfigWrapper
    subjectConfig: SubjectConfig

@typing.type_check_only
class CertificateDescription(typing_extensions.TypedDict, total=False):
    aiaIssuingCertificateUrls: typing.List[str]
    authorityKeyId: KeyId
    certFingerprint: CertificateFingerprint
    configValues: ReusableConfigValues
    crlDistributionPoints: typing.List[str]
    publicKey: PublicKey
    subjectDescription: SubjectDescription
    subjectKeyId: KeyId

@typing.type_check_only
class CertificateFingerprint(typing_extensions.TypedDict, total=False):
    sha256Hash: str

@typing.type_check_only
class CertificateRevocationList(typing_extensions.TypedDict, total=False):
    accessUrl: str
    createTime: str
    labels: typing.Dict[str, typing.Any]
    name: str
    pemCrl: str
    revokedCertificates: typing.List[RevokedCertificate]
    sequenceNumber: str
    state: typing_extensions.Literal["STATE_UNSPECIFIED", "ACTIVE", "SUPERSEDED"]
    updateTime: str

@typing.type_check_only
class DisableCertificateAuthorityRequest(typing_extensions.TypedDict, total=False):
    requestId: str

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class EnableCertificateAuthorityRequest(typing_extensions.TypedDict, total=False):
    requestId: str

@typing.type_check_only
class Expr(typing_extensions.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str

@typing.type_check_only
class ExtendedKeyUsageOptions(typing_extensions.TypedDict, total=False):
    clientAuth: bool
    codeSigning: bool
    emailProtection: bool
    ocspSigning: bool
    serverAuth: bool
    timeStamping: bool

@typing.type_check_only
class FetchCertificateAuthorityCsrResponse(typing_extensions.TypedDict, total=False):
    pemCsr: str

@typing.type_check_only
class IssuanceModes(typing_extensions.TypedDict, total=False):
    allowConfigBasedIssuance: bool
    allowCsrBasedIssuance: bool

@typing.type_check_only
class IssuingOptions(typing_extensions.TypedDict, total=False):
    includeCaCertUrl: bool
    includeCrlAccessUrl: bool

@typing.type_check_only
class KeyId(typing_extensions.TypedDict, total=False):
    keyId: str

@typing.type_check_only
class KeyUsage(typing_extensions.TypedDict, total=False):
    baseKeyUsage: KeyUsageOptions
    extendedKeyUsage: ExtendedKeyUsageOptions
    unknownExtendedKeyUsages: typing.List[ObjectId]

@typing.type_check_only
class KeyUsageOptions(typing_extensions.TypedDict, total=False):
    certSign: bool
    contentCommitment: bool
    crlSign: bool
    dataEncipherment: bool
    decipherOnly: bool
    digitalSignature: bool
    encipherOnly: bool
    keyAgreement: bool
    keyEncipherment: bool

@typing.type_check_only
class KeyVersionSpec(typing_extensions.TypedDict, total=False):
    algorithm: typing_extensions.Literal[
        "SIGN_HASH_ALGORITHM_UNSPECIFIED",
        "RSA_PSS_2048_SHA256",
        "RSA_PSS_3072_SHA256",
        "RSA_PSS_4096_SHA256",
        "RSA_PKCS1_2048_SHA256",
        "RSA_PKCS1_3072_SHA256",
        "RSA_PKCS1_4096_SHA256",
        "EC_P256_SHA256",
        "EC_P384_SHA384",
    ]
    cloudKmsKeyVersion: str

@typing.type_check_only
class ListCertificateAuthoritiesResponse(typing_extensions.TypedDict, total=False):
    certificateAuthorities: typing.List[CertificateAuthority]
    nextPageToken: str
    unreachable: typing.List[str]

@typing.type_check_only
class ListCertificateRevocationListsResponse(typing_extensions.TypedDict, total=False):
    certificateRevocationLists: typing.List[CertificateRevocationList]
    nextPageToken: str
    unreachable: typing.List[str]

@typing.type_check_only
class ListCertificatesResponse(typing_extensions.TypedDict, total=False):
    certificates: typing.List[Certificate]
    nextPageToken: str
    unreachable: typing.List[str]

@typing.type_check_only
class ListLocationsResponse(typing_extensions.TypedDict, total=False):
    locations: typing.List[Location]
    nextPageToken: str

@typing.type_check_only
class ListOperationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    operations: typing.List[Operation]

@typing.type_check_only
class ListReusableConfigsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    reusableConfigs: typing.List[ReusableConfig]
    unreachable: typing.List[str]

@typing.type_check_only
class Location(typing_extensions.TypedDict, total=False):
    displayName: str
    labels: typing.Dict[str, typing.Any]
    locationId: str
    metadata: typing.Dict[str, typing.Any]
    name: str

@typing.type_check_only
class ObjectId(typing_extensions.TypedDict, total=False):
    objectIdPath: typing.List[int]

@typing.type_check_only
class Operation(typing_extensions.TypedDict, total=False):
    done: bool
    error: Status
    metadata: typing.Dict[str, typing.Any]
    name: str
    response: typing.Dict[str, typing.Any]

@typing.type_check_only
class OperationMetadata(typing_extensions.TypedDict, total=False):
    apiVersion: str
    createTime: str
    endTime: str
    requestedCancellation: bool
    statusMessage: str
    target: str
    verb: str

@typing.type_check_only
class Policy(typing_extensions.TypedDict, total=False):
    auditConfigs: typing.List[AuditConfig]
    bindings: typing.List[Binding]
    etag: str
    version: int

@typing.type_check_only
class PublicKey(typing_extensions.TypedDict, total=False):
    key: str
    type: typing_extensions.Literal["KEY_TYPE_UNSPECIFIED", "PEM_RSA_KEY", "PEM_EC_KEY"]

@typing.type_check_only
class ReconciliationOperationMetadata(typing_extensions.TypedDict, total=False):
    deleteResource: bool
    exclusiveAction: typing_extensions.Literal[
        "UNKNOWN_REPAIR_ACTION", "DELETE", "RETRY"
    ]

@typing.type_check_only
class RestoreCertificateAuthorityRequest(typing_extensions.TypedDict, total=False):
    requestId: str

@typing.type_check_only
class ReusableConfig(typing_extensions.TypedDict, total=False):
    createTime: str
    description: str
    labels: typing.Dict[str, typing.Any]
    name: str
    updateTime: str
    values: ReusableConfigValues

@typing.type_check_only
class ReusableConfigValues(typing_extensions.TypedDict, total=False):
    additionalExtensions: typing.List[X509Extension]
    aiaOcspServers: typing.List[str]
    caOptions: CaOptions
    keyUsage: KeyUsage
    policyIds: typing.List[ObjectId]

@typing.type_check_only
class ReusableConfigWrapper(typing_extensions.TypedDict, total=False):
    reusableConfig: str
    reusableConfigValues: ReusableConfigValues

@typing.type_check_only
class RevocationDetails(typing_extensions.TypedDict, total=False):
    revocationState: typing_extensions.Literal[
        "REVOCATION_REASON_UNSPECIFIED",
        "KEY_COMPROMISE",
        "CERTIFICATE_AUTHORITY_COMPROMISE",
        "AFFILIATION_CHANGED",
        "SUPERSEDED",
        "CESSATION_OF_OPERATION",
        "CERTIFICATE_HOLD",
        "PRIVILEGE_WITHDRAWN",
        "ATTRIBUTE_AUTHORITY_COMPROMISE",
    ]
    revocationTime: str

@typing.type_check_only
class RevokeCertificateRequest(typing_extensions.TypedDict, total=False):
    reason: typing_extensions.Literal[
        "REVOCATION_REASON_UNSPECIFIED",
        "KEY_COMPROMISE",
        "CERTIFICATE_AUTHORITY_COMPROMISE",
        "AFFILIATION_CHANGED",
        "SUPERSEDED",
        "CESSATION_OF_OPERATION",
        "CERTIFICATE_HOLD",
        "PRIVILEGE_WITHDRAWN",
        "ATTRIBUTE_AUTHORITY_COMPROMISE",
    ]
    requestId: str

@typing.type_check_only
class RevokedCertificate(typing_extensions.TypedDict, total=False):
    certificate: str
    hexSerialNumber: str
    revocationReason: typing_extensions.Literal[
        "REVOCATION_REASON_UNSPECIFIED",
        "KEY_COMPROMISE",
        "CERTIFICATE_AUTHORITY_COMPROMISE",
        "AFFILIATION_CHANGED",
        "SUPERSEDED",
        "CESSATION_OF_OPERATION",
        "CERTIFICATE_HOLD",
        "PRIVILEGE_WITHDRAWN",
        "ATTRIBUTE_AUTHORITY_COMPROMISE",
    ]

@typing.type_check_only
class ScheduleDeleteCertificateAuthorityRequest(
    typing_extensions.TypedDict, total=False
):
    ignoreActiveCertificates: bool
    requestId: str

@typing.type_check_only
class SetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    policy: Policy
    updateMask: str

@typing.type_check_only
class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: typing.List[typing.Dict[str, typing.Any]]
    message: str

@typing.type_check_only
class Subject(typing_extensions.TypedDict, total=False):
    countryCode: str
    locality: str
    organization: str
    organizationalUnit: str
    postalCode: str
    province: str
    streetAddress: str

@typing.type_check_only
class SubjectAltNames(typing_extensions.TypedDict, total=False):
    customSans: typing.List[X509Extension]
    dnsNames: typing.List[str]
    emailAddresses: typing.List[str]
    ipAddresses: typing.List[str]
    uris: typing.List[str]

@typing.type_check_only
class SubjectConfig(typing_extensions.TypedDict, total=False):
    commonName: str
    subject: Subject
    subjectAltName: SubjectAltNames

@typing.type_check_only
class SubjectDescription(typing_extensions.TypedDict, total=False):
    commonName: str
    hexSerialNumber: str
    lifetime: str
    notAfterTime: str
    notBeforeTime: str
    subject: Subject
    subjectAltName: SubjectAltNames

@typing.type_check_only
class SubordinateConfig(typing_extensions.TypedDict, total=False):
    certificateAuthority: str
    pemIssuerChain: SubordinateConfigChain

@typing.type_check_only
class SubordinateConfigChain(typing_extensions.TypedDict, total=False):
    pemCertificates: typing.List[str]

@typing.type_check_only
class TestIamPermissionsRequest(typing_extensions.TypedDict, total=False):
    permissions: typing.List[str]

@typing.type_check_only
class TestIamPermissionsResponse(typing_extensions.TypedDict, total=False):
    permissions: typing.List[str]

@typing.type_check_only
class X509Extension(typing_extensions.TypedDict, total=False):
    critical: bool
    objectId: ObjectId
    value: str
