import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *
@typing.type_check_only
class SASPortalTestingResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class CustomersResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class DeploymentsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class DevicesResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: SasPortalDevice = ...,
                    **kwargs: typing.Any
                ) -> SasPortalDeviceHttpRequest: ...
                def createSigned(
                    self,
                    *,
                    parent: str,
                    body: SasPortalCreateSignedDeviceRequest = ...,
                    **kwargs: typing.Any
                ) -> SasPortalDeviceHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> SasPortalListDevicesResponseHttpRequest: ...
            def move(
                self,
                *,
                name: str,
                body: SasPortalMoveDeploymentRequest = ...,
                **kwargs: typing.Any
            ) -> SasPortalOperationHttpRequest: ...
            def devices(self) -> DevicesResource: ...
        @typing.type_check_only
        class DevicesResource(googleapiclient.discovery.Resource):
            def bulk(
                self,
                *,
                parent: str,
                body: SasPortalBulkCreateDeviceRequest = ...,
                **kwargs: typing.Any
            ) -> SasPortalBulkCreateDeviceResponseHttpRequest: ...
            def create(
                self, *, parent: str, body: SasPortalDevice = ..., **kwargs: typing.Any
            ) -> SasPortalDeviceHttpRequest: ...
            def createSigned(
                self,
                *,
                parent: str,
                body: SasPortalCreateSignedDeviceRequest = ...,
                **kwargs: typing.Any
            ) -> SasPortalDeviceHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> SasPortalEmptyHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> SasPortalDeviceHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                filter: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> SasPortalListDevicesResponseHttpRequest: ...
            def move(
                self,
                *,
                name: str,
                body: SasPortalMoveDeviceRequest = ...,
                **kwargs: typing.Any
            ) -> SasPortalOperationHttpRequest: ...
            def patch(
                self,
                *,
                name: str,
                body: SasPortalDevice = ...,
                updateMask: str = ...,
                **kwargs: typing.Any
            ) -> SasPortalDeviceHttpRequest: ...
            def signDevice(
                self,
                *,
                name: str,
                body: SasPortalSignDeviceRequest = ...,
                **kwargs: typing.Any
            ) -> SasPortalEmptyHttpRequest: ...
            def updateSigned(
                self,
                *,
                name: str,
                body: SasPortalUpdateSignedDeviceRequest = ...,
                **kwargs: typing.Any
            ) -> SasPortalDeviceHttpRequest: ...
        @typing.type_check_only
        class NodesResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class DevicesResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: SasPortalDevice = ...,
                    **kwargs: typing.Any
                ) -> SasPortalDeviceHttpRequest: ...
                def createSigned(
                    self,
                    *,
                    parent: str,
                    body: SasPortalCreateSignedDeviceRequest = ...,
                    **kwargs: typing.Any
                ) -> SasPortalDeviceHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> SasPortalListDevicesResponseHttpRequest: ...
            @typing.type_check_only
            class NodesResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: SasPortalNode = ...,
                    **kwargs: typing.Any
                ) -> SasPortalNodeHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> SasPortalListNodesResponseHttpRequest: ...
            def create(
                self, *, parent: str, body: SasPortalNode = ..., **kwargs: typing.Any
            ) -> SasPortalNodeHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> SasPortalEmptyHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> SasPortalNodeHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> SasPortalListNodesResponseHttpRequest: ...
            def move(
                self,
                *,
                name: str,
                body: SasPortalMoveNodeRequest = ...,
                **kwargs: typing.Any
            ) -> SasPortalOperationHttpRequest: ...
            def patch(
                self,
                *,
                name: str,
                body: SasPortalNode = ...,
                updateMask: str = ...,
                **kwargs: typing.Any
            ) -> SasPortalNodeHttpRequest: ...
            def devices(self) -> DevicesResource: ...
            def nodes(self) -> NodesResource: ...
        def get(
            self, *, name: str, **kwargs: typing.Any
        ) -> SasPortalCustomerHttpRequest: ...
        def list(
            self, *, pageSize: int = ..., pageToken: str = ..., **kwargs: typing.Any
        ) -> SasPortalListCustomersResponseHttpRequest: ...
        def patch(
            self,
            *,
            name: str,
            body: SasPortalCustomer = ...,
            updateMask: str = ...,
            **kwargs: typing.Any
        ) -> SasPortalCustomerHttpRequest: ...
        def deployments(self) -> DeploymentsResource: ...
        def devices(self) -> DevicesResource: ...
        def nodes(self) -> NodesResource: ...
    @typing.type_check_only
    class DeploymentsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class DevicesResource(googleapiclient.discovery.Resource):
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> SasPortalEmptyHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> SasPortalDeviceHttpRequest: ...
            def move(
                self,
                *,
                name: str,
                body: SasPortalMoveDeviceRequest = ...,
                **kwargs: typing.Any
            ) -> SasPortalOperationHttpRequest: ...
            def patch(
                self,
                *,
                name: str,
                body: SasPortalDevice = ...,
                updateMask: str = ...,
                **kwargs: typing.Any
            ) -> SasPortalDeviceHttpRequest: ...
            def signDevice(
                self,
                *,
                name: str,
                body: SasPortalSignDeviceRequest = ...,
                **kwargs: typing.Any
            ) -> SasPortalEmptyHttpRequest: ...
            def updateSigned(
                self,
                *,
                name: str,
                body: SasPortalUpdateSignedDeviceRequest = ...,
                **kwargs: typing.Any
            ) -> SasPortalDeviceHttpRequest: ...
        def devices(self) -> DevicesResource: ...
    @typing.type_check_only
    class InstallerResource(googleapiclient.discovery.Resource):
        def generateSecret(
            self, *, body: SasPortalGenerateSecretRequest = ..., **kwargs: typing.Any
        ) -> SasPortalGenerateSecretResponseHttpRequest: ...
        def validate(
            self, *, body: SasPortalValidateInstallerRequest = ..., **kwargs: typing.Any
        ) -> SasPortalValidateInstallerResponseHttpRequest: ...
    @typing.type_check_only
    class NodesResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class DeploymentsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class DevicesResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: SasPortalDevice = ...,
                    **kwargs: typing.Any
                ) -> SasPortalDeviceHttpRequest: ...
                def createSigned(
                    self,
                    *,
                    parent: str,
                    body: SasPortalCreateSignedDeviceRequest = ...,
                    **kwargs: typing.Any
                ) -> SasPortalDeviceHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> SasPortalListDevicesResponseHttpRequest: ...
            def move(
                self,
                *,
                name: str,
                body: SasPortalMoveDeploymentRequest = ...,
                **kwargs: typing.Any
            ) -> SasPortalOperationHttpRequest: ...
            def devices(self) -> DevicesResource: ...
        @typing.type_check_only
        class DevicesResource(googleapiclient.discovery.Resource):
            def bulk(
                self,
                *,
                parent: str,
                body: SasPortalBulkCreateDeviceRequest = ...,
                **kwargs: typing.Any
            ) -> SasPortalBulkCreateDeviceResponseHttpRequest: ...
            def create(
                self, *, parent: str, body: SasPortalDevice = ..., **kwargs: typing.Any
            ) -> SasPortalDeviceHttpRequest: ...
            def createSigned(
                self,
                *,
                parent: str,
                body: SasPortalCreateSignedDeviceRequest = ...,
                **kwargs: typing.Any
            ) -> SasPortalDeviceHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> SasPortalEmptyHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> SasPortalDeviceHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                filter: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> SasPortalListDevicesResponseHttpRequest: ...
            def move(
                self,
                *,
                name: str,
                body: SasPortalMoveDeviceRequest = ...,
                **kwargs: typing.Any
            ) -> SasPortalOperationHttpRequest: ...
            def patch(
                self,
                *,
                name: str,
                body: SasPortalDevice = ...,
                updateMask: str = ...,
                **kwargs: typing.Any
            ) -> SasPortalDeviceHttpRequest: ...
            def signDevice(
                self,
                *,
                name: str,
                body: SasPortalSignDeviceRequest = ...,
                **kwargs: typing.Any
            ) -> SasPortalEmptyHttpRequest: ...
            def updateSigned(
                self,
                *,
                name: str,
                body: SasPortalUpdateSignedDeviceRequest = ...,
                **kwargs: typing.Any
            ) -> SasPortalDeviceHttpRequest: ...
        @typing.type_check_only
        class NodesResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class DevicesResource(googleapiclient.discovery.Resource):
                def bulk(
                    self,
                    *,
                    parent: str,
                    body: SasPortalBulkCreateDeviceRequest = ...,
                    **kwargs: typing.Any
                ) -> SasPortalBulkCreateDeviceResponseHttpRequest: ...
                def create(
                    self,
                    *,
                    parent: str,
                    body: SasPortalDevice = ...,
                    **kwargs: typing.Any
                ) -> SasPortalDeviceHttpRequest: ...
                def createSigned(
                    self,
                    *,
                    parent: str,
                    body: SasPortalCreateSignedDeviceRequest = ...,
                    **kwargs: typing.Any
                ) -> SasPortalDeviceHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> SasPortalListDevicesResponseHttpRequest: ...
            @typing.type_check_only
            class NodesResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: SasPortalNode = ...,
                    **kwargs: typing.Any
                ) -> SasPortalNodeHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> SasPortalListNodesResponseHttpRequest: ...
            def create(
                self, *, parent: str, body: SasPortalNode = ..., **kwargs: typing.Any
            ) -> SasPortalNodeHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> SasPortalEmptyHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> SasPortalNodeHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> SasPortalListNodesResponseHttpRequest: ...
            def move(
                self,
                *,
                name: str,
                body: SasPortalMoveNodeRequest = ...,
                **kwargs: typing.Any
            ) -> SasPortalOperationHttpRequest: ...
            def patch(
                self,
                *,
                name: str,
                body: SasPortalNode = ...,
                updateMask: str = ...,
                **kwargs: typing.Any
            ) -> SasPortalNodeHttpRequest: ...
            def devices(self) -> DevicesResource: ...
            def nodes(self) -> NodesResource: ...
        def get(
            self, *, name: str, **kwargs: typing.Any
        ) -> SasPortalNodeHttpRequest: ...
        def deployments(self) -> DeploymentsResource: ...
        def devices(self) -> DevicesResource: ...
        def nodes(self) -> NodesResource: ...
    @typing.type_check_only
    class PoliciesResource(googleapiclient.discovery.Resource):
        def get(
            self, *, body: SasPortalGetPolicyRequest = ..., **kwargs: typing.Any
        ) -> SasPortalPolicyHttpRequest: ...
        def set(
            self, *, body: SasPortalSetPolicyRequest = ..., **kwargs: typing.Any
        ) -> SasPortalPolicyHttpRequest: ...
        def test(
            self, *, body: SasPortalTestPermissionsRequest = ..., **kwargs: typing.Any
        ) -> SasPortalTestPermissionsResponseHttpRequest: ...
    def customers(self) -> CustomersResource: ...
    def deployments(self) -> DeploymentsResource: ...
    def installer(self) -> InstallerResource: ...
    def nodes(self) -> NodesResource: ...
    def policies(self) -> PoliciesResource: ...

@typing.type_check_only
class SasPortalBulkCreateDeviceResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> SasPortalBulkCreateDeviceResponse: ...

@typing.type_check_only
class SasPortalCustomerHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> SasPortalCustomer: ...

@typing.type_check_only
class SasPortalDeviceHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> SasPortalDevice: ...

@typing.type_check_only
class SasPortalEmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> SasPortalEmpty: ...

@typing.type_check_only
class SasPortalGenerateSecretResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> SasPortalGenerateSecretResponse: ...

@typing.type_check_only
class SasPortalListCustomersResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> SasPortalListCustomersResponse: ...

@typing.type_check_only
class SasPortalListDevicesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> SasPortalListDevicesResponse: ...

@typing.type_check_only
class SasPortalListNodesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> SasPortalListNodesResponse: ...

@typing.type_check_only
class SasPortalNodeHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> SasPortalNode: ...

@typing.type_check_only
class SasPortalOperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> SasPortalOperation: ...

@typing.type_check_only
class SasPortalPolicyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> SasPortalPolicy: ...

@typing.type_check_only
class SasPortalTestPermissionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> SasPortalTestPermissionsResponse: ...

@typing.type_check_only
class SasPortalValidateInstallerResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> SasPortalValidateInstallerResponse: ...
