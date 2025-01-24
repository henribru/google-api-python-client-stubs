import typing

import typing_extensions

_list = list

@typing.type_check_only
class AdminSettings(typing_extensions.TypedDict, total=False):
    allowedEmailDomains: _list[str]

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
class CancelOperationRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class CustomDomain(typing_extensions.TypedDict, total=False):
    domain: str
    state: typing_extensions.Literal[
        "CUSTOM_DOMAIN_STATE_UNSPECIFIED",
        "UNVERIFIED",
        "VERIFIED",
        "MODIFYING",
        "AVAILABLE",
        "UNAVAILABLE",
        "UNKNOWN",
    ]

@typing.type_check_only
class Date(typing_extensions.TypedDict, total=False):
    day: int
    month: int
    year: int

@typing.type_check_only
class DenyMaintenancePeriod(typing_extensions.TypedDict, total=False):
    endDate: Date
    startDate: Date
    time: TimeOfDay

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class EncryptionConfig(typing_extensions.TypedDict, total=False):
    kmsKeyName: str
    kmsKeyNameVersion: str
    kmsKeyState: typing_extensions.Literal[
        "KMS_KEY_STATE_UNSPECIFIED", "VALID", "REVOKED"
    ]

@typing.type_check_only
class ExportEncryptionConfig(typing_extensions.TypedDict, total=False):
    kmsKeyName: str

@typing.type_check_only
class ExportInstanceRequest(typing_extensions.TypedDict, total=False):
    encryptionConfig: ExportEncryptionConfig
    gcsUri: str

@typing.type_check_only
class ExportMetadata(typing_extensions.TypedDict, total=False):
    exportEncryptionKey: ExportMetadataEncryptionKey
    filePaths: _list[str]
    lookerEncryptionKey: str
    lookerInstance: str
    lookerPlatformEdition: str
    lookerVersion: str
    source: typing_extensions.Literal[
        "SOURCE_UNSPECIFIED", "LOOKER_CORE", "LOOKER_ORIGINAL"
    ]

@typing.type_check_only
class ExportMetadataEncryptionKey(typing_extensions.TypedDict, total=False):
    cmek: str
    version: str

@typing.type_check_only
class Expr(typing_extensions.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str

@typing.type_check_only
class ImportInstanceRequest(typing_extensions.TypedDict, total=False):
    gcsUri: str

@typing.type_check_only
class Instance(typing_extensions.TypedDict, total=False):
    adminSettings: AdminSettings
    consumerNetwork: str
    createTime: str
    customDomain: CustomDomain
    denyMaintenancePeriod: DenyMaintenancePeriod
    egressPublicIp: str
    encryptionConfig: EncryptionConfig
    fipsEnabled: bool
    geminiEnabled: bool
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
    platformEdition: typing_extensions.Literal[
        "PLATFORM_EDITION_UNSPECIFIED",
        "LOOKER_CORE_TRIAL",
        "LOOKER_CORE_STANDARD",
        "LOOKER_CORE_STANDARD_ANNUAL",
        "LOOKER_CORE_ENTERPRISE_ANNUAL",
        "LOOKER_CORE_EMBED_ANNUAL",
        "LOOKER_CORE_NONPROD_STANDARD_ANNUAL",
        "LOOKER_CORE_NONPROD_ENTERPRISE_ANNUAL",
        "LOOKER_CORE_NONPROD_EMBED_ANNUAL",
    ]
    privateIpEnabled: bool
    pscConfig: PscConfig
    pscEnabled: bool
    publicIpEnabled: bool
    reservedRange: str
    state: typing_extensions.Literal[
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
    updateTime: str
    userMetadata: UserMetadata

@typing.type_check_only
class ListInstancesResponse(typing_extensions.TypedDict, total=False):
    instances: _list[Instance]
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

@typing.type_check_only
class Location(typing_extensions.TypedDict, total=False):
    displayName: str
    labels: dict[str, typing.Any]
    locationId: str
    metadata: dict[str, typing.Any]
    name: str

@typing.type_check_only
class MaintenanceSchedule(typing_extensions.TypedDict, total=False):
    endTime: str
    startTime: str

@typing.type_check_only
class MaintenanceWindow(typing_extensions.TypedDict, total=False):
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
    startTime: TimeOfDay

@typing.type_check_only
class OAuthConfig(typing_extensions.TypedDict, total=False):
    clientId: str
    clientSecret: str

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
class Policy(typing_extensions.TypedDict, total=False):
    auditConfigs: _list[AuditConfig]
    bindings: _list[Binding]
    etag: str
    version: int

@typing.type_check_only
class PscConfig(typing_extensions.TypedDict, total=False):
    allowedVpcs: _list[str]
    lookerServiceAttachmentUri: str
    serviceAttachments: _list[ServiceAttachment]

@typing.type_check_only
class RestartInstanceRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class ServiceAttachment(typing_extensions.TypedDict, total=False):
    connectionStatus: typing_extensions.Literal[
        "UNKNOWN", "ACCEPTED", "PENDING", "REJECTED", "NEEDS_ATTENTION", "CLOSED"
    ]
    localFqdn: str
    targetServiceAttachmentUri: str

@typing.type_check_only
class SetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    policy: Policy
    updateMask: str

@typing.type_check_only
class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class TestIamPermissionsRequest(typing_extensions.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class TestIamPermissionsResponse(typing_extensions.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class TimeOfDay(typing_extensions.TypedDict, total=False):
    hours: int
    minutes: int
    nanos: int
    seconds: int

@typing.type_check_only
class UserMetadata(typing_extensions.TypedDict, total=False):
    additionalDeveloperUserCount: int
    additionalStandardUserCount: int
    additionalViewerUserCount: int
