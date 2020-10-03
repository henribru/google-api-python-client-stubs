import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class CloudIotResource(googleapiclient.discovery.Resource):
    class ProjectsResource(googleapiclient.discovery.Resource):
        class LocationsResource(googleapiclient.discovery.Resource):
            class RegistriesResource(googleapiclient.discovery.Resource):
                class GroupsResource(googleapiclient.discovery.Resource):
                    class DevicesResource(googleapiclient.discovery.Resource):
                        def list(
                            self,
                            *,
                            parent: str,
                            pageToken: str = ...,
                            deviceIds: typing.Union[str, typing.List[str]] = ...,
                            fieldMask: str = ...,
                            gatewayListOptions_associationsDeviceId: str = ...,
                            gatewayListOptions_gatewayType: typing_extensions.Literal[
                                "GATEWAY_TYPE_UNSPECIFIED", "GATEWAY", "NON_GATEWAY"
                            ] = ...,
                            pageSize: int = ...,
                            deviceNumIds: typing.Union[str, typing.List[str]] = ...,
                            gatewayListOptions_associationsGatewayId: str = ...,
                            **kwargs: typing.Any
                        ) -> ListDevicesResponseHttpRequest: ...
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
                    def getIamPolicy(
                        self,
                        *,
                        resource: str,
                        body: GetIamPolicyRequest = ...,
                        **kwargs: typing.Any
                    ) -> PolicyHttpRequest: ...
                    def devices(self) -> DevicesResource: ...
                class DevicesResource(googleapiclient.discovery.Resource):
                    class ConfigVersionsResource(googleapiclient.discovery.Resource):
                        def list(
                            self,
                            *,
                            name: str,
                            numVersions: int = ...,
                            **kwargs: typing.Any
                        ) -> ListDeviceConfigVersionsResponseHttpRequest: ...
                    class StatesResource(googleapiclient.discovery.Resource):
                        def list(
                            self,
                            *,
                            name: str,
                            numStates: int = ...,
                            **kwargs: typing.Any
                        ) -> ListDeviceStatesResponseHttpRequest: ...
                    def get(
                        self, *, name: str, fieldMask: str = ..., **kwargs: typing.Any
                    ) -> DeviceHttpRequest: ...
                    def create(
                        self, *, parent: str, body: Device = ..., **kwargs: typing.Any
                    ) -> DeviceHttpRequest: ...
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> EmptyHttpRequest: ...
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
                    def modifyCloudToDeviceConfig(
                        self,
                        *,
                        name: str,
                        body: ModifyCloudToDeviceConfigRequest = ...,
                        **kwargs: typing.Any
                    ) -> DeviceConfigHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        gatewayListOptions_associationsGatewayId: str = ...,
                        pageSize: int = ...,
                        deviceNumIds: typing.Union[str, typing.List[str]] = ...,
                        gatewayListOptions_gatewayType: typing_extensions.Literal[
                            "GATEWAY_TYPE_UNSPECIFIED", "GATEWAY", "NON_GATEWAY"
                        ] = ...,
                        deviceIds: typing.Union[str, typing.List[str]] = ...,
                        fieldMask: str = ...,
                        pageToken: str = ...,
                        gatewayListOptions_associationsDeviceId: str = ...,
                        **kwargs: typing.Any
                    ) -> ListDevicesResponseHttpRequest: ...
                    def configVersions(self) -> ConfigVersionsResource: ...
                    def states(self) -> StatesResource: ...
                def bindDeviceToGateway(
                    self,
                    *,
                    parent: str,
                    body: BindDeviceToGatewayRequest = ...,
                    **kwargs: typing.Any
                ) -> BindDeviceToGatewayResponseHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def create(
                    self,
                    *,
                    parent: str,
                    body: DeviceRegistry = ...,
                    **kwargs: typing.Any
                ) -> DeviceRegistryHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageToken: str = ...,
                    pageSize: int = ...,
                    **kwargs: typing.Any
                ) -> ListDeviceRegistriesResponseHttpRequest: ...
                def unbindDeviceFromGateway(
                    self,
                    *,
                    parent: str,
                    body: UnbindDeviceFromGatewayRequest = ...,
                    **kwargs: typing.Any
                ) -> UnbindDeviceFromGatewayResponseHttpRequest: ...
                def testIamPermissions(
                    self,
                    *,
                    resource: str,
                    body: TestIamPermissionsRequest = ...,
                    **kwargs: typing.Any
                ) -> TestIamPermissionsResponseHttpRequest: ...
                def getIamPolicy(
                    self,
                    *,
                    resource: str,
                    body: GetIamPolicyRequest = ...,
                    **kwargs: typing.Any
                ) -> PolicyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> DeviceRegistryHttpRequest: ...
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
                def groups(self) -> GroupsResource: ...
                def devices(self) -> DevicesResource: ...
            def registries(self) -> RegistriesResource: ...
        def locations(self) -> LocationsResource: ...
    def projects(self) -> ProjectsResource: ...

class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Empty: ...

class ListDeviceConfigVersionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListDeviceConfigVersionsResponse: ...

class SendCommandToDeviceResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> SendCommandToDeviceResponse: ...

class DeviceRegistryHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> DeviceRegistry: ...

class BindDeviceToGatewayResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> BindDeviceToGatewayResponse: ...

class TestIamPermissionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> TestIamPermissionsResponse: ...

class UnbindDeviceFromGatewayResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> UnbindDeviceFromGatewayResponse: ...

class PolicyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Policy: ...

class ListDeviceRegistriesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListDeviceRegistriesResponse: ...

class ListDevicesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListDevicesResponse: ...

class DeviceHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Device: ...

class DeviceConfigHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> DeviceConfig: ...

class ListDeviceStatesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListDeviceStatesResponse: ...
