import typing

_list = list

@typing.type_check_only
class ActiveDirectory(typing.TypedDict, total=False):
    administrators: _list[str]
    aesEncryption: bool
    backupOperators: _list[str]
    createTime: str
    description: str
    dns: str
    domain: str
    encryptDcConnections: bool
    kdcHostname: str
    kdcIp: str
    labels: dict[str, typing.Any]
    ldapSigning: bool
    name: str
    netBiosPrefix: str
    nfsUsersWithLdap: bool
    organizationalUnit: str
    password: str
    securityOperators: _list[str]
    site: str
    state: typing.Literal[
        "STATE_UNSPECIFIED",
        "CREATING",
        "READY",
        "UPDATING",
        "IN_USE",
        "DELETING",
        "ERROR",
        "DIAGNOSING",
    ]
    stateDetails: str
    username: str

@typing.type_check_only
class Backup(typing.TypedDict, total=False):
    backupRegion: str
    backupType: typing.Literal["TYPE_UNSPECIFIED", "MANUAL", "SCHEDULED"]
    chainStorageBytes: str
    createTime: str
    description: str
    enforcedRetentionEndTime: str
    labels: dict[str, typing.Any]
    name: str
    ontapSource: OntapSource
    satisfiesPzi: bool
    satisfiesPzs: bool
    sourceSnapshot: str
    sourceVolume: str
    state: typing.Literal[
        "STATE_UNSPECIFIED",
        "CREATING",
        "UPLOADING",
        "READY",
        "DELETING",
        "ERROR",
        "UPDATING",
    ]
    volumeRegion: str
    volumeUsageBytes: str

@typing.type_check_only
class BackupConfig(typing.TypedDict, total=False):
    backupChainBytes: str
    backupPolicies: _list[str]
    backupVault: str
    scheduledBackupEnabled: bool

@typing.type_check_only
class BackupPolicy(typing.TypedDict, total=False):
    assignedVolumeCount: int
    createTime: str
    dailyBackupLimit: int
    description: str
    enabled: bool
    labels: dict[str, typing.Any]
    monthlyBackupLimit: int
    name: str
    state: typing.Literal[
        "STATE_UNSPECIFIED", "CREATING", "READY", "DELETING", "ERROR", "UPDATING"
    ]
    weeklyBackupLimit: int

@typing.type_check_only
class BackupRetentionPolicy(typing.TypedDict, total=False):
    backupMinimumEnforcedRetentionDays: int
    dailyBackupImmutable: bool
    manualBackupImmutable: bool
    monthlyBackupImmutable: bool
    weeklyBackupImmutable: bool

@typing.type_check_only
class BackupSource(typing.TypedDict, total=False):
    backup: str
    fileList: _list[str]

@typing.type_check_only
class BackupVault(typing.TypedDict, total=False):
    backupRegion: str
    backupRetentionPolicy: BackupRetentionPolicy
    backupVaultType: typing.Literal[
        "BACKUP_VAULT_TYPE_UNSPECIFIED", "IN_REGION", "CROSS_REGION"
    ]
    backupsCryptoKeyVersion: str
    createTime: str
    description: str
    destinationBackupVault: str
    encryptionState: typing.Literal[
        "ENCRYPTION_STATE_UNSPECIFIED",
        "ENCRYPTION_STATE_PENDING",
        "ENCRYPTION_STATE_COMPLETED",
        "ENCRYPTION_STATE_IN_PROGRESS",
        "ENCRYPTION_STATE_FAILED",
    ]
    kmsConfig: str
    labels: dict[str, typing.Any]
    name: str
    sourceBackupVault: str
    sourceRegion: str
    state: typing.Literal[
        "STATE_UNSPECIFIED", "CREATING", "READY", "DELETING", "ERROR", "UPDATING"
    ]

@typing.type_check_only
class BlockDevice(typing.TypedDict, total=False):
    hostGroups: _list[str]
    identifier: str
    name: str
    osType: typing.Literal["OS_TYPE_UNSPECIFIED", "LINUX", "WINDOWS", "ESXI"]
    sizeGib: str

