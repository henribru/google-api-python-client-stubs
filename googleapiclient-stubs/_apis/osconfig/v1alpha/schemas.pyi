import typing

_list = list

@typing.type_check_only
class CVSSv3(typing.TypedDict, total=False):
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
    exploitabilityScore: float
    impactScore: float
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
class CancelOperationRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class Date(typing.TypedDict, total=False):
    day: int
    month: int
    year: int

@typing.type_check_only
class Empty(typing.TypedDict, total=False): ...

@typing.type_check_only
class FixedOrPercent(typing.TypedDict, total=False):
    fixed: int
    percent: int

@typing.type_check_only
class GoogleCloudOsconfigV1__OSPolicyAssignmentOperationMetadata(
    typing.TypedDict, total=False
):
    apiMethod: typing.Literal["API_METHOD_UNSPECIFIED", "CREATE", "UPDATE", "DELETE"]
    osPolicyAssignment: str
    rolloutStartTime: str
    rolloutState: typing.Literal[
        "ROLLOUT_STATE_UNSPECIFIED",
        "IN_PROGRESS",
        "CANCELLING",
        "CANCELLED",
        "SUCCEEDED",
    ]
    rolloutUpdateTime: str

@typing.type_check_only
class GoogleCloudOsconfigV2__OperationMetadata(typing.TypedDict, total=False):
    apiVersion: str
    createTime: str
    endTime: str
    requestedCancellation: bool
    statusMessage: str
    target: str
    verb: str

@typing.type_check_only
class GoogleCloudOsconfigV2beta__OperationMetadata(typing.TypedDict, total=False):
    apiVersion: str
    createTime: str
    endTime: str
    requestedCancellation: bool
    statusMessage: str
    target: str
    verb: str

@typing.type_check_only
class InstanceOSPoliciesCompliance(typing.TypedDict, total=False):
    detailedState: str
    detailedStateReason: str
    instance: str
    lastComplianceCheckTime: str
    lastComplianceRunId: str
    name: str
    osPolicyCompliances: _list[InstanceOSPoliciesComplianceOSPolicyCompliance]
    state: typing.Literal[
        "OS_POLICY_COMPLIANCE_STATE_UNSPECIFIED",
        "COMPLIANT",
        "NON_COMPLIANT",
        "UNKNOWN",
        "NO_OS_POLICIES_APPLICABLE",
    ]

@typing.type_check_only
class InstanceOSPoliciesComplianceOSPolicyCompliance(typing.TypedDict, total=False):
    osPolicyAssignment: str
    osPolicyId: str
    osPolicyResourceCompliances: _list[OSPolicyResourceCompliance]
    state: typing.Literal[
        "OS_POLICY_COMPLIANCE_STATE_UNSPECIFIED",
        "COMPLIANT",
        "NON_COMPLIANT",
        "UNKNOWN",
        "NO_OS_POLICIES_APPLICABLE",
    ]

@typing.type_check_only
class Inventory(typing.TypedDict, total=False):
    items: dict[str, typing.Any]
    name: str
    osInfo: InventoryOsInfo
    updateTime: str

@typing.type_check_only
class InventoryItem(typing.TypedDict, total=False):
    availablePackage: InventorySoftwarePackage
    createTime: str
    id: str
    installedPackage: InventorySoftwarePackage
    originType: typing.Literal["ORIGIN_TYPE_UNSPECIFIED", "INVENTORY_REPORT"]
    type: typing.Literal["TYPE_UNSPECIFIED", "INSTALLED_PACKAGE", "AVAILABLE_PACKAGE"]
    updateTime: str

@typing.type_check_only
class InventoryOsInfo(typing.TypedDict, total=False):
    architecture: str
    hostname: str
    kernelRelease: str
    kernelVersion: str
    longName: str
    osconfigAgentVersion: str
    shortName: str
    version: str

@typing.type_check_only
class InventorySoftwarePackage(typing.TypedDict, total=False):
    aptPackage: InventoryVersionedPackage
    cosPackage: InventoryVersionedPackage
    googetPackage: InventoryVersionedPackage
    qfePackage: InventoryWindowsQuickFixEngineeringPackage
    windowsApplication: InventoryWindowsApplication
    wuaPackage: InventoryWindowsUpdatePackage
    yumPackage: InventoryVersionedPackage
    zypperPackage: InventoryVersionedPackage
    zypperPatch: InventoryZypperPatch

@typing.type_check_only
class InventoryVersionedPackage(typing.TypedDict, total=False):
    architecture: str
    packageName: str
    version: str

@typing.type_check_only
class InventoryWindowsApplication(typing.TypedDict, total=False):
    displayName: str
    displayVersion: str
    helpLink: str
    installDate: Date
    publisher: str

