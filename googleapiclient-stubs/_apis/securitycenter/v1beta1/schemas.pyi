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
class Application(typing_extensions.TypedDict, total=False):
    baseUri: str
    fullUri: str

@typing.type_check_only
class Asset(typing_extensions.TypedDict, total=False):
    createTime: str
    name: str
    resourceProperties: dict[str, typing.Any]
    securityCenterProperties: SecurityCenterProperties
    securityMarks: GoogleCloudSecuritycenterV1beta1SecurityMarks
    updateTime: str

@typing.type_check_only
class AssetDiscoveryConfig(typing_extensions.TypedDict, total=False):
    inclusionMode: typing_extensions.Literal[
        "INCLUSION_MODE_UNSPECIFIED", "INCLUDE_ONLY", "EXCLUDE"
    ]
    projectIds: _list[str]

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
class AuditConfig(typing_extensions.TypedDict, total=False):
    auditLogConfigs: _list[AuditLogConfig]
    service: str

@typing.type_check_only
class AuditLogConfig(typing_extensions.TypedDict, total=False):
    exemptedMembers: _list[str]
    logType: typing_extensions.Literal[
        "LOG_TYPE_UNSPECIFIED", "ADMIN_READ", "DATA_WRITE", "DATA_READ"
    ]

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
class Binding(typing_extensions.TypedDict, total=False):
    condition: Expr
    members: _list[str]
    role: str

@typing.type_check_only
class CancelOperationRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class CloudDlpDataProfile(typing_extensions.TypedDict, total=False):
    dataProfile: str
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
class ComplianceSnapshot(typing_extensions.TypedDict, total=False):
    category: str
    complianceStandard: str
    complianceVersion: str
    count: str
    leafContainerResource: str
    name: str
    projectDisplayName: str
    snapshotTime: str

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
class Cve(typing_extensions.TypedDict, total=False):
    cvssv3: Cvssv3
    exploitationActivity: typing_extensions.Literal[
        "EXPLOITATION_ACTIVITY_UNSPECIFIED",
        "WIDE",
        "CONFIRMED",
        "AVAILABLE",
        "ANTICIPATED",
        "NO_KNOWN",
    ]
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
class Database(typing_extensions.TypedDict, total=False):
    displayName: str
    grantees: _list[str]
    name: str
    query: str
    userName: str
    version: str

@typing.type_check_only
class Detection(typing_extensions.TypedDict, total=False):
    binary: str
    percentPagesMatched: float

@typing.type_check_only
class DiskPath(typing_extensions.TypedDict, total=False):
    partitionUuid: str
    relativePath: str

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class EnvironmentVariable(typing_extensions.TypedDict, total=False):
    name: str
    val: str

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
class Expr(typing_extensions.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str

@typing.type_check_only
class File(typing_extensions.TypedDict, total=False):
    contents: str
    diskPath: DiskPath
    hashedSize: str
    partiallyHashed: bool
    path: str
    sha256: str
    size: str

@typing.type_check_only
class Finding(typing_extensions.TypedDict, total=False):
    access: Access
    application: Application
    attackExposure: AttackExposure
    backupDisasterRecovery: BackupDisasterRecovery
    canonicalName: str
    category: str
    cloudDlpDataProfile: CloudDlpDataProfile
    cloudDlpInspection: CloudDlpInspection
    compliances: _list[Compliance]
    connections: _list[Connection]
    contacts: dict[str, typing.Any]
    containers: _list[Container]
    createTime: str
    database: Database
    description: str
    eventTime: str
    exfiltration: Exfiltration
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
    ]
    iamBindings: _list[IamBinding]
    indicator: Indicator
    kernelRootkit: KernelRootkit
    kubernetes: Kubernetes
    loadBalancers: _list[LoadBalancer]
    logEntries: _list[LogEntry]
    mitreAttack: MitreAttack
    moduleName: str
    mute: typing_extensions.Literal["MUTE_UNSPECIFIED", "MUTED", "UNMUTED", "UNDEFINED"]
    muteInitiator: str
    muteUpdateTime: str
    name: str
    nextSteps: str
    orgPolicies: _list[OrgPolicy]
    parent: str
    parentDisplayName: str
    processes: _list[Process]
    resourceName: str
    securityMarks: SecurityMarks
    securityPosture: SecurityPosture
    severity: typing_extensions.Literal[
        "SEVERITY_UNSPECIFIED", "CRITICAL", "HIGH", "MEDIUM", "LOW"
    ]
    sourceProperties: dict[str, typing.Any]
    state: typing_extensions.Literal["STATE_UNSPECIFIED", "ACTIVE", "INACTIVE"]
    vulnerability: Vulnerability

