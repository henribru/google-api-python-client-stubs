import typing

import typing_extensions

_list = list

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
class DatabaseConfig(typing_extensions.TypedDict, total=False):
    machineType: str

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
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "CREATING", "RUNNING", "UPDATING", "DELETING", "ERROR"
    ]
    updateTime: str
    uuid: str

@typing.type_check_only
class EnvironmentConfig(typing_extensions.TypedDict, total=False):
    airflowUri: str
    dagGcsPrefix: str
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
    softwareConfig: SoftwareConfig
    webServerConfig: WebServerConfig
    webServerNetworkAccessControl: WebServerNetworkAccessControl
    workloadsConfig: WorkloadsConfig

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
class LoadSnapshotRequest(typing_extensions.TypedDict, total=False):
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
    diskSizeGb: int
    enableIpMasqAgent: bool
    ipAllocationPolicy: IPAllocationPolicy
    location: str
    machineType: str
    maxPodsPerNode: int
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
    ]
    resource: str
    resourceUuid: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "PENDING", "RUNNING", "SUCCESSFUL", "FAILED"
    ]

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
    enablePrivateEnvironment: bool
    enablePrivatelyUsedPublicIps: bool
    networkingConfig: NetworkingConfig
    privateClusterConfig: PrivateClusterConfig
    webServerIpv4CidrBlock: str
    webServerIpv4ReservedRange: str

@typing.type_check_only
class RestartWebServerRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class SaveSnapshotRequest(typing_extensions.TypedDict, total=False):
    snapshotLocation: str

@typing.type_check_only
class SaveSnapshotResponse(typing_extensions.TypedDict, total=False):
    snapshotPath: str

@typing.type_check_only
class SchedulerResource(typing_extensions.TypedDict, total=False):
    count: int
    cpu: float
    memoryGb: float
    storageGb: float

@typing.type_check_only
class SoftwareConfig(typing_extensions.TypedDict, total=False):
    airflowConfigOverrides: dict[str, typing.Any]
    envVariables: dict[str, typing.Any]
    imageVersion: str
    pypiPackages: dict[str, typing.Any]
    pythonVersion: str
    schedulerCount: int

@typing.type_check_only
class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

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
    scheduler: SchedulerResource
    webServer: WebServerResource
    worker: WorkerResource
