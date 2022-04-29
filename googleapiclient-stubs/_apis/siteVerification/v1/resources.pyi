import collections.abc
import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

_list = list

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
    def webResource(self) -> WebResourceResource: ...

@typing.type_check_only
class SiteVerificationWebResourceGettokenResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> SiteVerificationWebResourceGettokenResponse: ...

@typing.type_check_only
class SiteVerificationWebResourceListResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> SiteVerificationWebResourceListResponse: ...

@typing.type_check_only
class SiteVerificationWebResourceResourceHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> SiteVerificationWebResourceResource: ...
