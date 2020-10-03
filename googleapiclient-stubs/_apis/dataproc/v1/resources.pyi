import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class DataprocResource(googleapiclient.discovery.Resource):
    class ProjectsResource(googleapiclient.discovery.Resource):
        class LocationsResource(googleapiclient.discovery.Resource):
            class WorkflowTemplatesResource(googleapiclient.discovery.Resource):
                def list(
                    self,
                    *,
                    parent: str,
                    pageToken: str = ...,
                    pageSize: int = ...,
                    **kwargs: typing.Any
                ) -> ListWorkflowTemplatesResponseHttpRequest: ...
                def update(
                    self,
                    *,
                    name: str,
                    body: WorkflowTemplate = ...,
                    **kwargs: typing.Any
                ) -> WorkflowTemplateHttpRequest: ...
                def instantiate(
                    self,
                    *,
                    name: str,
                    body: InstantiateWorkflowTemplateRequest = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def setIamPolicy(
                    self,
                    *,
                    resource: str,
                    body: SetIamPolicyRequest = ...,
                    **kwargs: typing.Any
                ) -> PolicyHttpRequest: ...
                def testIamPermissions(
                    self,
                    *,
                    resource: str,
                    body: TestIamPermissionsRequest = ...,
                    **kwargs: typing.Any
                ) -> TestIamPermissionsResponseHttpRequest: ...
                def instantiateInline(
                    self,
                    *,
                    parent: str,
                    body: WorkflowTemplate = ...,
                    requestId: str = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def get(
                    self, *, name: str, version: int = ..., **kwargs: typing.Any
                ) -> WorkflowTemplateHttpRequest: ...
                def getIamPolicy(
                    self,
                    *,
                    resource: str,
                    body: GetIamPolicyRequest = ...,
                    **kwargs: typing.Any
                ) -> PolicyHttpRequest: ...
                def create(
                    self,
                    *,
                    parent: str,
                    body: WorkflowTemplate = ...,
                    **kwargs: typing.Any
                ) -> WorkflowTemplateHttpRequest: ...
                def delete(
                    self, *, name: str, version: int = ..., **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
            class AutoscalingPoliciesResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: AutoscalingPolicy = ...,
                    **kwargs: typing.Any
                ) -> AutoscalingPolicyHttpRequest: ...
                def testIamPermissions(
                    self,
                    *,
                    resource: str,
                    body: TestIamPermissionsRequest = ...,
                    **kwargs: typing.Any
                ) -> TestIamPermissionsResponseHttpRequest: ...
                def getIamPolicy(
                    self,
                    *,
                    resource: str,
                    body: GetIamPolicyRequest = ...,
                    **kwargs: typing.Any
                ) -> PolicyHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> ListAutoscalingPoliciesResponseHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> AutoscalingPolicyHttpRequest: ...
                def setIamPolicy(
                    self,
                    *,
                    resource: str,
                    body: SetIamPolicyRequest = ...,
                    **kwargs: typing.Any
                ) -> PolicyHttpRequest: ...
                def update(
                    self,
                    *,
                    name: str,
                    body: AutoscalingPolicy = ...,
                    **kwargs: typing.Any
                ) -> AutoscalingPolicyHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
            def workflowTemplates(self) -> WorkflowTemplatesResource: ...
            def autoscalingPolicies(self) -> AutoscalingPoliciesResource: ...
        class RegionsResource(googleapiclient.discovery.Resource):
            class AutoscalingPoliciesResource(googleapiclient.discovery.Resource):
                def update(
                    self,
                    *,
                    name: str,
                    body: AutoscalingPolicy = ...,
                    **kwargs: typing.Any
                ) -> AutoscalingPolicyHttpRequest: ...
                def getIamPolicy(
                    self,
                    *,
                    resource: str,
                    body: GetIamPolicyRequest = ...,
                    **kwargs: typing.Any
                ) -> PolicyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> AutoscalingPolicyHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> ListAutoscalingPoliciesResponseHttpRequest: ...
                def testIamPermissions(
                    self,
                    *,
                    resource: str,
                    body: TestIamPermissionsRequest = ...,
                    **kwargs: typing.Any
                ) -> TestIamPermissionsResponseHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def setIamPolicy(
                    self,
                    *,
                    resource: str,
                    body: SetIamPolicyRequest = ...,
                    **kwargs: typing.Any
                ) -> PolicyHttpRequest: ...
                def create(
                    self,
                    *,
                    parent: str,
                    body: AutoscalingPolicy = ...,
                    **kwargs: typing.Any
                ) -> AutoscalingPolicyHttpRequest: ...
            class JobsResource(googleapiclient.discovery.Resource):
                def getIamPolicy(
                    self,
                    *,
                    resource: str,
                    body: GetIamPolicyRequest = ...,
                    **kwargs: typing.Any
                ) -> PolicyHttpRequest: ...
                def submitAsOperation(
                    self,
                    *,
                    projectId: str,
                    region: str,
                    body: SubmitJobRequest = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def list(
                    self,
                    *,
                    projectId: str,
                    region: str,
                    pageToken: str = ...,
                    clusterName: str = ...,
                    pageSize: int = ...,
                    jobStateMatcher: typing_extensions.Literal[
                        "ALL", "ACTIVE", "NON_ACTIVE"
                    ] = ...,
                    filter: str = ...,
                    **kwargs: typing.Any
                ) -> ListJobsResponseHttpRequest: ...
                def cancel(
                    self,
                    *,
                    projectId: str,
                    region: str,
                    jobId: str,
                    body: CancelJobRequest = ...,
                    **kwargs: typing.Any
                ) -> JobHttpRequest: ...
                def get(
                    self,
                    *,
                    projectId: str,
                    region: str,
                    jobId: str,
                    **kwargs: typing.Any
                ) -> JobHttpRequest: ...
                def setIamPolicy(
                    self,
                    *,
                    resource: str,
                    body: SetIamPolicyRequest = ...,
                    **kwargs: typing.Any
                ) -> PolicyHttpRequest: ...
                def submit(
                    self,
                    *,
                    projectId: str,
                    region: str,
                    body: SubmitJobRequest = ...,
                    **kwargs: typing.Any
                ) -> JobHttpRequest: ...
                def patch(
                    self,
                    *,
                    projectId: str,
                    region: str,
                    jobId: str,
                    body: Job = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any
                ) -> JobHttpRequest: ...
                def testIamPermissions(
                    self,
                    *,
                    resource: str,
                    body: TestIamPermissionsRequest = ...,
                    **kwargs: typing.Any
                ) -> TestIamPermissionsResponseHttpRequest: ...
                def delete(
                    self,
                    *,
                    projectId: str,
                    region: str,
                    jobId: str,
                    **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
            class OperationsResource(googleapiclient.discovery.Resource):
                def cancel(
                    self, *, name: str, **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def setIamPolicy(
                    self,
                    *,
                    resource: str,
                    body: SetIamPolicyRequest = ...,
                    **kwargs: typing.Any
                ) -> PolicyHttpRequest: ...
                def testIamPermissions(
                    self,
                    *,
                    resource: str,
                    body: TestIamPermissionsRequest = ...,
                    **kwargs: typing.Any
                ) -> TestIamPermissionsResponseHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def getIamPolicy(
                    self,
                    *,
                    resource: str,
                    body: GetIamPolicyRequest = ...,
                    **kwargs: typing.Any
                ) -> PolicyHttpRequest: ...
                def list(
                    self,
                    *,
                    name: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    filter: str = ...,
                    **kwargs: typing.Any
                ) -> ListOperationsResponseHttpRequest: ...
            class ClustersResource(googleapiclient.discovery.Resource):
                def delete(
                    self,
                    *,
                    projectId: str,
                    region: str,
                    clusterName: str,
                    requestId: str = ...,
                    clusterUuid: str = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def diagnose(
                    self,
                    *,
                    projectId: str,
                    region: str,
                    clusterName: str,
                    body: DiagnoseClusterRequest = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def getIamPolicy(
                    self,
                    *,
                    resource: str,
                    body: GetIamPolicyRequest = ...,
                    **kwargs: typing.Any
                ) -> PolicyHttpRequest: ...
                def get(
                    self,
                    *,
                    projectId: str,
                    region: str,
                    clusterName: str,
                    **kwargs: typing.Any
                ) -> ClusterHttpRequest: ...
                def testIamPermissions(
                    self,
                    *,
                    resource: str,
                    body: TestIamPermissionsRequest = ...,
                    **kwargs: typing.Any
                ) -> TestIamPermissionsResponseHttpRequest: ...
                def patch(
                    self,
                    *,
                    projectId: str,
                    region: str,
                    clusterName: str,
                    body: Cluster = ...,
                    gracefulDecommissionTimeout: str = ...,
                    requestId: str = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def create(
                    self,
                    *,
                    projectId: str,
                    region: str,
                    body: Cluster = ...,
                    requestId: str = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def setIamPolicy(
                    self,
                    *,
                    resource: str,
                    body: SetIamPolicyRequest = ...,
                    **kwargs: typing.Any
                ) -> PolicyHttpRequest: ...
                def list(
                    self,
                    *,
                    projectId: str,
                    region: str,
                    pageToken: str = ...,
                    filter: str = ...,
                    pageSize: int = ...,
                    **kwargs: typing.Any
                ) -> ListClustersResponseHttpRequest: ...
            class WorkflowTemplatesResource(googleapiclient.discovery.Resource):
                def instantiate(
                    self,
                    *,
                    name: str,
                    body: InstantiateWorkflowTemplateRequest = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def get(
                    self, *, name: str, version: int = ..., **kwargs: typing.Any
                ) -> WorkflowTemplateHttpRequest: ...
                def setIamPolicy(
                    self,
                    *,
                    resource: str,
                    body: SetIamPolicyRequest = ...,
                    **kwargs: typing.Any
                ) -> PolicyHttpRequest: ...
                def update(
                    self,
                    *,
                    name: str,
                    body: WorkflowTemplate = ...,
                    **kwargs: typing.Any
                ) -> WorkflowTemplateHttpRequest: ...
                def testIamPermissions(
                    self,
                    *,
                    resource: str,
                    body: TestIamPermissionsRequest = ...,
                    **kwargs: typing.Any
                ) -> TestIamPermissionsResponseHttpRequest: ...
                def delete(
                    self, *, name: str, version: int = ..., **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def instantiateInline(
                    self,
                    *,
                    parent: str,
                    body: WorkflowTemplate = ...,
                    requestId: str = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageToken: str = ...,
                    pageSize: int = ...,
                    **kwargs: typing.Any
                ) -> ListWorkflowTemplatesResponseHttpRequest: ...
                def create(
                    self,
                    *,
                    parent: str,
                    body: WorkflowTemplate = ...,
                    **kwargs: typing.Any
                ) -> WorkflowTemplateHttpRequest: ...
                def getIamPolicy(
                    self,
                    *,
                    resource: str,
                    body: GetIamPolicyRequest = ...,
                    **kwargs: typing.Any
                ) -> PolicyHttpRequest: ...
            def autoscalingPolicies(self) -> AutoscalingPoliciesResource: ...
            def jobs(self) -> JobsResource: ...
            def operations(self) -> OperationsResource: ...
            def clusters(self) -> ClustersResource: ...
            def workflowTemplates(self) -> WorkflowTemplatesResource: ...
        def locations(self) -> LocationsResource: ...
        def regions(self) -> RegionsResource: ...
    def projects(self) -> ProjectsResource: ...

class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Empty: ...

class JobHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Job: ...

class ListClustersResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListClustersResponse: ...

class ClusterHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Cluster: ...

class ListOperationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListOperationsResponse: ...

class AutoscalingPolicyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> AutoscalingPolicy: ...

class TestIamPermissionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> TestIamPermissionsResponse: ...

class ListJobsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListJobsResponse: ...

class PolicyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Policy: ...

class OperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Operation: ...

class WorkflowTemplateHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> WorkflowTemplate: ...

class ListAutoscalingPoliciesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListAutoscalingPoliciesResponse: ...

class ListWorkflowTemplatesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListWorkflowTemplatesResponse: ...
