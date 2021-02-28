import typing

import typing_extensions
@typing.type_check_only
class AllowedIpRange(typing_extensions.TypedDict, total=False):
    description: str
    value: str

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
    labels: typing.Dict[str, typing.Any]
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
    gkeCluster: str
    maintenanceWindow: MaintenanceWindow
    nodeConfig: NodeConfig
    nodeCount: int
    privateEnvironmentConfig: PrivateEnvironmentConfig
    softwareConfig: SoftwareConfig
    webServerConfig: WebServerConfig
    webServerNetworkAccessControl: WebServerNetworkAccessControl

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
    supportedPythonVersions: typing.List[str]
    upgradeDisabled: bool

@typing.type_check_only
class ListEnvironmentsResponse(typing_extensions.TypedDict, total=False):
    environments: typing.List[Environment]
    nextPageToken: str

@typing.type_check_only
class ListImageVersionsResponse(typing_extensions.TypedDict, total=False):
    imageVersions: typing.List[ImageVersion]
    nextPageToken: str

@typing.type_check_only
class ListOperationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    operations: typing.List[Operation]

@typing.type_check_only
class MaintenanceWindow(typing_extensions.TypedDict, total=False):
    endTime: str
    recurrence: str
    startTime: str

@typing.type_check_only
class NodeConfig(typing_extensions.TypedDict, total=False):
    diskSizeGb: int
    ipAllocationPolicy: IPAllocationPolicy
    location: str
    machineType: str
    maxPodsPerNode: int
    network: str
    oauthScopes: typing.List[str]
    serviceAccount: str
    subnetwork: str
    tags: typing.List[str]

@typing.type_check_only
class Operation(typing_extensions.TypedDict, total=False):
    done: bool
    error: Status
    metadata: typing.Dict[str, typing.Any]
    name: str
    response: typing.Dict[str, typing.Any]

@typing.type_check_only
class OperationMetadata(typing_extensions.TypedDict, total=False):
    createTime: str
    endTime: str
    operationType: typing_extensions.Literal[
        "TYPE_UNSPECIFIED", "CREATE", "DELETE", "UPDATE"
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
    cloudSqlIpv4CidrBlock: str
    enablePrivateEnvironment: bool
    privateClusterConfig: PrivateClusterConfig
    webServerIpv4CidrBlock: str
    webServerIpv4ReservedRange: str

@typing.type_check_only
class RestartWebServerRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class SoftwareConfig(typing_extensions.TypedDict, total=False):
    airflowConfigOverrides: typing.Dict[str, typing.Any]
    envVariables: typing.Dict[str, typing.Any]
    imageVersion: str
    pypiPackages: typing.Dict[str, typing.Any]
    pythonVersion: str

@typing.type_check_only
class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: typing.List[typing.Dict[str, typing.Any]]
    message: str

@typing.type_check_only
class WebServerConfig(typing_extensions.TypedDict, total=False):
    machineType: str

@typing.type_check_only
class WebServerNetworkAccessControl(typing_extensions.TypedDict, total=False):
    allowedIpRanges: typing.List[AllowedIpRange]
