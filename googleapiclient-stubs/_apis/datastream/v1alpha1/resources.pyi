import collections.abc
import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

_list = list

@typing.type_check_only
class DatastreamResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class ProjectsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class LocationsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class ConnectionProfilesResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: ConnectionProfile = ...,
                    connectionProfileId: str = ...,
                    requestId: str = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def delete(
                    self, *, name: str, requestId: str = ..., **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def discover(
                    self,
                    *,
                    parent: str,
                    body: DiscoverConnectionProfileRequest = ...,
                    **kwargs: typing.Any
                ) -> DiscoverConnectionProfileResponseHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> ConnectionProfileHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> ListConnectionProfilesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListConnectionProfilesResponseHttpRequest,
                    previous_response: ListConnectionProfilesResponse,
                ) -> ListConnectionProfilesResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: ConnectionProfile = ...,
                    requestId: str = ...,
                    updateMask: str = ...,
                    validateOnly: bool = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...

            @typing.type_check_only
            class OperationsResource(googleapiclient.discovery.Resource):
                def cancel(
                    self,
                    *,
                    name: str,
                    body: CancelOperationRequest = ...,
                    **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def list(
                    self,
                    *,
                    name: str,
                    filter: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> ListOperationsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListOperationsResponseHttpRequest,
                    previous_response: ListOperationsResponse,
                ) -> ListOperationsResponseHttpRequest | None: ...

            @typing.type_check_only
            class PrivateConnectionsResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class RoutesResource(googleapiclient.discovery.Resource):
                    def create(
                        self,
                        *,
                        parent: str,
                        body: Route = ...,
                        requestId: str = ...,
                        routeId: str = ...,
                        **kwargs: typing.Any
                    ) -> OperationHttpRequest: ...
                    def delete(
                        self, *, name: str, requestId: str = ..., **kwargs: typing.Any
                    ) -> OperationHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> RouteHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str = ...,
                        orderBy: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any
                    ) -> ListRoutesResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: ListRoutesResponseHttpRequest,
                        previous_response: ListRoutesResponse,
                    ) -> ListRoutesResponseHttpRequest | None: ...

                def create(
                    self,
                    *,
                    parent: str,
                    body: PrivateConnection = ...,
                    privateConnectionId: str = ...,
                    requestId: str = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def delete(
                    self,
                    *,
                    name: str,
                    force: bool = ...,
                    requestId: str = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> PrivateConnectionHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> ListPrivateConnectionsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListPrivateConnectionsResponseHttpRequest,
                    previous_response: ListPrivateConnectionsResponse,
                ) -> ListPrivateConnectionsResponseHttpRequest | None: ...
                def routes(self) -> RoutesResource: ...

            @typing.type_check_only
            class StreamsResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class ObjectsResource(googleapiclient.discovery.Resource):
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> StreamObjectHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any
                    ) -> ListStreamObjectsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: ListStreamObjectsResponseHttpRequest,
                        previous_response: ListStreamObjectsResponse,
                    ) -> ListStreamObjectsResponseHttpRequest | None: ...
                    def startBackfillJob(
                        self, *, object: str, **kwargs: typing.Any
                    ) -> StartBackfillJobResponseHttpRequest: ...
                    def stopBackfillJob(
                        self, *, object: str, **kwargs: typing.Any
                    ) -> StopBackfillJobResponseHttpRequest: ...

                def create(
                    self,
                    *,
                    parent: str,
                    body: Stream = ...,
                    force: bool = ...,
                    requestId: str = ...,
                    streamId: str = ...,
                    validateOnly: bool = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def delete(
                    self, *, name: str, requestId: str = ..., **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def fetchErrors(
                    self,
                    *,
                    stream: str,
                    body: FetchErrorsRequest = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> StreamHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> ListStreamsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListStreamsResponseHttpRequest,
                    previous_response: ListStreamsResponse,
                ) -> ListStreamsResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: Stream = ...,
                    force: bool = ...,
                    requestId: str = ...,
                    updateMask: str = ...,
                    validateOnly: bool = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def objects(self) -> ObjectsResource: ...

            def fetchStaticIps(
                self,
                *,
                name: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> FetchStaticIpsResponseHttpRequest: ...
            def fetchStaticIps_next(
                self,
                previous_request: FetchStaticIpsResponseHttpRequest,
                previous_response: FetchStaticIpsResponse,
            ) -> FetchStaticIpsResponseHttpRequest | None: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> LocationHttpRequest: ...
            def list(
                self,
                *,
                name: str,
                filter: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> ListLocationsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListLocationsResponseHttpRequest,
                previous_response: ListLocationsResponse,
            ) -> ListLocationsResponseHttpRequest | None: ...
            def connectionProfiles(self) -> ConnectionProfilesResource: ...
            def operations(self) -> OperationsResource: ...
            def privateConnections(self) -> PrivateConnectionsResource: ...
            def streams(self) -> StreamsResource: ...

        def locations(self) -> LocationsResource: ...

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
    def projects(self) -> ProjectsResource: ...

@typing.type_check_only
class ConnectionProfileHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ConnectionProfile: ...

@typing.type_check_only
class DiscoverConnectionProfileResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> DiscoverConnectionProfileResponse: ...

@typing.type_check_only
class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Empty: ...

@typing.type_check_only
class FetchStaticIpsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> FetchStaticIpsResponse: ...

@typing.type_check_only
class ListConnectionProfilesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListConnectionProfilesResponse: ...

@typing.type_check_only
class ListLocationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListLocationsResponse: ...

@typing.type_check_only
class ListOperationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListOperationsResponse: ...

@typing.type_check_only
class ListPrivateConnectionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListPrivateConnectionsResponse: ...

@typing.type_check_only
class ListRoutesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListRoutesResponse: ...

@typing.type_check_only
class ListStreamObjectsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListStreamObjectsResponse: ...

@typing.type_check_only
class ListStreamsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListStreamsResponse: ...

@typing.type_check_only
class LocationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Location: ...

@typing.type_check_only
class OperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Operation: ...

@typing.type_check_only
class PrivateConnectionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> PrivateConnection: ...

@typing.type_check_only
class RouteHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Route: ...

@typing.type_check_only
class StartBackfillJobResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> StartBackfillJobResponse: ...

@typing.type_check_only
class StopBackfillJobResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> StopBackfillJobResponse: ...

@typing.type_check_only
class StreamHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Stream: ...

@typing.type_check_only
class StreamObjectHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> StreamObject: ...
