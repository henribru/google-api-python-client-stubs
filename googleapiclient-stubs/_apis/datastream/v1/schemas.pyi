import typing

_list = list

@typing.type_check_only
class AppendOnly(typing.TypedDict, total=False): ...

@typing.type_check_only
class AvroFileFormat(typing.TypedDict, total=False): ...

@typing.type_check_only
class BackfillAllStrategy(typing.TypedDict, total=False):
    mongodbExcludedObjects: MongodbCluster
    mysqlExcludedObjects: MysqlRdbms
    oracleExcludedObjects: OracleRdbms
    postgresqlExcludedObjects: PostgresqlRdbms
    saasExcludedObjects: SourceCatalog
    salesforceExcludedObjects: SalesforceOrg
    spannerExcludedObjects: SpannerDatabase
    sqlServerExcludedObjects: SqlServerRdbms

@typing.type_check_only
class BackfillJob(typing.TypedDict, total=False):
    errors: _list[Error]
    eventFilter: EventFilter
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
class BasicEncryption(typing.TypedDict, total=False): ...

@typing.type_check_only
class BigQueryClustering(typing.TypedDict, total=False):
    columns: _list[str]

@typing.type_check_only
class BigQueryDestinationConfig(typing.TypedDict, total=False):
    appendOnly: AppendOnly
    blmtConfig: BlmtConfig
    dataFreshness: str
    merge: Merge
    singleTargetDataset: SingleTargetDataset
    sourceHierarchyDatasets: SourceHierarchyDatasets

@typing.type_check_only
class BigQueryPartitioning(typing.TypedDict, total=False):
    ingestionTimePartition: IngestionTimePartition
    integerRangePartition: IntegerRangePartition
    requirePartitionFilter: bool
    timeUnitPartition: TimeUnitPartition

@typing.type_check_only
class BigQueryProfile(typing.TypedDict, total=False): ...

@typing.type_check_only
class BinaryLogParser(typing.TypedDict, total=False):
    logFileDirectories: LogFileDirectories
    oracleAsmLogFileAccess: OracleAsmLogFileAccess

@typing.type_check_only
class BinaryLogPosition(typing.TypedDict, total=False): ...

@typing.type_check_only
class BlmtConfig(typing.TypedDict, total=False):
    bucket: str
    connectionName: str
    fileFormat: typing.Literal["FILE_FORMAT_UNSPECIFIED", "PARQUET"]
    rootPath: str
    tableFormat: typing.Literal["TABLE_FORMAT_UNSPECIFIED", "ICEBERG"]

@typing.type_check_only
class CancelOperationRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class CdcStrategy(typing.TypedDict, total=False):
    mostRecentStartPosition: MostRecentStartPosition
    nextAvailableStartPosition: NextAvailableStartPosition
    specificStartPosition: SpecificStartPosition

@typing.type_check_only
class ConnectionProfile(typing.TypedDict, total=False):
    bigqueryProfile: BigQueryProfile
    createTime: str
    dataverseProfile: DataverseProfile
    displayName: str
    forwardSshConnectivity: ForwardSshTunnelConnectivity
    gcsProfile: GcsProfile
    labels: dict[str, typing.Any]
    mongodbProfile: MongodbProfile
    mysqlProfile: MysqlProfile
    name: str
    oracleProfile: OracleProfile
    postgresqlProfile: PostgresqlProfile
    privateConnectivity: PrivateConnectivity
    salesforceMarketingCloudProfile: SalesforceMarketingCloudProfile
    salesforceProfile: SalesforceProfile
    satisfiesPzi: bool
    satisfiesPzs: bool
    serviceNowProfile: ServiceNowProfile
    spannerProfile: SpannerProfile
    sqlServerProfile: SqlServerProfile
    staticServiceIpConnectivity: StaticServiceIpConnectivity
    updateTime: str
    workdayProfile: WorkdayProfile

@typing.type_check_only
class CustomizationRule(typing.TypedDict, total=False):
    bigqueryClustering: BigQueryClustering
    bigqueryPartitioning: BigQueryPartitioning

@typing.type_check_only
class DatasetTemplate(typing.TypedDict, total=False):
    datasetIdPrefix: str
    kmsKeyName: str
    location: str

@typing.type_check_only
class DataverseProfile(typing.TypedDict, total=False):
    environmentUrl: str
    oauthClientCredentials: OauthClientCredentials
    tenantId: str

@typing.type_check_only
class DataverseSourceConfig(typing.TypedDict, total=False):
    excludeObjects: SourceCatalog
    includeObjects: SourceCatalog
    pollingInterval: str

@typing.type_check_only
class DebugInfo(typing.TypedDict, total=False):
    detail: str
    stackEntries: _list[str]

@typing.type_check_only
class DestinationConfig(typing.TypedDict, total=False):
    bigqueryDestinationConfig: BigQueryDestinationConfig
    destinationConnectionProfile: str
    gcsDestinationConfig: GcsDestinationConfig

@typing.type_check_only
class DiscoverConnectionProfileRequest(typing.TypedDict, total=False):
    connectionProfile: ConnectionProfile
    connectionProfileName: str
    fullHierarchy: bool
    hierarchyDepth: int
    mongodbCluster: MongodbCluster
    mysqlRdbms: MysqlRdbms
    oracleRdbms: OracleRdbms
    postgresqlRdbms: PostgresqlRdbms
    salesforceOrg: SalesforceOrg
    sourceCatalog: SourceCatalog
    spannerDatabase: SpannerDatabase
    sqlServerRdbms: SqlServerRdbms

@typing.type_check_only
class DiscoverConnectionProfileResponse(typing.TypedDict, total=False):
    mongodbCluster: MongodbCluster
    mysqlRdbms: MysqlRdbms
    oracleRdbms: OracleRdbms
    postgresqlRdbms: PostgresqlRdbms
    salesforceOrg: SalesforceOrg
    sourceCatalog: SourceCatalog
    spannerDatabase: SpannerDatabase
    sqlServerRdbms: SqlServerRdbms

@typing.type_check_only
class DropLargeObjects(typing.TypedDict, total=False): ...

@typing.type_check_only
class Empty(typing.TypedDict, total=False): ...

@typing.type_check_only
class EncryptionAndServerValidation(typing.TypedDict, total=False):
    caCertificate: str
    serverCertificateHostname: str

@typing.type_check_only
class EncryptionNotEnforced(typing.TypedDict, total=False): ...

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
class EventFilter(typing.TypedDict, total=False):
    sqlWhereClause: str

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
    jsonFileFormat: JsonFileFormat
    path: str

@typing.type_check_only
class GcsProfile(typing.TypedDict, total=False):
    bucket: str
    rootPath: str

@typing.type_check_only
class Gtid(typing.TypedDict, total=False): ...

@typing.type_check_only
class Help(typing.TypedDict, total=False):
    links: _list[Link]

@typing.type_check_only
class HostAddress(typing.TypedDict, total=False):
    hostname: str
    port: int

@typing.type_check_only
class IngestionTimePartition(typing.TypedDict, total=False):
    partitioningTimeGranularity: typing.Literal[
        "PARTITIONING_TIME_GRANULARITY_UNSPECIFIED",
        "PARTITIONING_TIME_GRANULARITY_HOUR",
        "PARTITIONING_TIME_GRANULARITY_DAY",
        "PARTITIONING_TIME_GRANULARITY_MONTH",
        "PARTITIONING_TIME_GRANULARITY_YEAR",
    ]

@typing.type_check_only
class IntegerRangePartition(typing.TypedDict, total=False):
    column: str
    end: str
    interval: str
    start: str

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
class LogFileDirectories(typing.TypedDict, total=False):
    archivedLogDirectory: str
    onlineLogDirectory: str

@typing.type_check_only
class LogMiner(typing.TypedDict, total=False): ...

@typing.type_check_only
class LookupStreamObjectRequest(typing.TypedDict, total=False):
    sourceObjectIdentifier: SourceObjectIdentifier

@typing.type_check_only
class Merge(typing.TypedDict, total=False): ...

@typing.type_check_only
class MongodbChangeStreamPosition(typing.TypedDict, total=False):
    startTime: str

@typing.type_check_only
class MongodbCluster(typing.TypedDict, total=False):
    databases: _list[MongodbDatabase]

@typing.type_check_only
class MongodbCollection(typing.TypedDict, total=False):
    collection: str
    fields: _list[MongodbField]

@typing.type_check_only
class MongodbDatabase(typing.TypedDict, total=False):
    collections: _list[MongodbCollection]
    database: str

@typing.type_check_only
class MongodbField(typing.TypedDict, total=False):
    field: str

@typing.type_check_only
class MongodbObjectIdentifier(typing.TypedDict, total=False):
    collection: str
    database: str

