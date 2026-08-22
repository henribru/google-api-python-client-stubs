import typing

_list = list

@typing.type_check_only
class AvroFileFormat(typing.TypedDict, total=False): ...

@typing.type_check_only
class BackfillAllStrategy(typing.TypedDict, total=False):
    mysqlExcludedObjects: MysqlRdbms
    oracleExcludedObjects: OracleRdbms

@typing.type_check_only
class BackfillJob(typing.TypedDict, total=False):
    errors: _list[Error]
    lastEndTime: str
    lastStartTime: str
    state: typing.Literal[
        "STATE_UNSPECIFIED",
        "NOT_STARTED",
        "PENDING",
        "ACTIVE",
        "STOPPED",
        "FAILED",
        "COMPLETED",
        "UNSUPPORTED",
    ]
    trigger: typing.Literal["TRIGGER_UNSPECIFIED", "AUTOMATIC", "MANUAL"]

@typing.type_check_only
class BackfillNoneStrategy(typing.TypedDict, total=False): ...

@typing.type_check_only
class BadRequest(typing.TypedDict, total=False):
    fieldViolations: _list[FieldViolation]

@typing.type_check_only
class CancelOperationRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class ConnectionProfile(typing.TypedDict, total=False):
    createTime: str
    displayName: str
    forwardSshConnectivity: ForwardSshTunnelConnectivity
    gcsProfile: GcsProfile
    labels: dict[str, typing.Any]
    mysqlProfile: MysqlProfile
    name: str
    noConnectivity: NoConnectivitySettings
    oracleProfile: OracleProfile
    privateConnectivity: PrivateConnectivity
    staticServiceIpConnectivity: StaticServiceIpConnectivity
    updateTime: str

@typing.type_check_only
class DebugInfo(typing.TypedDict, total=False):
    detail: str
    stackEntries: _list[str]

@typing.type_check_only
class DestinationConfig(typing.TypedDict, total=False):
    destinationConnectionProfileName: str
    gcsDestinationConfig: GcsDestinationConfig

@typing.type_check_only
class DiscoverConnectionProfileRequest(typing.TypedDict, total=False):
    connectionProfile: ConnectionProfile
    connectionProfileName: str
    mysqlRdbms: MysqlRdbms
    oracleRdbms: OracleRdbms
    recursionDepth: int
    recursive: bool

@typing.type_check_only
class DiscoverConnectionProfileResponse(typing.TypedDict, total=False):
    mysqlRdbms: MysqlRdbms
    oracleRdbms: OracleRdbms

@typing.type_check_only
class DropLargeObjects(typing.TypedDict, total=False): ...

@typing.type_check_only
class Empty(typing.TypedDict, total=False): ...

@typing.type_check_only
class Error(typing.TypedDict, total=False):
    details: dict[str, typing.Any]
    errorTime: str
    errorUuid: str
    message: str
    reason: str

@typing.type_check_only
class ErrorInfo(typing.TypedDict, total=False):
    domain: str
    metadata: dict[str, typing.Any]
    reason: str

@typing.type_check_only
class FetchErrorsRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class FetchErrorsResponse(typing.TypedDict, total=False):
    errors: _list[Error]

@typing.type_check_only
class FetchStaticIpsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    staticIps: _list[str]

@typing.type_check_only
class FieldViolation(typing.TypedDict, total=False):
    description: str
    field: str
    localizedMessage: LocalizedMessage
    reason: str

@typing.type_check_only
class ForwardSshTunnelConnectivity(typing.TypedDict, total=False):
    hostname: str
    password: str
    port: int
    privateKey: str
    username: str

@typing.type_check_only
class GcsDestinationConfig(typing.TypedDict, total=False):
    avroFileFormat: AvroFileFormat
    fileRotationInterval: str
    fileRotationMb: int
    gcsFileFormat: typing.Literal["GCS_FILE_FORMAT_UNSPECIFIED", "AVRO"]
    jsonFileFormat: JsonFileFormat
    path: str

@typing.type_check_only
class GcsProfile(typing.TypedDict, total=False):
    bucketName: str
    rootPath: str

@typing.type_check_only
class Help(typing.TypedDict, total=False):
    links: _list[Link]

