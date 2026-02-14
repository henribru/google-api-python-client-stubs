import collections.abc
import typing

import httplib2
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http

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
                **kwargs: typing.Any,
            ) -> GoogleChromeManagementV1CountChromeAppRequestsResponseHttpRequest: ...
            def countChromeAppRequests_next(
                self,
                previous_request: GoogleChromeManagementV1CountChromeAppRequestsResponseHttpRequest,
                previous_response: GoogleChromeManagementV1CountChromeAppRequestsResponse,
            ) -> (
                GoogleChromeManagementV1CountChromeAppRequestsResponseHttpRequest | None
            ): ...
            def fetchDevicesRequestingExtension(
                self,
                *,
                customer: str,
                extensionId: str = ...,
                orgUnitId: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any,
            ) -> GoogleChromeManagementV1FetchDevicesRequestingExtensionResponseHttpRequest: ...
            def fetchDevicesRequestingExtension_next(
                self,
                previous_request: GoogleChromeManagementV1FetchDevicesRequestingExtensionResponseHttpRequest,
                previous_response: GoogleChromeManagementV1FetchDevicesRequestingExtensionResponse,
            ) -> (
                GoogleChromeManagementV1FetchDevicesRequestingExtensionResponseHttpRequest
                | None
            ): ...
            def fetchUsersRequestingExtension(
                self,
                *,
                customer: str,
                extensionId: str = ...,
                orgUnitId: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any,
            ) -> (
                GoogleChromeManagementV1FetchUsersRequestingExtensionResponseHttpRequest
            ): ...
            def fetchUsersRequestingExtension_next(
                self,
                previous_request: GoogleChromeManagementV1FetchUsersRequestingExtensionResponseHttpRequest,
                previous_response: GoogleChromeManagementV1FetchUsersRequestingExtensionResponse,
            ) -> (
                GoogleChromeManagementV1FetchUsersRequestingExtensionResponseHttpRequest
                | None
            ): ...
            def android(self) -> AndroidResource: ...
            def chrome(self) -> ChromeResource: ...
            def web(self) -> WebResource: ...

        @typing.type_check_only
        class CertificateProvisioningProcessesResource(
            googleapiclient.discovery.Resource
        ):
            @typing.type_check_only
            class OperationsResource(googleapiclient.discovery.Resource):
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...

            def claim(
                self,
                *,
                name: str,
                body: GoogleChromeManagementVersionsV1ClaimCertificateProvisioningProcessRequest = ...,
                **kwargs: typing.Any,
            ) -> GoogleChromeManagementVersionsV1ClaimCertificateProvisioningProcessResponseHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleChromeManagementVersionsV1CertificateProvisioningProcessHttpRequest: ...
            def setFailure(
                self,
                *,
                name: str,
                body: GoogleChromeManagementVersionsV1SetFailureRequest = ...,
                **kwargs: typing.Any,
            ) -> GoogleChromeManagementVersionsV1SetFailureResponseHttpRequest: ...
            def signData(
                self,
                *,
                name: str,
                body: GoogleChromeManagementVersionsV1SignDataRequest = ...,
                **kwargs: typing.Any,
            ) -> GoogleLongrunningOperationHttpRequest: ...
            def uploadCertificate(
                self,
                *,
                name: str,
                body: GoogleChromeManagementVersionsV1UploadCertificateRequest = ...,
                **kwargs: typing.Any,
            ) -> (
                GoogleChromeManagementVersionsV1UploadCertificateResponseHttpRequest
            ): ...
            def operations(self) -> OperationsResource: ...

        @typing.type_check_only
        class ProfilesResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class CommandsResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleChromeManagementVersionsV1ChromeBrowserProfileCommand = ...,
                    **kwargs: typing.Any,
                ) -> GoogleChromeManagementVersionsV1ChromeBrowserProfileCommandHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleChromeManagementVersionsV1ChromeBrowserProfileCommandHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleChromeManagementVersionsV1ListChromeBrowserProfileCommandsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleChromeManagementVersionsV1ListChromeBrowserProfileCommandsResponseHttpRequest,
                    previous_response: GoogleChromeManagementVersionsV1ListChromeBrowserProfileCommandsResponse,
                ) -> (
                    GoogleChromeManagementVersionsV1ListChromeBrowserProfileCommandsResponseHttpRequest
                    | None
                ): ...

            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleProtobufEmptyHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleChromeManagementVersionsV1ChromeBrowserProfileHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                filter: str = ...,
                orderBy: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any,
            ) -> GoogleChromeManagementVersionsV1ListChromeBrowserProfilesResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: GoogleChromeManagementVersionsV1ListChromeBrowserProfilesResponseHttpRequest,
                previous_response: GoogleChromeManagementVersionsV1ListChromeBrowserProfilesResponse,
            ) -> (
                GoogleChromeManagementVersionsV1ListChromeBrowserProfilesResponseHttpRequest
                | None
            ): ...
            def commands(self) -> CommandsResource: ...

        @typing.type_check_only
        class ReportsResource(googleapiclient.discovery.Resource):
            def countActiveDevices(
                self,
                *,
                customer: str,
                date_day: int = ...,
                date_month: int = ...,
                date_year: int = ...,
                **kwargs: typing.Any,
            ) -> GoogleChromeManagementV1CountActiveDevicesResponseHttpRequest: ...
            def countChromeBrowsersNeedingAttention(
                self, *, customer: str, orgUnitId: str = ..., **kwargs: typing.Any
            ) -> GoogleChromeManagementV1CountChromeBrowsersNeedingAttentionResponseHttpRequest: ...
            def countChromeCrashEvents(
                self,
                *,
                customer: str,
                filter: str = ...,
                orderBy: str = ...,
                orgUnitId: str = ...,
                **kwargs: typing.Any,
            ) -> GoogleChromeManagementV1CountChromeCrashEventsResponseHttpRequest: ...
            def countChromeDevicesReachingAutoExpirationDate(
                self,
                *,
                customer: str,
                maxAueDate: str = ...,
                minAueDate: str = ...,
                orgUnitId: str = ...,
                **kwargs: typing.Any,
            ) -> GoogleChromeManagementV1CountChromeDevicesReachingAutoExpirationDateResponseHttpRequest: ...
            def countChromeDevicesThatNeedAttention(
                self,
                *,
                customer: str,
                orgUnitId: str = ...,
                readMask: str = ...,
                **kwargs: typing.Any,
            ) -> GoogleChromeManagementV1CountChromeDevicesThatNeedAttentionResponseHttpRequest: ...
            def countChromeHardwareFleetDevices(
                self,
                *,
                customer: str,
                orgUnitId: str = ...,
                readMask: str = ...,
                **kwargs: typing.Any,
            ) -> GoogleChromeManagementV1CountChromeHardwareFleetDevicesResponseHttpRequest: ...
            def countChromeVersions(
                self,
                *,
                customer: str,
                filter: str = ...,
                orgUnitId: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any,
            ) -> GoogleChromeManagementV1CountChromeVersionsResponseHttpRequest: ...
            def countChromeVersions_next(
                self,
                previous_request: GoogleChromeManagementV1CountChromeVersionsResponseHttpRequest,
                previous_response: GoogleChromeManagementV1CountChromeVersionsResponse,
            ) -> (
                GoogleChromeManagementV1CountChromeVersionsResponseHttpRequest | None
            ): ...
            def countDevicesPerBootType(
                self,
                *,
                customer: str,
                date_day: int = ...,
                date_month: int = ...,
                date_year: int = ...,
                **kwargs: typing.Any,
            ) -> GoogleChromeManagementV1CountDevicesPerBootTypeResponseHttpRequest: ...
            def countDevicesPerReleaseChannel(
                self,
                *,
                customer: str,
                date_day: int = ...,
                date_month: int = ...,
                date_year: int = ...,
                **kwargs: typing.Any,
            ) -> (
                GoogleChromeManagementV1CountDevicesPerReleaseChannelResponseHttpRequest
            ): ...
            def countInstalledApps(
                self,
                *,
                customer: str,
                filter: str = ...,
                orderBy: str = ...,
                orgUnitId: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any,
            ) -> GoogleChromeManagementV1CountInstalledAppsResponseHttpRequest: ...
            def countInstalledApps_next(
                self,
                previous_request: GoogleChromeManagementV1CountInstalledAppsResponseHttpRequest,
                previous_response: GoogleChromeManagementV1CountInstalledAppsResponse,
            ) -> (
                GoogleChromeManagementV1CountInstalledAppsResponseHttpRequest | None
            ): ...
            def countPrintJobsByPrinter(
                self,
                *,
                customer: str,
                filter: str = ...,
                orderBy: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                printerOrgUnitId: str = ...,
                **kwargs: typing.Any,
            ) -> GoogleChromeManagementV1CountPrintJobsByPrinterResponseHttpRequest: ...
            def countPrintJobsByPrinter_next(
                self,
                previous_request: GoogleChromeManagementV1CountPrintJobsByPrinterResponseHttpRequest,
                previous_response: GoogleChromeManagementV1CountPrintJobsByPrinterResponse,
            ) -> (
                GoogleChromeManagementV1CountPrintJobsByPrinterResponseHttpRequest
                | None
            ): ...
            def countPrintJobsByUser(
                self,
                *,
                customer: str,
                filter: str = ...,
                orderBy: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                printerOrgUnitId: str = ...,
                **kwargs: typing.Any,
            ) -> GoogleChromeManagementV1CountPrintJobsByUserResponseHttpRequest: ...
            def countPrintJobsByUser_next(
                self,
                previous_request: GoogleChromeManagementV1CountPrintJobsByUserResponseHttpRequest,
                previous_response: GoogleChromeManagementV1CountPrintJobsByUserResponse,
            ) -> (
                GoogleChromeManagementV1CountPrintJobsByUserResponseHttpRequest | None
            ): ...
            def enumeratePrintJobs(
                self,
                *,
                customer: str,
                filter: str = ...,
                orderBy: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                printerOrgUnitId: str = ...,
                **kwargs: typing.Any,
            ) -> GoogleChromeManagementV1EnumeratePrintJobsResponseHttpRequest: ...
            def enumeratePrintJobs_next(
                self,
                previous_request: GoogleChromeManagementV1EnumeratePrintJobsResponseHttpRequest,
                previous_response: GoogleChromeManagementV1EnumeratePrintJobsResponse,
            ) -> (
                GoogleChromeManagementV1EnumeratePrintJobsResponseHttpRequest | None
            ): ...
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
                **kwargs: typing.Any,
            ) -> GoogleChromeManagementV1FindInstalledAppDevicesResponseHttpRequest: ...
            def findInstalledAppDevices_next(
                self,
                previous_request: GoogleChromeManagementV1FindInstalledAppDevicesResponseHttpRequest,
                previous_response: GoogleChromeManagementV1FindInstalledAppDevicesResponse,
            ) -> (
                GoogleChromeManagementV1FindInstalledAppDevicesResponseHttpRequest
                | None
            ): ...

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
                    **kwargs: typing.Any,
                ) -> (
                    GoogleChromeManagementV1ListTelemetryDevicesResponseHttpRequest
                ): ...
                def list_next(
                    self,
                    previous_request: GoogleChromeManagementV1ListTelemetryDevicesResponseHttpRequest,
                    previous_response: GoogleChromeManagementV1ListTelemetryDevicesResponse,
                ) -> (
                    GoogleChromeManagementV1ListTelemetryDevicesResponseHttpRequest
                    | None
                ): ...

            @typing.type_check_only
            class EventsResource(googleapiclient.discovery.Resource):
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    readMask: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleChromeManagementV1ListTelemetryEventsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleChromeManagementV1ListTelemetryEventsResponseHttpRequest,
                    previous_response: GoogleChromeManagementV1ListTelemetryEventsResponse,
                ) -> (
                    GoogleChromeManagementV1ListTelemetryEventsResponseHttpRequest
                    | None
                ): ...

            @typing.type_check_only
            class NotificationConfigsResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleChromeManagementV1TelemetryNotificationConfig = ...,
                    **kwargs: typing.Any,
                ) -> GoogleChromeManagementV1TelemetryNotificationConfigHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleProtobufEmptyHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleChromeManagementV1ListTelemetryNotificationConfigsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleChromeManagementV1ListTelemetryNotificationConfigsResponseHttpRequest,
                    previous_response: GoogleChromeManagementV1ListTelemetryNotificationConfigsResponse,
                ) -> (
                    GoogleChromeManagementV1ListTelemetryNotificationConfigsResponseHttpRequest
                    | None
                ): ...

            @typing.type_check_only
            class UsersResource(googleapiclient.discovery.Resource):
                def get(
                    self, *, name: str, readMask: str = ..., **kwargs: typing.Any
                ) -> GoogleChromeManagementV1TelemetryUserHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    readMask: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleChromeManagementV1ListTelemetryUsersResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleChromeManagementV1ListTelemetryUsersResponseHttpRequest,
                    previous_response: GoogleChromeManagementV1ListTelemetryUsersResponse,
                ) -> (
                    GoogleChromeManagementV1ListTelemetryUsersResponseHttpRequest | None
                ): ...

            def devices(self) -> DevicesResource: ...
            def events(self) -> EventsResource: ...
            def notificationConfigs(self) -> NotificationConfigsResource: ...
            def users(self) -> UsersResource: ...

        @typing.type_check_only
        class ThirdPartyProfileUsersResource(googleapiclient.discovery.Resource):
            def move(
                self,
                *,
                name: str,
                body: GoogleChromeManagementVersionsV1MoveThirdPartyProfileUserRequest = ...,
                **kwargs: typing.Any,
            ) -> GoogleChromeManagementVersionsV1MoveThirdPartyProfileUserResponseHttpRequest: ...

        def apps(self) -> AppsResource: ...
        def certificateProvisioningProcesses(
            self,
        ) -> CertificateProvisioningProcessesResource: ...
        def profiles(self) -> ProfilesResource: ...
        def reports(self) -> ReportsResource: ...
        def telemetry(self) -> TelemetryResource: ...
        def thirdPartyProfileUsers(self) -> ThirdPartyProfileUsersResource: ...

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
        def list(
            self,
            *,
            name: str,
            filter: str = ...,
            pageSize: int = ...,
            pageToken: str = ...,
            returnPartialSuccess: bool = ...,
            **kwargs: typing.Any,
        ) -> GoogleLongrunningListOperationsResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: GoogleLongrunningListOperationsResponseHttpRequest,
            previous_response: GoogleLongrunningListOperationsResponse,
        ) -> GoogleLongrunningListOperationsResponseHttpRequest | None: ...

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
    def customers(self) -> CustomersResource: ...
    def operations(self) -> OperationsResource: ...

