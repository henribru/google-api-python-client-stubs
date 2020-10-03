import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class IAMCredentialsResource(googleapiclient.discovery.Resource):
    class ProjectsResource(googleapiclient.discovery.Resource):
        class ServiceAccountsResource(googleapiclient.discovery.Resource):
            def generateAccessToken(
                self,
                *,
                name: str,
                body: GenerateAccessTokenRequest = ...,
                **kwargs: typing.Any
            ) -> GenerateAccessTokenResponseHttpRequest: ...
            def signJwt(
                self, *, name: str, body: SignJwtRequest = ..., **kwargs: typing.Any
            ) -> SignJwtResponseHttpRequest: ...
            def signBlob(
                self, *, name: str, body: SignBlobRequest = ..., **kwargs: typing.Any
            ) -> SignBlobResponseHttpRequest: ...
            def generateIdToken(
                self,
                *,
                name: str,
                body: GenerateIdTokenRequest = ...,
                **kwargs: typing.Any
            ) -> GenerateIdTokenResponseHttpRequest: ...
        def serviceAccounts(self) -> ServiceAccountsResource: ...
    def projects(self) -> ProjectsResource: ...

class GenerateAccessTokenResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GenerateAccessTokenResponse: ...

class SignBlobResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> SignBlobResponse: ...

class GenerateIdTokenResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GenerateIdTokenResponse: ...

class SignJwtResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> SignJwtResponse: ...
