import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class SasportalResource(googleapiclient.discovery.Resource):
    class InstallerResource(googleapiclient.discovery.Resource):
        def generateSecret(
            self, *, body: SasPortalGenerateSecretRequest = ..., **kwargs: typing.Any
        ) -> SasPortalGenerateSecretResponseHttpRequest: ...
        def validate(
            self, *, body: SasPortalValidateInstallerRequest = ..., **kwargs: typing.Any
        ) -> SasPortalValidateInstallerResponseHttpRequest: ...
    class CustomersResource(googleapiclient.discovery.Resource):
        class NodesResource(googleapiclient.discovery.Resource):
            class NodesResource(googleapiclient.discovery.Resource):
                def list(
                    self,
                    *,
                    parent: str,
                    pageToken: str = ...,
                    pageSize: int = ...,
                    **kwargs: typing.Any
                ) -> SasPortalListNodesResponseHttpRequest: ...
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
                pageToken: str = ...,
                pageSize: int = ...,
                **kwargs: typing.Any
            ) -> SasPortalListNodesResponseHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> SasPortalNodeHttpRequest: ...
            def patch(
                self,
                *,
                name: str,
                body: SasPortalNode = ...,
                updateMask: str = ...,
                **kwargs: typing.Any
            ) -> SasPortalNodeHttpRequest: ...
            def move(
                self,
                *,
                name: str,
                body: SasPortalMoveNodeRequest = ...,
                **kwargs: typing.Any
            ) -> SasPortalOperationHttpRequest: ...
            def create(
                self, *, parent: str, body: SasPortalNode = ..., **kwargs: typing.Any
            ) -> SasPortalNodeHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> SasPortalEmptyHttpRequest: ...
            def nodes(self) -> NodesResource: ...
        class DevicesResource(googleapiclient.discovery.Resource):
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> SasPortalDeviceHttpRequest: ...
            def createSigned(
                self,
                *,
                parent: str,
                body: SasPortalCreateSignedDeviceRequest = ...,
                **kwargs: typing.Any
            ) -> SasPortalDeviceHttpRequest: ...
            def signDevice(
                self,
                *,
                name: str,
                body: SasPortalSignDeviceRequest = ...,
                **kwargs: typing.Any
            ) -> SasPortalEmptyHttpRequest: ...
            def create(
                self, *, parent: str, body: SasPortalDevice = ..., **kwargs: typing.Any
            ) -> SasPortalDeviceHttpRequest: ...
            def patch(
                self,
                *,
                name: str,
                body: SasPortalDevice = ...,
                updateMask: str = ...,
                **kwargs: typing.Any
            ) -> SasPortalDeviceHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageToken: str = ...,
                pageSize: int = ...,
                filter: str = ...,
                **kwargs: typing.Any
            ) -> SasPortalListDevicesResponseHttpRequest: ...
            def updateSigned(
                self,
                *,
                name: str,
                body: SasPortalUpdateSignedDeviceRequest = ...,
                **kwargs: typing.Any
            ) -> SasPortalDeviceHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> SasPortalEmptyHttpRequest: ...
            def move(
                self,
                *,
                name: str,
                body: SasPortalMoveDeviceRequest = ...,
                **kwargs: typing.Any
            ) -> SasPortalOperationHttpRequest: ...
            def bulk(
                self,
                *,
                parent: str,
                body: SasPortalBulkCreateDeviceRequest = ...,
                **kwargs: typing.Any
            ) -> SasPortalBulkCreateDeviceResponseHttpRequest: ...
        class DeploymentsResource(googleapiclient.discovery.Resource):
            class DevicesResource(googleapiclient.discovery.Resource):
                def list(
                    self,
                    *,
                    parent: str,
                    pageToken: str = ...,
                    pageSize: int = ...,
                    filter: str = ...,
                    **kwargs: typing.Any
                ) -> SasPortalListDevicesResponseHttpRequest: ...
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
            def move(
                self,
                *,
                name: str,
                body: SasPortalMoveDeploymentRequest = ...,
                **kwargs: typing.Any
            ) -> SasPortalOperationHttpRequest: ...
            def devices(self) -> DevicesResource: ...
        def list(
            self, *, pageSize: int = ..., pageToken: str = ..., **kwargs: typing.Any
        ) -> SasPortalListCustomersResponseHttpRequest: ...
        def get(
            self, *, name: str, **kwargs: typing.Any
        ) -> SasPortalCustomerHttpRequest: ...
        def patch(
            self,
            *,
            name: str,
            body: SasPortalCustomer = ...,
            updateMask: str = ...,
            **kwargs: typing.Any
        ) -> SasPortalCustomerHttpRequest: ...
        def nodes(self) -> NodesResource: ...
        def devices(self) -> DevicesResource: ...
        def deployments(self) -> DeploymentsResource: ...
    class PoliciesResource(googleapiclient.discovery.Resource):
        def get(
            self, *, body: SasPortalGetPolicyRequest = ..., **kwargs: typing.Any
        ) -> SasPortalPolicyHttpRequest: ...
        def test(
            self, *, body: SasPortalTestPermissionsRequest = ..., **kwargs: typing.Any
        ) -> SasPortalTestPermissionsResponseHttpRequest: ...
        def set(
            self, *, body: SasPortalSetPolicyRequest = ..., **kwargs: typing.Any
        ) -> SasPortalPolicyHttpRequest: ...
    class NodesResource(googleapiclient.discovery.Resource):
        class DevicesResource(googleapiclient.discovery.Resource):
            def create(
                self, *, parent: str, body: SasPortalDevice = ..., **kwargs: typing.Any
            ) -> SasPortalDeviceHttpRequest: ...
            def updateSigned(
                self,
                *,
                name: str,
                body: SasPortalUpdateSignedDeviceRequest = ...,
                **kwargs: typing.Any
            ) -> SasPortalDeviceHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> SasPortalEmptyHttpRequest: ...
            def patch(
                self,
                *,
                name: str,
                body: SasPortalDevice = ...,
                updateMask: str = ...,
                **kwargs: typing.Any
            ) -> SasPortalDeviceHttpRequest: ...
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
            def createSigned(
                self,
                *,
                parent: str,
                body: SasPortalCreateSignedDeviceRequest = ...,
                **kwargs: typing.Any
            ) -> SasPortalDeviceHttpRequest: ...
            def bulk(
                self,
                *,
                parent: str,
                body: SasPortalBulkCreateDeviceRequest = ...,
                **kwargs: typing.Any
            ) -> SasPortalBulkCreateDeviceResponseHttpRequest: ...
            def signDevice(
                self,
                *,
                name: str,
                body: SasPortalSignDeviceRequest = ...,
                **kwargs: typing.Any
            ) -> SasPortalEmptyHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                filter: str = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> SasPortalListDevicesResponseHttpRequest: ...
        class NodesResource(googleapiclient.discovery.Resource):
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
                def list(
                    self,
                    *,
                    parent: str,
                    pageToken: str = ...,
                    filter: str = ...,
                    pageSize: int = ...,
                    **kwargs: typing.Any
                ) -> SasPortalListDevicesResponseHttpRequest: ...
                def createSigned(
                    self,
                    *,
                    parent: str,
                    body: SasPortalCreateSignedDeviceRequest = ...,
                    **kwargs: typing.Any
                ) -> SasPortalDeviceHttpRequest: ...
            class NodesResource(googleapiclient.discovery.Resource):
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> SasPortalListNodesResponseHttpRequest: ...
                def create(
                    self,
                    *,
                    parent: str,
                    body: SasPortalNode = ...,
                    **kwargs: typing.Any
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
            def create(
                self, *, parent: str, body: SasPortalNode = ..., **kwargs: typing.Any
            ) -> SasPortalNodeHttpRequest: ...
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
        class DeploymentsResource(googleapiclient.discovery.Resource):
            class DevicesResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: SasPortalDevice = ...,
                    **kwargs: typing.Any
                ) -> SasPortalDeviceHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageToken: str = ...,
                    filter: str = ...,
                    pageSize: int = ...,
                    **kwargs: typing.Any
                ) -> SasPortalListDevicesResponseHttpRequest: ...
                def createSigned(
                    self,
                    *,
                    parent: str,
                    body: SasPortalCreateSignedDeviceRequest = ...,
                    **kwargs: typing.Any
                ) -> SasPortalDeviceHttpRequest: ...
            def move(
                self,
                *,
                name: str,
                body: SasPortalMoveDeploymentRequest = ...,
                **kwargs: typing.Any
            ) -> SasPortalOperationHttpRequest: ...
            def devices(self) -> DevicesResource: ...
        def get(
            self, *, name: str, **kwargs: typing.Any
        ) -> SasPortalNodeHttpRequest: ...
        def devices(self) -> DevicesResource: ...
        def nodes(self) -> NodesResource: ...
        def deployments(self) -> DeploymentsResource: ...
    class DeploymentsResource(googleapiclient.discovery.Resource):
        class DevicesResource(googleapiclient.discovery.Resource):
            def move(
                self,
                *,
                name: str,
                body: SasPortalMoveDeviceRequest = ...,
                **kwargs: typing.Any
            ) -> SasPortalOperationHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> SasPortalEmptyHttpRequest: ...
            def patch(
                self,
                *,
                name: str,
                body: SasPortalDevice = ...,
                updateMask: str = ...,
                **kwargs: typing.Any
            ) -> SasPortalDeviceHttpRequest: ...
            def updateSigned(
                self,
                *,
                name: str,
                body: SasPortalUpdateSignedDeviceRequest = ...,
                **kwargs: typing.Any
            ) -> SasPortalDeviceHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> SasPortalDeviceHttpRequest: ...
            def signDevice(
                self,
                *,
                name: str,
                body: SasPortalSignDeviceRequest = ...,
                **kwargs: typing.Any
            ) -> SasPortalEmptyHttpRequest: ...
        def devices(self) -> DevicesResource: ...
    def installer(self) -> InstallerResource: ...
    def customers(self) -> CustomersResource: ...
    def policies(self) -> PoliciesResource: ...
    def nodes(self) -> NodesResource: ...
    def deployments(self) -> DeploymentsResource: ...

class SasPortalListCustomersResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> SasPortalListCustomersResponse: ...

class SasPortalOperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> SasPortalOperation: ...

class SasPortalListDevicesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> SasPortalListDevicesResponse: ...

class SasPortalEmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> SasPortalEmpty: ...

class SasPortalListNodesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> SasPortalListNodesResponse: ...

class SasPortalBulkCreateDeviceResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> SasPortalBulkCreateDeviceResponse: ...

class SasPortalValidateInstallerResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> SasPortalValidateInstallerResponse: ...

class SasPortalDeviceHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> SasPortalDevice: ...

class SasPortalGenerateSecretResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> SasPortalGenerateSecretResponse: ...

class SasPortalCustomerHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> SasPortalCustomer: ...

class SasPortalNodeHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> SasPortalNode: ...

class SasPortalTestPermissionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> SasPortalTestPermissionsResponse: ...

class SasPortalPolicyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> SasPortalPolicy: ...
