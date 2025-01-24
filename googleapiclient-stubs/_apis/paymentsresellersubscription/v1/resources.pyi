import collections.abc
import typing

import httplib2
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http

from .schemas import *

_list = list

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
                filter: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any,
            ) -> (
                GoogleCloudPaymentsResellerSubscriptionV1ListProductsResponseHttpRequest
            ): ...
            def list_next(
                self,
                previous_request: GoogleCloudPaymentsResellerSubscriptionV1ListProductsResponseHttpRequest,
                previous_response: GoogleCloudPaymentsResellerSubscriptionV1ListProductsResponse,
            ) -> (
                GoogleCloudPaymentsResellerSubscriptionV1ListProductsResponseHttpRequest
                | None
            ): ...

        @typing.type_check_only
        class PromotionsResource(googleapiclient.discovery.Resource):
            def findEligible(
                self,
                *,
                parent: str,
                body: GoogleCloudPaymentsResellerSubscriptionV1FindEligiblePromotionsRequest = ...,
                **kwargs: typing.Any,
            ) -> GoogleCloudPaymentsResellerSubscriptionV1FindEligiblePromotionsResponseHttpRequest: ...
            def findEligible_next(
                self,
                previous_request: GoogleCloudPaymentsResellerSubscriptionV1FindEligiblePromotionsResponseHttpRequest,
                previous_response: GoogleCloudPaymentsResellerSubscriptionV1FindEligiblePromotionsResponse,
            ) -> (
                GoogleCloudPaymentsResellerSubscriptionV1FindEligiblePromotionsResponseHttpRequest
                | None
            ): ...
            def list(
                self,
                *,
                parent: str,
                filter: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any,
            ) -> GoogleCloudPaymentsResellerSubscriptionV1ListPromotionsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: GoogleCloudPaymentsResellerSubscriptionV1ListPromotionsResponseHttpRequest,
                previous_response: GoogleCloudPaymentsResellerSubscriptionV1ListPromotionsResponse,
            ) -> (
                GoogleCloudPaymentsResellerSubscriptionV1ListPromotionsResponseHttpRequest
                | None
            ): ...

        @typing.type_check_only
        class SubscriptionsResource(googleapiclient.discovery.Resource):
            def cancel(
                self,
                *,
                name: str,
                body: GoogleCloudPaymentsResellerSubscriptionV1CancelSubscriptionRequest = ...,
                **kwargs: typing.Any,
            ) -> GoogleCloudPaymentsResellerSubscriptionV1CancelSubscriptionResponseHttpRequest: ...
            def create(
                self,
                *,
                parent: str,
                body: GoogleCloudPaymentsResellerSubscriptionV1Subscription = ...,
                subscriptionId: str = ...,
                **kwargs: typing.Any,
            ) -> GoogleCloudPaymentsResellerSubscriptionV1SubscriptionHttpRequest: ...
            def entitle(
                self,
                *,
                name: str,
                body: GoogleCloudPaymentsResellerSubscriptionV1EntitleSubscriptionRequest = ...,
                **kwargs: typing.Any,
            ) -> GoogleCloudPaymentsResellerSubscriptionV1EntitleSubscriptionResponseHttpRequest: ...
            def extend(
                self,
                *,
                name: str,
                body: GoogleCloudPaymentsResellerSubscriptionV1ExtendSubscriptionRequest = ...,
                **kwargs: typing.Any,
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
                **kwargs: typing.Any,
            ) -> GoogleCloudPaymentsResellerSubscriptionV1SubscriptionHttpRequest: ...
            def undoCancel(
                self,
                *,
                name: str,
                body: GoogleCloudPaymentsResellerSubscriptionV1UndoCancelSubscriptionRequest = ...,
                **kwargs: typing.Any,
            ) -> GoogleCloudPaymentsResellerSubscriptionV1UndoCancelSubscriptionResponseHttpRequest: ...

        @typing.type_check_only
        class UserSessionsResource(googleapiclient.discovery.Resource):
            def generate(
                self,
                *,
                parent: str,
                body: GoogleCloudPaymentsResellerSubscriptionV1GenerateUserSessionRequest = ...,
                **kwargs: typing.Any,
            ) -> GoogleCloudPaymentsResellerSubscriptionV1GenerateUserSessionResponseHttpRequest: ...

        def products(self) -> ProductsResource: ...
        def promotions(self) -> PromotionsResource: ...
        def subscriptions(self) -> SubscriptionsResource: ...
        def userSessions(self) -> UserSessionsResource: ...

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
    def partners(self) -> PartnersResource: ...

@typing.type_check_only
class GoogleCloudPaymentsResellerSubscriptionV1CancelSubscriptionResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudPaymentsResellerSubscriptionV1CancelSubscriptionResponse: ...

@typing.type_check_only
class GoogleCloudPaymentsResellerSubscriptionV1EntitleSubscriptionResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudPaymentsResellerSubscriptionV1EntitleSubscriptionResponse: ...

@typing.type_check_only
class GoogleCloudPaymentsResellerSubscriptionV1ExtendSubscriptionResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudPaymentsResellerSubscriptionV1ExtendSubscriptionResponse: ...

@typing.type_check_only
class GoogleCloudPaymentsResellerSubscriptionV1FindEligiblePromotionsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudPaymentsResellerSubscriptionV1FindEligiblePromotionsResponse: ...

@typing.type_check_only
class GoogleCloudPaymentsResellerSubscriptionV1GenerateUserSessionResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudPaymentsResellerSubscriptionV1GenerateUserSessionResponse: ...

@typing.type_check_only
class GoogleCloudPaymentsResellerSubscriptionV1ListProductsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudPaymentsResellerSubscriptionV1ListProductsResponse: ...

@typing.type_check_only
class GoogleCloudPaymentsResellerSubscriptionV1ListPromotionsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudPaymentsResellerSubscriptionV1ListPromotionsResponse: ...

@typing.type_check_only
class GoogleCloudPaymentsResellerSubscriptionV1SubscriptionHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudPaymentsResellerSubscriptionV1Subscription: ...

@typing.type_check_only
class GoogleCloudPaymentsResellerSubscriptionV1UndoCancelSubscriptionResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudPaymentsResellerSubscriptionV1UndoCancelSubscriptionResponse: ...
