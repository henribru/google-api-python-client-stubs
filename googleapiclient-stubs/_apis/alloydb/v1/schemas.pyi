import typing

import typing_extensions

_list = list

@typing.type_check_only
class AutomatedBackupPolicy(typing_extensions.TypedDict, total=False):
    backupWindow: str
    enabled: bool
    encryptionConfig: EncryptionConfig
    labels: dict[str, typing.Any]
    location: str
    quantityBasedRetention: QuantityBasedRetention
    timeBasedRetention: TimeBasedRetention
    weeklySchedule: WeeklySchedule

@typing.type_check_only
class Backup(typing_extensions.TypedDict, total=False):
    annotations: dict[str, typing.Any]
    clusterName: str
    clusterUid: str
    createTime: str
    databaseVersion: typing_extensions.Literal[
        "DATABASE_VERSION_UNSPECIFIED", "POSTGRES_13", "POSTGRES_14"
    ]
    deleteTime: str
    description: str
    displayName: str
    encryptionConfig: EncryptionConfig
    encryptionInfo: EncryptionInfo
    etag: str
    expiryQuantity: QuantityBasedExpiry
    expiryTime: str
    labels: dict[str, typing.Any]
    name: str
    reconciling: bool
    sizeBytes: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "READY", "CREATING", "FAILED", "DELETING"
    ]
    type: typing_extensions.Literal[
        "TYPE_UNSPECIFIED", "ON_DEMAND", "AUTOMATED", "CONTINUOUS"
    ]
    uid: str
    updateTime: str

@typing.type_check_only
class BackupSource(typing_extensions.TypedDict, total=False):
    backupName: str
    backupUid: str

@typing.type_check_only
class CancelOperationRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class ClientConnectionConfig(typing_extensions.TypedDict, total=False):
    requireConnectors: bool
    sslConfig: SslConfig

@typing.type_check_only
class CloudControl2SharedOperationsReconciliationOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    deleteResource: bool
    exclusiveAction: typing_extensions.Literal[
        "UNKNOWN_REPAIR_ACTION", "DELETE", "RETRY"
    ]

@typing.type_check_only
class Cluster(typing_extensions.TypedDict, total=False):
    annotations: dict[str, typing.Any]
    automatedBackupPolicy: AutomatedBackupPolicy
    backupSource: BackupSource
    clusterType: typing_extensions.Literal[
        "CLUSTER_TYPE_UNSPECIFIED", "PRIMARY", "SECONDARY"
    ]
    continuousBackupConfig: ContinuousBackupConfig
    continuousBackupInfo: ContinuousBackupInfo
    createTime: str
    databaseVersion: typing_extensions.Literal[
        "DATABASE_VERSION_UNSPECIFIED", "POSTGRES_13", "POSTGRES_14"
    ]
    deleteTime: str
    displayName: str
    encryptionConfig: EncryptionConfig
    encryptionInfo: EncryptionInfo
    etag: str
    initialUser: UserPassword
    labels: dict[str, typing.Any]
    migrationSource: MigrationSource
    name: str
    network: str
    networkConfig: NetworkConfig
    primaryConfig: PrimaryConfig
    reconciling: bool
    secondaryConfig: SecondaryConfig
    sslConfig: SslConfig
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "READY",
        "STOPPED",
        "EMPTY",
        "CREATING",
        "DELETING",
        "FAILED",
        "BOOTSTRAPPING",
        "MAINTENANCE",
        "PROMOTING",
    ]
    uid: str
    updateTime: str

@typing.type_check_only
class ConnectionInfo(typing_extensions.TypedDict, total=False):
    instanceUid: str
    ipAddress: str
    name: str

@typing.type_check_only
class ContinuousBackupConfig(typing_extensions.TypedDict, total=False):
    enabled: bool
    encryptionConfig: EncryptionConfig
    recoveryWindowDays: int

@typing.type_check_only
class ContinuousBackupInfo(typing_extensions.TypedDict, total=False):
    earliestRestorableTime: str
    enabledTime: str
    encryptionInfo: EncryptionInfo
    schedule: _list[str]

@typing.type_check_only
class ContinuousBackupSource(typing_extensions.TypedDict, total=False):
    cluster: str
    pointInTime: str

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class EncryptionConfig(typing_extensions.TypedDict, total=False):
    kmsKeyName: str

@typing.type_check_only
class EncryptionInfo(typing_extensions.TypedDict, total=False):
    encryptionType: typing_extensions.Literal[
        "TYPE_UNSPECIFIED", "GOOGLE_DEFAULT_ENCRYPTION", "CUSTOMER_MANAGED_ENCRYPTION"
    ]
    kmsKeyVersions: _list[str]

