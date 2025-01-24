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
                @typing.type_check_only
                class SparkApplicationsResource(googleapiclient.discovery.Resource):
                    def access(
                        self, *, name: str, parent: str = ..., **kwargs: typing.Any
                    ) -> AccessSparkApplicationResponseHttpRequest: ...
                    def accessEnvironmentInfo(
                        self, *, name: str, parent: str = ..., **kwargs: typing.Any
                    ) -> AccessSparkApplicationEnvironmentInfoResponseHttpRequest: ...
                    def accessJob(
                        self,
                        *,
                        name: str,
                        jobId: str = ...,
                        parent: str = ...,
                        **kwargs: typing.Any,
                    ) -> AccessSparkApplicationJobResponseHttpRequest: ...
                    def accessSqlPlan(
                        self,
                        *,
                        name: str,
                        executionId: str = ...,
                        parent: str = ...,
                        **kwargs: typing.Any,
                    ) -> AccessSparkApplicationSqlSparkPlanGraphResponseHttpRequest: ...
                    def accessSqlQuery(
                        self,
                        *,
                        name: str,
                        details: bool = ...,
                        executionId: str = ...,
                        parent: str = ...,
                        planDescription: bool = ...,
                        **kwargs: typing.Any,
                    ) -> AccessSparkApplicationSqlQueryResponseHttpRequest: ...
                    def accessStageAttempt(
                        self,
                        *,
                        name: str,
                        parent: str = ...,
                        stageAttemptId: int = ...,
                        stageId: str = ...,
                        summaryMetricsMask: str = ...,
                        **kwargs: typing.Any,
                    ) -> AccessSparkApplicationStageAttemptResponseHttpRequest: ...
                    def accessStageRddGraph(
                        self,
                        *,
                        name: str,
                        parent: str = ...,
                        stageId: str = ...,
                        **kwargs: typing.Any,
                    ) -> (
                        AccessSparkApplicationStageRddOperationGraphResponseHttpRequest
                    ): ...
                    def search(
                        self,
                        *,
                        parent: str,
                        applicationStatus: typing_extensions.Literal[
                            "APPLICATION_STATUS_UNSPECIFIED",
                            "APPLICATION_STATUS_RUNNING",
                            "APPLICATION_STATUS_COMPLETED",
                        ] = ...,
                        maxEndTime: str = ...,
                        maxTime: str = ...,
                        minEndTime: str = ...,
                        minTime: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
                    ) -> SearchSparkApplicationsResponseHttpRequest: ...
                    def search_next(
                        self,
                        previous_request: SearchSparkApplicationsResponseHttpRequest,
                        previous_response: SearchSparkApplicationsResponse,
                    ) -> SearchSparkApplicationsResponseHttpRequest | None: ...
                    def searchExecutorStageSummary(
                        self,
                        *,
                        name: str,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        parent: str = ...,
                        stageAttemptId: int = ...,
                        stageId: str = ...,
                        **kwargs: typing.Any,
                    ) -> (
                        SearchSparkApplicationExecutorStageSummaryResponseHttpRequest
                    ): ...
                    def searchExecutorStageSummary_next(
                        self,
                        previous_request: SearchSparkApplicationExecutorStageSummaryResponseHttpRequest,
                        previous_response: SearchSparkApplicationExecutorStageSummaryResponse,
                    ) -> (
                        SearchSparkApplicationExecutorStageSummaryResponseHttpRequest
                        | None
                    ): ...
                    def searchExecutors(
                        self,
                        *,
                        name: str,
                        executorStatus: typing_extensions.Literal[
                            "EXECUTOR_STATUS_UNSPECIFIED",
                            "EXECUTOR_STATUS_ACTIVE",
                            "EXECUTOR_STATUS_DEAD",
                        ] = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        parent: str = ...,
                        **kwargs: typing.Any,
                    ) -> SearchSparkApplicationExecutorsResponseHttpRequest: ...
                    def searchExecutors_next(
                        self,
                        previous_request: SearchSparkApplicationExecutorsResponseHttpRequest,
                        previous_response: SearchSparkApplicationExecutorsResponse,
                    ) -> SearchSparkApplicationExecutorsResponseHttpRequest | None: ...
                    def searchJobs(
                        self,
                        *,
                        name: str,
                        jobStatus: typing_extensions.Literal[
                            "JOB_EXECUTION_STATUS_UNSPECIFIED",
                            "JOB_EXECUTION_STATUS_RUNNING",
                            "JOB_EXECUTION_STATUS_SUCCEEDED",
                            "JOB_EXECUTION_STATUS_FAILED",
                            "JOB_EXECUTION_STATUS_UNKNOWN",
                        ] = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        parent: str = ...,
                        **kwargs: typing.Any,
                    ) -> SearchSparkApplicationJobsResponseHttpRequest: ...
                    def searchJobs_next(
                        self,
                        previous_request: SearchSparkApplicationJobsResponseHttpRequest,
                        previous_response: SearchSparkApplicationJobsResponse,
                    ) -> SearchSparkApplicationJobsResponseHttpRequest | None: ...
                    def searchSqlQueries(
                        self,
                        *,
                        name: str,
                        details: bool = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        parent: str = ...,
                        planDescription: bool = ...,
                        **kwargs: typing.Any,
                    ) -> SearchSparkApplicationSqlQueriesResponseHttpRequest: ...
                    def searchSqlQueries_next(
                        self,
                        previous_request: SearchSparkApplicationSqlQueriesResponseHttpRequest,
                        previous_response: SearchSparkApplicationSqlQueriesResponse,
                    ) -> SearchSparkApplicationSqlQueriesResponseHttpRequest | None: ...
                    def searchStageAttemptTasks(
                        self,
                        *,
                        name: str,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        parent: str = ...,
                        sortRuntime: bool = ...,
                        stageAttemptId: int = ...,
                        stageId: str = ...,
                        taskStatus: typing_extensions.Literal[
                            "TASK_STATUS_UNSPECIFIED",
                            "TASK_STATUS_RUNNING",
                            "TASK_STATUS_SUCCESS",
                            "TASK_STATUS_FAILED",
                            "TASK_STATUS_KILLED",
                            "TASK_STATUS_PENDING",
                        ] = ...,
                        **kwargs: typing.Any,
                    ) -> SearchSparkApplicationStageAttemptTasksResponseHttpRequest: ...
                    def searchStageAttemptTasks_next(
                        self,
                        previous_request: SearchSparkApplicationStageAttemptTasksResponseHttpRequest,
                        previous_response: SearchSparkApplicationStageAttemptTasksResponse,
                    ) -> (
                        SearchSparkApplicationStageAttemptTasksResponseHttpRequest
                        | None
                    ): ...
                    def searchStageAttempts(
                        self,
                        *,
                        name: str,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        parent: str = ...,
                        stageId: str = ...,
                        summaryMetricsMask: str = ...,
                        **kwargs: typing.Any,
                    ) -> SearchSparkApplicationStageAttemptsResponseHttpRequest: ...
                    def searchStageAttempts_next(
                        self,
                        previous_request: SearchSparkApplicationStageAttemptsResponseHttpRequest,
                        previous_response: SearchSparkApplicationStageAttemptsResponse,
                    ) -> (
                        SearchSparkApplicationStageAttemptsResponseHttpRequest | None
                    ): ...
                    def searchStages(
                        self,
                        *,
                        name: str,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        parent: str = ...,
                        stageStatus: typing_extensions.Literal[
                            "STAGE_STATUS_UNSPECIFIED",
                            "STAGE_STATUS_ACTIVE",
                            "STAGE_STATUS_COMPLETE",
                            "STAGE_STATUS_FAILED",
                            "STAGE_STATUS_PENDING",
                            "STAGE_STATUS_SKIPPED",
                        ] = ...,
                        summaryMetricsMask: str = ...,
                        **kwargs: typing.Any,
                    ) -> SearchSparkApplicationStagesResponseHttpRequest: ...
                    def searchStages_next(
                        self,
                        previous_request: SearchSparkApplicationStagesResponseHttpRequest,
                        previous_response: SearchSparkApplicationStagesResponse,
                    ) -> SearchSparkApplicationStagesResponseHttpRequest | None: ...
                    def summarizeExecutors(
                        self, *, name: str, parent: str = ..., **kwargs: typing.Any
                    ) -> SummarizeSparkApplicationExecutorsResponseHttpRequest: ...
                    def summarizeJobs(
                        self, *, name: str, parent: str = ..., **kwargs: typing.Any
                    ) -> SummarizeSparkApplicationJobsResponseHttpRequest: ...
                    def summarizeStageAttemptTasks(
                        self,
                        *,
                        name: str,
                        parent: str = ...,
                        stageAttemptId: int = ...,
                        stageId: str = ...,
                        **kwargs: typing.Any,
                    ) -> (
                        SummarizeSparkApplicationStageAttemptTasksResponseHttpRequest
                    ): ...
                    def summarizeStages(
                        self, *, name: str, parent: str = ..., **kwargs: typing.Any
                    ) -> SummarizeSparkApplicationStagesResponseHttpRequest: ...
                    def write(
                        self,
                        *,
                        name: str,
                        body: WriteSparkApplicationContextRequest = ...,
                        **kwargs: typing.Any,
                    ) -> WriteSparkApplicationContextResponseHttpRequest: ...

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
                def sparkApplications(self) -> SparkApplicationsResource: ...

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
                @typing.type_check_only
                class SparkApplicationsResource(googleapiclient.discovery.Resource):
                    def access(
                        self, *, name: str, parent: str = ..., **kwargs: typing.Any
                    ) -> AccessSessionSparkApplicationResponseHttpRequest: ...
                    def accessEnvironmentInfo(
                        self, *, name: str, parent: str = ..., **kwargs: typing.Any
                    ) -> (
                        AccessSessionSparkApplicationEnvironmentInfoResponseHttpRequest
                    ): ...
                    def accessJob(
                        self,
                        *,
                        name: str,
                        jobId: str = ...,
                        parent: str = ...,
                        **kwargs: typing.Any,
                    ) -> AccessSessionSparkApplicationJobResponseHttpRequest: ...
                    def accessSqlPlan(
                        self,
                        *,
                        name: str,
                        executionId: str = ...,
                        parent: str = ...,
                        **kwargs: typing.Any,
                    ) -> AccessSessionSparkApplicationSqlSparkPlanGraphResponseHttpRequest: ...
                    def accessSqlQuery(
                        self,
                        *,
                        name: str,
                        details: bool = ...,
                        executionId: str = ...,
                        parent: str = ...,
                        planDescription: bool = ...,
                        **kwargs: typing.Any,
                    ) -> AccessSessionSparkApplicationSqlQueryResponseHttpRequest: ...
                    def accessStageAttempt(
                        self,
                        *,
                        name: str,
                        parent: str = ...,
                        stageAttemptId: int = ...,
                        stageId: str = ...,
                        summaryMetricsMask: str = ...,
                        **kwargs: typing.Any,
                    ) -> (
                        AccessSessionSparkApplicationStageAttemptResponseHttpRequest
                    ): ...
                    def accessStageRddGraph(
                        self,
                        *,
                        name: str,
                        parent: str = ...,
                        stageId: str = ...,
                        **kwargs: typing.Any,
                    ) -> AccessSessionSparkApplicationStageRddOperationGraphResponseHttpRequest: ...
                    def search(
                        self,
                        *,
                        parent: str,
                        applicationStatus: typing_extensions.Literal[
                            "APPLICATION_STATUS_UNSPECIFIED",
                            "APPLICATION_STATUS_RUNNING",
                            "APPLICATION_STATUS_COMPLETED",
                        ] = ...,
                        maxEndTime: str = ...,
                        maxTime: str = ...,
                        minEndTime: str = ...,
                        minTime: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
                    ) -> SearchSessionSparkApplicationsResponseHttpRequest: ...
                    def search_next(
                        self,
                        previous_request: SearchSessionSparkApplicationsResponseHttpRequest,
                        previous_response: SearchSessionSparkApplicationsResponse,
                    ) -> SearchSessionSparkApplicationsResponseHttpRequest | None: ...
                    def searchExecutorStageSummary(
                        self,
                        *,
                        name: str,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        parent: str = ...,
                        stageAttemptId: int = ...,
                        stageId: str = ...,
                        **kwargs: typing.Any,
                    ) -> SearchSessionSparkApplicationExecutorStageSummaryResponseHttpRequest: ...
                    def searchExecutorStageSummary_next(
                        self,
                        previous_request: SearchSessionSparkApplicationExecutorStageSummaryResponseHttpRequest,
                        previous_response: SearchSessionSparkApplicationExecutorStageSummaryResponse,
                    ) -> (
                        SearchSessionSparkApplicationExecutorStageSummaryResponseHttpRequest
                        | None
                    ): ...
                    def searchExecutors(
                        self,
                        *,
                        name: str,
                        executorStatus: typing_extensions.Literal[
                            "EXECUTOR_STATUS_UNSPECIFIED",
                            "EXECUTOR_STATUS_ACTIVE",
                            "EXECUTOR_STATUS_DEAD",
                        ] = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        parent: str = ...,
                        **kwargs: typing.Any,
                    ) -> SearchSessionSparkApplicationExecutorsResponseHttpRequest: ...
                    def searchExecutors_next(
                        self,
                        previous_request: SearchSessionSparkApplicationExecutorsResponseHttpRequest,
                        previous_response: SearchSessionSparkApplicationExecutorsResponse,
                    ) -> (
                        SearchSessionSparkApplicationExecutorsResponseHttpRequest | None
                    ): ...
                    def searchJobs(
                        self,
                        *,
                        name: str,
                        jobStatus: typing_extensions.Literal[
                            "JOB_EXECUTION_STATUS_UNSPECIFIED",
                            "JOB_EXECUTION_STATUS_RUNNING",
                            "JOB_EXECUTION_STATUS_SUCCEEDED",
                            "JOB_EXECUTION_STATUS_FAILED",
                            "JOB_EXECUTION_STATUS_UNKNOWN",
                        ] = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        parent: str = ...,
                        **kwargs: typing.Any,
                    ) -> SearchSessionSparkApplicationJobsResponseHttpRequest: ...
                    def searchJobs_next(
                        self,
                        previous_request: SearchSessionSparkApplicationJobsResponseHttpRequest,
                        previous_response: SearchSessionSparkApplicationJobsResponse,
                    ) -> (
                        SearchSessionSparkApplicationJobsResponseHttpRequest | None
                    ): ...
                    def searchSqlQueries(
                        self,
                        *,
                        name: str,
                        details: bool = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        parent: str = ...,
                        planDescription: bool = ...,
                        **kwargs: typing.Any,
                    ) -> SearchSessionSparkApplicationSqlQueriesResponseHttpRequest: ...
                    def searchSqlQueries_next(
                        self,
                        previous_request: SearchSessionSparkApplicationSqlQueriesResponseHttpRequest,
                        previous_response: SearchSessionSparkApplicationSqlQueriesResponse,
                    ) -> (
                        SearchSessionSparkApplicationSqlQueriesResponseHttpRequest
                        | None
                    ): ...
                    def searchStageAttemptTasks(
                        self,
                        *,
                        name: str,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        parent: str = ...,
                        sortRuntime: bool = ...,
                        stageAttemptId: int = ...,
                        stageId: str = ...,
                        taskStatus: typing_extensions.Literal[
                            "TASK_STATUS_UNSPECIFIED",
                            "TASK_STATUS_RUNNING",
                            "TASK_STATUS_SUCCESS",
                            "TASK_STATUS_FAILED",
                            "TASK_STATUS_KILLED",
                            "TASK_STATUS_PENDING",
                        ] = ...,
                        **kwargs: typing.Any,
                    ) -> SearchSessionSparkApplicationStageAttemptTasksResponseHttpRequest: ...
                    def searchStageAttemptTasks_next(
                        self,
                        previous_request: SearchSessionSparkApplicationStageAttemptTasksResponseHttpRequest,
                        previous_response: SearchSessionSparkApplicationStageAttemptTasksResponse,
                    ) -> (
                        SearchSessionSparkApplicationStageAttemptTasksResponseHttpRequest
                        | None
                    ): ...
                    def searchStageAttempts(
                        self,
                        *,
                        name: str,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        parent: str = ...,
                        stageId: str = ...,
                        summaryMetricsMask: str = ...,
                        **kwargs: typing.Any,
                    ) -> (
                        SearchSessionSparkApplicationStageAttemptsResponseHttpRequest
                    ): ...
                    def searchStageAttempts_next(
                        self,
                        previous_request: SearchSessionSparkApplicationStageAttemptsResponseHttpRequest,
                        previous_response: SearchSessionSparkApplicationStageAttemptsResponse,
                    ) -> (
                        SearchSessionSparkApplicationStageAttemptsResponseHttpRequest
                        | None
                    ): ...
                    def searchStages(
                        self,
                        *,
                        name: str,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        parent: str = ...,
                        stageStatus: typing_extensions.Literal[
                            "STAGE_STATUS_UNSPECIFIED",
                            "STAGE_STATUS_ACTIVE",
                            "STAGE_STATUS_COMPLETE",
                            "STAGE_STATUS_FAILED",
                            "STAGE_STATUS_PENDING",
                            "STAGE_STATUS_SKIPPED",
                        ] = ...,
                        summaryMetricsMask: str = ...,
                        **kwargs: typing.Any,
                    ) -> SearchSessionSparkApplicationStagesResponseHttpRequest: ...
                    def searchStages_next(
                        self,
                        previous_request: SearchSessionSparkApplicationStagesResponseHttpRequest,
                        previous_response: SearchSessionSparkApplicationStagesResponse,
                    ) -> (
                        SearchSessionSparkApplicationStagesResponseHttpRequest | None
                    ): ...
                    def summarizeExecutors(
                        self, *, name: str, parent: str = ..., **kwargs: typing.Any
                    ) -> (
                        SummarizeSessionSparkApplicationExecutorsResponseHttpRequest
                    ): ...
                    def summarizeJobs(
                        self, *, name: str, parent: str = ..., **kwargs: typing.Any
                    ) -> SummarizeSessionSparkApplicationJobsResponseHttpRequest: ...
                    def summarizeStageAttemptTasks(
                        self,
                        *,
                        name: str,
                        parent: str = ...,
                        stageAttemptId: int = ...,
                        stageId: str = ...,
                        **kwargs: typing.Any,
                    ) -> SummarizeSessionSparkApplicationStageAttemptTasksResponseHttpRequest: ...
                    def summarizeStages(
                        self, *, name: str, parent: str = ..., **kwargs: typing.Any
                    ) -> SummarizeSessionSparkApplicationStagesResponseHttpRequest: ...
                    def write(
                        self,
                        *,
                        name: str,
                        body: WriteSessionSparkApplicationContextRequest = ...,
                        **kwargs: typing.Any,
                    ) -> WriteSessionSparkApplicationContextResponseHttpRequest: ...

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
                def sparkApplications(self) -> SparkApplicationsResource: ...

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
class AccessSessionSparkApplicationEnvironmentInfoResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> AccessSessionSparkApplicationEnvironmentInfoResponse: ...

