import typing

import typing_extensions
@typing.type_check_only
class Backup(typing_extensions.TypedDict, total=False):
    capacityGb: str
    createTime: str
    description: str
    downloadBytes: str
    labels: typing.Dict[str, typing.Any]
    name: str
    sourceFileShare: str
    sourceInstance: str
    sourceInstanceTier: typing_extensions.Literal[
        "TIER_UNSPECIFIED",
        "STANDARD",
        "PREMIUM",
        "BASIC_HDD",
        "BASIC_SSD",
        "HIGH_SCALE_SSD",
    ]
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "CREATING", "FINALIZING", "READY", "DELETING"
    ]
    storageBytes: str

@typing.type_check_only
class CancelOperationRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class FileShareConfig(typing_extensions.TypedDict, total=False):
    capacityGb: str
    name: str
    nfsExportOptions: typing.List[NfsExportOptions]
    sourceBackup: str

@typing.type_check_only
class GoogleCloudSaasacceleratorManagementProvidersV1Instance(
    typing_extensions.TypedDict, total=False
):
    consumerDefinedName: str
    createTime: str
    labels: typing.Dict[str, typing.Any]
    maintenancePolicyNames: typing.Dict[str, typing.Any]
    maintenanceSchedules: typing.Dict[str, typing.Any]
    maintenanceSettings: GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceSettings
    name: str
    producerMetadata: typing.Dict[str, typing.Any]
    provisionedResources: typing.List[
        GoogleCloudSaasacceleratorManagementProvidersV1ProvisionedResource
    ]
    slmInstanceTemplate: str
    sloMetadata: GoogleCloudSaasacceleratorManagementProvidersV1SloMetadata
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
    updateTime: str

@typing.type_check_only
class GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceSchedule(
    typing_extensions.TypedDict, total=False
):
    canReschedule: bool
    endTime: str
    rolloutManagementPolicy: str
    startTime: str

@typing.type_check_only
class GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceSettings(
    typing_extensions.TypedDict, total=False
):
    exclude: bool

@typing.type_check_only
class GoogleCloudSaasacceleratorManagementProvidersV1NodeSloMetadata(
    typing_extensions.TypedDict, total=False
):
    exclusions: typing.List[GoogleCloudSaasacceleratorManagementProvidersV1SloExclusion]
    location: str
    nodeId: str

@typing.type_check_only
class GoogleCloudSaasacceleratorManagementProvidersV1ProvisionedResource(
    typing_extensions.TypedDict, total=False
):
    resourceType: str
    resourceUrl: str

@typing.type_check_only
class GoogleCloudSaasacceleratorManagementProvidersV1SloEligibility(
    typing_extensions.TypedDict, total=False
):
    eligible: bool
    reason: str

@typing.type_check_only
class GoogleCloudSaasacceleratorManagementProvidersV1SloExclusion(
    typing_extensions.TypedDict, total=False
):
    duration: str
    reason: str
    sliName: str
    startTime: str

@typing.type_check_only
class GoogleCloudSaasacceleratorManagementProvidersV1SloMetadata(
    typing_extensions.TypedDict, total=False
):
    eligibility: GoogleCloudSaasacceleratorManagementProvidersV1SloEligibility
    exclusions: typing.List[GoogleCloudSaasacceleratorManagementProvidersV1SloExclusion]
    nodes: typing.List[GoogleCloudSaasacceleratorManagementProvidersV1NodeSloMetadata]
    tier: str

@typing.type_check_only
class Instance(typing_extensions.TypedDict, total=False):
    createTime: str
    description: str
    etag: str
    fileShares: typing.List[FileShareConfig]
    labels: typing.Dict[str, typing.Any]
    name: str
    networks: typing.List[NetworkConfig]
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "CREATING",
        "READY",
        "REPAIRING",
        "DELETING",
        "ERROR",
        "RESTORING",
    ]
    statusMessage: str
    tier: typing_extensions.Literal[
        "TIER_UNSPECIFIED",
        "STANDARD",
        "PREMIUM",
        "BASIC_HDD",
        "BASIC_SSD",
        "HIGH_SCALE_SSD",
    ]

@typing.type_check_only
class ListBackupsResponse(typing_extensions.TypedDict, total=False):
    backups: typing.List[Backup]
    nextPageToken: str
    unreachable: typing.List[str]

@typing.type_check_only
class ListInstancesResponse(typing_extensions.TypedDict, total=False):
    instances: typing.List[Instance]
    nextPageToken: str
    unreachable: typing.List[str]

@typing.type_check_only
class ListLocationsResponse(typing_extensions.TypedDict, total=False):
    locations: typing.List[Location]
    nextPageToken: str

@typing.type_check_only
class ListOperationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    operations: typing.List[Operation]

@typing.type_check_only
class Location(typing_extensions.TypedDict, total=False):
    displayName: str
    labels: typing.Dict[str, typing.Any]
    locationId: str
    metadata: typing.Dict[str, typing.Any]
    name: str

@typing.type_check_only
class NetworkConfig(typing_extensions.TypedDict, total=False):
    ipAddresses: typing.List[str]
    modes: typing.List[str]
    network: str
    reservedIpRange: str

@typing.type_check_only
class NfsExportOptions(typing_extensions.TypedDict, total=False):
    accessMode: typing_extensions.Literal[
        "ACCESS_MODE_UNSPECIFIED", "READ_ONLY", "READ_WRITE"
    ]
    anonGid: str
    anonUid: str
    ipRanges: typing.List[str]
    squashMode: typing_extensions.Literal[
        "SQUASH_MODE_UNSPECIFIED", "NO_ROOT_SQUASH", "ROOT_SQUASH"
    ]

@typing.type_check_only
class Operation(typing_extensions.TypedDict, total=False):
    done: bool
    error: Status
    metadata: typing.Dict[str, typing.Any]
    name: str
    response: typing.Dict[str, typing.Any]

@typing.type_check_only
class OperationMetadata(typing_extensions.TypedDict, total=False):
    apiVersion: str
    cancelRequested: bool
    createTime: str
    endTime: str
    statusDetail: str
    target: str
    verb: str

@typing.type_check_only
class RestoreInstanceRequest(typing_extensions.TypedDict, total=False):
    fileShare: str
    sourceBackup: str
    sourceSnapshot: str

@typing.type_check_only
class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: typing.List[typing.Dict[str, typing.Any]]
    message: str
