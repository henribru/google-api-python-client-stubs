import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class CloudTraceResource(googleapiclient.discovery.Resource):
    class ProjectsResource(googleapiclient.discovery.Resource):
        class TracesResource(googleapiclient.discovery.Resource):
            class SpansResource(googleapiclient.discovery.Resource):
                def createSpan(
                    self, *, name: str, body: Span = ..., **kwargs: typing.Any
                ) -> SpanHttpRequest: ...
            def batchWrite(
                self,
                *,
                name: str,
                body: BatchWriteSpansRequest = ...,
                **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def spans(self) -> SpansResource: ...
        def traces(self) -> TracesResource: ...
    def projects(self) -> ProjectsResource: ...

class SpanHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Span: ...

class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Empty: ...