@typing.type_check_only
class CacheConfig(typing.TypedDict, total=False):
    cachePrePopulate: CachePrePopulate
    cachePrePopulateState: typing.Literal[
        "CACHE_PRE_POPULATE_STATE_UNSPECIFIED",
        "NOT_NEEDED",
        "IN_PROGRESS",
        "COMPLETE",
        "ERROR",
    ]
    cifsChangeNotifyEnabled: bool
    writebackEnabled: bool

@typing.type_check_only
class CacheParameters(typing.TypedDict, total=False):
    cacheConfig: CacheConfig
    cacheState: typing.Literal[
        "CACHE_STATE_UNSPECIFIED",
        "PENDING_CLUSTER_PEERING",
        "PENDING_SVM_PEERING",
        "PEERED",
        "ERROR",
    ]
    command: str
    enableGlobalFileLock: bool
    passphrase: str
    peerClusterName: str
    peerIpAddresses: _list[str]
    peerSvmName: str
    peerVolumeName: str
    peeringCommandExpiryTime: str
    stateDetails: str

@typing.type_check_only
class CachePrePopulate(typing.TypedDict, total=False):
    excludePathList: _list[str]
    pathList: _list[str]
    recursion: bool

@typing.type_check_only
class CancelOperationRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class CloneDetails(typing.TypedDict, total=False):
    sharedSpaceGib: str
    sourceSnapshot: str
    sourceVolume: str
    splitState: typing.Literal[
        "SPLIT_STATE_UNSPECIFIED",
        "SPLIT_STATE_NOT_SPLITTING",
        "SPLIT_STATE_IN_PROGRESS",
        "SPLIT_STATE_FAILED",
    ]

@typing.type_check_only
class DailySchedule(typing.TypedDict, total=False):
    hour: float
    minute: float
    snapshotsToKeep: float

@typing.type_check_only
class DestinationVolumeParameters(typing.TypedDict, total=False):
    description: str
    shareName: str
    storagePool: str
    tieringPolicy: TieringPolicy
    volumeId: str

@typing.type_check_only
class EncryptVolumesRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class EstablishPeeringRequest(typing.TypedDict, total=False):
    peerClusterName: str
    peerIpAddresses: _list[str]
    peerSvmName: str
    peerVolumeName: str

@typing.type_check_only
class EstablishVolumePeeringRequest(typing.TypedDict, total=False):
    peerClusterName: str
    peerIpAddresses: _list[str]
    peerSvmName: str
    peerVolumeName: str

@typing.type_check_only
class ExecuteOntapDeleteResponse(typing.TypedDict, total=False):
    body: dict[str, typing.Any]

@typing.type_check_only
class ExecuteOntapGetResponse(typing.TypedDict, total=False):
    body: dict[str, typing.Any]

@typing.type_check_only
class ExecuteOntapPatchRequest(typing.TypedDict, total=False):
    body: dict[str, typing.Any]

@typing.type_check_only
class ExecuteOntapPatchResponse(typing.TypedDict, total=False):
    body: dict[str, typing.Any]

@typing.type_check_only
class ExecuteOntapPostRequest(typing.TypedDict, total=False):
    body: dict[str, typing.Any]

@typing.type_check_only
class ExecuteOntapPostResponse(typing.TypedDict, total=False):
    body: dict[str, typing.Any]

@typing.type_check_only
class ExportPolicy(typing.TypedDict, total=False):
    rules: _list[SimpleExportPolicyRule]

@typing.type_check_only
class GoogleProtobufEmpty(typing.TypedDict, total=False): ...

@typing.type_check_only
class HostGroup(typing.TypedDict, total=False):
    createTime: str
    description: str
    hosts: _list[str]
    labels: dict[str, typing.Any]
    name: str
    osType: typing.Literal["OS_TYPE_UNSPECIFIED", "LINUX", "WINDOWS", "ESXI"]
    state: typing.Literal[
        "STATE_UNSPECIFIED", "CREATING", "READY", "UPDATING", "DELETING", "DISABLED"
    ]
    type: typing.Literal["TYPE_UNSPECIFIED", "ISCSI_INITIATOR"]

@typing.type_check_only
class HourlySchedule(typing.TypedDict, total=False):
    minute: float
    snapshotsToKeep: float

