import typing

import typing_extensions

_list = list

@typing.type_check_only
class BuildBazelRemoteExecutionV2Action(typing_extensions.TypedDict, total=False):
    commandDigest: BuildBazelRemoteExecutionV2Digest
    doNotCache: bool
    inputRootDigest: BuildBazelRemoteExecutionV2Digest
    platform: BuildBazelRemoteExecutionV2Platform
    salt: str
    timeout: str

@typing.type_check_only
class BuildBazelRemoteExecutionV2ActionCacheUpdateCapabilities(
    typing_extensions.TypedDict, total=False
):
    updateEnabled: bool

@typing.type_check_only
class BuildBazelRemoteExecutionV2ActionResult(typing_extensions.TypedDict, total=False):
    executionMetadata: BuildBazelRemoteExecutionV2ExecutedActionMetadata
    exitCode: int
    outputDirectories: _list[BuildBazelRemoteExecutionV2OutputDirectory]
    outputDirectorySymlinks: _list[BuildBazelRemoteExecutionV2OutputSymlink]
    outputFileSymlinks: _list[BuildBazelRemoteExecutionV2OutputSymlink]
    outputFiles: _list[BuildBazelRemoteExecutionV2OutputFile]
    outputSymlinks: _list[BuildBazelRemoteExecutionV2OutputSymlink]
    stderrDigest: BuildBazelRemoteExecutionV2Digest
    stderrRaw: str
    stdoutDigest: BuildBazelRemoteExecutionV2Digest
    stdoutRaw: str

@typing.type_check_only
class BuildBazelRemoteExecutionV2BatchReadBlobsRequest(
    typing_extensions.TypedDict, total=False
):
    digests: _list[BuildBazelRemoteExecutionV2Digest]

@typing.type_check_only
class BuildBazelRemoteExecutionV2BatchReadBlobsResponse(
    typing_extensions.TypedDict, total=False
):
    responses: _list[BuildBazelRemoteExecutionV2BatchReadBlobsResponseResponse]

@typing.type_check_only
class BuildBazelRemoteExecutionV2BatchReadBlobsResponseResponse(
    typing_extensions.TypedDict, total=False
):
    data: str
    digest: BuildBazelRemoteExecutionV2Digest
    status: GoogleRpcStatus

@typing.type_check_only
class BuildBazelRemoteExecutionV2BatchUpdateBlobsRequest(
    typing_extensions.TypedDict, total=False
):
    requests: _list[BuildBazelRemoteExecutionV2BatchUpdateBlobsRequestRequest]

@typing.type_check_only
class BuildBazelRemoteExecutionV2BatchUpdateBlobsRequestRequest(
    typing_extensions.TypedDict, total=False
):
    data: str
    digest: BuildBazelRemoteExecutionV2Digest

@typing.type_check_only
class BuildBazelRemoteExecutionV2BatchUpdateBlobsResponse(
    typing_extensions.TypedDict, total=False
):
    responses: _list[BuildBazelRemoteExecutionV2BatchUpdateBlobsResponseResponse]

@typing.type_check_only
class BuildBazelRemoteExecutionV2BatchUpdateBlobsResponseResponse(
    typing_extensions.TypedDict, total=False
):
    digest: BuildBazelRemoteExecutionV2Digest
    status: GoogleRpcStatus

@typing.type_check_only
class BuildBazelRemoteExecutionV2CacheCapabilities(
    typing_extensions.TypedDict, total=False
):
    actionCacheUpdateCapabilities: BuildBazelRemoteExecutionV2ActionCacheUpdateCapabilities
    cachePriorityCapabilities: BuildBazelRemoteExecutionV2PriorityCapabilities
    digestFunction: _list[str]
    maxBatchTotalSizeBytes: str
    supportedCompressor: _list[str]
    symlinkAbsolutePathStrategy: typing_extensions.Literal[
        "UNKNOWN", "DISALLOWED", "ALLOWED"
    ]

@typing.type_check_only
class BuildBazelRemoteExecutionV2Command(typing_extensions.TypedDict, total=False):
    arguments: _list[str]
    environmentVariables: _list[BuildBazelRemoteExecutionV2CommandEnvironmentVariable]
    outputDirectories: _list[str]
    outputFiles: _list[str]
    outputNodeProperties: _list[str]
    outputPaths: _list[str]
    platform: BuildBazelRemoteExecutionV2Platform
    workingDirectory: str

