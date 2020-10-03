import typing

import typing_extensions

class CreateVersionMetadataV1Beta(typing_extensions.TypedDict, total=False):
    cloudBuildId: str

class AutomaticScaling(typing_extensions.TypedDict, total=False):
    minIdleInstances: int
    standardSchedulerSettings: StandardSchedulerSettings
    maxTotalInstances: int
    maxIdleInstances: int
    coolDownPeriod: str
    diskUtilization: DiskUtilization
    minPendingLatency: str
    maxConcurrentRequests: int
    requestUtilization: RequestUtilization
    maxPendingLatency: str
    minTotalInstances: int
    cpuUtilization: CpuUtilization
    networkUtilization: NetworkUtilization
    customMetrics: typing.List[CustomMetric]

class DomainMapping(typing_extensions.TypedDict, total=False):
    name: str
    sslSettings: SslSettings
    id: str
    resourceRecords: typing.List[ResourceRecord]

class UrlMap(typing_extensions.TypedDict, total=False):
    staticFiles: StaticFilesHandler
    script: ScriptHandler
    login: typing_extensions.Literal[
        "LOGIN_UNSPECIFIED", "LOGIN_OPTIONAL", "LOGIN_ADMIN", "LOGIN_REQUIRED"
    ]
    apiEndpoint: ApiEndpointHandler
    authFailAction: typing_extensions.Literal[
        "AUTH_FAIL_ACTION_UNSPECIFIED",
        "AUTH_FAIL_ACTION_REDIRECT",
        "AUTH_FAIL_ACTION_UNAUTHORIZED",
    ]
    redirectHttpResponseCode: typing_extensions.Literal[
        "REDIRECT_HTTP_RESPONSE_CODE_UNSPECIFIED",
        "REDIRECT_HTTP_RESPONSE_CODE_301",
        "REDIRECT_HTTP_RESPONSE_CODE_302",
        "REDIRECT_HTTP_RESPONSE_CODE_303",
        "REDIRECT_HTTP_RESPONSE_CODE_307",
    ]
    securityLevel: typing_extensions.Literal[
        "SECURE_UNSPECIFIED",
        "SECURE_DEFAULT",
        "SECURE_NEVER",
        "SECURE_OPTIONAL",
        "SECURE_ALWAYS",
    ]
    urlRegex: str

class FileInfo(typing_extensions.TypedDict, total=False):
    sourceUrl: str
    mimeType: str
    sha1Sum: str

class ListDomainMappingsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    domainMappings: typing.List[DomainMapping]

class StandardSchedulerSettings(typing_extensions.TypedDict, total=False):
    maxInstances: int
    targetThroughputUtilization: float
    targetCpuUtilization: float
    minInstances: int

class CreateVersionMetadataV1Alpha(typing_extensions.TypedDict, total=False):
    cloudBuildId: str

class Volume(typing_extensions.TypedDict, total=False):
    sizeGb: float
    volumeType: str
    name: str

class Instance(typing_extensions.TypedDict, total=False):
    vmLiveness: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "UNKNOWN", "HEALTHY", "UNHEALTHY", "DRAINING", "TIMEOUT"
    ]
    vmStatus: str
    memoryUsage: str
    availability: typing_extensions.Literal["UNSPECIFIED", "RESIDENT", "DYNAMIC"]
    vmZoneName: str
    vmDebugEnabled: bool
    id: str
    startTime: str
    qps: float
    vmId: str
    name: str
    appEngineRelease: str
    vmIp: str
    requests: int
    errors: int
    vmName: str
    averageLatency: int

class Service(typing_extensions.TypedDict, total=False):
    split: TrafficSplit
    id: str
    name: str
    networkSettings: NetworkSettings

