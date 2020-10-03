import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class KgsearchResource(googleapiclient.discovery.Resource):
    class EntitiesResource(googleapiclient.discovery.Resource):
        def search(
            self,
            *,
            types: typing.Union[str, typing.List[str]] = ...,
            languages: typing.Union[str, typing.List[str]] = ...,
            prefix: bool = ...,
            ids: typing.Union[str, typing.List[str]] = ...,
            limit: int = ...,
            indent: bool = ...,
            query: str = ...,
            **kwargs: typing.Any
        ) -> SearchResponseHttpRequest: ...
    def entities(self) -> EntitiesResource: ...

class SearchResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> SearchResponse: ...
