import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class ServiceManagementResource(googleapiclient.discovery.Resource):
    class OperationsResource(googleapiclient.discovery.Resource):
        def get(self, *, name: str, **kwargs: typing.Any) -> OperationHttpRequest: ...
        def list(
            self,
            *,
            filter: str = ...,
            pageSize: int = ...,
            pageToken: str = ...,
            name: str = ...,
            **kwargs: typing.Any
        ) -> ListOperationsResponseHttpRequest: ...
    class ServicesResource(googleapiclient.discovery.Resource):
        class ConfigsResource(googleapiclient.discovery.Resource):
            def create(
                self, *, serviceName: str, body: Service = ..., **kwargs: typing.Any
            ) -> ServiceHttpRequest: ...
            def submit(
                self,
                *,
                serviceName: str,
                body: SubmitConfigSourceRequest = ...,
                **kwargs: typing.Any
            ) -> OperationHttpRequest: ...
            def list(
                self,
                *,
                serviceName: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> ListServiceConfigsResponseHttpRequest: ...
            def get(
                self,
                *,
                serviceName: str,
                configId: str,
                view: typing_extensions.Literal["BASIC", "FULL"] = ...,
                **kwargs: typing.Any
            ) -> ServiceHttpRequest: ...
        class ConsumersResource(googleapiclient.discovery.Resource):
            def getIamPolicy(
                self,
                *,
                resource: str,
                body: GetIamPolicyRequest = ...,
                **kwargs: typing.Any
            ) -> PolicyHttpRequest: ...
            def testIamPermissions(
                self,
                *,
                resource: str,
                body: TestIamPermissionsRequest = ...,
                **kwargs: typing.Any
            ) -> TestIamPermissionsResponseHttpRequest: ...
            def setIamPolicy(
                self,
                *,
                resource: str,
                body: SetIamPolicyRequest = ...,
                **kwargs: typing.Any
            ) -> PolicyHttpRequest: ...
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
        def create(
            self, *, body: ManagedService = ..., **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def delete(
            self, *, serviceName: str, **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def get(
            self, *, serviceName: str, **kwargs: typing.Any
        ) -> ManagedServiceHttpRequest: ...
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
        def enable(
            self,
            *,
            serviceName: str,
            body: EnableServiceRequest = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def setIamPolicy(
            self,
            *,
            resource: str,
            body: SetIamPolicyRequest = ...,
            **kwargs: typing.Any
        ) -> PolicyHttpRequest: ...
        def getConfig(
            self,
            *,
            serviceName: str,
            view: typing_extensions.Literal["BASIC", "FULL"] = ...,
            configId: str = ...,
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
            producerProjectId: str = ...,
            consumerId: str = ...,
            pageToken: str = ...,
            pageSize: int = ...,
            **kwargs: typing.Any
        ) -> ListServicesResponseHttpRequest: ...
        def generateConfigReport(
            self, *, body: GenerateConfigReportRequest = ..., **kwargs: typing.Any
        ) -> GenerateConfigReportResponseHttpRequest: ...
        def configs(self) -> ConfigsResource: ...
        def consumers(self) -> ConsumersResource: ...
        def rollouts(self) -> RolloutsResource: ...
    def operations(self) -> OperationsResource: ...
    def services(self) -> ServicesResource: ...

class ListServicesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListServicesResponse: ...

class GenerateConfigReportResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GenerateConfigReportResponse: ...

class ListOperationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListOperationsResponse: ...

class ListServiceRolloutsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListServiceRolloutsResponse: ...

class ManagedServiceHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ManagedService: ...

class TestIamPermissionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> TestIamPermissionsResponse: ...

class RolloutHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Rollout: ...

class ListServiceConfigsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListServiceConfigsResponse: ...

class PolicyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Policy: ...

class OperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Operation: ...

class ServiceHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Service: ...
