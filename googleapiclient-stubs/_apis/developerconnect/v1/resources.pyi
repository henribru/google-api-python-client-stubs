import collections.abc
import typing

import httplib2
import typing_extensions

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
            class ConnectionsResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class GitRepositoryLinksResource(googleapiclient.discovery.Resource):
                    def create(
                        self,
                        *,
                        parent: str,
                        body: GitRepositoryLink = ...,
                        gitRepositoryLinkId: str = ...,
                        requestId: str = ...,
                        validateOnly: bool = ...,
                        **kwargs: typing.Any,
                    ) -> OperationHttpRequest: ...
                    def delete(
                        self,
                        *,
                        name: str,
                        etag: str = ...,
                        requestId: str = ...,
                        validateOnly: bool = ...,
                        **kwargs: typing.Any,
                    ) -> OperationHttpRequest: ...
                    def fetchGitRefs(
                        self,
                        *,
                        gitRepositoryLink: str,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        refType: typing_extensions.Literal[
                            "REF_TYPE_UNSPECIFIED", "TAG", "BRANCH"
                        ] = ...,
                        **kwargs: typing.Any,
                    ) -> FetchGitRefsResponseHttpRequest: ...
                    def fetchGitRefs_next(
                        self,
                        previous_request: FetchGitRefsResponseHttpRequest,
                        previous_response: FetchGitRefsResponse,
                    ) -> FetchGitRefsResponseHttpRequest | None: ...
                    def fetchReadToken(
                        self,
                        *,
                        gitRepositoryLink: str,
                        body: FetchReadTokenRequest = ...,
                        **kwargs: typing.Any,
                    ) -> FetchReadTokenResponseHttpRequest: ...
                    def fetchReadWriteToken(
                        self,
                        *,
                        gitRepositoryLink: str,
                        body: FetchReadWriteTokenRequest = ...,
                        **kwargs: typing.Any,
                    ) -> FetchReadWriteTokenResponseHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GitRepositoryLinkHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str = ...,
                        orderBy: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
                    ) -> ListGitRepositoryLinksResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: ListGitRepositoryLinksResponseHttpRequest,
                        previous_response: ListGitRepositoryLinksResponse,
                    ) -> ListGitRepositoryLinksResponseHttpRequest | None: ...
                    def processGitLabEnterpriseWebhook(
                        self,
                        *,
                        name: str,
                        body: ProcessGitLabEnterpriseWebhookRequest = ...,
                        **kwargs: typing.Any,
                    ) -> EmptyHttpRequest: ...
                    def processGitLabWebhook(
                        self,
                        *,
                        name: str,
                        body: ProcessGitLabWebhookRequest = ...,
                        **kwargs: typing.Any,
                    ) -> EmptyHttpRequest: ...

                def create(
                    self,
                    *,
                    parent: str,
                    body: Connection = ...,
                    connectionId: str = ...,
                    requestId: str = ...,
                    validateOnly: bool = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def delete(
                    self,
                    *,
                    name: str,
                    etag: str = ...,
                    requestId: str = ...,
                    validateOnly: bool = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def fetchGitHubInstallations(
                    self, *, connection: str, **kwargs: typing.Any
                ) -> FetchGitHubInstallationsResponseHttpRequest: ...
                def fetchLinkableGitRepositories(
                    self,
                    *,
                    connection: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
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
                    filter: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
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
                    body: Connection = ...,
                    allowMissing: bool = ...,
                    requestId: str = ...,
                    updateMask: str = ...,
                    validateOnly: bool = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def processGitHubEnterpriseWebhook(
                    self,
                    *,
                    parent: str,
                    body: ProcessGitHubEnterpriseWebhookRequest = ...,
                    **kwargs: typing.Any,
                ) -> EmptyHttpRequest: ...
                def gitRepositoryLinks(self) -> GitRepositoryLinksResource: ...

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

            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> LocationHttpRequest: ...
            def list(
                self,
                *,
                name: str,
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
            def connections(self) -> ConnectionsResource: ...
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
class ConnectionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Connection: ...

@typing.type_check_only
class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Empty: ...

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
class GitRepositoryLinkHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GitRepositoryLink: ...

@typing.type_check_only
class ListConnectionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListConnectionsResponse: ...

@typing.type_check_only
class ListGitRepositoryLinksResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListGitRepositoryLinksResponse: ...

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
