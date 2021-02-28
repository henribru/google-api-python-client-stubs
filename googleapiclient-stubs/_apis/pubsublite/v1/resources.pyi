import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *
@typing.type_check_only
class PubsubLiteResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class AdminResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class ProjectsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class LocationsResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class SubscriptionsResource(googleapiclient.discovery.Resource):
                    def create(
                        self,
                        *,
                        parent: str,
                        body: Subscription = ...,
                        subscriptionId: str = ...,
                        **kwargs: typing.Any
                    ) -> SubscriptionHttpRequest: ...
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> EmptyHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> SubscriptionHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any
                    ) -> ListSubscriptionsResponseHttpRequest: ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: Subscription = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any
                    ) -> SubscriptionHttpRequest: ...
                @typing.type_check_only
                class TopicsResource(googleapiclient.discovery.Resource):
                    @typing.type_check_only
                    class SubscriptionsResource(googleapiclient.discovery.Resource):
                        def list(
                            self,
                            *,
                            name: str,
                            pageSize: int = ...,
                            pageToken: str = ...,
                            **kwargs: typing.Any
                        ) -> ListTopicSubscriptionsResponseHttpRequest: ...
                    def create(
                        self,
                        *,
                        parent: str,
                        body: Topic = ...,
                        topicId: str = ...,
                        **kwargs: typing.Any
                    ) -> TopicHttpRequest: ...
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> EmptyHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> TopicHttpRequest: ...
                    def getPartitions(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> TopicPartitionsHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any
                    ) -> ListTopicsResponseHttpRequest: ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: Topic = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any
                    ) -> TopicHttpRequest: ...
                    def subscriptions(self) -> SubscriptionsResource: ...
                def subscriptions(self) -> SubscriptionsResource: ...
                def topics(self) -> TopicsResource: ...
            def locations(self) -> LocationsResource: ...
        def projects(self) -> ProjectsResource: ...
    @typing.type_check_only
    class CursorResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class ProjectsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class LocationsResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class SubscriptionsResource(googleapiclient.discovery.Resource):
                    @typing.type_check_only
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
    @typing.type_check_only
    class TopicStatsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class ProjectsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class LocationsResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class TopicsResource(googleapiclient.discovery.Resource):
                    def computeHeadCursor(
                        self,
                        *,
                        topic: str,
                        body: ComputeHeadCursorRequest = ...,
                        **kwargs: typing.Any
                    ) -> ComputeHeadCursorResponseHttpRequest: ...
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
    def admin(self) -> AdminResource: ...
    def cursor(self) -> CursorResource: ...
    def topicStats(self) -> TopicStatsResource: ...

@typing.type_check_only
class ComputeHeadCursorResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> ComputeHeadCursorResponse: ...

@typing.type_check_only
class ComputeMessageStatsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> ComputeMessageStatsResponse: ...

@typing.type_check_only
class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> Empty: ...

@typing.type_check_only
class ListPartitionCursorsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> ListPartitionCursorsResponse: ...

@typing.type_check_only
class ListSubscriptionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> ListSubscriptionsResponse: ...

@typing.type_check_only
class ListTopicSubscriptionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> ListTopicSubscriptionsResponse: ...

@typing.type_check_only
class ListTopicsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> ListTopicsResponse: ...

@typing.type_check_only
class SubscriptionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> Subscription: ...

@typing.type_check_only
class TopicHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> Topic: ...

@typing.type_check_only
class TopicPartitionsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> TopicPartitions: ...
