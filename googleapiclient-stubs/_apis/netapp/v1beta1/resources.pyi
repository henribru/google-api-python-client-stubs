import collections.abc
import typing

import httplib2
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http

from .schemas import *

_list = list

@typing.type_check_only
class NetAppFilesResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class ProjectsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class LocationsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class ActiveDirectoriesResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: ActiveDirectory = ...,
                    activeDirectoryId: str = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> ActiveDirectoryHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> ListActiveDirectoriesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListActiveDirectoriesResponseHttpRequest,
                    previous_response: ListActiveDirectoriesResponse,
                ) -> ListActiveDirectoriesResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: ActiveDirectory = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...

            @typing.type_check_only
            class BackupPoliciesResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: BackupPolicy = ...,
                    backupPolicyId: str = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> BackupPolicyHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> ListBackupPoliciesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListBackupPoliciesResponseHttpRequest,
                    previous_response: ListBackupPoliciesResponse,
                ) -> ListBackupPoliciesResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: BackupPolicy = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...

            @typing.type_check_only
            class BackupVaultsResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class BackupsResource(googleapiclient.discovery.Resource):
                    def create(
                        self,
                        *,
                        parent: str,
                        body: Backup = ...,
                        backupId: str = ...,
                        **kwargs: typing.Any,
                    ) -> OperationHttpRequest: ...
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> OperationHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> BackupHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str = ...,
                        orderBy: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
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
                        body: Backup = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any,
                    ) -> OperationHttpRequest: ...

                def create(
                    self,
                    *,
                    parent: str,
                    body: BackupVault = ...,
                    backupVaultId: str = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> BackupVaultHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> ListBackupVaultsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListBackupVaultsResponseHttpRequest,
                    previous_response: ListBackupVaultsResponse,
                ) -> ListBackupVaultsResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: BackupVault = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def backups(self) -> BackupsResource: ...

            @typing.type_check_only
            class KmsConfigsResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: KmsConfig = ...,
                    kmsConfigId: str = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def encrypt(
                    self,
                    *,
                    name: str,
                    body: EncryptVolumesRequest = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> KmsConfigHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> ListKmsConfigsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListKmsConfigsResponseHttpRequest,
                    previous_response: ListKmsConfigsResponse,
                ) -> ListKmsConfigsResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: KmsConfig = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def verify(
                    self,
                    *,
                    name: str,
                    body: VerifyKmsConfigRequest = ...,
                    **kwargs: typing.Any,
                ) -> VerifyKmsConfigResponseHttpRequest: ...

            @typing.type_check_only
            class OperationsResource(googleapiclient.discovery.Resource):
                def cancel(
                    self,
                    *,
                    name: str,
                    body: CancelOperationRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleProtobufEmptyHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleProtobufEmptyHttpRequest: ...
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
            class StoragePoolsResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: StoragePool = ...,
                    storagePoolId: str = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> StoragePoolHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> ListStoragePoolsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListStoragePoolsResponseHttpRequest,
                    previous_response: ListStoragePoolsResponse,
                ) -> ListStoragePoolsResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: StoragePool = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def switch(
                    self,
                    *,
                    name: str,
                    body: SwitchActiveReplicaZoneRequest = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def validateDirectoryService(
                    self,
                    *,
                    name: str,
                    body: ValidateDirectoryServiceRequest = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...

            @typing.type_check_only
            class VolumesResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class ReplicationsResource(googleapiclient.discovery.Resource):
                    def create(
                        self,
                        *,
                        parent: str,
                        body: Replication = ...,
                        replicationId: str = ...,
                        **kwargs: typing.Any,
                    ) -> OperationHttpRequest: ...
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> OperationHttpRequest: ...
                    def establishPeering(
                        self,
                        *,
                        name: str,
                        body: EstablishPeeringRequest = ...,
                        **kwargs: typing.Any,
                    ) -> OperationHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> ReplicationHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str = ...,
                        orderBy: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
                    ) -> ListReplicationsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: ListReplicationsResponseHttpRequest,
                        previous_response: ListReplicationsResponse,
                    ) -> ListReplicationsResponseHttpRequest | None: ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: Replication = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any,
                    ) -> OperationHttpRequest: ...
                    def resume(
                        self,
                        *,
                        name: str,
                        body: ResumeReplicationRequest = ...,
                        **kwargs: typing.Any,
                    ) -> OperationHttpRequest: ...
                    def reverseDirection(
                        self,
                        *,
                        name: str,
                        body: ReverseReplicationDirectionRequest = ...,
                        **kwargs: typing.Any,
                    ) -> OperationHttpRequest: ...
                    def stop(
                        self,
                        *,
                        name: str,
                        body: StopReplicationRequest = ...,
                        **kwargs: typing.Any,
                    ) -> OperationHttpRequest: ...
                    def sync(
                        self,
                        *,
                        name: str,
                        body: SyncReplicationRequest = ...,
                        **kwargs: typing.Any,
                    ) -> OperationHttpRequest: ...

                @typing.type_check_only
                class SnapshotsResource(googleapiclient.discovery.Resource):
                    def create(
                        self,
                        *,
                        parent: str,
                        body: Snapshot = ...,
                        snapshotId: str = ...,
                        **kwargs: typing.Any,
                    ) -> OperationHttpRequest: ...
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> OperationHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> SnapshotHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str = ...,
                        orderBy: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
                    ) -> ListSnapshotsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: ListSnapshotsResponseHttpRequest,
                        previous_response: ListSnapshotsResponse,
                    ) -> ListSnapshotsResponseHttpRequest | None: ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: Snapshot = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any,
                    ) -> OperationHttpRequest: ...

                def create(
                    self,
                    *,
                    parent: str,
                    body: Volume = ...,
                    volumeId: str = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def delete(
                    self, *, name: str, force: bool = ..., **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> VolumeHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> ListVolumesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListVolumesResponseHttpRequest,
                    previous_response: ListVolumesResponse,
                ) -> ListVolumesResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: Volume = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def revert(
                    self,
                    *,
                    name: str,
                    body: RevertVolumeRequest = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def replications(self) -> ReplicationsResource: ...
                def snapshots(self) -> SnapshotsResource: ...

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
            def activeDirectories(self) -> ActiveDirectoriesResource: ...
            def backupPolicies(self) -> BackupPoliciesResource: ...
            def backupVaults(self) -> BackupVaultsResource: ...
            def kmsConfigs(self) -> KmsConfigsResource: ...
            def operations(self) -> OperationsResource: ...
            def storagePools(self) -> StoragePoolsResource: ...
            def volumes(self) -> VolumesResource: ...

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
class ActiveDirectoryHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ActiveDirectory: ...

@typing.type_check_only
class BackupHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Backup: ...

@typing.type_check_only
class BackupPolicyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> BackupPolicy: ...

@typing.type_check_only
class BackupVaultHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> BackupVault: ...

@typing.type_check_only
class GoogleProtobufEmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleProtobufEmpty: ...

@typing.type_check_only
class KmsConfigHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> KmsConfig: ...

@typing.type_check_only
class ListActiveDirectoriesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListActiveDirectoriesResponse: ...

@typing.type_check_only
class ListBackupPoliciesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListBackupPoliciesResponse: ...

@typing.type_check_only
class ListBackupVaultsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListBackupVaultsResponse: ...

@typing.type_check_only
class ListBackupsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListBackupsResponse: ...

@typing.type_check_only
class ListKmsConfigsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListKmsConfigsResponse: ...

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
class ListReplicationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListReplicationsResponse: ...

@typing.type_check_only
class ListSnapshotsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListSnapshotsResponse: ...

@typing.type_check_only
class ListStoragePoolsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListStoragePoolsResponse: ...

@typing.type_check_only
class ListVolumesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListVolumesResponse: ...

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
class ReplicationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Replication: ...

@typing.type_check_only
class SnapshotHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Snapshot: ...

@typing.type_check_only
class StoragePoolHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> StoragePool: ...

@typing.type_check_only
class VerifyKmsConfigResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> VerifyKmsConfigResponse: ...

@typing.type_check_only
class VolumeHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Volume: ...
