import typing

import typing_extensions

class GoogleRpc__Status(typing_extensions.TypedDict, total=False):
    code: int
    message: str
    details: typing.List[typing.Dict[str, typing.Any]]

class GoogleCloudMlV1__Config(typing_extensions.TypedDict, total=False):
    tpuServiceAccount: str

class GoogleCloudMlV1_StudyConfigParameterSpec_DiscreteValueSpec(
    typing_extensions.TypedDict, total=False
):
    values: typing.List[float]

class GoogleCloudMlV1__StopTrialRequest(typing_extensions.TypedDict, total=False): ...

class GoogleCloudMlV1__Measurement(typing_extensions.TypedDict, total=False):
    stepCount: str
    metrics: typing.List[GoogleCloudMlV1_Measurement_Metric]
    elapsedTime: str

class GoogleCloudMlV1_AutomatedStoppingConfig_DecayCurveAutomatedStoppingConfig(
    typing_extensions.TypedDict, total=False
):
    useElapsedTime: bool

class GoogleCloudMlV1__Study(typing_extensions.TypedDict, total=False):
    name: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "ACTIVE", "INACTIVE", "COMPLETED"
    ]
    studyConfig: GoogleCloudMlV1__StudyConfig
    createTime: str
    inactiveReason: str

class GoogleCloudMlV1__Trial(typing_extensions.TypedDict, total=False):
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "REQUESTED", "ACTIVE", "COMPLETED", "STOPPING"
    ]
    clientId: str
    measurements: typing.List[GoogleCloudMlV1__Measurement]
    endTime: str
    name: str
    finalMeasurement: GoogleCloudMlV1__Measurement
    trialInfeasible: bool
    parameters: typing.List[GoogleCloudMlV1_Trial_Parameter]
    infeasibleReason: str
    startTime: str

class GoogleCloudMlV1__BuiltInAlgorithmOutput(typing_extensions.TypedDict, total=False):
    runtimeVersion: str
    pythonVersion: str
    framework: str
    modelPath: str

class GoogleLongrunning__Operation(typing_extensions.TypedDict, total=False):
    name: str
    error: GoogleRpc__Status
    done: bool
    response: typing.Dict[str, typing.Any]
    metadata: typing.Dict[str, typing.Any]

class GoogleCloudMlV1__ExplanationConfig(typing_extensions.TypedDict, total=False):
    sampledShapleyAttribution: GoogleCloudMlV1__SampledShapleyAttribution
    xraiAttribution: GoogleCloudMlV1__XraiAttribution
    integratedGradientsAttribution: GoogleCloudMlV1__IntegratedGradientsAttribution

class GoogleCloudMlV1__ListVersionsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    versions: typing.List[GoogleCloudMlV1__Version]

class GoogleCloudMlV1__TrainingInput(typing_extensions.TypedDict, total=False):
    encryptionConfig: GoogleCloudMlV1__EncryptionConfig
    network: str
    pythonVersion: str
    scheduling: GoogleCloudMlV1__Scheduling
    workerCount: str
    jobDir: str
    evaluatorType: str
    region: str
    useChiefInTfConfig: bool
    parameterServerType: str
    scaleTier: typing_extensions.Literal[
        "BASIC", "STANDARD_1", "PREMIUM_1", "BASIC_GPU", "BASIC_TPU", "CUSTOM"
    ]
    hyperparameters: GoogleCloudMlV1__HyperparameterSpec
    workerType: str
    serviceAccount: str
    parameterServerCount: str
    masterConfig: GoogleCloudMlV1__ReplicaConfig
    packageUris: typing.List[str]
    runtimeVersion: str
    pythonModule: str
    evaluatorConfig: GoogleCloudMlV1__ReplicaConfig
    args: typing.List[str]
    workerConfig: GoogleCloudMlV1__ReplicaConfig
    parameterServerConfig: GoogleCloudMlV1__ReplicaConfig
    evaluatorCount: str
    masterType: str

class GoogleApi__HttpBody(typing_extensions.TypedDict, total=False):
    data: str
    extensions: typing.List[typing.Dict[str, typing.Any]]
    contentType: str

