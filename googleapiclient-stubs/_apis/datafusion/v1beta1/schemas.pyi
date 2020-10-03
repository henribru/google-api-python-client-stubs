import typing

import typing_extensions

class UpgradeInstanceRequest(typing_extensions.TypedDict, total=False): ...

class ListInstancesResponse(typing_extensions.TypedDict, total=False):
    instances: typing.List[Instance]
    nextPageToken: str
    unreachable: typing.List[str]

class Version(typing_extensions.TypedDict, total=False):
    availableFeatures: typing.List[str]
    defaultVersion: bool
    versionNumber: str

class ListLocationsResponse(typing_extensions.TypedDict, total=False):
    locations: typing.List[Location]
    nextPageToken: str

class Expr(typing_extensions.TypedDict, total=False):
    expression: str
    location: str
    description: str
    title: str

class NetworkConfig(typing_extensions.TypedDict, total=False):
    ipAllocation: str
    network: str

class ListAvailableVersionsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    availableVersions: typing.List[Version]

class TestIamPermissionsResponse(typing_extensions.TypedDict, total=False):
    permissions: typing.List[str]

class Operation(typing_extensions.TypedDict, total=False):
    error: Status
    response: typing.Dict[str, typing.Any]
    metadata: typing.Dict[str, typing.Any]
    name: str
    done: bool

class CancelOperationRequest(typing_extensions.TypedDict, total=False): ...

class Status(typing_extensions.TypedDict, total=False):
    details: typing.List[typing.Dict[str, typing.Any]]
    message: str
    code: int

class Location(typing_extensions.TypedDict, total=False):
    labels: typing.Dict[str, typing.Any]
    locationId: str
    name: str
    metadata: typing.Dict[str, typing.Any]
    displayName: str

class Accelerator(typing_extensions.TypedDict, total=False):
    acceleratorType: typing_extensions.Literal[
        "ACCELERATOR_TYPE_UNSPECIFIED", "CDC", "HEALTHCARE"
    ]

class Binding(typing_extensions.TypedDict, total=False):
    role: str
    condition: Expr
    bindingId: str
    members: typing.List[str]

class TestIamPermissionsRequest(typing_extensions.TypedDict, total=False):
    permissions: typing.List[str]

class RestartInstanceRequest(typing_extensions.TypedDict, total=False): ...
class Empty(typing_extensions.TypedDict, total=False): ...

class AuditConfig(typing_extensions.TypedDict, total=False):
    service: str
    auditLogConfigs: typing.List[AuditLogConfig]

class Policy(typing_extensions.TypedDict, total=False):
    auditConfigs: typing.List[AuditConfig]
    etag: str
    bindings: typing.List[Binding]
    version: int

class OperationMetadata(typing_extensions.TypedDict, total=False):
    createTime: str
    target: str
    requestedCancellation: bool
    endTime: str
    statusDetail: str
    apiVersion: str
    verb: str

class AuditLogConfig(typing_extensions.TypedDict, total=False):
    logType: typing_extensions.Literal[
        "LOG_TYPE_UNSPECIFIED", "ADMIN_READ", "DATA_WRITE", "DATA_READ"
    ]
    exemptedMembers: typing.List[str]

class ListOperationsResponse(typing_extensions.TypedDict, total=False):
    operations: typing.List[Operation]
    nextPageToken: str

class Instance(typing_extensions.TypedDict, total=False):
    accelerators: typing.List[Accelerator]
    availableVersion: typing.List[Version]
    gcsBucket: str
    serviceEndpoint: str
    dataprocServiceAccount: str
    displayName: str
    networkConfig: NetworkConfig
    enableStackdriverLogging: bool
    createTime: str
    type: typing_extensions.Literal[
        "TYPE_UNSPECIFIED", "BASIC", "ENTERPRISE", "DEVELOPER"
    ]
    zone: str
    stateMessage: str
    updateTime: str
    tenantProjectId: str
    version: str
    description: str
    options: typing.Dict[str, typing.Any]
    labels: typing.Dict[str, typing.Any]
    apiEndpoint: str
    name: str
    privateInstance: bool
    serviceAccount: str
    enableStackdriverMonitoring: bool
    p4ServiceAccount: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "CREATING",
        "RUNNING",
        "FAILED",
        "DELETING",
        "UPGRADING",
        "RESTARTING",
        "UPDATING",
        "AUTO_UPDATING",
        "AUTO_UPGRADING",
    ]

class SetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    updateMask: str
    policy: Policy
