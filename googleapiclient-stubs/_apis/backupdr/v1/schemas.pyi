import typing

_list = list

@typing.type_check_only
class AbandonBackupRequest(typing.TypedDict, total=False):
    requestId: str

@typing.type_check_only
class AcceleratorConfig(typing.TypedDict, total=False):
    acceleratorCount: int
    acceleratorType: str

@typing.type_check_only
class AccessConfig(typing.TypedDict, total=False):
    externalIpv6: str
    externalIpv6PrefixLength: int
    name: str
    natIP: str
    networkTier: typing.Literal["NETWORK_TIER_UNSPECIFIED", "PREMIUM", "STANDARD"]
    publicPtrDomainName: str
    setPublicPtr: bool
    type: typing.Literal["ACCESS_TYPE_UNSPECIFIED", "ONE_TO_ONE_NAT", "DIRECT_IPV6"]

@typing.type_check_only
class AdvancedMachineFeatures(typing.TypedDict, total=False):
    enableNestedVirtualization: bool
    enableUefiNetworking: bool
    threadsPerCore: int
    visibleCoreCount: int

@typing.type_check_only
class AliasIpRange(typing.TypedDict, total=False):
    ipCidrRange: str
    subnetworkRangeName: str

@typing.type_check_only
class AllocationAffinity(typing.TypedDict, total=False):
    consumeReservationType: typing.Literal[
        "TYPE_UNSPECIFIED", "NO_RESERVATION", "ANY_RESERVATION", "SPECIFIC_RESERVATION"
    ]
    key: str
    values: _list[str]

@typing.type_check_only
class AlloyDBClusterBackupPlanAssociationProperties(typing.TypedDict, total=False):
    clusterUid: str

@typing.type_check_only
class AlloyDBClusterDataSourceProperties(typing.TypedDict, total=False):
    clusterUid: str
    name: str
    pitrWindows: _list[AlloyDbPitrWindow]

@typing.type_check_only
class AlloyDBClusterDataSourceReferenceProperties(typing.TypedDict, total=False):
    name: str

@typing.type_check_only
class AlloyDbClusterBackupProperties(typing.TypedDict, total=False):
    chainId: str
    databaseVersion: str
    description: str
    storedBytes: str

@typing.type_check_only
class AlloyDbPitrWindow(typing.TypedDict, total=False):
    endTime: str
    logRetentionDays: str
    startTime: str

@typing.type_check_only
class AttachedDisk(typing.TypedDict, total=False):
    autoDelete: bool
    boot: bool
    deviceName: str
    diskEncryptionKey: CustomerEncryptionKey
    diskInterface: typing.Literal[
        "DISK_INTERFACE_UNSPECIFIED", "SCSI", "NVME", "NVDIMM", "ISCSI"
    ]
    diskSizeGb: str
    diskType: str
    diskTypeDeprecated: typing.Literal["DISK_TYPE_UNSPECIFIED", "SCRATCH", "PERSISTENT"]
    guestOsFeature: _list[GuestOsFeature]
    index: str
    initializeParams: InitializeParams
    kind: str
    license: _list[str]
    mode: typing.Literal["DISK_MODE_UNSPECIFIED", "READ_WRITE", "READ_ONLY", "LOCKED"]
    savedState: typing.Literal["DISK_SAVED_STATE_UNSPECIFIED", "PRESERVED"]
    source: str
    type: typing.Literal["DISK_TYPE_UNSPECIFIED", "SCRATCH", "PERSISTENT"]

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
class Backup(typing.TypedDict, total=False):
    alloyDbBackupProperties: AlloyDbClusterBackupProperties
    backupApplianceBackupProperties: BackupApplianceBackupProperties
    backupApplianceLocks: _list[BackupLock]
    backupRetentionInheritance: typing.Literal[
        "BACKUP_RETENTION_INHERITANCE_UNSPECIFIED",
        "INHERIT_VAULT_RETENTION",
        "MATCH_BACKUP_EXPIRE_TIME",
    ]
    backupType: typing.Literal[
        "BACKUP_TYPE_UNSPECIFIED", "SCHEDULED", "ON_DEMAND", "ON_DEMAND_OPERATIONAL"
    ]
    cloudSqlInstanceBackupProperties: CloudSqlInstanceBackupProperties
    computeInstanceBackupProperties: ComputeInstanceBackupProperties
    consistencyTime: str
    createTime: str
    description: str
    diskBackupProperties: DiskBackupProperties
    enforcedRetentionEndTime: str
    etag: str
    expireTime: str
    filestoreInstanceBackupProperties: FilestoreInstanceBackupProperties
    gcpBackupPlanInfo: GCPBackupPlanInfo
    gcpResource: BackupGcpResource
    kmsKeyVersions: _list[str]
    labels: dict[str, typing.Any]
    name: str
    resourceSizeBytes: str
    satisfiesPzi: bool
    satisfiesPzs: bool
    serviceLocks: _list[BackupLock]
    state: typing.Literal[
        "STATE_UNSPECIFIED", "CREATING", "ACTIVE", "DELETING", "ERROR", "UPLOADING"
    ]
    updateTime: str

