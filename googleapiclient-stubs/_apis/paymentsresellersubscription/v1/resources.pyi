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
            ) -> ListProductsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListProductsResponseHttpRequest,
                previous_response: ListProductsResponse,
            ) -> ListProductsResponseHttpRequest | None: ...

        @typing.type_check_only
        class PromotionsResource(googleapiclient.discovery.Resource):
            def findEligible(
                self,
                *,
                parent: str,
                body: FindEligiblePromotionsRequest = ...,
                **kwargs: typing.Any,
            ) -> FindEligiblePromotionsResponseHttpRequest: ...
            def findEligible_next(
                self,
                previous_request: FindEligiblePromotionsResponseHttpRequest,
                previous_response: FindEligiblePromotionsResponse,
            ) -> FindEligiblePromotionsResponseHttpRequest | None: ...
            def list(
                self,
                *,
                parent: str,
                filter: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any,
            ) -> ListPromotionsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListPromotionsResponseHttpRequest,
                previous_response: ListPromotionsResponse,
            ) -> ListPromotionsResponseHttpRequest | None: ...

        @typing.type_check_only
        class SubscriptionsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class LineItemsResource(googleapiclient.discovery.Resource):
                def patch(
                    self,
                    *,
                    name: str,
                    body: SubscriptionLineItem = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> SubscriptionLineItemHttpRequest: ...

            def cancel(
                self,
                *,
                name: str,
                body: CancelSubscriptionRequest = ...,
                **kwargs: typing.Any,
            ) -> CancelSubscriptionResponseHttpRequest: ...
            def create(
                self,
                *,
                parent: str,
                body: Subscription = ...,
                subscriptionId: str = ...,
                **kwargs: typing.Any,
            ) -> SubscriptionHttpRequest: ...
            def entitle(
                self,
                *,
                name: str,
                body: EntitleSubscriptionRequest = ...,
                **kwargs: typing.Any,
            ) -> EntitleSubscriptionResponseHttpRequest: ...
            def extend(
                self,
                *,
                name: str,
                body: ExtendSubscriptionRequest = ...,
                **kwargs: typing.Any,
            ) -> ExtendSubscriptionResponseHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> SubscriptionHttpRequest: ...
            def provision(
                self,
                *,
                parent: str,
                body: Subscription = ...,
                cycleOptions_initialCycleDuration_count: int = ...,
                cycleOptions_initialCycleDuration_unit: typing_extensions.Literal[
                    "UNIT_UNSPECIFIED", "MONTH", "DAY", "HOUR"
                ] = ...,
                subscriptionId: str = ...,
                **kwargs: typing.Any,
            ) -> SubscriptionHttpRequest: ...
            def resume(
                self,
                *,
                name: str,
                body: ResumeSubscriptionRequest = ...,
                **kwargs: typing.Any,
            ) -> ResumeSubscriptionResponseHttpRequest: ...
            def suspend(
                self,
                *,
                name: str,
                body: SuspendSubscriptionRequest = ...,
                **kwargs: typing.Any,
            ) -> SuspendSubscriptionResponseHttpRequest: ...
            def undoCancel(
                self,
                *,
                name: str,
                body: UndoCancelSubscriptionRequest = ...,
                **kwargs: typing.Any,
            ) -> UndoCancelSubscriptionResponseHttpRequest: ...
            def lineItems(self) -> LineItemsResource: ...

        @typing.type_check_only
        class UserSessionsResource(googleapiclient.discovery.Resource):
            def generate(
                self,
                *,
                parent: str,
                body: GenerateUserSessionRequest = ...,
                **kwargs: typing.Any,
            ) -> GenerateUserSessionResponseHttpRequest: ...

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
class CancelSubscriptionResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> CancelSubscriptionResponse: ...

@typing.type_check_only
class EntitleSubscriptionResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> EntitleSubscriptionResponse: ...

@typing.type_check_only
class ExtendSubscriptionResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ExtendSubscriptionResponse: ...

@typing.type_check_only
class FindEligiblePromotionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> FindEligiblePromotionsResponse: ...

@typing.type_check_only
class GenerateUserSessionResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GenerateUserSessionResponse: ...

@typing.type_check_only
class ListProductsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListProductsResponse: ...

@typing.type_check_only
class ListPromotionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListPromotionsResponse: ...

@typing.type_check_only
class ResumeSubscriptionResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ResumeSubscriptionResponse: ...

@typing.type_check_only
class SubscriptionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Subscription: ...

@typing.type_check_only
class SubscriptionLineItemHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> SubscriptionLineItem: ...

@typing.type_check_only
class SuspendSubscriptionResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> SuspendSubscriptionResponse: ...

@typing.type_check_only
class UndoCancelSubscriptionResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> UndoCancelSubscriptionResponse: ...
