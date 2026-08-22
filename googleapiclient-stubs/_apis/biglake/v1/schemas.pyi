import typing

_list = list

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
class Catalog(typing.TypedDict, total=False):
    createTime: str
    deleteTime: str
    expireTime: str
    name: str
    updateTime: str

@typing.type_check_only
class Database(typing.TypedDict, total=False):
    createTime: str
    deleteTime: str
    expireTime: str
    hiveOptions: HiveDatabaseOptions
    name: str
    type: typing.Literal["TYPE_UNSPECIFIED", "HIVE"]
    updateTime: str

@typing.type_check_only
class Expr(typing.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str

@typing.type_check_only
class HiveDatabaseOptions(typing.TypedDict, total=False):
    locationUri: str
    parameters: dict[str, typing.Any]

@typing.type_check_only
class HiveTableOptions(typing.TypedDict, total=False):
    parameters: dict[str, typing.Any]
    storageDescriptor: StorageDescriptor
    tableType: str

@typing.type_check_only
class ListCatalogsResponse(typing.TypedDict, total=False):
    catalogs: _list[Catalog]
    nextPageToken: str

@typing.type_check_only
class ListDatabasesResponse(typing.TypedDict, total=False):
    databases: _list[Database]
    nextPageToken: str

@typing.type_check_only
class ListTablesResponse(typing.TypedDict, total=False):
    nextPageToken: str
    tables: _list[Table]

@typing.type_check_only
class Policy(typing.TypedDict, total=False):
    auditConfigs: _list[AuditConfig]
    bindings: _list[Binding]
    etag: str
    version: int

@typing.type_check_only
class RenameTableRequest(typing.TypedDict, total=False):
    newName: str

@typing.type_check_only
class SerDeInfo(typing.TypedDict, total=False):
    serializationLib: str

@typing.type_check_only
class SetIamPolicyRequest(typing.TypedDict, total=False):
    policy: Policy
    updateMask: str

@typing.type_check_only
class StorageDescriptor(typing.TypedDict, total=False):
    inputFormat: str
    locationUri: str
    outputFormat: str
    serdeInfo: SerDeInfo

@typing.type_check_only
class Table(typing.TypedDict, total=False):
    createTime: str
    deleteTime: str
    etag: str
    expireTime: str
    hiveOptions: HiveTableOptions
    name: str
    type: typing.Literal["TYPE_UNSPECIFIED", "HIVE"]
    updateTime: str

@typing.type_check_only
class TestIamPermissionsRequest(typing.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class TestIamPermissionsResponse(typing.TypedDict, total=False):
    permissions: _list[str]
