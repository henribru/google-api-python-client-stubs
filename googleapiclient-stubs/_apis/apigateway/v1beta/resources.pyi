import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class ApigatewayResource(googleapiclient.discovery.Resource):
    class ProjectsResource(googleapiclient.discovery.Resource):
        class LocationsResource(googleapiclient.discovery.Resource):
            class GatewaysResource(googleapiclient.discovery.Resource):
                def getIamPolicy(
                    self,
                    *,
                    resource: str,
                    options_requestedPolicyVersion: int = ...,
                    **kwargs: typing.Any
                ) -> ApigatewayPolicyHttpRequest: ...
                def create(
                    self,
                    *,
                    parent: str,
                    body: ApigatewayGateway = ...,
                    gatewayId: str = ...,
                    **kwargs: typing.Any
                ) -> ApigatewayOperationHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> ApigatewayOperationHttpRequest: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: ApigatewayGateway = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any
                ) -> ApigatewayOperationHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    filter: str = ...,
                    **kwargs: typing.Any
                ) -> ApigatewayListGatewaysResponseHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> ApigatewayGatewayHttpRequest: ...
                def testIamPermissions(
                    self,
                    *,
                    resource: str,
                    body: ApigatewayTestIamPermissionsRequest = ...,
                    **kwargs: typing.Any
                ) -> ApigatewayTestIamPermissionsResponseHttpRequest: ...
                def setIamPolicy(
                    self,
                    *,
                    resource: str,
                    body: ApigatewaySetIamPolicyRequest = ...,
                    **kwargs: typing.Any
                ) -> ApigatewayPolicyHttpRequest: ...
            class OperationsResource(googleapiclient.discovery.Resource):
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> ApigatewayOperationHttpRequest: ...
                def cancel(
                    self,
                    *,
                    name: str,
                    body: ApigatewayCancelOperationRequest = ...,
                    **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def list(
                    self,
                    *,
                    name: str,
                    filter: str = ...,
                    pageToken: str = ...,
                    pageSize: int = ...,
                    **kwargs: typing.Any
                ) -> ApigatewayListOperationsResponseHttpRequest: ...
            class ApisResource(googleapiclient.discovery.Resource):
                class ConfigsResource(googleapiclient.discovery.Resource):
                    def get(
                        self,
                        *,
                        name: str,
                        view: typing_extensions.Literal[
                            "CONFIG_VIEW_UNSPECIFIED", "BASIC", "FULL"
                        ] = ...,
                        **kwargs: typing.Any
                    ) -> ApigatewayApiConfigHttpRequest: ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: ApigatewayApiConfig = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any
                    ) -> ApigatewayOperationHttpRequest: ...
                    def testIamPermissions(
                        self,
                        *,
                        resource: str,
                        body: ApigatewayTestIamPermissionsRequest = ...,
                        **kwargs: typing.Any
                    ) -> ApigatewayTestIamPermissionsResponseHttpRequest: ...
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> ApigatewayOperationHttpRequest: ...
                    def getIamPolicy(
                        self,
                        *,
                        resource: str,
                        options_requestedPolicyVersion: int = ...,
                        **kwargs: typing.Any
                    ) -> ApigatewayPolicyHttpRequest: ...
                    def setIamPolicy(
                        self,
                        *,
                        resource: str,
                        body: ApigatewaySetIamPolicyRequest = ...,
                        **kwargs: typing.Any
                    ) -> ApigatewayPolicyHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        orderBy: str = ...,
                        pageToken: str = ...,
                        pageSize: int = ...,
                        filter: str = ...,
                        **kwargs: typing.Any
                    ) -> ApigatewayListApiConfigsResponseHttpRequest: ...
                    def create(
                        self,
                        *,
                        parent: str,
                        body: ApigatewayApiConfig = ...,
                        apiConfigId: str = ...,
                        **kwargs: typing.Any
                    ) -> ApigatewayOperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> ApigatewayApiHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> ApigatewayOperationHttpRequest: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: ApigatewayApi = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any
                ) -> ApigatewayOperationHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> ApigatewayListApisResponseHttpRequest: ...
                def getIamPolicy(
                    self,
                    *,
                    resource: str,
                    options_requestedPolicyVersion: int = ...,
                    **kwargs: typing.Any
                ) -> ApigatewayPolicyHttpRequest: ...
                def setIamPolicy(
                    self,
                    *,
                    resource: str,
                    body: ApigatewaySetIamPolicyRequest = ...,
                    **kwargs: typing.Any
                ) -> ApigatewayPolicyHttpRequest: ...
                def create(
                    self,
                    *,
                    parent: str,
                    body: ApigatewayApi = ...,
                    apiId: str = ...,
                    **kwargs: typing.Any
                ) -> ApigatewayOperationHttpRequest: ...
                def testIamPermissions(
                    self,
                    *,
                    resource: str,
                    body: ApigatewayTestIamPermissionsRequest = ...,
                    **kwargs: typing.Any
                ) -> ApigatewayTestIamPermissionsResponseHttpRequest: ...
                def configs(self) -> ConfigsResource: ...
            def list(
                self,
                *,
                name: str,
                pageToken: str = ...,
                pageSize: int = ...,
                filter: str = ...,
                **kwargs: typing.Any
            ) -> ApigatewayListLocationsResponseHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> ApigatewayLocationHttpRequest: ...
            def gateways(self) -> GatewaysResource: ...
            def operations(self) -> OperationsResource: ...
            def apis(self) -> ApisResource: ...
        def locations(self) -> LocationsResource: ...
    def projects(self) -> ProjectsResource: ...

class ApigatewayLocationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ApigatewayLocation: ...

class ApigatewayListGatewaysResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ApigatewayListGatewaysResponse: ...

class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Empty: ...

class ApigatewayListApiConfigsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ApigatewayListApiConfigsResponse: ...

class ApigatewayTestIamPermissionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ApigatewayTestIamPermissionsResponse: ...

class ApigatewayListApisResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ApigatewayListApisResponse: ...

class ApigatewayGatewayHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ApigatewayGateway: ...

class ApigatewayApiConfigHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ApigatewayApiConfig: ...

class ApigatewayPolicyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ApigatewayPolicy: ...

class ApigatewayListOperationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ApigatewayListOperationsResponse: ...

class ApigatewayOperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ApigatewayOperation: ...

class ApigatewayApiHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ApigatewayApi: ...

class ApigatewayListLocationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ApigatewayListLocationsResponse: ...
