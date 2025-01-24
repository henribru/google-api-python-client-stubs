import collections.abc
import typing

import httplib2
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http

from .schemas import *

_list = list

@typing.type_check_only
class SecurityCommandCenterResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class FoldersResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class AssetsResource(googleapiclient.discovery.Resource):
            def group(
                self,
                *,
                parent: str,
                body: GroupAssetsRequest = ...,
                **kwargs: typing.Any,
            ) -> GroupAssetsResponseHttpRequest: ...
            def group_next(
                self,
                previous_request: GroupAssetsResponseHttpRequest,
                previous_response: GroupAssetsResponse,
            ) -> GroupAssetsResponseHttpRequest | None: ...
            def list(
                self,
                *,
                parent: str,
                compareDuration: str = ...,
                fieldMask: str = ...,
                filter: str = ...,
                orderBy: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                readTime: str = ...,
                **kwargs: typing.Any,
            ) -> ListAssetsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListAssetsResponseHttpRequest,
                previous_response: ListAssetsResponse,
            ) -> ListAssetsResponseHttpRequest | None: ...
            def updateSecurityMarks(
                self,
                *,
                name: str,
                body: SecurityMarks = ...,
                startTime: str = ...,
                updateMask: str = ...,
                **kwargs: typing.Any,
            ) -> SecurityMarksHttpRequest: ...

        @typing.type_check_only
        class BigQueryExportsResource(googleapiclient.discovery.Resource):
            def create(
                self,
                *,
                parent: str,
                body: GoogleCloudSecuritycenterV1BigQueryExport = ...,
                bigQueryExportId: str = ...,
                **kwargs: typing.Any,
            ) -> GoogleCloudSecuritycenterV1BigQueryExportHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleCloudSecuritycenterV1BigQueryExportHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any,
            ) -> ListBigQueryExportsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListBigQueryExportsResponseHttpRequest,
                previous_response: ListBigQueryExportsResponse,
            ) -> ListBigQueryExportsResponseHttpRequest | None: ...
            def patch(
                self,
                *,
                name: str,
                body: GoogleCloudSecuritycenterV1BigQueryExport = ...,
                updateMask: str = ...,
                **kwargs: typing.Any,
            ) -> GoogleCloudSecuritycenterV1BigQueryExportHttpRequest: ...

        @typing.type_check_only
        class EventThreatDetectionSettingsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class CustomModulesResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: EventThreatDetectionCustomModule = ...,
                    **kwargs: typing.Any,
                ) -> EventThreatDetectionCustomModuleHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> EventThreatDetectionCustomModuleHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> ListEventThreatDetectionCustomModulesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListEventThreatDetectionCustomModulesResponseHttpRequest,
                    previous_response: ListEventThreatDetectionCustomModulesResponse,
                ) -> (
                    ListEventThreatDetectionCustomModulesResponseHttpRequest | None
                ): ...
                def listDescendant(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> (
                    ListDescendantEventThreatDetectionCustomModulesResponseHttpRequest
                ): ...
                def listDescendant_next(
                    self,
                    previous_request: ListDescendantEventThreatDetectionCustomModulesResponseHttpRequest,
                    previous_response: ListDescendantEventThreatDetectionCustomModulesResponse,
                ) -> (
                    ListDescendantEventThreatDetectionCustomModulesResponseHttpRequest
                    | None
                ): ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: EventThreatDetectionCustomModule = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> EventThreatDetectionCustomModuleHttpRequest: ...

            @typing.type_check_only
            class EffectiveCustomModulesResource(googleapiclient.discovery.Resource):
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> EffectiveEventThreatDetectionCustomModuleHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> (
                    ListEffectiveEventThreatDetectionCustomModulesResponseHttpRequest
                ): ...
                def list_next(
                    self,
                    previous_request: ListEffectiveEventThreatDetectionCustomModulesResponseHttpRequest,
                    previous_response: ListEffectiveEventThreatDetectionCustomModulesResponse,
                ) -> (
                    ListEffectiveEventThreatDetectionCustomModulesResponseHttpRequest
                    | None
                ): ...

            def validateCustomModule(
                self,
                *,
                parent: str,
                body: ValidateEventThreatDetectionCustomModuleRequest = ...,
                **kwargs: typing.Any,
            ) -> ValidateEventThreatDetectionCustomModuleResponseHttpRequest: ...
            def customModules(self) -> CustomModulesResource: ...
            def effectiveCustomModules(self) -> EffectiveCustomModulesResource: ...

        @typing.type_check_only
        class FindingsResource(googleapiclient.discovery.Resource):
            def bulkMute(
                self,
                *,
                parent: str,
                body: BulkMuteFindingsRequest = ...,
                **kwargs: typing.Any,
            ) -> OperationHttpRequest: ...

        @typing.type_check_only
        class LocationsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class MuteConfigsResource(googleapiclient.discovery.Resource):
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudSecuritycenterV1MuteConfigHttpRequest: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudSecuritycenterV1MuteConfig = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudSecuritycenterV1MuteConfigHttpRequest: ...

            def muteConfigs(self) -> MuteConfigsResource: ...

        @typing.type_check_only
        class MuteConfigsResource(googleapiclient.discovery.Resource):
            def create(
                self,
                *,
                parent: str,
                body: GoogleCloudSecuritycenterV1MuteConfig = ...,
                muteConfigId: str = ...,
                **kwargs: typing.Any,
            ) -> GoogleCloudSecuritycenterV1MuteConfigHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleCloudSecuritycenterV1MuteConfigHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any,
            ) -> ListMuteConfigsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListMuteConfigsResponseHttpRequest,
                previous_response: ListMuteConfigsResponse,
            ) -> ListMuteConfigsResponseHttpRequest | None: ...
            def patch(
                self,
                *,
                name: str,
                body: GoogleCloudSecuritycenterV1MuteConfig = ...,
                updateMask: str = ...,
                **kwargs: typing.Any,
            ) -> GoogleCloudSecuritycenterV1MuteConfigHttpRequest: ...

        @typing.type_check_only
        class NotificationConfigsResource(googleapiclient.discovery.Resource):
            def create(
                self,
                *,
                parent: str,
                body: NotificationConfig = ...,
                configId: str = ...,
                **kwargs: typing.Any,
            ) -> NotificationConfigHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> NotificationConfigHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any,
            ) -> ListNotificationConfigsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListNotificationConfigsResponseHttpRequest,
                previous_response: ListNotificationConfigsResponse,
            ) -> ListNotificationConfigsResponseHttpRequest | None: ...
            def patch(
                self,
                *,
                name: str,
                body: NotificationConfig = ...,
                updateMask: str = ...,
                **kwargs: typing.Any,
            ) -> NotificationConfigHttpRequest: ...

        @typing.type_check_only
        class SecurityHealthAnalyticsSettingsResource(
            googleapiclient.discovery.Resource
        ):
            @typing.type_check_only
            class CustomModulesResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudSecuritycenterV1SecurityHealthAnalyticsCustomModule = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudSecuritycenterV1SecurityHealthAnalyticsCustomModuleHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudSecuritycenterV1SecurityHealthAnalyticsCustomModuleHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> ListSecurityHealthAnalyticsCustomModulesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListSecurityHealthAnalyticsCustomModulesResponseHttpRequest,
                    previous_response: ListSecurityHealthAnalyticsCustomModulesResponse,
                ) -> (
                    ListSecurityHealthAnalyticsCustomModulesResponseHttpRequest | None
                ): ...
                def listDescendant(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> ListDescendantSecurityHealthAnalyticsCustomModulesResponseHttpRequest: ...
                def listDescendant_next(
                    self,
                    previous_request: ListDescendantSecurityHealthAnalyticsCustomModulesResponseHttpRequest,
                    previous_response: ListDescendantSecurityHealthAnalyticsCustomModulesResponse,
                ) -> (
                    ListDescendantSecurityHealthAnalyticsCustomModulesResponseHttpRequest
                    | None
                ): ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudSecuritycenterV1SecurityHealthAnalyticsCustomModule = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudSecuritycenterV1SecurityHealthAnalyticsCustomModuleHttpRequest: ...
                def simulate(
                    self,
                    *,
                    parent: str,
                    body: SimulateSecurityHealthAnalyticsCustomModuleRequest = ...,
                    **kwargs: typing.Any,
                ) -> SimulateSecurityHealthAnalyticsCustomModuleResponseHttpRequest: ...

            @typing.type_check_only
            class EffectiveCustomModulesResource(googleapiclient.discovery.Resource):
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudSecuritycenterV1EffectiveSecurityHealthAnalyticsCustomModuleHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> (
                    ListEffectiveSecurityHealthAnalyticsCustomModulesResponseHttpRequest
                ): ...
                def list_next(
                    self,
                    previous_request: ListEffectiveSecurityHealthAnalyticsCustomModulesResponseHttpRequest,
                    previous_response: ListEffectiveSecurityHealthAnalyticsCustomModulesResponse,
                ) -> (
                    ListEffectiveSecurityHealthAnalyticsCustomModulesResponseHttpRequest
                    | None
                ): ...

            def customModules(self) -> CustomModulesResource: ...
            def effectiveCustomModules(self) -> EffectiveCustomModulesResource: ...

        @typing.type_check_only
        class SourcesResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class FindingsResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class ExternalSystemsResource(googleapiclient.discovery.Resource):
                    def patch(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudSecuritycenterV1ExternalSystem = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudSecuritycenterV1ExternalSystemHttpRequest: ...

                def group(
                    self,
                    *,
                    parent: str,
                    body: GroupFindingsRequest = ...,
                    **kwargs: typing.Any,
                ) -> GroupFindingsResponseHttpRequest: ...
                def group_next(
                    self,
                    previous_request: GroupFindingsResponseHttpRequest,
                    previous_response: GroupFindingsResponse,
                ) -> GroupFindingsResponseHttpRequest | None: ...
                def list(
                    self,
                    *,
                    parent: str,
                    compareDuration: str = ...,
                    fieldMask: str = ...,
                    filter: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    readTime: str = ...,
                    **kwargs: typing.Any,
                ) -> ListFindingsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListFindingsResponseHttpRequest,
                    previous_response: ListFindingsResponse,
                ) -> ListFindingsResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: Finding = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> FindingHttpRequest: ...
                def setMute(
                    self, *, name: str, body: SetMuteRequest = ..., **kwargs: typing.Any
                ) -> FindingHttpRequest: ...
                def setState(
                    self,
                    *,
                    name: str,
                    body: SetFindingStateRequest = ...,
                    **kwargs: typing.Any,
                ) -> FindingHttpRequest: ...
                def updateSecurityMarks(
                    self,
                    *,
                    name: str,
                    body: SecurityMarks = ...,
                    startTime: str = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> SecurityMarksHttpRequest: ...
                def externalSystems(self) -> ExternalSystemsResource: ...

            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any,
            ) -> ListSourcesResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListSourcesResponseHttpRequest,
                previous_response: ListSourcesResponse,
            ) -> ListSourcesResponseHttpRequest | None: ...
            def findings(self) -> FindingsResource: ...

        def assets(self) -> AssetsResource: ...
        def bigQueryExports(self) -> BigQueryExportsResource: ...
        def eventThreatDetectionSettings(
            self,
        ) -> EventThreatDetectionSettingsResource: ...
        def findings(self) -> FindingsResource: ...
        def locations(self) -> LocationsResource: ...
        def muteConfigs(self) -> MuteConfigsResource: ...
        def notificationConfigs(self) -> NotificationConfigsResource: ...
        def securityHealthAnalyticsSettings(
            self,
        ) -> SecurityHealthAnalyticsSettingsResource: ...
        def sources(self) -> SourcesResource: ...

    @typing.type_check_only
    class OrganizationsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class AssetsResource(googleapiclient.discovery.Resource):
            def group(
                self,
                *,
                parent: str,
                body: GroupAssetsRequest = ...,
                **kwargs: typing.Any,
            ) -> GroupAssetsResponseHttpRequest: ...
            def group_next(
                self,
                previous_request: GroupAssetsResponseHttpRequest,
                previous_response: GroupAssetsResponse,
            ) -> GroupAssetsResponseHttpRequest | None: ...
            def list(
                self,
                *,
                parent: str,
                compareDuration: str = ...,
                fieldMask: str = ...,
                filter: str = ...,
                orderBy: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                readTime: str = ...,
                **kwargs: typing.Any,
            ) -> ListAssetsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListAssetsResponseHttpRequest,
                previous_response: ListAssetsResponse,
            ) -> ListAssetsResponseHttpRequest | None: ...
            def runDiscovery(
                self,
                *,
                parent: str,
                body: RunAssetDiscoveryRequest = ...,
                **kwargs: typing.Any,
            ) -> OperationHttpRequest: ...
            def updateSecurityMarks(
                self,
                *,
                name: str,
                body: SecurityMarks = ...,
                startTime: str = ...,
                updateMask: str = ...,
                **kwargs: typing.Any,
            ) -> SecurityMarksHttpRequest: ...

        @typing.type_check_only
        class AttackPathsResource(googleapiclient.discovery.Resource):
            def list(
                self,
                *,
                parent: str,
                filter: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any,
            ) -> ListAttackPathsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListAttackPathsResponseHttpRequest,
                previous_response: ListAttackPathsResponse,
            ) -> ListAttackPathsResponseHttpRequest | None: ...

        @typing.type_check_only
        class BigQueryExportsResource(googleapiclient.discovery.Resource):
            def create(
                self,
                *,
                parent: str,
                body: GoogleCloudSecuritycenterV1BigQueryExport = ...,
                bigQueryExportId: str = ...,
                **kwargs: typing.Any,
            ) -> GoogleCloudSecuritycenterV1BigQueryExportHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleCloudSecuritycenterV1BigQueryExportHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any,
            ) -> ListBigQueryExportsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListBigQueryExportsResponseHttpRequest,
                previous_response: ListBigQueryExportsResponse,
            ) -> ListBigQueryExportsResponseHttpRequest | None: ...
            def patch(
                self,
                *,
                name: str,
                body: GoogleCloudSecuritycenterV1BigQueryExport = ...,
                updateMask: str = ...,
                **kwargs: typing.Any,
            ) -> GoogleCloudSecuritycenterV1BigQueryExportHttpRequest: ...

        @typing.type_check_only
        class EventThreatDetectionSettingsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class CustomModulesResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: EventThreatDetectionCustomModule = ...,
                    **kwargs: typing.Any,
                ) -> EventThreatDetectionCustomModuleHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> EventThreatDetectionCustomModuleHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> ListEventThreatDetectionCustomModulesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListEventThreatDetectionCustomModulesResponseHttpRequest,
                    previous_response: ListEventThreatDetectionCustomModulesResponse,
                ) -> (
                    ListEventThreatDetectionCustomModulesResponseHttpRequest | None
                ): ...
                def listDescendant(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> (
                    ListDescendantEventThreatDetectionCustomModulesResponseHttpRequest
                ): ...
                def listDescendant_next(
                    self,
                    previous_request: ListDescendantEventThreatDetectionCustomModulesResponseHttpRequest,
                    previous_response: ListDescendantEventThreatDetectionCustomModulesResponse,
                ) -> (
                    ListDescendantEventThreatDetectionCustomModulesResponseHttpRequest
                    | None
                ): ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: EventThreatDetectionCustomModule = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> EventThreatDetectionCustomModuleHttpRequest: ...

            @typing.type_check_only
            class EffectiveCustomModulesResource(googleapiclient.discovery.Resource):
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> EffectiveEventThreatDetectionCustomModuleHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> (
                    ListEffectiveEventThreatDetectionCustomModulesResponseHttpRequest
                ): ...
                def list_next(
                    self,
                    previous_request: ListEffectiveEventThreatDetectionCustomModulesResponseHttpRequest,
                    previous_response: ListEffectiveEventThreatDetectionCustomModulesResponse,
                ) -> (
                    ListEffectiveEventThreatDetectionCustomModulesResponseHttpRequest
                    | None
                ): ...

            def validateCustomModule(
                self,
                *,
                parent: str,
                body: ValidateEventThreatDetectionCustomModuleRequest = ...,
                **kwargs: typing.Any,
            ) -> ValidateEventThreatDetectionCustomModuleResponseHttpRequest: ...
            def customModules(self) -> CustomModulesResource: ...
            def effectiveCustomModules(self) -> EffectiveCustomModulesResource: ...

        @typing.type_check_only
        class FindingsResource(googleapiclient.discovery.Resource):
            def bulkMute(
                self,
                *,
                parent: str,
                body: BulkMuteFindingsRequest = ...,
                **kwargs: typing.Any,
            ) -> OperationHttpRequest: ...

        @typing.type_check_only
        class LocationsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class MuteConfigsResource(googleapiclient.discovery.Resource):
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudSecuritycenterV1MuteConfigHttpRequest: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudSecuritycenterV1MuteConfig = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudSecuritycenterV1MuteConfigHttpRequest: ...

            def muteConfigs(self) -> MuteConfigsResource: ...

        @typing.type_check_only
        class MuteConfigsResource(googleapiclient.discovery.Resource):
            def create(
                self,
                *,
                parent: str,
                body: GoogleCloudSecuritycenterV1MuteConfig = ...,
                muteConfigId: str = ...,
                **kwargs: typing.Any,
            ) -> GoogleCloudSecuritycenterV1MuteConfigHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleCloudSecuritycenterV1MuteConfigHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any,
            ) -> ListMuteConfigsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListMuteConfigsResponseHttpRequest,
                previous_response: ListMuteConfigsResponse,
            ) -> ListMuteConfigsResponseHttpRequest | None: ...
            def patch(
                self,
                *,
                name: str,
                body: GoogleCloudSecuritycenterV1MuteConfig = ...,
                updateMask: str = ...,
                **kwargs: typing.Any,
            ) -> GoogleCloudSecuritycenterV1MuteConfigHttpRequest: ...

        @typing.type_check_only
        class NotificationConfigsResource(googleapiclient.discovery.Resource):
            def create(
                self,
                *,
                parent: str,
                body: NotificationConfig = ...,
                configId: str = ...,
                **kwargs: typing.Any,
            ) -> NotificationConfigHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> NotificationConfigHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any,
            ) -> ListNotificationConfigsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListNotificationConfigsResponseHttpRequest,
                previous_response: ListNotificationConfigsResponse,
            ) -> ListNotificationConfigsResponseHttpRequest | None: ...
            def patch(
                self,
                *,
                name: str,
                body: NotificationConfig = ...,
                updateMask: str = ...,
                **kwargs: typing.Any,
            ) -> NotificationConfigHttpRequest: ...

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
        class ResourceValueConfigsResource(googleapiclient.discovery.Resource):
            def batchCreate(
                self,
                *,
                parent: str,
                body: BatchCreateResourceValueConfigsRequest = ...,
                **kwargs: typing.Any,
            ) -> BatchCreateResourceValueConfigsResponseHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleCloudSecuritycenterV1ResourceValueConfigHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any,
            ) -> ListResourceValueConfigsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListResourceValueConfigsResponseHttpRequest,
                previous_response: ListResourceValueConfigsResponse,
            ) -> ListResourceValueConfigsResponseHttpRequest | None: ...
            def patch(
                self,
                *,
                name: str,
                body: GoogleCloudSecuritycenterV1ResourceValueConfig = ...,
                updateMask: str = ...,
                **kwargs: typing.Any,
            ) -> GoogleCloudSecuritycenterV1ResourceValueConfigHttpRequest: ...

        @typing.type_check_only
        class SecurityHealthAnalyticsSettingsResource(
            googleapiclient.discovery.Resource
        ):
            @typing.type_check_only
            class CustomModulesResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudSecuritycenterV1SecurityHealthAnalyticsCustomModule = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudSecuritycenterV1SecurityHealthAnalyticsCustomModuleHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudSecuritycenterV1SecurityHealthAnalyticsCustomModuleHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> ListSecurityHealthAnalyticsCustomModulesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListSecurityHealthAnalyticsCustomModulesResponseHttpRequest,
                    previous_response: ListSecurityHealthAnalyticsCustomModulesResponse,
                ) -> (
                    ListSecurityHealthAnalyticsCustomModulesResponseHttpRequest | None
                ): ...
                def listDescendant(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> ListDescendantSecurityHealthAnalyticsCustomModulesResponseHttpRequest: ...
                def listDescendant_next(
                    self,
                    previous_request: ListDescendantSecurityHealthAnalyticsCustomModulesResponseHttpRequest,
                    previous_response: ListDescendantSecurityHealthAnalyticsCustomModulesResponse,
                ) -> (
                    ListDescendantSecurityHealthAnalyticsCustomModulesResponseHttpRequest
                    | None
                ): ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudSecuritycenterV1SecurityHealthAnalyticsCustomModule = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudSecuritycenterV1SecurityHealthAnalyticsCustomModuleHttpRequest: ...
                def simulate(
                    self,
                    *,
                    parent: str,
                    body: SimulateSecurityHealthAnalyticsCustomModuleRequest = ...,
                    **kwargs: typing.Any,
                ) -> SimulateSecurityHealthAnalyticsCustomModuleResponseHttpRequest: ...

            @typing.type_check_only
            class EffectiveCustomModulesResource(googleapiclient.discovery.Resource):
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudSecuritycenterV1EffectiveSecurityHealthAnalyticsCustomModuleHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> (
                    ListEffectiveSecurityHealthAnalyticsCustomModulesResponseHttpRequest
                ): ...
                def list_next(
                    self,
                    previous_request: ListEffectiveSecurityHealthAnalyticsCustomModulesResponseHttpRequest,
                    previous_response: ListEffectiveSecurityHealthAnalyticsCustomModulesResponse,
                ) -> (
                    ListEffectiveSecurityHealthAnalyticsCustomModulesResponseHttpRequest
                    | None
                ): ...

            def customModules(self) -> CustomModulesResource: ...
            def effectiveCustomModules(self) -> EffectiveCustomModulesResource: ...

        @typing.type_check_only
        class SimulationsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class AttackExposureResultsResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class AttackPathsResource(googleapiclient.discovery.Resource):
                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
                    ) -> ListAttackPathsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: ListAttackPathsResponseHttpRequest,
                        previous_response: ListAttackPathsResponse,
                    ) -> ListAttackPathsResponseHttpRequest | None: ...

                @typing.type_check_only
                class ValuedResourcesResource(googleapiclient.discovery.Resource):
                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str = ...,
                        orderBy: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
                    ) -> ListValuedResourcesResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: ListValuedResourcesResponseHttpRequest,
                        previous_response: ListValuedResourcesResponse,
                    ) -> ListValuedResourcesResponseHttpRequest | None: ...

                def attackPaths(self) -> AttackPathsResource: ...
                def valuedResources(self) -> ValuedResourcesResource: ...

            @typing.type_check_only
            class AttackPathsResource(googleapiclient.discovery.Resource):
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> ListAttackPathsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListAttackPathsResponseHttpRequest,
                    previous_response: ListAttackPathsResponse,
                ) -> ListAttackPathsResponseHttpRequest | None: ...

            @typing.type_check_only
            class ValuedResourcesResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class AttackPathsResource(googleapiclient.discovery.Resource):
                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
                    ) -> ListAttackPathsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: ListAttackPathsResponseHttpRequest,
                        previous_response: ListAttackPathsResponse,
                    ) -> ListAttackPathsResponseHttpRequest | None: ...

                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> ValuedResourceHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> ListValuedResourcesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListValuedResourcesResponseHttpRequest,
                    previous_response: ListValuedResourcesResponse,
                ) -> ListValuedResourcesResponseHttpRequest | None: ...
                def attackPaths(self) -> AttackPathsResource: ...

            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> SimulationHttpRequest: ...
            def attackExposureResults(self) -> AttackExposureResultsResource: ...
            def attackPaths(self) -> AttackPathsResource: ...
            def valuedResources(self) -> ValuedResourcesResource: ...

        @typing.type_check_only
        class SourcesResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class FindingsResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class ExternalSystemsResource(googleapiclient.discovery.Resource):
                    def patch(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudSecuritycenterV1ExternalSystem = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudSecuritycenterV1ExternalSystemHttpRequest: ...

                def create(
                    self,
                    *,
                    parent: str,
                    body: Finding = ...,
                    findingId: str = ...,
                    **kwargs: typing.Any,
                ) -> FindingHttpRequest: ...
                def group(
                    self,
                    *,
                    parent: str,
                    body: GroupFindingsRequest = ...,
                    **kwargs: typing.Any,
                ) -> GroupFindingsResponseHttpRequest: ...
                def group_next(
                    self,
                    previous_request: GroupFindingsResponseHttpRequest,
                    previous_response: GroupFindingsResponse,
                ) -> GroupFindingsResponseHttpRequest | None: ...
                def list(
                    self,
                    *,
                    parent: str,
                    compareDuration: str = ...,
                    fieldMask: str = ...,
                    filter: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    readTime: str = ...,
                    **kwargs: typing.Any,
                ) -> ListFindingsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListFindingsResponseHttpRequest,
                    previous_response: ListFindingsResponse,
                ) -> ListFindingsResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: Finding = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> FindingHttpRequest: ...
                def setMute(
                    self, *, name: str, body: SetMuteRequest = ..., **kwargs: typing.Any
                ) -> FindingHttpRequest: ...
                def setState(
                    self,
                    *,
                    name: str,
                    body: SetFindingStateRequest = ...,
                    **kwargs: typing.Any,
                ) -> FindingHttpRequest: ...
                def updateSecurityMarks(
                    self,
                    *,
                    name: str,
                    body: SecurityMarks = ...,
                    startTime: str = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> SecurityMarksHttpRequest: ...
                def externalSystems(self) -> ExternalSystemsResource: ...

            def create(
                self, *, parent: str, body: Source = ..., **kwargs: typing.Any
            ) -> SourceHttpRequest: ...
            def get(self, *, name: str, **kwargs: typing.Any) -> SourceHttpRequest: ...
            def getIamPolicy(
                self,
                *,
                resource: str,
                body: GetIamPolicyRequest = ...,
                **kwargs: typing.Any,
            ) -> PolicyHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any,
            ) -> ListSourcesResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListSourcesResponseHttpRequest,
                previous_response: ListSourcesResponse,
            ) -> ListSourcesResponseHttpRequest | None: ...
            def patch(
                self,
                *,
                name: str,
                body: Source = ...,
                updateMask: str = ...,
                **kwargs: typing.Any,
            ) -> SourceHttpRequest: ...
            def setIamPolicy(
                self,
                *,
                resource: str,
                body: SetIamPolicyRequest = ...,
                **kwargs: typing.Any,
            ) -> PolicyHttpRequest: ...
            def testIamPermissions(
                self,
                *,
                resource: str,
                body: TestIamPermissionsRequest = ...,
                **kwargs: typing.Any,
            ) -> TestIamPermissionsResponseHttpRequest: ...
            def findings(self) -> FindingsResource: ...

        @typing.type_check_only
        class ValuedResourcesResource(googleapiclient.discovery.Resource):
            def list(
                self,
                *,
                parent: str,
                filter: str = ...,
                orderBy: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any,
            ) -> ListValuedResourcesResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListValuedResourcesResponseHttpRequest,
                previous_response: ListValuedResourcesResponse,
            ) -> ListValuedResourcesResponseHttpRequest | None: ...

        def getOrganizationSettings(
            self, *, name: str, **kwargs: typing.Any
        ) -> OrganizationSettingsHttpRequest: ...
        def updateOrganizationSettings(
            self,
            *,
            name: str,
            body: OrganizationSettings = ...,
            updateMask: str = ...,
            **kwargs: typing.Any,
        ) -> OrganizationSettingsHttpRequest: ...
        def assets(self) -> AssetsResource: ...
        def attackPaths(self) -> AttackPathsResource: ...
        def bigQueryExports(self) -> BigQueryExportsResource: ...
        def eventThreatDetectionSettings(
            self,
        ) -> EventThreatDetectionSettingsResource: ...
        def findings(self) -> FindingsResource: ...
        def locations(self) -> LocationsResource: ...
        def muteConfigs(self) -> MuteConfigsResource: ...
        def notificationConfigs(self) -> NotificationConfigsResource: ...
        def operations(self) -> OperationsResource: ...
        def resourceValueConfigs(self) -> ResourceValueConfigsResource: ...
        def securityHealthAnalyticsSettings(
            self,
        ) -> SecurityHealthAnalyticsSettingsResource: ...
        def simulations(self) -> SimulationsResource: ...
        def sources(self) -> SourcesResource: ...
        def valuedResources(self) -> ValuedResourcesResource: ...

    @typing.type_check_only
    class ProjectsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class AssetsResource(googleapiclient.discovery.Resource):
            def group(
                self,
                *,
                parent: str,
                body: GroupAssetsRequest = ...,
                **kwargs: typing.Any,
            ) -> GroupAssetsResponseHttpRequest: ...
            def group_next(
                self,
                previous_request: GroupAssetsResponseHttpRequest,
                previous_response: GroupAssetsResponse,
            ) -> GroupAssetsResponseHttpRequest | None: ...
            def list(
                self,
                *,
                parent: str,
                compareDuration: str = ...,
                fieldMask: str = ...,
                filter: str = ...,
                orderBy: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                readTime: str = ...,
                **kwargs: typing.Any,
            ) -> ListAssetsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListAssetsResponseHttpRequest,
                previous_response: ListAssetsResponse,
            ) -> ListAssetsResponseHttpRequest | None: ...
            def updateSecurityMarks(
                self,
                *,
                name: str,
                body: SecurityMarks = ...,
                startTime: str = ...,
                updateMask: str = ...,
                **kwargs: typing.Any,
            ) -> SecurityMarksHttpRequest: ...

        @typing.type_check_only
        class BigQueryExportsResource(googleapiclient.discovery.Resource):
            def create(
                self,
                *,
                parent: str,
                body: GoogleCloudSecuritycenterV1BigQueryExport = ...,
                bigQueryExportId: str = ...,
                **kwargs: typing.Any,
            ) -> GoogleCloudSecuritycenterV1BigQueryExportHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleCloudSecuritycenterV1BigQueryExportHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any,
            ) -> ListBigQueryExportsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListBigQueryExportsResponseHttpRequest,
                previous_response: ListBigQueryExportsResponse,
            ) -> ListBigQueryExportsResponseHttpRequest | None: ...
            def patch(
                self,
                *,
                name: str,
                body: GoogleCloudSecuritycenterV1BigQueryExport = ...,
                updateMask: str = ...,
                **kwargs: typing.Any,
            ) -> GoogleCloudSecuritycenterV1BigQueryExportHttpRequest: ...

        @typing.type_check_only
        class EventThreatDetectionSettingsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class CustomModulesResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: EventThreatDetectionCustomModule = ...,
                    **kwargs: typing.Any,
                ) -> EventThreatDetectionCustomModuleHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> EventThreatDetectionCustomModuleHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> ListEventThreatDetectionCustomModulesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListEventThreatDetectionCustomModulesResponseHttpRequest,
                    previous_response: ListEventThreatDetectionCustomModulesResponse,
                ) -> (
                    ListEventThreatDetectionCustomModulesResponseHttpRequest | None
                ): ...
                def listDescendant(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> (
                    ListDescendantEventThreatDetectionCustomModulesResponseHttpRequest
                ): ...
                def listDescendant_next(
                    self,
                    previous_request: ListDescendantEventThreatDetectionCustomModulesResponseHttpRequest,
                    previous_response: ListDescendantEventThreatDetectionCustomModulesResponse,
                ) -> (
                    ListDescendantEventThreatDetectionCustomModulesResponseHttpRequest
                    | None
                ): ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: EventThreatDetectionCustomModule = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> EventThreatDetectionCustomModuleHttpRequest: ...

            @typing.type_check_only
            class EffectiveCustomModulesResource(googleapiclient.discovery.Resource):
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> EffectiveEventThreatDetectionCustomModuleHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> (
                    ListEffectiveEventThreatDetectionCustomModulesResponseHttpRequest
                ): ...
                def list_next(
                    self,
                    previous_request: ListEffectiveEventThreatDetectionCustomModulesResponseHttpRequest,
                    previous_response: ListEffectiveEventThreatDetectionCustomModulesResponse,
                ) -> (
                    ListEffectiveEventThreatDetectionCustomModulesResponseHttpRequest
                    | None
                ): ...

            def validateCustomModule(
                self,
                *,
                parent: str,
                body: ValidateEventThreatDetectionCustomModuleRequest = ...,
                **kwargs: typing.Any,
            ) -> ValidateEventThreatDetectionCustomModuleResponseHttpRequest: ...
            def customModules(self) -> CustomModulesResource: ...
            def effectiveCustomModules(self) -> EffectiveCustomModulesResource: ...

        @typing.type_check_only
        class FindingsResource(googleapiclient.discovery.Resource):
            def bulkMute(
                self,
                *,
                parent: str,
                body: BulkMuteFindingsRequest = ...,
                **kwargs: typing.Any,
            ) -> OperationHttpRequest: ...

        @typing.type_check_only
        class LocationsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class MuteConfigsResource(googleapiclient.discovery.Resource):
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudSecuritycenterV1MuteConfigHttpRequest: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudSecuritycenterV1MuteConfig = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudSecuritycenterV1MuteConfigHttpRequest: ...

            def muteConfigs(self) -> MuteConfigsResource: ...

        @typing.type_check_only
        class MuteConfigsResource(googleapiclient.discovery.Resource):
            def create(
                self,
                *,
                parent: str,
                body: GoogleCloudSecuritycenterV1MuteConfig = ...,
                muteConfigId: str = ...,
                **kwargs: typing.Any,
            ) -> GoogleCloudSecuritycenterV1MuteConfigHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleCloudSecuritycenterV1MuteConfigHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any,
            ) -> ListMuteConfigsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListMuteConfigsResponseHttpRequest,
                previous_response: ListMuteConfigsResponse,
            ) -> ListMuteConfigsResponseHttpRequest | None: ...
            def patch(
                self,
                *,
                name: str,
                body: GoogleCloudSecuritycenterV1MuteConfig = ...,
                updateMask: str = ...,
                **kwargs: typing.Any,
            ) -> GoogleCloudSecuritycenterV1MuteConfigHttpRequest: ...

        @typing.type_check_only
        class NotificationConfigsResource(googleapiclient.discovery.Resource):
            def create(
                self,
                *,
                parent: str,
                body: NotificationConfig = ...,
                configId: str = ...,
                **kwargs: typing.Any,
            ) -> NotificationConfigHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> NotificationConfigHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any,
            ) -> ListNotificationConfigsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListNotificationConfigsResponseHttpRequest,
                previous_response: ListNotificationConfigsResponse,
            ) -> ListNotificationConfigsResponseHttpRequest | None: ...
            def patch(
                self,
                *,
                name: str,
                body: NotificationConfig = ...,
                updateMask: str = ...,
                **kwargs: typing.Any,
            ) -> NotificationConfigHttpRequest: ...

        @typing.type_check_only
        class SecurityHealthAnalyticsSettingsResource(
            googleapiclient.discovery.Resource
        ):
            @typing.type_check_only
            class CustomModulesResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudSecuritycenterV1SecurityHealthAnalyticsCustomModule = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudSecuritycenterV1SecurityHealthAnalyticsCustomModuleHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudSecuritycenterV1SecurityHealthAnalyticsCustomModuleHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> ListSecurityHealthAnalyticsCustomModulesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListSecurityHealthAnalyticsCustomModulesResponseHttpRequest,
                    previous_response: ListSecurityHealthAnalyticsCustomModulesResponse,
                ) -> (
                    ListSecurityHealthAnalyticsCustomModulesResponseHttpRequest | None
                ): ...
                def listDescendant(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> ListDescendantSecurityHealthAnalyticsCustomModulesResponseHttpRequest: ...
                def listDescendant_next(
                    self,
                    previous_request: ListDescendantSecurityHealthAnalyticsCustomModulesResponseHttpRequest,
                    previous_response: ListDescendantSecurityHealthAnalyticsCustomModulesResponse,
                ) -> (
                    ListDescendantSecurityHealthAnalyticsCustomModulesResponseHttpRequest
                    | None
                ): ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudSecuritycenterV1SecurityHealthAnalyticsCustomModule = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudSecuritycenterV1SecurityHealthAnalyticsCustomModuleHttpRequest: ...
                def simulate(
                    self,
                    *,
                    parent: str,
                    body: SimulateSecurityHealthAnalyticsCustomModuleRequest = ...,
                    **kwargs: typing.Any,
                ) -> SimulateSecurityHealthAnalyticsCustomModuleResponseHttpRequest: ...

            @typing.type_check_only
            class EffectiveCustomModulesResource(googleapiclient.discovery.Resource):
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudSecuritycenterV1EffectiveSecurityHealthAnalyticsCustomModuleHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> (
                    ListEffectiveSecurityHealthAnalyticsCustomModulesResponseHttpRequest
                ): ...
                def list_next(
                    self,
                    previous_request: ListEffectiveSecurityHealthAnalyticsCustomModulesResponseHttpRequest,
                    previous_response: ListEffectiveSecurityHealthAnalyticsCustomModulesResponse,
                ) -> (
                    ListEffectiveSecurityHealthAnalyticsCustomModulesResponseHttpRequest
                    | None
                ): ...

            def customModules(self) -> CustomModulesResource: ...
            def effectiveCustomModules(self) -> EffectiveCustomModulesResource: ...

        @typing.type_check_only
        class SourcesResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class FindingsResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class ExternalSystemsResource(googleapiclient.discovery.Resource):
                    def patch(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudSecuritycenterV1ExternalSystem = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudSecuritycenterV1ExternalSystemHttpRequest: ...

                def group(
                    self,
                    *,
                    parent: str,
                    body: GroupFindingsRequest = ...,
                    **kwargs: typing.Any,
                ) -> GroupFindingsResponseHttpRequest: ...
                def group_next(
                    self,
                    previous_request: GroupFindingsResponseHttpRequest,
                    previous_response: GroupFindingsResponse,
                ) -> GroupFindingsResponseHttpRequest | None: ...
                def list(
                    self,
                    *,
                    parent: str,
                    compareDuration: str = ...,
                    fieldMask: str = ...,
                    filter: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    readTime: str = ...,
                    **kwargs: typing.Any,
                ) -> ListFindingsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListFindingsResponseHttpRequest,
                    previous_response: ListFindingsResponse,
                ) -> ListFindingsResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: Finding = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> FindingHttpRequest: ...
                def setMute(
                    self, *, name: str, body: SetMuteRequest = ..., **kwargs: typing.Any
                ) -> FindingHttpRequest: ...
                def setState(
                    self,
                    *,
                    name: str,
                    body: SetFindingStateRequest = ...,
                    **kwargs: typing.Any,
                ) -> FindingHttpRequest: ...
                def updateSecurityMarks(
                    self,
                    *,
                    name: str,
                    body: SecurityMarks = ...,
                    startTime: str = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> SecurityMarksHttpRequest: ...
                def externalSystems(self) -> ExternalSystemsResource: ...

            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any,
            ) -> ListSourcesResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListSourcesResponseHttpRequest,
                previous_response: ListSourcesResponse,
            ) -> ListSourcesResponseHttpRequest | None: ...
            def findings(self) -> FindingsResource: ...

        def assets(self) -> AssetsResource: ...
        def bigQueryExports(self) -> BigQueryExportsResource: ...
        def eventThreatDetectionSettings(
            self,
        ) -> EventThreatDetectionSettingsResource: ...
        def findings(self) -> FindingsResource: ...
        def locations(self) -> LocationsResource: ...
        def muteConfigs(self) -> MuteConfigsResource: ...
        def notificationConfigs(self) -> NotificationConfigsResource: ...
        def securityHealthAnalyticsSettings(
            self,
        ) -> SecurityHealthAnalyticsSettingsResource: ...
        def sources(self) -> SourcesResource: ...

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
    def folders(self) -> FoldersResource: ...
    def organizations(self) -> OrganizationsResource: ...
    def projects(self) -> ProjectsResource: ...

