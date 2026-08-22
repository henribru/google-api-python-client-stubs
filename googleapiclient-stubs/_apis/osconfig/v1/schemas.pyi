import typing

_list = list

@typing.type_check_only
class AptSettings(typing.TypedDict, total=False):
    excludes: _list[str]
    exclusivePackages: _list[str]
    type: typing.Literal["TYPE_UNSPECIFIED", "DIST", "UPGRADE"]

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
class CancelPatchJobRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class Date(typing.TypedDict, total=False):
    day: int
    month: int
    year: int

@typing.type_check_only
class Empty(typing.TypedDict, total=False): ...

@typing.type_check_only
class ExecStep(typing.TypedDict, total=False):
    linuxExecStepConfig: ExecStepConfig
    windowsExecStepConfig: ExecStepConfig

@typing.type_check_only
class ExecStepConfig(typing.TypedDict, total=False):
    allowedSuccessCodes: _list[int]
    gcsObject: GcsObject
    interpreter: typing.Literal[
        "INTERPRETER_UNSPECIFIED", "NONE", "SHELL", "POWERSHELL"
    ]
    localPath: str

@typing.type_check_only
class ExecutePatchJobRequest(typing.TypedDict, total=False):
    description: str
    displayName: str
    dryRun: bool
    duration: str
    instanceFilter: PatchInstanceFilter
    patchConfig: PatchConfig
    rollout: PatchRollout

@typing.type_check_only
class FixedOrPercent(typing.TypedDict, total=False):
    fixed: int
    percent: int

@typing.type_check_only
class GcsObject(typing.TypedDict, total=False):
    bucket: str
    generationNumber: str
    object: str

@typing.type_check_only
class GooSettings(typing.TypedDict, total=False): ...

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
class ListPatchDeploymentsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    patchDeployments: _list[PatchDeployment]

@typing.type_check_only
class ListPatchJobInstanceDetailsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    patchJobInstanceDetails: _list[PatchJobInstanceDetails]

@typing.type_check_only
class ListPatchJobsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    patchJobs: _list[PatchJob]

@typing.type_check_only
class ListVulnerabilityReportsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    vulnerabilityReports: _list[VulnerabilityReport]

@typing.type_check_only
class MessageSet(typing.TypedDict, total=False): ...

@typing.type_check_only
class MonthlySchedule(typing.TypedDict, total=False):
    monthDay: int
    weekDayOfMonth: WeekDayOfMonth

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
class OSPolicyResource(typing.TypedDict, total=False):
    exec: OSPolicyResourceExecResource
    file: OSPolicyResourceFileResource
    id: str
    pkg: OSPolicyResourcePackageResource
    repository: OSPolicyResourceRepositoryResource

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
class OneTimeSchedule(typing.TypedDict, total=False):
    executeTime: str

@typing.type_check_only
class Operation(typing.TypedDict, total=False):
    done: bool
    error: Status
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class PatchConfig(typing.TypedDict, total=False):
    apt: AptSettings
    goo: GooSettings
    migInstancesAllowed: bool
    postStep: ExecStep
    preStep: ExecStep
    rebootConfig: typing.Literal[
        "REBOOT_CONFIG_UNSPECIFIED", "DEFAULT", "ALWAYS", "NEVER"
    ]
    skipUnpatchableVms: bool
    windowsUpdate: WindowsUpdateSettings
    yum: YumSettings
    zypper: ZypperSettings

@typing.type_check_only
class PatchDeployment(typing.TypedDict, total=False):
    createTime: str
    description: str
    duration: str
    instanceFilter: PatchInstanceFilter
    lastExecuteTime: str
    name: str
    oneTimeSchedule: OneTimeSchedule
    patchConfig: PatchConfig
    recurringSchedule: RecurringSchedule
    rollout: PatchRollout
    state: typing.Literal["STATE_UNSPECIFIED", "ACTIVE", "PAUSED"]
    updateTime: str

@typing.type_check_only
class PatchInstanceFilter(typing.TypedDict, total=False):
    all: bool
    groupLabels: _list[PatchInstanceFilterGroupLabel]
    instanceNamePrefixes: _list[str]
    instances: _list[str]
    zones: _list[str]

@typing.type_check_only
class PatchInstanceFilterGroupLabel(typing.TypedDict, total=False):
    labels: dict[str, typing.Any]

@typing.type_check_only
class PatchJob(typing.TypedDict, total=False):
    createTime: str
    description: str
    displayName: str
    dryRun: bool
    duration: str
    errorMessage: str
    instanceDetailsSummary: PatchJobInstanceDetailsSummary
    instanceFilter: PatchInstanceFilter
    name: str
    patchConfig: PatchConfig
    patchDeployment: str
    percentComplete: float
    rollout: PatchRollout
    state: typing.Literal[
        "STATE_UNSPECIFIED",
        "STARTED",
        "INSTANCE_LOOKUP",
        "PATCHING",
        "SUCCEEDED",
        "COMPLETED_WITH_INACTIVE_VMS",
        "COMPLETED_WITH_ERRORS",
        "CANCELED",
        "TIMED_OUT",
    ]
    updateTime: str

