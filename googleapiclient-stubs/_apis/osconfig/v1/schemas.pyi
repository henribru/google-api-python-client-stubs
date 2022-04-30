import typing

import typing_extensions

_list = list

@typing.type_check_only
class AptSettings(typing_extensions.TypedDict, total=False):
    excludes: _list[str]
    exclusivePackages: _list[str]
    type: typing_extensions.Literal["TYPE_UNSPECIFIED", "DIST", "UPGRADE"]

@typing.type_check_only
class CVSSv3(typing_extensions.TypedDict, total=False):
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
    exploitabilityScore: float
    impactScore: float
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
class CancelOperationRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class CancelPatchJobRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Date(typing_extensions.TypedDict, total=False):
    day: int
    month: int
    year: int

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class ExecStep(typing_extensions.TypedDict, total=False):
    linuxExecStepConfig: ExecStepConfig
    windowsExecStepConfig: ExecStepConfig

@typing.type_check_only
class ExecStepConfig(typing_extensions.TypedDict, total=False):
    allowedSuccessCodes: _list[int]
    gcsObject: GcsObject
    interpreter: typing_extensions.Literal[
        "INTERPRETER_UNSPECIFIED", "NONE", "SHELL", "POWERSHELL"
    ]
    localPath: str

@typing.type_check_only
class ExecutePatchJobRequest(typing_extensions.TypedDict, total=False):
    description: str
    displayName: str
    dryRun: bool
    duration: str
    instanceFilter: PatchInstanceFilter
    patchConfig: PatchConfig
    rollout: PatchRollout

@typing.type_check_only
class FixedOrPercent(typing_extensions.TypedDict, total=False):
    fixed: int
    percent: int

@typing.type_check_only
class GcsObject(typing_extensions.TypedDict, total=False):
    bucket: str
    generationNumber: str
    object: str

