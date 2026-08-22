import typing

_list = list

@typing.type_check_only
class AdminSettings(typing.TypedDict, total=False):
    allowedEmailDomains: _list[str]

@typing.type_check_only
class CancelOperationRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class ControlledEgressConfig(typing.TypedDict, total=False):
    egressFqdns: _list[str]
    marketplaceEnabled: bool
    webProxyIps: _list[str]

@typing.type_check_only
class CustomDomain(typing.TypedDict, total=False):
    domain: str
    state: typing.Literal[
        "CUSTOM_DOMAIN_STATE_UNSPECIFIED",
        "UNVERIFIED",
        "VERIFIED",
        "MODIFYING",
        "AVAILABLE",
        "UNAVAILABLE",
        "UNKNOWN",
    ]

@typing.type_check_only
class Date(typing.TypedDict, total=False):
    day: int
    month: int
    year: int

@typing.type_check_only
class DenyMaintenancePeriod(typing.TypedDict, total=False):
    endDate: Date
    startDate: Date
    time: TimeOfDay

@typing.type_check_only
class Empty(typing.TypedDict, total=False): ...

@typing.type_check_only
class EncryptionConfig(typing.TypedDict, total=False):
    kmsKeyName: str
    kmsKeyNameVersion: str
    kmsKeyState: typing.Literal["KMS_KEY_STATE_UNSPECIFIED", "VALID", "REVOKED"]

@typing.type_check_only
class ExportEncryptionConfig(typing.TypedDict, total=False):
    kmsKeyName: str

@typing.type_check_only
class ExportInstanceRequest(typing.TypedDict, total=False):
    encryptionConfig: ExportEncryptionConfig
    gcsUri: str

@typing.type_check_only
class ExportMetadata(typing.TypedDict, total=False):
    esaSourceDatasetId: str
    exportEncryptionKey: ExportMetadataEncryptionKey
    filePaths: _list[str]
    lookerEncryptionKey: str
    lookerInstance: str
    lookerPlatformEdition: str
    lookerVersion: str
    source: typing.Literal["SOURCE_UNSPECIFIED", "LOOKER_CORE", "LOOKER_ORIGINAL"]

@typing.type_check_only
class ExportMetadataEncryptionKey(typing.TypedDict, total=False):
    cmek: str
    version: str

@typing.type_check_only
class ImportInstanceRequest(typing.TypedDict, total=False):
    gcsUri: str

@typing.type_check_only
class IngressIpAllowlistConfig(typing.TypedDict, total=False):
    allowlistRules: _list[IngressIpAllowlistRule]
    enabled: bool
    googleServicesEnabled: bool

@typing.type_check_only
class IngressIpAllowlistRule(typing.TypedDict, total=False):
    description: str
    ipRange: str

