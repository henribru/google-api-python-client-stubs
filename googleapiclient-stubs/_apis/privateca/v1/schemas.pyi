import typing

import typing_extensions

_list = list

@typing.type_check_only
class AccessUrls(typing_extensions.TypedDict, total=False):
    caCertificateAccessUrl: str
    crlAccessUrls: _list[str]

@typing.type_check_only
class ActivateCertificateAuthorityRequest(typing_extensions.TypedDict, total=False):
    pemCaCertificate: str
    requestId: str
    subordinateConfig: SubordinateConfig

@typing.type_check_only
class AllowedKeyType(typing_extensions.TypedDict, total=False):
    ellipticCurve: EcKeyType
    rsa: RsaKeyType

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
class Binding(typing_extensions.TypedDict, total=False):
    condition: Expr
    members: _list[str]
    role: str

@typing.type_check_only
class CaOptions(typing_extensions.TypedDict, total=False):
    isCa: bool
    maxIssuerPathLength: int

@typing.type_check_only
class CaPool(typing_extensions.TypedDict, total=False):
    issuancePolicy: IssuancePolicy
    labels: dict[str, typing.Any]
    name: str
    publishingOptions: PublishingOptions
    tier: typing_extensions.Literal["TIER_UNSPECIFIED", "ENTERPRISE", "DEVOPS"]

@typing.type_check_only
class CancelOperationRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class CertChain(typing_extensions.TypedDict, total=False):
    certificates: _list[str]

@typing.type_check_only
class Certificate(typing_extensions.TypedDict, total=False):
    certificateDescription: CertificateDescription
    certificateTemplate: str
    config: CertificateConfig
    createTime: str
    issuerCertificateAuthority: str
    labels: dict[str, typing.Any]
    lifetime: str
    name: str
    pemCertificate: str
    pemCertificateChain: _list[str]
    pemCsr: str
    revocationDetails: RevocationDetails
    subjectMode: typing_extensions.Literal[
        "SUBJECT_REQUEST_MODE_UNSPECIFIED", "DEFAULT", "REFLECTED_SPIFFE"
    ]
    updateTime: str

@typing.type_check_only
class CertificateAuthority(typing_extensions.TypedDict, total=False):
    accessUrls: AccessUrls
    caCertificateDescriptions: _list[CertificateDescription]
    config: CertificateConfig
    createTime: str
    deleteTime: str
    expireTime: str
    gcsBucket: str
    keySpec: KeyVersionSpec
    labels: dict[str, typing.Any]
    lifetime: str
    name: str
    pemCaCertificates: _list[str]
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "ENABLED",
        "DISABLED",
        "STAGED",
        "AWAITING_USER_ACTIVATION",
        "DELETED",
    ]
    subordinateConfig: SubordinateConfig
    tier: typing_extensions.Literal["TIER_UNSPECIFIED", "ENTERPRISE", "DEVOPS"]
    type: typing_extensions.Literal["TYPE_UNSPECIFIED", "SELF_SIGNED", "SUBORDINATE"]
    updateTime: str

@typing.type_check_only
class CertificateConfig(typing_extensions.TypedDict, total=False):
    publicKey: PublicKey
    subjectConfig: SubjectConfig
    x509Config: X509Parameters

@typing.type_check_only
class CertificateDescription(typing_extensions.TypedDict, total=False):
    aiaIssuingCertificateUrls: _list[str]
    authorityKeyId: KeyId
    certFingerprint: CertificateFingerprint
    crlDistributionPoints: _list[str]
    publicKey: PublicKey
    subjectDescription: SubjectDescription
    subjectKeyId: KeyId
    x509Description: X509Parameters

@typing.type_check_only
class CertificateExtensionConstraints(typing_extensions.TypedDict, total=False):
    additionalExtensions: _list[ObjectId]
    knownExtensions: _list[str]

@typing.type_check_only
class CertificateFingerprint(typing_extensions.TypedDict, total=False):
    sha256Hash: str

@typing.type_check_only
class CertificateIdentityConstraints(typing_extensions.TypedDict, total=False):
    allowSubjectAltNamesPassthrough: bool
    allowSubjectPassthrough: bool
    celExpression: Expr

@typing.type_check_only
class CertificateRevocationList(typing_extensions.TypedDict, total=False):
    accessUrl: str
    createTime: str
    labels: dict[str, typing.Any]
    name: str
    pemCrl: str
    revisionId: str
    revokedCertificates: _list[RevokedCertificate]
    sequenceNumber: str
    state: typing_extensions.Literal["STATE_UNSPECIFIED", "ACTIVE", "SUPERSEDED"]
    updateTime: str

@typing.type_check_only
class CertificateTemplate(typing_extensions.TypedDict, total=False):
    createTime: str
    description: str
    identityConstraints: CertificateIdentityConstraints
    labels: dict[str, typing.Any]
    name: str
    passthroughExtensions: CertificateExtensionConstraints
    predefinedValues: X509Parameters
    updateTime: str

@typing.type_check_only
class DisableCertificateAuthorityRequest(typing_extensions.TypedDict, total=False):
    requestId: str

