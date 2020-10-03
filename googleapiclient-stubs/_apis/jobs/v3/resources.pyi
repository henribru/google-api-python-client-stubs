import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class CloudTalentSolutionResource(googleapiclient.discovery.Resource):
    class ProjectsResource(googleapiclient.discovery.Resource):
        class JobsResource(googleapiclient.discovery.Resource):
            def search(
                self,
                *,
                parent: str,
                body: SearchJobsRequest = ...,
                **kwargs: typing.Any
            ) -> SearchJobsResponseHttpRequest: ...
            def batchDelete(
                self,
                *,
                parent: str,
                body: BatchDeleteJobsRequest = ...,
                **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                jobView: typing_extensions.Literal[
                    "JOB_VIEW_UNSPECIFIED",
                    "JOB_VIEW_ID_ONLY",
                    "JOB_VIEW_MINIMAL",
                    "JOB_VIEW_SMALL",
                    "JOB_VIEW_FULL",
                ] = ...,
                pageToken: str = ...,
                pageSize: int = ...,
                filter: str = ...,
                **kwargs: typing.Any
            ) -> ListJobsResponseHttpRequest: ...
            def get(self, *, name: str, **kwargs: typing.Any) -> JobHttpRequest: ...
            def create(
                self, *, parent: str, body: CreateJobRequest = ..., **kwargs: typing.Any
            ) -> JobHttpRequest: ...
            def patch(
                self, *, name: str, body: UpdateJobRequest = ..., **kwargs: typing.Any
            ) -> JobHttpRequest: ...
            def searchForAlert(
                self,
                *,
                parent: str,
                body: SearchJobsRequest = ...,
                **kwargs: typing.Any
            ) -> SearchJobsResponseHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
        class CompaniesResource(googleapiclient.discovery.Resource):
            def get(self, *, name: str, **kwargs: typing.Any) -> CompanyHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def create(
                self,
                *,
                parent: str,
                body: CreateCompanyRequest = ...,
                **kwargs: typing.Any
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
            def patch(
                self,
                *,
                name: str,
                body: UpdateCompanyRequest = ...,
                **kwargs: typing.Any
            ) -> CompanyHttpRequest: ...
        class ClientEventsResource(googleapiclient.discovery.Resource):
            def create(
                self,
                *,
                parent: str,
                body: CreateClientEventRequest = ...,
                **kwargs: typing.Any
            ) -> ClientEventHttpRequest: ...
        def complete(
            self,
            *,
            name: str,
            type: typing_extensions.Literal[
                "COMPLETION_TYPE_UNSPECIFIED", "JOB_TITLE", "COMPANY_NAME", "COMBINED"
            ] = ...,
            scope: typing_extensions.Literal[
                "COMPLETION_SCOPE_UNSPECIFIED", "TENANT", "PUBLIC"
            ] = ...,
            languageCodes: typing.Union[str, typing.List[str]] = ...,
            pageSize: int = ...,
            languageCode: str = ...,
            query: str = ...,
            companyName: str = ...,
            **kwargs: typing.Any
        ) -> CompleteQueryResponseHttpRequest: ...
        def jobs(self) -> JobsResource: ...
        def companies(self) -> CompaniesResource: ...
        def clientEvents(self) -> ClientEventsResource: ...
    def projects(self) -> ProjectsResource: ...

class ClientEventHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ClientEvent: ...

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

class CompleteQueryResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> CompleteQueryResponse: ...