@typing.type_check_only
class Folder(typing_extensions.TypedDict, total=False):
    resourceFolder: str
    resourceFolderDisplayName: str

@typing.type_check_only
class Geolocation(typing_extensions.TypedDict, total=False):
    regionCode: str

@typing.type_check_only
class GetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    options: GetPolicyOptions

@typing.type_check_only
class GetPolicyOptions(typing_extensions.TypedDict, total=False):
    requestedPolicyVersion: int

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
    filter: str
    mostRecentEditor: str
    name: str
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
    displayName: str
    folders: _list[Folder]
    name: str
    parent: str
    parentDisplayName: str
    project: str
    projectDisplayName: str
    type: str

@typing.type_check_only
class GoogleCloudSecuritycenterV1ResourceSelector(
    typing_extensions.TypedDict, total=False
):
    resourceTypes: _list[str]

@typing.type_check_only
class GoogleCloudSecuritycenterV1ResourceValueConfig(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    description: str
    name: str
    resourceLabelsSelector: dict[str, typing.Any]
    resourceType: str
    resourceValue: typing_extensions.Literal[
        "RESOURCE_VALUE_UNSPECIFIED", "HIGH", "MEDIUM", "LOW", "NONE"
    ]
    scope: str
    sensitiveDataProtectionMapping: GoogleCloudSecuritycenterV1SensitiveDataProtectionMapping
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
class GoogleCloudSecuritycenterV1beta1Finding(typing_extensions.TypedDict, total=False):
    category: str
    createTime: str
    eventTime: str
    externalUri: str
    name: str
    parent: str
    resourceName: str
    securityMarks: GoogleCloudSecuritycenterV1beta1SecurityMarks
    sourceProperties: dict[str, typing.Any]
    state: typing_extensions.Literal["STATE_UNSPECIFIED", "ACTIVE", "INACTIVE"]

@typing.type_check_only
class GoogleCloudSecuritycenterV1beta1RunAssetDiscoveryResponse(
    typing_extensions.TypedDict, total=False
):
    duration: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "COMPLETED", "SUPERSEDED", "TERMINATED"
    ]

@typing.type_check_only
class GoogleCloudSecuritycenterV1beta1SecurityMarks(
    typing_extensions.TypedDict, total=False
):
    marks: dict[str, typing.Any]
    name: str

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
class GoogleCloudSecuritycenterV2Application(typing_extensions.TypedDict, total=False):
    baseUri: str
    fullUri: str

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
class GoogleCloudSecuritycenterV2CloudDlpDataProfile(
    typing_extensions.TypedDict, total=False
):
    dataProfile: str
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
class GoogleCloudSecuritycenterV2Cve(typing_extensions.TypedDict, total=False):
    cvssv3: GoogleCloudSecuritycenterV2Cvssv3
    exploitationActivity: typing_extensions.Literal[
        "EXPLOITATION_ACTIVITY_UNSPECIFIED",
        "WIDE",
        "CONFIRMED",
        "AVAILABLE",
        "ANTICIPATED",
        "NO_KNOWN",
    ]
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
class GoogleCloudSecuritycenterV2Database(typing_extensions.TypedDict, total=False):
    displayName: str
    grantees: _list[str]
    name: str
    query: str
    userName: str
    version: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2Detection(typing_extensions.TypedDict, total=False):
    binary: str
    percentPagesMatched: float

