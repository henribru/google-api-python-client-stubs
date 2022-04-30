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
    class ProjectsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class SubscriptionsResource(googleapiclient.discovery.Resource):
            def acknowledge(
                self,
                *,
                subscription: str,
                body: AcknowledgeRequest = ...,
                **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def create(
                self, *, name: str, body: Subscription = ..., **kwargs: typing.Any
            ) -> SubscriptionHttpRequest: ...
            def delete(
                self, *, subscription: str, **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def get(
                self, *, subscription: str, **kwargs: typing.Any
            ) -> SubscriptionHttpRequest: ...
            def getIamPolicy(
                self,
                *,
                resource: str,
                options_requestedPolicyVersion: int = ...,
                **kwargs: typing.Any
            ) -> PolicyHttpRequest: ...
            def list(
                self,
                *,
                project: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> ListSubscriptionsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListSubscriptionsResponseHttpRequest,
                previous_response: ListSubscriptionsResponse,
            ) -> ListSubscriptionsResponseHttpRequest | None: ...
            def modifyAckDeadline(
                self,
                *,
                subscription: str,
                body: ModifyAckDeadlineRequest = ...,
                **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def modifyPushConfig(
                self,
                *,
                subscription: str,
                body: ModifyPushConfigRequest = ...,
                **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def pull(
                self,
                *,
                subscription: str,
                body: PullRequest = ...,
                **kwargs: typing.Any
            ) -> PullResponseHttpRequest: ...
            def setIamPolicy(
                self,
                *,
                resource: str,
                body: SetIamPolicyRequest = ...,
                **kwargs: typing.Any
            ) -> PolicyHttpRequest: ...
            def testIamPermissions(
                self,
                *,
                resource: str,
                body: TestIamPermissionsRequest = ...,
                **kwargs: typing.Any
            ) -> TestIamPermissionsResponseHttpRequest: ...

        @typing.type_check_only
        class TopicsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class SubscriptionsResource(googleapiclient.discovery.Resource):
                def list(
                    self,
                    *,
                    topic: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> ListTopicSubscriptionsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListTopicSubscriptionsResponseHttpRequest,
                    previous_response: ListTopicSubscriptionsResponse,
                ) -> ListTopicSubscriptionsResponseHttpRequest | None: ...

            def create(
                self, *, name: str, body: Topic = ..., **kwargs: typing.Any
            ) -> TopicHttpRequest: ...
            def delete(
                self, *, topic: str, **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def get(self, *, topic: str, **kwargs: typing.Any) -> TopicHttpRequest: ...
            def getIamPolicy(
                self,
                *,
                resource: str,
                options_requestedPolicyVersion: int = ...,
                **kwargs: typing.Any
            ) -> PolicyHttpRequest: ...
            def list(
                self,
                *,
                project: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> ListTopicsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListTopicsResponseHttpRequest,
                previous_response: ListTopicsResponse,
            ) -> ListTopicsResponseHttpRequest | None: ...
            def publish(
                self, *, topic: str, body: PublishRequest = ..., **kwargs: typing.Any
            ) -> PublishResponseHttpRequest: ...
            def setIamPolicy(
                self,
                *,
                resource: str,
                body: SetIamPolicyRequest = ...,
                **kwargs: typing.Any
            ) -> PolicyHttpRequest: ...
            def testIamPermissions(
                self,
                *,
                resource: str,
                body: TestIamPermissionsRequest = ...,
                **kwargs: typing.Any
            ) -> TestIamPermissionsResponseHttpRequest: ...
            def subscriptions(self) -> SubscriptionsResource: ...

        def subscriptions(self) -> SubscriptionsResource: ...
        def topics(self) -> TopicsResource: ...

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
    def projects(self) -> ProjectsResource: ...

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
class ListTopicSubscriptionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListTopicSubscriptionsResponse: ...

@typing.type_check_only
class ListTopicsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListTopicsResponse: ...

@typing.type_check_only
class PolicyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Policy: ...

@typing.type_check_only
class PublishResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> PublishResponse: ...

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
class TestIamPermissionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> TestIamPermissionsResponse: ...

@typing.type_check_only
class TopicHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Topic: ...
