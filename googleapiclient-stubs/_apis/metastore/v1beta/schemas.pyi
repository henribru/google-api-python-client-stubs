import typing

import typing_extensions
@typing.type_check_only
class AuditConfig(typing_extensions.TypedDict, total=False):
    auditLogConfigs: typing.List[AuditLogConfig]
    service: str

@typing.type_check_only
class AuditLogConfig(typing_extensions.TypedDict, total=False):
    exemptedMembers: typing.List[str]
    logType: typing_extensions.Literal[
        "LOG_TYPE_UNSPECIFIED", "ADMIN_READ", "DATA_WRITE", "DATA_READ"
    ]

@typing.type_check_only
class Binding(typing_extensions.TypedDict, total=False):
    condition: Expr
    members: typing.List[str]
    role: str

@typing.type_check_only
class DatabaseDump(typing_extensions.TypedDict, total=False):
    databaseType: typing_extensions.Literal["DATABASE_TYPE_UNSPECIFIED", "MYSQL"]
    gcsUri: str
    sourceDatabase: str

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class ExportMetadataRequest(typing_extensions.TypedDict, total=False):
    destinationGcsFolder: str
    requestId: str

@typing.type_check_only
class Expr(typing_extensions.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str

@typing.type_check_only
class HiveMetastoreConfig(typing_extensions.TypedDict, total=False):
    configOverrides: typing.Dict[str, typing.Any]
    kerberosConfig: KerberosConfig
    version: str

@typing.type_check_only
class HiveMetastoreVersion(typing_extensions.TypedDict, total=False):
    isDefault: bool
    version: str

@typing.type_check_only
class KerberosConfig(typing_extensions.TypedDict, total=False):
    keytab: Secret
    krb5ConfigGcsUri: str
    principal: str

@typing.type_check_only
class ListLocationsResponse(typing_extensions.TypedDict, total=False):
    locations: typing.List[Location]
    nextPageToken: str

@typing.type_check_only
class ListMetadataImportsResponse(typing_extensions.TypedDict, total=False):
    metadataImports: typing.List[MetadataImport]
    nextPageToken: str
    unreachable: typing.List[str]

@typing.type_check_only
class ListOperationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    operations: typing.List[Operation]

@typing.type_check_only
class ListServicesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    services: typing.List[Service]
    unreachable: typing.List[str]

@typing.type_check_only
class Location(typing_extensions.TypedDict, total=False):
    displayName: str
    labels: typing.Dict[str, typing.Any]
    locationId: str
    metadata: typing.Dict[str, typing.Any]
    name: str

@typing.type_check_only
class LocationMetadata(typing_extensions.TypedDict, total=False):
    supportedHiveMetastoreVersions: typing.List[HiveMetastoreVersion]

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
    hourOfDay: int

@typing.type_check_only
class MetadataExport(typing_extensions.TypedDict, total=False):
    destinationGcsUri: str
    endTime: str
    startTime: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "RUNNING", "SUCCEEDED", "FAILED", "CANCELLED"
    ]

@typing.type_check_only
class MetadataImport(typing_extensions.TypedDict, total=False):
    createTime: str
    databaseDump: DatabaseDump
    description: str
    name: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "RUNNING", "SUCCEEDED", "UPDATING", "FAILED"
    ]
    updateTime: str

@typing.type_check_only
class MetadataIntegration(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class MetadataManagementActivity(typing_extensions.TypedDict, total=False):
    metadataExports: typing.List[MetadataExport]
    restores: typing.List[Restore]

@typing.type_check_only
class Operation(typing_extensions.TypedDict, total=False):
    done: bool
    error: Status
    metadata: typing.Dict[str, typing.Any]
    name: str
    response: typing.Dict[str, typing.Any]

@typing.type_check_only
class Policy(typing_extensions.TypedDict, total=False):
    auditConfigs: typing.List[AuditConfig]
    bindings: typing.List[Binding]
    etag: str
    version: int

@typing.type_check_only
class Restore(typing_extensions.TypedDict, total=False):
    backup: str
    details: str
    endTime: str
    startTime: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "RUNNING", "SUCCEEDED", "FAILED", "CANCELLED"
    ]
    type: typing_extensions.Literal["RESTORE_TYPE_UNSPECIFIED", "FULL", "METADATA_ONLY"]

@typing.type_check_only
class Secret(typing_extensions.TypedDict, total=False):
    cloudSecret: str

@typing.type_check_only
class Service(typing_extensions.TypedDict, total=False):
    artifactGcsUri: str
    createTime: str
    endpointUri: str
    hiveMetastoreConfig: HiveMetastoreConfig
    labels: typing.Dict[str, typing.Any]
    maintenanceWindow: MaintenanceWindow
    metadataIntegration: MetadataIntegration
    metadataManagementActivity: MetadataManagementActivity
    name: str
    network: str
    port: int
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "CREATING",
        "ACTIVE",
        "SUSPENDING",
        "SUSPENDED",
        "UPDATING",
        "DELETING",
        "ERROR",
    ]
    stateMessage: str
    tier: typing_extensions.Literal["TIER_UNSPECIFIED", "DEVELOPER", "ENTERPRISE"]
    uid: str
    updateTime: str

@typing.type_check_only
class SetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    policy: Policy
    updateMask: str

@typing.type_check_only
class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: typing.List[typing.Dict[str, typing.Any]]
    message: str

@typing.type_check_only
class TestIamPermissionsRequest(typing_extensions.TypedDict, total=False):
    permissions: typing.List[str]

@typing.type_check_only
class TestIamPermissionsResponse(typing_extensions.TypedDict, total=False):
    permissions: typing.List[str]
