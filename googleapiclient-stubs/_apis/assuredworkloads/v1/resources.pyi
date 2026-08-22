import collections.abc
import typing

import httplib2

import googleapiclient.discovery
import googleapiclient.http

from .schemas import *

_list = list

@typing.type_check_only
class AssuredworkloadsResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class AssuredworkloadsResource(googleapiclient.discovery.Resource):
        def archiveResourceEvents(
            self,
            *,
            body: GoogleCloudAssuredworkloadsV1ArchiveResourceEventsRequest,
            **kwargs: typing.Any,
        ) -> GoogleCloudAssuredworkloadsV1ArchiveResourceEventsResponseHttpRequest: ...
        def revertArchivedResourceEvents(
            self,
            *,
            body: GoogleCloudAssuredworkloadsV1RevertArchivedResourceEventsRequest,
            **kwargs: typing.Any,
        ) -> (
            GoogleCloudAssuredworkloadsV1RevertArchivedResourceEventsResponseHttpRequest
        ): ...

    @typing.type_check_only
    class FoldersResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class LocationsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class DbFindingSummariesResource(googleapiclient.discovery.Resource):
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str | None = ...,
                    pageSize: int | None = ...,
                    pageToken: str | None = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudAssuredworkloadsV1ListDbFindingSummariesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudAssuredworkloadsV1ListDbFindingSummariesResponseHttpRequest,
                    previous_response: GoogleCloudAssuredworkloadsV1ListDbFindingSummariesResponse,
                ) -> (
                    GoogleCloudAssuredworkloadsV1ListDbFindingSummariesResponseHttpRequest
                    | None
                ): ...

            @typing.type_check_only
            class DbFrameworkComplianceReportsResource(
                googleapiclient.discovery.Resource
            ):
                @typing.type_check_only
                class DbControlComplianceSummariesResource(
                    googleapiclient.discovery.Resource
                ):
                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str | None = ...,
                        pageSize: int | None = ...,
                        pageToken: str | None = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudAssuredworkloadsV1ListDbControlComplianceSummariesResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudAssuredworkloadsV1ListDbControlComplianceSummariesResponseHttpRequest,
                        previous_response: GoogleCloudAssuredworkloadsV1ListDbControlComplianceSummariesResponse,
                    ) -> (
                        GoogleCloudAssuredworkloadsV1ListDbControlComplianceSummariesResponseHttpRequest
                        | None
                    ): ...

                def aggregate(
                    self,
                    *,
                    name: str,
                    filter: str | None = ...,
                    interval_endTime: str | None = ...,
                    interval_startTime: str | None = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudAssuredworkloadsV1AggregateDbFrameworkComplianceReportResponseHttpRequest: ...
                def fetch(
                    self,
                    *,
                    name: str,
                    endTime: str | None = ...,
                    filter: str | None = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudAssuredworkloadsV1FetchDbFrameworkComplianceReportResponseHttpRequest: ...
                def dbControlComplianceSummaries(
                    self,
                ) -> DbControlComplianceSummariesResource: ...

            @typing.type_check_only
            class DbFrameworkComplianceSummariesResource(
                googleapiclient.discovery.Resource
            ):
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str | None = ...,
                    pageSize: int | None = ...,
                    pageToken: str | None = ...,
                    view: typing.Literal[
                        "FRAMEWORK_COMPLIANCE_SUMMARY_VIEW_UNSPECIFIED",
                        "FRAMEWORK_COMPLIANCE_SUMMARY_VIEW_BASIC",
                        "FRAMEWORK_COMPLIANCE_SUMMARY_VIEW_FULL",
                    ]
                    | None = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudAssuredworkloadsV1ListDbFrameworkComplianceSummariesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudAssuredworkloadsV1ListDbFrameworkComplianceSummariesResponseHttpRequest,
                    previous_response: GoogleCloudAssuredworkloadsV1ListDbFrameworkComplianceSummariesResponse,
                ) -> (
                    GoogleCloudAssuredworkloadsV1ListDbFrameworkComplianceSummariesResponseHttpRequest
                    | None
                ): ...

            def dbFindingSummaries(self) -> DbFindingSummariesResource: ...
            def dbFrameworkComplianceReports(
                self,
            ) -> DbFrameworkComplianceReportsResource: ...
            def dbFrameworkComplianceSummaries(
                self,
            ) -> DbFrameworkComplianceSummariesResource: ...

        def locations(self) -> LocationsResource: ...

    @typing.type_check_only
    class OrganizationsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class LocationsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class DbFindingSummariesResource(googleapiclient.discovery.Resource):
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str | None = ...,
                    pageSize: int | None = ...,
                    pageToken: str | None = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudAssuredworkloadsV1ListDbFindingSummariesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudAssuredworkloadsV1ListDbFindingSummariesResponseHttpRequest,
                    previous_response: GoogleCloudAssuredworkloadsV1ListDbFindingSummariesResponse,
                ) -> (
                    GoogleCloudAssuredworkloadsV1ListDbFindingSummariesResponseHttpRequest
                    | None
                ): ...

            @typing.type_check_only
            class DbFrameworkComplianceReportsResource(
                googleapiclient.discovery.Resource
            ):
                @typing.type_check_only
                class DbControlComplianceSummariesResource(
                    googleapiclient.discovery.Resource
                ):
                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str | None = ...,
                        pageSize: int | None = ...,
                        pageToken: str | None = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudAssuredworkloadsV1ListDbControlComplianceSummariesResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudAssuredworkloadsV1ListDbControlComplianceSummariesResponseHttpRequest,
                        previous_response: GoogleCloudAssuredworkloadsV1ListDbControlComplianceSummariesResponse,
                    ) -> (
                        GoogleCloudAssuredworkloadsV1ListDbControlComplianceSummariesResponseHttpRequest
                        | None
                    ): ...

                def aggregate(
                    self,
                    *,
                    name: str,
                    filter: str | None = ...,
                    interval_endTime: str | None = ...,
                    interval_startTime: str | None = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudAssuredworkloadsV1AggregateDbFrameworkComplianceReportResponseHttpRequest: ...
                def fetch(
                    self,
                    *,
                    name: str,
                    endTime: str | None = ...,
                    filter: str | None = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudAssuredworkloadsV1FetchDbFrameworkComplianceReportResponseHttpRequest: ...
                def dbControlComplianceSummaries(
                    self,
                ) -> DbControlComplianceSummariesResource: ...

            @typing.type_check_only
            class DbFrameworkComplianceSummariesResource(
                googleapiclient.discovery.Resource
            ):
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str | None = ...,
                    pageSize: int | None = ...,
                    pageToken: str | None = ...,
                    view: typing.Literal[
                        "FRAMEWORK_COMPLIANCE_SUMMARY_VIEW_UNSPECIFIED",
                        "FRAMEWORK_COMPLIANCE_SUMMARY_VIEW_BASIC",
                        "FRAMEWORK_COMPLIANCE_SUMMARY_VIEW_FULL",
                    ]
                    | None = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudAssuredworkloadsV1ListDbFrameworkComplianceSummariesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudAssuredworkloadsV1ListDbFrameworkComplianceSummariesResponseHttpRequest,
                    previous_response: GoogleCloudAssuredworkloadsV1ListDbFrameworkComplianceSummariesResponse,
                ) -> (
                    GoogleCloudAssuredworkloadsV1ListDbFrameworkComplianceSummariesResponseHttpRequest
                    | None
                ): ...

            @typing.type_check_only
            class OperationsResource(googleapiclient.discovery.Resource):
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
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

            @typing.type_check_only
            class WorkloadsResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class UpdatesResource(googleapiclient.discovery.Resource):
                    def apply(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudAssuredworkloadsV1ApplyWorkloadUpdateRequest,
                        **kwargs: typing.Any,
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        pageSize: int | None = ...,
                        pageToken: str | None = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudAssuredworkloadsV1ListWorkloadUpdatesResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudAssuredworkloadsV1ListWorkloadUpdatesResponseHttpRequest,
                        previous_response: GoogleCloudAssuredworkloadsV1ListWorkloadUpdatesResponse,
                    ) -> (
                        GoogleCloudAssuredworkloadsV1ListWorkloadUpdatesResponseHttpRequest
                        | None
                    ): ...

                @typing.type_check_only
                class ViolationsResource(googleapiclient.discovery.Resource):
                    def acknowledge(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudAssuredworkloadsV1AcknowledgeViolationRequest,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudAssuredworkloadsV1AcknowledgeViolationResponseHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleCloudAssuredworkloadsV1ViolationHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str | None = ...,
                        interval_endTime: str | None = ...,
                        interval_startTime: str | None = ...,
                        orderBy: str | None = ...,
                        pageSize: int | None = ...,
                        pageToken: str | None = ...,
                        **kwargs: typing.Any,
                    ) -> (
                        GoogleCloudAssuredworkloadsV1ListViolationsResponseHttpRequest
                    ): ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudAssuredworkloadsV1ListViolationsResponseHttpRequest,
                        previous_response: GoogleCloudAssuredworkloadsV1ListViolationsResponse,
                    ) -> (
                        GoogleCloudAssuredworkloadsV1ListViolationsResponseHttpRequest
                        | None
                    ): ...

                def analyzeWorkloadMove(
                    self,
                    *,
                    target: str,
                    assetTypes: str | _list[str] | None = ...,
                    pageSize: int | None = ...,
                    pageToken: str | None = ...,
                    project: str | None = ...,
                    **kwargs: typing.Any,
                ) -> (
                    GoogleCloudAssuredworkloadsV1AnalyzeWorkloadMoveResponseHttpRequest
                ): ...
                def analyzeWorkloadMove_next(
                    self,
                    previous_request: GoogleCloudAssuredworkloadsV1AnalyzeWorkloadMoveResponseHttpRequest,
                    previous_response: GoogleCloudAssuredworkloadsV1AnalyzeWorkloadMoveResponse,
                ) -> (
                    GoogleCloudAssuredworkloadsV1AnalyzeWorkloadMoveResponseHttpRequest
                    | None
                ): ...
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudAssuredworkloadsV1Workload,
                    externalId: str | None = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def delete(
                    self, *, name: str, etag: str | None = ..., **kwargs: typing.Any
                ) -> GoogleProtobufEmptyHttpRequest: ...
                def enableComplianceUpdates(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudAssuredworkloadsV1EnableComplianceUpdatesResponseHttpRequest: ...
                def enableResourceMonitoring(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudAssuredworkloadsV1EnableResourceMonitoringResponseHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudAssuredworkloadsV1WorkloadHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str | None = ...,
                    pageSize: int | None = ...,
                    pageToken: str | None = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudAssuredworkloadsV1ListWorkloadsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudAssuredworkloadsV1ListWorkloadsResponseHttpRequest,
                    previous_response: GoogleCloudAssuredworkloadsV1ListWorkloadsResponse,
                ) -> (
                    GoogleCloudAssuredworkloadsV1ListWorkloadsResponseHttpRequest | None
                ): ...
                def mutatePartnerPermissions(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudAssuredworkloadsV1MutatePartnerPermissionsRequest,
                    **kwargs: typing.Any,
                ) -> GoogleCloudAssuredworkloadsV1WorkloadHttpRequest: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudAssuredworkloadsV1Workload,
                    updateMask: str | None = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudAssuredworkloadsV1WorkloadHttpRequest: ...
                def restrictAllowedResources(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudAssuredworkloadsV1RestrictAllowedResourcesRequest,
                    **kwargs: typing.Any,
                ) -> GoogleCloudAssuredworkloadsV1RestrictAllowedResourcesResponseHttpRequest: ...
                def updates(self) -> UpdatesResource: ...
                def violations(self) -> ViolationsResource: ...

            def dbFindingSummaries(self) -> DbFindingSummariesResource: ...
            def dbFrameworkComplianceReports(
                self,
            ) -> DbFrameworkComplianceReportsResource: ...
            def dbFrameworkComplianceSummaries(
                self,
            ) -> DbFrameworkComplianceSummariesResource: ...
            def operations(self) -> OperationsResource: ...
            def workloads(self) -> WorkloadsResource: ...

        def locations(self) -> LocationsResource: ...

    @typing.type_check_only
    class ProjectsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class LocationsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class DbFindingSummariesResource(googleapiclient.discovery.Resource):
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str | None = ...,
                    pageSize: int | None = ...,
                    pageToken: str | None = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudAssuredworkloadsV1ListDbFindingSummariesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudAssuredworkloadsV1ListDbFindingSummariesResponseHttpRequest,
                    previous_response: GoogleCloudAssuredworkloadsV1ListDbFindingSummariesResponse,
                ) -> (
                    GoogleCloudAssuredworkloadsV1ListDbFindingSummariesResponseHttpRequest
                    | None
                ): ...

            @typing.type_check_only
            class DbFrameworkComplianceReportsResource(
                googleapiclient.discovery.Resource
            ):
                @typing.type_check_only
                class DbControlComplianceSummariesResource(
                    googleapiclient.discovery.Resource
                ):
                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str | None = ...,
                        pageSize: int | None = ...,
                        pageToken: str | None = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudAssuredworkloadsV1ListDbControlComplianceSummariesResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudAssuredworkloadsV1ListDbControlComplianceSummariesResponseHttpRequest,
                        previous_response: GoogleCloudAssuredworkloadsV1ListDbControlComplianceSummariesResponse,
                    ) -> (
                        GoogleCloudAssuredworkloadsV1ListDbControlComplianceSummariesResponseHttpRequest
                        | None
                    ): ...

                def aggregate(
                    self,
                    *,
                    name: str,
                    filter: str | None = ...,
                    interval_endTime: str | None = ...,
                    interval_startTime: str | None = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudAssuredworkloadsV1AggregateDbFrameworkComplianceReportResponseHttpRequest: ...
                def fetch(
                    self,
                    *,
                    name: str,
                    endTime: str | None = ...,
                    filter: str | None = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudAssuredworkloadsV1FetchDbFrameworkComplianceReportResponseHttpRequest: ...
                def dbControlComplianceSummaries(
                    self,
                ) -> DbControlComplianceSummariesResource: ...

            @typing.type_check_only
            class DbFrameworkComplianceSummariesResource(
                googleapiclient.discovery.Resource
            ):
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str | None = ...,
                    pageSize: int | None = ...,
                    pageToken: str | None = ...,
                    view: typing.Literal[
                        "FRAMEWORK_COMPLIANCE_SUMMARY_VIEW_UNSPECIFIED",
                        "FRAMEWORK_COMPLIANCE_SUMMARY_VIEW_BASIC",
                        "FRAMEWORK_COMPLIANCE_SUMMARY_VIEW_FULL",
                    ]
                    | None = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudAssuredworkloadsV1ListDbFrameworkComplianceSummariesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudAssuredworkloadsV1ListDbFrameworkComplianceSummariesResponseHttpRequest,
                    previous_response: GoogleCloudAssuredworkloadsV1ListDbFrameworkComplianceSummariesResponse,
                ) -> (
                    GoogleCloudAssuredworkloadsV1ListDbFrameworkComplianceSummariesResponseHttpRequest
                    | None
                ): ...

            def dbFindingSummaries(self) -> DbFindingSummariesResource: ...
            def dbFrameworkComplianceReports(
                self,
            ) -> DbFrameworkComplianceReportsResource: ...
            def dbFrameworkComplianceSummaries(
                self,
            ) -> DbFrameworkComplianceSummariesResource: ...

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
        | None = None,
    ) -> googleapiclient.http.BatchHttpRequest: ...
    def assuredworkloads(self) -> AssuredworkloadsResource: ...
    def folders(self) -> FoldersResource: ...
    def organizations(self) -> OrganizationsResource: ...
    def projects(self) -> ProjectsResource: ...

