import collections.abc
import typing

import httplib2

import googleapiclient.discovery
import googleapiclient.http

from .schemas import *

_list = list

@typing.type_check_only
class FirebaseCloudMessagingResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class ProjectsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class MessagesResource(googleapiclient.discovery.Resource):
            def send(
                self, *, parent: str, body: SendMessageRequest, **kwargs: typing.Any
            ) -> MessageHttpRequest: ...

        @typing.type_check_only
        class RegistrationsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class TopicSubscriptionsResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: TopicSubscription,
                    topicName: str | None = ...,
                    **kwargs: typing.Any,
                ) -> TopicSubscriptionHttpRequest: ...
                def delete(
                    self,
                    *,
                    name: str,
                    allowMissing: bool | None = ...,
                    **kwargs: typing.Any,
                ) -> EmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> TopicSubscriptionHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int | None = ...,
                    pageToken: str | None = ...,
                    **kwargs: typing.Any,
                ) -> ListTopicSubscriptionsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListTopicSubscriptionsResponseHttpRequest,
                    previous_response: ListTopicSubscriptionsResponse,
                ) -> ListTopicSubscriptionsResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: TopicSubscription,
                    allowMissing: bool | None = ...,
                    **kwargs: typing.Any,
                ) -> TopicSubscriptionHttpRequest: ...

            def topicSubscriptions(self) -> TopicSubscriptionsResource: ...

        def messages(self) -> MessagesResource: ...
        def registrations(self) -> RegistrationsResource: ...

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
    def projects(self) -> ProjectsResource: ...

@typing.type_check_only
class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Empty: ...

@typing.type_check_only
class ListTopicSubscriptionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListTopicSubscriptionsResponse: ...

@typing.type_check_only
class MessageHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Message: ...

@typing.type_check_only
class TopicSubscriptionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> TopicSubscription: ...
