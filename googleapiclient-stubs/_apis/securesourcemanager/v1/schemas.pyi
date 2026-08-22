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
class BatchCreatePullRequestCommentsRequest(typing.TypedDict, total=False):
    requests: _list[CreatePullRequestCommentRequest]

@typing.type_check_only
class Binding(typing.TypedDict, total=False):
    condition: Expr
    members: _list[str]
    role: str

@typing.type_check_only
class Branch(typing.TypedDict, total=False):
    ref: str
    sha: str

@typing.type_check_only
class BranchRule(typing.TypedDict, total=False):
    allowStaleReviews: bool
    annotations: dict[str, typing.Any]
    createTime: str
    disabled: bool
    etag: str
    includePattern: str
    minimumApprovalsCount: int
    minimumReviewsCount: int
    name: str
    requireCommentsResolved: bool
    requireLinearHistory: bool
    requirePullRequest: bool
    requiredStatusChecks: _list[Check]
    uid: str
    updateTime: str

@typing.type_check_only
class CancelOperationRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class Check(typing.TypedDict, total=False):
    context: str

@typing.type_check_only
class CloseIssueRequest(typing.TypedDict, total=False):
    etag: str

@typing.type_check_only
class ClosePullRequestRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class Code(typing.TypedDict, total=False):
    body: str
    effectiveCommitSha: str
    effectiveRootComment: str
    position: Position
    reply: str
    resolved: bool

@typing.type_check_only
class Comment(typing.TypedDict, total=False):
    body: str

@typing.type_check_only
class CreatePullRequestCommentRequest(typing.TypedDict, total=False):
    parent: str
    pullRequestComment: PullRequestComment

@typing.type_check_only
class Empty(typing.TypedDict, total=False): ...

