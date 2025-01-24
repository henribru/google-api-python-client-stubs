import typing

import typing_extensions

_list = list

@typing.type_check_only
class GoogleCloudMetastoreV1AlterMetadataResourceLocationResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudMetastoreV1CustomRegionMetadata(
    typing_extensions.TypedDict, total=False
):
    optionalReadOnlyRegions: _list[str]
    requiredReadWriteRegions: _list[str]
    witnessRegion: str

@typing.type_check_only
class GoogleCloudMetastoreV1ErrorDetails(typing_extensions.TypedDict, total=False):
    details: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudMetastoreV1HiveMetastoreVersion(
    typing_extensions.TypedDict, total=False
):
    isDefault: bool
    version: str

@typing.type_check_only
class GoogleCloudMetastoreV1LocationMetadata(typing_extensions.TypedDict, total=False):
    customRegionMetadata: _list[GoogleCloudMetastoreV1CustomRegionMetadata]
    multiRegionMetadata: GoogleCloudMetastoreV1MultiRegionMetadata
    supportedHiveMetastoreVersions: _list[GoogleCloudMetastoreV1HiveMetastoreVersion]

@typing.type_check_only
class GoogleCloudMetastoreV1MoveTableToDatabaseResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudMetastoreV1MultiRegionMetadata(
    typing_extensions.TypedDict, total=False
):
    constituentRegions: _list[str]

@typing.type_check_only
class GoogleCloudMetastoreV1OperationMetadata(typing_extensions.TypedDict, total=False):
    apiVersion: str
    createTime: str
    endTime: str
    requestedCancellation: bool
    statusMessage: str
    target: str
    verb: str

@typing.type_check_only
class GoogleCloudMetastoreV1QueryMetadataResponse(
    typing_extensions.TypedDict, total=False
):
    resultManifestUri: str

@typing.type_check_only
class GoogleCloudMetastoreV1alphaAlterMetadataResourceLocationResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudMetastoreV1alphaCancelMigrationResponse(
    typing_extensions.TypedDict, total=False
):
    migrationExecution: str

@typing.type_check_only
class GoogleCloudMetastoreV1alphaCompleteMigrationResponse(
    typing_extensions.TypedDict, total=False
):
    migrationExecution: str

@typing.type_check_only
class GoogleCloudMetastoreV1alphaCustomRegionMetadata(
    typing_extensions.TypedDict, total=False
):
    optionalReadOnlyRegions: _list[str]
    requiredReadWriteRegions: _list[str]
    witnessRegion: str

@typing.type_check_only
class GoogleCloudMetastoreV1alphaErrorDetails(typing_extensions.TypedDict, total=False):
    details: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudMetastoreV1alphaHiveMetastoreVersion(
    typing_extensions.TypedDict, total=False
):
    isDefault: bool
    version: str

@typing.type_check_only
class GoogleCloudMetastoreV1alphaLocationMetadata(
    typing_extensions.TypedDict, total=False
):
    customRegionMetadata: _list[GoogleCloudMetastoreV1alphaCustomRegionMetadata]
    multiRegionMetadata: GoogleCloudMetastoreV1alphaMultiRegionMetadata
    supportedHiveMetastoreVersions: _list[
        GoogleCloudMetastoreV1alphaHiveMetastoreVersion
    ]

@typing.type_check_only
class GoogleCloudMetastoreV1alphaMoveTableToDatabaseResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudMetastoreV1alphaMultiRegionMetadata(
    typing_extensions.TypedDict, total=False
):
    constituentRegions: _list[str]

@typing.type_check_only
class GoogleCloudMetastoreV1alphaOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    apiVersion: str
    createTime: str
    endTime: str
    requestedCancellation: bool
    statusMessage: str
    target: str
    verb: str

@typing.type_check_only
class GoogleCloudMetastoreV1alphaQueryMetadataResponse(
    typing_extensions.TypedDict, total=False
):
    resultManifestUri: str

@typing.type_check_only
class GoogleCloudMetastoreV1betaAlterMetadataResourceLocationResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudMetastoreV1betaCancelMigrationResponse(
    typing_extensions.TypedDict, total=False
):
    migrationExecution: str

@typing.type_check_only
class GoogleCloudMetastoreV1betaCompleteMigrationResponse(
    typing_extensions.TypedDict, total=False
):
    migrationExecution: str

@typing.type_check_only
class GoogleCloudMetastoreV1betaCustomRegionMetadata(
    typing_extensions.TypedDict, total=False
):
    optionalReadOnlyRegions: _list[str]
    requiredReadWriteRegions: _list[str]
    witnessRegion: str

@typing.type_check_only
class GoogleCloudMetastoreV1betaErrorDetails(typing_extensions.TypedDict, total=False):
    details: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudMetastoreV1betaHiveMetastoreVersion(
    typing_extensions.TypedDict, total=False
):
    isDefault: bool
    version: str

