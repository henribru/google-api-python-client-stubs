import typing

_list = list

@typing.type_check_only
class CancelOperationRequest(typing.TypedDict, total=False): ...

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
class GoogleCloudOsconfigV2beta_OrchestrationScope_LocationSelector(
    typing.TypedDict, total=False
):
    includedLocations: _list[str]

@typing.type_check_only
class GoogleCloudOsconfigV2beta_OrchestrationScope_ResourceHierarchySelector(
    typing.TypedDict, total=False
):
    includedFolders: _list[str]
    includedProjects: _list[str]

@typing.type_check_only
class GoogleCloudOsconfigV2beta_OrchestrationScope_Selector(
    typing.TypedDict, total=False
):
    locationSelector: GoogleCloudOsconfigV2beta_OrchestrationScope_LocationSelector
    resourceHierarchySelector: (
        GoogleCloudOsconfigV2beta_OrchestrationScope_ResourceHierarchySelector
    )

@typing.type_check_only
class GoogleCloudOsconfigV2beta_PolicyOrchestrator_IterationState(
    typing.TypedDict, total=False
):
    error: Status
    failedActions: str
    finishTime: str
    iterationId: str
    performedActions: str
    progress: float
    startTime: str
    state: typing.Literal[
        "STATE_UNSPECIFIED", "PROCESSING", "COMPLETED", "FAILED", "CANCELLED", "UNKNOWN"
    ]

@typing.type_check_only
class GoogleCloudOsconfigV2beta_PolicyOrchestrator_OrchestrationState(
    typing.TypedDict, total=False
):
    currentIterationState: GoogleCloudOsconfigV2beta_PolicyOrchestrator_IterationState
    previousIterationState: GoogleCloudOsconfigV2beta_PolicyOrchestrator_IterationState

@typing.type_check_only
class GoogleCloudOsconfigV2beta__ListPolicyOrchestratorsResponse(
    typing.TypedDict, total=False
):
    nextPageToken: str
    policyOrchestrators: _list[GoogleCloudOsconfigV2beta__PolicyOrchestrator]
    unreachable: _list[str]

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
class GoogleCloudOsconfigV2beta__OrchestratedResource(typing.TypedDict, total=False):
    id: str
    osPolicyAssignmentV1Payload: OSPolicyAssignment

@typing.type_check_only
class GoogleCloudOsconfigV2beta__OrchestrationScope(typing.TypedDict, total=False):
    selectors: _list[GoogleCloudOsconfigV2beta_OrchestrationScope_Selector]

@typing.type_check_only
class GoogleCloudOsconfigV2beta__PolicyOrchestrator(typing.TypedDict, total=False):
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
class ListOperationsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    operations: _list[Operation]
    unreachable: _list[str]

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