@typing.type_check_only
class BatchCreateResourceValueConfigsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> BatchCreateResourceValueConfigsResponse: ...

@typing.type_check_only
class EffectiveEventThreatDetectionCustomModuleHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> EffectiveEventThreatDetectionCustomModule: ...

@typing.type_check_only
class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Empty: ...

@typing.type_check_only
class EventThreatDetectionCustomModuleHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> EventThreatDetectionCustomModule: ...

@typing.type_check_only
class FindingHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Finding: ...

@typing.type_check_only
class GoogleCloudSecuritycenterV1BigQueryExportHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudSecuritycenterV1BigQueryExport: ...

@typing.type_check_only
class GoogleCloudSecuritycenterV1EffectiveSecurityHealthAnalyticsCustomModuleHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudSecuritycenterV1EffectiveSecurityHealthAnalyticsCustomModule: ...

@typing.type_check_only
class GoogleCloudSecuritycenterV1ExternalSystemHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudSecuritycenterV1ExternalSystem: ...

@typing.type_check_only
class GoogleCloudSecuritycenterV1MuteConfigHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudSecuritycenterV1MuteConfig: ...

@typing.type_check_only
class GoogleCloudSecuritycenterV1ResourceValueConfigHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudSecuritycenterV1ResourceValueConfig: ...

