import typing

import typing_extensions

class AptRepository(typing_extensions.TypedDict, total=False):
    gpgKey: str
    uri: str
    components: typing.List[str]
    distribution: str
    archiveType: typing_extensions.Literal["ARCHIVE_TYPE_UNSPECIFIED", "DEB", "DEB_SRC"]

class CancelPatchJobRequest(typing_extensions.TypedDict, total=False): ...

class PatchJobInstanceDetailsSummary(typing_extensions.TypedDict, total=False):
    prePatchStepInstanceCount: str
    postPatchStepInstanceCount: str
    failedInstanceCount: str
    startedInstanceCount: str
    pendingInstanceCount: str
    ackedInstanceCount: str
    notifiedInstanceCount: str
    inactiveInstanceCount: str
    rebootingInstanceCount: str
    downloadingPatchesInstanceCount: str
    succeededRebootRequiredInstanceCount: str
    noAgentDetectedInstanceCount: str
    timedOutInstanceCount: str
    applyingPatchesInstanceCount: str
    succeededInstanceCount: str

class SoftwareRecipeArtifactRemote(typing_extensions.TypedDict, total=False):
    uri: str
    checksum: str

class GuestPolicy(typing_extensions.TypedDict, total=False):
    description: str
    packages: typing.List[Package]
    etag: str
    name: str
    packageRepositories: typing.List[PackageRepository]
    recipes: typing.List[SoftwareRecipe]
    createTime: str
    assignment: Assignment
    updateTime: str

class SoftwareRecipeStepExtractArchive(typing_extensions.TypedDict, total=False):
    destination: str
    artifactId: str
    type: typing_extensions.Literal[
        "ARCHIVE_TYPE_UNSPECIFIED",
        "TAR",
        "TAR_GZIP",
        "TAR_BZIP",
        "TAR_LZMA",
        "TAR_XZ",
        "ZIP",
    ]

class ExecutePatchJobRequest(typing_extensions.TypedDict, total=False):
    patchConfig: PatchConfig
    instanceFilter: PatchInstanceFilter
    dryRun: bool
    duration: str
    description: str
    rollout: PatchRollout
    displayName: str

class AssignmentOsType(typing_extensions.TypedDict, total=False):
    osVersion: str
    osArchitecture: str
    osShortName: str

class ListPatchJobInstanceDetailsResponse(typing_extensions.TypedDict, total=False):
    patchJobInstanceDetails: typing.List[PatchJobInstanceDetails]
    nextPageToken: str

class EffectiveGuestPolicy(typing_extensions.TypedDict, total=False):
    softwareRecipes: typing.List[EffectiveGuestPolicySourcedSoftwareRecipe]
    packageRepositories: typing.List[EffectiveGuestPolicySourcedPackageRepository]
    packages: typing.List[EffectiveGuestPolicySourcedPackage]

class SoftwareRecipe(typing_extensions.TypedDict, total=False):
    installSteps: typing.List[SoftwareRecipeStep]
    artifacts: typing.List[SoftwareRecipeArtifact]
    name: str
    version: str
    desiredState: typing_extensions.Literal[
        "DESIRED_STATE_UNSPECIFIED", "INSTALLED", "UPDATED", "REMOVED"
    ]
    updateSteps: typing.List[SoftwareRecipeStep]

class SoftwareRecipeStepRunScript(typing_extensions.TypedDict, total=False):
    allowedExitCodes: typing.List[int]
    script: str
    interpreter: typing_extensions.Literal[
        "INTERPRETER_UNSPECIFIED", "SHELL", "POWERSHELL"
    ]

class SoftwareRecipeStepInstallDpkg(typing_extensions.TypedDict, total=False):
    artifactId: str

class SoftwareRecipeStep(typing_extensions.TypedDict, total=False):
    rpmInstallation: SoftwareRecipeStepInstallRpm
    archiveExtraction: SoftwareRecipeStepExtractArchive
    scriptRun: SoftwareRecipeStepRunScript
    dpkgInstallation: SoftwareRecipeStepInstallDpkg
    msiInstallation: SoftwareRecipeStepInstallMsi
    fileCopy: SoftwareRecipeStepCopyFile
    fileExec: SoftwareRecipeStepExecFile

