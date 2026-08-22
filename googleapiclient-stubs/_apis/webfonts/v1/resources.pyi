import collections.abc
import typing

import httplib2

import googleapiclient.discovery
import googleapiclient.http

from .schemas import *

_list = list

@typing.type_check_only
class WebfontsResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class WebfontsResource(googleapiclient.discovery.Resource):
        def list(
            self,
            *,
            capability: typing.Literal[
                "CAPABILITY_UNSPECIFIED", "WOFF2", "VF", "FAMILY_TAGS"
            ]
            | _list[
                typing.Literal["CAPABILITY_UNSPECIFIED", "WOFF2", "VF", "FAMILY_TAGS"]
            ]
            | None = ...,
            category: str | None = ...,
            family: str | _list[str] | None = ...,
            sort: typing.Literal[
                "SORT_UNDEFINED", "ALPHA", "DATE", "POPULARITY", "STYLE", "TRENDING"
            ]
            | None = ...,
            subset: str | None = ...,
            **kwargs: typing.Any,
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
        | None = None,
    ) -> googleapiclient.http.BatchHttpRequest: ...
    def webfonts(self) -> WebfontsResource: ...

@typing.type_check_only
class WebfontListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> WebfontList: ...