@typing.type_check_only
class GoogleCloudMetastoreV1betaLocationMetadata(
    typing_extensions.TypedDict, total=False
):
    customRegionMetadata: _list[GoogleCloudMetastoreV1betaCustomRegionMetadata]
    multiRegionMetadata: GoogleCloudMetastoreV1betaMultiRegionMetadata
    supportedHiveMetastoreVersions: _list[
        GoogleCloudMetastoreV1betaHiveMetastoreVersion
    ]

@typing.type_check_only
class GoogleCloudMetastoreV1betaMoveTableToDatabaseResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudMetastoreV1betaMultiRegionMetadata(
    typing_extensions.TypedDict, total=False
):
    constituentRegions: _list[str]

@typing.type_check_only
class GoogleCloudMetastoreV1betaOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    apiVersion: str
    createTime: str
    endTime: str
    requestedCancellation: bool
    statusMessage: str
    target: str
    verb: str

@typing.type_check_only
class GoogleCloudMetastoreV1betaQueryMetadataResponse(
    typing_extensions.TypedDict, total=False
):
    resultManifestUri: str

@typing.type_check_only
class GoogleCloudMetastoreV2alphaAlterMetadataResourceLocationRequest(
    typing_extensions.TypedDict, total=False
):
    locationUri: str
    resourceName: str

@typing.type_check_only
class GoogleCloudMetastoreV2alphaAlterTablePropertiesRequest(
    typing_extensions.TypedDict, total=False
):
    properties: dict[str, typing.Any]
    tableName: str
    updateMask: str

@typing.type_check_only
class GoogleCloudMetastoreV2alphaAutoscalingConfig(
    typing_extensions.TypedDict, total=False
):
    autoscalingEnabled: bool
    autoscalingFactor: int
    limitConfig: GoogleCloudMetastoreV2alphaLimitConfig

@typing.type_check_only
class GoogleCloudMetastoreV2alphaAuxiliaryVersionConfig(
    typing_extensions.TypedDict, total=False
):
    configOverrides: dict[str, typing.Any]
    endpoints: _list[GoogleCloudMetastoreV2alphaEndpoint]
    version: str

@typing.type_check_only
class GoogleCloudMetastoreV2alphaBackup(typing_extensions.TypedDict, total=False):
    createTime: str
    description: str
    endTime: str
    name: str
    restoringServices: _list[str]
    serviceRevision: GoogleCloudMetastoreV2alphaService
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "CREATING", "DELETING", "ACTIVE", "FAILED", "RESTORING"
    ]

