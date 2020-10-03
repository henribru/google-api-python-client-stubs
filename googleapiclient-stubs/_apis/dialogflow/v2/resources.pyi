import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class DialogflowResource(googleapiclient.discovery.Resource):
    class ProjectsResource(googleapiclient.discovery.Resource):
        class LocationsResource(googleapiclient.discovery.Resource):
            class OperationsResource(googleapiclient.discovery.Resource):
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def list(
                    self,
                    *,
                    name: str,
                    pageSize: int = ...,
                    filter: str = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleLongrunningListOperationsResponseHttpRequest: ...
                def cancel(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleProtobufEmptyHttpRequest: ...
            def operations(self) -> OperationsResource: ...
        class AgentResource(googleapiclient.discovery.Resource):
            class SessionsResource(googleapiclient.discovery.Resource):
                class ContextsResource(googleapiclient.discovery.Resource):
                    def create(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudDialogflowV2Context = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudDialogflowV2ContextHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudDialogflowV2ListContextsResponseHttpRequest: ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudDialogflowV2Context = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudDialogflowV2ContextHttpRequest: ...
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleProtobufEmptyHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleCloudDialogflowV2ContextHttpRequest: ...
                class EntityTypesResource(googleapiclient.discovery.Resource):
                    def create(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudDialogflowV2SessionEntityType = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudDialogflowV2SessionEntityTypeHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleCloudDialogflowV2SessionEntityTypeHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        pageToken: str = ...,
                        pageSize: int = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudDialogflowV2ListSessionEntityTypesResponseHttpRequest: ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudDialogflowV2SessionEntityType = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudDialogflowV2SessionEntityTypeHttpRequest: ...
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleProtobufEmptyHttpRequest: ...
                def detectIntent(
                    self,
                    *,
                    session: str,
                    body: GoogleCloudDialogflowV2DetectIntentRequest = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudDialogflowV2DetectIntentResponseHttpRequest: ...
                def deleteContexts(
                    self, *, parent: str, **kwargs: typing.Any
                ) -> GoogleProtobufEmptyHttpRequest: ...
                def contexts(self) -> ContextsResource: ...
                def entityTypes(self) -> EntityTypesResource: ...
            class EnvironmentsResource(googleapiclient.discovery.Resource):
                class UsersResource(googleapiclient.discovery.Resource):
                    class SessionsResource(googleapiclient.discovery.Resource):
                        class EntityTypesResource(googleapiclient.discovery.Resource):
                            def patch(
                                self,
                                *,
                                name: str,
                                body: GoogleCloudDialogflowV2SessionEntityType = ...,
                                updateMask: str = ...,
                                **kwargs: typing.Any
                            ) -> GoogleCloudDialogflowV2SessionEntityTypeHttpRequest: ...
                            def create(
                                self,
                                *,
                                parent: str,
                                body: GoogleCloudDialogflowV2SessionEntityType = ...,
                                **kwargs: typing.Any
                            ) -> GoogleCloudDialogflowV2SessionEntityTypeHttpRequest: ...
                            def list(
                                self,
                                *,
                                parent: str,
                                pageToken: str = ...,
                                pageSize: int = ...,
                                **kwargs: typing.Any
                            ) -> GoogleCloudDialogflowV2ListSessionEntityTypesResponseHttpRequest: ...
                            def get(
                                self, *, name: str, **kwargs: typing.Any
                            ) -> GoogleCloudDialogflowV2SessionEntityTypeHttpRequest: ...
                            def delete(
                                self, *, name: str, **kwargs: typing.Any
                            ) -> GoogleProtobufEmptyHttpRequest: ...
                        class ContextsResource(googleapiclient.discovery.Resource):
                            def create(
                                self,
                                *,
                                parent: str,
                                body: GoogleCloudDialogflowV2Context = ...,
                                **kwargs: typing.Any
                            ) -> GoogleCloudDialogflowV2ContextHttpRequest: ...
                            def delete(
                                self, *, name: str, **kwargs: typing.Any
                            ) -> GoogleProtobufEmptyHttpRequest: ...
                            def get(
                                self, *, name: str, **kwargs: typing.Any
                            ) -> GoogleCloudDialogflowV2ContextHttpRequest: ...
                            def list(
                                self,
                                *,
                                parent: str,
                                pageSize: int = ...,
                                pageToken: str = ...,
                                **kwargs: typing.Any
                            ) -> GoogleCloudDialogflowV2ListContextsResponseHttpRequest: ...
                            def patch(
                                self,
                                *,
                                name: str,
                                body: GoogleCloudDialogflowV2Context = ...,
                                updateMask: str = ...,
                                **kwargs: typing.Any
                            ) -> GoogleCloudDialogflowV2ContextHttpRequest: ...
                        def deleteContexts(
                            self, *, parent: str, **kwargs: typing.Any
                        ) -> GoogleProtobufEmptyHttpRequest: ...
                        def detectIntent(
                            self,
                            *,
                            session: str,
                            body: GoogleCloudDialogflowV2DetectIntentRequest = ...,
                            **kwargs: typing.Any
                        ) -> GoogleCloudDialogflowV2DetectIntentResponseHttpRequest: ...
                        def entityTypes(self) -> EntityTypesResource: ...
                        def contexts(self) -> ContextsResource: ...
                    def sessions(self) -> SessionsResource: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudDialogflowV2ListEnvironmentsResponseHttpRequest: ...
                def users(self) -> UsersResource: ...
            class EntityTypesResource(googleapiclient.discovery.Resource):
                class EntitiesResource(googleapiclient.discovery.Resource):
                    def batchUpdate(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudDialogflowV2BatchUpdateEntitiesRequest = ...,
                        **kwargs: typing.Any
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def batchCreate(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudDialogflowV2BatchCreateEntitiesRequest = ...,
                        **kwargs: typing.Any
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def batchDelete(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudDialogflowV2BatchDeleteEntitiesRequest = ...,
                        **kwargs: typing.Any
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleProtobufEmptyHttpRequest: ...
                def batchUpdate(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudDialogflowV2BatchUpdateEntityTypesRequest = ...,
                    **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageToken: str = ...,
                    languageCode: str = ...,
                    pageSize: int = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudDialogflowV2ListEntityTypesResponseHttpRequest: ...
                def batchDelete(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudDialogflowV2BatchDeleteEntityTypesRequest = ...,
                    **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudDialogflowV2EntityType = ...,
                    languageCode: str = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudDialogflowV2EntityTypeHttpRequest: ...
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudDialogflowV2EntityType = ...,
                    languageCode: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudDialogflowV2EntityTypeHttpRequest: ...
                def get(
                    self, *, name: str, languageCode: str = ..., **kwargs: typing.Any
                ) -> GoogleCloudDialogflowV2EntityTypeHttpRequest: ...
                def entities(self) -> EntitiesResource: ...
            class IntentsResource(googleapiclient.discovery.Resource):
                def batchDelete(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudDialogflowV2BatchDeleteIntentsRequest = ...,
                    **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    intentView: typing_extensions.Literal[
                        "INTENT_VIEW_UNSPECIFIED", "INTENT_VIEW_FULL"
                    ] = ...,
                    languageCode: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudDialogflowV2ListIntentsResponseHttpRequest: ...
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudDialogflowV2Intent = ...,
                    intentView: typing_extensions.Literal[
                        "INTENT_VIEW_UNSPECIFIED", "INTENT_VIEW_FULL"
                    ] = ...,
                    languageCode: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudDialogflowV2IntentHttpRequest: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudDialogflowV2Intent = ...,
                    intentView: typing_extensions.Literal[
                        "INTENT_VIEW_UNSPECIFIED", "INTENT_VIEW_FULL"
                    ] = ...,
                    languageCode: str = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudDialogflowV2IntentHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleProtobufEmptyHttpRequest: ...
                def get(
                    self,
                    *,
                    name: str,
                    intentView: typing_extensions.Literal[
                        "INTENT_VIEW_UNSPECIFIED", "INTENT_VIEW_FULL"
                    ] = ...,
                    languageCode: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudDialogflowV2IntentHttpRequest: ...
                def batchUpdate(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudDialogflowV2BatchUpdateIntentsRequest = ...,
                    **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
            def getFulfillment(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleCloudDialogflowV2FulfillmentHttpRequest: ...
            def search(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudDialogflowV2SearchAgentsResponseHttpRequest: ...
            def restore(
                self,
                *,
                parent: str,
                body: GoogleCloudDialogflowV2RestoreAgentRequest = ...,
                **kwargs: typing.Any
            ) -> GoogleLongrunningOperationHttpRequest: ...
            def import_(
                self,
                *,
                parent: str,
                body: GoogleCloudDialogflowV2ImportAgentRequest = ...,
                **kwargs: typing.Any
            ) -> GoogleLongrunningOperationHttpRequest: ...
            def train(
                self,
                *,
                parent: str,
                body: GoogleCloudDialogflowV2TrainAgentRequest = ...,
                **kwargs: typing.Any
            ) -> GoogleLongrunningOperationHttpRequest: ...
            def updateFulfillment(
                self,
                *,
                name: str,
                body: GoogleCloudDialogflowV2Fulfillment = ...,
                updateMask: str = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudDialogflowV2FulfillmentHttpRequest: ...
            def export(
                self,
                *,
                parent: str,
                body: GoogleCloudDialogflowV2ExportAgentRequest = ...,
                **kwargs: typing.Any
            ) -> GoogleLongrunningOperationHttpRequest: ...
            def getValidationResult(
                self, *, parent: str, languageCode: str = ..., **kwargs: typing.Any
            ) -> GoogleCloudDialogflowV2ValidationResultHttpRequest: ...
            def sessions(self) -> SessionsResource: ...
            def environments(self) -> EnvironmentsResource: ...
            def entityTypes(self) -> EntityTypesResource: ...
            def intents(self) -> IntentsResource: ...
        class OperationsResource(googleapiclient.discovery.Resource):
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleLongrunningOperationHttpRequest: ...
            def cancel(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleProtobufEmptyHttpRequest: ...
            def list(
                self,
                *,
                name: str,
                filter: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> GoogleLongrunningListOperationsResponseHttpRequest: ...
        def deleteAgent(
            self, *, parent: str, **kwargs: typing.Any
        ) -> GoogleProtobufEmptyHttpRequest: ...
        def getAgent(
            self, *, parent: str, **kwargs: typing.Any
        ) -> GoogleCloudDialogflowV2AgentHttpRequest: ...
        def setAgent(
            self,
            *,
            parent: str,
            body: GoogleCloudDialogflowV2Agent = ...,
            updateMask: str = ...,
            **kwargs: typing.Any
        ) -> GoogleCloudDialogflowV2AgentHttpRequest: ...
        def locations(self) -> LocationsResource: ...
        def agent(self) -> AgentResource: ...
        def operations(self) -> OperationsResource: ...
    def projects(self) -> ProjectsResource: ...

class GoogleCloudDialogflowV2ListEnvironmentsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudDialogflowV2ListEnvironmentsResponse: ...

class GoogleCloudDialogflowV2AgentHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudDialogflowV2Agent: ...

class GoogleCloudDialogflowV2DetectIntentResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudDialogflowV2DetectIntentResponse: ...

class GoogleCloudDialogflowV2SearchAgentsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudDialogflowV2SearchAgentsResponse: ...

class GoogleProtobufEmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleProtobufEmpty: ...

class GoogleLongrunningListOperationsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleLongrunningListOperationsResponse: ...

class GoogleCloudDialogflowV2ValidationResultHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudDialogflowV2ValidationResult: ...

class GoogleCloudDialogflowV2ListIntentsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudDialogflowV2ListIntentsResponse: ...

class GoogleLongrunningOperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleLongrunningOperation: ...

class GoogleCloudDialogflowV2ContextHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudDialogflowV2Context: ...

class GoogleCloudDialogflowV2ListSessionEntityTypesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudDialogflowV2ListSessionEntityTypesResponse: ...

class GoogleCloudDialogflowV2EntityTypeHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudDialogflowV2EntityType: ...

class GoogleCloudDialogflowV2FulfillmentHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudDialogflowV2Fulfillment: ...

class GoogleCloudDialogflowV2ListEntityTypesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudDialogflowV2ListEntityTypesResponse: ...

class GoogleCloudDialogflowV2ListContextsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudDialogflowV2ListContextsResponse: ...

class GoogleCloudDialogflowV2IntentHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudDialogflowV2Intent: ...

class GoogleCloudDialogflowV2SessionEntityTypeHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudDialogflowV2SessionEntityType: ...
