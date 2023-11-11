import typing

import typing_extensions

_list = list

@typing.type_check_only
class Catalog(typing_extensions.TypedDict, total=False):
    createTime: str
    deleteTime: str
    expireTime: str
    name: str
    updateTime: str

@typing.type_check_only
class Database(typing_extensions.TypedDict, total=False):
    createTime: str
    deleteTime: str
    expireTime: str
    hiveOptions: HiveDatabaseOptions
    name: str
    type: typing_extensions.Literal["TYPE_UNSPECIFIED", "HIVE"]
    updateTime: str

@typing.type_check_only
class HiveDatabaseOptions(typing_extensions.TypedDict, total=False):
    locationUri: str
    parameters: dict[str, typing.Any]

@typing.type_check_only
class HiveTableOptions(typing_extensions.TypedDict, total=False):
    parameters: dict[str, typing.Any]
    storageDescriptor: StorageDescriptor
    tableType: str

@typing.type_check_only
class ListCatalogsResponse(typing_extensions.TypedDict, total=False):
    catalogs: _list[Catalog]
    nextPageToken: str

@typing.type_check_only
class ListDatabasesResponse(typing_extensions.TypedDict, total=False):
    databases: _list[Database]
    nextPageToken: str

@typing.type_check_only
class ListTablesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    tables: _list[Table]

@typing.type_check_only
class RenameTableRequest(typing_extensions.TypedDict, total=False):
    newName: str

@typing.type_check_only
class SerDeInfo(typing_extensions.TypedDict, total=False):
    serializationLib: str

@typing.type_check_only
class StorageDescriptor(typing_extensions.TypedDict, total=False):
    inputFormat: str
    locationUri: str
    outputFormat: str
    serdeInfo: SerDeInfo

@typing.type_check_only
class Table(typing_extensions.TypedDict, total=False):
    createTime: str
    deleteTime: str
    etag: str
    expireTime: str
    hiveOptions: HiveTableOptions
    name: str
    type: typing_extensions.Literal["TYPE_UNSPECIFIED", "HIVE"]
    updateTime: str
