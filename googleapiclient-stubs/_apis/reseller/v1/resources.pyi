import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class ResellerResource(googleapiclient.discovery.Resource):
    class CustomersResource(googleapiclient.discovery.Resource):
        def get(
            self, *, customerId: str, **kwargs: typing.Any
        ) -> CustomerHttpRequest: ...
        def update(
            self, *, customerId: str, body: Customer = ..., **kwargs: typing.Any
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
    class SubscriptionsResource(googleapiclient.discovery.Resource):
        def startPaidService(
            self, *, customerId: str, subscriptionId: str, **kwargs: typing.Any
        ) -> SubscriptionHttpRequest: ...
        def changeRenewalSettings(
            self,
            *,
            customerId: str,
            subscriptionId: str,
            body: RenewalSettings = ...,
            **kwargs: typing.Any
        ) -> SubscriptionHttpRequest: ...
        def changePlan(
            self,
            *,
            customerId: str,
            subscriptionId: str,
            body: ChangePlanRequest = ...,
            **kwargs: typing.Any
        ) -> SubscriptionHttpRequest: ...
        def insert(
            self,
            *,
            customerId: str,
            body: Subscription = ...,
            customerAuthToken: str = ...,
            **kwargs: typing.Any
        ) -> SubscriptionHttpRequest: ...
        def get(
            self, *, customerId: str, subscriptionId: str, **kwargs: typing.Any
        ) -> SubscriptionHttpRequest: ...
        def changeSeats(
            self,
            *,
            customerId: str,
            subscriptionId: str,
            body: Seats = ...,
            **kwargs: typing.Any
        ) -> SubscriptionHttpRequest: ...
        def activate(
            self, *, customerId: str, subscriptionId: str, **kwargs: typing.Any
        ) -> SubscriptionHttpRequest: ...
        def list(
            self,
            *,
            customerAuthToken: str = ...,
            maxResults: int = ...,
            pageToken: str = ...,
            customerId: str = ...,
            customerNamePrefix: str = ...,
            **kwargs: typing.Any
        ) -> SubscriptionsHttpRequest: ...
        def delete(
            self,
            *,
            customerId: str,
            subscriptionId: str,
            deletionType: typing_extensions.Literal["cancel", "transfer_to_direct"],
            **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def suspend(
            self, *, customerId: str, subscriptionId: str, **kwargs: typing.Any
        ) -> SubscriptionHttpRequest: ...
    def customers(self) -> CustomersResource: ...
    def resellernotify(self) -> ResellernotifyResource: ...
    def subscriptions(self) -> SubscriptionsResource: ...

class ResellernotifyGetwatchdetailsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ResellernotifyGetwatchdetailsResponse: ...

class SubscriptionsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Subscriptions: ...

class CustomerHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Customer: ...

class SubscriptionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Subscription: ...

class ResellernotifyResourceHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ResellernotifyResource: ...