@typing.type_check_only
class MongodbProfile(typing.TypedDict, total=False):
    additionalOptions: dict[str, typing.Any]
    hostAddresses: _list[HostAddress]
    password: str
    replicaSet: str
    secretManagerStoredPassword: str
    srvConnectionFormat: SrvConnectionFormat
    sslConfig: MongodbSslConfig
    standardConnectionFormat: StandardConnectionFormat
    username: str

@typing.type_check_only
class MongodbSourceConfig(typing.TypedDict, total=False):
    excludeObjects: MongodbCluster
    includeObjects: MongodbCluster
    jsonMode: typing.Literal["MONGODB_JSON_MODE_UNSPECIFIED", "STRICT", "CANONICAL"]
    maxConcurrentBackfillTasks: int

@typing.type_check_only
class MongodbSslConfig(typing.TypedDict, total=False):
    caCertificate: str
    caCertificateSet: bool
    clientCertificate: str
    clientCertificateSet: bool
    clientKey: str
    clientKeySet: bool
    secretManagerStoredClientKey: str

@typing.type_check_only
class MostRecentStartPosition(typing.TypedDict, total=False): ...

@typing.type_check_only
class MysqlColumn(typing.TypedDict, total=False):
    collation: str
    column: str
    dataType: str
    length: int
    nullable: bool
    ordinalPosition: int
    precision: int
    primaryKey: bool
    scale: int

@typing.type_check_only
class MysqlDatabase(typing.TypedDict, total=False):
    database: str
    mysqlTables: _list[MysqlTable]

@typing.type_check_only
class MysqlGtidPosition(typing.TypedDict, total=False):
    gtidSet: str

@typing.type_check_only
class MysqlLogPosition(typing.TypedDict, total=False):
    logFile: str
    logPosition: int

@typing.type_check_only
class MysqlObjectIdentifier(typing.TypedDict, total=False):
    database: str
    table: str

@typing.type_check_only
class MysqlProfile(typing.TypedDict, total=False):
    hostname: str
    password: str
    port: int
    secretManagerStoredPassword: str
    sslConfig: MysqlSslConfig
    username: str

@typing.type_check_only
class MysqlRdbms(typing.TypedDict, total=False):
    mysqlDatabases: _list[MysqlDatabase]

@typing.type_check_only
class MysqlSourceConfig(typing.TypedDict, total=False):
    binaryLogPosition: BinaryLogPosition
    excludeObjects: MysqlRdbms
    gtid: Gtid
    includeObjects: MysqlRdbms
    maxConcurrentBackfillTasks: int
    maxConcurrentCdcTasks: int

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
    table: str

@typing.type_check_only
class NextAvailableStartPosition(typing.TypedDict, total=False): ...

@typing.type_check_only
class Oauth2ClientCredentials(typing.TypedDict, total=False):
    clientId: str
    clientSecret: str
    secretManagerStoredClientSecret: str

@typing.type_check_only
class OauthClientCredentials(typing.TypedDict, total=False):
    clientId: str
    clientSecret: Secret

@typing.type_check_only
class OauthRefreshTokenCredentials(typing.TypedDict, total=False):
    oauthClientCredentials: OauthClientCredentials
    refreshToken: Secret

@typing.type_check_only
class ObjectFilter(typing.TypedDict, total=False):
    sourceObjectIdentifier: SourceObjectIdentifier

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
class OracleAsmConfig(typing.TypedDict, total=False):
    asmService: str
    connectionAttributes: dict[str, typing.Any]
    hostname: str
    oracleSslConfig: OracleSslConfig
    password: str
    port: int
    secretManagerStoredPassword: str
    username: str

@typing.type_check_only
class OracleAsmLogFileAccess(typing.TypedDict, total=False): ...

@typing.type_check_only
class OracleColumn(typing.TypedDict, total=False):
    column: str
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
    oracleAsmConfig: OracleAsmConfig
    oracleSslConfig: OracleSslConfig
    password: str
    port: int
    secretManagerStoredPassword: str
    username: str

@typing.type_check_only
class OracleRdbms(typing.TypedDict, total=False):
    oracleSchemas: _list[OracleSchema]

@typing.type_check_only
class OracleSchema(typing.TypedDict, total=False):
    oracleTables: _list[OracleTable]
    schema: str

@typing.type_check_only
class OracleScnPosition(typing.TypedDict, total=False):
    scn: str