@typing.type_check_only
class BuildBazelRemoteExecutionV2CommandEnvironmentVariable(
    typing_extensions.TypedDict, total=False
):
    name: str
    value: str

@typing.type_check_only
class BuildBazelRemoteExecutionV2Digest(typing_extensions.TypedDict, total=False):
    hash: str
    sizeBytes: str

@typing.type_check_only
class BuildBazelRemoteExecutionV2Directory(typing_extensions.TypedDict, total=False):
    directories: _list[BuildBazelRemoteExecutionV2DirectoryNode]
    files: _list[BuildBazelRemoteExecutionV2FileNode]
    nodeProperties: BuildBazelRemoteExecutionV2NodeProperties
    symlinks: _list[BuildBazelRemoteExecutionV2SymlinkNode]

@typing.type_check_only
class BuildBazelRemoteExecutionV2DirectoryNode(
    typing_extensions.TypedDict, total=False
):
    digest: BuildBazelRemoteExecutionV2Digest
    name: str

@typing.type_check_only
class BuildBazelRemoteExecutionV2ExecuteOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    actionDigest: BuildBazelRemoteExecutionV2Digest
    stage: typing_extensions.Literal[
        "UNKNOWN", "CACHE_CHECK", "QUEUED", "EXECUTING", "COMPLETED"
    ]
    stderrStreamName: str
    stdoutStreamName: str

@typing.type_check_only
class BuildBazelRemoteExecutionV2ExecuteRequest(
    typing_extensions.TypedDict, total=False
):
    actionDigest: BuildBazelRemoteExecutionV2Digest
    executionPolicy: BuildBazelRemoteExecutionV2ExecutionPolicy
    resultsCachePolicy: BuildBazelRemoteExecutionV2ResultsCachePolicy
    skipCacheLookup: bool

@typing.type_check_only
class BuildBazelRemoteExecutionV2ExecuteResponse(
    typing_extensions.TypedDict, total=False
):
    cachedResult: bool
    message: str
    result: BuildBazelRemoteExecutionV2ActionResult
    serverLogs: dict[str, typing.Any]
    status: GoogleRpcStatus

@typing.type_check_only
class BuildBazelRemoteExecutionV2ExecutedActionMetadata(
    typing_extensions.TypedDict, total=False
):
    auxiliaryMetadata: _list[dict[str, typing.Any]]
    executionCompletedTimestamp: str
    executionStartTimestamp: str
    inputFetchCompletedTimestamp: str
    inputFetchStartTimestamp: str
    outputUploadCompletedTimestamp: str
    outputUploadStartTimestamp: str
    queuedTimestamp: str
    worker: str
    workerCompletedTimestamp: str
    workerStartTimestamp: str

@typing.type_check_only
class BuildBazelRemoteExecutionV2ExecutionCapabilities(
    typing_extensions.TypedDict, total=False
):
    digestFunction: typing_extensions.Literal[
        "UNKNOWN", "SHA256", "SHA1", "MD5", "VSO", "SHA384", "SHA512", "MURMUR3"
    ]
    execEnabled: bool
    executionPriorityCapabilities: BuildBazelRemoteExecutionV2PriorityCapabilities
    supportedNodeProperties: _list[str]

@typing.type_check_only
class BuildBazelRemoteExecutionV2ExecutionPolicy(
    typing_extensions.TypedDict, total=False
):
    priority: int

@typing.type_check_only
class BuildBazelRemoteExecutionV2FileNode(typing_extensions.TypedDict, total=False):
    digest: BuildBazelRemoteExecutionV2Digest
    isExecutable: bool
    name: str
    nodeProperties: BuildBazelRemoteExecutionV2NodeProperties

@typing.type_check_only
class BuildBazelRemoteExecutionV2FindMissingBlobsRequest(
    typing_extensions.TypedDict, total=False
):
    blobDigests: _list[BuildBazelRemoteExecutionV2Digest]

@typing.type_check_only
class BuildBazelRemoteExecutionV2FindMissingBlobsResponse(
    typing_extensions.TypedDict, total=False
):
    missingBlobDigests: _list[BuildBazelRemoteExecutionV2Digest]

@typing.type_check_only
class BuildBazelRemoteExecutionV2GetTreeResponse(
    typing_extensions.TypedDict, total=False
):
    directories: _list[BuildBazelRemoteExecutionV2Directory]
    nextPageToken: str

@typing.type_check_only
class BuildBazelRemoteExecutionV2LogFile(typing_extensions.TypedDict, total=False):
    digest: BuildBazelRemoteExecutionV2Digest
    humanReadable: bool

