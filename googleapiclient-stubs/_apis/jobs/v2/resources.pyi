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
    class CompaniesResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class JobsResource(googleapiclient.discovery.Resource):
            def list(
                self,
                *,
                companyName: str,
                idsOnly: bool = ...,
                includeJobsCount: bool = ...,
                jobRequisitionId: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> ListCompanyJobsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListCompanyJobsResponseHttpRequest,
                previous_response: ListCompanyJobsResponse,
            ) -> ListCompanyJobsResponseHttpRequest | None: ...

        def create(
            self, *, body: Company = ..., **kwargs: typing.Any
        ) -> CompanyHttpRequest: ...
        def delete(self, *, name: str, **kwargs: typing.Any) -> EmptyHttpRequest: ...
        def get(self, *, name: str, **kwargs: typing.Any) -> CompanyHttpRequest: ...
        def list(
            self,
            *,
            mustHaveOpenJobs: bool = ...,
            pageSize: int = ...,
            pageToken: str = ...,
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
            updateCompanyFields: str = ...,
            **kwargs: typing.Any
        ) -> CompanyHttpRequest: ...
        def jobs(self) -> JobsResource: ...

    @typing.type_check_only
    class JobsResource(googleapiclient.discovery.Resource):
        def batchDelete(
            self, *, body: BatchDeleteJobsRequest = ..., **kwargs: typing.Any
        ) -> EmptyHttpRequest: ...
        def create(
            self, *, body: CreateJobRequest = ..., **kwargs: typing.Any
        ) -> JobHttpRequest: ...
        def delete(
            self, *, name: str, disableFastProcess: bool = ..., **kwargs: typing.Any
        ) -> EmptyHttpRequest: ...
        def deleteByFilter(
            self, *, body: DeleteJobsByFilterRequest = ..., **kwargs: typing.Any
        ) -> EmptyHttpRequest: ...
        def get(self, *, name: str, **kwargs: typing.Any) -> JobHttpRequest: ...
        def histogram(
            self, *, body: GetHistogramRequest = ..., **kwargs: typing.Any
        ) -> GetHistogramResponseHttpRequest: ...
        def list(
            self,
            *,
            filter: str = ...,
            idsOnly: bool = ...,
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
            self, *, name: str, body: UpdateJobRequest = ..., **kwargs: typing.Any
        ) -> JobHttpRequest: ...
        def search(
            self, *, body: SearchJobsRequest = ..., **kwargs: typing.Any
        ) -> SearchJobsResponseHttpRequest: ...
        def search_next(
            self,
            previous_request: SearchJobsResponseHttpRequest,
            previous_response: SearchJobsResponse,
        ) -> SearchJobsResponseHttpRequest | None: ...
        def searchForAlert(
            self, *, body: SearchJobsRequest = ..., **kwargs: typing.Any
        ) -> SearchJobsResponseHttpRequest: ...
        def searchForAlert_next(
            self,
            previous_request: SearchJobsResponseHttpRequest,
            previous_response: SearchJobsResponse,
        ) -> SearchJobsResponseHttpRequest | None: ...

    @typing.type_check_only
    class V2Resource(googleapiclient.discovery.Resource):
        def complete(
            self,
            *,
            companyName: str = ...,
            languageCode: str = ...,
            pageSize: int = ...,
            query: str = ...,
            scope: typing_extensions.Literal[
                "COMPLETION_SCOPE_UNSPECIFIED", "TENANT", "PUBLIC"
            ] = ...,
            type: typing_extensions.Literal[
                "COMPLETION_TYPE_UNSPECIFIED", "JOB_TITLE", "COMPANY_NAME", "COMBINED"
            ] = ...,
            **kwargs: typing.Any
        ) -> CompleteQueryResponseHttpRequest: ...

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
    def companies(self) -> CompaniesResource: ...
    def jobs(self) -> JobsResource: ...
    def v2(self) -> V2Resource: ...

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
class GetHistogramResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GetHistogramResponse: ...

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
class ListCompanyJobsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListCompanyJobsResponse: ...

@typing.type_check_only
class ListJobsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListJobsResponse: ...

@typing.type_check_only
class SearchJobsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> SearchJobsResponse: ...
