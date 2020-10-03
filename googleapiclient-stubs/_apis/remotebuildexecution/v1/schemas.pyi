import typing

import typing_extensions

class BuildBazelRemoteExecutionV2OutputDirectory(
    typing_extensions.TypedDict, total=False
):
    path: str
    treeDigest: BuildBazelRemoteExecutionV2Digest

class BuildBazelRemoteExecutionV2Platform(typing_extensions.TypedDict, total=False):
    properties: typing.List[BuildBazelRemoteExecutionV2PlatformProperty]

class GoogleDevtoolsRemotebuildexecutionAdminV1alphaDeleteWorkerPoolRequest(
    typing_extensions.TypedDict, total=False
):
    name: str

class GoogleDevtoolsRemotebuildexecutionAdminV1alphaWorkerConfig(
    typing_extensions.TypedDict, total=False
):
    vmImage: str
    diskType: str
    soleTenancy: GoogleDevtoolsRemotebuildexecutionAdminV1alphaSoleTenancyConfig
    machineType: str
    networkAccess: str
    diskSizeGb: str
    accelerator: GoogleDevtoolsRemotebuildexecutionAdminV1alphaAcceleratorConfig
    minCpuPlatform: str
    reserved: bool
    maxConcurrentActions: str
    labels: typing.Dict[str, typing.Any]

class BuildBazelRemoteExecutionV2OutputSymlink(
    typing_extensions.TypedDict, total=False
):
    path: str
    target: str
    nodeProperties: typing.List[BuildBazelRemoteExecutionV2NodeProperty]

class BuildBazelRemoteExecutionV2NodeProperty(typing_extensions.TypedDict, total=False):
    name: str
    value: str

class BuildBazelRemoteExecutionV2CommandEnvironmentVariable(
    typing_extensions.TypedDict, total=False
):
    name: str
    value: str

class GoogleDevtoolsRemoteworkersV1test2CommandTaskTimeouts(
    typing_extensions.TypedDict, total=False
):
    idle: str
    execution: str
    shutdown: str

class GoogleDevtoolsRemotebuildexecutionAdminV1alphaInstance(
    typing_extensions.TypedDict, total=False
):
    featurePolicy: GoogleDevtoolsRemotebuildexecutionAdminV1alphaFeaturePolicy
    name: str
    loggingEnabled: bool
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "CREATING", "RUNNING", "INACTIVE"
    ]
    location: str

class GoogleDevtoolsRemotebuildexecutionAdminV1alphaCreateInstanceRequest(
    typing_extensions.TypedDict, total=False
):
    instanceId: str
    instance: GoogleDevtoolsRemotebuildexecutionAdminV1alphaInstance
    parent: str

class GoogleDevtoolsRemoteworkersV1test2CommandTaskInputs(
    typing_extensions.TypedDict, total=False
):
    inlineBlobs: typing.List[GoogleDevtoolsRemoteworkersV1test2Blob]
    arguments: typing.List[str]
    files: typing.List[GoogleDevtoolsRemoteworkersV1test2Digest]
    environmentVariables: typing.List[
        GoogleDevtoolsRemoteworkersV1test2CommandTaskInputsEnvironmentVariable
    ]
    workingDirectory: str

class GoogleDevtoolsRemotebuildexecutionAdminV1alphaListInstancesResponse(
    typing_extensions.TypedDict, total=False
):
    instances: typing.List[GoogleDevtoolsRemotebuildexecutionAdminV1alphaInstance]

class GoogleDevtoolsRemotebuildexecutionAdminV1alphaAcceleratorConfig(
    typing_extensions.TypedDict, total=False
):
    acceleratorType: str
    acceleratorCount: str

class GoogleDevtoolsRemotebuildexecutionAdminV1alphaGetWorkerPoolRequest(
    typing_extensions.TypedDict, total=False
):
    name: str

class BuildBazelRemoteExecutionV2LogFile(typing_extensions.TypedDict, total=False):
    humanReadable: bool
    digest: BuildBazelRemoteExecutionV2Digest

class BuildBazelRemoteExecutionV2SymlinkNode(typing_extensions.TypedDict, total=False):
    nodeProperties: typing.List[BuildBazelRemoteExecutionV2NodeProperty]
    target: str
    name: str

