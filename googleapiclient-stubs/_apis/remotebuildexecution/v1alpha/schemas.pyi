import typing

import typing_extensions

class GoogleDevtoolsRemotebuildexecutionAdminV1alphaListWorkerPoolsResponse(
    typing_extensions.TypedDict, total=False
):
    workerPools: typing.List[GoogleDevtoolsRemotebuildexecutionAdminV1alphaWorkerPool]

class BuildBazelRemoteExecutionV2Platform(typing_extensions.TypedDict, total=False):
    properties: typing.List[BuildBazelRemoteExecutionV2PlatformProperty]

class GoogleDevtoolsRemotebuildexecutionAdminV1alphaDeleteInstanceRequest(
    typing_extensions.TypedDict, total=False
):
    name: str

class BuildBazelRemoteExecutionV2ExecutedActionMetadata(
    typing_extensions.TypedDict, total=False
):
    inputFetchStartTimestamp: str
    queuedTimestamp: str
    workerCompletedTimestamp: str
    executionCompletedTimestamp: str
    outputUploadStartTimestamp: str
    executionStartTimestamp: str
    worker: str
    workerStartTimestamp: str
    outputUploadCompletedTimestamp: str
    inputFetchCompletedTimestamp: str

class GoogleDevtoolsRemotebuildexecutionAdminV1alphaSoleTenancyConfig(
    typing_extensions.TypedDict, total=False
):
    nodeType: str
    nodesZone: str

class GoogleDevtoolsRemotebuildexecutionAdminV1alphaUpdateInstanceRequest(
    typing_extensions.TypedDict, total=False
):
    updateMask: str
    name: str
    loggingEnabled: bool
    instance: GoogleDevtoolsRemotebuildexecutionAdminV1alphaInstance

class GoogleDevtoolsRemotebuildexecutionAdminV1alphaGetInstanceRequest(
    typing_extensions.TypedDict, total=False
):
    name: str

class GoogleDevtoolsRemotebuildexecutionAdminV1alphaFeaturePolicyFeature(
    typing_extensions.TypedDict, total=False
):
    policy: typing_extensions.Literal[
        "POLICY_UNSPECIFIED", "ALLOWED", "FORBIDDEN", "RESTRICTED"
    ]
    allowedValues: typing.List[str]

class GoogleDevtoolsRemoteworkersV1test2CommandTask(
    typing_extensions.TypedDict, total=False
):
    expectedOutputs: GoogleDevtoolsRemoteworkersV1test2CommandTaskOutputs
    inputs: GoogleDevtoolsRemoteworkersV1test2CommandTaskInputs
    timeouts: GoogleDevtoolsRemoteworkersV1test2CommandTaskTimeouts

class GoogleDevtoolsRemotebuildexecutionAdminV1alphaGetWorkerPoolRequest(
    typing_extensions.TypedDict, total=False
):
    name: str

class GoogleDevtoolsRemoteworkersV1test2FileMetadata(
    typing_extensions.TypedDict, total=False
):
    isExecutable: bool
    digest: GoogleDevtoolsRemoteworkersV1test2Digest
    contents: str
    path: str

class BuildBazelRemoteExecutionV2PlatformProperty(
    typing_extensions.TypedDict, total=False
):
    name: str
    value: str

class GoogleDevtoolsRemoteworkersV1test2DirectoryMetadata(
    typing_extensions.TypedDict, total=False
):
    path: str
    digest: GoogleDevtoolsRemoteworkersV1test2Digest

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

class GoogleDevtoolsRemoteworkersV1test2Directory(
    typing_extensions.TypedDict, total=False
):
    directories: typing.List[GoogleDevtoolsRemoteworkersV1test2DirectoryMetadata]
    files: typing.List[GoogleDevtoolsRemoteworkersV1test2FileMetadata]

class GoogleRpcStatus(typing_extensions.TypedDict, total=False):
    details: typing.List[typing.Dict[str, typing.Any]]
    code: int
    message: str

class GoogleDevtoolsRemotebuildexecutionAdminV1alphaCreateInstanceRequest(
    typing_extensions.TypedDict, total=False
):
    parent: str
    instance: GoogleDevtoolsRemotebuildexecutionAdminV1alphaInstance
    instanceId: str

class GoogleDevtoolsRemoteworkersV1test2CommandTaskTimeouts(
    typing_extensions.TypedDict, total=False
):
    shutdown: str
    idle: str
    execution: str

