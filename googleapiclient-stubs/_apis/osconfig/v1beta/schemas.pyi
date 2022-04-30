import typing

import typing_extensions

_list = list

@typing.type_check_only
class AptRepository(typing_extensions.TypedDict, total=False):
    archiveType: typing_extensions.Literal["ARCHIVE_TYPE_UNSPECIFIED", "DEB", "DEB_SRC"]
    components: _list[str]
    distribution: str
    gpgKey: str
    uri: str

@typing.type_check_only
class AptSettings(typing_extensions.TypedDict, total=False):
    excludes: _list[str]
    exclusivePackages: _list[str]
    type: typing_extensions.Literal["TYPE_UNSPECIFIED", "DIST", "UPGRADE"]

@typing.type_check_only
class Assignment(typing_extensions.TypedDict, total=False):
    groupLabels: _list[AssignmentGroupLabel]
    instanceNamePrefixes: _list[str]
    instances: _list[str]
    osTypes: _list[AssignmentOsType]
    zones: _list[str]

@typing.type_check_only
class AssignmentGroupLabel(typing_extensions.TypedDict, total=False):
    labels: dict[str, typing.Any]

@typing.type_check_only
class AssignmentOsType(typing_extensions.TypedDict, total=False):
    osArchitecture: str
    osShortName: str
    osVersion: str

@typing.type_check_only
class CancelPatchJobRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class EffectiveGuestPolicy(typing_extensions.TypedDict, total=False):
    packageRepositories: _list[EffectiveGuestPolicySourcedPackageRepository]
    packages: _list[EffectiveGuestPolicySourcedPackage]
    softwareRecipes: _list[EffectiveGuestPolicySourcedSoftwareRecipe]

@typing.type_check_only
class EffectiveGuestPolicySourcedPackage(typing_extensions.TypedDict, total=False):
    package: Package
    source: str

@typing.type_check_only
class EffectiveGuestPolicySourcedPackageRepository(
    typing_extensions.TypedDict, total=False
):
    packageRepository: PackageRepository
    source: str

@typing.type_check_only
class EffectiveGuestPolicySourcedSoftwareRecipe(
    typing_extensions.TypedDict, total=False
):
    softwareRecipe: SoftwareRecipe
    source: str

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
class GooRepository(typing_extensions.TypedDict, total=False):
    name: str
    url: str

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
class GuestPolicy(typing_extensions.TypedDict, total=False):
    assignment: Assignment
    createTime: str
    description: str
    etag: str
    name: str
    packageRepositories: _list[PackageRepository]
    packages: _list[Package]
    recipes: _list[SoftwareRecipe]
    updateTime: str

@typing.type_check_only
class ListGuestPoliciesResponse(typing_extensions.TypedDict, total=False):
    guestPolicies: _list[GuestPolicy]
    nextPageToken: str

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
class LookupEffectiveGuestPolicyRequest(typing_extensions.TypedDict, total=False):
    osArchitecture: str
    osShortName: str
    osVersion: str

@typing.type_check_only
class MonthlySchedule(typing_extensions.TypedDict, total=False):
    monthDay: int
    weekDayOfMonth: WeekDayOfMonth

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
class OneTimeSchedule(typing_extensions.TypedDict, total=False):
    executeTime: str

@typing.type_check_only
class Package(typing_extensions.TypedDict, total=False):
    desiredState: typing_extensions.Literal[
        "DESIRED_STATE_UNSPECIFIED", "INSTALLED", "UPDATED", "REMOVED"
    ]
    manager: typing_extensions.Literal[
        "MANAGER_UNSPECIFIED", "ANY", "APT", "YUM", "ZYPPER", "GOO"
    ]
    name: str

