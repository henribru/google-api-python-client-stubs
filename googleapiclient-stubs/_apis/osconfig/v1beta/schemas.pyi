import typing

_list = list

@typing.type_check_only
class AptRepository(typing.TypedDict, total=False):
    archiveType: typing.Literal["ARCHIVE_TYPE_UNSPECIFIED", "DEB", "DEB_SRC"]
    components: _list[str]
    distribution: str
    gpgKey: str
    uri: str

@typing.type_check_only
class AptSettings(typing.TypedDict, total=False):
    excludes: _list[str]
    exclusivePackages: _list[str]
    type: typing.Literal["TYPE_UNSPECIFIED", "DIST", "UPGRADE"]

@typing.type_check_only
class Assignment(typing.TypedDict, total=False):
    groupLabels: _list[AssignmentGroupLabel]
    instanceNamePrefixes: _list[str]
    instances: _list[str]
    osTypes: _list[AssignmentOsType]
    zones: _list[str]

@typing.type_check_only
class AssignmentGroupLabel(typing.TypedDict, total=False):
    labels: dict[str, typing.Any]

@typing.type_check_only
class AssignmentOsType(typing.TypedDict, total=False):
    osArchitecture: str
    osShortName: str
    osVersion: str

@typing.type_check_only
class CancelPatchJobRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class EffectiveGuestPolicy(typing.TypedDict, total=False):
    packageRepositories: _list[EffectiveGuestPolicySourcedPackageRepository]
    packages: _list[EffectiveGuestPolicySourcedPackage]
    softwareRecipes: _list[EffectiveGuestPolicySourcedSoftwareRecipe]

@typing.type_check_only
class EffectiveGuestPolicySourcedPackage(typing.TypedDict, total=False):
    package: Package
    source: str

@typing.type_check_only
class EffectiveGuestPolicySourcedPackageRepository(typing.TypedDict, total=False):
    packageRepository: PackageRepository
    source: str

@typing.type_check_only
class EffectiveGuestPolicySourcedSoftwareRecipe(typing.TypedDict, total=False):
    softwareRecipe: SoftwareRecipe
    source: str

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
class GooRepository(typing.TypedDict, total=False):
    name: str
    url: str

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
class GuestPolicy(typing.TypedDict, total=False):
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
class ListGuestPoliciesResponse(typing.TypedDict, total=False):
    guestPolicies: _list[GuestPolicy]
    nextPageToken: str

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
class LookupEffectiveGuestPolicyRequest(typing.TypedDict, total=False):
    osArchitecture: str
    osShortName: str
    osVersion: str

@typing.type_check_only
class MessageSet(typing.TypedDict, total=False): ...

@typing.type_check_only
class MonthlySchedule(typing.TypedDict, total=False):
    monthDay: int
    weekDayOfMonth: WeekDayOfMonth

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
class OneTimeSchedule(typing.TypedDict, total=False):
    executeTime: str

@typing.type_check_only
class Package(typing.TypedDict, total=False):
    desiredState: typing.Literal[
        "DESIRED_STATE_UNSPECIFIED", "INSTALLED", "UPDATED", "REMOVED"
    ]
    manager: typing.Literal["MANAGER_UNSPECIFIED", "ANY", "APT", "YUM", "ZYPPER", "GOO"]
    name: str

@typing.type_check_only
class PackageRepository(typing.TypedDict, total=False):
    apt: AptRepository
    goo: GooRepository
    yum: YumRepository
    zypper: ZypperRepository

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
class SoftwareRecipe(typing.TypedDict, total=False):
    artifacts: _list[SoftwareRecipeArtifact]
    desiredState: typing.Literal[
        "DESIRED_STATE_UNSPECIFIED", "INSTALLED", "UPDATED", "REMOVED"
    ]
    installSteps: _list[SoftwareRecipeStep]
    name: str
    updateSteps: _list[SoftwareRecipeStep]
    version: str

@typing.type_check_only
class SoftwareRecipeArtifact(typing.TypedDict, total=False):
    allowInsecure: bool
    gcs: SoftwareRecipeArtifactGcs
    id: str
    remote: SoftwareRecipeArtifactRemote

@typing.type_check_only
class SoftwareRecipeArtifactGcs(typing.TypedDict, total=False):
    bucket: str
    generation: str
    object: str

@typing.type_check_only
class SoftwareRecipeArtifactRemote(typing.TypedDict, total=False):
    checksum: str
    uri: str

@typing.type_check_only
class SoftwareRecipeStep(typing.TypedDict, total=False):
    archiveExtraction: SoftwareRecipeStepExtractArchive
    dpkgInstallation: SoftwareRecipeStepInstallDpkg
    fileCopy: SoftwareRecipeStepCopyFile
    fileExec: SoftwareRecipeStepExecFile
    msiInstallation: SoftwareRecipeStepInstallMsi
    rpmInstallation: SoftwareRecipeStepInstallRpm
    scriptRun: SoftwareRecipeStepRunScript

@typing.type_check_only
class SoftwareRecipeStepCopyFile(typing.TypedDict, total=False):
    artifactId: str
    destination: str
    overwrite: bool
    permissions: str

@typing.type_check_only
class SoftwareRecipeStepExecFile(typing.TypedDict, total=False):
    allowedExitCodes: _list[int]
    args: _list[str]
    artifactId: str
    localPath: str

@typing.type_check_only
class SoftwareRecipeStepExtractArchive(typing.TypedDict, total=False):
    artifactId: str
    destination: str
    type: typing.Literal[
        "ARCHIVE_TYPE_UNSPECIFIED",
        "TAR",
        "TAR_GZIP",
        "TAR_BZIP",
        "TAR_LZMA",
        "TAR_XZ",
        "ZIP",
    ]

@typing.type_check_only
class SoftwareRecipeStepInstallDpkg(typing.TypedDict, total=False):
    artifactId: str

@typing.type_check_only
class SoftwareRecipeStepInstallMsi(typing.TypedDict, total=False):
    allowedExitCodes: _list[int]
    artifactId: str
    flags: _list[str]

@typing.type_check_only
class SoftwareRecipeStepInstallRpm(typing.TypedDict, total=False):
    artifactId: str

@typing.type_check_only
class SoftwareRecipeStepRunScript(typing.TypedDict, total=False):
    allowedExitCodes: _list[int]
    interpreter: typing.Literal["INTERPRETER_UNSPECIFIED", "SHELL", "POWERSHELL"]
    script: str

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
class YumRepository(typing.TypedDict, total=False):
    baseUrl: str
    displayName: str
    gpgKeys: _list[str]
    id: str

@typing.type_check_only
class YumSettings(typing.TypedDict, total=False):
    excludes: _list[str]
    exclusivePackages: _list[str]
    minimal: bool
    security: bool

@typing.type_check_only
class ZypperRepository(typing.TypedDict, total=False):
    baseUrl: str
    displayName: str
    gpgKeys: _list[str]
    id: str

@typing.type_check_only
class ZypperSettings(typing.TypedDict, total=False):
    categories: _list[str]
    excludes: _list[str]
    exclusivePatches: _list[str]
    severities: _list[str]
    withOptional: bool
    withUpdate: bool
