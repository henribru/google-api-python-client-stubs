import typing

import typing_extensions

_list = list

@typing.type_check_only
class AbandonReleaseRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class AbandonReleaseResponse(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class AdvanceChildRolloutJob(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class AdvanceChildRolloutJobRun(typing_extensions.TypedDict, total=False):
    rollout: str
    rolloutPhaseId: str

@typing.type_check_only
class AdvanceRolloutOperation(typing_extensions.TypedDict, total=False):
    destinationPhase: str
    rollout: str
    sourcePhase: str
    wait: str

@typing.type_check_only
class AdvanceRolloutRequest(typing_extensions.TypedDict, total=False):
    overrideDeployPolicy: _list[str]
    phaseId: str

@typing.type_check_only
class AdvanceRolloutResponse(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class AdvanceRolloutRule(typing_extensions.TypedDict, total=False):
    condition: AutomationRuleCondition
    id: str
    sourcePhases: _list[str]
    wait: str

@typing.type_check_only
class AnthosCluster(typing_extensions.TypedDict, total=False):
    membership: str

@typing.type_check_only
class ApproveRolloutRequest(typing_extensions.TypedDict, total=False):
    approved: bool
    overrideDeployPolicy: _list[str]

@typing.type_check_only
class ApproveRolloutResponse(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class AssociatedEntities(typing_extensions.TypedDict, total=False):
    anthosClusters: _list[AnthosCluster]
    gkeClusters: _list[GkeCluster]

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
class Automation(typing_extensions.TypedDict, total=False):
    annotations: dict[str, typing.Any]
    createTime: str
    description: str
    etag: str
    labels: dict[str, typing.Any]
    name: str
    rules: _list[AutomationRule]
    selector: AutomationResourceSelector
    serviceAccount: str
    suspended: bool
    uid: str
    updateTime: str

@typing.type_check_only
class AutomationEvent(typing_extensions.TypedDict, total=False):
    automation: str
    message: str
    pipelineUid: str
    type: typing_extensions.Literal[
        "TYPE_UNSPECIFIED",
        "TYPE_PUBSUB_NOTIFICATION_FAILURE",
        "TYPE_RESOURCE_STATE_CHANGE",
        "TYPE_PROCESS_ABORTED",
        "TYPE_RESTRICTION_VIOLATED",
        "TYPE_RESOURCE_DELETED",
        "TYPE_ROLLOUT_UPDATE",
        "TYPE_DEPLOY_POLICY_EVALUATION",
        "TYPE_RENDER_STATUES_CHANGE",
    ]

@typing.type_check_only
class AutomationResourceSelector(typing_extensions.TypedDict, total=False):
    targets: _list[TargetAttribute]

@typing.type_check_only
class AutomationRolloutMetadata(typing_extensions.TypedDict, total=False):
    advanceAutomationRuns: _list[str]
    promoteAutomationRun: str
    repairAutomationRuns: _list[str]

@typing.type_check_only
class AutomationRule(typing_extensions.TypedDict, total=False):
    advanceRolloutRule: AdvanceRolloutRule
    promoteReleaseRule: PromoteReleaseRule
    repairRolloutRule: RepairRolloutRule
    timedPromoteReleaseRule: TimedPromoteReleaseRule

@typing.type_check_only
class AutomationRuleCondition(typing_extensions.TypedDict, total=False):
    targetsPresentCondition: TargetsPresentCondition
    timedPromoteReleaseCondition: TimedPromoteReleaseCondition

@typing.type_check_only
class AutomationRun(typing_extensions.TypedDict, total=False):
    advanceRolloutOperation: AdvanceRolloutOperation
    automationId: str
    automationSnapshot: Automation
    createTime: str
    etag: str
    expireTime: str
    name: str
    policyViolation: PolicyViolation
    promoteReleaseOperation: PromoteReleaseOperation
    repairRolloutOperation: RepairRolloutOperation
    ruleId: str
    serviceAccount: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "SUCCEEDED",
        "CANCELLED",
        "FAILED",
        "IN_PROGRESS",
        "PENDING",
        "ABORTED",
    ]
    stateDescription: str
    targetId: str
    timedPromoteReleaseOperation: TimedPromoteReleaseOperation
    updateTime: str
    waitUntilTime: str

@typing.type_check_only
class AutomationRunEvent(typing_extensions.TypedDict, total=False):
    automationId: str
    automationRun: str
    destinationTargetId: str
    message: str
    pipelineUid: str
    ruleId: str
    type: typing_extensions.Literal[
        "TYPE_UNSPECIFIED",
        "TYPE_PUBSUB_NOTIFICATION_FAILURE",
        "TYPE_RESOURCE_STATE_CHANGE",
        "TYPE_PROCESS_ABORTED",
        "TYPE_RESTRICTION_VIOLATED",
        "TYPE_RESOURCE_DELETED",
        "TYPE_ROLLOUT_UPDATE",
        "TYPE_DEPLOY_POLICY_EVALUATION",
        "TYPE_RENDER_STATUES_CHANGE",
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
class Canary(typing_extensions.TypedDict, total=False):
    canaryDeployment: CanaryDeployment
    customCanaryDeployment: CustomCanaryDeployment
    runtimeConfig: RuntimeConfig

@typing.type_check_only
class CanaryDeployment(typing_extensions.TypedDict, total=False):
    percentages: _list[int]
    postdeploy: Postdeploy
    predeploy: Predeploy
    verify: bool

@typing.type_check_only
class CancelAutomationRunRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class CancelAutomationRunResponse(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class CancelOperationRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class CancelRolloutRequest(typing_extensions.TypedDict, total=False):
    overrideDeployPolicy: _list[str]

@typing.type_check_only
class CancelRolloutResponse(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class ChildRolloutJobs(typing_extensions.TypedDict, total=False):
    advanceRolloutJobs: _list[Job]
    createRolloutJobs: _list[Job]

@typing.type_check_only
class CloudRunConfig(typing_extensions.TypedDict, total=False):
    automaticTrafficControl: bool
    canaryRevisionTags: _list[str]
    priorRevisionTags: _list[str]
    stableRevisionTags: _list[str]

@typing.type_check_only
class CloudRunLocation(typing_extensions.TypedDict, total=False):
    location: str

@typing.type_check_only
class CloudRunMetadata(typing_extensions.TypedDict, total=False):
    job: str
    revision: str
    service: str
    serviceUrls: _list[str]

@typing.type_check_only
class CloudRunRenderMetadata(typing_extensions.TypedDict, total=False):
    service: str

@typing.type_check_only
class Config(typing_extensions.TypedDict, total=False):
    defaultSkaffoldVersion: str
    name: str
    supportedVersions: _list[SkaffoldVersion]

@typing.type_check_only
class CreateChildRolloutJob(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class CreateChildRolloutJobRun(typing_extensions.TypedDict, total=False):
    rollout: str
    rolloutPhaseId: str

@typing.type_check_only
class CustomCanaryDeployment(typing_extensions.TypedDict, total=False):
    phaseConfigs: _list[PhaseConfig]

@typing.type_check_only
class CustomMetadata(typing_extensions.TypedDict, total=False):
    values: dict[str, typing.Any]

@typing.type_check_only
class CustomTarget(typing_extensions.TypedDict, total=False):
    customTargetType: str

@typing.type_check_only
class CustomTargetDeployMetadata(typing_extensions.TypedDict, total=False):
    skipMessage: str

@typing.type_check_only
class CustomTargetSkaffoldActions(typing_extensions.TypedDict, total=False):
    deployAction: str
    includeSkaffoldModules: _list[SkaffoldModules]
    renderAction: str

@typing.type_check_only
class CustomTargetType(typing_extensions.TypedDict, total=False):
    annotations: dict[str, typing.Any]
    createTime: str
    customActions: CustomTargetSkaffoldActions
    customTargetTypeId: str
    description: str
    etag: str
    labels: dict[str, typing.Any]
    name: str
    uid: str
    updateTime: str

@typing.type_check_only
class CustomTargetTypeNotificationEvent(typing_extensions.TypedDict, total=False):
    customTargetType: str
    customTargetTypeUid: str
    message: str
    type: typing_extensions.Literal[
        "TYPE_UNSPECIFIED",
        "TYPE_PUBSUB_NOTIFICATION_FAILURE",
        "TYPE_RESOURCE_STATE_CHANGE",
        "TYPE_PROCESS_ABORTED",
        "TYPE_RESTRICTION_VIOLATED",
        "TYPE_RESOURCE_DELETED",
        "TYPE_ROLLOUT_UPDATE",
        "TYPE_DEPLOY_POLICY_EVALUATION",
        "TYPE_RENDER_STATUES_CHANGE",
    ]

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
    suspended: bool
    uid: str
    updateTime: str

@typing.type_check_only
class DeliveryPipelineAttribute(typing_extensions.TypedDict, total=False):
    id: str
    labels: dict[str, typing.Any]

@typing.type_check_only
class DeliveryPipelineNotificationEvent(typing_extensions.TypedDict, total=False):
    deliveryPipeline: str
    message: str
    pipelineUid: str
    type: typing_extensions.Literal[
        "TYPE_UNSPECIFIED",
        "TYPE_PUBSUB_NOTIFICATION_FAILURE",
        "TYPE_RESOURCE_STATE_CHANGE",
        "TYPE_PROCESS_ABORTED",
        "TYPE_RESTRICTION_VIOLATED",
        "TYPE_RESOURCE_DELETED",
        "TYPE_ROLLOUT_UPDATE",
        "TYPE_DEPLOY_POLICY_EVALUATION",
        "TYPE_RENDER_STATUES_CHANGE",
    ]

@typing.type_check_only
class DeployArtifact(typing_extensions.TypedDict, total=False):
    artifactUri: str
    manifestPaths: _list[str]

@typing.type_check_only
class DeployJob(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class DeployJobRun(typing_extensions.TypedDict, total=False):
    artifact: DeployArtifact
    build: str
    failureCause: typing_extensions.Literal[
        "FAILURE_CAUSE_UNSPECIFIED",
        "CLOUD_BUILD_UNAVAILABLE",
        "EXECUTION_FAILED",
        "DEADLINE_EXCEEDED",
        "MISSING_RESOURCES_FOR_CANARY",
        "CLOUD_BUILD_REQUEST_FAILED",
        "DEPLOY_FEATURE_NOT_SUPPORTED",
    ]
    failureMessage: str
    metadata: DeployJobRunMetadata

@typing.type_check_only
class DeployJobRunMetadata(typing_extensions.TypedDict, total=False):
    cloudRun: CloudRunMetadata
    custom: CustomMetadata
    customTarget: CustomTargetDeployMetadata

@typing.type_check_only
class DeployParameters(typing_extensions.TypedDict, total=False):
    matchTargetLabels: dict[str, typing.Any]
    values: dict[str, typing.Any]

@typing.type_check_only
class DeployPolicy(typing_extensions.TypedDict, total=False):
    annotations: dict[str, typing.Any]
    createTime: str
    description: str
    etag: str
    labels: dict[str, typing.Any]
    name: str
    rules: _list[PolicyRule]
    selectors: _list[DeployPolicyResourceSelector]
    suspended: bool
    uid: str
    updateTime: str

@typing.type_check_only
class DeployPolicyEvaluationEvent(typing_extensions.TypedDict, total=False):
    allowed: bool
    deliveryPipeline: str
    deployPolicy: str
    deployPolicyUid: str
    invoker: typing_extensions.Literal[
        "INVOKER_UNSPECIFIED", "USER", "DEPLOY_AUTOMATION"
    ]
    message: str
    overrides: _list[
        typing_extensions.Literal[
            "POLICY_VERDICT_OVERRIDE_UNSPECIFIED",
            "POLICY_OVERRIDDEN",
            "POLICY_SUSPENDED",
        ]
    ]
    pipelineUid: str
    rule: str
    ruleType: str
    target: str
    targetUid: str
    verdict: typing_extensions.Literal[
        "POLICY_VERDICT_UNSPECIFIED", "ALLOWED_BY_POLICY", "DENIED_BY_POLICY"
    ]

@typing.type_check_only
class DeployPolicyNotificationEvent(typing_extensions.TypedDict, total=False):
    deployPolicy: str
    deployPolicyUid: str
    message: str
    type: typing_extensions.Literal[
        "TYPE_UNSPECIFIED",
        "TYPE_PUBSUB_NOTIFICATION_FAILURE",
        "TYPE_RESOURCE_STATE_CHANGE",
        "TYPE_PROCESS_ABORTED",
        "TYPE_RESTRICTION_VIOLATED",
        "TYPE_RESOURCE_DELETED",
        "TYPE_ROLLOUT_UPDATE",
        "TYPE_DEPLOY_POLICY_EVALUATION",
        "TYPE_RENDER_STATUES_CHANGE",
    ]

@typing.type_check_only
class DeployPolicyResourceSelector(typing_extensions.TypedDict, total=False):
    deliveryPipeline: DeliveryPipelineAttribute
    target: TargetAttribute

@typing.type_check_only
class DeploymentJobs(typing_extensions.TypedDict, total=False):
    deployJob: Job
    postdeployJob: Job
    predeployJob: Job
    verifyJob: Job

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class ExecutionConfig(typing_extensions.TypedDict, total=False):
    artifactStorage: str
    defaultPool: DefaultPool
    executionTimeout: str
    privatePool: PrivatePool
    serviceAccount: str
    usages: _list[
        typing_extensions.Literal[
            "EXECUTION_ENVIRONMENT_USAGE_UNSPECIFIED",
            "RENDER",
            "DEPLOY",
            "VERIFY",
            "PREDEPLOY",
            "POSTDEPLOY",
        ]
    ]
    verbose: bool
    workerPool: str

@typing.type_check_only
class Expr(typing_extensions.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str

@typing.type_check_only
class GatewayServiceMesh(typing_extensions.TypedDict, total=False):
    deployment: str
    httpRoute: str
    podSelectorLabel: str
    routeDestinations: RouteDestinations
    routeUpdateWaitTime: str
    service: str
    stableCutbackDuration: str

@typing.type_check_only
class GkeCluster(typing_extensions.TypedDict, total=False):
    cluster: str
    dnsEndpoint: bool
    internalIp: bool
    proxyUrl: str

@typing.type_check_only
class IgnoreJobRequest(typing_extensions.TypedDict, total=False):
    jobId: str
    overrideDeployPolicy: _list[str]
    phaseId: str

@typing.type_check_only
class IgnoreJobResponse(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Job(typing_extensions.TypedDict, total=False):
    advanceChildRolloutJob: AdvanceChildRolloutJob
    createChildRolloutJob: CreateChildRolloutJob
    deployJob: DeployJob
    id: str
    jobRun: str
    postdeployJob: PostdeployJob
    predeployJob: PredeployJob
    skipMessage: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "PENDING",
        "DISABLED",
        "IN_PROGRESS",
        "SUCCEEDED",
        "FAILED",
        "ABORTED",
        "SKIPPED",
        "IGNORED",
    ]
    verifyJob: VerifyJob

@typing.type_check_only
class JobRun(typing_extensions.TypedDict, total=False):
    advanceChildRolloutJobRun: AdvanceChildRolloutJobRun
    createChildRolloutJobRun: CreateChildRolloutJobRun
    createTime: str
    deployJobRun: DeployJobRun
    endTime: str
    etag: str
    jobId: str
    name: str
    phaseId: str
    postdeployJobRun: PostdeployJobRun
    predeployJobRun: PredeployJobRun
    startTime: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "IN_PROGRESS",
        "SUCCEEDED",
        "FAILED",
        "TERMINATING",
        "TERMINATED",
    ]
    uid: str
    verifyJobRun: VerifyJobRun

@typing.type_check_only
class JobRunNotificationEvent(typing_extensions.TypedDict, total=False):
    jobRun: str
    message: str
    pipelineUid: str
    release: str
    releaseUid: str
    rollout: str
    rolloutUid: str
    targetId: str
    type: typing_extensions.Literal[
        "TYPE_UNSPECIFIED",
        "TYPE_PUBSUB_NOTIFICATION_FAILURE",
        "TYPE_RESOURCE_STATE_CHANGE",
        "TYPE_PROCESS_ABORTED",
        "TYPE_RESTRICTION_VIOLATED",
        "TYPE_RESOURCE_DELETED",
        "TYPE_ROLLOUT_UPDATE",
        "TYPE_DEPLOY_POLICY_EVALUATION",
        "TYPE_RENDER_STATUES_CHANGE",
    ]

@typing.type_check_only
class KubernetesConfig(typing_extensions.TypedDict, total=False):
    gatewayServiceMesh: GatewayServiceMesh
    serviceNetworking: ServiceNetworking

@typing.type_check_only
class ListAutomationRunsResponse(typing_extensions.TypedDict, total=False):
    automationRuns: _list[AutomationRun]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListAutomationsResponse(typing_extensions.TypedDict, total=False):
    automations: _list[Automation]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListCustomTargetTypesResponse(typing_extensions.TypedDict, total=False):
    customTargetTypes: _list[CustomTargetType]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListDeliveryPipelinesResponse(typing_extensions.TypedDict, total=False):
    deliveryPipelines: _list[DeliveryPipeline]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListDeployPoliciesResponse(typing_extensions.TypedDict, total=False):
    deployPolicies: _list[DeployPolicy]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListJobRunsResponse(typing_extensions.TypedDict, total=False):
    jobRuns: _list[JobRun]
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
class Metadata(typing_extensions.TypedDict, total=False):
    automation: AutomationRolloutMetadata
    cloudRun: CloudRunMetadata
    custom: CustomMetadata

@typing.type_check_only
class MultiTarget(typing_extensions.TypedDict, total=False):
    targetIds: _list[str]

@typing.type_check_only
class OneTimeWindow(typing_extensions.TypedDict, total=False):
    endDate: Date
    endTime: TimeOfDay
    startDate: Date
    startTime: TimeOfDay

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
class Phase(typing_extensions.TypedDict, total=False):
    childRolloutJobs: ChildRolloutJobs
    deploymentJobs: DeploymentJobs
    id: str
    skipMessage: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "PENDING",
        "IN_PROGRESS",
        "SUCCEEDED",
        "FAILED",
        "ABORTED",
        "SKIPPED",
    ]

@typing.type_check_only
class PhaseArtifact(typing_extensions.TypedDict, total=False):
    jobManifestsPath: str
    manifestPath: str
    skaffoldConfigPath: str

@typing.type_check_only
class PhaseConfig(typing_extensions.TypedDict, total=False):
    percentage: int
    phaseId: str
    postdeploy: Postdeploy
    predeploy: Predeploy
    profiles: _list[str]
    verify: bool

@typing.type_check_only
class PipelineCondition(typing_extensions.TypedDict, total=False):
    pipelineReadyCondition: PipelineReadyCondition
    targetsPresentCondition: TargetsPresentCondition
    targetsTypeCondition: TargetsTypeCondition

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
class PolicyRule(typing_extensions.TypedDict, total=False):
    rolloutRestriction: RolloutRestriction

@typing.type_check_only
class PolicyViolation(typing_extensions.TypedDict, total=False):
    policyViolationDetails: _list[PolicyViolationDetails]

@typing.type_check_only
class PolicyViolationDetails(typing_extensions.TypedDict, total=False):
    failureMessage: str
    policy: str
    ruleId: str

@typing.type_check_only
class Postdeploy(typing_extensions.TypedDict, total=False):
    actions: _list[str]

@typing.type_check_only
class PostdeployJob(typing_extensions.TypedDict, total=False):
    actions: _list[str]

@typing.type_check_only
class PostdeployJobRun(typing_extensions.TypedDict, total=False):
    build: str
    failureCause: typing_extensions.Literal[
        "FAILURE_CAUSE_UNSPECIFIED",
        "CLOUD_BUILD_UNAVAILABLE",
        "EXECUTION_FAILED",
        "DEADLINE_EXCEEDED",
        "CLOUD_BUILD_REQUEST_FAILED",
    ]
    failureMessage: str

@typing.type_check_only
class Predeploy(typing_extensions.TypedDict, total=False):
    actions: _list[str]

@typing.type_check_only
class PredeployJob(typing_extensions.TypedDict, total=False):
    actions: _list[str]

@typing.type_check_only
class PredeployJobRun(typing_extensions.TypedDict, total=False):
    build: str
    failureCause: typing_extensions.Literal[
        "FAILURE_CAUSE_UNSPECIFIED",
        "CLOUD_BUILD_UNAVAILABLE",
        "EXECUTION_FAILED",
        "DEADLINE_EXCEEDED",
        "CLOUD_BUILD_REQUEST_FAILED",
    ]
    failureMessage: str

@typing.type_check_only
class PrivatePool(typing_extensions.TypedDict, total=False):
    artifactStorage: str
    serviceAccount: str
    workerPool: str

@typing.type_check_only
class PromoteReleaseOperation(typing_extensions.TypedDict, total=False):
    phase: str
    rollout: str
    targetId: str
    wait: str

@typing.type_check_only
class PromoteReleaseRule(typing_extensions.TypedDict, total=False):
    condition: AutomationRuleCondition
    destinationPhase: str
    destinationTargetId: str
    id: str
    wait: str

@typing.type_check_only
class Release(typing_extensions.TypedDict, total=False):
    abandoned: bool
    annotations: dict[str, typing.Any]
    buildArtifacts: _list[BuildArtifact]
    condition: ReleaseCondition
    createTime: str
    customTargetTypeSnapshots: _list[CustomTargetType]
    deliveryPipelineSnapshot: DeliveryPipeline
    deployParameters: dict[str, typing.Any]
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
class ReleaseCondition(typing_extensions.TypedDict, total=False):
    releaseReadyCondition: ReleaseReadyCondition
    skaffoldSupportedCondition: SkaffoldSupportedCondition

@typing.type_check_only
class ReleaseNotificationEvent(typing_extensions.TypedDict, total=False):
    message: str
    pipelineUid: str
    release: str
    releaseUid: str
    type: typing_extensions.Literal[
        "TYPE_UNSPECIFIED",
        "TYPE_PUBSUB_NOTIFICATION_FAILURE",
        "TYPE_RESOURCE_STATE_CHANGE",
        "TYPE_PROCESS_ABORTED",
        "TYPE_RESTRICTION_VIOLATED",
        "TYPE_RESOURCE_DELETED",
        "TYPE_ROLLOUT_UPDATE",
        "TYPE_DEPLOY_POLICY_EVALUATION",
        "TYPE_RENDER_STATUES_CHANGE",
    ]

@typing.type_check_only
class ReleaseReadyCondition(typing_extensions.TypedDict, total=False):
    status: bool

@typing.type_check_only
class ReleaseRenderEvent(typing_extensions.TypedDict, total=False):
    message: str
    pipelineUid: str
    release: str
    releaseRenderState: typing_extensions.Literal[
        "RENDER_STATE_UNSPECIFIED", "SUCCEEDED", "FAILED", "IN_PROGRESS"
    ]
    type: typing_extensions.Literal[
        "TYPE_UNSPECIFIED",
        "TYPE_PUBSUB_NOTIFICATION_FAILURE",
        "TYPE_RESOURCE_STATE_CHANGE",
        "TYPE_PROCESS_ABORTED",
        "TYPE_RESTRICTION_VIOLATED",
        "TYPE_RESOURCE_DELETED",
        "TYPE_ROLLOUT_UPDATE",
        "TYPE_DEPLOY_POLICY_EVALUATION",
        "TYPE_RENDER_STATUES_CHANGE",
    ]

@typing.type_check_only
class RenderMetadata(typing_extensions.TypedDict, total=False):
    cloudRun: CloudRunRenderMetadata
    custom: CustomMetadata

@typing.type_check_only
class RepairPhase(typing_extensions.TypedDict, total=False):
    retry: RetryPhase
    rollback: RollbackAttempt

@typing.type_check_only
class RepairPhaseConfig(typing_extensions.TypedDict, total=False):
    retry: Retry
    rollback: Rollback

@typing.type_check_only
class RepairRolloutOperation(typing_extensions.TypedDict, total=False):
    currentRepairPhaseIndex: str
    jobId: str
    phaseId: str
    repairPhases: _list[RepairPhase]
    rollout: str

@typing.type_check_only
class RepairRolloutRule(typing_extensions.TypedDict, total=False):
    condition: AutomationRuleCondition
    id: str
    jobs: _list[str]
    phases: _list[str]
    repairPhases: _list[RepairPhaseConfig]

@typing.type_check_only
class Retry(typing_extensions.TypedDict, total=False):
    attempts: str
    backoffMode: typing_extensions.Literal[
        "BACKOFF_MODE_UNSPECIFIED", "BACKOFF_MODE_LINEAR", "BACKOFF_MODE_EXPONENTIAL"
    ]
    wait: str

@typing.type_check_only
class RetryAttempt(typing_extensions.TypedDict, total=False):
    attempt: str
    state: typing_extensions.Literal[
        "REPAIR_STATE_UNSPECIFIED",
        "REPAIR_STATE_SUCCEEDED",
        "REPAIR_STATE_CANCELLED",
        "REPAIR_STATE_FAILED",
        "REPAIR_STATE_IN_PROGRESS",
        "REPAIR_STATE_PENDING",
        "REPAIR_STATE_ABORTED",
    ]
    stateDesc: str
    wait: str

@typing.type_check_only
class RetryJobRequest(typing_extensions.TypedDict, total=False):
    jobId: str
    overrideDeployPolicy: _list[str]
    phaseId: str

@typing.type_check_only
class RetryJobResponse(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class RetryPhase(typing_extensions.TypedDict, total=False):
    attempts: _list[RetryAttempt]
    backoffMode: typing_extensions.Literal[
        "BACKOFF_MODE_UNSPECIFIED", "BACKOFF_MODE_LINEAR", "BACKOFF_MODE_EXPONENTIAL"
    ]
    totalAttempts: str

@typing.type_check_only
class Rollback(typing_extensions.TypedDict, total=False):
    destinationPhase: str
    disableRollbackIfRolloutPending: bool

@typing.type_check_only
class RollbackAttempt(typing_extensions.TypedDict, total=False):
    destinationPhase: str
    disableRollbackIfRolloutPending: bool
    rolloutId: str
    state: typing_extensions.Literal[
        "REPAIR_STATE_UNSPECIFIED",
        "REPAIR_STATE_SUCCEEDED",
        "REPAIR_STATE_CANCELLED",
        "REPAIR_STATE_FAILED",
        "REPAIR_STATE_IN_PROGRESS",
        "REPAIR_STATE_PENDING",
        "REPAIR_STATE_ABORTED",
    ]
    stateDesc: str

@typing.type_check_only
class RollbackTargetConfig(typing_extensions.TypedDict, total=False):
    rollout: Rollout
    startingPhaseId: str

@typing.type_check_only
class RollbackTargetRequest(typing_extensions.TypedDict, total=False):
    overrideDeployPolicy: _list[str]
    releaseId: str
    rollbackConfig: RollbackTargetConfig
    rolloutId: str
    rolloutToRollBack: str
    targetId: str
    validateOnly: bool

@typing.type_check_only
class RollbackTargetResponse(typing_extensions.TypedDict, total=False):
    rollbackConfig: RollbackTargetConfig

@typing.type_check_only
class Rollout(typing_extensions.TypedDict, total=False):
    activeRepairAutomationRun: str
    annotations: dict[str, typing.Any]
    approvalState: typing_extensions.Literal[
        "APPROVAL_STATE_UNSPECIFIED",
        "NEEDS_APPROVAL",
        "DOES_NOT_NEED_APPROVAL",
        "APPROVED",
        "REJECTED",
    ]
    approveTime: str
    controllerRollout: str
    createTime: str
    deployEndTime: str
    deployFailureCause: typing_extensions.Literal[
        "FAILURE_CAUSE_UNSPECIFIED",
        "CLOUD_BUILD_UNAVAILABLE",
        "EXECUTION_FAILED",
        "DEADLINE_EXCEEDED",
        "RELEASE_FAILED",
        "RELEASE_ABANDONED",
        "VERIFICATION_CONFIG_NOT_FOUND",
        "CLOUD_BUILD_REQUEST_FAILED",
        "OPERATION_FEATURE_NOT_SUPPORTED",
    ]
    deployStartTime: str
    deployingBuild: str
    description: str
    enqueueTime: str
    etag: str
    failureReason: str
    labels: dict[str, typing.Any]
    metadata: Metadata
    name: str
    phases: _list[Phase]
    rollbackOfRollout: str
    rolledBackByRollouts: _list[str]
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "SUCCEEDED",
        "FAILED",
        "IN_PROGRESS",
        "PENDING_APPROVAL",
        "APPROVAL_REJECTED",
        "PENDING",
        "PENDING_RELEASE",
        "CANCELLING",
        "CANCELLED",
        "HALTED",
    ]
    targetId: str
    uid: str

@typing.type_check_only
class RolloutNotificationEvent(typing_extensions.TypedDict, total=False):
    message: str
    pipelineUid: str
    release: str
    releaseUid: str
    rollout: str
    rolloutUid: str
    targetId: str
    type: typing_extensions.Literal[
        "TYPE_UNSPECIFIED",
        "TYPE_PUBSUB_NOTIFICATION_FAILURE",
        "TYPE_RESOURCE_STATE_CHANGE",
        "TYPE_PROCESS_ABORTED",
        "TYPE_RESTRICTION_VIOLATED",
        "TYPE_RESOURCE_DELETED",
        "TYPE_ROLLOUT_UPDATE",
        "TYPE_DEPLOY_POLICY_EVALUATION",
        "TYPE_RENDER_STATUES_CHANGE",
    ]

@typing.type_check_only
class RolloutRestriction(typing_extensions.TypedDict, total=False):
    actions: _list[
        typing_extensions.Literal[
            "ROLLOUT_ACTIONS_UNSPECIFIED",
            "ADVANCE",
            "APPROVE",
            "CANCEL",
            "CREATE",
            "IGNORE_JOB",
            "RETRY_JOB",
            "ROLLBACK",
            "TERMINATE_JOBRUN",
        ]
    ]
    id: str
    invokers: _list[
        typing_extensions.Literal["INVOKER_UNSPECIFIED", "USER", "DEPLOY_AUTOMATION"]
    ]
    timeWindows: TimeWindows

@typing.type_check_only
class RolloutUpdateEvent(typing_extensions.TypedDict, total=False):
    message: str
    pipelineUid: str
    release: str
    releaseUid: str
    rollout: str
    rolloutUpdateType: typing_extensions.Literal[
        "ROLLOUT_UPDATE_TYPE_UNSPECIFIED",
        "PENDING",
        "PENDING_RELEASE",
        "IN_PROGRESS",
        "CANCELLING",
        "CANCELLED",
        "HALTED",
        "SUCCEEDED",
        "FAILED",
        "APPROVAL_REQUIRED",
        "APPROVED",
        "REJECTED",
        "ADVANCE_REQUIRED",
        "ADVANCED",
    ]
    targetId: str
    type: typing_extensions.Literal[
        "TYPE_UNSPECIFIED",
        "TYPE_PUBSUB_NOTIFICATION_FAILURE",
        "TYPE_RESOURCE_STATE_CHANGE",
        "TYPE_PROCESS_ABORTED",
        "TYPE_RESTRICTION_VIOLATED",
        "TYPE_RESOURCE_DELETED",
        "TYPE_ROLLOUT_UPDATE",
        "TYPE_DEPLOY_POLICY_EVALUATION",
        "TYPE_RENDER_STATUES_CHANGE",
    ]

@typing.type_check_only
class RouteDestinations(typing_extensions.TypedDict, total=False):
    destinationIds: _list[str]
    propagateService: bool

@typing.type_check_only
class RuntimeConfig(typing_extensions.TypedDict, total=False):
    cloudRun: CloudRunConfig
    kubernetes: KubernetesConfig

@typing.type_check_only
class SerialPipeline(typing_extensions.TypedDict, total=False):
    stages: _list[Stage]

@typing.type_check_only
class ServiceNetworking(typing_extensions.TypedDict, total=False):
    deployment: str
    disablePodOverprovisioning: bool
    podSelectorLabel: str
    service: str

@typing.type_check_only
class SetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    policy: Policy
    updateMask: str

@typing.type_check_only
class SkaffoldGCBRepoSource(typing_extensions.TypedDict, total=False):
    path: str
    ref: str
    repository: str

@typing.type_check_only
class SkaffoldGCSSource(typing_extensions.TypedDict, total=False):
    path: str
    source: str

@typing.type_check_only
class SkaffoldGitSource(typing_extensions.TypedDict, total=False):
    path: str
    ref: str
    repo: str

@typing.type_check_only
class SkaffoldModules(typing_extensions.TypedDict, total=False):
    configs: _list[str]
    git: SkaffoldGitSource
    googleCloudBuildRepo: SkaffoldGCBRepoSource
    googleCloudStorage: SkaffoldGCSSource

@typing.type_check_only
class SkaffoldSupportedCondition(typing_extensions.TypedDict, total=False):
    maintenanceModeTime: str
    skaffoldSupportState: typing_extensions.Literal[
        "SKAFFOLD_SUPPORT_STATE_UNSPECIFIED",
        "SKAFFOLD_SUPPORT_STATE_SUPPORTED",
        "SKAFFOLD_SUPPORT_STATE_MAINTENANCE_MODE",
        "SKAFFOLD_SUPPORT_STATE_UNSUPPORTED",
    ]
    status: bool
    supportExpirationTime: str

@typing.type_check_only
class SkaffoldVersion(typing_extensions.TypedDict, total=False):
    maintenanceModeTime: str
    supportEndDate: Date
    supportExpirationTime: str
    version: str

@typing.type_check_only
class Stage(typing_extensions.TypedDict, total=False):
    deployParameters: _list[DeployParameters]
    profiles: _list[str]
    strategy: Strategy
    targetId: str

@typing.type_check_only
class Standard(typing_extensions.TypedDict, total=False):
    postdeploy: Postdeploy
    predeploy: Predeploy
    verify: bool

@typing.type_check_only
class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class Strategy(typing_extensions.TypedDict, total=False):
    canary: Canary
    standard: Standard

@typing.type_check_only
class Target(typing_extensions.TypedDict, total=False):
    annotations: dict[str, typing.Any]
    anthosCluster: AnthosCluster
    associatedEntities: dict[str, typing.Any]
    createTime: str
    customTarget: CustomTarget
    deployParameters: dict[str, typing.Any]
    description: str
    etag: str
    executionConfigs: _list[ExecutionConfig]
    gke: GkeCluster
    labels: dict[str, typing.Any]
    multiTarget: MultiTarget
    name: str
    requireApproval: bool
    run: CloudRunLocation
    targetId: str
    uid: str
    updateTime: str

@typing.type_check_only
class TargetArtifact(typing_extensions.TypedDict, total=False):
    artifactUri: str
    manifestPath: str
    phaseArtifacts: dict[str, typing.Any]
    skaffoldConfigPath: str

@typing.type_check_only
class TargetAttribute(typing_extensions.TypedDict, total=False):
    id: str
    labels: dict[str, typing.Any]

@typing.type_check_only
class TargetNotificationEvent(typing_extensions.TypedDict, total=False):
    message: str
    target: str
    type: typing_extensions.Literal[
        "TYPE_UNSPECIFIED",
        "TYPE_PUBSUB_NOTIFICATION_FAILURE",
        "TYPE_RESOURCE_STATE_CHANGE",
        "TYPE_PROCESS_ABORTED",
        "TYPE_RESTRICTION_VIOLATED",
        "TYPE_RESOURCE_DELETED",
        "TYPE_ROLLOUT_UPDATE",
        "TYPE_DEPLOY_POLICY_EVALUATION",
        "TYPE_RENDER_STATUES_CHANGE",
    ]

@typing.type_check_only
class TargetRender(typing_extensions.TypedDict, total=False):
    failureCause: typing_extensions.Literal[
        "FAILURE_CAUSE_UNSPECIFIED",
        "CLOUD_BUILD_UNAVAILABLE",
        "EXECUTION_FAILED",
        "CLOUD_BUILD_REQUEST_FAILED",
        "VERIFICATION_CONFIG_NOT_FOUND",
        "CUSTOM_ACTION_NOT_FOUND",
        "DEPLOYMENT_STRATEGY_NOT_SUPPORTED",
        "RENDER_FEATURE_NOT_SUPPORTED",
    ]
    failureMessage: str
    metadata: RenderMetadata
    renderingBuild: str
    renderingState: typing_extensions.Literal[
        "TARGET_RENDER_STATE_UNSPECIFIED", "SUCCEEDED", "FAILED", "IN_PROGRESS"
    ]

@typing.type_check_only
class Targets(typing_extensions.TypedDict, total=False):
    destinationTargetId: str
    sourceTargetId: str

@typing.type_check_only
class TargetsPresentCondition(typing_extensions.TypedDict, total=False):
    missingTargets: _list[str]
    status: bool
    updateTime: str

@typing.type_check_only
class TargetsTypeCondition(typing_extensions.TypedDict, total=False):
    errorDetails: str
    status: bool

@typing.type_check_only
class TerminateJobRunRequest(typing_extensions.TypedDict, total=False):
    overrideDeployPolicy: _list[str]

@typing.type_check_only
class TerminateJobRunResponse(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class TestIamPermissionsRequest(typing_extensions.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class TestIamPermissionsResponse(typing_extensions.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class TimeOfDay(typing_extensions.TypedDict, total=False):
    hours: int
    minutes: int
    nanos: int
    seconds: int

@typing.type_check_only
class TimeWindows(typing_extensions.TypedDict, total=False):
    oneTimeWindows: _list[OneTimeWindow]
    timeZone: str
    weeklyWindows: _list[WeeklyWindow]

@typing.type_check_only
class TimedPromoteReleaseCondition(typing_extensions.TypedDict, total=False):
    nextPromotionTime: str
    targetsList: _list[Targets]

@typing.type_check_only
class TimedPromoteReleaseOperation(typing_extensions.TypedDict, total=False):
    phase: str
    release: str
    targetId: str

@typing.type_check_only
class TimedPromoteReleaseRule(typing_extensions.TypedDict, total=False):
    condition: AutomationRuleCondition
    destinationPhase: str
    destinationTargetId: str
    id: str
    schedule: str
    timeZone: str

@typing.type_check_only
class VerifyJob(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class VerifyJobRun(typing_extensions.TypedDict, total=False):
    artifactUri: str
    build: str
    eventLogPath: str
    failureCause: typing_extensions.Literal[
        "FAILURE_CAUSE_UNSPECIFIED",
        "CLOUD_BUILD_UNAVAILABLE",
        "EXECUTION_FAILED",
        "DEADLINE_EXCEEDED",
        "VERIFICATION_CONFIG_NOT_FOUND",
        "CLOUD_BUILD_REQUEST_FAILED",
    ]
    failureMessage: str

@typing.type_check_only
class WeeklyWindow(typing_extensions.TypedDict, total=False):
    daysOfWeek: _list[
        typing_extensions.Literal[
            "DAY_OF_WEEK_UNSPECIFIED",
            "MONDAY",
            "TUESDAY",
            "WEDNESDAY",
            "THURSDAY",
            "FRIDAY",
            "SATURDAY",
            "SUNDAY",
        ]
    ]
    endTime: TimeOfDay
    startTime: TimeOfDay
