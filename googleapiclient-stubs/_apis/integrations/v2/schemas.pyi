import typing

_list = list

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
class EnterpriseCrmEventbusProtoCustomSuspensionRequest(typing.TypedDict, total=False):
    postToQueueWithTriggerIdRequest: (
        GoogleInternalCloudCrmEventbusV3PostToQueueWithTriggerIdRequest
    )
    suspensionInfoEventParameterKey: str

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
class EnterpriseCrmEventbusProtoNotification(typing.TypedDict, total=False):
    buganizerNotification: EnterpriseCrmEventbusProtoBuganizerNotification
    emailAddress: EnterpriseCrmEventbusProtoAddress
    escalatorQueue: str
    pubsubTopic: str
    request: EnterpriseCrmEventbusProtoCustomSuspensionRequest

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
class EnterpriseCrmEventbusProtoToken(typing.TypedDict, total=False):
    name: str
    value: str

@typing.type_check_only
class EnterpriseCrmEventbusProtoTransformExpression(typing.TypedDict, total=False):
    initialValue: EnterpriseCrmEventbusProtoBaseValue
    transformationFunctions: _list[EnterpriseCrmEventbusProtoFunction]

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
class EnterpriseCrmFrontendsEventbusProtoIntParameterArray(
    typing.TypedDict, total=False
):
    intValues: _list[str]

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
class GoogleApiHttpBody(typing.TypedDict, total=False):
    contentType: str
    data: str
    extensions: _list[dict[str, typing.Any]]

@typing.type_check_only
class GoogleCloudIntegrationsV2AttemptStats(typing.TypedDict, total=False):
    endTime: str
    startTime: str

@typing.type_check_only
class GoogleCloudIntegrationsV2CloudLoggingDetails(typing.TypedDict, total=False):
    cloudLoggingSeverity: typing.Literal[
        "CLOUD_LOGGING_SEVERITY_UNSPECIFIED", "INFO", "ERROR", "WARNING"
    ]
    enableCloudLogging: bool

@typing.type_check_only
class GoogleCloudIntegrationsV2DuetBooleanParameterArray(typing.TypedDict, total=False):
    booleanValues: _list[bool]

@typing.type_check_only
class GoogleCloudIntegrationsV2DuetCloudSchedulerConfig(typing.TypedDict, total=False):
    cronTab: str
    errorMessage: str
    location: str
    serviceAccountEmail: str

@typing.type_check_only
class GoogleCloudIntegrationsV2DuetDoubleParameterArray(typing.TypedDict, total=False):
    doubleValues: _list[float]

@typing.type_check_only
class GoogleCloudIntegrationsV2DuetErrorCatcherConfig(typing.TypedDict, total=False):
    description: str
    errorCatcherId: str
    errorCatcherNumber: str
    label: str
    startErrorTasks: _list[GoogleCloudIntegrationsV2DuetNextTask]

@typing.type_check_only
class GoogleCloudIntegrationsV2DuetEventParameter(typing.TypedDict, total=False):
    key: str
    value: GoogleCloudIntegrationsV2DuetValueType

@typing.type_check_only
class GoogleCloudIntegrationsV2DuetGenerateIntegrationBranchRequest(
    typing.TypedDict, total=False
):
    integrationBranchRequest: GoogleCloudIntegrationsV2DuetIntegrationBranchRequest
    prompt: str

@typing.type_check_only
class GoogleCloudIntegrationsV2DuetGenerateIntegrationBranchResponse(
    typing.TypedDict, total=False
):
    integrationBranch: GoogleCloudIntegrationsV2DuetIntegrationBranch

@typing.type_check_only
class GoogleCloudIntegrationsV2DuetGenerateIntegrationDocumentRequest(
    typing.TypedDict, total=False
):
    integrationDocumentRequest: GoogleCloudIntegrationsV2DuetIntegrationDocumentRequest

@typing.type_check_only
class GoogleCloudIntegrationsV2DuetGenerateIntegrationDocumentResponse(
    typing.TypedDict, total=False
):
    document: str

@typing.type_check_only
class GoogleCloudIntegrationsV2DuetGenerateIntegrationRequest(
    typing.TypedDict, total=False
):
    copilotEnabled: bool
    prompt: str

@typing.type_check_only
class GoogleCloudIntegrationsV2DuetGenerateIntegrationResponse(
    typing.TypedDict, total=False
):
    skeletonIntegrations: _list[GoogleCloudIntegrationsV2DuetIntegrationSkeleton]

@typing.type_check_only
class GoogleCloudIntegrationsV2DuetGenerateJavascriptRequest(
    typing.TypedDict, total=False
):
    javascriptRequest: GoogleCloudIntegrationsV2DuetJavascriptRequest
    prompt: str

@typing.type_check_only
class GoogleCloudIntegrationsV2DuetGenerateJavascriptResponse(
    typing.TypedDict, total=False
):
    recommendations: _list[GoogleCloudIntegrationsV2DuetJavascriptRecommendation]

@typing.type_check_only
class GoogleCloudIntegrationsV2DuetIntParameterArray(typing.TypedDict, total=False):
    intValues: _list[str]