@typing.type_check_only
class OracleSourceConfig(typing.TypedDict, total=False):
    binaryLogParser: BinaryLogParser
    dropLargeObjects: DropLargeObjects
    excludeObjects: OracleRdbms
    includeObjects: OracleRdbms
    logMiner: LogMiner
    maxConcurrentBackfillTasks: int
    maxConcurrentCdcTasks: int
    streamLargeObjects: StreamLargeObjects

@typing.type_check_only
class OracleSslConfig(typing.TypedDict, total=False):
    caCertificate: str
    caCertificateSet: bool
    serverCertificateDistinguishedName: str

@typing.type_check_only
class OracleTable(typing.TypedDict, total=False):
    oracleColumns: _list[OracleColumn]
    table: str

@typing.type_check_only
class PostgresqlColumn(typing.TypedDict, total=False):
    column: str
    dataType: str
    length: int
    nullable: bool
    ordinalPosition: int
    precision: int
    primaryKey: bool
    scale: int

@typing.type_check_only
class PostgresqlObjectIdentifier(typing.TypedDict, total=False):
    schema: str
    table: str

@typing.type_check_only
class PostgresqlProfile(typing.TypedDict, total=False):
    database: str
    hostname: str
    password: str
    port: int
    secretManagerStoredPassword: str
    sslConfig: PostgresqlSslConfig
    username: str

@typing.type_check_only
class PostgresqlRdbms(typing.TypedDict, total=False):
    postgresqlSchemas: _list[PostgresqlSchema]

@typing.type_check_only
class PostgresqlSchema(typing.TypedDict, total=False):
    postgresqlTables: _list[PostgresqlTable]
    schema: str

@typing.type_check_only
class PostgresqlSourceConfig(typing.TypedDict, total=False):
    excludeObjects: PostgresqlRdbms
    includeObjects: PostgresqlRdbms
    maxConcurrentBackfillTasks: int
    publication: str
    replicationSlot: str

@typing.type_check_only
class PostgresqlSslConfig(typing.TypedDict, total=False):
    serverAndClientVerification: ServerAndClientVerification
    serverVerification: ServerVerification

@typing.type_check_only
class PostgresqlTable(typing.TypedDict, total=False):
    postgresqlColumns: _list[PostgresqlColumn]
    table: str

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
    pscInterfaceConfig: PscInterfaceConfig
    satisfiesPzi: bool
    satisfiesPzs: bool
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
    privateConnection: str

@typing.type_check_only
class PscInterfaceConfig(typing.TypedDict, total=False):
    networkAttachment: str

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
class RuleSet(typing.TypedDict, total=False):
    customizationRules: _list[CustomizationRule]
    objectFilter: ObjectFilter

@typing.type_check_only
class RunStreamRequest(typing.TypedDict, total=False):
    cdcStrategy: CdcStrategy
    force: bool

@typing.type_check_only
class SalesforceField(typing.TypedDict, total=False):
    dataType: str
    name: str
    nillable: bool

@typing.type_check_only
class SalesforceMarketingCloudProfile(typing.TypedDict, total=False):
    oauthClientCredentials: OauthClientCredentials
    subdomain: str

@typing.type_check_only
class SalesforceMarketingCloudSourceConfig(typing.TypedDict, total=False):
    excludeObjects: SourceCatalog
    fullRefreshPollingInterval: str
    includeObjects: SourceCatalog
    pollingInterval: str

@typing.type_check_only
class SalesforceObject(typing.TypedDict, total=False):
    fields: _list[SalesforceField]
    objectName: str

@typing.type_check_only
class SalesforceObjectIdentifier(typing.TypedDict, total=False):
    objectName: str

@typing.type_check_only
class SalesforceOrg(typing.TypedDict, total=False):
    objects: _list[SalesforceObject]

@typing.type_check_only
class SalesforceProfile(typing.TypedDict, total=False):
    domain: str
    oauth2ClientCredentials: Oauth2ClientCredentials
    userCredentials: UserCredentials

@typing.type_check_only
class SalesforceSourceConfig(typing.TypedDict, total=False):
    excludeObjects: SalesforceOrg
    includeObjects: SalesforceOrg
    pollingInterval: str

@typing.type_check_only
class Secret(typing.TypedDict, total=False):
    rawValue: str
    secretVersion: str

@typing.type_check_only
class ServerAndClientVerification(typing.TypedDict, total=False):
    caCertificate: str
    clientCertificate: str
    clientKey: str
    serverCertificateHostname: str

@typing.type_check_only
class ServerVerification(typing.TypedDict, total=False):
    caCertificate: str
    serverCertificateHostname: str

