import collections.abc
import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

_list = list

@typing.type_check_only
class GenomicsResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class PipelinesResource(googleapiclient.discovery.Resource):
        def run(
            self, *, body: RunPipelineRequest = ..., **kwargs: typing.Any
        ) -> OperationHttpRequest: ...

    @typing.type_check_only
    class ProjectsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class OperationsResource(googleapiclient.discovery.Resource):
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
            def list(
                self,
                *,
                name: str,
                filter: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> ListOperationsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListOperationsResponseHttpRequest,
                previous_response: ListOperationsResponse,
            ) -> ListOperationsResponseHttpRequest | None: ...

        @typing.type_check_only
        class WorkersResource(googleapiclient.discovery.Resource):
            def checkIn(
                self, *, id: str, body: CheckInRequest = ..., **kwargs: typing.Any
            ) -> CheckInResponseHttpRequest: ...

        def operations(self) -> OperationsResource: ...
        def workers(self) -> WorkersResource: ...

    @typing.type_check_only
    class WorkersResource(googleapiclient.discovery.Resource):
        def checkIn(
            self, *, id: str, body: CheckInRequest = ..., **kwargs: typing.Any
        ) -> CheckInResponseHttpRequest: ...

    def new_batch_http_request(
        self,
        callback: collections.abc.Callable[
            [
                str,
                googleapiclient.http.HttpRequest,
                googleapiclient.errors.HttpError | None,
            ],
            typing.Any,
        ]
        | None = ...,
    ) -> googleapiclient.http.BatchHttpRequest: ...
    def pipelines(self) -> PipelinesResource: ...
    def projects(self) -> ProjectsResource: ...
    def workers(self) -> WorkersResource: ...

@typing.type_check_only
class CheckInResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> CheckInResponse: ...

@typing.type_check_only
class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Empty: ...

@typing.type_check_only
class ListOperationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListOperationsResponse: ...

@typing.type_check_only
class OperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Operation: ...