@typing.type_check_only
class BuildBazelRemoteExecutionV2NodeProperties(
    typing_extensions.TypedDict, total=False
):
    mtime: str
    properties: _list[BuildBazelRemoteExecutionV2NodeProperty]
    unixMode: int

@typing.type_check_only
class BuildBazelRemoteExecutionV2NodeProperty(typing_extensions.TypedDict, total=False):
    name: str
    value: str

@typing.type_check_only
class BuildBazelRemoteExecutionV2OutputDirectory(
    typing_extensions.TypedDict, total=False
):
    path: str
    treeDigest: BuildBazelRemoteExecutionV2Digest

@typing.type_check_only
class BuildBazelRemoteExecutionV2OutputFile(typing_extensions.TypedDict, total=False):
    contents: str
    digest: BuildBazelRemoteExecutionV2Digest
    isExecutable: bool
    nodeProperties: BuildBazelRemoteExecutionV2NodeProperties
    path: str

@typing.type_check_only
class BuildBazelRemoteExecutionV2OutputSymlink(
    typing_extensions.TypedDict, total=False
):
    nodeProperties: BuildBazelRemoteExecutionV2NodeProperties
    path: str
    target: str

@typing.type_check_only
class BuildBazelRemoteExecutionV2Platform(typing_extensions.TypedDict, total=False):
    properties: _list[BuildBazelRemoteExecutionV2PlatformProperty]

@typing.type_check_only
class BuildBazelRemoteExecutionV2PlatformProperty(
    typing_extensions.TypedDict, total=False
):
    name: str
    value: str

@typing.type_check_only
class BuildBazelRemoteExecutionV2PriorityCapabilities(
    typing_extensions.TypedDict, total=False
):
    priorities: _list[BuildBazelRemoteExecutionV2PriorityCapabilitiesPriorityRange]

@typing.type_check_only
class BuildBazelRemoteExecutionV2PriorityCapabilitiesPriorityRange(
    typing_extensions.TypedDict, total=False
):
    maxPriority: int
    minPriority: int

@typing.type_check_only
class BuildBazelRemoteExecutionV2RequestMetadata(
    typing_extensions.TypedDict, total=False
):
    actionId: str
    actionMnemonic: str
    configurationId: str
    correlatedInvocationsId: str
    targetId: str
    toolDetails: BuildBazelRemoteExecutionV2ToolDetails
    toolInvocationId: str

@typing.type_check_only
class BuildBazelRemoteExecutionV2ResultsCachePolicy(
    typing_extensions.TypedDict, total=False
):
    priority: int

@typing.type_check_only
class BuildBazelRemoteExecutionV2ServerCapabilities(
    typing_extensions.TypedDict, total=False
):
    cacheCapabilities: BuildBazelRemoteExecutionV2CacheCapabilities
    deprecatedApiVersion: BuildBazelSemverSemVer
    executionCapabilities: BuildBazelRemoteExecutionV2ExecutionCapabilities
    highApiVersion: BuildBazelSemverSemVer
    lowApiVersion: BuildBazelSemverSemVer

@typing.type_check_only
class BuildBazelRemoteExecutionV2SymlinkNode(typing_extensions.TypedDict, total=False):
    name: str
    nodeProperties: BuildBazelRemoteExecutionV2NodeProperties
    target: str

@typing.type_check_only
class BuildBazelRemoteExecutionV2ToolDetails(typing_extensions.TypedDict, total=False):
    toolName: str
    toolVersion: str

@typing.type_check_only
class BuildBazelRemoteExecutionV2Tree(typing_extensions.TypedDict, total=False):
    children: _list[BuildBazelRemoteExecutionV2Directory]
    root: BuildBazelRemoteExecutionV2Directory

