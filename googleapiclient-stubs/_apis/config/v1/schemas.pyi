import typing

_list = list

@typing.type_check_only
class ApplyResults(typing.TypedDict, total=False):
    artifacts: str
    content: str
    outputs: dict[str, typing.Any]

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
class AutoMigrationConfig(typing.TypedDict, total=False):
    autoMigrationEnabled: bool
    name: str
    updateTime: str

@typing.type_check_only
class Binding(typing.TypedDict, total=False):
    condition: Expr
    members: _list[str]
    role: str

@typing.type_check_only
class CancelOperationRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class DeleteStatefileRequest(typing.TypedDict, total=False):
    lockId: str

@typing.type_check_only
class Deployment(typing.TypedDict, total=False):
    annotations: dict[str, typing.Any]
    artifactsGcsBucket: str
    createTime: str
    deleteBuild: str
    deleteLogs: str
    deleteResults: ApplyResults
    errorCode: typing.Literal[
        "ERROR_CODE_UNSPECIFIED",
        "REVISION_FAILED",
        "CLOUD_BUILD_PERMISSION_DENIED",
        "DELETE_BUILD_API_FAILED",
        "DELETE_BUILD_RUN_FAILED",
        "BUCKET_CREATION_PERMISSION_DENIED",
        "BUCKET_CREATION_FAILED",
        "EXTERNAL_VALUE_SOURCE_IMPORT_FAILED",
    ]
    errorLogs: str
    importExistingResources: bool
    labels: dict[str, typing.Any]
    latestRevision: str
    lockState: typing.Literal[
        "LOCK_STATE_UNSPECIFIED",
        "LOCKED",
        "UNLOCKED",
        "LOCKING",
        "UNLOCKING",
        "LOCK_FAILED",
        "UNLOCK_FAILED",
    ]
    name: str
    providerConfig: ProviderConfig
    quotaValidation: typing.Literal[
        "QUOTA_VALIDATION_UNSPECIFIED", "ENABLED", "ENFORCED"
    ]
    serviceAccount: str
    state: typing.Literal[
        "STATE_UNSPECIFIED",
        "CREATING",
        "ACTIVE",
        "UPDATING",
        "DELETING",
        "FAILED",
        "SUSPENDED",
        "DELETED",
    ]
    stateDetail: str
    terraformBlueprint: TerraformBlueprint
    tfErrors: _list[TerraformError]
    tfVersion: str
    tfVersionConstraint: str
    updateTime: str
    workerPool: str

@typing.type_check_only
class DeploymentGroup(typing.TypedDict, total=False):
    annotations: dict[str, typing.Any]
    createTime: str
    deploymentUnits: _list[DeploymentUnit]
    labels: dict[str, typing.Any]
    name: str
    provisioningError: Status
    provisioningState: typing.Literal[
        "PROVISIONING_STATE_UNSPECIFIED",
        "PROVISIONING",
        "PROVISIONED",
        "FAILED_TO_PROVISION",
        "DEPROVISIONING",
        "DEPROVISIONED",
        "FAILED_TO_DEPROVISION",
    ]
    provisioningStateDescription: str
    state: typing.Literal[
        "STATE_UNSPECIFIED",
        "CREATING",
        "ACTIVE",
        "UPDATING",
        "DELETING",
        "FAILED",
        "SUSPENDED",
        "DELETED",
    ]
    stateDescription: str
    updateTime: str

@typing.type_check_only
class DeploymentGroupRevision(typing.TypedDict, total=False):
    alternativeIds: _list[str]
    createTime: str
    name: str
    snapshot: DeploymentGroup

@typing.type_check_only
class DeploymentOperationMetadata(typing.TypedDict, total=False):
    applyResults: ApplyResults
    applyResultsAvailable: bool
    build: str
    logs: str
    step: typing.Literal[
        "DEPLOYMENT_STEP_UNSPECIFIED",
        "PREPARING_STORAGE_BUCKET",
        "DOWNLOADING_BLUEPRINT",
        "RUNNING_TF_INIT",
        "RUNNING_TF_PLAN",
        "RUNNING_TF_APPLY",
        "RUNNING_TF_DESTROY",
        "RUNNING_TF_VALIDATE",
        "UNLOCKING_DEPLOYMENT",
        "SUCCEEDED",
        "FAILED",
        "VALIDATING_REPOSITORY",
        "RUNNING_QUOTA_VALIDATION",
    ]

