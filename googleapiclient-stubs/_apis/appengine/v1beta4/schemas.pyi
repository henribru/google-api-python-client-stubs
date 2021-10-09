import typing

import typing_extensions

_list = list

@typing.type_check_only
class ApiConfigHandler(typing_extensions.TypedDict, total=False):
    authFailAction: typing_extensions.Literal[
        "AUTH_FAIL_ACTION_UNSPECIFIED",
        "AUTH_FAIL_ACTION_REDIRECT",
        "AUTH_FAIL_ACTION_UNAUTHORIZED",
    ]
    login: typing_extensions.Literal[
        "LOGIN_UNSPECIFIED", "LOGIN_OPTIONAL", "LOGIN_ADMIN", "LOGIN_REQUIRED"
    ]
    script: str
    securityLevel: typing_extensions.Literal[
        "SECURE_UNSPECIFIED",
        "SECURE_DEFAULT",
        "SECURE_NEVER",
        "SECURE_OPTIONAL",
        "SECURE_ALWAYS",
    ]
    url: str

@typing.type_check_only
class ApiEndpointHandler(typing_extensions.TypedDict, total=False):
    scriptPath: str

@typing.type_check_only
class Application(typing_extensions.TypedDict, total=False):
    authDomain: str
    codeBucket: str
    defaultBucket: str
    defaultCookieExpiration: str
    defaultHostname: str
    dispatchRules: _list[UrlDispatchRule]
    iap: IdentityAwareProxy
    id: str
    location: str
    name: str

@typing.type_check_only
class AutomaticScaling(typing_extensions.TypedDict, total=False):
    coolDownPeriod: str
    cpuUtilization: CpuUtilization
    diskUtilization: DiskUtilization
    maxConcurrentRequests: int
    maxIdleInstances: int
    maxPendingLatency: str
    maxTotalInstances: int
    minIdleInstances: int
    minPendingLatency: str
    minTotalInstances: int
    networkUtilization: NetworkUtilization
    requestUtilization: RequestUtilization

@typing.type_check_only
class BasicScaling(typing_extensions.TypedDict, total=False):
    idleTimeout: str
    maxInstances: int

@typing.type_check_only
class ContainerInfo(typing_extensions.TypedDict, total=False):
    image: str

@typing.type_check_only
class CpuUtilization(typing_extensions.TypedDict, total=False):
    aggregationWindowLength: str
    targetUtilization: float

@typing.type_check_only
class CreateVersionMetadataV1(typing_extensions.TypedDict, total=False):
    cloudBuildId: str

@typing.type_check_only
class CreateVersionMetadataV1Alpha(typing_extensions.TypedDict, total=False):
    cloudBuildId: str

@typing.type_check_only
class CreateVersionMetadataV1Beta(typing_extensions.TypedDict, total=False):
    cloudBuildId: str

@typing.type_check_only
class DebugInstanceRequest(typing_extensions.TypedDict, total=False):
    sshKey: str

@typing.type_check_only
class Deployment(typing_extensions.TypedDict, total=False):
    container: ContainerInfo
    files: dict[str, typing.Any]
    sourceReferences: _list[SourceReference]

@typing.type_check_only
class DiskUtilization(typing_extensions.TypedDict, total=False):
    targetReadBytesPerSec: int
    targetReadOpsPerSec: int
    targetWriteBytesPerSec: int
    targetWriteOpsPerSec: int

@typing.type_check_only
class EndpointsApiService(typing_extensions.TypedDict, total=False):
    configId: str
    disableTraceSampling: bool
    name: str
    rolloutStrategy: typing_extensions.Literal[
        "UNSPECIFIED_ROLLOUT_STRATEGY", "FIXED", "MANAGED"
    ]

@typing.type_check_only
class ErrorHandler(typing_extensions.TypedDict, total=False):
    errorCode: typing_extensions.Literal[
        "ERROR_CODE_UNSPECIFIED",
        "ERROR_CODE_DEFAULT",
        "ERROR_CODE_OVER_QUOTA",
        "ERROR_CODE_DOS_API_DENIAL",
        "ERROR_CODE_TIMEOUT",
    ]
    mimeType: str
    staticFile: str

