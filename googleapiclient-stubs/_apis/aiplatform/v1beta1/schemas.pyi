import typing

import typing_extensions

_list = list

@typing.type_check_only
class GoogleApiHttpBody(typing_extensions.TypedDict, total=False):
    contentType: str
    data: str
    extensions: _list[dict[str, typing.Any]]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ActiveLearningConfig(
    typing_extensions.TypedDict, total=False
):
    maxDataItemCount: str
    maxDataItemPercentage: int
    sampleConfig: GoogleCloudAiplatformV1beta1SampleConfig
    trainingConfig: GoogleCloudAiplatformV1beta1TrainingConfig

@typing.type_check_only
class GoogleCloudAiplatformV1beta1AddContextArtifactsAndExecutionsRequest(
    typing_extensions.TypedDict, total=False
):
    artifacts: _list[str]
    executions: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1AddContextArtifactsAndExecutionsResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1AddContextChildrenRequest(
    typing_extensions.TypedDict, total=False
):
    childContexts: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1AddContextChildrenResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1AddExecutionEventsRequest(
    typing_extensions.TypedDict, total=False
):
    events: _list[GoogleCloudAiplatformV1beta1Event]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1AddExecutionEventsResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1AddTrialMeasurementRequest(
    typing_extensions.TypedDict, total=False
):
    measurement: GoogleCloudAiplatformV1beta1Measurement