@typing.type_check_only
class DeploymentOperationSummary(typing.TypedDict, total=False):
    artifacts: str
    build: str
    content: str
    deploymentStep: typing.Literal[
        "DEPLOYMENT_STEP_UNSPECIFIED",
        "PREPARING_STORAGE_BUCKET",
        "DOWNLOADING_BLUEPRINT",
        "RUNNING_TF_INIT",
        "RUNNING_TF_PLAN",
        "RUNNING_TF_APPLY",
        "RUNNING_TF_DESTROY",
        "RUNNING_TF_VALIDATE",
        "UNLOCKING_DEPLOYMENT",
        "SUCCEEDED",
        "FAILED",
        "VALIDATING_REPOSITORY",
        "RUNNING_QUOTA_VALIDATION",
    ]
    logs: str

@typing.type_check_only
class DeploymentSource(typing.TypedDict, total=False):
    deployment: str
    outputName: str

@typing.type_check_only
class DeploymentSpec(typing.TypedDict, total=False):
    deployment: Deployment
    deploymentId: str

@typing.type_check_only
class DeploymentUnit(typing.TypedDict, total=False):
    dependencies: _list[str]
    deployment: str
    id: str

@typing.type_check_only
class DeploymentUnitProgress(typing.TypedDict, total=False):
    deployment: str
    deploymentOperationSummary: DeploymentOperationSummary
    error: Status
    intent: typing.Literal[
        "INTENT_UNSPECIFIED",
        "CREATE_DEPLOYMENT",
        "UPDATE_DEPLOYMENT",
        "DELETE_DEPLOYMENT",
        "RECREATE_DEPLOYMENT",
        "CLEAN_UP",
        "UNCHANGED",
    ]
    state: typing.Literal[
        "STATE_UNSPECIFIED",
        "QUEUED",
        "APPLYING_DEPLOYMENT",
        "SUCCEEDED",
        "FAILED",
        "ABORTED",
        "SKIPPED",
        "DELETING_DEPLOYMENT",
        "PREVIEWING_DEPLOYMENT",
    ]
    stateDescription: str
    unitId: str

@typing.type_check_only
class DeprovisionDeploymentGroupRequest(typing.TypedDict, total=False):
    deletePolicy: typing.Literal["DELETE_POLICY_UNSPECIFIED", "DELETE", "ABANDON"]
    force: bool

@typing.type_check_only
class Empty(typing.TypedDict, total=False): ...

@typing.type_check_only
class ExportDeploymentStatefileRequest(typing.TypedDict, total=False):
    draft: bool

@typing.type_check_only
class ExportPreviewResultRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class ExportPreviewResultResponse(typing.TypedDict, total=False):
    result: PreviewResult

