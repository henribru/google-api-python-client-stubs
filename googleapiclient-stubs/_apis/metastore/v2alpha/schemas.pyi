import typing

_list = list

@typing.type_check_only
class GoogleCloudMetastoreV1AlterMetadataResourceLocationResponse(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudMetastoreV1CustomRegionMetadata(typing.TypedDict, total=False):
    optionalReadOnlyRegions: _list[str]
    requiredReadWriteRegions: _list[str]
    witnessRegion: str

@typing.type_check_only
class GoogleCloudMetastoreV1ErrorDetails(typing.TypedDict, total=False):
    details: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudMetastoreV1HiveMetastoreVersion(typing.TypedDict, total=False):
    isDefault: bool
    version: str

@typing.type_check_only
class GoogleCloudMetastoreV1LocationMetadata(typing.TypedDict, total=False):
    customRegionMetadata: _list[GoogleCloudMetastoreV1CustomRegionMetadata]
    multiRegionMetadata: GoogleCloudMetastoreV1MultiRegionMetadata
    supportedHiveMetastoreVersions: _list[GoogleCloudMetastoreV1HiveMetastoreVersion]

@typing.type_check_only
class GoogleCloudMetastoreV1MoveTableToDatabaseResponse(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudMetastoreV1MultiRegionMetadata(typing.TypedDict, total=False):
    constituentRegions: _list[str]
    continent: str
    witnessRegion: str

@typing.type_check_only
class GoogleCloudMetastoreV1OperationMetadata(typing.TypedDict, total=False):
    apiVersion: str
    createTime: str
    endTime: str
    requestedCancellation: bool
    statusMessage: str
    target: str
    verb: str

@typing.type_check_only
class GoogleCloudMetastoreV1QueryMetadataResponse(typing.TypedDict, total=False):
    resultManifestUri: str

@typing.type_check_only
class GoogleCloudMetastoreV1alphaAlterMetadataResourceLocationResponse(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudMetastoreV1alphaCancelMigrationResponse(typing.TypedDict, total=False):
    migrationExecution: str

@typing.type_check_only
class GoogleCloudMetastoreV1alphaCompleteMigrationResponse(
    typing.TypedDict, total=False
):
    migrationExecution: str

@typing.type_check_only
class GoogleCloudMetastoreV1alphaCustomRegionMetadata(typing.TypedDict, total=False):
    optionalReadOnlyRegions: _list[str]
    requiredReadWriteRegions: _list[str]
    witnessRegion: str

@typing.type_check_only
class GoogleCloudMetastoreV1alphaErrorDetails(typing.TypedDict, total=False):
    details: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudMetastoreV1alphaHiveMetastoreVersion(typing.TypedDict, total=False):
    isDefault: bool
    version: str

@typing.type_check_only
class GoogleCloudMetastoreV1alphaLocationMetadata(typing.TypedDict, total=False):
    customRegionMetadata: _list[GoogleCloudMetastoreV1alphaCustomRegionMetadata]
    multiRegionMetadata: GoogleCloudMetastoreV1alphaMultiRegionMetadata
    supportedHiveMetastoreVersions: _list[
        GoogleCloudMetastoreV1alphaHiveMetastoreVersion
    ]

@typing.type_check_only
class GoogleCloudMetastoreV1alphaMoveTableToDatabaseResponse(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudMetastoreV1alphaMultiRegionMetadata(typing.TypedDict, total=False):
    constituentRegions: _list[str]
    continent: str
    witnessRegion: str

@typing.type_check_only
class GoogleCloudMetastoreV1alphaOperationMetadata(typing.TypedDict, total=False):
    apiVersion: str
    createTime: str
    endTime: str
    requestedCancellation: bool
    statusMessage: str
    target: str
    verb: str

@typing.type_check_only
class GoogleCloudMetastoreV1alphaQueryMetadataResponse(typing.TypedDict, total=False):
    resultManifestUri: str

@typing.type_check_only
class GoogleCloudMetastoreV1betaAlterMetadataResourceLocationResponse(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudMetastoreV1betaCancelMigrationResponse(typing.TypedDict, total=False):
    migrationExecution: str

@typing.type_check_only
class GoogleCloudMetastoreV1betaCompleteMigrationResponse(
    typing.TypedDict, total=False
):
    migrationExecution: str

@typing.type_check_only
class GoogleCloudMetastoreV1betaCustomRegionMetadata(typing.TypedDict, total=False):
    optionalReadOnlyRegions: _list[str]
    requiredReadWriteRegions: _list[str]
    witnessRegion: str

@typing.type_check_only
class GoogleCloudMetastoreV1betaErrorDetails(typing.TypedDict, total=False):
    details: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudMetastoreV1betaHiveMetastoreVersion(typing.TypedDict, total=False):
    isDefault: bool
    version: str

@typing.type_check_only
class GoogleCloudMetastoreV1betaLocationMetadata(typing.TypedDict, total=False):
    customRegionMetadata: _list[GoogleCloudMetastoreV1betaCustomRegionMetadata]
    multiRegionMetadata: GoogleCloudMetastoreV1betaMultiRegionMetadata
    supportedHiveMetastoreVersions: _list[
        GoogleCloudMetastoreV1betaHiveMetastoreVersion
    ]

@typing.type_check_only
class GoogleCloudMetastoreV1betaMoveTableToDatabaseResponse(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudMetastoreV1betaMultiRegionMetadata(typing.TypedDict, total=False):
    constituentRegions: _list[str]
    continent: str
    witnessRegion: str

@typing.type_check_only
class GoogleCloudMetastoreV1betaOperationMetadata(typing.TypedDict, total=False):
    apiVersion: str
    createTime: str
    endTime: str
    requestedCancellation: bool
    statusMessage: str
    target: str
    verb: str

@typing.type_check_only
class GoogleCloudMetastoreV1betaQueryMetadataResponse(typing.TypedDict, total=False):
    resultManifestUri: str

@typing.type_check_only
class GoogleCloudMetastoreV2alphaAlterMetadataResourceLocationRequest(
    typing.TypedDict, total=False
):
    locationUri: str
    resourceName: str

@typing.type_check_only
class GoogleCloudMetastoreV2alphaAlterTablePropertiesRequest(
    typing.TypedDict, total=False
):
    properties: dict[str, typing.Any]
    tableName: str
    updateMask: str

@typing.type_check_only
class GoogleCloudMetastoreV2alphaAutoscalingConfig(typing.TypedDict, total=False):
    autoscalingEnabled: bool
    autoscalingFactor: int
    limitConfig: GoogleCloudMetastoreV2alphaLimitConfig

@typing.type_check_only
class GoogleCloudMetastoreV2alphaAuxiliaryVersionConfig(typing.TypedDict, total=False):
    configOverrides: dict[str, typing.Any]
    endpoints: _list[GoogleCloudMetastoreV2alphaEndpoint]
    version: str

@typing.type_check_only
class GoogleCloudMetastoreV2alphaBackup(typing.TypedDict, total=False):
    createTime: str
    description: str
    endTime: str
    name: str
    restoringServices: _list[str]
    serviceRevision: GoogleCloudMetastoreV2alphaService
    state: typing.Literal[
        "STATE_UNSPECIFIED", "CREATING", "DELETING", "ACTIVE", "FAILED", "RESTORING"
    ]

@typing.type_check_only
class GoogleCloudMetastoreV2alphaCancelMigrationRequest(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudMetastoreV2alphaCdcConfig(typing.TypedDict, total=False):
    bucket: str
    password: str
    reverseProxySubnet: str
    rootPath: str
    subnetIpRange: str
    username: str
    vpcNetwork: str

@typing.type_check_only
class GoogleCloudMetastoreV2alphaCloudSQLConnectionConfig(
    typing.TypedDict, total=False
):
    hiveDatabaseName: str
    instanceConnectionName: str
    ipAddress: str
    natSubnet: str
    password: str
    port: int
    proxySubnet: str
    username: str

@typing.type_check_only
class GoogleCloudMetastoreV2alphaCloudSQLMigrationConfig(typing.TypedDict, total=False):
    cdcConfig: GoogleCloudMetastoreV2alphaCdcConfig
    cloudSqlConnectionConfig: GoogleCloudMetastoreV2alphaCloudSQLConnectionConfig

@typing.type_check_only
class GoogleCloudMetastoreV2alphaCompleteMigrationRequest(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudMetastoreV2alphaDataCatalogConfig(typing.TypedDict, total=False):
    enabled: bool

@typing.type_check_only
class GoogleCloudMetastoreV2alphaDatabaseDump(typing.TypedDict, total=False):
    gcsUri: str
    type: typing.Literal["TYPE_UNSPECIFIED", "MYSQL", "AVRO"]

@typing.type_check_only
class GoogleCloudMetastoreV2alphaEncryptionConfig(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleCloudMetastoreV2alphaEndpoint(typing.TypedDict, total=False):
    endpointUri: str
    region: str

@typing.type_check_only
class GoogleCloudMetastoreV2alphaExportMetadataRequest(typing.TypedDict, total=False):
    databaseDumpType: typing.Literal["TYPE_UNSPECIFIED", "MYSQL", "AVRO"]
    destinationGcsFolder: str
    requestId: str

@typing.type_check_only
class GoogleCloudMetastoreV2alphaHiveMetastoreConfig(typing.TypedDict, total=False):
    auxiliaryVersions: dict[str, typing.Any]
    configOverrides: dict[str, typing.Any]
    endpointProtocol: typing.Literal["ENDPOINT_PROTOCOL_UNSPECIFIED", "THRIFT", "GRPC"]
    version: str

@typing.type_check_only
class GoogleCloudMetastoreV2alphaImportMetadataRequest(typing.TypedDict, total=False):
    databaseDump: GoogleCloudMetastoreV2alphaDatabaseDump
    description: str
    requestId: str

@typing.type_check_only
class GoogleCloudMetastoreV2alphaLatestBackup(typing.TypedDict, total=False):
    backupId: str
    duration: str
    startTime: str
    state: typing.Literal["STATE_UNSPECIFIED", "IN_PROGRESS", "SUCCEEDED", "FAILED"]

@typing.type_check_only
class GoogleCloudMetastoreV2alphaLimitConfig(typing.TypedDict, total=False):
    maxScalingFactor: int
    minScalingFactor: int

@typing.type_check_only
class GoogleCloudMetastoreV2alphaListBackupsResponse(typing.TypedDict, total=False):
    backups: _list[GoogleCloudMetastoreV2alphaBackup]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class GoogleCloudMetastoreV2alphaListMigrationExecutionsResponse(
    typing.TypedDict, total=False
):
    migrationExecutions: _list[GoogleCloudMetastoreV2alphaMigrationExecution]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class GoogleCloudMetastoreV2alphaListServicesResponse(typing.TypedDict, total=False):
    nextPageToken: str
    services: _list[GoogleCloudMetastoreV2alphaService]
    unreachable: _list[str]

@typing.type_check_only
class GoogleCloudMetastoreV2alphaMetadataIntegration(typing.TypedDict, total=False):
    dataCatalogConfig: GoogleCloudMetastoreV2alphaDataCatalogConfig

@typing.type_check_only
class GoogleCloudMetastoreV2alphaMigrationExecution(typing.TypedDict, total=False):
    cloudSqlMigrationConfig: GoogleCloudMetastoreV2alphaCloudSQLMigrationConfig
    createTime: str
    endTime: str
    name: str
    phase: typing.Literal["PHASE_UNSPECIFIED", "REPLICATION", "CUTOVER"]
    state: typing.Literal[
        "STATE_UNSPECIFIED",
        "STARTING",
        "RUNNING",
        "CANCELLING",
        "AWAITING_USER_ACTION",
        "SUCCEEDED",
        "FAILED",
        "CANCELLED",
        "DELETING",
    ]
    stateMessage: str

@typing.type_check_only
class GoogleCloudMetastoreV2alphaMoveTableToDatabaseRequest(
    typing.TypedDict, total=False
):
    dbName: str
    destinationDbName: str
    tableName: str

@typing.type_check_only
class GoogleCloudMetastoreV2alphaQueryMetadataRequest(typing.TypedDict, total=False):
    query: str

@typing.type_check_only
class GoogleCloudMetastoreV2alphaRemoveIamPolicyRequest(typing.TypedDict, total=False):
    asynchronous: bool

@typing.type_check_only
class GoogleCloudMetastoreV2alphaRemoveIamPolicyResponse(typing.TypedDict, total=False):
    success: bool

@typing.type_check_only
class GoogleCloudMetastoreV2alphaRestoreServiceRequest(typing.TypedDict, total=False):
    backup: str
    backupLocation: str
    requestId: str
    restoreType: typing.Literal["RESTORE_TYPE_UNSPECIFIED", "FULL", "METADATA_ONLY"]

@typing.type_check_only
class GoogleCloudMetastoreV2alphaScalingConfig(typing.TypedDict, total=False):
    autoscalingConfig: GoogleCloudMetastoreV2alphaAutoscalingConfig
    scalingFactor: int

@typing.type_check_only
class GoogleCloudMetastoreV2alphaScheduledBackup(typing.TypedDict, total=False):
    backupLocation: str
    cronSchedule: str
    enabled: bool
    latestBackup: GoogleCloudMetastoreV2alphaLatestBackup
    nextScheduledTime: str
    timeZone: str

@typing.type_check_only
class GoogleCloudMetastoreV2alphaService(typing.TypedDict, total=False):
    createTime: str
    encryptionConfig: GoogleCloudMetastoreV2alphaEncryptionConfig
    endpoints: _list[GoogleCloudMetastoreV2alphaEndpoint]
    hiveMetastoreConfig: GoogleCloudMetastoreV2alphaHiveMetastoreConfig
    labels: dict[str, typing.Any]
    metadataIntegration: GoogleCloudMetastoreV2alphaMetadataIntegration
    name: str
    scalingConfig: GoogleCloudMetastoreV2alphaScalingConfig
    scheduledBackup: GoogleCloudMetastoreV2alphaScheduledBackup
    state: typing.Literal[
        "STATE_UNSPECIFIED",
        "CREATING",
        "ACTIVE",
        "SUSPENDING",
        "SUSPENDED",
        "UPDATING",
        "DELETING",
        "ERROR",
        "MIGRATING",
    ]
    stateMessage: str
    uid: str
    updateTime: str
    warehouseGcsUri: str

@typing.type_check_only
class GoogleCloudMetastoreV2alphaStartMigrationRequest(typing.TypedDict, total=False):
    migrationExecution: GoogleCloudMetastoreV2alphaMigrationExecution
    requestId: str

@typing.type_check_only
class GoogleLongrunningOperation(typing.TypedDict, total=False):
    done: bool
    error: GoogleRpcStatus
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class GoogleRpcStatus(typing.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str
