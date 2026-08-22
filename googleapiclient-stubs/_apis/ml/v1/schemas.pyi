import typing

_list = list

@typing.type_check_only
class GoogleApi__HttpBody(typing.TypedDict, total=False):
    contentType: str
    data: str
    extensions: _list[dict[str, typing.Any]]

@typing.type_check_only
class GoogleCloudMlV1_AutomatedStoppingConfig_DecayCurveAutomatedStoppingConfig(
    typing.TypedDict, total=False
):
    useElapsedTime: bool

@typing.type_check_only
class GoogleCloudMlV1_AutomatedStoppingConfig_MedianAutomatedStoppingConfig(
    typing.TypedDict, total=False
):
    useElapsedTime: bool

@typing.type_check_only
class GoogleCloudMlV1_HyperparameterOutput_HyperparameterMetric(
    typing.TypedDict, total=False
):
    objectiveValue: float
    trainingStep: str

@typing.type_check_only
class GoogleCloudMlV1_Measurement_Metric(typing.TypedDict, total=False):
    metric: str
    value: float

@typing.type_check_only
class GoogleCloudMlV1_StudyConfigParameterSpec_CategoricalValueSpec(
    typing.TypedDict, total=False
):
    values: _list[str]

@typing.type_check_only
class GoogleCloudMlV1_StudyConfigParameterSpec_DiscreteValueSpec(
    typing.TypedDict, total=False
):
    values: _list[float]

@typing.type_check_only
class GoogleCloudMlV1_StudyConfigParameterSpec_DoubleValueSpec(
    typing.TypedDict, total=False
):
    maxValue: float
    minValue: float

@typing.type_check_only
class GoogleCloudMlV1_StudyConfigParameterSpec_IntegerValueSpec(
    typing.TypedDict, total=False
):
    maxValue: str
    minValue: str

@typing.type_check_only
class GoogleCloudMlV1_StudyConfigParameterSpec_MatchingParentCategoricalValueSpec(
    typing.TypedDict, total=False
):
    values: _list[str]

@typing.type_check_only
class GoogleCloudMlV1_StudyConfigParameterSpec_MatchingParentDiscreteValueSpec(
    typing.TypedDict, total=False
):
    values: _list[float]

@typing.type_check_only
class GoogleCloudMlV1_StudyConfigParameterSpec_MatchingParentIntValueSpec(
    typing.TypedDict, total=False
):
    values: _list[str]

@typing.type_check_only
class GoogleCloudMlV1_StudyConfig_MetricSpec(typing.TypedDict, total=False):
    goal: typing.Literal["GOAL_TYPE_UNSPECIFIED", "MAXIMIZE", "MINIMIZE"]
    metric: str

@typing.type_check_only
class GoogleCloudMlV1_StudyConfig_ParameterSpec(typing.TypedDict, total=False):
    categoricalValueSpec: GoogleCloudMlV1_StudyConfigParameterSpec_CategoricalValueSpec
    childParameterSpecs: _list[GoogleCloudMlV1_StudyConfig_ParameterSpec]
    discreteValueSpec: GoogleCloudMlV1_StudyConfigParameterSpec_DiscreteValueSpec
    doubleValueSpec: GoogleCloudMlV1_StudyConfigParameterSpec_DoubleValueSpec
    integerValueSpec: GoogleCloudMlV1_StudyConfigParameterSpec_IntegerValueSpec
    parameter: str
    parentCategoricalValues: (
        GoogleCloudMlV1_StudyConfigParameterSpec_MatchingParentCategoricalValueSpec
    )
    parentDiscreteValues: (
        GoogleCloudMlV1_StudyConfigParameterSpec_MatchingParentDiscreteValueSpec
    )
    parentIntValues: GoogleCloudMlV1_StudyConfigParameterSpec_MatchingParentIntValueSpec
    scaleType: typing.Literal[
        "SCALE_TYPE_UNSPECIFIED",
        "UNIT_LINEAR_SCALE",
        "UNIT_LOG_SCALE",
        "UNIT_REVERSE_LOG_SCALE",
    ]
    type: typing.Literal[
        "PARAMETER_TYPE_UNSPECIFIED", "DOUBLE", "INTEGER", "CATEGORICAL", "DISCRETE"
    ]

