import typing

_list = list

@typing.type_check_only
class AccessCredentials(typing.TypedDict, total=False):
    accessToken: str
    expiresIn: str
    refreshToken: str

@typing.type_check_only
class Action(typing.TypedDict, total=False):
    description: str
    displayName: str
    inputJsonSchema: JsonSchema
    inputParameters: _list[InputParameter]
    metadata: dict[str, typing.Any]
    name: str
    resultJsonSchema: JsonSchema
    resultMetadata: _list[ResultMetadata]

@typing.type_check_only
class AuthCodeData(typing.TypedDict, total=False):
    authCode: str
    pkceVerifier: str
    redirectUri: str
    scopes: _list[str]

@typing.type_check_only
class CheckReadinessResponse(typing.TypedDict, total=False):
    status: str

@typing.type_check_only
class CheckStatusResponse(typing.TypedDict, total=False):
    description: str
    metadata: dict[str, typing.Any]
    state: typing.Literal["STATE_UNSPECIFIED", "ACTIVE", "ERROR", "AUTH_ERROR"]

@typing.type_check_only
class DailyCycle(typing.TypedDict, total=False):
    duration: str
    startTime: TimeOfDay

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
class Entity(typing.TypedDict, total=False):
    fields: dict[str, typing.Any]
    metadata: dict[str, typing.Any]
    name: str

@typing.type_check_only
class EntityType(typing.TypedDict, total=False):
    defaultSortBy: str
    fields: _list[Field]
    jsonSchema: JsonSchema
    metadata: dict[str, typing.Any]
    name: str
    operations: _list[
        typing.Literal[
            "OPERATION_UNSPECIFIED", "LIST", "GET", "CREATE", "UPDATE", "DELETE"
        ]
    ]

@typing.type_check_only
class ExchangeAuthCodeRequest(typing.TypedDict, total=False):
    authCodeData: AuthCodeData
    executionConfig: ExecutionConfig
    oauth2Config: OAuth2Config

@typing.type_check_only
class ExchangeAuthCodeResponse(typing.TypedDict, total=False):
    accessCredentials: AccessCredentials
    metadata: dict[str, typing.Any]

@typing.type_check_only
class ExecuteActionRequest(typing.TypedDict, total=False):
    executionConfig: ExecutionConfig
    parameters: dict[str, typing.Any]

@typing.type_check_only
class ExecuteActionResponse(typing.TypedDict, total=False):
    metadata: dict[str, typing.Any]
    results: _list[dict[str, typing.Any]]

@typing.type_check_only
class ExecuteHttpRequestRequest(typing.TypedDict, total=False):
    headers: _list[HttpHeader]
    httpMethod: typing.Literal[
        "HTTP_METHOD_UNSPECIFIED",
        "HTTP_METHOD_GET",
        "HTTP_METHOD_POST",
        "HTTP_METHOD_PUT",
        "HTTP_METHOD_PATCH",
        "HTTP_METHOD_DELETE",
        "HTTP_METHOD_HEAD",
        "HTTP_METHOD_OPTIONS",
    ]
    rawBody: str
    url: str

@typing.type_check_only
class ExecuteHttpRequestResponse(typing.TypedDict, total=False):
    body: str
    headers: _list[HttpHeader]
    reason: str
    statusCode: int

@typing.type_check_only
class ExecuteSqlQueryRequest(typing.TypedDict, total=False):
    query: Query

@typing.type_check_only
class ExecuteSqlQueryResponse(typing.TypedDict, total=False):
    results: _list[dict[str, typing.Any]]

@typing.type_check_only
class ExecuteToolRequest(typing.TypedDict, total=False):
    executionConfig: ExecutionConfig
    parameters: dict[str, typing.Any]
    toolDefinition: dict[str, typing.Any]

@typing.type_check_only
class ExecuteToolResponse(typing.TypedDict, total=False):
    _meta: dict[str, typing.Any]
    metadata: dict[str, typing.Any]
    result: dict[str, typing.Any]

@typing.type_check_only
class ExecutionConfig(typing.TypedDict, total=False):
    headers: str

