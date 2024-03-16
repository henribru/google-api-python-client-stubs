import collections.abc
import typing

import httplib2
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http

from .schemas import *

_list = list

@typing.type_check_only
class SasportalResource(googleapiclient.discovery.Resource):
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
                    **kwargs: typing.Any,
                ) -> SasPortalDeviceHttpRequest: ...
                def createSigned(
                    self,
                    *,
                    parent: str,
                    body: SasPortalCreateSignedDeviceRequest = ...,
                    **kwargs: typing.Any,
                ) -> SasPortalDeviceHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> SasPortalListDevicesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: SasPortalListDevicesResponseHttpRequest,
                    previous_response: SasPortalListDevicesResponse,
                ) -> SasPortalListDevicesResponseHttpRequest | None: ...

            def create(
                self,
                *,
                parent: str,
                body: SasPortalDeployment = ...,
                **kwargs: typing.Any,
            ) -> SasPortalDeploymentHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> SasPortalEmptyHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> SasPortalDeploymentHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                filter: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any,
            ) -> SasPortalListDeploymentsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: SasPortalListDeploymentsResponseHttpRequest,
                previous_response: SasPortalListDeploymentsResponse,
            ) -> SasPortalListDeploymentsResponseHttpRequest | None: ...
            def move(
                self,
                *,
                name: str,
                body: SasPortalMoveDeploymentRequest = ...,
                **kwargs: typing.Any,
            ) -> SasPortalOperationHttpRequest: ...
            def patch(
                self,
                *,
                name: str,
                body: SasPortalDeployment = ...,
                updateMask: str = ...,
                **kwargs: typing.Any,
            ) -> SasPortalDeploymentHttpRequest: ...
            def devices(self) -> DevicesResource: ...

        @typing.type_check_only
        class DevicesResource(googleapiclient.discovery.Resource):
            def create(
                self, *, parent: str, body: SasPortalDevice = ..., **kwargs: typing.Any
            ) -> SasPortalDeviceHttpRequest: ...
            def createSigned(
                self,
                *,
                parent: str,
                body: SasPortalCreateSignedDeviceRequest = ...,
                **kwargs: typing.Any,
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
                **kwargs: typing.Any,
            ) -> SasPortalListDevicesResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: SasPortalListDevicesResponseHttpRequest,
                previous_response: SasPortalListDevicesResponse,
            ) -> SasPortalListDevicesResponseHttpRequest | None: ...
            def move(
                self,
                *,
                name: str,
                body: SasPortalMoveDeviceRequest = ...,
                **kwargs: typing.Any,
            ) -> SasPortalOperationHttpRequest: ...
            def patch(
                self,
                *,
                name: str,
                body: SasPortalDevice = ...,
                updateMask: str = ...,
                **kwargs: typing.Any,
            ) -> SasPortalDeviceHttpRequest: ...
            def signDevice(
                self,
                *,
                name: str,
                body: SasPortalSignDeviceRequest = ...,
                **kwargs: typing.Any,
            ) -> SasPortalEmptyHttpRequest: ...
            def updateSigned(
                self,
                *,
                name: str,
                body: SasPortalUpdateSignedDeviceRequest = ...,
                **kwargs: typing.Any,
            ) -> SasPortalDeviceHttpRequest: ...

        @typing.type_check_only
        class NodesResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class DeploymentsResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: SasPortalDeployment = ...,
                    **kwargs: typing.Any,
                ) -> SasPortalDeploymentHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> SasPortalListDeploymentsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: SasPortalListDeploymentsResponseHttpRequest,
                    previous_response: SasPortalListDeploymentsResponse,
                ) -> SasPortalListDeploymentsResponseHttpRequest | None: ...

            @typing.type_check_only
            class DevicesResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: SasPortalDevice = ...,
                    **kwargs: typing.Any,
                ) -> SasPortalDeviceHttpRequest: ...
                def createSigned(
                    self,
                    *,
                    parent: str,
                    body: SasPortalCreateSignedDeviceRequest = ...,
                    **kwargs: typing.Any,
                ) -> SasPortalDeviceHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> SasPortalListDevicesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: SasPortalListDevicesResponseHttpRequest,
                    previous_response: SasPortalListDevicesResponse,
                ) -> SasPortalListDevicesResponseHttpRequest | None: ...

            @typing.type_check_only
            class NodesResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: SasPortalNode = ...,
                    **kwargs: typing.Any,
                ) -> SasPortalNodeHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> SasPortalListNodesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: SasPortalListNodesResponseHttpRequest,
                    previous_response: SasPortalListNodesResponse,
                ) -> SasPortalListNodesResponseHttpRequest | None: ...

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
                filter: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any,
            ) -> SasPortalListNodesResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: SasPortalListNodesResponseHttpRequest,
                previous_response: SasPortalListNodesResponse,
            ) -> SasPortalListNodesResponseHttpRequest | None: ...
            def move(
                self,
                *,
                name: str,
                body: SasPortalMoveNodeRequest = ...,
                **kwargs: typing.Any,
            ) -> SasPortalOperationHttpRequest: ...
            def patch(
                self,
                *,
                name: str,
                body: SasPortalNode = ...,
                updateMask: str = ...,
                **kwargs: typing.Any,
            ) -> SasPortalNodeHttpRequest: ...
            def deployments(self) -> DeploymentsResource: ...
            def devices(self) -> DevicesResource: ...
            def nodes(self) -> NodesResource: ...

        def get(
            self, *, name: str, **kwargs: typing.Any
        ) -> SasPortalCustomerHttpRequest: ...
        def list(
            self, *, pageSize: int = ..., pageToken: str = ..., **kwargs: typing.Any
        ) -> SasPortalListCustomersResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: SasPortalListCustomersResponseHttpRequest,
            previous_response: SasPortalListCustomersResponse,
        ) -> SasPortalListCustomersResponseHttpRequest | None: ...
        def listGcpProjectDeployments(
            self, **kwargs: typing.Any
        ) -> SasPortalListGcpProjectDeploymentsResponseHttpRequest: ...
        def listLegacyOrganizations(
            self, **kwargs: typing.Any
        ) -> SasPortalListLegacyOrganizationsResponseHttpRequest: ...
        def migrateOrganization(
            self,
            *,
            body: SasPortalMigrateOrganizationRequest = ...,
            **kwargs: typing.Any,
        ) -> SasPortalOperationHttpRequest: ...
        def patch(
            self,
            *,
            name: str,
            body: SasPortalCustomer = ...,
            updateMask: str = ...,
            **kwargs: typing.Any,
        ) -> SasPortalCustomerHttpRequest: ...
        def provisionDeployment(
            self,
            *,
            body: SasPortalProvisionDeploymentRequest = ...,
            **kwargs: typing.Any,
        ) -> SasPortalProvisionDeploymentResponseHttpRequest: ...
        def setupSasAnalytics(
            self, *, body: SasPortalSetupSasAnalyticsRequest = ..., **kwargs: typing.Any
        ) -> SasPortalOperationHttpRequest: ...
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
                **kwargs: typing.Any,
            ) -> SasPortalOperationHttpRequest: ...
            def patch(
                self,
                *,
                name: str,
                body: SasPortalDevice = ...,
                updateMask: str = ...,
                **kwargs: typing.Any,
            ) -> SasPortalDeviceHttpRequest: ...
            def signDevice(
                self,
                *,
                name: str,
                body: SasPortalSignDeviceRequest = ...,
                **kwargs: typing.Any,
            ) -> SasPortalEmptyHttpRequest: ...
            def updateSigned(
                self,
                *,
                name: str,
                body: SasPortalUpdateSignedDeviceRequest = ...,
                **kwargs: typing.Any,
            ) -> SasPortalDeviceHttpRequest: ...

        def get(
            self, *, name: str, **kwargs: typing.Any
        ) -> SasPortalDeploymentHttpRequest: ...
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
                    **kwargs: typing.Any,
                ) -> SasPortalDeviceHttpRequest: ...
                def createSigned(
                    self,
                    *,
                    parent: str,
                    body: SasPortalCreateSignedDeviceRequest = ...,
                    **kwargs: typing.Any,
                ) -> SasPortalDeviceHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> SasPortalListDevicesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: SasPortalListDevicesResponseHttpRequest,
                    previous_response: SasPortalListDevicesResponse,
                ) -> SasPortalListDevicesResponseHttpRequest | None: ...

            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> SasPortalEmptyHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> SasPortalDeploymentHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                filter: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any,
            ) -> SasPortalListDeploymentsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: SasPortalListDeploymentsResponseHttpRequest,
                previous_response: SasPortalListDeploymentsResponse,
            ) -> SasPortalListDeploymentsResponseHttpRequest | None: ...
            def move(
                self,
                *,
                name: str,
                body: SasPortalMoveDeploymentRequest = ...,
                **kwargs: typing.Any,
            ) -> SasPortalOperationHttpRequest: ...
            def patch(
                self,
                *,
                name: str,
                body: SasPortalDeployment = ...,
                updateMask: str = ...,
                **kwargs: typing.Any,
            ) -> SasPortalDeploymentHttpRequest: ...
            def devices(self) -> DevicesResource: ...

        @typing.type_check_only
        class DevicesResource(googleapiclient.discovery.Resource):
            def create(
                self, *, parent: str, body: SasPortalDevice = ..., **kwargs: typing.Any
            ) -> SasPortalDeviceHttpRequest: ...
            def createSigned(
                self,
                *,
                parent: str,
                body: SasPortalCreateSignedDeviceRequest = ...,
                **kwargs: typing.Any,
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
                **kwargs: typing.Any,
            ) -> SasPortalListDevicesResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: SasPortalListDevicesResponseHttpRequest,
                previous_response: SasPortalListDevicesResponse,
            ) -> SasPortalListDevicesResponseHttpRequest | None: ...
            def move(
                self,
                *,
                name: str,
                body: SasPortalMoveDeviceRequest = ...,
                **kwargs: typing.Any,
            ) -> SasPortalOperationHttpRequest: ...
            def patch(
                self,
                *,
                name: str,
                body: SasPortalDevice = ...,
                updateMask: str = ...,
                **kwargs: typing.Any,
            ) -> SasPortalDeviceHttpRequest: ...
            def signDevice(
                self,
                *,
                name: str,
                body: SasPortalSignDeviceRequest = ...,
                **kwargs: typing.Any,
            ) -> SasPortalEmptyHttpRequest: ...
            def updateSigned(
                self,
                *,
                name: str,
                body: SasPortalUpdateSignedDeviceRequest = ...,
                **kwargs: typing.Any,
            ) -> SasPortalDeviceHttpRequest: ...

        @typing.type_check_only
        class NodesResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class DeploymentsResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: SasPortalDeployment = ...,
                    **kwargs: typing.Any,
                ) -> SasPortalDeploymentHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> SasPortalListDeploymentsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: SasPortalListDeploymentsResponseHttpRequest,
                    previous_response: SasPortalListDeploymentsResponse,
                ) -> SasPortalListDeploymentsResponseHttpRequest | None: ...

            @typing.type_check_only
            class DevicesResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: SasPortalDevice = ...,
                    **kwargs: typing.Any,
                ) -> SasPortalDeviceHttpRequest: ...
                def createSigned(
                    self,
                    *,
                    parent: str,
                    body: SasPortalCreateSignedDeviceRequest = ...,
                    **kwargs: typing.Any,
                ) -> SasPortalDeviceHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> SasPortalListDevicesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: SasPortalListDevicesResponseHttpRequest,
                    previous_response: SasPortalListDevicesResponse,
                ) -> SasPortalListDevicesResponseHttpRequest | None: ...

            @typing.type_check_only
            class NodesResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: SasPortalNode = ...,
                    **kwargs: typing.Any,
                ) -> SasPortalNodeHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> SasPortalListNodesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: SasPortalListNodesResponseHttpRequest,
                    previous_response: SasPortalListNodesResponse,
                ) -> SasPortalListNodesResponseHttpRequest | None: ...

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
                filter: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any,
            ) -> SasPortalListNodesResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: SasPortalListNodesResponseHttpRequest,
                previous_response: SasPortalListNodesResponse,
            ) -> SasPortalListNodesResponseHttpRequest | None: ...
            def move(
                self,
                *,
                name: str,
                body: SasPortalMoveNodeRequest = ...,
                **kwargs: typing.Any,
            ) -> SasPortalOperationHttpRequest: ...
            def patch(
                self,
                *,
                name: str,
                body: SasPortalNode = ...,
                updateMask: str = ...,
                **kwargs: typing.Any,
            ) -> SasPortalNodeHttpRequest: ...
            def deployments(self) -> DeploymentsResource: ...
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
    def customers(self) -> CustomersResource: ...
    def deployments(self) -> DeploymentsResource: ...
    def installer(self) -> InstallerResource: ...
    def nodes(self) -> NodesResource: ...
    def policies(self) -> PoliciesResource: ...

