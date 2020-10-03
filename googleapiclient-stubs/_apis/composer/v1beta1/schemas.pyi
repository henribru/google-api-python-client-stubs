import typing

import typing_extensions

class OperationMetadata(typing_extensions.TypedDict, total=False):
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "PENDING", "RUNNING", "SUCCESSFUL", "FAILED"
    ]
    operationType: typing_extensions.Literal[
        "TYPE_UNSPECIFIED", "CREATE", "DELETE", "UPDATE"
    ]
    endTime: str
    resource: str
    createTime: str
    resourceUuid: str

class Status(typing_extensions.TypedDict, total=False):
    details: typing.List[typing.Dict[str, typing.Any]]
    message: str
    code: int

class Operation(typing_extensions.TypedDict, total=False):
    name: str
    done: bool
    metadata: typing.Dict[str, typing.Any]
    response: typing.Dict[str, typing.Any]
    error: Status

class AllowedIpRange(typing_extensions.TypedDict, total=False):
    value: str
    description: str

class ImageVersion(typing_extensions.TypedDict, total=False):
    supportedPythonVersions: typing.List[str]
    isDefault: bool
    imageVersionId: str

class DatabaseConfig(typing_extensions.TypedDict, total=False):
    machineType: str

class NodeConfig(typing_extensions.TypedDict, total=False):
    subnetwork: str
    diskSizeGb: int
    tags: typing.List[str]
    location: str
    network: str
    serviceAccount: str
    oauthScopes: typing.List[str]
    machineType: str
    ipAllocationPolicy: IPAllocationPolicy

class Environment(typing_extensions.TypedDict, total=False):
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "CREATING", "RUNNING", "UPDATING", "DELETING", "ERROR"
    ]
    labels: typing.Dict[str, typing.Any]
    name: str
    uuid: str
    updateTime: str
    config: EnvironmentConfig
    createTime: str

class Empty(typing_extensions.TypedDict, total=False): ...

class WebServerConfig(typing_extensions.TypedDict, total=False):
    machineType: str

class ListEnvironmentsResponse(typing_extensions.TypedDict, total=False):
    environments: typing.List[Environment]
    nextPageToken: str

class WebServerNetworkAccessControl(typing_extensions.TypedDict, total=False):
    allowedIpRanges: typing.List[AllowedIpRange]

class IPAllocationPolicy(typing_extensions.TypedDict, total=False):
    servicesIpv4CidrBlock: str
    servicesSecondaryRangeName: str
    clusterSecondaryRangeName: str
    clusterIpv4CidrBlock: str
    useIpAliases: bool

class EnvironmentConfig(typing_extensions.TypedDict, total=False):
    nodeCount: int
    airflowUri: str
    softwareConfig: SoftwareConfig
    gkeCluster: str
    webServerNetworkAccessControl: WebServerNetworkAccessControl
    nodeConfig: NodeConfig
    dagGcsPrefix: str
    webServerConfig: WebServerConfig
    privateEnvironmentConfig: PrivateEnvironmentConfig
    databaseConfig: DatabaseConfig

class ListOperationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    operations: typing.List[Operation]

class PrivateEnvironmentConfig(typing_extensions.TypedDict, total=False):
    webServerIpv4ReservedRange: str
    webServerIpv4CidrBlock: str
    cloudSqlIpv4CidrBlock: str
    privateClusterConfig: PrivateClusterConfig
    enablePrivateEnvironment: bool

class PrivateClusterConfig(typing_extensions.TypedDict, total=False):
    enablePrivateEndpoint: bool
    masterIpv4CidrBlock: str
    masterIpv4ReservedRange: str

class SoftwareConfig(typing_extensions.TypedDict, total=False):
    envVariables: typing.Dict[str, typing.Any]
    pythonVersion: str
    imageVersion: str
    pypiPackages: typing.Dict[str, typing.Any]
    airflowConfigOverrides: typing.Dict[str, typing.Any]

class ListImageVersionsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    imageVersions: typing.List[ImageVersion]
