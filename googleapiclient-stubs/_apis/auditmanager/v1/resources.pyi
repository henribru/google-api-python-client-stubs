import collections.abc
import typing

import httplib2

import googleapiclient.discovery
import googleapiclient.http

from .schemas import *

_list = list

@typing.type_check_only
class CloudAuditManagerResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class FoldersResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class LocationsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class AuditReportsResource(googleapiclient.discovery.Resource):
                def generate(
                    self,
                    *,
                    scope: str,
                    body: GenerateAuditReportRequest,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> AuditReportHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int | None = ...,
                    pageToken: str | None = ...,
                    **kwargs: typing.Any,
                ) -> ListAuditReportsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListAuditReportsResponseHttpRequest,
                    previous_response: ListAuditReportsResponse,
                ) -> ListAuditReportsResponseHttpRequest | None: ...

            @typing.type_check_only
            class AuditScopeReportsResource(googleapiclient.discovery.Resource):
                def generate(
                    self,
                    *,
                    scope: str,
                    body: GenerateAuditScopeReportRequest,
                    **kwargs: typing.Any,
                ) -> AuditScopeReportHttpRequest: ...

            @typing.type_check_only
            class OperationDetailsResource(googleapiclient.discovery.Resource):
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> OperationHttpRequest: ...

            @typing.type_check_only
            class OperationIdsResource(googleapiclient.discovery.Resource):
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> OperationHttpRequest: ...

            @typing.type_check_only
            class ResourceEnrollmentStatusesResource(
                googleapiclient.discovery.Resource
            ):
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> ResourceEnrollmentStatusHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int | None = ...,
                    pageToken: str | None = ...,
                    **kwargs: typing.Any,
                ) -> ListResourceEnrollmentStatusesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListResourceEnrollmentStatusesResponseHttpRequest,
                    previous_response: ListResourceEnrollmentStatusesResponse,
                ) -> ListResourceEnrollmentStatusesResponseHttpRequest | None: ...

            @typing.type_check_only
            class StandardsResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class ControlsResource(googleapiclient.discovery.Resource):
                    def list(
                        self,
                        *,
                        parent: str,
                        pageSize: int | None = ...,
                        pageToken: str | None = ...,
                        **kwargs: typing.Any,
                    ) -> ListControlsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: ListControlsResponseHttpRequest,
                        previous_response: ListControlsResponse,
                    ) -> ListControlsResponseHttpRequest | None: ...

                def controls(self) -> ControlsResource: ...

            def enrollResource(
                self, *, scope: str, body: EnrollResourceRequest, **kwargs: typing.Any
            ) -> EnrollmentHttpRequest: ...
            def auditReports(self) -> AuditReportsResource: ...
            def auditScopeReports(self) -> AuditScopeReportsResource: ...
            def operationDetails(self) -> OperationDetailsResource: ...
            def operationIds(self) -> OperationIdsResource: ...
            def resourceEnrollmentStatuses(
                self,
            ) -> ResourceEnrollmentStatusesResource: ...
            def standards(self) -> StandardsResource: ...

        def locations(self) -> LocationsResource: ...

    @typing.type_check_only
    class OrganizationsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class LocationsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class AuditReportsResource(googleapiclient.discovery.Resource):
                def generate(
                    self,
                    *,
                    scope: str,
                    body: GenerateAuditReportRequest,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> AuditReportHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int | None = ...,
                    pageToken: str | None = ...,
                    **kwargs: typing.Any,
                ) -> ListAuditReportsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListAuditReportsResponseHttpRequest,
                    previous_response: ListAuditReportsResponse,
                ) -> ListAuditReportsResponseHttpRequest | None: ...

            @typing.type_check_only
            class AuditScopeReportsResource(googleapiclient.discovery.Resource):
                def generate(
                    self,
                    *,
                    scope: str,
                    body: GenerateAuditScopeReportRequest,
                    **kwargs: typing.Any,
                ) -> AuditScopeReportHttpRequest: ...

            @typing.type_check_only
            class OperationDetailsResource(googleapiclient.discovery.Resource):
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> OperationHttpRequest: ...

            @typing.type_check_only
            class OperationIdsResource(googleapiclient.discovery.Resource):
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> OperationHttpRequest: ...

            @typing.type_check_only
            class OperationsResource(googleapiclient.discovery.Resource):
                def cancel(
                    self,
                    *,
                    name: str,
                    body: CancelOperationRequest,
                    **kwargs: typing.Any,
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
                    filter: str | None = ...,
                    pageSize: int | None = ...,
                    pageToken: str | None = ...,
                    returnPartialSuccess: bool | None = ...,
                    **kwargs: typing.Any,
                ) -> ListOperationsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListOperationsResponseHttpRequest,
                    previous_response: ListOperationsResponse,
                ) -> ListOperationsResponseHttpRequest | None: ...

            @typing.type_check_only
            class ResourceEnrollmentStatusesResource(
                googleapiclient.discovery.Resource
            ):
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> ResourceEnrollmentStatusHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int | None = ...,
                    pageToken: str | None = ...,
                    **kwargs: typing.Any,
                ) -> ListResourceEnrollmentStatusesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListResourceEnrollmentStatusesResponseHttpRequest,
                    previous_response: ListResourceEnrollmentStatusesResponse,
                ) -> ListResourceEnrollmentStatusesResponseHttpRequest | None: ...

            @typing.type_check_only
            class StandardsResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class ControlsResource(googleapiclient.discovery.Resource):
                    def list(
                        self,
                        *,
                        parent: str,
                        pageSize: int | None = ...,
                        pageToken: str | None = ...,
                        **kwargs: typing.Any,
                    ) -> ListControlsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: ListControlsResponseHttpRequest,
                        previous_response: ListControlsResponse,
                    ) -> ListControlsResponseHttpRequest | None: ...

                def controls(self) -> ControlsResource: ...

            def enrollResource(
                self, *, scope: str, body: EnrollResourceRequest, **kwargs: typing.Any
            ) -> EnrollmentHttpRequest: ...
            def auditReports(self) -> AuditReportsResource: ...
            def auditScopeReports(self) -> AuditScopeReportsResource: ...
            def operationDetails(self) -> OperationDetailsResource: ...
            def operationIds(self) -> OperationIdsResource: ...
            def operations(self) -> OperationsResource: ...
            def resourceEnrollmentStatuses(
                self,
            ) -> ResourceEnrollmentStatusesResource: ...
            def standards(self) -> StandardsResource: ...

        def locations(self) -> LocationsResource: ...

    @typing.type_check_only
    class ProjectsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class LocationsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class AuditReportsResource(googleapiclient.discovery.Resource):
                def generate(
                    self,
                    *,
                    scope: str,
                    body: GenerateAuditReportRequest,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> AuditReportHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int | None = ...,
                    pageToken: str | None = ...,
                    **kwargs: typing.Any,
                ) -> ListAuditReportsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListAuditReportsResponseHttpRequest,
                    previous_response: ListAuditReportsResponse,
                ) -> ListAuditReportsResponseHttpRequest | None: ...

            @typing.type_check_only
            class AuditScopeReportsResource(googleapiclient.discovery.Resource):
                def generate(
                    self,
                    *,
                    scope: str,
                    body: GenerateAuditScopeReportRequest,
                    **kwargs: typing.Any,
                ) -> AuditScopeReportHttpRequest: ...

            @typing.type_check_only
            class OperationDetailsResource(googleapiclient.discovery.Resource):
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> OperationHttpRequest: ...

            @typing.type_check_only
            class OperationIdsResource(googleapiclient.discovery.Resource):
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> OperationHttpRequest: ...

            @typing.type_check_only
            class OperationsResource(googleapiclient.discovery.Resource):
                def cancel(
                    self,
                    *,
                    name: str,
                    body: CancelOperationRequest,
                    **kwargs: typing.Any,
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
                    filter: str | None = ...,
                    pageSize: int | None = ...,
                    pageToken: str | None = ...,
                    returnPartialSuccess: bool | None = ...,
                    **kwargs: typing.Any,
                ) -> ListOperationsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListOperationsResponseHttpRequest,
                    previous_response: ListOperationsResponse,
                ) -> ListOperationsResponseHttpRequest | None: ...

            @typing.type_check_only
            class ResourceEnrollmentStatusesResource(
                googleapiclient.discovery.Resource
            ):
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> ResourceEnrollmentStatusHttpRequest: ...

            @typing.type_check_only
            class StandardsResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class ControlsResource(googleapiclient.discovery.Resource):
                    def list(
                        self,
                        *,
                        parent: str,
                        pageSize: int | None = ...,
                        pageToken: str | None = ...,
                        **kwargs: typing.Any,
                    ) -> ListControlsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: ListControlsResponseHttpRequest,
                        previous_response: ListControlsResponse,
                    ) -> ListControlsResponseHttpRequest | None: ...

                def controls(self) -> ControlsResource: ...

            def enrollResource(
                self, *, scope: str, body: EnrollResourceRequest, **kwargs: typing.Any
            ) -> EnrollmentHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> LocationHttpRequest: ...
            def list(
                self,
                *,
                name: str,
                extraLocationTypes: str | _list[str] | None = ...,
                filter: str | None = ...,
                pageSize: int | None = ...,
                pageToken: str | None = ...,
                **kwargs: typing.Any,
            ) -> ListLocationsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListLocationsResponseHttpRequest,
                previous_response: ListLocationsResponse,
            ) -> ListLocationsResponseHttpRequest | None: ...
            def auditReports(self) -> AuditReportsResource: ...
            def auditScopeReports(self) -> AuditScopeReportsResource: ...
            def operationDetails(self) -> OperationDetailsResource: ...
            def operationIds(self) -> OperationIdsResource: ...
            def operations(self) -> OperationsResource: ...
            def resourceEnrollmentStatuses(
                self,
            ) -> ResourceEnrollmentStatusesResource: ...
            def standards(self) -> StandardsResource: ...

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
    def folders(self) -> FoldersResource: ...
    def organizations(self) -> OrganizationsResource: ...
    def projects(self) -> ProjectsResource: ...

@typing.type_check_only
class AuditReportHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> AuditReport: ...

@typing.type_check_only
class AuditScopeReportHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> AuditScopeReport: ...

@typing.type_check_only
class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Empty: ...

@typing.type_check_only
class EnrollmentHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Enrollment: ...

@typing.type_check_only
class ListAuditReportsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListAuditReportsResponse: ...

@typing.type_check_only
class ListControlsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListControlsResponse: ...

@typing.type_check_only
class ListLocationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListLocationsResponse: ...

@typing.type_check_only
class ListOperationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListOperationsResponse: ...

@typing.type_check_only
class ListResourceEnrollmentStatusesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListResourceEnrollmentStatusesResponse: ...

@typing.type_check_only
class LocationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Location: ...

@typing.type_check_only
class OperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Operation: ...

@typing.type_check_only
class ResourceEnrollmentStatusHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ResourceEnrollmentStatus: ...
