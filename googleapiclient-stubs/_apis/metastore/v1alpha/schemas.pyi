import typing

import typing_extensions

_list = list

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
class AuxiliaryVersionConfig(typing_extensions.TypedDict, total=False):
    configOverrides: dict[str, typing.Any]
    networkConfig: NetworkConfig
    version: str

@typing.type_check_only
class BackendMetastore(typing_extensions.TypedDict, total=False):
    metastoreType: typing_extensions.Literal[
        "METASTORE_TYPE_UNSPECIFIED", "BIGQUERY", "DATAPROC_METASTORE"
    ]
    name: str

@typing.type_check_only
class Backup(typing_extensions.TypedDict, total=False):
    createTime: str
    description: str
    endTime: str
    name: str
    restoringServices: _list[str]
    serviceRevision: Service
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "CREATING", "DELETING", "ACTIVE", "FAILED", "RESTORING"
    ]

@typing.type_check_only
class Binding(typing_extensions.TypedDict, total=False):
    condition: Expr
    members: _list[str]
    role: str

@typing.type_check_only
class Consumer(typing_extensions.TypedDict, total=False):
    endpointUri: str
    subnetwork: str

@typing.type_check_only
class DataCatalogConfig(typing_extensions.TypedDict, total=False):
    enabled: bool

@typing.type_check_only
class DatabaseDump(typing_extensions.TypedDict, total=False):
    databaseType: typing_extensions.Literal["DATABASE_TYPE_UNSPECIFIED", "MYSQL"]
    gcsUri: str
    sourceDatabase: str
    type: typing_extensions.Literal["TYPE_UNSPECIFIED", "MYSQL", "AVRO"]

@typing.type_check_only
class DataplexConfig(typing_extensions.TypedDict, total=False):
    lakeResources: dict[str, typing.Any]

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class EncryptionConfig(typing_extensions.TypedDict, total=False):
    kmsKey: str

@typing.type_check_only
class ExportMetadataRequest(typing_extensions.TypedDict, total=False):
    databaseDumpType: typing_extensions.Literal["TYPE_UNSPECIFIED", "MYSQL", "AVRO"]
    destinationGcsFolder: str
    requestId: str

@typing.type_check_only
class Expr(typing_extensions.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str

@typing.type_check_only
class Federation(typing_extensions.TypedDict, total=False):
    backendMetastores: dict[str, typing.Any]
    createTime: str
    endpointUri: str
    labels: dict[str, typing.Any]
    name: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "CREATING", "ACTIVE", "UPDATING", "DELETING", "ERROR"
    ]
    stateMessage: str
    uid: str
    updateTime: str
    version: str

@typing.type_check_only
class HiveMetastoreConfig(typing_extensions.TypedDict, total=False):
    auxiliaryVersions: dict[str, typing.Any]
    configOverrides: dict[str, typing.Any]
    endpointProtocol: typing_extensions.Literal[
        "ENDPOINT_PROTOCOL_UNSPECIFIED", "THRIFT", "GRPC"
    ]
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
class Lake(typing_extensions.TypedDict, total=False):
    name: str

@typing.type_check_only
class ListBackupsResponse(typing_extensions.TypedDict, total=False):
    backups: _list[Backup]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListFederationsResponse(typing_extensions.TypedDict, total=False):
    federations: _list[Federation]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListLocationsResponse(typing_extensions.TypedDict, total=False):
    locations: _list[Location]
    nextPageToken: str

@typing.type_check_only
class ListMetadataImportsResponse(typing_extensions.TypedDict, total=False):
    metadataImports: _list[MetadataImport]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListOperationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    operations: _list[Operation]

@typing.type_check_only
class ListServicesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    services: _list[Service]
    unreachable: _list[str]

@typing.type_check_only
class Location(typing_extensions.TypedDict, total=False):
    displayName: str
    labels: dict[str, typing.Any]
    locationId: str
    metadata: dict[str, typing.Any]
    name: str

@typing.type_check_only
class LocationMetadata(typing_extensions.TypedDict, total=False):
    supportedHiveMetastoreVersions: _list[HiveMetastoreVersion]

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
    databaseDumpType: typing_extensions.Literal["TYPE_UNSPECIFIED", "MYSQL", "AVRO"]
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
    endTime: str
    name: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "RUNNING", "SUCCEEDED", "UPDATING", "FAILED"
    ]
    updateTime: str

@typing.type_check_only
class MetadataIntegration(typing_extensions.TypedDict, total=False):
    dataCatalogConfig: DataCatalogConfig
    dataplexConfig: DataplexConfig

@typing.type_check_only
class MetadataManagementActivity(typing_extensions.TypedDict, total=False):
    metadataExports: _list[MetadataExport]
    restores: _list[Restore]

@typing.type_check_only
class NetworkConfig(typing_extensions.TypedDict, total=False):
    consumers: _list[Consumer]

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
class RemoveIamPolicyRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class RemoveIamPolicyResponse(typing_extensions.TypedDict, total=False):
    success: bool

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
class RestoreServiceRequest(typing_extensions.TypedDict, total=False):
    backup: str
    requestId: str
    restoreType: typing_extensions.Literal[
        "RESTORE_TYPE_UNSPECIFIED", "FULL", "METADATA_ONLY"
    ]

@typing.type_check_only
class Secret(typing_extensions.TypedDict, total=False):
    cloudSecret: str

@typing.type_check_only
class Service(typing_extensions.TypedDict, total=False):
    artifactGcsUri: str
    createTime: str
    databaseType: typing_extensions.Literal[
        "DATABASE_TYPE_UNSPECIFIED", "MYSQL", "SPANNER"
    ]
    encryptionConfig: EncryptionConfig
    endpointUri: str
    hiveMetastoreConfig: HiveMetastoreConfig
    labels: dict[str, typing.Any]
    maintenanceWindow: MaintenanceWindow
    metadataIntegration: MetadataIntegration
    metadataManagementActivity: MetadataManagementActivity
    name: str
    network: str
    networkConfig: NetworkConfig
    port: int
    releaseChannel: typing_extensions.Literal[
        "RELEASE_CHANNEL_UNSPECIFIED", "CANARY", "STABLE"
    ]
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
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class TestIamPermissionsRequest(typing_extensions.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class TestIamPermissionsResponse(typing_extensions.TypedDict, total=False):
    permissions: _list[str]
