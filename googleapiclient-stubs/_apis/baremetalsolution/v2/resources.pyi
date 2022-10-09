import collections.abc
import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

_list = list

@typing.type_check_only
class BaremetalsolutionResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class ProjectsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class LocationsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class InstanceProvisioningSettingsResource(
                googleapiclient.discovery.Resource
            ):
                def fetch(
                    self, *, location: str, **kwargs: typing.Any
                ) -> FetchInstanceProvisioningSettingsResponseHttpRequest: ...

            @typing.type_check_only
            class InstancesResource(googleapiclient.discovery.Resource):
                def create(
                    self, *, parent: str, body: Instance = ..., **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def detachLun(
                    self,
                    *,
                    instance: str,
                    body: DetachLunRequest = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def disableInteractiveSerialConsole(
                    self,
                    *,
                    name: str,
                    body: DisableInteractiveSerialConsoleRequest = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def enableInteractiveSerialConsole(
                    self,
                    *,
                    name: str,
                    body: EnableInteractiveSerialConsoleRequest = ...,
                    **kwargs: typing.Any
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
                    **kwargs: typing.Any
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
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def reset(
                    self,
                    *,
                    name: str,
                    body: ResetInstanceRequest = ...,
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
                    **kwargs: typing.Any
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
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...

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
                    **kwargs: typing.Any
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
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...

            @typing.type_check_only
            class OperationsResource(googleapiclient.discovery.Resource):
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> OperationHttpRequest: ...

            @typing.type_check_only
            class ProvisioningConfigsResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: ProvisioningConfig = ...,
                    email: str = ...,
                    **kwargs: typing.Any
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
                    **kwargs: typing.Any
                ) -> ProvisioningConfigHttpRequest: ...
                def submit(
                    self,
                    *,
                    parent: str,
                    body: SubmitProvisioningConfigRequest = ...,
                    **kwargs: typing.Any
                ) -> SubmitProvisioningConfigResponseHttpRequest: ...

            @typing.type_check_only
            class ProvisioningQuotasResource(googleapiclient.discovery.Resource):
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
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
                    **kwargs: typing.Any
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
                    **kwargs: typing.Any
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
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> LunHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any
                    ) -> ListLunsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: ListLunsResponseHttpRequest,
                        previous_response: ListLunsResponse,
                    ) -> ListLunsResponseHttpRequest | None: ...

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
                    **kwargs: typing.Any
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
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def resize(
                    self,
                    *,
                    volume: str,
                    body: ResizeVolumeRequest = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def luns(self) -> LunsResource: ...

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
            def instanceProvisioningSettings(
                self,
            ) -> InstanceProvisioningSettingsResource: ...
            def instances(self) -> InstancesResource: ...
            def networks(self) -> NetworksResource: ...
            def nfsShares(self) -> NfsSharesResource: ...
            def operations(self) -> OperationsResource: ...
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
class FetchInstanceProvisioningSettingsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> FetchInstanceProvisioningSettingsResponse: ...

@typing.type_check_only
class InstanceHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Instance: ...

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
class ListLunsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListLunsResponse: ...

@typing.type_check_only
class ListNetworkUsageResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListNetworkUsageResponse: ...

@typing.type_check_only
class ListNetworksResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListNetworksResponse: ...

@typing.type_check_only
class ListNfsSharesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListNfsSharesResponse: ...

@typing.type_check_only
class ListProvisioningQuotasResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListProvisioningQuotasResponse: ...

@typing.type_check_only
class ListSSHKeysResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListSSHKeysResponse: ...

@typing.type_check_only
class ListVolumesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListVolumesResponse: ...

@typing.type_check_only
class LocationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Location: ...

@typing.type_check_only
class LunHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Lun: ...

@typing.type_check_only
class NetworkHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Network: ...

@typing.type_check_only
class NfsShareHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> NfsShare: ...

@typing.type_check_only
class OperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Operation: ...

@typing.type_check_only
class ProvisioningConfigHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ProvisioningConfig: ...

@typing.type_check_only
class SSHKeyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> SSHKey: ...

@typing.type_check_only
class SubmitProvisioningConfigResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> SubmitProvisioningConfigResponse: ...

@typing.type_check_only
class VolumeHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Volume: ...
