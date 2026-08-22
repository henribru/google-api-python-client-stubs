import typing

_list = list

@typing.type_check_only
class Access(typing.TypedDict, total=False):
    callerIp: str
    callerIpGeo: Geolocation
    methodName: str
    principalEmail: str
    principalSubject: str
    serviceAccountDelegationInfo: _list[ServiceAccountDelegationInfo]
    serviceAccountKeyName: str
    serviceName: str
    userAgent: str
    userAgentFamily: str
    userName: str

@typing.type_check_only
class AccessReview(typing.TypedDict, total=False):
    group: str
    name: str
    ns: str
    resource: str
    subresource: str
    verb: str
    version: str

@typing.type_check_only
class AdaptiveProtection(typing.TypedDict, total=False):
    confidence: float

@typing.type_check_only
class AdcApplication(typing.TypedDict, total=False):
    attributes: GoogleCloudSecuritycenterV1ResourceApplicationAttributes
    name: str

@typing.type_check_only
class AdcApplicationTemplateRevision(typing.TypedDict, total=False):
    name: str

@typing.type_check_only
class AdcSharedTemplateRevision(typing.TypedDict, total=False):
    name: str

@typing.type_check_only
class AffectedResources(typing.TypedDict, total=False):
    count: str

@typing.type_check_only
class Agent(typing.TypedDict, total=False):
    displayName: str
    id: str

@typing.type_check_only
class AgentAnomaly(typing.TypedDict, total=False):
    confidenceScore: float
    detectorReferences: _list[DetectorReference]
    invocationReferences: _list[InvocationReference]

@typing.type_check_only
class AgentDataAccessEvent(typing.TypedDict, total=False):
    eventId: str
    eventTime: str
    operation: typing.Literal["OPERATION_UNSPECIFIED", "READ", "MOVE", "COPY"]
    principalSubject: str

@typing.type_check_only
class AgentSession(typing.TypedDict, total=False):
    sessionId: str

@typing.type_check_only
class AiModel(typing.TypedDict, total=False):
    deploymentPlatform: typing.Literal[
        "DEPLOYMENT_PLATFORM_UNSPECIFIED", "VERTEX_AI", "GKE", "GCE", "FINE_TUNED_MODEL"
    ]
    displayName: str
    domain: str
    library: str
    location: str
    name: str
    publisher: str
    usageCategory: str

@typing.type_check_only
class Allowed(typing.TypedDict, total=False):
    ipRules: _list[IpRule]

@typing.type_check_only
class Application(typing.TypedDict, total=False):
    baseUri: str
    fullUri: str

@typing.type_check_only
class ArtifactGuardPolicies(typing.TypedDict, total=False):
    failingPolicies: _list[ArtifactGuardPolicy]
    resourceId: str

@typing.type_check_only
class ArtifactGuardPolicy(typing.TypedDict, total=False):
    failureReason: str
    policyId: str
    type: typing.Literal["ARTIFACT_GUARD_POLICY_TYPE_UNSPECIFIED", "VULNERABILITY"]

@typing.type_check_only
class Asset(typing.TypedDict, total=False):
    createTime: str
    name: str
    resourceProperties: dict[str, typing.Any]
    securityCenterProperties: SecurityCenterProperties
    securityMarks: GoogleCloudSecuritycenterV1beta1SecurityMarks
    updateTime: str

@typing.type_check_only
class AssetDiscoveryConfig(typing.TypedDict, total=False):
    inclusionMode: typing.Literal[
        "INCLUSION_MODE_UNSPECIFIED", "INCLUDE_ONLY", "EXCLUDE"
    ]
    projectIds: _list[str]

@typing.type_check_only
class Attack(typing.TypedDict, total=False):
    classification: str
    volumeBps: int
    volumeBpsLong: str
    volumePps: int
    volumePpsLong: str

@typing.type_check_only
class AttackExposure(typing.TypedDict, total=False):
    attackExposureResult: str
    exposedHighValueResourcesCount: int
    exposedLowValueResourcesCount: int
    exposedMediumValueResourcesCount: int
    latestCalculationTime: str
    score: float
    state: typing.Literal["STATE_UNSPECIFIED", "CALCULATED", "NOT_CALCULATED"]

@typing.type_check_only
class AuditConfig(typing.TypedDict, total=False):
    auditLogConfigs: _list[AuditLogConfig]
    service: str

@typing.type_check_only
class AuditLogConfig(typing.TypedDict, total=False):
    exemptedMembers: _list[str]
    logType: typing.Literal[
        "LOG_TYPE_UNSPECIFIED", "ADMIN_READ", "DATA_WRITE", "DATA_READ"
    ]

@typing.type_check_only
class AwsAccount(typing.TypedDict, total=False):
    id: str
    name: str

@typing.type_check_only
class AwsMetadata(typing.TypedDict, total=False):
    account: AwsAccount
    organization: AwsOrganization
    organizationalUnits: _list[AwsOrganizationalUnit]

@typing.type_check_only
class AwsOrganization(typing.TypedDict, total=False):
    id: str

@typing.type_check_only
class AwsOrganizationalUnit(typing.TypedDict, total=False):
    id: str
    name: str

@typing.type_check_only
class AzureManagementGroup(typing.TypedDict, total=False):
    displayName: str
    id: str

@typing.type_check_only
class AzureMetadata(typing.TypedDict, total=False):
    managementGroups: _list[AzureManagementGroup]
    resourceGroup: AzureResourceGroup
    subscription: AzureSubscription
    tenant: AzureTenant

@typing.type_check_only
class AzureResourceGroup(typing.TypedDict, total=False):
    id: str
    name: str

@typing.type_check_only
class AzureSubscription(typing.TypedDict, total=False):
    displayName: str
    id: str

@typing.type_check_only
class AzureTenant(typing.TypedDict, total=False):
    displayName: str
    id: str

@typing.type_check_only
class BackupDisasterRecovery(typing.TypedDict, total=False):
    appliance: str
    applications: _list[str]
    backupCreateTime: str
    backupTemplate: str
    backupType: str
    host: str
    policies: _list[str]
    policyOptions: _list[str]
    profile: str
    storagePool: str

@typing.type_check_only
class BigQueryDestination(typing.TypedDict, total=False):
    dataset: str

@typing.type_check_only
class Binding(typing.TypedDict, total=False):
    condition: Expr
    members: _list[str]
    role: str

@typing.type_check_only
class CancelOperationRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class Chokepoint(typing.TypedDict, total=False):
    relatedFindings: _list[str]

@typing.type_check_only
class CloudArmor(typing.TypedDict, total=False):
    adaptiveProtection: AdaptiveProtection
    attack: Attack
    duration: str
    requests: Requests
    securityPolicy: SecurityPolicy
    threatVector: str

@typing.type_check_only
class CloudControl(typing.TypedDict, total=False):
    cloudControlName: str
    policyType: str
    type: typing.Literal["CLOUD_CONTROL_TYPE_UNSPECIFIED", "BUILT_IN", "CUSTOM"]
    version: int

@typing.type_check_only
class CloudDlpDataProfile(typing.TypedDict, total=False):
    dataProfile: str
    infoTypes: _list[InfoType]
    parentType: typing.Literal["PARENT_TYPE_UNSPECIFIED", "ORGANIZATION", "PROJECT"]

@typing.type_check_only
class CloudDlpInspection(typing.TypedDict, total=False):
    fullScan: bool
    infoType: str
    infoTypeCount: str
    inspectJob: str

@typing.type_check_only
class CloudLoggingEntry(typing.TypedDict, total=False):
    insertId: str
    logId: str
    resourceContainer: str
    timestamp: str

@typing.type_check_only
class Compliance(typing.TypedDict, total=False):
    ids: _list[str]
    standard: str
    version: str

@typing.type_check_only
class ComplianceDetails(typing.TypedDict, total=False):
    cloudControl: CloudControl
    cloudControlDeploymentNames: _list[str]
    frameworks: _list[Framework]

@typing.type_check_only
class Connection(typing.TypedDict, total=False):
    destinationIp: str
    destinationPort: int
    protocol: typing.Literal["PROTOCOL_UNSPECIFIED", "ICMP", "TCP", "UDP", "GRE", "ESP"]
    sourceIp: str
    sourcePort: int

@typing.type_check_only
class Contact(typing.TypedDict, total=False):
    email: str

@typing.type_check_only
class ContactDetails(typing.TypedDict, total=False):
    contacts: _list[Contact]

@typing.type_check_only
class Container(typing.TypedDict, total=False):
    createTime: str
    imageId: str
    labels: _list[Label]
    name: str
    uri: str

@typing.type_check_only
class Control(typing.TypedDict, total=False):
    controlName: str
    displayName: str

@typing.type_check_only
class Cve(typing.TypedDict, total=False):
    cvssv3: Cvssv3
    exploitReleaseDate: str
    exploitationActivity: typing.Literal[
        "EXPLOITATION_ACTIVITY_UNSPECIFIED",
        "WIDE",
        "CONFIRMED",
        "AVAILABLE",
        "ANTICIPATED",
        "NO_KNOWN",
    ]
    firstExploitationDate: str
    id: str
    impact: typing.Literal[
        "RISK_RATING_UNSPECIFIED", "LOW", "MEDIUM", "HIGH", "CRITICAL"
    ]
    observedInTheWild: bool
    references: _list[Reference]
    upstreamFixAvailable: bool
    zeroDay: bool

@typing.type_check_only
class Cvssv3(typing.TypedDict, total=False):
    attackComplexity: typing.Literal[
        "ATTACK_COMPLEXITY_UNSPECIFIED",
        "ATTACK_COMPLEXITY_LOW",
        "ATTACK_COMPLEXITY_HIGH",
    ]
    attackVector: typing.Literal[
        "ATTACK_VECTOR_UNSPECIFIED",
        "ATTACK_VECTOR_NETWORK",
        "ATTACK_VECTOR_ADJACENT",
        "ATTACK_VECTOR_LOCAL",
        "ATTACK_VECTOR_PHYSICAL",
    ]
    availabilityImpact: typing.Literal[
        "IMPACT_UNSPECIFIED", "IMPACT_HIGH", "IMPACT_LOW", "IMPACT_NONE"
    ]
    baseScore: float
    confidentialityImpact: typing.Literal[
        "IMPACT_UNSPECIFIED", "IMPACT_HIGH", "IMPACT_LOW", "IMPACT_NONE"
    ]
    integrityImpact: typing.Literal[
        "IMPACT_UNSPECIFIED", "IMPACT_HIGH", "IMPACT_LOW", "IMPACT_NONE"
    ]
    privilegesRequired: typing.Literal[
        "PRIVILEGES_REQUIRED_UNSPECIFIED",
        "PRIVILEGES_REQUIRED_NONE",
        "PRIVILEGES_REQUIRED_LOW",
        "PRIVILEGES_REQUIRED_HIGH",
    ]
    scope: typing.Literal["SCOPE_UNSPECIFIED", "SCOPE_UNCHANGED", "SCOPE_CHANGED"]
    userInteraction: typing.Literal[
        "USER_INTERACTION_UNSPECIFIED",
        "USER_INTERACTION_NONE",
        "USER_INTERACTION_REQUIRED",
    ]

@typing.type_check_only
class Cwe(typing.TypedDict, total=False):
    id: str
    references: _list[Reference]

@typing.type_check_only
class DataAccessEvent(typing.TypedDict, total=False):
    eventId: str
    eventTime: str
    operation: typing.Literal["OPERATION_UNSPECIFIED", "READ", "MOVE", "COPY"]
    principalEmail: str

@typing.type_check_only
class DataFlowEvent(typing.TypedDict, total=False):
    eventId: str
    eventTime: str
    operation: typing.Literal["OPERATION_UNSPECIFIED", "READ", "MOVE", "COPY"]
    principalEmail: str
    violatedLocation: str

@typing.type_check_only
class DataRetentionDeletionEvent(typing.TypedDict, total=False):
    dataObjectCount: str
    eventDetectionTime: str
    eventType: typing.Literal[
        "EVENT_TYPE_UNSPECIFIED",
        "EVENT_TYPE_MAX_TTL_EXCEEDED",
        "EVENT_TYPE_MAX_TTL_FROM_CREATION",
        "EVENT_TYPE_MAX_TTL_FROM_LAST_MODIFICATION",
        "EVENT_TYPE_MIN_TTL_FROM_CREATION",
    ]
    maxRetentionAllowed: str
    minRetentionAllowed: str

@typing.type_check_only
class Database(typing.TypedDict, total=False):
    displayName: str
    grantees: _list[str]
    name: str
    query: str
    userName: str
    version: str

@typing.type_check_only
class Dataset(typing.TypedDict, total=False):
    displayName: str
    name: str
    source: str

@typing.type_check_only
class Denied(typing.TypedDict, total=False):
    ipRules: _list[IpRule]

@typing.type_check_only
class Detection(typing.TypedDict, total=False):
    binary: str
    percentPagesMatched: float

@typing.type_check_only
class DetectorReference(typing.TypedDict, total=False):
    detectorId: str
    displayName: str
    explanation: str
    recommendation: str
    severity: typing.Literal[
        "SEVERITY_UNSPECIFIED", "CRITICAL", "HIGH", "MEDIUM", "LOW"
    ]

@typing.type_check_only
class DiscoveredWorkload(typing.TypedDict, total=False):
    confidence: typing.Literal["CONFIDENCE_UNSPECIFIED", "CONFIDENCE_HIGH"]
    detectedRelevantHardware: bool
    detectedRelevantKeywords: bool
    detectedRelevantPackages: bool
    workloadType: typing.Literal[
        "WORKLOAD_TYPE_UNSPECIFIED", "MCP_SERVER", "AI_INFERENCE", "AGENT"
    ]

@typing.type_check_only
class Disk(typing.TypedDict, total=False):
    name: str

@typing.type_check_only
class DiskPath(typing.TypedDict, total=False):
    partitionUuid: str
    relativePath: str

@typing.type_check_only
class DynamicMuteRecord(typing.TypedDict, total=False):
    matchTime: str
    muteConfig: str

@typing.type_check_only
class Empty(typing.TypedDict, total=False): ...

@typing.type_check_only
class EnvironmentVariable(typing.TypedDict, total=False):
    name: str
    val: str

@typing.type_check_only
class ExfilResource(typing.TypedDict, total=False):
    components: _list[str]
    name: str

@typing.type_check_only
class Exfiltration(typing.TypedDict, total=False):
    sources: _list[ExfilResource]
    targets: _list[ExfilResource]
    totalExfiltratedBytes: str

@typing.type_check_only
class ExportFindingsMetadata(typing.TypedDict, total=False):
    bigQueryDestination: BigQueryDestination
    exportStartTime: str

@typing.type_check_only
class ExportFindingsResponse(typing.TypedDict, total=False): ...