@typing.type_check_only
class AccessSessionSparkApplicationJobResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> AccessSessionSparkApplicationJobResponse: ...

@typing.type_check_only
class AccessSessionSparkApplicationResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> AccessSessionSparkApplicationResponse: ...

@typing.type_check_only
class AccessSessionSparkApplicationSqlQueryResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> AccessSessionSparkApplicationSqlQueryResponse: ...

@typing.type_check_only
class AccessSessionSparkApplicationSqlSparkPlanGraphResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> AccessSessionSparkApplicationSqlSparkPlanGraphResponse: ...

@typing.type_check_only
class AccessSessionSparkApplicationStageAttemptResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> AccessSessionSparkApplicationStageAttemptResponse: ...

@typing.type_check_only
class AccessSessionSparkApplicationStageRddOperationGraphResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> AccessSessionSparkApplicationStageRddOperationGraphResponse: ...

@typing.type_check_only
class AccessSparkApplicationEnvironmentInfoResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> AccessSparkApplicationEnvironmentInfoResponse: ...

@typing.type_check_only
class AccessSparkApplicationJobResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> AccessSparkApplicationJobResponse: ...

@typing.type_check_only
class AccessSparkApplicationResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> AccessSparkApplicationResponse: ...

@typing.type_check_only
class AccessSparkApplicationSqlQueryResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> AccessSparkApplicationSqlQueryResponse: ...

