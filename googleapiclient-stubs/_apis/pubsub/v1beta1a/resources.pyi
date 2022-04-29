import collections.abc
import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

_list = list

@typing.type_check_only
class PubsubResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class SubscriptionsResource(googleapiclient.discovery.Resource):
        def acknowledge(
            self, *, body: AcknowledgeRequest = ..., **kwargs: typing.Any
        ) -> EmptyHttpRequest: ...
        def create(
            self, *, body: Subscription = ..., **kwargs: typing.Any
        ) -> SubscriptionHttpRequest: ...
        def delete(
            self, *, subscription: str, **kwargs: typing.Any
        ) -> EmptyHttpRequest: ...
        def get(
            self, *, subscription: str, **kwargs: typing.Any
        ) -> SubscriptionHttpRequest: ...
        def list(
            self,
            *,
            maxResults: int = ...,
            pageToken: str = ...,
            query: str = ...,
            **kwargs: typing.Any
        ) -> ListSubscriptionsResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: ListSubscriptionsResponseHttpRequest,
            previous_response: ListSubscriptionsResponse,
        ) -> ListSubscriptionsResponseHttpRequest | None: ...
        def modifyAckDeadline(
            self, *, body: ModifyAckDeadlineRequest = ..., **kwargs: typing.Any
        ) -> EmptyHttpRequest: ...
        def modifyPushConfig(
            self, *, body: ModifyPushConfigRequest = ..., **kwargs: typing.Any
        ) -> EmptyHttpRequest: ...
        def pull(
            self, *, body: PullRequest = ..., **kwargs: typing.Any
        ) -> PullResponseHttpRequest: ...
        def pullBatch(
            self, *, body: PullBatchRequest = ..., **kwargs: typing.Any
        ) -> PullBatchResponseHttpRequest: ...

    @typing.type_check_only
    class TopicsResource(googleapiclient.discovery.Resource):
        def create(
            self, *, body: Topic = ..., **kwargs: typing.Any
        ) -> TopicHttpRequest: ...
        def delete(self, *, topic: str, **kwargs: typing.Any) -> EmptyHttpRequest: ...
        def get(self, *, topic: str, **kwargs: typing.Any) -> TopicHttpRequest: ...
        def list(
            self,
            *,
            maxResults: int = ...,
            pageToken: str = ...,
            query: str = ...,
            **kwargs: typing.Any
        ) -> ListTopicsResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: ListTopicsResponseHttpRequest,
            previous_response: ListTopicsResponse,
        ) -> ListTopicsResponseHttpRequest | None: ...
        def publish(
            self, *, body: PublishRequest = ..., **kwargs: typing.Any
        ) -> EmptyHttpRequest: ...
        def publishBatch(
            self, *, body: PublishBatchRequest = ..., **kwargs: typing.Any
        ) -> PublishBatchResponseHttpRequest: ...

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
    def subscriptions(self) -> SubscriptionsResource: ...
    def topics(self) -> TopicsResource: ...

@typing.type_check_only
class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Empty: ...

@typing.type_check_only
class ListSubscriptionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListSubscriptionsResponse: ...

@typing.type_check_only
class ListTopicsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListTopicsResponse: ...

@typing.type_check_only
class PublishBatchResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> PublishBatchResponse: ...

@typing.type_check_only
class PullBatchResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> PullBatchResponse: ...

@typing.type_check_only
class PullResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> PullResponse: ...

@typing.type_check_only
class SubscriptionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Subscription: ...

@typing.type_check_only
class TopicHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Topic: ...