@typing.type_check_only
class GooSettings(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class GoogleCloudOsconfigV1__OSPolicyAssignmentOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    apiMethod: typing_extensions.Literal[
        "API_METHOD_UNSPECIFIED", "CREATE", "UPDATE", "DELETE"
    ]
    osPolicyAssignment: str
    rolloutStartTime: str
    rolloutState: typing_extensions.Literal[
        "ROLLOUT_STATE_UNSPECIFIED",
        "IN_PROGRESS",
        "CANCELLING",
        "CANCELLED",
        "SUCCEEDED",
    ]
    rolloutUpdateTime: str

@typing.type_check_only
class Inventory(typing_extensions.TypedDict, total=False):
    items: dict[str, typing.Any]
    name: str
    osInfo: InventoryOsInfo
    updateTime: str

@typing.type_check_only
class InventoryItem(typing_extensions.TypedDict, total=False):
    availablePackage: InventorySoftwarePackage
    createTime: str
    id: str
    installedPackage: InventorySoftwarePackage
    originType: typing_extensions.Literal["ORIGIN_TYPE_UNSPECIFIED", "INVENTORY_REPORT"]
    type: typing_extensions.Literal[
        "TYPE_UNSPECIFIED", "INSTALLED_PACKAGE", "AVAILABLE_PACKAGE"
    ]
    updateTime: str

@typing.type_check_only
class InventoryOsInfo(typing_extensions.TypedDict, total=False):
    architecture: str
    hostname: str
    kernelRelease: str
    kernelVersion: str
    longName: str
    osconfigAgentVersion: str
    shortName: str
    version: str

@typing.type_check_only
class InventorySoftwarePackage(typing_extensions.TypedDict, total=False):
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
class InventoryVersionedPackage(typing_extensions.TypedDict, total=False):
    architecture: str
    packageName: str
    version: str

@typing.type_check_only
class InventoryWindowsApplication(typing_extensions.TypedDict, total=False):
    displayName: str
    displayVersion: str
    helpLink: str
    installDate: Date
    publisher: str

@typing.type_check_only
class InventoryWindowsQuickFixEngineeringPackage(
    typing_extensions.TypedDict, total=False
):
    caption: str
    description: str
    hotFixId: str
    installTime: str

@typing.type_check_only
class InventoryWindowsUpdatePackage(typing_extensions.TypedDict, total=False):
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
class InventoryWindowsUpdatePackageWindowsUpdateCategory(
    typing_extensions.TypedDict, total=False
):
    id: str
    name: str

@typing.type_check_only
class InventoryZypperPatch(typing_extensions.TypedDict, total=False):
    category: str
    patchName: str
    severity: str
    summary: str

@typing.type_check_only
class ListInventoriesResponse(typing_extensions.TypedDict, total=False):
    inventories: _list[Inventory]
    nextPageToken: str

@typing.type_check_only
class ListOSPolicyAssignmentReportsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    osPolicyAssignmentReports: _list[OSPolicyAssignmentReport]

@typing.type_check_only
class ListOSPolicyAssignmentRevisionsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    osPolicyAssignments: _list[OSPolicyAssignment]

@typing.type_check_only
class ListOSPolicyAssignmentsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    osPolicyAssignments: _list[OSPolicyAssignment]

@typing.type_check_only
class ListPatchDeploymentsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    patchDeployments: _list[PatchDeployment]

@typing.type_check_only
class ListPatchJobInstanceDetailsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    patchJobInstanceDetails: _list[PatchJobInstanceDetails]

@typing.type_check_only
class ListPatchJobsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    patchJobs: _list[PatchJob]

@typing.type_check_only
class ListVulnerabilityReportsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    vulnerabilityReports: _list[VulnerabilityReport]

@typing.type_check_only
class MonthlySchedule(typing_extensions.TypedDict, total=False):
    monthDay: int
    weekDayOfMonth: WeekDayOfMonth

@typing.type_check_only
class OSPolicy(typing_extensions.TypedDict, total=False):
    allowNoResourceGroupMatch: bool
    description: str
    id: str
    mode: typing_extensions.Literal["MODE_UNSPECIFIED", "VALIDATION", "ENFORCEMENT"]
    resourceGroups: _list[OSPolicyResourceGroup]

@typing.type_check_only
class OSPolicyAssignment(typing_extensions.TypedDict, total=False):
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
    rolloutState: typing_extensions.Literal[
        "ROLLOUT_STATE_UNSPECIFIED",
        "IN_PROGRESS",
        "CANCELLING",
        "CANCELLED",
        "SUCCEEDED",
    ]
    uid: str

@typing.type_check_only
class OSPolicyAssignmentInstanceFilter(typing_extensions.TypedDict, total=False):
    all: bool
    exclusionLabels: _list[OSPolicyAssignmentLabelSet]
    inclusionLabels: _list[OSPolicyAssignmentLabelSet]
    inventories: _list[OSPolicyAssignmentInstanceFilterInventory]

@typing.type_check_only
class OSPolicyAssignmentInstanceFilterInventory(
    typing_extensions.TypedDict, total=False
):
    osShortName: str
    osVersion: str

@typing.type_check_only
class OSPolicyAssignmentLabelSet(typing_extensions.TypedDict, total=False):
    labels: dict[str, typing.Any]

@typing.type_check_only
class OSPolicyAssignmentOperationMetadata(typing_extensions.TypedDict, total=False):
    apiMethod: typing_extensions.Literal[
        "API_METHOD_UNSPECIFIED", "CREATE", "UPDATE", "DELETE"
    ]
    osPolicyAssignment: str
    rolloutStartTime: str
    rolloutState: typing_extensions.Literal[
        "ROLLOUT_STATE_UNSPECIFIED",
        "IN_PROGRESS",
        "CANCELLING",
        "CANCELLED",
        "SUCCEEDED",
    ]
    rolloutUpdateTime: str

@typing.type_check_only
class OSPolicyAssignmentReport(typing_extensions.TypedDict, total=False):
    instance: str
    lastRunId: str
    name: str
    osPolicyAssignment: str
    osPolicyCompliances: _list[OSPolicyAssignmentReportOSPolicyCompliance]
    updateTime: str

@typing.type_check_only
class OSPolicyAssignmentReportOSPolicyCompliance(
    typing_extensions.TypedDict, total=False
):
    complianceState: typing_extensions.Literal["UNKNOWN", "COMPLIANT", "NON_COMPLIANT"]
    complianceStateReason: str
    osPolicyId: str
    osPolicyResourceCompliances: _list[
        OSPolicyAssignmentReportOSPolicyComplianceOSPolicyResourceCompliance
    ]

@typing.type_check_only
class OSPolicyAssignmentReportOSPolicyComplianceOSPolicyResourceCompliance(
    typing_extensions.TypedDict, total=False
):
    complianceState: typing_extensions.Literal["UNKNOWN", "COMPLIANT", "NON_COMPLIANT"]
    complianceStateReason: str
    configSteps: _list[
        OSPolicyAssignmentReportOSPolicyComplianceOSPolicyResourceComplianceOSPolicyResourceConfigStep
    ]
    execResourceOutput: OSPolicyAssignmentReportOSPolicyComplianceOSPolicyResourceComplianceExecResourceOutput
    osPolicyResourceId: str

@typing.type_check_only
class OSPolicyAssignmentReportOSPolicyComplianceOSPolicyResourceComplianceExecResourceOutput(
    typing_extensions.TypedDict, total=False
):
    enforcementOutput: str

@typing.type_check_only
class OSPolicyAssignmentReportOSPolicyComplianceOSPolicyResourceComplianceOSPolicyResourceConfigStep(
    typing_extensions.TypedDict, total=False
):
    errorMessage: str
    type: typing_extensions.Literal[
        "TYPE_UNSPECIFIED",
        "VALIDATION",
        "DESIRED_STATE_CHECK",
        "DESIRED_STATE_ENFORCEMENT",
        "DESIRED_STATE_CHECK_POST_ENFORCEMENT",
    ]

@typing.type_check_only
class OSPolicyAssignmentRollout(typing_extensions.TypedDict, total=False):
    disruptionBudget: FixedOrPercent
    minWaitDuration: str

@typing.type_check_only
class OSPolicyInventoryFilter(typing_extensions.TypedDict, total=False):
    osShortName: str
    osVersion: str

@typing.type_check_only
class OSPolicyResource(typing_extensions.TypedDict, total=False):
    exec: OSPolicyResourceExecResource
    file: OSPolicyResourceFileResource
    id: str
    pkg: OSPolicyResourcePackageResource
    repository: OSPolicyResourceRepositoryResource

@typing.type_check_only
class OSPolicyResourceExecResource(typing_extensions.TypedDict, total=False):
    enforce: OSPolicyResourceExecResourceExec
    validate: OSPolicyResourceExecResourceExec

@typing.type_check_only
class OSPolicyResourceExecResourceExec(typing_extensions.TypedDict, total=False):
    args: _list[str]
    file: OSPolicyResourceFile
    interpreter: typing_extensions.Literal[
        "INTERPRETER_UNSPECIFIED", "NONE", "SHELL", "POWERSHELL"
    ]
    outputFilePath: str
    script: str

@typing.type_check_only
class OSPolicyResourceFile(typing_extensions.TypedDict, total=False):
    allowInsecure: bool
    gcs: OSPolicyResourceFileGcs
    localPath: str
    remote: OSPolicyResourceFileRemote

@typing.type_check_only
class OSPolicyResourceFileGcs(typing_extensions.TypedDict, total=False):
    bucket: str
    generation: str
    object: str

@typing.type_check_only
class OSPolicyResourceFileRemote(typing_extensions.TypedDict, total=False):
    sha256Checksum: str
    uri: str

@typing.type_check_only
class OSPolicyResourceFileResource(typing_extensions.TypedDict, total=False):
    content: str
    file: OSPolicyResourceFile
    path: str
    permissions: str
    state: typing_extensions.Literal[
        "DESIRED_STATE_UNSPECIFIED", "PRESENT", "ABSENT", "CONTENTS_MATCH"
    ]

@typing.type_check_only
class OSPolicyResourceGroup(typing_extensions.TypedDict, total=False):
    inventoryFilters: _list[OSPolicyInventoryFilter]
    resources: _list[OSPolicyResource]

@typing.type_check_only
class OSPolicyResourcePackageResource(typing_extensions.TypedDict, total=False):
    apt: OSPolicyResourcePackageResourceAPT
    deb: OSPolicyResourcePackageResourceDeb
    desiredState: typing_extensions.Literal[
        "DESIRED_STATE_UNSPECIFIED", "INSTALLED", "REMOVED"
    ]
    googet: OSPolicyResourcePackageResourceGooGet
    msi: OSPolicyResourcePackageResourceMSI
    rpm: OSPolicyResourcePackageResourceRPM
    yum: OSPolicyResourcePackageResourceYUM
    zypper: OSPolicyResourcePackageResourceZypper

@typing.type_check_only
class OSPolicyResourcePackageResourceAPT(typing_extensions.TypedDict, total=False):
    name: str

@typing.type_check_only
class OSPolicyResourcePackageResourceDeb(typing_extensions.TypedDict, total=False):
    pullDeps: bool
    source: OSPolicyResourceFile

@typing.type_check_only
class OSPolicyResourcePackageResourceGooGet(typing_extensions.TypedDict, total=False):
    name: str

@typing.type_check_only
class OSPolicyResourcePackageResourceMSI(typing_extensions.TypedDict, total=False):
    properties: _list[str]
    source: OSPolicyResourceFile

@typing.type_check_only
class OSPolicyResourcePackageResourceRPM(typing_extensions.TypedDict, total=False):
    pullDeps: bool
    source: OSPolicyResourceFile

@typing.type_check_only
class OSPolicyResourcePackageResourceYUM(typing_extensions.TypedDict, total=False):
    name: str

@typing.type_check_only
class OSPolicyResourcePackageResourceZypper(typing_extensions.TypedDict, total=False):
    name: str

@typing.type_check_only
class OSPolicyResourceRepositoryResource(typing_extensions.TypedDict, total=False):
    apt: OSPolicyResourceRepositoryResourceAptRepository
    goo: OSPolicyResourceRepositoryResourceGooRepository
    yum: OSPolicyResourceRepositoryResourceYumRepository
    zypper: OSPolicyResourceRepositoryResourceZypperRepository

@typing.type_check_only
class OSPolicyResourceRepositoryResourceAptRepository(
    typing_extensions.TypedDict, total=False
):
    archiveType: typing_extensions.Literal["ARCHIVE_TYPE_UNSPECIFIED", "DEB", "DEB_SRC"]
    components: _list[str]
    distribution: str
    gpgKey: str
    uri: str

@typing.type_check_only
class OSPolicyResourceRepositoryResourceGooRepository(
    typing_extensions.TypedDict, total=False
):
    name: str
    url: str

@typing.type_check_only
class OSPolicyResourceRepositoryResourceYumRepository(
    typing_extensions.TypedDict, total=False
):
    baseUrl: str
    displayName: str
    gpgKeys: _list[str]
    id: str

@typing.type_check_only
class OSPolicyResourceRepositoryResourceZypperRepository(
    typing_extensions.TypedDict, total=False
):
    baseUrl: str
    displayName: str
    gpgKeys: _list[str]
    id: str

@typing.type_check_only
class OneTimeSchedule(typing_extensions.TypedDict, total=False):
    executeTime: str

@typing.type_check_only
class Operation(typing_extensions.TypedDict, total=False):
    done: bool
    error: Status
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class PatchConfig(typing_extensions.TypedDict, total=False):
    apt: AptSettings
    goo: GooSettings
    migInstancesAllowed: bool
    postStep: ExecStep
    preStep: ExecStep
    rebootConfig: typing_extensions.Literal[
        "REBOOT_CONFIG_UNSPECIFIED", "DEFAULT", "ALWAYS", "NEVER"
    ]
    windowsUpdate: WindowsUpdateSettings
    yum: YumSettings
    zypper: ZypperSettings

@typing.type_check_only
class PatchDeployment(typing_extensions.TypedDict, total=False):
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
    state: typing_extensions.Literal["STATE_UNSPECIFIED", "ACTIVE", "PAUSED"]
    updateTime: str

@typing.type_check_only
class PatchInstanceFilter(typing_extensions.TypedDict, total=False):
    all: bool
    groupLabels: _list[PatchInstanceFilterGroupLabel]
    instanceNamePrefixes: _list[str]
    instances: _list[str]
    zones: _list[str]

@typing.type_check_only
class PatchInstanceFilterGroupLabel(typing_extensions.TypedDict, total=False):
    labels: dict[str, typing.Any]

@typing.type_check_only
class PatchJob(typing_extensions.TypedDict, total=False):
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
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "STARTED",
        "INSTANCE_LOOKUP",
        "PATCHING",
        "SUCCEEDED",
        "COMPLETED_WITH_ERRORS",
        "CANCELED",
        "TIMED_OUT",
    ]
    updateTime: str