@typing.type_check_only
class GoogleCloudSecuritycenterV2DiskPath(typing_extensions.TypedDict, total=False):
    partitionUuid: str
    relativePath: str

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
    hashedSize: str
    partiallyHashed: bool
    path: str
    sha256: str
    size: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2Finding(typing_extensions.TypedDict, total=False):
    access: GoogleCloudSecuritycenterV2Access
    application: GoogleCloudSecuritycenterV2Application
    attackExposure: GoogleCloudSecuritycenterV2AttackExposure
    backupDisasterRecovery: GoogleCloudSecuritycenterV2BackupDisasterRecovery
    canonicalName: str
    category: str
    cloudDlpDataProfile: GoogleCloudSecuritycenterV2CloudDlpDataProfile
    cloudDlpInspection: GoogleCloudSecuritycenterV2CloudDlpInspection
    compliances: _list[GoogleCloudSecuritycenterV2Compliance]
    connections: _list[GoogleCloudSecuritycenterV2Connection]
    contacts: dict[str, typing.Any]
    containers: _list[GoogleCloudSecuritycenterV2Container]
    createTime: str
    database: GoogleCloudSecuritycenterV2Database
    description: str
    eventTime: str
    exfiltration: GoogleCloudSecuritycenterV2Exfiltration
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
    ]
    iamBindings: _list[GoogleCloudSecuritycenterV2IamBinding]
    indicator: GoogleCloudSecuritycenterV2Indicator
    kernelRootkit: GoogleCloudSecuritycenterV2KernelRootkit
    kubernetes: GoogleCloudSecuritycenterV2Kubernetes
    loadBalancers: _list[GoogleCloudSecuritycenterV2LoadBalancer]
    logEntries: _list[GoogleCloudSecuritycenterV2LogEntry]
    mitreAttack: GoogleCloudSecuritycenterV2MitreAttack
    moduleName: str
    mute: typing_extensions.Literal["MUTE_UNSPECIFIED", "MUTED", "UNMUTED", "UNDEFINED"]
    muteInitiator: str
    muteUpdateTime: str
    name: str
    nextSteps: str
    orgPolicies: _list[GoogleCloudSecuritycenterV2OrgPolicy]
    parent: str
    parentDisplayName: str
    processes: _list[GoogleCloudSecuritycenterV2Process]
    resourceName: str
    securityMarks: GoogleCloudSecuritycenterV2SecurityMarks
    securityPosture: GoogleCloudSecuritycenterV2SecurityPosture
    severity: typing_extensions.Literal[
        "SEVERITY_UNSPECIFIED", "CRITICAL", "HIGH", "MEDIUM", "LOW"
    ]
    sourceProperties: dict[str, typing.Any]
    state: typing_extensions.Literal["STATE_UNSPECIFIED", "ACTIVE", "INACTIVE"]
    vulnerability: GoogleCloudSecuritycenterV2Vulnerability