@typing.type_check_only
class FailoverInstanceRequest(typing_extensions.TypedDict, total=False):
    requestId: str
    validateOnly: bool

@typing.type_check_only
class GenerateClientCertificateRequest(typing_extensions.TypedDict, total=False):
    certDuration: str
    publicKey: str
    requestId: str

@typing.type_check_only
class GenerateClientCertificateResponse(typing_extensions.TypedDict, total=False):
    caCert: str
    pemCertificateChain: _list[str]

@typing.type_check_only
class GoogleCloudLocationListLocationsResponse(
    typing_extensions.TypedDict, total=False
):
    locations: _list[GoogleCloudLocationLocation]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudLocationLocation(typing_extensions.TypedDict, total=False):
    displayName: str
    labels: dict[str, typing.Any]
    locationId: str
    metadata: dict[str, typing.Any]
    name: str

@typing.type_check_only
class GoogleTypeTimeOfDay(typing_extensions.TypedDict, total=False):
    hours: int
    minutes: int
    nanos: int
    seconds: int

@typing.type_check_only
class InjectFaultRequest(typing_extensions.TypedDict, total=False):
    faultType: typing_extensions.Literal["FAULT_TYPE_UNSPECIFIED", "STOP_VM"]
    requestId: str
    validateOnly: bool

@typing.type_check_only
class Instance(typing_extensions.TypedDict, total=False):
    annotations: dict[str, typing.Any]
    availabilityType: typing_extensions.Literal[
        "AVAILABILITY_TYPE_UNSPECIFIED", "ZONAL", "REGIONAL"
    ]
    clientConnectionConfig: ClientConnectionConfig
    createTime: str
    databaseFlags: dict[str, typing.Any]
    deleteTime: str
    displayName: str
    etag: str
    gceZone: str
    instanceType: typing_extensions.Literal[
        "INSTANCE_TYPE_UNSPECIFIED", "PRIMARY", "READ_POOL", "SECONDARY"
    ]
    ipAddress: str
    labels: dict[str, typing.Any]
    machineConfig: MachineConfig
    name: str
    nodes: _list[Node]
    queryInsightsConfig: QueryInsightsInstanceConfig
    readPoolConfig: ReadPoolConfig
    reconciling: bool
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "READY",
        "STOPPED",
        "CREATING",
        "DELETING",
        "MAINTENANCE",
        "FAILED",
        "BOOTSTRAPPING",
        "PROMOTING",
    ]
    uid: str
    updateTime: str
    writableNode: Node

@typing.type_check_only
class IntegerRestrictions(typing_extensions.TypedDict, total=False):
    maxValue: str
    minValue: str

@typing.type_check_only
class ListBackupsResponse(typing_extensions.TypedDict, total=False):
    backups: _list[Backup]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListClustersResponse(typing_extensions.TypedDict, total=False):
    clusters: _list[Cluster]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListInstancesResponse(typing_extensions.TypedDict, total=False):
    instances: _list[Instance]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListOperationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    operations: _list[Operation]

@typing.type_check_only
class ListSupportedDatabaseFlagsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    supportedDatabaseFlags: _list[SupportedDatabaseFlag]

@typing.type_check_only
class ListUsersResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    unreachable: _list[str]
    users: _list[User]

@typing.type_check_only
class MachineConfig(typing_extensions.TypedDict, total=False):
    cpuCount: int

@typing.type_check_only
class MigrationSource(typing_extensions.TypedDict, total=False):
    hostPort: str
    referenceId: str
    sourceType: typing_extensions.Literal["MIGRATION_SOURCE_TYPE_UNSPECIFIED", "DMS"]

@typing.type_check_only
class NetworkConfig(typing_extensions.TypedDict, total=False):
    allocatedIpRange: str
    network: str

@typing.type_check_only
class Node(typing_extensions.TypedDict, total=False):
    id: str
    ip: str
    state: str
    zoneId: str

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
class PrimaryConfig(typing_extensions.TypedDict, total=False):
    secondaryClusterNames: _list[str]

@typing.type_check_only
class PromoteClusterRequest(typing_extensions.TypedDict, total=False):
    etag: str
    requestId: str
    validateOnly: bool

@typing.type_check_only
class QuantityBasedExpiry(typing_extensions.TypedDict, total=False):
    retentionCount: int
    totalRetentionCount: int

@typing.type_check_only
class QuantityBasedRetention(typing_extensions.TypedDict, total=False):
    count: int

