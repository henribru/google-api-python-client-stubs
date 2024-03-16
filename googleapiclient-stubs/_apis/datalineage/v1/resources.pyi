import collections.abc
import typing

import httplib2
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http

from .schemas import *

_list = list

@typing.type_check_only
class DatalineageResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class ProjectsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class LocationsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class OperationsResource(googleapiclient.discovery.Resource):
                def cancel(
                    self,
                    *,
                    name: str,
                    body: GoogleLongrunningCancelOperationRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleProtobufEmptyHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleProtobufEmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def list(
                    self,
                    *,
                    name: str,
                    filter: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningListOperationsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleLongrunningListOperationsResponseHttpRequest,
                    previous_response: GoogleLongrunningListOperationsResponse,
                ) -> GoogleLongrunningListOperationsResponseHttpRequest | None: ...

            @typing.type_check_only
            class ProcessesResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class RunsResource(googleapiclient.discovery.Resource):
                    @typing.type_check_only
                    class LineageEventsResource(googleapiclient.discovery.Resource):
                        def create(
                            self,
                            *,
                            parent: str,
                            body: GoogleCloudDatacatalogLineageV1LineageEvent = ...,
                            requestId: str = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudDatacatalogLineageV1LineageEventHttpRequest: ...
                        def delete(
                            self,
                            *,
                            name: str,
                            allowMissing: bool = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleProtobufEmptyHttpRequest: ...
                        def get(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> GoogleCloudDatacatalogLineageV1LineageEventHttpRequest: ...
                        def list(
                            self,
                            *,
                            parent: str,
                            pageSize: int = ...,
                            pageToken: str = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudDatacatalogLineageV1ListLineageEventsResponseHttpRequest: ...
                        def list_next(
                            self,
                            previous_request: GoogleCloudDatacatalogLineageV1ListLineageEventsResponseHttpRequest,
                            previous_response: GoogleCloudDatacatalogLineageV1ListLineageEventsResponse,
                        ) -> (
                            GoogleCloudDatacatalogLineageV1ListLineageEventsResponseHttpRequest
                            | None
                        ): ...

                    def create(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudDatacatalogLineageV1Run = ...,
                        requestId: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudDatacatalogLineageV1RunHttpRequest: ...
                    def delete(
                        self,
                        *,
                        name: str,
                        allowMissing: bool = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleCloudDatacatalogLineageV1RunHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudDatacatalogLineageV1ListRunsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudDatacatalogLineageV1ListRunsResponseHttpRequest,
                        previous_response: GoogleCloudDatacatalogLineageV1ListRunsResponse,
                    ) -> (
                        GoogleCloudDatacatalogLineageV1ListRunsResponseHttpRequest
                        | None
                    ): ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudDatacatalogLineageV1Run = ...,
                        allowMissing: bool = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudDatacatalogLineageV1RunHttpRequest: ...
                    def lineageEvents(self) -> LineageEventsResource: ...

                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudDatacatalogLineageV1Process = ...,
                    requestId: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudDatacatalogLineageV1ProcessHttpRequest: ...
                def delete(
                    self, *, name: str, allowMissing: bool = ..., **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudDatacatalogLineageV1ProcessHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> (
                    GoogleCloudDatacatalogLineageV1ListProcessesResponseHttpRequest
                ): ...
                def list_next(
                    self,
                    previous_request: GoogleCloudDatacatalogLineageV1ListProcessesResponseHttpRequest,
                    previous_response: GoogleCloudDatacatalogLineageV1ListProcessesResponse,
                ) -> (
                    GoogleCloudDatacatalogLineageV1ListProcessesResponseHttpRequest
                    | None
                ): ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudDatacatalogLineageV1Process = ...,
                    allowMissing: bool = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudDatacatalogLineageV1ProcessHttpRequest: ...
                def runs(self) -> RunsResource: ...

            def batchSearchLinkProcesses(
                self,
                *,
                parent: str,
                body: GoogleCloudDatacatalogLineageV1BatchSearchLinkProcessesRequest = ...,
                **kwargs: typing.Any,
            ) -> GoogleCloudDatacatalogLineageV1BatchSearchLinkProcessesResponseHttpRequest: ...
            def batchSearchLinkProcesses_next(
                self,
                previous_request: GoogleCloudDatacatalogLineageV1BatchSearchLinkProcessesResponseHttpRequest,
                previous_response: GoogleCloudDatacatalogLineageV1BatchSearchLinkProcessesResponse,
            ) -> (
                GoogleCloudDatacatalogLineageV1BatchSearchLinkProcessesResponseHttpRequest
                | None
            ): ...
            def processOpenLineageRunEvent(
                self,
                *,
                parent: str,
                body: dict[str, typing.Any] = ...,
                requestId: str = ...,
                **kwargs: typing.Any,
            ) -> GoogleCloudDatacatalogLineageV1ProcessOpenLineageRunEventResponseHttpRequest: ...
            def searchLinks(
                self,
                *,
                parent: str,
                body: GoogleCloudDatacatalogLineageV1SearchLinksRequest = ...,
                **kwargs: typing.Any,
            ) -> GoogleCloudDatacatalogLineageV1SearchLinksResponseHttpRequest: ...
            def searchLinks_next(
                self,
                previous_request: GoogleCloudDatacatalogLineageV1SearchLinksResponseHttpRequest,
                previous_response: GoogleCloudDatacatalogLineageV1SearchLinksResponse,
            ) -> (
                GoogleCloudDatacatalogLineageV1SearchLinksResponseHttpRequest | None
            ): ...
            def operations(self) -> OperationsResource: ...
            def processes(self) -> ProcessesResource: ...

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
class GoogleCloudDatacatalogLineageV1BatchSearchLinkProcessesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDatacatalogLineageV1BatchSearchLinkProcessesResponse: ...

@typing.type_check_only
class GoogleCloudDatacatalogLineageV1LineageEventHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDatacatalogLineageV1LineageEvent: ...

@typing.type_check_only
class GoogleCloudDatacatalogLineageV1ListLineageEventsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDatacatalogLineageV1ListLineageEventsResponse: ...

@typing.type_check_only
class GoogleCloudDatacatalogLineageV1ListProcessesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDatacatalogLineageV1ListProcessesResponse: ...

@typing.type_check_only
class GoogleCloudDatacatalogLineageV1ListRunsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDatacatalogLineageV1ListRunsResponse: ...

@typing.type_check_only
class GoogleCloudDatacatalogLineageV1ProcessHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDatacatalogLineageV1Process: ...

@typing.type_check_only
class GoogleCloudDatacatalogLineageV1ProcessOpenLineageRunEventResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDatacatalogLineageV1ProcessOpenLineageRunEventResponse: ...

@typing.type_check_only
class GoogleCloudDatacatalogLineageV1RunHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDatacatalogLineageV1Run: ...

@typing.type_check_only
class GoogleCloudDatacatalogLineageV1SearchLinksResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDatacatalogLineageV1SearchLinksResponse: ...

@typing.type_check_only
class GoogleLongrunningListOperationsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleLongrunningListOperationsResponse: ...

@typing.type_check_only
class GoogleLongrunningOperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleLongrunningOperation: ...

@typing.type_check_only
class GoogleProtobufEmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleProtobufEmpty: ...
