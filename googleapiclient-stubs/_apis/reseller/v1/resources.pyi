import collections.abc
import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

_list = list

@typing.type_check_only
class ResellerResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class CustomersResource(googleapiclient.discovery.Resource):
        def get(
            self, *, customerId: str, **kwargs: typing.Any
        ) -> CustomerHttpRequest: ...
        def insert(
            self,
            *,
            body: Customer = ...,
            customerAuthToken: str = ...,
            **kwargs: typing.Any
        ) -> CustomerHttpRequest: ...
        def patch(
            self, *, customerId: str, body: Customer = ..., **kwargs: typing.Any
        ) -> CustomerHttpRequest: ...
        def update(
            self, *, customerId: str, body: Customer = ..., **kwargs: typing.Any
        ) -> CustomerHttpRequest: ...

    @typing.type_check_only
    class ResellernotifyResource(googleapiclient.discovery.Resource):
        def getwatchdetails(
            self, **kwargs: typing.Any
        ) -> ResellernotifyGetwatchdetailsResponseHttpRequest: ...
        def register(
            self, *, serviceAccountEmailAddress: str = ..., **kwargs: typing.Any
        ) -> ResellernotifyResourceHttpRequest: ...
        def unregister(
            self, *, serviceAccountEmailAddress: str = ..., **kwargs: typing.Any
        ) -> ResellernotifyResourceHttpRequest: ...

    @typing.type_check_only
    class SubscriptionsResource(googleapiclient.discovery.Resource):
        def activate(
            self, *, customerId: str, subscriptionId: str, **kwargs: typing.Any
        ) -> SubscriptionHttpRequest: ...
        def changePlan(
            self,
            *,
            customerId: str,
            subscriptionId: str,
            body: ChangePlanRequest = ...,
            **kwargs: typing.Any
        ) -> SubscriptionHttpRequest: ...
        def changeRenewalSettings(
            self,
            *,
            customerId: str,
            subscriptionId: str,
            body: RenewalSettings = ...,
            **kwargs: typing.Any
        ) -> SubscriptionHttpRequest: ...
        def changeSeats(
            self,
            *,
            customerId: str,
            subscriptionId: str,
            body: Seats = ...,
            **kwargs: typing.Any
        ) -> SubscriptionHttpRequest: ...
        def delete(
            self,
            *,
            customerId: str,
            subscriptionId: str,
            deletionType: typing_extensions.Literal[
                "deletion_type_undefined", "cancel", "transfer_to_direct"
            ],
            **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def get(
            self, *, customerId: str, subscriptionId: str, **kwargs: typing.Any
        ) -> SubscriptionHttpRequest: ...
        def insert(
            self,
            *,
            customerId: str,
            body: Subscription = ...,
            customerAuthToken: str = ...,
            **kwargs: typing.Any
        ) -> SubscriptionHttpRequest: ...
        def list(
            self,
            *,
            customerAuthToken: str = ...,
            customerId: str = ...,
            customerNamePrefix: str = ...,
            maxResults: int = ...,
            pageToken: str = ...,
            **kwargs: typing.Any
        ) -> SubscriptionsHttpRequest: ...
        def list_next(
            self,
            previous_request: SubscriptionsHttpRequest,
            previous_response: Subscriptions,
        ) -> SubscriptionsHttpRequest | None: ...
        def startPaidService(
            self, *, customerId: str, subscriptionId: str, **kwargs: typing.Any
        ) -> SubscriptionHttpRequest: ...
        def suspend(
            self, *, customerId: str, subscriptionId: str, **kwargs: typing.Any
        ) -> SubscriptionHttpRequest: ...

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
    def customers(self) -> CustomersResource: ...
    def resellernotify(self) -> ResellernotifyResource: ...
    def subscriptions(self) -> SubscriptionsResource: ...

@typing.type_check_only
class CustomerHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Customer: ...

@typing.type_check_only
class ResellernotifyGetwatchdetailsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ResellernotifyGetwatchdetailsResponse: ...

@typing.type_check_only
class ResellernotifyResourceHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ResellernotifyResource: ...

@typing.type_check_only
class SubscriptionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Subscription: ...

@typing.type_check_only
class SubscriptionsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Subscriptions: ...
