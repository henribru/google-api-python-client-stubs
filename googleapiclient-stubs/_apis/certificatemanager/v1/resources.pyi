import collections.abc
import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

_list = list

@typing.type_check_only
class CertificateManagerResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class ProjectsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class LocationsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class CertificateIssuanceConfigsResource(
                googleapiclient.discovery.Resource
            ):
                def create(
                    self,
                    *,
                    parent: str,
                    body: CertificateIssuanceConfig = ...,
                    certificateIssuanceConfigId: str = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> CertificateIssuanceConfigHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> ListCertificateIssuanceConfigsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListCertificateIssuanceConfigsResponseHttpRequest,
                    previous_response: ListCertificateIssuanceConfigsResponse,
                ) -> ListCertificateIssuanceConfigsResponseHttpRequest | None: ...

            @typing.type_check_only
            class CertificateMapsResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class CertificateMapEntriesResource(googleapiclient.discovery.Resource):
                    def create(
                        self,
                        *,
                        parent: str,
                        body: CertificateMapEntry = ...,
                        certificateMapEntryId: str = ...,
                        **kwargs: typing.Any
                    ) -> OperationHttpRequest: ...
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> OperationHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> CertificateMapEntryHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str = ...,
                        orderBy: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any
                    ) -> ListCertificateMapEntriesResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: ListCertificateMapEntriesResponseHttpRequest,
                        previous_response: ListCertificateMapEntriesResponse,
                    ) -> ListCertificateMapEntriesResponseHttpRequest | None: ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: CertificateMapEntry = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any
                    ) -> OperationHttpRequest: ...

                def create(
                    self,
                    *,
                    parent: str,
                    body: CertificateMap = ...,
                    certificateMapId: str = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> CertificateMapHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> ListCertificateMapsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListCertificateMapsResponseHttpRequest,
                    previous_response: ListCertificateMapsResponse,
                ) -> ListCertificateMapsResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: CertificateMap = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def certificateMapEntries(self) -> CertificateMapEntriesResource: ...

            @typing.type_check_only
            class CertificatesResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: Certificate = ...,
                    certificateId: str = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> CertificateHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> ListCertificatesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListCertificatesResponseHttpRequest,
                    previous_response: ListCertificatesResponse,
                ) -> ListCertificatesResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: Certificate = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...

            @typing.type_check_only
            class DnsAuthorizationsResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: DnsAuthorization = ...,
                    dnsAuthorizationId: str = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> DnsAuthorizationHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> ListDnsAuthorizationsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListDnsAuthorizationsResponseHttpRequest,
                    previous_response: ListDnsAuthorizationsResponse,
                ) -> ListDnsAuthorizationsResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: DnsAuthorization = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...

            @typing.type_check_only
            class OperationsResource(googleapiclient.discovery.Resource):
                def cancel(
                    self,
                    *,
                    name: str,
                    body: CancelOperationRequest = ...,
                    **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def list(
                    self,
                    *,
                    name: str,
                    filter: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> ListOperationsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListOperationsResponseHttpRequest,
                    previous_response: ListOperationsResponse,
                ) -> ListOperationsResponseHttpRequest | None: ...

            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> LocationHttpRequest: ...
            def list(
                self,
                *,
                name: str,
                filter: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> ListLocationsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListLocationsResponseHttpRequest,
                previous_response: ListLocationsResponse,
            ) -> ListLocationsResponseHttpRequest | None: ...
            def certificateIssuanceConfigs(
                self,
            ) -> CertificateIssuanceConfigsResource: ...
            def certificateMaps(self) -> CertificateMapsResource: ...
            def certificates(self) -> CertificatesResource: ...
            def dnsAuthorizations(self) -> DnsAuthorizationsResource: ...
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
class CertificateHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Certificate: ...

@typing.type_check_only
class CertificateIssuanceConfigHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> CertificateIssuanceConfig: ...

@typing.type_check_only
class CertificateMapHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> CertificateMap: ...

@typing.type_check_only
class CertificateMapEntryHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> CertificateMapEntry: ...

@typing.type_check_only
class DnsAuthorizationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> DnsAuthorization: ...

@typing.type_check_only
class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Empty: ...

@typing.type_check_only
class ListCertificateIssuanceConfigsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListCertificateIssuanceConfigsResponse: ...

@typing.type_check_only
class ListCertificateMapEntriesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListCertificateMapEntriesResponse: ...

@typing.type_check_only
class ListCertificateMapsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListCertificateMapsResponse: ...

@typing.type_check_only
class ListCertificatesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListCertificatesResponse: ...

@typing.type_check_only
class ListDnsAuthorizationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListDnsAuthorizationsResponse: ...

@typing.type_check_only
class ListLocationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListLocationsResponse: ...

@typing.type_check_only
class ListOperationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListOperationsResponse: ...

@typing.type_check_only
class LocationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Location: ...

@typing.type_check_only
class OperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Operation: ...
