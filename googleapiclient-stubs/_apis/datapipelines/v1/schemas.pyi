import typing

_list = list

@typing.type_check_only
class GoogleCloudDatapipelinesV1DataflowJobDetails(typing.TypedDict, total=False):
    currentWorkers: int
    resourceInfo: dict[str, typing.Any]
    sdkVersion: GoogleCloudDatapipelinesV1SdkVersion

@typing.type_check_only
class GoogleCloudDatapipelinesV1FlexTemplateRuntimeEnvironment(
    typing.TypedDict, total=False
):
    additionalExperiments: _list[str]
    additionalUserLabels: dict[str, typing.Any]
    enableStreamingEngine: bool
    flexrsGoal: typing.Literal[
        "FLEXRS_UNSPECIFIED", "FLEXRS_SPEED_OPTIMIZED", "FLEXRS_COST_OPTIMIZED"
    ]
    ipConfiguration: typing.Literal[
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
class GoogleCloudDatapipelinesV1Job(typing.TypedDict, total=False):
    createTime: str
    dataflowJobDetails: GoogleCloudDatapipelinesV1DataflowJobDetails
    endTime: str
    id: str
    name: str
    state: typing.Literal[
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
    typing.TypedDict, total=False
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
    typing.TypedDict, total=False
):
    launchParameter: GoogleCloudDatapipelinesV1LaunchFlexTemplateParameter
    location: str
    projectId: str
    validateOnly: bool

@typing.type_check_only
class GoogleCloudDatapipelinesV1LaunchTemplateParameters(typing.TypedDict, total=False):
    environment: GoogleCloudDatapipelinesV1RuntimeEnvironment
    jobName: str
    parameters: dict[str, typing.Any]
    transformNameMapping: dict[str, typing.Any]
    update: bool

@typing.type_check_only
class GoogleCloudDatapipelinesV1LaunchTemplateRequest(typing.TypedDict, total=False):
    gcsPath: str
    launchParameters: GoogleCloudDatapipelinesV1LaunchTemplateParameters
    location: str
    projectId: str
    validateOnly: bool

@typing.type_check_only
class GoogleCloudDatapipelinesV1ListJobsResponse(typing.TypedDict, total=False):
    jobs: _list[GoogleCloudDatapipelinesV1Job]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudDatapipelinesV1ListPipelinesResponse(typing.TypedDict, total=False):
    nextPageToken: str
    pipelines: _list[GoogleCloudDatapipelinesV1Pipeline]

@typing.type_check_only
class GoogleCloudDatapipelinesV1Pipeline(typing.TypedDict, total=False):
    createTime: str
    displayName: str
    jobCount: int
    lastUpdateTime: str
    name: str
    pipelineSources: dict[str, typing.Any]
    scheduleInfo: GoogleCloudDatapipelinesV1ScheduleSpec
    schedulerServiceAccountEmail: str
    state: typing.Literal[
        "STATE_UNSPECIFIED",
        "STATE_RESUMING",
        "STATE_ACTIVE",
        "STATE_STOPPING",
        "STATE_ARCHIVED",
        "STATE_PAUSED",
    ]
    type: typing.Literal[
        "PIPELINE_TYPE_UNSPECIFIED", "PIPELINE_TYPE_BATCH", "PIPELINE_TYPE_STREAMING"
    ]
    workload: GoogleCloudDatapipelinesV1Workload

@typing.type_check_only
class GoogleCloudDatapipelinesV1RunPipelineRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleCloudDatapipelinesV1RunPipelineResponse(typing.TypedDict, total=False):
    job: GoogleCloudDatapipelinesV1Job

@typing.type_check_only
class GoogleCloudDatapipelinesV1RuntimeEnvironment(typing.TypedDict, total=False):
    additionalExperiments: _list[str]
    additionalUserLabels: dict[str, typing.Any]
    bypassTempDirValidation: bool
    enableStreamingEngine: bool
    ipConfiguration: typing.Literal[
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
class GoogleCloudDatapipelinesV1ScheduleSpec(typing.TypedDict, total=False):
    nextJobTime: str
    schedule: str
    timeZone: str

@typing.type_check_only
class GoogleCloudDatapipelinesV1SdkVersion(typing.TypedDict, total=False):
    sdkSupportStatus: typing.Literal[
        "UNKNOWN", "SUPPORTED", "STALE", "DEPRECATED", "UNSUPPORTED"
    ]
    version: str
    versionDisplayName: str

@typing.type_check_only
class GoogleCloudDatapipelinesV1StopPipelineRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleCloudDatapipelinesV1Workload(typing.TypedDict, total=False):
    dataflowFlexTemplateRequest: GoogleCloudDatapipelinesV1LaunchFlexTemplateRequest
    dataflowLaunchTemplateRequest: GoogleCloudDatapipelinesV1LaunchTemplateRequest

@typing.type_check_only
class GoogleProtobufEmpty(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleRpcStatus(typing.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str