@typing.type_check_only
class FileInfo(typing_extensions.TypedDict, total=False):
    mimeType: str
    sha1Sum: str
    sourceUrl: str

@typing.type_check_only
class HealthCheck(typing_extensions.TypedDict, total=False):
    checkInterval: str
    disableHealthCheck: bool
    healthyThreshold: int
    host: str
    restartThreshold: int
    timeout: str
    unhealthyThreshold: int

@typing.type_check_only
class IdentityAwareProxy(typing_extensions.TypedDict, total=False):
    enabled: bool
    oauth2ClientId: str
    oauth2ClientSecret: str
    oauth2ClientSecretSha256: str

@typing.type_check_only
class Instance(typing_extensions.TypedDict, total=False):
    appEngineRelease: str
    availability: typing_extensions.Literal["UNSPECIFIED", "RESIDENT", "DYNAMIC"]
    averageLatency: int
    errors: int
    id: str
    memoryUsage: str
    name: str
    qps: float
    requests: int
    startTimestamp: str
    vmId: str
    vmIp: str
    vmName: str
    vmStatus: str
    vmUnlocked: bool
    vmZoneName: str

@typing.type_check_only
class Library(typing_extensions.TypedDict, total=False):
    name: str
    version: str

@typing.type_check_only
class ListInstancesResponse(typing_extensions.TypedDict, total=False):
    instances: _list[Instance]
    nextPageToken: str

@typing.type_check_only
class ListLocationsResponse(typing_extensions.TypedDict, total=False):
    locations: _list[Location]
    nextPageToken: str

@typing.type_check_only
class ListModulesResponse(typing_extensions.TypedDict, total=False):
    modules: _list[Module]
    nextPageToken: str

@typing.type_check_only
class ListOperationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    operations: _list[Operation]

@typing.type_check_only
class ListVersionsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    versions: _list[Version]

@typing.type_check_only
class Location(typing_extensions.TypedDict, total=False):
    displayName: str
    labels: dict[str, typing.Any]
    locationId: str
    metadata: dict[str, typing.Any]
    name: str

@typing.type_check_only
class LocationMetadata(typing_extensions.TypedDict, total=False):
    flexibleEnvironmentAvailable: bool
    standardEnvironmentAvailable: bool

@typing.type_check_only
class ManualScaling(typing_extensions.TypedDict, total=False):
    instances: int

@typing.type_check_only
class Module(typing_extensions.TypedDict, total=False):
    id: str
    name: str
    split: TrafficSplit

@typing.type_check_only
class Network(typing_extensions.TypedDict, total=False):
    forwardedPorts: _list[str]
    instanceTag: str
    name: str

@typing.type_check_only
class NetworkUtilization(typing_extensions.TypedDict, total=False):
    targetReceivedBytesPerSec: int
    targetReceivedPacketsPerSec: int
    targetSentBytesPerSec: int
    targetSentPacketsPerSec: int

@typing.type_check_only
class Operation(typing_extensions.TypedDict, total=False):
    done: bool
    error: Status
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class OperationMetadata(typing_extensions.TypedDict, total=False):
    endTime: str
    insertTime: str
    method: str
    operationType: str
    target: str
    user: str

@typing.type_check_only
class OperationMetadataV1(typing_extensions.TypedDict, total=False):
    createVersionMetadata: CreateVersionMetadataV1
    endTime: str
    ephemeralMessage: str
    insertTime: str
    method: str
    target: str
    user: str
    warning: _list[str]

@typing.type_check_only
class OperationMetadataV1Alpha(typing_extensions.TypedDict, total=False):
    createVersionMetadata: CreateVersionMetadataV1Alpha
    endTime: str
    ephemeralMessage: str
    insertTime: str
    method: str
    target: str
    user: str
    warning: _list[str]

@typing.type_check_only
class OperationMetadataV1Beta(typing_extensions.TypedDict, total=False):
    createVersionMetadata: CreateVersionMetadataV1Beta
    endTime: str
    ephemeralMessage: str
    insertTime: str
    method: str
    target: str
    user: str
    warning: _list[str]

@typing.type_check_only
class OperationMetadataV1Beta5(typing_extensions.TypedDict, total=False):
    endTime: str
    insertTime: str
    method: str
    target: str
    user: str

