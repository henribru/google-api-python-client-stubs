import typing

import typing_extensions

_list = list

@typing.type_check_only
class CrmlogErrorCode(typing_extensions.TypedDict, total=False):
    commonErrorCode: typing_extensions.Literal[
        "COMMON_ERROR_CODE_UNSPECIFIED",
        "INVALID_CREDENTIALS",
        "REQUIRED_FIELDS_MISSING",
        "INVALID_FIELDS",
        "BACKEND",
        "GENERAL",
        "INTERNAL",
        "IO_ERROR",
        "NOT_FOUND",
        "EVENT_BUS",
        "ALREADY_EXISTS",
        "CONCORD",
        "CONVERSION",
        "FLUME",
        "PERMISSION",
        "SALES_FORCE",
        "SPANNER",
        "UNIMPLEMENTED",
        "RELTIO",
        "WORKFLOW_NOT_FOUND",
        "QUOTA_THROTTLED",
        "QUOTA_ENQUEUED",
        "INVALID_QUOTA_CONFIGURATION",
        "TASK_NOT_FOUND",
        "EXECUTION_TIMEOUT",
        "INVALID_EVENT_EXECUTION_STATE",
        "INVALID_ATTRIBUTE",
        "MISSING_ATTRIBUTE",
        "CLIENT_UNAUTHORIZED_FOR_WORKFLOW",
        "INVALID_PARAMETER",
        "MISSING_PARAMETER",
        "UNAUTHROIZED_WORKFLOW_EDITOR_ACTION",
        "FAILED_PRECONDITION",
        "INVALID_CLIENT",
        "MISSING_CLIENT",
        "INVALID_WORKFLOW",
        "MISSING_QUOTA_CONFIGURATION",
        "UNHANDLED_TASK_ERROR",
        "SCRIPT_TASK_RUNTIME_ERROR",
        "RPC",
        "INVALID_PROTO",
        "UNHANDLED_EVENTBUS_ERROR",
        "INVALID_TASK_STATE",
        "TYPED_TASK_INVALID_INPUT_OPERATION",
        "TYPED_TASK_INVALID_OUTPUT_OPERATION",
        "VALIDATION_ERROR",
        "RESUME_ERROR",
        "APPS_SCRIPT_EXECUTION_ERROR",
        "INVALID_VECTOR_USER",
        "INFORMATICA",
        "RETRYABLE_TASK_ERROR",
        "INVALID_TENANT",
        "WRONG_TENANT",
        "INFORMATICA_BACKEND_UNAVAILABLE",
        "RPC_PERMISSION_DENIED",
        "SYNC_EVENTBUS_EXECUTION_TIMEOUT",
        "ASYNC_EVENTBUS_EXECUTION_TIMEOUT",
        "NOT_SUPPORTED_DATA_TYPE",
        "UNSANITIZED_USER_INPUT",
        "TRANSFORM_EXPRESSION_EVALUATION_ERROR",
        "HTTP_EXCEPTION",
        "EXECUTION_CANCELLED",
    ]

@typing.type_check_only
class EnterpriseCrmCardsCellValue(typing_extensions.TypedDict, total=False):
    booleanValue: bool
    doubleValue: float
    empty: GoogleProtobufEmpty
    longValue: str
    stringValue: str

@typing.type_check_only
class EnterpriseCrmCardsRow(typing_extensions.TypedDict, total=False):
    cells: _list[EnterpriseCrmCardsCellValue]

@typing.type_check_only
class EnterpriseCrmCardsTabularData(typing_extensions.TypedDict, total=False):
    headers: _list[str]
    rows: _list[EnterpriseCrmCardsRow]

@typing.type_check_only
class EnterpriseCrmCardsTemplatesAplosSeriesData(
    typing_extensions.TypedDict, total=False
):
    rows: _list[EnterpriseCrmCardsTemplatesAplosSeriesDataRow]

@typing.type_check_only
class EnterpriseCrmCardsTemplatesAplosSeriesDataRow(
    typing_extensions.TypedDict, total=False
):
    x: EnterpriseCrmCardsCellValue
    y: EnterpriseCrmCardsCellValue

@typing.type_check_only
class EnterpriseCrmCardsTemplatesAplosSeriesListData(
    typing_extensions.TypedDict, total=False
):
    series: _list[EnterpriseCrmCardsTemplatesAplosSeriesListDataSeries]

@typing.type_check_only
class EnterpriseCrmCardsTemplatesAplosSeriesListDataSeries(
    typing_extensions.TypedDict, total=False
):
    data: EnterpriseCrmCardsTemplatesAplosSeriesData
    name: str

@typing.type_check_only
class EnterpriseCrmEventbusAuthconfigAuthConfigTaskParam(
    typing_extensions.TypedDict, total=False
):
    allowedCredentialTypes: _list[str]
    allowedServiceAccountInContext: bool
    authConfigId: str
    scope: str
    useServiceAccountInContext: bool

@typing.type_check_only
class EnterpriseCrmEventbusProtoAddress(typing_extensions.TypedDict, total=False):
    email: str
    name: str
    tokens: _list[EnterpriseCrmEventbusProtoToken]

@typing.type_check_only
class EnterpriseCrmEventbusProtoAttributes(typing_extensions.TypedDict, total=False):
    dataType: typing_extensions.Literal[
        "DATA_TYPE_UNSPECIFIED", "EMAIL", "URL", "CURRENCY", "TIMESTAMP", "DOMAIN_NAME"
    ]
    defaultValue: EnterpriseCrmEventbusProtoValueType
    isRequired: bool
    isSearchable: bool
    logSettings: EnterpriseCrmEventbusProtoLogSettings
    searchable: typing_extensions.Literal["UNSPECIFIED", "YES", "NO"]
    taskVisibility: _list[str]

@typing.type_check_only
class EnterpriseCrmEventbusProtoBaseAlertConfigErrorEnumList(
    typing_extensions.TypedDict, total=False
):
    enumStrings: _list[str]
    filterType: typing_extensions.Literal["DEFAULT_INCLUSIVE", "EXCLUSIVE"]

@typing.type_check_only
class EnterpriseCrmEventbusProtoBaseAlertConfigThresholdValue(
    typing_extensions.TypedDict, total=False
):
    absolute: str
    percentage: int

@typing.type_check_only
class EnterpriseCrmEventbusProtoBaseFunction(typing_extensions.TypedDict, total=False):
    functionName: typing_extensions.Literal[
        "UNSPECIFIED",
        "NOW_IN_MILLIS",
        "INT_LIST",
        "ENVIRONMENT",
        "GET_EXECUTION_ID",
        "GET_INTEGRATION_NAME",
        "GET_REGION",
        "GET_UUID",
        "GET_PROJECT_ID",
    ]

@typing.type_check_only
class EnterpriseCrmEventbusProtoBaseValue(typing_extensions.TypedDict, total=False):
    baseFunction: EnterpriseCrmEventbusProtoFunction
    literalValue: EnterpriseCrmEventbusProtoParameterValueType
    referenceValue: str

@typing.type_check_only
class EnterpriseCrmEventbusProtoBooleanArrayFunction(
    typing_extensions.TypedDict, total=False
):
    functionName: typing_extensions.Literal[
        "UNSPECIFIED",
        "GET",
        "APPEND",
        "SIZE",
        "TO_SET",
        "APPEND_ALL",
        "TO_JSON",
        "SET",
        "REMOVE",
        "REMOVE_AT",
        "CONTAINS",
        "FOR_EACH",
        "FILTER",
    ]

@typing.type_check_only
class EnterpriseCrmEventbusProtoBooleanFunction(
    typing_extensions.TypedDict, total=False
):
    functionName: typing_extensions.Literal[
        "UNSPECIFIED",
        "TO_JSON",
        "NOT",
        "AND",
        "NAND",
        "OR",
        "XOR",
        "NOR",
        "XNOR",
        "TO_STRING",
        "EQUALS",
    ]

@typing.type_check_only
class EnterpriseCrmEventbusProtoBooleanParameterArray(
    typing_extensions.TypedDict, total=False
):
    booleanValues: _list[bool]

@typing.type_check_only
class EnterpriseCrmEventbusProtoBuganizerNotification(
    typing_extensions.TypedDict, total=False
):
    assigneeEmailAddress: str
    componentId: str
    templateId: str
    title: str

@typing.type_check_only
class EnterpriseCrmEventbusProtoCombinedCondition(
    typing_extensions.TypedDict, total=False
):
    conditions: _list[EnterpriseCrmEventbusProtoCondition]

@typing.type_check_only
class EnterpriseCrmEventbusProtoCondition(typing_extensions.TypedDict, total=False):
    eventPropertyKey: str
    operator: typing_extensions.Literal[
        "UNSET",
        "EQUALS",
        "CONTAINS",
        "LESS_THAN",
        "GREATER_THAN",
        "EXISTS",
        "DOES_NOT_EXIST",
        "IS_EMPTY",
        "IS_NOT_EMPTY",
    ]
    value: EnterpriseCrmEventbusProtoValueType

@typing.type_check_only
class EnterpriseCrmEventbusProtoConditionResult(
    typing_extensions.TypedDict, total=False
):
    currentTaskNumber: str
    nextTaskNumber: str
    result: bool

@typing.type_check_only
class EnterpriseCrmEventbusProtoConnectorsConnection(
    typing_extensions.TypedDict, total=False
):
    connectionName: str
    connectorVersion: str
    serviceName: str

@typing.type_check_only
class EnterpriseCrmEventbusProtoConnectorsGenericConnectorTaskConfig(
    typing_extensions.TypedDict, total=False
):
    connection: EnterpriseCrmEventbusProtoConnectorsConnection
    operation: typing_extensions.Literal[
        "OPERATION_UNSPECIFIED",
        "EXECUTE_ACTION",
        "LIST_ENTITIES",
        "GET_ENTITY",
        "CREATE_ENTITY",
        "UPDATE_ENTITY",
        "DELETE_ENTITY",
    ]

@typing.type_check_only
class EnterpriseCrmEventbusProtoCoordinate(typing_extensions.TypedDict, total=False):
    x: int
    y: int

@typing.type_check_only
class EnterpriseCrmEventbusProtoCustomSuspensionRequest(
    typing_extensions.TypedDict, total=False
):
    postToQueueWithTriggerIdRequest: GoogleInternalCloudCrmEventbusV3PostToQueueWithTriggerIdRequest
    suspensionInfoEventParameterKey: str

@typing.type_check_only
class EnterpriseCrmEventbusProtoDoubleArray(typing_extensions.TypedDict, total=False):
    values: _list[float]

@typing.type_check_only
class EnterpriseCrmEventbusProtoDoubleArrayFunction(
    typing_extensions.TypedDict, total=False
):
    functionName: typing_extensions.Literal[
        "UNSPECIFIED",
        "GET",
        "APPEND",
        "SIZE",
        "SUM",
        "AVG",
        "MAX",
        "MIN",
        "TO_SET",
        "APPEND_ALL",
        "TO_JSON",
        "SET",
        "REMOVE",
        "REMOVE_AT",
        "CONTAINS",
        "FOR_EACH",
        "FILTER",
    ]

@typing.type_check_only
class EnterpriseCrmEventbusProtoDoubleFunction(
    typing_extensions.TypedDict, total=False
):
    functionName: typing_extensions.Literal[
        "UNSPECIFIED",
        "TO_JSON",
        "TO_STRING",
        "ADD",
        "SUBTRACT",
        "MULTIPLY",
        "DIVIDE",
        "EXPONENT",
        "ROUND",
        "FLOOR",
        "CEIL",
        "GREATER_THAN",
        "LESS_THAN",
        "EQUALS",
        "GREATER_THAN_EQUALS",
        "LESS_THAN_EQUALS",
        "MOD",
    ]

@typing.type_check_only
class EnterpriseCrmEventbusProtoDoubleParameterArray(
    typing_extensions.TypedDict, total=False
):
    doubleValues: _list[float]