@typing.type_check_only
class SasPortalCustomerHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> SasPortalCustomer: ...

@typing.type_check_only
class SasPortalDeploymentHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> SasPortalDeployment: ...

@typing.type_check_only
class SasPortalDeviceHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> SasPortalDevice: ...

@typing.type_check_only
class SasPortalEmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> SasPortalEmpty: ...

@typing.type_check_only
class SasPortalGenerateSecretResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> SasPortalGenerateSecretResponse: ...

@typing.type_check_only
class SasPortalListCustomersResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> SasPortalListCustomersResponse: ...

@typing.type_check_only
class SasPortalListDeploymentsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> SasPortalListDeploymentsResponse: ...

@typing.type_check_only
class SasPortalListDevicesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> SasPortalListDevicesResponse: ...

@typing.type_check_only
class SasPortalListGcpProjectDeploymentsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> SasPortalListGcpProjectDeploymentsResponse: ...

@typing.type_check_only
class SasPortalListLegacyOrganizationsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> SasPortalListLegacyOrganizationsResponse: ...

@typing.type_check_only
class SasPortalListNodesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> SasPortalListNodesResponse: ...

@typing.type_check_only
class SasPortalNodeHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> SasPortalNode: ...

@typing.type_check_only
class SasPortalOperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> SasPortalOperation: ...

@typing.type_check_only
class SasPortalPolicyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> SasPortalPolicy: ...

@typing.type_check_only
class SasPortalProvisionDeploymentResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> SasPortalProvisionDeploymentResponse: ...

@typing.type_check_only
class SasPortalTestPermissionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> SasPortalTestPermissionsResponse: ...

@typing.type_check_only
class SasPortalValidateInstallerResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> SasPortalValidateInstallerResponse: ...