@typing.type_check_only
class GoogleCloudSecuritycenterV2Geolocation(typing_extensions.TypedDict, total=False):
    regionCode: str

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
            "MASQUERADING",
            "MATCH_LEGITIMATE_NAME_OR_LOCATION",
            "BOOT_OR_LOGON_INITIALIZATION_SCRIPTS",
            "STARTUP_ITEMS",
            "NETWORK_SERVICE_DISCOVERY",
            "PROCESS_DISCOVERY",
            "COMMAND_AND_SCRIPTING_INTERPRETER",
            "UNIX_SHELL",
            "PERMISSION_GROUPS_DISCOVERY",
            "CLOUD_GROUPS",
            "APPLICATION_LAYER_PROTOCOL",
            "DNS",
            "SOFTWARE_DEPLOYMENT_TOOLS",
            "VALID_ACCOUNTS",
            "DEFAULT_ACCOUNTS",
            "LOCAL_ACCOUNTS",
            "CLOUD_ACCOUNTS",
            "PROXY",
            "EXTERNAL_PROXY",
            "MULTI_HOP_PROXY",
            "ACCOUNT_MANIPULATION",
            "ADDITIONAL_CLOUD_CREDENTIALS",
            "SSH_AUTHORIZED_KEYS",
            "ADDITIONAL_CONTAINER_CLUSTER_ROLES",
            "INGRESS_TOOL_TRANSFER",
            "NATIVE_API",
            "BRUTE_FORCE",
            "SHARED_MODULES",
            "ACCESS_TOKEN_MANIPULATION",
            "TOKEN_IMPERSONATION_OR_THEFT",
            "EXPLOIT_PUBLIC_FACING_APPLICATION",
            "DOMAIN_POLICY_MODIFICATION",
            "DATA_DESTRUCTION",
            "SERVICE_STOP",
            "INHIBIT_SYSTEM_RECOVERY",
            "RESOURCE_HIJACKING",
            "NETWORK_DENIAL_OF_SERVICE",
            "CLOUD_SERVICE_DISCOVERY",
            "STEAL_APPLICATION_ACCESS_TOKEN",
            "ACCOUNT_ACCESS_REMOVAL",
            "STEAL_WEB_SESSION_COOKIE",
            "CREATE_OR_MODIFY_SYSTEM_PROCESS",
            "ABUSE_ELEVATION_CONTROL_MECHANISM",
            "UNSECURED_CREDENTIALS",
            "MODIFY_AUTHENTICATION_PROCESS",
            "IMPAIR_DEFENSES",
            "DISABLE_OR_MODIFY_TOOLS",
            "EXFILTRATION_OVER_WEB_SERVICE",
            "EXFILTRATION_TO_CLOUD_STORAGE",
            "DYNAMIC_RESOLUTION",
            "LATERAL_TOOL_TRANSFER",
            "MODIFY_CLOUD_COMPUTE_INFRASTRUCTURE",
            "CREATE_SNAPSHOT",
            "CLOUD_INFRASTRUCTURE_DISCOVERY",
            "OBTAIN_CAPABILITIES",
            "ACTIVE_SCANNING",
            "SCANNING_IP_BLOCKS",
            "CONTAINER_AND_RESOURCE_DISCOVERY",
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
            "MASQUERADING",
            "MATCH_LEGITIMATE_NAME_OR_LOCATION",
            "BOOT_OR_LOGON_INITIALIZATION_SCRIPTS",
            "STARTUP_ITEMS",
            "NETWORK_SERVICE_DISCOVERY",
            "PROCESS_DISCOVERY",
            "COMMAND_AND_SCRIPTING_INTERPRETER",
            "UNIX_SHELL",
            "PERMISSION_GROUPS_DISCOVERY",
            "CLOUD_GROUPS",
            "APPLICATION_LAYER_PROTOCOL",
            "DNS",
            "SOFTWARE_DEPLOYMENT_TOOLS",
            "VALID_ACCOUNTS",
            "DEFAULT_ACCOUNTS",
            "LOCAL_ACCOUNTS",
            "CLOUD_ACCOUNTS",
            "PROXY",
            "EXTERNAL_PROXY",
            "MULTI_HOP_PROXY",
            "ACCOUNT_MANIPULATION",
            "ADDITIONAL_CLOUD_CREDENTIALS",
            "SSH_AUTHORIZED_KEYS",
            "ADDITIONAL_CONTAINER_CLUSTER_ROLES",
            "INGRESS_TOOL_TRANSFER",
            "NATIVE_API",
            "BRUTE_FORCE",
            "SHARED_MODULES",
            "ACCESS_TOKEN_MANIPULATION",
            "TOKEN_IMPERSONATION_OR_THEFT",
            "EXPLOIT_PUBLIC_FACING_APPLICATION",
            "DOMAIN_POLICY_MODIFICATION",
            "DATA_DESTRUCTION",
            "SERVICE_STOP",
            "INHIBIT_SYSTEM_RECOVERY",
            "RESOURCE_HIJACKING",
            "NETWORK_DENIAL_OF_SERVICE",
            "CLOUD_SERVICE_DISCOVERY",
            "STEAL_APPLICATION_ACCESS_TOKEN",
            "ACCOUNT_ACCESS_REMOVAL",
            "STEAL_WEB_SESSION_COOKIE",
            "CREATE_OR_MODIFY_SYSTEM_PROCESS",
            "ABUSE_ELEVATION_CONTROL_MECHANISM",
            "UNSECURED_CREDENTIALS",
            "MODIFY_AUTHENTICATION_PROCESS",
            "IMPAIR_DEFENSES",
            "DISABLE_OR_MODIFY_TOOLS",
            "EXFILTRATION_OVER_WEB_SERVICE",
            "EXFILTRATION_TO_CLOUD_STORAGE",
            "DYNAMIC_RESOLUTION",
            "LATERAL_TOOL_TRANSFER",
            "MODIFY_CLOUD_COMPUTE_INFRASTRUCTURE",
            "CREATE_SNAPSHOT",
            "CLOUD_INFRASTRUCTURE_DISCOVERY",
            "OBTAIN_CAPABILITIES",
            "ACTIVE_SCANNING",
            "SCANNING_IP_BLOCKS",
            "CONTAINER_AND_RESOURCE_DISCOVERY",
        ]
    ]
    version: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2MuteConfig(typing_extensions.TypedDict, total=False):
    createTime: str
    description: str
    filter: str
    mostRecentEditor: str
    name: str
    type: typing_extensions.Literal["MUTE_CONFIG_TYPE_UNSPECIFIED", "STATIC"]
    updateTime: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2Node(typing_extensions.TypedDict, total=False):
    name: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2NodePool(typing_extensions.TypedDict, total=False):
    name: str
    nodes: _list[GoogleCloudSecuritycenterV2Node]

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
class GoogleCloudSecuritycenterV2Resource(typing_extensions.TypedDict, total=False):
    displayName: str
    name: str
    type: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2ResourceValueConfig(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    description: str
    name: str
    resourceLabelsSelector: dict[str, typing.Any]
    resourceType: str
    resourceValue: typing_extensions.Literal[
        "RESOURCE_VALUE_UNSPECIFIED", "HIGH", "MEDIUM", "LOW", "NONE"
    ]
    scope: str
    sensitiveDataProtectionMapping: GoogleCloudSecuritycenterV2SensitiveDataProtectionMapping
    tagValues: _list[str]
    updateTime: str

@typing.type_check_only
class GoogleCloudSecuritycenterV2Role(typing_extensions.TypedDict, total=False):
    kind: typing_extensions.Literal["KIND_UNSPECIFIED", "ROLE", "CLUSTER_ROLE"]
    name: str
    ns: str

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
class GoogleCloudSecuritycenterV2ServiceAccountDelegationInfo(
    typing_extensions.TypedDict, total=False
):
    principalEmail: str
    principalSubject: str

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
class GoogleCloudSecuritycenterV2Vulnerability(
    typing_extensions.TypedDict, total=False
):
    cve: GoogleCloudSecuritycenterV2Cve
    fixedPackage: GoogleCloudSecuritycenterV2Package
    offendingPackage: GoogleCloudSecuritycenterV2Package
    securityBulletin: GoogleCloudSecuritycenterV2SecurityBulletin

@typing.type_check_only
class GoogleCloudSecuritycenterV2YaraRuleSignature(
    typing_extensions.TypedDict, total=False
):
    yaraRule: str

@typing.type_check_only
class GroupAssetsRequest(typing_extensions.TypedDict, total=False):
    compareDuration: str
    filter: str
    groupBy: str
    pageSize: int
    pageToken: str
    readTime: str

@typing.type_check_only
class GroupAssetsResponse(typing_extensions.TypedDict, total=False):
    groupByResults: _list[GroupResult]
    nextPageToken: str
    readTime: str

@typing.type_check_only
class GroupFindingsRequest(typing_extensions.TypedDict, total=False):
    filter: str
    groupBy: str
    pageSize: int
    pageToken: str
    readTime: str

@typing.type_check_only
class GroupFindingsResponse(typing_extensions.TypedDict, total=False):
    groupByResults: _list[GroupResult]
    nextPageToken: str
    readTime: str

@typing.type_check_only
class GroupResult(typing_extensions.TypedDict, total=False):
    count: str
    properties: dict[str, typing.Any]

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
class ListAssetsResponse(typing_extensions.TypedDict, total=False):
    listAssetsResults: _list[ListAssetsResult]
    nextPageToken: str
    readTime: str
    totalSize: int

@typing.type_check_only
class ListAssetsResult(typing_extensions.TypedDict, total=False):
    asset: Asset
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "UNUSED", "ADDED", "REMOVED", "ACTIVE"
    ]

