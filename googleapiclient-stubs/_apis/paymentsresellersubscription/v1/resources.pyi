import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

@typing.type_check_only
class PaymentsResellerSubscriptionResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class PartnersResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class ProductsResource(googleapiclient.discovery.Resource):
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudPaymentsResellerSubscriptionV1ListProductsResponseHttpRequest: ...
        @typing.type_check_only
        class PromotionsResource(googleapiclient.discovery.Resource):
            def list(
                self,
                *,
                parent: str,
                filter: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudPaymentsResellerSubscriptionV1ListPromotionsResponseHttpRequest: ...
        @typing.type_check_only
        class SubscriptionsResource(googleapiclient.discovery.Resource):
            def cancel(
                self,
                *,
                name: str,
                body: GoogleCloudPaymentsResellerSubscriptionV1CancelSubscriptionRequest = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudPaymentsResellerSubscriptionV1CancelSubscriptionResponseHttpRequest: ...
            def create(
                self,
                *,
                parent: str,
                body: GoogleCloudPaymentsResellerSubscriptionV1Subscription = ...,
                subscriptionId: str = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudPaymentsResellerSubscriptionV1SubscriptionHttpRequest: ...
            def entitle(
                self,
                *,
                name: str,
                body: GoogleCloudPaymentsResellerSubscriptionV1EntitleSubscriptionRequest = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudPaymentsResellerSubscriptionV1EntitleSubscriptionResponseHttpRequest: ...
            def extend(
                self,
                *,
                name: str,
                body: GoogleCloudPaymentsResellerSubscriptionV1ExtendSubscriptionRequest = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudPaymentsResellerSubscriptionV1ExtendSubscriptionResponseHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleCloudPaymentsResellerSubscriptionV1SubscriptionHttpRequest: ...
            def provision(
                self,
                *,
                parent: str,
                body: GoogleCloudPaymentsResellerSubscriptionV1Subscription = ...,
                subscriptionId: str = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudPaymentsResellerSubscriptionV1SubscriptionHttpRequest: ...
            def undoCancel(
                self,
                *,
                name: str,
                body: GoogleCloudPaymentsResellerSubscriptionV1UndoCancelSubscriptionRequest = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudPaymentsResellerSubscriptionV1UndoCancelSubscriptionResponseHttpRequest: ...
        def products(self) -> ProductsResource: ...
        def promotions(self) -> PromotionsResource: ...
        def subscriptions(self) -> SubscriptionsResource: ...
    def partners(self) -> PartnersResource: ...

@typing.type_check_only
class GoogleCloudPaymentsResellerSubscriptionV1CancelSubscriptionResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleCloudPaymentsResellerSubscriptionV1CancelSubscriptionResponse: ...

@typing.type_check_only
class GoogleCloudPaymentsResellerSubscriptionV1EntitleSubscriptionResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleCloudPaymentsResellerSubscriptionV1EntitleSubscriptionResponse: ...

@typing.type_check_only
class GoogleCloudPaymentsResellerSubscriptionV1ExtendSubscriptionResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleCloudPaymentsResellerSubscriptionV1ExtendSubscriptionResponse: ...

@typing.type_check_only
class GoogleCloudPaymentsResellerSubscriptionV1ListProductsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleCloudPaymentsResellerSubscriptionV1ListProductsResponse: ...

@typing.type_check_only
class GoogleCloudPaymentsResellerSubscriptionV1ListPromotionsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleCloudPaymentsResellerSubscriptionV1ListPromotionsResponse: ...

@typing.type_check_only
class GoogleCloudPaymentsResellerSubscriptionV1SubscriptionHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleCloudPaymentsResellerSubscriptionV1Subscription: ...

@typing.type_check_only
class GoogleCloudPaymentsResellerSubscriptionV1UndoCancelSubscriptionResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleCloudPaymentsResellerSubscriptionV1UndoCancelSubscriptionResponse: ...