@typing.type_check_only
class Field(typing.TypedDict, total=False):
    additionalDetails: dict[str, typing.Any]
    dataType: typing.Literal[
        "DATA_TYPE_UNSPECIFIED",
        "INT",
        "SMALLINT",
        "DOUBLE",
        "DATE",
        "DATETIME",
        "TIME",
        "STRING",
        "LONG",
        "BOOLEAN",
        "DECIMAL",
        "UUID",
        "BLOB",
        "BIT",
        "TINYINT",
        "INTEGER",
        "BIGINT",
        "FLOAT",
        "REAL",
        "NUMERIC",
        "CHAR",
        "VARCHAR",
        "LONGVARCHAR",
        "TIMESTAMP",
        "NCHAR",
        "NVARCHAR",
        "LONGNVARCHAR",
        "NULL",
        "OTHER",
        "JAVA_OBJECT",
        "DISTINCT",
        "STRUCT",
        "ARRAY",
        "CLOB",
        "REF",
        "DATALINK",
        "ROWID",
        "BINARY",
        "VARBINARY",
        "LONGVARBINARY",
        "NCLOB",
        "SQLXML",
        "REF_CURSOR",
        "TIME_WITH_TIMEZONE",
        "TIMESTAMP_WITH_TIMEZONE",
    ]
    defaultValue: typing.Any
    description: str
    jsonSchema: JsonSchema
    key: bool
    name: str
    nullable: bool
    reference: Reference

@typing.type_check_only
class GenerateCustomToolspecRequest(typing.TypedDict, total=False):
    toolNames: _list[ToolName]

@typing.type_check_only
class GenerateCustomToolspecResponse(typing.TypedDict, total=False):
    toolSpec: ToolSpec

@typing.type_check_only
class GetResourcePostRequest(typing.TypedDict, total=False):
    executionConfig: ExecutionConfig
    toolSpec: ToolSpec

@typing.type_check_only
class GetResourceResponse(typing.TypedDict, total=False):
    _meta: dict[str, typing.Any]
    data: str
    metadata: dict[str, typing.Any]
    mimeType: str

@typing.type_check_only
class HttpHeader(typing.TypedDict, total=False):
    key: str
    value: str

@typing.type_check_only
class InputParameter(typing.TypedDict, total=False):
    additionalDetails: dict[str, typing.Any]
    dataType: typing.Literal[
        "DATA_TYPE_UNSPECIFIED",
        "INT",
        "SMALLINT",
        "DOUBLE",
        "DATE",
        "DATETIME",
        "TIME",
        "STRING",
        "LONG",
        "BOOLEAN",
        "DECIMAL",
        "UUID",
        "BLOB",
        "BIT",
        "TINYINT",
        "INTEGER",
        "BIGINT",
        "FLOAT",
        "REAL",
        "NUMERIC",
        "CHAR",
        "VARCHAR",
        "LONGVARCHAR",
        "TIMESTAMP",
        "NCHAR",
        "NVARCHAR",
        "LONGNVARCHAR",
        "NULL",
        "OTHER",
        "JAVA_OBJECT",
        "DISTINCT",
        "STRUCT",
        "ARRAY",
        "CLOB",
        "REF",
        "DATALINK",
        "ROWID",
        "BINARY",
        "VARBINARY",
        "LONGVARBINARY",
        "NCLOB",
        "SQLXML",
        "REF_CURSOR",
        "TIME_WITH_TIMEZONE",
        "TIMESTAMP_WITH_TIMEZONE",
    ]
    defaultValue: typing.Any
    description: str
    jsonSchema: JsonSchema
    name: str
    nullable: bool

@typing.type_check_only
class Instance(typing.TypedDict, total=False):
    consumerDefinedName: str
    consumerProjectNumber: str
    createTime: str
    instanceType: str
    labels: dict[str, typing.Any]
    maintenancePolicyNames: dict[str, typing.Any]
    maintenanceSchedules: dict[str, typing.Any]
    maintenanceSettings: MaintenanceSettings
    name: str
    notificationParameters: dict[str, typing.Any]
    producerMetadata: dict[str, typing.Any]
    provisionedResources: _list[ProvisionedResource]
    slmInstanceTemplate: str
    sloMetadata: SloMetadata
    softwareVersions: dict[str, typing.Any]
    state: typing.Literal[
        "STATE_UNSPECIFIED",
        "CREATING",
        "READY",
        "UPDATING",
        "REPAIRING",
        "DELETING",
        "ERROR",
    ]
    tenantProjectId: str
    updateTime: str

