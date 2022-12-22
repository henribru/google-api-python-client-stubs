import collections.abc
import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

_list = list

@typing.type_check_only
class CloudSecurityTokenResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class V1Resource(googleapiclient.discovery.Resource):
        def introspect(
            self,
            *,
            body: GoogleIdentityStsV1IntrospectTokenRequest = ...,
            **kwargs: typing.Any
        ) -> GoogleIdentityStsV1IntrospectTokenResponseHttpRequest: ...
        def oauthtoken(
            self,
            *,
            body: GoogleIdentityStsV1ExchangeOauthTokenRequest = ...,
            **kwargs: typing.Any
        ) -> GoogleIdentityStsV1ExchangeOauthTokenResponseHttpRequest: ...
        def token(
            self,
            *,
            body: GoogleIdentityStsV1ExchangeTokenRequest = ...,
            **kwargs: typing.Any
        ) -> GoogleIdentityStsV1ExchangeTokenResponseHttpRequest: ...

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
    def v1(self) -> V1Resource: ...

@typing.type_check_only
class GoogleIdentityStsV1ExchangeOauthTokenResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleIdentityStsV1ExchangeOauthTokenResponse: ...

@typing.type_check_only
class GoogleIdentityStsV1ExchangeTokenResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleIdentityStsV1ExchangeTokenResponse: ...

@typing.type_check_only
class GoogleIdentityStsV1IntrospectTokenResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleIdentityStsV1IntrospectTokenResponse: ...
