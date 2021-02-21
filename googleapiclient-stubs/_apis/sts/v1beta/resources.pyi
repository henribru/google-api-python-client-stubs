import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *
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
    def v1beta(self) -> V1betaResource: ...

@typing.type_check_only
class GoogleIdentityStsV1betaExchangeTokenResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleIdentityStsV1betaExchangeTokenResponse: ...