class Version(typing_extensions.TypedDict, total=False):
    envVariables: typing.Dict[str, typing.Any]
    instanceClass: str
    versionUrl: str
    zones: typing.List[str]
    runtimeMainExecutablePath: str
    runtimeApiVersion: str
    basicScaling: BasicScaling
    vpcAccessConnector: VpcAccessConnector
    betaSettings: typing.Dict[str, typing.Any]
    buildEnvVariables: typing.Dict[str, typing.Any]
    errorHandlers: typing.List[ErrorHandler]
    apiConfig: ApiConfigHandler
    runtimeChannel: str
    nobuildFilesRegex: str
    threadsafe: bool
    createTime: str
    readinessCheck: ReadinessCheck
    deployment: Deployment
    handlers: typing.List[UrlMap]
    automaticScaling: AutomaticScaling
    network: Network
    diskUsageBytes: str
    servingStatus: typing_extensions.Literal[
        "SERVING_STATUS_UNSPECIFIED", "SERVING", "STOPPED"
    ]
    manualScaling: ManualScaling
    libraries: typing.List[Library]
    runtime: str
    resources: Resources
    endpointsApiService: EndpointsApiService
    createdBy: str
    name: str
    defaultExpiration: str
    env: str
    inboundServices: typing.List[str]
    entrypoint: Entrypoint
    id: str
    healthCheck: HealthCheck
    livenessCheck: LivenessCheck
    vm: bool

class Application(typing_extensions.TypedDict, total=False):
    defaultCookieExpiration: str
    featureSettings: FeatureSettings
    gcrDomain: str
    dispatchRules: typing.List[UrlDispatchRule]
    name: str
    defaultBucket: str
    iap: IdentityAwareProxy
    defaultHostname: str
    codeBucket: str
    authDomain: str
    databaseType: typing_extensions.Literal[
        "DATABASE_TYPE_UNSPECIFIED",
        "CLOUD_DATASTORE",
        "CLOUD_FIRESTORE",
        "CLOUD_DATASTORE_COMPATIBILITY",
    ]
    locationId: str
    id: str
    servingStatus: typing_extensions.Literal[
        "UNSPECIFIED", "SERVING", "USER_DISABLED", "SYSTEM_DISABLED"
    ]

class LivenessCheck(typing_extensions.TypedDict, total=False):
    host: str
    path: str
    checkInterval: str
    initialDelay: str
    failureThreshold: int
    timeout: str
    successThreshold: int

class StaticFilesHandler(typing_extensions.TypedDict, total=False):
    path: str
    uploadPathRegex: str
    requireMatchingFile: bool
    mimeType: str
    applicationReadable: bool
    httpHeaders: typing.Dict[str, typing.Any]
    expiration: str

class BatchUpdateIngressRulesRequest(typing_extensions.TypedDict, total=False):
    ingressRules: typing.List[FirewallRule]

class CpuUtilization(typing_extensions.TypedDict, total=False):
    aggregationWindowLength: str
    targetUtilization: float

class ApiConfigHandler(typing_extensions.TypedDict, total=False):
    authFailAction: typing_extensions.Literal[
        "AUTH_FAIL_ACTION_UNSPECIFIED",
        "AUTH_FAIL_ACTION_REDIRECT",
        "AUTH_FAIL_ACTION_UNAUTHORIZED",
    ]
    script: str
    url: str
    login: typing_extensions.Literal[
        "LOGIN_UNSPECIFIED", "LOGIN_OPTIONAL", "LOGIN_ADMIN", "LOGIN_REQUIRED"
    ]
    securityLevel: typing_extensions.Literal[
        "SECURE_UNSPECIFIED",
        "SECURE_DEFAULT",
        "SECURE_NEVER",
        "SECURE_OPTIONAL",
        "SECURE_ALWAYS",
    ]

class RepairApplicationRequest(typing_extensions.TypedDict, total=False): ...

class VpcAccessConnector(typing_extensions.TypedDict, total=False):
    name: str

class ListServicesResponse(typing_extensions.TypedDict, total=False):
    services: typing.List[Service]
    nextPageToken: str

class ScriptHandler(typing_extensions.TypedDict, total=False):
    scriptPath: str

