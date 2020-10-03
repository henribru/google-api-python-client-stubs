import typing

import typing_extensions

class DeploymentsCancelPreviewRequest(typing_extensions.TypedDict, total=False):
    fingerprint: str

class Condition(typing_extensions.TypedDict, total=False):
    iam: str
    op: str
    sys: str
    svc: str
    values: typing.List[str]

class DeploymentUpdateLabelEntry(typing_extensions.TypedDict, total=False):
    value: str
    key: str

class TypesListResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    types: typing.List[Type]

class ResourcesListResponse(typing_extensions.TypedDict, total=False):
    resources: typing.List[Resource]
    nextPageToken: str

class OperationsListResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    operations: typing.List[Operation]

class Deployment(typing_extensions.TypedDict, total=False):
    description: str
    target: TargetConfiguration
    updateTime: str
    id: str
    manifest: str
    fingerprint: str
    name: str
    update: DeploymentUpdate
    operation: Operation
    labels: typing.List[DeploymentLabelEntry]
    selfLink: str
    insertTime: str

class ResourceAccessControl(typing_extensions.TypedDict, total=False):
    gcpIamPolicy: str

class LogConfigDataAccessOptions(typing_extensions.TypedDict, total=False):
    logMode: str

class AuditLogConfig(typing_extensions.TypedDict, total=False):
    exemptedMembers: typing.List[str]
    ignoreChildExemptions: bool
    logType: str

class ConfigFile(typing_extensions.TypedDict, total=False):
    content: str

class ManifestsListResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    manifests: typing.List[Manifest]

class LogConfig(typing_extensions.TypedDict, total=False):
    dataAccess: LogConfigDataAccessOptions
    counter: LogConfigCounterOptions
    cloudAudit: LogConfigCloudAuditOptions

class LogConfigCounterOptionsCustomField(typing_extensions.TypedDict, total=False):
    value: str
    name: str

class Expr(typing_extensions.TypedDict, total=False):
    expression: str
    description: str
    location: str
    title: str

class Policy(typing_extensions.TypedDict, total=False):
    iamOwned: bool
    auditConfigs: typing.List[AuditConfig]
    version: int
    bindings: typing.List[Binding]
    rules: typing.List[Rule]
    etag: str

class Binding(typing_extensions.TypedDict, total=False):
    condition: Expr
    members: typing.List[str]
    role: str

class Manifest(typing_extensions.TypedDict, total=False):
    id: str
    name: str
    selfLink: str
    config: ConfigFile
    expandedConfig: str
    insertTime: str
    layout: str
    imports: typing.List[ImportFile]

class Resource(typing_extensions.TypedDict, total=False):
    updateTime: str
    type: str
    id: str
    finalProperties: str
    name: str
    properties: str
    manifest: str
    update: ResourceUpdate
    insertTime: str
    accessControl: ResourceAccessControl
    warnings: typing.List[typing.Dict[str, typing.Any]]
    url: str

class Rule(typing_extensions.TypedDict, total=False):
    description: str
    permissions: typing.List[str]
    ins: typing.List[str]
    conditions: typing.List[Condition]
    action: str
    logConfigs: typing.List[LogConfig]
    notIns: typing.List[str]

class Operation(typing_extensions.TypedDict, total=False):
    zone: str
    progress: int
    selfLink: str
    region: str
    name: str
    endTime: str
    targetLink: str
    startTime: str
    kind: str
    clientOperationId: str
    httpErrorMessage: str
    id: str
    httpErrorStatusCode: int
    user: str
    description: str
    operationType: str
    targetId: str
    creationTimestamp: str
    warnings: typing.List[typing.Dict[str, typing.Any]]
    error: typing.Dict[str, typing.Any]
    insertTime: str
    status: str
    statusMessage: str

class AuditConfig(typing_extensions.TypedDict, total=False):
    auditLogConfigs: typing.List[AuditLogConfig]
    service: str
    exemptedMembers: typing.List[str]

class AuthorizationLoggingOptions(typing_extensions.TypedDict, total=False):
    permissionType: str

class TestPermissionsRequest(typing_extensions.TypedDict, total=False):
    permissions: typing.List[str]

class GlobalSetPolicyRequest(typing_extensions.TypedDict, total=False):
    bindings: typing.List[Binding]
    policy: Policy
    etag: str

class TestPermissionsResponse(typing_extensions.TypedDict, total=False):
    permissions: typing.List[str]

class DeploymentsStopRequest(typing_extensions.TypedDict, total=False):
    fingerprint: str

class TargetConfiguration(typing_extensions.TypedDict, total=False):
    imports: typing.List[ImportFile]
    config: ConfigFile

class Type(typing_extensions.TypedDict, total=False):
    insertTime: str
    id: str
    operation: Operation
    name: str
    selfLink: str

class LogConfigCloudAuditOptions(typing_extensions.TypedDict, total=False):
    logName: str
    authorizationLoggingOptions: AuthorizationLoggingOptions

class LogConfigCounterOptions(typing_extensions.TypedDict, total=False):
    metric: str
    customFields: typing.List[LogConfigCounterOptionsCustomField]
    field: str

class ImportFile(typing_extensions.TypedDict, total=False):
    content: str
    name: str

class DeploymentUpdate(typing_extensions.TypedDict, total=False):
    description: str
    manifest: str
    labels: typing.List[DeploymentUpdateLabelEntry]

class DeploymentsListResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    deployments: typing.List[Deployment]

class DeploymentLabelEntry(typing_extensions.TypedDict, total=False):
    value: str
    key: str

class ResourceUpdate(typing_extensions.TypedDict, total=False):
    accessControl: ResourceAccessControl
    manifest: str
    finalProperties: str
    error: typing.Dict[str, typing.Any]
    properties: str
    intent: str
    state: str
    warnings: typing.List[typing.Dict[str, typing.Any]]
