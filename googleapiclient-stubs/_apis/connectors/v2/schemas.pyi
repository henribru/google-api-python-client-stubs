import typing

import typing_extensions

_list = list

@typing.type_check_only
class AccessCredentials(typing_extensions.TypedDict, total=False):
    accessToken: str
    expiresIn: str
    refreshToken: str

@typing.type_check_only
class Action(typing_extensions.TypedDict, total=False):
    description: str
    displayName: str
    inputJsonSchema: JsonSchema
    inputParameters: _list[InputParameter]
    name: str
    resultJsonSchema: JsonSchema
    resultMetadata: _list[ResultMetadata]

@typing.type_check_only
class AuthCodeData(typing_extensions.TypedDict, total=False):
    authCode: str
    pkceVerifier: str
    redirectUri: str

@typing.type_check_only
class CheckReadinessResponse(typing_extensions.TypedDict, total=False):
    status: str

@typing.type_check_only
class CheckStatusResponse(typing_extensions.TypedDict, total=False):
    description: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "ACTIVE", "ERROR", "AUTH_ERROR"
    ]

@typing.type_check_only
class DailyCycle(typing_extensions.TypedDict, total=False):
    duration: str
    startTime: TimeOfDay

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
class Entity(typing_extensions.TypedDict, total=False):
    fields: dict[str, typing.Any]
    name: str

@typing.type_check_only
class EntityType(typing_extensions.TypedDict, total=False):
    fields: _list[Field]
    jsonSchema: JsonSchema
    name: str
    operations: _list[
        typing_extensions.Literal[
            "OPERATION_UNSPECIFIED", "LIST", "GET", "CREATE", "UPDATE", "DELETE"
        ]
    ]

@typing.type_check_only
class ExchangeAuthCodeRequest(typing_extensions.TypedDict, total=False):
    authCodeData: AuthCodeData

@typing.type_check_only
class ExchangeAuthCodeResponse(typing_extensions.TypedDict, total=False):
    accessCredentials: AccessCredentials

@typing.type_check_only
class ExecuteActionRequest(typing_extensions.TypedDict, total=False):
    parameters: dict[str, typing.Any]

@typing.type_check_only
class ExecuteActionResponse(typing_extensions.TypedDict, total=False):
    results: _list[dict[str, typing.Any]]

@typing.type_check_only
class ExecuteSqlQueryRequest(typing_extensions.TypedDict, total=False):
    query: Query

@typing.type_check_only
class ExecuteSqlQueryResponse(typing_extensions.TypedDict, total=False):
    results: _list[dict[str, typing.Any]]

@typing.type_check_only
class Field(typing_extensions.TypedDict, total=False):
    additionalDetails: dict[str, typing.Any]
    dataType: typing_extensions.Literal[
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
class InputParameter(typing_extensions.TypedDict, total=False):
    additionalDetails: dict[str, typing.Any]
    dataType: typing_extensions.Literal[
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
class Instance(typing_extensions.TypedDict, total=False):
    consumerDefinedName: str
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
    state: typing_extensions.Literal[
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

@typing.type_check_only
class JsonSchema(typing_extensions.TypedDict, total=False):
    additionalDetails: dict[str, typing.Any]
    default: typing.Any
    description: str
    enum: _list[typing.Any]
    format: str
    items: JsonSchema
    jdbcType: typing_extensions.Literal[
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
    properties: dict[str, typing.Any]
    required: _list[str]
    type: _list[str]

@typing.type_check_only
class ListActionsResponse(typing_extensions.TypedDict, total=False):
    actions: _list[Action]
    nextPageToken: str
    unsupportedActionNames: _list[str]

@typing.type_check_only
class ListEntitiesResponse(typing_extensions.TypedDict, total=False):
    entities: _list[Entity]
    nextPageToken: str

@typing.type_check_only
class ListEntityTypesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    types: _list[EntityType]
    unsupportedTypeNames: _list[str]

@typing.type_check_only
class MaintenancePolicy(typing_extensions.TypedDict, total=False):
    createTime: str
    description: str
    labels: dict[str, typing.Any]
    name: str
    state: typing_extensions.Literal["STATE_UNSPECIFIED", "READY", "DELETING"]
    updatePolicy: UpdatePolicy
    updateTime: str

@typing.type_check_only
class MaintenanceSchedule(typing_extensions.TypedDict, total=False):
    canReschedule: bool
    endTime: str
    rolloutManagementPolicy: str
    scheduleDeadlineTime: str
    startTime: str

@typing.type_check_only
class MaintenanceSettings(typing_extensions.TypedDict, total=False):
    exclude: bool
    isRollback: bool
    maintenancePolicies: dict[str, typing.Any]

@typing.type_check_only
class MaintenanceWindow(typing_extensions.TypedDict, total=False):
    dailyCycle: DailyCycle
    weeklyCycle: WeeklyCycle

@typing.type_check_only
class NodeSloMetadata(typing_extensions.TypedDict, total=False):
    location: str
    nodeId: str
    perSliEligibility: PerSliSloEligibility

@typing.type_check_only
class NotificationParameter(typing_extensions.TypedDict, total=False):
    values: _list[str]

@typing.type_check_only
class PerSliSloEligibility(typing_extensions.TypedDict, total=False):
    eligibilities: dict[str, typing.Any]

@typing.type_check_only
class ProvisionedResource(typing_extensions.TypedDict, total=False):
    resourceType: str
    resourceUrl: str

@typing.type_check_only
class Query(typing_extensions.TypedDict, total=False):
    maxRows: str
    query: str
    queryParameters: _list[QueryParameter]
    timeout: str

@typing.type_check_only
class QueryParameter(typing_extensions.TypedDict, total=False):
    dataType: typing_extensions.Literal[
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
class Reference(typing_extensions.TypedDict, total=False):
    name: str
    type: str

@typing.type_check_only
class RefreshAccessTokenRequest(typing_extensions.TypedDict, total=False):
    refreshToken: str

@typing.type_check_only
class RefreshAccessTokenResponse(typing_extensions.TypedDict, total=False):
    accessCredentials: AccessCredentials

@typing.type_check_only
class ResultMetadata(typing_extensions.TypedDict, total=False):
    dataType: typing_extensions.Literal[
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
class Schedule(typing_extensions.TypedDict, total=False):
    day: typing_extensions.Literal[
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
class SloEligibility(typing_extensions.TypedDict, total=False):
    eligible: bool
    reason: str

@typing.type_check_only
class SloMetadata(typing_extensions.TypedDict, total=False):
    nodes: _list[NodeSloMetadata]
    perSliEligibility: PerSliSloEligibility
    tier: str

@typing.type_check_only
class TimeOfDay(typing_extensions.TypedDict, total=False):
    hours: int
    minutes: int
    nanos: int
    seconds: int

@typing.type_check_only
class UpdateEntitiesWithConditionsResponse(typing_extensions.TypedDict, total=False):
    response: dict[str, typing.Any]

@typing.type_check_only
class UpdatePolicy(typing_extensions.TypedDict, total=False):
    channel: typing_extensions.Literal[
        "UPDATE_CHANNEL_UNSPECIFIED", "EARLIER", "LATER", "WEEK1", "WEEK2", "WEEK5"
    ]
    denyMaintenancePeriods: _list[DenyMaintenancePeriod]
    window: MaintenanceWindow

@typing.type_check_only
class WeeklyCycle(typing_extensions.TypedDict, total=False):
    schedule: _list[Schedule]
