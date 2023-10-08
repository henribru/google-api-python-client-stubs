import collections.abc
import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

_list = list

@typing.type_check_only
class MigrationCenterAPIResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class ProjectsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class LocationsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class AssetsResource(googleapiclient.discovery.Resource):
                def aggregateValues(
                    self,
                    *,
                    parent: str,
                    body: AggregateAssetsValuesRequest = ...,
                    **kwargs: typing.Any
                ) -> AggregateAssetsValuesResponseHttpRequest: ...
                def batchDelete(
                    self,
                    *,
                    parent: str,
                    body: BatchDeleteAssetsRequest = ...,
                    **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def batchUpdate(
                    self,
                    *,
                    parent: str,
                    body: BatchUpdateAssetsRequest = ...,
                    **kwargs: typing.Any
                ) -> BatchUpdateAssetsResponseHttpRequest: ...
                def delete(
                    self, *, name: str, requestId: str = ..., **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def get(
                    self,
                    *,
                    name: str,
                    view: typing_extensions.Literal[
                        "ASSET_VIEW_UNSPECIFIED", "ASSET_VIEW_BASIC", "ASSET_VIEW_FULL"
                    ] = ...,
                    **kwargs: typing.Any
                ) -> AssetHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    view: typing_extensions.Literal[
                        "ASSET_VIEW_UNSPECIFIED", "ASSET_VIEW_BASIC", "ASSET_VIEW_FULL"
                    ] = ...,
                    **kwargs: typing.Any
                ) -> ListAssetsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListAssetsResponseHttpRequest,
                    previous_response: ListAssetsResponse,
                ) -> ListAssetsResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: Asset = ...,
                    requestId: str = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any
                ) -> AssetHttpRequest: ...
                def reportAssetFrames(
                    self,
                    *,
                    parent: str,
                    body: Frames = ...,
                    source: str = ...,
                    **kwargs: typing.Any
                ) -> ReportAssetFramesResponseHttpRequest: ...

            @typing.type_check_only
            class GroupsResource(googleapiclient.discovery.Resource):
                def addAssets(
                    self,
                    *,
                    group: str,
                    body: AddAssetsToGroupRequest = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def create(
                    self,
                    *,
                    parent: str,
                    body: Group = ...,
                    groupId: str = ...,
                    requestId: str = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def delete(
                    self, *, name: str, requestId: str = ..., **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GroupHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> ListGroupsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListGroupsResponseHttpRequest,
                    previous_response: ListGroupsResponse,
                ) -> ListGroupsResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: Group = ...,
                    requestId: str = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def removeAssets(
                    self,
                    *,
                    group: str,
                    body: RemoveAssetsFromGroupRequest = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...

            @typing.type_check_only
            class ImportJobsResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class ImportDataFilesResource(googleapiclient.discovery.Resource):
                    def create(
                        self,
                        *,
                        parent: str,
                        body: ImportDataFile = ...,
                        importDataFileId: str = ...,
                        requestId: str = ...,
                        **kwargs: typing.Any
                    ) -> OperationHttpRequest: ...
                    def delete(
                        self, *, name: str, requestId: str = ..., **kwargs: typing.Any
                    ) -> OperationHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> ImportDataFileHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str = ...,
                        orderBy: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any
                    ) -> ListImportDataFilesResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: ListImportDataFilesResponseHttpRequest,
                        previous_response: ListImportDataFilesResponse,
                    ) -> ListImportDataFilesResponseHttpRequest | None: ...

                def create(
                    self,
                    *,
                    parent: str,
                    body: ImportJob = ...,
                    importJobId: str = ...,
                    requestId: str = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def delete(
                    self,
                    *,
                    name: str,
                    force: bool = ...,
                    requestId: str = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def get(
                    self,
                    *,
                    name: str,
                    view: typing_extensions.Literal[
                        "IMPORT_JOB_VIEW_UNSPECIFIED",
                        "IMPORT_JOB_VIEW_BASIC",
                        "IMPORT_JOB_VIEW_FULL",
                    ] = ...,
                    **kwargs: typing.Any
                ) -> ImportJobHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    view: typing_extensions.Literal[
                        "IMPORT_JOB_VIEW_UNSPECIFIED",
                        "IMPORT_JOB_VIEW_BASIC",
                        "IMPORT_JOB_VIEW_FULL",
                    ] = ...,
                    **kwargs: typing.Any
                ) -> ListImportJobsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListImportJobsResponseHttpRequest,
                    previous_response: ListImportJobsResponse,
                ) -> ListImportJobsResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: ImportJob = ...,
                    requestId: str = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def run(
                    self,
                    *,
                    name: str,
                    body: RunImportJobRequest = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def validate(
                    self,
                    *,
                    name: str,
                    body: ValidateImportJobRequest = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def importDataFiles(self) -> ImportDataFilesResource: ...

            @typing.type_check_only
            class OperationsResource(googleapiclient.discovery.Resource):
                def cancel(
                    self,
                    *,
                    name: str,
                    body: CancelOperationRequest = ...,
                    **kwargs: typing.Any
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
                    **kwargs: typing.Any
                ) -> ListOperationsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListOperationsResponseHttpRequest,
                    previous_response: ListOperationsResponse,
                ) -> ListOperationsResponseHttpRequest | None: ...

            @typing.type_check_only
            class PreferenceSetsResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: PreferenceSet = ...,
                    preferenceSetId: str = ...,
                    requestId: str = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def delete(
                    self, *, name: str, requestId: str = ..., **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> PreferenceSetHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> ListPreferenceSetsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListPreferenceSetsResponseHttpRequest,
                    previous_response: ListPreferenceSetsResponse,
                ) -> ListPreferenceSetsResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: PreferenceSet = ...,
                    requestId: str = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...

            @typing.type_check_only
            class ReportConfigsResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class ReportsResource(googleapiclient.discovery.Resource):
                    def create(
                        self,
                        *,
                        parent: str,
                        body: Report = ...,
                        reportId: str = ...,
                        requestId: str = ...,
                        **kwargs: typing.Any
                    ) -> OperationHttpRequest: ...
                    def delete(
                        self, *, name: str, requestId: str = ..., **kwargs: typing.Any
                    ) -> OperationHttpRequest: ...
                    def get(
                        self,
                        *,
                        name: str,
                        view: typing_extensions.Literal[
                            "REPORT_VIEW_UNSPECIFIED",
                            "REPORT_VIEW_BASIC",
                            "REPORT_VIEW_FULL",
                            "REPORT_VIEW_STANDARD",
                        ] = ...,
                        **kwargs: typing.Any
                    ) -> ReportHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str = ...,
                        orderBy: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        view: typing_extensions.Literal[
                            "REPORT_VIEW_UNSPECIFIED",
                            "REPORT_VIEW_BASIC",
                            "REPORT_VIEW_FULL",
                            "REPORT_VIEW_STANDARD",
                        ] = ...,
                        **kwargs: typing.Any
                    ) -> ListReportsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: ListReportsResponseHttpRequest,
                        previous_response: ListReportsResponse,
                    ) -> ListReportsResponseHttpRequest | None: ...

                def create(
                    self,
                    *,
                    parent: str,
                    body: ReportConfig = ...,
                    reportConfigId: str = ...,
                    requestId: str = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def delete(
                    self,
                    *,
                    name: str,
                    force: bool = ...,
                    requestId: str = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> ReportConfigHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> ListReportConfigsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListReportConfigsResponseHttpRequest,
                    previous_response: ListReportConfigsResponse,
                ) -> ListReportConfigsResponseHttpRequest | None: ...
                def reports(self) -> ReportsResource: ...

            @typing.type_check_only
            class SourcesResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class ErrorFramesResource(googleapiclient.discovery.Resource):
                    def get(
                        self,
                        *,
                        name: str,
                        view: typing_extensions.Literal[
                            "ERROR_FRAME_VIEW_UNSPECIFIED",
                            "ERROR_FRAME_VIEW_BASIC",
                            "ERROR_FRAME_VIEW_FULL",
                        ] = ...,
                        **kwargs: typing.Any
                    ) -> ErrorFrameHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        view: typing_extensions.Literal[
                            "ERROR_FRAME_VIEW_UNSPECIFIED",
                            "ERROR_FRAME_VIEW_BASIC",
                            "ERROR_FRAME_VIEW_FULL",
                        ] = ...,
                        **kwargs: typing.Any
                    ) -> ListErrorFramesResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: ListErrorFramesResponseHttpRequest,
                        previous_response: ListErrorFramesResponse,
                    ) -> ListErrorFramesResponseHttpRequest | None: ...

                def create(
                    self,
                    *,
                    parent: str,
                    body: Source = ...,
                    requestId: str = ...,
                    sourceId: str = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def delete(
                    self, *, name: str, requestId: str = ..., **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> SourceHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
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
                    requestId: str = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def errorFrames(self) -> ErrorFramesResource: ...

            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> LocationHttpRequest: ...
            def getSettings(
                self, *, name: str, **kwargs: typing.Any
            ) -> SettingsHttpRequest: ...
            def list(
                self,
                *,
                name: str,
                filter: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> ListLocationsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListLocationsResponseHttpRequest,
                previous_response: ListLocationsResponse,
            ) -> ListLocationsResponseHttpRequest | None: ...
            def updateSettings(
                self,
                *,
                name: str,
                body: Settings = ...,
                requestId: str = ...,
                updateMask: str = ...,
                **kwargs: typing.Any
            ) -> OperationHttpRequest: ...
            def assets(self) -> AssetsResource: ...
            def groups(self) -> GroupsResource: ...
            def importJobs(self) -> ImportJobsResource: ...
            def operations(self) -> OperationsResource: ...
            def preferenceSets(self) -> PreferenceSetsResource: ...
            def reportConfigs(self) -> ReportConfigsResource: ...
            def sources(self) -> SourcesResource: ...

        def locations(self) -> LocationsResource: ...

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
    def projects(self) -> ProjectsResource: ...

@typing.type_check_only
class AggregateAssetsValuesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> AggregateAssetsValuesResponse: ...

@typing.type_check_only
class AssetHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Asset: ...

@typing.type_check_only
class BatchUpdateAssetsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> BatchUpdateAssetsResponse: ...

@typing.type_check_only
class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Empty: ...

@typing.type_check_only
class ErrorFrameHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ErrorFrame: ...

@typing.type_check_only
class GroupHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Group: ...

@typing.type_check_only
class ImportDataFileHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ImportDataFile: ...

@typing.type_check_only
class ImportJobHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ImportJob: ...

@typing.type_check_only
class ListAssetsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListAssetsResponse: ...

@typing.type_check_only
class ListErrorFramesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListErrorFramesResponse: ...

@typing.type_check_only
class ListGroupsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListGroupsResponse: ...

@typing.type_check_only
class ListImportDataFilesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListImportDataFilesResponse: ...

@typing.type_check_only
class ListImportJobsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListImportJobsResponse: ...

@typing.type_check_only
class ListLocationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListLocationsResponse: ...

@typing.type_check_only
class ListOperationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListOperationsResponse: ...

@typing.type_check_only
class ListPreferenceSetsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListPreferenceSetsResponse: ...

@typing.type_check_only
class ListReportConfigsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListReportConfigsResponse: ...

@typing.type_check_only
class ListReportsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListReportsResponse: ...

@typing.type_check_only
class ListSourcesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListSourcesResponse: ...

@typing.type_check_only
class LocationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Location: ...

@typing.type_check_only
class OperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Operation: ...

@typing.type_check_only
class PreferenceSetHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> PreferenceSet: ...

@typing.type_check_only
class ReportHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Report: ...

@typing.type_check_only
class ReportAssetFramesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ReportAssetFramesResponse: ...

@typing.type_check_only
class ReportConfigHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ReportConfig: ...

@typing.type_check_only
class SettingsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Settings: ...

@typing.type_check_only
class SourceHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Source: ...
