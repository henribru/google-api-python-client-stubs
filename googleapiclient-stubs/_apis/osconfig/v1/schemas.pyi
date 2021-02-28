import typing

import typing_extensions
@typing.type_check_only
class AptSettings(typing_extensions.TypedDict, total=False):
    excludes: typing.List[str]
    exclusivePackages: typing.List[str]
    type: typing_extensions.Literal["TYPE_UNSPECIFIED", "DIST", "UPGRADE"]

@typing.type_check_only
class CancelPatchJobRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class ExecStep(typing_extensions.TypedDict, total=False):
    linuxExecStepConfig: ExecStepConfig
    windowsExecStepConfig: ExecStepConfig

@typing.type_check_only
class ExecStepConfig(typing_extensions.TypedDict, total=False):
    allowedSuccessCodes: typing.List[int]
    gcsObject: GcsObject
    interpreter: typing_extensions.Literal[
        "INTERPRETER_UNSPECIFIED", "SHELL", "POWERSHELL"
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
class Inventory(typing_extensions.TypedDict, total=False):
    items: typing.Dict[str, typing.Any]
    osInfo: InventoryOsInfo

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
class InventoryWindowsQuickFixEngineeringPackage(
    typing_extensions.TypedDict, total=False
):
    caption: str
    description: str
    hotFixId: str
    installTime: str

@typing.type_check_only
class InventoryWindowsUpdatePackage(typing_extensions.TypedDict, total=False):
    categories: typing.List[InventoryWindowsUpdatePackageWindowsUpdateCategory]
    description: str
    kbArticleIds: typing.List[str]
    lastDeploymentChangeTime: str
    moreInfoUrls: typing.List[str]
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
class ListPatchDeploymentsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    patchDeployments: typing.List[PatchDeployment]

@typing.type_check_only
class ListPatchJobInstanceDetailsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    patchJobInstanceDetails: typing.List[PatchJobInstanceDetails]

@typing.type_check_only
class ListPatchJobsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    patchJobs: typing.List[PatchJob]

@typing.type_check_only
class MonthlySchedule(typing_extensions.TypedDict, total=False):
    monthDay: int
    weekDayOfMonth: WeekDayOfMonth

@typing.type_check_only
class OneTimeSchedule(typing_extensions.TypedDict, total=False):
    executeTime: str

@typing.type_check_only
class PatchConfig(typing_extensions.TypedDict, total=False):
    apt: AptSettings
    goo: GooSettings
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
    updateTime: str

@typing.type_check_only
class PatchInstanceFilter(typing_extensions.TypedDict, total=False):
    all: bool
    groupLabels: typing.List[PatchInstanceFilterGroupLabel]
    instanceNamePrefixes: typing.List[str]
    instances: typing.List[str]
    zones: typing.List[str]

@typing.type_check_only
class PatchInstanceFilterGroupLabel(typing_extensions.TypedDict, total=False):
    labels: typing.Dict[str, typing.Any]

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
class RecurringSchedule(typing_extensions.TypedDict, total=False):
    endTime: str
    frequency: typing_extensions.Literal["FREQUENCY_UNSPECIFIED", "WEEKLY", "MONTHLY"]
    lastExecuteTime: str
    monthly: MonthlySchedule
    nextExecuteTime: str
    startTime: str
    timeOfDay: TimeOfDay
    timeZone: TimeZone
    weekly: WeeklySchedule

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
    classifications: typing.List[str]
    excludes: typing.List[str]
    exclusivePatches: typing.List[str]

@typing.type_check_only
class YumSettings(typing_extensions.TypedDict, total=False):
    excludes: typing.List[str]
    exclusivePackages: typing.List[str]
    minimal: bool
    security: bool

@typing.type_check_only
class ZypperSettings(typing_extensions.TypedDict, total=False):
    categories: typing.List[str]
    excludes: typing.List[str]
    exclusivePatches: typing.List[str]
    severities: typing.List[str]
    withOptional: bool
    withUpdate: bool
