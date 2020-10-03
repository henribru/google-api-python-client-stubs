import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class TrafficDirectorServiceResource(googleapiclient.discovery.Resource):
    class DiscoveryResource(googleapiclient.discovery.Resource):
        def client_status(
            self, *, body: ClientStatusRequest = ..., **kwargs: typing.Any
        ) -> ClientStatusResponseHttpRequest: ...
    def discovery(self) -> DiscoveryResource: ...

class ClientStatusResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ClientStatusResponse: ...
