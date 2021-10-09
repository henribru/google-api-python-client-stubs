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
class BooleanConstraint(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class BooleanPolicy(typing_extensions.TypedDict, total=False):
    enforced: bool

@typing.type_check_only
class ClearOrgPolicyRequest(typing_extensions.TypedDict, total=False):
    constraint: str
    etag: str

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
class Constraint(typing_extensions.TypedDict, total=False):
    booleanConstraint: BooleanConstraint
    constraintDefault: typing_extensions.Literal[
        "CONSTRAINT_DEFAULT_UNSPECIFIED", "ALLOW", "DENY"
    ]
    description: str
    displayName: str
    listConstraint: ListConstraint
    name: str
    version: int

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
class GetEffectiveOrgPolicyRequest(typing_extensions.TypedDict, total=False):
    constraint: str

@typing.type_check_only
class GetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    options: GetPolicyOptions

@typing.type_check_only
class GetOrgPolicyRequest(typing_extensions.TypedDict, total=False):
    constraint: str

@typing.type_check_only
class GetPolicyOptions(typing_extensions.TypedDict, total=False):
    requestedPolicyVersion: int

@typing.type_check_only
class Lien(typing_extensions.TypedDict, total=False):
    createTime: str
    name: str
    origin: str
    parent: str
    reason: str
    restrictions: _list[str]

@typing.type_check_only
class ListAvailableOrgPolicyConstraintsRequest(
    typing_extensions.TypedDict, total=False
):
    pageSize: int
    pageToken: str

@typing.type_check_only
class ListAvailableOrgPolicyConstraintsResponse(
    typing_extensions.TypedDict, total=False
):
    constraints: _list[Constraint]
    nextPageToken: str

@typing.type_check_only
class ListConstraint(typing_extensions.TypedDict, total=False):
    suggestedValue: str
    supportsUnder: bool

@typing.type_check_only
class ListLiensResponse(typing_extensions.TypedDict, total=False):
    liens: _list[Lien]
    nextPageToken: str

@typing.type_check_only
class ListOrgPoliciesRequest(typing_extensions.TypedDict, total=False):
    pageSize: int
    pageToken: str

@typing.type_check_only
class ListOrgPoliciesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    policies: _list[OrgPolicy]

@typing.type_check_only
class ListPolicy(typing_extensions.TypedDict, total=False):
    allValues: typing_extensions.Literal["ALL_VALUES_UNSPECIFIED", "ALLOW", "DENY"]
    allowedValues: _list[str]
    deniedValues: _list[str]
    inheritFromParent: bool
    suggestedValue: str

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
class Operation(typing_extensions.TypedDict, total=False):
    done: bool
    error: Status
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class OrgPolicy(typing_extensions.TypedDict, total=False):
    booleanPolicy: BooleanPolicy
    constraint: str
    etag: str
    listPolicy: ListPolicy
    restoreDefault: RestoreDefault
    updateTime: str
    version: int

@typing.type_check_only
class Organization(typing_extensions.TypedDict, total=False):
    creationTime: str
    displayName: str
    lifecycleState: typing_extensions.Literal[
        "LIFECYCLE_STATE_UNSPECIFIED", "ACTIVE", "DELETE_REQUESTED"
    ]
    name: str
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
class RestoreDefault(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class SearchOrganizationsRequest(typing_extensions.TypedDict, total=False):
    filter: str
    pageSize: int
    pageToken: str

@typing.type_check_only
class SearchOrganizationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    organizations: _list[Organization]

@typing.type_check_only
class SetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    policy: Policy
    updateMask: str

@typing.type_check_only
class SetOrgPolicyRequest(typing_extensions.TypedDict, total=False):
    policy: OrgPolicy

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
