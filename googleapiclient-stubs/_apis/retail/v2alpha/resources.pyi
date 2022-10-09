import collections.abc
import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

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
                        body: GoogleCloudRetailV2alphaAddCatalogAttributeRequest = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudRetailV2alphaAttributesConfigHttpRequest: ...
                    def batchRemoveCatalogAttributes(
                        self,
                        *,
                        attributesConfig: str,
                        body: GoogleCloudRetailV2alphaBatchRemoveCatalogAttributesRequest = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudRetailV2alphaBatchRemoveCatalogAttributesResponseHttpRequest: ...
                    def removeCatalogAttribute(
                        self,
                        *,
                        attributesConfig: str,
                        body: GoogleCloudRetailV2alphaRemoveCatalogAttributeRequest = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudRetailV2alphaAttributesConfigHttpRequest: ...
                    def replaceCatalogAttribute(
                        self,
                        *,
                        attributesConfig: str,
                        body: GoogleCloudRetailV2alphaReplaceCatalogAttributeRequest = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudRetailV2alphaAttributesConfigHttpRequest: ...

                @typing.type_check_only
                class BranchesResource(googleapiclient.discovery.Resource):
                    @typing.type_check_only
                    class OperationsResource(googleapiclient.discovery.Resource):
                        def get(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> GoogleLongrunningOperationHttpRequest: ...

                    @typing.type_check_only
                    class PlacesResource(googleapiclient.discovery.Resource):
                        @typing.type_check_only
                        class OperationsResource(googleapiclient.discovery.Resource):
                            def get(
                                self, *, name: str, **kwargs: typing.Any
                            ) -> GoogleLongrunningOperationHttpRequest: ...

                        def operations(self) -> OperationsResource: ...

                    @typing.type_check_only
                    class ProductsResource(googleapiclient.discovery.Resource):
                        def addFulfillmentPlaces(
                            self,
                            *,
                            product: str,
                            body: GoogleCloudRetailV2alphaAddFulfillmentPlacesRequest = ...,
                            **kwargs: typing.Any
                        ) -> GoogleLongrunningOperationHttpRequest: ...
                        def addLocalInventories(
                            self,
                            *,
                            product: str,
                            body: GoogleCloudRetailV2alphaAddLocalInventoriesRequest = ...,
                            **kwargs: typing.Any
                        ) -> GoogleLongrunningOperationHttpRequest: ...
                        def create(
                            self,
                            *,
                            parent: str,
                            body: GoogleCloudRetailV2alphaProduct = ...,
                            productId: str = ...,
                            **kwargs: typing.Any
                        ) -> GoogleCloudRetailV2alphaProductHttpRequest: ...
                        def delete(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> GoogleProtobufEmptyHttpRequest: ...
                        def get(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> GoogleCloudRetailV2alphaProductHttpRequest: ...
                        def import_(
                            self,
                            *,
                            parent: str,
                            body: GoogleCloudRetailV2alphaImportProductsRequest = ...,
                            **kwargs: typing.Any
                        ) -> GoogleLongrunningOperationHttpRequest: ...
                        def list(
                            self,
                            *,
                            parent: str,
                            filter: str = ...,
                            pageSize: int = ...,
                            pageToken: str = ...,
                            readMask: str = ...,
                            requireTotalSize: bool = ...,
                            **kwargs: typing.Any
                        ) -> GoogleCloudRetailV2alphaListProductsResponseHttpRequest: ...
                        def list_next(
                            self,
                            previous_request: GoogleCloudRetailV2alphaListProductsResponseHttpRequest,
                            previous_response: GoogleCloudRetailV2alphaListProductsResponse,
                        ) -> GoogleCloudRetailV2alphaListProductsResponseHttpRequest | None: ...
                        def patch(
                            self,
                            *,
                            name: str,
                            body: GoogleCloudRetailV2alphaProduct = ...,
                            allowMissing: bool = ...,
                            updateMask: str = ...,
                            **kwargs: typing.Any
                        ) -> GoogleCloudRetailV2alphaProductHttpRequest: ...
                        def purge(
                            self,
                            *,
                            parent: str,
                            body: GoogleCloudRetailV2alphaPurgeProductsRequest = ...,
                            **kwargs: typing.Any
                        ) -> GoogleLongrunningOperationHttpRequest: ...
                        def removeFulfillmentPlaces(
                            self,
                            *,
                            product: str,
                            body: GoogleCloudRetailV2alphaRemoveFulfillmentPlacesRequest = ...,
                            **kwargs: typing.Any
                        ) -> GoogleLongrunningOperationHttpRequest: ...
                        def removeLocalInventories(
                            self,
                            *,
                            product: str,
                            body: GoogleCloudRetailV2alphaRemoveLocalInventoriesRequest = ...,
                            **kwargs: typing.Any
                        ) -> GoogleLongrunningOperationHttpRequest: ...
                        def setInventory(
                            self,
                            *,
                            name: str,
                            body: GoogleCloudRetailV2alphaSetInventoryRequest = ...,
                            **kwargs: typing.Any
                        ) -> GoogleLongrunningOperationHttpRequest: ...

                    def operations(self) -> OperationsResource: ...
                    def places(self) -> PlacesResource: ...
                    def products(self) -> ProductsResource: ...

                @typing.type_check_only
                class CompletionDataResource(googleapiclient.discovery.Resource):
                    def import_(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudRetailV2alphaImportCompletionDataRequest = ...,
                        **kwargs: typing.Any
                    ) -> GoogleLongrunningOperationHttpRequest: ...

                @typing.type_check_only
                class ControlsResource(googleapiclient.discovery.Resource):
                    def create(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudRetailV2alphaControl = ...,
                        controlId: str = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudRetailV2alphaControlHttpRequest: ...
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleProtobufEmptyHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleCloudRetailV2alphaControlHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudRetailV2alphaListControlsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudRetailV2alphaListControlsResponseHttpRequest,
                        previous_response: GoogleCloudRetailV2alphaListControlsResponse,
                    ) -> GoogleCloudRetailV2alphaListControlsResponseHttpRequest | None: ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudRetailV2alphaControl = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudRetailV2alphaControlHttpRequest: ...

                @typing.type_check_only
                class ModelsResource(googleapiclient.discovery.Resource):
                    def create(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudRetailV2alphaModel = ...,
                        dryRun: bool = ...,
                        **kwargs: typing.Any
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleProtobufEmptyHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudRetailV2alphaListModelsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudRetailV2alphaListModelsResponseHttpRequest,
                        previous_response: GoogleCloudRetailV2alphaListModelsResponse,
                    ) -> GoogleCloudRetailV2alphaListModelsResponseHttpRequest | None: ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudRetailV2alphaModel = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudRetailV2alphaModelHttpRequest: ...
                    def pause(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudRetailV2alphaPauseModelRequest = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudRetailV2alphaModelHttpRequest: ...
                    def resume(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudRetailV2alphaResumeModelRequest = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudRetailV2alphaModelHttpRequest: ...
                    def tune(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudRetailV2alphaTuneModelRequest = ...,
                        **kwargs: typing.Any
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
                        **kwargs: typing.Any
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
                        body: GoogleCloudRetailV2alphaPredictRequest = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudRetailV2alphaPredictResponseHttpRequest: ...
                    def search(
                        self,
                        *,
                        placement: str,
                        body: GoogleCloudRetailV2alphaSearchRequest = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudRetailV2alphaSearchResponseHttpRequest: ...
                    def search_next(
                        self,
                        previous_request: GoogleCloudRetailV2alphaSearchResponseHttpRequest,
                        previous_response: GoogleCloudRetailV2alphaSearchResponse,
                    ) -> GoogleCloudRetailV2alphaSearchResponseHttpRequest | None: ...

                @typing.type_check_only
                class ServingConfigsResource(googleapiclient.discovery.Resource):
                    def addControl(
                        self,
                        *,
                        servingConfig: str,
                        body: GoogleCloudRetailV2alphaAddControlRequest = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudRetailV2alphaServingConfigHttpRequest: ...
                    def create(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudRetailV2alphaServingConfig = ...,
                        servingConfigId: str = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudRetailV2alphaServingConfigHttpRequest: ...
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleProtobufEmptyHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleCloudRetailV2alphaServingConfigHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudRetailV2alphaListServingConfigsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudRetailV2alphaListServingConfigsResponseHttpRequest,
                        previous_response: GoogleCloudRetailV2alphaListServingConfigsResponse,
                    ) -> GoogleCloudRetailV2alphaListServingConfigsResponseHttpRequest | None: ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudRetailV2alphaServingConfig = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudRetailV2alphaServingConfigHttpRequest: ...
                    def predict(
                        self,
                        *,
                        placement: str,
                        body: GoogleCloudRetailV2alphaPredictRequest = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudRetailV2alphaPredictResponseHttpRequest: ...
                    def removeControl(
                        self,
                        *,
                        servingConfig: str,
                        body: GoogleCloudRetailV2alphaRemoveControlRequest = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudRetailV2alphaServingConfigHttpRequest: ...
                    def search(
                        self,
                        *,
                        placement: str,
                        body: GoogleCloudRetailV2alphaSearchRequest = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudRetailV2alphaSearchResponseHttpRequest: ...
                    def search_next(
                        self,
                        previous_request: GoogleCloudRetailV2alphaSearchResponseHttpRequest,
                        previous_response: GoogleCloudRetailV2alphaSearchResponse,
                    ) -> GoogleCloudRetailV2alphaSearchResponseHttpRequest | None: ...

                @typing.type_check_only
                class UserEventsResource(googleapiclient.discovery.Resource):
                    def collect(
                        self,
                        *,
                        parent: str,
                        ets: str = ...,
                        uri: str = ...,
                        userEvent: str = ...,
                        **kwargs: typing.Any
                    ) -> GoogleApiHttpBodyHttpRequest: ...
                    def import_(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudRetailV2alphaImportUserEventsRequest = ...,
                        **kwargs: typing.Any
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def purge(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudRetailV2alphaPurgeUserEventsRequest = ...,
                        **kwargs: typing.Any
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def rejoin(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudRetailV2alphaRejoinUserEventsRequest = ...,
                        **kwargs: typing.Any
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def write(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudRetailV2alphaUserEvent = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudRetailV2alphaUserEventHttpRequest: ...

                def completeQuery(
                    self,
                    *,
                    catalog: str,
                    dataset: str = ...,
                    deviceType: str = ...,
                    languageCodes: str | _list[str] = ...,
                    maxSuggestions: int = ...,
                    query: str = ...,
                    visitorId: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudRetailV2alphaCompleteQueryResponseHttpRequest: ...
                def getAttributesConfig(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudRetailV2alphaAttributesConfigHttpRequest: ...
                def getCompletionConfig(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudRetailV2alphaCompletionConfigHttpRequest: ...
                def getDefaultBranch(
                    self, *, catalog: str, **kwargs: typing.Any
                ) -> GoogleCloudRetailV2alphaGetDefaultBranchResponseHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudRetailV2alphaListCatalogsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudRetailV2alphaListCatalogsResponseHttpRequest,
                    previous_response: GoogleCloudRetailV2alphaListCatalogsResponse,
                ) -> GoogleCloudRetailV2alphaListCatalogsResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudRetailV2alphaCatalog = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudRetailV2alphaCatalogHttpRequest: ...
                def setDefaultBranch(
                    self,
                    *,
                    catalog: str,
                    body: GoogleCloudRetailV2alphaSetDefaultBranchRequest = ...,
                    **kwargs: typing.Any
                ) -> GoogleProtobufEmptyHttpRequest: ...
                def updateAttributesConfig(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudRetailV2alphaAttributesConfig = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudRetailV2alphaAttributesConfigHttpRequest: ...
                def updateCompletionConfig(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudRetailV2alphaCompletionConfig = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudRetailV2alphaCompletionConfigHttpRequest: ...
                def attributesConfig(self) -> AttributesConfigResource: ...
                def branches(self) -> BranchesResource: ...
                def completionData(self) -> CompletionDataResource: ...
                def controls(self) -> ControlsResource: ...
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
                    **kwargs: typing.Any
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
                **kwargs: typing.Any
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
        | None = ...,
    ) -> googleapiclient.http.BatchHttpRequest: ...
    def projects(self) -> ProjectsResource: ...

@typing.type_check_only
class GoogleApiHttpBodyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleApiHttpBody: ...

@typing.type_check_only
class GoogleCloudRetailV2alphaAttributesConfigHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudRetailV2alphaAttributesConfig: ...

@typing.type_check_only
class GoogleCloudRetailV2alphaBatchRemoveCatalogAttributesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudRetailV2alphaBatchRemoveCatalogAttributesResponse: ...

@typing.type_check_only
class GoogleCloudRetailV2alphaCatalogHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudRetailV2alphaCatalog: ...

@typing.type_check_only
class GoogleCloudRetailV2alphaCompleteQueryResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudRetailV2alphaCompleteQueryResponse: ...

@typing.type_check_only
class GoogleCloudRetailV2alphaCompletionConfigHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudRetailV2alphaCompletionConfig: ...

@typing.type_check_only
class GoogleCloudRetailV2alphaControlHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudRetailV2alphaControl: ...

@typing.type_check_only
class GoogleCloudRetailV2alphaGetDefaultBranchResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudRetailV2alphaGetDefaultBranchResponse: ...

@typing.type_check_only
class GoogleCloudRetailV2alphaListCatalogsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudRetailV2alphaListCatalogsResponse: ...

@typing.type_check_only
class GoogleCloudRetailV2alphaListControlsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudRetailV2alphaListControlsResponse: ...

@typing.type_check_only
class GoogleCloudRetailV2alphaListModelsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudRetailV2alphaListModelsResponse: ...

@typing.type_check_only
class GoogleCloudRetailV2alphaListProductsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudRetailV2alphaListProductsResponse: ...

@typing.type_check_only
class GoogleCloudRetailV2alphaListServingConfigsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudRetailV2alphaListServingConfigsResponse: ...

@typing.type_check_only
class GoogleCloudRetailV2alphaModelHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudRetailV2alphaModel: ...

@typing.type_check_only
class GoogleCloudRetailV2alphaPredictResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudRetailV2alphaPredictResponse: ...

@typing.type_check_only
class GoogleCloudRetailV2alphaProductHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudRetailV2alphaProduct: ...

@typing.type_check_only
class GoogleCloudRetailV2alphaSearchResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudRetailV2alphaSearchResponse: ...

@typing.type_check_only
class GoogleCloudRetailV2alphaServingConfigHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudRetailV2alphaServingConfig: ...

@typing.type_check_only
class GoogleCloudRetailV2alphaUserEventHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudRetailV2alphaUserEvent: ...

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
