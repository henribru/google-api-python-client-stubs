import typing

import typing_extensions

_list = list

@typing.type_check_only
class GoogleCloudDatapipelinesV1ArrayValue(typing_extensions.TypedDict, total=False):
    elements: _list[GoogleCloudDatapipelinesV1FieldValue]

@typing.type_check_only
class GoogleCloudDatapipelinesV1AtomicValue(typing_extensions.TypedDict, total=False):
    booleanValue: bool
    byteValue: int
    bytesValue: str
    datetimeValue: GoogleTypeDateTime
    decimalValue: GoogleTypeDecimal
    doubleValue: float
    floatValue: float
    int16Value: int
    int32Value: int
    int64Value: str
    stringValue: str

@typing.type_check_only
class GoogleCloudDatapipelinesV1BatchGetTransformDescriptionsResponse(
    typing_extensions.TypedDict, total=False
):
    transformDescriptions: _list[GoogleCloudDatapipelinesV1TransformDescription]

@typing.type_check_only
class GoogleCloudDatapipelinesV1ComputeSchemaRequest(
    typing_extensions.TypedDict, total=False
):
    config: GoogleCloudDatapipelinesV1ConfiguredTransform
    inputSchemas: _list[GoogleCloudDatapipelinesV1Schema]
    rawSchema: GoogleCloudDatapipelinesV1RawSchemaInfo

@typing.type_check_only
class GoogleCloudDatapipelinesV1ConfiguredTransform(
    typing_extensions.TypedDict, total=False
):
    config: GoogleCloudDatapipelinesV1Row
    uniformResourceName: str

@typing.type_check_only
class GoogleCloudDatapipelinesV1DataflowJobDetails(
    typing_extensions.TypedDict, total=False
):
    currentWorkers: int
    resourceInfo: dict[str, typing.Any]
    sdkVersion: GoogleCloudDatapipelinesV1SdkVersion

@typing.type_check_only
class GoogleCloudDatapipelinesV1EnumerationValue(
    typing_extensions.TypedDict, total=False
):
    name: str

@typing.type_check_only
class GoogleCloudDatapipelinesV1Field(typing_extensions.TypedDict, total=False):
    name: str
    type: GoogleCloudDatapipelinesV1FieldType

@typing.type_check_only
class GoogleCloudDatapipelinesV1FieldType(typing_extensions.TypedDict, total=False):
    collectionElementType: GoogleCloudDatapipelinesV1FieldType
    logicalType: GoogleCloudDatapipelinesV1LogicalType
    mapType: GoogleCloudDatapipelinesV1MapType
    nullable: bool
    rowSchema: GoogleCloudDatapipelinesV1Schema
    type: typing_extensions.Literal[
        "TYPE_NAME_UNSPECIFIED",
        "TYPE_NAME_BYTE",
        "TYPE_NAME_INT16",
        "TYPE_NAME_INT32",
        "TYPE_NAME_INT64",
        "TYPE_NAME_DECIMAL",
        "TYPE_NAME_FLOAT",
        "TYPE_NAME_DOUBLE",
        "TYPE_NAME_STRING",
        "TYPE_NAME_DATETIME",
        "TYPE_NAME_BOOLEAN",
        "TYPE_NAME_BYTES",
        "TYPE_NAME_ARRAY",
        "TYPE_NAME_ITERABLE",
        "TYPE_NAME_MAP",
        "TYPE_NAME_ROW",
        "TYPE_NAME_LOGICAL_TYPE",
    ]

@typing.type_check_only
class GoogleCloudDatapipelinesV1FieldValue(typing_extensions.TypedDict, total=False):
    arrayValue: GoogleCloudDatapipelinesV1ArrayValue
    atomicValue: GoogleCloudDatapipelinesV1AtomicValue
    enumValue: GoogleCloudDatapipelinesV1EnumerationValue
    fixedBytesValue: GoogleCloudDatapipelinesV1FixedBytesValue
    iterableValue: GoogleCloudDatapipelinesV1IterableValue
    mapValue: GoogleCloudDatapipelinesV1MapValue
    rowValue: GoogleCloudDatapipelinesV1Row

@typing.type_check_only
class GoogleCloudDatapipelinesV1FixedBytesValue(
    typing_extensions.TypedDict, total=False
):
    value: str

