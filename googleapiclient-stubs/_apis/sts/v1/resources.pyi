import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *
@typing.type_check_only
class CloudSecurityTokenResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class V1Resource(googleapiclient.discovery.Resource):
        def token(
            self,
            *,
            body: GoogleIdentityStsV1ExchangeTokenRequest = ...,
            **kwargs: typing.Any
        ) -> GoogleIdentityStsV1ExchangeTokenResponseHttpRequest: ...
    def v1(self) -> V1Resource: ...

@typing.type_check_only
class GoogleIdentityStsV1ExchangeTokenResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleIdentityStsV1ExchangeTokenResponse: ...
