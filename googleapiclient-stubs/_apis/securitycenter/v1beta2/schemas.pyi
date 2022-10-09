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
    userAgentFamily: str
    username: str

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
class Compliance(typing_extensions.TypedDict, total=False):
    ids: _list[str]
    standard: str
    version: str

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
class Cve(typing_extensions.TypedDict, total=False):
    cvssv3: Cvssv3
    id: str
    references: _list[Reference]
    upstreamFixAvailable: bool

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

@typing.type_check_only
class Details(typing_extensions.TypedDict, total=False):
    endTime: str
    startTime: str
    type: typing_extensions.Literal[
        "TYPE_UNSPECIFIED", "STANDARD", "TRIAL", "ALPHA", "DEMO"
    ]

@typing.type_check_only
class Detection(typing_extensions.TypedDict, total=False):
    binary: str
    percentPagesMatched: float

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

@typing.type_check_only
class File(typing_extensions.TypedDict, total=False):
    contents: str
    hashedSize: str
    partiallyHashed: bool
    path: str
    sha256: str
    size: str

@typing.type_check_only
class Finding(typing_extensions.TypedDict, total=False):
    access: Access
    canonicalName: str
    category: str
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
    findingClass: typing_extensions.Literal[
        "FINDING_CLASS_UNSPECIFIED",
        "THREAT",
        "VULNERABILITY",
        "MISCONFIGURATION",
        "OBSERVATION",
        "SCC_ERROR",
    ]
    iamBindings: _list[IamBinding]
    indicator: Indicator
    kubernetes: Kubernetes
    mitreAttack: MitreAttack
    mute: typing_extensions.Literal["MUTE_UNSPECIFIED", "MUTED", "UNMUTED", "UNDEFINED"]
    muteInitiator: str
    muteUpdateTime: str
    name: str
    nextSteps: str
    parent: str
    parentDisplayName: str
    processes: _list[Process]
    resourceName: str
    securityMarks: SecurityMarks
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
class GoogleCloudSecuritycenterV1ExposedResource(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudSecuritycenterV1ExposurePath(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudSecuritycenterV1ExternalSystem(
    typing_extensions.TypedDict, total=False
):
    assignees: _list[str]
    externalSystemUpdateTime: str
    externalUid: str
    name: str
    status: str

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
class GoogleCloudSecuritycenterV1ResourceValueConfig(
    typing_extensions.TypedDict, total=False
):
    name: str
    resourceValue: typing_extensions.Literal[
        "RESOURCE_VALUE_UNSPECIFIED", "HIGH", "MEDIUM", "LOW", "NONE"
    ]
    tagValues: _list[str]

@typing.type_check_only
class GoogleCloudSecuritycenterV1RunAssetDiscoveryResponse(
    typing_extensions.TypedDict, total=False
):
    duration: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "COMPLETED", "SUPERSEDED", "TERMINATED"
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
class Kubernetes(typing_extensions.TypedDict, total=False):
    accessReviews: _list[AccessReview]
    bindings: _list[GoogleCloudSecuritycenterV1Binding]
    nodePools: _list[NodePool]
    nodes: _list[Node]
    pods: _list[Pod]
    roles: _list[Role]

@typing.type_check_only
class Label(typing_extensions.TypedDict, total=False):
    name: str
    value: str

@typing.type_check_only
class MemoryHashSignature(typing_extensions.TypedDict, total=False):
    binaryFamily: str
    detections: _list[Detection]

@typing.type_check_only
class MitreAttack(typing_extensions.TypedDict, total=False):
    additionalTactics: _list[str]
    additionalTechniques: _list[str]
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
    primaryTechniques: _list[str]
    version: str

@typing.type_check_only
class Node(typing_extensions.TypedDict, total=False):
    name: str

@typing.type_check_only
class NodePool(typing_extensions.TypedDict, total=False):
    name: str
    nodes: _list[Node]

@typing.type_check_only
class OnboardingState(typing_extensions.TypedDict, total=False):
    name: str
    onboardingLevel: typing_extensions.Literal[
        "ONBOARDING_LEVEL_UNSPECIFIED",
        "ONBOARDING_LEVEL_PROJECT",
        "ONBOARDING_LEVEL_ORGANIZATION",
    ]

@typing.type_check_only
class Pod(typing_extensions.TypedDict, total=False):
    containers: _list[Container]
    labels: _list[Label]
    name: str
    ns: str

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
class Role(typing_extensions.TypedDict, total=False):
    kind: typing_extensions.Literal["KIND_UNSPECIFIED", "ROLE", "CLUSTER_ROLE"]
    name: str
    ns: str

@typing.type_check_only
class SecurityCenterSettings(typing_extensions.TypedDict, total=False):
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
class ServiceAccountDelegationInfo(typing_extensions.TypedDict, total=False):
    principalEmail: str
    principalSubject: str

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
    tier: typing_extensions.Literal["TIER_UNSPECIFIED", "STANDARD", "PREMIUM"]

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
