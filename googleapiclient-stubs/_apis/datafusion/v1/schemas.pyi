import typing

import typing_extensions

class ListOperationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    operations: typing.List[Operation]

class Empty(typing_extensions.TypedDict, total=False): ...

class ListLocationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    locations: typing.List[Location]

class CancelOperationRequest(typing_extensions.TypedDict, total=False): ...

class Operation(typing_extensions.TypedDict, total=False):
    error: Status
    response: typing.Dict[str, typing.Any]
    done: bool
    metadata: typing.Dict[str, typing.Any]
    name: str

class Status(typing_extensions.TypedDict, total=False):
    details: typing.List[typing.Dict[str, typing.Any]]
    code: int
    message: str

class RestartInstanceRequest(typing_extensions.TypedDict, total=False): ...

class TestIamPermissionsResponse(typing_extensions.TypedDict, total=False):
    permissions: typing.List[str]

class ListInstancesResponse(typing_extensions.TypedDict, total=False):
    instances: typing.List[Instance]
    nextPageToken: str
    unreachable: typing.List[str]

class AuditLogConfig(typing_extensions.TypedDict, total=False):
    logType: typing_extensions.Literal[
        "LOG_TYPE_UNSPECIFIED", "ADMIN_READ", "DATA_WRITE", "DATA_READ"
    ]
    exemptedMembers: typing.List[str]

class NetworkConfig(typing_extensions.TypedDict, total=False):
    network: str
    ipAllocation: str

class OperationMetadata(typing_extensions.TypedDict, total=False):
    createTime: str
    statusDetail: str
    target: str
    apiVersion: str
    endTime: str
    requestedCancellation: bool
    verb: str

class Location(typing_extensions.TypedDict, total=False):
    name: str
    locationId: str
    labels: typing.Dict[str, typing.Any]
    metadata: typing.Dict[str, typing.Any]
    displayName: str

class Accelerator(typing_extensions.TypedDict, total=False):
    acceleratorType: typing_extensions.Literal[
        "ACCELERATOR_TYPE_UNSPECIFIED", "CDC", "HEALTHCARE"
    ]

class ListAvailableVersionsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    availableVersions: typing.List[Version]

class SetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    policy: Policy
    updateMask: str

class Version(typing_extensions.TypedDict, total=False):
    versionNumber: str
    defaultVersion: bool
    availableFeatures: typing.List[str]

class AuditConfig(typing_extensions.TypedDict, total=False):
    auditLogConfigs: typing.List[AuditLogConfig]
    service: str

class TestIamPermissionsRequest(typing_extensions.TypedDict, total=False):
    permissions: typing.List[str]

class Binding(typing_extensions.TypedDict, total=False):
    members: typing.List[str]
    role: str
    condition: Expr
    bindingId: str

class Policy(typing_extensions.TypedDict, total=False):
    etag: str
    auditConfigs: typing.List[AuditConfig]
    bindings: typing.List[Binding]
    version: int

class Expr(typing_extensions.TypedDict, total=False):
    description: str
    location: str
    title: str
    expression: str

class Instance(typing_extensions.TypedDict, total=False):
    enableStackdriverLogging: bool
    displayName: str
    zone: str
    enableStackdriverMonitoring: bool
    updateTime: str
    p4ServiceAccount: str
    gcsBucket: str
    serviceAccount: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "CREATING",
        "ACTIVE",
        "FAILED",
        "DELETING",
        "UPGRADING",
        "RESTARTING",
        "UPDATING",
        "AUTO_UPDATING",
        "AUTO_UPGRADING",
    ]
    networkConfig: NetworkConfig
    labels: typing.Dict[str, typing.Any]
    name: str
    accelerators: typing.List[Accelerator]
    serviceEndpoint: str
    version: str
    options: typing.Dict[str, typing.Any]
    description: str
    apiEndpoint: str
    type: typing_extensions.Literal[
        "TYPE_UNSPECIFIED", "BASIC", "ENTERPRISE", "DEVELOPER"
    ]
    createTime: str
    dataprocServiceAccount: str
    tenantProjectId: str
    availableVersion: typing.List[Version]
    privateInstance: bool
    stateMessage: str
