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
    databaseType: typing_extensions.Literal[
        "DATABASE_TYPE_UNSPECIFIED",
        "CLOUD_DATASTORE",
        "CLOUD_FIRESTORE",
        "CLOUD_DATASTORE_COMPATIBILITY",
    ]
    defaultBucket: str
    defaultCookieExpiration: str
    defaultHostname: str
    dispatchRules: _list[UrlDispatchRule]
    featureSettings: FeatureSettings
    gcrDomain: str
    iap: IdentityAwareProxy
    id: str
    locationId: str
    name: str
    serviceAccount: str
    servingStatus: typing_extensions.Literal[
        "UNSPECIFIED", "SERVING", "USER_DISABLED", "SYSTEM_DISABLED"
    ]

@typing.type_check_only
class AuthorizedCertificate(typing_extensions.TypedDict, total=False):
    certificateRawData: CertificateRawData
    displayName: str
    domainMappingsCount: int
    domainNames: _list[str]
    expireTime: str
    id: str
    managedCertificate: ManagedCertificate
    name: str
    visibleDomainMappings: _list[str]

@typing.type_check_only
class AuthorizedDomain(typing_extensions.TypedDict, total=False):
    id: str
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
    standardSchedulerSettings: StandardSchedulerSettings

@typing.type_check_only
class BasicScaling(typing_extensions.TypedDict, total=False):
    idleTimeout: str
    maxInstances: int

@typing.type_check_only
class BatchUpdateIngressRulesRequest(typing_extensions.TypedDict, total=False):
    ingressRules: _list[FirewallRule]

@typing.type_check_only
class BatchUpdateIngressRulesResponse(typing_extensions.TypedDict, total=False):
    ingressRules: _list[FirewallRule]

@typing.type_check_only
class CertificateRawData(typing_extensions.TypedDict, total=False):
    privateKey: str
    publicCertificate: str

@typing.type_check_only
class CloudBuildOptions(typing_extensions.TypedDict, total=False):
    appYamlPath: str
    cloudBuildTimeout: str

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
    cloudBuildOptions: CloudBuildOptions
    container: ContainerInfo
    files: dict[str, typing.Any]
    zip: ZipInfo

@typing.type_check_only
class DiskUtilization(typing_extensions.TypedDict, total=False):
    targetReadBytesPerSecond: int
    targetReadOpsPerSecond: int
    targetWriteBytesPerSecond: int
    targetWriteOpsPerSecond: int

@typing.type_check_only
class DomainMapping(typing_extensions.TypedDict, total=False):
    id: str
    name: str
    resourceRecords: _list[ResourceRecord]
    sslSettings: SslSettings

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class EndpointsApiService(typing_extensions.TypedDict, total=False):
    configId: str
    disableTraceSampling: bool
    name: str
    rolloutStrategy: typing_extensions.Literal[
        "UNSPECIFIED_ROLLOUT_STRATEGY", "FIXED", "MANAGED"
    ]

@typing.type_check_only
class Entrypoint(typing_extensions.TypedDict, total=False):
    shell: str

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
class FeatureSettings(typing_extensions.TypedDict, total=False):
    splitHealthChecks: bool
    useContainerOptimizedOs: bool

@typing.type_check_only
class FileInfo(typing_extensions.TypedDict, total=False):
    mimeType: str
    sha1Sum: str
    sourceUrl: str

@typing.type_check_only
class FirewallRule(typing_extensions.TypedDict, total=False):
    action: typing_extensions.Literal["UNSPECIFIED_ACTION", "ALLOW", "DENY"]
    description: str
    priority: int
    sourceRange: str

@typing.type_check_only
class GoogleAppengineV1betaLocationMetadata(typing_extensions.TypedDict, total=False):
    flexibleEnvironmentAvailable: bool
    searchApiAvailable: bool
    standardEnvironmentAvailable: bool

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
    startTime: str
    vmDebugEnabled: bool
    vmId: str
    vmIp: str
    vmLiveness: typing_extensions.Literal[
        "LIVENESS_STATE_UNSPECIFIED",
        "UNKNOWN",
        "HEALTHY",
        "UNHEALTHY",
        "DRAINING",
        "TIMEOUT",
    ]
    vmName: str
    vmStatus: str
    vmZoneName: str

