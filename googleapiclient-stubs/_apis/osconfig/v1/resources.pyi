import collections.abc
import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

_list = list

@typing.type_check_only
class OSConfigResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class ProjectsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class LocationsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class InstancesResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class InventoriesResource(googleapiclient.discovery.Resource):
                    def get(
                        self,
                        *,
                        name: str,
                        view: typing_extensions.Literal[
                            "INVENTORY_VIEW_UNSPECIFIED", "BASIC", "FULL"
                        ] = ...,
                        **kwargs: typing.Any
                    ) -> InventoryHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        view: typing_extensions.Literal[
                            "INVENTORY_VIEW_UNSPECIFIED", "BASIC", "FULL"
                        ] = ...,
                        **kwargs: typing.Any
                    ) -> ListInventoriesResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: ListInventoriesResponseHttpRequest,
                        previous_response: ListInventoriesResponse,
                    ) -> ListInventoriesResponseHttpRequest | None: ...

                @typing.type_check_only
                class OsPolicyAssignmentsResource(googleapiclient.discovery.Resource):
                    @typing.type_check_only
                    class ReportsResource(googleapiclient.discovery.Resource):
                        def get(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> OSPolicyAssignmentReportHttpRequest: ...
                        def list(
                            self,
                            *,
                            parent: str,
                            filter: str = ...,
                            pageSize: int = ...,
                            pageToken: str = ...,
                            **kwargs: typing.Any
                        ) -> ListOSPolicyAssignmentReportsResponseHttpRequest: ...
                        def list_next(
                            self,
                            previous_request: ListOSPolicyAssignmentReportsResponseHttpRequest,
                            previous_response: ListOSPolicyAssignmentReportsResponse,
                        ) -> (
                            ListOSPolicyAssignmentReportsResponseHttpRequest | None
                        ): ...

                    def reports(self) -> ReportsResource: ...

                @typing.type_check_only
                class VulnerabilityReportsResource(googleapiclient.discovery.Resource):
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> VulnerabilityReportHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any
                    ) -> ListVulnerabilityReportsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: ListVulnerabilityReportsResponseHttpRequest,
                        previous_response: ListVulnerabilityReportsResponse,
                    ) -> ListVulnerabilityReportsResponseHttpRequest | None: ...

                def inventories(self) -> InventoriesResource: ...
                def osPolicyAssignments(self) -> OsPolicyAssignmentsResource: ...
                def vulnerabilityReports(self) -> VulnerabilityReportsResource: ...

            @typing.type_check_only
            class OsPolicyAssignmentsResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class OperationsResource(googleapiclient.discovery.Resource):
                    def cancel(
                        self,
                        *,
                        name: str,
                        body: CancelOperationRequest = ...,
                        **kwargs: typing.Any
                    ) -> EmptyHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> OperationHttpRequest: ...

                def create(
                    self,
                    *,
                    parent: str,
                    body: OSPolicyAssignment = ...,
                    osPolicyAssignmentId: str = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> OSPolicyAssignmentHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> ListOSPolicyAssignmentsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListOSPolicyAssignmentsResponseHttpRequest,
                    previous_response: ListOSPolicyAssignmentsResponse,
                ) -> ListOSPolicyAssignmentsResponseHttpRequest | None: ...
                def listRevisions(
                    self,
                    *,
                    name: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> ListOSPolicyAssignmentRevisionsResponseHttpRequest: ...
                def listRevisions_next(
                    self,
                    previous_request: ListOSPolicyAssignmentRevisionsResponseHttpRequest,
                    previous_response: ListOSPolicyAssignmentRevisionsResponse,
                ) -> ListOSPolicyAssignmentRevisionsResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: OSPolicyAssignment = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def operations(self) -> OperationsResource: ...

            def instances(self) -> InstancesResource: ...
            def osPolicyAssignments(self) -> OsPolicyAssignmentsResource: ...

        @typing.type_check_only
        class PatchDeploymentsResource(googleapiclient.discovery.Resource):
            def create(
                self,
                *,
                parent: str,
                body: PatchDeployment = ...,
                patchDeploymentId: str = ...,
                **kwargs: typing.Any
            ) -> PatchDeploymentHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> PatchDeploymentHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> ListPatchDeploymentsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListPatchDeploymentsResponseHttpRequest,
                previous_response: ListPatchDeploymentsResponse,
            ) -> ListPatchDeploymentsResponseHttpRequest | None: ...
            def patch(
                self,
                *,
                name: str,
                body: PatchDeployment = ...,
                updateMask: str = ...,
                **kwargs: typing.Any
            ) -> PatchDeploymentHttpRequest: ...
            def pause(
                self,
                *,
                name: str,
                body: PausePatchDeploymentRequest = ...,
                **kwargs: typing.Any
            ) -> PatchDeploymentHttpRequest: ...
            def resume(
                self,
                *,
                name: str,
                body: ResumePatchDeploymentRequest = ...,
                **kwargs: typing.Any
            ) -> PatchDeploymentHttpRequest: ...

        @typing.type_check_only
        class PatchJobsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class InstanceDetailsResource(googleapiclient.discovery.Resource):
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> ListPatchJobInstanceDetailsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListPatchJobInstanceDetailsResponseHttpRequest,
                    previous_response: ListPatchJobInstanceDetailsResponse,
                ) -> ListPatchJobInstanceDetailsResponseHttpRequest | None: ...

            def cancel(
                self,
                *,
                name: str,
                body: CancelPatchJobRequest = ...,
                **kwargs: typing.Any
            ) -> PatchJobHttpRequest: ...
            def execute(
                self,
                *,
                parent: str,
                body: ExecutePatchJobRequest = ...,
                **kwargs: typing.Any
            ) -> PatchJobHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> PatchJobHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                filter: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> ListPatchJobsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListPatchJobsResponseHttpRequest,
                previous_response: ListPatchJobsResponse,
            ) -> ListPatchJobsResponseHttpRequest | None: ...
            def instanceDetails(self) -> InstanceDetailsResource: ...

        def locations(self) -> LocationsResource: ...
        def patchDeployments(self) -> PatchDeploymentsResource: ...
        def patchJobs(self) -> PatchJobsResource: ...

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
class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Empty: ...

@typing.type_check_only
class InventoryHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Inventory: ...

@typing.type_check_only
class ListInventoriesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListInventoriesResponse: ...

@typing.type_check_only
class ListOSPolicyAssignmentReportsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListOSPolicyAssignmentReportsResponse: ...

@typing.type_check_only
class ListOSPolicyAssignmentRevisionsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListOSPolicyAssignmentRevisionsResponse: ...

@typing.type_check_only
class ListOSPolicyAssignmentsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListOSPolicyAssignmentsResponse: ...

@typing.type_check_only
class ListPatchDeploymentsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListPatchDeploymentsResponse: ...

@typing.type_check_only
class ListPatchJobInstanceDetailsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListPatchJobInstanceDetailsResponse: ...

@typing.type_check_only
class ListPatchJobsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListPatchJobsResponse: ...

@typing.type_check_only
class ListVulnerabilityReportsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListVulnerabilityReportsResponse: ...

@typing.type_check_only
class OSPolicyAssignmentHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> OSPolicyAssignment: ...

@typing.type_check_only
class OSPolicyAssignmentReportHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> OSPolicyAssignmentReport: ...

@typing.type_check_only
class OperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Operation: ...

@typing.type_check_only
class PatchDeploymentHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> PatchDeployment: ...

@typing.type_check_only
class PatchJobHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> PatchJob: ...

@typing.type_check_only
class VulnerabilityReportHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> VulnerabilityReport: ...
