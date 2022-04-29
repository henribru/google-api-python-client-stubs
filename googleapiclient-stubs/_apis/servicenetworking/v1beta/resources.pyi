import collections.abc
import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

_list = list

@typing.type_check_only
class ServiceNetworkingResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class OperationsResource(googleapiclient.discovery.Resource):
        def get(self, *, name: str, **kwargs: typing.Any) -> OperationHttpRequest: ...

    @typing.type_check_only
    class ServicesResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class ConnectionsResource(googleapiclient.discovery.Resource):
            def create(
                self,
                *,
                parent: str,
                body: GoogleCloudServicenetworkingV1betaConnection = ...,
                **kwargs: typing.Any
            ) -> OperationHttpRequest: ...
            def list(
                self, *, parent: str, network: str = ..., **kwargs: typing.Any
            ) -> ListConnectionsResponseHttpRequest: ...

        def addSubnetwork(
            self, *, parent: str, body: AddSubnetworkRequest = ..., **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def searchRange(
            self, *, parent: str, body: SearchRangeRequest = ..., **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def updateConnections(
            self,
            *,
            name: str,
            body: GoogleCloudServicenetworkingV1betaConnection = ...,
            force: bool = ...,
            updateMask: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def connections(self) -> ConnectionsResource: ...

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
    def operations(self) -> OperationsResource: ...
    def services(self) -> ServicesResource: ...

@typing.type_check_only
class ListConnectionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListConnectionsResponse: ...

@typing.type_check_only
class OperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Operation: ...
