import typing

_list = list

@typing.type_check_only
class AuditConfig(typing.TypedDict, total=False):
    auditLogConfigs: _list[AuditLogConfig]
    service: str

@typing.type_check_only
class AuditLogConfig(typing.TypedDict, total=False):
    exemptedMembers: _list[str]
    logType: typing.Literal[
        "LOG_TYPE_UNSPECIFIED", "ADMIN_READ", "DATA_WRITE", "DATA_READ"
    ]

@typing.type_check_only
class BatchCreateRepositoriesRequest(typing.TypedDict, total=False):
    requests: _list[CreateRepositoryRequest]

@typing.type_check_only
class BatchCreateRepositoriesResponse(typing.TypedDict, total=False):
    repositories: _list[Repository]

@typing.type_check_only
class Binding(typing.TypedDict, total=False):
    condition: Expr
    members: _list[str]
    role: str

@typing.type_check_only
class BitbucketCloudConfig(typing.TypedDict, total=False):
    authorizerCredential: UserCredential
    readAuthorizerCredential: UserCredential
    webhookSecretSecretVersion: str
    workspace: str

@typing.type_check_only
class BitbucketDataCenterConfig(typing.TypedDict, total=False):
    authorizerCredential: UserCredential
    hostUri: str
    readAuthorizerCredential: UserCredential
    serverVersion: str
    serviceDirectoryConfig: GoogleDevtoolsCloudbuildV2ServiceDirectoryConfig
    sslCa: str
    webhookSecretSecretVersion: str

@typing.type_check_only
class CancelOperationRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class ChildStatusReference(typing.TypedDict, total=False):
    name: str
    pipelineTaskName: str
    type: typing.Literal["TYPE_UNSPECIFIED", "TASK_RUN"]
    whenExpressions: _list[WhenExpression]

@typing.type_check_only
class Connection(typing.TypedDict, total=False):
    annotations: dict[str, typing.Any]
    bitbucketCloudConfig: BitbucketCloudConfig
    bitbucketDataCenterConfig: BitbucketDataCenterConfig
    createTime: str
    disabled: bool
    etag: str
    githubConfig: GitHubConfig
    githubEnterpriseConfig: GoogleDevtoolsCloudbuildV2GitHubEnterpriseConfig
    gitlabConfig: GoogleDevtoolsCloudbuildV2GitLabConfig
    installationState: InstallationState
    name: str
    reconciling: bool
    updateTime: str

@typing.type_check_only
class CreateRepositoryRequest(typing.TypedDict, total=False):
    parent: str
    repository: Repository
    repositoryId: str

@typing.type_check_only
class EmbeddedTask(typing.TypedDict, total=False):
    annotations: dict[str, typing.Any]
    taskSpec: TaskSpec

@typing.type_check_only
class Empty(typing.TypedDict, total=False): ...

@typing.type_check_only
class EmptyDirVolumeSource(typing.TypedDict, total=False): ...

@typing.type_check_only
class EnvVar(typing.TypedDict, total=False):
    name: str
    value: str

@typing.type_check_only
class ExecAction(typing.TypedDict, total=False):
    command: _list[str]

