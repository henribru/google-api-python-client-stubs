import collections.abc
import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

_list = list

@typing.type_check_only
class IAMCredentialsResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class ProjectsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class ServiceAccountsResource(googleapiclient.discovery.Resource):
            def generateAccessToken(
                self,
                *,
                name: str,
                body: GenerateAccessTokenRequest = ...,
                **kwargs: typing.Any
            ) -> GenerateAccessTokenResponseHttpRequest: ...
            def generateIdToken(
                self,
                *,
                name: str,
                body: GenerateIdTokenRequest = ...,
                **kwargs: typing.Any
            ) -> GenerateIdTokenResponseHttpRequest: ...
            def signBlob(
                self, *, name: str, body: SignBlobRequest = ..., **kwargs: typing.Any
            ) -> SignBlobResponseHttpRequest: ...
            def signJwt(
                self, *, name: str, body: SignJwtRequest = ..., **kwargs: typing.Any
            ) -> SignJwtResponseHttpRequest: ...

        def serviceAccounts(self) -> ServiceAccountsResource: ...

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
class GenerateAccessTokenResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GenerateAccessTokenResponse: ...

@typing.type_check_only
class GenerateIdTokenResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GenerateIdTokenResponse: ...

@typing.type_check_only
class SignBlobResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> SignBlobResponse: ...

@typing.type_check_only
class SignJwtResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> SignJwtResponse: ...
