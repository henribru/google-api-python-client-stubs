import typing

import typing_extensions
@typing.type_check_only
class Backup(typing_extensions.TypedDict, total=False):
    endTime: str
    expireTime: str
    name: str
    sizeBytes: str
    sourceTable: str
    startTime: str
    state: typing_extensions.Literal["STATE_UNSPECIFIED", "CREATING", "READY"]

@typing.type_check_only
class BackupInfo(typing_extensions.TypedDict, total=False):
    backup: str
    endTime: str
    sourceTable: str
    startTime: str

@typing.type_check_only
class Cluster(typing_extensions.TypedDict, total=False):
    defaultStorageType: typing_extensions.Literal[
        "STORAGE_TYPE_UNSPECIFIED", "SSD", "HDD"
    ]
    location: str
    name: str
    serveNodes: int
    state: typing_extensions.Literal[
        "STATE_NOT_KNOWN", "READY", "CREATING", "RESIZING", "DISABLED"
    ]

@typing.type_check_only
class CreateBackupMetadata(typing_extensions.TypedDict, total=False):
    endTime: str
    name: str
    sourceTable: str
    startTime: str

@typing.type_check_only
class CreateClusterMetadata(typing_extensions.TypedDict, total=False):
    finishTime: str
    originalRequest: CreateClusterRequest
    requestTime: str
    tables: typing.Dict[str, typing.Any]

@typing.type_check_only
class CreateClusterRequest(typing_extensions.TypedDict, total=False):
    cluster: Cluster
    clusterId: str
    parent: str

@typing.type_check_only
class CreateInstanceMetadata(typing_extensions.TypedDict, total=False):
    finishTime: str
    originalRequest: CreateInstanceRequest
    requestTime: str

@typing.type_check_only
class CreateInstanceRequest(typing_extensions.TypedDict, total=False):
    clusters: typing.Dict[str, typing.Any]
    instance: Instance
    instanceId: str
    parent: str

@typing.type_check_only
class FailureTrace(typing_extensions.TypedDict, total=False):
    frames: typing.List[Frame]

@typing.type_check_only
class Frame(typing_extensions.TypedDict, total=False):
    targetName: str
    workflowGuid: str
    zoneId: str

@typing.type_check_only
class Instance(typing_extensions.TypedDict, total=False):
    displayName: str
    labels: typing.Dict[str, typing.Any]
    name: str
    state: typing_extensions.Literal["STATE_NOT_KNOWN", "READY", "CREATING"]
    type: typing_extensions.Literal["TYPE_UNSPECIFIED", "PRODUCTION", "DEVELOPMENT"]

@typing.type_check_only
class OperationProgress(typing_extensions.TypedDict, total=False):
    endTime: str
    progressPercent: int
    startTime: str

@typing.type_check_only
class OptimizeRestoredTableMetadata(typing_extensions.TypedDict, total=False):
    name: str
    progress: OperationProgress

@typing.type_check_only
class PartialUpdateInstanceRequest(typing_extensions.TypedDict, total=False):
    instance: Instance
    updateMask: str

@typing.type_check_only
class RestoreTableMetadata(typing_extensions.TypedDict, total=False):
    backupInfo: BackupInfo
    name: str
    optimizeTableOperationName: str
    progress: OperationProgress
    sourceType: typing_extensions.Literal["RESTORE_SOURCE_TYPE_UNSPECIFIED", "BACKUP"]

@typing.type_check_only
class TableProgress(typing_extensions.TypedDict, total=False):
    estimatedCopiedBytes: str
    estimatedSizeBytes: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "PENDING", "COPYING", "COMPLETED", "CANCELLED"
    ]

@typing.type_check_only
class UpdateAppProfileMetadata(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class UpdateClusterMetadata(typing_extensions.TypedDict, total=False):
    finishTime: str
    originalRequest: Cluster
    requestTime: str

@typing.type_check_only
class UpdateInstanceMetadata(typing_extensions.TypedDict, total=False):
    finishTime: str
    originalRequest: PartialUpdateInstanceRequest
    requestTime: str