class GoogleDevtoolsRemotebuildexecutionAdminV1alphaListInstancesResponse(
    typing_extensions.TypedDict, total=False
):
    instances: typing.List[GoogleDevtoolsRemotebuildexecutionAdminV1alphaInstance]

class GoogleDevtoolsRemotebuildexecutionAdminV1alphaInstance(
    typing_extensions.TypedDict, total=False
):
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "CREATING", "RUNNING", "INACTIVE"
    ]
    featurePolicy: GoogleDevtoolsRemotebuildexecutionAdminV1alphaFeaturePolicy
    loggingEnabled: bool
    name: str
    location: str

class GoogleDevtoolsRemoteworkersV1test2CommandTaskOutputs(
    typing_extensions.TypedDict, total=False
):
    stderrDestination: str
    directories: typing.List[str]
    files: typing.List[str]
    stdoutDestination: str

class GoogleDevtoolsRemotebuildbotCommandEvents(
    typing_extensions.TypedDict, total=False
):
    numWarnings: str
    dockerCacheHit: bool
    numErrors: str
    inputCacheMiss: float

class GoogleDevtoolsRemotebuildbotCommandDurations(
    typing_extensions.TypedDict, total=False
):
    execution: str
    overall: str
    uploadStartTime: str
    stdout: str
    download: str
    execStartTime: str
    isoPrepDone: str
    downloadStartTime: str
    dockerPrepStartTime: str
    dockerPrep: str
    upload: str

class BuildBazelRemoteExecutionV2ExecuteResponse(
    typing_extensions.TypedDict, total=False
):
    message: str
    status: GoogleRpcStatus
    serverLogs: typing.Dict[str, typing.Any]
    result: BuildBazelRemoteExecutionV2ActionResult
    cachedResult: bool

class GoogleDevtoolsRemotebuildexecutionAdminV1alphaUpdateWorkerPoolRequest(
    typing_extensions.TypedDict, total=False
):
    updateMask: str
    workerPool: GoogleDevtoolsRemotebuildexecutionAdminV1alphaWorkerPool

class BuildBazelRemoteExecutionV2SymlinkNode(typing_extensions.TypedDict, total=False):
    name: str
    nodeProperties: typing.List[BuildBazelRemoteExecutionV2NodeProperty]
    target: str

class GoogleDevtoolsRemoteworkersV1test2Digest(
    typing_extensions.TypedDict, total=False
):
    sizeBytes: str
    hash: str

class BuildBazelRemoteExecutionV2RequestMetadata(
    typing_extensions.TypedDict, total=False
):
    toolInvocationId: str
    actionId: str
    correlatedInvocationsId: str
    toolDetails: BuildBazelRemoteExecutionV2ToolDetails

class GoogleLongrunningOperation(typing_extensions.TypedDict, total=False):
    error: GoogleRpcStatus
    metadata: typing.Dict[str, typing.Any]
    name: str
    response: typing.Dict[str, typing.Any]
    done: bool

class BuildBazelRemoteExecutionV2LogFile(typing_extensions.TypedDict, total=False):
    humanReadable: bool
    digest: BuildBazelRemoteExecutionV2Digest

class GoogleDevtoolsRemoteworkersV1test2AdminTemp(
    typing_extensions.TypedDict, total=False
):
    arg: str
    command: typing_extensions.Literal[
        "UNSPECIFIED", "BOT_UPDATE", "BOT_RESTART", "BOT_TERMINATE", "HOST_RESTART"
    ]

class BuildBazelRemoteExecutionV2Command(typing_extensions.TypedDict, total=False):
    workingDirectory: str
    outputFiles: typing.List[str]
    environmentVariables: typing.List[
        BuildBazelRemoteExecutionV2CommandEnvironmentVariable
    ]
    outputDirectories: typing.List[str]
    outputPaths: typing.List[str]
    platform: BuildBazelRemoteExecutionV2Platform
    arguments: typing.List[str]

class GoogleDevtoolsRemotebuildexecutionAdminV1alphaWorkerConfig(
    typing_extensions.TypedDict, total=False
):
    labels: typing.Dict[str, typing.Any]
    reserved: bool
    accelerator: GoogleDevtoolsRemotebuildexecutionAdminV1alphaAcceleratorConfig
    maxConcurrentActions: str
    networkAccess: str
    minCpuPlatform: str
    soleTenancy: GoogleDevtoolsRemotebuildexecutionAdminV1alphaSoleTenancyConfig
    machineType: str
    diskType: str
    vmImage: str
    diskSizeGb: str

