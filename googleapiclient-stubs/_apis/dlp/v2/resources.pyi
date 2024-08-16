import collections.abc
import typing

import httplib2
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http

from .schemas import *

_list = list

@typing.type_check_only
class DLPResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class InfoTypesResource(googleapiclient.discovery.Resource):
        def list(
            self,
            *,
            filter: str = ...,
            languageCode: str = ...,
            locationId: str = ...,
            parent: str = ...,
            **kwargs: typing.Any,
        ) -> GooglePrivacyDlpV2ListInfoTypesResponseHttpRequest: ...

    @typing.type_check_only
    class LocationsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class InfoTypesResource(googleapiclient.discovery.Resource):
            def list(
                self,
                *,
                parent: str,
                filter: str = ...,
                languageCode: str = ...,
                locationId: str = ...,
                **kwargs: typing.Any,
            ) -> GooglePrivacyDlpV2ListInfoTypesResponseHttpRequest: ...

        def infoTypes(self) -> InfoTypesResource: ...

    @typing.type_check_only
    class OrganizationsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class DeidentifyTemplatesResource(googleapiclient.discovery.Resource):
            def create(
                self,
                *,
                parent: str,
                body: GooglePrivacyDlpV2CreateDeidentifyTemplateRequest = ...,
                **kwargs: typing.Any,
            ) -> GooglePrivacyDlpV2DeidentifyTemplateHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleProtobufEmptyHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GooglePrivacyDlpV2DeidentifyTemplateHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                locationId: str = ...,
                orderBy: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any,
            ) -> GooglePrivacyDlpV2ListDeidentifyTemplatesResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: GooglePrivacyDlpV2ListDeidentifyTemplatesResponseHttpRequest,
                previous_response: GooglePrivacyDlpV2ListDeidentifyTemplatesResponse,
            ) -> (
                GooglePrivacyDlpV2ListDeidentifyTemplatesResponseHttpRequest | None
            ): ...
            def patch(
                self,
                *,
                name: str,
                body: GooglePrivacyDlpV2UpdateDeidentifyTemplateRequest = ...,
                **kwargs: typing.Any,
            ) -> GooglePrivacyDlpV2DeidentifyTemplateHttpRequest: ...

        @typing.type_check_only
        class InspectTemplatesResource(googleapiclient.discovery.Resource):
            def create(
                self,
                *,
                parent: str,
                body: GooglePrivacyDlpV2CreateInspectTemplateRequest = ...,
                **kwargs: typing.Any,
            ) -> GooglePrivacyDlpV2InspectTemplateHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleProtobufEmptyHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GooglePrivacyDlpV2InspectTemplateHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                locationId: str = ...,
                orderBy: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any,
            ) -> GooglePrivacyDlpV2ListInspectTemplatesResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: GooglePrivacyDlpV2ListInspectTemplatesResponseHttpRequest,
                previous_response: GooglePrivacyDlpV2ListInspectTemplatesResponse,
            ) -> GooglePrivacyDlpV2ListInspectTemplatesResponseHttpRequest | None: ...
            def patch(
                self,
                *,
                name: str,
                body: GooglePrivacyDlpV2UpdateInspectTemplateRequest = ...,
                **kwargs: typing.Any,
            ) -> GooglePrivacyDlpV2InspectTemplateHttpRequest: ...

        @typing.type_check_only
        class LocationsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class ColumnDataProfilesResource(googleapiclient.discovery.Resource):
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GooglePrivacyDlpV2ColumnDataProfileHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> GooglePrivacyDlpV2ListColumnDataProfilesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GooglePrivacyDlpV2ListColumnDataProfilesResponseHttpRequest,
                    previous_response: GooglePrivacyDlpV2ListColumnDataProfilesResponse,
                ) -> (
                    GooglePrivacyDlpV2ListColumnDataProfilesResponseHttpRequest | None
                ): ...

            @typing.type_check_only
            class ConnectionsResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: GooglePrivacyDlpV2CreateConnectionRequest = ...,
                    **kwargs: typing.Any,
                ) -> GooglePrivacyDlpV2ConnectionHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleProtobufEmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GooglePrivacyDlpV2ConnectionHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> GooglePrivacyDlpV2ListConnectionsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GooglePrivacyDlpV2ListConnectionsResponseHttpRequest,
                    previous_response: GooglePrivacyDlpV2ListConnectionsResponse,
                ) -> GooglePrivacyDlpV2ListConnectionsResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GooglePrivacyDlpV2UpdateConnectionRequest = ...,
                    **kwargs: typing.Any,
                ) -> GooglePrivacyDlpV2ConnectionHttpRequest: ...
                def search(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> GooglePrivacyDlpV2SearchConnectionsResponseHttpRequest: ...
                def search_next(
                    self,
                    previous_request: GooglePrivacyDlpV2SearchConnectionsResponseHttpRequest,
                    previous_response: GooglePrivacyDlpV2SearchConnectionsResponse,
                ) -> GooglePrivacyDlpV2SearchConnectionsResponseHttpRequest | None: ...

            @typing.type_check_only
            class DeidentifyTemplatesResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: GooglePrivacyDlpV2CreateDeidentifyTemplateRequest = ...,
                    **kwargs: typing.Any,
                ) -> GooglePrivacyDlpV2DeidentifyTemplateHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleProtobufEmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GooglePrivacyDlpV2DeidentifyTemplateHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    locationId: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> GooglePrivacyDlpV2ListDeidentifyTemplatesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GooglePrivacyDlpV2ListDeidentifyTemplatesResponseHttpRequest,
                    previous_response: GooglePrivacyDlpV2ListDeidentifyTemplatesResponse,
                ) -> (
                    GooglePrivacyDlpV2ListDeidentifyTemplatesResponseHttpRequest | None
                ): ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GooglePrivacyDlpV2UpdateDeidentifyTemplateRequest = ...,
                    **kwargs: typing.Any,
                ) -> GooglePrivacyDlpV2DeidentifyTemplateHttpRequest: ...

            @typing.type_check_only
            class DiscoveryConfigsResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: GooglePrivacyDlpV2CreateDiscoveryConfigRequest = ...,
                    **kwargs: typing.Any,
                ) -> GooglePrivacyDlpV2DiscoveryConfigHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleProtobufEmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GooglePrivacyDlpV2DiscoveryConfigHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> GooglePrivacyDlpV2ListDiscoveryConfigsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GooglePrivacyDlpV2ListDiscoveryConfigsResponseHttpRequest,
                    previous_response: GooglePrivacyDlpV2ListDiscoveryConfigsResponse,
                ) -> (
                    GooglePrivacyDlpV2ListDiscoveryConfigsResponseHttpRequest | None
                ): ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GooglePrivacyDlpV2UpdateDiscoveryConfigRequest = ...,
                    **kwargs: typing.Any,
                ) -> GooglePrivacyDlpV2DiscoveryConfigHttpRequest: ...

            @typing.type_check_only
            class DlpJobsResource(googleapiclient.discovery.Resource):
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    locationId: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    type: typing_extensions.Literal[
                        "DLP_JOB_TYPE_UNSPECIFIED", "INSPECT_JOB", "RISK_ANALYSIS_JOB"
                    ] = ...,
                    **kwargs: typing.Any,
                ) -> GooglePrivacyDlpV2ListDlpJobsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GooglePrivacyDlpV2ListDlpJobsResponseHttpRequest,
                    previous_response: GooglePrivacyDlpV2ListDlpJobsResponse,
                ) -> GooglePrivacyDlpV2ListDlpJobsResponseHttpRequest | None: ...

            @typing.type_check_only
            class FileStoreDataProfilesResource(googleapiclient.discovery.Resource):
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleProtobufEmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GooglePrivacyDlpV2FileStoreDataProfileHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> GooglePrivacyDlpV2ListFileStoreDataProfilesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GooglePrivacyDlpV2ListFileStoreDataProfilesResponseHttpRequest,
                    previous_response: GooglePrivacyDlpV2ListFileStoreDataProfilesResponse,
                ) -> (
                    GooglePrivacyDlpV2ListFileStoreDataProfilesResponseHttpRequest
                    | None
                ): ...

            @typing.type_check_only
            class InspectTemplatesResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: GooglePrivacyDlpV2CreateInspectTemplateRequest = ...,
                    **kwargs: typing.Any,
                ) -> GooglePrivacyDlpV2InspectTemplateHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleProtobufEmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GooglePrivacyDlpV2InspectTemplateHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    locationId: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> GooglePrivacyDlpV2ListInspectTemplatesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GooglePrivacyDlpV2ListInspectTemplatesResponseHttpRequest,
                    previous_response: GooglePrivacyDlpV2ListInspectTemplatesResponse,
                ) -> (
                    GooglePrivacyDlpV2ListInspectTemplatesResponseHttpRequest | None
                ): ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GooglePrivacyDlpV2UpdateInspectTemplateRequest = ...,
                    **kwargs: typing.Any,
                ) -> GooglePrivacyDlpV2InspectTemplateHttpRequest: ...

            @typing.type_check_only
            class JobTriggersResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: GooglePrivacyDlpV2CreateJobTriggerRequest = ...,
                    **kwargs: typing.Any,
                ) -> GooglePrivacyDlpV2JobTriggerHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleProtobufEmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GooglePrivacyDlpV2JobTriggerHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    locationId: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    type: typing_extensions.Literal[
                        "DLP_JOB_TYPE_UNSPECIFIED", "INSPECT_JOB", "RISK_ANALYSIS_JOB"
                    ] = ...,
                    **kwargs: typing.Any,
                ) -> GooglePrivacyDlpV2ListJobTriggersResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GooglePrivacyDlpV2ListJobTriggersResponseHttpRequest,
                    previous_response: GooglePrivacyDlpV2ListJobTriggersResponse,
                ) -> GooglePrivacyDlpV2ListJobTriggersResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GooglePrivacyDlpV2UpdateJobTriggerRequest = ...,
                    **kwargs: typing.Any,
                ) -> GooglePrivacyDlpV2JobTriggerHttpRequest: ...

            @typing.type_check_only
            class ProjectDataProfilesResource(googleapiclient.discovery.Resource):
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GooglePrivacyDlpV2ProjectDataProfileHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> GooglePrivacyDlpV2ListProjectDataProfilesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GooglePrivacyDlpV2ListProjectDataProfilesResponseHttpRequest,
                    previous_response: GooglePrivacyDlpV2ListProjectDataProfilesResponse,
                ) -> (
                    GooglePrivacyDlpV2ListProjectDataProfilesResponseHttpRequest | None
                ): ...

            @typing.type_check_only
            class StoredInfoTypesResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: GooglePrivacyDlpV2CreateStoredInfoTypeRequest = ...,
                    **kwargs: typing.Any,
                ) -> GooglePrivacyDlpV2StoredInfoTypeHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleProtobufEmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GooglePrivacyDlpV2StoredInfoTypeHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    locationId: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> GooglePrivacyDlpV2ListStoredInfoTypesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GooglePrivacyDlpV2ListStoredInfoTypesResponseHttpRequest,
                    previous_response: GooglePrivacyDlpV2ListStoredInfoTypesResponse,
                ) -> (
                    GooglePrivacyDlpV2ListStoredInfoTypesResponseHttpRequest | None
                ): ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GooglePrivacyDlpV2UpdateStoredInfoTypeRequest = ...,
                    **kwargs: typing.Any,
                ) -> GooglePrivacyDlpV2StoredInfoTypeHttpRequest: ...

            @typing.type_check_only
            class TableDataProfilesResource(googleapiclient.discovery.Resource):
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleProtobufEmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GooglePrivacyDlpV2TableDataProfileHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> GooglePrivacyDlpV2ListTableDataProfilesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GooglePrivacyDlpV2ListTableDataProfilesResponseHttpRequest,
                    previous_response: GooglePrivacyDlpV2ListTableDataProfilesResponse,
                ) -> (
                    GooglePrivacyDlpV2ListTableDataProfilesResponseHttpRequest | None
                ): ...

            def columnDataProfiles(self) -> ColumnDataProfilesResource: ...
            def connections(self) -> ConnectionsResource: ...
            def deidentifyTemplates(self) -> DeidentifyTemplatesResource: ...
            def discoveryConfigs(self) -> DiscoveryConfigsResource: ...
            def dlpJobs(self) -> DlpJobsResource: ...
            def fileStoreDataProfiles(self) -> FileStoreDataProfilesResource: ...
            def inspectTemplates(self) -> InspectTemplatesResource: ...
            def jobTriggers(self) -> JobTriggersResource: ...
            def projectDataProfiles(self) -> ProjectDataProfilesResource: ...
            def storedInfoTypes(self) -> StoredInfoTypesResource: ...
            def tableDataProfiles(self) -> TableDataProfilesResource: ...

        @typing.type_check_only
        class StoredInfoTypesResource(googleapiclient.discovery.Resource):
            def create(
                self,
                *,
                parent: str,
                body: GooglePrivacyDlpV2CreateStoredInfoTypeRequest = ...,
                **kwargs: typing.Any,
            ) -> GooglePrivacyDlpV2StoredInfoTypeHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleProtobufEmptyHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GooglePrivacyDlpV2StoredInfoTypeHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                locationId: str = ...,
                orderBy: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any,
            ) -> GooglePrivacyDlpV2ListStoredInfoTypesResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: GooglePrivacyDlpV2ListStoredInfoTypesResponseHttpRequest,
                previous_response: GooglePrivacyDlpV2ListStoredInfoTypesResponse,
            ) -> GooglePrivacyDlpV2ListStoredInfoTypesResponseHttpRequest | None: ...
            def patch(
                self,
                *,
                name: str,
                body: GooglePrivacyDlpV2UpdateStoredInfoTypeRequest = ...,
                **kwargs: typing.Any,
            ) -> GooglePrivacyDlpV2StoredInfoTypeHttpRequest: ...

        def deidentifyTemplates(self) -> DeidentifyTemplatesResource: ...
        def inspectTemplates(self) -> InspectTemplatesResource: ...
        def locations(self) -> LocationsResource: ...
        def storedInfoTypes(self) -> StoredInfoTypesResource: ...

    @typing.type_check_only
    class ProjectsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class ContentResource(googleapiclient.discovery.Resource):
            def deidentify(
                self,
                *,
                parent: str,
                body: GooglePrivacyDlpV2DeidentifyContentRequest = ...,
                **kwargs: typing.Any,
            ) -> GooglePrivacyDlpV2DeidentifyContentResponseHttpRequest: ...
            def inspect(
                self,
                *,
                parent: str,
                body: GooglePrivacyDlpV2InspectContentRequest = ...,
                **kwargs: typing.Any,
            ) -> GooglePrivacyDlpV2InspectContentResponseHttpRequest: ...
            def reidentify(
                self,
                *,
                parent: str,
                body: GooglePrivacyDlpV2ReidentifyContentRequest = ...,
                **kwargs: typing.Any,
            ) -> GooglePrivacyDlpV2ReidentifyContentResponseHttpRequest: ...

        @typing.type_check_only
        class DeidentifyTemplatesResource(googleapiclient.discovery.Resource):
            def create(
                self,
                *,
                parent: str,
                body: GooglePrivacyDlpV2CreateDeidentifyTemplateRequest = ...,
                **kwargs: typing.Any,
            ) -> GooglePrivacyDlpV2DeidentifyTemplateHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleProtobufEmptyHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GooglePrivacyDlpV2DeidentifyTemplateHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                locationId: str = ...,
                orderBy: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any,
            ) -> GooglePrivacyDlpV2ListDeidentifyTemplatesResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: GooglePrivacyDlpV2ListDeidentifyTemplatesResponseHttpRequest,
                previous_response: GooglePrivacyDlpV2ListDeidentifyTemplatesResponse,
            ) -> (
                GooglePrivacyDlpV2ListDeidentifyTemplatesResponseHttpRequest | None
            ): ...
            def patch(
                self,
                *,
                name: str,
                body: GooglePrivacyDlpV2UpdateDeidentifyTemplateRequest = ...,
                **kwargs: typing.Any,
            ) -> GooglePrivacyDlpV2DeidentifyTemplateHttpRequest: ...

        @typing.type_check_only
        class DlpJobsResource(googleapiclient.discovery.Resource):
            def cancel(
                self,
                *,
                name: str,
                body: GooglePrivacyDlpV2CancelDlpJobRequest = ...,
                **kwargs: typing.Any,
            ) -> GoogleProtobufEmptyHttpRequest: ...
            def create(
                self,
                *,
                parent: str,
                body: GooglePrivacyDlpV2CreateDlpJobRequest = ...,
                **kwargs: typing.Any,
            ) -> GooglePrivacyDlpV2DlpJobHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleProtobufEmptyHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GooglePrivacyDlpV2DlpJobHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                filter: str = ...,
                locationId: str = ...,
                orderBy: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                type: typing_extensions.Literal[
                    "DLP_JOB_TYPE_UNSPECIFIED", "INSPECT_JOB", "RISK_ANALYSIS_JOB"
                ] = ...,
                **kwargs: typing.Any,
            ) -> GooglePrivacyDlpV2ListDlpJobsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: GooglePrivacyDlpV2ListDlpJobsResponseHttpRequest,
                previous_response: GooglePrivacyDlpV2ListDlpJobsResponse,
            ) -> GooglePrivacyDlpV2ListDlpJobsResponseHttpRequest | None: ...

        @typing.type_check_only
        class ImageResource(googleapiclient.discovery.Resource):
            def redact(
                self,
                *,
                parent: str,
                body: GooglePrivacyDlpV2RedactImageRequest = ...,
                **kwargs: typing.Any,
            ) -> GooglePrivacyDlpV2RedactImageResponseHttpRequest: ...

        @typing.type_check_only
        class InspectTemplatesResource(googleapiclient.discovery.Resource):
            def create(
                self,
                *,
                parent: str,
                body: GooglePrivacyDlpV2CreateInspectTemplateRequest = ...,
                **kwargs: typing.Any,
            ) -> GooglePrivacyDlpV2InspectTemplateHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleProtobufEmptyHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GooglePrivacyDlpV2InspectTemplateHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                locationId: str = ...,
                orderBy: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any,
            ) -> GooglePrivacyDlpV2ListInspectTemplatesResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: GooglePrivacyDlpV2ListInspectTemplatesResponseHttpRequest,
                previous_response: GooglePrivacyDlpV2ListInspectTemplatesResponse,
            ) -> GooglePrivacyDlpV2ListInspectTemplatesResponseHttpRequest | None: ...
            def patch(
                self,
                *,
                name: str,
                body: GooglePrivacyDlpV2UpdateInspectTemplateRequest = ...,
                **kwargs: typing.Any,
            ) -> GooglePrivacyDlpV2InspectTemplateHttpRequest: ...

        @typing.type_check_only
        class JobTriggersResource(googleapiclient.discovery.Resource):
            def activate(
                self,
                *,
                name: str,
                body: GooglePrivacyDlpV2ActivateJobTriggerRequest = ...,
                **kwargs: typing.Any,
            ) -> GooglePrivacyDlpV2DlpJobHttpRequest: ...
            def create(
                self,
                *,
                parent: str,
                body: GooglePrivacyDlpV2CreateJobTriggerRequest = ...,
                **kwargs: typing.Any,
            ) -> GooglePrivacyDlpV2JobTriggerHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleProtobufEmptyHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GooglePrivacyDlpV2JobTriggerHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                filter: str = ...,
                locationId: str = ...,
                orderBy: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                type: typing_extensions.Literal[
                    "DLP_JOB_TYPE_UNSPECIFIED", "INSPECT_JOB", "RISK_ANALYSIS_JOB"
                ] = ...,
                **kwargs: typing.Any,
            ) -> GooglePrivacyDlpV2ListJobTriggersResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: GooglePrivacyDlpV2ListJobTriggersResponseHttpRequest,
                previous_response: GooglePrivacyDlpV2ListJobTriggersResponse,
            ) -> GooglePrivacyDlpV2ListJobTriggersResponseHttpRequest | None: ...
            def patch(
                self,
                *,
                name: str,
                body: GooglePrivacyDlpV2UpdateJobTriggerRequest = ...,
                **kwargs: typing.Any,
            ) -> GooglePrivacyDlpV2JobTriggerHttpRequest: ...

        @typing.type_check_only
        class LocationsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class ColumnDataProfilesResource(googleapiclient.discovery.Resource):
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GooglePrivacyDlpV2ColumnDataProfileHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> GooglePrivacyDlpV2ListColumnDataProfilesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GooglePrivacyDlpV2ListColumnDataProfilesResponseHttpRequest,
                    previous_response: GooglePrivacyDlpV2ListColumnDataProfilesResponse,
                ) -> (
                    GooglePrivacyDlpV2ListColumnDataProfilesResponseHttpRequest | None
                ): ...

            @typing.type_check_only
            class ConnectionsResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: GooglePrivacyDlpV2CreateConnectionRequest = ...,
                    **kwargs: typing.Any,
                ) -> GooglePrivacyDlpV2ConnectionHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleProtobufEmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GooglePrivacyDlpV2ConnectionHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> GooglePrivacyDlpV2ListConnectionsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GooglePrivacyDlpV2ListConnectionsResponseHttpRequest,
                    previous_response: GooglePrivacyDlpV2ListConnectionsResponse,
                ) -> GooglePrivacyDlpV2ListConnectionsResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GooglePrivacyDlpV2UpdateConnectionRequest = ...,
                    **kwargs: typing.Any,
                ) -> GooglePrivacyDlpV2ConnectionHttpRequest: ...
                def search(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> GooglePrivacyDlpV2SearchConnectionsResponseHttpRequest: ...
                def search_next(
                    self,
                    previous_request: GooglePrivacyDlpV2SearchConnectionsResponseHttpRequest,
                    previous_response: GooglePrivacyDlpV2SearchConnectionsResponse,
                ) -> GooglePrivacyDlpV2SearchConnectionsResponseHttpRequest | None: ...

            @typing.type_check_only
            class ContentResource(googleapiclient.discovery.Resource):
                def deidentify(
                    self,
                    *,
                    parent: str,
                    body: GooglePrivacyDlpV2DeidentifyContentRequest = ...,
                    **kwargs: typing.Any,
                ) -> GooglePrivacyDlpV2DeidentifyContentResponseHttpRequest: ...
                def inspect(
                    self,
                    *,
                    parent: str,
                    body: GooglePrivacyDlpV2InspectContentRequest = ...,
                    **kwargs: typing.Any,
                ) -> GooglePrivacyDlpV2InspectContentResponseHttpRequest: ...
                def reidentify(
                    self,
                    *,
                    parent: str,
                    body: GooglePrivacyDlpV2ReidentifyContentRequest = ...,
                    **kwargs: typing.Any,
                ) -> GooglePrivacyDlpV2ReidentifyContentResponseHttpRequest: ...

            @typing.type_check_only
            class DeidentifyTemplatesResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: GooglePrivacyDlpV2CreateDeidentifyTemplateRequest = ...,
                    **kwargs: typing.Any,
                ) -> GooglePrivacyDlpV2DeidentifyTemplateHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleProtobufEmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GooglePrivacyDlpV2DeidentifyTemplateHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    locationId: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> GooglePrivacyDlpV2ListDeidentifyTemplatesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GooglePrivacyDlpV2ListDeidentifyTemplatesResponseHttpRequest,
                    previous_response: GooglePrivacyDlpV2ListDeidentifyTemplatesResponse,
                ) -> (
                    GooglePrivacyDlpV2ListDeidentifyTemplatesResponseHttpRequest | None
                ): ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GooglePrivacyDlpV2UpdateDeidentifyTemplateRequest = ...,
                    **kwargs: typing.Any,
                ) -> GooglePrivacyDlpV2DeidentifyTemplateHttpRequest: ...

            @typing.type_check_only
            class DiscoveryConfigsResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: GooglePrivacyDlpV2CreateDiscoveryConfigRequest = ...,
                    **kwargs: typing.Any,
                ) -> GooglePrivacyDlpV2DiscoveryConfigHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleProtobufEmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GooglePrivacyDlpV2DiscoveryConfigHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> GooglePrivacyDlpV2ListDiscoveryConfigsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GooglePrivacyDlpV2ListDiscoveryConfigsResponseHttpRequest,
                    previous_response: GooglePrivacyDlpV2ListDiscoveryConfigsResponse,
                ) -> (
                    GooglePrivacyDlpV2ListDiscoveryConfigsResponseHttpRequest | None
                ): ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GooglePrivacyDlpV2UpdateDiscoveryConfigRequest = ...,
                    **kwargs: typing.Any,
                ) -> GooglePrivacyDlpV2DiscoveryConfigHttpRequest: ...

            @typing.type_check_only
            class DlpJobsResource(googleapiclient.discovery.Resource):
                def cancel(
                    self,
                    *,
                    name: str,
                    body: GooglePrivacyDlpV2CancelDlpJobRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleProtobufEmptyHttpRequest: ...
                def create(
                    self,
                    *,
                    parent: str,
                    body: GooglePrivacyDlpV2CreateDlpJobRequest = ...,
                    **kwargs: typing.Any,
                ) -> GooglePrivacyDlpV2DlpJobHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleProtobufEmptyHttpRequest: ...
                def finish(
                    self,
                    *,
                    name: str,
                    body: GooglePrivacyDlpV2FinishDlpJobRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleProtobufEmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GooglePrivacyDlpV2DlpJobHttpRequest: ...
                def hybridInspect(
                    self,
                    *,
                    name: str,
                    body: GooglePrivacyDlpV2HybridInspectDlpJobRequest = ...,
                    **kwargs: typing.Any,
                ) -> GooglePrivacyDlpV2HybridInspectResponseHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    locationId: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    type: typing_extensions.Literal[
                        "DLP_JOB_TYPE_UNSPECIFIED", "INSPECT_JOB", "RISK_ANALYSIS_JOB"
                    ] = ...,
                    **kwargs: typing.Any,
                ) -> GooglePrivacyDlpV2ListDlpJobsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GooglePrivacyDlpV2ListDlpJobsResponseHttpRequest,
                    previous_response: GooglePrivacyDlpV2ListDlpJobsResponse,
                ) -> GooglePrivacyDlpV2ListDlpJobsResponseHttpRequest | None: ...

            @typing.type_check_only
            class FileStoreDataProfilesResource(googleapiclient.discovery.Resource):
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleProtobufEmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GooglePrivacyDlpV2FileStoreDataProfileHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> GooglePrivacyDlpV2ListFileStoreDataProfilesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GooglePrivacyDlpV2ListFileStoreDataProfilesResponseHttpRequest,
                    previous_response: GooglePrivacyDlpV2ListFileStoreDataProfilesResponse,
                ) -> (
                    GooglePrivacyDlpV2ListFileStoreDataProfilesResponseHttpRequest
                    | None
                ): ...

            @typing.type_check_only
            class ImageResource(googleapiclient.discovery.Resource):
                def redact(
                    self,
                    *,
                    parent: str,
                    body: GooglePrivacyDlpV2RedactImageRequest = ...,
                    **kwargs: typing.Any,
                ) -> GooglePrivacyDlpV2RedactImageResponseHttpRequest: ...

            @typing.type_check_only
            class InspectTemplatesResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: GooglePrivacyDlpV2CreateInspectTemplateRequest = ...,
                    **kwargs: typing.Any,
                ) -> GooglePrivacyDlpV2InspectTemplateHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleProtobufEmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GooglePrivacyDlpV2InspectTemplateHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    locationId: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> GooglePrivacyDlpV2ListInspectTemplatesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GooglePrivacyDlpV2ListInspectTemplatesResponseHttpRequest,
                    previous_response: GooglePrivacyDlpV2ListInspectTemplatesResponse,
                ) -> (
                    GooglePrivacyDlpV2ListInspectTemplatesResponseHttpRequest | None
                ): ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GooglePrivacyDlpV2UpdateInspectTemplateRequest = ...,
                    **kwargs: typing.Any,
                ) -> GooglePrivacyDlpV2InspectTemplateHttpRequest: ...

            @typing.type_check_only
            class JobTriggersResource(googleapiclient.discovery.Resource):
                def activate(
                    self,
                    *,
                    name: str,
                    body: GooglePrivacyDlpV2ActivateJobTriggerRequest = ...,
                    **kwargs: typing.Any,
                ) -> GooglePrivacyDlpV2DlpJobHttpRequest: ...
                def create(
                    self,
                    *,
                    parent: str,
                    body: GooglePrivacyDlpV2CreateJobTriggerRequest = ...,
                    **kwargs: typing.Any,
                ) -> GooglePrivacyDlpV2JobTriggerHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleProtobufEmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GooglePrivacyDlpV2JobTriggerHttpRequest: ...
                def hybridInspect(
                    self,
                    *,
                    name: str,
                    body: GooglePrivacyDlpV2HybridInspectJobTriggerRequest = ...,
                    **kwargs: typing.Any,
                ) -> GooglePrivacyDlpV2HybridInspectResponseHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    locationId: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    type: typing_extensions.Literal[
                        "DLP_JOB_TYPE_UNSPECIFIED", "INSPECT_JOB", "RISK_ANALYSIS_JOB"
                    ] = ...,
                    **kwargs: typing.Any,
                ) -> GooglePrivacyDlpV2ListJobTriggersResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GooglePrivacyDlpV2ListJobTriggersResponseHttpRequest,
                    previous_response: GooglePrivacyDlpV2ListJobTriggersResponse,
                ) -> GooglePrivacyDlpV2ListJobTriggersResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GooglePrivacyDlpV2UpdateJobTriggerRequest = ...,
                    **kwargs: typing.Any,
                ) -> GooglePrivacyDlpV2JobTriggerHttpRequest: ...

            @typing.type_check_only
            class ProjectDataProfilesResource(googleapiclient.discovery.Resource):
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GooglePrivacyDlpV2ProjectDataProfileHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> GooglePrivacyDlpV2ListProjectDataProfilesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GooglePrivacyDlpV2ListProjectDataProfilesResponseHttpRequest,
                    previous_response: GooglePrivacyDlpV2ListProjectDataProfilesResponse,
                ) -> (
                    GooglePrivacyDlpV2ListProjectDataProfilesResponseHttpRequest | None
                ): ...

            @typing.type_check_only
            class StoredInfoTypesResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: GooglePrivacyDlpV2CreateStoredInfoTypeRequest = ...,
                    **kwargs: typing.Any,
                ) -> GooglePrivacyDlpV2StoredInfoTypeHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleProtobufEmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GooglePrivacyDlpV2StoredInfoTypeHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    locationId: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> GooglePrivacyDlpV2ListStoredInfoTypesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GooglePrivacyDlpV2ListStoredInfoTypesResponseHttpRequest,
                    previous_response: GooglePrivacyDlpV2ListStoredInfoTypesResponse,
                ) -> (
                    GooglePrivacyDlpV2ListStoredInfoTypesResponseHttpRequest | None
                ): ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GooglePrivacyDlpV2UpdateStoredInfoTypeRequest = ...,
                    **kwargs: typing.Any,
                ) -> GooglePrivacyDlpV2StoredInfoTypeHttpRequest: ...

            @typing.type_check_only
            class TableDataProfilesResource(googleapiclient.discovery.Resource):
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleProtobufEmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GooglePrivacyDlpV2TableDataProfileHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> GooglePrivacyDlpV2ListTableDataProfilesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GooglePrivacyDlpV2ListTableDataProfilesResponseHttpRequest,
                    previous_response: GooglePrivacyDlpV2ListTableDataProfilesResponse,
                ) -> (
                    GooglePrivacyDlpV2ListTableDataProfilesResponseHttpRequest | None
                ): ...

            def columnDataProfiles(self) -> ColumnDataProfilesResource: ...
            def connections(self) -> ConnectionsResource: ...
            def content(self) -> ContentResource: ...
            def deidentifyTemplates(self) -> DeidentifyTemplatesResource: ...
            def discoveryConfigs(self) -> DiscoveryConfigsResource: ...
            def dlpJobs(self) -> DlpJobsResource: ...
            def fileStoreDataProfiles(self) -> FileStoreDataProfilesResource: ...
            def image(self) -> ImageResource: ...
            def inspectTemplates(self) -> InspectTemplatesResource: ...
            def jobTriggers(self) -> JobTriggersResource: ...
            def projectDataProfiles(self) -> ProjectDataProfilesResource: ...
            def storedInfoTypes(self) -> StoredInfoTypesResource: ...
            def tableDataProfiles(self) -> TableDataProfilesResource: ...

        @typing.type_check_only
        class StoredInfoTypesResource(googleapiclient.discovery.Resource):
            def create(
                self,
                *,
                parent: str,
                body: GooglePrivacyDlpV2CreateStoredInfoTypeRequest = ...,
                **kwargs: typing.Any,
            ) -> GooglePrivacyDlpV2StoredInfoTypeHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleProtobufEmptyHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GooglePrivacyDlpV2StoredInfoTypeHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                locationId: str = ...,
                orderBy: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any,
            ) -> GooglePrivacyDlpV2ListStoredInfoTypesResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: GooglePrivacyDlpV2ListStoredInfoTypesResponseHttpRequest,
                previous_response: GooglePrivacyDlpV2ListStoredInfoTypesResponse,
            ) -> GooglePrivacyDlpV2ListStoredInfoTypesResponseHttpRequest | None: ...
            def patch(
                self,
                *,
                name: str,
                body: GooglePrivacyDlpV2UpdateStoredInfoTypeRequest = ...,
                **kwargs: typing.Any,
            ) -> GooglePrivacyDlpV2StoredInfoTypeHttpRequest: ...

        def content(self) -> ContentResource: ...
        def deidentifyTemplates(self) -> DeidentifyTemplatesResource: ...
        def dlpJobs(self) -> DlpJobsResource: ...
        def image(self) -> ImageResource: ...
        def inspectTemplates(self) -> InspectTemplatesResource: ...
        def jobTriggers(self) -> JobTriggersResource: ...
        def locations(self) -> LocationsResource: ...
        def storedInfoTypes(self) -> StoredInfoTypesResource: ...

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
    def infoTypes(self) -> InfoTypesResource: ...
    def locations(self) -> LocationsResource: ...
    def organizations(self) -> OrganizationsResource: ...
    def projects(self) -> ProjectsResource: ...