@typing.type_check_only
class GoogleChromeManagementV1AppDetailsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleChromeManagementV1AppDetails: ...

@typing.type_check_only
class GoogleChromeManagementV1CountActiveDevicesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleChromeManagementV1CountActiveDevicesResponse: ...

@typing.type_check_only
class GoogleChromeManagementV1CountChromeAppRequestsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleChromeManagementV1CountChromeAppRequestsResponse: ...

@typing.type_check_only
class GoogleChromeManagementV1CountChromeBrowsersNeedingAttentionResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleChromeManagementV1CountChromeBrowsersNeedingAttentionResponse: ...

@typing.type_check_only
class GoogleChromeManagementV1CountChromeCrashEventsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleChromeManagementV1CountChromeCrashEventsResponse: ...

@typing.type_check_only
class GoogleChromeManagementV1CountChromeDevicesReachingAutoExpirationDateResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> (
        GoogleChromeManagementV1CountChromeDevicesReachingAutoExpirationDateResponse
    ): ...

@typing.type_check_only
class GoogleChromeManagementV1CountChromeDevicesThatNeedAttentionResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleChromeManagementV1CountChromeDevicesThatNeedAttentionResponse: ...

@typing.type_check_only
class GoogleChromeManagementV1CountChromeHardwareFleetDevicesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleChromeManagementV1CountChromeHardwareFleetDevicesResponse: ...

