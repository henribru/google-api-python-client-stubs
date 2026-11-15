import collections.abc
import typing

import httplib2

import googleapiclient.discovery
import googleapiclient.http

from .schemas import *

_list = list

@typing.type_check_only
class DeveloperConnectResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class ProjectsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class LocationsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class AccountConnectorsResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class UsersResource(googleapiclient.discovery.Resource):
                    def delete(
                        self,
                        *,
                        name: str,
                        etag: str | None = ...,
                        requestId: str | None = ...,
                        validateOnly: bool | None = ...,
                        **kwargs: typing.Any,
                    ) -> OperationHttpRequest: ...
                    def deleteSelf(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> OperationHttpRequest: ...
                    def fetchAccessToken(
                        self,
                        *,
                        accountConnector: str,
                        body: FetchAccessTokenRequest,
                        **kwargs: typing.Any,
                    ) -> FetchAccessTokenResponseHttpRequest: ...
                    def fetchSelf(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> UserHttpRequest: ...
                    def finishOAuthFlow(
                        self,
                        *,
                        accountConnector: str,
                        googleOauthParams_scopes: str | _list[str] | None = ...,
                        googleOauthParams_ticket: str | None = ...,
                        googleOauthParams_versionInfo: str | None = ...,
                        oauthParams_code: str | None = ...,
                        oauthParams_ticket: str | None = ...,
                        **kwargs: typing.Any,
                    ) -> FinishOAuthResponseHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str | None = ...,
                        orderBy: str | None = ...,
                        pageSize: int | None = ...,
                        pageToken: str | None = ...,
                        **kwargs: typing.Any,
                    ) -> ListUsersResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: ListUsersResponseHttpRequest,
                        previous_response: ListUsersResponse,
                    ) -> ListUsersResponseHttpRequest | None: ...
                    def startOAuthFlow(
                        self, *, accountConnector: str, **kwargs: typing.Any
                    ) -> StartOAuthResponseHttpRequest: ...

                def create(
                    self,
                    *,
                    parent: str,
                    body: AccountConnector,
                    accountConnectorId: str | None = ...,
                    requestId: str | None = ...,
                    validateOnly: bool | None = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def delete(
                    self,
                    *,
                    name: str,
                    etag: str | None = ...,
                    force: bool | None = ...,
                    requestId: str | None = ...,
                    validateOnly: bool | None = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def fetchUserRepositories(
                    self,
                    *,
                    accountConnector: str,
                    pageSize: int | None = ...,
                    pageToken: str | None = ...,
                    repository: str | None = ...,
                    **kwargs: typing.Any,
                ) -> FetchUserRepositoriesResponseHttpRequest: ...
                def fetchUserRepositories_next(
                    self,
                    previous_request: FetchUserRepositoriesResponseHttpRequest,
                    previous_response: FetchUserRepositoriesResponse,
                ) -> FetchUserRepositoriesResponseHttpRequest | None: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> AccountConnectorHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str | None = ...,
                    orderBy: str | None = ...,
                    pageSize: int | None = ...,
                    pageToken: str | None = ...,
                    **kwargs: typing.Any,
                ) -> ListAccountConnectorsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListAccountConnectorsResponseHttpRequest,
                    previous_response: ListAccountConnectorsResponse,
                ) -> ListAccountConnectorsResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: AccountConnector,
                    allowMissing: bool | None = ...,
                    requestId: str | None = ...,
                    updateMask: str | None = ...,
                    validateOnly: bool | None = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def users(self) -> UsersResource: ...

            @typing.type_check_only
            class ConnectionsResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class GitRepositoryLinksResource(googleapiclient.discovery.Resource):
                    def addPullRequestComment(
                        self,
                        *,
                        name: str,
                        body: AddGitRepositoryLinkPullRequestCommentRequest,
                        **kwargs: typing.Any,
                    ) -> PullRequestCommentHttpRequest: ...
                    def addPullRequestReviewComment(
                        self,
                        *,
                        name: str,
                        body: AddGitRepositoryLinkPullRequestReviewCommentRequest,
                        **kwargs: typing.Any,
                    ) -> PullRequestReviewCommentHttpRequest: ...
                    def create(
                        self,
                        *,
                        parent: str,
                        body: GitRepositoryLink,
                        gitRepositoryLinkId: str | None = ...,
                        requestId: str | None = ...,
                        validateOnly: bool | None = ...,
                        **kwargs: typing.Any,
                    ) -> OperationHttpRequest: ...
                    def delete(
                        self,
                        *,
                        name: str,
                        etag: str | None = ...,
                        requestId: str | None = ...,
                        validateOnly: bool | None = ...,
                        **kwargs: typing.Any,
                    ) -> OperationHttpRequest: ...
                    def diffCommit(
                        self,
                        *,
                        name: str,
                        baseSha: str | None = ...,
                        headSha: str | None = ...,
                        pathFilters: str | _list[str] | None = ...,
                        **kwargs: typing.Any,
                    ) -> DiffGitRepositoryLinkCommitResponseHttpRequest: ...
                    def fetchCommit(
                        self,
                        *,
                        name: str,
                        commitSha: str | None = ...,
                        pathFilters: str | _list[str] | None = ...,
                        view: typing.Literal["COMMIT_VIEW_UNSPECIFIED", "BASIC", "FULL"]
                        | None = ...,
                        **kwargs: typing.Any,
                    ) -> FetchGitRepositoryLinkCommitResponseHttpRequest: ...
                    def fetchCommitList(
                        self,
                        *,
                        name: str,
                        pageSize: int | None = ...,
                        pageToken: str | None = ...,
                        ref: str | None = ...,
                        view: typing.Literal["COMMIT_VIEW_UNSPECIFIED", "BASIC", "FULL"]
                        | None = ...,
                        **kwargs: typing.Any,
                    ) -> FetchGitRepositoryLinkCommitListResponseHttpRequest: ...
                    def fetchCommitList_next(
                        self,
                        previous_request: FetchGitRepositoryLinkCommitListResponseHttpRequest,
                        previous_response: FetchGitRepositoryLinkCommitListResponse,
                    ) -> FetchGitRepositoryLinkCommitListResponseHttpRequest | None: ...
                    def fetchFileBlame(
                        self,
                        *,
                        name: str,
                        firstLine: int | None = ...,
                        lastLine: int | None = ...,
                        path: str | None = ...,
                        ref: str | None = ...,
                        **kwargs: typing.Any,
                    ) -> FetchGitRepositoryLinkFileBlameResponseHttpRequest: ...
                    def fetchGitRefs(
                        self,
                        *,
                        gitRepositoryLink: str,
                        pageSize: int | None = ...,
                        pageToken: str | None = ...,
                        refType: typing.Literal["REF_TYPE_UNSPECIFIED", "TAG", "BRANCH"]
                        | None = ...,
                        **kwargs: typing.Any,
                    ) -> FetchGitRefsResponseHttpRequest: ...
                    def fetchGitRefs_next(
                        self,
                        previous_request: FetchGitRefsResponseHttpRequest,
                        previous_response: FetchGitRefsResponse,
                    ) -> FetchGitRefsResponseHttpRequest | None: ...
                    def fetchPullRequest(
                        self,
                        *,
                        name: str,
                        pullRequestId: str | None = ...,
                        **kwargs: typing.Any,
                    ) -> PullRequestHttpRequest: ...
                    def fetchPullRequestList(
                        self,
                        *,
                        name: str,
                        filter: str | None = ...,
                        pageSize: int | None = ...,
                        pageToken: str | None = ...,
                        **kwargs: typing.Any,
                    ) -> FetchGitRepositoryLinkPullRequestListResponseHttpRequest: ...
                    def fetchPullRequestList_next(
                        self,
                        previous_request: FetchGitRepositoryLinkPullRequestListResponseHttpRequest,
                        previous_response: FetchGitRepositoryLinkPullRequestListResponse,
                    ) -> (
                        FetchGitRepositoryLinkPullRequestListResponseHttpRequest | None
                    ): ...
                    def fetchReadToken(
                        self,
                        *,
                        gitRepositoryLink: str,
                        body: FetchReadTokenRequest,
                        **kwargs: typing.Any,
                    ) -> FetchReadTokenResponseHttpRequest: ...
                    def fetchReadWriteToken(
                        self,
                        *,
                        gitRepositoryLink: str,
                        body: FetchReadWriteTokenRequest,
                        **kwargs: typing.Any,
                    ) -> FetchReadWriteTokenResponseHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GitRepositoryLinkHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str | None = ...,
                        orderBy: str | None = ...,
                        pageSize: int | None = ...,
                        pageToken: str | None = ...,
                        **kwargs: typing.Any,
                    ) -> ListGitRepositoryLinksResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: ListGitRepositoryLinksResponseHttpRequest,
                        previous_response: ListGitRepositoryLinksResponse,
                    ) -> ListGitRepositoryLinksResponseHttpRequest | None: ...
                    def modifyPullRequest(
                        self,
                        *,
                        name: str,
                        body: ModifyGitRepositoryLinkPullRequestRequest,
                        **kwargs: typing.Any,
                    ) -> PullRequestHttpRequest: ...
                    def openPullRequest(
                        self,
                        *,
                        name: str,
                        body: OpenGitRepositoryLinkPullRequestRequest,
                        **kwargs: typing.Any,
                    ) -> PullRequestHttpRequest: ...
                    def processBitbucketCloudWebhook(
                        self,
                        *,
                        name: str,
                        body: ProcessBitbucketCloudWebhookRequest,
                        **kwargs: typing.Any,
                    ) -> EmptyHttpRequest: ...
                    def processBitbucketDataCenterWebhook(
                        self,
                        *,
                        name: str,
                        body: ProcessBitbucketDataCenterWebhookRequest,
                        **kwargs: typing.Any,
                    ) -> EmptyHttpRequest: ...
                    def processGitLabEnterpriseWebhook(
                        self,
                        *,
                        name: str,
                        body: ProcessGitLabEnterpriseWebhookRequest,
                        **kwargs: typing.Any,
                    ) -> EmptyHttpRequest: ...
                    def processGitLabWebhook(
                        self,
                        *,
                        name: str,
                        body: ProcessGitLabWebhookRequest,
                        **kwargs: typing.Any,
                    ) -> EmptyHttpRequest: ...

                def create(
                    self,
                    *,
                    parent: str,
                    body: Connection,
                    connectionId: str | None = ...,
                    requestId: str | None = ...,
                    validateOnly: bool | None = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def delete(
                    self,
                    *,
                    name: str,
                    etag: str | None = ...,
                    requestId: str | None = ...,
                    validateOnly: bool | None = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def fetchGitHubInstallations(
                    self, *, connection: str, **kwargs: typing.Any
                ) -> FetchGitHubInstallationsResponseHttpRequest: ...
                def fetchLinkableGitRepositories(
                    self,
                    *,
                    connection: str,
                    pageSize: int | None = ...,
                    pageToken: str | None = ...,
                    **kwargs: typing.Any,
                ) -> FetchLinkableGitRepositoriesResponseHttpRequest: ...
                def fetchLinkableGitRepositories_next(
                    self,
                    previous_request: FetchLinkableGitRepositoriesResponseHttpRequest,
                    previous_response: FetchLinkableGitRepositoriesResponse,
                ) -> FetchLinkableGitRepositoriesResponseHttpRequest | None: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> ConnectionHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str | None = ...,
                    orderBy: str | None = ...,
                    pageSize: int | None = ...,
                    pageToken: str | None = ...,
                    **kwargs: typing.Any,
                ) -> ListConnectionsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListConnectionsResponseHttpRequest,
                    previous_response: ListConnectionsResponse,
                ) -> ListConnectionsResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: Connection,
                    allowMissing: bool | None = ...,
                    requestId: str | None = ...,
                    updateMask: str | None = ...,
                    validateOnly: bool | None = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def processGitHubEnterpriseWebhook(
                    self,
                    *,
                    parent: str,
                    body: ProcessGitHubEnterpriseWebhookRequest,
                    **kwargs: typing.Any,
                ) -> EmptyHttpRequest: ...
                def gitRepositoryLinks(self) -> GitRepositoryLinksResource: ...

            @typing.type_check_only
            class InsightsConfigsResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class DeploymentEventsResource(googleapiclient.discovery.Resource):
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> DeploymentEventHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str | None = ...,
                        orderBy: str | None = ...,
                        pageSize: int | None = ...,
                        pageToken: str | None = ...,
                        **kwargs: typing.Any,
                    ) -> ListDeploymentEventsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: ListDeploymentEventsResponseHttpRequest,
                        previous_response: ListDeploymentEventsResponse,
                    ) -> ListDeploymentEventsResponseHttpRequest | None: ...

                def create(
                    self,
                    *,
                    parent: str,
                    body: InsightsConfig,
                    insightsConfigId: str | None = ...,
                    validateOnly: bool | None = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def delete(
                    self,
                    *,
                    name: str,
                    etag: str | None = ...,
                    requestId: str | None = ...,
                    validateOnly: bool | None = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> InsightsConfigHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str | None = ...,
                    orderBy: str | None = ...,
                    pageSize: int | None = ...,
                    pageToken: str | None = ...,
                    **kwargs: typing.Any,
                ) -> ListInsightsConfigsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListInsightsConfigsResponseHttpRequest,
                    previous_response: ListInsightsConfigsResponse,
                ) -> ListInsightsConfigsResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: InsightsConfig,
                    allowMissing: bool | None = ...,
                    requestId: str | None = ...,
                    validateOnly: bool | None = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def deploymentEvents(self) -> DeploymentEventsResource: ...

            @typing.type_check_only
            class OperationsResource(googleapiclient.discovery.Resource):
                def cancel(
                    self,
                    *,
                    name: str,
                    body: CancelOperationRequest,
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
                    filter: str | None = ...,
                    pageSize: int | None = ...,
                    pageToken: str | None = ...,
                    returnPartialSuccess: bool | None = ...,
                    **kwargs: typing.Any,
                ) -> ListOperationsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListOperationsResponseHttpRequest,
                    previous_response: ListOperationsResponse,
                ) -> ListOperationsResponseHttpRequest | None: ...

            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> LocationHttpRequest: ...
            def list(
                self,
                *,
                name: str,
                extraLocationTypes: str | _list[str] | None = ...,
                filter: str | None = ...,
                pageSize: int | None = ...,
                pageToken: str | None = ...,
                **kwargs: typing.Any,
            ) -> ListLocationsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListLocationsResponseHttpRequest,
                previous_response: ListLocationsResponse,
            ) -> ListLocationsResponseHttpRequest | None: ...
            def accountConnectors(self) -> AccountConnectorsResource: ...
            def connections(self) -> ConnectionsResource: ...
            def insightsConfigs(self) -> InsightsConfigsResource: ...
            def operations(self) -> OperationsResource: ...

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
class AccountConnectorHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> AccountConnector: ...

