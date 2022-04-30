import collections.abc
import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

_list = list

@typing.type_check_only
class SmartDeviceManagementResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class EnterprisesResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class DevicesResource(googleapiclient.discovery.Resource):
            def executeCommand(
                self,
                *,
                name: str,
                body: GoogleHomeEnterpriseSdmV1ExecuteDeviceCommandRequest = ...,
                **kwargs: typing.Any
            ) -> GoogleHomeEnterpriseSdmV1ExecuteDeviceCommandResponseHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleHomeEnterpriseSdmV1DeviceHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                filter: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> GoogleHomeEnterpriseSdmV1ListDevicesResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: GoogleHomeEnterpriseSdmV1ListDevicesResponseHttpRequest,
                previous_response: GoogleHomeEnterpriseSdmV1ListDevicesResponse,
            ) -> GoogleHomeEnterpriseSdmV1ListDevicesResponseHttpRequest | None: ...

        @typing.type_check_only
        class StructuresResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class RoomsResource(googleapiclient.discovery.Resource):
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleHomeEnterpriseSdmV1RoomHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleHomeEnterpriseSdmV1ListRoomsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleHomeEnterpriseSdmV1ListRoomsResponseHttpRequest,
                    previous_response: GoogleHomeEnterpriseSdmV1ListRoomsResponse,
                ) -> GoogleHomeEnterpriseSdmV1ListRoomsResponseHttpRequest | None: ...

            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleHomeEnterpriseSdmV1StructureHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                filter: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> GoogleHomeEnterpriseSdmV1ListStructuresResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: GoogleHomeEnterpriseSdmV1ListStructuresResponseHttpRequest,
                previous_response: GoogleHomeEnterpriseSdmV1ListStructuresResponse,
            ) -> GoogleHomeEnterpriseSdmV1ListStructuresResponseHttpRequest | None: ...
            def rooms(self) -> RoomsResource: ...

        def devices(self) -> DevicesResource: ...
        def structures(self) -> StructuresResource: ...

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
    def enterprises(self) -> EnterprisesResource: ...

@typing.type_check_only
class GoogleHomeEnterpriseSdmV1DeviceHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleHomeEnterpriseSdmV1Device: ...

@typing.type_check_only
class GoogleHomeEnterpriseSdmV1ExecuteDeviceCommandResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleHomeEnterpriseSdmV1ExecuteDeviceCommandResponse: ...

@typing.type_check_only
class GoogleHomeEnterpriseSdmV1ListDevicesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleHomeEnterpriseSdmV1ListDevicesResponse: ...

@typing.type_check_only
class GoogleHomeEnterpriseSdmV1ListRoomsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleHomeEnterpriseSdmV1ListRoomsResponse: ...

@typing.type_check_only
class GoogleHomeEnterpriseSdmV1ListStructuresResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleHomeEnterpriseSdmV1ListStructuresResponse: ...

@typing.type_check_only
class GoogleHomeEnterpriseSdmV1RoomHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleHomeEnterpriseSdmV1Room: ...

@typing.type_check_only
class GoogleHomeEnterpriseSdmV1StructureHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleHomeEnterpriseSdmV1Structure: ...
