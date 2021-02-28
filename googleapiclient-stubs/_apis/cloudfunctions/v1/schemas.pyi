import typing

import typing_extensions
@typing.type_check_only
class AuditConfig(typing_extensions.TypedDict, total=False):
    auditLogConfigs: typing.List[AuditLogConfig]
    service: str

@typing.type_check_only
class AuditLogConfig(typing_extensions.TypedDict, total=False):
    exemptedMembers: typing.List[str]
    logType: typing_extensions.Literal[
        "LOG_TYPE_UNSPECIFIED", "ADMIN_READ", "DATA_WRITE", "DATA_READ"
    ]

@typing.type_check_only
class Binding(typing_extensions.TypedDict, total=False):
    condition: Expr
    members: typing.List[str]
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
    buildEnvironmentVariables: typing.Dict[str, typing.Any]
    buildId: str
    buildWorkerPool: str
    description: str
    entryPoint: str
    environmentVariables: typing.Dict[str, typing.Any]
    eventTrigger: EventTrigger
    httpsTrigger: HttpsTrigger
    ingressSettings: typing_extensions.Literal[
        "INGRESS_SETTINGS_UNSPECIFIED",
        "ALLOW_ALL",
        "ALLOW_INTERNAL_ONLY",
        "ALLOW_INTERNAL_AND_GCLB",
    ]
    labels: typing.Dict[str, typing.Any]
    maxInstances: int
    name: str
    network: str
    runtime: str
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
class GenerateUploadUrlRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class GenerateUploadUrlResponse(typing_extensions.TypedDict, total=False):
    uploadUrl: str

@typing.type_check_only
class HttpsTrigger(typing_extensions.TypedDict, total=False):
    securityLevel: typing_extensions.Literal[
        "SECURITY_LEVEL_UNSPECIFIED", "SECURE_ALWAYS", "SECURE_OPTIONAL"
    ]
    url: str

@typing.type_check_only
class ListFunctionsResponse(typing_extensions.TypedDict, total=False):
    functions: typing.List[CloudFunction]
    nextPageToken: str
    unreachable: typing.List[str]

@typing.type_check_only
class ListLocationsResponse(typing_extensions.TypedDict, total=False):
    locations: typing.List[Location]
    nextPageToken: str

@typing.type_check_only
class ListOperationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    operations: typing.List[Operation]

@typing.type_check_only
class Location(typing_extensions.TypedDict, total=False):
    displayName: str
    labels: typing.Dict[str, typing.Any]
    locationId: str
    metadata: typing.Dict[str, typing.Any]
    name: str

@typing.type_check_only
class Operation(typing_extensions.TypedDict, total=False):
    done: bool
    error: Status
    metadata: typing.Dict[str, typing.Any]
    name: str
    response: typing.Dict[str, typing.Any]

@typing.type_check_only
class OperationMetadataV1(typing_extensions.TypedDict, total=False):
    buildId: str
    request: typing.Dict[str, typing.Any]
    sourceToken: str
    target: str
    type: typing_extensions.Literal[
        "OPERATION_UNSPECIFIED", "CREATE_FUNCTION", "UPDATE_FUNCTION", "DELETE_FUNCTION"
    ]
    updateTime: str
    versionId: str

@typing.type_check_only
class Policy(typing_extensions.TypedDict, total=False):
    auditConfigs: typing.List[AuditConfig]
    bindings: typing.List[Binding]
    etag: str
    version: int

@typing.type_check_only
class Retry(typing_extensions.TypedDict, total=False): ...

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
    details: typing.List[typing.Dict[str, typing.Any]]
    message: str

@typing.type_check_only
class TestIamPermissionsRequest(typing_extensions.TypedDict, total=False):
    permissions: typing.List[str]

@typing.type_check_only
class TestIamPermissionsResponse(typing_extensions.TypedDict, total=False):
    permissions: typing.List[str]
