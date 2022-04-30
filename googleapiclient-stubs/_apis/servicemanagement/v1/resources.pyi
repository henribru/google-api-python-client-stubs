import collections.abc
import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

_list = list

@typing.type_check_only
class ServiceManagementResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class OperationsResource(googleapiclient.discovery.Resource):
        def get(self, *, name: str, **kwargs: typing.Any) -> OperationHttpRequest: ...
        def list(
            self,
            *,
            filter: str = ...,
            name: str = ...,
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
    class ServicesResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class ConfigsResource(googleapiclient.discovery.Resource):
            def create(
                self, *, serviceName: str, body: Service = ..., **kwargs: typing.Any
            ) -> ServiceHttpRequest: ...
            def get(
                self,
                *,
                serviceName: str,
                configId: str,
                view: typing_extensions.Literal["BASIC", "FULL"] = ...,
                **kwargs: typing.Any
            ) -> ServiceHttpRequest: ...
            def list(
                self,
                *,
                serviceName: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> ListServiceConfigsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListServiceConfigsResponseHttpRequest,
                previous_response: ListServiceConfigsResponse,
            ) -> ListServiceConfigsResponseHttpRequest | None: ...
            def submit(
                self,
                *,
                serviceName: str,
                body: SubmitConfigSourceRequest = ...,
                **kwargs: typing.Any
            ) -> OperationHttpRequest: ...

        @typing.type_check_only
        class ConsumersResource(googleapiclient.discovery.Resource):
            def getIamPolicy(
                self,
                *,
                resource: str,
                body: GetIamPolicyRequest = ...,
                **kwargs: typing.Any
            ) -> PolicyHttpRequest: ...
            def setIamPolicy(
                self,
                *,
                resource: str,
                body: SetIamPolicyRequest = ...,
                **kwargs: typing.Any
            ) -> PolicyHttpRequest: ...
            def testIamPermissions(
                self,
                *,
                resource: str,
                body: TestIamPermissionsRequest = ...,
                **kwargs: typing.Any
            ) -> TestIamPermissionsResponseHttpRequest: ...

        @typing.type_check_only
        class RolloutsResource(googleapiclient.discovery.Resource):
            def create(
                self, *, serviceName: str, body: Rollout = ..., **kwargs: typing.Any
            ) -> OperationHttpRequest: ...
            def get(
                self, *, serviceName: str, rolloutId: str, **kwargs: typing.Any
            ) -> RolloutHttpRequest: ...
            def list(
                self,
                *,
                serviceName: str,
                filter: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> ListServiceRolloutsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListServiceRolloutsResponseHttpRequest,
                previous_response: ListServiceRolloutsResponse,
            ) -> ListServiceRolloutsResponseHttpRequest | None: ...

        def create(
            self, *, body: ManagedService = ..., **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def delete(
            self, *, serviceName: str, **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def generateConfigReport(
            self, *, body: GenerateConfigReportRequest = ..., **kwargs: typing.Any
        ) -> GenerateConfigReportResponseHttpRequest: ...
        def get(
            self, *, serviceName: str, **kwargs: typing.Any
        ) -> ManagedServiceHttpRequest: ...
        def getConfig(
            self,
            *,
            serviceName: str,
            configId: str = ...,
            view: typing_extensions.Literal["BASIC", "FULL"] = ...,
            **kwargs: typing.Any
        ) -> ServiceHttpRequest: ...
        def getIamPolicy(
            self,
            *,
            resource: str,
            body: GetIamPolicyRequest = ...,
            **kwargs: typing.Any
        ) -> PolicyHttpRequest: ...
        def list(
            self,
            *,
            consumerId: str = ...,
            pageSize: int = ...,
            pageToken: str = ...,
            producerProjectId: str = ...,
            **kwargs: typing.Any
        ) -> ListServicesResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: ListServicesResponseHttpRequest,
            previous_response: ListServicesResponse,
        ) -> ListServicesResponseHttpRequest | None: ...
        def setIamPolicy(
            self,
            *,
            resource: str,
            body: SetIamPolicyRequest = ...,
            **kwargs: typing.Any
        ) -> PolicyHttpRequest: ...
        def testIamPermissions(
            self,
            *,
            resource: str,
            body: TestIamPermissionsRequest = ...,
            **kwargs: typing.Any
        ) -> TestIamPermissionsResponseHttpRequest: ...
        def undelete(
            self, *, serviceName: str, **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def configs(self) -> ConfigsResource: ...
        def consumers(self) -> ConsumersResource: ...
        def rollouts(self) -> RolloutsResource: ...

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
    def services(self) -> ServicesResource: ...

@typing.type_check_only
class GenerateConfigReportResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GenerateConfigReportResponse: ...

@typing.type_check_only
class ListOperationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListOperationsResponse: ...

@typing.type_check_only
class ListServiceConfigsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListServiceConfigsResponse: ...

@typing.type_check_only
class ListServiceRolloutsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListServiceRolloutsResponse: ...

@typing.type_check_only
class ListServicesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListServicesResponse: ...

@typing.type_check_only
class ManagedServiceHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ManagedService: ...

@typing.type_check_only
class OperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Operation: ...

@typing.type_check_only
class PolicyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Policy: ...

@typing.type_check_only
class RolloutHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Rollout: ...

@typing.type_check_only
class ServiceHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Service: ...

@typing.type_check_only
class TestIamPermissionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> TestIamPermissionsResponse: ...