@typing.type_check_only
class GoogleChromeManagementV1CountChromeVersionsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleChromeManagementV1CountChromeVersionsResponse: ...

@typing.type_check_only
class GoogleChromeManagementV1CountDevicesPerBootTypeResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleChromeManagementV1CountDevicesPerBootTypeResponse: ...

@typing.type_check_only
class GoogleChromeManagementV1CountDevicesPerReleaseChannelResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleChromeManagementV1CountDevicesPerReleaseChannelResponse: ...

@typing.type_check_only
class GoogleChromeManagementV1CountInstalledAppsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleChromeManagementV1CountInstalledAppsResponse: ...

@typing.type_check_only
class GoogleChromeManagementV1CountPrintJobsByPrinterResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleChromeManagementV1CountPrintJobsByPrinterResponse: ...

@typing.type_check_only
class GoogleChromeManagementV1CountPrintJobsByUserResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleChromeManagementV1CountPrintJobsByUserResponse: ...

@typing.type_check_only
class GoogleChromeManagementV1EnumeratePrintJobsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleChromeManagementV1EnumeratePrintJobsResponse: ...

@typing.type_check_only
class GoogleChromeManagementV1FetchDevicesRequestingExtensionResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleChromeManagementV1FetchDevicesRequestingExtensionResponse: ...

