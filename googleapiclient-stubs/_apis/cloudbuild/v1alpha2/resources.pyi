import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class CloudBuildResource(googleapiclient.discovery.Resource):
    class ProjectsResource(googleapiclient.discovery.Resource):
        class LocationsResource(googleapiclient.discovery.Resource):
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
            def operations(self) -> OperationsResource: ...
        class WorkerPoolsResource(googleapiclient.discovery.Resource):
            def list(
                self, *, parent: str, **kwargs: typing.Any
            ) -> ListWorkerPoolsResponseHttpRequest: ...
            def create(
                self,
                *,
                parent: str,
                body: WorkerPool = ...,
                workerPoolId: str = ...,
                **kwargs: typing.Any
            ) -> WorkerPoolHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def patch(
                self,
                *,
                name: str,
                body: WorkerPool = ...,
                updateMask: str = ...,
                **kwargs: typing.Any
            ) -> WorkerPoolHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> WorkerPoolHttpRequest: ...
        def locations(self) -> LocationsResource: ...
        def workerPools(self) -> WorkerPoolsResource: ...
    def projects(self) -> ProjectsResource: ...

class ListWorkerPoolsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListWorkerPoolsResponse: ...

class WorkerPoolHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> WorkerPool: ...

class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Empty: ...

class OperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Operation: ...