@typing.type_check_only
class GoogleCloudAssuredworkloadsV1AcknowledgeViolationResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAssuredworkloadsV1AcknowledgeViolationResponse: ...

@typing.type_check_only
class GoogleCloudAssuredworkloadsV1AggregateDbFrameworkComplianceReportResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAssuredworkloadsV1AggregateDbFrameworkComplianceReportResponse: ...

@typing.type_check_only
class GoogleCloudAssuredworkloadsV1AnalyzeWorkloadMoveResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAssuredworkloadsV1AnalyzeWorkloadMoveResponse: ...

@typing.type_check_only
class GoogleCloudAssuredworkloadsV1ArchiveResourceEventsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAssuredworkloadsV1ArchiveResourceEventsResponse: ...

@typing.type_check_only
class GoogleCloudAssuredworkloadsV1EnableComplianceUpdatesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAssuredworkloadsV1EnableComplianceUpdatesResponse: ...

@typing.type_check_only
class GoogleCloudAssuredworkloadsV1EnableResourceMonitoringResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAssuredworkloadsV1EnableResourceMonitoringResponse: ...

@typing.type_check_only
class GoogleCloudAssuredworkloadsV1FetchDbFrameworkComplianceReportResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAssuredworkloadsV1FetchDbFrameworkComplianceReportResponse: ...

