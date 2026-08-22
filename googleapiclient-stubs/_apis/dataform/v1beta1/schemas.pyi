import typing

_list = list

@typing.type_check_only
class ActionErrorTable(typing.TypedDict, total=False):
    retentionDays: int
    target: Target

@typing.type_check_only
class ActionIncrementalLoadMode(typing.TypedDict, total=False):
    column: str

@typing.type_check_only
class ActionLoadConfig(typing.TypedDict, total=False):
    append: ActionSimpleLoadMode
    maximum: ActionIncrementalLoadMode
    replace: ActionSimpleLoadMode
    unique: ActionIncrementalLoadMode

@typing.type_check_only
class ActionSimpleLoadMode(typing.TypedDict, total=False): ...

@typing.type_check_only
class ActionSqlDefinition(typing.TypedDict, total=False):
    errorTable: ActionErrorTable
    loadConfig: ActionLoadConfig
    query: str

@typing.type_check_only
class Assertion(typing.TypedDict, total=False):
    dependencyTargets: _list[Target]
    disabled: bool
    parentAction: Target
    relationDescriptor: RelationDescriptor
    selectQuery: str
    tags: _list[str]

@typing.type_check_only
class BigQueryAction(typing.TypedDict, total=False):
    jobId: str
    sqlScript: str

@typing.type_check_only
class Binding(typing.TypedDict, total=False):
    condition: Expr
    members: _list[str]
    role: str

@typing.type_check_only
class CancelOperationRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class CancelWorkflowInvocationRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class CancelWorkflowInvocationResponse(typing.TypedDict, total=False): ...

@typing.type_check_only
class CodeCompilationConfig(typing.TypedDict, total=False):
    assertionSchema: str
    builtinAssertionNamePrefix: str
    databaseSuffix: str
    defaultDatabase: str
    defaultLocation: str
    defaultNotebookRuntimeOptions: NotebookRuntimeOptions
    defaultSchema: str
    pipelineConfig: PipelineConfig
    schemaSuffix: str
    tablePrefix: str
    vars: dict[str, typing.Any]

@typing.type_check_only
class ColumnDescriptor(typing.TypedDict, total=False):
    bigqueryPolicyTags: _list[str]
    description: str
    path: _list[str]

@typing.type_check_only
class CommitAuthor(typing.TypedDict, total=False):
    emailAddress: str
    name: str

@typing.type_check_only
class CommitLogEntry(typing.TypedDict, total=False):
    author: CommitAuthor
    commitMessage: str
    commitSha: str
    commitTime: str

@typing.type_check_only
class CommitMetadata(typing.TypedDict, total=False):
    author: CommitAuthor
    commitMessage: str

@typing.type_check_only
class CommitRepositoryChangesRequest(typing.TypedDict, total=False):
    commitMetadata: CommitMetadata
    fileOperations: dict[str, typing.Any]
    requiredHeadCommitSha: str

@typing.type_check_only
class CommitRepositoryChangesResponse(typing.TypedDict, total=False):
    commitSha: str

@typing.type_check_only
class CommitWorkspaceChangesRequest(typing.TypedDict, total=False):
    author: CommitAuthor
    commitMessage: str
    paths: _list[str]

@typing.type_check_only
class CommitWorkspaceChangesResponse(typing.TypedDict, total=False): ...

@typing.type_check_only
class CompilationError(typing.TypedDict, total=False):
    actionTarget: Target
    message: str
    path: str
    stack: str

@typing.type_check_only
class CompilationResult(typing.TypedDict, total=False):
    codeCompilationConfig: CodeCompilationConfig
    compilationErrors: _list[CompilationError]
    createTime: str
    dataEncryptionState: DataEncryptionState
    dataformCoreVersion: str
    gcsRepositorySnapshotMetadata: GcsRepositorySnapshotMetadata
    gitCommitish: str
    internalMetadata: str
    name: str
    privateResourceMetadata: PrivateResourceMetadata
    releaseConfig: str
    resolvedGitCommitSha: str
    workspace: str

