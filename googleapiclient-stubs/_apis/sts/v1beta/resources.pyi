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
    class V1betaResource(googleapiclient.discovery.Resource):
        def token(
            self,
            *,
            body: GoogleIdentityStsV1betaExchangeTokenRequest = ...,
            **kwargs: typing.Any
        ) -> GoogleIdentityStsV1betaExchangeTokenResponseHttpRequest: ...

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
    def v1beta(self) -> V1betaResource: ...

@typing.type_check_only
class GoogleIdentityStsV1betaExchangeTokenResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleIdentityStsV1betaExchangeTokenResponse: ...
