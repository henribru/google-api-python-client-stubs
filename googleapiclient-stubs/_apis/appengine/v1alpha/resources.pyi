import collections.abc
import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

_list = list

@typing.type_check_only
class AppengineResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class AppsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class AuthorizedCertificatesResource(googleapiclient.discovery.Resource):
            def create(
                self,
                *,
                appsId: str,
                body: AuthorizedCertificate = ...,
                **kwargs: typing.Any
            ) -> AuthorizedCertificateHttpRequest: ...
            def delete(
                self,
                *,
                appsId: str,
                authorizedCertificatesId: str,
                **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def get(
                self,
                *,
                appsId: str,
                authorizedCertificatesId: str,
                view: typing_extensions.Literal[
                    "BASIC_CERTIFICATE", "FULL_CERTIFICATE"
                ] = ...,
                **kwargs: typing.Any
            ) -> AuthorizedCertificateHttpRequest: ...
            def list(
                self,
                *,
                appsId: str,
                pageSize: int = ...,
                pageToken: str = ...,
                view: typing_extensions.Literal[
                    "BASIC_CERTIFICATE", "FULL_CERTIFICATE"
                ] = ...,
                **kwargs: typing.Any
            ) -> ListAuthorizedCertificatesResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListAuthorizedCertificatesResponseHttpRequest,
                previous_response: ListAuthorizedCertificatesResponse,
            ) -> ListAuthorizedCertificatesResponseHttpRequest | None: ...
            def patch(
                self,
                *,
                appsId: str,
                authorizedCertificatesId: str,
                body: AuthorizedCertificate = ...,
                updateMask: str = ...,
                **kwargs: typing.Any
            ) -> AuthorizedCertificateHttpRequest: ...

        @typing.type_check_only
        class AuthorizedDomainsResource(googleapiclient.discovery.Resource):
            def list(
                self,
                *,
                appsId: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> ListAuthorizedDomainsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListAuthorizedDomainsResponseHttpRequest,
                previous_response: ListAuthorizedDomainsResponse,
            ) -> ListAuthorizedDomainsResponseHttpRequest | None: ...

        @typing.type_check_only
        class DomainMappingsResource(googleapiclient.discovery.Resource):
            def create(
                self,
                *,
                appsId: str,
                body: DomainMapping = ...,
                noManagedCertificate: bool = ...,
                overrideStrategy: typing_extensions.Literal[
                    "UNSPECIFIED_DOMAIN_OVERRIDE_STRATEGY", "STRICT", "OVERRIDE"
                ] = ...,
                **kwargs: typing.Any
            ) -> OperationHttpRequest: ...
            def delete(
                self, *, appsId: str, domainMappingsId: str, **kwargs: typing.Any
            ) -> OperationHttpRequest: ...
            def get(
                self, *, appsId: str, domainMappingsId: str, **kwargs: typing.Any
            ) -> DomainMappingHttpRequest: ...
            def list(
                self,
                *,
                appsId: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> ListDomainMappingsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListDomainMappingsResponseHttpRequest,
                previous_response: ListDomainMappingsResponse,
            ) -> ListDomainMappingsResponseHttpRequest | None: ...
            def patch(
                self,
                *,
                appsId: str,
                domainMappingsId: str,
                body: DomainMapping = ...,
                noManagedCertificate: bool = ...,
                updateMask: str = ...,
                **kwargs: typing.Any
            ) -> OperationHttpRequest: ...

        @typing.type_check_only
        class LocationsResource(googleapiclient.discovery.Resource):
            def get(
                self, *, appsId: str, locationsId: str, **kwargs: typing.Any
            ) -> LocationHttpRequest: ...
            def list(
                self,
                *,
                appsId: str,
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

        @typing.type_check_only
        class OperationsResource(googleapiclient.discovery.Resource):
            def get(
                self, *, appsId: str, operationsId: str, **kwargs: typing.Any
            ) -> OperationHttpRequest: ...
            def list(
                self,
                *,
                appsId: str,
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

        def authorizedCertificates(self) -> AuthorizedCertificatesResource: ...
        def authorizedDomains(self) -> AuthorizedDomainsResource: ...
        def domainMappings(self) -> DomainMappingsResource: ...
        def locations(self) -> LocationsResource: ...
        def operations(self) -> OperationsResource: ...

    @typing.type_check_only
    class ProjectsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class LocationsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class OperationsResource(googleapiclient.discovery.Resource):
                def get(
                    self,
                    *,
                    projectsId: str,
                    locationsId: str,
                    operationsId: str,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def list(
                    self,
                    *,
                    projectsId: str,
                    locationsId: str,
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
                self, *, projectsId: str, locationsId: str, **kwargs: typing.Any
            ) -> LocationHttpRequest: ...
            def list(
                self,
                *,
                projectsId: str,
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
    def apps(self) -> AppsResource: ...
    def projects(self) -> ProjectsResource: ...

@typing.type_check_only
class AuthorizedCertificateHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> AuthorizedCertificate: ...

@typing.type_check_only
class DomainMappingHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> DomainMapping: ...

@typing.type_check_only
class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Empty: ...

@typing.type_check_only
class ListAuthorizedCertificatesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListAuthorizedCertificatesResponse: ...

@typing.type_check_only
class ListAuthorizedDomainsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListAuthorizedDomainsResponse: ...

@typing.type_check_only
class ListDomainMappingsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListDomainMappingsResponse: ...

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
