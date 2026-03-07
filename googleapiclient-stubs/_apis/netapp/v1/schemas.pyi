import typing

import typing_extensions

_list = list

@typing.type_check_only
class ActiveDirectory(typing_extensions.TypedDict, total=False):
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
    state: typing_extensions.Literal[
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
class Backup(typing_extensions.TypedDict, total=False):
    backupRegion: str
    backupType: typing_extensions.Literal["TYPE_UNSPECIFIED", "MANUAL", "SCHEDULED"]
    chainStorageBytes: str
    createTime: str
    description: str
    enforcedRetentionEndTime: str
    labels: dict[str, typing.Any]
    name: str
    satisfiesPzi: bool
    satisfiesPzs: bool
    sourceSnapshot: str
    sourceVolume: str
    state: typing_extensions.Literal[
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
class BackupConfig(typing_extensions.TypedDict, total=False):
    backupChainBytes: str
    backupPolicies: _list[str]
    backupVault: str
    scheduledBackupEnabled: bool

@typing.type_check_only
class BackupPolicy(typing_extensions.TypedDict, total=False):
    assignedVolumeCount: int
    createTime: str
    dailyBackupLimit: int
    description: str
    enabled: bool
    labels: dict[str, typing.Any]
    monthlyBackupLimit: int
    name: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "CREATING", "READY", "DELETING", "ERROR", "UPDATING"
    ]
    weeklyBackupLimit: int

@typing.type_check_only
class BackupRetentionPolicy(typing_extensions.TypedDict, total=False):
    backupMinimumEnforcedRetentionDays: int
    dailyBackupImmutable: bool
    manualBackupImmutable: bool
    monthlyBackupImmutable: bool
    weeklyBackupImmutable: bool

@typing.type_check_only
class BackupVault(typing_extensions.TypedDict, total=False):
    backupRegion: str
    backupRetentionPolicy: BackupRetentionPolicy
    backupVaultType: typing_extensions.Literal[
        "BACKUP_VAULT_TYPE_UNSPECIFIED", "IN_REGION", "CROSS_REGION"
    ]
    backupsCryptoKeyVersion: str
    createTime: str
    description: str
    destinationBackupVault: str
    encryptionState: typing_extensions.Literal[
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
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "CREATING", "READY", "DELETING", "ERROR", "UPDATING"
    ]

@typing.type_check_only
class BlockDevice(typing_extensions.TypedDict, total=False):
    hostGroups: _list[str]
    identifier: str
    name: str
    osType: typing_extensions.Literal["OS_TYPE_UNSPECIFIED", "LINUX", "WINDOWS", "ESXI"]
    sizeGib: str

@typing.type_check_only
class CacheConfig(typing_extensions.TypedDict, total=False):
    cachePrePopulate: CachePrePopulate
    cachePrePopulateState: typing_extensions.Literal[
        "CACHE_PRE_POPULATE_STATE_UNSPECIFIED",
        "NOT_NEEDED",
        "IN_PROGRESS",
        "COMPLETE",
        "ERROR",
    ]
    cifsChangeNotifyEnabled: bool
    writebackEnabled: bool

@typing.type_check_only
class CacheParameters(typing_extensions.TypedDict, total=False):
    cacheConfig: CacheConfig
    cacheState: typing_extensions.Literal[
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
class CachePrePopulate(typing_extensions.TypedDict, total=False):
    excludePathList: _list[str]
    pathList: _list[str]
    recursion: bool

@typing.type_check_only
class CancelOperationRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class CloneDetails(typing_extensions.TypedDict, total=False):
    sharedSpaceGib: str
    sourceSnapshot: str
    sourceVolume: str

@typing.type_check_only
class DailySchedule(typing_extensions.TypedDict, total=False):
    hour: float
    minute: float
    snapshotsToKeep: float

@typing.type_check_only
class DestinationVolumeParameters(typing_extensions.TypedDict, total=False):
    description: str
    shareName: str
    storagePool: str
    tieringPolicy: TieringPolicy
    volumeId: str

@typing.type_check_only
class EncryptVolumesRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class EstablishPeeringRequest(typing_extensions.TypedDict, total=False):
    peerClusterName: str
    peerIpAddresses: _list[str]
    peerSvmName: str
    peerVolumeName: str

@typing.type_check_only
class EstablishVolumePeeringRequest(typing_extensions.TypedDict, total=False):
    peerClusterName: str
    peerIpAddresses: _list[str]
    peerSvmName: str
    peerVolumeName: str

@typing.type_check_only
class ExportPolicy(typing_extensions.TypedDict, total=False):
    rules: _list[SimpleExportPolicyRule]

@typing.type_check_only
class GoogleProtobufEmpty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class HostGroup(typing_extensions.TypedDict, total=False):
    createTime: str
    description: str
    hosts: _list[str]
    labels: dict[str, typing.Any]
    name: str
    osType: typing_extensions.Literal["OS_TYPE_UNSPECIFIED", "LINUX", "WINDOWS", "ESXI"]
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "CREATING", "READY", "UPDATING", "DELETING", "DISABLED"
    ]
    type: typing_extensions.Literal["TYPE_UNSPECIFIED", "ISCSI_INITIATOR"]

@typing.type_check_only
class HourlySchedule(typing_extensions.TypedDict, total=False):
    minute: float
    snapshotsToKeep: float

@typing.type_check_only
class HybridPeeringDetails(typing_extensions.TypedDict, total=False):
    command: str
    commandExpiryTime: str
    passphrase: str
    peerClusterName: str
    peerSvmName: str
    peerVolumeName: str
    subnetIp: str

@typing.type_check_only
class HybridReplicationParameters(typing_extensions.TypedDict, total=False):
    clusterLocation: str
    description: str
    hybridReplicationType: typing_extensions.Literal[
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
    replicationSchedule: typing_extensions.Literal[
        "HYBRID_REPLICATION_SCHEDULE_UNSPECIFIED", "EVERY_10_MINUTES", "HOURLY", "DAILY"
    ]

@typing.type_check_only
class KmsConfig(typing_extensions.TypedDict, total=False):
    createTime: str
    cryptoKeyName: str
    description: str
    instructions: str
    labels: dict[str, typing.Any]
    name: str
    serviceAccount: str
    state: typing_extensions.Literal[
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
class ListActiveDirectoriesResponse(typing_extensions.TypedDict, total=False):
    activeDirectories: _list[ActiveDirectory]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListBackupPoliciesResponse(typing_extensions.TypedDict, total=False):
    backupPolicies: _list[BackupPolicy]
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
class ListHostGroupsResponse(typing_extensions.TypedDict, total=False):
    hostGroups: _list[HostGroup]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListKmsConfigsResponse(typing_extensions.TypedDict, total=False):
    kmsConfigs: _list[KmsConfig]
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
class ListQuotaRulesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    quotaRules: _list[QuotaRule]
    unreachable: _list[str]

@typing.type_check_only
class ListReplicationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    replications: _list[Replication]
    unreachable: _list[str]

@typing.type_check_only
class ListSnapshotsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    snapshots: _list[Snapshot]
    unreachable: _list[str]

@typing.type_check_only
class ListStoragePoolsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    storagePools: _list[StoragePool]
    unreachable: _list[str]

@typing.type_check_only
class ListVolumesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    unreachable: _list[str]
    volumes: _list[Volume]

@typing.type_check_only
class Location(typing_extensions.TypedDict, total=False):
    displayName: str
    labels: dict[str, typing.Any]
    locationId: str
    metadata: dict[str, typing.Any]
    name: str

@typing.type_check_only
class LocationMetadata(typing_extensions.TypedDict, total=False):
    hasOntapProxy: bool
    hasVcp: bool
    supportedFlexPerformance: _list[
        typing_extensions.Literal[
            "FLEX_PERFORMANCE_UNSPECIFIED",
            "FLEX_PERFORMANCE_DEFAULT",
            "FLEX_PERFORMANCE_CUSTOM",
        ]
    ]
    supportedServiceLevels: _list[
        typing_extensions.Literal[
            "SERVICE_LEVEL_UNSPECIFIED", "PREMIUM", "EXTREME", "STANDARD", "FLEX"
        ]
    ]

@typing.type_check_only
class MonthlySchedule(typing_extensions.TypedDict, total=False):
    daysOfMonth: str
    hour: float
    minute: float
    snapshotsToKeep: float

@typing.type_check_only
class MountOption(typing_extensions.TypedDict, total=False):
    export: str
    exportFull: str
    instructions: str
    ipAddress: str
    protocol: typing_extensions.Literal[
        "PROTOCOLS_UNSPECIFIED", "NFSV3", "NFSV4", "SMB", "ISCSI"
    ]

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
class QuotaRule(typing_extensions.TypedDict, total=False):
    createTime: str
    description: str
    diskLimitMib: int
    labels: dict[str, typing.Any]
    name: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "CREATING", "UPDATING", "DELETING", "READY", "ERROR"
    ]
    stateDetails: str
    target: str
    type: typing_extensions.Literal[
        "TYPE_UNSPECIFIED",
        "INDIVIDUAL_USER_QUOTA",
        "INDIVIDUAL_GROUP_QUOTA",
        "DEFAULT_USER_QUOTA",
        "DEFAULT_GROUP_QUOTA",
    ]

@typing.type_check_only
class Replication(typing_extensions.TypedDict, total=False):
    clusterLocation: str
    createTime: str
    description: str
    destinationVolume: str
    destinationVolumeParameters: DestinationVolumeParameters
    healthy: bool
    hybridPeeringDetails: HybridPeeringDetails
    hybridReplicationType: typing_extensions.Literal[
        "HYBRID_REPLICATION_TYPE_UNSPECIFIED",
        "MIGRATION",
        "CONTINUOUS_REPLICATION",
        "ONPREM_REPLICATION",
        "REVERSE_ONPREM_REPLICATION",
    ]
    hybridReplicationUserCommands: UserCommands
    labels: dict[str, typing.Any]
    mirrorState: typing_extensions.Literal[
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
    replicationSchedule: typing_extensions.Literal[
        "REPLICATION_SCHEDULE_UNSPECIFIED", "EVERY_10_MINUTES", "HOURLY", "DAILY"
    ]
    role: typing_extensions.Literal[
        "REPLICATION_ROLE_UNSPECIFIED", "SOURCE", "DESTINATION"
    ]
    sourceVolume: str
    state: typing_extensions.Literal[
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
class RestoreBackupFilesRequest(typing_extensions.TypedDict, total=False):
    backup: str
    fileList: _list[str]
    restoreDestinationPath: str

@typing.type_check_only
class RestoreParameters(typing_extensions.TypedDict, total=False):
    sourceBackup: str
    sourceSnapshot: str

@typing.type_check_only
class ResumeReplicationRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class ReverseReplicationDirectionRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class RevertVolumeRequest(typing_extensions.TypedDict, total=False):
    snapshotId: str

@typing.type_check_only
class SimpleExportPolicyRule(typing_extensions.TypedDict, total=False):
    accessType: typing_extensions.Literal[
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
    squashMode: typing_extensions.Literal[
        "SQUASH_MODE_UNSPECIFIED", "NO_ROOT_SQUASH", "ROOT_SQUASH", "ALL_SQUASH"
    ]

@typing.type_check_only
class Snapshot(typing_extensions.TypedDict, total=False):
    createTime: str
    description: str
    labels: dict[str, typing.Any]
    name: str
    state: typing_extensions.Literal[
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
class SnapshotPolicy(typing_extensions.TypedDict, total=False):
    dailySchedule: DailySchedule
    enabled: bool
    hourlySchedule: HourlySchedule
    monthlySchedule: MonthlySchedule
    weeklySchedule: WeeklySchedule

@typing.type_check_only
class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class StopReplicationRequest(typing_extensions.TypedDict, total=False):
    force: bool

@typing.type_check_only
class StoragePool(typing_extensions.TypedDict, total=False):
    activeDirectory: str
    allowAutoTiering: bool
    availableThroughputMibps: float
    capacityGib: str
    coldTierSizeUsedGib: str
    createTime: str
    customPerformanceEnabled: bool
    description: str
    enableHotTierAutoResize: bool
    encryptionType: typing_extensions.Literal[
        "ENCRYPTION_TYPE_UNSPECIFIED", "SERVICE_MANAGED", "CLOUD_KMS"
    ]
    globalAccessAllowed: bool
    hotTierSizeGib: str
    hotTierSizeUsedGib: str
    kmsConfig: str
    labels: dict[str, typing.Any]
    ldapEnabled: bool
    name: str
    network: str
    psaRange: str
    qosType: typing_extensions.Literal["QOS_TYPE_UNSPECIFIED", "AUTO", "MANUAL"]
    replicaZone: str
    satisfiesPzi: bool
    satisfiesPzs: bool
    serviceLevel: typing_extensions.Literal[
        "SERVICE_LEVEL_UNSPECIFIED", "PREMIUM", "EXTREME", "STANDARD", "FLEX"
    ]
    state: typing_extensions.Literal[
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
    type: typing_extensions.Literal[
        "STORAGE_POOL_TYPE_UNSPECIFIED", "FILE", "UNIFIED", "UNIFIED_LARGE_CAPACITY"
    ]
    volumeCapacityGib: str
    volumeCount: int
    zone: str

@typing.type_check_only
class SwitchActiveReplicaZoneRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class SyncReplicationRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class TieringPolicy(typing_extensions.TypedDict, total=False):
    coolingThresholdDays: int
    hotTierBypassModeEnabled: bool
    tierAction: typing_extensions.Literal[
        "TIER_ACTION_UNSPECIFIED", "ENABLED", "PAUSED"
    ]

@typing.type_check_only
class TransferStats(typing_extensions.TypedDict, total=False):
    lagDuration: str
    lastTransferBytes: str
    lastTransferDuration: str
    lastTransferEndTime: str
    lastTransferError: str
    totalTransferDuration: str
    transferBytes: str
    updateTime: str

@typing.type_check_only
class UserCommands(typing_extensions.TypedDict, total=False):
    commands: _list[str]

@typing.type_check_only
class ValidateDirectoryServiceRequest(typing_extensions.TypedDict, total=False):
    directoryServiceType: typing_extensions.Literal[
        "DIRECTORY_SERVICE_TYPE_UNSPECIFIED", "ACTIVE_DIRECTORY"
    ]

@typing.type_check_only
class VerifyKmsConfigRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class VerifyKmsConfigResponse(typing_extensions.TypedDict, total=False):
    healthError: str
    healthy: bool
    instructions: str

@typing.type_check_only
class Volume(typing_extensions.TypedDict, total=False):
    activeDirectory: str
    backupConfig: BackupConfig
    blockDevices: _list[BlockDevice]
    cacheParameters: CacheParameters
    capacityGib: str
    cloneDetails: CloneDetails
    coldTierSizeGib: str
    createTime: str
    description: str
    encryptionType: typing_extensions.Literal[
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
    ldapEnabled: bool
    mountOptions: _list[MountOption]
    multipleEndpoints: bool
    name: str
    network: str
    protocols: _list[
        typing_extensions.Literal[
            "PROTOCOLS_UNSPECIFIED", "NFSV3", "NFSV4", "SMB", "ISCSI"
        ]
    ]
    psaRange: str
    replicaZone: str
    restoreParameters: RestoreParameters
    restrictedActions: _list[
        typing_extensions.Literal["RESTRICTED_ACTION_UNSPECIFIED", "DELETE"]
    ]
    securityStyle: typing_extensions.Literal[
        "SECURITY_STYLE_UNSPECIFIED", "NTFS", "UNIX"
    ]
    serviceLevel: typing_extensions.Literal[
        "SERVICE_LEVEL_UNSPECIFIED", "PREMIUM", "EXTREME", "STANDARD", "FLEX"
    ]
    shareName: str
    smbSettings: _list[
        typing_extensions.Literal[
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
    state: typing_extensions.Literal[
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
class WeeklySchedule(typing_extensions.TypedDict, total=False):
    day: str
    hour: float
    minute: float
    snapshotsToKeep: float