@typing.type_check_only
class GooglePrivacyDlpV2ColumnDataProfileHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GooglePrivacyDlpV2ColumnDataProfile: ...

@typing.type_check_only
class GooglePrivacyDlpV2ConnectionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GooglePrivacyDlpV2Connection: ...

@typing.type_check_only
class GooglePrivacyDlpV2DeidentifyContentResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GooglePrivacyDlpV2DeidentifyContentResponse: ...

@typing.type_check_only
class GooglePrivacyDlpV2DeidentifyTemplateHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GooglePrivacyDlpV2DeidentifyTemplate: ...

@typing.type_check_only
class GooglePrivacyDlpV2DiscoveryConfigHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GooglePrivacyDlpV2DiscoveryConfig: ...

@typing.type_check_only
class GooglePrivacyDlpV2DlpJobHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GooglePrivacyDlpV2DlpJob: ...

@typing.type_check_only
class GooglePrivacyDlpV2FileStoreDataProfileHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GooglePrivacyDlpV2FileStoreDataProfile: ...

@typing.type_check_only
class GooglePrivacyDlpV2HybridInspectResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GooglePrivacyDlpV2HybridInspectResponse: ...

@typing.type_check_only
class GooglePrivacyDlpV2InspectContentResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GooglePrivacyDlpV2InspectContentResponse: ...