@typing.type_check_only
class ConnectionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Connection: ...

@typing.type_check_only
class DeploymentEventHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> DeploymentEvent: ...

@typing.type_check_only
class DiffGitRepositoryLinkCommitResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> DiffGitRepositoryLinkCommitResponse: ...

@typing.type_check_only
class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Empty: ...

@typing.type_check_only
class FetchAccessTokenResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> FetchAccessTokenResponse: ...

@typing.type_check_only
class FetchGitHubInstallationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> FetchGitHubInstallationsResponse: ...

@typing.type_check_only
class FetchGitRefsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> FetchGitRefsResponse: ...

@typing.type_check_only
class FetchGitRepositoryLinkCommitListResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> FetchGitRepositoryLinkCommitListResponse: ...

@typing.type_check_only
class FetchGitRepositoryLinkCommitResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> FetchGitRepositoryLinkCommitResponse: ...

@typing.type_check_only
class FetchGitRepositoryLinkFileBlameResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> FetchGitRepositoryLinkFileBlameResponse: ...

@typing.type_check_only
class FetchGitRepositoryLinkPullRequestListResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> FetchGitRepositoryLinkPullRequestListResponse: ...

@typing.type_check_only
class FetchLinkableGitRepositoriesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> FetchLinkableGitRepositoriesResponse: ...

