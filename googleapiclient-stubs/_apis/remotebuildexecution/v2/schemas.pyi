import typing

import typing_extensions

class BuildBazelRemoteExecutionV2WaitExecutionRequest(
    typing_extensions.TypedDict, total=False
): ...

class GoogleDevtoolsRemotebuildexecutionAdminV1alphaCreateWorkerPoolRequest(
    typing_extensions.TypedDict, total=False
):
    workerPool: GoogleDevtoolsRemotebuildexecutionAdminV1alphaWorkerPool
    parent: str
    poolId: str

class GoogleRpcStatus(typing_extensions.TypedDict, total=False):
    details: typing.List[typing.Dict[str, typing.Any]]
    message: str
    code: int

class BuildBazelRemoteExecutionV2ResultsCachePolicy(
    typing_extensions.TypedDict, total=False
):
    priority: int

class BuildBazelRemoteExecutionV2FindMissingBlobsRequest(
    typing_extensions.TypedDict, total=False
):
    blobDigests: typing.List[BuildBazelRemoteExecutionV2Digest]

class GoogleLongrunningOperation(typing_extensions.TypedDict, total=False):
    name: str
    error: GoogleRpcStatus
    done: bool
    metadata: typing.Dict[str, typing.Any]
    response: typing.Dict[str, typing.Any]

class GoogleDevtoolsRemotebuildexecutionAdminV1alphaGetInstanceRequest(
    typing_extensions.TypedDict, total=False
):
    name: str

class GoogleDevtoolsRemotebuildexecutionAdminV1alphaListWorkerPoolsRequest(
    typing_extensions.TypedDict, total=False
):
    parent: str
    filter: str

class BuildBazelRemoteExecutionV2PriorityCapabilities(
    typing_extensions.TypedDict, total=False
):
    priorities: typing.List[
        BuildBazelRemoteExecutionV2PriorityCapabilitiesPriorityRange
    ]

class GoogleDevtoolsRemotebuildexecutionAdminV1alphaUpdateInstanceRequest(
    typing_extensions.TypedDict, total=False
):
    updateMask: str
    loggingEnabled: bool
    instance: GoogleDevtoolsRemotebuildexecutionAdminV1alphaInstance
    name: str

class BuildBazelRemoteExecutionV2ExecuteRequest(
    typing_extensions.TypedDict, total=False
):
    executionPolicy: BuildBazelRemoteExecutionV2ExecutionPolicy
    skipCacheLookup: bool
    actionDigest: BuildBazelRemoteExecutionV2Digest
    resultsCachePolicy: BuildBazelRemoteExecutionV2ResultsCachePolicy

class BuildBazelRemoteExecutionV2BatchUpdateBlobsRequest(
    typing_extensions.TypedDict, total=False
):
    requests: typing.List[BuildBazelRemoteExecutionV2BatchUpdateBlobsRequestRequest]

class GoogleDevtoolsRemoteworkersV1test2CommandTaskInputsEnvironmentVariable(
    typing_extensions.TypedDict, total=False
):
    name: str
    value: str

class GoogleDevtoolsRemotebuildexecutionAdminV1alphaFeaturePolicyFeature(
    typing_extensions.TypedDict, total=False
):
    allowedValues: typing.List[str]
    policy: typing_extensions.Literal[
        "POLICY_UNSPECIFIED", "ALLOWED", "FORBIDDEN", "RESTRICTED"
    ]

class BuildBazelRemoteExecutionV2Platform(typing_extensions.TypedDict, total=False):
    properties: typing.List[BuildBazelRemoteExecutionV2PlatformProperty]

class GoogleDevtoolsRemoteworkersV1test2Blob(typing_extensions.TypedDict, total=False):
    contents: str
    digest: GoogleDevtoolsRemoteworkersV1test2Digest

class GoogleDevtoolsRemoteworkersV1test2CommandTaskTimeouts(
    typing_extensions.TypedDict, total=False
):
    idle: str
    execution: str
    shutdown: str

