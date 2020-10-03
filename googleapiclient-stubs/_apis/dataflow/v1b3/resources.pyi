import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class DataflowResource(googleapiclient.discovery.Resource):
    class ProjectsResource(googleapiclient.discovery.Resource):
        class TemplatesResource(googleapiclient.discovery.Resource):
            def create(
                self,
                *,
                projectId: str,
                body: CreateJobFromTemplateRequest = ...,
                **kwargs: typing.Any
            ) -> JobHttpRequest: ...
            def launch(
                self,
                *,
                projectId: str,
                body: LaunchTemplateParameters = ...,
                dynamicTemplate_gcsPath: str = ...,
                location: str = ...,
                validateOnly: bool = ...,
                dynamicTemplate_stagingLocation: str = ...,
                gcsPath: str = ...,
                **kwargs: typing.Any
            ) -> LaunchTemplateResponseHttpRequest: ...
            def get(
                self,
                *,
                projectId: str,
                gcsPath: str = ...,
                view: typing_extensions.Literal["METADATA_ONLY"] = ...,
                location: str = ...,
                **kwargs: typing.Any
            ) -> GetTemplateResponseHttpRequest: ...
        class CatalogTemplatesResource(googleapiclient.discovery.Resource):
            class TemplateVersionsResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: CreateTemplateVersionRequest = ...,
                    **kwargs: typing.Any
                ) -> TemplateVersionHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> TemplateVersionHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def tag(
                self,
                *,
                name: str,
                body: ModifyTemplateVersionTagRequest = ...,
                **kwargs: typing.Any
            ) -> ModifyTemplateVersionTagResponseHttpRequest: ...
            def label(
                self,
                *,
                name: str,
                body: ModifyTemplateVersionLabelRequest = ...,
                **kwargs: typing.Any
            ) -> ModifyTemplateVersionLabelResponseHttpRequest: ...
            def commit(
                self,
                *,
                name: str,
                body: CommitTemplateVersionRequest = ...,
                **kwargs: typing.Any
            ) -> TemplateVersionHttpRequest: ...
            def templateVersions(self) -> TemplateVersionsResource: ...
        class LocationsResource(googleapiclient.discovery.Resource):
            class SqlResource(googleapiclient.discovery.Resource):
                def validate(
                    self,
                    *,
                    projectId: str,
                    location: str,
                    query: str = ...,
                    **kwargs: typing.Any
                ) -> ValidateResponseHttpRequest: ...
            class SnapshotsResource(googleapiclient.discovery.Resource):
                def list(
                    self,
                    *,
                    projectId: str,
                    location: str,
                    jobId: str = ...,
                    **kwargs: typing.Any
                ) -> ListSnapshotsResponseHttpRequest: ...
                def delete(
                    self,
                    *,
                    projectId: str,
                    location: str,
                    snapshotId: str,
                    **kwargs: typing.Any
                ) -> DeleteSnapshotResponseHttpRequest: ...
                def get(
                    self,
                    *,
                    projectId: str,
                    location: str,
                    snapshotId: str,
                    **kwargs: typing.Any
                ) -> SnapshotHttpRequest: ...
            class JobsResource(googleapiclient.discovery.Resource):
                class SnapshotsResource(googleapiclient.discovery.Resource):
                    def list(
                        self,
                        *,
                        projectId: str,
                        location: str,
                        jobId: str,
                        **kwargs: typing.Any
                    ) -> ListSnapshotsResponseHttpRequest: ...
                class StagesResource(googleapiclient.discovery.Resource):
                    def getExecutionDetails(
                        self,
                        *,
                        projectId: str,
                        location: str,
                        jobId: str,
                        stageId: str,
                        startTime: str = ...,
                        pageToken: str = ...,
                        endTime: str = ...,
                        pageSize: int = ...,
                        **kwargs: typing.Any
                    ) -> StageExecutionDetailsHttpRequest: ...
                class DebugResource(googleapiclient.discovery.Resource):
                    def getConfig(
                        self,
                        *,
                        projectId: str,
                        location: str,
                        jobId: str,
                        body: GetDebugConfigRequest = ...,
                        **kwargs: typing.Any
                    ) -> GetDebugConfigResponseHttpRequest: ...
                    def sendCapture(
                        self,
                        *,
                        projectId: str,
                        location: str,
                        jobId: str,
                        body: SendDebugCaptureRequest = ...,
                        **kwargs: typing.Any
                    ) -> SendDebugCaptureResponseHttpRequest: ...
                class MessagesResource(googleapiclient.discovery.Resource):
                    def list(
                        self,
                        *,
                        projectId: str,
                        location: str,
                        jobId: str,
                        pageToken: str = ...,
                        pageSize: int = ...,
                        minimumImportance: typing_extensions.Literal[
                            "JOB_MESSAGE_IMPORTANCE_UNKNOWN",
                            "JOB_MESSAGE_DEBUG",
                            "JOB_MESSAGE_DETAILED",
                            "JOB_MESSAGE_BASIC",
                            "JOB_MESSAGE_WARNING",
                            "JOB_MESSAGE_ERROR",
                        ] = ...,
                        endTime: str = ...,
                        startTime: str = ...,
                        **kwargs: typing.Any
                    ) -> ListJobMessagesResponseHttpRequest: ...
                class WorkItemsResource(googleapiclient.discovery.Resource):
                    def lease(
                        self,
                        *,
                        projectId: str,
                        location: str,
                        jobId: str,
                        body: LeaseWorkItemRequest = ...,
                        **kwargs: typing.Any
                    ) -> LeaseWorkItemResponseHttpRequest: ...
                    def reportStatus(
                        self,
                        *,
                        projectId: str,
                        location: str,
                        jobId: str,
                        body: ReportWorkItemStatusRequest = ...,
                        **kwargs: typing.Any
                    ) -> ReportWorkItemStatusResponseHttpRequest: ...
                def get(
                    self,
                    *,
                    projectId: str,
                    location: str,
                    jobId: str,
                    view: typing_extensions.Literal[
                        "JOB_VIEW_UNKNOWN",
                        "JOB_VIEW_SUMMARY",
                        "JOB_VIEW_ALL",
                        "JOB_VIEW_DESCRIPTION",
                    ] = ...,
                    **kwargs: typing.Any
                ) -> JobHttpRequest: ...
                def snapshot(
                    self,
                    *,
                    projectId: str,
                    location: str,
                    jobId: str,
                    body: SnapshotJobRequest = ...,
                    **kwargs: typing.Any
                ) -> SnapshotHttpRequest: ...
                def create(
                    self,
                    *,
                    projectId: str,
                    location: str,
                    body: Job = ...,
                    replaceJobId: str = ...,
                    view: typing_extensions.Literal[
                        "JOB_VIEW_UNKNOWN",
                        "JOB_VIEW_SUMMARY",
                        "JOB_VIEW_ALL",
                        "JOB_VIEW_DESCRIPTION",
                    ] = ...,
                    **kwargs: typing.Any
                ) -> JobHttpRequest: ...
                def update(
                    self,
                    *,
                    projectId: str,
                    location: str,
                    jobId: str,
                    body: Job = ...,
                    **kwargs: typing.Any
                ) -> JobHttpRequest: ...
                def getMetrics(
                    self,
                    *,
                    projectId: str,
                    location: str,
                    jobId: str,
                    startTime: str = ...,
                    **kwargs: typing.Any
                ) -> JobMetricsHttpRequest: ...
                def getExecutionDetails(
                    self,
                    *,
                    projectId: str,
                    location: str,
                    jobId: str,
                    pageToken: str = ...,
                    pageSize: int = ...,
                    **kwargs: typing.Any
                ) -> JobExecutionDetailsHttpRequest: ...
                def list(
                    self,
                    *,
                    projectId: str,
                    location: str,
                    filter: typing_extensions.Literal[
                        "UNKNOWN", "ALL", "TERMINATED", "ACTIVE"
                    ] = ...,
                    pageToken: str = ...,
                    pageSize: int = ...,
                    view: typing_extensions.Literal[
                        "JOB_VIEW_UNKNOWN",
                        "JOB_VIEW_SUMMARY",
                        "JOB_VIEW_ALL",
                        "JOB_VIEW_DESCRIPTION",
                    ] = ...,
                    **kwargs: typing.Any
                ) -> ListJobsResponseHttpRequest: ...
                def snapshots(self) -> SnapshotsResource: ...
                def stages(self) -> StagesResource: ...
                def debug(self) -> DebugResource: ...
                def messages(self) -> MessagesResource: ...
                def workItems(self) -> WorkItemsResource: ...
            class TemplatesResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    projectId: str,
                    location: str,
                    body: CreateJobFromTemplateRequest = ...,
                    **kwargs: typing.Any
                ) -> JobHttpRequest: ...
                def get(
                    self,
                    *,
                    projectId: str,
                    location: str,
                    gcsPath: str = ...,
                    view: typing_extensions.Literal["METADATA_ONLY"] = ...,
                    **kwargs: typing.Any
                ) -> GetTemplateResponseHttpRequest: ...
                def launch(
                    self,
                    *,
                    projectId: str,
                    location: str,
                    body: LaunchTemplateParameters = ...,
                    dynamicTemplate_stagingLocation: str = ...,
                    gcsPath: str = ...,
                    dynamicTemplate_gcsPath: str = ...,
                    validateOnly: bool = ...,
                    **kwargs: typing.Any
                ) -> LaunchTemplateResponseHttpRequest: ...
            class FlexTemplatesResource(googleapiclient.discovery.Resource):
                def launch(
                    self,
                    *,
                    projectId: str,
                    location: str,
                    body: LaunchFlexTemplateRequest = ...,
                    **kwargs: typing.Any
                ) -> LaunchFlexTemplateResponseHttpRequest: ...
            def workerMessages(
                self,
                *,
                projectId: str,
                location: str,
                body: SendWorkerMessagesRequest = ...,
                **kwargs: typing.Any
            ) -> SendWorkerMessagesResponseHttpRequest: ...
            def sql(self) -> SqlResource: ...
            def snapshots(self) -> SnapshotsResource: ...
            def jobs(self) -> JobsResource: ...
            def templates(self) -> TemplatesResource: ...
            def flexTemplates(self) -> FlexTemplatesResource: ...
        class TemplateVersionsResource(googleapiclient.discovery.Resource):
            def list(
                self,
                *,
                parent: str,
                pageToken: str = ...,
                pageSize: int = ...,
                **kwargs: typing.Any
            ) -> ListTemplateVersionsResponseHttpRequest: ...
        class JobsResource(googleapiclient.discovery.Resource):
            class MessagesResource(googleapiclient.discovery.Resource):
                def list(
                    self,
                    *,
                    projectId: str,
                    jobId: str,
                    location: str = ...,
                    pageSize: int = ...,
                    startTime: str = ...,
                    pageToken: str = ...,
                    endTime: str = ...,
                    minimumImportance: typing_extensions.Literal[
                        "JOB_MESSAGE_IMPORTANCE_UNKNOWN",
                        "JOB_MESSAGE_DEBUG",
                        "JOB_MESSAGE_DETAILED",
                        "JOB_MESSAGE_BASIC",
                        "JOB_MESSAGE_WARNING",
                        "JOB_MESSAGE_ERROR",
                    ] = ...,
                    **kwargs: typing.Any
                ) -> ListJobMessagesResponseHttpRequest: ...
            class WorkItemsResource(googleapiclient.discovery.Resource):
                def lease(
                    self,
                    *,
                    projectId: str,
                    jobId: str,
                    body: LeaseWorkItemRequest = ...,
                    **kwargs: typing.Any
                ) -> LeaseWorkItemResponseHttpRequest: ...
                def reportStatus(
                    self,
                    *,
                    projectId: str,
                    jobId: str,
                    body: ReportWorkItemStatusRequest = ...,
                    **kwargs: typing.Any
                ) -> ReportWorkItemStatusResponseHttpRequest: ...
            class DebugResource(googleapiclient.discovery.Resource):
                def getConfig(
                    self,
                    *,
                    projectId: str,
                    jobId: str,
                    body: GetDebugConfigRequest = ...,
                    **kwargs: typing.Any
                ) -> GetDebugConfigResponseHttpRequest: ...
                def sendCapture(
                    self,
                    *,
                    projectId: str,
                    jobId: str,
                    body: SendDebugCaptureRequest = ...,
                    **kwargs: typing.Any
                ) -> SendDebugCaptureResponseHttpRequest: ...
            def snapshot(
                self,
                *,
                projectId: str,
                jobId: str,
                body: SnapshotJobRequest = ...,
                **kwargs: typing.Any
            ) -> SnapshotHttpRequest: ...
            def list(
                self,
                *,
                projectId: str,
                location: str = ...,
                pageToken: str = ...,
                filter: typing_extensions.Literal[
                    "UNKNOWN", "ALL", "TERMINATED", "ACTIVE"
                ] = ...,
                pageSize: int = ...,
                view: typing_extensions.Literal[
                    "JOB_VIEW_UNKNOWN",
                    "JOB_VIEW_SUMMARY",
                    "JOB_VIEW_ALL",
                    "JOB_VIEW_DESCRIPTION",
                ] = ...,
                **kwargs: typing.Any
            ) -> ListJobsResponseHttpRequest: ...
            def create(
                self,
                *,
                projectId: str,
                body: Job = ...,
                location: str = ...,
                replaceJobId: str = ...,
                view: typing_extensions.Literal[
                    "JOB_VIEW_UNKNOWN",
                    "JOB_VIEW_SUMMARY",
                    "JOB_VIEW_ALL",
                    "JOB_VIEW_DESCRIPTION",
                ] = ...,
                **kwargs: typing.Any
            ) -> JobHttpRequest: ...
            def getMetrics(
                self,
                *,
                projectId: str,
                jobId: str,
                startTime: str = ...,
                location: str = ...,
                **kwargs: typing.Any
            ) -> JobMetricsHttpRequest: ...
            def update(
                self,
                *,
                projectId: str,
                jobId: str,
                body: Job = ...,
                location: str = ...,
                **kwargs: typing.Any
            ) -> JobHttpRequest: ...
            def aggregated(
                self,
                *,
                projectId: str,
                view: typing_extensions.Literal[
                    "JOB_VIEW_UNKNOWN",
                    "JOB_VIEW_SUMMARY",
                    "JOB_VIEW_ALL",
                    "JOB_VIEW_DESCRIPTION",
                ] = ...,
                pageToken: str = ...,
                pageSize: int = ...,
                location: str = ...,
                filter: typing_extensions.Literal[
                    "UNKNOWN", "ALL", "TERMINATED", "ACTIVE"
                ] = ...,
                **kwargs: typing.Any
            ) -> ListJobsResponseHttpRequest: ...
            def get(
                self,
                *,
                projectId: str,
                jobId: str,
                location: str = ...,
                view: typing_extensions.Literal[
                    "JOB_VIEW_UNKNOWN",
                    "JOB_VIEW_SUMMARY",
                    "JOB_VIEW_ALL",
                    "JOB_VIEW_DESCRIPTION",
                ] = ...,
                **kwargs: typing.Any
            ) -> JobHttpRequest: ...
            def messages(self) -> MessagesResource: ...
            def workItems(self) -> WorkItemsResource: ...
            def debug(self) -> DebugResource: ...
        class SnapshotsResource(googleapiclient.discovery.Resource):
            def get(
                self,
                *,
                projectId: str,
                snapshotId: str,
                location: str = ...,
                **kwargs: typing.Any
            ) -> SnapshotHttpRequest: ...
            def list(
                self,
                *,
                projectId: str,
                jobId: str = ...,
                location: str = ...,
                **kwargs: typing.Any
            ) -> ListSnapshotsResponseHttpRequest: ...
        def workerMessages(
            self,
            *,
            projectId: str,
            body: SendWorkerMessagesRequest = ...,
            **kwargs: typing.Any
        ) -> SendWorkerMessagesResponseHttpRequest: ...
        def deleteSnapshots(
            self,
            *,
            projectId: str,
            snapshotId: str = ...,
            location: str = ...,
            **kwargs: typing.Any
        ) -> DeleteSnapshotResponseHttpRequest: ...
        def templates(self) -> TemplatesResource: ...
        def catalogTemplates(self) -> CatalogTemplatesResource: ...
        def locations(self) -> LocationsResource: ...
        def templateVersions(self) -> TemplateVersionsResource: ...
        def jobs(self) -> JobsResource: ...
        def snapshots(self) -> SnapshotsResource: ...
    def projects(self) -> ProjectsResource: ...

class JobHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Job: ...

class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Empty: ...

class ReportWorkItemStatusResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ReportWorkItemStatusResponse: ...

class SendWorkerMessagesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> SendWorkerMessagesResponse: ...

class ListJobMessagesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListJobMessagesResponse: ...

class ValidateResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ValidateResponse: ...

class GetDebugConfigResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GetDebugConfigResponse: ...

class LaunchTemplateResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> LaunchTemplateResponse: ...

class JobMetricsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> JobMetrics: ...

class TemplateVersionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> TemplateVersion: ...

class DeleteSnapshotResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> DeleteSnapshotResponse: ...

class ListTemplateVersionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListTemplateVersionsResponse: ...

class LaunchFlexTemplateResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> LaunchFlexTemplateResponse: ...

class ModifyTemplateVersionLabelResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ModifyTemplateVersionLabelResponse: ...

class ListSnapshotsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListSnapshotsResponse: ...

class JobExecutionDetailsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> JobExecutionDetails: ...

class GetTemplateResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GetTemplateResponse: ...

class StageExecutionDetailsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> StageExecutionDetails: ...

class LeaseWorkItemResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> LeaseWorkItemResponse: ...

class SnapshotHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Snapshot: ...

class ListJobsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListJobsResponse: ...

class SendDebugCaptureResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> SendDebugCaptureResponse: ...

class ModifyTemplateVersionTagResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ModifyTemplateVersionTagResponse: ...