@typing.type_check_only
class QueryInsightsInstanceConfig(typing_extensions.TypedDict, total=False):
    queryPlansPerMinute: int
    queryStringLength: int
    recordApplicationTags: bool
    recordClientAddress: bool

@typing.type_check_only
class ReadPoolConfig(typing_extensions.TypedDict, total=False):
    nodeCount: int

@typing.type_check_only
class RestartInstanceRequest(typing_extensions.TypedDict, total=False):
    requestId: str
    validateOnly: bool

@typing.type_check_only
class RestoreClusterRequest(typing_extensions.TypedDict, total=False):
    backupSource: BackupSource
    cluster: Cluster
    clusterId: str
    continuousBackupSource: ContinuousBackupSource
    requestId: str
    validateOnly: bool

@typing.type_check_only
class SecondaryConfig(typing_extensions.TypedDict, total=False):
    primaryClusterName: str

@typing.type_check_only
class SslConfig(typing_extensions.TypedDict, total=False):
    caSource: typing_extensions.Literal["CA_SOURCE_UNSPECIFIED", "CA_SOURCE_MANAGED"]
    sslMode: typing_extensions.Literal[
        "SSL_MODE_UNSPECIFIED",
        "SSL_MODE_ALLOW",
        "SSL_MODE_REQUIRE",
        "SSL_MODE_VERIFY_CA",
        "ALLOW_UNENCRYPTED_AND_ENCRYPTED",
        "ENCRYPTED_ONLY",
    ]

@typing.type_check_only
class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class StorageDatabasecenterPartnerapiV1mainAvailabilityConfiguration(
    typing_extensions.TypedDict, total=False
):
    availabilityType: typing_extensions.Literal[
        "AVAILABILITY_TYPE_UNSPECIFIED",
        "ZONAL",
        "REGIONAL",
        "MULTI_REGIONAL",
        "AVAILABILITY_TYPE_OTHER",
    ]
    externalReplicaConfigured: bool
    promotableReplicaConfigured: bool

@typing.type_check_only
class StorageDatabasecenterPartnerapiV1mainBackupConfiguration(
    typing_extensions.TypedDict, total=False
):
    automatedBackupEnabled: bool
    backupRetentionSettings: StorageDatabasecenterPartnerapiV1mainRetentionSettings
    pointInTimeRecoveryEnabled: bool

@typing.type_check_only
class StorageDatabasecenterPartnerapiV1mainBackupRun(
    typing_extensions.TypedDict, total=False
):
    endTime: str
    error: StorageDatabasecenterPartnerapiV1mainOperationError
    startTime: str
    status: typing_extensions.Literal["STATUS_UNSPECIFIED", "SUCCESSFUL", "FAILED"]

@typing.type_check_only
class StorageDatabasecenterPartnerapiV1mainCompliance(
    typing_extensions.TypedDict, total=False
):
    standard: str
    version: str

@typing.type_check_only
class StorageDatabasecenterPartnerapiV1mainDatabaseResourceFeed(
    typing_extensions.TypedDict, total=False
):
    feedTimestamp: str
    feedType: typing_extensions.Literal[
        "FEEDTYPE_UNSPECIFIED",
        "RESOURCE_METADATA",
        "OBSERVABILITY_DATA",
        "SECURITY_FINDING_DATA",
    ]
    resourceHealthSignalData: StorageDatabasecenterPartnerapiV1mainDatabaseResourceHealthSignalData
    resourceId: StorageDatabasecenterPartnerapiV1mainDatabaseResourceId
    resourceMetadata: StorageDatabasecenterPartnerapiV1mainDatabaseResourceMetadata

@typing.type_check_only
class StorageDatabasecenterPartnerapiV1mainDatabaseResourceHealthSignalData(
    typing_extensions.TypedDict, total=False
):
    additionalMetadata: dict[str, typing.Any]
    compliance: _list[StorageDatabasecenterPartnerapiV1mainCompliance]
    description: str
    eventTime: str
    externalUri: str
    name: str
    provider: typing_extensions.Literal[
        "PROVIDER_UNSPECIFIED",
        "GCP",
        "AWS",
        "AZURE",
        "ONPREM",
        "SELFMANAGED",
        "PROVIDER_OTHER",
    ]
    resourceContainer: str
    resourceName: str
    signalClass: typing_extensions.Literal[
        "CLASS_UNSPECIFIED",
        "THREAT",
        "VULNERABILITY",
        "MISCONFIGURATION",
        "OBSERVATION",
        "ERROR",
    ]
    signalId: str
    state: typing_extensions.Literal["STATE_UNSPECIFIED", "ACTIVE", "RESOLVED", "MUTED"]