@typing.type_check_only
class CompilationResultAction(typing.TypedDict, total=False):
    assertion: Assertion
    canonicalTarget: Target
    dataPreparation: DataPreparation
    declaration: Declaration
    filePath: str
    internalMetadata: str
    notebook: Notebook
    operations: Operations
    relation: Relation
    target: Target

@typing.type_check_only
class ComputeRepositoryAccessTokenStatusResponse(typing.TypedDict, total=False):
    tokenStatus: typing.Literal[
        "TOKEN_STATUS_UNSPECIFIED", "NOT_FOUND", "INVALID", "VALID", "PERMISSION_DENIED"
    ]

@typing.type_check_only
class Config(typing.TypedDict, total=False):
    defaultKmsKeyName: str
    internalMetadata: str
    name: str

@typing.type_check_only
class DataEncryptionState(typing.TypedDict, total=False):
    kmsKeyVersionName: str

@typing.type_check_only
class DataPreparation(typing.TypedDict, total=False):
    contentsSql: SqlDefinition
    contentsYaml: str
    dependencyTargets: _list[Target]
    disabled: bool
    tags: _list[str]

@typing.type_check_only
class DataPreparationAction(typing.TypedDict, total=False):
    contentsSql: ActionSqlDefinition
    contentsYaml: str
    generatedSql: str
    jobId: str

@typing.type_check_only
class Declaration(typing.TypedDict, total=False):
    relationDescriptor: RelationDescriptor

@typing.type_check_only
class DeleteFile(typing.TypedDict, total=False): ...

@typing.type_check_only
class DeleteFolderTreeRequest(typing.TypedDict, total=False):
    force: bool

@typing.type_check_only
class DeleteRepositoryLongRunningRequest(typing.TypedDict, total=False):
    force: bool

@typing.type_check_only
class DeleteTeamFolderTreeRequest(typing.TypedDict, total=False):
    force: bool

@typing.type_check_only
class DirectoryEntry(typing.TypedDict, total=False):
    directory: str
    file: str
    metadata: FilesystemEntryMetadata

@typing.type_check_only
class DirectorySearchResult(typing.TypedDict, total=False):
    path: str

@typing.type_check_only
class Empty(typing.TypedDict, total=False): ...

@typing.type_check_only
class ErrorTable(typing.TypedDict, total=False):
    retentionDays: int
    target: Target

