import collections.abc
import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

_list = list

@typing.type_check_only
class CloudDomainsResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class ProjectsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class LocationsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class OperationsResource(googleapiclient.discovery.Resource):
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

            @typing.type_check_only
            class RegistrationsResource(googleapiclient.discovery.Resource):
                def configureContactSettings(
                    self,
                    *,
                    registration: str,
                    body: ConfigureContactSettingsRequest = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def configureDnsSettings(
                    self,
                    *,
                    registration: str,
                    body: ConfigureDnsSettingsRequest = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def configureManagementSettings(
                    self,
                    *,
                    registration: str,
                    body: ConfigureManagementSettingsRequest = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def export(
                    self,
                    *,
                    name: str,
                    body: ExportRegistrationRequest = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> RegistrationHttpRequest: ...
                def getIamPolicy(
                    self,
                    *,
                    resource: str,
                    options_requestedPolicyVersion: int = ...,
                    **kwargs: typing.Any
                ) -> PolicyHttpRequest: ...
                def import_(
                    self,
                    *,
                    parent: str,
                    body: ImportDomainRequest = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> ListRegistrationsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListRegistrationsResponseHttpRequest,
                    previous_response: ListRegistrationsResponse,
                ) -> ListRegistrationsResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: Registration = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def register(
                    self,
                    *,
                    parent: str,
                    body: RegisterDomainRequest = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def resetAuthorizationCode(
                    self,
                    *,
                    registration: str,
                    body: ResetAuthorizationCodeRequest = ...,
                    **kwargs: typing.Any
                ) -> AuthorizationCodeHttpRequest: ...
                def retrieveAuthorizationCode(
                    self, *, registration: str, **kwargs: typing.Any
                ) -> AuthorizationCodeHttpRequest: ...
                def retrieveImportableDomains(
                    self,
                    *,
                    location: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> RetrieveImportableDomainsResponseHttpRequest: ...
                def retrieveImportableDomains_next(
                    self,
                    previous_request: RetrieveImportableDomainsResponseHttpRequest,
                    previous_response: RetrieveImportableDomainsResponse,
                ) -> RetrieveImportableDomainsResponseHttpRequest | None: ...
                def retrieveRegisterParameters(
                    self, *, location: str, domainName: str = ..., **kwargs: typing.Any
                ) -> RetrieveRegisterParametersResponseHttpRequest: ...
                def retrieveTransferParameters(
                    self, *, location: str, domainName: str = ..., **kwargs: typing.Any
                ) -> RetrieveTransferParametersResponseHttpRequest: ...
                def searchDomains(
                    self, *, location: str, query: str = ..., **kwargs: typing.Any
                ) -> SearchDomainsResponseHttpRequest: ...
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
                def transfer(
                    self,
                    *,
                    parent: str,
                    body: TransferDomainRequest = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...

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
            def operations(self) -> OperationsResource: ...
            def registrations(self) -> RegistrationsResource: ...

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
class AuthorizationCodeHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> AuthorizationCode: ...

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
class ListRegistrationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListRegistrationsResponse: ...

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

@typing.type_check_only
class PolicyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Policy: ...

@typing.type_check_only
class RegistrationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Registration: ...

@typing.type_check_only
class RetrieveImportableDomainsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> RetrieveImportableDomainsResponse: ...

@typing.type_check_only
class RetrieveRegisterParametersResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> RetrieveRegisterParametersResponse: ...

@typing.type_check_only
class RetrieveTransferParametersResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> RetrieveTransferParametersResponse: ...

@typing.type_check_only
class SearchDomainsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> SearchDomainsResponse: ...

@typing.type_check_only
class TestIamPermissionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> TestIamPermissionsResponse: ...
