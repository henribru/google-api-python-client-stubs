import typing

import typing_extensions

_list = list

@typing.type_check_only
class BootDisk(typing_extensions.TypedDict, total=False):
    sizeGb: str
    type: str

@typing.type_check_only
class BucketReference(typing_extensions.TypedDict, total=False):
    bucket: str

@typing.type_check_only
class CancelOperationRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class CheckClusterHealth(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Cluster(typing_extensions.TypedDict, total=False):
    computeResources: dict[str, typing.Any]
    createTime: str
    description: str
    labels: dict[str, typing.Any]
    name: str
    networkResources: dict[str, typing.Any]
    orchestrator: Orchestrator
    reconciling: bool
    storageResources: dict[str, typing.Any]
    updateTime: str

@typing.type_check_only
class ComputeInstance(typing_extensions.TypedDict, total=False):
    instance: str

@typing.type_check_only
class ComputeInstanceSlurmNodeSet(typing_extensions.TypedDict, total=False):
    bootDisk: BootDisk
    labels: dict[str, typing.Any]
    startupScript: str

@typing.type_check_only
class ComputeResource(typing_extensions.TypedDict, total=False):
    config: ComputeResourceConfig

@typing.type_check_only
class ComputeResourceConfig(typing_extensions.TypedDict, total=False):
    newFlexStartInstances: NewFlexStartInstancesConfig
    newOnDemandInstances: NewOnDemandInstancesConfig
    newReservedInstances: NewReservedInstancesConfig
    newSpotInstances: NewSpotInstancesConfig

@typing.type_check_only
class CreateFilestoreInstance(typing_extensions.TypedDict, total=False):
    filestore: str

@typing.type_check_only
class CreateLoginNode(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class CreateLustreInstance(typing_extensions.TypedDict, total=False):
    lustre: str

@typing.type_check_only
class CreateNetwork(typing_extensions.TypedDict, total=False):
    network: str

@typing.type_check_only
class CreateNodeset(typing_extensions.TypedDict, total=False):
    nodesets: _list[str]

@typing.type_check_only
class CreateOrchestrator(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class CreatePartition(typing_extensions.TypedDict, total=False):
    partitions: _list[str]

@typing.type_check_only
class CreatePrivateServiceAccess(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class CreateStorageBucket(typing_extensions.TypedDict, total=False):
    bucket: str

@typing.type_check_only
class DeleteFilestoreInstance(typing_extensions.TypedDict, total=False):
    filestore: str

@typing.type_check_only
class DeleteLoginNode(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class DeleteLustreInstance(typing_extensions.TypedDict, total=False):
    lustre: str

@typing.type_check_only
class DeleteNetwork(typing_extensions.TypedDict, total=False):
    network: str

@typing.type_check_only
class DeleteNodeset(typing_extensions.TypedDict, total=False):
    nodesets: _list[str]

@typing.type_check_only
class DeleteOrchestrator(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class DeletePartition(typing_extensions.TypedDict, total=False):
    partitions: _list[str]

@typing.type_check_only
class DeletePrivateServiceAccess(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class DeleteStorageBucket(typing_extensions.TypedDict, total=False):
    bucket: str

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class ExistingBucketConfig(typing_extensions.TypedDict, total=False):
    bucket: str

@typing.type_check_only
class ExistingFilestoreConfig(typing_extensions.TypedDict, total=False):
    filestore: str

@typing.type_check_only
class ExistingLustreConfig(typing_extensions.TypedDict, total=False):
    lustre: str

@typing.type_check_only
class ExistingNetworkConfig(typing_extensions.TypedDict, total=False):
    network: str
    subnetwork: str

@typing.type_check_only
class FileShareConfig(typing_extensions.TypedDict, total=False):
    capacityGb: str
    fileShare: str

@typing.type_check_only
class FilestoreReference(typing_extensions.TypedDict, total=False):
    filestore: str

@typing.type_check_only
class GcsAutoclassConfig(typing_extensions.TypedDict, total=False):
    enabled: bool
    terminalStorageClass: typing_extensions.Literal[
        "TERMINAL_STORAGE_CLASS_UNSPECIFIED"
    ]

@typing.type_check_only
class GcsHierarchicalNamespaceConfig(typing_extensions.TypedDict, total=False):
    enabled: bool

@typing.type_check_only
class ListClustersResponse(typing_extensions.TypedDict, total=False):
    clusters: _list[Cluster]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListLocationsResponse(typing_extensions.TypedDict, total=False):
    locations: _list[Location]
    nextPageToken: str

@typing.type_check_only
class ListOperationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    operations: _list[Operation]
    unreachable: _list[str]

@typing.type_check_only
class Location(typing_extensions.TypedDict, total=False):
    displayName: str
    labels: dict[str, typing.Any]
    locationId: str
    metadata: dict[str, typing.Any]
    name: str

@typing.type_check_only
class LustreReference(typing_extensions.TypedDict, total=False):
    lustre: str

@typing.type_check_only
class NetworkReference(typing_extensions.TypedDict, total=False):
    network: str
    subnetwork: str

@typing.type_check_only
class NetworkResource(typing_extensions.TypedDict, total=False):
    config: NetworkResourceConfig
    network: NetworkReference

@typing.type_check_only
class NetworkResourceConfig(typing_extensions.TypedDict, total=False):
    existingNetwork: ExistingNetworkConfig
    newNetwork: NewNetworkConfig

@typing.type_check_only
class NewBucketConfig(typing_extensions.TypedDict, total=False):
    autoclass: GcsAutoclassConfig
    bucket: str
    hierarchicalNamespace: GcsHierarchicalNamespaceConfig
    storageClass: typing_extensions.Literal[
        "STORAGE_CLASS_UNSPECIFIED", "STANDARD", "NEARLINE", "COLDLINE", "ARCHIVE"
    ]

@typing.type_check_only
class NewFilestoreConfig(typing_extensions.TypedDict, total=False):
    description: str
    fileShares: _list[FileShareConfig]
    filestore: str
    protocol: typing_extensions.Literal["PROTOCOL_UNSPECIFIED", "NFSV3", "NFSV41"]
    tier: typing_extensions.Literal["TIER_UNSPECIFIED", "ZONAL", "REGIONAL"]

@typing.type_check_only
class NewFlexStartInstancesConfig(typing_extensions.TypedDict, total=False):
    machineType: str
    maxDuration: str
    zone: str

@typing.type_check_only
class NewLustreConfig(typing_extensions.TypedDict, total=False):
    capacityGb: str
    description: str
    filesystem: str
    lustre: str

@typing.type_check_only
class NewNetworkConfig(typing_extensions.TypedDict, total=False):
    description: str
    network: str

@typing.type_check_only
class NewOnDemandInstancesConfig(typing_extensions.TypedDict, total=False):
    machineType: str
    zone: str

@typing.type_check_only
class NewReservedInstancesConfig(typing_extensions.TypedDict, total=False):
    reservation: str

@typing.type_check_only
class NewSpotInstancesConfig(typing_extensions.TypedDict, total=False):
    machineType: str
    terminationAction: typing_extensions.Literal[
        "TERMINATION_ACTION_UNSPECIFIED", "STOP", "DELETE"
    ]
    zone: str

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
    progress: OperationProgress
    requestedCancellation: bool
    target: str
    verb: str

@typing.type_check_only
class OperationProgress(typing_extensions.TypedDict, total=False):
    steps: _list[OperationStep]

@typing.type_check_only
class OperationStep(typing_extensions.TypedDict, total=False):
    checkClusterHealth: CheckClusterHealth
    createFilestoreInstance: CreateFilestoreInstance
    createLoginNode: CreateLoginNode
    createLustreInstance: CreateLustreInstance
    createNetwork: CreateNetwork
    createNodeset: CreateNodeset
    createOrchestrator: CreateOrchestrator
    createPartition: CreatePartition
    createPrivateServiceAccess: CreatePrivateServiceAccess
    createStorageBucket: CreateStorageBucket
    deleteFilestoreInstance: DeleteFilestoreInstance
    deleteLoginNode: DeleteLoginNode
    deleteLustreInstance: DeleteLustreInstance
    deleteNetwork: DeleteNetwork
    deleteNodeset: DeleteNodeset
    deleteOrchestrator: DeleteOrchestrator
    deletePartition: DeletePartition
    deletePrivateServiceAccess: DeletePrivateServiceAccess
    deleteStorageBucket: DeleteStorageBucket
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "WAITING", "IN_PROGRESS", "DONE"
    ]
    updateLoginNode: UpdateLoginNode
    updateNodeset: UpdateNodeset
    updateOrchestrator: UpdateOrchestrator
    updatePartition: UpdatePartition

@typing.type_check_only
class Orchestrator(typing_extensions.TypedDict, total=False):
    slurm: SlurmOrchestrator

@typing.type_check_only
class SlurmLoginNodes(typing_extensions.TypedDict, total=False):
    bootDisk: BootDisk
    count: str
    enableOsLogin: bool
    enablePublicIps: bool
    instances: _list[ComputeInstance]
    labels: dict[str, typing.Any]
    machineType: str
    startupScript: str
    storageConfigs: _list[StorageConfig]
    zone: str

@typing.type_check_only
class SlurmNodeSet(typing_extensions.TypedDict, total=False):
    computeId: str
    computeInstance: ComputeInstanceSlurmNodeSet
    id: str
    maxDynamicNodeCount: str
    staticNodeCount: str
    storageConfigs: _list[StorageConfig]

@typing.type_check_only
class SlurmOrchestrator(typing_extensions.TypedDict, total=False):
    defaultPartition: str
    epilogBashScripts: _list[str]
    loginNodes: SlurmLoginNodes
    nodeSets: _list[SlurmNodeSet]
    partitions: _list[SlurmPartition]
    prologBashScripts: _list[str]

@typing.type_check_only
class SlurmPartition(typing_extensions.TypedDict, total=False):
    id: str
    nodeSetIds: _list[str]

@typing.type_check_only
class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class StorageConfig(typing_extensions.TypedDict, total=False):
    id: str
    localMount: str

@typing.type_check_only
class StorageResource(typing_extensions.TypedDict, total=False):
    bucket: BucketReference
    config: StorageResourceConfig
    filestore: FilestoreReference
    lustre: LustreReference

@typing.type_check_only
class StorageResourceConfig(typing_extensions.TypedDict, total=False):
    existingBucket: ExistingBucketConfig
    existingFilestore: ExistingFilestoreConfig
    existingLustre: ExistingLustreConfig
    newBucket: NewBucketConfig
    newFilestore: NewFilestoreConfig
    newLustre: NewLustreConfig

@typing.type_check_only
class UpdateLoginNode(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class UpdateNodeset(typing_extensions.TypedDict, total=False):
    nodesets: _list[str]

@typing.type_check_only
class UpdateOrchestrator(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class UpdatePartition(typing_extensions.TypedDict, total=False):
    partitions: _list[str]