@typing.type_check_only
class EnterpriseCrmEventbusProtoErrorDetail(typing_extensions.TypedDict, total=False):
    errorCode: CrmlogErrorCode
    errorMessage: str
    severity: typing_extensions.Literal["SEVERITY_UNSPECIFIED", "ERROR", "WARN", "INFO"]
    taskNumber: int

@typing.type_check_only
class EnterpriseCrmEventbusProtoEventBusProperties(
    typing_extensions.TypedDict, total=False
):
    properties: _list[EnterpriseCrmEventbusProtoPropertyEntry]

@typing.type_check_only
class EnterpriseCrmEventbusProtoEventExecutionDetails(
    typing_extensions.TypedDict, total=False
):
    eventAttemptStats: _list[
        EnterpriseCrmEventbusProtoEventExecutionDetailsEventAttemptStats
    ]
    eventExecutionSnapshot: _list[EnterpriseCrmEventbusProtoEventExecutionSnapshot]
    eventExecutionState: typing_extensions.Literal[
        "UNSPECIFIED",
        "ON_HOLD",
        "IN_PROCESS",
        "SUCCEEDED",
        "FAILED",
        "CANCELED",
        "RETRY_ON_HOLD",
        "SUSPENDED",
    ]
    eventRetriesFromBeginningCount: int
    logFilePath: str
    networkAddress: str
    nextExecutionTime: str
    ryeLockUnheldCount: int

@typing.type_check_only
class EnterpriseCrmEventbusProtoEventExecutionDetailsEventAttemptStats(
    typing_extensions.TypedDict, total=False
):
    endTime: str
    startTime: str

@typing.type_check_only
class EnterpriseCrmEventbusProtoEventExecutionSnapshot(
    typing_extensions.TypedDict, total=False
):
    checkpointTaskNumber: str
    conditionResults: _list[EnterpriseCrmEventbusProtoConditionResult]
    diffParams: EnterpriseCrmEventbusProtoEventParameters
    eventExecutionInfoId: str
    eventExecutionSnapshotId: str
    eventExecutionSnapshotMetadata: EnterpriseCrmEventbusProtoEventExecutionSnapshotEventExecutionSnapshotMetadata
    eventParams: EnterpriseCrmEventbusProtoEventParameters
    exceedMaxSize: bool
    snapshotTime: str
    taskExecutionDetails: _list[EnterpriseCrmEventbusProtoTaskExecutionDetails]
    taskName: str

@typing.type_check_only
class EnterpriseCrmEventbusProtoEventExecutionSnapshotEventExecutionSnapshotMetadata(
    typing_extensions.TypedDict, total=False
):
    eventAttemptNum: int
    taskAttemptNum: int
    taskName: str
    taskNumber: str

@typing.type_check_only
class EnterpriseCrmEventbusProtoEventParameters(
    typing_extensions.TypedDict, total=False
):
    parameters: _list[EnterpriseCrmEventbusProtoParameterEntry]

@typing.type_check_only
class EnterpriseCrmEventbusProtoExecutionTraceInfo(
    typing_extensions.TypedDict, total=False
):
    parentEventExecutionInfoId: str
    traceId: str

@typing.type_check_only
class EnterpriseCrmEventbusProtoExternalTraffic(
    typing_extensions.TypedDict, total=False
):
    gcpProjectId: str
    gcpProjectNumber: str
    location: str
    source: typing_extensions.Literal["SOURCE_UNSPECIFIED", "APIGEE", "SECURITY"]

@typing.type_check_only
class EnterpriseCrmEventbusProtoFailurePolicy(typing_extensions.TypedDict, total=False):
    intervalInSeconds: str
    maxNumRetries: int
    retryStrategy: typing_extensions.Literal[
        "UNSPECIFIED",
        "IGNORE",
        "NONE",
        "FATAL",
        "FIXED_INTERVAL",
        "LINEAR_BACKOFF",
        "EXPONENTIAL_BACKOFF",
        "RESTART_WORKFLOW_WITH_BACKOFF",
    ]

@typing.type_check_only
class EnterpriseCrmEventbusProtoField(typing_extensions.TypedDict, total=False):
    cardinality: typing_extensions.Literal["UNSPECIFIED", "OPTIONAL"]
    defaultValue: EnterpriseCrmEventbusProtoParameterValueType
    fieldType: typing_extensions.Literal[
        "DATA_TYPE_UNSPECIFIED",
        "STRING_VALUE",
        "INT_VALUE",
        "DOUBLE_VALUE",
        "BOOLEAN_VALUE",
        "PROTO_VALUE",
        "SERIALIZED_OBJECT_VALUE",
        "STRING_ARRAY",
        "INT_ARRAY",
        "DOUBLE_ARRAY",
        "PROTO_ARRAY",
        "PROTO_ENUM",
        "BOOLEAN_ARRAY",
        "PROTO_ENUM_ARRAY",
        "BYTES",
        "BYTES_ARRAY",
        "NON_SERIALIZABLE_OBJECT",
        "JSON_VALUE",
    ]
    protoDefPath: str
    referenceKey: str
    transformExpression: EnterpriseCrmEventbusProtoTransformExpression

@typing.type_check_only
class EnterpriseCrmEventbusProtoFieldMappingConfig(
    typing_extensions.TypedDict, total=False
):
    mappedFields: _list[EnterpriseCrmEventbusProtoMappedField]

@typing.type_check_only
class EnterpriseCrmEventbusProtoFunction(dict[str, typing.Any]): ...

@typing.type_check_only
class EnterpriseCrmEventbusProtoFunctionType(typing_extensions.TypedDict, total=False):
    baseFunction: EnterpriseCrmEventbusProtoBaseFunction
    booleanArrayFunction: EnterpriseCrmEventbusProtoBooleanArrayFunction
    booleanFunction: EnterpriseCrmEventbusProtoBooleanFunction
    doubleArrayFunction: EnterpriseCrmEventbusProtoDoubleArrayFunction
    doubleFunction: EnterpriseCrmEventbusProtoDoubleFunction
    intArrayFunction: EnterpriseCrmEventbusProtoIntArrayFunction
    intFunction: EnterpriseCrmEventbusProtoIntFunction
    jsonFunction: EnterpriseCrmEventbusProtoJsonFunction
    protoArrayFunction: EnterpriseCrmEventbusProtoProtoArrayFunction
    protoFunction: EnterpriseCrmEventbusProtoProtoFunction
    stringArrayFunction: EnterpriseCrmEventbusProtoStringArrayFunction
    stringFunction: EnterpriseCrmEventbusProtoStringFunction

@typing.type_check_only
class EnterpriseCrmEventbusProtoIntArray(typing_extensions.TypedDict, total=False):
    values: _list[str]

@typing.type_check_only
class EnterpriseCrmEventbusProtoIntArrayFunction(
    typing_extensions.TypedDict, total=False
):
    functionName: typing_extensions.Literal[
        "UNSPECIFIED",
        "GET",
        "APPEND",
        "SIZE",
        "SUM",
        "AVG",
        "MAX",
        "MIN",
        "TO_SET",
        "APPEND_ALL",
        "TO_JSON",
        "SET",
        "REMOVE",
        "REMOVE_AT",
        "CONTAINS",
        "FOR_EACH",
        "FILTER",
    ]

@typing.type_check_only
class EnterpriseCrmEventbusProtoIntFunction(typing_extensions.TypedDict, total=False):
    functionName: typing_extensions.Literal[
        "UNSPECIFIED",
        "ADD",
        "SUBTRACT",
        "MULTIPLY",
        "DIVIDE",
        "EXPONENT",
        "GREATER_THAN_EQUAL_TO",
        "GREATER_THAN",
        "LESS_THAN_EQUAL_TO",
        "LESS_THAN",
        "TO_DOUBLE",
        "TO_STRING",
        "EQUALS",
        "TO_JSON",
        "MOD",
        "EPOCH_TO_HUMAN_READABLE_TIME",
    ]

@typing.type_check_only
class EnterpriseCrmEventbusProtoIntParameterArray(
    typing_extensions.TypedDict, total=False
):
    intValues: _list[str]

@typing.type_check_only
class EnterpriseCrmEventbusProtoJsonFunction(typing_extensions.TypedDict, total=False):
    functionName: typing_extensions.Literal[
        "UNSPECIFIED",
        "GET_PROPERTY",
        "GET_ELEMENT",
        "APPEND_ELEMENT",
        "SIZE",
        "SET_PROPERTY",
        "FLATTEN",
        "FLATTEN_ONCE",
        "MERGE",
        "TO_STRING",
        "TO_INT",
        "TO_DOUBLE",
        "TO_BOOLEAN",
        "TO_PROTO",
        "TO_STRING_ARRAY",
        "TO_INT_ARRAY",
        "TO_DOUBLE_ARRAY",
        "TO_PROTO_ARRAY",
        "TO_BOOLEAN_ARRAY",
        "REMOVE_PROPERTY",
        "RESOLVE_TEMPLATE",
        "EQUALS",
        "FOR_EACH",
        "FILTER_ELEMENTS",
    ]

@typing.type_check_only
class EnterpriseCrmEventbusProtoLogSettings(typing_extensions.TypedDict, total=False):
    logFieldName: str
    sanitizeOptions: EnterpriseCrmLoggingGwsSanitizeOptions
    seedPeriod: typing_extensions.Literal[
        "SEED_PERIOD_UNSPECIFIED", "DAY", "WEEK", "MONTH"
    ]
    seedScope: typing_extensions.Literal[
        "SEED_SCOPE_UNSPECIFIED", "EVENT_NAME", "TIME_PERIOD", "PARAM_NAME"
    ]
    shorteningLimits: EnterpriseCrmLoggingGwsFieldLimits

@typing.type_check_only
class EnterpriseCrmEventbusProtoLoopMetadata(typing_extensions.TypedDict, total=False):
    currentIterationCount: str
    currentIterationDetail: str
    errorMsg: str
    failureLocation: typing_extensions.Literal[
        "UNKNOWN",
        "SUBWORKFLOW",
        "PARAM_OVERRIDING",
        "PARAM_AGGREGATING",
        "SETTING_ITERATION_ELEMENT",
        "GETTING_LIST_TO_ITERATE",
        "CONDITION_EVALUATION",
        "BUILDING_REQUEST",
    ]

@typing.type_check_only
class EnterpriseCrmEventbusProtoMappedField(dict[str, typing.Any]): ...

@typing.type_check_only
class EnterpriseCrmEventbusProtoNextTask(typing_extensions.TypedDict, total=False):
    combinedConditions: _list[EnterpriseCrmEventbusProtoCombinedCondition]
    condition: str
    description: str
    label: str
    taskConfigId: str
    taskNumber: str

@typing.type_check_only
class EnterpriseCrmEventbusProtoNextTeardownTask(
    typing_extensions.TypedDict, total=False
):
    name: str

@typing.type_check_only
class EnterpriseCrmEventbusProtoNodeIdentifier(
    typing_extensions.TypedDict, total=False
):
    elementIdentifier: str
    elementType: typing_extensions.Literal[
        "UNKNOWN_TYPE", "TASK_CONFIG", "TRIGGER_CONFIG"
    ]

@typing.type_check_only
class EnterpriseCrmEventbusProtoNotification(typing_extensions.TypedDict, total=False):
    buganizerNotification: EnterpriseCrmEventbusProtoBuganizerNotification
    emailAddress: EnterpriseCrmEventbusProtoAddress
    escalatorQueue: str
    pubsubTopic: str
    request: EnterpriseCrmEventbusProtoCustomSuspensionRequest

@typing.type_check_only
class EnterpriseCrmEventbusProtoParamSpecEntryConfig(
    typing_extensions.TypedDict, total=False
):
    descriptivePhrase: str
    helpText: str
    hideDefaultValue: bool
    inputDisplayOption: typing_extensions.Literal[
        "DEFAULT", "STRING_MULTI_LINE", "NUMBER_SLIDER", "BOOLEAN_TOGGLE"
    ]
    isHidden: bool
    label: str
    parameterNameOption: typing_extensions.Literal[
        "DEFAULT_NOT_PARAMETER_NAME",
        "IS_PARAMETER_NAME",
        "KEY_IS_PARAMETER_NAME",
        "VALUE_IS_PARAMETER_NAME",
    ]
    subSectionLabel: str
    uiPlaceholderText: str

