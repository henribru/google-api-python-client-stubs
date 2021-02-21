import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *
@typing.type_check_only
class TrafficDirectorServiceResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class DiscoveryResource(googleapiclient.discovery.Resource):
        def client_status(
            self, *, body: ClientStatusRequest = ..., **kwargs: typing.Any
        ) -> ClientStatusResponseHttpRequest: ...
    def discovery(self) -> DiscoveryResource: ...

@typing.type_check_only
class ClientStatusResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> ClientStatusResponse: ...
