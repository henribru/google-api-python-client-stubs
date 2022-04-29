import collections.abc
import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

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
            **kwargs: typing.Any
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
                **kwargs: typing.Any
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
                **kwargs: typing.Any
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
                **kwargs: typing.Any
            ) -> GooglePrivacyDlpV2ListDeidentifyTemplatesResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: GooglePrivacyDlpV2ListDeidentifyTemplatesResponseHttpRequest,
                previous_response: GooglePrivacyDlpV2ListDeidentifyTemplatesResponse,
            ) -> GooglePrivacyDlpV2ListDeidentifyTemplatesResponseHttpRequest | None: ...
            def patch(
                self,
                *,
                name: str,
                body: GooglePrivacyDlpV2UpdateDeidentifyTemplateRequest = ...,
                **kwargs: typing.Any
            ) -> GooglePrivacyDlpV2DeidentifyTemplateHttpRequest: ...

        @typing.type_check_only
        class InspectTemplatesResource(googleapiclient.discovery.Resource):
            def create(
                self,
                *,
                parent: str,
                body: GooglePrivacyDlpV2CreateInspectTemplateRequest = ...,
                **kwargs: typing.Any
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
                **kwargs: typing.Any
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
                **kwargs: typing.Any
            ) -> GooglePrivacyDlpV2InspectTemplateHttpRequest: ...

        @typing.type_check_only
        class LocationsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class DeidentifyTemplatesResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: GooglePrivacyDlpV2CreateDeidentifyTemplateRequest = ...,
                    **kwargs: typing.Any
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
                    **kwargs: typing.Any
                ) -> GooglePrivacyDlpV2ListDeidentifyTemplatesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GooglePrivacyDlpV2ListDeidentifyTemplatesResponseHttpRequest,
                    previous_response: GooglePrivacyDlpV2ListDeidentifyTemplatesResponse,
                ) -> GooglePrivacyDlpV2ListDeidentifyTemplatesResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GooglePrivacyDlpV2UpdateDeidentifyTemplateRequest = ...,
                    **kwargs: typing.Any
                ) -> GooglePrivacyDlpV2DeidentifyTemplateHttpRequest: ...

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
                    **kwargs: typing.Any
                ) -> GooglePrivacyDlpV2ListDlpJobsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GooglePrivacyDlpV2ListDlpJobsResponseHttpRequest,
                    previous_response: GooglePrivacyDlpV2ListDlpJobsResponse,
                ) -> GooglePrivacyDlpV2ListDlpJobsResponseHttpRequest | None: ...

            @typing.type_check_only
            class InspectTemplatesResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: GooglePrivacyDlpV2CreateInspectTemplateRequest = ...,
                    **kwargs: typing.Any
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
                    **kwargs: typing.Any
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
                    **kwargs: typing.Any
                ) -> GooglePrivacyDlpV2InspectTemplateHttpRequest: ...

            @typing.type_check_only
            class JobTriggersResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: GooglePrivacyDlpV2CreateJobTriggerRequest = ...,
                    **kwargs: typing.Any
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
                    **kwargs: typing.Any
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
                    **kwargs: typing.Any
                ) -> GooglePrivacyDlpV2JobTriggerHttpRequest: ...

            @typing.type_check_only
            class StoredInfoTypesResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: GooglePrivacyDlpV2CreateStoredInfoTypeRequest = ...,
                    **kwargs: typing.Any
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
                    **kwargs: typing.Any
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
                    **kwargs: typing.Any
                ) -> GooglePrivacyDlpV2StoredInfoTypeHttpRequest: ...

            def deidentifyTemplates(self) -> DeidentifyTemplatesResource: ...
            def dlpJobs(self) -> DlpJobsResource: ...
            def inspectTemplates(self) -> InspectTemplatesResource: ...
            def jobTriggers(self) -> JobTriggersResource: ...
            def storedInfoTypes(self) -> StoredInfoTypesResource: ...

        @typing.type_check_only
        class StoredInfoTypesResource(googleapiclient.discovery.Resource):
            def create(
                self,
                *,
                parent: str,
                body: GooglePrivacyDlpV2CreateStoredInfoTypeRequest = ...,
                **kwargs: typing.Any
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
                **kwargs: typing.Any
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
                **kwargs: typing.Any
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
                **kwargs: typing.Any
            ) -> GooglePrivacyDlpV2DeidentifyContentResponseHttpRequest: ...
            def inspect(
                self,
                *,
                parent: str,
                body: GooglePrivacyDlpV2InspectContentRequest = ...,
                **kwargs: typing.Any
            ) -> GooglePrivacyDlpV2InspectContentResponseHttpRequest: ...
            def reidentify(
                self,
                *,
                parent: str,
                body: GooglePrivacyDlpV2ReidentifyContentRequest = ...,
                **kwargs: typing.Any
            ) -> GooglePrivacyDlpV2ReidentifyContentResponseHttpRequest: ...

        @typing.type_check_only
        class DeidentifyTemplatesResource(googleapiclient.discovery.Resource):
            def create(
                self,
                *,
                parent: str,
                body: GooglePrivacyDlpV2CreateDeidentifyTemplateRequest = ...,
                **kwargs: typing.Any
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
                **kwargs: typing.Any
            ) -> GooglePrivacyDlpV2ListDeidentifyTemplatesResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: GooglePrivacyDlpV2ListDeidentifyTemplatesResponseHttpRequest,
                previous_response: GooglePrivacyDlpV2ListDeidentifyTemplatesResponse,
            ) -> GooglePrivacyDlpV2ListDeidentifyTemplatesResponseHttpRequest | None: ...
            def patch(
                self,
                *,
                name: str,
                body: GooglePrivacyDlpV2UpdateDeidentifyTemplateRequest = ...,
                **kwargs: typing.Any
            ) -> GooglePrivacyDlpV2DeidentifyTemplateHttpRequest: ...

        @typing.type_check_only
        class DlpJobsResource(googleapiclient.discovery.Resource):
            def cancel(
                self,
                *,
                name: str,
                body: GooglePrivacyDlpV2CancelDlpJobRequest = ...,
                **kwargs: typing.Any
            ) -> GoogleProtobufEmptyHttpRequest: ...
            def create(
                self,
                *,
                parent: str,
                body: GooglePrivacyDlpV2CreateDlpJobRequest = ...,
                **kwargs: typing.Any
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
                **kwargs: typing.Any
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
                **kwargs: typing.Any
            ) -> GooglePrivacyDlpV2RedactImageResponseHttpRequest: ...

        @typing.type_check_only
        class InspectTemplatesResource(googleapiclient.discovery.Resource):
            def create(
                self,
                *,
                parent: str,
                body: GooglePrivacyDlpV2CreateInspectTemplateRequest = ...,
                **kwargs: typing.Any
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
                **kwargs: typing.Any
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
                **kwargs: typing.Any
            ) -> GooglePrivacyDlpV2InspectTemplateHttpRequest: ...

        @typing.type_check_only
        class JobTriggersResource(googleapiclient.discovery.Resource):
            def activate(
                self,
                *,
                name: str,
                body: GooglePrivacyDlpV2ActivateJobTriggerRequest = ...,
                **kwargs: typing.Any
            ) -> GooglePrivacyDlpV2DlpJobHttpRequest: ...
            def create(
                self,
                *,
                parent: str,
                body: GooglePrivacyDlpV2CreateJobTriggerRequest = ...,
                **kwargs: typing.Any
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
                **kwargs: typing.Any
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
                **kwargs: typing.Any
            ) -> GooglePrivacyDlpV2JobTriggerHttpRequest: ...

        @typing.type_check_only
        class LocationsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class ContentResource(googleapiclient.discovery.Resource):
                def deidentify(
                    self,
                    *,
                    parent: str,
                    body: GooglePrivacyDlpV2DeidentifyContentRequest = ...,
                    **kwargs: typing.Any
                ) -> GooglePrivacyDlpV2DeidentifyContentResponseHttpRequest: ...
                def inspect(
                    self,
                    *,
                    parent: str,
                    body: GooglePrivacyDlpV2InspectContentRequest = ...,
                    **kwargs: typing.Any
                ) -> GooglePrivacyDlpV2InspectContentResponseHttpRequest: ...
                def reidentify(
                    self,
                    *,
                    parent: str,
                    body: GooglePrivacyDlpV2ReidentifyContentRequest = ...,
                    **kwargs: typing.Any
                ) -> GooglePrivacyDlpV2ReidentifyContentResponseHttpRequest: ...

            @typing.type_check_only
            class DeidentifyTemplatesResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: GooglePrivacyDlpV2CreateDeidentifyTemplateRequest = ...,
                    **kwargs: typing.Any
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
                    **kwargs: typing.Any
                ) -> GooglePrivacyDlpV2ListDeidentifyTemplatesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GooglePrivacyDlpV2ListDeidentifyTemplatesResponseHttpRequest,
                    previous_response: GooglePrivacyDlpV2ListDeidentifyTemplatesResponse,
                ) -> GooglePrivacyDlpV2ListDeidentifyTemplatesResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GooglePrivacyDlpV2UpdateDeidentifyTemplateRequest = ...,
                    **kwargs: typing.Any
                ) -> GooglePrivacyDlpV2DeidentifyTemplateHttpRequest: ...

            @typing.type_check_only
            class DlpJobsResource(googleapiclient.discovery.Resource):
                def cancel(
                    self,
                    *,
                    name: str,
                    body: GooglePrivacyDlpV2CancelDlpJobRequest = ...,
                    **kwargs: typing.Any
                ) -> GoogleProtobufEmptyHttpRequest: ...
                def create(
                    self,
                    *,
                    parent: str,
                    body: GooglePrivacyDlpV2CreateDlpJobRequest = ...,
                    **kwargs: typing.Any
                ) -> GooglePrivacyDlpV2DlpJobHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleProtobufEmptyHttpRequest: ...
                def finish(
                    self,
                    *,
                    name: str,
                    body: GooglePrivacyDlpV2FinishDlpJobRequest = ...,
                    **kwargs: typing.Any
                ) -> GoogleProtobufEmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GooglePrivacyDlpV2DlpJobHttpRequest: ...
                def hybridInspect(
                    self,
                    *,
                    name: str,
                    body: GooglePrivacyDlpV2HybridInspectDlpJobRequest = ...,
                    **kwargs: typing.Any
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
                    **kwargs: typing.Any
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
                    **kwargs: typing.Any
                ) -> GooglePrivacyDlpV2RedactImageResponseHttpRequest: ...

            @typing.type_check_only
            class InspectTemplatesResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: GooglePrivacyDlpV2CreateInspectTemplateRequest = ...,
                    **kwargs: typing.Any
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
                    **kwargs: typing.Any
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
                    **kwargs: typing.Any
                ) -> GooglePrivacyDlpV2InspectTemplateHttpRequest: ...

            @typing.type_check_only
            class JobTriggersResource(googleapiclient.discovery.Resource):
                def activate(
                    self,
                    *,
                    name: str,
                    body: GooglePrivacyDlpV2ActivateJobTriggerRequest = ...,
                    **kwargs: typing.Any
                ) -> GooglePrivacyDlpV2DlpJobHttpRequest: ...
                def create(
                    self,
                    *,
                    parent: str,
                    body: GooglePrivacyDlpV2CreateJobTriggerRequest = ...,
                    **kwargs: typing.Any
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
                    **kwargs: typing.Any
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
                    **kwargs: typing.Any
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
                    **kwargs: typing.Any
                ) -> GooglePrivacyDlpV2JobTriggerHttpRequest: ...

            @typing.type_check_only
            class StoredInfoTypesResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: GooglePrivacyDlpV2CreateStoredInfoTypeRequest = ...,
                    **kwargs: typing.Any
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
                    **kwargs: typing.Any
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
                    **kwargs: typing.Any
                ) -> GooglePrivacyDlpV2StoredInfoTypeHttpRequest: ...

            def content(self) -> ContentResource: ...
            def deidentifyTemplates(self) -> DeidentifyTemplatesResource: ...
            def dlpJobs(self) -> DlpJobsResource: ...
            def image(self) -> ImageResource: ...
            def inspectTemplates(self) -> InspectTemplatesResource: ...
            def jobTriggers(self) -> JobTriggersResource: ...
            def storedInfoTypes(self) -> StoredInfoTypesResource: ...

        @typing.type_check_only
        class StoredInfoTypesResource(googleapiclient.discovery.Resource):
            def create(
                self,
                *,
                parent: str,
                body: GooglePrivacyDlpV2CreateStoredInfoTypeRequest = ...,
                **kwargs: typing.Any
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
                **kwargs: typing.Any
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
                **kwargs: typing.Any
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
        | None = ...,
    ) -> googleapiclient.http.BatchHttpRequest: ...
    def infoTypes(self) -> InfoTypesResource: ...
    def locations(self) -> LocationsResource: ...
    def organizations(self) -> OrganizationsResource: ...
    def projects(self) -> ProjectsResource: ...

