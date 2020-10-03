import typing

import typing_extensions

class Location(typing_extensions.TypedDict, total=False):
    name: str
    labels: typing.Dict[str, typing.Any]
    locationId: str
    metadata: typing.Dict[str, typing.Any]
    displayName: str

class ListLocationsResponse(typing_extensions.TypedDict, total=False):
    locations: typing.List[Location]
    nextPageToken: str

class CancelOperationRequest(typing_extensions.TypedDict, total=False): ...

class GoogleCloudSaasacceleratorManagementProvidersV1NodeSloMetadata(
    typing_extensions.TypedDict, total=False
):
    nodeId: str
    exclusions: typing.List[GoogleCloudSaasacceleratorManagementProvidersV1SloExclusion]
    location: str

class FileShareConfig(typing_extensions.TypedDict, total=False):
    name: str
    sourceBackup: str
    nfsExportOptions: typing.List[NfsExportOptions]
    capacityGb: str

class GoogleCloudSaasacceleratorManagementProvidersV1Instance(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    labels: typing.Dict[str, typing.Any]
    slmInstanceTemplate: str
    name: str
    maintenanceSettings: GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceSettings
    updateTime: str
    provisionedResources: typing.List[
        GoogleCloudSaasacceleratorManagementProvidersV1ProvisionedResource
    ]
    maintenanceSchedules: typing.Dict[str, typing.Any]
    softwareVersions: typing.Dict[str, typing.Any]
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "CREATING",
        "READY",
        "UPDATING",
        "REPAIRING",
        "DELETING",
        "ERROR",
    ]
    tenantProjectId: str
    producerMetadata: typing.Dict[str, typing.Any]
    maintenancePolicyNames: typing.Dict[str, typing.Any]
    consumerDefinedName: str
    sloMetadata: GoogleCloudSaasacceleratorManagementProvidersV1SloMetadata

class GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceSchedule(
    typing_extensions.TypedDict, total=False
):
    startTime: str
    rolloutManagementPolicy: str
    endTime: str
    canReschedule: bool

class NfsExportOptions(typing_extensions.TypedDict, total=False):
    ipRanges: typing.List[str]
    anonGid: str
    accessMode: typing_extensions.Literal[
        "ACCESS_MODE_UNSPECIFIED", "READ_ONLY", "READ_WRITE"
    ]
    anonUid: str
    squashMode: typing_extensions.Literal[
        "SQUASH_MODE_UNSPECIFIED", "NO_ROOT_SQUASH", "ROOT_SQUASH"
    ]

class Empty(typing_extensions.TypedDict, total=False): ...

class NetworkConfig(typing_extensions.TypedDict, total=False):
    reservedIpRange: str
    ipAddresses: typing.List[str]
    network: str
    modes: typing.List[str]

class Instance(typing_extensions.TypedDict, total=False):
    createTime: str
    statusMessage: str
    fileShares: typing.List[FileShareConfig]
    tier: typing_extensions.Literal[
        "TIER_UNSPECIFIED",
        "STANDARD",
        "PREMIUM",
        "BASIC_HDD",
        "BASIC_SSD",
        "HIGH_SCALE_SSD",
    ]
    description: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "CREATING",
        "READY",
        "REPAIRING",
        "DELETING",
        "ERROR",
        "RESTORING",
    ]
    name: str
    networks: typing.List[NetworkConfig]
    etag: str
    labels: typing.Dict[str, typing.Any]

class Status(typing_extensions.TypedDict, total=False):
    message: str
    code: int
    details: typing.List[typing.Dict[str, typing.Any]]

class RestoreInstanceRequest(typing_extensions.TypedDict, total=False):
    fileShare: str
    sourceSnapshot: str
    sourceBackup: str

class GoogleCloudSaasacceleratorManagementProvidersV1ProvisionedResource(
    typing_extensions.TypedDict, total=False
):
    resourceType: str
    resourceUrl: str

class Backup(typing_extensions.TypedDict, total=False):
    labels: typing.Dict[str, typing.Any]
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "CREATING", "FINALIZING", "READY", "DELETING"
    ]
    downloadBytes: str
    capacityGb: str
    storageBytes: str
    sourceInstance: str
    createTime: str
    name: str
    sourceFileShare: str
    sourceInstanceTier: typing_extensions.Literal[
        "TIER_UNSPECIFIED",
        "STANDARD",
        "PREMIUM",
        "BASIC_HDD",
        "BASIC_SSD",
        "HIGH_SCALE_SSD",
    ]
    description: str

class GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceSettings(
    typing_extensions.TypedDict, total=False
):
    exclude: bool

class GoogleCloudSaasacceleratorManagementProvidersV1SloEligibility(
    typing_extensions.TypedDict, total=False
):
    reason: str
    eligible: bool

class OperationMetadata(typing_extensions.TypedDict, total=False):
    cancelRequested: bool
    createTime: str
    verb: str
    target: str
    endTime: str
    statusDetail: str
    apiVersion: str

class ListOperationsResponse(typing_extensions.TypedDict, total=False):
    operations: typing.List[Operation]
    nextPageToken: str

class GoogleCloudSaasacceleratorManagementProvidersV1SloExclusion(
    typing_extensions.TypedDict, total=False
):
    duration: str
    startTime: str
    sliName: str
    reason: str

class ListInstancesResponse(typing_extensions.TypedDict, total=False):
    instances: typing.List[Instance]
    unreachable: typing.List[str]
    nextPageToken: str

class GoogleCloudSaasacceleratorManagementProvidersV1SloMetadata(
    typing_extensions.TypedDict, total=False
):
    tier: str
    nodes: typing.List[GoogleCloudSaasacceleratorManagementProvidersV1NodeSloMetadata]
    eligibility: GoogleCloudSaasacceleratorManagementProvidersV1SloEligibility
    exclusions: typing.List[GoogleCloudSaasacceleratorManagementProvidersV1SloExclusion]

class Operation(typing_extensions.TypedDict, total=False):
    error: Status
    name: str
    done: bool
    metadata: typing.Dict[str, typing.Any]
    response: typing.Dict[str, typing.Any]

class ListBackupsResponse(typing_extensions.TypedDict, total=False):
    backups: typing.List[Backup]
    nextPageToken: str
    unreachable: typing.List[str]