@typing.type_check_only
class GoogleChromeManagementV1FetchUsersRequestingExtensionResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleChromeManagementV1FetchUsersRequestingExtensionResponse: ...

@typing.type_check_only
class GoogleChromeManagementV1FindInstalledAppDevicesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleChromeManagementV1FindInstalledAppDevicesResponse: ...

@typing.type_check_only
class GoogleChromeManagementV1ListTelemetryDevicesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleChromeManagementV1ListTelemetryDevicesResponse: ...

@typing.type_check_only
class GoogleChromeManagementV1ListTelemetryEventsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleChromeManagementV1ListTelemetryEventsResponse: ...

@typing.type_check_only
class GoogleChromeManagementV1ListTelemetryNotificationConfigsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleChromeManagementV1ListTelemetryNotificationConfigsResponse: ...

@typing.type_check_only
class GoogleChromeManagementV1ListTelemetryUsersResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleChromeManagementV1ListTelemetryUsersResponse: ...

@typing.type_check_only
class GoogleChromeManagementV1TelemetryDeviceHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleChromeManagementV1TelemetryDevice: ...

@typing.type_check_only
class GoogleChromeManagementV1TelemetryNotificationConfigHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleChromeManagementV1TelemetryNotificationConfig: ...

@typing.type_check_only
class GoogleChromeManagementV1TelemetryUserHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleChromeManagementV1TelemetryUser: ...