AlternativeJsonSchema = typing.TypedDict(
    "AlternativeJsonSchema",
    {
        "$comment": str,
        "$defs": dict[str, typing.Any],
        "$id": str,
        "$ref": str,
        "$schema": str,
        "additionalDetails": dict[str, typing.Any],
        "additionalItems": JsonSchema,
        "additionalProperties": JsonSchema,
        "allOf": _list[JsonSchema],
        "anyOf": _list[JsonSchema],
        "const": typing.Any,
        "contains": JsonSchema,
        "contentEncoding": str,
        "contentMediaType": str,
        "default": typing.Any,
        "definitions": dict[str, typing.Any],
        "dependencies": dict[str, typing.Any],
        "description": str,
        "else": JsonSchema,
        "enum": _list[typing.Any],
        "examples": _list[typing.Any],
        "exclusiveMaximum": typing.Any,
        "exclusiveMinimum": typing.Any,
        "format": str,
        "if": JsonSchema,
        "items": JsonSchema,
        "jdbcType": typing.Literal[
            "DATA_TYPE_UNSPECIFIED",
            "INT",
            "SMALLINT",
            "DOUBLE",
            "DATE",
            "DATETIME",
            "TIME",
            "STRING",
            "LONG",
            "BOOLEAN",
            "DECIMAL",
            "UUID",
            "BLOB",
            "BIT",
            "TINYINT",
            "INTEGER",
            "BIGINT",
            "FLOAT",
            "REAL",
            "NUMERIC",
            "CHAR",
            "VARCHAR",
            "LONGVARCHAR",
            "TIMESTAMP",
            "NCHAR",
            "NVARCHAR",
            "LONGNVARCHAR",
            "NULL",
            "OTHER",
            "JAVA_OBJECT",
            "DISTINCT",
            "STRUCT",
            "ARRAY",
            "CLOB",
            "REF",
            "DATALINK",
            "ROWID",
            "BINARY",
            "VARBINARY",
            "LONGVARBINARY",
            "NCLOB",
            "SQLXML",
            "REF_CURSOR",
            "TIME_WITH_TIMEZONE",
            "TIMESTAMP_WITH_TIMEZONE",
        ],
        "maxItems": int,
        "maxLength": int,
        "maxProperties": int,
        "maximum": typing.Any,
        "minItems": int,
        "minLength": int,
        "minProperties": int,
        "minimum": typing.Any,
        "multipleOf": float,
        "not": JsonSchema,
        "oneOf": _list[JsonSchema],
        "pattern": str,
        "patternProperties": dict[str, typing.Any],
        "properties": dict[str, typing.Any],
        "propertyNames": JsonSchema,
        "readOnly": bool,
        "required": _list[str],
        "then": JsonSchema,
        "title": str,
        "type": _list[str],
        "uniqueItems": bool,
        "writeOnly": bool,
    },
    total=False,
)

@typing.type_check_only
class JsonSchema(AlternativeJsonSchema): ...

@typing.type_check_only
class ListActionsResponse(typing.TypedDict, total=False):
    actions: _list[Action]
    metadata: dict[str, typing.Any]
    nextPageToken: str
    unsupportedActionNames: _list[str]

@typing.type_check_only
class ListCustomToolNamesResponse(typing.TypedDict, total=False):
    toolNames: _list[ToolName]

@typing.type_check_only
class ListEntitiesResponse(typing.TypedDict, total=False):
    entities: _list[Entity]
    metadata: dict[str, typing.Any]
    nextPageToken: str

@typing.type_check_only
class ListEntityTypesResponse(typing.TypedDict, total=False):
    metadata: dict[str, typing.Any]
    nextPageToken: str
    types: _list[EntityType]
    unsupportedTypeNames: _list[str]

