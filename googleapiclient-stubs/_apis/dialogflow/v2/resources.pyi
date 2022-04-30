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
        class AgentResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class EntityTypesResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class EntitiesResource(googleapiclient.discovery.Resource):
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
                    def batchUpdate(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudDialogflowV2BatchUpdateEntitiesRequest = ...,
                        **kwargs: typing.Any
                    ) -> GoogleLongrunningOperationHttpRequest: ...

                def batchDelete(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudDialogflowV2BatchDeleteEntityTypesRequest = ...,
                    **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def batchUpdate(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudDialogflowV2BatchUpdateEntityTypesRequest = ...,
                    **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudDialogflowV2EntityType = ...,
                    languageCode: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudDialogflowV2EntityTypeHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleProtobufEmptyHttpRequest: ...
                def get(
                    self, *, name: str, languageCode: str = ..., **kwargs: typing.Any
                ) -> GoogleCloudDialogflowV2EntityTypeHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    languageCode: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudDialogflowV2ListEntityTypesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudDialogflowV2ListEntityTypesResponseHttpRequest,
                    previous_response: GoogleCloudDialogflowV2ListEntityTypesResponse,
                ) -> GoogleCloudDialogflowV2ListEntityTypesResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudDialogflowV2EntityType = ...,
                    languageCode: str = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudDialogflowV2EntityTypeHttpRequest: ...
                def entities(self) -> EntitiesResource: ...

            @typing.type_check_only
            class EnvironmentsResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class IntentsResource(googleapiclient.discovery.Resource):
                    def list(
                        self,
                        *,
                        parent: str,
                        intentView: typing_extensions.Literal[
                            "INTENT_VIEW_UNSPECIFIED", "INTENT_VIEW_FULL"
                        ] = ...,
                        languageCode: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudDialogflowV2ListIntentsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudDialogflowV2ListIntentsResponseHttpRequest,
                        previous_response: GoogleCloudDialogflowV2ListIntentsResponse,
                    ) -> GoogleCloudDialogflowV2ListIntentsResponseHttpRequest | None: ...

                @typing.type_check_only
                class UsersResource(googleapiclient.discovery.Resource):
                    @typing.type_check_only
                    class SessionsResource(googleapiclient.discovery.Resource):
                        @typing.type_check_only
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
                            def list_next(
                                self,
                                previous_request: GoogleCloudDialogflowV2ListContextsResponseHttpRequest,
                                previous_response: GoogleCloudDialogflowV2ListContextsResponse,
                            ) -> GoogleCloudDialogflowV2ListContextsResponseHttpRequest | None: ...
                            def patch(
                                self,
                                *,
                                name: str,
                                body: GoogleCloudDialogflowV2Context = ...,
                                updateMask: str = ...,
                                **kwargs: typing.Any
                            ) -> GoogleCloudDialogflowV2ContextHttpRequest: ...

                        @typing.type_check_only
                        class EntityTypesResource(googleapiclient.discovery.Resource):
                            def create(
                                self,
                                *,
                                parent: str,
                                body: GoogleCloudDialogflowV2SessionEntityType = ...,
                                **kwargs: typing.Any
                            ) -> GoogleCloudDialogflowV2SessionEntityTypeHttpRequest: ...
                            def delete(
                                self, *, name: str, **kwargs: typing.Any
                            ) -> GoogleProtobufEmptyHttpRequest: ...
                            def get(
                                self, *, name: str, **kwargs: typing.Any
                            ) -> GoogleCloudDialogflowV2SessionEntityTypeHttpRequest: ...
                            def list(
                                self,
                                *,
                                parent: str,
                                pageSize: int = ...,
                                pageToken: str = ...,
                                **kwargs: typing.Any
                            ) -> GoogleCloudDialogflowV2ListSessionEntityTypesResponseHttpRequest: ...
                            def list_next(
                                self,
                                previous_request: GoogleCloudDialogflowV2ListSessionEntityTypesResponseHttpRequest,
                                previous_response: GoogleCloudDialogflowV2ListSessionEntityTypesResponse,
                            ) -> GoogleCloudDialogflowV2ListSessionEntityTypesResponseHttpRequest | None: ...
                            def patch(
                                self,
                                *,
                                name: str,
                                body: GoogleCloudDialogflowV2SessionEntityType = ...,
                                updateMask: str = ...,
                                **kwargs: typing.Any
                            ) -> GoogleCloudDialogflowV2SessionEntityTypeHttpRequest: ...

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
                        def contexts(self) -> ContextsResource: ...
                        def entityTypes(self) -> EntityTypesResource: ...

                    def sessions(self) -> SessionsResource: ...

                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudDialogflowV2Environment = ...,
                    environmentId: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudDialogflowV2EnvironmentHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleProtobufEmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudDialogflowV2EnvironmentHttpRequest: ...
                def getHistory(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudDialogflowV2EnvironmentHistoryHttpRequest: ...
                def getHistory_next(
                    self,
                    previous_request: GoogleCloudDialogflowV2EnvironmentHistoryHttpRequest,
                    previous_response: GoogleCloudDialogflowV2EnvironmentHistory,
                ) -> GoogleCloudDialogflowV2EnvironmentHistoryHttpRequest | None: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudDialogflowV2ListEnvironmentsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudDialogflowV2ListEnvironmentsResponseHttpRequest,
                    previous_response: GoogleCloudDialogflowV2ListEnvironmentsResponse,
                ) -> GoogleCloudDialogflowV2ListEnvironmentsResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudDialogflowV2Environment = ...,
                    allowLoadToDraftAndDiscardChanges: bool = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudDialogflowV2EnvironmentHttpRequest: ...
                def intents(self) -> IntentsResource: ...
                def users(self) -> UsersResource: ...

            @typing.type_check_only
            class IntentsResource(googleapiclient.discovery.Resource):
                def batchDelete(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudDialogflowV2BatchDeleteIntentsRequest = ...,
                    **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def batchUpdate(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudDialogflowV2BatchUpdateIntentsRequest = ...,
                    **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
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
                def list(
                    self,
                    *,
                    parent: str,
                    intentView: typing_extensions.Literal[
                        "INTENT_VIEW_UNSPECIFIED", "INTENT_VIEW_FULL"
                    ] = ...,
                    languageCode: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudDialogflowV2ListIntentsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudDialogflowV2ListIntentsResponseHttpRequest,
                    previous_response: GoogleCloudDialogflowV2ListIntentsResponse,
                ) -> GoogleCloudDialogflowV2ListIntentsResponseHttpRequest | None: ...
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

            @typing.type_check_only
            class KnowledgeBasesResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class DocumentsResource(googleapiclient.discovery.Resource):
                    def create(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudDialogflowV2Document = ...,
                        **kwargs: typing.Any
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleCloudDialogflowV2DocumentHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudDialogflowV2ListDocumentsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudDialogflowV2ListDocumentsResponseHttpRequest,
                        previous_response: GoogleCloudDialogflowV2ListDocumentsResponse,
                    ) -> GoogleCloudDialogflowV2ListDocumentsResponseHttpRequest | None: ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudDialogflowV2Document = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def reload(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudDialogflowV2ReloadDocumentRequest = ...,
                        **kwargs: typing.Any
                    ) -> GoogleLongrunningOperationHttpRequest: ...

                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudDialogflowV2KnowledgeBase = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudDialogflowV2KnowledgeBaseHttpRequest: ...
                def delete(
                    self, *, name: str, force: bool = ..., **kwargs: typing.Any
                ) -> GoogleProtobufEmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudDialogflowV2KnowledgeBaseHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudDialogflowV2ListKnowledgeBasesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudDialogflowV2ListKnowledgeBasesResponseHttpRequest,
                    previous_response: GoogleCloudDialogflowV2ListKnowledgeBasesResponse,
                ) -> GoogleCloudDialogflowV2ListKnowledgeBasesResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudDialogflowV2KnowledgeBase = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudDialogflowV2KnowledgeBaseHttpRequest: ...
                def documents(self) -> DocumentsResource: ...

            @typing.type_check_only
            class SessionsResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
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
                    def list_next(
                        self,
                        previous_request: GoogleCloudDialogflowV2ListContextsResponseHttpRequest,
                        previous_response: GoogleCloudDialogflowV2ListContextsResponse,
                    ) -> GoogleCloudDialogflowV2ListContextsResponseHttpRequest | None: ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudDialogflowV2Context = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudDialogflowV2ContextHttpRequest: ...

                @typing.type_check_only
                class EntityTypesResource(googleapiclient.discovery.Resource):
                    def create(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudDialogflowV2SessionEntityType = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudDialogflowV2SessionEntityTypeHttpRequest: ...
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleProtobufEmptyHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleCloudDialogflowV2SessionEntityTypeHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudDialogflowV2ListSessionEntityTypesResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudDialogflowV2ListSessionEntityTypesResponseHttpRequest,
                        previous_response: GoogleCloudDialogflowV2ListSessionEntityTypesResponse,
                    ) -> GoogleCloudDialogflowV2ListSessionEntityTypesResponseHttpRequest | None: ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudDialogflowV2SessionEntityType = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudDialogflowV2SessionEntityTypeHttpRequest: ...

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
                def contexts(self) -> ContextsResource: ...
                def entityTypes(self) -> EntityTypesResource: ...

            @typing.type_check_only
            class VersionsResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudDialogflowV2Version = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudDialogflowV2VersionHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleProtobufEmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudDialogflowV2VersionHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudDialogflowV2ListVersionsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudDialogflowV2ListVersionsResponseHttpRequest,
                    previous_response: GoogleCloudDialogflowV2ListVersionsResponse,
                ) -> GoogleCloudDialogflowV2ListVersionsResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudDialogflowV2Version = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudDialogflowV2VersionHttpRequest: ...

            def export(
                self,
                *,
                parent: str,
                body: GoogleCloudDialogflowV2ExportAgentRequest = ...,
                **kwargs: typing.Any
            ) -> GoogleLongrunningOperationHttpRequest: ...
            def getFulfillment(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleCloudDialogflowV2FulfillmentHttpRequest: ...
            def getValidationResult(
                self, *, parent: str, languageCode: str = ..., **kwargs: typing.Any
            ) -> GoogleCloudDialogflowV2ValidationResultHttpRequest: ...
            def import_(
                self,
                *,
                parent: str,
                body: GoogleCloudDialogflowV2ImportAgentRequest = ...,
                **kwargs: typing.Any
            ) -> GoogleLongrunningOperationHttpRequest: ...
            def restore(
                self,
                *,
                parent: str,
                body: GoogleCloudDialogflowV2RestoreAgentRequest = ...,
                **kwargs: typing.Any
            ) -> GoogleLongrunningOperationHttpRequest: ...
            def search(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudDialogflowV2SearchAgentsResponseHttpRequest: ...
            def search_next(
                self,
                previous_request: GoogleCloudDialogflowV2SearchAgentsResponseHttpRequest,
                previous_response: GoogleCloudDialogflowV2SearchAgentsResponse,
            ) -> GoogleCloudDialogflowV2SearchAgentsResponseHttpRequest | None: ...
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
            def entityTypes(self) -> EntityTypesResource: ...
            def environments(self) -> EnvironmentsResource: ...
            def intents(self) -> IntentsResource: ...
            def knowledgeBases(self) -> KnowledgeBasesResource: ...
            def sessions(self) -> SessionsResource: ...
            def versions(self) -> VersionsResource: ...

        @typing.type_check_only
        class AnswerRecordsResource(googleapiclient.discovery.Resource):
            def list(
                self,
                *,
                parent: str,
                filter: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudDialogflowV2ListAnswerRecordsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: GoogleCloudDialogflowV2ListAnswerRecordsResponseHttpRequest,
                previous_response: GoogleCloudDialogflowV2ListAnswerRecordsResponse,
            ) -> GoogleCloudDialogflowV2ListAnswerRecordsResponseHttpRequest | None: ...
            def patch(
                self,
                *,
                name: str,
                body: GoogleCloudDialogflowV2AnswerRecord = ...,
                updateMask: str = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudDialogflowV2AnswerRecordHttpRequest: ...

        @typing.type_check_only
        class ConversationDatasetsResource(googleapiclient.discovery.Resource):
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleCloudDialogflowV2ConversationDatasetHttpRequest: ...
            def importConversationData(
                self,
                *,
                name: str,
                body: GoogleCloudDialogflowV2ImportConversationDataRequest = ...,
                **kwargs: typing.Any
            ) -> GoogleLongrunningOperationHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudDialogflowV2ListConversationDatasetsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: GoogleCloudDialogflowV2ListConversationDatasetsResponseHttpRequest,
                previous_response: GoogleCloudDialogflowV2ListConversationDatasetsResponse,
            ) -> GoogleCloudDialogflowV2ListConversationDatasetsResponseHttpRequest | None: ...

        @typing.type_check_only
        class ConversationModelsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class EvaluationsResource(googleapiclient.discovery.Resource):
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudDialogflowV2ConversationModelEvaluationHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudDialogflowV2ListConversationModelEvaluationsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudDialogflowV2ListConversationModelEvaluationsResponseHttpRequest,
                    previous_response: GoogleCloudDialogflowV2ListConversationModelEvaluationsResponse,
                ) -> GoogleCloudDialogflowV2ListConversationModelEvaluationsResponseHttpRequest | None: ...

            def create(
                self,
                *,
                parent: str,
                body: GoogleCloudDialogflowV2ConversationModel = ...,
                **kwargs: typing.Any
            ) -> GoogleLongrunningOperationHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleLongrunningOperationHttpRequest: ...
            def deploy(
                self,
                *,
                name: str,
                body: GoogleCloudDialogflowV2DeployConversationModelRequest = ...,
                **kwargs: typing.Any
            ) -> GoogleLongrunningOperationHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleCloudDialogflowV2ConversationModelHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudDialogflowV2ListConversationModelsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: GoogleCloudDialogflowV2ListConversationModelsResponseHttpRequest,
                previous_response: GoogleCloudDialogflowV2ListConversationModelsResponse,
            ) -> GoogleCloudDialogflowV2ListConversationModelsResponseHttpRequest | None: ...
            def undeploy(
                self,
                *,
                name: str,
                body: GoogleCloudDialogflowV2UndeployConversationModelRequest = ...,
                **kwargs: typing.Any
            ) -> GoogleLongrunningOperationHttpRequest: ...
            def evaluations(self) -> EvaluationsResource: ...

        @typing.type_check_only
        class ConversationProfilesResource(googleapiclient.discovery.Resource):
            def clearSuggestionFeatureConfig(
                self,
                *,
                conversationProfile: str,
                body: GoogleCloudDialogflowV2ClearSuggestionFeatureConfigRequest = ...,
                **kwargs: typing.Any
            ) -> GoogleLongrunningOperationHttpRequest: ...
            def create(
                self,
                *,
                parent: str,
                body: GoogleCloudDialogflowV2ConversationProfile = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudDialogflowV2ConversationProfileHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleProtobufEmptyHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleCloudDialogflowV2ConversationProfileHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudDialogflowV2ListConversationProfilesResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: GoogleCloudDialogflowV2ListConversationProfilesResponseHttpRequest,
                previous_response: GoogleCloudDialogflowV2ListConversationProfilesResponse,
            ) -> GoogleCloudDialogflowV2ListConversationProfilesResponseHttpRequest | None: ...
            def patch(
                self,
                *,
                name: str,
                body: GoogleCloudDialogflowV2ConversationProfile = ...,
                updateMask: str = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudDialogflowV2ConversationProfileHttpRequest: ...
            def setSuggestionFeatureConfig(
                self,
                *,
                conversationProfile: str,
                body: GoogleCloudDialogflowV2SetSuggestionFeatureConfigRequest = ...,
                **kwargs: typing.Any
            ) -> GoogleLongrunningOperationHttpRequest: ...

        @typing.type_check_only
        class ConversationsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class MessagesResource(googleapiclient.discovery.Resource):
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudDialogflowV2ListMessagesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudDialogflowV2ListMessagesResponseHttpRequest,
                    previous_response: GoogleCloudDialogflowV2ListMessagesResponse,
                ) -> GoogleCloudDialogflowV2ListMessagesResponseHttpRequest | None: ...

            @typing.type_check_only
            class ParticipantsResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class SuggestionsResource(googleapiclient.discovery.Resource):
                    def suggestArticles(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudDialogflowV2SuggestArticlesRequest = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudDialogflowV2SuggestArticlesResponseHttpRequest: ...
                    def suggestFaqAnswers(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudDialogflowV2SuggestFaqAnswersRequest = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudDialogflowV2SuggestFaqAnswersResponseHttpRequest: ...
                    def suggestSmartReplies(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudDialogflowV2SuggestSmartRepliesRequest = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudDialogflowV2SuggestSmartRepliesResponseHttpRequest: ...

                def analyzeContent(
                    self,
                    *,
                    participant: str,
                    body: GoogleCloudDialogflowV2AnalyzeContentRequest = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudDialogflowV2AnalyzeContentResponseHttpRequest: ...
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudDialogflowV2Participant = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudDialogflowV2ParticipantHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudDialogflowV2ParticipantHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudDialogflowV2ListParticipantsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudDialogflowV2ListParticipantsResponseHttpRequest,
                    previous_response: GoogleCloudDialogflowV2ListParticipantsResponse,
                ) -> GoogleCloudDialogflowV2ListParticipantsResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudDialogflowV2Participant = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudDialogflowV2ParticipantHttpRequest: ...
                def suggestions(self) -> SuggestionsResource: ...

            def complete(
                self,
                *,
                name: str,
                body: GoogleCloudDialogflowV2CompleteConversationRequest = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudDialogflowV2ConversationHttpRequest: ...
            def create(
                self,
                *,
                parent: str,
                body: GoogleCloudDialogflowV2Conversation = ...,
                conversationId: str = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudDialogflowV2ConversationHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleCloudDialogflowV2ConversationHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                filter: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudDialogflowV2ListConversationsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: GoogleCloudDialogflowV2ListConversationsResponseHttpRequest,
                previous_response: GoogleCloudDialogflowV2ListConversationsResponse,
            ) -> GoogleCloudDialogflowV2ListConversationsResponseHttpRequest | None: ...
            def messages(self) -> MessagesResource: ...
            def participants(self) -> ParticipantsResource: ...

        @typing.type_check_only
        class KnowledgeBasesResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class DocumentsResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudDialogflowV2Document = ...,
                    **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def export(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudDialogflowV2ExportDocumentRequest = ...,
                    **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudDialogflowV2DocumentHttpRequest: ...
                def import_(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudDialogflowV2ImportDocumentsRequest = ...,
                    **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudDialogflowV2ListDocumentsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudDialogflowV2ListDocumentsResponseHttpRequest,
                    previous_response: GoogleCloudDialogflowV2ListDocumentsResponse,
                ) -> GoogleCloudDialogflowV2ListDocumentsResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudDialogflowV2Document = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def reload(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudDialogflowV2ReloadDocumentRequest = ...,
                    **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...

            def create(
                self,
                *,
                parent: str,
                body: GoogleCloudDialogflowV2KnowledgeBase = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudDialogflowV2KnowledgeBaseHttpRequest: ...
            def delete(
                self, *, name: str, force: bool = ..., **kwargs: typing.Any
            ) -> GoogleProtobufEmptyHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleCloudDialogflowV2KnowledgeBaseHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                filter: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudDialogflowV2ListKnowledgeBasesResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: GoogleCloudDialogflowV2ListKnowledgeBasesResponseHttpRequest,
                previous_response: GoogleCloudDialogflowV2ListKnowledgeBasesResponse,
            ) -> GoogleCloudDialogflowV2ListKnowledgeBasesResponseHttpRequest | None: ...
            def patch(
                self,
                *,
                name: str,
                body: GoogleCloudDialogflowV2KnowledgeBase = ...,
                updateMask: str = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudDialogflowV2KnowledgeBaseHttpRequest: ...
            def documents(self) -> DocumentsResource: ...

        @typing.type_check_only
        class LocationsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class AgentResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class EntityTypesResource(googleapiclient.discovery.Resource):
                    @typing.type_check_only
                    class EntitiesResource(googleapiclient.discovery.Resource):
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
                        def batchUpdate(
                            self,
                            *,
                            parent: str,
                            body: GoogleCloudDialogflowV2BatchUpdateEntitiesRequest = ...,
                            **kwargs: typing.Any
                        ) -> GoogleLongrunningOperationHttpRequest: ...

                    def batchDelete(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudDialogflowV2BatchDeleteEntityTypesRequest = ...,
                        **kwargs: typing.Any
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def batchUpdate(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudDialogflowV2BatchUpdateEntityTypesRequest = ...,
                        **kwargs: typing.Any
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def create(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudDialogflowV2EntityType = ...,
                        languageCode: str = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudDialogflowV2EntityTypeHttpRequest: ...
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleProtobufEmptyHttpRequest: ...
                    def get(
                        self,
                        *,
                        name: str,
                        languageCode: str = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudDialogflowV2EntityTypeHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        languageCode: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudDialogflowV2ListEntityTypesResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudDialogflowV2ListEntityTypesResponseHttpRequest,
                        previous_response: GoogleCloudDialogflowV2ListEntityTypesResponse,
                    ) -> GoogleCloudDialogflowV2ListEntityTypesResponseHttpRequest | None: ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudDialogflowV2EntityType = ...,
                        languageCode: str = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudDialogflowV2EntityTypeHttpRequest: ...
                    def entities(self) -> EntitiesResource: ...

                @typing.type_check_only
                class EnvironmentsResource(googleapiclient.discovery.Resource):
                    @typing.type_check_only
                    class IntentsResource(googleapiclient.discovery.Resource):
                        def list(
                            self,
                            *,
                            parent: str,
                            intentView: typing_extensions.Literal[
                                "INTENT_VIEW_UNSPECIFIED", "INTENT_VIEW_FULL"
                            ] = ...,
                            languageCode: str = ...,
                            pageSize: int = ...,
                            pageToken: str = ...,
                            **kwargs: typing.Any
                        ) -> GoogleCloudDialogflowV2ListIntentsResponseHttpRequest: ...
                        def list_next(
                            self,
                            previous_request: GoogleCloudDialogflowV2ListIntentsResponseHttpRequest,
                            previous_response: GoogleCloudDialogflowV2ListIntentsResponse,
                        ) -> GoogleCloudDialogflowV2ListIntentsResponseHttpRequest | None: ...

                    @typing.type_check_only
                    class UsersResource(googleapiclient.discovery.Resource):
                        @typing.type_check_only
                        class SessionsResource(googleapiclient.discovery.Resource):
                            @typing.type_check_only
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
                                def list_next(
                                    self,
                                    previous_request: GoogleCloudDialogflowV2ListContextsResponseHttpRequest,
                                    previous_response: GoogleCloudDialogflowV2ListContextsResponse,
                                ) -> GoogleCloudDialogflowV2ListContextsResponseHttpRequest | None: ...
                                def patch(
                                    self,
                                    *,
                                    name: str,
                                    body: GoogleCloudDialogflowV2Context = ...,
                                    updateMask: str = ...,
                                    **kwargs: typing.Any
                                ) -> GoogleCloudDialogflowV2ContextHttpRequest: ...

                            @typing.type_check_only
                            class EntityTypesResource(
                                googleapiclient.discovery.Resource
                            ):
                                def create(
                                    self,
                                    *,
                                    parent: str,
                                    body: GoogleCloudDialogflowV2SessionEntityType = ...,
                                    **kwargs: typing.Any
                                ) -> GoogleCloudDialogflowV2SessionEntityTypeHttpRequest: ...
                                def delete(
                                    self, *, name: str, **kwargs: typing.Any
                                ) -> GoogleProtobufEmptyHttpRequest: ...
                                def get(
                                    self, *, name: str, **kwargs: typing.Any
                                ) -> GoogleCloudDialogflowV2SessionEntityTypeHttpRequest: ...
                                def list(
                                    self,
                                    *,
                                    parent: str,
                                    pageSize: int = ...,
                                    pageToken: str = ...,
                                    **kwargs: typing.Any
                                ) -> GoogleCloudDialogflowV2ListSessionEntityTypesResponseHttpRequest: ...
                                def list_next(
                                    self,
                                    previous_request: GoogleCloudDialogflowV2ListSessionEntityTypesResponseHttpRequest,
                                    previous_response: GoogleCloudDialogflowV2ListSessionEntityTypesResponse,
                                ) -> GoogleCloudDialogflowV2ListSessionEntityTypesResponseHttpRequest | None: ...
                                def patch(
                                    self,
                                    *,
                                    name: str,
                                    body: GoogleCloudDialogflowV2SessionEntityType = ...,
                                    updateMask: str = ...,
                                    **kwargs: typing.Any
                                ) -> GoogleCloudDialogflowV2SessionEntityTypeHttpRequest: ...

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
                            def contexts(self) -> ContextsResource: ...
                            def entityTypes(self) -> EntityTypesResource: ...

                        def sessions(self) -> SessionsResource: ...

                    def create(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudDialogflowV2Environment = ...,
                        environmentId: str = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudDialogflowV2EnvironmentHttpRequest: ...
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleProtobufEmptyHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleCloudDialogflowV2EnvironmentHttpRequest: ...
                    def getHistory(
                        self,
                        *,
                        parent: str,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudDialogflowV2EnvironmentHistoryHttpRequest: ...
                    def getHistory_next(
                        self,
                        previous_request: GoogleCloudDialogflowV2EnvironmentHistoryHttpRequest,
                        previous_response: GoogleCloudDialogflowV2EnvironmentHistory,
                    ) -> GoogleCloudDialogflowV2EnvironmentHistoryHttpRequest | None: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudDialogflowV2ListEnvironmentsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudDialogflowV2ListEnvironmentsResponseHttpRequest,
                        previous_response: GoogleCloudDialogflowV2ListEnvironmentsResponse,
                    ) -> GoogleCloudDialogflowV2ListEnvironmentsResponseHttpRequest | None: ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudDialogflowV2Environment = ...,
                        allowLoadToDraftAndDiscardChanges: bool = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudDialogflowV2EnvironmentHttpRequest: ...
                    def intents(self) -> IntentsResource: ...
                    def users(self) -> UsersResource: ...

                @typing.type_check_only
                class IntentsResource(googleapiclient.discovery.Resource):
                    def batchDelete(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudDialogflowV2BatchDeleteIntentsRequest = ...,
                        **kwargs: typing.Any
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def batchUpdate(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudDialogflowV2BatchUpdateIntentsRequest = ...,
                        **kwargs: typing.Any
                    ) -> GoogleLongrunningOperationHttpRequest: ...
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
                    def list(
                        self,
                        *,
                        parent: str,
                        intentView: typing_extensions.Literal[
                            "INTENT_VIEW_UNSPECIFIED", "INTENT_VIEW_FULL"
                        ] = ...,
                        languageCode: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudDialogflowV2ListIntentsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudDialogflowV2ListIntentsResponseHttpRequest,
                        previous_response: GoogleCloudDialogflowV2ListIntentsResponse,
                    ) -> GoogleCloudDialogflowV2ListIntentsResponseHttpRequest | None: ...
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

                @typing.type_check_only
                class SessionsResource(googleapiclient.discovery.Resource):
                    @typing.type_check_only
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
                        def list_next(
                            self,
                            previous_request: GoogleCloudDialogflowV2ListContextsResponseHttpRequest,
                            previous_response: GoogleCloudDialogflowV2ListContextsResponse,
                        ) -> GoogleCloudDialogflowV2ListContextsResponseHttpRequest | None: ...
                        def patch(
                            self,
                            *,
                            name: str,
                            body: GoogleCloudDialogflowV2Context = ...,
                            updateMask: str = ...,
                            **kwargs: typing.Any
                        ) -> GoogleCloudDialogflowV2ContextHttpRequest: ...

                    @typing.type_check_only
                    class EntityTypesResource(googleapiclient.discovery.Resource):
                        def create(
                            self,
                            *,
                            parent: str,
                            body: GoogleCloudDialogflowV2SessionEntityType = ...,
                            **kwargs: typing.Any
                        ) -> GoogleCloudDialogflowV2SessionEntityTypeHttpRequest: ...
                        def delete(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> GoogleProtobufEmptyHttpRequest: ...
                        def get(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> GoogleCloudDialogflowV2SessionEntityTypeHttpRequest: ...
                        def list(
                            self,
                            *,
                            parent: str,
                            pageSize: int = ...,
                            pageToken: str = ...,
                            **kwargs: typing.Any
                        ) -> GoogleCloudDialogflowV2ListSessionEntityTypesResponseHttpRequest: ...
                        def list_next(
                            self,
                            previous_request: GoogleCloudDialogflowV2ListSessionEntityTypesResponseHttpRequest,
                            previous_response: GoogleCloudDialogflowV2ListSessionEntityTypesResponse,
                        ) -> GoogleCloudDialogflowV2ListSessionEntityTypesResponseHttpRequest | None: ...
                        def patch(
                            self,
                            *,
                            name: str,
                            body: GoogleCloudDialogflowV2SessionEntityType = ...,
                            updateMask: str = ...,
                            **kwargs: typing.Any
                        ) -> GoogleCloudDialogflowV2SessionEntityTypeHttpRequest: ...

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
                    def contexts(self) -> ContextsResource: ...
                    def entityTypes(self) -> EntityTypesResource: ...

                @typing.type_check_only
                class VersionsResource(googleapiclient.discovery.Resource):
                    def create(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudDialogflowV2Version = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudDialogflowV2VersionHttpRequest: ...
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleProtobufEmptyHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleCloudDialogflowV2VersionHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudDialogflowV2ListVersionsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudDialogflowV2ListVersionsResponseHttpRequest,
                        previous_response: GoogleCloudDialogflowV2ListVersionsResponse,
                    ) -> GoogleCloudDialogflowV2ListVersionsResponseHttpRequest | None: ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudDialogflowV2Version = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudDialogflowV2VersionHttpRequest: ...

                def export(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudDialogflowV2ExportAgentRequest = ...,
                    **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def getFulfillment(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudDialogflowV2FulfillmentHttpRequest: ...
                def getValidationResult(
                    self, *, parent: str, languageCode: str = ..., **kwargs: typing.Any
                ) -> GoogleCloudDialogflowV2ValidationResultHttpRequest: ...
                def import_(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudDialogflowV2ImportAgentRequest = ...,
                    **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def restore(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudDialogflowV2RestoreAgentRequest = ...,
                    **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def search(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudDialogflowV2SearchAgentsResponseHttpRequest: ...
                def search_next(
                    self,
                    previous_request: GoogleCloudDialogflowV2SearchAgentsResponseHttpRequest,
                    previous_response: GoogleCloudDialogflowV2SearchAgentsResponse,
                ) -> GoogleCloudDialogflowV2SearchAgentsResponseHttpRequest | None: ...
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
                def entityTypes(self) -> EntityTypesResource: ...
                def environments(self) -> EnvironmentsResource: ...
                def intents(self) -> IntentsResource: ...
                def sessions(self) -> SessionsResource: ...
                def versions(self) -> VersionsResource: ...

            @typing.type_check_only
            class AnswerRecordsResource(googleapiclient.discovery.Resource):
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudDialogflowV2ListAnswerRecordsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudDialogflowV2ListAnswerRecordsResponseHttpRequest,
                    previous_response: GoogleCloudDialogflowV2ListAnswerRecordsResponse,
                ) -> GoogleCloudDialogflowV2ListAnswerRecordsResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudDialogflowV2AnswerRecord = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudDialogflowV2AnswerRecordHttpRequest: ...

            @typing.type_check_only
            class ConversationDatasetsResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudDialogflowV2ConversationDataset = ...,
                    **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudDialogflowV2ConversationDatasetHttpRequest: ...
                def importConversationData(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudDialogflowV2ImportConversationDataRequest = ...,
                    **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudDialogflowV2ListConversationDatasetsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudDialogflowV2ListConversationDatasetsResponseHttpRequest,
                    previous_response: GoogleCloudDialogflowV2ListConversationDatasetsResponse,
                ) -> GoogleCloudDialogflowV2ListConversationDatasetsResponseHttpRequest | None: ...

            @typing.type_check_only
            class ConversationModelsResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class EvaluationsResource(googleapiclient.discovery.Resource):
                    def create(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudDialogflowV2CreateConversationModelEvaluationRequest = ...,
                        **kwargs: typing.Any
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleCloudDialogflowV2ConversationModelEvaluationHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudDialogflowV2ListConversationModelEvaluationsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudDialogflowV2ListConversationModelEvaluationsResponseHttpRequest,
                        previous_response: GoogleCloudDialogflowV2ListConversationModelEvaluationsResponse,
                    ) -> GoogleCloudDialogflowV2ListConversationModelEvaluationsResponseHttpRequest | None: ...

                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudDialogflowV2ConversationModel = ...,
                    **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def deploy(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudDialogflowV2DeployConversationModelRequest = ...,
                    **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudDialogflowV2ConversationModelHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudDialogflowV2ListConversationModelsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudDialogflowV2ListConversationModelsResponseHttpRequest,
                    previous_response: GoogleCloudDialogflowV2ListConversationModelsResponse,
                ) -> GoogleCloudDialogflowV2ListConversationModelsResponseHttpRequest | None: ...
                def undeploy(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudDialogflowV2UndeployConversationModelRequest = ...,
                    **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def evaluations(self) -> EvaluationsResource: ...

            @typing.type_check_only
            class ConversationProfilesResource(googleapiclient.discovery.Resource):
                def clearSuggestionFeatureConfig(
                    self,
                    *,
                    conversationProfile: str,
                    body: GoogleCloudDialogflowV2ClearSuggestionFeatureConfigRequest = ...,
                    **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudDialogflowV2ConversationProfile = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudDialogflowV2ConversationProfileHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleProtobufEmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudDialogflowV2ConversationProfileHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudDialogflowV2ListConversationProfilesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudDialogflowV2ListConversationProfilesResponseHttpRequest,
                    previous_response: GoogleCloudDialogflowV2ListConversationProfilesResponse,
                ) -> GoogleCloudDialogflowV2ListConversationProfilesResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudDialogflowV2ConversationProfile = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudDialogflowV2ConversationProfileHttpRequest: ...
                def setSuggestionFeatureConfig(
                    self,
                    *,
                    conversationProfile: str,
                    body: GoogleCloudDialogflowV2SetSuggestionFeatureConfigRequest = ...,
                    **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...

            @typing.type_check_only
            class ConversationsResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class MessagesResource(googleapiclient.discovery.Resource):
                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudDialogflowV2ListMessagesResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudDialogflowV2ListMessagesResponseHttpRequest,
                        previous_response: GoogleCloudDialogflowV2ListMessagesResponse,
                    ) -> GoogleCloudDialogflowV2ListMessagesResponseHttpRequest | None: ...

                @typing.type_check_only
                class ParticipantsResource(googleapiclient.discovery.Resource):
                    @typing.type_check_only
                    class SuggestionsResource(googleapiclient.discovery.Resource):
                        def suggestArticles(
                            self,
                            *,
                            parent: str,
                            body: GoogleCloudDialogflowV2SuggestArticlesRequest = ...,
                            **kwargs: typing.Any
                        ) -> GoogleCloudDialogflowV2SuggestArticlesResponseHttpRequest: ...
                        def suggestFaqAnswers(
                            self,
                            *,
                            parent: str,
                            body: GoogleCloudDialogflowV2SuggestFaqAnswersRequest = ...,
                            **kwargs: typing.Any
                        ) -> GoogleCloudDialogflowV2SuggestFaqAnswersResponseHttpRequest: ...
                        def suggestSmartReplies(
                            self,
                            *,
                            parent: str,
                            body: GoogleCloudDialogflowV2SuggestSmartRepliesRequest = ...,
                            **kwargs: typing.Any
                        ) -> GoogleCloudDialogflowV2SuggestSmartRepliesResponseHttpRequest: ...

                    def analyzeContent(
                        self,
                        *,
                        participant: str,
                        body: GoogleCloudDialogflowV2AnalyzeContentRequest = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudDialogflowV2AnalyzeContentResponseHttpRequest: ...
                    def create(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudDialogflowV2Participant = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudDialogflowV2ParticipantHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleCloudDialogflowV2ParticipantHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudDialogflowV2ListParticipantsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudDialogflowV2ListParticipantsResponseHttpRequest,
                        previous_response: GoogleCloudDialogflowV2ListParticipantsResponse,
                    ) -> GoogleCloudDialogflowV2ListParticipantsResponseHttpRequest | None: ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudDialogflowV2Participant = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudDialogflowV2ParticipantHttpRequest: ...
                    def suggestions(self) -> SuggestionsResource: ...

                def complete(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudDialogflowV2CompleteConversationRequest = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudDialogflowV2ConversationHttpRequest: ...
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudDialogflowV2Conversation = ...,
                    conversationId: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudDialogflowV2ConversationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudDialogflowV2ConversationHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudDialogflowV2ListConversationsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudDialogflowV2ListConversationsResponseHttpRequest,
                    previous_response: GoogleCloudDialogflowV2ListConversationsResponse,
                ) -> GoogleCloudDialogflowV2ListConversationsResponseHttpRequest | None: ...
                def messages(self) -> MessagesResource: ...
                def participants(self) -> ParticipantsResource: ...

            @typing.type_check_only
            class KnowledgeBasesResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class DocumentsResource(googleapiclient.discovery.Resource):
                    def create(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudDialogflowV2Document = ...,
                        **kwargs: typing.Any
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def export(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudDialogflowV2ExportDocumentRequest = ...,
                        **kwargs: typing.Any
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleCloudDialogflowV2DocumentHttpRequest: ...
                    def import_(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudDialogflowV2ImportDocumentsRequest = ...,
                        **kwargs: typing.Any
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudDialogflowV2ListDocumentsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudDialogflowV2ListDocumentsResponseHttpRequest,
                        previous_response: GoogleCloudDialogflowV2ListDocumentsResponse,
                    ) -> GoogleCloudDialogflowV2ListDocumentsResponseHttpRequest | None: ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudDialogflowV2Document = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def reload(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudDialogflowV2ReloadDocumentRequest = ...,
                        **kwargs: typing.Any
                    ) -> GoogleLongrunningOperationHttpRequest: ...

                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudDialogflowV2KnowledgeBase = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudDialogflowV2KnowledgeBaseHttpRequest: ...
                def delete(
                    self, *, name: str, force: bool = ..., **kwargs: typing.Any
                ) -> GoogleProtobufEmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudDialogflowV2KnowledgeBaseHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudDialogflowV2ListKnowledgeBasesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudDialogflowV2ListKnowledgeBasesResponseHttpRequest,
                    previous_response: GoogleCloudDialogflowV2ListKnowledgeBasesResponse,
                ) -> GoogleCloudDialogflowV2ListKnowledgeBasesResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudDialogflowV2KnowledgeBase = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudDialogflowV2KnowledgeBaseHttpRequest: ...
                def documents(self) -> DocumentsResource: ...

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

            def deleteAgent(
                self, *, parent: str, **kwargs: typing.Any
            ) -> GoogleProtobufEmptyHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleCloudLocationLocationHttpRequest: ...
            def getAgent(
                self, *, parent: str, **kwargs: typing.Any
            ) -> GoogleCloudDialogflowV2AgentHttpRequest: ...
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
            def setAgent(
                self,
                *,
                parent: str,
                body: GoogleCloudDialogflowV2Agent = ...,
                updateMask: str = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudDialogflowV2AgentHttpRequest: ...
            def agent(self) -> AgentResource: ...
            def answerRecords(self) -> AnswerRecordsResource: ...
            def conversationDatasets(self) -> ConversationDatasetsResource: ...
            def conversationModels(self) -> ConversationModelsResource: ...
            def conversationProfiles(self) -> ConversationProfilesResource: ...
            def conversations(self) -> ConversationsResource: ...
            def knowledgeBases(self) -> KnowledgeBasesResource: ...
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
            def list_next(
                self,
                previous_request: GoogleLongrunningListOperationsResponseHttpRequest,
                previous_response: GoogleLongrunningListOperationsResponse,
            ) -> GoogleLongrunningListOperationsResponseHttpRequest | None: ...

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
        def agent(self) -> AgentResource: ...
        def answerRecords(self) -> AnswerRecordsResource: ...
        def conversationDatasets(self) -> ConversationDatasetsResource: ...
        def conversationModels(self) -> ConversationModelsResource: ...
        def conversationProfiles(self) -> ConversationProfilesResource: ...
        def conversations(self) -> ConversationsResource: ...
        def knowledgeBases(self) -> KnowledgeBasesResource: ...
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
class GoogleCloudDialogflowV2AgentHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDialogflowV2Agent: ...

@typing.type_check_only
class GoogleCloudDialogflowV2AnalyzeContentResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDialogflowV2AnalyzeContentResponse: ...

@typing.type_check_only
class GoogleCloudDialogflowV2AnswerRecordHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDialogflowV2AnswerRecord: ...

@typing.type_check_only
class GoogleCloudDialogflowV2ContextHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDialogflowV2Context: ...

@typing.type_check_only
class GoogleCloudDialogflowV2ConversationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDialogflowV2Conversation: ...

@typing.type_check_only
class GoogleCloudDialogflowV2ConversationDatasetHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDialogflowV2ConversationDataset: ...

@typing.type_check_only
class GoogleCloudDialogflowV2ConversationModelHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDialogflowV2ConversationModel: ...

@typing.type_check_only
class GoogleCloudDialogflowV2ConversationModelEvaluationHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDialogflowV2ConversationModelEvaluation: ...

@typing.type_check_only
class GoogleCloudDialogflowV2ConversationProfileHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDialogflowV2ConversationProfile: ...

@typing.type_check_only
class GoogleCloudDialogflowV2DetectIntentResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDialogflowV2DetectIntentResponse: ...

@typing.type_check_only
class GoogleCloudDialogflowV2DocumentHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDialogflowV2Document: ...

@typing.type_check_only
class GoogleCloudDialogflowV2EntityTypeHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDialogflowV2EntityType: ...

@typing.type_check_only
class GoogleCloudDialogflowV2EnvironmentHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDialogflowV2Environment: ...

@typing.type_check_only
class GoogleCloudDialogflowV2EnvironmentHistoryHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDialogflowV2EnvironmentHistory: ...

@typing.type_check_only
class GoogleCloudDialogflowV2FulfillmentHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDialogflowV2Fulfillment: ...

@typing.type_check_only
class GoogleCloudDialogflowV2IntentHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDialogflowV2Intent: ...

@typing.type_check_only
class GoogleCloudDialogflowV2KnowledgeBaseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDialogflowV2KnowledgeBase: ...

@typing.type_check_only
class GoogleCloudDialogflowV2ListAnswerRecordsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDialogflowV2ListAnswerRecordsResponse: ...

@typing.type_check_only
class GoogleCloudDialogflowV2ListContextsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDialogflowV2ListContextsResponse: ...

@typing.type_check_only
class GoogleCloudDialogflowV2ListConversationDatasetsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDialogflowV2ListConversationDatasetsResponse: ...

@typing.type_check_only
class GoogleCloudDialogflowV2ListConversationModelEvaluationsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDialogflowV2ListConversationModelEvaluationsResponse: ...

@typing.type_check_only
class GoogleCloudDialogflowV2ListConversationModelsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDialogflowV2ListConversationModelsResponse: ...

@typing.type_check_only
class GoogleCloudDialogflowV2ListConversationProfilesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDialogflowV2ListConversationProfilesResponse: ...

@typing.type_check_only
class GoogleCloudDialogflowV2ListConversationsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDialogflowV2ListConversationsResponse: ...

@typing.type_check_only
class GoogleCloudDialogflowV2ListDocumentsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDialogflowV2ListDocumentsResponse: ...

@typing.type_check_only
class GoogleCloudDialogflowV2ListEntityTypesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDialogflowV2ListEntityTypesResponse: ...

@typing.type_check_only
class GoogleCloudDialogflowV2ListEnvironmentsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDialogflowV2ListEnvironmentsResponse: ...

@typing.type_check_only
class GoogleCloudDialogflowV2ListIntentsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDialogflowV2ListIntentsResponse: ...

@typing.type_check_only
class GoogleCloudDialogflowV2ListKnowledgeBasesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDialogflowV2ListKnowledgeBasesResponse: ...

@typing.type_check_only
class GoogleCloudDialogflowV2ListMessagesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDialogflowV2ListMessagesResponse: ...

@typing.type_check_only
class GoogleCloudDialogflowV2ListParticipantsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDialogflowV2ListParticipantsResponse: ...

@typing.type_check_only
class GoogleCloudDialogflowV2ListSessionEntityTypesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDialogflowV2ListSessionEntityTypesResponse: ...

@typing.type_check_only
class GoogleCloudDialogflowV2ListVersionsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDialogflowV2ListVersionsResponse: ...

@typing.type_check_only
class GoogleCloudDialogflowV2ParticipantHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDialogflowV2Participant: ...

@typing.type_check_only
class GoogleCloudDialogflowV2SearchAgentsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDialogflowV2SearchAgentsResponse: ...

@typing.type_check_only
class GoogleCloudDialogflowV2SessionEntityTypeHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDialogflowV2SessionEntityType: ...

@typing.type_check_only
class GoogleCloudDialogflowV2SuggestArticlesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDialogflowV2SuggestArticlesResponse: ...

@typing.type_check_only
class GoogleCloudDialogflowV2SuggestFaqAnswersResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDialogflowV2SuggestFaqAnswersResponse: ...

@typing.type_check_only
class GoogleCloudDialogflowV2SuggestSmartRepliesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDialogflowV2SuggestSmartRepliesResponse: ...

@typing.type_check_only
class GoogleCloudDialogflowV2ValidationResultHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDialogflowV2ValidationResult: ...

@typing.type_check_only
class GoogleCloudDialogflowV2VersionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDialogflowV2Version: ...

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
