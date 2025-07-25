import collections.abc
import typing

import httplib2
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http

from .schemas import *

_list = list

@typing.type_check_only
class CloudRetailResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class ProjectsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class LocationsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class CatalogsResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class AttributesConfigResource(googleapiclient.discovery.Resource):
                    def addCatalogAttribute(
                        self,
                        *,
                        attributesConfig: str,
                        body: GoogleCloudRetailV2betaAddCatalogAttributeRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudRetailV2betaAttributesConfigHttpRequest: ...
                    def batchRemoveCatalogAttributes(
                        self,
                        *,
                        attributesConfig: str,
                        body: GoogleCloudRetailV2betaBatchRemoveCatalogAttributesRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudRetailV2betaBatchRemoveCatalogAttributesResponseHttpRequest: ...
                    def removeCatalogAttribute(
                        self,
                        *,
                        attributesConfig: str,
                        body: GoogleCloudRetailV2betaRemoveCatalogAttributeRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudRetailV2betaAttributesConfigHttpRequest: ...
                    def replaceCatalogAttribute(
                        self,
                        *,
                        attributesConfig: str,
                        body: GoogleCloudRetailV2betaReplaceCatalogAttributeRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudRetailV2betaAttributesConfigHttpRequest: ...

                @typing.type_check_only
                class BranchesResource(googleapiclient.discovery.Resource):
                    @typing.type_check_only
                    class OperationsResource(googleapiclient.discovery.Resource):
                        def get(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> GoogleLongrunningOperationHttpRequest: ...

                    @typing.type_check_only
                    class ProductsResource(googleapiclient.discovery.Resource):
                        def addFulfillmentPlaces(
                            self,
                            *,
                            product: str,
                            body: GoogleCloudRetailV2betaAddFulfillmentPlacesRequest = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleLongrunningOperationHttpRequest: ...
                        def addLocalInventories(
                            self,
                            *,
                            product: str,
                            body: GoogleCloudRetailV2betaAddLocalInventoriesRequest = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleLongrunningOperationHttpRequest: ...
                        def create(
                            self,
                            *,
                            parent: str,
                            body: GoogleCloudRetailV2betaProduct = ...,
                            productId: str = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudRetailV2betaProductHttpRequest: ...
                        def delete(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> GoogleProtobufEmptyHttpRequest: ...
                        def export(
                            self,
                            *,
                            parent: str,
                            body: GoogleCloudRetailV2betaExportProductsRequest = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleLongrunningOperationHttpRequest: ...
                        def get(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> GoogleCloudRetailV2betaProductHttpRequest: ...
                        def import_(
                            self,
                            *,
                            parent: str,
                            body: GoogleCloudRetailV2betaImportProductsRequest = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleLongrunningOperationHttpRequest: ...
                        def list(
                            self,
                            *,
                            parent: str,
                            filter: str = ...,
                            pageSize: int = ...,
                            pageToken: str = ...,
                            readMask: str = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudRetailV2betaListProductsResponseHttpRequest: ...
                        def list_next(
                            self,
                            previous_request: GoogleCloudRetailV2betaListProductsResponseHttpRequest,
                            previous_response: GoogleCloudRetailV2betaListProductsResponse,
                        ) -> (
                            GoogleCloudRetailV2betaListProductsResponseHttpRequest
                            | None
                        ): ...
                        def patch(
                            self,
                            *,
                            name: str,
                            body: GoogleCloudRetailV2betaProduct = ...,
                            allowMissing: bool = ...,
                            updateMask: str = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudRetailV2betaProductHttpRequest: ...
                        def purge(
                            self,
                            *,
                            parent: str,
                            body: GoogleCloudRetailV2betaPurgeProductsRequest = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleLongrunningOperationHttpRequest: ...
                        def removeFulfillmentPlaces(
                            self,
                            *,
                            product: str,
                            body: GoogleCloudRetailV2betaRemoveFulfillmentPlacesRequest = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleLongrunningOperationHttpRequest: ...
                        def removeLocalInventories(
                            self,
                            *,
                            product: str,
                            body: GoogleCloudRetailV2betaRemoveLocalInventoriesRequest = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleLongrunningOperationHttpRequest: ...
                        def setInventory(
                            self,
                            *,
                            name: str,
                            body: GoogleCloudRetailV2betaSetInventoryRequest = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleLongrunningOperationHttpRequest: ...

                    def operations(self) -> OperationsResource: ...
                    def products(self) -> ProductsResource: ...

                @typing.type_check_only
                class CompletionDataResource(googleapiclient.discovery.Resource):
                    def import_(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudRetailV2betaImportCompletionDataRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleLongrunningOperationHttpRequest: ...

                @typing.type_check_only
                class ControlsResource(googleapiclient.discovery.Resource):
                    def create(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudRetailV2betaControl = ...,
                        controlId: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudRetailV2betaControlHttpRequest: ...
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleProtobufEmptyHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleCloudRetailV2betaControlHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudRetailV2betaListControlsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudRetailV2betaListControlsResponseHttpRequest,
                        previous_response: GoogleCloudRetailV2betaListControlsResponse,
                    ) -> (
                        GoogleCloudRetailV2betaListControlsResponseHttpRequest | None
                    ): ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudRetailV2betaControl = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudRetailV2betaControlHttpRequest: ...

                @typing.type_check_only
                class GenerativeQuestionResource(googleapiclient.discovery.Resource):
                    def batchUpdate(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudRetailV2betaBatchUpdateGenerativeQuestionConfigsRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudRetailV2betaBatchUpdateGenerativeQuestionConfigsResponseHttpRequest: ...

                @typing.type_check_only
                class GenerativeQuestionsResource(googleapiclient.discovery.Resource):
                    def list(
                        self, *, parent: str, **kwargs: typing.Any
                    ) -> GoogleCloudRetailV2betaListGenerativeQuestionConfigsResponseHttpRequest: ...

                @typing.type_check_only
                class ModelsResource(googleapiclient.discovery.Resource):
                    def create(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudRetailV2betaModel = ...,
                        dryRun: bool = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleProtobufEmptyHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleCloudRetailV2betaModelHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudRetailV2betaListModelsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudRetailV2betaListModelsResponseHttpRequest,
                        previous_response: GoogleCloudRetailV2betaListModelsResponse,
                    ) -> (
                        GoogleCloudRetailV2betaListModelsResponseHttpRequest | None
                    ): ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudRetailV2betaModel = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudRetailV2betaModelHttpRequest: ...
                    def pause(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudRetailV2betaPauseModelRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudRetailV2betaModelHttpRequest: ...
                    def resume(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudRetailV2betaResumeModelRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudRetailV2betaModelHttpRequest: ...
                    def tune(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudRetailV2betaTuneModelRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleLongrunningOperationHttpRequest: ...

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
                class PlacementsResource(googleapiclient.discovery.Resource):
                    def predict(
                        self,
                        *,
                        placement: str,
                        body: GoogleCloudRetailV2betaPredictRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudRetailV2betaPredictResponseHttpRequest: ...
                    def search(
                        self,
                        *,
                        placement: str,
                        body: GoogleCloudRetailV2betaSearchRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudRetailV2betaSearchResponseHttpRequest: ...
                    def search_next(
                        self,
                        previous_request: GoogleCloudRetailV2betaSearchResponseHttpRequest,
                        previous_response: GoogleCloudRetailV2betaSearchResponse,
                    ) -> GoogleCloudRetailV2betaSearchResponseHttpRequest | None: ...

                @typing.type_check_only
                class ServingConfigsResource(googleapiclient.discovery.Resource):
                    def addControl(
                        self,
                        *,
                        servingConfig: str,
                        body: GoogleCloudRetailV2betaAddControlRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudRetailV2betaServingConfigHttpRequest: ...
                    def create(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudRetailV2betaServingConfig = ...,
                        servingConfigId: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudRetailV2betaServingConfigHttpRequest: ...
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleProtobufEmptyHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleCloudRetailV2betaServingConfigHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
                    ) -> (
                        GoogleCloudRetailV2betaListServingConfigsResponseHttpRequest
                    ): ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudRetailV2betaListServingConfigsResponseHttpRequest,
                        previous_response: GoogleCloudRetailV2betaListServingConfigsResponse,
                    ) -> (
                        GoogleCloudRetailV2betaListServingConfigsResponseHttpRequest
                        | None
                    ): ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudRetailV2betaServingConfig = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudRetailV2betaServingConfigHttpRequest: ...
                    def predict(
                        self,
                        *,
                        placement: str,
                        body: GoogleCloudRetailV2betaPredictRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudRetailV2betaPredictResponseHttpRequest: ...
                    def removeControl(
                        self,
                        *,
                        servingConfig: str,
                        body: GoogleCloudRetailV2betaRemoveControlRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudRetailV2betaServingConfigHttpRequest: ...
                    def search(
                        self,
                        *,
                        placement: str,
                        body: GoogleCloudRetailV2betaSearchRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudRetailV2betaSearchResponseHttpRequest: ...
                    def search_next(
                        self,
                        previous_request: GoogleCloudRetailV2betaSearchResponseHttpRequest,
                        previous_response: GoogleCloudRetailV2betaSearchResponse,
                    ) -> GoogleCloudRetailV2betaSearchResponseHttpRequest | None: ...

                @typing.type_check_only
                class UserEventsResource(googleapiclient.discovery.Resource):
                    def collect(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudRetailV2betaCollectUserEventRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleApiHttpBodyHttpRequest: ...
                    def export(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudRetailV2betaExportUserEventsRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def import_(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudRetailV2betaImportUserEventsRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def purge(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudRetailV2betaPurgeUserEventsRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def rejoin(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudRetailV2betaRejoinUserEventsRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def write(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudRetailV2betaUserEvent = ...,
                        writeAsync: bool = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudRetailV2betaUserEventHttpRequest: ...

                def completeQuery(
                    self,
                    *,
                    catalog: str,
                    dataset: str = ...,
                    deviceType: str = ...,
                    enableAttributeSuggestions: bool = ...,
                    entity: str = ...,
                    languageCodes: str | _list[str] = ...,
                    maxSuggestions: int = ...,
                    query: str = ...,
                    visitorId: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudRetailV2betaCompleteQueryResponseHttpRequest: ...
                def exportAnalyticsMetrics(
                    self,
                    *,
                    catalog: str,
                    body: GoogleCloudRetailV2betaExportAnalyticsMetricsRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def getAttributesConfig(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudRetailV2betaAttributesConfigHttpRequest: ...
                def getCompletionConfig(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudRetailV2betaCompletionConfigHttpRequest: ...
                def getConversationalSearchCustomizationConfig(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudRetailV2betaConversationalSearchCustomizationConfigHttpRequest: ...
                def getDefaultBranch(
                    self, *, catalog: str, **kwargs: typing.Any
                ) -> GoogleCloudRetailV2betaGetDefaultBranchResponseHttpRequest: ...
                def getGenerativeQuestionFeature(
                    self, *, catalog: str, **kwargs: typing.Any
                ) -> (
                    GoogleCloudRetailV2betaGenerativeQuestionsFeatureConfigHttpRequest
                ): ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudRetailV2betaListCatalogsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudRetailV2betaListCatalogsResponseHttpRequest,
                    previous_response: GoogleCloudRetailV2betaListCatalogsResponse,
                ) -> GoogleCloudRetailV2betaListCatalogsResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudRetailV2betaCatalog = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudRetailV2betaCatalogHttpRequest: ...
                def setDefaultBranch(
                    self,
                    *,
                    catalog: str,
                    body: GoogleCloudRetailV2betaSetDefaultBranchRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleProtobufEmptyHttpRequest: ...
                def updateAttributesConfig(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudRetailV2betaAttributesConfig = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudRetailV2betaAttributesConfigHttpRequest: ...
                def updateCompletionConfig(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudRetailV2betaCompletionConfig = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudRetailV2betaCompletionConfigHttpRequest: ...
                def updateConversationalSearchCustomizationConfig(
                    self,
                    *,
                    catalog: str,
                    body: GoogleCloudRetailV2betaConversationalSearchCustomizationConfig = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudRetailV2betaConversationalSearchCustomizationConfigHttpRequest: ...
                def updateGenerativeQuestion(
                    self,
                    *,
                    catalog: str,
                    body: GoogleCloudRetailV2betaGenerativeQuestionConfig = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudRetailV2betaGenerativeQuestionConfigHttpRequest: ...
                def updateGenerativeQuestionFeature(
                    self,
                    *,
                    catalog: str,
                    body: GoogleCloudRetailV2betaGenerativeQuestionsFeatureConfig = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> (
                    GoogleCloudRetailV2betaGenerativeQuestionsFeatureConfigHttpRequest
                ): ...
                def attributesConfig(self) -> AttributesConfigResource: ...
                def branches(self) -> BranchesResource: ...
                def completionData(self) -> CompletionDataResource: ...
                def controls(self) -> ControlsResource: ...
                def generativeQuestion(self) -> GenerativeQuestionResource: ...
                def generativeQuestions(self) -> GenerativeQuestionsResource: ...
                def models(self) -> ModelsResource: ...
                def operations(self) -> OperationsResource: ...
                def placements(self) -> PlacementsResource: ...
                def servingConfigs(self) -> ServingConfigsResource: ...
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

            def catalogs(self) -> CatalogsResource: ...
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

        def getAlertConfig(
            self, *, name: str, **kwargs: typing.Any
        ) -> GoogleCloudRetailV2betaAlertConfigHttpRequest: ...
        def updateAlertConfig(
            self,
            *,
            name: str,
            body: GoogleCloudRetailV2betaAlertConfig = ...,
            updateMask: str = ...,
            **kwargs: typing.Any,
        ) -> GoogleCloudRetailV2betaAlertConfigHttpRequest: ...
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
class GoogleCloudRetailV2betaAlertConfigHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudRetailV2betaAlertConfig: ...

@typing.type_check_only
class GoogleCloudRetailV2betaAttributesConfigHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudRetailV2betaAttributesConfig: ...

@typing.type_check_only
class GoogleCloudRetailV2betaBatchRemoveCatalogAttributesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudRetailV2betaBatchRemoveCatalogAttributesResponse: ...

@typing.type_check_only
class GoogleCloudRetailV2betaBatchUpdateGenerativeQuestionConfigsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudRetailV2betaBatchUpdateGenerativeQuestionConfigsResponse: ...

@typing.type_check_only
class GoogleCloudRetailV2betaCatalogHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudRetailV2betaCatalog: ...

@typing.type_check_only
class GoogleCloudRetailV2betaCompleteQueryResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudRetailV2betaCompleteQueryResponse: ...

@typing.type_check_only
class GoogleCloudRetailV2betaCompletionConfigHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudRetailV2betaCompletionConfig: ...

@typing.type_check_only
class GoogleCloudRetailV2betaControlHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudRetailV2betaControl: ...

@typing.type_check_only
class GoogleCloudRetailV2betaConversationalSearchCustomizationConfigHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudRetailV2betaConversationalSearchCustomizationConfig: ...

@typing.type_check_only
class GoogleCloudRetailV2betaGenerativeQuestionConfigHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudRetailV2betaGenerativeQuestionConfig: ...

@typing.type_check_only
class GoogleCloudRetailV2betaGenerativeQuestionsFeatureConfigHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudRetailV2betaGenerativeQuestionsFeatureConfig: ...

@typing.type_check_only
class GoogleCloudRetailV2betaGetDefaultBranchResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudRetailV2betaGetDefaultBranchResponse: ...

@typing.type_check_only
class GoogleCloudRetailV2betaListCatalogsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudRetailV2betaListCatalogsResponse: ...

@typing.type_check_only
class GoogleCloudRetailV2betaListControlsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudRetailV2betaListControlsResponse: ...

@typing.type_check_only
class GoogleCloudRetailV2betaListGenerativeQuestionConfigsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudRetailV2betaListGenerativeQuestionConfigsResponse: ...

@typing.type_check_only
class GoogleCloudRetailV2betaListModelsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudRetailV2betaListModelsResponse: ...

@typing.type_check_only
class GoogleCloudRetailV2betaListProductsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudRetailV2betaListProductsResponse: ...

@typing.type_check_only
class GoogleCloudRetailV2betaListServingConfigsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudRetailV2betaListServingConfigsResponse: ...

@typing.type_check_only
class GoogleCloudRetailV2betaModelHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudRetailV2betaModel: ...

@typing.type_check_only
class GoogleCloudRetailV2betaPredictResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudRetailV2betaPredictResponse: ...

@typing.type_check_only
class GoogleCloudRetailV2betaProductHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudRetailV2betaProduct: ...

@typing.type_check_only
class GoogleCloudRetailV2betaSearchResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudRetailV2betaSearchResponse: ...

@typing.type_check_only
class GoogleCloudRetailV2betaServingConfigHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudRetailV2betaServingConfig: ...

@typing.type_check_only
class GoogleCloudRetailV2betaUserEventHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudRetailV2betaUserEvent: ...

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