@typing.type_check_only
class Expr(typing.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str

@typing.type_check_only
class ExternalExposure(typing.TypedDict, total=False):
    backendBucket: str
    backendService: str
    exposedApplication: str
    exposedEndpoint: str
    exposedService: str
    forwardingRule: str
    hostnameUri: str
    httpResponse: _list[HttpResponse]
    instanceGroup: str
    internalBackendService: str
    loadBalancerFirewallPolicy: str
    networkEndpointGroup: str
    networkIngressFirewallPolicy: str
    networkPathInsightsGenerationTime: str
    privateIpAddress: str
    privatePort: str
    pscNetworkAttachment: str
    pscServiceAttachment: str
    publicIpAddress: str
    publicPort: str
    serviceFirewallPolicy: str

@typing.type_check_only
class File(typing.TypedDict, total=False):
    contents: str
    diskPath: DiskPath
    fileLoadState: typing.Literal[
        "FILE_LOAD_STATE_UNSPECIFIED", "LOADED_BY_PROCESS", "NOT_LOADED_BY_PROCESS"
    ]
    hashedSize: str
    operations: _list[FileOperation]
    partiallyHashed: bool
    path: str
    sha256: str
    size: str

@typing.type_check_only
class FileOperation(typing.TypedDict, total=False):
    type: typing.Literal[
        "OPERATION_TYPE_UNSPECIFIED", "OPEN", "READ", "RENAME", "WRITE", "EXECUTE"
    ]

@typing.type_check_only
class Finding(typing.TypedDict, total=False):
    access: Access
    affectedResources: AffectedResources
    agent: Agent
    agentAnomaly: AgentAnomaly
    agentDataAccessEvents: _list[AgentDataAccessEvent]
    agentSessions: _list[AgentSession]
    aiModel: AiModel
    application: Application
    artifactGuardPolicies: ArtifactGuardPolicies
    attackExposure: AttackExposure
    backupDisasterRecovery: BackupDisasterRecovery
    canonicalName: str
    category: str
    chokepoint: Chokepoint
    cloudArmor: CloudArmor
    cloudDlpDataProfile: CloudDlpDataProfile
    cloudDlpInspection: CloudDlpInspection
    complianceDetails: ComplianceDetails
    compliances: _list[Compliance]
    connections: _list[Connection]
    contacts: dict[str, typing.Any]
    containers: _list[Container]
    createTime: str
    dataAccessEvents: _list[DataAccessEvent]
    dataFlowEvents: _list[DataFlowEvent]
    dataRetentionDeletionEvents: _list[DataRetentionDeletionEvent]
    database: Database
    description: str
    discoveredWorkload: DiscoveredWorkload
    disk: Disk
    eventTime: str
    exfiltration: Exfiltration
    externalExposure: ExternalExposure
    externalSystems: dict[str, typing.Any]
    externalUri: str
    files: _list[File]
    findingClass: typing.Literal[
        "FINDING_CLASS_UNSPECIFIED",
        "THREAT",
        "VULNERABILITY",
        "MISCONFIGURATION",
        "OBSERVATION",
        "SCC_ERROR",
        "POSTURE_VIOLATION",
        "TOXIC_COMBINATION",
        "SENSITIVE_DATA_RISK",
        "CHOKEPOINT",
        "EXTERNAL_EXPOSURE",
        "SECRET",
    ]
    groupMemberships: _list[GroupMembership]
    iamBindings: _list[IamBinding]
    iamDetails: GoogleCloudSecuritycenterV1IamDetails
    indicator: Indicator
    ipRules: IpRules
    job: Job
    kernelRootkit: KernelRootkit
    kubernetes: Kubernetes
    loadBalancers: _list[LoadBalancer]
    logEntries: _list[LogEntry]
    mitreAttack: MitreAttack
    moduleName: str
    mute: typing.Literal["MUTE_UNSPECIFIED", "MUTED", "UNMUTED", "UNDEFINED"]
    muteInfo: MuteInfo
    muteInitiator: str
    muteUpdateTime: str
    name: str
    networks: _list[Network]
    nextSteps: str
    notebook: Notebook
    orgPolicies: _list[OrgPolicy]
    parent: str
    parentDisplayName: str
    policyViolationSummary: PolicyViolationSummary
    processes: _list[Process]
    resourceName: str
    secret: Secret
    securityMarks: SecurityMarks
    securityPosture: SecurityPosture
    severity: typing.Literal[
        "SEVERITY_UNSPECIFIED", "CRITICAL", "HIGH", "MEDIUM", "LOW"
    ]
    sourceProperties: dict[str, typing.Any]
    state: typing.Literal["STATE_UNSPECIFIED", "ACTIVE", "INACTIVE"]
    toxicCombination: ToxicCombination
    vertexAi: VertexAi
    vulnerability: Vulnerability

@typing.type_check_only
class Folder(typing.TypedDict, total=False):
    resourceFolder: str
    resourceFolderDisplayName: str

@typing.type_check_only
class Framework(typing.TypedDict, total=False):
    category: _list[
        typing.Literal[
            "FRAMEWORK_CATEGORY_UNSPECIFIED",
            "SECURITY_BENCHMARKS",
            "ASSURED_WORKLOADS",
            "DATA_SECURITY",
            "GOOGLE_BEST_PRACTICES",
            "CUSTOM_FRAMEWORK",
        ]
    ]
    controls: _list[Control]
    displayName: str
    name: str
    type: typing.Literal[
        "FRAMEWORK_TYPE_UNSPECIFIED", "FRAMEWORK_TYPE_BUILT_IN", "FRAMEWORK_TYPE_CUSTOM"
    ]

@typing.type_check_only
class GcpMetadata(typing.TypedDict, total=False):
    folders: _list[GoogleCloudSecuritycenterV2Folder]
    organization: str
    parent: str
    parentDisplayName: str
    project: str
    projectDisplayName: str

@typing.type_check_only
class Geolocation(typing.TypedDict, total=False):
    regionCode: str

@typing.type_check_only
class GetIamPolicyRequest(typing.TypedDict, total=False):
    options: GetPolicyOptions

@typing.type_check_only
class GetPolicyOptions(typing.TypedDict, total=False):
    requestedPolicyVersion: int

@typing.type_check_only
class GoogleCloudSecuritycenterV1BigQueryExport(typing.TypedDict, total=False):
    createTime: str
    dataset: str
    description: str
    filter: str
    mostRecentEditor: str
    name: str
    principal: str
    updateTime: str

@typing.type_check_only
class GoogleCloudSecuritycenterV1Binding(typing.TypedDict, total=False):
    name: str
    ns: str
    role: Role
    subjects: _list[Subject]

@typing.type_check_only
class GoogleCloudSecuritycenterV1BulkMuteFindingsResponse(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudSecuritycenterV1CustomConfig(typing.TypedDict, total=False):
    customOutput: GoogleCloudSecuritycenterV1CustomOutputSpec
    description: str
    predicate: Expr
    recommendation: str
    resourceSelector: GoogleCloudSecuritycenterV1ResourceSelector
    severity: typing.Literal[
        "SEVERITY_UNSPECIFIED", "CRITICAL", "HIGH", "MEDIUM", "LOW"
    ]

@typing.type_check_only
class GoogleCloudSecuritycenterV1CustomOutputSpec(typing.TypedDict, total=False):
    properties: _list[GoogleCloudSecuritycenterV1Property]

@typing.type_check_only
class GoogleCloudSecuritycenterV1EffectiveSecurityHealthAnalyticsCustomModule(
    typing.TypedDict, total=False
):
    cloudProvider: typing.Literal[
        "CLOUD_PROVIDER_UNSPECIFIED",
        "GOOGLE_CLOUD_PLATFORM",
        "AMAZON_WEB_SERVICES",
        "MICROSOFT_AZURE",
    ]
    customConfig: GoogleCloudSecuritycenterV1CustomConfig
    displayName: str
    enablementState: typing.Literal[
        "ENABLEMENT_STATE_UNSPECIFIED", "ENABLED", "DISABLED"
    ]
    name: str

@typing.type_check_only
class GoogleCloudSecuritycenterV1ExternalSystem(typing.TypedDict, total=False):
    assignees: _list[str]
    caseCloseTime: str
    caseCreateTime: str
    casePriority: str
    caseSla: str
    caseUri: str
    externalSystemUpdateTime: str
    externalUid: str
    name: str
    status: str
    ticketInfo: TicketInfo

@typing.type_check_only
class GoogleCloudSecuritycenterV1IamDetails(typing.TypedDict, total=False):
    iamRolePermissions: _list[GoogleCloudSecuritycenterV1IamRolePermission]

@typing.type_check_only
class GoogleCloudSecuritycenterV1IamRolePermission(typing.TypedDict, total=False):
    name: str
    role: str

@typing.type_check_only
class GoogleCloudSecuritycenterV1MuteConfig(typing.TypedDict, total=False):
    createTime: str
    description: str
    displayName: str
    expiryTime: str
    filter: str
    mostRecentEditor: str
    name: str
    type: typing.Literal["MUTE_CONFIG_TYPE_UNSPECIFIED", "STATIC", "DYNAMIC"]
    updateTime: str

@typing.type_check_only
class GoogleCloudSecuritycenterV1NotificationMessage(typing.TypedDict, total=False):
    finding: Finding
    notificationConfigName: str
    resource: GoogleCloudSecuritycenterV1Resource

@typing.type_check_only
class GoogleCloudSecuritycenterV1Property(typing.TypedDict, total=False):
    name: str
    valueExpression: Expr

@typing.type_check_only
class GoogleCloudSecuritycenterV1Resource(typing.TypedDict, total=False):
    adcApplication: AdcApplication
    adcApplicationTemplate: AdcApplicationTemplateRevision
    adcSharedTemplate: AdcSharedTemplateRevision
    application: GoogleCloudSecuritycenterV1ResourceApplication
    awsMetadata: AwsMetadata
    azureMetadata: AzureMetadata
    cloudProvider: typing.Literal[
        "CLOUD_PROVIDER_UNSPECIFIED",
        "GOOGLE_CLOUD_PLATFORM",
        "AMAZON_WEB_SERVICES",
        "MICROSOFT_AZURE",
    ]
    displayName: str
    folders: _list[Folder]
    location: str
    name: str
    organization: str
    parent: str
    parentDisplayName: str
    project: str
    projectDisplayName: str
    resourcePath: ResourcePath
    resourcePathString: str
    service: str
    type: str

@typing.type_check_only
class GoogleCloudSecuritycenterV1ResourceApplication(typing.TypedDict, total=False):
    attributes: GoogleCloudSecuritycenterV1ResourceApplicationAttributes
    name: str

@typing.type_check_only
class GoogleCloudSecuritycenterV1ResourceApplicationAttributes(
    typing.TypedDict, total=False
):
    businessOwners: _list[
        GoogleCloudSecuritycenterV1ResourceApplicationAttributesContactInfo
    ]
    criticality: GoogleCloudSecuritycenterV1ResourceApplicationAttributesCriticality
    developerOwners: _list[
        GoogleCloudSecuritycenterV1ResourceApplicationAttributesContactInfo
    ]
    environment: GoogleCloudSecuritycenterV1ResourceApplicationAttributesEnvironment
    operatorOwners: _list[
        GoogleCloudSecuritycenterV1ResourceApplicationAttributesContactInfo
    ]

@typing.type_check_only
class GoogleCloudSecuritycenterV1ResourceApplicationAttributesContactInfo(
    typing.TypedDict, total=False
):
    email: str

@typing.type_check_only
class GoogleCloudSecuritycenterV1ResourceApplicationAttributesCriticality(
    typing.TypedDict, total=False
):
    type: typing.Literal[
        "CRITICALITY_TYPE_UNSPECIFIED", "MISSION_CRITICAL", "HIGH", "MEDIUM", "LOW"
    ]

@typing.type_check_only
class GoogleCloudSecuritycenterV1ResourceApplicationAttributesEnvironment(
    typing.TypedDict, total=False
):
    type: typing.Literal[
        "ENVIRONMENT_TYPE_UNSPECIFIED", "PRODUCTION", "STAGING", "TEST", "DEVELOPMENT"
    ]

@typing.type_check_only
class GoogleCloudSecuritycenterV1ResourceSelector(typing.TypedDict, total=False):
    resourceTypes: _list[str]

@typing.type_check_only
class GoogleCloudSecuritycenterV1ResourceValueConfig(typing.TypedDict, total=False):
    cloudProvider: typing.Literal[
        "CLOUD_PROVIDER_UNSPECIFIED",
        "GOOGLE_CLOUD_PLATFORM",
        "AMAZON_WEB_SERVICES",
        "MICROSOFT_AZURE",
    ]
    createTime: str
    description: str
    name: str
    resourceLabelsSelector: dict[str, typing.Any]
    resourceType: str
    resourceValue: typing.Literal[
        "RESOURCE_VALUE_UNSPECIFIED", "HIGH", "MEDIUM", "LOW", "NONE"
    ]
    scope: str
    sensitiveDataProtectionMapping: (
        GoogleCloudSecuritycenterV1SensitiveDataProtectionMapping
    )
    tagValues: _list[str]
    updateTime: str

@typing.type_check_only
class GoogleCloudSecuritycenterV1RunAssetDiscoveryResponse(
    typing.TypedDict, total=False
):
    duration: str
    state: typing.Literal["STATE_UNSPECIFIED", "COMPLETED", "SUPERSEDED", "TERMINATED"]

@typing.type_check_only
class GoogleCloudSecuritycenterV1SecurityHealthAnalyticsCustomModule(
    typing.TypedDict, total=False
):
    ancestorModule: str
    cloudProvider: typing.Literal[
        "CLOUD_PROVIDER_UNSPECIFIED",
        "GOOGLE_CLOUD_PLATFORM",
        "AMAZON_WEB_SERVICES",
        "MICROSOFT_AZURE",
    ]
    customConfig: GoogleCloudSecuritycenterV1CustomConfig
    displayName: str
    enablementState: typing.Literal[
        "ENABLEMENT_STATE_UNSPECIFIED", "ENABLED", "DISABLED", "INHERITED"
    ]
    lastEditor: str
    name: str
    updateTime: str

@typing.type_check_only
class GoogleCloudSecuritycenterV1SensitiveDataProtectionMapping(
    typing.TypedDict, total=False
):
    highSensitivityMapping: typing.Literal[
        "RESOURCE_VALUE_UNSPECIFIED", "HIGH", "MEDIUM", "LOW", "NONE"
    ]
    mediumSensitivityMapping: typing.Literal[
        "RESOURCE_VALUE_UNSPECIFIED", "HIGH", "MEDIUM", "LOW", "NONE"
    ]

@typing.type_check_only
class GoogleCloudSecuritycenterV1beta1Finding(typing.TypedDict, total=False):
    category: str
    createTime: str
    eventTime: str
    externalUri: str
    name: str
    parent: str
    resourceName: str
    securityMarks: GoogleCloudSecuritycenterV1beta1SecurityMarks
    sourceProperties: dict[str, typing.Any]
    state: typing.Literal["STATE_UNSPECIFIED", "ACTIVE", "INACTIVE"]

@typing.type_check_only
class GoogleCloudSecuritycenterV1beta1RunAssetDiscoveryResponse(
    typing.TypedDict, total=False
):
    duration: str
    state: typing.Literal["STATE_UNSPECIFIED", "COMPLETED", "SUPERSEDED", "TERMINATED"]

@typing.type_check_only
class GoogleCloudSecuritycenterV1beta1SecurityMarks(typing.TypedDict, total=False):
    marks: dict[str, typing.Any]
    name: str

@typing.type_check_only
class GoogleCloudSecuritycenterV1p1beta1Finding(typing.TypedDict, total=False):
    canonicalName: str
    category: str
    createTime: str
    eventTime: str
    externalUri: str
    name: str
    parent: str
    resourceName: str
    securityMarks: GoogleCloudSecuritycenterV1p1beta1SecurityMarks
    severity: typing.Literal[
        "SEVERITY_UNSPECIFIED", "CRITICAL", "HIGH", "MEDIUM", "LOW"
    ]
    sourceProperties: dict[str, typing.Any]
    state: typing.Literal["STATE_UNSPECIFIED", "ACTIVE", "INACTIVE"]

@typing.type_check_only
class GoogleCloudSecuritycenterV1p1beta1Folder(typing.TypedDict, total=False):
    resourceFolder: str
    resourceFolderDisplayName: str

@typing.type_check_only
class GoogleCloudSecuritycenterV1p1beta1NotificationMessage(
    typing.TypedDict, total=False
):
    finding: GoogleCloudSecuritycenterV1p1beta1Finding
    notificationConfigName: str
    resource: GoogleCloudSecuritycenterV1p1beta1Resource

@typing.type_check_only
class GoogleCloudSecuritycenterV1p1beta1Resource(typing.TypedDict, total=False):
    folders: _list[GoogleCloudSecuritycenterV1p1beta1Folder]
    name: str
    parent: str
    parentDisplayName: str
    project: str
    projectDisplayName: str

@typing.type_check_only
class GoogleCloudSecuritycenterV1p1beta1RunAssetDiscoveryResponse(
    typing.TypedDict, total=False
):
    duration: str
    state: typing.Literal["STATE_UNSPECIFIED", "COMPLETED", "SUPERSEDED", "TERMINATED"]

@typing.type_check_only
class GoogleCloudSecuritycenterV1p1beta1SecurityMarks(typing.TypedDict, total=False):
    canonicalName: str
    marks: dict[str, typing.Any]
    name: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2Access(typing.TypedDict, total=False):
    callerIp: str
    callerIpGeo: GoogleCloudSecuritycenterV2Geolocation
    methodName: str
    principalEmail: str
    principalSubject: str
    serviceAccountDelegationInfo: _list[
        GoogleCloudSecuritycenterV2ServiceAccountDelegationInfo
    ]
    serviceAccountKeyName: str
    serviceName: str
    userAgent: str
    userAgentFamily: str
    userName: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2AccessReview(typing.TypedDict, total=False):
    group: str
    name: str
    ns: str
    resource: str
    subresource: str
    verb: str
    version: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2AdaptiveProtection(typing.TypedDict, total=False):
    confidence: float

@typing.type_check_only
class GoogleCloudSecuritycenterV2AdcApplication(typing.TypedDict, total=False):
    attributes: GoogleCloudSecuritycenterV2ResourceApplicationAttributes
    name: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2AdcApplicationTemplateRevision(
    typing.TypedDict, total=False
):
    name: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2AdcSharedTemplateRevision(
    typing.TypedDict, total=False
):
    name: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2AffectedResources(typing.TypedDict, total=False):
    count: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2Agent(typing.TypedDict, total=False):
    displayName: str
    id: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2AgentAnomaly(typing.TypedDict, total=False):
    confidenceScore: float
    detectorReferences: _list[GoogleCloudSecuritycenterV2DetectorReference]
    invocationReferences: _list[GoogleCloudSecuritycenterV2InvocationReference]

@typing.type_check_only
class GoogleCloudSecuritycenterV2AgentDataAccessEvent(typing.TypedDict, total=False):
    eventId: str
    eventTime: str
    operation: typing.Literal["OPERATION_UNSPECIFIED", "READ", "MOVE", "COPY"]
    principalSubject: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2AgentSession(typing.TypedDict, total=False):
    sessionId: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2AiModel(typing.TypedDict, total=False):
    deploymentPlatform: typing.Literal[
        "DEPLOYMENT_PLATFORM_UNSPECIFIED", "VERTEX_AI", "GKE", "GCE", "FINE_TUNED_MODEL"
    ]
    displayName: str
    domain: str
    library: str
    location: str
    name: str
    publisher: str
    usageCategory: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2Allowed(typing.TypedDict, total=False):
    ipRules: _list[GoogleCloudSecuritycenterV2IpRule]

@typing.type_check_only
class GoogleCloudSecuritycenterV2Application(typing.TypedDict, total=False):
    baseUri: str
    fullUri: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2ArtifactGuardPolicies(typing.TypedDict, total=False):
    failingPolicies: _list[GoogleCloudSecuritycenterV2ArtifactGuardPolicy]
    resourceId: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2ArtifactGuardPolicy(typing.TypedDict, total=False):
    failureReason: str
    policyId: str
    type: typing.Literal["ARTIFACT_GUARD_POLICY_TYPE_UNSPECIFIED", "VULNERABILITY"]

@typing.type_check_only
class GoogleCloudSecuritycenterV2Attack(typing.TypedDict, total=False):
    classification: str
    volumeBps: int
    volumeBpsLong: str
    volumePps: int
    volumePpsLong: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2AttackExposure(typing.TypedDict, total=False):
    attackExposureResult: str
    exposedHighValueResourcesCount: int
    exposedLowValueResourcesCount: int
    exposedMediumValueResourcesCount: int
    latestCalculationTime: str
    score: float
    state: typing.Literal["STATE_UNSPECIFIED", "CALCULATED", "NOT_CALCULATED"]

@typing.type_check_only
class GoogleCloudSecuritycenterV2AwsAccount(typing.TypedDict, total=False):
    id: str
    name: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2AwsMetadata(typing.TypedDict, total=False):
    account: GoogleCloudSecuritycenterV2AwsAccount
    organization: GoogleCloudSecuritycenterV2AwsOrganization
    organizationalUnits: _list[GoogleCloudSecuritycenterV2AwsOrganizationalUnit]

@typing.type_check_only
class GoogleCloudSecuritycenterV2AwsOrganization(typing.TypedDict, total=False):
    id: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2AwsOrganizationalUnit(typing.TypedDict, total=False):
    id: str
    name: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2AzureManagementGroup(typing.TypedDict, total=False):
    displayName: str
    id: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2AzureMetadata(typing.TypedDict, total=False):
    managementGroups: _list[GoogleCloudSecuritycenterV2AzureManagementGroup]
    resourceGroup: GoogleCloudSecuritycenterV2AzureResourceGroup
    subscription: GoogleCloudSecuritycenterV2AzureSubscription
    tenant: GoogleCloudSecuritycenterV2AzureTenant

@typing.type_check_only
class GoogleCloudSecuritycenterV2AzureResourceGroup(typing.TypedDict, total=False):
    id: str
    name: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2AzureSubscription(typing.TypedDict, total=False):
    displayName: str
    id: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2AzureTenant(typing.TypedDict, total=False):
    displayName: str
    id: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2BackupDisasterRecovery(typing.TypedDict, total=False):
    appliance: str
    applications: _list[str]
    backupCreateTime: str
    backupTemplate: str
    backupType: str
    host: str
    policies: _list[str]
    policyOptions: _list[str]
    profile: str
    storagePool: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2BigQueryExport(typing.TypedDict, total=False):
    createTime: str
    cryptoKeyName: str
    dataset: str
    description: str
    filter: str
    mostRecentEditor: str
    name: str
    principal: str
    updateTime: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2Binding(typing.TypedDict, total=False):
    name: str
    ns: str
    role: GoogleCloudSecuritycenterV2Role
    subjects: _list[GoogleCloudSecuritycenterV2Subject]

@typing.type_check_only
class GoogleCloudSecuritycenterV2BulkMuteFindingsResponse(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudSecuritycenterV2Chokepoint(typing.TypedDict, total=False):
    relatedFindings: _list[str]

@typing.type_check_only
class GoogleCloudSecuritycenterV2CloudArmor(typing.TypedDict, total=False):
    adaptiveProtection: GoogleCloudSecuritycenterV2AdaptiveProtection
    attack: GoogleCloudSecuritycenterV2Attack
    duration: str
    requests: GoogleCloudSecuritycenterV2Requests
    securityPolicy: GoogleCloudSecuritycenterV2SecurityPolicy
    threatVector: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2CloudControl(typing.TypedDict, total=False):
    cloudControlName: str
    policyType: str
    type: typing.Literal["CLOUD_CONTROL_TYPE_UNSPECIFIED", "BUILT_IN", "CUSTOM"]
    version: int

@typing.type_check_only
class GoogleCloudSecuritycenterV2CloudDlpDataProfile(typing.TypedDict, total=False):
    dataProfile: str
    infoTypes: _list[GoogleCloudSecuritycenterV2InfoType]
    parentType: typing.Literal["PARENT_TYPE_UNSPECIFIED", "ORGANIZATION", "PROJECT"]

@typing.type_check_only
class GoogleCloudSecuritycenterV2CloudDlpInspection(typing.TypedDict, total=False):
    fullScan: bool
    infoType: str
    infoTypeCount: str
    inspectJob: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2CloudLoggingEntry(typing.TypedDict, total=False):
    insertId: str
    logId: str
    resourceContainer: str
    timestamp: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2Compliance(typing.TypedDict, total=False):
    ids: _list[str]
    standard: str
    version: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2ComplianceDetails(typing.TypedDict, total=False):
    cloudControl: GoogleCloudSecuritycenterV2CloudControl
    cloudControlDeploymentNames: _list[str]
    frameworks: _list[GoogleCloudSecuritycenterV2Framework]

@typing.type_check_only
class GoogleCloudSecuritycenterV2Connection(typing.TypedDict, total=False):
    destinationIp: str
    destinationPort: int
    protocol: typing.Literal["PROTOCOL_UNSPECIFIED", "ICMP", "TCP", "UDP", "GRE", "ESP"]
    sourceIp: str
    sourcePort: int

@typing.type_check_only
class GoogleCloudSecuritycenterV2Contact(typing.TypedDict, total=False):
    email: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2ContactDetails(typing.TypedDict, total=False):
    contacts: _list[GoogleCloudSecuritycenterV2Contact]

@typing.type_check_only
class GoogleCloudSecuritycenterV2Container(typing.TypedDict, total=False):
    createTime: str
    imageId: str
    labels: _list[GoogleCloudSecuritycenterV2Label]
    name: str
    uri: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2Control(typing.TypedDict, total=False):
    controlName: str
    displayName: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2Cve(typing.TypedDict, total=False):
    cvssv3: GoogleCloudSecuritycenterV2Cvssv3
    exploitReleaseDate: str
    exploitationActivity: typing.Literal[
        "EXPLOITATION_ACTIVITY_UNSPECIFIED",
        "WIDE",
        "CONFIRMED",
        "AVAILABLE",
        "ANTICIPATED",
        "NO_KNOWN",
    ]
    firstExploitationDate: str
    id: str
    impact: typing.Literal[
        "RISK_RATING_UNSPECIFIED", "LOW", "MEDIUM", "HIGH", "CRITICAL"
    ]
    observedInTheWild: bool
    references: _list[GoogleCloudSecuritycenterV2Reference]
    upstreamFixAvailable: bool
    zeroDay: bool

@typing.type_check_only
class GoogleCloudSecuritycenterV2Cvssv3(typing.TypedDict, total=False):
    attackComplexity: typing.Literal[
        "ATTACK_COMPLEXITY_UNSPECIFIED",
        "ATTACK_COMPLEXITY_LOW",
        "ATTACK_COMPLEXITY_HIGH",
    ]
    attackVector: typing.Literal[
        "ATTACK_VECTOR_UNSPECIFIED",
        "ATTACK_VECTOR_NETWORK",
        "ATTACK_VECTOR_ADJACENT",
        "ATTACK_VECTOR_LOCAL",
        "ATTACK_VECTOR_PHYSICAL",
    ]
    availabilityImpact: typing.Literal[
        "IMPACT_UNSPECIFIED", "IMPACT_HIGH", "IMPACT_LOW", "IMPACT_NONE"
    ]
    baseScore: float
    confidentialityImpact: typing.Literal[
        "IMPACT_UNSPECIFIED", "IMPACT_HIGH", "IMPACT_LOW", "IMPACT_NONE"
    ]
    integrityImpact: typing.Literal[
        "IMPACT_UNSPECIFIED", "IMPACT_HIGH", "IMPACT_LOW", "IMPACT_NONE"
    ]
    privilegesRequired: typing.Literal[
        "PRIVILEGES_REQUIRED_UNSPECIFIED",
        "PRIVILEGES_REQUIRED_NONE",
        "PRIVILEGES_REQUIRED_LOW",
        "PRIVILEGES_REQUIRED_HIGH",
    ]
    scope: typing.Literal["SCOPE_UNSPECIFIED", "SCOPE_UNCHANGED", "SCOPE_CHANGED"]
    userInteraction: typing.Literal[
        "USER_INTERACTION_UNSPECIFIED",
        "USER_INTERACTION_NONE",
        "USER_INTERACTION_REQUIRED",
    ]

@typing.type_check_only
class GoogleCloudSecuritycenterV2Cwe(typing.TypedDict, total=False):
    id: str
    references: _list[GoogleCloudSecuritycenterV2Reference]

@typing.type_check_only
class GoogleCloudSecuritycenterV2DataAccessEvent(typing.TypedDict, total=False):
    eventId: str
    eventTime: str
    operation: typing.Literal["OPERATION_UNSPECIFIED", "READ", "MOVE", "COPY"]
    principalEmail: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2DataFlowEvent(typing.TypedDict, total=False):
    eventId: str
    eventTime: str
    operation: typing.Literal["OPERATION_UNSPECIFIED", "READ", "MOVE", "COPY"]
    principalEmail: str
    violatedLocation: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2DataRetentionDeletionEvent(
    typing.TypedDict, total=False
):
    dataObjectCount: str
    eventDetectionTime: str
    eventType: typing.Literal[
        "EVENT_TYPE_UNSPECIFIED",
        "EVENT_TYPE_MAX_TTL_EXCEEDED",
        "EVENT_TYPE_MAX_TTL_FROM_CREATION",
        "EVENT_TYPE_MAX_TTL_FROM_LAST_MODIFICATION",
        "EVENT_TYPE_MIN_TTL_FROM_CREATION",
    ]
    maxRetentionAllowed: str
    minRetentionAllowed: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2Database(typing.TypedDict, total=False):
    displayName: str
    grantees: _list[str]
    name: str
    query: str
    userName: str
    version: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2Dataset(typing.TypedDict, total=False):
    displayName: str
    name: str
    source: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2Denied(typing.TypedDict, total=False):
    ipRules: _list[GoogleCloudSecuritycenterV2IpRule]

@typing.type_check_only
class GoogleCloudSecuritycenterV2Detection(typing.TypedDict, total=False):
    binary: str
    percentPagesMatched: float

@typing.type_check_only
class GoogleCloudSecuritycenterV2DetectorReference(typing.TypedDict, total=False):
    detectorId: str
    displayName: str
    explanation: str
    recommendation: str
    severity: typing.Literal[
        "SEVERITY_UNSPECIFIED", "CRITICAL", "HIGH", "MEDIUM", "LOW"
    ]

@typing.type_check_only
class GoogleCloudSecuritycenterV2DiscoveredWorkload(typing.TypedDict, total=False):
    confidence: typing.Literal["CONFIDENCE_UNSPECIFIED", "CONFIDENCE_HIGH"]
    detectedRelevantHardware: bool
    detectedRelevantKeywords: bool
    detectedRelevantPackages: bool
    workloadType: typing.Literal[
        "WORKLOAD_TYPE_UNSPECIFIED", "MCP_SERVER", "AI_INFERENCE", "AGENT"
    ]

@typing.type_check_only
class GoogleCloudSecuritycenterV2Disk(typing.TypedDict, total=False):
    name: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2DiskPath(typing.TypedDict, total=False):
    partitionUuid: str
    relativePath: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2DynamicMuteRecord(typing.TypedDict, total=False):
    matchTime: str
    muteConfig: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2EnvironmentVariable(typing.TypedDict, total=False):
    name: str
    val: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2ExfilResource(typing.TypedDict, total=False):
    components: _list[str]
    name: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2Exfiltration(typing.TypedDict, total=False):
    sources: _list[GoogleCloudSecuritycenterV2ExfilResource]
    targets: _list[GoogleCloudSecuritycenterV2ExfilResource]
    totalExfiltratedBytes: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2ExternalExposure(typing.TypedDict, total=False):
    backendBucket: str
    backendService: str
    exposedApplication: str
    exposedEndpoint: str
    exposedService: str
    forwardingRule: str
    hostnameUri: str
    httpResponse: _list[GoogleCloudSecuritycenterV2HttpResponse]
    instanceGroup: str
    internalBackendService: str
    loadBalancerFirewallPolicy: str
    networkEndpointGroup: str
    networkIngressFirewallPolicy: str
    networkPathInsightsGenerationTime: str
    privateIpAddress: str
    privatePort: str
    pscNetworkAttachment: str
    pscServiceAttachment: str
    publicIpAddress: str
    publicPort: str
    serviceFirewallPolicy: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2ExternalSystem(typing.TypedDict, total=False):
    assignees: _list[str]
    caseCloseTime: str
    caseCreateTime: str
    casePriority: str
    caseSla: str
    caseUri: str
    externalSystemUpdateTime: str
    externalUid: str
    name: str
    status: str
    ticketInfo: GoogleCloudSecuritycenterV2TicketInfo

@typing.type_check_only
class GoogleCloudSecuritycenterV2File(typing.TypedDict, total=False):
    contents: str
    diskPath: GoogleCloudSecuritycenterV2DiskPath
    fileLoadState: typing.Literal[
        "FILE_LOAD_STATE_UNSPECIFIED", "LOADED_BY_PROCESS", "NOT_LOADED_BY_PROCESS"
    ]
    hashedSize: str
    operations: _list[GoogleCloudSecuritycenterV2FileOperation]
    partiallyHashed: bool
    path: str
    sha256: str
    size: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2FileOperation(typing.TypedDict, total=False):
    type: typing.Literal[
        "OPERATION_TYPE_UNSPECIFIED", "OPEN", "READ", "RENAME", "WRITE", "EXECUTE"
    ]

@typing.type_check_only
class GoogleCloudSecuritycenterV2Finding(typing.TypedDict, total=False):
    access: GoogleCloudSecuritycenterV2Access
    affectedResources: GoogleCloudSecuritycenterV2AffectedResources
    agent: GoogleCloudSecuritycenterV2Agent
    agentAnomaly: GoogleCloudSecuritycenterV2AgentAnomaly
    agentDataAccessEvents: _list[GoogleCloudSecuritycenterV2AgentDataAccessEvent]
    agentSessions: _list[GoogleCloudSecuritycenterV2AgentSession]
    aiModel: GoogleCloudSecuritycenterV2AiModel
    application: GoogleCloudSecuritycenterV2Application
    artifactGuardPolicies: GoogleCloudSecuritycenterV2ArtifactGuardPolicies
    attackExposure: GoogleCloudSecuritycenterV2AttackExposure
    backupDisasterRecovery: GoogleCloudSecuritycenterV2BackupDisasterRecovery
    canonicalName: str
    category: str
    chokepoint: GoogleCloudSecuritycenterV2Chokepoint
    cloudArmor: GoogleCloudSecuritycenterV2CloudArmor
    cloudDlpDataProfile: GoogleCloudSecuritycenterV2CloudDlpDataProfile
    cloudDlpInspection: GoogleCloudSecuritycenterV2CloudDlpInspection
    complianceDetails: GoogleCloudSecuritycenterV2ComplianceDetails
    compliances: _list[GoogleCloudSecuritycenterV2Compliance]
    connections: _list[GoogleCloudSecuritycenterV2Connection]
    contacts: dict[str, typing.Any]
    containers: _list[GoogleCloudSecuritycenterV2Container]
    createTime: str
    cryptoKeyName: str
    dataAccessEvents: _list[GoogleCloudSecuritycenterV2DataAccessEvent]
    dataFlowEvents: _list[GoogleCloudSecuritycenterV2DataFlowEvent]
    dataRetentionDeletionEvents: _list[
        GoogleCloudSecuritycenterV2DataRetentionDeletionEvent
    ]
    database: GoogleCloudSecuritycenterV2Database
    description: str
    discoveredWorkload: GoogleCloudSecuritycenterV2DiscoveredWorkload
    disk: GoogleCloudSecuritycenterV2Disk
    eventTime: str
    exfiltration: GoogleCloudSecuritycenterV2Exfiltration
    externalExposure: GoogleCloudSecuritycenterV2ExternalExposure
    externalSystems: dict[str, typing.Any]
    externalUri: str
    files: _list[GoogleCloudSecuritycenterV2File]
    findingClass: typing.Literal[
        "FINDING_CLASS_UNSPECIFIED",
        "THREAT",
        "VULNERABILITY",
        "MISCONFIGURATION",
        "OBSERVATION",
        "SCC_ERROR",
        "POSTURE_VIOLATION",
        "TOXIC_COMBINATION",
        "SENSITIVE_DATA_RISK",
        "CHOKEPOINT",
        "EXTERNAL_EXPOSURE",
        "SECRET",
    ]
    groupMemberships: _list[GoogleCloudSecuritycenterV2GroupMembership]
    iamBindings: _list[GoogleCloudSecuritycenterV2IamBinding]
    iamDetails: GoogleCloudSecuritycenterV2IamDetails
    indicator: GoogleCloudSecuritycenterV2Indicator
    ipRules: GoogleCloudSecuritycenterV2IpRules
    job: GoogleCloudSecuritycenterV2Job
    kernelRootkit: GoogleCloudSecuritycenterV2KernelRootkit
    kubernetes: GoogleCloudSecuritycenterV2Kubernetes
    loadBalancers: _list[GoogleCloudSecuritycenterV2LoadBalancer]
    logEntries: _list[GoogleCloudSecuritycenterV2LogEntry]
    mitreAttack: GoogleCloudSecuritycenterV2MitreAttack
    moduleName: str
    mute: typing.Literal["MUTE_UNSPECIFIED", "MUTED", "UNMUTED", "UNDEFINED"]
    muteInfo: GoogleCloudSecuritycenterV2MuteInfo
    muteInitiator: str
    muteUpdateTime: str
    name: str
    networks: _list[GoogleCloudSecuritycenterV2Network]
    nextSteps: str
    notebook: GoogleCloudSecuritycenterV2Notebook
    orgPolicies: _list[GoogleCloudSecuritycenterV2OrgPolicy]
    parent: str
    parentDisplayName: str
    policyViolationSummary: GoogleCloudSecuritycenterV2PolicyViolationSummary
    processes: _list[GoogleCloudSecuritycenterV2Process]
    resourceName: str
    secret: GoogleCloudSecuritycenterV2Secret
    securityMarks: GoogleCloudSecuritycenterV2SecurityMarks
    securityPosture: GoogleCloudSecuritycenterV2SecurityPosture
    severity: typing.Literal[
        "SEVERITY_UNSPECIFIED", "CRITICAL", "HIGH", "MEDIUM", "LOW"
    ]
    sourceProperties: dict[str, typing.Any]
    state: typing.Literal["STATE_UNSPECIFIED", "ACTIVE", "INACTIVE"]
    toxicCombination: GoogleCloudSecuritycenterV2ToxicCombination
    vertexAi: GoogleCloudSecuritycenterV2VertexAi
    vulnerability: GoogleCloudSecuritycenterV2Vulnerability

@typing.type_check_only
class GoogleCloudSecuritycenterV2Folder(typing.TypedDict, total=False):
    resourceFolder: str
    resourceFolderDisplayName: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2Framework(typing.TypedDict, total=False):
    category: _list[
        typing.Literal[
            "FRAMEWORK_CATEGORY_UNSPECIFIED",
            "SECURITY_BENCHMARKS",
            "ASSURED_WORKLOADS",
            "DATA_SECURITY",
            "GOOGLE_BEST_PRACTICES",
            "CUSTOM_FRAMEWORK",
        ]
    ]
    controls: _list[GoogleCloudSecuritycenterV2Control]
    displayName: str
    name: str
    type: typing.Literal[
        "FRAMEWORK_TYPE_UNSPECIFIED", "FRAMEWORK_TYPE_BUILT_IN", "FRAMEWORK_TYPE_CUSTOM"
    ]

@typing.type_check_only
class GoogleCloudSecuritycenterV2Geolocation(typing.TypedDict, total=False):
    regionCode: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2GroupMembership(typing.TypedDict, total=False):
    groupId: str
    groupType: typing.Literal[
        "GROUP_TYPE_UNSPECIFIED",
        "GROUP_TYPE_TOXIC_COMBINATION",
        "GROUP_TYPE_CHOKEPOINT",
    ]

@typing.type_check_only
class GoogleCloudSecuritycenterV2HttpResponse(typing.TypedDict, total=False):
    path: str
    statusCode: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2IamBinding(typing.TypedDict, total=False):
    action: typing.Literal["ACTION_UNSPECIFIED", "ADD", "REMOVE"]
    member: str
    role: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2IamDetails(typing.TypedDict, total=False):
    iamRolePermissions: _list[GoogleCloudSecuritycenterV2IamRolePermission]

@typing.type_check_only
class GoogleCloudSecuritycenterV2IamRolePermission(typing.TypedDict, total=False):
    name: str
    role: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2Indicator(typing.TypedDict, total=False):
    domains: _list[str]
    ipAddresses: _list[str]
    signatures: _list[GoogleCloudSecuritycenterV2ProcessSignature]
    uris: _list[str]

@typing.type_check_only
class GoogleCloudSecuritycenterV2InfoType(typing.TypedDict, total=False):
    name: str
    sensitivityScore: GoogleCloudSecuritycenterV2SensitivityScore
    version: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2InvocationReference(typing.TypedDict, total=False):
    invocationId: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2IpRule(typing.TypedDict, total=False):
    portRanges: _list[GoogleCloudSecuritycenterV2PortRange]
    protocol: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2IpRules(typing.TypedDict, total=False):
    allowed: GoogleCloudSecuritycenterV2Allowed
    denied: GoogleCloudSecuritycenterV2Denied
    destinationIpRanges: _list[str]
    direction: typing.Literal["DIRECTION_UNSPECIFIED", "INGRESS", "EGRESS"]
    exposedServices: _list[str]
    sourceIpRanges: _list[str]

@typing.type_check_only
class GoogleCloudSecuritycenterV2Issue(typing.TypedDict, total=False):
    createTime: str
    description: str
    detection: str
    domains: _list[GoogleCloudSecuritycenterV2IssueDomain]
    exposureScore: float
    issueType: typing.Literal[
        "ISSUE_TYPE_UNSPECIFIED", "CHOKEPOINT", "TOXIC_COMBINATION", "INSIGHT"
    ]
    lastObservationTime: str
    mute: GoogleCloudSecuritycenterV2IssueMute
    name: str
    primaryResource: GoogleCloudSecuritycenterV2IssueResource
    relatedFindings: _list[GoogleCloudSecuritycenterV2IssueFinding]
    remediations: _list[str]
    secondaryResources: _list[GoogleCloudSecuritycenterV2IssueResource]
    securityContexts: _list[GoogleCloudSecuritycenterV2IssueSecurityContext]
    severity: typing.Literal[
        "SEVERITY_UNSPECIFIED", "CRITICAL", "HIGH", "MEDIUM", "LOW"
    ]
    state: typing.Literal["STATE_UNSPECIFIED", "ACTIVE", "INACTIVE"]
    updateTime: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2IssueDomain(typing.TypedDict, total=False):
    domainCategory: typing.Literal[
        "DOMAIN_CATEGORY_UNSPECIFIED",
        "AI",
        "CODE",
        "CONTAINER",
        "DATA",
        "IDENTITY_AND_ACCESS",
        "VULNERABILITY",
        "THREAT",
    ]

@typing.type_check_only
class GoogleCloudSecuritycenterV2IssueFinding(typing.TypedDict, total=False):
    cve: GoogleCloudSecuritycenterV2IssueFindingCve
    name: str
    securityBulletin: GoogleCloudSecuritycenterV2IssueFindingSecurityBulletin

@typing.type_check_only
class GoogleCloudSecuritycenterV2IssueFindingCve(typing.TypedDict, total=False):
    name: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2IssueFindingSecurityBulletin(
    typing.TypedDict, total=False
):
    name: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2IssueMute(typing.TypedDict, total=False):
    muteInitiator: str
    muteReason: str
    muteState: typing.Literal["MUTE_STATE_UNSPECIFIED", "NOT_MUTED", "MUTED"]
    muteUpdateTime: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2IssueResource(typing.TypedDict, total=False):
    adcApplication: GoogleCloudSecuritycenterV2IssueResourceAdcApplication
    adcApplicationTemplate: (
        GoogleCloudSecuritycenterV2IssueResourceAdcApplicationTemplateRevision
    )
    adcSharedTemplate: GoogleCloudSecuritycenterV2IssueResourceAdcSharedTemplateRevision
    application: GoogleCloudSecuritycenterV2IssueResourceApplication
    awsMetadata: GoogleCloudSecuritycenterV2IssueResourceAwsMetadata
    azureMetadata: GoogleCloudSecuritycenterV2IssueResourceAzureMetadata
    cloudProvider: typing.Literal[
        "CLOUD_PROVIDER_UNSPECIFIED",
        "GOOGLE_CLOUD",
        "AMAZON_WEB_SERVICES",
        "MICROSOFT_AZURE",
    ]
    displayName: str
    googleCloudMetadata: GoogleCloudSecuritycenterV2IssueResourceGoogleCloudMetadata
    name: str
    type: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2IssueResourceAdcApplication(
    typing.TypedDict, total=False
):
    attributes: GoogleCloudSecuritycenterV2IssueResourceApplicationAttributes
    name: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2IssueResourceAdcApplicationTemplateRevision(
    typing.TypedDict, total=False
):
    name: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2IssueResourceAdcSharedTemplateRevision(
    typing.TypedDict, total=False
):
    name: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2IssueResourceApplication(
    typing.TypedDict, total=False
):
    attributes: GoogleCloudSecuritycenterV2IssueResourceApplicationAttributes
    name: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2IssueResourceApplicationAttributes(
    typing.TypedDict, total=False
):
    businessOwners: _list[
        GoogleCloudSecuritycenterV2IssueResourceApplicationAttributesContactInfo
    ]
    criticality: (
        GoogleCloudSecuritycenterV2IssueResourceApplicationAttributesCriticality
    )
    developerOwners: _list[
        GoogleCloudSecuritycenterV2IssueResourceApplicationAttributesContactInfo
    ]
    environment: (
        GoogleCloudSecuritycenterV2IssueResourceApplicationAttributesEnvironment
    )
    operatorOwners: _list[
        GoogleCloudSecuritycenterV2IssueResourceApplicationAttributesContactInfo
    ]

@typing.type_check_only
class GoogleCloudSecuritycenterV2IssueResourceApplicationAttributesContactInfo(
    typing.TypedDict, total=False
):
    email: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2IssueResourceApplicationAttributesCriticality(
    typing.TypedDict, total=False
):
    type: typing.Literal[
        "CRITICALITY_TYPE_UNSPECIFIED", "MISSION_CRITICAL", "HIGH", "MEDIUM", "LOW"
    ]

@typing.type_check_only
class GoogleCloudSecuritycenterV2IssueResourceApplicationAttributesEnvironment(
    typing.TypedDict, total=False
):
    type: typing.Literal[
        "ENVIRONMENT_TYPE_UNSPECIFIED", "PRODUCTION", "STAGING", "TEST", "DEVELOPMENT"
    ]

@typing.type_check_only
class GoogleCloudSecuritycenterV2IssueResourceAwsMetadata(
    typing.TypedDict, total=False
):
    account: GoogleCloudSecuritycenterV2IssueResourceAwsMetadataAwsAccount

@typing.type_check_only
class GoogleCloudSecuritycenterV2IssueResourceAwsMetadataAwsAccount(
    typing.TypedDict, total=False
):
    id: str
    name: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2IssueResourceAzureMetadata(
    typing.TypedDict, total=False
):
    subscription: GoogleCloudSecuritycenterV2IssueResourceAzureMetadataAzureSubscription

@typing.type_check_only
class GoogleCloudSecuritycenterV2IssueResourceAzureMetadataAzureSubscription(
    typing.TypedDict, total=False
):
    displayName: str
    id: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2IssueResourceGoogleCloudMetadata(
    typing.TypedDict, total=False
):
    projectId: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2IssueSecurityContext(typing.TypedDict, total=False):
    aggregatedCount: GoogleCloudSecuritycenterV2IssueSecurityContextAggregatedCount
    context: GoogleCloudSecuritycenterV2IssueSecurityContextContext

@typing.type_check_only
class GoogleCloudSecuritycenterV2IssueSecurityContextAggregatedCount(
    typing.TypedDict, total=False
):
    key: str
    value: int

@typing.type_check_only
class GoogleCloudSecuritycenterV2IssueSecurityContextContext(
    typing.TypedDict, total=False
):
    type: str
    values: _list[str]

@typing.type_check_only
class GoogleCloudSecuritycenterV2Job(typing.TypedDict, total=False):
    errorCode: int
    location: str
    name: str
    state: typing.Literal[
        "JOB_STATE_UNSPECIFIED", "PENDING", "RUNNING", "SUCCEEDED", "FAILED"
    ]

@typing.type_check_only
class GoogleCloudSecuritycenterV2KernelRootkit(typing.TypedDict, total=False):
    name: str
    unexpectedCodeModification: bool
    unexpectedFtraceHandler: bool
    unexpectedInterruptHandler: bool
    unexpectedKernelCodePages: bool
    unexpectedKprobeHandler: bool
    unexpectedProcessesInRunqueue: bool
    unexpectedReadOnlyDataModification: bool
    unexpectedSystemCallHandler: bool

@typing.type_check_only
class GoogleCloudSecuritycenterV2Kubernetes(typing.TypedDict, total=False):
    accessReviews: _list[GoogleCloudSecuritycenterV2AccessReview]
    bindings: _list[GoogleCloudSecuritycenterV2Binding]
    nodePools: _list[GoogleCloudSecuritycenterV2NodePool]
    nodes: _list[GoogleCloudSecuritycenterV2Node]
    objects: _list[GoogleCloudSecuritycenterV2Object]
    pods: _list[GoogleCloudSecuritycenterV2Pod]
    roles: _list[GoogleCloudSecuritycenterV2Role]

@typing.type_check_only
class GoogleCloudSecuritycenterV2Label(typing.TypedDict, total=False):
    name: str
    value: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2LoadBalancer(typing.TypedDict, total=False):
    name: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2LogEntry(typing.TypedDict, total=False):
    cloudLoggingEntry: GoogleCloudSecuritycenterV2CloudLoggingEntry

@typing.type_check_only
class GoogleCloudSecuritycenterV2MemoryHashSignature(typing.TypedDict, total=False):
    binaryFamily: str
    detections: _list[GoogleCloudSecuritycenterV2Detection]

@typing.type_check_only
class GoogleCloudSecuritycenterV2MitreAttack(typing.TypedDict, total=False):
    additionalTactics: _list[
        typing.Literal[
            "TACTIC_UNSPECIFIED",
            "RECONNAISSANCE",
            "RESOURCE_DEVELOPMENT",
            "INITIAL_ACCESS",
            "EXECUTION",
            "PERSISTENCE",
            "PRIVILEGE_ESCALATION",
            "DEFENSE_EVASION",
            "CREDENTIAL_ACCESS",
            "DISCOVERY",
            "LATERAL_MOVEMENT",
            "COLLECTION",
            "COMMAND_AND_CONTROL",
            "EXFILTRATION",
            "IMPACT",
        ]
    ]
    additionalTechniques: _list[
        typing.Literal[
            "TECHNIQUE_UNSPECIFIED",
            "DATA_OBFUSCATION",
            "DATA_OBFUSCATION_STEGANOGRAPHY",
            "OS_CREDENTIAL_DUMPING",
            "OS_CREDENTIAL_DUMPING_PROC_FILESYSTEM",
            "OS_CREDENTIAL_DUMPING_ETC_PASSWORD_AND_ETC_SHADOW",
            "DATA_FROM_LOCAL_SYSTEM",
            "AUTOMATED_EXFILTRATION",
            "OBFUSCATED_FILES_OR_INFO",
            "STEGANOGRAPHY",
            "COMPILE_AFTER_DELIVERY",
            "COMMAND_OBFUSCATION",
            "SCHEDULED_TRANSFER",
            "SYSTEM_OWNER_USER_DISCOVERY",
            "MASQUERADING",
            "MATCH_LEGITIMATE_NAME_OR_LOCATION",
            "BOOT_OR_LOGON_INITIALIZATION_SCRIPTS",
            "STARTUP_ITEMS",
            "NETWORK_SERVICE_DISCOVERY",
            "SCHEDULED_TASK_JOB",
            "SCHEDULED_TASK_JOB_CRON",
            "CONTAINER_ORCHESTRATION_JOB",
            "PROCESS_INJECTION",
            "INPUT_CAPTURE",
            "INPUT_CAPTURE_KEYLOGGING",
            "PROCESS_DISCOVERY",
            "COMMAND_AND_SCRIPTING_INTERPRETER",
            "UNIX_SHELL",
            "PYTHON",
            "EXPLOITATION_FOR_PRIVILEGE_ESCALATION",
            "PERMISSION_GROUPS_DISCOVERY",
            "CLOUD_GROUPS",
            "INDICATOR_REMOVAL",
            "INDICATOR_REMOVAL_CLEAR_LINUX_OR_MAC_SYSTEM_LOGS",
            "INDICATOR_REMOVAL_CLEAR_COMMAND_HISTORY",
            "INDICATOR_REMOVAL_FILE_DELETION",
            "INDICATOR_REMOVAL_TIMESTOMP",
            "INDICATOR_REMOVAL_CLEAR_MAILBOX_DATA",
            "APPLICATION_LAYER_PROTOCOL",
            "DNS",
            "SOFTWARE_DEPLOYMENT_TOOLS",
            "VALID_ACCOUNTS",
            "DEFAULT_ACCOUNTS",
            "LOCAL_ACCOUNTS",
            "CLOUD_ACCOUNTS",
            "FILE_AND_DIRECTORY_DISCOVERY",
            "ACCOUNT_DISCOVERY_LOCAL_ACCOUNT",
            "PROXY",
            "EXTERNAL_PROXY",
            "MULTI_HOP_PROXY",
            "ACCOUNT_MANIPULATION",
            "ADDITIONAL_CLOUD_CREDENTIALS",
            "ADDITIONAL_CLOUD_ROLES",
            "SSH_AUTHORIZED_KEYS",
            "ADDITIONAL_CONTAINER_CLUSTER_ROLES",
            "MULTI_STAGE_CHANNELS",
            "INGRESS_TOOL_TRANSFER",
            "NATIVE_API",
            "BRUTE_FORCE",
            "AUTOMATED_COLLECTION",
            "SHARED_MODULES",
            "DATA_ENCODING",
            "STANDARD_ENCODING",
            "ACCESS_TOKEN_MANIPULATION",
            "TOKEN_IMPERSONATION_OR_THEFT",
            "CREATE_ACCOUNT",
            "LOCAL_ACCOUNT",
            "DEOBFUSCATE_DECODE_FILES_OR_INFO",
            "EXPLOIT_PUBLIC_FACING_APPLICATION",
            "SUPPLY_CHAIN_COMPROMISE",
            "COMPROMISE_SOFTWARE_DEPENDENCIES_AND_DEVELOPMENT_TOOLS",
            "EXPLOITATION_FOR_CLIENT_EXECUTION",
            "USER_EXECUTION",
            "EXPLOITATION_FOR_CREDENTIAL_ACCESS",
            "LINUX_AND_MAC_FILE_AND_DIRECTORY_PERMISSIONS_MODIFICATION",
            "DOMAIN_POLICY_MODIFICATION",
            "DATA_DESTRUCTION",
            "DATA_ENCRYPTED_FOR_IMPACT",
            "SERVICE_STOP",
            "INHIBIT_SYSTEM_RECOVERY",
            "FIRMWARE_CORRUPTION",
            "RESOURCE_HIJACKING",
            "NETWORK_DENIAL_OF_SERVICE",
            "CLOUD_SERVICE_DISCOVERY",
            "STEAL_APPLICATION_ACCESS_TOKEN",
            "ACCOUNT_ACCESS_REMOVAL",
            "TRANSFER_DATA_TO_CLOUD_ACCOUNT",
            "STEAL_WEB_SESSION_COOKIE",
            "CREATE_OR_MODIFY_SYSTEM_PROCESS",
            "EVENT_TRIGGERED_EXECUTION",
            "BOOT_OR_LOGON_AUTOSTART_EXECUTION",
            "KERNEL_MODULES_AND_EXTENSIONS",
            "SHORTCUT_MODIFICATION",
            "ABUSE_ELEVATION_CONTROL_MECHANISM",
            "ABUSE_ELEVATION_CONTROL_MECHANISM_SETUID_AND_SETGID",
            "ABUSE_ELEVATION_CONTROL_MECHANISM_SUDO_AND_SUDO_CACHING",
            "UNSECURED_CREDENTIALS",
            "CREDENTIALS_IN_FILES",
            "BASH_HISTORY",
            "PRIVATE_KEYS",
            "SUBVERT_TRUST_CONTROL",
            "INSTALL_ROOT_CERTIFICATE",
            "COMPROMISE_HOST_SOFTWARE_BINARY",
            "CREDENTIALS_FROM_PASSWORD_STORES",
            "MODIFY_AUTHENTICATION_PROCESS",
            "PLUGGABLE_AUTHENTICATION_MODULES",
            "MULTI_FACTOR_AUTHENTICATION",
            "IMPAIR_DEFENSES",
            "DISABLE_OR_MODIFY_TOOLS",
            "INDICATOR_BLOCKING",
            "DISABLE_OR_MODIFY_LINUX_AUDIT_SYSTEM",
            "HIDE_ARTIFACTS",
            "HIDDEN_FILES_AND_DIRECTORIES",
            "HIDDEN_USERS",
            "EXFILTRATION_OVER_WEB_SERVICE",
            "EXFILTRATION_TO_CLOUD_STORAGE",
            "DYNAMIC_RESOLUTION",
            "LATERAL_TOOL_TRANSFER",
            "HIJACK_EXECUTION_FLOW",
            "HIJACK_EXECUTION_FLOW_DYNAMIC_LINKER_HIJACKING",
            "MODIFY_CLOUD_COMPUTE_INFRASTRUCTURE",
            "CREATE_SNAPSHOT",
            "CLOUD_INFRASTRUCTURE_DISCOVERY",
            "DEVELOP_CAPABILITIES",
            "DEVELOP_CAPABILITIES_MALWARE",
            "OBTAIN_CAPABILITIES",
            "OBTAIN_CAPABILITIES_MALWARE",
            "OBTAIN_CAPABILITIES_VULNERABILITIES",
            "ACTIVE_SCANNING",
            "SCANNING_IP_BLOCKS",
            "STAGE_CAPABILITIES",
            "UPLOAD_MALWARE",
            "CONTAINER_ADMINISTRATION_COMMAND",
            "DEPLOY_CONTAINER",
            "ESCAPE_TO_HOST",
            "CONTAINER_AND_RESOURCE_DISCOVERY",
            "REFLECTIVE_CODE_LOADING",
            "STEAL_OR_FORGE_AUTHENTICATION_CERTIFICATES",
            "FINANCIAL_THEFT",
        ]
    ]
    primaryTactic: typing.Literal[
        "TACTIC_UNSPECIFIED",
        "RECONNAISSANCE",
        "RESOURCE_DEVELOPMENT",
        "INITIAL_ACCESS",
        "EXECUTION",
        "PERSISTENCE",
        "PRIVILEGE_ESCALATION",
        "DEFENSE_EVASION",
        "CREDENTIAL_ACCESS",
        "DISCOVERY",
        "LATERAL_MOVEMENT",
        "COLLECTION",
        "COMMAND_AND_CONTROL",
        "EXFILTRATION",
        "IMPACT",
    ]
    primaryTechniques: _list[
        typing.Literal[
            "TECHNIQUE_UNSPECIFIED",
            "DATA_OBFUSCATION",
            "DATA_OBFUSCATION_STEGANOGRAPHY",
            "OS_CREDENTIAL_DUMPING",
            "OS_CREDENTIAL_DUMPING_PROC_FILESYSTEM",
            "OS_CREDENTIAL_DUMPING_ETC_PASSWORD_AND_ETC_SHADOW",
            "DATA_FROM_LOCAL_SYSTEM",
            "AUTOMATED_EXFILTRATION",
            "OBFUSCATED_FILES_OR_INFO",
            "STEGANOGRAPHY",
            "COMPILE_AFTER_DELIVERY",
            "COMMAND_OBFUSCATION",
            "SCHEDULED_TRANSFER",
            "SYSTEM_OWNER_USER_DISCOVERY",
            "MASQUERADING",
            "MATCH_LEGITIMATE_NAME_OR_LOCATION",
            "BOOT_OR_LOGON_INITIALIZATION_SCRIPTS",
            "STARTUP_ITEMS",
            "NETWORK_SERVICE_DISCOVERY",
            "SCHEDULED_TASK_JOB",
            "SCHEDULED_TASK_JOB_CRON",
            "CONTAINER_ORCHESTRATION_JOB",
            "PROCESS_INJECTION",
            "INPUT_CAPTURE",
            "INPUT_CAPTURE_KEYLOGGING",
            "PROCESS_DISCOVERY",
            "COMMAND_AND_SCRIPTING_INTERPRETER",
            "UNIX_SHELL",
            "PYTHON",
            "EXPLOITATION_FOR_PRIVILEGE_ESCALATION",
            "PERMISSION_GROUPS_DISCOVERY",
            "CLOUD_GROUPS",
            "INDICATOR_REMOVAL",
            "INDICATOR_REMOVAL_CLEAR_LINUX_OR_MAC_SYSTEM_LOGS",
            "INDICATOR_REMOVAL_CLEAR_COMMAND_HISTORY",
            "INDICATOR_REMOVAL_FILE_DELETION",
            "INDICATOR_REMOVAL_TIMESTOMP",
            "INDICATOR_REMOVAL_CLEAR_MAILBOX_DATA",
            "APPLICATION_LAYER_PROTOCOL",
            "DNS",
            "SOFTWARE_DEPLOYMENT_TOOLS",
            "VALID_ACCOUNTS",
            "DEFAULT_ACCOUNTS",
            "LOCAL_ACCOUNTS",
            "CLOUD_ACCOUNTS",
            "FILE_AND_DIRECTORY_DISCOVERY",
            "ACCOUNT_DISCOVERY_LOCAL_ACCOUNT",
            "PROXY",
            "EXTERNAL_PROXY",
            "MULTI_HOP_PROXY",
            "ACCOUNT_MANIPULATION",
            "ADDITIONAL_CLOUD_CREDENTIALS",
            "ADDITIONAL_CLOUD_ROLES",
            "SSH_AUTHORIZED_KEYS",
            "ADDITIONAL_CONTAINER_CLUSTER_ROLES",
            "MULTI_STAGE_CHANNELS",
            "INGRESS_TOOL_TRANSFER",
            "NATIVE_API",
            "BRUTE_FORCE",
            "AUTOMATED_COLLECTION",
            "SHARED_MODULES",
            "DATA_ENCODING",
            "STANDARD_ENCODING",
            "ACCESS_TOKEN_MANIPULATION",
            "TOKEN_IMPERSONATION_OR_THEFT",
            "CREATE_ACCOUNT",
            "LOCAL_ACCOUNT",
            "DEOBFUSCATE_DECODE_FILES_OR_INFO",
            "EXPLOIT_PUBLIC_FACING_APPLICATION",
            "SUPPLY_CHAIN_COMPROMISE",
            "COMPROMISE_SOFTWARE_DEPENDENCIES_AND_DEVELOPMENT_TOOLS",
            "EXPLOITATION_FOR_CLIENT_EXECUTION",
            "USER_EXECUTION",
            "EXPLOITATION_FOR_CREDENTIAL_ACCESS",
            "LINUX_AND_MAC_FILE_AND_DIRECTORY_PERMISSIONS_MODIFICATION",
            "DOMAIN_POLICY_MODIFICATION",
            "DATA_DESTRUCTION",
            "DATA_ENCRYPTED_FOR_IMPACT",
            "SERVICE_STOP",
            "INHIBIT_SYSTEM_RECOVERY",
            "FIRMWARE_CORRUPTION",
            "RESOURCE_HIJACKING",
            "NETWORK_DENIAL_OF_SERVICE",
            "CLOUD_SERVICE_DISCOVERY",
            "STEAL_APPLICATION_ACCESS_TOKEN",
            "ACCOUNT_ACCESS_REMOVAL",
            "TRANSFER_DATA_TO_CLOUD_ACCOUNT",
            "STEAL_WEB_SESSION_COOKIE",
            "CREATE_OR_MODIFY_SYSTEM_PROCESS",
            "EVENT_TRIGGERED_EXECUTION",
            "BOOT_OR_LOGON_AUTOSTART_EXECUTION",
            "KERNEL_MODULES_AND_EXTENSIONS",
            "SHORTCUT_MODIFICATION",
            "ABUSE_ELEVATION_CONTROL_MECHANISM",
            "ABUSE_ELEVATION_CONTROL_MECHANISM_SETUID_AND_SETGID",
            "ABUSE_ELEVATION_CONTROL_MECHANISM_SUDO_AND_SUDO_CACHING",
            "UNSECURED_CREDENTIALS",
            "CREDENTIALS_IN_FILES",
            "BASH_HISTORY",
            "PRIVATE_KEYS",
            "SUBVERT_TRUST_CONTROL",
            "INSTALL_ROOT_CERTIFICATE",
            "COMPROMISE_HOST_SOFTWARE_BINARY",
            "CREDENTIALS_FROM_PASSWORD_STORES",
            "MODIFY_AUTHENTICATION_PROCESS",
            "PLUGGABLE_AUTHENTICATION_MODULES",
            "MULTI_FACTOR_AUTHENTICATION",
            "IMPAIR_DEFENSES",
            "DISABLE_OR_MODIFY_TOOLS",
            "INDICATOR_BLOCKING",
            "DISABLE_OR_MODIFY_LINUX_AUDIT_SYSTEM",
            "HIDE_ARTIFACTS",
            "HIDDEN_FILES_AND_DIRECTORIES",
            "HIDDEN_USERS",
            "EXFILTRATION_OVER_WEB_SERVICE",
            "EXFILTRATION_TO_CLOUD_STORAGE",
            "DYNAMIC_RESOLUTION",
            "LATERAL_TOOL_TRANSFER",
            "HIJACK_EXECUTION_FLOW",
            "HIJACK_EXECUTION_FLOW_DYNAMIC_LINKER_HIJACKING",
            "MODIFY_CLOUD_COMPUTE_INFRASTRUCTURE",
            "CREATE_SNAPSHOT",
            "CLOUD_INFRASTRUCTURE_DISCOVERY",
            "DEVELOP_CAPABILITIES",
            "DEVELOP_CAPABILITIES_MALWARE",
            "OBTAIN_CAPABILITIES",
            "OBTAIN_CAPABILITIES_MALWARE",
            "OBTAIN_CAPABILITIES_VULNERABILITIES",
            "ACTIVE_SCANNING",
            "SCANNING_IP_BLOCKS",
            "STAGE_CAPABILITIES",
            "UPLOAD_MALWARE",
            "CONTAINER_ADMINISTRATION_COMMAND",
            "DEPLOY_CONTAINER",
            "ESCAPE_TO_HOST",
            "CONTAINER_AND_RESOURCE_DISCOVERY",
            "REFLECTIVE_CODE_LOADING",
            "STEAL_OR_FORGE_AUTHENTICATION_CERTIFICATES",
            "FINANCIAL_THEFT",
        ]
    ]
    version: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2MuteConfig(typing.TypedDict, total=False):
    createTime: str
    cryptoKeyName: str
    description: str
    expiryTime: str
    filter: str
    mostRecentEditor: str
    name: str
    type: typing.Literal["MUTE_CONFIG_TYPE_UNSPECIFIED", "STATIC", "DYNAMIC"]
    updateTime: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2MuteInfo(typing.TypedDict, total=False):
    dynamicMuteRecords: _list[GoogleCloudSecuritycenterV2DynamicMuteRecord]
    staticMute: GoogleCloudSecuritycenterV2StaticMute

@typing.type_check_only
class GoogleCloudSecuritycenterV2Network(typing.TypedDict, total=False):
    name: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2Node(typing.TypedDict, total=False):
    name: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2NodePool(typing.TypedDict, total=False):
    name: str
    nodes: _list[GoogleCloudSecuritycenterV2Node]

@typing.type_check_only
class GoogleCloudSecuritycenterV2Notebook(typing.TypedDict, total=False):
    lastAuthor: str
    name: str
    notebookUpdateTime: str
    service: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2NotificationMessage(typing.TypedDict, total=False):
    finding: GoogleCloudSecuritycenterV2Finding
    notificationConfigName: str
    resource: GoogleCloudSecuritycenterV2Resource

@typing.type_check_only
class GoogleCloudSecuritycenterV2Object(typing.TypedDict, total=False):
    containers: _list[GoogleCloudSecuritycenterV2Container]
    group: str
    kind: str
    name: str
    ns: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2OrgPolicy(typing.TypedDict, total=False):
    name: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2Package(typing.TypedDict, total=False):
    cpeUri: str
    packageName: str
    packageType: str
    packageVersion: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2Pipeline(typing.TypedDict, total=False):
    displayName: str
    name: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2Pod(typing.TypedDict, total=False):
    containers: _list[GoogleCloudSecuritycenterV2Container]
    labels: _list[GoogleCloudSecuritycenterV2Label]
    name: str
    ns: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2PolicyDriftDetails(typing.TypedDict, total=False):
    detectedValue: str
    expectedValue: str
    field: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2PolicyViolationSummary(typing.TypedDict, total=False):
    conformantResourcesCount: str
    evaluationErrorsCount: str
    outOfScopeResourcesCount: str
    policyViolationsCount: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2PortRange(typing.TypedDict, total=False):
    max: str
    min: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2Process(typing.TypedDict, total=False):
    args: _list[str]
    argumentsTruncated: bool
    binary: GoogleCloudSecuritycenterV2File
    envVariables: _list[GoogleCloudSecuritycenterV2EnvironmentVariable]
    envVariablesTruncated: bool
    libraries: _list[GoogleCloudSecuritycenterV2File]
    name: str
    parentPid: str
    pid: str
    script: GoogleCloudSecuritycenterV2File
    userId: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2ProcessSignature(typing.TypedDict, total=False):
    memoryHashSignature: GoogleCloudSecuritycenterV2MemoryHashSignature
    signatureType: typing.Literal[
        "SIGNATURE_TYPE_UNSPECIFIED", "SIGNATURE_TYPE_PROCESS", "SIGNATURE_TYPE_FILE"
    ]
    yaraRuleSignature: GoogleCloudSecuritycenterV2YaraRuleSignature

@typing.type_check_only
class GoogleCloudSecuritycenterV2Reference(typing.TypedDict, total=False):
    source: str
    uri: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2Requests(typing.TypedDict, total=False):
    longTermAllowed: int
    longTermDenied: int
    ratio: float
    shortTermAllowed: int

@typing.type_check_only
class GoogleCloudSecuritycenterV2Resource(typing.TypedDict, total=False):
    adcApplication: GoogleCloudSecuritycenterV2AdcApplication
    adcApplicationTemplate: GoogleCloudSecuritycenterV2AdcApplicationTemplateRevision
    adcSharedTemplate: GoogleCloudSecuritycenterV2AdcSharedTemplateRevision
    application: GoogleCloudSecuritycenterV2ResourceApplication
    awsMetadata: GoogleCloudSecuritycenterV2AwsMetadata
    azureMetadata: GoogleCloudSecuritycenterV2AzureMetadata
    cloudProvider: typing.Literal[
        "CLOUD_PROVIDER_UNSPECIFIED",
        "GOOGLE_CLOUD_PLATFORM",
        "AMAZON_WEB_SERVICES",
        "MICROSOFT_AZURE",
    ]
    displayName: str
    gcpMetadata: GcpMetadata
    location: str
    name: str
    resourcePath: GoogleCloudSecuritycenterV2ResourcePath
    resourcePathString: str
    service: str
    type: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2ResourceApplication(typing.TypedDict, total=False):
    attributes: GoogleCloudSecuritycenterV2ResourceApplicationAttributes
    name: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2ResourceApplicationAttributes(
    typing.TypedDict, total=False
):
    businessOwners: _list[
        GoogleCloudSecuritycenterV2ResourceApplicationAttributesContactInfo
    ]
    criticality: GoogleCloudSecuritycenterV2ResourceApplicationAttributesCriticality
    developerOwners: _list[
        GoogleCloudSecuritycenterV2ResourceApplicationAttributesContactInfo
    ]
    environment: GoogleCloudSecuritycenterV2ResourceApplicationAttributesEnvironment
    operatorOwners: _list[
        GoogleCloudSecuritycenterV2ResourceApplicationAttributesContactInfo
    ]

@typing.type_check_only
class GoogleCloudSecuritycenterV2ResourceApplicationAttributesContactInfo(
    typing.TypedDict, total=False
):
    email: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2ResourceApplicationAttributesCriticality(
    typing.TypedDict, total=False
):
    type: typing.Literal[
        "CRITICALITY_TYPE_UNSPECIFIED", "MISSION_CRITICAL", "HIGH", "MEDIUM", "LOW"
    ]

@typing.type_check_only
class GoogleCloudSecuritycenterV2ResourceApplicationAttributesEnvironment(
    typing.TypedDict, total=False
):
    type: typing.Literal[
        "ENVIRONMENT_TYPE_UNSPECIFIED", "PRODUCTION", "STAGING", "TEST", "DEVELOPMENT"
    ]

@typing.type_check_only
class GoogleCloudSecuritycenterV2ResourcePath(typing.TypedDict, total=False):
    nodes: _list[GoogleCloudSecuritycenterV2ResourcePathNode]

@typing.type_check_only
class GoogleCloudSecuritycenterV2ResourcePathNode(typing.TypedDict, total=False):
    displayName: str
    id: str
    nodeType: typing.Literal[
        "RESOURCE_PATH_NODE_TYPE_UNSPECIFIED",
        "GCP_ORGANIZATION",
        "GCP_FOLDER",
        "GCP_PROJECT",
        "AWS_ORGANIZATION",
        "AWS_ORGANIZATIONAL_UNIT",
        "AWS_ACCOUNT",
        "AZURE_MANAGEMENT_GROUP",
        "AZURE_SUBSCRIPTION",
        "AZURE_RESOURCE_GROUP",
    ]

@typing.type_check_only
class GoogleCloudSecuritycenterV2ResourceValueConfig(typing.TypedDict, total=False):
    cloudProvider: typing.Literal[
        "CLOUD_PROVIDER_UNSPECIFIED",
        "GOOGLE_CLOUD_PLATFORM",
        "AMAZON_WEB_SERVICES",
        "MICROSOFT_AZURE",
    ]
    createTime: str
    description: str
    name: str
    resourceLabelsSelector: dict[str, typing.Any]
    resourceType: str
    resourceValue: typing.Literal[
        "RESOURCE_VALUE_UNSPECIFIED", "HIGH", "MEDIUM", "LOW", "NONE"
    ]
    scope: str
    sensitiveDataProtectionMapping: (
        GoogleCloudSecuritycenterV2SensitiveDataProtectionMapping
    )
    tagValues: _list[str]
    updateTime: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2Role(typing.TypedDict, total=False):
    kind: typing.Literal["KIND_UNSPECIFIED", "ROLE", "CLUSTER_ROLE"]
    name: str
    ns: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2Secret(typing.TypedDict, total=False):
    environmentVariable: GoogleCloudSecuritycenterV2SecretEnvironmentVariable
    filePath: GoogleCloudSecuritycenterV2SecretFilePath
    status: GoogleCloudSecuritycenterV2SecretStatus
    type: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2SecretEnvironmentVariable(
    typing.TypedDict, total=False
):
    key: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2SecretFilePath(typing.TypedDict, total=False):
    path: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2SecretStatus(typing.TypedDict, total=False):
    lastUpdatedTime: str
    validity: typing.Literal[
        "SECRET_VALIDITY_UNSPECIFIED",
        "SECRET_VALIDITY_UNSUPPORTED",
        "SECRET_VALIDITY_FAILED",
        "SECRET_VALIDITY_INVALID",
        "SECRET_VALIDITY_VALID",
    ]

@typing.type_check_only
class GoogleCloudSecuritycenterV2SecurityBulletin(typing.TypedDict, total=False):
    bulletinId: str
    submissionTime: str
    suggestedUpgradeVersion: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2SecurityMarks(typing.TypedDict, total=False):
    canonicalName: str
    marks: dict[str, typing.Any]
    name: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2SecurityPolicy(typing.TypedDict, total=False):
    name: str
    preview: bool
    type: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2SecurityPosture(typing.TypedDict, total=False):
    changedPolicy: str
    name: str
    policy: str
    policyDriftDetails: _list[GoogleCloudSecuritycenterV2PolicyDriftDetails]
    policySet: str
    postureDeployment: str
    postureDeploymentResource: str
    revisionId: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2SensitiveDataProtectionMapping(
    typing.TypedDict, total=False
):
    highSensitivityMapping: typing.Literal[
        "RESOURCE_VALUE_UNSPECIFIED", "HIGH", "MEDIUM", "LOW", "NONE"
    ]
    mediumSensitivityMapping: typing.Literal[
        "RESOURCE_VALUE_UNSPECIFIED", "HIGH", "MEDIUM", "LOW", "NONE"
    ]

@typing.type_check_only
class GoogleCloudSecuritycenterV2SensitivityScore(typing.TypedDict, total=False):
    score: typing.Literal[
        "SENSITIVITY_SCORE_LEVEL_UNSPECIFIED",
        "SENSITIVITY_LOW",
        "SENSITIVITY_UNKNOWN",
        "SENSITIVITY_MODERATE",
        "SENSITIVITY_HIGH",
    ]

@typing.type_check_only
class GoogleCloudSecuritycenterV2ServiceAccountDelegationInfo(
    typing.TypedDict, total=False
):
    principalEmail: str
    principalSubject: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2StaticMute(typing.TypedDict, total=False):
    applyTime: str
    state: typing.Literal["MUTE_UNSPECIFIED", "MUTED", "UNMUTED", "UNDEFINED"]

@typing.type_check_only
class GoogleCloudSecuritycenterV2Subject(typing.TypedDict, total=False):
    kind: typing.Literal["AUTH_TYPE_UNSPECIFIED", "USER", "SERVICEACCOUNT", "GROUP"]
    name: str
    ns: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2TicketInfo(typing.TypedDict, total=False):
    assignee: str
    description: str
    id: str
    status: str
    updateTime: str
    uri: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2ToxicCombination(typing.TypedDict, total=False):
    attackExposureScore: float
    relatedFindings: _list[str]

@typing.type_check_only
class GoogleCloudSecuritycenterV2VertexAi(typing.TypedDict, total=False):
    datasets: _list[GoogleCloudSecuritycenterV2Dataset]
    pipelines: _list[GoogleCloudSecuritycenterV2Pipeline]

@typing.type_check_only
class GoogleCloudSecuritycenterV2Vulnerability(typing.TypedDict, total=False):
    cve: GoogleCloudSecuritycenterV2Cve
    cwes: _list[GoogleCloudSecuritycenterV2Cwe]
    fixedPackage: GoogleCloudSecuritycenterV2Package
    offendingPackage: GoogleCloudSecuritycenterV2Package
    providerRiskScore: str
    reachable: bool
    securityBulletin: GoogleCloudSecuritycenterV2SecurityBulletin

@typing.type_check_only
class GoogleCloudSecuritycenterV2YaraRuleSignature(typing.TypedDict, total=False):
    yaraRule: str

@typing.type_check_only
class GroupAssetsRequest(typing.TypedDict, total=False):
    compareDuration: str
    filter: str
    groupBy: str
    pageSize: int
    pageToken: str
    readTime: str

@typing.type_check_only
class GroupAssetsResponse(typing.TypedDict, total=False):
    groupByResults: _list[GroupResult]
    nextPageToken: str
    readTime: str

@typing.type_check_only
class GroupFindingsRequest(typing.TypedDict, total=False):
    filter: str
    groupBy: str
    pageSize: int
    pageToken: str
    readTime: str

@typing.type_check_only
class GroupFindingsResponse(typing.TypedDict, total=False):
    groupByResults: _list[GroupResult]
    nextPageToken: str
    readTime: str

@typing.type_check_only
class GroupMembership(typing.TypedDict, total=False):
    groupId: str
    groupType: typing.Literal[
        "GROUP_TYPE_UNSPECIFIED",
        "GROUP_TYPE_TOXIC_COMBINATION",
        "GROUP_TYPE_CHOKEPOINT",
    ]

@typing.type_check_only
class GroupResult(typing.TypedDict, total=False):
    count: str
    properties: dict[str, typing.Any]

@typing.type_check_only
class HttpResponse(typing.TypedDict, total=False):
    path: str
    statusCode: str

@typing.type_check_only
class IamBinding(typing.TypedDict, total=False):
    action: typing.Literal["ACTION_UNSPECIFIED", "ADD", "REMOVE"]
    member: str
    role: str

@typing.type_check_only
class Indicator(typing.TypedDict, total=False):
    domains: _list[str]
    ipAddresses: _list[str]
    signatures: _list[ProcessSignature]
    uris: _list[str]

@typing.type_check_only
class InfoType(typing.TypedDict, total=False):
    name: str
    sensitivityScore: SensitivityScore
    version: str

@typing.type_check_only
class InvocationReference(typing.TypedDict, total=False):
    invocationId: str

@typing.type_check_only
class IpRule(typing.TypedDict, total=False):
    portRanges: _list[PortRange]
    protocol: str

@typing.type_check_only
class IpRules(typing.TypedDict, total=False):
    allowed: Allowed
    denied: Denied
    destinationIpRanges: _list[str]
    direction: typing.Literal["DIRECTION_UNSPECIFIED", "INGRESS", "EGRESS"]
    exposedServices: _list[str]
    sourceIpRanges: _list[str]

@typing.type_check_only
class Job(typing.TypedDict, total=False):
    errorCode: int
    location: str
    name: str
    state: typing.Literal[
        "JOB_STATE_UNSPECIFIED", "PENDING", "RUNNING", "SUCCEEDED", "FAILED"
    ]

@typing.type_check_only
class KernelRootkit(typing.TypedDict, total=False):
    name: str
    unexpectedCodeModification: bool
    unexpectedFtraceHandler: bool
    unexpectedInterruptHandler: bool
    unexpectedKernelCodePages: bool
    unexpectedKprobeHandler: bool
    unexpectedProcessesInRunqueue: bool
    unexpectedReadOnlyDataModification: bool
    unexpectedSystemCallHandler: bool

@typing.type_check_only
class Kubernetes(typing.TypedDict, total=False):
    accessReviews: _list[AccessReview]
    bindings: _list[GoogleCloudSecuritycenterV1Binding]
    nodePools: _list[NodePool]
    nodes: _list[Node]
    objects: _list[Object]
    pods: _list[Pod]
    roles: _list[Role]

@typing.type_check_only
class Label(typing.TypedDict, total=False):
    name: str
    value: str

@typing.type_check_only
class ListAssetsResponse(typing.TypedDict, total=False):
    listAssetsResults: _list[ListAssetsResult]
    nextPageToken: str
    readTime: str
    totalSize: int

@typing.type_check_only
class ListAssetsResult(typing.TypedDict, total=False):
    asset: Asset
    state: typing.Literal["STATE_UNSPECIFIED", "UNUSED", "ADDED", "REMOVED", "ACTIVE"]

@typing.type_check_only
class ListFindingsResponse(typing.TypedDict, total=False):
    findings: _list[GoogleCloudSecuritycenterV1beta1Finding]
    nextPageToken: str
    readTime: str
    totalSize: int

@typing.type_check_only
class ListOperationsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    operations: _list[Operation]
    unreachable: _list[str]

@typing.type_check_only
class ListSourcesResponse(typing.TypedDict, total=False):
    nextPageToken: str
    sources: _list[Source]

@typing.type_check_only
class LoadBalancer(typing.TypedDict, total=False):
    name: str

@typing.type_check_only
class LogEntry(typing.TypedDict, total=False):
    cloudLoggingEntry: CloudLoggingEntry

@typing.type_check_only
class MemoryHashSignature(typing.TypedDict, total=False):
    binaryFamily: str
    detections: _list[Detection]

@typing.type_check_only
class MitreAttack(typing.TypedDict, total=False):
    additionalTactics: _list[
        typing.Literal[
            "TACTIC_UNSPECIFIED",
            "RECONNAISSANCE",
            "RESOURCE_DEVELOPMENT",
            "INITIAL_ACCESS",
            "EXECUTION",
            "PERSISTENCE",
            "PRIVILEGE_ESCALATION",
            "DEFENSE_EVASION",
            "CREDENTIAL_ACCESS",
            "DISCOVERY",
            "LATERAL_MOVEMENT",
            "COLLECTION",
            "COMMAND_AND_CONTROL",
            "EXFILTRATION",
            "IMPACT",
        ]
    ]
    additionalTechniques: _list[
        typing.Literal[
            "TECHNIQUE_UNSPECIFIED",
            "DATA_OBFUSCATION",
            "DATA_OBFUSCATION_STEGANOGRAPHY",
            "OS_CREDENTIAL_DUMPING",
            "OS_CREDENTIAL_DUMPING_PROC_FILESYSTEM",
            "OS_CREDENTIAL_DUMPING_ETC_PASSWORD_AND_ETC_SHADOW",
            "DATA_FROM_LOCAL_SYSTEM",
            "AUTOMATED_EXFILTRATION",
            "OBFUSCATED_FILES_OR_INFO",
            "STEGANOGRAPHY",
            "COMPILE_AFTER_DELIVERY",
            "COMMAND_OBFUSCATION",
            "SCHEDULED_TRANSFER",
            "SYSTEM_OWNER_USER_DISCOVERY",
            "MASQUERADING",
            "MATCH_LEGITIMATE_NAME_OR_LOCATION",
            "BOOT_OR_LOGON_INITIALIZATION_SCRIPTS",
            "STARTUP_ITEMS",
            "NETWORK_SERVICE_DISCOVERY",
            "SCHEDULED_TASK_JOB",
            "SCHEDULED_TASK_JOB_CRON",
            "CONTAINER_ORCHESTRATION_JOB",
            "PROCESS_INJECTION",
            "INPUT_CAPTURE",
            "INPUT_CAPTURE_KEYLOGGING",
            "PROCESS_DISCOVERY",
            "COMMAND_AND_SCRIPTING_INTERPRETER",
            "UNIX_SHELL",
            "PYTHON",
            "EXPLOITATION_FOR_PRIVILEGE_ESCALATION",
            "PERMISSION_GROUPS_DISCOVERY",
            "CLOUD_GROUPS",
            "INDICATOR_REMOVAL",
            "INDICATOR_REMOVAL_CLEAR_LINUX_OR_MAC_SYSTEM_LOGS",
            "INDICATOR_REMOVAL_CLEAR_COMMAND_HISTORY",
            "INDICATOR_REMOVAL_FILE_DELETION",
            "INDICATOR_REMOVAL_TIMESTOMP",
            "INDICATOR_REMOVAL_CLEAR_MAILBOX_DATA",
            "APPLICATION_LAYER_PROTOCOL",
            "DNS",
            "SOFTWARE_DEPLOYMENT_TOOLS",
            "VALID_ACCOUNTS",
            "DEFAULT_ACCOUNTS",
            "LOCAL_ACCOUNTS",
            "CLOUD_ACCOUNTS",
            "FILE_AND_DIRECTORY_DISCOVERY",
            "ACCOUNT_DISCOVERY_LOCAL_ACCOUNT",
            "PROXY",
            "EXTERNAL_PROXY",
            "MULTI_HOP_PROXY",
            "ACCOUNT_MANIPULATION",
            "ADDITIONAL_CLOUD_CREDENTIALS",
            "ADDITIONAL_CLOUD_ROLES",
            "SSH_AUTHORIZED_KEYS",
            "ADDITIONAL_CONTAINER_CLUSTER_ROLES",
            "MULTI_STAGE_CHANNELS",
            "INGRESS_TOOL_TRANSFER",
            "NATIVE_API",
            "BRUTE_FORCE",
            "AUTOMATED_COLLECTION",
            "SHARED_MODULES",
            "DATA_ENCODING",
            "STANDARD_ENCODING",
            "ACCESS_TOKEN_MANIPULATION",
            "TOKEN_IMPERSONATION_OR_THEFT",
            "CREATE_ACCOUNT",
            "LOCAL_ACCOUNT",
            "DEOBFUSCATE_DECODE_FILES_OR_INFO",
            "EXPLOIT_PUBLIC_FACING_APPLICATION",
            "SUPPLY_CHAIN_COMPROMISE",
            "COMPROMISE_SOFTWARE_DEPENDENCIES_AND_DEVELOPMENT_TOOLS",
            "EXPLOITATION_FOR_CLIENT_EXECUTION",
            "USER_EXECUTION",
            "EXPLOITATION_FOR_CREDENTIAL_ACCESS",
            "LINUX_AND_MAC_FILE_AND_DIRECTORY_PERMISSIONS_MODIFICATION",
            "DOMAIN_POLICY_MODIFICATION",
            "DATA_DESTRUCTION",
            "DATA_ENCRYPTED_FOR_IMPACT",
            "SERVICE_STOP",
            "INHIBIT_SYSTEM_RECOVERY",
            "FIRMWARE_CORRUPTION",
            "RESOURCE_HIJACKING",
            "NETWORK_DENIAL_OF_SERVICE",
            "CLOUD_SERVICE_DISCOVERY",
            "STEAL_APPLICATION_ACCESS_TOKEN",
            "ACCOUNT_ACCESS_REMOVAL",
            "TRANSFER_DATA_TO_CLOUD_ACCOUNT",
            "STEAL_WEB_SESSION_COOKIE",
            "CREATE_OR_MODIFY_SYSTEM_PROCESS",
            "EVENT_TRIGGERED_EXECUTION",
            "BOOT_OR_LOGON_AUTOSTART_EXECUTION",
            "KERNEL_MODULES_AND_EXTENSIONS",
            "SHORTCUT_MODIFICATION",
            "ABUSE_ELEVATION_CONTROL_MECHANISM",
            "ABUSE_ELEVATION_CONTROL_MECHANISM_SETUID_AND_SETGID",
            "ABUSE_ELEVATION_CONTROL_MECHANISM_SUDO_AND_SUDO_CACHING",
            "UNSECURED_CREDENTIALS",
            "CREDENTIALS_IN_FILES",
            "BASH_HISTORY",
            "PRIVATE_KEYS",
            "SUBVERT_TRUST_CONTROL",
            "INSTALL_ROOT_CERTIFICATE",
            "COMPROMISE_HOST_SOFTWARE_BINARY",
            "CREDENTIALS_FROM_PASSWORD_STORES",
            "MODIFY_AUTHENTICATION_PROCESS",
            "PLUGGABLE_AUTHENTICATION_MODULES",
            "MULTI_FACTOR_AUTHENTICATION",
            "IMPAIR_DEFENSES",
            "DISABLE_OR_MODIFY_TOOLS",
            "INDICATOR_BLOCKING",
            "DISABLE_OR_MODIFY_LINUX_AUDIT_SYSTEM",
            "HIDE_ARTIFACTS",
            "HIDDEN_FILES_AND_DIRECTORIES",
            "HIDDEN_USERS",
            "EXFILTRATION_OVER_WEB_SERVICE",
            "EXFILTRATION_TO_CLOUD_STORAGE",
            "DYNAMIC_RESOLUTION",
            "LATERAL_TOOL_TRANSFER",
            "HIJACK_EXECUTION_FLOW",
            "HIJACK_EXECUTION_FLOW_DYNAMIC_LINKER_HIJACKING",
            "MODIFY_CLOUD_COMPUTE_INFRASTRUCTURE",
            "CREATE_SNAPSHOT",
            "CLOUD_INFRASTRUCTURE_DISCOVERY",
            "DEVELOP_CAPABILITIES",
            "DEVELOP_CAPABILITIES_MALWARE",
            "OBTAIN_CAPABILITIES",
            "OBTAIN_CAPABILITIES_MALWARE",
            "OBTAIN_CAPABILITIES_VULNERABILITIES",
            "ACTIVE_SCANNING",
            "SCANNING_IP_BLOCKS",
            "STAGE_CAPABILITIES",
            "UPLOAD_MALWARE",
            "CONTAINER_ADMINISTRATION_COMMAND",
            "DEPLOY_CONTAINER",
            "ESCAPE_TO_HOST",
            "CONTAINER_AND_RESOURCE_DISCOVERY",
            "REFLECTIVE_CODE_LOADING",
            "STEAL_OR_FORGE_AUTHENTICATION_CERTIFICATES",
            "FINANCIAL_THEFT",
        ]
    ]
    primaryTactic: typing.Literal[
        "TACTIC_UNSPECIFIED",
        "RECONNAISSANCE",
        "RESOURCE_DEVELOPMENT",
        "INITIAL_ACCESS",
        "EXECUTION",
        "PERSISTENCE",
        "PRIVILEGE_ESCALATION",
        "DEFENSE_EVASION",
        "CREDENTIAL_ACCESS",
        "DISCOVERY",
        "LATERAL_MOVEMENT",
        "COLLECTION",
        "COMMAND_AND_CONTROL",
        "EXFILTRATION",
        "IMPACT",
    ]
    primaryTechniques: _list[
        typing.Literal[
            "TECHNIQUE_UNSPECIFIED",
            "DATA_OBFUSCATION",
            "DATA_OBFUSCATION_STEGANOGRAPHY",
            "OS_CREDENTIAL_DUMPING",
            "OS_CREDENTIAL_DUMPING_PROC_FILESYSTEM",
            "OS_CREDENTIAL_DUMPING_ETC_PASSWORD_AND_ETC_SHADOW",
            "DATA_FROM_LOCAL_SYSTEM",
            "AUTOMATED_EXFILTRATION",
            "OBFUSCATED_FILES_OR_INFO",
            "STEGANOGRAPHY",
            "COMPILE_AFTER_DELIVERY",
            "COMMAND_OBFUSCATION",
            "SCHEDULED_TRANSFER",
            "SYSTEM_OWNER_USER_DISCOVERY",
            "MASQUERADING",
            "MATCH_LEGITIMATE_NAME_OR_LOCATION",
            "BOOT_OR_LOGON_INITIALIZATION_SCRIPTS",
            "STARTUP_ITEMS",
            "NETWORK_SERVICE_DISCOVERY",
            "SCHEDULED_TASK_JOB",
            "SCHEDULED_TASK_JOB_CRON",
            "CONTAINER_ORCHESTRATION_JOB",
            "PROCESS_INJECTION",
            "INPUT_CAPTURE",
            "INPUT_CAPTURE_KEYLOGGING",
            "PROCESS_DISCOVERY",
            "COMMAND_AND_SCRIPTING_INTERPRETER",
            "UNIX_SHELL",
            "PYTHON",
            "EXPLOITATION_FOR_PRIVILEGE_ESCALATION",
            "PERMISSION_GROUPS_DISCOVERY",
            "CLOUD_GROUPS",
            "INDICATOR_REMOVAL",
            "INDICATOR_REMOVAL_CLEAR_LINUX_OR_MAC_SYSTEM_LOGS",
            "INDICATOR_REMOVAL_CLEAR_COMMAND_HISTORY",
            "INDICATOR_REMOVAL_FILE_DELETION",
            "INDICATOR_REMOVAL_TIMESTOMP",
            "INDICATOR_REMOVAL_CLEAR_MAILBOX_DATA",
            "APPLICATION_LAYER_PROTOCOL",
            "DNS",
            "SOFTWARE_DEPLOYMENT_TOOLS",
            "VALID_ACCOUNTS",
            "DEFAULT_ACCOUNTS",
            "LOCAL_ACCOUNTS",
            "CLOUD_ACCOUNTS",
            "FILE_AND_DIRECTORY_DISCOVERY",
            "ACCOUNT_DISCOVERY_LOCAL_ACCOUNT",
            "PROXY",
            "EXTERNAL_PROXY",
            "MULTI_HOP_PROXY",
            "ACCOUNT_MANIPULATION",
            "ADDITIONAL_CLOUD_CREDENTIALS",
            "ADDITIONAL_CLOUD_ROLES",
            "SSH_AUTHORIZED_KEYS",
            "ADDITIONAL_CONTAINER_CLUSTER_ROLES",
            "MULTI_STAGE_CHANNELS",
            "INGRESS_TOOL_TRANSFER",
            "NATIVE_API",
            "BRUTE_FORCE",
            "AUTOMATED_COLLECTION",
            "SHARED_MODULES",
            "DATA_ENCODING",
            "STANDARD_ENCODING",
            "ACCESS_TOKEN_MANIPULATION",
            "TOKEN_IMPERSONATION_OR_THEFT",
            "CREATE_ACCOUNT",
            "LOCAL_ACCOUNT",
            "DEOBFUSCATE_DECODE_FILES_OR_INFO",
            "EXPLOIT_PUBLIC_FACING_APPLICATION",
            "SUPPLY_CHAIN_COMPROMISE",
            "COMPROMISE_SOFTWARE_DEPENDENCIES_AND_DEVELOPMENT_TOOLS",
            "EXPLOITATION_FOR_CLIENT_EXECUTION",
            "USER_EXECUTION",
            "EXPLOITATION_FOR_CREDENTIAL_ACCESS",
            "LINUX_AND_MAC_FILE_AND_DIRECTORY_PERMISSIONS_MODIFICATION",
            "DOMAIN_POLICY_MODIFICATION",
            "DATA_DESTRUCTION",
            "DATA_ENCRYPTED_FOR_IMPACT",
            "SERVICE_STOP",
            "INHIBIT_SYSTEM_RECOVERY",
            "FIRMWARE_CORRUPTION",
            "RESOURCE_HIJACKING",
            "NETWORK_DENIAL_OF_SERVICE",
            "CLOUD_SERVICE_DISCOVERY",
            "STEAL_APPLICATION_ACCESS_TOKEN",
            "ACCOUNT_ACCESS_REMOVAL",
            "TRANSFER_DATA_TO_CLOUD_ACCOUNT",
            "STEAL_WEB_SESSION_COOKIE",
            "CREATE_OR_MODIFY_SYSTEM_PROCESS",
            "EVENT_TRIGGERED_EXECUTION",
            "BOOT_OR_LOGON_AUTOSTART_EXECUTION",
            "KERNEL_MODULES_AND_EXTENSIONS",
            "SHORTCUT_MODIFICATION",
            "ABUSE_ELEVATION_CONTROL_MECHANISM",
            "ABUSE_ELEVATION_CONTROL_MECHANISM_SETUID_AND_SETGID",
            "ABUSE_ELEVATION_CONTROL_MECHANISM_SUDO_AND_SUDO_CACHING",
            "UNSECURED_CREDENTIALS",
            "CREDENTIALS_IN_FILES",
            "BASH_HISTORY",
            "PRIVATE_KEYS",
            "SUBVERT_TRUST_CONTROL",
            "INSTALL_ROOT_CERTIFICATE",
            "COMPROMISE_HOST_SOFTWARE_BINARY",
            "CREDENTIALS_FROM_PASSWORD_STORES",
            "MODIFY_AUTHENTICATION_PROCESS",
            "PLUGGABLE_AUTHENTICATION_MODULES",
            "MULTI_FACTOR_AUTHENTICATION",
            "IMPAIR_DEFENSES",
            "DISABLE_OR_MODIFY_TOOLS",
            "INDICATOR_BLOCKING",
            "DISABLE_OR_MODIFY_LINUX_AUDIT_SYSTEM",
            "HIDE_ARTIFACTS",
            "HIDDEN_FILES_AND_DIRECTORIES",
            "HIDDEN_USERS",
            "EXFILTRATION_OVER_WEB_SERVICE",
            "EXFILTRATION_TO_CLOUD_STORAGE",
            "DYNAMIC_RESOLUTION",
            "LATERAL_TOOL_TRANSFER",
            "HIJACK_EXECUTION_FLOW",
            "HIJACK_EXECUTION_FLOW_DYNAMIC_LINKER_HIJACKING",
            "MODIFY_CLOUD_COMPUTE_INFRASTRUCTURE",
            "CREATE_SNAPSHOT",
            "CLOUD_INFRASTRUCTURE_DISCOVERY",
            "DEVELOP_CAPABILITIES",
            "DEVELOP_CAPABILITIES_MALWARE",
            "OBTAIN_CAPABILITIES",
            "OBTAIN_CAPABILITIES_MALWARE",
            "OBTAIN_CAPABILITIES_VULNERABILITIES",
            "ACTIVE_SCANNING",
            "SCANNING_IP_BLOCKS",
            "STAGE_CAPABILITIES",
            "UPLOAD_MALWARE",
            "CONTAINER_ADMINISTRATION_COMMAND",
            "DEPLOY_CONTAINER",
            "ESCAPE_TO_HOST",
            "CONTAINER_AND_RESOURCE_DISCOVERY",
            "REFLECTIVE_CODE_LOADING",
            "STEAL_OR_FORGE_AUTHENTICATION_CERTIFICATES",
            "FINANCIAL_THEFT",
        ]
    ]
    version: str

@typing.type_check_only
class MuteInfo(typing.TypedDict, total=False):
    dynamicMuteRecords: _list[DynamicMuteRecord]
    staticMute: StaticMute

@typing.type_check_only
class Network(typing.TypedDict, total=False):
    name: str

@typing.type_check_only
class Node(typing.TypedDict, total=False):
    name: str

@typing.type_check_only
class NodePool(typing.TypedDict, total=False):
    name: str
    nodes: _list[Node]

@typing.type_check_only
class Notebook(typing.TypedDict, total=False):
    lastAuthor: str
    name: str
    notebookUpdateTime: str
    service: str

@typing.type_check_only
class Object(typing.TypedDict, total=False):
    containers: _list[Container]
    group: str
    kind: str
    name: str
    ns: str

@typing.type_check_only
class Operation(typing.TypedDict, total=False):
    done: bool
    error: Status
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class OrgPolicy(typing.TypedDict, total=False):
    name: str

@typing.type_check_only
class OrganizationSettings(typing.TypedDict, total=False):
    assetDiscoveryConfig: AssetDiscoveryConfig
    enableAssetDiscovery: bool
    name: str

@typing.type_check_only
class Package(typing.TypedDict, total=False):
    cpeUri: str
    packageName: str
    packageType: str
    packageVersion: str

@typing.type_check_only
class Pipeline(typing.TypedDict, total=False):
    displayName: str
    name: str

@typing.type_check_only
class Pod(typing.TypedDict, total=False):
    containers: _list[Container]
    labels: _list[Label]
    name: str
    ns: str

@typing.type_check_only
class Policy(typing.TypedDict, total=False):
    auditConfigs: _list[AuditConfig]
    bindings: _list[Binding]
    etag: str
    version: int

@typing.type_check_only
class PolicyDriftDetails(typing.TypedDict, total=False):
    detectedValue: str
    expectedValue: str
    field: str

@typing.type_check_only
class PolicyViolationSummary(typing.TypedDict, total=False):
    conformantResourcesCount: str
    evaluationErrorsCount: str
    outOfScopeResourcesCount: str
    policyViolationsCount: str

@typing.type_check_only
class PortRange(typing.TypedDict, total=False):
    max: str
    min: str

@typing.type_check_only
class Process(typing.TypedDict, total=False):
    args: _list[str]
    argumentsTruncated: bool
    binary: File
    envVariables: _list[EnvironmentVariable]
    envVariablesTruncated: bool
    libraries: _list[File]
    name: str
    parentPid: str
    pid: str
    script: File
    userId: str

@typing.type_check_only
class ProcessSignature(typing.TypedDict, total=False):
    memoryHashSignature: MemoryHashSignature
    signatureType: typing.Literal[
        "SIGNATURE_TYPE_UNSPECIFIED", "SIGNATURE_TYPE_PROCESS", "SIGNATURE_TYPE_FILE"
    ]
    yaraRuleSignature: YaraRuleSignature

@typing.type_check_only
class Reference(typing.TypedDict, total=False):
    source: str
    uri: str

@typing.type_check_only
class Requests(typing.TypedDict, total=False):
    longTermAllowed: int
    longTermDenied: int
    ratio: float
    shortTermAllowed: int

@typing.type_check_only
class ResourcePath(typing.TypedDict, total=False):
    nodes: _list[ResourcePathNode]

@typing.type_check_only
class ResourcePathNode(typing.TypedDict, total=False):
    displayName: str
    id: str
    nodeType: typing.Literal[
        "RESOURCE_PATH_NODE_TYPE_UNSPECIFIED",
        "GCP_ORGANIZATION",
        "GCP_FOLDER",
        "GCP_PROJECT",
        "AWS_ORGANIZATION",
        "AWS_ORGANIZATIONAL_UNIT",
        "AWS_ACCOUNT",
        "AZURE_MANAGEMENT_GROUP",
        "AZURE_SUBSCRIPTION",
        "AZURE_RESOURCE_GROUP",
    ]

@typing.type_check_only
class Role(typing.TypedDict, total=False):
    kind: typing.Literal["KIND_UNSPECIFIED", "ROLE", "CLUSTER_ROLE"]
    name: str
    ns: str

@typing.type_check_only
class RunAssetDiscoveryRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class Secret(typing.TypedDict, total=False):
    environmentVariable: SecretEnvironmentVariable
    filePath: SecretFilePath
    status: SecretStatus
    type: str

@typing.type_check_only
class SecretEnvironmentVariable(typing.TypedDict, total=False):
    key: str

@typing.type_check_only
class SecretFilePath(typing.TypedDict, total=False):
    path: str

@typing.type_check_only
class SecretStatus(typing.TypedDict, total=False):
    lastUpdatedTime: str
    validity: typing.Literal[
        "SECRET_VALIDITY_UNSPECIFIED",
        "SECRET_VALIDITY_UNSUPPORTED",
        "SECRET_VALIDITY_FAILED",
        "SECRET_VALIDITY_INVALID",
        "SECRET_VALIDITY_VALID",
    ]

@typing.type_check_only
class SecurityBulletin(typing.TypedDict, total=False):
    bulletinId: str
    submissionTime: str
    suggestedUpgradeVersion: str

@typing.type_check_only
class SecurityCenterProperties(typing.TypedDict, total=False):
    resourceName: str
    resourceOwners: _list[str]
    resourceParent: str
    resourceProject: str
    resourceType: str

@typing.type_check_only
class SecurityMarks(typing.TypedDict, total=False):
    canonicalName: str
    marks: dict[str, typing.Any]
    name: str

@typing.type_check_only
class SecurityPolicy(typing.TypedDict, total=False):
    name: str
    preview: bool
    type: str

@typing.type_check_only
class SecurityPosture(typing.TypedDict, total=False):
    changedPolicy: str
    name: str
    policy: str
    policyDriftDetails: _list[PolicyDriftDetails]
    policySet: str
    postureDeployment: str
    postureDeploymentResource: str
    revisionId: str

@typing.type_check_only
class SensitivityScore(typing.TypedDict, total=False):
    score: typing.Literal[
        "SENSITIVITY_SCORE_LEVEL_UNSPECIFIED",
        "SENSITIVITY_LOW",
        "SENSITIVITY_UNKNOWN",
        "SENSITIVITY_MODERATE",
        "SENSITIVITY_HIGH",
    ]

@typing.type_check_only
class ServiceAccountDelegationInfo(typing.TypedDict, total=False):
    principalEmail: str
    principalSubject: str

@typing.type_check_only
class SetFindingStateRequest(typing.TypedDict, total=False):
    startTime: str
    state: typing.Literal["STATE_UNSPECIFIED", "ACTIVE", "INACTIVE"]

@typing.type_check_only
class SetIamPolicyRequest(typing.TypedDict, total=False):
    policy: Policy
    updateMask: str

@typing.type_check_only
class Source(typing.TypedDict, total=False):
    description: str
    displayName: str
    name: str

@typing.type_check_only
class StaticMute(typing.TypedDict, total=False):
    applyTime: str
    state: typing.Literal["MUTE_UNSPECIFIED", "MUTED", "UNMUTED", "UNDEFINED"]

@typing.type_check_only
class Status(typing.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class Subject(typing.TypedDict, total=False):
    kind: typing.Literal["AUTH_TYPE_UNSPECIFIED", "USER", "SERVICEACCOUNT", "GROUP"]
    name: str
    ns: str

@typing.type_check_only
class TestIamPermissionsRequest(typing.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class TestIamPermissionsResponse(typing.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class TicketInfo(typing.TypedDict, total=False):
    assignee: str
    description: str
    id: str
    status: str
    updateTime: str
    uri: str

@typing.type_check_only
class ToxicCombination(typing.TypedDict, total=False):
    attackExposureScore: float
    relatedFindings: _list[str]

@typing.type_check_only
class VertexAi(typing.TypedDict, total=False):
    datasets: _list[Dataset]
    pipelines: _list[Pipeline]

@typing.type_check_only
class Vulnerability(typing.TypedDict, total=False):
    cve: Cve
    cwes: _list[Cwe]
    fixedPackage: Package
    offendingPackage: Package
    providerRiskScore: str
    reachable: bool
    securityBulletin: SecurityBulletin

@typing.type_check_only
class VulnerabilityCountBySeverity(typing.TypedDict, total=False):
    severityToFindingCount: dict[str, typing.Any]

@typing.type_check_only
class VulnerabilitySnapshot(typing.TypedDict, total=False):
    cloudProvider: typing.Literal[
        "CLOUD_PROVIDER_UNSPECIFIED",
        "GOOGLE_CLOUD_PLATFORM",
        "AMAZON_WEB_SERVICES",
        "MICROSOFT_AZURE",
    ]
    findingCount: VulnerabilityCountBySeverity
    name: str
    snapshotTime: str

@typing.type_check_only
class YaraRuleSignature(typing.TypedDict, total=False):
    yaraRule: str
