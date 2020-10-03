import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class PubsubResource(googleapiclient.discovery.Resource):
    class ProjectsResource(googleapiclient.discovery.Resource):
        class TopicsResource(googleapiclient.discovery.Resource):
            class SnapshotsResource(googleapiclient.discovery.Resource):
                def list(
                    self,
                    *,
                    topic: str,
                    pageToken: str = ...,
                    pageSize: int = ...,
                    **kwargs: typing.Any
                ) -> ListTopicSnapshotsResponseHttpRequest: ...
            class SubscriptionsResource(googleapiclient.discovery.Resource):
                def list(
                    self,
                    *,
                    topic: str,
                    pageToken: str = ...,
                    pageSize: int = ...,
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
            def setIamPolicy(
                self,
                *,
                resource: str,
                body: SetIamPolicyRequest = ...,
                **kwargs: typing.Any
            ) -> PolicyHttpRequest: ...
            def create(
                self, *, name: str, body: Topic = ..., **kwargs: typing.Any
            ) -> TopicHttpRequest: ...
            def get(self, *, topic: str, **kwargs: typing.Any) -> TopicHttpRequest: ...
            def testIamPermissions(
                self,
                *,
                resource: str,
                body: TestIamPermissionsRequest = ...,
                **kwargs: typing.Any
            ) -> TestIamPermissionsResponseHttpRequest: ...
            def getIamPolicy(
                self,
                *,
                resource: str,
                options_requestedPolicyVersion: int = ...,
                **kwargs: typing.Any
            ) -> PolicyHttpRequest: ...
            def delete(
                self, *, topic: str, **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def publish(
                self, *, topic: str, body: PublishRequest = ..., **kwargs: typing.Any
            ) -> PublishResponseHttpRequest: ...
            def patch(
                self, *, name: str, body: UpdateTopicRequest = ..., **kwargs: typing.Any
            ) -> TopicHttpRequest: ...
            def snapshots(self) -> SnapshotsResource: ...
            def subscriptions(self) -> SubscriptionsResource: ...
        class SubscriptionsResource(googleapiclient.discovery.Resource):
            def setIamPolicy(
                self,
                *,
                resource: str,
                body: SetIamPolicyRequest = ...,
                **kwargs: typing.Any
            ) -> PolicyHttpRequest: ...
            def seek(
                self,
                *,
                subscription: str,
                body: SeekRequest = ...,
                **kwargs: typing.Any
            ) -> SeekResponseHttpRequest: ...
            def modifyPushConfig(
                self,
                *,
                subscription: str,
                body: ModifyPushConfigRequest = ...,
                **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def list(
                self,
                *,
                project: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> ListSubscriptionsResponseHttpRequest: ...
            def modifyAckDeadline(
                self,
                *,
                subscription: str,
                body: ModifyAckDeadlineRequest = ...,
                **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def pull(
                self,
                *,
                subscription: str,
                body: PullRequest = ...,
                **kwargs: typing.Any
            ) -> PullResponseHttpRequest: ...
            def getIamPolicy(
                self,
                *,
                resource: str,
                options_requestedPolicyVersion: int = ...,
                **kwargs: typing.Any
            ) -> PolicyHttpRequest: ...
            def get(
                self, *, subscription: str, **kwargs: typing.Any
            ) -> SubscriptionHttpRequest: ...
            def create(
                self, *, name: str, body: Subscription = ..., **kwargs: typing.Any
            ) -> SubscriptionHttpRequest: ...
            def acknowledge(
                self,
                *,
                subscription: str,
                body: AcknowledgeRequest = ...,
                **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def testIamPermissions(
                self,
                *,
                resource: str,
                body: TestIamPermissionsRequest = ...,
                **kwargs: typing.Any
            ) -> TestIamPermissionsResponseHttpRequest: ...
            def delete(
                self, *, subscription: str, **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def patch(
                self,
                *,
                name: str,
                body: UpdateSubscriptionRequest = ...,
                **kwargs: typing.Any
            ) -> SubscriptionHttpRequest: ...
            def detach(
                self, *, subscription: str, **kwargs: typing.Any
            ) -> DetachSubscriptionResponseHttpRequest: ...
        class SnapshotsResource(googleapiclient.discovery.Resource):
            def create(
                self,
                *,
                name: str,
                body: CreateSnapshotRequest = ...,
                **kwargs: typing.Any
            ) -> SnapshotHttpRequest: ...
            def get(
                self, *, snapshot: str, **kwargs: typing.Any
            ) -> SnapshotHttpRequest: ...
            def patch(
                self,
                *,
                name: str,
                body: UpdateSnapshotRequest = ...,
                **kwargs: typing.Any
            ) -> SnapshotHttpRequest: ...
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
            ) -> ListSnapshotsResponseHttpRequest: ...
            def delete(
                self, *, snapshot: str, **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
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
        def topics(self) -> TopicsResource: ...
        def subscriptions(self) -> SubscriptionsResource: ...
        def snapshots(self) -> SnapshotsResource: ...
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

class DetachSubscriptionResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> DetachSubscriptionResponse: ...

class ListTopicsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListTopicsResponse: ...

class PullResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> PullResponse: ...

class ListSnapshotsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListSnapshotsResponse: ...

class PublishResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> PublishResponse: ...

class TestIamPermissionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> TestIamPermissionsResponse: ...

class SnapshotHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Snapshot: ...

class PolicyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Policy: ...

class SeekResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> SeekResponse: ...

class TopicHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Topic: ...

class SubscriptionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Subscription: ...

class ListTopicSnapshotsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListTopicSnapshotsResponse: ...
