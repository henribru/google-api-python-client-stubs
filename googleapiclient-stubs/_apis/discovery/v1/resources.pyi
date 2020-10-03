import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class DiscoveryResource(googleapiclient.discovery.Resource):
    class ApisResource(googleapiclient.discovery.Resource):
        def list(
            self, *, name: str = ..., preferred: bool = ..., **kwargs: typing.Any
        ) -> DirectoryListHttpRequest: ...
        def getRest(
            self, *, api: str, version: str, **kwargs: typing.Any
        ) -> RestDescriptionHttpRequest: ...
    def apis(self) -> ApisResource: ...

class RestDescriptionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> RestDescription: ...

class DirectoryListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> DirectoryList: ...
