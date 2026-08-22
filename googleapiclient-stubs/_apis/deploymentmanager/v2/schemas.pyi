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
class Binding(typing.TypedDict, total=False):
    condition: Expr
    members: _list[str]
    role: str

@typing.type_check_only
class BulkInsertOperationStatus(typing.TypedDict, total=False):
    createdVmCount: int
    deletedVmCount: int
    failedToCreateVmCount: int
    status: typing.Literal["STATUS_UNSPECIFIED", "CREATING", "ROLLING_BACK", "DONE"]
    targetVmCount: int

@typing.type_check_only
class ConfigFile(typing.TypedDict, total=False):
    content: str

@typing.type_check_only
class DebugInfo(typing.TypedDict, total=False):
    detail: str
    stackEntries: _list[str]

@typing.type_check_only
class Deployment(typing.TypedDict, total=False):
    description: str
    fingerprint: str
    id: str
    insertTime: str
    labels: _list[DeploymentLabelEntry]
    manifest: str
    name: str
    operation: Operation
    selfLink: str
    target: TargetConfiguration
    update: DeploymentUpdate
    updateTime: str

@typing.type_check_only
class DeploymentLabelEntry(typing.TypedDict, total=False):
    key: str
    value: str

@typing.type_check_only
class DeploymentUpdate(typing.TypedDict, total=False):
    description: str
    labels: _list[DeploymentUpdateLabelEntry]
    manifest: str

@typing.type_check_only
class DeploymentUpdateLabelEntry(typing.TypedDict, total=False):
    key: str
    value: str

@typing.type_check_only
class DeploymentsCancelPreviewRequest(typing.TypedDict, total=False):
    fingerprint: str

@typing.type_check_only
class DeploymentsListResponse(typing.TypedDict, total=False):
    deployments: _list[Deployment]
    nextPageToken: str

@typing.type_check_only
class DeploymentsStopRequest(typing.TypedDict, total=False):
    fingerprint: str

@typing.type_check_only
class ErrorInfo(typing.TypedDict, total=False):
    domain: str
    metadatas: dict[str, typing.Any]
    reason: str

