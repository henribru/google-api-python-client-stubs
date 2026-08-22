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
class Capability(typing.TypedDict, total=False):
    name: str
    value: bool

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
class EffectiveTag(typing.TypedDict, total=False):
    inherited: bool
    namespacedTagKey: str
    namespacedTagValue: str
    tagKey: str
    tagKeyParentName: str
    tagValue: str

@typing.type_check_only
class EffectiveTagBindingCollection(typing.TypedDict, total=False):
    effectiveTags: dict[str, typing.Any]
    fullResourceName: str
    name: str

@typing.type_check_only
class Empty(typing.TypedDict, total=False): ...

@typing.type_check_only
class Expr(typing.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str

@typing.type_check_only
class FetchResourceSemanticsResponse(typing.TypedDict, total=False):
    fullResourceName: str
    semantics: dict[str, typing.Any]

@typing.type_check_only
class Folder(typing.TypedDict, total=False):
    configuredCapabilities: _list[str]
    createTime: str
    deleteTime: str
    displayName: str
    etag: str
    managementProject: str
    name: str
    parent: str
    state: typing.Literal["STATE_UNSPECIFIED", "ACTIVE", "DELETE_REQUESTED"]
    tags: dict[str, typing.Any]
    updateTime: str

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
class Lien(typing.TypedDict, total=False):
    createTime: str
    name: str
    origin: str
    parent: str
    reason: str
    restrictions: _list[str]

@typing.type_check_only
class ListEffectiveTagsResponse(typing.TypedDict, total=False):
    effectiveTags: _list[EffectiveTag]
    nextPageToken: str

@typing.type_check_only
class ListFoldersResponse(typing.TypedDict, total=False):
    folders: _list[Folder]
    nextPageToken: str

@typing.type_check_only
class ListLiensResponse(typing.TypedDict, total=False):
    liens: _list[Lien]
    nextPageToken: str

@typing.type_check_only
class ListProjectsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    projects: _list[Project]

@typing.type_check_only
class ListTagBindingsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    tagBindings: _list[TagBinding]

@typing.type_check_only
class ListTagHoldsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    tagHolds: _list[TagHold]

@typing.type_check_only
class ListTagKeysResponse(typing.TypedDict, total=False):
    nextPageToken: str
    tagKeys: _list[TagKey]

@typing.type_check_only
class ListTagValuesResponse(typing.TypedDict, total=False):
    nextPageToken: str
    tagValues: _list[TagValue]

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
class MoveProjectRequest(typing.TypedDict, total=False):
    destinationParent: str

@typing.type_check_only
class Operation(typing.TypedDict, total=False):
    done: bool
    error: Status
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class Organization(typing.TypedDict, total=False):
    createTime: str
    deleteTime: str
    directoryCustomerId: str
    displayName: str
    etag: str
    name: str
    state: typing.Literal["STATE_UNSPECIFIED", "ACTIVE", "DELETE_REQUESTED"]
    updateTime: str

@typing.type_check_only
class Policy(typing.TypedDict, total=False):
    auditConfigs: _list[AuditConfig]
    bindings: _list[Binding]
    etag: str
    version: int

@typing.type_check_only
class Project(typing.TypedDict, total=False):
    configuredCapabilities: _list[str]
    createTime: str
    deleteTime: str
    displayName: str
    etag: str
    labels: dict[str, typing.Any]
    name: str
    parent: str
    projectId: str
    state: typing.Literal["STATE_UNSPECIFIED", "ACTIVE", "DELETE_REQUESTED"]
    tags: dict[str, typing.Any]
    updateTime: str

@typing.type_check_only
class ProjectCreationStatus(typing.TypedDict, total=False):
    createTime: str
    gettable: bool
    ready: bool

@typing.type_check_only
class SearchFoldersResponse(typing.TypedDict, total=False):
    folders: _list[Folder]
    nextPageToken: str

@typing.type_check_only
class SearchOrganizationsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    organizations: _list[Organization]

@typing.type_check_only
class SearchProjectsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    projects: _list[Project]

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
class TagBinding(typing.TypedDict, total=False):
    name: str
    parent: str
    tagValue: str
    tagValueNamespacedName: str

@typing.type_check_only
class TagBindingCollection(typing.TypedDict, total=False):
    etag: str
    fullResourceName: str
    name: str
    tags: dict[str, typing.Any]

@typing.type_check_only
class TagHold(typing.TypedDict, total=False):
    createTime: str
    helpLink: str
    holder: str
    name: str
    origin: str

@typing.type_check_only
class TagKey(typing.TypedDict, total=False):
    allowedValuesRegex: str
    createTime: str
    description: str
    etag: str
    name: str
    namespacedName: str
    parent: str
    purpose: typing.Literal["PURPOSE_UNSPECIFIED", "GCE_FIREWALL", "DATA_GOVERNANCE"]
    purposeData: dict[str, typing.Any]
    shortName: str
    updateTime: str

@typing.type_check_only
class TagValue(typing.TypedDict, total=False):
    createTime: str
    description: str
    etag: str
    name: str
    namespacedName: str
    parent: str
    shortName: str
    updateTime: str

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
class UndeleteProjectRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class UpdateFolderMetadata(typing.TypedDict, total=False): ...

@typing.type_check_only
class UpdateProjectMetadata(typing.TypedDict, total=False): ...

@typing.type_check_only
class UpdateTagKeyMetadata(typing.TypedDict, total=False): ...

@typing.type_check_only
class UpdateTagValueMetadata(typing.TypedDict, total=False): ...
