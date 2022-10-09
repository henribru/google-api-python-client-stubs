import collections.abc
import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

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
                    **kwargs: typing.Any
                ) -> GoogleLongrunningListOperationsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleLongrunningListOperationsResponseHttpRequest,
                    previous_response: GoogleLongrunningListOperationsResponse,
                ) -> GoogleLongrunningListOperationsResponseHttpRequest | None: ...

            @typing.type_check_only
            class WorkloadsResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class ViolationsResource(googleapiclient.discovery.Resource):
                    def acknowledge(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudAssuredworkloadsV1AcknowledgeViolationRequest = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudAssuredworkloadsV1AcknowledgeViolationResponseHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleCloudAssuredworkloadsV1ViolationHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str = ...,
                        interval_endTime: str = ...,
                        interval_startTime: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudAssuredworkloadsV1ListViolationsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudAssuredworkloadsV1ListViolationsResponseHttpRequest,
                        previous_response: GoogleCloudAssuredworkloadsV1ListViolationsResponse,
                    ) -> GoogleCloudAssuredworkloadsV1ListViolationsResponseHttpRequest | None: ...

                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudAssuredworkloadsV1Workload = ...,
                    externalId: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def delete(
                    self, *, name: str, etag: str = ..., **kwargs: typing.Any
                ) -> GoogleProtobufEmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudAssuredworkloadsV1WorkloadHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudAssuredworkloadsV1ListWorkloadsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudAssuredworkloadsV1ListWorkloadsResponseHttpRequest,
                    previous_response: GoogleCloudAssuredworkloadsV1ListWorkloadsResponse,
                ) -> GoogleCloudAssuredworkloadsV1ListWorkloadsResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudAssuredworkloadsV1Workload = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudAssuredworkloadsV1WorkloadHttpRequest: ...
                def restrictAllowedResources(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudAssuredworkloadsV1RestrictAllowedResourcesRequest = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudAssuredworkloadsV1RestrictAllowedResourcesResponseHttpRequest: ...
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
        | None = ...,
    ) -> googleapiclient.http.BatchHttpRequest: ...
    def organizations(self) -> OrganizationsResource: ...

@typing.type_check_only
class GoogleCloudAssuredworkloadsV1AcknowledgeViolationResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudAssuredworkloadsV1AcknowledgeViolationResponse: ...

@typing.type_check_only
class GoogleCloudAssuredworkloadsV1ListViolationsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudAssuredworkloadsV1ListViolationsResponse: ...

@typing.type_check_only
class GoogleCloudAssuredworkloadsV1ListWorkloadsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudAssuredworkloadsV1ListWorkloadsResponse: ...

@typing.type_check_only
class GoogleCloudAssuredworkloadsV1RestrictAllowedResourcesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudAssuredworkloadsV1RestrictAllowedResourcesResponse: ...

@typing.type_check_only
class GoogleCloudAssuredworkloadsV1ViolationHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudAssuredworkloadsV1Violation: ...

@typing.type_check_only
class GoogleCloudAssuredworkloadsV1WorkloadHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudAssuredworkloadsV1Workload: ...

@typing.type_check_only
class GoogleLongrunningListOperationsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleLongrunningListOperationsResponse: ...

@typing.type_check_only
class GoogleLongrunningOperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleLongrunningOperation: ...

@typing.type_check_only
class GoogleProtobufEmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleProtobufEmpty: ...
