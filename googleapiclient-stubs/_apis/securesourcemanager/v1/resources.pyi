import collections.abc
import typing

import httplib2
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http

from .schemas import *

_list = list

@typing.type_check_only
class SecureSourceManagerResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class ProjectsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class LocationsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class InstancesResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: Instance = ...,
                    instanceId: str = ...,
                    requestId: str = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def delete(
                    self, *, name: str, requestId: str = ..., **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> InstanceHttpRequest: ...
                def getIamPolicy(
                    self,
                    *,
                    resource: str,
                    options_requestedPolicyVersion: int = ...,
                    **kwargs: typing.Any,
                ) -> PolicyHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> ListInstancesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListInstancesResponseHttpRequest,
                    previous_response: ListInstancesResponse,
                ) -> ListInstancesResponseHttpRequest | None: ...
                def setIamPolicy(
                    self,
                    *,
                    resource: str,
                    body: SetIamPolicyRequest = ...,
                    **kwargs: typing.Any,
                ) -> PolicyHttpRequest: ...
                def testIamPermissions(
                    self,
                    *,
                    resource: str,
                    body: TestIamPermissionsRequest = ...,
                    **kwargs: typing.Any,
                ) -> TestIamPermissionsResponseHttpRequest: ...

            @typing.type_check_only
            class OperationsResource(googleapiclient.discovery.Resource):
                def cancel(
                    self,
                    *,
                    name: str,
                    body: CancelOperationRequest = ...,
                    **kwargs: typing.Any,
                ) -> EmptyHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def list(
                    self,
                    *,
                    name: str,
                    filter: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> ListOperationsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListOperationsResponseHttpRequest,
                    previous_response: ListOperationsResponse,
                ) -> ListOperationsResponseHttpRequest | None: ...

            @typing.type_check_only
            class RepositoriesResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class BranchRulesResource(googleapiclient.discovery.Resource):
                    def create(
                        self,
                        *,
                        parent: str,
                        body: BranchRule = ...,
                        branchRuleId: str = ...,
                        **kwargs: typing.Any,
                    ) -> OperationHttpRequest: ...
                    def delete(
                        self,
                        *,
                        name: str,
                        allowMissing: bool = ...,
                        **kwargs: typing.Any,
                    ) -> OperationHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> BranchRuleHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
                    ) -> ListBranchRulesResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: ListBranchRulesResponseHttpRequest,
                        previous_response: ListBranchRulesResponse,
                    ) -> ListBranchRulesResponseHttpRequest | None: ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: BranchRule = ...,
                        updateMask: str = ...,
                        validateOnly: bool = ...,
                        **kwargs: typing.Any,
                    ) -> OperationHttpRequest: ...

                @typing.type_check_only
                class HooksResource(googleapiclient.discovery.Resource):
                    def create(
                        self,
                        *,
                        parent: str,
                        body: Hook = ...,
                        hookId: str = ...,
                        **kwargs: typing.Any,
                    ) -> OperationHttpRequest: ...
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> OperationHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> HookHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
                    ) -> ListHooksResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: ListHooksResponseHttpRequest,
                        previous_response: ListHooksResponse,
                    ) -> ListHooksResponseHttpRequest | None: ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: Hook = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any,
                    ) -> OperationHttpRequest: ...

                @typing.type_check_only
                class IssuesResource(googleapiclient.discovery.Resource):
                    @typing.type_check_only
                    class IssueCommentsResource(googleapiclient.discovery.Resource):
                        def create(
                            self,
                            *,
                            parent: str,
                            body: IssueComment = ...,
                            **kwargs: typing.Any,
                        ) -> OperationHttpRequest: ...
                        def delete(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> OperationHttpRequest: ...
                        def get(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> IssueCommentHttpRequest: ...
                        def list(
                            self,
                            *,
                            parent: str,
                            pageSize: int = ...,
                            pageToken: str = ...,
                            **kwargs: typing.Any,
                        ) -> ListIssueCommentsResponseHttpRequest: ...
                        def list_next(
                            self,
                            previous_request: ListIssueCommentsResponseHttpRequest,
                            previous_response: ListIssueCommentsResponse,
                        ) -> ListIssueCommentsResponseHttpRequest | None: ...
                        def patch(
                            self,
                            *,
                            name: str,
                            body: IssueComment = ...,
                            updateMask: str = ...,
                            **kwargs: typing.Any,
                        ) -> OperationHttpRequest: ...

                    def close(  # type: ignore[override]
                        self,
                        *,
                        name: str,
                        body: CloseIssueRequest = ...,
                        **kwargs: typing.Any,
                    ) -> OperationHttpRequest: ...
                    def create(
                        self, *, parent: str, body: Issue = ..., **kwargs: typing.Any
                    ) -> OperationHttpRequest: ...
                    def delete(
                        self, *, name: str, etag: str = ..., **kwargs: typing.Any
                    ) -> OperationHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> IssueHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
                    ) -> ListIssuesResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: ListIssuesResponseHttpRequest,
                        previous_response: ListIssuesResponse,
                    ) -> ListIssuesResponseHttpRequest | None: ...
                    def open(
                        self,
                        *,
                        name: str,
                        body: OpenIssueRequest = ...,
                        **kwargs: typing.Any,
                    ) -> OperationHttpRequest: ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: Issue = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any,
                    ) -> OperationHttpRequest: ...
                    def issueComments(self) -> IssueCommentsResource: ...

                @typing.type_check_only
                class PullRequestsResource(googleapiclient.discovery.Resource):
                    @typing.type_check_only
                    class PullRequestCommentsResource(
                        googleapiclient.discovery.Resource
                    ):
                        def batchCreate(
                            self,
                            *,
                            parent: str,
                            body: BatchCreatePullRequestCommentsRequest = ...,
                            **kwargs: typing.Any,
                        ) -> OperationHttpRequest: ...
                        def create(
                            self,
                            *,
                            parent: str,
                            body: PullRequestComment = ...,
                            **kwargs: typing.Any,
                        ) -> OperationHttpRequest: ...
                        def delete(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> OperationHttpRequest: ...
                        def get(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> PullRequestCommentHttpRequest: ...
                        def list(
                            self,
                            *,
                            parent: str,
                            pageSize: int = ...,
                            pageToken: str = ...,
                            **kwargs: typing.Any,
                        ) -> ListPullRequestCommentsResponseHttpRequest: ...
                        def list_next(
                            self,
                            previous_request: ListPullRequestCommentsResponseHttpRequest,
                            previous_response: ListPullRequestCommentsResponse,
                        ) -> ListPullRequestCommentsResponseHttpRequest | None: ...
                        def patch(
                            self,
                            *,
                            name: str,
                            body: PullRequestComment = ...,
                            updateMask: str = ...,
                            **kwargs: typing.Any,
                        ) -> OperationHttpRequest: ...
                        def resolve(
                            self,
                            *,
                            parent: str,
                            body: ResolvePullRequestCommentsRequest = ...,
                            **kwargs: typing.Any,
                        ) -> OperationHttpRequest: ...
                        def unresolve(
                            self,
                            *,
                            parent: str,
                            body: UnresolvePullRequestCommentsRequest = ...,
                            **kwargs: typing.Any,
                        ) -> OperationHttpRequest: ...

                    def close(  # type: ignore[override]
                        self,
                        *,
                        name: str,
                        body: ClosePullRequestRequest = ...,
                        **kwargs: typing.Any,
                    ) -> OperationHttpRequest: ...
                    def create(
                        self,
                        *,
                        parent: str,
                        body: PullRequest = ...,
                        **kwargs: typing.Any,
                    ) -> OperationHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> PullRequestHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
                    ) -> ListPullRequestsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: ListPullRequestsResponseHttpRequest,
                        previous_response: ListPullRequestsResponse,
                    ) -> ListPullRequestsResponseHttpRequest | None: ...
                    def listFileDiffs(
                        self,
                        *,
                        name: str,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
                    ) -> ListPullRequestFileDiffsResponseHttpRequest: ...
                    def listFileDiffs_next(
                        self,
                        previous_request: ListPullRequestFileDiffsResponseHttpRequest,
                        previous_response: ListPullRequestFileDiffsResponse,
                    ) -> ListPullRequestFileDiffsResponseHttpRequest | None: ...
                    def merge(
                        self,
                        *,
                        name: str,
                        body: MergePullRequestRequest = ...,
                        **kwargs: typing.Any,
                    ) -> OperationHttpRequest: ...
                    def open(
                        self,
                        *,
                        name: str,
                        body: OpenPullRequestRequest = ...,
                        **kwargs: typing.Any,
                    ) -> OperationHttpRequest: ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: PullRequest = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any,
                    ) -> OperationHttpRequest: ...
                    def pullRequestComments(self) -> PullRequestCommentsResource: ...

                def create(
                    self,
                    *,
                    parent: str,
                    body: Repository = ...,
                    repositoryId: str = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def delete(
                    self, *, name: str, allowMissing: bool = ..., **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def fetchBlob(
                    self, *, repository: str, sha: str = ..., **kwargs: typing.Any
                ) -> FetchBlobResponseHttpRequest: ...
                def fetchTree(
                    self,
                    *,
                    repository: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    recursive: bool = ...,
                    ref: str = ...,
                    **kwargs: typing.Any,
                ) -> FetchTreeResponseHttpRequest: ...
                def fetchTree_next(
                    self,
                    previous_request: FetchTreeResponseHttpRequest,
                    previous_response: FetchTreeResponse,
                ) -> FetchTreeResponseHttpRequest | None: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> RepositoryHttpRequest: ...
                def getIamPolicy(
                    self,
                    *,
                    resource: str,
                    options_requestedPolicyVersion: int = ...,
                    **kwargs: typing.Any,
                ) -> PolicyHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    instance: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
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
                    validateOnly: bool = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def setIamPolicy(
                    self,
                    *,
                    resource: str,
                    body: SetIamPolicyRequest = ...,
                    **kwargs: typing.Any,
                ) -> PolicyHttpRequest: ...
                def testIamPermissions(
                    self,
                    *,
                    resource: str,
                    body: TestIamPermissionsRequest = ...,
                    **kwargs: typing.Any,
                ) -> TestIamPermissionsResponseHttpRequest: ...
                def branchRules(self) -> BranchRulesResource: ...
                def hooks(self) -> HooksResource: ...
                def issues(self) -> IssuesResource: ...
                def pullRequests(self) -> PullRequestsResource: ...

            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> LocationHttpRequest: ...
            def list(
                self,
                *,
                name: str,
                extraLocationTypes: str | _list[str] = ...,
                filter: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any,
            ) -> ListLocationsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListLocationsResponseHttpRequest,
                previous_response: ListLocationsResponse,
            ) -> ListLocationsResponseHttpRequest | None: ...
            def instances(self) -> InstancesResource: ...
            def operations(self) -> OperationsResource: ...
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
        | None = None,
    ) -> googleapiclient.http.BatchHttpRequest: ...
    def projects(self) -> ProjectsResource: ...