class BuildBazelRemoteExecutionV2ExecuteResponse(
    typing_extensions.TypedDict, total=False
):
    serverLogs: typing.Dict[str, typing.Any]
    status: GoogleRpcStatus
    cachedResult: bool
    message: str
    result: BuildBazelRemoteExecutionV2ActionResult

class GoogleDevtoolsRemotebuildbotCommandEvents(
    typing_extensions.TypedDict, total=False
):
    numErrors: str
    numWarnings: str
    dockerCacheHit: bool
    inputCacheMiss: float

class BuildBazelRemoteExecutionV2OutputFile(typing_extensions.TypedDict, total=False):
    contents: str
    nodeProperties: typing.List[BuildBazelRemoteExecutionV2NodeProperty]
    isExecutable: bool
    path: str
    digest: BuildBazelRemoteExecutionV2Digest

class GoogleDevtoolsRemoteworkersV1test2CommandTaskOutputs(
    typing_extensions.TypedDict, total=False
):
    stderrDestination: str
    directories: typing.List[str]
    files: typing.List[str]
    stdoutDestination: str

class GoogleDevtoolsRemotebuildexecutionAdminV1alphaListInstancesRequest(
    typing_extensions.TypedDict, total=False
):
    parent: str

class BuildBazelRemoteExecutionV2ExecutedActionMetadata(
    typing_extensions.TypedDict, total=False
):
    workerCompletedTimestamp: str
    queuedTimestamp: str
    workerStartTimestamp: str
    worker: str
    inputFetchStartTimestamp: str
    outputUploadStartTimestamp: str
    inputFetchCompletedTimestamp: str
    executionStartTimestamp: str
    executionCompletedTimestamp: str
    outputUploadCompletedTimestamp: str

class BuildBazelRemoteExecutionV2ActionResult(typing_extensions.TypedDict, total=False):
    exitCode: int
    outputFileSymlinks: typing.List[BuildBazelRemoteExecutionV2OutputSymlink]
    outputDirectorySymlinks: typing.List[BuildBazelRemoteExecutionV2OutputSymlink]
    stderrDigest: BuildBazelRemoteExecutionV2Digest
    stdoutDigest: BuildBazelRemoteExecutionV2Digest
    outputFiles: typing.List[BuildBazelRemoteExecutionV2OutputFile]
    stdoutRaw: str
    outputSymlinks: typing.List[BuildBazelRemoteExecutionV2OutputSymlink]
    outputDirectories: typing.List[BuildBazelRemoteExecutionV2OutputDirectory]
    stderrRaw: str
    executionMetadata: BuildBazelRemoteExecutionV2ExecutedActionMetadata

class GoogleDevtoolsRemoteworkersV1test2AdminTemp(
    typing_extensions.TypedDict, total=False
):
    arg: str
    command: typing_extensions.Literal[
        "UNSPECIFIED", "BOT_UPDATE", "BOT_RESTART", "BOT_TERMINATE", "HOST_RESTART"
    ]

class BuildBazelRemoteExecutionV2CommandEnvironmentVariable(
    typing_extensions.TypedDict, total=False
):
    name: str
    value: str

class BuildBazelRemoteExecutionV2BatchUpdateBlobsResponse(
    typing_extensions.TypedDict, total=False
):
    responses: typing.List[BuildBazelRemoteExecutionV2BatchUpdateBlobsResponseResponse]

class GoogleDevtoolsRemotebuildexecutionAdminV1alphaCreateInstanceRequest(
    typing_extensions.TypedDict, total=False
):
    parent: str
    instance: GoogleDevtoolsRemotebuildexecutionAdminV1alphaInstance
    instanceId: str

class BuildBazelRemoteExecutionV2ExecutionPolicy(
    typing_extensions.TypedDict, total=False
):
    priority: int

