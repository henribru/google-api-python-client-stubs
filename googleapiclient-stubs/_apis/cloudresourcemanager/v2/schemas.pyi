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
class CloudresourcemanagerGoogleCloudResourcemanagerV2alpha1FolderOperation(
    typing.TypedDict, total=False
):
    destinationParent: str
    displayName: str
    operationType: typing.Literal["OPERATION_TYPE_UNSPECIFIED", "CREATE", "MOVE"]
    sourceParent: str

@typing.type_check_only
class CloudresourcemanagerGoogleCloudResourcemanagerV2beta1FolderOperation(
    typing.TypedDict, total=False
):
    destinationParent: str
    displayName: str
    operationType: typing.Literal["OPERATION_TYPE_UNSPECIFIED", "CREATE", "MOVE"]
    sourceParent: str

@typing.type_check_only
class CreateFolderMetadata(typing.TypedDict, total=False):
    displayName: str
    parent: str

@typing.type_check_only
class CreateProjectMetadata(typing.TypedDict, total=False):
    createTime: str
    gettable: bool
    ready: bool

@typing.type_check_only
class CreateTagBindingMetadata(typing.TypedDict, total=False): ...

@typing.type_check_only
class CreateTagKeyMetadata(typing.TypedDict, total=False): ...

@typing.type_check_only
class CreateTagValueMetadata(typing.TypedDict, total=False): ...

@typing.type_check_only
class DeleteFolderMetadata(typing.TypedDict, total=False): ...

@typing.type_check_only
class DeleteOrganizationMetadata(typing.TypedDict, total=False): ...

@typing.type_check_only
class DeleteProjectMetadata(typing.TypedDict, total=False): ...

@typing.type_check_only
class DeleteTagBindingMetadata(typing.TypedDict, total=False): ...

@typing.type_check_only
class DeleteTagKeyMetadata(typing.TypedDict, total=False): ...

@typing.type_check_only
class DeleteTagValueMetadata(typing.TypedDict, total=False): ...

@typing.type_check_only
class Expr(typing.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str

@typing.type_check_only
class Folder(typing.TypedDict, total=False):
    configuredCapabilities: _list[str]
    createTime: str
    displayName: str
    lifecycleState: typing.Literal[
        "LIFECYCLE_STATE_UNSPECIFIED", "ACTIVE", "DELETE_REQUESTED"
    ]
    managementProject: str
    name: str
    parent: str
    tags: dict[str, typing.Any]

@typing.type_check_only
class FolderOperation(typing.TypedDict, total=False):
    destinationParent: str
    displayName: str
    operationType: typing.Literal["OPERATION_TYPE_UNSPECIFIED", "CREATE", "MOVE"]
    sourceParent: str

@typing.type_check_only
class FolderOperationError(typing.TypedDict, total=False):
    errorMessageId: typing.Literal[
        "ERROR_TYPE_UNSPECIFIED",
        "ACTIVE_FOLDER_HEIGHT_VIOLATION",
        "MAX_CHILD_FOLDERS_VIOLATION",
        "FOLDER_NAME_UNIQUENESS_VIOLATION",
        "RESOURCE_DELETED_VIOLATION",
        "PARENT_DELETED_VIOLATION",
        "CYCLE_INTRODUCED_VIOLATION",
        "FOLDER_BEING_MOVED_VIOLATION",
        "FOLDER_TO_DELETE_NON_EMPTY_VIOLATION",
        "DELETED_FOLDER_HEIGHT_VIOLATION",
        "FOLDER_TO_DELETE_CONFIGURED_CAPABILITY_VIOLATION",
    ]

@typing.type_check_only
class GetIamPolicyRequest(typing.TypedDict, total=False):
    options: GetPolicyOptions

@typing.type_check_only
class GetPolicyOptions(typing.TypedDict, total=False):
    requestedPolicyVersion: int

@typing.type_check_only
class ListFoldersResponse(typing.TypedDict, total=False):
    folders: _list[Folder]
    nextPageToken: str

@typing.type_check_only
class MoveFolderMetadata(typing.TypedDict, total=False):
    destinationParent: str
    displayName: str
    sourceParent: str

@typing.type_check_only
class MoveFolderRequest(typing.TypedDict, total=False):
    destinationParent: str

@typing.type_check_only
class MoveProjectMetadata(typing.TypedDict, total=False): ...

@typing.type_check_only
class Operation(typing.TypedDict, total=False):
    done: bool
    error: Status
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class Policy(typing.TypedDict, total=False):
    auditConfigs: _list[AuditConfig]
    bindings: _list[Binding]
    etag: str
    version: int

@typing.type_check_only
class ProjectCreationStatus(typing.TypedDict, total=False):
    createTime: str
    gettable: bool
    ready: bool

@typing.type_check_only
class SearchFoldersRequest(typing.TypedDict, total=False):
    pageSize: int
    pageToken: str
    query: str

@typing.type_check_only
class SearchFoldersResponse(typing.TypedDict, total=False):
    folders: _list[Folder]
    nextPageToken: str

@typing.type_check_only
class SetIamPolicyRequest(typing.TypedDict, total=False):
    policy: Policy
    updateMask: str

@typing.type_check_only
class Status(typing.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class TestIamPermissionsRequest(typing.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class TestIamPermissionsResponse(typing.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class UndeleteFolderMetadata(typing.TypedDict, total=False): ...

@typing.type_check_only
class UndeleteFolderRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class UndeleteOrganizationMetadata(typing.TypedDict, total=False): ...

@typing.type_check_only
class UndeleteProjectMetadata(typing.TypedDict, total=False): ...

@typing.type_check_only
class UpdateFolderMetadata(typing.TypedDict, total=False): ...

@typing.type_check_only
class UpdateProjectMetadata(typing.TypedDict, total=False): ...

@typing.type_check_only
class UpdateTagKeyMetadata(typing.TypedDict, total=False): ...

@typing.type_check_only
class UpdateTagValueMetadata(typing.TypedDict, total=False): ...