@typing.type_check_only
class HybridPeeringDetails(typing.TypedDict, total=False):
    command: str
    commandExpiryTime: str
    passphrase: str
    peerClusterName: str
    peerSvmName: str
    peerVolumeName: str
    subnetIp: str

@typing.type_check_only
class HybridReplicationParameters(typing.TypedDict, total=False):
    clusterLocation: str
    description: str
    hybridReplicationType: typing.Literal[
        "VOLUME_HYBRID_REPLICATION_TYPE_UNSPECIFIED",
        "MIGRATION",
        "CONTINUOUS_REPLICATION",
        "ONPREM_REPLICATION",
        "REVERSE_ONPREM_REPLICATION",
    ]
    labels: dict[str, typing.Any]
    largeVolumeConstituentCount: int
    peerClusterName: str
    peerIpAddresses: _list[str]
    peerSvmName: str
    peerVolumeName: str
    replication: str
    replicationSchedule: typing.Literal[
        "HYBRID_REPLICATION_SCHEDULE_UNSPECIFIED", "EVERY_10_MINUTES", "HOURLY", "DAILY"
    ]

@typing.type_check_only
class KmsConfig(typing.TypedDict, total=False):
    createTime: str
    cryptoKeyName: str
    description: str
    instructions: str
    labels: dict[str, typing.Any]
    name: str
    serviceAccount: str
    state: typing.Literal[
        "STATE_UNSPECIFIED",
        "READY",
        "CREATING",
        "DELETING",
        "UPDATING",
        "IN_USE",
        "ERROR",
        "KEY_CHECK_PENDING",
        "KEY_NOT_REACHABLE",
        "DISABLING",
        "DISABLED",
        "MIGRATING",
    ]
    stateDetails: str

@typing.type_check_only
class LargeCapacityConfig(typing.TypedDict, total=False):
    constituentCount: int

@typing.type_check_only
class ListActiveDirectoriesResponse(typing.TypedDict, total=False):
    activeDirectories: _list[ActiveDirectory]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListBackupConfigsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    unreachable: _list[str]
    volumeBackupConfigs: _list[VolumeBackupConfig]

@typing.type_check_only
class ListBackupPoliciesResponse(typing.TypedDict, total=False):
    backupPolicies: _list[BackupPolicy]
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
class ListHostGroupsResponse(typing.TypedDict, total=False):
    hostGroups: _list[HostGroup]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListKmsConfigsResponse(typing.TypedDict, total=False):
    kmsConfigs: _list[KmsConfig]
    nextPageToken: str
    unreachable: _list[str]

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
class ListQuotaRulesResponse(typing.TypedDict, total=False):
    nextPageToken: str
    quotaRules: _list[QuotaRule]
    unreachable: _list[str]

@typing.type_check_only
class ListReplicationsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    replications: _list[Replication]
    unreachable: _list[str]

@typing.type_check_only
class ListSnapshotsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    snapshots: _list[Snapshot]
    unreachable: _list[str]

@typing.type_check_only
class ListStoragePoolsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    storagePools: _list[StoragePool]
    unreachable: _list[str]

@typing.type_check_only
class ListVolumesResponse(typing.TypedDict, total=False):
    nextPageToken: str
    unreachable: _list[str]
    volumes: _list[Volume]

@typing.type_check_only
class Location(typing.TypedDict, total=False):
    displayName: str
    labels: dict[str, typing.Any]
    locationId: str
    metadata: dict[str, typing.Any]
    name: str

@typing.type_check_only
class LocationMetadata(typing.TypedDict, total=False):
    flexPerformanceTier: typing.Literal["FLEX_PERFORMANCE_TIER_UNSPECIFIED", "LIMITED"]
    hasOntapProxy: bool
    hasVcp: bool
    supportedFlexPerformance: _list[
        typing.Literal[
            "FLEX_PERFORMANCE_UNSPECIFIED",
            "FLEX_PERFORMANCE_DEFAULT",
            "FLEX_PERFORMANCE_CUSTOM",
        ]
    ]
    supportedServiceLevels: _list[
        typing.Literal[
            "SERVICE_LEVEL_UNSPECIFIED", "PREMIUM", "EXTREME", "STANDARD", "FLEX"
        ]
    ]