class EffectiveGuestPolicySourcedPackage(typing_extensions.TypedDict, total=False):
    package: Package
    source: str

class PatchJob(typing_extensions.TypedDict, total=False):
    patchDeployment: str
    instanceFilter: PatchInstanceFilter
    description: str
    updateTime: str
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
    patchConfig: PatchConfig
    displayName: str
    createTime: str
    percentComplete: float
    instanceDetailsSummary: PatchJobInstanceDetailsSummary
    rollout: PatchRollout
    name: str
    duration: str
    errorMessage: str
    dryRun: bool

class Assignment(typing_extensions.TypedDict, total=False):
    osTypes: typing.List[AssignmentOsType]
    zones: typing.List[str]
    instanceNamePrefixes: typing.List[str]
    instances: typing.List[str]
    groupLabels: typing.List[AssignmentGroupLabel]

class PatchConfig(typing_extensions.TypedDict, total=False):
    apt: AptSettings
    goo: GooSettings
    zypper: ZypperSettings
    yum: YumSettings
    postStep: ExecStep
    rebootConfig: typing_extensions.Literal[
        "REBOOT_CONFIG_UNSPECIFIED", "DEFAULT", "ALWAYS", "NEVER"
    ]
    windowsUpdate: WindowsUpdateSettings
    preStep: ExecStep

class WindowsUpdateSettings(typing_extensions.TypedDict, total=False):
    excludes: typing.List[str]
    exclusivePatches: typing.List[str]
    classifications: typing.List[str]

class ZypperSettings(typing_extensions.TypedDict, total=False):
    severities: typing.List[str]
    excludes: typing.List[str]
    categories: typing.List[str]
    exclusivePatches: typing.List[str]
    withUpdate: bool
    withOptional: bool

class AptSettings(typing_extensions.TypedDict, total=False):
    type: typing_extensions.Literal["TYPE_UNSPECIFIED", "DIST", "UPGRADE"]
    excludes: typing.List[str]
    exclusivePackages: typing.List[str]

class YumSettings(typing_extensions.TypedDict, total=False):
    exclusivePackages: typing.List[str]
    excludes: typing.List[str]
    security: bool
    minimal: bool

class SoftwareRecipeStepCopyFile(typing_extensions.TypedDict, total=False):
    destination: str
    artifactId: str
    overwrite: bool
    permissions: str

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

class ExecStep(typing_extensions.TypedDict, total=False):
    linuxExecStepConfig: ExecStepConfig
    windowsExecStepConfig: ExecStepConfig

class YumRepository(typing_extensions.TypedDict, total=False):
    id: str
    gpgKeys: typing.List[str]
    displayName: str
    baseUrl: str

class RecurringSchedule(typing_extensions.TypedDict, total=False):
    monthly: MonthlySchedule
    frequency: typing_extensions.Literal["FREQUENCY_UNSPECIFIED", "WEEKLY", "MONTHLY"]
    timeZone: TimeZone
    lastExecuteTime: str
    nextExecuteTime: str
    weekly: WeeklySchedule
    timeOfDay: TimeOfDay
    endTime: str
    startTime: str

class GooSettings(typing_extensions.TypedDict, total=False): ...

class EffectiveGuestPolicySourcedSoftwareRecipe(
    typing_extensions.TypedDict, total=False
):
    source: str
    softwareRecipe: SoftwareRecipe

class FixedOrPercent(typing_extensions.TypedDict, total=False):
    fixed: int
    percent: int

class GcsObject(typing_extensions.TypedDict, total=False):
    object: str
    bucket: str
    generationNumber: str

class ListGuestPoliciesResponse(typing_extensions.TypedDict, total=False):
    guestPolicies: typing.List[GuestPolicy]
    nextPageToken: str

class LookupEffectiveGuestPolicyRequest(typing_extensions.TypedDict, total=False):
    osShortName: str
    osArchitecture: str
    osVersion: str

class PatchInstanceFilter(typing_extensions.TypedDict, total=False):
    instances: typing.List[str]
    all: bool
    zones: typing.List[str]
    groupLabels: typing.List[PatchInstanceFilterGroupLabel]
    instanceNamePrefixes: typing.List[str]

