import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class WebfontsResource(googleapiclient.discovery.Resource):
    class WebfontsResource(googleapiclient.discovery.Resource):
        def list(
            self,
            *,
            sort: typing_extensions.Literal[
                "SORT_UNDEFINED", "ALPHA", "DATE", "POPULARITY", "STYLE", "TRENDING"
            ] = ...,
            **kwargs: typing.Any
        ) -> WebfontListHttpRequest: ...
    def webfonts(self) -> WebfontsResource: ...

class WebfontListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> WebfontList: ...
