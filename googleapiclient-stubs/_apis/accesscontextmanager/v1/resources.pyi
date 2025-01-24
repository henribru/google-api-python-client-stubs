import collections.abc
import typing

import httplib2
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http

from .schemas import *

_list = list

@typing.type_check_only
class AccessContextManagerResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class AccessPoliciesResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class AccessLevelsResource(googleapiclient.discovery.Resource):
            def create(
                self, *, parent: str, body: AccessLevel = ..., **kwargs: typing.Any
            ) -> OperationHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> OperationHttpRequest: ...
            def get(
                self,
                *,
                name: str,
                accessLevelFormat: typing_extensions.Literal[
                    "LEVEL_FORMAT_UNSPECIFIED", "AS_DEFINED", "CEL"
                ] = ...,
                **kwargs: typing.Any,
            ) -> AccessLevelHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                accessLevelFormat: typing_extensions.Literal[
                    "LEVEL_FORMAT_UNSPECIFIED", "AS_DEFINED", "CEL"
                ] = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any,
            ) -> ListAccessLevelsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListAccessLevelsResponseHttpRequest,
                previous_response: ListAccessLevelsResponse,
            ) -> ListAccessLevelsResponseHttpRequest | None: ...
            def patch(
                self,
                *,
                name: str,
                body: AccessLevel = ...,
                updateMask: str = ...,
                **kwargs: typing.Any,
            ) -> OperationHttpRequest: ...
            def replaceAll(
                self,
                *,
                parent: str,
                body: ReplaceAccessLevelsRequest = ...,
                **kwargs: typing.Any,
            ) -> OperationHttpRequest: ...
            def testIamPermissions(
                self,
                *,
                resource: str,
                body: TestIamPermissionsRequest = ...,
                **kwargs: typing.Any,
            ) -> TestIamPermissionsResponseHttpRequest: ...

        @typing.type_check_only
        class AuthorizedOrgsDescsResource(googleapiclient.discovery.Resource):
            def create(
                self,
                *,
                parent: str,
                body: AuthorizedOrgsDesc = ...,
                **kwargs: typing.Any,
            ) -> OperationHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> OperationHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> AuthorizedOrgsDescHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any,
            ) -> ListAuthorizedOrgsDescsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListAuthorizedOrgsDescsResponseHttpRequest,
                previous_response: ListAuthorizedOrgsDescsResponse,
            ) -> ListAuthorizedOrgsDescsResponseHttpRequest | None: ...
            def patch(
                self,
                *,
                name: str,
                body: AuthorizedOrgsDesc = ...,
                updateMask: str = ...,
                **kwargs: typing.Any,
            ) -> OperationHttpRequest: ...

        @typing.type_check_only
        class ServicePerimetersResource(googleapiclient.discovery.Resource):
            def commit(
                self,
                *,
                parent: str,
                body: CommitServicePerimetersRequest = ...,
                **kwargs: typing.Any,
            ) -> OperationHttpRequest: ...
            def create(
                self, *, parent: str, body: ServicePerimeter = ..., **kwargs: typing.Any
            ) -> OperationHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> OperationHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> ServicePerimeterHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any,
            ) -> ListServicePerimetersResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListServicePerimetersResponseHttpRequest,
                previous_response: ListServicePerimetersResponse,
            ) -> ListServicePerimetersResponseHttpRequest | None: ...
            def patch(
                self,
                *,
                name: str,
                body: ServicePerimeter = ...,
                updateMask: str = ...,
                **kwargs: typing.Any,
            ) -> OperationHttpRequest: ...
            def replaceAll(
                self,
                *,
                parent: str,
                body: ReplaceServicePerimetersRequest = ...,
                **kwargs: typing.Any,
            ) -> OperationHttpRequest: ...
            def testIamPermissions(
                self,
                *,
                resource: str,
                body: TestIamPermissionsRequest = ...,
                **kwargs: typing.Any,
            ) -> TestIamPermissionsResponseHttpRequest: ...

        def create(
            self, *, body: AccessPolicy = ..., **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def delete(
            self, *, name: str, **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def get(
            self, *, name: str, **kwargs: typing.Any
        ) -> AccessPolicyHttpRequest: ...
        def getIamPolicy(
            self,
            *,
            resource: str,
            body: GetIamPolicyRequest = ...,
            **kwargs: typing.Any,
        ) -> PolicyHttpRequest: ...
        def list(
            self,
            *,
            pageSize: int = ...,
            pageToken: str = ...,
            parent: str = ...,
            **kwargs: typing.Any,
        ) -> ListAccessPoliciesResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: ListAccessPoliciesResponseHttpRequest,
            previous_response: ListAccessPoliciesResponse,
        ) -> ListAccessPoliciesResponseHttpRequest | None: ...
        def patch(
            self,
            *,
            name: str,
            body: AccessPolicy = ...,
            updateMask: str = ...,
            **kwargs: typing.Any,
        ) -> OperationHttpRequest: ...
        def setIamPolicy(
            self,
            *,
            resource: str,
            body: SetIamPolicyRequest = ...,
            **kwargs: typing.Any,
        ) -> PolicyHttpRequest: ...
        def testIamPermissions(
            self,
            *,
            resource: str,
            body: TestIamPermissionsRequest = ...,
            **kwargs: typing.Any,
        ) -> TestIamPermissionsResponseHttpRequest: ...
        def accessLevels(self) -> AccessLevelsResource: ...
        def authorizedOrgsDescs(self) -> AuthorizedOrgsDescsResource: ...
        def servicePerimeters(self) -> ServicePerimetersResource: ...

    @typing.type_check_only
    class OperationsResource(googleapiclient.discovery.Resource):
        def cancel(
            self, *, name: str, body: CancelOperationRequest = ..., **kwargs: typing.Any
        ) -> EmptyHttpRequest: ...
        def delete(self, *, name: str, **kwargs: typing.Any) -> EmptyHttpRequest: ...
        def get(self, *, name: str, **kwargs: typing.Any) -> OperationHttpRequest: ...
        def list(
            self,
            *,
            name: str,
            filter: str = ...,
            pageSize: int = ...,
            pageToken: str = ...,
            **kwargs: typing.Any,
        ) -> ListOperationsResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: ListOperationsResponseHttpRequest,
            previous_response: ListOperationsResponse,
        ) -> ListOperationsResponseHttpRequest | None: ...

    @typing.type_check_only
    class OrganizationsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class GcpUserAccessBindingsResource(googleapiclient.discovery.Resource):
            def create(
                self,
                *,
                parent: str,
                body: GcpUserAccessBinding = ...,
                **kwargs: typing.Any,
            ) -> OperationHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> OperationHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GcpUserAccessBindingHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any,
            ) -> ListGcpUserAccessBindingsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListGcpUserAccessBindingsResponseHttpRequest,
                previous_response: ListGcpUserAccessBindingsResponse,
            ) -> ListGcpUserAccessBindingsResponseHttpRequest | None: ...
            def patch(
                self,
                *,
                name: str,
                body: GcpUserAccessBinding = ...,
                append: bool = ...,
                updateMask: str = ...,
                **kwargs: typing.Any,
            ) -> OperationHttpRequest: ...

        def gcpUserAccessBindings(self) -> GcpUserAccessBindingsResource: ...

    @typing.type_check_only
    class ServicesResource(googleapiclient.discovery.Resource):
        def get(
            self, *, name: str, **kwargs: typing.Any
        ) -> SupportedServiceHttpRequest: ...
        def list(
            self, *, pageSize: int = ..., pageToken: str = ..., **kwargs: typing.Any
        ) -> ListSupportedServicesResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: ListSupportedServicesResponseHttpRequest,
            previous_response: ListSupportedServicesResponse,
        ) -> ListSupportedServicesResponseHttpRequest | None: ...

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
    def accessPolicies(self) -> AccessPoliciesResource: ...
    def operations(self) -> OperationsResource: ...
    def organizations(self) -> OrganizationsResource: ...
    def services(self) -> ServicesResource: ...

