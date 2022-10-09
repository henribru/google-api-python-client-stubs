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
                        body: GoogleCloudDialogflowV2beta1BatchCreateEntitiesRequest = ...,
                        **kwargs: typing.Any
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def batchDelete(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudDialogflowV2beta1BatchDeleteEntitiesRequest = ...,
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
                def batchUpdate(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudDialogflowV2beta1BatchUpdateEntityTypesRequest = ...,
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
                    self, *, name: str, languageCode: str = ..., **kwargs: typing.Any
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
                def list_next(
                    self,
                    previous_request: GoogleCloudDialogflowV2beta1ListEntityTypesResponseHttpRequest,
                    previous_response: GoogleCloudDialogflowV2beta1ListEntityTypesResponse,
                ) -> GoogleCloudDialogflowV2beta1ListEntityTypesResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudDialogflowV2beta1EntityType = ...,
                    languageCode: str = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudDialogflowV2beta1EntityTypeHttpRequest: ...
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
                    ) -> GoogleCloudDialogflowV2beta1ListIntentsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudDialogflowV2beta1ListIntentsResponseHttpRequest,
                        previous_response: GoogleCloudDialogflowV2beta1ListIntentsResponse,
                    ) -> GoogleCloudDialogflowV2beta1ListIntentsResponseHttpRequest | None: ...

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
                                body: GoogleCloudDialogflowV2beta1Context = ...,
                                **kwargs: typing.Any
                            ) -> GoogleCloudDialogflowV2beta1ContextHttpRequest: ...
                            def delete(
                                self, *, name: str, **kwargs: typing.Any
                            ) -> GoogleProtobufEmptyHttpRequest: ...
                            def get(
                                self, *, name: str, **kwargs: typing.Any
                            ) -> GoogleCloudDialogflowV2beta1ContextHttpRequest: ...
                            def list(
                                self,
                                *,
                                parent: str,
                                pageSize: int = ...,
                                pageToken: str = ...,
                                **kwargs: typing.Any
                            ) -> GoogleCloudDialogflowV2beta1ListContextsResponseHttpRequest: ...
                            def list_next(
                                self,
                                previous_request: GoogleCloudDialogflowV2beta1ListContextsResponseHttpRequest,
                                previous_response: GoogleCloudDialogflowV2beta1ListContextsResponse,
                            ) -> GoogleCloudDialogflowV2beta1ListContextsResponseHttpRequest | None: ...
                            def patch(
                                self,
                                *,
                                name: str,
                                body: GoogleCloudDialogflowV2beta1Context = ...,
                                updateMask: str = ...,
                                **kwargs: typing.Any
                            ) -> GoogleCloudDialogflowV2beta1ContextHttpRequest: ...

                        @typing.type_check_only
                        class EntityTypesResource(googleapiclient.discovery.Resource):
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
                            def list_next(
                                self,
                                previous_request: GoogleCloudDialogflowV2beta1ListSessionEntityTypesResponseHttpRequest,
                                previous_response: GoogleCloudDialogflowV2beta1ListSessionEntityTypesResponse,
                            ) -> GoogleCloudDialogflowV2beta1ListSessionEntityTypesResponseHttpRequest | None: ...
                            def patch(
                                self,
                                *,
                                name: str,
                                body: GoogleCloudDialogflowV2beta1SessionEntityType = ...,
                                updateMask: str = ...,
                                **kwargs: typing.Any
                            ) -> GoogleCloudDialogflowV2beta1SessionEntityTypeHttpRequest: ...

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
                        def contexts(self) -> ContextsResource: ...
                        def entityTypes(self) -> EntityTypesResource: ...

                    def sessions(self) -> SessionsResource: ...

                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudDialogflowV2beta1Environment = ...,
                    environmentId: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudDialogflowV2beta1EnvironmentHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleProtobufEmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudDialogflowV2beta1EnvironmentHttpRequest: ...
                def getHistory(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudDialogflowV2beta1EnvironmentHistoryHttpRequest: ...
                def getHistory_next(
                    self,
                    previous_request: GoogleCloudDialogflowV2beta1EnvironmentHistoryHttpRequest,
                    previous_response: GoogleCloudDialogflowV2beta1EnvironmentHistory,
                ) -> GoogleCloudDialogflowV2beta1EnvironmentHistoryHttpRequest | None: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudDialogflowV2beta1ListEnvironmentsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudDialogflowV2beta1ListEnvironmentsResponseHttpRequest,
                    previous_response: GoogleCloudDialogflowV2beta1ListEnvironmentsResponse,
                ) -> GoogleCloudDialogflowV2beta1ListEnvironmentsResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudDialogflowV2beta1Environment = ...,
                    allowLoadToDraftAndDiscardChanges: bool = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudDialogflowV2beta1EnvironmentHttpRequest: ...
                def intents(self) -> IntentsResource: ...
                def users(self) -> UsersResource: ...

            @typing.type_check_only
            class IntentsResource(googleapiclient.discovery.Resource):
                def batchDelete(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudDialogflowV2beta1BatchDeleteIntentsRequest = ...,
                    **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
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
                def get(
                    self,
                    *,
                    name: str,
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
                    intentView: typing_extensions.Literal[
                        "INTENT_VIEW_UNSPECIFIED", "INTENT_VIEW_FULL"
                    ] = ...,
                    languageCode: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudDialogflowV2beta1ListIntentsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudDialogflowV2beta1ListIntentsResponseHttpRequest,
                    previous_response: GoogleCloudDialogflowV2beta1ListIntentsResponse,
                ) -> GoogleCloudDialogflowV2beta1ListIntentsResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudDialogflowV2beta1Intent = ...,
                    intentView: typing_extensions.Literal[
                        "INTENT_VIEW_UNSPECIFIED", "INTENT_VIEW_FULL"
                    ] = ...,
                    languageCode: str = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudDialogflowV2beta1IntentHttpRequest: ...

            @typing.type_check_only
            class KnowledgeBasesResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class DocumentsResource(googleapiclient.discovery.Resource):
                    def create(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudDialogflowV2beta1Document = ...,
                        importGcsCustomMetadata: bool = ...,
                        **kwargs: typing.Any
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleCloudDialogflowV2beta1DocumentHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudDialogflowV2beta1ListDocumentsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudDialogflowV2beta1ListDocumentsResponseHttpRequest,
                        previous_response: GoogleCloudDialogflowV2beta1ListDocumentsResponse,
                    ) -> GoogleCloudDialogflowV2beta1ListDocumentsResponseHttpRequest | None: ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudDialogflowV2beta1Document = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def reload(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudDialogflowV2beta1ReloadDocumentRequest = ...,
                        **kwargs: typing.Any
                    ) -> GoogleLongrunningOperationHttpRequest: ...

                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudDialogflowV2beta1KnowledgeBase = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudDialogflowV2beta1KnowledgeBaseHttpRequest: ...
                def delete(
                    self, *, name: str, force: bool = ..., **kwargs: typing.Any
                ) -> GoogleProtobufEmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudDialogflowV2beta1KnowledgeBaseHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudDialogflowV2beta1ListKnowledgeBasesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudDialogflowV2beta1ListKnowledgeBasesResponseHttpRequest,
                    previous_response: GoogleCloudDialogflowV2beta1ListKnowledgeBasesResponse,
                ) -> GoogleCloudDialogflowV2beta1ListKnowledgeBasesResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudDialogflowV2beta1KnowledgeBase = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudDialogflowV2beta1KnowledgeBaseHttpRequest: ...
                def documents(self) -> DocumentsResource: ...

            @typing.type_check_only
            class SessionsResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
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
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleCloudDialogflowV2beta1ContextHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudDialogflowV2beta1ListContextsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudDialogflowV2beta1ListContextsResponseHttpRequest,
                        previous_response: GoogleCloudDialogflowV2beta1ListContextsResponse,
                    ) -> GoogleCloudDialogflowV2beta1ListContextsResponseHttpRequest | None: ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudDialogflowV2beta1Context = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudDialogflowV2beta1ContextHttpRequest: ...

                @typing.type_check_only
                class EntityTypesResource(googleapiclient.discovery.Resource):
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
                    def list_next(
                        self,
                        previous_request: GoogleCloudDialogflowV2beta1ListSessionEntityTypesResponseHttpRequest,
                        previous_response: GoogleCloudDialogflowV2beta1ListSessionEntityTypesResponse,
                    ) -> GoogleCloudDialogflowV2beta1ListSessionEntityTypesResponseHttpRequest | None: ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudDialogflowV2beta1SessionEntityType = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudDialogflowV2beta1SessionEntityTypeHttpRequest: ...

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
                def contexts(self) -> ContextsResource: ...
                def entityTypes(self) -> EntityTypesResource: ...

            @typing.type_check_only
            class VersionsResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudDialogflowV2beta1Version = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudDialogflowV2beta1VersionHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleProtobufEmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudDialogflowV2beta1VersionHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudDialogflowV2beta1ListVersionsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudDialogflowV2beta1ListVersionsResponseHttpRequest,
                    previous_response: GoogleCloudDialogflowV2beta1ListVersionsResponse,
                ) -> GoogleCloudDialogflowV2beta1ListVersionsResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudDialogflowV2beta1Version = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudDialogflowV2beta1VersionHttpRequest: ...

            def export(
                self,
                *,
                parent: str,
                body: GoogleCloudDialogflowV2beta1ExportAgentRequest = ...,
                **kwargs: typing.Any
            ) -> GoogleLongrunningOperationHttpRequest: ...
            def getFulfillment(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleCloudDialogflowV2beta1FulfillmentHttpRequest: ...
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
            def restore(
                self,
                *,
                parent: str,
                body: GoogleCloudDialogflowV2beta1RestoreAgentRequest = ...,
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
            def search_next(
                self,
                previous_request: GoogleCloudDialogflowV2beta1SearchAgentsResponseHttpRequest,
                previous_response: GoogleCloudDialogflowV2beta1SearchAgentsResponse,
            ) -> GoogleCloudDialogflowV2beta1SearchAgentsResponseHttpRequest | None: ...
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
            def environments(self) -> EnvironmentsResource: ...
            def intents(self) -> IntentsResource: ...
            def knowledgeBases(self) -> KnowledgeBasesResource: ...
            def sessions(self) -> SessionsResource: ...
            def versions(self) -> VersionsResource: ...

        @typing.type_check_only
        class AnswerRecordsResource(googleapiclient.discovery.Resource):
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleCloudDialogflowV2beta1AnswerRecordHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                filter: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudDialogflowV2beta1ListAnswerRecordsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: GoogleCloudDialogflowV2beta1ListAnswerRecordsResponseHttpRequest,
                previous_response: GoogleCloudDialogflowV2beta1ListAnswerRecordsResponse,
            ) -> GoogleCloudDialogflowV2beta1ListAnswerRecordsResponseHttpRequest | None: ...
            def patch(
                self,
                *,
                name: str,
                body: GoogleCloudDialogflowV2beta1AnswerRecord = ...,
                updateMask: str = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudDialogflowV2beta1AnswerRecordHttpRequest: ...

        @typing.type_check_only
        class ConversationProfilesResource(googleapiclient.discovery.Resource):
            def clearSuggestionFeatureConfig(
                self,
                *,
                conversationProfile: str,
                body: GoogleCloudDialogflowV2beta1ClearSuggestionFeatureConfigRequest = ...,
                **kwargs: typing.Any
            ) -> GoogleLongrunningOperationHttpRequest: ...
            def create(
                self,
                *,
                parent: str,
                body: GoogleCloudDialogflowV2beta1ConversationProfile = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudDialogflowV2beta1ConversationProfileHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleProtobufEmptyHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleCloudDialogflowV2beta1ConversationProfileHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudDialogflowV2beta1ListConversationProfilesResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: GoogleCloudDialogflowV2beta1ListConversationProfilesResponseHttpRequest,
                previous_response: GoogleCloudDialogflowV2beta1ListConversationProfilesResponse,
            ) -> GoogleCloudDialogflowV2beta1ListConversationProfilesResponseHttpRequest | None: ...
            def patch(
                self,
                *,
                name: str,
                body: GoogleCloudDialogflowV2beta1ConversationProfile = ...,
                updateMask: str = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudDialogflowV2beta1ConversationProfileHttpRequest: ...
            def setSuggestionFeatureConfig(
                self,
                *,
                conversationProfile: str,
                body: GoogleCloudDialogflowV2beta1SetSuggestionFeatureConfigRequest = ...,
                **kwargs: typing.Any
            ) -> GoogleLongrunningOperationHttpRequest: ...

        @typing.type_check_only
        class ConversationsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class MessagesResource(googleapiclient.discovery.Resource):
                def batchCreate(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudDialogflowV2beta1BatchCreateMessagesRequest = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudDialogflowV2beta1BatchCreateMessagesResponseHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudDialogflowV2beta1ListMessagesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudDialogflowV2beta1ListMessagesResponseHttpRequest,
                    previous_response: GoogleCloudDialogflowV2beta1ListMessagesResponse,
                ) -> GoogleCloudDialogflowV2beta1ListMessagesResponseHttpRequest | None: ...

            @typing.type_check_only
            class ParticipantsResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class SuggestionsResource(googleapiclient.discovery.Resource):
                    def compile(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudDialogflowV2beta1CompileSuggestionRequest = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudDialogflowV2beta1CompileSuggestionResponseHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudDialogflowV2beta1ListSuggestionsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudDialogflowV2beta1ListSuggestionsResponseHttpRequest,
                        previous_response: GoogleCloudDialogflowV2beta1ListSuggestionsResponse,
                    ) -> GoogleCloudDialogflowV2beta1ListSuggestionsResponseHttpRequest | None: ...
                    def suggestArticles(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudDialogflowV2beta1SuggestArticlesRequest = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudDialogflowV2beta1SuggestArticlesResponseHttpRequest: ...
                    def suggestFaqAnswers(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudDialogflowV2beta1SuggestFaqAnswersRequest = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudDialogflowV2beta1SuggestFaqAnswersResponseHttpRequest: ...
                    def suggestSmartReplies(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudDialogflowV2beta1SuggestSmartRepliesRequest = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudDialogflowV2beta1SuggestSmartRepliesResponseHttpRequest: ...

                def analyzeContent(
                    self,
                    *,
                    participant: str,
                    body: GoogleCloudDialogflowV2beta1AnalyzeContentRequest = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudDialogflowV2beta1AnalyzeContentResponseHttpRequest: ...
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudDialogflowV2beta1Participant = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudDialogflowV2beta1ParticipantHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudDialogflowV2beta1ParticipantHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudDialogflowV2beta1ListParticipantsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudDialogflowV2beta1ListParticipantsResponseHttpRequest,
                    previous_response: GoogleCloudDialogflowV2beta1ListParticipantsResponse,
                ) -> GoogleCloudDialogflowV2beta1ListParticipantsResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudDialogflowV2beta1Participant = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudDialogflowV2beta1ParticipantHttpRequest: ...
                def suggestions(self) -> SuggestionsResource: ...

            @typing.type_check_only
            class SuggestionsResource(googleapiclient.discovery.Resource):
                def suggestConversationSummary(
                    self,
                    *,
                    conversation: str,
                    body: GoogleCloudDialogflowV2beta1SuggestConversationSummaryRequest = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudDialogflowV2beta1SuggestConversationSummaryResponseHttpRequest: ...

            def complete(
                self,
                *,
                name: str,
                body: GoogleCloudDialogflowV2beta1CompleteConversationRequest = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudDialogflowV2beta1ConversationHttpRequest: ...
            def create(
                self,
                *,
                parent: str,
                body: GoogleCloudDialogflowV2beta1Conversation = ...,
                conversationId: str = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudDialogflowV2beta1ConversationHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleCloudDialogflowV2beta1ConversationHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                filter: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudDialogflowV2beta1ListConversationsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: GoogleCloudDialogflowV2beta1ListConversationsResponseHttpRequest,
                previous_response: GoogleCloudDialogflowV2beta1ListConversationsResponse,
            ) -> GoogleCloudDialogflowV2beta1ListConversationsResponseHttpRequest | None: ...
            def messages(self) -> MessagesResource: ...
            def participants(self) -> ParticipantsResource: ...
            def suggestions(self) -> SuggestionsResource: ...

        @typing.type_check_only
        class KnowledgeBasesResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class DocumentsResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudDialogflowV2beta1Document = ...,
                    importGcsCustomMetadata: bool = ...,
                    **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudDialogflowV2beta1DocumentHttpRequest: ...
                def import_(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudDialogflowV2beta1ImportDocumentsRequest = ...,
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
                ) -> GoogleCloudDialogflowV2beta1ListDocumentsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudDialogflowV2beta1ListDocumentsResponseHttpRequest,
                    previous_response: GoogleCloudDialogflowV2beta1ListDocumentsResponse,
                ) -> GoogleCloudDialogflowV2beta1ListDocumentsResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudDialogflowV2beta1Document = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def reload(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudDialogflowV2beta1ReloadDocumentRequest = ...,
                    **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...

            def create(
                self,
                *,
                parent: str,
                body: GoogleCloudDialogflowV2beta1KnowledgeBase = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudDialogflowV2beta1KnowledgeBaseHttpRequest: ...
            def delete(
                self, *, name: str, force: bool = ..., **kwargs: typing.Any
            ) -> GoogleProtobufEmptyHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleCloudDialogflowV2beta1KnowledgeBaseHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                filter: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudDialogflowV2beta1ListKnowledgeBasesResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: GoogleCloudDialogflowV2beta1ListKnowledgeBasesResponseHttpRequest,
                previous_response: GoogleCloudDialogflowV2beta1ListKnowledgeBasesResponse,
            ) -> GoogleCloudDialogflowV2beta1ListKnowledgeBasesResponseHttpRequest | None: ...
            def patch(
                self,
                *,
                name: str,
                body: GoogleCloudDialogflowV2beta1KnowledgeBase = ...,
                updateMask: str = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudDialogflowV2beta1KnowledgeBaseHttpRequest: ...
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
                            body: GoogleCloudDialogflowV2beta1BatchCreateEntitiesRequest = ...,
                            **kwargs: typing.Any
                        ) -> GoogleLongrunningOperationHttpRequest: ...
                        def batchDelete(
                            self,
                            *,
                            parent: str,
                            body: GoogleCloudDialogflowV2beta1BatchDeleteEntitiesRequest = ...,
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
                    def batchUpdate(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudDialogflowV2beta1BatchUpdateEntityTypesRequest = ...,
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
                    def list(
                        self,
                        *,
                        parent: str,
                        languageCode: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudDialogflowV2beta1ListEntityTypesResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudDialogflowV2beta1ListEntityTypesResponseHttpRequest,
                        previous_response: GoogleCloudDialogflowV2beta1ListEntityTypesResponse,
                    ) -> GoogleCloudDialogflowV2beta1ListEntityTypesResponseHttpRequest | None: ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudDialogflowV2beta1EntityType = ...,
                        languageCode: str = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudDialogflowV2beta1EntityTypeHttpRequest: ...
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
                        ) -> GoogleCloudDialogflowV2beta1ListIntentsResponseHttpRequest: ...
                        def list_next(
                            self,
                            previous_request: GoogleCloudDialogflowV2beta1ListIntentsResponseHttpRequest,
                            previous_response: GoogleCloudDialogflowV2beta1ListIntentsResponse,
                        ) -> GoogleCloudDialogflowV2beta1ListIntentsResponseHttpRequest | None: ...

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
                                    body: GoogleCloudDialogflowV2beta1Context = ...,
                                    **kwargs: typing.Any
                                ) -> GoogleCloudDialogflowV2beta1ContextHttpRequest: ...
                                def delete(
                                    self, *, name: str, **kwargs: typing.Any
                                ) -> GoogleProtobufEmptyHttpRequest: ...
                                def get(
                                    self, *, name: str, **kwargs: typing.Any
                                ) -> GoogleCloudDialogflowV2beta1ContextHttpRequest: ...
                                def list(
                                    self,
                                    *,
                                    parent: str,
                                    pageSize: int = ...,
                                    pageToken: str = ...,
                                    **kwargs: typing.Any
                                ) -> GoogleCloudDialogflowV2beta1ListContextsResponseHttpRequest: ...
                                def list_next(
                                    self,
                                    previous_request: GoogleCloudDialogflowV2beta1ListContextsResponseHttpRequest,
                                    previous_response: GoogleCloudDialogflowV2beta1ListContextsResponse,
                                ) -> GoogleCloudDialogflowV2beta1ListContextsResponseHttpRequest | None: ...
                                def patch(
                                    self,
                                    *,
                                    name: str,
                                    body: GoogleCloudDialogflowV2beta1Context = ...,
                                    updateMask: str = ...,
                                    **kwargs: typing.Any
                                ) -> GoogleCloudDialogflowV2beta1ContextHttpRequest: ...

                            @typing.type_check_only
                            class EntityTypesResource(
                                googleapiclient.discovery.Resource
                            ):
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
                                def list_next(
                                    self,
                                    previous_request: GoogleCloudDialogflowV2beta1ListSessionEntityTypesResponseHttpRequest,
                                    previous_response: GoogleCloudDialogflowV2beta1ListSessionEntityTypesResponse,
                                ) -> GoogleCloudDialogflowV2beta1ListSessionEntityTypesResponseHttpRequest | None: ...
                                def patch(
                                    self,
                                    *,
                                    name: str,
                                    body: GoogleCloudDialogflowV2beta1SessionEntityType = ...,
                                    updateMask: str = ...,
                                    **kwargs: typing.Any
                                ) -> GoogleCloudDialogflowV2beta1SessionEntityTypeHttpRequest: ...

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
                            def contexts(self) -> ContextsResource: ...
                            def entityTypes(self) -> EntityTypesResource: ...

                        def sessions(self) -> SessionsResource: ...

                    def create(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudDialogflowV2beta1Environment = ...,
                        environmentId: str = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudDialogflowV2beta1EnvironmentHttpRequest: ...
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleProtobufEmptyHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleCloudDialogflowV2beta1EnvironmentHttpRequest: ...
                    def getHistory(
                        self,
                        *,
                        parent: str,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudDialogflowV2beta1EnvironmentHistoryHttpRequest: ...
                    def getHistory_next(
                        self,
                        previous_request: GoogleCloudDialogflowV2beta1EnvironmentHistoryHttpRequest,
                        previous_response: GoogleCloudDialogflowV2beta1EnvironmentHistory,
                    ) -> GoogleCloudDialogflowV2beta1EnvironmentHistoryHttpRequest | None: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudDialogflowV2beta1ListEnvironmentsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudDialogflowV2beta1ListEnvironmentsResponseHttpRequest,
                        previous_response: GoogleCloudDialogflowV2beta1ListEnvironmentsResponse,
                    ) -> GoogleCloudDialogflowV2beta1ListEnvironmentsResponseHttpRequest | None: ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudDialogflowV2beta1Environment = ...,
                        allowLoadToDraftAndDiscardChanges: bool = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudDialogflowV2beta1EnvironmentHttpRequest: ...
                    def intents(self) -> IntentsResource: ...
                    def users(self) -> UsersResource: ...

                @typing.type_check_only
                class IntentsResource(googleapiclient.discovery.Resource):
                    def batchDelete(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudDialogflowV2beta1BatchDeleteIntentsRequest = ...,
                        **kwargs: typing.Any
                    ) -> GoogleLongrunningOperationHttpRequest: ...
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
                    def get(
                        self,
                        *,
                        name: str,
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
                        intentView: typing_extensions.Literal[
                            "INTENT_VIEW_UNSPECIFIED", "INTENT_VIEW_FULL"
                        ] = ...,
                        languageCode: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudDialogflowV2beta1ListIntentsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudDialogflowV2beta1ListIntentsResponseHttpRequest,
                        previous_response: GoogleCloudDialogflowV2beta1ListIntentsResponse,
                    ) -> GoogleCloudDialogflowV2beta1ListIntentsResponseHttpRequest | None: ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudDialogflowV2beta1Intent = ...,
                        intentView: typing_extensions.Literal[
                            "INTENT_VIEW_UNSPECIFIED", "INTENT_VIEW_FULL"
                        ] = ...,
                        languageCode: str = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudDialogflowV2beta1IntentHttpRequest: ...

                @typing.type_check_only
                class SessionsResource(googleapiclient.discovery.Resource):
                    @typing.type_check_only
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
                        def get(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> GoogleCloudDialogflowV2beta1ContextHttpRequest: ...
                        def list(
                            self,
                            *,
                            parent: str,
                            pageSize: int = ...,
                            pageToken: str = ...,
                            **kwargs: typing.Any
                        ) -> GoogleCloudDialogflowV2beta1ListContextsResponseHttpRequest: ...
                        def list_next(
                            self,
                            previous_request: GoogleCloudDialogflowV2beta1ListContextsResponseHttpRequest,
                            previous_response: GoogleCloudDialogflowV2beta1ListContextsResponse,
                        ) -> GoogleCloudDialogflowV2beta1ListContextsResponseHttpRequest | None: ...
                        def patch(
                            self,
                            *,
                            name: str,
                            body: GoogleCloudDialogflowV2beta1Context = ...,
                            updateMask: str = ...,
                            **kwargs: typing.Any
                        ) -> GoogleCloudDialogflowV2beta1ContextHttpRequest: ...

                    @typing.type_check_only
                    class EntityTypesResource(googleapiclient.discovery.Resource):
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
                        def list_next(
                            self,
                            previous_request: GoogleCloudDialogflowV2beta1ListSessionEntityTypesResponseHttpRequest,
                            previous_response: GoogleCloudDialogflowV2beta1ListSessionEntityTypesResponse,
                        ) -> GoogleCloudDialogflowV2beta1ListSessionEntityTypesResponseHttpRequest | None: ...
                        def patch(
                            self,
                            *,
                            name: str,
                            body: GoogleCloudDialogflowV2beta1SessionEntityType = ...,
                            updateMask: str = ...,
                            **kwargs: typing.Any
                        ) -> GoogleCloudDialogflowV2beta1SessionEntityTypeHttpRequest: ...

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
                    def contexts(self) -> ContextsResource: ...
                    def entityTypes(self) -> EntityTypesResource: ...

                @typing.type_check_only
                class VersionsResource(googleapiclient.discovery.Resource):
                    def create(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudDialogflowV2beta1Version = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudDialogflowV2beta1VersionHttpRequest: ...
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleProtobufEmptyHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleCloudDialogflowV2beta1VersionHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudDialogflowV2beta1ListVersionsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudDialogflowV2beta1ListVersionsResponseHttpRequest,
                        previous_response: GoogleCloudDialogflowV2beta1ListVersionsResponse,
                    ) -> GoogleCloudDialogflowV2beta1ListVersionsResponseHttpRequest | None: ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudDialogflowV2beta1Version = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudDialogflowV2beta1VersionHttpRequest: ...

                def export(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudDialogflowV2beta1ExportAgentRequest = ...,
                    **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def getFulfillment(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudDialogflowV2beta1FulfillmentHttpRequest: ...
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
                def restore(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudDialogflowV2beta1RestoreAgentRequest = ...,
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
                def search_next(
                    self,
                    previous_request: GoogleCloudDialogflowV2beta1SearchAgentsResponseHttpRequest,
                    previous_response: GoogleCloudDialogflowV2beta1SearchAgentsResponse,
                ) -> GoogleCloudDialogflowV2beta1SearchAgentsResponseHttpRequest | None: ...
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
                def environments(self) -> EnvironmentsResource: ...
                def intents(self) -> IntentsResource: ...
                def sessions(self) -> SessionsResource: ...
                def versions(self) -> VersionsResource: ...

            @typing.type_check_only
            class AnswerRecordsResource(googleapiclient.discovery.Resource):
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudDialogflowV2beta1AnswerRecordHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudDialogflowV2beta1ListAnswerRecordsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudDialogflowV2beta1ListAnswerRecordsResponseHttpRequest,
                    previous_response: GoogleCloudDialogflowV2beta1ListAnswerRecordsResponse,
                ) -> GoogleCloudDialogflowV2beta1ListAnswerRecordsResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudDialogflowV2beta1AnswerRecord = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudDialogflowV2beta1AnswerRecordHttpRequest: ...

            @typing.type_check_only
            class ConversationProfilesResource(googleapiclient.discovery.Resource):
                def clearSuggestionFeatureConfig(
                    self,
                    *,
                    conversationProfile: str,
                    body: GoogleCloudDialogflowV2beta1ClearSuggestionFeatureConfigRequest = ...,
                    **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudDialogflowV2beta1ConversationProfile = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudDialogflowV2beta1ConversationProfileHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleProtobufEmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudDialogflowV2beta1ConversationProfileHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudDialogflowV2beta1ListConversationProfilesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudDialogflowV2beta1ListConversationProfilesResponseHttpRequest,
                    previous_response: GoogleCloudDialogflowV2beta1ListConversationProfilesResponse,
                ) -> GoogleCloudDialogflowV2beta1ListConversationProfilesResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudDialogflowV2beta1ConversationProfile = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudDialogflowV2beta1ConversationProfileHttpRequest: ...
                def setSuggestionFeatureConfig(
                    self,
                    *,
                    conversationProfile: str,
                    body: GoogleCloudDialogflowV2beta1SetSuggestionFeatureConfigRequest = ...,
                    **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...

            @typing.type_check_only
            class ConversationsResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class MessagesResource(googleapiclient.discovery.Resource):
                    def batchCreate(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudDialogflowV2beta1BatchCreateMessagesRequest = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudDialogflowV2beta1BatchCreateMessagesResponseHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudDialogflowV2beta1ListMessagesResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudDialogflowV2beta1ListMessagesResponseHttpRequest,
                        previous_response: GoogleCloudDialogflowV2beta1ListMessagesResponse,
                    ) -> GoogleCloudDialogflowV2beta1ListMessagesResponseHttpRequest | None: ...

                @typing.type_check_only
                class ParticipantsResource(googleapiclient.discovery.Resource):
                    @typing.type_check_only
                    class SuggestionsResource(googleapiclient.discovery.Resource):
                        def suggestArticles(
                            self,
                            *,
                            parent: str,
                            body: GoogleCloudDialogflowV2beta1SuggestArticlesRequest = ...,
                            **kwargs: typing.Any
                        ) -> GoogleCloudDialogflowV2beta1SuggestArticlesResponseHttpRequest: ...
                        def suggestFaqAnswers(
                            self,
                            *,
                            parent: str,
                            body: GoogleCloudDialogflowV2beta1SuggestFaqAnswersRequest = ...,
                            **kwargs: typing.Any
                        ) -> GoogleCloudDialogflowV2beta1SuggestFaqAnswersResponseHttpRequest: ...
                        def suggestSmartReplies(
                            self,
                            *,
                            parent: str,
                            body: GoogleCloudDialogflowV2beta1SuggestSmartRepliesRequest = ...,
                            **kwargs: typing.Any
                        ) -> GoogleCloudDialogflowV2beta1SuggestSmartRepliesResponseHttpRequest: ...

                    def analyzeContent(
                        self,
                        *,
                        participant: str,
                        body: GoogleCloudDialogflowV2beta1AnalyzeContentRequest = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudDialogflowV2beta1AnalyzeContentResponseHttpRequest: ...
                    def create(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudDialogflowV2beta1Participant = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudDialogflowV2beta1ParticipantHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleCloudDialogflowV2beta1ParticipantHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudDialogflowV2beta1ListParticipantsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudDialogflowV2beta1ListParticipantsResponseHttpRequest,
                        previous_response: GoogleCloudDialogflowV2beta1ListParticipantsResponse,
                    ) -> GoogleCloudDialogflowV2beta1ListParticipantsResponseHttpRequest | None: ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudDialogflowV2beta1Participant = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudDialogflowV2beta1ParticipantHttpRequest: ...
                    def suggestions(self) -> SuggestionsResource: ...

                @typing.type_check_only
                class SuggestionsResource(googleapiclient.discovery.Resource):
                    def suggestConversationSummary(
                        self,
                        *,
                        conversation: str,
                        body: GoogleCloudDialogflowV2beta1SuggestConversationSummaryRequest = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudDialogflowV2beta1SuggestConversationSummaryResponseHttpRequest: ...

                def complete(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudDialogflowV2beta1CompleteConversationRequest = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudDialogflowV2beta1ConversationHttpRequest: ...
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudDialogflowV2beta1Conversation = ...,
                    conversationId: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudDialogflowV2beta1ConversationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudDialogflowV2beta1ConversationHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudDialogflowV2beta1ListConversationsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudDialogflowV2beta1ListConversationsResponseHttpRequest,
                    previous_response: GoogleCloudDialogflowV2beta1ListConversationsResponse,
                ) -> GoogleCloudDialogflowV2beta1ListConversationsResponseHttpRequest | None: ...
                def messages(self) -> MessagesResource: ...
                def participants(self) -> ParticipantsResource: ...
                def suggestions(self) -> SuggestionsResource: ...

            @typing.type_check_only
            class KnowledgeBasesResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class DocumentsResource(googleapiclient.discovery.Resource):
                    def create(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudDialogflowV2beta1Document = ...,
                        importGcsCustomMetadata: bool = ...,
                        **kwargs: typing.Any
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleCloudDialogflowV2beta1DocumentHttpRequest: ...
                    def import_(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudDialogflowV2beta1ImportDocumentsRequest = ...,
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
                    ) -> GoogleCloudDialogflowV2beta1ListDocumentsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudDialogflowV2beta1ListDocumentsResponseHttpRequest,
                        previous_response: GoogleCloudDialogflowV2beta1ListDocumentsResponse,
                    ) -> GoogleCloudDialogflowV2beta1ListDocumentsResponseHttpRequest | None: ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudDialogflowV2beta1Document = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def reload(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudDialogflowV2beta1ReloadDocumentRequest = ...,
                        **kwargs: typing.Any
                    ) -> GoogleLongrunningOperationHttpRequest: ...

                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudDialogflowV2beta1KnowledgeBase = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudDialogflowV2beta1KnowledgeBaseHttpRequest: ...
                def delete(
                    self, *, name: str, force: bool = ..., **kwargs: typing.Any
                ) -> GoogleProtobufEmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudDialogflowV2beta1KnowledgeBaseHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudDialogflowV2beta1ListKnowledgeBasesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudDialogflowV2beta1ListKnowledgeBasesResponseHttpRequest,
                    previous_response: GoogleCloudDialogflowV2beta1ListKnowledgeBasesResponse,
                ) -> GoogleCloudDialogflowV2beta1ListKnowledgeBasesResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudDialogflowV2beta1KnowledgeBase = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudDialogflowV2beta1KnowledgeBaseHttpRequest: ...
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
            ) -> GoogleCloudDialogflowV2beta1AgentHttpRequest: ...
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
                body: GoogleCloudDialogflowV2beta1Agent = ...,
                updateMask: str = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudDialogflowV2beta1AgentHttpRequest: ...
            def agent(self) -> AgentResource: ...
            def answerRecords(self) -> AnswerRecordsResource: ...
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
        def answerRecords(self) -> AnswerRecordsResource: ...
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
class GoogleCloudDialogflowV2beta1AgentHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDialogflowV2beta1Agent: ...

@typing.type_check_only
class GoogleCloudDialogflowV2beta1AnalyzeContentResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDialogflowV2beta1AnalyzeContentResponse: ...

@typing.type_check_only
class GoogleCloudDialogflowV2beta1AnswerRecordHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDialogflowV2beta1AnswerRecord: ...

@typing.type_check_only
class GoogleCloudDialogflowV2beta1BatchCreateMessagesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDialogflowV2beta1BatchCreateMessagesResponse: ...

@typing.type_check_only
class GoogleCloudDialogflowV2beta1CompileSuggestionResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDialogflowV2beta1CompileSuggestionResponse: ...

@typing.type_check_only
class GoogleCloudDialogflowV2beta1ContextHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDialogflowV2beta1Context: ...

@typing.type_check_only
class GoogleCloudDialogflowV2beta1ConversationHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDialogflowV2beta1Conversation: ...

@typing.type_check_only
class GoogleCloudDialogflowV2beta1ConversationProfileHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDialogflowV2beta1ConversationProfile: ...

@typing.type_check_only
class GoogleCloudDialogflowV2beta1DetectIntentResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDialogflowV2beta1DetectIntentResponse: ...

@typing.type_check_only
class GoogleCloudDialogflowV2beta1DocumentHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDialogflowV2beta1Document: ...

@typing.type_check_only
class GoogleCloudDialogflowV2beta1EntityTypeHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDialogflowV2beta1EntityType: ...

@typing.type_check_only
class GoogleCloudDialogflowV2beta1EnvironmentHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDialogflowV2beta1Environment: ...

@typing.type_check_only
class GoogleCloudDialogflowV2beta1EnvironmentHistoryHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDialogflowV2beta1EnvironmentHistory: ...

@typing.type_check_only
class GoogleCloudDialogflowV2beta1FulfillmentHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDialogflowV2beta1Fulfillment: ...

@typing.type_check_only
class GoogleCloudDialogflowV2beta1IntentHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDialogflowV2beta1Intent: ...

@typing.type_check_only
class GoogleCloudDialogflowV2beta1KnowledgeBaseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDialogflowV2beta1KnowledgeBase: ...

@typing.type_check_only
class GoogleCloudDialogflowV2beta1ListAnswerRecordsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDialogflowV2beta1ListAnswerRecordsResponse: ...

@typing.type_check_only
class GoogleCloudDialogflowV2beta1ListContextsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDialogflowV2beta1ListContextsResponse: ...

@typing.type_check_only
class GoogleCloudDialogflowV2beta1ListConversationProfilesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDialogflowV2beta1ListConversationProfilesResponse: ...

@typing.type_check_only
class GoogleCloudDialogflowV2beta1ListConversationsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDialogflowV2beta1ListConversationsResponse: ...

@typing.type_check_only
class GoogleCloudDialogflowV2beta1ListDocumentsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDialogflowV2beta1ListDocumentsResponse: ...

@typing.type_check_only
class GoogleCloudDialogflowV2beta1ListEntityTypesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDialogflowV2beta1ListEntityTypesResponse: ...

@typing.type_check_only
class GoogleCloudDialogflowV2beta1ListEnvironmentsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDialogflowV2beta1ListEnvironmentsResponse: ...

@typing.type_check_only
class GoogleCloudDialogflowV2beta1ListIntentsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDialogflowV2beta1ListIntentsResponse: ...

@typing.type_check_only
class GoogleCloudDialogflowV2beta1ListKnowledgeBasesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDialogflowV2beta1ListKnowledgeBasesResponse: ...

@typing.type_check_only
class GoogleCloudDialogflowV2beta1ListMessagesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDialogflowV2beta1ListMessagesResponse: ...

@typing.type_check_only
class GoogleCloudDialogflowV2beta1ListParticipantsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDialogflowV2beta1ListParticipantsResponse: ...

@typing.type_check_only
class GoogleCloudDialogflowV2beta1ListSessionEntityTypesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDialogflowV2beta1ListSessionEntityTypesResponse: ...

@typing.type_check_only
class GoogleCloudDialogflowV2beta1ListSuggestionsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDialogflowV2beta1ListSuggestionsResponse: ...

@typing.type_check_only
class GoogleCloudDialogflowV2beta1ListVersionsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDialogflowV2beta1ListVersionsResponse: ...

@typing.type_check_only
class GoogleCloudDialogflowV2beta1ParticipantHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDialogflowV2beta1Participant: ...

@typing.type_check_only
class GoogleCloudDialogflowV2beta1SearchAgentsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDialogflowV2beta1SearchAgentsResponse: ...

@typing.type_check_only
class GoogleCloudDialogflowV2beta1SessionEntityTypeHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDialogflowV2beta1SessionEntityType: ...

@typing.type_check_only
class GoogleCloudDialogflowV2beta1SuggestArticlesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDialogflowV2beta1SuggestArticlesResponse: ...

@typing.type_check_only
class GoogleCloudDialogflowV2beta1SuggestConversationSummaryResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDialogflowV2beta1SuggestConversationSummaryResponse: ...

@typing.type_check_only
class GoogleCloudDialogflowV2beta1SuggestFaqAnswersResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDialogflowV2beta1SuggestFaqAnswersResponse: ...

@typing.type_check_only
class GoogleCloudDialogflowV2beta1SuggestSmartRepliesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDialogflowV2beta1SuggestSmartRepliesResponse: ...

@typing.type_check_only
class GoogleCloudDialogflowV2beta1ValidationResultHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDialogflowV2beta1ValidationResult: ...

@typing.type_check_only
class GoogleCloudDialogflowV2beta1VersionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDialogflowV2beta1Version: ...

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
