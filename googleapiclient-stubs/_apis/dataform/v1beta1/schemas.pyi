import typing

import typing_extensions

_list = list

@typing.type_check_only
class Assertion(typing_extensions.TypedDict, total=False):
    dependencyTargets: _list[Target]
    disabled: bool
    parentAction: Target
    relationDescriptor: RelationDescriptor
    selectQuery: str
    tags: _list[str]

@typing.type_check_only
class BigQueryAction(typing_extensions.TypedDict, total=False):
    sqlScript: str

@typing.type_check_only
class CancelWorkflowInvocationRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class CodeCompilationConfig(typing_extensions.TypedDict, total=False):
    assertionSchema: str
    databaseSuffix: str
    defaultDatabase: str
    defaultLocation: str
    defaultSchema: str
    schemaSuffix: str
    tablePrefix: str
    vars: dict[str, typing.Any]

@typing.type_check_only
class ColumnDescriptor(typing_extensions.TypedDict, total=False):
    bigqueryPolicyTags: _list[str]
    description: str
    path: _list[str]

@typing.type_check_only
class CommitAuthor(typing_extensions.TypedDict, total=False):
    emailAddress: str
    name: str

@typing.type_check_only
class CommitWorkspaceChangesRequest(typing_extensions.TypedDict, total=False):
    author: CommitAuthor
    commitMessage: str
    paths: _list[str]

@typing.type_check_only
class CompilationError(typing_extensions.TypedDict, total=False):
    actionTarget: Target
    message: str
    path: str
    stack: str

@typing.type_check_only
class CompilationResult(typing_extensions.TypedDict, total=False):
    codeCompilationConfig: CodeCompilationConfig
    compilationErrors: _list[CompilationError]
    dataformCoreVersion: str
    gitCommitish: str
    name: str
    releaseConfig: str
    resolvedGitCommitSha: str
    workspace: str

@typing.type_check_only
class CompilationResultAction(typing_extensions.TypedDict, total=False):
    assertion: Assertion
    canonicalTarget: Target
    declaration: Declaration
    filePath: str
    operations: Operations
    relation: Relation
    target: Target

@typing.type_check_only
class Declaration(typing_extensions.TypedDict, total=False):
    relationDescriptor: RelationDescriptor

@typing.type_check_only
class DirectoryEntry(typing_extensions.TypedDict, total=False):
    directory: str
    file: str

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class FetchFileDiffResponse(typing_extensions.TypedDict, total=False):
    formattedDiff: str

@typing.type_check_only
class FetchFileGitStatusesResponse(typing_extensions.TypedDict, total=False):
    uncommittedFileChanges: _list[UncommittedFileChange]

@typing.type_check_only
class FetchGitAheadBehindResponse(typing_extensions.TypedDict, total=False):
    commitsAhead: int
    commitsBehind: int

@typing.type_check_only
class FetchRemoteBranchesResponse(typing_extensions.TypedDict, total=False):
    branches: _list[str]

@typing.type_check_only
class GitRemoteSettings(typing_extensions.TypedDict, total=False):
    authenticationTokenSecretVersion: str
    defaultBranch: str
    tokenStatus: typing_extensions.Literal[
        "TOKEN_STATUS_UNSPECIFIED", "NOT_FOUND", "INVALID", "VALID"
    ]
    url: str

@typing.type_check_only
class IncrementalTableConfig(typing_extensions.TypedDict, total=False):
    incrementalPostOperations: _list[str]
    incrementalPreOperations: _list[str]
    incrementalSelectQuery: str
    refreshDisabled: bool
    uniqueKeyParts: _list[str]
    updatePartitionFilter: str

