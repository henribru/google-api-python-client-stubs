import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class CloudTalentSolutionResource(googleapiclient.discovery.Resource):
    class ProjectsResource(googleapiclient.discovery.Resource):
        class OperationsResource(googleapiclient.discovery.Resource):
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> OperationHttpRequest: ...
        class CompaniesResource(googleapiclient.discovery.Resource):
            def create(
                self,
                *,
                parent: str,
                body: CreateCompanyRequest = ...,
                **kwargs: typing.Any
            ) -> CompanyHttpRequest: ...
            def patch(
                self,
                *,
                name: str,
                body: UpdateCompanyRequest = ...,
                **kwargs: typing.Any
            ) -> CompanyHttpRequest: ...
            def get(self, *, name: str, **kwargs: typing.Any) -> CompanyHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                requireOpenJobs: bool = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> ListCompaniesResponseHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
        class JobsResource(googleapiclient.discovery.Resource):
            def patch(
                self, *, name: str, body: UpdateJobRequest = ..., **kwargs: typing.Any
            ) -> JobHttpRequest: ...
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
                filter: str = ...,
                pageSize: int = ...,
                **kwargs: typing.Any
            ) -> ListJobsResponseHttpRequest: ...
            def create(
                self, *, parent: str, body: CreateJobRequest = ..., **kwargs: typing.Any
            ) -> JobHttpRequest: ...
            def searchForAlert(
                self,
                *,
                parent: str,
                body: SearchJobsRequest = ...,
                **kwargs: typing.Any
            ) -> SearchJobsResponseHttpRequest: ...
            def get(self, *, name: str, **kwargs: typing.Any) -> JobHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
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
            query: str = ...,
            type: typing_extensions.Literal[
                "COMPLETION_TYPE_UNSPECIFIED", "JOB_TITLE", "COMPANY_NAME", "COMBINED"
            ] = ...,
            languageCodes: typing.Union[str, typing.List[str]] = ...,
            languageCode: str = ...,
            scope: typing_extensions.Literal[
                "COMPLETION_SCOPE_UNSPECIFIED", "TENANT", "PUBLIC"
            ] = ...,
            pageSize: int = ...,
            companyName: str = ...,
            **kwargs: typing.Any
        ) -> CompleteQueryResponseHttpRequest: ...
        def operations(self) -> OperationsResource: ...
        def companies(self) -> CompaniesResource: ...
        def jobs(self) -> JobsResource: ...
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

class OperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Operation: ...

class CompleteQueryResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> CompleteQueryResponse: ...