@typing.type_check_only
class BackupApplianceBackupConfig(typing.TypedDict, total=False):
    applicationName: str
    backupApplianceId: str
    backupApplianceName: str
    hostName: str
    slaId: str
    slpName: str
    sltName: str

@typing.type_check_only
class BackupApplianceBackupProperties(typing.TypedDict, total=False):
    finalizeTime: str
    generationId: int
    recoveryRangeEndTime: str
    recoveryRangeStartTime: str

@typing.type_check_only
class BackupApplianceLockInfo(typing.TypedDict, total=False):
    backupApplianceId: str
    backupApplianceName: str
    backupImage: str
    jobName: str
    lockReason: str
    slaId: str

@typing.type_check_only
class BackupConfigDetails(typing.TypedDict, total=False):
    applicableResource: str
    backupConfigSource: str
    backupConfigSourceDisplayName: str
    backupDrPlanConfig: BackupDrPlanConfig
    backupDrTemplateConfig: BackupDrTemplateConfig
    backupLocations: _list[BackupLocation]
    backupVault: str
    latestSuccessfulBackupTime: str
    pitrSettings: PitrSettings
    state: typing.Literal["STATE_UNSPECIFIED", "ACTIVE", "INACTIVE", "ERROR"]
    type: typing.Literal[
        "TYPE_UNSPECIFIED",
        "CLOUD_SQL_INSTANCE_BACKUP_CONFIG",
        "COMPUTE_ENGINE_RESOURCE_POLICY",
        "BACKUPDR_BACKUP_PLAN",
        "BACKUPDR_TEMPLATE",
    ]

@typing.type_check_only
class BackupConfigInfo(typing.TypedDict, total=False):
    backupApplianceBackupConfig: BackupApplianceBackupConfig
    gcpBackupConfig: GcpBackupConfig
    lastBackupError: Status
    lastBackupState: typing.Literal[
        "LAST_BACKUP_STATE_UNSPECIFIED",
        "FIRST_BACKUP_PENDING",
        "SUCCEEDED",
        "FAILED",
        "PERMISSION_DENIED",
    ]
    lastSuccessfulBackupConsistencyTime: str

@typing.type_check_only
class BackupDrPlanConfig(typing.TypedDict, total=False):
    backupDrPlanRules: _list[BackupDrPlanRule]

@typing.type_check_only
class BackupDrPlanRule(typing.TypedDict, total=False):
    lastSuccessfulBackupTime: str
    ruleId: str

@typing.type_check_only
class BackupDrTemplateConfig(typing.TypedDict, total=False):
    firstPartyManagementUri: str
    thirdPartyManagementUri: str

@typing.type_check_only
class BackupGcpResource(typing.TypedDict, total=False):
    gcpResourcename: str
    location: str
    type: str

@typing.type_check_only
class BackupLocation(typing.TypedDict, total=False):
    locationId: str
    type: typing.Literal["TYPE_UNSPECIFIED", "ZONAL", "REGIONAL", "MULTI_REGIONAL"]

@typing.type_check_only
class BackupLock(typing.TypedDict, total=False):
    backupApplianceLockInfo: BackupApplianceLockInfo
    lockUntilTime: str
    serviceLockInfo: ServiceLockInfo

@typing.type_check_only
class BackupPlan(typing.TypedDict, total=False):
    backupRules: _list[BackupRule]
    backupVault: str
    backupVaultServiceAccount: str
    computeInstanceBackupPlanProperties: ComputeInstanceBackupPlanProperties
    createTime: str
    description: str
    diskBackupPlanProperties: DiskBackupPlanProperties
    etag: str
    labels: dict[str, typing.Any]
    logRetentionDays: str
    maxCustomOnDemandRetentionDays: int
    name: str
    resourceType: str
    revisionId: str
    revisionName: str
    state: typing.Literal[
        "STATE_UNSPECIFIED", "CREATING", "ACTIVE", "DELETING", "INACTIVE", "UPDATING"
    ]
    supportedResourceTypes: _list[str]
    updateTime: str

