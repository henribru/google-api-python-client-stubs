import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class AccessContextManagerResource(googleapiclient.discovery.Resource):
    class AccessPoliciesResource(googleapiclient.discovery.Resource):
        class AccessLevelsResource(googleapiclient.discovery.Resource):
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> OperationHttpRequest: ...
            def patch(
                self,
                *,
                name: str,
                body: AccessLevel = ...,
                updateMask: str = ...,
                **kwargs: typing.Any
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
            def create(
                self, *, parent: str, body: AccessLevel = ..., **kwargs: typing.Any
            ) -> OperationHttpRequest: ...
            def replaceAll(
                self,
                *,
                parent: str,
                body: ReplaceAccessLevelsRequest = ...,
                **kwargs: typing.Any
            ) -> OperationHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                accessLevelFormat: typing_extensions.Literal[
                    "LEVEL_FORMAT_UNSPECIFIED", "AS_DEFINED", "CEL"
                ] = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> ListAccessLevelsResponseHttpRequest: ...
        class ServicePerimetersResource(googleapiclient.discovery.Resource):
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> ServicePerimeterHttpRequest: ...
            def patch(
                self,
                *,
                name: str,
                body: ServicePerimeter = ...,
                updateMask: str = ...,
                **kwargs: typing.Any
            ) -> OperationHttpRequest: ...
            def create(
                self, *, parent: str, body: ServicePerimeter = ..., **kwargs: typing.Any
            ) -> OperationHttpRequest: ...
            def commit(
                self,
                *,
                parent: str,
                body: CommitServicePerimetersRequest = ...,
                **kwargs: typing.Any
            ) -> OperationHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> OperationHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageToken: str = ...,
                pageSize: int = ...,
                **kwargs: typing.Any
            ) -> ListServicePerimetersResponseHttpRequest: ...
            def replaceAll(
                self,
                *,
                parent: str,
                body: ReplaceServicePerimetersRequest = ...,
                **kwargs: typing.Any
            ) -> OperationHttpRequest: ...
        def delete(
            self, *, name: str, **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def list(
            self,
            *,
            parent: str = ...,
            pageToken: str = ...,
            pageSize: int = ...,
            **kwargs: typing.Any
        ) -> ListAccessPoliciesResponseHttpRequest: ...
        def patch(
            self,
            *,
            name: str,
            body: AccessPolicy = ...,
            updateMask: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def create(
            self, *, body: AccessPolicy = ..., **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def get(
            self, *, name: str, **kwargs: typing.Any
        ) -> AccessPolicyHttpRequest: ...
        def accessLevels(self) -> AccessLevelsResource: ...
        def servicePerimeters(self) -> ServicePerimetersResource: ...
    class OperationsResource(googleapiclient.discovery.Resource):
        def delete(self, *, name: str, **kwargs: typing.Any) -> EmptyHttpRequest: ...
        def list(
            self,
            *,
            name: str,
            filter: str = ...,
            pageToken: str = ...,
            pageSize: int = ...,
            **kwargs: typing.Any
        ) -> ListOperationsResponseHttpRequest: ...
        def cancel(
            self, *, name: str, body: CancelOperationRequest = ..., **kwargs: typing.Any
        ) -> EmptyHttpRequest: ...
        def get(self, *, name: str, **kwargs: typing.Any) -> OperationHttpRequest: ...
    class OrganizationsResource(googleapiclient.discovery.Resource):
        class GcpUserAccessBindingsResource(googleapiclient.discovery.Resource):
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> OperationHttpRequest: ...
            def create(
                self,
                *,
                parent: str,
                body: GcpUserAccessBinding = ...,
                **kwargs: typing.Any
            ) -> OperationHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> ListGcpUserAccessBindingsResponseHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GcpUserAccessBindingHttpRequest: ...
            def patch(
                self,
                *,
                name: str,
                body: GcpUserAccessBinding = ...,
                updateMask: str = ...,
                **kwargs: typing.Any
            ) -> OperationHttpRequest: ...
        def gcpUserAccessBindings(self) -> GcpUserAccessBindingsResource: ...
    def accessPolicies(self) -> AccessPoliciesResource: ...
    def operations(self) -> OperationsResource: ...
    def organizations(self) -> OrganizationsResource: ...

class ListAccessPoliciesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListAccessPoliciesResponse: ...

class AccessLevelHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> AccessLevel: ...

class ListServicePerimetersResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListServicePerimetersResponse: ...

class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Empty: ...

class ListAccessLevelsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListAccessLevelsResponse: ...

class ListOperationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListOperationsResponse: ...

class GcpUserAccessBindingHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GcpUserAccessBinding: ...

class ServicePerimeterHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ServicePerimeter: ...

class AccessPolicyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> AccessPolicy: ...

class OperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Operation: ...

class ListGcpUserAccessBindingsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListGcpUserAccessBindingsResponse: ...
