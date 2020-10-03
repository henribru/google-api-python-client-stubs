import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class GenomicsResource(googleapiclient.discovery.Resource):
    class OperationsResource(googleapiclient.discovery.Resource):
        def list(
            self,
            *,
            name: str,
            filter: str = ...,
            pageToken: str = ...,
            pageSize: int = ...,
            **kwargs: typing.Any
        ) -> ListOperationsResponseHttpRequest: ...
        def get(self, *, name: str, **kwargs: typing.Any) -> OperationHttpRequest: ...
        def cancel(
            self, *, name: str, body: CancelOperationRequest = ..., **kwargs: typing.Any
        ) -> EmptyHttpRequest: ...
    class PipelinesResource(googleapiclient.discovery.Resource):
        def delete(
            self, *, pipelineId: str, **kwargs: typing.Any
        ) -> EmptyHttpRequest: ...
        def create(
            self, *, body: Pipeline = ..., **kwargs: typing.Any
        ) -> PipelineHttpRequest: ...
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
            projectId: str = ...,
            pageToken: str = ...,
            **kwargs: typing.Any
        ) -> ListPipelinesResponseHttpRequest: ...
        def setOperationStatus(
            self, *, body: SetOperationStatusRequest = ..., **kwargs: typing.Any
        ) -> EmptyHttpRequest: ...
        def run(
            self, *, body: RunPipelineRequest = ..., **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
    def operations(self) -> OperationsResource: ...
    def pipelines(self) -> PipelinesResource: ...

class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Empty: ...

class ListOperationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListOperationsResponse: ...

class ListPipelinesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListPipelinesResponse: ...

class OperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Operation: ...

class PipelineHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Pipeline: ...

class ControllerConfigHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ControllerConfig: ...