class BuildBazelRemoteExecutionV2Digest(typing_extensions.TypedDict, total=False):
    sizeBytes: str
    hash: str

class BuildBazelRemoteExecutionV2Command(typing_extensions.TypedDict, total=False):
    workingDirectory: str
    outputDirectories: typing.List[str]
    platform: BuildBazelRemoteExecutionV2Platform
    outputFiles: typing.List[str]
    outputPaths: typing.List[str]
    environmentVariables: typing.List[
        BuildBazelRemoteExecutionV2CommandEnvironmentVariable
    ]
    arguments: typing.List[str]

class BuildBazelRemoteExecutionV2BatchReadBlobsResponseResponse(
    typing_extensions.TypedDict, total=False
):
    status: GoogleRpcStatus
    digest: BuildBazelRemoteExecutionV2Digest
    data: str

class BuildBazelRemoteExecutionV2Directory(typing_extensions.TypedDict, total=False):
    directories: typing.List[BuildBazelRemoteExecutionV2DirectoryNode]
    files: typing.List[BuildBazelRemoteExecutionV2FileNode]
    nodeProperties: typing.List[BuildBazelRemoteExecutionV2NodeProperty]
    symlinks: typing.List[BuildBazelRemoteExecutionV2SymlinkNode]

class BuildBazelRemoteExecutionV2SymlinkNode(typing_extensions.TypedDict, total=False):
    target: str
    name: str
    nodeProperties: typing.List[BuildBazelRemoteExecutionV2NodeProperty]

class GoogleDevtoolsRemotebuildbotResourceUsageStat(
    typing_extensions.TypedDict, total=False
):
    used: str
    total: str

class BuildBazelRemoteExecutionV2ToolDetails(typing_extensions.TypedDict, total=False):
    toolVersion: str
    toolName: str

class BuildBazelRemoteExecutionV2ServerCapabilities(
    typing_extensions.TypedDict, total=False
):
    lowApiVersion: BuildBazelSemverSemVer
    cacheCapabilities: BuildBazelRemoteExecutionV2CacheCapabilities
    highApiVersion: BuildBazelSemverSemVer
    executionCapabilities: BuildBazelRemoteExecutionV2ExecutionCapabilities
    deprecatedApiVersion: BuildBazelSemverSemVer

class GoogleDevtoolsRemotebuildexecutionAdminV1alphaGetWorkerPoolRequest(
    typing_extensions.TypedDict, total=False
):
    name: str

class BuildBazelRemoteExecutionV2OutputDirectory(
    typing_extensions.TypedDict, total=False
):
    path: str
    treeDigest: BuildBazelRemoteExecutionV2Digest

class GoogleDevtoolsRemotebuildbotCommandDurations(
    typing_extensions.TypedDict, total=False
):
    stdout: str
    downloadStartTime: str
    download: str
    upload: str
    isoPrepDone: str
    execStartTime: str
    dockerPrepStartTime: str
    execution: str
    dockerPrep: str
    uploadStartTime: str
    overall: str

class BuildBazelRemoteExecutionV2BatchUpdateBlobsRequestRequest(
    typing_extensions.TypedDict, total=False
):
    digest: BuildBazelRemoteExecutionV2Digest
    data: str

class BuildBazelRemoteExecutionV2GetTreeResponse(
    typing_extensions.TypedDict, total=False
):
    directories: typing.List[BuildBazelRemoteExecutionV2Directory]
    nextPageToken: str

class BuildBazelRemoteExecutionV2BatchReadBlobsResponse(
    typing_extensions.TypedDict, total=False
):
    responses: typing.List[BuildBazelRemoteExecutionV2BatchReadBlobsResponseResponse]

class GoogleDevtoolsRemoteworkersV1test2CommandOverhead(
    typing_extensions.TypedDict, total=False
):
    duration: str
    overhead: str

class BuildBazelRemoteExecutionV2PlatformProperty(
    typing_extensions.TypedDict, total=False
):
    name: str
    value: str

