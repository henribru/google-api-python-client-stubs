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
    reservationAffinity: ReservationAffinity

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
    reservationAffinity: ReservationAffinity
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
class HttpOptions(typing.TypedDict, total=False):
    allowedUnauthenticatedCorsPreflightRequests: bool
    disableLocalhostReplacement: bool

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
class OAuthToken(typing.TypedDict, total=False):
    accessToken: str
    email: str
    expireTime: str
    expiresIn: str
    scopes: str

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
class PushCredentialsRequest(typing.TypedDict, total=False):
    applicationDefaultCredentials: OAuthToken

@typing.type_check_only
class ReadinessCheck(typing.TypedDict, total=False):
    path: str
    port: int

@typing.type_check_only
class ReservationAffinity(typing.TypedDict, total=False):
    consumeReservationType: typing.Literal[
        "TYPE_UNSPECIFIED", "NO_RESERVATION", "ANY_RESERVATION", "SPECIFIC_RESERVATION"
    ]
    key: str
    values: _list[str]

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
class SuspendWorkstationRequest(typing.TypedDict, total=False):
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
    boostConfigs: _list[WorkstationBoostConfig]
    conditions: _list[Status]
    createTime: str
    degraded: bool
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
    satisfiesPzi: bool
    satisfiesPzs: bool
    sourceWorkstation: str
    startTime: str
    state: typing.Literal[
        "STATE_UNSPECIFIED",
        "STATE_STARTING",
        "STATE_RUNNING",
        "STATE_STOPPING",
        "STATE_STOPPED",
        "STATE_SUSPENDING",
        "STATE_SUSPENDED",
    ]
    uid: str
    updateTime: str

@typing.type_check_only
class WorkstationBoostConfig(typing.TypedDict, total=False):
    id: str
    running: bool

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
    satisfiesPzi: bool
    satisfiesPzs: bool
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
    enablePushingCredentials: bool
    encryptionKey: CustomerEncryptionKey
    ephemeralDirectories: _list[EphemeralDirectory]
    etag: str
    grantWorkstationAdminRoleOnCreate: bool
    host: Host
    httpOptions: HttpOptions
    idleAction: typing.Literal["IDLE_ACTION_UNSPECIFIED", "STOP", "SUSPEND"]
    idleTimeout: str
    labels: dict[str, typing.Any]
    maxUsableWorkstations: int
    name: str
    persistentDirectories: _list[PersistentDirectory]
    readinessChecks: _list[ReadinessCheck]
    reconciling: bool
    replicaZones: _list[str]
    runningTimeout: str
    satisfiesPzi: bool
    satisfiesPzs: bool
    uid: str
    updateTime: str

@typing.type_check_only
class WorkstationPersistentDirectory(typing.TypedDict, total=False):
    mountPath: str
    sizeGb: int