class GoogleCloudMlV1__CheckTrialEarlyStoppingStateMetatdata(
    typing_extensions.TypedDict, total=False
):
    trial: str
    createTime: str
    study: str

class GoogleLongrunning__ListOperationsResponse(
    typing_extensions.TypedDict, total=False
):
    operations: typing.List[GoogleLongrunning__Operation]
    nextPageToken: str

class GoogleCloudMlV1__ListTrialsResponse(typing_extensions.TypedDict, total=False):
    trials: typing.List[GoogleCloudMlV1__Trial]

class GoogleCloudMlV1_Measurement_Metric(typing_extensions.TypedDict, total=False):
    value: float
    metric: str

class GoogleCloudMlV1__ReplicaConfig(typing_extensions.TypedDict, total=False):
    containerCommand: typing.List[str]
    imageUri: str
    tpuTfVersion: str
    acceleratorConfig: GoogleCloudMlV1__AcceleratorConfig
    containerArgs: typing.List[str]

class GoogleCloudMlV1__RequestLoggingConfig(typing_extensions.TypedDict, total=False):
    samplingPercentage: float
    bigqueryTableName: str

class GoogleCloudMlV1__PredictionOutput(typing_extensions.TypedDict, total=False):
    outputPath: str
    nodeHours: float
    predictionCount: str
    errorCount: str

class GoogleIamV1__AuditLogConfig(typing_extensions.TypedDict, total=False):
    exemptedMembers: typing.List[str]
    logType: typing_extensions.Literal[
        "LOG_TYPE_UNSPECIFIED", "ADMIN_READ", "DATA_WRITE", "DATA_READ"
    ]

class GoogleCloudMlV1__Model(typing_extensions.TypedDict, total=False):
    labels: typing.Dict[str, typing.Any]
    etag: str
    onlinePredictionLogging: bool
    regions: typing.List[str]
    defaultVersion: GoogleCloudMlV1__Version
    name: str
    onlinePredictionConsoleLogging: bool
    description: str

class GoogleType__Expr(typing_extensions.TypedDict, total=False):
    expression: str
    location: str
    description: str
    title: str

class GoogleCloudMlV1__StudyConfig(typing.Dict[str, typing.Any]): ...

class GoogleCloudMlV1_StudyConfigParameterSpec_IntegerValueSpec(
    typing_extensions.TypedDict, total=False
):
    maxValue: str
    minValue: str

class GoogleCloudMlV1__AutomatedStoppingConfig(
    typing_extensions.TypedDict, total=False
):
    medianAutomatedStoppingConfig: GoogleCloudMlV1_AutomatedStoppingConfig_MedianAutomatedStoppingConfig
    decayCurveStoppingConfig: GoogleCloudMlV1_AutomatedStoppingConfig_DecayCurveAutomatedStoppingConfig

class GoogleCloudMlV1__ListModelsResponse(typing_extensions.TypedDict, total=False):
    models: typing.List[GoogleCloudMlV1__Model]
    nextPageToken: str

class GoogleIamV1__Policy(typing_extensions.TypedDict, total=False):
    etag: str
    bindings: typing.List[GoogleIamV1__Binding]
    version: int
    auditConfigs: typing.List[GoogleIamV1__AuditConfig]

class GoogleCloudMlV1__EncryptionConfig(typing_extensions.TypedDict, total=False):
    kmsKeyName: str

class GoogleCloudMlV1__AcceleratorConfig(typing_extensions.TypedDict, total=False):
    count: str
    type: typing_extensions.Literal[
        "ACCELERATOR_TYPE_UNSPECIFIED",
        "NVIDIA_TESLA_K80",
        "NVIDIA_TESLA_P100",
        "NVIDIA_TESLA_V100",
        "NVIDIA_TESLA_P4",
        "NVIDIA_TESLA_T4",
        "TPU_V2",
        "TPU_V3",
    ]

class GoogleCloudMlV1_HyperparameterOutput_HyperparameterMetric(
    typing_extensions.TypedDict, total=False
):
    objectiveValue: float
    trainingStep: str

class GoogleCloudMlV1_StudyConfigParameterSpec_DoubleValueSpec(
    typing_extensions.TypedDict, total=False
):
    maxValue: float
    minValue: float