@typing.type_check_only
class EnterpriseCrmEventbusProtoParamSpecEntryProtoDefinition(
    typing_extensions.TypedDict, total=False
):
    fullName: str
    path: str

@typing.type_check_only
class EnterpriseCrmEventbusProtoParamSpecEntryValidationRule(
    typing_extensions.TypedDict, total=False
):
    doubleRange: EnterpriseCrmEventbusProtoParamSpecEntryValidationRuleDoubleRange
    intRange: EnterpriseCrmEventbusProtoParamSpecEntryValidationRuleIntRange
    stringRegex: EnterpriseCrmEventbusProtoParamSpecEntryValidationRuleStringRegex

@typing.type_check_only
class EnterpriseCrmEventbusProtoParamSpecEntryValidationRuleDoubleRange(
    typing_extensions.TypedDict, total=False
):
    max: float
    min: float

@typing.type_check_only
class EnterpriseCrmEventbusProtoParamSpecEntryValidationRuleIntRange(
    typing_extensions.TypedDict, total=False
):
    max: str
    min: str

@typing.type_check_only
class EnterpriseCrmEventbusProtoParamSpecEntryValidationRuleStringRegex(
    typing_extensions.TypedDict, total=False
):
    exclusive: bool
    regex: str

@typing.type_check_only
class EnterpriseCrmEventbusProtoParameterEntry(
    typing_extensions.TypedDict, total=False
):
    key: str
    value: EnterpriseCrmEventbusProtoParameterValueType

@typing.type_check_only
class EnterpriseCrmEventbusProtoParameterMap(typing_extensions.TypedDict, total=False):
    entries: _list[EnterpriseCrmEventbusProtoParameterMapEntry]
    keyType: typing_extensions.Literal[
        "DATA_TYPE_UNSPECIFIED",
        "STRING_VALUE",
        "INT_VALUE",
        "DOUBLE_VALUE",
        "BOOLEAN_VALUE",
        "PROTO_VALUE",
        "SERIALIZED_OBJECT_VALUE",
        "STRING_ARRAY",
        "INT_ARRAY",
        "DOUBLE_ARRAY",
        "PROTO_ARRAY",
        "PROTO_ENUM",
        "BOOLEAN_ARRAY",
        "PROTO_ENUM_ARRAY",
        "BYTES",
        "BYTES_ARRAY",
        "NON_SERIALIZABLE_OBJECT",
        "JSON_VALUE",
    ]
    valueType: typing_extensions.Literal[
        "DATA_TYPE_UNSPECIFIED",
        "STRING_VALUE",
        "INT_VALUE",
        "DOUBLE_VALUE",
        "BOOLEAN_VALUE",
        "PROTO_VALUE",
        "SERIALIZED_OBJECT_VALUE",
        "STRING_ARRAY",
        "INT_ARRAY",
        "DOUBLE_ARRAY",
        "PROTO_ARRAY",
        "PROTO_ENUM",
        "BOOLEAN_ARRAY",
        "PROTO_ENUM_ARRAY",
        "BYTES",
        "BYTES_ARRAY",
        "NON_SERIALIZABLE_OBJECT",
        "JSON_VALUE",
    ]

@typing.type_check_only
class EnterpriseCrmEventbusProtoParameterMapEntry(
    typing_extensions.TypedDict, total=False
):
    key: EnterpriseCrmEventbusProtoParameterMapField
    value: EnterpriseCrmEventbusProtoParameterMapField

@typing.type_check_only
class EnterpriseCrmEventbusProtoParameterMapField(
    typing_extensions.TypedDict, total=False
):
    literalValue: EnterpriseCrmEventbusProtoParameterValueType
    referenceKey: str

@typing.type_check_only
class EnterpriseCrmEventbusProtoParameterValueType(
    typing_extensions.TypedDict, total=False
):
    booleanArray: EnterpriseCrmEventbusProtoBooleanParameterArray
    booleanValue: bool
    doubleArray: EnterpriseCrmEventbusProtoDoubleParameterArray
    doubleValue: float
    intArray: EnterpriseCrmEventbusProtoIntParameterArray
    intValue: str
    protoArray: EnterpriseCrmEventbusProtoProtoParameterArray
    protoValue: dict[str, typing.Any]
    serializedObjectValue: EnterpriseCrmEventbusProtoSerializedObjectParameter
    stringArray: EnterpriseCrmEventbusProtoStringParameterArray
    stringValue: str

@typing.type_check_only
class EnterpriseCrmEventbusProtoPropertyEntry(typing_extensions.TypedDict, total=False):
    key: str
    value: EnterpriseCrmEventbusProtoValueType

@typing.type_check_only
class EnterpriseCrmEventbusProtoProtoArrayFunction(
    typing_extensions.TypedDict, total=False
):
    functionName: typing_extensions.Literal[
        "UNSPECIFIED",
        "GET",
        "APPEND",
        "SIZE",
        "TO_SET",
        "APPEND_ALL",
        "TO_JSON",
        "SET",
        "REMOVE",
        "REMOVE_AT",
        "CONTAINS",
        "FOR_EACH",
        "FILTER",
    ]

@typing.type_check_only
class EnterpriseCrmEventbusProtoProtoFunction(typing_extensions.TypedDict, total=False):
    functionName: typing_extensions.Literal[
        "UNSPECIFIED",
        "GET_STRING_SUBFIELD",
        "GET_INT_SUBFIELD",
        "GET_DOUBLE_SUBFIELD",
        "GET_BOOLEAN_SUBFIELD",
        "GET_STRING_ARRAY_SUBFIELD",
        "GET_INT_ARRAY_SUBFIELD",
        "GET_DOUBLE_ARRAY_SUBFIELD",
        "GET_BOOLEAN_ARRAY_SUBFIELD",
        "GET_PROTO_ARRAY_SUBFIELD",
        "GET_PROTO_SUBFIELD",
        "TO_JSON",
        "GET_BYTES_SUBFIELD_AS_UTF_8_STRING",
        "GET_BYTES_SUBFIELD_AS_PROTO",
        "EQUALS",
    ]

@typing.type_check_only
class EnterpriseCrmEventbusProtoProtoParameterArray(
    typing_extensions.TypedDict, total=False
):
    protoValues: _list[dict[str, typing.Any]]

@typing.type_check_only
class EnterpriseCrmEventbusProtoScatterResponse(
    typing_extensions.TypedDict, total=False
):
    errorMsg: str
    executionIds: _list[str]
    isSuccessful: bool
    responseParams: _list[EnterpriseCrmEventbusProtoParameterEntry]
    scatterElement: EnterpriseCrmEventbusProtoParameterValueType

@typing.type_check_only
class EnterpriseCrmEventbusProtoSerializedObjectParameter(
    typing_extensions.TypedDict, total=False
):
    objectValue: str

@typing.type_check_only
class EnterpriseCrmEventbusProtoStringArray(typing_extensions.TypedDict, total=False):
    values: _list[str]

@typing.type_check_only
class EnterpriseCrmEventbusProtoStringArrayFunction(
    typing_extensions.TypedDict, total=False
):
    functionName: typing_extensions.Literal[
        "UNSPECIFIED",
        "GET",
        "APPEND",
        "SIZE",
        "TO_SET",
        "APPEND_ALL",
        "TO_JSON",
        "SET",
        "REMOVE",
        "REMOVE_AT",
        "CONTAINS",
        "FOR_EACH",
        "FILTER",
    ]

@typing.type_check_only
class EnterpriseCrmEventbusProtoStringFunction(
    typing_extensions.TypedDict, total=False
):
    functionName: typing_extensions.Literal[
        "UNSPECIFIED",
        "CONCAT",
        "TO_UPPERCASE",
        "TO_LOWERCASE",
        "CONTAINS",
        "SPLIT",
        "LENGTH",
        "EQUALS",
        "TO_INT",
        "TO_DOUBLE",
        "TO_BOOLEAN",
        "TO_BASE_64",
        "TO_JSON",
        "EQUALS_IGNORE_CASE",
        "REPLACE_ALL",
        "SUBSTRING",
        "RESOLVE_TEMPLATE",
    ]

@typing.type_check_only
class EnterpriseCrmEventbusProtoStringParameterArray(
    typing_extensions.TypedDict, total=False
):
    stringValues: _list[str]

@typing.type_check_only
class EnterpriseCrmEventbusProtoSuccessPolicy(typing_extensions.TypedDict, total=False):
    finalState: typing_extensions.Literal["UNSPECIFIED", "SUCCEEDED", "SUSPENDED"]

@typing.type_check_only
class EnterpriseCrmEventbusProtoSuspensionAuthPermissions(
    typing_extensions.TypedDict, total=False
):
    gaiaIdentity: EnterpriseCrmEventbusProtoSuspensionAuthPermissionsGaiaIdentity
    googleGroup: EnterpriseCrmEventbusProtoSuspensionAuthPermissionsGaiaIdentity
    loasRole: str
    mdbGroup: str

@typing.type_check_only
class EnterpriseCrmEventbusProtoSuspensionAuthPermissionsGaiaIdentity(
    typing_extensions.TypedDict, total=False
):
    emailAddress: str
    gaiaId: str

@typing.type_check_only
class EnterpriseCrmEventbusProtoSuspensionConfig(
    typing_extensions.TypedDict, total=False
):
    customMessage: str
    notifications: _list[EnterpriseCrmEventbusProtoNotification]
    suspensionExpiration: EnterpriseCrmEventbusProtoSuspensionExpiration
    whoMayResolve: _list[EnterpriseCrmEventbusProtoSuspensionAuthPermissions]

@typing.type_check_only
class EnterpriseCrmEventbusProtoSuspensionExpiration(
    typing_extensions.TypedDict, total=False
):
    expireAfterMs: int
    liftWhenExpired: bool
    remindAfterMs: int

@typing.type_check_only
class EnterpriseCrmEventbusProtoSuspensionResolutionInfo(
    typing_extensions.TypedDict, total=False
):
    audit: EnterpriseCrmEventbusProtoSuspensionResolutionInfoAudit
    createdTimestamp: str
    eventExecutionInfoId: str
    externalTraffic: EnterpriseCrmEventbusProtoExternalTraffic
    lastModifiedTimestamp: str
    product: typing_extensions.Literal[
        "UNSPECIFIED_PRODUCT", "IP", "APIGEE", "SECURITY"
    ]
    status: typing_extensions.Literal["PENDING_UNSPECIFIED", "REJECTED", "LIFTED"]
    suspensionConfig: EnterpriseCrmEventbusProtoSuspensionConfig
    suspensionId: str
    taskNumber: str
    workflowName: str

@typing.type_check_only
class EnterpriseCrmEventbusProtoSuspensionResolutionInfoAudit(
    typing_extensions.TypedDict, total=False
):
    resolvedBy: str
    timestamp: str

@typing.type_check_only
class EnterpriseCrmEventbusProtoTaskAlertConfig(
    typing_extensions.TypedDict, total=False
):
    aggregationPeriod: str
    alertDisabled: bool
    alertName: str
    clientId: str
    durationThresholdMs: str
    errorEnumList: EnterpriseCrmEventbusProtoBaseAlertConfigErrorEnumList
    metricType: typing_extensions.Literal[
        "METRIC_TYPE_UNSPECIFIED",
        "TASK_ERROR_RATE",
        "TASK_WARNING_RATE",
        "TASK_RATE",
        "TASK_AVERAGE_DURATION",
        "TASK_PERCENTILE_DURATION",
    ]
    numAggregationPeriods: int
    onlyFinalAttempt: bool
    playbookUrl: str
    thresholdType: typing_extensions.Literal[
        "UNSPECIFIED_THRESHOLD_TYPE", "EXPECTED_MIN", "EXPECTED_MAX"
    ]
    thresholdValue: EnterpriseCrmEventbusProtoBaseAlertConfigThresholdValue
    warningEnumList: EnterpriseCrmEventbusProtoBaseAlertConfigErrorEnumList

