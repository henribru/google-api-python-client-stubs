import collections.abc
import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

_list = list

@typing.type_check_only
class CloudTalentSolutionResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class ProjectsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class OperationsResource(googleapiclient.discovery.Resource):
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> OperationHttpRequest: ...

        @typing.type_check_only
        class TenantsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class ClientEventsResource(googleapiclient.discovery.Resource):
                def create(
                    self, *, parent: str, body: ClientEvent = ..., **kwargs: typing.Any
                ) -> ClientEventHttpRequest: ...

            @typing.type_check_only
            class CompaniesResource(googleapiclient.discovery.Resource):
                def create(
                    self, *, parent: str, body: Company = ..., **kwargs: typing.Any
                ) -> CompanyHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> CompanyHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    requireOpenJobs: bool = ...,
                    **kwargs: typing.Any
                ) -> ListCompaniesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListCompaniesResponseHttpRequest,
                    previous_response: ListCompaniesResponse,
                ) -> ListCompaniesResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: Company = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any
                ) -> CompanyHttpRequest: ...

            @typing.type_check_only
            class JobsResource(googleapiclient.discovery.Resource):
                def batchCreate(
                    self,
                    *,
                    parent: str,
                    body: BatchCreateJobsRequest = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def batchDelete(
                    self,
                    *,
                    parent: str,
                    body: BatchDeleteJobsRequest = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def batchUpdate(
                    self,
                    *,
                    parent: str,
                    body: BatchUpdateJobsRequest = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def create(
                    self, *, parent: str, body: Job = ..., **kwargs: typing.Any
                ) -> JobHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def get(self, *, name: str, **kwargs: typing.Any) -> JobHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    jobView: typing_extensions.Literal[
                        "JOB_VIEW_UNSPECIFIED",
                        "JOB_VIEW_ID_ONLY",
                        "JOB_VIEW_MINIMAL",
                        "JOB_VIEW_SMALL",
                        "JOB_VIEW_FULL",
                    ] = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> ListJobsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListJobsResponseHttpRequest,
                    previous_response: ListJobsResponse,
                ) -> ListJobsResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: Job = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any
                ) -> JobHttpRequest: ...
                def search(
                    self,
                    *,
                    parent: str,
                    body: SearchJobsRequest = ...,
                    **kwargs: typing.Any
                ) -> SearchJobsResponseHttpRequest: ...
                def search_next(
                    self,
                    previous_request: SearchJobsResponseHttpRequest,
                    previous_response: SearchJobsResponse,
                ) -> SearchJobsResponseHttpRequest | None: ...
                def searchForAlert(
                    self,
                    *,
                    parent: str,
                    body: SearchJobsRequest = ...,
                    **kwargs: typing.Any
                ) -> SearchJobsResponseHttpRequest: ...
                def searchForAlert_next(
                    self,
                    previous_request: SearchJobsResponseHttpRequest,
                    previous_response: SearchJobsResponse,
                ) -> SearchJobsResponseHttpRequest | None: ...

            def completeQuery(
                self,
                *,
                tenant: str,
                company: str = ...,
                languageCodes: str | _list[str] = ...,
                pageSize: int = ...,
                query: str = ...,
                scope: typing_extensions.Literal[
                    "COMPLETION_SCOPE_UNSPECIFIED", "TENANT", "PUBLIC"
                ] = ...,
                type: typing_extensions.Literal[
                    "COMPLETION_TYPE_UNSPECIFIED",
                    "JOB_TITLE",
                    "COMPANY_NAME",
                    "COMBINED",
                ] = ...,
                **kwargs: typing.Any
            ) -> CompleteQueryResponseHttpRequest: ...
            def create(
                self, *, parent: str, body: Tenant = ..., **kwargs: typing.Any
            ) -> TenantHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def get(self, *, name: str, **kwargs: typing.Any) -> TenantHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> ListTenantsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListTenantsResponseHttpRequest,
                previous_response: ListTenantsResponse,
            ) -> ListTenantsResponseHttpRequest | None: ...
            def patch(
                self,
                *,
                name: str,
                body: Tenant = ...,
                updateMask: str = ...,
                **kwargs: typing.Any
            ) -> TenantHttpRequest: ...
            def clientEvents(self) -> ClientEventsResource: ...
            def companies(self) -> CompaniesResource: ...
            def jobs(self) -> JobsResource: ...

        def operations(self) -> OperationsResource: ...
        def tenants(self) -> TenantsResource: ...

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
class ClientEventHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ClientEvent: ...

@typing.type_check_only
class CompanyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Company: ...

@typing.type_check_only
class CompleteQueryResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> CompleteQueryResponse: ...

@typing.type_check_only
class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Empty: ...

@typing.type_check_only
class JobHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Job: ...

@typing.type_check_only
class ListCompaniesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListCompaniesResponse: ...

@typing.type_check_only
class ListJobsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListJobsResponse: ...

@typing.type_check_only
class ListTenantsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListTenantsResponse: ...

@typing.type_check_only
class OperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Operation: ...

@typing.type_check_only
class SearchJobsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> SearchJobsResponse: ...

@typing.type_check_only
class TenantHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Tenant: ...