class GoogleCloudMlV1__CheckTrialEarlyStoppingStateResponse(
    typing_extensions.TypedDict, total=False
):
    shouldStop: bool
    startTime: str
    endTime: str

class GoogleCloudMlV1__Capability(typing_extensions.TypedDict, total=False):
    type: typing_extensions.Literal[
        "TYPE_UNSPECIFIED", "TRAINING", "BATCH_PREDICTION", "ONLINE_PREDICTION"
    ]
    availableAccelerators: typing.List[str]

class GoogleCloudMlV1__Job(typing_extensions.TypedDict, total=False):
    createTime: str
    jobId: str
    etag: str
    errorMessage: str
    endTime: str
    predictionInput: GoogleCloudMlV1__PredictionInput
    state: typing_extensions.Literal[
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
    labels: typing.Dict[str, typing.Any]
    predictionOutput: GoogleCloudMlV1__PredictionOutput
    startTime: str
    trainingOutput: GoogleCloudMlV1__TrainingOutput

class GoogleCloudMlV1__CheckTrialEarlyStoppingStateRequest(
    typing_extensions.TypedDict, total=False
): ...

class GoogleCloudMlV1__ListStudiesResponse(typing_extensions.TypedDict, total=False):
    studies: typing.List[GoogleCloudMlV1__Study]

class GoogleCloudMlV1__OperationMetadata(typing_extensions.TypedDict, total=False):
    version: GoogleCloudMlV1__Version
    isCancellationRequested: bool
    labels: typing.Dict[str, typing.Any]
    createTime: str
    endTime: str
    startTime: str
    operationType: typing_extensions.Literal[
        "OPERATION_TYPE_UNSPECIFIED",
        "CREATE_VERSION",
        "DELETE_VERSION",
        "DELETE_MODEL",
        "UPDATE_MODEL",
        "UPDATE_VERSION",
        "UPDATE_CONFIG",
    ]
    modelName: str
    projectNumber: str

class GoogleIamV1__Binding(typing_extensions.TypedDict, total=False):
    role: str
    members: typing.List[str]
    condition: GoogleType__Expr
    bindingId: str

class GoogleCloudMlV1_StudyConfigParameterSpec_MatchingParentIntValueSpec(
    typing_extensions.TypedDict, total=False
):
    values: typing.List[str]

class GoogleCloudMlV1__PredictRequest(typing_extensions.TypedDict, total=False):
    httpBody: GoogleApi__HttpBody

class GoogleCloudMlV1__ParameterSpec(typing_extensions.TypedDict, total=False):
    maxValue: float
    parameterName: str
    minValue: float
    scaleType: typing_extensions.Literal[
        "NONE", "UNIT_LINEAR_SCALE", "UNIT_LOG_SCALE", "UNIT_REVERSE_LOG_SCALE"
    ]
    categoricalValues: typing.List[str]
    discreteValues: typing.List[float]
    type: typing_extensions.Literal[
        "PARAMETER_TYPE_UNSPECIFIED", "DOUBLE", "INTEGER", "CATEGORICAL", "DISCRETE"
    ]

class GoogleCloudMlV1__CompleteTrialRequest(typing_extensions.TypedDict, total=False):
    finalMeasurement: GoogleCloudMlV1__Measurement
    trialInfeasible: bool
    infeasibleReason: str

class GoogleCloudMlV1_StudyConfig_ParameterSpec(typing.Dict[str, typing.Any]): ...

class GoogleCloudMlV1_AutomatedStoppingConfig_MedianAutomatedStoppingConfig(
    typing_extensions.TypedDict, total=False
):
    useElapsedTime: bool

class GoogleProtobuf__Empty(typing_extensions.TypedDict, total=False): ...

class GoogleCloudMlV1__ListJobsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    jobs: typing.List[GoogleCloudMlV1__Job]

class GoogleCloudMlV1__SampledShapleyAttribution(
    typing_extensions.TypedDict, total=False
):
    numPaths: int

class GoogleCloudMlV1_StudyConfig_MetricSpec(typing_extensions.TypedDict, total=False):
    goal: typing_extensions.Literal["GOAL_TYPE_UNSPECIFIED", "MAXIMIZE", "MINIMIZE"]
    metric: str

class GoogleCloudMlV1__XraiAttribution(typing_extensions.TypedDict, total=False):
    numIntegralSteps: int

class GoogleCloudMlV1__Scheduling(typing_extensions.TypedDict, total=False):
    maxRunningTime: str
    maxWaitTime: str

class GoogleCloudMlV1__TrainingOutput(typing_extensions.TypedDict, total=False):
    trials: typing.List[GoogleCloudMlV1__HyperparameterOutput]
    consumedMLUnits: float
    isHyperparameterTuningJob: bool
    isBuiltInAlgorithmJob: bool
    builtInAlgorithmOutput: GoogleCloudMlV1__BuiltInAlgorithmOutput
    hyperparameterMetricTag: str
    completedTrialCount: str

class GoogleCloudMlV1__AddTrialMeasurementRequest(
    typing_extensions.TypedDict, total=False
):
    measurement: GoogleCloudMlV1__Measurement

class GoogleCloudMlV1__ExplainRequest(typing_extensions.TypedDict, total=False):
    httpBody: GoogleApi__HttpBody

class GoogleCloudMlV1_StudyConfigParameterSpec_MatchingParentCategoricalValueSpec(
    typing_extensions.TypedDict, total=False
):
    values: typing.List[str]

class GoogleCloudMlV1__ContainerSpec(typing_extensions.TypedDict, total=False):
    image: str
    args: typing.List[str]
    ports: typing.List[GoogleCloudMlV1__ContainerPort]
    env: typing.List[GoogleCloudMlV1__EnvVar]
    command: typing.List[str]

class GoogleCloudMlV1__PredictionInput(typing_extensions.TypedDict, total=False):
    batchSize: str
    uri: str
    maxWorkerCount: str
    inputPaths: typing.List[str]
    outputDataFormat: typing_extensions.Literal[
        "DATA_FORMAT_UNSPECIFIED", "JSON", "TEXT", "TF_RECORD", "TF_RECORD_GZIP", "CSV"
    ]
    signatureName: str
    versionName: str
    modelName: str
    runtimeVersion: str
    region: str
    dataFormat: typing_extensions.Literal[
        "DATA_FORMAT_UNSPECIFIED", "JSON", "TEXT", "TF_RECORD", "TF_RECORD_GZIP", "CSV"
    ]
    outputPath: str

class GoogleIamV1__AuditConfig(typing_extensions.TypedDict, total=False):
    auditLogConfigs: typing.List[GoogleIamV1__AuditLogConfig]
    service: str

class GoogleCloudMlV1__RouteMap(typing_extensions.TypedDict, total=False):
    health: str
    predict: str

class GoogleCloudMlV1__SuggestTrialsResponse(typing_extensions.TypedDict, total=False):
    endTime: str
    startTime: str
    trials: typing.List[GoogleCloudMlV1__Trial]
    studyState: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "ACTIVE", "INACTIVE", "COMPLETED"
    ]

