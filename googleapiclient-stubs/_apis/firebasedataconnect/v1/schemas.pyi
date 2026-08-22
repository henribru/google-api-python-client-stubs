import typing

_list = list

@typing.type_check_only
class CancelOperationRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class ClientCache(typing.TypedDict, total=False):
    entityIdIncluded: bool
    strictValidationEnabled: bool

@typing.type_check_only
class CloudSqlInstance(typing.TypedDict, total=False):
    edition: typing.Literal[
        "EDITION_UNSPECIFIED",
        "EDITION_ENTERPRISE",
        "EDITION_ENTERPRISE_PLUS",
        "EDITION_DEVELOPER",
    ]
    instance: str

@typing.type_check_only
class CodeChunk(typing.TypedDict, total=False):
    code: str
    languageCode: str

@typing.type_check_only
class Connector(typing.TypedDict, total=False):
    annotations: dict[str, typing.Any]
    clientCache: ClientCache
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
class DataConnectProperties(typing.TypedDict, total=False):
    entityId: str
    entityIds: _list[str]
    maxAge: str
    path: _list[typing.Any]

@typing.type_check_only
class Datasource(typing.TypedDict, total=False):
    httpGraphql: HttpGraphql
    postgresql: PostgreSql

@typing.type_check_only
class Empty(typing.TypedDict, total=False): ...

@typing.type_check_only
class ExecuteMutationRequest(typing.TypedDict, total=False):
    operationName: str
    variables: dict[str, typing.Any]

@typing.type_check_only
class ExecuteMutationResponse(typing.TypedDict, total=False):
    data: dict[str, typing.Any]
    errors: _list[GraphqlError]
    extensions: GraphqlResponseExtensions

@typing.type_check_only
class ExecuteQueryRequest(typing.TypedDict, total=False):
    operationName: str
    variables: dict[str, typing.Any]

@typing.type_check_only
class ExecuteQueryResponse(typing.TypedDict, total=False):
    data: dict[str, typing.Any]
    errors: _list[GraphqlError]
    extensions: GraphqlResponseExtensions

@typing.type_check_only
class File(typing.TypedDict, total=False):
    content: str
    path: str

@typing.type_check_only
class GenerateQueryRequest(typing.TypedDict, total=False):
    prompt: str
    schemas: _list[Schema]

@typing.type_check_only
class GenerateQueryResponse(typing.TypedDict, total=False):
    part: Part
    status: GenerationStatus

@typing.type_check_only
class GenerateSchemaRequest(typing.TypedDict, total=False):
    prompt: str

@typing.type_check_only
class GenerateSchemaResponse(typing.TypedDict, total=False):
    part: Part
    status: GenerationStatus

@typing.type_check_only
class GenerationStatus(typing.TypedDict, total=False):
    message: str
    state: typing.Literal[
        "STATE_UNSPECIFIED", "ANALYZING_CODE", "GENERATING_CODE", "COMPLETED"
    ]

@typing.type_check_only
class GraphqlError(typing.TypedDict, total=False):
    extensions: GraphqlErrorExtensions
    locations: _list[SourceLocation]
    message: str
    path: _list[typing.Any]

@typing.type_check_only
class GraphqlErrorExtensions(typing.TypedDict, total=False):
    code: typing.Literal[
        "OK",
        "CANCELLED",
        "UNKNOWN",
        "INVALID_ARGUMENT",
        "DEADLINE_EXCEEDED",
        "NOT_FOUND",
        "ALREADY_EXISTS",
        "PERMISSION_DENIED",
        "UNAUTHENTICATED",
        "RESOURCE_EXHAUSTED",
        "FAILED_PRECONDITION",
        "ABORTED",
        "OUT_OF_RANGE",
        "UNIMPLEMENTED",
        "INTERNAL",
        "UNAVAILABLE",
        "DATA_LOSS",
    ]
    debugDetails: str
    file: str
    warningLevel: typing.Literal[
        "WARNING_LEVEL_UNKNOWN",
        "LOG_ONLY",
        "INTERACTIVE_ACK",
        "REQUIRE_ACK",
        "REQUIRE_FORCE",
    ]
    workarounds: _list[Workaround]

@typing.type_check_only
class GraphqlRequest(typing.TypedDict, total=False):
    extensions: GraphqlRequestExtensions
    operationName: str
    query: str
    variables: dict[str, typing.Any]

@typing.type_check_only
class GraphqlRequestExtensions(typing.TypedDict, total=False):
    impersonate: Impersonation

@typing.type_check_only
class GraphqlResponse(typing.TypedDict, total=False):
    data: dict[str, typing.Any]
    errors: _list[GraphqlError]
    extensions: GraphqlResponseExtensions

@typing.type_check_only
class GraphqlResponseExtensions(typing.TypedDict, total=False):
    dataConnect: _list[DataConnectProperties]

@typing.type_check_only
class HttpGraphql(typing.TypedDict, total=False):
    timeout: str
    uri: str

@typing.type_check_only
class ImpersonateRequest(typing.TypedDict, total=False):
    extensions: GraphqlRequestExtensions
    operationName: str
    variables: dict[str, typing.Any]

@typing.type_check_only
class Impersonation(typing.TypedDict, total=False):
    authClaims: dict[str, typing.Any]
    includeDebugDetails: bool
    unauthenticated: bool

@typing.type_check_only
class ListConnectorsResponse(typing.TypedDict, total=False):
    connectors: _list[Connector]
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
class ListSchemasResponse(typing.TypedDict, total=False):
    nextPageToken: str
    schemas: _list[Schema]
    unreachable: _list[str]

@typing.type_check_only
class ListServicesResponse(typing.TypedDict, total=False):
    nextPageToken: str
    services: _list[Service]
    unreachable: _list[str]

@typing.type_check_only
class Location(typing.TypedDict, total=False):
    displayName: str
    labels: dict[str, typing.Any]
    locationId: str
    metadata: dict[str, typing.Any]
    name: str

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
class Part(typing.TypedDict, total=False):
    codeChunk: CodeChunk
    textChunk: TextChunk

@typing.type_check_only
class PostgreSql(typing.TypedDict, total=False):
    cloudSql: CloudSqlInstance
    database: str
    ephemeral: bool
    schema: str
    schemaMigration: typing.Literal[
        "SQL_SCHEMA_MIGRATION_UNSPECIFIED", "MIGRATE_COMPATIBLE"
    ]
    schemaValidation: typing.Literal[
        "SQL_SCHEMA_VALIDATION_UNSPECIFIED", "NONE", "STRICT", "COMPATIBLE"
    ]
    unlinked: bool

@typing.type_check_only
class Schema(typing.TypedDict, total=False):
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
class Service(typing.TypedDict, total=False):
    annotations: dict[str, typing.Any]
    connectors: _list[Connector]
    createTime: str
    displayName: str
    etag: str
    labels: dict[str, typing.Any]
    name: str
    reconciling: bool
    schemas: _list[Schema]
    source: Source
    uid: str
    updateTime: str

@typing.type_check_only
class Source(typing.TypedDict, total=False):
    files: _list[File]

@typing.type_check_only
class SourceLocation(typing.TypedDict, total=False):
    column: int
    line: int

@typing.type_check_only
class Status(typing.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class TextChunk(typing.TypedDict, total=False):
    text: str

@typing.type_check_only
class Workaround(typing.TypedDict, total=False):
    description: str
    reason: str
    replace: str
