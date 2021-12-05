import typing

import typing_extensions

_list = list

@typing.type_check_only
class ApproveRolloutRequest(typing_extensions.TypedDict, total=False):
    approved: bool

@typing.type_check_only
class ApproveRolloutResponse(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class AuditConfig(typing_extensions.TypedDict, total=False):
    auditLogConfigs: _list[AuditLogConfig]
    service: str

@typing.type_check_only
class AuditLogConfig(typing_extensions.TypedDict, total=False):
    exemptedMembers: _list[str]
    logType: typing_extensions.Literal[
        "LOG_TYPE_UNSPECIFIED", "ADMIN_READ", "DATA_WRITE", "DATA_READ"
    ]

@typing.type_check_only
class Binding(typing_extensions.TypedDict, total=False):
    condition: Expr
    members: _list[str]
    role: str

@typing.type_check_only
class BuildArtifact(typing_extensions.TypedDict, total=False):
    image: str
    tag: str

@typing.type_check_only
class CancelOperationRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Config(typing_extensions.TypedDict, total=False):
    defaultSkaffoldVersion: str
    name: str
    supportedVersions: _list[SkaffoldVersion]

@typing.type_check_only
class Date(typing_extensions.TypedDict, total=False):
    day: int
    month: int
    year: int

@typing.type_check_only
class DefaultPool(typing_extensions.TypedDict, total=False):
    artifactStorage: str
    serviceAccount: str

@typing.type_check_only
class DeliveryPipeline(typing_extensions.TypedDict, total=False):
    annotations: dict[str, typing.Any]
    condition: PipelineCondition
    createTime: str
    description: str
    etag: str
    labels: dict[str, typing.Any]
    name: str
    serialPipeline: SerialPipeline
    uid: str
    updateTime: str

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class ExecutionConfig(typing_extensions.TypedDict, total=False):
    defaultPool: DefaultPool
    privatePool: PrivatePool
    usages: _list[str]

@typing.type_check_only
class Expr(typing_extensions.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str

@typing.type_check_only
class GkeCluster(typing_extensions.TypedDict, total=False):
    cluster: str

@typing.type_check_only
class ListDeliveryPipelinesResponse(typing_extensions.TypedDict, total=False):
    deliveryPipelines: _list[DeliveryPipeline]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListLocationsResponse(typing_extensions.TypedDict, total=False):
    locations: _list[Location]
    nextPageToken: str

@typing.type_check_only
class ListOperationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    operations: _list[Operation]

@typing.type_check_only
class ListReleasesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    releases: _list[Release]
    unreachable: _list[str]

@typing.type_check_only
class ListRolloutsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    rollouts: _list[Rollout]
    unreachable: _list[str]

@typing.type_check_only
class ListTargetsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    targets: _list[Target]
    unreachable: _list[str]

@typing.type_check_only
class Location(typing_extensions.TypedDict, total=False):
    displayName: str
    labels: dict[str, typing.Any]
    locationId: str
    metadata: dict[str, typing.Any]
    name: str

@typing.type_check_only
class Operation(typing_extensions.TypedDict, total=False):
    done: bool
    error: Status
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class OperationMetadata(typing_extensions.TypedDict, total=False):
    apiVersion: str
    createTime: str
    endTime: str
    requestedCancellation: bool
    statusMessage: str
    target: str
    verb: str

@typing.type_check_only
class PipelineCondition(typing_extensions.TypedDict, total=False):
    pipelineReadyCondition: PipelineReadyCondition
    targetsPresentCondition: TargetsPresentCondition

@typing.type_check_only
class PipelineReadyCondition(typing_extensions.TypedDict, total=False):
    status: bool
    updateTime: str

@typing.type_check_only
class Policy(typing_extensions.TypedDict, total=False):
    auditConfigs: _list[AuditConfig]
    bindings: _list[Binding]
    etag: str
    version: int

@typing.type_check_only
class PrivatePool(typing_extensions.TypedDict, total=False):
    artifactStorage: str
    serviceAccount: str
    workerPool: str

@typing.type_check_only
class Release(typing_extensions.TypedDict, total=False):
    annotations: dict[str, typing.Any]
    buildArtifacts: _list[BuildArtifact]
    createTime: str
    deliveryPipelineSnapshot: DeliveryPipeline
    description: str
    etag: str
    labels: dict[str, typing.Any]
    name: str
    renderEndTime: str
    renderStartTime: str
    renderState: typing_extensions.Literal[
        "RENDER_STATE_UNSPECIFIED", "SUCCEEDED", "FAILED", "IN_PROGRESS"
    ]
    skaffoldConfigPath: str
    skaffoldConfigUri: str
    skaffoldVersion: str
    targetArtifacts: dict[str, typing.Any]
    targetRenders: dict[str, typing.Any]
    targetSnapshots: _list[Target]
    uid: str

@typing.type_check_only
class Rollout(typing_extensions.TypedDict, total=False):
    annotations: dict[str, typing.Any]
    approvalState: typing_extensions.Literal[
        "APPROVAL_STATE_UNSPECIFIED",
        "NEEDS_APPROVAL",
        "DOES_NOT_NEED_APPROVAL",
        "APPROVED",
        "REJECTED",
    ]
    approveTime: str
    createTime: str
    deployEndTime: str
    deployStartTime: str
    deployingBuild: str
    description: str
    enqueueTime: str
    etag: str
    failureReason: str
    labels: dict[str, typing.Any]
    name: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "SUCCEEDED",
        "FAILED",
        "IN_PROGRESS",
        "PENDING_APPROVAL",
        "APPROVAL_REJECTED",
        "PENDING",
        "PENDING_RELEASE",
    ]
    targetId: str
    uid: str

@typing.type_check_only
class SerialPipeline(typing_extensions.TypedDict, total=False):
    stages: _list[Stage]

@typing.type_check_only
class SetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    policy: Policy
    updateMask: str

@typing.type_check_only
class SkaffoldVersion(typing_extensions.TypedDict, total=False):
    supportEndDate: Date
    version: str

@typing.type_check_only
class Stage(typing_extensions.TypedDict, total=False):
    profiles: _list[str]
    targetId: str

@typing.type_check_only
class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class Target(typing_extensions.TypedDict, total=False):
    annotations: dict[str, typing.Any]
    createTime: str
    description: str
    etag: str
    executionConfigs: _list[ExecutionConfig]
    gke: GkeCluster
    labels: dict[str, typing.Any]
    name: str
    requireApproval: bool
    targetId: str
    uid: str
    updateTime: str

@typing.type_check_only
class TargetArtifact(typing_extensions.TypedDict, total=False):
    artifactUri: str
    manifestPath: str
    skaffoldConfigPath: str

@typing.type_check_only
class TargetRender(typing_extensions.TypedDict, total=False):
    renderingBuild: str
    renderingState: typing_extensions.Literal[
        "TARGET_RENDER_STATE_UNSPECIFIED", "SUCCEEDED", "FAILED", "IN_PROGRESS"
    ]

@typing.type_check_only
class TargetsPresentCondition(typing_extensions.TypedDict, total=False):
    missingTargets: _list[str]
    status: bool
    updateTime: str

@typing.type_check_only
class TestIamPermissionsRequest(typing_extensions.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class TestIamPermissionsResponse(typing_extensions.TypedDict, total=False):
    permissions: _list[str]
