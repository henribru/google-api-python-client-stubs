import collections.abc
import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

_list = list

@typing.type_check_only
class ChromeManagementResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class CustomersResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class AppsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class AndroidResource(googleapiclient.discovery.Resource):
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleChromeManagementV1AppDetailsHttpRequest: ...

            @typing.type_check_only
            class ChromeResource(googleapiclient.discovery.Resource):
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleChromeManagementV1AppDetailsHttpRequest: ...

            @typing.type_check_only
            class WebResource(googleapiclient.discovery.Resource):
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleChromeManagementV1AppDetailsHttpRequest: ...

            def countChromeAppRequests(
                self,
                *,
                customer: str,
                orderBy: str = ...,
                orgUnitId: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> GoogleChromeManagementV1CountChromeAppRequestsResponseHttpRequest: ...
            def countChromeAppRequests_next(
                self,
                previous_request: GoogleChromeManagementV1CountChromeAppRequestsResponseHttpRequest,
                previous_response: GoogleChromeManagementV1CountChromeAppRequestsResponse,
            ) -> GoogleChromeManagementV1CountChromeAppRequestsResponseHttpRequest | None: ...
            def android(self) -> AndroidResource: ...
            def chrome(self) -> ChromeResource: ...
            def web(self) -> WebResource: ...

        @typing.type_check_only
        class ReportsResource(googleapiclient.discovery.Resource):
            def countChromeDevicesReachingAutoExpirationDate(
                self,
                *,
                customer: str,
                maxAueDate: str = ...,
                minAueDate: str = ...,
                orgUnitId: str = ...,
                **kwargs: typing.Any
            ) -> GoogleChromeManagementV1CountChromeDevicesReachingAutoExpirationDateResponseHttpRequest: ...
            def countChromeDevicesThatNeedAttention(
                self,
                *,
                customer: str,
                orgUnitId: str = ...,
                readMask: str = ...,
                **kwargs: typing.Any
            ) -> GoogleChromeManagementV1CountChromeDevicesThatNeedAttentionResponseHttpRequest: ...
            def countChromeHardwareFleetDevices(
                self,
                *,
                customer: str,
                orgUnitId: str = ...,
                readMask: str = ...,
                **kwargs: typing.Any
            ) -> GoogleChromeManagementV1CountChromeHardwareFleetDevicesResponseHttpRequest: ...
            def countChromeVersions(
                self,
                *,
                customer: str,
                filter: str = ...,
                orgUnitId: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> GoogleChromeManagementV1CountChromeVersionsResponseHttpRequest: ...
            def countChromeVersions_next(
                self,
                previous_request: GoogleChromeManagementV1CountChromeVersionsResponseHttpRequest,
                previous_response: GoogleChromeManagementV1CountChromeVersionsResponse,
            ) -> GoogleChromeManagementV1CountChromeVersionsResponseHttpRequest | None: ...
            def countInstalledApps(
                self,
                *,
                customer: str,
                filter: str = ...,
                orderBy: str = ...,
                orgUnitId: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> GoogleChromeManagementV1CountInstalledAppsResponseHttpRequest: ...
            def countInstalledApps_next(
                self,
                previous_request: GoogleChromeManagementV1CountInstalledAppsResponseHttpRequest,
                previous_response: GoogleChromeManagementV1CountInstalledAppsResponse,
            ) -> GoogleChromeManagementV1CountInstalledAppsResponseHttpRequest | None: ...
            def findInstalledAppDevices(
                self,
                *,
                customer: str,
                appId: str = ...,
                appType: typing_extensions.Literal[
                    "APP_TYPE_UNSPECIFIED",
                    "EXTENSION",
                    "APP",
                    "THEME",
                    "HOSTED_APP",
                    "ANDROID_APP",
                ] = ...,
                filter: str = ...,
                orderBy: str = ...,
                orgUnitId: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> GoogleChromeManagementV1FindInstalledAppDevicesResponseHttpRequest: ...
            def findInstalledAppDevices_next(
                self,
                previous_request: GoogleChromeManagementV1FindInstalledAppDevicesResponseHttpRequest,
                previous_response: GoogleChromeManagementV1FindInstalledAppDevicesResponse,
            ) -> GoogleChromeManagementV1FindInstalledAppDevicesResponseHttpRequest | None: ...

        @typing.type_check_only
        class TelemetryResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class DevicesResource(googleapiclient.discovery.Resource):
                def get(
                    self, *, name: str, readMask: str = ..., **kwargs: typing.Any
                ) -> GoogleChromeManagementV1TelemetryDeviceHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    readMask: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleChromeManagementV1ListTelemetryDevicesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleChromeManagementV1ListTelemetryDevicesResponseHttpRequest,
                    previous_response: GoogleChromeManagementV1ListTelemetryDevicesResponse,
                ) -> GoogleChromeManagementV1ListTelemetryDevicesResponseHttpRequest | None: ...

            def devices(self) -> DevicesResource: ...

        def apps(self) -> AppsResource: ...
        def reports(self) -> ReportsResource: ...
        def telemetry(self) -> TelemetryResource: ...

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
    def customers(self) -> CustomersResource: ...

@typing.type_check_only
class GoogleChromeManagementV1AppDetailsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleChromeManagementV1AppDetails: ...

@typing.type_check_only
class GoogleChromeManagementV1CountChromeAppRequestsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleChromeManagementV1CountChromeAppRequestsResponse: ...

@typing.type_check_only
class GoogleChromeManagementV1CountChromeDevicesReachingAutoExpirationDateResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleChromeManagementV1CountChromeDevicesReachingAutoExpirationDateResponse: ...

@typing.type_check_only
class GoogleChromeManagementV1CountChromeDevicesThatNeedAttentionResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleChromeManagementV1CountChromeDevicesThatNeedAttentionResponse: ...

@typing.type_check_only
class GoogleChromeManagementV1CountChromeHardwareFleetDevicesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleChromeManagementV1CountChromeHardwareFleetDevicesResponse: ...

@typing.type_check_only
class GoogleChromeManagementV1CountChromeVersionsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleChromeManagementV1CountChromeVersionsResponse: ...

@typing.type_check_only
class GoogleChromeManagementV1CountInstalledAppsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleChromeManagementV1CountInstalledAppsResponse: ...

@typing.type_check_only
class GoogleChromeManagementV1FindInstalledAppDevicesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleChromeManagementV1FindInstalledAppDevicesResponse: ...

@typing.type_check_only
class GoogleChromeManagementV1ListTelemetryDevicesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleChromeManagementV1ListTelemetryDevicesResponse: ...

@typing.type_check_only
class GoogleChromeManagementV1TelemetryDeviceHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleChromeManagementV1TelemetryDevice: ...
