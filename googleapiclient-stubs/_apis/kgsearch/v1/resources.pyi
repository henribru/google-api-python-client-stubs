import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *
@typing.type_check_only
class KgsearchResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class EntitiesResource(googleapiclient.discovery.Resource):
        def search(
            self,
            *,
            ids: typing.Union[str, typing.List[str]] = ...,
            indent: bool = ...,
            languages: typing.Union[str, typing.List[str]] = ...,
            limit: int = ...,
            prefix: bool = ...,
            query: str = ...,
            types: typing.Union[str, typing.List[str]] = ...,
            **kwargs: typing.Any
        ) -> SearchResponseHttpRequest: ...
    def entities(self) -> EntitiesResource: ...

@typing.type_check_only
class SearchResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> SearchResponse: ...