@typing.type_check_only
class GooglePrivacyDlpV2InspectTemplateHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GooglePrivacyDlpV2InspectTemplate: ...

@typing.type_check_only
class GooglePrivacyDlpV2JobTriggerHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GooglePrivacyDlpV2JobTrigger: ...

@typing.type_check_only
class GooglePrivacyDlpV2ListColumnDataProfilesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GooglePrivacyDlpV2ListColumnDataProfilesResponse: ...

@typing.type_check_only
class GooglePrivacyDlpV2ListConnectionsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GooglePrivacyDlpV2ListConnectionsResponse: ...

@typing.type_check_only
class GooglePrivacyDlpV2ListDeidentifyTemplatesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GooglePrivacyDlpV2ListDeidentifyTemplatesResponse: ...

@typing.type_check_only
class GooglePrivacyDlpV2ListDiscoveryConfigsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GooglePrivacyDlpV2ListDiscoveryConfigsResponse: ...

@typing.type_check_only
class GooglePrivacyDlpV2ListDlpJobsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GooglePrivacyDlpV2ListDlpJobsResponse: ...

@typing.type_check_only
class GooglePrivacyDlpV2ListFileStoreDataProfilesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GooglePrivacyDlpV2ListFileStoreDataProfilesResponse: ...

@typing.type_check_only
class GooglePrivacyDlpV2ListInfoTypesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GooglePrivacyDlpV2ListInfoTypesResponse: ...