class Resources(typing_extensions.TypedDict, total=False):
    cpu: float
    memoryGb: float
    diskGb: float
    volumes: typing.List[Volume]
    kmsKeyReference: str

class Operation(typing_extensions.TypedDict, total=False):
    response: typing.Dict[str, typing.Any]
    error: Status
    name: str
    done: bool
    metadata: typing.Dict[str, typing.Any]

class NetworkSettings(typing_extensions.TypedDict, total=False):
    ingressTrafficAllowed: typing_extensions.Literal[
        "INGRESS_TRAFFIC_ALLOWED_UNSPECIFIED",
        "INGRESS_TRAFFIC_ALLOWED_ALL",
        "INGRESS_TRAFFIC_ALLOWED_INTERNAL_ONLY",
        "INGRESS_TRAFFIC_ALLOWED_INTERNAL_AND_LB",
    ]

class Empty(typing_extensions.TypedDict, total=False): ...

class UrlDispatchRule(typing_extensions.TypedDict, total=False):
    path: str
    service: str
    domain: str

class Entrypoint(typing_extensions.TypedDict, total=False):
    shell: str

class AuthorizedDomain(typing_extensions.TypedDict, total=False):
    id: str
    name: str

class ContainerInfo(typing_extensions.TypedDict, total=False):
    image: str

class IdentityAwareProxy(typing_extensions.TypedDict, total=False):
    oauth2ClientId: str
    oauth2ClientSecretSha256: str
    enabled: bool
    oauth2ClientSecret: str

class ListIngressRulesResponse(typing_extensions.TypedDict, total=False):
    ingressRules: typing.List[FirewallRule]
    nextPageToken: str

class ReadinessCheck(typing_extensions.TypedDict, total=False):
    host: str
    failureThreshold: int
    path: str
    appStartTimeout: str
    checkInterval: str
    timeout: str
    successThreshold: int

class OperationMetadataV1Beta(typing_extensions.TypedDict, total=False):
    warning: typing.List[str]
    createVersionMetadata: CreateVersionMetadataV1Beta
    insertTime: str
    endTime: str
    target: str
    user: str
    method: str
    ephemeralMessage: str

class CreateVersionMetadataV1(typing_extensions.TypedDict, total=False):
    cloudBuildId: str

class DebugInstanceRequest(typing_extensions.TypedDict, total=False):
    sshKey: str

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

class FeatureSettings(typing_extensions.TypedDict, total=False):
    splitHealthChecks: bool
    useContainerOptimizedOs: bool

class TrafficSplit(typing_extensions.TypedDict, total=False):
    shardBy: typing_extensions.Literal["UNSPECIFIED", "COOKIE", "IP", "RANDOM"]
    allocations: typing.Dict[str, typing.Any]

class BasicScaling(typing_extensions.TypedDict, total=False):
    maxInstances: int
    idleTimeout: str

class OperationMetadataV1(typing_extensions.TypedDict, total=False):
    ephemeralMessage: str
    user: str
    method: str
    endTime: str
    createVersionMetadata: CreateVersionMetadataV1
    warning: typing.List[str]
    insertTime: str
    target: str

class AuthorizedCertificate(typing_extensions.TypedDict, total=False):
    name: str
    certificateRawData: CertificateRawData
    domainNames: typing.List[str]
    expireTime: str
    managedCertificate: ManagedCertificate
    displayName: str
    visibleDomainMappings: typing.List[str]
    domainMappingsCount: int
    id: str

class BatchUpdateIngressRulesResponse(typing_extensions.TypedDict, total=False):
    ingressRules: typing.List[FirewallRule]

class ListAuthorizedDomainsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    domains: typing.List[AuthorizedDomain]

class ManualScaling(typing_extensions.TypedDict, total=False):
    instances: int

class DiskUtilization(typing_extensions.TypedDict, total=False):
    targetWriteOpsPerSecond: int
    targetWriteBytesPerSecond: int
    targetReadBytesPerSecond: int
    targetReadOpsPerSecond: int

