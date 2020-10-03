import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class DLPResource(googleapiclient.discovery.Resource):
    class OrganizationsResource(googleapiclient.discovery.Resource):
        class LocationsResource(googleapiclient.discovery.Resource):
            class StoredInfoTypesResource(googleapiclient.discovery.Resource):
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GooglePrivacyDlpV2StoredInfoTypeHttpRequest: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GooglePrivacyDlpV2UpdateStoredInfoTypeRequest = ...,
                    **kwargs: typing.Any
                ) -> GooglePrivacyDlpV2StoredInfoTypeHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageToken: str = ...,
                    locationId: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    **kwargs: typing.Any
                ) -> GooglePrivacyDlpV2ListStoredInfoTypesResponseHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleProtobufEmptyHttpRequest: ...
                def create(
                    self,
                    *,
                    parent: str,
                    body: GooglePrivacyDlpV2CreateStoredInfoTypeRequest = ...,
                    **kwargs: typing.Any
                ) -> GooglePrivacyDlpV2StoredInfoTypeHttpRequest: ...
            class InspectTemplatesResource(googleapiclient.discovery.Resource):
                def patch(
                    self,
                    *,
                    name: str,
                    body: GooglePrivacyDlpV2UpdateInspectTemplateRequest = ...,
                    **kwargs: typing.Any
                ) -> GooglePrivacyDlpV2InspectTemplateHttpRequest: ...
                def create(
                    self,
                    *,
                    parent: str,
                    body: GooglePrivacyDlpV2CreateInspectTemplateRequest = ...,
                    **kwargs: typing.Any
                ) -> GooglePrivacyDlpV2InspectTemplateHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    locationId: str = ...,
                    pageToken: str = ...,
                    orderBy: str = ...,
                    **kwargs: typing.Any
                ) -> GooglePrivacyDlpV2ListInspectTemplatesResponseHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleProtobufEmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GooglePrivacyDlpV2InspectTemplateHttpRequest: ...
            class DeidentifyTemplatesResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: GooglePrivacyDlpV2CreateDeidentifyTemplateRequest = ...,
                    **kwargs: typing.Any
                ) -> GooglePrivacyDlpV2DeidentifyTemplateHttpRequest: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GooglePrivacyDlpV2UpdateDeidentifyTemplateRequest = ...,
                    **kwargs: typing.Any
                ) -> GooglePrivacyDlpV2DeidentifyTemplateHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    locationId: str = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> GooglePrivacyDlpV2ListDeidentifyTemplatesResponseHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GooglePrivacyDlpV2DeidentifyTemplateHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleProtobufEmptyHttpRequest: ...
            def storedInfoTypes(self) -> StoredInfoTypesResource: ...
            def inspectTemplates(self) -> InspectTemplatesResource: ...
            def deidentifyTemplates(self) -> DeidentifyTemplatesResource: ...
        class StoredInfoTypesResource(googleapiclient.discovery.Resource):
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleProtobufEmptyHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GooglePrivacyDlpV2StoredInfoTypeHttpRequest: ...
            def create(
                self,
                *,
                parent: str,
                body: GooglePrivacyDlpV2CreateStoredInfoTypeRequest = ...,
                **kwargs: typing.Any
            ) -> GooglePrivacyDlpV2StoredInfoTypeHttpRequest: ...
            def patch(
                self,
                *,
                name: str,
                body: GooglePrivacyDlpV2UpdateStoredInfoTypeRequest = ...,
                **kwargs: typing.Any
            ) -> GooglePrivacyDlpV2StoredInfoTypeHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                orderBy: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                locationId: str = ...,
                **kwargs: typing.Any
            ) -> GooglePrivacyDlpV2ListStoredInfoTypesResponseHttpRequest: ...
        class InspectTemplatesResource(googleapiclient.discovery.Resource):
            def list(
                self,
                *,
                parent: str,
                pageToken: str = ...,
                locationId: str = ...,
                orderBy: str = ...,
                pageSize: int = ...,
                **kwargs: typing.Any
            ) -> GooglePrivacyDlpV2ListInspectTemplatesResponseHttpRequest: ...
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
            def patch(
                self,
                *,
                name: str,
                body: GooglePrivacyDlpV2UpdateInspectTemplateRequest = ...,
                **kwargs: typing.Any
            ) -> GooglePrivacyDlpV2InspectTemplateHttpRequest: ...
        class DeidentifyTemplatesResource(googleapiclient.discovery.Resource):
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleProtobufEmptyHttpRequest: ...
            def create(
                self,
                *,
                parent: str,
                body: GooglePrivacyDlpV2CreateDeidentifyTemplateRequest = ...,
                **kwargs: typing.Any
            ) -> GooglePrivacyDlpV2DeidentifyTemplateHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GooglePrivacyDlpV2DeidentifyTemplateHttpRequest: ...
            def patch(
                self,
                *,
                name: str,
                body: GooglePrivacyDlpV2UpdateDeidentifyTemplateRequest = ...,
                **kwargs: typing.Any
            ) -> GooglePrivacyDlpV2DeidentifyTemplateHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageToken: str = ...,
                orderBy: str = ...,
                locationId: str = ...,
                pageSize: int = ...,
                **kwargs: typing.Any
            ) -> GooglePrivacyDlpV2ListDeidentifyTemplatesResponseHttpRequest: ...
        def locations(self) -> LocationsResource: ...
        def storedInfoTypes(self) -> StoredInfoTypesResource: ...
        def inspectTemplates(self) -> InspectTemplatesResource: ...
        def deidentifyTemplates(self) -> DeidentifyTemplatesResource: ...
    class LocationsResource(googleapiclient.discovery.Resource):
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
    class InfoTypesResource(googleapiclient.discovery.Resource):
        def list(
            self,
            *,
            languageCode: str = ...,
            parent: str = ...,
            filter: str = ...,
            locationId: str = ...,
            **kwargs: typing.Any
        ) -> GooglePrivacyDlpV2ListInfoTypesResponseHttpRequest: ...
    class ProjectsResource(googleapiclient.discovery.Resource):
        class StoredInfoTypesResource(googleapiclient.discovery.Resource):
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GooglePrivacyDlpV2StoredInfoTypeHttpRequest: ...
            def patch(
                self,
                *,
                name: str,
                body: GooglePrivacyDlpV2UpdateStoredInfoTypeRequest = ...,
                **kwargs: typing.Any
            ) -> GooglePrivacyDlpV2StoredInfoTypeHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                locationId: str = ...,
                pageSize: int = ...,
                orderBy: str = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> GooglePrivacyDlpV2ListStoredInfoTypesResponseHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleProtobufEmptyHttpRequest: ...
            def create(
                self,
                *,
                parent: str,
                body: GooglePrivacyDlpV2CreateStoredInfoTypeRequest = ...,
                **kwargs: typing.Any
            ) -> GooglePrivacyDlpV2StoredInfoTypeHttpRequest: ...
        class InspectTemplatesResource(googleapiclient.discovery.Resource):
            def create(
                self,
                *,
                parent: str,
                body: GooglePrivacyDlpV2CreateInspectTemplateRequest = ...,
                **kwargs: typing.Any
            ) -> GooglePrivacyDlpV2InspectTemplateHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                orderBy: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                locationId: str = ...,
                **kwargs: typing.Any
            ) -> GooglePrivacyDlpV2ListInspectTemplatesResponseHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GooglePrivacyDlpV2InspectTemplateHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleProtobufEmptyHttpRequest: ...
            def patch(
                self,
                *,
                name: str,
                body: GooglePrivacyDlpV2UpdateInspectTemplateRequest = ...,
                **kwargs: typing.Any
            ) -> GooglePrivacyDlpV2InspectTemplateHttpRequest: ...
        class ImageResource(googleapiclient.discovery.Resource):
            def redact(
                self,
                *,
                parent: str,
                body: GooglePrivacyDlpV2RedactImageRequest = ...,
                **kwargs: typing.Any
            ) -> GooglePrivacyDlpV2RedactImageResponseHttpRequest: ...
        class LocationsResource(googleapiclient.discovery.Resource):
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
                def patch(
                    self,
                    *,
                    name: str,
                    body: GooglePrivacyDlpV2UpdateInspectTemplateRequest = ...,
                    **kwargs: typing.Any
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
            class ContentResource(googleapiclient.discovery.Resource):
                def deidentify(
                    self,
                    *,
                    parent: str,
                    body: GooglePrivacyDlpV2DeidentifyContentRequest = ...,
                    **kwargs: typing.Any
                ) -> GooglePrivacyDlpV2DeidentifyContentResponseHttpRequest: ...
                def reidentify(
                    self,
                    *,
                    parent: str,
                    body: GooglePrivacyDlpV2ReidentifyContentRequest = ...,
                    **kwargs: typing.Any
                ) -> GooglePrivacyDlpV2ReidentifyContentResponseHttpRequest: ...
                def inspect(
                    self,
                    *,
                    parent: str,
                    body: GooglePrivacyDlpV2InspectContentRequest = ...,
                    **kwargs: typing.Any
                ) -> GooglePrivacyDlpV2InspectContentResponseHttpRequest: ...
            class StoredInfoTypesResource(googleapiclient.discovery.Resource):
                def patch(
                    self,
                    *,
                    name: str,
                    body: GooglePrivacyDlpV2UpdateStoredInfoTypeRequest = ...,
                    **kwargs: typing.Any
                ) -> GooglePrivacyDlpV2StoredInfoTypeHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleProtobufEmptyHttpRequest: ...
                def create(
                    self,
                    *,
                    parent: str,
                    body: GooglePrivacyDlpV2CreateStoredInfoTypeRequest = ...,
                    **kwargs: typing.Any
                ) -> GooglePrivacyDlpV2StoredInfoTypeHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GooglePrivacyDlpV2StoredInfoTypeHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    locationId: str = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> GooglePrivacyDlpV2ListStoredInfoTypesResponseHttpRequest: ...
            class JobTriggersResource(googleapiclient.discovery.Resource):
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleProtobufEmptyHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    locationId: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    orderBy: str = ...,
                    **kwargs: typing.Any
                ) -> GooglePrivacyDlpV2ListJobTriggersResponseHttpRequest: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GooglePrivacyDlpV2UpdateJobTriggerRequest = ...,
                    **kwargs: typing.Any
                ) -> GooglePrivacyDlpV2JobTriggerHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GooglePrivacyDlpV2JobTriggerHttpRequest: ...
                def create(
                    self,
                    *,
                    parent: str,
                    body: GooglePrivacyDlpV2CreateJobTriggerRequest = ...,
                    **kwargs: typing.Any
                ) -> GooglePrivacyDlpV2JobTriggerHttpRequest: ...
                def activate(
                    self,
                    *,
                    name: str,
                    body: GooglePrivacyDlpV2ActivateJobTriggerRequest = ...,
                    **kwargs: typing.Any
                ) -> GooglePrivacyDlpV2DlpJobHttpRequest: ...
                def hybridInspect(
                    self,
                    *,
                    name: str,
                    body: GooglePrivacyDlpV2HybridInspectJobTriggerRequest = ...,
                    **kwargs: typing.Any
                ) -> GooglePrivacyDlpV2HybridInspectResponseHttpRequest: ...
            class ImageResource(googleapiclient.discovery.Resource):
                def redact(
                    self,
                    *,
                    parent: str,
                    body: GooglePrivacyDlpV2RedactImageRequest = ...,
                    **kwargs: typing.Any
                ) -> GooglePrivacyDlpV2RedactImageResponseHttpRequest: ...
            class DlpJobsResource(googleapiclient.discovery.Resource):
                def cancel(
                    self,
                    *,
                    name: str,
                    body: GooglePrivacyDlpV2CancelDlpJobRequest = ...,
                    **kwargs: typing.Any
                ) -> GoogleProtobufEmptyHttpRequest: ...
                def finish(
                    self,
                    *,
                    name: str,
                    body: GooglePrivacyDlpV2FinishDlpJobRequest = ...,
                    **kwargs: typing.Any
                ) -> GoogleProtobufEmptyHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    orderBy: str = ...,
                    pageToken: str = ...,
                    filter: str = ...,
                    locationId: str = ...,
                    type: typing_extensions.Literal[
                        "DLP_JOB_TYPE_UNSPECIFIED", "INSPECT_JOB", "RISK_ANALYSIS_JOB"
                    ] = ...,
                    **kwargs: typing.Any
                ) -> GooglePrivacyDlpV2ListDlpJobsResponseHttpRequest: ...
                def create(
                    self,
                    *,
                    parent: str,
                    body: GooglePrivacyDlpV2CreateDlpJobRequest = ...,
                    **kwargs: typing.Any
                ) -> GooglePrivacyDlpV2DlpJobHttpRequest: ...
                def hybridInspect(
                    self,
                    *,
                    name: str,
                    body: GooglePrivacyDlpV2HybridInspectDlpJobRequest = ...,
                    **kwargs: typing.Any
                ) -> GooglePrivacyDlpV2HybridInspectResponseHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GooglePrivacyDlpV2DlpJobHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleProtobufEmptyHttpRequest: ...
            class DeidentifyTemplatesResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: GooglePrivacyDlpV2CreateDeidentifyTemplateRequest = ...,
                    **kwargs: typing.Any
                ) -> GooglePrivacyDlpV2DeidentifyTemplateHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GooglePrivacyDlpV2DeidentifyTemplateHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleProtobufEmptyHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    locationId: str = ...,
                    **kwargs: typing.Any
                ) -> GooglePrivacyDlpV2ListDeidentifyTemplatesResponseHttpRequest: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GooglePrivacyDlpV2UpdateDeidentifyTemplateRequest = ...,
                    **kwargs: typing.Any
                ) -> GooglePrivacyDlpV2DeidentifyTemplateHttpRequest: ...
            def inspectTemplates(self) -> InspectTemplatesResource: ...
            def content(self) -> ContentResource: ...
            def storedInfoTypes(self) -> StoredInfoTypesResource: ...
            def jobTriggers(self) -> JobTriggersResource: ...
            def image(self) -> ImageResource: ...
            def dlpJobs(self) -> DlpJobsResource: ...
            def deidentifyTemplates(self) -> DeidentifyTemplatesResource: ...
        class DlpJobsResource(googleapiclient.discovery.Resource):
            def cancel(
                self,
                *,
                name: str,
                body: GooglePrivacyDlpV2CancelDlpJobRequest = ...,
                **kwargs: typing.Any
            ) -> GoogleProtobufEmptyHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GooglePrivacyDlpV2DlpJobHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                type: typing_extensions.Literal[
                    "DLP_JOB_TYPE_UNSPECIFIED", "INSPECT_JOB", "RISK_ANALYSIS_JOB"
                ] = ...,
                locationId: str = ...,
                orderBy: str = ...,
                pageToken: str = ...,
                filter: str = ...,
                pageSize: int = ...,
                **kwargs: typing.Any
            ) -> GooglePrivacyDlpV2ListDlpJobsResponseHttpRequest: ...
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
        class DeidentifyTemplatesResource(googleapiclient.discovery.Resource):
            def patch(
                self,
                *,
                name: str,
                body: GooglePrivacyDlpV2UpdateDeidentifyTemplateRequest = ...,
                **kwargs: typing.Any
            ) -> GooglePrivacyDlpV2DeidentifyTemplateHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleProtobufEmptyHttpRequest: ...
            def create(
                self,
                *,
                parent: str,
                body: GooglePrivacyDlpV2CreateDeidentifyTemplateRequest = ...,
                **kwargs: typing.Any
            ) -> GooglePrivacyDlpV2DeidentifyTemplateHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageToken: str = ...,
                locationId: str = ...,
                pageSize: int = ...,
                orderBy: str = ...,
                **kwargs: typing.Any
            ) -> GooglePrivacyDlpV2ListDeidentifyTemplatesResponseHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GooglePrivacyDlpV2DeidentifyTemplateHttpRequest: ...
        class ContentResource(googleapiclient.discovery.Resource):
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
            def deidentify(
                self,
                *,
                parent: str,
                body: GooglePrivacyDlpV2DeidentifyContentRequest = ...,
                **kwargs: typing.Any
            ) -> GooglePrivacyDlpV2DeidentifyContentResponseHttpRequest: ...
        class JobTriggersResource(googleapiclient.discovery.Resource):
            def list(
                self,
                *,
                parent: str,
                orderBy: str = ...,
                filter: str = ...,
                pageToken: str = ...,
                pageSize: int = ...,
                locationId: str = ...,
                **kwargs: typing.Any
            ) -> GooglePrivacyDlpV2ListJobTriggersResponseHttpRequest: ...
            def patch(
                self,
                *,
                name: str,
                body: GooglePrivacyDlpV2UpdateJobTriggerRequest = ...,
                **kwargs: typing.Any
            ) -> GooglePrivacyDlpV2JobTriggerHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleProtobufEmptyHttpRequest: ...
            def activate(
                self,
                *,
                name: str,
                body: GooglePrivacyDlpV2ActivateJobTriggerRequest = ...,
                **kwargs: typing.Any
            ) -> GooglePrivacyDlpV2DlpJobHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GooglePrivacyDlpV2JobTriggerHttpRequest: ...
            def create(
                self,
                *,
                parent: str,
                body: GooglePrivacyDlpV2CreateJobTriggerRequest = ...,
                **kwargs: typing.Any
            ) -> GooglePrivacyDlpV2JobTriggerHttpRequest: ...
        def storedInfoTypes(self) -> StoredInfoTypesResource: ...
        def inspectTemplates(self) -> InspectTemplatesResource: ...
        def image(self) -> ImageResource: ...
        def locations(self) -> LocationsResource: ...
        def dlpJobs(self) -> DlpJobsResource: ...
        def deidentifyTemplates(self) -> DeidentifyTemplatesResource: ...
        def content(self) -> ContentResource: ...
        def jobTriggers(self) -> JobTriggersResource: ...
    def organizations(self) -> OrganizationsResource: ...
    def locations(self) -> LocationsResource: ...
    def infoTypes(self) -> InfoTypesResource: ...
    def projects(self) -> ProjectsResource: ...

