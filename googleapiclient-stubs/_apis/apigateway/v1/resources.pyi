import collections.abc
import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

_list = list

@typing.type_check_only
class ApigatewayResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class ProjectsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class LocationsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class ApisResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class ConfigsResource(googleapiclient.discovery.Resource):
                    def create(
                        self,
                        *,
                        parent: str,
                        body: ApigatewayApiConfig = ...,
                        apiConfigId: str = ...,
                        **kwargs: typing.Any
                    ) -> ApigatewayOperationHttpRequest: ...
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> ApigatewayOperationHttpRequest: ...
                    def get(
                        self,
                        *,
                        name: str,
                        view: typing_extensions.Literal[
                            "CONFIG_VIEW_UNSPECIFIED", "BASIC", "FULL"
                        ] = ...,
                        **kwargs: typing.Any
                    ) -> ApigatewayApiConfigHttpRequest: ...
                    def getIamPolicy(
                        self,
                        *,
                        resource: str,
                        options_requestedPolicyVersion: int = ...,
                        **kwargs: typing.Any
                    ) -> ApigatewayPolicyHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str = ...,
                        orderBy: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any
                    ) -> ApigatewayListApiConfigsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: ApigatewayListApiConfigsResponseHttpRequest,
                        previous_response: ApigatewayListApiConfigsResponse,
                    ) -> ApigatewayListApiConfigsResponseHttpRequest | None: ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: ApigatewayApiConfig = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any
                    ) -> ApigatewayOperationHttpRequest: ...
                    def setIamPolicy(
                        self,
                        *,
                        resource: str,
                        body: ApigatewaySetIamPolicyRequest = ...,
                        **kwargs: typing.Any
                    ) -> ApigatewayPolicyHttpRequest: ...
                    def testIamPermissions(
                        self,
                        *,
                        resource: str,
                        body: ApigatewayTestIamPermissionsRequest = ...,
                        **kwargs: typing.Any
                    ) -> ApigatewayTestIamPermissionsResponseHttpRequest: ...

                def create(
                    self,
                    *,
                    parent: str,
                    body: ApigatewayApi = ...,
                    apiId: str = ...,
                    **kwargs: typing.Any
                ) -> ApigatewayOperationHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> ApigatewayOperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> ApigatewayApiHttpRequest: ...
                def getIamPolicy(
                    self,
                    *,
                    resource: str,
                    options_requestedPolicyVersion: int = ...,
                    **kwargs: typing.Any
                ) -> ApigatewayPolicyHttpRequest: ...
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
                def list_next(
                    self,
                    previous_request: ApigatewayListApisResponseHttpRequest,
                    previous_response: ApigatewayListApisResponse,
                ) -> ApigatewayListApisResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: ApigatewayApi = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any
                ) -> ApigatewayOperationHttpRequest: ...
                def setIamPolicy(
                    self,
                    *,
                    resource: str,
                    body: ApigatewaySetIamPolicyRequest = ...,
                    **kwargs: typing.Any
                ) -> ApigatewayPolicyHttpRequest: ...
                def testIamPermissions(
                    self,
                    *,
                    resource: str,
                    body: ApigatewayTestIamPermissionsRequest = ...,
                    **kwargs: typing.Any
                ) -> ApigatewayTestIamPermissionsResponseHttpRequest: ...
                def configs(self) -> ConfigsResource: ...

            @typing.type_check_only
            class GatewaysResource(googleapiclient.discovery.Resource):
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
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> ApigatewayGatewayHttpRequest: ...
                def getIamPolicy(
                    self,
                    *,
                    resource: str,
                    options_requestedPolicyVersion: int = ...,
                    **kwargs: typing.Any
                ) -> ApigatewayPolicyHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> ApigatewayListGatewaysResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ApigatewayListGatewaysResponseHttpRequest,
                    previous_response: ApigatewayListGatewaysResponse,
                ) -> ApigatewayListGatewaysResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: ApigatewayGateway = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any
                ) -> ApigatewayOperationHttpRequest: ...
                def setIamPolicy(
                    self,
                    *,
                    resource: str,
                    body: ApigatewaySetIamPolicyRequest = ...,
                    **kwargs: typing.Any
                ) -> ApigatewayPolicyHttpRequest: ...
                def testIamPermissions(
                    self,
                    *,
                    resource: str,
                    body: ApigatewayTestIamPermissionsRequest = ...,
                    **kwargs: typing.Any
                ) -> ApigatewayTestIamPermissionsResponseHttpRequest: ...

            @typing.type_check_only
            class OperationsResource(googleapiclient.discovery.Resource):
                def cancel(
                    self,
                    *,
                    name: str,
                    body: ApigatewayCancelOperationRequest = ...,
                    **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> ApigatewayOperationHttpRequest: ...
                def list(
                    self,
                    *,
                    name: str,
                    filter: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> ApigatewayListOperationsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ApigatewayListOperationsResponseHttpRequest,
                    previous_response: ApigatewayListOperationsResponse,
                ) -> ApigatewayListOperationsResponseHttpRequest | None: ...

            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> ApigatewayLocationHttpRequest: ...
            def list(
                self,
                *,
                name: str,
                filter: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> ApigatewayListLocationsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ApigatewayListLocationsResponseHttpRequest,
                previous_response: ApigatewayListLocationsResponse,
            ) -> ApigatewayListLocationsResponseHttpRequest | None: ...
            def apis(self) -> ApisResource: ...
            def gateways(self) -> GatewaysResource: ...
            def operations(self) -> OperationsResource: ...

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
        | None = ...,
    ) -> googleapiclient.http.BatchHttpRequest: ...
    def projects(self) -> ProjectsResource: ...

@typing.type_check_only
class ApigatewayApiHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ApigatewayApi: ...

@typing.type_check_only
class ApigatewayApiConfigHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ApigatewayApiConfig: ...

@typing.type_check_only
class ApigatewayGatewayHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ApigatewayGateway: ...

@typing.type_check_only
class ApigatewayListApiConfigsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ApigatewayListApiConfigsResponse: ...

@typing.type_check_only
class ApigatewayListApisResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ApigatewayListApisResponse: ...

@typing.type_check_only
class ApigatewayListGatewaysResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ApigatewayListGatewaysResponse: ...

@typing.type_check_only
class ApigatewayListLocationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ApigatewayListLocationsResponse: ...

@typing.type_check_only
class ApigatewayListOperationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ApigatewayListOperationsResponse: ...

@typing.type_check_only
class ApigatewayLocationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ApigatewayLocation: ...

@typing.type_check_only
class ApigatewayOperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ApigatewayOperation: ...

@typing.type_check_only
class ApigatewayPolicyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ApigatewayPolicy: ...

@typing.type_check_only
class ApigatewayTestIamPermissionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ApigatewayTestIamPermissionsResponse: ...

@typing.type_check_only
class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Empty: ...
