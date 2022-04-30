import collections.abc
import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

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
                    ) -> GoogleCloudDialogflowCxV3ChangelogHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudDialogflowCxV3ListChangelogsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudDialogflowCxV3ListChangelogsResponseHttpRequest,
                        previous_response: GoogleCloudDialogflowCxV3ListChangelogsResponse,
                    ) -> GoogleCloudDialogflowCxV3ListChangelogsResponseHttpRequest | None: ...

                @typing.type_check_only
                class EntityTypesResource(googleapiclient.discovery.Resource):
                    def create(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudDialogflowCxV3EntityType = ...,
                        languageCode: str = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudDialogflowCxV3EntityTypeHttpRequest: ...
                    def delete(
                        self, *, name: str, force: bool = ..., **kwargs: typing.Any
                    ) -> GoogleProtobufEmptyHttpRequest: ...
                    def get(
                        self,
                        *,
                        name: str,
                        languageCode: str = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudDialogflowCxV3EntityTypeHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        languageCode: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudDialogflowCxV3ListEntityTypesResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudDialogflowCxV3ListEntityTypesResponseHttpRequest,
                        previous_response: GoogleCloudDialogflowCxV3ListEntityTypesResponse,
                    ) -> GoogleCloudDialogflowCxV3ListEntityTypesResponseHttpRequest | None: ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudDialogflowCxV3EntityType = ...,
                        languageCode: str = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudDialogflowCxV3EntityTypeHttpRequest: ...

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
                            **kwargs: typing.Any
                        ) -> GoogleCloudDialogflowCxV3ListContinuousTestResultsResponseHttpRequest: ...
                        def list_next(
                            self,
                            previous_request: GoogleCloudDialogflowCxV3ListContinuousTestResultsResponseHttpRequest,
                            previous_response: GoogleCloudDialogflowCxV3ListContinuousTestResultsResponse,
                        ) -> GoogleCloudDialogflowCxV3ListContinuousTestResultsResponseHttpRequest | None: ...

                    @typing.type_check_only
                    class DeploymentsResource(googleapiclient.discovery.Resource):
                        def get(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> GoogleCloudDialogflowCxV3DeploymentHttpRequest: ...
                        def list(
                            self,
                            *,
                            parent: str,
                            pageSize: int = ...,
                            pageToken: str = ...,
                            **kwargs: typing.Any
                        ) -> GoogleCloudDialogflowCxV3ListDeploymentsResponseHttpRequest: ...
                        def list_next(
                            self,
                            previous_request: GoogleCloudDialogflowCxV3ListDeploymentsResponseHttpRequest,
                            previous_response: GoogleCloudDialogflowCxV3ListDeploymentsResponse,
                        ) -> GoogleCloudDialogflowCxV3ListDeploymentsResponseHttpRequest | None: ...

                    @typing.type_check_only
                    class ExperimentsResource(googleapiclient.discovery.Resource):
                        def create(
                            self,
                            *,
                            parent: str,
                            body: GoogleCloudDialogflowCxV3Experiment = ...,
                            **kwargs: typing.Any
                        ) -> GoogleCloudDialogflowCxV3ExperimentHttpRequest: ...
                        def delete(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> GoogleProtobufEmptyHttpRequest: ...
                        def get(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> GoogleCloudDialogflowCxV3ExperimentHttpRequest: ...
                        def list(
                            self,
                            *,
                            parent: str,
                            pageSize: int = ...,
                            pageToken: str = ...,
                            **kwargs: typing.Any
                        ) -> GoogleCloudDialogflowCxV3ListExperimentsResponseHttpRequest: ...
                        def list_next(
                            self,
                            previous_request: GoogleCloudDialogflowCxV3ListExperimentsResponseHttpRequest,
                            previous_response: GoogleCloudDialogflowCxV3ListExperimentsResponse,
                        ) -> GoogleCloudDialogflowCxV3ListExperimentsResponseHttpRequest | None: ...
                        def patch(
                            self,
                            *,
                            name: str,
                            body: GoogleCloudDialogflowCxV3Experiment = ...,
                            updateMask: str = ...,
                            **kwargs: typing.Any
                        ) -> GoogleCloudDialogflowCxV3ExperimentHttpRequest: ...
                        def start(
                            self,
                            *,
                            name: str,
                            body: GoogleCloudDialogflowCxV3StartExperimentRequest = ...,
                            **kwargs: typing.Any
                        ) -> GoogleCloudDialogflowCxV3ExperimentHttpRequest: ...
                        def stop(
                            self,
                            *,
                            name: str,
                            body: GoogleCloudDialogflowCxV3StopExperimentRequest = ...,
                            **kwargs: typing.Any
                        ) -> GoogleCloudDialogflowCxV3ExperimentHttpRequest: ...

                    @typing.type_check_only
                    class SessionsResource(googleapiclient.discovery.Resource):
                        @typing.type_check_only
                        class EntityTypesResource(googleapiclient.discovery.Resource):
                            def create(
                                self,
                                *,
                                parent: str,
                                body: GoogleCloudDialogflowCxV3SessionEntityType = ...,
                                **kwargs: typing.Any
                            ) -> GoogleCloudDialogflowCxV3SessionEntityTypeHttpRequest: ...
                            def delete(
                                self, *, name: str, **kwargs: typing.Any
                            ) -> GoogleProtobufEmptyHttpRequest: ...
                            def get(
                                self, *, name: str, **kwargs: typing.Any
                            ) -> GoogleCloudDialogflowCxV3SessionEntityTypeHttpRequest: ...
                            def list(
                                self,
                                *,
                                parent: str,
                                pageSize: int = ...,
                                pageToken: str = ...,
                                **kwargs: typing.Any
                            ) -> GoogleCloudDialogflowCxV3ListSessionEntityTypesResponseHttpRequest: ...
                            def list_next(
                                self,
                                previous_request: GoogleCloudDialogflowCxV3ListSessionEntityTypesResponseHttpRequest,
                                previous_response: GoogleCloudDialogflowCxV3ListSessionEntityTypesResponse,
                            ) -> GoogleCloudDialogflowCxV3ListSessionEntityTypesResponseHttpRequest | None: ...
                            def patch(
                                self,
                                *,
                                name: str,
                                body: GoogleCloudDialogflowCxV3SessionEntityType = ...,
                                updateMask: str = ...,
                                **kwargs: typing.Any
                            ) -> GoogleCloudDialogflowCxV3SessionEntityTypeHttpRequest: ...

                        def detectIntent(
                            self,
                            *,
                            session: str,
                            body: GoogleCloudDialogflowCxV3DetectIntentRequest = ...,
                            **kwargs: typing.Any
                        ) -> GoogleCloudDialogflowCxV3DetectIntentResponseHttpRequest: ...
                        def fulfillIntent(
                            self,
                            *,
                            session: str,
                            body: GoogleCloudDialogflowCxV3FulfillIntentRequest = ...,
                            **kwargs: typing.Any
                        ) -> GoogleCloudDialogflowCxV3FulfillIntentResponseHttpRequest: ...
                        def matchIntent(
                            self,
                            *,
                            session: str,
                            body: GoogleCloudDialogflowCxV3MatchIntentRequest = ...,
                            **kwargs: typing.Any
                        ) -> GoogleCloudDialogflowCxV3MatchIntentResponseHttpRequest: ...
                        def entityTypes(self) -> EntityTypesResource: ...

                    def create(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudDialogflowCxV3Environment = ...,
                        **kwargs: typing.Any
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleProtobufEmptyHttpRequest: ...
                    def deployFlow(
                        self,
                        *,
                        environment: str,
                        body: GoogleCloudDialogflowCxV3DeployFlowRequest = ...,
                        **kwargs: typing.Any
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleCloudDialogflowCxV3EnvironmentHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudDialogflowCxV3ListEnvironmentsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudDialogflowCxV3ListEnvironmentsResponseHttpRequest,
                        previous_response: GoogleCloudDialogflowCxV3ListEnvironmentsResponse,
                    ) -> GoogleCloudDialogflowCxV3ListEnvironmentsResponseHttpRequest | None: ...
                    def lookupEnvironmentHistory(
                        self,
                        *,
                        name: str,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudDialogflowCxV3LookupEnvironmentHistoryResponseHttpRequest: ...
                    def lookupEnvironmentHistory_next(
                        self,
                        previous_request: GoogleCloudDialogflowCxV3LookupEnvironmentHistoryResponseHttpRequest,
                        previous_response: GoogleCloudDialogflowCxV3LookupEnvironmentHistoryResponse,
                    ) -> GoogleCloudDialogflowCxV3LookupEnvironmentHistoryResponseHttpRequest | None: ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudDialogflowCxV3Environment = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def runContinuousTest(
                        self,
                        *,
                        environment: str,
                        body: GoogleCloudDialogflowCxV3RunContinuousTestRequest = ...,
                        **kwargs: typing.Any
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
                            body: GoogleCloudDialogflowCxV3Page = ...,
                            languageCode: str = ...,
                            **kwargs: typing.Any
                        ) -> GoogleCloudDialogflowCxV3PageHttpRequest: ...
                        def delete(
                            self, *, name: str, force: bool = ..., **kwargs: typing.Any
                        ) -> GoogleProtobufEmptyHttpRequest: ...
                        def get(
                            self,
                            *,
                            name: str,
                            languageCode: str = ...,
                            **kwargs: typing.Any
                        ) -> GoogleCloudDialogflowCxV3PageHttpRequest: ...
                        def list(
                            self,
                            *,
                            parent: str,
                            languageCode: str = ...,
                            pageSize: int = ...,
                            pageToken: str = ...,
                            **kwargs: typing.Any
                        ) -> GoogleCloudDialogflowCxV3ListPagesResponseHttpRequest: ...
                        def list_next(
                            self,
                            previous_request: GoogleCloudDialogflowCxV3ListPagesResponseHttpRequest,
                            previous_response: GoogleCloudDialogflowCxV3ListPagesResponse,
                        ) -> GoogleCloudDialogflowCxV3ListPagesResponseHttpRequest | None: ...
                        def patch(
                            self,
                            *,
                            name: str,
                            body: GoogleCloudDialogflowCxV3Page = ...,
                            languageCode: str = ...,
                            updateMask: str = ...,
                            **kwargs: typing.Any
                        ) -> GoogleCloudDialogflowCxV3PageHttpRequest: ...

                    @typing.type_check_only
                    class TransitionRouteGroupsResource(
                        googleapiclient.discovery.Resource
                    ):
                        def create(
                            self,
                            *,
                            parent: str,
                            body: GoogleCloudDialogflowCxV3TransitionRouteGroup = ...,
                            languageCode: str = ...,
                            **kwargs: typing.Any
                        ) -> GoogleCloudDialogflowCxV3TransitionRouteGroupHttpRequest: ...
                        def delete(
                            self, *, name: str, force: bool = ..., **kwargs: typing.Any
                        ) -> GoogleProtobufEmptyHttpRequest: ...
                        def get(
                            self,
                            *,
                            name: str,
                            languageCode: str = ...,
                            **kwargs: typing.Any
                        ) -> GoogleCloudDialogflowCxV3TransitionRouteGroupHttpRequest: ...
                        def list(
                            self,
                            *,
                            parent: str,
                            languageCode: str = ...,
                            pageSize: int = ...,
                            pageToken: str = ...,
                            **kwargs: typing.Any
                        ) -> GoogleCloudDialogflowCxV3ListTransitionRouteGroupsResponseHttpRequest: ...
                        def list_next(
                            self,
                            previous_request: GoogleCloudDialogflowCxV3ListTransitionRouteGroupsResponseHttpRequest,
                            previous_response: GoogleCloudDialogflowCxV3ListTransitionRouteGroupsResponse,
                        ) -> GoogleCloudDialogflowCxV3ListTransitionRouteGroupsResponseHttpRequest | None: ...
                        def patch(
                            self,
                            *,
                            name: str,
                            body: GoogleCloudDialogflowCxV3TransitionRouteGroup = ...,
                            languageCode: str = ...,
                            updateMask: str = ...,
                            **kwargs: typing.Any
                        ) -> GoogleCloudDialogflowCxV3TransitionRouteGroupHttpRequest: ...

                    @typing.type_check_only
                    class VersionsResource(googleapiclient.discovery.Resource):
                        def compareVersions(
                            self,
                            *,
                            baseVersion: str,
                            body: GoogleCloudDialogflowCxV3CompareVersionsRequest = ...,
                            **kwargs: typing.Any
                        ) -> GoogleCloudDialogflowCxV3CompareVersionsResponseHttpRequest: ...
                        def create(
                            self,
                            *,
                            parent: str,
                            body: GoogleCloudDialogflowCxV3Version = ...,
                            **kwargs: typing.Any
                        ) -> GoogleLongrunningOperationHttpRequest: ...
                        def delete(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> GoogleProtobufEmptyHttpRequest: ...
                        def get(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> GoogleCloudDialogflowCxV3VersionHttpRequest: ...
                        def list(
                            self,
                            *,
                            parent: str,
                            pageSize: int = ...,
                            pageToken: str = ...,
                            **kwargs: typing.Any
                        ) -> GoogleCloudDialogflowCxV3ListVersionsResponseHttpRequest: ...
                        def list_next(
                            self,
                            previous_request: GoogleCloudDialogflowCxV3ListVersionsResponseHttpRequest,
                            previous_response: GoogleCloudDialogflowCxV3ListVersionsResponse,
                        ) -> GoogleCloudDialogflowCxV3ListVersionsResponseHttpRequest | None: ...
                        def load(
                            self,
                            *,
                            name: str,
                            body: GoogleCloudDialogflowCxV3LoadVersionRequest = ...,
                            **kwargs: typing.Any
                        ) -> GoogleLongrunningOperationHttpRequest: ...
                        def patch(
                            self,
                            *,
                            name: str,
                            body: GoogleCloudDialogflowCxV3Version = ...,
                            updateMask: str = ...,
                            **kwargs: typing.Any
                        ) -> GoogleCloudDialogflowCxV3VersionHttpRequest: ...

                    def create(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudDialogflowCxV3Flow = ...,
                        languageCode: str = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudDialogflowCxV3FlowHttpRequest: ...
                    def delete(
                        self, *, name: str, force: bool = ..., **kwargs: typing.Any
                    ) -> GoogleProtobufEmptyHttpRequest: ...
                    def export(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudDialogflowCxV3ExportFlowRequest = ...,
                        **kwargs: typing.Any
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def get(
                        self,
                        *,
                        name: str,
                        languageCode: str = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudDialogflowCxV3FlowHttpRequest: ...
                    def getValidationResult(
                        self,
                        *,
                        name: str,
                        languageCode: str = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudDialogflowCxV3FlowValidationResultHttpRequest: ...
                    def import_(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudDialogflowCxV3ImportFlowRequest = ...,
                        **kwargs: typing.Any
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        languageCode: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudDialogflowCxV3ListFlowsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudDialogflowCxV3ListFlowsResponseHttpRequest,
                        previous_response: GoogleCloudDialogflowCxV3ListFlowsResponse,
                    ) -> GoogleCloudDialogflowCxV3ListFlowsResponseHttpRequest | None: ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudDialogflowCxV3Flow = ...,
                        languageCode: str = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudDialogflowCxV3FlowHttpRequest: ...
                    def train(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudDialogflowCxV3TrainFlowRequest = ...,
                        **kwargs: typing.Any
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def validate(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudDialogflowCxV3ValidateFlowRequest = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudDialogflowCxV3FlowValidationResultHttpRequest: ...
                    def pages(self) -> PagesResource: ...
                    def transitionRouteGroups(
                        self,
                    ) -> TransitionRouteGroupsResource: ...
                    def versions(self) -> VersionsResource: ...

                @typing.type_check_only
                class IntentsResource(googleapiclient.discovery.Resource):
                    def create(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudDialogflowCxV3Intent = ...,
                        languageCode: str = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudDialogflowCxV3IntentHttpRequest: ...
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleProtobufEmptyHttpRequest: ...
                    def get(
                        self,
                        *,
                        name: str,
                        languageCode: str = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudDialogflowCxV3IntentHttpRequest: ...
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
                        **kwargs: typing.Any
                    ) -> GoogleCloudDialogflowCxV3ListIntentsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudDialogflowCxV3ListIntentsResponseHttpRequest,
                        previous_response: GoogleCloudDialogflowCxV3ListIntentsResponse,
                    ) -> GoogleCloudDialogflowCxV3ListIntentsResponseHttpRequest | None: ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudDialogflowCxV3Intent = ...,
                        languageCode: str = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudDialogflowCxV3IntentHttpRequest: ...

                @typing.type_check_only
                class SessionsResource(googleapiclient.discovery.Resource):
                    @typing.type_check_only
                    class EntityTypesResource(googleapiclient.discovery.Resource):
                        def create(
                            self,
                            *,
                            parent: str,
                            body: GoogleCloudDialogflowCxV3SessionEntityType = ...,
                            **kwargs: typing.Any
                        ) -> GoogleCloudDialogflowCxV3SessionEntityTypeHttpRequest: ...
                        def delete(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> GoogleProtobufEmptyHttpRequest: ...
                        def get(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> GoogleCloudDialogflowCxV3SessionEntityTypeHttpRequest: ...
                        def list(
                            self,
                            *,
                            parent: str,
                            pageSize: int = ...,
                            pageToken: str = ...,
                            **kwargs: typing.Any
                        ) -> GoogleCloudDialogflowCxV3ListSessionEntityTypesResponseHttpRequest: ...
                        def list_next(
                            self,
                            previous_request: GoogleCloudDialogflowCxV3ListSessionEntityTypesResponseHttpRequest,
                            previous_response: GoogleCloudDialogflowCxV3ListSessionEntityTypesResponse,
                        ) -> GoogleCloudDialogflowCxV3ListSessionEntityTypesResponseHttpRequest | None: ...
                        def patch(
                            self,
                            *,
                            name: str,
                            body: GoogleCloudDialogflowCxV3SessionEntityType = ...,
                            updateMask: str = ...,
                            **kwargs: typing.Any
                        ) -> GoogleCloudDialogflowCxV3SessionEntityTypeHttpRequest: ...

                    def detectIntent(
                        self,
                        *,
                        session: str,
                        body: GoogleCloudDialogflowCxV3DetectIntentRequest = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudDialogflowCxV3DetectIntentResponseHttpRequest: ...
                    def fulfillIntent(
                        self,
                        *,
                        session: str,
                        body: GoogleCloudDialogflowCxV3FulfillIntentRequest = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudDialogflowCxV3FulfillIntentResponseHttpRequest: ...
                    def matchIntent(
                        self,
                        *,
                        session: str,
                        body: GoogleCloudDialogflowCxV3MatchIntentRequest = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudDialogflowCxV3MatchIntentResponseHttpRequest: ...
                    def entityTypes(self) -> EntityTypesResource: ...

                @typing.type_check_only
                class TestCasesResource(googleapiclient.discovery.Resource):
                    @typing.type_check_only
                    class ResultsResource(googleapiclient.discovery.Resource):
                        def get(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> GoogleCloudDialogflowCxV3TestCaseResultHttpRequest: ...
                        def list(
                            self,
                            *,
                            parent: str,
                            filter: str = ...,
                            pageSize: int = ...,
                            pageToken: str = ...,
                            **kwargs: typing.Any
                        ) -> GoogleCloudDialogflowCxV3ListTestCaseResultsResponseHttpRequest: ...
                        def list_next(
                            self,
                            previous_request: GoogleCloudDialogflowCxV3ListTestCaseResultsResponseHttpRequest,
                            previous_response: GoogleCloudDialogflowCxV3ListTestCaseResultsResponse,
                        ) -> GoogleCloudDialogflowCxV3ListTestCaseResultsResponseHttpRequest | None: ...

                    def batchDelete(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudDialogflowCxV3BatchDeleteTestCasesRequest = ...,
                        **kwargs: typing.Any
                    ) -> GoogleProtobufEmptyHttpRequest: ...
                    def batchRun(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudDialogflowCxV3BatchRunTestCasesRequest = ...,
                        **kwargs: typing.Any
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
                        **kwargs: typing.Any
                    ) -> GoogleCloudDialogflowCxV3CalculateCoverageResponseHttpRequest: ...
                    def create(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudDialogflowCxV3TestCase = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudDialogflowCxV3TestCaseHttpRequest: ...
                    def export(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudDialogflowCxV3ExportTestCasesRequest = ...,
                        **kwargs: typing.Any
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleCloudDialogflowCxV3TestCaseHttpRequest: ...
                    def import_(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudDialogflowCxV3ImportTestCasesRequest = ...,
                        **kwargs: typing.Any
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
                        **kwargs: typing.Any
                    ) -> GoogleCloudDialogflowCxV3ListTestCasesResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudDialogflowCxV3ListTestCasesResponseHttpRequest,
                        previous_response: GoogleCloudDialogflowCxV3ListTestCasesResponse,
                    ) -> GoogleCloudDialogflowCxV3ListTestCasesResponseHttpRequest | None: ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudDialogflowCxV3TestCase = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudDialogflowCxV3TestCaseHttpRequest: ...
                    def run(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudDialogflowCxV3RunTestCaseRequest = ...,
                        **kwargs: typing.Any
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def results(self) -> ResultsResource: ...

                @typing.type_check_only
                class WebhooksResource(googleapiclient.discovery.Resource):
                    def create(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudDialogflowCxV3Webhook = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudDialogflowCxV3WebhookHttpRequest: ...
                    def delete(
                        self, *, name: str, force: bool = ..., **kwargs: typing.Any
                    ) -> GoogleProtobufEmptyHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleCloudDialogflowCxV3WebhookHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudDialogflowCxV3ListWebhooksResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudDialogflowCxV3ListWebhooksResponseHttpRequest,
                        previous_response: GoogleCloudDialogflowCxV3ListWebhooksResponse,
                    ) -> GoogleCloudDialogflowCxV3ListWebhooksResponseHttpRequest | None: ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudDialogflowCxV3Webhook = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudDialogflowCxV3WebhookHttpRequest: ...

                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudDialogflowCxV3Agent = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudDialogflowCxV3AgentHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleProtobufEmptyHttpRequest: ...
                def export(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudDialogflowCxV3ExportAgentRequest = ...,
                    **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudDialogflowCxV3AgentHttpRequest: ...
                def getValidationResult(
                    self, *, name: str, languageCode: str = ..., **kwargs: typing.Any
                ) -> GoogleCloudDialogflowCxV3AgentValidationResultHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudDialogflowCxV3ListAgentsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudDialogflowCxV3ListAgentsResponseHttpRequest,
                    previous_response: GoogleCloudDialogflowCxV3ListAgentsResponse,
                ) -> GoogleCloudDialogflowCxV3ListAgentsResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudDialogflowCxV3Agent = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudDialogflowCxV3AgentHttpRequest: ...
                def restore(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudDialogflowCxV3RestoreAgentRequest = ...,
                    **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def validate(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudDialogflowCxV3ValidateAgentRequest = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudDialogflowCxV3AgentValidationResultHttpRequest: ...
                def changelogs(self) -> ChangelogsResource: ...
                def entityTypes(self) -> EntityTypesResource: ...
                def environments(self) -> EnvironmentsResource: ...
                def flows(self) -> FlowsResource: ...
                def intents(self) -> IntentsResource: ...
                def sessions(self) -> SessionsResource: ...
                def testCases(self) -> TestCasesResource: ...
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
                    **kwargs: typing.Any
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
                    body: GoogleCloudDialogflowCxV3SecuritySettings = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudDialogflowCxV3SecuritySettingsHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleProtobufEmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudDialogflowCxV3SecuritySettingsHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudDialogflowCxV3ListSecuritySettingsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudDialogflowCxV3ListSecuritySettingsResponseHttpRequest,
                    previous_response: GoogleCloudDialogflowCxV3ListSecuritySettingsResponse,
                ) -> GoogleCloudDialogflowCxV3ListSecuritySettingsResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudDialogflowCxV3SecuritySettings = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudDialogflowCxV3SecuritySettingsHttpRequest: ...

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
                **kwargs: typing.Any
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
                **kwargs: typing.Any
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
        | None = ...,
    ) -> googleapiclient.http.BatchHttpRequest: ...
    def projects(self) -> ProjectsResource: ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3AgentHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDialogflowCxV3Agent: ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3AgentValidationResultHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDialogflowCxV3AgentValidationResult: ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3CalculateCoverageResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDialogflowCxV3CalculateCoverageResponse: ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3ChangelogHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDialogflowCxV3Changelog: ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3CompareVersionsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDialogflowCxV3CompareVersionsResponse: ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3DeploymentHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDialogflowCxV3Deployment: ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3DetectIntentResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDialogflowCxV3DetectIntentResponse: ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3EntityTypeHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDialogflowCxV3EntityType: ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3EnvironmentHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDialogflowCxV3Environment: ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3ExperimentHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDialogflowCxV3Experiment: ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3FlowHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDialogflowCxV3Flow: ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3FlowValidationResultHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDialogflowCxV3FlowValidationResult: ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3FulfillIntentResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDialogflowCxV3FulfillIntentResponse: ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3IntentHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDialogflowCxV3Intent: ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3ListAgentsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDialogflowCxV3ListAgentsResponse: ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3ListChangelogsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDialogflowCxV3ListChangelogsResponse: ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3ListContinuousTestResultsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDialogflowCxV3ListContinuousTestResultsResponse: ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3ListDeploymentsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDialogflowCxV3ListDeploymentsResponse: ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3ListEntityTypesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDialogflowCxV3ListEntityTypesResponse: ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3ListEnvironmentsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDialogflowCxV3ListEnvironmentsResponse: ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3ListExperimentsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDialogflowCxV3ListExperimentsResponse: ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3ListFlowsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDialogflowCxV3ListFlowsResponse: ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3ListIntentsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDialogflowCxV3ListIntentsResponse: ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3ListPagesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDialogflowCxV3ListPagesResponse: ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3ListSecuritySettingsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDialogflowCxV3ListSecuritySettingsResponse: ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3ListSessionEntityTypesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDialogflowCxV3ListSessionEntityTypesResponse: ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3ListTestCaseResultsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDialogflowCxV3ListTestCaseResultsResponse: ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3ListTestCasesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDialogflowCxV3ListTestCasesResponse: ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3ListTransitionRouteGroupsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDialogflowCxV3ListTransitionRouteGroupsResponse: ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3ListVersionsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDialogflowCxV3ListVersionsResponse: ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3ListWebhooksResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDialogflowCxV3ListWebhooksResponse: ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3LookupEnvironmentHistoryResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDialogflowCxV3LookupEnvironmentHistoryResponse: ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3MatchIntentResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDialogflowCxV3MatchIntentResponse: ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3PageHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDialogflowCxV3Page: ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3SecuritySettingsHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDialogflowCxV3SecuritySettings: ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3SessionEntityTypeHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDialogflowCxV3SessionEntityType: ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3TestCaseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDialogflowCxV3TestCase: ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3TestCaseResultHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDialogflowCxV3TestCaseResult: ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3TransitionRouteGroupHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDialogflowCxV3TransitionRouteGroup: ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3VersionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDialogflowCxV3Version: ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3WebhookHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDialogflowCxV3Webhook: ...

@typing.type_check_only
class GoogleCloudLocationListLocationsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudLocationListLocationsResponse: ...

@typing.type_check_only
class GoogleCloudLocationLocationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudLocationLocation: ...

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
