import collections.abc
import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

_list = list

@typing.type_check_only
class RecommendationsAIResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class ProjectsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class LocationsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class CatalogsResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class CatalogItemsResource(googleapiclient.discovery.Resource):
                    def create(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudRecommendationengineV1beta1CatalogItem = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudRecommendationengineV1beta1CatalogItemHttpRequest: ...
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleProtobufEmptyHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleCloudRecommendationengineV1beta1CatalogItemHttpRequest: ...
                    def import_(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudRecommendationengineV1beta1ImportCatalogItemsRequest = ...,
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
                    ) -> GoogleCloudRecommendationengineV1beta1ListCatalogItemsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudRecommendationengineV1beta1ListCatalogItemsResponseHttpRequest,
                        previous_response: GoogleCloudRecommendationengineV1beta1ListCatalogItemsResponse,
                    ) -> GoogleCloudRecommendationengineV1beta1ListCatalogItemsResponseHttpRequest | None: ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudRecommendationengineV1beta1CatalogItem = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudRecommendationengineV1beta1CatalogItemHttpRequest: ...

                @typing.type_check_only
                class EventStoresResource(googleapiclient.discovery.Resource):
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
                            name: str,
                            body: GoogleCloudRecommendationengineV1beta1PredictRequest = ...,
                            **kwargs: typing.Any
                        ) -> GoogleCloudRecommendationengineV1beta1PredictResponseHttpRequest: ...
                        def predict_next(
                            self,
                            previous_request: GoogleCloudRecommendationengineV1beta1PredictResponseHttpRequest,
                            previous_response: GoogleCloudRecommendationengineV1beta1PredictResponse,
                        ) -> GoogleCloudRecommendationengineV1beta1PredictResponseHttpRequest | None: ...

                    @typing.type_check_only
                    class PredictionApiKeyRegistrationsResource(
                        googleapiclient.discovery.Resource
                    ):
                        def create(
                            self,
                            *,
                            parent: str,
                            body: GoogleCloudRecommendationengineV1beta1CreatePredictionApiKeyRegistrationRequest = ...,
                            **kwargs: typing.Any
                        ) -> GoogleCloudRecommendationengineV1beta1PredictionApiKeyRegistrationHttpRequest: ...
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
                        ) -> GoogleCloudRecommendationengineV1beta1ListPredictionApiKeyRegistrationsResponseHttpRequest: ...
                        def list_next(
                            self,
                            previous_request: GoogleCloudRecommendationengineV1beta1ListPredictionApiKeyRegistrationsResponseHttpRequest,
                            previous_response: GoogleCloudRecommendationengineV1beta1ListPredictionApiKeyRegistrationsResponse,
                        ) -> GoogleCloudRecommendationengineV1beta1ListPredictionApiKeyRegistrationsResponseHttpRequest | None: ...

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
                            body: GoogleCloudRecommendationengineV1beta1ImportUserEventsRequest = ...,
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
                        ) -> GoogleCloudRecommendationengineV1beta1ListUserEventsResponseHttpRequest: ...
                        def list_next(
                            self,
                            previous_request: GoogleCloudRecommendationengineV1beta1ListUserEventsResponseHttpRequest,
                            previous_response: GoogleCloudRecommendationengineV1beta1ListUserEventsResponse,
                        ) -> GoogleCloudRecommendationengineV1beta1ListUserEventsResponseHttpRequest | None: ...
                        def purge(
                            self,
                            *,
                            parent: str,
                            body: GoogleCloudRecommendationengineV1beta1PurgeUserEventsRequest = ...,
                            **kwargs: typing.Any
                        ) -> GoogleLongrunningOperationHttpRequest: ...
                        def rejoin(
                            self,
                            *,
                            parent: str,
                            body: GoogleCloudRecommendationengineV1beta1RejoinUserEventsRequest = ...,
                            **kwargs: typing.Any
                        ) -> GoogleLongrunningOperationHttpRequest: ...
                        def write(
                            self,
                            *,
                            parent: str,
                            body: GoogleCloudRecommendationengineV1beta1UserEvent = ...,
                            **kwargs: typing.Any
                        ) -> GoogleCloudRecommendationengineV1beta1UserEventHttpRequest: ...

                    def operations(self) -> OperationsResource: ...
                    def placements(self) -> PlacementsResource: ...
                    def predictionApiKeyRegistrations(
                        self,
                    ) -> PredictionApiKeyRegistrationsResource: ...
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

                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudRecommendationengineV1beta1ListCatalogsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudRecommendationengineV1beta1ListCatalogsResponseHttpRequest,
                    previous_response: GoogleCloudRecommendationengineV1beta1ListCatalogsResponse,
                ) -> GoogleCloudRecommendationengineV1beta1ListCatalogsResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudRecommendationengineV1beta1Catalog = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudRecommendationengineV1beta1CatalogHttpRequest: ...
                def catalogItems(self) -> CatalogItemsResource: ...
                def eventStores(self) -> EventStoresResource: ...
                def operations(self) -> OperationsResource: ...

            def catalogs(self) -> CatalogsResource: ...

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
class GoogleCloudRecommendationengineV1beta1CatalogHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudRecommendationengineV1beta1Catalog: ...

@typing.type_check_only
class GoogleCloudRecommendationengineV1beta1CatalogItemHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudRecommendationengineV1beta1CatalogItem: ...

@typing.type_check_only
class GoogleCloudRecommendationengineV1beta1ListCatalogItemsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudRecommendationengineV1beta1ListCatalogItemsResponse: ...

@typing.type_check_only
class GoogleCloudRecommendationengineV1beta1ListCatalogsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudRecommendationengineV1beta1ListCatalogsResponse: ...

@typing.type_check_only
class GoogleCloudRecommendationengineV1beta1ListPredictionApiKeyRegistrationsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudRecommendationengineV1beta1ListPredictionApiKeyRegistrationsResponse: ...

@typing.type_check_only
class GoogleCloudRecommendationengineV1beta1ListUserEventsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudRecommendationengineV1beta1ListUserEventsResponse: ...

@typing.type_check_only
class GoogleCloudRecommendationengineV1beta1PredictResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudRecommendationengineV1beta1PredictResponse: ...

@typing.type_check_only
class GoogleCloudRecommendationengineV1beta1PredictionApiKeyRegistrationHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudRecommendationengineV1beta1PredictionApiKeyRegistration: ...

@typing.type_check_only
class GoogleCloudRecommendationengineV1beta1UserEventHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudRecommendationengineV1beta1UserEvent: ...

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
