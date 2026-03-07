import typing

import typing_extensions

_list = list

@typing.type_check_only
class Access(typing_extensions.TypedDict, total=False):
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
class AccessReview(typing_extensions.TypedDict, total=False):
    group: str
    name: str
    ns: str
    resource: str
    subresource: str
    verb: str
    version: str

@typing.type_check_only
class AdaptiveProtection(typing_extensions.TypedDict, total=False):
    confidence: float

@typing.type_check_only
class AdcApplication(typing_extensions.TypedDict, total=False):
    attributes: GoogleCloudSecuritycenterV1ResourceApplicationAttributes
    name: str

@typing.type_check_only
class AdcApplicationTemplateRevision(typing_extensions.TypedDict, total=False):
    name: str

@typing.type_check_only
class AdcSharedTemplateRevision(typing_extensions.TypedDict, total=False):
    name: str

@typing.type_check_only
class AffectedResources(typing_extensions.TypedDict, total=False):
    count: str

@typing.type_check_only
class AiModel(typing_extensions.TypedDict, total=False):
    deploymentPlatform: typing_extensions.Literal[
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
class Allowed(typing_extensions.TypedDict, total=False):
    ipRules: _list[IpRule]

@typing.type_check_only
class Application(typing_extensions.TypedDict, total=False):
    baseUri: str
    fullUri: str

@typing.type_check_only
class ArtifactGuardPolicies(typing_extensions.TypedDict, total=False):
    failingPolicies: _list[ArtifactGuardPolicy]
    resourceId: str

@typing.type_check_only
class ArtifactGuardPolicy(typing_extensions.TypedDict, total=False):
    failureReason: str
    policyId: str
    type: typing_extensions.Literal[
        "ARTIFACT_GUARD_POLICY_TYPE_UNSPECIFIED", "VULNERABILITY"
    ]

@typing.type_check_only
class Attack(typing_extensions.TypedDict, total=False):
    classification: str
    volumeBps: int
    volumeBpsLong: str
    volumePps: int
    volumePpsLong: str

@typing.type_check_only
class AttackExposure(typing_extensions.TypedDict, total=False):
    attackExposureResult: str
    exposedHighValueResourcesCount: int
    exposedLowValueResourcesCount: int
    exposedMediumValueResourcesCount: int
    latestCalculationTime: str
    score: float
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "CALCULATED", "NOT_CALCULATED"
    ]

@typing.type_check_only
class AwsAccount(typing_extensions.TypedDict, total=False):
    id: str
    name: str

@typing.type_check_only
class AwsMetadata(typing_extensions.TypedDict, total=False):
    account: AwsAccount
    organization: AwsOrganization
    organizationalUnits: _list[AwsOrganizationalUnit]

@typing.type_check_only
class AwsOrganization(typing_extensions.TypedDict, total=False):
    id: str

@typing.type_check_only
class AwsOrganizationalUnit(typing_extensions.TypedDict, total=False):
    id: str
    name: str

@typing.type_check_only
class AzureManagementGroup(typing_extensions.TypedDict, total=False):
    displayName: str
    id: str

@typing.type_check_only
class AzureMetadata(typing_extensions.TypedDict, total=False):
    managementGroups: _list[AzureManagementGroup]
    resourceGroup: AzureResourceGroup
    subscription: AzureSubscription
    tenant: AzureTenant

@typing.type_check_only
class AzureResourceGroup(typing_extensions.TypedDict, total=False):
    id: str
    name: str

@typing.type_check_only
class AzureSubscription(typing_extensions.TypedDict, total=False):
    displayName: str
    id: str

@typing.type_check_only
class AzureTenant(typing_extensions.TypedDict, total=False):
    displayName: str
    id: str

@typing.type_check_only
class BackupDisasterRecovery(typing_extensions.TypedDict, total=False):
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
class BigQueryDestination(typing_extensions.TypedDict, total=False):
    dataset: str

@typing.type_check_only
class Chokepoint(typing_extensions.TypedDict, total=False):
    relatedFindings: _list[str]

@typing.type_check_only
class CloudArmor(typing_extensions.TypedDict, total=False):
    adaptiveProtection: AdaptiveProtection
    attack: Attack
    duration: str
    requests: Requests
    securityPolicy: SecurityPolicy
    threatVector: str

@typing.type_check_only
class CloudControl(typing_extensions.TypedDict, total=False):
    cloudControlName: str
    policyType: str
    type: typing_extensions.Literal[
        "CLOUD_CONTROL_TYPE_UNSPECIFIED", "BUILT_IN", "CUSTOM"
    ]
    version: int

@typing.type_check_only
class CloudDlpDataProfile(typing_extensions.TypedDict, total=False):
    dataProfile: str
    infoTypes: _list[InfoType]
    parentType: typing_extensions.Literal[
        "PARENT_TYPE_UNSPECIFIED", "ORGANIZATION", "PROJECT"
    ]

@typing.type_check_only
class CloudDlpInspection(typing_extensions.TypedDict, total=False):
    fullScan: bool
    infoType: str
    infoTypeCount: str
    inspectJob: str

@typing.type_check_only
class CloudLoggingEntry(typing_extensions.TypedDict, total=False):
    insertId: str
    logId: str
    resourceContainer: str
    timestamp: str

@typing.type_check_only
class Compliance(typing_extensions.TypedDict, total=False):
    ids: _list[str]
    standard: str
    version: str

@typing.type_check_only
class ComplianceDetails(typing_extensions.TypedDict, total=False):
    cloudControl: CloudControl
    cloudControlDeploymentNames: _list[str]
    frameworks: _list[Framework]

@typing.type_check_only
class Config(typing_extensions.TypedDict, total=False):
    moduleEnablementState: typing_extensions.Literal[
        "ENABLEMENT_STATE_UNSPECIFIED", "INHERITED", "ENABLED", "DISABLED"
    ]
    value: dict[str, typing.Any]

@typing.type_check_only
class Connection(typing_extensions.TypedDict, total=False):
    destinationIp: str
    destinationPort: int
    protocol: typing_extensions.Literal[
        "PROTOCOL_UNSPECIFIED", "ICMP", "TCP", "UDP", "GRE", "ESP"
    ]
    sourceIp: str
    sourcePort: int

@typing.type_check_only
class Contact(typing_extensions.TypedDict, total=False):
    email: str

@typing.type_check_only
class ContactDetails(typing_extensions.TypedDict, total=False):
    contacts: _list[Contact]

@typing.type_check_only
class Container(typing_extensions.TypedDict, total=False):
    createTime: str
    imageId: str
    labels: _list[Label]
    name: str
    uri: str

@typing.type_check_only
class ContainerThreatDetectionSettings(typing_extensions.TypedDict, total=False):
    modules: dict[str, typing.Any]
    name: str
    serviceAccount: str
    serviceEnablementState: typing_extensions.Literal[
        "ENABLEMENT_STATE_UNSPECIFIED", "INHERITED", "ENABLED", "DISABLED"
    ]
    updateTime: str

@typing.type_check_only
class Control(typing_extensions.TypedDict, total=False):
    controlName: str
    displayName: str

@typing.type_check_only
class Cve(typing_extensions.TypedDict, total=False):
    cvssv3: Cvssv3
    exploitReleaseDate: str
    exploitationActivity: typing_extensions.Literal[
        "EXPLOITATION_ACTIVITY_UNSPECIFIED",
        "WIDE",
        "CONFIRMED",
        "AVAILABLE",
        "ANTICIPATED",
        "NO_KNOWN",
    ]
    firstExploitationDate: str
    id: str
    impact: typing_extensions.Literal[
        "RISK_RATING_UNSPECIFIED", "LOW", "MEDIUM", "HIGH", "CRITICAL"
    ]
    observedInTheWild: bool
    references: _list[Reference]
    upstreamFixAvailable: bool
    zeroDay: bool

@typing.type_check_only
class Cvssv3(typing_extensions.TypedDict, total=False):
    attackComplexity: typing_extensions.Literal[
        "ATTACK_COMPLEXITY_UNSPECIFIED",
        "ATTACK_COMPLEXITY_LOW",
        "ATTACK_COMPLEXITY_HIGH",
    ]
    attackVector: typing_extensions.Literal[
        "ATTACK_VECTOR_UNSPECIFIED",
        "ATTACK_VECTOR_NETWORK",
        "ATTACK_VECTOR_ADJACENT",
        "ATTACK_VECTOR_LOCAL",
        "ATTACK_VECTOR_PHYSICAL",
    ]
    availabilityImpact: typing_extensions.Literal[
        "IMPACT_UNSPECIFIED", "IMPACT_HIGH", "IMPACT_LOW", "IMPACT_NONE"
    ]
    baseScore: float
    confidentialityImpact: typing_extensions.Literal[
        "IMPACT_UNSPECIFIED", "IMPACT_HIGH", "IMPACT_LOW", "IMPACT_NONE"
    ]
    integrityImpact: typing_extensions.Literal[
        "IMPACT_UNSPECIFIED", "IMPACT_HIGH", "IMPACT_LOW", "IMPACT_NONE"
    ]
    privilegesRequired: typing_extensions.Literal[
        "PRIVILEGES_REQUIRED_UNSPECIFIED",
        "PRIVILEGES_REQUIRED_NONE",
        "PRIVILEGES_REQUIRED_LOW",
        "PRIVILEGES_REQUIRED_HIGH",
    ]
    scope: typing_extensions.Literal[
        "SCOPE_UNSPECIFIED", "SCOPE_UNCHANGED", "SCOPE_CHANGED"
    ]
    userInteraction: typing_extensions.Literal[
        "USER_INTERACTION_UNSPECIFIED",
        "USER_INTERACTION_NONE",
        "USER_INTERACTION_REQUIRED",
    ]