class BuildBazelRemoteExecutionV2LogFile(typing_extensions.TypedDict, total=False):
    humanReadable: bool
    digest: BuildBazelRemoteExecutionV2Digest

class GoogleDevtoolsRemotebuildexecutionAdminV1alphaAutoscale(
    typing_extensions.TypedDict, total=False
):
    minSize: str
    maxSize: str

class BuildBazelSemverSemVer(typing_extensions.TypedDict, total=False):
    major: int
    prerelease: str
    patch: int
    minor: int

class BuildBazelRemoteExecutionV2FindMissingBlobsResponse(
    typing_extensions.TypedDict, total=False
):
    missingBlobDigests: typing.List[BuildBazelRemoteExecutionV2Digest]

class BuildBazelRemoteExecutionV2NodeProperty(typing_extensions.TypedDict, total=False):
    value: str
    name: str

class GoogleDevtoolsRemotebuildexecutionAdminV1alphaListInstancesResponse(
    typing_extensions.TypedDict, total=False
):
    instances: typing.List[GoogleDevtoolsRemotebuildexecutionAdminV1alphaInstance]

class BuildBazelRemoteExecutionV2Tree(typing_extensions.TypedDict, total=False):
    root: BuildBazelRemoteExecutionV2Directory
    children: typing.List[BuildBazelRemoteExecutionV2Directory]

class GoogleDevtoolsRemoteworkersV1test2Digest(
    typing_extensions.TypedDict, total=False
):
    hash: str
    sizeBytes: str

class BuildBazelRemoteExecutionV2ExecuteOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    stdoutStreamName: str
    stderrStreamName: str
    actionDigest: BuildBazelRemoteExecutionV2Digest
    stage: typing_extensions.Literal[
        "UNKNOWN", "CACHE_CHECK", "QUEUED", "EXECUTING", "COMPLETED"
    ]

class GoogleDevtoolsRemotebuildexecutionAdminV1alphaWorkerConfig(
    typing_extensions.TypedDict, total=False
):
    accelerator: GoogleDevtoolsRemotebuildexecutionAdminV1alphaAcceleratorConfig
    diskType: str
    diskSizeGb: str
    soleTenancy: GoogleDevtoolsRemotebuildexecutionAdminV1alphaSoleTenancyConfig
    vmImage: str
    networkAccess: str
    maxConcurrentActions: str
    minCpuPlatform: str
    reserved: bool
    machineType: str
    labels: typing.Dict[str, typing.Any]

class BuildBazelRemoteExecutionV2DirectoryNode(
    typing_extensions.TypedDict, total=False
):
    digest: BuildBazelRemoteExecutionV2Digest
    name: str

class GoogleDevtoolsRemotebuildbotResourceUsage(
    typing_extensions.TypedDict, total=False
):
    cpuUsedPercent: float
    diskUsage: GoogleDevtoolsRemotebuildbotResourceUsageStat
    memoryUsage: GoogleDevtoolsRemotebuildbotResourceUsageStat

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

class BuildBazelRemoteExecutionV2CacheCapabilities(
    typing_extensions.TypedDict, total=False
):
    cachePriorityCapabilities: BuildBazelRemoteExecutionV2PriorityCapabilities
    digestFunction: typing.List[str]
    maxBatchTotalSizeBytes: str
    symlinkAbsolutePathStrategy: typing_extensions.Literal[
        "UNKNOWN", "DISALLOWED", "ALLOWED"
    ]
    actionCacheUpdateCapabilities: BuildBazelRemoteExecutionV2ActionCacheUpdateCapabilities

class GoogleDevtoolsRemoteworkersV1test2CommandResult(
    typing_extensions.TypedDict, total=False
):
    status: GoogleRpcStatus
    overhead: str
    metadata: typing.List[typing.Dict[str, typing.Any]]
    outputs: GoogleDevtoolsRemoteworkersV1test2Digest
    duration: str
    exitCode: int