@typing.type_check_only
class GoogleCloudIntegrationsV2DuetIntegrationBranch(typing.TypedDict, total=False):
    branchCondition: str
    explanation: str
    integrationParameters: _list[GoogleCloudIntegrationsV2DuetIntegrationParameter]
    taskConfigs: _list[GoogleCloudIntegrationsV2DuetTaskConfig]

@typing.type_check_only
class GoogleCloudIntegrationsV2DuetIntegrationBranchRequest(
    typing.TypedDict, total=False
):
    branchCondition: str
    integrationParameters: _list[GoogleCloudIntegrationsV2DuetIntegrationParameter]
    taskConfigs: _list[GoogleCloudIntegrationsV2DuetTaskConfig]

@typing.type_check_only
class GoogleCloudIntegrationsV2DuetIntegrationConfigParameter(
    typing.TypedDict, total=False
):
    parameter: GoogleCloudIntegrationsV2DuetIntegrationParameter
    value: GoogleCloudIntegrationsV2DuetValueType

@typing.type_check_only
class GoogleCloudIntegrationsV2DuetIntegrationDocumentRequest(
    typing.TypedDict, total=False
):
    integrationVersion: GoogleCloudIntegrationsV2DuetIntegrationVersion

@typing.type_check_only
class GoogleCloudIntegrationsV2DuetIntegrationParameter(typing.TypedDict, total=False):
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
    ]
    defaultValue: GoogleCloudIntegrationsV2DuetValueType
    description: str
    displayName: str
    inputOutputType: typing.Literal["IN_OUT_TYPE_UNSPECIFIED", "IN", "OUT", "IN_OUT"]
    isTransient: bool
    jsonSchema: str
    key: str

@typing.type_check_only
class GoogleCloudIntegrationsV2DuetIntegrationSkeleton(typing.TypedDict, total=False):
    explanation: str
    integrationVersion: GoogleCloudIntegrationsV2DuetIntegrationVersion
    name: str
    tag: str

@typing.type_check_only
class GoogleCloudIntegrationsV2DuetIntegrationVersion(typing.TypedDict, total=False):
    description: str
    errorCatcherConfigs: _list[GoogleCloudIntegrationsV2DuetErrorCatcherConfig]
    integrationConfigParameters: _list[
        GoogleCloudIntegrationsV2DuetIntegrationConfigParameter
    ]
    integrationParameters: _list[GoogleCloudIntegrationsV2DuetIntegrationParameter]
    name: str
    snapshotNumber: str
    state: typing.Literal[
        "INTEGRATION_STATE_UNSPECIFIED", "DRAFT", "ACTIVE", "ARCHIVED", "SNAPSHOT"
    ]
    taskConfigs: _list[GoogleCloudIntegrationsV2DuetTaskConfig]
    triggerConfigs: _list[GoogleCloudIntegrationsV2DuetTriggerConfig]
    userLabel: str

@typing.type_check_only
class GoogleCloudIntegrationsV2DuetJavascriptRecommendation(
    typing.TypedDict, total=False
):
    explanation: str
    integrationParameters: _list[GoogleCloudIntegrationsV2DuetIntegrationParameter]
    taskConfig: GoogleCloudIntegrationsV2DuetTaskConfig

@typing.type_check_only
class GoogleCloudIntegrationsV2DuetJavascriptRequest(typing.TypedDict, total=False):
    copilotEnabled: bool
    integrationVersion: GoogleCloudIntegrationsV2DuetIntegrationVersion
    taskId: str
    useCurrentScript: bool

@typing.type_check_only
class GoogleCloudIntegrationsV2DuetNextTask(typing.TypedDict, total=False):
    condition: str
    description: str
    displayName: str
    taskConfigId: str
    taskId: str

@typing.type_check_only
class GoogleCloudIntegrationsV2DuetRecommendTasksRequest(typing.TypedDict, total=False):
    prompt: str
    replaceTaskRequest: GoogleCloudIntegrationsV2DuetReplaceTaskRequest

@typing.type_check_only
class GoogleCloudIntegrationsV2DuetRecommendTasksResponse(
    typing.TypedDict, total=False
):
    taskConfigs: _list[GoogleCloudIntegrationsV2DuetTaskConfig]
    taskResponseStatuses: _list[GoogleCloudIntegrationsV2DuetTaskResponseStatus]

@typing.type_check_only
class GoogleCloudIntegrationsV2DuetReplaceTaskRequest(typing.TypedDict, total=False):
    copilotEnabled: bool
    taskConfig: GoogleCloudIntegrationsV2DuetTaskConfig
    taskTypes: _list[
        typing.Literal["TASK_TYPE_UNSPECIFIED", "CONNECTOR_TASK", "REST_TASK"]
    ]

@typing.type_check_only
class GoogleCloudIntegrationsV2DuetStringParameterArray(typing.TypedDict, total=False):
    stringValues: _list[str]