class LocationMetadata(typing_extensions.TypedDict, total=False):
    flexibleEnvironmentAvailable: bool
    standardEnvironmentAvailable: bool

class CustomMetric(typing_extensions.TypedDict, total=False):
    singleInstanceAssignment: float
    targetUtilization: float
    targetType: str
    metricName: str
    filter: str

class ListVersionsResponse(typing_extensions.TypedDict, total=False):
    versions: typing.List[Version]
    nextPageToken: str

class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: typing.List[typing.Dict[str, typing.Any]]
    message: str

class OperationMetadataV1Alpha(typing_extensions.TypedDict, total=False):
    user: str
    method: str
    endTime: str
    warning: typing.List[str]
    insertTime: str
    ephemeralMessage: str
    target: str
    createVersionMetadata: CreateVersionMetadataV1Alpha

class ListOperationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    operations: typing.List[Operation]

class CloudBuildOptions(typing_extensions.TypedDict, total=False):
    cloudBuildTimeout: str
    appYamlPath: str

class Location(typing_extensions.TypedDict, total=False):
    locationId: str
    metadata: typing.Dict[str, typing.Any]
    displayName: str
    labels: typing.Dict[str, typing.Any]
    name: str

class Network(typing_extensions.TypedDict, total=False):
    sessionAffinity: bool
    name: str
    forwardedPorts: typing.List[str]
    instanceTag: str
    subnetworkName: str

class SslSettings(typing_extensions.TypedDict, total=False):
    sslManagementType: typing_extensions.Literal["AUTOMATIC", "MANUAL"]
    certificateId: str
    pendingManagedCertificateId: str

class RequestUtilization(typing_extensions.TypedDict, total=False):
    targetConcurrentRequests: int
    targetRequestCountPerSecond: int

class HealthCheck(typing_extensions.TypedDict, total=False):
    timeout: str
    unhealthyThreshold: int
    checkInterval: str
    healthyThreshold: int
    disableHealthCheck: bool
    host: str
    restartThreshold: int

class ListInstancesResponse(typing_extensions.TypedDict, total=False):
    instances: typing.List[Instance]
    nextPageToken: str

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

class ListLocationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    locations: typing.List[Location]

class ApiEndpointHandler(typing_extensions.TypedDict, total=False):
    scriptPath: str

class BuildInfo(typing_extensions.TypedDict, total=False):
    cloudBuildId: str

class NetworkUtilization(typing_extensions.TypedDict, total=False):
    targetReceivedPacketsPerSecond: int
    targetReceivedBytesPerSecond: int
    targetSentPacketsPerSecond: int
    targetSentBytesPerSecond: int

class CertificateRawData(typing_extensions.TypedDict, total=False):
    privateKey: str
    publicCertificate: str

class EndpointsApiService(typing_extensions.TypedDict, total=False):
    name: str
    disableTraceSampling: bool
    rolloutStrategy: typing_extensions.Literal[
        "UNSPECIFIED_ROLLOUT_STRATEGY", "FIXED", "MANAGED"
    ]
    configId: str

class ResourceRecord(typing_extensions.TypedDict, total=False):
    type: typing_extensions.Literal["A", "AAAA", "CNAME"]
    name: str
    rrdata: str

class ListAuthorizedCertificatesResponse(typing_extensions.TypedDict, total=False):
    certificates: typing.List[AuthorizedCertificate]
    nextPageToken: str

class Library(typing_extensions.TypedDict, total=False):
    name: str
    version: str

class ZipInfo(typing_extensions.TypedDict, total=False):
    sourceUrl: str
    filesCount: int

class Deployment(typing_extensions.TypedDict, total=False):
    build: BuildInfo
    cloudBuildOptions: CloudBuildOptions
    files: typing.Dict[str, typing.Any]
    container: ContainerInfo
    zip: ZipInfo

class FirewallRule(typing_extensions.TypedDict, total=False):
    priority: int
    description: str
    sourceRange: str
    action: typing_extensions.Literal["UNSPECIFIED_ACTION", "ALLOW", "DENY"]