@typing.type_check_only
class ListFindingsResponse(typing_extensions.TypedDict, total=False):
    findings: _list[GoogleCloudSecuritycenterV1beta1Finding]
    nextPageToken: str
    readTime: str
    totalSize: int

@typing.type_check_only
class ListOperationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    operations: _list[Operation]

@typing.type_check_only
class ListSourcesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    sources: _list[Source]

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
            "MASQUERADING",
            "MATCH_LEGITIMATE_NAME_OR_LOCATION",
            "BOOT_OR_LOGON_INITIALIZATION_SCRIPTS",
            "STARTUP_ITEMS",
            "NETWORK_SERVICE_DISCOVERY",
            "PROCESS_DISCOVERY",
            "COMMAND_AND_SCRIPTING_INTERPRETER",
            "UNIX_SHELL",
            "PERMISSION_GROUPS_DISCOVERY",
            "CLOUD_GROUPS",
            "APPLICATION_LAYER_PROTOCOL",
            "DNS",
            "SOFTWARE_DEPLOYMENT_TOOLS",
            "VALID_ACCOUNTS",
            "DEFAULT_ACCOUNTS",
            "LOCAL_ACCOUNTS",
            "CLOUD_ACCOUNTS",
            "PROXY",
            "EXTERNAL_PROXY",
            "MULTI_HOP_PROXY",
            "ACCOUNT_MANIPULATION",
            "ADDITIONAL_CLOUD_CREDENTIALS",
            "SSH_AUTHORIZED_KEYS",
            "ADDITIONAL_CONTAINER_CLUSTER_ROLES",
            "INGRESS_TOOL_TRANSFER",
            "NATIVE_API",
            "BRUTE_FORCE",
            "SHARED_MODULES",
            "ACCESS_TOKEN_MANIPULATION",
            "TOKEN_IMPERSONATION_OR_THEFT",
            "EXPLOIT_PUBLIC_FACING_APPLICATION",
            "DOMAIN_POLICY_MODIFICATION",
            "DATA_DESTRUCTION",
            "SERVICE_STOP",
            "INHIBIT_SYSTEM_RECOVERY",
            "RESOURCE_HIJACKING",
            "NETWORK_DENIAL_OF_SERVICE",
            "CLOUD_SERVICE_DISCOVERY",
            "STEAL_APPLICATION_ACCESS_TOKEN",
            "ACCOUNT_ACCESS_REMOVAL",
            "STEAL_WEB_SESSION_COOKIE",
            "CREATE_OR_MODIFY_SYSTEM_PROCESS",
            "ABUSE_ELEVATION_CONTROL_MECHANISM",
            "UNSECURED_CREDENTIALS",
            "MODIFY_AUTHENTICATION_PROCESS",
            "IMPAIR_DEFENSES",
            "DISABLE_OR_MODIFY_TOOLS",
            "EXFILTRATION_OVER_WEB_SERVICE",
            "EXFILTRATION_TO_CLOUD_STORAGE",
            "DYNAMIC_RESOLUTION",
            "LATERAL_TOOL_TRANSFER",
            "MODIFY_CLOUD_COMPUTE_INFRASTRUCTURE",
            "CREATE_SNAPSHOT",
            "CLOUD_INFRASTRUCTURE_DISCOVERY",
            "OBTAIN_CAPABILITIES",
            "ACTIVE_SCANNING",
            "SCANNING_IP_BLOCKS",
            "CONTAINER_AND_RESOURCE_DISCOVERY",
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
            "MASQUERADING",
            "MATCH_LEGITIMATE_NAME_OR_LOCATION",
            "BOOT_OR_LOGON_INITIALIZATION_SCRIPTS",
            "STARTUP_ITEMS",
            "NETWORK_SERVICE_DISCOVERY",
            "PROCESS_DISCOVERY",
            "COMMAND_AND_SCRIPTING_INTERPRETER",
            "UNIX_SHELL",
            "PERMISSION_GROUPS_DISCOVERY",
            "CLOUD_GROUPS",
            "APPLICATION_LAYER_PROTOCOL",
            "DNS",
            "SOFTWARE_DEPLOYMENT_TOOLS",
            "VALID_ACCOUNTS",
            "DEFAULT_ACCOUNTS",
            "LOCAL_ACCOUNTS",
            "CLOUD_ACCOUNTS",
            "PROXY",
            "EXTERNAL_PROXY",
            "MULTI_HOP_PROXY",
            "ACCOUNT_MANIPULATION",
            "ADDITIONAL_CLOUD_CREDENTIALS",
            "SSH_AUTHORIZED_KEYS",
            "ADDITIONAL_CONTAINER_CLUSTER_ROLES",
            "INGRESS_TOOL_TRANSFER",
            "NATIVE_API",
            "BRUTE_FORCE",
            "SHARED_MODULES",
            "ACCESS_TOKEN_MANIPULATION",
            "TOKEN_IMPERSONATION_OR_THEFT",
            "EXPLOIT_PUBLIC_FACING_APPLICATION",
            "DOMAIN_POLICY_MODIFICATION",
            "DATA_DESTRUCTION",
            "SERVICE_STOP",
            "INHIBIT_SYSTEM_RECOVERY",
            "RESOURCE_HIJACKING",
            "NETWORK_DENIAL_OF_SERVICE",
            "CLOUD_SERVICE_DISCOVERY",
            "STEAL_APPLICATION_ACCESS_TOKEN",
            "ACCOUNT_ACCESS_REMOVAL",
            "STEAL_WEB_SESSION_COOKIE",
            "CREATE_OR_MODIFY_SYSTEM_PROCESS",
            "ABUSE_ELEVATION_CONTROL_MECHANISM",
            "UNSECURED_CREDENTIALS",
            "MODIFY_AUTHENTICATION_PROCESS",
            "IMPAIR_DEFENSES",
            "DISABLE_OR_MODIFY_TOOLS",
            "EXFILTRATION_OVER_WEB_SERVICE",
            "EXFILTRATION_TO_CLOUD_STORAGE",
            "DYNAMIC_RESOLUTION",
            "LATERAL_TOOL_TRANSFER",
            "MODIFY_CLOUD_COMPUTE_INFRASTRUCTURE",
            "CREATE_SNAPSHOT",
            "CLOUD_INFRASTRUCTURE_DISCOVERY",
            "OBTAIN_CAPABILITIES",
            "ACTIVE_SCANNING",
            "SCANNING_IP_BLOCKS",
            "CONTAINER_AND_RESOURCE_DISCOVERY",
        ]
    ]
    version: str

