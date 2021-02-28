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
class BillingView(typing_extensions.TypedDict, total=False):
    reportRequests: typing.List[GoogleApiServicecontrolV1ReportRequest]

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
class Exemplar(typing_extensions.TypedDict, total=False):
    attachments: typing.List[typing.Dict[str, typing.Any]]
    timestamp: str
    value: float

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
class GoogleApiServicecontrolV1AttributeValue(typing_extensions.TypedDict, total=False):
    boolValue: bool
    intValue: str
    stringValue: GoogleApiServicecontrolV1TruncatableString

@typing.type_check_only
class GoogleApiServicecontrolV1Attributes(typing_extensions.TypedDict, total=False):
    attributeMap: typing.Dict[str, typing.Any]
    droppedAttributesCount: int

@typing.type_check_only
class GoogleApiServicecontrolV1Distribution(typing_extensions.TypedDict, total=False):
    bucketCounts: typing.List[str]
    count: str
    exemplars: typing.List[Exemplar]
    explicitBuckets: GoogleApiServicecontrolV1ExplicitBuckets
    exponentialBuckets: GoogleApiServicecontrolV1ExponentialBuckets
    linearBuckets: GoogleApiServicecontrolV1LinearBuckets
    maximum: float
    mean: float
    minimum: float
    sumOfSquaredDeviation: float

@typing.type_check_only
class GoogleApiServicecontrolV1ExplicitBuckets(
    typing_extensions.TypedDict, total=False
):
    bounds: typing.List[float]

@typing.type_check_only
class GoogleApiServicecontrolV1ExponentialBuckets(
    typing_extensions.TypedDict, total=False
):
    growthFactor: float
    numFiniteBuckets: int
    scale: float

@typing.type_check_only
class GoogleApiServicecontrolV1HttpRequest(typing_extensions.TypedDict, total=False):
    cacheFillBytes: str
    cacheHit: bool
    cacheLookup: bool
    cacheValidatedWithOriginServer: bool
    latency: str
    protocol: str
    referer: str
    remoteIp: str
    requestMethod: str
    requestSize: str
    requestUrl: str
    responseSize: str
    serverIp: str
    status: int
    userAgent: str

@typing.type_check_only
class GoogleApiServicecontrolV1LinearBuckets(typing_extensions.TypedDict, total=False):
    numFiniteBuckets: int
    offset: float
    width: float

@typing.type_check_only
class GoogleApiServicecontrolV1LogEntry(typing_extensions.TypedDict, total=False):
    httpRequest: GoogleApiServicecontrolV1HttpRequest
    insertId: str
    labels: typing.Dict[str, typing.Any]
    name: str
    operation: GoogleApiServicecontrolV1LogEntryOperation
    protoPayload: typing.Dict[str, typing.Any]
    severity: typing_extensions.Literal[
        "DEFAULT",
        "DEBUG",
        "INFO",
        "NOTICE",
        "WARNING",
        "ERROR",
        "CRITICAL",
        "ALERT",
        "EMERGENCY",
    ]
    sourceLocation: GoogleApiServicecontrolV1LogEntrySourceLocation
    structPayload: typing.Dict[str, typing.Any]
    textPayload: str
    timestamp: str
    trace: str

@typing.type_check_only
class GoogleApiServicecontrolV1LogEntryOperation(
    typing_extensions.TypedDict, total=False
):
    first: bool
    id: str
    last: bool
    producer: str

@typing.type_check_only
class GoogleApiServicecontrolV1LogEntrySourceLocation(
    typing_extensions.TypedDict, total=False
):
    file: str
    function: str
    line: str

@typing.type_check_only
class GoogleApiServicecontrolV1MetricValue(typing_extensions.TypedDict, total=False):
    boolValue: bool
    distributionValue: GoogleApiServicecontrolV1Distribution
    doubleValue: float
    endTime: str
    int64Value: str
    labels: typing.Dict[str, typing.Any]
    moneyValue: Money
    startTime: str
    stringValue: str

@typing.type_check_only
class GoogleApiServicecontrolV1MetricValueSet(typing_extensions.TypedDict, total=False):
    metricName: str
    metricValues: typing.List[GoogleApiServicecontrolV1MetricValue]

@typing.type_check_only
class GoogleApiServicecontrolV1Operation(typing_extensions.TypedDict, total=False):
    consumerId: str
    endTime: str
    extensions: typing.List[typing.Dict[str, typing.Any]]
    importance: typing_extensions.Literal["LOW", "HIGH", "DEBUG"]
    labels: typing.Dict[str, typing.Any]
    logEntries: typing.List[GoogleApiServicecontrolV1LogEntry]
    metricValueSets: typing.List[GoogleApiServicecontrolV1MetricValueSet]
    operationId: str
    operationName: str
    quotaProperties: GoogleApiServicecontrolV1QuotaProperties
    resources: typing.List[GoogleApiServicecontrolV1ResourceInfo]
    startTime: str
    traceSpans: typing.List[GoogleApiServicecontrolV1TraceSpan]
    userLabels: typing.Dict[str, typing.Any]

@typing.type_check_only
class GoogleApiServicecontrolV1QuotaProperties(
    typing_extensions.TypedDict, total=False
):
    quotaMode: typing_extensions.Literal[
        "ACQUIRE", "ACQUIRE_BEST_EFFORT", "CHECK", "RELEASE"
    ]

@typing.type_check_only
class GoogleApiServicecontrolV1ReportRequest(typing_extensions.TypedDict, total=False):
    operations: typing.List[GoogleApiServicecontrolV1Operation]
    serviceConfigId: str
    serviceName: str

@typing.type_check_only
class GoogleApiServicecontrolV1ResourceInfo(typing_extensions.TypedDict, total=False):
    resourceContainer: str
    resourceLocation: str
    resourceName: str

@typing.type_check_only
class GoogleApiServicecontrolV1TraceSpan(typing_extensions.TypedDict, total=False):
    attributes: GoogleApiServicecontrolV1Attributes
    childSpanCount: int
    displayName: GoogleApiServicecontrolV1TruncatableString
    endTime: str
    name: str
    parentSpanId: str
    sameProcessAsParentSpan: bool
    spanId: str
    spanKind: typing_extensions.Literal[
        "SPAN_KIND_UNSPECIFIED", "INTERNAL", "SERVER", "CLIENT", "PRODUCER", "CONSUMER"
    ]
    startTime: str
    status: Status

@typing.type_check_only
class GoogleApiServicecontrolV1TruncatableString(
    typing_extensions.TypedDict, total=False
):
    truncatedByteCount: int
    value: str

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
class Money(typing_extensions.TypedDict, total=False):
    currencyCode: str
    nanos: int
    units: str

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