@typing.type_check_only
class ServiceNowProfile(typing.TypedDict, total=False):
    instance: str
    oauthClientCredentials: OauthClientCredentials
    userPasswordCredentials: UserPasswordCredentials

@typing.type_check_only
class ServiceNowSourceConfig(typing.TypedDict, total=False):
    excludeObjects: SourceCatalog
    includeObjects: SourceCatalog
    pollingInterval: str

@typing.type_check_only
class SingleTargetDataset(typing.TypedDict, total=False):
    datasetId: str

@typing.type_check_only
class SourceCatalog(typing.TypedDict, total=False):
    objects: _list[SourceObject]

@typing.type_check_only
class SourceConfig(typing.TypedDict, total=False):
    dataverseSourceConfig: DataverseSourceConfig
    mongodbSourceConfig: MongodbSourceConfig
    mysqlSourceConfig: MysqlSourceConfig
    oracleSourceConfig: OracleSourceConfig
    postgresqlSourceConfig: PostgresqlSourceConfig
    salesforceMarketingCloudSourceConfig: SalesforceMarketingCloudSourceConfig
    salesforceSourceConfig: SalesforceSourceConfig
    serviceNowSourceConfig: ServiceNowSourceConfig
    sourceConnectionProfile: str
    spannerSourceConfig: SpannerSourceConfig
    sqlServerSourceConfig: SqlServerSourceConfig
    workdaySourceConfig: WorkdaySourceConfig

@typing.type_check_only
class SourceHierarchyDatasets(typing.TypedDict, total=False):
    datasetTemplate: DatasetTemplate
    projectId: str

@typing.type_check_only
class SourceObject(typing.TypedDict, total=False):
    objectName: str
    properties: _list[SourceProperty]

@typing.type_check_only
class SourceObjectIdentifier(typing.TypedDict, total=False):
    mongodbIdentifier: MongodbObjectIdentifier
    mysqlIdentifier: MysqlObjectIdentifier
    oracleIdentifier: OracleObjectIdentifier
    postgresqlIdentifier: PostgresqlObjectIdentifier
    salesforceIdentifier: SalesforceObjectIdentifier
    spannerIdentifier: SpannerObjectIdentifier
    sqlServerIdentifier: SqlServerObjectIdentifier

@typing.type_check_only
class SourceProperty(typing.TypedDict, total=False):
    primaryKey: bool
    properties: _list[SourceProperty]
    propertyName: str

@typing.type_check_only
class SpannerChangeStreamPosition(typing.TypedDict, total=False):
    startTime: str

@typing.type_check_only
class SpannerColumn(typing.TypedDict, total=False):
    column: str
    dataType: str
    isPrimaryKey: bool
    ordinalPosition: str

@typing.type_check_only
class SpannerDatabase(typing.TypedDict, total=False):
    schemas: _list[SpannerSchema]

@typing.type_check_only
class SpannerObjectIdentifier(typing.TypedDict, total=False):
    schema: str
    table: str

@typing.type_check_only
class SpannerProfile(typing.TypedDict, total=False):
    database: str
    host: str

@typing.type_check_only
class SpannerSchema(typing.TypedDict, total=False):
    schema: str
    tables: _list[SpannerTable]

@typing.type_check_only
class SpannerSourceConfig(typing.TypedDict, total=False):
    backfillDataBoostEnabled: bool
    changeStreamName: str
    excludeObjects: SpannerDatabase
    fgacRole: str
    includeObjects: SpannerDatabase
    maxConcurrentBackfillTasks: int
    maxConcurrentCdcTasks: int
    spannerRpcPriority: typing.Literal[
        "SPANNER_RPC_PRIORITY_UNSPECIFIED", "LOW", "MEDIUM", "HIGH"
    ]

@typing.type_check_only
class SpannerTable(typing.TypedDict, total=False):
    columns: _list[SpannerColumn]
    table: str

@typing.type_check_only
class SpecificStartPosition(typing.TypedDict, total=False):
    mongodbChangeStreamPosition: MongodbChangeStreamPosition
    mysqlGtidPosition: MysqlGtidPosition
    mysqlLogPosition: MysqlLogPosition
    oracleScnPosition: OracleScnPosition
    spannerChangeStreamPosition: SpannerChangeStreamPosition
    sqlServerLsnPosition: SqlServerLsnPosition

@typing.type_check_only
class SqlServerChangeTables(typing.TypedDict, total=False): ...