@typing.type_check_only
class InventoryWindowsQuickFixEngineeringPackage(typing.TypedDict, total=False):
    caption: str
    description: str
    hotFixId: str
    installTime: str

@typing.type_check_only
class InventoryWindowsUpdatePackage(typing.TypedDict, total=False):
    categories: _list[InventoryWindowsUpdatePackageWindowsUpdateCategory]
    description: str
    kbArticleIds: _list[str]
    lastDeploymentChangeTime: str
    moreInfoUrls: _list[str]
    revisionNumber: int
    supportUrl: str
    title: str
    updateId: str

@typing.type_check_only
class InventoryWindowsUpdatePackageWindowsUpdateCategory(typing.TypedDict, total=False):
    id: str
    name: str

@typing.type_check_only
class InventoryZypperPatch(typing.TypedDict, total=False):
    category: str
    patchName: str
    severity: str
    summary: str

@typing.type_check_only
class ListInstanceOSPoliciesCompliancesResponse(typing.TypedDict, total=False):
    instanceOsPoliciesCompliances: _list[InstanceOSPoliciesCompliance]
    nextPageToken: str

@typing.type_check_only
class ListInventoriesResponse(typing.TypedDict, total=False):
    inventories: _list[Inventory]
    nextPageToken: str

@typing.type_check_only
class ListOSPolicyAssignmentReportsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    osPolicyAssignmentReports: _list[OSPolicyAssignmentReport]

@typing.type_check_only
class ListOSPolicyAssignmentRevisionsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    osPolicyAssignments: _list[OSPolicyAssignment]

@typing.type_check_only
class ListOSPolicyAssignmentsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    osPolicyAssignments: _list[OSPolicyAssignment]

@typing.type_check_only
class ListVulnerabilityReportsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    vulnerabilityReports: _list[VulnerabilityReport]

@typing.type_check_only
class MessageSet(typing.TypedDict, total=False): ...

@typing.type_check_only
class OSPolicy(typing.TypedDict, total=False):
    allowNoResourceGroupMatch: bool
    description: str
    id: str
    mode: typing.Literal["MODE_UNSPECIFIED", "VALIDATION", "ENFORCEMENT"]
    resourceGroups: _list[OSPolicyResourceGroup]

@typing.type_check_only
class OSPolicyAssignment(typing.TypedDict, total=False):
    baseline: bool
    deleted: bool
    description: str
    etag: str
    instanceFilter: OSPolicyAssignmentInstanceFilter
    name: str
    osPolicies: _list[OSPolicy]
    reconciling: bool
    revisionCreateTime: str
    revisionId: str
    rollout: OSPolicyAssignmentRollout
    rolloutState: typing.Literal[
        "ROLLOUT_STATE_UNSPECIFIED",
        "IN_PROGRESS",
        "CANCELLING",
        "CANCELLED",
        "SUCCEEDED",
    ]
    uid: str

@typing.type_check_only
class OSPolicyAssignmentInstanceFilter(typing.TypedDict, total=False):
    all: bool
    exclusionLabels: _list[OSPolicyAssignmentLabelSet]
    inclusionLabels: _list[OSPolicyAssignmentLabelSet]
    inventories: _list[OSPolicyAssignmentInstanceFilterInventory]
    osShortNames: _list[str]

@typing.type_check_only
class OSPolicyAssignmentInstanceFilterInventory(typing.TypedDict, total=False):
    osShortName: str
    osVersion: str

@typing.type_check_only
class OSPolicyAssignmentLabelSet(typing.TypedDict, total=False):
    labels: dict[str, typing.Any]

@typing.type_check_only
class OSPolicyAssignmentOperationMetadata(typing.TypedDict, total=False):
    apiMethod: typing.Literal["API_METHOD_UNSPECIFIED", "CREATE", "UPDATE", "DELETE"]
    osPolicyAssignment: str
    rolloutStartTime: str
    rolloutState: typing.Literal[
        "ROLLOUT_STATE_UNSPECIFIED",
        "IN_PROGRESS",
        "CANCELLING",
        "CANCELLED",
        "SUCCEEDED",
    ]
    rolloutUpdateTime: str

@typing.type_check_only
class OSPolicyAssignmentReport(typing.TypedDict, total=False):
    instance: str
    lastRunId: str
    name: str
    osPolicyAssignment: str
    osPolicyCompliances: _list[OSPolicyAssignmentReportOSPolicyCompliance]
    updateTime: str

@typing.type_check_only
class OSPolicyAssignmentReportOSPolicyCompliance(typing.TypedDict, total=False):
    complianceState: typing.Literal["UNKNOWN", "COMPLIANT", "NON_COMPLIANT"]
    complianceStateReason: str
    osPolicyId: str
    osPolicyResourceCompliances: _list[
        OSPolicyAssignmentReportOSPolicyComplianceOSPolicyResourceCompliance
    ]