class GoogleDevtoolsRemoteworkersV1test2Digest(
    typing_extensions.TypedDict, total=False
):
    hash: str
    sizeBytes: str

class GoogleDevtoolsRemotebuildbotResourceUsage(
    typing_extensions.TypedDict, total=False
):
    memoryUsage: GoogleDevtoolsRemotebuildbotResourceUsageStat
    diskUsage: GoogleDevtoolsRemotebuildbotResourceUsageStat
    cpuUsedPercent: float

class GoogleDevtoolsRemotebuildexecutionAdminV1alphaGetInstanceRequest(
    typing_extensions.TypedDict, total=False
):
    name: str

class GoogleDevtoolsRemotebuildexecutionAdminV1alphaUpdateWorkerPoolRequest(
    typing_extensions.TypedDict, total=False
):
    updateMask: str
    workerPool: GoogleDevtoolsRemotebuildexecutionAdminV1alphaWorkerPool

class GoogleDevtoolsRemoteworkersV1test2CommandTaskOutputs(
    typing_extensions.TypedDict, total=False
):
    stdoutDestination: str
    stderrDestination: str
    files: typing.List[str]
    directories: typing.List[str]

class GoogleLongrunningCancelOperationRequest(
    typing_extensions.TypedDict, total=False
): ...

class BuildBazelRemoteExecutionV2OutputFile(typing_extensions.TypedDict, total=False):
    isExecutable: bool
    digest: BuildBazelRemoteExecutionV2Digest
    path: str
    contents: str
    nodeProperties: typing.List[BuildBazelRemoteExecutionV2NodeProperty]

class GoogleDevtoolsRemoteworkersV1test2CommandOverhead(
    typing_extensions.TypedDict, total=False
):
    overhead: str
    duration: str

class BuildBazelRemoteExecutionV2Command(typing_extensions.TypedDict, total=False):
    outputFiles: typing.List[str]
    outputDirectories: typing.List[str]
    environmentVariables: typing.List[
        BuildBazelRemoteExecutionV2CommandEnvironmentVariable
    ]
    platform: BuildBazelRemoteExecutionV2Platform
    workingDirectory: str
    arguments: typing.List[str]
    outputPaths: typing.List[str]

class GoogleDevtoolsRemotebuildexecutionAdminV1alphaSoleTenancyConfig(
    typing_extensions.TypedDict, total=False
):
    nodeType: str
    nodesZone: str

class GoogleDevtoolsRemoteworkersV1test2Blob(typing_extensions.TypedDict, total=False):
    digest: GoogleDevtoolsRemoteworkersV1test2Digest
    contents: str

class BuildBazelRemoteExecutionV2DirectoryNode(
    typing_extensions.TypedDict, total=False
):
    name: str
    digest: BuildBazelRemoteExecutionV2Digest

class GoogleBytestreamMedia(typing_extensions.TypedDict, total=False):
    resourceName: str

class GoogleDevtoolsRemotebuildbotCommandStatus(
    typing_extensions.TypedDict, total=False
):
    message: str
    code: typing_extensions.Literal[
        "OK",
        "INVALID_ARGUMENT",
        "DEADLINE_EXCEEDED",
        "NOT_FOUND",
        "PERMISSION_DENIED",
        "INTERNAL",
        "ABORTED",
        "FAILED_PRECONDITION",
        "CLEANUP_ERROR",
        "DOWNLOAD_INPUTS_ERROR",
        "UNKNOWN",
        "UPLOAD_OUTPUTS_ERROR",
        "UPLOAD_OUTPUTS_BYTES_LIMIT_EXCEEDED",
        "DOCKER_LOGIN_ERROR",
        "DOCKER_IMAGE_PULL_ERROR",
        "DOCKER_IMAGE_EXIST_ERROR",
        "DUPLICATE_INPUTS",
        "DOCKER_IMAGE_PERMISSION_DENIED",
        "DOCKER_IMAGE_NOT_FOUND",
        "WORKING_DIR_NOT_FOUND",
        "WORKING_DIR_NOT_IN_BASE_DIR",
        "DOCKER_UNAVAILABLE",
        "NO_CUDA_CAPABLE_DEVICE",
        "REMOTE_CAS_DOWNLOAD_ERROR",
        "REMOTE_CAS_UPLOAD_ERROR",
        "LOCAL_CASPROXY_NOT_RUNNING",
        "DOCKER_CREATE_CONTAINER_ERROR",
        "DOCKER_INVALID_ULIMIT",
        "DOCKER_UNKNOWN_RUNTIME",
        "DOCKER_UNKNOWN_CAPABILITY",
        "DOCKER_UNKNOWN_ERROR",
        "DOCKER_CREATE_COMPUTE_SYSTEM_ERROR",
        "DOCKER_PREPARELAYER_ERROR",
        "DOCKER_INCOMPATIBLE_OS_ERROR",
        "DOCKER_CREATE_RUNTIME_FILE_NOT_FOUND",
        "DOCKER_CREATE_RUNTIME_PERMISSION_DENIED",
        "DOCKER_CREATE_PROCESS_FILE_NOT_FOUND",
        "DOCKER_CREATE_COMPUTE_SYSTEM_INCORRECT_PARAMETER_ERROR",
    ]

