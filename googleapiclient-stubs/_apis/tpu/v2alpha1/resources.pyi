import collections.abc
import typing

import httplib2
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http

from .schemas import *

_list = list

@typing.type_check_only
class TPUResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class ProjectsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class LocationsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class AcceleratorTypesResource(googleapiclient.discovery.Resource):
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> AcceleratorTypeHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> ListAcceleratorTypesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListAcceleratorTypesResponseHttpRequest,
                    previous_response: ListAcceleratorTypesResponse,
                ) -> ListAcceleratorTypesResponseHttpRequest | None: ...

            @typing.type_check_only
            class NodesResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: Node = ...,
                    nodeId: str = ...,
                    requestId: str = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def delete(
                    self, *, name: str, requestId: str = ..., **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> NodeHttpRequest: ...
                def getGuestAttributes(
                    self,
                    *,
                    name: str,
                    body: GetGuestAttributesRequest = ...,
                    **kwargs: typing.Any,
                ) -> GetGuestAttributesResponseHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> ListNodesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListNodesResponseHttpRequest,
                    previous_response: ListNodesResponse,
                ) -> ListNodesResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: Node = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def performMaintenance(
                    self,
                    *,
                    name: str,
                    body: PerformMaintenanceRequest = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def simulateMaintenanceEvent(
                    self,
                    *,
                    name: str,
                    body: SimulateMaintenanceEventRequest = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def start(
                    self,
                    *,
                    name: str,
                    body: StartNodeRequest = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def stop(
                    self,
                    *,
                    name: str,
                    body: StopNodeRequest = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...

            @typing.type_check_only
            class OperationsResource(googleapiclient.discovery.Resource):
                def cancel(
                    self, *, name: str, **kwargs: typing.Any
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
                    **kwargs: typing.Any,
                ) -> ListOperationsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListOperationsResponseHttpRequest,
                    previous_response: ListOperationsResponse,
                ) -> ListOperationsResponseHttpRequest | None: ...

            @typing.type_check_only
            class QueuedResourcesResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: QueuedResource = ...,
                    queuedResourceId: str = ...,
                    requestId: str = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def delete(
                    self,
                    *,
                    name: str,
                    force: bool = ...,
                    requestId: str = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> QueuedResourceHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> ListQueuedResourcesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListQueuedResourcesResponseHttpRequest,
                    previous_response: ListQueuedResourcesResponse,
                ) -> ListQueuedResourcesResponseHttpRequest | None: ...
                def performMaintenanceQueuedResource(
                    self,
                    *,
                    name: str,
                    body: PerformMaintenanceQueuedResourceRequest = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def reset(
                    self,
                    *,
                    name: str,
                    body: ResetQueuedResourceRequest = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...

            @typing.type_check_only
            class ReservationsResource(googleapiclient.discovery.Resource):
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> ListReservationsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListReservationsResponseHttpRequest,
                    previous_response: ListReservationsResponse,
                ) -> ListReservationsResponseHttpRequest | None: ...

            @typing.type_check_only
            class RuntimeVersionsResource(googleapiclient.discovery.Resource):
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> RuntimeVersionHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> ListRuntimeVersionsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListRuntimeVersionsResponseHttpRequest,
                    previous_response: ListRuntimeVersionsResponse,
                ) -> ListRuntimeVersionsResponseHttpRequest | None: ...

            def generateServiceIdentity(
                self,
                *,
                parent: str,
                body: GenerateServiceIdentityRequest = ...,
                **kwargs: typing.Any,
            ) -> GenerateServiceIdentityResponseHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> LocationHttpRequest: ...
            def list(
                self,
                *,
                name: str,
                extraLocationTypes: str | _list[str] = ...,
                filter: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any,
            ) -> ListLocationsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListLocationsResponseHttpRequest,
                previous_response: ListLocationsResponse,
            ) -> ListLocationsResponseHttpRequest | None: ...
            def acceleratorTypes(self) -> AcceleratorTypesResource: ...
            def nodes(self) -> NodesResource: ...
            def operations(self) -> OperationsResource: ...
            def queuedResources(self) -> QueuedResourcesResource: ...
            def reservations(self) -> ReservationsResource: ...
            def runtimeVersions(self) -> RuntimeVersionsResource: ...

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
        | None = None,
    ) -> googleapiclient.http.BatchHttpRequest: ...
    def projects(self) -> ProjectsResource: ...

@typing.type_check_only
class AcceleratorTypeHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> AcceleratorType: ...

@typing.type_check_only
class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Empty: ...

@typing.type_check_only
class GenerateServiceIdentityResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GenerateServiceIdentityResponse: ...

@typing.type_check_only
class GetGuestAttributesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GetGuestAttributesResponse: ...

@typing.type_check_only
class ListAcceleratorTypesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListAcceleratorTypesResponse: ...

@typing.type_check_only
class ListLocationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListLocationsResponse: ...

@typing.type_check_only
class ListNodesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListNodesResponse: ...

@typing.type_check_only
class ListOperationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListOperationsResponse: ...

@typing.type_check_only
class ListQueuedResourcesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListQueuedResourcesResponse: ...

@typing.type_check_only
class ListReservationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListReservationsResponse: ...

@typing.type_check_only
class ListRuntimeVersionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListRuntimeVersionsResponse: ...

@typing.type_check_only
class LocationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Location: ...

@typing.type_check_only
class NodeHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Node: ...

@typing.type_check_only
class OperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Operation: ...

@typing.type_check_only
class QueuedResourceHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> QueuedResource: ...

@typing.type_check_only
class RuntimeVersionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> RuntimeVersion: ...