@typing.type_check_only
class BackupPlanAssociation(typing.TypedDict, total=False):
    alloydbClusterBackupPlanAssociationProperties: (
        AlloyDBClusterBackupPlanAssociationProperties
    )
    backupPlan: str
    backupPlanRevisionId: str
    backupPlanRevisionName: str
    cloudSqlInstanceBackupPlanAssociationProperties: (
        CloudSqlInstanceBackupPlanAssociationProperties
    )
    createTime: str
    dataSource: str
    filestoreInstanceBackupPlanAssociationProperties: (
        FilestoreInstanceBackupPlanAssociationProperties
    )
    name: str
    resource: str
    resourceType: str
    rulesConfigInfo: _list[RuleConfigInfo]
    state: typing.Literal[
        "STATE_UNSPECIFIED", "CREATING", "ACTIVE", "DELETING", "INACTIVE", "UPDATING"
    ]
    updateTime: str

@typing.type_check_only
class BackupPlanRevision(typing.TypedDict, total=False):
    backupPlanSnapshot: BackupPlan
    createTime: str
    name: str
    revisionId: str
    state: typing.Literal[
        "STATE_UNSPECIFIED", "CREATING", "ACTIVE", "DELETING", "INACTIVE"
    ]

@typing.type_check_only
class BackupRule(typing.TypedDict, total=False):
    backupRetentionDays: int
    ruleId: str
    standardSchedule: StandardSchedule

@typing.type_check_only
class BackupVault(typing.TypedDict, total=False):
    accessRestriction: typing.Literal[
        "ACCESS_RESTRICTION_UNSPECIFIED",
        "WITHIN_PROJECT",
        "WITHIN_ORGANIZATION",
        "UNRESTRICTED",
        "WITHIN_ORG_BUT_UNRESTRICTED_FOR_BA",
    ]
    annotations: dict[str, typing.Any]
    backupCount: str
    backupMinimumEnforcedRetentionDuration: str
    backupRetentionInheritance: typing.Literal[
        "BACKUP_RETENTION_INHERITANCE_UNSPECIFIED",
        "INHERIT_VAULT_RETENTION",
        "MATCH_BACKUP_EXPIRE_TIME",
    ]
    createTime: str
    deletable: bool
    description: str
    effectiveTime: str
    encryptionConfig: EncryptionConfig
    etag: str
    labels: dict[str, typing.Any]
    name: str
    serviceAccount: str
    state: typing.Literal[
        "STATE_UNSPECIFIED", "CREATING", "ACTIVE", "DELETING", "ERROR", "UPDATING"
    ]
    totalStoredBytes: str
    uid: str
    updateTime: str

@typing.type_check_only
class BackupWindow(typing.TypedDict, total=False):
    endHourOfDay: int
    startHourOfDay: int

@typing.type_check_only
class Binding(typing.TypedDict, total=False):
    condition: Expr
    members: _list[str]
    role: str

@typing.type_check_only
class CancelOperationRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class CloudSqlInstanceBackupPlanAssociationProperties(typing.TypedDict, total=False):
    instanceCreateTime: str

@typing.type_check_only
class CloudSqlInstanceBackupProperties(typing.TypedDict, total=False):
    databaseInstalledVersion: str
    finalBackup: bool
    instanceCreateTime: str
    instanceDeleteTime: str
    instanceTier: str
    sourceInstance: str

@typing.type_check_only
class CloudSqlInstanceDataSourceProperties(typing.TypedDict, total=False):
    databaseInstalledVersion: str
    instanceCreateTime: str
    instanceTier: str
    name: str

@typing.type_check_only
class CloudSqlInstanceDataSourceReferenceProperties(typing.TypedDict, total=False):
    databaseInstalledVersion: str
    instanceCreateTime: str
    instanceTier: str
    name: str

@typing.type_check_only
class CloudSqlInstanceInitializationConfig(typing.TypedDict, total=False):
    edition: typing.Literal["EDITION_UNSPECIFIED", "ENTERPRISE", "ENTERPRISE_PLUS"]

@typing.type_check_only
class ComputeInstanceBackupPlanProperties(typing.TypedDict, total=False):
    bootDiskOnly: bool
    diskExclusionLabels: DiskExclusionLabels
    guestFlush: bool

