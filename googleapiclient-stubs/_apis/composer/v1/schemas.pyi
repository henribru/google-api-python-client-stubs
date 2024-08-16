import typing

import typing_extensions

_list = list

@typing.type_check_only
class AirflowMetadataRetentionPolicyConfig(typing_extensions.TypedDict, total=False):
    retentionDays: int
    retentionMode: typing_extensions.Literal[
        "RETENTION_MODE_UNSPECIFIED",
        "RETENTION_MODE_ENABLED",
        "RETENTION_MODE_DISABLED",
    ]

@typing.type_check_only
class AllowedIpRange(typing_extensions.TypedDict, total=False):
    description: str
    value: str

@typing.type_check_only
class CheckUpgradeRequest(typing_extensions.TypedDict, total=False):
    imageVersion: str

@typing.type_check_only
class CheckUpgradeResponse(typing_extensions.TypedDict, total=False):
    buildLogUri: str
    containsPypiModulesConflict: typing_extensions.Literal[
        "CONFLICT_RESULT_UNSPECIFIED", "CONFLICT", "NO_CONFLICT"
    ]
    imageVersion: str
    pypiConflictBuildLogExtract: str
    pypiDependencies: dict[str, typing.Any]

@typing.type_check_only
class CidrBlock(typing_extensions.TypedDict, total=False):
    cidrBlock: str
    displayName: str

@typing.type_check_only
class CloudDataLineageIntegration(typing_extensions.TypedDict, total=False):
    enabled: bool

@typing.type_check_only
class ComposerWorkload(typing_extensions.TypedDict, total=False):
    name: str
    status: ComposerWorkloadStatus
    type: typing_extensions.Literal[
        "COMPOSER_WORKLOAD_TYPE_UNSPECIFIED",
        "CELERY_WORKER",
        "KUBERNETES_WORKER",
        "KUBERNETES_OPERATOR_POD",
        "SCHEDULER",
        "DAG_PROCESSOR",
        "TRIGGERER",
        "WEB_SERVER",
        "REDIS",
    ]

@typing.type_check_only
class ComposerWorkloadStatus(typing_extensions.TypedDict, total=False):
    detailedStatusMessage: str
    state: typing_extensions.Literal[
        "COMPOSER_WORKLOAD_STATE_UNSPECIFIED",
        "PENDING",
        "OK",
        "WARNING",
        "ERROR",
        "SUCCEEDED",
        "FAILED",
    ]
    statusMessage: str

@typing.type_check_only
class DagProcessorResource(typing_extensions.TypedDict, total=False):
    count: int
    cpu: float
    memoryGb: float
    storageGb: float

@typing.type_check_only
class DataRetentionConfig(typing_extensions.TypedDict, total=False):
    airflowMetadataRetentionConfig: AirflowMetadataRetentionPolicyConfig
    taskLogsRetentionConfig: TaskLogsRetentionConfig

@typing.type_check_only
class DatabaseConfig(typing_extensions.TypedDict, total=False):
    machineType: str
    zone: str

@typing.type_check_only
class DatabaseFailoverRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class DatabaseFailoverResponse(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Date(typing_extensions.TypedDict, total=False):
    day: int
    month: int
    year: int

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class EncryptionConfig(typing_extensions.TypedDict, total=False):
    kmsKeyName: str

@typing.type_check_only
class Environment(typing_extensions.TypedDict, total=False):
    config: EnvironmentConfig
    createTime: str
    labels: dict[str, typing.Any]
    name: str
    satisfiesPzi: bool
    satisfiesPzs: bool
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "CREATING", "RUNNING", "UPDATING", "DELETING", "ERROR"
    ]
    storageConfig: StorageConfig
    updateTime: str
    uuid: str

@typing.type_check_only
class EnvironmentConfig(typing_extensions.TypedDict, total=False):
    airflowByoidUri: str
    airflowUri: str
    dagGcsPrefix: str
    dataRetentionConfig: DataRetentionConfig
    databaseConfig: DatabaseConfig
    encryptionConfig: EncryptionConfig
    environmentSize: typing_extensions.Literal[
        "ENVIRONMENT_SIZE_UNSPECIFIED",
        "ENVIRONMENT_SIZE_SMALL",
        "ENVIRONMENT_SIZE_MEDIUM",
        "ENVIRONMENT_SIZE_LARGE",
    ]
    gkeCluster: str
    maintenanceWindow: MaintenanceWindow
    masterAuthorizedNetworksConfig: MasterAuthorizedNetworksConfig
    nodeConfig: NodeConfig
    nodeCount: int
    privateEnvironmentConfig: PrivateEnvironmentConfig
    recoveryConfig: RecoveryConfig
    resilienceMode: typing_extensions.Literal[
        "RESILIENCE_MODE_UNSPECIFIED", "HIGH_RESILIENCE"
    ]
    softwareConfig: SoftwareConfig
    webServerConfig: WebServerConfig
    webServerNetworkAccessControl: WebServerNetworkAccessControl
    workloadsConfig: WorkloadsConfig

