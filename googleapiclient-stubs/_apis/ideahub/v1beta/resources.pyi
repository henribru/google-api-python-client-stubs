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
    class PlatformsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class PropertiesResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class IdeaActivitiesResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleSearchIdeahubV1betaIdeaActivity = ...,
                    **kwargs: typing.Any
                ) -> GoogleSearchIdeahubV1betaIdeaActivityHttpRequest: ...

            @typing.type_check_only
            class IdeaStatesResource(googleapiclient.discovery.Resource):
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleSearchIdeahubV1betaIdeaState = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleSearchIdeahubV1betaIdeaStateHttpRequest: ...

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
                ) -> GoogleSearchIdeahubV1betaListIdeasResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleSearchIdeahubV1betaListIdeasResponseHttpRequest,
                    previous_response: GoogleSearchIdeahubV1betaListIdeasResponse,
                ) -> GoogleSearchIdeahubV1betaListIdeasResponseHttpRequest | None: ...

            @typing.type_check_only
            class LocalesResource(googleapiclient.discovery.Resource):
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleSearchIdeahubV1betaListAvailableLocalesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleSearchIdeahubV1betaListAvailableLocalesResponseHttpRequest,
                    previous_response: GoogleSearchIdeahubV1betaListAvailableLocalesResponse,
                ) -> GoogleSearchIdeahubV1betaListAvailableLocalesResponseHttpRequest | None: ...

            @typing.type_check_only
            class TopicStatesResource(googleapiclient.discovery.Resource):
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleSearchIdeahubV1betaTopicState = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleSearchIdeahubV1betaTopicStateHttpRequest: ...

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
    def platforms(self) -> PlatformsResource: ...

@typing.type_check_only
class GoogleSearchIdeahubV1betaIdeaActivityHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleSearchIdeahubV1betaIdeaActivity: ...

@typing.type_check_only
class GoogleSearchIdeahubV1betaIdeaStateHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleSearchIdeahubV1betaIdeaState: ...

@typing.type_check_only
class GoogleSearchIdeahubV1betaListAvailableLocalesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleSearchIdeahubV1betaListAvailableLocalesResponse: ...

@typing.type_check_only
class GoogleSearchIdeahubV1betaListIdeasResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleSearchIdeahubV1betaListIdeasResponse: ...

@typing.type_check_only
class GoogleSearchIdeahubV1betaTopicStateHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleSearchIdeahubV1betaTopicState: ...