@typing.type_check_only
class BuildBazelRemoteExecutionV2WaitExecutionRequest(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class BuildBazelSemverSemVer(typing_extensions.TypedDict, total=False):
    major: int
    minor: int
    patch: int
    prerelease: str

@typing.type_check_only
class GoogleDevtoolsRemotebuildbotCommandDurations(
    typing_extensions.TypedDict, total=False
):
    casRelease: str
    cmWaitForAssignment: str
    dockerPrep: str
    dockerPrepStartTime: str
    download: str
    downloadStartTime: str
    execStartTime: str
    execution: str
    isoPrepDone: str
    overall: str
    stdout: str
    upload: str
    uploadStartTime: str

@typing.type_check_only
class GoogleDevtoolsRemotebuildbotCommandEvents(
    typing_extensions.TypedDict, total=False
):
    cmUsage: typing_extensions.Literal["CONFIG_NONE", "CONFIG_MATCH", "CONFIG_MISMATCH"]
    dockerCacheHit: bool
    dockerImageName: str
    inputCacheMiss: float
    numErrors: str
    numWarnings: str
    outputLocation: typing_extensions.Literal[
        "LOCATION_UNDEFINED",
        "LOCATION_NONE",
        "LOCATION_EXEC_ROOT_RELATIVE",
        "LOCATION_WORKING_DIR_RELATIVE",
        "LOCATION_EXEC_ROOT_AND_WORKING_DIR_RELATIVE",
        "LOCATION_EXEC_ROOT_RELATIVE_OUTPUT_OUTSIDE_WORKING_DIR",
        "LOCATION_EXEC_ROOT_AND_WORKING_DIR_RELATIVE_OUTPUT_OUTSIDE_WORKING_DIR",
    ]
    usedAsyncContainer: bool

@typing.type_check_only
class GoogleDevtoolsRemotebuildbotCommandStatus(
    typing_extensions.TypedDict, total=False
):
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
        "DOCKER_TOO_MANY_SYMBOLIC_LINK_LEVELS",
        "LOCAL_CONTAINER_MANAGER_NOT_RUNNING",
        "DOCKER_IMAGE_VPCSC_PERMISSION_DENIED",
        "WORKING_DIR_NOT_RELATIVE",
        "DOCKER_MISSING_CONTAINER",
    ]
    message: str

@typing.type_check_only
class GoogleDevtoolsRemotebuildbotResourceUsage(
    typing_extensions.TypedDict, total=False
):
    cpuUsedPercent: float
    diskUsage: GoogleDevtoolsRemotebuildbotResourceUsageStat
    memoryUsage: GoogleDevtoolsRemotebuildbotResourceUsageStat
    totalDiskIoStats: GoogleDevtoolsRemotebuildbotResourceUsageIOStats

@typing.type_check_only
class GoogleDevtoolsRemotebuildbotResourceUsageIOStats(
    typing_extensions.TypedDict, total=False
):
    readBytesCount: str
    readCount: str
    readTimeMs: str
    writeBytesCount: str
    writeCount: str
    writeTimeMs: str

@typing.type_check_only
class GoogleDevtoolsRemotebuildbotResourceUsageStat(
    typing_extensions.TypedDict, total=False
):
    total: str
    used: str

@typing.type_check_only
class GoogleDevtoolsRemotebuildexecutionAdminV1alphaAcceleratorConfig(
    typing_extensions.TypedDict, total=False
):
    acceleratorCount: str
    acceleratorType: str

@typing.type_check_only
class GoogleDevtoolsRemotebuildexecutionAdminV1alphaAutoscale(
    typing_extensions.TypedDict, total=False
):
    maxSize: str
    minSize: str

@typing.type_check_only
class GoogleDevtoolsRemotebuildexecutionAdminV1alphaCreateInstanceRequest(
    typing_extensions.TypedDict, total=False
):
    instance: GoogleDevtoolsRemotebuildexecutionAdminV1alphaInstance
    instanceId: str
    parent: str

@typing.type_check_only
class GoogleDevtoolsRemotebuildexecutionAdminV1alphaCreateWorkerPoolRequest(
    typing_extensions.TypedDict, total=False
):
    parent: str
    poolId: str
    workerPool: GoogleDevtoolsRemotebuildexecutionAdminV1alphaWorkerPool

@typing.type_check_only
class GoogleDevtoolsRemotebuildexecutionAdminV1alphaDeleteInstanceRequest(
    typing_extensions.TypedDict, total=False
):
    name: str

@typing.type_check_only
class GoogleDevtoolsRemotebuildexecutionAdminV1alphaDeleteWorkerPoolRequest(
    typing_extensions.TypedDict, total=False
):
    name: str

