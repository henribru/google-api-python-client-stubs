import collections.abc
import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

_list = list

@typing.type_check_only
class IdeahubResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class IdeasResource(googleapiclient.discovery.Resource):
        def list(
            self,
            *,
            filter: str = ...,
            orderBy: str = ...,
            pageSize: int = ...,
            pageToken: str = ...,
            parent: str = ...,
            **kwargs: typing.Any
        ) -> GoogleSearchIdeahubV1alphaListIdeasResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: GoogleSearchIdeahubV1alphaListIdeasResponseHttpRequest,
            previous_response: GoogleSearchIdeahubV1alphaListIdeasResponse,
        ) -> GoogleSearchIdeahubV1alphaListIdeasResponseHttpRequest | None: ...

    @typing.type_check_only
    class PlatformsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class PropertiesResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class IdeaActivitiesResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleSearchIdeahubV1alphaIdeaActivity = ...,
                    **kwargs: typing.Any
                ) -> GoogleSearchIdeahubV1alphaIdeaActivityHttpRequest: ...

            @typing.type_check_only
            class IdeaStatesResource(googleapiclient.discovery.Resource):
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleSearchIdeahubV1alphaIdeaState = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleSearchIdeahubV1alphaIdeaStateHttpRequest: ...

            @typing.type_check_only
            class IdeasResource(googleapiclient.discovery.Resource):
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleSearchIdeahubV1alphaListIdeasResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleSearchIdeahubV1alphaListIdeasResponseHttpRequest,
                    previous_response: GoogleSearchIdeahubV1alphaListIdeasResponse,
                ) -> GoogleSearchIdeahubV1alphaListIdeasResponseHttpRequest | None: ...

            @typing.type_check_only
            class LocalesResource(googleapiclient.discovery.Resource):
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleSearchIdeahubV1alphaListAvailableLocalesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleSearchIdeahubV1alphaListAvailableLocalesResponseHttpRequest,
                    previous_response: GoogleSearchIdeahubV1alphaListAvailableLocalesResponse,
                ) -> GoogleSearchIdeahubV1alphaListAvailableLocalesResponseHttpRequest | None: ...

            @typing.type_check_only
            class TopicStatesResource(googleapiclient.discovery.Resource):
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleSearchIdeahubV1alphaTopicState = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleSearchIdeahubV1alphaTopicStateHttpRequest: ...

            def ideaActivities(self) -> IdeaActivitiesResource: ...
            def ideaStates(self) -> IdeaStatesResource: ...
            def ideas(self) -> IdeasResource: ...
            def locales(self) -> LocalesResource: ...
            def topicStates(self) -> TopicStatesResource: ...

        def properties(self) -> PropertiesResource: ...

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
    def ideas(self) -> IdeasResource: ...
    def platforms(self) -> PlatformsResource: ...

@typing.type_check_only
class GoogleSearchIdeahubV1alphaIdeaActivityHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleSearchIdeahubV1alphaIdeaActivity: ...

@typing.type_check_only
class GoogleSearchIdeahubV1alphaIdeaStateHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleSearchIdeahubV1alphaIdeaState: ...

@typing.type_check_only
class GoogleSearchIdeahubV1alphaListAvailableLocalesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleSearchIdeahubV1alphaListAvailableLocalesResponse: ...

@typing.type_check_only
class GoogleSearchIdeahubV1alphaListIdeasResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleSearchIdeahubV1alphaListIdeasResponse: ...

@typing.type_check_only
class GoogleSearchIdeahubV1alphaTopicStateHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleSearchIdeahubV1alphaTopicState: ...