@typing.type_check_only
class GoogleCloudDatapipelinesV1FlexTemplateRuntimeEnvironment(
    typing_extensions.TypedDict, total=False
):
    additionalExperiments: _list[str]
    additionalUserLabels: dict[str, typing.Any]
    enableStreamingEngine: bool
    flexrsGoal: typing_extensions.Literal[
        "FLEXRS_UNSPECIFIED", "FLEXRS_SPEED_OPTIMIZED", "FLEXRS_COST_OPTIMIZED"
    ]
    ipConfiguration: typing_extensions.Literal[
        "WORKER_IP_UNSPECIFIED", "WORKER_IP_PUBLIC", "WORKER_IP_PRIVATE"
    ]
    kmsKeyName: str
    machineType: str
    maxWorkers: int
    network: str
    numWorkers: int
    serviceAccountEmail: str
    subnetwork: str
    tempLocation: str
    workerRegion: str
    workerZone: str
    zone: str

@typing.type_check_only
class GoogleCloudDatapipelinesV1IterableValue(typing_extensions.TypedDict, total=False):
    elements: _list[GoogleCloudDatapipelinesV1FieldValue]

@typing.type_check_only
class GoogleCloudDatapipelinesV1Job(typing_extensions.TypedDict, total=False):
    createTime: str
    dataflowJobDetails: GoogleCloudDatapipelinesV1DataflowJobDetails
    endTime: str
    id: str
    name: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "STATE_PENDING",
        "STATE_RUNNING",
        "STATE_DONE",
        "STATE_FAILED",
        "STATE_CANCELLED",
    ]
    status: GoogleRpcStatus

@typing.type_check_only
class GoogleCloudDatapipelinesV1LaunchFlexTemplateParameter(
    typing_extensions.TypedDict, total=False
):
    containerSpecGcsPath: str
    environment: GoogleCloudDatapipelinesV1FlexTemplateRuntimeEnvironment
    jobName: str
    launchOptions: dict[str, typing.Any]
    parameters: dict[str, typing.Any]
    transformNameMappings: dict[str, typing.Any]
    update: bool

@typing.type_check_only
class GoogleCloudDatapipelinesV1LaunchFlexTemplateRequest(
    typing_extensions.TypedDict, total=False
):
    launchParameter: GoogleCloudDatapipelinesV1LaunchFlexTemplateParameter
    location: str
    projectId: str
    validateOnly: bool

@typing.type_check_only
class GoogleCloudDatapipelinesV1LaunchTemplateParameters(
    typing_extensions.TypedDict, total=False
):
    environment: GoogleCloudDatapipelinesV1RuntimeEnvironment
    jobName: str
    parameters: dict[str, typing.Any]
    transformNameMapping: dict[str, typing.Any]
    update: bool

@typing.type_check_only
class GoogleCloudDatapipelinesV1LaunchTemplateRequest(
    typing_extensions.TypedDict, total=False
):
    gcsPath: str
    launchParameters: GoogleCloudDatapipelinesV1LaunchTemplateParameters
    location: str
    projectId: str
    validateOnly: bool

@typing.type_check_only
class GoogleCloudDatapipelinesV1ListJobsResponse(
    typing_extensions.TypedDict, total=False
):
    jobs: _list[GoogleCloudDatapipelinesV1Job]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudDatapipelinesV1ListPipelinesResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    pipelines: _list[GoogleCloudDatapipelinesV1Pipeline]

@typing.type_check_only
class GoogleCloudDatapipelinesV1LogicalType(typing_extensions.TypedDict, total=False):
    enumerationType: GoogleCloudDatapipelinesV1LogicalTypeEnumerationType
    fixedBytes: GoogleCloudDatapipelinesV1LogicalTypeFixedBytes

@typing.type_check_only
class GoogleCloudDatapipelinesV1LogicalTypeEnumerationType(
    typing_extensions.TypedDict, total=False
):
    values: _list[str]

@typing.type_check_only
class GoogleCloudDatapipelinesV1LogicalTypeFixedBytes(
    typing_extensions.TypedDict, total=False
):
    sizeBytes: int

@typing.type_check_only
class GoogleCloudDatapipelinesV1MapType(typing_extensions.TypedDict, total=False):
    mapKeyType: GoogleCloudDatapipelinesV1FieldType
    mapValueType: GoogleCloudDatapipelinesV1FieldType

@typing.type_check_only
class GoogleCloudDatapipelinesV1MapValue(typing_extensions.TypedDict, total=False):
    entries: _list[GoogleCloudDatapipelinesV1MapValueEntry]

@typing.type_check_only
class GoogleCloudDatapipelinesV1MapValueEntry(typing_extensions.TypedDict, total=False):
    key: GoogleCloudDatapipelinesV1FieldValue
    value: GoogleCloudDatapipelinesV1FieldValue

