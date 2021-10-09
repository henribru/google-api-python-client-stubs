import typing

import typing_extensions

_list = list

@typing.type_check_only
class Ancestor(typing_extensions.TypedDict, total=False):
    resourceId: ResourceId

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
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Expr(typing_extensions.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str

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
class GetAncestryRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class GetAncestryResponse(typing_extensions.TypedDict, total=False):
    ancestor: _list[Ancestor]

@typing.type_check_only
class GetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    options: GetPolicyOptions

@typing.type_check_only
class GetPolicyOptions(typing_extensions.TypedDict, total=False):
    requestedPolicyVersion: int

@typing.type_check_only
class ListOrganizationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    organizations: _list[Organization]

@typing.type_check_only
class ListProjectsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    projects: _list[Project]

@typing.type_check_only
class MoveFolderMetadata(typing_extensions.TypedDict, total=False):
    destinationParent: str
    displayName: str
    sourceParent: str

@typing.type_check_only
class MoveProjectMetadata(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Organization(typing_extensions.TypedDict, total=False):
    creationTime: str
    displayName: str
    lifecycleState: typing_extensions.Literal[
        "LIFECYCLE_STATE_UNSPECIFIED", "ACTIVE", "DELETE_REQUESTED"
    ]
    name: str
    organizationId: str
    owner: OrganizationOwner

@typing.type_check_only
class OrganizationOwner(typing_extensions.TypedDict, total=False):
    directoryCustomerId: str

@typing.type_check_only
class Policy(typing_extensions.TypedDict, total=False):
    auditConfigs: _list[AuditConfig]
    bindings: _list[Binding]
    etag: str
    version: int

@typing.type_check_only
class Project(typing_extensions.TypedDict, total=False):
    createTime: str
    labels: dict[str, typing.Any]
    lifecycleState: typing_extensions.Literal[
        "LIFECYCLE_STATE_UNSPECIFIED",
        "ACTIVE",
        "DELETE_REQUESTED",
        "DELETE_IN_PROGRESS",
    ]
    name: str
    parent: ResourceId
    projectId: str
    projectNumber: str

@typing.type_check_only
class ProjectCreationStatus(typing_extensions.TypedDict, total=False):
    createTime: str
    gettable: bool
    ready: bool

@typing.type_check_only
class ResourceId(typing_extensions.TypedDict, total=False):
    id: str
    type: str

@typing.type_check_only
class SetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    policy: Policy
    updateMask: str

@typing.type_check_only
class TestIamPermissionsRequest(typing_extensions.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class TestIamPermissionsResponse(typing_extensions.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class UndeleteFolderMetadata(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class UndeleteOrganizationMetadata(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class UndeleteProjectMetadata(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class UndeleteProjectRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class UpdateFolderMetadata(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class UpdateProjectMetadata(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class UpdateTagKeyMetadata(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class UpdateTagValueMetadata(typing_extensions.TypedDict, total=False): ...
