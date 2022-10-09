import typing

import typing_extensions

_list = list

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
class BuildConfig(typing_extensions.TypedDict, total=False):
    build: str
    dockerRepository: str
    entryPoint: str
    environmentVariables: dict[str, typing.Any]
    runtime: str
    source: Source
    sourceProvenance: SourceProvenance
    workerPool: str

@typing.type_check_only
class EventFilter(typing_extensions.TypedDict, total=False):
    attribute: str
    operator: str
    value: str

@typing.type_check_only
class EventTrigger(typing_extensions.TypedDict, total=False):
    channel: str
    eventFilters: _list[EventFilter]
    eventType: str
    pubsubTopic: str
    retryPolicy: typing_extensions.Literal[
        "RETRY_POLICY_UNSPECIFIED", "RETRY_POLICY_DO_NOT_RETRY", "RETRY_POLICY_RETRY"
    ]
    serviceAccountEmail: str
    trigger: str
    triggerRegion: str

@typing.type_check_only
class Expr(typing_extensions.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str

@typing.type_check_only
class Function(typing_extensions.TypedDict, total=False):
    buildConfig: BuildConfig
    description: str
    environment: typing_extensions.Literal["ENVIRONMENT_UNSPECIFIED", "GEN_1", "GEN_2"]
    eventTrigger: EventTrigger
    labels: dict[str, typing.Any]
    name: str
    serviceConfig: ServiceConfig
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "ACTIVE", "FAILED", "DEPLOYING", "DELETING", "UNKNOWN"
    ]
    stateMessages: _list[GoogleCloudFunctionsV2alphaStateMessage]
    updateTime: str

@typing.type_check_only
class GenerateDownloadUrlRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class GenerateDownloadUrlResponse(typing_extensions.TypedDict, total=False):
    downloadUrl: str

@typing.type_check_only
class GenerateUploadUrlRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class GenerateUploadUrlResponse(typing_extensions.TypedDict, total=False):
    storageSource: StorageSource
    uploadUrl: str

@typing.type_check_only
class GoogleCloudFunctionsV2OperationMetadata(typing_extensions.TypedDict, total=False):
    apiVersion: str
    cancelRequested: bool
    createTime: str
    endTime: str
    requestResource: dict[str, typing.Any]
    stages: _list[GoogleCloudFunctionsV2Stage]
    statusDetail: str
    target: str
    verb: str

@typing.type_check_only
class GoogleCloudFunctionsV2Stage(typing_extensions.TypedDict, total=False):
    message: str
    name: typing_extensions.Literal[
        "NAME_UNSPECIFIED",
        "ARTIFACT_REGISTRY",
        "BUILD",
        "SERVICE",
        "TRIGGER",
        "SERVICE_ROLLBACK",
        "TRIGGER_ROLLBACK",
    ]
    resource: str
    resourceUri: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "NOT_STARTED", "IN_PROGRESS", "COMPLETE"
    ]
    stateMessages: _list[GoogleCloudFunctionsV2StateMessage]

@typing.type_check_only
class GoogleCloudFunctionsV2StateMessage(typing_extensions.TypedDict, total=False):
    message: str
    severity: typing_extensions.Literal[
        "SEVERITY_UNSPECIFIED", "ERROR", "WARNING", "INFO"
    ]
    type: str

@typing.type_check_only
class GoogleCloudFunctionsV2alphaOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    apiVersion: str
    cancelRequested: bool
    createTime: str
    endTime: str
    requestResource: dict[str, typing.Any]
    stages: _list[GoogleCloudFunctionsV2alphaStage]
    statusDetail: str
    target: str
    verb: str

@typing.type_check_only
class GoogleCloudFunctionsV2alphaStage(typing_extensions.TypedDict, total=False):
    message: str
    name: typing_extensions.Literal[
        "NAME_UNSPECIFIED",
        "ARTIFACT_REGISTRY",
        "BUILD",
        "SERVICE",
        "TRIGGER",
        "SERVICE_ROLLBACK",
        "TRIGGER_ROLLBACK",
    ]
    resource: str
    resourceUri: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "NOT_STARTED", "IN_PROGRESS", "COMPLETE"
    ]
    stateMessages: _list[GoogleCloudFunctionsV2alphaStateMessage]

@typing.type_check_only
class GoogleCloudFunctionsV2alphaStateMessage(typing_extensions.TypedDict, total=False):
    message: str
    severity: typing_extensions.Literal[
        "SEVERITY_UNSPECIFIED", "ERROR", "WARNING", "INFO"
    ]
    type: str

@typing.type_check_only
class GoogleCloudFunctionsV2betaOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    apiVersion: str
    cancelRequested: bool
    createTime: str
    endTime: str
    requestResource: dict[str, typing.Any]
    stages: _list[GoogleCloudFunctionsV2betaStage]
    statusDetail: str
    target: str
    verb: str