@typing.type_check_only
class JsonFileFormat(typing.TypedDict, total=False):
    compression: typing.Literal[
        "JSON_COMPRESSION_UNSPECIFIED", "NO_COMPRESSION", "GZIP"
    ]
    schemaFileFormat: typing.Literal[
        "SCHEMA_FILE_FORMAT_UNSPECIFIED", "NO_SCHEMA_FILE", "AVRO_SCHEMA_FILE"
    ]

@typing.type_check_only
class Link(typing.TypedDict, total=False):
    description: str
    url: str

@typing.type_check_only
class ListConnectionProfilesResponse(typing.TypedDict, total=False):
    connectionProfiles: _list[ConnectionProfile]
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
class ListPrivateConnectionsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    privateConnections: _list[PrivateConnection]
    unreachable: _list[str]

@typing.type_check_only
class ListRoutesResponse(typing.TypedDict, total=False):
    nextPageToken: str
    routes: _list[Route]
    unreachable: _list[str]

@typing.type_check_only
class ListStreamObjectsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    streamObjects: _list[StreamObject]

@typing.type_check_only
class ListStreamsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    streams: _list[Stream]
    unreachable: _list[str]

@typing.type_check_only
class LocalizedMessage(typing.TypedDict, total=False):
    locale: str
    message: str

@typing.type_check_only
class Location(typing.TypedDict, total=False):
    displayName: str
    labels: dict[str, typing.Any]
    locationId: str
    metadata: dict[str, typing.Any]
    name: str

@typing.type_check_only
class MysqlColumn(typing.TypedDict, total=False):
    collation: str
    columnName: str
    dataType: str
    length: int
    nullable: bool
    ordinalPosition: int
    primaryKey: bool

@typing.type_check_only
class MysqlDatabase(typing.TypedDict, total=False):
    databaseName: str
    mysqlTables: _list[MysqlTable]

@typing.type_check_only
class MysqlObjectIdentifier(typing.TypedDict, total=False):
    database: str
    table: str

@typing.type_check_only
class MysqlProfile(typing.TypedDict, total=False):
    hostname: str
    password: str
    port: int
    sslConfig: MysqlSslConfig
    username: str

@typing.type_check_only
class MysqlRdbms(typing.TypedDict, total=False):
    mysqlDatabases: _list[MysqlDatabase]

@typing.type_check_only
class MysqlSourceConfig(typing.TypedDict, total=False):
    allowlist: MysqlRdbms
    rejectlist: MysqlRdbms

@typing.type_check_only
class MysqlSslConfig(typing.TypedDict, total=False):
    caCertificate: str
    caCertificateSet: bool
    clientCertificate: str
    clientCertificateSet: bool
    clientKey: str
    clientKeySet: bool

@typing.type_check_only
class MysqlTable(typing.TypedDict, total=False):
    mysqlColumns: _list[MysqlColumn]
    tableName: str

@typing.type_check_only
class NoConnectivitySettings(typing.TypedDict, total=False): ...

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
    validationResult: ValidationResult
    verb: str

@typing.type_check_only
class OracleColumn(typing.TypedDict, total=False):
    columnName: str
    dataType: str
    encoding: str
    length: int
    nullable: bool
    ordinalPosition: int
    precision: int
    primaryKey: bool
    scale: int

@typing.type_check_only
class OracleObjectIdentifier(typing.TypedDict, total=False):
    schema: str
    table: str

@typing.type_check_only
class OracleProfile(typing.TypedDict, total=False):
    connectionAttributes: dict[str, typing.Any]
    databaseService: str
    hostname: str
    password: str
    port: int
    username: str

@typing.type_check_only
class OracleRdbms(typing.TypedDict, total=False):
    oracleSchemas: _list[OracleSchema]

@typing.type_check_only
class OracleSchema(typing.TypedDict, total=False):
    oracleTables: _list[OracleTable]
    schemaName: str

@typing.type_check_only
class OracleSourceConfig(typing.TypedDict, total=False):
    allowlist: OracleRdbms
    dropLargeObjects: DropLargeObjects
    rejectlist: OracleRdbms

@typing.type_check_only
class OracleTable(typing.TypedDict, total=False):
    oracleColumns: _list[OracleColumn]
    tableName: str

@typing.type_check_only
class PreconditionFailure(typing.TypedDict, total=False):
    violations: _list[PreconditionFailureViolation]

