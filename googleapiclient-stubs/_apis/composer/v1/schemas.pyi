import typing

import typing_extensions

class Empty(typing_extensions.TypedDict, total=False): ...

class PrivateEnvironmentConfig(typing_extensions.TypedDict, total=False):
    webServerIpv4CidrBlock: str
    webServerIpv4ReservedRange: str
    privateClusterConfig: PrivateClusterConfig
    enablePrivateEnvironment: bool
    cloudSqlIpv4CidrBlock: str

class Environment(typing_extensions.TypedDict, total=False):
    createTime: str
    uuid: str
    name: str
    config: EnvironmentConfig
    labels: typing.Dict[str, typing.Any]
    updateTime: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "CREATING", "RUNNING", "UPDATING", "DELETING", "ERROR"
    ]

class ImageVersion(typing_extensions.TypedDict, total=False):
    supportedPythonVersions: typing.List[str]
    imageVersionId: str
    isDefault: bool

class ListOperationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    operations: typing.List[Operation]

class SoftwareConfig(typing_extensions.TypedDict, total=False):
    pythonVersion: str
    imageVersion: str
    pypiPackages: typing.Dict[str, typing.Any]
    airflowConfigOverrides: typing.Dict[str, typing.Any]
    envVariables: typing.Dict[str, typing.Any]

class OperationMetadata(typing_extensions.TypedDict, total=False):
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "PENDING", "RUNNING", "SUCCEEDED", "SUCCESSFUL", "FAILED"
    ]
    endTime: str
    resource: str
    resourceUuid: str
    createTime: str
    operationType: typing_extensions.Literal[
        "TYPE_UNSPECIFIED", "CREATE", "DELETE", "UPDATE"
    ]

class PrivateClusterConfig(typing_extensions.TypedDict, total=False):
    masterIpv4ReservedRange: str
    enablePrivateEndpoint: bool
    masterIpv4CidrBlock: str

class Operation(typing_extensions.TypedDict, total=False):
    metadata: typing.Dict[str, typing.Any]
    name: str
    error: Status
    done: bool
    response: typing.Dict[str, typing.Any]

class ListEnvironmentsResponse(typing_extensions.TypedDict, total=False):
    environments: typing.List[Environment]
    nextPageToken: str

class Status(typing_extensions.TypedDict, total=False):
    code: int
    message: str
    details: typing.List[typing.Dict[str, typing.Any]]

class EnvironmentConfig(typing_extensions.TypedDict, total=False):
    dagGcsPrefix: str
    airflowUri: str
    gkeCluster: str
    privateEnvironmentConfig: PrivateEnvironmentConfig
    softwareConfig: SoftwareConfig
    nodeConfig: NodeConfig
    nodeCount: int

class IPAllocationPolicy(typing_extensions.TypedDict, total=False):
    useIpAliases: bool
    servicesIpv4CidrBlock: str
    servicesSecondaryRangeName: str
    clusterIpv4CidrBlock: str
    clusterSecondaryRangeName: str

class ListImageVersionsResponse(typing_extensions.TypedDict, total=False):
    imageVersions: typing.List[ImageVersion]
    nextPageToken: str

class NodeConfig(typing_extensions.TypedDict, total=False):
    ipAllocationPolicy: IPAllocationPolicy
    machineType: str
    oauthScopes: typing.List[str]
    tags: typing.List[str]
    diskSizeGb: int
    subnetwork: str
    location: str
    serviceAccount: str
    network: str
