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

        @typing.type_check_only
        class ServicePerimetersResource(googleapiclient.discovery.Resource):
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

        def create(
            self, *, body: AccessPolicy = ..., **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def delete(
            self, *, name: str, **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def get(
            self, *, name: str, **kwargs: typing.Any
        ) -> AccessPolicyHttpRequest: ...
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
        def accessLevels(self) -> AccessLevelsResource: ...
        def servicePerimeters(self) -> ServicePerimetersResource: ...

    @typing.type_check_only
    class OperationsResource(googleapiclient.discovery.Resource):
        def get(self, *, name: str, **kwargs: typing.Any) -> OperationHttpRequest: ...

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
class ServicePerimeterHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ServicePerimeter: ...