@typing.type_check_only
class InstallNpmPackagesRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class InstallNpmPackagesResponse(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Interval(typing_extensions.TypedDict, total=False):
    endTime: str
    startTime: str

@typing.type_check_only
class InvocationConfig(typing_extensions.TypedDict, total=False):
    fullyRefreshIncrementalTablesEnabled: bool
    includedTags: _list[str]
    includedTargets: _list[Target]
    transitiveDependenciesIncluded: bool
    transitiveDependentsIncluded: bool

@typing.type_check_only
class ListCompilationResultsResponse(typing_extensions.TypedDict, total=False):
    compilationResults: _list[CompilationResult]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListLocationsResponse(typing_extensions.TypedDict, total=False):
    locations: _list[Location]
    nextPageToken: str

@typing.type_check_only
class ListReleaseConfigsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    releaseConfigs: _list[ReleaseConfig]
    unreachable: _list[str]

@typing.type_check_only
class ListRepositoriesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    repositories: _list[Repository]
    unreachable: _list[str]

@typing.type_check_only
class ListWorkflowConfigsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    unreachable: _list[str]
    workflowConfigs: _list[WorkflowConfig]

@typing.type_check_only
class ListWorkflowInvocationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    unreachable: _list[str]
    workflowInvocations: _list[WorkflowInvocation]

@typing.type_check_only
class ListWorkspacesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    unreachable: _list[str]
    workspaces: _list[Workspace]

@typing.type_check_only
class Location(typing_extensions.TypedDict, total=False):
    displayName: str
    labels: dict[str, typing.Any]
    locationId: str
    metadata: dict[str, typing.Any]
    name: str

@typing.type_check_only
class MakeDirectoryRequest(typing_extensions.TypedDict, total=False):
    path: str

@typing.type_check_only
class MakeDirectoryResponse(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class MoveDirectoryRequest(typing_extensions.TypedDict, total=False):
    newPath: str
    path: str

@typing.type_check_only
class MoveDirectoryResponse(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class MoveFileRequest(typing_extensions.TypedDict, total=False):
    newPath: str
    path: str

@typing.type_check_only
class MoveFileResponse(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class OperationMetadata(typing_extensions.TypedDict, total=False):
    apiVersion: str
    cancelRequested: bool
    createTime: str
    endTime: str
    statusDetail: str
    target: str
    verb: str

@typing.type_check_only
class Operations(typing_extensions.TypedDict, total=False):
    dependencyTargets: _list[Target]
    disabled: bool
    hasOutput: bool
    queries: _list[str]
    relationDescriptor: RelationDescriptor
    tags: _list[str]

@typing.type_check_only
class PullGitCommitsRequest(typing_extensions.TypedDict, total=False):
    author: CommitAuthor
    remoteBranch: str

@typing.type_check_only
class PushGitCommitsRequest(typing_extensions.TypedDict, total=False):
    remoteBranch: str

@typing.type_check_only
class QueryCompilationResultActionsResponse(typing_extensions.TypedDict, total=False):
    compilationResultActions: _list[CompilationResultAction]
    nextPageToken: str

@typing.type_check_only
class QueryDirectoryContentsResponse(typing_extensions.TypedDict, total=False):
    directoryEntries: _list[DirectoryEntry]
    nextPageToken: str

@typing.type_check_only
class QueryWorkflowInvocationActionsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    workflowInvocationActions: _list[WorkflowInvocationAction]

@typing.type_check_only
class ReadFileResponse(typing_extensions.TypedDict, total=False):
    fileContents: str

@typing.type_check_only
class Relation(typing_extensions.TypedDict, total=False):
    additionalOptions: dict[str, typing.Any]
    clusterExpressions: _list[str]
    dependencyTargets: _list[Target]
    disabled: bool
    incrementalTableConfig: IncrementalTableConfig
    partitionExpirationDays: int
    partitionExpression: str
    postOperations: _list[str]
    preOperations: _list[str]
    relationDescriptor: RelationDescriptor
    relationType: typing_extensions.Literal[
        "RELATION_TYPE_UNSPECIFIED",
        "TABLE",
        "VIEW",
        "INCREMENTAL_TABLE",
        "MATERIALIZED_VIEW",
    ]
    requirePartitionFilter: bool
    selectQuery: str
    tags: _list[str]

@typing.type_check_only
class RelationDescriptor(typing_extensions.TypedDict, total=False):
    bigqueryLabels: dict[str, typing.Any]
    columns: _list[ColumnDescriptor]
    description: str

@typing.type_check_only
class ReleaseConfig(typing_extensions.TypedDict, total=False):
    codeCompilationConfig: CodeCompilationConfig
    cronSchedule: str
    gitCommitish: str
    name: str
    recentScheduledReleaseRecords: _list[ScheduledReleaseRecord]
    releaseCompilationResult: str
    timeZone: str

@typing.type_check_only
class RemoveDirectoryRequest(typing_extensions.TypedDict, total=False):
    path: str

@typing.type_check_only
class RemoveFileRequest(typing_extensions.TypedDict, total=False):
    path: str

@typing.type_check_only
class Repository(typing_extensions.TypedDict, total=False):
    gitRemoteSettings: GitRemoteSettings
    name: str
    npmrcEnvironmentVariablesSecretVersion: str
    workspaceCompilationOverrides: WorkspaceCompilationOverrides

@typing.type_check_only
class ResetWorkspaceChangesRequest(typing_extensions.TypedDict, total=False):
    clean: bool
    paths: _list[str]

@typing.type_check_only
class ScheduledExecutionRecord(typing_extensions.TypedDict, total=False):
    errorStatus: Status
    executionTime: str
    workflowInvocation: str

@typing.type_check_only
class ScheduledReleaseRecord(typing_extensions.TypedDict, total=False):
    compilationResult: str
    errorStatus: Status
    releaseTime: str

@typing.type_check_only
class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class Target(typing_extensions.TypedDict, total=False):
    database: str
    name: str
    schema: str

@typing.type_check_only
class UncommittedFileChange(typing_extensions.TypedDict, total=False):
    path: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "ADDED", "DELETED", "MODIFIED", "HAS_CONFLICTS"
    ]

@typing.type_check_only
class WorkflowConfig(typing_extensions.TypedDict, total=False):
    cronSchedule: str
    invocationConfig: InvocationConfig
    name: str
    recentScheduledExecutionRecords: _list[ScheduledExecutionRecord]
    releaseConfig: str
    timeZone: str

@typing.type_check_only
class WorkflowInvocation(typing_extensions.TypedDict, total=False):
    compilationResult: str
    invocationConfig: InvocationConfig
    invocationTiming: Interval
    name: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "RUNNING", "SUCCEEDED", "CANCELLED", "FAILED", "CANCELING"
    ]
    workflowConfig: str

@typing.type_check_only
class WorkflowInvocationAction(typing_extensions.TypedDict, total=False):
    bigqueryAction: BigQueryAction
    canonicalTarget: Target
    failureReason: str
    invocationTiming: Interval
    state: typing_extensions.Literal[
        "PENDING", "RUNNING", "SKIPPED", "DISABLED", "SUCCEEDED", "CANCELLED", "FAILED"
    ]
    target: Target

@typing.type_check_only
class Workspace(typing_extensions.TypedDict, total=False):
    name: str

@typing.type_check_only
class WorkspaceCompilationOverrides(typing_extensions.TypedDict, total=False):
    defaultDatabase: str
    schemaSuffix: str
    tablePrefix: str

@typing.type_check_only
class WriteFileRequest(typing_extensions.TypedDict, total=False):
    contents: str
    path: str

@typing.type_check_only
class WriteFileResponse(typing_extensions.TypedDict, total=False): ...
