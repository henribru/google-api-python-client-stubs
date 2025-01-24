import typing

import typing_extensions

_list = list

@typing.type_check_only
class Accelerator(typing_extensions.TypedDict, total=False):
    count: int
    type: str

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
class BoostConfig(typing_extensions.TypedDict, total=False):
    accelerators: _list[Accelerator]
    bootDiskSizeGb: int
    enableNestedVirtualization: bool
    id: str
    machineType: str
    poolSize: int

@typing.type_check_only
class CancelOperationRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Container(typing_extensions.TypedDict, total=False):
    args: _list[str]
    command: _list[str]
    env: dict[str, typing.Any]
    image: str
    runAsUser: int
    workingDir: str

@typing.type_check_only
class CustomerEncryptionKey(typing_extensions.TypedDict, total=False):
    kmsKey: str
    kmsKeyServiceAccount: str

@typing.type_check_only
class DomainConfig(typing_extensions.TypedDict, total=False):
    domain: str

@typing.type_check_only
class EphemeralDirectory(typing_extensions.TypedDict, total=False):
    gcePd: GcePersistentDisk
    mountPath: str

@typing.type_check_only
class Expr(typing_extensions.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str

@typing.type_check_only
class GceConfidentialInstanceConfig(typing_extensions.TypedDict, total=False):
    enableConfidentialCompute: bool

@typing.type_check_only
class GceInstance(typing_extensions.TypedDict, total=False):
    accelerators: _list[Accelerator]
    boostConfigs: _list[BoostConfig]
    bootDiskSizeGb: int
    confidentialInstanceConfig: GceConfidentialInstanceConfig
    disablePublicIpAddresses: bool
    disableSsh: bool
    enableNestedVirtualization: bool
    machineType: str
    poolSize: int
    pooledInstances: int
    serviceAccount: str
    serviceAccountScopes: _list[str]
    shieldedInstanceConfig: GceShieldedInstanceConfig
    tags: _list[str]
    vmTags: dict[str, typing.Any]

@typing.type_check_only
class GceInstanceHost(typing_extensions.TypedDict, total=False):
    id: str
    name: str
    zone: str

@typing.type_check_only
class GcePersistentDisk(typing_extensions.TypedDict, total=False):
    diskType: str
    readOnly: bool
    sourceImage: str
    sourceSnapshot: str

@typing.type_check_only
class GceRegionalPersistentDisk(typing_extensions.TypedDict, total=False):
    diskType: str
    fsType: str
    reclaimPolicy: typing_extensions.Literal[
        "RECLAIM_POLICY_UNSPECIFIED", "DELETE", "RETAIN"
    ]
    sizeGb: int
    sourceSnapshot: str

@typing.type_check_only
class GceShieldedInstanceConfig(typing_extensions.TypedDict, total=False):
    enableIntegrityMonitoring: bool
    enableSecureBoot: bool
    enableVtpm: bool

@typing.type_check_only
class GenerateAccessTokenRequest(typing_extensions.TypedDict, total=False):
    expireTime: str
    port: int
    ttl: str

@typing.type_check_only
class GenerateAccessTokenResponse(typing_extensions.TypedDict, total=False):
    accessToken: str
    expireTime: str

@typing.type_check_only
class GoogleProtobufEmpty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Host(typing_extensions.TypedDict, total=False):
    gceInstance: GceInstance

@typing.type_check_only
class ListLocationsResponse(typing_extensions.TypedDict, total=False):
    locations: _list[Location]
    nextPageToken: str

@typing.type_check_only
class ListOperationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    operations: _list[Operation]

@typing.type_check_only
class ListUsableWorkstationConfigsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    unreachable: _list[str]
    workstationConfigs: _list[WorkstationConfig]

@typing.type_check_only
class ListUsableWorkstationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    unreachable: _list[str]
    workstations: _list[Workstation]

@typing.type_check_only
class ListWorkstationClustersResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    unreachable: _list[str]
    workstationClusters: _list[WorkstationCluster]

@typing.type_check_only
class ListWorkstationConfigsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    unreachable: _list[str]
    workstationConfigs: _list[WorkstationConfig]

@typing.type_check_only
class ListWorkstationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    unreachable: _list[str]
    workstations: _list[Workstation]

@typing.type_check_only
class Location(typing_extensions.TypedDict, total=False):
    displayName: str
    labels: dict[str, typing.Any]
    locationId: str
    metadata: dict[str, typing.Any]
    name: str

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
    statusMessage: str
    target: str
    verb: str

@typing.type_check_only
class PersistentDirectory(typing_extensions.TypedDict, total=False):
    gcePd: GceRegionalPersistentDisk
    mountPath: str

@typing.type_check_only
class Policy(typing_extensions.TypedDict, total=False):
    auditConfigs: _list[AuditConfig]
    bindings: _list[Binding]
    etag: str
    version: int

@typing.type_check_only
class PortRange(typing_extensions.TypedDict, total=False):
    first: int
    last: int

@typing.type_check_only
class PrivateClusterConfig(typing_extensions.TypedDict, total=False):
    allowedProjects: _list[str]
    clusterHostname: str
    enablePrivateEndpoint: bool
    serviceAttachmentUri: str

@typing.type_check_only
class ReadinessCheck(typing_extensions.TypedDict, total=False):
    path: str
    port: int

@typing.type_check_only
class RuntimeHost(typing_extensions.TypedDict, total=False):
    gceInstanceHost: GceInstanceHost

@typing.type_check_only
class SetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    policy: Policy
    updateMask: str

@typing.type_check_only
class StartWorkstationRequest(typing_extensions.TypedDict, total=False):
    boostConfig: str
    etag: str
    validateOnly: bool

@typing.type_check_only
class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class StopWorkstationRequest(typing_extensions.TypedDict, total=False):
    etag: str
    validateOnly: bool

@typing.type_check_only
class TestIamPermissionsRequest(typing_extensions.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class TestIamPermissionsResponse(typing_extensions.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class Workstation(typing_extensions.TypedDict, total=False):
    annotations: dict[str, typing.Any]
    createTime: str
    deleteTime: str
    displayName: str
    env: dict[str, typing.Any]
    etag: str
    host: str
    kmsKey: str
    labels: dict[str, typing.Any]
    name: str
    reconciling: bool
    runtimeHost: RuntimeHost
    sourceWorkstation: str
    startTime: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "STATE_STARTING",
        "STATE_RUNNING",
        "STATE_STOPPING",
        "STATE_STOPPED",
    ]
    uid: str
    updateTime: str

@typing.type_check_only
class WorkstationCluster(typing_extensions.TypedDict, total=False):
    annotations: dict[str, typing.Any]
    conditions: _list[Status]
    controlPlaneIp: str
    createTime: str
    degraded: bool
    deleteTime: str
    displayName: str
    domainConfig: DomainConfig
    etag: str
    labels: dict[str, typing.Any]
    name: str
    network: str
    privateClusterConfig: PrivateClusterConfig
    reconciling: bool
    subnetwork: str
    tags: dict[str, typing.Any]
    uid: str
    updateTime: str

@typing.type_check_only
class WorkstationConfig(typing_extensions.TypedDict, total=False):
    allowedPorts: _list[PortRange]
    annotations: dict[str, typing.Any]
    conditions: _list[Status]
    container: Container
    createTime: str
    degraded: bool
    deleteTime: str
    disableTcpConnections: bool
    displayName: str
    enableAuditAgent: bool
    encryptionKey: CustomerEncryptionKey
    ephemeralDirectories: _list[EphemeralDirectory]
    etag: str
    grantWorkstationAdminRoleOnCreate: bool
    host: Host
    idleTimeout: str
    labels: dict[str, typing.Any]
    maxUsableWorkstations: int
    name: str
    persistentDirectories: _list[PersistentDirectory]
    readinessChecks: _list[ReadinessCheck]
    reconciling: bool
    replicaZones: _list[str]
    runningTimeout: str
    uid: str
    updateTime: str
