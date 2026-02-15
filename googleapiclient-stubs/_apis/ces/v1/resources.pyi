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
                def agents(self) -> AgentsResource: ...
                def changelogs(self) -> ChangelogsResource: ...
                def conversations(self) -> ConversationsResource: ...
                def deployments(self) -> DeploymentsResource: ...
                def examples(self) -> ExamplesResource: ...
                def guardrails(self) -> GuardrailsResource: ...
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
