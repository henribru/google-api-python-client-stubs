import typing

import typing_extensions

_list = list

@typing.type_check_only
class AbandonBackupRequest(typing_extensions.TypedDict, total=False):
    requestId: str

@typing.type_check_only
class AcceleratorConfig(typing_extensions.TypedDict, total=False):
    acceleratorCount: int
    acceleratorType: str

@typing.type_check_only
class AccessConfig(typing_extensions.TypedDict, total=False):
    externalIpv6: str
    externalIpv6PrefixLength: int
    name: str
    natIP: str
    networkTier: typing_extensions.Literal[
        "NETWORK_TIER_UNSPECIFIED", "PREMIUM", "STANDARD"
    ]
    publicPtrDomainName: str
    setPublicPtr: bool
    type: typing_extensions.Literal[
        "ACCESS_TYPE_UNSPECIFIED", "ONE_TO_ONE_NAT", "DIRECT_IPV6"
    ]

@typing.type_check_only
class AdvancedMachineFeatures(typing_extensions.TypedDict, total=False):
    enableNestedVirtualization: bool
    enableUefiNetworking: bool
    threadsPerCore: int
    visibleCoreCount: int

@typing.type_check_only
class AliasIpRange(typing_extensions.TypedDict, total=False):
    ipCidrRange: str
    subnetworkRangeName: str

@typing.type_check_only
class AllocationAffinity(typing_extensions.TypedDict, total=False):
    consumeReservationType: typing_extensions.Literal[
        "TYPE_UNSPECIFIED", "NO_RESERVATION", "ANY_RESERVATION", "SPECIFIC_RESERVATION"
    ]
    key: str
    values: _list[str]

@typing.type_check_only
class AttachedDisk(typing_extensions.TypedDict, total=False):
    autoDelete: bool
    boot: bool
    deviceName: str
    diskEncryptionKey: CustomerEncryptionKey
    diskInterface: typing_extensions.Literal[
        "DISK_INTERFACE_UNSPECIFIED", "SCSI", "NVME", "NVDIMM", "ISCSI"
    ]
    diskSizeGb: str
    diskType: str
    diskTypeDeprecated: typing_extensions.Literal[
        "DISK_TYPE_UNSPECIFIED", "SCRATCH", "PERSISTENT"
    ]
    guestOsFeature: _list[GuestOsFeature]
    index: str
    initializeParams: InitializeParams
    kind: str
    license: _list[str]
    mode: typing_extensions.Literal[
        "DISK_MODE_UNSPECIFIED", "READ_WRITE", "READ_ONLY", "LOCKED"
    ]
    savedState: typing_extensions.Literal["DISK_SAVED_STATE_UNSPECIFIED", "PRESERVED"]
    source: str
    type: typing_extensions.Literal["DISK_TYPE_UNSPECIFIED", "SCRATCH", "PERSISTENT"]

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
class Backup(typing_extensions.TypedDict, total=False):
    backupApplianceBackupProperties: BackupApplianceBackupProperties
    backupApplianceLocks: _list[BackupLock]
    backupType: typing_extensions.Literal[
        "BACKUP_TYPE_UNSPECIFIED", "SCHEDULED", "ON_DEMAND"
    ]
    computeInstanceBackupProperties: ComputeInstanceBackupProperties
    consistencyTime: str
    createTime: str
    description: str
    enforcedRetentionEndTime: str
    etag: str
    expireTime: str
    gcpBackupPlanInfo: GCPBackupPlanInfo
    labels: dict[str, typing.Any]
    name: str
    resourceSizeBytes: str
    satisfiesPzi: bool
    satisfiesPzs: bool
    serviceLocks: _list[BackupLock]
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "CREATING", "ACTIVE", "DELETING", "ERROR"
    ]
    updateTime: str

@typing.type_check_only
class BackupApplianceBackupConfig(typing_extensions.TypedDict, total=False):
    applicationName: str
    backupApplianceId: str
    backupApplianceName: str
    hostName: str
    slaId: str
    slpName: str
    sltName: str

