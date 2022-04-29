import collections.abc
import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

_list = list

@typing.type_check_only
class CloudShellResource(googleapiclient.discovery.Resource):
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
    class UsersResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class EnvironmentsResource(googleapiclient.discovery.Resource):
            def addPublicKey(
                self,
                *,
                environment: str,
                body: AddPublicKeyRequest = ...,
                **kwargs: typing.Any
            ) -> OperationHttpRequest: ...
            def authorize(
                self,
                *,
                name: str,
                body: AuthorizeEnvironmentRequest = ...,
                **kwargs: typing.Any
            ) -> OperationHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> EnvironmentHttpRequest: ...
            def removePublicKey(
                self,
                *,
                environment: str,
                body: RemovePublicKeyRequest = ...,
                **kwargs: typing.Any
            ) -> OperationHttpRequest: ...
            def start(
                self,
                *,
                name: str,
                body: StartEnvironmentRequest = ...,
                **kwargs: typing.Any
            ) -> OperationHttpRequest: ...

        def environments(self) -> EnvironmentsResource: ...

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
    def operations(self) -> OperationsResource: ...
    def users(self) -> UsersResource: ...

@typing.type_check_only
class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Empty: ...

@typing.type_check_only
class EnvironmentHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Environment: ...

@typing.type_check_only
class ListOperationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListOperationsResponse: ...

@typing.type_check_only
class OperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Operation: ...
