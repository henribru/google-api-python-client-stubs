import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class DialogflowResource(googleapiclient.discovery.Resource):
    class ProjectsResource(googleapiclient.discovery.Resource):
        class AgentResource(googleapiclient.discovery.Resource):
            class EntityTypesResource(googleapiclient.discovery.Resource):
                class EntitiesResource(googleapiclient.discovery.Resource):
                    def batchCreate(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudDialogflowV2beta1BatchCreateEntitiesRequest = ...,
                        **kwargs: typing.Any
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def batchUpdate(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudDialogflowV2beta1BatchUpdateEntitiesRequest = ...,
                        **kwargs: typing.Any
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def batchDelete(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudDialogflowV2beta1BatchDeleteEntitiesRequest = ...,
                        **kwargs: typing.Any
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudDialogflowV2beta1EntityType = ...,
                    languageCode: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudDialogflowV2beta1EntityTypeHttpRequest: ...
                def get(
                    self, *, name: str, languageCode: str = ..., **kwargs: typing.Any
                ) -> GoogleCloudDialogflowV2beta1EntityTypeHttpRequest: ...
                def batchUpdate(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudDialogflowV2beta1BatchUpdateEntityTypesRequest = ...,
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
                ) -> GoogleCloudDialogflowV2beta1ListEntityTypesResponseHttpRequest: ...
                def batchDelete(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudDialogflowV2beta1BatchDeleteEntityTypesRequest = ...,
                    **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudDialogflowV2beta1EntityType = ...,
                    updateMask: str = ...,
                    languageCode: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudDialogflowV2beta1EntityTypeHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleProtobufEmptyHttpRequest: ...
                def entities(self) -> EntitiesResource: ...
            class IntentsResource(googleapiclient.discovery.Resource):
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudDialogflowV2beta1Intent = ...,
                    updateMask: str = ...,
                    intentView: typing_extensions.Literal[
                        "INTENT_VIEW_UNSPECIFIED", "INTENT_VIEW_FULL"
                    ] = ...,
                    languageCode: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudDialogflowV2beta1IntentHttpRequest: ...
                def get(
                    self,
                    *,
                    name: str,
                    languageCode: str = ...,
                    intentView: typing_extensions.Literal[
                        "INTENT_VIEW_UNSPECIFIED", "INTENT_VIEW_FULL"
                    ] = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudDialogflowV2beta1IntentHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    languageCode: str = ...,
                    pageToken: str = ...,
                    intentView: typing_extensions.Literal[
                        "INTENT_VIEW_UNSPECIFIED", "INTENT_VIEW_FULL"
                    ] = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudDialogflowV2beta1ListIntentsResponseHttpRequest: ...
                def batchUpdate(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudDialogflowV2beta1BatchUpdateIntentsRequest = ...,
                    **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudDialogflowV2beta1Intent = ...,
                    intentView: typing_extensions.Literal[
                        "INTENT_VIEW_UNSPECIFIED", "INTENT_VIEW_FULL"
                    ] = ...,
                    languageCode: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudDialogflowV2beta1IntentHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleProtobufEmptyHttpRequest: ...
                def batchDelete(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudDialogflowV2beta1BatchDeleteIntentsRequest = ...,
                    **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
            class SessionsResource(googleapiclient.discovery.Resource):
                class EntityTypesResource(googleapiclient.discovery.Resource):
                    def create(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudDialogflowV2beta1SessionEntityType = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudDialogflowV2beta1SessionEntityTypeHttpRequest: ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudDialogflowV2beta1SessionEntityType = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudDialogflowV2beta1SessionEntityTypeHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudDialogflowV2beta1ListSessionEntityTypesResponseHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleCloudDialogflowV2beta1SessionEntityTypeHttpRequest: ...
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleProtobufEmptyHttpRequest: ...
                class ContextsResource(googleapiclient.discovery.Resource):
                    def create(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudDialogflowV2beta1Context = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudDialogflowV2beta1ContextHttpRequest: ...
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleProtobufEmptyHttpRequest: ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudDialogflowV2beta1Context = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudDialogflowV2beta1ContextHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleCloudDialogflowV2beta1ContextHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        pageToken: str = ...,
                        pageSize: int = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudDialogflowV2beta1ListContextsResponseHttpRequest: ...
                def detectIntent(
                    self,
                    *,
                    session: str,
                    body: GoogleCloudDialogflowV2beta1DetectIntentRequest = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudDialogflowV2beta1DetectIntentResponseHttpRequest: ...
                def deleteContexts(
                    self, *, parent: str, **kwargs: typing.Any
                ) -> GoogleProtobufEmptyHttpRequest: ...
                def entityTypes(self) -> EntityTypesResource: ...
                def contexts(self) -> ContextsResource: ...
            class KnowledgeBasesResource(googleapiclient.discovery.Resource):
                class DocumentsResource(googleapiclient.discovery.Resource):
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudDialogflowV2beta1ListDocumentsResponseHttpRequest: ...
                    def create(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudDialogflowV2beta1Document = ...,
                        **kwargs: typing.Any
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudDialogflowV2beta1Document = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleCloudDialogflowV2beta1DocumentHttpRequest: ...
                    def reload(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudDialogflowV2beta1ReloadDocumentRequest = ...,
                        **kwargs: typing.Any
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudDialogflowV2beta1KnowledgeBaseHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudDialogflowV2beta1ListKnowledgeBasesResponseHttpRequest: ...
                def delete(
                    self, *, name: str, force: bool = ..., **kwargs: typing.Any
                ) -> GoogleProtobufEmptyHttpRequest: ...
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudDialogflowV2beta1KnowledgeBase = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudDialogflowV2beta1KnowledgeBaseHttpRequest: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudDialogflowV2beta1KnowledgeBase = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudDialogflowV2beta1KnowledgeBaseHttpRequest: ...
                def documents(self) -> DocumentsResource: ...
            class EnvironmentsResource(googleapiclient.discovery.Resource):
                class UsersResource(googleapiclient.discovery.Resource):
                    class SessionsResource(googleapiclient.discovery.Resource):
                        class EntityTypesResource(googleapiclient.discovery.Resource):
                            def list(
                                self,
                                *,
                                parent: str,
                                pageToken: str = ...,
                                pageSize: int = ...,
                                **kwargs: typing.Any
                            ) -> GoogleCloudDialogflowV2beta1ListSessionEntityTypesResponseHttpRequest: ...
                            def get(
                                self, *, name: str, **kwargs: typing.Any
                            ) -> GoogleCloudDialogflowV2beta1SessionEntityTypeHttpRequest: ...
                            def create(
                                self,
                                *,
                                parent: str,
                                body: GoogleCloudDialogflowV2beta1SessionEntityType = ...,
                                **kwargs: typing.Any
                            ) -> GoogleCloudDialogflowV2beta1SessionEntityTypeHttpRequest: ...
                            def delete(
                                self, *, name: str, **kwargs: typing.Any
                            ) -> GoogleProtobufEmptyHttpRequest: ...
                            def patch(
                                self,
                                *,
                                name: str,
                                body: GoogleCloudDialogflowV2beta1SessionEntityType = ...,
                                updateMask: str = ...,
                                **kwargs: typing.Any
                            ) -> GoogleCloudDialogflowV2beta1SessionEntityTypeHttpRequest: ...
                        class ContextsResource(googleapiclient.discovery.Resource):
                            def list(
                                self,
                                *,
                                parent: str,
                                pageToken: str = ...,
                                pageSize: int = ...,
                                **kwargs: typing.Any
                            ) -> GoogleCloudDialogflowV2beta1ListContextsResponseHttpRequest: ...
                            def create(
                                self,
                                *,
                                parent: str,
                                body: GoogleCloudDialogflowV2beta1Context = ...,
                                **kwargs: typing.Any
                            ) -> GoogleCloudDialogflowV2beta1ContextHttpRequest: ...
                            def delete(
                                self, *, name: str, **kwargs: typing.Any
                            ) -> GoogleProtobufEmptyHttpRequest: ...
                            def get(
                                self, *, name: str, **kwargs: typing.Any
                            ) -> GoogleCloudDialogflowV2beta1ContextHttpRequest: ...
                            def patch(
                                self,
                                *,
                                name: str,
                                body: GoogleCloudDialogflowV2beta1Context = ...,
                                updateMask: str = ...,
                                **kwargs: typing.Any
                            ) -> GoogleCloudDialogflowV2beta1ContextHttpRequest: ...
                        def deleteContexts(
                            self, *, parent: str, **kwargs: typing.Any
                        ) -> GoogleProtobufEmptyHttpRequest: ...
                        def detectIntent(
                            self,
                            *,
                            session: str,
                            body: GoogleCloudDialogflowV2beta1DetectIntentRequest = ...,
                            **kwargs: typing.Any
                        ) -> GoogleCloudDialogflowV2beta1DetectIntentResponseHttpRequest: ...
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
                ) -> GoogleCloudDialogflowV2beta1ListEnvironmentsResponseHttpRequest: ...
                def users(self) -> UsersResource: ...
            def getFulfillment(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleCloudDialogflowV2beta1FulfillmentHttpRequest: ...
            def restore(
                self,
                *,
                parent: str,
                body: GoogleCloudDialogflowV2beta1RestoreAgentRequest = ...,
                **kwargs: typing.Any
            ) -> GoogleLongrunningOperationHttpRequest: ...
            def getValidationResult(
                self, *, parent: str, languageCode: str = ..., **kwargs: typing.Any
            ) -> GoogleCloudDialogflowV2beta1ValidationResultHttpRequest: ...
            def import_(
                self,
                *,
                parent: str,
                body: GoogleCloudDialogflowV2beta1ImportAgentRequest = ...,
                **kwargs: typing.Any
            ) -> GoogleLongrunningOperationHttpRequest: ...
            def export(
                self,
                *,
                parent: str,
                body: GoogleCloudDialogflowV2beta1ExportAgentRequest = ...,
                **kwargs: typing.Any
            ) -> GoogleLongrunningOperationHttpRequest: ...
            def search(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudDialogflowV2beta1SearchAgentsResponseHttpRequest: ...
            def train(
                self,
                *,
                parent: str,
                body: GoogleCloudDialogflowV2beta1TrainAgentRequest = ...,
                **kwargs: typing.Any
            ) -> GoogleLongrunningOperationHttpRequest: ...
            def updateFulfillment(
                self,
                *,
                name: str,
                body: GoogleCloudDialogflowV2beta1Fulfillment = ...,
                updateMask: str = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudDialogflowV2beta1FulfillmentHttpRequest: ...
            def entityTypes(self) -> EntityTypesResource: ...
            def intents(self) -> IntentsResource: ...
            def sessions(self) -> SessionsResource: ...
            def knowledgeBases(self) -> KnowledgeBasesResource: ...
            def environments(self) -> EnvironmentsResource: ...
        class LocationsResource(googleapiclient.discovery.Resource):
            class AgentResource(googleapiclient.discovery.Resource):
                class EntityTypesResource(googleapiclient.discovery.Resource):
                    class EntitiesResource(googleapiclient.discovery.Resource):
                        def batchDelete(
                            self,
                            *,
                            parent: str,
                            body: GoogleCloudDialogflowV2beta1BatchDeleteEntitiesRequest = ...,
                            **kwargs: typing.Any
                        ) -> GoogleLongrunningOperationHttpRequest: ...
                        def batchCreate(
                            self,
                            *,
                            parent: str,
                            body: GoogleCloudDialogflowV2beta1BatchCreateEntitiesRequest = ...,
                            **kwargs: typing.Any
                        ) -> GoogleLongrunningOperationHttpRequest: ...
                        def batchUpdate(
                            self,
                            *,
                            parent: str,
                            body: GoogleCloudDialogflowV2beta1BatchUpdateEntitiesRequest = ...,
                            **kwargs: typing.Any
                        ) -> GoogleLongrunningOperationHttpRequest: ...
                    def batchDelete(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudDialogflowV2beta1BatchDeleteEntityTypesRequest = ...,
                        **kwargs: typing.Any
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def create(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudDialogflowV2beta1EntityType = ...,
                        languageCode: str = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudDialogflowV2beta1EntityTypeHttpRequest: ...
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleProtobufEmptyHttpRequest: ...
                    def get(
                        self,
                        *,
                        name: str,
                        languageCode: str = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudDialogflowV2beta1EntityTypeHttpRequest: ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudDialogflowV2beta1EntityType = ...,
                        languageCode: str = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudDialogflowV2beta1EntityTypeHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        languageCode: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudDialogflowV2beta1ListEntityTypesResponseHttpRequest: ...
                    def batchUpdate(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudDialogflowV2beta1BatchUpdateEntityTypesRequest = ...,
                        **kwargs: typing.Any
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def entities(self) -> EntitiesResource: ...
                class IntentsResource(googleapiclient.discovery.Resource):
                    def batchDelete(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudDialogflowV2beta1BatchDeleteIntentsRequest = ...,
                        **kwargs: typing.Any
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleProtobufEmptyHttpRequest: ...
                    def create(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudDialogflowV2beta1Intent = ...,
                        intentView: typing_extensions.Literal[
                            "INTENT_VIEW_UNSPECIFIED", "INTENT_VIEW_FULL"
                        ] = ...,
                        languageCode: str = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudDialogflowV2beta1IntentHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        pageSize: int = ...,
                        languageCode: str = ...,
                        pageToken: str = ...,
                        intentView: typing_extensions.Literal[
                            "INTENT_VIEW_UNSPECIFIED", "INTENT_VIEW_FULL"
                        ] = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudDialogflowV2beta1ListIntentsResponseHttpRequest: ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudDialogflowV2beta1Intent = ...,
                        updateMask: str = ...,
                        languageCode: str = ...,
                        intentView: typing_extensions.Literal[
                            "INTENT_VIEW_UNSPECIFIED", "INTENT_VIEW_FULL"
                        ] = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudDialogflowV2beta1IntentHttpRequest: ...
                    def get(
                        self,
                        *,
                        name: str,
                        languageCode: str = ...,
                        intentView: typing_extensions.Literal[
                            "INTENT_VIEW_UNSPECIFIED", "INTENT_VIEW_FULL"
                        ] = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudDialogflowV2beta1IntentHttpRequest: ...
                    def batchUpdate(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudDialogflowV2beta1BatchUpdateIntentsRequest = ...,
                        **kwargs: typing.Any
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                class SessionsResource(googleapiclient.discovery.Resource):
                    class EntityTypesResource(googleapiclient.discovery.Resource):
                        def delete(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> GoogleProtobufEmptyHttpRequest: ...
                        def patch(
                            self,
                            *,
                            name: str,
                            body: GoogleCloudDialogflowV2beta1SessionEntityType = ...,
                            updateMask: str = ...,
                            **kwargs: typing.Any
                        ) -> GoogleCloudDialogflowV2beta1SessionEntityTypeHttpRequest: ...
                        def create(
                            self,
                            *,
                            parent: str,
                            body: GoogleCloudDialogflowV2beta1SessionEntityType = ...,
                            **kwargs: typing.Any
                        ) -> GoogleCloudDialogflowV2beta1SessionEntityTypeHttpRequest: ...
                        def get(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> GoogleCloudDialogflowV2beta1SessionEntityTypeHttpRequest: ...
                        def list(
                            self,
                            *,
                            parent: str,
                            pageToken: str = ...,
                            pageSize: int = ...,
                            **kwargs: typing.Any
                        ) -> GoogleCloudDialogflowV2beta1ListSessionEntityTypesResponseHttpRequest: ...
                    class ContextsResource(googleapiclient.discovery.Resource):
                        def list(
                            self,
                            *,
                            parent: str,
                            pageToken: str = ...,
                            pageSize: int = ...,
                            **kwargs: typing.Any
                        ) -> GoogleCloudDialogflowV2beta1ListContextsResponseHttpRequest: ...
                        def patch(
                            self,
                            *,
                            name: str,
                            body: GoogleCloudDialogflowV2beta1Context = ...,
                            updateMask: str = ...,
                            **kwargs: typing.Any
                        ) -> GoogleCloudDialogflowV2beta1ContextHttpRequest: ...
                        def create(
                            self,
                            *,
                            parent: str,
                            body: GoogleCloudDialogflowV2beta1Context = ...,
                            **kwargs: typing.Any
                        ) -> GoogleCloudDialogflowV2beta1ContextHttpRequest: ...
                        def get(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> GoogleCloudDialogflowV2beta1ContextHttpRequest: ...
                        def delete(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> GoogleProtobufEmptyHttpRequest: ...
                    def deleteContexts(
                        self, *, parent: str, **kwargs: typing.Any
                    ) -> GoogleProtobufEmptyHttpRequest: ...
                    def detectIntent(
                        self,
                        *,
                        session: str,
                        body: GoogleCloudDialogflowV2beta1DetectIntentRequest = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudDialogflowV2beta1DetectIntentResponseHttpRequest: ...
                    def entityTypes(self) -> EntityTypesResource: ...
                    def contexts(self) -> ContextsResource: ...
                class EnvironmentsResource(googleapiclient.discovery.Resource):
                    class UsersResource(googleapiclient.discovery.Resource):
                        class SessionsResource(googleapiclient.discovery.Resource):
                            class EntityTypesResource(
                                googleapiclient.discovery.Resource
                            ):
                                def get(
                                    self, *, name: str, **kwargs: typing.Any
                                ) -> GoogleCloudDialogflowV2beta1SessionEntityTypeHttpRequest: ...
                                def list(
                                    self,
                                    *,
                                    parent: str,
                                    pageSize: int = ...,
                                    pageToken: str = ...,
                                    **kwargs: typing.Any
                                ) -> GoogleCloudDialogflowV2beta1ListSessionEntityTypesResponseHttpRequest: ...
                                def delete(
                                    self, *, name: str, **kwargs: typing.Any
                                ) -> GoogleProtobufEmptyHttpRequest: ...
                                def create(
                                    self,
                                    *,
                                    parent: str,
                                    body: GoogleCloudDialogflowV2beta1SessionEntityType = ...,
                                    **kwargs: typing.Any
                                ) -> GoogleCloudDialogflowV2beta1SessionEntityTypeHttpRequest: ...
                                def patch(
                                    self,
                                    *,
                                    name: str,
                                    body: GoogleCloudDialogflowV2beta1SessionEntityType = ...,
                                    updateMask: str = ...,
                                    **kwargs: typing.Any
                                ) -> GoogleCloudDialogflowV2beta1SessionEntityTypeHttpRequest: ...
                            class ContextsResource(googleapiclient.discovery.Resource):
                                def list(
                                    self,
                                    *,
                                    parent: str,
                                    pageSize: int = ...,
                                    pageToken: str = ...,
                                    **kwargs: typing.Any
                                ) -> GoogleCloudDialogflowV2beta1ListContextsResponseHttpRequest: ...
                                def patch(
                                    self,
                                    *,
                                    name: str,
                                    body: GoogleCloudDialogflowV2beta1Context = ...,
                                    updateMask: str = ...,
                                    **kwargs: typing.Any
                                ) -> GoogleCloudDialogflowV2beta1ContextHttpRequest: ...
                                def create(
                                    self,
                                    *,
                                    parent: str,
                                    body: GoogleCloudDialogflowV2beta1Context = ...,
                                    **kwargs: typing.Any
                                ) -> GoogleCloudDialogflowV2beta1ContextHttpRequest: ...
                                def delete(
                                    self, *, name: str, **kwargs: typing.Any
                                ) -> GoogleProtobufEmptyHttpRequest: ...
                                def get(
                                    self, *, name: str, **kwargs: typing.Any
                                ) -> GoogleCloudDialogflowV2beta1ContextHttpRequest: ...
                            def deleteContexts(
                                self, *, parent: str, **kwargs: typing.Any
                            ) -> GoogleProtobufEmptyHttpRequest: ...
                            def detectIntent(
                                self,
                                *,
                                session: str,
                                body: GoogleCloudDialogflowV2beta1DetectIntentRequest = ...,
                                **kwargs: typing.Any
                            ) -> GoogleCloudDialogflowV2beta1DetectIntentResponseHttpRequest: ...
                            def entityTypes(self) -> EntityTypesResource: ...
                            def contexts(self) -> ContextsResource: ...
                        def sessions(self) -> SessionsResource: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        pageToken: str = ...,
                        pageSize: int = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudDialogflowV2beta1ListEnvironmentsResponseHttpRequest: ...
                    def users(self) -> UsersResource: ...
                def getValidationResult(
                    self, *, parent: str, languageCode: str = ..., **kwargs: typing.Any
                ) -> GoogleCloudDialogflowV2beta1ValidationResultHttpRequest: ...
                def search(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudDialogflowV2beta1SearchAgentsResponseHttpRequest: ...
                def updateFulfillment(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudDialogflowV2beta1Fulfillment = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudDialogflowV2beta1FulfillmentHttpRequest: ...
                def train(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudDialogflowV2beta1TrainAgentRequest = ...,
                    **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def import_(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudDialogflowV2beta1ImportAgentRequest = ...,
                    **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def restore(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudDialogflowV2beta1RestoreAgentRequest = ...,
                    **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def getFulfillment(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudDialogflowV2beta1FulfillmentHttpRequest: ...
                def export(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudDialogflowV2beta1ExportAgentRequest = ...,
                    **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def entityTypes(self) -> EntityTypesResource: ...
                def intents(self) -> IntentsResource: ...
                def sessions(self) -> SessionsResource: ...
                def environments(self) -> EnvironmentsResource: ...
            class OperationsResource(googleapiclient.discovery.Resource):
                def list(
                    self,
                    *,
                    name: str,
                    filter: str = ...,
                    pageToken: str = ...,
                    pageSize: int = ...,
                    **kwargs: typing.Any
                ) -> GoogleLongrunningListOperationsResponseHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def cancel(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleProtobufEmptyHttpRequest: ...
            def deleteAgent(
                self, *, parent: str, **kwargs: typing.Any
            ) -> GoogleProtobufEmptyHttpRequest: ...
            def getAgent(
                self, *, parent: str, **kwargs: typing.Any
            ) -> GoogleCloudDialogflowV2beta1AgentHttpRequest: ...
            def setAgent(
                self,
                *,
                parent: str,
                body: GoogleCloudDialogflowV2beta1Agent = ...,
                updateMask: str = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudDialogflowV2beta1AgentHttpRequest: ...
            def agent(self) -> AgentResource: ...
            def operations(self) -> OperationsResource: ...
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
                pageSize: int = ...,
                pageToken: str = ...,
                filter: str = ...,
                **kwargs: typing.Any
            ) -> GoogleLongrunningListOperationsResponseHttpRequest: ...
        class KnowledgeBasesResource(googleapiclient.discovery.Resource):
            class DocumentsResource(googleapiclient.discovery.Resource):
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudDialogflowV2beta1DocumentHttpRequest: ...
                def reload(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudDialogflowV2beta1ReloadDocumentRequest = ...,
                    **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudDialogflowV2beta1ListDocumentsResponseHttpRequest: ...
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudDialogflowV2beta1Document = ...,
                    **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudDialogflowV2beta1Document = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleCloudDialogflowV2beta1KnowledgeBaseHttpRequest: ...
            def delete(
                self, *, name: str, force: bool = ..., **kwargs: typing.Any
            ) -> GoogleProtobufEmptyHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudDialogflowV2beta1ListKnowledgeBasesResponseHttpRequest: ...
            def create(
                self,
                *,
                parent: str,
                body: GoogleCloudDialogflowV2beta1KnowledgeBase = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudDialogflowV2beta1KnowledgeBaseHttpRequest: ...
            def patch(
                self,
                *,
                name: str,
                body: GoogleCloudDialogflowV2beta1KnowledgeBase = ...,
                updateMask: str = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudDialogflowV2beta1KnowledgeBaseHttpRequest: ...
            def documents(self) -> DocumentsResource: ...
        def getAgent(
            self, *, parent: str, **kwargs: typing.Any
        ) -> GoogleCloudDialogflowV2beta1AgentHttpRequest: ...
        def setAgent(
            self,
            *,
            parent: str,
            body: GoogleCloudDialogflowV2beta1Agent = ...,
            updateMask: str = ...,
            **kwargs: typing.Any
        ) -> GoogleCloudDialogflowV2beta1AgentHttpRequest: ...
        def deleteAgent(
            self, *, parent: str, **kwargs: typing.Any
        ) -> GoogleProtobufEmptyHttpRequest: ...
        def agent(self) -> AgentResource: ...
        def locations(self) -> LocationsResource: ...
        def operations(self) -> OperationsResource: ...
        def knowledgeBases(self) -> KnowledgeBasesResource: ...
    def projects(self) -> ProjectsResource: ...

class GoogleCloudDialogflowV2beta1FulfillmentHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudDialogflowV2beta1Fulfillment: ...

class GoogleCloudDialogflowV2beta1ListContextsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudDialogflowV2beta1ListContextsResponse: ...

class GoogleProtobufEmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleProtobufEmpty: ...

class GoogleCloudDialogflowV2beta1ValidationResultHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudDialogflowV2beta1ValidationResult: ...

class GoogleCloudDialogflowV2beta1ContextHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudDialogflowV2beta1Context: ...

class GoogleCloudDialogflowV2beta1SessionEntityTypeHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudDialogflowV2beta1SessionEntityType: ...

class GoogleCloudDialogflowV2beta1IntentHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudDialogflowV2beta1Intent: ...

class GoogleCloudDialogflowV2beta1DocumentHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudDialogflowV2beta1Document: ...

class GoogleCloudDialogflowV2beta1SearchAgentsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudDialogflowV2beta1SearchAgentsResponse: ...

class GoogleLongrunningListOperationsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleLongrunningListOperationsResponse: ...

class GoogleCloudDialogflowV2beta1ListEnvironmentsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudDialogflowV2beta1ListEnvironmentsResponse: ...

class GoogleLongrunningOperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleLongrunningOperation: ...

class GoogleCloudDialogflowV2beta1AgentHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudDialogflowV2beta1Agent: ...

class GoogleCloudDialogflowV2beta1DetectIntentResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudDialogflowV2beta1DetectIntentResponse: ...

class GoogleCloudDialogflowV2beta1ListDocumentsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudDialogflowV2beta1ListDocumentsResponse: ...

class GoogleCloudDialogflowV2beta1KnowledgeBaseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudDialogflowV2beta1KnowledgeBase: ...

class GoogleCloudDialogflowV2beta1ListKnowledgeBasesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudDialogflowV2beta1ListKnowledgeBasesResponse: ...

class GoogleCloudDialogflowV2beta1EntityTypeHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudDialogflowV2beta1EntityType: ...

class GoogleCloudDialogflowV2beta1ListSessionEntityTypesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudDialogflowV2beta1ListSessionEntityTypesResponse: ...

class GoogleCloudDialogflowV2beta1ListEntityTypesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudDialogflowV2beta1ListEntityTypesResponse: ...

class GoogleCloudDialogflowV2beta1ListIntentsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudDialogflowV2beta1ListIntentsResponse: ...
