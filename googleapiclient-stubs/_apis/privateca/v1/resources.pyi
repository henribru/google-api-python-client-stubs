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
            class CaPoolsResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class CertificateAuthoritiesResource(
                    googleapiclient.discovery.Resource
                ):
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
                    def delete(
                        self,
                        *,
                        name: str,
                        ignoreActiveCertificates: bool = ...,
                        requestId: str = ...,
                        skipGracePeriod: bool = ...,
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
                    def undelete(
                        self,
                        *,
                        name: str,
                        body: UndeleteCertificateAuthorityRequest = ...,
                        **kwargs: typing.Any
                    ) -> OperationHttpRequest: ...
                    def certificateRevocationLists(
                        self,
                    ) -> CertificateRevocationListsResource: ...

                @typing.type_check_only
                class CertificatesResource(googleapiclient.discovery.Resource):
                    def create(
                        self,
                        *,
                        parent: str,
                        body: Certificate = ...,
                        certificateId: str = ...,
                        issuingCertificateAuthorityId: str = ...,
                        requestId: str = ...,
                        validateOnly: bool = ...,
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

                def create(
                    self,
                    *,
                    parent: str,
                    body: CaPool = ...,
                    caPoolId: str = ...,
                    requestId: str = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def delete(
                    self, *, name: str, requestId: str = ..., **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def fetchCaCerts(
                    self,
                    *,
                    caPool: str,
                    body: FetchCaCertsRequest = ...,
                    **kwargs: typing.Any
                ) -> FetchCaCertsResponseHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> CaPoolHttpRequest: ...
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
                ) -> ListCaPoolsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListCaPoolsResponseHttpRequest,
                    previous_response: ListCaPoolsResponse,
                ) -> ListCaPoolsResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: CaPool = ...,
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
                def certificateAuthorities(self) -> CertificateAuthoritiesResource: ...
                def certificates(self) -> CertificatesResource: ...

            @typing.type_check_only
            class CertificateTemplatesResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: CertificateTemplate = ...,
                    certificateTemplateId: str = ...,
                    requestId: str = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def delete(
                    self, *, name: str, requestId: str = ..., **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> CertificateTemplateHttpRequest: ...
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
                ) -> ListCertificateTemplatesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListCertificateTemplatesResponseHttpRequest,
                    previous_response: ListCertificateTemplatesResponse,
                ) -> ListCertificateTemplatesResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: CertificateTemplate = ...,
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
            def caPools(self) -> CaPoolsResource: ...
            def certificateTemplates(self) -> CertificateTemplatesResource: ...
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
class CaPoolHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> CaPool: ...

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
class CertificateTemplateHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> CertificateTemplate: ...

@typing.type_check_only
class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Empty: ...

@typing.type_check_only
class FetchCaCertsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> FetchCaCertsResponse: ...

@typing.type_check_only
class FetchCertificateAuthorityCsrResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> FetchCertificateAuthorityCsrResponse: ...

@typing.type_check_only
class ListCaPoolsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListCaPoolsResponse: ...

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
class ListCertificateTemplatesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListCertificateTemplatesResponse: ...

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
class TestIamPermissionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> TestIamPermissionsResponse: ...