@typing.type_check_only
class GoogleCloudMetastoreV2alphaCancelMigrationRequest(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudMetastoreV2alphaCdcConfig(typing_extensions.TypedDict, total=False):
    bucket: str
    password: str
    reverseProxySubnet: str
    rootPath: str
    subnetIpRange: str
    username: str
    vpcNetwork: str

@typing.type_check_only
class GoogleCloudMetastoreV2alphaCloudSQLConnectionConfig(
    typing_extensions.TypedDict, total=False
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
class GoogleCloudMetastoreV2alphaCloudSQLMigrationConfig(
    typing_extensions.TypedDict, total=False
):
    cdcConfig: GoogleCloudMetastoreV2alphaCdcConfig
    cloudSqlConnectionConfig: GoogleCloudMetastoreV2alphaCloudSQLConnectionConfig

@typing.type_check_only
class GoogleCloudMetastoreV2alphaCompleteMigrationRequest(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudMetastoreV2alphaDataCatalogConfig(
    typing_extensions.TypedDict, total=False
):
    enabled: bool

@typing.type_check_only
class GoogleCloudMetastoreV2alphaDatabaseDump(typing_extensions.TypedDict, total=False):
    gcsUri: str
    type: typing_extensions.Literal["TYPE_UNSPECIFIED", "MYSQL", "AVRO"]

@typing.type_check_only
class GoogleCloudMetastoreV2alphaEncryptionConfig(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudMetastoreV2alphaEndpoint(typing_extensions.TypedDict, total=False):
    endpointUri: str
    region: str

@typing.type_check_only
class GoogleCloudMetastoreV2alphaExportMetadataRequest(
    typing_extensions.TypedDict, total=False
):
    databaseDumpType: typing_extensions.Literal["TYPE_UNSPECIFIED", "MYSQL", "AVRO"]
    destinationGcsFolder: str
    requestId: str

@typing.type_check_only
class GoogleCloudMetastoreV2alphaHiveMetastoreConfig(
    typing_extensions.TypedDict, total=False
):
    auxiliaryVersions: dict[str, typing.Any]
    configOverrides: dict[str, typing.Any]
    endpointProtocol: typing_extensions.Literal[
        "ENDPOINT_PROTOCOL_UNSPECIFIED", "THRIFT", "GRPC"
    ]
    version: str

@typing.type_check_only
class GoogleCloudMetastoreV2alphaImportMetadataRequest(
    typing_extensions.TypedDict, total=False
):
    databaseDump: GoogleCloudMetastoreV2alphaDatabaseDump
    description: str
    requestId: str

@typing.type_check_only
class GoogleCloudMetastoreV2alphaLatestBackup(typing_extensions.TypedDict, total=False):
    backupId: str
    duration: str
    startTime: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "IN_PROGRESS", "SUCCEEDED", "FAILED"
    ]

@typing.type_check_only
class GoogleCloudMetastoreV2alphaLimitConfig(typing_extensions.TypedDict, total=False):
    maxScalingFactor: int
    minScalingFactor: int

@typing.type_check_only
class GoogleCloudMetastoreV2alphaListBackupsResponse(
    typing_extensions.TypedDict, total=False
):
    backups: _list[GoogleCloudMetastoreV2alphaBackup]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class GoogleCloudMetastoreV2alphaListMigrationExecutionsResponse(
    typing_extensions.TypedDict, total=False
):
    migrationExecutions: _list[GoogleCloudMetastoreV2alphaMigrationExecution]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class GoogleCloudMetastoreV2alphaListServicesResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    services: _list[GoogleCloudMetastoreV2alphaService]
    unreachable: _list[str]

@typing.type_check_only
class GoogleCloudMetastoreV2alphaMetadataIntegration(
    typing_extensions.TypedDict, total=False
):
    dataCatalogConfig: GoogleCloudMetastoreV2alphaDataCatalogConfig

@typing.type_check_only
class GoogleCloudMetastoreV2alphaMigrationExecution(
    typing_extensions.TypedDict, total=False
):
    cloudSqlMigrationConfig: GoogleCloudMetastoreV2alphaCloudSQLMigrationConfig
    createTime: str
    endTime: str
    name: str
    phase: typing_extensions.Literal["PHASE_UNSPECIFIED", "REPLICATION", "CUTOVER"]
    state: typing_extensions.Literal[
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
    typing_extensions.TypedDict, total=False
):
    dbName: str
    destinationDbName: str
    tableName: str

@typing.type_check_only
class GoogleCloudMetastoreV2alphaQueryMetadataRequest(
    typing_extensions.TypedDict, total=False
):
    query: str

@typing.type_check_only
class GoogleCloudMetastoreV2alphaRemoveIamPolicyRequest(
    typing_extensions.TypedDict, total=False
):
    asynchronous: bool

@typing.type_check_only
class GoogleCloudMetastoreV2alphaRemoveIamPolicyResponse(
    typing_extensions.TypedDict, total=False
):
    success: bool

@typing.type_check_only
class GoogleCloudMetastoreV2alphaRestoreServiceRequest(
    typing_extensions.TypedDict, total=False
):
    backup: str
    backupLocation: str
    requestId: str
    restoreType: typing_extensions.Literal[
        "RESTORE_TYPE_UNSPECIFIED", "FULL", "METADATA_ONLY"
    ]

@typing.type_check_only
class GoogleCloudMetastoreV2alphaScalingConfig(
    typing_extensions.TypedDict, total=False
):
    autoscalingConfig: GoogleCloudMetastoreV2alphaAutoscalingConfig
    scalingFactor: int

@typing.type_check_only
class GoogleCloudMetastoreV2alphaScheduledBackup(
    typing_extensions.TypedDict, total=False
):
    backupLocation: str
    cronSchedule: str
    enabled: bool
    latestBackup: GoogleCloudMetastoreV2alphaLatestBackup
    nextScheduledTime: str
    timeZone: str

@typing.type_check_only
class GoogleCloudMetastoreV2alphaService(typing_extensions.TypedDict, total=False):
    createTime: str
    encryptionConfig: GoogleCloudMetastoreV2alphaEncryptionConfig
    endpoints: _list[GoogleCloudMetastoreV2alphaEndpoint]
    hiveMetastoreConfig: GoogleCloudMetastoreV2alphaHiveMetastoreConfig
    labels: dict[str, typing.Any]
    metadataIntegration: GoogleCloudMetastoreV2alphaMetadataIntegration
    name: str
    scalingConfig: GoogleCloudMetastoreV2alphaScalingConfig
    scheduledBackup: GoogleCloudMetastoreV2alphaScheduledBackup
    state: typing_extensions.Literal[
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
class GoogleCloudMetastoreV2alphaStartMigrationRequest(
    typing_extensions.TypedDict, total=False
):
    migrationExecution: GoogleCloudMetastoreV2alphaMigrationExecution
    requestId: str

@typing.type_check_only
class GoogleLongrunningOperation(typing_extensions.TypedDict, total=False):
    done: bool
    error: GoogleRpcStatus
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class GoogleRpcStatus(typing_extensions.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str
