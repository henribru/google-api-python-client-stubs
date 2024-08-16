import collections.abc
import typing

import httplib2
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http

from .schemas import *

_list = list

@typing.type_check_only
class MerchantResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class AccountsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class NotificationsubscriptionsResource(googleapiclient.discovery.Resource):
            def create(
                self,
                *,
                parent: str,
                body: NotificationSubscription = ...,
                **kwargs: typing.Any,
            ) -> NotificationSubscriptionHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> NotificationSubscriptionHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any,
            ) -> ListNotificationSubscriptionsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListNotificationSubscriptionsResponseHttpRequest,
                previous_response: ListNotificationSubscriptionsResponse,
            ) -> ListNotificationSubscriptionsResponseHttpRequest | None: ...
            def patch(
                self,
                *,
                name: str,
                body: NotificationSubscription = ...,
                updateMask: str = ...,
                **kwargs: typing.Any,
            ) -> NotificationSubscriptionHttpRequest: ...

        def notificationsubscriptions(self) -> NotificationsubscriptionsResource: ...

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
    def accounts(self) -> AccountsResource: ...

@typing.type_check_only
class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Empty: ...

@typing.type_check_only
class ListNotificationSubscriptionsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListNotificationSubscriptionsResponse: ...

@typing.type_check_only
class NotificationSubscriptionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> NotificationSubscription: ...
