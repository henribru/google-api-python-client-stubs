import typing

import typing_extensions

class ListOrganizationsResponse(typing_extensions.TypedDict, total=False):
    organizations: typing.List[Organization]
    nextPageToken: str

class ListProjectsResponse(typing_extensions.TypedDict, total=False):
    projects: typing.List[Project]
    nextPageToken: str

class AuditLogConfig(typing_extensions.TypedDict, total=False):
    exemptedMembers: typing.List[str]
    logType: typing_extensions.Literal[
        "LOG_TYPE_UNSPECIFIED", "ADMIN_READ", "DATA_WRITE", "DATA_READ"
    ]

class GetAncestryResponse(typing_extensions.TypedDict, total=False):
    ancestor: typing.List[Ancestor]

class Organization(typing_extensions.TypedDict, total=False):
    displayName: str
    lifecycleState: typing_extensions.Literal[
        "LIFECYCLE_STATE_UNSPECIFIED", "ACTIVE", "DELETE_REQUESTED"
    ]
    organizationId: str
    name: str
    owner: OrganizationOwner
    creationTime: str

class OrganizationOwner(typing_extensions.TypedDict, total=False):
    directoryCustomerId: str

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

class TestIamPermissionsRequest(typing_extensions.TypedDict, total=False):
    permissions: typing.List[str]

class GetAncestryRequest(typing_extensions.TypedDict, total=False): ...

class FolderOperation(typing_extensions.TypedDict, total=False):
    operationType: typing_extensions.Literal[
        "OPERATION_TYPE_UNSPECIFIED", "CREATE", "MOVE"
    ]
    destinationParent: str
    sourceParent: str
    displayName: str

class ResourceId(typing_extensions.TypedDict, total=False):
    type: str
    id: str

class Project(typing_extensions.TypedDict, total=False):
    parent: ResourceId
    labels: typing.Dict[str, typing.Any]
    projectNumber: str
    lifecycleState: typing_extensions.Literal[
        "LIFECYCLE_STATE_UNSPECIFIED",
        "ACTIVE",
        "DELETE_REQUESTED",
        "DELETE_IN_PROGRESS",
    ]
    projectId: str
    name: str
    createTime: str

class Ancestor(typing_extensions.TypedDict, total=False):
    resourceId: ResourceId

class SetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    updateMask: str
    policy: Policy

class Empty(typing_extensions.TypedDict, total=False): ...

class GetPolicyOptions(typing_extensions.TypedDict, total=False):
    requestedPolicyVersion: int

class Binding(typing_extensions.TypedDict, total=False):
    members: typing.List[str]
    role: str
    condition: Expr
    bindingId: str

class GetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    options: GetPolicyOptions

class Expr(typing_extensions.TypedDict, total=False):
    title: str
    location: str
    description: str
    expression: str

class ProjectCreationStatus(typing_extensions.TypedDict, total=False):
    createTime: str
    gettable: bool
    ready: bool

class Policy(typing_extensions.TypedDict, total=False):
    bindings: typing.List[Binding]
    etag: str
    version: int
    auditConfigs: typing.List[AuditConfig]

class AuditConfig(typing_extensions.TypedDict, total=False):
    auditLogConfigs: typing.List[AuditLogConfig]
    service: str

class TestIamPermissionsResponse(typing_extensions.TypedDict, total=False):
    permissions: typing.List[str]

class UndeleteProjectRequest(typing_extensions.TypedDict, total=False): ...