@typing.type_check_only
class PackageRepository(typing_extensions.TypedDict, total=False):
    apt: AptRepository
    goo: GooRepository
    yum: YumRepository
    zypper: ZypperRepository

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
class SoftwareRecipe(typing_extensions.TypedDict, total=False):
    artifacts: _list[SoftwareRecipeArtifact]
    desiredState: typing_extensions.Literal[
        "DESIRED_STATE_UNSPECIFIED", "INSTALLED", "UPDATED", "REMOVED"
    ]
    installSteps: _list[SoftwareRecipeStep]
    name: str
    updateSteps: _list[SoftwareRecipeStep]
    version: str

@typing.type_check_only
class SoftwareRecipeArtifact(typing_extensions.TypedDict, total=False):
    allowInsecure: bool
    gcs: SoftwareRecipeArtifactGcs
    id: str
    remote: SoftwareRecipeArtifactRemote

@typing.type_check_only
class SoftwareRecipeArtifactGcs(typing_extensions.TypedDict, total=False):
    bucket: str
    generation: str
    object: str

@typing.type_check_only
class SoftwareRecipeArtifactRemote(typing_extensions.TypedDict, total=False):
    checksum: str
    uri: str

@typing.type_check_only
class SoftwareRecipeStep(typing_extensions.TypedDict, total=False):
    archiveExtraction: SoftwareRecipeStepExtractArchive
    dpkgInstallation: SoftwareRecipeStepInstallDpkg
    fileCopy: SoftwareRecipeStepCopyFile
    fileExec: SoftwareRecipeStepExecFile
    msiInstallation: SoftwareRecipeStepInstallMsi
    rpmInstallation: SoftwareRecipeStepInstallRpm
    scriptRun: SoftwareRecipeStepRunScript

@typing.type_check_only
class SoftwareRecipeStepCopyFile(typing_extensions.TypedDict, total=False):
    artifactId: str
    destination: str
    overwrite: bool
    permissions: str

@typing.type_check_only
class SoftwareRecipeStepExecFile(typing_extensions.TypedDict, total=False):
    allowedExitCodes: _list[int]
    args: _list[str]
    artifactId: str
    localPath: str

@typing.type_check_only
class SoftwareRecipeStepExtractArchive(typing_extensions.TypedDict, total=False):
    artifactId: str
    destination: str
    type: typing_extensions.Literal[
        "ARCHIVE_TYPE_UNSPECIFIED",
        "TAR",
        "TAR_GZIP",
        "TAR_BZIP",
        "TAR_LZMA",
        "TAR_XZ",
        "ZIP",
    ]

@typing.type_check_only
class SoftwareRecipeStepInstallDpkg(typing_extensions.TypedDict, total=False):
    artifactId: str

@typing.type_check_only
class SoftwareRecipeStepInstallMsi(typing_extensions.TypedDict, total=False):
    allowedExitCodes: _list[int]
    artifactId: str
    flags: _list[str]

@typing.type_check_only
class SoftwareRecipeStepInstallRpm(typing_extensions.TypedDict, total=False):
    artifactId: str

@typing.type_check_only
class SoftwareRecipeStepRunScript(typing_extensions.TypedDict, total=False):
    allowedExitCodes: _list[int]
    interpreter: typing_extensions.Literal[
        "INTERPRETER_UNSPECIFIED", "SHELL", "POWERSHELL"
    ]
    script: str

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
class YumRepository(typing_extensions.TypedDict, total=False):
    baseUrl: str
    displayName: str
    gpgKeys: _list[str]
    id: str

@typing.type_check_only
class YumSettings(typing_extensions.TypedDict, total=False):
    excludes: _list[str]
    exclusivePackages: _list[str]
    minimal: bool
    security: bool

@typing.type_check_only
class ZypperRepository(typing_extensions.TypedDict, total=False):
    baseUrl: str
    displayName: str
    gpgKeys: _list[str]
    id: str

@typing.type_check_only
class ZypperSettings(typing_extensions.TypedDict, total=False):
    categories: _list[str]
    excludes: _list[str]
    exclusivePatches: _list[str]
    severities: _list[str]
    withOptional: bool
    withUpdate: bool
