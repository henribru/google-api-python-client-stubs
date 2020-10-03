import typing

import typing_extensions

class Operation(typing_extensions.TypedDict, total=False):
    metadata: typing.Dict[str, typing.Any]
    done: bool
    error: Status
    response: typing.Dict[str, typing.Any]
    name: str

class SearchOrganizationsRequest(typing_extensions.TypedDict, total=False):
    pageToken: str
    filter: str
    pageSize: int

class FolderOperation(typing_extensions.TypedDict, total=False):
    destinationParent: str
    displayName: str
    operationType: typing_extensions.Literal[
        "OPERATION_TYPE_UNSPECIFIED", "CREATE", "MOVE"
    ]
    sourceParent: str

class GetAncestryResponse(typing_extensions.TypedDict, total=False):
    ancestor: typing.List[Ancestor]

class ResourceId(typing_extensions.TypedDict, total=False):
    id: str
    type: str

class GetAncestryRequest(typing_extensions.TypedDict, total=False): ...

class GetEffectiveOrgPolicyRequest(typing_extensions.TypedDict, total=False):
    constraint: str

class Ancestor(typing_extensions.TypedDict, total=False):
    resourceId: ResourceId

class ListOrgPoliciesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    policies: typing.List[OrgPolicy]

class OrganizationOwner(typing_extensions.TypedDict, total=False):
    directoryCustomerId: str

class ListOrgPoliciesRequest(typing_extensions.TypedDict, total=False):
    pageToken: str
    pageSize: int

class ListConstraint(typing_extensions.TypedDict, total=False):
    supportsUnder: bool
    suggestedValue: str

class ListAvailableOrgPolicyConstraintsResponse(
    typing_extensions.TypedDict, total=False
):
    constraints: typing.List[Constraint]
    nextPageToken: str

class Empty(typing_extensions.TypedDict, total=False): ...

class SetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    policy: Policy
    updateMask: str

class ProjectCreationStatus(typing_extensions.TypedDict, total=False):
    createTime: str
    ready: bool
    gettable: bool

class AuditConfig(typing_extensions.TypedDict, total=False):
    auditLogConfigs: typing.List[AuditLogConfig]
    service: str

class OrgPolicy(typing_extensions.TypedDict, total=False):
    listPolicy: ListPolicy
    etag: str
    constraint: str
    booleanPolicy: BooleanPolicy
    version: int
    updateTime: str
    restoreDefault: RestoreDefault

class Constraint(typing_extensions.TypedDict, total=False):
    constraintDefault: typing_extensions.Literal[
        "CONSTRAINT_DEFAULT_UNSPECIFIED", "ALLOW", "DENY"
    ]
    description: str
    listConstraint: ListConstraint
    name: str
    version: int
    booleanConstraint: BooleanConstraint
    displayName: str

class BooleanPolicy(typing_extensions.TypedDict, total=False):
    enforced: bool

class SetOrgPolicyRequest(typing_extensions.TypedDict, total=False):
    policy: OrgPolicy

class Policy(typing_extensions.TypedDict, total=False):
    version: int
    bindings: typing.List[Binding]
    etag: str
    auditConfigs: typing.List[AuditConfig]

class Status(typing_extensions.TypedDict, total=False):
    details: typing.List[typing.Dict[str, typing.Any]]
    code: int
    message: str

class ClearOrgPolicyRequest(typing_extensions.TypedDict, total=False):
    constraint: str
    etag: str

class GetPolicyOptions(typing_extensions.TypedDict, total=False):
    requestedPolicyVersion: int

class SearchOrganizationsResponse(typing_extensions.TypedDict, total=False):
    organizations: typing.List[Organization]
    nextPageToken: str

class Lien(typing_extensions.TypedDict, total=False):
    reason: str
    origin: str
    restrictions: typing.List[str]
    parent: str
    name: str
    createTime: str

class BooleanConstraint(typing_extensions.TypedDict, total=False): ...

class Expr(typing_extensions.TypedDict, total=False):
    title: str
    location: str
    expression: str
    description: str

class ListLiensResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    liens: typing.List[Lien]

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

class Organization(typing_extensions.TypedDict, total=False):
    displayName: str
    lifecycleState: typing_extensions.Literal[
        "LIFECYCLE_STATE_UNSPECIFIED", "ACTIVE", "DELETE_REQUESTED"
    ]
    owner: OrganizationOwner
    creationTime: str
    name: str

class Binding(typing_extensions.TypedDict, total=False):
    role: str
    bindingId: str
    members: typing.List[str]
    condition: Expr

class AuditLogConfig(typing_extensions.TypedDict, total=False):
    exemptedMembers: typing.List[str]
    logType: typing_extensions.Literal[
        "LOG_TYPE_UNSPECIFIED", "ADMIN_READ", "DATA_WRITE", "DATA_READ"
    ]

class Project(typing_extensions.TypedDict, total=False):
    projectNumber: str
    name: str
    createTime: str
    labels: typing.Dict[str, typing.Any]
    projectId: str
    parent: ResourceId
    lifecycleState: typing_extensions.Literal[
        "LIFECYCLE_STATE_UNSPECIFIED",
        "ACTIVE",
        "DELETE_REQUESTED",
        "DELETE_IN_PROGRESS",
    ]

class GetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    options: GetPolicyOptions

class UndeleteProjectRequest(typing_extensions.TypedDict, total=False): ...
class RestoreDefault(typing_extensions.TypedDict, total=False): ...

class TestIamPermissionsRequest(typing_extensions.TypedDict, total=False):
    permissions: typing.List[str]

class ListPolicy(typing_extensions.TypedDict, total=False):
    suggestedValue: str
    allowedValues: typing.List[str]
    allValues: typing_extensions.Literal["ALL_VALUES_UNSPECIFIED", "ALLOW", "DENY"]
    deniedValues: typing.List[str]
    inheritFromParent: bool

class GetOrgPolicyRequest(typing_extensions.TypedDict, total=False):
    constraint: str

class ListAvailableOrgPolicyConstraintsRequest(
    typing_extensions.TypedDict, total=False
):
    pageSize: int
    pageToken: str

class ListProjectsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    projects: typing.List[Project]

class TestIamPermissionsResponse(typing_extensions.TypedDict, total=False):
    permissions: typing.List[str]