@typing.type_check_only
class Library(typing_extensions.TypedDict, total=False):
    name: str
    version: str

@typing.type_check_only
class ListAuthorizedCertificatesResponse(typing_extensions.TypedDict, total=False):
    certificates: _list[AuthorizedCertificate]
    nextPageToken: str

@typing.type_check_only
class ListAuthorizedDomainsResponse(typing_extensions.TypedDict, total=False):
    domains: _list[AuthorizedDomain]
    nextPageToken: str

@typing.type_check_only
class ListDomainMappingsResponse(typing_extensions.TypedDict, total=False):
    domainMappings: _list[DomainMapping]
    nextPageToken: str

@typing.type_check_only
class ListIngressRulesResponse(typing_extensions.TypedDict, total=False):
    ingressRules: _list[FirewallRule]
    nextPageToken: str

@typing.type_check_only
class ListInstancesResponse(typing_extensions.TypedDict, total=False):
    instances: _list[Instance]
    nextPageToken: str

@typing.type_check_only
class ListLocationsResponse(typing_extensions.TypedDict, total=False):
    locations: _list[Location]
    nextPageToken: str

@typing.type_check_only
class ListOperationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    operations: _list[Operation]

@typing.type_check_only
class ListServicesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    services: _list[Service]

@typing.type_check_only
class ListVersionsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    versions: _list[Version]

@typing.type_check_only
class LivenessCheck(typing_extensions.TypedDict, total=False):
    checkInterval: str
    failureThreshold: int
    host: str
    initialDelay: str
    path: str
    successThreshold: int
    timeout: str

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
    searchApiAvailable: bool
    standardEnvironmentAvailable: bool

@typing.type_check_only
class ManagedCertificate(typing_extensions.TypedDict, total=False):
    lastRenewalTime: str
    status: typing_extensions.Literal[
        "MANAGEMENT_STATUS_UNSPECIFIED",
        "OK",
        "PENDING",
        "FAILED_RETRYING_NOT_VISIBLE",
        "FAILED_PERMANENT",
        "FAILED_RETRYING_CAA_FORBIDDEN",
        "FAILED_RETRYING_CAA_CHECKING",
    ]

@typing.type_check_only
class ManualScaling(typing_extensions.TypedDict, total=False):
    instances: int

@typing.type_check_only
class Network(typing_extensions.TypedDict, total=False):
    forwardedPorts: _list[str]
    instanceIpMode: typing_extensions.Literal[
        "INSTANCE_IP_MODE_UNSPECIFIED", "EXTERNAL", "INTERNAL"
    ]
    instanceTag: str
    name: str
    sessionAffinity: bool
    subnetworkName: str

@typing.type_check_only
class NetworkSettings(typing_extensions.TypedDict, total=False):
    ingressTrafficAllowed: typing_extensions.Literal[
        "INGRESS_TRAFFIC_ALLOWED_UNSPECIFIED",
        "INGRESS_TRAFFIC_ALLOWED_ALL",
        "INGRESS_TRAFFIC_ALLOWED_INTERNAL_ONLY",
        "INGRESS_TRAFFIC_ALLOWED_INTERNAL_AND_LB",
    ]

@typing.type_check_only
class NetworkUtilization(typing_extensions.TypedDict, total=False):
    targetReceivedBytesPerSecond: int
    targetReceivedPacketsPerSecond: int
    targetSentBytesPerSecond: int
    targetSentPacketsPerSecond: int

@typing.type_check_only
class Operation(typing_extensions.TypedDict, total=False):
    done: bool
    error: Status
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

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
class ReadinessCheck(typing_extensions.TypedDict, total=False):
    appStartTimeout: str
    checkInterval: str
    failureThreshold: int
    host: str
    path: str
    successThreshold: int
    timeout: str

