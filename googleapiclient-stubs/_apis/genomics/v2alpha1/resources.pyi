import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class GenomicsResource(googleapiclient.discovery.Resource):
    class ProjectsResource(googleapiclient.discovery.Resource):
        class OperationsResource(googleapiclient.discovery.Resource):
            def list(
                self,
                *,
                name: str,
                pageSize: int = ...,
                filter: str = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> ListOperationsResponseHttpRequest: ...
            def cancel(
                self,
                *,
                name: str,
                body: CancelOperationRequest = ...,
                **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> OperationHttpRequest: ...
        class WorkersResource(googleapiclient.discovery.Resource):
            def checkIn(
                self, *, id: str, body: CheckInRequest = ..., **kwargs: typing.Any
            ) -> CheckInResponseHttpRequest: ...
        def operations(self) -> OperationsResource: ...
        def workers(self) -> WorkersResource: ...
    class PipelinesResource(googleapiclient.discovery.Resource):
        def run(
            self, *, body: RunPipelineRequest = ..., **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
    class WorkersResource(googleapiclient.discovery.Resource):
        def checkIn(
            self, *, id: str, body: CheckInRequest = ..., **kwargs: typing.Any
        ) -> CheckInResponseHttpRequest: ...
    def projects(self) -> ProjectsResource: ...
    def pipelines(self) -> PipelinesResource: ...
    def workers(self) -> WorkersResource: ...

class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Empty: ...

class OperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Operation: ...

class ListOperationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListOperationsResponse: ...

class CheckInResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> CheckInResponse: ...
