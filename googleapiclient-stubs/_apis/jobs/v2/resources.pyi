import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class CloudTalentSolutionResource(googleapiclient.discovery.Resource):
    class CompaniesResource(googleapiclient.discovery.Resource):
        class JobsResource(googleapiclient.discovery.Resource):
            def list(
                self,
                *,
                companyName: str,
                includeJobsCount: bool = ...,
                pageToken: str = ...,
                idsOnly: bool = ...,
                pageSize: int = ...,
                jobRequisitionId: str = ...,
                **kwargs: typing.Any
            ) -> ListCompanyJobsResponseHttpRequest: ...
        def get(self, *, name: str, **kwargs: typing.Any) -> CompanyHttpRequest: ...
        def delete(self, *, name: str, **kwargs: typing.Any) -> EmptyHttpRequest: ...
        def list(
            self,
            *,
            pageSize: int = ...,
            pageToken: str = ...,
            mustHaveOpenJobs: bool = ...,
            **kwargs: typing.Any
        ) -> ListCompaniesResponseHttpRequest: ...
        def patch(
            self,
            *,
            name: str,
            body: Company = ...,
            updateCompanyFields: str = ...,
            **kwargs: typing.Any
        ) -> CompanyHttpRequest: ...
        def create(
            self, *, body: Company = ..., **kwargs: typing.Any
        ) -> CompanyHttpRequest: ...
        def jobs(self) -> JobsResource: ...
    class JobsResource(googleapiclient.discovery.Resource):
        def delete(
            self, *, name: str, disableFastProcess: bool = ..., **kwargs: typing.Any
        ) -> EmptyHttpRequest: ...
        def create(
            self, *, body: CreateJobRequest = ..., **kwargs: typing.Any
        ) -> JobHttpRequest: ...
        def searchForAlert(
            self, *, body: SearchJobsRequest = ..., **kwargs: typing.Any
        ) -> SearchJobsResponseHttpRequest: ...
        def patch(
            self, *, name: str, body: UpdateJobRequest = ..., **kwargs: typing.Any
        ) -> JobHttpRequest: ...
        def search(
            self, *, body: SearchJobsRequest = ..., **kwargs: typing.Any
        ) -> SearchJobsResponseHttpRequest: ...
        def get(self, *, name: str, **kwargs: typing.Any) -> JobHttpRequest: ...
        def list(
            self,
            *,
            filter: str = ...,
            idsOnly: bool = ...,
            pageSize: int = ...,
            pageToken: str = ...,
            **kwargs: typing.Any
        ) -> ListJobsResponseHttpRequest: ...
        def deleteByFilter(
            self, *, body: DeleteJobsByFilterRequest = ..., **kwargs: typing.Any
        ) -> EmptyHttpRequest: ...
        def histogram(
            self, *, body: GetHistogramRequest = ..., **kwargs: typing.Any
        ) -> GetHistogramResponseHttpRequest: ...
        def batchDelete(
            self, *, body: BatchDeleteJobsRequest = ..., **kwargs: typing.Any
        ) -> EmptyHttpRequest: ...
    class V2Resource(googleapiclient.discovery.Resource):
        def complete(
            self,
            *,
            languageCode: str = ...,
            pageSize: int = ...,
            type: typing_extensions.Literal[
                "COMPLETION_TYPE_UNSPECIFIED", "JOB_TITLE", "COMPANY_NAME", "COMBINED"
            ] = ...,
            scope: typing_extensions.Literal[
                "COMPLETION_SCOPE_UNSPECIFIED", "TENANT", "PUBLIC"
            ] = ...,
            companyName: str = ...,
            query: str = ...,
            **kwargs: typing.Any
        ) -> CompleteQueryResponseHttpRequest: ...
    def companies(self) -> CompaniesResource: ...
    def jobs(self) -> JobsResource: ...
    def v2(self) -> V2Resource: ...

class ListCompaniesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListCompaniesResponse: ...

class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Empty: ...

class JobHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Job: ...

class GetHistogramResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GetHistogramResponse: ...

class CompleteQueryResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> CompleteQueryResponse: ...

class SearchJobsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> SearchJobsResponse: ...

class ListJobsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListJobsResponse: ...

class CompanyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Company: ...

class ListCompanyJobsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListCompanyJobsResponse: ...
