import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class CloudSecurityTokenResource(googleapiclient.discovery.Resource):
    class V1Resource(googleapiclient.discovery.Resource):
        def token(
            self,
            *,
            body: GoogleIdentityStsV1ExchangeTokenRequest = ...,
            **kwargs: typing.Any
        ) -> GoogleIdentityStsV1ExchangeTokenResponseHttpRequest: ...
    def v1(self) -> V1Resource: ...

class GoogleIdentityStsV1ExchangeTokenResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleIdentityStsV1ExchangeTokenResponse: ...
