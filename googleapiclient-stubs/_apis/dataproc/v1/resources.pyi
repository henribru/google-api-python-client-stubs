import collections.abc
import typing

import httplib2
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http

from .schemas import *

_list = list

@typing.type_check_only
class DataprocResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class ProjectsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class LocationsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class AutoscalingPoliciesResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: AutoscalingPolicy = ...,
                    **kwargs: typing.Any,
                ) -> AutoscalingPolicyHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> AutoscalingPolicyHttpRequest: ...
                def getIamPolicy(
                    self,
                    *,
                    resource: str,
                    body: GetIamPolicyRequest = ...,
                    **kwargs: typing.Any,
                ) -> PolicyHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> ListAutoscalingPoliciesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListAutoscalingPoliciesResponseHttpRequest,
                    previous_response: ListAutoscalingPoliciesResponse,
                ) -> ListAutoscalingPoliciesResponseHttpRequest | None: ...
                def setIamPolicy(
                    self,
                    *,
                    resource: str,
                    body: SetIamPolicyRequest = ...,
                    **kwargs: typing.Any,
                ) -> PolicyHttpRequest: ...
                def testIamPermissions(
                    self,
                    *,
                    resource: str,
                    body: TestIamPermissionsRequest = ...,
                    **kwargs: typing.Any,
                ) -> TestIamPermissionsResponseHttpRequest: ...
                def update(
                    self,
                    *,
                    name: str,
                    body: AutoscalingPolicy = ...,
                    **kwargs: typing.Any,
                ) -> AutoscalingPolicyHttpRequest: ...

            @typing.type_check_only
            class BatchesResource(googleapiclient.discovery.Resource):
                def analyze(
                    self,
                    *,
                    name: str,
                    body: AnalyzeBatchRequest = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def create(
                    self,
                    *,
                    parent: str,
                    body: Batch = ...,
                    batchId: str = ...,
                    requestId: str = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> BatchHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> ListBatchesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListBatchesResponseHttpRequest,
                    previous_response: ListBatchesResponse,
                ) -> ListBatchesResponseHttpRequest | None: ...

            @typing.type_check_only
            class OperationsResource(googleapiclient.discovery.Resource):
                def cancel(
                    self, *, name: str, **kwargs: typing.Any
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
                    **kwargs: typing.Any,
                ) -> ListOperationsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListOperationsResponseHttpRequest,
                    previous_response: ListOperationsResponse,
                ) -> ListOperationsResponseHttpRequest | None: ...

            @typing.type_check_only
            class SessionTemplatesResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: SessionTemplate = ...,
                    **kwargs: typing.Any,
                ) -> SessionTemplateHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> SessionTemplateHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> ListSessionTemplatesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListSessionTemplatesResponseHttpRequest,
                    previous_response: ListSessionTemplatesResponse,
                ) -> ListSessionTemplatesResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: SessionTemplate = ...,
                    **kwargs: typing.Any,
                ) -> SessionTemplateHttpRequest: ...

            @typing.type_check_only
            class SessionsResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: Session = ...,
                    requestId: str = ...,
                    sessionId: str = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def delete(
                    self, *, name: str, requestId: str = ..., **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> SessionHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> ListSessionsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListSessionsResponseHttpRequest,
                    previous_response: ListSessionsResponse,
                ) -> ListSessionsResponseHttpRequest | None: ...
                def terminate(
                    self,
                    *,
                    name: str,
                    body: TerminateSessionRequest = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...

            @typing.type_check_only
            class WorkflowTemplatesResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: WorkflowTemplate = ...,
                    **kwargs: typing.Any,
                ) -> WorkflowTemplateHttpRequest: ...
                def delete(
                    self, *, name: str, version: int = ..., **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def get(
                    self, *, name: str, version: int = ..., **kwargs: typing.Any
                ) -> WorkflowTemplateHttpRequest: ...
                def getIamPolicy(
                    self,
                    *,
                    resource: str,
                    body: GetIamPolicyRequest = ...,
                    **kwargs: typing.Any,
                ) -> PolicyHttpRequest: ...
                def instantiate(
                    self,
                    *,
                    name: str,
                    body: InstantiateWorkflowTemplateRequest = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def instantiateInline(
                    self,
                    *,
                    parent: str,
                    body: WorkflowTemplate = ...,
                    requestId: str = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> ListWorkflowTemplatesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListWorkflowTemplatesResponseHttpRequest,
                    previous_response: ListWorkflowTemplatesResponse,
                ) -> ListWorkflowTemplatesResponseHttpRequest | None: ...
                def setIamPolicy(
                    self,
                    *,
                    resource: str,
                    body: SetIamPolicyRequest = ...,
                    **kwargs: typing.Any,
                ) -> PolicyHttpRequest: ...
                def testIamPermissions(
                    self,
                    *,
                    resource: str,
                    body: TestIamPermissionsRequest = ...,
                    **kwargs: typing.Any,
                ) -> TestIamPermissionsResponseHttpRequest: ...
                def update(
                    self,
                    *,
                    name: str,
                    body: WorkflowTemplate = ...,
                    **kwargs: typing.Any,
                ) -> WorkflowTemplateHttpRequest: ...

            def autoscalingPolicies(self) -> AutoscalingPoliciesResource: ...
            def batches(self) -> BatchesResource: ...
            def operations(self) -> OperationsResource: ...
            def sessionTemplates(self) -> SessionTemplatesResource: ...
            def sessions(self) -> SessionsResource: ...
            def workflowTemplates(self) -> WorkflowTemplatesResource: ...

        @typing.type_check_only
        class RegionsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class AutoscalingPoliciesResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: AutoscalingPolicy = ...,
                    **kwargs: typing.Any,
                ) -> AutoscalingPolicyHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> AutoscalingPolicyHttpRequest: ...
                def getIamPolicy(
                    self,
                    *,
                    resource: str,
                    body: GetIamPolicyRequest = ...,
                    **kwargs: typing.Any,
                ) -> PolicyHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> ListAutoscalingPoliciesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListAutoscalingPoliciesResponseHttpRequest,
                    previous_response: ListAutoscalingPoliciesResponse,
                ) -> ListAutoscalingPoliciesResponseHttpRequest | None: ...
                def setIamPolicy(
                    self,
                    *,
                    resource: str,
                    body: SetIamPolicyRequest = ...,
                    **kwargs: typing.Any,
                ) -> PolicyHttpRequest: ...
                def testIamPermissions(
                    self,
                    *,
                    resource: str,
                    body: TestIamPermissionsRequest = ...,
                    **kwargs: typing.Any,
                ) -> TestIamPermissionsResponseHttpRequest: ...
                def update(
                    self,
                    *,
                    name: str,
                    body: AutoscalingPolicy = ...,
                    **kwargs: typing.Any,
                ) -> AutoscalingPolicyHttpRequest: ...

            @typing.type_check_only
            class ClustersResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class NodeGroupsResource(googleapiclient.discovery.Resource):
                    def create(
                        self,
                        *,
                        parent: str,
                        body: NodeGroup = ...,
                        nodeGroupId: str = ...,
                        parentOperationId: str = ...,
                        requestId: str = ...,
                        **kwargs: typing.Any,
                    ) -> OperationHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> NodeGroupHttpRequest: ...
                    def repair(
                        self,
                        *,
                        name: str,
                        body: RepairNodeGroupRequest = ...,
                        **kwargs: typing.Any,
                    ) -> OperationHttpRequest: ...
                    def resize(
                        self,
                        *,
                        name: str,
                        body: ResizeNodeGroupRequest = ...,
                        **kwargs: typing.Any,
                    ) -> OperationHttpRequest: ...

                def create(
                    self,
                    *,
                    projectId: str,
                    region: str,
                    body: Cluster = ...,
                    actionOnFailedPrimaryWorkers: typing_extensions.Literal[
                        "FAILURE_ACTION_UNSPECIFIED", "NO_ACTION", "DELETE"
                    ] = ...,
                    requestId: str = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def delete(
                    self,
                    *,
                    projectId: str,
                    region: str,
                    clusterName: str,
                    clusterUuid: str = ...,
                    gracefulTerminationTimeout: str = ...,
                    requestId: str = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def diagnose(
                    self,
                    *,
                    projectId: str,
                    region: str,
                    clusterName: str,
                    body: DiagnoseClusterRequest = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def get(
                    self,
                    *,
                    projectId: str,
                    region: str,
                    clusterName: str,
                    **kwargs: typing.Any,
                ) -> ClusterHttpRequest: ...
                def getIamPolicy(
                    self,
                    *,
                    resource: str,
                    body: GetIamPolicyRequest = ...,
                    **kwargs: typing.Any,
                ) -> PolicyHttpRequest: ...
                def injectCredentials(
                    self,
                    *,
                    project: str,
                    region: str,
                    cluster: str,
                    body: InjectCredentialsRequest = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def list(
                    self,
                    *,
                    projectId: str,
                    region: str,
                    filter: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> ListClustersResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListClustersResponseHttpRequest,
                    previous_response: ListClustersResponse,
                ) -> ListClustersResponseHttpRequest | None: ...
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
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def repair(
                    self,
                    *,
                    projectId: str,
                    region: str,
                    clusterName: str,
                    body: RepairClusterRequest = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def setIamPolicy(
                    self,
                    *,
                    resource: str,
                    body: SetIamPolicyRequest = ...,
                    **kwargs: typing.Any,
                ) -> PolicyHttpRequest: ...
                def start(
                    self,
                    *,
                    projectId: str,
                    region: str,
                    clusterName: str,
                    body: StartClusterRequest = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def stop(
                    self,
                    *,
                    projectId: str,
                    region: str,
                    clusterName: str,
                    body: StopClusterRequest = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def testIamPermissions(
                    self,
                    *,
                    resource: str,
                    body: TestIamPermissionsRequest = ...,
                    **kwargs: typing.Any,
                ) -> TestIamPermissionsResponseHttpRequest: ...
                def nodeGroups(self) -> NodeGroupsResource: ...

            @typing.type_check_only
            class JobsResource(googleapiclient.discovery.Resource):
                def cancel(
                    self,
                    *,
                    projectId: str,
                    region: str,
                    jobId: str,
                    body: CancelJobRequest = ...,
                    **kwargs: typing.Any,
                ) -> JobHttpRequest: ...
                def delete(
                    self,
                    *,
                    projectId: str,
                    region: str,
                    jobId: str,
                    **kwargs: typing.Any,
                ) -> EmptyHttpRequest: ...
                def get(
                    self,
                    *,
                    projectId: str,
                    region: str,
                    jobId: str,
                    **kwargs: typing.Any,
                ) -> JobHttpRequest: ...
                def getIamPolicy(
                    self,
                    *,
                    resource: str,
                    body: GetIamPolicyRequest = ...,
                    **kwargs: typing.Any,
                ) -> PolicyHttpRequest: ...
                def list(
                    self,
                    *,
                    projectId: str,
                    region: str,
                    clusterName: str = ...,
                    filter: str = ...,
                    jobStateMatcher: typing_extensions.Literal[
                        "ALL", "ACTIVE", "NON_ACTIVE"
                    ] = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> ListJobsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListJobsResponseHttpRequest,
                    previous_response: ListJobsResponse,
                ) -> ListJobsResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    projectId: str,
                    region: str,
                    jobId: str,
                    body: Job = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> JobHttpRequest: ...
                def setIamPolicy(
                    self,
                    *,
                    resource: str,
                    body: SetIamPolicyRequest = ...,
                    **kwargs: typing.Any,
                ) -> PolicyHttpRequest: ...
                def submit(
                    self,
                    *,
                    projectId: str,
                    region: str,
                    body: SubmitJobRequest = ...,
                    **kwargs: typing.Any,
                ) -> JobHttpRequest: ...
                def submitAsOperation(
                    self,
                    *,
                    projectId: str,
                    region: str,
                    body: SubmitJobRequest = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def testIamPermissions(
                    self,
                    *,
                    resource: str,
                    body: TestIamPermissionsRequest = ...,
                    **kwargs: typing.Any,
                ) -> TestIamPermissionsResponseHttpRequest: ...

            @typing.type_check_only
            class OperationsResource(googleapiclient.discovery.Resource):
                def cancel(
                    self, *, name: str, **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
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
                    **kwargs: typing.Any,
                ) -> PolicyHttpRequest: ...
                def list(
                    self,
                    *,
                    name: str,
                    filter: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> ListOperationsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListOperationsResponseHttpRequest,
                    previous_response: ListOperationsResponse,
                ) -> ListOperationsResponseHttpRequest | None: ...
                def setIamPolicy(
                    self,
                    *,
                    resource: str,
                    body: SetIamPolicyRequest = ...,
                    **kwargs: typing.Any,
                ) -> PolicyHttpRequest: ...
                def testIamPermissions(
                    self,
                    *,
                    resource: str,
                    body: TestIamPermissionsRequest = ...,
                    **kwargs: typing.Any,
                ) -> TestIamPermissionsResponseHttpRequest: ...

            @typing.type_check_only
            class WorkflowTemplatesResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: WorkflowTemplate = ...,
                    **kwargs: typing.Any,
                ) -> WorkflowTemplateHttpRequest: ...
                def delete(
                    self, *, name: str, version: int = ..., **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def get(
                    self, *, name: str, version: int = ..., **kwargs: typing.Any
                ) -> WorkflowTemplateHttpRequest: ...
                def getIamPolicy(
                    self,
                    *,
                    resource: str,
                    body: GetIamPolicyRequest = ...,
                    **kwargs: typing.Any,
                ) -> PolicyHttpRequest: ...
                def instantiate(
                    self,
                    *,
                    name: str,
                    body: InstantiateWorkflowTemplateRequest = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def instantiateInline(
                    self,
                    *,
                    parent: str,
                    body: WorkflowTemplate = ...,
                    requestId: str = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> ListWorkflowTemplatesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListWorkflowTemplatesResponseHttpRequest,
                    previous_response: ListWorkflowTemplatesResponse,
                ) -> ListWorkflowTemplatesResponseHttpRequest | None: ...
                def setIamPolicy(
                    self,
                    *,
                    resource: str,
                    body: SetIamPolicyRequest = ...,
                    **kwargs: typing.Any,
                ) -> PolicyHttpRequest: ...
                def testIamPermissions(
                    self,
                    *,
                    resource: str,
                    body: TestIamPermissionsRequest = ...,
                    **kwargs: typing.Any,
                ) -> TestIamPermissionsResponseHttpRequest: ...
                def update(
                    self,
                    *,
                    name: str,
                    body: WorkflowTemplate = ...,
                    **kwargs: typing.Any,
                ) -> WorkflowTemplateHttpRequest: ...

            def autoscalingPolicies(self) -> AutoscalingPoliciesResource: ...
            def clusters(self) -> ClustersResource: ...
            def jobs(self) -> JobsResource: ...
            def operations(self) -> OperationsResource: ...
            def workflowTemplates(self) -> WorkflowTemplatesResource: ...

        def locations(self) -> LocationsResource: ...
        def regions(self) -> RegionsResource: ...

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
    def projects(self) -> ProjectsResource: ...

@typing.type_check_only
class AutoscalingPolicyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> AutoscalingPolicy: ...

@typing.type_check_only
class BatchHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Batch: ...

@typing.type_check_only
class ClusterHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Cluster: ...

@typing.type_check_only
class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Empty: ...

@typing.type_check_only
class JobHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Job: ...

@typing.type_check_only
class ListAutoscalingPoliciesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListAutoscalingPoliciesResponse: ...

@typing.type_check_only
class ListBatchesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListBatchesResponse: ...

@typing.type_check_only
class ListClustersResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListClustersResponse: ...

@typing.type_check_only
class ListJobsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListJobsResponse: ...

@typing.type_check_only
class ListOperationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListOperationsResponse: ...

@typing.type_check_only
class ListSessionTemplatesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListSessionTemplatesResponse: ...

@typing.type_check_only
class ListSessionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListSessionsResponse: ...

@typing.type_check_only
class ListWorkflowTemplatesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListWorkflowTemplatesResponse: ...

@typing.type_check_only
class NodeGroupHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> NodeGroup: ...

@typing.type_check_only
class OperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Operation: ...

@typing.type_check_only
class PolicyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Policy: ...

@typing.type_check_only
class SessionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Session: ...

@typing.type_check_only
class SessionTemplateHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> SessionTemplate: ...

@typing.type_check_only
class TestIamPermissionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> TestIamPermissionsResponse: ...

@typing.type_check_only
class WorkflowTemplateHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> WorkflowTemplate: ...