@typing.type_check_only
class BackupApplianceBackupProperties(typing_extensions.TypedDict, total=False):
    finalizeTime: str
    generationId: int
    recoveryRangeEndTime: str
    recoveryRangeStartTime: str

@typing.type_check_only
class BackupApplianceLockInfo(typing_extensions.TypedDict, total=False):
    backupApplianceId: str
    backupApplianceName: str
    backupImage: str
    jobName: str
    lockReason: str
    slaId: str

@typing.type_check_only
class BackupConfigInfo(typing_extensions.TypedDict, total=False):
    backupApplianceBackupConfig: BackupApplianceBackupConfig
    gcpBackupConfig: GcpBackupConfig
    lastBackupError: Status
    lastBackupState: typing_extensions.Literal[
        "LAST_BACKUP_STATE_UNSPECIFIED",
        "FIRST_BACKUP_PENDING",
        "SUCCEEDED",
        "FAILED",
        "PERMISSION_DENIED",
    ]
    lastSuccessfulBackupConsistencyTime: str

@typing.type_check_only
class BackupLock(typing_extensions.TypedDict, total=False):
    backupApplianceLockInfo: BackupApplianceLockInfo
    lockUntilTime: str
    serviceLockInfo: ServiceLockInfo

@typing.type_check_only
class BackupPlan(typing_extensions.TypedDict, total=False):
    backupRules: _list[BackupRule]
    backupVault: str
    backupVaultServiceAccount: str
    createTime: str
    description: str
    etag: str
    labels: dict[str, typing.Any]
    name: str
    resourceType: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "CREATING", "ACTIVE", "DELETING", "INACTIVE"
    ]
    updateTime: str

@typing.type_check_only
class BackupPlanAssociation(typing_extensions.TypedDict, total=False):
    backupPlan: str
    createTime: str
    dataSource: str
    name: str
    resource: str
    resourceType: str
    rulesConfigInfo: _list[RuleConfigInfo]
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "CREATING", "ACTIVE", "DELETING", "INACTIVE", "UPDATING"
    ]
    updateTime: str

@typing.type_check_only
class BackupRule(typing_extensions.TypedDict, total=False):
    backupRetentionDays: int
    ruleId: str
    standardSchedule: StandardSchedule

@typing.type_check_only
class BackupVault(typing_extensions.TypedDict, total=False):
    accessRestriction: typing_extensions.Literal[
        "ACCESS_RESTRICTION_UNSPECIFIED",
        "WITHIN_PROJECT",
        "WITHIN_ORGANIZATION",
        "UNRESTRICTED",
        "WITHIN_ORG_BUT_UNRESTRICTED_FOR_BA",
    ]
    annotations: dict[str, typing.Any]
    backupCount: str
    backupMinimumEnforcedRetentionDuration: str
    createTime: str
    deletable: bool
    description: str
    effectiveTime: str
    etag: str
    labels: dict[str, typing.Any]
    name: str
    serviceAccount: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "CREATING", "ACTIVE", "DELETING", "ERROR"
    ]
    totalStoredBytes: str
    uid: str
    updateTime: str

@typing.type_check_only
class BackupWindow(typing_extensions.TypedDict, total=False):
    endHourOfDay: int
    startHourOfDay: int

@typing.type_check_only
class Binding(typing_extensions.TypedDict, total=False):
    condition: Expr
    members: _list[str]
    role: str

@typing.type_check_only
class CancelOperationRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class ComputeInstanceBackupProperties(typing_extensions.TypedDict, total=False):
    canIpForward: bool
    description: str
    disk: _list[AttachedDisk]
    guestAccelerator: _list[AcceleratorConfig]
    keyRevocationActionType: typing_extensions.Literal[
        "KEY_REVOCATION_ACTION_TYPE_UNSPECIFIED", "NONE", "STOP"
    ]
    labels: dict[str, typing.Any]
    machineType: str
    metadata: Metadata
    minCpuPlatform: str
    networkInterface: _list[NetworkInterface]
    scheduling: Scheduling
    serviceAccount: _list[ServiceAccount]
    sourceInstance: str
    tags: Tags

