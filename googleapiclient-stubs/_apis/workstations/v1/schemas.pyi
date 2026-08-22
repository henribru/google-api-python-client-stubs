import typing

_list = list

@typing.type_check_only
class Accelerator(typing.TypedDict, total=False):
    count: int
    type: str

@typing.type_check_only
class AuditConfig(typing.TypedDict, total=False):
    auditLogConfigs: _list[AuditLogConfig]
    service: str

@typing.type_check_only
class AuditLogConfig(typing.TypedDict, total=False):
    exemptedMembers: _list[str]
    logType: typing.Literal[
        "LOG_TYPE_UNSPECIFIED", "ADMIN_READ", "DATA_WRITE", "DATA_READ"
    ]

@typing.type_check_only
class Binding(typing.TypedDict, total=False):
    condition: Expr
    members: _list[str]
    role: str

@typing.type_check_only
class BoostConfig(typing.TypedDict, total=False):
    accelerators: _list[Accelerator]
    bootDiskSizeGb: int
    enableNestedVirtualization: bool
    id: str
    machineType: str
    poolSize: int

@typing.type_check_only
class CancelOperationRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class Container(typing.TypedDict, total=False):
    args: _list[str]
    command: _list[str]
    env: dict[str, typing.Any]
    image: str
    runAsUser: int
    workingDir: str

@typing.type_check_only
class CustomerEncryptionKey(typing.TypedDict, total=False):
    kmsKey: str
    kmsKeyServiceAccount: str

@typing.type_check_only
class DomainConfig(typing.TypedDict, total=False):
    domain: str

@typing.type_check_only
class EphemeralDirectory(typing.TypedDict, total=False):
    gcePd: GcePersistentDisk
    mountPath: str

