import typing

import typing_extensions

_list = list

@typing.type_check_only
class GoogleCloudDatapipelinesV1DataflowJobDetails(
    typing_extensions.TypedDict, total=False
):
    currentWorkers: int
    resourceInfo: dict[str, typing.Any]
    sdkVersion: GoogleCloudDatapipelinesV1SdkVersion

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
