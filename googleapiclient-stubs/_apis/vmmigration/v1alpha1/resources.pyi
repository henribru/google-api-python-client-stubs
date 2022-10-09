import collections.abc
import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

_list = list

@typing.type_check_only
class VMMigrationServiceResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class ProjectsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class LocationsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class GroupsResource(googleapiclient.discovery.Resource):
                def addGroupMigration(
                    self,
                    *,
                    group: str,
                    body: AddGroupMigrationRequest = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def create(
                    self,
                    *,
                    parent: str,
                    body: Group = ...,
                    groupId: str = ...,
                    requestId: str = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def delete(
                    self, *, name: str, requestId: str = ..., **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GroupHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> ListGroupsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListGroupsResponseHttpRequest,
                    previous_response: ListGroupsResponse,
                ) -> ListGroupsResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: Group = ...,
                    requestId: str = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def removeGroupMigration(
                    self,
                    *,
                    group: str,
                    body: RemoveGroupMigrationRequest = ...,
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
            class SourcesResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class DatacenterConnectorsResource(googleapiclient.discovery.Resource):
                    def create(
                        self,
                        *,
                        parent: str,
                        body: DatacenterConnector = ...,
                        datacenterConnectorId: str = ...,
                        requestId: str = ...,
                        **kwargs: typing.Any
                    ) -> OperationHttpRequest: ...
                    def delete(
                        self, *, name: str, requestId: str = ..., **kwargs: typing.Any
                    ) -> OperationHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> DatacenterConnectorHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str = ...,
                        orderBy: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any
                    ) -> ListDatacenterConnectorsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: ListDatacenterConnectorsResponseHttpRequest,
                        previous_response: ListDatacenterConnectorsResponse,
                    ) -> ListDatacenterConnectorsResponseHttpRequest | None: ...
                    def upgradeAppliance(
                        self,
                        *,
                        datacenterConnector: str,
                        body: UpgradeApplianceRequest = ...,
                        **kwargs: typing.Any
                    ) -> OperationHttpRequest: ...

                @typing.type_check_only
                class MigratingVmsResource(googleapiclient.discovery.Resource):
                    @typing.type_check_only
                    class CloneJobsResource(googleapiclient.discovery.Resource):
                        def cancel(
                            self,
                            *,
                            name: str,
                            body: CancelCloneJobRequest = ...,
                            **kwargs: typing.Any
                        ) -> OperationHttpRequest: ...
                        def create(
                            self,
                            *,
                            parent: str,
                            body: CloneJob = ...,
                            cloneJobId: str = ...,
                            requestId: str = ...,
                            **kwargs: typing.Any
                        ) -> OperationHttpRequest: ...
                        def get(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> CloneJobHttpRequest: ...
                        def list(
                            self,
                            *,
                            parent: str,
                            filter: str = ...,
                            orderBy: str = ...,
                            pageSize: int = ...,
                            pageToken: str = ...,
                            **kwargs: typing.Any
                        ) -> ListCloneJobsResponseHttpRequest: ...
                        def list_next(
                            self,
                            previous_request: ListCloneJobsResponseHttpRequest,
                            previous_response: ListCloneJobsResponse,
                        ) -> ListCloneJobsResponseHttpRequest | None: ...

                    @typing.type_check_only
                    class CutoverJobsResource(googleapiclient.discovery.Resource):
                        def cancel(
                            self,
                            *,
                            name: str,
                            body: CancelCutoverJobRequest = ...,
                            **kwargs: typing.Any
                        ) -> OperationHttpRequest: ...
                        def create(
                            self,
                            *,
                            parent: str,
                            body: CutoverJob = ...,
                            cutoverJobId: str = ...,
                            requestId: str = ...,
                            **kwargs: typing.Any
                        ) -> OperationHttpRequest: ...
                        def get(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> CutoverJobHttpRequest: ...
                        def list(
                            self,
                            *,
                            parent: str,
                            filter: str = ...,
                            orderBy: str = ...,
                            pageSize: int = ...,
                            pageToken: str = ...,
                            **kwargs: typing.Any
                        ) -> ListCutoverJobsResponseHttpRequest: ...
                        def list_next(
                            self,
                            previous_request: ListCutoverJobsResponseHttpRequest,
                            previous_response: ListCutoverJobsResponse,
                        ) -> ListCutoverJobsResponseHttpRequest | None: ...

                    @typing.type_check_only
                    class ReplicationCyclesResource(googleapiclient.discovery.Resource):
                        def get(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> ReplicationCycleHttpRequest: ...
                        def list(
                            self,
                            *,
                            parent: str,
                            filter: str = ...,
                            orderBy: str = ...,
                            pageSize: int = ...,
                            pageToken: str = ...,
                            **kwargs: typing.Any
                        ) -> ListReplicationCyclesResponseHttpRequest: ...
                        def list_next(
                            self,
                            previous_request: ListReplicationCyclesResponseHttpRequest,
                            previous_response: ListReplicationCyclesResponse,
                        ) -> ListReplicationCyclesResponseHttpRequest | None: ...

                    def create(
                        self,
                        *,
                        parent: str,
                        body: MigratingVm = ...,
                        migratingVmId: str = ...,
                        requestId: str = ...,
                        **kwargs: typing.Any
                    ) -> OperationHttpRequest: ...
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> OperationHttpRequest: ...
                    def finalizeMigration(
                        self,
                        *,
                        migratingVm: str,
                        body: FinalizeMigrationRequest = ...,
                        **kwargs: typing.Any
                    ) -> OperationHttpRequest: ...
                    def get(
                        self,
                        *,
                        name: str,
                        view: typing_extensions.Literal[
                            "MIGRATING_VM_VIEW_UNSPECIFIED",
                            "MIGRATING_VM_VIEW_BASIC",
                            "MIGRATING_VM_VIEW_FULL",
                        ] = ...,
                        **kwargs: typing.Any
                    ) -> MigratingVmHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str = ...,
                        orderBy: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        view: typing_extensions.Literal[
                            "MIGRATING_VM_VIEW_UNSPECIFIED",
                            "MIGRATING_VM_VIEW_BASIC",
                            "MIGRATING_VM_VIEW_FULL",
                        ] = ...,
                        **kwargs: typing.Any
                    ) -> ListMigratingVmsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: ListMigratingVmsResponseHttpRequest,
                        previous_response: ListMigratingVmsResponse,
                    ) -> ListMigratingVmsResponseHttpRequest | None: ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: MigratingVm = ...,
                        requestId: str = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any
                    ) -> OperationHttpRequest: ...
                    def pauseMigration(
                        self,
                        *,
                        migratingVm: str,
                        body: PauseMigrationRequest = ...,
                        **kwargs: typing.Any
                    ) -> OperationHttpRequest: ...
                    def resumeMigration(
                        self,
                        *,
                        migratingVm: str,
                        body: ResumeMigrationRequest = ...,
                        **kwargs: typing.Any
                    ) -> OperationHttpRequest: ...
                    def startMigration(
                        self,
                        *,
                        migratingVm: str,
                        body: StartMigrationRequest = ...,
                        **kwargs: typing.Any
                    ) -> OperationHttpRequest: ...
                    def cloneJobs(self) -> CloneJobsResource: ...
                    def cutoverJobs(self) -> CutoverJobsResource: ...
                    def replicationCycles(self) -> ReplicationCyclesResource: ...

                @typing.type_check_only
                class UtilizationReportsResource(googleapiclient.discovery.Resource):
                    def create(
                        self,
                        *,
                        parent: str,
                        body: UtilizationReport = ...,
                        requestId: str = ...,
                        utilizationReportId: str = ...,
                        **kwargs: typing.Any
                    ) -> OperationHttpRequest: ...
                    def delete(
                        self, *, name: str, requestId: str = ..., **kwargs: typing.Any
                    ) -> OperationHttpRequest: ...
                    def get(
                        self,
                        *,
                        name: str,
                        view: typing_extensions.Literal[
                            "UTILIZATION_REPORT_VIEW_UNSPECIFIED", "BASIC", "FULL"
                        ] = ...,
                        **kwargs: typing.Any
                    ) -> UtilizationReportHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str = ...,
                        orderBy: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        view: typing_extensions.Literal[
                            "UTILIZATION_REPORT_VIEW_UNSPECIFIED", "BASIC", "FULL"
                        ] = ...,
                        **kwargs: typing.Any
                    ) -> ListUtilizationReportsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: ListUtilizationReportsResponseHttpRequest,
                        previous_response: ListUtilizationReportsResponse,
                    ) -> ListUtilizationReportsResponseHttpRequest | None: ...

                def create(
                    self,
                    *,
                    parent: str,
                    body: Source = ...,
                    requestId: str = ...,
                    sourceId: str = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def delete(
                    self, *, name: str, requestId: str = ..., **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def fetchInventory(
                    self,
                    *,
                    source: str,
                    forceRefresh: bool = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> FetchInventoryResponseHttpRequest: ...
                def fetchInventory_next(
                    self,
                    previous_request: FetchInventoryResponseHttpRequest,
                    previous_response: FetchInventoryResponse,
                ) -> FetchInventoryResponseHttpRequest | None: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> SourceHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> ListSourcesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListSourcesResponseHttpRequest,
                    previous_response: ListSourcesResponse,
                ) -> ListSourcesResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: Source = ...,
                    requestId: str = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def datacenterConnectors(self) -> DatacenterConnectorsResource: ...
                def migratingVms(self) -> MigratingVmsResource: ...
                def utilizationReports(self) -> UtilizationReportsResource: ...

            @typing.type_check_only
            class TargetProjectsResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: TargetProject = ...,
                    requestId: str = ...,
                    targetProjectId: str = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def delete(
                    self, *, name: str, requestId: str = ..., **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> TargetProjectHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> ListTargetProjectsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListTargetProjectsResponseHttpRequest,
                    previous_response: ListTargetProjectsResponse,
                ) -> ListTargetProjectsResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: TargetProject = ...,
                    requestId: str = ...,
                    updateMask: str = ...,
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
            def groups(self) -> GroupsResource: ...
            def operations(self) -> OperationsResource: ...
            def sources(self) -> SourcesResource: ...
            def targetProjects(self) -> TargetProjectsResource: ...

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
class CloneJobHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> CloneJob: ...

@typing.type_check_only
class CutoverJobHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> CutoverJob: ...

@typing.type_check_only
class DatacenterConnectorHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> DatacenterConnector: ...

@typing.type_check_only
class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Empty: ...

@typing.type_check_only
class FetchInventoryResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> FetchInventoryResponse: ...

@typing.type_check_only
class GroupHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Group: ...

@typing.type_check_only
class ListCloneJobsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListCloneJobsResponse: ...

@typing.type_check_only
class ListCutoverJobsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListCutoverJobsResponse: ...

@typing.type_check_only
class ListDatacenterConnectorsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListDatacenterConnectorsResponse: ...

@typing.type_check_only
class ListGroupsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListGroupsResponse: ...

@typing.type_check_only
class ListLocationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListLocationsResponse: ...

@typing.type_check_only
class ListMigratingVmsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListMigratingVmsResponse: ...

@typing.type_check_only
class ListOperationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListOperationsResponse: ...

@typing.type_check_only
class ListReplicationCyclesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListReplicationCyclesResponse: ...

@typing.type_check_only
class ListSourcesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListSourcesResponse: ...

@typing.type_check_only
class ListTargetProjectsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListTargetProjectsResponse: ...

@typing.type_check_only
class ListUtilizationReportsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListUtilizationReportsResponse: ...

@typing.type_check_only
class LocationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Location: ...

@typing.type_check_only
class MigratingVmHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> MigratingVm: ...

@typing.type_check_only
class OperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Operation: ...

@typing.type_check_only
class ReplicationCycleHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ReplicationCycle: ...

@typing.type_check_only
class SourceHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Source: ...

@typing.type_check_only
class TargetProjectHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> TargetProject: ...

@typing.type_check_only
class UtilizationReportHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> UtilizationReport: ...