class GoogleDevtoolsRemoteworkersV1test2AdminTemp(
    typing_extensions.TypedDict, total=False
):
    command: typing_extensions.Literal[
        "UNSPECIFIED", "BOT_UPDATE", "BOT_RESTART", "BOT_TERMINATE", "HOST_RESTART"
    ]
    arg: str

class BuildBazelRemoteExecutionV2ExecuteOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    stdoutStreamName: str
    stage: typing_extensions.Literal[
        "UNKNOWN", "CACHE_CHECK", "QUEUED", "EXECUTING", "COMPLETED"
    ]
    actionDigest: BuildBazelRemoteExecutionV2Digest
    stderrStreamName: str

class BuildBazelRemoteExecutionV2ActionResult(typing_extensions.TypedDict, total=False):
    stderrRaw: str
    outputDirectories: typing.List[BuildBazelRemoteExecutionV2OutputDirectory]
    stderrDigest: BuildBazelRemoteExecutionV2Digest
    exitCode: int
    outputFileSymlinks: typing.List[BuildBazelRemoteExecutionV2OutputSymlink]
    outputDirectorySymlinks: typing.List[BuildBazelRemoteExecutionV2OutputSymlink]
    stdoutDigest: BuildBazelRemoteExecutionV2Digest
    executionMetadata: BuildBazelRemoteExecutionV2ExecutedActionMetadata
    stdoutRaw: str
    outputSymlinks: typing.List[BuildBazelRemoteExecutionV2OutputSymlink]
    outputFiles: typing.List[BuildBazelRemoteExecutionV2OutputFile]

class GoogleDevtoolsRemotebuildexecutionAdminV1alphaAutoscale(
    typing_extensions.TypedDict, total=False
):
    minSize: str
    maxSize: str

class GoogleLongrunningOperation(typing_extensions.TypedDict, total=False):
    error: GoogleRpcStatus
    name: str
    response: typing.Dict[str, typing.Any]
    done: bool
    metadata: typing.Dict[str, typing.Any]

class GoogleLongrunningListOperationsResponse(typing_extensions.TypedDict, total=False):
    operations: typing.List[GoogleLongrunningOperation]
    nextPageToken: str

class GoogleDevtoolsRemotebuildexecutionAdminV1alphaDeleteInstanceRequest(
    typing_extensions.TypedDict, total=False
):
    name: str

class GoogleDevtoolsRemoteworkersV1test2CommandOutputs(
    typing_extensions.TypedDict, total=False
):
    outputs: GoogleDevtoolsRemoteworkersV1test2Digest
    exitCode: int

class GoogleRpcStatus(typing_extensions.TypedDict, total=False):
    message: str
    code: int
    details: typing.List[typing.Dict[str, typing.Any]]

class BuildBazelRemoteExecutionV2ExecutedActionMetadata(
    typing_extensions.TypedDict, total=False
):
    queuedTimestamp: str
    worker: str
    executionStartTimestamp: str
    executionCompletedTimestamp: str
    workerStartTimestamp: str
    outputUploadStartTimestamp: str
    inputFetchCompletedTimestamp: str
    inputFetchStartTimestamp: str
    workerCompletedTimestamp: str
    outputUploadCompletedTimestamp: str