@typing.type_check_only
class GooglePrivacyDlpV2DeidentifyContentResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GooglePrivacyDlpV2DeidentifyContentResponse: ...

@typing.type_check_only
class GooglePrivacyDlpV2DeidentifyTemplateHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GooglePrivacyDlpV2DeidentifyTemplate: ...

@typing.type_check_only
class GooglePrivacyDlpV2DlpJobHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GooglePrivacyDlpV2DlpJob: ...

@typing.type_check_only
class GooglePrivacyDlpV2HybridInspectResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GooglePrivacyDlpV2HybridInspectResponse: ...

@typing.type_check_only
class GooglePrivacyDlpV2InspectContentResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GooglePrivacyDlpV2InspectContentResponse: ...

@typing.type_check_only
class GooglePrivacyDlpV2InspectTemplateHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GooglePrivacyDlpV2InspectTemplate: ...

@typing.type_check_only
class GooglePrivacyDlpV2JobTriggerHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GooglePrivacyDlpV2JobTrigger: ...

@typing.type_check_only
class GooglePrivacyDlpV2ListDeidentifyTemplatesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GooglePrivacyDlpV2ListDeidentifyTemplatesResponse: ...

@typing.type_check_only
class GooglePrivacyDlpV2ListDlpJobsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GooglePrivacyDlpV2ListDlpJobsResponse: ...

@typing.type_check_only
class GooglePrivacyDlpV2ListInfoTypesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GooglePrivacyDlpV2ListInfoTypesResponse: ...

@typing.type_check_only
class GooglePrivacyDlpV2ListInspectTemplatesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GooglePrivacyDlpV2ListInspectTemplatesResponse: ...

@typing.type_check_only
class GooglePrivacyDlpV2ListJobTriggersResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GooglePrivacyDlpV2ListJobTriggersResponse: ...

@typing.type_check_only
class GooglePrivacyDlpV2ListStoredInfoTypesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GooglePrivacyDlpV2ListStoredInfoTypesResponse: ...

@typing.type_check_only
class GooglePrivacyDlpV2RedactImageResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GooglePrivacyDlpV2RedactImageResponse: ...

@typing.type_check_only
class GooglePrivacyDlpV2ReidentifyContentResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GooglePrivacyDlpV2ReidentifyContentResponse: ...

@typing.type_check_only
class GooglePrivacyDlpV2StoredInfoTypeHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GooglePrivacyDlpV2StoredInfoType: ...

@typing.type_check_only
class GoogleProtobufEmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleProtobufEmpty: ...
