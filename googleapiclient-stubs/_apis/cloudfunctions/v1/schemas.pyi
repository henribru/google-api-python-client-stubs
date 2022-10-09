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
class CallFunctionRequest(typing_extensions.TypedDict, total=False):
    data: str

@typing.type_check_only
class CallFunctionResponse(typing_extensions.TypedDict, total=False):
    error: str
    executionId: str
    result: str

@typing.type_check_only
class CloudFunction(typing_extensions.TypedDict, total=False):
    availableMemoryMb: int
    buildEnvironmentVariables: dict[str, typing.Any]
    buildId: str
    buildName: str
    buildWorkerPool: str
    description: str
    dockerRegistry: typing_extensions.Literal[
        "DOCKER_REGISTRY_UNSPECIFIED", "CONTAINER_REGISTRY", "ARTIFACT_REGISTRY"
    ]
    dockerRepository: str
    entryPoint: str
    environmentVariables: dict[str, typing.Any]
    eventTrigger: EventTrigger
    httpsTrigger: HttpsTrigger
    ingressSettings: typing_extensions.Literal[
        "INGRESS_SETTINGS_UNSPECIFIED",
        "ALLOW_ALL",
        "ALLOW_INTERNAL_ONLY",
        "ALLOW_INTERNAL_AND_GCLB",
    ]
    kmsKeyName: str
    labels: dict[str, typing.Any]
    maxInstances: int
    minInstances: int
    name: str
    network: str
    runtime: str
    secretEnvironmentVariables: _list[SecretEnvVar]
    secretVolumes: _list[SecretVolume]
    serviceAccountEmail: str
    sourceArchiveUrl: str
    sourceRepository: SourceRepository
    sourceToken: str
    sourceUploadUrl: str
    status: typing_extensions.Literal[
        "CLOUD_FUNCTION_STATUS_UNSPECIFIED",
        "ACTIVE",
        "OFFLINE",
        "DEPLOY_IN_PROGRESS",
        "DELETE_IN_PROGRESS",
        "UNKNOWN",
    ]
    timeout: str
    updateTime: str
    versionId: str
    vpcConnector: str
    vpcConnectorEgressSettings: typing_extensions.Literal[
        "VPC_CONNECTOR_EGRESS_SETTINGS_UNSPECIFIED",
        "PRIVATE_RANGES_ONLY",
        "ALL_TRAFFIC",
    ]

@typing.type_check_only
class EventTrigger(typing_extensions.TypedDict, total=False):
    eventType: str
    failurePolicy: FailurePolicy
    resource: str
    service: str

@typing.type_check_only
class Expr(typing_extensions.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str

@typing.type_check_only
class FailurePolicy(typing_extensions.TypedDict, total=False):
    retry: Retry

@typing.type_check_only
class GenerateDownloadUrlRequest(typing_extensions.TypedDict, total=False):
    versionId: str

@typing.type_check_only
class GenerateDownloadUrlResponse(typing_extensions.TypedDict, total=False):
    downloadUrl: str

@typing.type_check_only
class GenerateUploadUrlRequest(typing_extensions.TypedDict, total=False):
    kmsKeyName: str

@typing.type_check_only
class GenerateUploadUrlResponse(typing_extensions.TypedDict, total=False):
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
class HttpsTrigger(typing_extensions.TypedDict, total=False):
    securityLevel: typing_extensions.Literal[
        "SECURITY_LEVEL_UNSPECIFIED", "SECURE_ALWAYS", "SECURE_OPTIONAL"
    ]
    url: str

@typing.type_check_only
class ListFunctionsResponse(typing_extensions.TypedDict, total=False):
    functions: _list[CloudFunction]
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
class Retry(typing_extensions.TypedDict, total=False): ...

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
class SetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    policy: Policy
    updateMask: str

@typing.type_check_only
class SourceRepository(typing_extensions.TypedDict, total=False):
    deployedUrl: str
    url: str

@typing.type_check_only
class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class TestIamPermissionsRequest(typing_extensions.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class TestIamPermissionsResponse(typing_extensions.TypedDict, total=False):
    permissions: _list[str]
