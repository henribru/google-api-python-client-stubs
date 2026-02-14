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
            class AssessmentRulesResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudContactcenterinsightsV1AssessmentRule = ...,
                    assessmentRuleId: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudContactcenterinsightsV1AssessmentRuleHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleProtobufEmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudContactcenterinsightsV1AssessmentRuleHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudContactcenterinsightsV1ListAssessmentRulesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudContactcenterinsightsV1ListAssessmentRulesResponseHttpRequest,
                    previous_response: GoogleCloudContactcenterinsightsV1ListAssessmentRulesResponse,
                ) -> (
                    GoogleCloudContactcenterinsightsV1ListAssessmentRulesResponseHttpRequest
                    | None
                ): ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudContactcenterinsightsV1AssessmentRule = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudContactcenterinsightsV1AssessmentRuleHttpRequest: ...

            @typing.type_check_only
            class AuthorizedViewSetsResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class AuthorizedViewsResource(googleapiclient.discovery.Resource):
                    @typing.type_check_only
                    class ConversationsResource(googleapiclient.discovery.Resource):
                        @typing.type_check_only
                        class AssessmentsResource(googleapiclient.discovery.Resource):
                            @typing.type_check_only
                            class NotesResource(googleapiclient.discovery.Resource):
                                def create(
                                    self,
                                    *,
                                    parent: str,
                                    body: GoogleCloudContactcenterinsightsV1Note = ...,
                                    **kwargs: typing.Any,
                                ) -> (
                                    GoogleCloudContactcenterinsightsV1NoteHttpRequest
                                ): ...
                                def delete(
                                    self, *, name: str, **kwargs: typing.Any
                                ) -> GoogleProtobufEmptyHttpRequest: ...
                                def list(
                                    self,
                                    *,
                                    parent: str,
                                    pageSize: int = ...,
                                    pageToken: str = ...,
                                    **kwargs: typing.Any,
                                ) -> GoogleCloudContactcenterinsightsV1ListNotesResponseHttpRequest: ...
                                def list_next(
                                    self,
                                    previous_request: GoogleCloudContactcenterinsightsV1ListNotesResponseHttpRequest,
                                    previous_response: GoogleCloudContactcenterinsightsV1ListNotesResponse,
                                ) -> (
                                    GoogleCloudContactcenterinsightsV1ListNotesResponseHttpRequest
                                    | None
                                ): ...
                                def patch(
                                    self,
                                    *,
                                    name: str,
                                    body: GoogleCloudContactcenterinsightsV1Note = ...,
                                    updateMask: str = ...,
                                    **kwargs: typing.Any,
                                ) -> (
                                    GoogleCloudContactcenterinsightsV1NoteHttpRequest
                                ): ...

                            def appeal(
                                self,
                                *,
                                name: str,
                                body: GoogleCloudContactcenterinsightsV1AppealAssessmentRequest = ...,
                                **kwargs: typing.Any,
                            ) -> (
                                GoogleCloudContactcenterinsightsV1AssessmentHttpRequest
                            ): ...
                            def create(
                                self,
                                *,
                                parent: str,
                                body: GoogleCloudContactcenterinsightsV1Assessment = ...,
                                **kwargs: typing.Any,
                            ) -> (
                                GoogleCloudContactcenterinsightsV1AssessmentHttpRequest
                            ): ...
                            def delete(
                                self,
                                *,
                                name: str,
                                force: bool = ...,
                                **kwargs: typing.Any,
                            ) -> GoogleProtobufEmptyHttpRequest: ...
                            def finalize(
                                self,
                                *,
                                name: str,
                                body: GoogleCloudContactcenterinsightsV1FinalizeAssessmentRequest = ...,
                                **kwargs: typing.Any,
                            ) -> (
                                GoogleCloudContactcenterinsightsV1AssessmentHttpRequest
                            ): ...
                            def get(
                                self, *, name: str, **kwargs: typing.Any
                            ) -> (
                                GoogleCloudContactcenterinsightsV1AssessmentHttpRequest
                            ): ...
                            def list(
                                self,
                                *,
                                parent: str,
                                filter: str = ...,
                                pageSize: int = ...,
                                pageToken: str = ...,
                                **kwargs: typing.Any,
                            ) -> GoogleCloudContactcenterinsightsV1ListAssessmentsResponseHttpRequest: ...
                            def list_next(
                                self,
                                previous_request: GoogleCloudContactcenterinsightsV1ListAssessmentsResponseHttpRequest,
                                previous_response: GoogleCloudContactcenterinsightsV1ListAssessmentsResponse,
                            ) -> (
                                GoogleCloudContactcenterinsightsV1ListAssessmentsResponseHttpRequest
                                | None
                            ): ...
                            def publish(
                                self,
                                *,
                                name: str,
                                body: GoogleCloudContactcenterinsightsV1PublishAssessmentRequest = ...,
                                **kwargs: typing.Any,
                            ) -> (
                                GoogleCloudContactcenterinsightsV1AssessmentHttpRequest
                            ): ...
                            def notes(self) -> NotesResource: ...

                        @typing.type_check_only
                        class FeedbackLabelsResource(
                            googleapiclient.discovery.Resource
                        ):
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

                        def calculateStats(
                            self,
                            *,
                            location: str,
                            filter: str = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudContactcenterinsightsV1CalculateStatsResponseHttpRequest: ...
                        def delete(
                            self, *, name: str, force: bool = ..., **kwargs: typing.Any
                        ) -> GoogleProtobufEmptyHttpRequest: ...
                        def generateSignedAudio(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> GoogleCloudContactcenterinsightsV1GenerateConversationSignedAudioResponseHttpRequest: ...
                        def get(
                            self,
                            *,
                            name: str,
                            view: typing_extensions.Literal[
                                "CONVERSATION_VIEW_UNSPECIFIED", "FULL", "BASIC"
                            ] = ...,
                            **kwargs: typing.Any,
                        ) -> (
                            GoogleCloudContactcenterinsightsV1ConversationHttpRequest
                        ): ...
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
                        def assessments(self) -> AssessmentsResource: ...
                        def feedbackLabels(self) -> FeedbackLabelsResource: ...

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
                            returnPartialSuccess: bool = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleLongrunningListOperationsResponseHttpRequest: ...
                        def list_next(
                            self,
                            previous_request: GoogleLongrunningListOperationsResponseHttpRequest,
                            previous_response: GoogleLongrunningListOperationsResponse,
                        ) -> (
                            GoogleLongrunningListOperationsResponseHttpRequest | None
                        ): ...

                    def create(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudContactcenterinsightsV1AuthorizedView = ...,
                        authorizedViewId: str = ...,
                        **kwargs: typing.Any,
                    ) -> (
                        GoogleCloudContactcenterinsightsV1AuthorizedViewHttpRequest
                    ): ...
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleProtobufEmptyHttpRequest: ...
                    def generativeInsights(
                        self,
                        *,
                        location: str,
                        body: GoogleCloudContactcenterinsightsV1GenerativeInsightsRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> (
                        GoogleCloudContactcenterinsightsV1AuthorizedViewHttpRequest
                    ): ...
                    def getIamPolicy(
                        self,
                        *,
                        resource: str,
                        options_requestedPolicyVersion: int = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleIamV1PolicyHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str = ...,
                        orderBy: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudContactcenterinsightsV1ListAuthorizedViewsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudContactcenterinsightsV1ListAuthorizedViewsResponseHttpRequest,
                        previous_response: GoogleCloudContactcenterinsightsV1ListAuthorizedViewsResponse,
                    ) -> (
                        GoogleCloudContactcenterinsightsV1ListAuthorizedViewsResponseHttpRequest
                        | None
                    ): ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudContactcenterinsightsV1AuthorizedView = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any,
                    ) -> (
                        GoogleCloudContactcenterinsightsV1AuthorizedViewHttpRequest
                    ): ...
                    def queryMetrics(
                        self,
                        *,
                        location: str,
                        body: GoogleCloudContactcenterinsightsV1QueryMetricsRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def queryPerformanceOverview(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudContactcenterinsightsV1QueryPerformanceOverviewRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def search(
                        self,
                        *,
                        parent: str,
                        orderBy: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        query: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudContactcenterinsightsV1SearchAuthorizedViewsResponseHttpRequest: ...
                    def search_next(
                        self,
                        previous_request: GoogleCloudContactcenterinsightsV1SearchAuthorizedViewsResponseHttpRequest,
                        previous_response: GoogleCloudContactcenterinsightsV1SearchAuthorizedViewsResponse,
                    ) -> (
                        GoogleCloudContactcenterinsightsV1SearchAuthorizedViewsResponseHttpRequest
                        | None
                    ): ...
                    def setIamPolicy(
                        self,
                        *,
                        resource: str,
                        body: GoogleIamV1SetIamPolicyRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleIamV1PolicyHttpRequest: ...
                    def testIamPermissions(
                        self,
                        *,
                        resource: str,
                        body: GoogleIamV1TestIamPermissionsRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleIamV1TestIamPermissionsResponseHttpRequest: ...
                    def conversations(self) -> ConversationsResource: ...
                    def operations(self) -> OperationsResource: ...

                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudContactcenterinsightsV1AuthorizedViewSet = ...,
                    authorizedViewSetId: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudContactcenterinsightsV1AuthorizedViewSetHttpRequest: ...
                def delete(
                    self, *, name: str, force: bool = ..., **kwargs: typing.Any
                ) -> GoogleProtobufEmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudContactcenterinsightsV1AuthorizedViewSetHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudContactcenterinsightsV1ListAuthorizedViewSetsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudContactcenterinsightsV1ListAuthorizedViewSetsResponseHttpRequest,
                    previous_response: GoogleCloudContactcenterinsightsV1ListAuthorizedViewSetsResponse,
                ) -> (
                    GoogleCloudContactcenterinsightsV1ListAuthorizedViewSetsResponseHttpRequest
                    | None
                ): ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudContactcenterinsightsV1AuthorizedViewSet = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudContactcenterinsightsV1AuthorizedViewSetHttpRequest: ...
                def authorizedViews(self) -> AuthorizedViewsResource: ...

            @typing.type_check_only
            class AutoLabelingRulesResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudContactcenterinsightsV1AutoLabelingRule = ...,
                    autoLabelingRuleId: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudContactcenterinsightsV1AutoLabelingRuleHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleProtobufEmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudContactcenterinsightsV1AutoLabelingRuleHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudContactcenterinsightsV1ListAutoLabelingRulesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudContactcenterinsightsV1ListAutoLabelingRulesResponseHttpRequest,
                    previous_response: GoogleCloudContactcenterinsightsV1ListAutoLabelingRulesResponse,
                ) -> (
                    GoogleCloudContactcenterinsightsV1ListAutoLabelingRulesResponseHttpRequest
                    | None
                ): ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudContactcenterinsightsV1AutoLabelingRule = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudContactcenterinsightsV1AutoLabelingRuleHttpRequest: ...
                def test(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudContactcenterinsightsV1TestAutoLabelingRuleRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudContactcenterinsightsV1TestAutoLabelingRuleResponseHttpRequest: ...

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
                class AssessmentsResource(googleapiclient.discovery.Resource):
                    @typing.type_check_only
                    class NotesResource(googleapiclient.discovery.Resource):
                        def create(
                            self,
                            *,
                            parent: str,
                            body: GoogleCloudContactcenterinsightsV1Note = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudContactcenterinsightsV1NoteHttpRequest: ...
                        def delete(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> GoogleProtobufEmptyHttpRequest: ...
                        def list(
                            self,
                            *,
                            parent: str,
                            pageSize: int = ...,
                            pageToken: str = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudContactcenterinsightsV1ListNotesResponseHttpRequest: ...
                        def list_next(
                            self,
                            previous_request: GoogleCloudContactcenterinsightsV1ListNotesResponseHttpRequest,
                            previous_response: GoogleCloudContactcenterinsightsV1ListNotesResponse,
                        ) -> (
                            GoogleCloudContactcenterinsightsV1ListNotesResponseHttpRequest
                            | None
                        ): ...
                        def patch(
                            self,
                            *,
                            name: str,
                            body: GoogleCloudContactcenterinsightsV1Note = ...,
                            updateMask: str = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudContactcenterinsightsV1NoteHttpRequest: ...

                    def appeal(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudContactcenterinsightsV1AppealAssessmentRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudContactcenterinsightsV1AssessmentHttpRequest: ...
                    def create(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudContactcenterinsightsV1Assessment = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudContactcenterinsightsV1AssessmentHttpRequest: ...
                    def delete(
                        self, *, name: str, force: bool = ..., **kwargs: typing.Any
                    ) -> GoogleProtobufEmptyHttpRequest: ...
                    def finalize(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudContactcenterinsightsV1FinalizeAssessmentRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudContactcenterinsightsV1AssessmentHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleCloudContactcenterinsightsV1AssessmentHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudContactcenterinsightsV1ListAssessmentsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudContactcenterinsightsV1ListAssessmentsResponseHttpRequest,
                        previous_response: GoogleCloudContactcenterinsightsV1ListAssessmentsResponse,
                    ) -> (
                        GoogleCloudContactcenterinsightsV1ListAssessmentsResponseHttpRequest
                        | None
                    ): ...
                    def publish(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudContactcenterinsightsV1PublishAssessmentRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudContactcenterinsightsV1AssessmentHttpRequest: ...
                    def notes(self) -> NotesResource: ...

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

                @typing.type_check_only
                class SegmentsResource(googleapiclient.discovery.Resource):
                    def bulkAnalyze(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudContactcenterinsightsV1BulkAnalyzeConversationsRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleLongrunningOperationHttpRequest: ...

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
                def generateSignedAudio(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudContactcenterinsightsV1GenerateConversationSignedAudioResponseHttpRequest: ...
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
                    allowMissing: bool = ...,
                    conversationAutoLabelingUpdateConfig_allowAutoLabelingUpdate: bool = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudContactcenterinsightsV1ConversationHttpRequest: ...
                def sample(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudContactcenterinsightsV1SampleConversationsRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def upload(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudContactcenterinsightsV1UploadConversationRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def analyses(self) -> AnalysesResource: ...
                def assessments(self) -> AssessmentsResource: ...
                def feedbackLabels(self) -> FeedbackLabelsResource: ...
                def segments(self) -> SegmentsResource: ...

            @typing.type_check_only
            class DashboardsResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class ChartsResource(googleapiclient.discovery.Resource):
                    def create(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudContactcenterinsightsV1Chart = ...,
                        chartId: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudContactcenterinsightsV1ChartHttpRequest: ...
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleProtobufEmptyHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleCloudContactcenterinsightsV1ChartHttpRequest: ...
                    def list(
                        self, *, parent: str, **kwargs: typing.Any
                    ) -> (
                        GoogleCloudContactcenterinsightsV1ListChartsResponseHttpRequest
                    ): ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudContactcenterinsightsV1Chart = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudContactcenterinsightsV1ChartHttpRequest: ...

                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudContactcenterinsightsV1Dashboard = ...,
                    dashboardId: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudContactcenterinsightsV1DashboardHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleProtobufEmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudContactcenterinsightsV1DashboardHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> (
                    GoogleCloudContactcenterinsightsV1ListDashboardsResponseHttpRequest
                ): ...
                def list_next(
                    self,
                    previous_request: GoogleCloudContactcenterinsightsV1ListDashboardsResponseHttpRequest,
                    previous_response: GoogleCloudContactcenterinsightsV1ListDashboardsResponse,
                ) -> (
                    GoogleCloudContactcenterinsightsV1ListDashboardsResponseHttpRequest
                    | None
                ): ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudContactcenterinsightsV1Dashboard = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudContactcenterinsightsV1DashboardHttpRequest: ...
                def charts(self) -> ChartsResource: ...

            @typing.type_check_only
            class DatasetsResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class ConversationsResource(googleapiclient.discovery.Resource):
                    @typing.type_check_only
                    class FeedbackLabelsResource(googleapiclient.discovery.Resource):
                        def create(
                            self,
                            *,
                            parent: str,
                            body: GoogleCloudContactcenterinsightsV1FeedbackLabel = ...,
                            feedbackLabelId: str = ...,
                            **kwargs: typing.Any,
                        ) -> (
                            GoogleCloudContactcenterinsightsV1FeedbackLabelHttpRequest
                        ): ...
                        def delete(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> GoogleProtobufEmptyHttpRequest: ...
                        def get(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> (
                            GoogleCloudContactcenterinsightsV1FeedbackLabelHttpRequest
                        ): ...
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
                        ) -> (
                            GoogleCloudContactcenterinsightsV1FeedbackLabelHttpRequest
                        ): ...

                    def bulkDelete(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudContactcenterinsightsV1BulkDeleteConversationsRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def calculateStats(
                        self,
                        *,
                        location: str,
                        body: GoogleCloudContactcenterinsightsV1CalculateStatsRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudContactcenterinsightsV1CalculateStatsResponseHttpRequest: ...
                    def delete(
                        self, *, name: str, force: bool = ..., **kwargs: typing.Any
                    ) -> GoogleProtobufEmptyHttpRequest: ...
                    def generateSignedAudio(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleCloudContactcenterinsightsV1GenerateConversationSignedAudioResponseHttpRequest: ...
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
                    def sample(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudContactcenterinsightsV1SampleConversationsRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def feedbackLabels(self) -> FeedbackLabelsResource: ...

                @typing.type_check_only
                class InsightsdataResource(googleapiclient.discovery.Resource):
                    def export(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudContactcenterinsightsV1ExportInsightsDataRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleLongrunningOperationHttpRequest: ...

                def bulkDeleteFeedbackLabels(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudContactcenterinsightsV1BulkDeleteFeedbackLabelsRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
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
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudContactcenterinsightsV1Dataset = ...,
                    datasetId: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudContactcenterinsightsV1DatasetHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudContactcenterinsightsV1DatasetHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> (
                    GoogleCloudContactcenterinsightsV1ListDatasetsResponseHttpRequest
                ): ...
                def list_next(
                    self,
                    previous_request: GoogleCloudContactcenterinsightsV1ListDatasetsResponseHttpRequest,
                    previous_response: GoogleCloudContactcenterinsightsV1ListDatasetsResponse,
                ) -> (
                    GoogleCloudContactcenterinsightsV1ListDatasetsResponseHttpRequest
                    | None
                ): ...
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
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudContactcenterinsightsV1Dataset = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudContactcenterinsightsV1DatasetHttpRequest: ...
                def conversations(self) -> ConversationsResource: ...
                def insightsdata(self) -> InsightsdataResource: ...

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
                    returnPartialSuccess: bool = ...,
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
            class QaQuestionTagsResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudContactcenterinsightsV1QaQuestionTag = ...,
                    qaQuestionTagId: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudContactcenterinsightsV1QaQuestionTagHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudContactcenterinsightsV1QaQuestionTagHttpRequest: ...
                def list(
                    self, *, parent: str, filter: str = ..., **kwargs: typing.Any
                ) -> GoogleCloudContactcenterinsightsV1ListQaQuestionTagsResponseHttpRequest: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudContactcenterinsightsV1QaQuestionTag = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...

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
                        qaScorecardSources: typing_extensions.Literal[
                            "QA_SCORECARD_SOURCE_UNSPECIFIED",
                            "QA_SCORECARD_SOURCE_CUSTOMER_DEFINED",
                            "QA_SCORECARD_SOURCE_DISCOVERY_ENGINE",
                        ]
                        | _list[
                            typing_extensions.Literal[
                                "QA_SCORECARD_SOURCE_UNSPECIFIED",
                                "QA_SCORECARD_SOURCE_CUSTOMER_DEFINED",
                                "QA_SCORECARD_SOURCE_DISCOVERY_ENGINE",
                            ]
                        ] = ...,
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
                    qaScorecardSources: typing_extensions.Literal[
                        "QA_SCORECARD_SOURCE_UNSPECIFIED",
                        "QA_SCORECARD_SOURCE_CUSTOMER_DEFINED",
                        "QA_SCORECARD_SOURCE_DISCOVERY_ENGINE",
                    ]
                    | _list[
                        typing_extensions.Literal[
                            "QA_SCORECARD_SOURCE_UNSPECIFIED",
                            "QA_SCORECARD_SOURCE_CUSTOMER_DEFINED",
                            "QA_SCORECARD_SOURCE_DISCOVERY_ENGINE",
                        ]
                    ] = ...,
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

            def bulkDeleteFeedbackLabels(
                self,
                *,
                parent: str,
                body: GoogleCloudContactcenterinsightsV1BulkDeleteFeedbackLabelsRequest = ...,
                **kwargs: typing.Any,
            ) -> GoogleLongrunningOperationHttpRequest: ...
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
            def generativeInsights(
                self,
                *,
                location: str,
                body: GoogleCloudContactcenterinsightsV1GenerativeInsightsRequest = ...,
                **kwargs: typing.Any,
            ) -> GoogleLongrunningOperationHttpRequest: ...
            def getCorrelationConfig(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleCloudContactcenterinsightsV1CorrelationConfigHttpRequest: ...
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
            def queryPerformanceOverview(
                self,
                *,
                parent: str,
                body: GoogleCloudContactcenterinsightsV1QueryPerformanceOverviewRequest = ...,
                **kwargs: typing.Any,
            ) -> GoogleLongrunningOperationHttpRequest: ...
            def testCorrelationConfig(
                self,
                *,
                location: str,
                body: GoogleCloudContactcenterinsightsV1TestCorrelationConfigRequest = ...,
                **kwargs: typing.Any,
            ) -> GoogleLongrunningOperationHttpRequest: ...
            def updateCorrelationConfig(
                self,
                *,
                name: str,
                body: GoogleCloudContactcenterinsightsV1CorrelationConfig = ...,
                updateMask: str = ...,
                **kwargs: typing.Any,
            ) -> GoogleCloudContactcenterinsightsV1CorrelationConfigHttpRequest: ...
            def updateSettings(
                self,
                *,
                name: str,
                body: GoogleCloudContactcenterinsightsV1Settings = ...,
                updateMask: str = ...,
                **kwargs: typing.Any,
            ) -> GoogleCloudContactcenterinsightsV1SettingsHttpRequest: ...
            def analysisRules(self) -> AnalysisRulesResource: ...
            def assessmentRules(self) -> AssessmentRulesResource: ...
            def authorizedViewSets(self) -> AuthorizedViewSetsResource: ...
            def autoLabelingRules(self) -> AutoLabelingRulesResource: ...
            def conversations(self) -> ConversationsResource: ...
            def dashboards(self) -> DashboardsResource: ...
            def datasets(self) -> DatasetsResource: ...
            def encryptionSpec(self) -> EncryptionSpecResource: ...
            def insightsdata(self) -> InsightsdataResource: ...
            def issueModels(self) -> IssueModelsResource: ...
            def operations(self) -> OperationsResource: ...
            def phraseMatchers(self) -> PhraseMatchersResource: ...
            def qaQuestionTags(self) -> QaQuestionTagsResource: ...
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
class GoogleCloudContactcenterinsightsV1AssessmentHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudContactcenterinsightsV1Assessment: ...

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1AssessmentRuleHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudContactcenterinsightsV1AssessmentRule: ...

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1AuthorizedViewHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudContactcenterinsightsV1AuthorizedView: ...

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1AuthorizedViewSetHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudContactcenterinsightsV1AuthorizedViewSet: ...

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1AutoLabelingRuleHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudContactcenterinsightsV1AutoLabelingRule: ...

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
class GoogleCloudContactcenterinsightsV1ChartHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudContactcenterinsightsV1Chart: ...

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
class GoogleCloudContactcenterinsightsV1CorrelationConfigHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudContactcenterinsightsV1CorrelationConfig: ...

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1DashboardHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudContactcenterinsightsV1Dashboard: ...

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1DatasetHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudContactcenterinsightsV1Dataset: ...

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
class GoogleCloudContactcenterinsightsV1GenerateConversationSignedAudioResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudContactcenterinsightsV1GenerateConversationSignedAudioResponse: ...

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
class GoogleCloudContactcenterinsightsV1ListAssessmentRulesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudContactcenterinsightsV1ListAssessmentRulesResponse: ...

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1ListAssessmentsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudContactcenterinsightsV1ListAssessmentsResponse: ...

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1ListAuthorizedViewSetsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudContactcenterinsightsV1ListAuthorizedViewSetsResponse: ...

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1ListAuthorizedViewsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudContactcenterinsightsV1ListAuthorizedViewsResponse: ...

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1ListAutoLabelingRulesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudContactcenterinsightsV1ListAutoLabelingRulesResponse: ...

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1ListChartsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudContactcenterinsightsV1ListChartsResponse: ...

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
class GoogleCloudContactcenterinsightsV1ListDashboardsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudContactcenterinsightsV1ListDashboardsResponse: ...

@typing.type_check_only
class GoogleCloudContactcenterinsightsV1ListDatasetsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudContactcenterinsightsV1ListDatasetsResponse: ...

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
class GoogleCloudContactcenterinsightsV1ListNotesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudContactcenterinsightsV1ListNotesResponse: ...

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
class GoogleCloudContactcenterinsightsV1ListQaQuestionTagsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudContactcenterinsightsV1ListQaQuestionTagsResponse: ...

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
class GoogleCloudContactcenterinsightsV1NoteHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudContactcenterinsightsV1Note: ...

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
class GoogleCloudContactcenterinsightsV1QaQuestionTagHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudContactcenterinsightsV1QaQuestionTag: ...

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
class GoogleCloudContactcenterinsightsV1SearchAuthorizedViewsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudContactcenterinsightsV1SearchAuthorizedViewsResponse: ...

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
class GoogleCloudContactcenterinsightsV1TestAutoLabelingRuleResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudContactcenterinsightsV1TestAutoLabelingRuleResponse: ...

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
class GoogleIamV1PolicyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleIamV1Policy: ...

@typing.type_check_only
class GoogleIamV1TestIamPermissionsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleIamV1TestIamPermissionsResponse: ...

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