@typing.type_check_only
class Expr(typing.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str

@typing.type_check_only
class FirewallPolicyRuleOperationMetadata(typing.TypedDict, total=False):
    allocatedPriority: int

@typing.type_check_only
class GetVersionOperationMetadata(typing.TypedDict, total=False):
    inlineSbomInfo: GetVersionOperationMetadataSbomInfo

@typing.type_check_only
class GetVersionOperationMetadataSbomInfo(typing.TypedDict, total=False):
    currentComponentVersions: dict[str, typing.Any]
    targetComponentVersions: dict[str, typing.Any]

@typing.type_check_only
class GlobalSetPolicyRequest(typing.TypedDict, total=False):
    bindings: _list[Binding]
    etag: str
    policy: Policy
    updateMask: str

@typing.type_check_only
class Help(typing.TypedDict, total=False):
    links: _list[HelpLink]

@typing.type_check_only
class HelpLink(typing.TypedDict, total=False):
    description: str
    url: str

@typing.type_check_only
class ImportFile(typing.TypedDict, total=False):
    content: str
    name: str

@typing.type_check_only
class InstancesBulkInsertOperationMetadata(typing.TypedDict, total=False):
    machineType: str
    perLocationStatus: dict[str, typing.Any]

@typing.type_check_only
class LocalizedMessage(typing.TypedDict, total=False):
    locale: str
    message: str

@typing.type_check_only
class Manifest(typing.TypedDict, total=False):
    config: ConfigFile
    expandedConfig: str
    id: str
    imports: _list[ImportFile]
    insertTime: str
    layout: str
    manifestSizeBytes: str
    manifestSizeLimitBytes: str
    name: str
    selfLink: str

@typing.type_check_only
class ManifestsListResponse(typing.TypedDict, total=False):
    manifests: _list[Manifest]
    nextPageToken: str

@typing.type_check_only
class Operation(typing.TypedDict, total=False):
    clientOperationId: str
    creationTimestamp: str
    description: str
    endTime: str
    error: dict[str, typing.Any]
    firewallPolicyRuleOperationMetadata: FirewallPolicyRuleOperationMetadata
    getVersionOperationMetadata: GetVersionOperationMetadata
    httpErrorMessage: str
    httpErrorStatusCode: int
    id: str
    insertTime: str
    instancesBulkInsertOperationMetadata: InstancesBulkInsertOperationMetadata
    kind: str
    name: str
    operationGroupId: str
    operationType: str
    progress: int
    region: str
    selfLink: str
    selfLinkWithId: str
    setAutoscalerLinkOperationMetadata: SetAutoscalerLinkOperationMetadata
    setCommonInstanceMetadataOperationMetadata: (
        SetCommonInstanceMetadataOperationMetadata
    )
    startTime: str
    status: typing.Literal["PENDING", "RUNNING", "DONE"]
    statusMessage: str
    targetId: str
    targetLink: str
    user: str
    warnings: _list[dict[str, typing.Any]]
    zone: str

@typing.type_check_only
class OperationsListResponse(typing.TypedDict, total=False):
    nextPageToken: str
    operations: _list[Operation]

@typing.type_check_only
class Policy(typing.TypedDict, total=False):
    auditConfigs: _list[AuditConfig]
    bindings: _list[Binding]
    etag: str
    version: int

@typing.type_check_only
class QuotaExceededInfo(typing.TypedDict, total=False):
    dimensions: dict[str, typing.Any]
    futureLimit: float
    limit: float
    limitName: str
    metricName: str
    rolloutStatus: typing.Literal["ROLLOUT_STATUS_UNSPECIFIED", "IN_PROGRESS"]

@typing.type_check_only
class Resource(typing.TypedDict, total=False):
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
    warnings: _list[dict[str, typing.Any]]

@typing.type_check_only
class ResourceAccessControl(typing.TypedDict, total=False):
    gcpIamPolicy: str

@typing.type_check_only
class ResourceUpdate(typing.TypedDict, total=False):
    accessControl: ResourceAccessControl
    error: dict[str, typing.Any]
    finalProperties: str
    intent: typing.Literal[
        "CREATE_OR_ACQUIRE", "DELETE", "ACQUIRE", "UPDATE", "ABANDON", "CREATE"
    ]
    manifest: str
    properties: str
    state: typing.Literal["PENDING", "IN_PROGRESS", "IN_PREVIEW", "FAILED", "ABORTED"]
    warnings: _list[dict[str, typing.Any]]

@typing.type_check_only
class ResourcesListResponse(typing.TypedDict, total=False):
    nextPageToken: str
    resources: _list[Resource]

@typing.type_check_only
class SetAutoscalerLinkOperationMetadata(typing.TypedDict, total=False):
    zonalIgmIds: _list[str]
    zoneToIgmIds: dict[str, typing.Any]

@typing.type_check_only
class SetCommonInstanceMetadataOperationMetadata(typing.TypedDict, total=False):
    clientOperationId: str
    perLocationOperations: dict[str, typing.Any]

@typing.type_check_only
class SetCommonInstanceMetadataOperationMetadataPerLocationOperationInfo(
    typing.TypedDict, total=False
):
    error: Status
    state: typing.Literal[
        "UNSPECIFIED", "PROPAGATING", "PROPAGATED", "ABANDONED", "FAILED", "DONE"
    ]

@typing.type_check_only
class Status(typing.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class TargetConfiguration(typing.TypedDict, total=False):
    config: ConfigFile
    imports: _list[ImportFile]

@typing.type_check_only
class TestPermissionsRequest(typing.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class TestPermissionsResponse(typing.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class Type(typing.TypedDict, total=False):
    id: str
    insertTime: str
    name: str
    operation: Operation
    selfLink: str

@typing.type_check_only
class TypesListResponse(typing.TypedDict, total=False):
    nextPageToken: str
    types: _list[Type]
