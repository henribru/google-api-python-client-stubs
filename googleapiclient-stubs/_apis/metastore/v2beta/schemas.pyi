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
class GoogleCloudMetastoreV2betaAlterMetadataResourceLocationRequest(
    typing_extensions.TypedDict, total=False
):
    locationUri: str
    resourceName: str

@typing.type_check_only
class GoogleCloudMetastoreV2betaAlterTablePropertiesRequest(
    typing_extensions.TypedDict, total=False
):
    properties: dict[str, typing.Any]
    tableName: str
    updateMask: str

@typing.type_check_only
class GoogleCloudMetastoreV2betaAutoscalingConfig(
    typing_extensions.TypedDict, total=False
):
    autoscalingEnabled: bool
    autoscalingFactor: int
    limitConfig: GoogleCloudMetastoreV2betaLimitConfig

@typing.type_check_only
class GoogleCloudMetastoreV2betaAuxiliaryVersionConfig(
    typing_extensions.TypedDict, total=False
):
    configOverrides: dict[str, typing.Any]
    endpoints: _list[GoogleCloudMetastoreV2betaEndpoint]
    version: str

@typing.type_check_only
class GoogleCloudMetastoreV2betaBackup(typing_extensions.TypedDict, total=False):
    createTime: str
    description: str
    endTime: str
    name: str
    restoringServices: _list[str]
    serviceRevision: GoogleCloudMetastoreV2betaService
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "CREATING", "DELETING", "ACTIVE", "FAILED", "RESTORING"
    ]

