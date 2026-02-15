import collections.abc
import typing

import httplib2
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http

from .schemas import *

_list = list

@typing.type_check_only
class CustomerEngagementSuiteResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class ProjectsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class LocationsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class AppsResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class AgentsResource(googleapiclient.discovery.Resource):
                    def create(
                        self,
                        *,
                        parent: str,
                        body: Agent = ...,
                        agentId: str = ...,
                        **kwargs: typing.Any,
                    ) -> AgentHttpRequest: ...
                    def delete(
                        self,
                        *,
                        name: str,
                        etag: str = ...,
                        force: bool = ...,
                        **kwargs: typing.Any,
                    ) -> EmptyHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> AgentHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str = ...,
                        orderBy: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
                    ) -> ListAgentsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: ListAgentsResponseHttpRequest,
                        previous_response: ListAgentsResponse,
                    ) -> ListAgentsResponseHttpRequest | None: ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: Agent = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any,
                    ) -> AgentHttpRequest: ...

                @typing.type_check_only
                class ChangelogsResource(googleapiclient.discovery.Resource):
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> ChangelogHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str = ...,
                        orderBy: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
                    ) -> ListChangelogsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: ListChangelogsResponseHttpRequest,
                        previous_response: ListChangelogsResponse,
                    ) -> ListChangelogsResponseHttpRequest | None: ...

                @typing.type_check_only
                class ConversationsResource(googleapiclient.discovery.Resource):
                    def batchDelete(
                        self,
                        *,
                        parent: str,
                        body: BatchDeleteConversationsRequest = ...,
                        **kwargs: typing.Any,
                    ) -> OperationHttpRequest: ...
                    def delete(
                        self,
                        *,
                        name: str,
                        source: typing_extensions.Literal[
                            "SOURCE_UNSPECIFIED", "LIVE", "SIMULATOR", "EVAL"
                        ] = ...,
                        **kwargs: typing.Any,
                    ) -> EmptyHttpRequest: ...
                    def generateEvaluation(
                        self,
                        *,
                        conversation: str,
                        body: GenerateEvaluationRequest = ...,
                        **kwargs: typing.Any,
                    ) -> OperationHttpRequest: ...
                    def get(
                        self,
                        *,
                        name: str,
                        source: typing_extensions.Literal[
                            "SOURCE_UNSPECIFIED", "LIVE", "SIMULATOR", "EVAL"
                        ] = ...,
                        **kwargs: typing.Any,
                    ) -> ConversationHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        source: typing_extensions.Literal[
                            "SOURCE_UNSPECIFIED", "LIVE", "SIMULATOR", "EVAL"
                        ] = ...,
                        **kwargs: typing.Any,
                    ) -> ListConversationsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: ListConversationsResponseHttpRequest,
                        previous_response: ListConversationsResponse,
                    ) -> ListConversationsResponseHttpRequest | None: ...

                @typing.type_check_only
                class DeploymentsResource(googleapiclient.discovery.Resource):
                    def create(
                        self,
                        *,
                        parent: str,
                        body: Deployment = ...,
                        deploymentId: str = ...,
                        **kwargs: typing.Any,
                    ) -> DeploymentHttpRequest: ...
                    def delete(
                        self, *, name: str, etag: str = ..., **kwargs: typing.Any
                    ) -> EmptyHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> DeploymentHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        orderBy: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
                    ) -> ListDeploymentsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: ListDeploymentsResponseHttpRequest,
                        previous_response: ListDeploymentsResponse,
                    ) -> ListDeploymentsResponseHttpRequest | None: ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: Deployment = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any,
                    ) -> DeploymentHttpRequest: ...

                @typing.type_check_only
                class EvaluationDatasetsResource(googleapiclient.discovery.Resource):
                    def create(
                        self,
                        *,
                        parent: str,
                        body: EvaluationDataset = ...,
                        evaluationDatasetId: str = ...,
                        **kwargs: typing.Any,
                    ) -> EvaluationDatasetHttpRequest: ...
                    def delete(
                        self, *, name: str, etag: str = ..., **kwargs: typing.Any
                    ) -> EmptyHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> EvaluationDatasetHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str = ...,
                        orderBy: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
                    ) -> ListEvaluationDatasetsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: ListEvaluationDatasetsResponseHttpRequest,
                        previous_response: ListEvaluationDatasetsResponse,
                    ) -> ListEvaluationDatasetsResponseHttpRequest | None: ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: EvaluationDataset = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any,
                    ) -> EvaluationDatasetHttpRequest: ...

                @typing.type_check_only
                class EvaluationExpectationsResource(
                    googleapiclient.discovery.Resource
                ):
                    def create(
                        self,
                        *,
                        parent: str,
                        body: EvaluationExpectation = ...,
                        evaluationExpectationId: str = ...,
                        **kwargs: typing.Any,
                    ) -> EvaluationExpectationHttpRequest: ...
                    def delete(
                        self, *, name: str, etag: str = ..., **kwargs: typing.Any
                    ) -> EmptyHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> EvaluationExpectationHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str = ...,
                        orderBy: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
                    ) -> ListEvaluationExpectationsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: ListEvaluationExpectationsResponseHttpRequest,
                        previous_response: ListEvaluationExpectationsResponse,
                    ) -> ListEvaluationExpectationsResponseHttpRequest | None: ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: EvaluationExpectation = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any,
                    ) -> EvaluationExpectationHttpRequest: ...

                @typing.type_check_only
                class EvaluationRunsResource(googleapiclient.discovery.Resource):
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> OperationHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> EvaluationRunHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str = ...,
                        orderBy: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
                    ) -> ListEvaluationRunsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: ListEvaluationRunsResponseHttpRequest,
                        previous_response: ListEvaluationRunsResponse,
                    ) -> ListEvaluationRunsResponseHttpRequest | None: ...

                @typing.type_check_only
                class EvaluationsResource(googleapiclient.discovery.Resource):
                    @typing.type_check_only
                    class ResultsResource(googleapiclient.discovery.Resource):
                        def delete(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> EmptyHttpRequest: ...
                        def get(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> EvaluationResultHttpRequest: ...
                        def list(
                            self,
                            *,
                            parent: str,
                            filter: str = ...,
                            orderBy: str = ...,
                            pageSize: int = ...,
                            pageToken: str = ...,
                            **kwargs: typing.Any,
                        ) -> ListEvaluationResultsResponseHttpRequest: ...
                        def list_next(
                            self,
                            previous_request: ListEvaluationResultsResponseHttpRequest,
                            previous_response: ListEvaluationResultsResponse,
                        ) -> ListEvaluationResultsResponseHttpRequest | None: ...

                    def create(
                        self,
                        *,
                        parent: str,
                        body: Evaluation = ...,
                        evaluationId: str = ...,
                        **kwargs: typing.Any,
                    ) -> EvaluationHttpRequest: ...
                    def delete(
                        self,
                        *,
                        name: str,
                        etag: str = ...,
                        force: bool = ...,
                        **kwargs: typing.Any,
                    ) -> EmptyHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> EvaluationHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str = ...,
                        lastTenResults: bool = ...,
                        orderBy: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
                    ) -> ListEvaluationsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: ListEvaluationsResponseHttpRequest,
                        previous_response: ListEvaluationsResponse,
                    ) -> ListEvaluationsResponseHttpRequest | None: ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: Evaluation = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any,
                    ) -> EvaluationHttpRequest: ...
                    def results(self) -> ResultsResource: ...

                @typing.type_check_only
                class ExamplesResource(googleapiclient.discovery.Resource):
                    def create(
                        self,
                        *,
                        parent: str,
                        body: Example = ...,
                        exampleId: str = ...,
                        **kwargs: typing.Any,
                    ) -> ExampleHttpRequest: ...
                    def delete(
                        self, *, name: str, etag: str = ..., **kwargs: typing.Any
                    ) -> EmptyHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> ExampleHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str = ...,
                        orderBy: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
                    ) -> ListExamplesResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: ListExamplesResponseHttpRequest,
                        previous_response: ListExamplesResponse,
                    ) -> ListExamplesResponseHttpRequest | None: ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: Example = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any,
                    ) -> ExampleHttpRequest: ...

                @typing.type_check_only
                class GuardrailsResource(googleapiclient.discovery.Resource):
                    def create(
                        self,
                        *,
                        parent: str,
                        body: Guardrail = ...,
                        guardrailId: str = ...,
                        **kwargs: typing.Any,
                    ) -> GuardrailHttpRequest: ...
                    def delete(
                        self,
                        *,
                        name: str,
                        etag: str = ...,
                        force: bool = ...,
                        **kwargs: typing.Any,
                    ) -> EmptyHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GuardrailHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str = ...,
                        orderBy: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
                    ) -> ListGuardrailsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: ListGuardrailsResponseHttpRequest,
                        previous_response: ListGuardrailsResponse,
                    ) -> ListGuardrailsResponseHttpRequest | None: ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: Guardrail = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any,
                    ) -> GuardrailHttpRequest: ...

                @typing.type_check_only
                class ScheduledEvaluationRunsResource(
                    googleapiclient.discovery.Resource
                ):
                    def create(
                        self,
                        *,
                        parent: str,
                        body: ScheduledEvaluationRun = ...,
                        scheduledEvaluationRunId: str = ...,
                        **kwargs: typing.Any,
                    ) -> ScheduledEvaluationRunHttpRequest: ...
                    def delete(
                        self, *, name: str, etag: str = ..., **kwargs: typing.Any
                    ) -> EmptyHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> ScheduledEvaluationRunHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str = ...,
                        orderBy: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
                    ) -> ListScheduledEvaluationRunsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: ListScheduledEvaluationRunsResponseHttpRequest,
                        previous_response: ListScheduledEvaluationRunsResponse,
                    ) -> ListScheduledEvaluationRunsResponseHttpRequest | None: ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: ScheduledEvaluationRun = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any,
                    ) -> ScheduledEvaluationRunHttpRequest: ...

                @typing.type_check_only
                class SessionsResource(googleapiclient.discovery.Resource):
                    def generateChatToken(
                        self,
                        *,
                        name: str,
                        body: GenerateChatTokenRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GenerateChatTokenResponseHttpRequest: ...
                    def runSession(
                        self,
                        *,
                        session: str,
                        body: RunSessionRequest = ...,
                        **kwargs: typing.Any,
                    ) -> RunSessionResponseHttpRequest: ...

                @typing.type_check_only
                class ToolsResource(googleapiclient.discovery.Resource):
                    def create(
                        self,
                        *,
                        parent: str,
                        body: Tool = ...,
                        toolId: str = ...,
                        **kwargs: typing.Any,
                    ) -> ToolHttpRequest: ...
                    def delete(
                        self,
                        *,
                        name: str,
                        etag: str = ...,
                        force: bool = ...,
                        **kwargs: typing.Any,
                    ) -> EmptyHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> ToolHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str = ...,
                        orderBy: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
                    ) -> ListToolsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: ListToolsResponseHttpRequest,
                        previous_response: ListToolsResponse,
                    ) -> ListToolsResponseHttpRequest | None: ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: Tool = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any,
                    ) -> ToolHttpRequest: ...

                @typing.type_check_only
                class ToolsetsResource(googleapiclient.discovery.Resource):
                    def create(
                        self,
                        *,
                        parent: str,
                        body: Toolset = ...,
                        toolsetId: str = ...,
                        **kwargs: typing.Any,
                    ) -> ToolsetHttpRequest: ...
                    def delete(
                        self,
                        *,
                        name: str,
                        etag: str = ...,
                        force: bool = ...,
                        **kwargs: typing.Any,
                    ) -> EmptyHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> ToolsetHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str = ...,
                        orderBy: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
                    ) -> ListToolsetsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: ListToolsetsResponseHttpRequest,
                        previous_response: ListToolsetsResponse,
                    ) -> ListToolsetsResponseHttpRequest | None: ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: Toolset = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any,
                    ) -> ToolsetHttpRequest: ...
                    def retrieveTools(
                        self,
                        *,
                        toolset: str,
                        body: RetrieveToolsRequest = ...,
                        **kwargs: typing.Any,
                    ) -> RetrieveToolsResponseHttpRequest: ...

                @typing.type_check_only
                class VersionsResource(googleapiclient.discovery.Resource):
                    def create(
                        self,
                        *,
                        parent: str,
                        body: AppVersion = ...,
                        appVersionId: str = ...,
                        **kwargs: typing.Any,
                    ) -> AppVersionHttpRequest: ...
                    def delete(
                        self, *, name: str, etag: str = ..., **kwargs: typing.Any
                    ) -> EmptyHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> AppVersionHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str = ...,
                        orderBy: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
                    ) -> ListAppVersionsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: ListAppVersionsResponseHttpRequest,
                        previous_response: ListAppVersionsResponse,
                    ) -> ListAppVersionsResponseHttpRequest | None: ...
                    def restore(
                        self,
                        *,
                        name: str,
                        body: RestoreAppVersionRequest = ...,
                        **kwargs: typing.Any,
                    ) -> OperationHttpRequest: ...

                def create(
                    self,
                    *,
                    parent: str,
                    body: App = ...,
                    appId: str = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def delete(
                    self, *, name: str, etag: str = ..., **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def executeTool(
                    self,
                    *,
                    parent: str,
                    body: ExecuteToolRequest = ...,
                    **kwargs: typing.Any,
                ) -> ExecuteToolResponseHttpRequest: ...
                def exportApp(
                    self,
                    *,
                    name: str,
                    body: ExportAppRequest = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def get(self, *, name: str, **kwargs: typing.Any) -> AppHttpRequest: ...
                def importApp(
                    self,
                    *,
                    parent: str,
                    body: ImportAppRequest = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def importEvaluations(
                    self,
                    *,
                    parent: str,
                    body: ImportEvaluationsRequest = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> ListAppsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListAppsResponseHttpRequest,
                    previous_response: ListAppsResponse,
                ) -> ListAppsResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: App = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> AppHttpRequest: ...
                def retrieveToolSchema(
                    self,
                    *,
                    parent: str,
                    body: RetrieveToolSchemaRequest = ...,
                    **kwargs: typing.Any,
                ) -> RetrieveToolSchemaResponseHttpRequest: ...
                def runEvaluation(
                    self,
                    *,
                    app: str,
                    body: RunEvaluationRequest = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def testPersonaVoice(
                    self,
                    *,
                    app: str,
                    body: TestPersonaVoiceRequest = ...,
                    **kwargs: typing.Any,
                ) -> TestPersonaVoiceResponseHttpRequest: ...
                def agents(self) -> AgentsResource: ...
                def changelogs(self) -> ChangelogsResource: ...
                def conversations(self) -> ConversationsResource: ...
                def deployments(self) -> DeploymentsResource: ...
                def evaluationDatasets(self) -> EvaluationDatasetsResource: ...
                def evaluationExpectations(self) -> EvaluationExpectationsResource: ...
                def evaluationRuns(self) -> EvaluationRunsResource: ...
                def evaluations(self) -> EvaluationsResource: ...
                def examples(self) -> ExamplesResource: ...
                def guardrails(self) -> GuardrailsResource: ...
                def scheduledEvaluationRuns(
                    self,
                ) -> ScheduledEvaluationRunsResource: ...
                def sessions(self) -> SessionsResource: ...
                def tools(self) -> ToolsResource: ...
                def toolsets(self) -> ToolsetsResource: ...
                def versions(self) -> VersionsResource: ...

            @typing.type_check_only
            class OperationsResource(googleapiclient.discovery.Resource):
                def cancel(
                    self,
                    *,
                    name: str,
                    body: CancelOperationRequest = ...,
                    **kwargs: typing.Any,
                ) -> EmptyHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def list(
                    self,
                    *,
                    name: str,
                    filter: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    returnPartialSuccess: bool = ...,
                    **kwargs: typing.Any,
                ) -> ListOperationsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListOperationsResponseHttpRequest,
                    previous_response: ListOperationsResponse,
                ) -> ListOperationsResponseHttpRequest | None: ...

            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> LocationHttpRequest: ...
            def list(
                self,
                *,
                name: str,
                extraLocationTypes: str | _list[str] = ...,
                filter: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any,
            ) -> ListLocationsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListLocationsResponseHttpRequest,
                previous_response: ListLocationsResponse,
            ) -> ListLocationsResponseHttpRequest | None: ...
            def apps(self) -> AppsResource: ...
            def operations(self) -> OperationsResource: ...

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
class AgentHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Agent: ...

@typing.type_check_only
class AppHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> App: ...

@typing.type_check_only
class AppVersionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> AppVersion: ...

@typing.type_check_only
class ChangelogHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Changelog: ...

@typing.type_check_only
class ConversationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Conversation: ...

@typing.type_check_only
class DeploymentHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Deployment: ...

@typing.type_check_only
class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Empty: ...

@typing.type_check_only
class EvaluationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Evaluation: ...

@typing.type_check_only
class EvaluationDatasetHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> EvaluationDataset: ...

@typing.type_check_only
class EvaluationExpectationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> EvaluationExpectation: ...

@typing.type_check_only
class EvaluationResultHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> EvaluationResult: ...

@typing.type_check_only
class EvaluationRunHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> EvaluationRun: ...

@typing.type_check_only
class ExampleHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Example: ...

@typing.type_check_only
class ExecuteToolResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ExecuteToolResponse: ...

@typing.type_check_only
class GenerateChatTokenResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GenerateChatTokenResponse: ...

@typing.type_check_only
class GuardrailHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Guardrail: ...

@typing.type_check_only
class ListAgentsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListAgentsResponse: ...

@typing.type_check_only
class ListAppVersionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListAppVersionsResponse: ...

@typing.type_check_only
class ListAppsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListAppsResponse: ...

@typing.type_check_only
class ListChangelogsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListChangelogsResponse: ...

@typing.type_check_only
class ListConversationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListConversationsResponse: ...

@typing.type_check_only
class ListDeploymentsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListDeploymentsResponse: ...

@typing.type_check_only
class ListEvaluationDatasetsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListEvaluationDatasetsResponse: ...

@typing.type_check_only
class ListEvaluationExpectationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListEvaluationExpectationsResponse: ...

@typing.type_check_only
class ListEvaluationResultsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListEvaluationResultsResponse: ...

@typing.type_check_only
class ListEvaluationRunsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListEvaluationRunsResponse: ...

@typing.type_check_only
class ListEvaluationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListEvaluationsResponse: ...

@typing.type_check_only
class ListExamplesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListExamplesResponse: ...

@typing.type_check_only
class ListGuardrailsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListGuardrailsResponse: ...

@typing.type_check_only
class ListLocationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListLocationsResponse: ...

@typing.type_check_only
class ListOperationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListOperationsResponse: ...

@typing.type_check_only
class ListScheduledEvaluationRunsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListScheduledEvaluationRunsResponse: ...

@typing.type_check_only
class ListToolsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListToolsResponse: ...

@typing.type_check_only
class ListToolsetsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListToolsetsResponse: ...

@typing.type_check_only
class LocationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Location: ...

@typing.type_check_only
class OperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Operation: ...

@typing.type_check_only
class RetrieveToolSchemaResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> RetrieveToolSchemaResponse: ...

@typing.type_check_only
class RetrieveToolsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> RetrieveToolsResponse: ...

@typing.type_check_only
class RunSessionResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> RunSessionResponse: ...

@typing.type_check_only
class ScheduledEvaluationRunHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ScheduledEvaluationRun: ...

@typing.type_check_only
class TestPersonaVoiceResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> TestPersonaVoiceResponse: ...

@typing.type_check_only
class ToolHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Tool: ...

@typing.type_check_only
class ToolsetHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Toolset: ...
