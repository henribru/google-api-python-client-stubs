import collections.abc
import typing

import httplib2
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http

from .schemas import *

_list = list

@typing.type_check_only
class BaremetalsolutionResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class ProjectsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class LocationsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class InstancesResource(googleapiclient.discovery.Resource):
                def detachLun(
                    self,
                    *,
                    instance: str,
                    body: DetachLunRequest = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def disableHyperthreading(
                    self,
                    *,
                    name: str,
                    body: DisableHyperthreadingRequest = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def disableInteractiveSerialConsole(
                    self,
                    *,
                    name: str,
                    body: DisableInteractiveSerialConsoleRequest = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def enableHyperthreading(
                    self,
                    *,
                    name: str,
                    body: EnableHyperthreadingRequest = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def enableInteractiveSerialConsole(
                    self,
                    *,
                    name: str,
                    body: EnableInteractiveSerialConsoleRequest = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> InstanceHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> ListInstancesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListInstancesResponseHttpRequest,
                    previous_response: ListInstancesResponse,
                ) -> ListInstancesResponseHttpRequest | None: ...
                def loadAuthInfo(
                    self, *, name: str, **kwargs: typing.Any
                ) -> LoadInstanceAuthInfoResponseHttpRequest: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: Instance = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def reimage(
                    self,
                    *,
                    name: str,
                    body: ReimageInstanceRequest = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def rename(
                    self,
                    *,
                    name: str,
                    body: RenameInstanceRequest = ...,
                    **kwargs: typing.Any,
                ) -> InstanceHttpRequest: ...
                def reset(
                    self,
                    *,
                    name: str,
                    body: ResetInstanceRequest = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def start(
                    self,
                    *,
                    name: str,
                    body: StartInstanceRequest = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def stop(
                    self,
                    *,
                    name: str,
                    body: StopInstanceRequest = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...

            @typing.type_check_only
            class NetworksResource(googleapiclient.discovery.Resource):
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> NetworkHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> ListNetworksResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListNetworksResponseHttpRequest,
                    previous_response: ListNetworksResponse,
                ) -> ListNetworksResponseHttpRequest | None: ...
                def listNetworkUsage(
                    self, *, location: str, **kwargs: typing.Any
                ) -> ListNetworkUsageResponseHttpRequest: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: Network = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def rename(
                    self,
                    *,
                    name: str,
                    body: RenameNetworkRequest = ...,
                    **kwargs: typing.Any,
                ) -> NetworkHttpRequest: ...

            @typing.type_check_only
            class NfsSharesResource(googleapiclient.discovery.Resource):
                def create(
                    self, *, parent: str, body: NfsShare = ..., **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> NfsShareHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> ListNfsSharesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListNfsSharesResponseHttpRequest,
                    previous_response: ListNfsSharesResponse,
                ) -> ListNfsSharesResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: NfsShare = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def rename(
                    self,
                    *,
                    name: str,
                    body: RenameNfsShareRequest = ...,
                    **kwargs: typing.Any,
                ) -> NfsShareHttpRequest: ...

            @typing.type_check_only
            class OperationsResource(googleapiclient.discovery.Resource):
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> OperationHttpRequest: ...

            @typing.type_check_only
            class OsImagesResource(googleapiclient.discovery.Resource):
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> OSImageHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> ListOSImagesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListOSImagesResponseHttpRequest,
                    previous_response: ListOSImagesResponse,
                ) -> ListOSImagesResponseHttpRequest | None: ...

            @typing.type_check_only
            class ProvisioningConfigsResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: ProvisioningConfig = ...,
                    email: str = ...,
                    **kwargs: typing.Any,
                ) -> ProvisioningConfigHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> ProvisioningConfigHttpRequest: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: ProvisioningConfig = ...,
                    email: str = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> ProvisioningConfigHttpRequest: ...
                def submit(
                    self,
                    *,
                    parent: str,
                    body: SubmitProvisioningConfigRequest = ...,
                    **kwargs: typing.Any,
                ) -> SubmitProvisioningConfigResponseHttpRequest: ...

            @typing.type_check_only
            class ProvisioningQuotasResource(googleapiclient.discovery.Resource):
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> ListProvisioningQuotasResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListProvisioningQuotasResponseHttpRequest,
                    previous_response: ListProvisioningQuotasResponse,
                ) -> ListProvisioningQuotasResponseHttpRequest | None: ...

            @typing.type_check_only
            class SshKeysResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: SSHKey = ...,
                    sshKeyId: str = ...,
                    **kwargs: typing.Any,
                ) -> SSHKeyHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> ListSSHKeysResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListSSHKeysResponseHttpRequest,
                    previous_response: ListSSHKeysResponse,
                ) -> ListSSHKeysResponseHttpRequest | None: ...

            @typing.type_check_only
            class VolumesResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class LunsResource(googleapiclient.discovery.Resource):
                    def evict(
                        self,
                        *,
                        name: str,
                        body: EvictLunRequest = ...,
                        **kwargs: typing.Any,
                    ) -> OperationHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> LunHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
                    ) -> ListLunsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: ListLunsResponseHttpRequest,
                        previous_response: ListLunsResponse,
                    ) -> ListLunsResponseHttpRequest | None: ...

                @typing.type_check_only
                class SnapshotsResource(googleapiclient.discovery.Resource):
                    def create(
                        self,
                        *,
                        parent: str,
                        body: VolumeSnapshot = ...,
                        **kwargs: typing.Any,
                    ) -> VolumeSnapshotHttpRequest: ...
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> EmptyHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> VolumeSnapshotHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
                    ) -> ListVolumeSnapshotsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: ListVolumeSnapshotsResponseHttpRequest,
                        previous_response: ListVolumeSnapshotsResponse,
                    ) -> ListVolumeSnapshotsResponseHttpRequest | None: ...
                    def restoreVolumeSnapshot(
                        self,
                        *,
                        volumeSnapshot: str,
                        body: RestoreVolumeSnapshotRequest = ...,
                        **kwargs: typing.Any,
                    ) -> OperationHttpRequest: ...

                def evict(
                    self,
                    *,
                    name: str,
                    body: EvictVolumeRequest = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> VolumeHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
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
                def rename(
                    self,
                    *,
                    name: str,
                    body: RenameVolumeRequest = ...,
                    **kwargs: typing.Any,
                ) -> VolumeHttpRequest: ...
                def resize(
                    self,
                    *,
                    volume: str,
                    body: ResizeVolumeRequest = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def luns(self) -> LunsResource: ...
                def snapshots(self) -> SnapshotsResource: ...

            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> LocationHttpRequest: ...
            def list(
                self,
                *,
                name: str,
                extraLocationTypes: str | _list[str] = ...,
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
            def instances(self) -> InstancesResource: ...
            def networks(self) -> NetworksResource: ...
            def nfsShares(self) -> NfsSharesResource: ...
            def operations(self) -> OperationsResource: ...
            def osImages(self) -> OsImagesResource: ...
            def provisioningConfigs(self) -> ProvisioningConfigsResource: ...
            def provisioningQuotas(self) -> ProvisioningQuotasResource: ...
            def sshKeys(self) -> SshKeysResource: ...
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
class ListLunsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListLunsResponse: ...

@typing.type_check_only
class ListNetworkUsageResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListNetworkUsageResponse: ...

@typing.type_check_only
class ListNetworksResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListNetworksResponse: ...

@typing.type_check_only
class ListNfsSharesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListNfsSharesResponse: ...

@typing.type_check_only
class ListOSImagesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListOSImagesResponse: ...

@typing.type_check_only
class ListProvisioningQuotasResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListProvisioningQuotasResponse: ...

@typing.type_check_only
class ListSSHKeysResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListSSHKeysResponse: ...

@typing.type_check_only
class ListVolumeSnapshotsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListVolumeSnapshotsResponse: ...

@typing.type_check_only
class ListVolumesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListVolumesResponse: ...

@typing.type_check_only
class LoadInstanceAuthInfoResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> LoadInstanceAuthInfoResponse: ...

@typing.type_check_only
class LocationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Location: ...

@typing.type_check_only
class LunHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Lun: ...

@typing.type_check_only
class NetworkHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Network: ...

@typing.type_check_only
class NfsShareHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> NfsShare: ...

@typing.type_check_only
class OSImageHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> OSImage: ...

@typing.type_check_only
class OperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Operation: ...

@typing.type_check_only
class ProvisioningConfigHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ProvisioningConfig: ...

@typing.type_check_only
class SSHKeyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> SSHKey: ...

@typing.type_check_only
class SubmitProvisioningConfigResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> SubmitProvisioningConfigResponse: ...

@typing.type_check_only
class VolumeHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Volume: ...

@typing.type_check_only
class VolumeSnapshotHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> VolumeSnapshot: ...