@typing.type_check_only
class EnterpriseCrmEventbusProtoTaskExecutionDetails(
    typing_extensions.TypedDict, total=False
):
    taskAttemptStats: _list[
        EnterpriseCrmEventbusProtoTaskExecutionDetailsTaskAttemptStats
    ]
    taskExecutionState: typing_extensions.Literal[
        "UNSPECIFIED",
        "PENDING_EXECUTION",
        "IN_PROCESS",
        "SUCCEED",
        "FAILED",
        "FATAL",
        "RETRY_ON_HOLD",
        "SKIPPED",
        "CANCELED",
        "PENDING_ROLLBACK",
        "ROLLBACK_IN_PROCESS",
        "ROLLEDBACK",
        "SUSPENDED",
    ]
    taskNumber: str

@typing.type_check_only
class EnterpriseCrmEventbusProtoTaskExecutionDetailsTaskAttemptStats(
    typing_extensions.TypedDict, total=False
):
    endTime: str
    startTime: str

@typing.type_check_only
class EnterpriseCrmEventbusProtoTaskMetadata(typing_extensions.TypedDict, total=False):
    activeTaskName: str
    admins: _list[EnterpriseCrmEventbusProtoTaskMetadataAdmin]
    category: typing_extensions.Literal[
        "UNSPECIFIED_CATEGORY",
        "CUSTOM",
        "FLOW_CONTROL",
        "DATA_MANIPULATION",
        "SCRIPTING",
        "CONNECTOR",
        "HIDDEN",
        "CLOUD_SYSTEMS",
        "CUSTOM_TASK_TEMPLATE",
    ]
    codeSearchLink: str
    defaultJsonValidationOption: typing_extensions.Literal[
        "UNSPECIFIED_JSON_VALIDATION_OPTION",
        "SKIP",
        "PRE_EXECUTION",
        "POST_EXECUTION",
        "PRE_POST_EXECUTION",
    ]
    defaultSpec: str
    description: str
    descriptiveName: str
    docMarkdown: str
    externalCategory: typing_extensions.Literal[
        "UNSPECIFIED_EXTERNAL_CATEGORY", "CORE", "CONNECTORS"
    ]
    externalCategorySequence: int
    externalDocHtml: str
    externalDocLink: str
    externalDocMarkdown: str
    g3DocLink: str
    iconLink: str
    isDeprecated: bool
    name: str
    standaloneExternalDocHtml: str
    status: typing_extensions.Literal[
        "UNSPECIFIED_STATUS", "DEFAULT_INACTIVE", "ACTIVE"
    ]
    system: typing_extensions.Literal[
        "UNSPECIFIED_SYSTEM",
        "GENERIC",
        "BUGANIZER",
        "SALESFORCE",
        "CLOUD_SQL",
        "PLX",
        "SHEETS",
        "GOOGLE_GROUPS",
        "EMAIL",
        "SPANNER",
        "DATA_BRIDGE",
    ]
    tags: _list[str]

@typing.type_check_only
class EnterpriseCrmEventbusProtoTaskMetadataAdmin(
    typing_extensions.TypedDict, total=False
):
    googleGroupEmail: str
    userEmail: str

@typing.type_check_only
class EnterpriseCrmEventbusProtoTaskUiConfig(typing_extensions.TypedDict, total=False):
    taskUiModuleConfigs: _list[EnterpriseCrmEventbusProtoTaskUiModuleConfig]

@typing.type_check_only
class EnterpriseCrmEventbusProtoTaskUiModuleConfig(
    typing_extensions.TypedDict, total=False
):
    moduleId: typing_extensions.Literal[
        "UNSPECIFIED_TASK_MODULE",
        "LABEL",
        "ERROR_HANDLING",
        "TASK_PARAM_TABLE",
        "TASK_PARAM_FORM",
        "PRECONDITION",
        "SCRIPT_EDITOR",
        "RPC",
        "TASK_SUMMARY",
        "SUSPENSION",
        "RPC_TYPED",
        "SUB_WORKFLOW",
        "APPS_SCRIPT_NAVIGATOR",
        "SUB_WORKFLOW_FOR_EACH_LOOP",
        "FIELD_MAPPING",
        "README",
        "REST_CALLER",
        "SUB_WORKFLOW_SCATTER_GATHER",
        "CLOUD_SQL",
        "GENERIC_CONNECTOR_TASK",
    ]

@typing.type_check_only
class EnterpriseCrmEventbusProtoTeardown(typing_extensions.TypedDict, total=False):
    teardownTaskConfigs: _list[EnterpriseCrmEventbusProtoTeardownTaskConfig]

@typing.type_check_only
class EnterpriseCrmEventbusProtoTeardownTaskConfig(
    typing_extensions.TypedDict, total=False
):
    creatorEmail: str
    name: str
    nextTeardownTask: EnterpriseCrmEventbusProtoNextTeardownTask
    parameters: EnterpriseCrmEventbusProtoEventParameters
    properties: EnterpriseCrmEventbusProtoEventBusProperties
    teardownTaskImplementationClassName: str

@typing.type_check_only
class EnterpriseCrmEventbusProtoToken(typing_extensions.TypedDict, total=False):
    name: str
    value: str

@typing.type_check_only
class EnterpriseCrmEventbusProtoTransformExpression(dict[str, typing.Any]): ...

@typing.type_check_only
class EnterpriseCrmEventbusProtoTriggerCriteria(
    typing_extensions.TypedDict, total=False
):
    condition: str
    parameters: EnterpriseCrmEventbusProtoEventParameters
    triggerCriteriaTaskImplementationClassName: str

@typing.type_check_only
class EnterpriseCrmEventbusProtoValueType(typing_extensions.TypedDict, total=False):
    booleanValue: bool
    doubleArray: EnterpriseCrmEventbusProtoDoubleArray
    doubleValue: float
    intArray: EnterpriseCrmEventbusProtoIntArray
    intValue: str
    protoValue: dict[str, typing.Any]
    stringArray: EnterpriseCrmEventbusProtoStringArray
    stringValue: str

@typing.type_check_only
class EnterpriseCrmEventbusProtoWorkflowAlertConfig(
    typing_extensions.TypedDict, total=False
):
    aggregationPeriod: str
    alertDisabled: bool
    alertName: str
    clientId: str
    durationThresholdMs: str
    errorEnumList: EnterpriseCrmEventbusProtoBaseAlertConfigErrorEnumList
    metricType: typing_extensions.Literal[
        "METRIC_TYPE_UNSPECIFIED",
        "EVENT_ERROR_RATE",
        "EVENT_WARNING_RATE",
        "TASK_ERROR_RATE",
        "TASK_WARNING_RATE",
        "TASK_RATE",
        "EVENT_RATE",
        "EVENT_AVERAGE_DURATION",
        "EVENT_PERCENTILE_DURATION",
        "TASK_AVERAGE_DURATION",
        "TASK_PERCENTILE_DURATION",
    ]
    numAggregationPeriods: int
    onlyFinalAttempt: bool
    playbookUrl: str
    thresholdType: typing_extensions.Literal[
        "UNSPECIFIED_THRESHOLD_TYPE", "EXPECTED_MIN", "EXPECTED_MAX"
    ]
    thresholdValue: EnterpriseCrmEventbusProtoBaseAlertConfigThresholdValue
    warningEnumList: EnterpriseCrmEventbusProtoBaseAlertConfigErrorEnumList

@typing.type_check_only
class EnterpriseCrmEventbusStats(typing_extensions.TypedDict, total=False):
    dimensions: EnterpriseCrmEventbusStatsDimensions
    durationInSeconds: float
    errorRate: float
    qps: float
    warningRate: float

@typing.type_check_only
class EnterpriseCrmEventbusStatsDimensions(typing_extensions.TypedDict, total=False):
    clientId: str
    enumFilterType: typing_extensions.Literal["DEFAULT_INCLUSIVE", "EXCLUSIVE"]
    errorEnumString: str
    retryAttempt: typing_extensions.Literal[
        "UNSPECIFIED", "FINAL", "RETRYABLE", "CANCELED"
    ]
    taskName: str
    taskNumber: str
    triggerId: str
    warningEnumString: str
    workflowId: str
    workflowName: str

@typing.type_check_only
class EnterpriseCrmFrontendsEventbusProtoBooleanParameterArray(
    typing_extensions.TypedDict, total=False
):
    booleanValues: _list[bool]

@typing.type_check_only
class EnterpriseCrmFrontendsEventbusProtoDoubleParameterArray(
    typing_extensions.TypedDict, total=False
):
    doubleValues: _list[float]

@typing.type_check_only
class EnterpriseCrmFrontendsEventbusProtoEventExecutionDetails(
    typing_extensions.TypedDict, total=False
):
    eventAttemptStats: _list[
        EnterpriseCrmEventbusProtoEventExecutionDetailsEventAttemptStats
    ]
    eventExecutionSnapshot: _list[
        EnterpriseCrmFrontendsEventbusProtoEventExecutionSnapshot
    ]
    eventExecutionState: typing_extensions.Literal[
        "UNSPECIFIED",
        "ON_HOLD",
        "IN_PROCESS",
        "SUCCEEDED",
        "FAILED",
        "CANCELED",
        "RETRY_ON_HOLD",
        "SUSPENDED",
    ]
    eventRetriesFromBeginningCount: int
    logFilePath: str
    networkAddress: str
    nextExecutionTime: str
    ryeLockUnheldCount: int

@typing.type_check_only
class EnterpriseCrmFrontendsEventbusProtoEventExecutionInfo(
    typing_extensions.TypedDict, total=False
):
    clientId: str
    createTime: str
    errorCode: CrmlogErrorCode
    errors: _list[EnterpriseCrmEventbusProtoErrorDetail]
    eventExecutionDetails: EnterpriseCrmFrontendsEventbusProtoEventExecutionDetails
    eventExecutionInfoId: str
    executionTraceInfo: EnterpriseCrmEventbusProtoExecutionTraceInfo
    lastModifiedTime: str
    postMethod: typing_extensions.Literal[
        "UNSPECIFIED",
        "POST",
        "POST_TO_QUEUE",
        "SCHEDULE",
        "POST_BY_EVENT_CONFIG_ID",
        "POST_WITH_EVENT_DETAILS",
    ]
    product: typing_extensions.Literal[
        "UNSPECIFIED_PRODUCT", "IP", "APIGEE", "SECURITY"
    ]
    requestId: str
    requestParams: EnterpriseCrmFrontendsEventbusProtoEventParameters
    responseParams: EnterpriseCrmFrontendsEventbusProtoEventParameters
    snapshotNumber: str
    tenant: str
    triggerId: str
    workflowId: str
    workflowName: str
    workflowRetryBackoffIntervalSeconds: str

@typing.type_check_only
class EnterpriseCrmFrontendsEventbusProtoEventExecutionSnapshot(
    typing_extensions.TypedDict, total=False
):
    checkpointTaskNumber: str
    conditionResults: _list[EnterpriseCrmEventbusProtoConditionResult]
    diffParams: EnterpriseCrmFrontendsEventbusProtoEventParameters
    eventExecutionInfoId: str
    eventExecutionSnapshotId: str
    eventExecutionSnapshotMetadata: EnterpriseCrmEventbusProtoEventExecutionSnapshotEventExecutionSnapshotMetadata
    eventParams: EnterpriseCrmFrontendsEventbusProtoEventParameters
    snapshotTime: str
    taskExecutionDetails: _list[EnterpriseCrmEventbusProtoTaskExecutionDetails]
    taskName: str

@typing.type_check_only
class EnterpriseCrmFrontendsEventbusProtoEventParameters(
    typing_extensions.TypedDict, total=False
):
    parameters: _list[EnterpriseCrmFrontendsEventbusProtoParameterEntry]

