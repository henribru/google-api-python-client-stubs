import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class DialogflowResource(googleapiclient.discovery.Resource):
    class ProjectsResource(googleapiclient.discovery.Resource):
        class OperationsResource(googleapiclient.discovery.Resource):
            def list(
                self,
                *,
                name: str,
                pageToken: str = ...,
                pageSize: int = ...,
                filter: str = ...,
                **kwargs: typing.Any
            ) -> GoogleLongrunningListOperationsResponseHttpRequest: ...
            def cancel(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleProtobufEmptyHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleLongrunningOperationHttpRequest: ...
        class LocationsResource(googleapiclient.discovery.Resource):
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
            class AgentsResource(googleapiclient.discovery.Resource):
                class EnvironmentsResource(googleapiclient.discovery.Resource):
                    class SessionsResource(googleapiclient.discovery.Resource):
                        class EntityTypesResource(googleapiclient.discovery.Resource):
                            def get(
                                self, *, name: str, **kwargs: typing.Any
                            ) -> GoogleCloudDialogflowCxV3beta1SessionEntityTypeHttpRequest: ...
                            def patch(
                                self,
                                *,
                                name: str,
                                body: GoogleCloudDialogflowCxV3beta1SessionEntityType = ...,
                                updateMask: str = ...,
                                **kwargs: typing.Any
                            ) -> GoogleCloudDialogflowCxV3beta1SessionEntityTypeHttpRequest: ...
                            def list(
                                self,
                                *,
                                parent: str,
                                pageToken: str = ...,
                                pageSize: int = ...,
                                **kwargs: typing.Any
                            ) -> GoogleCloudDialogflowCxV3beta1ListSessionEntityTypesResponseHttpRequest: ...
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
                    def list(
                        self,
                        *,
                        parent: str,
                        pageToken: str = ...,
                        pageSize: int = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudDialogflowCxV3beta1ListEnvironmentsResponseHttpRequest: ...
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleProtobufEmptyHttpRequest: ...
                    def lookupEnvironmentHistory(
                        self,
                        *,
                        name: str,
                        pageToken: str = ...,
                        pageSize: int = ...,
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
                    def create(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudDialogflowCxV3beta1Environment = ...,
                        **kwargs: typing.Any
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleCloudDialogflowCxV3beta1EnvironmentHttpRequest: ...
                    def sessions(self) -> SessionsResource: ...
                class WebhooksResource(googleapiclient.discovery.Resource):
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleCloudDialogflowCxV3beta1WebhookHttpRequest: ...
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
                        body: GoogleCloudDialogflowCxV3beta1Webhook = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudDialogflowCxV3beta1WebhookHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudDialogflowCxV3beta1ListWebhooksResponseHttpRequest: ...
                    def delete(
                        self, *, name: str, force: bool = ..., **kwargs: typing.Any
                    ) -> GoogleProtobufEmptyHttpRequest: ...
                class FlowsResource(googleapiclient.discovery.Resource):
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
                        def list(
                            self,
                            *,
                            parent: str,
                            languageCode: str = ...,
                            pageToken: str = ...,
                            pageSize: int = ...,
                            **kwargs: typing.Any
                        ) -> GoogleCloudDialogflowCxV3beta1ListTransitionRouteGroupsResponseHttpRequest: ...
                        def get(
                            self,
                            *,
                            name: str,
                            languageCode: str = ...,
                            **kwargs: typing.Any
                        ) -> GoogleCloudDialogflowCxV3beta1TransitionRouteGroupHttpRequest: ...
                        def patch(
                            self,
                            *,
                            name: str,
                            body: GoogleCloudDialogflowCxV3beta1TransitionRouteGroup = ...,
                            languageCode: str = ...,
                            updateMask: str = ...,
                            **kwargs: typing.Any
                        ) -> GoogleCloudDialogflowCxV3beta1TransitionRouteGroupHttpRequest: ...
                    class PagesResource(googleapiclient.discovery.Resource):
                        def patch(
                            self,
                            *,
                            name: str,
                            body: GoogleCloudDialogflowCxV3beta1Page = ...,
                            updateMask: str = ...,
                            languageCode: str = ...,
                            **kwargs: typing.Any
                        ) -> GoogleCloudDialogflowCxV3beta1PageHttpRequest: ...
                        def create(
                            self,
                            *,
                            parent: str,
                            body: GoogleCloudDialogflowCxV3beta1Page = ...,
                            languageCode: str = ...,
                            **kwargs: typing.Any
                        ) -> GoogleCloudDialogflowCxV3beta1PageHttpRequest: ...
                        def get(
                            self,
                            *,
                            name: str,
                            languageCode: str = ...,
                            **kwargs: typing.Any
                        ) -> GoogleCloudDialogflowCxV3beta1PageHttpRequest: ...
                        def delete(
                            self, *, name: str, force: bool = ..., **kwargs: typing.Any
                        ) -> GoogleProtobufEmptyHttpRequest: ...
                        def list(
                            self,
                            *,
                            parent: str,
                            pageToken: str = ...,
                            languageCode: str = ...,
                            pageSize: int = ...,
                            **kwargs: typing.Any
                        ) -> GoogleCloudDialogflowCxV3beta1ListPagesResponseHttpRequest: ...
                    class VersionsResource(googleapiclient.discovery.Resource):
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
                            body: GoogleCloudDialogflowCxV3beta1Version = ...,
                            **kwargs: typing.Any
                        ) -> GoogleLongrunningOperationHttpRequest: ...
                        def delete(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> GoogleProtobufEmptyHttpRequest: ...
                        def load(
                            self,
                            *,
                            name: str,
                            body: GoogleCloudDialogflowCxV3beta1LoadVersionRequest = ...,
                            **kwargs: typing.Any
                        ) -> GoogleLongrunningOperationHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        languageCode: str = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudDialogflowCxV3beta1ListFlowsResponseHttpRequest: ...
                    def create(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudDialogflowCxV3beta1Flow = ...,
                        languageCode: str = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudDialogflowCxV3beta1FlowHttpRequest: ...
                    def train(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudDialogflowCxV3beta1TrainFlowRequest = ...,
                        **kwargs: typing.Any
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def get(
                        self,
                        *,
                        name: str,
                        languageCode: str = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudDialogflowCxV3beta1FlowHttpRequest: ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudDialogflowCxV3beta1Flow = ...,
                        languageCode: str = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudDialogflowCxV3beta1FlowHttpRequest: ...
                    def delete(
                        self, *, name: str, force: bool = ..., **kwargs: typing.Any
                    ) -> GoogleProtobufEmptyHttpRequest: ...
                    def transitionRouteGroups(
                        self,
                    ) -> TransitionRouteGroupsResource: ...
                    def pages(self) -> PagesResource: ...
                    def versions(self) -> VersionsResource: ...
                class EntityTypesResource(googleapiclient.discovery.Resource):
                    def patch(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudDialogflowCxV3beta1EntityType = ...,
                        languageCode: str = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudDialogflowCxV3beta1EntityTypeHttpRequest: ...
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
                    def delete(
                        self, *, name: str, force: bool = ..., **kwargs: typing.Any
                    ) -> GoogleProtobufEmptyHttpRequest: ...
                    def create(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudDialogflowCxV3beta1EntityType = ...,
                        languageCode: str = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudDialogflowCxV3beta1EntityTypeHttpRequest: ...
                class IntentsResource(googleapiclient.discovery.Resource):
                    def patch(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudDialogflowCxV3beta1Intent = ...,
                        updateMask: str = ...,
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
                        pageSize: int = ...,
                        languageCode: str = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudDialogflowCxV3beta1ListIntentsResponseHttpRequest: ...
                    def create(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudDialogflowCxV3beta1Intent = ...,
                        languageCode: str = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudDialogflowCxV3beta1IntentHttpRequest: ...
                class SessionsResource(googleapiclient.discovery.Resource):
                    class EntityTypesResource(googleapiclient.discovery.Resource):
                        def patch(
                            self,
                            *,
                            name: str,
                            body: GoogleCloudDialogflowCxV3beta1SessionEntityType = ...,
                            updateMask: str = ...,
                            **kwargs: typing.Any
                        ) -> GoogleCloudDialogflowCxV3beta1SessionEntityTypeHttpRequest: ...
                        def get(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> GoogleCloudDialogflowCxV3beta1SessionEntityTypeHttpRequest: ...
                        def list(
                            self,
                            *,
                            parent: str,
                            pageToken: str = ...,
                            pageSize: int = ...,
                            **kwargs: typing.Any
                        ) -> GoogleCloudDialogflowCxV3beta1ListSessionEntityTypesResponseHttpRequest: ...
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
                    def detectIntent(
                        self,
                        *,
                        session: str,
                        body: GoogleCloudDialogflowCxV3beta1DetectIntentRequest = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudDialogflowCxV3beta1DetectIntentResponseHttpRequest: ...
                    def entityTypes(self) -> EntityTypesResource: ...
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudDialogflowCxV3beta1Agent = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudDialogflowCxV3beta1AgentHttpRequest: ...
                def export(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudDialogflowCxV3beta1ExportAgentRequest = ...,
                    **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def restore(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudDialogflowCxV3beta1RestoreAgentRequest = ...,
                    **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudDialogflowCxV3beta1AgentHttpRequest: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudDialogflowCxV3beta1Agent = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudDialogflowCxV3beta1AgentHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleProtobufEmptyHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageToken: str = ...,
                    pageSize: int = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudDialogflowCxV3beta1ListAgentsResponseHttpRequest: ...
                def environments(self) -> EnvironmentsResource: ...
                def webhooks(self) -> WebhooksResource: ...
                def flows(self) -> FlowsResource: ...
                def entityTypes(self) -> EntityTypesResource: ...
                def intents(self) -> IntentsResource: ...
                def sessions(self) -> SessionsResource: ...
            def operations(self) -> OperationsResource: ...
            def agents(self) -> AgentsResource: ...
        def operations(self) -> OperationsResource: ...
        def locations(self) -> LocationsResource: ...
    def projects(self) -> ProjectsResource: ...

class GoogleCloudDialogflowCxV3beta1VersionHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudDialogflowCxV3beta1Version: ...

class GoogleCloudDialogflowCxV3beta1ListTransitionRouteGroupsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudDialogflowCxV3beta1ListTransitionRouteGroupsResponse: ...

class GoogleCloudDialogflowCxV3beta1EntityTypeHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudDialogflowCxV3beta1EntityType: ...

class GoogleCloudDialogflowCxV3beta1MatchIntentResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudDialogflowCxV3beta1MatchIntentResponse: ...

class GoogleCloudDialogflowCxV3beta1ListIntentsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudDialogflowCxV3beta1ListIntentsResponse: ...

class GoogleCloudDialogflowCxV3beta1ListWebhooksResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudDialogflowCxV3beta1ListWebhooksResponse: ...

class GoogleProtobufEmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleProtobufEmpty: ...

class GoogleCloudDialogflowCxV3beta1DetectIntentResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudDialogflowCxV3beta1DetectIntentResponse: ...

class GoogleCloudDialogflowCxV3beta1WebhookHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudDialogflowCxV3beta1Webhook: ...

class GoogleLongrunningListOperationsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleLongrunningListOperationsResponse: ...

class GoogleCloudDialogflowCxV3beta1TransitionRouteGroupHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudDialogflowCxV3beta1TransitionRouteGroup: ...

class GoogleCloudDialogflowCxV3beta1ListPagesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudDialogflowCxV3beta1ListPagesResponse: ...

class GoogleLongrunningOperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleLongrunningOperation: ...

class GoogleCloudDialogflowCxV3beta1IntentHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudDialogflowCxV3beta1Intent: ...

class GoogleCloudDialogflowCxV3beta1ListSessionEntityTypesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudDialogflowCxV3beta1ListSessionEntityTypesResponse: ...

class GoogleCloudDialogflowCxV3beta1AgentHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudDialogflowCxV3beta1Agent: ...

class GoogleCloudDialogflowCxV3beta1PageHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudDialogflowCxV3beta1Page: ...

class GoogleCloudDialogflowCxV3beta1ListEnvironmentsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudDialogflowCxV3beta1ListEnvironmentsResponse: ...

class GoogleCloudDialogflowCxV3beta1FlowHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudDialogflowCxV3beta1Flow: ...

class GoogleCloudDialogflowCxV3beta1SessionEntityTypeHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudDialogflowCxV3beta1SessionEntityType: ...

class GoogleCloudDialogflowCxV3beta1LookupEnvironmentHistoryResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudDialogflowCxV3beta1LookupEnvironmentHistoryResponse: ...

class GoogleCloudDialogflowCxV3beta1EnvironmentHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudDialogflowCxV3beta1Environment: ...

class GoogleCloudDialogflowCxV3beta1ListAgentsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudDialogflowCxV3beta1ListAgentsResponse: ...

class GoogleCloudDialogflowCxV3beta1ListFlowsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudDialogflowCxV3beta1ListFlowsResponse: ...

class GoogleCloudDialogflowCxV3beta1ListVersionsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudDialogflowCxV3beta1ListVersionsResponse: ...

class GoogleCloudDialogflowCxV3beta1ListEntityTypesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudDialogflowCxV3beta1ListEntityTypesResponse: ...

class GoogleCloudDialogflowCxV3beta1FulfillIntentResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudDialogflowCxV3beta1FulfillIntentResponse: ...
