import collections.abc
import typing

import httplib2

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
                orderBy: str | None = ...,
                orgUnitId: str | None = ...,
                pageSize: int | None = ...,
                pageToken: str | None = ...,
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
                extensionId: str | None = ...,
                orgUnitId: str | None = ...,
                pageSize: int | None = ...,
                pageToken: str | None = ...,
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
                extensionId: str | None = ...,
                orgUnitId: str | None = ...,
                pageSize: int | None = ...,
                pageToken: str | None = ...,
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
                body: GoogleChromeManagementVersionsV1ClaimCertificateProvisioningProcessRequest,
                **kwargs: typing.Any,
            ) -> GoogleChromeManagementVersionsV1ClaimCertificateProvisioningProcessResponseHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleChromeManagementVersionsV1CertificateProvisioningProcessHttpRequest: ...
            def setFailure(
                self,
                *,
                name: str,
                body: GoogleChromeManagementVersionsV1SetFailureRequest,
                **kwargs: typing.Any,
            ) -> GoogleChromeManagementVersionsV1SetFailureResponseHttpRequest: ...
            def signData(
                self,
                *,
                name: str,
                body: GoogleChromeManagementVersionsV1SignDataRequest,
                **kwargs: typing.Any,
            ) -> GoogleLongrunningOperationHttpRequest: ...
            def uploadCertificate(
                self,
                *,
                name: str,
                body: GoogleChromeManagementVersionsV1UploadCertificateRequest,
                **kwargs: typing.Any,
            ) -> (
                GoogleChromeManagementVersionsV1UploadCertificateResponseHttpRequest
            ): ...
            def operations(self) -> OperationsResource: ...

        @typing.type_check_only
        class ConnectorConfigsResource(googleapiclient.discovery.Resource):
            def create(
                self,
                *,
                parent: str,
                body: GoogleChromeManagementVersionsV1ConnectorConfig,
                connectorConfigId: str | None = ...,
                **kwargs: typing.Any,
            ) -> GoogleChromeManagementVersionsV1ConnectorConfigHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleProtobufEmptyHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleChromeManagementVersionsV1ConnectorConfigHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int | None = ...,
                pageToken: str | None = ...,
                **kwargs: typing.Any,
            ) -> (
                GoogleChromeManagementVersionsV1ListConnectorConfigsResponseHttpRequest
            ): ...
            def list_next(
                self,
                previous_request: GoogleChromeManagementVersionsV1ListConnectorConfigsResponseHttpRequest,
                previous_response: GoogleChromeManagementVersionsV1ListConnectorConfigsResponse,
            ) -> (
                GoogleChromeManagementVersionsV1ListConnectorConfigsResponseHttpRequest
                | None
            ): ...
            def patch(
                self,
                *,
                name: str,
                body: GoogleChromeManagementVersionsV1ConnectorConfig,
                updateMask: str | None = ...,
                **kwargs: typing.Any,
            ) -> GoogleChromeManagementVersionsV1ConnectorConfigHttpRequest: ...

        @typing.type_check_only
        class EnterpriseResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class SecurityInsightsResource(googleapiclient.discovery.Resource):
                def checkEnablementStatus(
                    self, *, customer: str, **kwargs: typing.Any
                ) -> GoogleChromeManagementVersionsV1CheckEnablementStatusResponseHttpRequest: ...
                def disable(
                    self,
                    *,
                    customer: str,
                    body: GoogleChromeManagementVersionsV1DisableInsightsRequest,
                    **kwargs: typing.Any,
                ) -> (
                    GoogleChromeManagementVersionsV1DisableInsightsResponseHttpRequest
                ): ...
                def enable(
                    self,
                    *,
                    customer: str,
                    body: GoogleChromeManagementVersionsV1EnableInsightsRequest,
                    **kwargs: typing.Any,
                ) -> (
                    GoogleChromeManagementVersionsV1EnableInsightsResponseHttpRequest
                ): ...
                def queryContentTransfers(
                    self,
                    *,
                    customer: str,
                    filter: str | None = ...,
                    **kwargs: typing.Any,
                ) -> GoogleChromeManagementVersionsV1QueryContentTransfersResponseHttpRequest: ...
                def queryContentTransfersBreakdowns(
                    self,
                    *,
                    customer: str,
                    breakdown: typing.Literal[
                        "CONTENT_TRANSFERS_BREAKDOWN_DIMENSION_UNSPECIFIED",
                        "USER",
                        "EVENT_DOMAIN",
                        "CONTENT_CATEGORY",
                    ]
                    | None = ...,
                    filter: str | None = ...,
                    fixedTimeRange: typing.Literal[
                        "FIXED_TIME_RANGE_UNSPECIFIED",
                        "FIXED_TIME_RANGE_FOUR_HOURS",
                        "FIXED_TIME_RANGE_ONE_DAY",
                        "FIXED_TIME_RANGE_ONE_WEEK",
                        "FIXED_TIME_RANGE_FOUR_WEEKS",
                    ]
                    | None = ...,
                    metric: typing.Literal[
                        "CONTENT_TRANSFERS_METRIC_UNSPECIFIED",
                        "CONTENT_TRANSFERS_METRIC_TOTAL_TRANSFERS",
                        "CONTENT_TRANSFERS_METRIC_TOTAL_UPLOADS",
                        "CONTENT_TRANSFERS_METRIC_TOTAL_DOWNLOADS",
                        "CONTENT_TRANSFERS_METRIC_TOTAL_PRINTS",
                        "CONTENT_TRANSFERS_METRIC_TOTAL_SENSITIVE_TRANSFERS",
                        "CONTENT_TRANSFERS_METRIC_SENSITIVE_UPLOADS",
                        "CONTENT_TRANSFERS_METRIC_SENSITIVE_DOWNLOADS",
                        "CONTENT_TRANSFERS_METRIC_SENSITIVE_PRINTS",
                    ]
                    | None = ...,
                    pageSize: int | None = ...,
                    pageToken: str | None = ...,
                    **kwargs: typing.Any,
                ) -> GoogleChromeManagementVersionsV1QueryContentTransfersBreakdownsResponseHttpRequest: ...
                def queryContentTransfersBreakdowns_next(
                    self,
                    previous_request: GoogleChromeManagementVersionsV1QueryContentTransfersBreakdownsResponseHttpRequest,
                    previous_response: GoogleChromeManagementVersionsV1QueryContentTransfersBreakdownsResponse,
                ) -> (
                    GoogleChromeManagementVersionsV1QueryContentTransfersBreakdownsResponseHttpRequest
                    | None
                ): ...
                def queryUrlVisits(
                    self,
                    *,
                    customer: str,
                    filter: str | None = ...,
                    **kwargs: typing.Any,
                ) -> (
                    GoogleChromeManagementVersionsV1QueryUrlVisitsResponseHttpRequest
                ): ...
                def queryUrlVisitsBreakdowns(
                    self,
                    *,
                    customer: str,
                    breakdown: typing.Literal[
                        "URL_VISITS_BREAKDOWN_DIMENSION_UNSPECIFIED",
                        "USER",
                        "EVENT_DOMAIN",
                    ]
                    | None = ...,
                    filter: str | None = ...,
                    fixedTimeRange: typing.Literal[
                        "FIXED_TIME_RANGE_UNSPECIFIED",
                        "FIXED_TIME_RANGE_FOUR_HOURS",
                        "FIXED_TIME_RANGE_ONE_DAY",
                        "FIXED_TIME_RANGE_ONE_WEEK",
                        "FIXED_TIME_RANGE_FOUR_WEEKS",
                    ]
                    | None = ...,
                    metric: typing.Literal[
                        "URL_VISITS_METRIC_UNSPECIFIED",
                        "URL_VISITS_METRIC_TOTAL_SUSPICIOUS_URL_VISITS",
                        "URL_VISITS_METRIC_HIGH_RISK_URL_VISITS",
                        "URL_VISITS_METRIC_MEDIUM_RISK_URL_VISITS",
                        "URL_VISITS_METRIC_LOW_RISK_URL_VISITS",
                    ]
                    | None = ...,
                    pageSize: int | None = ...,
                    pageToken: str | None = ...,
                    **kwargs: typing.Any,
                ) -> GoogleChromeManagementVersionsV1QueryUrlVisitsBreakdownsResponseHttpRequest: ...
                def queryUrlVisitsBreakdowns_next(
                    self,
                    previous_request: GoogleChromeManagementVersionsV1QueryUrlVisitsBreakdownsResponseHttpRequest,
                    previous_response: GoogleChromeManagementVersionsV1QueryUrlVisitsBreakdownsResponse,
                ) -> (
                    GoogleChromeManagementVersionsV1QueryUrlVisitsBreakdownsResponseHttpRequest
                    | None
                ): ...

            def securityInsights(self) -> SecurityInsightsResource: ...

        @typing.type_check_only
        class ProfilesResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class CommandsResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleChromeManagementVersionsV1ChromeBrowserProfileCommand,
                    **kwargs: typing.Any,
                ) -> GoogleChromeManagementVersionsV1ChromeBrowserProfileCommandHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleChromeManagementVersionsV1ChromeBrowserProfileCommandHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int | None = ...,
                    pageToken: str | None = ...,
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
                filter: str | None = ...,
                orderBy: str | None = ...,
                pageSize: int | None = ...,
                pageToken: str | None = ...,
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
                date_day: int | None = ...,
                date_month: int | None = ...,
                date_year: int | None = ...,
                **kwargs: typing.Any,
            ) -> GoogleChromeManagementV1CountActiveDevicesResponseHttpRequest: ...
            def countChromeBrowsersNeedingAttention(
                self,
                *,
                customer: str,
                orgUnitId: str | None = ...,
                **kwargs: typing.Any,
            ) -> GoogleChromeManagementV1CountChromeBrowsersNeedingAttentionResponseHttpRequest: ...
            def countChromeCrashEvents(
                self,
                *,
                customer: str,
                filter: str | None = ...,
                orderBy: str | None = ...,
                orgUnitId: str | None = ...,
                **kwargs: typing.Any,
            ) -> GoogleChromeManagementV1CountChromeCrashEventsResponseHttpRequest: ...
            def countChromeDevicesReachingAutoExpirationDate(
                self,
                *,
                customer: str,
                maxAueDate: str | None = ...,
                minAueDate: str | None = ...,
                orgUnitId: str | None = ...,
                **kwargs: typing.Any,
            ) -> GoogleChromeManagementV1CountChromeDevicesReachingAutoExpirationDateResponseHttpRequest: ...
            def countChromeDevicesThatNeedAttention(
                self,
                *,
                customer: str,
                orgUnitId: str | None = ...,
                readMask: str | None = ...,
                **kwargs: typing.Any,
            ) -> GoogleChromeManagementV1CountChromeDevicesThatNeedAttentionResponseHttpRequest: ...
            def countChromeHardwareFleetDevices(
                self,
                *,
                customer: str,
                orgUnitId: str | None = ...,
                readMask: str | None = ...,
                **kwargs: typing.Any,
            ) -> GoogleChromeManagementV1CountChromeHardwareFleetDevicesResponseHttpRequest: ...
            def countChromeProfileVersions(
                self,
                *,
                customer: str,
                filter: str | None = ...,
                orgUnitId: str | None = ...,
                pageSize: int | None = ...,
                pageToken: str | None = ...,
                **kwargs: typing.Any,
            ) -> (
                GoogleChromeManagementV1CountChromeProfileVersionsResponseHttpRequest
            ): ...
            def countChromeProfileVersions_next(
                self,
                previous_request: GoogleChromeManagementV1CountChromeProfileVersionsResponseHttpRequest,
                previous_response: GoogleChromeManagementV1CountChromeProfileVersionsResponse,
            ) -> (
                GoogleChromeManagementV1CountChromeProfileVersionsResponseHttpRequest
                | None
            ): ...
            def countChromeVersions(
                self,
                *,
                customer: str,
                filter: str | None = ...,
                orgUnitId: str | None = ...,
                pageSize: int | None = ...,
                pageToken: str | None = ...,
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
                date_day: int | None = ...,
                date_month: int | None = ...,
                date_year: int | None = ...,
                **kwargs: typing.Any,
            ) -> GoogleChromeManagementV1CountDevicesPerBootTypeResponseHttpRequest: ...
            def countDevicesPerReleaseChannel(
                self,
                *,
                customer: str,
                date_day: int | None = ...,
                date_month: int | None = ...,
                date_year: int | None = ...,
                **kwargs: typing.Any,
            ) -> (
                GoogleChromeManagementV1CountDevicesPerReleaseChannelResponseHttpRequest
            ): ...
            def countInstalledApps(
                self,
                *,
                customer: str,
                filter: str | None = ...,
                orderBy: str | None = ...,
                orgUnitId: str | None = ...,
                pageSize: int | None = ...,
                pageToken: str | None = ...,
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
                filter: str | None = ...,
                orderBy: str | None = ...,
                pageSize: int | None = ...,
                pageToken: str | None = ...,
                printerOrgUnitId: str | None = ...,
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
                filter: str | None = ...,
                orderBy: str | None = ...,
                pageSize: int | None = ...,
                pageToken: str | None = ...,
                printerOrgUnitId: str | None = ...,
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
                filter: str | None = ...,
                orderBy: str | None = ...,
                pageSize: int | None = ...,
                pageToken: str | None = ...,
                printerOrgUnitId: str | None = ...,
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
                appId: str | None = ...,
                appType: typing.Literal[
                    "APP_TYPE_UNSPECIFIED",
                    "EXTENSION",
                    "APP",
                    "THEME",
                    "HOSTED_APP",
                    "ANDROID_APP",
                ]
                | None = ...,
                filter: str | None = ...,
                orderBy: str | None = ...,
                orgUnitId: str | None = ...,
                pageSize: int | None = ...,
                pageToken: str | None = ...,
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
            def findInstalledAppProfiles(
                self,
                *,
                customer: str,
                appId: str | None = ...,
                appType: typing.Literal[
                    "APP_TYPE_UNSPECIFIED",
                    "EXTENSION",
                    "APP",
                    "THEME",
                    "HOSTED_APP",
                    "ANDROID_APP",
                ]
                | None = ...,
                filter: str | None = ...,
                orderBy: str | None = ...,
                orgUnitId: str | None = ...,
                pageSize: int | None = ...,
                pageToken: str | None = ...,
                **kwargs: typing.Any,
            ) -> (
                GoogleChromeManagementV1FindInstalledAppProfilesResponseHttpRequest
            ): ...
            def findInstalledAppProfiles_next(
                self,
                previous_request: GoogleChromeManagementV1FindInstalledAppProfilesResponseHttpRequest,
                previous_response: GoogleChromeManagementV1FindInstalledAppProfilesResponse,
            ) -> (
                GoogleChromeManagementV1FindInstalledAppProfilesResponseHttpRequest
                | None
            ): ...

        @typing.type_check_only
        class TelemetryResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class DevicesResource(googleapiclient.discovery.Resource):
                def get(
                    self, *, name: str, readMask: str | None = ..., **kwargs: typing.Any
                ) -> GoogleChromeManagementV1TelemetryDeviceHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str | None = ...,
                    pageSize: int | None = ...,
                    pageToken: str | None = ...,
                    readMask: str | None = ...,
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
                    filter: str | None = ...,
                    pageSize: int | None = ...,
                    pageToken: str | None = ...,
                    readMask: str | None = ...,
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
                    body: GoogleChromeManagementV1TelemetryNotificationConfig,
                    **kwargs: typing.Any,
                ) -> GoogleChromeManagementV1TelemetryNotificationConfigHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleProtobufEmptyHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int | None = ...,
                    pageToken: str | None = ...,
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
                    self, *, name: str, readMask: str | None = ..., **kwargs: typing.Any
                ) -> GoogleChromeManagementV1TelemetryUserHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str | None = ...,
                    pageSize: int | None = ...,
                    pageToken: str | None = ...,
                    readMask: str | None = ...,
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
                body: GoogleChromeManagementVersionsV1MoveThirdPartyProfileUserRequest,
                **kwargs: typing.Any,
            ) -> GoogleChromeManagementVersionsV1MoveThirdPartyProfileUserResponseHttpRequest: ...

        def apps(self) -> AppsResource: ...
        def certificateProvisioningProcesses(
            self,
        ) -> CertificateProvisioningProcessesResource: ...
        def connectorConfigs(self) -> ConnectorConfigsResource: ...
        def enterprise(self) -> EnterpriseResource: ...
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
            body: GoogleLongrunningCancelOperationRequest,
            **kwargs: typing.Any,
        ) -> GoogleProtobufEmptyHttpRequest: ...
        def delete(
            self, *, name: str, **kwargs: typing.Any
        ) -> GoogleProtobufEmptyHttpRequest: ...
        def list(
            self,
            *,
            name: str,
            filter: str | None = ...,
            pageSize: int | None = ...,
            pageToken: str | None = ...,
            returnPartialSuccess: bool | None = ...,
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
class GoogleChromeManagementV1CountChromeProfileVersionsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleChromeManagementV1CountChromeProfileVersionsResponse: ...

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
class GoogleChromeManagementV1FindInstalledAppProfilesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleChromeManagementV1FindInstalledAppProfilesResponse: ...

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
class GoogleChromeManagementVersionsV1CheckEnablementStatusResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleChromeManagementVersionsV1CheckEnablementStatusResponse: ...

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
class GoogleChromeManagementVersionsV1ConnectorConfigHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleChromeManagementVersionsV1ConnectorConfig: ...

@typing.type_check_only
class GoogleChromeManagementVersionsV1DisableInsightsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleChromeManagementVersionsV1DisableInsightsResponse: ...

@typing.type_check_only
class GoogleChromeManagementVersionsV1EnableInsightsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleChromeManagementVersionsV1EnableInsightsResponse: ...

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
class GoogleChromeManagementVersionsV1ListConnectorConfigsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleChromeManagementVersionsV1ListConnectorConfigsResponse: ...

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
class GoogleChromeManagementVersionsV1QueryContentTransfersBreakdownsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleChromeManagementVersionsV1QueryContentTransfersBreakdownsResponse: ...

@typing.type_check_only
class GoogleChromeManagementVersionsV1QueryContentTransfersResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleChromeManagementVersionsV1QueryContentTransfersResponse: ...

@typing.type_check_only
class GoogleChromeManagementVersionsV1QueryUrlVisitsBreakdownsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleChromeManagementVersionsV1QueryUrlVisitsBreakdownsResponse: ...

@typing.type_check_only
class GoogleChromeManagementVersionsV1QueryUrlVisitsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleChromeManagementVersionsV1QueryUrlVisitsResponse: ...

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
