import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class PubsubResource(googleapiclient.discovery.Resource):
    class ProjectsResource(googleapiclient.discovery.Resource):
        class SubscriptionsResource(googleapiclient.discovery.Resource):
            def setIamPolicy(
                self,
                *,
                resource: str,
                body: SetIamPolicyRequest = ...,
                **kwargs: typing.Any
            ) -> PolicyHttpRequest: ...
            def delete(
                self, *, subscription: str, **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def getIamPolicy(
                self,
                *,
                resource: str,
                options_requestedPolicyVersion: int = ...,
                **kwargs: typing.Any
            ) -> PolicyHttpRequest: ...
            def modifyAckDeadline(
                self,
                *,
                subscription: str,
                body: ModifyAckDeadlineRequest = ...,
                **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def create(
                self, *, name: str, body: Subscription = ..., **kwargs: typing.Any
            ) -> SubscriptionHttpRequest: ...
            def list(
                self,
                *,
                project: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> ListSubscriptionsResponseHttpRequest: ...
            def acknowledge(
                self,
                *,
                subscription: str,
                body: AcknowledgeRequest = ...,
                **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def get(
                self, *, subscription: str, **kwargs: typing.Any
            ) -> SubscriptionHttpRequest: ...
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
            def testIamPermissions(
                self,
                *,
                resource: str,
                body: TestIamPermissionsRequest = ...,
                **kwargs: typing.Any
            ) -> TestIamPermissionsResponseHttpRequest: ...
        class TopicsResource(googleapiclient.discovery.Resource):
            class SubscriptionsResource(googleapiclient.discovery.Resource):
                def list(
                    self,
                    *,
                    topic: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> ListTopicSubscriptionsResponseHttpRequest: ...
            def list(
                self,
                *,
                project: str,
                pageToken: str = ...,
                pageSize: int = ...,
                **kwargs: typing.Any
            ) -> ListTopicsResponseHttpRequest: ...
            def testIamPermissions(
                self,
                *,
                resource: str,
                body: TestIamPermissionsRequest = ...,
                **kwargs: typing.Any
            ) -> TestIamPermissionsResponseHttpRequest: ...
            def publish(
                self, *, topic: str, body: PublishRequest = ..., **kwargs: typing.Any
            ) -> PublishResponseHttpRequest: ...
            def create(
                self, *, name: str, body: Topic = ..., **kwargs: typing.Any
            ) -> TopicHttpRequest: ...
            def getIamPolicy(
                self,
                *,
                resource: str,
                options_requestedPolicyVersion: int = ...,
                **kwargs: typing.Any
            ) -> PolicyHttpRequest: ...
            def get(self, *, topic: str, **kwargs: typing.Any) -> TopicHttpRequest: ...
            def delete(
                self, *, topic: str, **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def setIamPolicy(
                self,
                *,
                resource: str,
                body: SetIamPolicyRequest = ...,
                **kwargs: typing.Any
            ) -> PolicyHttpRequest: ...
            def subscriptions(self) -> SubscriptionsResource: ...
        def subscriptions(self) -> SubscriptionsResource: ...
        def topics(self) -> TopicsResource: ...
    def projects(self) -> ProjectsResource: ...

class ListSubscriptionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListSubscriptionsResponse: ...

class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Empty: ...

class ListTopicSubscriptionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListTopicSubscriptionsResponse: ...

class PullResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> PullResponse: ...

class PublishResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> PublishResponse: ...

class TestIamPermissionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> TestIamPermissionsResponse: ...

class PolicyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Policy: ...

class TopicHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Topic: ...

class SubscriptionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Subscription: ...

class ListTopicsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListTopicsResponse: ...