@typing.type_check_only
class GooglePrivacyDlpV2ListInspectTemplatesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GooglePrivacyDlpV2ListInspectTemplatesResponse: ...

@typing.type_check_only
class GooglePrivacyDlpV2ListJobTriggersResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GooglePrivacyDlpV2ListJobTriggersResponse: ...

@typing.type_check_only
class GooglePrivacyDlpV2ListProjectDataProfilesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GooglePrivacyDlpV2ListProjectDataProfilesResponse: ...

@typing.type_check_only
class GooglePrivacyDlpV2ListStoredInfoTypesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GooglePrivacyDlpV2ListStoredInfoTypesResponse: ...

@typing.type_check_only
class GooglePrivacyDlpV2ListTableDataProfilesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GooglePrivacyDlpV2ListTableDataProfilesResponse: ...

@typing.type_check_only
class GooglePrivacyDlpV2ProjectDataProfileHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GooglePrivacyDlpV2ProjectDataProfile: ...

@typing.type_check_only
class GooglePrivacyDlpV2RedactImageResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GooglePrivacyDlpV2RedactImageResponse: ...

@typing.type_check_only
class GooglePrivacyDlpV2ReidentifyContentResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GooglePrivacyDlpV2ReidentifyContentResponse: ...

@typing.type_check_only
class GooglePrivacyDlpV2SearchConnectionsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GooglePrivacyDlpV2SearchConnectionsResponse: ...

@typing.type_check_only
class GooglePrivacyDlpV2StoredInfoTypeHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GooglePrivacyDlpV2StoredInfoType: ...

@typing.type_check_only
class GooglePrivacyDlpV2TableDataProfileHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GooglePrivacyDlpV2TableDataProfile: ...

@typing.type_check_only
class GoogleProtobufEmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleProtobufEmpty: ...