@typing.type_check_only
class ListResourcesResponse(typing.TypedDict, total=False):
    metadata: dict[str, typing.Any]
    nextPageToken: str
    resources: _list[Resource]

@typing.type_check_only
class ListToolsPostRequest(typing.TypedDict, total=False):
    executionConfig: ExecutionConfig
    pageSize: int
    pageToken: str
    toolNames: _list[str]
    toolSpec: ToolSpec

@typing.type_check_only
class ListToolsResponse(typing.TypedDict, total=False):
    metadata: dict[str, typing.Any]
    nextPageToken: str
    tools: _list[Tool]

@typing.type_check_only
class MaintenancePolicy(typing.TypedDict, total=False):
    createTime: str
    description: str
    labels: dict[str, typing.Any]
    name: str
    state: typing.Literal["STATE_UNSPECIFIED", "READY", "DELETING"]
    updatePolicy: UpdatePolicy
    updateTime: str

@typing.type_check_only
class MaintenanceSchedule(typing.TypedDict, total=False):
    canReschedule: bool
    endTime: str
    rolloutManagementPolicy: str
    scheduleDeadlineTime: str
    startTime: str

@typing.type_check_only
class MaintenanceSettings(typing.TypedDict, total=False):
    exclude: bool
    isRollback: bool
    maintenancePolicies: dict[str, typing.Any]

@typing.type_check_only
class MaintenanceWindow(typing.TypedDict, total=False):
    dailyCycle: DailyCycle
    weeklyCycle: WeeklyCycle

@typing.type_check_only
class NodeSloMetadata(typing.TypedDict, total=False):
    location: str
    nodeId: str
    perSliEligibility: PerSliSloEligibility

@typing.type_check_only
class NotificationParameter(typing.TypedDict, total=False):
    values: _list[str]

@typing.type_check_only
class OAuth2Config(typing.TypedDict, total=False):
    authUri: str
    clientId: str
    clientSecret: str

@typing.type_check_only
class PerSliSloEligibility(typing.TypedDict, total=False):
    eligibilities: dict[str, typing.Any]

@typing.type_check_only
class ProvisionedResource(typing.TypedDict, total=False):
    resourceType: str
    resourceUrl: str

@typing.type_check_only
class Query(typing.TypedDict, total=False):
    maxRows: str
    query: str
    queryParameters: _list[QueryParameter]
    timeout: str

@typing.type_check_only
class QueryParameter(typing.TypedDict, total=False):
    dataType: typing.Literal[
        "DATA_TYPE_UNSPECIFIED",
        "INT",
        "SMALLINT",
        "DOUBLE",
        "DATE",
        "DATETIME",
        "TIME",
        "STRING",
        "LONG",
        "BOOLEAN",
        "DECIMAL",
        "UUID",
        "BLOB",
        "BIT",
        "TINYINT",
        "INTEGER",
        "BIGINT",
        "FLOAT",
        "REAL",
        "NUMERIC",
        "CHAR",
        "VARCHAR",
        "LONGVARCHAR",
        "TIMESTAMP",
        "NCHAR",
        "NVARCHAR",
        "LONGNVARCHAR",
        "NULL",
        "OTHER",
        "JAVA_OBJECT",
        "DISTINCT",
        "STRUCT",
        "ARRAY",
        "CLOB",
        "REF",
        "DATALINK",
        "ROWID",
        "BINARY",
        "VARBINARY",
        "LONGVARBINARY",
        "NCLOB",
        "SQLXML",
        "REF_CURSOR",
        "TIME_WITH_TIMEZONE",
        "TIMESTAMP_WITH_TIMEZONE",
    ]
    value: typing.Any

@typing.type_check_only
class Reference(typing.TypedDict, total=False):
    name: str
    type: str

@typing.type_check_only
class RefreshAccessTokenRequest(typing.TypedDict, total=False):
    executionConfig: ExecutionConfig
    oauth2Config: OAuth2Config
    refreshToken: str

@typing.type_check_only
class RefreshAccessTokenResponse(typing.TypedDict, total=False):
    accessCredentials: AccessCredentials
    metadata: dict[str, typing.Any]