class GoogleDevtoolsRemotebuildbotResourceUsage(
    typing_extensions.TypedDict, total=False
):
    diskUsage: GoogleDevtoolsRemotebuildbotResourceUsageStat
    cpuUsedPercent: float
    memoryUsage: GoogleDevtoolsRemotebuildbotResourceUsageStat

class BuildBazelRemoteExecutionV2CommandEnvironmentVariable(
    typing_extensions.TypedDict, total=False
):
    name: str
    value: str

class BuildBazelRemoteExecutionV2ExecuteOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    stderrStreamName: str
    stdoutStreamName: str
    actionDigest: BuildBazelRemoteExecutionV2Digest
    stage: typing_extensions.Literal[
        "UNKNOWN", "CACHE_CHECK", "QUEUED", "EXECUTING", "COMPLETED"
    ]

class BuildBazelRemoteExecutionV2ToolDetails(typing_extensions.TypedDict, total=False):
    toolName: str
    toolVersion: str

class GoogleDevtoolsRemoteworkersV1test2CommandOutputs(
    typing_extensions.TypedDict, total=False
):
    exitCode: int
    outputs: GoogleDevtoolsRemoteworkersV1test2Digest

class BuildBazelRemoteExecutionV2OutputFile(typing_extensions.TypedDict, total=False):
    nodeProperties: typing.List[BuildBazelRemoteExecutionV2NodeProperty]
    path: str
    isExecutable: bool
    digest: BuildBazelRemoteExecutionV2Digest
    contents: str

class GoogleDevtoolsRemoteworkersV1test2CommandTaskInputs(
    typing_extensions.TypedDict, total=False
):
    files: typing.List[GoogleDevtoolsRemoteworkersV1test2Digest]
    inlineBlobs: typing.List[GoogleDevtoolsRemoteworkersV1test2Blob]
    environmentVariables: typing.List[
        GoogleDevtoolsRemoteworkersV1test2CommandTaskInputsEnvironmentVariable
    ]
    arguments: typing.List[str]
    workingDirectory: str

class GoogleDevtoolsRemotebuildexecutionAdminV1alphaDeleteWorkerPoolRequest(
    typing_extensions.TypedDict, total=False
):
    name: str

class BuildBazelRemoteExecutionV2FileNode(typing_extensions.TypedDict, total=False):
    isExecutable: bool
    nodeProperties: typing.List[BuildBazelRemoteExecutionV2NodeProperty]
    digest: BuildBazelRemoteExecutionV2Digest
    name: str

class BuildBazelRemoteExecutionV2NodeProperty(typing_extensions.TypedDict, total=False):
    name: str
    value: str

class GoogleDevtoolsRemoteworkersV1test2CommandTaskInputsEnvironmentVariable(
    typing_extensions.TypedDict, total=False
):
    name: str
    value: str

class GoogleDevtoolsRemotebuildexecutionAdminV1alphaCreateWorkerPoolRequest(
    typing_extensions.TypedDict, total=False
):
    poolId: str
    workerPool: GoogleDevtoolsRemotebuildexecutionAdminV1alphaWorkerPool
    parent: str

class GoogleDevtoolsRemotebuildexecutionAdminV1alphaListInstancesRequest(
    typing_extensions.TypedDict, total=False
):
    parent: str

class BuildBazelRemoteExecutionV2Action(typing_extensions.TypedDict, total=False):
    outputNodeProperties: typing.List[str]
    commandDigest: BuildBazelRemoteExecutionV2Digest
    timeout: str
    doNotCache: bool
    inputRootDigest: BuildBazelRemoteExecutionV2Digest

class GoogleDevtoolsRemotebuildexecutionAdminV1alphaWorkerPool(
    typing_extensions.TypedDict, total=False
):
    channel: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "CREATING", "RUNNING", "UPDATING", "DELETING", "INACTIVE"
    ]
    workerConfig: GoogleDevtoolsRemotebuildexecutionAdminV1alphaWorkerConfig
    name: str
    autoscale: GoogleDevtoolsRemotebuildexecutionAdminV1alphaAutoscale
    workerCount: str

class BuildBazelRemoteExecutionV2Tree(typing_extensions.TypedDict, total=False):
    children: typing.List[BuildBazelRemoteExecutionV2Directory]
    root: BuildBazelRemoteExecutionV2Directory

class GoogleDevtoolsRemoteworkersV1test2CommandOverhead(
    typing_extensions.TypedDict, total=False
):
    duration: str
    overhead: str

class GoogleDevtoolsRemotebuildexecutionAdminV1alphaAcceleratorConfig(
    typing_extensions.TypedDict, total=False
):
    acceleratorType: str
    acceleratorCount: str

