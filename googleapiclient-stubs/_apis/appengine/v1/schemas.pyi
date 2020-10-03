import typing

import typing_extensions

class Service(typing_extensions.TypedDict, total=False):
    split: TrafficSplit
    name: str
    networkSettings: NetworkSettings
    id: str

class TrafficSplit(typing_extensions.TypedDict, total=False):
    shardBy: typing_extensions.Literal["UNSPECIFIED", "COOKIE", "IP", "RANDOM"]
    allocations: typing.Dict[str, typing.Any]

class Location(typing_extensions.TypedDict, total=False):
    labels: typing.Dict[str, typing.Any]
    name: str
    locationId: str
    displayName: str
    metadata: typing.Dict[str, typing.Any]

class ManualScaling(typing_extensions.TypedDict, total=False):
    instances: int

class ErrorHandler(typing_extensions.TypedDict, total=False):
    mimeType: str
    staticFile: str
    errorCode: typing_extensions.Literal[
        "ERROR_CODE_UNSPECIFIED",
        "ERROR_CODE_DEFAULT",
        "ERROR_CODE_OVER_QUOTA",
        "ERROR_CODE_DOS_API_DENIAL",
        "ERROR_CODE_TIMEOUT",
    ]

class DebugInstanceRequest(typing_extensions.TypedDict, total=False):
    sshKey: str

class Network(typing_extensions.TypedDict, total=False):
    forwardedPorts: typing.List[str]
    subnetworkName: str
    instanceTag: str
    sessionAffinity: bool
    name: str

class StandardSchedulerSettings(typing_extensions.TypedDict, total=False):
    targetThroughputUtilization: float
    minInstances: int
    targetCpuUtilization: float
    maxInstances: int

class ListAuthorizedDomainsResponse(typing_extensions.TypedDict, total=False):
    domains: typing.List[AuthorizedDomain]
    nextPageToken: str

class SslSettings(typing_extensions.TypedDict, total=False):
    pendingManagedCertificateId: str
    certificateId: str
    sslManagementType: typing_extensions.Literal[
        "SSL_MANAGEMENT_TYPE_UNSPECIFIED", "AUTOMATIC", "MANUAL"
    ]

class Deployment(typing_extensions.TypedDict, total=False):
    cloudBuildOptions: CloudBuildOptions
    container: ContainerInfo
    files: typing.Dict[str, typing.Any]
    zip: ZipInfo

class CreateVersionMetadataV1(typing_extensions.TypedDict, total=False):
    cloudBuildId: str

class ListServicesResponse(typing_extensions.TypedDict, total=False):
    services: typing.List[Service]
    nextPageToken: str

class StaticFilesHandler(typing_extensions.TypedDict, total=False):
    expiration: str
    uploadPathRegex: str
    requireMatchingFile: bool
    httpHeaders: typing.Dict[str, typing.Any]
    path: str
    mimeType: str
    applicationReadable: bool

class Library(typing_extensions.TypedDict, total=False):
    name: str
    version: str

class LivenessCheck(typing_extensions.TypedDict, total=False):
    timeout: str
    checkInterval: str
    path: str
    host: str
    initialDelay: str
    failureThreshold: int
    successThreshold: int

class CertificateRawData(typing_extensions.TypedDict, total=False):
    publicCertificate: str
    privateKey: str

class Volume(typing_extensions.TypedDict, total=False):
    volumeType: str
    name: str
    sizeGb: float

class HealthCheck(typing_extensions.TypedDict, total=False):
    checkInterval: str
    restartThreshold: int
    unhealthyThreshold: int
    host: str
    healthyThreshold: int
    disableHealthCheck: bool
    timeout: str

class OperationMetadataV1(typing_extensions.TypedDict, total=False):
    method: str
    warning: typing.List[str]
    createVersionMetadata: CreateVersionMetadataV1
    insertTime: str
    endTime: str
    user: str
    target: str
    ephemeralMessage: str