class GoogleDevtoolsRemoteworkersV1test2DirectoryMetadata(
    typing_extensions.TypedDict, total=False
):
    path: str
    digest: GoogleDevtoolsRemoteworkersV1test2Digest

class GoogleDevtoolsRemotebuildexecutionAdminV1alphaFeaturePolicy(
    typing_extensions.TypedDict, total=False
):
    dockerNetwork: GoogleDevtoolsRemotebuildexecutionAdminV1alphaFeaturePolicyFeature
    dockerPrivileged: GoogleDevtoolsRemotebuildexecutionAdminV1alphaFeaturePolicyFeature
    containerImageSources: GoogleDevtoolsRemotebuildexecutionAdminV1alphaFeaturePolicyFeature
    dockerRunAsRoot: GoogleDevtoolsRemotebuildexecutionAdminV1alphaFeaturePolicyFeature
    dockerSiblingContainers: GoogleDevtoolsRemotebuildexecutionAdminV1alphaFeaturePolicyFeature
    linuxIsolation: typing_extensions.Literal[
        "LINUX_ISOLATION_UNSPECIFIED", "GVISOR", "OFF"
    ]
    dockerAddCapabilities: GoogleDevtoolsRemotebuildexecutionAdminV1alphaFeaturePolicyFeature
    dockerChrootPath: GoogleDevtoolsRemotebuildexecutionAdminV1alphaFeaturePolicyFeature
    dockerRuntime: GoogleDevtoolsRemotebuildexecutionAdminV1alphaFeaturePolicyFeature

class GoogleProtobufEmpty(typing_extensions.TypedDict, total=False): ...

class BuildBazelRemoteExecutionV2RequestMetadata(
    typing_extensions.TypedDict, total=False
):
    correlatedInvocationsId: str
    toolDetails: BuildBazelRemoteExecutionV2ToolDetails
    toolInvocationId: str
    actionId: str

class GoogleDevtoolsRemoteworkersV1test2FileMetadata(
    typing_extensions.TypedDict, total=False
):
    contents: str
    isExecutable: bool
    digest: GoogleDevtoolsRemoteworkersV1test2Digest
    path: str

class GoogleDevtoolsRemotebuildexecutionAdminV1alphaCreateWorkerPoolRequest(
    typing_extensions.TypedDict, total=False
):
    poolId: str
    parent: str
    workerPool: GoogleDevtoolsRemotebuildexecutionAdminV1alphaWorkerPool

class GoogleDevtoolsRemoteworkersV1test2CommandResult(
    typing_extensions.TypedDict, total=False
):
    metadata: typing.List[typing.Dict[str, typing.Any]]
    exitCode: int
    outputs: GoogleDevtoolsRemoteworkersV1test2Digest
    duration: str
    overhead: str
    status: GoogleRpcStatus

class GoogleDevtoolsRemoteworkersV1test2CommandTask(
    typing_extensions.TypedDict, total=False
):
    expectedOutputs: GoogleDevtoolsRemoteworkersV1test2CommandTaskOutputs
    inputs: GoogleDevtoolsRemoteworkersV1test2CommandTaskInputs
    timeouts: GoogleDevtoolsRemoteworkersV1test2CommandTaskTimeouts

class GoogleDevtoolsRemotebuildexecutionAdminV1alphaListWorkerPoolsResponse(
    typing_extensions.TypedDict, total=False
):
    workerPools: typing.List[GoogleDevtoolsRemotebuildexecutionAdminV1alphaWorkerPool]

class GoogleDevtoolsRemotebuildexecutionAdminV1alphaWorkerPool(
    typing_extensions.TypedDict, total=False
):
    workerCount: str
    autoscale: GoogleDevtoolsRemotebuildexecutionAdminV1alphaAutoscale
    channel: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "CREATING", "RUNNING", "UPDATING", "DELETING", "INACTIVE"
    ]
    name: str
    workerConfig: GoogleDevtoolsRemotebuildexecutionAdminV1alphaWorkerConfig

class GoogleDevtoolsRemotebuildbotResourceUsageStat(
    typing_extensions.TypedDict, total=False
):
    used: str
    total: str

