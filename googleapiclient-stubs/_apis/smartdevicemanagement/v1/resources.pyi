import collections.abc
import typing

import httplib2
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http

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
                **kwargs: typing.Any,
            ) -> GoogleHomeEnterpriseSdmV1ExecuteDeviceCommandResponseHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleHomeEnterpriseSdmV1DeviceHttpRequest: ...
            def list(
                self, *, parent: str, filter: str = ..., **kwargs: typing.Any
            ) -> GoogleHomeEnterpriseSdmV1ListDevicesResponseHttpRequest: ...

        @typing.type_check_only
        class StructuresResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class RoomsResource(googleapiclient.discovery.Resource):
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleHomeEnterpriseSdmV1RoomHttpRequest: ...
                def list(
                    self, *, parent: str, **kwargs: typing.Any
                ) -> GoogleHomeEnterpriseSdmV1ListRoomsResponseHttpRequest: ...

            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleHomeEnterpriseSdmV1StructureHttpRequest: ...
            def list(
                self, *, parent: str, filter: str = ..., **kwargs: typing.Any
            ) -> GoogleHomeEnterpriseSdmV1ListStructuresResponseHttpRequest: ...
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
        | None = None,
    ) -> googleapiclient.http.BatchHttpRequest: ...
    def enterprises(self) -> EnterprisesResource: ...

@typing.type_check_only
class GoogleHomeEnterpriseSdmV1DeviceHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleHomeEnterpriseSdmV1Device: ...

@typing.type_check_only
class GoogleHomeEnterpriseSdmV1ExecuteDeviceCommandResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleHomeEnterpriseSdmV1ExecuteDeviceCommandResponse: ...

@typing.type_check_only
class GoogleHomeEnterpriseSdmV1ListDevicesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleHomeEnterpriseSdmV1ListDevicesResponse: ...

@typing.type_check_only
class GoogleHomeEnterpriseSdmV1ListRoomsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleHomeEnterpriseSdmV1ListRoomsResponse: ...

@typing.type_check_only
class GoogleHomeEnterpriseSdmV1ListStructuresResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleHomeEnterpriseSdmV1ListStructuresResponse: ...

@typing.type_check_only
class GoogleHomeEnterpriseSdmV1RoomHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleHomeEnterpriseSdmV1Room: ...

@typing.type_check_only
class GoogleHomeEnterpriseSdmV1StructureHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleHomeEnterpriseSdmV1Structure: ...
