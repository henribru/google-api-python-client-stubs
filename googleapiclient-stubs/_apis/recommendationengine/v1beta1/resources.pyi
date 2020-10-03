import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class RecommendationsAIResource(googleapiclient.discovery.Resource):
    class ProjectsResource(googleapiclient.discovery.Resource):
        class LocationsResource(googleapiclient.discovery.Resource):
            class CatalogsResource(googleapiclient.discovery.Resource):
                class CatalogItemsResource(googleapiclient.discovery.Resource):
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleProtobufEmptyHttpRequest: ...
                    def import_(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudRecommendationengineV1beta1ImportCatalogItemsRequest = ...,
                        **kwargs: typing.Any
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleCloudRecommendationengineV1beta1CatalogItemHttpRequest: ...
                    def create(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudRecommendationengineV1beta1CatalogItem = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudRecommendationengineV1beta1CatalogItemHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        filter: str = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudRecommendationengineV1beta1ListCatalogItemsResponseHttpRequest: ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudRecommendationengineV1beta1CatalogItem = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudRecommendationengineV1beta1CatalogItemHttpRequest: ...
                class EventStoresResource(googleapiclient.discovery.Resource):
                    class PredictionApiKeyRegistrationsResource(
                        googleapiclient.discovery.Resource
                    ):
                        def delete(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> GoogleProtobufEmptyHttpRequest: ...
                        def list(
                            self,
                            *,
                            parent: str,
                            pageToken: str = ...,
                            pageSize: int = ...,
                            **kwargs: typing.Any
                        ) -> GoogleCloudRecommendationengineV1beta1ListPredictionApiKeyRegistrationsResponseHttpRequest: ...
                        def create(
                            self,
                            *,
                            parent: str,
                            body: GoogleCloudRecommendationengineV1beta1CreatePredictionApiKeyRegistrationRequest = ...,
                            **kwargs: typing.Any
                        ) -> GoogleCloudRecommendationengineV1beta1PredictionApiKeyRegistrationHttpRequest: ...
                    class UserEventsResource(googleapiclient.discovery.Resource):
                        def collect(
                            self,
                            *,
                            parent: str,
                            uri: str = ...,
                            ets: str = ...,
                            userEvent: str = ...,
                            **kwargs: typing.Any
                        ) -> GoogleApiHttpBodyHttpRequest: ...
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
                        def purge(
                            self,
                            *,
                            parent: str,
                            body: GoogleCloudRecommendationengineV1beta1PurgeUserEventsRequest = ...,
                            **kwargs: typing.Any
                        ) -> GoogleLongrunningOperationHttpRequest: ...
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
                            pageToken: str = ...,
                            pageSize: int = ...,
                            filter: str = ...,
                            **kwargs: typing.Any
                        ) -> GoogleCloudRecommendationengineV1beta1ListUserEventsResponseHttpRequest: ...
                    class OperationsResource(googleapiclient.discovery.Resource):
                        def list(
                            self,
                            *,
                            name: str,
                            pageToken: str = ...,
                            filter: str = ...,
                            pageSize: int = ...,
                            **kwargs: typing.Any
                        ) -> GoogleLongrunningListOperationsResponseHttpRequest: ...
                        def get(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> GoogleLongrunningOperationHttpRequest: ...
                    class PlacementsResource(googleapiclient.discovery.Resource):
                        def predict(
                            self,
                            *,
                            name: str,
                            body: GoogleCloudRecommendationengineV1beta1PredictRequest = ...,
                            **kwargs: typing.Any
                        ) -> GoogleCloudRecommendationengineV1beta1PredictResponseHttpRequest: ...
                    def predictionApiKeyRegistrations(
                        self,
                    ) -> PredictionApiKeyRegistrationsResource: ...
                    def userEvents(self) -> UserEventsResource: ...
                    def operations(self) -> OperationsResource: ...
                    def placements(self) -> PlacementsResource: ...
                class OperationsResource(googleapiclient.discovery.Resource):
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def list(
                        self,
                        *,
                        name: str,
                        pageToken: str = ...,
                        pageSize: int = ...,
                        filter: str = ...,
                        **kwargs: typing.Any
                    ) -> GoogleLongrunningListOperationsResponseHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudRecommendationengineV1beta1ListCatalogsResponseHttpRequest: ...
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
    def projects(self) -> ProjectsResource: ...

class GoogleCloudRecommendationengineV1beta1ListCatalogsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudRecommendationengineV1beta1ListCatalogsResponse: ...

class GoogleCloudRecommendationengineV1beta1ListUserEventsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudRecommendationengineV1beta1ListUserEventsResponse: ...

class GoogleCloudRecommendationengineV1beta1ListPredictionApiKeyRegistrationsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudRecommendationengineV1beta1ListPredictionApiKeyRegistrationsResponse: ...

class GoogleCloudRecommendationengineV1beta1PredictionApiKeyRegistrationHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudRecommendationengineV1beta1PredictionApiKeyRegistration: ...

class GoogleCloudRecommendationengineV1beta1ListCatalogItemsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudRecommendationengineV1beta1ListCatalogItemsResponse: ...

class GoogleCloudRecommendationengineV1beta1CatalogItemHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudRecommendationengineV1beta1CatalogItem: ...

class GoogleProtobufEmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleProtobufEmpty: ...

class GoogleCloudRecommendationengineV1beta1PredictResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudRecommendationengineV1beta1PredictResponse: ...

class GoogleCloudRecommendationengineV1beta1CatalogHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudRecommendationengineV1beta1Catalog: ...

class GoogleApiHttpBodyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleApiHttpBody: ...

class GoogleLongrunningListOperationsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleLongrunningListOperationsResponse: ...

class GoogleCloudRecommendationengineV1beta1UserEventHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudRecommendationengineV1beta1UserEvent: ...

class GoogleLongrunningOperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleLongrunningOperation: ...