@typing.type_check_only
class RequestUtilization(typing_extensions.TypedDict, total=False):
    targetConcurrentRequests: int
    targetRequestCountPerSec: int

@typing.type_check_only
class Resources(typing_extensions.TypedDict, total=False):
    cpu: float
    diskGb: float
    memoryGb: float
    volumes: _list[Volume]

@typing.type_check_only
class ScriptHandler(typing_extensions.TypedDict, total=False):
    scriptPath: str

@typing.type_check_only
class SourceReference(typing_extensions.TypedDict, total=False):
    repository: str
    revisionId: str

@typing.type_check_only
class StaticDirectoryHandler(typing_extensions.TypedDict, total=False):
    applicationReadable: bool
    directory: str
    expiration: str
    httpHeaders: dict[str, typing.Any]
    mimeType: str
    requireMatchingFile: bool

@typing.type_check_only
class StaticFilesHandler(typing_extensions.TypedDict, total=False):
    applicationReadable: bool
    expiration: str
    httpHeaders: dict[str, typing.Any]
    mimeType: str
    path: str
    requireMatchingFile: bool
    uploadPathRegex: str

@typing.type_check_only
class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class TrafficSplit(typing_extensions.TypedDict, total=False):
    allocations: dict[str, typing.Any]
    shardBy: typing_extensions.Literal["UNSPECIFIED", "COOKIE", "IP"]

@typing.type_check_only
class UrlDispatchRule(typing_extensions.TypedDict, total=False):
    domain: str
    module: str
    path: str

@typing.type_check_only
class UrlMap(typing_extensions.TypedDict, total=False):
    apiEndpoint: ApiEndpointHandler
    authFailAction: typing_extensions.Literal[
        "AUTH_FAIL_ACTION_UNSPECIFIED",
        "AUTH_FAIL_ACTION_REDIRECT",
        "AUTH_FAIL_ACTION_UNAUTHORIZED",
    ]
    login: typing_extensions.Literal[
        "LOGIN_UNSPECIFIED", "LOGIN_OPTIONAL", "LOGIN_ADMIN", "LOGIN_REQUIRED"
    ]
    redirectHttpResponseCode: typing_extensions.Literal[
        "REDIRECT_HTTP_RESPONSE_CODE_UNSPECIFIED",
        "REDIRECT_HTTP_RESPONSE_CODE_301",
        "REDIRECT_HTTP_RESPONSE_CODE_302",
        "REDIRECT_HTTP_RESPONSE_CODE_303",
        "REDIRECT_HTTP_RESPONSE_CODE_307",
    ]
    script: ScriptHandler
    securityLevel: typing_extensions.Literal[
        "SECURE_UNSPECIFIED",
        "SECURE_DEFAULT",
        "SECURE_NEVER",
        "SECURE_OPTIONAL",
        "SECURE_ALWAYS",
    ]
    staticDirectory: StaticDirectoryHandler
    staticFiles: StaticFilesHandler
    urlRegex: str

@typing.type_check_only
class Version(typing_extensions.TypedDict, total=False):
    apiConfig: ApiConfigHandler
    automaticScaling: AutomaticScaling
    basicScaling: BasicScaling
    betaSettings: dict[str, typing.Any]
    creationTime: str
    defaultExpiration: str
    deployer: str
    deployment: Deployment
    endpointsApiService: EndpointsApiService
    env: str
    envVariables: dict[str, typing.Any]
    errorHandlers: _list[ErrorHandler]
    handlers: _list[UrlMap]
    healthCheck: HealthCheck
    id: str
    inboundServices: _list[str]
    instanceClass: str
    libraries: _list[Library]
    manualScaling: ManualScaling
    name: str
    network: Network
    nobuildFilesRegex: str
    resources: Resources
    runtime: str
    runtimeApiVersion: str
    runtimeMainExecutablePath: str
    servingStatus: typing_extensions.Literal[
        "SERVING_STATUS_UNSPECIFIED", "SERVING", "STOPPED"
    ]
    threadsafe: bool
    vm: bool

@typing.type_check_only
class Volume(typing_extensions.TypedDict, total=False):
    name: str
    sizeGb: float
    volumeType: str