@typing.type_check_only
class AccessLevelHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> AccessLevel: ...

@typing.type_check_only
class AccessPolicyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> AccessPolicy: ...

@typing.type_check_only
class AuthorizedOrgsDescHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> AuthorizedOrgsDesc: ...

@typing.type_check_only
class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Empty: ...

@typing.type_check_only
class GcpUserAccessBindingHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GcpUserAccessBinding: ...

@typing.type_check_only
class ListAccessLevelsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListAccessLevelsResponse: ...

@typing.type_check_only
class ListAccessPoliciesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListAccessPoliciesResponse: ...

@typing.type_check_only
class ListAuthorizedOrgsDescsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListAuthorizedOrgsDescsResponse: ...

@typing.type_check_only
class ListGcpUserAccessBindingsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListGcpUserAccessBindingsResponse: ...

@typing.type_check_only
class ListOperationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListOperationsResponse: ...

@typing.type_check_only
class ListServicePerimetersResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListServicePerimetersResponse: ...

@typing.type_check_only
class ListSupportedServicesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListSupportedServicesResponse: ...

@typing.type_check_only
class OperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Operation: ...

@typing.type_check_only
class PolicyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Policy: ...

@typing.type_check_only
class ServicePerimeterHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ServicePerimeter: ...

@typing.type_check_only
class SupportedServiceHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> SupportedService: ...

@typing.type_check_only
class TestIamPermissionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> TestIamPermissionsResponse: ...
