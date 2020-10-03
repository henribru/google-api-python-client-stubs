import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class SmartDeviceManagementResource(googleapiclient.discovery.Resource):
    class EnterprisesResource(googleapiclient.discovery.Resource):
        class StructuresResource(googleapiclient.discovery.Resource):
            class RoomsResource(googleapiclient.discovery.Resource):
                def list(
                    self,
                    *,
                    parent: str,
                    pageToken: str = ...,
                    pageSize: int = ...,
                    **kwargs: typing.Any
                ) -> GoogleHomeEnterpriseSdmV1ListRoomsResponseHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleHomeEnterpriseSdmV1RoomHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleHomeEnterpriseSdmV1StructureHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                filter: str = ...,
                pageToken: str = ...,
                pageSize: int = ...,
                **kwargs: typing.Any
            ) -> GoogleHomeEnterpriseSdmV1ListStructuresResponseHttpRequest: ...
            def rooms(self) -> RoomsResource: ...
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
                view: typing_extensions.Literal[
                    "DEVICE_DETAILS_VIEW_UNSPECIFIED", "DEVICE_CONSOLE_VIEW"
                ] = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> GoogleHomeEnterpriseSdmV1ListDevicesResponseHttpRequest: ...
        def structures(self) -> StructuresResource: ...
        def devices(self) -> DevicesResource: ...
    def enterprises(self) -> EnterprisesResource: ...

class GoogleHomeEnterpriseSdmV1StructureHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleHomeEnterpriseSdmV1Structure: ...

class GoogleHomeEnterpriseSdmV1DeviceHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleHomeEnterpriseSdmV1Device: ...

class GoogleHomeEnterpriseSdmV1RoomHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleHomeEnterpriseSdmV1Room: ...

class GoogleHomeEnterpriseSdmV1ListRoomsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleHomeEnterpriseSdmV1ListRoomsResponse: ...

class GoogleHomeEnterpriseSdmV1ListStructuresResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleHomeEnterpriseSdmV1ListStructuresResponse: ...

class GoogleHomeEnterpriseSdmV1ListDevicesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleHomeEnterpriseSdmV1ListDevicesResponse: ...

class GoogleHomeEnterpriseSdmV1ExecuteDeviceCommandResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleHomeEnterpriseSdmV1ExecuteDeviceCommandResponse: ...
