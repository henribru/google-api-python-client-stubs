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
    class UsersResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class EnvironmentsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class PublicKeysResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: CreatePublicKeyRequest = ...,
                    **kwargs: typing.Any
                ) -> PublicKeyHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...

            def authorize(
                self,
                *,
                name: str,
                body: AuthorizeEnvironmentRequest = ...,
                **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> EnvironmentHttpRequest: ...
            def patch(
                self,
                *,
                name: str,
                body: Environment = ...,
                updateMask: str = ...,
                **kwargs: typing.Any
            ) -> EnvironmentHttpRequest: ...
            def start(
                self,
                *,
                name: str,
                body: StartEnvironmentRequest = ...,
                **kwargs: typing.Any
            ) -> OperationHttpRequest: ...
            def publicKeys(self) -> PublicKeysResource: ...

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
class OperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Operation: ...

@typing.type_check_only
class PublicKeyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> PublicKey: ...