class BuildBazelRemoteExecutionV2FileNode(typing_extensions.TypedDict, total=False):
    nodeProperties: typing.List[BuildBazelRemoteExecutionV2NodeProperty]
    name: str
    digest: BuildBazelRemoteExecutionV2Digest
    isExecutable: bool

class GoogleDevtoolsRemotebuildbotCommandDurations(
    typing_extensions.TypedDict, total=False
):
    overall: str
    upload: str
    dockerPrep: str
    downloadStartTime: str
    stdout: str
    execution: str
    uploadStartTime: str
    dockerPrepStartTime: str
    execStartTime: str
    download: str
    isoPrepDone: str

class GoogleDevtoolsRemotebuildexecutionAdminV1alphaFeaturePolicyFeature(
    typing_extensions.TypedDict, total=False
):
    policy: typing_extensions.Literal[
        "POLICY_UNSPECIFIED", "ALLOWED", "FORBIDDEN", "RESTRICTED"
    ]
    allowedValues: typing.List[str]

class BuildBazelRemoteExecutionV2Tree(typing_extensions.TypedDict, total=False):
    root: BuildBazelRemoteExecutionV2Directory
    children: typing.List[BuildBazelRemoteExecutionV2Directory]

class BuildBazelRemoteExecutionV2Action(typing_extensions.TypedDict, total=False):
    timeout: str
    inputRootDigest: BuildBazelRemoteExecutionV2Digest
    outputNodeProperties: typing.List[str]
    doNotCache: bool
    commandDigest: BuildBazelRemoteExecutionV2Digest

class BuildBazelRemoteExecutionV2ExecuteResponse(
    typing_extensions.TypedDict, total=False
):
    message: str
    result: BuildBazelRemoteExecutionV2ActionResult
    status: GoogleRpcStatus
    cachedResult: bool
    serverLogs: typing.Dict[str, typing.Any]

class GoogleDevtoolsRemotebuildexecutionAdminV1alphaListInstancesRequest(
    typing_extensions.TypedDict, total=False
):
    parent: str

class BuildBazelRemoteExecutionV2Directory(typing_extensions.TypedDict, total=False):
    directories: typing.List[BuildBazelRemoteExecutionV2DirectoryNode]
    nodeProperties: typing.List[BuildBazelRemoteExecutionV2NodeProperty]
    symlinks: typing.List[BuildBazelRemoteExecutionV2SymlinkNode]
    files: typing.List[BuildBazelRemoteExecutionV2FileNode]

class BuildBazelRemoteExecutionV2PlatformProperty(
    typing_extensions.TypedDict, total=False
):
    name: str
    value: str

class GoogleDevtoolsRemoteworkersV1test2CommandTaskInputsEnvironmentVariable(
    typing_extensions.TypedDict, total=False
):
    name: str
    value: str

class BuildBazelRemoteExecutionV2Digest(typing_extensions.TypedDict, total=False):
    sizeBytes: str
    hash: str

class GoogleDevtoolsRemotebuildbotCommandEvents(
    typing_extensions.TypedDict, total=False
):
    inputCacheMiss: float
    numWarnings: str
    dockerCacheHit: bool
    numErrors: str

class GoogleDevtoolsRemotebuildexecutionAdminV1alphaUpdateInstanceRequest(
    typing_extensions.TypedDict, total=False
):
    updateMask: str
    instance: GoogleDevtoolsRemotebuildexecutionAdminV1alphaInstance
    loggingEnabled: bool
    name: str

class BuildBazelRemoteExecutionV2ToolDetails(typing_extensions.TypedDict, total=False):
    toolName: str
    toolVersion: str

class GoogleDevtoolsRemoteworkersV1test2Directory(
    typing_extensions.TypedDict, total=False
):
    files: typing.List[GoogleDevtoolsRemoteworkersV1test2FileMetadata]
    directories: typing.List[GoogleDevtoolsRemoteworkersV1test2DirectoryMetadata]

class GoogleDevtoolsRemotebuildexecutionAdminV1alphaListWorkerPoolsRequest(
    typing_extensions.TypedDict, total=False
):
    parent: str
    filter: str
