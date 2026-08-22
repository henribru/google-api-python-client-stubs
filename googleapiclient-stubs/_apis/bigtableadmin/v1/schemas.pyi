import typing

_list = list

@typing.type_check_only
class AutoscalingLimits(typing.TypedDict, total=False):
    maxServeNodes: int
    minServeNodes: int

@typing.type_check_only
class AutoscalingTargets(typing.TypedDict, total=False):
    cpuUtilizationPercent: int

@typing.type_check_only
class Backup(typing.TypedDict, total=False):
    encryptionInfo: EncryptionInfo
    endTime: str
    expireTime: str
    name: str
    sizeBytes: str
    sourceTable: str
    startTime: str
    state: typing.Literal["STATE_UNSPECIFIED", "CREATING", "READY"]

@typing.type_check_only
class BackupInfo(typing.TypedDict, total=False):
    backup: str
    endTime: str
    sourceTable: str
    startTime: str

@typing.type_check_only
class Cluster(typing.TypedDict, total=False):
    clusterConfig: ClusterConfig
    defaultStorageType: typing.Literal["STORAGE_TYPE_UNSPECIFIED", "SSD", "HDD"]
    encryptionConfig: EncryptionConfig
    location: str
    name: str
    serveNodes: int
    state: typing.Literal[
        "STATE_NOT_KNOWN", "READY", "CREATING", "RESIZING", "DISABLED"
    ]

@typing.type_check_only
class ClusterAutoscalingConfig(typing.TypedDict, total=False):
    autoscalingLimits: AutoscalingLimits
    autoscalingTargets: AutoscalingTargets

@typing.type_check_only
class ClusterConfig(typing.TypedDict, total=False):
    clusterAutoscalingConfig: ClusterAutoscalingConfig

@typing.type_check_only
class CreateBackupMetadata(typing.TypedDict, total=False):
    endTime: str
    name: str
    sourceTable: str
    startTime: str

@typing.type_check_only
class CreateClusterMetadata(typing.TypedDict, total=False):
    finishTime: str
    originalRequest: CreateClusterRequest
    requestTime: str
    tables: dict[str, typing.Any]

@typing.type_check_only
class CreateClusterRequest(typing.TypedDict, total=False):
    cluster: Cluster
    clusterId: str
    parent: str

@typing.type_check_only
class CreateInstanceMetadata(typing.TypedDict, total=False):
    finishTime: str
    originalRequest: CreateInstanceRequest
    requestTime: str

@typing.type_check_only
class CreateInstanceRequest(typing.TypedDict, total=False):
    clusters: dict[str, typing.Any]
    instance: Instance
    instanceId: str
    parent: str

@typing.type_check_only
class EncryptionConfig(typing.TypedDict, total=False):
    kmsKeyName: str

@typing.type_check_only
class EncryptionInfo(typing.TypedDict, total=False):
    encryptionStatus: Status
    encryptionType: typing.Literal[
        "ENCRYPTION_TYPE_UNSPECIFIED",
        "GOOGLE_DEFAULT_ENCRYPTION",
        "CUSTOMER_MANAGED_ENCRYPTION",
    ]
    kmsKeyVersion: str

@typing.type_check_only
class Instance(typing.TypedDict, total=False):
    createTime: str
    displayName: str
    labels: dict[str, typing.Any]
    name: str
    state: typing.Literal["STATE_NOT_KNOWN", "READY", "CREATING"]
    type: typing.Literal["TYPE_UNSPECIFIED", "PRODUCTION", "DEVELOPMENT"]

@typing.type_check_only
class OperationProgress(typing.TypedDict, total=False):
    endTime: str
    progressPercent: int
    startTime: str

@typing.type_check_only
class OptimizeRestoredTableMetadata(typing.TypedDict, total=False):
    name: str
    progress: OperationProgress

@typing.type_check_only
class PartialUpdateClusterMetadata(typing.TypedDict, total=False):
    finishTime: str
    originalRequest: PartialUpdateClusterRequest
    requestTime: str

@typing.type_check_only
class PartialUpdateClusterRequest(typing.TypedDict, total=False):
    cluster: Cluster
    updateMask: str

@typing.type_check_only
class PartialUpdateInstanceRequest(typing.TypedDict, total=False):
    instance: Instance
    updateMask: str

@typing.type_check_only
class RestoreTableMetadata(typing.TypedDict, total=False):
    backupInfo: BackupInfo
    name: str
    optimizeTableOperationName: str
    progress: OperationProgress
    sourceType: typing.Literal["RESTORE_SOURCE_TYPE_UNSPECIFIED", "BACKUP"]

@typing.type_check_only
class Status(typing.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class TableProgress(typing.TypedDict, total=False):
    estimatedCopiedBytes: str
    estimatedSizeBytes: str
    state: typing.Literal[
        "STATE_UNSPECIFIED", "PENDING", "COPYING", "COMPLETED", "CANCELLED"
    ]

@typing.type_check_only
class UpdateAppProfileMetadata(typing.TypedDict, total=False): ...

@typing.type_check_only
class UpdateClusterMetadata(typing.TypedDict, total=False):
    finishTime: str
    originalRequest: Cluster
    requestTime: str

@typing.type_check_only
class UpdateInstanceMetadata(typing.TypedDict, total=False):
    finishTime: str
    originalRequest: PartialUpdateInstanceRequest
    requestTime: str
