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
class ConfigFile(typing_extensions.TypedDict, total=False):
    content: str

@typing.type_check_only
class Deployment(typing_extensions.TypedDict, total=False):
    description: str
    fingerprint: str
    id: str
    insertTime: str
    labels: typing.List[DeploymentLabelEntry]
    manifest: str
    name: str
    operation: Operation
    selfLink: str
    target: TargetConfiguration
    update: DeploymentUpdate
    updateTime: str

@typing.type_check_only
class DeploymentLabelEntry(typing_extensions.TypedDict, total=False):
    key: str
    value: str

@typing.type_check_only
class DeploymentUpdate(typing_extensions.TypedDict, total=False):
    description: str
    labels: typing.List[DeploymentUpdateLabelEntry]
    manifest: str

@typing.type_check_only
class DeploymentUpdateLabelEntry(typing_extensions.TypedDict, total=False):
    key: str
    value: str

@typing.type_check_only
class DeploymentsCancelPreviewRequest(typing_extensions.TypedDict, total=False):
    fingerprint: str

@typing.type_check_only
class DeploymentsListResponse(typing_extensions.TypedDict, total=False):
    deployments: typing.List[Deployment]
    nextPageToken: str

@typing.type_check_only
class DeploymentsStopRequest(typing_extensions.TypedDict, total=False):
    fingerprint: str

@typing.type_check_only
class Expr(typing_extensions.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str

@typing.type_check_only
class GlobalSetPolicyRequest(typing_extensions.TypedDict, total=False):
    bindings: typing.List[Binding]
    etag: str
    policy: Policy

@typing.type_check_only
class ImportFile(typing_extensions.TypedDict, total=False):
    content: str
    name: str

@typing.type_check_only
class Manifest(typing_extensions.TypedDict, total=False):
    config: ConfigFile
    expandedConfig: str
    id: str
    imports: typing.List[ImportFile]
    insertTime: str
    layout: str
    manifestSizeBytes: str
    manifestSizeLimitBytes: str
    name: str
    selfLink: str

@typing.type_check_only
class ManifestsListResponse(typing_extensions.TypedDict, total=False):
    manifests: typing.List[Manifest]
    nextPageToken: str

@typing.type_check_only
class Operation(typing_extensions.TypedDict, total=False):
    clientOperationId: str
    creationTimestamp: str
    description: str
    endTime: str
    error: typing.Dict[str, typing.Any]
    httpErrorMessage: str
    httpErrorStatusCode: int
    id: str
    insertTime: str
    kind: str
    name: str
    operationGroupId: str
    operationType: str
    progress: int
    region: str
    selfLink: str
    startTime: str
    status: typing_extensions.Literal["PENDING", "RUNNING", "DONE"]
    statusMessage: str
    targetId: str
    targetLink: str
    user: str
    warnings: typing.List[typing.Dict[str, typing.Any]]
    zone: str

@typing.type_check_only
class OperationsListResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    operations: typing.List[Operation]

@typing.type_check_only
class Policy(typing_extensions.TypedDict, total=False):
    auditConfigs: typing.List[AuditConfig]
    bindings: typing.List[Binding]
    etag: str
    version: int

@typing.type_check_only
class Resource(typing_extensions.TypedDict, total=False):
    accessControl: ResourceAccessControl
    finalProperties: str
    id: str
    insertTime: str
    manifest: str
    name: str
    properties: str
    type: str
    update: ResourceUpdate
    updateTime: str
    url: str
    warnings: typing.List[typing.Dict[str, typing.Any]]

@typing.type_check_only
class ResourceAccessControl(typing_extensions.TypedDict, total=False):
    gcpIamPolicy: str

@typing.type_check_only
class ResourceUpdate(typing_extensions.TypedDict, total=False):
    accessControl: ResourceAccessControl
    error: typing.Dict[str, typing.Any]
    finalProperties: str
    intent: typing_extensions.Literal[
        "CREATE_OR_ACQUIRE", "DELETE", "ACQUIRE", "UPDATE", "ABANDON", "CREATE"
    ]
    manifest: str
    properties: str
    state: typing_extensions.Literal[
        "PENDING", "IN_PROGRESS", "IN_PREVIEW", "FAILED", "ABORTED"
    ]
    warnings: typing.List[typing.Dict[str, typing.Any]]

@typing.type_check_only
class ResourcesListResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    resources: typing.List[Resource]

@typing.type_check_only
class TargetConfiguration(typing_extensions.TypedDict, total=False):
    config: ConfigFile
    imports: typing.List[ImportFile]

@typing.type_check_only
class TestPermissionsRequest(typing_extensions.TypedDict, total=False):
    permissions: typing.List[str]

@typing.type_check_only
class TestPermissionsResponse(typing_extensions.TypedDict, total=False):
    permissions: typing.List[str]

@typing.type_check_only
class Type(typing_extensions.TypedDict, total=False):
    id: str
    insertTime: str
    name: str
    operation: Operation
    selfLink: str

@typing.type_check_only
class TypesListResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    types: typing.List[Type]
