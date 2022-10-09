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
class Asset(typing_extensions.TypedDict, total=False):
    canonicalName: str
    createTime: str
    iamPolicy: IamPolicy
    name: str
    resourceProperties: dict[str, typing.Any]
    securityCenterProperties: SecurityCenterProperties
    securityMarks: SecurityMarks
    updateTime: str

@typing.type_check_only
class AssetDiscoveryConfig(typing_extensions.TypedDict, total=False):
    folderIds: _list[str]
    inclusionMode: typing_extensions.Literal[
        "INCLUSION_MODE_UNSPECIFIED", "INCLUDE_ONLY", "EXCLUDE"
    ]
    projectIds: _list[str]

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
class Binding(typing_extensions.TypedDict, total=False):
    condition: Expr
    members: _list[str]
    role: str

@typing.type_check_only
class BulkMuteFindingsRequest(typing_extensions.TypedDict, total=False):
    filter: str
    muteAnnotation: str

@typing.type_check_only
class Compliance(typing_extensions.TypedDict, total=False):
    ids: _list[str]
    standard: str
    version: str

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
class Detection(typing_extensions.TypedDict, total=False):
    binary: str
    percentPagesMatched: float

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

@typing.type_check_only
class Expr(typing_extensions.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str

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
    totalSize: int

@typing.type_check_only
class GroupFindingsRequest(typing_extensions.TypedDict, total=False):
    compareDuration: str
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
    totalSize: int

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
class IamPolicy(typing_extensions.TypedDict, total=False):
    policyBlob: str

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
class ListAssetsResponse(typing_extensions.TypedDict, total=False):
    listAssetsResults: _list[ListAssetsResult]
    nextPageToken: str
    readTime: str
    totalSize: int

@typing.type_check_only
class ListAssetsResult(typing_extensions.TypedDict, total=False):
    asset: Asset
    stateChange: typing_extensions.Literal["UNUSED", "ADDED", "REMOVED", "ACTIVE"]

@typing.type_check_only
class ListBigQueryExportsResponse(typing_extensions.TypedDict, total=False):
    bigQueryExports: _list[GoogleCloudSecuritycenterV1BigQueryExport]
    nextPageToken: str

@typing.type_check_only
class ListFindingsResponse(typing_extensions.TypedDict, total=False):
    listFindingsResults: _list[ListFindingsResult]
    nextPageToken: str
    readTime: str
    totalSize: int

@typing.type_check_only
class ListFindingsResult(typing_extensions.TypedDict, total=False):
    finding: Finding
    resource: Resource
    stateChange: typing_extensions.Literal[
        "UNUSED", "CHANGED", "UNCHANGED", "ADDED", "REMOVED"
    ]

@typing.type_check_only
class ListMuteConfigsResponse(typing_extensions.TypedDict, total=False):
    muteConfigs: _list[GoogleCloudSecuritycenterV1MuteConfig]
    nextPageToken: str

@typing.type_check_only
class ListNotificationConfigsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    notificationConfigs: _list[NotificationConfig]

@typing.type_check_only
class ListOperationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    operations: _list[Operation]

@typing.type_check_only
class ListSourcesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    sources: _list[Source]

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
class NotificationConfig(typing_extensions.TypedDict, total=False):
    description: str
    name: str
    pubsubTopic: str
    serviceAccount: str
    streamingConfig: StreamingConfig

@typing.type_check_only
class Operation(typing_extensions.TypedDict, total=False):
    done: bool
    error: Status
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class OrganizationSettings(typing_extensions.TypedDict, total=False):
    assetDiscoveryConfig: AssetDiscoveryConfig
    enableAssetDiscovery: bool
    name: str

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
class Reference(typing_extensions.TypedDict, total=False):
    source: str
    uri: str

@typing.type_check_only
class Resource(typing_extensions.TypedDict, total=False):
    displayName: str
    folders: _list[Folder]
    name: str
    parentDisplayName: str
    parentName: str
    projectDisplayName: str
    projectName: str
    type: str

@typing.type_check_only
class Role(typing_extensions.TypedDict, total=False):
    kind: typing_extensions.Literal["KIND_UNSPECIFIED", "ROLE", "CLUSTER_ROLE"]
    name: str
    ns: str

@typing.type_check_only
class RunAssetDiscoveryRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class SecurityCenterProperties(typing_extensions.TypedDict, total=False):
    folders: _list[Folder]
    resourceDisplayName: str
    resourceName: str
    resourceOwners: _list[str]
    resourceParent: str
    resourceParentDisplayName: str
    resourceProject: str
    resourceProjectDisplayName: str
    resourceType: str

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
class SetFindingStateRequest(typing_extensions.TypedDict, total=False):
    startTime: str
    state: typing_extensions.Literal["STATE_UNSPECIFIED", "ACTIVE", "INACTIVE"]

@typing.type_check_only
class SetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    policy: Policy
    updateMask: str

@typing.type_check_only
class SetMuteRequest(typing_extensions.TypedDict, total=False):
    mute: typing_extensions.Literal["MUTE_UNSPECIFIED", "MUTED", "UNMUTED", "UNDEFINED"]

@typing.type_check_only
class Source(typing_extensions.TypedDict, total=False):
    canonicalName: str
    description: str
    displayName: str
    name: str

@typing.type_check_only
class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class StreamingConfig(typing_extensions.TypedDict, total=False):
    filter: str

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
class Vulnerability(typing_extensions.TypedDict, total=False):
    cve: Cve

@typing.type_check_only
class YaraRuleSignature(typing_extensions.TypedDict, total=False):
    yaraRule: str
