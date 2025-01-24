import typing

import typing_extensions

_list = list

@typing.type_check_only
class CancelOperationRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class FixedOrPercent(typing_extensions.TypedDict, total=False):
    fixed: int
    percent: int

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
class GoogleCloudOsconfigV2beta_OrchestrationScope_LocationSelector(
    typing_extensions.TypedDict, total=False
):
    includedLocations: _list[str]

@typing.type_check_only
class GoogleCloudOsconfigV2beta_OrchestrationScope_ResourceHierarchySelector(
    typing_extensions.TypedDict, total=False
):
    includedFolders: _list[str]
    includedProjects: _list[str]

@typing.type_check_only
class GoogleCloudOsconfigV2beta_OrchestrationScope_Selector(
    typing_extensions.TypedDict, total=False
):
    locationSelector: GoogleCloudOsconfigV2beta_OrchestrationScope_LocationSelector
    resourceHierarchySelector: (
        GoogleCloudOsconfigV2beta_OrchestrationScope_ResourceHierarchySelector
    )

@typing.type_check_only
class GoogleCloudOsconfigV2beta_PolicyOrchestrator_IterationState(
    typing_extensions.TypedDict, total=False
):
    error: Status
    failedActions: str
    finishTime: str
    performedActions: str
    progress: float
    rolloutResource: str
    startTime: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "PROCESSING", "COMPLETED", "FAILED", "CANCELLED", "UNKNOWN"
    ]

@typing.type_check_only
class GoogleCloudOsconfigV2beta_PolicyOrchestrator_OrchestrationState(
    typing_extensions.TypedDict, total=False
):
    currentIterationState: GoogleCloudOsconfigV2beta_PolicyOrchestrator_IterationState
    previousIterationState: GoogleCloudOsconfigV2beta_PolicyOrchestrator_IterationState

@typing.type_check_only
class GoogleCloudOsconfigV2beta__ListPolicyOrchestratorsResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    policyOrchestrators: _list[GoogleCloudOsconfigV2beta__PolicyOrchestrator]
    unreachable: _list[str]

@typing.type_check_only
class GoogleCloudOsconfigV2beta__OperationMetadata(
    typing_extensions.TypedDict, total=False
):
    apiVersion: str
    createTime: str
    endTime: str
    requestedCancellation: bool
    statusMessage: str
    target: str
    verb: str

@typing.type_check_only
class GoogleCloudOsconfigV2beta__OrchestratedResource(
    typing_extensions.TypedDict, total=False
):
    id: str
    osPolicyAssignmentV1Payload: OSPolicyAssignment

@typing.type_check_only
class GoogleCloudOsconfigV2beta__OrchestrationScope(
    typing_extensions.TypedDict, total=False
):
    selectors: _list[GoogleCloudOsconfigV2beta_OrchestrationScope_Selector]

@typing.type_check_only
class GoogleCloudOsconfigV2beta__PolicyOrchestrator(
    typing_extensions.TypedDict, total=False
):
    action: str
    createTime: str
    description: str
    etag: str
    labels: dict[str, typing.Any]
    name: str
    orchestratedResource: GoogleCloudOsconfigV2beta__OrchestratedResource
    orchestrationScope: GoogleCloudOsconfigV2beta__OrchestrationScope
    orchestrationState: GoogleCloudOsconfigV2beta_PolicyOrchestrator_OrchestrationState
    reconciling: bool
    state: str
    updateTime: str

@typing.type_check_only
class ListOperationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    operations: _list[Operation]

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
class Operation(typing_extensions.TypedDict, total=False):
    done: bool
    error: Status
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str