@typing.type_check_only
class FetchReadTokenResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> FetchReadTokenResponse: ...

@typing.type_check_only
class FetchReadWriteTokenResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> FetchReadWriteTokenResponse: ...

@typing.type_check_only
class FetchUserRepositoriesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> FetchUserRepositoriesResponse: ...

@typing.type_check_only
class FinishOAuthResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> FinishOAuthResponse: ...

@typing.type_check_only
class GitRepositoryLinkHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GitRepositoryLink: ...

@typing.type_check_only
class InsightsConfigHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> InsightsConfig: ...

@typing.type_check_only
class ListAccountConnectorsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListAccountConnectorsResponse: ...

@typing.type_check_only
class ListConnectionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListConnectionsResponse: ...

@typing.type_check_only
class ListDeploymentEventsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListDeploymentEventsResponse: ...

@typing.type_check_only
class ListGitRepositoryLinksResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListGitRepositoryLinksResponse: ...

@typing.type_check_only
class ListInsightsConfigsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListInsightsConfigsResponse: ...

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
class ListUsersResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListUsersResponse: ...

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
class PullRequestReviewCommentHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> PullRequestReviewComment: ...

@typing.type_check_only
class StartOAuthResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> StartOAuthResponse: ...

@typing.type_check_only
class UserHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> User: ...
