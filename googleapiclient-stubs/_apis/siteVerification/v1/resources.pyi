import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *
@typing.type_check_only
class SiteVerificationResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class WebResourceResource(googleapiclient.discovery.Resource):
        def delete(
            self, *, id: str, **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def get(
            self, *, id: str, **kwargs: typing.Any
        ) -> SiteVerificationWebResourceResourceHttpRequest: ...
        def getToken(
            self,
            *,
            body: SiteVerificationWebResourceGettokenRequest = ...,
            **kwargs: typing.Any
        ) -> SiteVerificationWebResourceGettokenResponseHttpRequest: ...
        def insert(
            self,
            *,
            verificationMethod: str,
            body: SiteVerificationWebResourceResource = ...,
            **kwargs: typing.Any
        ) -> SiteVerificationWebResourceResourceHttpRequest: ...
        def list(
            self, **kwargs: typing.Any
        ) -> SiteVerificationWebResourceListResponseHttpRequest: ...
        def patch(
            self,
            *,
            id: str,
            body: SiteVerificationWebResourceResource = ...,
            **kwargs: typing.Any
        ) -> SiteVerificationWebResourceResourceHttpRequest: ...
        def update(
            self,
            *,
            id: str,
            body: SiteVerificationWebResourceResource = ...,
            **kwargs: typing.Any
        ) -> SiteVerificationWebResourceResourceHttpRequest: ...
    def webResource(self) -> WebResourceResource: ...

@typing.type_check_only
class SiteVerificationWebResourceGettokenResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> SiteVerificationWebResourceGettokenResponse: ...

@typing.type_check_only
class SiteVerificationWebResourceListResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> SiteVerificationWebResourceListResponse: ...

@typing.type_check_only
class SiteVerificationWebResourceResourceHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> SiteVerificationWebResourceResource: ...
