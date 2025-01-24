import collections.abc
import typing

import httplib2
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http

from .schemas import *

_list = list

@typing.type_check_only
class DialogflowResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class ProjectsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class LocationsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class AgentsResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class ChangelogsResource(googleapiclient.discovery.Resource):
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleCloudDialogflowCxV3beta1ChangelogHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
                    ) -> (
                        GoogleCloudDialogflowCxV3beta1ListChangelogsResponseHttpRequest
                    ): ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudDialogflowCxV3beta1ListChangelogsResponseHttpRequest,
                        previous_response: GoogleCloudDialogflowCxV3beta1ListChangelogsResponse,
                    ) -> (
                        GoogleCloudDialogflowCxV3beta1ListChangelogsResponseHttpRequest
                        | None
                    ): ...

                @typing.type_check_only
                class ConversationsResource(googleapiclient.discovery.Resource):
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleProtobufEmptyHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleCloudDialogflowCxV3beta1ConversationHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudDialogflowCxV3beta1ListConversationsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudDialogflowCxV3beta1ListConversationsResponseHttpRequest,
                        previous_response: GoogleCloudDialogflowCxV3beta1ListConversationsResponse,
                    ) -> (
                        GoogleCloudDialogflowCxV3beta1ListConversationsResponseHttpRequest
                        | None
                    ): ...

                @typing.type_check_only
                class EntityTypesResource(googleapiclient.discovery.Resource):
                    def create(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudDialogflowCxV3beta1EntityType = ...,
                        languageCode: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudDialogflowCxV3beta1EntityTypeHttpRequest: ...
                    def delete(
                        self, *, name: str, force: bool = ..., **kwargs: typing.Any
                    ) -> GoogleProtobufEmptyHttpRequest: ...
                    def export(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudDialogflowCxV3beta1ExportEntityTypesRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def get(
                        self,
                        *,
                        name: str,
                        languageCode: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudDialogflowCxV3beta1EntityTypeHttpRequest: ...
                    def import_(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudDialogflowCxV3beta1ImportEntityTypesRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        languageCode: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
                    ) -> (
                        GoogleCloudDialogflowCxV3beta1ListEntityTypesResponseHttpRequest
                    ): ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudDialogflowCxV3beta1ListEntityTypesResponseHttpRequest,
                        previous_response: GoogleCloudDialogflowCxV3beta1ListEntityTypesResponse,
                    ) -> (
                        GoogleCloudDialogflowCxV3beta1ListEntityTypesResponseHttpRequest
                        | None
                    ): ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudDialogflowCxV3beta1EntityType = ...,
                        languageCode: str = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudDialogflowCxV3beta1EntityTypeHttpRequest: ...

                @typing.type_check_only
                class EnvironmentsResource(googleapiclient.discovery.Resource):
                    @typing.type_check_only
                    class ContinuousTestResultsResource(
                        googleapiclient.discovery.Resource
                    ):
                        def list(
                            self,
                            *,
                            parent: str,
                            pageSize: int = ...,
                            pageToken: str = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudDialogflowCxV3beta1ListContinuousTestResultsResponseHttpRequest: ...
                        def list_next(
                            self,
                            previous_request: GoogleCloudDialogflowCxV3beta1ListContinuousTestResultsResponseHttpRequest,
                            previous_response: GoogleCloudDialogflowCxV3beta1ListContinuousTestResultsResponse,
                        ) -> (
                            GoogleCloudDialogflowCxV3beta1ListContinuousTestResultsResponseHttpRequest
                            | None
                        ): ...

                    @typing.type_check_only
                    class DeploymentsResource(googleapiclient.discovery.Resource):
                        def get(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> GoogleCloudDialogflowCxV3beta1DeploymentHttpRequest: ...
                        def list(
                            self,
                            *,
                            parent: str,
                            pageSize: int = ...,
                            pageToken: str = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudDialogflowCxV3beta1ListDeploymentsResponseHttpRequest: ...
                        def list_next(
                            self,
                            previous_request: GoogleCloudDialogflowCxV3beta1ListDeploymentsResponseHttpRequest,
                            previous_response: GoogleCloudDialogflowCxV3beta1ListDeploymentsResponse,
                        ) -> (
                            GoogleCloudDialogflowCxV3beta1ListDeploymentsResponseHttpRequest
                            | None
                        ): ...

                    @typing.type_check_only
                    class ExperimentsResource(googleapiclient.discovery.Resource):
                        def create(
                            self,
                            *,
                            parent: str,
                            body: GoogleCloudDialogflowCxV3beta1Experiment = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudDialogflowCxV3beta1ExperimentHttpRequest: ...
                        def delete(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> GoogleProtobufEmptyHttpRequest: ...
                        def get(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> GoogleCloudDialogflowCxV3beta1ExperimentHttpRequest: ...
                        def list(
                            self,
                            *,
                            parent: str,
                            pageSize: int = ...,
                            pageToken: str = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudDialogflowCxV3beta1ListExperimentsResponseHttpRequest: ...
                        def list_next(
                            self,
                            previous_request: GoogleCloudDialogflowCxV3beta1ListExperimentsResponseHttpRequest,
                            previous_response: GoogleCloudDialogflowCxV3beta1ListExperimentsResponse,
                        ) -> (
                            GoogleCloudDialogflowCxV3beta1ListExperimentsResponseHttpRequest
                            | None
                        ): ...
                        def patch(
                            self,
                            *,
                            name: str,
                            body: GoogleCloudDialogflowCxV3beta1Experiment = ...,
                            updateMask: str = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudDialogflowCxV3beta1ExperimentHttpRequest: ...
                        def start(
                            self,
                            *,
                            name: str,
                            body: GoogleCloudDialogflowCxV3beta1StartExperimentRequest = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudDialogflowCxV3beta1ExperimentHttpRequest: ...
                        def stop(
                            self,
                            *,
                            name: str,
                            body: GoogleCloudDialogflowCxV3beta1StopExperimentRequest = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudDialogflowCxV3beta1ExperimentHttpRequest: ...

                    @typing.type_check_only
                    class SessionsResource(googleapiclient.discovery.Resource):
                        @typing.type_check_only
                        class EntityTypesResource(googleapiclient.discovery.Resource):
                            def create(
                                self,
                                *,
                                parent: str,
                                body: GoogleCloudDialogflowCxV3beta1SessionEntityType = ...,
                                **kwargs: typing.Any,
                            ) -> GoogleCloudDialogflowCxV3beta1SessionEntityTypeHttpRequest: ...
                            def delete(
                                self, *, name: str, **kwargs: typing.Any
                            ) -> GoogleProtobufEmptyHttpRequest: ...
                            def get(
                                self, *, name: str, **kwargs: typing.Any
                            ) -> GoogleCloudDialogflowCxV3beta1SessionEntityTypeHttpRequest: ...
                            def list(
                                self,
                                *,
                                parent: str,
                                pageSize: int = ...,
                                pageToken: str = ...,
                                **kwargs: typing.Any,
                            ) -> GoogleCloudDialogflowCxV3beta1ListSessionEntityTypesResponseHttpRequest: ...
                            def list_next(
                                self,
                                previous_request: GoogleCloudDialogflowCxV3beta1ListSessionEntityTypesResponseHttpRequest,
                                previous_response: GoogleCloudDialogflowCxV3beta1ListSessionEntityTypesResponse,
                            ) -> (
                                GoogleCloudDialogflowCxV3beta1ListSessionEntityTypesResponseHttpRequest
                                | None
                            ): ...
                            def patch(
                                self,
                                *,
                                name: str,
                                body: GoogleCloudDialogflowCxV3beta1SessionEntityType = ...,
                                updateMask: str = ...,
                                **kwargs: typing.Any,
                            ) -> GoogleCloudDialogflowCxV3beta1SessionEntityTypeHttpRequest: ...

                        def detectIntent(
                            self,
                            *,
                            session: str,
                            body: GoogleCloudDialogflowCxV3beta1DetectIntentRequest = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudDialogflowCxV3beta1DetectIntentResponseHttpRequest: ...
                        def fulfillIntent(
                            self,
                            *,
                            session: str,
                            body: GoogleCloudDialogflowCxV3beta1FulfillIntentRequest = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudDialogflowCxV3beta1FulfillIntentResponseHttpRequest: ...
                        def matchIntent(
                            self,
                            *,
                            session: str,
                            body: GoogleCloudDialogflowCxV3beta1MatchIntentRequest = ...,
                            **kwargs: typing.Any,
                        ) -> (
                            GoogleCloudDialogflowCxV3beta1MatchIntentResponseHttpRequest
                        ): ...
                        def serverStreamingDetectIntent(
                            self,
                            *,
                            session: str,
                            body: GoogleCloudDialogflowCxV3beta1DetectIntentRequest = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudDialogflowCxV3beta1DetectIntentResponseHttpRequest: ...
                        def entityTypes(self) -> EntityTypesResource: ...

                    def create(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudDialogflowCxV3beta1Environment = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleProtobufEmptyHttpRequest: ...
                    def deployFlow(
                        self,
                        *,
                        environment: str,
                        body: GoogleCloudDialogflowCxV3beta1DeployFlowRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleCloudDialogflowCxV3beta1EnvironmentHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudDialogflowCxV3beta1ListEnvironmentsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudDialogflowCxV3beta1ListEnvironmentsResponseHttpRequest,
                        previous_response: GoogleCloudDialogflowCxV3beta1ListEnvironmentsResponse,
                    ) -> (
                        GoogleCloudDialogflowCxV3beta1ListEnvironmentsResponseHttpRequest
                        | None
                    ): ...
                    def lookupEnvironmentHistory(
                        self,
                        *,
                        name: str,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudDialogflowCxV3beta1LookupEnvironmentHistoryResponseHttpRequest: ...
                    def lookupEnvironmentHistory_next(
                        self,
                        previous_request: GoogleCloudDialogflowCxV3beta1LookupEnvironmentHistoryResponseHttpRequest,
                        previous_response: GoogleCloudDialogflowCxV3beta1LookupEnvironmentHistoryResponse,
                    ) -> (
                        GoogleCloudDialogflowCxV3beta1LookupEnvironmentHistoryResponseHttpRequest
                        | None
                    ): ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudDialogflowCxV3beta1Environment = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def runContinuousTest(
                        self,
                        *,
                        environment: str,
                        body: GoogleCloudDialogflowCxV3beta1RunContinuousTestRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def continuousTestResults(
                        self,
                    ) -> ContinuousTestResultsResource: ...
                    def deployments(self) -> DeploymentsResource: ...
                    def experiments(self) -> ExperimentsResource: ...
                    def sessions(self) -> SessionsResource: ...

                @typing.type_check_only
                class FlowsResource(googleapiclient.discovery.Resource):
                    @typing.type_check_only
                    class PagesResource(googleapiclient.discovery.Resource):
                        def create(
                            self,
                            *,
                            parent: str,
                            body: GoogleCloudDialogflowCxV3beta1Page = ...,
                            languageCode: str = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudDialogflowCxV3beta1PageHttpRequest: ...
                        def delete(
                            self, *, name: str, force: bool = ..., **kwargs: typing.Any
                        ) -> GoogleProtobufEmptyHttpRequest: ...
                        def get(
                            self,
                            *,
                            name: str,
                            languageCode: str = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudDialogflowCxV3beta1PageHttpRequest: ...
                        def list(
                            self,
                            *,
                            parent: str,
                            languageCode: str = ...,
                            pageSize: int = ...,
                            pageToken: str = ...,
                            **kwargs: typing.Any,
                        ) -> (
                            GoogleCloudDialogflowCxV3beta1ListPagesResponseHttpRequest
                        ): ...
                        def list_next(
                            self,
                            previous_request: GoogleCloudDialogflowCxV3beta1ListPagesResponseHttpRequest,
                            previous_response: GoogleCloudDialogflowCxV3beta1ListPagesResponse,
                        ) -> (
                            GoogleCloudDialogflowCxV3beta1ListPagesResponseHttpRequest
                            | None
                        ): ...
                        def patch(
                            self,
                            *,
                            name: str,
                            body: GoogleCloudDialogflowCxV3beta1Page = ...,
                            languageCode: str = ...,
                            updateMask: str = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudDialogflowCxV3beta1PageHttpRequest: ...

                    @typing.type_check_only
                    class TransitionRouteGroupsResource(
                        googleapiclient.discovery.Resource
                    ):
                        def create(
                            self,
                            *,
                            parent: str,
                            body: GoogleCloudDialogflowCxV3beta1TransitionRouteGroup = ...,
                            languageCode: str = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudDialogflowCxV3beta1TransitionRouteGroupHttpRequest: ...
                        def delete(
                            self, *, name: str, force: bool = ..., **kwargs: typing.Any
                        ) -> GoogleProtobufEmptyHttpRequest: ...
                        def get(
                            self,
                            *,
                            name: str,
                            languageCode: str = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudDialogflowCxV3beta1TransitionRouteGroupHttpRequest: ...
                        def list(
                            self,
                            *,
                            parent: str,
                            languageCode: str = ...,
                            pageSize: int = ...,
                            pageToken: str = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudDialogflowCxV3beta1ListTransitionRouteGroupsResponseHttpRequest: ...
                        def list_next(
                            self,
                            previous_request: GoogleCloudDialogflowCxV3beta1ListTransitionRouteGroupsResponseHttpRequest,
                            previous_response: GoogleCloudDialogflowCxV3beta1ListTransitionRouteGroupsResponse,
                        ) -> (
                            GoogleCloudDialogflowCxV3beta1ListTransitionRouteGroupsResponseHttpRequest
                            | None
                        ): ...
                        def patch(
                            self,
                            *,
                            name: str,
                            body: GoogleCloudDialogflowCxV3beta1TransitionRouteGroup = ...,
                            languageCode: str = ...,
                            updateMask: str = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudDialogflowCxV3beta1TransitionRouteGroupHttpRequest: ...

                    @typing.type_check_only
                    class VersionsResource(googleapiclient.discovery.Resource):
                        def compareVersions(
                            self,
                            *,
                            baseVersion: str,
                            body: GoogleCloudDialogflowCxV3beta1CompareVersionsRequest = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudDialogflowCxV3beta1CompareVersionsResponseHttpRequest: ...
                        def create(
                            self,
                            *,
                            parent: str,
                            body: GoogleCloudDialogflowCxV3beta1Version = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleLongrunningOperationHttpRequest: ...
                        def delete(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> GoogleProtobufEmptyHttpRequest: ...
                        def get(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> GoogleCloudDialogflowCxV3beta1VersionHttpRequest: ...
                        def list(
                            self,
                            *,
                            parent: str,
                            pageSize: int = ...,
                            pageToken: str = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudDialogflowCxV3beta1ListVersionsResponseHttpRequest: ...
                        def list_next(
                            self,
                            previous_request: GoogleCloudDialogflowCxV3beta1ListVersionsResponseHttpRequest,
                            previous_response: GoogleCloudDialogflowCxV3beta1ListVersionsResponse,
                        ) -> (
                            GoogleCloudDialogflowCxV3beta1ListVersionsResponseHttpRequest
                            | None
                        ): ...
                        def load(
                            self,
                            *,
                            name: str,
                            body: GoogleCloudDialogflowCxV3beta1LoadVersionRequest = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleLongrunningOperationHttpRequest: ...
                        def patch(
                            self,
                            *,
                            name: str,
                            body: GoogleCloudDialogflowCxV3beta1Version = ...,
                            updateMask: str = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudDialogflowCxV3beta1VersionHttpRequest: ...

                    def create(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudDialogflowCxV3beta1Flow = ...,
                        languageCode: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudDialogflowCxV3beta1FlowHttpRequest: ...
                    def delete(
                        self, *, name: str, force: bool = ..., **kwargs: typing.Any
                    ) -> GoogleProtobufEmptyHttpRequest: ...
                    def export(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudDialogflowCxV3beta1ExportFlowRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def get(
                        self,
                        *,
                        name: str,
                        languageCode: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudDialogflowCxV3beta1FlowHttpRequest: ...
                    def getValidationResult(
                        self,
                        *,
                        name: str,
                        languageCode: str = ...,
                        **kwargs: typing.Any,
                    ) -> (
                        GoogleCloudDialogflowCxV3beta1FlowValidationResultHttpRequest
                    ): ...
                    def import_(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudDialogflowCxV3beta1ImportFlowRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        languageCode: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudDialogflowCxV3beta1ListFlowsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudDialogflowCxV3beta1ListFlowsResponseHttpRequest,
                        previous_response: GoogleCloudDialogflowCxV3beta1ListFlowsResponse,
                    ) -> (
                        GoogleCloudDialogflowCxV3beta1ListFlowsResponseHttpRequest
                        | None
                    ): ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudDialogflowCxV3beta1Flow = ...,
                        languageCode: str = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudDialogflowCxV3beta1FlowHttpRequest: ...
                    def train(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudDialogflowCxV3beta1TrainFlowRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def validate(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudDialogflowCxV3beta1ValidateFlowRequest = ...,
                        **kwargs: typing.Any,
                    ) -> (
                        GoogleCloudDialogflowCxV3beta1FlowValidationResultHttpRequest
                    ): ...
                    def pages(self) -> PagesResource: ...
                    def transitionRouteGroups(
                        self,
                    ) -> TransitionRouteGroupsResource: ...
                    def versions(self) -> VersionsResource: ...

                @typing.type_check_only
                class GeneratorsResource(googleapiclient.discovery.Resource):
                    def create(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudDialogflowCxV3beta1Generator = ...,
                        languageCode: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudDialogflowCxV3beta1GeneratorHttpRequest: ...
                    def delete(
                        self, *, name: str, force: bool = ..., **kwargs: typing.Any
                    ) -> GoogleProtobufEmptyHttpRequest: ...
                    def get(
                        self,
                        *,
                        name: str,
                        languageCode: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudDialogflowCxV3beta1GeneratorHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        languageCode: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
                    ) -> (
                        GoogleCloudDialogflowCxV3beta1ListGeneratorsResponseHttpRequest
                    ): ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudDialogflowCxV3beta1ListGeneratorsResponseHttpRequest,
                        previous_response: GoogleCloudDialogflowCxV3beta1ListGeneratorsResponse,
                    ) -> (
                        GoogleCloudDialogflowCxV3beta1ListGeneratorsResponseHttpRequest
                        | None
                    ): ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudDialogflowCxV3beta1Generator = ...,
                        languageCode: str = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudDialogflowCxV3beta1GeneratorHttpRequest: ...

                @typing.type_check_only
                class IntentsResource(googleapiclient.discovery.Resource):
                    def create(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudDialogflowCxV3beta1Intent = ...,
                        languageCode: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudDialogflowCxV3beta1IntentHttpRequest: ...
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleProtobufEmptyHttpRequest: ...
                    def export(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudDialogflowCxV3beta1ExportIntentsRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def get(
                        self,
                        *,
                        name: str,
                        languageCode: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudDialogflowCxV3beta1IntentHttpRequest: ...
                    def import_(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudDialogflowCxV3beta1ImportIntentsRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        intentView: typing_extensions.Literal[
                            "INTENT_VIEW_UNSPECIFIED",
                            "INTENT_VIEW_PARTIAL",
                            "INTENT_VIEW_FULL",
                        ] = ...,
                        languageCode: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
                    ) -> (
                        GoogleCloudDialogflowCxV3beta1ListIntentsResponseHttpRequest
                    ): ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudDialogflowCxV3beta1ListIntentsResponseHttpRequest,
                        previous_response: GoogleCloudDialogflowCxV3beta1ListIntentsResponse,
                    ) -> (
                        GoogleCloudDialogflowCxV3beta1ListIntentsResponseHttpRequest
                        | None
                    ): ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudDialogflowCxV3beta1Intent = ...,
                        languageCode: str = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudDialogflowCxV3beta1IntentHttpRequest: ...

                @typing.type_check_only
                class PlaybooksResource(googleapiclient.discovery.Resource):
                    @typing.type_check_only
                    class ExamplesResource(googleapiclient.discovery.Resource):
                        def create(
                            self,
                            *,
                            parent: str,
                            body: GoogleCloudDialogflowCxV3beta1Example = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudDialogflowCxV3beta1ExampleHttpRequest: ...
                        def delete(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> GoogleProtobufEmptyHttpRequest: ...
                        def get(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> GoogleCloudDialogflowCxV3beta1ExampleHttpRequest: ...
                        def list(
                            self,
                            *,
                            parent: str,
                            languageCode: str = ...,
                            pageSize: int = ...,
                            pageToken: str = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudDialogflowCxV3beta1ListExamplesResponseHttpRequest: ...
                        def list_next(
                            self,
                            previous_request: GoogleCloudDialogflowCxV3beta1ListExamplesResponseHttpRequest,
                            previous_response: GoogleCloudDialogflowCxV3beta1ListExamplesResponse,
                        ) -> (
                            GoogleCloudDialogflowCxV3beta1ListExamplesResponseHttpRequest
                            | None
                        ): ...
                        def patch(
                            self,
                            *,
                            name: str,
                            body: GoogleCloudDialogflowCxV3beta1Example = ...,
                            updateMask: str = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudDialogflowCxV3beta1ExampleHttpRequest: ...

                    @typing.type_check_only
                    class VersionsResource(googleapiclient.discovery.Resource):
                        def create(
                            self,
                            *,
                            parent: str,
                            body: GoogleCloudDialogflowCxV3beta1PlaybookVersion = ...,
                            **kwargs: typing.Any,
                        ) -> (
                            GoogleCloudDialogflowCxV3beta1PlaybookVersionHttpRequest
                        ): ...
                        def delete(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> GoogleProtobufEmptyHttpRequest: ...
                        def get(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> (
                            GoogleCloudDialogflowCxV3beta1PlaybookVersionHttpRequest
                        ): ...
                        def list(
                            self,
                            *,
                            parent: str,
                            pageSize: int = ...,
                            pageToken: str = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudDialogflowCxV3beta1ListPlaybookVersionsResponseHttpRequest: ...
                        def list_next(
                            self,
                            previous_request: GoogleCloudDialogflowCxV3beta1ListPlaybookVersionsResponseHttpRequest,
                            previous_response: GoogleCloudDialogflowCxV3beta1ListPlaybookVersionsResponse,
                        ) -> (
                            GoogleCloudDialogflowCxV3beta1ListPlaybookVersionsResponseHttpRequest
                            | None
                        ): ...
                        def restore(
                            self,
                            *,
                            name: str,
                            body: GoogleCloudDialogflowCxV3beta1RestorePlaybookVersionRequest = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudDialogflowCxV3beta1RestorePlaybookVersionResponseHttpRequest: ...

                    def create(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudDialogflowCxV3beta1Playbook = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudDialogflowCxV3beta1PlaybookHttpRequest: ...
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleProtobufEmptyHttpRequest: ...
                    def export(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudDialogflowCxV3beta1ExportPlaybookRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleCloudDialogflowCxV3beta1PlaybookHttpRequest: ...
                    def import_(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudDialogflowCxV3beta1ImportPlaybookRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
                    ) -> (
                        GoogleCloudDialogflowCxV3beta1ListPlaybooksResponseHttpRequest
                    ): ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudDialogflowCxV3beta1ListPlaybooksResponseHttpRequest,
                        previous_response: GoogleCloudDialogflowCxV3beta1ListPlaybooksResponse,
                    ) -> (
                        GoogleCloudDialogflowCxV3beta1ListPlaybooksResponseHttpRequest
                        | None
                    ): ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudDialogflowCxV3beta1Playbook = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudDialogflowCxV3beta1PlaybookHttpRequest: ...
                    def examples(self) -> ExamplesResource: ...
                    def versions(self) -> VersionsResource: ...

                @typing.type_check_only
                class SessionsResource(googleapiclient.discovery.Resource):
                    @typing.type_check_only
                    class EntityTypesResource(googleapiclient.discovery.Resource):
                        def create(
                            self,
                            *,
                            parent: str,
                            body: GoogleCloudDialogflowCxV3beta1SessionEntityType = ...,
                            **kwargs: typing.Any,
                        ) -> (
                            GoogleCloudDialogflowCxV3beta1SessionEntityTypeHttpRequest
                        ): ...
                        def delete(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> GoogleProtobufEmptyHttpRequest: ...
                        def get(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> (
                            GoogleCloudDialogflowCxV3beta1SessionEntityTypeHttpRequest
                        ): ...
                        def list(
                            self,
                            *,
                            parent: str,
                            pageSize: int = ...,
                            pageToken: str = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudDialogflowCxV3beta1ListSessionEntityTypesResponseHttpRequest: ...
                        def list_next(
                            self,
                            previous_request: GoogleCloudDialogflowCxV3beta1ListSessionEntityTypesResponseHttpRequest,
                            previous_response: GoogleCloudDialogflowCxV3beta1ListSessionEntityTypesResponse,
                        ) -> (
                            GoogleCloudDialogflowCxV3beta1ListSessionEntityTypesResponseHttpRequest
                            | None
                        ): ...
                        def patch(
                            self,
                            *,
                            name: str,
                            body: GoogleCloudDialogflowCxV3beta1SessionEntityType = ...,
                            updateMask: str = ...,
                            **kwargs: typing.Any,
                        ) -> (
                            GoogleCloudDialogflowCxV3beta1SessionEntityTypeHttpRequest
                        ): ...

                    def detectIntent(
                        self,
                        *,
                        session: str,
                        body: GoogleCloudDialogflowCxV3beta1DetectIntentRequest = ...,
                        **kwargs: typing.Any,
                    ) -> (
                        GoogleCloudDialogflowCxV3beta1DetectIntentResponseHttpRequest
                    ): ...
                    def fulfillIntent(
                        self,
                        *,
                        session: str,
                        body: GoogleCloudDialogflowCxV3beta1FulfillIntentRequest = ...,
                        **kwargs: typing.Any,
                    ) -> (
                        GoogleCloudDialogflowCxV3beta1FulfillIntentResponseHttpRequest
                    ): ...
                    def matchIntent(
                        self,
                        *,
                        session: str,
                        body: GoogleCloudDialogflowCxV3beta1MatchIntentRequest = ...,
                        **kwargs: typing.Any,
                    ) -> (
                        GoogleCloudDialogflowCxV3beta1MatchIntentResponseHttpRequest
                    ): ...
                    def serverStreamingDetectIntent(
                        self,
                        *,
                        session: str,
                        body: GoogleCloudDialogflowCxV3beta1DetectIntentRequest = ...,
                        **kwargs: typing.Any,
                    ) -> (
                        GoogleCloudDialogflowCxV3beta1DetectIntentResponseHttpRequest
                    ): ...
                    def submitAnswerFeedback(
                        self,
                        *,
                        session: str,
                        body: GoogleCloudDialogflowCxV3beta1SubmitAnswerFeedbackRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudDialogflowCxV3beta1AnswerFeedbackHttpRequest: ...
                    def entityTypes(self) -> EntityTypesResource: ...

                @typing.type_check_only
                class TestCasesResource(googleapiclient.discovery.Resource):
                    @typing.type_check_only
                    class ResultsResource(googleapiclient.discovery.Resource):
                        def get(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> (
                            GoogleCloudDialogflowCxV3beta1TestCaseResultHttpRequest
                        ): ...
                        def list(
                            self,
                            *,
                            parent: str,
                            filter: str = ...,
                            pageSize: int = ...,
                            pageToken: str = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudDialogflowCxV3beta1ListTestCaseResultsResponseHttpRequest: ...
                        def list_next(
                            self,
                            previous_request: GoogleCloudDialogflowCxV3beta1ListTestCaseResultsResponseHttpRequest,
                            previous_response: GoogleCloudDialogflowCxV3beta1ListTestCaseResultsResponse,
                        ) -> (
                            GoogleCloudDialogflowCxV3beta1ListTestCaseResultsResponseHttpRequest
                            | None
                        ): ...

                    def batchDelete(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudDialogflowCxV3beta1BatchDeleteTestCasesRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleProtobufEmptyHttpRequest: ...
                    def batchRun(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudDialogflowCxV3beta1BatchRunTestCasesRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def calculateCoverage(
                        self,
                        *,
                        agent: str,
                        type: typing_extensions.Literal[
                            "COVERAGE_TYPE_UNSPECIFIED",
                            "INTENT",
                            "PAGE_TRANSITION",
                            "TRANSITION_ROUTE_GROUP",
                        ] = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudDialogflowCxV3beta1CalculateCoverageResponseHttpRequest: ...
                    def create(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudDialogflowCxV3beta1TestCase = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudDialogflowCxV3beta1TestCaseHttpRequest: ...
                    def export(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudDialogflowCxV3beta1ExportTestCasesRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleCloudDialogflowCxV3beta1TestCaseHttpRequest: ...
                    def import_(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudDialogflowCxV3beta1ImportTestCasesRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        view: typing_extensions.Literal[
                            "TEST_CASE_VIEW_UNSPECIFIED", "BASIC", "FULL"
                        ] = ...,
                        **kwargs: typing.Any,
                    ) -> (
                        GoogleCloudDialogflowCxV3beta1ListTestCasesResponseHttpRequest
                    ): ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudDialogflowCxV3beta1ListTestCasesResponseHttpRequest,
                        previous_response: GoogleCloudDialogflowCxV3beta1ListTestCasesResponse,
                    ) -> (
                        GoogleCloudDialogflowCxV3beta1ListTestCasesResponseHttpRequest
                        | None
                    ): ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudDialogflowCxV3beta1TestCase = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudDialogflowCxV3beta1TestCaseHttpRequest: ...
                    def run(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudDialogflowCxV3beta1RunTestCaseRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def results(self) -> ResultsResource: ...

                @typing.type_check_only
                class ToolsResource(googleapiclient.discovery.Resource):
                    def create(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudDialogflowCxV3beta1Tool = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudDialogflowCxV3beta1ToolHttpRequest: ...
                    def delete(
                        self, *, name: str, force: bool = ..., **kwargs: typing.Any
                    ) -> GoogleProtobufEmptyHttpRequest: ...
                    def export(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudDialogflowCxV3beta1ExportToolsRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleCloudDialogflowCxV3beta1ToolHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudDialogflowCxV3beta1ListToolsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudDialogflowCxV3beta1ListToolsResponseHttpRequest,
                        previous_response: GoogleCloudDialogflowCxV3beta1ListToolsResponse,
                    ) -> (
                        GoogleCloudDialogflowCxV3beta1ListToolsResponseHttpRequest
                        | None
                    ): ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudDialogflowCxV3beta1Tool = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudDialogflowCxV3beta1ToolHttpRequest: ...

                @typing.type_check_only
                class TransitionRouteGroupsResource(googleapiclient.discovery.Resource):
                    def create(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudDialogflowCxV3beta1TransitionRouteGroup = ...,
                        languageCode: str = ...,
                        **kwargs: typing.Any,
                    ) -> (
                        GoogleCloudDialogflowCxV3beta1TransitionRouteGroupHttpRequest
                    ): ...
                    def delete(
                        self, *, name: str, force: bool = ..., **kwargs: typing.Any
                    ) -> GoogleProtobufEmptyHttpRequest: ...
                    def get(
                        self,
                        *,
                        name: str,
                        languageCode: str = ...,
                        **kwargs: typing.Any,
                    ) -> (
                        GoogleCloudDialogflowCxV3beta1TransitionRouteGroupHttpRequest
                    ): ...
                    def list(
                        self,
                        *,
                        parent: str,
                        languageCode: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudDialogflowCxV3beta1ListTransitionRouteGroupsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudDialogflowCxV3beta1ListTransitionRouteGroupsResponseHttpRequest,
                        previous_response: GoogleCloudDialogflowCxV3beta1ListTransitionRouteGroupsResponse,
                    ) -> (
                        GoogleCloudDialogflowCxV3beta1ListTransitionRouteGroupsResponseHttpRequest
                        | None
                    ): ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudDialogflowCxV3beta1TransitionRouteGroup = ...,
                        languageCode: str = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any,
                    ) -> (
                        GoogleCloudDialogflowCxV3beta1TransitionRouteGroupHttpRequest
                    ): ...

                @typing.type_check_only
                class WebhooksResource(googleapiclient.discovery.Resource):
                    def create(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudDialogflowCxV3beta1Webhook = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudDialogflowCxV3beta1WebhookHttpRequest: ...
                    def delete(
                        self, *, name: str, force: bool = ..., **kwargs: typing.Any
                    ) -> GoogleProtobufEmptyHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleCloudDialogflowCxV3beta1WebhookHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
                    ) -> (
                        GoogleCloudDialogflowCxV3beta1ListWebhooksResponseHttpRequest
                    ): ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudDialogflowCxV3beta1ListWebhooksResponseHttpRequest,
                        previous_response: GoogleCloudDialogflowCxV3beta1ListWebhooksResponse,
                    ) -> (
                        GoogleCloudDialogflowCxV3beta1ListWebhooksResponseHttpRequest
                        | None
                    ): ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudDialogflowCxV3beta1Webhook = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudDialogflowCxV3beta1WebhookHttpRequest: ...

                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudDialogflowCxV3beta1Agent = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudDialogflowCxV3beta1AgentHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleProtobufEmptyHttpRequest: ...
                def export(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudDialogflowCxV3beta1ExportAgentRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudDialogflowCxV3beta1AgentHttpRequest: ...
                def getGenerativeSettings(
                    self, *, name: str, languageCode: str = ..., **kwargs: typing.Any
                ) -> GoogleCloudDialogflowCxV3beta1GenerativeSettingsHttpRequest: ...
                def getValidationResult(
                    self, *, name: str, languageCode: str = ..., **kwargs: typing.Any
                ) -> GoogleCloudDialogflowCxV3beta1AgentValidationResultHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudDialogflowCxV3beta1ListAgentsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudDialogflowCxV3beta1ListAgentsResponseHttpRequest,
                    previous_response: GoogleCloudDialogflowCxV3beta1ListAgentsResponse,
                ) -> (
                    GoogleCloudDialogflowCxV3beta1ListAgentsResponseHttpRequest | None
                ): ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudDialogflowCxV3beta1Agent = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudDialogflowCxV3beta1AgentHttpRequest: ...
                def restore(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudDialogflowCxV3beta1RestoreAgentRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def updateGenerativeSettings(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudDialogflowCxV3beta1GenerativeSettings = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudDialogflowCxV3beta1GenerativeSettingsHttpRequest: ...
                def validate(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudDialogflowCxV3beta1ValidateAgentRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudDialogflowCxV3beta1AgentValidationResultHttpRequest: ...
                def changelogs(self) -> ChangelogsResource: ...
                def conversations(self) -> ConversationsResource: ...
                def entityTypes(self) -> EntityTypesResource: ...
                def environments(self) -> EnvironmentsResource: ...
                def flows(self) -> FlowsResource: ...
                def generators(self) -> GeneratorsResource: ...
                def intents(self) -> IntentsResource: ...
                def playbooks(self) -> PlaybooksResource: ...
                def sessions(self) -> SessionsResource: ...
                def testCases(self) -> TestCasesResource: ...
                def tools(self) -> ToolsResource: ...
                def transitionRouteGroups(self) -> TransitionRouteGroupsResource: ...
                def webhooks(self) -> WebhooksResource: ...

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
            class SecuritySettingsResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudDialogflowCxV3beta1SecuritySettings = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudDialogflowCxV3beta1SecuritySettingsHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleProtobufEmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudDialogflowCxV3beta1SecuritySettingsHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudDialogflowCxV3beta1ListSecuritySettingsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudDialogflowCxV3beta1ListSecuritySettingsResponseHttpRequest,
                    previous_response: GoogleCloudDialogflowCxV3beta1ListSecuritySettingsResponse,
                ) -> (
                    GoogleCloudDialogflowCxV3beta1ListSecuritySettingsResponseHttpRequest
                    | None
                ): ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudDialogflowCxV3beta1SecuritySettings = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudDialogflowCxV3beta1SecuritySettingsHttpRequest: ...

            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleCloudLocationLocationHttpRequest: ...
            def list(
                self,
                *,
                name: str,
                filter: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any,
            ) -> GoogleCloudLocationListLocationsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: GoogleCloudLocationListLocationsResponseHttpRequest,
                previous_response: GoogleCloudLocationListLocationsResponse,
            ) -> GoogleCloudLocationListLocationsResponseHttpRequest | None: ...
            def agents(self) -> AgentsResource: ...
            def operations(self) -> OperationsResource: ...
            def securitySettings(self) -> SecuritySettingsResource: ...

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

        def locations(self) -> LocationsResource: ...
        def operations(self) -> OperationsResource: ...

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
class GoogleCloudDialogflowCxV3beta1AgentHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDialogflowCxV3beta1Agent: ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1AgentValidationResultHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDialogflowCxV3beta1AgentValidationResult: ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1AnswerFeedbackHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDialogflowCxV3beta1AnswerFeedback: ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1CalculateCoverageResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDialogflowCxV3beta1CalculateCoverageResponse: ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ChangelogHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDialogflowCxV3beta1Changelog: ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1CompareVersionsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDialogflowCxV3beta1CompareVersionsResponse: ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ConversationHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDialogflowCxV3beta1Conversation: ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1DeploymentHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDialogflowCxV3beta1Deployment: ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1DetectIntentResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDialogflowCxV3beta1DetectIntentResponse: ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1EntityTypeHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDialogflowCxV3beta1EntityType: ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1EnvironmentHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDialogflowCxV3beta1Environment: ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ExampleHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDialogflowCxV3beta1Example: ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ExperimentHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDialogflowCxV3beta1Experiment: ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1FlowHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDialogflowCxV3beta1Flow: ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1FlowValidationResultHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDialogflowCxV3beta1FlowValidationResult: ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1FulfillIntentResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDialogflowCxV3beta1FulfillIntentResponse: ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1GenerativeSettingsHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDialogflowCxV3beta1GenerativeSettings: ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1GeneratorHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDialogflowCxV3beta1Generator: ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1IntentHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDialogflowCxV3beta1Intent: ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ListAgentsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDialogflowCxV3beta1ListAgentsResponse: ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ListChangelogsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDialogflowCxV3beta1ListChangelogsResponse: ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ListContinuousTestResultsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDialogflowCxV3beta1ListContinuousTestResultsResponse: ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ListConversationsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDialogflowCxV3beta1ListConversationsResponse: ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ListDeploymentsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDialogflowCxV3beta1ListDeploymentsResponse: ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ListEntityTypesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDialogflowCxV3beta1ListEntityTypesResponse: ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ListEnvironmentsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDialogflowCxV3beta1ListEnvironmentsResponse: ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ListExamplesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDialogflowCxV3beta1ListExamplesResponse: ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ListExperimentsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDialogflowCxV3beta1ListExperimentsResponse: ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ListFlowsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDialogflowCxV3beta1ListFlowsResponse: ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ListGeneratorsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDialogflowCxV3beta1ListGeneratorsResponse: ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ListIntentsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDialogflowCxV3beta1ListIntentsResponse: ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ListPagesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDialogflowCxV3beta1ListPagesResponse: ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ListPlaybookVersionsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDialogflowCxV3beta1ListPlaybookVersionsResponse: ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ListPlaybooksResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDialogflowCxV3beta1ListPlaybooksResponse: ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ListSecuritySettingsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDialogflowCxV3beta1ListSecuritySettingsResponse: ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ListSessionEntityTypesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDialogflowCxV3beta1ListSessionEntityTypesResponse: ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ListTestCaseResultsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDialogflowCxV3beta1ListTestCaseResultsResponse: ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ListTestCasesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDialogflowCxV3beta1ListTestCasesResponse: ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ListToolsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDialogflowCxV3beta1ListToolsResponse: ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ListTransitionRouteGroupsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDialogflowCxV3beta1ListTransitionRouteGroupsResponse: ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ListVersionsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDialogflowCxV3beta1ListVersionsResponse: ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ListWebhooksResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDialogflowCxV3beta1ListWebhooksResponse: ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1LookupEnvironmentHistoryResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDialogflowCxV3beta1LookupEnvironmentHistoryResponse: ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1MatchIntentResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDialogflowCxV3beta1MatchIntentResponse: ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1PageHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDialogflowCxV3beta1Page: ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1PlaybookHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDialogflowCxV3beta1Playbook: ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1PlaybookVersionHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDialogflowCxV3beta1PlaybookVersion: ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1RestorePlaybookVersionResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDialogflowCxV3beta1RestorePlaybookVersionResponse: ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1SecuritySettingsHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDialogflowCxV3beta1SecuritySettings: ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1SessionEntityTypeHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDialogflowCxV3beta1SessionEntityType: ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1TestCaseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDialogflowCxV3beta1TestCase: ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1TestCaseResultHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDialogflowCxV3beta1TestCaseResult: ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ToolHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDialogflowCxV3beta1Tool: ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1TransitionRouteGroupHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDialogflowCxV3beta1TransitionRouteGroup: ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1VersionHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDialogflowCxV3beta1Version: ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1WebhookHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDialogflowCxV3beta1Webhook: ...

@typing.type_check_only
class GoogleCloudLocationListLocationsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudLocationListLocationsResponse: ...

@typing.type_check_only
class GoogleCloudLocationLocationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudLocationLocation: ...

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
