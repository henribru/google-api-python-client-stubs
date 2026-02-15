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
    class MessageResource(googleapiclient.discovery.Resource):
        def stream(
            self, *, body: SendMessageRequest = ..., **kwargs: typing.Any
        ) -> StreamResponseHttpRequest: ...

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

    @typing.type_check_only
    class TasksResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class PushNotificationConfigsResource(googleapiclient.discovery.Resource):
            def create(
                self,
                *,
                parent: str,
                body: TaskPushNotificationConfig = ...,
                configId: str = ...,
                tenant: str = ...,
                **kwargs: typing.Any,
            ) -> TaskPushNotificationConfigHttpRequest: ...
            def delete(
                self, *, name: str, tenant: str = ..., **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def get(
                self, *, name: str, tenant: str = ..., **kwargs: typing.Any
            ) -> TaskPushNotificationConfigHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                tenant: str = ...,
                **kwargs: typing.Any,
            ) -> ListTaskPushNotificationConfigResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListTaskPushNotificationConfigResponseHttpRequest,
                previous_response: ListTaskPushNotificationConfigResponse,
            ) -> ListTaskPushNotificationConfigResponseHttpRequest | None: ...

        def cancel(
            self, *, name: str, body: CancelTaskRequest = ..., **kwargs: typing.Any
        ) -> TaskHttpRequest: ...
        def get(
            self,
            *,
            name: str,
            historyLength: int = ...,
            tenant: str = ...,
            **kwargs: typing.Any,
        ) -> TaskHttpRequest: ...
        def subscribe(
            self, *, name: str, tenant: str = ..., **kwargs: typing.Any
        ) -> StreamResponseHttpRequest: ...
        def pushNotificationConfigs(self) -> PushNotificationConfigsResource: ...

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
    def message(self) -> MessageResource: ...
    def operations(self) -> OperationsResource: ...
    def subscriptions(self) -> SubscriptionsResource: ...
    def tasks(self) -> TasksResource: ...

@typing.type_check_only
class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Empty: ...

@typing.type_check_only
class ListSubscriptionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListSubscriptionsResponse: ...

@typing.type_check_only
class ListTaskPushNotificationConfigResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListTaskPushNotificationConfigResponse: ...

@typing.type_check_only
class OperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Operation: ...

@typing.type_check_only
class StreamResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> StreamResponse: ...

@typing.type_check_only
class SubscriptionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Subscription: ...

@typing.type_check_only
class TaskHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Task: ...

@typing.type_check_only
class TaskPushNotificationConfigHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> TaskPushNotificationConfig: ...
