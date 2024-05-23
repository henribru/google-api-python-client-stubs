import collections.abc
import typing

import httplib2
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http

from .schemas import *

_list = list

@typing.type_check_only
class DiscoveryEngineResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class ProjectsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class LocationsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class CollectionsResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class DataConnectorResource(googleapiclient.discovery.Resource):
                    @typing.type_check_only
                    class OperationsResource(googleapiclient.discovery.Resource):
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
                        ) -> (
                            GoogleLongrunningListOperationsResponseHttpRequest | None
                        ): ...

                    def operations(self) -> OperationsResource: ...

                @typing.type_check_only
                class DataStoresResource(googleapiclient.discovery.Resource):
                    @typing.type_check_only
                    class BranchesResource(googleapiclient.discovery.Resource):
                        @typing.type_check_only
                        class DocumentsResource(googleapiclient.discovery.Resource):
                            def create(
                                self,
                                *,
                                parent: str,
                                body: GoogleCloudDiscoveryengineV1betaDocument = ...,
                                documentId: str = ...,
                                **kwargs: typing.Any,
                            ) -> (
                                GoogleCloudDiscoveryengineV1betaDocumentHttpRequest
                            ): ...
                            def delete(
                                self, *, name: str, **kwargs: typing.Any
                            ) -> GoogleProtobufEmptyHttpRequest: ...
                            def get(
                                self, *, name: str, **kwargs: typing.Any
                            ) -> (
                                GoogleCloudDiscoveryengineV1betaDocumentHttpRequest
                            ): ...
                            def import_(
                                self,
                                *,
                                parent: str,
                                body: GoogleCloudDiscoveryengineV1betaImportDocumentsRequest = ...,
                                **kwargs: typing.Any,
                            ) -> GoogleLongrunningOperationHttpRequest: ...
                            def list(
                                self,
                                *,
                                parent: str,
                                pageSize: int = ...,
                                pageToken: str = ...,
                                **kwargs: typing.Any,
                            ) -> GoogleCloudDiscoveryengineV1betaListDocumentsResponseHttpRequest: ...
                            def list_next(
                                self,
                                previous_request: GoogleCloudDiscoveryengineV1betaListDocumentsResponseHttpRequest,
                                previous_response: GoogleCloudDiscoveryengineV1betaListDocumentsResponse,
                            ) -> (
                                GoogleCloudDiscoveryengineV1betaListDocumentsResponseHttpRequest
                                | None
                            ): ...
                            def patch(
                                self,
                                *,
                                name: str,
                                body: GoogleCloudDiscoveryengineV1betaDocument = ...,
                                allowMissing: bool = ...,
                                updateMask: str = ...,
                                **kwargs: typing.Any,
                            ) -> (
                                GoogleCloudDiscoveryengineV1betaDocumentHttpRequest
                            ): ...
                            def purge(
                                self,
                                *,
                                parent: str,
                                body: GoogleCloudDiscoveryengineV1betaPurgeDocumentsRequest = ...,
                                **kwargs: typing.Any,
                            ) -> GoogleLongrunningOperationHttpRequest: ...

                        @typing.type_check_only
                        class OperationsResource(googleapiclient.discovery.Resource):
                            def cancel(
                                self,
                                *,
                                name: str,
                                body: GoogleLongrunningCancelOperationRequest = ...,
                                **kwargs: typing.Any,
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
                            ) -> (
                                GoogleLongrunningListOperationsResponseHttpRequest
                                | None
                            ): ...

                        def documents(self) -> DocumentsResource: ...
                        def operations(self) -> OperationsResource: ...

                    @typing.type_check_only
                    class ConversationsResource(googleapiclient.discovery.Resource):
                        def converse(
                            self,
                            *,
                            name: str,
                            body: GoogleCloudDiscoveryengineV1betaConverseConversationRequest = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudDiscoveryengineV1betaConverseConversationResponseHttpRequest: ...
                        def create(
                            self,
                            *,
                            parent: str,
                            body: GoogleCloudDiscoveryengineV1betaConversation = ...,
                            **kwargs: typing.Any,
                        ) -> (
                            GoogleCloudDiscoveryengineV1betaConversationHttpRequest
                        ): ...
                        def delete(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> GoogleProtobufEmptyHttpRequest: ...
                        def get(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> (
                            GoogleCloudDiscoveryengineV1betaConversationHttpRequest
                        ): ...
                        def list(
                            self,
                            *,
                            parent: str,
                            filter: str = ...,
                            orderBy: str = ...,
                            pageSize: int = ...,
                            pageToken: str = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudDiscoveryengineV1betaListConversationsResponseHttpRequest: ...
                        def list_next(
                            self,
                            previous_request: GoogleCloudDiscoveryengineV1betaListConversationsResponseHttpRequest,
                            previous_response: GoogleCloudDiscoveryengineV1betaListConversationsResponse,
                        ) -> (
                            GoogleCloudDiscoveryengineV1betaListConversationsResponseHttpRequest
                            | None
                        ): ...
                        def patch(
                            self,
                            *,
                            name: str,
                            body: GoogleCloudDiscoveryengineV1betaConversation = ...,
                            updateMask: str = ...,
                            **kwargs: typing.Any,
                        ) -> (
                            GoogleCloudDiscoveryengineV1betaConversationHttpRequest
                        ): ...

                    @typing.type_check_only
                    class CustomModelsResource(googleapiclient.discovery.Resource):
                        def list(
                            self, *, dataStore: str, **kwargs: typing.Any
                        ) -> GoogleCloudDiscoveryengineV1betaListCustomModelsResponseHttpRequest: ...

                    @typing.type_check_only
                    class ModelsResource(googleapiclient.discovery.Resource):
                        @typing.type_check_only
                        class OperationsResource(googleapiclient.discovery.Resource):
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
                            ) -> (
                                GoogleLongrunningListOperationsResponseHttpRequest
                                | None
                            ): ...

                        def operations(self) -> OperationsResource: ...

                    @typing.type_check_only
                    class OperationsResource(googleapiclient.discovery.Resource):
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
                        ) -> (
                            GoogleLongrunningListOperationsResponseHttpRequest | None
                        ): ...

                    @typing.type_check_only
                    class SchemasResource(googleapiclient.discovery.Resource):
                        @typing.type_check_only
                        class OperationsResource(googleapiclient.discovery.Resource):
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
                            ) -> (
                                GoogleLongrunningListOperationsResponseHttpRequest
                                | None
                            ): ...

                        def create(
                            self,
                            *,
                            parent: str,
                            body: GoogleCloudDiscoveryengineV1betaSchema = ...,
                            schemaId: str = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleLongrunningOperationHttpRequest: ...
                        def delete(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> GoogleLongrunningOperationHttpRequest: ...
                        def get(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> GoogleCloudDiscoveryengineV1betaSchemaHttpRequest: ...
                        def list(
                            self,
                            *,
                            parent: str,
                            pageSize: int = ...,
                            pageToken: str = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudDiscoveryengineV1betaListSchemasResponseHttpRequest: ...
                        def list_next(
                            self,
                            previous_request: GoogleCloudDiscoveryengineV1betaListSchemasResponseHttpRequest,
                            previous_response: GoogleCloudDiscoveryengineV1betaListSchemasResponse,
                        ) -> (
                            GoogleCloudDiscoveryengineV1betaListSchemasResponseHttpRequest
                            | None
                        ): ...
                        def patch(
                            self,
                            *,
                            name: str,
                            body: GoogleCloudDiscoveryengineV1betaSchema = ...,
                            allowMissing: bool = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleLongrunningOperationHttpRequest: ...
                        def operations(self) -> OperationsResource: ...

                    @typing.type_check_only
                    class ServingConfigsResource(googleapiclient.discovery.Resource):
                        def answer(
                            self,
                            *,
                            servingConfig: str,
                            body: GoogleCloudDiscoveryengineV1betaAnswerQueryRequest = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudDiscoveryengineV1betaAnswerQueryResponseHttpRequest: ...
                        def get(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> (
                            GoogleCloudDiscoveryengineV1betaServingConfigHttpRequest
                        ): ...
                        def list(
                            self,
                            *,
                            parent: str,
                            pageSize: int = ...,
                            pageToken: str = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudDiscoveryengineV1betaListServingConfigsResponseHttpRequest: ...
                        def list_next(
                            self,
                            previous_request: GoogleCloudDiscoveryengineV1betaListServingConfigsResponseHttpRequest,
                            previous_response: GoogleCloudDiscoveryengineV1betaListServingConfigsResponse,
                        ) -> (
                            GoogleCloudDiscoveryengineV1betaListServingConfigsResponseHttpRequest
                            | None
                        ): ...
                        def patch(
                            self,
                            *,
                            name: str,
                            body: GoogleCloudDiscoveryengineV1betaServingConfig = ...,
                            updateMask: str = ...,
                            **kwargs: typing.Any,
                        ) -> (
                            GoogleCloudDiscoveryengineV1betaServingConfigHttpRequest
                        ): ...
                        def recommend(
                            self,
                            *,
                            servingConfig: str,
                            body: GoogleCloudDiscoveryengineV1betaRecommendRequest = ...,
                            **kwargs: typing.Any,
                        ) -> (
                            GoogleCloudDiscoveryengineV1betaRecommendResponseHttpRequest
                        ): ...
                        def search(
                            self,
                            *,
                            servingConfig: str,
                            body: GoogleCloudDiscoveryengineV1betaSearchRequest = ...,
                            **kwargs: typing.Any,
                        ) -> (
                            GoogleCloudDiscoveryengineV1betaSearchResponseHttpRequest
                        ): ...
                        def search_next(
                            self,
                            previous_request: GoogleCloudDiscoveryengineV1betaSearchResponseHttpRequest,
                            previous_response: GoogleCloudDiscoveryengineV1betaSearchResponse,
                        ) -> (
                            GoogleCloudDiscoveryengineV1betaSearchResponseHttpRequest
                            | None
                        ): ...

                    @typing.type_check_only
                    class SessionsResource(googleapiclient.discovery.Resource):
                        @typing.type_check_only
                        class AnswersResource(googleapiclient.discovery.Resource):
                            def get(
                                self, *, name: str, **kwargs: typing.Any
                            ) -> GoogleCloudDiscoveryengineV1betaAnswerHttpRequest: ...

                        def create(
                            self,
                            *,
                            parent: str,
                            body: GoogleCloudDiscoveryengineV1betaSession = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudDiscoveryengineV1betaSessionHttpRequest: ...
                        def delete(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> GoogleProtobufEmptyHttpRequest: ...
                        def get(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> GoogleCloudDiscoveryengineV1betaSessionHttpRequest: ...
                        def list(
                            self,
                            *,
                            parent: str,
                            filter: str = ...,
                            orderBy: str = ...,
                            pageSize: int = ...,
                            pageToken: str = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudDiscoveryengineV1betaListSessionsResponseHttpRequest: ...
                        def list_next(
                            self,
                            previous_request: GoogleCloudDiscoveryengineV1betaListSessionsResponseHttpRequest,
                            previous_response: GoogleCloudDiscoveryengineV1betaListSessionsResponse,
                        ) -> (
                            GoogleCloudDiscoveryengineV1betaListSessionsResponseHttpRequest
                            | None
                        ): ...
                        def patch(
                            self,
                            *,
                            name: str,
                            body: GoogleCloudDiscoveryengineV1betaSession = ...,
                            updateMask: str = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudDiscoveryengineV1betaSessionHttpRequest: ...
                        def answers(self) -> AnswersResource: ...

                    @typing.type_check_only
                    class SiteSearchEngineResource(googleapiclient.discovery.Resource):
                        @typing.type_check_only
                        class OperationsResource(googleapiclient.discovery.Resource):
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
                            ) -> (
                                GoogleLongrunningListOperationsResponseHttpRequest
                                | None
                            ): ...

                        @typing.type_check_only
                        class TargetSitesResource(googleapiclient.discovery.Resource):
                            @typing.type_check_only
                            class OperationsResource(
                                googleapiclient.discovery.Resource
                            ):
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
                                ) -> (
                                    GoogleLongrunningListOperationsResponseHttpRequest
                                ): ...
                                def list_next(
                                    self,
                                    previous_request: GoogleLongrunningListOperationsResponseHttpRequest,
                                    previous_response: GoogleLongrunningListOperationsResponse,
                                ) -> (
                                    GoogleLongrunningListOperationsResponseHttpRequest
                                    | None
                                ): ...

                            def batchCreate(
                                self,
                                *,
                                parent: str,
                                body: GoogleCloudDiscoveryengineV1betaBatchCreateTargetSitesRequest = ...,
                                **kwargs: typing.Any,
                            ) -> GoogleLongrunningOperationHttpRequest: ...
                            def create(
                                self,
                                *,
                                parent: str,
                                body: GoogleCloudDiscoveryengineV1betaTargetSite = ...,
                                **kwargs: typing.Any,
                            ) -> GoogleLongrunningOperationHttpRequest: ...
                            def delete(
                                self, *, name: str, **kwargs: typing.Any
                            ) -> GoogleLongrunningOperationHttpRequest: ...
                            def get(
                                self, *, name: str, **kwargs: typing.Any
                            ) -> (
                                GoogleCloudDiscoveryengineV1betaTargetSiteHttpRequest
                            ): ...
                            def list(
                                self,
                                *,
                                parent: str,
                                pageSize: int = ...,
                                pageToken: str = ...,
                                **kwargs: typing.Any,
                            ) -> GoogleCloudDiscoveryengineV1betaListTargetSitesResponseHttpRequest: ...
                            def list_next(
                                self,
                                previous_request: GoogleCloudDiscoveryengineV1betaListTargetSitesResponseHttpRequest,
                                previous_response: GoogleCloudDiscoveryengineV1betaListTargetSitesResponse,
                            ) -> (
                                GoogleCloudDiscoveryengineV1betaListTargetSitesResponseHttpRequest
                                | None
                            ): ...
                            def patch(
                                self,
                                *,
                                name: str,
                                body: GoogleCloudDiscoveryengineV1betaTargetSite = ...,
                                **kwargs: typing.Any,
                            ) -> GoogleLongrunningOperationHttpRequest: ...
                            def operations(self) -> OperationsResource: ...

                        def batchVerifyTargetSites(
                            self,
                            *,
                            parent: str,
                            body: GoogleCloudDiscoveryengineV1betaBatchVerifyTargetSitesRequest = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleLongrunningOperationHttpRequest: ...
                        def disableAdvancedSiteSearch(
                            self,
                            *,
                            siteSearchEngine: str,
                            body: GoogleCloudDiscoveryengineV1betaDisableAdvancedSiteSearchRequest = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleLongrunningOperationHttpRequest: ...
                        def enableAdvancedSiteSearch(
                            self,
                            *,
                            siteSearchEngine: str,
                            body: GoogleCloudDiscoveryengineV1betaEnableAdvancedSiteSearchRequest = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleLongrunningOperationHttpRequest: ...
                        def fetchDomainVerificationStatus(
                            self,
                            *,
                            siteSearchEngine: str,
                            pageSize: int = ...,
                            pageToken: str = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudDiscoveryengineV1betaFetchDomainVerificationStatusResponseHttpRequest: ...
                        def fetchDomainVerificationStatus_next(
                            self,
                            previous_request: GoogleCloudDiscoveryengineV1betaFetchDomainVerificationStatusResponseHttpRequest,
                            previous_response: GoogleCloudDiscoveryengineV1betaFetchDomainVerificationStatusResponse,
                        ) -> (
                            GoogleCloudDiscoveryengineV1betaFetchDomainVerificationStatusResponseHttpRequest
                            | None
                        ): ...
                        def recrawlUris(
                            self,
                            *,
                            siteSearchEngine: str,
                            body: GoogleCloudDiscoveryengineV1betaRecrawlUrisRequest = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleLongrunningOperationHttpRequest: ...
                        def operations(self) -> OperationsResource: ...
                        def targetSites(self) -> TargetSitesResource: ...

                    @typing.type_check_only
                    class SuggestionDenyListEntriesResource(
                        googleapiclient.discovery.Resource
                    ):
                        def import_(
                            self,
                            *,
                            parent: str,
                            body: GoogleCloudDiscoveryengineV1betaImportSuggestionDenyListEntriesRequest = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleLongrunningOperationHttpRequest: ...
                        def purge(
                            self,
                            *,
                            parent: str,
                            body: GoogleCloudDiscoveryengineV1betaPurgeSuggestionDenyListEntriesRequest = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleLongrunningOperationHttpRequest: ...

                    @typing.type_check_only
                    class UserEventsResource(googleapiclient.discovery.Resource):
                        def collect(
                            self,
                            *,
                            parent: str,
                            ets: str = ...,
                            uri: str = ...,
                            userEvent: str = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleApiHttpBodyHttpRequest: ...
                        def import_(
                            self,
                            *,
                            parent: str,
                            body: GoogleCloudDiscoveryengineV1betaImportUserEventsRequest = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleLongrunningOperationHttpRequest: ...
                        def write(
                            self,
                            *,
                            parent: str,
                            body: GoogleCloudDiscoveryengineV1betaUserEvent = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudDiscoveryengineV1betaUserEventHttpRequest: ...

                    def completeQuery(
                        self,
                        *,
                        dataStore: str,
                        includeTailSuggestions: bool = ...,
                        query: str = ...,
                        queryModel: str = ...,
                        userPseudoId: str = ...,
                        **kwargs: typing.Any,
                    ) -> (
                        GoogleCloudDiscoveryengineV1betaCompleteQueryResponseHttpRequest
                    ): ...
                    def create(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudDiscoveryengineV1betaDataStore = ...,
                        createAdvancedSiteSearch: bool = ...,
                        dataStoreId: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleCloudDiscoveryengineV1betaDataStoreHttpRequest: ...
                    def getSiteSearchEngine(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> (
                        GoogleCloudDiscoveryengineV1betaSiteSearchEngineHttpRequest
                    ): ...
                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudDiscoveryengineV1betaListDataStoresResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudDiscoveryengineV1betaListDataStoresResponseHttpRequest,
                        previous_response: GoogleCloudDiscoveryengineV1betaListDataStoresResponse,
                    ) -> (
                        GoogleCloudDiscoveryengineV1betaListDataStoresResponseHttpRequest
                        | None
                    ): ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudDiscoveryengineV1betaDataStore = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudDiscoveryengineV1betaDataStoreHttpRequest: ...
                    def trainCustomModel(
                        self,
                        *,
                        dataStore: str,
                        body: GoogleCloudDiscoveryengineV1betaTrainCustomModelRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def branches(self) -> BranchesResource: ...
                    def conversations(self) -> ConversationsResource: ...
                    def customModels(self) -> CustomModelsResource: ...
                    def models(self) -> ModelsResource: ...
                    def operations(self) -> OperationsResource: ...
                    def schemas(self) -> SchemasResource: ...
                    def servingConfigs(self) -> ServingConfigsResource: ...
                    def sessions(self) -> SessionsResource: ...
                    def siteSearchEngine(self) -> SiteSearchEngineResource: ...
                    def suggestionDenyListEntries(
                        self,
                    ) -> SuggestionDenyListEntriesResource: ...
                    def userEvents(self) -> UserEventsResource: ...

                @typing.type_check_only
                class EnginesResource(googleapiclient.discovery.Resource):
                    @typing.type_check_only
                    class ConversationsResource(googleapiclient.discovery.Resource):
                        def converse(
                            self,
                            *,
                            name: str,
                            body: GoogleCloudDiscoveryengineV1betaConverseConversationRequest = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudDiscoveryengineV1betaConverseConversationResponseHttpRequest: ...
                        def create(
                            self,
                            *,
                            parent: str,
                            body: GoogleCloudDiscoveryengineV1betaConversation = ...,
                            **kwargs: typing.Any,
                        ) -> (
                            GoogleCloudDiscoveryengineV1betaConversationHttpRequest
                        ): ...
                        def delete(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> GoogleProtobufEmptyHttpRequest: ...
                        def get(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> (
                            GoogleCloudDiscoveryengineV1betaConversationHttpRequest
                        ): ...
                        def list(
                            self,
                            *,
                            parent: str,
                            filter: str = ...,
                            orderBy: str = ...,
                            pageSize: int = ...,
                            pageToken: str = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudDiscoveryengineV1betaListConversationsResponseHttpRequest: ...
                        def list_next(
                            self,
                            previous_request: GoogleCloudDiscoveryengineV1betaListConversationsResponseHttpRequest,
                            previous_response: GoogleCloudDiscoveryengineV1betaListConversationsResponse,
                        ) -> (
                            GoogleCloudDiscoveryengineV1betaListConversationsResponseHttpRequest
                            | None
                        ): ...
                        def patch(
                            self,
                            *,
                            name: str,
                            body: GoogleCloudDiscoveryengineV1betaConversation = ...,
                            updateMask: str = ...,
                            **kwargs: typing.Any,
                        ) -> (
                            GoogleCloudDiscoveryengineV1betaConversationHttpRequest
                        ): ...

                    @typing.type_check_only
                    class OperationsResource(googleapiclient.discovery.Resource):
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
                        ) -> (
                            GoogleLongrunningListOperationsResponseHttpRequest | None
                        ): ...

                    @typing.type_check_only
                    class ServingConfigsResource(googleapiclient.discovery.Resource):
                        def answer(
                            self,
                            *,
                            servingConfig: str,
                            body: GoogleCloudDiscoveryengineV1betaAnswerQueryRequest = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudDiscoveryengineV1betaAnswerQueryResponseHttpRequest: ...
                        def get(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> (
                            GoogleCloudDiscoveryengineV1betaServingConfigHttpRequest
                        ): ...
                        def list(
                            self,
                            *,
                            parent: str,
                            pageSize: int = ...,
                            pageToken: str = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudDiscoveryengineV1betaListServingConfigsResponseHttpRequest: ...
                        def list_next(
                            self,
                            previous_request: GoogleCloudDiscoveryengineV1betaListServingConfigsResponseHttpRequest,
                            previous_response: GoogleCloudDiscoveryengineV1betaListServingConfigsResponse,
                        ) -> (
                            GoogleCloudDiscoveryengineV1betaListServingConfigsResponseHttpRequest
                            | None
                        ): ...
                        def patch(
                            self,
                            *,
                            name: str,
                            body: GoogleCloudDiscoveryengineV1betaServingConfig = ...,
                            updateMask: str = ...,
                            **kwargs: typing.Any,
                        ) -> (
                            GoogleCloudDiscoveryengineV1betaServingConfigHttpRequest
                        ): ...
                        def recommend(
                            self,
                            *,
                            servingConfig: str,
                            body: GoogleCloudDiscoveryengineV1betaRecommendRequest = ...,
                            **kwargs: typing.Any,
                        ) -> (
                            GoogleCloudDiscoveryengineV1betaRecommendResponseHttpRequest
                        ): ...
                        def search(
                            self,
                            *,
                            servingConfig: str,
                            body: GoogleCloudDiscoveryengineV1betaSearchRequest = ...,
                            **kwargs: typing.Any,
                        ) -> (
                            GoogleCloudDiscoveryengineV1betaSearchResponseHttpRequest
                        ): ...
                        def search_next(
                            self,
                            previous_request: GoogleCloudDiscoveryengineV1betaSearchResponseHttpRequest,
                            previous_response: GoogleCloudDiscoveryengineV1betaSearchResponse,
                        ) -> (
                            GoogleCloudDiscoveryengineV1betaSearchResponseHttpRequest
                            | None
                        ): ...

                    @typing.type_check_only
                    class SessionsResource(googleapiclient.discovery.Resource):
                        @typing.type_check_only
                        class AnswersResource(googleapiclient.discovery.Resource):
                            def get(
                                self, *, name: str, **kwargs: typing.Any
                            ) -> GoogleCloudDiscoveryengineV1betaAnswerHttpRequest: ...

                        def create(
                            self,
                            *,
                            parent: str,
                            body: GoogleCloudDiscoveryengineV1betaSession = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudDiscoveryengineV1betaSessionHttpRequest: ...
                        def delete(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> GoogleProtobufEmptyHttpRequest: ...
                        def get(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> GoogleCloudDiscoveryengineV1betaSessionHttpRequest: ...
                        def list(
                            self,
                            *,
                            parent: str,
                            filter: str = ...,
                            orderBy: str = ...,
                            pageSize: int = ...,
                            pageToken: str = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudDiscoveryengineV1betaListSessionsResponseHttpRequest: ...
                        def list_next(
                            self,
                            previous_request: GoogleCloudDiscoveryengineV1betaListSessionsResponseHttpRequest,
                            previous_response: GoogleCloudDiscoveryengineV1betaListSessionsResponse,
                        ) -> (
                            GoogleCloudDiscoveryengineV1betaListSessionsResponseHttpRequest
                            | None
                        ): ...
                        def patch(
                            self,
                            *,
                            name: str,
                            body: GoogleCloudDiscoveryengineV1betaSession = ...,
                            updateMask: str = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudDiscoveryengineV1betaSessionHttpRequest: ...
                        def answers(self) -> AnswersResource: ...

                    def create(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudDiscoveryengineV1betaEngine = ...,
                        engineId: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleCloudDiscoveryengineV1betaEngineHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
                    ) -> (
                        GoogleCloudDiscoveryengineV1betaListEnginesResponseHttpRequest
                    ): ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudDiscoveryengineV1betaListEnginesResponseHttpRequest,
                        previous_response: GoogleCloudDiscoveryengineV1betaListEnginesResponse,
                    ) -> (
                        GoogleCloudDiscoveryengineV1betaListEnginesResponseHttpRequest
                        | None
                    ): ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudDiscoveryengineV1betaEngine = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudDiscoveryengineV1betaEngineHttpRequest: ...
                    def pause(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudDiscoveryengineV1betaPauseEngineRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudDiscoveryengineV1betaEngineHttpRequest: ...
                    def resume(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudDiscoveryengineV1betaResumeEngineRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudDiscoveryengineV1betaEngineHttpRequest: ...
                    def tune(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudDiscoveryengineV1betaTuneEngineRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def conversations(self) -> ConversationsResource: ...
                    def operations(self) -> OperationsResource: ...
                    def servingConfigs(self) -> ServingConfigsResource: ...
                    def sessions(self) -> SessionsResource: ...

                @typing.type_check_only
                class OperationsResource(googleapiclient.discovery.Resource):
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

                def dataConnector(self) -> DataConnectorResource: ...
                def dataStores(self) -> DataStoresResource: ...
                def engines(self) -> EnginesResource: ...
                def operations(self) -> OperationsResource: ...

            @typing.type_check_only
            class DataStoresResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class BranchesResource(googleapiclient.discovery.Resource):
                    @typing.type_check_only
                    class DocumentsResource(googleapiclient.discovery.Resource):
                        def create(
                            self,
                            *,
                            parent: str,
                            body: GoogleCloudDiscoveryengineV1betaDocument = ...,
                            documentId: str = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudDiscoveryengineV1betaDocumentHttpRequest: ...
                        def delete(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> GoogleProtobufEmptyHttpRequest: ...
                        def get(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> GoogleCloudDiscoveryengineV1betaDocumentHttpRequest: ...
                        def import_(
                            self,
                            *,
                            parent: str,
                            body: GoogleCloudDiscoveryengineV1betaImportDocumentsRequest = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleLongrunningOperationHttpRequest: ...
                        def list(
                            self,
                            *,
                            parent: str,
                            pageSize: int = ...,
                            pageToken: str = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudDiscoveryengineV1betaListDocumentsResponseHttpRequest: ...
                        def list_next(
                            self,
                            previous_request: GoogleCloudDiscoveryengineV1betaListDocumentsResponseHttpRequest,
                            previous_response: GoogleCloudDiscoveryengineV1betaListDocumentsResponse,
                        ) -> (
                            GoogleCloudDiscoveryengineV1betaListDocumentsResponseHttpRequest
                            | None
                        ): ...
                        def patch(
                            self,
                            *,
                            name: str,
                            body: GoogleCloudDiscoveryengineV1betaDocument = ...,
                            allowMissing: bool = ...,
                            updateMask: str = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudDiscoveryengineV1betaDocumentHttpRequest: ...
                        def purge(
                            self,
                            *,
                            parent: str,
                            body: GoogleCloudDiscoveryengineV1betaPurgeDocumentsRequest = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleLongrunningOperationHttpRequest: ...

                    @typing.type_check_only
                    class OperationsResource(googleapiclient.discovery.Resource):
                        def cancel(
                            self,
                            *,
                            name: str,
                            body: GoogleLongrunningCancelOperationRequest = ...,
                            **kwargs: typing.Any,
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
                        ) -> (
                            GoogleLongrunningListOperationsResponseHttpRequest | None
                        ): ...

                    def documents(self) -> DocumentsResource: ...
                    def operations(self) -> OperationsResource: ...

                @typing.type_check_only
                class ConversationsResource(googleapiclient.discovery.Resource):
                    def converse(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudDiscoveryengineV1betaConverseConversationRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudDiscoveryengineV1betaConverseConversationResponseHttpRequest: ...
                    def create(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudDiscoveryengineV1betaConversation = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudDiscoveryengineV1betaConversationHttpRequest: ...
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleProtobufEmptyHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleCloudDiscoveryengineV1betaConversationHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str = ...,
                        orderBy: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudDiscoveryengineV1betaListConversationsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudDiscoveryengineV1betaListConversationsResponseHttpRequest,
                        previous_response: GoogleCloudDiscoveryengineV1betaListConversationsResponse,
                    ) -> (
                        GoogleCloudDiscoveryengineV1betaListConversationsResponseHttpRequest
                        | None
                    ): ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudDiscoveryengineV1betaConversation = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudDiscoveryengineV1betaConversationHttpRequest: ...

                @typing.type_check_only
                class ModelsResource(googleapiclient.discovery.Resource):
                    @typing.type_check_only
                    class OperationsResource(googleapiclient.discovery.Resource):
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
                        ) -> (
                            GoogleLongrunningListOperationsResponseHttpRequest | None
                        ): ...

                    def operations(self) -> OperationsResource: ...

                @typing.type_check_only
                class OperationsResource(googleapiclient.discovery.Resource):
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
                class SchemasResource(googleapiclient.discovery.Resource):
                    def create(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudDiscoveryengineV1betaSchema = ...,
                        schemaId: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleCloudDiscoveryengineV1betaSchemaHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
                    ) -> (
                        GoogleCloudDiscoveryengineV1betaListSchemasResponseHttpRequest
                    ): ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudDiscoveryengineV1betaListSchemasResponseHttpRequest,
                        previous_response: GoogleCloudDiscoveryengineV1betaListSchemasResponse,
                    ) -> (
                        GoogleCloudDiscoveryengineV1betaListSchemasResponseHttpRequest
                        | None
                    ): ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudDiscoveryengineV1betaSchema = ...,
                        allowMissing: bool = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleLongrunningOperationHttpRequest: ...

                @typing.type_check_only
                class ServingConfigsResource(googleapiclient.discovery.Resource):
                    def answer(
                        self,
                        *,
                        servingConfig: str,
                        body: GoogleCloudDiscoveryengineV1betaAnswerQueryRequest = ...,
                        **kwargs: typing.Any,
                    ) -> (
                        GoogleCloudDiscoveryengineV1betaAnswerQueryResponseHttpRequest
                    ): ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleCloudDiscoveryengineV1betaServingConfigHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudDiscoveryengineV1betaListServingConfigsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudDiscoveryengineV1betaListServingConfigsResponseHttpRequest,
                        previous_response: GoogleCloudDiscoveryengineV1betaListServingConfigsResponse,
                    ) -> (
                        GoogleCloudDiscoveryengineV1betaListServingConfigsResponseHttpRequest
                        | None
                    ): ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudDiscoveryengineV1betaServingConfig = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudDiscoveryengineV1betaServingConfigHttpRequest: ...
                    def recommend(
                        self,
                        *,
                        servingConfig: str,
                        body: GoogleCloudDiscoveryengineV1betaRecommendRequest = ...,
                        **kwargs: typing.Any,
                    ) -> (
                        GoogleCloudDiscoveryengineV1betaRecommendResponseHttpRequest
                    ): ...
                    def search(
                        self,
                        *,
                        servingConfig: str,
                        body: GoogleCloudDiscoveryengineV1betaSearchRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudDiscoveryengineV1betaSearchResponseHttpRequest: ...
                    def search_next(
                        self,
                        previous_request: GoogleCloudDiscoveryengineV1betaSearchResponseHttpRequest,
                        previous_response: GoogleCloudDiscoveryengineV1betaSearchResponse,
                    ) -> (
                        GoogleCloudDiscoveryengineV1betaSearchResponseHttpRequest | None
                    ): ...

                @typing.type_check_only
                class SessionsResource(googleapiclient.discovery.Resource):
                    @typing.type_check_only
                    class AnswersResource(googleapiclient.discovery.Resource):
                        def get(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> GoogleCloudDiscoveryengineV1betaAnswerHttpRequest: ...

                    def create(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudDiscoveryengineV1betaSession = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudDiscoveryengineV1betaSessionHttpRequest: ...
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleProtobufEmptyHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleCloudDiscoveryengineV1betaSessionHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str = ...,
                        orderBy: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
                    ) -> (
                        GoogleCloudDiscoveryengineV1betaListSessionsResponseHttpRequest
                    ): ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudDiscoveryengineV1betaListSessionsResponseHttpRequest,
                        previous_response: GoogleCloudDiscoveryengineV1betaListSessionsResponse,
                    ) -> (
                        GoogleCloudDiscoveryengineV1betaListSessionsResponseHttpRequest
                        | None
                    ): ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudDiscoveryengineV1betaSession = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudDiscoveryengineV1betaSessionHttpRequest: ...
                    def answers(self) -> AnswersResource: ...

                @typing.type_check_only
                class SiteSearchEngineResource(googleapiclient.discovery.Resource):
                    @typing.type_check_only
                    class TargetSitesResource(googleapiclient.discovery.Resource):
                        def batchCreate(
                            self,
                            *,
                            parent: str,
                            body: GoogleCloudDiscoveryengineV1betaBatchCreateTargetSitesRequest = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleLongrunningOperationHttpRequest: ...
                        def create(
                            self,
                            *,
                            parent: str,
                            body: GoogleCloudDiscoveryengineV1betaTargetSite = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleLongrunningOperationHttpRequest: ...
                        def delete(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> GoogleLongrunningOperationHttpRequest: ...
                        def get(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> GoogleCloudDiscoveryengineV1betaTargetSiteHttpRequest: ...
                        def list(
                            self,
                            *,
                            parent: str,
                            pageSize: int = ...,
                            pageToken: str = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudDiscoveryengineV1betaListTargetSitesResponseHttpRequest: ...
                        def list_next(
                            self,
                            previous_request: GoogleCloudDiscoveryengineV1betaListTargetSitesResponseHttpRequest,
                            previous_response: GoogleCloudDiscoveryengineV1betaListTargetSitesResponse,
                        ) -> (
                            GoogleCloudDiscoveryengineV1betaListTargetSitesResponseHttpRequest
                            | None
                        ): ...
                        def patch(
                            self,
                            *,
                            name: str,
                            body: GoogleCloudDiscoveryengineV1betaTargetSite = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleLongrunningOperationHttpRequest: ...

                    def disableAdvancedSiteSearch(
                        self,
                        *,
                        siteSearchEngine: str,
                        body: GoogleCloudDiscoveryengineV1betaDisableAdvancedSiteSearchRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def enableAdvancedSiteSearch(
                        self,
                        *,
                        siteSearchEngine: str,
                        body: GoogleCloudDiscoveryengineV1betaEnableAdvancedSiteSearchRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def recrawlUris(
                        self,
                        *,
                        siteSearchEngine: str,
                        body: GoogleCloudDiscoveryengineV1betaRecrawlUrisRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def targetSites(self) -> TargetSitesResource: ...

                @typing.type_check_only
                class SuggestionDenyListEntriesResource(
                    googleapiclient.discovery.Resource
                ):
                    def import_(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudDiscoveryengineV1betaImportSuggestionDenyListEntriesRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def purge(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudDiscoveryengineV1betaPurgeSuggestionDenyListEntriesRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleLongrunningOperationHttpRequest: ...

                @typing.type_check_only
                class UserEventsResource(googleapiclient.discovery.Resource):
                    def collect(
                        self,
                        *,
                        parent: str,
                        ets: str = ...,
                        uri: str = ...,
                        userEvent: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleApiHttpBodyHttpRequest: ...
                    def import_(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudDiscoveryengineV1betaImportUserEventsRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def write(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudDiscoveryengineV1betaUserEvent = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudDiscoveryengineV1betaUserEventHttpRequest: ...

                def completeQuery(
                    self,
                    *,
                    dataStore: str,
                    includeTailSuggestions: bool = ...,
                    query: str = ...,
                    queryModel: str = ...,
                    userPseudoId: str = ...,
                    **kwargs: typing.Any,
                ) -> (
                    GoogleCloudDiscoveryengineV1betaCompleteQueryResponseHttpRequest
                ): ...
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudDiscoveryengineV1betaDataStore = ...,
                    createAdvancedSiteSearch: bool = ...,
                    dataStoreId: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudDiscoveryengineV1betaDataStoreHttpRequest: ...
                def getSiteSearchEngine(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudDiscoveryengineV1betaSiteSearchEngineHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> (
                    GoogleCloudDiscoveryengineV1betaListDataStoresResponseHttpRequest
                ): ...
                def list_next(
                    self,
                    previous_request: GoogleCloudDiscoveryengineV1betaListDataStoresResponseHttpRequest,
                    previous_response: GoogleCloudDiscoveryengineV1betaListDataStoresResponse,
                ) -> (
                    GoogleCloudDiscoveryengineV1betaListDataStoresResponseHttpRequest
                    | None
                ): ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudDiscoveryengineV1betaDataStore = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudDiscoveryengineV1betaDataStoreHttpRequest: ...
                def branches(self) -> BranchesResource: ...
                def conversations(self) -> ConversationsResource: ...
                def models(self) -> ModelsResource: ...
                def operations(self) -> OperationsResource: ...
                def schemas(self) -> SchemasResource: ...
                def servingConfigs(self) -> ServingConfigsResource: ...
                def sessions(self) -> SessionsResource: ...
                def siteSearchEngine(self) -> SiteSearchEngineResource: ...
                def suggestionDenyListEntries(
                    self,
                ) -> SuggestionDenyListEntriesResource: ...
                def userEvents(self) -> UserEventsResource: ...

            @typing.type_check_only
            class GroundingConfigsResource(googleapiclient.discovery.Resource):
                def check(
                    self,
                    *,
                    groundingConfig: str,
                    body: GoogleCloudDiscoveryengineV1betaCheckGroundingRequest = ...,
                    **kwargs: typing.Any,
                ) -> (
                    GoogleCloudDiscoveryengineV1betaCheckGroundingResponseHttpRequest
                ): ...

            @typing.type_check_only
            class OperationsResource(googleapiclient.discovery.Resource):
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
            class RankingConfigsResource(googleapiclient.discovery.Resource):
                def rank(
                    self,
                    *,
                    rankingConfig: str,
                    body: GoogleCloudDiscoveryengineV1betaRankRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudDiscoveryengineV1betaRankResponseHttpRequest: ...

            @typing.type_check_only
            class UserEventsResource(googleapiclient.discovery.Resource):
                def write(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudDiscoveryengineV1betaUserEvent = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudDiscoveryengineV1betaUserEventHttpRequest: ...

            def collections(self) -> CollectionsResource: ...
            def dataStores(self) -> DataStoresResource: ...
            def groundingConfigs(self) -> GroundingConfigsResource: ...
            def operations(self) -> OperationsResource: ...
            def rankingConfigs(self) -> RankingConfigsResource: ...
            def userEvents(self) -> UserEventsResource: ...

        @typing.type_check_only
        class OperationsResource(googleapiclient.discovery.Resource):
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
class GoogleApiHttpBodyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleApiHttpBody: ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaAnswerHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDiscoveryengineV1betaAnswer: ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaAnswerQueryResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDiscoveryengineV1betaAnswerQueryResponse: ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaCheckGroundingResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDiscoveryengineV1betaCheckGroundingResponse: ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaCompleteQueryResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDiscoveryengineV1betaCompleteQueryResponse: ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaConversationHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDiscoveryengineV1betaConversation: ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaConverseConversationResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDiscoveryengineV1betaConverseConversationResponse: ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaDataStoreHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDiscoveryengineV1betaDataStore: ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaDocumentHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDiscoveryengineV1betaDocument: ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaEngineHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDiscoveryengineV1betaEngine: ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaFetchDomainVerificationStatusResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDiscoveryengineV1betaFetchDomainVerificationStatusResponse: ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaListConversationsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDiscoveryengineV1betaListConversationsResponse: ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaListCustomModelsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDiscoveryengineV1betaListCustomModelsResponse: ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaListDataStoresResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDiscoveryengineV1betaListDataStoresResponse: ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaListDocumentsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDiscoveryengineV1betaListDocumentsResponse: ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaListEnginesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDiscoveryengineV1betaListEnginesResponse: ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaListSchemasResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDiscoveryengineV1betaListSchemasResponse: ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaListServingConfigsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDiscoveryengineV1betaListServingConfigsResponse: ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaListSessionsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDiscoveryengineV1betaListSessionsResponse: ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaListTargetSitesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDiscoveryengineV1betaListTargetSitesResponse: ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaRankResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDiscoveryengineV1betaRankResponse: ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaRecommendResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDiscoveryengineV1betaRecommendResponse: ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaSchemaHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDiscoveryengineV1betaSchema: ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaSearchResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDiscoveryengineV1betaSearchResponse: ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaServingConfigHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDiscoveryengineV1betaServingConfig: ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaSessionHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDiscoveryengineV1betaSession: ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaSiteSearchEngineHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDiscoveryengineV1betaSiteSearchEngine: ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaTargetSiteHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDiscoveryengineV1betaTargetSite: ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaUserEventHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDiscoveryengineV1betaUserEvent: ...

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