@typing.type_check_only
class Expr(typing.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str

@typing.type_check_only
class FetchBlobResponse(typing.TypedDict, total=False):
    content: str
    sha: str

@typing.type_check_only
class FetchTreeResponse(typing.TypedDict, total=False):
    nextPageToken: str
    treeEntries: _list[TreeEntry]

@typing.type_check_only
class FileDiff(typing.TypedDict, total=False):
    action: typing.Literal["ACTION_UNSPECIFIED", "ADDED", "MODIFIED", "DELETED"]
    name: str
    patch: str
    sha: str

@typing.type_check_only
class Hook(typing.TypedDict, total=False):
    createTime: str
    disabled: bool
    events: _list[typing.Literal["UNSPECIFIED", "PUSH", "PULL_REQUEST"]]
    name: str
    pushOption: PushOption
    sensitiveQueryString: str
    targetUri: str
    uid: str
    updateTime: str

@typing.type_check_only
class HostConfig(typing.TypedDict, total=False):
    api: str
    gitHttp: str
    gitSsh: str
    html: str

@typing.type_check_only
class InitialConfig(typing.TypedDict, total=False):
    defaultBranch: str
    gitignores: _list[str]
    license: str
    readme: str

@typing.type_check_only
class Instance(typing.TypedDict, total=False):
    createTime: str
    hostConfig: HostConfig
    kmsKey: str
    labels: dict[str, typing.Any]
    name: str
    privateConfig: PrivateConfig
    state: typing.Literal[
        "STATE_UNSPECIFIED", "CREATING", "ACTIVE", "DELETING", "PAUSED", "UNKNOWN"
    ]
    stateNote: typing.Literal[
        "STATE_NOTE_UNSPECIFIED", "PAUSED_CMEK_UNAVAILABLE", "INSTANCE_RESUMING"
    ]
    updateTime: str
    workforceIdentityFederationConfig: WorkforceIdentityFederationConfig

@typing.type_check_only
class Issue(typing.TypedDict, total=False):
    body: str
    closeTime: str
    createTime: str
    etag: str
    name: str
    state: typing.Literal["STATE_UNSPECIFIED", "OPEN", "CLOSED"]
    title: str
    updateTime: str

@typing.type_check_only
class IssueComment(typing.TypedDict, total=False):
    body: str
    createTime: str
    name: str
    updateTime: str

@typing.type_check_only
class ListBranchRulesResponse(typing.TypedDict, total=False):
    branchRules: _list[BranchRule]
    nextPageToken: str

@typing.type_check_only
class ListHooksResponse(typing.TypedDict, total=False):
    hooks: _list[Hook]
    nextPageToken: str

@typing.type_check_only
class ListInstancesResponse(typing.TypedDict, total=False):
    instances: _list[Instance]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListIssueCommentsResponse(typing.TypedDict, total=False):
    issueComments: _list[IssueComment]
    nextPageToken: str

@typing.type_check_only
class ListIssuesResponse(typing.TypedDict, total=False):
    issues: _list[Issue]
    nextPageToken: str

@typing.type_check_only
class ListLocationsResponse(typing.TypedDict, total=False):
    locations: _list[Location]
    nextPageToken: str

@typing.type_check_only
class ListOperationsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    operations: _list[Operation]

@typing.type_check_only
class ListPullRequestCommentsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    pullRequestComments: _list[PullRequestComment]

@typing.type_check_only
class ListPullRequestFileDiffsResponse(typing.TypedDict, total=False):
    fileDiffs: _list[FileDiff]
    nextPageToken: str

@typing.type_check_only
class ListPullRequestsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    pullRequests: _list[PullRequest]

@typing.type_check_only
class ListRepositoriesResponse(typing.TypedDict, total=False):
    nextPageToken: str
    repositories: _list[Repository]

@typing.type_check_only
class Location(typing.TypedDict, total=False):
    displayName: str
    labels: dict[str, typing.Any]
    locationId: str
    metadata: dict[str, typing.Any]
    name: str

@typing.type_check_only
class MergePullRequestRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class OpenIssueRequest(typing.TypedDict, total=False):
    etag: str

@typing.type_check_only
class OpenPullRequestRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class Operation(typing.TypedDict, total=False):
    done: bool
    error: Status
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class OperationMetadata(typing.TypedDict, total=False):
    apiVersion: str
    createTime: str
    endTime: str
    requestedCancellation: bool
    statusMessage: str
    target: str
    verb: str

@typing.type_check_only
class Policy(typing.TypedDict, total=False):
    auditConfigs: _list[AuditConfig]
    bindings: _list[Binding]
    etag: str
    version: int

@typing.type_check_only
class Position(typing.TypedDict, total=False):
    line: str
    path: str

@typing.type_check_only
class PrivateConfig(typing.TypedDict, total=False):
    caPool: str
    httpServiceAttachment: str
    isPrivate: bool
    pscAllowedProjects: _list[str]
    sshServiceAttachment: str

@typing.type_check_only
class PullRequest(typing.TypedDict, total=False):
    base: Branch
    body: str
    closeTime: str
    createTime: str
    head: Branch
    name: str
    state: typing.Literal["STATE_UNSPECIFIED", "OPEN", "CLOSED", "MERGED"]
    title: str
    updateTime: str

@typing.type_check_only
class PullRequestComment(typing.TypedDict, total=False):
    code: Code
    comment: Comment
    createTime: str
    name: str
    review: Review
    updateTime: str

@typing.type_check_only
class PushOption(typing.TypedDict, total=False):
    branchFilter: str

@typing.type_check_only
class Repository(typing.TypedDict, total=False):
    createTime: str
    description: str
    etag: str
    initialConfig: InitialConfig
    instance: str
    name: str
    uid: str
    updateTime: str
    uris: URIs

@typing.type_check_only
class ResolvePullRequestCommentsRequest(typing.TypedDict, total=False):
    autoFill: bool
    names: _list[str]

@typing.type_check_only
class Review(typing.TypedDict, total=False):
    actionType: typing.Literal[
        "ACTION_TYPE_UNSPECIFIED", "COMMENT", "CHANGE_REQUESTED", "APPROVED"
    ]
    body: str
    effectiveCommitSha: str

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
class TreeEntry(typing.TypedDict, total=False):
    mode: str
    path: str
    sha: str
    size: str
    type: typing.Literal["OBJECT_TYPE_UNSPECIFIED", "TREE", "BLOB", "COMMIT"]

@typing.type_check_only
class URIs(typing.TypedDict, total=False):
    api: str
    gitHttps: str
    html: str

@typing.type_check_only
class UnresolvePullRequestCommentsRequest(typing.TypedDict, total=False):
    autoFill: bool
    names: _list[str]

@typing.type_check_only
class WorkforceIdentityFederationConfig(typing.TypedDict, total=False):
    enabled: bool
