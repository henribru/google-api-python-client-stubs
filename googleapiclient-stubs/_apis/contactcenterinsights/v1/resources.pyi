import collections.abc
import typing

import httplib2
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http

from .schemas import *

_list = list

@typing.type_check_only
class ContactcenterinsightsResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class ProjectsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class LocationsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class AnalysisRulesResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudContactcenterinsightsV1AnalysisRule = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudContactcenterinsightsV1AnalysisRuleHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleProtobufEmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudContactcenterinsightsV1AnalysisRuleHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudContactcenterinsightsV1ListAnalysisRulesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudContactcenterinsightsV1ListAnalysisRulesResponseHttpRequest,
                    previous_response: GoogleCloudContactcenterinsightsV1ListAnalysisRulesResponse,
                ) -> (
                    GoogleCloudContactcenterinsightsV1ListAnalysisRulesResponseHttpRequest
                    | None
                ): ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudContactcenterinsightsV1AnalysisRule = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudContactcenterinsightsV1AnalysisRuleHttpRequest: ...

            @typing.type_check_only
            class AuthorizedViewSetsResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class AuthorizedViewsResource(googleapiclient.discovery.Resource):
                    @typing.type_check_only
                    class ConversationsResource(googleapiclient.discovery.Resource):
                        def calculateStats(
                            self,
                            *,
                            location: str,
                            filter: str = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudContactcenterinsightsV1CalculateStatsResponseHttpRequest: ...

                    def queryMetrics(
                        self,
                        *,
                        location: str,
                        body: GoogleCloudContactcenterinsightsV1QueryMetricsRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def conversations(self) -> ConversationsResource: ...

                def authorizedViews(self) -> AuthorizedViewsResource: ...

            @typing.type_check_only
            class ConversationsResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class AnalysesResource(googleapiclient.discovery.Resource):
                    def create(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudContactcenterinsightsV1Analysis = ...,
                        **kwargs: typing.Any,
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
                        **kwargs: typing.Any,
                    ) -> GoogleCloudContactcenterinsightsV1ListAnalysesResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudContactcenterinsightsV1ListAnalysesResponseHttpRequest,
                        previous_response: GoogleCloudContactcenterinsightsV1ListAnalysesResponse,
                    ) -> (
                        GoogleCloudContactcenterinsightsV1ListAnalysesResponseHttpRequest
                        | None
                    ): ...

                @typing.type_check_only
                class FeedbackLabelsResource(googleapiclient.discovery.Resource):
                    def create(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudContactcenterinsightsV1FeedbackLabel = ...,
                        feedbackLabelId: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudContactcenterinsightsV1FeedbackLabelHttpRequest: ...
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleProtobufEmptyHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleCloudContactcenterinsightsV1FeedbackLabelHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudContactcenterinsightsV1ListFeedbackLabelsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudContactcenterinsightsV1ListFeedbackLabelsResponseHttpRequest,
                        previous_response: GoogleCloudContactcenterinsightsV1ListFeedbackLabelsResponse,
                    ) -> (
                        GoogleCloudContactcenterinsightsV1ListFeedbackLabelsResponseHttpRequest
                        | None
                    ): ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudContactcenterinsightsV1FeedbackLabel = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudContactcenterinsightsV1FeedbackLabelHttpRequest: ...

                def bulkAnalyze(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudContactcenterinsightsV1BulkAnalyzeConversationsRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def bulkDelete(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudContactcenterinsightsV1BulkDeleteConversationsRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def calculateStats(
                    self, *, location: str, filter: str = ..., **kwargs: typing.Any
                ) -> (
                    GoogleCloudContactcenterinsightsV1CalculateStatsResponseHttpRequest
                ): ...
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudContactcenterinsightsV1Conversation = ...,
                    conversationId: str = ...,
                    **kwargs: typing.Any,
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
                    **kwargs: typing.Any,
                ) -> GoogleCloudContactcenterinsightsV1ConversationHttpRequest: ...
                def ingest(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudContactcenterinsightsV1IngestConversationsRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    view: typing_extensions.Literal[
                        "CONVERSATION_VIEW_UNSPECIFIED", "FULL", "BASIC"
                    ] = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudContactcenterinsightsV1ListConversationsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudContactcenterinsightsV1ListConversationsResponseHttpRequest,
                    previous_response: GoogleCloudContactcenterinsightsV1ListConversationsResponse,
                ) -> (
                    GoogleCloudContactcenterinsightsV1ListConversationsResponseHttpRequest
                    | None
                ): ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudContactcenterinsightsV1Conversation = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudContactcenterinsightsV1ConversationHttpRequest: ...
                def upload(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudContactcenterinsightsV1UploadConversationRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def analyses(self) -> AnalysesResource: ...
                def feedbackLabels(self) -> FeedbackLabelsResource: ...

            @typing.type_check_only
            class EncryptionSpecResource(googleapiclient.discovery.Resource):
                def initialize(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudContactcenterinsightsV1InitializeEncryptionSpecRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...

            @typing.type_check_only
            class InsightsdataResource(googleapiclient.discovery.Resource):
                def export(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudContactcenterinsightsV1ExportInsightsDataRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...

            @typing.type_check_only
            class IssueModelsResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class IssuesResource(googleapiclient.discovery.Resource):
                    def create(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudContactcenterinsightsV1Issue = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleProtobufEmptyHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleCloudContactcenterinsightsV1IssueHttpRequest: ...
                    def list(
                        self, *, parent: str, **kwargs: typing.Any
                    ) -> (
                        GoogleCloudContactcenterinsightsV1ListIssuesResponseHttpRequest
                    ): ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudContactcenterinsightsV1Issue = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudContactcenterinsightsV1IssueHttpRequest: ...

                def calculateIssueModelStats(
                    self, *, issueModel: str, **kwargs: typing.Any
                ) -> GoogleCloudContactcenterinsightsV1CalculateIssueModelStatsResponseHttpRequest: ...
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudContactcenterinsightsV1IssueModel = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def deploy(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudContactcenterinsightsV1DeployIssueModelRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def export(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudContactcenterinsightsV1ExportIssueModelRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudContactcenterinsightsV1IssueModelHttpRequest: ...
                def import_(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudContactcenterinsightsV1ImportIssueModelRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def list(
                    self, *, parent: str, **kwargs: typing.Any
                ) -> (
                    GoogleCloudContactcenterinsightsV1ListIssueModelsResponseHttpRequest
                ): ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudContactcenterinsightsV1IssueModel = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudContactcenterinsightsV1IssueModelHttpRequest: ...
                def undeploy(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudContactcenterinsightsV1UndeployIssueModelRequest = ...,
                    **kwargs: typing.Any,
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
                    **kwargs: typing.Any,
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
                    **kwargs: typing.Any,
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
                    **kwargs: typing.Any,
                ) -> GoogleCloudContactcenterinsightsV1ListPhraseMatchersResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudContactcenterinsightsV1ListPhraseMatchersResponseHttpRequest,
                    previous_response: GoogleCloudContactcenterinsightsV1ListPhraseMatchersResponse,
                ) -> (
                    GoogleCloudContactcenterinsightsV1ListPhraseMatchersResponseHttpRequest
                    | None
                ): ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudContactcenterinsightsV1PhraseMatcher = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudContactcenterinsightsV1PhraseMatcherHttpRequest: ...

            @typing.type_check_only
            class QaScorecardsResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class RevisionsResource(googleapiclient.discovery.Resource):
                    @typing.type_check_only
                    class QaQuestionsResource(googleapiclient.discovery.Resource):
                        def create(
                            self,
                            *,
                            parent: str,
                            body: GoogleCloudContactcenterinsightsV1QaQuestion = ...,
                            qaQuestionId: str = ...,
                            **kwargs: typing.Any,
                        ) -> (
                            GoogleCloudContactcenterinsightsV1QaQuestionHttpRequest
                        ): ...
                        def delete(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> GoogleProtobufEmptyHttpRequest: ...
                        def get(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> (
                            GoogleCloudContactcenterinsightsV1QaQuestionHttpRequest
                        ): ...
                        def list(
                            self,
                            *,
                            parent: str,
                            pageSize: int = ...,
                            pageToken: str = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudContactcenterinsightsV1ListQaQuestionsResponseHttpRequest: ...
                        def list_next(
                            self,
                            previous_request: GoogleCloudContactcenterinsightsV1ListQaQuestionsResponseHttpRequest,
                            previous_response: GoogleCloudContactcenterinsightsV1ListQaQuestionsResponse,
                        ) -> (
                            GoogleCloudContactcenterinsightsV1ListQaQuestionsResponseHttpRequest
                            | None
                        ): ...
                        def patch(
                            self,
                            *,
                            name: str,
                            body: GoogleCloudContactcenterinsightsV1QaQuestion = ...,
                            updateMask: str = ...,
                            **kwargs: typing.Any,
                        ) -> (
                            GoogleCloudContactcenterinsightsV1QaQuestionHttpRequest
                        ): ...

                    def create(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudContactcenterinsightsV1QaScorecardRevision = ...,
                        qaScorecardRevisionId: str = ...,
                        **kwargs: typing.Any,
                    ) -> (
                        GoogleCloudContactcenterinsightsV1QaScorecardRevisionHttpRequest
                    ): ...
                    def delete(
                        self, *, name: str, force: bool = ..., **kwargs: typing.Any
                    ) -> GoogleProtobufEmptyHttpRequest: ...
                    def deploy(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudContactcenterinsightsV1DeployQaScorecardRevisionRequest = ...,
                        **kwargs: typing.Any,
                    ) -> (
                        GoogleCloudContactcenterinsightsV1QaScorecardRevisionHttpRequest
                    ): ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> (
                        GoogleCloudContactcenterinsightsV1QaScorecardRevisionHttpRequest
                    ): ...
                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudContactcenterinsightsV1ListQaScorecardRevisionsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudContactcenterinsightsV1ListQaScorecardRevisionsResponseHttpRequest,
                        previous_response: GoogleCloudContactcenterinsightsV1ListQaScorecardRevisionsResponse,
                    ) -> (
                        GoogleCloudContactcenterinsightsV1ListQaScorecardRevisionsResponseHttpRequest
                        | None
                    ): ...
                    def tuneQaScorecardRevision(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudContactcenterinsightsV1TuneQaScorecardRevisionRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def undeploy(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudContactcenterinsightsV1UndeployQaScorecardRevisionRequest = ...,
                        **kwargs: typing.Any,
                    ) -> (
                        GoogleCloudContactcenterinsightsV1QaScorecardRevisionHttpRequest
                    ): ...
                    def qaQuestions(self) -> QaQuestionsResource: ...

                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudContactcenterinsightsV1QaScorecard = ...,
                    qaScorecardId: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudContactcenterinsightsV1QaScorecardHttpRequest: ...
                def delete(
                    self, *, name: str, force: bool = ..., **kwargs: typing.Any
                ) -> GoogleProtobufEmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudContactcenterinsightsV1QaScorecardHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudContactcenterinsightsV1ListQaScorecardsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudContactcenterinsightsV1ListQaScorecardsResponseHttpRequest,
                    previous_response: GoogleCloudContactcenterinsightsV1ListQaScorecardsResponse,
                ) -> (
                    GoogleCloudContactcenterinsightsV1ListQaScorecardsResponseHttpRequest
                    | None
                ): ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudContactcenterinsightsV1QaScorecard = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudContactcenterinsightsV1QaScorecardHttpRequest: ...
                def revisions(self) -> RevisionsResource: ...

            @typing.type_check_only
            class ViewsResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudContactcenterinsightsV1View = ...,
                    **kwargs: typing.Any,
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
                    **kwargs: typing.Any,
                ) -> GoogleCloudContactcenterinsightsV1ListViewsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudContactcenterinsightsV1ListViewsResponseHttpRequest,
                    previous_response: GoogleCloudContactcenterinsightsV1ListViewsResponse,
                ) -> (
                    GoogleCloudContactcenterinsightsV1ListViewsResponseHttpRequest
                    | None
                ): ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudContactcenterinsightsV1View = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudContactcenterinsightsV1ViewHttpRequest: ...

            def bulkDownloadFeedbackLabels(
                self,
                *,
                parent: str,
                body: GoogleCloudContactcenterinsightsV1BulkDownloadFeedbackLabelsRequest = ...,
                **kwargs: typing.Any,
            ) -> GoogleLongrunningOperationHttpRequest: ...
            def bulkUploadFeedbackLabels(
                self,
                *,
                parent: str,
                body: GoogleCloudContactcenterinsightsV1BulkUploadFeedbackLabelsRequest = ...,
                **kwargs: typing.Any,
            ) -> GoogleLongrunningOperationHttpRequest: ...
            def getEncryptionSpec(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleCloudContactcenterinsightsV1EncryptionSpecHttpRequest: ...
            def getSettings(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleCloudContactcenterinsightsV1SettingsHttpRequest: ...
            def listAllFeedbackLabels(
                self,
                *,
                parent: str,
                filter: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any,
            ) -> GoogleCloudContactcenterinsightsV1ListAllFeedbackLabelsResponseHttpRequest: ...
            def listAllFeedbackLabels_next(
                self,
                previous_request: GoogleCloudContactcenterinsightsV1ListAllFeedbackLabelsResponseHttpRequest,
                previous_response: GoogleCloudContactcenterinsightsV1ListAllFeedbackLabelsResponse,
            ) -> (
                GoogleCloudContactcenterinsightsV1ListAllFeedbackLabelsResponseHttpRequest
                | None
            ): ...
            def queryMetrics(
                self,
                *,
                location: str,
                body: GoogleCloudContactcenterinsightsV1QueryMetricsRequest = ...,
                **kwargs: typing.Any,
            ) -> GoogleLongrunningOperationHttpRequest: ...
            def updateSettings(
                self,
                *,
                name: str,
                body: GoogleCloudContactcenterinsightsV1Settings = ...,
                updateMask: str = ...,
                **kwargs: typing.Any,
            ) -> GoogleCloudContactcenterinsightsV1SettingsHttpRequest: ...
            def analysisRules(self) -> AnalysisRulesResource: ...
            def authorizedViewSets(self) -> AuthorizedViewSetsResource: ...
            def conversations(self) -> ConversationsResource: ...
            def encryptionSpec(self) -> EncryptionSpecResource: ...
            def insightsdata(self) -> InsightsdataResource: ...
            def issueModels(self) -> IssueModelsResource: ...
            def operations(self) -> OperationsResource: ...
            def phraseMatchers(self) -> PhraseMatchersResource: ...
            def qaScorecards(self) -> QaScorecardsResource: ...
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
        | None = None,
    ) -> googleapiclient.http.BatchHttpRequest: ...
    def projects(self) -> ProjectsResource: ...

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1AnalysisHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudContactcenterinsightsV1Analysis: ...

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1AnalysisRuleHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudContactcenterinsightsV1AnalysisRule: ...

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1CalculateIssueModelStatsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudContactcenterinsightsV1CalculateIssueModelStatsResponse: ...

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1CalculateStatsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudContactcenterinsightsV1CalculateStatsResponse: ...

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1ConversationHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudContactcenterinsightsV1Conversation: ...

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1EncryptionSpecHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudContactcenterinsightsV1EncryptionSpec: ...

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1FeedbackLabelHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudContactcenterinsightsV1FeedbackLabel: ...

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1IssueHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudContactcenterinsightsV1Issue: ...

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1IssueModelHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudContactcenterinsightsV1IssueModel: ...

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1ListAllFeedbackLabelsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudContactcenterinsightsV1ListAllFeedbackLabelsResponse: ...

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1ListAnalysesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudContactcenterinsightsV1ListAnalysesResponse: ...

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1ListAnalysisRulesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudContactcenterinsightsV1ListAnalysisRulesResponse: ...

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1ListConversationsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudContactcenterinsightsV1ListConversationsResponse: ...

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1ListFeedbackLabelsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudContactcenterinsightsV1ListFeedbackLabelsResponse: ...

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1ListIssueModelsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudContactcenterinsightsV1ListIssueModelsResponse: ...

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1ListIssuesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudContactcenterinsightsV1ListIssuesResponse: ...

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1ListPhraseMatchersResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudContactcenterinsightsV1ListPhraseMatchersResponse: ...

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1ListQaQuestionsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudContactcenterinsightsV1ListQaQuestionsResponse: ...

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1ListQaScorecardRevisionsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudContactcenterinsightsV1ListQaScorecardRevisionsResponse: ...

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1ListQaScorecardsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudContactcenterinsightsV1ListQaScorecardsResponse: ...

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1ListViewsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudContactcenterinsightsV1ListViewsResponse: ...

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1PhraseMatcherHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudContactcenterinsightsV1PhraseMatcher: ...

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1QaQuestionHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudContactcenterinsightsV1QaQuestion: ...

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1QaScorecardHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudContactcenterinsightsV1QaScorecard: ...

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1QaScorecardRevisionHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudContactcenterinsightsV1QaScorecardRevision: ...

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1SettingsHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudContactcenterinsightsV1Settings: ...

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1ViewHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudContactcenterinsightsV1View: ...

@typing.type_check_only
class GoogleLongrunningListOperationsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleLongrunningListOperationsResponse: ...

@typing.type_check_only
class GoogleLongrunningOperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleLongrunningOperation: ...

@typing.type_check_only
class GoogleProtobufEmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleProtobufEmpty: ...