@typing.type_check_only
class Expr(typing.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str

@typing.type_check_only
class GatewayConfig(typing.TypedDict, total=False):
    http2Enabled: bool

@typing.type_check_only
class GceConfidentialInstanceConfig(typing.TypedDict, total=False):
    enableConfidentialCompute: bool

@typing.type_check_only
class GceHyperdiskBalancedHighAvailability(typing.TypedDict, total=False):
    archiveTimeout: str
    maxSizeGb: int
    reclaimPolicy: typing.Literal["RECLAIM_POLICY_UNSPECIFIED", "DELETE", "RETAIN"]
    sizeGb: int
    sourceSnapshot: str

@typing.type_check_only
class GceInstance(typing.TypedDict, total=False):
    accelerators: _list[Accelerator]
    boostConfigs: _list[BoostConfig]
    bootDiskSizeGb: int
    confidentialInstanceConfig: GceConfidentialInstanceConfig
    disablePublicIpAddresses: bool
    disableSsh: bool
    enableNestedVirtualization: bool
    instanceMetadata: dict[str, typing.Any]
    machineType: str
    poolSize: int
    pooledInstances: int
    serviceAccount: str
    serviceAccountScopes: _list[str]
    shieldedInstanceConfig: GceShieldedInstanceConfig
    startupScriptUri: str
    tags: _list[str]
    vmTags: dict[str, typing.Any]

@typing.type_check_only
class GceInstanceHost(typing.TypedDict, total=False):
    id: str
    name: str
    zone: str

@typing.type_check_only
class GcePersistentDisk(typing.TypedDict, total=False):
    diskType: str
    readOnly: bool
    sourceImage: str
    sourceSnapshot: str

@typing.type_check_only
class GceRegionalPersistentDisk(typing.TypedDict, total=False):
    archiveTimeout: str
    diskType: str
    fsType: str
    maxSizeGb: int
    reclaimPolicy: typing.Literal["RECLAIM_POLICY_UNSPECIFIED", "DELETE", "RETAIN"]
    sizeGb: int
    sourceSnapshot: str

@typing.type_check_only
class GceShieldedInstanceConfig(typing.TypedDict, total=False):
    enableIntegrityMonitoring: bool
    enableSecureBoot: bool
    enableVtpm: bool

@typing.type_check_only
class GenerateAccessTokenRequest(typing.TypedDict, total=False):
    expireTime: str
    port: int
    ttl: str

@typing.type_check_only
class GenerateAccessTokenResponse(typing.TypedDict, total=False):
    accessToken: str
    expireTime: str

@typing.type_check_only
class GoogleProtobufEmpty(typing.TypedDict, total=False): ...

@typing.type_check_only
class Host(typing.TypedDict, total=False):
    gceInstance: GceInstance

@typing.type_check_only
class ListLocationsResponse(typing.TypedDict, total=False):
    locations: _list[Location]
    nextPageToken: str

@typing.type_check_only
class ListOperationsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    operations: _list[Operation]
    unreachable: _list[str]

@typing.type_check_only
class ListUsableWorkstationConfigsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    unreachable: _list[str]
    workstationConfigs: _list[WorkstationConfig]

@typing.type_check_only
class ListUsableWorkstationsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    unreachable: _list[str]
    workstations: _list[Workstation]

@typing.type_check_only
class ListWorkstationClustersResponse(typing.TypedDict, total=False):
    nextPageToken: str
    unreachable: _list[str]
    workstationClusters: _list[WorkstationCluster]

@typing.type_check_only
class ListWorkstationConfigsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    unreachable: _list[str]
    workstationConfigs: _list[WorkstationConfig]

@typing.type_check_only
class ListWorkstationsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    unreachable: _list[str]
    workstations: _list[Workstation]

@typing.type_check_only
class Location(typing.TypedDict, total=False):
    displayName: str
    labels: dict[str, typing.Any]
    locationId: str
    metadata: dict[str, typing.Any]
    name: str

@typing.type_check_only
class Operation(typing.TypedDict, total=False):
    done: bool
    error: Status
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class OperationMetadata(typing.TypedDict, total=False):
    apiVersion: str
    createTime: str
    endTime: str
    requestedCancellation: bool
    statusMessage: str
    target: str
    verb: str

@typing.type_check_only
class PersistentDirectory(typing.TypedDict, total=False):
    gceHd: GceHyperdiskBalancedHighAvailability
    gcePd: GceRegionalPersistentDisk
    mountPath: str

@typing.type_check_only
class Policy(typing.TypedDict, total=False):
    auditConfigs: _list[AuditConfig]
    bindings: _list[Binding]
    etag: str
    version: int

@typing.type_check_only
class PortRange(typing.TypedDict, total=False):
    first: int
    last: int

@typing.type_check_only
class PrivateClusterConfig(typing.TypedDict, total=False):
    allowedProjects: _list[str]
    clusterHostname: str
    enablePrivateEndpoint: bool
    serviceAttachmentUri: str

@typing.type_check_only
class ReadinessCheck(typing.TypedDict, total=False):
    path: str
    port: int

@typing.type_check_only
class RuntimeHost(typing.TypedDict, total=False):
    gceInstanceHost: GceInstanceHost

@typing.type_check_only
class SetIamPolicyRequest(typing.TypedDict, total=False):
    policy: Policy
    updateMask: str

@typing.type_check_only
class StartWorkstationRequest(typing.TypedDict, total=False):
    boostConfig: str
    etag: str
    validateOnly: bool

@typing.type_check_only
class Status(typing.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class StopWorkstationRequest(typing.TypedDict, total=False):
    etag: str
    validateOnly: bool

@typing.type_check_only
class TestIamPermissionsRequest(typing.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class TestIamPermissionsResponse(typing.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class Workstation(typing.TypedDict, total=False):
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
    persistentDirectories: _list[WorkstationPersistentDirectory]
    reconciling: bool
    runtimeHost: RuntimeHost
    sourceWorkstation: str
    startTime: str
    state: typing.Literal[
        "STATE_UNSPECIFIED",
        "STATE_STARTING",
        "STATE_RUNNING",
        "STATE_STOPPING",
        "STATE_STOPPED",
    ]
    uid: str
    updateTime: str

@typing.type_check_only
class WorkstationCluster(typing.TypedDict, total=False):
    annotations: dict[str, typing.Any]
    conditions: _list[Status]
    controlPlaneIp: str
    createTime: str
    degraded: bool
    deleteTime: str
    displayName: str
    domainConfig: DomainConfig
    etag: str
    gatewayConfig: GatewayConfig
    labels: dict[str, typing.Any]
    name: str
    network: str
    privateClusterConfig: PrivateClusterConfig
    reconciling: bool
    subnetwork: str
    tags: dict[str, typing.Any]
    uid: str
    updateTime: str
    workstationAuthorizationUrl: str
    workstationLaunchUrl: str

@typing.type_check_only
class WorkstationConfig(typing.TypedDict, total=False):
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

@typing.type_check_only
class WorkstationPersistentDirectory(typing.TypedDict, total=False):
    mountPath: str
    sizeGb: int