@typing.type_check_only
class AccessSparkApplicationSqlSparkPlanGraphResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> AccessSparkApplicationSqlSparkPlanGraphResponse: ...

@typing.type_check_only
class AccessSparkApplicationStageAttemptResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> AccessSparkApplicationStageAttemptResponse: ...

@typing.type_check_only
class AccessSparkApplicationStageRddOperationGraphResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> AccessSparkApplicationStageRddOperationGraphResponse: ...

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
class SearchSessionSparkApplicationExecutorStageSummaryResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> SearchSessionSparkApplicationExecutorStageSummaryResponse: ...

@typing.type_check_only
class SearchSessionSparkApplicationExecutorsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> SearchSessionSparkApplicationExecutorsResponse: ...

@typing.type_check_only
class SearchSessionSparkApplicationJobsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> SearchSessionSparkApplicationJobsResponse: ...

@typing.type_check_only
class SearchSessionSparkApplicationSqlQueriesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> SearchSessionSparkApplicationSqlQueriesResponse: ...

@typing.type_check_only
class SearchSessionSparkApplicationStageAttemptTasksResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> SearchSessionSparkApplicationStageAttemptTasksResponse: ...

@typing.type_check_only
class SearchSessionSparkApplicationStageAttemptsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> SearchSessionSparkApplicationStageAttemptsResponse: ...

