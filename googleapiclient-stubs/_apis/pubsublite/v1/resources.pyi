import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class PubsubLiteResource(googleapiclient.discovery.Resource):
    class TopicStatsResource(googleapiclient.discovery.Resource):
        class ProjectsResource(googleapiclient.discovery.Resource):
            class LocationsResource(googleapiclient.discovery.Resource):
                class TopicsResource(googleapiclient.discovery.Resource):
                    def computeMessageStats(
                        self,
                        *,
                        topic: str,
                        body: ComputeMessageStatsRequest = ...,
                        **kwargs: typing.Any
                    ) -> ComputeMessageStatsResponseHttpRequest: ...
                def topics(self) -> TopicsResource: ...
            def locations(self) -> LocationsResource: ...
        def projects(self) -> ProjectsResource: ...
    class CursorResource(googleapiclient.discovery.Resource):
        class ProjectsResource(googleapiclient.discovery.Resource):
            class LocationsResource(googleapiclient.discovery.Resource):
                class SubscriptionsResource(googleapiclient.discovery.Resource):
                    class CursorsResource(googleapiclient.discovery.Resource):
                        def list(
                            self,
                            *,
                            parent: str,
                            pageSize: int = ...,
                            pageToken: str = ...,
                            **kwargs: typing.Any
                        ) -> ListPartitionCursorsResponseHttpRequest: ...
                    def cursors(self) -> CursorsResource: ...
                def subscriptions(self) -> SubscriptionsResource: ...
            def locations(self) -> LocationsResource: ...
        def projects(self) -> ProjectsResource: ...
    class AdminResource(googleapiclient.discovery.Resource):
        class ProjectsResource(googleapiclient.discovery.Resource):
            class LocationsResource(googleapiclient.discovery.Resource):
                class TopicsResource(googleapiclient.discovery.Resource):
                    class SubscriptionsResource(googleapiclient.discovery.Resource):
                        def list(
                            self,
                            *,
                            name: str,
                            pageSize: int = ...,
                            pageToken: str = ...,
                            **kwargs: typing.Any
                        ) -> ListTopicSubscriptionsResponseHttpRequest: ...
                    def getPartitions(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> TopicPartitionsHttpRequest: ...
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> EmptyHttpRequest: ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: Topic = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any
                    ) -> TopicHttpRequest: ...
                    def create(
                        self,
                        *,
                        parent: str,
                        body: Topic = ...,
                        topicId: str = ...,
                        **kwargs: typing.Any
                    ) -> TopicHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> TopicHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any
                    ) -> ListTopicsResponseHttpRequest: ...
                    def subscriptions(self) -> SubscriptionsResource: ...
                class SubscriptionsResource(googleapiclient.discovery.Resource):
                    def patch(
                        self,
                        *,
                        name: str,
                        body: Subscription = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any
                    ) -> SubscriptionHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> SubscriptionHttpRequest: ...
                    def create(
                        self,
                        *,
                        parent: str,
                        body: Subscription = ...,
                        subscriptionId: str = ...,
                        **kwargs: typing.Any
                    ) -> SubscriptionHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any
                    ) -> ListSubscriptionsResponseHttpRequest: ...
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> EmptyHttpRequest: ...
                def topics(self) -> TopicsResource: ...
                def subscriptions(self) -> SubscriptionsResource: ...
            def locations(self) -> LocationsResource: ...
        def projects(self) -> ProjectsResource: ...
    def topicStats(self) -> TopicStatsResource: ...
    def cursor(self) -> CursorResource: ...
    def admin(self) -> AdminResource: ...

class ListPartitionCursorsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListPartitionCursorsResponse: ...

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

class TopicPartitionsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> TopicPartitions: ...

class ComputeMessageStatsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ComputeMessageStatsResponse: ...

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
