import collections.abc
import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

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
                **kwargs: typing.Any
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
                **kwargs: typing.Any
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
                **kwargs: typing.Any
            ) -> OperationHttpRequest: ...
            def replaceAll(
                self,
                *,
                parent: str,
                body: ReplaceAccessLevelsRequest = ...,
                **kwargs: typing.Any
            ) -> OperationHttpRequest: ...
            def testIamPermissions(
                self,
                *,
                resource: str,
                body: TestIamPermissionsRequest = ...,
                **kwargs: typing.Any
            ) -> TestIamPermissionsResponseHttpRequest: ...

        @typing.type_check_only
        class ServicePerimetersResource(googleapiclient.discovery.Resource):
            def commit(
                self,
                *,
                parent: str,
                body: CommitServicePerimetersRequest = ...,
                **kwargs: typing.Any
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
                **kwargs: typing.Any
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
                **kwargs: typing.Any
            ) -> OperationHttpRequest: ...
            def replaceAll(
                self,
                *,
                parent: str,
                body: ReplaceServicePerimetersRequest = ...,
                **kwargs: typing.Any
            ) -> OperationHttpRequest: ...
            def testIamPermissions(
                self,
                *,
                resource: str,
                body: TestIamPermissionsRequest = ...,
                **kwargs: typing.Any
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
            **kwargs: typing.Any
        ) -> PolicyHttpRequest: ...
        def list(
            self,
            *,
            pageSize: int = ...,
            pageToken: str = ...,
            parent: str = ...,
            **kwargs: typing.Any
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
        def accessLevels(self) -> AccessLevelsResource: ...
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
            **kwargs: typing.Any
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
                **kwargs: typing.Any
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
                **kwargs: typing.Any
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
                updateMask: str = ...,
                **kwargs: typing.Any
            ) -> OperationHttpRequest: ...

        def gcpUserAccessBindings(self) -> GcpUserAccessBindingsResource: ...

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
    def accessPolicies(self) -> AccessPoliciesResource: ...
    def operations(self) -> OperationsResource: ...
    def organizations(self) -> OrganizationsResource: ...

@typing.type_check_only
class AccessLevelHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> AccessLevel: ...

@typing.type_check_only
class AccessPolicyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> AccessPolicy: ...

@typing.type_check_only
class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Empty: ...

@typing.type_check_only
class GcpUserAccessBindingHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GcpUserAccessBinding: ...

@typing.type_check_only
class ListAccessLevelsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListAccessLevelsResponse: ...

@typing.type_check_only
class ListAccessPoliciesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListAccessPoliciesResponse: ...

@typing.type_check_only
class ListGcpUserAccessBindingsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListGcpUserAccessBindingsResponse: ...

@typing.type_check_only
class ListOperationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListOperationsResponse: ...

@typing.type_check_only
class ListServicePerimetersResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListServicePerimetersResponse: ...

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
class ServicePerimeterHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ServicePerimeter: ...

@typing.type_check_only
class TestIamPermissionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> TestIamPermissionsResponse: ...