@typing.type_check_only
class ComputeInstanceBackupProperties(typing.TypedDict, total=False):
    canIpForward: bool
    description: str
    disk: _list[AttachedDisk]
    excludedDisks: _list[str]
    guestAccelerator: _list[AcceleratorConfig]
    guestFlush: bool
    includedDisks: _list[str]
    keyRevocationActionType: typing.Literal[
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
class ComputeInstanceDataSourceProperties(typing.TypedDict, total=False):
    description: str
    machineType: str
    name: str
    totalDiskCount: str
    totalDiskSizeGb: str

@typing.type_check_only
class ComputeInstanceRestoreProperties(typing.TypedDict, total=False):
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
    keyRevocationActionType: typing.Literal[
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
    privateIpv6GoogleAccess: typing.Literal[
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
class ComputeInstanceTargetEnvironment(typing.TypedDict, total=False):
    project: str
    useProjectServiceAccount: bool
    zone: str

@typing.type_check_only
class ConfidentialInstanceConfig(typing.TypedDict, total=False):
    enableConfidentialCompute: bool

@typing.type_check_only
class CustomerEncryptionKey(typing.TypedDict, total=False):
    kmsKeyName: str
    kmsKeyServiceAccount: str
    rawKey: str
    rsaEncryptedKey: str

@typing.type_check_only
class DataSource(typing.TypedDict, total=False):
    backupBlockedByVaultAccessRestriction: bool
    backupConfigInfo: BackupConfigInfo
    backupCount: str
    configState: typing.Literal["BACKUP_CONFIG_STATE_UNSPECIFIED", "ACTIVE", "PASSIVE"]
    createTime: str
    dataSourceBackupApplianceApplication: DataSourceBackupApplianceApplication
    dataSourceGcpResource: DataSourceGcpResource
    etag: str
    labels: dict[str, typing.Any]
    name: str
    state: typing.Literal[
        "STATE_UNSPECIFIED", "CREATING", "ACTIVE", "DELETING", "ERROR"
    ]
    totalStoredBytes: str
    updateTime: str

@typing.type_check_only
class DataSourceBackupApplianceApplication(typing.TypedDict, total=False):
    applianceId: str
    applicationId: str
    applicationName: str
    backupAppliance: str
    hostId: str
    hostname: str
    type: str

@typing.type_check_only
class DataSourceBackupConfigInfo(typing.TypedDict, total=False):
    lastBackupState: typing.Literal[
        "LAST_BACKUP_STATE_UNSPECIFIED",
        "FIRST_BACKUP_PENDING",
        "SUCCEEDED",
        "FAILED",
        "PERMISSION_DENIED",
    ]
    lastSuccessfulBackupConsistencyTime: str

@typing.type_check_only
class DataSourceGcpResource(typing.TypedDict, total=False):
    alloyDbClusterDatasourceProperties: AlloyDBClusterDataSourceProperties
    cloudSqlInstanceDatasourceProperties: CloudSqlInstanceDataSourceProperties
    computeInstanceDatasourceProperties: ComputeInstanceDataSourceProperties
    diskDatasourceProperties: DiskDataSourceProperties
    filestoreInstanceDatasourceProperties: FilestoreInstanceDataSourceProperties
    gcpResourcename: str
    location: str
    type: str

@typing.type_check_only
class DataSourceGcpResourceInfo(typing.TypedDict, total=False):
    alloyDbClusterProperties: AlloyDBClusterDataSourceReferenceProperties
    cloudSqlInstanceProperties: CloudSqlInstanceDataSourceReferenceProperties
    filestoreInstanceProperties: FilestoreInstanceDataSourceReferenceProperties
    gcpResourcename: str
    location: str
    type: str

@typing.type_check_only
class DataSourceReference(typing.TypedDict, total=False):
    createTime: str
    dataSource: str
    dataSourceBackupConfigInfo: DataSourceBackupConfigInfo
    dataSourceBackupConfigState: typing.Literal[
        "BACKUP_CONFIG_STATE_UNSPECIFIED", "ACTIVE", "PASSIVE"
    ]
    dataSourceBackupCount: str
    dataSourceGcpResourceInfo: DataSourceGcpResourceInfo
    name: str
    totalStoredBytes: str

@typing.type_check_only
class DiskBackupPlanProperties(typing.TypedDict, total=False):
    guestFlush: bool

@typing.type_check_only
class DiskBackupProperties(typing.TypedDict, total=False):
    accessMode: str
    architecture: typing.Literal["ARCHITECTURE_UNSPECIFIED", "X86_64", "ARM64"]
    description: str
    enableConfidentialCompute: bool
    guestFlush: bool
    guestOsFeature: _list[GuestOsFeature]
    labels: dict[str, typing.Any]
    licenses: _list[str]
    physicalBlockSizeBytes: str
    provisionedIops: str
    provisionedThroughput: str
    region: str
    replicaZones: _list[str]
    sizeGb: str
    sourceDisk: str
    storagePool: str
    type: str
    zone: str

@typing.type_check_only
class DiskDataSourceProperties(typing.TypedDict, total=False):
    description: str
    name: str
    sizeGb: str
    type: str

@typing.type_check_only
class DiskExclusionLabels(typing.TypedDict, total=False):
    labels: _list[LabelKeyValPair]

@typing.type_check_only
class DiskRestoreProperties(typing.TypedDict, total=False):
    accessMode: typing.Literal["READ_WRITE_SINGLE", "READ_WRITE_MANY", "READ_ONLY_MANY"]
    architecture: typing.Literal["ARCHITECTURE_UNSPECIFIED", "X86_64", "ARM64"]
    description: str
    diskEncryptionKey: CustomerEncryptionKey
    enableConfidentialCompute: bool
    guestOsFeature: _list[GuestOsFeature]
    labels: dict[str, typing.Any]
    licenses: _list[str]
    name: str
    physicalBlockSizeBytes: str
    provisionedIops: str
    provisionedThroughput: str
    resourceManagerTags: dict[str, typing.Any]
    resourcePolicy: _list[str]
    sizeGb: str
    storagePool: str
    type: str

@typing.type_check_only
class DiskTargetEnvironment(typing.TypedDict, total=False):
    project: str
    useProjectServiceAccount: bool
    zone: str

@typing.type_check_only
class DisplayDevice(typing.TypedDict, total=False):
    enableDisplay: bool

@typing.type_check_only
class Empty(typing.TypedDict, total=False): ...

@typing.type_check_only
class EncryptionConfig(typing.TypedDict, total=False):
    kmsKeyName: str

@typing.type_check_only
class EndTrialRequest(typing.TypedDict, total=False):
    endReason: typing.Literal["END_REASON_UNSPECIFIED", "MOVE_TO_PAID", "DISCONTINUED"]

@typing.type_check_only
class Entry(typing.TypedDict, total=False):
    key: str
    value: str

@typing.type_check_only
class Expr(typing.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str

@typing.type_check_only
class FetchAccessTokenRequest(typing.TypedDict, total=False):
    generationId: int

@typing.type_check_only
class FetchAccessTokenResponse(typing.TypedDict, total=False):
    expireTime: str
    readLocation: str
    token: str
    writeLocation: str

@typing.type_check_only
class FetchBackupPlanAssociationsForResourceTypeResponse(typing.TypedDict, total=False):
    backupPlanAssociations: _list[BackupPlanAssociation]
    nextPageToken: str

@typing.type_check_only
class FetchBackupsForResourceTypeResponse(typing.TypedDict, total=False):
    backups: _list[Backup]
    nextPageToken: str

@typing.type_check_only
class FetchDataSourceReferencesForResourceTypeResponse(typing.TypedDict, total=False):
    dataSourceReferences: _list[DataSourceReference]
    nextPageToken: str

@typing.type_check_only
class FetchMsComplianceMetadataRequest(typing.TypedDict, total=False):
    projectId: str

@typing.type_check_only
class FetchMsComplianceMetadataResponse(typing.TypedDict, total=False):
    isAssuredWorkload: bool

@typing.type_check_only
class FetchResourceBackupConfigsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    resourceBackupConfigs: _list[ResourceBackupConfig]

@typing.type_check_only
class FetchUsableBackupVaultsResponse(typing.TypedDict, total=False):
    backupVaults: _list[BackupVault]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class FilestoreInstanceBackupPlanAssociationProperties(typing.TypedDict, total=False):
    instanceCreateTime: str

@typing.type_check_only
class FilestoreInstanceBackupProperties(typing.TypedDict, total=False):
    sourceInstance: str

@typing.type_check_only
class FilestoreInstanceDataSourceProperties(typing.TypedDict, total=False):
    instanceCreateTime: str
    name: str

@typing.type_check_only
class FilestoreInstanceDataSourceReferenceProperties(typing.TypedDict, total=False):
    instanceCreateTime: str
    name: str

@typing.type_check_only
class FinalizeBackupRequest(typing.TypedDict, total=False):
    backupId: str
    consistencyTime: str
    description: str
    recoveryRangeEndTime: str
    recoveryRangeStartTime: str
    requestId: str
    retentionDuration: str

@typing.type_check_only
class GCPBackupPlanInfo(typing.TypedDict, total=False):
    backupPlan: str
    backupPlanRevisionId: str
    backupPlanRevisionName: str
    backupPlanRuleId: str

@typing.type_check_only
class GcpBackupConfig(typing.TypedDict, total=False):
    backupPlan: str
    backupPlanAssociation: str
    backupPlanDescription: str
    backupPlanRevisionId: str
    backupPlanRevisionName: str
    backupPlanRules: _list[str]

@typing.type_check_only
class GcpResource(typing.TypedDict, total=False):
    gcpResourcename: str
    location: str
    type: str

@typing.type_check_only
class GoogleCloudBackupdrV1OperationMetadata(typing.TypedDict, total=False):
    additionalInfo: dict[str, typing.Any]
    apiVersion: str
    createTime: str
    endTime: str
    requestedCancellation: bool
    statusMessage: str
    target: str
    verb: str

@typing.type_check_only
class GuestOsFeature(typing.TypedDict, total=False):
    type: typing.Literal[
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
class InitializeParams(typing.TypedDict, total=False):
    diskName: str
    replicaZones: _list[str]

@typing.type_check_only
class InitializeServiceRequest(typing.TypedDict, total=False):
    backupPlanLocation: str
    cloudSqlInstanceInitializationConfig: CloudSqlInstanceInitializationConfig
    requestId: str
    resourceType: str
    validateOnly: bool

@typing.type_check_only
class InitiateBackupRequest(typing.TypedDict, total=False):
    backupId: str
    requestId: str

@typing.type_check_only
class InitiateBackupResponse(typing.TypedDict, total=False):
    backup: str
    baseBackupGenerationId: int
    newBackupGenerationId: int

@typing.type_check_only
class InstanceParams(typing.TypedDict, total=False):
    resourceManagerTags: dict[str, typing.Any]

@typing.type_check_only
class LabelKeyValPair(typing.TypedDict, total=False):
    key: str
    value: str

@typing.type_check_only
class ListBackupPlanAssociationsResponse(typing.TypedDict, total=False):
    backupPlanAssociations: _list[BackupPlanAssociation]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListBackupPlanRevisionsResponse(typing.TypedDict, total=False):
    backupPlanRevisions: _list[BackupPlanRevision]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListBackupPlansResponse(typing.TypedDict, total=False):
    backupPlans: _list[BackupPlan]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListBackupVaultsResponse(typing.TypedDict, total=False):
    backupVaults: _list[BackupVault]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListBackupsResponse(typing.TypedDict, total=False):
    backups: _list[Backup]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListDataSourceReferencesResponse(typing.TypedDict, total=False):
    dataSourceReferences: _list[DataSourceReference]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListDataSourcesResponse(typing.TypedDict, total=False):
    dataSources: _list[DataSource]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListLocationsResponse(typing.TypedDict, total=False):
    locations: _list[Location]
    nextPageToken: str

@typing.type_check_only
class ListManagementServersResponse(typing.TypedDict, total=False):
    managementServers: _list[ManagementServer]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListOperationsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    operations: _list[Operation]
    unreachable: _list[str]

@typing.type_check_only
class ListResourceBackupConfigsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    resourceBackupConfigs: _list[ResourceBackupConfig]

@typing.type_check_only
class Location(typing.TypedDict, total=False):
    displayName: str
    labels: dict[str, typing.Any]
    locationId: str
    metadata: dict[str, typing.Any]
    name: str

@typing.type_check_only
class LocationMetadata(typing.TypedDict, total=False):
    unsupportedFeatures: _list[
        typing.Literal[
            "FEATURE_UNSPECIFIED",
            "MANAGEMENT_SERVER",
            "COMPUTE_INSTANCE",
            "PROTECTION_SUMMARY",
            "DISK",
            "CLOUD_SQL",
            "ALLOY_DB",
            "FILESTORE",
            "BV_AF",
            "CEP_MONITORING_COMPUTE_INSTANCE",
            "CEP_MONITORING_DISK",
            "BV_CUSTOM_PROBERS",
            "FT_CUSTOM_PROBERS",
        ]
    ]

@typing.type_check_only
class ManagementServer(typing.TypedDict, total=False):
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
    state: typing.Literal[
        "INSTANCE_STATE_UNSPECIFIED",
        "CREATING",
        "READY",
        "UPDATING",
        "DELETING",
        "REPAIRING",
        "MAINTENANCE",
        "ERROR",
    ]
    type: typing.Literal["INSTANCE_TYPE_UNSPECIFIED", "BACKUP_RESTORE"]
    updateTime: str
    workforceIdentityBasedManagementUri: WorkforceIdentityBasedManagementURI
    workforceIdentityBasedOauth2ClientId: WorkforceIdentityBasedOAuth2ClientID

@typing.type_check_only
class ManagementURI(typing.TypedDict, total=False):
    api: str
    webUi: str

@typing.type_check_only
class Metadata(typing.TypedDict, total=False):
    items: _list[Entry]

@typing.type_check_only
class NetworkConfig(typing.TypedDict, total=False):
    network: str
    peeringMode: typing.Literal["PEERING_MODE_UNSPECIFIED", "PRIVATE_SERVICE_ACCESS"]

@typing.type_check_only
class NetworkInterface(typing.TypedDict, total=False):
    accessConfigs: _list[AccessConfig]
    aliasIpRanges: _list[AliasIpRange]
    internalIpv6PrefixLength: int
    ipv6AccessConfigs: _list[AccessConfig]
    ipv6AccessType: typing.Literal[
        "UNSPECIFIED_IPV6_ACCESS_TYPE", "INTERNAL", "EXTERNAL"
    ]
    ipv6Address: str
    name: str
    network: str
    networkAttachment: str
    networkIP: str
    nicType: typing.Literal["NIC_TYPE_UNSPECIFIED", "VIRTIO_NET", "GVNIC"]
    queueCount: int
    stackType: typing.Literal["STACK_TYPE_UNSPECIFIED", "IPV4_ONLY", "IPV4_IPV6"]
    subnetwork: str

@typing.type_check_only
class NetworkPerformanceConfig(typing.TypedDict, total=False):
    totalEgressBandwidthTier: typing.Literal["TIER_UNSPECIFIED", "DEFAULT", "TIER_1"]

@typing.type_check_only
class NodeAffinity(typing.TypedDict, total=False):
    key: str
    operator: typing.Literal["OPERATOR_UNSPECIFIED", "IN", "NOT_IN"]
    values: _list[str]

@typing.type_check_only
class Operation(typing.TypedDict, total=False):
    done: bool
    error: Status
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class OperationMetadata(typing.TypedDict, total=False):
    additionalInfo: dict[str, typing.Any]
    apiVersion: str
    createTime: str
    endTime: str
    requestedCancellation: bool
    statusMessage: str
    target: str
    verb: str

@typing.type_check_only
class PitrSettings(typing.TypedDict, total=False):
    retentionDays: int

@typing.type_check_only
class Policy(typing.TypedDict, total=False):
    auditConfigs: _list[AuditConfig]
    bindings: _list[Binding]
    etag: str
    version: int

@typing.type_check_only
class RegionDiskTargetEnvironment(typing.TypedDict, total=False):
    project: str
    region: str
    replicaZones: _list[str]
    useProjectServiceAccount: bool

@typing.type_check_only
class RemoveDataSourceRequest(typing.TypedDict, total=False):
    requestId: str

@typing.type_check_only
class ResourceBackupConfig(typing.TypedDict, total=False):
    backupConfigsDetails: _list[BackupConfigDetails]
    backupConfigured: bool
    name: str
    targetResource: str
    targetResourceDisplayName: str
    targetResourceLabels: dict[str, typing.Any]
    targetResourceType: typing.Literal[
        "RESOURCE_TYPE_UNSPECIFIED",
        "CLOUD_SQL_INSTANCE",
        "COMPUTE_ENGINE_VM",
        "COMPUTE_ENGINE_DISK",
        "COMPUTE_ENGINE_REGIONAL_DISK",
        "FILESTORE_INSTANCE",
    ]
    uid: str
    vaulted: bool

@typing.type_check_only
class RestoreBackupRequest(typing.TypedDict, total=False):
    clearOverridesFieldMask: str
    computeInstanceRestoreProperties: ComputeInstanceRestoreProperties
    computeInstanceTargetEnvironment: ComputeInstanceTargetEnvironment
    diskRestoreProperties: DiskRestoreProperties
    diskTargetEnvironment: DiskTargetEnvironment
    regionDiskTargetEnvironment: RegionDiskTargetEnvironment
    requestId: str

@typing.type_check_only
class RestoreBackupResponse(typing.TypedDict, total=False):
    targetResource: TargetResource

@typing.type_check_only
class RuleConfigInfo(typing.TypedDict, total=False):
    lastBackupError: Status
    lastBackupState: typing.Literal[
        "LAST_BACKUP_STATE_UNSPECIFIED",
        "FIRST_BACKUP_PENDING",
        "PERMISSION_DENIED",
        "SUCCEEDED",
        "FAILED",
    ]
    lastSuccessfulBackupConsistencyTime: str
    ruleId: str

@typing.type_check_only
class Scheduling(typing.TypedDict, total=False):
    automaticRestart: bool
    instanceTerminationAction: typing.Literal[
        "INSTANCE_TERMINATION_ACTION_UNSPECIFIED", "DELETE", "STOP"
    ]
    localSsdRecoveryTimeout: SchedulingDuration
    minNodeCpus: int
    nodeAffinities: _list[NodeAffinity]
    onHostMaintenance: typing.Literal[
        "ON_HOST_MAINTENANCE_UNSPECIFIED", "TERMINATE", "MIGRATE"
    ]
    preemptible: bool
    provisioningModel: typing.Literal[
        "PROVISIONING_MODEL_UNSPECIFIED", "STANDARD", "SPOT"
    ]

@typing.type_check_only
class SchedulingDuration(typing.TypedDict, total=False):
    nanos: int
    seconds: str

@typing.type_check_only
class ServiceAccount(typing.TypedDict, total=False):
    email: str
    scopes: _list[str]

@typing.type_check_only
class ServiceLockInfo(typing.TypedDict, total=False):
    operation: str

@typing.type_check_only
class SetIamPolicyRequest(typing.TypedDict, total=False):
    policy: Policy
    updateMask: str

@typing.type_check_only
class SetInternalStatusRequest(typing.TypedDict, total=False):
    backupConfigState: typing.Literal[
        "BACKUP_CONFIG_STATE_UNSPECIFIED", "ACTIVE", "PASSIVE"
    ]
    requestId: str
    value: str

@typing.type_check_only
class SetInternalStatusResponse(typing.TypedDict, total=False): ...

@typing.type_check_only
class StandardSchedule(typing.TypedDict, total=False):
    backupWindow: BackupWindow
    daysOfMonth: _list[int]
    daysOfWeek: _list[
        typing.Literal[
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
        typing.Literal[
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
    recurrenceType: typing.Literal[
        "RECURRENCE_TYPE_UNSPECIFIED", "HOURLY", "DAILY", "WEEKLY", "MONTHLY", "YEARLY"
    ]
    timeZone: str
    weekDayOfMonth: WeekDayOfMonth

@typing.type_check_only
class Status(typing.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class SubscribeTrialRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class Tags(typing.TypedDict, total=False):
    items: _list[str]

@typing.type_check_only
class TargetResource(typing.TypedDict, total=False):
    gcpResource: GcpResource

@typing.type_check_only
class TestIamPermissionsRequest(typing.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class TestIamPermissionsResponse(typing.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class Trial(typing.TypedDict, total=False):
    endReason: typing.Literal["END_REASON_UNSPECIFIED", "MOVE_TO_PAID", "DISCONTINUED"]
    endTime: str
    name: str
    startTime: str
    state: typing.Literal[
        "STATE_UNSPECIFIED",
        "SUBSCRIBED",
        "UNSUBSCRIBED",
        "EXPIRED",
        "ELIGIBLE",
        "NOT_ELIGIBLE",
    ]

@typing.type_check_only
class TriggerBackupRequest(typing.TypedDict, total=False):
    customRetentionDays: int
    labels: dict[str, typing.Any]
    requestId: str
    ruleId: str

@typing.type_check_only
class WeekDayOfMonth(typing.TypedDict, total=False):
    dayOfWeek: typing.Literal[
        "DAY_OF_WEEK_UNSPECIFIED",
        "MONDAY",
        "TUESDAY",
        "WEDNESDAY",
        "THURSDAY",
        "FRIDAY",
        "SATURDAY",
        "SUNDAY",
    ]
    weekOfMonth: typing.Literal[
        "WEEK_OF_MONTH_UNSPECIFIED", "FIRST", "SECOND", "THIRD", "FOURTH", "LAST"
    ]

@typing.type_check_only
class WorkforceIdentityBasedManagementURI(typing.TypedDict, total=False):
    firstPartyManagementUri: str
    thirdPartyManagementUri: str

@typing.type_check_only
class WorkforceIdentityBasedOAuth2ClientID(typing.TypedDict, total=False):
    firstPartyOauth2ClientId: str
    thirdPartyOauth2ClientId: str