class RepairApplicationRequest(typing_extensions.TypedDict, total=False): ...

class CpuUtilization(typing_extensions.TypedDict, total=False):
    targetUtilization: float
    aggregationWindowLength: str

class AuthorizedDomain(typing_extensions.TypedDict, total=False):
    id: str
    name: str

class AutomaticScaling(typing_extensions.TypedDict, total=False):
    minPendingLatency: str
    diskUtilization: DiskUtilization
    coolDownPeriod: str
    networkUtilization: NetworkUtilization
    minIdleInstances: int
    maxTotalInstances: int
    requestUtilization: RequestUtilization
    cpuUtilization: CpuUtilization
    maxConcurrentRequests: int
    standardSchedulerSettings: StandardSchedulerSettings
    minTotalInstances: int
    maxIdleInstances: int
    maxPendingLatency: str

class ScriptHandler(typing_extensions.TypedDict, total=False):
    scriptPath: str

class ApiEndpointHandler(typing_extensions.TypedDict, total=False):
    scriptPath: str

class DiskUtilization(typing_extensions.TypedDict, total=False):
    targetReadOpsPerSecond: int
    targetReadBytesPerSecond: int
    targetWriteBytesPerSecond: int
    targetWriteOpsPerSecond: int

class AuthorizedCertificate(typing_extensions.TypedDict, total=False):
    expireTime: str
    id: str
    visibleDomainMappings: typing.List[str]
    domainNames: typing.List[str]
    certificateRawData: CertificateRawData
    displayName: str
    name: str
    domainMappingsCount: int
    managedCertificate: ManagedCertificate

class UrlDispatchRule(typing_extensions.TypedDict, total=False):
    domain: str
    path: str
    service: str

class BasicScaling(typing_extensions.TypedDict, total=False):
    maxInstances: int
    idleTimeout: str

class FirewallRule(typing_extensions.TypedDict, total=False):
    action: typing_extensions.Literal["UNSPECIFIED_ACTION", "ALLOW", "DENY"]
    sourceRange: str
    description: str
    priority: int

class EndpointsApiService(typing_extensions.TypedDict, total=False):
    configId: str
    disableTraceSampling: bool
    name: str
    rolloutStrategy: typing_extensions.Literal[
        "UNSPECIFIED_ROLLOUT_STRATEGY", "FIXED", "MANAGED"
    ]

class UrlMap(typing_extensions.TypedDict, total=False):
    securityLevel: typing_extensions.Literal[
        "SECURE_UNSPECIFIED",
        "SECURE_DEFAULT",
        "SECURE_NEVER",
        "SECURE_OPTIONAL",
        "SECURE_ALWAYS",
    ]
    redirectHttpResponseCode: typing_extensions.Literal[
        "REDIRECT_HTTP_RESPONSE_CODE_UNSPECIFIED",
        "REDIRECT_HTTP_RESPONSE_CODE_301",
        "REDIRECT_HTTP_RESPONSE_CODE_302",
        "REDIRECT_HTTP_RESPONSE_CODE_303",
        "REDIRECT_HTTP_RESPONSE_CODE_307",
    ]
    login: typing_extensions.Literal[
        "LOGIN_UNSPECIFIED", "LOGIN_OPTIONAL", "LOGIN_ADMIN", "LOGIN_REQUIRED"
    ]
    script: ScriptHandler
    staticFiles: StaticFilesHandler
    authFailAction: typing_extensions.Literal[
        "AUTH_FAIL_ACTION_UNSPECIFIED",
        "AUTH_FAIL_ACTION_REDIRECT",
        "AUTH_FAIL_ACTION_UNAUTHORIZED",
    ]
    apiEndpoint: ApiEndpointHandler
    urlRegex: str

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

class CreateVersionMetadataV1Alpha(typing_extensions.TypedDict, total=False):
    cloudBuildId: str

class IdentityAwareProxy(typing_extensions.TypedDict, total=False):
    oauth2ClientId: str
    oauth2ClientSecretSha256: str
    oauth2ClientSecret: str
    enabled: bool