@typing.type_check_only
class BranchRuleHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> BranchRule: ...

@typing.type_check_only
class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Empty: ...

@typing.type_check_only
class FetchBlobResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> FetchBlobResponse: ...

@typing.type_check_only
class FetchTreeResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> FetchTreeResponse: ...

@typing.type_check_only
class HookHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Hook: ...

@typing.type_check_only
class InstanceHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Instance: ...

@typing.type_check_only
class IssueHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Issue: ...

@typing.type_check_only
class IssueCommentHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> IssueComment: ...

@typing.type_check_only
class ListBranchRulesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListBranchRulesResponse: ...

@typing.type_check_only
class ListHooksResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListHooksResponse: ...

@typing.type_check_only
class ListInstancesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListInstancesResponse: ...

@typing.type_check_only
class ListIssueCommentsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListIssueCommentsResponse: ...

@typing.type_check_only
class ListIssuesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListIssuesResponse: ...

@typing.type_check_only
class ListLocationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListLocationsResponse: ...

@typing.type_check_only
class ListOperationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListOperationsResponse: ...

@typing.type_check_only
class ListPullRequestCommentsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListPullRequestCommentsResponse: ...

@typing.type_check_only
class ListPullRequestFileDiffsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListPullRequestFileDiffsResponse: ...

@typing.type_check_only
class ListPullRequestsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListPullRequestsResponse: ...

@typing.type_check_only
class ListRepositoriesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListRepositoriesResponse: ...

@typing.type_check_only
class LocationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Location: ...

@typing.type_check_only
class OperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Operation: ...

@typing.type_check_only
class PolicyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Policy: ...

@typing.type_check_only
class PullRequestHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> PullRequest: ...

@typing.type_check_only
class PullRequestCommentHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> PullRequestComment: ...

@typing.type_check_only
class RepositoryHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Repository: ...

@typing.type_check_only
class TestIamPermissionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> TestIamPermissionsResponse: ...