@typing.type_check_only
class MonthlySchedule(typing.TypedDict, total=False):
    daysOfMonth: str
    hour: float
    minute: float
    snapshotsToKeep: float

@typing.type_check_only
class MountOption(typing.TypedDict, total=False):
    export: str
    exportFull: str
    instructions: str
    ipAddress: str
    protocol: typing.Literal[
        "PROTOCOLS_UNSPECIFIED", "NFSV3", "NFSV4", "SMB", "ISCSI", "NVME"
    ]

@typing.type_check_only
class OntapSource(typing.TypedDict, total=False):
    snapshotUuid: str
    storagePool: str
    volumeUuid: str

@typing.type_check_only
class OntapVolumeTarget(typing.TypedDict, total=False):
    restoreDestinationPath: str
    volumeUuid: str

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
class QuotaRule(typing.TypedDict, total=False):
    createTime: str
    description: str
    diskLimitMib: int
    labels: dict[str, typing.Any]
    name: str
    state: typing.Literal[
        "STATE_UNSPECIFIED", "CREATING", "UPDATING", "DELETING", "READY", "ERROR"
    ]
    stateDetails: str
    target: str
    type: typing.Literal[
        "TYPE_UNSPECIFIED",
        "INDIVIDUAL_USER_QUOTA",
        "INDIVIDUAL_GROUP_QUOTA",
        "DEFAULT_USER_QUOTA",
        "DEFAULT_GROUP_QUOTA",
    ]

@typing.type_check_only
class Replication(typing.TypedDict, total=False):
    clusterLocation: str
    createTime: str
    description: str
    destinationVolume: str
    destinationVolumeParameters: DestinationVolumeParameters
    healthy: bool
    hybridPeeringDetails: HybridPeeringDetails
    hybridReplicationType: typing.Literal[
        "HYBRID_REPLICATION_TYPE_UNSPECIFIED",
        "MIGRATION",
        "CONTINUOUS_REPLICATION",
        "ONPREM_REPLICATION",
        "REVERSE_ONPREM_REPLICATION",
    ]
    hybridReplicationUserCommands: UserCommands
    labels: dict[str, typing.Any]
    mirrorState: typing.Literal[
        "MIRROR_STATE_UNSPECIFIED",
        "PREPARING",
        "MIRRORED",
        "STOPPED",
        "TRANSFERRING",
        "BASELINE_TRANSFERRING",
        "ABORTED",
        "EXTERNALLY_MANAGED",
        "PENDING_PEERING",
    ]
    name: str
    replicationSchedule: typing.Literal[
        "REPLICATION_SCHEDULE_UNSPECIFIED", "EVERY_10_MINUTES", "HOURLY", "DAILY"
    ]
    role: typing.Literal["REPLICATION_ROLE_UNSPECIFIED", "SOURCE", "DESTINATION"]
    sourceVolume: str
    state: typing.Literal[
        "STATE_UNSPECIFIED",
        "CREATING",
        "READY",
        "UPDATING",
        "DELETING",
        "ERROR",
        "PENDING_CLUSTER_PEERING",
        "PENDING_SVM_PEERING",
        "PENDING_REMOTE_RESYNC",
        "EXTERNALLY_MANAGED_REPLICATION",
    ]
    stateDetails: str
    transferStats: TransferStats

@typing.type_check_only
class RestoreBackupFilesRequest(typing.TypedDict, total=False):
    backup: str
    fileList: _list[str]
    restoreDestinationPath: str

@typing.type_check_only
class RestoreParameters(typing.TypedDict, total=False):
    sourceBackup: str
    sourceSnapshot: str

@typing.type_check_only
class RestoreVolumeRequest(typing.TypedDict, total=False):
    backupSource: BackupSource
    ontapVolumeTarget: OntapVolumeTarget

@typing.type_check_only
class ResumeReplicationRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class ReverseReplicationDirectionRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class RevertVolumeRequest(typing.TypedDict, total=False):
    snapshotId: str