@typing.type_check_only
class ExecuteAirflowCommandRequest(typing_extensions.TypedDict, total=False):
    command: str
    parameters: _list[str]
    subcommand: str

@typing.type_check_only
class ExecuteAirflowCommandResponse(typing_extensions.TypedDict, total=False):
    error: str
    executionId: str
    pod: str
    podNamespace: str

@typing.type_check_only
class ExitInfo(typing_extensions.TypedDict, total=False):
    error: str
    exitCode: int

@typing.type_check_only
class FetchDatabasePropertiesResponse(typing_extensions.TypedDict, total=False):
    isFailoverReplicaAvailable: bool
    primaryGceZone: str
    secondaryGceZone: str

@typing.type_check_only
class IPAllocationPolicy(typing_extensions.TypedDict, total=False):
    clusterIpv4CidrBlock: str
    clusterSecondaryRangeName: str
    servicesIpv4CidrBlock: str
    servicesSecondaryRangeName: str
    useIpAliases: bool

@typing.type_check_only
class ImageVersion(typing_extensions.TypedDict, total=False):
    creationDisabled: bool
    imageVersionId: str
    isDefault: bool
    releaseDate: Date
    supportedPythonVersions: _list[str]
    upgradeDisabled: bool

@typing.type_check_only
class Line(typing_extensions.TypedDict, total=False):
    content: str
    lineNumber: int

@typing.type_check_only
class ListEnvironmentsResponse(typing_extensions.TypedDict, total=False):
    environments: _list[Environment]
    nextPageToken: str

@typing.type_check_only
class ListImageVersionsResponse(typing_extensions.TypedDict, total=False):
    imageVersions: _list[ImageVersion]
    nextPageToken: str

@typing.type_check_only
class ListOperationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    operations: _list[Operation]

@typing.type_check_only
class ListUserWorkloadsConfigMapsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    userWorkloadsConfigMaps: _list[UserWorkloadsConfigMap]

@typing.type_check_only
class ListUserWorkloadsSecretsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    userWorkloadsSecrets: _list[UserWorkloadsSecret]

@typing.type_check_only
class ListWorkloadsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    workloads: _list[ComposerWorkload]

@typing.type_check_only
class LoadSnapshotRequest(typing_extensions.TypedDict, total=False):
    skipAirflowOverridesSetting: bool
    skipEnvironmentVariablesSetting: bool
    skipGcsDataCopying: bool
    skipPypiPackagesInstallation: bool
    snapshotPath: str

@typing.type_check_only
class LoadSnapshotResponse(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class MaintenanceWindow(typing_extensions.TypedDict, total=False):
    endTime: str
    recurrence: str
    startTime: str

@typing.type_check_only
class MasterAuthorizedNetworksConfig(typing_extensions.TypedDict, total=False):
    cidrBlocks: _list[CidrBlock]
    enabled: bool

@typing.type_check_only
class NetworkingConfig(typing_extensions.TypedDict, total=False):
    connectionType: typing_extensions.Literal[
        "CONNECTION_TYPE_UNSPECIFIED", "VPC_PEERING", "PRIVATE_SERVICE_CONNECT"
    ]

@typing.type_check_only
class NodeConfig(typing_extensions.TypedDict, total=False):
    composerInternalIpv4CidrBlock: str
    composerNetworkAttachment: str
    diskSizeGb: int
    enableIpMasqAgent: bool
    ipAllocationPolicy: IPAllocationPolicy
    location: str
    machineType: str
    network: str
    oauthScopes: _list[str]
    serviceAccount: str
    subnetwork: str
    tags: _list[str]

@typing.type_check_only
class Operation(typing_extensions.TypedDict, total=False):
    done: bool
    error: Status
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class OperationMetadata(typing_extensions.TypedDict, total=False):
    createTime: str
    endTime: str
    operationType: typing_extensions.Literal[
        "TYPE_UNSPECIFIED",
        "CREATE",
        "DELETE",
        "UPDATE",
        "CHECK",
        "SAVE_SNAPSHOT",
        "LOAD_SNAPSHOT",
        "DATABASE_FAILOVER",
    ]
    resource: str
    resourceUuid: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "PENDING", "RUNNING", "SUCCEEDED", "SUCCESSFUL", "FAILED"
    ]

@typing.type_check_only
class PollAirflowCommandRequest(typing_extensions.TypedDict, total=False):
    executionId: str
    nextLineNumber: int
    pod: str
    podNamespace: str

