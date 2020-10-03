import typing

import typing_extensions

class SearchFoldersRequest(typing_extensions.TypedDict, total=False):
    pageSize: int
    pageToken: str
    query: str

class GetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    options: GetPolicyOptions

class Policy(typing_extensions.TypedDict, total=False):
    auditConfigs: typing.List[AuditConfig]
    bindings: typing.List[Binding]
    version: int
    etag: str

class ListFoldersResponse(typing_extensions.TypedDict, total=False):
    folders: typing.List[Folder]
    nextPageToken: str

class MoveFolderRequest(typing_extensions.TypedDict, total=False):
    destinationParent: str

class FolderOperation(typing_extensions.TypedDict, total=False):
    operationType: typing_extensions.Literal[
        "OPERATION_TYPE_UNSPECIFIED", "CREATE", "MOVE"
    ]
    destinationParent: str
    displayName: str
    sourceParent: str

class TestIamPermissionsRequest(typing_extensions.TypedDict, total=False):
    permissions: typing.List[str]

class Folder(typing_extensions.TypedDict, total=False):
    lifecycleState: typing_extensions.Literal[
        "LIFECYCLE_STATE_UNSPECIFIED", "ACTIVE", "DELETE_REQUESTED"
    ]
    parent: str
    name: str
    createTime: str
    displayName: str

class Expr(typing_extensions.TypedDict, total=False):
    description: str
    location: str
    title: str
    expression: str

class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: typing.List[typing.Dict[str, typing.Any]]
    message: str

class ProjectCreationStatus(typing_extensions.TypedDict, total=False):
    ready: bool
    createTime: str
    gettable: bool

class SetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    policy: Policy
    updateMask: str

class AuditLogConfig(typing_extensions.TypedDict, total=False):
    logType: typing_extensions.Literal[
        "LOG_TYPE_UNSPECIFIED", "ADMIN_READ", "DATA_WRITE", "DATA_READ"
    ]
    exemptedMembers: typing.List[str]

class Binding(typing_extensions.TypedDict, total=False):
    bindingId: str
    condition: Expr
    role: str
    members: typing.List[str]

class SearchFoldersResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    folders: typing.List[Folder]

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

class GetPolicyOptions(typing_extensions.TypedDict, total=False):
    requestedPolicyVersion: int

class Operation(typing_extensions.TypedDict, total=False):
    name: str
    metadata: typing.Dict[str, typing.Any]
    response: typing.Dict[str, typing.Any]
    done: bool
    error: Status

class UndeleteFolderRequest(typing_extensions.TypedDict, total=False): ...

class TestIamPermissionsResponse(typing_extensions.TypedDict, total=False):
    permissions: typing.List[str]

class AuditConfig(typing_extensions.TypedDict, total=False):
    auditLogConfigs: typing.List[AuditLogConfig]
    service: str