@typing.type_check_only
class Expr(typing.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str

@typing.type_check_only
class FetchGitRefsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    refNames: _list[str]

@typing.type_check_only
class FetchLinkableRepositoriesResponse(typing.TypedDict, total=False):
    nextPageToken: str
    repositories: _list[Repository]

@typing.type_check_only
class FetchReadTokenRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class FetchReadTokenResponse(typing.TypedDict, total=False):
    expirationTime: str
    token: str

@typing.type_check_only
class FetchReadWriteTokenRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class FetchReadWriteTokenResponse(typing.TypedDict, total=False):
    expirationTime: str
    token: str

@typing.type_check_only
class GitHubConfig(typing.TypedDict, total=False):
    appInstallationId: str
    authorizerCredential: OAuthCredential

@typing.type_check_only
class GoogleDevtoolsCloudbuildV2Condition(typing.TypedDict, total=False):
    lastTransitionTime: str
    message: str
    reason: str
    severity: typing.Literal["SEVERITY_UNSPECIFIED", "WARNING", "INFO"]
    status: typing.Literal["UNKNOWN", "TRUE", "FALSE"]
    type: str

@typing.type_check_only
class GoogleDevtoolsCloudbuildV2GitHubEnterpriseConfig(typing.TypedDict, total=False):
    apiKey: str
    appId: str
    appInstallationId: str
    appSlug: str
    hostUri: str
    privateKeySecretVersion: str
    serverVersion: str
    serviceDirectoryConfig: GoogleDevtoolsCloudbuildV2ServiceDirectoryConfig
    sslCa: str
    webhookSecretSecretVersion: str

@typing.type_check_only
class GoogleDevtoolsCloudbuildV2GitLabConfig(typing.TypedDict, total=False):
    authorizerCredential: UserCredential
    hostUri: str
    readAuthorizerCredential: UserCredential
    serverVersion: str
    serviceDirectoryConfig: GoogleDevtoolsCloudbuildV2ServiceDirectoryConfig
    sslCa: str
    webhookSecretSecretVersion: str

@typing.type_check_only
class GoogleDevtoolsCloudbuildV2OperationMetadata(typing.TypedDict, total=False):
    apiVersion: str
    createTime: str
    endTime: str
    requestedCancellation: bool
    statusMessage: str
    target: str
    verb: str

@typing.type_check_only
class GoogleDevtoolsCloudbuildV2ServiceDirectoryConfig(typing.TypedDict, total=False):
    service: str

@typing.type_check_only
class HttpBody(typing.TypedDict, total=False):
    contentType: str
    data: str
    extensions: _list[dict[str, typing.Any]]

@typing.type_check_only
class InstallationState(typing.TypedDict, total=False):
    actionUri: str
    message: str
    stage: typing.Literal[
        "STAGE_UNSPECIFIED",
        "PENDING_CREATE_APP",
        "PENDING_USER_OAUTH",
        "PENDING_INSTALL_APP",
        "COMPLETE",
    ]

@typing.type_check_only
class ListConnectionsResponse(typing.TypedDict, total=False):
    connections: _list[Connection]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListLocationsResponse(typing.TypedDict, total=False):
    locations: _list[Location]
    nextPageToken: str

@typing.type_check_only
class ListRepositoriesResponse(typing.TypedDict, total=False):
    nextPageToken: str
    repositories: _list[Repository]
    unreachable: _list[str]

@typing.type_check_only
class Location(typing.TypedDict, total=False):
    displayName: str
    labels: dict[str, typing.Any]
    locationId: str
    metadata: dict[str, typing.Any]
    name: str

@typing.type_check_only
class OAuthCredential(typing.TypedDict, total=False):
    oauthTokenSecretVersion: str
    username: str

@typing.type_check_only
class Operation(typing.TypedDict, total=False):
    done: bool
    error: Status
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class OperationMetadata(typing.TypedDict, total=False):
    apiVersion: str
    cancelRequested: bool
    createTime: str
    endTime: str
    statusDetail: str
    target: str
    verb: str

@typing.type_check_only
class Param(typing.TypedDict, total=False):
    name: str
    value: ParamValue

@typing.type_check_only
class ParamSpec(typing.TypedDict, total=False):
    default: ParamValue
    description: str
    name: str
    type: typing.Literal["TYPE_UNSPECIFIED", "STRING", "ARRAY", "OBJECT"]

@typing.type_check_only
class ParamValue(typing.TypedDict, total=False):
    arrayVal: _list[str]
    objectVal: dict[str, typing.Any]
    stringVal: str
    type: typing.Literal["TYPE_UNSPECIFIED", "STRING", "ARRAY", "OBJECT"]

@typing.type_check_only
class PipelineRef(typing.TypedDict, total=False):
    name: str
    params: _list[Param]
    resolver: typing.Literal[
        "RESOLVER_NAME_UNSPECIFIED",
        "BUNDLES",
        "GCB_REPO",
        "GIT",
        "DEVELOPER_CONNECT",
        "DEFAULT",
    ]

@typing.type_check_only
class PipelineResult(typing.TypedDict, total=False):
    description: str
    name: str
    type: typing.Literal["TYPE_UNSPECIFIED", "STRING", "ARRAY", "OBJECT"]
    value: ResultValue

@typing.type_check_only
class PipelineRun(typing.TypedDict, total=False):
    annotations: dict[str, typing.Any]
    childReferences: _list[ChildStatusReference]
    completionTime: str
    conditions: _list[GoogleDevtoolsCloudbuildV2Condition]
    createTime: str
    etag: str
    finallyStartTime: str
    gcbParams: dict[str, typing.Any]
    name: str
    params: _list[Param]
    pipelineRef: PipelineRef
    pipelineRunStatus: typing.Literal[
        "PIPELINE_RUN_STATUS_UNSPECIFIED", "PIPELINE_RUN_CANCELLED"
    ]
    pipelineSpec: PipelineSpec
    pipelineSpecYaml: str
    provenance: Provenance
    record: str
    resolvedPipelineSpec: PipelineSpec
    results: _list[PipelineRunResult]
    security: Security
    serviceAccount: str
    skippedTasks: _list[SkippedTask]
    startTime: str
    timeouts: TimeoutFields
    uid: str
    updateTime: str
    worker: Worker
    workerPool: str
    workflow: str
    workspaces: _list[WorkspaceBinding]

@typing.type_check_only
class PipelineRunResult(typing.TypedDict, total=False):
    name: str
    value: ResultValue

@typing.type_check_only
class PipelineSpec(typing.TypedDict, total=False):
    finallyTasks: _list[PipelineTask]
    generatedYaml: str
    params: _list[ParamSpec]
    results: _list[PipelineResult]
    tasks: _list[PipelineTask]
    workspaces: _list[PipelineWorkspaceDeclaration]

@typing.type_check_only
class PipelineTask(typing.TypedDict, total=False):
    name: str
    params: _list[Param]
    retries: int
    runAfter: _list[str]
    taskRef: TaskRef
    taskSpec: EmbeddedTask
    timeout: str
    whenExpressions: _list[WhenExpression]
    workspaces: _list[WorkspacePipelineTaskBinding]

@typing.type_check_only
class PipelineWorkspaceDeclaration(typing.TypedDict, total=False):
    description: str
    name: str
    optional: bool

@typing.type_check_only
class Policy(typing.TypedDict, total=False):
    auditConfigs: _list[AuditConfig]
    bindings: _list[Binding]
    etag: str
    version: int

@typing.type_check_only
class Probe(typing.TypedDict, total=False):
    exec: ExecAction
    periodSeconds: int

@typing.type_check_only
class PropertySpec(typing.TypedDict, total=False):
    type: typing.Literal["TYPE_UNSPECIFIED", "STRING"]

@typing.type_check_only
class Provenance(typing.TypedDict, total=False):
    enabled: typing.Literal["ENABLED_UNSPECIFIED", "REQUIRED", "OPTIMISTIC", "DISABLED"]
    region: typing.Literal["REGION_UNSPECIFIED", "GLOBAL"]
    storage: typing.Literal[
        "STORAGE_UNSPECIFIED",
        "PREFER_ARTIFACT_PROJECT",
        "ARTIFACT_PROJECT_ONLY",
        "BUILD_PROJECT_ONLY",
    ]

@typing.type_check_only
class Repository(typing.TypedDict, total=False):
    annotations: dict[str, typing.Any]
    createTime: str
    etag: str
    name: str
    remoteUri: str
    updateTime: str
    webhookId: str

@typing.type_check_only
class ResultValue(typing.TypedDict, total=False):
    arrayVal: _list[str]
    objectVal: dict[str, typing.Any]
    stringVal: str
    type: typing.Literal["TYPE_UNSPECIFIED", "STRING", "ARRAY", "OBJECT"]

@typing.type_check_only
class RunWorkflowCustomOperationMetadata(typing.TypedDict, total=False):
    apiVersion: str
    createTime: str
    endTime: str
    pipelineRunId: str
    requestedCancellation: bool
    target: str
    verb: str

@typing.type_check_only
class SecretVolumeSource(typing.TypedDict, total=False):
    secretName: str
    secretVersion: str

@typing.type_check_only
class Security(typing.TypedDict, total=False):
    privilegeMode: typing.Literal[
        "PRIVILEGE_MODE_UNSPECIFIED", "PRIVILEGED", "UNPRIVILEGED"
    ]
    serviceAccount: str

@typing.type_check_only
class SecurityContext(typing.TypedDict, total=False):
    allowPrivilegeEscalation: bool
    privileged: bool
    runAsGroup: str
    runAsNonRoot: bool
    runAsUser: str

@typing.type_check_only
class SetIamPolicyRequest(typing.TypedDict, total=False):
    policy: Policy
    updateMask: str

@typing.type_check_only
class Sidecar(typing.TypedDict, total=False):
    args: _list[str]
    command: _list[str]
    env: _list[EnvVar]
    image: str
    name: str
    readinessProbe: Probe
    script: str
    securityContext: SecurityContext
    volumeMounts: _list[VolumeMount]
    workingDir: str

@typing.type_check_only
class SkippedTask(typing.TypedDict, total=False):
    name: str
    reason: str
    whenExpressions: _list[WhenExpression]

@typing.type_check_only
class Status(typing.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class Step(typing.TypedDict, total=False):
    args: _list[str]
    command: _list[str]
    env: _list[EnvVar]
    image: str
    name: str
    onError: typing.Literal["ON_ERROR_TYPE_UNSPECIFIED", "STOP_AND_FAIL", "CONTINUE"]
    params: _list[Param]
    ref: StepRef
    script: str
    securityContext: SecurityContext
    timeout: str
    volumeMounts: _list[VolumeMount]
    workingDir: str

@typing.type_check_only
class StepRef(typing.TypedDict, total=False):
    name: str
    params: _list[Param]
    resolver: typing.Literal[
        "RESOLVER_NAME_UNSPECIFIED",
        "BUNDLES",
        "GCB_REPO",
        "GIT",
        "DEVELOPER_CONNECT",
        "DEFAULT",
    ]

@typing.type_check_only
class StepTemplate(typing.TypedDict, total=False):
    env: _list[EnvVar]
    volumeMounts: _list[VolumeMount]

@typing.type_check_only
class TaskRef(typing.TypedDict, total=False):
    name: str
    params: _list[Param]
    resolver: typing.Literal[
        "RESOLVER_NAME_UNSPECIFIED",
        "BUNDLES",
        "GCB_REPO",
        "GIT",
        "DEVELOPER_CONNECT",
        "DEFAULT",
    ]

@typing.type_check_only
class TaskResult(typing.TypedDict, total=False):
    description: str
    name: str
    properties: dict[str, typing.Any]
    type: typing.Literal["TYPE_UNSPECIFIED", "STRING", "ARRAY", "OBJECT"]
    value: ParamValue

@typing.type_check_only
class TaskSpec(typing.TypedDict, total=False):
    description: str
    managedSidecars: _list[
        typing.Literal["MANAGED_SIDECAR_UNSPECIFIED", "PRIVILEGED_DOCKER_DAEMON"]
    ]
    params: _list[ParamSpec]
    results: _list[TaskResult]
    sidecars: _list[Sidecar]
    stepTemplate: StepTemplate
    steps: _list[Step]
    volumes: _list[VolumeSource]
    workspaces: _list[WorkspaceDeclaration]

@typing.type_check_only
class TestIamPermissionsRequest(typing.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class TestIamPermissionsResponse(typing.TypedDict, total=False):
    permissions: _list[str]

AlternativeTimeoutFields = typing.TypedDict(
    "AlternativeTimeoutFields",
    {
        "finally": str,
        "pipeline": str,
        "tasks": str,
    },
    total=False,
)

@typing.type_check_only
class TimeoutFields(AlternativeTimeoutFields): ...

@typing.type_check_only
class UserCredential(typing.TypedDict, total=False):
    userTokenSecretVersion: str
    username: str

@typing.type_check_only
class VolumeMount(typing.TypedDict, total=False):
    mountPath: str
    name: str
    readOnly: bool
    subPath: str
    subPathExpr: str

@typing.type_check_only
class VolumeSource(typing.TypedDict, total=False):
    emptyDir: EmptyDirVolumeSource
    name: str

@typing.type_check_only
class WhenExpression(typing.TypedDict, total=False):
    expressionOperator: typing.Literal[
        "EXPRESSION_OPERATOR_UNSPECIFIED", "IN", "NOT_IN"
    ]
    input: str
    values: _list[str]

@typing.type_check_only
class Worker(typing.TypedDict, total=False):
    machineType: str

@typing.type_check_only
class WorkspaceBinding(typing.TypedDict, total=False):
    name: str
    secret: SecretVolumeSource
    subPath: str

@typing.type_check_only
class WorkspaceDeclaration(typing.TypedDict, total=False):
    description: str
    mountPath: str
    name: str
    optional: bool
    readOnly: bool

@typing.type_check_only
class WorkspacePipelineTaskBinding(typing.TypedDict, total=False):
    name: str
    subPath: str
    workspace: str
