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
class GoogleCloudMetastoreV2AlterMetadataResourceLocationRequest(
    typing_extensions.TypedDict, total=False
):
    locationUri: str
    resourceName: str

@typing.type_check_only
class GoogleCloudMetastoreV2AlterTablePropertiesRequest(
    typing_extensions.TypedDict, total=False
):
    properties: dict[str, typing.Any]
    tableName: str
    updateMask: str

@typing.type_check_only
class GoogleCloudMetastoreV2AuxiliaryVersionConfig(
    typing_extensions.TypedDict, total=False
):
    configOverrides: dict[str, typing.Any]
    endpoints: _list[GoogleCloudMetastoreV2Endpoint]
    version: str

@typing.type_check_only
class GoogleCloudMetastoreV2Backup(typing_extensions.TypedDict, total=False):
    createTime: str
    description: str
    endTime: str
    name: str
    restoringServices: _list[str]
    serviceRevision: GoogleCloudMetastoreV2Service
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "CREATING", "DELETING", "ACTIVE", "FAILED", "RESTORING"
    ]

@typing.type_check_only
class GoogleCloudMetastoreV2DataCatalogConfig(typing_extensions.TypedDict, total=False):
    enabled: bool

@typing.type_check_only
class GoogleCloudMetastoreV2DatabaseDump(typing_extensions.TypedDict, total=False):
    gcsUri: str
    type: typing_extensions.Literal["TYPE_UNSPECIFIED", "MYSQL", "AVRO"]

@typing.type_check_only
class GoogleCloudMetastoreV2EncryptionConfig(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudMetastoreV2Endpoint(typing_extensions.TypedDict, total=False):
    endpointUri: str
    region: str

@typing.type_check_only
class GoogleCloudMetastoreV2ExportMetadataRequest(
    typing_extensions.TypedDict, total=False
):
    databaseDumpType: typing_extensions.Literal["TYPE_UNSPECIFIED", "MYSQL", "AVRO"]
    destinationGcsFolder: str
    requestId: str

@typing.type_check_only
class GoogleCloudMetastoreV2HiveMetastoreConfig(
    typing_extensions.TypedDict, total=False
):
    auxiliaryVersions: dict[str, typing.Any]
    configOverrides: dict[str, typing.Any]
    endpointProtocol: typing_extensions.Literal[
        "ENDPOINT_PROTOCOL_UNSPECIFIED", "THRIFT", "GRPC"
    ]
    version: str

@typing.type_check_only
class GoogleCloudMetastoreV2ImportMetadataRequest(
    typing_extensions.TypedDict, total=False
):
    databaseDump: GoogleCloudMetastoreV2DatabaseDump
    description: str
    requestId: str

@typing.type_check_only
class GoogleCloudMetastoreV2LatestBackup(typing_extensions.TypedDict, total=False):
    backupId: str
    duration: str
    startTime: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "IN_PROGRESS", "SUCCEEDED", "FAILED"
    ]

@typing.type_check_only
class GoogleCloudMetastoreV2ListBackupsResponse(
    typing_extensions.TypedDict, total=False
):
    backups: _list[GoogleCloudMetastoreV2Backup]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class GoogleCloudMetastoreV2ListServicesResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    services: _list[GoogleCloudMetastoreV2Service]
    unreachable: _list[str]

@typing.type_check_only
class GoogleCloudMetastoreV2MetadataIntegration(
    typing_extensions.TypedDict, total=False
):
    dataCatalogConfig: GoogleCloudMetastoreV2DataCatalogConfig

@typing.type_check_only
class GoogleCloudMetastoreV2MoveTableToDatabaseRequest(
    typing_extensions.TypedDict, total=False
):
    dbName: str
    destinationDbName: str
    tableName: str

@typing.type_check_only
class GoogleCloudMetastoreV2QueryMetadataRequest(
    typing_extensions.TypedDict, total=False
):
    query: str

@typing.type_check_only
class GoogleCloudMetastoreV2RestoreServiceRequest(
    typing_extensions.TypedDict, total=False
):
    backup: str
    backupLocation: str
    requestId: str
    restoreType: typing_extensions.Literal[
        "RESTORE_TYPE_UNSPECIFIED", "FULL", "METADATA_ONLY"
    ]

@typing.type_check_only
class GoogleCloudMetastoreV2ScalingConfig(typing_extensions.TypedDict, total=False):
    scalingFactor: int

@typing.type_check_only
class GoogleCloudMetastoreV2ScheduledBackup(typing_extensions.TypedDict, total=False):
    backupLocation: str
    cronSchedule: str
    enabled: bool
    latestBackup: GoogleCloudMetastoreV2LatestBackup
    nextScheduledTime: str
    timeZone: str

@typing.type_check_only
class GoogleCloudMetastoreV2Service(typing_extensions.TypedDict, total=False):
    createTime: str
    encryptionConfig: GoogleCloudMetastoreV2EncryptionConfig
    endpoints: _list[GoogleCloudMetastoreV2Endpoint]
    hiveMetastoreConfig: GoogleCloudMetastoreV2HiveMetastoreConfig
    labels: dict[str, typing.Any]
    metadataIntegration: GoogleCloudMetastoreV2MetadataIntegration
    name: str
    scalingConfig: GoogleCloudMetastoreV2ScalingConfig
    scheduledBackup: GoogleCloudMetastoreV2ScheduledBackup
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "CREATING",
        "ACTIVE",
        "SUSPENDING",
        "SUSPENDED",
        "UPDATING",
        "DELETING",
        "ERROR",
    ]
    stateMessage: str
    uid: str
    updateTime: str
    warehouseGcsUri: str

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
