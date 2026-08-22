import typing

_list = list

@typing.type_check_only
class AccessUrls(typing.TypedDict, total=False):
    caCertificateAccessUrl: str
    crlAccessUrls: _list[str]

@typing.type_check_only
class ActivateCertificateAuthorityRequest(typing.TypedDict, total=False):
    pemCaCertificate: str
    requestId: str
    subordinateConfig: SubordinateConfig

@typing.type_check_only
class AllowedKeyType(typing.TypedDict, total=False):
    ellipticCurve: EcKeyType
    rsa: RsaKeyType

@typing.type_check_only
class AttributeTypeAndValue(typing.TypedDict, total=False):
    objectId: ObjectId
    type: typing.Literal[
        "ATTRIBUTE_TYPE_UNSPECIFIED",
        "COMMON_NAME",
        "COUNTRY_CODE",
        "ORGANIZATION",
        "ORGANIZATIONAL_UNIT",
        "LOCALITY",
        "PROVINCE",
        "STREET_ADDRESS",
        "POSTAL_CODE",
    ]
    value: str

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
class Binding(typing.TypedDict, total=False):
    condition: Expr
    members: _list[str]
    role: str

@typing.type_check_only
class CaOptions(typing.TypedDict, total=False):
    isCa: bool
    maxIssuerPathLength: int

@typing.type_check_only
class CaPool(typing.TypedDict, total=False):
    encryptionSpec: EncryptionSpec
    issuancePolicy: IssuancePolicy
    labels: dict[str, typing.Any]
    name: str
    publishingOptions: PublishingOptions
    tier: typing.Literal["TIER_UNSPECIFIED", "ENTERPRISE", "DEVOPS"]

@typing.type_check_only
class CancelOperationRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class CertChain(typing.TypedDict, total=False):
    certificates: _list[str]

@typing.type_check_only
class Certificate(typing.TypedDict, total=False):
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
    requestedNotBeforeTime: str
    revocationDetails: RevocationDetails
    subjectMode: typing.Literal[
        "SUBJECT_REQUEST_MODE_UNSPECIFIED",
        "DEFAULT",
        "RDN_SEQUENCE",
        "REFLECTED_SPIFFE",
    ]
    updateTime: str

@typing.type_check_only
class CertificateAuthority(typing.TypedDict, total=False):
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
    satisfiesPzi: bool
    satisfiesPzs: bool
    state: typing.Literal[
        "STATE_UNSPECIFIED",
        "ENABLED",
        "DISABLED",
        "STAGED",
        "AWAITING_USER_ACTIVATION",
        "DELETED",
    ]
    subordinateConfig: SubordinateConfig
    tier: typing.Literal["TIER_UNSPECIFIED", "ENTERPRISE", "DEVOPS"]
    type: typing.Literal["TYPE_UNSPECIFIED", "SELF_SIGNED", "SUBORDINATE"]
    updateTime: str
    userDefinedAccessUrls: UserDefinedAccessUrls

@typing.type_check_only
class CertificateConfig(typing.TypedDict, total=False):
    publicKey: PublicKey
    subjectConfig: SubjectConfig
    subjectKeyId: CertificateConfigKeyId
    x509Config: X509Parameters

@typing.type_check_only
class CertificateConfigKeyId(typing.TypedDict, total=False):
    keyId: str

@typing.type_check_only
class CertificateDescription(typing.TypedDict, total=False):
    aiaIssuingCertificateUrls: _list[str]
    authorityKeyId: KeyId
    certFingerprint: CertificateFingerprint
    crlDistributionPoints: _list[str]
    publicKey: PublicKey
    subjectDescription: SubjectDescription
    subjectKeyId: KeyId
    tbsCertificateDigest: str
    x509Description: X509Parameters

@typing.type_check_only
class CertificateExtensionConstraints(typing.TypedDict, total=False):
    additionalExtensions: _list[ObjectId]
    knownExtensions: _list[
        typing.Literal[
            "KNOWN_CERTIFICATE_EXTENSION_UNSPECIFIED",
            "BASE_KEY_USAGE",
            "EXTENDED_KEY_USAGE",
            "CA_OPTIONS",
            "POLICY_IDS",
            "AIA_OCSP_SERVERS",
            "NAME_CONSTRAINTS",
        ]
    ]

@typing.type_check_only
class CertificateFingerprint(typing.TypedDict, total=False):
    sha256Hash: str

