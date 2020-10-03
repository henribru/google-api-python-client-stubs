import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class CloudTraceResource(googleapiclient.discovery.Resource):
    class ProjectsResource(googleapiclient.discovery.Resource):
        class TracesResource(googleapiclient.discovery.Resource):
            def list(
                self,
                *,
                projectId: str,
                endTime: str = ...,
                startTime: str = ...,
                filter: str = ...,
                view: typing_extensions.Literal[
                    "VIEW_TYPE_UNSPECIFIED", "MINIMAL", "ROOTSPAN", "COMPLETE"
                ] = ...,
                pageToken: str = ...,
                orderBy: str = ...,
                pageSize: int = ...,
                **kwargs: typing.Any
            ) -> ListTracesResponseHttpRequest: ...
            def get(
                self, *, projectId: str, traceId: str, **kwargs: typing.Any
            ) -> TraceHttpRequest: ...
        def patchTraces(
            self, *, projectId: str, body: Traces = ..., **kwargs: typing.Any
        ) -> EmptyHttpRequest: ...
        def traces(self) -> TracesResource: ...
    def projects(self) -> ProjectsResource: ...

class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Empty: ...

class TraceHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Trace: ...

class ListTracesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListTracesResponse: ...
