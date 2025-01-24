import collections.abc
import typing

import httplib2
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http

from .schemas import *

_list = list

@typing.type_check_only
class AssuredworkloadsResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class OrganizationsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class LocationsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class OperationsResource(googleapiclient.discovery.Resource):
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def list(
                    self,
                    *,
                    name: str,
                    filter: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
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
                        body: GoogleCloudAssuredworkloadsV1beta1ApplyWorkloadUpdateRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudAssuredworkloadsV1beta1ListWorkloadUpdatesResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudAssuredworkloadsV1beta1ListWorkloadUpdatesResponseHttpRequest,
                        previous_response: GoogleCloudAssuredworkloadsV1beta1ListWorkloadUpdatesResponse,
                    ) -> (
                        GoogleCloudAssuredworkloadsV1beta1ListWorkloadUpdatesResponseHttpRequest
                        | None
                    ): ...

                @typing.type_check_only
                class ViolationsResource(googleapiclient.discovery.Resource):
                    def acknowledge(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudAssuredworkloadsV1beta1AcknowledgeViolationRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudAssuredworkloadsV1beta1AcknowledgeViolationResponseHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleCloudAssuredworkloadsV1beta1ViolationHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str = ...,
                        interval_endTime: str = ...,
                        interval_startTime: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudAssuredworkloadsV1beta1ListViolationsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudAssuredworkloadsV1beta1ListViolationsResponseHttpRequest,
                        previous_response: GoogleCloudAssuredworkloadsV1beta1ListViolationsResponse,
                    ) -> (
                        GoogleCloudAssuredworkloadsV1beta1ListViolationsResponseHttpRequest
                        | None
                    ): ...

                def analyzeWorkloadMove(
                    self,
                    *,
                    target: str,
                    assetTypes: str | _list[str] = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    project: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudAssuredworkloadsV1beta1AnalyzeWorkloadMoveResponseHttpRequest: ...
                def analyzeWorkloadMove_next(
                    self,
                    previous_request: GoogleCloudAssuredworkloadsV1beta1AnalyzeWorkloadMoveResponseHttpRequest,
                    previous_response: GoogleCloudAssuredworkloadsV1beta1AnalyzeWorkloadMoveResponse,
                ) -> (
                    GoogleCloudAssuredworkloadsV1beta1AnalyzeWorkloadMoveResponseHttpRequest
                    | None
                ): ...
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudAssuredworkloadsV1beta1Workload = ...,
                    externalId: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def delete(
                    self, *, name: str, etag: str = ..., **kwargs: typing.Any
                ) -> GoogleProtobufEmptyHttpRequest: ...
                def enableComplianceUpdates(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudAssuredworkloadsV1beta1EnableComplianceUpdatesResponseHttpRequest: ...
                def enableResourceMonitoring(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudAssuredworkloadsV1beta1EnableResourceMonitoringResponseHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudAssuredworkloadsV1beta1WorkloadHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> (
                    GoogleCloudAssuredworkloadsV1beta1ListWorkloadsResponseHttpRequest
                ): ...
                def list_next(
                    self,
                    previous_request: GoogleCloudAssuredworkloadsV1beta1ListWorkloadsResponseHttpRequest,
                    previous_response: GoogleCloudAssuredworkloadsV1beta1ListWorkloadsResponse,
                ) -> (
                    GoogleCloudAssuredworkloadsV1beta1ListWorkloadsResponseHttpRequest
                    | None
                ): ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudAssuredworkloadsV1beta1Workload = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudAssuredworkloadsV1beta1WorkloadHttpRequest: ...
                def restrictAllowedResources(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudAssuredworkloadsV1beta1RestrictAllowedResourcesRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudAssuredworkloadsV1beta1RestrictAllowedResourcesResponseHttpRequest: ...
                def updates(self) -> UpdatesResource: ...
                def violations(self) -> ViolationsResource: ...

            def operations(self) -> OperationsResource: ...
            def workloads(self) -> WorkloadsResource: ...

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
    def organizations(self) -> OrganizationsResource: ...

@typing.type_check_only
class GoogleCloudAssuredworkloadsV1beta1AcknowledgeViolationResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAssuredworkloadsV1beta1AcknowledgeViolationResponse: ...

@typing.type_check_only
class GoogleCloudAssuredworkloadsV1beta1AnalyzeWorkloadMoveResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAssuredworkloadsV1beta1AnalyzeWorkloadMoveResponse: ...

@typing.type_check_only
class GoogleCloudAssuredworkloadsV1beta1EnableComplianceUpdatesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAssuredworkloadsV1beta1EnableComplianceUpdatesResponse: ...

@typing.type_check_only
class GoogleCloudAssuredworkloadsV1beta1EnableResourceMonitoringResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAssuredworkloadsV1beta1EnableResourceMonitoringResponse: ...

@typing.type_check_only
class GoogleCloudAssuredworkloadsV1beta1ListViolationsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAssuredworkloadsV1beta1ListViolationsResponse: ...

@typing.type_check_only
class GoogleCloudAssuredworkloadsV1beta1ListWorkloadUpdatesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAssuredworkloadsV1beta1ListWorkloadUpdatesResponse: ...

@typing.type_check_only
class GoogleCloudAssuredworkloadsV1beta1ListWorkloadsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAssuredworkloadsV1beta1ListWorkloadsResponse: ...

@typing.type_check_only
class GoogleCloudAssuredworkloadsV1beta1RestrictAllowedResourcesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAssuredworkloadsV1beta1RestrictAllowedResourcesResponse: ...

@typing.type_check_only
class GoogleCloudAssuredworkloadsV1beta1ViolationHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAssuredworkloadsV1beta1Violation: ...

@typing.type_check_only
class GoogleCloudAssuredworkloadsV1beta1WorkloadHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAssuredworkloadsV1beta1Workload: ...

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
