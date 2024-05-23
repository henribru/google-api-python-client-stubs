import collections.abc
import typing

import httplib2
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http

from .schemas import *

_list = list

@typing.type_check_only
class FirebaseMLResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class ProjectsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class LocationsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class PublishersResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class ModelsResource(googleapiclient.discovery.Resource):
                    def countTokens(
                        self,
                        *,
                        endpoint: str,
                        body: CountTokensRequest = ...,
                        **kwargs: typing.Any,
                    ) -> CountTokensResponseHttpRequest: ...
                    def generateContent(
                        self,
                        *,
                        model: str,
                        body: GenerateContentRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GenerateContentResponseHttpRequest: ...
                    def streamGenerateContent(
                        self,
                        *,
                        model: str,
                        body: GenerateContentRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GenerateContentResponseHttpRequest: ...

                def models(self) -> ModelsResource: ...

            def publishers(self) -> PublishersResource: ...

        def locations(self) -> LocationsResource: ...

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
class CountTokensResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> CountTokensResponse: ...

@typing.type_check_only
class GenerateContentResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GenerateContentResponse: ...