@typing.type_check_only
class GoogleCloudFunctionsV2betaStage(typing_extensions.TypedDict, total=False):
    message: str
    name: typing_extensions.Literal[
        "NAME_UNSPECIFIED",
        "ARTIFACT_REGISTRY",
        "BUILD",
        "SERVICE",
        "TRIGGER",
        "SERVICE_ROLLBACK",
        "TRIGGER_ROLLBACK",
    ]
    resource: str
    resourceUri: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "NOT_STARTED", "IN_PROGRESS", "COMPLETE"
    ]
    stateMessages: _list[GoogleCloudFunctionsV2betaStateMessage]

@typing.type_check_only
class GoogleCloudFunctionsV2betaStateMessage(typing_extensions.TypedDict, total=False):
    message: str
    severity: typing_extensions.Literal[
        "SEVERITY_UNSPECIFIED", "ERROR", "WARNING", "INFO"
    ]
    type: str

@typing.type_check_only
class ListFunctionsResponse(typing_extensions.TypedDict, total=False):
    functions: _list[Function]
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
class ListRuntimesResponse(typing_extensions.TypedDict, total=False):
    runtimes: _list[Runtime]

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
class OperationMetadataV1(typing_extensions.TypedDict, total=False):
    buildId: str
    buildName: str
    request: dict[str, typing.Any]
    sourceToken: str
    target: str
    type: typing_extensions.Literal[
        "OPERATION_UNSPECIFIED", "CREATE_FUNCTION", "UPDATE_FUNCTION", "DELETE_FUNCTION"
    ]
    updateTime: str
    versionId: str

@typing.type_check_only
class Policy(typing_extensions.TypedDict, total=False):
    auditConfigs: _list[AuditConfig]
    bindings: _list[Binding]
    etag: str
    version: int

@typing.type_check_only
class RepoSource(typing_extensions.TypedDict, total=False):
    branchName: str
    commitSha: str
    dir: str
    invertRegex: bool
    projectId: str
    repoName: str
    tagName: str

@typing.type_check_only
class Runtime(typing_extensions.TypedDict, total=False):
    displayName: str
    environment: typing_extensions.Literal["ENVIRONMENT_UNSPECIFIED", "GEN_1", "GEN_2"]
    name: str
    stage: typing_extensions.Literal[
        "RUNTIME_STAGE_UNSPECIFIED",
        "DEVELOPMENT",
        "ALPHA",
        "BETA",
        "GA",
        "DEPRECATED",
        "DECOMMISSIONED",
    ]
    warnings: _list[str]

@typing.type_check_only
class SecretEnvVar(typing_extensions.TypedDict, total=False):
    key: str
    projectId: str
    secret: str
    version: str

@typing.type_check_only
class SecretVersion(typing_extensions.TypedDict, total=False):
    path: str
    version: str

@typing.type_check_only
class SecretVolume(typing_extensions.TypedDict, total=False):
    mountPath: str
    projectId: str
    secret: str
    versions: _list[SecretVersion]

@typing.type_check_only
class ServiceConfig(typing_extensions.TypedDict, total=False):
    allTrafficOnLatestRevision: bool
    availableMemory: str
    environmentVariables: dict[str, typing.Any]
    ingressSettings: typing_extensions.Literal[
        "INGRESS_SETTINGS_UNSPECIFIED",
        "ALLOW_ALL",
        "ALLOW_INTERNAL_ONLY",
        "ALLOW_INTERNAL_AND_GCLB",
    ]
    maxInstanceCount: int
    minInstanceCount: int
    revision: str
    secretEnvironmentVariables: _list[SecretEnvVar]
    secretVolumes: _list[SecretVolume]
    service: str
    serviceAccountEmail: str
    timeoutSeconds: int
    uri: str
    vpcConnector: str
    vpcConnectorEgressSettings: typing_extensions.Literal[
        "VPC_CONNECTOR_EGRESS_SETTINGS_UNSPECIFIED",
        "PRIVATE_RANGES_ONLY",
        "ALL_TRAFFIC",
    ]

@typing.type_check_only
class SetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    policy: Policy
    updateMask: str

@typing.type_check_only
class Source(typing_extensions.TypedDict, total=False):
    repoSource: RepoSource
    storageSource: StorageSource

@typing.type_check_only
class SourceProvenance(typing_extensions.TypedDict, total=False):
    resolvedRepoSource: RepoSource
    resolvedStorageSource: StorageSource

@typing.type_check_only
class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class StorageSource(typing_extensions.TypedDict, total=False):
    bucket: str
    generation: str
    object: str

@typing.type_check_only
class TestIamPermissionsRequest(typing_extensions.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class TestIamPermissionsResponse(typing_extensions.TypedDict, total=False):
    permissions: _list[str]