@typing.type_check_only
class GoogleCloudMlV1_Trial_Parameter(typing.TypedDict, total=False):
    floatValue: float
    intValue: str
    parameter: str
    stringValue: str

@typing.type_check_only
class GoogleCloudMlV1__AcceleratorConfig(typing.TypedDict, total=False):
    count: str
    type: typing.Literal[
        "ACCELERATOR_TYPE_UNSPECIFIED",
        "NVIDIA_TESLA_K80",
        "NVIDIA_TESLA_P100",
        "NVIDIA_TESLA_V100",
        "NVIDIA_TESLA_P4",
        "NVIDIA_TESLA_T4",
        "NVIDIA_TESLA_A100",
        "TPU_V2",
        "TPU_V3",
        "TPU_V2_POD",
        "TPU_V3_POD",
        "TPU_V4_POD",
    ]

@typing.type_check_only
class GoogleCloudMlV1__AddTrialMeasurementRequest(typing.TypedDict, total=False):
    measurement: GoogleCloudMlV1__Measurement

@typing.type_check_only
class GoogleCloudMlV1__AutoScaling(typing.TypedDict, total=False):
    maxNodes: int
    metrics: _list[GoogleCloudMlV1__MetricSpec]
    minNodes: int

@typing.type_check_only
class GoogleCloudMlV1__AutomatedStoppingConfig(typing.TypedDict, total=False):
    decayCurveStoppingConfig: (
        GoogleCloudMlV1_AutomatedStoppingConfig_DecayCurveAutomatedStoppingConfig
    )
    medianAutomatedStoppingConfig: (
        GoogleCloudMlV1_AutomatedStoppingConfig_MedianAutomatedStoppingConfig
    )

@typing.type_check_only
class GoogleCloudMlV1__BuiltInAlgorithmOutput(typing.TypedDict, total=False):
    framework: str
    modelPath: str
    pythonVersion: str
    runtimeVersion: str

@typing.type_check_only
class GoogleCloudMlV1__CancelJobRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleCloudMlV1__Capability(typing.TypedDict, total=False):
    availableAccelerators: _list[
        typing.Literal[
            "ACCELERATOR_TYPE_UNSPECIFIED",
            "NVIDIA_TESLA_K80",
            "NVIDIA_TESLA_P100",
            "NVIDIA_TESLA_V100",
            "NVIDIA_TESLA_P4",
            "NVIDIA_TESLA_T4",
            "NVIDIA_TESLA_A100",
            "TPU_V2",
            "TPU_V3",
            "TPU_V2_POD",
            "TPU_V3_POD",
            "TPU_V4_POD",
        ]
    ]
    type: typing.Literal[
        "TYPE_UNSPECIFIED", "TRAINING", "BATCH_PREDICTION", "ONLINE_PREDICTION"
    ]

@typing.type_check_only
class GoogleCloudMlV1__CheckTrialEarlyStoppingStateMetatdata(
    typing.TypedDict, total=False
):
    createTime: str
    study: str
    trial: str

