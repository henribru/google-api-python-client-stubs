import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

_list = list

@typing.type_check_only
class KgsearchResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class EntitiesResource(googleapiclient.discovery.Resource):
        def search(
            self,
            *,
            ids: str | _list[str] = ...,
            indent: bool = ...,
            languages: str | _list[str] = ...,
            limit: int = ...,
            prefix: bool = ...,
            query: str = ...,
            types: str | _list[str] = ...,
            **kwargs: typing.Any
        ) -> SearchResponseHttpRequest: ...
    def entities(self) -> EntitiesResource: ...

@typing.type_check_only
class SearchResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> SearchResponse: ...
