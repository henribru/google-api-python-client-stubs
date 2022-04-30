import collections.abc
import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

_list = list

@typing.type_check_only
class WebfontsResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class WebfontsResource(googleapiclient.discovery.Resource):
        def list(
            self,
            *,
            sort: typing_extensions.Literal[
                "SORT_UNDEFINED", "ALPHA", "DATE", "POPULARITY", "STYLE", "TRENDING"
            ] = ...,
            **kwargs: typing.Any
        ) -> WebfontListHttpRequest: ...

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
    def webfonts(self) -> WebfontsResource: ...

@typing.type_check_only
class WebfontListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> WebfontList: ...
