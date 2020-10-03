import typing

import typing_extensions

class SearchFoldersResponse(typing_extensions.TypedDict, total=False):
    folders: typing.List[Folder]
    nextPageToken: str

class Expr(typing_extensions.TypedDict, total=False):
    description: str
    title: str
    location: str
    expression: str

class Operation(typing_extensions.TypedDict, total=False):
    name: str
    response: typing.Dict[str, typing.Any]
    error: Status
    done: bool
    metadata: typing.Dict[str, typing.Any]

class GetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    options: GetPolicyOptions

class TestIamPermissionsRequest(typing_extensions.TypedDict, total=False):
    permissions: typing.List[str]

class SearchFoldersRequest(typing_extensions.TypedDict, total=False):
    pageToken: str
    query: str
    pageSize: int

class Policy(typing_extensions.TypedDict, total=False):
    etag: str
    auditConfigs: typing.List[AuditConfig]
    version: int
    bindings: typing.List[Binding]

class Folder(typing_extensions.TypedDict, total=False):
    displayName: str
    lifecycleState: typing_extensions.Literal[
        "LIFECYCLE_STATE_UNSPECIFIED", "ACTIVE", "DELETE_REQUESTED"
    ]
    parent: str
    name: str
    createTime: str

class Binding(typing_extensions.TypedDict, total=False):
    condition: Expr
    role: str
    bindingId: str
    members: typing.List[str]

class TestIamPermissionsResponse(typing_extensions.TypedDict, total=False):
    permissions: typing.List[str]

class AuditConfig(typing_extensions.TypedDict, total=False):
    auditLogConfigs: typing.List[AuditLogConfig]
    service: str

class ListFoldersResponse(typing_extensions.TypedDict, total=False):
    folders: typing.List[Folder]
    nextPageToken: str

class SetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    policy: Policy
    updateMask: str

class UndeleteFolderRequest(typing_extensions.TypedDict, total=False): ...

class ProjectCreationStatus(typing_extensions.TypedDict, total=False):
    ready: bool
    createTime: str
    gettable: bool

class FolderOperation(typing_extensions.TypedDict, total=False):
    operationType: typing_extensions.Literal[
        "OPERATION_TYPE_UNSPECIFIED", "CREATE", "MOVE"
    ]
    destinationParent: str
    sourceParent: str
    displayName: str

class AuditLogConfig(typing_extensions.TypedDict, total=False):
    exemptedMembers: typing.List[str]
    logType: typing_extensions.Literal[
        "LOG_TYPE_UNSPECIFIED", "ADMIN_READ", "DATA_WRITE", "DATA_READ"
    ]

class GetPolicyOptions(typing_extensions.TypedDict, total=False):
    requestedPolicyVersion: int

class MoveFolderRequest(typing_extensions.TypedDict, total=False):
    destinationParent: str

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

class Status(typing_extensions.TypedDict, total=False):
    details: typing.List[typing.Dict[str, typing.Any]]
    code: int
    message: str
