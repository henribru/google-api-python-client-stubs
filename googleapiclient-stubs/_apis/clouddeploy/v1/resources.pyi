import collections.abc
import typing

import httplib2
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http

from .schemas import *

_list = list

@typing.type_check_only
class CloudDeployResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class ProjectsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class LocationsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class CustomTargetTypesResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: CustomTargetType = ...,
                    customTargetTypeId: str = ...,
                    requestId: str = ...,
                    validateOnly: bool = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def delete(
                    self,
                    *,
                    name: str,
                    allowMissing: bool = ...,
                    etag: str = ...,
                    requestId: str = ...,
                    validateOnly: bool = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> CustomTargetTypeHttpRequest: ...
                def getIamPolicy(
                    self,
                    *,
                    resource: str,
                    options_requestedPolicyVersion: int = ...,
                    **kwargs: typing.Any,
                ) -> PolicyHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> ListCustomTargetTypesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListCustomTargetTypesResponseHttpRequest,
                    previous_response: ListCustomTargetTypesResponse,
                ) -> ListCustomTargetTypesResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: CustomTargetType = ...,
                    allowMissing: bool = ...,
                    requestId: str = ...,
                    updateMask: str = ...,
                    validateOnly: bool = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def setIamPolicy(
                    self,
                    *,
                    resource: str,
                    body: SetIamPolicyRequest = ...,
                    **kwargs: typing.Any,
                ) -> PolicyHttpRequest: ...

            @typing.type_check_only
            class DeliveryPipelinesResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class AutomationRunsResource(googleapiclient.discovery.Resource):
                    def cancel(
                        self,
                        *,
                        name: str,
                        body: CancelAutomationRunRequest = ...,
                        **kwargs: typing.Any,
                    ) -> CancelAutomationRunResponseHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> AutomationRunHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str = ...,
                        orderBy: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
                    ) -> ListAutomationRunsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: ListAutomationRunsResponseHttpRequest,
                        previous_response: ListAutomationRunsResponse,
                    ) -> ListAutomationRunsResponseHttpRequest | None: ...

                @typing.type_check_only
                class AutomationsResource(googleapiclient.discovery.Resource):
                    def create(
                        self,
                        *,
                        parent: str,
                        body: Automation = ...,
                        automationId: str = ...,
                        requestId: str = ...,
                        validateOnly: bool = ...,
                        **kwargs: typing.Any,
                    ) -> OperationHttpRequest: ...
                    def delete(
                        self,
                        *,
                        name: str,
                        allowMissing: bool = ...,
                        etag: str = ...,
                        requestId: str = ...,
                        validateOnly: bool = ...,
                        **kwargs: typing.Any,
                    ) -> OperationHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> AutomationHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str = ...,
                        orderBy: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
                    ) -> ListAutomationsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: ListAutomationsResponseHttpRequest,
                        previous_response: ListAutomationsResponse,
                    ) -> ListAutomationsResponseHttpRequest | None: ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: Automation = ...,
                        allowMissing: bool = ...,
                        requestId: str = ...,
                        updateMask: str = ...,
                        validateOnly: bool = ...,
                        **kwargs: typing.Any,
                    ) -> OperationHttpRequest: ...

                @typing.type_check_only
                class ReleasesResource(googleapiclient.discovery.Resource):
                    @typing.type_check_only
                    class RolloutsResource(googleapiclient.discovery.Resource):
                        @typing.type_check_only
                        class JobRunsResource(googleapiclient.discovery.Resource):
                            def get(
                                self, *, name: str, **kwargs: typing.Any
                            ) -> JobRunHttpRequest: ...
                            def list(
                                self,
                                *,
                                parent: str,
                                filter: str = ...,
                                orderBy: str = ...,
                                pageSize: int = ...,
                                pageToken: str = ...,
                                **kwargs: typing.Any,
                            ) -> ListJobRunsResponseHttpRequest: ...
                            def list_next(
                                self,
                                previous_request: ListJobRunsResponseHttpRequest,
                                previous_response: ListJobRunsResponse,
                            ) -> ListJobRunsResponseHttpRequest | None: ...
                            def terminate(
                                self,
                                *,
                                name: str,
                                body: TerminateJobRunRequest = ...,
                                **kwargs: typing.Any,
                            ) -> TerminateJobRunResponseHttpRequest: ...

                        def advance(
                            self,
                            *,
                            name: str,
                            body: AdvanceRolloutRequest = ...,
                            **kwargs: typing.Any,
                        ) -> AdvanceRolloutResponseHttpRequest: ...
                        def approve(
                            self,
                            *,
                            name: str,
                            body: ApproveRolloutRequest = ...,
                            **kwargs: typing.Any,
                        ) -> ApproveRolloutResponseHttpRequest: ...
                        def cancel(
                            self,
                            *,
                            name: str,
                            body: CancelRolloutRequest = ...,
                            **kwargs: typing.Any,
                        ) -> CancelRolloutResponseHttpRequest: ...
                        def create(
                            self,
                            *,
                            parent: str,
                            body: Rollout = ...,
                            overrideDeployPolicy: str | _list[str] = ...,
                            requestId: str = ...,
                            rolloutId: str = ...,
                            startingPhaseId: str = ...,
                            validateOnly: bool = ...,
                            **kwargs: typing.Any,
                        ) -> OperationHttpRequest: ...
                        def get(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> RolloutHttpRequest: ...
                        def ignoreJob(
                            self,
                            *,
                            rollout: str,
                            body: IgnoreJobRequest = ...,
                            **kwargs: typing.Any,
                        ) -> IgnoreJobResponseHttpRequest: ...
                        def list(
                            self,
                            *,
                            parent: str,
                            filter: str = ...,
                            orderBy: str = ...,
                            pageSize: int = ...,
                            pageToken: str = ...,
                            **kwargs: typing.Any,
                        ) -> ListRolloutsResponseHttpRequest: ...
                        def list_next(
                            self,
                            previous_request: ListRolloutsResponseHttpRequest,
                            previous_response: ListRolloutsResponse,
                        ) -> ListRolloutsResponseHttpRequest | None: ...
                        def retryJob(
                            self,
                            *,
                            rollout: str,
                            body: RetryJobRequest = ...,
                            **kwargs: typing.Any,
                        ) -> RetryJobResponseHttpRequest: ...
                        def jobRuns(self) -> JobRunsResource: ...

                    def abandon(
                        self,
                        *,
                        name: str,
                        body: AbandonReleaseRequest = ...,
                        **kwargs: typing.Any,
                    ) -> AbandonReleaseResponseHttpRequest: ...
                    def create(
                        self,
                        *,
                        parent: str,
                        body: Release = ...,
                        overrideDeployPolicy: str | _list[str] = ...,
                        releaseId: str = ...,
                        requestId: str = ...,
                        validateOnly: bool = ...,
                        **kwargs: typing.Any,
                    ) -> OperationHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> ReleaseHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str = ...,
                        orderBy: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
                    ) -> ListReleasesResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: ListReleasesResponseHttpRequest,
                        previous_response: ListReleasesResponse,
                    ) -> ListReleasesResponseHttpRequest | None: ...
                    def rollouts(self) -> RolloutsResource: ...

                def create(
                    self,
                    *,
                    parent: str,
                    body: DeliveryPipeline = ...,
                    deliveryPipelineId: str = ...,
                    requestId: str = ...,
                    validateOnly: bool = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def delete(
                    self,
                    *,
                    name: str,
                    allowMissing: bool = ...,
                    etag: str = ...,
                    force: bool = ...,
                    requestId: str = ...,
                    validateOnly: bool = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> DeliveryPipelineHttpRequest: ...
                def getIamPolicy(
                    self,
                    *,
                    resource: str,
                    options_requestedPolicyVersion: int = ...,
                    **kwargs: typing.Any,
                ) -> PolicyHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> ListDeliveryPipelinesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListDeliveryPipelinesResponseHttpRequest,
                    previous_response: ListDeliveryPipelinesResponse,
                ) -> ListDeliveryPipelinesResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: DeliveryPipeline = ...,
                    allowMissing: bool = ...,
                    requestId: str = ...,
                    updateMask: str = ...,
                    validateOnly: bool = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def rollbackTarget(
                    self,
                    *,
                    name: str,
                    body: RollbackTargetRequest = ...,
                    **kwargs: typing.Any,
                ) -> RollbackTargetResponseHttpRequest: ...
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
                def automationRuns(self) -> AutomationRunsResource: ...
                def automations(self) -> AutomationsResource: ...
                def releases(self) -> ReleasesResource: ...

            @typing.type_check_only
            class DeployPoliciesResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: DeployPolicy = ...,
                    deployPolicyId: str = ...,
                    requestId: str = ...,
                    validateOnly: bool = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def delete(
                    self,
                    *,
                    name: str,
                    allowMissing: bool = ...,
                    etag: str = ...,
                    requestId: str = ...,
                    validateOnly: bool = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> DeployPolicyHttpRequest: ...
                def getIamPolicy(
                    self,
                    *,
                    resource: str,
                    options_requestedPolicyVersion: int = ...,
                    **kwargs: typing.Any,
                ) -> PolicyHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> ListDeployPoliciesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListDeployPoliciesResponseHttpRequest,
                    previous_response: ListDeployPoliciesResponse,
                ) -> ListDeployPoliciesResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: DeployPolicy = ...,
                    allowMissing: bool = ...,
                    requestId: str = ...,
                    updateMask: str = ...,
                    validateOnly: bool = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def setIamPolicy(
                    self,
                    *,
                    resource: str,
                    body: SetIamPolicyRequest = ...,
                    **kwargs: typing.Any,
                ) -> PolicyHttpRequest: ...

            @typing.type_check_only
            class OperationsResource(googleapiclient.discovery.Resource):
                def cancel(
                    self,
                    *,
                    name: str,
                    body: CancelOperationRequest = ...,
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
            class TargetsResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: Target = ...,
                    requestId: str = ...,
                    targetId: str = ...,
                    validateOnly: bool = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def delete(
                    self,
                    *,
                    name: str,
                    allowMissing: bool = ...,
                    etag: str = ...,
                    requestId: str = ...,
                    validateOnly: bool = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> TargetHttpRequest: ...
                def getIamPolicy(
                    self,
                    *,
                    resource: str,
                    options_requestedPolicyVersion: int = ...,
                    **kwargs: typing.Any,
                ) -> PolicyHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> ListTargetsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListTargetsResponseHttpRequest,
                    previous_response: ListTargetsResponse,
                ) -> ListTargetsResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: Target = ...,
                    allowMissing: bool = ...,
                    requestId: str = ...,
                    updateMask: str = ...,
                    validateOnly: bool = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
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

            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> LocationHttpRequest: ...
            def getConfig(
                self, *, name: str, **kwargs: typing.Any
            ) -> ConfigHttpRequest: ...
            def list(
                self,
                *,
                name: str,
                filter: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any,
            ) -> ListLocationsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListLocationsResponseHttpRequest,
                previous_response: ListLocationsResponse,
            ) -> ListLocationsResponseHttpRequest | None: ...
            def customTargetTypes(self) -> CustomTargetTypesResource: ...
            def deliveryPipelines(self) -> DeliveryPipelinesResource: ...
            def deployPolicies(self) -> DeployPoliciesResource: ...
            def operations(self) -> OperationsResource: ...
            def targets(self) -> TargetsResource: ...

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
    def projects(self) -> ProjectsResource: ...

@typing.type_check_only
class AbandonReleaseResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> AbandonReleaseResponse: ...

@typing.type_check_only
class AdvanceRolloutResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> AdvanceRolloutResponse: ...

@typing.type_check_only
class ApproveRolloutResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ApproveRolloutResponse: ...

@typing.type_check_only
class AutomationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Automation: ...

@typing.type_check_only
class AutomationRunHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> AutomationRun: ...

@typing.type_check_only
class CancelAutomationRunResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> CancelAutomationRunResponse: ...

@typing.type_check_only
class CancelRolloutResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> CancelRolloutResponse: ...

@typing.type_check_only
class ConfigHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Config: ...

@typing.type_check_only
class CustomTargetTypeHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> CustomTargetType: ...

@typing.type_check_only
class DeliveryPipelineHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> DeliveryPipeline: ...

@typing.type_check_only
class DeployPolicyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> DeployPolicy: ...

@typing.type_check_only
class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Empty: ...

@typing.type_check_only
class IgnoreJobResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> IgnoreJobResponse: ...

@typing.type_check_only
class JobRunHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> JobRun: ...

@typing.type_check_only
class ListAutomationRunsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListAutomationRunsResponse: ...

@typing.type_check_only
class ListAutomationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListAutomationsResponse: ...

@typing.type_check_only
class ListCustomTargetTypesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListCustomTargetTypesResponse: ...

@typing.type_check_only
class ListDeliveryPipelinesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListDeliveryPipelinesResponse: ...

@typing.type_check_only
class ListDeployPoliciesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListDeployPoliciesResponse: ...

@typing.type_check_only
class ListJobRunsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListJobRunsResponse: ...

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
class ListReleasesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListReleasesResponse: ...

@typing.type_check_only
class ListRolloutsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListRolloutsResponse: ...

@typing.type_check_only
class ListTargetsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListTargetsResponse: ...

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
class PolicyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Policy: ...

@typing.type_check_only
class ReleaseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Release: ...

@typing.type_check_only
class RetryJobResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> RetryJobResponse: ...

@typing.type_check_only
class RollbackTargetResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> RollbackTargetResponse: ...

@typing.type_check_only
class RolloutHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Rollout: ...

@typing.type_check_only
class TargetHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Target: ...

@typing.type_check_only
class TerminateJobRunResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> TerminateJobRunResponse: ...

@typing.type_check_only
class TestIamPermissionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> TestIamPermissionsResponse: ...
