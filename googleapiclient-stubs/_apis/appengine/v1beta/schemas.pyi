import typing

_list = list

@typing.type_check_only
class ApiConfigHandler(typing.TypedDict, total=False):
    authFailAction: typing.Literal[
        "AUTH_FAIL_ACTION_UNSPECIFIED",
        "AUTH_FAIL_ACTION_REDIRECT",
        "AUTH_FAIL_ACTION_UNAUTHORIZED",
    ]
    login: typing.Literal[
        "LOGIN_UNSPECIFIED", "LOGIN_OPTIONAL", "LOGIN_ADMIN", "LOGIN_REQUIRED"
    ]
    script: str
    securityLevel: typing.Literal[
        "SECURE_UNSPECIFIED",
        "SECURE_DEFAULT",
        "SECURE_NEVER",
        "SECURE_OPTIONAL",
        "SECURE_ALWAYS",
    ]
    url: str

@typing.type_check_only
class ApiEndpointHandler(typing.TypedDict, total=False):
    scriptPath: str

@typing.type_check_only
class Application(typing.TypedDict, total=False):
    authDomain: str
    codeBucket: str
    databaseType: typing.Literal[
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
    generatedCustomerMetadata: dict[str, typing.Any]
    iap: IdentityAwareProxy
    id: str
    locationId: str
    name: str
    serviceAccount: str
    servingStatus: typing.Literal[
        "UNSPECIFIED", "SERVING", "USER_DISABLED", "SYSTEM_DISABLED"
    ]
    sslPolicy: typing.Literal["SSL_POLICY_UNSPECIFIED", "DEFAULT", "MODERN"]

@typing.type_check_only
class AuthorizedCertificate(typing.TypedDict, total=False):
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
class AuthorizedDomain(typing.TypedDict, total=False):
    id: str
    name: str

@typing.type_check_only
class AutomaticScaling(typing.TypedDict, total=False):
    coolDownPeriod: str
    cpuUtilization: CpuUtilization
    customMetrics: _list[CustomMetric]
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
class BasicScaling(typing.TypedDict, total=False):
    idleTimeout: str
    maxInstances: int

@typing.type_check_only
class BatchUpdateIngressRulesRequest(typing.TypedDict, total=False):
    ingressRules: _list[FirewallRule]

@typing.type_check_only
class BatchUpdateIngressRulesResponse(typing.TypedDict, total=False):
    ingressRules: _list[FirewallRule]

@typing.type_check_only
class BuildInfo(typing.TypedDict, total=False):
    cloudBuildId: str

@typing.type_check_only
class CertificateRawData(typing.TypedDict, total=False):
    privateKey: str
    publicCertificate: str

@typing.type_check_only
class CloudBuildOptions(typing.TypedDict, total=False):
    appYamlPath: str
    cloudBuildTimeout: str

@typing.type_check_only
class ContainerInfo(typing.TypedDict, total=False):
    image: str

@typing.type_check_only
class ContainerState(typing.TypedDict, total=False):
    currentReasons: Reasons
    previousReasons: Reasons
    state: typing.Literal["UNKNOWN_STATE", "ON", "OFF", "DELETED"]

@typing.type_check_only
class CpuUtilization(typing.TypedDict, total=False):
    aggregationWindowLength: str
    targetUtilization: float

@typing.type_check_only
class CreateVersionMetadataV1(typing.TypedDict, total=False):
    cloudBuildId: str

@typing.type_check_only
class CreateVersionMetadataV1Alpha(typing.TypedDict, total=False):
    cloudBuildId: str

@typing.type_check_only
class CreateVersionMetadataV1Beta(typing.TypedDict, total=False):
    cloudBuildId: str

@typing.type_check_only
class CustomMetric(typing.TypedDict, total=False):
    filter: str
    metricName: str
    singleInstanceAssignment: float
    targetType: str
    targetUtilization: float

@typing.type_check_only
class Date(typing.TypedDict, total=False):
    day: int
    month: int
    year: int

@typing.type_check_only
class DebugInstanceRequest(typing.TypedDict, total=False):
    sshKey: str

@typing.type_check_only
class Deployment(typing.TypedDict, total=False):
    build: BuildInfo
    cloudBuildOptions: CloudBuildOptions
    container: ContainerInfo
    files: dict[str, typing.Any]
    zip: ZipInfo

@typing.type_check_only
class DiskUtilization(typing.TypedDict, total=False):
    targetReadBytesPerSecond: int
    targetReadOpsPerSecond: int
    targetWriteBytesPerSecond: int
    targetWriteOpsPerSecond: int

@typing.type_check_only
class DomainMapping(typing.TypedDict, total=False):
    id: str
    name: str
    resourceRecords: _list[ResourceRecord]
    sslSettings: SslSettings

@typing.type_check_only
class Empty(typing.TypedDict, total=False): ...

@typing.type_check_only
class EndpointsApiService(typing.TypedDict, total=False):
    configId: str
    disableTraceSampling: bool
    name: str
    rolloutStrategy: typing.Literal["UNSPECIFIED_ROLLOUT_STRATEGY", "FIXED", "MANAGED"]

@typing.type_check_only
class Entrypoint(typing.TypedDict, total=False):
    shell: str

@typing.type_check_only
class ErrorHandler(typing.TypedDict, total=False):
    errorCode: typing.Literal[
        "ERROR_CODE_UNSPECIFIED",
        "ERROR_CODE_DEFAULT",
        "ERROR_CODE_OVER_QUOTA",
        "ERROR_CODE_DOS_API_DENIAL",
        "ERROR_CODE_TIMEOUT",
    ]
    mimeType: str
    staticFile: str

@typing.type_check_only
class ExportAppImageRequest(typing.TypedDict, total=False):
    destinationRepository: str

@typing.type_check_only
class FeatureSettings(typing.TypedDict, total=False):
    splitHealthChecks: bool
    useContainerOptimizedOs: bool

@typing.type_check_only
class FileInfo(typing.TypedDict, total=False):
    mimeType: str
    sha1Sum: str
    sourceUrl: str

@typing.type_check_only
class FirewallRule(typing.TypedDict, total=False):
    action: typing.Literal["UNSPECIFIED_ACTION", "ALLOW", "DENY"]
    description: str
    priority: int
    sourceRange: str

@typing.type_check_only
class FlexibleRuntimeSettings(typing.TypedDict, total=False):
    operatingSystem: str
    runtimeVersion: str

@typing.type_check_only
class GceTag(typing.TypedDict, total=False):
    parent: _list[str]
    tag: str

@typing.type_check_only
class GoogleAppengineV1betaLocationMetadata(typing.TypedDict, total=False):
    flexibleEnvironmentAvailable: bool
    searchApiAvailable: bool
    standardEnvironmentAvailable: bool

@typing.type_check_only
class HealthCheck(typing.TypedDict, total=False):
    checkInterval: str
    disableHealthCheck: bool
    healthyThreshold: int
    host: str
    restartThreshold: int
    timeout: str
    unhealthyThreshold: int

@typing.type_check_only
class IdentityAwareProxy(typing.TypedDict, total=False):
    enabled: bool
    oauth2ClientId: str
    oauth2ClientSecret: str
    oauth2ClientSecretSha256: str

@typing.type_check_only
class Instance(typing.TypedDict, total=False):
    appEngineRelease: str
    availability: typing.Literal["UNSPECIFIED", "RESIDENT", "DYNAMIC"]
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
    vmLiveness: typing.Literal[
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
class Library(typing.TypedDict, total=False):
    name: str
    version: str

@typing.type_check_only
class ListAuthorizedCertificatesResponse(typing.TypedDict, total=False):
    certificates: _list[AuthorizedCertificate]
    nextPageToken: str

@typing.type_check_only
class ListAuthorizedDomainsResponse(typing.TypedDict, total=False):
    domains: _list[AuthorizedDomain]
    nextPageToken: str

@typing.type_check_only
class ListDomainMappingsResponse(typing.TypedDict, total=False):
    domainMappings: _list[DomainMapping]
    nextPageToken: str

@typing.type_check_only
class ListIngressRulesResponse(typing.TypedDict, total=False):
    ingressRules: _list[FirewallRule]
    nextPageToken: str

@typing.type_check_only
class ListInstancesResponse(typing.TypedDict, total=False):
    instances: _list[Instance]
    nextPageToken: str

@typing.type_check_only
class ListLocationsResponse(typing.TypedDict, total=False):
    locations: _list[Location]
    nextPageToken: str

@typing.type_check_only
class ListOperationsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    operations: _list[Operation]
    unreachable: _list[str]

@typing.type_check_only
class ListRuntimesResponse(typing.TypedDict, total=False):
    nextPageToken: str
    runtimes: _list[Runtime]

@typing.type_check_only
class ListServicesResponse(typing.TypedDict, total=False):
    nextPageToken: str
    services: _list[Service]

@typing.type_check_only
class ListVersionsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    versions: _list[Version]

@typing.type_check_only
class LivenessCheck(typing.TypedDict, total=False):
    checkInterval: str
    failureThreshold: int
    host: str
    initialDelay: str
    path: str
    successThreshold: int
    timeout: str

@typing.type_check_only
class Location(typing.TypedDict, total=False):
    displayName: str
    labels: dict[str, typing.Any]
    locationId: str
    metadata: dict[str, typing.Any]
    name: str

@typing.type_check_only
class LocationMetadata(typing.TypedDict, total=False):
    flexibleEnvironmentAvailable: bool
    searchApiAvailable: bool
    standardEnvironmentAvailable: bool

@typing.type_check_only
class ManagedCertificate(typing.TypedDict, total=False):
    lastRenewalTime: str
    status: typing.Literal[
        "MANAGEMENT_STATUS_UNSPECIFIED",
        "OK",
        "PENDING",
        "FAILED_RETRYING_NOT_VISIBLE",
        "FAILED_PERMANENT",
        "FAILED_RETRYING_CAA_FORBIDDEN",
        "FAILED_RETRYING_CAA_CHECKING",
    ]

@typing.type_check_only
class ManualScaling(typing.TypedDict, total=False):
    instances: int

@typing.type_check_only
class Network(typing.TypedDict, total=False):
    forwardedPorts: _list[str]
    instanceIpMode: typing.Literal[
        "INSTANCE_IP_MODE_UNSPECIFIED", "EXTERNAL", "INTERNAL"
    ]
    instanceTag: str
    name: str
    sessionAffinity: bool
    subnetworkName: str

@typing.type_check_only
class NetworkSettings(typing.TypedDict, total=False):
    ingressTrafficAllowed: typing.Literal[
        "INGRESS_TRAFFIC_ALLOWED_UNSPECIFIED",
        "INGRESS_TRAFFIC_ALLOWED_ALL",
        "INGRESS_TRAFFIC_ALLOWED_INTERNAL_ONLY",
        "INGRESS_TRAFFIC_ALLOWED_INTERNAL_AND_LB",
    ]

@typing.type_check_only
class NetworkUtilization(typing.TypedDict, total=False):
    targetReceivedBytesPerSecond: int
    targetReceivedPacketsPerSecond: int
    targetSentBytesPerSecond: int
    targetSentPacketsPerSecond: int

@typing.type_check_only
class Operation(typing.TypedDict, total=False):
    done: bool
    error: Status
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class OperationMetadataV1(typing.TypedDict, total=False):
    createVersionMetadata: CreateVersionMetadataV1
    endTime: str
    ephemeralMessage: str
    insertTime: str
    method: str
    target: str
    user: str
    warning: _list[str]

@typing.type_check_only
class OperationMetadataV1Alpha(typing.TypedDict, total=False):
    createVersionMetadata: CreateVersionMetadataV1Alpha
    endTime: str
    ephemeralMessage: str
    insertTime: str
    method: str
    target: str
    user: str
    warning: _list[str]

@typing.type_check_only
class OperationMetadataV1Beta(typing.TypedDict, total=False):
    createVersionMetadata: CreateVersionMetadataV1Beta
    endTime: str
    ephemeralMessage: str
    insertTime: str
    method: str
    target: str
    user: str
    warning: _list[str]

@typing.type_check_only
class ProjectEvent(typing.TypedDict, total=False):
    eventId: str
    phase: typing.Literal[
        "CONTAINER_EVENT_PHASE_UNSPECIFIED",
        "BEFORE_RESOURCE_HANDLING",
        "AFTER_RESOURCE_HANDLING",
    ]
    projectMetadata: ProjectsMetadata
    state: ContainerState

@typing.type_check_only
class ProjectsMetadata(typing.TypedDict, total=False):
    consumerProjectId: str
    consumerProjectNumber: str
    consumerProjectState: typing.Literal["UNKNOWN_STATE", "ON", "OFF", "DELETED"]
    gceTag: _list[GceTag]
    isGceProjectDeprovisioning: bool
    p4ServiceAccount: str
    producerProjectId: str
    producerProjectNumber: str
    tenantProjectId: str
    tenantProjectNumber: str

@typing.type_check_only
class ReadinessCheck(typing.TypedDict, total=False):
    appStartTimeout: str
    checkInterval: str
    failureThreshold: int
    host: str
    path: str
    successThreshold: int
    timeout: str

@typing.type_check_only
class Reasons(typing.TypedDict, total=False):
    abuse: typing.Literal[
        "ABUSE_UNKNOWN_REASON", "ABUSE_CONTROL_PLANE_SYNC", "SUSPEND", "REINSTATE"
    ]
    billing: typing.Literal[
        "BILLING_UNKNOWN_REASON",
        "BILLING_CONTROL_PLANE_SYNC",
        "PROBATION",
        "CLOSE",
        "OPEN",
    ]
    dataGovernance: typing.Literal[
        "DATA_GOVERNANCE_UNKNOWN_REASON",
        "DATA_GOVERNANCE_CONTROL_PLANE_SYNC",
        "HIDE",
        "UNHIDE",
        "PURGE",
    ]
    serviceActivation: typing.Literal[
        "SERVICE_ACTIVATION_STATUS_UNSPECIFIED",
        "SERVICE_ACTIVATION_ENABLED",
        "SERVICE_ACTIVATION_DISABLED",
        "SERVICE_ACTIVATION_DISABLED_FULL",
        "SERVICE_ACTIVATION_UNKNOWN_REASON",
    ]
    serviceManagement: typing.Literal[
        "SERVICE_MANAGEMENT_UNKNOWN_REASON",
        "SERVICE_MANAGEMENT_CONTROL_PLANE_SYNC",
        "ACTIVATION",
        "PREPARE_DEACTIVATION",
        "ABORT_DEACTIVATION",
        "COMMIT_DEACTIVATION",
    ]

@typing.type_check_only
class RepairApplicationRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class RequestUtilization(typing.TypedDict, total=False):
    targetConcurrentRequests: int
    targetRequestCountPerSecond: int

@typing.type_check_only
class ResourceEvent(typing.TypedDict, total=False):
    eventId: str
    name: str
    state: ContainerState

@typing.type_check_only
class ResourceRecord(typing.TypedDict, total=False):
    name: str
    rrdata: str
    type: typing.Literal["A", "AAAA", "CNAME"]

@typing.type_check_only
class Resources(typing.TypedDict, total=False):
    cpu: float
    diskGb: float
    kmsKeyReference: str
    memoryGb: float
    volumes: _list[Volume]

@typing.type_check_only
class Runtime(typing.TypedDict, total=False):
    decommissionedDate: Date
    deprecationDate: Date
    displayName: str
    endOfSupportDate: Date
    environment: typing.Literal["ENVIRONMENT_UNSPECIFIED", "STANDARD", "FLEXIBLE"]
    name: str
    stage: typing.Literal[
        "RUNTIME_STAGE_UNSPECIFIED",
        "DEVELOPMENT",
        "ALPHA",
        "BETA",
        "GA",
        "DEPRECATED",
        "DECOMMISSIONED",
        "END_OF_SUPPORT",
    ]
    supportedOperatingSystems: _list[str]
    warnings: _list[str]

@typing.type_check_only
class ScriptHandler(typing.TypedDict, total=False):
    scriptPath: str

@typing.type_check_only
class Service(typing.TypedDict, total=False):
    generatedCustomerMetadata: dict[str, typing.Any]
    id: str
    labels: dict[str, typing.Any]
    name: str
    networkSettings: NetworkSettings
    split: TrafficSplit

@typing.type_check_only
class SslSettings(typing.TypedDict, total=False):
    certificateId: str
    pendingManagedCertificateId: str
    sslManagementType: typing.Literal["AUTOMATIC", "MANUAL"]

@typing.type_check_only
class StandardSchedulerSettings(typing.TypedDict, total=False):
    maxInstances: int
    minInstances: int
    targetCpuUtilization: float
    targetThroughputUtilization: float

@typing.type_check_only
class StaticFilesHandler(typing.TypedDict, total=False):
    applicationReadable: bool
    expiration: str
    httpHeaders: dict[str, typing.Any]
    mimeType: str
    path: str
    requireMatchingFile: bool
    uploadPathRegex: str

@typing.type_check_only
class Status(typing.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class TrafficSplit(typing.TypedDict, total=False):
    allocations: dict[str, typing.Any]
    shardBy: typing.Literal["UNSPECIFIED", "COOKIE", "IP", "RANDOM"]

@typing.type_check_only
class UrlDispatchRule(typing.TypedDict, total=False):
    domain: str
    path: str
    service: str

@typing.type_check_only
class UrlMap(typing.TypedDict, total=False):
    apiEndpoint: ApiEndpointHandler
    authFailAction: typing.Literal[
        "AUTH_FAIL_ACTION_UNSPECIFIED",
        "AUTH_FAIL_ACTION_REDIRECT",
        "AUTH_FAIL_ACTION_UNAUTHORIZED",
    ]
    login: typing.Literal[
        "LOGIN_UNSPECIFIED", "LOGIN_OPTIONAL", "LOGIN_ADMIN", "LOGIN_REQUIRED"
    ]
    redirectHttpResponseCode: typing.Literal[
        "REDIRECT_HTTP_RESPONSE_CODE_UNSPECIFIED",
        "REDIRECT_HTTP_RESPONSE_CODE_301",
        "REDIRECT_HTTP_RESPONSE_CODE_302",
        "REDIRECT_HTTP_RESPONSE_CODE_303",
        "REDIRECT_HTTP_RESPONSE_CODE_307",
    ]
    script: ScriptHandler
    securityLevel: typing.Literal[
        "SECURE_UNSPECIFIED",
        "SECURE_DEFAULT",
        "SECURE_NEVER",
        "SECURE_OPTIONAL",
        "SECURE_ALWAYS",
    ]
    staticFiles: StaticFilesHandler
    urlRegex: str

@typing.type_check_only
class Version(typing.TypedDict, total=False):
    apiConfig: ApiConfigHandler
    appEngineApis: bool
    appEngineBundledServices: _list[
        typing.Literal[
            "BUNDLED_SERVICE_TYPE_UNSPECIFIED",
            "BUNDLED_SERVICE_TYPE_APP_IDENTITY_SERVICE",
            "BUNDLED_SERVICE_TYPE_BLOBSTORE",
            "BUNDLED_SERVICE_TYPE_CAPABILITY_SERVICE",
            "BUNDLED_SERVICE_TYPE_DATASTORE_V3",
            "BUNDLED_SERVICE_TYPE_DEFERRED",
            "BUNDLED_SERVICE_TYPE_IMAGES",
            "BUNDLED_SERVICE_TYPE_MAIL",
            "BUNDLED_SERVICE_TYPE_MEMCACHE",
            "BUNDLED_SERVICE_TYPE_MODULES",
            "BUNDLED_SERVICE_TYPE_NAMESPACES",
            "BUNDLED_SERVICE_TYPE_NDB",
            "BUNDLED_SERVICE_TYPE_SEARCH",
            "BUNDLED_SERVICE_TYPE_TASKQUEUES",
            "BUNDLED_SERVICE_TYPE_URLFETCH",
            "BUNDLED_SERVICE_TYPE_USERS",
        ]
    ]
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
    flexibleRuntimeSettings: FlexibleRuntimeSettings
    generatedCustomerMetadata: dict[str, typing.Any]
    handlers: _list[UrlMap]
    healthCheck: HealthCheck
    id: str
    inboundServices: _list[
        typing.Literal[
            "INBOUND_SERVICE_UNSPECIFIED",
            "INBOUND_SERVICE_MAIL",
            "INBOUND_SERVICE_MAIL_BOUNCE",
            "INBOUND_SERVICE_XMPP_ERROR",
            "INBOUND_SERVICE_XMPP_MESSAGE",
            "INBOUND_SERVICE_XMPP_SUBSCRIBE",
            "INBOUND_SERVICE_XMPP_PRESENCE",
            "INBOUND_SERVICE_CHANNEL_PRESENCE",
            "INBOUND_SERVICE_WARMUP",
        ]
    ]
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
    servingStatus: typing.Literal["SERVING_STATUS_UNSPECIFIED", "SERVING", "STOPPED"]
    threadsafe: bool
    versionUrl: str
    vm: bool
    vpcAccess: VpcAccess
    vpcAccessConnector: VpcAccessConnector
    zones: _list[str]

@typing.type_check_only
class Volume(typing.TypedDict, total=False):
    name: str
    sizeGb: float
    volumeType: str

@typing.type_check_only
class VpcAccess(typing.TypedDict, total=False):
    networkInterfaces: _list[VpcNetworkInterface]
    vpcEgress: typing.Literal[
        "VPC_EGRESS_UNSPECIFIED", "ALL_TRAFFIC", "PRIVATE_IP_RANGES"
    ]

@typing.type_check_only
class VpcAccessConnector(typing.TypedDict, total=False):
    egressSetting: typing.Literal[
        "EGRESS_SETTING_UNSPECIFIED", "ALL_TRAFFIC", "PRIVATE_IP_RANGES"
    ]
    name: str

@typing.type_check_only
class VpcNetworkInterface(typing.TypedDict, total=False):
    network: str
    subnet: str
    tags: _list[str]

@typing.type_check_only
class ZipInfo(typing.TypedDict, total=False):
    filesCount: int
    sourceUrl: str