@typing.type_check_only
class Node(typing_extensions.TypedDict, total=False):
    name: str

@typing.type_check_only
class NodePool(typing_extensions.TypedDict, total=False):
    name: str
    nodes: _list[Node]

@typing.type_check_only
class Object(typing_extensions.TypedDict, total=False):
    containers: _list[Container]
    group: str
    kind: str
    name: str
    ns: str

@typing.type_check_only
class Operation(typing_extensions.TypedDict, total=False):
    done: bool
    error: Status
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class OrgPolicy(typing_extensions.TypedDict, total=False):
    name: str

@typing.type_check_only
class OrganizationSettings(typing_extensions.TypedDict, total=False):
    assetDiscoveryConfig: AssetDiscoveryConfig
    enableAssetDiscovery: bool
    name: str

@typing.type_check_only
class Package(typing_extensions.TypedDict, total=False):
    cpeUri: str
    packageName: str
    packageType: str
    packageVersion: str

@typing.type_check_only
class Pod(typing_extensions.TypedDict, total=False):
    containers: _list[Container]
    labels: _list[Label]
    name: str
    ns: str

@typing.type_check_only
class Policy(typing_extensions.TypedDict, total=False):
    auditConfigs: _list[AuditConfig]
    bindings: _list[Binding]
    etag: str
    version: int