@typing.type_check_only
class EnterpriseCrmFrontendsEventbusProtoIntParameterArray(
    typing_extensions.TypedDict, total=False
):
    intValues: _list[str]

@typing.type_check_only
class EnterpriseCrmFrontendsEventbusProtoParamSpecEntry(
    typing_extensions.TypedDict, total=False
):
    className: str
    collectionElementClassName: str
    config: EnterpriseCrmEventbusProtoParamSpecEntryConfig
    dataType: typing_extensions.Literal[
        "DATA_TYPE_UNSPECIFIED",
        "STRING_VALUE",
        "INT_VALUE",
        "DOUBLE_VALUE",
        "BOOLEAN_VALUE",
        "PROTO_VALUE",
        "SERIALIZED_OBJECT_VALUE",
        "STRING_ARRAY",
        "INT_ARRAY",
        "DOUBLE_ARRAY",
        "PROTO_ARRAY",
        "PROTO_ENUM",
        "BOOLEAN_ARRAY",
        "PROTO_ENUM_ARRAY",
        "BYTES",
        "BYTES_ARRAY",
        "NON_SERIALIZABLE_OBJECT",
        "JSON_VALUE",
    ]
    defaultValue: EnterpriseCrmFrontendsEventbusProtoParameterValueType
    isDeprecated: bool
    isOutput: bool
    jsonSchema: str
    key: str
    protoDef: EnterpriseCrmEventbusProtoParamSpecEntryProtoDefinition
    required: bool
    validationRule: EnterpriseCrmEventbusProtoParamSpecEntryValidationRule

@typing.type_check_only
class EnterpriseCrmFrontendsEventbusProtoParamSpecsMessage(
    typing_extensions.TypedDict, total=False
):
    parameters: _list[EnterpriseCrmFrontendsEventbusProtoParamSpecEntry]

@typing.type_check_only
class EnterpriseCrmFrontendsEventbusProtoParameterEntry(
    typing_extensions.TypedDict, total=False
):
    dataType: typing_extensions.Literal[
        "DATA_TYPE_UNSPECIFIED",
        "STRING_VALUE",
        "INT_VALUE",
        "DOUBLE_VALUE",
        "BOOLEAN_VALUE",
        "PROTO_VALUE",
        "SERIALIZED_OBJECT_VALUE",
        "STRING_ARRAY",
        "INT_ARRAY",
        "DOUBLE_ARRAY",
        "PROTO_ARRAY",
        "PROTO_ENUM",
        "BOOLEAN_ARRAY",
        "PROTO_ENUM_ARRAY",
        "BYTES",
        "BYTES_ARRAY",
        "NON_SERIALIZABLE_OBJECT",
        "JSON_VALUE",
    ]
    key: str
    value: EnterpriseCrmFrontendsEventbusProtoParameterValueType

@typing.type_check_only
class EnterpriseCrmFrontendsEventbusProtoParameterMap(
    typing_extensions.TypedDict, total=False
):
    entries: _list[EnterpriseCrmFrontendsEventbusProtoParameterMapEntry]
    keyType: typing_extensions.Literal[
        "DATA_TYPE_UNSPECIFIED",
        "STRING_VALUE",
        "INT_VALUE",
        "DOUBLE_VALUE",
        "BOOLEAN_VALUE",
        "PROTO_VALUE",
        "SERIALIZED_OBJECT_VALUE",
        "STRING_ARRAY",
        "INT_ARRAY",
        "DOUBLE_ARRAY",
        "PROTO_ARRAY",
        "PROTO_ENUM",
        "BOOLEAN_ARRAY",
        "PROTO_ENUM_ARRAY",
        "BYTES",
        "BYTES_ARRAY",
        "NON_SERIALIZABLE_OBJECT",
        "JSON_VALUE",
    ]
    valueType: typing_extensions.Literal[
        "DATA_TYPE_UNSPECIFIED",
        "STRING_VALUE",
        "INT_VALUE",
        "DOUBLE_VALUE",
        "BOOLEAN_VALUE",
        "PROTO_VALUE",
        "SERIALIZED_OBJECT_VALUE",
        "STRING_ARRAY",
        "INT_ARRAY",
        "DOUBLE_ARRAY",
        "PROTO_ARRAY",
        "PROTO_ENUM",
        "BOOLEAN_ARRAY",
        "PROTO_ENUM_ARRAY",
        "BYTES",
        "BYTES_ARRAY",
        "NON_SERIALIZABLE_OBJECT",
        "JSON_VALUE",
    ]

@typing.type_check_only
class EnterpriseCrmFrontendsEventbusProtoParameterMapEntry(
    typing_extensions.TypedDict, total=False
):
    key: EnterpriseCrmFrontendsEventbusProtoParameterMapField
    value: EnterpriseCrmFrontendsEventbusProtoParameterMapField

@typing.type_check_only
class EnterpriseCrmFrontendsEventbusProtoParameterMapField(
    typing_extensions.TypedDict, total=False
):
    literalValue: EnterpriseCrmFrontendsEventbusProtoParameterValueType
    referenceKey: str

@typing.type_check_only
class EnterpriseCrmFrontendsEventbusProtoParameterValueType(
    typing_extensions.TypedDict, total=False
):
    booleanArray: EnterpriseCrmFrontendsEventbusProtoBooleanParameterArray
    booleanValue: bool
    doubleArray: EnterpriseCrmFrontendsEventbusProtoDoubleParameterArray
    doubleValue: float
    intArray: EnterpriseCrmFrontendsEventbusProtoIntParameterArray
    intValue: str
    jsonValue: str
    protoArray: EnterpriseCrmFrontendsEventbusProtoProtoParameterArray
    protoValue: dict[str, typing.Any]
    serializedObjectValue: EnterpriseCrmFrontendsEventbusProtoSerializedObjectParameter
    stringArray: EnterpriseCrmFrontendsEventbusProtoStringParameterArray
    stringValue: str

@typing.type_check_only
class EnterpriseCrmFrontendsEventbusProtoProtoParameterArray(
    typing_extensions.TypedDict, total=False
):
    protoValues: _list[dict[str, typing.Any]]

@typing.type_check_only
class EnterpriseCrmFrontendsEventbusProtoRollbackStrategy(
    typing_extensions.TypedDict, total=False
):
    parameters: EnterpriseCrmFrontendsEventbusProtoEventParameters
    rollbackTaskImplementationClassName: str
    taskNumbersToRollback: _list[str]

@typing.type_check_only
class EnterpriseCrmFrontendsEventbusProtoSerializedObjectParameter(
    typing_extensions.TypedDict, total=False
):
    objectValue: str

@typing.type_check_only
class EnterpriseCrmFrontendsEventbusProtoStringParameterArray(
    typing_extensions.TypedDict, total=False
):
    stringValues: _list[str]

@typing.type_check_only
class EnterpriseCrmFrontendsEventbusProtoTaskConfig(
    typing_extensions.TypedDict, total=False
):
    alertConfigs: _list[EnterpriseCrmEventbusProtoTaskAlertConfig]
    createTime: str
    creatorEmail: str
    description: str
    disableStrictTypeValidation: bool
    failurePolicy: EnterpriseCrmEventbusProtoFailurePolicy
    incomingEdgeCount: int
    jsonValidationOption: typing_extensions.Literal[
        "UNSPECIFIED_JSON_VALIDATION_OPTION",
        "SKIP",
        "PRE_EXECUTION",
        "POST_EXECUTION",
        "PRE_POST_EXECUTION",
    ]
    label: str
    lastModifiedTime: str
    nextTasks: _list[EnterpriseCrmEventbusProtoNextTask]
    nextTasksExecutionPolicy: typing_extensions.Literal[
        "UNSPECIFIED", "RUN_ALL_MATCH", "RUN_FIRST_MATCH"
    ]
    parameters: dict[str, typing.Any]
    position: EnterpriseCrmEventbusProtoCoordinate
    precondition: str
    preconditionLabel: str
    rollbackStrategy: EnterpriseCrmFrontendsEventbusProtoRollbackStrategy
    successPolicy: EnterpriseCrmEventbusProtoSuccessPolicy
    synchronousCallFailurePolicy: EnterpriseCrmEventbusProtoFailurePolicy
    taskEntity: EnterpriseCrmFrontendsEventbusProtoTaskEntity
    taskExecutionStrategy: typing_extensions.Literal[
        "WHEN_ALL_SUCCEED", "WHEN_ANY_SUCCEED", "WHEN_ALL_TASKS_AND_CONDITIONS_SUCCEED"
    ]
    taskName: str
    taskNumber: str
    taskSpec: str
    taskTemplateName: str
    taskType: typing_extensions.Literal["TASK", "ASIS_TEMPLATE", "IO_TEMPLATE"]

@typing.type_check_only
class EnterpriseCrmFrontendsEventbusProtoTaskEntity(
    typing_extensions.TypedDict, total=False
):
    disabledForVpcSc: bool
    metadata: EnterpriseCrmEventbusProtoTaskMetadata
    paramSpecs: EnterpriseCrmFrontendsEventbusProtoParamSpecsMessage
    stats: EnterpriseCrmEventbusStats
    taskType: typing_extensions.Literal["TASK", "ASIS_TEMPLATE", "IO_TEMPLATE"]
    uiConfig: EnterpriseCrmEventbusProtoTaskUiConfig

@typing.type_check_only
class EnterpriseCrmFrontendsEventbusProtoTriggerConfig(
    typing_extensions.TypedDict, total=False
):
    alertConfig: _list[EnterpriseCrmEventbusProtoWorkflowAlertConfig]
    description: str
    enabledClients: _list[str]
    label: str
    nextTasksExecutionPolicy: typing_extensions.Literal[
        "UNSPECIFIED", "RUN_ALL_MATCH", "RUN_FIRST_MATCH"
    ]
    pauseWorkflowExecutions: bool
    position: EnterpriseCrmEventbusProtoCoordinate
    properties: dict[str, typing.Any]
    startTasks: _list[EnterpriseCrmEventbusProtoNextTask]
    triggerCriteria: EnterpriseCrmEventbusProtoTriggerCriteria
    triggerId: str
    triggerNumber: str
    triggerType: typing_extensions.Literal[
        "UNKNOWN",
        "CLOUD_PUBSUB",
        "GOOPS",
        "SFDC_SYNC",
        "CRON",
        "API",
        "MANIFOLD_TRIGGER",
        "DATALAYER_DATA_CHANGE",
        "SFDC_CHANNEL",
        "CLOUD_PUBSUB_EXTERNAL",
        "SFDC_CDC_CHANNEL",
        "SFDC_PLATFORM_EVENTS_CHANNEL",
    ]

@typing.type_check_only
class EnterpriseCrmFrontendsEventbusProtoWorkflowParameterEntry(
    dict[str, typing.Any]
): ...

@typing.type_check_only
class EnterpriseCrmFrontendsEventbusProtoWorkflowParameters(
    typing_extensions.TypedDict, total=False
):
    parameters: _list[EnterpriseCrmFrontendsEventbusProtoWorkflowParameterEntry]

@typing.type_check_only
class EnterpriseCrmLoggingGwsFieldLimits(typing_extensions.TypedDict, total=False):
    logAction: typing_extensions.Literal["LOG_ACTION_UNSPECIFIED", "DONT_LOG", "LOG"]
    logType: _list[str]
    maxArraySize: int
    maxStringLength: int
    shortenerType: typing_extensions.Literal[
        "SHORTENER_TYPE_UNSPECIFIED",
        "SHORTEN",
        "HASH",
        "SHORTEN_WITH_HASH",
        "SHORTEN_EMAIL",
        "SHORTEN_EMAIL_WITH_HASH",
        "SHORTEN_DOMAIN",
    ]

