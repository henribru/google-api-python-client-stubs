import collections.abc
import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

_list = list

@typing.type_check_only
class AIPlatformNotebooksResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class ProjectsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class LocationsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class EnvironmentsResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: Environment = ...,
                    environmentId: str = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> EnvironmentHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> ListEnvironmentsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListEnvironmentsResponseHttpRequest,
                    previous_response: ListEnvironmentsResponse,
                ) -> ListEnvironmentsResponseHttpRequest | None: ...

            @typing.type_check_only
            class ExecutionsResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: Execution = ...,
                    executionId: str = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> ExecutionHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> ListExecutionsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListExecutionsResponseHttpRequest,
                    previous_response: ListExecutionsResponse,
                ) -> ListExecutionsResponseHttpRequest | None: ...

            @typing.type_check_only
            class InstancesResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: Instance = ...,
                    instanceId: str = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> InstanceHttpRequest: ...
                def getIamPolicy(
                    self,
                    *,
                    resource: str,
                    options_requestedPolicyVersion: int = ...,
                    **kwargs: typing.Any
                ) -> PolicyHttpRequest: ...
                def getInstanceHealth(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GetInstanceHealthResponseHttpRequest: ...
                def isUpgradeable(
                    self,
                    *,
                    notebookInstance: str,
                    type: typing_extensions.Literal[
                        "UPGRADE_TYPE_UNSPECIFIED",
                        "UPGRADE_FRAMEWORK",
                        "UPGRADE_OS",
                        "UPGRADE_CUDA",
                        "UPGRADE_ALL",
                    ] = ...,
                    **kwargs: typing.Any
                ) -> IsInstanceUpgradeableResponseHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> ListInstancesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListInstancesResponseHttpRequest,
                    previous_response: ListInstancesResponse,
                ) -> ListInstancesResponseHttpRequest | None: ...
                def register(
                    self,
                    *,
                    parent: str,
                    body: RegisterInstanceRequest = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def report(
                    self,
                    *,
                    name: str,
                    body: ReportInstanceInfoRequest = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def reset(
                    self,
                    *,
                    name: str,
                    body: ResetInstanceRequest = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def rollback(
                    self,
                    *,
                    name: str,
                    body: RollbackInstanceRequest = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def setAccelerator(
                    self,
                    *,
                    name: str,
                    body: SetInstanceAcceleratorRequest = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def setIamPolicy(
                    self,
                    *,
                    resource: str,
                    body: SetIamPolicyRequest = ...,
                    **kwargs: typing.Any
                ) -> PolicyHttpRequest: ...
                def setLabels(
                    self,
                    *,
                    name: str,
                    body: SetInstanceLabelsRequest = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def setMachineType(
                    self,
                    *,
                    name: str,
                    body: SetInstanceMachineTypeRequest = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def start(
                    self,
                    *,
                    name: str,
                    body: StartInstanceRequest = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def stop(
                    self,
                    *,
                    name: str,
                    body: StopInstanceRequest = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def testIamPermissions(
                    self,
                    *,
                    resource: str,
                    body: TestIamPermissionsRequest = ...,
                    **kwargs: typing.Any
                ) -> TestIamPermissionsResponseHttpRequest: ...
                def updateConfig(
                    self,
                    *,
                    name: str,
                    body: UpdateInstanceConfigRequest = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def updateMetadataItems(
                    self,
                    *,
                    name: str,
                    body: UpdateInstanceMetadataItemsRequest = ...,
                    **kwargs: typing.Any
                ) -> UpdateInstanceMetadataItemsResponseHttpRequest: ...
                def updateShieldedInstanceConfig(
                    self,
                    *,
                    name: str,
                    body: UpdateShieldedInstanceConfigRequest = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def upgrade(
                    self,
                    *,
                    name: str,
                    body: UpgradeInstanceRequest = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def upgradeInternal(
                    self,
                    *,
                    name: str,
                    body: UpgradeInstanceInternalRequest = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...

            @typing.type_check_only
            class OperationsResource(googleapiclient.discovery.Resource):
                def cancel(
                    self,
                    *,
                    name: str,
                    body: CancelOperationRequest = ...,
                    **kwargs: typing.Any
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
                    **kwargs: typing.Any
                ) -> ListOperationsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListOperationsResponseHttpRequest,
                    previous_response: ListOperationsResponse,
                ) -> ListOperationsResponseHttpRequest | None: ...

            @typing.type_check_only
            class RuntimesResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: Runtime = ...,
                    requestId: str = ...,
                    runtimeId: str = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def delete(
                    self, *, name: str, requestId: str = ..., **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> RuntimeHttpRequest: ...
                def getIamPolicy(
                    self,
                    *,
                    resource: str,
                    options_requestedPolicyVersion: int = ...,
                    **kwargs: typing.Any
                ) -> PolicyHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> ListRuntimesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListRuntimesResponseHttpRequest,
                    previous_response: ListRuntimesResponse,
                ) -> ListRuntimesResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: Runtime = ...,
                    requestId: str = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def refreshRuntimeTokenInternal(
                    self,
                    *,
                    name: str,
                    body: RefreshRuntimeTokenInternalRequest = ...,
                    **kwargs: typing.Any
                ) -> RefreshRuntimeTokenInternalResponseHttpRequest: ...
                def reportEvent(
                    self,
                    *,
                    name: str,
                    body: ReportRuntimeEventRequest = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def reset(
                    self,
                    *,
                    name: str,
                    body: ResetRuntimeRequest = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def setIamPolicy(
                    self,
                    *,
                    resource: str,
                    body: SetIamPolicyRequest = ...,
                    **kwargs: typing.Any
                ) -> PolicyHttpRequest: ...
                def start(
                    self,
                    *,
                    name: str,
                    body: StartRuntimeRequest = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def stop(
                    self,
                    *,
                    name: str,
                    body: StopRuntimeRequest = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def switch(
                    self,
                    *,
                    name: str,
                    body: SwitchRuntimeRequest = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def testIamPermissions(
                    self,
                    *,
                    resource: str,
                    body: TestIamPermissionsRequest = ...,
                    **kwargs: typing.Any
                ) -> TestIamPermissionsResponseHttpRequest: ...

            @typing.type_check_only
            class SchedulesResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: Schedule = ...,
                    scheduleId: str = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> ScheduleHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> ListSchedulesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListSchedulesResponseHttpRequest,
                    previous_response: ListSchedulesResponse,
                ) -> ListSchedulesResponseHttpRequest | None: ...
                def trigger(
                    self,
                    *,
                    name: str,
                    body: TriggerScheduleRequest = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...

            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> LocationHttpRequest: ...
            def list(
                self,
                *,
                name: str,
                filter: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> ListLocationsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListLocationsResponseHttpRequest,
                previous_response: ListLocationsResponse,
            ) -> ListLocationsResponseHttpRequest | None: ...
            def environments(self) -> EnvironmentsResource: ...
            def executions(self) -> ExecutionsResource: ...
            def instances(self) -> InstancesResource: ...
            def operations(self) -> OperationsResource: ...
            def runtimes(self) -> RuntimesResource: ...
            def schedules(self) -> SchedulesResource: ...

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
    def projects(self) -> ProjectsResource: ...

@typing.type_check_only
class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Empty: ...

@typing.type_check_only
class EnvironmentHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Environment: ...

@typing.type_check_only
class ExecutionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Execution: ...

@typing.type_check_only
class GetInstanceHealthResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GetInstanceHealthResponse: ...

@typing.type_check_only
class InstanceHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Instance: ...

@typing.type_check_only
class IsInstanceUpgradeableResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> IsInstanceUpgradeableResponse: ...

@typing.type_check_only
class ListEnvironmentsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListEnvironmentsResponse: ...

@typing.type_check_only
class ListExecutionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListExecutionsResponse: ...

@typing.type_check_only
class ListInstancesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListInstancesResponse: ...

@typing.type_check_only
class ListLocationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListLocationsResponse: ...

@typing.type_check_only
class ListOperationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListOperationsResponse: ...

@typing.type_check_only
class ListRuntimesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListRuntimesResponse: ...

@typing.type_check_only
class ListSchedulesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListSchedulesResponse: ...

@typing.type_check_only
class LocationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Location: ...

@typing.type_check_only
class OperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Operation: ...

@typing.type_check_only
class PolicyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Policy: ...

@typing.type_check_only
class RefreshRuntimeTokenInternalResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> RefreshRuntimeTokenInternalResponse: ...

@typing.type_check_only
class RuntimeHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Runtime: ...

@typing.type_check_only
class ScheduleHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Schedule: ...

@typing.type_check_only
class TestIamPermissionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> TestIamPermissionsResponse: ...

@typing.type_check_only
class UpdateInstanceMetadataItemsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> UpdateInstanceMetadataItemsResponse: ...