@typing.type_check_only
class CertificateIdentityConstraints(typing.TypedDict, total=False):
    allowSubjectAltNamesPassthrough: bool
    allowSubjectPassthrough: bool
    celExpression: Expr

@typing.type_check_only
class CertificateRevocationList(typing.TypedDict, total=False):
    accessUrl: str
    createTime: str
    labels: dict[str, typing.Any]
    name: str
    pemCrl: str
    revisionId: str
    revokedCertificates: _list[RevokedCertificate]
    sequenceNumber: str
    state: typing.Literal["STATE_UNSPECIFIED", "ACTIVE", "SUPERSEDED"]
    updateTime: str

@typing.type_check_only
class CertificateTemplate(typing.TypedDict, total=False):
    createTime: str
    description: str
    identityConstraints: CertificateIdentityConstraints
    labels: dict[str, typing.Any]
    maximumLifetime: str
    name: str
    passthroughExtensions: CertificateExtensionConstraints
    predefinedValues: X509Parameters
    updateTime: str

@typing.type_check_only
class DisableCertificateAuthorityRequest(typing.TypedDict, total=False):
    ignoreDependentResources: bool
    requestId: str

@typing.type_check_only
class EcKeyType(typing.TypedDict, total=False):
    signatureAlgorithm: typing.Literal[
        "EC_SIGNATURE_ALGORITHM_UNSPECIFIED", "ECDSA_P256", "ECDSA_P384", "EDDSA_25519"
    ]

@typing.type_check_only
class Empty(typing.TypedDict, total=False): ...

@typing.type_check_only
class EnableCertificateAuthorityRequest(typing.TypedDict, total=False):
    requestId: str

@typing.type_check_only
class EncryptionSpec(typing.TypedDict, total=False):
    cloudKmsKey: str

