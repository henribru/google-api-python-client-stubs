import collections.abc
import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

_list = list

@typing.type_check_only
class DataformResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class ProjectsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class LocationsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class RepositoriesResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class CompilationResultsResource(googleapiclient.discovery.Resource):
                    def create(
                        self,
                        *,
                        parent: str,
                        body: CompilationResult = ...,
                        **kwargs: typing.Any
                    ) -> CompilationResultHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> CompilationResultHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any
                    ) -> ListCompilationResultsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: ListCompilationResultsResponseHttpRequest,
                        previous_response: ListCompilationResultsResponse,
                    ) -> ListCompilationResultsResponseHttpRequest | None: ...
                    def query(
                        self,
                        *,
                        name: str,
                        filter: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any
                    ) -> QueryCompilationResultActionsResponseHttpRequest: ...
                    def query_next(
                        self,
                        previous_request: QueryCompilationResultActionsResponseHttpRequest,
                        previous_response: QueryCompilationResultActionsResponse,
                    ) -> QueryCompilationResultActionsResponseHttpRequest | None: ...

                @typing.type_check_only
                class ReleaseConfigsResource(googleapiclient.discovery.Resource):
                    def create(
                        self,
                        *,
                        parent: str,
                        body: ReleaseConfig = ...,
                        releaseConfigId: str = ...,
                        **kwargs: typing.Any
                    ) -> ReleaseConfigHttpRequest: ...
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> EmptyHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> ReleaseConfigHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any
                    ) -> ListReleaseConfigsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: ListReleaseConfigsResponseHttpRequest,
                        previous_response: ListReleaseConfigsResponse,
                    ) -> ListReleaseConfigsResponseHttpRequest | None: ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: ReleaseConfig = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any
                    ) -> ReleaseConfigHttpRequest: ...

                @typing.type_check_only
                class WorkflowConfigsResource(googleapiclient.discovery.Resource):
                    def create(
                        self,
                        *,
                        parent: str,
                        body: WorkflowConfig = ...,
                        workflowConfigId: str = ...,
                        **kwargs: typing.Any
                    ) -> WorkflowConfigHttpRequest: ...
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> EmptyHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> WorkflowConfigHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any
                    ) -> ListWorkflowConfigsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: ListWorkflowConfigsResponseHttpRequest,
                        previous_response: ListWorkflowConfigsResponse,
                    ) -> ListWorkflowConfigsResponseHttpRequest | None: ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: WorkflowConfig = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any
                    ) -> WorkflowConfigHttpRequest: ...

                @typing.type_check_only
                class WorkflowInvocationsResource(googleapiclient.discovery.Resource):
                    def cancel(
                        self,
                        *,
                        name: str,
                        body: CancelWorkflowInvocationRequest = ...,
                        **kwargs: typing.Any
                    ) -> EmptyHttpRequest: ...
                    def create(
                        self,
                        *,
                        parent: str,
                        body: WorkflowInvocation = ...,
                        **kwargs: typing.Any
                    ) -> WorkflowInvocationHttpRequest: ...
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> EmptyHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> WorkflowInvocationHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str = ...,
                        orderBy: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any
                    ) -> ListWorkflowInvocationsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: ListWorkflowInvocationsResponseHttpRequest,
                        previous_response: ListWorkflowInvocationsResponse,
                    ) -> ListWorkflowInvocationsResponseHttpRequest | None: ...
                    def query(
                        self,
                        *,
                        name: str,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any
                    ) -> QueryWorkflowInvocationActionsResponseHttpRequest: ...
                    def query_next(
                        self,
                        previous_request: QueryWorkflowInvocationActionsResponseHttpRequest,
                        previous_response: QueryWorkflowInvocationActionsResponse,
                    ) -> QueryWorkflowInvocationActionsResponseHttpRequest | None: ...

                @typing.type_check_only
                class WorkspacesResource(googleapiclient.discovery.Resource):
                    def commit(
                        self,
                        *,
                        name: str,
                        body: CommitWorkspaceChangesRequest = ...,
                        **kwargs: typing.Any
                    ) -> EmptyHttpRequest: ...
                    def create(
                        self,
                        *,
                        parent: str,
                        body: Workspace = ...,
                        workspaceId: str = ...,
                        **kwargs: typing.Any
                    ) -> WorkspaceHttpRequest: ...
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> EmptyHttpRequest: ...
                    def fetchFileDiff(
                        self, *, workspace: str, path: str = ..., **kwargs: typing.Any
                    ) -> FetchFileDiffResponseHttpRequest: ...
                    def fetchFileGitStatuses(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> FetchFileGitStatusesResponseHttpRequest: ...
                    def fetchGitAheadBehind(
                        self,
                        *,
                        name: str,
                        remoteBranch: str = ...,
                        **kwargs: typing.Any
                    ) -> FetchGitAheadBehindResponseHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> WorkspaceHttpRequest: ...
                    def installNpmPackages(
                        self,
                        *,
                        workspace: str,
                        body: InstallNpmPackagesRequest = ...,
                        **kwargs: typing.Any
                    ) -> InstallNpmPackagesResponseHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str = ...,
                        orderBy: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any
                    ) -> ListWorkspacesResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: ListWorkspacesResponseHttpRequest,
                        previous_response: ListWorkspacesResponse,
                    ) -> ListWorkspacesResponseHttpRequest | None: ...
                    def makeDirectory(
                        self,
                        *,
                        workspace: str,
                        body: MakeDirectoryRequest = ...,
                        **kwargs: typing.Any
                    ) -> MakeDirectoryResponseHttpRequest: ...
                    def moveDirectory(
                        self,
                        *,
                        workspace: str,
                        body: MoveDirectoryRequest = ...,
                        **kwargs: typing.Any
                    ) -> MoveDirectoryResponseHttpRequest: ...
                    def moveFile(
                        self,
                        *,
                        workspace: str,
                        body: MoveFileRequest = ...,
                        **kwargs: typing.Any
                    ) -> MoveFileResponseHttpRequest: ...
                    def pull(
                        self,
                        *,
                        name: str,
                        body: PullGitCommitsRequest = ...,
                        **kwargs: typing.Any
                    ) -> EmptyHttpRequest: ...
                    def push(
                        self,
                        *,
                        name: str,
                        body: PushGitCommitsRequest = ...,
                        **kwargs: typing.Any
                    ) -> EmptyHttpRequest: ...
                    def queryDirectoryContents(
                        self,
                        *,
                        workspace: str,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        path: str = ...,
                        **kwargs: typing.Any
                    ) -> QueryDirectoryContentsResponseHttpRequest: ...
                    def queryDirectoryContents_next(
                        self,
                        previous_request: QueryDirectoryContentsResponseHttpRequest,
                        previous_response: QueryDirectoryContentsResponse,
                    ) -> QueryDirectoryContentsResponseHttpRequest | None: ...
                    def readFile(
                        self, *, workspace: str, path: str = ..., **kwargs: typing.Any
                    ) -> ReadFileResponseHttpRequest: ...
                    def removeDirectory(
                        self,
                        *,
                        workspace: str,
                        body: RemoveDirectoryRequest = ...,
                        **kwargs: typing.Any
                    ) -> EmptyHttpRequest: ...
                    def removeFile(
                        self,
                        *,
                        workspace: str,
                        body: RemoveFileRequest = ...,
                        **kwargs: typing.Any
                    ) -> EmptyHttpRequest: ...
                    def reset(
                        self,
                        *,
                        name: str,
                        body: ResetWorkspaceChangesRequest = ...,
                        **kwargs: typing.Any
                    ) -> EmptyHttpRequest: ...
                    def writeFile(
                        self,
                        *,
                        workspace: str,
                        body: WriteFileRequest = ...,
                        **kwargs: typing.Any
                    ) -> WriteFileResponseHttpRequest: ...

                def create(
                    self,
                    *,
                    parent: str,
                    body: Repository = ...,
                    repositoryId: str = ...,
                    **kwargs: typing.Any
                ) -> RepositoryHttpRequest: ...
                def delete(
                    self, *, name: str, force: bool = ..., **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def fetchRemoteBranches(
                    self, *, name: str, **kwargs: typing.Any
                ) -> FetchRemoteBranchesResponseHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> RepositoryHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> ListRepositoriesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListRepositoriesResponseHttpRequest,
                    previous_response: ListRepositoriesResponse,
                ) -> ListRepositoriesResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: Repository = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any
                ) -> RepositoryHttpRequest: ...
                def compilationResults(self) -> CompilationResultsResource: ...
                def releaseConfigs(self) -> ReleaseConfigsResource: ...
                def workflowConfigs(self) -> WorkflowConfigsResource: ...
                def workflowInvocations(self) -> WorkflowInvocationsResource: ...
                def workspaces(self) -> WorkspacesResource: ...

            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> LocationHttpRequest: ...
            def list(
                self,
                *,
                name: str,
                filter: str = ...,
                includeUnrevealedLocations: bool = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> ListLocationsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListLocationsResponseHttpRequest,
                previous_response: ListLocationsResponse,
            ) -> ListLocationsResponseHttpRequest | None: ...
            def repositories(self) -> RepositoriesResource: ...

        def locations(self) -> LocationsResource: ...

    def new_batch_http_request(
        self,
        callback: collections.abc.Callable[
            [
                str,
                googleapiclient.http.HttpRequest,
                googleapiclient.errors.HttpError | None,
            ],
            typing.Any,
        ]
        | None = ...,
    ) -> googleapiclient.http.BatchHttpRequest: ...
    def projects(self) -> ProjectsResource: ...

