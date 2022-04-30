import collections.abc
import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

_list = list

@typing.type_check_only
class AndroidProvisioningPartnerResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class CustomersResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class ConfigurationsResource(googleapiclient.discovery.Resource):
            def create(
                self, *, parent: str, body: Configuration = ..., **kwargs: typing.Any
            ) -> ConfigurationHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> ConfigurationHttpRequest: ...
            def list(
                self, *, parent: str, **kwargs: typing.Any
            ) -> CustomerListConfigurationsResponseHttpRequest: ...
            def patch(
                self,
                *,
                name: str,
                body: Configuration = ...,
                updateMask: str = ...,
                **kwargs: typing.Any
            ) -> ConfigurationHttpRequest: ...

        @typing.type_check_only
        class DevicesResource(googleapiclient.discovery.Resource):
            def applyConfiguration(
                self,
                *,
                parent: str,
                body: CustomerApplyConfigurationRequest = ...,
                **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def get(self, *, name: str, **kwargs: typing.Any) -> DeviceHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: str = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> CustomerListDevicesResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: CustomerListDevicesResponseHttpRequest,
                previous_response: CustomerListDevicesResponse,
            ) -> CustomerListDevicesResponseHttpRequest | None: ...
            def removeConfiguration(
                self,
                *,
                parent: str,
                body: CustomerRemoveConfigurationRequest = ...,
                **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def unclaim(
                self,
                *,
                parent: str,
                body: CustomerUnclaimDeviceRequest = ...,
                **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...

        @typing.type_check_only
        class DpcsResource(googleapiclient.discovery.Resource):
            def list(
                self, *, parent: str, **kwargs: typing.Any
            ) -> CustomerListDpcsResponseHttpRequest: ...

        def list(
            self, *, pageSize: int = ..., pageToken: str = ..., **kwargs: typing.Any
        ) -> CustomerListCustomersResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: CustomerListCustomersResponseHttpRequest,
            previous_response: CustomerListCustomersResponse,
        ) -> CustomerListCustomersResponseHttpRequest | None: ...
        def configurations(self) -> ConfigurationsResource: ...
        def devices(self) -> DevicesResource: ...
        def dpcs(self) -> DpcsResource: ...

    @typing.type_check_only
    class OperationsResource(googleapiclient.discovery.Resource):
        def get(self, *, name: str, **kwargs: typing.Any) -> OperationHttpRequest: ...

    @typing.type_check_only
    class PartnersResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class CustomersResource(googleapiclient.discovery.Resource):
            def create(
                self,
                *,
                parent: str,
                body: CreateCustomerRequest = ...,
                **kwargs: typing.Any
            ) -> CompanyHttpRequest: ...
            def list(
                self,
                *,
                partnerId: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> ListCustomersResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListCustomersResponseHttpRequest,
                previous_response: ListCustomersResponse,
            ) -> ListCustomersResponseHttpRequest | None: ...

        @typing.type_check_only
        class DevicesResource(googleapiclient.discovery.Resource):
            def claim(
                self,
                *,
                partnerId: str,
                body: ClaimDeviceRequest = ...,
                **kwargs: typing.Any
            ) -> ClaimDeviceResponseHttpRequest: ...
            def claimAsync(
                self,
                *,
                partnerId: str,
                body: ClaimDevicesRequest = ...,
                **kwargs: typing.Any
            ) -> OperationHttpRequest: ...
            def findByIdentifier(
                self,
                *,
                partnerId: str,
                body: FindDevicesByDeviceIdentifierRequest = ...,
                **kwargs: typing.Any
            ) -> FindDevicesByDeviceIdentifierResponseHttpRequest: ...
            def findByIdentifier_next(
                self,
                previous_request: FindDevicesByDeviceIdentifierResponseHttpRequest,
                previous_response: FindDevicesByDeviceIdentifierResponse,
            ) -> FindDevicesByDeviceIdentifierResponseHttpRequest | None: ...
            def findByOwner(
                self,
                *,
                partnerId: str,
                body: FindDevicesByOwnerRequest = ...,
                **kwargs: typing.Any
            ) -> FindDevicesByOwnerResponseHttpRequest: ...
            def findByOwner_next(
                self,
                previous_request: FindDevicesByOwnerResponseHttpRequest,
                previous_response: FindDevicesByOwnerResponse,
            ) -> FindDevicesByOwnerResponseHttpRequest | None: ...
            def get(self, *, name: str, **kwargs: typing.Any) -> DeviceHttpRequest: ...
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

        @typing.type_check_only
        class VendorsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class CustomersResource(googleapiclient.discovery.Resource):
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> ListVendorCustomersResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListVendorCustomersResponseHttpRequest,
                    previous_response: ListVendorCustomersResponse,
                ) -> ListVendorCustomersResponseHttpRequest | None: ...

            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> ListVendorsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListVendorsResponseHttpRequest,
                previous_response: ListVendorsResponse,
            ) -> ListVendorsResponseHttpRequest | None: ...
            def customers(self) -> CustomersResource: ...

        def customers(self) -> CustomersResource: ...
        def devices(self) -> DevicesResource: ...
        def vendors(self) -> VendorsResource: ...

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
    def customers(self) -> CustomersResource: ...
    def operations(self) -> OperationsResource: ...
    def partners(self) -> PartnersResource: ...

@typing.type_check_only
class ClaimDeviceResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ClaimDeviceResponse: ...

@typing.type_check_only
class CompanyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Company: ...

@typing.type_check_only
class ConfigurationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Configuration: ...

@typing.type_check_only
class CustomerListConfigurationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> CustomerListConfigurationsResponse: ...

@typing.type_check_only
class CustomerListCustomersResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> CustomerListCustomersResponse: ...

@typing.type_check_only
class CustomerListDevicesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> CustomerListDevicesResponse: ...

@typing.type_check_only
class CustomerListDpcsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> CustomerListDpcsResponse: ...

@typing.type_check_only
class DeviceHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Device: ...

@typing.type_check_only
class DeviceMetadataHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> DeviceMetadata: ...

@typing.type_check_only
class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Empty: ...

@typing.type_check_only
class FindDevicesByDeviceIdentifierResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> FindDevicesByDeviceIdentifierResponse: ...

@typing.type_check_only
class FindDevicesByOwnerResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> FindDevicesByOwnerResponse: ...

@typing.type_check_only
class ListCustomersResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListCustomersResponse: ...

@typing.type_check_only
class ListVendorCustomersResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListVendorCustomersResponse: ...

@typing.type_check_only
class ListVendorsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListVendorsResponse: ...

@typing.type_check_only
class OperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Operation: ...