@typing.type_check_only
class SimpleExportPolicyRule(typing.TypedDict, total=False):
    accessType: typing.Literal[
        "ACCESS_TYPE_UNSPECIFIED", "READ_ONLY", "READ_WRITE", "READ_NONE"
    ]
    allowedClients: str
    anonUid: str
    hasRootAccess: str
    kerberos5ReadOnly: bool
    kerberos5ReadWrite: bool
    kerberos5iReadOnly: bool
    kerberos5iReadWrite: bool
    kerberos5pReadOnly: bool
    kerberos5pReadWrite: bool
    nfsv3: bool
    nfsv4: bool
    squashMode: typing.Literal[
        "SQUASH_MODE_UNSPECIFIED", "NO_ROOT_SQUASH", "ROOT_SQUASH", "ALL_SQUASH"
    ]

@typing.type_check_only
class Snapshot(typing.TypedDict, total=False):
    createTime: str
    description: str
    labels: dict[str, typing.Any]
    name: str
    state: typing.Literal[
        "STATE_UNSPECIFIED",
        "READY",
        "CREATING",
        "DELETING",
        "UPDATING",
        "DISABLED",
        "ERROR",
    ]
    stateDetails: str
    usedBytes: float

@typing.type_check_only
class SnapshotPolicy(typing.TypedDict, total=False):
    dailySchedule: DailySchedule
    enabled: bool
    hourlySchedule: HourlySchedule
    monthlySchedule: MonthlySchedule
    weeklySchedule: WeeklySchedule

@typing.type_check_only
class SplitStatus(typing.TypedDict, total=False):
    progressPercent: int
    splitState: typing.Literal[
        "SPLIT_STATE_UNSPECIFIED",
        "SPLIT_STATE_NOT_SPLITTING",
        "SPLIT_STATE_IN_PROGRESS",
        "SPLIT_STATE_FAILED",
    ]
    stateDetails: str