class GooRepository(typing_extensions.TypedDict, total=False):
    name: str
    url: str

class SoftwareRecipeArtifactGcs(typing_extensions.TypedDict, total=False):
    bucket: str
    object: str
    generation: str

class PatchDeployment(typing_extensions.TypedDict, total=False):
    rollout: PatchRollout
    createTime: str
    description: str
    patchConfig: PatchConfig
    duration: str
    instanceFilter: PatchInstanceFilter
    recurringSchedule: RecurringSchedule
    oneTimeSchedule: OneTimeSchedule
    name: str
    updateTime: str
    lastExecuteTime: str

class MonthlySchedule(typing_extensions.TypedDict, total=False):
    monthDay: int
    weekDayOfMonth: WeekDayOfMonth

class AssignmentGroupLabel(typing_extensions.TypedDict, total=False):
    labels: typing.Dict[str, typing.Any]

class EffectiveGuestPolicySourcedPackageRepository(
    typing_extensions.TypedDict, total=False
):
    source: str
    packageRepository: PackageRepository

class SoftwareRecipeArtifact(typing_extensions.TypedDict, total=False):
    gcs: SoftwareRecipeArtifactGcs
    allowInsecure: bool
    id: str
    remote: SoftwareRecipeArtifactRemote

class ListPatchJobsResponse(typing_extensions.TypedDict, total=False):
    patchJobs: typing.List[PatchJob]
    nextPageToken: str

class SoftwareRecipeStepInstallMsi(typing_extensions.TypedDict, total=False):
    flags: typing.List[str]
    allowedExitCodes: typing.List[int]
    artifactId: str

class SoftwareRecipeStepInstallRpm(typing_extensions.TypedDict, total=False):
    artifactId: str

class ListPatchDeploymentsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    patchDeployments: typing.List[PatchDeployment]

class Empty(typing_extensions.TypedDict, total=False): ...

class OneTimeSchedule(typing_extensions.TypedDict, total=False):
    executeTime: str

class Package(typing_extensions.TypedDict, total=False):
    manager: typing_extensions.Literal[
        "MANAGER_UNSPECIFIED", "ANY", "APT", "YUM", "ZYPPER", "GOO"
    ]
    name: str
    desiredState: typing_extensions.Literal[
        "DESIRED_STATE_UNSPECIFIED", "INSTALLED", "UPDATED", "REMOVED"
    ]

class TimeZone(typing_extensions.TypedDict, total=False):
    id: str
    version: str

class TimeOfDay(typing_extensions.TypedDict, total=False):
    hours: int
    seconds: int
    minutes: int
    nanos: int

class PatchRollout(typing_extensions.TypedDict, total=False):
    disruptionBudget: FixedOrPercent
    mode: typing_extensions.Literal[
        "MODE_UNSPECIFIED", "ZONE_BY_ZONE", "CONCURRENT_ZONES"
    ]

class ZypperRepository(typing_extensions.TypedDict, total=False):
    id: str
    displayName: str
    gpgKeys: typing.List[str]
    baseUrl: str

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

class ExecStepConfig(typing_extensions.TypedDict, total=False):
    gcsObject: GcsObject
    localPath: str
    interpreter: typing_extensions.Literal[
        "INTERPRETER_UNSPECIFIED", "SHELL", "POWERSHELL"
    ]
    allowedSuccessCodes: typing.List[int]

class PatchInstanceFilterGroupLabel(typing_extensions.TypedDict, total=False):
    labels: typing.Dict[str, typing.Any]

class PackageRepository(typing_extensions.TypedDict, total=False):
    zypper: ZypperRepository
    yum: YumRepository
    apt: AptRepository
    goo: GooRepository

class PatchJobInstanceDetails(typing_extensions.TypedDict, total=False):
    attemptCount: str
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
    name: str
    failureReason: str
    instanceSystemId: str

class SoftwareRecipeStepExecFile(typing_extensions.TypedDict, total=False):
    artifactId: str
    allowedExitCodes: typing.List[int]
    localPath: str
    args: typing.List[str]
