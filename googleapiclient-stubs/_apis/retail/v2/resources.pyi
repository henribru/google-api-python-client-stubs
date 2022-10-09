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
                        body: GoogleCloudRetailV2AddCatalogAttributeRequest = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudRetailV2AttributesConfigHttpRequest: ...
                    def removeCatalogAttribute(
                        self,
                        *,
                        attributesConfig: str,
                        body: GoogleCloudRetailV2RemoveCatalogAttributeRequest = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudRetailV2AttributesConfigHttpRequest: ...
                    def replaceCatalogAttribute(
                        self,
                        *,
                        attributesConfig: str,
                        body: GoogleCloudRetailV2ReplaceCatalogAttributeRequest = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudRetailV2AttributesConfigHttpRequest: ...

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
                            body: GoogleCloudRetailV2AddFulfillmentPlacesRequest = ...,
                            **kwargs: typing.Any
                        ) -> GoogleLongrunningOperationHttpRequest: ...
                        def addLocalInventories(
                            self,
                            *,
                            product: str,
                            body: GoogleCloudRetailV2AddLocalInventoriesRequest = ...,
                            **kwargs: typing.Any
                        ) -> GoogleLongrunningOperationHttpRequest: ...
                        def create(
                            self,
                            *,
                            parent: str,
                            body: GoogleCloudRetailV2Product = ...,
                            productId: str = ...,
                            **kwargs: typing.Any
                        ) -> GoogleCloudRetailV2ProductHttpRequest: ...
                        def delete(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> GoogleProtobufEmptyHttpRequest: ...
                        def get(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> GoogleCloudRetailV2ProductHttpRequest: ...
                        def import_(
                            self,
                            *,
                            parent: str,
                            body: GoogleCloudRetailV2ImportProductsRequest = ...,
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
                            **kwargs: typing.Any
                        ) -> GoogleCloudRetailV2ListProductsResponseHttpRequest: ...
                        def list_next(
                            self,
                            previous_request: GoogleCloudRetailV2ListProductsResponseHttpRequest,
                            previous_response: GoogleCloudRetailV2ListProductsResponse,
                        ) -> GoogleCloudRetailV2ListProductsResponseHttpRequest | None: ...
                        def patch(
                            self,
                            *,
                            name: str,
                            body: GoogleCloudRetailV2Product = ...,
                            allowMissing: bool = ...,
                            updateMask: str = ...,
                            **kwargs: typing.Any
                        ) -> GoogleCloudRetailV2ProductHttpRequest: ...
                        def removeFulfillmentPlaces(
                            self,
                            *,
                            product: str,
                            body: GoogleCloudRetailV2RemoveFulfillmentPlacesRequest = ...,
                            **kwargs: typing.Any
                        ) -> GoogleLongrunningOperationHttpRequest: ...
                        def removeLocalInventories(
                            self,
                            *,
                            product: str,
                            body: GoogleCloudRetailV2RemoveLocalInventoriesRequest = ...,
                            **kwargs: typing.Any
                        ) -> GoogleLongrunningOperationHttpRequest: ...
                        def setInventory(
                            self,
                            *,
                            name: str,
                            body: GoogleCloudRetailV2SetInventoryRequest = ...,
                            **kwargs: typing.Any
                        ) -> GoogleLongrunningOperationHttpRequest: ...

                    def operations(self) -> OperationsResource: ...
                    def products(self) -> ProductsResource: ...

                @typing.type_check_only
                class CompletionDataResource(googleapiclient.discovery.Resource):
                    def import_(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudRetailV2ImportCompletionDataRequest = ...,
                        **kwargs: typing.Any
                    ) -> GoogleLongrunningOperationHttpRequest: ...

                @typing.type_check_only
                class ControlsResource(googleapiclient.discovery.Resource):
                    def create(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudRetailV2Control = ...,
                        controlId: str = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudRetailV2ControlHttpRequest: ...
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleProtobufEmptyHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleCloudRetailV2ControlHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudRetailV2ListControlsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudRetailV2ListControlsResponseHttpRequest,
                        previous_response: GoogleCloudRetailV2ListControlsResponse,
                    ) -> GoogleCloudRetailV2ListControlsResponseHttpRequest | None: ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudRetailV2Control = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudRetailV2ControlHttpRequest: ...

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
                        body: GoogleCloudRetailV2PredictRequest = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudRetailV2PredictResponseHttpRequest: ...
                    def search(
                        self,
                        *,
                        placement: str,
                        body: GoogleCloudRetailV2SearchRequest = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudRetailV2SearchResponseHttpRequest: ...
                    def search_next(
                        self,
                        previous_request: GoogleCloudRetailV2SearchResponseHttpRequest,
                        previous_response: GoogleCloudRetailV2SearchResponse,
                    ) -> GoogleCloudRetailV2SearchResponseHttpRequest | None: ...

                @typing.type_check_only
                class ServingConfigsResource(googleapiclient.discovery.Resource):
                    def addControl(
                        self,
                        *,
                        servingConfig: str,
                        body: GoogleCloudRetailV2AddControlRequest = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudRetailV2ServingConfigHttpRequest: ...
                    def create(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudRetailV2ServingConfig = ...,
                        servingConfigId: str = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudRetailV2ServingConfigHttpRequest: ...
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleProtobufEmptyHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleCloudRetailV2ServingConfigHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudRetailV2ListServingConfigsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudRetailV2ListServingConfigsResponseHttpRequest,
                        previous_response: GoogleCloudRetailV2ListServingConfigsResponse,
                    ) -> GoogleCloudRetailV2ListServingConfigsResponseHttpRequest | None: ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudRetailV2ServingConfig = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudRetailV2ServingConfigHttpRequest: ...
                    def predict(
                        self,
                        *,
                        placement: str,
                        body: GoogleCloudRetailV2PredictRequest = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudRetailV2PredictResponseHttpRequest: ...
                    def removeControl(
                        self,
                        *,
                        servingConfig: str,
                        body: GoogleCloudRetailV2RemoveControlRequest = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudRetailV2ServingConfigHttpRequest: ...
                    def search(
                        self,
                        *,
                        placement: str,
                        body: GoogleCloudRetailV2SearchRequest = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudRetailV2SearchResponseHttpRequest: ...
                    def search_next(
                        self,
                        previous_request: GoogleCloudRetailV2SearchResponseHttpRequest,
                        previous_response: GoogleCloudRetailV2SearchResponse,
                    ) -> GoogleCloudRetailV2SearchResponseHttpRequest | None: ...

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
                        body: GoogleCloudRetailV2ImportUserEventsRequest = ...,
                        **kwargs: typing.Any
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def purge(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudRetailV2PurgeUserEventsRequest = ...,
                        **kwargs: typing.Any
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def rejoin(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudRetailV2RejoinUserEventsRequest = ...,
                        **kwargs: typing.Any
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def write(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudRetailV2UserEvent = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudRetailV2UserEventHttpRequest: ...

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
                ) -> GoogleCloudRetailV2CompleteQueryResponseHttpRequest: ...
                def getAttributesConfig(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudRetailV2AttributesConfigHttpRequest: ...
                def getCompletionConfig(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudRetailV2CompletionConfigHttpRequest: ...
                def getDefaultBranch(
                    self, *, catalog: str, **kwargs: typing.Any
                ) -> GoogleCloudRetailV2GetDefaultBranchResponseHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudRetailV2ListCatalogsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudRetailV2ListCatalogsResponseHttpRequest,
                    previous_response: GoogleCloudRetailV2ListCatalogsResponse,
                ) -> GoogleCloudRetailV2ListCatalogsResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudRetailV2Catalog = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudRetailV2CatalogHttpRequest: ...
                def setDefaultBranch(
                    self,
                    *,
                    catalog: str,
                    body: GoogleCloudRetailV2SetDefaultBranchRequest = ...,
                    **kwargs: typing.Any
                ) -> GoogleProtobufEmptyHttpRequest: ...
                def updateAttributesConfig(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudRetailV2AttributesConfig = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudRetailV2AttributesConfigHttpRequest: ...
                def updateCompletionConfig(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudRetailV2CompletionConfig = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudRetailV2CompletionConfigHttpRequest: ...
                def attributesConfig(self) -> AttributesConfigResource: ...
                def branches(self) -> BranchesResource: ...
                def completionData(self) -> CompletionDataResource: ...
                def controls(self) -> ControlsResource: ...
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
class GoogleCloudRetailV2AttributesConfigHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudRetailV2AttributesConfig: ...

@typing.type_check_only
class GoogleCloudRetailV2CatalogHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudRetailV2Catalog: ...

@typing.type_check_only
class GoogleCloudRetailV2CompleteQueryResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudRetailV2CompleteQueryResponse: ...

@typing.type_check_only
class GoogleCloudRetailV2CompletionConfigHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudRetailV2CompletionConfig: ...

@typing.type_check_only
class GoogleCloudRetailV2ControlHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudRetailV2Control: ...

@typing.type_check_only
class GoogleCloudRetailV2GetDefaultBranchResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudRetailV2GetDefaultBranchResponse: ...

@typing.type_check_only
class GoogleCloudRetailV2ListCatalogsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudRetailV2ListCatalogsResponse: ...

@typing.type_check_only
class GoogleCloudRetailV2ListControlsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudRetailV2ListControlsResponse: ...

@typing.type_check_only
class GoogleCloudRetailV2ListProductsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudRetailV2ListProductsResponse: ...

@typing.type_check_only
class GoogleCloudRetailV2ListServingConfigsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudRetailV2ListServingConfigsResponse: ...

@typing.type_check_only
class GoogleCloudRetailV2PredictResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudRetailV2PredictResponse: ...

@typing.type_check_only
class GoogleCloudRetailV2ProductHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudRetailV2Product: ...

@typing.type_check_only
class GoogleCloudRetailV2SearchResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudRetailV2SearchResponse: ...

@typing.type_check_only
class GoogleCloudRetailV2ServingConfigHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudRetailV2ServingConfig: ...

@typing.type_check_only
class GoogleCloudRetailV2UserEventHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudRetailV2UserEvent: ...

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
