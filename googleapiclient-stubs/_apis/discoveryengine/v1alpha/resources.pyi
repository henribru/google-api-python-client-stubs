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
    class BillingAccountsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class BillingAccountLicenseConfigsResource(googleapiclient.discovery.Resource):
            def distributeLicenseConfig(
                self,
                *,
                billingAccountLicenseConfig: str,
                body: GoogleCloudDiscoveryengineV1alphaDistributeLicenseConfigRequest = ...,
                **kwargs: typing.Any,
            ) -> GoogleCloudDiscoveryengineV1alphaDistributeLicenseConfigResponseHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> (
                GoogleCloudDiscoveryengineV1alphaBillingAccountLicenseConfigHttpRequest
            ): ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any,
            ) -> GoogleCloudDiscoveryengineV1alphaListBillingAccountLicenseConfigsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: GoogleCloudDiscoveryengineV1alphaListBillingAccountLicenseConfigsResponseHttpRequest,
                previous_response: GoogleCloudDiscoveryengineV1alphaListBillingAccountLicenseConfigsResponse,
            ) -> (
                GoogleCloudDiscoveryengineV1alphaListBillingAccountLicenseConfigsResponseHttpRequest
                | None
            ): ...
            def retractLicenseConfig(
                self,
                *,
                billingAccountLicenseConfig: str,
                body: GoogleCloudDiscoveryengineV1alphaRetractLicenseConfigRequest = ...,
                **kwargs: typing.Any,
            ) -> (
                GoogleCloudDiscoveryengineV1alphaRetractLicenseConfigResponseHttpRequest
            ): ...

        def billingAccountLicenseConfigs(
            self,
        ) -> BillingAccountLicenseConfigsResource: ...

    @typing.type_check_only
    class ProjectsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class LocationsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class AuthorizationsResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudDiscoveryengineV1alphaAuthorization = ...,
                    authorizationId: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudDiscoveryengineV1alphaAuthorizationHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleProtobufEmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudDiscoveryengineV1alphaAuthorizationHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudDiscoveryengineV1alphaListAuthorizationsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudDiscoveryengineV1alphaListAuthorizationsResponseHttpRequest,
                    previous_response: GoogleCloudDiscoveryengineV1alphaListAuthorizationsResponse,
                ) -> (
                    GoogleCloudDiscoveryengineV1alphaListAuthorizationsResponseHttpRequest
                    | None
                ): ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudDiscoveryengineV1alphaAuthorization = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudDiscoveryengineV1alphaAuthorizationHttpRequest: ...

            @typing.type_check_only
            class CmekConfigsResource(googleapiclient.discovery.Resource):
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudDiscoveryengineV1alphaCmekConfigHttpRequest: ...
                def list(
                    self, *, parent: str, **kwargs: typing.Any
                ) -> (
                    GoogleCloudDiscoveryengineV1alphaListCmekConfigsResponseHttpRequest
                ): ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudDiscoveryengineV1alphaCmekConfig = ...,
                    setDefault: bool = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...

            @typing.type_check_only
            class CollectionsResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class DataConnectorResource(googleapiclient.discovery.Resource):
                    @typing.type_check_only
                    class ConnectorRunsResource(googleapiclient.discovery.Resource):
                        def list(
                            self,
                            *,
                            parent: str,
                            pageSize: int = ...,
                            pageToken: str = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudDiscoveryengineV1alphaListConnectorRunsResponseHttpRequest: ...
                        def list_next(
                            self,
                            previous_request: GoogleCloudDiscoveryengineV1alphaListConnectorRunsResponseHttpRequest,
                            previous_response: GoogleCloudDiscoveryengineV1alphaListConnectorRunsResponse,
                        ) -> (
                            GoogleCloudDiscoveryengineV1alphaListConnectorRunsResponseHttpRequest
                            | None
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
                            returnPartialSuccess: bool = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleLongrunningListOperationsResponseHttpRequest: ...
                        def list_next(
                            self,
                            previous_request: GoogleLongrunningListOperationsResponseHttpRequest,
                            previous_response: GoogleLongrunningListOperationsResponse,
                        ) -> (
                            GoogleLongrunningListOperationsResponseHttpRequest | None
                        ): ...

                    def acquireAccessToken(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudDiscoveryengineV1alphaAcquireAccessTokenRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudDiscoveryengineV1alphaAcquireAccessTokenResponseHttpRequest: ...
                    def checkRefreshToken(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleCloudDiscoveryengineV1alphaCheckRefreshTokenResponseHttpRequest: ...
                    def getConnectorSecret(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleCloudDiscoveryengineV1alphaGetConnectorSecretResponseHttpRequest: ...
                    def startConnectorRun(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudDiscoveryengineV1alphaStartConnectorRunRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudDiscoveryengineV1alphaConnectorRunHttpRequest: ...
                    def connectorRuns(self) -> ConnectorRunsResource: ...
                    def operations(self) -> OperationsResource: ...

                @typing.type_check_only
                class DataStoresResource(googleapiclient.discovery.Resource):
                    @typing.type_check_only
                    class BranchesResource(googleapiclient.discovery.Resource):
                        @typing.type_check_only
                        class DocumentsResource(googleapiclient.discovery.Resource):
                            @typing.type_check_only
                            class ChunksResource(googleapiclient.discovery.Resource):
                                def get(
                                    self, *, name: str, **kwargs: typing.Any
                                ) -> (
                                    GoogleCloudDiscoveryengineV1alphaChunkHttpRequest
                                ): ...
                                def list(
                                    self,
                                    *,
                                    parent: str,
                                    pageSize: int = ...,
                                    pageToken: str = ...,
                                    **kwargs: typing.Any,
                                ) -> GoogleCloudDiscoveryengineV1alphaListChunksResponseHttpRequest: ...
                                def list_next(
                                    self,
                                    previous_request: GoogleCloudDiscoveryengineV1alphaListChunksResponseHttpRequest,
                                    previous_response: GoogleCloudDiscoveryengineV1alphaListChunksResponse,
                                ) -> (
                                    GoogleCloudDiscoveryengineV1alphaListChunksResponseHttpRequest
                                    | None
                                ): ...

                            def create(
                                self,
                                *,
                                parent: str,
                                body: GoogleCloudDiscoveryengineV1alphaDocument = ...,
                                documentId: str = ...,
                                **kwargs: typing.Any,
                            ) -> (
                                GoogleCloudDiscoveryengineV1alphaDocumentHttpRequest
                            ): ...
                            def delete(
                                self, *, name: str, **kwargs: typing.Any
                            ) -> GoogleProtobufEmptyHttpRequest: ...
                            def get(
                                self, *, name: str, **kwargs: typing.Any
                            ) -> (
                                GoogleCloudDiscoveryengineV1alphaDocumentHttpRequest
                            ): ...
                            def getProcessedDocument(
                                self,
                                *,
                                name: str,
                                imageId: str = ...,
                                processedDocumentFormat: typing_extensions.Literal[
                                    "PROCESSED_DOCUMENT_FORMAT_UNSPECIFIED", "JSON"
                                ] = ...,
                                processedDocumentType: typing_extensions.Literal[
                                    "PROCESSED_DOCUMENT_TYPE_UNSPECIFIED",
                                    "PARSED_DOCUMENT",
                                    "CHUNKED_DOCUMENT",
                                    "IMAGE_CONVERTED_DOCUMENT",
                                    "IMAGE_BYTES",
                                ] = ...,
                                **kwargs: typing.Any,
                            ) -> GoogleCloudDiscoveryengineV1alphaProcessedDocumentHttpRequest: ...
                            def import_(
                                self,
                                *,
                                parent: str,
                                body: GoogleCloudDiscoveryengineV1alphaImportDocumentsRequest = ...,
                                **kwargs: typing.Any,
                            ) -> GoogleLongrunningOperationHttpRequest: ...
                            def list(
                                self,
                                *,
                                parent: str,
                                pageSize: int = ...,
                                pageToken: str = ...,
                                **kwargs: typing.Any,
                            ) -> GoogleCloudDiscoveryengineV1alphaListDocumentsResponseHttpRequest: ...
                            def list_next(
                                self,
                                previous_request: GoogleCloudDiscoveryengineV1alphaListDocumentsResponseHttpRequest,
                                previous_response: GoogleCloudDiscoveryengineV1alphaListDocumentsResponse,
                            ) -> (
                                GoogleCloudDiscoveryengineV1alphaListDocumentsResponseHttpRequest
                                | None
                            ): ...
                            def patch(
                                self,
                                *,
                                name: str,
                                body: GoogleCloudDiscoveryengineV1alphaDocument = ...,
                                allowMissing: bool = ...,
                                updateMask: str = ...,
                                **kwargs: typing.Any,
                            ) -> (
                                GoogleCloudDiscoveryengineV1alphaDocumentHttpRequest
                            ): ...
                            def purge(
                                self,
                                *,
                                parent: str,
                                body: GoogleCloudDiscoveryengineV1alphaPurgeDocumentsRequest = ...,
                                **kwargs: typing.Any,
                            ) -> GoogleLongrunningOperationHttpRequest: ...
                            def chunks(self) -> ChunksResource: ...

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
                                returnPartialSuccess: bool = ...,
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
                        ) -> GoogleCloudDiscoveryengineV1alphaBatchGetDocumentsMetadataResponseHttpRequest: ...
                        def get(
                            self,
                            *,
                            name: str,
                            view: typing_extensions.Literal[
                                "BRANCH_VIEW_UNSPECIFIED",
                                "BRANCH_VIEW_BASIC",
                                "BRANCH_VIEW_FULL",
                            ] = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudDiscoveryengineV1alphaBranchHttpRequest: ...
                        def list(
                            self,
                            *,
                            parent: str,
                            view: typing_extensions.Literal[
                                "BRANCH_VIEW_UNSPECIFIED",
                                "BRANCH_VIEW_BASIC",
                                "BRANCH_VIEW_FULL",
                            ] = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudDiscoveryengineV1alphaListBranchesResponseHttpRequest: ...
                        def documents(self) -> DocumentsResource: ...
                        def operations(self) -> OperationsResource: ...

                    @typing.type_check_only
                    class CompletionConfigResource(googleapiclient.discovery.Resource):
                        def completeQuery(
                            self,
                            *,
                            completionConfig: str,
                            body: GoogleCloudDiscoveryengineV1alphaAdvancedCompleteQueryRequest = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudDiscoveryengineV1alphaAdvancedCompleteQueryResponseHttpRequest: ...

                    @typing.type_check_only
                    class CompletionSuggestionsResource(
                        googleapiclient.discovery.Resource
                    ):
                        def import_(
                            self,
                            *,
                            parent: str,
                            body: GoogleCloudDiscoveryengineV1alphaImportCompletionSuggestionsRequest = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleLongrunningOperationHttpRequest: ...
                        def purge(
                            self,
                            *,
                            parent: str,
                            body: GoogleCloudDiscoveryengineV1alphaPurgeCompletionSuggestionsRequest = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleLongrunningOperationHttpRequest: ...

                    @typing.type_check_only
                    class ControlsResource(googleapiclient.discovery.Resource):
                        def create(
                            self,
                            *,
                            parent: str,
                            body: GoogleCloudDiscoveryengineV1alphaControl = ...,
                            controlId: str = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudDiscoveryengineV1alphaControlHttpRequest: ...
                        def delete(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> GoogleProtobufEmptyHttpRequest: ...
                        def get(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> GoogleCloudDiscoveryengineV1alphaControlHttpRequest: ...
                        def list(
                            self,
                            *,
                            parent: str,
                            filter: str = ...,
                            pageSize: int = ...,
                            pageToken: str = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudDiscoveryengineV1alphaListControlsResponseHttpRequest: ...
                        def list_next(
                            self,
                            previous_request: GoogleCloudDiscoveryengineV1alphaListControlsResponseHttpRequest,
                            previous_response: GoogleCloudDiscoveryengineV1alphaListControlsResponse,
                        ) -> (
                            GoogleCloudDiscoveryengineV1alphaListControlsResponseHttpRequest
                            | None
                        ): ...
                        def patch(
                            self,
                            *,
                            name: str,
                            body: GoogleCloudDiscoveryengineV1alphaControl = ...,
                            updateMask: str = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudDiscoveryengineV1alphaControlHttpRequest: ...

                    @typing.type_check_only
                    class ConversationsResource(googleapiclient.discovery.Resource):
                        def converse(
                            self,
                            *,
                            name: str,
                            body: GoogleCloudDiscoveryengineV1alphaConverseConversationRequest = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudDiscoveryengineV1alphaConverseConversationResponseHttpRequest: ...
                        def create(
                            self,
                            *,
                            parent: str,
                            body: GoogleCloudDiscoveryengineV1alphaConversation = ...,
                            **kwargs: typing.Any,
                        ) -> (
                            GoogleCloudDiscoveryengineV1alphaConversationHttpRequest
                        ): ...
                        def delete(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> GoogleProtobufEmptyHttpRequest: ...
                        def get(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> (
                            GoogleCloudDiscoveryengineV1alphaConversationHttpRequest
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
                        ) -> GoogleCloudDiscoveryengineV1alphaListConversationsResponseHttpRequest: ...
                        def list_next(
                            self,
                            previous_request: GoogleCloudDiscoveryengineV1alphaListConversationsResponseHttpRequest,
                            previous_response: GoogleCloudDiscoveryengineV1alphaListConversationsResponse,
                        ) -> (
                            GoogleCloudDiscoveryengineV1alphaListConversationsResponseHttpRequest
                            | None
                        ): ...
                        def patch(
                            self,
                            *,
                            name: str,
                            body: GoogleCloudDiscoveryengineV1alphaConversation = ...,
                            updateMask: str = ...,
                            **kwargs: typing.Any,
                        ) -> (
                            GoogleCloudDiscoveryengineV1alphaConversationHttpRequest
                        ): ...

                    @typing.type_check_only
                    class CustomModelsResource(googleapiclient.discovery.Resource):
                        def list(
                            self, *, dataStore: str, **kwargs: typing.Any
                        ) -> GoogleCloudDiscoveryengineV1alphaListCustomModelsResponseHttpRequest: ...

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
                                returnPartialSuccess: bool = ...,
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
                            returnPartialSuccess: bool = ...,
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
                                returnPartialSuccess: bool = ...,
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
                            body: GoogleCloudDiscoveryengineV1alphaSchema = ...,
                            schemaId: str = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleLongrunningOperationHttpRequest: ...
                        def delete(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> GoogleLongrunningOperationHttpRequest: ...
                        def get(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> GoogleCloudDiscoveryengineV1alphaSchemaHttpRequest: ...
                        def list(
                            self,
                            *,
                            parent: str,
                            pageSize: int = ...,
                            pageToken: str = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudDiscoveryengineV1alphaListSchemasResponseHttpRequest: ...
                        def list_next(
                            self,
                            previous_request: GoogleCloudDiscoveryengineV1alphaListSchemasResponseHttpRequest,
                            previous_response: GoogleCloudDiscoveryengineV1alphaListSchemasResponse,
                        ) -> (
                            GoogleCloudDiscoveryengineV1alphaListSchemasResponseHttpRequest
                            | None
                        ): ...
                        def patch(
                            self,
                            *,
                            name: str,
                            body: GoogleCloudDiscoveryengineV1alphaSchema = ...,
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
                            body: GoogleCloudDiscoveryengineV1alphaAnswerQueryRequest = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudDiscoveryengineV1alphaAnswerQueryResponseHttpRequest: ...
                        def create(
                            self,
                            *,
                            parent: str,
                            body: GoogleCloudDiscoveryengineV1alphaServingConfig = ...,
                            servingConfigId: str = ...,
                            **kwargs: typing.Any,
                        ) -> (
                            GoogleCloudDiscoveryengineV1alphaServingConfigHttpRequest
                        ): ...
                        def delete(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> GoogleProtobufEmptyHttpRequest: ...
                        def get(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> (
                            GoogleCloudDiscoveryengineV1alphaServingConfigHttpRequest
                        ): ...
                        def list(
                            self,
                            *,
                            parent: str,
                            pageSize: int = ...,
                            pageToken: str = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudDiscoveryengineV1alphaListServingConfigsResponseHttpRequest: ...
                        def list_next(
                            self,
                            previous_request: GoogleCloudDiscoveryengineV1alphaListServingConfigsResponseHttpRequest,
                            previous_response: GoogleCloudDiscoveryengineV1alphaListServingConfigsResponse,
                        ) -> (
                            GoogleCloudDiscoveryengineV1alphaListServingConfigsResponseHttpRequest
                            | None
                        ): ...
                        def patch(
                            self,
                            *,
                            name: str,
                            body: GoogleCloudDiscoveryengineV1alphaServingConfig = ...,
                            updateMask: str = ...,
                            **kwargs: typing.Any,
                        ) -> (
                            GoogleCloudDiscoveryengineV1alphaServingConfigHttpRequest
                        ): ...
                        def recommend(
                            self,
                            *,
                            servingConfig: str,
                            body: GoogleCloudDiscoveryengineV1alphaRecommendRequest = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudDiscoveryengineV1alphaRecommendResponseHttpRequest: ...
                        def search(
                            self,
                            *,
                            servingConfig: str,
                            body: GoogleCloudDiscoveryengineV1alphaSearchRequest = ...,
                            **kwargs: typing.Any,
                        ) -> (
                            GoogleCloudDiscoveryengineV1alphaSearchResponseHttpRequest
                        ): ...
                        def search_next(
                            self,
                            previous_request: GoogleCloudDiscoveryengineV1alphaSearchResponseHttpRequest,
                            previous_response: GoogleCloudDiscoveryengineV1alphaSearchResponse,
                        ) -> (
                            GoogleCloudDiscoveryengineV1alphaSearchResponseHttpRequest
                            | None
                        ): ...
                        def searchLite(
                            self,
                            *,
                            servingConfig: str,
                            body: GoogleCloudDiscoveryengineV1alphaSearchRequest = ...,
                            **kwargs: typing.Any,
                        ) -> (
                            GoogleCloudDiscoveryengineV1alphaSearchResponseHttpRequest
                        ): ...
                        def searchLite_next(
                            self,
                            previous_request: GoogleCloudDiscoveryengineV1alphaSearchResponseHttpRequest,
                            previous_response: GoogleCloudDiscoveryengineV1alphaSearchResponse,
                        ) -> (
                            GoogleCloudDiscoveryengineV1alphaSearchResponseHttpRequest
                            | None
                        ): ...
                        def streamAnswer(
                            self,
                            *,
                            servingConfig: str,
                            body: GoogleCloudDiscoveryengineV1alphaAnswerQueryRequest = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudDiscoveryengineV1alphaAnswerQueryResponseHttpRequest: ...

                    @typing.type_check_only
                    class SessionsResource(googleapiclient.discovery.Resource):
                        @typing.type_check_only
                        class AnswersResource(googleapiclient.discovery.Resource):
                            def get(
                                self, *, name: str, **kwargs: typing.Any
                            ) -> GoogleCloudDiscoveryengineV1alphaAnswerHttpRequest: ...

                        def create(
                            self,
                            *,
                            parent: str,
                            body: GoogleCloudDiscoveryengineV1alphaSession = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudDiscoveryengineV1alphaSessionHttpRequest: ...
                        def delete(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> GoogleProtobufEmptyHttpRequest: ...
                        def get(
                            self,
                            *,
                            name: str,
                            includeAnswerDetails: bool = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudDiscoveryengineV1alphaSessionHttpRequest: ...
                        def list(
                            self,
                            *,
                            parent: str,
                            filter: str = ...,
                            orderBy: str = ...,
                            pageSize: int = ...,
                            pageToken: str = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudDiscoveryengineV1alphaListSessionsResponseHttpRequest: ...
                        def list_next(
                            self,
                            previous_request: GoogleCloudDiscoveryengineV1alphaListSessionsResponseHttpRequest,
                            previous_response: GoogleCloudDiscoveryengineV1alphaListSessionsResponse,
                        ) -> (
                            GoogleCloudDiscoveryengineV1alphaListSessionsResponseHttpRequest
                            | None
                        ): ...
                        def patch(
                            self,
                            *,
                            name: str,
                            body: GoogleCloudDiscoveryengineV1alphaSession = ...,
                            updateMask: str = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudDiscoveryengineV1alphaSessionHttpRequest: ...
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
                                returnPartialSuccess: bool = ...,
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
                        class SitemapsResource(googleapiclient.discovery.Resource):
                            def create(
                                self,
                                *,
                                parent: str,
                                body: GoogleCloudDiscoveryengineV1alphaSitemap = ...,
                                **kwargs: typing.Any,
                            ) -> GoogleLongrunningOperationHttpRequest: ...
                            def delete(
                                self, *, name: str, **kwargs: typing.Any
                            ) -> GoogleLongrunningOperationHttpRequest: ...
                            def fetch(
                                self,
                                *,
                                parent: str,
                                matcher_urisMatcher_uris: str | _list[str] = ...,
                                **kwargs: typing.Any,
                            ) -> GoogleCloudDiscoveryengineV1alphaFetchSitemapsResponseHttpRequest: ...

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
                                    returnPartialSuccess: bool = ...,
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
                                body: GoogleCloudDiscoveryengineV1alphaBatchCreateTargetSitesRequest = ...,
                                **kwargs: typing.Any,
                            ) -> GoogleLongrunningOperationHttpRequest: ...
                            def create(
                                self,
                                *,
                                parent: str,
                                body: GoogleCloudDiscoveryengineV1alphaTargetSite = ...,
                                **kwargs: typing.Any,
                            ) -> GoogleLongrunningOperationHttpRequest: ...
                            def delete(
                                self, *, name: str, **kwargs: typing.Any
                            ) -> GoogleLongrunningOperationHttpRequest: ...
                            def get(
                                self, *, name: str, **kwargs: typing.Any
                            ) -> (
                                GoogleCloudDiscoveryengineV1alphaTargetSiteHttpRequest
                            ): ...
                            def list(
                                self,
                                *,
                                parent: str,
                                pageSize: int = ...,
                                pageToken: str = ...,
                                **kwargs: typing.Any,
                            ) -> GoogleCloudDiscoveryengineV1alphaListTargetSitesResponseHttpRequest: ...
                            def list_next(
                                self,
                                previous_request: GoogleCloudDiscoveryengineV1alphaListTargetSitesResponseHttpRequest,
                                previous_response: GoogleCloudDiscoveryengineV1alphaListTargetSitesResponse,
                            ) -> (
                                GoogleCloudDiscoveryengineV1alphaListTargetSitesResponseHttpRequest
                                | None
                            ): ...
                            def patch(
                                self,
                                *,
                                name: str,
                                body: GoogleCloudDiscoveryengineV1alphaTargetSite = ...,
                                **kwargs: typing.Any,
                            ) -> GoogleLongrunningOperationHttpRequest: ...
                            def operations(self) -> OperationsResource: ...

                        def batchVerifyTargetSites(
                            self,
                            *,
                            parent: str,
                            body: GoogleCloudDiscoveryengineV1alphaBatchVerifyTargetSitesRequest = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleLongrunningOperationHttpRequest: ...
                        def disableAdvancedSiteSearch(
                            self,
                            *,
                            siteSearchEngine: str,
                            body: GoogleCloudDiscoveryengineV1alphaDisableAdvancedSiteSearchRequest = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleLongrunningOperationHttpRequest: ...
                        def enableAdvancedSiteSearch(
                            self,
                            *,
                            siteSearchEngine: str,
                            body: GoogleCloudDiscoveryengineV1alphaEnableAdvancedSiteSearchRequest = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleLongrunningOperationHttpRequest: ...
                        def fetchDomainVerificationStatus(
                            self,
                            *,
                            siteSearchEngine: str,
                            pageSize: int = ...,
                            pageToken: str = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudDiscoveryengineV1alphaFetchDomainVerificationStatusResponseHttpRequest: ...
                        def fetchDomainVerificationStatus_next(
                            self,
                            previous_request: GoogleCloudDiscoveryengineV1alphaFetchDomainVerificationStatusResponseHttpRequest,
                            previous_response: GoogleCloudDiscoveryengineV1alphaFetchDomainVerificationStatusResponse,
                        ) -> (
                            GoogleCloudDiscoveryengineV1alphaFetchDomainVerificationStatusResponseHttpRequest
                            | None
                        ): ...
                        def getUriPatternDocumentData(
                            self, *, siteSearchEngine: str, **kwargs: typing.Any
                        ) -> GoogleCloudDiscoveryengineV1alphaGetUriPatternDocumentDataResponseHttpRequest: ...
                        def recrawlUris(
                            self,
                            *,
                            siteSearchEngine: str,
                            body: GoogleCloudDiscoveryengineV1alphaRecrawlUrisRequest = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleLongrunningOperationHttpRequest: ...
                        def setUriPatternDocumentData(
                            self,
                            *,
                            siteSearchEngine: str,
                            body: GoogleCloudDiscoveryengineV1alphaSetUriPatternDocumentDataRequest = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleLongrunningOperationHttpRequest: ...
                        def operations(self) -> OperationsResource: ...
                        def sitemaps(self) -> SitemapsResource: ...
                        def targetSites(self) -> TargetSitesResource: ...

                    @typing.type_check_only
                    class SuggestionDenyListEntriesResource(
                        googleapiclient.discovery.Resource
                    ):
                        def import_(
                            self,
                            *,
                            parent: str,
                            body: GoogleCloudDiscoveryengineV1alphaImportSuggestionDenyListEntriesRequest = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleLongrunningOperationHttpRequest: ...
                        def purge(
                            self,
                            *,
                            parent: str,
                            body: GoogleCloudDiscoveryengineV1alphaPurgeSuggestionDenyListEntriesRequest = ...,
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
                            body: GoogleCloudDiscoveryengineV1alphaImportUserEventsRequest = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleLongrunningOperationHttpRequest: ...
                        def purge(
                            self,
                            *,
                            parent: str,
                            body: GoogleCloudDiscoveryengineV1alphaPurgeUserEventsRequest = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleLongrunningOperationHttpRequest: ...
                        def write(
                            self,
                            *,
                            parent: str,
                            body: GoogleCloudDiscoveryengineV1alphaUserEvent = ...,
                            writeAsync: bool = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudDiscoveryengineV1alphaUserEventHttpRequest: ...

                    @typing.type_check_only
                    class WidgetConfigsResource(googleapiclient.discovery.Resource):
                        def get(
                            self,
                            *,
                            name: str,
                            acceptCache: bool = ...,
                            getWidgetConfigRequestOption_turnOffCollectionComponents: bool = ...,
                            **kwargs: typing.Any,
                        ) -> (
                            GoogleCloudDiscoveryengineV1alphaWidgetConfigHttpRequest
                        ): ...
                        def patch(
                            self,
                            *,
                            name: str,
                            body: GoogleCloudDiscoveryengineV1alphaWidgetConfig = ...,
                            updateMask: str = ...,
                            **kwargs: typing.Any,
                        ) -> (
                            GoogleCloudDiscoveryengineV1alphaWidgetConfigHttpRequest
                        ): ...

                    def addPatientFilter(
                        self,
                        *,
                        dataStore: str,
                        body: GoogleCloudDiscoveryengineV1alphaAddPatientFilterRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def completeQuery(
                        self,
                        *,
                        dataStore: str,
                        includeTailSuggestions: bool = ...,
                        query: str = ...,
                        queryModel: str = ...,
                        userPseudoId: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudDiscoveryengineV1alphaCompleteQueryResponseHttpRequest: ...
                    def create(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudDiscoveryengineV1alphaDataStore = ...,
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
                    def deletePatientFilter(
                        self,
                        *,
                        dataStore: str,
                        body: GoogleCloudDiscoveryengineV1alphaDeletePatientFiltersRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleCloudDiscoveryengineV1alphaDataStoreHttpRequest: ...
                    def getDocumentProcessingConfig(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleCloudDiscoveryengineV1alphaDocumentProcessingConfigHttpRequest: ...
                    def getSiteSearchEngine(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> (
                        GoogleCloudDiscoveryengineV1alphaSiteSearchEngineHttpRequest
                    ): ...
                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudDiscoveryengineV1alphaListDataStoresResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudDiscoveryengineV1alphaListDataStoresResponseHttpRequest,
                        previous_response: GoogleCloudDiscoveryengineV1alphaListDataStoresResponse,
                    ) -> (
                        GoogleCloudDiscoveryengineV1alphaListDataStoresResponseHttpRequest
                        | None
                    ): ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudDiscoveryengineV1alphaDataStore = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudDiscoveryengineV1alphaDataStoreHttpRequest: ...
                    def removePatientFilter(
                        self,
                        *,
                        dataStore: str,
                        body: GoogleCloudDiscoveryengineV1alphaRemovePatientFilterRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def replacePatientFilter(
                        self,
                        *,
                        dataStore: str,
                        body: GoogleCloudDiscoveryengineV1alphaReplacePatientFilterRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def trainCustomModel(
                        self,
                        *,
                        dataStore: str,
                        body: GoogleCloudDiscoveryengineV1alphaTrainCustomModelRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def updateDocumentProcessingConfig(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudDiscoveryengineV1alphaDocumentProcessingConfig = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudDiscoveryengineV1alphaDocumentProcessingConfigHttpRequest: ...
                    def branches(self) -> BranchesResource: ...
                    def completionConfig(self) -> CompletionConfigResource: ...
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
                    def widgetConfigs(self) -> WidgetConfigsResource: ...

                @typing.type_check_only
                class EnginesResource(googleapiclient.discovery.Resource):
                    @typing.type_check_only
                    class AnalyticsResource(googleapiclient.discovery.Resource):
                        def exportMetrics(
                            self,
                            *,
                            analytics: str,
                            body: GoogleCloudDiscoveryengineV1alphaExportMetricsRequest = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleLongrunningOperationHttpRequest: ...
                        def getConfig(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> (
                            GoogleCloudDiscoveryengineV1alphaAnalyticsConfigHttpRequest
                        ): ...
                        def updateConfig(
                            self,
                            *,
                            name: str,
                            body: GoogleCloudDiscoveryengineV1alphaAnalyticsConfig = ...,
                            updateMask: str = ...,
                            **kwargs: typing.Any,
                        ) -> (
                            GoogleCloudDiscoveryengineV1alphaAnalyticsConfigHttpRequest
                        ): ...

                    @typing.type_check_only
                    class AssistantsResource(googleapiclient.discovery.Resource):
                        @typing.type_check_only
                        class AgentsResource(googleapiclient.discovery.Resource):
                            @typing.type_check_only
                            class FilesResource(googleapiclient.discovery.Resource):
                                def import_(
                                    self,
                                    *,
                                    parent: str,
                                    body: GoogleCloudDiscoveryengineV1alphaImportAgentFileRequest = ...,
                                    **kwargs: typing.Any,
                                ) -> GoogleCloudDiscoveryengineV1alphaImportAgentFileResponseHttpRequest: ...

                            @typing.type_check_only
                            class OperationsResource(
                                googleapiclient.discovery.Resource
                            ):
                                def get(
                                    self, *, name: str, **kwargs: typing.Any
                                ) -> GoogleLongrunningOperationHttpRequest: ...

                            def create(
                                self,
                                *,
                                parent: str,
                                body: GoogleCloudDiscoveryengineV1alphaAgent = ...,
                                **kwargs: typing.Any,
                            ) -> GoogleCloudDiscoveryengineV1alphaAgentHttpRequest: ...
                            def delete(
                                self, *, name: str, **kwargs: typing.Any
                            ) -> GoogleLongrunningOperationHttpRequest: ...
                            def disableAgent(
                                self,
                                *,
                                name: str,
                                revisionId: str = ...,
                                **kwargs: typing.Any,
                            ) -> GoogleCloudDiscoveryengineV1alphaAgentHttpRequest: ...
                            def enableAgent(
                                self,
                                *,
                                name: str,
                                revisionId: str = ...,
                                **kwargs: typing.Any,
                            ) -> GoogleCloudDiscoveryengineV1alphaAgentHttpRequest: ...
                            def get(
                                self, *, name: str, **kwargs: typing.Any
                            ) -> GoogleCloudDiscoveryengineV1alphaAgentHttpRequest: ...
                            def getAgentView(
                                self,
                                *,
                                name: str,
                                adminView: bool = ...,
                                languageCode: str = ...,
                                maxSuggestedPrompts: int = ...,
                                **kwargs: typing.Any,
                            ) -> GoogleCloudDiscoveryengineV1alphaGetAgentViewResponseHttpRequest: ...
                            def getIamPolicy(
                                self,
                                *,
                                resource: str,
                                options_requestedPolicyVersion: int = ...,
                                **kwargs: typing.Any,
                            ) -> GoogleIamV1PolicyHttpRequest: ...
                            def list(
                                self,
                                *,
                                parent: str,
                                orderBy: str = ...,
                                pageSize: int = ...,
                                pageToken: str = ...,
                                **kwargs: typing.Any,
                            ) -> GoogleCloudDiscoveryengineV1alphaListAgentsResponseHttpRequest: ...
                            def list_next(
                                self,
                                previous_request: GoogleCloudDiscoveryengineV1alphaListAgentsResponseHttpRequest,
                                previous_response: GoogleCloudDiscoveryengineV1alphaListAgentsResponse,
                            ) -> (
                                GoogleCloudDiscoveryengineV1alphaListAgentsResponseHttpRequest
                                | None
                            ): ...
                            def patch(
                                self,
                                *,
                                name: str,
                                body: GoogleCloudDiscoveryengineV1alphaAgent = ...,
                                updateMask: str = ...,
                                **kwargs: typing.Any,
                            ) -> GoogleCloudDiscoveryengineV1alphaAgentHttpRequest: ...
                            def setIamPolicy(
                                self,
                                *,
                                resource: str,
                                body: GoogleIamV1SetIamPolicyRequest = ...,
                                **kwargs: typing.Any,
                            ) -> GoogleIamV1PolicyHttpRequest: ...
                            def suspendAgent(
                                self,
                                *,
                                name: str,
                                suspensionReason: str = ...,
                                **kwargs: typing.Any,
                            ) -> GoogleCloudDiscoveryengineV1alphaAgentHttpRequest: ...
                            def files(self) -> FilesResource: ...
                            def operations(self) -> OperationsResource: ...

                        @typing.type_check_only
                        class CannedQueriesResource(googleapiclient.discovery.Resource):
                            def create(
                                self,
                                *,
                                parent: str,
                                body: GoogleCloudDiscoveryengineV1alphaCannedQuery = ...,
                                cannedQueryId: str = ...,
                                **kwargs: typing.Any,
                            ) -> (
                                GoogleCloudDiscoveryengineV1alphaCannedQueryHttpRequest
                            ): ...
                            def delete(
                                self, *, name: str, **kwargs: typing.Any
                            ) -> GoogleProtobufEmptyHttpRequest: ...
                            def get(
                                self, *, name: str, **kwargs: typing.Any
                            ) -> (
                                GoogleCloudDiscoveryengineV1alphaCannedQueryHttpRequest
                            ): ...
                            def list(
                                self,
                                *,
                                parent: str,
                                filter: str = ...,
                                pageSize: int = ...,
                                pageToken: str = ...,
                                **kwargs: typing.Any,
                            ) -> GoogleCloudDiscoveryengineV1alphaListCannedQueriesResponseHttpRequest: ...
                            def list_next(
                                self,
                                previous_request: GoogleCloudDiscoveryengineV1alphaListCannedQueriesResponseHttpRequest,
                                previous_response: GoogleCloudDiscoveryengineV1alphaListCannedQueriesResponse,
                            ) -> (
                                GoogleCloudDiscoveryengineV1alphaListCannedQueriesResponseHttpRequest
                                | None
                            ): ...
                            def patch(
                                self,
                                *,
                                name: str,
                                body: GoogleCloudDiscoveryengineV1alphaCannedQuery = ...,
                                updateMask: str = ...,
                                **kwargs: typing.Any,
                            ) -> (
                                GoogleCloudDiscoveryengineV1alphaCannedQueryHttpRequest
                            ): ...

                        def create(
                            self,
                            *,
                            parent: str,
                            body: GoogleCloudDiscoveryengineV1alphaAssistant = ...,
                            assistantId: str = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudDiscoveryengineV1alphaAssistantHttpRequest: ...
                        def delete(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> GoogleProtobufEmptyHttpRequest: ...
                        def get(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> GoogleCloudDiscoveryengineV1alphaAssistantHttpRequest: ...
                        def list(
                            self,
                            *,
                            parent: str,
                            pageSize: int = ...,
                            pageToken: str = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudDiscoveryengineV1alphaListAssistantsResponseHttpRequest: ...
                        def list_next(
                            self,
                            previous_request: GoogleCloudDiscoveryengineV1alphaListAssistantsResponseHttpRequest,
                            previous_response: GoogleCloudDiscoveryengineV1alphaListAssistantsResponse,
                        ) -> (
                            GoogleCloudDiscoveryengineV1alphaListAssistantsResponseHttpRequest
                            | None
                        ): ...
                        def listAvailableAgentViews(
                            self,
                            *,
                            parent: str,
                            adminView: bool = ...,
                            agentOrigin: typing_extensions.Literal[
                                "AGENT_ORIGIN_UNSPECIFIED",
                                "GOOGLE",
                                "ORGANIZATION",
                                "USER",
                            ] = ...,
                            filter: str = ...,
                            languageCode: str = ...,
                            maxSuggestedPrompts: int = ...,
                            pageSize: int = ...,
                            pageToken: str = ...,
                            sortBy: str = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudDiscoveryengineV1alphaListAvailableAgentViewsResponseHttpRequest: ...
                        def listAvailableAgentViews_next(
                            self,
                            previous_request: GoogleCloudDiscoveryengineV1alphaListAvailableAgentViewsResponseHttpRequest,
                            previous_response: GoogleCloudDiscoveryengineV1alphaListAvailableAgentViewsResponse,
                        ) -> (
                            GoogleCloudDiscoveryengineV1alphaListAvailableAgentViewsResponseHttpRequest
                            | None
                        ): ...
                        def patch(
                            self,
                            *,
                            name: str,
                            body: GoogleCloudDiscoveryengineV1alphaAssistant = ...,
                            updateMask: str = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudDiscoveryengineV1alphaAssistantHttpRequest: ...
                        def streamAssist(
                            self,
                            *,
                            name: str,
                            body: GoogleCloudDiscoveryengineV1alphaStreamAssistRequest = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudDiscoveryengineV1alphaStreamAssistResponseHttpRequest: ...
                        def agents(self) -> AgentsResource: ...
                        def cannedQueries(self) -> CannedQueriesResource: ...

                    @typing.type_check_only
                    class CompletionConfigResource(googleapiclient.discovery.Resource):
                        def completeQuery(
                            self,
                            *,
                            completionConfig: str,
                            body: GoogleCloudDiscoveryengineV1alphaAdvancedCompleteQueryRequest = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudDiscoveryengineV1alphaAdvancedCompleteQueryResponseHttpRequest: ...
                        def removeSuggestion(
                            self,
                            *,
                            completionConfig: str,
                            body: GoogleCloudDiscoveryengineV1alphaRemoveSuggestionRequest = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudDiscoveryengineV1alphaRemoveSuggestionResponseHttpRequest: ...

                    @typing.type_check_only
                    class ControlsResource(googleapiclient.discovery.Resource):
                        def create(
                            self,
                            *,
                            parent: str,
                            body: GoogleCloudDiscoveryengineV1alphaControl = ...,
                            controlId: str = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudDiscoveryengineV1alphaControlHttpRequest: ...
                        def delete(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> GoogleProtobufEmptyHttpRequest: ...
                        def get(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> GoogleCloudDiscoveryengineV1alphaControlHttpRequest: ...
                        def list(
                            self,
                            *,
                            parent: str,
                            filter: str = ...,
                            pageSize: int = ...,
                            pageToken: str = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudDiscoveryengineV1alphaListControlsResponseHttpRequest: ...
                        def list_next(
                            self,
                            previous_request: GoogleCloudDiscoveryengineV1alphaListControlsResponseHttpRequest,
                            previous_response: GoogleCloudDiscoveryengineV1alphaListControlsResponse,
                        ) -> (
                            GoogleCloudDiscoveryengineV1alphaListControlsResponseHttpRequest
                            | None
                        ): ...
                        def patch(
                            self,
                            *,
                            name: str,
                            body: GoogleCloudDiscoveryengineV1alphaControl = ...,
                            updateMask: str = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudDiscoveryengineV1alphaControlHttpRequest: ...

                    @typing.type_check_only
                    class ConversationsResource(googleapiclient.discovery.Resource):
                        def converse(
                            self,
                            *,
                            name: str,
                            body: GoogleCloudDiscoveryengineV1alphaConverseConversationRequest = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudDiscoveryengineV1alphaConverseConversationResponseHttpRequest: ...
                        def create(
                            self,
                            *,
                            parent: str,
                            body: GoogleCloudDiscoveryengineV1alphaConversation = ...,
                            **kwargs: typing.Any,
                        ) -> (
                            GoogleCloudDiscoveryengineV1alphaConversationHttpRequest
                        ): ...
                        def delete(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> GoogleProtobufEmptyHttpRequest: ...
                        def get(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> (
                            GoogleCloudDiscoveryengineV1alphaConversationHttpRequest
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
                        ) -> GoogleCloudDiscoveryengineV1alphaListConversationsResponseHttpRequest: ...
                        def list_next(
                            self,
                            previous_request: GoogleCloudDiscoveryengineV1alphaListConversationsResponseHttpRequest,
                            previous_response: GoogleCloudDiscoveryengineV1alphaListConversationsResponse,
                        ) -> (
                            GoogleCloudDiscoveryengineV1alphaListConversationsResponseHttpRequest
                            | None
                        ): ...
                        def patch(
                            self,
                            *,
                            name: str,
                            body: GoogleCloudDiscoveryengineV1alphaConversation = ...,
                            updateMask: str = ...,
                            **kwargs: typing.Any,
                        ) -> (
                            GoogleCloudDiscoveryengineV1alphaConversationHttpRequest
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
                            returnPartialSuccess: bool = ...,
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
                            body: GoogleCloudDiscoveryengineV1alphaAnswerQueryRequest = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudDiscoveryengineV1alphaAnswerQueryResponseHttpRequest: ...
                        def create(
                            self,
                            *,
                            parent: str,
                            body: GoogleCloudDiscoveryengineV1alphaServingConfig = ...,
                            servingConfigId: str = ...,
                            **kwargs: typing.Any,
                        ) -> (
                            GoogleCloudDiscoveryengineV1alphaServingConfigHttpRequest
                        ): ...
                        def delete(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> GoogleProtobufEmptyHttpRequest: ...
                        def get(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> (
                            GoogleCloudDiscoveryengineV1alphaServingConfigHttpRequest
                        ): ...
                        def list(
                            self,
                            *,
                            parent: str,
                            pageSize: int = ...,
                            pageToken: str = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudDiscoveryengineV1alphaListServingConfigsResponseHttpRequest: ...
                        def list_next(
                            self,
                            previous_request: GoogleCloudDiscoveryengineV1alphaListServingConfigsResponseHttpRequest,
                            previous_response: GoogleCloudDiscoveryengineV1alphaListServingConfigsResponse,
                        ) -> (
                            GoogleCloudDiscoveryengineV1alphaListServingConfigsResponseHttpRequest
                            | None
                        ): ...
                        def patch(
                            self,
                            *,
                            name: str,
                            body: GoogleCloudDiscoveryengineV1alphaServingConfig = ...,
                            updateMask: str = ...,
                            **kwargs: typing.Any,
                        ) -> (
                            GoogleCloudDiscoveryengineV1alphaServingConfigHttpRequest
                        ): ...
                        def recommend(
                            self,
                            *,
                            servingConfig: str,
                            body: GoogleCloudDiscoveryengineV1alphaRecommendRequest = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudDiscoveryengineV1alphaRecommendResponseHttpRequest: ...
                        def search(
                            self,
                            *,
                            servingConfig: str,
                            body: GoogleCloudDiscoveryengineV1alphaSearchRequest = ...,
                            **kwargs: typing.Any,
                        ) -> (
                            GoogleCloudDiscoveryengineV1alphaSearchResponseHttpRequest
                        ): ...
                        def search_next(
                            self,
                            previous_request: GoogleCloudDiscoveryengineV1alphaSearchResponseHttpRequest,
                            previous_response: GoogleCloudDiscoveryengineV1alphaSearchResponse,
                        ) -> (
                            GoogleCloudDiscoveryengineV1alphaSearchResponseHttpRequest
                            | None
                        ): ...
                        def searchLite(
                            self,
                            *,
                            servingConfig: str,
                            body: GoogleCloudDiscoveryengineV1alphaSearchRequest = ...,
                            **kwargs: typing.Any,
                        ) -> (
                            GoogleCloudDiscoveryengineV1alphaSearchResponseHttpRequest
                        ): ...
                        def searchLite_next(
                            self,
                            previous_request: GoogleCloudDiscoveryengineV1alphaSearchResponseHttpRequest,
                            previous_response: GoogleCloudDiscoveryengineV1alphaSearchResponse,
                        ) -> (
                            GoogleCloudDiscoveryengineV1alphaSearchResponseHttpRequest
                            | None
                        ): ...
                        def streamAnswer(
                            self,
                            *,
                            servingConfig: str,
                            body: GoogleCloudDiscoveryengineV1alphaAnswerQueryRequest = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudDiscoveryengineV1alphaAnswerQueryResponseHttpRequest: ...

                    @typing.type_check_only
                    class SessionsResource(googleapiclient.discovery.Resource):
                        @typing.type_check_only
                        class AlphaEvolveExperimentsResource(
                            googleapiclient.discovery.Resource
                        ):
                            @typing.type_check_only
                            class OperationsResource(
                                googleapiclient.discovery.Resource
                            ):
                                def get(
                                    self, *, name: str, **kwargs: typing.Any
                                ) -> GoogleLongrunningOperationHttpRequest: ...

                            def operations(self) -> OperationsResource: ...

                        @typing.type_check_only
                        class AnswersResource(googleapiclient.discovery.Resource):
                            def get(
                                self, *, name: str, **kwargs: typing.Any
                            ) -> GoogleCloudDiscoveryengineV1alphaAnswerHttpRequest: ...

                        @typing.type_check_only
                        class FilesResource(googleapiclient.discovery.Resource):
                            def list(
                                self,
                                *,
                                parent: str,
                                filter: str = ...,
                                orderBy: str = ...,
                                pageSize: int = ...,
                                pageToken: str = ...,
                                **kwargs: typing.Any,
                            ) -> GoogleCloudDiscoveryengineV1alphaListFilesResponseHttpRequest: ...
                            def list_next(
                                self,
                                previous_request: GoogleCloudDiscoveryengineV1alphaListFilesResponseHttpRequest,
                                previous_response: GoogleCloudDiscoveryengineV1alphaListFilesResponse,
                            ) -> (
                                GoogleCloudDiscoveryengineV1alphaListFilesResponseHttpRequest
                                | None
                            ): ...

                        @typing.type_check_only
                        class OperationsResource(googleapiclient.discovery.Resource):
                            def get(
                                self, *, name: str, **kwargs: typing.Any
                            ) -> GoogleLongrunningOperationHttpRequest: ...

                        def create(
                            self,
                            *,
                            parent: str,
                            body: GoogleCloudDiscoveryengineV1alphaSession = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudDiscoveryengineV1alphaSessionHttpRequest: ...
                        def delete(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> GoogleProtobufEmptyHttpRequest: ...
                        def get(
                            self,
                            *,
                            name: str,
                            includeAnswerDetails: bool = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudDiscoveryengineV1alphaSessionHttpRequest: ...
                        def list(
                            self,
                            *,
                            parent: str,
                            filter: str = ...,
                            orderBy: str = ...,
                            pageSize: int = ...,
                            pageToken: str = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudDiscoveryengineV1alphaListSessionsResponseHttpRequest: ...
                        def list_next(
                            self,
                            previous_request: GoogleCloudDiscoveryengineV1alphaListSessionsResponseHttpRequest,
                            previous_response: GoogleCloudDiscoveryengineV1alphaListSessionsResponse,
                        ) -> (
                            GoogleCloudDiscoveryengineV1alphaListSessionsResponseHttpRequest
                            | None
                        ): ...
                        def patch(
                            self,
                            *,
                            name: str,
                            body: GoogleCloudDiscoveryengineV1alphaSession = ...,
                            updateMask: str = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudDiscoveryengineV1alphaSessionHttpRequest: ...
                        def alphaEvolveExperiments(
                            self,
                        ) -> AlphaEvolveExperimentsResource: ...
                        def answers(self) -> AnswersResource: ...
                        def files(self) -> FilesResource: ...
                        def operations(self) -> OperationsResource: ...

                    @typing.type_check_only
                    class WidgetConfigsResource(googleapiclient.discovery.Resource):
                        def get(
                            self,
                            *,
                            name: str,
                            acceptCache: bool = ...,
                            getWidgetConfigRequestOption_turnOffCollectionComponents: bool = ...,
                            **kwargs: typing.Any,
                        ) -> (
                            GoogleCloudDiscoveryengineV1alphaWidgetConfigHttpRequest
                        ): ...
                        def patch(
                            self,
                            *,
                            name: str,
                            body: GoogleCloudDiscoveryengineV1alphaWidgetConfig = ...,
                            updateMask: str = ...,
                            **kwargs: typing.Any,
                        ) -> (
                            GoogleCloudDiscoveryengineV1alphaWidgetConfigHttpRequest
                        ): ...

                    def create(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudDiscoveryengineV1alphaEngine = ...,
                        engineId: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleCloudDiscoveryengineV1alphaEngineHttpRequest: ...
                    def getWorkspaceSettings(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> (
                        GoogleCloudDiscoveryengineV1alphaWorkspaceSettingsHttpRequest
                    ): ...
                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
                    ) -> (
                        GoogleCloudDiscoveryengineV1alphaListEnginesResponseHttpRequest
                    ): ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudDiscoveryengineV1alphaListEnginesResponseHttpRequest,
                        previous_response: GoogleCloudDiscoveryengineV1alphaListEnginesResponse,
                    ) -> (
                        GoogleCloudDiscoveryengineV1alphaListEnginesResponseHttpRequest
                        | None
                    ): ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudDiscoveryengineV1alphaEngine = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudDiscoveryengineV1alphaEngineHttpRequest: ...
                    def pause(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudDiscoveryengineV1alphaPauseEngineRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudDiscoveryengineV1alphaEngineHttpRequest: ...
                    def resume(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudDiscoveryengineV1alphaResumeEngineRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudDiscoveryengineV1alphaEngineHttpRequest: ...
                    def tune(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudDiscoveryengineV1alphaTuneEngineRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def analytics(self) -> AnalyticsResource: ...
                    def assistants(self) -> AssistantsResource: ...
                    def completionConfig(self) -> CompletionConfigResource: ...
                    def controls(self) -> ControlsResource: ...
                    def conversations(self) -> ConversationsResource: ...
                    def operations(self) -> OperationsResource: ...
                    def servingConfigs(self) -> ServingConfigsResource: ...
                    def sessions(self) -> SessionsResource: ...
                    def widgetConfigs(self) -> WidgetConfigsResource: ...

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
                        returnPartialSuccess: bool = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleLongrunningListOperationsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: GoogleLongrunningListOperationsResponseHttpRequest,
                        previous_response: GoogleLongrunningListOperationsResponse,
                    ) -> GoogleLongrunningListOperationsResponseHttpRequest | None: ...

                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudDiscoveryengineV1alphaCollectionHttpRequest: ...
                def getDataConnector(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudDiscoveryengineV1alphaDataConnectorHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> (
                    GoogleCloudDiscoveryengineV1alphaListCollectionsResponseHttpRequest
                ): ...
                def list_next(
                    self,
                    previous_request: GoogleCloudDiscoveryengineV1alphaListCollectionsResponseHttpRequest,
                    previous_response: GoogleCloudDiscoveryengineV1alphaListCollectionsResponse,
                ) -> (
                    GoogleCloudDiscoveryengineV1alphaListCollectionsResponseHttpRequest
                    | None
                ): ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudDiscoveryengineV1alphaCollection = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def updateDataConnector(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudDiscoveryengineV1alphaDataConnector = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudDiscoveryengineV1alphaDataConnectorHttpRequest: ...
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
                        @typing.type_check_only
                        class ChunksResource(googleapiclient.discovery.Resource):
                            def get(
                                self, *, name: str, **kwargs: typing.Any
                            ) -> GoogleCloudDiscoveryengineV1alphaChunkHttpRequest: ...
                            def list(
                                self,
                                *,
                                parent: str,
                                pageSize: int = ...,
                                pageToken: str = ...,
                                **kwargs: typing.Any,
                            ) -> GoogleCloudDiscoveryengineV1alphaListChunksResponseHttpRequest: ...
                            def list_next(
                                self,
                                previous_request: GoogleCloudDiscoveryengineV1alphaListChunksResponseHttpRequest,
                                previous_response: GoogleCloudDiscoveryengineV1alphaListChunksResponse,
                            ) -> (
                                GoogleCloudDiscoveryengineV1alphaListChunksResponseHttpRequest
                                | None
                            ): ...

                        def create(
                            self,
                            *,
                            parent: str,
                            body: GoogleCloudDiscoveryengineV1alphaDocument = ...,
                            documentId: str = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudDiscoveryengineV1alphaDocumentHttpRequest: ...
                        def delete(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> GoogleProtobufEmptyHttpRequest: ...
                        def get(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> GoogleCloudDiscoveryengineV1alphaDocumentHttpRequest: ...
                        def getProcessedDocument(
                            self,
                            *,
                            name: str,
                            imageId: str = ...,
                            processedDocumentFormat: typing_extensions.Literal[
                                "PROCESSED_DOCUMENT_FORMAT_UNSPECIFIED", "JSON"
                            ] = ...,
                            processedDocumentType: typing_extensions.Literal[
                                "PROCESSED_DOCUMENT_TYPE_UNSPECIFIED",
                                "PARSED_DOCUMENT",
                                "CHUNKED_DOCUMENT",
                                "IMAGE_CONVERTED_DOCUMENT",
                                "IMAGE_BYTES",
                            ] = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudDiscoveryengineV1alphaProcessedDocumentHttpRequest: ...
                        def import_(
                            self,
                            *,
                            parent: str,
                            body: GoogleCloudDiscoveryengineV1alphaImportDocumentsRequest = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleLongrunningOperationHttpRequest: ...
                        def list(
                            self,
                            *,
                            parent: str,
                            pageSize: int = ...,
                            pageToken: str = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudDiscoveryengineV1alphaListDocumentsResponseHttpRequest: ...
                        def list_next(
                            self,
                            previous_request: GoogleCloudDiscoveryengineV1alphaListDocumentsResponseHttpRequest,
                            previous_response: GoogleCloudDiscoveryengineV1alphaListDocumentsResponse,
                        ) -> (
                            GoogleCloudDiscoveryengineV1alphaListDocumentsResponseHttpRequest
                            | None
                        ): ...
                        def patch(
                            self,
                            *,
                            name: str,
                            body: GoogleCloudDiscoveryengineV1alphaDocument = ...,
                            allowMissing: bool = ...,
                            updateMask: str = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudDiscoveryengineV1alphaDocumentHttpRequest: ...
                        def purge(
                            self,
                            *,
                            parent: str,
                            body: GoogleCloudDiscoveryengineV1alphaPurgeDocumentsRequest = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleLongrunningOperationHttpRequest: ...
                        def chunks(self) -> ChunksResource: ...

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
                            returnPartialSuccess: bool = ...,
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
                    ) -> GoogleCloudDiscoveryengineV1alphaBatchGetDocumentsMetadataResponseHttpRequest: ...
                    def get(
                        self,
                        *,
                        name: str,
                        view: typing_extensions.Literal[
                            "BRANCH_VIEW_UNSPECIFIED",
                            "BRANCH_VIEW_BASIC",
                            "BRANCH_VIEW_FULL",
                        ] = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudDiscoveryengineV1alphaBranchHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        view: typing_extensions.Literal[
                            "BRANCH_VIEW_UNSPECIFIED",
                            "BRANCH_VIEW_BASIC",
                            "BRANCH_VIEW_FULL",
                        ] = ...,
                        **kwargs: typing.Any,
                    ) -> (
                        GoogleCloudDiscoveryengineV1alphaListBranchesResponseHttpRequest
                    ): ...
                    def documents(self) -> DocumentsResource: ...
                    def operations(self) -> OperationsResource: ...

                @typing.type_check_only
                class CompletionConfigResource(googleapiclient.discovery.Resource):
                    def completeQuery(
                        self,
                        *,
                        completionConfig: str,
                        body: GoogleCloudDiscoveryengineV1alphaAdvancedCompleteQueryRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudDiscoveryengineV1alphaAdvancedCompleteQueryResponseHttpRequest: ...

                @typing.type_check_only
                class CompletionSuggestionsResource(googleapiclient.discovery.Resource):
                    def import_(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudDiscoveryengineV1alphaImportCompletionSuggestionsRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def purge(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudDiscoveryengineV1alphaPurgeCompletionSuggestionsRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleLongrunningOperationHttpRequest: ...

                @typing.type_check_only
                class ControlsResource(googleapiclient.discovery.Resource):
                    def create(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudDiscoveryengineV1alphaControl = ...,
                        controlId: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudDiscoveryengineV1alphaControlHttpRequest: ...
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleProtobufEmptyHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleCloudDiscoveryengineV1alphaControlHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
                    ) -> (
                        GoogleCloudDiscoveryengineV1alphaListControlsResponseHttpRequest
                    ): ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudDiscoveryengineV1alphaListControlsResponseHttpRequest,
                        previous_response: GoogleCloudDiscoveryengineV1alphaListControlsResponse,
                    ) -> (
                        GoogleCloudDiscoveryengineV1alphaListControlsResponseHttpRequest
                        | None
                    ): ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudDiscoveryengineV1alphaControl = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudDiscoveryengineV1alphaControlHttpRequest: ...

                @typing.type_check_only
                class ConversationsResource(googleapiclient.discovery.Resource):
                    def converse(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudDiscoveryengineV1alphaConverseConversationRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudDiscoveryengineV1alphaConverseConversationResponseHttpRequest: ...
                    def create(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudDiscoveryengineV1alphaConversation = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudDiscoveryengineV1alphaConversationHttpRequest: ...
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleProtobufEmptyHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleCloudDiscoveryengineV1alphaConversationHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str = ...,
                        orderBy: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudDiscoveryengineV1alphaListConversationsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudDiscoveryengineV1alphaListConversationsResponseHttpRequest,
                        previous_response: GoogleCloudDiscoveryengineV1alphaListConversationsResponse,
                    ) -> (
                        GoogleCloudDiscoveryengineV1alphaListConversationsResponseHttpRequest
                        | None
                    ): ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudDiscoveryengineV1alphaConversation = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudDiscoveryengineV1alphaConversationHttpRequest: ...

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
                            returnPartialSuccess: bool = ...,
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
                        returnPartialSuccess: bool = ...,
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
                        body: GoogleCloudDiscoveryengineV1alphaSchema = ...,
                        schemaId: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleCloudDiscoveryengineV1alphaSchemaHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
                    ) -> (
                        GoogleCloudDiscoveryengineV1alphaListSchemasResponseHttpRequest
                    ): ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudDiscoveryengineV1alphaListSchemasResponseHttpRequest,
                        previous_response: GoogleCloudDiscoveryengineV1alphaListSchemasResponse,
                    ) -> (
                        GoogleCloudDiscoveryengineV1alphaListSchemasResponseHttpRequest
                        | None
                    ): ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudDiscoveryengineV1alphaSchema = ...,
                        allowMissing: bool = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleLongrunningOperationHttpRequest: ...

                @typing.type_check_only
                class ServingConfigsResource(googleapiclient.discovery.Resource):
                    def answer(
                        self,
                        *,
                        servingConfig: str,
                        body: GoogleCloudDiscoveryengineV1alphaAnswerQueryRequest = ...,
                        **kwargs: typing.Any,
                    ) -> (
                        GoogleCloudDiscoveryengineV1alphaAnswerQueryResponseHttpRequest
                    ): ...
                    def create(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudDiscoveryengineV1alphaServingConfig = ...,
                        servingConfigId: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudDiscoveryengineV1alphaServingConfigHttpRequest: ...
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleProtobufEmptyHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleCloudDiscoveryengineV1alphaServingConfigHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudDiscoveryengineV1alphaListServingConfigsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudDiscoveryengineV1alphaListServingConfigsResponseHttpRequest,
                        previous_response: GoogleCloudDiscoveryengineV1alphaListServingConfigsResponse,
                    ) -> (
                        GoogleCloudDiscoveryengineV1alphaListServingConfigsResponseHttpRequest
                        | None
                    ): ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudDiscoveryengineV1alphaServingConfig = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudDiscoveryengineV1alphaServingConfigHttpRequest: ...
                    def recommend(
                        self,
                        *,
                        servingConfig: str,
                        body: GoogleCloudDiscoveryengineV1alphaRecommendRequest = ...,
                        **kwargs: typing.Any,
                    ) -> (
                        GoogleCloudDiscoveryengineV1alphaRecommendResponseHttpRequest
                    ): ...
                    def search(
                        self,
                        *,
                        servingConfig: str,
                        body: GoogleCloudDiscoveryengineV1alphaSearchRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudDiscoveryengineV1alphaSearchResponseHttpRequest: ...
                    def search_next(
                        self,
                        previous_request: GoogleCloudDiscoveryengineV1alphaSearchResponseHttpRequest,
                        previous_response: GoogleCloudDiscoveryengineV1alphaSearchResponse,
                    ) -> (
                        GoogleCloudDiscoveryengineV1alphaSearchResponseHttpRequest
                        | None
                    ): ...
                    def searchLite(
                        self,
                        *,
                        servingConfig: str,
                        body: GoogleCloudDiscoveryengineV1alphaSearchRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudDiscoveryengineV1alphaSearchResponseHttpRequest: ...
                    def searchLite_next(
                        self,
                        previous_request: GoogleCloudDiscoveryengineV1alphaSearchResponseHttpRequest,
                        previous_response: GoogleCloudDiscoveryengineV1alphaSearchResponse,
                    ) -> (
                        GoogleCloudDiscoveryengineV1alphaSearchResponseHttpRequest
                        | None
                    ): ...
                    def streamAnswer(
                        self,
                        *,
                        servingConfig: str,
                        body: GoogleCloudDiscoveryengineV1alphaAnswerQueryRequest = ...,
                        **kwargs: typing.Any,
                    ) -> (
                        GoogleCloudDiscoveryengineV1alphaAnswerQueryResponseHttpRequest
                    ): ...

                @typing.type_check_only
                class SessionsResource(googleapiclient.discovery.Resource):
                    @typing.type_check_only
                    class AnswersResource(googleapiclient.discovery.Resource):
                        def get(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> GoogleCloudDiscoveryengineV1alphaAnswerHttpRequest: ...

                    def create(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudDiscoveryengineV1alphaSession = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudDiscoveryengineV1alphaSessionHttpRequest: ...
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleProtobufEmptyHttpRequest: ...
                    def get(
                        self,
                        *,
                        name: str,
                        includeAnswerDetails: bool = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudDiscoveryengineV1alphaSessionHttpRequest: ...
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
                        GoogleCloudDiscoveryengineV1alphaListSessionsResponseHttpRequest
                    ): ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudDiscoveryengineV1alphaListSessionsResponseHttpRequest,
                        previous_response: GoogleCloudDiscoveryengineV1alphaListSessionsResponse,
                    ) -> (
                        GoogleCloudDiscoveryengineV1alphaListSessionsResponseHttpRequest
                        | None
                    ): ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudDiscoveryengineV1alphaSession = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudDiscoveryengineV1alphaSessionHttpRequest: ...
                    def answers(self) -> AnswersResource: ...

                @typing.type_check_only
                class SiteSearchEngineResource(googleapiclient.discovery.Resource):
                    @typing.type_check_only
                    class SitemapsResource(googleapiclient.discovery.Resource):
                        def create(
                            self,
                            *,
                            parent: str,
                            body: GoogleCloudDiscoveryengineV1alphaSitemap = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleLongrunningOperationHttpRequest: ...
                        def delete(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> GoogleLongrunningOperationHttpRequest: ...
                        def fetch(
                            self,
                            *,
                            parent: str,
                            matcher_urisMatcher_uris: str | _list[str] = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudDiscoveryengineV1alphaFetchSitemapsResponseHttpRequest: ...

                    @typing.type_check_only
                    class TargetSitesResource(googleapiclient.discovery.Resource):
                        def batchCreate(
                            self,
                            *,
                            parent: str,
                            body: GoogleCloudDiscoveryengineV1alphaBatchCreateTargetSitesRequest = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleLongrunningOperationHttpRequest: ...
                        def create(
                            self,
                            *,
                            parent: str,
                            body: GoogleCloudDiscoveryengineV1alphaTargetSite = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleLongrunningOperationHttpRequest: ...
                        def delete(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> GoogleLongrunningOperationHttpRequest: ...
                        def get(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> GoogleCloudDiscoveryengineV1alphaTargetSiteHttpRequest: ...
                        def list(
                            self,
                            *,
                            parent: str,
                            pageSize: int = ...,
                            pageToken: str = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudDiscoveryengineV1alphaListTargetSitesResponseHttpRequest: ...
                        def list_next(
                            self,
                            previous_request: GoogleCloudDiscoveryengineV1alphaListTargetSitesResponseHttpRequest,
                            previous_response: GoogleCloudDiscoveryengineV1alphaListTargetSitesResponse,
                        ) -> (
                            GoogleCloudDiscoveryengineV1alphaListTargetSitesResponseHttpRequest
                            | None
                        ): ...
                        def patch(
                            self,
                            *,
                            name: str,
                            body: GoogleCloudDiscoveryengineV1alphaTargetSite = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleLongrunningOperationHttpRequest: ...

                    def disableAdvancedSiteSearch(
                        self,
                        *,
                        siteSearchEngine: str,
                        body: GoogleCloudDiscoveryengineV1alphaDisableAdvancedSiteSearchRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def enableAdvancedSiteSearch(
                        self,
                        *,
                        siteSearchEngine: str,
                        body: GoogleCloudDiscoveryengineV1alphaEnableAdvancedSiteSearchRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def recrawlUris(
                        self,
                        *,
                        siteSearchEngine: str,
                        body: GoogleCloudDiscoveryengineV1alphaRecrawlUrisRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def sitemaps(self) -> SitemapsResource: ...
                    def targetSites(self) -> TargetSitesResource: ...

                @typing.type_check_only
                class SuggestionDenyListEntriesResource(
                    googleapiclient.discovery.Resource
                ):
                    def import_(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudDiscoveryengineV1alphaImportSuggestionDenyListEntriesRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def purge(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudDiscoveryengineV1alphaPurgeSuggestionDenyListEntriesRequest = ...,
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
                        body: GoogleCloudDiscoveryengineV1alphaImportUserEventsRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def purge(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudDiscoveryengineV1alphaPurgeUserEventsRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def write(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudDiscoveryengineV1alphaUserEvent = ...,
                        writeAsync: bool = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudDiscoveryengineV1alphaUserEventHttpRequest: ...

                @typing.type_check_only
                class WidgetConfigsResource(googleapiclient.discovery.Resource):
                    def get(
                        self,
                        *,
                        name: str,
                        acceptCache: bool = ...,
                        getWidgetConfigRequestOption_turnOffCollectionComponents: bool = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudDiscoveryengineV1alphaWidgetConfigHttpRequest: ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudDiscoveryengineV1alphaWidgetConfig = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudDiscoveryengineV1alphaWidgetConfigHttpRequest: ...

                def addPatientFilter(
                    self,
                    *,
                    dataStore: str,
                    body: GoogleCloudDiscoveryengineV1alphaAddPatientFilterRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
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
                    GoogleCloudDiscoveryengineV1alphaCompleteQueryResponseHttpRequest
                ): ...
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudDiscoveryengineV1alphaDataStore = ...,
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
                def deletePatientFilter(
                    self,
                    *,
                    dataStore: str,
                    body: GoogleCloudDiscoveryengineV1alphaDeletePatientFiltersRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudDiscoveryengineV1alphaDataStoreHttpRequest: ...
                def getDocumentProcessingConfig(
                    self, *, name: str, **kwargs: typing.Any
                ) -> (
                    GoogleCloudDiscoveryengineV1alphaDocumentProcessingConfigHttpRequest
                ): ...
                def getSiteSearchEngine(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudDiscoveryengineV1alphaSiteSearchEngineHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> (
                    GoogleCloudDiscoveryengineV1alphaListDataStoresResponseHttpRequest
                ): ...
                def list_next(
                    self,
                    previous_request: GoogleCloudDiscoveryengineV1alphaListDataStoresResponseHttpRequest,
                    previous_response: GoogleCloudDiscoveryengineV1alphaListDataStoresResponse,
                ) -> (
                    GoogleCloudDiscoveryengineV1alphaListDataStoresResponseHttpRequest
                    | None
                ): ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudDiscoveryengineV1alphaDataStore = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudDiscoveryengineV1alphaDataStoreHttpRequest: ...
                def removePatientFilter(
                    self,
                    *,
                    dataStore: str,
                    body: GoogleCloudDiscoveryengineV1alphaRemovePatientFilterRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def replacePatientFilter(
                    self,
                    *,
                    dataStore: str,
                    body: GoogleCloudDiscoveryengineV1alphaReplacePatientFilterRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def updateDocumentProcessingConfig(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudDiscoveryengineV1alphaDocumentProcessingConfig = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> (
                    GoogleCloudDiscoveryengineV1alphaDocumentProcessingConfigHttpRequest
                ): ...
                def branches(self) -> BranchesResource: ...
                def completionConfig(self) -> CompletionConfigResource: ...
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
                def widgetConfigs(self) -> WidgetConfigsResource: ...

            @typing.type_check_only
            class EvaluationsResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class OperationsResource(googleapiclient.discovery.Resource):
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleLongrunningOperationHttpRequest: ...

                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudDiscoveryengineV1alphaEvaluation = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudDiscoveryengineV1alphaEvaluationHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> (
                    GoogleCloudDiscoveryengineV1alphaListEvaluationsResponseHttpRequest
                ): ...
                def list_next(
                    self,
                    previous_request: GoogleCloudDiscoveryengineV1alphaListEvaluationsResponseHttpRequest,
                    previous_response: GoogleCloudDiscoveryengineV1alphaListEvaluationsResponse,
                ) -> (
                    GoogleCloudDiscoveryengineV1alphaListEvaluationsResponseHttpRequest
                    | None
                ): ...
                def listResults(
                    self,
                    *,
                    evaluation: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudDiscoveryengineV1alphaListEvaluationResultsResponseHttpRequest: ...
                def listResults_next(
                    self,
                    previous_request: GoogleCloudDiscoveryengineV1alphaListEvaluationResultsResponseHttpRequest,
                    previous_response: GoogleCloudDiscoveryengineV1alphaListEvaluationResultsResponse,
                ) -> (
                    GoogleCloudDiscoveryengineV1alphaListEvaluationResultsResponseHttpRequest
                    | None
                ): ...
                def operations(self) -> OperationsResource: ...

            @typing.type_check_only
            class GroundingConfigsResource(googleapiclient.discovery.Resource):
                def check(
                    self,
                    *,
                    groundingConfig: str,
                    body: GoogleCloudDiscoveryengineV1alphaCheckGroundingRequest = ...,
                    **kwargs: typing.Any,
                ) -> (
                    GoogleCloudDiscoveryengineV1alphaCheckGroundingResponseHttpRequest
                ): ...

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
                        returnPartialSuccess: bool = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleLongrunningListOperationsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: GoogleLongrunningListOperationsResponseHttpRequest,
                        previous_response: GoogleLongrunningListOperationsResponse,
                    ) -> GoogleLongrunningListOperationsResponseHttpRequest | None: ...

                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudDiscoveryengineV1alphaIdentityMappingStore = ...,
                    cmekConfigName: str = ...,
                    disableCmek: bool = ...,
                    identityMappingStoreId: str = ...,
                    **kwargs: typing.Any,
                ) -> (
                    GoogleCloudDiscoveryengineV1alphaIdentityMappingStoreHttpRequest
                ): ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> (
                    GoogleCloudDiscoveryengineV1alphaIdentityMappingStoreHttpRequest
                ): ...
                def importIdentityMappings(
                    self,
                    *,
                    identityMappingStore: str,
                    body: GoogleCloudDiscoveryengineV1alphaImportIdentityMappingsRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudDiscoveryengineV1alphaListIdentityMappingStoresResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudDiscoveryengineV1alphaListIdentityMappingStoresResponseHttpRequest,
                    previous_response: GoogleCloudDiscoveryengineV1alphaListIdentityMappingStoresResponse,
                ) -> (
                    GoogleCloudDiscoveryengineV1alphaListIdentityMappingStoresResponseHttpRequest
                    | None
                ): ...
                def listIdentityMappings(
                    self,
                    *,
                    identityMappingStore: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudDiscoveryengineV1alphaListIdentityMappingsResponseHttpRequest: ...
                def listIdentityMappings_next(
                    self,
                    previous_request: GoogleCloudDiscoveryengineV1alphaListIdentityMappingsResponseHttpRequest,
                    previous_response: GoogleCloudDiscoveryengineV1alphaListIdentityMappingsResponse,
                ) -> (
                    GoogleCloudDiscoveryengineV1alphaListIdentityMappingsResponseHttpRequest
                    | None
                ): ...
                def purgeIdentityMappings(
                    self,
                    *,
                    identityMappingStore: str,
                    body: GoogleCloudDiscoveryengineV1alphaPurgeIdentityMappingsRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def operations(self) -> OperationsResource: ...

            @typing.type_check_only
            class LicenseConfigsResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudDiscoveryengineV1alphaLicenseConfig = ...,
                    licenseConfigId: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudDiscoveryengineV1alphaLicenseConfigHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudDiscoveryengineV1alphaLicenseConfigHttpRequest: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudDiscoveryengineV1alphaLicenseConfig = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudDiscoveryengineV1alphaLicenseConfigHttpRequest: ...

            @typing.type_check_only
            class NotebooksResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class AudioOverviewsResource(googleapiclient.discovery.Resource):
                    def create(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudNotebooklmV1alphaCreateAudioOverviewRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudNotebooklmV1alphaCreateAudioOverviewResponseHttpRequest: ...
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleProtobufEmptyHttpRequest: ...

                @typing.type_check_only
                class SourcesResource(googleapiclient.discovery.Resource):
                    def batchCreate(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudNotebooklmV1alphaBatchCreateSourcesRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudNotebooklmV1alphaBatchCreateSourcesResponseHttpRequest: ...
                    def batchDelete(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudNotebooklmV1alphaBatchDeleteSourcesRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleProtobufEmptyHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleCloudNotebooklmV1alphaSourceHttpRequest: ...

                def batchDelete(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudNotebooklmV1alphaBatchDeleteNotebooksRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleProtobufEmptyHttpRequest: ...
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudNotebooklmV1alphaNotebook = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudNotebooklmV1alphaNotebookHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudNotebooklmV1alphaNotebookHttpRequest: ...
                def listRecentlyViewed(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudNotebooklmV1alphaListRecentlyViewedNotebooksResponseHttpRequest: ...
                def listRecentlyViewed_next(
                    self,
                    previous_request: GoogleCloudNotebooklmV1alphaListRecentlyViewedNotebooksResponseHttpRequest,
                    previous_response: GoogleCloudNotebooklmV1alphaListRecentlyViewedNotebooksResponse,
                ) -> (
                    GoogleCloudNotebooklmV1alphaListRecentlyViewedNotebooksResponseHttpRequest
                    | None
                ): ...
                def share(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudNotebooklmV1alphaShareNotebookRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudNotebooklmV1alphaShareNotebookResponseHttpRequest: ...
                def audioOverviews(self) -> AudioOverviewsResource: ...
                def sources(self) -> SourcesResource: ...

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
                    returnPartialSuccess: bool = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningListOperationsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleLongrunningListOperationsResponseHttpRequest,
                    previous_response: GoogleLongrunningListOperationsResponse,
                ) -> GoogleLongrunningListOperationsResponseHttpRequest | None: ...

            @typing.type_check_only
            class PodcastsResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class OperationsResource(googleapiclient.discovery.Resource):
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleLongrunningOperationHttpRequest: ...

                def operations(self) -> OperationsResource: ...

            @typing.type_check_only
            class RankingConfigsResource(googleapiclient.discovery.Resource):
                def rank(
                    self,
                    *,
                    rankingConfig: str,
                    body: GoogleCloudDiscoveryengineV1alphaRankRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudDiscoveryengineV1alphaRankResponseHttpRequest: ...

            @typing.type_check_only
            class RequirementsResource(googleapiclient.discovery.Resource):
                def checkRequirement(
                    self,
                    *,
                    location: str,
                    body: GoogleCloudDiscoveryengineV1alphaCheckRequirementRequest = ...,
                    **kwargs: typing.Any,
                ) -> (
                    GoogleCloudDiscoveryengineV1alphaCheckRequirementResponseHttpRequest
                ): ...

            @typing.type_check_only
            class SampleQuerySetsResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class OperationsResource(googleapiclient.discovery.Resource):
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleLongrunningOperationHttpRequest: ...

                @typing.type_check_only
                class SampleQueriesResource(googleapiclient.discovery.Resource):
                    def create(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudDiscoveryengineV1alphaSampleQuery = ...,
                        sampleQueryId: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudDiscoveryengineV1alphaSampleQueryHttpRequest: ...
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleProtobufEmptyHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleCloudDiscoveryengineV1alphaSampleQueryHttpRequest: ...
                    def import_(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudDiscoveryengineV1alphaImportSampleQueriesRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudDiscoveryengineV1alphaListSampleQueriesResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudDiscoveryengineV1alphaListSampleQueriesResponseHttpRequest,
                        previous_response: GoogleCloudDiscoveryengineV1alphaListSampleQueriesResponse,
                    ) -> (
                        GoogleCloudDiscoveryengineV1alphaListSampleQueriesResponseHttpRequest
                        | None
                    ): ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudDiscoveryengineV1alphaSampleQuery = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudDiscoveryengineV1alphaSampleQueryHttpRequest: ...

                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudDiscoveryengineV1alphaSampleQuerySet = ...,
                    sampleQuerySetId: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudDiscoveryengineV1alphaSampleQuerySetHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleProtobufEmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudDiscoveryengineV1alphaSampleQuerySetHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudDiscoveryengineV1alphaListSampleQuerySetsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudDiscoveryengineV1alphaListSampleQuerySetsResponseHttpRequest,
                    previous_response: GoogleCloudDiscoveryengineV1alphaListSampleQuerySetsResponse,
                ) -> (
                    GoogleCloudDiscoveryengineV1alphaListSampleQuerySetsResponseHttpRequest
                    | None
                ): ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudDiscoveryengineV1alphaSampleQuerySet = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudDiscoveryengineV1alphaSampleQuerySetHttpRequest: ...
                def operations(self) -> OperationsResource: ...
                def sampleQueries(self) -> SampleQueriesResource: ...

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
                    body: GoogleCloudDiscoveryengineV1alphaImportUserEventsRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def write(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudDiscoveryengineV1alphaUserEvent = ...,
                    writeAsync: bool = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudDiscoveryengineV1alphaUserEventHttpRequest: ...

            @typing.type_check_only
            class UserStoresResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class LicenseConfigsUsageStatsResource(
                    googleapiclient.discovery.Resource
                ):
                    def list(
                        self, *, parent: str, **kwargs: typing.Any
                    ) -> GoogleCloudDiscoveryengineV1alphaListLicenseConfigsUsageStatsResponseHttpRequest: ...

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
                        returnPartialSuccess: bool = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleLongrunningListOperationsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: GoogleLongrunningListOperationsResponseHttpRequest,
                        previous_response: GoogleLongrunningListOperationsResponse,
                    ) -> GoogleLongrunningListOperationsResponseHttpRequest | None: ...

                @typing.type_check_only
                class UserLicensesResource(googleapiclient.discovery.Resource):
                    def list(
                        self,
                        *,
                        parent: str,
                        orderBy: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudDiscoveryengineV1alphaListUserLicensesResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudDiscoveryengineV1alphaListUserLicensesResponseHttpRequest,
                        previous_response: GoogleCloudDiscoveryengineV1alphaListUserLicensesResponse,
                    ) -> (
                        GoogleCloudDiscoveryengineV1alphaListUserLicensesResponseHttpRequest
                        | None
                    ): ...

                def batchUpdateUserLicenses(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudDiscoveryengineV1alphaBatchUpdateUserLicensesRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudDiscoveryengineV1alphaUserStore = ...,
                    userStoreId: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudDiscoveryengineV1alphaUserStoreHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudDiscoveryengineV1alphaUserStoreHttpRequest: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudDiscoveryengineV1alphaUserStore = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudDiscoveryengineV1alphaUserStoreHttpRequest: ...
                def licenseConfigsUsageStats(
                    self,
                ) -> LicenseConfigsUsageStatsResource: ...
                def operations(self) -> OperationsResource: ...
                def userLicenses(self) -> UserLicensesResource: ...

            def estimateDataSize(
                self,
                *,
                location: str,
                body: GoogleCloudDiscoveryengineV1alphaEstimateDataSizeRequest = ...,
                **kwargs: typing.Any,
            ) -> GoogleLongrunningOperationHttpRequest: ...
            def getAclConfig(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleCloudDiscoveryengineV1alphaAclConfigHttpRequest: ...
            def getCmekConfig(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleCloudDiscoveryengineV1alphaCmekConfigHttpRequest: ...
            def obtainCrawlRate(
                self,
                *,
                location: str,
                body: GoogleCloudDiscoveryengineV1alphaObtainCrawlRateRequest = ...,
                **kwargs: typing.Any,
            ) -> (
                GoogleCloudDiscoveryengineV1alphaObtainCrawlRateResponseHttpRequest
            ): ...
            def queryConfigurablePricingUsageStats(
                self,
                *,
                project: str,
                location: str,
                metricTypes: typing_extensions.Literal[
                    "BILLING_METRIC_TYPE_UNSPECIFIED",
                    "DAILY_MDN_QPM",
                    "DAILY_MIN_QPM",
                    "DAILY_MAX_QPM",
                    "DAILY_SEARCH_REQUEST",
                    "TOTAL_STORAGE",
                ]
                | _list[
                    typing_extensions.Literal[
                        "BILLING_METRIC_TYPE_UNSPECIFIED",
                        "DAILY_MDN_QPM",
                        "DAILY_MIN_QPM",
                        "DAILY_MAX_QPM",
                        "DAILY_SEARCH_REQUEST",
                        "TOTAL_STORAGE",
                    ]
                ] = ...,
                timeRange_endDate_day: int = ...,
                timeRange_endDate_month: int = ...,
                timeRange_endDate_year: int = ...,
                timeRange_startDate_day: int = ...,
                timeRange_startDate_month: int = ...,
                timeRange_startDate_year: int = ...,
                **kwargs: typing.Any,
            ) -> GoogleCloudDiscoveryengineV1alphaQueryConfigurablePricingUsageStatsResponseHttpRequest: ...
            def removeDedicatedCrawlRate(
                self,
                *,
                location: str,
                body: GoogleCloudDiscoveryengineV1alphaRemoveDedicatedCrawlRateRequest = ...,
                **kwargs: typing.Any,
            ) -> GoogleLongrunningOperationHttpRequest: ...
            def setDedicatedCrawlRate(
                self,
                *,
                location: str,
                body: GoogleCloudDiscoveryengineV1alphaSetDedicatedCrawlRateRequest = ...,
                **kwargs: typing.Any,
            ) -> GoogleLongrunningOperationHttpRequest: ...
            def setUpDataConnector(
                self,
                *,
                parent: str,
                body: GoogleCloudDiscoveryengineV1alphaSetUpDataConnectorRequest = ...,
                **kwargs: typing.Any,
            ) -> GoogleLongrunningOperationHttpRequest: ...
            def setUpDataConnectorV2(
                self,
                *,
                parent: str,
                body: GoogleCloudDiscoveryengineV1alphaDataConnector = ...,
                collectionDisplayName: str = ...,
                collectionId: str = ...,
                **kwargs: typing.Any,
            ) -> GoogleLongrunningOperationHttpRequest: ...
            def updateAclConfig(
                self,
                *,
                name: str,
                body: GoogleCloudDiscoveryengineV1alphaAclConfig = ...,
                **kwargs: typing.Any,
            ) -> GoogleCloudDiscoveryengineV1alphaAclConfigHttpRequest: ...
            def updateCmekConfig(
                self,
                *,
                name: str,
                body: GoogleCloudDiscoveryengineV1alphaCmekConfig = ...,
                setDefault: bool = ...,
                **kwargs: typing.Any,
            ) -> GoogleLongrunningOperationHttpRequest: ...
            def authorizations(self) -> AuthorizationsResource: ...
            def cmekConfigs(self) -> CmekConfigsResource: ...
            def collections(self) -> CollectionsResource: ...
            def dataStores(self) -> DataStoresResource: ...
            def evaluations(self) -> EvaluationsResource: ...
            def groundingConfigs(self) -> GroundingConfigsResource: ...
            def identityMappingStores(self) -> IdentityMappingStoresResource: ...
            def licenseConfigs(self) -> LicenseConfigsResource: ...
            def notebooks(self) -> NotebooksResource: ...
            def operations(self) -> OperationsResource: ...
            def podcasts(self) -> PodcastsResource: ...
            def rankingConfigs(self) -> RankingConfigsResource: ...
            def requirements(self) -> RequirementsResource: ...
            def sampleQuerySets(self) -> SampleQuerySetsResource: ...
            def userEvents(self) -> UserEventsResource: ...
            def userStores(self) -> UserStoresResource: ...

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
                returnPartialSuccess: bool = ...,
                **kwargs: typing.Any,
            ) -> GoogleLongrunningListOperationsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: GoogleLongrunningListOperationsResponseHttpRequest,
                previous_response: GoogleLongrunningListOperationsResponse,
            ) -> GoogleLongrunningListOperationsResponseHttpRequest | None: ...

        def get(
            self, *, name: str, **kwargs: typing.Any
        ) -> GoogleCloudDiscoveryengineV1alphaProjectHttpRequest: ...
        def patch(
            self,
            *,
            name: str,
            body: GoogleCloudDiscoveryengineV1alphaProject = ...,
            updateMask: str = ...,
            **kwargs: typing.Any,
        ) -> GoogleCloudDiscoveryengineV1alphaProjectHttpRequest: ...
        def provision(
            self,
            *,
            name: str,
            body: GoogleCloudDiscoveryengineV1alphaProvisionProjectRequest = ...,
            **kwargs: typing.Any,
        ) -> GoogleLongrunningOperationHttpRequest: ...
        def reportConsentChange(
            self,
            *,
            project: str,
            body: GoogleCloudDiscoveryengineV1alphaReportConsentChangeRequest = ...,
            **kwargs: typing.Any,
        ) -> GoogleCloudDiscoveryengineV1alphaProjectHttpRequest: ...
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
    def billingAccounts(self) -> BillingAccountsResource: ...
    def projects(self) -> ProjectsResource: ...

@typing.type_check_only
class GoogleApiHttpBodyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleApiHttpBody: ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAclConfigHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDiscoveryengineV1alphaAclConfig: ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAcquireAccessTokenResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDiscoveryengineV1alphaAcquireAccessTokenResponse: ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAdvancedCompleteQueryResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDiscoveryengineV1alphaAdvancedCompleteQueryResponse: ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAgentHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDiscoveryengineV1alphaAgent: ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAnalyticsConfigHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDiscoveryengineV1alphaAnalyticsConfig: ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAnswerHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDiscoveryengineV1alphaAnswer: ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAnswerQueryResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDiscoveryengineV1alphaAnswerQueryResponse: ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAssistantHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDiscoveryengineV1alphaAssistant: ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAuthorizationHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDiscoveryengineV1alphaAuthorization: ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaBatchGetDocumentsMetadataResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDiscoveryengineV1alphaBatchGetDocumentsMetadataResponse: ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaBillingAccountLicenseConfigHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDiscoveryengineV1alphaBillingAccountLicenseConfig: ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaBranchHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDiscoveryengineV1alphaBranch: ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaCannedQueryHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDiscoveryengineV1alphaCannedQuery: ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaCheckGroundingResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDiscoveryengineV1alphaCheckGroundingResponse: ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaCheckRefreshTokenResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDiscoveryengineV1alphaCheckRefreshTokenResponse: ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaCheckRequirementResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDiscoveryengineV1alphaCheckRequirementResponse: ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaChunkHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDiscoveryengineV1alphaChunk: ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaCmekConfigHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDiscoveryengineV1alphaCmekConfig: ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaCollectionHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDiscoveryengineV1alphaCollection: ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaCompleteQueryResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDiscoveryengineV1alphaCompleteQueryResponse: ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaConnectorRunHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDiscoveryengineV1alphaConnectorRun: ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaControlHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDiscoveryengineV1alphaControl: ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaConversationHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDiscoveryengineV1alphaConversation: ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaConverseConversationResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDiscoveryengineV1alphaConverseConversationResponse: ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaDataConnectorHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDiscoveryengineV1alphaDataConnector: ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaDataStoreHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDiscoveryengineV1alphaDataStore: ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaDistributeLicenseConfigResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDiscoveryengineV1alphaDistributeLicenseConfigResponse: ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaDocumentHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDiscoveryengineV1alphaDocument: ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaDocumentProcessingConfigHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDiscoveryengineV1alphaDocumentProcessingConfig: ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaEngineHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDiscoveryengineV1alphaEngine: ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaEvaluationHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDiscoveryengineV1alphaEvaluation: ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaFetchDomainVerificationStatusResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDiscoveryengineV1alphaFetchDomainVerificationStatusResponse: ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaFetchSitemapsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDiscoveryengineV1alphaFetchSitemapsResponse: ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaGetAgentViewResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDiscoveryengineV1alphaGetAgentViewResponse: ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaGetConnectorSecretResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDiscoveryengineV1alphaGetConnectorSecretResponse: ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaGetUriPatternDocumentDataResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDiscoveryengineV1alphaGetUriPatternDocumentDataResponse: ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaIdentityMappingStoreHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDiscoveryengineV1alphaIdentityMappingStore: ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaImportAgentFileResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDiscoveryengineV1alphaImportAgentFileResponse: ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaLicenseConfigHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDiscoveryengineV1alphaLicenseConfig: ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaListAgentsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDiscoveryengineV1alphaListAgentsResponse: ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaListAssistantsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDiscoveryengineV1alphaListAssistantsResponse: ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaListAuthorizationsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDiscoveryengineV1alphaListAuthorizationsResponse: ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaListAvailableAgentViewsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDiscoveryengineV1alphaListAvailableAgentViewsResponse: ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaListBillingAccountLicenseConfigsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDiscoveryengineV1alphaListBillingAccountLicenseConfigsResponse: ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaListBranchesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDiscoveryengineV1alphaListBranchesResponse: ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaListCannedQueriesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDiscoveryengineV1alphaListCannedQueriesResponse: ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaListChunksResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDiscoveryengineV1alphaListChunksResponse: ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaListCmekConfigsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDiscoveryengineV1alphaListCmekConfigsResponse: ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaListCollectionsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDiscoveryengineV1alphaListCollectionsResponse: ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaListConnectorRunsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDiscoveryengineV1alphaListConnectorRunsResponse: ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaListControlsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDiscoveryengineV1alphaListControlsResponse: ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaListConversationsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDiscoveryengineV1alphaListConversationsResponse: ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaListCustomModelsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDiscoveryengineV1alphaListCustomModelsResponse: ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaListDataStoresResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDiscoveryengineV1alphaListDataStoresResponse: ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaListDocumentsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDiscoveryengineV1alphaListDocumentsResponse: ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaListEnginesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDiscoveryengineV1alphaListEnginesResponse: ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaListEvaluationResultsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDiscoveryengineV1alphaListEvaluationResultsResponse: ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaListEvaluationsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDiscoveryengineV1alphaListEvaluationsResponse: ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaListFilesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDiscoveryengineV1alphaListFilesResponse: ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaListIdentityMappingStoresResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDiscoveryengineV1alphaListIdentityMappingStoresResponse: ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaListIdentityMappingsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDiscoveryengineV1alphaListIdentityMappingsResponse: ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaListLicenseConfigsUsageStatsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDiscoveryengineV1alphaListLicenseConfigsUsageStatsResponse: ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaListSampleQueriesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDiscoveryengineV1alphaListSampleQueriesResponse: ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaListSampleQuerySetsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDiscoveryengineV1alphaListSampleQuerySetsResponse: ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaListSchemasResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDiscoveryengineV1alphaListSchemasResponse: ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaListServingConfigsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDiscoveryengineV1alphaListServingConfigsResponse: ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaListSessionsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDiscoveryengineV1alphaListSessionsResponse: ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaListTargetSitesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDiscoveryengineV1alphaListTargetSitesResponse: ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaListUserLicensesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDiscoveryengineV1alphaListUserLicensesResponse: ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaObtainCrawlRateResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDiscoveryengineV1alphaObtainCrawlRateResponse: ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaProcessedDocumentHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDiscoveryengineV1alphaProcessedDocument: ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaProjectHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDiscoveryengineV1alphaProject: ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaQueryConfigurablePricingUsageStatsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> (
        GoogleCloudDiscoveryengineV1alphaQueryConfigurablePricingUsageStatsResponse
    ): ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaRankResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDiscoveryengineV1alphaRankResponse: ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaRecommendResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDiscoveryengineV1alphaRecommendResponse: ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaRemoveSuggestionResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDiscoveryengineV1alphaRemoveSuggestionResponse: ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaRetractLicenseConfigResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDiscoveryengineV1alphaRetractLicenseConfigResponse: ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSampleQueryHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDiscoveryengineV1alphaSampleQuery: ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSampleQuerySetHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDiscoveryengineV1alphaSampleQuerySet: ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSchemaHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDiscoveryengineV1alphaSchema: ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSearchResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDiscoveryengineV1alphaSearchResponse: ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaServingConfigHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDiscoveryengineV1alphaServingConfig: ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSessionHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDiscoveryengineV1alphaSession: ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSiteSearchEngineHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDiscoveryengineV1alphaSiteSearchEngine: ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaStreamAssistResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDiscoveryengineV1alphaStreamAssistResponse: ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaTargetSiteHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDiscoveryengineV1alphaTargetSite: ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaUserEventHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDiscoveryengineV1alphaUserEvent: ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaUserStoreHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDiscoveryengineV1alphaUserStore: ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaWidgetConfigHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDiscoveryengineV1alphaWidgetConfig: ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaWorkspaceSettingsHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDiscoveryengineV1alphaWorkspaceSettings: ...

@typing.type_check_only
class GoogleCloudNotebooklmV1alphaBatchCreateSourcesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudNotebooklmV1alphaBatchCreateSourcesResponse: ...

@typing.type_check_only
class GoogleCloudNotebooklmV1alphaCreateAudioOverviewResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudNotebooklmV1alphaCreateAudioOverviewResponse: ...

@typing.type_check_only
class GoogleCloudNotebooklmV1alphaListRecentlyViewedNotebooksResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudNotebooklmV1alphaListRecentlyViewedNotebooksResponse: ...

@typing.type_check_only
class GoogleCloudNotebooklmV1alphaNotebookHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudNotebooklmV1alphaNotebook: ...

@typing.type_check_only
class GoogleCloudNotebooklmV1alphaShareNotebookResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudNotebooklmV1alphaShareNotebookResponse: ...

@typing.type_check_only
class GoogleCloudNotebooklmV1alphaSourceHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudNotebooklmV1alphaSource: ...

@typing.type_check_only
class GoogleIamV1PolicyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleIamV1Policy: ...

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