@typing.type_check_only
class Resource(typing.TypedDict, total=False):
    _meta: dict[str, typing.Any]
    description: str
    mimeType: str
    name: str
    size: str
    uri: str

@typing.type_check_only
class ResultMetadata(typing.TypedDict, total=False):
    dataType: typing.Literal[
        "DATA_TYPE_UNSPECIFIED",
        "INT",
        "SMALLINT",
        "DOUBLE",
        "DATE",
        "DATETIME",
        "TIME",
        "STRING",
        "LONG",
        "BOOLEAN",
        "DECIMAL",
        "UUID",
        "BLOB",
        "BIT",
        "TINYINT",
        "INTEGER",
        "BIGINT",
        "FLOAT",
        "REAL",
        "NUMERIC",
        "CHAR",
        "VARCHAR",
        "LONGVARCHAR",
        "TIMESTAMP",
        "NCHAR",
        "NVARCHAR",
        "LONGNVARCHAR",
        "NULL",
        "OTHER",
        "JAVA_OBJECT",
        "DISTINCT",
        "STRUCT",
        "ARRAY",
        "CLOB",
        "REF",
        "DATALINK",
        "ROWID",
        "BINARY",
        "VARBINARY",
        "LONGVARBINARY",
        "NCLOB",
        "SQLXML",
        "REF_CURSOR",
        "TIME_WITH_TIMEZONE",
        "TIMESTAMP_WITH_TIMEZONE",
    ]
    defaultValue: typing.Any
    description: str
    jsonSchema: JsonSchema
    name: str
    nullable: bool

@typing.type_check_only
class Schedule(typing.TypedDict, total=False):
    day: typing.Literal[
        "DAY_OF_WEEK_UNSPECIFIED",
        "MONDAY",
        "TUESDAY",
        "WEDNESDAY",
        "THURSDAY",
        "FRIDAY",
        "SATURDAY",
        "SUNDAY",
    ]
    duration: str
    startTime: TimeOfDay

@typing.type_check_only
class SloEligibility(typing.TypedDict, total=False):
    eligible: bool
    reason: str

@typing.type_check_only
class SloMetadata(typing.TypedDict, total=False):
    nodes: _list[NodeSloMetadata]
    perSliEligibility: PerSliSloEligibility
    tier: str

@typing.type_check_only
class TimeOfDay(typing.TypedDict, total=False):
    hours: int
    minutes: int
    nanos: int
    seconds: int

@typing.type_check_only
class Tool(typing.TypedDict, total=False):
    _meta: dict[str, typing.Any]
    annotations: ToolAnnotations
    dependsOn: _list[str]
    description: str
    inputSchema: JsonSchema
    name: str
    outputSchema: JsonSchema

@typing.type_check_only
class ToolAnnotations(typing.TypedDict, total=False):
    destructiveHint: bool
    idempotentHint: bool
    openWorldHint: bool
    readOnlyHint: bool
    title: str

@typing.type_check_only
class ToolName(typing.TypedDict, total=False):
    entityName: str
    name: str
    operation: typing.Literal[
        "OPERATION_UNSPECIFIED", "LIST", "GET", "CREATE", "UPDATE", "DELETE"
    ]

@typing.type_check_only
class ToolSpec(typing.TypedDict, total=False):
    toolDefinitions: _list[dict[str, typing.Any]]
    toolSpecVersion: str

@typing.type_check_only
class UpdateEntitiesWithConditionsResponse(typing.TypedDict, total=False):
    metadata: dict[str, typing.Any]
    response: dict[str, typing.Any]

@typing.type_check_only
class UpdatePolicy(typing.TypedDict, total=False):
    channel: typing.Literal[
        "UPDATE_CHANNEL_UNSPECIFIED", "EARLIER", "LATER", "WEEK1", "WEEK2", "WEEK5"
    ]
    denyMaintenancePeriods: _list[DenyMaintenancePeriod]
    window: MaintenanceWindow

@typing.type_check_only
class WeeklyCycle(typing.TypedDict, total=False):
    schedule: _list[Schedule]
