import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *
@typing.type_check_only
class DialogflowResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class ProjectsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class LocationsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class AgentsResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class EntityTypesResource(googleapiclient.discovery.Resource):
                    def create(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudDialogflowCxV3beta1EntityType = ...,
                        languageCode: str = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudDialogflowCxV3beta1EntityTypeHttpRequest: ...
                    def delete(
                        self, *, name: str, force: bool = ..., **kwargs: typing.Any
                    ) -> GoogleProtobufEmptyHttpRequest: ...
                    def get(
                        self,
                        *,
                        name: str,
                        languageCode: str = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudDialogflowCxV3beta1EntityTypeHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        languageCode: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudDialogflowCxV3beta1ListEntityTypesResponseHttpRequest: ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudDialogflowCxV3beta1EntityType = ...,
                        languageCode: str = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudDialogflowCxV3beta1EntityTypeHttpRequest: ...
                @typing.type_check_only
                class EnvironmentsResource(googleapiclient.discovery.Resource):
                    @typing.type_check_only
                    class SessionsResource(googleapiclient.discovery.Resource):
                        @typing.type_check_only
                        class EntityTypesResource(googleapiclient.discovery.Resource):
                            def create(
                                self,
                                *,
                                parent: str,
                                body: GoogleCloudDialogflowCxV3beta1SessionEntityType = ...,
                                **kwargs: typing.Any
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
                                **kwargs: typing.Any
                            ) -> GoogleCloudDialogflowCxV3beta1ListSessionEntityTypesResponseHttpRequest: ...
                            def patch(
                                self,
                                *,
                                name: str,
                                body: GoogleCloudDialogflowCxV3beta1SessionEntityType = ...,
                                updateMask: str = ...,
                                **kwargs: typing.Any
                            ) -> GoogleCloudDialogflowCxV3beta1SessionEntityTypeHttpRequest: ...
                        def detectIntent(
                            self,
                            *,
                            session: str,
                            body: GoogleCloudDialogflowCxV3beta1DetectIntentRequest = ...,
                            **kwargs: typing.Any
                        ) -> GoogleCloudDialogflowCxV3beta1DetectIntentResponseHttpRequest: ...
                        def fulfillIntent(
                            self,
                            *,
                            session: str,
                            body: GoogleCloudDialogflowCxV3beta1FulfillIntentRequest = ...,
                            **kwargs: typing.Any
                        ) -> GoogleCloudDialogflowCxV3beta1FulfillIntentResponseHttpRequest: ...
                        def matchIntent(
                            self,
                            *,
                            session: str,
                            body: GoogleCloudDialogflowCxV3beta1MatchIntentRequest = ...,
                            **kwargs: typing.Any
                        ) -> GoogleCloudDialogflowCxV3beta1MatchIntentResponseHttpRequest: ...
                        def entityTypes(self) -> EntityTypesResource: ...
                    def create(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudDialogflowCxV3beta1Environment = ...,
                        **kwargs: typing.Any
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleProtobufEmptyHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleCloudDialogflowCxV3beta1EnvironmentHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudDialogflowCxV3beta1ListEnvironmentsResponseHttpRequest: ...
                    def lookupEnvironmentHistory(
                        self,
                        *,
                        name: str,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudDialogflowCxV3beta1LookupEnvironmentHistoryResponseHttpRequest: ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudDialogflowCxV3beta1Environment = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any
                    ) -> GoogleLongrunningOperationHttpRequest: ...
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
                            **kwargs: typing.Any
                        ) -> GoogleCloudDialogflowCxV3beta1PageHttpRequest: ...
                        def delete(
                            self, *, name: str, force: bool = ..., **kwargs: typing.Any
                        ) -> GoogleProtobufEmptyHttpRequest: ...
                        def get(
                            self,
                            *,
                            name: str,
                            languageCode: str = ...,
                            **kwargs: typing.Any
                        ) -> GoogleCloudDialogflowCxV3beta1PageHttpRequest: ...
                        def list(
                            self,
                            *,
                            parent: str,
                            languageCode: str = ...,
                            pageSize: int = ...,
                            pageToken: str = ...,
                            **kwargs: typing.Any
                        ) -> GoogleCloudDialogflowCxV3beta1ListPagesResponseHttpRequest: ...
                        def patch(
                            self,
                            *,
                            name: str,
                            body: GoogleCloudDialogflowCxV3beta1Page = ...,
                            languageCode: str = ...,
                            updateMask: str = ...,
                            **kwargs: typing.Any
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
                            **kwargs: typing.Any
                        ) -> GoogleCloudDialogflowCxV3beta1TransitionRouteGroupHttpRequest: ...
                        def delete(
                            self, *, name: str, force: bool = ..., **kwargs: typing.Any
                        ) -> GoogleProtobufEmptyHttpRequest: ...
                        def get(
                            self,
                            *,
                            name: str,
                            languageCode: str = ...,
                            **kwargs: typing.Any
                        ) -> GoogleCloudDialogflowCxV3beta1TransitionRouteGroupHttpRequest: ...
                        def list(
                            self,
                            *,
                            parent: str,
                            languageCode: str = ...,
                            pageSize: int = ...,
                            pageToken: str = ...,
                            **kwargs: typing.Any
                        ) -> GoogleCloudDialogflowCxV3beta1ListTransitionRouteGroupsResponseHttpRequest: ...
                        def patch(
                            self,
                            *,
                            name: str,
                            body: GoogleCloudDialogflowCxV3beta1TransitionRouteGroup = ...,
                            languageCode: str = ...,
                            updateMask: str = ...,
                            **kwargs: typing.Any
                        ) -> GoogleCloudDialogflowCxV3beta1TransitionRouteGroupHttpRequest: ...
                    @typing.type_check_only
                    class VersionsResource(googleapiclient.discovery.Resource):
                        def create(
                            self,
                            *,
                            parent: str,
                            body: GoogleCloudDialogflowCxV3beta1Version = ...,
                            **kwargs: typing.Any
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
                            **kwargs: typing.Any
                        ) -> GoogleCloudDialogflowCxV3beta1ListVersionsResponseHttpRequest: ...
                        def load(
                            self,
                            *,
                            name: str,
                            body: GoogleCloudDialogflowCxV3beta1LoadVersionRequest = ...,
                            **kwargs: typing.Any
                        ) -> GoogleLongrunningOperationHttpRequest: ...
                        def patch(
                            self,
                            *,
                            name: str,
                            body: GoogleCloudDialogflowCxV3beta1Version = ...,
                            updateMask: str = ...,
                            **kwargs: typing.Any
                        ) -> GoogleCloudDialogflowCxV3beta1VersionHttpRequest: ...
                    def create(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudDialogflowCxV3beta1Flow = ...,
                        languageCode: str = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudDialogflowCxV3beta1FlowHttpRequest: ...
                    def delete(
                        self, *, name: str, force: bool = ..., **kwargs: typing.Any
                    ) -> GoogleProtobufEmptyHttpRequest: ...
                    def get(
                        self,
                        *,
                        name: str,
                        languageCode: str = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudDialogflowCxV3beta1FlowHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        languageCode: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudDialogflowCxV3beta1ListFlowsResponseHttpRequest: ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudDialogflowCxV3beta1Flow = ...,
                        languageCode: str = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudDialogflowCxV3beta1FlowHttpRequest: ...
                    def train(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudDialogflowCxV3beta1TrainFlowRequest = ...,
                        **kwargs: typing.Any
                    ) -> GoogleLongrunningOperationHttpRequest: ...
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
                        body: GoogleCloudDialogflowCxV3beta1Intent = ...,
                        languageCode: str = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudDialogflowCxV3beta1IntentHttpRequest: ...
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleProtobufEmptyHttpRequest: ...
                    def get(
                        self,
                        *,
                        name: str,
                        languageCode: str = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudDialogflowCxV3beta1IntentHttpRequest: ...
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
                    ) -> GoogleCloudDialogflowCxV3beta1ListIntentsResponseHttpRequest: ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudDialogflowCxV3beta1Intent = ...,
                        languageCode: str = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudDialogflowCxV3beta1IntentHttpRequest: ...
                @typing.type_check_only
                class SessionsResource(googleapiclient.discovery.Resource):
                    @typing.type_check_only
                    class EntityTypesResource(googleapiclient.discovery.Resource):
                        def create(
                            self,
                            *,
                            parent: str,
                            body: GoogleCloudDialogflowCxV3beta1SessionEntityType = ...,
                            **kwargs: typing.Any
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
                            **kwargs: typing.Any
                        ) -> GoogleCloudDialogflowCxV3beta1ListSessionEntityTypesResponseHttpRequest: ...
                        def patch(
                            self,
                            *,
                            name: str,
                            body: GoogleCloudDialogflowCxV3beta1SessionEntityType = ...,
                            updateMask: str = ...,
                            **kwargs: typing.Any
                        ) -> GoogleCloudDialogflowCxV3beta1SessionEntityTypeHttpRequest: ...
                    def detectIntent(
                        self,
                        *,
                        session: str,
                        body: GoogleCloudDialogflowCxV3beta1DetectIntentRequest = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudDialogflowCxV3beta1DetectIntentResponseHttpRequest: ...
                    def fulfillIntent(
                        self,
                        *,
                        session: str,
                        body: GoogleCloudDialogflowCxV3beta1FulfillIntentRequest = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudDialogflowCxV3beta1FulfillIntentResponseHttpRequest: ...
                    def matchIntent(
                        self,
                        *,
                        session: str,
                        body: GoogleCloudDialogflowCxV3beta1MatchIntentRequest = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudDialogflowCxV3beta1MatchIntentResponseHttpRequest: ...
                    def entityTypes(self) -> EntityTypesResource: ...
                @typing.type_check_only
                class WebhooksResource(googleapiclient.discovery.Resource):
                    def create(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudDialogflowCxV3beta1Webhook = ...,
                        **kwargs: typing.Any
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
                        **kwargs: typing.Any
                    ) -> GoogleCloudDialogflowCxV3beta1ListWebhooksResponseHttpRequest: ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudDialogflowCxV3beta1Webhook = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudDialogflowCxV3beta1WebhookHttpRequest: ...
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudDialogflowCxV3beta1Agent = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudDialogflowCxV3beta1AgentHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleProtobufEmptyHttpRequest: ...
                def export(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudDialogflowCxV3beta1ExportAgentRequest = ...,
                    **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudDialogflowCxV3beta1AgentHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudDialogflowCxV3beta1ListAgentsResponseHttpRequest: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudDialogflowCxV3beta1Agent = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudDialogflowCxV3beta1AgentHttpRequest: ...
                def restore(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudDialogflowCxV3beta1RestoreAgentRequest = ...,
                    **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def entityTypes(self) -> EntityTypesResource: ...
                def environments(self) -> EnvironmentsResource: ...
                def flows(self) -> FlowsResource: ...
                def intents(self) -> IntentsResource: ...
                def sessions(self) -> SessionsResource: ...
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
            def agents(self) -> AgentsResource: ...
            def operations(self) -> OperationsResource: ...
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
        def locations(self) -> LocationsResource: ...
        def operations(self) -> OperationsResource: ...
    def projects(self) -> ProjectsResource: ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1AgentHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudDialogflowCxV3beta1Agent: ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1DetectIntentResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudDialogflowCxV3beta1DetectIntentResponse: ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1EntityTypeHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudDialogflowCxV3beta1EntityType: ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1EnvironmentHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudDialogflowCxV3beta1Environment: ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1FlowHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudDialogflowCxV3beta1Flow: ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1FulfillIntentResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudDialogflowCxV3beta1FulfillIntentResponse: ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1IntentHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudDialogflowCxV3beta1Intent: ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ListAgentsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudDialogflowCxV3beta1ListAgentsResponse: ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ListEntityTypesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudDialogflowCxV3beta1ListEntityTypesResponse: ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ListEnvironmentsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudDialogflowCxV3beta1ListEnvironmentsResponse: ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ListFlowsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudDialogflowCxV3beta1ListFlowsResponse: ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ListIntentsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudDialogflowCxV3beta1ListIntentsResponse: ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ListPagesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudDialogflowCxV3beta1ListPagesResponse: ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ListSessionEntityTypesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudDialogflowCxV3beta1ListSessionEntityTypesResponse: ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ListTransitionRouteGroupsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudDialogflowCxV3beta1ListTransitionRouteGroupsResponse: ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ListVersionsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudDialogflowCxV3beta1ListVersionsResponse: ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1ListWebhooksResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudDialogflowCxV3beta1ListWebhooksResponse: ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1LookupEnvironmentHistoryResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudDialogflowCxV3beta1LookupEnvironmentHistoryResponse: ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1MatchIntentResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudDialogflowCxV3beta1MatchIntentResponse: ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1PageHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudDialogflowCxV3beta1Page: ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1SessionEntityTypeHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudDialogflowCxV3beta1SessionEntityType: ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1TransitionRouteGroupHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudDialogflowCxV3beta1TransitionRouteGroup: ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1VersionHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudDialogflowCxV3beta1Version: ...

@typing.type_check_only
class GoogleCloudDialogflowCxV3beta1WebhookHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudDialogflowCxV3beta1Webhook: ...

@typing.type_check_only
class GoogleLongrunningListOperationsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleLongrunningListOperationsResponse: ...

@typing.type_check_only
class GoogleLongrunningOperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleLongrunningOperation: ...

@typing.type_check_only
class GoogleProtobufEmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleProtobufEmpty: ...