@typing.type_check_only
class Instance(typing.TypedDict, total=False):
    acceleratedSecurityPatchEnabled: bool
    adminSettings: AdminSettings
    catalogIntegrationOptOut: bool
    classType: typing.Literal["CLASS_TYPE_UNSPECIFIED", "R1", "P1"]
    consumerNetwork: str
    controlledEgressConfig: ControlledEgressConfig
    controlledEgressEnabled: bool
    createTime: str
    customDomain: CustomDomain
    denyMaintenancePeriod: DenyMaintenancePeriod
    egressPublicIp: str
    encryptionConfig: EncryptionConfig
    fipsEnabled: bool
    geminiEnabled: bool
    ingressIpAllowlistConfig: IngressIpAllowlistConfig
    ingressPrivateIp: str
    ingressPublicIp: str
    lastDenyMaintenancePeriod: DenyMaintenancePeriod
    linkedLspProjectNumber: str
    lookerUri: str
    lookerVersion: str
    maintenanceSchedule: MaintenanceSchedule
    maintenanceWindow: MaintenanceWindow
    name: str
    oauthConfig: OAuthConfig
    periodicExportConfig: PeriodicExportConfig
    platformEdition: typing.Literal[
        "PLATFORM_EDITION_UNSPECIFIED",
        "LOOKER_CORE_TRIAL",
        "LOOKER_CORE_STANDARD",
        "LOOKER_CORE_STANDARD_ANNUAL",
        "LOOKER_CORE_ENTERPRISE_ANNUAL",
        "LOOKER_CORE_EMBED_ANNUAL",
        "LOOKER_CORE_NONPROD_STANDARD_ANNUAL",
        "LOOKER_CORE_NONPROD_ENTERPRISE_ANNUAL",
        "LOOKER_CORE_NONPROD_EMBED_ANNUAL",
        "LOOKER_CORE_TRIAL_STANDARD",
        "LOOKER_CORE_TRIAL_ENTERPRISE",
        "LOOKER_CORE_TRIAL_EMBED",
    ]
    privateIpEnabled: bool
    pscConfig: PscConfig
    pscEnabled: bool
    publicIpEnabled: bool
    releaseChannel: typing.Literal[
        "RELEASE_CHANNEL_UNSPECIFIED", "RAPID", "REGULAR", "STABLE"
    ]
    reservedRange: str
    satisfiesPzi: bool
    satisfiesPzs: bool
    softDeleteReason: typing.Literal[
        "SOFT_DELETE_REASON_UNSPECIFIED",
        "BILLING_ACCOUNT_ISSUE",
        "TRIAL_EXPIRED",
        "CUSTOMER_REQUEST",
    ]
    state: typing.Literal[
        "STATE_UNSPECIFIED",
        "ACTIVE",
        "CREATING",
        "FAILED",
        "SUSPENDED",
        "UPDATING",
        "DELETING",
        "EXPORTING",
        "IMPORTING",
    ]
    suspendedTime: str
    updateTime: str
    userMetadata: UserMetadata

@typing.type_check_only
class InstanceBackup(typing.TypedDict, total=False):
    createTime: str
    encryptionConfig: EncryptionConfig
    expireTime: str
    name: str
    state: typing.Literal[
        "STATE_UNSPECIFIED", "CREATING", "DELETING", "ACTIVE", "FAILED"
    ]

@typing.type_check_only
class ListInstanceBackupsResponse(typing.TypedDict, total=False):
    instanceBackups: _list[InstanceBackup]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListInstancesResponse(typing.TypedDict, total=False):
    instances: _list[Instance]
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
class Location(typing.TypedDict, total=False):
    displayName: str
    labels: dict[str, typing.Any]
    locationId: str
    metadata: dict[str, typing.Any]
    name: str

@typing.type_check_only
class MaintenanceSchedule(typing.TypedDict, total=False):
    endTime: str
    startTime: str

@typing.type_check_only
class MaintenanceWindow(typing.TypedDict, total=False):
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
    startTime: TimeOfDay

@typing.type_check_only
class OAuthConfig(typing.TypedDict, total=False):
    clientId: str
    clientSecret: str
    sharedOauthClientEnabled: bool

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
class PeriodicExportConfig(typing.TypedDict, total=False):
    gcsUri: str
    kmsKey: str
    startTime: TimeOfDay

@typing.type_check_only
class PscConfig(typing.TypedDict, total=False):
    allowedVpcs: _list[str]
    lookerServiceAttachmentUri: str
    serviceAttachments: _list[ServiceAttachment]

@typing.type_check_only
class RestartInstanceRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class RestoreInstanceRequest(typing.TypedDict, total=False):
    backup: str

@typing.type_check_only
class ServiceAttachment(typing.TypedDict, total=False):
    connectionStatus: typing.Literal[
        "UNKNOWN", "ACCEPTED", "PENDING", "REJECTED", "NEEDS_ATTENTION", "CLOSED"
    ]
    failureReason: str
    localFqdn: str
    localFqdns: _list[str]
    targetServiceAttachmentUri: str

@typing.type_check_only
class Status(typing.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class TimeOfDay(typing.TypedDict, total=False):
    hours: int
    minutes: int
    nanos: int
    seconds: int

@typing.type_check_only
class UndeleteInstanceRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class UserMetadata(typing.TypedDict, total=False):
    additionalDeveloperUserCount: int
    additionalStandardUserCount: int
    additionalViewerUserCount: int