@typing.type_check_only
class GoogleCloudMetastoreV2betaCancelMigrationRequest(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudMetastoreV2betaCdcConfig(typing_extensions.TypedDict, total=False):
    bucket: str
    password: str
    reverseProxySubnet: str
    rootPath: str
    subnetIpRange: str
    username: str
    vpcNetwork: str

@typing.type_check_only
class GoogleCloudMetastoreV2betaCloudSQLConnectionConfig(
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
class GoogleCloudMetastoreV2betaCloudSQLMigrationConfig(
    typing_extensions.TypedDict, total=False
):
    cdcConfig: GoogleCloudMetastoreV2betaCdcConfig
    cloudSqlConnectionConfig: GoogleCloudMetastoreV2betaCloudSQLConnectionConfig

@typing.type_check_only
class GoogleCloudMetastoreV2betaCompleteMigrationRequest(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudMetastoreV2betaDataCatalogConfig(
    typing_extensions.TypedDict, total=False
):
    enabled: bool

@typing.type_check_only
class GoogleCloudMetastoreV2betaDatabaseDump(typing_extensions.TypedDict, total=False):
    gcsUri: str
    type: typing_extensions.Literal["TYPE_UNSPECIFIED", "MYSQL", "AVRO"]

@typing.type_check_only
class GoogleCloudMetastoreV2betaEncryptionConfig(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudMetastoreV2betaEndpoint(typing_extensions.TypedDict, total=False):
    endpointUri: str
    region: str

@typing.type_check_only
class GoogleCloudMetastoreV2betaExportMetadataRequest(
    typing_extensions.TypedDict, total=False
):
    databaseDumpType: typing_extensions.Literal["TYPE_UNSPECIFIED", "MYSQL", "AVRO"]
    destinationGcsFolder: str
    requestId: str

@typing.type_check_only
class GoogleCloudMetastoreV2betaHiveMetastoreConfig(
    typing_extensions.TypedDict, total=False
):
    auxiliaryVersions: dict[str, typing.Any]
    configOverrides: dict[str, typing.Any]
    endpointProtocol: typing_extensions.Literal[
        "ENDPOINT_PROTOCOL_UNSPECIFIED", "THRIFT", "GRPC"
    ]
    version: str

@typing.type_check_only
class GoogleCloudMetastoreV2betaImportMetadataRequest(
    typing_extensions.TypedDict, total=False
):
    databaseDump: GoogleCloudMetastoreV2betaDatabaseDump
    description: str
    requestId: str

@typing.type_check_only
class GoogleCloudMetastoreV2betaLatestBackup(typing_extensions.TypedDict, total=False):
    backupId: str
    duration: str
    startTime: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "IN_PROGRESS", "SUCCEEDED", "FAILED"
    ]

@typing.type_check_only
class GoogleCloudMetastoreV2betaLimitConfig(typing_extensions.TypedDict, total=False):
    maxScalingFactor: int
    minScalingFactor: int

@typing.type_check_only
class GoogleCloudMetastoreV2betaListBackupsResponse(
    typing_extensions.TypedDict, total=False
):
    backups: _list[GoogleCloudMetastoreV2betaBackup]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class GoogleCloudMetastoreV2betaListMigrationExecutionsResponse(
    typing_extensions.TypedDict, total=False
):
    migrationExecutions: _list[GoogleCloudMetastoreV2betaMigrationExecution]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class GoogleCloudMetastoreV2betaListServicesResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    services: _list[GoogleCloudMetastoreV2betaService]
    unreachable: _list[str]

@typing.type_check_only
class GoogleCloudMetastoreV2betaMetadataIntegration(
    typing_extensions.TypedDict, total=False
):
    dataCatalogConfig: GoogleCloudMetastoreV2betaDataCatalogConfig

@typing.type_check_only
class GoogleCloudMetastoreV2betaMigrationExecution(
    typing_extensions.TypedDict, total=False
):
    cloudSqlMigrationConfig: GoogleCloudMetastoreV2betaCloudSQLMigrationConfig
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
class GoogleCloudMetastoreV2betaMoveTableToDatabaseRequest(
    typing_extensions.TypedDict, total=False
):
    dbName: str
    destinationDbName: str
    tableName: str

@typing.type_check_only
class GoogleCloudMetastoreV2betaQueryMetadataRequest(
    typing_extensions.TypedDict, total=False
):
    query: str

@typing.type_check_only
class GoogleCloudMetastoreV2betaRemoveIamPolicyRequest(
    typing_extensions.TypedDict, total=False
):
    asynchronous: bool

@typing.type_check_only
class GoogleCloudMetastoreV2betaRemoveIamPolicyResponse(
    typing_extensions.TypedDict, total=False
):
    success: bool

@typing.type_check_only
class GoogleCloudMetastoreV2betaRestoreServiceRequest(
    typing_extensions.TypedDict, total=False
):
    backup: str
    backupLocation: str
    requestId: str
    restoreType: typing_extensions.Literal[
        "RESTORE_TYPE_UNSPECIFIED", "FULL", "METADATA_ONLY"
    ]

@typing.type_check_only
class GoogleCloudMetastoreV2betaScalingConfig(typing_extensions.TypedDict, total=False):
    autoscalingConfig: GoogleCloudMetastoreV2betaAutoscalingConfig
    scalingFactor: int

@typing.type_check_only
class GoogleCloudMetastoreV2betaScheduledBackup(
    typing_extensions.TypedDict, total=False
):
    backupLocation: str
    cronSchedule: str
    enabled: bool
    latestBackup: GoogleCloudMetastoreV2betaLatestBackup
    nextScheduledTime: str
    timeZone: str

@typing.type_check_only
class GoogleCloudMetastoreV2betaService(typing_extensions.TypedDict, total=False):
    createTime: str
    encryptionConfig: GoogleCloudMetastoreV2betaEncryptionConfig
    endpoints: _list[GoogleCloudMetastoreV2betaEndpoint]
    hiveMetastoreConfig: GoogleCloudMetastoreV2betaHiveMetastoreConfig
    labels: dict[str, typing.Any]
    metadataIntegration: GoogleCloudMetastoreV2betaMetadataIntegration
    name: str
    scalingConfig: GoogleCloudMetastoreV2betaScalingConfig
    scheduledBackup: GoogleCloudMetastoreV2betaScheduledBackup
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
class GoogleCloudMetastoreV2betaStartMigrationRequest(
    typing_extensions.TypedDict, total=False
):
    migrationExecution: GoogleCloudMetastoreV2betaMigrationExecution
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