@typing.type_check_only
class PatchJobInstanceDetails(typing.TypedDict, total=False):
    attemptCount: str
    failureReason: str
    instanceSystemId: str
    name: str
    state: typing.Literal[
        "PATCH_STATE_UNSPECIFIED",
        "PENDING",
        "INACTIVE",
        "NOTIFIED",
        "STARTED",
        "DOWNLOADING_PATCHES",
        "APPLYING_PATCHES",
        "REBOOTING",
        "SUCCEEDED",
        "SUCCEEDED_REBOOT_REQUIRED",
        "FAILED",
        "ACKED",
        "TIMED_OUT",
        "RUNNING_PRE_PATCH_STEP",
        "RUNNING_POST_PATCH_STEP",
        "NO_AGENT_DETECTED",
        "SKIPPED",
    ]

@typing.type_check_only
class PatchJobInstanceDetailsSummary(typing.TypedDict, total=False):
    ackedInstanceCount: str
    applyingPatchesInstanceCount: str
    downloadingPatchesInstanceCount: str
    failedInstanceCount: str
    inactiveInstanceCount: str
    noAgentDetectedInstanceCount: str
    notifiedInstanceCount: str
    pendingInstanceCount: str
    postPatchStepInstanceCount: str
    prePatchStepInstanceCount: str
    rebootingInstanceCount: str
    skippedInstanceCount: str
    startedInstanceCount: str
    succeededInstanceCount: str
    succeededRebootRequiredInstanceCount: str
    timedOutInstanceCount: str

@typing.type_check_only
class PatchRollout(typing.TypedDict, total=False):
    disruptionBudget: FixedOrPercent
    mode: typing.Literal["MODE_UNSPECIFIED", "ZONE_BY_ZONE", "CONCURRENT_ZONES"]

@typing.type_check_only
class PausePatchDeploymentRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class ProjectFeatureSettings(typing.TypedDict, total=False):
    name: str
    patchAndConfigFeatureSet: typing.Literal[
        "PATCH_AND_CONFIG_FEATURE_SET_UNSPECIFIED", "OSCONFIG_B", "OSCONFIG_C"
    ]

@typing.type_check_only
class RecurringSchedule(typing.TypedDict, total=False):
    endTime: str
    frequency: typing.Literal["FREQUENCY_UNSPECIFIED", "WEEKLY", "MONTHLY", "DAILY"]
    lastExecuteTime: str
    monthly: MonthlySchedule
    nextExecuteTime: str
    startTime: str
    timeOfDay: TimeOfDay
    timeZone: TimeZone
    weekly: WeeklySchedule

@typing.type_check_only
class ResumePatchDeploymentRequest(typing.TypedDict, total=False): ...

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
class TimeOfDay(typing.TypedDict, total=False):
    hours: int
    minutes: int
    nanos: int
    seconds: int

@typing.type_check_only
class TimeZone(typing.TypedDict, total=False):
    id: str
    version: str

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

@typing.type_check_only
class WeekDayOfMonth(typing.TypedDict, total=False):
    dayOfWeek: typing.Literal[
        "DAY_OF_WEEK_UNSPECIFIED",
        "MONDAY",
        "TUESDAY",
        "WEDNESDAY",
        "THURSDAY",
        "FRIDAY",
        "SATURDAY",
        "SUNDAY",
    ]
    dayOffset: int
    weekOrdinal: int

@typing.type_check_only
class WeeklySchedule(typing.TypedDict, total=False):
    dayOfWeek: typing.Literal[
        "DAY_OF_WEEK_UNSPECIFIED",
        "MONDAY",
        "TUESDAY",
        "WEDNESDAY",
        "THURSDAY",
        "FRIDAY",
        "SATURDAY",
        "SUNDAY",
    ]

@typing.type_check_only
class WindowsUpdateSettings(typing.TypedDict, total=False):
    classifications: _list[
        typing.Literal[
            "CLASSIFICATION_UNSPECIFIED",
            "CRITICAL",
            "SECURITY",
            "DEFINITION",
            "DRIVER",
            "FEATURE_PACK",
            "SERVICE_PACK",
            "TOOL",
            "UPDATE_ROLLUP",
            "UPDATE",
        ]
    ]
    excludes: _list[str]
    exclusivePatches: _list[str]

@typing.type_check_only
class YumSettings(typing.TypedDict, total=False):
    excludes: _list[str]
    exclusivePackages: _list[str]
    minimal: bool
    security: bool

@typing.type_check_only
class ZypperSettings(typing.TypedDict, total=False):
    categories: _list[str]
    excludes: _list[str]
    exclusivePatches: _list[str]
    severities: _list[str]
    withOptional: bool
    withUpdate: bool
