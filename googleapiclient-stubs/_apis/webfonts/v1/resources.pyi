import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *
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
    def webfonts(self) -> WebfontsResource: ...

@typing.type_check_only
class WebfontListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> WebfontList: ...
