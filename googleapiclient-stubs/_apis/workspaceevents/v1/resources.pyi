import collections.abc
import typing

import httplib2
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http

from .schemas import *

_list = list

@typing.type_check_only
class WorkspaceEventsResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class OperationsResource(googleapiclient.discovery.Resource):
        def get(self, *, name: str, **kwargs: typing.Any) -> OperationHttpRequest: ...

    @typing.type_check_only
    class SubscriptionsResource(googleapiclient.discovery.Resource):
        def create(
            self,
            *,
            body: Subscription = ...,
            validateOnly: bool = ...,
            **kwargs: typing.Any,
        ) -> OperationHttpRequest: ...
        def delete(
            self,
            *,
            name: str,
            allowMissing: bool = ...,
            etag: str = ...,
            validateOnly: bool = ...,
            **kwargs: typing.Any,
        ) -> OperationHttpRequest: ...
        def get(
            self, *, name: str, **kwargs: typing.Any
        ) -> SubscriptionHttpRequest: ...
        def list(
            self,
            *,
            filter: str = ...,
            pageSize: int = ...,
            pageToken: str = ...,
            **kwargs: typing.Any,
        ) -> ListSubscriptionsResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: ListSubscriptionsResponseHttpRequest,
            previous_response: ListSubscriptionsResponse,
        ) -> ListSubscriptionsResponseHttpRequest | None: ...
        def patch(
            self,
            *,
            name: str,
            body: Subscription = ...,
            updateMask: str = ...,
            validateOnly: bool = ...,
            **kwargs: typing.Any,
        ) -> OperationHttpRequest: ...
        def reactivate(
            self,
            *,
            name: str,
            body: ReactivateSubscriptionRequest = ...,
            **kwargs: typing.Any,
        ) -> OperationHttpRequest: ...

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
    def operations(self) -> OperationsResource: ...
    def subscriptions(self) -> SubscriptionsResource: ...

@typing.type_check_only
class ListSubscriptionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListSubscriptionsResponse: ...

@typing.type_check_only
class OperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Operation: ...

@typing.type_check_only
class SubscriptionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Subscription: ...