@typing.type_check_only
class StartSplitRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class Status(typing.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class StopReplicationRequest(typing.TypedDict, total=False):
    force: bool

@typing.type_check_only
class StoragePool(typing.TypedDict, total=False):
    activeDirectory: str
    allowAutoTiering: bool
    availableThroughputMibps: float
    capacityGib: str
    coldTierSizeUsedGib: str
    createTime: str
    customPerformanceEnabled: bool
    description: str
    enableHotTierAutoResize: bool
    encryptionType: typing.Literal[
        "ENCRYPTION_TYPE_UNSPECIFIED", "SERVICE_MANAGED", "CLOUD_KMS"
    ]
    globalAccessAllowed: bool
    hotTierSizeGib: str
    hotTierSizeUsedGib: str
    kmsConfig: str
    labels: dict[str, typing.Any]
    ldapEnabled: bool
    mode: typing.Literal["MODE_UNSPECIFIED", "DEFAULT", "ONTAP"]
    name: str
    network: str
    psaRange: str
    qosType: typing.Literal["QOS_TYPE_UNSPECIFIED", "AUTO", "MANUAL"]
    replicaZone: str
    satisfiesPzi: bool
    satisfiesPzs: bool
    scaleType: typing.Literal[
        "SCALE_TYPE_UNSPECIFIED", "SCALE_TYPE_DEFAULT", "SCALE_TYPE_SCALEOUT"
    ]
    serviceLevel: typing.Literal[
        "SERVICE_LEVEL_UNSPECIFIED", "PREMIUM", "EXTREME", "STANDARD", "FLEX"
    ]
    state: typing.Literal[
        "STATE_UNSPECIFIED",
        "READY",
        "CREATING",
        "DELETING",
        "UPDATING",
        "RESTORING",
        "DISABLED",
        "ERROR",
    ]
    stateDetails: str
    totalIops: str
    totalThroughputMibps: str
    type: typing.Literal["STORAGE_POOL_TYPE_UNSPECIFIED", "FILE", "UNIFIED"]
    volumeCapacityGib: str
    volumeCount: int
    zone: str

@typing.type_check_only
class SwitchActiveReplicaZoneRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class SyncReplicationRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class TieringPolicy(typing.TypedDict, total=False):
    coolingThresholdDays: int
    hotTierBypassModeEnabled: bool
    tierAction: typing.Literal["TIER_ACTION_UNSPECIFIED", "ENABLED", "PAUSED"]

@typing.type_check_only
class TransferStats(typing.TypedDict, total=False):
    lagDuration: str
    lastTransferBytes: str
    lastTransferDuration: str
    lastTransferEndTime: str
    lastTransferError: str
    totalTransferDuration: str
    transferBytes: str
    updateTime: str

@typing.type_check_only
class UpdateBackupConfigRequest(typing.TypedDict, total=False):
    backupConfig: BackupConfig
    updateMask: str
    volumeUuid: str

@typing.type_check_only
class UserCommands(typing.TypedDict, total=False):
    commands: _list[str]

@typing.type_check_only
class ValidateDirectoryServiceRequest(typing.TypedDict, total=False):
    directoryServiceType: typing.Literal[
        "DIRECTORY_SERVICE_TYPE_UNSPECIFIED", "ACTIVE_DIRECTORY"
    ]

@typing.type_check_only
class VerifyKmsConfigRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class VerifyKmsConfigResponse(typing.TypedDict, total=False):
    healthError: str
    healthy: bool
    instructions: str

@typing.type_check_only
class Volume(typing.TypedDict, total=False):
    activeDirectory: str
    backupConfig: BackupConfig
    blockDevices: _list[BlockDevice]
    cacheParameters: CacheParameters
    capacityGib: str
    cloneDetails: CloneDetails
    coldTierSizeGib: str
    createTime: str
    description: str
    encryptionType: typing.Literal[
        "ENCRYPTION_TYPE_UNSPECIFIED", "SERVICE_MANAGED", "CLOUD_KMS"
    ]
    exportPolicy: ExportPolicy
    hasReplication: bool
    hotTierSizeUsedGib: str
    hybridReplicationParameters: HybridReplicationParameters
    kerberosEnabled: bool
    kmsConfig: str
    labels: dict[str, typing.Any]
    largeCapacity: bool
    largeCapacityConfig: LargeCapacityConfig
    ldapEnabled: bool
    mountOptions: _list[MountOption]
    multipleEndpoints: bool
    name: str
    network: str
    protocols: _list[
        typing.Literal[
            "PROTOCOLS_UNSPECIFIED", "NFSV3", "NFSV4", "SMB", "ISCSI", "NVME"
        ]
    ]
    psaRange: str
    replicaZone: str
    restoreParameters: RestoreParameters
    restrictedActions: _list[typing.Literal["RESTRICTED_ACTION_UNSPECIFIED", "DELETE"]]
    securityStyle: typing.Literal["SECURITY_STYLE_UNSPECIFIED", "NTFS", "UNIX"]
    serviceLevel: typing.Literal[
        "SERVICE_LEVEL_UNSPECIFIED", "PREMIUM", "EXTREME", "STANDARD", "FLEX"
    ]
    shareName: str
    smbSettings: _list[
        typing.Literal[
            "SMB_SETTINGS_UNSPECIFIED",
            "ENCRYPT_DATA",
            "BROWSABLE",
            "CHANGE_NOTIFY",
            "NON_BROWSABLE",
            "OPLOCKS",
            "SHOW_SNAPSHOT",
            "SHOW_PREVIOUS_VERSIONS",
            "ACCESS_BASED_ENUMERATION",
            "CONTINUOUSLY_AVAILABLE",
        ]
    ]
    snapReserve: float
    snapshotDirectory: bool
    snapshotPolicy: SnapshotPolicy
    state: typing.Literal[
        "STATE_UNSPECIFIED",
        "READY",
        "CREATING",
        "DELETING",
        "UPDATING",
        "RESTORING",
        "DISABLED",
        "ERROR",
        "PREPARING",
        "READ_ONLY",
    ]
    stateDetails: str
    storagePool: str
    throughputMibps: float
    tieringPolicy: TieringPolicy
    unixPermissions: str
    usedGib: str
    zone: str

@typing.type_check_only
class VolumeBackupConfig(typing.TypedDict, total=False):
    backupConfig: BackupConfig
    volumeUuid: str

@typing.type_check_only
class WeeklySchedule(typing.TypedDict, total=False):
    day: str
    hour: float
    minute: float
    snapshotsToKeep: float