@typing.type_check_only
class Expr(typing.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str

@typing.type_check_only
class ExtendedKeyUsageOptions(typing.TypedDict, total=False):
    clientAuth: bool
    codeSigning: bool
    emailProtection: bool
    ocspSigning: bool
    serverAuth: bool
    timeStamping: bool

@typing.type_check_only
class FetchCaCertsRequest(typing.TypedDict, total=False):
    requestId: str

@typing.type_check_only
class FetchCaCertsResponse(typing.TypedDict, total=False):
    caCerts: _list[CertChain]

@typing.type_check_only
class FetchCertificateAuthorityCsrResponse(typing.TypedDict, total=False):
    pemCsr: str

@typing.type_check_only
class IssuanceModes(typing.TypedDict, total=False):
    allowConfigBasedIssuance: bool
    allowCsrBasedIssuance: bool

@typing.type_check_only
class IssuancePolicy(typing.TypedDict, total=False):
    allowRequesterSpecifiedNotBeforeTime: bool
    allowedIssuanceModes: IssuanceModes
    allowedKeyTypes: _list[AllowedKeyType]
    backdateDuration: str
    baselineValues: X509Parameters
    identityConstraints: CertificateIdentityConstraints
    maximumLifetime: str
    passthroughExtensions: CertificateExtensionConstraints

@typing.type_check_only
class KeyId(typing.TypedDict, total=False):
    keyId: str

@typing.type_check_only
class KeyUsage(typing.TypedDict, total=False):
    baseKeyUsage: KeyUsageOptions
    extendedKeyUsage: ExtendedKeyUsageOptions
    unknownExtendedKeyUsages: _list[ObjectId]

@typing.type_check_only
class KeyUsageOptions(typing.TypedDict, total=False):
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
class KeyVersionSpec(typing.TypedDict, total=False):
    algorithm: typing.Literal[
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
class ListCaPoolsResponse(typing.TypedDict, total=False):
    caPools: _list[CaPool]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListCertificateAuthoritiesResponse(typing.TypedDict, total=False):
    certificateAuthorities: _list[CertificateAuthority]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListCertificateRevocationListsResponse(typing.TypedDict, total=False):
    certificateRevocationLists: _list[CertificateRevocationList]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListCertificateTemplatesResponse(typing.TypedDict, total=False):
    certificateTemplates: _list[CertificateTemplate]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListCertificatesResponse(typing.TypedDict, total=False):
    certificates: _list[Certificate]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListLocationsResponse(typing.TypedDict, total=False):
    locations: _list[Location]
    nextPageToken: str

@typing.type_check_only
class ListOperationsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    operations: _list[Operation]
    unreachable: _list[str]

@typing.type_check_only
class Location(typing.TypedDict, total=False):
    displayName: str
    labels: dict[str, typing.Any]
    locationId: str
    metadata: dict[str, typing.Any]
    name: str

@typing.type_check_only
class NameConstraints(typing.TypedDict, total=False):
    critical: bool
    excludedDnsNames: _list[str]
    excludedEmailAddresses: _list[str]
    excludedIpRanges: _list[str]
    excludedUris: _list[str]
    permittedDnsNames: _list[str]
    permittedEmailAddresses: _list[str]
    permittedIpRanges: _list[str]
    permittedUris: _list[str]

@typing.type_check_only
class ObjectId(typing.TypedDict, total=False):
    objectIdPath: _list[int]

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
    createTime: str
    endTime: str
    requestedCancellation: bool
    statusMessage: str
    target: str
    verb: str

@typing.type_check_only
class Policy(typing.TypedDict, total=False):
    auditConfigs: _list[AuditConfig]
    bindings: _list[Binding]
    etag: str
    version: int

@typing.type_check_only
class PublicKey(typing.TypedDict, total=False):
    format: typing.Literal["KEY_FORMAT_UNSPECIFIED", "PEM"]
    key: str

@typing.type_check_only
class PublishingOptions(typing.TypedDict, total=False):
    encodingFormat: typing.Literal["ENCODING_FORMAT_UNSPECIFIED", "PEM", "DER"]
    publishCaCert: bool
    publishCrl: bool

@typing.type_check_only
class RelativeDistinguishedName(typing.TypedDict, total=False):
    attributes: _list[AttributeTypeAndValue]

@typing.type_check_only
class RevocationDetails(typing.TypedDict, total=False):
    revocationState: typing.Literal[
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
class RevokeCertificateRequest(typing.TypedDict, total=False):
    reason: typing.Literal[
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
class RevokedCertificate(typing.TypedDict, total=False):
    certificate: str
    hexSerialNumber: str
    revocationReason: typing.Literal[
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
class RsaKeyType(typing.TypedDict, total=False):
    maxModulusSize: str
    minModulusSize: str

@typing.type_check_only
class SetIamPolicyRequest(typing.TypedDict, total=False):
    policy: Policy
    updateMask: str

@typing.type_check_only
class Status(typing.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class Subject(typing.TypedDict, total=False):
    commonName: str
    countryCode: str
    locality: str
    organization: str
    organizationalUnit: str
    postalCode: str
    province: str
    rdnSequence: _list[RelativeDistinguishedName]
    streetAddress: str

@typing.type_check_only
class SubjectAltNames(typing.TypedDict, total=False):
    customSans: _list[X509Extension]
    dnsNames: _list[str]
    emailAddresses: _list[str]
    ipAddresses: _list[str]
    uris: _list[str]

@typing.type_check_only
class SubjectConfig(typing.TypedDict, total=False):
    subject: Subject
    subjectAltName: SubjectAltNames

@typing.type_check_only
class SubjectDescription(typing.TypedDict, total=False):
    hexSerialNumber: str
    lifetime: str
    notAfterTime: str
    notBeforeTime: str
    subject: Subject
    subjectAltName: SubjectAltNames

@typing.type_check_only
class SubordinateConfig(typing.TypedDict, total=False):
    certificateAuthority: str
    pemIssuerChain: SubordinateConfigChain

@typing.type_check_only
class SubordinateConfigChain(typing.TypedDict, total=False):
    pemCertificates: _list[str]

@typing.type_check_only
class TestIamPermissionsRequest(typing.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class TestIamPermissionsResponse(typing.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class UndeleteCertificateAuthorityRequest(typing.TypedDict, total=False):
    requestId: str

@typing.type_check_only
class UserDefinedAccessUrls(typing.TypedDict, total=False):
    aiaIssuingCertificateUrls: _list[str]
    crlAccessUrls: _list[str]

@typing.type_check_only
class X509Extension(typing.TypedDict, total=False):
    critical: bool
    objectId: ObjectId
    value: str

@typing.type_check_only
class X509Parameters(typing.TypedDict, total=False):
    additionalExtensions: _list[X509Extension]
    aiaOcspServers: _list[str]
    caOptions: CaOptions
    keyUsage: KeyUsage
    nameConstraints: NameConstraints
    policyIds: _list[ObjectId]