@typing.type_check_only
class SearchSessionSparkApplicationStagesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> SearchSessionSparkApplicationStagesResponse: ...

@typing.type_check_only
class SearchSessionSparkApplicationsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> SearchSessionSparkApplicationsResponse: ...

@typing.type_check_only
class SearchSparkApplicationExecutorStageSummaryResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> SearchSparkApplicationExecutorStageSummaryResponse: ...

@typing.type_check_only
class SearchSparkApplicationExecutorsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> SearchSparkApplicationExecutorsResponse: ...

@typing.type_check_only
class SearchSparkApplicationJobsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> SearchSparkApplicationJobsResponse: ...

@typing.type_check_only
class SearchSparkApplicationSqlQueriesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> SearchSparkApplicationSqlQueriesResponse: ...

@typing.type_check_only
class SearchSparkApplicationStageAttemptTasksResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> SearchSparkApplicationStageAttemptTasksResponse: ...

@typing.type_check_only
class SearchSparkApplicationStageAttemptsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> SearchSparkApplicationStageAttemptsResponse: ...

@typing.type_check_only
class SearchSparkApplicationStagesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> SearchSparkApplicationStagesResponse: ...

@typing.type_check_only
class SearchSparkApplicationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> SearchSparkApplicationsResponse: ...

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
class SummarizeSessionSparkApplicationExecutorsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> SummarizeSessionSparkApplicationExecutorsResponse: ...

@typing.type_check_only
class SummarizeSessionSparkApplicationJobsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> SummarizeSessionSparkApplicationJobsResponse: ...

@typing.type_check_only
class SummarizeSessionSparkApplicationStageAttemptTasksResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> SummarizeSessionSparkApplicationStageAttemptTasksResponse: ...

@typing.type_check_only
class SummarizeSessionSparkApplicationStagesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> SummarizeSessionSparkApplicationStagesResponse: ...

@typing.type_check_only
class SummarizeSparkApplicationExecutorsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> SummarizeSparkApplicationExecutorsResponse: ...

@typing.type_check_only
class SummarizeSparkApplicationJobsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> SummarizeSparkApplicationJobsResponse: ...

@typing.type_check_only
class SummarizeSparkApplicationStageAttemptTasksResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> SummarizeSparkApplicationStageAttemptTasksResponse: ...

@typing.type_check_only
class SummarizeSparkApplicationStagesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> SummarizeSparkApplicationStagesResponse: ...

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

@typing.type_check_only
class WriteSessionSparkApplicationContextResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> WriteSessionSparkApplicationContextResponse: ...

@typing.type_check_only
class WriteSparkApplicationContextResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> WriteSparkApplicationContextResponse: ...