@typing.type_check_only
class PollAirflowCommandResponse(typing_extensions.TypedDict, total=False):
    exitInfo: ExitInfo
    output: _list[Line]
    outputEnd: bool

@typing.type_check_only
class PrivateClusterConfig(typing_extensions.TypedDict, total=False):
    enablePrivateEndpoint: bool
    masterIpv4CidrBlock: str
    masterIpv4ReservedRange: str

@typing.type_check_only
class PrivateEnvironmentConfig(typing_extensions.TypedDict, total=False):
    cloudComposerConnectionSubnetwork: str
    cloudComposerNetworkIpv4CidrBlock: str
    cloudComposerNetworkIpv4ReservedRange: str
    cloudSqlIpv4CidrBlock: str
    enablePrivateBuildsOnly: bool
    enablePrivateEnvironment: bool
    enablePrivatelyUsedPublicIps: bool
    networkingConfig: NetworkingConfig
    privateClusterConfig: PrivateClusterConfig
    webServerIpv4CidrBlock: str
    webServerIpv4ReservedRange: str

@typing.type_check_only
class RecoveryConfig(typing_extensions.TypedDict, total=False):
    scheduledSnapshotsConfig: ScheduledSnapshotsConfig

@typing.type_check_only
class SaveSnapshotRequest(typing_extensions.TypedDict, total=False):
    snapshotLocation: str

@typing.type_check_only
class SaveSnapshotResponse(typing_extensions.TypedDict, total=False):
    snapshotPath: str

@typing.type_check_only
class ScheduledSnapshotsConfig(typing_extensions.TypedDict, total=False):
    enabled: bool
    snapshotCreationSchedule: str
    snapshotLocation: str
    timeZone: str

@typing.type_check_only
class SchedulerResource(typing_extensions.TypedDict, total=False):
    count: int
    cpu: float
    memoryGb: float
    storageGb: float

@typing.type_check_only
class SoftwareConfig(typing_extensions.TypedDict, total=False):
    airflowConfigOverrides: dict[str, typing.Any]
    cloudDataLineageIntegration: CloudDataLineageIntegration
    envVariables: dict[str, typing.Any]
    imageVersion: str
    pypiPackages: dict[str, typing.Any]
    pythonVersion: str
    schedulerCount: int
    webServerPluginsMode: typing_extensions.Literal[
        "WEB_SERVER_PLUGINS_MODE_UNSPECIFIED", "PLUGINS_DISABLED", "PLUGINS_ENABLED"
    ]

@typing.type_check_only
class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class StopAirflowCommandRequest(typing_extensions.TypedDict, total=False):
    executionId: str
    force: bool
    pod: str
    podNamespace: str

@typing.type_check_only
class StopAirflowCommandResponse(typing_extensions.TypedDict, total=False):
    isDone: bool
    output: _list[str]

@typing.type_check_only
class StorageConfig(typing_extensions.TypedDict, total=False):
    bucket: str

@typing.type_check_only
class TaskLogsRetentionConfig(typing_extensions.TypedDict, total=False):
    storageMode: typing_extensions.Literal[
        "TASK_LOGS_STORAGE_MODE_UNSPECIFIED",
        "CLOUD_LOGGING_AND_CLOUD_STORAGE",
        "CLOUD_LOGGING_ONLY",
    ]

@typing.type_check_only
class TriggererResource(typing_extensions.TypedDict, total=False):
    count: int
    cpu: float
    memoryGb: float

@typing.type_check_only
class UserWorkloadsConfigMap(typing_extensions.TypedDict, total=False):
    data: dict[str, typing.Any]
    name: str

@typing.type_check_only
class UserWorkloadsSecret(typing_extensions.TypedDict, total=False):
    data: dict[str, typing.Any]
    name: str

@typing.type_check_only
class WebServerConfig(typing_extensions.TypedDict, total=False):
    machineType: str

@typing.type_check_only
class WebServerNetworkAccessControl(typing_extensions.TypedDict, total=False):
    allowedIpRanges: _list[AllowedIpRange]

@typing.type_check_only
class WebServerResource(typing_extensions.TypedDict, total=False):
    cpu: float
    memoryGb: float
    storageGb: float

@typing.type_check_only
class WorkerResource(typing_extensions.TypedDict, total=False):
    cpu: float
    maxCount: int
    memoryGb: float
    minCount: int
    storageGb: float

@typing.type_check_only
class WorkloadsConfig(typing_extensions.TypedDict, total=False):
    dagProcessor: DagProcessorResource
    scheduler: SchedulerResource
    triggerer: TriggererResource
    webServer: WebServerResource
    worker: WorkerResource