@typing.type_check_only
class SqlServerColumn(typing.TypedDict, total=False):
    column: str
    dataType: str
    length: int
    nullable: bool
    ordinalPosition: int
    precision: int
    primaryKey: bool
    scale: int

@typing.type_check_only
class SqlServerLsnPosition(typing.TypedDict, total=False):
    lsn: str

@typing.type_check_only
class SqlServerObjectIdentifier(typing.TypedDict, total=False):
    schema: str
    table: str

@typing.type_check_only
class SqlServerProfile(typing.TypedDict, total=False):
    database: str
    hostname: str
    password: str
    port: int
    secretManagerStoredPassword: str
    sslConfig: SqlServerSslConfig
    username: str

@typing.type_check_only
class SqlServerRdbms(typing.TypedDict, total=False):
    schemas: _list[SqlServerSchema]

@typing.type_check_only
class SqlServerSchema(typing.TypedDict, total=False):
    schema: str
    tables: _list[SqlServerTable]

@typing.type_check_only
class SqlServerSourceConfig(typing.TypedDict, total=False):
    changeTables: SqlServerChangeTables
    excludeObjects: SqlServerRdbms
    includeObjects: SqlServerRdbms
    maxConcurrentBackfillTasks: int
    maxConcurrentCdcTasks: int
    transactionLogs: SqlServerTransactionLogs

@typing.type_check_only
class SqlServerSslConfig(typing.TypedDict, total=False):
    basicEncryption: BasicEncryption
    encryptionAndServerValidation: EncryptionAndServerValidation
    encryptionNotEnforced: EncryptionNotEnforced

@typing.type_check_only
class SqlServerTable(typing.TypedDict, total=False):
    columns: _list[SqlServerColumn]
    table: str

@typing.type_check_only
class SqlServerTransactionLogs(typing.TypedDict, total=False): ...

@typing.type_check_only
class SrvConnectionFormat(typing.TypedDict, total=False): ...

@typing.type_check_only
class StandardConnectionFormat(typing.TypedDict, total=False):
    directConnection: bool

@typing.type_check_only
class StartBackfillJobRequest(typing.TypedDict, total=False):
    eventFilter: EventFilter

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
class StopBackfillJobRequest(typing.TypedDict, total=False): ...

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
    lastRecoveryTime: str
    name: str
    ruleSets: _list[RuleSet]
    satisfiesPzi: bool
    satisfiesPzs: bool
    sourceConfig: SourceConfig
    state: typing.Literal[
        "STATE_UNSPECIFIED",
        "NOT_STARTED",
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
class StreamLargeObjects(typing.TypedDict, total=False): ...

@typing.type_check_only
class StreamObject(typing.TypedDict, total=False):
    backfillJob: BackfillJob
    createTime: str
    customizationRules: _list[CustomizationRule]
    displayName: str
    errors: _list[Error]
    name: str
    sourceObject: SourceObjectIdentifier
    updateTime: str

@typing.type_check_only
class TimeUnitPartition(typing.TypedDict, total=False):
    column: str
    partitioningTimeGranularity: typing.Literal[
        "PARTITIONING_TIME_GRANULARITY_UNSPECIFIED",
        "PARTITIONING_TIME_GRANULARITY_HOUR",
        "PARTITIONING_TIME_GRANULARITY_DAY",
        "PARTITIONING_TIME_GRANULARITY_MONTH",
        "PARTITIONING_TIME_GRANULARITY_YEAR",
    ]

@typing.type_check_only
class UserCredentials(typing.TypedDict, total=False):
    password: str
    secretManagerStoredPassword: str
    secretManagerStoredSecurityToken: str
    securityToken: str
    username: str

@typing.type_check_only
class UserPasswordCredentials(typing.TypedDict, total=False):
    password: Secret
    username: str

@typing.type_check_only
class Validation(typing.TypedDict, total=False):
    code: str
    description: str
    message: _list[ValidationMessage]
    state: typing.Literal[
        "STATE_UNSPECIFIED", "NOT_EXECUTED", "FAILED", "PASSED", "WARNING"
    ]

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
    vpc: str

@typing.type_check_only
class WorkdayProfile(typing.TypedDict, total=False):
    host: str
    oauthRefreshTokenCredentials: OauthRefreshTokenCredentials
    tenant: str

@typing.type_check_only
class WorkdaySourceConfig(typing.TypedDict, total=False):
    excludeObjects: SourceCatalog
    includeObjects: SourceCatalog
    pollingInterval: str
