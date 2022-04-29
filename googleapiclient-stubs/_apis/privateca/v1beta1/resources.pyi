import collections.abc
import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

_list = list

@typing.type_check_only
class CertificateAuthorityServiceResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class ProjectsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class LocationsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class CertificateAuthoritiesResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class CertificateRevocationListsResource(
                    googleapiclient.discovery.Resource
                ):
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> CertificateRevocationListHttpRequest: ...
                    def getIamPolicy(
                        self,
                        *,
                        resource: str,
                        options_requestedPolicyVersion: int = ...,
                        **kwargs: typing.Any
                    ) -> PolicyHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str = ...,
                        orderBy: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any
                    ) -> ListCertificateRevocationListsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: ListCertificateRevocationListsResponseHttpRequest,
                        previous_response: ListCertificateRevocationListsResponse,
                    ) -> ListCertificateRevocationListsResponseHttpRequest | None: ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: CertificateRevocationList = ...,
                        requestId: str = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any
                    ) -> OperationHttpRequest: ...
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

                @typing.type_check_only
                class CertificatesResource(googleapiclient.discovery.Resource):
                    def create(
                        self,
                        *,
                        parent: str,
                        body: Certificate = ...,
                        certificateId: str = ...,
                        requestId: str = ...,
                        **kwargs: typing.Any
                    ) -> CertificateHttpRequest: ...
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
                        requestId: str = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any
                    ) -> CertificateHttpRequest: ...
                    def revoke(
                        self,
                        *,
                        name: str,
                        body: RevokeCertificateRequest = ...,
                        **kwargs: typing.Any
                    ) -> CertificateHttpRequest: ...

                def activate(
                    self,
                    *,
                    name: str,
                    body: ActivateCertificateAuthorityRequest = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def create(
                    self,
                    *,
                    parent: str,
                    body: CertificateAuthority = ...,
                    certificateAuthorityId: str = ...,
                    requestId: str = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def disable(
                    self,
                    *,
                    name: str,
                    body: DisableCertificateAuthorityRequest = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def enable(
                    self,
                    *,
                    name: str,
                    body: EnableCertificateAuthorityRequest = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def fetch(
                    self, *, name: str, **kwargs: typing.Any
                ) -> FetchCertificateAuthorityCsrResponseHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> CertificateAuthorityHttpRequest: ...
                def getIamPolicy(
                    self,
                    *,
                    resource: str,
                    options_requestedPolicyVersion: int = ...,
                    **kwargs: typing.Any
                ) -> PolicyHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> ListCertificateAuthoritiesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListCertificateAuthoritiesResponseHttpRequest,
                    previous_response: ListCertificateAuthoritiesResponse,
                ) -> ListCertificateAuthoritiesResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: CertificateAuthority = ...,
                    requestId: str = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def restore(
                    self,
                    *,
                    name: str,
                    body: RestoreCertificateAuthorityRequest = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def scheduleDelete(
                    self,
                    *,
                    name: str,
                    body: ScheduleDeleteCertificateAuthorityRequest = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
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
                def certificateRevocationLists(
                    self,
                ) -> CertificateRevocationListsResource: ...
                def certificates(self) -> CertificatesResource: ...

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

            @typing.type_check_only
            class ReusableConfigsResource(googleapiclient.discovery.Resource):
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> ReusableConfigHttpRequest: ...
                def getIamPolicy(
                    self,
                    *,
                    resource: str,
                    options_requestedPolicyVersion: int = ...,
                    **kwargs: typing.Any
                ) -> PolicyHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> ListReusableConfigsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListReusableConfigsResponseHttpRequest,
                    previous_response: ListReusableConfigsResponse,
                ) -> ListReusableConfigsResponseHttpRequest | None: ...
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
            def certificateAuthorities(self) -> CertificateAuthoritiesResource: ...
            def operations(self) -> OperationsResource: ...
            def reusableConfigs(self) -> ReusableConfigsResource: ...

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
class CertificateAuthorityHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> CertificateAuthority: ...

@typing.type_check_only
class CertificateRevocationListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> CertificateRevocationList: ...

@typing.type_check_only
class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Empty: ...

@typing.type_check_only
class FetchCertificateAuthorityCsrResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> FetchCertificateAuthorityCsrResponse: ...

@typing.type_check_only
class ListCertificateAuthoritiesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListCertificateAuthoritiesResponse: ...

@typing.type_check_only
class ListCertificateRevocationListsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListCertificateRevocationListsResponse: ...

@typing.type_check_only
class ListCertificatesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListCertificatesResponse: ...

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
class ListReusableConfigsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListReusableConfigsResponse: ...

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
class ReusableConfigHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ReusableConfig: ...

@typing.type_check_only
class TestIamPermissionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> TestIamPermissionsResponse: ...