@typing.type_check_only
class PreconditionFailureViolation(typing.TypedDict, total=False):
    description: str
    subject: str
    type: str

@typing.type_check_only
class PrivateConnection(typing.TypedDict, total=False):
    createTime: str
    displayName: str
    error: Error
    labels: dict[str, typing.Any]
    name: str
    state: typing.Literal[
        "STATE_UNSPECIFIED",
        "CREATING",
        "CREATED",
        "FAILED",
        "DELETING",
        "FAILED_TO_DELETE",
    ]
    updateTime: str
    vpcPeeringConfig: VpcPeeringConfig

@typing.type_check_only
class PrivateConnectivity(typing.TypedDict, total=False):
    privateConnectionName: str

@typing.type_check_only
class QuotaFailure(typing.TypedDict, total=False):
    violations: _list[QuotaFailureViolation]

@typing.type_check_only
class QuotaFailureViolation(typing.TypedDict, total=False):
    apiService: str
    description: str
    futureQuotaValue: str
    quotaDimensions: dict[str, typing.Any]
    quotaId: str
    quotaMetric: str
    quotaValue: str
    subject: str

@typing.type_check_only
class RequestInfo(typing.TypedDict, total=False):
    requestId: str
    servingData: str

@typing.type_check_only
class ResourceInfo(typing.TypedDict, total=False):
    description: str
    owner: str
    resourceName: str
    resourceType: str

@typing.type_check_only
class RetryInfo(typing.TypedDict, total=False):
    retryDelay: str

@typing.type_check_only
class Route(typing.TypedDict, total=False):
    createTime: str
    destinationAddress: str
    destinationPort: int
    displayName: str
    labels: dict[str, typing.Any]
    name: str
    updateTime: str

@typing.type_check_only
class SourceConfig(typing.TypedDict, total=False):
    mysqlSourceConfig: MysqlSourceConfig
    oracleSourceConfig: OracleSourceConfig
    sourceConnectionProfileName: str

@typing.type_check_only
class SourceObjectIdentifier(typing.TypedDict, total=False):
    mysqlIdentifier: MysqlObjectIdentifier
    oracleIdentifier: OracleObjectIdentifier

@typing.type_check_only
class StartBackfillJobResponse(typing.TypedDict, total=False):
    object: StreamObject

@typing.type_check_only
class StaticServiceIpConnectivity(typing.TypedDict, total=False): ...

@typing.type_check_only
class Status(typing.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class StopBackfillJobResponse(typing.TypedDict, total=False):
    object: StreamObject

@typing.type_check_only
class Stream(typing.TypedDict, total=False):
    backfillAll: BackfillAllStrategy
    backfillNone: BackfillNoneStrategy
    createTime: str
    customerManagedEncryptionKey: str
    destinationConfig: DestinationConfig
    displayName: str
    errors: _list[Error]
    labels: dict[str, typing.Any]
    name: str
    sourceConfig: SourceConfig
    state: typing.Literal[
        "STATE_UNSPECIFIED",
        "CREATED",
        "RUNNING",
        "PAUSED",
        "MAINTENANCE",
        "FAILED",
        "FAILED_PERMANENTLY",
        "STARTING",
        "DRAINING",
    ]
    updateTime: str

@typing.type_check_only
class StreamObject(typing.TypedDict, total=False):
    backfillJob: BackfillJob
    createTime: str
    displayName: str
    errors: _list[Error]
    name: str
    sourceObject: SourceObjectIdentifier
    updateTime: str

@typing.type_check_only
class Validation(typing.TypedDict, total=False):
    code: str
    description: str
    message: _list[ValidationMessage]
    status: typing.Literal["STATUS_UNSPECIFIED", "NOT_EXECUTED", "FAILED", "PASSED"]

@typing.type_check_only
class ValidationMessage(typing.TypedDict, total=False):
    code: str
    level: typing.Literal["LEVEL_UNSPECIFIED", "WARNING", "ERROR"]
    message: str
    metadata: dict[str, typing.Any]

@typing.type_check_only
class ValidationResult(typing.TypedDict, total=False):
    validations: _list[Validation]

@typing.type_check_only
class VpcPeeringConfig(typing.TypedDict, total=False):
    subnet: str
    vpcName: str
