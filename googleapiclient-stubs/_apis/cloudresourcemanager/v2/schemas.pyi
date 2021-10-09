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
class CloudresourcemanagerGoogleCloudResourcemanagerV2alpha1FolderOperation(
    typing_extensions.TypedDict, total=False
):
    destinationParent: str
    displayName: str
    operationType: typing_extensions.Literal[
        "OPERATION_TYPE_UNSPECIFIED", "CREATE", "MOVE"
    ]
    sourceParent: str

@typing.type_check_only
class CloudresourcemanagerGoogleCloudResourcemanagerV2beta1FolderOperation(
    typing_extensions.TypedDict, total=False
):
    destinationParent: str
    displayName: str
    operationType: typing_extensions.Literal[
        "OPERATION_TYPE_UNSPECIFIED", "CREATE", "MOVE"
    ]
    sourceParent: str

@typing.type_check_only
class CreateFolderMetadata(typing_extensions.TypedDict, total=False):
    displayName: str
    parent: str

@typing.type_check_only
class CreateProjectMetadata(typing_extensions.TypedDict, total=False):
    createTime: str
    gettable: bool
    ready: bool

@typing.type_check_only
class CreateTagBindingMetadata(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class CreateTagKeyMetadata(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class CreateTagValueMetadata(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class DeleteFolderMetadata(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class DeleteOrganizationMetadata(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class DeleteProjectMetadata(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class DeleteTagBindingMetadata(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class DeleteTagKeyMetadata(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class DeleteTagValueMetadata(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Expr(typing_extensions.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str

@typing.type_check_only
class Folder(typing_extensions.TypedDict, total=False):
    createTime: str
    displayName: str
    lifecycleState: typing_extensions.Literal[
        "LIFECYCLE_STATE_UNSPECIFIED", "ACTIVE", "DELETE_REQUESTED"
    ]
    name: str
    parent: str

@typing.type_check_only
class FolderOperation(typing_extensions.TypedDict, total=False):
    destinationParent: str
    displayName: str
    operationType: typing_extensions.Literal[
        "OPERATION_TYPE_UNSPECIFIED", "CREATE", "MOVE"
    ]
    sourceParent: str

@typing.type_check_only
class FolderOperationError(typing_extensions.TypedDict, total=False):
    errorMessageId: typing_extensions.Literal[
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
    ]

@typing.type_check_only
class GetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    options: GetPolicyOptions

@typing.type_check_only
class GetPolicyOptions(typing_extensions.TypedDict, total=False):
    requestedPolicyVersion: int

@typing.type_check_only
class ListFoldersResponse(typing_extensions.TypedDict, total=False):
    folders: _list[Folder]
    nextPageToken: str

@typing.type_check_only
class MoveFolderMetadata(typing_extensions.TypedDict, total=False):
    destinationParent: str
    displayName: str
    sourceParent: str

@typing.type_check_only
class MoveFolderRequest(typing_extensions.TypedDict, total=False):
    destinationParent: str

@typing.type_check_only
class MoveProjectMetadata(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Operation(typing_extensions.TypedDict, total=False):
    done: bool
    error: Status
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class Policy(typing_extensions.TypedDict, total=False):
    auditConfigs: _list[AuditConfig]
    bindings: _list[Binding]
    etag: str
    version: int

@typing.type_check_only
class ProjectCreationStatus(typing_extensions.TypedDict, total=False):
    createTime: str
    gettable: bool
    ready: bool

@typing.type_check_only
class SearchFoldersRequest(typing_extensions.TypedDict, total=False):
    pageSize: int
    pageToken: str
    query: str

@typing.type_check_only
class SearchFoldersResponse(typing_extensions.TypedDict, total=False):
    folders: _list[Folder]
    nextPageToken: str

@typing.type_check_only
class SetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    policy: Policy
    updateMask: str

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

@typing.type_check_only
class UndeleteFolderMetadata(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class UndeleteFolderRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class UndeleteOrganizationMetadata(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class UndeleteProjectMetadata(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class UpdateFolderMetadata(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class UpdateProjectMetadata(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class UpdateTagKeyMetadata(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class UpdateTagValueMetadata(typing_extensions.TypedDict, total=False): ...
