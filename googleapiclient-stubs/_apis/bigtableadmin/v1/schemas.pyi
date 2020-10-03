import typing

import typing_extensions

class RestoreTableMetadata(typing_extensions.TypedDict, total=False):
    name: str
    progress: OperationProgress
    optimizeTableOperationName: str
    sourceType: typing_extensions.Literal["RESTORE_SOURCE_TYPE_UNSPECIFIED", "BACKUP"]
    backupInfo: BackupInfo

class PartialUpdateInstanceRequest(typing_extensions.TypedDict, total=False):
    instance: Instance
    updateMask: str

class Backup(typing_extensions.TypedDict, total=False):
    state: typing_extensions.Literal["STATE_UNSPECIFIED", "CREATING", "READY"]
    endTime: str
    sizeBytes: str
    startTime: str
    expireTime: str
    sourceTable: str
    name: str

class BackupInfo(typing_extensions.TypedDict, total=False):
    sourceTable: str
    endTime: str
    backup: str
    startTime: str

class UpdateClusterMetadata(typing_extensions.TypedDict, total=False):
    originalRequest: Cluster
    requestTime: str
    finishTime: str

class OptimizeRestoredTableMetadata(typing_extensions.TypedDict, total=False):
    name: str
    progress: OperationProgress

class CreateClusterRequest(typing_extensions.TypedDict, total=False):
    cluster: Cluster
    clusterId: str
    parent: str

class TableProgress(typing_extensions.TypedDict, total=False):
    estimatedSizeBytes: str
    estimatedCopiedBytes: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "PENDING", "COPYING", "COMPLETED", "CANCELLED"
    ]

class UpdateInstanceMetadata(typing_extensions.TypedDict, total=False):
    originalRequest: PartialUpdateInstanceRequest
    finishTime: str
    requestTime: str

class OperationProgress(typing_extensions.TypedDict, total=False):
    endTime: str
    progressPercent: int
    startTime: str

class UpdateAppProfileMetadata(typing_extensions.TypedDict, total=False): ...

class FailureTrace(typing_extensions.TypedDict, total=False):
    frames: typing.List[Frame]

class CreateInstanceMetadata(typing_extensions.TypedDict, total=False):
    originalRequest: CreateInstanceRequest
    finishTime: str
    requestTime: str

class Instance(typing_extensions.TypedDict, total=False):
    state: typing_extensions.Literal["STATE_NOT_KNOWN", "READY", "CREATING"]
    displayName: str
    name: str
    labels: typing.Dict[str, typing.Any]
    type: typing_extensions.Literal["TYPE_UNSPECIFIED", "PRODUCTION", "DEVELOPMENT"]

class Frame(typing_extensions.TypedDict, total=False):
    workflowGuid: str
    zoneId: str
    targetName: str

class CreateClusterMetadata(typing_extensions.TypedDict, total=False):
    finishTime: str
    tables: typing.Dict[str, typing.Any]
    requestTime: str
    originalRequest: CreateClusterRequest

class CreateInstanceRequest(typing_extensions.TypedDict, total=False):
    clusters: typing.Dict[str, typing.Any]
    instance: Instance
    parent: str
    instanceId: str

class Cluster(typing_extensions.TypedDict, total=False):
    name: str
    serveNodes: int
    defaultStorageType: typing_extensions.Literal[
        "STORAGE_TYPE_UNSPECIFIED", "SSD", "HDD"
    ]
    location: str
    state: typing_extensions.Literal[
        "STATE_NOT_KNOWN", "READY", "CREATING", "RESIZING", "DISABLED"
    ]

class CreateBackupMetadata(typing_extensions.TypedDict, total=False):
    startTime: str
    sourceTable: str
    endTime: str
    name: str
