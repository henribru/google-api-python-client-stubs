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
    jobId: str
    sqlScript: str

@typing.type_check_only
class Binding(typing_extensions.TypedDict, total=False):
    condition: Expr
    members: _list[str]
    role: str

@typing.type_check_only
class CancelWorkflowInvocationRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class CodeCompilationConfig(typing_extensions.TypedDict, total=False):
    assertionSchema: str
    databaseSuffix: str
    defaultDatabase: str
    defaultLocation: str
    defaultNotebookRuntimeOptions: NotebookRuntimeOptions
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
class CommitLogEntry(typing_extensions.TypedDict, total=False):
    author: CommitAuthor
    commitMessage: str
    commitSha: str
    commitTime: str

@typing.type_check_only
class CommitMetadata(typing_extensions.TypedDict, total=False):
    author: CommitAuthor
    commitMessage: str

@typing.type_check_only
class CommitRepositoryChangesRequest(typing_extensions.TypedDict, total=False):
    commitMetadata: CommitMetadata
    fileOperations: dict[str, typing.Any]
    requiredHeadCommitSha: str

@typing.type_check_only
class CommitRepositoryChangesResponse(typing_extensions.TypedDict, total=False):
    commitSha: str

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
    createTime: str
    dataEncryptionState: DataEncryptionState
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
    notebook: Notebook
    operations: Operations
    relation: Relation
    target: Target

@typing.type_check_only
class ComputeRepositoryAccessTokenStatusResponse(
    typing_extensions.TypedDict, total=False
):
    tokenStatus: typing_extensions.Literal[
        "TOKEN_STATUS_UNSPECIFIED", "NOT_FOUND", "INVALID", "VALID"
    ]

@typing.type_check_only
class Config(typing_extensions.TypedDict, total=False):
    defaultKmsKeyName: str
    name: str

@typing.type_check_only
class DataEncryptionState(typing_extensions.TypedDict, total=False):
    kmsKeyVersionName: str

@typing.type_check_only
class Declaration(typing_extensions.TypedDict, total=False):
    relationDescriptor: RelationDescriptor

@typing.type_check_only
class DeleteFile(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class DirectoryEntry(typing_extensions.TypedDict, total=False):
    directory: str
    file: str

@typing.type_check_only
class DirectorySearchResult(typing_extensions.TypedDict, total=False):
    path: str

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Expr(typing_extensions.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str

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
class FetchRepositoryHistoryResponse(typing_extensions.TypedDict, total=False):
    commits: _list[CommitLogEntry]
    nextPageToken: str

@typing.type_check_only
class FileOperation(typing_extensions.TypedDict, total=False):
    deleteFile: DeleteFile
    writeFile: WriteFile

@typing.type_check_only
class FileSearchResult(typing_extensions.TypedDict, total=False):
    path: str

@typing.type_check_only
class GitRemoteSettings(typing_extensions.TypedDict, total=False):
    authenticationTokenSecretVersion: str
    defaultBranch: str
    sshAuthenticationConfig: SshAuthenticationConfig
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
    serviceAccount: str
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
class Notebook(typing_extensions.TypedDict, total=False):
    contents: str
    dependencyTargets: _list[Target]
    disabled: bool
    tags: _list[str]

@typing.type_check_only
class NotebookAction(typing_extensions.TypedDict, total=False):
    contents: str
    jobId: str

@typing.type_check_only
class NotebookRuntimeOptions(typing_extensions.TypedDict, total=False):
    gcsOutputBucket: str

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
class Policy(typing_extensions.TypedDict, total=False):
    bindings: _list[Binding]
    etag: str
    version: int

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
class QueryRepositoryDirectoryContentsResponse(
    typing_extensions.TypedDict, total=False
):
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
class ReadRepositoryFileResponse(typing_extensions.TypedDict, total=False):
    contents: str

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
    disabled: bool
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
    createTime: str
    dataEncryptionState: DataEncryptionState
    displayName: str
    gitRemoteSettings: GitRemoteSettings
    kmsKeyName: str
    labels: dict[str, typing.Any]
    name: str
    npmrcEnvironmentVariablesSecretVersion: str
    serviceAccount: str
    setAuthenticatedUserAdmin: bool
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
class SearchFilesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    searchResults: _list[SearchResult]

@typing.type_check_only
class SearchResult(typing_extensions.TypedDict, total=False):
    directory: DirectorySearchResult
    file: FileSearchResult

@typing.type_check_only
class SetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    policy: Policy

@typing.type_check_only
class SshAuthenticationConfig(typing_extensions.TypedDict, total=False):
    hostPublicKey: str
    userPrivateKeySecretVersion: str

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
class TestIamPermissionsRequest(typing_extensions.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class TestIamPermissionsResponse(typing_extensions.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class UncommittedFileChange(typing_extensions.TypedDict, total=False):
    path: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "ADDED", "DELETED", "MODIFIED", "HAS_CONFLICTS"
    ]

@typing.type_check_only
class WorkflowConfig(typing_extensions.TypedDict, total=False):
    createTime: str
    cronSchedule: str
    invocationConfig: InvocationConfig
    name: str
    recentScheduledExecutionRecords: _list[ScheduledExecutionRecord]
    releaseConfig: str
    timeZone: str
    updateTime: str

@typing.type_check_only
class WorkflowInvocation(typing_extensions.TypedDict, total=False):
    compilationResult: str
    dataEncryptionState: DataEncryptionState
    invocationConfig: InvocationConfig
    invocationTiming: Interval
    name: str
    resolvedCompilationResult: str
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
    notebookAction: NotebookAction
    state: typing_extensions.Literal[
        "PENDING", "RUNNING", "SKIPPED", "DISABLED", "SUCCEEDED", "CANCELLED", "FAILED"
    ]
    target: Target

@typing.type_check_only
class Workspace(typing_extensions.TypedDict, total=False):
    createTime: str
    dataEncryptionState: DataEncryptionState
    name: str

@typing.type_check_only
class WorkspaceCompilationOverrides(typing_extensions.TypedDict, total=False):
    defaultDatabase: str
    schemaSuffix: str
    tablePrefix: str

@typing.type_check_only
class WriteFile(typing_extensions.TypedDict, total=False):
    contents: str

@typing.type_check_only
class WriteFileRequest(typing_extensions.TypedDict, total=False):
    contents: str
    path: str

@typing.type_check_only
class WriteFileResponse(typing_extensions.TypedDict, total=False): ...
