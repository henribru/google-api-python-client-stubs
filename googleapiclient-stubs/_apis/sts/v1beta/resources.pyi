import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class CloudSecurityTokenResource(googleapiclient.discovery.Resource):
    class V1betaResource(googleapiclient.discovery.Resource):
        def token(
            self,
            *,
            body: GoogleIdentityStsV1betaExchangeTokenRequest = ...,
            **kwargs: typing.Any
        ) -> GoogleIdentityStsV1betaExchangeTokenResponseHttpRequest: ...
    def v1beta(self) -> V1betaResource: ...

class GoogleIdentityStsV1betaExchangeTokenResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleIdentityStsV1betaExchangeTokenResponse: ...