class ZipInfo(typing_extensions.TypedDict, total=False):
    filesCount: int
    sourceUrl: str

class VpcAccessConnector(typing_extensions.TypedDict, total=False):
    name: str

class Empty(typing_extensions.TypedDict, total=False): ...

class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: typing.List[typing.Dict[str, typing.Any]]
    message: str

class CloudBuildOptions(typing_extensions.TypedDict, total=False):
    cloudBuildTimeout: str
    appYamlPath: str

class OperationMetadataV1Alpha(typing_extensions.TypedDict, total=False):
    user: str
    ephemeralMessage: str
    target: str
    endTime: str
    method: str
    createVersionMetadata: CreateVersionMetadataV1Alpha
    warning: typing.List[str]
    insertTime: str

class ListDomainMappingsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    domainMappings: typing.List[DomainMapping]

class FeatureSettings(typing_extensions.TypedDict, total=False):
    useContainerOptimizedOs: bool
    splitHealthChecks: bool

class LocationMetadata(typing_extensions.TypedDict, total=False):
    flexibleEnvironmentAvailable: bool
    standardEnvironmentAvailable: bool

class ListVersionsResponse(typing_extensions.TypedDict, total=False):
    versions: typing.List[Version]
    nextPageToken: str

class Application(typing_extensions.TypedDict, total=False):
    featureSettings: FeatureSettings
    servingStatus: typing_extensions.Literal[
        "UNSPECIFIED", "SERVING", "USER_DISABLED", "SYSTEM_DISABLED"
    ]
    defaultHostname: str
    defaultBucket: str
    name: str
    locationId: str
    codeBucket: str
    defaultCookieExpiration: str
    gcrDomain: str
    authDomain: str
    databaseType: typing_extensions.Literal[
        "DATABASE_TYPE_UNSPECIFIED",
        "CLOUD_DATASTORE",
        "CLOUD_FIRESTORE",
        "CLOUD_DATASTORE_COMPATIBILITY",
    ]
    id: str
    dispatchRules: typing.List[UrlDispatchRule]
    iap: IdentityAwareProxy

class ResourceRecord(typing_extensions.TypedDict, total=False):
    name: str
    rrdata: str
    type: typing_extensions.Literal["RECORD_TYPE_UNSPECIFIED", "A", "AAAA", "CNAME"]

class CreateVersionMetadataV1Beta(typing_extensions.TypedDict, total=False):
    cloudBuildId: str

class ListAuthorizedCertificatesResponse(typing_extensions.TypedDict, total=False):
    certificates: typing.List[AuthorizedCertificate]
    nextPageToken: str

class Resources(typing_extensions.TypedDict, total=False):
    memoryGb: float
    cpu: float
    diskGb: float
    volumes: typing.List[Volume]
    kmsKeyReference: str

class DomainMapping(typing_extensions.TypedDict, total=False):
    id: str
    sslSettings: SslSettings
    name: str
    resourceRecords: typing.List[ResourceRecord]

class OperationMetadataV1Beta(typing_extensions.TypedDict, total=False):
    ephemeralMessage: str
    createVersionMetadata: CreateVersionMetadataV1Beta
    user: str
    warning: typing.List[str]
    method: str
    target: str
    endTime: str
    insertTime: str