@typing.type_check_only
class RepairApplicationRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class RequestUtilization(typing_extensions.TypedDict, total=False):
    targetConcurrentRequests: int
    targetRequestCountPerSecond: int

@typing.type_check_only
class ResourceRecord(typing_extensions.TypedDict, total=False):
    name: str
    rrdata: str
    type: typing_extensions.Literal["RECORD_TYPE_UNSPECIFIED", "A", "AAAA", "CNAME"]

@typing.type_check_only
class Resources(typing_extensions.TypedDict, total=False):
    cpu: float
    diskGb: float
    kmsKeyReference: str
    memoryGb: float
    volumes: _list[Volume]

@typing.type_check_only
class ScriptHandler(typing_extensions.TypedDict, total=False):
    scriptPath: str

@typing.type_check_only
class Service(typing_extensions.TypedDict, total=False):
    id: str
    labels: dict[str, typing.Any]
    name: str
    networkSettings: NetworkSettings
    split: TrafficSplit

@typing.type_check_only
class SslSettings(typing_extensions.TypedDict, total=False):
    certificateId: str
    pendingManagedCertificateId: str
    sslManagementType: typing_extensions.Literal[
        "SSL_MANAGEMENT_TYPE_UNSPECIFIED", "AUTOMATIC", "MANUAL"
    ]

@typing.type_check_only
class StandardSchedulerSettings(typing_extensions.TypedDict, total=False):
    maxInstances: int
    minInstances: int
    targetCpuUtilization: float
    targetThroughputUtilization: float

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
    shardBy: typing_extensions.Literal["UNSPECIFIED", "COOKIE", "IP", "RANDOM"]

@typing.type_check_only
class UrlDispatchRule(typing_extensions.TypedDict, total=False):
    domain: str
    path: str
    service: str

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
    staticFiles: StaticFilesHandler
    urlRegex: str

@typing.type_check_only
class Version(typing_extensions.TypedDict, total=False):
    apiConfig: ApiConfigHandler
    appEngineApis: bool
    automaticScaling: AutomaticScaling
    basicScaling: BasicScaling
    betaSettings: dict[str, typing.Any]
    buildEnvVariables: dict[str, typing.Any]
    createTime: str
    createdBy: str
    defaultExpiration: str
    deployment: Deployment
    diskUsageBytes: str
    endpointsApiService: EndpointsApiService
    entrypoint: Entrypoint
    env: str
    envVariables: dict[str, typing.Any]
    errorHandlers: _list[ErrorHandler]
    handlers: _list[UrlMap]
    healthCheck: HealthCheck
    id: str
    inboundServices: _list[str]
    instanceClass: str
    libraries: _list[Library]
    livenessCheck: LivenessCheck
    manualScaling: ManualScaling
    name: str
    network: Network
    nobuildFilesRegex: str
    readinessCheck: ReadinessCheck
    resources: Resources
    runtime: str
    runtimeApiVersion: str
    runtimeChannel: str
    runtimeMainExecutablePath: str
    serviceAccount: str
    servingStatus: typing_extensions.Literal[
        "SERVING_STATUS_UNSPECIFIED", "SERVING", "STOPPED"
    ]
    threadsafe: bool
    versionUrl: str
    vm: bool
    vpcAccessConnector: VpcAccessConnector
    zones: _list[str]

@typing.type_check_only
class Volume(typing_extensions.TypedDict, total=False):
    name: str
    sizeGb: float
    volumeType: str

@typing.type_check_only
class VpcAccessConnector(typing_extensions.TypedDict, total=False):
    egressSetting: typing_extensions.Literal[
        "EGRESS_SETTING_UNSPECIFIED", "ALL_TRAFFIC", "PRIVATE_IP_RANGES"
    ]
    name: str

@typing.type_check_only
class ZipInfo(typing_extensions.TypedDict, total=False):
    filesCount: int
    sourceUrl: str
