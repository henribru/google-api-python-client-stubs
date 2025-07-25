import collections.abc
import typing

import httplib2
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http

from .schemas import *

_list = list

@typing.type_check_only
class CloudFunctionsResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class ProjectsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class LocationsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class FunctionsResource(googleapiclient.discovery.Resource):
                def abortFunctionUpgrade(
                    self,
                    *,
                    name: str,
                    body: AbortFunctionUpgradeRequest = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def commitFunctionUpgrade(
                    self,
                    *,
                    name: str,
                    body: CommitFunctionUpgradeRequest = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def create(
                    self,
                    *,
                    parent: str,
                    body: Function = ...,
                    functionId: str = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def detachFunction(
                    self,
                    *,
                    name: str,
                    body: DetachFunctionRequest = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def generateDownloadUrl(
                    self,
                    *,
                    name: str,
                    body: GenerateDownloadUrlRequest = ...,
                    **kwargs: typing.Any,
                ) -> GenerateDownloadUrlResponseHttpRequest: ...
                def generateUploadUrl(
                    self,
                    *,
                    parent: str,
                    body: GenerateUploadUrlRequest = ...,
                    **kwargs: typing.Any,
                ) -> GenerateUploadUrlResponseHttpRequest: ...
                def get(
                    self, *, name: str, revision: str = ..., **kwargs: typing.Any
                ) -> FunctionHttpRequest: ...
                def getIamPolicy(
                    self,
                    *,
                    resource: str,
                    options_requestedPolicyVersion: int = ...,
                    **kwargs: typing.Any,
                ) -> PolicyHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> ListFunctionsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListFunctionsResponseHttpRequest,
                    previous_response: ListFunctionsResponse,
                ) -> ListFunctionsResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: Function = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def redirectFunctionUpgradeTraffic(
                    self,
                    *,
                    name: str,
                    body: RedirectFunctionUpgradeTrafficRequest = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def rollbackFunctionUpgradeTraffic(
                    self,
                    *,
                    name: str,
                    body: RollbackFunctionUpgradeTrafficRequest = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def setIamPolicy(
                    self,
                    *,
                    resource: str,
                    body: SetIamPolicyRequest = ...,
                    **kwargs: typing.Any,
                ) -> PolicyHttpRequest: ...
                def setupFunctionUpgradeConfig(
                    self,
                    *,
                    name: str,
                    body: SetupFunctionUpgradeConfigRequest = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def testIamPermissions(
                    self,
                    *,
                    resource: str,
                    body: TestIamPermissionsRequest = ...,
                    **kwargs: typing.Any,
                ) -> TestIamPermissionsResponseHttpRequest: ...

            @typing.type_check_only
            class OperationsResource(googleapiclient.discovery.Resource):
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
                    **kwargs: typing.Any,
                ) -> ListOperationsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListOperationsResponseHttpRequest,
                    previous_response: ListOperationsResponse,
                ) -> ListOperationsResponseHttpRequest | None: ...

            @typing.type_check_only
            class RuntimesResource(googleapiclient.discovery.Resource):
                def list(
                    self, *, parent: str, filter: str = ..., **kwargs: typing.Any
                ) -> ListRuntimesResponseHttpRequest: ...

            def list(
                self,
                *,
                name: str,
                extraLocationTypes: str | _list[str] = ...,
                filter: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any,
            ) -> ListLocationsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListLocationsResponseHttpRequest,
                previous_response: ListLocationsResponse,
            ) -> ListLocationsResponseHttpRequest | None: ...
            def functions(self) -> FunctionsResource: ...
            def operations(self) -> OperationsResource: ...
            def runtimes(self) -> RuntimesResource: ...

        def locations(self) -> LocationsResource: ...

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
        | None = None,
    ) -> googleapiclient.http.BatchHttpRequest: ...
    def projects(self) -> ProjectsResource: ...

@typing.type_check_only
class FunctionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Function: ...

@typing.type_check_only
class GenerateDownloadUrlResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GenerateDownloadUrlResponse: ...

@typing.type_check_only
class GenerateUploadUrlResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GenerateUploadUrlResponse: ...

@typing.type_check_only
class ListFunctionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListFunctionsResponse: ...

@typing.type_check_only
class ListLocationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListLocationsResponse: ...

@typing.type_check_only
class ListOperationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListOperationsResponse: ...

@typing.type_check_only
class ListRuntimesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListRuntimesResponse: ...

@typing.type_check_only
class OperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Operation: ...

@typing.type_check_only
class PolicyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Policy: ...

@typing.type_check_only
class TestIamPermissionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> TestIamPermissionsResponse: ...