@typing.type_check_only
class ExportRevisionStatefileRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class Expr(typing.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str

@typing.type_check_only
class ExternalValueSource(typing.TypedDict, total=False):
    deploymentSource: DeploymentSource

@typing.type_check_only
class GitSource(typing.TypedDict, total=False):
    directory: str
    ref: str
    repo: str

@typing.type_check_only
class ImportStatefileRequest(typing.TypedDict, total=False):
    lockId: str

@typing.type_check_only
class ListDeploymentGroupRevisionsResponse(typing.TypedDict, total=False):
    deploymentGroupRevisions: _list[DeploymentGroupRevision]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListDeploymentGroupsResponse(typing.TypedDict, total=False):
    deploymentGroups: _list[DeploymentGroup]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListDeploymentsResponse(typing.TypedDict, total=False):
    deployments: _list[Deployment]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListLocationsResponse(typing.TypedDict, total=False):
    locations: _list[Location]
    nextPageToken: str

@typing.type_check_only
class ListOperationsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    operations: _list[Operation]
    unreachable: _list[str]

@typing.type_check_only
class ListPreviewsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    previews: _list[Preview]
    unreachable: _list[str]

@typing.type_check_only
class ListResourceChangesResponse(typing.TypedDict, total=False):
    nextPageToken: str
    resourceChanges: _list[ResourceChange]
    unreachable: _list[str]

@typing.type_check_only
class ListResourceDriftsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    resourceDrifts: _list[ResourceDrift]
    unreachable: _list[str]

@typing.type_check_only
class ListResourcesResponse(typing.TypedDict, total=False):
    nextPageToken: str
    resources: _list[Resource]
    unreachable: _list[str]

@typing.type_check_only
class ListRevisionsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    revisions: _list[Revision]
    unreachable: _list[str]

@typing.type_check_only
class ListTerraformVersionsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    terraformVersions: _list[TerraformVersion]
    unreachable: _list[str]

@typing.type_check_only
class Location(typing.TypedDict, total=False):
    displayName: str
    labels: dict[str, typing.Any]
    locationId: str
    metadata: dict[str, typing.Any]
    name: str

@typing.type_check_only
class LockDeploymentRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class LockInfo(typing.TypedDict, total=False):
    createTime: str
    info: str
    lockId: str
    operation: str
    version: str
    who: str

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
    createTime: str
    deploymentMetadata: DeploymentOperationMetadata
    endTime: str
    previewMetadata: PreviewOperationMetadata
    provisionDeploymentGroupMetadata: ProvisionDeploymentGroupOperationMetadata
    requestedCancellation: bool
    statusMessage: str
    target: str
    verb: str

@typing.type_check_only
class Policy(typing.TypedDict, total=False):
    auditConfigs: _list[AuditConfig]
    bindings: _list[Binding]
    etag: str
    version: int

@typing.type_check_only
class Preview(typing.TypedDict, total=False):
    annotations: dict[str, typing.Any]
    artifactsGcsBucket: str
    build: str
    createTime: str
    deployment: str
    errorCode: typing.Literal[
        "ERROR_CODE_UNSPECIFIED",
        "CLOUD_BUILD_PERMISSION_DENIED",
        "BUCKET_CREATION_PERMISSION_DENIED",
        "BUCKET_CREATION_FAILED",
        "DEPLOYMENT_LOCK_ACQUIRE_FAILED",
        "PREVIEW_BUILD_API_FAILED",
        "PREVIEW_BUILD_RUN_FAILED",
        "EXTERNAL_VALUE_SOURCE_IMPORT_FAILED",
    ]
    errorLogs: str
    errorStatus: Status
    labels: dict[str, typing.Any]
    logs: str
    name: str
    previewArtifacts: PreviewArtifacts
    previewMode: typing.Literal["PREVIEW_MODE_UNSPECIFIED", "DEFAULT", "DELETE"]
    providerConfig: ProviderConfig
    serviceAccount: str
    state: typing.Literal[
        "STATE_UNSPECIFIED",
        "CREATING",
        "SUCCEEDED",
        "APPLYING",
        "STALE",
        "DELETING",
        "FAILED",
        "DELETED",
    ]
    terraformBlueprint: TerraformBlueprint
    tfErrors: _list[TerraformError]
    tfVersion: str
    tfVersionConstraint: str
    workerPool: str

@typing.type_check_only
class PreviewArtifacts(typing.TypedDict, total=False):
    artifacts: str
    content: str

@typing.type_check_only
class PreviewOperationMetadata(typing.TypedDict, total=False):
    build: str
    logs: str
    previewArtifacts: PreviewArtifacts
    step: typing.Literal[
        "PREVIEW_STEP_UNSPECIFIED",
        "PREPARING_STORAGE_BUCKET",
        "DOWNLOADING_BLUEPRINT",
        "RUNNING_TF_INIT",
        "RUNNING_TF_PLAN",
        "FETCHING_DEPLOYMENT",
        "LOCKING_DEPLOYMENT",
        "UNLOCKING_DEPLOYMENT",
        "SUCCEEDED",
        "FAILED",
        "VALIDATING_REPOSITORY",
    ]

@typing.type_check_only
class PreviewResult(typing.TypedDict, total=False):
    binarySignedUri: str
    jsonSignedUri: str

@typing.type_check_only
class PropertyChange(typing.TypedDict, total=False):
    after: typing.Any
    afterSensitivePaths: _list[str]
    before: typing.Any
    beforeSensitivePaths: _list[str]
    path: str

@typing.type_check_only
class PropertyDrift(typing.TypedDict, total=False):
    after: typing.Any
    afterSensitivePaths: _list[str]
    before: typing.Any
    beforeSensitivePaths: _list[str]
    path: str

@typing.type_check_only
class ProviderConfig(typing.TypedDict, total=False):
    sourceType: typing.Literal["PROVIDER_SOURCE_UNSPECIFIED", "SERVICE_MAINTAINED"]

@typing.type_check_only
class ProvisionDeploymentGroupOperationMetadata(typing.TypedDict, total=False):
    deploymentUnitProgresses: _list[DeploymentUnitProgress]
    step: typing.Literal[
        "PROVISION_DEPLOYMENT_GROUP_STEP_UNSPECIFIED",
        "VALIDATING_DEPLOYMENT_GROUP",
        "ASSOCIATING_DEPLOYMENTS_TO_DEPLOYMENT_GROUP",
        "PROVISIONING_DEPLOYMENT_UNITS",
        "DISASSOCIATING_DEPLOYMENTS_FROM_DEPLOYMENT_GROUP",
        "SUCCEEDED",
        "FAILED",
        "DEPROVISIONING_DEPLOYMENT_UNITS",
    ]

@typing.type_check_only
class ProvisionDeploymentGroupRequest(typing.TypedDict, total=False):
    deploymentSpecs: dict[str, typing.Any]

@typing.type_check_only
class Resource(typing.TypedDict, total=False):
    caiAssets: dict[str, typing.Any]
    intent: typing.Literal[
        "INTENT_UNSPECIFIED", "CREATE", "UPDATE", "DELETE", "RECREATE", "UNCHANGED"
    ]
    name: str
    state: typing.Literal[
        "STATE_UNSPECIFIED", "PLANNED", "IN_PROGRESS", "RECONCILED", "FAILED"
    ]
    terraformInfo: ResourceTerraformInfo

@typing.type_check_only
class ResourceCAIInfo(typing.TypedDict, total=False):
    fullResourceName: str

@typing.type_check_only
class ResourceChange(typing.TypedDict, total=False):
    intent: typing.Literal[
        "INTENT_UNSPECIFIED", "CREATE", "UPDATE", "DELETE", "RECREATE", "UNCHANGED"
    ]
    name: str
    propertyChanges: _list[PropertyChange]
    terraformInfo: ResourceChangeTerraformInfo

@typing.type_check_only
class ResourceChangeTerraformInfo(typing.TypedDict, total=False):
    actions: _list[str]
    address: str
    provider: str
    resourceName: str
    type: str

@typing.type_check_only
class ResourceDrift(typing.TypedDict, total=False):
    name: str
    propertyDrifts: _list[PropertyDrift]
    terraformInfo: ResourceDriftTerraformInfo

@typing.type_check_only
class ResourceDriftTerraformInfo(typing.TypedDict, total=False):
    address: str
    provider: str
    resourceName: str
    type: str

@typing.type_check_only
class ResourceTerraformInfo(typing.TypedDict, total=False):
    address: str
    id: str
    type: str

@typing.type_check_only
class Revision(typing.TypedDict, total=False):
    action: typing.Literal["ACTION_UNSPECIFIED", "CREATE", "UPDATE", "DELETE"]
    applyResults: ApplyResults
    build: str
    createTime: str
    errorCode: typing.Literal[
        "ERROR_CODE_UNSPECIFIED",
        "CLOUD_BUILD_PERMISSION_DENIED",
        "APPLY_BUILD_API_FAILED",
        "APPLY_BUILD_RUN_FAILED",
        "QUOTA_VALIDATION_FAILED",
        "EXTERNAL_VALUE_SOURCE_IMPORT_FAILED",
    ]
    errorLogs: str
    importExistingResources: bool
    logs: str
    name: str
    providerConfig: ProviderConfig
    quotaValidation: typing.Literal[
        "QUOTA_VALIDATION_UNSPECIFIED", "ENABLED", "ENFORCED"
    ]
    quotaValidationResults: str
    serviceAccount: str
    state: typing.Literal["STATE_UNSPECIFIED", "APPLYING", "APPLIED", "FAILED"]
    stateDetail: str
    terraformBlueprint: TerraformBlueprint
    tfErrors: _list[TerraformError]
    tfVersion: str
    tfVersionConstraint: str
    updateTime: str
    workerPool: str

@typing.type_check_only
class SetIamPolicyRequest(typing.TypedDict, total=False):
    policy: Policy
    updateMask: str

@typing.type_check_only
class Statefile(typing.TypedDict, total=False):
    signedUri: str

@typing.type_check_only
class Status(typing.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class TerraformBlueprint(typing.TypedDict, total=False):
    externalValues: dict[str, typing.Any]
    gcsSource: str
    gitSource: GitSource
    inputValues: dict[str, typing.Any]

@typing.type_check_only
class TerraformError(typing.TypedDict, total=False):
    error: Status
    errorDescription: str
    httpResponseCode: int
    resourceAddress: str

@typing.type_check_only
class TerraformOutput(typing.TypedDict, total=False):
    sensitive: bool
    value: typing.Any

@typing.type_check_only
class TerraformVariable(typing.TypedDict, total=False):
    inputValue: typing.Any

@typing.type_check_only
class TerraformVersion(typing.TypedDict, total=False):
    deprecateTime: str
    name: str
    obsoleteTime: str
    state: typing.Literal["STATE_UNSPECIFIED", "ACTIVE", "DEPRECATED", "OBSOLETE"]
    supportTime: str

@typing.type_check_only
class TestIamPermissionsRequest(typing.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class TestIamPermissionsResponse(typing.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class UnlockDeploymentRequest(typing.TypedDict, total=False):
    lockId: str