@typing.type_check_only
class CompilationResultHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> CompilationResult: ...

@typing.type_check_only
class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Empty: ...

@typing.type_check_only
class FetchFileDiffResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> FetchFileDiffResponse: ...

@typing.type_check_only
class FetchFileGitStatusesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> FetchFileGitStatusesResponse: ...

@typing.type_check_only
class FetchGitAheadBehindResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> FetchGitAheadBehindResponse: ...

@typing.type_check_only
class FetchRemoteBranchesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> FetchRemoteBranchesResponse: ...

@typing.type_check_only
class InstallNpmPackagesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> InstallNpmPackagesResponse: ...

@typing.type_check_only
class ListCompilationResultsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListCompilationResultsResponse: ...

@typing.type_check_only
class ListLocationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListLocationsResponse: ...

@typing.type_check_only
class ListReleaseConfigsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListReleaseConfigsResponse: ...

@typing.type_check_only
class ListRepositoriesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListRepositoriesResponse: ...

@typing.type_check_only
class ListWorkflowConfigsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListWorkflowConfigsResponse: ...

@typing.type_check_only
class ListWorkflowInvocationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListWorkflowInvocationsResponse: ...

@typing.type_check_only
class ListWorkspacesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListWorkspacesResponse: ...

@typing.type_check_only
class LocationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Location: ...

@typing.type_check_only
class MakeDirectoryResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> MakeDirectoryResponse: ...

@typing.type_check_only
class MoveDirectoryResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> MoveDirectoryResponse: ...

@typing.type_check_only
class MoveFileResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> MoveFileResponse: ...

@typing.type_check_only
class QueryCompilationResultActionsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> QueryCompilationResultActionsResponse: ...

@typing.type_check_only
class QueryDirectoryContentsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> QueryDirectoryContentsResponse: ...

@typing.type_check_only
class QueryWorkflowInvocationActionsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> QueryWorkflowInvocationActionsResponse: ...

@typing.type_check_only
class ReadFileResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ReadFileResponse: ...

@typing.type_check_only
class ReleaseConfigHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ReleaseConfig: ...

@typing.type_check_only
class RepositoryHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Repository: ...

@typing.type_check_only
class WorkflowConfigHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> WorkflowConfig: ...

@typing.type_check_only
class WorkflowInvocationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> WorkflowInvocation: ...

@typing.type_check_only
class WorkspaceHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Workspace: ...

@typing.type_check_only
class WriteFileResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> WriteFileResponse: ...
