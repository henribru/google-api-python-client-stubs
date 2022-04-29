import collections.abc
import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

_list = list

@typing.type_check_only
class CloudIotResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class ProjectsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class LocationsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class RegistriesResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class DevicesResource(googleapiclient.discovery.Resource):
                    @typing.type_check_only
                    class ConfigVersionsResource(googleapiclient.discovery.Resource):
                        def list(
                            self,
                            *,
                            name: str,
                            numVersions: int = ...,
                            **kwargs: typing.Any
                        ) -> ListDeviceConfigVersionsResponseHttpRequest: ...

                    @typing.type_check_only
                    class StatesResource(googleapiclient.discovery.Resource):
                        def list(
                            self,
                            *,
                            name: str,
                            numStates: int = ...,
                            **kwargs: typing.Any
                        ) -> ListDeviceStatesResponseHttpRequest: ...

                    def create(
                        self, *, parent: str, body: Device = ..., **kwargs: typing.Any
                    ) -> DeviceHttpRequest: ...
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> EmptyHttpRequest: ...
                    def get(
                        self, *, name: str, fieldMask: str = ..., **kwargs: typing.Any
                    ) -> DeviceHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        deviceIds: str | _list[str] = ...,
                        deviceNumIds: str | _list[str] = ...,
                        fieldMask: str = ...,
                        gatewayListOptions_associationsDeviceId: str = ...,
                        gatewayListOptions_associationsGatewayId: str = ...,
                        gatewayListOptions_gatewayType: typing_extensions.Literal[
                            "GATEWAY_TYPE_UNSPECIFIED", "GATEWAY", "NON_GATEWAY"
                        ] = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any
                    ) -> ListDevicesResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: ListDevicesResponseHttpRequest,
                        previous_response: ListDevicesResponse,
                    ) -> ListDevicesResponseHttpRequest | None: ...
                    def modifyCloudToDeviceConfig(
                        self,
                        *,
                        name: str,
                        body: ModifyCloudToDeviceConfigRequest = ...,
                        **kwargs: typing.Any
                    ) -> DeviceConfigHttpRequest: ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: Device = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any
                    ) -> DeviceHttpRequest: ...
                    def sendCommandToDevice(
                        self,
                        *,
                        name: str,
                        body: SendCommandToDeviceRequest = ...,
                        **kwargs: typing.Any
                    ) -> SendCommandToDeviceResponseHttpRequest: ...
                    def configVersions(self) -> ConfigVersionsResource: ...
                    def states(self) -> StatesResource: ...

                @typing.type_check_only
                class GroupsResource(googleapiclient.discovery.Resource):
                    @typing.type_check_only
                    class DevicesResource(googleapiclient.discovery.Resource):
                        def list(
                            self,
                            *,
                            parent: str,
                            deviceIds: str | _list[str] = ...,
                            deviceNumIds: str | _list[str] = ...,
                            fieldMask: str = ...,
                            gatewayListOptions_associationsDeviceId: str = ...,
                            gatewayListOptions_associationsGatewayId: str = ...,
                            gatewayListOptions_gatewayType: typing_extensions.Literal[
                                "GATEWAY_TYPE_UNSPECIFIED", "GATEWAY", "NON_GATEWAY"
                            ] = ...,
                            pageSize: int = ...,
                            pageToken: str = ...,
                            **kwargs: typing.Any
                        ) -> ListDevicesResponseHttpRequest: ...
                        def list_next(
                            self,
                            previous_request: ListDevicesResponseHttpRequest,
                            previous_response: ListDevicesResponse,
                        ) -> ListDevicesResponseHttpRequest | None: ...

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
                    def devices(self) -> DevicesResource: ...

                def bindDeviceToGateway(
                    self,
                    *,
                    parent: str,
                    body: BindDeviceToGatewayRequest = ...,
                    **kwargs: typing.Any
                ) -> BindDeviceToGatewayResponseHttpRequest: ...
                def create(
                    self,
                    *,
                    parent: str,
                    body: DeviceRegistry = ...,
                    **kwargs: typing.Any
                ) -> DeviceRegistryHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> DeviceRegistryHttpRequest: ...
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
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> ListDeviceRegistriesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListDeviceRegistriesResponseHttpRequest,
                    previous_response: ListDeviceRegistriesResponse,
                ) -> ListDeviceRegistriesResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: DeviceRegistry = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any
                ) -> DeviceRegistryHttpRequest: ...
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
                def unbindDeviceFromGateway(
                    self,
                    *,
                    parent: str,
                    body: UnbindDeviceFromGatewayRequest = ...,
                    **kwargs: typing.Any
                ) -> UnbindDeviceFromGatewayResponseHttpRequest: ...
                def devices(self) -> DevicesResource: ...
                def groups(self) -> GroupsResource: ...

            def registries(self) -> RegistriesResource: ...

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
class BindDeviceToGatewayResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> BindDeviceToGatewayResponse: ...

@typing.type_check_only
class DeviceHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Device: ...

@typing.type_check_only
class DeviceConfigHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> DeviceConfig: ...

@typing.type_check_only
class DeviceRegistryHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> DeviceRegistry: ...

@typing.type_check_only
class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Empty: ...

@typing.type_check_only
class ListDeviceConfigVersionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListDeviceConfigVersionsResponse: ...

@typing.type_check_only
class ListDeviceRegistriesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListDeviceRegistriesResponse: ...

@typing.type_check_only
class ListDeviceStatesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListDeviceStatesResponse: ...

@typing.type_check_only
class ListDevicesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListDevicesResponse: ...

@typing.type_check_only
class PolicyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Policy: ...

@typing.type_check_only
class SendCommandToDeviceResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> SendCommandToDeviceResponse: ...

@typing.type_check_only
class TestIamPermissionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> TestIamPermissionsResponse: ...

@typing.type_check_only
class UnbindDeviceFromGatewayResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> UnbindDeviceFromGatewayResponse: ...
