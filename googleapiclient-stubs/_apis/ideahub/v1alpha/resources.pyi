import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

@typing.type_check_only
class IdeahubResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class IdeasResource(googleapiclient.discovery.Resource):
        def list(
            self,
            *,
            creator_platform: typing_extensions.Literal[
                "UNKNOWN", "BLOGGER", "SITEKIT"
            ] = ...,
            creator_platformId: str = ...,
            filter: str = ...,
            orderBy: str = ...,
            pageSize: int = ...,
            pageToken: str = ...,
            parent: str = ...,
            **kwargs: typing.Any
        ) -> GoogleSearchIdeahubV1alphaListIdeasResponseHttpRequest: ...
    @typing.type_check_only
    class PlatformsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class PropertiesResource(googleapiclient.discovery.Resource):
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
                    creator_platform: typing_extensions.Literal[
                        "UNKNOWN", "BLOGGER", "SITEKIT"
                    ] = ...,
                    creator_platformId: str = ...,
                    filter: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleSearchIdeahubV1alphaListIdeasResponseHttpRequest: ...
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
            def ideaStates(self) -> IdeaStatesResource: ...
            def ideas(self) -> IdeasResource: ...
            def locales(self) -> LocalesResource: ...
        def properties(self) -> PropertiesResource: ...
    def ideas(self) -> IdeasResource: ...
    def platforms(self) -> PlatformsResource: ...

@typing.type_check_only
class GoogleSearchIdeahubV1alphaIdeaStateHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleSearchIdeahubV1alphaIdeaState: ...

@typing.type_check_only
class GoogleSearchIdeahubV1alphaListAvailableLocalesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleSearchIdeahubV1alphaListAvailableLocalesResponse: ...

@typing.type_check_only
class GoogleSearchIdeahubV1alphaListIdeasResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleSearchIdeahubV1alphaListIdeasResponse: ...