@typing.type_check_only
class GoogleDevtoolsRemotebuildexecutionAdminV1alphaFeaturePolicy(
    typing_extensions.TypedDict, total=False
):
    containerImageSources: GoogleDevtoolsRemotebuildexecutionAdminV1alphaFeaturePolicyFeature
    dockerAddCapabilities: GoogleDevtoolsRemotebuildexecutionAdminV1alphaFeaturePolicyFeature
    dockerChrootPath: GoogleDevtoolsRemotebuildexecutionAdminV1alphaFeaturePolicyFeature
    dockerNetwork: GoogleDevtoolsRemotebuildexecutionAdminV1alphaFeaturePolicyFeature
    dockerPrivileged: GoogleDevtoolsRemotebuildexecutionAdminV1alphaFeaturePolicyFeature
    dockerRunAsRoot: GoogleDevtoolsRemotebuildexecutionAdminV1alphaFeaturePolicyFeature
    dockerRuntime: GoogleDevtoolsRemotebuildexecutionAdminV1alphaFeaturePolicyFeature
    dockerSiblingContainers: GoogleDevtoolsRemotebuildexecutionAdminV1alphaFeaturePolicyFeature
    linuxIsolation: typing_extensions.Literal[
        "LINUX_ISOLATION_UNSPECIFIED", "GVISOR", "OFF"
    ]

@typing.type_check_only
class GoogleDevtoolsRemotebuildexecutionAdminV1alphaFeaturePolicyFeature(
    typing_extensions.TypedDict, total=False
):
    allowedValues: _list[str]
    policy: typing_extensions.Literal[
        "POLICY_UNSPECIFIED", "ALLOWED", "FORBIDDEN", "RESTRICTED"
    ]

@typing.type_check_only
class GoogleDevtoolsRemotebuildexecutionAdminV1alphaGetInstanceRequest(
    typing_extensions.TypedDict, total=False
):
    name: str

@typing.type_check_only
class GoogleDevtoolsRemotebuildexecutionAdminV1alphaGetWorkerPoolRequest(
    typing_extensions.TypedDict, total=False
):
    name: str

@typing.type_check_only
class GoogleDevtoolsRemotebuildexecutionAdminV1alphaInstance(
    typing_extensions.TypedDict, total=False
):
    featurePolicy: GoogleDevtoolsRemotebuildexecutionAdminV1alphaFeaturePolicy
    location: str
    loggingEnabled: bool
    name: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "CREATING", "RUNNING", "INACTIVE"
    ]

@typing.type_check_only
class GoogleDevtoolsRemotebuildexecutionAdminV1alphaListInstancesRequest(
    typing_extensions.TypedDict, total=False
):
    parent: str

@typing.type_check_only
class GoogleDevtoolsRemotebuildexecutionAdminV1alphaListInstancesResponse(
    typing_extensions.TypedDict, total=False
):
    instances: _list[GoogleDevtoolsRemotebuildexecutionAdminV1alphaInstance]

@typing.type_check_only
class GoogleDevtoolsRemotebuildexecutionAdminV1alphaListWorkerPoolsRequest(
    typing_extensions.TypedDict, total=False
):
    filter: str
    parent: str

@typing.type_check_only
class GoogleDevtoolsRemotebuildexecutionAdminV1alphaListWorkerPoolsResponse(
    typing_extensions.TypedDict, total=False
):
    workerPools: _list[GoogleDevtoolsRemotebuildexecutionAdminV1alphaWorkerPool]

@typing.type_check_only
class GoogleDevtoolsRemotebuildexecutionAdminV1alphaUpdateInstanceRequest(
    typing_extensions.TypedDict, total=False
):
    instance: GoogleDevtoolsRemotebuildexecutionAdminV1alphaInstance
    loggingEnabled: bool
    name: str
    updateMask: str

@typing.type_check_only
class GoogleDevtoolsRemotebuildexecutionAdminV1alphaUpdateWorkerPoolRequest(
    typing_extensions.TypedDict, total=False
):
    updateMask: str
    workerPool: GoogleDevtoolsRemotebuildexecutionAdminV1alphaWorkerPool

@typing.type_check_only
class GoogleDevtoolsRemotebuildexecutionAdminV1alphaWorkerConfig(
    typing_extensions.TypedDict, total=False
):
    accelerator: GoogleDevtoolsRemotebuildexecutionAdminV1alphaAcceleratorConfig
    diskSizeGb: str
    diskType: str
    labels: dict[str, typing.Any]
    machineType: str
    maxConcurrentActions: str
    minCpuPlatform: str
    networkAccess: str
    reserved: bool
    soleTenantNodeType: str
    vmImage: str

@typing.type_check_only
class GoogleDevtoolsRemotebuildexecutionAdminV1alphaWorkerPool(
    typing_extensions.TypedDict, total=False
):
    autoscale: GoogleDevtoolsRemotebuildexecutionAdminV1alphaAutoscale
    channel: str
    name: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "CREATING", "RUNNING", "UPDATING", "DELETING", "INACTIVE"
    ]
    workerConfig: GoogleDevtoolsRemotebuildexecutionAdminV1alphaWorkerConfig
    workerCount: str

