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
            def get(
                self, *, projectId: str, traceId: str, **kwargs: typing.Any
            ) -> TraceHttpRequest: ...
            def list(
                self,
                *,
                projectId: str,
                endTime: str = ...,
                filter: str = ...,
                orderBy: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                startTime: str = ...,
                view: typing_extensions.Literal[
                    "VIEW_TYPE_UNSPECIFIED", "MINIMAL", "ROOTSPAN", "COMPLETE"
                ] = ...,
                **kwargs: typing.Any
            ) -> ListTracesResponseHttpRequest: ...
        def patchTraces(
            self, *, projectId: str, body: Traces = ..., **kwargs: typing.Any
        ) -> EmptyHttpRequest: ...
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
class ListTracesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> ListTracesResponse: ...

@typing.type_check_only
class TraceHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> Trace: ...
