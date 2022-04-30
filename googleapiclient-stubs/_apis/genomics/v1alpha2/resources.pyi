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
    class OperationsResource(googleapiclient.discovery.Resource):
        def cancel(
            self, *, name: str, body: CancelOperationRequest = ..., **kwargs: typing.Any
        ) -> EmptyHttpRequest: ...
        def get(self, *, name: str, **kwargs: typing.Any) -> OperationHttpRequest: ...
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
    class PipelinesResource(googleapiclient.discovery.Resource):
        def create(
            self, *, body: Pipeline = ..., **kwargs: typing.Any
        ) -> PipelineHttpRequest: ...
        def delete(
            self, *, pipelineId: str, **kwargs: typing.Any
        ) -> EmptyHttpRequest: ...
        def get(
            self, *, pipelineId: str, **kwargs: typing.Any
        ) -> PipelineHttpRequest: ...
        def getControllerConfig(
            self,
            *,
            operationId: str = ...,
            validationToken: str = ...,
            **kwargs: typing.Any
        ) -> ControllerConfigHttpRequest: ...
        def list(
            self,
            *,
            namePrefix: str = ...,
            pageSize: int = ...,
            pageToken: str = ...,
            projectId: str = ...,
            **kwargs: typing.Any
        ) -> ListPipelinesResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: ListPipelinesResponseHttpRequest,
            previous_response: ListPipelinesResponse,
        ) -> ListPipelinesResponseHttpRequest | None: ...
        def run(
            self, *, body: RunPipelineRequest = ..., **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def setOperationStatus(
            self, *, body: SetOperationStatusRequest = ..., **kwargs: typing.Any
        ) -> EmptyHttpRequest: ...

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
    def operations(self) -> OperationsResource: ...
    def pipelines(self) -> PipelinesResource: ...

@typing.type_check_only
class ControllerConfigHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ControllerConfig: ...

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
class ListPipelinesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListPipelinesResponse: ...

@typing.type_check_only
class OperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Operation: ...

@typing.type_check_only
class PipelineHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Pipeline: ...
