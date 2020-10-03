import typing

import typing_extensions

class MemcacheParameters(typing_extensions.TypedDict, total=False):
    id: str
    params: typing.Dict[str, typing.Any]

class GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceSettings(
    typing_extensions.TypedDict, total=False
):
    exclude: bool

class GoogleCloudSaasacceleratorManagementProvidersV1Instance(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    name: str
    labels: typing.Dict[str, typing.Any]
    maintenanceSchedules: typing.Dict[str, typing.Any]
    producerMetadata: typing.Dict[str, typing.Any]
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "CREATING",
        "READY",
        "UPDATING",
        "REPAIRING",
        "DELETING",
        "ERROR",
    ]
    consumerDefinedName: str
    maintenancePolicyNames: typing.Dict[str, typing.Any]
    softwareVersions: typing.Dict[str, typing.Any]
    slmInstanceTemplate: str
    maintenanceSettings: GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceSettings
    sloMetadata: GoogleCloudSaasacceleratorManagementProvidersV1SloMetadata
    updateTime: str
    provisionedResources: typing.List[
        GoogleCloudSaasacceleratorManagementProvidersV1ProvisionedResource
    ]
    tenantProjectId: str

class ListInstancesResponse(typing_extensions.TypedDict, total=False):
    unreachable: typing.List[str]
    nextPageToken: str
    resources: typing.List[Instance]

class UpdateParametersRequest(typing_extensions.TypedDict, total=False):
    parameters: MemcacheParameters
    updateMask: str

class InstanceMessage(typing_extensions.TypedDict, total=False):
    code: typing_extensions.Literal["CODE_UNSPECIFIED", "ZONE_DISTRIBUTION_UNBALANCED"]
    message: str

class Empty(typing_extensions.TypedDict, total=False): ...

class NodeConfig(typing_extensions.TypedDict, total=False):
    cpuCount: int
    memorySizeMb: int

class ZoneMetadata(typing_extensions.TypedDict, total=False): ...

class Operation(typing_extensions.TypedDict, total=False):
    response: typing.Dict[str, typing.Any]
    done: bool
    error: Status
    metadata: typing.Dict[str, typing.Any]
    name: str

class GoogleCloudSaasacceleratorManagementProvidersV1ProvisionedResource(
    typing_extensions.TypedDict, total=False
):
    resourceUrl: str
    resourceType: str

class ApplyParametersRequest(typing_extensions.TypedDict, total=False):
    nodeIds: typing.List[str]
    applyAll: bool

class GoogleCloudSaasacceleratorManagementProvidersV1SloEligibility(
    typing_extensions.TypedDict, total=False
):
    reason: str
    eligible: bool

class CancelOperationRequest(typing_extensions.TypedDict, total=False): ...

class ListOperationsResponse(typing_extensions.TypedDict, total=False):
    operations: typing.List[Operation]
    nextPageToken: str

class Status(typing_extensions.TypedDict, total=False):
    message: str
    code: int
    details: typing.List[typing.Dict[str, typing.Any]]

class GoogleCloudSaasacceleratorManagementProvidersV1SloExclusion(
    typing_extensions.TypedDict, total=False
):
    duration: str
    sliName: str
    reason: str
    startTime: str

class GoogleCloudMemcacheV1beta2OperationMetadata(
    typing_extensions.TypedDict, total=False
):
    verb: str
    apiVersion: str
    cancelRequested: bool
    createTime: str
    endTime: str
    target: str
    statusDetail: str

class GoogleCloudSaasacceleratorManagementProvidersV1NodeSloMetadata(
    typing_extensions.TypedDict, total=False
):
    location: str
    nodeId: str
    exclusions: typing.List[GoogleCloudSaasacceleratorManagementProvidersV1SloExclusion]

class ListLocationsResponse(typing_extensions.TypedDict, total=False):
    locations: typing.List[Location]
    nextPageToken: str

class GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceSchedule(
    typing_extensions.TypedDict, total=False
):
    endTime: str
    startTime: str
    rolloutManagementPolicy: str
    canReschedule: bool

class Node(typing_extensions.TypedDict, total=False):
    zone: str
    parameters: MemcacheParameters
    port: int
    host: str
    nodeId: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "CREATING", "READY", "DELETING", "UPDATING"
    ]

class GoogleCloudMemcacheV1beta2LocationMetadata(
    typing_extensions.TypedDict, total=False
):
    availableZones: typing.Dict[str, typing.Any]

class GoogleCloudSaasacceleratorManagementProvidersV1SloMetadata(
    typing_extensions.TypedDict, total=False
):
    nodes: typing.List[GoogleCloudSaasacceleratorManagementProvidersV1NodeSloMetadata]
    tier: str
    exclusions: typing.List[GoogleCloudSaasacceleratorManagementProvidersV1SloExclusion]
    eligibility: GoogleCloudSaasacceleratorManagementProvidersV1SloEligibility

class Location(typing_extensions.TypedDict, total=False):
    displayName: str
    locationId: str
    labels: typing.Dict[str, typing.Any]
    metadata: typing.Dict[str, typing.Any]
    name: str

class Instance(typing_extensions.TypedDict, total=False):
    updateTime: str
    memcacheFullVersion: str
    displayName: str
    memcacheNodes: typing.List[Node]
    zones: typing.List[str]
    instanceMessages: typing.List[InstanceMessage]
    parameters: MemcacheParameters
    nodeCount: int
    discoveryEndpoint: str
    nodeConfig: NodeConfig
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "CREATING", "READY", "DELETING", "PERFORMING_MAINTENANCE"
    ]
    createTime: str
    name: str
    memcacheVersion: typing_extensions.Literal[
        "MEMCACHE_VERSION_UNSPECIFIED", "MEMCACHE_1_5"
    ]
    authorizedNetwork: str
    labels: typing.Dict[str, typing.Any]
