import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *
@typing.type_check_only
class CloudTraceResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class ProjectsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class TracesResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
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

@typing.type_check_only
class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> Empty: ...

@typing.type_check_only
class SpanHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> Span: ...
