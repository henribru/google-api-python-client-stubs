import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class CloudTraceResource(googleapiclient.discovery.Resource):
    class ProjectsResource(googleapiclient.discovery.Resource):
        class TraceSinksResource(googleapiclient.discovery.Resource):
            def list(
                self,
                *,
                parent: str,
                pageToken: str = ...,
                pageSize: int = ...,
                **kwargs: typing.Any
            ) -> ListTraceSinksResponseHttpRequest: ...
            def create(
                self, *, parent: str, body: TraceSink = ..., **kwargs: typing.Any
            ) -> TraceSinkHttpRequest: ...
            def patch(
                self,
                *,
                name: str,
                body: TraceSink = ...,
                updateMask: str = ...,
                **kwargs: typing.Any
            ) -> TraceSinkHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> TraceSinkHttpRequest: ...
        def traceSinks(self) -> TraceSinksResource: ...
    def projects(self) -> ProjectsResource: ...

class TraceSinkHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> TraceSink: ...

class ListTraceSinksResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListTraceSinksResponse: ...

class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Empty: ...
