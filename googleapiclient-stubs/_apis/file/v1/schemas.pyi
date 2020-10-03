import typing

import typing_extensions

class Instance(typing_extensions.TypedDict, total=False):
    fileShares: typing.List[FileShareConfig]
    labels: typing.Dict[str, typing.Any]
    etag: str
    name: str
    createTime: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "CREATING", "READY", "REPAIRING", "DELETING", "ERROR"
    ]
    description: str
    networks: typing.List[NetworkConfig]
    statusMessage: str
    tier: typing_extensions.Literal[
        "TIER_UNSPECIFIED",
        "STANDARD",
        "PREMIUM",
        "BASIC_HDD",
        "BASIC_SSD",
        "HIGH_SCALE_SSD",
    ]

class CancelOperationRequest(typing_extensions.TypedDict, total=False): ...

class GoogleCloudSaasacceleratorManagementProvidersV1NodeSloMetadata(
    typing_extensions.TypedDict, total=False
):
    exclusions: typing.List[GoogleCloudSaasacceleratorManagementProvidersV1SloExclusion]
    location: str
    nodeId: str

class Empty(typing_extensions.TypedDict, total=False): ...

class ListLocationsResponse(typing_extensions.TypedDict, total=False):
    locations: typing.List[Location]
    nextPageToken: str

class FileShareConfig(typing_extensions.TypedDict, total=False):
    capacityGb: str
    name: str

class Operation(typing_extensions.TypedDict, total=False):
    name: str
    error: Status
    response: typing.Dict[str, typing.Any]
    metadata: typing.Dict[str, typing.Any]
    done: bool

class Location(typing_extensions.TypedDict, total=False):
    name: str
    locationId: str
    metadata: typing.Dict[str, typing.Any]
    labels: typing.Dict[str, typing.Any]
    displayName: str

class GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceSchedule(
    typing_extensions.TypedDict, total=False
):
    rolloutManagementPolicy: str
    endTime: str
    canReschedule: bool
    startTime: str

class ListOperationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    operations: typing.List[Operation]

class Status(typing_extensions.TypedDict, total=False):
    details: typing.List[typing.Dict[str, typing.Any]]
    code: int
    message: str

class GoogleCloudSaasacceleratorManagementProvidersV1Instance(
    typing_extensions.TypedDict, total=False
):
    slmInstanceTemplate: str
    tenantProjectId: str
    createTime: str
    name: str
    maintenanceSchedules: typing.Dict[str, typing.Any]
    consumerDefinedName: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "CREATING",
        "READY",
        "UPDATING",
        "REPAIRING",
        "DELETING",
        "ERROR",
    ]
    maintenancePolicyNames: typing.Dict[str, typing.Any]
    sloMetadata: GoogleCloudSaasacceleratorManagementProvidersV1SloMetadata
    producerMetadata: typing.Dict[str, typing.Any]
    maintenanceSettings: GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceSettings
    softwareVersions: typing.Dict[str, typing.Any]
    updateTime: str
    labels: typing.Dict[str, typing.Any]
    provisionedResources: typing.List[
        GoogleCloudSaasacceleratorManagementProvidersV1ProvisionedResource
    ]

class GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceSettings(
    typing_extensions.TypedDict, total=False
):
    exclude: bool

class GoogleCloudSaasacceleratorManagementProvidersV1SloExclusion(
    typing_extensions.TypedDict, total=False
):
    duration: str
    reason: str
    sliName: str
    startTime: str

class ListInstancesResponse(typing_extensions.TypedDict, total=False):
    unreachable: typing.List[str]
    instances: typing.List[Instance]
    nextPageToken: str

class NetworkConfig(typing_extensions.TypedDict, total=False):
    reservedIpRange: str
    ipAddresses: typing.List[str]
    modes: typing.List[str]
    network: str

class OperationMetadata(typing_extensions.TypedDict, total=False):
    target: str
    cancelRequested: bool
    apiVersion: str
    verb: str
    statusDetail: str
    endTime: str
    createTime: str

class GoogleCloudSaasacceleratorManagementProvidersV1SloMetadata(
    typing_extensions.TypedDict, total=False
):
    exclusions: typing.List[GoogleCloudSaasacceleratorManagementProvidersV1SloExclusion]
    eligibility: GoogleCloudSaasacceleratorManagementProvidersV1SloEligibility
    nodes: typing.List[GoogleCloudSaasacceleratorManagementProvidersV1NodeSloMetadata]
    tier: str

class GoogleCloudSaasacceleratorManagementProvidersV1ProvisionedResource(
    typing_extensions.TypedDict, total=False
):
    resourceType: str
    resourceUrl: str

class GoogleCloudSaasacceleratorManagementProvidersV1SloEligibility(
    typing_extensions.TypedDict, total=False
):
    eligible: bool
    reason: str