@typing.type_check_only
class GoogleCloudAssuredworkloadsV1ListDbControlComplianceSummariesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAssuredworkloadsV1ListDbControlComplianceSummariesResponse: ...

@typing.type_check_only
class GoogleCloudAssuredworkloadsV1ListDbFindingSummariesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAssuredworkloadsV1ListDbFindingSummariesResponse: ...

@typing.type_check_only
class GoogleCloudAssuredworkloadsV1ListDbFrameworkComplianceSummariesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAssuredworkloadsV1ListDbFrameworkComplianceSummariesResponse: ...

@typing.type_check_only
class GoogleCloudAssuredworkloadsV1ListViolationsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAssuredworkloadsV1ListViolationsResponse: ...

@typing.type_check_only
class GoogleCloudAssuredworkloadsV1ListWorkloadUpdatesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAssuredworkloadsV1ListWorkloadUpdatesResponse: ...

@typing.type_check_only
class GoogleCloudAssuredworkloadsV1ListWorkloadsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAssuredworkloadsV1ListWorkloadsResponse: ...

@typing.type_check_only
class GoogleCloudAssuredworkloadsV1RestrictAllowedResourcesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAssuredworkloadsV1RestrictAllowedResourcesResponse: ...

@typing.type_check_only
class GoogleCloudAssuredworkloadsV1RevertArchivedResourceEventsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAssuredworkloadsV1RevertArchivedResourceEventsResponse: ...

@typing.type_check_only
class GoogleCloudAssuredworkloadsV1ViolationHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAssuredworkloadsV1Violation: ...

@typing.type_check_only
class GoogleCloudAssuredworkloadsV1WorkloadHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAssuredworkloadsV1Workload: ...

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