class GoogleCloudMlV1__EnvVar(typing_extensions.TypedDict, total=False):
    value: str
    name: str

class GoogleCloudMlV1__ListLocationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    locations: typing.List[GoogleCloudMlV1__Location]

class GoogleCloudMlV1__CancelJobRequest(typing_extensions.TypedDict, total=False): ...

class GoogleCloudMlV1__Version(typing_extensions.TypedDict, total=False):
    pythonVersion: str
    acceleratorConfig: GoogleCloudMlV1__AcceleratorConfig
    predictionClass: str
    description: str
    autoScaling: GoogleCloudMlV1__AutoScaling
    createTime: str
    container: GoogleCloudMlV1__ContainerSpec
    machineType: str
    explanationConfig: GoogleCloudMlV1__ExplanationConfig
    name: str
    errorMessage: str
    state: typing_extensions.Literal[
        "UNKNOWN", "READY", "CREATING", "FAILED", "DELETING", "UPDATING"
    ]
    labels: typing.Dict[str, typing.Any]
    serviceAccount: str
    routes: GoogleCloudMlV1__RouteMap
    isDefault: bool
    etag: str
    framework: typing_extensions.Literal[
        "FRAMEWORK_UNSPECIFIED", "TENSORFLOW", "SCIKIT_LEARN", "XGBOOST"
    ]
    manualScaling: GoogleCloudMlV1__ManualScaling
    requestLoggingConfig: GoogleCloudMlV1__RequestLoggingConfig
    deploymentUri: str
    packageUris: typing.List[str]
    lastUseTime: str
    runtimeVersion: str