@typing.type_check_only
class OSPolicyAssignmentReportOSPolicyComplianceOSPolicyResourceCompliance(
    typing.TypedDict, total=False
):
    complianceState: typing.Literal["UNKNOWN", "COMPLIANT", "NON_COMPLIANT"]
    complianceStateReason: str
    configSteps: _list[
        OSPolicyAssignmentReportOSPolicyComplianceOSPolicyResourceComplianceOSPolicyResourceConfigStep
    ]
    execResourceOutput: OSPolicyAssignmentReportOSPolicyComplianceOSPolicyResourceComplianceExecResourceOutput
    osPolicyResourceId: str

@typing.type_check_only
class OSPolicyAssignmentReportOSPolicyComplianceOSPolicyResourceComplianceExecResourceOutput(
    typing.TypedDict, total=False
):
    enforcementOutput: str

@typing.type_check_only
class OSPolicyAssignmentReportOSPolicyComplianceOSPolicyResourceComplianceOSPolicyResourceConfigStep(
    typing.TypedDict, total=False
):
    errorMessage: str
    type: typing.Literal[
        "TYPE_UNSPECIFIED",
        "VALIDATION",
        "DESIRED_STATE_CHECK",
        "DESIRED_STATE_ENFORCEMENT",
        "DESIRED_STATE_CHECK_POST_ENFORCEMENT",
    ]

@typing.type_check_only
class OSPolicyAssignmentRollout(typing.TypedDict, total=False):
    disruptionBudget: FixedOrPercent
    minWaitDuration: str

@typing.type_check_only
class OSPolicyInventoryFilter(typing.TypedDict, total=False):
    osShortName: str
    osVersion: str

@typing.type_check_only
class OSPolicyOSFilter(typing.TypedDict, total=False):
    osShortName: str
    osVersion: str

@typing.type_check_only
class OSPolicyResource(typing.TypedDict, total=False):
    exec: OSPolicyResourceExecResource
    file: OSPolicyResourceFileResource
    id: str
    pkg: OSPolicyResourcePackageResource
    repository: OSPolicyResourceRepositoryResource

@typing.type_check_only
class OSPolicyResourceCompliance(typing.TypedDict, total=False):
    configSteps: _list[OSPolicyResourceConfigStep]
    execResourceOutput: OSPolicyResourceComplianceExecResourceOutput
    osPolicyResourceId: str
    state: typing.Literal[
        "OS_POLICY_COMPLIANCE_STATE_UNSPECIFIED",
        "COMPLIANT",
        "NON_COMPLIANT",
        "UNKNOWN",
        "NO_OS_POLICIES_APPLICABLE",
    ]

@typing.type_check_only
class OSPolicyResourceComplianceExecResourceOutput(typing.TypedDict, total=False):
    enforcementOutput: str

@typing.type_check_only
class OSPolicyResourceConfigStep(typing.TypedDict, total=False):
    errorMessage: str
    outcome: typing.Literal["OUTCOME_UNSPECIFIED", "SUCCEEDED", "FAILED"]
    type: typing.Literal[
        "TYPE_UNSPECIFIED",
        "VALIDATION",
        "DESIRED_STATE_CHECK",
        "DESIRED_STATE_ENFORCEMENT",
        "DESIRED_STATE_CHECK_POST_ENFORCEMENT",
    ]

@typing.type_check_only
class OSPolicyResourceExecResource(typing.TypedDict, total=False):
    enforce: OSPolicyResourceExecResourceExec
    validate: OSPolicyResourceExecResourceExec

@typing.type_check_only
class OSPolicyResourceExecResourceExec(typing.TypedDict, total=False):
    args: _list[str]
    file: OSPolicyResourceFile
    interpreter: typing.Literal[
        "INTERPRETER_UNSPECIFIED", "NONE", "SHELL", "POWERSHELL"
    ]
    outputFilePath: str
    script: str

@typing.type_check_only
class OSPolicyResourceFile(typing.TypedDict, total=False):
    allowInsecure: bool
    gcs: OSPolicyResourceFileGcs
    localPath: str
    remote: OSPolicyResourceFileRemote

@typing.type_check_only
class OSPolicyResourceFileGcs(typing.TypedDict, total=False):
    bucket: str
    generation: str
    object: str

@typing.type_check_only
class OSPolicyResourceFileRemote(typing.TypedDict, total=False):
    sha256Checksum: str
    uri: str

@typing.type_check_only
class OSPolicyResourceFileResource(typing.TypedDict, total=False):
    content: str
    file: OSPolicyResourceFile
    path: str
    permissions: str
    state: typing.Literal[
        "DESIRED_STATE_UNSPECIFIED", "PRESENT", "ABSENT", "CONTENTS_MATCH"
    ]

@typing.type_check_only
class OSPolicyResourceGroup(typing.TypedDict, total=False):
    inventoryFilters: _list[OSPolicyInventoryFilter]
    osFilter: OSPolicyOSFilter
    resources: _list[OSPolicyResource]