@typing.type_check_only
class ComputeInstanceDataSourceProperties(typing_extensions.TypedDict, total=False):
    description: str
    machineType: str
    name: str
    totalDiskCount: str
    totalDiskSizeGb: str

@typing.type_check_only
class ComputeInstanceRestoreProperties(typing_extensions.TypedDict, total=False):
    advancedMachineFeatures: AdvancedMachineFeatures
    canIpForward: bool
    confidentialInstanceConfig: ConfidentialInstanceConfig
    deletionProtection: bool
    description: str
    disks: _list[AttachedDisk]
    displayDevice: DisplayDevice
    guestAccelerators: _list[AcceleratorConfig]
    hostname: str
    instanceEncryptionKey: CustomerEncryptionKey
    keyRevocationActionType: typing_extensions.Literal[
        "KEY_REVOCATION_ACTION_TYPE_UNSPECIFIED", "NONE", "STOP"
    ]
    labels: dict[str, typing.Any]
    machineType: str
    metadata: Metadata
    minCpuPlatform: str
    name: str
    networkInterfaces: _list[NetworkInterface]
    networkPerformanceConfig: NetworkPerformanceConfig
    params: InstanceParams
    privateIpv6GoogleAccess: typing_extensions.Literal[
        "INSTANCE_PRIVATE_IPV6_GOOGLE_ACCESS_UNSPECIFIED",
        "INHERIT_FROM_SUBNETWORK",
        "ENABLE_OUTBOUND_VM_ACCESS_TO_GOOGLE",
        "ENABLE_BIDIRECTIONAL_ACCESS_TO_GOOGLE",
    ]
    reservationAffinity: AllocationAffinity
    resourcePolicies: _list[str]
    scheduling: Scheduling
    serviceAccounts: _list[ServiceAccount]
    tags: Tags

@typing.type_check_only
class ComputeInstanceTargetEnvironment(typing_extensions.TypedDict, total=False):
    project: str
    zone: str

@typing.type_check_only
class ConfidentialInstanceConfig(typing_extensions.TypedDict, total=False):
    enableConfidentialCompute: bool

@typing.type_check_only
class CustomerEncryptionKey(typing_extensions.TypedDict, total=False):
    kmsKeyName: str
    kmsKeyServiceAccount: str
    rawKey: str
    rsaEncryptedKey: str

@typing.type_check_only
class DataSource(typing_extensions.TypedDict, total=False):
    backupConfigInfo: BackupConfigInfo
    backupCount: str
    configState: typing_extensions.Literal[
        "BACKUP_CONFIG_STATE_UNSPECIFIED", "ACTIVE", "PASSIVE"
    ]
    createTime: str
    dataSourceBackupApplianceApplication: DataSourceBackupApplianceApplication
    dataSourceGcpResource: DataSourceGcpResource
    etag: str
    labels: dict[str, typing.Any]
    name: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "CREATING", "ACTIVE", "DELETING", "ERROR"
    ]
    totalStoredBytes: str
    updateTime: str

@typing.type_check_only
class DataSourceBackupApplianceApplication(typing_extensions.TypedDict, total=False):
    applianceId: str
    applicationId: str
    applicationName: str
    backupAppliance: str
    hostId: str
    hostname: str
    type: str

@typing.type_check_only
class DataSourceGcpResource(typing_extensions.TypedDict, total=False):
    computeInstanceDatasourceProperties: ComputeInstanceDataSourceProperties
    gcpResourcename: str
    location: str
    type: str

@typing.type_check_only
class DisplayDevice(typing_extensions.TypedDict, total=False):
    enableDisplay: bool

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Entry(typing_extensions.TypedDict, total=False):
    key: str
    value: str