@typing.type_check_only
class GoogleCloudMlV1__CheckTrialEarlyStoppingStateRequest(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudMlV1__CheckTrialEarlyStoppingStateResponse(
    typing.TypedDict, total=False
):
    endTime: str
    shouldStop: bool
    startTime: str

@typing.type_check_only
class GoogleCloudMlV1__CompleteTrialRequest(typing.TypedDict, total=False):
    finalMeasurement: GoogleCloudMlV1__Measurement
    infeasibleReason: str
    trialInfeasible: bool

@typing.type_check_only
class GoogleCloudMlV1__Config(typing.TypedDict, total=False):
    tpuServiceAccount: str

@typing.type_check_only
class GoogleCloudMlV1__ContainerPort(typing.TypedDict, total=False):
    containerPort: int

@typing.type_check_only
class GoogleCloudMlV1__ContainerSpec(typing.TypedDict, total=False):
    args: _list[str]
    command: _list[str]
    env: _list[GoogleCloudMlV1__EnvVar]
    image: str
    ports: _list[GoogleCloudMlV1__ContainerPort]

@typing.type_check_only
class GoogleCloudMlV1__DiskConfig(typing.TypedDict, total=False):
    bootDiskSizeGb: int
    bootDiskType: str

@typing.type_check_only
class GoogleCloudMlV1__EncryptionConfig(typing.TypedDict, total=False):
    kmsKeyName: str

@typing.type_check_only
class GoogleCloudMlV1__EnvVar(typing.TypedDict, total=False):
    name: str
    value: str

@typing.type_check_only
class GoogleCloudMlV1__ExplainRequest(typing.TypedDict, total=False):
    httpBody: GoogleApi__HttpBody

@typing.type_check_only
class GoogleCloudMlV1__ExplanationConfig(typing.TypedDict, total=False):
    integratedGradientsAttribution: GoogleCloudMlV1__IntegratedGradientsAttribution
    sampledShapleyAttribution: GoogleCloudMlV1__SampledShapleyAttribution
    xraiAttribution: GoogleCloudMlV1__XraiAttribution

@typing.type_check_only
class GoogleCloudMlV1__GetConfigResponse(typing.TypedDict, total=False):
    config: GoogleCloudMlV1__Config
    serviceAccount: str
    serviceAccountProject: str

@typing.type_check_only
class GoogleCloudMlV1__HyperparameterOutput(typing.TypedDict, total=False):
    allMetrics: _list[GoogleCloudMlV1_HyperparameterOutput_HyperparameterMetric]
    builtInAlgorithmOutput: GoogleCloudMlV1__BuiltInAlgorithmOutput
    endTime: str
    finalMetric: GoogleCloudMlV1_HyperparameterOutput_HyperparameterMetric
    hyperparameters: dict[str, typing.Any]
    isTrialStoppedEarly: bool
    startTime: str
    state: typing.Literal[
        "STATE_UNSPECIFIED",
        "QUEUED",
        "PREPARING",
        "RUNNING",
        "SUCCEEDED",
        "FAILED",
        "CANCELLING",
        "CANCELLED",
    ]
    trialId: str
    webAccessUris: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudMlV1__HyperparameterSpec(typing.TypedDict, total=False):
    algorithm: typing.Literal["ALGORITHM_UNSPECIFIED", "GRID_SEARCH", "RANDOM_SEARCH"]
    enableTrialEarlyStopping: bool
    goal: typing.Literal["GOAL_TYPE_UNSPECIFIED", "MAXIMIZE", "MINIMIZE"]
    hyperparameterMetricTag: str
    maxFailedTrials: int
    maxParallelTrials: int
    maxTrials: int
    params: _list[GoogleCloudMlV1__ParameterSpec]
    resumePreviousJobId: str

@typing.type_check_only
class GoogleCloudMlV1__IntegratedGradientsAttribution(typing.TypedDict, total=False):
    numIntegralSteps: int

@typing.type_check_only
class GoogleCloudMlV1__Job(typing.TypedDict, total=False):
    createTime: str
    endTime: str
    errorMessage: str
    etag: str
    jobId: str
    jobPosition: str
    labels: dict[str, typing.Any]
    predictionInput: GoogleCloudMlV1__PredictionInput
    predictionOutput: GoogleCloudMlV1__PredictionOutput
    startTime: str
    state: typing.Literal[
        "STATE_UNSPECIFIED",
        "QUEUED",
        "PREPARING",
        "RUNNING",
        "SUCCEEDED",
        "FAILED",
        "CANCELLING",
        "CANCELLED",
    ]
    trainingInput: GoogleCloudMlV1__TrainingInput
    trainingOutput: GoogleCloudMlV1__TrainingOutput

@typing.type_check_only
class GoogleCloudMlV1__ListJobsResponse(typing.TypedDict, total=False):
    jobs: _list[GoogleCloudMlV1__Job]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudMlV1__ListLocationsResponse(typing.TypedDict, total=False):
    locations: _list[GoogleCloudMlV1__Location]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudMlV1__ListModelsResponse(typing.TypedDict, total=False):
    models: _list[GoogleCloudMlV1__Model]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudMlV1__ListOptimalTrialsRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleCloudMlV1__ListOptimalTrialsResponse(typing.TypedDict, total=False):
    trials: _list[GoogleCloudMlV1__Trial]

@typing.type_check_only
class GoogleCloudMlV1__ListStudiesResponse(typing.TypedDict, total=False):
    studies: _list[GoogleCloudMlV1__Study]

@typing.type_check_only
class GoogleCloudMlV1__ListTrialsResponse(typing.TypedDict, total=False):
    trials: _list[GoogleCloudMlV1__Trial]

@typing.type_check_only
class GoogleCloudMlV1__ListVersionsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    versions: _list[GoogleCloudMlV1__Version]

@typing.type_check_only
class GoogleCloudMlV1__Location(typing.TypedDict, total=False):
    capabilities: _list[GoogleCloudMlV1__Capability]
    name: str

@typing.type_check_only
class GoogleCloudMlV1__ManualScaling(typing.TypedDict, total=False):
    nodes: int

@typing.type_check_only
class GoogleCloudMlV1__Measurement(typing.TypedDict, total=False):
    elapsedTime: str
    metrics: _list[GoogleCloudMlV1_Measurement_Metric]
    stepCount: str

@typing.type_check_only
class GoogleCloudMlV1__MetricSpec(typing.TypedDict, total=False):
    name: typing.Literal["METRIC_NAME_UNSPECIFIED", "CPU_USAGE", "GPU_DUTY_CYCLE"]
    target: int

@typing.type_check_only
class GoogleCloudMlV1__Model(typing.TypedDict, total=False):
    defaultVersion: GoogleCloudMlV1__Version
    description: str
    etag: str
    labels: dict[str, typing.Any]
    name: str
    onlinePredictionConsoleLogging: bool
    onlinePredictionLogging: bool
    regions: _list[str]

@typing.type_check_only
class GoogleCloudMlV1__OperationMetadata(typing.TypedDict, total=False):
    createTime: str
    endTime: str
    isCancellationRequested: bool
    labels: dict[str, typing.Any]
    modelName: str
    operationType: typing.Literal[
        "OPERATION_TYPE_UNSPECIFIED",
        "CREATE_VERSION",
        "DELETE_VERSION",
        "DELETE_MODEL",
        "UPDATE_MODEL",
        "UPDATE_VERSION",
        "UPDATE_CONFIG",
    ]
    projectNumber: str
    startTime: str
    version: GoogleCloudMlV1__Version

@typing.type_check_only
class GoogleCloudMlV1__ParameterSpec(typing.TypedDict, total=False):
    categoricalValues: _list[str]
    discreteValues: _list[float]
    maxValue: float
    minValue: float
    parameterName: str
    scaleType: typing.Literal[
        "NONE", "UNIT_LINEAR_SCALE", "UNIT_LOG_SCALE", "UNIT_REVERSE_LOG_SCALE"
    ]
    type: typing.Literal[
        "PARAMETER_TYPE_UNSPECIFIED", "DOUBLE", "INTEGER", "CATEGORICAL", "DISCRETE"
    ]

@typing.type_check_only
class GoogleCloudMlV1__PredictRequest(typing.TypedDict, total=False):
    httpBody: GoogleApi__HttpBody

@typing.type_check_only
class GoogleCloudMlV1__PredictionInput(typing.TypedDict, total=False):
    batchSize: str
    dataFormat: typing.Literal[
        "DATA_FORMAT_UNSPECIFIED", "JSON", "TEXT", "TF_RECORD", "TF_RECORD_GZIP", "CSV"
    ]
    inputPaths: _list[str]
    maxWorkerCount: str
    modelName: str
    outputDataFormat: typing.Literal[
        "DATA_FORMAT_UNSPECIFIED", "JSON", "TEXT", "TF_RECORD", "TF_RECORD_GZIP", "CSV"
    ]
    outputPath: str
    region: str
    runtimeVersion: str
    signatureName: str
    uri: str
    versionName: str

@typing.type_check_only
class GoogleCloudMlV1__PredictionOutput(typing.TypedDict, total=False):
    errorCount: str
    nodeHours: float
    outputPath: str
    predictionCount: str

@typing.type_check_only
class GoogleCloudMlV1__ReplicaConfig(typing.TypedDict, total=False):
    acceleratorConfig: GoogleCloudMlV1__AcceleratorConfig
    containerArgs: _list[str]
    containerCommand: _list[str]
    diskConfig: GoogleCloudMlV1__DiskConfig
    imageUri: str
    tpuTfVersion: str

@typing.type_check_only
class GoogleCloudMlV1__RequestLoggingConfig(typing.TypedDict, total=False):
    bigqueryTableName: str
    samplingPercentage: float

@typing.type_check_only
class GoogleCloudMlV1__RouteMap(typing.TypedDict, total=False):
    health: str
    predict: str

@typing.type_check_only
class GoogleCloudMlV1__SampledShapleyAttribution(typing.TypedDict, total=False):
    numPaths: int

@typing.type_check_only
class GoogleCloudMlV1__Scheduling(typing.TypedDict, total=False):
    maxRunningTime: str
    maxWaitTime: str
    priority: int

@typing.type_check_only
class GoogleCloudMlV1__SetDefaultVersionRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleCloudMlV1__StopTrialRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleCloudMlV1__Study(typing.TypedDict, total=False):
    createTime: str
    inactiveReason: str
    name: str
    state: typing.Literal["STATE_UNSPECIFIED", "ACTIVE", "INACTIVE", "COMPLETED"]
    studyConfig: GoogleCloudMlV1__StudyConfig

@typing.type_check_only
class GoogleCloudMlV1__StudyConfig(typing.TypedDict, total=False):
    algorithm: typing.Literal[
        "ALGORITHM_UNSPECIFIED",
        "GAUSSIAN_PROCESS_BANDIT",
        "GRID_SEARCH",
        "RANDOM_SEARCH",
    ]
    automatedStoppingConfig: GoogleCloudMlV1__AutomatedStoppingConfig
    metrics: _list[GoogleCloudMlV1_StudyConfig_MetricSpec]
    parameters: _list[GoogleCloudMlV1_StudyConfig_ParameterSpec]

@typing.type_check_only
class GoogleCloudMlV1__SuggestTrialsMetadata(typing.TypedDict, total=False):
    clientId: str
    createTime: str
    study: str
    suggestionCount: int

@typing.type_check_only
class GoogleCloudMlV1__SuggestTrialsRequest(typing.TypedDict, total=False):
    clientId: str
    suggestionCount: int

@typing.type_check_only
class GoogleCloudMlV1__SuggestTrialsResponse(typing.TypedDict, total=False):
    endTime: str
    startTime: str
    studyState: typing.Literal["STATE_UNSPECIFIED", "ACTIVE", "INACTIVE", "COMPLETED"]
    trials: _list[GoogleCloudMlV1__Trial]

@typing.type_check_only
class GoogleCloudMlV1__TrainingInput(typing.TypedDict, total=False):
    args: _list[str]
    enableWebAccess: bool
    encryptionConfig: GoogleCloudMlV1__EncryptionConfig
    evaluatorConfig: GoogleCloudMlV1__ReplicaConfig
    evaluatorCount: str
    evaluatorType: str
    hyperparameters: GoogleCloudMlV1__HyperparameterSpec
    jobDir: str
    masterConfig: GoogleCloudMlV1__ReplicaConfig
    masterType: str
    network: str
    packageUris: _list[str]
    parameterServerConfig: GoogleCloudMlV1__ReplicaConfig
    parameterServerCount: str
    parameterServerType: str
    pythonModule: str
    pythonVersion: str
    region: str
    runtimeVersion: str
    scaleTier: typing.Literal[
        "BASIC", "STANDARD_1", "PREMIUM_1", "BASIC_GPU", "BASIC_TPU", "CUSTOM"
    ]
    scheduling: GoogleCloudMlV1__Scheduling
    serviceAccount: str
    useChiefInTfConfig: bool
    workerConfig: GoogleCloudMlV1__ReplicaConfig
    workerCount: str
    workerType: str

@typing.type_check_only
class GoogleCloudMlV1__TrainingOutput(typing.TypedDict, total=False):
    builtInAlgorithmOutput: GoogleCloudMlV1__BuiltInAlgorithmOutput
    completedTrialCount: str
    consumedMLUnits: float
    hyperparameterMetricTag: str
    isBuiltInAlgorithmJob: bool
    isHyperparameterTuningJob: bool
    trials: _list[GoogleCloudMlV1__HyperparameterOutput]
    webAccessUris: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudMlV1__Trial(typing.TypedDict, total=False):
    clientId: str
    endTime: str
    finalMeasurement: GoogleCloudMlV1__Measurement
    infeasibleReason: str
    measurements: _list[GoogleCloudMlV1__Measurement]
    name: str
    parameters: _list[GoogleCloudMlV1_Trial_Parameter]
    startTime: str
    state: typing.Literal[
        "STATE_UNSPECIFIED", "REQUESTED", "ACTIVE", "COMPLETED", "STOPPING"
    ]
    trialInfeasible: bool

@typing.type_check_only
class GoogleCloudMlV1__Version(typing.TypedDict, total=False):
    acceleratorConfig: GoogleCloudMlV1__AcceleratorConfig
    autoScaling: GoogleCloudMlV1__AutoScaling
    container: GoogleCloudMlV1__ContainerSpec
    createTime: str
    deploymentUri: str
    description: str
    errorMessage: str
    etag: str
    explanationConfig: GoogleCloudMlV1__ExplanationConfig
    framework: typing.Literal[
        "FRAMEWORK_UNSPECIFIED", "TENSORFLOW", "SCIKIT_LEARN", "XGBOOST"
    ]
    isDefault: bool
    labels: dict[str, typing.Any]
    lastMigrationModelId: str
    lastMigrationTime: str
    lastUseTime: str
    machineType: str
    manualScaling: GoogleCloudMlV1__ManualScaling
    name: str
    packageUris: _list[str]
    predictionClass: str
    pythonVersion: str
    requestLoggingConfig: GoogleCloudMlV1__RequestLoggingConfig
    routes: GoogleCloudMlV1__RouteMap
    runtimeVersion: str
    serviceAccount: str
    state: typing.Literal[
        "UNKNOWN", "READY", "CREATING", "FAILED", "DELETING", "UPDATING"
    ]

@typing.type_check_only
class GoogleCloudMlV1__XraiAttribution(typing.TypedDict, total=False):
    numIntegralSteps: int

@typing.type_check_only
class GoogleIamV1__AuditConfig(typing.TypedDict, total=False):
    auditLogConfigs: _list[GoogleIamV1__AuditLogConfig]
    service: str

@typing.type_check_only
class GoogleIamV1__AuditLogConfig(typing.TypedDict, total=False):
    exemptedMembers: _list[str]
    logType: typing.Literal[
        "LOG_TYPE_UNSPECIFIED", "ADMIN_READ", "DATA_WRITE", "DATA_READ"
    ]

@typing.type_check_only
class GoogleIamV1__Binding(typing.TypedDict, total=False):
    condition: GoogleType__Expr
    members: _list[str]
    role: str

@typing.type_check_only
class GoogleIamV1__Policy(typing.TypedDict, total=False):
    auditConfigs: _list[GoogleIamV1__AuditConfig]
    bindings: _list[GoogleIamV1__Binding]
    etag: str
    version: int

@typing.type_check_only
class GoogleIamV1__SetIamPolicyRequest(typing.TypedDict, total=False):
    policy: GoogleIamV1__Policy
    updateMask: str

@typing.type_check_only
class GoogleIamV1__TestIamPermissionsRequest(typing.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class GoogleIamV1__TestIamPermissionsResponse(typing.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class GoogleLongrunning__ListOperationsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    operations: _list[GoogleLongrunning__Operation]
    unreachable: _list[str]

@typing.type_check_only
class GoogleLongrunning__Operation(typing.TypedDict, total=False):
    done: bool
    error: GoogleRpc__Status
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class GoogleProtobuf__Empty(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleRpc__Status(typing.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class GoogleType__Expr(typing.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str
