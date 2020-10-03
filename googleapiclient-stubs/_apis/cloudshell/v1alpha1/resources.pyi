import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class CloudShellResource(googleapiclient.discovery.Resource):
    class UsersResource(googleapiclient.discovery.Resource):
        class EnvironmentsResource(googleapiclient.discovery.Resource):
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
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> EnvironmentHttpRequest: ...
            def authorize(
                self,
                *,
                name: str,
                body: AuthorizeEnvironmentRequest = ...,
                **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
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
    def users(self) -> UsersResource: ...

class OperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Operation: ...

class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Empty: ...

class EnvironmentHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Environment: ...

class PublicKeyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> PublicKey: ...