@typing.type_check_only
class PatchJobInstanceDetails(typing_extensions.TypedDict, total=False):
    attemptCount: str
    failureReason: str
    instanceSystemId: str
    name: str
    state: typing_extensions.Literal[
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
    ]

@typing.type_check_only
class PatchJobInstanceDetailsSummary(typing_extensions.TypedDict, total=False):
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
    startedInstanceCount: str
    succeededInstanceCount: str
    succeededRebootRequiredInstanceCount: str
    timedOutInstanceCount: str

@typing.type_check_only
class PatchRollout(typing_extensions.TypedDict, total=False):
    disruptionBudget: FixedOrPercent
    mode: typing_extensions.Literal[
        "MODE_UNSPECIFIED", "ZONE_BY_ZONE", "CONCURRENT_ZONES"
    ]

@typing.type_check_only
class PausePatchDeploymentRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class RecurringSchedule(typing_extensions.TypedDict, total=False):
    endTime: str
    frequency: typing_extensions.Literal[
        "FREQUENCY_UNSPECIFIED", "WEEKLY", "MONTHLY", "DAILY"
    ]
    lastExecuteTime: str
    monthly: MonthlySchedule
    nextExecuteTime: str
    startTime: str
    timeOfDay: TimeOfDay
    timeZone: TimeZone
    weekly: WeeklySchedule

