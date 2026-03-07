import collections.abc
import typing

import httplib2
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http

from .schemas import *

_list = list

@typing.type_check_only
class ThreatIntelligenceServiceResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class ProjectsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class AlertsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class DocumentsResource(googleapiclient.discovery.Resource):
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> AlertDocumentHttpRequest: ...

            def benign(
                self,
                *,
                name: str,
                body: MarkAlertAsBenignRequest = ...,
                **kwargs: typing.Any,
            ) -> AlertHttpRequest: ...
            def duplicate(
                self,
                *,
                name: str,
                body: MarkAlertAsDuplicateRequest = ...,
                **kwargs: typing.Any,
            ) -> AlertHttpRequest: ...
            def enumerateFacets(
                self, *, parent: str, filter: str = ..., **kwargs: typing.Any
            ) -> EnumerateAlertFacetsResponseHttpRequest: ...
            def escalate(
                self,
                *,
                name: str,
                body: MarkAlertAsEscalatedRequest = ...,
                **kwargs: typing.Any,
            ) -> AlertHttpRequest: ...
            def falsePositive(
                self,
                *,
                name: str,
                body: MarkAlertAsFalsePositiveRequest = ...,
                **kwargs: typing.Any,
            ) -> AlertHttpRequest: ...
            def get(self, *, name: str, **kwargs: typing.Any) -> AlertHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                filter: str = ...,
                orderBy: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any,
            ) -> ListAlertsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListAlertsResponseHttpRequest,
                previous_response: ListAlertsResponse,
            ) -> ListAlertsResponseHttpRequest | None: ...
            def notActionable(
                self,
                *,
                name: str,
                body: MarkAlertAsNotActionableRequest = ...,
                **kwargs: typing.Any,
            ) -> AlertHttpRequest: ...
            def read(
                self,
                *,
                name: str,
                body: MarkAlertAsReadRequest = ...,
                **kwargs: typing.Any,
            ) -> AlertHttpRequest: ...
            def resolve(
                self,
                *,
                name: str,
                body: MarkAlertAsResolvedRequest = ...,
                **kwargs: typing.Any,
            ) -> AlertHttpRequest: ...
            def trackExternally(
                self,
                *,
                name: str,
                body: MarkAlertAsTrackedExternallyRequest = ...,
                **kwargs: typing.Any,
            ) -> AlertHttpRequest: ...
            def triage(
                self,
                *,
                name: str,
                body: MarkAlertAsTriagedRequest = ...,
                **kwargs: typing.Any,
            ) -> AlertHttpRequest: ...
            def documents(self) -> DocumentsResource: ...

        @typing.type_check_only
        class ConfigurationsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class RevisionsResource(googleapiclient.discovery.Resource):
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> ListConfigurationRevisionsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListConfigurationRevisionsResponseHttpRequest,
                    previous_response: ListConfigurationRevisionsResponse,
                ) -> ListConfigurationRevisionsResponseHttpRequest | None: ...

            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> ConfigurationHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                filter: str = ...,
                orderBy: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any,
            ) -> ListConfigurationsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListConfigurationsResponseHttpRequest,
                previous_response: ListConfigurationsResponse,
            ) -> ListConfigurationsResponseHttpRequest | None: ...
            def upsert(
                self,
                *,
                parent: str,
                body: Configuration = ...,
                publishTime: str = ...,
                **kwargs: typing.Any,
            ) -> UpsertConfigurationResponseHttpRequest: ...
            def revisions(self) -> RevisionsResource: ...

        @typing.type_check_only
        class FindingsResource(googleapiclient.discovery.Resource):
            def get(self, *, name: str, **kwargs: typing.Any) -> FindingHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                filter: str = ...,
                orderBy: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any,
            ) -> ListFindingsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListFindingsResponseHttpRequest,
                previous_response: ListFindingsResponse,
            ) -> ListFindingsResponseHttpRequest | None: ...
            def search(
                self,
                *,
                parent: str,
                orderBy: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                query: str = ...,
                **kwargs: typing.Any,
            ) -> SearchFindingsResponseHttpRequest: ...
            def search_next(
                self,
                previous_request: SearchFindingsResponseHttpRequest,
                previous_response: SearchFindingsResponse,
            ) -> SearchFindingsResponseHttpRequest | None: ...

        def generateOrgProfile(
            self,
            *,
            name: str,
            body: GenerateOrgProfileConfigurationRequest = ...,
            **kwargs: typing.Any,
        ) -> OperationHttpRequest: ...
        def alerts(self) -> AlertsResource: ...
        def configurations(self) -> ConfigurationsResource: ...
        def findings(self) -> FindingsResource: ...

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
class AlertHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Alert: ...

@typing.type_check_only
class AlertDocumentHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> AlertDocument: ...

@typing.type_check_only
class ConfigurationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Configuration: ...

@typing.type_check_only
class EnumerateAlertFacetsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> EnumerateAlertFacetsResponse: ...

@typing.type_check_only
class FindingHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Finding: ...

@typing.type_check_only
class ListAlertsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListAlertsResponse: ...

@typing.type_check_only
class ListConfigurationRevisionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListConfigurationRevisionsResponse: ...

@typing.type_check_only
class ListConfigurationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListConfigurationsResponse: ...

@typing.type_check_only
class ListFindingsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListFindingsResponse: ...

@typing.type_check_only
class OperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Operation: ...

@typing.type_check_only
class SearchFindingsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> SearchFindingsResponse: ...

@typing.type_check_only
class UpsertConfigurationResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> UpsertConfigurationResponse: ...
