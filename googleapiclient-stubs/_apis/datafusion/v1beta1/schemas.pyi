import typing

import typing_extensions

_list = list

@typing.type_check_only
class Accelerator(typing_extensions.TypedDict, total=False):
    acceleratorType: typing_extensions.Literal[
        "ACCELERATOR_TYPE_UNSPECIFIED", "CDC", "HEALTHCARE"
    ]

@typing.type_check_only
class AuditConfig(typing_extensions.TypedDict, total=False):
    auditLogConfigs: _list[AuditLogConfig]
    service: str

@typing.type_check_only
class AuditLogConfig(typing_extensions.TypedDict, total=False):
    exemptedMembers: _list[str]
    logType: typing_extensions.Literal[
        "LOG_TYPE_UNSPECIFIED", "ADMIN_READ", "DATA_WRITE", "DATA_READ"
    ]

@typing.type_check_only
class Binding(typing_extensions.TypedDict, total=False):
    condition: Expr
    members: _list[str]
    role: str

@typing.type_check_only
class CancelOperationRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class CryptoKeyConfig(typing_extensions.TypedDict, total=False):
    keyReference: str

@typing.type_check_only
class DnsPeering(typing_extensions.TypedDict, total=False):
    description: str
    domain: str
    name: str
    targetNetwork: str
    targetProject: str

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class EventPublishConfig(typing_extensions.TypedDict, total=False):
    enabled: bool
    topic: str

@typing.type_check_only
class Expr(typing_extensions.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str

@typing.type_check_only
class IAMPolicy(typing_extensions.TypedDict, total=False):
    policy: Policy
    status: Status

@typing.type_check_only
class Instance(typing_extensions.TypedDict, total=False):
    accelerators: _list[Accelerator]
    apiEndpoint: str
    availableVersion: _list[Version]
    createTime: str
    cryptoKeyConfig: CryptoKeyConfig
    dataprocServiceAccount: str
    description: str
    disabledReason: _list[str]
    displayName: str
    enableRbac: bool
    enableStackdriverLogging: bool
    enableStackdriverMonitoring: bool
    eventPublishConfig: EventPublishConfig
    gcsBucket: str
    labels: dict[str, typing.Any]
    name: str
    networkConfig: NetworkConfig
    options: dict[str, typing.Any]
    p4ServiceAccount: str
    privateInstance: bool
    serviceAccount: str
    serviceEndpoint: str
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
        "DISABLED",
    ]
    stateMessage: str
    tenantProjectId: str
    type: typing_extensions.Literal[
        "TYPE_UNSPECIFIED", "BASIC", "ENTERPRISE", "DEVELOPER"
    ]
    updateTime: str
    version: str
    zone: str

@typing.type_check_only
class ListAvailableVersionsResponse(typing_extensions.TypedDict, total=False):
    availableVersions: _list[Version]
    nextPageToken: str

@typing.type_check_only
class ListDnsPeeringsResponse(typing_extensions.TypedDict, total=False):
    dnsPeerings: _list[DnsPeering]
    nextPageToken: str

@typing.type_check_only
class ListInstancesResponse(typing_extensions.TypedDict, total=False):
    instances: _list[Instance]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListLocationsResponse(typing_extensions.TypedDict, total=False):
    locations: _list[Location]
    nextPageToken: str

@typing.type_check_only
class ListNamespacesResponse(typing_extensions.TypedDict, total=False):
    namespaces: _list[Namespace]
    nextPageToken: str

@typing.type_check_only
class ListOperationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    operations: _list[Operation]

@typing.type_check_only
class Location(typing_extensions.TypedDict, total=False):
    displayName: str
    labels: dict[str, typing.Any]
    locationId: str
    metadata: dict[str, typing.Any]
    name: str

@typing.type_check_only
class Namespace(typing_extensions.TypedDict, total=False):
    iamPolicy: IAMPolicy
    name: str

@typing.type_check_only
class NetworkConfig(typing_extensions.TypedDict, total=False):
    ipAllocation: str
    network: str

@typing.type_check_only
class Operation(typing_extensions.TypedDict, total=False):
    done: bool
    error: Status
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class OperationMetadata(typing_extensions.TypedDict, total=False):
    apiVersion: str
    createTime: str
    endTime: str
    requestedCancellation: bool
    statusDetail: str
    target: str
    verb: str

@typing.type_check_only
class Policy(typing_extensions.TypedDict, total=False):
    auditConfigs: _list[AuditConfig]
    bindings: _list[Binding]
    etag: str
    version: int

@typing.type_check_only
class RemoveIamPolicyRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class RemoveIamPolicyResponse(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class RestartInstanceRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class SetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    policy: Policy
    updateMask: str

@typing.type_check_only
class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class TestIamPermissionsRequest(typing_extensions.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class TestIamPermissionsResponse(typing_extensions.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class UpgradeInstanceRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Version(typing_extensions.TypedDict, total=False):
    availableFeatures: _list[str]
    defaultVersion: bool
    type: typing_extensions.Literal[
        "TYPE_UNSPECIFIED", "TYPE_PREVIEW", "TYPE_GENERAL_AVAILABILITY"
    ]
    versionNumber: str