class Version(typing_extensions.TypedDict, total=False):
    envVariables: typing.Dict[str, typing.Any]
    env: str
    runtimeApiVersion: str
    betaSettings: typing.Dict[str, typing.Any]
    entrypoint: Entrypoint
    instanceClass: str
    createTime: str
    servingStatus: typing_extensions.Literal[
        "SERVING_STATUS_UNSPECIFIED", "SERVING", "STOPPED"
    ]
    inboundServices: typing.List[str]
    endpointsApiService: EndpointsApiService
    id: str
    resources: Resources
    runtime: str
    manualScaling: ManualScaling
    readinessCheck: ReadinessCheck
    createdBy: str
    name: str
    livenessCheck: LivenessCheck
    basicScaling: BasicScaling
    apiConfig: ApiConfigHandler
    threadsafe: bool
    buildEnvVariables: typing.Dict[str, typing.Any]
    diskUsageBytes: str
    defaultExpiration: str
    runtimeChannel: str
    deployment: Deployment
    runtimeMainExecutablePath: str
    automaticScaling: AutomaticScaling
    handlers: typing.List[UrlMap]
    libraries: typing.List[Library]
    nobuildFilesRegex: str
    network: Network
    versionUrl: str
    errorHandlers: typing.List[ErrorHandler]
    vpcAccessConnector: VpcAccessConnector
    vm: bool
    healthCheck: HealthCheck
    zones: typing.List[str]

class NetworkUtilization(typing_extensions.TypedDict, total=False):
    targetReceivedPacketsPerSecond: int
    targetSentBytesPerSecond: int
    targetReceivedBytesPerSecond: int
    targetSentPacketsPerSecond: int

class Operation(typing_extensions.TypedDict, total=False):
    done: bool
    error: Status
    metadata: typing.Dict[str, typing.Any]
    response: typing.Dict[str, typing.Any]
    name: str

class NetworkSettings(typing_extensions.TypedDict, total=False):
    ingressTrafficAllowed: typing_extensions.Literal[
        "INGRESS_TRAFFIC_ALLOWED_UNSPECIFIED",
        "INGRESS_TRAFFIC_ALLOWED_ALL",
        "INGRESS_TRAFFIC_ALLOWED_INTERNAL_ONLY",
        "INGRESS_TRAFFIC_ALLOWED_INTERNAL_AND_LB",
    ]

class ContainerInfo(typing_extensions.TypedDict, total=False):
    image: str

class ListLocationsResponse(typing_extensions.TypedDict, total=False):
    locations: typing.List[Location]
    nextPageToken: str

class ListInstancesResponse(typing_extensions.TypedDict, total=False):
    instances: typing.List[Instance]
    nextPageToken: str

class Instance(typing_extensions.TypedDict, total=False):
    startTime: str
    vmId: str
    id: str
    requests: int
    vmName: str
    errors: int
    qps: float
    appEngineRelease: str
    vmDebugEnabled: bool
    name: str
    vmStatus: str
    averageLatency: int
    vmZoneName: str
    availability: typing_extensions.Literal["UNSPECIFIED", "RESIDENT", "DYNAMIC"]
    vmIp: str
    memoryUsage: str

class ListOperationsResponse(typing_extensions.TypedDict, total=False):
    operations: typing.List[Operation]
    nextPageToken: str

class ReadinessCheck(typing_extensions.TypedDict, total=False):
    host: str
    appStartTimeout: str
    successThreshold: int
    checkInterval: str
    path: str
    timeout: str
    failureThreshold: int

class Entrypoint(typing_extensions.TypedDict, total=False):
    shell: str

class BatchUpdateIngressRulesResponse(typing_extensions.TypedDict, total=False):
    ingressRules: typing.List[FirewallRule]

class ListIngressRulesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    ingressRules: typing.List[FirewallRule]

class BatchUpdateIngressRulesRequest(typing_extensions.TypedDict, total=False):
    ingressRules: typing.List[FirewallRule]

class RequestUtilization(typing_extensions.TypedDict, total=False):
    targetConcurrentRequests: int
    targetRequestCountPerSecond: int

class FileInfo(typing_extensions.TypedDict, total=False):
    sha1Sum: str
    mimeType: str
    sourceUrl: str

class ApiConfigHandler(typing_extensions.TypedDict, total=False):
    authFailAction: typing_extensions.Literal[
        "AUTH_FAIL_ACTION_UNSPECIFIED",
        "AUTH_FAIL_ACTION_REDIRECT",
        "AUTH_FAIL_ACTION_UNAUTHORIZED",
    ]
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
    script: str
    url: str