@typing.type_check_only
class GoogleCloudDatapipelinesV1Pipeline(typing_extensions.TypedDict, total=False):
    createTime: str
    displayName: str
    jobCount: int
    lastUpdateTime: str
    name: str
    pipelineSources: dict[str, typing.Any]
    scheduleInfo: GoogleCloudDatapipelinesV1ScheduleSpec
    schedulerServiceAccountEmail: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "STATE_RESUMING",
        "STATE_ACTIVE",
        "STATE_STOPPING",
        "STATE_ARCHIVED",
        "STATE_PAUSED",
    ]
    type: typing_extensions.Literal[
        "PIPELINE_TYPE_UNSPECIFIED", "PIPELINE_TYPE_BATCH", "PIPELINE_TYPE_STREAMING"
    ]
    workload: GoogleCloudDatapipelinesV1Workload

@typing.type_check_only
class GoogleCloudDatapipelinesV1RawSchemaInfo(typing_extensions.TypedDict, total=False):
    rawSchema: str
    type: typing_extensions.Literal[
        "RAW_SCHEMA_TYPE_UNSPECIFIED", "RAW_SCHEMA_TYPE_AVRO"
    ]

@typing.type_check_only
class GoogleCloudDatapipelinesV1Row(typing_extensions.TypedDict, total=False):
    schema: GoogleCloudDatapipelinesV1SchemaSource
    values: _list[GoogleCloudDatapipelinesV1FieldValue]

@typing.type_check_only
class GoogleCloudDatapipelinesV1RunPipelineRequest(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDatapipelinesV1RunPipelineResponse(
    typing_extensions.TypedDict, total=False
):
    job: GoogleCloudDatapipelinesV1Job

@typing.type_check_only
class GoogleCloudDatapipelinesV1RuntimeEnvironment(
    typing_extensions.TypedDict, total=False
):
    additionalExperiments: _list[str]
    additionalUserLabels: dict[str, typing.Any]
    bypassTempDirValidation: bool
    enableStreamingEngine: bool
    ipConfiguration: typing_extensions.Literal[
        "WORKER_IP_UNSPECIFIED", "WORKER_IP_PUBLIC", "WORKER_IP_PRIVATE"
    ]
    kmsKeyName: str
    machineType: str
    maxWorkers: int
    network: str
    numWorkers: int
    serviceAccountEmail: str
    subnetwork: str
    tempLocation: str
    workerRegion: str
    workerZone: str
    zone: str

@typing.type_check_only
class GoogleCloudDatapipelinesV1ScheduleSpec(typing_extensions.TypedDict, total=False):
    nextJobTime: str
    schedule: str
    timeZone: str

@typing.type_check_only
class GoogleCloudDatapipelinesV1Schema(typing_extensions.TypedDict, total=False):
    fields: _list[GoogleCloudDatapipelinesV1Field]
    referenceId: str

@typing.type_check_only
class GoogleCloudDatapipelinesV1SchemaSource(typing_extensions.TypedDict, total=False):
    localSchema: GoogleCloudDatapipelinesV1Schema
    referenceId: str

@typing.type_check_only
class GoogleCloudDatapipelinesV1SdkVersion(typing_extensions.TypedDict, total=False):
    sdkSupportStatus: typing_extensions.Literal[
        "UNKNOWN", "SUPPORTED", "STALE", "DEPRECATED", "UNSUPPORTED"
    ]
    version: str
    versionDisplayName: str

@typing.type_check_only
class GoogleCloudDatapipelinesV1StopPipelineRequest(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDatapipelinesV1TransformDescription(
    typing_extensions.TypedDict, total=False
):
    name: str
    options: GoogleCloudDatapipelinesV1Schema
    uniformResourceName: str

@typing.type_check_only
class GoogleCloudDatapipelinesV1Workload(typing_extensions.TypedDict, total=False):
    dataflowFlexTemplateRequest: GoogleCloudDatapipelinesV1LaunchFlexTemplateRequest
    dataflowLaunchTemplateRequest: GoogleCloudDatapipelinesV1LaunchTemplateRequest

@typing.type_check_only
class GoogleProtobufEmpty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class GoogleRpcStatus(typing_extensions.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class GoogleTypeDateTime(typing_extensions.TypedDict, total=False):
    day: int
    hours: int
    minutes: int
    month: int
    nanos: int
    seconds: int
    timeZone: GoogleTypeTimeZone
    utcOffset: str
    year: int

@typing.type_check_only
class GoogleTypeDecimal(typing_extensions.TypedDict, total=False):
    value: str

@typing.type_check_only
class GoogleTypeTimeZone(typing_extensions.TypedDict, total=False):
    id: str
    version: str