@typing.type_check_only
class EcKeyType(typing_extensions.TypedDict, total=False):
    signatureAlgorithm: typing_extensions.Literal[
        "EC_SIGNATURE_ALGORITHM_UNSPECIFIED", "ECDSA_P256", "ECDSA_P384", "EDDSA_25519"
    ]

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
class FetchCaCertsRequest(typing_extensions.TypedDict, total=False):
    requestId: str

@typing.type_check_only
class FetchCaCertsResponse(typing_extensions.TypedDict, total=False):
    caCerts: _list[CertChain]

@typing.type_check_only
class FetchCertificateAuthorityCsrResponse(typing_extensions.TypedDict, total=False):
    pemCsr: str

@typing.type_check_only
class IssuanceModes(typing_extensions.TypedDict, total=False):
    allowConfigBasedIssuance: bool
    allowCsrBasedIssuance: bool

@typing.type_check_only
class IssuancePolicy(typing_extensions.TypedDict, total=False):
    allowedIssuanceModes: IssuanceModes
    allowedKeyTypes: _list[AllowedKeyType]
    baselineValues: X509Parameters
    identityConstraints: CertificateIdentityConstraints
    maximumLifetime: str
    passthroughExtensions: CertificateExtensionConstraints

@typing.type_check_only
class KeyId(typing_extensions.TypedDict, total=False):
    keyId: str

@typing.type_check_only
class KeyUsage(typing_extensions.TypedDict, total=False):
    baseKeyUsage: KeyUsageOptions
    extendedKeyUsage: ExtendedKeyUsageOptions
    unknownExtendedKeyUsages: _list[ObjectId]

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
class ListCaPoolsResponse(typing_extensions.TypedDict, total=False):
    caPools: _list[CaPool]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListCertificateAuthoritiesResponse(typing_extensions.TypedDict, total=False):
    certificateAuthorities: _list[CertificateAuthority]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListCertificateRevocationListsResponse(typing_extensions.TypedDict, total=False):
    certificateRevocationLists: _list[CertificateRevocationList]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListCertificateTemplatesResponse(typing_extensions.TypedDict, total=False):
    certificateTemplates: _list[CertificateTemplate]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListCertificatesResponse(typing_extensions.TypedDict, total=False):
    certificates: _list[Certificate]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListLocationsResponse(typing_extensions.TypedDict, total=False):
    locations: _list[Location]
    nextPageToken: str

@typing.type_check_only
class ListOperationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    operations: _list[Operation]

@typing.type_check_only
class Location(typing_extensions.TypedDict, total=False):
    displayName: str
    labels: dict[str, typing.Any]
    locationId: str
    metadata: dict[str, typing.Any]
    name: str

@typing.type_check_only
class ObjectId(typing_extensions.TypedDict, total=False):
    objectIdPath: _list[int]

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
    createTime: str
    endTime: str
    requestedCancellation: bool
    statusMessage: str
    target: str
    verb: str

@typing.type_check_only
class Policy(typing_extensions.TypedDict, total=False):
    auditConfigs: _list[AuditConfig]
    bindings: _list[Binding]
    etag: str
    version: int

@typing.type_check_only
class PublicKey(typing_extensions.TypedDict, total=False):
    format: typing_extensions.Literal["KEY_FORMAT_UNSPECIFIED", "PEM"]
    key: str

@typing.type_check_only
class PublishingOptions(typing_extensions.TypedDict, total=False):
    publishCaCert: bool
    publishCrl: bool

@typing.type_check_only
class ReconciliationOperationMetadata(typing_extensions.TypedDict, total=False):
    deleteResource: bool
    exclusiveAction: typing_extensions.Literal[
        "UNKNOWN_REPAIR_ACTION", "DELETE", "RETRY"
    ]

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
class RsaKeyType(typing_extensions.TypedDict, total=False):
    maxModulusSize: str
    minModulusSize: str

@typing.type_check_only
class SetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    policy: Policy
    updateMask: str

@typing.type_check_only
class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class Subject(typing_extensions.TypedDict, total=False):
    commonName: str
    countryCode: str
    locality: str
    organization: str
    organizationalUnit: str
    postalCode: str
    province: str
    streetAddress: str

@typing.type_check_only
class SubjectAltNames(typing_extensions.TypedDict, total=False):
    customSans: _list[X509Extension]
    dnsNames: _list[str]
    emailAddresses: _list[str]
    ipAddresses: _list[str]
    uris: _list[str]

@typing.type_check_only
class SubjectConfig(typing_extensions.TypedDict, total=False):
    subject: Subject
    subjectAltName: SubjectAltNames

@typing.type_check_only
class SubjectDescription(typing_extensions.TypedDict, total=False):
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
    pemCertificates: _list[str]

@typing.type_check_only
class TestIamPermissionsRequest(typing_extensions.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class TestIamPermissionsResponse(typing_extensions.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class UndeleteCertificateAuthorityRequest(typing_extensions.TypedDict, total=False):
    requestId: str

@typing.type_check_only
class X509Extension(typing_extensions.TypedDict, total=False):
    critical: bool
    objectId: ObjectId
    value: str

@typing.type_check_only
class X509Parameters(typing_extensions.TypedDict, total=False):
    additionalExtensions: _list[X509Extension]
    aiaOcspServers: _list[str]
    caOptions: CaOptions
    keyUsage: KeyUsage
    policyIds: _list[ObjectId]
