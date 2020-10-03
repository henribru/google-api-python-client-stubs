import typing

import typing_extensions

class Operation(typing_extensions.TypedDict, total=False):
    response: typing.Dict[str, typing.Any]
    name: str
    done: bool
    error: Status
    metadata: typing.Dict[str, typing.Any]

class Retry(typing_extensions.TypedDict, total=False): ...

class GenerateUploadUrlResponse(typing_extensions.TypedDict, total=False):
    uploadUrl: str

class Policy(typing_extensions.TypedDict, total=False):
    bindings: typing.List[Binding]
    etag: str
    auditConfigs: typing.List[AuditConfig]
    version: int

class GenerateUploadUrlRequest(typing_extensions.TypedDict, total=False): ...

class Binding(typing_extensions.TypedDict, total=False):
    role: str
    condition: Expr
    members: typing.List[str]

class TestIamPermissionsRequest(typing_extensions.TypedDict, total=False):
    permissions: typing.List[str]

class AuditConfig(typing_extensions.TypedDict, total=False):
    service: str
    auditLogConfigs: typing.List[AuditLogConfig]

class FailurePolicy(typing_extensions.TypedDict, total=False):
    retry: Retry

class ListOperationsResponse(typing_extensions.TypedDict, total=False):
    operations: typing.List[Operation]
    nextPageToken: str

class SourceRepository(typing_extensions.TypedDict, total=False):
    deployedUrl: str
    url: str

class HttpsTrigger(typing_extensions.TypedDict, total=False):
    url: str

class CallFunctionRequest(typing_extensions.TypedDict, total=False):
    data: str

class ListLocationsResponse(typing_extensions.TypedDict, total=False):
    locations: typing.List[Location]
    nextPageToken: str

class OperationMetadataV1(typing_extensions.TypedDict, total=False):
    target: str
    buildId: str
    updateTime: str
    versionId: str
    type: typing_extensions.Literal[
        "OPERATION_UNSPECIFIED", "CREATE_FUNCTION", "UPDATE_FUNCTION", "DELETE_FUNCTION"
    ]
    request: typing.Dict[str, typing.Any]

class Expr(typing_extensions.TypedDict, total=False):
    location: str
    title: str
    description: str
    expression: str

class Location(typing_extensions.TypedDict, total=False):
    labels: typing.Dict[str, typing.Any]
    displayName: str
    metadata: typing.Dict[str, typing.Any]
    name: str
    locationId: str

class ListFunctionsResponse(typing_extensions.TypedDict, total=False):
    unreachable: typing.List[str]
    nextPageToken: str
    functions: typing.List[CloudFunction]

class TestIamPermissionsResponse(typing_extensions.TypedDict, total=False):
    permissions: typing.List[str]

class EventTrigger(typing_extensions.TypedDict, total=False):
    failurePolicy: FailurePolicy
    resource: str
    service: str
    eventType: str

class GenerateDownloadUrlResponse(typing_extensions.TypedDict, total=False):
    downloadUrl: str

class AuditLogConfig(typing_extensions.TypedDict, total=False):
    logType: typing_extensions.Literal[
        "LOG_TYPE_UNSPECIFIED", "ADMIN_READ", "DATA_WRITE", "DATA_READ"
    ]
    exemptedMembers: typing.List[str]

class SetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    updateMask: str
    policy: Policy

class GenerateDownloadUrlRequest(typing_extensions.TypedDict, total=False):
    versionId: str

class Status(typing_extensions.TypedDict, total=False):
    details: typing.List[typing.Dict[str, typing.Any]]
    code: int
    message: str

class CloudFunction(typing_extensions.TypedDict, total=False):
    runtime: str
    buildId: str
    availableMemoryMb: int
    entryPoint: str
    updateTime: str
    serviceAccountEmail: str
    eventTrigger: EventTrigger
    vpcConnector: str
    buildEnvironmentVariables: typing.Dict[str, typing.Any]
    sourceRepository: SourceRepository
    ingressSettings: typing_extensions.Literal[
        "INGRESS_SETTINGS_UNSPECIFIED",
        "ALLOW_ALL",
        "ALLOW_INTERNAL_ONLY",
        "ALLOW_INTERNAL_AND_GCLB",
    ]
    sourceUploadUrl: str
    network: str
    maxInstances: int
    status: typing_extensions.Literal[
        "CLOUD_FUNCTION_STATUS_UNSPECIFIED",
        "ACTIVE",
        "OFFLINE",
        "DEPLOY_IN_PROGRESS",
        "DELETE_IN_PROGRESS",
        "UNKNOWN",
    ]
    timeout: str
    description: str
    sourceArchiveUrl: str
    labels: typing.Dict[str, typing.Any]
    httpsTrigger: HttpsTrigger
    vpcConnectorEgressSettings: typing_extensions.Literal[
        "VPC_CONNECTOR_EGRESS_SETTINGS_UNSPECIFIED",
        "PRIVATE_RANGES_ONLY",
        "ALL_TRAFFIC",
    ]
    environmentVariables: typing.Dict[str, typing.Any]
    name: str
    versionId: str

class CallFunctionResponse(typing_extensions.TypedDict, total=False):
    executionId: str
    error: str
    result: str