@typing.type_check_only
class EnterpriseCrmLoggingGwsSanitizeOptions(typing_extensions.TypedDict, total=False):
    isAlreadySanitized: bool
    logType: _list[str]
    privacy: typing_extensions.Literal[
        "PRIVACY_TYPE_UNSPECIFIED", "NOT_PII", "PII", "SPII", "UNSURE"
    ]
    sanitizeType: typing_extensions.Literal[
        "SANITIZE_TYPE_UNSPECIFIED",
        "SCRUB",
        "ANONYMIZE",
        "ANONYMIZE_LIMITED_REPEATABLE",
        "OBFUSCATE",
        "ENCRYPT",
        "DO_NOT_SANITIZE",
    ]

@typing.type_check_only
class GoogleCloudConnectorsV1AuthConfig(typing_extensions.TypedDict, total=False):
    additionalVariables: _list[GoogleCloudConnectorsV1ConfigVariable]
    authType: typing_extensions.Literal[
        "AUTH_TYPE_UNSPECIFIED",
        "USER_PASSWORD",
        "OAUTH2_JWT_BEARER",
        "OAUTH2_CLIENT_CREDENTIALS",
        "SSH_PUBLIC_KEY",
        "OAUTH2_AUTH_CODE_FLOW",
    ]
    oauth2ClientCredentials: GoogleCloudConnectorsV1AuthConfigOauth2ClientCredentials
    oauth2JwtBearer: GoogleCloudConnectorsV1AuthConfigOauth2JwtBearer
    sshPublicKey: GoogleCloudConnectorsV1AuthConfigSshPublicKey
    userPassword: GoogleCloudConnectorsV1AuthConfigUserPassword

@typing.type_check_only
class GoogleCloudConnectorsV1AuthConfigOauth2ClientCredentials(
    typing_extensions.TypedDict, total=False
):
    clientId: str
    clientSecret: GoogleCloudConnectorsV1Secret

@typing.type_check_only
class GoogleCloudConnectorsV1AuthConfigOauth2JwtBearer(
    typing_extensions.TypedDict, total=False
):
    clientKey: GoogleCloudConnectorsV1Secret
    jwtClaims: GoogleCloudConnectorsV1AuthConfigOauth2JwtBearerJwtClaims

@typing.type_check_only
class GoogleCloudConnectorsV1AuthConfigOauth2JwtBearerJwtClaims(
    typing_extensions.TypedDict, total=False
):
    audience: str
    issuer: str
    subject: str

@typing.type_check_only
class GoogleCloudConnectorsV1AuthConfigSshPublicKey(
    typing_extensions.TypedDict, total=False
):
    certType: str
    password: GoogleCloudConnectorsV1Secret
    sshClientCert: GoogleCloudConnectorsV1Secret
    sshClientCertPass: GoogleCloudConnectorsV1Secret
    username: str

@typing.type_check_only
class GoogleCloudConnectorsV1AuthConfigUserPassword(
    typing_extensions.TypedDict, total=False
):
    password: GoogleCloudConnectorsV1Secret
    username: str

@typing.type_check_only
class GoogleCloudConnectorsV1ConfigVariable(typing_extensions.TypedDict, total=False):
    boolValue: bool
    intValue: str
    key: str
    secretValue: GoogleCloudConnectorsV1Secret
    stringValue: str

@typing.type_check_only
class GoogleCloudConnectorsV1Connection(typing_extensions.TypedDict, total=False):
    authConfig: GoogleCloudConnectorsV1AuthConfig
    configVariables: _list[GoogleCloudConnectorsV1ConfigVariable]
    connectorVersion: str
    createTime: str
    description: str
    destinationConfigs: _list[GoogleCloudConnectorsV1DestinationConfig]
    envoyImageLocation: str
    imageLocation: str
    labels: dict[str, typing.Any]
    lockConfig: GoogleCloudConnectorsV1LockConfig
    name: str
    nodeConfig: GoogleCloudConnectorsV1NodeConfig
    serviceAccount: str
    serviceDirectory: str
    status: GoogleCloudConnectorsV1ConnectionStatus
    suspended: bool
    updateTime: str

@typing.type_check_only
class GoogleCloudConnectorsV1ConnectionStatus(typing_extensions.TypedDict, total=False):
    description: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "CREATING",
        "ACTIVE",
        "INACTIVE",
        "DELETING",
        "UPDATING",
        "ERROR",
    ]
    status: str

@typing.type_check_only
class GoogleCloudConnectorsV1Destination(typing_extensions.TypedDict, total=False):
    host: str
    port: int
    serviceAttachment: str

@typing.type_check_only
class GoogleCloudConnectorsV1DestinationConfig(
    typing_extensions.TypedDict, total=False
):
    destinations: _list[GoogleCloudConnectorsV1Destination]
    key: str

@typing.type_check_only
class GoogleCloudConnectorsV1LockConfig(typing_extensions.TypedDict, total=False):
    locked: bool
    reason: str

@typing.type_check_only
class GoogleCloudConnectorsV1NodeConfig(typing_extensions.TypedDict, total=False):
    maxNodeCount: int
    minNodeCount: int

