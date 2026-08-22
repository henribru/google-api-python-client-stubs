import collections.abc
import typing

import httplib2

import googleapiclient.discovery
import googleapiclient.http

from .schemas import *

_list = list

@typing.type_check_only
class AgentIdentityResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class ProjectsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class LocationsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class AccessSummariesResource(googleapiclient.discovery.Resource):
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> AccessSummaryHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str | None = ...,
                    orderBy: str | None = ...,
                    pageSize: int | None = ...,
                    pageToken: str | None = ...,
                    **kwargs: typing.Any,
                ) -> ListAccessSummariesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListAccessSummariesResponseHttpRequest,
                    previous_response: ListAccessSummariesResponse,
                ) -> ListAccessSummariesResponseHttpRequest | None: ...

            @typing.type_check_only
            class AuthProvidersResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class AuthorizationsResource(googleapiclient.discovery.Resource):
                    def delete(
                        self,
                        *,
                        name: str,
                        requestId: str | None = ...,
                        **kwargs: typing.Any,
                    ) -> EmptyHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> AuthorizationHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str | None = ...,
                        orderBy: str | None = ...,
                        pageSize: int | None = ...,
                        pageToken: str | None = ...,
                        **kwargs: typing.Any,
                    ) -> ListAuthorizationsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: ListAuthorizationsResponseHttpRequest,
                        previous_response: ListAuthorizationsResponse,
                    ) -> ListAuthorizationsResponseHttpRequest | None: ...

                def create(
                    self,
                    *,
                    parent: str,
                    body: AuthProvider,
                    authProviderId: str | None = ...,
                    requestId: str | None = ...,
                    **kwargs: typing.Any,
                ) -> AuthProviderHttpRequest: ...
                def delete(
                    self,
                    *,
                    name: str,
                    requestId: str | None = ...,
                    **kwargs: typing.Any,
                ) -> EmptyHttpRequest: ...
                def disable(
                    self,
                    *,
                    name: str,
                    body: DisableAuthProviderRequest,
                    **kwargs: typing.Any,
                ) -> AuthProviderHttpRequest: ...
                def enable(
                    self,
                    *,
                    name: str,
                    body: EnableAuthProviderRequest,
                    **kwargs: typing.Any,
                ) -> AuthProviderHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> AuthProviderHttpRequest: ...
                def getIamPolicy(
                    self,
                    *,
                    resource: str,
                    options_requestedPolicyVersion: int | None = ...,
                    **kwargs: typing.Any,
                ) -> PolicyHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str | None = ...,
                    orderBy: str | None = ...,
                    pageSize: int | None = ...,
                    pageToken: str | None = ...,
                    showDeleted: bool | None = ...,
                    **kwargs: typing.Any,
                ) -> ListAuthProvidersResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListAuthProvidersResponseHttpRequest,
                    previous_response: ListAuthProvidersResponse,
                ) -> ListAuthProvidersResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: AuthProvider,
                    requestId: str | None = ...,
                    updateMask: str | None = ...,
                    **kwargs: typing.Any,
                ) -> AuthProviderHttpRequest: ...
                def query(
                    self,
                    *,
                    parent: str,
                    pageSize: int | None = ...,
                    pageToken: str | None = ...,
                    workloadId: str | None = ...,
                    **kwargs: typing.Any,
                ) -> QueryAuthProvidersResponseHttpRequest: ...
                def query_next(
                    self,
                    previous_request: QueryAuthProvidersResponseHttpRequest,
                    previous_response: QueryAuthProvidersResponse,
                ) -> QueryAuthProvidersResponseHttpRequest | None: ...
                def queryWorkloads(
                    self,
                    *,
                    name: str,
                    pageSize: int | None = ...,
                    pageToken: str | None = ...,
                    **kwargs: typing.Any,
                ) -> QueryWorkloadsResponseHttpRequest: ...
                def queryWorkloads_next(
                    self,
                    previous_request: QueryWorkloadsResponseHttpRequest,
                    previous_response: QueryWorkloadsResponse,
                ) -> QueryWorkloadsResponseHttpRequest | None: ...
                def revokeAuthorization(
                    self,
                    *,
                    name: str,
                    body: RevokeAuthorizationRequest,
                    **kwargs: typing.Any,
                ) -> RevokeAuthorizationResponseHttpRequest: ...
                def setIamPolicy(
                    self,
                    *,
                    resource: str,
                    body: SetIamPolicyRequest,
                    **kwargs: typing.Any,
                ) -> PolicyHttpRequest: ...
                def testIamPermissions(
                    self,
                    *,
                    resource: str,
                    body: TestIamPermissionsRequest,
                    **kwargs: typing.Any,
                ) -> TestIamPermissionsResponseHttpRequest: ...
                def undelete(
                    self,
                    *,
                    name: str,
                    body: UndeleteAuthProviderRequest,
                    **kwargs: typing.Any,
                ) -> AuthProviderHttpRequest: ...
                def authorizations(self) -> AuthorizationsResource: ...

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
            def accessSummaries(self) -> AccessSummariesResource: ...
            def authProviders(self) -> AuthProvidersResource: ...

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
class AccessSummaryHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> AccessSummary: ...

@typing.type_check_only
class AuthProviderHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> AuthProvider: ...

@typing.type_check_only
class AuthorizationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Authorization: ...

@typing.type_check_only
class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Empty: ...

@typing.type_check_only
class ListAccessSummariesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListAccessSummariesResponse: ...

@typing.type_check_only
class ListAuthProvidersResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListAuthProvidersResponse: ...

@typing.type_check_only
class ListAuthorizationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListAuthorizationsResponse: ...

@typing.type_check_only
class ListLocationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListLocationsResponse: ...

@typing.type_check_only
class LocationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Location: ...

@typing.type_check_only
class PolicyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Policy: ...

@typing.type_check_only
class QueryAuthProvidersResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> QueryAuthProvidersResponse: ...

@typing.type_check_only
class QueryWorkloadsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> QueryWorkloadsResponse: ...

@typing.type_check_only
class RevokeAuthorizationResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> RevokeAuthorizationResponse: ...

@typing.type_check_only
class TestIamPermissionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> TestIamPermissionsResponse: ...
