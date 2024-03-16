import collections.abc
import typing

import httplib2
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http

from .schemas import *

_list = list

@typing.type_check_only
class PlayGroupingResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class AppsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class TokensResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class TagsResource(googleapiclient.discovery.Resource):
                def createOrUpdate(
                    self,
                    *,
                    appPackage: str,
                    token: str,
                    body: CreateOrUpdateTagsRequest = ...,
                    **kwargs: typing.Any,
                ) -> CreateOrUpdateTagsResponseHttpRequest: ...

            def verify(
                self,
                *,
                appPackage: str,
                token: str,
                body: VerifyTokenRequest = ...,
                **kwargs: typing.Any,
            ) -> VerifyTokenResponseHttpRequest: ...
            def tags(self) -> TagsResource: ...

        def tokens(self) -> TokensResource: ...

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
    def apps(self) -> AppsResource: ...

@typing.type_check_only
class CreateOrUpdateTagsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> CreateOrUpdateTagsResponse: ...

@typing.type_check_only
class VerifyTokenResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> VerifyTokenResponse: ...
