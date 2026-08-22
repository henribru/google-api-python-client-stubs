import collections.abc
import typing

import httplib2

import googleapiclient.discovery
import googleapiclient.http

from .schemas import *

_list = list

@typing.type_check_only
class CloudAlloyDBAdminResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class ProjectsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class LocationsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class BackupsResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: Backup,
                    backupId: str | None = ...,
                    requestId: str | None = ...,
                    validateOnly: bool | None = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def delete(
                    self,
                    *,
                    name: str,
                    etag: str | None = ...,
                    requestId: str | None = ...,
                    validateOnly: bool | None = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def get(
                    self,
                    *,
                    name: str,
                    view: typing.Literal[
                        "BACKUP_VIEW_UNSPECIFIED",
                        "BACKUP_VIEW_BASIC",
                        "BACKUP_VIEW_CLUSTER_DELETED",
                    ]
                    | None = ...,
                    **kwargs: typing.Any,
                ) -> BackupHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str | None = ...,
                    orderBy: str | None = ...,
                    pageSize: int | None = ...,
                    pageToken: str | None = ...,
                    view: typing.Literal[
                        "BACKUP_VIEW_UNSPECIFIED",
                        "BACKUP_VIEW_BASIC",
                        "BACKUP_VIEW_CLUSTER_DELETED",
                    ]
                    | None = ...,
                    **kwargs: typing.Any,
                ) -> ListBackupsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListBackupsResponseHttpRequest,
                    previous_response: ListBackupsResponse,
                ) -> ListBackupsResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: Backup,
                    allowMissing: bool | None = ...,
                    requestId: str | None = ...,
                    updateMask: str | None = ...,
                    validateOnly: bool | None = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...

            @typing.type_check_only
            class ClustersResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class InstancesResource(googleapiclient.discovery.Resource):
                    def create(
                        self,
                        *,
                        parent: str,
                        body: Instance,
                        instanceId: str | None = ...,
                        requestId: str | None = ...,
                        validateOnly: bool | None = ...,
                        **kwargs: typing.Any,
                    ) -> OperationHttpRequest: ...
                    def createsecondary(
                        self,
                        *,
                        parent: str,
                        body: Instance,
                        instanceId: str | None = ...,
                        requestId: str | None = ...,
                        validateOnly: bool | None = ...,
                        **kwargs: typing.Any,
                    ) -> OperationHttpRequest: ...
                    def delete(
                        self,
                        *,
                        name: str,
                        etag: str | None = ...,
                        requestId: str | None = ...,
                        validateOnly: bool | None = ...,
                        **kwargs: typing.Any,
                    ) -> OperationHttpRequest: ...
                    def failover(
                        self,
                        *,
                        name: str,
                        body: FailoverInstanceRequest,
                        **kwargs: typing.Any,
                    ) -> OperationHttpRequest: ...
                    def get(
                        self,
                        *,
                        name: str,
                        view: typing.Literal[
                            "INSTANCE_VIEW_UNSPECIFIED",
                            "INSTANCE_VIEW_BASIC",
                            "INSTANCE_VIEW_FULL",
                        ]
                        | None = ...,
                        **kwargs: typing.Any,
                    ) -> InstanceHttpRequest: ...
                    def getConnectionInfo(
                        self,
                        *,
                        parent: str,
                        requestId: str | None = ...,
                        **kwargs: typing.Any,
                    ) -> ConnectionInfoHttpRequest: ...
                    def injectFault(
                        self,
                        *,
                        name: str,
                        body: InjectFaultRequest,
                        **kwargs: typing.Any,
                    ) -> OperationHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str | None = ...,
                        orderBy: str | None = ...,
                        pageSize: int | None = ...,
                        pageToken: str | None = ...,
                        **kwargs: typing.Any,
                    ) -> ListInstancesResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: ListInstancesResponseHttpRequest,
                        previous_response: ListInstancesResponse,
                    ) -> ListInstancesResponseHttpRequest | None: ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: Instance,
                        allowMissing: bool | None = ...,
                        requestId: str | None = ...,
                        updateMask: str | None = ...,
                        validateOnly: bool | None = ...,
                        **kwargs: typing.Any,
                    ) -> OperationHttpRequest: ...
                    def restart(
                        self,
                        *,
                        name: str,
                        body: RestartInstanceRequest,
                        **kwargs: typing.Any,
                    ) -> OperationHttpRequest: ...

                @typing.type_check_only
                class UsersResource(googleapiclient.discovery.Resource):
                    def create(
                        self,
                        *,
                        parent: str,
                        body: User,
                        requestId: str | None = ...,
                        userId: str | None = ...,
                        validateOnly: bool | None = ...,
                        **kwargs: typing.Any,
                    ) -> UserHttpRequest: ...
                    def delete(
                        self,
                        *,
                        name: str,
                        requestId: str | None = ...,
                        validateOnly: bool | None = ...,
                        **kwargs: typing.Any,
                    ) -> EmptyHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> UserHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str | None = ...,
                        orderBy: str | None = ...,
                        pageSize: int | None = ...,
                        pageToken: str | None = ...,
                        **kwargs: typing.Any,
                    ) -> ListUsersResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: ListUsersResponseHttpRequest,
                        previous_response: ListUsersResponse,
                    ) -> ListUsersResponseHttpRequest | None: ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: User,
                        allowMissing: bool | None = ...,
                        requestId: str | None = ...,
                        updateMask: str | None = ...,
                        validateOnly: bool | None = ...,
                        **kwargs: typing.Any,
                    ) -> UserHttpRequest: ...

                def create(
                    self,
                    *,
                    parent: str,
                    body: Cluster,
                    clusterId: str | None = ...,
                    requestId: str | None = ...,
                    validateOnly: bool | None = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def createsecondary(
                    self,
                    *,
                    parent: str,
                    body: Cluster,
                    clusterId: str | None = ...,
                    requestId: str | None = ...,
                    validateOnly: bool | None = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def delete(
                    self,
                    *,
                    name: str,
                    etag: str | None = ...,
                    force: bool | None = ...,
                    requestId: str | None = ...,
                    validateOnly: bool | None = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def export(
                    self, *, name: str, body: ExportClusterRequest, **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def get(
                    self,
                    *,
                    name: str,
                    view: typing.Literal[
                        "CLUSTER_VIEW_UNSPECIFIED",
                        "CLUSTER_VIEW_BASIC",
                        "CLUSTER_VIEW_CONTINUOUS_BACKUP",
                    ]
                    | None = ...,
                    **kwargs: typing.Any,
                ) -> ClusterHttpRequest: ...
                def import_(
                    self, *, name: str, body: ImportClusterRequest, **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str | None = ...,
                    orderBy: str | None = ...,
                    pageSize: int | None = ...,
                    pageToken: str | None = ...,
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
                    name: str,
                    body: Cluster,
                    allowMissing: bool | None = ...,
                    requestId: str | None = ...,
                    updateMask: str | None = ...,
                    validateOnly: bool | None = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def promote(
                    self,
                    *,
                    name: str,
                    body: PromoteClusterRequest,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def restore(
                    self,
                    *,
                    parent: str,
                    body: RestoreClusterRequest,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def restoreFromCloudSQL(
                    self,
                    *,
                    parent: str,
                    body: RestoreFromCloudSQLRequest,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def switchover(
                    self,
                    *,
                    name: str,
                    body: SwitchoverClusterRequest,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def upgrade(
                    self,
                    *,
                    name: str,
                    body: UpgradeClusterRequest,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def instances(self) -> InstancesResource: ...
                def users(self) -> UsersResource: ...

            @typing.type_check_only
            class EndpointsResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: Endpoint,
                    endpointId: str | None = ...,
                    requestId: str | None = ...,
                    validateOnly: bool | None = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def delete(
                    self,
                    *,
                    name: str,
                    etag: str | None = ...,
                    requestId: str | None = ...,
                    validateOnly: bool | None = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> EndpointHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str | None = ...,
                    orderBy: str | None = ...,
                    pageSize: int | None = ...,
                    pageToken: str | None = ...,
                    **kwargs: typing.Any,
                ) -> ListEndpointsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListEndpointsResponseHttpRequest,
                    previous_response: ListEndpointsResponse,
                ) -> ListEndpointsResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: Endpoint,
                    allowMissing: bool | None = ...,
                    requestId: str | None = ...,
                    updateMask: str | None = ...,
                    validateOnly: bool | None = ...,
                    **kwargs: typing.Any,
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
            class SupportedDatabaseFlagsResource(googleapiclient.discovery.Resource):
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int | None = ...,
                    pageToken: str | None = ...,
                    scope: typing.Literal[
                        "SCOPE_UNSPECIFIED", "DATABASE", "CONNECTION_POOL"
                    ]
                    | None = ...,
                    **kwargs: typing.Any,
                ) -> ListSupportedDatabaseFlagsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListSupportedDatabaseFlagsResponseHttpRequest,
                    previous_response: ListSupportedDatabaseFlagsResponse,
                ) -> ListSupportedDatabaseFlagsResponseHttpRequest | None: ...

            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleCloudLocationLocationHttpRequest: ...
            def list(
                self,
                *,
                name: str,
                extraLocationTypes: str | _list[str] | None = ...,
                filter: str | None = ...,
                pageSize: int | None = ...,
                pageToken: str | None = ...,
                **kwargs: typing.Any,
            ) -> GoogleCloudLocationListLocationsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: GoogleCloudLocationListLocationsResponseHttpRequest,
                previous_response: GoogleCloudLocationListLocationsResponse,
            ) -> GoogleCloudLocationListLocationsResponseHttpRequest | None: ...
            def backups(self) -> BackupsResource: ...
            def clusters(self) -> ClustersResource: ...
            def endpoints(self) -> EndpointsResource: ...
            def operations(self) -> OperationsResource: ...
            def supportedDatabaseFlags(self) -> SupportedDatabaseFlagsResource: ...

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
class BackupHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Backup: ...

@typing.type_check_only
class ClusterHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Cluster: ...

@typing.type_check_only
class ConnectionInfoHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ConnectionInfo: ...

@typing.type_check_only
class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Empty: ...

@typing.type_check_only
class EndpointHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Endpoint: ...

@typing.type_check_only
class GoogleCloudLocationListLocationsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudLocationListLocationsResponse: ...

@typing.type_check_only
class GoogleCloudLocationLocationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudLocationLocation: ...

@typing.type_check_only
class InstanceHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Instance: ...

@typing.type_check_only
class ListBackupsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListBackupsResponse: ...

@typing.type_check_only
class ListClustersResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListClustersResponse: ...

@typing.type_check_only
class ListEndpointsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListEndpointsResponse: ...

@typing.type_check_only
class ListInstancesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListInstancesResponse: ...

@typing.type_check_only
class ListOperationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListOperationsResponse: ...

@typing.type_check_only
class ListSupportedDatabaseFlagsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListSupportedDatabaseFlagsResponse: ...

@typing.type_check_only
class ListUsersResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListUsersResponse: ...

@typing.type_check_only
class OperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Operation: ...

@typing.type_check_only
class UserHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> User: ...