@typing.type_check_only
class ResumePatchDeploymentRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class TimeOfDay(typing_extensions.TypedDict, total=False):
    hours: int
    minutes: int
    nanos: int
    seconds: int

@typing.type_check_only
class TimeZone(typing_extensions.TypedDict, total=False):
    id: str
    version: str

@typing.type_check_only
class VulnerabilityReport(typing_extensions.TypedDict, total=False):
    name: str
    updateTime: str
    vulnerabilities: _list[VulnerabilityReportVulnerability]

@typing.type_check_only
class VulnerabilityReportVulnerability(typing_extensions.TypedDict, total=False):
    availableInventoryItemIds: _list[str]
    createTime: str
    details: VulnerabilityReportVulnerabilityDetails
    installedInventoryItemIds: _list[str]
    items: _list[VulnerabilityReportVulnerabilityItem]
    updateTime: str

@typing.type_check_only
class VulnerabilityReportVulnerabilityDetails(typing_extensions.TypedDict, total=False):
    cve: str
    cvssV2Score: float
    cvssV3: CVSSv3
    description: str
    references: _list[VulnerabilityReportVulnerabilityDetailsReference]
    severity: str

@typing.type_check_only
class VulnerabilityReportVulnerabilityDetailsReference(
    typing_extensions.TypedDict, total=False
):
    source: str
    url: str

@typing.type_check_only
class VulnerabilityReportVulnerabilityItem(typing_extensions.TypedDict, total=False):
    availableInventoryItemId: str
    fixedCpeUri: str
    installedInventoryItemId: str
    upstreamFix: str

@typing.type_check_only
class WeekDayOfMonth(typing_extensions.TypedDict, total=False):
    dayOfWeek: typing_extensions.Literal[
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
class WeeklySchedule(typing_extensions.TypedDict, total=False):
    dayOfWeek: typing_extensions.Literal[
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
class WindowsUpdateSettings(typing_extensions.TypedDict, total=False):
    classifications: _list[str]
    excludes: _list[str]
    exclusivePatches: _list[str]

@typing.type_check_only
class YumSettings(typing_extensions.TypedDict, total=False):
    excludes: _list[str]
    exclusivePackages: _list[str]
    minimal: bool
    security: bool

@typing.type_check_only
class ZypperSettings(typing_extensions.TypedDict, total=False):
    categories: _list[str]
    excludes: _list[str]
    exclusivePatches: _list[str]
    severities: _list[str]
    withOptional: bool
    withUpdate: bool
