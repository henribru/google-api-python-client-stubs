import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *
@typing.type_check_only
class DataflowResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class ProjectsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class CatalogTemplatesResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class TemplateVersionsResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: CreateTemplateVersionRequest = ...,
                    **kwargs: typing.Any
                ) -> TemplateVersionHttpRequest: ...
            def commit(
                self,
                *,
                name: str,
                body: CommitTemplateVersionRequest = ...,
                **kwargs: typing.Any
            ) -> TemplateVersionHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> TemplateVersionHttpRequest: ...
            def label(
                self,
                *,
                name: str,
                body: ModifyTemplateVersionLabelRequest = ...,
                **kwargs: typing.Any
            ) -> ModifyTemplateVersionLabelResponseHttpRequest: ...
            def tag(
                self,
                *,
                name: str,
                body: ModifyTemplateVersionTagRequest = ...,
                **kwargs: typing.Any
            ) -> ModifyTemplateVersionTagResponseHttpRequest: ...
            def templateVersions(self) -> TemplateVersionsResource: ...
        @typing.type_check_only
        class JobsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
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
            @typing.type_check_only
            class MessagesResource(googleapiclient.discovery.Resource):
                def list(
                    self,
                    *,
                    projectId: str,
                    jobId: str,
                    endTime: str = ...,
                    location: str = ...,
                    minimumImportance: typing_extensions.Literal[
                        "JOB_MESSAGE_IMPORTANCE_UNKNOWN",
                        "JOB_MESSAGE_DEBUG",
                        "JOB_MESSAGE_DETAILED",
                        "JOB_MESSAGE_BASIC",
                        "JOB_MESSAGE_WARNING",
                        "JOB_MESSAGE_ERROR",
                    ] = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    startTime: str = ...,
                    **kwargs: typing.Any
                ) -> ListJobMessagesResponseHttpRequest: ...
            @typing.type_check_only
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
            def aggregated(
                self,
                *,
                projectId: str,
                filter: typing_extensions.Literal[
                    "UNKNOWN", "ALL", "TERMINATED", "ACTIVE"
                ] = ...,
                location: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
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
            def getMetrics(
                self,
                *,
                projectId: str,
                jobId: str,
                location: str = ...,
                startTime: str = ...,
                **kwargs: typing.Any
            ) -> JobMetricsHttpRequest: ...
            def list(
                self,
                *,
                projectId: str,
                filter: typing_extensions.Literal[
                    "UNKNOWN", "ALL", "TERMINATED", "ACTIVE"
                ] = ...,
                location: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                view: typing_extensions.Literal[
                    "JOB_VIEW_UNKNOWN",
                    "JOB_VIEW_SUMMARY",
                    "JOB_VIEW_ALL",
                    "JOB_VIEW_DESCRIPTION",
                ] = ...,
                **kwargs: typing.Any
            ) -> ListJobsResponseHttpRequest: ...
            def snapshot(
                self,
                *,
                projectId: str,
                jobId: str,
                body: SnapshotJobRequest = ...,
                **kwargs: typing.Any
            ) -> SnapshotHttpRequest: ...
            def update(
                self,
                *,
                projectId: str,
                jobId: str,
                body: Job = ...,
                location: str = ...,
                **kwargs: typing.Any
            ) -> JobHttpRequest: ...
            def debug(self) -> DebugResource: ...
            def messages(self) -> MessagesResource: ...
            def workItems(self) -> WorkItemsResource: ...
        @typing.type_check_only
        class LocationsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class FlexTemplatesResource(googleapiclient.discovery.Resource):
                def launch(
                    self,
                    *,
                    projectId: str,
                    location: str,
                    body: LaunchFlexTemplateRequest = ...,
                    **kwargs: typing.Any
                ) -> LaunchFlexTemplateResponseHttpRequest: ...
            @typing.type_check_only
            class JobsResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
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
                @typing.type_check_only
                class MessagesResource(googleapiclient.discovery.Resource):
                    def list(
                        self,
                        *,
                        projectId: str,
                        location: str,
                        jobId: str,
                        endTime: str = ...,
                        minimumImportance: typing_extensions.Literal[
                            "JOB_MESSAGE_IMPORTANCE_UNKNOWN",
                            "JOB_MESSAGE_DEBUG",
                            "JOB_MESSAGE_DETAILED",
                            "JOB_MESSAGE_BASIC",
                            "JOB_MESSAGE_WARNING",
                            "JOB_MESSAGE_ERROR",
                        ] = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        startTime: str = ...,
                        **kwargs: typing.Any
                    ) -> ListJobMessagesResponseHttpRequest: ...
                @typing.type_check_only
                class SnapshotsResource(googleapiclient.discovery.Resource):
                    def list(
                        self,
                        *,
                        projectId: str,
                        location: str,
                        jobId: str,
                        **kwargs: typing.Any
                    ) -> ListSnapshotsResponseHttpRequest: ...
                @typing.type_check_only
                class StagesResource(googleapiclient.discovery.Resource):
                    def getExecutionDetails(
                        self,
                        *,
                        projectId: str,
                        location: str,
                        jobId: str,
                        stageId: str,
                        endTime: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        startTime: str = ...,
                        **kwargs: typing.Any
                    ) -> StageExecutionDetailsHttpRequest: ...
                @typing.type_check_only
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
                def getExecutionDetails(
                    self,
                    *,
                    projectId: str,
                    location: str,
                    jobId: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> JobExecutionDetailsHttpRequest: ...
                def getMetrics(
                    self,
                    *,
                    projectId: str,
                    location: str,
                    jobId: str,
                    startTime: str = ...,
                    **kwargs: typing.Any
                ) -> JobMetricsHttpRequest: ...
                def list(
                    self,
                    *,
                    projectId: str,
                    location: str,
                    filter: typing_extensions.Literal[
                        "UNKNOWN", "ALL", "TERMINATED", "ACTIVE"
                    ] = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    view: typing_extensions.Literal[
                        "JOB_VIEW_UNKNOWN",
                        "JOB_VIEW_SUMMARY",
                        "JOB_VIEW_ALL",
                        "JOB_VIEW_DESCRIPTION",
                    ] = ...,
                    **kwargs: typing.Any
                ) -> ListJobsResponseHttpRequest: ...
                def snapshot(
                    self,
                    *,
                    projectId: str,
                    location: str,
                    jobId: str,
                    body: SnapshotJobRequest = ...,
                    **kwargs: typing.Any
                ) -> SnapshotHttpRequest: ...
                def update(
                    self,
                    *,
                    projectId: str,
                    location: str,
                    jobId: str,
                    body: Job = ...,
                    **kwargs: typing.Any
                ) -> JobHttpRequest: ...
                def debug(self) -> DebugResource: ...
                def messages(self) -> MessagesResource: ...
                def snapshots(self) -> SnapshotsResource: ...
                def stages(self) -> StagesResource: ...
                def workItems(self) -> WorkItemsResource: ...
            @typing.type_check_only
            class SnapshotsResource(googleapiclient.discovery.Resource):
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
                def list(
                    self,
                    *,
                    projectId: str,
                    location: str,
                    jobId: str = ...,
                    **kwargs: typing.Any
                ) -> ListSnapshotsResponseHttpRequest: ...
            @typing.type_check_only
            class SqlResource(googleapiclient.discovery.Resource):
                def validate(
                    self,
                    *,
                    projectId: str,
                    location: str,
                    query: str = ...,
                    **kwargs: typing.Any
                ) -> ValidateResponseHttpRequest: ...
            @typing.type_check_only
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
                    dynamicTemplate_gcsPath: str = ...,
                    dynamicTemplate_stagingLocation: str = ...,
                    gcsPath: str = ...,
                    validateOnly: bool = ...,
                    **kwargs: typing.Any
                ) -> LaunchTemplateResponseHttpRequest: ...
            def workerMessages(
                self,
                *,
                projectId: str,
                location: str,
                body: SendWorkerMessagesRequest = ...,
                **kwargs: typing.Any
            ) -> SendWorkerMessagesResponseHttpRequest: ...
            def flexTemplates(self) -> FlexTemplatesResource: ...
            def jobs(self) -> JobsResource: ...
            def snapshots(self) -> SnapshotsResource: ...
            def sql(self) -> SqlResource: ...
            def templates(self) -> TemplatesResource: ...
        @typing.type_check_only
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
        @typing.type_check_only
        class TemplateVersionsResource(googleapiclient.discovery.Resource):
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> ListTemplateVersionsResponseHttpRequest: ...
        @typing.type_check_only
        class TemplatesResource(googleapiclient.discovery.Resource):
            def create(
                self,
                *,
                projectId: str,
                body: CreateJobFromTemplateRequest = ...,
                **kwargs: typing.Any
            ) -> JobHttpRequest: ...
            def get(
                self,
                *,
                projectId: str,
                gcsPath: str = ...,
                location: str = ...,
                view: typing_extensions.Literal["METADATA_ONLY"] = ...,
                **kwargs: typing.Any
            ) -> GetTemplateResponseHttpRequest: ...
            def launch(
                self,
                *,
                projectId: str,
                body: LaunchTemplateParameters = ...,
                dynamicTemplate_gcsPath: str = ...,
                dynamicTemplate_stagingLocation: str = ...,
                gcsPath: str = ...,
                location: str = ...,
                validateOnly: bool = ...,
                **kwargs: typing.Any
            ) -> LaunchTemplateResponseHttpRequest: ...
        def deleteSnapshots(
            self,
            *,
            projectId: str,
            location: str = ...,
            snapshotId: str = ...,
            **kwargs: typing.Any
        ) -> DeleteSnapshotResponseHttpRequest: ...
        def workerMessages(
            self,
            *,
            projectId: str,
            body: SendWorkerMessagesRequest = ...,
            **kwargs: typing.Any
        ) -> SendWorkerMessagesResponseHttpRequest: ...
        def catalogTemplates(self) -> CatalogTemplatesResource: ...
        def jobs(self) -> JobsResource: ...
        def locations(self) -> LocationsResource: ...
        def snapshots(self) -> SnapshotsResource: ...
        def templateVersions(self) -> TemplateVersionsResource: ...
        def templates(self) -> TemplatesResource: ...
    def projects(self) -> ProjectsResource: ...

@typing.type_check_only
class DeleteSnapshotResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> DeleteSnapshotResponse: ...

@typing.type_check_only
class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> Empty: ...

@typing.type_check_only
class GetDebugConfigResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GetDebugConfigResponse: ...

@typing.type_check_only
class GetTemplateResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GetTemplateResponse: ...

@typing.type_check_only
class JobHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> Job: ...

@typing.type_check_only
class JobExecutionDetailsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> JobExecutionDetails: ...

@typing.type_check_only
class JobMetricsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> JobMetrics: ...

@typing.type_check_only
class LaunchFlexTemplateResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> LaunchFlexTemplateResponse: ...

@typing.type_check_only
class LaunchTemplateResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> LaunchTemplateResponse: ...

@typing.type_check_only
class LeaseWorkItemResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> LeaseWorkItemResponse: ...

@typing.type_check_only
class ListJobMessagesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> ListJobMessagesResponse: ...

@typing.type_check_only
class ListJobsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> ListJobsResponse: ...

@typing.type_check_only
class ListSnapshotsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> ListSnapshotsResponse: ...

@typing.type_check_only
class ListTemplateVersionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> ListTemplateVersionsResponse: ...

@typing.type_check_only
class ModifyTemplateVersionLabelResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> ModifyTemplateVersionLabelResponse: ...

@typing.type_check_only
class ModifyTemplateVersionTagResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> ModifyTemplateVersionTagResponse: ...

@typing.type_check_only
class ReportWorkItemStatusResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> ReportWorkItemStatusResponse: ...

@typing.type_check_only
class SendDebugCaptureResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> SendDebugCaptureResponse: ...

@typing.type_check_only
class SendWorkerMessagesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> SendWorkerMessagesResponse: ...

@typing.type_check_only
class SnapshotHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> Snapshot: ...

@typing.type_check_only
class StageExecutionDetailsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> StageExecutionDetails: ...

@typing.type_check_only
class TemplateVersionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> TemplateVersion: ...

@typing.type_check_only
class ValidateResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> ValidateResponse: ...