@typing.type_check_only
class PolicyDriftDetails(typing_extensions.TypedDict, total=False):
    detectedValue: str
    expectedValue: str
    field: str

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

@typing.type_check_only
class ProcessSignature(typing_extensions.TypedDict, total=False):
    memoryHashSignature: MemoryHashSignature
    signatureType: typing_extensions.Literal[
        "SIGNATURE_TYPE_UNSPECIFIED", "SIGNATURE_TYPE_PROCESS", "SIGNATURE_TYPE_FILE"
    ]
    yaraRuleSignature: YaraRuleSignature

@typing.type_check_only
class Reference(typing_extensions.TypedDict, total=False):
    source: str
    uri: str

@typing.type_check_only
class Role(typing_extensions.TypedDict, total=False):
    kind: typing_extensions.Literal["KIND_UNSPECIFIED", "ROLE", "CLUSTER_ROLE"]
    name: str
    ns: str

@typing.type_check_only
class RunAssetDiscoveryRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class SecurityBulletin(typing_extensions.TypedDict, total=False):
    bulletinId: str
    submissionTime: str
    suggestedUpgradeVersion: str

@typing.type_check_only
class SecurityCenterProperties(typing_extensions.TypedDict, total=False):
    resourceName: str
    resourceOwners: _list[str]
    resourceParent: str
    resourceProject: str
    resourceType: str

