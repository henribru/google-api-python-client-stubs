import collections.abc
import typing

import httplib2
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http

from .schemas import *

_list = list

@typing.type_check_only
class CloudRedisResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class ProjectsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class LocationsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class BackupCollectionsResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class BackupsResource(googleapiclient.discovery.Resource):
                    def delete(
                        self, *, name: str, requestId: str = ..., **kwargs: typing.Any
                    ) -> OperationHttpRequest: ...
                    def export(
                        self,
                        *,
                        name: str,
                        body: ExportBackupRequest = ...,
                        **kwargs: typing.Any,
                    ) -> OperationHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> BackupHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
                    ) -> ListBackupsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: ListBackupsResponseHttpRequest,
                        previous_response: ListBackupsResponse,
                    ) -> ListBackupsResponseHttpRequest | None: ...

                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> BackupCollectionHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> ListBackupCollectionsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListBackupCollectionsResponseHttpRequest,
                    previous_response: ListBackupCollectionsResponse,
                ) -> ListBackupCollectionsResponseHttpRequest | None: ...
                def backups(self) -> BackupsResource: ...

            @typing.type_check_only
            class ClustersResource(googleapiclient.discovery.Resource):
                def backup(
                    self,
                    *,
                    name: str,
                    body: BackupClusterRequest = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def create(
                    self,
                    *,
                    parent: str,
                    body: Cluster = ...,
                    clusterId: str = ...,
                    requestId: str = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def delete(
                    self, *, name: str, requestId: str = ..., **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> ClusterHttpRequest: ...
                def getCertificateAuthority(
                    self, *, name: str, **kwargs: typing.Any
                ) -> CertificateAuthorityHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
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
                    name: str,
                    body: Cluster = ...,
                    requestId: str = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def rescheduleClusterMaintenance(
                    self,
                    *,
                    name: str,
                    body: RescheduleClusterMaintenanceRequest = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...

            @typing.type_check_only
            class InstancesResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: Instance = ...,
                    instanceId: str = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def export(
                    self,
                    *,
                    name: str,
                    body: ExportInstanceRequest = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def failover(
                    self,
                    *,
                    name: str,
                    body: FailoverInstanceRequest = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> InstanceHttpRequest: ...
                def getAuthString(
                    self, *, name: str, **kwargs: typing.Any
                ) -> InstanceAuthStringHttpRequest: ...
                def import_(
                    self,
                    *,
                    name: str,
                    body: ImportInstanceRequest = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
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
                    body: Instance = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def rescheduleMaintenance(
                    self,
                    *,
                    name: str,
                    body: RescheduleMaintenanceRequest = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def upgrade(
                    self,
                    *,
                    name: str,
                    body: UpgradeInstanceRequest = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...

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
                **kwargs: typing.Any,
            ) -> ListLocationsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListLocationsResponseHttpRequest,
                previous_response: ListLocationsResponse,
            ) -> ListLocationsResponseHttpRequest | None: ...
            def backupCollections(self) -> BackupCollectionsResource: ...
            def clusters(self) -> ClustersResource: ...
            def instances(self) -> InstancesResource: ...
            def operations(self) -> OperationsResource: ...

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
class BackupCollectionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> BackupCollection: ...

@typing.type_check_only
class CertificateAuthorityHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> CertificateAuthority: ...

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
class InstanceHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Instance: ...

@typing.type_check_only
class InstanceAuthStringHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> InstanceAuthString: ...

@typing.type_check_only
class ListBackupCollectionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListBackupCollectionsResponse: ...

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
class ListInstancesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListInstancesResponse: ...

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