@typing.type_check_only
class Expr(typing_extensions.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str

@typing.type_check_only
class FetchAccessTokenRequest(typing_extensions.TypedDict, total=False):
    generationId: int

@typing.type_check_only
class FetchAccessTokenResponse(typing_extensions.TypedDict, total=False):
    expireTime: str
    readLocation: str
    token: str
    writeLocation: str

@typing.type_check_only
class FetchUsableBackupVaultsResponse(typing_extensions.TypedDict, total=False):
    backupVaults: _list[BackupVault]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class FinalizeBackupRequest(typing_extensions.TypedDict, total=False):
    backupId: str
    consistencyTime: str
    description: str
    recoveryRangeEndTime: str
    recoveryRangeStartTime: str
    requestId: str
    retentionDuration: str

@typing.type_check_only
class GCPBackupPlanInfo(typing_extensions.TypedDict, total=False):
    backupPlan: str
    backupPlanRuleId: str

@typing.type_check_only
class GcpBackupConfig(typing_extensions.TypedDict, total=False):
    backupPlan: str
    backupPlanAssociation: str
    backupPlanDescription: str
    backupPlanRules: _list[str]

@typing.type_check_only
class GcpResource(typing_extensions.TypedDict, total=False):
    gcpResourcename: str
    location: str
    type: str

@typing.type_check_only
class GuestOsFeature(typing_extensions.TypedDict, total=False):
    type: typing_extensions.Literal[
        "FEATURE_TYPE_UNSPECIFIED",
        "VIRTIO_SCSI_MULTIQUEUE",
        "WINDOWS",
        "MULTI_IP_SUBNET",
        "UEFI_COMPATIBLE",
        "SECURE_BOOT",
        "GVNIC",
        "SEV_CAPABLE",
        "BARE_METAL_LINUX_COMPATIBLE",
        "SUSPEND_RESUME_COMPATIBLE",
        "SEV_LIVE_MIGRATABLE",
        "SEV_SNP_CAPABLE",
        "TDX_CAPABLE",
        "IDPF",
        "SEV_LIVE_MIGRATABLE_V2",
    ]

@typing.type_check_only
class InitializeParams(typing_extensions.TypedDict, total=False):
    diskName: str
    replicaZones: _list[str]

@typing.type_check_only
class InitializeServiceRequest(typing_extensions.TypedDict, total=False):
    requestId: str
    resourceType: str

@typing.type_check_only
class InitiateBackupRequest(typing_extensions.TypedDict, total=False):
    backupId: str
    requestId: str

@typing.type_check_only
class InitiateBackupResponse(typing_extensions.TypedDict, total=False):
    backup: str
    baseBackupGenerationId: int
    newBackupGenerationId: int

@typing.type_check_only
class InstanceParams(typing_extensions.TypedDict, total=False):
    resourceManagerTags: dict[str, typing.Any]

@typing.type_check_only
class ListBackupPlanAssociationsResponse(typing_extensions.TypedDict, total=False):
    backupPlanAssociations: _list[BackupPlanAssociation]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListBackupPlansResponse(typing_extensions.TypedDict, total=False):
    backupPlans: _list[BackupPlan]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListBackupVaultsResponse(typing_extensions.TypedDict, total=False):
    backupVaults: _list[BackupVault]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListBackupsResponse(typing_extensions.TypedDict, total=False):
    backups: _list[Backup]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListDataSourcesResponse(typing_extensions.TypedDict, total=False):
    dataSources: _list[DataSource]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListLocationsResponse(typing_extensions.TypedDict, total=False):
    locations: _list[Location]
    nextPageToken: str

@typing.type_check_only
class ListManagementServersResponse(typing_extensions.TypedDict, total=False):
    managementServers: _list[ManagementServer]
    nextPageToken: str
    unreachable: _list[str]

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
class ManagementServer(typing_extensions.TypedDict, total=False):
    baProxyUri: _list[str]
    createTime: str
    description: str
    etag: str
    labels: dict[str, typing.Any]
    managementUri: ManagementURI
    name: str
    networks: _list[NetworkConfig]
    oauth2ClientId: str
    satisfiesPzi: bool
    satisfiesPzs: bool
    state: typing_extensions.Literal[
        "INSTANCE_STATE_UNSPECIFIED",
        "CREATING",
        "READY",
        "UPDATING",
        "DELETING",
        "REPAIRING",
        "MAINTENANCE",
        "ERROR",
    ]
    type: typing_extensions.Literal["INSTANCE_TYPE_UNSPECIFIED", "BACKUP_RESTORE"]
    updateTime: str
    workforceIdentityBasedManagementUri: WorkforceIdentityBasedManagementURI
    workforceIdentityBasedOauth2ClientId: WorkforceIdentityBasedOAuth2ClientID

@typing.type_check_only
class ManagementURI(typing_extensions.TypedDict, total=False):
    api: str
    webUi: str

@typing.type_check_only
class Metadata(typing_extensions.TypedDict, total=False):
    items: _list[Entry]

@typing.type_check_only
class NetworkConfig(typing_extensions.TypedDict, total=False):
    network: str
    peeringMode: typing_extensions.Literal[
        "PEERING_MODE_UNSPECIFIED", "PRIVATE_SERVICE_ACCESS"
    ]

@typing.type_check_only
class NetworkInterface(typing_extensions.TypedDict, total=False):
    accessConfigs: _list[AccessConfig]
    aliasIpRanges: _list[AliasIpRange]
    internalIpv6PrefixLength: int
    ipv6AccessConfigs: _list[AccessConfig]
    ipv6AccessType: typing_extensions.Literal[
        "UNSPECIFIED_IPV6_ACCESS_TYPE", "INTERNAL", "EXTERNAL"
    ]
    ipv6Address: str
    name: str
    network: str
    networkAttachment: str
    networkIP: str
    nicType: typing_extensions.Literal["NIC_TYPE_UNSPECIFIED", "VIRTIO_NET", "GVNIC"]
    queueCount: int
    stackType: typing_extensions.Literal[
        "STACK_TYPE_UNSPECIFIED", "IPV4_ONLY", "IPV4_IPV6"
    ]
    subnetwork: str

@typing.type_check_only
class NetworkPerformanceConfig(typing_extensions.TypedDict, total=False):
    totalEgressBandwidthTier: typing_extensions.Literal[
        "TIER_UNSPECIFIED", "DEFAULT", "TIER_1"
    ]

@typing.type_check_only
class NodeAffinity(typing_extensions.TypedDict, total=False):
    key: str
    operator: typing_extensions.Literal["OPERATOR_UNSPECIFIED", "IN", "NOT_IN"]
    values: _list[str]

@typing.type_check_only
class Operation(typing_extensions.TypedDict, total=False):
    done: bool
    error: Status
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class OperationMetadata(typing_extensions.TypedDict, total=False):
    additionalInfo: dict[str, typing.Any]
    apiVersion: str
    createTime: str
    endTime: str
    requestedCancellation: bool
    statusMessage: str
    target: str
    verb: str

@typing.type_check_only
class Policy(typing_extensions.TypedDict, total=False):
    auditConfigs: _list[AuditConfig]
    bindings: _list[Binding]
    etag: str
    version: int

@typing.type_check_only
class RemoveDataSourceRequest(typing_extensions.TypedDict, total=False):
    requestId: str

@typing.type_check_only
class RestoreBackupRequest(typing_extensions.TypedDict, total=False):
    computeInstanceRestoreProperties: ComputeInstanceRestoreProperties
    computeInstanceTargetEnvironment: ComputeInstanceTargetEnvironment
    requestId: str

@typing.type_check_only
class RestoreBackupResponse(typing_extensions.TypedDict, total=False):
    targetResource: TargetResource

@typing.type_check_only
class RuleConfigInfo(typing_extensions.TypedDict, total=False):
    lastBackupError: Status
    lastBackupState: typing_extensions.Literal[
        "LAST_BACKUP_STATE_UNSPECIFIED",
        "FIRST_BACKUP_PENDING",
        "PERMISSION_DENIED",
        "SUCCEEDED",
        "FAILED",
    ]
    lastSuccessfulBackupConsistencyTime: str
    ruleId: str

@typing.type_check_only
class Scheduling(typing_extensions.TypedDict, total=False):
    automaticRestart: bool
    instanceTerminationAction: typing_extensions.Literal[
        "INSTANCE_TERMINATION_ACTION_UNSPECIFIED", "DELETE", "STOP"
    ]
    localSsdRecoveryTimeout: SchedulingDuration
    minNodeCpus: int
    nodeAffinities: _list[NodeAffinity]
    onHostMaintenance: typing_extensions.Literal[
        "ON_HOST_MAINTENANCE_UNSPECIFIED", "TERMINATE", "MIGRATE"
    ]
    preemptible: bool
    provisioningModel: typing_extensions.Literal[
        "PROVISIONING_MODEL_UNSPECIFIED", "STANDARD", "SPOT"
    ]

@typing.type_check_only
class SchedulingDuration(typing_extensions.TypedDict, total=False):
    nanos: int
    seconds: str

@typing.type_check_only
class ServiceAccount(typing_extensions.TypedDict, total=False):
    email: str
    scopes: _list[str]

@typing.type_check_only
class ServiceLockInfo(typing_extensions.TypedDict, total=False):
    operation: str

@typing.type_check_only
class SetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    policy: Policy
    updateMask: str

@typing.type_check_only
class SetInternalStatusRequest(typing_extensions.TypedDict, total=False):
    backupConfigState: typing_extensions.Literal[
        "BACKUP_CONFIG_STATE_UNSPECIFIED", "ACTIVE", "PASSIVE"
    ]
    requestId: str
    value: str

@typing.type_check_only
class SetInternalStatusResponse(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class StandardSchedule(typing_extensions.TypedDict, total=False):
    backupWindow: BackupWindow
    daysOfMonth: _list[int]
    daysOfWeek: _list[
        typing_extensions.Literal[
            "DAY_OF_WEEK_UNSPECIFIED",
            "MONDAY",
            "TUESDAY",
            "WEDNESDAY",
            "THURSDAY",
            "FRIDAY",
            "SATURDAY",
            "SUNDAY",
        ]
    ]
    hourlyFrequency: int
    months: _list[
        typing_extensions.Literal[
            "MONTH_UNSPECIFIED",
            "JANUARY",
            "FEBRUARY",
            "MARCH",
            "APRIL",
            "MAY",
            "JUNE",
            "JULY",
            "AUGUST",
            "SEPTEMBER",
            "OCTOBER",
            "NOVEMBER",
            "DECEMBER",
        ]
    ]
    recurrenceType: typing_extensions.Literal[
        "RECURRENCE_TYPE_UNSPECIFIED", "HOURLY", "DAILY", "WEEKLY", "MONTHLY", "YEARLY"
    ]
    timeZone: str
    weekDayOfMonth: WeekDayOfMonth

@typing.type_check_only
class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class Tags(typing_extensions.TypedDict, total=False):
    items: _list[str]

@typing.type_check_only
class TargetResource(typing_extensions.TypedDict, total=False):
    gcpResource: GcpResource

@typing.type_check_only
class TestIamPermissionsRequest(typing_extensions.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class TestIamPermissionsResponse(typing_extensions.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class TriggerBackupRequest(typing_extensions.TypedDict, total=False):
    requestId: str
    ruleId: str

@typing.type_check_only
class WeekDayOfMonth(typing_extensions.TypedDict, total=False):
    dayOfWeek: typing_extensions.Literal[
        "DAY_OF_WEEK_UNSPECIFIED",
        "MONDAY",
        "TUESDAY",
        "WEDNESDAY",
        "THURSDAY",
        "FRIDAY",
        "SATURDAY",
        "SUNDAY",
    ]
    weekOfMonth: typing_extensions.Literal[
        "WEEK_OF_MONTH_UNSPECIFIED", "FIRST", "SECOND", "THIRD", "FOURTH", "LAST"
    ]

@typing.type_check_only
class WorkforceIdentityBasedManagementURI(typing_extensions.TypedDict, total=False):
    firstPartyManagementUri: str
    thirdPartyManagementUri: str

@typing.type_check_only
class WorkforceIdentityBasedOAuth2ClientID(typing_extensions.TypedDict, total=False):
    firstPartyOauth2ClientId: str
    thirdPartyOauth2ClientId: str