@typing.type_check_only
class GoogleChromeManagementVersionsV1CertificateProvisioningProcessHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleChromeManagementVersionsV1CertificateProvisioningProcess: ...

@typing.type_check_only
class GoogleChromeManagementVersionsV1ChromeBrowserProfileHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleChromeManagementVersionsV1ChromeBrowserProfile: ...

@typing.type_check_only
class GoogleChromeManagementVersionsV1ChromeBrowserProfileCommandHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleChromeManagementVersionsV1ChromeBrowserProfileCommand: ...

@typing.type_check_only
class GoogleChromeManagementVersionsV1ClaimCertificateProvisioningProcessResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> (
        GoogleChromeManagementVersionsV1ClaimCertificateProvisioningProcessResponse
    ): ...

@typing.type_check_only
class GoogleChromeManagementVersionsV1ListChromeBrowserProfileCommandsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleChromeManagementVersionsV1ListChromeBrowserProfileCommandsResponse: ...

@typing.type_check_only
class GoogleChromeManagementVersionsV1ListChromeBrowserProfilesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleChromeManagementVersionsV1ListChromeBrowserProfilesResponse: ...

@typing.type_check_only
class GoogleChromeManagementVersionsV1MoveThirdPartyProfileUserResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleChromeManagementVersionsV1MoveThirdPartyProfileUserResponse: ...

@typing.type_check_only
class GoogleChromeManagementVersionsV1SetFailureResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleChromeManagementVersionsV1SetFailureResponse: ...

@typing.type_check_only
class GoogleChromeManagementVersionsV1UploadCertificateResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleChromeManagementVersionsV1UploadCertificateResponse: ...

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