@typing.type_check_only
class GoogleDevtoolsRemoteworkersV1test2AdminTemp(
    typing_extensions.TypedDict, total=False
):
    arg: str
    command: typing_extensions.Literal[
        "UNSPECIFIED", "BOT_UPDATE", "BOT_RESTART", "BOT_TERMINATE", "HOST_RESTART"
    ]

@typing.type_check_only
class GoogleDevtoolsRemoteworkersV1test2Blob(typing_extensions.TypedDict, total=False):
    contents: str
    digest: GoogleDevtoolsRemoteworkersV1test2Digest

@typing.type_check_only
class GoogleDevtoolsRemoteworkersV1test2CommandOutputs(
    typing_extensions.TypedDict, total=False
):
    exitCode: int
    outputs: GoogleDevtoolsRemoteworkersV1test2Digest

@typing.type_check_only
class GoogleDevtoolsRemoteworkersV1test2CommandOverhead(
    typing_extensions.TypedDict, total=False
):
    duration: str
    overhead: str

@typing.type_check_only
class GoogleDevtoolsRemoteworkersV1test2CommandResult(
    typing_extensions.TypedDict, total=False
):
    duration: str
    exitCode: int
    metadata: _list[dict[str, typing.Any]]
    outputs: GoogleDevtoolsRemoteworkersV1test2Digest
    overhead: str
    status: GoogleRpcStatus

@typing.type_check_only
class GoogleDevtoolsRemoteworkersV1test2CommandTask(
    typing_extensions.TypedDict, total=False
):
    expectedOutputs: GoogleDevtoolsRemoteworkersV1test2CommandTaskOutputs
    inputs: GoogleDevtoolsRemoteworkersV1test2CommandTaskInputs
    timeouts: GoogleDevtoolsRemoteworkersV1test2CommandTaskTimeouts

@typing.type_check_only
class GoogleDevtoolsRemoteworkersV1test2CommandTaskInputs(
    typing_extensions.TypedDict, total=False
):
    arguments: _list[str]
    environmentVariables: _list[
        GoogleDevtoolsRemoteworkersV1test2CommandTaskInputsEnvironmentVariable
    ]
    files: _list[GoogleDevtoolsRemoteworkersV1test2Digest]
    inlineBlobs: _list[GoogleDevtoolsRemoteworkersV1test2Blob]
    workingDirectory: str

@typing.type_check_only
class GoogleDevtoolsRemoteworkersV1test2CommandTaskInputsEnvironmentVariable(
    typing_extensions.TypedDict, total=False
):
    name: str
    value: str

@typing.type_check_only
class GoogleDevtoolsRemoteworkersV1test2CommandTaskOutputs(
    typing_extensions.TypedDict, total=False
):
    directories: _list[str]
    files: _list[str]
    stderrDestination: str
    stdoutDestination: str

@typing.type_check_only
class GoogleDevtoolsRemoteworkersV1test2CommandTaskTimeouts(
    typing_extensions.TypedDict, total=False
):
    execution: str
    idle: str
    shutdown: str

@typing.type_check_only
class GoogleDevtoolsRemoteworkersV1test2Digest(
    typing_extensions.TypedDict, total=False
):
    hash: str
    sizeBytes: str

@typing.type_check_only
class GoogleDevtoolsRemoteworkersV1test2Directory(
    typing_extensions.TypedDict, total=False
):
    directories: _list[GoogleDevtoolsRemoteworkersV1test2DirectoryMetadata]
    files: _list[GoogleDevtoolsRemoteworkersV1test2FileMetadata]

@typing.type_check_only
class GoogleDevtoolsRemoteworkersV1test2DirectoryMetadata(
    typing_extensions.TypedDict, total=False
):
    digest: GoogleDevtoolsRemoteworkersV1test2Digest
    path: str

@typing.type_check_only
class GoogleDevtoolsRemoteworkersV1test2FileMetadata(
    typing_extensions.TypedDict, total=False
):
    contents: str
    digest: GoogleDevtoolsRemoteworkersV1test2Digest
    isExecutable: bool
    path: str

@typing.type_check_only
class GoogleLongrunningOperation(typing_extensions.TypedDict, total=False):
    done: bool
    error: GoogleRpcStatus
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class GoogleRpcStatus(typing_extensions.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str