@typing.type_check_only
class Expr(typing.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str

@typing.type_check_only
class FetchFileDiffResponse(typing.TypedDict, total=False):
    formattedDiff: str

@typing.type_check_only
class FetchFileGitStatusesResponse(typing.TypedDict, total=False):
    uncommittedFileChanges: _list[UncommittedFileChange]

@typing.type_check_only
class FetchGitAheadBehindResponse(typing.TypedDict, total=False):
    commitsAhead: int
    commitsBehind: int

@typing.type_check_only
class FetchRemoteBranchesResponse(typing.TypedDict, total=False):
    branches: _list[str]

@typing.type_check_only
class FetchRepositoryHistoryResponse(typing.TypedDict, total=False):
    commits: _list[CommitLogEntry]
    nextPageToken: str

@typing.type_check_only
class FileOperation(typing.TypedDict, total=False):
    deleteFile: DeleteFile
    writeFile: WriteFile

@typing.type_check_only
class FileSearchResult(typing.TypedDict, total=False):
    path: str

@typing.type_check_only
class FilesystemEntryMetadata(typing.TypedDict, total=False):
    sizeBytes: str
    updateTime: str

@typing.type_check_only
class Folder(typing.TypedDict, total=False):
    containingFolder: str
    createTime: str
    creatorIamPrincipal: str
    displayName: str
    internalMetadata: str
    name: str
    teamFolderName: str
    updateTime: str

@typing.type_check_only
class FolderContentsEntry(typing.TypedDict, total=False):
    folder: Folder
    repository: Repository

@typing.type_check_only
class GcsRepositorySnapshotDestination(typing.TypedDict, total=False):
    repositorySnapshotUri: str

@typing.type_check_only
class GcsRepositorySnapshotMetadata(typing.TypedDict, total=False):
    crc32cChecksum: str
    generation: str
    repositorySnapshotUri: str

@typing.type_check_only
class GitRemoteSettings(typing.TypedDict, total=False):
    authenticationTokenSecretVersion: str
    defaultBranch: str
    effectiveDefaultBranch: str
    gitRepositoryLink: str
    sshAuthenticationConfig: SshAuthenticationConfig
    tokenStatus: typing.Literal[
        "TOKEN_STATUS_UNSPECIFIED", "NOT_FOUND", "INVALID", "VALID"
    ]
    url: str

@typing.type_check_only
class IamPolicyOverrideView(typing.TypedDict, total=False):
    iamPolicyName: PolicyName
    isActive: bool

@typing.type_check_only
class IncrementalLoadMode(typing.TypedDict, total=False):
    column: str

@typing.type_check_only
class IncrementalTableConfig(typing.TypedDict, total=False):
    incrementalPostOperations: _list[str]
    incrementalPreOperations: _list[str]
    incrementalSelectQuery: str
    refreshDisabled: bool
    uniqueKeyParts: _list[str]
    updatePartitionFilter: str

@typing.type_check_only
class InstallNpmPackagesRequest(typing.TypedDict, total=False):
    pipelineConfig: PipelineConfig

@typing.type_check_only
class InstallNpmPackagesResponse(typing.TypedDict, total=False): ...

@typing.type_check_only
class Interval(typing.TypedDict, total=False):
    endTime: str
    startTime: str

@typing.type_check_only
class InvocationConfig(typing.TypedDict, total=False):
    fullyRefreshIncrementalTablesEnabled: bool
    includedTags: _list[str]
    includedTargets: _list[Target]
    queryPriority: typing.Literal["QUERY_PRIORITY_UNSPECIFIED", "INTERACTIVE", "BATCH"]
    serviceAccount: str
    transitiveDependenciesIncluded: bool
    transitiveDependentsIncluded: bool

@typing.type_check_only
class ListCompilationResultsResponse(typing.TypedDict, total=False):
    compilationResults: _list[CompilationResult]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListLocationsResponse(typing.TypedDict, total=False):
    locations: _list[Location]
    nextPageToken: str

@typing.type_check_only
class ListOperationsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    operations: _list[Operation]
    unreachable: _list[str]

@typing.type_check_only
class ListReleaseConfigsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    releaseConfigs: _list[ReleaseConfig]
    unreachable: _list[str]

@typing.type_check_only
class ListRepositoriesResponse(typing.TypedDict, total=False):
    nextPageToken: str
    repositories: _list[Repository]
    unreachable: _list[str]

@typing.type_check_only
class ListWorkflowConfigsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    unreachable: _list[str]
    workflowConfigs: _list[WorkflowConfig]

@typing.type_check_only
class ListWorkflowInvocationsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    unreachable: _list[str]
    workflowInvocations: _list[WorkflowInvocation]

@typing.type_check_only
class ListWorkspacesResponse(typing.TypedDict, total=False):
    nextPageToken: str
    unreachable: _list[str]
    workspaces: _list[Workspace]

@typing.type_check_only
class LoadConfig(typing.TypedDict, total=False):
    append: SimpleLoadMode
    maximum: IncrementalLoadMode
    replace: SimpleLoadMode
    unique: IncrementalLoadMode

@typing.type_check_only
class Location(typing.TypedDict, total=False):
    displayName: str
    labels: dict[str, typing.Any]
    locationId: str
    metadata: dict[str, typing.Any]
    name: str

@typing.type_check_only
class MakeDirectoryRequest(typing.TypedDict, total=False):
    path: str

@typing.type_check_only
class MakeDirectoryResponse(typing.TypedDict, total=False): ...

@typing.type_check_only
class MoveDirectoryRequest(typing.TypedDict, total=False):
    newPath: str
    path: str

@typing.type_check_only
class MoveDirectoryResponse(typing.TypedDict, total=False): ...

@typing.type_check_only
class MoveFileRequest(typing.TypedDict, total=False):
    newPath: str
    path: str

@typing.type_check_only
class MoveFileResponse(typing.TypedDict, total=False): ...

@typing.type_check_only
class MoveFolderRequest(typing.TypedDict, total=False):
    destinationContainingFolder: str

@typing.type_check_only
class MoveRepositoryRequest(typing.TypedDict, total=False):
    destinationContainingFolder: str

@typing.type_check_only
class Notebook(typing.TypedDict, total=False):
    contents: str
    dependencyTargets: _list[Target]
    disabled: bool
    tags: _list[str]

@typing.type_check_only
class NotebookAction(typing.TypedDict, total=False):
    contents: str
    filePath: str
    jobId: str

@typing.type_check_only
class NotebookRuntimeOptions(typing.TypedDict, total=False):
    aiPlatformNotebookRuntimeTemplate: str
    gcsOutputBucket: str
    gcsRepositorySnapshotDestination: GcsRepositorySnapshotDestination

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
    cancelRequested: bool
    createTime: str
    endTime: str
    statusDetail: str
    target: str
    verb: str

@typing.type_check_only
class Operations(typing.TypedDict, total=False):
    dependencyTargets: _list[Target]
    disabled: bool
    hasOutput: bool
    queries: _list[str]
    relationDescriptor: RelationDescriptor
    tags: _list[str]

@typing.type_check_only
class PipelineConfig(typing.TypedDict, total=False):
    path: str
    pipelineType: typing.Literal[
        "PIPELINE_TYPE_UNSPECIFIED", "DATAFORM", "SQL", "NOTEBOOK"
    ]

@typing.type_check_only
class Policy(typing.TypedDict, total=False):
    bindings: _list[Binding]
    etag: str
    version: int

@typing.type_check_only
class PolicyName(typing.TypedDict, total=False):
    id: str
    region: str
    type: str

@typing.type_check_only
class PrivateResourceMetadata(typing.TypedDict, total=False):
    userScoped: bool

@typing.type_check_only
class PullGitCommitsRequest(typing.TypedDict, total=False):
    author: CommitAuthor
    remoteBranch: str

@typing.type_check_only
class PullGitCommitsResponse(typing.TypedDict, total=False): ...

@typing.type_check_only
class PushGitCommitsRequest(typing.TypedDict, total=False):
    remoteBranch: str

@typing.type_check_only
class PushGitCommitsResponse(typing.TypedDict, total=False): ...

@typing.type_check_only
class QueryCompilationResultActionsResponse(typing.TypedDict, total=False):
    compilationResultActions: _list[CompilationResultAction]
    nextPageToken: str

@typing.type_check_only
class QueryDirectoryContentsResponse(typing.TypedDict, total=False):
    directoryEntries: _list[DirectoryEntry]
    nextPageToken: str

@typing.type_check_only
class QueryFolderContentsResponse(typing.TypedDict, total=False):
    entries: _list[FolderContentsEntry]
    nextPageToken: str

@typing.type_check_only
class QueryRepositoryDirectoryContentsResponse(typing.TypedDict, total=False):
    directoryEntries: _list[DirectoryEntry]
    nextPageToken: str

@typing.type_check_only
class QueryTeamFolderContentsResponse(typing.TypedDict, total=False):
    entries: _list[TeamFolderContentsEntry]
    nextPageToken: str

@typing.type_check_only
class QueryUserRootContentsResponse(typing.TypedDict, total=False):
    entries: _list[RootContentsEntry]
    nextPageToken: str

@typing.type_check_only
class QueryWorkflowInvocationActionsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    workflowInvocationActions: _list[WorkflowInvocationAction]

@typing.type_check_only
class ReadFileResponse(typing.TypedDict, total=False):
    fileContents: str

@typing.type_check_only
class ReadRepositoryFileResponse(typing.TypedDict, total=False):
    contents: str

@typing.type_check_only
class Relation(typing.TypedDict, total=False):
    additionalOptions: dict[str, typing.Any]
    clusterExpressions: _list[str]
    connection: str
    dependencyTargets: _list[Target]
    disabled: bool
    fileFormat: typing.Literal["FILE_FORMAT_UNSPECIFIED", "PARQUET"]
    incrementalTableConfig: IncrementalTableConfig
    partitionExpirationDays: int
    partitionExpression: str
    postOperations: _list[str]
    preOperations: _list[str]
    relationDescriptor: RelationDescriptor
    relationType: typing.Literal[
        "RELATION_TYPE_UNSPECIFIED",
        "TABLE",
        "VIEW",
        "INCREMENTAL_TABLE",
        "MATERIALIZED_VIEW",
    ]
    requirePartitionFilter: bool
    selectQuery: str
    storageUri: str
    tableFormat: typing.Literal["TABLE_FORMAT_UNSPECIFIED", "ICEBERG"]
    tags: _list[str]

@typing.type_check_only
class RelationDescriptor(typing.TypedDict, total=False):
    bigqueryLabels: dict[str, typing.Any]
    columns: _list[ColumnDescriptor]
    description: str

@typing.type_check_only
class ReleaseConfig(typing.TypedDict, total=False):
    codeCompilationConfig: CodeCompilationConfig
    cronSchedule: str
    disabled: bool
    gitCommitish: str
    internalMetadata: str
    name: str
    recentScheduledReleaseRecords: _list[ScheduledReleaseRecord]
    releaseCompilationResult: str
    timeZone: str

@typing.type_check_only
class RemoveDirectoryRequest(typing.TypedDict, total=False):
    path: str

@typing.type_check_only
class RemoveDirectoryResponse(typing.TypedDict, total=False): ...

@typing.type_check_only
class RemoveFileRequest(typing.TypedDict, total=False):
    path: str

@typing.type_check_only
class RemoveFileResponse(typing.TypedDict, total=False): ...

@typing.type_check_only
class Repository(typing.TypedDict, total=False):
    containingFolder: str
    createTime: str
    dataEncryptionState: DataEncryptionState
    displayName: str
    gitRemoteSettings: GitRemoteSettings
    internalMetadata: str
    kmsKeyName: str
    labels: dict[str, typing.Any]
    name: str
    npmrcEnvironmentVariablesSecretVersion: str
    serviceAccount: str
    setAuthenticatedUserAdmin: bool
    teamFolderName: str
    workspaceCompilationOverrides: WorkspaceCompilationOverrides

@typing.type_check_only
class ResetWorkspaceChangesRequest(typing.TypedDict, total=False):
    clean: bool
    paths: _list[str]

@typing.type_check_only
class ResetWorkspaceChangesResponse(typing.TypedDict, total=False): ...

@typing.type_check_only
class RootContentsEntry(typing.TypedDict, total=False):
    folder: Folder
    repository: Repository

@typing.type_check_only
class ScheduledExecutionRecord(typing.TypedDict, total=False):
    errorStatus: Status
    executionTime: str
    workflowInvocation: str

@typing.type_check_only
class ScheduledReleaseRecord(typing.TypedDict, total=False):
    compilationResult: str
    errorStatus: Status
    releaseTime: str

@typing.type_check_only
class SearchFilesResponse(typing.TypedDict, total=False):
    nextPageToken: str
    searchResults: _list[SearchResult]

@typing.type_check_only
class SearchResult(typing.TypedDict, total=False):
    directory: DirectorySearchResult
    file: FileSearchResult

@typing.type_check_only
class SearchTeamFoldersResponse(typing.TypedDict, total=False):
    nextPageToken: str
    results: _list[TeamFolderSearchResult]

@typing.type_check_only
class SetIamPolicyRequest(typing.TypedDict, total=False):
    policy: Policy

@typing.type_check_only
class SimpleLoadMode(typing.TypedDict, total=False): ...

@typing.type_check_only
class SqlDefinition(typing.TypedDict, total=False):
    errorTable: ErrorTable
    load: LoadConfig
    query: str

@typing.type_check_only
class SshAuthenticationConfig(typing.TypedDict, total=False):
    hostPublicKey: str
    userPrivateKeySecretVersion: str

@typing.type_check_only
class Status(typing.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class TableUpdateTrigger(typing.TypedDict, total=False):
    table: Target
    triggerUpdateTime: str

@typing.type_check_only
class Target(typing.TypedDict, total=False):
    database: str
    name: str
    schema: str

@typing.type_check_only
class TeamFolder(typing.TypedDict, total=False):
    createTime: str
    creatorIamPrincipal: str
    displayName: str
    internalMetadata: str
    name: str
    updateTime: str

@typing.type_check_only
class TeamFolderContentsEntry(typing.TypedDict, total=False):
    folder: Folder
    repository: Repository

@typing.type_check_only
class TeamFolderSearchResult(typing.TypedDict, total=False):
    teamFolder: TeamFolder

@typing.type_check_only
class TestIamPermissionsRequest(typing.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class TestIamPermissionsResponse(typing.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class TriggerEvaluationRecord(typing.TypedDict, total=False):
    evaluationTime: str
    status: Status

@typing.type_check_only
class UncommittedFileChange(typing.TypedDict, total=False):
    path: str
    state: typing.Literal[
        "STATE_UNSPECIFIED", "ADDED", "DELETED", "MODIFIED", "HAS_CONFLICTS"
    ]

@typing.type_check_only
class WorkflowConfig(typing.TypedDict, total=False):
    createTime: str
    cronSchedule: str
    disabled: bool
    internalMetadata: str
    invocationConfig: InvocationConfig
    name: str
    recentScheduledExecutionRecords: _list[ScheduledExecutionRecord]
    releaseConfig: str
    timeZone: str
    updateTime: str
    workflowTriggerConfig: WorkflowTriggerConfig

@typing.type_check_only
class WorkflowInvocation(typing.TypedDict, total=False):
    compilationResult: str
    dataEncryptionState: DataEncryptionState
    internalMetadata: str
    invocationConfig: InvocationConfig
    invocationTiming: Interval
    name: str
    pipelineConfig: PipelineConfig
    privateResourceMetadata: PrivateResourceMetadata
    resolvedCompilationResult: str
    state: typing.Literal[
        "STATE_UNSPECIFIED", "RUNNING", "SUCCEEDED", "CANCELLED", "FAILED", "CANCELING"
    ]
    workflowConfig: str

@typing.type_check_only
class WorkflowInvocationAction(typing.TypedDict, total=False):
    bigqueryAction: BigQueryAction
    canonicalTarget: Target
    dataPreparationAction: DataPreparationAction
    failureReason: str
    internalMetadata: str
    invocationTiming: Interval
    notebookAction: NotebookAction
    state: typing.Literal[
        "PENDING", "RUNNING", "SKIPPED", "DISABLED", "SUCCEEDED", "CANCELLED", "FAILED"
    ]
    target: Target

@typing.type_check_only
class WorkflowTrigger(typing.TypedDict, total=False):
    tableUpdateTrigger: TableUpdateTrigger

@typing.type_check_only
class WorkflowTriggerConfig(typing.TypedDict, total=False):
    condition: typing.Literal["CONDITION_UNSPECIFIED", "ALL", "ANY"]
    lastSuccessfulEvaluationTime: str
    maxWaitDuration: str
    minExecutionDuration: str
    recentTriggerEvaluationRecords: _list[TriggerEvaluationRecord]
    workflowTriggers: _list[WorkflowTrigger]

@typing.type_check_only
class Workspace(typing.TypedDict, total=False):
    createTime: str
    dataEncryptionState: DataEncryptionState
    disableMoves: bool
    internalMetadata: str
    name: str
    privateResourceMetadata: PrivateResourceMetadata

@typing.type_check_only
class WorkspaceCompilationOverrides(typing.TypedDict, total=False):
    defaultDatabase: str
    schemaSuffix: str
    tablePrefix: str

@typing.type_check_only
class WriteFile(typing.TypedDict, total=False):
    contents: str

@typing.type_check_only
class WriteFileRequest(typing.TypedDict, total=False):
    contents: str
    path: str

@typing.type_check_only
class WriteFileResponse(typing.TypedDict, total=False): ...