@typing.type_check_only
class GoogleCloudIntegrationsV2DuetTaskConfig(typing.TypedDict, total=False):
    description: str
    displayName: str
    errorCatcherId: str
    externalTaskType: typing.Literal[
        "EXTERNAL_TASK_TYPE_UNSPECIFIED", "NORMAL_TASK", "ERROR_TASK"
    ]
    nextTasks: _list[GoogleCloudIntegrationsV2DuetNextTask]
    parameters: dict[str, typing.Any]
    task: str
    taskId: str

@typing.type_check_only
class GoogleCloudIntegrationsV2DuetTaskResponseStatus(typing.TypedDict, total=False):
    errorMessage: str
    httpCode: int
    taskType: typing.Literal["TASK_TYPE_UNSPECIFIED", "CONNECTOR_TASK", "REST_TASK"]

@typing.type_check_only
class GoogleCloudIntegrationsV2DuetTriggerConfig(typing.TypedDict, total=False):
    cloudSchedulerConfig: GoogleCloudIntegrationsV2DuetCloudSchedulerConfig
    description: str
    errorCatcherId: str
    inputVariables: GoogleCloudIntegrationsV2DuetTriggerConfigVariables
    label: str
    outputVariables: GoogleCloudIntegrationsV2DuetTriggerConfigVariables
    properties: dict[str, typing.Any]
    startTasks: _list[GoogleCloudIntegrationsV2DuetNextTask]
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
    ]

@typing.type_check_only
class GoogleCloudIntegrationsV2DuetTriggerConfigVariables(
    typing.TypedDict, total=False
):
    names: _list[str]

@typing.type_check_only
class GoogleCloudIntegrationsV2DuetTroubleshootExecutionResponse(
    typing.TypedDict, total=False
):
    detailedExplanation: str
    displayMessage: str
    errorMessage: str
    executionId: str
    rootCause: str

@typing.type_check_only
class GoogleCloudIntegrationsV2DuetValueType(typing.TypedDict, total=False):
    booleanArray: GoogleCloudIntegrationsV2DuetBooleanParameterArray
    booleanValue: bool
    doubleArray: GoogleCloudIntegrationsV2DuetDoubleParameterArray
    doubleValue: float
    intArray: GoogleCloudIntegrationsV2DuetIntParameterArray
    intValue: str
    jsonValue: str
    stringArray: GoogleCloudIntegrationsV2DuetStringParameterArray
    stringValue: str

@typing.type_check_only
class GoogleCloudIntegrationsV2Execution(typing.TypedDict, total=False):
    cloudLoggingDetails: GoogleCloudIntegrationsV2CloudLoggingDetails
    containTaskVariables: bool
    createTime: str
    executionAttemptStats: _list[GoogleCloudIntegrationsV2AttemptStats]
    integrationVersionNumber: str
    integrationVersionUserLabel: str
    name: str
    replayInfo: GoogleCloudIntegrationsV2ExecutionReplayInfo
    requestVariables: dict[str, typing.Any]
    responseVariables: dict[str, typing.Any]
    state: typing.Literal[
        "STATE_UNSPECIFIED",
        "ON_HOLD",
        "IN_PROCESS",
        "SUCCEEDED",
        "FAILED",
        "CANCELLED",
        "RETRY_ON_HOLD",
        "SUSPENDED",
    ]
    taskExecutions: _list[GoogleCloudIntegrationsV2TaskExecution]
    triggerId: str
    updateTime: str

@typing.type_check_only
class GoogleCloudIntegrationsV2ExecutionReplayInfo(typing.TypedDict, total=False):
    originalExecutionId: str
    replayMode: typing.Literal[
        "REPLAY_MODE_UNSPECIFIED",
        "REPLAY_MODE_FROM_BEGINNING",
        "REPLAY_MODE_POINT_OF_FAILURE",
    ]
    replayReason: str
    replayedExecutionIds: _list[str]

@typing.type_check_only
class GoogleCloudIntegrationsV2ListExecutionsResponse(typing.TypedDict, total=False):
    executions: _list[GoogleCloudIntegrationsV2Execution]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudIntegrationsV2TaskExecution(typing.TypedDict, total=False):
    name: str
    taskExecutionDetails: _list[GoogleCloudIntegrationsV2TaskExecutionDetails]
    taskExecutionMetadata: GoogleCloudIntegrationsV2TaskExecutionTaskExecutionMetadata
    variables: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudIntegrationsV2TaskExecutionDetails(typing.TypedDict, total=False):
    taskAttemptStats: _list[GoogleCloudIntegrationsV2AttemptStats]
    taskExecutionState: typing.Literal[
        "STATE_UNSPECIFIED",
        "IN_PROCESS",
        "SUCCEED",
        "FAILED",
        "FATAL",
        "RETRY_ON_HOLD",
        "CANCELLED",
        "SUSPENDED",
    ]
    taskNumber: str

@typing.type_check_only
class GoogleCloudIntegrationsV2TaskExecutionTaskExecutionMetadata(
    typing.TypedDict, total=False
):
    ancestorIterationNumbers: _list[str]
    ancestorTaskNumbers: _list[str]
    executionAttempt: int
    privateIntegrationName: str
    task: str
    taskAttempt: int
    taskLabel: str
    taskNumber: str

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
    workflowId: str
    workflowName: str
