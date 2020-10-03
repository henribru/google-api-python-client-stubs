import typing

import typing_extensions

class TimeOfDay(typing_extensions.TypedDict, total=False):
    seconds: int
    nanos: int
    hours: int
    minutes: int

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

class OneTimeSchedule(typing_extensions.TypedDict, total=False):
    executeTime: str

class PatchJobInstanceDetailsSummary(typing_extensions.TypedDict, total=False):
    noAgentDetectedInstanceCount: str
    prePatchStepInstanceCount: str
    pendingInstanceCount: str
    inactiveInstanceCount: str
    startedInstanceCount: str
    downloadingPatchesInstanceCount: str
    failedInstanceCount: str
    rebootingInstanceCount: str
    timedOutInstanceCount: str
    succeededInstanceCount: str
    postPatchStepInstanceCount: str
    succeededRebootRequiredInstanceCount: str
    ackedInstanceCount: str
    applyingPatchesInstanceCount: str
    notifiedInstanceCount: str

class PatchDeployment(typing_extensions.TypedDict, total=False):
    createTime: str
    patchConfig: PatchConfig
    lastExecuteTime: str
    description: str
    instanceFilter: PatchInstanceFilter
    rollout: PatchRollout
    updateTime: str
    name: str
    duration: str
    oneTimeSchedule: OneTimeSchedule
    recurringSchedule: RecurringSchedule

class YumSettings(typing_extensions.TypedDict, total=False):
    exclusivePackages: typing.List[str]
    excludes: typing.List[str]
    minimal: bool
    security: bool

class GcsObject(typing_extensions.TypedDict, total=False):
    generationNumber: str
    object: str
    bucket: str

class ListPatchJobInstanceDetailsResponse(typing_extensions.TypedDict, total=False):
    patchJobInstanceDetails: typing.List[PatchJobInstanceDetails]
    nextPageToken: str

class ZypperSettings(typing_extensions.TypedDict, total=False):
    excludes: typing.List[str]
    exclusivePatches: typing.List[str]
    severities: typing.List[str]
    withUpdate: bool
    withOptional: bool
    categories: typing.List[str]

class AptSettings(typing_extensions.TypedDict, total=False):
    excludes: typing.List[str]
    type: typing_extensions.Literal["TYPE_UNSPECIFIED", "DIST", "UPGRADE"]
    exclusivePackages: typing.List[str]

class PatchInstanceFilter(typing_extensions.TypedDict, total=False):
    zones: typing.List[str]
    instanceNamePrefixes: typing.List[str]
    all: bool
    instances: typing.List[str]
    groupLabels: typing.List[PatchInstanceFilterGroupLabel]

class ExecStepConfig(typing_extensions.TypedDict, total=False):
    interpreter: typing_extensions.Literal[
        "INTERPRETER_UNSPECIFIED", "SHELL", "POWERSHELL"
    ]
    gcsObject: GcsObject
    allowedSuccessCodes: typing.List[int]
    localPath: str

class PatchJob(typing_extensions.TypedDict, total=False):
    displayName: str
    patchConfig: PatchConfig
    description: str
    name: str
    errorMessage: str
    updateTime: str
    percentComplete: float
    instanceDetailsSummary: PatchJobInstanceDetailsSummary
    duration: str
    rollout: PatchRollout
    instanceFilter: PatchInstanceFilter
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
    patchDeployment: str
    dryRun: bool
    createTime: str

class Empty(typing_extensions.TypedDict, total=False): ...

class RecurringSchedule(typing_extensions.TypedDict, total=False):
    weekly: WeeklySchedule
    frequency: typing_extensions.Literal["FREQUENCY_UNSPECIFIED", "WEEKLY", "MONTHLY"]
    startTime: str
    nextExecuteTime: str
    lastExecuteTime: str
    monthly: MonthlySchedule
    endTime: str
    timeZone: TimeZone
    timeOfDay: TimeOfDay

class PatchConfig(typing_extensions.TypedDict, total=False):
    preStep: ExecStep
    windowsUpdate: WindowsUpdateSettings
    goo: GooSettings
    yum: YumSettings
    postStep: ExecStep
    apt: AptSettings
    zypper: ZypperSettings
    rebootConfig: typing_extensions.Literal[
        "REBOOT_CONFIG_UNSPECIFIED", "DEFAULT", "ALWAYS", "NEVER"
    ]

class WindowsUpdateSettings(typing_extensions.TypedDict, total=False):
    exclusivePatches: typing.List[str]
    classifications: typing.List[str]
    excludes: typing.List[str]

class TimeZone(typing_extensions.TypedDict, total=False):
    version: str
    id: str

class GooSettings(typing_extensions.TypedDict, total=False): ...

class ListPatchJobsResponse(typing_extensions.TypedDict, total=False):
    patchJobs: typing.List[PatchJob]
    nextPageToken: str

class ExecStep(typing_extensions.TypedDict, total=False):
    windowsExecStepConfig: ExecStepConfig
    linuxExecStepConfig: ExecStepConfig

class PatchInstanceFilterGroupLabel(typing_extensions.TypedDict, total=False):
    labels: typing.Dict[str, typing.Any]

class CancelPatchJobRequest(typing_extensions.TypedDict, total=False): ...

class PatchRollout(typing_extensions.TypedDict, total=False):
    disruptionBudget: FixedOrPercent
    mode: typing_extensions.Literal[
        "MODE_UNSPECIFIED", "ZONE_BY_ZONE", "CONCURRENT_ZONES"
    ]

class ListPatchDeploymentsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    patchDeployments: typing.List[PatchDeployment]

class MonthlySchedule(typing_extensions.TypedDict, total=False):
    monthDay: int
    weekDayOfMonth: WeekDayOfMonth

class PatchJobInstanceDetails(typing_extensions.TypedDict, total=False):
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
    instanceSystemId: str
    attemptCount: str
    failureReason: str

class WeekDayOfMonth(typing_extensions.TypedDict, total=False):
    weekOrdinal: int
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

class FixedOrPercent(typing_extensions.TypedDict, total=False):
    percent: int
    fixed: int

class ExecutePatchJobRequest(typing_extensions.TypedDict, total=False):
    rollout: PatchRollout
    dryRun: bool
    description: str
    displayName: str
    duration: str
    patchConfig: PatchConfig
    instanceFilter: PatchInstanceFilter