class GooglePrivacyDlpV2DlpJobHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GooglePrivacyDlpV2DlpJob: ...

class GooglePrivacyDlpV2HybridInspectResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GooglePrivacyDlpV2HybridInspectResponse: ...

class GooglePrivacyDlpV2ReidentifyContentResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GooglePrivacyDlpV2ReidentifyContentResponse: ...

class GooglePrivacyDlpV2ListStoredInfoTypesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GooglePrivacyDlpV2ListStoredInfoTypesResponse: ...

class GooglePrivacyDlpV2StoredInfoTypeHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GooglePrivacyDlpV2StoredInfoType: ...

class GoogleProtobufEmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleProtobufEmpty: ...

class GooglePrivacyDlpV2RedactImageResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GooglePrivacyDlpV2RedactImageResponse: ...

class GooglePrivacyDlpV2ListDlpJobsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GooglePrivacyDlpV2ListDlpJobsResponse: ...

class GooglePrivacyDlpV2JobTriggerHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GooglePrivacyDlpV2JobTrigger: ...

class GooglePrivacyDlpV2ListInfoTypesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GooglePrivacyDlpV2ListInfoTypesResponse: ...

class GooglePrivacyDlpV2ListInspectTemplatesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GooglePrivacyDlpV2ListInspectTemplatesResponse: ...

class GooglePrivacyDlpV2InspectTemplateHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GooglePrivacyDlpV2InspectTemplate: ...

class GooglePrivacyDlpV2DeidentifyContentResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GooglePrivacyDlpV2DeidentifyContentResponse: ...

class GooglePrivacyDlpV2DeidentifyTemplateHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GooglePrivacyDlpV2DeidentifyTemplate: ...

class GooglePrivacyDlpV2ListDeidentifyTemplatesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GooglePrivacyDlpV2ListDeidentifyTemplatesResponse: ...

class GooglePrivacyDlpV2InspectContentResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GooglePrivacyDlpV2InspectContentResponse: ...

class GooglePrivacyDlpV2ListJobTriggersResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GooglePrivacyDlpV2ListJobTriggersResponse: ...