@typing.type_check_only
class GoogleCloudConnectorsV1Secret(typing_extensions.TypedDict, total=False):
    secretVersion: str

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaAccessToken(
    typing_extensions.TypedDict, total=False
):
    accessToken: str
    accessTokenExpireTime: str
    refreshToken: str
    refreshTokenExpireTime: str
    tokenType: str

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaArchiveBundleRequest(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaArchiveBundleResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaArchiveIntegrationVersionRequest(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaArchiveIntegrationVersionResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaAttemptStats(
    typing_extensions.TypedDict, total=False
):
    endTime: str
    startTime: str

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaAuthConfig(
    typing_extensions.TypedDict, total=False
):
    certificateId: str
    createTime: str
    creatorEmail: str
    credentialType: typing_extensions.Literal[
        "CREDENTIAL_TYPE_UNSPECIFIED",
        "USERNAME_AND_PASSWORD",
        "API_KEY",
        "OAUTH2_AUTHORIZATION_CODE",
        "OAUTH2_IMPLICIT",
        "OAUTH2_CLIENT_CREDENTIALS",
        "OAUTH2_RESOURCE_OWNER_CREDENTIALS",
        "JWT",
        "AUTH_TOKEN",
        "SERVICE_ACCOUNT",
        "CLIENT_CERTIFICATE_ONLY",
        "OIDC_TOKEN",
    ]
    decryptedCredential: GoogleCloudIntegrationsV1alphaCredential
    description: str
    displayName: str
    encryptedCredential: str
    expiryNotificationDuration: _list[str]
    lastModifierEmail: str
    name: str
    overrideValidTime: str
    reason: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "VALID",
        "INVALID",
        "SOFT_DELETED",
        "EXPIRED",
        "UNAUTHORIZED",
        "UNSUPPORTED",
    ]
    updateTime: str
    validTime: str
    visibility: typing_extensions.Literal[
        "AUTH_CONFIG_VISIBILITY_UNSPECIFIED", "PRIVATE", "CLIENT_VISIBLE"
    ]

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaAuthToken(typing_extensions.TypedDict, total=False):
    token: str
    type: str

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaBooleanParameterArray(
    typing_extensions.TypedDict, total=False
):
    booleanValues: _list[bool]

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaCancelExecutionRequest(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaCancelExecutionResponse(
    typing_extensions.TypedDict, total=False
):
    isCanceled: bool

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaCertificate(
    typing_extensions.TypedDict, total=False
):
    certificateStatus: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "ACTIVE", "EXPIRED"
    ]
    credentialId: str
    description: str
    displayName: str
    name: str
    rawCertificate: GoogleCloudIntegrationsV1alphaClientCertificate
    requestorId: str
    validEndTime: str
    validStartTime: str

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaClientCertificate(
    typing_extensions.TypedDict, total=False
):
    encryptedPrivateKey: str
    passphrase: str
    sslCertificate: str

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaConnectionSchemaMetadata(
    typing_extensions.TypedDict, total=False
):
    actions: _list[str]
    entities: _list[str]

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaCreateAppsScriptProjectRequest(
    typing_extensions.TypedDict, total=False
):
    appsScriptProject: str
    authConfigId: str

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaCreateAppsScriptProjectResponse(
    typing_extensions.TypedDict, total=False
):
    projectId: str

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaCreateBundleRequest(
    typing_extensions.TypedDict, total=False
):
    bundleId: str
    integrations: _list[str]
    secondaryCustomerOrgId: str

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaCreateBundleResponse(
    typing_extensions.TypedDict, total=False
):
    config: GoogleCloudIntegrationsV1alphaIntegrationBundleConfig
    triggerId: str

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaCredential(
    typing_extensions.TypedDict, total=False
):
    authToken: GoogleCloudIntegrationsV1alphaAuthToken
    credentialType: typing_extensions.Literal[
        "CREDENTIAL_TYPE_UNSPECIFIED",
        "USERNAME_AND_PASSWORD",
        "API_KEY",
        "OAUTH2_AUTHORIZATION_CODE",
        "OAUTH2_IMPLICIT",
        "OAUTH2_CLIENT_CREDENTIALS",
        "OAUTH2_RESOURCE_OWNER_CREDENTIALS",
        "JWT",
        "AUTH_TOKEN",
        "SERVICE_ACCOUNT",
        "CLIENT_CERTIFICATE_ONLY",
        "OIDC_TOKEN",
    ]
    jwt: GoogleCloudIntegrationsV1alphaJwt
    oauth2AuthorizationCode: GoogleCloudIntegrationsV1alphaOAuth2AuthorizationCode
    oauth2ClientCredentials: GoogleCloudIntegrationsV1alphaOAuth2ClientCredentials
    oauth2ResourceOwnerCredentials: GoogleCloudIntegrationsV1alphaOAuth2ResourceOwnerCredentials
    oidcToken: GoogleCloudIntegrationsV1alphaOidcToken
    serviceAccountCredentials: GoogleCloudIntegrationsV1alphaServiceAccountCredentials
    usernameAndPassword: GoogleCloudIntegrationsV1alphaUsernameAndPassword

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaDeactivateIntegrationVersionRequest(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaDeactivateIntegrationVersionResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaDoubleParameterArray(
    typing_extensions.TypedDict, total=False
):
    doubleValues: _list[float]

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaDownloadIntegrationVersionResponse(
    typing_extensions.TypedDict, total=False
):
    content: str

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaEnumerateConnectorPlatformRegionsResponse(
    typing_extensions.TypedDict, total=False
):
    regions: _list[str]

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaEventParameter(
    typing_extensions.TypedDict, total=False
):
    key: str
    value: GoogleCloudIntegrationsV1alphaValueType

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaExecuteIntegrationsRequest(
    typing_extensions.TypedDict, total=False
):
    doNotPropagateError: bool
    executionId: str
    inputParameters: dict[str, typing.Any]
    parameterEntries: _list[EnterpriseCrmFrontendsEventbusProtoParameterEntry]
    parameters: EnterpriseCrmFrontendsEventbusProtoEventParameters
    requestId: str
    triggerId: str

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaExecuteIntegrationsResponse(
    typing_extensions.TypedDict, total=False
):
    eventParameters: EnterpriseCrmFrontendsEventbusProtoEventParameters
    executionFailed: bool
    executionId: str
    outputParameters: dict[str, typing.Any]
    parameterEntries: _list[EnterpriseCrmFrontendsEventbusProtoParameterEntry]

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaExecution(dict[str, typing.Any]): ...

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaExecutionDetails(
    typing_extensions.TypedDict, total=False
):
    attemptStats: _list[GoogleCloudIntegrationsV1alphaAttemptStats]
    executionSnapshots: _list[GoogleCloudIntegrationsV1alphaExecutionSnapshot]
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "PENDING",
        "PROCESSING",
        "SUCCEEDED",
        "FAILED",
        "CANCELLED",
        "RETRY_ON_HOLD",
        "SUSPENDED",
    ]

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaExecutionSnapshot(
    typing_extensions.TypedDict, total=False
):
    checkpointTaskNumber: str
    executionSnapshotMetadata: GoogleCloudIntegrationsV1alphaExecutionSnapshotExecutionSnapshotMetadata
    params: dict[str, typing.Any]
    taskExecutionDetails: _list[GoogleCloudIntegrationsV1alphaTaskExecutionDetails]

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaExecutionSnapshotExecutionSnapshotMetadata(
    typing_extensions.TypedDict, total=False
):
    executionAttempt: int
    task: str
    taskAttempt: int
    taskNumber: str

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaFailurePolicy(
    typing_extensions.TypedDict, total=False
):
    intervalTime: str
    maxRetries: int
    retryStrategy: typing_extensions.Literal[
        "RETRY_STRATEGY_UNSPECIFIED",
        "IGNORE",
        "NONE",
        "FATAL",
        "FIXED_INTERVAL",
        "LINEAR_BACKOFF",
        "EXPONENTIAL_BACKOFF",
        "RESTART_INTEGRATION_WITH_BACKOFF",
    ]

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaGenerateTokenResponse(
    typing_extensions.TypedDict, total=False
):
    message: str

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaGetBundleResponse(
    typing_extensions.TypedDict, total=False
):
    config: GoogleCloudIntegrationsV1alphaIntegrationBundleConfig

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaIntParameterArray(
    typing_extensions.TypedDict, total=False
):
    intValues: _list[str]

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaIntegration(
    typing_extensions.TypedDict, total=False
):
    active: bool
    description: str
    name: str
    updateTime: str

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaIntegrationAlertConfig(
    typing_extensions.TypedDict, total=False
):
    aggregationPeriod: str
    alertThreshold: int
    disableAlert: bool
    displayName: str
    durationThreshold: str
    metricType: typing_extensions.Literal[
        "METRIC_TYPE_UNSPECIFIED",
        "EVENT_ERROR_RATE",
        "EVENT_WARNING_RATE",
        "TASK_ERROR_RATE",
        "TASK_WARNING_RATE",
        "TASK_RATE",
        "EVENT_RATE",
        "EVENT_AVERAGE_DURATION",
        "EVENT_PERCENTILE_DURATION",
        "TASK_AVERAGE_DURATION",
        "TASK_PERCENTILE_DURATION",
    ]
    onlyFinalAttempt: bool
    thresholdType: typing_extensions.Literal[
        "THRESHOLD_TYPE_UNSPECIFIED", "EXPECTED_MIN", "EXPECTED_MAX"
    ]
    thresholdValue: GoogleCloudIntegrationsV1alphaIntegrationAlertConfigThresholdValue

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaIntegrationAlertConfigThresholdValue(
    typing_extensions.TypedDict, total=False
):
    absolute: str
    percentage: int

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaIntegrationBundleConfig(
    typing_extensions.TypedDict, total=False
):
    integrations: _list[str]
    serviceAccount: str

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaIntegrationParameter(
    typing_extensions.TypedDict, total=False
):
    dataType: typing_extensions.Literal[
        "INTEGRATION_PARAMETER_DATA_TYPE_UNSPECIFIED",
        "STRING_VALUE",
        "INT_VALUE",
        "DOUBLE_VALUE",
        "BOOLEAN_VALUE",
        "STRING_ARRAY",
        "INT_ARRAY",
        "DOUBLE_ARRAY",
        "BOOLEAN_ARRAY",
        "JSON_VALUE",
        "PROTO_VALUE",
        "PROTO_ARRAY",
    ]
    defaultValue: GoogleCloudIntegrationsV1alphaValueType
    displayName: str
    inputOutputType: typing_extensions.Literal[
        "IN_OUT_TYPE_UNSPECIFIED", "IN", "OUT", "IN_OUT"
    ]
    isTransient: bool
    jsonSchema: str
    key: str
    producer: str
    searchable: bool

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaIntegrationTemplateVersion(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    databasePersistencePolicy: typing_extensions.Literal[
        "DATABASE_PERSISTENCE_POLICY_UNSPECIFIED", "DATABASE_PERSISTENCE_DISABLED"
    ]
    description: str
    lastModifierEmail: str
    name: str
    parentIntegrationVersionId: str
    snapshotNumber: str
    status: typing_extensions.Literal[
        "UNKNOWN", "DRAFT", "ACTIVE", "ARCHIVED", "SNAPSHOT"
    ]
    taskConfigs: _list[EnterpriseCrmFrontendsEventbusProtoTaskConfig]
    teardown: EnterpriseCrmEventbusProtoTeardown
    templateParameters: EnterpriseCrmFrontendsEventbusProtoWorkflowParameters
    triggerConfigs: _list[EnterpriseCrmFrontendsEventbusProtoTriggerConfig]
    updateTime: str
    userLabel: str

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaIntegrationVersion(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    databasePersistencePolicy: typing_extensions.Literal[
        "DATABASE_PERSISTENCE_POLICY_UNSPECIFIED", "DATABASE_PERSISTENCE_DISABLED"
    ]
    description: str
    integrationParameters: _list[GoogleCloudIntegrationsV1alphaIntegrationParameter]
    integrationParametersInternal: EnterpriseCrmFrontendsEventbusProtoWorkflowParameters
    lastModifierEmail: str
    lockHolder: str
    name: str
    origin: typing_extensions.Literal[
        "UNSPECIFIED", "UI", "PIPER_V2", "PIPER_V3", "APPLICATION_IP_PROVISIONING"
    ]
    parentTemplateId: str
    snapshotNumber: str
    state: typing_extensions.Literal[
        "INTEGRATION_STATE_UNSPECIFIED", "DRAFT", "ACTIVE", "ARCHIVED", "SNAPSHOT"
    ]
    status: typing_extensions.Literal[
        "UNKNOWN", "DRAFT", "ACTIVE", "ARCHIVED", "SNAPSHOT"
    ]
    taskConfigs: _list[GoogleCloudIntegrationsV1alphaTaskConfig]
    taskConfigsInternal: _list[EnterpriseCrmFrontendsEventbusProtoTaskConfig]
    teardown: EnterpriseCrmEventbusProtoTeardown
    triggerConfigs: _list[GoogleCloudIntegrationsV1alphaTriggerConfig]
    triggerConfigsInternal: _list[EnterpriseCrmFrontendsEventbusProtoTriggerConfig]
    updateTime: str
    userLabel: str

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaJwt(typing_extensions.TypedDict, total=False):
    jwt: str
    jwtHeader: str
    jwtPayload: str
    secret: str

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaLiftSuspensionRequest(
    typing_extensions.TypedDict, total=False
):
    suspensionResult: str

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaLiftSuspensionResponse(
    typing_extensions.TypedDict, total=False
):
    eventExecutionInfoId: str

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaLinkAppsScriptProjectRequest(
    typing_extensions.TypedDict, total=False
):
    scriptId: str

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaLinkAppsScriptProjectResponse(
    typing_extensions.TypedDict, total=False
):
    scriptId: str

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaListAuthConfigsResponse(
    typing_extensions.TypedDict, total=False
):
    authConfigs: _list[GoogleCloudIntegrationsV1alphaAuthConfig]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaListCertificatesResponse(
    typing_extensions.TypedDict, total=False
):
    certificates: _list[GoogleCloudIntegrationsV1alphaCertificate]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaListConnectionsResponse(
    typing_extensions.TypedDict, total=False
):
    connections: _list[GoogleCloudConnectorsV1Connection]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaListExecutionSnapshotsResponse(
    typing_extensions.TypedDict, total=False
):
    executionSnapshots: _list[EnterpriseCrmEventbusProtoEventExecutionSnapshot]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaListExecutionsResponse(
    typing_extensions.TypedDict, total=False
):
    executionInfos: _list[EnterpriseCrmFrontendsEventbusProtoEventExecutionInfo]
    executions: _list[GoogleCloudIntegrationsV1alphaExecution]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaListIntegrationTemplateVersionsResponse(
    typing_extensions.TypedDict, total=False
):
    integrationTemplateVersions: _list[
        GoogleCloudIntegrationsV1alphaIntegrationTemplateVersion
    ]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaListIntegrationVersionsResponse(
    typing_extensions.TypedDict, total=False
):
    integrationVersions: _list[GoogleCloudIntegrationsV1alphaIntegrationVersion]
    nextPageToken: str
    noPermission: bool

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaListIntegrationsResponse(
    typing_extensions.TypedDict, total=False
):
    integrations: _list[GoogleCloudIntegrationsV1alphaIntegration]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaListRuntimeActionSchemasResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    runtimeActionSchemas: _list[GoogleCloudIntegrationsV1alphaRuntimeActionSchema]

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaListRuntimeEntitySchemasResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    runtimeEntitySchemas: _list[GoogleCloudIntegrationsV1alphaRuntimeEntitySchema]

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaListSfdcChannelsResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    sfdcChannels: _list[GoogleCloudIntegrationsV1alphaSfdcChannel]

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaListSfdcInstancesResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    sfdcInstances: _list[GoogleCloudIntegrationsV1alphaSfdcInstance]

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaListSuspensionsResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    suspensions: _list[GoogleCloudIntegrationsV1alphaSuspension]

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaListTaskEntitiesResponse(
    typing_extensions.TypedDict, total=False
):
    taskEntities: _list[EnterpriseCrmFrontendsEventbusProtoTaskEntity]

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaMonitorExecutionStatsRequest(
    typing_extensions.TypedDict, total=False
):
    duration: str
    endTime: str
    mashQuery: GoogleCloudIntegrationsV1alphaMonitorExecutionStatsRequestMashQuery
    metricFieldTable: bool
    outputPeriod: str
    responseTemplate: typing_extensions.Literal[
        "DATA_FORMAT_UNSPECIFIED", "TABLE_CONFIG", "APLOSE_SERIES_LIST_CONFIG"
    ]

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaMonitorExecutionStatsRequestGroupBy(
    typing_extensions.TypedDict, total=False
):
    fields: _list[str]
    reducer: str

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaMonitorExecutionStatsRequestMashQuery(
    typing_extensions.TypedDict, total=False
):
    firstQuery: GoogleCloudIntegrationsV1alphaMonitorExecutionStatsRequestMashQueryComponent
    operationMode: GoogleCloudIntegrationsV1alphaMonitorExecutionStatsRequestMashQueryOperationMode
    secondQuery: GoogleCloudIntegrationsV1alphaMonitorExecutionStatsRequestMashQueryComponent

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaMonitorExecutionStatsRequestMashQueryComponent(
    typing_extensions.TypedDict, total=False
):
    borgTaskMetric: typing_extensions.Literal[
        "BORG_TASK_METRIC_UNSPECIFIED",
        "TASK_INDIVIDUAL_COUNT",
        "EVENT_COUNT",
        "EVENT_DURATION",
        "TASK_INDIVIDUAL_DURATION",
    ]
    dataFilters: _list[str]
    fetchFilters: _list[str]
    groupBy: GoogleCloudIntegrationsV1alphaMonitorExecutionStatsRequestGroupBy
    pointOperation: str
    timeDelta: str

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaMonitorExecutionStatsRequestMashQueryOperationMode(
    typing_extensions.TypedDict, total=False
):
    joinConfig: GoogleCloudIntegrationsV1alphaMonitorExecutionStatsRequestMashQueryOperationModeJoinConfig
    operationType: typing_extensions.Literal[
        "OPERATION_TYPE_UNSPECIFIED", "UNION", "JOIN"
    ]
    unionConfig: GoogleCloudIntegrationsV1alphaMonitorExecutionStatsRequestMashQueryOperationModeUnionConfig

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaMonitorExecutionStatsRequestMashQueryOperationModeJoinConfig(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaMonitorExecutionStatsRequestMashQueryOperationModeUnionConfig(
    typing_extensions.TypedDict, total=False
):
    reducer: str

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaMonitorExecutionStatsResponse(
    typing_extensions.TypedDict, total=False
):
    aplosSeriesListData: EnterpriseCrmCardsTemplatesAplosSeriesListData
    tableData: EnterpriseCrmCardsTabularData

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaNextTask(typing_extensions.TypedDict, total=False):
    condition: str
    description: str
    displayName: str
    taskConfigId: str
    taskId: str

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaOAuth2AuthorizationCode(
    typing_extensions.TypedDict, total=False
):
    accessToken: GoogleCloudIntegrationsV1alphaAccessToken
    applyReauthPolicy: bool
    authCode: str
    authEndpoint: str
    authParams: GoogleCloudIntegrationsV1alphaParameterMap
    clientId: str
    clientSecret: str
    requestType: typing_extensions.Literal[
        "REQUEST_TYPE_UNSPECIFIED", "REQUEST_BODY", "QUERY_PARAMETERS", "ENCODED_HEADER"
    ]
    scope: str
    tokenEndpoint: str
    tokenParams: GoogleCloudIntegrationsV1alphaParameterMap

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaOAuth2ClientCredentials(
    typing_extensions.TypedDict, total=False
):
    accessToken: GoogleCloudIntegrationsV1alphaAccessToken
    clientId: str
    clientSecret: str
    requestType: typing_extensions.Literal[
        "REQUEST_TYPE_UNSPECIFIED", "REQUEST_BODY", "QUERY_PARAMETERS", "ENCODED_HEADER"
    ]
    scope: str
    tokenEndpoint: str
    tokenParams: GoogleCloudIntegrationsV1alphaParameterMap

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaOAuth2ResourceOwnerCredentials(
    typing_extensions.TypedDict, total=False
):
    accessToken: GoogleCloudIntegrationsV1alphaAccessToken
    clientId: str
    clientSecret: str
    password: str
    requestType: typing_extensions.Literal[
        "REQUEST_TYPE_UNSPECIFIED", "REQUEST_BODY", "QUERY_PARAMETERS", "ENCODED_HEADER"
    ]
    scope: str
    tokenEndpoint: str
    tokenParams: GoogleCloudIntegrationsV1alphaParameterMap
    username: str

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaOidcToken(typing_extensions.TypedDict, total=False):
    audience: str
    serviceAccountEmail: str
    token: str
    tokenExpireTime: str

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaParameterMap(
    typing_extensions.TypedDict, total=False
):
    entries: _list[GoogleCloudIntegrationsV1alphaParameterMapEntry]
    keyType: typing_extensions.Literal[
        "INTEGRATION_PARAMETER_DATA_TYPE_UNSPECIFIED",
        "STRING_VALUE",
        "INT_VALUE",
        "DOUBLE_VALUE",
        "BOOLEAN_VALUE",
        "STRING_ARRAY",
        "INT_ARRAY",
        "DOUBLE_ARRAY",
        "BOOLEAN_ARRAY",
        "JSON_VALUE",
        "PROTO_VALUE",
        "PROTO_ARRAY",
    ]
    valueType: typing_extensions.Literal[
        "INTEGRATION_PARAMETER_DATA_TYPE_UNSPECIFIED",
        "STRING_VALUE",
        "INT_VALUE",
        "DOUBLE_VALUE",
        "BOOLEAN_VALUE",
        "STRING_ARRAY",
        "INT_ARRAY",
        "DOUBLE_ARRAY",
        "BOOLEAN_ARRAY",
        "JSON_VALUE",
        "PROTO_VALUE",
        "PROTO_ARRAY",
    ]

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaParameterMapEntry(
    typing_extensions.TypedDict, total=False
):
    key: GoogleCloudIntegrationsV1alphaParameterMapField
    value: GoogleCloudIntegrationsV1alphaParameterMapField

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaParameterMapField(
    typing_extensions.TypedDict, total=False
):
    literalValue: GoogleCloudIntegrationsV1alphaValueType
    referenceKey: str

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaPublishIntegrationVersionRequest(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaPublishIntegrationVersionResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaResolveSuspensionRequest(
    typing_extensions.TypedDict, total=False
):
    suspension: GoogleCloudIntegrationsV1alphaSuspension

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaResolveSuspensionResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaRuntimeActionSchema(
    typing_extensions.TypedDict, total=False
):
    action: str
    inputSchema: str
    outputSchema: str

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaRuntimeEntitySchema(
    typing_extensions.TypedDict, total=False
):
    arrayFieldSchema: str
    entity: str
    fieldSchema: str

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaScheduleIntegrationsRequest(
    typing_extensions.TypedDict, total=False
):
    inputParameters: dict[str, typing.Any]
    parameterEntries: _list[EnterpriseCrmFrontendsEventbusProtoParameterEntry]
    parameters: EnterpriseCrmEventbusProtoEventParameters
    requestId: str
    scheduleTime: str
    triggerId: str

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaScheduleIntegrationsResponse(
    typing_extensions.TypedDict, total=False
):
    executionInfoIds: _list[str]

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaServiceAccountCredentials(
    typing_extensions.TypedDict, total=False
):
    scope: str
    serviceAccount: str

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaSfdcChannel(
    typing_extensions.TypedDict, total=False
):
    channelTopic: str
    createTime: str
    deleteTime: str
    description: str
    displayName: str
    isActive: bool
    lastReplayId: str
    name: str
    updateTime: str

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaSfdcInstance(
    typing_extensions.TypedDict, total=False
):
    authConfigId: _list[str]
    createTime: str
    deleteTime: str
    description: str
    displayName: str
    name: str
    serviceAuthority: str
    sfdcOrgId: str
    updateTime: str

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaStringParameterArray(
    typing_extensions.TypedDict, total=False
):
    stringValues: _list[str]

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaSuccessPolicy(
    typing_extensions.TypedDict, total=False
):
    finalState: typing_extensions.Literal[
        "FINAL_STATE_UNSPECIFIED", "SUCCEEDED", "SUSPENDED"
    ]

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaSuspension(
    typing_extensions.TypedDict, total=False
):
    approvalConfig: GoogleCloudIntegrationsV1alphaSuspensionApprovalConfig
    audit: GoogleCloudIntegrationsV1alphaSuspensionAudit
    createTime: str
    eventExecutionInfoId: str
    integration: str
    lastModifyTime: str
    name: str
    state: typing_extensions.Literal[
        "RESOLUTION_STATE_UNSPECIFIED", "PENDING", "REJECTED", "LIFTED"
    ]
    suspensionConfig: EnterpriseCrmEventbusProtoSuspensionConfig
    taskId: str

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaSuspensionApprovalConfig(
    typing_extensions.TypedDict, total=False
):
    customMessage: str
    emailAddresses: _list[str]
    expiration: GoogleCloudIntegrationsV1alphaSuspensionApprovalExpiration

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaSuspensionApprovalExpiration(
    typing_extensions.TypedDict, total=False
):
    expireTime: str
    liftWhenExpired: bool
    remindTime: str

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaSuspensionAudit(
    typing_extensions.TypedDict, total=False
):
    resolveTime: str
    resolver: str

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaTakeoverEditLockRequest(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaTakeoverEditLockResponse(
    typing_extensions.TypedDict, total=False
):
    integrationVersion: GoogleCloudIntegrationsV1alphaIntegrationVersion

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaTaskConfig(
    typing_extensions.TypedDict, total=False
):
    description: str
    displayName: str
    failurePolicy: GoogleCloudIntegrationsV1alphaFailurePolicy
    jsonValidationOption: typing_extensions.Literal[
        "JSON_VALIDATION_OPTION_UNSPECIFIED",
        "SKIP",
        "PRE_EXECUTION",
        "POST_EXECUTION",
        "PRE_POST_EXECUTION",
    ]
    nextTasks: _list[GoogleCloudIntegrationsV1alphaNextTask]
    nextTasksExecutionPolicy: typing_extensions.Literal[
        "NEXT_TASKS_EXECUTION_POLICY_UNSPECIFIED", "RUN_ALL_MATCH", "RUN_FIRST_MATCH"
    ]
    parameters: dict[str, typing.Any]
    successPolicy: GoogleCloudIntegrationsV1alphaSuccessPolicy
    synchronousCallFailurePolicy: GoogleCloudIntegrationsV1alphaFailurePolicy
    task: str
    taskExecutionStrategy: typing_extensions.Literal[
        "TASK_EXECUTION_STRATEGY_UNSPECIFIED",
        "WHEN_ALL_SUCCEED",
        "WHEN_ANY_SUCCEED",
        "WHEN_ALL_TASKS_AND_CONDITIONS_SUCCEED",
    ]
    taskId: str
    taskTemplate: str

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaTaskExecutionDetails(
    typing_extensions.TypedDict, total=False
):
    taskAttemptStats: _list[GoogleCloudIntegrationsV1alphaAttemptStats]
    taskExecutionState: typing_extensions.Literal[
        "TASK_EXECUTION_STATE_UNSPECIFIED",
        "PENDING_EXECUTION",
        "IN_PROCESS",
        "SUCCEED",
        "FAILED",
        "FATAL",
        "RETRY_ON_HOLD",
        "SKIPPED",
        "CANCELLED",
        "PENDING_ROLLBACK",
        "ROLLBACK_IN_PROCESS",
        "ROLLEDBACK",
        "SUSPENDED",
    ]
    taskNumber: str

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaTriggerConfig(
    typing_extensions.TypedDict, total=False
):
    alertConfig: _list[GoogleCloudIntegrationsV1alphaIntegrationAlertConfig]
    description: str
    label: str
    nextTasksExecutionPolicy: typing_extensions.Literal[
        "NEXT_TASKS_EXECUTION_POLICY_UNSPECIFIED", "RUN_ALL_MATCH", "RUN_FIRST_MATCH"
    ]
    properties: dict[str, typing.Any]
    startTasks: _list[GoogleCloudIntegrationsV1alphaNextTask]
    triggerId: str
    triggerNumber: str
    triggerType: typing_extensions.Literal[
        "TRIGGER_TYPE_UNSPECIFIED",
        "CRON",
        "API",
        "SFDC_CHANNEL",
        "CLOUD_PUBSUB_EXTERNAL",
        "SFDC_CDC_CHANNEL",
    ]

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaUpdateBundleRequest(
    typing_extensions.TypedDict, total=False
):
    config: GoogleCloudIntegrationsV1alphaIntegrationBundleConfig

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaUpdateBundleResponse(
    typing_extensions.TypedDict, total=False
):
    config: GoogleCloudIntegrationsV1alphaIntegrationBundleConfig

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaUploadIntegrationVersionRequest(
    typing_extensions.TypedDict, total=False
):
    content: str
    fileFormat: typing_extensions.Literal["FILE_FORMAT_UNSPECIFIED", "JSON", "YAML"]

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaUploadIntegrationVersionResponse(
    typing_extensions.TypedDict, total=False
):
    integrationVersion: GoogleCloudIntegrationsV1alphaIntegrationVersion

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaUsernameAndPassword(
    typing_extensions.TypedDict, total=False
):
    password: str
    username: str

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaValidateIntegrationVersionRequest(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaValidateIntegrationVersionResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaValueType(typing_extensions.TypedDict, total=False):
    booleanArray: GoogleCloudIntegrationsV1alphaBooleanParameterArray
    booleanValue: bool
    doubleArray: GoogleCloudIntegrationsV1alphaDoubleParameterArray
    doubleValue: float
    intArray: GoogleCloudIntegrationsV1alphaIntParameterArray
    intValue: str
    jsonValue: str
    stringArray: GoogleCloudIntegrationsV1alphaStringParameterArray
    stringValue: str

@typing.type_check_only
class GoogleInternalCloudCrmEventbusV3PostToQueueWithTriggerIdRequest(
    typing_extensions.TypedDict, total=False
):
    clientId: str
    ignoreErrorIfNoActiveWorkflow: bool
    parameters: EnterpriseCrmEventbusProtoEventParameters
    priority: typing_extensions.Literal[
        "UNSPCIFIED", "SHEDDABLE", "SHEDDABLE_PLUS", "CRITICAL", "CRITICAL_PLUS"
    ]
    requestId: str
    scheduledTime: str
    testMode: bool
    triggerId: str
    workflowName: str

@typing.type_check_only
class GoogleProtobufEmpty(typing_extensions.TypedDict, total=False): ...