@typing.type_check_only
class GoogleCloudSecuritycenterV1SecurityHealthAnalyticsCustomModuleHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudSecuritycenterV1SecurityHealthAnalyticsCustomModule: ...

@typing.type_check_only
class GroupAssetsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GroupAssetsResponse: ...

@typing.type_check_only
class GroupFindingsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GroupFindingsResponse: ...

@typing.type_check_only
class ListAssetsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListAssetsResponse: ...

@typing.type_check_only
class ListAttackPathsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListAttackPathsResponse: ...

@typing.type_check_only
class ListBigQueryExportsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListBigQueryExportsResponse: ...

@typing.type_check_only
class ListDescendantEventThreatDetectionCustomModulesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListDescendantEventThreatDetectionCustomModulesResponse: ...

@typing.type_check_only
class ListDescendantSecurityHealthAnalyticsCustomModulesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListDescendantSecurityHealthAnalyticsCustomModulesResponse: ...

@typing.type_check_only
class ListEffectiveEventThreatDetectionCustomModulesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListEffectiveEventThreatDetectionCustomModulesResponse: ...

@typing.type_check_only
class ListEffectiveSecurityHealthAnalyticsCustomModulesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListEffectiveSecurityHealthAnalyticsCustomModulesResponse: ...

@typing.type_check_only
class ListEventThreatDetectionCustomModulesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListEventThreatDetectionCustomModulesResponse: ...