@typing.type_check_only
class SecurityMarks(typing_extensions.TypedDict, total=False):
    canonicalName: str
    marks: dict[str, typing.Any]
    name: str

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
class ServiceAccountDelegationInfo(typing_extensions.TypedDict, total=False):
    principalEmail: str
    principalSubject: str

@typing.type_check_only
class SetFindingStateRequest(typing_extensions.TypedDict, total=False):
    startTime: str
    state: typing_extensions.Literal["STATE_UNSPECIFIED", "ACTIVE", "INACTIVE"]

@typing.type_check_only
class SetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    policy: Policy
    updateMask: str

@typing.type_check_only
class Source(typing_extensions.TypedDict, total=False):
    description: str
    displayName: str
    name: str

@typing.type_check_only
class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class Subject(typing_extensions.TypedDict, total=False):
    kind: typing_extensions.Literal[
        "AUTH_TYPE_UNSPECIFIED", "USER", "SERVICEACCOUNT", "GROUP"
    ]
    name: str
    ns: str

@typing.type_check_only
class TestIamPermissionsRequest(typing_extensions.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class TestIamPermissionsResponse(typing_extensions.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class TicketInfo(typing_extensions.TypedDict, total=False):
    assignee: str
    description: str
    id: str
    status: str
    updateTime: str
    uri: str

@typing.type_check_only
class Vulnerability(typing_extensions.TypedDict, total=False):
    cve: Cve
    fixedPackage: Package
    offendingPackage: Package
    securityBulletin: SecurityBulletin

@typing.type_check_only
class YaraRuleSignature(typing_extensions.TypedDict, total=False):
    yaraRule: str
