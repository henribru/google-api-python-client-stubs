import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class SiteVerificationResource(googleapiclient.discovery.Resource):
    class WebResourceResource(googleapiclient.discovery.Resource):
        def get(
            self, *, id: str, **kwargs: typing.Any
        ) -> SiteVerificationWebResourceResourceHttpRequest: ...
        def delete(
            self, *, id: str, **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def getToken(
            self,
            *,
            body: SiteVerificationWebResourceGettokenRequest = ...,
            **kwargs: typing.Any
        ) -> SiteVerificationWebResourceGettokenResponseHttpRequest: ...
        def update(
            self,
            *,
            id: str,
            body: SiteVerificationWebResourceResource = ...,
            **kwargs: typing.Any
        ) -> SiteVerificationWebResourceResourceHttpRequest: ...
        def patch(
            self,
            *,
            id: str,
            body: SiteVerificationWebResourceResource = ...,
            **kwargs: typing.Any
        ) -> SiteVerificationWebResourceResourceHttpRequest: ...
        def list(
            self, **kwargs: typing.Any
        ) -> SiteVerificationWebResourceListResponseHttpRequest: ...
        def insert(
            self,
            *,
            verificationMethod: str,
            body: SiteVerificationWebResourceResource = ...,
            **kwargs: typing.Any
        ) -> SiteVerificationWebResourceResourceHttpRequest: ...
    def webResource(self) -> WebResourceResource: ...

class SiteVerificationWebResourceResourceHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> SiteVerificationWebResourceResource: ...

class SiteVerificationWebResourceListResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> SiteVerificationWebResourceListResponse: ...

class SiteVerificationWebResourceGettokenResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> SiteVerificationWebResourceGettokenResponse: ...
