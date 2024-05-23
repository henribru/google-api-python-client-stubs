import typing

import typing_extensions

_list = list

@typing.type_check_only
class ApplyResults(typing_extensions.TypedDict, total=False):
    artifacts: str
    content: str
    outputs: dict[str, typing.Any]

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
class CancelOperationRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class DeleteStatefileRequest(typing_extensions.TypedDict, total=False):
    lockId: str

@typing.type_check_only
class Deployment(typing_extensions.TypedDict, total=False):
    annotations: dict[str, typing.Any]
    artifactsGcsBucket: str
    createTime: str
    deleteBuild: str
    deleteLogs: str
    deleteResults: ApplyResults
    errorCode: typing_extensions.Literal[
        "ERROR_CODE_UNSPECIFIED",
        "REVISION_FAILED",
        "CLOUD_BUILD_PERMISSION_DENIED",
        "DELETE_BUILD_API_FAILED",
        "DELETE_BUILD_RUN_FAILED",
        "BUCKET_CREATION_PERMISSION_DENIED",
        "BUCKET_CREATION_FAILED",
    ]
    errorLogs: str
    importExistingResources: bool
    labels: dict[str, typing.Any]
    latestRevision: str
    lockState: typing_extensions.Literal[
        "LOCK_STATE_UNSPECIFIED",
        "LOCKED",
        "UNLOCKED",
        "LOCKING",
        "UNLOCKING",
        "LOCK_FAILED",
        "UNLOCK_FAILED",
    ]
    name: str
    quotaValidation: typing_extensions.Literal[
        "QUOTA_VALIDATION_UNSPECIFIED", "ENABLED", "ENFORCED"
    ]
    serviceAccount: str
    state: typing_extensions.Literal[
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
class DeploymentOperationMetadata(typing_extensions.TypedDict, total=False):
    applyResults: ApplyResults
    build: str
    logs: str
    step: typing_extensions.Literal[
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
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class ExportDeploymentStatefileRequest(typing_extensions.TypedDict, total=False):
    draft: bool

@typing.type_check_only
class ExportPreviewResultRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class ExportPreviewResultResponse(typing_extensions.TypedDict, total=False):
    result: PreviewResult

@typing.type_check_only
class ExportRevisionStatefileRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Expr(typing_extensions.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str

@typing.type_check_only
class GitSource(typing_extensions.TypedDict, total=False):
    directory: str
    ref: str
    repo: str

@typing.type_check_only
class ImportStatefileRequest(typing_extensions.TypedDict, total=False):
    lockId: str

@typing.type_check_only
class ListDeploymentsResponse(typing_extensions.TypedDict, total=False):
    deployments: _list[Deployment]
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
class ListPreviewsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    previews: _list[Preview]
    unreachable: _list[str]

@typing.type_check_only
class ListResourcesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    resources: _list[Resource]
    unreachable: _list[str]

@typing.type_check_only
class ListRevisionsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    revisions: _list[Revision]
    unreachable: _list[str]

@typing.type_check_only
class ListTerraformVersionsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    terraformVersions: _list[TerraformVersion]
    unreachable: _list[str]

@typing.type_check_only
class Location(typing_extensions.TypedDict, total=False):
    displayName: str
    labels: dict[str, typing.Any]
    locationId: str
    metadata: dict[str, typing.Any]
    name: str

@typing.type_check_only
class LockDeploymentRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class LockInfo(typing_extensions.TypedDict, total=False):
    createTime: str
    info: str
    lockId: str
    operation: str
    version: str
    who: str

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
    deploymentMetadata: DeploymentOperationMetadata
    endTime: str
    previewMetadata: PreviewOperationMetadata
    requestedCancellation: bool
    statusMessage: str
    target: str
    verb: str

@typing.type_check_only
class Policy(typing_extensions.TypedDict, total=False):
    auditConfigs: _list[AuditConfig]
    bindings: _list[Binding]
    etag: str
    version: int

@typing.type_check_only
class Preview(typing_extensions.TypedDict, total=False):
    annotations: dict[str, typing.Any]
    artifactsGcsBucket: str
    build: str
    createTime: str
    deployment: str
    errorCode: typing_extensions.Literal[
        "ERROR_CODE_UNSPECIFIED",
        "CLOUD_BUILD_PERMISSION_DENIED",
        "BUCKET_CREATION_PERMISSION_DENIED",
        "BUCKET_CREATION_FAILED",
        "DEPLOYMENT_LOCK_ACQUIRE_FAILED",
        "PREVIEW_BUILD_API_FAILED",
        "PREVIEW_BUILD_RUN_FAILED",
    ]
    errorLogs: str
    errorStatus: Status
    labels: dict[str, typing.Any]
    logs: str
    name: str
    previewArtifacts: PreviewArtifacts
    previewMode: typing_extensions.Literal[
        "PREVIEW_MODE_UNSPECIFIED", "DEFAULT", "DELETE"
    ]
    serviceAccount: str
    state: typing_extensions.Literal[
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
class PreviewArtifacts(typing_extensions.TypedDict, total=False):
    artifacts: str
    content: str

@typing.type_check_only
class PreviewOperationMetadata(typing_extensions.TypedDict, total=False):
    build: str
    logs: str
    previewArtifacts: PreviewArtifacts
    step: typing_extensions.Literal[
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
class PreviewResult(typing_extensions.TypedDict, total=False):
    binarySignedUri: str
    jsonSignedUri: str

@typing.type_check_only
class Resource(typing_extensions.TypedDict, total=False):
    caiAssets: dict[str, typing.Any]
    intent: typing_extensions.Literal[
        "INTENT_UNSPECIFIED", "CREATE", "UPDATE", "DELETE", "RECREATE", "UNCHANGED"
    ]
    name: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "PLANNED", "IN_PROGRESS", "RECONCILED", "FAILED"
    ]
    terraformInfo: ResourceTerraformInfo

@typing.type_check_only
class ResourceCAIInfo(typing_extensions.TypedDict, total=False):
    fullResourceName: str

@typing.type_check_only
class ResourceTerraformInfo(typing_extensions.TypedDict, total=False):
    address: str
    id: str
    type: str

@typing.type_check_only
class Revision(typing_extensions.TypedDict, total=False):
    action: typing_extensions.Literal[
        "ACTION_UNSPECIFIED", "CREATE", "UPDATE", "DELETE"
    ]
    applyResults: ApplyResults
    build: str
    createTime: str
    errorCode: typing_extensions.Literal[
        "ERROR_CODE_UNSPECIFIED",
        "CLOUD_BUILD_PERMISSION_DENIED",
        "APPLY_BUILD_API_FAILED",
        "APPLY_BUILD_RUN_FAILED",
        "QUOTA_VALIDATION_FAILED",
    ]
    errorLogs: str
    importExistingResources: bool
    logs: str
    name: str
    quotaValidation: typing_extensions.Literal[
        "QUOTA_VALIDATION_UNSPECIFIED", "ENABLED", "ENFORCED"
    ]
    quotaValidationResults: str
    serviceAccount: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "APPLYING", "APPLIED", "FAILED"
    ]
    stateDetail: str
    terraformBlueprint: TerraformBlueprint
    tfErrors: _list[TerraformError]
    tfVersion: str
    tfVersionConstraint: str
    updateTime: str
    workerPool: str

@typing.type_check_only
class SetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    policy: Policy
    updateMask: str

@typing.type_check_only
class Statefile(typing_extensions.TypedDict, total=False):
    signedUri: str

@typing.type_check_only
class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class TerraformBlueprint(typing_extensions.TypedDict, total=False):
    gcsSource: str
    gitSource: GitSource
    inputValues: dict[str, typing.Any]

@typing.type_check_only
class TerraformError(typing_extensions.TypedDict, total=False):
    error: Status
    errorDescription: str
    httpResponseCode: int
    resourceAddress: str

@typing.type_check_only
class TerraformOutput(typing_extensions.TypedDict, total=False):
    sensitive: bool
    value: typing.Any

@typing.type_check_only
class TerraformVariable(typing_extensions.TypedDict, total=False):
    inputValue: typing.Any

@typing.type_check_only
class TerraformVersion(typing_extensions.TypedDict, total=False):
    deprecateTime: str
    name: str
    obsoleteTime: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "ACTIVE", "DEPRECATED", "OBSOLETE"
    ]
    supportTime: str

@typing.type_check_only
class TestIamPermissionsRequest(typing_extensions.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class TestIamPermissionsResponse(typing_extensions.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class UnlockDeploymentRequest(typing_extensions.TypedDict, total=False):
    lockId: str