@typing.type_check_only
class Cwe(typing_extensions.TypedDict, total=False):
    id: str
    references: _list[Reference]

@typing.type_check_only
class DataAccessEvent(typing_extensions.TypedDict, total=False):
    eventId: str
    eventTime: str
    operation: typing_extensions.Literal[
        "OPERATION_UNSPECIFIED", "READ", "MOVE", "COPY"
    ]
    principalEmail: str

@typing.type_check_only
class DataFlowEvent(typing_extensions.TypedDict, total=False):
    eventId: str
    eventTime: str
    operation: typing_extensions.Literal[
        "OPERATION_UNSPECIFIED", "READ", "MOVE", "COPY"
    ]
    principalEmail: str
    violatedLocation: str

@typing.type_check_only
class DataRetentionDeletionEvent(typing_extensions.TypedDict, total=False):
    dataObjectCount: str
    eventDetectionTime: str
    eventType: typing_extensions.Literal[
        "EVENT_TYPE_UNSPECIFIED",
        "EVENT_TYPE_MAX_TTL_EXCEEDED",
        "EVENT_TYPE_MAX_TTL_FROM_CREATION",
        "EVENT_TYPE_MAX_TTL_FROM_LAST_MODIFICATION",
    ]
    maxRetentionAllowed: str

@typing.type_check_only
class Database(typing_extensions.TypedDict, total=False):
    displayName: str
    grantees: _list[str]
    name: str
    query: str
    userName: str
    version: str

@typing.type_check_only
class Dataset(typing_extensions.TypedDict, total=False):
    displayName: str
    name: str
    source: str

@typing.type_check_only
class Denied(typing_extensions.TypedDict, total=False):
    ipRules: _list[IpRule]

@typing.type_check_only
class Details(typing_extensions.TypedDict, total=False):
    endTime: str
    startTime: str
    type: typing_extensions.Literal[
        "TYPE_UNSPECIFIED", "STANDARD", "TRIAL", "ALPHA", "DEMO", "PAY_AS_YOU_GO"
    ]

@typing.type_check_only
class Detection(typing_extensions.TypedDict, total=False):
    binary: str
    percentPagesMatched: float

@typing.type_check_only
class Disk(typing_extensions.TypedDict, total=False):
    name: str

@typing.type_check_only
class DiskPath(typing_extensions.TypedDict, total=False):
    partitionUuid: str
    relativePath: str

@typing.type_check_only
class DynamicMuteRecord(typing_extensions.TypedDict, total=False):
    matchTime: str
    muteConfig: str

@typing.type_check_only
class EnvironmentVariable(typing_extensions.TypedDict, total=False):
    name: str
    val: str

@typing.type_check_only
class EventThreatDetectionSettings(typing_extensions.TypedDict, total=False):
    modules: dict[str, typing.Any]
    name: str
    serviceEnablementState: typing_extensions.Literal[
        "ENABLEMENT_STATE_UNSPECIFIED", "INHERITED", "ENABLED", "DISABLED"
    ]
    updateTime: str

@typing.type_check_only
class ExfilResource(typing_extensions.TypedDict, total=False):
    components: _list[str]
    name: str

@typing.type_check_only
class Exfiltration(typing_extensions.TypedDict, total=False):
    sources: _list[ExfilResource]
    targets: _list[ExfilResource]
    totalExfiltratedBytes: str

@typing.type_check_only
class ExportFindingsMetadata(typing_extensions.TypedDict, total=False):
    bigQueryDestination: BigQueryDestination
    exportStartTime: str