class GoogleIamV1__TestIamPermissionsRequest(typing_extensions.TypedDict, total=False):
    permissions: typing.List[str]

class GoogleCloudMlV1_StudyConfigParameterSpec_MatchingParentDiscreteValueSpec(
    typing_extensions.TypedDict, total=False
):
    values: typing.List[float]

class GoogleCloudMlV1__Location(typing_extensions.TypedDict, total=False):
    name: str
    capabilities: typing.List[GoogleCloudMlV1__Capability]

class GoogleCloudMlV1__SetDefaultVersionRequest(
    typing_extensions.TypedDict, total=False
): ...

class GoogleIamV1__TestIamPermissionsResponse(typing_extensions.TypedDict, total=False):
    permissions: typing.List[str]

class GoogleCloudMlV1_Trial_Parameter(typing_extensions.TypedDict, total=False):
    floatValue: float
    parameter: str
    stringValue: str
    intValue: str

class GoogleCloudMlV1__ManualScaling(typing_extensions.TypedDict, total=False):
    nodes: int

class GoogleCloudMlV1__HyperparameterOutput(typing_extensions.TypedDict, total=False):
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "QUEUED",
        "PREPARING",
        "RUNNING",
        "SUCCEEDED",
        "FAILED",
        "CANCELLING",
        "CANCELLED",
    ]
    allMetrics: typing.List[GoogleCloudMlV1_HyperparameterOutput_HyperparameterMetric]
    finalMetric: GoogleCloudMlV1_HyperparameterOutput_HyperparameterMetric
    endTime: str
    trialId: str
    builtInAlgorithmOutput: GoogleCloudMlV1__BuiltInAlgorithmOutput
    startTime: str
    hyperparameters: typing.Dict[str, typing.Any]
    isTrialStoppedEarly: bool

class GoogleCloudMlV1_StudyConfigParameterSpec_CategoricalValueSpec(
    typing_extensions.TypedDict, total=False
):
    values: typing.List[str]

class GoogleCloudMlV1__ContainerPort(typing_extensions.TypedDict, total=False):
    containerPort: int

class GoogleCloudMlV1__GetConfigResponse(typing_extensions.TypedDict, total=False):
    serviceAccount: str
    config: GoogleCloudMlV1__Config
    serviceAccountProject: str

class GoogleCloudMlV1__AutoScaling(typing_extensions.TypedDict, total=False):
    minNodes: int

class GoogleCloudMlV1__HyperparameterSpec(typing_extensions.TypedDict, total=False):
    params: typing.List[GoogleCloudMlV1__ParameterSpec]
    algorithm: typing_extensions.Literal[
        "ALGORITHM_UNSPECIFIED", "GRID_SEARCH", "RANDOM_SEARCH"
    ]
    enableTrialEarlyStopping: bool
    hyperparameterMetricTag: str
    resumePreviousJobId: str
    goal: typing_extensions.Literal["GOAL_TYPE_UNSPECIFIED", "MAXIMIZE", "MINIMIZE"]
    maxFailedTrials: int
    maxTrials: int
    maxParallelTrials: int

class GoogleCloudMlV1__IntegratedGradientsAttribution(
    typing_extensions.TypedDict, total=False
):
    numIntegralSteps: int

class GoogleCloudMlV1__SuggestTrialsRequest(typing_extensions.TypedDict, total=False):
    clientId: str
    suggestionCount: int

class GoogleCloudMlV1__SuggestTrialsMetadata(typing_extensions.TypedDict, total=False):
    suggestionCount: int
    study: str
    createTime: str
    clientId: str

class GoogleIamV1__SetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    policy: GoogleIamV1__Policy
    updateMask: str
