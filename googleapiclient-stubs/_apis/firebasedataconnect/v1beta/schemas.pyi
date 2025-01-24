import typing

import typing_extensions

_list = list

@typing.type_check_only
class CancelOperationRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class CloudSqlInstance(typing_extensions.TypedDict, total=False):
    instance: str

@typing.type_check_only
class Connector(typing_extensions.TypedDict, total=False):
    annotations: dict[str, typing.Any]
    createTime: str
    displayName: str
    etag: str
    labels: dict[str, typing.Any]
    name: str
    reconciling: bool
    source: Source
    uid: str
    updateTime: str

@typing.type_check_only
class Datasource(typing_extensions.TypedDict, total=False):
    postgresql: PostgreSql

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class ExecuteMutationRequest(typing_extensions.TypedDict, total=False):
    operationName: str
    variables: dict[str, typing.Any]

@typing.type_check_only
class ExecuteMutationResponse(typing_extensions.TypedDict, total=False):
    data: dict[str, typing.Any]
    errors: _list[GraphqlError]

@typing.type_check_only
class ExecuteQueryRequest(typing_extensions.TypedDict, total=False):
    operationName: str
    variables: dict[str, typing.Any]

@typing.type_check_only
class ExecuteQueryResponse(typing_extensions.TypedDict, total=False):
    data: dict[str, typing.Any]
    errors: _list[GraphqlError]

@typing.type_check_only
class File(typing_extensions.TypedDict, total=False):
    content: str
    path: str

@typing.type_check_only
class GraphqlError(typing_extensions.TypedDict, total=False):
    extensions: GraphqlErrorExtensions
    locations: _list[SourceLocation]
    message: str
    path: _list[typing.Any]

@typing.type_check_only
class GraphqlErrorExtensions(typing_extensions.TypedDict, total=False):
    file: str

@typing.type_check_only
class GraphqlRequest(typing_extensions.TypedDict, total=False):
    extensions: GraphqlRequestExtensions
    operationName: str
    query: str
    variables: dict[str, typing.Any]

@typing.type_check_only
class GraphqlRequestExtensions(typing_extensions.TypedDict, total=False):
    impersonate: Impersonation

@typing.type_check_only
class GraphqlResponse(typing_extensions.TypedDict, total=False):
    data: dict[str, typing.Any]
    errors: _list[GraphqlError]

@typing.type_check_only
class Impersonation(typing_extensions.TypedDict, total=False):
    authClaims: dict[str, typing.Any]
    unauthenticated: bool

@typing.type_check_only
class ListConnectorsResponse(typing_extensions.TypedDict, total=False):
    connectors: _list[Connector]
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
class ListSchemasResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    schemas: _list[Schema]
    unreachable: _list[str]

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
class PostgreSql(typing_extensions.TypedDict, total=False):
    cloudSql: CloudSqlInstance
    database: str
    schemaMigration: typing_extensions.Literal[
        "SQL_SCHEMA_MIGRATION_UNSPECIFIED", "MIGRATE_COMPATIBLE"
    ]
    schemaValidation: typing_extensions.Literal[
        "SQL_SCHEMA_VALIDATION_UNSPECIFIED", "NONE", "STRICT", "COMPATIBLE"
    ]
    unlinked: bool

@typing.type_check_only
class Schema(typing_extensions.TypedDict, total=False):
    annotations: dict[str, typing.Any]
    createTime: str
    datasources: _list[Datasource]
    displayName: str
    etag: str
    labels: dict[str, typing.Any]
    name: str
    reconciling: bool
    source: Source
    uid: str
    updateTime: str

@typing.type_check_only
class Service(typing_extensions.TypedDict, total=False):
    annotations: dict[str, typing.Any]
    createTime: str
    displayName: str
    etag: str
    labels: dict[str, typing.Any]
    name: str
    reconciling: bool
    uid: str
    updateTime: str

@typing.type_check_only
class Source(typing_extensions.TypedDict, total=False):
    files: _list[File]

@typing.type_check_only
class SourceLocation(typing_extensions.TypedDict, total=False):
    column: int
    line: int

@typing.type_check_only
class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str
