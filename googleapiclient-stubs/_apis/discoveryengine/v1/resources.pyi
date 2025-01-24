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
                                body: GoogleCloudDiscoveryengineV1Document = ...,
                                documentId: str = ...,
                                **kwargs: typing.Any,
                            ) -> GoogleCloudDiscoveryengineV1DocumentHttpRequest: ...
                            def delete(
                                self, *, name: str, **kwargs: typing.Any
                            ) -> GoogleProtobufEmptyHttpRequest: ...
                            def get(
                                self, *, name: str, **kwargs: typing.Any
                            ) -> GoogleCloudDiscoveryengineV1DocumentHttpRequest: ...
                            def import_(
                                self,
                                *,
                                parent: str,
                                body: GoogleCloudDiscoveryengineV1ImportDocumentsRequest = ...,
                                **kwargs: typing.Any,
                            ) -> GoogleLongrunningOperationHttpRequest: ...
                            def list(
                                self,
                                *,
                                parent: str,
                                pageSize: int = ...,
                                pageToken: str = ...,
                                **kwargs: typing.Any,
                            ) -> GoogleCloudDiscoveryengineV1ListDocumentsResponseHttpRequest: ...
                            def list_next(
                                self,
                                previous_request: GoogleCloudDiscoveryengineV1ListDocumentsResponseHttpRequest,
                                previous_response: GoogleCloudDiscoveryengineV1ListDocumentsResponse,
                            ) -> (
                                GoogleCloudDiscoveryengineV1ListDocumentsResponseHttpRequest
                                | None
                            ): ...
                            def patch(
                                self,
                                *,
                                name: str,
                                body: GoogleCloudDiscoveryengineV1Document = ...,
                                allowMissing: bool = ...,
                                updateMask: str = ...,
                                **kwargs: typing.Any,
                            ) -> GoogleCloudDiscoveryengineV1DocumentHttpRequest: ...
                            def purge(
                                self,
                                *,
                                parent: str,
                                body: GoogleCloudDiscoveryengineV1PurgeDocumentsRequest = ...,
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

                        def batchGetDocumentsMetadata(
                            self,
                            *,
                            parent: str,
                            matcher_fhirMatcher_fhirResources: str | _list[str] = ...,
                            matcher_urisMatcher_uris: str | _list[str] = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudDiscoveryengineV1BatchGetDocumentsMetadataResponseHttpRequest: ...
                        def documents(self) -> DocumentsResource: ...
                        def operations(self) -> OperationsResource: ...

                    @typing.type_check_only
                    class CompletionSuggestionsResource(
                        googleapiclient.discovery.Resource
                    ):
                        def import_(
                            self,
                            *,
                            parent: str,
                            body: GoogleCloudDiscoveryengineV1ImportCompletionSuggestionsRequest = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleLongrunningOperationHttpRequest: ...
                        def purge(
                            self,
                            *,
                            parent: str,
                            body: GoogleCloudDiscoveryengineV1PurgeCompletionSuggestionsRequest = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleLongrunningOperationHttpRequest: ...

                    @typing.type_check_only
                    class ControlsResource(googleapiclient.discovery.Resource):
                        def create(
                            self,
                            *,
                            parent: str,
                            body: GoogleCloudDiscoveryengineV1Control = ...,
                            controlId: str = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudDiscoveryengineV1ControlHttpRequest: ...
                        def delete(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> GoogleProtobufEmptyHttpRequest: ...
                        def get(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> GoogleCloudDiscoveryengineV1ControlHttpRequest: ...
                        def list(
                            self,
                            *,
                            parent: str,
                            filter: str = ...,
                            pageSize: int = ...,
                            pageToken: str = ...,
                            **kwargs: typing.Any,
                        ) -> (
                            GoogleCloudDiscoveryengineV1ListControlsResponseHttpRequest
                        ): ...
                        def list_next(
                            self,
                            previous_request: GoogleCloudDiscoveryengineV1ListControlsResponseHttpRequest,
                            previous_response: GoogleCloudDiscoveryengineV1ListControlsResponse,
                        ) -> (
                            GoogleCloudDiscoveryengineV1ListControlsResponseHttpRequest
                            | None
                        ): ...
                        def patch(
                            self,
                            *,
                            name: str,
                            body: GoogleCloudDiscoveryengineV1Control = ...,
                            updateMask: str = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudDiscoveryengineV1ControlHttpRequest: ...

                    @typing.type_check_only
                    class ConversationsResource(googleapiclient.discovery.Resource):
                        def converse(
                            self,
                            *,
                            name: str,
                            body: GoogleCloudDiscoveryengineV1ConverseConversationRequest = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudDiscoveryengineV1ConverseConversationResponseHttpRequest: ...
                        def create(
                            self,
                            *,
                            parent: str,
                            body: GoogleCloudDiscoveryengineV1Conversation = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudDiscoveryengineV1ConversationHttpRequest: ...
                        def delete(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> GoogleProtobufEmptyHttpRequest: ...
                        def get(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> GoogleCloudDiscoveryengineV1ConversationHttpRequest: ...
                        def list(
                            self,
                            *,
                            parent: str,
                            filter: str = ...,
                            orderBy: str = ...,
                            pageSize: int = ...,
                            pageToken: str = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudDiscoveryengineV1ListConversationsResponseHttpRequest: ...
                        def list_next(
                            self,
                            previous_request: GoogleCloudDiscoveryengineV1ListConversationsResponseHttpRequest,
                            previous_response: GoogleCloudDiscoveryengineV1ListConversationsResponse,
                        ) -> (
                            GoogleCloudDiscoveryengineV1ListConversationsResponseHttpRequest
                            | None
                        ): ...
                        def patch(
                            self,
                            *,
                            name: str,
                            body: GoogleCloudDiscoveryengineV1Conversation = ...,
                            updateMask: str = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudDiscoveryengineV1ConversationHttpRequest: ...

                    @typing.type_check_only
                    class CustomModelsResource(googleapiclient.discovery.Resource):
                        def list(
                            self, *, dataStore: str, **kwargs: typing.Any
                        ) -> GoogleCloudDiscoveryengineV1ListCustomModelsResponseHttpRequest: ...

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
                            body: GoogleCloudDiscoveryengineV1Schema = ...,
                            schemaId: str = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleLongrunningOperationHttpRequest: ...
                        def delete(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> GoogleLongrunningOperationHttpRequest: ...
                        def get(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> GoogleCloudDiscoveryengineV1SchemaHttpRequest: ...
                        def list(
                            self,
                            *,
                            parent: str,
                            pageSize: int = ...,
                            pageToken: str = ...,
                            **kwargs: typing.Any,
                        ) -> (
                            GoogleCloudDiscoveryengineV1ListSchemasResponseHttpRequest
                        ): ...
                        def list_next(
                            self,
                            previous_request: GoogleCloudDiscoveryengineV1ListSchemasResponseHttpRequest,
                            previous_response: GoogleCloudDiscoveryengineV1ListSchemasResponse,
                        ) -> (
                            GoogleCloudDiscoveryengineV1ListSchemasResponseHttpRequest
                            | None
                        ): ...
                        def patch(
                            self,
                            *,
                            name: str,
                            body: GoogleCloudDiscoveryengineV1Schema = ...,
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
                            body: GoogleCloudDiscoveryengineV1AnswerQueryRequest = ...,
                            **kwargs: typing.Any,
                        ) -> (
                            GoogleCloudDiscoveryengineV1AnswerQueryResponseHttpRequest
                        ): ...
                        def patch(
                            self,
                            *,
                            name: str,
                            body: GoogleCloudDiscoveryengineV1ServingConfig = ...,
                            updateMask: str = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudDiscoveryengineV1ServingConfigHttpRequest: ...
                        def recommend(
                            self,
                            *,
                            servingConfig: str,
                            body: GoogleCloudDiscoveryengineV1RecommendRequest = ...,
                            **kwargs: typing.Any,
                        ) -> (
                            GoogleCloudDiscoveryengineV1RecommendResponseHttpRequest
                        ): ...
                        def search(
                            self,
                            *,
                            servingConfig: str,
                            body: GoogleCloudDiscoveryengineV1SearchRequest = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudDiscoveryengineV1SearchResponseHttpRequest: ...
                        def search_next(
                            self,
                            previous_request: GoogleCloudDiscoveryengineV1SearchResponseHttpRequest,
                            previous_response: GoogleCloudDiscoveryengineV1SearchResponse,
                        ) -> (
                            GoogleCloudDiscoveryengineV1SearchResponseHttpRequest | None
                        ): ...
                        def searchLite(
                            self,
                            *,
                            servingConfig: str,
                            body: GoogleCloudDiscoveryengineV1SearchRequest = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudDiscoveryengineV1SearchResponseHttpRequest: ...
                        def searchLite_next(
                            self,
                            previous_request: GoogleCloudDiscoveryengineV1SearchResponseHttpRequest,
                            previous_response: GoogleCloudDiscoveryengineV1SearchResponse,
                        ) -> (
                            GoogleCloudDiscoveryengineV1SearchResponseHttpRequest | None
                        ): ...
                        def streamAnswer(
                            self,
                            *,
                            servingConfig: str,
                            body: GoogleCloudDiscoveryengineV1AnswerQueryRequest = ...,
                            **kwargs: typing.Any,
                        ) -> (
                            GoogleCloudDiscoveryengineV1AnswerQueryResponseHttpRequest
                        ): ...

                    @typing.type_check_only
                    class SessionsResource(googleapiclient.discovery.Resource):
                        @typing.type_check_only
                        class AnswersResource(googleapiclient.discovery.Resource):
                            def get(
                                self, *, name: str, **kwargs: typing.Any
                            ) -> GoogleCloudDiscoveryengineV1AnswerHttpRequest: ...

                        def create(
                            self,
                            *,
                            parent: str,
                            body: GoogleCloudDiscoveryengineV1Session = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudDiscoveryengineV1SessionHttpRequest: ...
                        def delete(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> GoogleProtobufEmptyHttpRequest: ...
                        def get(
                            self,
                            *,
                            name: str,
                            includeAnswerDetails: bool = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudDiscoveryengineV1SessionHttpRequest: ...
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
                            GoogleCloudDiscoveryengineV1ListSessionsResponseHttpRequest
                        ): ...
                        def list_next(
                            self,
                            previous_request: GoogleCloudDiscoveryengineV1ListSessionsResponseHttpRequest,
                            previous_response: GoogleCloudDiscoveryengineV1ListSessionsResponse,
                        ) -> (
                            GoogleCloudDiscoveryengineV1ListSessionsResponseHttpRequest
                            | None
                        ): ...
                        def patch(
                            self,
                            *,
                            name: str,
                            body: GoogleCloudDiscoveryengineV1Session = ...,
                            updateMask: str = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudDiscoveryengineV1SessionHttpRequest: ...
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
                                body: GoogleCloudDiscoveryengineV1BatchCreateTargetSitesRequest = ...,
                                **kwargs: typing.Any,
                            ) -> GoogleLongrunningOperationHttpRequest: ...
                            def create(
                                self,
                                *,
                                parent: str,
                                body: GoogleCloudDiscoveryengineV1TargetSite = ...,
                                **kwargs: typing.Any,
                            ) -> GoogleLongrunningOperationHttpRequest: ...
                            def delete(
                                self, *, name: str, **kwargs: typing.Any
                            ) -> GoogleLongrunningOperationHttpRequest: ...
                            def get(
                                self, *, name: str, **kwargs: typing.Any
                            ) -> GoogleCloudDiscoveryengineV1TargetSiteHttpRequest: ...
                            def list(
                                self,
                                *,
                                parent: str,
                                pageSize: int = ...,
                                pageToken: str = ...,
                                **kwargs: typing.Any,
                            ) -> GoogleCloudDiscoveryengineV1ListTargetSitesResponseHttpRequest: ...
                            def list_next(
                                self,
                                previous_request: GoogleCloudDiscoveryengineV1ListTargetSitesResponseHttpRequest,
                                previous_response: GoogleCloudDiscoveryengineV1ListTargetSitesResponse,
                            ) -> (
                                GoogleCloudDiscoveryengineV1ListTargetSitesResponseHttpRequest
                                | None
                            ): ...
                            def patch(
                                self,
                                *,
                                name: str,
                                body: GoogleCloudDiscoveryengineV1TargetSite = ...,
                                **kwargs: typing.Any,
                            ) -> GoogleLongrunningOperationHttpRequest: ...
                            def operations(self) -> OperationsResource: ...

                        def batchVerifyTargetSites(
                            self,
                            *,
                            parent: str,
                            body: GoogleCloudDiscoveryengineV1BatchVerifyTargetSitesRequest = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleLongrunningOperationHttpRequest: ...
                        def disableAdvancedSiteSearch(
                            self,
                            *,
                            siteSearchEngine: str,
                            body: GoogleCloudDiscoveryengineV1DisableAdvancedSiteSearchRequest = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleLongrunningOperationHttpRequest: ...
                        def enableAdvancedSiteSearch(
                            self,
                            *,
                            siteSearchEngine: str,
                            body: GoogleCloudDiscoveryengineV1EnableAdvancedSiteSearchRequest = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleLongrunningOperationHttpRequest: ...
                        def fetchDomainVerificationStatus(
                            self,
                            *,
                            siteSearchEngine: str,
                            pageSize: int = ...,
                            pageToken: str = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudDiscoveryengineV1FetchDomainVerificationStatusResponseHttpRequest: ...
                        def fetchDomainVerificationStatus_next(
                            self,
                            previous_request: GoogleCloudDiscoveryengineV1FetchDomainVerificationStatusResponseHttpRequest,
                            previous_response: GoogleCloudDiscoveryengineV1FetchDomainVerificationStatusResponse,
                        ) -> (
                            GoogleCloudDiscoveryengineV1FetchDomainVerificationStatusResponseHttpRequest
                            | None
                        ): ...
                        def recrawlUris(
                            self,
                            *,
                            siteSearchEngine: str,
                            body: GoogleCloudDiscoveryengineV1RecrawlUrisRequest = ...,
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
                            body: GoogleCloudDiscoveryengineV1ImportSuggestionDenyListEntriesRequest = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleLongrunningOperationHttpRequest: ...
                        def purge(
                            self,
                            *,
                            parent: str,
                            body: GoogleCloudDiscoveryengineV1PurgeSuggestionDenyListEntriesRequest = ...,
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
                            body: GoogleCloudDiscoveryengineV1ImportUserEventsRequest = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleLongrunningOperationHttpRequest: ...
                        def purge(
                            self,
                            *,
                            parent: str,
                            body: GoogleCloudDiscoveryengineV1PurgeUserEventsRequest = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleLongrunningOperationHttpRequest: ...
                        def write(
                            self,
                            *,
                            parent: str,
                            body: GoogleCloudDiscoveryengineV1UserEvent = ...,
                            writeAsync: bool = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudDiscoveryengineV1UserEventHttpRequest: ...

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
                        GoogleCloudDiscoveryengineV1CompleteQueryResponseHttpRequest
                    ): ...
                    def create(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudDiscoveryengineV1DataStore = ...,
                        cmekConfigName: str = ...,
                        createAdvancedSiteSearch: bool = ...,
                        dataStoreId: str = ...,
                        disableCmek: bool = ...,
                        skipDefaultSchemaCreation: bool = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleCloudDiscoveryengineV1DataStoreHttpRequest: ...
                    def getSiteSearchEngine(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleCloudDiscoveryengineV1SiteSearchEngineHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
                    ) -> (
                        GoogleCloudDiscoveryengineV1ListDataStoresResponseHttpRequest
                    ): ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudDiscoveryengineV1ListDataStoresResponseHttpRequest,
                        previous_response: GoogleCloudDiscoveryengineV1ListDataStoresResponse,
                    ) -> (
                        GoogleCloudDiscoveryengineV1ListDataStoresResponseHttpRequest
                        | None
                    ): ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudDiscoveryengineV1DataStore = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudDiscoveryengineV1DataStoreHttpRequest: ...
                    def trainCustomModel(
                        self,
                        *,
                        dataStore: str,
                        body: GoogleCloudDiscoveryengineV1TrainCustomModelRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def branches(self) -> BranchesResource: ...
                    def completionSuggestions(
                        self,
                    ) -> CompletionSuggestionsResource: ...
                    def controls(self) -> ControlsResource: ...
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
                    class ControlsResource(googleapiclient.discovery.Resource):
                        def create(
                            self,
                            *,
                            parent: str,
                            body: GoogleCloudDiscoveryengineV1Control = ...,
                            controlId: str = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudDiscoveryengineV1ControlHttpRequest: ...
                        def delete(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> GoogleProtobufEmptyHttpRequest: ...
                        def get(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> GoogleCloudDiscoveryengineV1ControlHttpRequest: ...
                        def list(
                            self,
                            *,
                            parent: str,
                            filter: str = ...,
                            pageSize: int = ...,
                            pageToken: str = ...,
                            **kwargs: typing.Any,
                        ) -> (
                            GoogleCloudDiscoveryengineV1ListControlsResponseHttpRequest
                        ): ...
                        def list_next(
                            self,
                            previous_request: GoogleCloudDiscoveryengineV1ListControlsResponseHttpRequest,
                            previous_response: GoogleCloudDiscoveryengineV1ListControlsResponse,
                        ) -> (
                            GoogleCloudDiscoveryengineV1ListControlsResponseHttpRequest
                            | None
                        ): ...
                        def patch(
                            self,
                            *,
                            name: str,
                            body: GoogleCloudDiscoveryengineV1Control = ...,
                            updateMask: str = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudDiscoveryengineV1ControlHttpRequest: ...

                    @typing.type_check_only
                    class ConversationsResource(googleapiclient.discovery.Resource):
                        def converse(
                            self,
                            *,
                            name: str,
                            body: GoogleCloudDiscoveryengineV1ConverseConversationRequest = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudDiscoveryengineV1ConverseConversationResponseHttpRequest: ...
                        def create(
                            self,
                            *,
                            parent: str,
                            body: GoogleCloudDiscoveryengineV1Conversation = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudDiscoveryengineV1ConversationHttpRequest: ...
                        def delete(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> GoogleProtobufEmptyHttpRequest: ...
                        def get(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> GoogleCloudDiscoveryengineV1ConversationHttpRequest: ...
                        def list(
                            self,
                            *,
                            parent: str,
                            filter: str = ...,
                            orderBy: str = ...,
                            pageSize: int = ...,
                            pageToken: str = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudDiscoveryengineV1ListConversationsResponseHttpRequest: ...
                        def list_next(
                            self,
                            previous_request: GoogleCloudDiscoveryengineV1ListConversationsResponseHttpRequest,
                            previous_response: GoogleCloudDiscoveryengineV1ListConversationsResponse,
                        ) -> (
                            GoogleCloudDiscoveryengineV1ListConversationsResponseHttpRequest
                            | None
                        ): ...
                        def patch(
                            self,
                            *,
                            name: str,
                            body: GoogleCloudDiscoveryengineV1Conversation = ...,
                            updateMask: str = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudDiscoveryengineV1ConversationHttpRequest: ...

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
                            body: GoogleCloudDiscoveryengineV1AnswerQueryRequest = ...,
                            **kwargs: typing.Any,
                        ) -> (
                            GoogleCloudDiscoveryengineV1AnswerQueryResponseHttpRequest
                        ): ...
                        def patch(
                            self,
                            *,
                            name: str,
                            body: GoogleCloudDiscoveryengineV1ServingConfig = ...,
                            updateMask: str = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudDiscoveryengineV1ServingConfigHttpRequest: ...
                        def recommend(
                            self,
                            *,
                            servingConfig: str,
                            body: GoogleCloudDiscoveryengineV1RecommendRequest = ...,
                            **kwargs: typing.Any,
                        ) -> (
                            GoogleCloudDiscoveryengineV1RecommendResponseHttpRequest
                        ): ...
                        def search(
                            self,
                            *,
                            servingConfig: str,
                            body: GoogleCloudDiscoveryengineV1SearchRequest = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudDiscoveryengineV1SearchResponseHttpRequest: ...
                        def search_next(
                            self,
                            previous_request: GoogleCloudDiscoveryengineV1SearchResponseHttpRequest,
                            previous_response: GoogleCloudDiscoveryengineV1SearchResponse,
                        ) -> (
                            GoogleCloudDiscoveryengineV1SearchResponseHttpRequest | None
                        ): ...
                        def searchLite(
                            self,
                            *,
                            servingConfig: str,
                            body: GoogleCloudDiscoveryengineV1SearchRequest = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudDiscoveryengineV1SearchResponseHttpRequest: ...
                        def searchLite_next(
                            self,
                            previous_request: GoogleCloudDiscoveryengineV1SearchResponseHttpRequest,
                            previous_response: GoogleCloudDiscoveryengineV1SearchResponse,
                        ) -> (
                            GoogleCloudDiscoveryengineV1SearchResponseHttpRequest | None
                        ): ...
                        def streamAnswer(
                            self,
                            *,
                            servingConfig: str,
                            body: GoogleCloudDiscoveryengineV1AnswerQueryRequest = ...,
                            **kwargs: typing.Any,
                        ) -> (
                            GoogleCloudDiscoveryengineV1AnswerQueryResponseHttpRequest
                        ): ...

                    @typing.type_check_only
                    class SessionsResource(googleapiclient.discovery.Resource):
                        @typing.type_check_only
                        class AnswersResource(googleapiclient.discovery.Resource):
                            def get(
                                self, *, name: str, **kwargs: typing.Any
                            ) -> GoogleCloudDiscoveryengineV1AnswerHttpRequest: ...

                        def create(
                            self,
                            *,
                            parent: str,
                            body: GoogleCloudDiscoveryengineV1Session = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudDiscoveryengineV1SessionHttpRequest: ...
                        def delete(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> GoogleProtobufEmptyHttpRequest: ...
                        def get(
                            self,
                            *,
                            name: str,
                            includeAnswerDetails: bool = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudDiscoveryengineV1SessionHttpRequest: ...
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
                            GoogleCloudDiscoveryengineV1ListSessionsResponseHttpRequest
                        ): ...
                        def list_next(
                            self,
                            previous_request: GoogleCloudDiscoveryengineV1ListSessionsResponseHttpRequest,
                            previous_response: GoogleCloudDiscoveryengineV1ListSessionsResponse,
                        ) -> (
                            GoogleCloudDiscoveryengineV1ListSessionsResponseHttpRequest
                            | None
                        ): ...
                        def patch(
                            self,
                            *,
                            name: str,
                            body: GoogleCloudDiscoveryengineV1Session = ...,
                            updateMask: str = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudDiscoveryengineV1SessionHttpRequest: ...
                        def answers(self) -> AnswersResource: ...

                    def create(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudDiscoveryengineV1Engine = ...,
                        engineId: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleCloudDiscoveryengineV1EngineHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudDiscoveryengineV1ListEnginesResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudDiscoveryengineV1ListEnginesResponseHttpRequest,
                        previous_response: GoogleCloudDiscoveryengineV1ListEnginesResponse,
                    ) -> (
                        GoogleCloudDiscoveryengineV1ListEnginesResponseHttpRequest
                        | None
                    ): ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudDiscoveryengineV1Engine = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudDiscoveryengineV1EngineHttpRequest: ...
                    def controls(self) -> ControlsResource: ...
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
                            body: GoogleCloudDiscoveryengineV1Document = ...,
                            documentId: str = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudDiscoveryengineV1DocumentHttpRequest: ...
                        def delete(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> GoogleProtobufEmptyHttpRequest: ...
                        def get(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> GoogleCloudDiscoveryengineV1DocumentHttpRequest: ...
                        def import_(
                            self,
                            *,
                            parent: str,
                            body: GoogleCloudDiscoveryengineV1ImportDocumentsRequest = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleLongrunningOperationHttpRequest: ...
                        def list(
                            self,
                            *,
                            parent: str,
                            pageSize: int = ...,
                            pageToken: str = ...,
                            **kwargs: typing.Any,
                        ) -> (
                            GoogleCloudDiscoveryengineV1ListDocumentsResponseHttpRequest
                        ): ...
                        def list_next(
                            self,
                            previous_request: GoogleCloudDiscoveryengineV1ListDocumentsResponseHttpRequest,
                            previous_response: GoogleCloudDiscoveryengineV1ListDocumentsResponse,
                        ) -> (
                            GoogleCloudDiscoveryengineV1ListDocumentsResponseHttpRequest
                            | None
                        ): ...
                        def patch(
                            self,
                            *,
                            name: str,
                            body: GoogleCloudDiscoveryengineV1Document = ...,
                            allowMissing: bool = ...,
                            updateMask: str = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudDiscoveryengineV1DocumentHttpRequest: ...
                        def purge(
                            self,
                            *,
                            parent: str,
                            body: GoogleCloudDiscoveryengineV1PurgeDocumentsRequest = ...,
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

                    def batchGetDocumentsMetadata(
                        self,
                        *,
                        parent: str,
                        matcher_fhirMatcher_fhirResources: str | _list[str] = ...,
                        matcher_urisMatcher_uris: str | _list[str] = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudDiscoveryengineV1BatchGetDocumentsMetadataResponseHttpRequest: ...
                    def documents(self) -> DocumentsResource: ...
                    def operations(self) -> OperationsResource: ...

                @typing.type_check_only
                class CompletionSuggestionsResource(googleapiclient.discovery.Resource):
                    def import_(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudDiscoveryengineV1ImportCompletionSuggestionsRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def purge(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudDiscoveryengineV1PurgeCompletionSuggestionsRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleLongrunningOperationHttpRequest: ...

                @typing.type_check_only
                class ControlsResource(googleapiclient.discovery.Resource):
                    def create(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudDiscoveryengineV1Control = ...,
                        controlId: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudDiscoveryengineV1ControlHttpRequest: ...
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleProtobufEmptyHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleCloudDiscoveryengineV1ControlHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
                    ) -> (
                        GoogleCloudDiscoveryengineV1ListControlsResponseHttpRequest
                    ): ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudDiscoveryengineV1ListControlsResponseHttpRequest,
                        previous_response: GoogleCloudDiscoveryengineV1ListControlsResponse,
                    ) -> (
                        GoogleCloudDiscoveryengineV1ListControlsResponseHttpRequest
                        | None
                    ): ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudDiscoveryengineV1Control = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudDiscoveryengineV1ControlHttpRequest: ...

                @typing.type_check_only
                class ConversationsResource(googleapiclient.discovery.Resource):
                    def converse(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudDiscoveryengineV1ConverseConversationRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudDiscoveryengineV1ConverseConversationResponseHttpRequest: ...
                    def create(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudDiscoveryengineV1Conversation = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudDiscoveryengineV1ConversationHttpRequest: ...
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleProtobufEmptyHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleCloudDiscoveryengineV1ConversationHttpRequest: ...
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
                        GoogleCloudDiscoveryengineV1ListConversationsResponseHttpRequest
                    ): ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudDiscoveryengineV1ListConversationsResponseHttpRequest,
                        previous_response: GoogleCloudDiscoveryengineV1ListConversationsResponse,
                    ) -> (
                        GoogleCloudDiscoveryengineV1ListConversationsResponseHttpRequest
                        | None
                    ): ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudDiscoveryengineV1Conversation = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudDiscoveryengineV1ConversationHttpRequest: ...

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
                        body: GoogleCloudDiscoveryengineV1Schema = ...,
                        schemaId: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleCloudDiscoveryengineV1SchemaHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudDiscoveryengineV1ListSchemasResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudDiscoveryengineV1ListSchemasResponseHttpRequest,
                        previous_response: GoogleCloudDiscoveryengineV1ListSchemasResponse,
                    ) -> (
                        GoogleCloudDiscoveryengineV1ListSchemasResponseHttpRequest
                        | None
                    ): ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudDiscoveryengineV1Schema = ...,
                        allowMissing: bool = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleLongrunningOperationHttpRequest: ...

                @typing.type_check_only
                class ServingConfigsResource(googleapiclient.discovery.Resource):
                    def answer(
                        self,
                        *,
                        servingConfig: str,
                        body: GoogleCloudDiscoveryengineV1AnswerQueryRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudDiscoveryengineV1AnswerQueryResponseHttpRequest: ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudDiscoveryengineV1ServingConfig = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudDiscoveryengineV1ServingConfigHttpRequest: ...
                    def recommend(
                        self,
                        *,
                        servingConfig: str,
                        body: GoogleCloudDiscoveryengineV1RecommendRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudDiscoveryengineV1RecommendResponseHttpRequest: ...
                    def search(
                        self,
                        *,
                        servingConfig: str,
                        body: GoogleCloudDiscoveryengineV1SearchRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudDiscoveryengineV1SearchResponseHttpRequest: ...
                    def search_next(
                        self,
                        previous_request: GoogleCloudDiscoveryengineV1SearchResponseHttpRequest,
                        previous_response: GoogleCloudDiscoveryengineV1SearchResponse,
                    ) -> (
                        GoogleCloudDiscoveryengineV1SearchResponseHttpRequest | None
                    ): ...
                    def searchLite(
                        self,
                        *,
                        servingConfig: str,
                        body: GoogleCloudDiscoveryengineV1SearchRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudDiscoveryengineV1SearchResponseHttpRequest: ...
                    def searchLite_next(
                        self,
                        previous_request: GoogleCloudDiscoveryengineV1SearchResponseHttpRequest,
                        previous_response: GoogleCloudDiscoveryengineV1SearchResponse,
                    ) -> (
                        GoogleCloudDiscoveryengineV1SearchResponseHttpRequest | None
                    ): ...
                    def streamAnswer(
                        self,
                        *,
                        servingConfig: str,
                        body: GoogleCloudDiscoveryengineV1AnswerQueryRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudDiscoveryengineV1AnswerQueryResponseHttpRequest: ...

                @typing.type_check_only
                class SessionsResource(googleapiclient.discovery.Resource):
                    @typing.type_check_only
                    class AnswersResource(googleapiclient.discovery.Resource):
                        def get(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> GoogleCloudDiscoveryengineV1AnswerHttpRequest: ...

                    def create(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudDiscoveryengineV1Session = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudDiscoveryengineV1SessionHttpRequest: ...
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleProtobufEmptyHttpRequest: ...
                    def get(
                        self,
                        *,
                        name: str,
                        includeAnswerDetails: bool = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudDiscoveryengineV1SessionHttpRequest: ...
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
                        GoogleCloudDiscoveryengineV1ListSessionsResponseHttpRequest
                    ): ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudDiscoveryengineV1ListSessionsResponseHttpRequest,
                        previous_response: GoogleCloudDiscoveryengineV1ListSessionsResponse,
                    ) -> (
                        GoogleCloudDiscoveryengineV1ListSessionsResponseHttpRequest
                        | None
                    ): ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudDiscoveryengineV1Session = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudDiscoveryengineV1SessionHttpRequest: ...
                    def answers(self) -> AnswersResource: ...

                @typing.type_check_only
                class SiteSearchEngineResource(googleapiclient.discovery.Resource):
                    @typing.type_check_only
                    class TargetSitesResource(googleapiclient.discovery.Resource):
                        def batchCreate(
                            self,
                            *,
                            parent: str,
                            body: GoogleCloudDiscoveryengineV1BatchCreateTargetSitesRequest = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleLongrunningOperationHttpRequest: ...
                        def create(
                            self,
                            *,
                            parent: str,
                            body: GoogleCloudDiscoveryengineV1TargetSite = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleLongrunningOperationHttpRequest: ...
                        def delete(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> GoogleLongrunningOperationHttpRequest: ...
                        def get(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> GoogleCloudDiscoveryengineV1TargetSiteHttpRequest: ...
                        def list(
                            self,
                            *,
                            parent: str,
                            pageSize: int = ...,
                            pageToken: str = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudDiscoveryengineV1ListTargetSitesResponseHttpRequest: ...
                        def list_next(
                            self,
                            previous_request: GoogleCloudDiscoveryengineV1ListTargetSitesResponseHttpRequest,
                            previous_response: GoogleCloudDiscoveryengineV1ListTargetSitesResponse,
                        ) -> (
                            GoogleCloudDiscoveryengineV1ListTargetSitesResponseHttpRequest
                            | None
                        ): ...
                        def patch(
                            self,
                            *,
                            name: str,
                            body: GoogleCloudDiscoveryengineV1TargetSite = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleLongrunningOperationHttpRequest: ...

                    def disableAdvancedSiteSearch(
                        self,
                        *,
                        siteSearchEngine: str,
                        body: GoogleCloudDiscoveryengineV1DisableAdvancedSiteSearchRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def enableAdvancedSiteSearch(
                        self,
                        *,
                        siteSearchEngine: str,
                        body: GoogleCloudDiscoveryengineV1EnableAdvancedSiteSearchRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def recrawlUris(
                        self,
                        *,
                        siteSearchEngine: str,
                        body: GoogleCloudDiscoveryengineV1RecrawlUrisRequest = ...,
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
                        body: GoogleCloudDiscoveryengineV1ImportSuggestionDenyListEntriesRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def purge(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudDiscoveryengineV1PurgeSuggestionDenyListEntriesRequest = ...,
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
                        body: GoogleCloudDiscoveryengineV1ImportUserEventsRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def purge(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudDiscoveryengineV1PurgeUserEventsRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def write(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudDiscoveryengineV1UserEvent = ...,
                        writeAsync: bool = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudDiscoveryengineV1UserEventHttpRequest: ...

                def completeQuery(
                    self,
                    *,
                    dataStore: str,
                    includeTailSuggestions: bool = ...,
                    query: str = ...,
                    queryModel: str = ...,
                    userPseudoId: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudDiscoveryengineV1CompleteQueryResponseHttpRequest: ...
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudDiscoveryengineV1DataStore = ...,
                    cmekConfigName: str = ...,
                    createAdvancedSiteSearch: bool = ...,
                    dataStoreId: str = ...,
                    disableCmek: bool = ...,
                    skipDefaultSchemaCreation: bool = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudDiscoveryengineV1DataStoreHttpRequest: ...
                def getSiteSearchEngine(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudDiscoveryengineV1SiteSearchEngineHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudDiscoveryengineV1ListDataStoresResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudDiscoveryengineV1ListDataStoresResponseHttpRequest,
                    previous_response: GoogleCloudDiscoveryengineV1ListDataStoresResponse,
                ) -> (
                    GoogleCloudDiscoveryengineV1ListDataStoresResponseHttpRequest | None
                ): ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudDiscoveryengineV1DataStore = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudDiscoveryengineV1DataStoreHttpRequest: ...
                def branches(self) -> BranchesResource: ...
                def completionSuggestions(self) -> CompletionSuggestionsResource: ...
                def controls(self) -> ControlsResource: ...
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
                    body: GoogleCloudDiscoveryengineV1CheckGroundingRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudDiscoveryengineV1CheckGroundingResponseHttpRequest: ...

            @typing.type_check_only
            class IdentityMappingStoresResource(googleapiclient.discovery.Resource):
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
            class RankingConfigsResource(googleapiclient.discovery.Resource):
                def rank(
                    self,
                    *,
                    rankingConfig: str,
                    body: GoogleCloudDiscoveryengineV1RankRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudDiscoveryengineV1RankResponseHttpRequest: ...

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
                    body: GoogleCloudDiscoveryengineV1ImportUserEventsRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def write(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudDiscoveryengineV1UserEvent = ...,
                    writeAsync: bool = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudDiscoveryengineV1UserEventHttpRequest: ...

            def generateGroundedContent(
                self,
                *,
                location: str,
                body: GoogleCloudDiscoveryengineV1GenerateGroundedContentRequest = ...,
                **kwargs: typing.Any,
            ) -> (
                GoogleCloudDiscoveryengineV1GenerateGroundedContentResponseHttpRequest
            ): ...
            def collections(self) -> CollectionsResource: ...
            def dataStores(self) -> DataStoresResource: ...
            def groundingConfigs(self) -> GroundingConfigsResource: ...
            def identityMappingStores(self) -> IdentityMappingStoresResource: ...
            def operations(self) -> OperationsResource: ...
            def rankingConfigs(self) -> RankingConfigsResource: ...
            def userEvents(self) -> UserEventsResource: ...

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
            ) -> GoogleLongrunningListOperationsResponseHttpRequest | None: ...

        def provision(
            self,
            *,
            name: str,
            body: GoogleCloudDiscoveryengineV1ProvisionProjectRequest = ...,
            **kwargs: typing.Any,
        ) -> GoogleLongrunningOperationHttpRequest: ...
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
class GoogleCloudDiscoveryengineV1AnswerHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDiscoveryengineV1Answer: ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1AnswerQueryResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDiscoveryengineV1AnswerQueryResponse: ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1BatchGetDocumentsMetadataResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDiscoveryengineV1BatchGetDocumentsMetadataResponse: ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1CheckGroundingResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDiscoveryengineV1CheckGroundingResponse: ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1CompleteQueryResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDiscoveryengineV1CompleteQueryResponse: ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1ControlHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDiscoveryengineV1Control: ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1ConversationHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDiscoveryengineV1Conversation: ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1ConverseConversationResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDiscoveryengineV1ConverseConversationResponse: ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1DataStoreHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDiscoveryengineV1DataStore: ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1DocumentHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDiscoveryengineV1Document: ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1EngineHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDiscoveryengineV1Engine: ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1FetchDomainVerificationStatusResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDiscoveryengineV1FetchDomainVerificationStatusResponse: ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1GenerateGroundedContentResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDiscoveryengineV1GenerateGroundedContentResponse: ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1ListControlsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDiscoveryengineV1ListControlsResponse: ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1ListConversationsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDiscoveryengineV1ListConversationsResponse: ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1ListCustomModelsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDiscoveryengineV1ListCustomModelsResponse: ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1ListDataStoresResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDiscoveryengineV1ListDataStoresResponse: ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1ListDocumentsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDiscoveryengineV1ListDocumentsResponse: ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1ListEnginesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDiscoveryengineV1ListEnginesResponse: ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1ListSchemasResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDiscoveryengineV1ListSchemasResponse: ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1ListSessionsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDiscoveryengineV1ListSessionsResponse: ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1ListTargetSitesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDiscoveryengineV1ListTargetSitesResponse: ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1RankResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDiscoveryengineV1RankResponse: ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1RecommendResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDiscoveryengineV1RecommendResponse: ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1SchemaHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDiscoveryengineV1Schema: ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1SearchResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDiscoveryengineV1SearchResponse: ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1ServingConfigHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDiscoveryengineV1ServingConfig: ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1SessionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDiscoveryengineV1Session: ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1SiteSearchEngineHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDiscoveryengineV1SiteSearchEngine: ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1TargetSiteHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDiscoveryengineV1TargetSite: ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1UserEventHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDiscoveryengineV1UserEvent: ...

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
