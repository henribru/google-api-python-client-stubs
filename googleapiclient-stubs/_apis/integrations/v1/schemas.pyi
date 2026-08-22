import typing

_list = list

@typing.type_check_only
class CrmlogErrorCode(typing.TypedDict, total=False):
    commonErrorCode: typing.Literal[
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
class EnterpriseCrmEventbusAuthconfigAuthConfigTaskParam(typing.TypedDict, total=False):
    allowedCredentialTypes: _list[
        typing.Literal[
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
    ]
    allowedServiceAccountInContext: bool
    authConfigId: str
    scope: str
    useServiceAccountInContext: bool

@typing.type_check_only
class EnterpriseCrmEventbusProtoAddress(typing.TypedDict, total=False):
    email: str
    name: str
    tokens: _list[EnterpriseCrmEventbusProtoToken]

@typing.type_check_only
class EnterpriseCrmEventbusProtoAttributes(typing.TypedDict, total=False):
    dataType: typing.Literal[
        "DATA_TYPE_UNSPECIFIED", "EMAIL", "URL", "CURRENCY", "TIMESTAMP", "DOMAIN_NAME"
    ]
    defaultValue: EnterpriseCrmEventbusProtoValueType
    isRequired: bool
    isSearchable: bool
    logSettings: EnterpriseCrmEventbusProtoLogSettings
    masked: bool
    readOnly: bool
    searchable: typing.Literal["UNSPECIFIED", "YES", "NO"]
    taskVisibility: _list[str]

@typing.type_check_only
class EnterpriseCrmEventbusProtoBaseAlertConfigErrorEnumList(
    typing.TypedDict, total=False
):
    enumStrings: _list[str]
    filterType: typing.Literal["DEFAULT_INCLUSIVE", "EXCLUSIVE"]

@typing.type_check_only
class EnterpriseCrmEventbusProtoBaseAlertConfigThresholdValue(
    typing.TypedDict, total=False
):
    absolute: str
    percentage: int

@typing.type_check_only
class EnterpriseCrmEventbusProtoBaseFunction(typing.TypedDict, total=False):
    functionName: typing.Literal[
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
class EnterpriseCrmEventbusProtoBaseValue(typing.TypedDict, total=False):
    baseFunction: EnterpriseCrmEventbusProtoFunction
    literalValue: EnterpriseCrmEventbusProtoParameterValueType
    referenceValue: str

@typing.type_check_only
class EnterpriseCrmEventbusProtoBooleanArrayFunction(typing.TypedDict, total=False):
    functionName: typing.Literal[
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
class EnterpriseCrmEventbusProtoBooleanFunction(typing.TypedDict, total=False):
    functionName: typing.Literal[
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
class EnterpriseCrmEventbusProtoBooleanParameterArray(typing.TypedDict, total=False):
    booleanValues: _list[bool]

@typing.type_check_only
class EnterpriseCrmEventbusProtoBuganizerNotification(typing.TypedDict, total=False):
    assigneeEmailAddress: str
    componentId: str
    templateId: str
    title: str

@typing.type_check_only
class EnterpriseCrmEventbusProtoCloudKmsConfig(typing.TypedDict, total=False):
    gcpProjectId: str
    keyName: str
    keyRingName: str
    keyVersionName: str
    locationName: str
    serviceAccount: str

@typing.type_check_only
class EnterpriseCrmEventbusProtoCloudLoggingDetails(typing.TypedDict, total=False):
    cloudLoggingSeverity: typing.Literal[
        "CLOUD_LOGGING_SEVERITY_UNSPECIFIED", "INFO", "ERROR", "WARNING"
    ]
    enableCloudLogging: bool

@typing.type_check_only
class EnterpriseCrmEventbusProtoCloudSchedulerConfig(typing.TypedDict, total=False):
    cronTab: str
    errorMessage: str
    location: str
    serviceAccountEmail: str

@typing.type_check_only
class EnterpriseCrmEventbusProtoCombinedCondition(typing.TypedDict, total=False):
    conditions: _list[EnterpriseCrmEventbusProtoCondition]

@typing.type_check_only
class EnterpriseCrmEventbusProtoCondition(typing.TypedDict, total=False):
    eventPropertyKey: str
    operator: typing.Literal[
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
class EnterpriseCrmEventbusProtoConditionResult(typing.TypedDict, total=False):
    currentTaskNumber: str
    nextTaskNumber: str
    result: bool

@typing.type_check_only
class EnterpriseCrmEventbusProtoConditionalFailurePolicies(
    typing.TypedDict, total=False
):
    defaultFailurePolicy: EnterpriseCrmEventbusProtoFailurePolicy
    failurePolicies: _list[EnterpriseCrmEventbusProtoFailurePolicy]

@typing.type_check_only
class EnterpriseCrmEventbusProtoConnectorsConnection(typing.TypedDict, total=False):
    connectionName: str
    connectorVersion: str
    host: str
    serviceName: str

@typing.type_check_only
class EnterpriseCrmEventbusProtoConnectorsGenericConnectorTaskConfig(
    typing.TypedDict, total=False
):
    connection: EnterpriseCrmEventbusProtoConnectorsConnection
    operation: typing.Literal[
        "OPERATION_UNSPECIFIED",
        "EXECUTE_ACTION",
        "LIST_ENTITIES",
        "GET_ENTITY",
        "CREATE_ENTITY",
        "UPDATE_ENTITY",
        "DELETE_ENTITY",
        "EXECUTE_QUERY",
    ]

@typing.type_check_only
class EnterpriseCrmEventbusProtoCoordinate(typing.TypedDict, total=False):
    x: int
    y: int

@typing.type_check_only
class EnterpriseCrmEventbusProtoCustomSuspensionRequest(typing.TypedDict, total=False):
    postToQueueWithTriggerIdRequest: (
        GoogleInternalCloudCrmEventbusV3PostToQueueWithTriggerIdRequest
    )
    suspensionInfoEventParameterKey: str

@typing.type_check_only
class EnterpriseCrmEventbusProtoDoubleArray(typing.TypedDict, total=False):
    values: _list[float]

@typing.type_check_only
class EnterpriseCrmEventbusProtoDoubleArrayFunction(typing.TypedDict, total=False):
    functionName: typing.Literal[
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
class EnterpriseCrmEventbusProtoDoubleFunction(typing.TypedDict, total=False):
    functionName: typing.Literal[
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
class EnterpriseCrmEventbusProtoDoubleParameterArray(typing.TypedDict, total=False):
    doubleValues: _list[float]

@typing.type_check_only
class EnterpriseCrmEventbusProtoErrorDetail(typing.TypedDict, total=False):
    errorCode: CrmlogErrorCode
    errorMessage: str
    severity: typing.Literal["SEVERITY_UNSPECIFIED", "ERROR", "WARN", "INFO"]
    taskNumber: int

@typing.type_check_only
class EnterpriseCrmEventbusProtoEventBusProperties(typing.TypedDict, total=False):
    properties: _list[EnterpriseCrmEventbusProtoPropertyEntry]

@typing.type_check_only
class EnterpriseCrmEventbusProtoEventExecutionDetails(typing.TypedDict, total=False):
    cancelReason: str
    eventAttemptStats: _list[
        EnterpriseCrmEventbusProtoEventExecutionDetailsEventAttemptStats
    ]
    eventExecutionSnapshot: _list[EnterpriseCrmEventbusProtoEventExecutionSnapshot]
    eventExecutionSnapshotsSize: str
    eventExecutionState: typing.Literal[
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
    typing.TypedDict, total=False
):
    endTime: str
    startTime: str

@typing.type_check_only
class EnterpriseCrmEventbusProtoEventExecutionSnapshot(typing.TypedDict, total=False):
    checkpointTaskNumber: str
    clientId: str
    conditionResults: _list[EnterpriseCrmEventbusProtoConditionResult]
    diffParams: EnterpriseCrmEventbusProtoEventParameters
    eventExecutionInfoId: str
    eventExecutionSnapshotId: str
    eventExecutionSnapshotMetadata: (
        EnterpriseCrmEventbusProtoEventExecutionSnapshotEventExecutionSnapshotMetadata
    )
    eventParams: EnterpriseCrmEventbusProtoEventParameters
    exceedMaxSize: bool
    snapshotTime: str
    taskExecutionDetails: _list[EnterpriseCrmEventbusProtoTaskExecutionDetails]
    taskName: str
    workflowName: str

@typing.type_check_only
class EnterpriseCrmEventbusProtoEventExecutionSnapshotEventExecutionSnapshotMetadata(
    typing.TypedDict, total=False
):
    ancestorIterationNumbers: _list[str]
    ancestorTaskNumbers: _list[str]
    eventAttemptNum: int
    integrationName: str
    taskAttemptNum: int
    taskLabel: str
    taskName: str
    taskNumber: str

@typing.type_check_only
class EnterpriseCrmEventbusProtoEventParameters(typing.TypedDict, total=False):
    parameters: _list[EnterpriseCrmEventbusProtoParameterEntry]

@typing.type_check_only
class EnterpriseCrmEventbusProtoExecutionTraceInfo(typing.TypedDict, total=False):
    parentEventExecutionInfoId: str
    traceId: str

@typing.type_check_only
class EnterpriseCrmEventbusProtoExternalTraffic(typing.TypedDict, total=False):
    enableInternalIp: bool
    gcpProjectId: str
    gcpProjectNumber: str
    location: str
    retryRequestForQuota: bool
    source: typing.Literal["SOURCE_UNSPECIFIED", "APIGEE", "SECURITY"]

@typing.type_check_only
class EnterpriseCrmEventbusProtoFailurePolicy(typing.TypedDict, total=False):
    intervalInSeconds: str
    maxNumRetries: int
    retryCondition: str
    retryStrategy: typing.Literal[
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
class EnterpriseCrmEventbusProtoField(typing.TypedDict, total=False):
    cardinality: typing.Literal["UNSPECIFIED", "OPTIONAL"]
    defaultValue: EnterpriseCrmEventbusProtoParameterValueType
    fieldType: typing.Literal[
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
class EnterpriseCrmEventbusProtoFieldMappingConfig(typing.TypedDict, total=False):
    mappedFields: _list[EnterpriseCrmEventbusProtoMappedField]

@typing.type_check_only
class EnterpriseCrmEventbusProtoFunction(typing.TypedDict, total=False):
    functionType: EnterpriseCrmEventbusProtoFunctionType
    parameters: _list[EnterpriseCrmEventbusProtoTransformExpression]

@typing.type_check_only
class EnterpriseCrmEventbusProtoFunctionType(typing.TypedDict, total=False):
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
class EnterpriseCrmEventbusProtoIntArray(typing.TypedDict, total=False):
    values: _list[str]

@typing.type_check_only
class EnterpriseCrmEventbusProtoIntArrayFunction(typing.TypedDict, total=False):
    functionName: typing.Literal[
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
class EnterpriseCrmEventbusProtoIntFunction(typing.TypedDict, total=False):
    functionName: typing.Literal[
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
class EnterpriseCrmEventbusProtoIntParameterArray(typing.TypedDict, total=False):
    intValues: _list[str]

@typing.type_check_only
class EnterpriseCrmEventbusProtoJsonFunction(typing.TypedDict, total=False):
    functionName: typing.Literal[
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
class EnterpriseCrmEventbusProtoLogSettings(typing.TypedDict, total=False):
    logFieldName: str
    seedPeriod: typing.Literal["SEED_PERIOD_UNSPECIFIED", "DAY", "WEEK", "MONTH"]
    seedScope: typing.Literal[
        "SEED_SCOPE_UNSPECIFIED", "EVENT_NAME", "TIME_PERIOD", "PARAM_NAME"
    ]

@typing.type_check_only
class EnterpriseCrmEventbusProtoLoopMetadata(typing.TypedDict, total=False):
    currentIterationCount: str
    currentIterationDetail: str
    errorMsg: str
    failureLocation: typing.Literal[
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
class EnterpriseCrmEventbusProtoMappedField(typing.TypedDict, total=False):
    inputField: EnterpriseCrmEventbusProtoField
    outputField: EnterpriseCrmEventbusProtoField

@typing.type_check_only
class EnterpriseCrmEventbusProtoNextTask(typing.TypedDict, total=False):
    combinedConditions: _list[EnterpriseCrmEventbusProtoCombinedCondition]
    condition: str
    description: str
    label: str
    taskConfigId: str
    taskNumber: str

@typing.type_check_only
class EnterpriseCrmEventbusProtoNextTeardownTask(typing.TypedDict, total=False):
    name: str

@typing.type_check_only
class EnterpriseCrmEventbusProtoNodeIdentifier(typing.TypedDict, total=False):
    elementIdentifier: str
    elementType: typing.Literal["UNKNOWN_TYPE", "TASK_CONFIG", "TRIGGER_CONFIG"]

@typing.type_check_only
class EnterpriseCrmEventbusProtoNotification(typing.TypedDict, total=False):
    buganizerNotification: EnterpriseCrmEventbusProtoBuganizerNotification
    emailAddress: EnterpriseCrmEventbusProtoAddress
    escalatorQueue: str
    pubsubTopic: str
    request: EnterpriseCrmEventbusProtoCustomSuspensionRequest

@typing.type_check_only
class EnterpriseCrmEventbusProtoParamSpecEntryConfig(typing.TypedDict, total=False):
    descriptivePhrase: str
    helpText: str
    hideDefaultValue: bool
    inputDisplayOption: typing.Literal[
        "DEFAULT", "STRING_MULTI_LINE", "NUMBER_SLIDER", "BOOLEAN_TOGGLE"
    ]
    isHidden: bool
    label: str
    parameterNameOption: typing.Literal[
        "DEFAULT_NOT_PARAMETER_NAME",
        "IS_PARAMETER_NAME",
        "KEY_IS_PARAMETER_NAME",
        "VALUE_IS_PARAMETER_NAME",
    ]
    subSectionLabel: str
    uiPlaceholderText: str

@typing.type_check_only
class EnterpriseCrmEventbusProtoParamSpecEntryProtoDefinition(
    typing.TypedDict, total=False
):
    fullName: str
    path: str

@typing.type_check_only
class EnterpriseCrmEventbusProtoParamSpecEntryValidationRule(
    typing.TypedDict, total=False
):
    doubleRange: EnterpriseCrmEventbusProtoParamSpecEntryValidationRuleDoubleRange
    intRange: EnterpriseCrmEventbusProtoParamSpecEntryValidationRuleIntRange
    stringRegex: EnterpriseCrmEventbusProtoParamSpecEntryValidationRuleStringRegex

@typing.type_check_only
class EnterpriseCrmEventbusProtoParamSpecEntryValidationRuleDoubleRange(
    typing.TypedDict, total=False
):
    max: float
    min: float

@typing.type_check_only
class EnterpriseCrmEventbusProtoParamSpecEntryValidationRuleIntRange(
    typing.TypedDict, total=False
):
    max: str
    min: str

@typing.type_check_only
class EnterpriseCrmEventbusProtoParamSpecEntryValidationRuleStringRegex(
    typing.TypedDict, total=False
):
    exclusive: bool
    regex: str

@typing.type_check_only
class EnterpriseCrmEventbusProtoParameterEntry(typing.TypedDict, total=False):
    key: str
    masked: bool
    value: EnterpriseCrmEventbusProtoParameterValueType

@typing.type_check_only
class EnterpriseCrmEventbusProtoParameterMap(typing.TypedDict, total=False):
    entries: _list[EnterpriseCrmEventbusProtoParameterMapEntry]
    keyType: typing.Literal[
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
    valueType: typing.Literal[
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
class EnterpriseCrmEventbusProtoParameterMapEntry(typing.TypedDict, total=False):
    key: EnterpriseCrmEventbusProtoParameterMapField
    value: EnterpriseCrmEventbusProtoParameterMapField

@typing.type_check_only
class EnterpriseCrmEventbusProtoParameterMapField(typing.TypedDict, total=False):
    literalValue: EnterpriseCrmEventbusProtoParameterValueType
    referenceKey: str

@typing.type_check_only
class EnterpriseCrmEventbusProtoParameterValueType(typing.TypedDict, total=False):
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
class EnterpriseCrmEventbusProtoPropertyEntry(typing.TypedDict, total=False):
    key: str
    value: EnterpriseCrmEventbusProtoValueType

@typing.type_check_only
class EnterpriseCrmEventbusProtoProtoArrayFunction(typing.TypedDict, total=False):
    functionName: typing.Literal[
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
class EnterpriseCrmEventbusProtoProtoFunction(typing.TypedDict, total=False):
    functionName: typing.Literal[
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
class EnterpriseCrmEventbusProtoProtoParameterArray(typing.TypedDict, total=False):
    protoValues: _list[dict[str, typing.Any]]

@typing.type_check_only
class EnterpriseCrmEventbusProtoScatterResponse(typing.TypedDict, total=False):
    errorMsg: str
    executionIds: _list[str]
    isSuccessful: bool
    responseParams: _list[EnterpriseCrmEventbusProtoParameterEntry]
    scatterElement: EnterpriseCrmEventbusProtoParameterValueType

@typing.type_check_only
class EnterpriseCrmEventbusProtoSerializedObjectParameter(
    typing.TypedDict, total=False
):
    objectValue: str

@typing.type_check_only
class EnterpriseCrmEventbusProtoStringArray(typing.TypedDict, total=False):
    values: _list[str]

@typing.type_check_only
class EnterpriseCrmEventbusProtoStringArrayFunction(typing.TypedDict, total=False):
    functionName: typing.Literal[
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
class EnterpriseCrmEventbusProtoStringFunction(typing.TypedDict, total=False):
    functionName: typing.Literal[
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
        "DECODE_BASE64_STRING",
    ]

@typing.type_check_only
class EnterpriseCrmEventbusProtoStringParameterArray(typing.TypedDict, total=False):
    stringValues: _list[str]

@typing.type_check_only
class EnterpriseCrmEventbusProtoSuccessPolicy(typing.TypedDict, total=False):
    finalState: typing.Literal["UNSPECIFIED", "SUCCEEDED", "SUSPENDED"]

@typing.type_check_only
class EnterpriseCrmEventbusProtoSuspensionAuthPermissions(
    typing.TypedDict, total=False
):
    gaiaIdentity: EnterpriseCrmEventbusProtoSuspensionAuthPermissionsGaiaIdentity
    googleGroup: EnterpriseCrmEventbusProtoSuspensionAuthPermissionsGaiaIdentity
    loasRole: str
    mdbGroup: str

@typing.type_check_only
class EnterpriseCrmEventbusProtoSuspensionAuthPermissionsGaiaIdentity(
    typing.TypedDict, total=False
):
    emailAddress: str
    gaiaId: str

@typing.type_check_only
class EnterpriseCrmEventbusProtoSuspensionConfig(typing.TypedDict, total=False):
    customMessage: str
    notifications: _list[EnterpriseCrmEventbusProtoNotification]
    suspensionExpiration: EnterpriseCrmEventbusProtoSuspensionExpiration
    whoMayResolve: _list[EnterpriseCrmEventbusProtoSuspensionAuthPermissions]

@typing.type_check_only
class EnterpriseCrmEventbusProtoSuspensionExpiration(typing.TypedDict, total=False):
    expireAfterMs: int
    liftWhenExpired: bool
    remindAfterMs: int

@typing.type_check_only
class EnterpriseCrmEventbusProtoSuspensionResolutionInfo(typing.TypedDict, total=False):
    audit: EnterpriseCrmEventbusProtoSuspensionResolutionInfoAudit
    clientId: str
    cloudKmsConfig: EnterpriseCrmEventbusProtoCloudKmsConfig
    createdTimestamp: str
    encryptedSuspensionResolutionInfo: str
    eventExecutionInfoId: str
    externalTraffic: EnterpriseCrmEventbusProtoExternalTraffic
    lastModifiedTimestamp: str
    product: typing.Literal["UNSPECIFIED_PRODUCT", "IP", "APIGEE", "SECURITY"]
    status: typing.Literal["PENDING_UNSPECIFIED", "REJECTED", "LIFTED", "CANCELED"]
    suspensionConfig: EnterpriseCrmEventbusProtoSuspensionConfig
    suspensionId: str
    taskNumber: str
    workflowName: str
    wrappedDek: str

@typing.type_check_only
class EnterpriseCrmEventbusProtoSuspensionResolutionInfoAudit(
    typing.TypedDict, total=False
):
    resolvedBy: str
    resolvedByCpi: str
    timestamp: str

@typing.type_check_only
class EnterpriseCrmEventbusProtoTaskAlertConfig(typing.TypedDict, total=False):
    aggregationPeriod: str
    alertDisabled: bool
    alertName: str
    clientId: str
    durationThresholdMs: str
    errorEnumList: EnterpriseCrmEventbusProtoBaseAlertConfigErrorEnumList
    metricType: typing.Literal[
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
    thresholdType: typing.Literal[
        "UNSPECIFIED_THRESHOLD_TYPE", "EXPECTED_MIN", "EXPECTED_MAX"
    ]
    thresholdValue: EnterpriseCrmEventbusProtoBaseAlertConfigThresholdValue
    warningEnumList: EnterpriseCrmEventbusProtoBaseAlertConfigErrorEnumList

@typing.type_check_only
class EnterpriseCrmEventbusProtoTaskExecutionDetails(typing.TypedDict, total=False):
    skippedOnFailure: bool
    taskAttemptStats: _list[
        EnterpriseCrmEventbusProtoTaskExecutionDetailsTaskAttemptStats
    ]
    taskExecutionState: typing.Literal[
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
    typing.TypedDict, total=False
):
    endTime: str
    startTime: str

@typing.type_check_only
class EnterpriseCrmEventbusProtoTaskMetadata(typing.TypedDict, total=False):
    activeTaskName: str
    admins: _list[EnterpriseCrmEventbusProtoTaskMetadataAdmin]
    category: typing.Literal[
        "UNSPECIFIED_CATEGORY",
        "CUSTOM",
        "FLOW_CONTROL",
        "DATA_MANIPULATION",
        "SCRIPTING",
        "CONNECTOR",
        "HIDDEN",
        "CLOUD_SYSTEMS",
        "CUSTOM_TASK_TEMPLATE",
        "TASK_RECOMMENDATIONS",
    ]
    codeSearchLink: str
    defaultJsonValidationOption: typing.Literal[
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
    externalCategory: typing.Literal[
        "UNSPECIFIED_EXTERNAL_CATEGORY",
        "CORE",
        "CONNECTORS",
        "EXTERNAL_HTTP",
        "EXTERNAL_INTEGRATION_SERVICES",
        "EXTERNAL_CUSTOMER_ACTIONS",
        "EXTERNAL_FLOW_CONTROL",
        "EXTERNAL_WORKSPACE",
        "EXTERNAL_SECURITY",
        "EXTERNAL_DATABASES",
        "EXTERNAL_ANALYTICS",
        "EXTERNAL_BYOC",
        "EXTERNAL_BYOT",
        "EXTERNAL_ARTIFICIAL_INTELIGENCE",
        "EXTERNAL_DATA_MANIPULATION",
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
    status: typing.Literal["UNSPECIFIED_STATUS", "DEFAULT_INACTIVE", "ACTIVE"]
    system: typing.Literal[
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
class EnterpriseCrmEventbusProtoTaskMetadataAdmin(typing.TypedDict, total=False):
    googleGroupEmail: str
    userEmail: str

@typing.type_check_only
class EnterpriseCrmEventbusProtoTaskUiConfig(typing.TypedDict, total=False):
    taskUiModuleConfigs: _list[EnterpriseCrmEventbusProtoTaskUiModuleConfig]

@typing.type_check_only
class EnterpriseCrmEventbusProtoTaskUiModuleConfig(typing.TypedDict, total=False):
    moduleId: typing.Literal[
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
class EnterpriseCrmEventbusProtoTeardown(typing.TypedDict, total=False):
    teardownTaskConfigs: _list[EnterpriseCrmEventbusProtoTeardownTaskConfig]

@typing.type_check_only
class EnterpriseCrmEventbusProtoTeardownTaskConfig(typing.TypedDict, total=False):
    creatorEmail: str
    name: str
    nextTeardownTask: EnterpriseCrmEventbusProtoNextTeardownTask
    parameters: EnterpriseCrmEventbusProtoEventParameters
    properties: EnterpriseCrmEventbusProtoEventBusProperties
    teardownTaskImplementationClassName: str

@typing.type_check_only
class EnterpriseCrmEventbusProtoToken(typing.TypedDict, total=False):
    name: str
    value: str

@typing.type_check_only
class EnterpriseCrmEventbusProtoTransformExpression(typing.TypedDict, total=False):
    initialValue: EnterpriseCrmEventbusProtoBaseValue
    transformationFunctions: _list[EnterpriseCrmEventbusProtoFunction]

@typing.type_check_only
class EnterpriseCrmEventbusProtoTriggerCriteria(typing.TypedDict, total=False):
    condition: str
    parameters: EnterpriseCrmEventbusProtoEventParameters
    triggerCriteriaTaskImplementationClassName: str

@typing.type_check_only
class EnterpriseCrmEventbusProtoValueType(typing.TypedDict, total=False):
    booleanValue: bool
    doubleArray: EnterpriseCrmEventbusProtoDoubleArray
    doubleValue: float
    intArray: EnterpriseCrmEventbusProtoIntArray
    intValue: str
    protoValue: dict[str, typing.Any]
    stringArray: EnterpriseCrmEventbusProtoStringArray
    stringValue: str

@typing.type_check_only
class EnterpriseCrmEventbusProtoWorkflowAlertConfig(typing.TypedDict, total=False):
    aggregationPeriod: str
    alertDisabled: bool
    alertName: str
    clientId: str
    durationThresholdMs: str
    errorEnumList: EnterpriseCrmEventbusProtoBaseAlertConfigErrorEnumList
    metricType: typing.Literal[
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
    thresholdType: typing.Literal[
        "UNSPECIFIED_THRESHOLD_TYPE", "EXPECTED_MIN", "EXPECTED_MAX"
    ]
    thresholdValue: EnterpriseCrmEventbusProtoBaseAlertConfigThresholdValue
    warningEnumList: EnterpriseCrmEventbusProtoBaseAlertConfigErrorEnumList

@typing.type_check_only
class EnterpriseCrmEventbusStats(typing.TypedDict, total=False):
    dimensions: EnterpriseCrmEventbusStatsDimensions
    durationInSeconds: float
    errorRate: float
    qps: float
    warningRate: float

@typing.type_check_only
class EnterpriseCrmEventbusStatsDimensions(typing.TypedDict, total=False):
    clientId: str
    enumFilterType: typing.Literal["DEFAULT_INCLUSIVE", "EXCLUSIVE"]
    errorEnumString: str
    retryAttempt: typing.Literal["UNSPECIFIED", "FINAL", "RETRYABLE", "CANCELED"]
    taskName: str
    taskNumber: str
    triggerId: str
    warningEnumString: str
    workflowId: str
    workflowName: str

@typing.type_check_only
class EnterpriseCrmFrontendsEventbusProtoBooleanParameterArray(
    typing.TypedDict, total=False
):
    booleanValues: _list[bool]

@typing.type_check_only
class EnterpriseCrmFrontendsEventbusProtoDoubleParameterArray(
    typing.TypedDict, total=False
):
    doubleValues: _list[float]

@typing.type_check_only
class EnterpriseCrmFrontendsEventbusProtoEventExecutionDetails(
    typing.TypedDict, total=False
):
    cancelReason: str
    eventAttemptStats: _list[
        EnterpriseCrmEventbusProtoEventExecutionDetailsEventAttemptStats
    ]
    eventExecutionSnapshot: _list[
        EnterpriseCrmFrontendsEventbusProtoEventExecutionSnapshot
    ]
    eventExecutionSnapshotsSize: str
    eventExecutionState: typing.Literal[
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
    typing.TypedDict, total=False
):
    clientId: str
    cloudLoggingDetails: EnterpriseCrmEventbusProtoCloudLoggingDetails
    createTime: str
    errorCode: CrmlogErrorCode
    errors: _list[EnterpriseCrmEventbusProtoErrorDetail]
    eventExecutionDetails: EnterpriseCrmFrontendsEventbusProtoEventExecutionDetails
    eventExecutionInfoId: str
    executionTraceInfo: EnterpriseCrmEventbusProtoExecutionTraceInfo
    integrationVersionUserLabel: str
    lastModifiedTime: str
    postMethod: typing.Literal[
        "UNSPECIFIED",
        "POST",
        "POST_TO_QUEUE",
        "SCHEDULE",
        "POST_BY_EVENT_CONFIG_ID",
        "POST_WITH_EVENT_DETAILS",
    ]
    product: typing.Literal["UNSPECIFIED_PRODUCT", "IP", "APIGEE", "SECURITY"]
    replayInfo: EnterpriseCrmFrontendsEventbusProtoEventExecutionInfoReplayInfo
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
class EnterpriseCrmFrontendsEventbusProtoEventExecutionInfoReplayInfo(
    typing.TypedDict, total=False
):
    originalExecutionInfoId: str
    replayMode: typing.Literal[
        "REPLAY_MODE_UNSPECIFIED",
        "REPLAY_MODE_FROM_BEGINNING",
        "REPLAY_MODE_POINT_OF_FAILURE",
    ]
    replayReason: str
    replayedExecutionInfoIds: _list[str]

@typing.type_check_only
class EnterpriseCrmFrontendsEventbusProtoEventExecutionSnapshot(
    typing.TypedDict, total=False
):
    checkpointTaskNumber: str
    conditionResults: _list[EnterpriseCrmEventbusProtoConditionResult]
    diffParams: EnterpriseCrmFrontendsEventbusProtoEventParameters
    eventExecutionInfoId: str
    eventExecutionSnapshotId: str
    eventExecutionSnapshotMetadata: (
        EnterpriseCrmEventbusProtoEventExecutionSnapshotEventExecutionSnapshotMetadata
    )
    eventParams: EnterpriseCrmFrontendsEventbusProtoEventParameters
    snapshotTime: str
    taskExecutionDetails: _list[EnterpriseCrmEventbusProtoTaskExecutionDetails]
    taskName: str

@typing.type_check_only
class EnterpriseCrmFrontendsEventbusProtoEventParameters(typing.TypedDict, total=False):
    parameters: _list[EnterpriseCrmFrontendsEventbusProtoParameterEntry]

@typing.type_check_only
class EnterpriseCrmFrontendsEventbusProtoIntParameterArray(
    typing.TypedDict, total=False
):
    intValues: _list[str]

@typing.type_check_only
class EnterpriseCrmFrontendsEventbusProtoParamSpecEntry(typing.TypedDict, total=False):
    className: str
    collectionElementClassName: str
    config: EnterpriseCrmEventbusProtoParamSpecEntryConfig
    dataType: typing.Literal[
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
    typing.TypedDict, total=False
):
    parameters: _list[EnterpriseCrmFrontendsEventbusProtoParamSpecEntry]

@typing.type_check_only
class EnterpriseCrmFrontendsEventbusProtoParameterEntry(typing.TypedDict, total=False):
    dataType: typing.Literal[
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
    masked: bool
    value: EnterpriseCrmFrontendsEventbusProtoParameterValueType

@typing.type_check_only
class EnterpriseCrmFrontendsEventbusProtoParameterMap(typing.TypedDict, total=False):
    entries: _list[EnterpriseCrmFrontendsEventbusProtoParameterMapEntry]
    keyType: typing.Literal[
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
    valueType: typing.Literal[
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
    typing.TypedDict, total=False
):
    key: EnterpriseCrmFrontendsEventbusProtoParameterMapField
    value: EnterpriseCrmFrontendsEventbusProtoParameterMapField

@typing.type_check_only
class EnterpriseCrmFrontendsEventbusProtoParameterMapField(
    typing.TypedDict, total=False
):
    literalValue: EnterpriseCrmFrontendsEventbusProtoParameterValueType
    referenceKey: str

@typing.type_check_only
class EnterpriseCrmFrontendsEventbusProtoParameterValueType(
    typing.TypedDict, total=False
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
    typing.TypedDict, total=False
):
    protoValues: _list[dict[str, typing.Any]]

@typing.type_check_only
class EnterpriseCrmFrontendsEventbusProtoRollbackStrategy(
    typing.TypedDict, total=False
):
    parameters: EnterpriseCrmFrontendsEventbusProtoEventParameters
    rollbackTaskImplementationClassName: str
    taskNumbersToRollback: _list[str]

@typing.type_check_only
class EnterpriseCrmFrontendsEventbusProtoSerializedObjectParameter(
    typing.TypedDict, total=False
):
    objectValue: str

@typing.type_check_only
class EnterpriseCrmFrontendsEventbusProtoStringParameterArray(
    typing.TypedDict, total=False
):
    stringValues: _list[str]

@typing.type_check_only
class EnterpriseCrmFrontendsEventbusProtoTaskConfig(typing.TypedDict, total=False):
    alertConfigs: _list[EnterpriseCrmEventbusProtoTaskAlertConfig]
    conditionalFailurePolicies: EnterpriseCrmEventbusProtoConditionalFailurePolicies
    createTime: str
    creatorEmail: str
    description: str
    disableStrictTypeValidation: bool
    errorCatcherId: str
    externalTaskType: typing.Literal[
        "EXTERNAL_TASK_TYPE_UNSPECIFIED", "NORMAL_TASK", "ERROR_TASK"
    ]
    failurePolicy: EnterpriseCrmEventbusProtoFailurePolicy
    incomingEdgeCount: int
    jsonValidationOption: typing.Literal[
        "UNSPECIFIED_JSON_VALIDATION_OPTION",
        "SKIP",
        "PRE_EXECUTION",
        "POST_EXECUTION",
        "PRE_POST_EXECUTION",
    ]
    label: str
    lastModifiedTime: str
    nextTasks: _list[EnterpriseCrmEventbusProtoNextTask]
    nextTasksExecutionPolicy: typing.Literal[
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
    taskExecutionStrategy: typing.Literal[
        "WHEN_ALL_SUCCEED", "WHEN_ANY_SUCCEED", "WHEN_ALL_TASKS_AND_CONDITIONS_SUCCEED"
    ]
    taskName: str
    taskNumber: str
    taskSpec: str
    taskTemplateName: str
    taskType: typing.Literal["TASK", "ASIS_TEMPLATE", "IO_TEMPLATE"]

@typing.type_check_only
class EnterpriseCrmFrontendsEventbusProtoTaskEntity(typing.TypedDict, total=False):
    disabledForVpcSc: bool
    metadata: EnterpriseCrmEventbusProtoTaskMetadata
    paramSpecs: EnterpriseCrmFrontendsEventbusProtoParamSpecsMessage
    stats: EnterpriseCrmEventbusStats
    taskType: typing.Literal["TASK", "ASIS_TEMPLATE", "IO_TEMPLATE"]
    uiConfig: EnterpriseCrmEventbusProtoTaskUiConfig

@typing.type_check_only
class EnterpriseCrmFrontendsEventbusProtoTriggerConfig(typing.TypedDict, total=False):
    alertConfig: _list[EnterpriseCrmEventbusProtoWorkflowAlertConfig]
    cloudSchedulerConfig: EnterpriseCrmEventbusProtoCloudSchedulerConfig
    description: str
    enabledClients: _list[str]
    errorCatcherId: str
    inputVariables: EnterpriseCrmFrontendsEventbusProtoTriggerConfigVariables
    label: str
    nextTasksExecutionPolicy: typing.Literal[
        "UNSPECIFIED", "RUN_ALL_MATCH", "RUN_FIRST_MATCH"
    ]
    outputVariables: EnterpriseCrmFrontendsEventbusProtoTriggerConfigVariables
    pauseWorkflowExecutions: bool
    position: EnterpriseCrmEventbusProtoCoordinate
    properties: dict[str, typing.Any]
    startTasks: _list[EnterpriseCrmEventbusProtoNextTask]
    triggerCriteria: EnterpriseCrmEventbusProtoTriggerCriteria
    triggerId: str
    triggerName: str
    triggerNumber: str
    triggerType: typing.Literal[
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
        "CLOUD_SCHEDULER",
        "INTEGRATION_CONNECTOR_TRIGGER",
        "PRIVATE_TRIGGER",
        "EVENTARC_TRIGGER",
    ]

@typing.type_check_only
class EnterpriseCrmFrontendsEventbusProtoTriggerConfigVariables(
    typing.TypedDict, total=False
):
    names: _list[str]

@typing.type_check_only
class EnterpriseCrmFrontendsEventbusProtoWorkflowParameterEntry(
    typing.TypedDict, total=False
):
    attributes: EnterpriseCrmEventbusProtoAttributes
    children: _list[EnterpriseCrmFrontendsEventbusProtoWorkflowParameterEntry]
    containsLargeData: bool
    dataType: typing.Literal[
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
    description: str
    inOutType: typing.Literal["IN_OUT_TYPE_UNSPECIFIED", "IN", "OUT", "IN_OUT"]
    isTransient: bool
    jsonSchema: str
    key: str
    name: str
    producedBy: EnterpriseCrmEventbusProtoNodeIdentifier
    producer: str
    protoDefName: str
    protoDefPath: str
    required: bool

@typing.type_check_only
class EnterpriseCrmFrontendsEventbusProtoWorkflowParameters(
    typing.TypedDict, total=False
):
    parameters: _list[EnterpriseCrmFrontendsEventbusProtoWorkflowParameterEntry]

@typing.type_check_only
class GoogleCloudConnectorsV1AuthConfig(typing.TypedDict, total=False):
    additionalVariables: _list[GoogleCloudConnectorsV1ConfigVariable]
    authKey: str
    authType: typing.Literal[
        "AUTH_TYPE_UNSPECIFIED",
        "USER_PASSWORD",
        "OAUTH2_JWT_BEARER",
        "OAUTH2_CLIENT_CREDENTIALS",
        "SSH_PUBLIC_KEY",
        "OAUTH2_AUTH_CODE_FLOW",
        "GOOGLE_AUTHENTICATION",
        "OAUTH2_AUTH_CODE_FLOW_GOOGLE_MANAGED",
    ]
    oauth2AuthCodeFlow: GoogleCloudConnectorsV1AuthConfigOauth2AuthCodeFlow
    oauth2AuthCodeFlowGoogleManaged: (
        GoogleCloudConnectorsV1AuthConfigOauth2AuthCodeFlowGoogleManaged
    )
    oauth2ClientCredentials: GoogleCloudConnectorsV1AuthConfigOauth2ClientCredentials
    oauth2JwtBearer: GoogleCloudConnectorsV1AuthConfigOauth2JwtBearer
    sshPublicKey: GoogleCloudConnectorsV1AuthConfigSshPublicKey
    userPassword: GoogleCloudConnectorsV1AuthConfigUserPassword

@typing.type_check_only
class GoogleCloudConnectorsV1AuthConfigOauth2AuthCodeFlow(
    typing.TypedDict, total=False
):
    authCode: str
    authUri: str
    clientId: str
    clientSecret: GoogleCloudConnectorsV1Secret
    enablePkce: bool
    pkceVerifier: str
    redirectUri: str
    scopes: _list[str]

@typing.type_check_only
class GoogleCloudConnectorsV1AuthConfigOauth2AuthCodeFlowGoogleManaged(
    typing.TypedDict, total=False
):
    authCode: str
    redirectUri: str
    scopes: _list[str]

@typing.type_check_only
class GoogleCloudConnectorsV1AuthConfigOauth2ClientCredentials(
    typing.TypedDict, total=False
):
    clientId: str
    clientSecret: GoogleCloudConnectorsV1Secret

@typing.type_check_only
class GoogleCloudConnectorsV1AuthConfigOauth2JwtBearer(typing.TypedDict, total=False):
    clientKey: GoogleCloudConnectorsV1Secret
    jwtClaims: GoogleCloudConnectorsV1AuthConfigOauth2JwtBearerJwtClaims

@typing.type_check_only
class GoogleCloudConnectorsV1AuthConfigOauth2JwtBearerJwtClaims(
    typing.TypedDict, total=False
):
    audience: str
    issuer: str
    subject: str

@typing.type_check_only
class GoogleCloudConnectorsV1AuthConfigSshPublicKey(typing.TypedDict, total=False):
    certType: str
    sshClientCert: GoogleCloudConnectorsV1Secret
    sshClientCertPass: GoogleCloudConnectorsV1Secret
    username: str

@typing.type_check_only
class GoogleCloudConnectorsV1AuthConfigUserPassword(typing.TypedDict, total=False):
    password: GoogleCloudConnectorsV1Secret
    username: str

@typing.type_check_only
class GoogleCloudConnectorsV1BillingConfig(typing.TypedDict, total=False):
    billingCategory: typing.Literal[
        "BILLING_CATEGORY_UNSPECIFIED",
        "GCP_AND_TECHNICAL_CONNECTOR",
        "NON_GCP_CONNECTOR",
    ]

@typing.type_check_only
class GoogleCloudConnectorsV1ConfigVariable(typing.TypedDict, total=False):
    boolValue: bool
    encryptionKeyValue: GoogleCloudConnectorsV1EncryptionKey
    intValue: str
    key: str
    secretValue: GoogleCloudConnectorsV1Secret
    stringValue: str

@typing.type_check_only
class GoogleCloudConnectorsV1Connection(typing.TypedDict, total=False):
    asyncOperationsEnabled: bool
    authConfig: GoogleCloudConnectorsV1AuthConfig
    authOverrideEnabled: bool
    billingConfig: GoogleCloudConnectorsV1BillingConfig
    configVariables: _list[GoogleCloudConnectorsV1ConfigVariable]
    connectionRevision: str
    connectorVersion: str
    connectorVersionInfraConfig: GoogleCloudConnectorsV1ConnectorVersionInfraConfig
    connectorVersionLaunchStage: typing.Literal[
        "LAUNCH_STAGE_UNSPECIFIED",
        "PREVIEW",
        "GA",
        "DEPRECATED",
        "TEST",
        "PRIVATE_PREVIEW",
    ]
    createTime: str
    description: str
    destinationConfigs: _list[GoogleCloudConnectorsV1DestinationConfig]
    envoyImageLocation: str
    euaOauthAuthConfig: GoogleCloudConnectorsV1AuthConfig
    eventingConfig: GoogleCloudConnectorsV1EventingConfig
    eventingEnablementType: typing.Literal[
        "EVENTING_ENABLEMENT_TYPE_UNSPECIFIED",
        "EVENTING_AND_CONNECTION",
        "ONLY_EVENTING",
    ]
    eventingRuntimeData: GoogleCloudConnectorsV1EventingRuntimeData
    fallbackOnAdminCredentials: bool
    host: str
    imageLocation: str
    isTrustedTester: bool
    labels: dict[str, typing.Any]
    lockConfig: GoogleCloudConnectorsV1LockConfig
    logConfig: GoogleCloudConnectorsV1LogConfig
    name: str
    nodeConfig: GoogleCloudConnectorsV1NodeConfig
    serviceAccount: str
    serviceDirectory: str
    sslConfig: GoogleCloudConnectorsV1SslConfig
    status: GoogleCloudConnectorsV1ConnectionStatus
    subscriptionType: typing.Literal["SUBSCRIPTION_TYPE_UNSPECIFIED", "PAY_G", "PAID"]
    suspended: bool
    tlsServiceDirectory: str
    trafficShapingConfigs: _list[GoogleCloudConnectorsV1TrafficShapingConfig]
    updateTime: str

@typing.type_check_only
class GoogleCloudConnectorsV1ConnectionStatus(typing.TypedDict, total=False):
    description: str
    state: typing.Literal[
        "STATE_UNSPECIFIED",
        "CREATING",
        "ACTIVE",
        "INACTIVE",
        "DELETING",
        "UPDATING",
        "ERROR",
        "AUTHORIZATION_REQUIRED",
    ]
    status: str

@typing.type_check_only
class GoogleCloudConnectorsV1ConnectorVersionInfraConfig(typing.TypedDict, total=False):
    connectionRatelimitWindowSeconds: str
    deploymentModel: typing.Literal[
        "DEPLOYMENT_MODEL_UNSPECIFIED", "GKE_MST", "CLOUD_RUN_MST"
    ]
    deploymentModelMigrationState: typing.Literal[
        "DEPLOYMENT_MODEL_MIGRATION_STATE_UNSPECIFIED",
        "IN_PROGRESS",
        "COMPLETED",
        "ROLLEDBACK",
        "ROLLBACK_IN_PROGRESS",
    ]
    hpaConfig: GoogleCloudConnectorsV1HPAConfig
    internalclientRatelimitThreshold: str
    maxInstanceRequestConcurrency: int
    ratelimitThreshold: str
    resourceLimits: GoogleCloudConnectorsV1ResourceLimits
    resourceRequests: GoogleCloudConnectorsV1ResourceRequests
    sharedDeployment: str
    tlsMigrationState: typing.Literal[
        "TLS_MIGRATION_STATE_UNSPECIFIED",
        "TLS_MIGRATION_NOT_STARTED",
        "TLS_MIGRATION_COMPLETED",
    ]

@typing.type_check_only
class GoogleCloudConnectorsV1Destination(typing.TypedDict, total=False):
    host: str
    port: int
    serviceAttachment: str

@typing.type_check_only
class GoogleCloudConnectorsV1DestinationConfig(typing.TypedDict, total=False):
    destinations: _list[GoogleCloudConnectorsV1Destination]
    key: str

@typing.type_check_only
class GoogleCloudConnectorsV1EncryptionKey(typing.TypedDict, total=False):
    kmsKeyName: str
    type: typing.Literal["TYPE_UNSPECIFIED", "GOOGLE_MANAGED", "CUSTOMER_MANAGED"]

@typing.type_check_only
class GoogleCloudConnectorsV1EnrichmentConfig(typing.TypedDict, total=False):
    appendAcl: bool

@typing.type_check_only
class GoogleCloudConnectorsV1EventingConfig(typing.TypedDict, total=False):
    additionalVariables: _list[GoogleCloudConnectorsV1ConfigVariable]
    allowedEventTypes: _list[str]
    authConfig: GoogleCloudConnectorsV1AuthConfig
    deadLetterConfig: GoogleCloudConnectorsV1EventingConfigDeadLetterConfig
    enrichmentConfig: GoogleCloudConnectorsV1EnrichmentConfig
    enrichmentEnabled: bool
    eventsListenerIngressEndpoint: str
    listenerAuthConfig: GoogleCloudConnectorsV1AuthConfig
    privateConnectivityAllowlistedProjects: _list[str]
    privateConnectivityEnabled: bool
    proxyDestinationConfig: GoogleCloudConnectorsV1DestinationConfig
    registrationDestinationConfig: GoogleCloudConnectorsV1DestinationConfig
    sslConfig: GoogleCloudConnectorsV1SslConfig

@typing.type_check_only
class GoogleCloudConnectorsV1EventingConfigDeadLetterConfig(
    typing.TypedDict, total=False
):
    projectId: str
    topic: str

@typing.type_check_only
class GoogleCloudConnectorsV1EventingRuntimeData(typing.TypedDict, total=False):
    eventsListenerEndpoint: str
    eventsListenerPscSa: str
    status: GoogleCloudConnectorsV1EventingStatus
    webhookData: GoogleCloudConnectorsV1EventingRuntimeDataWebhookData
    webhookSubscriptions: GoogleCloudConnectorsV1EventingRuntimeDataWebhookSubscriptions

@typing.type_check_only
class GoogleCloudConnectorsV1EventingRuntimeDataWebhookData(
    typing.TypedDict, total=False
):
    additionalVariables: _list[GoogleCloudConnectorsV1ConfigVariable]
    createTime: str
    id: str
    name: str
    nextRefreshTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudConnectorsV1EventingRuntimeDataWebhookSubscriptions(
    typing.TypedDict, total=False
):
    webhookData: _list[GoogleCloudConnectorsV1EventingRuntimeDataWebhookData]

@typing.type_check_only
class GoogleCloudConnectorsV1EventingStatus(typing.TypedDict, total=False):
    description: str
    state: typing.Literal[
        "STATE_UNSPECIFIED", "ACTIVE", "ERROR", "INGRESS_ENDPOINT_REQUIRED"
    ]

@typing.type_check_only
class GoogleCloudConnectorsV1HPAConfig(typing.TypedDict, total=False):
    cpuUtilizationThreshold: str
    memoryUtilizationThreshold: str

@typing.type_check_only
class GoogleCloudConnectorsV1LockConfig(typing.TypedDict, total=False):
    locked: bool
    reason: str

@typing.type_check_only
class GoogleCloudConnectorsV1LogConfig(typing.TypedDict, total=False):
    enabled: bool
    level: typing.Literal["LOG_LEVEL_UNSPECIFIED", "ERROR", "INFO", "DEBUG"]

@typing.type_check_only
class GoogleCloudConnectorsV1NodeConfig(typing.TypedDict, total=False):
    maxNodeCount: int
    minNodeCount: int

@typing.type_check_only
class GoogleCloudConnectorsV1ResourceLimits(typing.TypedDict, total=False):
    cpu: str
    memory: str

@typing.type_check_only
class GoogleCloudConnectorsV1ResourceRequests(typing.TypedDict, total=False):
    cpu: str
    memory: str

@typing.type_check_only
class GoogleCloudConnectorsV1Secret(typing.TypedDict, total=False):
    secretVersion: str

@typing.type_check_only
class GoogleCloudConnectorsV1SslConfig(typing.TypedDict, total=False):
    additionalVariables: _list[GoogleCloudConnectorsV1ConfigVariable]
    clientCertType: typing.Literal["CERT_TYPE_UNSPECIFIED", "PEM"]
    clientCertificate: GoogleCloudConnectorsV1Secret
    clientPrivateKey: GoogleCloudConnectorsV1Secret
    clientPrivateKeyPass: GoogleCloudConnectorsV1Secret
    privateServerCertificate: GoogleCloudConnectorsV1Secret
    serverCertType: typing.Literal["CERT_TYPE_UNSPECIFIED", "PEM"]
    trustModel: typing.Literal["PUBLIC", "PRIVATE", "INSECURE"]
    type: typing.Literal["SSL_TYPE_UNSPECIFIED", "TLS", "MTLS"]
    useSsl: bool

@typing.type_check_only
class GoogleCloudConnectorsV1TrafficShapingConfig(typing.TypedDict, total=False):
    duration: str
    quotaLimit: str

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaAccessToken(typing.TypedDict, total=False):
    accessToken: str
    accessTokenExpireTime: str
    refreshToken: str
    refreshTokenExpireTime: str
    tokenType: str

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaApiTriggerResource(typing.TypedDict, total=False):
    integrationResource: str
    triggerId: _list[str]

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaAssertion(typing.TypedDict, total=False):
    assertionStrategy: typing.Literal[
        "ASSERTION_STRATEGY_UNSPECIFIED",
        "ASSERT_SUCCESSFUL_EXECUTION",
        "ASSERT_FAILED_EXECUTION",
        "ASSERT_NO_EXECUTION",
        "ASSERT_EQUALS",
        "ASSERT_NOT_EQUALS",
        "ASSERT_CONTAINS",
        "ASSERT_CONDITION",
    ]
    condition: str
    parameter: GoogleCloudIntegrationsV1alphaEventParameter
    retryCount: int

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaAssertionResult(typing.TypedDict, total=False):
    assertion: GoogleCloudIntegrationsV1alphaAssertion
    failureMessage: str
    status: typing.Literal["ASSERTION_STATUS_UNSPECIFIED", "SUCCEEDED", "FAILED"]
    taskName: str
    taskNumber: str

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaAttemptStats(typing.TypedDict, total=False):
    endTime: str
    startTime: str

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaAuthConfig(typing.TypedDict, total=False):
    certificateId: str
    createTime: str
    creatorEmail: str
    credentialType: typing.Literal[
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
    state: typing.Literal[
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
    visibility: typing.Literal[
        "AUTH_CONFIG_VISIBILITY_UNSPECIFIED", "PRIVATE", "CLIENT_VISIBLE"
    ]

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaAuthToken(typing.TypedDict, total=False):
    token: str
    type: str

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaBooleanParameterArray(
    typing.TypedDict, total=False
):
    booleanValues: _list[bool]

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaCancelExecutionRequest(
    typing.TypedDict, total=False
):
    cancelReason: str

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaCancelExecutionResponse(
    typing.TypedDict, total=False
):
    isCanceled: bool

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaCertificate(typing.TypedDict, total=False):
    certificateStatus: typing.Literal["STATE_UNSPECIFIED", "ACTIVE", "EXPIRED"]
    credentialId: str
    description: str
    displayName: str
    name: str
    rawCertificate: GoogleCloudIntegrationsV1alphaClientCertificate
    requestorId: str
    validEndTime: str
    validStartTime: str

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaChangeCustomerConfigRequest(
    typing.TypedDict, total=False
):
    customerConfig: GoogleCloudIntegrationsV1alphaCustomerConfig
    updateMask: str

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaChangeCustomerConfigResponse(
    typing.TypedDict, total=False
):
    customerConfig: GoogleCloudIntegrationsV1alphaCustomerConfig

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaClientCertificate(typing.TypedDict, total=False):
    encryptedPrivateKey: str
    passphrase: str
    sslCertificate: str

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaClientConfig(typing.TypedDict, total=False):
    billingType: typing.Literal[
        "BILLING_TYPE_UNSPECIFIED",
        "BILLING_TYPE_APIGEE_TRIALS",
        "BILLING_TYPE_APIGEE_SUBSCRIPTION",
        "BILLING_TYPE_PAYG",
    ]
    clientState: typing.Literal[
        "CLIENT_STATE_UNSPECIFIED", "CLIENT_STATE_ACTIVE", "CLIENT_STATE_DISABLED"
    ]
    cloudKmsConfig: GoogleCloudIntegrationsV1alphaCloudKmsConfig
    createTime: str
    customerConfig: GoogleCloudIntegrationsV1alphaCustomerConfig
    description: str
    enableHttpCall: bool
    enableInternalIp: bool
    enableManagedAiFeatures: bool
    enableVariableMasking: bool
    id: str
    isGmek: bool
    p4ServiceAccount: str
    projectId: str
    region: str
    runAsServiceAccount: str

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaCloudKmsConfig(typing.TypedDict, total=False):
    key: str
    keyVersion: str
    kmsLocation: str
    kmsProjectId: str
    kmsRing: str

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaCloudLoggingDetails(typing.TypedDict, total=False):
    cloudLoggingSeverity: typing.Literal[
        "CLOUD_LOGGING_SEVERITY_UNSPECIFIED", "INFO", "ERROR", "WARNING"
    ]
    enableCloudLogging: bool

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaCloudSchedulerConfig(typing.TypedDict, total=False):
    cronTab: str
    errorMessage: str
    location: str
    serviceAccountEmail: str

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaConditionalFailurePolicies(
    typing.TypedDict, total=False
):
    defaultFailurePolicy: GoogleCloudIntegrationsV1alphaFailurePolicy
    failurePolicies: _list[GoogleCloudIntegrationsV1alphaFailurePolicy]

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaConnectionSchemaMetadata(
    typing.TypedDict, total=False
):
    actions: _list[str]
    entities: _list[str]

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaCoordinate(typing.TypedDict, total=False):
    x: int
    y: int

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaCreateAppsScriptProjectRequest(
    typing.TypedDict, total=False
):
    appsScriptProject: str
    authConfigId: str

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaCreateAppsScriptProjectResponse(
    typing.TypedDict, total=False
):
    projectId: str

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaCreateCloudFunctionRequest(
    typing.TypedDict, total=False
):
    functionName: str
    functionRegion: str
    gcfApiVersion: typing.Literal[
        "GCF_API_VERSION_UNSPECIFIED", "API_VERSION_V1", "API_VERSION_V2"
    ]
    projectId: str

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaCreateCloudFunctionResponse(
    typing.TypedDict, total=False
):
    triggerUrl: str

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaCredential(typing.TypedDict, total=False):
    authToken: GoogleCloudIntegrationsV1alphaAuthToken
    credentialType: typing.Literal[
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
    oauth2ResourceOwnerCredentials: (
        GoogleCloudIntegrationsV1alphaOAuth2ResourceOwnerCredentials
    )
    oidcToken: GoogleCloudIntegrationsV1alphaOidcToken
    serviceAccountCredentials: GoogleCloudIntegrationsV1alphaServiceAccountCredentials
    usernameAndPassword: GoogleCloudIntegrationsV1alphaUsernameAndPassword

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaCustomerConfig(typing.TypedDict, total=False):
    cloudKmsConfig: GoogleCloudIntegrationsV1alphaCloudKmsConfig
    enableHttpCall: bool
    enableManagedAiFeatures: bool
    enableVariableMasking: bool
    runAsServiceAccount: str

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaDeprovisionClientRequest(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaDoubleParameterArray(typing.TypedDict, total=False):
    doubleValues: _list[float]

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaDownloadExecutionResponse(
    typing.TypedDict, total=False
):
    content: str

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaDownloadIntegrationVersionResponse(
    typing.TypedDict, total=False
):
    content: str
    files: _list[GoogleCloudIntegrationsV1alphaSerializedFile]

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaDownloadJsonPackageResponse(
    typing.TypedDict, total=False
):
    files: _list[GoogleCloudIntegrationsV1alphaFile]

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaDownloadTemplateResponse(
    typing.TypedDict, total=False
):
    content: str

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaDownloadTestCaseResponse(
    typing.TypedDict, total=False
):
    content: str

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaEnumerateConnectorPlatformRegionsResponse(
    typing.TypedDict, total=False
):
    regions: _list[str]

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaErrorCatcherConfig(typing.TypedDict, total=False):
    description: str
    errorCatcherId: str
    errorCatcherNumber: str
    label: str
    position: GoogleCloudIntegrationsV1alphaCoordinate
    startErrorTasks: _list[GoogleCloudIntegrationsV1alphaNextTask]

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaEventParameter(typing.TypedDict, total=False):
    key: str
    masked: bool
    value: GoogleCloudIntegrationsV1alphaValueType

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaExecuteEventResponse(typing.TypedDict, total=False):
    executionId: str

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaExecuteIntegrationsRequest(
    typing.TypedDict, total=False
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
    typing.TypedDict, total=False
):
    eventParameters: EnterpriseCrmFrontendsEventbusProtoEventParameters
    executionFailed: bool
    executionId: str
    outputParameters: dict[str, typing.Any]
    parameterEntries: _list[EnterpriseCrmFrontendsEventbusProtoParameterEntry]
    parameters: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaExecuteTestCaseRequest(
    typing.TypedDict, total=False
):
    inputParameters: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaExecuteTestCaseResponse(
    typing.TypedDict, total=False
):
    assertionResults: _list[GoogleCloudIntegrationsV1alphaAssertionResult]
    executionId: str
    outputParameters: dict[str, typing.Any]
    testExecutionState: typing.Literal["STATE_UNSPECIFIED", "PASSED", "FAILED"]

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaExecuteTestCasesRequest(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaExecuteTestCasesResponse(
    typing.TypedDict, total=False
):
    executeTestCaseResponses: _list[
        GoogleCloudIntegrationsV1alphaExecuteTestCaseResponse
    ]

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaExecution(typing.TypedDict, total=False):
    cloudKmsKey: str
    cloudLoggingDetails: GoogleCloudIntegrationsV1alphaCloudLoggingDetails
    createTime: str
    directSubExecutions: _list[GoogleCloudIntegrationsV1alphaExecution]
    eventExecutionDetails: EnterpriseCrmEventbusProtoEventExecutionDetails
    executionDetails: GoogleCloudIntegrationsV1alphaExecutionDetails
    executionMethod: typing.Literal[
        "EXECUTION_METHOD_UNSPECIFIED", "POST", "POST_TO_QUEUE", "SCHEDULE"
    ]
    integrationVersionState: typing.Literal[
        "INTEGRATION_STATE_UNSPECIFIED", "DRAFT", "ACTIVE", "ARCHIVED", "SNAPSHOT"
    ]
    name: str
    replayInfo: GoogleCloudIntegrationsV1alphaExecutionReplayInfo
    requestParameters: dict[str, typing.Any]
    requestParams: _list[EnterpriseCrmFrontendsEventbusProtoParameterEntry]
    responseParameters: dict[str, typing.Any]
    responseParams: _list[EnterpriseCrmFrontendsEventbusProtoParameterEntry]
    snapshotNumber: str
    triggerId: str
    updateTime: str

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaExecutionDetails(typing.TypedDict, total=False):
    attemptStats: _list[GoogleCloudIntegrationsV1alphaAttemptStats]
    eventExecutionSnapshotsSize: str
    executionSnapshots: _list[GoogleCloudIntegrationsV1alphaExecutionSnapshot]
    state: typing.Literal[
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
class GoogleCloudIntegrationsV1alphaExecutionReplayInfo(typing.TypedDict, total=False):
    originalExecutionInfoId: str
    replayMode: typing.Literal[
        "REPLAY_MODE_UNSPECIFIED",
        "REPLAY_MODE_FROM_BEGINNING",
        "REPLAY_MODE_POINT_OF_FAILURE",
    ]
    replayReason: str
    replayedExecutionInfoIds: _list[str]

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaExecutionSnapshot(typing.TypedDict, total=False):
    checkpointTaskNumber: str
    executionSnapshotMetadata: (
        GoogleCloudIntegrationsV1alphaExecutionSnapshotExecutionSnapshotMetadata
    )
    params: dict[str, typing.Any]
    taskExecutionDetails: _list[GoogleCloudIntegrationsV1alphaTaskExecutionDetails]

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaExecutionSnapshotExecutionSnapshotMetadata(
    typing.TypedDict, total=False
):
    ancestorIterationNumbers: _list[str]
    ancestorTaskNumbers: _list[str]
    executionAttempt: int
    integrationName: str
    task: str
    taskAttempt: int
    taskLabel: str
    taskNumber: str

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaFailurePolicy(typing.TypedDict, total=False):
    condition: str
    intervalTime: str
    maxRetries: int
    retryStrategy: typing.Literal[
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
class GoogleCloudIntegrationsV1alphaFile(typing.TypedDict, total=False):
    integrationConfig: dict[str, typing.Any]
    integrationVersion: GoogleCloudIntegrationsV1alphaIntegrationVersion
    type: typing.Literal[
        "INTEGRATION_FILE_UNSPECIFIED", "INTEGRATION", "INTEGRATION_CONFIG_VARIABLES"
    ]

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaGenerateOpenApiSpecRequest(
    typing.TypedDict, total=False
):
    apiTriggerResources: _list[GoogleCloudIntegrationsV1alphaApiTriggerResource]
    fileFormat: typing.Literal["FILE_FORMAT_UNSPECIFIED", "JSON", "YAML"]

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaGenerateOpenApiSpecResponse(
    typing.TypedDict, total=False
):
    openApiSpec: str

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaGenerateTokenResponse(
    typing.TypedDict, total=False
):
    message: str

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaGetClientMetadataResponse(
    typing.TypedDict, total=False
):
    properties: GoogleCloudIntegrationsV1alphaProjectProperties

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaGetClientResponse(typing.TypedDict, total=False):
    client: GoogleCloudIntegrationsV1alphaClientConfig

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaImportTemplateRequest(
    typing.TypedDict, total=False
):
    integration: str
    subIntegrations: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaImportTemplateResponse(
    typing.TypedDict, total=False
):
    integrationVersion: GoogleCloudIntegrationsV1alphaIntegrationVersion
    subIntegrationVersions: _list[GoogleCloudIntegrationsV1alphaIntegrationVersion]

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaIntParameterArray(typing.TypedDict, total=False):
    intValues: _list[str]

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaIntegration(typing.TypedDict, total=False):
    active: bool
    createTime: str
    creatorEmail: str
    description: str
    lastModifierEmail: str
    name: str
    updateTime: str

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaIntegrationAlertConfig(
    typing.TypedDict, total=False
):
    aggregationPeriod: str
    alertThreshold: int
    disableAlert: bool
    displayName: str
    durationThreshold: str
    metricType: typing.Literal[
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
    thresholdType: typing.Literal[
        "THRESHOLD_TYPE_UNSPECIFIED", "EXPECTED_MIN", "EXPECTED_MAX"
    ]
    thresholdValue: GoogleCloudIntegrationsV1alphaIntegrationAlertConfigThresholdValue

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaIntegrationAlertConfigThresholdValue(
    typing.TypedDict, total=False
):
    absolute: str
    percentage: int

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaIntegrationConfigParameter(
    typing.TypedDict, total=False
):
    parameter: GoogleCloudIntegrationsV1alphaIntegrationParameter
    value: GoogleCloudIntegrationsV1alphaValueType

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaIntegrationParameter(typing.TypedDict, total=False):
    containsLargeData: bool
    dataType: typing.Literal[
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
        "NON_SERIALIZABLE_OBJECT",
        "PROTO_ENUM",
        "SERIALIZED_OBJECT_VALUE",
        "PROTO_ENUM_ARRAY",
        "BYTES",
        "BYTES_ARRAY",
    ]
    defaultValue: GoogleCloudIntegrationsV1alphaValueType
    description: str
    displayName: str
    inputOutputType: typing.Literal["IN_OUT_TYPE_UNSPECIFIED", "IN", "OUT", "IN_OUT"]
    isTransient: bool
    jsonSchema: str
    key: str
    masked: bool
    producer: str
    searchable: bool

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaIntegrationVersion(typing.TypedDict, total=False):
    cloudKmsKey: str
    cloudLoggingDetails: GoogleCloudIntegrationsV1alphaCloudLoggingDetails
    createTime: str
    createdFromTemplate: str
    databasePersistencePolicy: typing.Literal[
        "DATABASE_PERSISTENCE_POLICY_UNSPECIFIED",
        "DATABASE_PERSISTENCE_DISABLED",
        "DATABASE_PERSISTENCE_ASYNC",
    ]
    description: str
    enableVariableMasking: bool
    errorCatcherConfigs: _list[GoogleCloudIntegrationsV1alphaErrorCatcherConfig]
    integrationConfigParameters: _list[
        GoogleCloudIntegrationsV1alphaIntegrationConfigParameter
    ]
    integrationParameters: _list[GoogleCloudIntegrationsV1alphaIntegrationParameter]
    integrationParametersInternal: EnterpriseCrmFrontendsEventbusProtoWorkflowParameters
    lastModifierEmail: str
    lockHolder: str
    name: str
    origin: typing.Literal[
        "UNSPECIFIED",
        "UI",
        "PIPER_V2",
        "PIPER_V3",
        "APPLICATION_IP_PROVISIONING",
        "TEST_CASE",
    ]
    parentTemplateId: str
    runAsServiceAccount: str
    snapshotNumber: str
    state: typing.Literal[
        "INTEGRATION_STATE_UNSPECIFIED", "DRAFT", "ACTIVE", "ARCHIVED", "SNAPSHOT"
    ]
    status: typing.Literal["UNKNOWN", "DRAFT", "ACTIVE", "ARCHIVED", "SNAPSHOT"]
    taskConfigs: _list[GoogleCloudIntegrationsV1alphaTaskConfig]
    taskConfigsInternal: _list[EnterpriseCrmFrontendsEventbusProtoTaskConfig]
    teardown: EnterpriseCrmEventbusProtoTeardown
    triggerConfigs: _list[GoogleCloudIntegrationsV1alphaTriggerConfig]
    triggerConfigsInternal: _list[EnterpriseCrmFrontendsEventbusProtoTriggerConfig]
    updateTime: str
    userLabel: str

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaIntegrationVersionTemplate(
    typing.TypedDict, total=False
):
    integrationVersion: GoogleCloudIntegrationsV1alphaIntegrationVersion
    key: str

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaJwt(typing.TypedDict, total=False):
    jwt: str
    jwtHeader: str
    jwtPayload: str
    secret: str

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaLiftSuspensionRequest(
    typing.TypedDict, total=False
):
    suspensionResult: str

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaLiftSuspensionResponse(
    typing.TypedDict, total=False
):
    eventExecutionInfoId: str

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaLinkAppsScriptProjectRequest(
    typing.TypedDict, total=False
):
    scriptId: str

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaLinkAppsScriptProjectResponse(
    typing.TypedDict, total=False
):
    scriptId: str

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaListAuthConfigsResponse(
    typing.TypedDict, total=False
):
    authConfigs: _list[GoogleCloudIntegrationsV1alphaAuthConfig]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaListCertificatesResponse(
    typing.TypedDict, total=False
):
    certificates: _list[GoogleCloudIntegrationsV1alphaCertificate]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaListConnectionsResponse(
    typing.TypedDict, total=False
):
    connections: _list[GoogleCloudConnectorsV1Connection]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaListExecutionsResponse(
    typing.TypedDict, total=False
):
    executionInfos: _list[EnterpriseCrmFrontendsEventbusProtoEventExecutionInfo]
    executions: _list[GoogleCloudIntegrationsV1alphaExecution]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaListIntegrationVersionsResponse(
    typing.TypedDict, total=False
):
    integrationVersions: _list[GoogleCloudIntegrationsV1alphaIntegrationVersion]
    nextPageToken: str
    noPermission: bool

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaListIntegrationsResponse(
    typing.TypedDict, total=False
):
    integrations: _list[GoogleCloudIntegrationsV1alphaIntegration]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaListRuntimeActionSchemasResponse(
    typing.TypedDict, total=False
):
    nextPageToken: str
    runtimeActionSchemas: _list[GoogleCloudIntegrationsV1alphaRuntimeActionSchema]

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaListRuntimeEntitySchemasResponse(
    typing.TypedDict, total=False
):
    nextPageToken: str
    runtimeEntitySchemas: _list[GoogleCloudIntegrationsV1alphaRuntimeEntitySchema]

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaListSfdcChannelsResponse(
    typing.TypedDict, total=False
):
    nextPageToken: str
    sfdcChannels: _list[GoogleCloudIntegrationsV1alphaSfdcChannel]

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaListSfdcInstancesResponse(
    typing.TypedDict, total=False
):
    nextPageToken: str
    sfdcInstances: _list[GoogleCloudIntegrationsV1alphaSfdcInstance]

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaListSuspensionsResponse(
    typing.TypedDict, total=False
):
    nextPageToken: str
    suspensions: _list[GoogleCloudIntegrationsV1alphaSuspension]

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaListTemplatesResponse(
    typing.TypedDict, total=False
):
    nextPageToken: str
    templates: _list[GoogleCloudIntegrationsV1alphaTemplate]

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaListTestCasesResponse(
    typing.TypedDict, total=False
):
    nextPageToken: str
    testCases: _list[GoogleCloudIntegrationsV1alphaTestCase]

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaMockConfig(typing.TypedDict, total=False):
    failedExecutions: str
    mockStrategy: typing.Literal[
        "MOCK_STRATEGY_UNSPECIFIED",
        "NO_MOCK_STRATEGY",
        "SPECIFIC_MOCK_STRATEGY",
        "FAILURE_MOCK_STRATEGY",
        "SKIP_MOCK_STRATEGY",
    ]
    parameters: _list[GoogleCloudIntegrationsV1alphaEventParameter]

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaNextTask(typing.TypedDict, total=False):
    condition: str
    description: str
    displayName: str
    taskConfigId: str
    taskId: str

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaOAuth2AuthorizationCode(
    typing.TypedDict, total=False
):
    accessToken: GoogleCloudIntegrationsV1alphaAccessToken
    applyReauthPolicy: bool
    authCode: str
    authEndpoint: str
    authParams: GoogleCloudIntegrationsV1alphaParameterMap
    clientId: str
    clientSecret: str
    requestType: typing.Literal[
        "REQUEST_TYPE_UNSPECIFIED", "REQUEST_BODY", "QUERY_PARAMETERS", "ENCODED_HEADER"
    ]
    scope: str
    tokenEndpoint: str
    tokenParams: GoogleCloudIntegrationsV1alphaParameterMap

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaOAuth2ClientCredentials(
    typing.TypedDict, total=False
):
    accessToken: GoogleCloudIntegrationsV1alphaAccessToken
    clientId: str
    clientSecret: str
    requestType: typing.Literal[
        "REQUEST_TYPE_UNSPECIFIED", "REQUEST_BODY", "QUERY_PARAMETERS", "ENCODED_HEADER"
    ]
    scope: str
    tokenEndpoint: str
    tokenParams: GoogleCloudIntegrationsV1alphaParameterMap

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaOAuth2ResourceOwnerCredentials(
    typing.TypedDict, total=False
):
    accessToken: GoogleCloudIntegrationsV1alphaAccessToken
    clientId: str
    clientSecret: str
    password: str
    requestType: typing.Literal[
        "REQUEST_TYPE_UNSPECIFIED", "REQUEST_BODY", "QUERY_PARAMETERS", "ENCODED_HEADER"
    ]
    scope: str
    tokenEndpoint: str
    tokenParams: GoogleCloudIntegrationsV1alphaParameterMap
    username: str

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaOidcToken(typing.TypedDict, total=False):
    audience: str
    serviceAccountEmail: str
    token: str
    tokenExpireTime: str

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaParameterMap(typing.TypedDict, total=False):
    entries: _list[GoogleCloudIntegrationsV1alphaParameterMapEntry]
    keyType: typing.Literal[
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
        "NON_SERIALIZABLE_OBJECT",
        "PROTO_ENUM",
        "SERIALIZED_OBJECT_VALUE",
        "PROTO_ENUM_ARRAY",
        "BYTES",
        "BYTES_ARRAY",
    ]
    valueType: typing.Literal[
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
        "NON_SERIALIZABLE_OBJECT",
        "PROTO_ENUM",
        "SERIALIZED_OBJECT_VALUE",
        "PROTO_ENUM_ARRAY",
        "BYTES",
        "BYTES_ARRAY",
    ]

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaParameterMapEntry(typing.TypedDict, total=False):
    key: GoogleCloudIntegrationsV1alphaParameterMapField
    value: GoogleCloudIntegrationsV1alphaParameterMapField

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaParameterMapField(typing.TypedDict, total=False):
    literalValue: GoogleCloudIntegrationsV1alphaValueType
    referenceKey: str

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaProjectProperties(typing.TypedDict, total=False):
    billingType: typing.Literal[
        "BILLING_TYPE_UNSPECIFIED",
        "APIGEE_TRIALS",
        "APIGEE_SUBSCRIPTION",
        "PAYG",
        "SUBSCRIPTION",
        "NO_BILLING",
    ]
    ipEnablementState: typing.Literal[
        "IP_ENABLEMENT_STATE_UNSPECIFIED",
        "IP_ENABLEMENT_STATE_STANDALONE",
        "IP_ENABLEMENT_STATE_APIGEE",
        "IP_ENABLEMENT_STATE_APIGEE_ENTITLED",
    ]
    provisionedRegions: _list[str]

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaProvisionClientPostProcessorRequest(
    typing.TypedDict, total=False
):
    workflows: _list[
        typing.Literal[
            "SAMPLE_INTEGRATIONS_UNSPECIFIED",
            "SAMPLE_WORKFLOW_ECOM_PROCESSING",
            "EXECUTE_CONNECTOR_TOOL_WORKFLOW",
        ]
    ]

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaProvisionClientPostProcessorResponse(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaProvisionClientRequest(
    typing.TypedDict, total=False
):
    cloudKmsConfig: GoogleCloudIntegrationsV1alphaCloudKmsConfig
    createSampleWorkflows: bool
    enableHttpCall: bool
    enableManagedAiFeatures: bool
    provisionGmek: bool
    runAsServiceAccount: str
    skipCpProvision: bool

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaPublishIntegrationVersionRequest(
    typing.TypedDict, total=False
):
    configParameters: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaPublishIntegrationVersionResponse(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaReplaceServiceAccountRequest(
    typing.TypedDict, total=False
):
    runAsServiceAccount: str

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaReplayExecutionRequest(
    typing.TypedDict, total=False
):
    modifiedParameters: dict[str, typing.Any]
    replayMode: typing.Literal[
        "REPLAY_MODE_UNSPECIFIED",
        "REPLAY_MODE_FROM_BEGINNING",
        "REPLAY_MODE_POINT_OF_FAILURE",
    ]
    replayReason: str
    updateMask: str

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaReplayExecutionResponse(
    typing.TypedDict, total=False
):
    executionId: str
    outputParameters: dict[str, typing.Any]
    replayedExecutionId: str

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaResolveSuspensionRequest(
    typing.TypedDict, total=False
):
    suspension: GoogleCloudIntegrationsV1alphaSuspension

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaResolveSuspensionResponse(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaRuntimeActionSchema(typing.TypedDict, total=False):
    action: str
    inputSchema: str
    outputSchema: str

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaRuntimeEntitySchema(typing.TypedDict, total=False):
    arrayFieldSchema: str
    entity: str
    fieldSchema: str

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaScheduleIntegrationsRequest(
    typing.TypedDict, total=False
):
    inputParameters: dict[str, typing.Any]
    parameterEntries: _list[EnterpriseCrmFrontendsEventbusProtoParameterEntry]
    parameters: EnterpriseCrmEventbusProtoEventParameters
    requestId: str
    scheduleTime: str
    triggerId: str
    userGeneratedExecutionId: str

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaScheduleIntegrationsResponse(
    typing.TypedDict, total=False
):
    executionInfoIds: _list[str]

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaSearchIntegrationsResponse(
    typing.TypedDict, total=False
):
    integrations: _list[
        GoogleCloudIntegrationsV1alphaSearchIntegrationsResponseIntegrationSearchResult
    ]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaSearchIntegrationsResponseIntegrationSearchResult(
    typing.TypedDict, total=False
):
    createTime: str
    creator: str
    description: str
    id: str
    name: str
    region: str
    status: typing.Literal[
        "INTEGRATION_STATE_UNSPECIFIED", "DRAFT", "ACTIVE", "ARCHIVED", "SNAPSHOT"
    ]
    version: str

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaSearchTemplatesResponse(
    typing.TypedDict, total=False
):
    nextPageToken: str
    templates: _list[GoogleCloudIntegrationsV1alphaTemplate]

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaSerializedFile(typing.TypedDict, total=False):
    content: str
    file: typing.Literal[
        "INTEGRATION_FILE_UNSPECIFIED", "INTEGRATION", "INTEGRATION_CONFIG_VARIABLES"
    ]

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaServiceAccountCredentials(
    typing.TypedDict, total=False
):
    scope: str
    serviceAccount: str

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaSfdcChannel(typing.TypedDict, total=False):
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
class GoogleCloudIntegrationsV1alphaSfdcInstance(typing.TypedDict, total=False):
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
class GoogleCloudIntegrationsV1alphaShareTemplateRequest(typing.TypedDict, total=False):
    resourceNames: _list[str]

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaStringParameterArray(typing.TypedDict, total=False):
    stringValues: _list[str]

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaSuccessPolicy(typing.TypedDict, total=False):
    finalState: typing.Literal["FINAL_STATE_UNSPECIFIED", "SUCCEEDED", "SUSPENDED"]

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaSuspension(typing.TypedDict, total=False):
    approvalConfig: GoogleCloudIntegrationsV1alphaSuspensionApprovalConfig
    audit: GoogleCloudIntegrationsV1alphaSuspensionAudit
    createTime: str
    eventExecutionInfoId: str
    integration: str
    lastModifyTime: str
    name: str
    state: typing.Literal[
        "RESOLUTION_STATE_UNSPECIFIED", "PENDING", "REJECTED", "LIFTED"
    ]
    suspensionConfig: EnterpriseCrmEventbusProtoSuspensionConfig
    taskId: str

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaSuspensionApprovalConfig(
    typing.TypedDict, total=False
):
    customMessage: str
    emailAddresses: _list[str]
    expiration: GoogleCloudIntegrationsV1alphaSuspensionApprovalExpiration

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaSuspensionApprovalExpiration(
    typing.TypedDict, total=False
):
    expireTime: str
    liftWhenExpired: bool
    remindTime: str

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaSuspensionAudit(typing.TypedDict, total=False):
    resolveTime: str
    resolver: str

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaSwitchEncryptionRequest(
    typing.TypedDict, total=False
):
    cloudKmsConfig: GoogleCloudIntegrationsV1alphaCloudKmsConfig

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaSwitchVariableMaskingRequest(
    typing.TypedDict, total=False
):
    enableVariableMasking: bool

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaTakeoverEditLockRequest(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaTakeoverEditLockResponse(
    typing.TypedDict, total=False
):
    integrationVersion: GoogleCloudIntegrationsV1alphaIntegrationVersion

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaTakeoverTestCaseEditLockRequest(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaTaskConfig(typing.TypedDict, total=False):
    conditionalFailurePolicies: GoogleCloudIntegrationsV1alphaConditionalFailurePolicies
    description: str
    displayName: str
    errorCatcherId: str
    externalTaskType: typing.Literal[
        "EXTERNAL_TASK_TYPE_UNSPECIFIED", "NORMAL_TASK", "ERROR_TASK"
    ]
    failurePolicy: GoogleCloudIntegrationsV1alphaFailurePolicy
    jsonValidationOption: typing.Literal[
        "JSON_VALIDATION_OPTION_UNSPECIFIED",
        "SKIP",
        "PRE_EXECUTION",
        "POST_EXECUTION",
        "PRE_POST_EXECUTION",
    ]
    nextTasks: _list[GoogleCloudIntegrationsV1alphaNextTask]
    nextTasksExecutionPolicy: typing.Literal[
        "NEXT_TASKS_EXECUTION_POLICY_UNSPECIFIED", "RUN_ALL_MATCH", "RUN_FIRST_MATCH"
    ]
    parameters: dict[str, typing.Any]
    position: GoogleCloudIntegrationsV1alphaCoordinate
    successPolicy: GoogleCloudIntegrationsV1alphaSuccessPolicy
    synchronousCallFailurePolicy: GoogleCloudIntegrationsV1alphaFailurePolicy
    task: str
    taskExecutionStrategy: typing.Literal[
        "TASK_EXECUTION_STRATEGY_UNSPECIFIED",
        "WHEN_ALL_SUCCEED",
        "WHEN_ANY_SUCCEED",
        "WHEN_ALL_TASKS_AND_CONDITIONS_SUCCEED",
    ]
    taskId: str
    taskTemplate: str

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaTaskExecutionDetails(typing.TypedDict, total=False):
    taskAttemptStats: _list[GoogleCloudIntegrationsV1alphaAttemptStats]
    taskExecutionState: typing.Literal[
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
class GoogleCloudIntegrationsV1alphaTemplate(typing.TypedDict, total=False):
    author: str
    categories: _list[
        typing.Literal[
            "CATEGORY_UNSPECIFIED",
            "AI_MACHINE_LEARNING",
            "BUSINESS_INTELLIGENCE",
            "COLLABORATION",
            "CUSTOMER_SERVICE",
            "DATABASES",
            "DEVOPS_IT",
            "CONTENT_AND_FILES",
            "FINANCE_AND_ACCOUNTING",
            "HUMAN_RESOURCES",
            "OPERATIONS",
            "PRODUCT_PROJECT_MANAGEMENT",
            "PRODUCTIVITY",
            "SALES_AND_MARKETING",
            "UNIVERSAL_CONNECTORS",
            "UTILITY",
            "OTHERS",
        ]
    ]
    components: _list[GoogleCloudIntegrationsV1alphaTemplateComponent]
    createTime: str
    description: str
    displayName: str
    docLink: str
    lastUsedTime: str
    name: str
    sharedWith: _list[str]
    tags: _list[str]
    templateBundle: GoogleCloudIntegrationsV1alphaTemplateBundle
    updateTime: str
    usageCount: str
    usageInfo: str
    visibility: typing.Literal["VISIBILITY_UNSPECIFIED", "PRIVATE", "SHARED", "PUBLIC"]

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaTemplateBundle(typing.TypedDict, total=False):
    integrationVersionTemplate: GoogleCloudIntegrationsV1alphaIntegrationVersionTemplate
    subIntegrationVersionTemplates: _list[
        GoogleCloudIntegrationsV1alphaIntegrationVersionTemplate
    ]

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaTemplateComponent(typing.TypedDict, total=False):
    name: str
    type: typing.Literal["TYPE_UNSPECIFIED", "TRIGGER", "TASK", "CONNECTOR"]

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaTestCase(typing.TypedDict, total=False):
    createTime: str
    creatorEmail: str
    databasePersistencePolicy: typing.Literal[
        "DATABASE_PERSISTENCE_POLICY_UNSPECIFIED",
        "DATABASE_PERSISTENCE_DISABLED",
        "DATABASE_PERSISTENCE_ASYNC",
    ]
    description: str
    displayName: str
    lastModifierEmail: str
    lockHolderEmail: str
    name: str
    testInputParameters: _list[GoogleCloudIntegrationsV1alphaIntegrationParameter]
    testTaskConfigs: _list[GoogleCloudIntegrationsV1alphaTestTaskConfig]
    triggerConfig: GoogleCloudIntegrationsV1alphaTriggerConfig
    triggerId: str
    updateTime: str

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaTestIntegrationsRequest(
    typing.TypedDict, total=False
):
    clientId: str
    configParameters: dict[str, typing.Any]
    deadlineSecondsTime: str
    inputParameters: dict[str, typing.Any]
    integrationVersion: GoogleCloudIntegrationsV1alphaIntegrationVersion
    parameters: EnterpriseCrmFrontendsEventbusProtoEventParameters
    testMode: bool
    triggerId: str

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaTestIntegrationsResponse(
    typing.TypedDict, total=False
):
    eventParameters: EnterpriseCrmFrontendsEventbusProtoEventParameters
    executionFailed: bool
    executionId: str
    parameterEntries: _list[EnterpriseCrmFrontendsEventbusProtoParameterEntry]
    parameters: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaTestTaskConfig(typing.TypedDict, total=False):
    assertions: _list[GoogleCloudIntegrationsV1alphaAssertion]
    mockConfig: GoogleCloudIntegrationsV1alphaMockConfig
    task: str
    taskConfig: GoogleCloudIntegrationsV1alphaTaskConfig
    taskNumber: str

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaToggleHttpRequest(typing.TypedDict, total=False):
    enableHttpCall: bool

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaTriggerConfig(typing.TypedDict, total=False):
    alertConfig: _list[GoogleCloudIntegrationsV1alphaIntegrationAlertConfig]
    cloudSchedulerConfig: GoogleCloudIntegrationsV1alphaCloudSchedulerConfig
    description: str
    errorCatcherId: str
    inputVariables: GoogleCloudIntegrationsV1alphaTriggerConfigVariables
    label: str
    nextTasksExecutionPolicy: typing.Literal[
        "NEXT_TASKS_EXECUTION_POLICY_UNSPECIFIED", "RUN_ALL_MATCH", "RUN_FIRST_MATCH"
    ]
    outputVariables: GoogleCloudIntegrationsV1alphaTriggerConfigVariables
    position: GoogleCloudIntegrationsV1alphaCoordinate
    properties: dict[str, typing.Any]
    startTasks: _list[GoogleCloudIntegrationsV1alphaNextTask]
    trigger: str
    triggerId: str
    triggerNumber: str
    triggerType: typing.Literal[
        "TRIGGER_TYPE_UNSPECIFIED",
        "CRON",
        "API",
        "SFDC_CHANNEL",
        "CLOUD_PUBSUB_EXTERNAL",
        "SFDC_CDC_CHANNEL",
        "CLOUD_SCHEDULER",
        "INTEGRATION_CONNECTOR_TRIGGER",
        "PRIVATE_TRIGGER",
        "CLOUD_PUBSUB",
        "EVENTARC_TRIGGER",
    ]

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaTriggerConfigVariables(
    typing.TypedDict, total=False
):
    names: _list[str]

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaUnpublishIntegrationVersionRequest(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaUnshareTemplateRequest(
    typing.TypedDict, total=False
):
    resourceNames: _list[str]

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaUploadIntegrationVersionRequest(
    typing.TypedDict, total=False
):
    content: str
    fileFormat: typing.Literal["FILE_FORMAT_UNSPECIFIED", "JSON", "YAML"]

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaUploadIntegrationVersionResponse(
    typing.TypedDict, total=False
):
    integrationVersion: GoogleCloudIntegrationsV1alphaIntegrationVersion

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaUploadTemplateRequest(
    typing.TypedDict, total=False
):
    content: str
    fileFormat: typing.Literal["FILE_FORMAT_UNSPECIFIED", "JSON", "YAML"]

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaUploadTemplateResponse(
    typing.TypedDict, total=False
):
    template: GoogleCloudIntegrationsV1alphaTemplate

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaUploadTestCaseRequest(
    typing.TypedDict, total=False
):
    content: str
    fileFormat: typing.Literal["FILE_FORMAT_UNSPECIFIED", "JSON", "YAML"]

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaUploadTestCaseResponse(
    typing.TypedDict, total=False
):
    testCase: GoogleCloudIntegrationsV1alphaTestCase

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaUseTemplateRequest(typing.TypedDict, total=False):
    integrationDetails: (
        GoogleCloudIntegrationsV1alphaUseTemplateRequestIntegrationDetails
    )
    integrationRegion: str
    subIntegrations: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaUseTemplateRequestIntegrationDetails(
    typing.TypedDict, total=False
):
    integration: str
    integrationDescription: str

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaUseTemplateResponse(typing.TypedDict, total=False):
    integrationVersion: GoogleCloudIntegrationsV1alphaIntegrationVersion
    subIntegrationVersions: _list[GoogleCloudIntegrationsV1alphaIntegrationVersion]

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaUsernameAndPassword(typing.TypedDict, total=False):
    password: str
    username: str

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaValueType(typing.TypedDict, total=False):
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
    typing.TypedDict, total=False
):
    clientId: str
    ignoreErrorIfNoActiveWorkflow: bool
    parameters: EnterpriseCrmEventbusProtoEventParameters
    priority: typing.Literal[
        "UNSPCIFIED", "SHEDDABLE", "SHEDDABLE_PLUS", "CRITICAL", "CRITICAL_PLUS"
    ]
    quotaRetryCount: int
    requestId: str
    resourceName: str
    scheduledTime: str
    testMode: bool
    triggerId: str
    userGeneratedExecutionId: str
    workflowName: str

@typing.type_check_only
class GoogleProtobufEmpty(typing.TypedDict, total=False): ...