@typing.type_check_only
class StorageDatabasecenterPartnerapiV1mainDatabaseResourceId(
    typing_extensions.TypedDict, total=False
):
    provider: typing_extensions.Literal[
        "PROVIDER_UNSPECIFIED",
        "GCP",
        "AWS",
        "AZURE",
        "ONPREM",
        "SELFMANAGED",
        "PROVIDER_OTHER",
    ]
    providerDescription: str
    resourceType: str
    uniqueId: str

@typing.type_check_only
class StorageDatabasecenterPartnerapiV1mainDatabaseResourceMetadata(
    typing_extensions.TypedDict, total=False
):
    availabilityConfiguration: StorageDatabasecenterPartnerapiV1mainAvailabilityConfiguration
    backupConfiguration: StorageDatabasecenterPartnerapiV1mainBackupConfiguration
    backupRun: StorageDatabasecenterPartnerapiV1mainBackupRun
    creationTime: str
    currentState: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "HEALTHY",
        "UNHEALTHY",
        "SUSPENDED",
        "DELETED",
        "STATE_OTHER",
    ]
    customMetadata: dict[str, typing.Any]
    expectedState: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "HEALTHY",
        "UNHEALTHY",
        "SUSPENDED",
        "DELETED",
        "STATE_OTHER",
    ]
    id: StorageDatabasecenterPartnerapiV1mainDatabaseResourceId
    instanceType: typing_extensions.Literal[
        "INSTANCE_TYPE_UNSPECIFIED", "PRIMARY", "READ_REPLICA", "OTHER"
    ]
    location: str
    primaryResourceId: StorageDatabasecenterPartnerapiV1mainDatabaseResourceId
    product: StorageDatabasecenterProtoCommonProduct
    resourceContainer: str
    resourceName: str
    updationTime: str
    userLabels: dict[str, typing.Any]

@typing.type_check_only
class StorageDatabasecenterPartnerapiV1mainOperationError(
    typing_extensions.TypedDict, total=False
):
    code: str
    message: str

@typing.type_check_only
class StorageDatabasecenterPartnerapiV1mainRetentionSettings(
    typing_extensions.TypedDict, total=False
):
    quantityBasedRetention: int
    retentionUnit: typing_extensions.Literal[
        "RETENTION_UNIT_UNSPECIFIED", "COUNT", "TIME", "RETENTION_UNIT_OTHER"
    ]
    timeBasedRetention: str

@typing.type_check_only
class StorageDatabasecenterProtoCommonProduct(typing_extensions.TypedDict, total=False):
    engine: typing_extensions.Literal[
        "ENGINE_UNSPECIFIED",
        "MYSQL",
        "POSTGRES",
        "SQL_SERVER",
        "NATIVE",
        "SPANGRES",
        "ENGINE_OTHER",
    ]
    type: typing_extensions.Literal[
        "PRODUCT_TYPE_UNSPECIFIED",
        "CLOUD_SQL",
        "ALLOYDB",
        "SPANNER",
        "ON_PREM",
        "PRODUCT_TYPE_OTHER",
    ]
    version: str

@typing.type_check_only
class StringRestrictions(typing_extensions.TypedDict, total=False):
    allowedValues: _list[str]

@typing.type_check_only
class SupportedDatabaseFlag(typing_extensions.TypedDict, total=False):
    acceptsMultipleValues: bool
    flagName: str
    integerRestrictions: IntegerRestrictions
    name: str
    requiresDbRestart: bool
    stringRestrictions: StringRestrictions
    supportedDbVersions: _list[str]
    valueType: typing_extensions.Literal[
        "VALUE_TYPE_UNSPECIFIED", "STRING", "INTEGER", "FLOAT", "NONE"
    ]

@typing.type_check_only
class TimeBasedRetention(typing_extensions.TypedDict, total=False):
    retentionPeriod: str

@typing.type_check_only
class User(typing_extensions.TypedDict, total=False):
    databaseRoles: _list[str]
    name: str
    password: str
    userType: typing_extensions.Literal[
        "USER_TYPE_UNSPECIFIED", "ALLOYDB_BUILT_IN", "ALLOYDB_IAM_USER"
    ]

@typing.type_check_only
class UserPassword(typing_extensions.TypedDict, total=False):
    password: str
    user: str

@typing.type_check_only
class WeeklySchedule(typing_extensions.TypedDict, total=False):
    daysOfWeek: _list[str]
    startTimes: _list[GoogleTypeTimeOfDay]
