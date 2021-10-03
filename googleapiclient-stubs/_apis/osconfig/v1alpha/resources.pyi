import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

@typing.type_check_only
class OSConfigResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class ProjectsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class LocationsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class InstanceOSPoliciesCompliancesResource(
                googleapiclient.discovery.Resource
            ):
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> InstanceOSPoliciesComplianceHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> ListInstanceOSPoliciesCompliancesResponseHttpRequest: ...
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
                @typing.type_check_only
                class OsPolicyAssignmentsResource(googleapiclient.discovery.Resource):
                    @typing.type_check_only
                    class ReportsResource(googleapiclient.discovery.Resource):
                        def list(
                            self,
                            *,
                            parent: str,
                            filter: str = ...,
                            pageSize: int = ...,
                            pageToken: str = ...,
                            **kwargs: typing.Any
                        ) -> ListOSPolicyAssignmentReportsResponseHttpRequest: ...
                    def getReport(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> OSPolicyAssignmentReportHttpRequest: ...
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
                def listRevisions(
                    self,
                    *,
                    name: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> ListOSPolicyAssignmentRevisionsResponseHttpRequest: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: OSPolicyAssignment = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def operations(self) -> OperationsResource: ...
            def instanceOSPoliciesCompliances(
                self,
            ) -> InstanceOSPoliciesCompliancesResource: ...
            def instances(self) -> InstancesResource: ...
            def osPolicyAssignments(self) -> OsPolicyAssignmentsResource: ...
        def locations(self) -> LocationsResource: ...
    def projects(self) -> ProjectsResource: ...

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
class InstanceOSPoliciesComplianceHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> InstanceOSPoliciesCompliance: ...

@typing.type_check_only
class InventoryHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> Inventory: ...

@typing.type_check_only
class ListInstanceOSPoliciesCompliancesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> ListInstanceOSPoliciesCompliancesResponse: ...

@typing.type_check_only
class ListInventoriesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> ListInventoriesResponse: ...

@typing.type_check_only
class ListOSPolicyAssignmentReportsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> ListOSPolicyAssignmentReportsResponse: ...

@typing.type_check_only
class ListOSPolicyAssignmentRevisionsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> ListOSPolicyAssignmentRevisionsResponse: ...

@typing.type_check_only
class ListOSPolicyAssignmentsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> ListOSPolicyAssignmentsResponse: ...

@typing.type_check_only
class ListVulnerabilityReportsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> ListVulnerabilityReportsResponse: ...

@typing.type_check_only
class OSPolicyAssignmentHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> OSPolicyAssignment: ...

@typing.type_check_only
class OSPolicyAssignmentReportHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> OSPolicyAssignmentReport: ...

@typing.type_check_only
class OperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> Operation: ...

@typing.type_check_only
class VulnerabilityReportHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> VulnerabilityReport: ...