@typing.type_check_only
class OSPolicyResourcePackageResource(typing.TypedDict, total=False):
    apt: OSPolicyResourcePackageResourceAPT
    deb: OSPolicyResourcePackageResourceDeb
    desiredState: typing.Literal["DESIRED_STATE_UNSPECIFIED", "INSTALLED", "REMOVED"]
    googet: OSPolicyResourcePackageResourceGooGet
    msi: OSPolicyResourcePackageResourceMSI
    rpm: OSPolicyResourcePackageResourceRPM
    yum: OSPolicyResourcePackageResourceYUM
    zypper: OSPolicyResourcePackageResourceZypper

@typing.type_check_only
class OSPolicyResourcePackageResourceAPT(typing.TypedDict, total=False):
    name: str

@typing.type_check_only
class OSPolicyResourcePackageResourceDeb(typing.TypedDict, total=False):
    pullDeps: bool
    source: OSPolicyResourceFile

@typing.type_check_only
class OSPolicyResourcePackageResourceGooGet(typing.TypedDict, total=False):
    name: str

@typing.type_check_only
class OSPolicyResourcePackageResourceMSI(typing.TypedDict, total=False):
    properties: _list[str]
    source: OSPolicyResourceFile

@typing.type_check_only
class OSPolicyResourcePackageResourceRPM(typing.TypedDict, total=False):
    pullDeps: bool
    source: OSPolicyResourceFile

@typing.type_check_only
class OSPolicyResourcePackageResourceYUM(typing.TypedDict, total=False):
    name: str

@typing.type_check_only
class OSPolicyResourcePackageResourceZypper(typing.TypedDict, total=False):
    name: str

@typing.type_check_only
class OSPolicyResourceRepositoryResource(typing.TypedDict, total=False):
    apt: OSPolicyResourceRepositoryResourceAptRepository
    goo: OSPolicyResourceRepositoryResourceGooRepository
    yum: OSPolicyResourceRepositoryResourceYumRepository
    zypper: OSPolicyResourceRepositoryResourceZypperRepository

@typing.type_check_only
class OSPolicyResourceRepositoryResourceAptRepository(typing.TypedDict, total=False):
    archiveType: typing.Literal["ARCHIVE_TYPE_UNSPECIFIED", "DEB", "DEB_SRC"]
    components: _list[str]
    distribution: str
    gpgKey: str
    uri: str

@typing.type_check_only
class OSPolicyResourceRepositoryResourceGooRepository(typing.TypedDict, total=False):
    name: str
    url: str

@typing.type_check_only
class OSPolicyResourceRepositoryResourceYumRepository(typing.TypedDict, total=False):
    baseUrl: str
    displayName: str
    gpgKeys: _list[str]
    id: str

@typing.type_check_only
class OSPolicyResourceRepositoryResourceZypperRepository(typing.TypedDict, total=False):
    baseUrl: str
    displayName: str
    gpgKeys: _list[str]
    id: str

@typing.type_check_only
class Operation(typing.TypedDict, total=False):
    done: bool
    error: Status
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class Status(typing.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class StatusProto(typing.TypedDict, total=False):
    canonicalCode: int
    code: int
    message: str
    messageSet: MessageSet
    space: str

@typing.type_check_only
class VulnerabilityReport(typing.TypedDict, total=False):
    highestUpgradableCveSeverity: typing.Literal[
        "VULNERABILITY_SEVERITY_LEVEL_UNSPECIFIED",
        "NONE",
        "MINIMAL",
        "LOW",
        "MEDIUM",
        "HIGH",
        "CRITICAL",
    ]
    name: str
    updateTime: str
    vulnerabilities: _list[VulnerabilityReportVulnerability]

@typing.type_check_only
class VulnerabilityReportVulnerability(typing.TypedDict, total=False):
    availableInventoryItemIds: _list[str]
    createTime: str
    details: VulnerabilityReportVulnerabilityDetails
    installedInventoryItemIds: _list[str]
    items: _list[VulnerabilityReportVulnerabilityItem]
    updateTime: str

@typing.type_check_only
class VulnerabilityReportVulnerabilityDetails(typing.TypedDict, total=False):
    cve: str
    cvssV2Score: float
    cvssV3: CVSSv3
    description: str
    references: _list[VulnerabilityReportVulnerabilityDetailsReference]
    severity: str

@typing.type_check_only
class VulnerabilityReportVulnerabilityDetailsReference(typing.TypedDict, total=False):
    source: str
    url: str

@typing.type_check_only
class VulnerabilityReportVulnerabilityItem(typing.TypedDict, total=False):
    availableInventoryItemId: str
    fixedCpeUri: str
    installedInventoryItemId: str
    upstreamFix: str