class GoogleDevtoolsRemotebuildexecutionAdminV1alphaDeleteInstanceRequest(
    typing_extensions.TypedDict, total=False
):
    name: str

class BuildBazelRemoteExecutionV2PriorityCapabilitiesPriorityRange(
    typing_extensions.TypedDict, total=False
):
    maxPriority: int
    minPriority: int

class BuildBazelRemoteExecutionV2OutputSymlink(
    typing_extensions.TypedDict, total=False
):
    nodeProperties: typing.List[BuildBazelRemoteExecutionV2NodeProperty]
    target: str
    path: str

class GoogleDevtoolsRemotebuildexecutionAdminV1alphaUpdateWorkerPoolRequest(
    typing_extensions.TypedDict, total=False
):
    updateMask: str
    workerPool: GoogleDevtoolsRemotebuildexecutionAdminV1alphaWorkerPool

class GoogleDevtoolsRemotebuildexecutionAdminV1alphaSoleTenancyConfig(
    typing_extensions.TypedDict, total=False
):
    nodesZone: str
    nodeType: str

class BuildBazelRemoteExecutionV2FileNode(typing_extensions.TypedDict, total=False):
    name: str
    digest: BuildBazelRemoteExecutionV2Digest
    isExecutable: bool
    nodeProperties: typing.List[BuildBazelRemoteExecutionV2NodeProperty]

class GoogleDevtoolsRemotebuildexecutionAdminV1alphaDeleteWorkerPoolRequest(
    typing_extensions.TypedDict, total=False
):
    name: str

class GoogleDevtoolsRemoteworkersV1test2Directory(
    typing_extensions.TypedDict, total=False
):
    files: typing.List[GoogleDevtoolsRemoteworkersV1test2FileMetadata]
    directories: typing.List[GoogleDevtoolsRemoteworkersV1test2DirectoryMetadata]

class BuildBazelRemoteExecutionV2Action(typing_extensions.TypedDict, total=False):
    doNotCache: bool
    inputRootDigest: BuildBazelRemoteExecutionV2Digest
    timeout: str
    commandDigest: BuildBazelRemoteExecutionV2Digest
    outputNodeProperties: typing.List[str]

class GoogleDevtoolsRemoteworkersV1test2CommandTaskInputs(
    typing_extensions.TypedDict, total=False
):
    workingDirectory: str
    inlineBlobs: typing.List[GoogleDevtoolsRemoteworkersV1test2Blob]
    arguments: typing.List[str]
    files: typing.List[GoogleDevtoolsRemoteworkersV1test2Digest]
    environmentVariables: typing.List[
        GoogleDevtoolsRemoteworkersV1test2CommandTaskInputsEnvironmentVariable
    ]

class GoogleDevtoolsRemoteworkersV1test2CommandTask(
    typing_extensions.TypedDict, total=False
):
    expectedOutputs: GoogleDevtoolsRemoteworkersV1test2CommandTaskOutputs
    timeouts: GoogleDevtoolsRemoteworkersV1test2CommandTaskTimeouts
    inputs: GoogleDevtoolsRemoteworkersV1test2CommandTaskInputs

class BuildBazelRemoteExecutionV2BatchReadBlobsRequest(
    typing_extensions.TypedDict, total=False
):
    digests: typing.List[BuildBazelRemoteExecutionV2Digest]