class GoogleDevtoolsRemoteworkersV1test2Blob(typing_extensions.TypedDict, total=False):
    contents: str
    digest: GoogleDevtoolsRemoteworkersV1test2Digest

class BuildBazelRemoteExecutionV2OutputDirectory(
    typing_extensions.TypedDict, total=False
):
    path: str
    treeDigest: BuildBazelRemoteExecutionV2Digest

class BuildBazelRemoteExecutionV2OutputSymlink(
    typing_extensions.TypedDict, total=False
):
    target: str
    path: str
    nodeProperties: typing.List[BuildBazelRemoteExecutionV2NodeProperty]

class GoogleDevtoolsRemotebuildexecutionAdminV1alphaFeaturePolicy(
    typing_extensions.TypedDict, total=False
):
    dockerPrivileged: GoogleDevtoolsRemotebuildexecutionAdminV1alphaFeaturePolicyFeature
    dockerNetwork: GoogleDevtoolsRemotebuildexecutionAdminV1alphaFeaturePolicyFeature
    dockerAddCapabilities: GoogleDevtoolsRemotebuildexecutionAdminV1alphaFeaturePolicyFeature
    linuxIsolation: typing_extensions.Literal[
        "LINUX_ISOLATION_UNSPECIFIED", "GVISOR", "OFF"
    ]
    dockerRunAsRoot: GoogleDevtoolsRemotebuildexecutionAdminV1alphaFeaturePolicyFeature
    dockerRuntime: GoogleDevtoolsRemotebuildexecutionAdminV1alphaFeaturePolicyFeature
    containerImageSources: GoogleDevtoolsRemotebuildexecutionAdminV1alphaFeaturePolicyFeature
    dockerSiblingContainers: GoogleDevtoolsRemotebuildexecutionAdminV1alphaFeaturePolicyFeature
    dockerChrootPath: GoogleDevtoolsRemotebuildexecutionAdminV1alphaFeaturePolicyFeature

class GoogleDevtoolsRemotebuildbotResourceUsageStat(
    typing_extensions.TypedDict, total=False
):
    total: str
    used: str

class BuildBazelRemoteExecutionV2ActionResult(typing_extensions.TypedDict, total=False):
    outputDirectorySymlinks: typing.List[BuildBazelRemoteExecutionV2OutputSymlink]
    outputDirectories: typing.List[BuildBazelRemoteExecutionV2OutputDirectory]
    stdoutRaw: str
    stdoutDigest: BuildBazelRemoteExecutionV2Digest
    outputSymlinks: typing.List[BuildBazelRemoteExecutionV2OutputSymlink]
    stderrRaw: str
    stderrDigest: BuildBazelRemoteExecutionV2Digest
    exitCode: int
    outputFileSymlinks: typing.List[BuildBazelRemoteExecutionV2OutputSymlink]
    outputFiles: typing.List[BuildBazelRemoteExecutionV2OutputFile]
    executionMetadata: BuildBazelRemoteExecutionV2ExecutedActionMetadata

class GoogleDevtoolsRemoteworkersV1test2CommandResult(
    typing_extensions.TypedDict, total=False
):
    outputs: GoogleDevtoolsRemoteworkersV1test2Digest
    duration: str
    overhead: str
    exitCode: int
    status: GoogleRpcStatus
    metadata: typing.List[typing.Dict[str, typing.Any]]

class BuildBazelRemoteExecutionV2DirectoryNode(
    typing_extensions.TypedDict, total=False
):
    name: str
    digest: BuildBazelRemoteExecutionV2Digest

class GoogleDevtoolsRemotebuildexecutionAdminV1alphaListWorkerPoolsRequest(
    typing_extensions.TypedDict, total=False
):
    filter: str
    parent: str

class BuildBazelRemoteExecutionV2Digest(typing_extensions.TypedDict, total=False):
    sizeBytes: str
    hash: str

class GoogleDevtoolsRemotebuildexecutionAdminV1alphaAutoscale(
    typing_extensions.TypedDict, total=False
):
    minSize: str
    maxSize: str

class BuildBazelRemoteExecutionV2Directory(typing_extensions.TypedDict, total=False):
    symlinks: typing.List[BuildBazelRemoteExecutionV2SymlinkNode]
    files: typing.List[BuildBazelRemoteExecutionV2FileNode]
    directories: typing.List[BuildBazelRemoteExecutionV2DirectoryNode]
    nodeProperties: typing.List[BuildBazelRemoteExecutionV2NodeProperty]
