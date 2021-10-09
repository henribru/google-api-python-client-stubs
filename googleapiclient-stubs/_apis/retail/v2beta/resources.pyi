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
                            **kwargs: typing.Any
                        ) -> GoogleLongrunningOperationHttpRequest: ...
                        def create(
                            self,
                            *,
                            parent: str,
                            body: GoogleCloudRetailV2betaProduct = ...,
                            productId: str = ...,
                            **kwargs: typing.Any
                        ) -> GoogleCloudRetailV2betaProductHttpRequest: ...
                        def delete(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> GoogleProtobufEmptyHttpRequest: ...
                        def get(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> GoogleCloudRetailV2betaProductHttpRequest: ...
                        def import_(
                            self,
                            *,
                            parent: str,
                            body: GoogleCloudRetailV2betaImportProductsRequest = ...,
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
                        ) -> GoogleCloudRetailV2betaListProductsResponseHttpRequest: ...
                        def list_next(
                            self,
                            previous_request: GoogleCloudRetailV2betaListProductsResponseHttpRequest,
                            previous_response: GoogleCloudRetailV2betaListProductsResponse,
                        ) -> GoogleCloudRetailV2betaListProductsResponseHttpRequest | None: ...
                        def patch(
                            self,
                            *,
                            name: str,
                            body: GoogleCloudRetailV2betaProduct = ...,
                            allowMissing: bool = ...,
                            updateMask: str = ...,
                            **kwargs: typing.Any
                        ) -> GoogleCloudRetailV2betaProductHttpRequest: ...
                        def removeFulfillmentPlaces(
                            self,
                            *,
                            product: str,
                            body: GoogleCloudRetailV2betaRemoveFulfillmentPlacesRequest = ...,
                            **kwargs: typing.Any
                        ) -> GoogleLongrunningOperationHttpRequest: ...
                        def setInventory(
                            self,
                            *,
                            name: str,
                            body: GoogleCloudRetailV2betaSetInventoryRequest = ...,
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
                        body: GoogleCloudRetailV2betaImportCompletionDataRequest = ...,
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
                        body: GoogleCloudRetailV2betaPredictRequest = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudRetailV2betaPredictResponseHttpRequest: ...
                    def search(
                        self,
                        *,
                        placement: str,
                        body: GoogleCloudRetailV2betaSearchRequest = ...,
                        **kwargs: typing.Any
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
                        ets: str = ...,
                        uri: str = ...,
                        userEvent: str = ...,
                        **kwargs: typing.Any
                    ) -> GoogleApiHttpBodyHttpRequest: ...
                    def import_(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudRetailV2betaImportUserEventsRequest = ...,
                        **kwargs: typing.Any
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def purge(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudRetailV2betaPurgeUserEventsRequest = ...,
                        **kwargs: typing.Any
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def rejoin(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudRetailV2betaRejoinUserEventsRequest = ...,
                        **kwargs: typing.Any
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def write(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudRetailV2betaUserEvent = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudRetailV2betaUserEventHttpRequest: ...
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
                ) -> GoogleCloudRetailV2betaCompleteQueryResponseHttpRequest: ...
                def getDefaultBranch(
                    self, *, catalog: str, **kwargs: typing.Any
                ) -> GoogleCloudRetailV2betaGetDefaultBranchResponseHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
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
                    **kwargs: typing.Any
                ) -> GoogleCloudRetailV2betaCatalogHttpRequest: ...
                def setDefaultBranch(
                    self,
                    *,
                    catalog: str,
                    body: GoogleCloudRetailV2betaSetDefaultBranchRequest = ...,
                    **kwargs: typing.Any
                ) -> GoogleProtobufEmptyHttpRequest: ...
                def branches(self) -> BranchesResource: ...
                def completionData(self) -> CompletionDataResource: ...
                def operations(self) -> OperationsResource: ...
                def placements(self) -> PlacementsResource: ...
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
        def locations(self) -> LocationsResource: ...
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
class GoogleCloudRetailV2betaCatalogHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudRetailV2betaCatalog: ...

@typing.type_check_only
class GoogleCloudRetailV2betaCompleteQueryResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudRetailV2betaCompleteQueryResponse: ...

@typing.type_check_only
class GoogleCloudRetailV2betaGetDefaultBranchResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudRetailV2betaGetDefaultBranchResponse: ...

@typing.type_check_only
class GoogleCloudRetailV2betaListCatalogsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudRetailV2betaListCatalogsResponse: ...

@typing.type_check_only
class GoogleCloudRetailV2betaListProductsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudRetailV2betaListProductsResponse: ...

@typing.type_check_only
class GoogleCloudRetailV2betaPredictResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudRetailV2betaPredictResponse: ...

@typing.type_check_only
class GoogleCloudRetailV2betaProductHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudRetailV2betaProduct: ...

@typing.type_check_only
class GoogleCloudRetailV2betaSearchResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudRetailV2betaSearchResponse: ...

@typing.type_check_only
class GoogleCloudRetailV2betaUserEventHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudRetailV2betaUserEvent: ...

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