class GoogleDevtoolsRemotebuildexecutionAdminV1alphaFeaturePolicy(
    typing_extensions.TypedDict, total=False
):
    dockerPrivileged: GoogleDevtoolsRemotebuildexecutionAdminV1alphaFeaturePolicyFeature
    dockerSiblingContainers: GoogleDevtoolsRemotebuildexecutionAdminV1alphaFeaturePolicyFeature
    linuxIsolation: typing_extensions.Literal[
        "LINUX_ISOLATION_UNSPECIFIED", "GVISOR", "OFF"
    ]
    dockerRuntime: GoogleDevtoolsRemotebuildexecutionAdminV1alphaFeaturePolicyFeature
    dockerRunAsRoot: GoogleDevtoolsRemotebuildexecutionAdminV1alphaFeaturePolicyFeature
    dockerNetwork: GoogleDevtoolsRemotebuildexecutionAdminV1alphaFeaturePolicyFeature
    dockerChrootPath: GoogleDevtoolsRemotebuildexecutionAdminV1alphaFeaturePolicyFeature
    dockerAddCapabilities: GoogleDevtoolsRemotebuildexecutionAdminV1alphaFeaturePolicyFeature
    containerImageSources: GoogleDevtoolsRemotebuildexecutionAdminV1alphaFeaturePolicyFeature

class BuildBazelRemoteExecutionV2BatchUpdateBlobsResponseResponse(
    typing_extensions.TypedDict, total=False
):
    digest: BuildBazelRemoteExecutionV2Digest
    status: GoogleRpcStatus

class GoogleDevtoolsRemoteworkersV1test2CommandOutputs(
    typing_extensions.TypedDict, total=False
):
    outputs: GoogleDevtoolsRemoteworkersV1test2Digest
    exitCode: int

class GoogleDevtoolsRemoteworkersV1test2DirectoryMetadata(
    typing_extensions.TypedDict, total=False
):
    path: str
    digest: GoogleDevtoolsRemoteworkersV1test2Digest

class BuildBazelRemoteExecutionV2RequestMetadata(
    typing_extensions.TypedDict, total=False
):
    toolDetails: BuildBazelRemoteExecutionV2ToolDetails
    correlatedInvocationsId: str
    toolInvocationId: str
    actionId: str

class GoogleDevtoolsRemotebuildexecutionAdminV1alphaAcceleratorConfig(
    typing_extensions.TypedDict, total=False
):
    acceleratorCount: str
    acceleratorType: str

class GoogleDevtoolsRemoteworkersV1test2FileMetadata(
    typing_extensions.TypedDict, total=False
):
    isExecutable: bool
    path: str
    digest: GoogleDevtoolsRemoteworkersV1test2Digest
    contents: str

class GoogleDevtoolsRemotebuildexecutionAdminV1alphaInstance(
    typing_extensions.TypedDict, total=False
):
    location: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "CREATING", "RUNNING", "INACTIVE"
    ]
    loggingEnabled: bool
    featurePolicy: GoogleDevtoolsRemotebuildexecutionAdminV1alphaFeaturePolicy
    name: str

class BuildBazelRemoteExecutionV2ExecutionCapabilities(
    typing_extensions.TypedDict, total=False
):
    executionPriorityCapabilities: BuildBazelRemoteExecutionV2PriorityCapabilities
    digestFunction: typing_extensions.Literal[
        "UNKNOWN", "SHA256", "SHA1", "MD5", "VSO", "SHA384", "SHA512"
    ]
    execEnabled: bool
    supportedNodeProperties: typing.List[str]

class BuildBazelRemoteExecutionV2ActionCacheUpdateCapabilities(
    typing_extensions.TypedDict, total=False
):
    updateEnabled: bool

class GoogleDevtoolsRemotebuildexecutionAdminV1alphaListWorkerPoolsResponse(
    typing_extensions.TypedDict, total=False
):
    workerPools: typing.List[GoogleDevtoolsRemotebuildexecutionAdminV1alphaWorkerPool]

class GoogleDevtoolsRemotebuildexecutionAdminV1alphaWorkerPool(
    typing_extensions.TypedDict, total=False
):
    name: str
    workerCount: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "CREATING", "RUNNING", "UPDATING", "DELETING", "INACTIVE"
    ]
    channel: str
    workerConfig: GoogleDevtoolsRemotebuildexecutionAdminV1alphaWorkerConfig
    autoscale: GoogleDevtoolsRemotebuildexecutionAdminV1alphaAutoscale