@typing.type_check_only
class ListFindingsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListFindingsResponse: ...

@typing.type_check_only
class ListMuteConfigsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListMuteConfigsResponse: ...

@typing.type_check_only
class ListNotificationConfigsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListNotificationConfigsResponse: ...

@typing.type_check_only
class ListOperationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListOperationsResponse: ...

@typing.type_check_only
class ListResourceValueConfigsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListResourceValueConfigsResponse: ...

@typing.type_check_only
class ListSecurityHealthAnalyticsCustomModulesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListSecurityHealthAnalyticsCustomModulesResponse: ...

@typing.type_check_only
class ListSourcesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListSourcesResponse: ...

@typing.type_check_only
class ListValuedResourcesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListValuedResourcesResponse: ...

@typing.type_check_only
class NotificationConfigHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> NotificationConfig: ...

@typing.type_check_only
class OperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Operation: ...

@typing.type_check_only
class OrganizationSettingsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> OrganizationSettings: ...

@typing.type_check_only
class PolicyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Policy: ...

@typing.type_check_only
class SecurityMarksHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> SecurityMarks: ...

@typing.type_check_only
class SimulateSecurityHealthAnalyticsCustomModuleResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> SimulateSecurityHealthAnalyticsCustomModuleResponse: ...

@typing.type_check_only
class SimulationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Simulation: ...

@typing.type_check_only
class SourceHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Source: ...

@typing.type_check_only
class TestIamPermissionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> TestIamPermissionsResponse: ...

@typing.type_check_only
class ValidateEventThreatDetectionCustomModuleResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ValidateEventThreatDetectionCustomModuleResponse: ...

@typing.type_check_only
class ValuedResourceHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ValuedResource: ...
