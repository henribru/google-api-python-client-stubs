import collections.abc
import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

_list = list

@typing.type_check_only
class ContactcenterinsightsResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class ProjectsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class LocationsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class ConversationsResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class AnalysesResource(googleapiclient.discovery.Resource):
                    def create(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudContactcenterinsightsV1Analysis = ...,
                        **kwargs: typing.Any
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleProtobufEmptyHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleCloudContactcenterinsightsV1AnalysisHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudContactcenterinsightsV1ListAnalysesResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudContactcenterinsightsV1ListAnalysesResponseHttpRequest,
                        previous_response: GoogleCloudContactcenterinsightsV1ListAnalysesResponse,
                    ) -> GoogleCloudContactcenterinsightsV1ListAnalysesResponseHttpRequest | None: ...

                def calculateStats(
                    self, *, location: str, filter: str = ..., **kwargs: typing.Any
                ) -> GoogleCloudContactcenterinsightsV1CalculateStatsResponseHttpRequest: ...
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudContactcenterinsightsV1Conversation = ...,
                    conversationId: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudContactcenterinsightsV1ConversationHttpRequest: ...
                def delete(
                    self, *, name: str, force: bool = ..., **kwargs: typing.Any
                ) -> GoogleProtobufEmptyHttpRequest: ...
                def get(
                    self,
                    *,
                    name: str,
                    view: typing_extensions.Literal[
                        "CONVERSATION_VIEW_UNSPECIFIED", "FULL", "BASIC"
                    ] = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudContactcenterinsightsV1ConversationHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    view: typing_extensions.Literal[
                        "CONVERSATION_VIEW_UNSPECIFIED", "FULL", "BASIC"
                    ] = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudContactcenterinsightsV1ListConversationsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudContactcenterinsightsV1ListConversationsResponseHttpRequest,
                    previous_response: GoogleCloudContactcenterinsightsV1ListConversationsResponse,
                ) -> GoogleCloudContactcenterinsightsV1ListConversationsResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudContactcenterinsightsV1Conversation = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudContactcenterinsightsV1ConversationHttpRequest: ...
                def analyses(self) -> AnalysesResource: ...

            @typing.type_check_only
            class InsightsdataResource(googleapiclient.discovery.Resource):
                def export(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudContactcenterinsightsV1ExportInsightsDataRequest = ...,
                    **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...

            @typing.type_check_only
            class IssueModelsResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class IssuesResource(googleapiclient.discovery.Resource):
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleCloudContactcenterinsightsV1IssueHttpRequest: ...
                    def list(
                        self, *, parent: str, **kwargs: typing.Any
                    ) -> GoogleCloudContactcenterinsightsV1ListIssuesResponseHttpRequest: ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudContactcenterinsightsV1Issue = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudContactcenterinsightsV1IssueHttpRequest: ...

                def calculateIssueModelStats(
                    self, *, issueModel: str, **kwargs: typing.Any
                ) -> GoogleCloudContactcenterinsightsV1CalculateIssueModelStatsResponseHttpRequest: ...
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudContactcenterinsightsV1IssueModel = ...,
                    **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def deploy(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudContactcenterinsightsV1DeployIssueModelRequest = ...,
                    **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudContactcenterinsightsV1IssueModelHttpRequest: ...
                def list(
                    self, *, parent: str, **kwargs: typing.Any
                ) -> GoogleCloudContactcenterinsightsV1ListIssueModelsResponseHttpRequest: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudContactcenterinsightsV1IssueModel = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudContactcenterinsightsV1IssueModelHttpRequest: ...
                def undeploy(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudContactcenterinsightsV1UndeployIssueModelRequest = ...,
                    **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def issues(self) -> IssuesResource: ...

            @typing.type_check_only
            class OperationsResource(googleapiclient.discovery.Resource):
                def cancel(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleProtobufEmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def list(
                    self,
                    *,
                    name: str,
                    filter: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleLongrunningListOperationsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleLongrunningListOperationsResponseHttpRequest,
                    previous_response: GoogleLongrunningListOperationsResponse,
                ) -> GoogleLongrunningListOperationsResponseHttpRequest | None: ...

            @typing.type_check_only
            class PhraseMatchersResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudContactcenterinsightsV1PhraseMatcher = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudContactcenterinsightsV1PhraseMatcherHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleProtobufEmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudContactcenterinsightsV1PhraseMatcherHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudContactcenterinsightsV1ListPhraseMatchersResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudContactcenterinsightsV1ListPhraseMatchersResponseHttpRequest,
                    previous_response: GoogleCloudContactcenterinsightsV1ListPhraseMatchersResponse,
                ) -> GoogleCloudContactcenterinsightsV1ListPhraseMatchersResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudContactcenterinsightsV1PhraseMatcher = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudContactcenterinsightsV1PhraseMatcherHttpRequest: ...

            @typing.type_check_only
            class ViewsResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudContactcenterinsightsV1View = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudContactcenterinsightsV1ViewHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleProtobufEmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudContactcenterinsightsV1ViewHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudContactcenterinsightsV1ListViewsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudContactcenterinsightsV1ListViewsResponseHttpRequest,
                    previous_response: GoogleCloudContactcenterinsightsV1ListViewsResponse,
                ) -> GoogleCloudContactcenterinsightsV1ListViewsResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudContactcenterinsightsV1View = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudContactcenterinsightsV1ViewHttpRequest: ...

            def getSettings(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleCloudContactcenterinsightsV1SettingsHttpRequest: ...
            def updateSettings(
                self,
                *,
                name: str,
                body: GoogleCloudContactcenterinsightsV1Settings = ...,
                updateMask: str = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudContactcenterinsightsV1SettingsHttpRequest: ...
            def conversations(self) -> ConversationsResource: ...
            def insightsdata(self) -> InsightsdataResource: ...
            def issueModels(self) -> IssueModelsResource: ...
            def operations(self) -> OperationsResource: ...
            def phraseMatchers(self) -> PhraseMatchersResource: ...
            def views(self) -> ViewsResource: ...

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
        | None = ...,
    ) -> googleapiclient.http.BatchHttpRequest: ...
    def projects(self) -> ProjectsResource: ...

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1AnalysisHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudContactcenterinsightsV1Analysis: ...

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1CalculateIssueModelStatsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudContactcenterinsightsV1CalculateIssueModelStatsResponse: ...

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1CalculateStatsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudContactcenterinsightsV1CalculateStatsResponse: ...

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1ConversationHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudContactcenterinsightsV1Conversation: ...

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1IssueHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudContactcenterinsightsV1Issue: ...

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1IssueModelHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudContactcenterinsightsV1IssueModel: ...

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1ListAnalysesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudContactcenterinsightsV1ListAnalysesResponse: ...

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1ListConversationsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudContactcenterinsightsV1ListConversationsResponse: ...

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1ListIssueModelsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudContactcenterinsightsV1ListIssueModelsResponse: ...

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1ListIssuesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudContactcenterinsightsV1ListIssuesResponse: ...

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1ListPhraseMatchersResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudContactcenterinsightsV1ListPhraseMatchersResponse: ...

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1ListViewsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudContactcenterinsightsV1ListViewsResponse: ...

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1PhraseMatcherHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudContactcenterinsightsV1PhraseMatcher: ...

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1SettingsHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudContactcenterinsightsV1Settings: ...

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1ViewHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudContactcenterinsightsV1View: ...

@typing.type_check_only
class GoogleLongrunningListOperationsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleLongrunningListOperationsResponse: ...

@typing.type_check_only
class GoogleLongrunningOperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleLongrunningOperation: ...

@typing.type_check_only
class GoogleProtobufEmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleProtobufEmpty: ...
