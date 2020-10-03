import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class AndroidProvisioningPartnerResource(googleapiclient.discovery.Resource):
    class PartnersResource(googleapiclient.discovery.Resource):
        class CustomersResource(googleapiclient.discovery.Resource):
            def list(
                self,
                *,
                partnerId: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> ListCustomersResponseHttpRequest: ...
            def create(
                self,
                *,
                parent: str,
                body: CreateCustomerRequest = ...,
                **kwargs: typing.Any
            ) -> CompanyHttpRequest: ...
        class DevicesResource(googleapiclient.discovery.Resource):
            def get(self, *, name: str, **kwargs: typing.Any) -> DeviceHttpRequest: ...
            def claimAsync(
                self,
                *,
                partnerId: str,
                body: ClaimDevicesRequest = ...,
                **kwargs: typing.Any
            ) -> OperationHttpRequest: ...
            def unclaimAsync(
                self,
                *,
                partnerId: str,
                body: UnclaimDevicesRequest = ...,
                **kwargs: typing.Any
            ) -> OperationHttpRequest: ...
            def updateMetadataAsync(
                self,
                *,
                partnerId: str,
                body: UpdateDeviceMetadataInBatchRequest = ...,
                **kwargs: typing.Any
            ) -> OperationHttpRequest: ...
            def findByIdentifier(
                self,
                *,
                partnerId: str,
                body: FindDevicesByDeviceIdentifierRequest = ...,
                **kwargs: typing.Any
            ) -> FindDevicesByDeviceIdentifierResponseHttpRequest: ...
            def metadata(
                self,
                *,
                metadataOwnerId: str,
                deviceId: str,
                body: UpdateDeviceMetadataRequest = ...,
                **kwargs: typing.Any
            ) -> DeviceMetadataHttpRequest: ...
            def unclaim(
                self,
                *,
                partnerId: str,
                body: UnclaimDeviceRequest = ...,
                **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def claim(
                self,
                *,
                partnerId: str,
                body: ClaimDeviceRequest = ...,
                **kwargs: typing.Any
            ) -> ClaimDeviceResponseHttpRequest: ...
            def findByOwner(
                self,
                *,
                partnerId: str,
                body: FindDevicesByOwnerRequest = ...,
                **kwargs: typing.Any
            ) -> FindDevicesByOwnerResponseHttpRequest: ...
        class VendorsResource(googleapiclient.discovery.Resource):
            class CustomersResource(googleapiclient.discovery.Resource):
                def list(
                    self,
                    *,
                    parent: str,
                    pageToken: str = ...,
                    pageSize: int = ...,
                    **kwargs: typing.Any
                ) -> ListVendorCustomersResponseHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageToken: str = ...,
                pageSize: int = ...,
                **kwargs: typing.Any
            ) -> ListVendorsResponseHttpRequest: ...
            def customers(self) -> CustomersResource: ...
        def customers(self) -> CustomersResource: ...
        def devices(self) -> DevicesResource: ...
        def vendors(self) -> VendorsResource: ...
    class CustomersResource(googleapiclient.discovery.Resource):
        class DpcsResource(googleapiclient.discovery.Resource):
            def list(
                self, *, parent: str, **kwargs: typing.Any
            ) -> CustomerListDpcsResponseHttpRequest: ...
        class DevicesResource(googleapiclient.discovery.Resource):
            def applyConfiguration(
                self,
                *,
                parent: str,
                body: CustomerApplyConfigurationRequest = ...,
                **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def get(self, *, name: str, **kwargs: typing.Any) -> DeviceHttpRequest: ...
            def unclaim(
                self,
                *,
                parent: str,
                body: CustomerUnclaimDeviceRequest = ...,
                **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageToken: str = ...,
                pageSize: str = ...,
                **kwargs: typing.Any
            ) -> CustomerListDevicesResponseHttpRequest: ...
            def removeConfiguration(
                self,
                *,
                parent: str,
                body: CustomerRemoveConfigurationRequest = ...,
                **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
        class ConfigurationsResource(googleapiclient.discovery.Resource):
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> ConfigurationHttpRequest: ...
            def create(
                self, *, parent: str, body: Configuration = ..., **kwargs: typing.Any
            ) -> ConfigurationHttpRequest: ...
            def patch(
                self,
                *,
                name: str,
                body: Configuration = ...,
                updateMask: str = ...,
                **kwargs: typing.Any
            ) -> ConfigurationHttpRequest: ...
            def list(
                self, *, parent: str, **kwargs: typing.Any
            ) -> CustomerListConfigurationsResponseHttpRequest: ...
        def list(
            self, *, pageSize: int = ..., pageToken: str = ..., **kwargs: typing.Any
        ) -> CustomerListCustomersResponseHttpRequest: ...
        def dpcs(self) -> DpcsResource: ...
        def devices(self) -> DevicesResource: ...
        def configurations(self) -> ConfigurationsResource: ...
    class OperationsResource(googleapiclient.discovery.Resource):
        def get(self, *, name: str, **kwargs: typing.Any) -> OperationHttpRequest: ...
    def partners(self) -> PartnersResource: ...
    def customers(self) -> CustomersResource: ...
    def operations(self) -> OperationsResource: ...

class ConfigurationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Configuration: ...

class CustomerListConfigurationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> CustomerListConfigurationsResponse: ...

class CustomerListCustomersResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> CustomerListCustomersResponse: ...

class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Empty: ...

class ClaimDeviceResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ClaimDeviceResponse: ...

class CustomerListDevicesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> CustomerListDevicesResponse: ...

class FindDevicesByDeviceIdentifierResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> FindDevicesByDeviceIdentifierResponse: ...

class CustomerListDpcsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> CustomerListDpcsResponse: ...

class DeviceMetadataHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> DeviceMetadata: ...

class FindDevicesByOwnerResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> FindDevicesByOwnerResponse: ...

class CompanyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Company: ...

class ListVendorsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListVendorsResponse: ...

class ListVendorCustomersResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListVendorCustomersResponse: ...

class OperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Operation: ...

class ListCustomersResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListCustomersResponse: ...

class DeviceHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Device: ...
