import collections.abc
import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

_list = list

@typing.type_check_only
class RemoteBuildExecutionResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class ProjectsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class InstancesResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class WorkerpoolsResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleDevtoolsRemotebuildexecutionAdminV1alphaCreateWorkerPoolRequest = ...,
                    **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleDevtoolsRemotebuildexecutionAdminV1alphaWorkerPoolHttpRequest: ...
                def list(
                    self, *, parent: str, filter: str = ..., **kwargs: typing.Any
                ) -> GoogleDevtoolsRemotebuildexecutionAdminV1alphaListWorkerPoolsResponseHttpRequest: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleDevtoolsRemotebuildexecutionAdminV1alphaUpdateWorkerPoolRequest = ...,
                    **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...

            def create(
                self,
                *,
                parent: str,
                body: GoogleDevtoolsRemotebuildexecutionAdminV1alphaCreateInstanceRequest = ...,
                **kwargs: typing.Any
            ) -> GoogleLongrunningOperationHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleLongrunningOperationHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleDevtoolsRemotebuildexecutionAdminV1alphaInstanceHttpRequest: ...
            def list(
                self, *, parent: str, **kwargs: typing.Any
            ) -> GoogleDevtoolsRemotebuildexecutionAdminV1alphaListInstancesResponseHttpRequest: ...
            def patch(
                self,
                *,
                name: str,
                body: GoogleDevtoolsRemotebuildexecutionAdminV1alphaInstance = ...,
                loggingEnabled: bool = ...,
                name1: str = ...,
                updateMask: str = ...,
                **kwargs: typing.Any
            ) -> GoogleLongrunningOperationHttpRequest: ...
            def workerpools(self) -> WorkerpoolsResource: ...

        @typing.type_check_only
        class OperationsResource(googleapiclient.discovery.Resource):
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleLongrunningOperationHttpRequest: ...

        def instances(self) -> InstancesResource: ...
        def operations(self) -> OperationsResource: ...

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
    def projects(self) -> ProjectsResource: ...

@typing.type_check_only
class GoogleDevtoolsRemotebuildexecutionAdminV1alphaInstanceHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleDevtoolsRemotebuildexecutionAdminV1alphaInstance: ...

@typing.type_check_only
class GoogleDevtoolsRemotebuildexecutionAdminV1alphaListInstancesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleDevtoolsRemotebuildexecutionAdminV1alphaListInstancesResponse: ...

@typing.type_check_only
class GoogleDevtoolsRemotebuildexecutionAdminV1alphaListWorkerPoolsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleDevtoolsRemotebuildexecutionAdminV1alphaListWorkerPoolsResponse: ...

@typing.type_check_only
class GoogleDevtoolsRemotebuildexecutionAdminV1alphaWorkerPoolHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleDevtoolsRemotebuildexecutionAdminV1alphaWorkerPool: ...

@typing.type_check_only
class GoogleLongrunningOperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleLongrunningOperation: ...
