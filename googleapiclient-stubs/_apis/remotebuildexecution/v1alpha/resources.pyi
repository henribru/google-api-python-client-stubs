import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class RemoteBuildExecutionResource(googleapiclient.discovery.Resource):
    class ProjectsResource(googleapiclient.discovery.Resource):
        class InstancesResource(googleapiclient.discovery.Resource):
            class WorkerpoolsResource(googleapiclient.discovery.Resource):
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleDevtoolsRemotebuildexecutionAdminV1alphaWorkerPoolHttpRequest: ...
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleDevtoolsRemotebuildexecutionAdminV1alphaCreateWorkerPoolRequest = ...,
                    **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleDevtoolsRemotebuildexecutionAdminV1alphaUpdateWorkerPoolRequest = ...,
                    **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def list(
                    self, *, parent: str, filter: str = ..., **kwargs: typing.Any
                ) -> GoogleDevtoolsRemotebuildexecutionAdminV1alphaListWorkerPoolsResponseHttpRequest: ...
            def create(
                self,
                *,
                parent: str,
                body: GoogleDevtoolsRemotebuildexecutionAdminV1alphaCreateInstanceRequest = ...,
                **kwargs: typing.Any
            ) -> GoogleLongrunningOperationHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleDevtoolsRemotebuildexecutionAdminV1alphaInstanceHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleLongrunningOperationHttpRequest: ...
            def patch(
                self,
                *,
                name: str,
                body: GoogleDevtoolsRemotebuildexecutionAdminV1alphaInstance = ...,
                name1: str = ...,
                updateMask: str = ...,
                loggingEnabled: bool = ...,
                **kwargs: typing.Any
            ) -> GoogleLongrunningOperationHttpRequest: ...
            def list(
                self, *, parent: str, **kwargs: typing.Any
            ) -> GoogleDevtoolsRemotebuildexecutionAdminV1alphaListInstancesResponseHttpRequest: ...
            def workerpools(self) -> WorkerpoolsResource: ...
        class OperationsResource(googleapiclient.discovery.Resource):
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleLongrunningOperationHttpRequest: ...
        def instances(self) -> InstancesResource: ...
        def operations(self) -> OperationsResource: ...
    def projects(self) -> ProjectsResource: ...

class GoogleDevtoolsRemotebuildexecutionAdminV1alphaListWorkerPoolsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleDevtoolsRemotebuildexecutionAdminV1alphaListWorkerPoolsResponse: ...

class GoogleDevtoolsRemotebuildexecutionAdminV1alphaListInstancesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleDevtoolsRemotebuildexecutionAdminV1alphaListInstancesResponse: ...

class GoogleDevtoolsRemotebuildexecutionAdminV1alphaWorkerPoolHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleDevtoolsRemotebuildexecutionAdminV1alphaWorkerPool: ...

class GoogleLongrunningOperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleLongrunningOperation: ...

class GoogleDevtoolsRemotebuildexecutionAdminV1alphaInstanceHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleDevtoolsRemotebuildexecutionAdminV1alphaInstance: ...