@typing.type_check_only
class ExportFindingsResponse(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Expr(typing_extensions.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str

@typing.type_check_only
class ExternalExposure(typing_extensions.TypedDict, total=False):
    backendService: str
    exposedEndpoint: str
    exposedService: str
    forwardingRule: str
    instanceGroup: str
    loadBalancerFirewallPolicy: str
    networkEndpointGroup: str
    privateIpAddress: str
    privatePort: str
    publicIpAddress: str
    publicPort: str
    serviceFirewallPolicy: str

@typing.type_check_only
class File(typing_extensions.TypedDict, total=False):
    contents: str
    diskPath: DiskPath
    fileLoadState: typing_extensions.Literal[
        "FILE_LOAD_STATE_UNSPECIFIED", "LOADED_BY_PROCESS", "NOT_LOADED_BY_PROCESS"
    ]
    hashedSize: str
    operations: _list[FileOperation]
    partiallyHashed: bool
    path: str
    sha256: str
    size: str

@typing.type_check_only
class FileOperation(typing_extensions.TypedDict, total=False):
    type: typing_extensions.Literal[
        "OPERATION_TYPE_UNSPECIFIED", "OPEN", "READ", "RENAME", "WRITE", "EXECUTE"
    ]

@typing.type_check_only
class Finding(typing_extensions.TypedDict, total=False):
    access: Access
    affectedResources: AffectedResources
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
    disk: Disk
    eventTime: str
    exfiltration: Exfiltration
    externalExposure: ExternalExposure
    externalSystems: dict[str, typing.Any]
    externalUri: str
    files: _list[File]
    findingClass: typing_extensions.Literal[
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
    ]
    groupMemberships: _list[GroupMembership]
    iamBindings: _list[IamBinding]
    indicator: Indicator
    ipRules: IpRules
    job: Job
    kernelRootkit: KernelRootkit
    kubernetes: Kubernetes
    loadBalancers: _list[LoadBalancer]
    logEntries: _list[LogEntry]
    mitreAttack: MitreAttack
    moduleName: str
    mute: typing_extensions.Literal["MUTE_UNSPECIFIED", "MUTED", "UNMUTED", "UNDEFINED"]
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
    processes: _list[Process]
    resourceName: str
    secret: Secret
    securityMarks: SecurityMarks
    securityPosture: SecurityPosture
    severity: typing_extensions.Literal[
        "SEVERITY_UNSPECIFIED", "CRITICAL", "HIGH", "MEDIUM", "LOW"
    ]
    sourceProperties: dict[str, typing.Any]
    state: typing_extensions.Literal["STATE_UNSPECIFIED", "ACTIVE", "INACTIVE"]
    toxicCombination: ToxicCombination
    vertexAi: VertexAi
    vulnerability: Vulnerability

@typing.type_check_only
class Folder(typing_extensions.TypedDict, total=False):
    resourceFolder: str
    resourceFolderDisplayName: str

@typing.type_check_only
class Framework(typing_extensions.TypedDict, total=False):
    category: _list[
        typing_extensions.Literal[
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
    type: typing_extensions.Literal[
        "FRAMEWORK_TYPE_UNSPECIFIED", "FRAMEWORK_TYPE_BUILT_IN", "FRAMEWORK_TYPE_CUSTOM"
    ]

@typing.type_check_only
class GcpMetadata(typing_extensions.TypedDict, total=False):
    folders: _list[GoogleCloudSecuritycenterV2Folder]
    organization: str
    parent: str
    parentDisplayName: str
    project: str
    projectDisplayName: str

@typing.type_check_only
class Geolocation(typing_extensions.TypedDict, total=False):
    regionCode: str

@typing.type_check_only
class GoogleCloudSecuritycenterV1BigQueryExport(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    dataset: str
    description: str
    filter: str
    mostRecentEditor: str
    name: str
    principal: str
    updateTime: str

@typing.type_check_only
class GoogleCloudSecuritycenterV1Binding(typing_extensions.TypedDict, total=False):
    name: str
    ns: str
    role: Role
    subjects: _list[Subject]

@typing.type_check_only
class GoogleCloudSecuritycenterV1BulkMuteFindingsResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudSecuritycenterV1CustomConfig(typing_extensions.TypedDict, total=False):
    customOutput: GoogleCloudSecuritycenterV1CustomOutputSpec
    description: str
    predicate: Expr
    recommendation: str
    resourceSelector: GoogleCloudSecuritycenterV1ResourceSelector
    severity: typing_extensions.Literal[
        "SEVERITY_UNSPECIFIED", "CRITICAL", "HIGH", "MEDIUM", "LOW"
    ]

@typing.type_check_only
class GoogleCloudSecuritycenterV1CustomOutputSpec(
    typing_extensions.TypedDict, total=False
):
    properties: _list[GoogleCloudSecuritycenterV1Property]

@typing.type_check_only
class GoogleCloudSecuritycenterV1EffectiveSecurityHealthAnalyticsCustomModule(
    typing_extensions.TypedDict, total=False
):
    cloudProvider: typing_extensions.Literal[
        "CLOUD_PROVIDER_UNSPECIFIED",
        "GOOGLE_CLOUD_PLATFORM",
        "AMAZON_WEB_SERVICES",
        "MICROSOFT_AZURE",
    ]
    customConfig: GoogleCloudSecuritycenterV1CustomConfig
    displayName: str
    enablementState: typing_extensions.Literal[
        "ENABLEMENT_STATE_UNSPECIFIED", "ENABLED", "DISABLED"
    ]
    name: str

@typing.type_check_only
class GoogleCloudSecuritycenterV1ExternalSystem(
    typing_extensions.TypedDict, total=False
):
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
class GoogleCloudSecuritycenterV1MuteConfig(typing_extensions.TypedDict, total=False):
    createTime: str
    description: str
    displayName: str
    expiryTime: str
    filter: str
    mostRecentEditor: str
    name: str
    type: typing_extensions.Literal["MUTE_CONFIG_TYPE_UNSPECIFIED", "STATIC", "DYNAMIC"]
    updateTime: str

@typing.type_check_only
class GoogleCloudSecuritycenterV1NotificationMessage(
    typing_extensions.TypedDict, total=False
):
    finding: Finding
    notificationConfigName: str
    resource: GoogleCloudSecuritycenterV1Resource

@typing.type_check_only
class GoogleCloudSecuritycenterV1Property(typing_extensions.TypedDict, total=False):
    name: str
    valueExpression: Expr

@typing.type_check_only
class GoogleCloudSecuritycenterV1Resource(typing_extensions.TypedDict, total=False):
    adcApplication: AdcApplication
    adcApplicationTemplate: AdcApplicationTemplateRevision
    adcSharedTemplate: AdcSharedTemplateRevision
    application: GoogleCloudSecuritycenterV1ResourceApplication
    awsMetadata: AwsMetadata
    azureMetadata: AzureMetadata
    cloudProvider: typing_extensions.Literal[
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
class GoogleCloudSecuritycenterV1ResourceApplication(
    typing_extensions.TypedDict, total=False
):
    attributes: GoogleCloudSecuritycenterV1ResourceApplicationAttributes
    name: str

@typing.type_check_only
class GoogleCloudSecuritycenterV1ResourceApplicationAttributes(
    typing_extensions.TypedDict, total=False
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
    typing_extensions.TypedDict, total=False
):
    email: str

@typing.type_check_only
class GoogleCloudSecuritycenterV1ResourceApplicationAttributesCriticality(
    typing_extensions.TypedDict, total=False
):
    type: typing_extensions.Literal[
        "CRITICALITY_TYPE_UNSPECIFIED", "MISSION_CRITICAL", "HIGH", "MEDIUM", "LOW"
    ]

@typing.type_check_only
class GoogleCloudSecuritycenterV1ResourceApplicationAttributesEnvironment(
    typing_extensions.TypedDict, total=False
):
    type: typing_extensions.Literal[
        "ENVIRONMENT_TYPE_UNSPECIFIED", "PRODUCTION", "STAGING", "TEST", "DEVELOPMENT"
    ]

@typing.type_check_only
class GoogleCloudSecuritycenterV1ResourceSelector(
    typing_extensions.TypedDict, total=False
):
    resourceTypes: _list[str]

@typing.type_check_only
class GoogleCloudSecuritycenterV1ResourceValueConfig(
    typing_extensions.TypedDict, total=False
):
    cloudProvider: typing_extensions.Literal[
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
    resourceValue: typing_extensions.Literal[
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
    typing_extensions.TypedDict, total=False
):
    duration: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "COMPLETED", "SUPERSEDED", "TERMINATED"
    ]

@typing.type_check_only
class GoogleCloudSecuritycenterV1SecurityHealthAnalyticsCustomModule(
    typing_extensions.TypedDict, total=False
):
    ancestorModule: str
    cloudProvider: typing_extensions.Literal[
        "CLOUD_PROVIDER_UNSPECIFIED",
        "GOOGLE_CLOUD_PLATFORM",
        "AMAZON_WEB_SERVICES",
        "MICROSOFT_AZURE",
    ]
    customConfig: GoogleCloudSecuritycenterV1CustomConfig
    displayName: str
    enablementState: typing_extensions.Literal[
        "ENABLEMENT_STATE_UNSPECIFIED", "ENABLED", "DISABLED", "INHERITED"
    ]
    lastEditor: str
    name: str
    updateTime: str

@typing.type_check_only
class GoogleCloudSecuritycenterV1SensitiveDataProtectionMapping(
    typing_extensions.TypedDict, total=False
):
    highSensitivityMapping: typing_extensions.Literal[
        "RESOURCE_VALUE_UNSPECIFIED", "HIGH", "MEDIUM", "LOW", "NONE"
    ]
    mediumSensitivityMapping: typing_extensions.Literal[
        "RESOURCE_VALUE_UNSPECIFIED", "HIGH", "MEDIUM", "LOW", "NONE"
    ]

@typing.type_check_only
class GoogleCloudSecuritycenterV1beta1RunAssetDiscoveryResponse(
    typing_extensions.TypedDict, total=False
):
    duration: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "COMPLETED", "SUPERSEDED", "TERMINATED"
    ]

@typing.type_check_only
class GoogleCloudSecuritycenterV1p1beta1Finding(
    typing_extensions.TypedDict, total=False
):
    canonicalName: str
    category: str
    createTime: str
    eventTime: str
    externalUri: str
    name: str
    parent: str
    resourceName: str
    securityMarks: GoogleCloudSecuritycenterV1p1beta1SecurityMarks
    severity: typing_extensions.Literal[
        "SEVERITY_UNSPECIFIED", "CRITICAL", "HIGH", "MEDIUM", "LOW"
    ]
    sourceProperties: dict[str, typing.Any]
    state: typing_extensions.Literal["STATE_UNSPECIFIED", "ACTIVE", "INACTIVE"]

@typing.type_check_only
class GoogleCloudSecuritycenterV1p1beta1Folder(
    typing_extensions.TypedDict, total=False
):
    resourceFolder: str
    resourceFolderDisplayName: str

@typing.type_check_only
class GoogleCloudSecuritycenterV1p1beta1NotificationMessage(
    typing_extensions.TypedDict, total=False
):
    finding: GoogleCloudSecuritycenterV1p1beta1Finding
    notificationConfigName: str
    resource: GoogleCloudSecuritycenterV1p1beta1Resource

@typing.type_check_only
class GoogleCloudSecuritycenterV1p1beta1Resource(
    typing_extensions.TypedDict, total=False
):
    folders: _list[GoogleCloudSecuritycenterV1p1beta1Folder]
    name: str
    parent: str
    parentDisplayName: str
    project: str
    projectDisplayName: str

@typing.type_check_only
class GoogleCloudSecuritycenterV1p1beta1RunAssetDiscoveryResponse(
    typing_extensions.TypedDict, total=False
):
    duration: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "COMPLETED", "SUPERSEDED", "TERMINATED"
    ]

@typing.type_check_only
class GoogleCloudSecuritycenterV1p1beta1SecurityMarks(
    typing_extensions.TypedDict, total=False
):
    canonicalName: str
    marks: dict[str, typing.Any]
    name: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2Access(typing_extensions.TypedDict, total=False):
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
class GoogleCloudSecuritycenterV2AccessReview(typing_extensions.TypedDict, total=False):
    group: str
    name: str
    ns: str
    resource: str
    subresource: str
    verb: str
    version: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2AdaptiveProtection(
    typing_extensions.TypedDict, total=False
):
    confidence: float

@typing.type_check_only
class GoogleCloudSecuritycenterV2AdcApplication(
    typing_extensions.TypedDict, total=False
):
    attributes: GoogleCloudSecuritycenterV2ResourceApplicationAttributes
    name: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2AdcApplicationTemplateRevision(
    typing_extensions.TypedDict, total=False
):
    name: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2AdcSharedTemplateRevision(
    typing_extensions.TypedDict, total=False
):
    name: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2AffectedResources(
    typing_extensions.TypedDict, total=False
):
    count: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2AiModel(typing_extensions.TypedDict, total=False):
    deploymentPlatform: typing_extensions.Literal[
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
class GoogleCloudSecuritycenterV2Allowed(typing_extensions.TypedDict, total=False):
    ipRules: _list[GoogleCloudSecuritycenterV2IpRule]

@typing.type_check_only
class GoogleCloudSecuritycenterV2Application(typing_extensions.TypedDict, total=False):
    baseUri: str
    fullUri: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2ArtifactGuardPolicies(
    typing_extensions.TypedDict, total=False
):
    failingPolicies: _list[GoogleCloudSecuritycenterV2ArtifactGuardPolicy]
    resourceId: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2ArtifactGuardPolicy(
    typing_extensions.TypedDict, total=False
):
    failureReason: str
    policyId: str
    type: typing_extensions.Literal[
        "ARTIFACT_GUARD_POLICY_TYPE_UNSPECIFIED", "VULNERABILITY"
    ]

@typing.type_check_only
class GoogleCloudSecuritycenterV2Attack(typing_extensions.TypedDict, total=False):
    classification: str
    volumeBps: int
    volumeBpsLong: str
    volumePps: int
    volumePpsLong: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2AttackExposure(
    typing_extensions.TypedDict, total=False
):
    attackExposureResult: str
    exposedHighValueResourcesCount: int
    exposedLowValueResourcesCount: int
    exposedMediumValueResourcesCount: int
    latestCalculationTime: str
    score: float
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "CALCULATED", "NOT_CALCULATED"
    ]

@typing.type_check_only
class GoogleCloudSecuritycenterV2AwsAccount(typing_extensions.TypedDict, total=False):
    id: str
    name: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2AwsMetadata(typing_extensions.TypedDict, total=False):
    account: GoogleCloudSecuritycenterV2AwsAccount
    organization: GoogleCloudSecuritycenterV2AwsOrganization
    organizationalUnits: _list[GoogleCloudSecuritycenterV2AwsOrganizationalUnit]

@typing.type_check_only
class GoogleCloudSecuritycenterV2AwsOrganization(
    typing_extensions.TypedDict, total=False
):
    id: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2AwsOrganizationalUnit(
    typing_extensions.TypedDict, total=False
):
    id: str
    name: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2AzureManagementGroup(
    typing_extensions.TypedDict, total=False
):
    displayName: str
    id: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2AzureMetadata(
    typing_extensions.TypedDict, total=False
):
    managementGroups: _list[GoogleCloudSecuritycenterV2AzureManagementGroup]
    resourceGroup: GoogleCloudSecuritycenterV2AzureResourceGroup
    subscription: GoogleCloudSecuritycenterV2AzureSubscription
    tenant: GoogleCloudSecuritycenterV2AzureTenant

@typing.type_check_only
class GoogleCloudSecuritycenterV2AzureResourceGroup(
    typing_extensions.TypedDict, total=False
):
    id: str
    name: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2AzureSubscription(
    typing_extensions.TypedDict, total=False
):
    displayName: str
    id: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2AzureTenant(typing_extensions.TypedDict, total=False):
    displayName: str
    id: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2BackupDisasterRecovery(
    typing_extensions.TypedDict, total=False
):
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
class GoogleCloudSecuritycenterV2BigQueryExport(
    typing_extensions.TypedDict, total=False
):
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
class GoogleCloudSecuritycenterV2Binding(typing_extensions.TypedDict, total=False):
    name: str
    ns: str
    role: GoogleCloudSecuritycenterV2Role
    subjects: _list[GoogleCloudSecuritycenterV2Subject]

@typing.type_check_only
class GoogleCloudSecuritycenterV2BulkMuteFindingsResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudSecuritycenterV2Chokepoint(typing_extensions.TypedDict, total=False):
    relatedFindings: _list[str]

@typing.type_check_only
class GoogleCloudSecuritycenterV2CloudArmor(typing_extensions.TypedDict, total=False):
    adaptiveProtection: GoogleCloudSecuritycenterV2AdaptiveProtection
    attack: GoogleCloudSecuritycenterV2Attack
    duration: str
    requests: GoogleCloudSecuritycenterV2Requests
    securityPolicy: GoogleCloudSecuritycenterV2SecurityPolicy
    threatVector: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2CloudControl(typing_extensions.TypedDict, total=False):
    cloudControlName: str
    policyType: str
    type: typing_extensions.Literal[
        "CLOUD_CONTROL_TYPE_UNSPECIFIED", "BUILT_IN", "CUSTOM"
    ]
    version: int

@typing.type_check_only
class GoogleCloudSecuritycenterV2CloudDlpDataProfile(
    typing_extensions.TypedDict, total=False
):
    dataProfile: str
    infoTypes: _list[GoogleCloudSecuritycenterV2InfoType]
    parentType: typing_extensions.Literal[
        "PARENT_TYPE_UNSPECIFIED", "ORGANIZATION", "PROJECT"
    ]

@typing.type_check_only
class GoogleCloudSecuritycenterV2CloudDlpInspection(
    typing_extensions.TypedDict, total=False
):
    fullScan: bool
    infoType: str
    infoTypeCount: str
    inspectJob: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2CloudLoggingEntry(
    typing_extensions.TypedDict, total=False
):
    insertId: str
    logId: str
    resourceContainer: str
    timestamp: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2Compliance(typing_extensions.TypedDict, total=False):
    ids: _list[str]
    standard: str
    version: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2ComplianceDetails(
    typing_extensions.TypedDict, total=False
):
    cloudControl: GoogleCloudSecuritycenterV2CloudControl
    cloudControlDeploymentNames: _list[str]
    frameworks: _list[GoogleCloudSecuritycenterV2Framework]

@typing.type_check_only
class GoogleCloudSecuritycenterV2Connection(typing_extensions.TypedDict, total=False):
    destinationIp: str
    destinationPort: int
    protocol: typing_extensions.Literal[
        "PROTOCOL_UNSPECIFIED", "ICMP", "TCP", "UDP", "GRE", "ESP"
    ]
    sourceIp: str
    sourcePort: int

@typing.type_check_only
class GoogleCloudSecuritycenterV2Contact(typing_extensions.TypedDict, total=False):
    email: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2ContactDetails(
    typing_extensions.TypedDict, total=False
):
    contacts: _list[GoogleCloudSecuritycenterV2Contact]

@typing.type_check_only
class GoogleCloudSecuritycenterV2Container(typing_extensions.TypedDict, total=False):
    createTime: str
    imageId: str
    labels: _list[GoogleCloudSecuritycenterV2Label]
    name: str
    uri: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2Control(typing_extensions.TypedDict, total=False):
    controlName: str
    displayName: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2Cve(typing_extensions.TypedDict, total=False):
    cvssv3: GoogleCloudSecuritycenterV2Cvssv3
    exploitReleaseDate: str
    exploitationActivity: typing_extensions.Literal[
        "EXPLOITATION_ACTIVITY_UNSPECIFIED",
        "WIDE",
        "CONFIRMED",
        "AVAILABLE",
        "ANTICIPATED",
        "NO_KNOWN",
    ]
    firstExploitationDate: str
    id: str
    impact: typing_extensions.Literal[
        "RISK_RATING_UNSPECIFIED", "LOW", "MEDIUM", "HIGH", "CRITICAL"
    ]
    observedInTheWild: bool
    references: _list[GoogleCloudSecuritycenterV2Reference]
    upstreamFixAvailable: bool
    zeroDay: bool

@typing.type_check_only
class GoogleCloudSecuritycenterV2Cvssv3(typing_extensions.TypedDict, total=False):
    attackComplexity: typing_extensions.Literal[
        "ATTACK_COMPLEXITY_UNSPECIFIED",
        "ATTACK_COMPLEXITY_LOW",
        "ATTACK_COMPLEXITY_HIGH",
    ]
    attackVector: typing_extensions.Literal[
        "ATTACK_VECTOR_UNSPECIFIED",
        "ATTACK_VECTOR_NETWORK",
        "ATTACK_VECTOR_ADJACENT",
        "ATTACK_VECTOR_LOCAL",
        "ATTACK_VECTOR_PHYSICAL",
    ]
    availabilityImpact: typing_extensions.Literal[
        "IMPACT_UNSPECIFIED", "IMPACT_HIGH", "IMPACT_LOW", "IMPACT_NONE"
    ]
    baseScore: float
    confidentialityImpact: typing_extensions.Literal[
        "IMPACT_UNSPECIFIED", "IMPACT_HIGH", "IMPACT_LOW", "IMPACT_NONE"
    ]
    integrityImpact: typing_extensions.Literal[
        "IMPACT_UNSPECIFIED", "IMPACT_HIGH", "IMPACT_LOW", "IMPACT_NONE"
    ]
    privilegesRequired: typing_extensions.Literal[
        "PRIVILEGES_REQUIRED_UNSPECIFIED",
        "PRIVILEGES_REQUIRED_NONE",
        "PRIVILEGES_REQUIRED_LOW",
        "PRIVILEGES_REQUIRED_HIGH",
    ]
    scope: typing_extensions.Literal[
        "SCOPE_UNSPECIFIED", "SCOPE_UNCHANGED", "SCOPE_CHANGED"
    ]
    userInteraction: typing_extensions.Literal[
        "USER_INTERACTION_UNSPECIFIED",
        "USER_INTERACTION_NONE",
        "USER_INTERACTION_REQUIRED",
    ]

@typing.type_check_only
class GoogleCloudSecuritycenterV2Cwe(typing_extensions.TypedDict, total=False):
    id: str
    references: _list[GoogleCloudSecuritycenterV2Reference]

@typing.type_check_only
class GoogleCloudSecuritycenterV2DataAccessEvent(
    typing_extensions.TypedDict, total=False
):
    eventId: str
    eventTime: str
    operation: typing_extensions.Literal[
        "OPERATION_UNSPECIFIED", "READ", "MOVE", "COPY"
    ]
    principalEmail: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2DataFlowEvent(
    typing_extensions.TypedDict, total=False
):
    eventId: str
    eventTime: str
    operation: typing_extensions.Literal[
        "OPERATION_UNSPECIFIED", "READ", "MOVE", "COPY"
    ]
    principalEmail: str
    violatedLocation: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2DataRetentionDeletionEvent(
    typing_extensions.TypedDict, total=False
):
    dataObjectCount: str
    eventDetectionTime: str
    eventType: typing_extensions.Literal[
        "EVENT_TYPE_UNSPECIFIED",
        "EVENT_TYPE_MAX_TTL_EXCEEDED",
        "EVENT_TYPE_MAX_TTL_FROM_CREATION",
        "EVENT_TYPE_MAX_TTL_FROM_LAST_MODIFICATION",
    ]
    maxRetentionAllowed: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2Database(typing_extensions.TypedDict, total=False):
    displayName: str
    grantees: _list[str]
    name: str
    query: str
    userName: str
    version: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2Dataset(typing_extensions.TypedDict, total=False):
    displayName: str
    name: str
    source: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2Denied(typing_extensions.TypedDict, total=False):
    ipRules: _list[GoogleCloudSecuritycenterV2IpRule]

@typing.type_check_only
class GoogleCloudSecuritycenterV2Detection(typing_extensions.TypedDict, total=False):
    binary: str
    percentPagesMatched: float

@typing.type_check_only
class GoogleCloudSecuritycenterV2Disk(typing_extensions.TypedDict, total=False):
    name: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2DiskPath(typing_extensions.TypedDict, total=False):
    partitionUuid: str
    relativePath: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2DynamicMuteRecord(
    typing_extensions.TypedDict, total=False
):
    matchTime: str
    muteConfig: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2EnvironmentVariable(
    typing_extensions.TypedDict, total=False
):
    name: str
    val: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2ExfilResource(
    typing_extensions.TypedDict, total=False
):
    components: _list[str]
    name: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2Exfiltration(typing_extensions.TypedDict, total=False):
    sources: _list[GoogleCloudSecuritycenterV2ExfilResource]
    targets: _list[GoogleCloudSecuritycenterV2ExfilResource]
    totalExfiltratedBytes: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2ExternalExposure(
    typing_extensions.TypedDict, total=False
):
    backendService: str
    exposedEndpoint: str
    exposedService: str
    forwardingRule: str
    instanceGroup: str
    loadBalancerFirewallPolicy: str
    networkEndpointGroup: str
    privateIpAddress: str
    privatePort: str
    publicIpAddress: str
    publicPort: str
    serviceFirewallPolicy: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2ExternalSystem(
    typing_extensions.TypedDict, total=False
):
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
class GoogleCloudSecuritycenterV2File(typing_extensions.TypedDict, total=False):
    contents: str
    diskPath: GoogleCloudSecuritycenterV2DiskPath
    fileLoadState: typing_extensions.Literal[
        "FILE_LOAD_STATE_UNSPECIFIED", "LOADED_BY_PROCESS", "NOT_LOADED_BY_PROCESS"
    ]
    hashedSize: str
    operations: _list[GoogleCloudSecuritycenterV2FileOperation]
    partiallyHashed: bool
    path: str
    sha256: str
    size: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2FileOperation(
    typing_extensions.TypedDict, total=False
):
    type: typing_extensions.Literal[
        "OPERATION_TYPE_UNSPECIFIED", "OPEN", "READ", "RENAME", "WRITE", "EXECUTE"
    ]

@typing.type_check_only
class GoogleCloudSecuritycenterV2Finding(typing_extensions.TypedDict, total=False):
    access: GoogleCloudSecuritycenterV2Access
    affectedResources: GoogleCloudSecuritycenterV2AffectedResources
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
    disk: GoogleCloudSecuritycenterV2Disk
    eventTime: str
    exfiltration: GoogleCloudSecuritycenterV2Exfiltration
    externalExposure: GoogleCloudSecuritycenterV2ExternalExposure
    externalSystems: dict[str, typing.Any]
    externalUri: str
    files: _list[GoogleCloudSecuritycenterV2File]
    findingClass: typing_extensions.Literal[
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
    ]
    groupMemberships: _list[GoogleCloudSecuritycenterV2GroupMembership]
    iamBindings: _list[GoogleCloudSecuritycenterV2IamBinding]
    indicator: GoogleCloudSecuritycenterV2Indicator
    ipRules: GoogleCloudSecuritycenterV2IpRules
    job: GoogleCloudSecuritycenterV2Job
    kernelRootkit: GoogleCloudSecuritycenterV2KernelRootkit
    kubernetes: GoogleCloudSecuritycenterV2Kubernetes
    loadBalancers: _list[GoogleCloudSecuritycenterV2LoadBalancer]
    logEntries: _list[GoogleCloudSecuritycenterV2LogEntry]
    mitreAttack: GoogleCloudSecuritycenterV2MitreAttack
    moduleName: str
    mute: typing_extensions.Literal["MUTE_UNSPECIFIED", "MUTED", "UNMUTED", "UNDEFINED"]
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
    processes: _list[GoogleCloudSecuritycenterV2Process]
    resourceName: str
    secret: GoogleCloudSecuritycenterV2Secret
    securityMarks: GoogleCloudSecuritycenterV2SecurityMarks
    securityPosture: GoogleCloudSecuritycenterV2SecurityPosture
    severity: typing_extensions.Literal[
        "SEVERITY_UNSPECIFIED", "CRITICAL", "HIGH", "MEDIUM", "LOW"
    ]
    sourceProperties: dict[str, typing.Any]
    state: typing_extensions.Literal["STATE_UNSPECIFIED", "ACTIVE", "INACTIVE"]
    toxicCombination: GoogleCloudSecuritycenterV2ToxicCombination
    vertexAi: GoogleCloudSecuritycenterV2VertexAi
    vulnerability: GoogleCloudSecuritycenterV2Vulnerability

@typing.type_check_only
class GoogleCloudSecuritycenterV2Folder(typing_extensions.TypedDict, total=False):
    resourceFolder: str
    resourceFolderDisplayName: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2Framework(typing_extensions.TypedDict, total=False):
    category: _list[
        typing_extensions.Literal[
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
    type: typing_extensions.Literal[
        "FRAMEWORK_TYPE_UNSPECIFIED", "FRAMEWORK_TYPE_BUILT_IN", "FRAMEWORK_TYPE_CUSTOM"
    ]

@typing.type_check_only
class GoogleCloudSecuritycenterV2Geolocation(typing_extensions.TypedDict, total=False):
    regionCode: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2GroupMembership(
    typing_extensions.TypedDict, total=False
):
    groupId: str
    groupType: typing_extensions.Literal[
        "GROUP_TYPE_UNSPECIFIED",
        "GROUP_TYPE_TOXIC_COMBINATION",
        "GROUP_TYPE_CHOKEPOINT",
    ]

@typing.type_check_only
class GoogleCloudSecuritycenterV2IamBinding(typing_extensions.TypedDict, total=False):
    action: typing_extensions.Literal["ACTION_UNSPECIFIED", "ADD", "REMOVE"]
    member: str
    role: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2Indicator(typing_extensions.TypedDict, total=False):
    domains: _list[str]
    ipAddresses: _list[str]
    signatures: _list[GoogleCloudSecuritycenterV2ProcessSignature]
    uris: _list[str]

@typing.type_check_only
class GoogleCloudSecuritycenterV2InfoType(typing_extensions.TypedDict, total=False):
    name: str
    sensitivityScore: GoogleCloudSecuritycenterV2SensitivityScore
    version: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2IpRule(typing_extensions.TypedDict, total=False):
    portRanges: _list[GoogleCloudSecuritycenterV2PortRange]
    protocol: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2IpRules(typing_extensions.TypedDict, total=False):
    allowed: GoogleCloudSecuritycenterV2Allowed
    denied: GoogleCloudSecuritycenterV2Denied
    destinationIpRanges: _list[str]
    direction: typing_extensions.Literal["DIRECTION_UNSPECIFIED", "INGRESS", "EGRESS"]
    exposedServices: _list[str]
    sourceIpRanges: _list[str]

@typing.type_check_only
class GoogleCloudSecuritycenterV2Issue(typing_extensions.TypedDict, total=False):
    createTime: str
    description: str
    detection: str
    domains: _list[GoogleCloudSecuritycenterV2IssueDomain]
    exposureScore: float
    issueType: typing_extensions.Literal[
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
    severity: typing_extensions.Literal[
        "SEVERITY_UNSPECIFIED", "CRITICAL", "HIGH", "MEDIUM", "LOW"
    ]
    state: typing_extensions.Literal["STATE_UNSPECIFIED", "ACTIVE", "INACTIVE"]
    updateTime: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2IssueDomain(typing_extensions.TypedDict, total=False):
    domainCategory: typing_extensions.Literal[
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
class GoogleCloudSecuritycenterV2IssueFinding(typing_extensions.TypedDict, total=False):
    cve: GoogleCloudSecuritycenterV2IssueFindingCve
    name: str
    securityBulletin: GoogleCloudSecuritycenterV2IssueFindingSecurityBulletin

@typing.type_check_only
class GoogleCloudSecuritycenterV2IssueFindingCve(
    typing_extensions.TypedDict, total=False
):
    name: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2IssueFindingSecurityBulletin(
    typing_extensions.TypedDict, total=False
):
    name: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2IssueMute(typing_extensions.TypedDict, total=False):
    muteInitiator: str
    muteReason: str
    muteState: typing_extensions.Literal["MUTE_STATE_UNSPECIFIED", "NOT_MUTED", "MUTED"]
    muteUpdateTime: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2IssueResource(
    typing_extensions.TypedDict, total=False
):
    adcApplication: GoogleCloudSecuritycenterV2IssueResourceAdcApplication
    adcApplicationTemplate: (
        GoogleCloudSecuritycenterV2IssueResourceAdcApplicationTemplateRevision
    )
    adcSharedTemplate: GoogleCloudSecuritycenterV2IssueResourceAdcSharedTemplateRevision
    application: GoogleCloudSecuritycenterV2IssueResourceApplication
    awsMetadata: GoogleCloudSecuritycenterV2IssueResourceAwsMetadata
    azureMetadata: GoogleCloudSecuritycenterV2IssueResourceAzureMetadata
    cloudProvider: typing_extensions.Literal[
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
    typing_extensions.TypedDict, total=False
):
    attributes: GoogleCloudSecuritycenterV2IssueResourceApplicationAttributes
    name: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2IssueResourceAdcApplicationTemplateRevision(
    typing_extensions.TypedDict, total=False
):
    name: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2IssueResourceAdcSharedTemplateRevision(
    typing_extensions.TypedDict, total=False
):
    name: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2IssueResourceApplication(
    typing_extensions.TypedDict, total=False
):
    attributes: GoogleCloudSecuritycenterV2IssueResourceApplicationAttributes
    name: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2IssueResourceApplicationAttributes(
    typing_extensions.TypedDict, total=False
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
    typing_extensions.TypedDict, total=False
):
    email: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2IssueResourceApplicationAttributesCriticality(
    typing_extensions.TypedDict, total=False
):
    type: typing_extensions.Literal[
        "CRITICALITY_TYPE_UNSPECIFIED", "MISSION_CRITICAL", "HIGH", "MEDIUM", "LOW"
    ]

@typing.type_check_only
class GoogleCloudSecuritycenterV2IssueResourceApplicationAttributesEnvironment(
    typing_extensions.TypedDict, total=False
):
    type: typing_extensions.Literal[
        "ENVIRONMENT_TYPE_UNSPECIFIED", "PRODUCTION", "STAGING", "TEST", "DEVELOPMENT"
    ]

@typing.type_check_only
class GoogleCloudSecuritycenterV2IssueResourceAwsMetadata(
    typing_extensions.TypedDict, total=False
):
    account: GoogleCloudSecuritycenterV2IssueResourceAwsMetadataAwsAccount

@typing.type_check_only
class GoogleCloudSecuritycenterV2IssueResourceAwsMetadataAwsAccount(
    typing_extensions.TypedDict, total=False
):
    id: str
    name: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2IssueResourceAzureMetadata(
    typing_extensions.TypedDict, total=False
):
    subscription: GoogleCloudSecuritycenterV2IssueResourceAzureMetadataAzureSubscription

@typing.type_check_only
class GoogleCloudSecuritycenterV2IssueResourceAzureMetadataAzureSubscription(
    typing_extensions.TypedDict, total=False
):
    displayName: str
    id: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2IssueResourceGoogleCloudMetadata(
    typing_extensions.TypedDict, total=False
):
    projectId: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2IssueSecurityContext(
    typing_extensions.TypedDict, total=False
):
    aggregatedCount: GoogleCloudSecuritycenterV2IssueSecurityContextAggregatedCount
    context: GoogleCloudSecuritycenterV2IssueSecurityContextContext

@typing.type_check_only
class GoogleCloudSecuritycenterV2IssueSecurityContextAggregatedCount(
    typing_extensions.TypedDict, total=False
):
    key: str
    value: int

@typing.type_check_only
class GoogleCloudSecuritycenterV2IssueSecurityContextContext(
    typing_extensions.TypedDict, total=False
):
    type: str
    values: _list[str]

@typing.type_check_only
class GoogleCloudSecuritycenterV2Job(typing_extensions.TypedDict, total=False):
    errorCode: int
    location: str
    name: str
    state: typing_extensions.Literal[
        "JOB_STATE_UNSPECIFIED", "PENDING", "RUNNING", "SUCCEEDED", "FAILED"
    ]

@typing.type_check_only
class GoogleCloudSecuritycenterV2KernelRootkit(
    typing_extensions.TypedDict, total=False
):
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
class GoogleCloudSecuritycenterV2Kubernetes(typing_extensions.TypedDict, total=False):
    accessReviews: _list[GoogleCloudSecuritycenterV2AccessReview]
    bindings: _list[GoogleCloudSecuritycenterV2Binding]
    nodePools: _list[GoogleCloudSecuritycenterV2NodePool]
    nodes: _list[GoogleCloudSecuritycenterV2Node]
    objects: _list[GoogleCloudSecuritycenterV2Object]
    pods: _list[GoogleCloudSecuritycenterV2Pod]
    roles: _list[GoogleCloudSecuritycenterV2Role]

@typing.type_check_only
class GoogleCloudSecuritycenterV2Label(typing_extensions.TypedDict, total=False):
    name: str
    value: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2LoadBalancer(typing_extensions.TypedDict, total=False):
    name: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2LogEntry(typing_extensions.TypedDict, total=False):
    cloudLoggingEntry: GoogleCloudSecuritycenterV2CloudLoggingEntry

@typing.type_check_only
class GoogleCloudSecuritycenterV2MemoryHashSignature(
    typing_extensions.TypedDict, total=False
):
    binaryFamily: str
    detections: _list[GoogleCloudSecuritycenterV2Detection]

@typing.type_check_only
class GoogleCloudSecuritycenterV2MitreAttack(typing_extensions.TypedDict, total=False):
    additionalTactics: _list[
        typing_extensions.Literal[
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
        typing_extensions.Literal[
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
    primaryTactic: typing_extensions.Literal[
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
        typing_extensions.Literal[
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
class GoogleCloudSecuritycenterV2MuteConfig(typing_extensions.TypedDict, total=False):
    createTime: str
    cryptoKeyName: str
    description: str
    expiryTime: str
    filter: str
    mostRecentEditor: str
    name: str
    type: typing_extensions.Literal["MUTE_CONFIG_TYPE_UNSPECIFIED", "STATIC", "DYNAMIC"]
    updateTime: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2MuteInfo(typing_extensions.TypedDict, total=False):
    dynamicMuteRecords: _list[GoogleCloudSecuritycenterV2DynamicMuteRecord]
    staticMute: GoogleCloudSecuritycenterV2StaticMute

@typing.type_check_only
class GoogleCloudSecuritycenterV2Network(typing_extensions.TypedDict, total=False):
    name: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2Node(typing_extensions.TypedDict, total=False):
    name: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2NodePool(typing_extensions.TypedDict, total=False):
    name: str
    nodes: _list[GoogleCloudSecuritycenterV2Node]

@typing.type_check_only
class GoogleCloudSecuritycenterV2Notebook(typing_extensions.TypedDict, total=False):
    lastAuthor: str
    name: str
    notebookUpdateTime: str
    service: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2NotificationMessage(
    typing_extensions.TypedDict, total=False
):
    finding: GoogleCloudSecuritycenterV2Finding
    notificationConfigName: str
    resource: GoogleCloudSecuritycenterV2Resource

@typing.type_check_only
class GoogleCloudSecuritycenterV2Object(typing_extensions.TypedDict, total=False):
    containers: _list[GoogleCloudSecuritycenterV2Container]
    group: str
    kind: str
    name: str
    ns: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2OrgPolicy(typing_extensions.TypedDict, total=False):
    name: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2Package(typing_extensions.TypedDict, total=False):
    cpeUri: str
    packageName: str
    packageType: str
    packageVersion: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2Pipeline(typing_extensions.TypedDict, total=False):
    displayName: str
    name: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2Pod(typing_extensions.TypedDict, total=False):
    containers: _list[GoogleCloudSecuritycenterV2Container]
    labels: _list[GoogleCloudSecuritycenterV2Label]
    name: str
    ns: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2PolicyDriftDetails(
    typing_extensions.TypedDict, total=False
):
    detectedValue: str
    expectedValue: str
    field: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2PortRange(typing_extensions.TypedDict, total=False):
    max: str
    min: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2Process(typing_extensions.TypedDict, total=False):
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
class GoogleCloudSecuritycenterV2ProcessSignature(
    typing_extensions.TypedDict, total=False
):
    memoryHashSignature: GoogleCloudSecuritycenterV2MemoryHashSignature
    signatureType: typing_extensions.Literal[
        "SIGNATURE_TYPE_UNSPECIFIED", "SIGNATURE_TYPE_PROCESS", "SIGNATURE_TYPE_FILE"
    ]
    yaraRuleSignature: GoogleCloudSecuritycenterV2YaraRuleSignature

@typing.type_check_only
class GoogleCloudSecuritycenterV2Reference(typing_extensions.TypedDict, total=False):
    source: str
    uri: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2Requests(typing_extensions.TypedDict, total=False):
    longTermAllowed: int
    longTermDenied: int
    ratio: float
    shortTermAllowed: int

@typing.type_check_only
class GoogleCloudSecuritycenterV2Resource(typing_extensions.TypedDict, total=False):
    adcApplication: GoogleCloudSecuritycenterV2AdcApplication
    adcApplicationTemplate: GoogleCloudSecuritycenterV2AdcApplicationTemplateRevision
    adcSharedTemplate: GoogleCloudSecuritycenterV2AdcSharedTemplateRevision
    application: GoogleCloudSecuritycenterV2ResourceApplication
    awsMetadata: GoogleCloudSecuritycenterV2AwsMetadata
    azureMetadata: GoogleCloudSecuritycenterV2AzureMetadata
    cloudProvider: typing_extensions.Literal[
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
class GoogleCloudSecuritycenterV2ResourceApplication(
    typing_extensions.TypedDict, total=False
):
    attributes: GoogleCloudSecuritycenterV2ResourceApplicationAttributes
    name: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2ResourceApplicationAttributes(
    typing_extensions.TypedDict, total=False
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
    typing_extensions.TypedDict, total=False
):
    email: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2ResourceApplicationAttributesCriticality(
    typing_extensions.TypedDict, total=False
):
    type: typing_extensions.Literal[
        "CRITICALITY_TYPE_UNSPECIFIED", "MISSION_CRITICAL", "HIGH", "MEDIUM", "LOW"
    ]

@typing.type_check_only
class GoogleCloudSecuritycenterV2ResourceApplicationAttributesEnvironment(
    typing_extensions.TypedDict, total=False
):
    type: typing_extensions.Literal[
        "ENVIRONMENT_TYPE_UNSPECIFIED", "PRODUCTION", "STAGING", "TEST", "DEVELOPMENT"
    ]

@typing.type_check_only
class GoogleCloudSecuritycenterV2ResourcePath(typing_extensions.TypedDict, total=False):
    nodes: _list[GoogleCloudSecuritycenterV2ResourcePathNode]

@typing.type_check_only
class GoogleCloudSecuritycenterV2ResourcePathNode(
    typing_extensions.TypedDict, total=False
):
    displayName: str
    id: str
    nodeType: typing_extensions.Literal[
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
class GoogleCloudSecuritycenterV2ResourceValueConfig(
    typing_extensions.TypedDict, total=False
):
    cloudProvider: typing_extensions.Literal[
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
    resourceValue: typing_extensions.Literal[
        "RESOURCE_VALUE_UNSPECIFIED", "HIGH", "MEDIUM", "LOW", "NONE"
    ]
    scope: str
    sensitiveDataProtectionMapping: (
        GoogleCloudSecuritycenterV2SensitiveDataProtectionMapping
    )
    tagValues: _list[str]
    updateTime: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2Role(typing_extensions.TypedDict, total=False):
    kind: typing_extensions.Literal["KIND_UNSPECIFIED", "ROLE", "CLUSTER_ROLE"]
    name: str
    ns: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2Secret(typing_extensions.TypedDict, total=False):
    environmentVariable: GoogleCloudSecuritycenterV2SecretEnvironmentVariable
    filePath: GoogleCloudSecuritycenterV2SecretFilePath
    status: GoogleCloudSecuritycenterV2SecretStatus
    type: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2SecretEnvironmentVariable(
    typing_extensions.TypedDict, total=False
):
    key: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2SecretFilePath(
    typing_extensions.TypedDict, total=False
):
    path: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2SecretStatus(typing_extensions.TypedDict, total=False):
    lastUpdatedTime: str
    validity: typing_extensions.Literal[
        "SECRET_VALIDITY_UNSPECIFIED",
        "SECRET_VALIDITY_UNSUPPORTED",
        "SECRET_VALIDITY_FAILED",
        "SECRET_VALIDITY_INVALID",
        "SECRET_VALIDITY_VALID",
    ]

@typing.type_check_only
class GoogleCloudSecuritycenterV2SecurityBulletin(
    typing_extensions.TypedDict, total=False
):
    bulletinId: str
    submissionTime: str
    suggestedUpgradeVersion: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2SecurityMarks(
    typing_extensions.TypedDict, total=False
):
    canonicalName: str
    marks: dict[str, typing.Any]
    name: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2SecurityPolicy(
    typing_extensions.TypedDict, total=False
):
    name: str
    preview: bool
    type: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2SecurityPosture(
    typing_extensions.TypedDict, total=False
):
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
    typing_extensions.TypedDict, total=False
):
    highSensitivityMapping: typing_extensions.Literal[
        "RESOURCE_VALUE_UNSPECIFIED", "HIGH", "MEDIUM", "LOW", "NONE"
    ]
    mediumSensitivityMapping: typing_extensions.Literal[
        "RESOURCE_VALUE_UNSPECIFIED", "HIGH", "MEDIUM", "LOW", "NONE"
    ]

@typing.type_check_only
class GoogleCloudSecuritycenterV2SensitivityScore(
    typing_extensions.TypedDict, total=False
):
    score: typing_extensions.Literal[
        "SENSITIVITY_SCORE_LEVEL_UNSPECIFIED",
        "SENSITIVITY_LOW",
        "SENSITIVITY_UNKNOWN",
        "SENSITIVITY_MODERATE",
        "SENSITIVITY_HIGH",
    ]

@typing.type_check_only
class GoogleCloudSecuritycenterV2ServiceAccountDelegationInfo(
    typing_extensions.TypedDict, total=False
):
    principalEmail: str
    principalSubject: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2StaticMute(typing_extensions.TypedDict, total=False):
    applyTime: str
    state: typing_extensions.Literal[
        "MUTE_UNSPECIFIED", "MUTED", "UNMUTED", "UNDEFINED"
    ]

@typing.type_check_only
class GoogleCloudSecuritycenterV2Subject(typing_extensions.TypedDict, total=False):
    kind: typing_extensions.Literal[
        "AUTH_TYPE_UNSPECIFIED", "USER", "SERVICEACCOUNT", "GROUP"
    ]
    name: str
    ns: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2TicketInfo(typing_extensions.TypedDict, total=False):
    assignee: str
    description: str
    id: str
    status: str
    updateTime: str
    uri: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2ToxicCombination(
    typing_extensions.TypedDict, total=False
):
    attackExposureScore: float
    relatedFindings: _list[str]

@typing.type_check_only
class GoogleCloudSecuritycenterV2VertexAi(typing_extensions.TypedDict, total=False):
    datasets: _list[GoogleCloudSecuritycenterV2Dataset]
    pipelines: _list[GoogleCloudSecuritycenterV2Pipeline]

@typing.type_check_only
class GoogleCloudSecuritycenterV2Vulnerability(
    typing_extensions.TypedDict, total=False
):
    cve: GoogleCloudSecuritycenterV2Cve
    cwes: _list[GoogleCloudSecuritycenterV2Cwe]
    fixedPackage: GoogleCloudSecuritycenterV2Package
    offendingPackage: GoogleCloudSecuritycenterV2Package
    providerRiskScore: str
    reachable: bool
    securityBulletin: GoogleCloudSecuritycenterV2SecurityBulletin

@typing.type_check_only
class GoogleCloudSecuritycenterV2YaraRuleSignature(
    typing_extensions.TypedDict, total=False
):
    yaraRule: str

@typing.type_check_only
class GroupMembership(typing_extensions.TypedDict, total=False):
    groupId: str
    groupType: typing_extensions.Literal[
        "GROUP_TYPE_UNSPECIFIED",
        "GROUP_TYPE_TOXIC_COMBINATION",
        "GROUP_TYPE_CHOKEPOINT",
    ]

@typing.type_check_only
class IamBinding(typing_extensions.TypedDict, total=False):
    action: typing_extensions.Literal["ACTION_UNSPECIFIED", "ADD", "REMOVE"]
    member: str
    role: str

@typing.type_check_only
class Indicator(typing_extensions.TypedDict, total=False):
    domains: _list[str]
    ipAddresses: _list[str]
    signatures: _list[ProcessSignature]
    uris: _list[str]

@typing.type_check_only
class InfoType(typing_extensions.TypedDict, total=False):
    name: str
    sensitivityScore: SensitivityScore
    version: str

@typing.type_check_only
class IpRule(typing_extensions.TypedDict, total=False):
    portRanges: _list[PortRange]
    protocol: str

@typing.type_check_only
class IpRules(typing_extensions.TypedDict, total=False):
    allowed: Allowed
    denied: Denied
    destinationIpRanges: _list[str]
    direction: typing_extensions.Literal["DIRECTION_UNSPECIFIED", "INGRESS", "EGRESS"]
    exposedServices: _list[str]
    sourceIpRanges: _list[str]

@typing.type_check_only
class Job(typing_extensions.TypedDict, total=False):
    errorCode: int
    location: str
    name: str
    state: typing_extensions.Literal[
        "JOB_STATE_UNSPECIFIED", "PENDING", "RUNNING", "SUCCEEDED", "FAILED"
    ]

@typing.type_check_only
class KernelRootkit(typing_extensions.TypedDict, total=False):
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
class Kubernetes(typing_extensions.TypedDict, total=False):
    accessReviews: _list[AccessReview]
    bindings: _list[GoogleCloudSecuritycenterV1Binding]
    nodePools: _list[NodePool]
    nodes: _list[Node]
    objects: _list[Object]
    pods: _list[Pod]
    roles: _list[Role]

@typing.type_check_only
class Label(typing_extensions.TypedDict, total=False):
    name: str
    value: str

@typing.type_check_only
class LoadBalancer(typing_extensions.TypedDict, total=False):
    name: str

@typing.type_check_only
class LogEntry(typing_extensions.TypedDict, total=False):
    cloudLoggingEntry: CloudLoggingEntry

@typing.type_check_only
class MemoryHashSignature(typing_extensions.TypedDict, total=False):
    binaryFamily: str
    detections: _list[Detection]

@typing.type_check_only
class MitreAttack(typing_extensions.TypedDict, total=False):
    additionalTactics: _list[
        typing_extensions.Literal[
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
        typing_extensions.Literal[
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
    primaryTactic: typing_extensions.Literal[
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
        typing_extensions.Literal[
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
class MuteInfo(typing_extensions.TypedDict, total=False):
    dynamicMuteRecords: _list[DynamicMuteRecord]
    staticMute: StaticMute

@typing.type_check_only
class Network(typing_extensions.TypedDict, total=False):
    name: str

@typing.type_check_only
class Node(typing_extensions.TypedDict, total=False):
    name: str

@typing.type_check_only
class NodePool(typing_extensions.TypedDict, total=False):
    name: str
    nodes: _list[Node]

@typing.type_check_only
class Notebook(typing_extensions.TypedDict, total=False):
    lastAuthor: str
    name: str
    notebookUpdateTime: str
    service: str

@typing.type_check_only
class Object(typing_extensions.TypedDict, total=False):
    containers: _list[Container]
    group: str
    kind: str
    name: str
    ns: str

@typing.type_check_only
class OrgPolicy(typing_extensions.TypedDict, total=False):
    name: str

@typing.type_check_only
class Package(typing_extensions.TypedDict, total=False):
    cpeUri: str
    packageName: str
    packageType: str
    packageVersion: str

@typing.type_check_only
class Pipeline(typing_extensions.TypedDict, total=False):
    displayName: str
    name: str

@typing.type_check_only
class Pod(typing_extensions.TypedDict, total=False):
    containers: _list[Container]
    labels: _list[Label]
    name: str
    ns: str

@typing.type_check_only
class PolicyDriftDetails(typing_extensions.TypedDict, total=False):
    detectedValue: str
    expectedValue: str
    field: str

@typing.type_check_only
class PortRange(typing_extensions.TypedDict, total=False):
    max: str
    min: str

@typing.type_check_only
class Process(typing_extensions.TypedDict, total=False):
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
class ProcessSignature(typing_extensions.TypedDict, total=False):
    memoryHashSignature: MemoryHashSignature
    signatureType: typing_extensions.Literal[
        "SIGNATURE_TYPE_UNSPECIFIED", "SIGNATURE_TYPE_PROCESS", "SIGNATURE_TYPE_FILE"
    ]
    yaraRuleSignature: YaraRuleSignature

@typing.type_check_only
class RapidVulnerabilityDetectionSettings(typing_extensions.TypedDict, total=False):
    modules: dict[str, typing.Any]
    name: str
    serviceEnablementState: typing_extensions.Literal[
        "ENABLEMENT_STATE_UNSPECIFIED", "INHERITED", "ENABLED", "DISABLED"
    ]
    updateTime: str

@typing.type_check_only
class Reference(typing_extensions.TypedDict, total=False):
    source: str
    uri: str

@typing.type_check_only
class Requests(typing_extensions.TypedDict, total=False):
    longTermAllowed: int
    longTermDenied: int
    ratio: float
    shortTermAllowed: int

@typing.type_check_only
class ResourcePath(typing_extensions.TypedDict, total=False):
    nodes: _list[ResourcePathNode]

@typing.type_check_only
class ResourcePathNode(typing_extensions.TypedDict, total=False):
    displayName: str
    id: str
    nodeType: typing_extensions.Literal[
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
class Role(typing_extensions.TypedDict, total=False):
    kind: typing_extensions.Literal["KIND_UNSPECIFIED", "ROLE", "CLUSTER_ROLE"]
    name: str
    ns: str

@typing.type_check_only
class Secret(typing_extensions.TypedDict, total=False):
    environmentVariable: SecretEnvironmentVariable
    filePath: SecretFilePath
    status: SecretStatus
    type: str

@typing.type_check_only
class SecretEnvironmentVariable(typing_extensions.TypedDict, total=False):
    key: str

@typing.type_check_only
class SecretFilePath(typing_extensions.TypedDict, total=False):
    path: str

@typing.type_check_only
class SecretStatus(typing_extensions.TypedDict, total=False):
    lastUpdatedTime: str
    validity: typing_extensions.Literal[
        "SECRET_VALIDITY_UNSPECIFIED",
        "SECRET_VALIDITY_UNSUPPORTED",
        "SECRET_VALIDITY_FAILED",
        "SECRET_VALIDITY_INVALID",
        "SECRET_VALIDITY_VALID",
    ]

@typing.type_check_only
class SecurityBulletin(typing_extensions.TypedDict, total=False):
    bulletinId: str
    submissionTime: str
    suggestedUpgradeVersion: str

@typing.type_check_only
class SecurityCenterSettings(typing_extensions.TypedDict, total=False):
    cryptoKeyName: str
    logSinkProject: str
    name: str
    onboardingTime: str
    orgServiceAccount: str

@typing.type_check_only
class SecurityHealthAnalyticsSettings(typing_extensions.TypedDict, total=False):
    modules: dict[str, typing.Any]
    name: str
    serviceAccount: str
    serviceEnablementState: typing_extensions.Literal[
        "ENABLEMENT_STATE_UNSPECIFIED", "INHERITED", "ENABLED", "DISABLED"
    ]
    updateTime: str

@typing.type_check_only
class SecurityMarks(typing_extensions.TypedDict, total=False):
    canonicalName: str
    marks: dict[str, typing.Any]
    name: str

@typing.type_check_only
class SecurityPolicy(typing_extensions.TypedDict, total=False):
    name: str
    preview: bool
    type: str

@typing.type_check_only
class SecurityPosture(typing_extensions.TypedDict, total=False):
    changedPolicy: str
    name: str
    policy: str
    policyDriftDetails: _list[PolicyDriftDetails]
    policySet: str
    postureDeployment: str
    postureDeploymentResource: str
    revisionId: str

@typing.type_check_only
class SensitivityScore(typing_extensions.TypedDict, total=False):
    score: typing_extensions.Literal[
        "SENSITIVITY_SCORE_LEVEL_UNSPECIFIED",
        "SENSITIVITY_LOW",
        "SENSITIVITY_UNKNOWN",
        "SENSITIVITY_MODERATE",
        "SENSITIVITY_HIGH",
    ]

@typing.type_check_only
class ServiceAccountDelegationInfo(typing_extensions.TypedDict, total=False):
    principalEmail: str
    principalSubject: str

@typing.type_check_only
class StaticMute(typing_extensions.TypedDict, total=False):
    applyTime: str
    state: typing_extensions.Literal[
        "MUTE_UNSPECIFIED", "MUTED", "UNMUTED", "UNDEFINED"
    ]

@typing.type_check_only
class Subject(typing_extensions.TypedDict, total=False):
    kind: typing_extensions.Literal[
        "AUTH_TYPE_UNSPECIFIED", "USER", "SERVICEACCOUNT", "GROUP"
    ]
    name: str
    ns: str

@typing.type_check_only
class Subscription(typing_extensions.TypedDict, total=False):
    details: Details
    name: str
    tier: typing_extensions.Literal[
        "TIER_UNSPECIFIED", "STANDARD", "PREMIUM", "ENTERPRISE", "ENTERPRISE_MC"
    ]

@typing.type_check_only
class TicketInfo(typing_extensions.TypedDict, total=False):
    assignee: str
    description: str
    id: str
    status: str
    updateTime: str
    uri: str

@typing.type_check_only
class ToxicCombination(typing_extensions.TypedDict, total=False):
    attackExposureScore: float
    relatedFindings: _list[str]

@typing.type_check_only
class VertexAi(typing_extensions.TypedDict, total=False):
    datasets: _list[Dataset]
    pipelines: _list[Pipeline]

@typing.type_check_only
class VirtualMachineThreatDetectionSettings(typing_extensions.TypedDict, total=False):
    modules: dict[str, typing.Any]
    name: str
    serviceAccount: str
    serviceEnablementState: typing_extensions.Literal[
        "ENABLEMENT_STATE_UNSPECIFIED", "INHERITED", "ENABLED", "DISABLED"
    ]
    updateTime: str

@typing.type_check_only
class Vulnerability(typing_extensions.TypedDict, total=False):
    cve: Cve
    cwes: _list[Cwe]
    fixedPackage: Package
    offendingPackage: Package
    providerRiskScore: str
    reachable: bool
    securityBulletin: SecurityBulletin

@typing.type_check_only
class VulnerabilityCountBySeverity(typing_extensions.TypedDict, total=False):
    severityToFindingCount: dict[str, typing.Any]

@typing.type_check_only
class VulnerabilitySnapshot(typing_extensions.TypedDict, total=False):
    cloudProvider: typing_extensions.Literal[
        "CLOUD_PROVIDER_UNSPECIFIED",
        "GOOGLE_CLOUD_PLATFORM",
        "AMAZON_WEB_SERVICES",
        "MICROSOFT_AZURE",
    ]
    findingCount: VulnerabilityCountBySeverity
    name: str
    snapshotTime: str

@typing.type_check_only
class WebSecurityScannerSettings(typing_extensions.TypedDict, total=False):
    modules: dict[str, typing.Any]
    name: str
    serviceEnablementState: typing_extensions.Literal[
        "ENABLEMENT_STATE_UNSPECIFIED", "INHERITED", "ENABLED", "DISABLED"
    ]
    updateTime: str

@typing.type_check_only
class YaraRuleSignature(typing_extensions.TypedDict, total=False):
    yaraRule: str