@typing.type_check_only
class GoogleCloudAiplatformV1beta1Annotation(typing_extensions.TypedDict, total=False):
    annotationSource: GoogleCloudAiplatformV1beta1UserActionReference
    createTime: str
    etag: str
    labels: dict[str, typing.Any]
    name: str
    payload: typing.Any
    payloadSchemaUri: str
    updateTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1AnnotationSpec(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    displayName: str
    etag: str
    name: str
    updateTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1Artifact(typing_extensions.TypedDict, total=False):
    createTime: str
    description: str
    displayName: str
    etag: str
    labels: dict[str, typing.Any]
    metadata: dict[str, typing.Any]
    name: str
    schemaTitle: str
    schemaVersion: str
    state: typing_extensions.Literal["STATE_UNSPECIFIED", "PENDING", "LIVE"]
    updateTime: str
    uri: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1AssignNotebookRuntimeOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata
    progressMessage: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1AssignNotebookRuntimeRequest(
    typing_extensions.TypedDict, total=False
):
    notebookRuntime: GoogleCloudAiplatformV1beta1NotebookRuntime
    notebookRuntimeId: str
    notebookRuntimeTemplate: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1Attribution(typing_extensions.TypedDict, total=False):
    approximationError: float
    baselineOutputValue: float
    featureAttributions: typing.Any
    instanceOutputValue: float
    outputDisplayName: str
    outputIndex: _list[int]
    outputName: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1AutomaticResources(
    typing_extensions.TypedDict, total=False
):
    maxReplicaCount: int
    minReplicaCount: int

@typing.type_check_only
class GoogleCloudAiplatformV1beta1AutoscalingMetricSpec(
    typing_extensions.TypedDict, total=False
):
    metricName: str
    target: int

@typing.type_check_only
class GoogleCloudAiplatformV1beta1AvroSource(typing_extensions.TypedDict, total=False):
    gcsSource: GoogleCloudAiplatformV1beta1GcsSource

@typing.type_check_only
class GoogleCloudAiplatformV1beta1BatchCreateFeaturesOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1BatchCreateFeaturesRequest(
    typing_extensions.TypedDict, total=False
):
    requests: _list[GoogleCloudAiplatformV1beta1CreateFeatureRequest]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1BatchCreateFeaturesResponse(
    typing_extensions.TypedDict, total=False
):
    features: _list[GoogleCloudAiplatformV1beta1Feature]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1BatchCreateTensorboardRunsRequest(
    typing_extensions.TypedDict, total=False
):
    requests: _list[GoogleCloudAiplatformV1beta1CreateTensorboardRunRequest]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1BatchCreateTensorboardRunsResponse(
    typing_extensions.TypedDict, total=False
):
    tensorboardRuns: _list[GoogleCloudAiplatformV1beta1TensorboardRun]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1BatchCreateTensorboardTimeSeriesRequest(
    typing_extensions.TypedDict, total=False
):
    requests: _list[GoogleCloudAiplatformV1beta1CreateTensorboardTimeSeriesRequest]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1BatchCreateTensorboardTimeSeriesResponse(
    typing_extensions.TypedDict, total=False
):
    tensorboardTimeSeries: _list[GoogleCloudAiplatformV1beta1TensorboardTimeSeries]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1BatchDedicatedResources(
    typing_extensions.TypedDict, total=False
):
    machineSpec: GoogleCloudAiplatformV1beta1MachineSpec
    maxReplicaCount: int
    startingReplicaCount: int

@typing.type_check_only
class GoogleCloudAiplatformV1beta1BatchImportEvaluatedAnnotationsRequest(
    typing_extensions.TypedDict, total=False
):
    evaluatedAnnotations: _list[GoogleCloudAiplatformV1beta1EvaluatedAnnotation]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1BatchImportEvaluatedAnnotationsResponse(
    typing_extensions.TypedDict, total=False
):
    importedEvaluatedAnnotationsCount: int

@typing.type_check_only
class GoogleCloudAiplatformV1beta1BatchImportModelEvaluationSlicesRequest(
    typing_extensions.TypedDict, total=False
):
    modelEvaluationSlices: _list[GoogleCloudAiplatformV1beta1ModelEvaluationSlice]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1BatchImportModelEvaluationSlicesResponse(
    typing_extensions.TypedDict, total=False
):
    importedModelEvaluationSlices: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1BatchMigrateResourcesOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata
    partialResults: _list[
        GoogleCloudAiplatformV1beta1BatchMigrateResourcesOperationMetadataPartialResult
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1BatchMigrateResourcesOperationMetadataPartialResult(
    typing_extensions.TypedDict, total=False
):
    dataset: str
    error: GoogleRpcStatus
    model: str
    request: GoogleCloudAiplatformV1beta1MigrateResourceRequest

@typing.type_check_only
class GoogleCloudAiplatformV1beta1BatchMigrateResourcesRequest(
    typing_extensions.TypedDict, total=False
):
    migrateResourceRequests: _list[GoogleCloudAiplatformV1beta1MigrateResourceRequest]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1BatchMigrateResourcesResponse(
    typing_extensions.TypedDict, total=False
):
    migrateResourceResponses: _list[GoogleCloudAiplatformV1beta1MigrateResourceResponse]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1BatchPredictionJob(
    typing_extensions.TypedDict, total=False
):
    completionStats: GoogleCloudAiplatformV1beta1CompletionStats
    createTime: str
    dedicatedResources: GoogleCloudAiplatformV1beta1BatchDedicatedResources
    disableContainerLogging: bool
    displayName: str
    encryptionSpec: GoogleCloudAiplatformV1beta1EncryptionSpec
    endTime: str
    error: GoogleRpcStatus
    explanationSpec: GoogleCloudAiplatformV1beta1ExplanationSpec
    generateExplanation: bool
    inputConfig: GoogleCloudAiplatformV1beta1BatchPredictionJobInputConfig
    instanceConfig: GoogleCloudAiplatformV1beta1BatchPredictionJobInstanceConfig
    labels: dict[str, typing.Any]
    manualBatchTuningParameters: GoogleCloudAiplatformV1beta1ManualBatchTuningParameters
    model: str
    modelMonitoringConfig: GoogleCloudAiplatformV1beta1ModelMonitoringConfig
    modelMonitoringStatsAnomalies: _list[
        GoogleCloudAiplatformV1beta1ModelMonitoringStatsAnomalies
    ]
    modelMonitoringStatus: GoogleRpcStatus
    modelParameters: typing.Any
    modelVersionId: str
    name: str
    outputConfig: GoogleCloudAiplatformV1beta1BatchPredictionJobOutputConfig
    outputInfo: GoogleCloudAiplatformV1beta1BatchPredictionJobOutputInfo
    partialFailures: _list[GoogleRpcStatus]
    resourcesConsumed: GoogleCloudAiplatformV1beta1ResourcesConsumed
    serviceAccount: str
    startTime: str
    state: typing_extensions.Literal[
        "JOB_STATE_UNSPECIFIED",
        "JOB_STATE_QUEUED",
        "JOB_STATE_PENDING",
        "JOB_STATE_RUNNING",
        "JOB_STATE_SUCCEEDED",
        "JOB_STATE_FAILED",
        "JOB_STATE_CANCELLING",
        "JOB_STATE_CANCELLED",
        "JOB_STATE_PAUSED",
        "JOB_STATE_EXPIRED",
        "JOB_STATE_UPDATING",
        "JOB_STATE_PARTIALLY_SUCCEEDED",
    ]
    unmanagedContainerModel: GoogleCloudAiplatformV1beta1UnmanagedContainerModel
    updateTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1BatchPredictionJobInputConfig(
    typing_extensions.TypedDict, total=False
):
    bigquerySource: GoogleCloudAiplatformV1beta1BigQuerySource
    gcsSource: GoogleCloudAiplatformV1beta1GcsSource
    instancesFormat: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1BatchPredictionJobInstanceConfig(
    typing_extensions.TypedDict, total=False
):
    excludedFields: _list[str]
    includedFields: _list[str]
    instanceType: str
    keyField: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1BatchPredictionJobOutputConfig(
    typing_extensions.TypedDict, total=False
):
    bigqueryDestination: GoogleCloudAiplatformV1beta1BigQueryDestination
    gcsDestination: GoogleCloudAiplatformV1beta1GcsDestination
    predictionsFormat: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1BatchPredictionJobOutputInfo(
    typing_extensions.TypedDict, total=False
):
    bigqueryOutputDataset: str
    bigqueryOutputTable: str
    gcsOutputDirectory: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1BatchReadFeatureValuesOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1BatchReadFeatureValuesRequest(
    typing_extensions.TypedDict, total=False
):
    bigqueryReadInstances: GoogleCloudAiplatformV1beta1BigQuerySource
    csvReadInstances: GoogleCloudAiplatformV1beta1CsvSource
    destination: GoogleCloudAiplatformV1beta1FeatureValueDestination
    entityTypeSpecs: _list[
        GoogleCloudAiplatformV1beta1BatchReadFeatureValuesRequestEntityTypeSpec
    ]
    passThroughFields: _list[
        GoogleCloudAiplatformV1beta1BatchReadFeatureValuesRequestPassThroughField
    ]
    startTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1BatchReadFeatureValuesRequestEntityTypeSpec(
    typing_extensions.TypedDict, total=False
):
    entityTypeId: str
    featureSelector: GoogleCloudAiplatformV1beta1FeatureSelector
    settings: _list[GoogleCloudAiplatformV1beta1DestinationFeatureSetting]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1BatchReadFeatureValuesRequestPassThroughField(
    typing_extensions.TypedDict, total=False
):
    fieldName: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1BatchReadFeatureValuesResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1BatchReadTensorboardTimeSeriesDataResponse(
    typing_extensions.TypedDict, total=False
):
    timeSeriesData: _list[GoogleCloudAiplatformV1beta1TimeSeriesData]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1BigQueryDestination(
    typing_extensions.TypedDict, total=False
):
    outputUri: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1BigQuerySource(
    typing_extensions.TypedDict, total=False
):
    inputUri: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1BlurBaselineConfig(
    typing_extensions.TypedDict, total=False
):
    maxBlurSigma: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1BoolArray(typing_extensions.TypedDict, total=False):
    values: _list[bool]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CancelBatchPredictionJobRequest(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CancelCustomJobRequest(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CancelDataLabelingJobRequest(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CancelHyperparameterTuningJobRequest(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CancelNasJobRequest(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CancelPipelineJobRequest(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CancelTrainingPipelineRequest(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CheckTrialEarlyStoppingStateMetatdata(
    typing_extensions.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata
    study: str
    trial: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CheckTrialEarlyStoppingStateRequest(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CheckTrialEarlyStoppingStateResponse(
    typing_extensions.TypedDict, total=False
):
    shouldStop: bool

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CompleteTrialRequest(
    typing_extensions.TypedDict, total=False
):
    finalMeasurement: GoogleCloudAiplatformV1beta1Measurement
    infeasibleReason: str
    trialInfeasible: bool

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CompletionStats(
    typing_extensions.TypedDict, total=False
):
    failedCount: str
    incompleteCount: str
    successfulCount: str
    successfulForecastPointCount: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ContainerRegistryDestination(
    typing_extensions.TypedDict, total=False
):
    outputUri: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ContainerSpec(
    typing_extensions.TypedDict, total=False
):
    args: _list[str]
    command: _list[str]
    env: _list[GoogleCloudAiplatformV1beta1EnvVar]
    imageUri: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1Context(typing_extensions.TypedDict, total=False):
    createTime: str
    description: str
    displayName: str
    etag: str
    labels: dict[str, typing.Any]
    metadata: dict[str, typing.Any]
    name: str
    parentContexts: _list[str]
    schemaTitle: str
    schemaVersion: str
    updateTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CopyModelOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CopyModelRequest(
    typing_extensions.TypedDict, total=False
):
    encryptionSpec: GoogleCloudAiplatformV1beta1EncryptionSpec
    modelId: str
    parentModel: str
    sourceModel: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CopyModelResponse(
    typing_extensions.TypedDict, total=False
):
    model: str
    modelVersionId: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CountTokensRequest(
    typing_extensions.TypedDict, total=False
):
    instances: _list[typing.Any]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CountTokensResponse(
    typing_extensions.TypedDict, total=False
):
    totalBillableCharacters: int
    totalTokens: int

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CreateDatasetOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CreateDatasetVersionOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CreateDeploymentResourcePoolOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CreateDeploymentResourcePoolRequest(
    typing_extensions.TypedDict, total=False
):
    deploymentResourcePool: GoogleCloudAiplatformV1beta1DeploymentResourcePool
    deploymentResourcePoolId: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CreateEndpointOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CreateEntityTypeOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CreateExtensionControllerOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CreateExtensionDeploymentOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CreateFeatureOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CreateFeatureRequest(
    typing_extensions.TypedDict, total=False
):
    feature: GoogleCloudAiplatformV1beta1Feature
    featureId: str
    parent: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CreateFeaturestoreOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CreateIndexEndpointOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CreateIndexOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata
    nearestNeighborSearchOperationMetadata: GoogleCloudAiplatformV1beta1NearestNeighborSearchOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CreateMetadataStoreOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CreateNotebookRuntimeTemplateOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CreatePersistentResourceOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CreatePipelineJobRequest(
    typing_extensions.TypedDict, total=False
):
    parent: str
    pipelineJob: GoogleCloudAiplatformV1beta1PipelineJob
    pipelineJobId: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CreateSolverOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CreateSpecialistPoolOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CreateTensorboardOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CreateTensorboardRunRequest(
    typing_extensions.TypedDict, total=False
):
    parent: str
    tensorboardRun: GoogleCloudAiplatformV1beta1TensorboardRun
    tensorboardRunId: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CreateTensorboardTimeSeriesRequest(
    typing_extensions.TypedDict, total=False
):
    parent: str
    tensorboardTimeSeries: GoogleCloudAiplatformV1beta1TensorboardTimeSeries
    tensorboardTimeSeriesId: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CsvDestination(
    typing_extensions.TypedDict, total=False
):
    gcsDestination: GoogleCloudAiplatformV1beta1GcsDestination

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CsvSource(typing_extensions.TypedDict, total=False):
    gcsSource: GoogleCloudAiplatformV1beta1GcsSource

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CustomJob(typing_extensions.TypedDict, total=False):
    createTime: str
    displayName: str
    encryptionSpec: GoogleCloudAiplatformV1beta1EncryptionSpec
    endTime: str
    error: GoogleRpcStatus
    jobSpec: GoogleCloudAiplatformV1beta1CustomJobSpec
    labels: dict[str, typing.Any]
    name: str
    startTime: str
    state: typing_extensions.Literal[
        "JOB_STATE_UNSPECIFIED",
        "JOB_STATE_QUEUED",
        "JOB_STATE_PENDING",
        "JOB_STATE_RUNNING",
        "JOB_STATE_SUCCEEDED",
        "JOB_STATE_FAILED",
        "JOB_STATE_CANCELLING",
        "JOB_STATE_CANCELLED",
        "JOB_STATE_PAUSED",
        "JOB_STATE_EXPIRED",
        "JOB_STATE_UPDATING",
        "JOB_STATE_PARTIALLY_SUCCEEDED",
    ]
    updateTime: str
    webAccessUris: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CustomJobSpec(
    typing_extensions.TypedDict, total=False
):
    baseOutputDirectory: GoogleCloudAiplatformV1beta1GcsDestination
    enableDashboardAccess: bool
    enableWebAccess: bool
    experiment: str
    experimentRun: str
    network: str
    persistentResourceId: str
    reservedIpRanges: _list[str]
    scheduling: GoogleCloudAiplatformV1beta1Scheduling
    serviceAccount: str
    tensorboard: str
    workerPoolSpecs: _list[GoogleCloudAiplatformV1beta1WorkerPoolSpec]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1DataItem(typing_extensions.TypedDict, total=False):
    createTime: str
    etag: str
    labels: dict[str, typing.Any]
    name: str
    payload: typing.Any
    updateTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1DataItemView(
    typing_extensions.TypedDict, total=False
):
    annotations: _list[GoogleCloudAiplatformV1beta1Annotation]
    dataItem: GoogleCloudAiplatformV1beta1DataItem
    hasTruncatedAnnotations: bool

@typing.type_check_only
class GoogleCloudAiplatformV1beta1DataLabelingJob(
    typing_extensions.TypedDict, total=False
):
    activeLearningConfig: GoogleCloudAiplatformV1beta1ActiveLearningConfig
    annotationLabels: dict[str, typing.Any]
    createTime: str
    currentSpend: GoogleTypeMoney
    datasets: _list[str]
    displayName: str
    encryptionSpec: GoogleCloudAiplatformV1beta1EncryptionSpec
    error: GoogleRpcStatus
    inputs: typing.Any
    inputsSchemaUri: str
    instructionUri: str
    labelerCount: int
    labelingProgress: int
    labels: dict[str, typing.Any]
    name: str
    specialistPools: _list[str]
    state: typing_extensions.Literal[
        "JOB_STATE_UNSPECIFIED",
        "JOB_STATE_QUEUED",
        "JOB_STATE_PENDING",
        "JOB_STATE_RUNNING",
        "JOB_STATE_SUCCEEDED",
        "JOB_STATE_FAILED",
        "JOB_STATE_CANCELLING",
        "JOB_STATE_CANCELLED",
        "JOB_STATE_PAUSED",
        "JOB_STATE_EXPIRED",
        "JOB_STATE_UPDATING",
        "JOB_STATE_PARTIALLY_SUCCEEDED",
    ]
    updateTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1Dataset(typing_extensions.TypedDict, total=False):
    createTime: str
    dataItemCount: str
    description: str
    displayName: str
    encryptionSpec: GoogleCloudAiplatformV1beta1EncryptionSpec
    etag: str
    labels: dict[str, typing.Any]
    metadata: typing.Any
    metadataArtifact: str
    metadataSchemaUri: str
    name: str
    savedQueries: _list[GoogleCloudAiplatformV1beta1SavedQuery]
    updateTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1DatasetVersion(
    typing_extensions.TypedDict, total=False
):
    bigQueryDatasetName: str
    createTime: str
    etag: str
    name: str
    updateTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1DedicatedResources(
    typing_extensions.TypedDict, total=False
):
    autoscalingMetricSpecs: _list[GoogleCloudAiplatformV1beta1AutoscalingMetricSpec]
    machineSpec: GoogleCloudAiplatformV1beta1MachineSpec
    maxReplicaCount: int
    minReplicaCount: int

@typing.type_check_only
class GoogleCloudAiplatformV1beta1DeleteFeatureValuesOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1DeleteFeatureValuesRequest(
    typing_extensions.TypedDict, total=False
):
    selectEntity: GoogleCloudAiplatformV1beta1DeleteFeatureValuesRequestSelectEntity
    selectTimeRangeAndFeature: GoogleCloudAiplatformV1beta1DeleteFeatureValuesRequestSelectTimeRangeAndFeature

@typing.type_check_only
class GoogleCloudAiplatformV1beta1DeleteFeatureValuesRequestSelectEntity(
    typing_extensions.TypedDict, total=False
):
    entityIdSelector: GoogleCloudAiplatformV1beta1EntityIdSelector

@typing.type_check_only
class GoogleCloudAiplatformV1beta1DeleteFeatureValuesRequestSelectTimeRangeAndFeature(
    typing_extensions.TypedDict, total=False
):
    featureSelector: GoogleCloudAiplatformV1beta1FeatureSelector
    skipOnlineStorageDelete: bool
    timeRange: GoogleTypeInterval

@typing.type_check_only
class GoogleCloudAiplatformV1beta1DeleteFeatureValuesResponse(
    typing_extensions.TypedDict, total=False
):
    selectEntity: GoogleCloudAiplatformV1beta1DeleteFeatureValuesResponseSelectEntity
    selectTimeRangeAndFeature: GoogleCloudAiplatformV1beta1DeleteFeatureValuesResponseSelectTimeRangeAndFeature

@typing.type_check_only
class GoogleCloudAiplatformV1beta1DeleteFeatureValuesResponseSelectEntity(
    typing_extensions.TypedDict, total=False
):
    offlineStorageDeletedEntityRowCount: str
    onlineStorageDeletedEntityCount: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1DeleteFeatureValuesResponseSelectTimeRangeAndFeature(
    typing_extensions.TypedDict, total=False
):
    impactedFeatureCount: str
    offlineStorageModifiedEntityRowCount: str
    onlineStorageModifiedEntityCount: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1DeleteMetadataStoreOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1DeleteOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1DeployIndexOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    deployedIndexId: str
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1DeployIndexRequest(
    typing_extensions.TypedDict, total=False
):
    deployedIndex: GoogleCloudAiplatformV1beta1DeployedIndex

@typing.type_check_only
class GoogleCloudAiplatformV1beta1DeployIndexResponse(
    typing_extensions.TypedDict, total=False
):
    deployedIndex: GoogleCloudAiplatformV1beta1DeployedIndex

@typing.type_check_only
class GoogleCloudAiplatformV1beta1DeployModelOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1DeployModelRequest(
    typing_extensions.TypedDict, total=False
):
    deployedModel: GoogleCloudAiplatformV1beta1DeployedModel
    trafficSplit: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1DeployModelResponse(
    typing_extensions.TypedDict, total=False
):
    deployedModel: GoogleCloudAiplatformV1beta1DeployedModel

@typing.type_check_only
class GoogleCloudAiplatformV1beta1DeploySolverOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1DeployedIndex(
    typing_extensions.TypedDict, total=False
):
    automaticResources: GoogleCloudAiplatformV1beta1AutomaticResources
    createTime: str
    dedicatedResources: GoogleCloudAiplatformV1beta1DedicatedResources
    deployedIndexAuthConfig: GoogleCloudAiplatformV1beta1DeployedIndexAuthConfig
    deploymentGroup: str
    displayName: str
    enableAccessLogging: bool
    id: str
    index: str
    indexSyncTime: str
    privateEndpoints: GoogleCloudAiplatformV1beta1IndexPrivateEndpoints
    reservedIpRanges: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1DeployedIndexAuthConfig(
    typing_extensions.TypedDict, total=False
):
    authProvider: GoogleCloudAiplatformV1beta1DeployedIndexAuthConfigAuthProvider

@typing.type_check_only
class GoogleCloudAiplatformV1beta1DeployedIndexAuthConfigAuthProvider(
    typing_extensions.TypedDict, total=False
):
    allowedIssuers: _list[str]
    audiences: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1DeployedIndexRef(
    typing_extensions.TypedDict, total=False
):
    deployedIndexId: str
    indexEndpoint: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1DeployedModel(
    typing_extensions.TypedDict, total=False
):
    automaticResources: GoogleCloudAiplatformV1beta1AutomaticResources
    createTime: str
    dedicatedResources: GoogleCloudAiplatformV1beta1DedicatedResources
    disableExplanations: bool
    displayName: str
    enableAccessLogging: bool
    enableContainerLogging: bool
    explanationSpec: GoogleCloudAiplatformV1beta1ExplanationSpec
    id: str
    model: str
    modelVersionId: str
    privateEndpoints: GoogleCloudAiplatformV1beta1PrivateEndpoints
    serviceAccount: str
    sharedResources: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1DeployedModelRef(
    typing_extensions.TypedDict, total=False
):
    deployedModelId: str
    endpoint: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1DeploymentResourcePool(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    dedicatedResources: GoogleCloudAiplatformV1beta1DedicatedResources
    name: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1DestinationFeatureSetting(
    typing_extensions.TypedDict, total=False
):
    destinationField: str
    featureId: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1DiskSpec(typing_extensions.TypedDict, total=False):
    bootDiskSizeGb: int
    bootDiskType: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1DoubleArray(typing_extensions.TypedDict, total=False):
    values: _list[float]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1EncryptionSpec(
    typing_extensions.TypedDict, total=False
):
    kmsKeyName: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1Endpoint(typing_extensions.TypedDict, total=False):
    createTime: str
    deployedModels: _list[GoogleCloudAiplatformV1beta1DeployedModel]
    description: str
    displayName: str
    enablePrivateServiceConnect: bool
    encryptionSpec: GoogleCloudAiplatformV1beta1EncryptionSpec
    etag: str
    labels: dict[str, typing.Any]
    modelDeploymentMonitoringJob: str
    name: str
    network: str
    predictRequestResponseLoggingConfig: GoogleCloudAiplatformV1beta1PredictRequestResponseLoggingConfig
    trafficSplit: dict[str, typing.Any]
    updateTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1EntityIdSelector(
    typing_extensions.TypedDict, total=False
):
    csvSource: GoogleCloudAiplatformV1beta1CsvSource
    entityIdField: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1EntityType(typing_extensions.TypedDict, total=False):
    createTime: str
    description: str
    etag: str
    labels: dict[str, typing.Any]
    monitoringConfig: GoogleCloudAiplatformV1beta1FeaturestoreMonitoringConfig
    name: str
    offlineStorageTtlDays: int
    updateTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1EnvVar(typing_extensions.TypedDict, total=False):
    name: str
    value: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ErrorAnalysisAnnotation(
    typing_extensions.TypedDict, total=False
):
    attributedItems: _list[
        GoogleCloudAiplatformV1beta1ErrorAnalysisAnnotationAttributedItem
    ]
    outlierScore: float
    outlierThreshold: float
    queryType: typing_extensions.Literal[
        "QUERY_TYPE_UNSPECIFIED",
        "ALL_SIMILAR",
        "SAME_CLASS_SIMILAR",
        "SAME_CLASS_DISSIMILAR",
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ErrorAnalysisAnnotationAttributedItem(
    typing_extensions.TypedDict, total=False
):
    annotationResourceName: str
    distance: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1EvaluatedAnnotation(
    typing_extensions.TypedDict, total=False
):
    dataItemPayload: typing.Any
    errorAnalysisAnnotations: _list[GoogleCloudAiplatformV1beta1ErrorAnalysisAnnotation]
    evaluatedDataItemViewId: str
    explanations: _list[GoogleCloudAiplatformV1beta1EvaluatedAnnotationExplanation]
    groundTruths: _list[typing.Any]
    predictions: _list[typing.Any]
    type: typing_extensions.Literal[
        "EVALUATED_ANNOTATION_TYPE_UNSPECIFIED",
        "TRUE_POSITIVE",
        "FALSE_POSITIVE",
        "FALSE_NEGATIVE",
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1EvaluatedAnnotationExplanation(
    typing_extensions.TypedDict, total=False
):
    explanation: GoogleCloudAiplatformV1beta1Explanation
    explanationType: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1Event(typing_extensions.TypedDict, total=False):
    artifact: str
    eventTime: str
    execution: str
    labels: dict[str, typing.Any]
    type: typing_extensions.Literal["TYPE_UNSPECIFIED", "INPUT", "OUTPUT"]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1Examples(typing_extensions.TypedDict, total=False):
    exampleGcsSource: GoogleCloudAiplatformV1beta1ExamplesExampleGcsSource
    gcsSource: GoogleCloudAiplatformV1beta1GcsSource
    nearestNeighborSearchConfig: typing.Any
    neighborCount: int
    presets: GoogleCloudAiplatformV1beta1Presets

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ExamplesExampleGcsSource(
    typing_extensions.TypedDict, total=False
):
    dataFormat: typing_extensions.Literal["DATA_FORMAT_UNSPECIFIED", "JSONL"]
    gcsSource: GoogleCloudAiplatformV1beta1GcsSource

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ExamplesOverride(
    typing_extensions.TypedDict, total=False
):
    crowdingCount: int
    dataFormat: typing_extensions.Literal[
        "DATA_FORMAT_UNSPECIFIED", "INSTANCES", "EMBEDDINGS"
    ]
    neighborCount: int
    restrictions: _list[GoogleCloudAiplatformV1beta1ExamplesRestrictionsNamespace]
    returnEmbeddings: bool

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ExamplesRestrictionsNamespace(
    typing_extensions.TypedDict, total=False
):
    allow: _list[str]
    deny: _list[str]
    namespaceName: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1Execution(typing_extensions.TypedDict, total=False):
    createTime: str
    description: str
    displayName: str
    etag: str
    labels: dict[str, typing.Any]
    metadata: dict[str, typing.Any]
    name: str
    schemaTitle: str
    schemaVersion: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "NEW",
        "RUNNING",
        "COMPLETE",
        "FAILED",
        "CACHED",
        "CANCELLED",
    ]
    updateTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ExplainRequest(
    typing_extensions.TypedDict, total=False
):
    deployedModelId: str
    explanationSpecOverride: GoogleCloudAiplatformV1beta1ExplanationSpecOverride
    instances: _list[typing.Any]
    parameters: typing.Any

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ExplainResponse(
    typing_extensions.TypedDict, total=False
):
    deployedModelId: str
    explanations: _list[GoogleCloudAiplatformV1beta1Explanation]
    predictions: _list[typing.Any]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1Explanation(typing_extensions.TypedDict, total=False):
    attributions: _list[GoogleCloudAiplatformV1beta1Attribution]
    neighbors: _list[GoogleCloudAiplatformV1beta1Neighbor]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ExplanationMetadata(
    typing_extensions.TypedDict, total=False
):
    featureAttributionsSchemaUri: str
    inputs: dict[str, typing.Any]
    latentSpaceSource: str
    outputs: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ExplanationMetadataInputMetadata(
    typing_extensions.TypedDict, total=False
):
    denseShapeTensorName: str
    encodedBaselines: _list[typing.Any]
    encodedTensorName: str
    encoding: typing_extensions.Literal[
        "ENCODING_UNSPECIFIED",
        "IDENTITY",
        "BAG_OF_FEATURES",
        "BAG_OF_FEATURES_SPARSE",
        "INDICATOR",
        "COMBINED_EMBEDDING",
        "CONCAT_EMBEDDING",
    ]
    featureValueDomain: GoogleCloudAiplatformV1beta1ExplanationMetadataInputMetadataFeatureValueDomain
    groupName: str
    indexFeatureMapping: _list[str]
    indicesTensorName: str
    inputBaselines: _list[typing.Any]
    inputTensorName: str
    modality: str
    visualization: GoogleCloudAiplatformV1beta1ExplanationMetadataInputMetadataVisualization

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ExplanationMetadataInputMetadataFeatureValueDomain(
    typing_extensions.TypedDict, total=False
):
    maxValue: float
    minValue: float
    originalMean: float
    originalStddev: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ExplanationMetadataInputMetadataVisualization(
    typing_extensions.TypedDict, total=False
):
    clipPercentLowerbound: float
    clipPercentUpperbound: float
    colorMap: typing_extensions.Literal[
        "COLOR_MAP_UNSPECIFIED",
        "PINK_GREEN",
        "VIRIDIS",
        "RED",
        "GREEN",
        "RED_GREEN",
        "PINK_WHITE_GREEN",
    ]
    overlayType: typing_extensions.Literal[
        "OVERLAY_TYPE_UNSPECIFIED", "NONE", "ORIGINAL", "GRAYSCALE", "MASK_BLACK"
    ]
    polarity: typing_extensions.Literal[
        "POLARITY_UNSPECIFIED", "POSITIVE", "NEGATIVE", "BOTH"
    ]
    type: typing_extensions.Literal["TYPE_UNSPECIFIED", "PIXELS", "OUTLINES"]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ExplanationMetadataOutputMetadata(
    typing_extensions.TypedDict, total=False
):
    displayNameMappingKey: str
    indexDisplayNameMapping: typing.Any
    outputTensorName: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ExplanationMetadataOverride(
    typing_extensions.TypedDict, total=False
):
    inputs: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ExplanationMetadataOverrideInputMetadataOverride(
    typing_extensions.TypedDict, total=False
):
    inputBaselines: _list[typing.Any]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ExplanationParameters(
    typing_extensions.TypedDict, total=False
):
    examples: GoogleCloudAiplatformV1beta1Examples
    integratedGradientsAttribution: GoogleCloudAiplatformV1beta1IntegratedGradientsAttribution
    outputIndices: _list[typing.Any]
    sampledShapleyAttribution: GoogleCloudAiplatformV1beta1SampledShapleyAttribution
    topK: int
    xraiAttribution: GoogleCloudAiplatformV1beta1XraiAttribution

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ExplanationSpec(
    typing_extensions.TypedDict, total=False
):
    metadata: GoogleCloudAiplatformV1beta1ExplanationMetadata
    parameters: GoogleCloudAiplatformV1beta1ExplanationParameters

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ExplanationSpecOverride(
    typing_extensions.TypedDict, total=False
):
    examplesOverride: GoogleCloudAiplatformV1beta1ExamplesOverride
    metadata: GoogleCloudAiplatformV1beta1ExplanationMetadataOverride
    parameters: GoogleCloudAiplatformV1beta1ExplanationParameters

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ExportDataConfig(
    typing_extensions.TypedDict, total=False
):
    annotationsFilter: str
    filterSplit: GoogleCloudAiplatformV1beta1ExportFilterSplit
    fractionSplit: GoogleCloudAiplatformV1beta1ExportFractionSplit
    gcsDestination: GoogleCloudAiplatformV1beta1GcsDestination

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ExportDataOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    gcsOutputDirectory: str
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ExportDataRequest(
    typing_extensions.TypedDict, total=False
):
    exportConfig: GoogleCloudAiplatformV1beta1ExportDataConfig

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ExportDataResponse(
    typing_extensions.TypedDict, total=False
):
    exportedFiles: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ExportEndpointOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ExportEndpointResponse(
    typing_extensions.TypedDict, total=False
):
    outputInfo: GoogleCloudAiplatformV1beta1ExportEndpointResponseOutputInfo

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ExportEndpointResponseOutputInfo(
    typing_extensions.TypedDict, total=False
):
    bigQueryDestination: GoogleCloudAiplatformV1beta1BigQueryDestination

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ExportFeatureValuesOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ExportFeatureValuesRequest(
    typing_extensions.TypedDict, total=False
):
    destination: GoogleCloudAiplatformV1beta1FeatureValueDestination
    featureSelector: GoogleCloudAiplatformV1beta1FeatureSelector
    fullExport: GoogleCloudAiplatformV1beta1ExportFeatureValuesRequestFullExport
    settings: _list[GoogleCloudAiplatformV1beta1DestinationFeatureSetting]
    snapshotExport: GoogleCloudAiplatformV1beta1ExportFeatureValuesRequestSnapshotExport

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ExportFeatureValuesRequestFullExport(
    typing_extensions.TypedDict, total=False
):
    endTime: str
    startTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ExportFeatureValuesRequestSnapshotExport(
    typing_extensions.TypedDict, total=False
):
    snapshotTime: str
    startTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ExportFeatureValuesResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ExportFilterSplit(
    typing_extensions.TypedDict, total=False
):
    testFilter: str
    trainingFilter: str
    validationFilter: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ExportFractionSplit(
    typing_extensions.TypedDict, total=False
):
    testFraction: float
    trainingFraction: float
    validationFraction: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ExportModelOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata
    outputInfo: GoogleCloudAiplatformV1beta1ExportModelOperationMetadataOutputInfo

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ExportModelOperationMetadataOutputInfo(
    typing_extensions.TypedDict, total=False
):
    artifactOutputUri: str
    imageOutputUri: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ExportModelRequest(
    typing_extensions.TypedDict, total=False
):
    outputConfig: GoogleCloudAiplatformV1beta1ExportModelRequestOutputConfig

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ExportModelRequestOutputConfig(
    typing_extensions.TypedDict, total=False
):
    artifactDestination: GoogleCloudAiplatformV1beta1GcsDestination
    exportFormatId: str
    imageDestination: GoogleCloudAiplatformV1beta1ContainerRegistryDestination

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ExportModelResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ExportTensorboardTimeSeriesDataRequest(
    typing_extensions.TypedDict, total=False
):
    filter: str
    orderBy: str
    pageSize: int
    pageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ExportTensorboardTimeSeriesDataResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    timeSeriesDataPoints: _list[GoogleCloudAiplatformV1beta1TimeSeriesDataPoint]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1Feature(typing_extensions.TypedDict, total=False):
    createTime: str
    description: str
    disableMonitoring: bool
    etag: str
    labels: dict[str, typing.Any]
    monitoringConfig: GoogleCloudAiplatformV1beta1FeaturestoreMonitoringConfig
    monitoringStats: _list[GoogleCloudAiplatformV1beta1FeatureStatsAnomaly]
    monitoringStatsAnomalies: _list[
        GoogleCloudAiplatformV1beta1FeatureMonitoringStatsAnomaly
    ]
    name: str
    updateTime: str
    valueType: typing_extensions.Literal[
        "VALUE_TYPE_UNSPECIFIED",
        "BOOL",
        "BOOL_ARRAY",
        "DOUBLE",
        "DOUBLE_ARRAY",
        "INT64",
        "INT64_ARRAY",
        "STRING",
        "STRING_ARRAY",
        "BYTES",
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1FeatureMonitoringStatsAnomaly(
    typing_extensions.TypedDict, total=False
):
    featureStatsAnomaly: GoogleCloudAiplatformV1beta1FeatureStatsAnomaly
    objective: typing_extensions.Literal[
        "OBJECTIVE_UNSPECIFIED", "IMPORT_FEATURE_ANALYSIS", "SNAPSHOT_ANALYSIS"
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1FeatureNoiseSigma(
    typing_extensions.TypedDict, total=False
):
    noiseSigma: _list[GoogleCloudAiplatformV1beta1FeatureNoiseSigmaNoiseSigmaForFeature]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1FeatureNoiseSigmaNoiseSigmaForFeature(
    typing_extensions.TypedDict, total=False
):
    name: str
    sigma: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1FeatureSelector(
    typing_extensions.TypedDict, total=False
):
    idMatcher: GoogleCloudAiplatformV1beta1IdMatcher

@typing.type_check_only
class GoogleCloudAiplatformV1beta1FeatureStatsAnomaly(
    typing_extensions.TypedDict, total=False
):
    anomalyDetectionThreshold: float
    anomalyUri: str
    distributionDeviation: float
    endTime: str
    score: float
    startTime: str
    statsUri: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1FeatureValue(
    typing_extensions.TypedDict, total=False
):
    boolArrayValue: GoogleCloudAiplatformV1beta1BoolArray
    boolValue: bool
    bytesValue: str
    doubleArrayValue: GoogleCloudAiplatformV1beta1DoubleArray
    doubleValue: float
    int64ArrayValue: GoogleCloudAiplatformV1beta1Int64Array
    int64Value: str
    metadata: GoogleCloudAiplatformV1beta1FeatureValueMetadata
    stringArrayValue: GoogleCloudAiplatformV1beta1StringArray
    stringValue: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1FeatureValueDestination(
    typing_extensions.TypedDict, total=False
):
    bigqueryDestination: GoogleCloudAiplatformV1beta1BigQueryDestination
    csvDestination: GoogleCloudAiplatformV1beta1CsvDestination
    tfrecordDestination: GoogleCloudAiplatformV1beta1TFRecordDestination

@typing.type_check_only
class GoogleCloudAiplatformV1beta1FeatureValueList(
    typing_extensions.TypedDict, total=False
):
    values: _list[GoogleCloudAiplatformV1beta1FeatureValue]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1FeatureValueMetadata(
    typing_extensions.TypedDict, total=False
):
    generateTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1Featurestore(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    encryptionSpec: GoogleCloudAiplatformV1beta1EncryptionSpec
    etag: str
    labels: dict[str, typing.Any]
    name: str
    onlineServingConfig: GoogleCloudAiplatformV1beta1FeaturestoreOnlineServingConfig
    onlineStorageTtlDays: int
    state: typing_extensions.Literal["STATE_UNSPECIFIED", "STABLE", "UPDATING"]
    updateTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1FeaturestoreMonitoringConfig(
    typing_extensions.TypedDict, total=False
):
    categoricalThresholdConfig: GoogleCloudAiplatformV1beta1FeaturestoreMonitoringConfigThresholdConfig
    importFeaturesAnalysis: GoogleCloudAiplatformV1beta1FeaturestoreMonitoringConfigImportFeaturesAnalysis
    numericalThresholdConfig: GoogleCloudAiplatformV1beta1FeaturestoreMonitoringConfigThresholdConfig
    snapshotAnalysis: GoogleCloudAiplatformV1beta1FeaturestoreMonitoringConfigSnapshotAnalysis

@typing.type_check_only
class GoogleCloudAiplatformV1beta1FeaturestoreMonitoringConfigImportFeaturesAnalysis(
    typing_extensions.TypedDict, total=False
):
    anomalyDetectionBaseline: typing_extensions.Literal[
        "BASELINE_UNSPECIFIED",
        "LATEST_STATS",
        "MOST_RECENT_SNAPSHOT_STATS",
        "PREVIOUS_IMPORT_FEATURES_STATS",
    ]
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "DEFAULT", "ENABLED", "DISABLED"
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1FeaturestoreMonitoringConfigSnapshotAnalysis(
    typing_extensions.TypedDict, total=False
):
    disabled: bool
    monitoringInterval: str
    monitoringIntervalDays: int
    stalenessDays: int

@typing.type_check_only
class GoogleCloudAiplatformV1beta1FeaturestoreMonitoringConfigThresholdConfig(
    typing_extensions.TypedDict, total=False
):
    value: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1FeaturestoreOnlineServingConfig(
    typing_extensions.TypedDict, total=False
):
    fixedNodeCount: int
    scaling: GoogleCloudAiplatformV1beta1FeaturestoreOnlineServingConfigScaling

@typing.type_check_only
class GoogleCloudAiplatformV1beta1FeaturestoreOnlineServingConfigScaling(
    typing_extensions.TypedDict, total=False
):
    cpuUtilizationTarget: int
    maxNodeCount: int
    minNodeCount: int

@typing.type_check_only
class GoogleCloudAiplatformV1beta1FilterSplit(typing_extensions.TypedDict, total=False):
    testFilter: str
    trainingFilter: str
    validationFilter: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1FindNeighborsRequest(
    typing_extensions.TypedDict, total=False
):
    deployedIndexId: str
    queries: _list[GoogleCloudAiplatformV1beta1FindNeighborsRequestQuery]
    returnFullDatapoint: bool

@typing.type_check_only
class GoogleCloudAiplatformV1beta1FindNeighborsRequestQuery(
    typing_extensions.TypedDict, total=False
):
    approximateNeighborCount: int
    datapoint: GoogleCloudAiplatformV1beta1IndexDatapoint
    fractionLeafNodesToSearchOverride: float
    neighborCount: int
    perCrowdingAttributeNeighborCount: int

@typing.type_check_only
class GoogleCloudAiplatformV1beta1FindNeighborsResponse(
    typing_extensions.TypedDict, total=False
):
    nearestNeighbors: _list[
        GoogleCloudAiplatformV1beta1FindNeighborsResponseNearestNeighbors
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1FindNeighborsResponseNearestNeighbors(
    typing_extensions.TypedDict, total=False
):
    id: str
    neighbors: _list[GoogleCloudAiplatformV1beta1FindNeighborsResponseNeighbor]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1FindNeighborsResponseNeighbor(
    typing_extensions.TypedDict, total=False
):
    datapoint: GoogleCloudAiplatformV1beta1IndexDatapoint
    distance: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1FractionSplit(
    typing_extensions.TypedDict, total=False
):
    testFraction: float
    trainingFraction: float
    validationFraction: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1GcsDestination(
    typing_extensions.TypedDict, total=False
):
    outputUriPrefix: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1GcsSource(typing_extensions.TypedDict, total=False):
    uris: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1GenerateAccessTokenRequest(
    typing_extensions.TypedDict, total=False
):
    vmToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1GenerateAccessTokenResponse(
    typing_extensions.TypedDict, total=False
):
    accessToken: str
    expiresIn: int
    scope: str
    tokenType: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1GenericOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    partialFailures: _list[GoogleRpcStatus]
    updateTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1HyperparameterTuningJob(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    displayName: str
    encryptionSpec: GoogleCloudAiplatformV1beta1EncryptionSpec
    endTime: str
    error: GoogleRpcStatus
    labels: dict[str, typing.Any]
    maxFailedTrialCount: int
    maxTrialCount: int
    name: str
    parallelTrialCount: int
    startTime: str
    state: typing_extensions.Literal[
        "JOB_STATE_UNSPECIFIED",
        "JOB_STATE_QUEUED",
        "JOB_STATE_PENDING",
        "JOB_STATE_RUNNING",
        "JOB_STATE_SUCCEEDED",
        "JOB_STATE_FAILED",
        "JOB_STATE_CANCELLING",
        "JOB_STATE_CANCELLED",
        "JOB_STATE_PAUSED",
        "JOB_STATE_EXPIRED",
        "JOB_STATE_UPDATING",
        "JOB_STATE_PARTIALLY_SUCCEEDED",
    ]
    studySpec: GoogleCloudAiplatformV1beta1StudySpec
    trialJobSpec: GoogleCloudAiplatformV1beta1CustomJobSpec
    trials: _list[GoogleCloudAiplatformV1beta1Trial]
    updateTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1IdMatcher(typing_extensions.TypedDict, total=False):
    ids: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ImportDataConfig(
    typing_extensions.TypedDict, total=False
):
    annotationLabels: dict[str, typing.Any]
    dataItemLabels: dict[str, typing.Any]
    gcsSource: GoogleCloudAiplatformV1beta1GcsSource
    importSchemaUri: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ImportDataOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ImportDataRequest(
    typing_extensions.TypedDict, total=False
):
    importConfigs: _list[GoogleCloudAiplatformV1beta1ImportDataConfig]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ImportDataResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ImportExtensionOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ImportFeatureValuesOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    blockingOperationIds: _list[str]
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata
    importedEntityCount: str
    importedFeatureValueCount: str
    invalidRowCount: str
    sourceUris: _list[str]
    timestampOutsideRetentionRowsCount: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ImportFeatureValuesRequest(
    typing_extensions.TypedDict, total=False
):
    avroSource: GoogleCloudAiplatformV1beta1AvroSource
    bigquerySource: GoogleCloudAiplatformV1beta1BigQuerySource
    csvSource: GoogleCloudAiplatformV1beta1CsvSource
    disableIngestionAnalysis: bool
    disableOnlineServing: bool
    entityIdField: str
    featureSpecs: _list[
        GoogleCloudAiplatformV1beta1ImportFeatureValuesRequestFeatureSpec
    ]
    featureTime: str
    featureTimeField: str
    workerCount: int

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ImportFeatureValuesRequestFeatureSpec(
    typing_extensions.TypedDict, total=False
):
    id: str
    sourceField: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ImportFeatureValuesResponse(
    typing_extensions.TypedDict, total=False
):
    importedEntityCount: str
    importedFeatureValueCount: str
    invalidRowCount: str
    timestampOutsideRetentionRowsCount: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ImportModelEvaluationRequest(
    typing_extensions.TypedDict, total=False
):
    modelEvaluation: GoogleCloudAiplatformV1beta1ModelEvaluation

@typing.type_check_only
class GoogleCloudAiplatformV1beta1Index(typing_extensions.TypedDict, total=False):
    createTime: str
    deployedIndexes: _list[GoogleCloudAiplatformV1beta1DeployedIndexRef]
    description: str
    displayName: str
    encryptionSpec: GoogleCloudAiplatformV1beta1EncryptionSpec
    etag: str
    indexStats: GoogleCloudAiplatformV1beta1IndexStats
    indexUpdateMethod: typing_extensions.Literal[
        "INDEX_UPDATE_METHOD_UNSPECIFIED", "BATCH_UPDATE", "STREAM_UPDATE"
    ]
    labels: dict[str, typing.Any]
    metadata: typing.Any
    metadataSchemaUri: str
    name: str
    updateTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1IndexDatapoint(
    typing_extensions.TypedDict, total=False
):
    crowdingTag: GoogleCloudAiplatformV1beta1IndexDatapointCrowdingTag
    datapointId: str
    featureVector: _list[float]
    restricts: _list[GoogleCloudAiplatformV1beta1IndexDatapointRestriction]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1IndexDatapointCrowdingTag(
    typing_extensions.TypedDict, total=False
):
    crowdingAttribute: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1IndexDatapointRestriction(
    typing_extensions.TypedDict, total=False
):
    allowList: _list[str]
    denyList: _list[str]
    namespace: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1IndexEndpoint(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    deployedIndexes: _list[GoogleCloudAiplatformV1beta1DeployedIndex]
    description: str
    displayName: str
    enablePrivateServiceConnect: bool
    encryptionSpec: GoogleCloudAiplatformV1beta1EncryptionSpec
    etag: str
    labels: dict[str, typing.Any]
    name: str
    network: str
    privateServiceConnectConfig: GoogleCloudAiplatformV1beta1PrivateServiceConnectConfig
    publicEndpointDomainName: str
    publicEndpointEnabled: bool
    updateTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1IndexPrivateEndpoints(
    typing_extensions.TypedDict, total=False
):
    matchGrpcAddress: str
    serviceAttachment: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1IndexStats(typing_extensions.TypedDict, total=False):
    shardsCount: int
    vectorsCount: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1InputDataConfig(
    typing_extensions.TypedDict, total=False
):
    annotationSchemaUri: str
    annotationsFilter: str
    bigqueryDestination: GoogleCloudAiplatformV1beta1BigQueryDestination
    datasetId: str
    filterSplit: GoogleCloudAiplatformV1beta1FilterSplit
    fractionSplit: GoogleCloudAiplatformV1beta1FractionSplit
    gcsDestination: GoogleCloudAiplatformV1beta1GcsDestination
    persistMlUseAssignment: bool
    predefinedSplit: GoogleCloudAiplatformV1beta1PredefinedSplit
    savedQueryId: str
    stratifiedSplit: GoogleCloudAiplatformV1beta1StratifiedSplit
    timestampSplit: GoogleCloudAiplatformV1beta1TimestampSplit

@typing.type_check_only
class GoogleCloudAiplatformV1beta1Int64Array(typing_extensions.TypedDict, total=False):
    values: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1IntegratedGradientsAttribution(
    typing_extensions.TypedDict, total=False
):
    blurBaselineConfig: GoogleCloudAiplatformV1beta1BlurBaselineConfig
    smoothGradConfig: GoogleCloudAiplatformV1beta1SmoothGradConfig
    stepCount: int

@typing.type_check_only
class GoogleCloudAiplatformV1beta1LargeModelReference(
    typing_extensions.TypedDict, total=False
):
    name: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1LineageSubgraph(
    typing_extensions.TypedDict, total=False
):
    artifacts: _list[GoogleCloudAiplatformV1beta1Artifact]
    events: _list[GoogleCloudAiplatformV1beta1Event]
    executions: _list[GoogleCloudAiplatformV1beta1Execution]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListAnnotationsResponse(
    typing_extensions.TypedDict, total=False
):
    annotations: _list[GoogleCloudAiplatformV1beta1Annotation]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListArtifactsResponse(
    typing_extensions.TypedDict, total=False
):
    artifacts: _list[GoogleCloudAiplatformV1beta1Artifact]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListBatchPredictionJobsResponse(
    typing_extensions.TypedDict, total=False
):
    batchPredictionJobs: _list[GoogleCloudAiplatformV1beta1BatchPredictionJob]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListContextsResponse(
    typing_extensions.TypedDict, total=False
):
    contexts: _list[GoogleCloudAiplatformV1beta1Context]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListCustomJobsResponse(
    typing_extensions.TypedDict, total=False
):
    customJobs: _list[GoogleCloudAiplatformV1beta1CustomJob]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListDataItemsResponse(
    typing_extensions.TypedDict, total=False
):
    dataItems: _list[GoogleCloudAiplatformV1beta1DataItem]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListDataLabelingJobsResponse(
    typing_extensions.TypedDict, total=False
):
    dataLabelingJobs: _list[GoogleCloudAiplatformV1beta1DataLabelingJob]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListDatasetVersionsResponse(
    typing_extensions.TypedDict, total=False
):
    datasetVersions: _list[GoogleCloudAiplatformV1beta1DatasetVersion]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListDatasetsResponse(
    typing_extensions.TypedDict, total=False
):
    datasets: _list[GoogleCloudAiplatformV1beta1Dataset]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListDeploymentResourcePoolsResponse(
    typing_extensions.TypedDict, total=False
):
    deploymentResourcePools: _list[GoogleCloudAiplatformV1beta1DeploymentResourcePool]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListEndpointsResponse(
    typing_extensions.TypedDict, total=False
):
    endpoints: _list[GoogleCloudAiplatformV1beta1Endpoint]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListEntityTypesResponse(
    typing_extensions.TypedDict, total=False
):
    entityTypes: _list[GoogleCloudAiplatformV1beta1EntityType]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListExecutionsResponse(
    typing_extensions.TypedDict, total=False
):
    executions: _list[GoogleCloudAiplatformV1beta1Execution]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListFeaturesResponse(
    typing_extensions.TypedDict, total=False
):
    features: _list[GoogleCloudAiplatformV1beta1Feature]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListFeaturestoresResponse(
    typing_extensions.TypedDict, total=False
):
    featurestores: _list[GoogleCloudAiplatformV1beta1Featurestore]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListHyperparameterTuningJobsResponse(
    typing_extensions.TypedDict, total=False
):
    hyperparameterTuningJobs: _list[GoogleCloudAiplatformV1beta1HyperparameterTuningJob]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListIndexEndpointsResponse(
    typing_extensions.TypedDict, total=False
):
    indexEndpoints: _list[GoogleCloudAiplatformV1beta1IndexEndpoint]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListIndexesResponse(
    typing_extensions.TypedDict, total=False
):
    indexes: _list[GoogleCloudAiplatformV1beta1Index]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListMetadataSchemasResponse(
    typing_extensions.TypedDict, total=False
):
    metadataSchemas: _list[GoogleCloudAiplatformV1beta1MetadataSchema]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListMetadataStoresResponse(
    typing_extensions.TypedDict, total=False
):
    metadataStores: _list[GoogleCloudAiplatformV1beta1MetadataStore]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListModelDeploymentMonitoringJobsResponse(
    typing_extensions.TypedDict, total=False
):
    modelDeploymentMonitoringJobs: _list[
        GoogleCloudAiplatformV1beta1ModelDeploymentMonitoringJob
    ]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListModelEvaluationSlicesResponse(
    typing_extensions.TypedDict, total=False
):
    modelEvaluationSlices: _list[GoogleCloudAiplatformV1beta1ModelEvaluationSlice]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListModelEvaluationsResponse(
    typing_extensions.TypedDict, total=False
):
    modelEvaluations: _list[GoogleCloudAiplatformV1beta1ModelEvaluation]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListModelVersionsResponse(
    typing_extensions.TypedDict, total=False
):
    models: _list[GoogleCloudAiplatformV1beta1Model]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListModelsResponse(
    typing_extensions.TypedDict, total=False
):
    models: _list[GoogleCloudAiplatformV1beta1Model]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListNasJobsResponse(
    typing_extensions.TypedDict, total=False
):
    nasJobs: _list[GoogleCloudAiplatformV1beta1NasJob]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListNasTrialDetailsResponse(
    typing_extensions.TypedDict, total=False
):
    nasTrialDetails: _list[GoogleCloudAiplatformV1beta1NasTrialDetail]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListNotebookRuntimeTemplatesResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    notebookRuntimeTemplates: _list[GoogleCloudAiplatformV1beta1NotebookRuntimeTemplate]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListNotebookRuntimesResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    notebookRuntimes: _list[GoogleCloudAiplatformV1beta1NotebookRuntime]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListOptimalTrialsRequest(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListOptimalTrialsResponse(
    typing_extensions.TypedDict, total=False
):
    optimalTrials: _list[GoogleCloudAiplatformV1beta1Trial]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListPersistentResourcesResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    persistentResources: _list[GoogleCloudAiplatformV1beta1PersistentResource]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListPipelineJobsResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    pipelineJobs: _list[GoogleCloudAiplatformV1beta1PipelineJob]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListSavedQueriesResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    savedQueries: _list[GoogleCloudAiplatformV1beta1SavedQuery]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListSchedulesResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    schedules: _list[GoogleCloudAiplatformV1beta1Schedule]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListSpecialistPoolsResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    specialistPools: _list[GoogleCloudAiplatformV1beta1SpecialistPool]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListStudiesResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    studies: _list[GoogleCloudAiplatformV1beta1Study]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListTensorboardExperimentsResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    tensorboardExperiments: _list[GoogleCloudAiplatformV1beta1TensorboardExperiment]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListTensorboardRunsResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    tensorboardRuns: _list[GoogleCloudAiplatformV1beta1TensorboardRun]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListTensorboardTimeSeriesResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    tensorboardTimeSeries: _list[GoogleCloudAiplatformV1beta1TensorboardTimeSeries]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListTensorboardsResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    tensorboards: _list[GoogleCloudAiplatformV1beta1Tensorboard]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListTrainingPipelinesResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    trainingPipelines: _list[GoogleCloudAiplatformV1beta1TrainingPipeline]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListTrialsResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    trials: _list[GoogleCloudAiplatformV1beta1Trial]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1LookupStudyRequest(
    typing_extensions.TypedDict, total=False
):
    displayName: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1MachineSpec(typing_extensions.TypedDict, total=False):
    acceleratorCount: int
    acceleratorType: typing_extensions.Literal[
        "ACCELERATOR_TYPE_UNSPECIFIED",
        "NVIDIA_TESLA_K80",
        "NVIDIA_TESLA_P100",
        "NVIDIA_TESLA_V100",
        "NVIDIA_TESLA_P4",
        "NVIDIA_TESLA_T4",
        "NVIDIA_TESLA_A100",
        "NVIDIA_A100_80GB",
        "NVIDIA_L4",
        "NVIDIA_H100_80GB",
        "TPU_V2",
        "TPU_V3",
        "TPU_V4_POD",
        "TPU_V5_LITEPOD",
    ]
    machineType: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ManualBatchTuningParameters(
    typing_extensions.TypedDict, total=False
):
    batchSize: int

@typing.type_check_only
class GoogleCloudAiplatformV1beta1Measurement(typing_extensions.TypedDict, total=False):
    elapsedDuration: str
    metrics: _list[GoogleCloudAiplatformV1beta1MeasurementMetric]
    stepCount: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1MeasurementMetric(
    typing_extensions.TypedDict, total=False
):
    metricId: str
    value: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1MergeVersionAliasesRequest(
    typing_extensions.TypedDict, total=False
):
    versionAliases: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1MetadataSchema(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    description: str
    name: str
    schema: str
    schemaType: typing_extensions.Literal[
        "METADATA_SCHEMA_TYPE_UNSPECIFIED",
        "ARTIFACT_TYPE",
        "EXECUTION_TYPE",
        "CONTEXT_TYPE",
    ]
    schemaVersion: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1MetadataStore(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    description: str
    encryptionSpec: GoogleCloudAiplatformV1beta1EncryptionSpec
    name: str
    state: GoogleCloudAiplatformV1beta1MetadataStoreMetadataStoreState
    updateTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1MetadataStoreMetadataStoreState(
    typing_extensions.TypedDict, total=False
):
    diskUtilizationBytes: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1MigratableResource(
    typing_extensions.TypedDict, total=False
):
    automlDataset: GoogleCloudAiplatformV1beta1MigratableResourceAutomlDataset
    automlModel: GoogleCloudAiplatformV1beta1MigratableResourceAutomlModel
    dataLabelingDataset: GoogleCloudAiplatformV1beta1MigratableResourceDataLabelingDataset
    lastMigrateTime: str
    lastUpdateTime: str
    mlEngineModelVersion: GoogleCloudAiplatformV1beta1MigratableResourceMlEngineModelVersion

@typing.type_check_only
class GoogleCloudAiplatformV1beta1MigratableResourceAutomlDataset(
    typing_extensions.TypedDict, total=False
):
    dataset: str
    datasetDisplayName: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1MigratableResourceAutomlModel(
    typing_extensions.TypedDict, total=False
):
    model: str
    modelDisplayName: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1MigratableResourceDataLabelingDataset(
    typing_extensions.TypedDict, total=False
):
    dataLabelingAnnotatedDatasets: _list[
        GoogleCloudAiplatformV1beta1MigratableResourceDataLabelingDatasetDataLabelingAnnotatedDataset
    ]
    dataset: str
    datasetDisplayName: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1MigratableResourceDataLabelingDatasetDataLabelingAnnotatedDataset(
    typing_extensions.TypedDict, total=False
):
    annotatedDataset: str
    annotatedDatasetDisplayName: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1MigratableResourceMlEngineModelVersion(
    typing_extensions.TypedDict, total=False
):
    endpoint: str
    version: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1MigrateResourceRequest(
    typing_extensions.TypedDict, total=False
):
    migrateAutomlDatasetConfig: GoogleCloudAiplatformV1beta1MigrateResourceRequestMigrateAutomlDatasetConfig
    migrateAutomlModelConfig: GoogleCloudAiplatformV1beta1MigrateResourceRequestMigrateAutomlModelConfig
    migrateDataLabelingDatasetConfig: GoogleCloudAiplatformV1beta1MigrateResourceRequestMigrateDataLabelingDatasetConfig
    migrateMlEngineModelVersionConfig: GoogleCloudAiplatformV1beta1MigrateResourceRequestMigrateMlEngineModelVersionConfig

@typing.type_check_only
class GoogleCloudAiplatformV1beta1MigrateResourceRequestMigrateAutomlDatasetConfig(
    typing_extensions.TypedDict, total=False
):
    dataset: str
    datasetDisplayName: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1MigrateResourceRequestMigrateAutomlModelConfig(
    typing_extensions.TypedDict, total=False
):
    model: str
    modelDisplayName: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1MigrateResourceRequestMigrateDataLabelingDatasetConfig(
    typing_extensions.TypedDict, total=False
):
    dataset: str
    datasetDisplayName: str
    migrateDataLabelingAnnotatedDatasetConfigs: _list[
        GoogleCloudAiplatformV1beta1MigrateResourceRequestMigrateDataLabelingDatasetConfigMigrateDataLabelingAnnotatedDatasetConfig
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1MigrateResourceRequestMigrateDataLabelingDatasetConfigMigrateDataLabelingAnnotatedDatasetConfig(
    typing_extensions.TypedDict, total=False
):
    annotatedDataset: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1MigrateResourceRequestMigrateMlEngineModelVersionConfig(
    typing_extensions.TypedDict, total=False
):
    endpoint: str
    modelDisplayName: str
    modelVersion: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1MigrateResourceResponse(
    typing_extensions.TypedDict, total=False
):
    dataset: str
    migratableResource: GoogleCloudAiplatformV1beta1MigratableResource
    model: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1Model(typing_extensions.TypedDict, total=False):
    artifactUri: str
    containerSpec: GoogleCloudAiplatformV1beta1ModelContainerSpec
    createTime: str
    deployedModels: _list[GoogleCloudAiplatformV1beta1DeployedModelRef]
    description: str
    displayName: str
    encryptionSpec: GoogleCloudAiplatformV1beta1EncryptionSpec
    etag: str
    explanationSpec: GoogleCloudAiplatformV1beta1ExplanationSpec
    labels: dict[str, typing.Any]
    metadata: typing.Any
    metadataArtifact: str
    metadataSchemaUri: str
    modelSourceInfo: GoogleCloudAiplatformV1beta1ModelSourceInfo
    name: str
    originalModelInfo: GoogleCloudAiplatformV1beta1ModelOriginalModelInfo
    predictSchemata: GoogleCloudAiplatformV1beta1PredictSchemata
    supportedDeploymentResourcesTypes: _list[str]
    supportedExportFormats: _list[GoogleCloudAiplatformV1beta1ModelExportFormat]
    supportedInputStorageFormats: _list[str]
    supportedOutputStorageFormats: _list[str]
    trainingPipeline: str
    updateTime: str
    versionAliases: _list[str]
    versionCreateTime: str
    versionDescription: str
    versionId: str
    versionUpdateTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ModelContainerSpec(
    typing_extensions.TypedDict, total=False
):
    args: _list[str]
    command: _list[str]
    env: _list[GoogleCloudAiplatformV1beta1EnvVar]
    healthRoute: str
    imageUri: str
    ports: _list[GoogleCloudAiplatformV1beta1Port]
    predictRoute: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ModelDeploymentMonitoringBigQueryTable(
    typing_extensions.TypedDict, total=False
):
    bigqueryTablePath: str
    logSource: typing_extensions.Literal[
        "LOG_SOURCE_UNSPECIFIED", "TRAINING", "SERVING"
    ]
    logType: typing_extensions.Literal["LOG_TYPE_UNSPECIFIED", "PREDICT", "EXPLAIN"]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ModelDeploymentMonitoringJob(
    typing_extensions.TypedDict, total=False
):
    analysisInstanceSchemaUri: str
    bigqueryTables: _list[
        GoogleCloudAiplatformV1beta1ModelDeploymentMonitoringBigQueryTable
    ]
    createTime: str
    displayName: str
    enableMonitoringPipelineLogs: bool
    encryptionSpec: GoogleCloudAiplatformV1beta1EncryptionSpec
    endpoint: str
    error: GoogleRpcStatus
    labels: dict[str, typing.Any]
    latestMonitoringPipelineMetadata: GoogleCloudAiplatformV1beta1ModelDeploymentMonitoringJobLatestMonitoringPipelineMetadata
    logTtl: str
    loggingSamplingStrategy: GoogleCloudAiplatformV1beta1SamplingStrategy
    modelDeploymentMonitoringObjectiveConfigs: _list[
        GoogleCloudAiplatformV1beta1ModelDeploymentMonitoringObjectiveConfig
    ]
    modelDeploymentMonitoringScheduleConfig: GoogleCloudAiplatformV1beta1ModelDeploymentMonitoringScheduleConfig
    modelMonitoringAlertConfig: GoogleCloudAiplatformV1beta1ModelMonitoringAlertConfig
    name: str
    nextScheduleTime: str
    predictInstanceSchemaUri: str
    samplePredictInstance: typing.Any
    scheduleState: typing_extensions.Literal[
        "MONITORING_SCHEDULE_STATE_UNSPECIFIED", "PENDING", "OFFLINE", "RUNNING"
    ]
    state: typing_extensions.Literal[
        "JOB_STATE_UNSPECIFIED",
        "JOB_STATE_QUEUED",
        "JOB_STATE_PENDING",
        "JOB_STATE_RUNNING",
        "JOB_STATE_SUCCEEDED",
        "JOB_STATE_FAILED",
        "JOB_STATE_CANCELLING",
        "JOB_STATE_CANCELLED",
        "JOB_STATE_PAUSED",
        "JOB_STATE_EXPIRED",
        "JOB_STATE_UPDATING",
        "JOB_STATE_PARTIALLY_SUCCEEDED",
    ]
    statsAnomaliesBaseDirectory: GoogleCloudAiplatformV1beta1GcsDestination
    updateTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ModelDeploymentMonitoringJobLatestMonitoringPipelineMetadata(
    typing_extensions.TypedDict, total=False
):
    runTime: str
    status: GoogleRpcStatus

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ModelDeploymentMonitoringObjectiveConfig(
    typing_extensions.TypedDict, total=False
):
    deployedModelId: str
    objectiveConfig: GoogleCloudAiplatformV1beta1ModelMonitoringObjectiveConfig

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ModelDeploymentMonitoringScheduleConfig(
    typing_extensions.TypedDict, total=False
):
    monitorInterval: str
    monitorWindow: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ModelEvaluation(
    typing_extensions.TypedDict, total=False
):
    biasConfigs: GoogleCloudAiplatformV1beta1ModelEvaluationBiasConfig
    createTime: str
    displayName: str
    explanationSpecs: _list[
        GoogleCloudAiplatformV1beta1ModelEvaluationModelEvaluationExplanationSpec
    ]
    metadata: typing.Any
    metrics: typing.Any
    metricsSchemaUri: str
    modelExplanation: GoogleCloudAiplatformV1beta1ModelExplanation
    name: str
    sliceDimensions: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ModelEvaluationBiasConfig(
    typing_extensions.TypedDict, total=False
):
    biasSlices: GoogleCloudAiplatformV1beta1ModelEvaluationSliceSliceSliceSpec
    labels: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ModelEvaluationModelEvaluationExplanationSpec(
    typing_extensions.TypedDict, total=False
):
    explanationSpec: GoogleCloudAiplatformV1beta1ExplanationSpec
    explanationType: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ModelEvaluationSlice(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    metrics: typing.Any
    metricsSchemaUri: str
    modelExplanation: GoogleCloudAiplatformV1beta1ModelExplanation
    name: str
    slice: GoogleCloudAiplatformV1beta1ModelEvaluationSliceSlice

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ModelEvaluationSliceSlice(
    typing_extensions.TypedDict, total=False
):
    dimension: str
    sliceSpec: GoogleCloudAiplatformV1beta1ModelEvaluationSliceSliceSliceSpec
    value: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ModelEvaluationSliceSliceSliceSpec(
    typing_extensions.TypedDict, total=False
):
    configs: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ModelEvaluationSliceSliceSliceSpecRange(
    typing_extensions.TypedDict, total=False
):
    high: float
    low: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ModelEvaluationSliceSliceSliceSpecSliceConfig(
    typing_extensions.TypedDict, total=False
):
    allValues: bool
    range: GoogleCloudAiplatformV1beta1ModelEvaluationSliceSliceSliceSpecRange
    value: GoogleCloudAiplatformV1beta1ModelEvaluationSliceSliceSliceSpecValue

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ModelEvaluationSliceSliceSliceSpecValue(
    typing_extensions.TypedDict, total=False
):
    floatValue: float
    stringValue: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ModelExplanation(
    typing_extensions.TypedDict, total=False
):
    meanAttributions: _list[GoogleCloudAiplatformV1beta1Attribution]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ModelExportFormat(
    typing_extensions.TypedDict, total=False
):
    exportableContents: _list[str]
    id: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ModelMonitoringAlertConfig(
    typing_extensions.TypedDict, total=False
):
    emailAlertConfig: GoogleCloudAiplatformV1beta1ModelMonitoringAlertConfigEmailAlertConfig
    enableLogging: bool
    notificationChannels: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ModelMonitoringAlertConfigEmailAlertConfig(
    typing_extensions.TypedDict, total=False
):
    userEmails: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ModelMonitoringConfig(
    typing_extensions.TypedDict, total=False
):
    alertConfig: GoogleCloudAiplatformV1beta1ModelMonitoringAlertConfig
    analysisInstanceSchemaUri: str
    objectiveConfigs: _list[GoogleCloudAiplatformV1beta1ModelMonitoringObjectiveConfig]
    statsAnomaliesBaseDirectory: GoogleCloudAiplatformV1beta1GcsDestination

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ModelMonitoringObjectiveConfig(
    typing_extensions.TypedDict, total=False
):
    explanationConfig: GoogleCloudAiplatformV1beta1ModelMonitoringObjectiveConfigExplanationConfig
    predictionDriftDetectionConfig: GoogleCloudAiplatformV1beta1ModelMonitoringObjectiveConfigPredictionDriftDetectionConfig
    trainingDataset: GoogleCloudAiplatformV1beta1ModelMonitoringObjectiveConfigTrainingDataset
    trainingPredictionSkewDetectionConfig: GoogleCloudAiplatformV1beta1ModelMonitoringObjectiveConfigTrainingPredictionSkewDetectionConfig

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ModelMonitoringObjectiveConfigExplanationConfig(
    typing_extensions.TypedDict, total=False
):
    enableFeatureAttributes: bool
    explanationBaseline: GoogleCloudAiplatformV1beta1ModelMonitoringObjectiveConfigExplanationConfigExplanationBaseline

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ModelMonitoringObjectiveConfigExplanationConfigExplanationBaseline(
    typing_extensions.TypedDict, total=False
):
    bigquery: GoogleCloudAiplatformV1beta1BigQueryDestination
    gcs: GoogleCloudAiplatformV1beta1GcsDestination
    predictionFormat: typing_extensions.Literal[
        "PREDICTION_FORMAT_UNSPECIFIED", "JSONL", "BIGQUERY"
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ModelMonitoringObjectiveConfigPredictionDriftDetectionConfig(
    typing_extensions.TypedDict, total=False
):
    attributionScoreDriftThresholds: dict[str, typing.Any]
    defaultDriftThreshold: GoogleCloudAiplatformV1beta1ThresholdConfig
    driftThresholds: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ModelMonitoringObjectiveConfigTrainingDataset(
    typing_extensions.TypedDict, total=False
):
    bigquerySource: GoogleCloudAiplatformV1beta1BigQuerySource
    dataFormat: str
    dataset: str
    gcsSource: GoogleCloudAiplatformV1beta1GcsSource
    loggingSamplingStrategy: GoogleCloudAiplatformV1beta1SamplingStrategy
    targetField: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ModelMonitoringObjectiveConfigTrainingPredictionSkewDetectionConfig(
    typing_extensions.TypedDict, total=False
):
    attributionScoreSkewThresholds: dict[str, typing.Any]
    defaultSkewThreshold: GoogleCloudAiplatformV1beta1ThresholdConfig
    skewThresholds: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ModelMonitoringStatsAnomalies(
    typing_extensions.TypedDict, total=False
):
    anomalyCount: int
    deployedModelId: str
    featureStats: _list[
        GoogleCloudAiplatformV1beta1ModelMonitoringStatsAnomaliesFeatureHistoricStatsAnomalies
    ]
    objective: typing_extensions.Literal[
        "MODEL_DEPLOYMENT_MONITORING_OBJECTIVE_TYPE_UNSPECIFIED",
        "RAW_FEATURE_SKEW",
        "RAW_FEATURE_DRIFT",
        "FEATURE_ATTRIBUTION_SKEW",
        "FEATURE_ATTRIBUTION_DRIFT",
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ModelMonitoringStatsAnomaliesFeatureHistoricStatsAnomalies(
    typing_extensions.TypedDict, total=False
):
    featureDisplayName: str
    predictionStats: _list[GoogleCloudAiplatformV1beta1FeatureStatsAnomaly]
    threshold: GoogleCloudAiplatformV1beta1ThresholdConfig
    trainingStats: GoogleCloudAiplatformV1beta1FeatureStatsAnomaly

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ModelOriginalModelInfo(
    typing_extensions.TypedDict, total=False
):
    model: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ModelSourceInfo(
    typing_extensions.TypedDict, total=False
):
    copy: bool
    sourceType: typing_extensions.Literal[
        "MODEL_SOURCE_TYPE_UNSPECIFIED",
        "AUTOML",
        "CUSTOM",
        "BQML",
        "MODEL_GARDEN",
        "GENIE",
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1MutateDeployedIndexOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    deployedIndexId: str
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1MutateDeployedIndexResponse(
    typing_extensions.TypedDict, total=False
):
    deployedIndex: GoogleCloudAiplatformV1beta1DeployedIndex

@typing.type_check_only
class GoogleCloudAiplatformV1beta1MutateDeployedModelOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1MutateDeployedModelRequest(
    typing_extensions.TypedDict, total=False
):
    deployedModel: GoogleCloudAiplatformV1beta1DeployedModel
    updateMask: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1MutateDeployedModelResponse(
    typing_extensions.TypedDict, total=False
):
    deployedModel: GoogleCloudAiplatformV1beta1DeployedModel

@typing.type_check_only
class GoogleCloudAiplatformV1beta1NasJob(typing_extensions.TypedDict, total=False):
    createTime: str
    displayName: str
    enableRestrictedImageTraining: bool
    encryptionSpec: GoogleCloudAiplatformV1beta1EncryptionSpec
    endTime: str
    error: GoogleRpcStatus
    labels: dict[str, typing.Any]
    name: str
    nasJobOutput: GoogleCloudAiplatformV1beta1NasJobOutput
    nasJobSpec: GoogleCloudAiplatformV1beta1NasJobSpec
    startTime: str
    state: typing_extensions.Literal[
        "JOB_STATE_UNSPECIFIED",
        "JOB_STATE_QUEUED",
        "JOB_STATE_PENDING",
        "JOB_STATE_RUNNING",
        "JOB_STATE_SUCCEEDED",
        "JOB_STATE_FAILED",
        "JOB_STATE_CANCELLING",
        "JOB_STATE_CANCELLED",
        "JOB_STATE_PAUSED",
        "JOB_STATE_EXPIRED",
        "JOB_STATE_UPDATING",
        "JOB_STATE_PARTIALLY_SUCCEEDED",
    ]
    updateTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1NasJobOutput(
    typing_extensions.TypedDict, total=False
):
    multiTrialJobOutput: GoogleCloudAiplatformV1beta1NasJobOutputMultiTrialJobOutput

@typing.type_check_only
class GoogleCloudAiplatformV1beta1NasJobOutputMultiTrialJobOutput(
    typing_extensions.TypedDict, total=False
):
    searchTrials: _list[GoogleCloudAiplatformV1beta1NasTrial]
    trainTrials: _list[GoogleCloudAiplatformV1beta1NasTrial]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1NasJobSpec(typing_extensions.TypedDict, total=False):
    multiTrialAlgorithmSpec: GoogleCloudAiplatformV1beta1NasJobSpecMultiTrialAlgorithmSpec
    resumeNasJobId: str
    searchSpaceSpec: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1NasJobSpecMultiTrialAlgorithmSpec(
    typing_extensions.TypedDict, total=False
):
    metric: GoogleCloudAiplatformV1beta1NasJobSpecMultiTrialAlgorithmSpecMetricSpec
    multiTrialAlgorithm: typing_extensions.Literal[
        "MULTI_TRIAL_ALGORITHM_UNSPECIFIED", "REINFORCEMENT_LEARNING", "GRID_SEARCH"
    ]
    searchTrialSpec: GoogleCloudAiplatformV1beta1NasJobSpecMultiTrialAlgorithmSpecSearchTrialSpec
    trainTrialSpec: GoogleCloudAiplatformV1beta1NasJobSpecMultiTrialAlgorithmSpecTrainTrialSpec

@typing.type_check_only
class GoogleCloudAiplatformV1beta1NasJobSpecMultiTrialAlgorithmSpecMetricSpec(
    typing_extensions.TypedDict, total=False
):
    goal: typing_extensions.Literal["GOAL_TYPE_UNSPECIFIED", "MAXIMIZE", "MINIMIZE"]
    metricId: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1NasJobSpecMultiTrialAlgorithmSpecSearchTrialSpec(
    typing_extensions.TypedDict, total=False
):
    maxFailedTrialCount: int
    maxParallelTrialCount: int
    maxTrialCount: int
    searchTrialJobSpec: GoogleCloudAiplatformV1beta1CustomJobSpec

@typing.type_check_only
class GoogleCloudAiplatformV1beta1NasJobSpecMultiTrialAlgorithmSpecTrainTrialSpec(
    typing_extensions.TypedDict, total=False
):
    frequency: int
    maxParallelTrialCount: int
    trainTrialJobSpec: GoogleCloudAiplatformV1beta1CustomJobSpec

@typing.type_check_only
class GoogleCloudAiplatformV1beta1NasTrial(typing_extensions.TypedDict, total=False):
    endTime: str
    finalMeasurement: GoogleCloudAiplatformV1beta1Measurement
    id: str
    startTime: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "REQUESTED",
        "ACTIVE",
        "STOPPING",
        "SUCCEEDED",
        "INFEASIBLE",
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1NasTrialDetail(
    typing_extensions.TypedDict, total=False
):
    name: str
    parameters: str
    searchTrial: GoogleCloudAiplatformV1beta1NasTrial
    trainTrial: GoogleCloudAiplatformV1beta1NasTrial

@typing.type_check_only
class GoogleCloudAiplatformV1beta1NearestNeighborSearchOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    contentValidationStats: _list[
        GoogleCloudAiplatformV1beta1NearestNeighborSearchOperationMetadataContentValidationStats
    ]
    dataBytesCount: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1NearestNeighborSearchOperationMetadataContentValidationStats(
    typing_extensions.TypedDict, total=False
):
    invalidRecordCount: str
    partialErrors: _list[
        GoogleCloudAiplatformV1beta1NearestNeighborSearchOperationMetadataRecordError
    ]
    sourceGcsUri: str
    validRecordCount: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1NearestNeighborSearchOperationMetadataRecordError(
    typing_extensions.TypedDict, total=False
):
    embeddingId: str
    errorMessage: str
    errorType: typing_extensions.Literal[
        "ERROR_TYPE_UNSPECIFIED",
        "EMPTY_LINE",
        "INVALID_JSON_SYNTAX",
        "INVALID_CSV_SYNTAX",
        "INVALID_AVRO_SYNTAX",
        "INVALID_EMBEDDING_ID",
        "EMBEDDING_SIZE_MISMATCH",
        "NAMESPACE_MISSING",
    ]
    rawRecord: str
    sourceGcsUri: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1Neighbor(typing_extensions.TypedDict, total=False):
    neighborDistance: float
    neighborId: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1NetworkSpec(typing_extensions.TypedDict, total=False):
    enableInternetAccess: bool
    network: str
    subnetwork: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1NfsMount(typing_extensions.TypedDict, total=False):
    mountPoint: str
    path: str
    server: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1NotebookEucConfig(
    typing_extensions.TypedDict, total=False
):
    bypassActasCheck: bool
    eucDisabled: bool

@typing.type_check_only
class GoogleCloudAiplatformV1beta1NotebookIdleShutdownConfig(
    typing_extensions.TypedDict, total=False
):
    idleShutdownDisabled: bool
    idleTimeout: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1NotebookRuntime(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    description: str
    displayName: str
    expirationTime: str
    healthState: typing_extensions.Literal[
        "HEALTH_STATE_UNSPECIFIED", "HEALTHY", "UNHEALTHY"
    ]
    labels: dict[str, typing.Any]
    name: str
    notebookRuntimeTemplateRef: GoogleCloudAiplatformV1beta1NotebookRuntimeTemplateRef
    notebookRuntimeType: typing_extensions.Literal[
        "NOTEBOOK_RUNTIME_TYPE_UNSPECIFIED", "USER_DEFINED", "ONE_CLICK"
    ]
    proxyUri: str
    runtimeState: typing_extensions.Literal[
        "RUNTIME_STATE_UNSPECIFIED",
        "RUNNING",
        "BEING_STARTED",
        "BEING_STOPPED",
        "STOPPED",
        "BEING_UPGRADED",
    ]
    runtimeUser: str
    serviceAccount: str
    updateTime: str
    version: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1NotebookRuntimeTemplate(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    dataPersistentDiskSpec: GoogleCloudAiplatformV1beta1PersistentDiskSpec
    description: str
    displayName: str
    etag: str
    eucConfig: GoogleCloudAiplatformV1beta1NotebookEucConfig
    idleShutdownConfig: GoogleCloudAiplatformV1beta1NotebookIdleShutdownConfig
    isDefault: bool
    labels: dict[str, typing.Any]
    machineSpec: GoogleCloudAiplatformV1beta1MachineSpec
    name: str
    networkSpec: GoogleCloudAiplatformV1beta1NetworkSpec
    notebookRuntimeType: typing_extensions.Literal[
        "NOTEBOOK_RUNTIME_TYPE_UNSPECIFIED", "USER_DEFINED", "ONE_CLICK"
    ]
    serviceAccount: str
    updateTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1NotebookRuntimeTemplateRef(
    typing_extensions.TypedDict, total=False
):
    notebookRuntimeTemplate: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1PauseModelDeploymentMonitoringJobRequest(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1PauseScheduleRequest(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1PersistentDiskSpec(
    typing_extensions.TypedDict, total=False
):
    diskSizeGb: str
    diskType: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1PersistentResource(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    displayName: str
    encryptionSpec: GoogleCloudAiplatformV1beta1EncryptionSpec
    error: GoogleRpcStatus
    labels: dict[str, typing.Any]
    name: str
    network: str
    reservedIpRanges: _list[str]
    resourcePools: _list[GoogleCloudAiplatformV1beta1ResourcePool]
    resourceRuntime: GoogleCloudAiplatformV1beta1ResourceRuntime
    resourceRuntimeSpec: GoogleCloudAiplatformV1beta1ResourceRuntimeSpec
    startTime: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "PROVISIONING", "RUNNING", "STOPPING", "ERROR"
    ]
    updateTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1PipelineJob(typing_extensions.TypedDict, total=False):
    createTime: str
    displayName: str
    encryptionSpec: GoogleCloudAiplatformV1beta1EncryptionSpec
    endTime: str
    error: GoogleRpcStatus
    jobDetail: GoogleCloudAiplatformV1beta1PipelineJobDetail
    labels: dict[str, typing.Any]
    name: str
    network: str
    pipelineSpec: dict[str, typing.Any]
    reservedIpRanges: _list[str]
    runtimeConfig: GoogleCloudAiplatformV1beta1PipelineJobRuntimeConfig
    scheduleName: str
    serviceAccount: str
    startTime: str
    state: typing_extensions.Literal[
        "PIPELINE_STATE_UNSPECIFIED",
        "PIPELINE_STATE_QUEUED",
        "PIPELINE_STATE_PENDING",
        "PIPELINE_STATE_RUNNING",
        "PIPELINE_STATE_SUCCEEDED",
        "PIPELINE_STATE_FAILED",
        "PIPELINE_STATE_CANCELLING",
        "PIPELINE_STATE_CANCELLED",
        "PIPELINE_STATE_PAUSED",
    ]
    templateMetadata: GoogleCloudAiplatformV1beta1PipelineTemplateMetadata
    templateUri: str
    updateTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1PipelineJobDetail(
    typing_extensions.TypedDict, total=False
):
    pipelineContext: GoogleCloudAiplatformV1beta1Context
    pipelineRunContext: GoogleCloudAiplatformV1beta1Context
    taskDetails: _list[GoogleCloudAiplatformV1beta1PipelineTaskDetail]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1PipelineJobRuntimeConfig(
    typing_extensions.TypedDict, total=False
):
    failurePolicy: typing_extensions.Literal[
        "PIPELINE_FAILURE_POLICY_UNSPECIFIED",
        "PIPELINE_FAILURE_POLICY_FAIL_SLOW",
        "PIPELINE_FAILURE_POLICY_FAIL_FAST",
    ]
    gcsOutputDirectory: str
    inputArtifacts: dict[str, typing.Any]
    parameterValues: dict[str, typing.Any]
    parameters: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1PipelineJobRuntimeConfigInputArtifact(
    typing_extensions.TypedDict, total=False
):
    artifactId: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1PipelineTaskDetail(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    endTime: str
    error: GoogleRpcStatus
    execution: GoogleCloudAiplatformV1beta1Execution
    executorDetail: GoogleCloudAiplatformV1beta1PipelineTaskExecutorDetail
    inputs: dict[str, typing.Any]
    outputs: dict[str, typing.Any]
    parentTaskId: str
    pipelineTaskStatus: _list[
        GoogleCloudAiplatformV1beta1PipelineTaskDetailPipelineTaskStatus
    ]
    startTime: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "PENDING",
        "RUNNING",
        "SUCCEEDED",
        "CANCEL_PENDING",
        "CANCELLING",
        "CANCELLED",
        "FAILED",
        "SKIPPED",
        "NOT_TRIGGERED",
    ]
    taskId: str
    taskName: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1PipelineTaskDetailArtifactList(
    typing_extensions.TypedDict, total=False
):
    artifacts: _list[GoogleCloudAiplatformV1beta1Artifact]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1PipelineTaskDetailPipelineTaskStatus(
    typing_extensions.TypedDict, total=False
):
    error: GoogleRpcStatus
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "PENDING",
        "RUNNING",
        "SUCCEEDED",
        "CANCEL_PENDING",
        "CANCELLING",
        "CANCELLED",
        "FAILED",
        "SKIPPED",
        "NOT_TRIGGERED",
    ]
    updateTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1PipelineTaskExecutorDetail(
    typing_extensions.TypedDict, total=False
):
    containerDetail: GoogleCloudAiplatformV1beta1PipelineTaskExecutorDetailContainerDetail
    customJobDetail: GoogleCloudAiplatformV1beta1PipelineTaskExecutorDetailCustomJobDetail

@typing.type_check_only
class GoogleCloudAiplatformV1beta1PipelineTaskExecutorDetailContainerDetail(
    typing_extensions.TypedDict, total=False
):
    failedMainJobs: _list[str]
    failedPreCachingCheckJobs: _list[str]
    mainJob: str
    preCachingCheckJob: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1PipelineTaskExecutorDetailCustomJobDetail(
    typing_extensions.TypedDict, total=False
):
    failedJobs: _list[str]
    job: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1PipelineTemplateMetadata(
    typing_extensions.TypedDict, total=False
):
    version: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1Port(typing_extensions.TypedDict, total=False):
    containerPort: int

@typing.type_check_only
class GoogleCloudAiplatformV1beta1PredefinedSplit(
    typing_extensions.TypedDict, total=False
):
    key: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1PredictRequest(
    typing_extensions.TypedDict, total=False
):
    instances: _list[typing.Any]
    parameters: typing.Any

@typing.type_check_only
class GoogleCloudAiplatformV1beta1PredictRequestResponseLoggingConfig(
    typing_extensions.TypedDict, total=False
):
    bigqueryDestination: GoogleCloudAiplatformV1beta1BigQueryDestination
    enabled: bool
    samplingRate: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1PredictResponse(
    typing_extensions.TypedDict, total=False
):
    deployedModelId: str
    metadata: typing.Any
    model: str
    modelDisplayName: str
    modelVersionId: str
    predictions: _list[typing.Any]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1PredictSchemata(
    typing_extensions.TypedDict, total=False
):
    instanceSchemaUri: str
    parametersSchemaUri: str
    predictionSchemaUri: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1Presets(typing_extensions.TypedDict, total=False):
    modality: typing_extensions.Literal[
        "MODALITY_UNSPECIFIED", "IMAGE", "TEXT", "TABULAR"
    ]
    query: typing_extensions.Literal["PRECISE", "FAST"]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1PrivateEndpoints(
    typing_extensions.TypedDict, total=False
):
    explainHttpUri: str
    healthHttpUri: str
    predictHttpUri: str
    serviceAttachment: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1PrivateServiceConnectConfig(
    typing_extensions.TypedDict, total=False
):
    enablePrivateServiceConnect: bool
    projectAllowlist: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1PublisherModel(
    typing_extensions.TypedDict, total=False
):
    frameworks: _list[str]
    launchStage: typing_extensions.Literal[
        "LAUNCH_STAGE_UNSPECIFIED",
        "EXPERIMENTAL",
        "PRIVATE_PREVIEW",
        "PUBLIC_PREVIEW",
        "GA",
    ]
    name: str
    openSourceCategory: typing_extensions.Literal[
        "OPEN_SOURCE_CATEGORY_UNSPECIFIED",
        "PROPRIETARY",
        "GOOGLE_OWNED_OSS_WITH_GOOGLE_CHECKPOINT",
        "THIRD_PARTY_OWNED_OSS_WITH_GOOGLE_CHECKPOINT",
        "GOOGLE_OWNED_OSS",
        "THIRD_PARTY_OWNED_OSS",
    ]
    parent: GoogleCloudAiplatformV1beta1PublisherModelParent
    predictSchemata: GoogleCloudAiplatformV1beta1PredictSchemata
    publisherModelTemplate: str
    supportedActions: GoogleCloudAiplatformV1beta1PublisherModelCallToAction
    versionId: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1PublisherModelCallToAction(
    typing_extensions.TypedDict, total=False
):
    createApplication: GoogleCloudAiplatformV1beta1PublisherModelCallToActionRegionalResourceReferences
    deploy: GoogleCloudAiplatformV1beta1PublisherModelCallToActionDeploy
    openEvaluationPipeline: GoogleCloudAiplatformV1beta1PublisherModelCallToActionRegionalResourceReferences
    openFineTuningPipeline: GoogleCloudAiplatformV1beta1PublisherModelCallToActionRegionalResourceReferences
    openGenerationAiStudio: GoogleCloudAiplatformV1beta1PublisherModelCallToActionRegionalResourceReferences
    openGenie: GoogleCloudAiplatformV1beta1PublisherModelCallToActionRegionalResourceReferences
    openNotebook: GoogleCloudAiplatformV1beta1PublisherModelCallToActionRegionalResourceReferences
    openPromptTuningPipeline: GoogleCloudAiplatformV1beta1PublisherModelCallToActionRegionalResourceReferences
    requestAccess: GoogleCloudAiplatformV1beta1PublisherModelCallToActionRegionalResourceReferences
    viewRestApi: GoogleCloudAiplatformV1beta1PublisherModelCallToActionViewRestApi

@typing.type_check_only
class GoogleCloudAiplatformV1beta1PublisherModelCallToActionDeploy(
    typing_extensions.TypedDict, total=False
):
    artifactUri: str
    automaticResources: GoogleCloudAiplatformV1beta1AutomaticResources
    containerSpec: GoogleCloudAiplatformV1beta1ModelContainerSpec
    dedicatedResources: GoogleCloudAiplatformV1beta1DedicatedResources
    largeModelReference: GoogleCloudAiplatformV1beta1LargeModelReference
    modelDisplayName: str
    sharedResources: str
    title: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1PublisherModelCallToActionRegionalResourceReferences(
    typing_extensions.TypedDict, total=False
):
    references: dict[str, typing.Any]
    title: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1PublisherModelCallToActionViewRestApi(
    typing_extensions.TypedDict, total=False
):
    documentations: _list[GoogleCloudAiplatformV1beta1PublisherModelDocumentation]
    title: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1PublisherModelDocumentation(
    typing_extensions.TypedDict, total=False
):
    content: str
    title: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1PublisherModelParent(
    typing_extensions.TypedDict, total=False
):
    displayName: str
    reference: GoogleCloudAiplatformV1beta1PublisherModelResourceReference

@typing.type_check_only
class GoogleCloudAiplatformV1beta1PublisherModelResourceReference(
    typing_extensions.TypedDict, total=False
):
    resourceName: str
    uri: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1PurgeArtifactsMetadata(
    typing_extensions.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1PurgeArtifactsRequest(
    typing_extensions.TypedDict, total=False
):
    filter: str
    force: bool

@typing.type_check_only
class GoogleCloudAiplatformV1beta1PurgeArtifactsResponse(
    typing_extensions.TypedDict, total=False
):
    purgeCount: str
    purgeSample: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1PurgeContextsMetadata(
    typing_extensions.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1PurgeContextsRequest(
    typing_extensions.TypedDict, total=False
):
    filter: str
    force: bool

@typing.type_check_only
class GoogleCloudAiplatformV1beta1PurgeContextsResponse(
    typing_extensions.TypedDict, total=False
):
    purgeCount: str
    purgeSample: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1PurgeExecutionsMetadata(
    typing_extensions.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1PurgeExecutionsRequest(
    typing_extensions.TypedDict, total=False
):
    filter: str
    force: bool

@typing.type_check_only
class GoogleCloudAiplatformV1beta1PurgeExecutionsResponse(
    typing_extensions.TypedDict, total=False
):
    purgeCount: str
    purgeSample: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1PythonPackageSpec(
    typing_extensions.TypedDict, total=False
):
    args: _list[str]
    env: _list[GoogleCloudAiplatformV1beta1EnvVar]
    executorImageUri: str
    packageUris: _list[str]
    pythonModule: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1QueryDeployedModelsResponse(
    typing_extensions.TypedDict, total=False
):
    deployedModelRefs: _list[GoogleCloudAiplatformV1beta1DeployedModelRef]
    deployedModels: _list[GoogleCloudAiplatformV1beta1DeployedModel]
    nextPageToken: str
    totalDeployedModelCount: int
    totalEndpointCount: int

@typing.type_check_only
class GoogleCloudAiplatformV1beta1RawPredictRequest(
    typing_extensions.TypedDict, total=False
):
    httpBody: GoogleApiHttpBody

@typing.type_check_only
class GoogleCloudAiplatformV1beta1RaySpec(typing_extensions.TypedDict, total=False):
    headNodeResourcePoolId: str
    imageUri: str
    resourcePoolImages: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ReadFeatureValuesRequest(
    typing_extensions.TypedDict, total=False
):
    entityId: str
    featureSelector: GoogleCloudAiplatformV1beta1FeatureSelector

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ReadFeatureValuesResponse(
    typing_extensions.TypedDict, total=False
):
    entityView: GoogleCloudAiplatformV1beta1ReadFeatureValuesResponseEntityView
    header: GoogleCloudAiplatformV1beta1ReadFeatureValuesResponseHeader

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ReadFeatureValuesResponseEntityView(
    typing_extensions.TypedDict, total=False
):
    data: _list[GoogleCloudAiplatformV1beta1ReadFeatureValuesResponseEntityViewData]
    entityId: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ReadFeatureValuesResponseEntityViewData(
    typing_extensions.TypedDict, total=False
):
    value: GoogleCloudAiplatformV1beta1FeatureValue
    values: GoogleCloudAiplatformV1beta1FeatureValueList

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ReadFeatureValuesResponseFeatureDescriptor(
    typing_extensions.TypedDict, total=False
):
    id: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ReadFeatureValuesResponseHeader(
    typing_extensions.TypedDict, total=False
):
    entityType: str
    featureDescriptors: _list[
        GoogleCloudAiplatformV1beta1ReadFeatureValuesResponseFeatureDescriptor
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ReadIndexDatapointsRequest(
    typing_extensions.TypedDict, total=False
):
    deployedIndexId: str
    ids: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ReadIndexDatapointsResponse(
    typing_extensions.TypedDict, total=False
):
    datapoints: _list[GoogleCloudAiplatformV1beta1IndexDatapoint]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ReadTensorboardBlobDataResponse(
    typing_extensions.TypedDict, total=False
):
    blobs: _list[GoogleCloudAiplatformV1beta1TensorboardBlob]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ReadTensorboardSizeResponse(
    typing_extensions.TypedDict, total=False
):
    storageSizeByte: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ReadTensorboardTimeSeriesDataResponse(
    typing_extensions.TypedDict, total=False
):
    timeSeriesData: GoogleCloudAiplatformV1beta1TimeSeriesData

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ReadTensorboardUsageResponse(
    typing_extensions.TypedDict, total=False
):
    monthlyUsageData: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ReadTensorboardUsageResponsePerMonthUsageData(
    typing_extensions.TypedDict, total=False
):
    userUsageData: _list[
        GoogleCloudAiplatformV1beta1ReadTensorboardUsageResponsePerUserUsageData
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ReadTensorboardUsageResponsePerUserUsageData(
    typing_extensions.TypedDict, total=False
):
    username: str
    viewCount: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1RemoveContextChildrenRequest(
    typing_extensions.TypedDict, total=False
):
    childContexts: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1RemoveContextChildrenResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1RemoveDatapointsRequest(
    typing_extensions.TypedDict, total=False
):
    datapointIds: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1RemoveDatapointsResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ReportRuntimeEventRequest(
    typing_extensions.TypedDict, total=False
):
    eventDetails: dict[str, typing.Any]
    eventType: typing_extensions.Literal["EVENT_TYPE_UNSPECIFIED", "HEARTBEAT", "IDLE"]
    vmToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ReportRuntimeEventResponse(
    typing_extensions.TypedDict, total=False
):
    idleShutdownMessage: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ResourcePool(
    typing_extensions.TypedDict, total=False
):
    autoscalingSpec: GoogleCloudAiplatformV1beta1ResourcePoolAutoscalingSpec
    diskSpec: GoogleCloudAiplatformV1beta1DiskSpec
    id: str
    machineSpec: GoogleCloudAiplatformV1beta1MachineSpec
    replicaCount: str
    usedReplicaCount: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ResourcePoolAutoscalingSpec(
    typing_extensions.TypedDict, total=False
):
    maxReplicaCount: str
    minReplicaCount: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ResourceRuntime(
    typing_extensions.TypedDict, total=False
):
    accessUris: dict[str, typing.Any]
    notebookRuntimeTemplate: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ResourceRuntimeSpec(
    typing_extensions.TypedDict, total=False
):
    raySpec: GoogleCloudAiplatformV1beta1RaySpec
    serviceAccountSpec: GoogleCloudAiplatformV1beta1ServiceAccountSpec

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ResourcesConsumed(
    typing_extensions.TypedDict, total=False
):
    replicaHours: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1RestoreDatasetVersionOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ResumeModelDeploymentMonitoringJobRequest(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ResumeScheduleRequest(
    typing_extensions.TypedDict, total=False
):
    catchUp: bool

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SampleConfig(
    typing_extensions.TypedDict, total=False
):
    followingBatchSamplePercentage: int
    initialBatchSamplePercentage: int
    sampleStrategy: typing_extensions.Literal[
        "SAMPLE_STRATEGY_UNSPECIFIED", "UNCERTAINTY"
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SampledShapleyAttribution(
    typing_extensions.TypedDict, total=False
):
    pathCount: int

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SamplingStrategy(
    typing_extensions.TypedDict, total=False
):
    randomSampleConfig: GoogleCloudAiplatformV1beta1SamplingStrategyRandomSampleConfig

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SamplingStrategyRandomSampleConfig(
    typing_extensions.TypedDict, total=False
):
    sampleRate: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SavedQuery(typing_extensions.TypedDict, total=False):
    annotationFilter: str
    annotationSpecCount: int
    createTime: str
    displayName: str
    etag: str
    metadata: typing.Any
    name: str
    problemType: str
    supportAutomlTraining: bool
    updateTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1Scalar(typing_extensions.TypedDict, total=False):
    value: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1Schedule(typing_extensions.TypedDict, total=False):
    allowQueueing: bool
    catchUp: bool
    createPipelineJobRequest: GoogleCloudAiplatformV1beta1CreatePipelineJobRequest
    createTime: str
    cron: str
    displayName: str
    endTime: str
    lastPauseTime: str
    lastResumeTime: str
    lastScheduledRunResponse: GoogleCloudAiplatformV1beta1ScheduleRunResponse
    maxConcurrentRunCount: str
    maxRunCount: str
    name: str
    nextRunTime: str
    startTime: str
    startedRunCount: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "ACTIVE", "PAUSED", "COMPLETED"
    ]
    updateTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ScheduleRunResponse(
    typing_extensions.TypedDict, total=False
):
    runResponse: str
    scheduledRunTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1Scheduling(typing_extensions.TypedDict, total=False):
    disableRetries: bool
    restartJobOnWorkerRestart: bool
    timeout: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaAnnotationSpecColor(
    typing_extensions.TypedDict, total=False
):
    color: GoogleTypeColor
    displayName: str
    id: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaImageBoundingBoxAnnotation(
    typing_extensions.TypedDict, total=False
):
    annotationSpecId: str
    displayName: str
    xMax: float
    xMin: float
    yMax: float
    yMin: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaImageClassificationAnnotation(
    typing_extensions.TypedDict, total=False
):
    annotationSpecId: str
    displayName: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaImageDataItem(
    typing_extensions.TypedDict, total=False
):
    gcsUri: str
    mimeType: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaImageDatasetMetadata(
    typing_extensions.TypedDict, total=False
):
    dataItemSchemaUri: str
    gcsBucket: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaImageSegmentationAnnotation(
    typing_extensions.TypedDict, total=False
):
    maskAnnotation: GoogleCloudAiplatformV1beta1SchemaImageSegmentationAnnotationMaskAnnotation
    polygonAnnotation: GoogleCloudAiplatformV1beta1SchemaImageSegmentationAnnotationPolygonAnnotation
    polylineAnnotation: GoogleCloudAiplatformV1beta1SchemaImageSegmentationAnnotationPolylineAnnotation

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaImageSegmentationAnnotationMaskAnnotation(
    typing_extensions.TypedDict, total=False
):
    annotationSpecColors: _list[GoogleCloudAiplatformV1beta1SchemaAnnotationSpecColor]
    maskGcsUri: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaImageSegmentationAnnotationPolygonAnnotation(
    typing_extensions.TypedDict, total=False
):
    annotationSpecId: str
    displayName: str
    vertexes: _list[GoogleCloudAiplatformV1beta1SchemaVertex]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaImageSegmentationAnnotationPolylineAnnotation(
    typing_extensions.TypedDict, total=False
):
    annotationSpecId: str
    displayName: str
    vertexes: _list[GoogleCloudAiplatformV1beta1SchemaVertex]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaModelevaluationMetricsBoundingBoxMetrics(
    typing_extensions.TypedDict, total=False
):
    confidenceMetrics: _list[
        GoogleCloudAiplatformV1beta1SchemaModelevaluationMetricsBoundingBoxMetricsConfidenceMetrics
    ]
    iouThreshold: float
    meanAveragePrecision: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaModelevaluationMetricsBoundingBoxMetricsConfidenceMetrics(
    typing_extensions.TypedDict, total=False
):
    confidenceThreshold: float
    f1Score: float
    precision: float
    recall: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaModelevaluationMetricsClassificationEvaluationMetrics(
    typing_extensions.TypedDict, total=False
):
    auPrc: float
    auRoc: float
    confidenceMetrics: _list[
        GoogleCloudAiplatformV1beta1SchemaModelevaluationMetricsClassificationEvaluationMetricsConfidenceMetrics
    ]
    confusionMatrix: GoogleCloudAiplatformV1beta1SchemaModelevaluationMetricsConfusionMatrix
    logLoss: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaModelevaluationMetricsClassificationEvaluationMetricsConfidenceMetrics(
    typing_extensions.TypedDict, total=False
):
    confidenceThreshold: float
    confusionMatrix: GoogleCloudAiplatformV1beta1SchemaModelevaluationMetricsConfusionMatrix
    f1Score: float
    f1ScoreAt1: float
    f1ScoreMacro: float
    f1ScoreMicro: float
    falseNegativeCount: str
    falsePositiveCount: str
    falsePositiveRate: float
    falsePositiveRateAt1: float
    maxPredictions: int
    precision: float
    precisionAt1: float
    recall: float
    recallAt1: float
    trueNegativeCount: str
    truePositiveCount: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaModelevaluationMetricsConfusionMatrix(
    typing_extensions.TypedDict, total=False
):
    annotationSpecs: _list[
        GoogleCloudAiplatformV1beta1SchemaModelevaluationMetricsConfusionMatrixAnnotationSpecRef
    ]
    rows: _list[list]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaModelevaluationMetricsConfusionMatrixAnnotationSpecRef(
    typing_extensions.TypedDict, total=False
):
    displayName: str
    id: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaModelevaluationMetricsForecastingEvaluationMetrics(
    typing_extensions.TypedDict, total=False
):
    meanAbsoluteError: float
    meanAbsolutePercentageError: float
    quantileMetrics: _list[
        GoogleCloudAiplatformV1beta1SchemaModelevaluationMetricsForecastingEvaluationMetricsQuantileMetricsEntry
    ]
    rSquared: float
    rootMeanSquaredError: float
    rootMeanSquaredLogError: float
    rootMeanSquaredPercentageError: float
    weightedAbsolutePercentageError: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaModelevaluationMetricsForecastingEvaluationMetricsQuantileMetricsEntry(
    typing_extensions.TypedDict, total=False
):
    observedQuantile: float
    quantile: float
    scaledPinballLoss: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaModelevaluationMetricsGeneralTextGenerationEvaluationMetrics(
    typing_extensions.TypedDict, total=False
):
    bleu: float
    rougeLSum: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaModelevaluationMetricsImageObjectDetectionEvaluationMetrics(
    typing_extensions.TypedDict, total=False
):
    boundingBoxMeanAveragePrecision: float
    boundingBoxMetrics: _list[
        GoogleCloudAiplatformV1beta1SchemaModelevaluationMetricsBoundingBoxMetrics
    ]
    evaluatedBoundingBoxCount: int

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaModelevaluationMetricsImageSegmentationEvaluationMetrics(
    typing_extensions.TypedDict, total=False
):
    confidenceMetricsEntries: _list[
        GoogleCloudAiplatformV1beta1SchemaModelevaluationMetricsImageSegmentationEvaluationMetricsConfidenceMetricsEntry
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaModelevaluationMetricsImageSegmentationEvaluationMetricsConfidenceMetricsEntry(
    typing_extensions.TypedDict, total=False
):
    confidenceThreshold: float
    confusionMatrix: GoogleCloudAiplatformV1beta1SchemaModelevaluationMetricsConfusionMatrix
    diceScoreCoefficient: float
    iouScore: float
    precision: float
    recall: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaModelevaluationMetricsQuestionAnsweringEvaluationMetrics(
    typing_extensions.TypedDict, total=False
):
    exactMatch: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaModelevaluationMetricsRegressionEvaluationMetrics(
    typing_extensions.TypedDict, total=False
):
    meanAbsoluteError: float
    meanAbsolutePercentageError: float
    rSquared: float
    rootMeanSquaredError: float
    rootMeanSquaredLogError: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaModelevaluationMetricsSummarizationEvaluationMetrics(
    typing_extensions.TypedDict, total=False
):
    rougeLSum: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaModelevaluationMetricsTextExtractionEvaluationMetrics(
    typing_extensions.TypedDict, total=False
):
    confidenceMetrics: _list[
        GoogleCloudAiplatformV1beta1SchemaModelevaluationMetricsTextExtractionEvaluationMetricsConfidenceMetrics
    ]
    confusionMatrix: GoogleCloudAiplatformV1beta1SchemaModelevaluationMetricsConfusionMatrix

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaModelevaluationMetricsTextExtractionEvaluationMetricsConfidenceMetrics(
    typing_extensions.TypedDict, total=False
):
    confidenceThreshold: float
    f1Score: float
    precision: float
    recall: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaModelevaluationMetricsTextSentimentEvaluationMetrics(
    typing_extensions.TypedDict, total=False
):
    confusionMatrix: GoogleCloudAiplatformV1beta1SchemaModelevaluationMetricsConfusionMatrix
    f1Score: float
    linearKappa: float
    meanAbsoluteError: float
    meanSquaredError: float
    precision: float
    quadraticKappa: float
    recall: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaModelevaluationMetricsTrackMetrics(
    typing_extensions.TypedDict, total=False
):
    confidenceMetrics: _list[
        GoogleCloudAiplatformV1beta1SchemaModelevaluationMetricsTrackMetricsConfidenceMetrics
    ]
    iouThreshold: float
    meanBoundingBoxIou: float
    meanMismatchRate: float
    meanTrackingAveragePrecision: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaModelevaluationMetricsTrackMetricsConfidenceMetrics(
    typing_extensions.TypedDict, total=False
):
    boundingBoxIou: float
    confidenceThreshold: float
    mismatchRate: float
    trackingPrecision: float
    trackingRecall: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaModelevaluationMetricsVideoActionMetrics(
    typing_extensions.TypedDict, total=False
):
    confidenceMetrics: _list[
        GoogleCloudAiplatformV1beta1SchemaModelevaluationMetricsVideoActionMetricsConfidenceMetrics
    ]
    meanAveragePrecision: float
    precisionWindowLength: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaModelevaluationMetricsVideoActionMetricsConfidenceMetrics(
    typing_extensions.TypedDict, total=False
):
    confidenceThreshold: float
    f1Score: float
    precision: float
    recall: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaModelevaluationMetricsVideoActionRecognitionMetrics(
    typing_extensions.TypedDict, total=False
):
    evaluatedActionCount: int
    videoActionMetrics: _list[
        GoogleCloudAiplatformV1beta1SchemaModelevaluationMetricsVideoActionMetrics
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaModelevaluationMetricsVideoObjectTrackingMetrics(
    typing_extensions.TypedDict, total=False
):
    boundingBoxMeanAveragePrecision: float
    boundingBoxMetrics: _list[
        GoogleCloudAiplatformV1beta1SchemaModelevaluationMetricsBoundingBoxMetrics
    ]
    evaluatedBoundingBoxCount: int
    evaluatedFrameCount: int
    evaluatedTrackCount: int
    trackMeanAveragePrecision: float
    trackMeanBoundingBoxIou: float
    trackMeanMismatchRate: float
    trackMetrics: _list[
        GoogleCloudAiplatformV1beta1SchemaModelevaluationMetricsTrackMetrics
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaPredictInstanceImageClassificationPredictionInstance(
    typing_extensions.TypedDict, total=False
):
    content: str
    mimeType: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaPredictInstanceImageObjectDetectionPredictionInstance(
    typing_extensions.TypedDict, total=False
):
    content: str
    mimeType: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaPredictInstanceImageSegmentationPredictionInstance(
    typing_extensions.TypedDict, total=False
):
    content: str
    mimeType: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaPredictInstanceTextClassificationPredictionInstance(
    typing_extensions.TypedDict, total=False
):
    content: str
    mimeType: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaPredictInstanceTextExtractionPredictionInstance(
    typing_extensions.TypedDict, total=False
):
    content: str
    key: str
    mimeType: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaPredictInstanceTextSentimentPredictionInstance(
    typing_extensions.TypedDict, total=False
):
    content: str
    mimeType: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaPredictInstanceVideoActionRecognitionPredictionInstance(
    typing_extensions.TypedDict, total=False
):
    content: str
    mimeType: str
    timeSegmentEnd: str
    timeSegmentStart: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaPredictInstanceVideoClassificationPredictionInstance(
    typing_extensions.TypedDict, total=False
):
    content: str
    mimeType: str
    timeSegmentEnd: str
    timeSegmentStart: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaPredictInstanceVideoObjectTrackingPredictionInstance(
    typing_extensions.TypedDict, total=False
):
    content: str
    mimeType: str
    timeSegmentEnd: str
    timeSegmentStart: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaPredictParamsImageClassificationPredictionParams(
    typing_extensions.TypedDict, total=False
):
    confidenceThreshold: float
    maxPredictions: int

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaPredictParamsImageObjectDetectionPredictionParams(
    typing_extensions.TypedDict, total=False
):
    confidenceThreshold: float
    maxPredictions: int

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaPredictParamsImageSegmentationPredictionParams(
    typing_extensions.TypedDict, total=False
):
    confidenceThreshold: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaPredictParamsVideoActionRecognitionPredictionParams(
    typing_extensions.TypedDict, total=False
):
    confidenceThreshold: float
    maxPredictions: int

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaPredictParamsVideoClassificationPredictionParams(
    typing_extensions.TypedDict, total=False
):
    confidenceThreshold: float
    maxPredictions: int
    oneSecIntervalClassification: bool
    segmentClassification: bool
    shotClassification: bool

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaPredictParamsVideoObjectTrackingPredictionParams(
    typing_extensions.TypedDict, total=False
):
    confidenceThreshold: float
    maxPredictions: int
    minBoundingBoxSize: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaPredictPredictionClassificationPredictionResult(
    typing_extensions.TypedDict, total=False
):
    confidences: _list[float]
    displayNames: _list[str]
    ids: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaPredictPredictionImageObjectDetectionPredictionResult(
    typing_extensions.TypedDict, total=False
):
    bboxes: _list[list]
    confidences: _list[float]
    displayNames: _list[str]
    ids: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaPredictPredictionImageSegmentationPredictionResult(
    typing_extensions.TypedDict, total=False
):
    categoryMask: str
    confidenceMask: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaPredictPredictionTabularClassificationPredictionResult(
    typing_extensions.TypedDict, total=False
):
    classes: _list[str]
    scores: _list[float]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaPredictPredictionTabularRegressionPredictionResult(
    typing_extensions.TypedDict, total=False
):
    lowerBound: float
    quantilePredictions: _list[float]
    quantileValues: _list[float]
    upperBound: float
    value: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaPredictPredictionTextExtractionPredictionResult(
    typing_extensions.TypedDict, total=False
):
    confidences: _list[float]
    displayNames: _list[str]
    ids: _list[str]
    textSegmentEndOffsets: _list[str]
    textSegmentStartOffsets: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaPredictPredictionTextSentimentPredictionResult(
    typing_extensions.TypedDict, total=False
):
    sentiment: int

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaPredictPredictionTftFeatureImportance(
    typing_extensions.TypedDict, total=False
):
    attributeColumns: _list[str]
    attributeWeights: _list[float]
    contextColumns: _list[str]
    contextWeights: _list[float]
    horizonColumns: _list[str]
    horizonWeights: _list[float]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaPredictPredictionTimeSeriesForecastingPredictionResult(
    typing_extensions.TypedDict, total=False
):
    quantilePredictions: _list[float]
    quantileValues: _list[float]
    tftFeatureImportance: GoogleCloudAiplatformV1beta1SchemaPredictPredictionTftFeatureImportance
    value: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaPredictPredictionVideoActionRecognitionPredictionResult(
    typing_extensions.TypedDict, total=False
):
    confidence: float
    displayName: str
    id: str
    timeSegmentEnd: str
    timeSegmentStart: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaPredictPredictionVideoClassificationPredictionResult(
    typing_extensions.TypedDict, total=False
):
    confidence: float
    displayName: str
    id: str
    timeSegmentEnd: str
    timeSegmentStart: str
    type: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaPredictPredictionVideoObjectTrackingPredictionResult(
    typing_extensions.TypedDict, total=False
):
    confidence: float
    displayName: str
    frames: _list[
        GoogleCloudAiplatformV1beta1SchemaPredictPredictionVideoObjectTrackingPredictionResultFrame
    ]
    id: str
    timeSegmentEnd: str
    timeSegmentStart: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaPredictPredictionVideoObjectTrackingPredictionResultFrame(
    typing_extensions.TypedDict, total=False
):
    timeOffset: str
    xMax: float
    xMin: float
    yMax: float
    yMin: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaPredictionResult(
    typing_extensions.TypedDict, total=False
):
    error: GoogleCloudAiplatformV1beta1SchemaPredictionResultError
    instance: dict[str, typing.Any]
    key: str
    prediction: typing.Any

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaPredictionResultError(
    typing_extensions.TypedDict, total=False
):
    message: str
    status: typing_extensions.Literal[
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

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTablesDatasetMetadata(
    typing_extensions.TypedDict, total=False
):
    inputConfig: GoogleCloudAiplatformV1beta1SchemaTablesDatasetMetadataInputConfig

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTablesDatasetMetadataBigQuerySource(
    typing_extensions.TypedDict, total=False
):
    uri: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTablesDatasetMetadataGcsSource(
    typing_extensions.TypedDict, total=False
):
    uri: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTablesDatasetMetadataInputConfig(
    typing_extensions.TypedDict, total=False
):
    bigquerySource: GoogleCloudAiplatformV1beta1SchemaTablesDatasetMetadataBigQuerySource
    gcsSource: GoogleCloudAiplatformV1beta1SchemaTablesDatasetMetadataGcsSource

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTextClassificationAnnotation(
    typing_extensions.TypedDict, total=False
):
    annotationSpecId: str
    displayName: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTextDataItem(
    typing_extensions.TypedDict, total=False
):
    gcsUri: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTextDatasetMetadata(
    typing_extensions.TypedDict, total=False
):
    dataItemSchemaUri: str
    gcsBucket: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTextExtractionAnnotation(
    typing_extensions.TypedDict, total=False
):
    annotationSpecId: str
    displayName: str
    textSegment: GoogleCloudAiplatformV1beta1SchemaTextSegment

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTextSegment(
    typing_extensions.TypedDict, total=False
):
    content: str
    endOffset: str
    startOffset: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTextSentimentAnnotation(
    typing_extensions.TypedDict, total=False
):
    annotationSpecId: str
    displayName: str
    sentiment: int
    sentimentMax: int

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTextSentimentSavedQueryMetadata(
    typing_extensions.TypedDict, total=False
):
    sentimentMax: int

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTimeSegment(
    typing_extensions.TypedDict, total=False
):
    endTimeOffset: str
    startTimeOffset: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTimeSeriesDatasetMetadata(
    typing_extensions.TypedDict, total=False
):
    inputConfig: GoogleCloudAiplatformV1beta1SchemaTimeSeriesDatasetMetadataInputConfig
    timeColumn: str
    timeSeriesIdentifierColumn: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTimeSeriesDatasetMetadataBigQuerySource(
    typing_extensions.TypedDict, total=False
):
    uri: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTimeSeriesDatasetMetadataGcsSource(
    typing_extensions.TypedDict, total=False
):
    uri: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTimeSeriesDatasetMetadataInputConfig(
    typing_extensions.TypedDict, total=False
):
    bigquerySource: GoogleCloudAiplatformV1beta1SchemaTimeSeriesDatasetMetadataBigQuerySource
    gcsSource: GoogleCloudAiplatformV1beta1SchemaTimeSeriesDatasetMetadataGcsSource

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlForecasting(
    typing_extensions.TypedDict, total=False
):
    inputs: GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlForecastingInputs
    metadata: GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlForecastingMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlForecastingInputs(
    typing_extensions.TypedDict, total=False
):
    additionalExperiments: _list[str]
    availableAtForecastColumns: _list[str]
    contextWindow: str
    dataGranularity: GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlForecastingInputsGranularity
    enableProbabilisticInference: bool
    exportEvaluatedDataItemsConfig: GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionExportEvaluatedDataItemsConfig
    forecastHorizon: str
    hierarchyConfig: GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionHierarchyConfig
    holidayRegions: _list[str]
    optimizationObjective: str
    quantiles: _list[float]
    targetColumn: str
    timeColumn: str
    timeSeriesAttributeColumns: _list[str]
    timeSeriesIdentifierColumn: str
    trainBudgetMilliNodeHours: str
    transformations: _list[
        GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlForecastingInputsTransformation
    ]
    unavailableAtForecastColumns: _list[str]
    validationOptions: str
    weightColumn: str
    windowConfig: GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionWindowConfig

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlForecastingInputsGranularity(
    typing_extensions.TypedDict, total=False
):
    quantity: str
    unit: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlForecastingInputsTransformation(
    typing_extensions.TypedDict, total=False
):
    auto: GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlForecastingInputsTransformationAutoTransformation
    categorical: GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlForecastingInputsTransformationCategoricalTransformation
    numeric: GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlForecastingInputsTransformationNumericTransformation
    text: GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlForecastingInputsTransformationTextTransformation
    timestamp: GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlForecastingInputsTransformationTimestampTransformation

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlForecastingInputsTransformationAutoTransformation(
    typing_extensions.TypedDict, total=False
):
    columnName: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlForecastingInputsTransformationCategoricalTransformation(
    typing_extensions.TypedDict, total=False
):
    columnName: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlForecastingInputsTransformationNumericTransformation(
    typing_extensions.TypedDict, total=False
):
    columnName: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlForecastingInputsTransformationTextTransformation(
    typing_extensions.TypedDict, total=False
):
    columnName: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlForecastingInputsTransformationTimestampTransformation(
    typing_extensions.TypedDict, total=False
):
    columnName: str
    timeFormat: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlForecastingMetadata(
    typing_extensions.TypedDict, total=False
):
    evaluatedDataItemsBigqueryUri: str
    trainCostMilliNodeHours: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlImageClassification(
    typing_extensions.TypedDict, total=False
):
    inputs: GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlImageClassificationInputs
    metadata: GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlImageClassificationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlImageClassificationInputs(
    typing_extensions.TypedDict, total=False
):
    baseModelId: str
    budgetMilliNodeHours: str
    disableEarlyStopping: bool
    modelType: typing_extensions.Literal[
        "MODEL_TYPE_UNSPECIFIED",
        "CLOUD",
        "CLOUD_1",
        "MOBILE_TF_LOW_LATENCY_1",
        "MOBILE_TF_VERSATILE_1",
        "MOBILE_TF_HIGH_ACCURACY_1",
        "EFFICIENTNET",
        "MAXVIT",
        "VIT",
        "COCA",
    ]
    multiLabel: bool
    tunableParameter: GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutomlImageTrainingTunableParameter
    uptrainBaseModelId: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlImageClassificationMetadata(
    typing_extensions.TypedDict, total=False
):
    costMilliNodeHours: str
    successfulStopReason: typing_extensions.Literal[
        "SUCCESSFUL_STOP_REASON_UNSPECIFIED", "BUDGET_REACHED", "MODEL_CONVERGED"
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlImageObjectDetection(
    typing_extensions.TypedDict, total=False
):
    inputs: GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlImageObjectDetectionInputs
    metadata: GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlImageObjectDetectionMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlImageObjectDetectionInputs(
    typing_extensions.TypedDict, total=False
):
    budgetMilliNodeHours: str
    disableEarlyStopping: bool
    modelType: typing_extensions.Literal[
        "MODEL_TYPE_UNSPECIFIED",
        "CLOUD_HIGH_ACCURACY_1",
        "CLOUD_LOW_LATENCY_1",
        "CLOUD_1",
        "MOBILE_TF_LOW_LATENCY_1",
        "MOBILE_TF_VERSATILE_1",
        "MOBILE_TF_HIGH_ACCURACY_1",
        "CLOUD_STREAMING_1",
        "SPINENET",
        "YOLO",
    ]
    tunableParameter: GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutomlImageTrainingTunableParameter
    uptrainBaseModelId: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlImageObjectDetectionMetadata(
    typing_extensions.TypedDict, total=False
):
    costMilliNodeHours: str
    successfulStopReason: typing_extensions.Literal[
        "SUCCESSFUL_STOP_REASON_UNSPECIFIED", "BUDGET_REACHED", "MODEL_CONVERGED"
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlImageSegmentation(
    typing_extensions.TypedDict, total=False
):
    inputs: GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlImageSegmentationInputs
    metadata: GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlImageSegmentationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlImageSegmentationInputs(
    typing_extensions.TypedDict, total=False
):
    baseModelId: str
    budgetMilliNodeHours: str
    modelType: typing_extensions.Literal[
        "MODEL_TYPE_UNSPECIFIED",
        "CLOUD_HIGH_ACCURACY_1",
        "CLOUD_LOW_ACCURACY_1",
        "MOBILE_TF_LOW_LATENCY_1",
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlImageSegmentationMetadata(
    typing_extensions.TypedDict, total=False
):
    costMilliNodeHours: str
    successfulStopReason: typing_extensions.Literal[
        "SUCCESSFUL_STOP_REASON_UNSPECIFIED", "BUDGET_REACHED", "MODEL_CONVERGED"
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlTables(
    typing_extensions.TypedDict, total=False
):
    inputs: GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlTablesInputs
    metadata: GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlTablesMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlTablesInputs(
    typing_extensions.TypedDict, total=False
):
    additionalExperiments: _list[str]
    disableEarlyStopping: bool
    exportEvaluatedDataItemsConfig: GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionExportEvaluatedDataItemsConfig
    optimizationObjective: str
    optimizationObjectivePrecisionValue: float
    optimizationObjectiveRecallValue: float
    predictionType: str
    targetColumn: str
    trainBudgetMilliNodeHours: str
    transformations: _list[
        GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlTablesInputsTransformation
    ]
    weightColumnName: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlTablesInputsTransformation(
    typing_extensions.TypedDict, total=False
):
    auto: GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlTablesInputsTransformationAutoTransformation
    categorical: GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlTablesInputsTransformationCategoricalTransformation
    numeric: GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlTablesInputsTransformationNumericTransformation
    repeatedCategorical: GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlTablesInputsTransformationCategoricalArrayTransformation
    repeatedNumeric: GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlTablesInputsTransformationNumericArrayTransformation
    repeatedText: GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlTablesInputsTransformationTextArrayTransformation
    text: GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlTablesInputsTransformationTextTransformation
    timestamp: GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlTablesInputsTransformationTimestampTransformation

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlTablesInputsTransformationAutoTransformation(
    typing_extensions.TypedDict, total=False
):
    columnName: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlTablesInputsTransformationCategoricalArrayTransformation(
    typing_extensions.TypedDict, total=False
):
    columnName: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlTablesInputsTransformationCategoricalTransformation(
    typing_extensions.TypedDict, total=False
):
    columnName: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlTablesInputsTransformationNumericArrayTransformation(
    typing_extensions.TypedDict, total=False
):
    columnName: str
    invalidValuesAllowed: bool

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlTablesInputsTransformationNumericTransformation(
    typing_extensions.TypedDict, total=False
):
    columnName: str
    invalidValuesAllowed: bool

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlTablesInputsTransformationTextArrayTransformation(
    typing_extensions.TypedDict, total=False
):
    columnName: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlTablesInputsTransformationTextTransformation(
    typing_extensions.TypedDict, total=False
):
    columnName: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlTablesInputsTransformationTimestampTransformation(
    typing_extensions.TypedDict, total=False
):
    columnName: str
    invalidValuesAllowed: bool
    timeFormat: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlTablesMetadata(
    typing_extensions.TypedDict, total=False
):
    evaluatedDataItemsBigqueryUri: str
    trainCostMilliNodeHours: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlTextClassification(
    typing_extensions.TypedDict, total=False
):
    inputs: GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlTextClassificationInputs

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlTextClassificationInputs(
    typing_extensions.TypedDict, total=False
):
    multiLabel: bool

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlTextExtraction(
    typing_extensions.TypedDict, total=False
):
    inputs: GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlTextExtractionInputs

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlTextExtractionInputs(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlTextSentiment(
    typing_extensions.TypedDict, total=False
):
    inputs: GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlTextSentimentInputs

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlTextSentimentInputs(
    typing_extensions.TypedDict, total=False
):
    sentimentMax: int

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlVideoActionRecognition(
    typing_extensions.TypedDict, total=False
):
    inputs: GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlVideoActionRecognitionInputs

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlVideoActionRecognitionInputs(
    typing_extensions.TypedDict, total=False
):
    modelType: typing_extensions.Literal[
        "MODEL_TYPE_UNSPECIFIED",
        "CLOUD",
        "MOBILE_VERSATILE_1",
        "MOBILE_JETSON_VERSATILE_1",
        "MOBILE_CORAL_VERSATILE_1",
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlVideoClassification(
    typing_extensions.TypedDict, total=False
):
    inputs: GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlVideoClassificationInputs

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlVideoClassificationInputs(
    typing_extensions.TypedDict, total=False
):
    modelType: typing_extensions.Literal[
        "MODEL_TYPE_UNSPECIFIED",
        "CLOUD",
        "MOBILE_VERSATILE_1",
        "MOBILE_JETSON_VERSATILE_1",
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlVideoObjectTracking(
    typing_extensions.TypedDict, total=False
):
    inputs: GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlVideoObjectTrackingInputs

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlVideoObjectTrackingInputs(
    typing_extensions.TypedDict, total=False
):
    modelType: typing_extensions.Literal[
        "MODEL_TYPE_UNSPECIFIED",
        "CLOUD",
        "MOBILE_VERSATILE_1",
        "MOBILE_CORAL_VERSATILE_1",
        "MOBILE_CORAL_LOW_LATENCY_1",
        "MOBILE_JETSON_VERSATILE_1",
        "MOBILE_JETSON_LOW_LATENCY_1",
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutomlImageTrainingTunableParameter(
    typing_extensions.TypedDict, total=False
):
    checkpointName: str
    datasetConfig: dict[str, typing.Any]
    studySpec: GoogleCloudAiplatformV1beta1StudySpec
    trainerConfig: dict[str, typing.Any]
    trainerType: typing_extensions.Literal[
        "TRAINER_TYPE_UNSPECIFIED", "AUTOML_TRAINER", "MODEL_GARDEN_TRAINER"
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionCustomJobMetadata(
    typing_extensions.TypedDict, total=False
):
    backingCustomJob: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionCustomTask(
    typing_extensions.TypedDict, total=False
):
    inputs: GoogleCloudAiplatformV1beta1CustomJobSpec
    metadata: GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionCustomJobMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionExportEvaluatedDataItemsConfig(
    typing_extensions.TypedDict, total=False
):
    destinationBigqueryUri: str
    overrideExistingTable: bool

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionHierarchyConfig(
    typing_extensions.TypedDict, total=False
):
    groupColumns: _list[str]
    groupTemporalTotalWeight: float
    groupTotalWeight: float
    temporalTotalWeight: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionHyperparameterTuningJobMetadata(
    typing_extensions.TypedDict, total=False
):
    backingHyperparameterTuningJob: str
    bestTrialBackingCustomJob: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionHyperparameterTuningJobSpec(
    typing_extensions.TypedDict, total=False
):
    maxFailedTrialCount: int
    maxTrialCount: int
    parallelTrialCount: int
    studySpec: GoogleCloudAiplatformV1beta1StudySpec
    trialJobSpec: GoogleCloudAiplatformV1beta1CustomJobSpec

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionHyperparameterTuningTask(
    typing_extensions.TypedDict, total=False
):
    inputs: GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionHyperparameterTuningJobSpec
    metadata: GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionHyperparameterTuningJobMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionSeq2SeqPlusForecasting(
    typing_extensions.TypedDict, total=False
):
    inputs: GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionSeq2SeqPlusForecastingInputs
    metadata: GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionSeq2SeqPlusForecastingMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionSeq2SeqPlusForecastingInputs(
    typing_extensions.TypedDict, total=False
):
    additionalExperiments: _list[str]
    availableAtForecastColumns: _list[str]
    contextWindow: str
    dataGranularity: GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionSeq2SeqPlusForecastingInputsGranularity
    exportEvaluatedDataItemsConfig: GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionExportEvaluatedDataItemsConfig
    forecastHorizon: str
    hierarchyConfig: GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionHierarchyConfig
    holidayRegions: _list[str]
    optimizationObjective: str
    quantiles: _list[float]
    targetColumn: str
    timeColumn: str
    timeSeriesAttributeColumns: _list[str]
    timeSeriesIdentifierColumn: str
    trainBudgetMilliNodeHours: str
    transformations: _list[
        GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionSeq2SeqPlusForecastingInputsTransformation
    ]
    unavailableAtForecastColumns: _list[str]
    validationOptions: str
    weightColumn: str
    windowConfig: GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionWindowConfig

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionSeq2SeqPlusForecastingInputsGranularity(
    typing_extensions.TypedDict, total=False
):
    quantity: str
    unit: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionSeq2SeqPlusForecastingInputsTransformation(
    typing_extensions.TypedDict, total=False
):
    auto: GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionSeq2SeqPlusForecastingInputsTransformationAutoTransformation
    categorical: GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionSeq2SeqPlusForecastingInputsTransformationCategoricalTransformation
    numeric: GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionSeq2SeqPlusForecastingInputsTransformationNumericTransformation
    text: GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionSeq2SeqPlusForecastingInputsTransformationTextTransformation
    timestamp: GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionSeq2SeqPlusForecastingInputsTransformationTimestampTransformation

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionSeq2SeqPlusForecastingInputsTransformationAutoTransformation(
    typing_extensions.TypedDict, total=False
):
    columnName: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionSeq2SeqPlusForecastingInputsTransformationCategoricalTransformation(
    typing_extensions.TypedDict, total=False
):
    columnName: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionSeq2SeqPlusForecastingInputsTransformationNumericTransformation(
    typing_extensions.TypedDict, total=False
):
    columnName: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionSeq2SeqPlusForecastingInputsTransformationTextTransformation(
    typing_extensions.TypedDict, total=False
):
    columnName: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionSeq2SeqPlusForecastingInputsTransformationTimestampTransformation(
    typing_extensions.TypedDict, total=False
):
    columnName: str
    timeFormat: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionSeq2SeqPlusForecastingMetadata(
    typing_extensions.TypedDict, total=False
):
    evaluatedDataItemsBigqueryUri: str
    trainCostMilliNodeHours: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionTftForecasting(
    typing_extensions.TypedDict, total=False
):
    inputs: GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionTftForecastingInputs
    metadata: GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionTftForecastingMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionTftForecastingInputs(
    typing_extensions.TypedDict, total=False
):
    additionalExperiments: _list[str]
    availableAtForecastColumns: _list[str]
    contextWindow: str
    dataGranularity: GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionTftForecastingInputsGranularity
    exportEvaluatedDataItemsConfig: GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionExportEvaluatedDataItemsConfig
    forecastHorizon: str
    hierarchyConfig: GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionHierarchyConfig
    holidayRegions: _list[str]
    optimizationObjective: str
    quantiles: _list[float]
    targetColumn: str
    timeColumn: str
    timeSeriesAttributeColumns: _list[str]
    timeSeriesIdentifierColumn: str
    trainBudgetMilliNodeHours: str
    transformations: _list[
        GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionTftForecastingInputsTransformation
    ]
    unavailableAtForecastColumns: _list[str]
    validationOptions: str
    weightColumn: str
    windowConfig: GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionWindowConfig

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionTftForecastingInputsGranularity(
    typing_extensions.TypedDict, total=False
):
    quantity: str
    unit: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionTftForecastingInputsTransformation(
    typing_extensions.TypedDict, total=False
):
    auto: GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionTftForecastingInputsTransformationAutoTransformation
    categorical: GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionTftForecastingInputsTransformationCategoricalTransformation
    numeric: GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionTftForecastingInputsTransformationNumericTransformation
    text: GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionTftForecastingInputsTransformationTextTransformation
    timestamp: GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionTftForecastingInputsTransformationTimestampTransformation

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionTftForecastingInputsTransformationAutoTransformation(
    typing_extensions.TypedDict, total=False
):
    columnName: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionTftForecastingInputsTransformationCategoricalTransformation(
    typing_extensions.TypedDict, total=False
):
    columnName: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionTftForecastingInputsTransformationNumericTransformation(
    typing_extensions.TypedDict, total=False
):
    columnName: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionTftForecastingInputsTransformationTextTransformation(
    typing_extensions.TypedDict, total=False
):
    columnName: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionTftForecastingInputsTransformationTimestampTransformation(
    typing_extensions.TypedDict, total=False
):
    columnName: str
    timeFormat: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionTftForecastingMetadata(
    typing_extensions.TypedDict, total=False
):
    evaluatedDataItemsBigqueryUri: str
    trainCostMilliNodeHours: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionWindowConfig(
    typing_extensions.TypedDict, total=False
):
    column: str
    maxCount: str
    strideLength: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaVertex(
    typing_extensions.TypedDict, total=False
):
    x: float
    y: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaVideoActionRecognitionAnnotation(
    typing_extensions.TypedDict, total=False
):
    annotationSpecId: str
    displayName: str
    timeSegment: GoogleCloudAiplatformV1beta1SchemaTimeSegment

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaVideoClassificationAnnotation(
    typing_extensions.TypedDict, total=False
):
    annotationSpecId: str
    displayName: str
    timeSegment: GoogleCloudAiplatformV1beta1SchemaTimeSegment

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaVideoDataItem(
    typing_extensions.TypedDict, total=False
):
    gcsUri: str
    mimeType: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaVideoDatasetMetadata(
    typing_extensions.TypedDict, total=False
):
    dataItemSchemaUri: str
    gcsBucket: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaVideoObjectTrackingAnnotation(
    typing_extensions.TypedDict, total=False
):
    annotationSpecId: str
    displayName: str
    instanceId: str
    timeOffset: str
    xMax: float
    xMin: float
    yMax: float
    yMin: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaVisualInspectionClassificationLabelSavedQueryMetadata(
    typing_extensions.TypedDict, total=False
):
    multiLabel: bool

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SchemaVisualInspectionMaskSavedQueryMetadata(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SearchDataItemsResponse(
    typing_extensions.TypedDict, total=False
):
    dataItemViews: _list[GoogleCloudAiplatformV1beta1DataItemView]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SearchFeaturesResponse(
    typing_extensions.TypedDict, total=False
):
    features: _list[GoogleCloudAiplatformV1beta1Feature]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SearchMigratableResourcesRequest(
    typing_extensions.TypedDict, total=False
):
    filter: str
    pageSize: int
    pageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SearchMigratableResourcesResponse(
    typing_extensions.TypedDict, total=False
):
    migratableResources: _list[GoogleCloudAiplatformV1beta1MigratableResource]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SearchModelDeploymentMonitoringStatsAnomaliesRequest(
    typing_extensions.TypedDict, total=False
):
    deployedModelId: str
    endTime: str
    featureDisplayName: str
    objectives: _list[
        GoogleCloudAiplatformV1beta1SearchModelDeploymentMonitoringStatsAnomaliesRequestStatsAnomaliesObjective
    ]
    pageSize: int
    pageToken: str
    startTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SearchModelDeploymentMonitoringStatsAnomaliesRequestStatsAnomaliesObjective(
    typing_extensions.TypedDict, total=False
):
    topFeatureCount: int
    type: typing_extensions.Literal[
        "MODEL_DEPLOYMENT_MONITORING_OBJECTIVE_TYPE_UNSPECIFIED",
        "RAW_FEATURE_SKEW",
        "RAW_FEATURE_DRIFT",
        "FEATURE_ATTRIBUTION_SKEW",
        "FEATURE_ATTRIBUTION_DRIFT",
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SearchModelDeploymentMonitoringStatsAnomaliesResponse(
    typing_extensions.TypedDict, total=False
):
    monitoringStats: _list[GoogleCloudAiplatformV1beta1ModelMonitoringStatsAnomalies]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ServiceAccountSpec(
    typing_extensions.TypedDict, total=False
):
    enableCustomServiceAccount: bool
    serviceAccount: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SmoothGradConfig(
    typing_extensions.TypedDict, total=False
):
    featureNoiseSigma: GoogleCloudAiplatformV1beta1FeatureNoiseSigma
    noiseSigma: float
    noisySampleCount: int

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SpecialistPool(
    typing_extensions.TypedDict, total=False
):
    displayName: str
    name: str
    pendingDataLabelingJobs: _list[str]
    specialistManagerEmails: _list[str]
    specialistManagersCount: int
    specialistWorkerEmails: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1StartNotebookRuntimeOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata
    progressMessage: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1StartNotebookRuntimeRequest(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1StopTrialRequest(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1StratifiedSplit(
    typing_extensions.TypedDict, total=False
):
    key: str
    testFraction: float
    trainingFraction: float
    validationFraction: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1StreamingPredictRequest(
    typing_extensions.TypedDict, total=False
):
    inputs: _list[GoogleCloudAiplatformV1beta1Tensor]
    parameters: GoogleCloudAiplatformV1beta1Tensor

@typing.type_check_only
class GoogleCloudAiplatformV1beta1StreamingPredictResponse(
    typing_extensions.TypedDict, total=False
):
    outputs: _list[GoogleCloudAiplatformV1beta1Tensor]
    parameters: GoogleCloudAiplatformV1beta1Tensor

@typing.type_check_only
class GoogleCloudAiplatformV1beta1StreamingReadFeatureValuesRequest(
    typing_extensions.TypedDict, total=False
):
    entityIds: _list[str]
    featureSelector: GoogleCloudAiplatformV1beta1FeatureSelector

@typing.type_check_only
class GoogleCloudAiplatformV1beta1StringArray(typing_extensions.TypedDict, total=False):
    values: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1Study(typing_extensions.TypedDict, total=False):
    createTime: str
    displayName: str
    inactiveReason: str
    name: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "ACTIVE", "INACTIVE", "COMPLETED"
    ]
    studySpec: GoogleCloudAiplatformV1beta1StudySpec

@typing.type_check_only
class GoogleCloudAiplatformV1beta1StudySpec(typing_extensions.TypedDict, total=False):
    algorithm: typing_extensions.Literal[
        "ALGORITHM_UNSPECIFIED", "GRID_SEARCH", "RANDOM_SEARCH"
    ]
    convexAutomatedStoppingSpec: GoogleCloudAiplatformV1beta1StudySpecConvexAutomatedStoppingSpec
    convexStopConfig: GoogleCloudAiplatformV1beta1StudySpecConvexStopConfig
    decayCurveStoppingSpec: GoogleCloudAiplatformV1beta1StudySpecDecayCurveAutomatedStoppingSpec
    measurementSelectionType: typing_extensions.Literal[
        "MEASUREMENT_SELECTION_TYPE_UNSPECIFIED", "LAST_MEASUREMENT", "BEST_MEASUREMENT"
    ]
    medianAutomatedStoppingSpec: GoogleCloudAiplatformV1beta1StudySpecMedianAutomatedStoppingSpec
    metrics: _list[GoogleCloudAiplatformV1beta1StudySpecMetricSpec]
    observationNoise: typing_extensions.Literal[
        "OBSERVATION_NOISE_UNSPECIFIED", "LOW", "HIGH"
    ]
    parameters: _list[GoogleCloudAiplatformV1beta1StudySpecParameterSpec]
    transferLearningConfig: GoogleCloudAiplatformV1beta1StudySpecTransferLearningConfig

@typing.type_check_only
class GoogleCloudAiplatformV1beta1StudySpecConvexAutomatedStoppingSpec(
    typing_extensions.TypedDict, total=False
):
    learningRateParameterName: str
    maxStepCount: str
    minMeasurementCount: str
    minStepCount: str
    updateAllStoppedTrials: bool
    useElapsedDuration: bool

@typing.type_check_only
class GoogleCloudAiplatformV1beta1StudySpecConvexStopConfig(
    typing_extensions.TypedDict, total=False
):
    autoregressiveOrder: str
    learningRateParameterName: str
    maxNumSteps: str
    minNumSteps: str
    useSeconds: bool

@typing.type_check_only
class GoogleCloudAiplatformV1beta1StudySpecDecayCurveAutomatedStoppingSpec(
    typing_extensions.TypedDict, total=False
):
    useElapsedDuration: bool

@typing.type_check_only
class GoogleCloudAiplatformV1beta1StudySpecMedianAutomatedStoppingSpec(
    typing_extensions.TypedDict, total=False
):
    useElapsedDuration: bool

@typing.type_check_only
class GoogleCloudAiplatformV1beta1StudySpecMetricSpec(
    typing_extensions.TypedDict, total=False
):
    goal: typing_extensions.Literal["GOAL_TYPE_UNSPECIFIED", "MAXIMIZE", "MINIMIZE"]
    metricId: str
    safetyConfig: GoogleCloudAiplatformV1beta1StudySpecMetricSpecSafetyMetricConfig

@typing.type_check_only
class GoogleCloudAiplatformV1beta1StudySpecMetricSpecSafetyMetricConfig(
    typing_extensions.TypedDict, total=False
):
    desiredMinSafeTrialsFraction: float
    safetyThreshold: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1StudySpecParameterSpec(
    typing_extensions.TypedDict, total=False
):
    categoricalValueSpec: GoogleCloudAiplatformV1beta1StudySpecParameterSpecCategoricalValueSpec
    conditionalParameterSpecs: _list[
        GoogleCloudAiplatformV1beta1StudySpecParameterSpecConditionalParameterSpec
    ]
    discreteValueSpec: GoogleCloudAiplatformV1beta1StudySpecParameterSpecDiscreteValueSpec
    doubleValueSpec: GoogleCloudAiplatformV1beta1StudySpecParameterSpecDoubleValueSpec
    integerValueSpec: GoogleCloudAiplatformV1beta1StudySpecParameterSpecIntegerValueSpec
    parameterId: str
    scaleType: typing_extensions.Literal[
        "SCALE_TYPE_UNSPECIFIED",
        "UNIT_LINEAR_SCALE",
        "UNIT_LOG_SCALE",
        "UNIT_REVERSE_LOG_SCALE",
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1StudySpecParameterSpecCategoricalValueSpec(
    typing_extensions.TypedDict, total=False
):
    defaultValue: str
    values: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1StudySpecParameterSpecConditionalParameterSpec(
    typing_extensions.TypedDict, total=False
):
    parameterSpec: GoogleCloudAiplatformV1beta1StudySpecParameterSpec
    parentCategoricalValues: GoogleCloudAiplatformV1beta1StudySpecParameterSpecConditionalParameterSpecCategoricalValueCondition
    parentDiscreteValues: GoogleCloudAiplatformV1beta1StudySpecParameterSpecConditionalParameterSpecDiscreteValueCondition
    parentIntValues: GoogleCloudAiplatformV1beta1StudySpecParameterSpecConditionalParameterSpecIntValueCondition

@typing.type_check_only
class GoogleCloudAiplatformV1beta1StudySpecParameterSpecConditionalParameterSpecCategoricalValueCondition(
    typing_extensions.TypedDict, total=False
):
    values: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1StudySpecParameterSpecConditionalParameterSpecDiscreteValueCondition(
    typing_extensions.TypedDict, total=False
):
    values: _list[float]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1StudySpecParameterSpecConditionalParameterSpecIntValueCondition(
    typing_extensions.TypedDict, total=False
):
    values: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1StudySpecParameterSpecDiscreteValueSpec(
    typing_extensions.TypedDict, total=False
):
    defaultValue: float
    values: _list[float]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1StudySpecParameterSpecDoubleValueSpec(
    typing_extensions.TypedDict, total=False
):
    defaultValue: float
    maxValue: float
    minValue: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1StudySpecParameterSpecIntegerValueSpec(
    typing_extensions.TypedDict, total=False
):
    defaultValue: str
    maxValue: str
    minValue: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1StudySpecTransferLearningConfig(
    typing_extensions.TypedDict, total=False
):
    disableTransferLearning: bool
    priorStudyNames: _list[str]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SuggestTrialsMetadata(
    typing_extensions.TypedDict, total=False
):
    clientId: str
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SuggestTrialsRequest(
    typing_extensions.TypedDict, total=False
):
    clientId: str
    contexts: _list[GoogleCloudAiplatformV1beta1TrialContext]
    suggestionCount: int

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SuggestTrialsResponse(
    typing_extensions.TypedDict, total=False
):
    endTime: str
    startTime: str
    studyState: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "ACTIVE", "INACTIVE", "COMPLETED"
    ]
    trials: _list[GoogleCloudAiplatformV1beta1Trial]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1TFRecordDestination(
    typing_extensions.TypedDict, total=False
):
    gcsDestination: GoogleCloudAiplatformV1beta1GcsDestination

@typing.type_check_only
class GoogleCloudAiplatformV1beta1Tensor(typing_extensions.TypedDict, total=False):
    boolVal: _list[bool]
    bytesVal: _list[str]
    doubleVal: _list[float]
    dtype: typing_extensions.Literal[
        "DATA_TYPE_UNSPECIFIED",
        "BOOL",
        "STRING",
        "FLOAT",
        "DOUBLE",
        "INT8",
        "INT16",
        "INT32",
        "INT64",
        "UINT8",
        "UINT16",
        "UINT32",
        "UINT64",
    ]
    floatVal: _list[float]
    int64Val: _list[str]
    intVal: _list[int]
    listVal: _list[GoogleCloudAiplatformV1beta1Tensor]
    shape: _list[str]
    stringVal: _list[str]
    structVal: dict[str, typing.Any]
    tensorVal: str
    uint64Val: _list[str]
    uintVal: _list[int]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1Tensorboard(typing_extensions.TypedDict, total=False):
    blobStoragePathPrefix: str
    createTime: str
    description: str
    displayName: str
    encryptionSpec: GoogleCloudAiplatformV1beta1EncryptionSpec
    etag: str
    isDefault: bool
    labels: dict[str, typing.Any]
    name: str
    runCount: int
    updateTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1TensorboardBlob(
    typing_extensions.TypedDict, total=False
):
    data: str
    id: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1TensorboardBlobSequence(
    typing_extensions.TypedDict, total=False
):
    values: _list[GoogleCloudAiplatformV1beta1TensorboardBlob]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1TensorboardExperiment(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    description: str
    displayName: str
    etag: str
    labels: dict[str, typing.Any]
    name: str
    source: str
    updateTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1TensorboardRun(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    description: str
    displayName: str
    etag: str
    labels: dict[str, typing.Any]
    name: str
    updateTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1TensorboardTensor(
    typing_extensions.TypedDict, total=False
):
    value: str
    versionNumber: int

@typing.type_check_only
class GoogleCloudAiplatformV1beta1TensorboardTimeSeries(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    description: str
    displayName: str
    etag: str
    metadata: GoogleCloudAiplatformV1beta1TensorboardTimeSeriesMetadata
    name: str
    pluginData: str
    pluginName: str
    updateTime: str
    valueType: typing_extensions.Literal[
        "VALUE_TYPE_UNSPECIFIED", "SCALAR", "TENSOR", "BLOB_SEQUENCE"
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1TensorboardTimeSeriesMetadata(
    typing_extensions.TypedDict, total=False
):
    maxBlobSequenceLength: str
    maxStep: str
    maxWallTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ThresholdConfig(
    typing_extensions.TypedDict, total=False
):
    value: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1TimeSeriesData(
    typing_extensions.TypedDict, total=False
):
    tensorboardTimeSeriesId: str
    valueType: typing_extensions.Literal[
        "VALUE_TYPE_UNSPECIFIED", "SCALAR", "TENSOR", "BLOB_SEQUENCE"
    ]
    values: _list[GoogleCloudAiplatformV1beta1TimeSeriesDataPoint]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1TimeSeriesDataPoint(
    typing_extensions.TypedDict, total=False
):
    blobs: GoogleCloudAiplatformV1beta1TensorboardBlobSequence
    scalar: GoogleCloudAiplatformV1beta1Scalar
    step: str
    tensor: GoogleCloudAiplatformV1beta1TensorboardTensor
    wallTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1TimestampSplit(
    typing_extensions.TypedDict, total=False
):
    key: str
    testFraction: float
    trainingFraction: float
    validationFraction: float

@typing.type_check_only
class GoogleCloudAiplatformV1beta1TrainingConfig(
    typing_extensions.TypedDict, total=False
):
    timeoutTrainingMilliHours: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1TrainingPipeline(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    displayName: str
    encryptionSpec: GoogleCloudAiplatformV1beta1EncryptionSpec
    endTime: str
    error: GoogleRpcStatus
    inputDataConfig: GoogleCloudAiplatformV1beta1InputDataConfig
    labels: dict[str, typing.Any]
    modelId: str
    modelToUpload: GoogleCloudAiplatformV1beta1Model
    name: str
    parentModel: str
    startTime: str
    state: typing_extensions.Literal[
        "PIPELINE_STATE_UNSPECIFIED",
        "PIPELINE_STATE_QUEUED",
        "PIPELINE_STATE_PENDING",
        "PIPELINE_STATE_RUNNING",
        "PIPELINE_STATE_SUCCEEDED",
        "PIPELINE_STATE_FAILED",
        "PIPELINE_STATE_CANCELLING",
        "PIPELINE_STATE_CANCELLED",
        "PIPELINE_STATE_PAUSED",
    ]
    trainingTaskDefinition: str
    trainingTaskInputs: typing.Any
    trainingTaskMetadata: typing.Any
    updateTime: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1Trial(typing_extensions.TypedDict, total=False):
    clientId: str
    customJob: str
    endTime: str
    finalMeasurement: GoogleCloudAiplatformV1beta1Measurement
    id: str
    infeasibleReason: str
    measurements: _list[GoogleCloudAiplatformV1beta1Measurement]
    name: str
    parameters: _list[GoogleCloudAiplatformV1beta1TrialParameter]
    startTime: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "REQUESTED",
        "ACTIVE",
        "STOPPING",
        "SUCCEEDED",
        "INFEASIBLE",
    ]
    webAccessUris: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1TrialContext(
    typing_extensions.TypedDict, total=False
):
    description: str
    parameters: _list[GoogleCloudAiplatformV1beta1TrialParameter]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1TrialParameter(
    typing_extensions.TypedDict, total=False
):
    parameterId: str
    value: typing.Any

@typing.type_check_only
class GoogleCloudAiplatformV1beta1UndeployIndexOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1UndeployIndexRequest(
    typing_extensions.TypedDict, total=False
):
    deployedIndexId: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1UndeployIndexResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1UndeployModelOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1UndeployModelRequest(
    typing_extensions.TypedDict, total=False
):
    deployedModelId: str
    trafficSplit: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1UndeployModelResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1UndeploySolverOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1UnmanagedContainerModel(
    typing_extensions.TypedDict, total=False
):
    artifactUri: str
    containerSpec: GoogleCloudAiplatformV1beta1ModelContainerSpec
    predictSchemata: GoogleCloudAiplatformV1beta1PredictSchemata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1UpdateDeploymentResourcePoolOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1UpdateExplanationDatasetOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1UpdateExplanationDatasetRequest(
    typing_extensions.TypedDict, total=False
):
    examples: GoogleCloudAiplatformV1beta1Examples

@typing.type_check_only
class GoogleCloudAiplatformV1beta1UpdateExplanationDatasetResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1UpdateFeaturestoreOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1UpdateIndexOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata
    nearestNeighborSearchOperationMetadata: GoogleCloudAiplatformV1beta1NearestNeighborSearchOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1UpdateModelDeploymentMonitoringJobOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1UpdatePersistentResourceOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1UpdateSpecialistPoolOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata
    specialistPool: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1UpdateTensorboardOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1UploadModelOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    genericMetadata: GoogleCloudAiplatformV1beta1GenericOperationMetadata

@typing.type_check_only
class GoogleCloudAiplatformV1beta1UploadModelRequest(
    typing_extensions.TypedDict, total=False
):
    model: GoogleCloudAiplatformV1beta1Model
    modelId: str
    parentModel: str
    serviceAccount: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1UploadModelResponse(
    typing_extensions.TypedDict, total=False
):
    model: str
    modelVersionId: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1UpsertDatapointsRequest(
    typing_extensions.TypedDict, total=False
):
    datapoints: _list[GoogleCloudAiplatformV1beta1IndexDatapoint]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1UpsertDatapointsResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1UserActionReference(
    typing_extensions.TypedDict, total=False
):
    dataLabelingJob: str
    method: str
    operation: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1Value(typing_extensions.TypedDict, total=False):
    doubleValue: float
    intValue: str
    stringValue: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1WorkerPoolSpec(
    typing_extensions.TypedDict, total=False
):
    containerSpec: GoogleCloudAiplatformV1beta1ContainerSpec
    diskSpec: GoogleCloudAiplatformV1beta1DiskSpec
    machineSpec: GoogleCloudAiplatformV1beta1MachineSpec
    nfsMounts: _list[GoogleCloudAiplatformV1beta1NfsMount]
    pythonPackageSpec: GoogleCloudAiplatformV1beta1PythonPackageSpec
    replicaCount: str

@typing.type_check_only
class GoogleCloudAiplatformV1beta1WriteFeatureValuesPayload(
    typing_extensions.TypedDict, total=False
):
    entityId: str
    featureValues: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1WriteFeatureValuesRequest(
    typing_extensions.TypedDict, total=False
):
    payloads: _list[GoogleCloudAiplatformV1beta1WriteFeatureValuesPayload]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1WriteFeatureValuesResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1WriteTensorboardExperimentDataRequest(
    typing_extensions.TypedDict, total=False
):
    writeRunDataRequests: _list[
        GoogleCloudAiplatformV1beta1WriteTensorboardRunDataRequest
    ]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1WriteTensorboardExperimentDataResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1WriteTensorboardRunDataRequest(
    typing_extensions.TypedDict, total=False
):
    tensorboardRun: str
    timeSeriesData: _list[GoogleCloudAiplatformV1beta1TimeSeriesData]

@typing.type_check_only
class GoogleCloudAiplatformV1beta1WriteTensorboardRunDataResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1XraiAttribution(
    typing_extensions.TypedDict, total=False
):
    blurBaselineConfig: GoogleCloudAiplatformV1beta1BlurBaselineConfig
    smoothGradConfig: GoogleCloudAiplatformV1beta1SmoothGradConfig
    stepCount: int

@typing.type_check_only
class GoogleCloudLocationListLocationsResponse(
    typing_extensions.TypedDict, total=False
):
    locations: _list[GoogleCloudLocationLocation]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudLocationLocation(typing_extensions.TypedDict, total=False):
    displayName: str
    labels: dict[str, typing.Any]
    locationId: str
    metadata: dict[str, typing.Any]
    name: str

@typing.type_check_only
class GoogleIamV1Binding(typing_extensions.TypedDict, total=False):
    condition: GoogleTypeExpr
    members: _list[str]
    role: str

@typing.type_check_only
class GoogleIamV1GetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    options: GoogleIamV1GetPolicyOptions

@typing.type_check_only
class GoogleIamV1GetPolicyOptions(typing_extensions.TypedDict, total=False):
    requestedPolicyVersion: int

@typing.type_check_only
class GoogleIamV1Policy(typing_extensions.TypedDict, total=False):
    bindings: _list[GoogleIamV1Binding]
    etag: str
    version: int

@typing.type_check_only
class GoogleIamV1SetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    policy: GoogleIamV1Policy

@typing.type_check_only
class GoogleIamV1TestIamPermissionsRequest(typing_extensions.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class GoogleIamV1TestIamPermissionsResponse(typing_extensions.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class GoogleLongrunningListOperationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    operations: _list[GoogleLongrunningOperation]

@typing.type_check_only
class GoogleLongrunningOperation(typing_extensions.TypedDict, total=False):
    done: bool
    error: GoogleRpcStatus
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class GoogleProtobufEmpty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class GoogleRpcStatus(typing_extensions.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class GoogleTypeColor(typing_extensions.TypedDict, total=False):
    alpha: float
    blue: float
    green: float
    red: float

@typing.type_check_only
class GoogleTypeExpr(typing_extensions.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str

@typing.type_check_only
class GoogleTypeInterval(typing_extensions.TypedDict, total=False):
    endTime: str
    startTime: str

@typing.type_check_only
class GoogleTypeMoney(typing_extensions.TypedDict, total=False):
    currencyCode: str
    nanos: int
    units: str
