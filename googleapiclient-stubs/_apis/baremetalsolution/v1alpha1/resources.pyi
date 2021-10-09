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
            class InstancesResource(googleapiclient.discovery.Resource):
                def disableInteractiveSerialConsole(
                    self,
                    *,
                    instance: str,
                    body: DisableInteractiveSerialConsoleRequest = ...,
                    **kwargs: typing.Any
                ) -> DisableInteractiveSerialConsoleResponseHttpRequest: ...
                def enableInteractiveSerialConsole(
                    self,
                    *,
                    instance: str,
                    body: EnableInteractiveSerialConsoleRequest = ...,
                    **kwargs: typing.Any
                ) -> EnableInteractiveSerialConsoleResponseHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> InstanceHttpRequest: ...
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
                def readSerialPortOutput(
                    self, *, instance: str, startByte: str = ..., **kwargs: typing.Any
                ) -> SerialPortOutputHttpRequest: ...
                def resetInstance(
                    self,
                    *,
                    instance: str,
                    body: ResetInstanceRequest = ...,
                    **kwargs: typing.Any
                ) -> ResetInstanceResponseHttpRequest: ...
            @typing.type_check_only
            class LunsResource(googleapiclient.discovery.Resource):
                def get(self, *, name: str, **kwargs: typing.Any) -> LunHttpRequest: ...
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
            @typing.type_check_only
            class VolumesResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class SnapshotsResource(googleapiclient.discovery.Resource):
                    def create(
                        self,
                        *,
                        parent: str,
                        body: VolumeSnapshot = ...,
                        **kwargs: typing.Any
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
                        **kwargs: typing.Any
                    ) -> ListVolumeSnapshotsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: ListVolumeSnapshotsResponseHttpRequest,
                        previous_response: ListVolumeSnapshotsResponse,
                    ) -> ListVolumeSnapshotsResponseHttpRequest | None: ...
                    def restore(
                        self,
                        *,
                        name: str,
                        body: RestoreVolumeSnapshotRequest = ...,
                        **kwargs: typing.Any
                    ) -> EmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> VolumeHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
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
                ) -> VolumeHttpRequest: ...
                def setVolumeSnapshotSchedulePolicy(
                    self,
                    *,
                    volume: str,
                    body: SetVolumeSnapshotSchedulePolicyRequest = ...,
                    **kwargs: typing.Any
                ) -> SetVolumeSnapshotSchedulePolicyResponseHttpRequest: ...
                def snapshots(self) -> SnapshotsResource: ...
            def submitProvisioningConfig(
                self,
                *,
                project: str,
                location: str,
                body: SubmitProvisioningConfigRequest = ...,
                **kwargs: typing.Any
            ) -> ProvisioningConfigHttpRequest: ...
            def instances(self) -> InstancesResource: ...
            def luns(self) -> LunsResource: ...
            def volumes(self) -> VolumesResource: ...
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
        class SnapshotSchedulePoliciesResource(googleapiclient.discovery.Resource):
            def create(
                self,
                *,
                parent: str,
                body: SnapshotSchedulePolicy = ...,
                **kwargs: typing.Any
            ) -> SnapshotSchedulePolicyHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> SnapshotSchedulePolicyHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> ListSnapshotSchedulePoliciesResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListSnapshotSchedulePoliciesResponseHttpRequest,
                previous_response: ListSnapshotSchedulePoliciesResponse,
            ) -> ListSnapshotSchedulePoliciesResponseHttpRequest | None: ...
            def patch(
                self,
                *,
                name: str,
                body: SnapshotSchedulePolicy = ...,
                updateMask: str = ...,
                **kwargs: typing.Any
            ) -> SnapshotSchedulePolicyHttpRequest: ...
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
        def locations(self) -> LocationsResource: ...
        def provisioningQuotas(self) -> ProvisioningQuotasResource: ...
        def snapshotSchedulePolicies(self) -> SnapshotSchedulePoliciesResource: ...
        def sshKeys(self) -> SshKeysResource: ...
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
class DisableInteractiveSerialConsoleResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> DisableInteractiveSerialConsoleResponse: ...

@typing.type_check_only
class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Empty: ...

@typing.type_check_only
class EnableInteractiveSerialConsoleResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> EnableInteractiveSerialConsoleResponse: ...

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
class ListLunsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListLunsResponse: ...

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
class ListSnapshotSchedulePoliciesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListSnapshotSchedulePoliciesResponse: ...

@typing.type_check_only
class ListVolumeSnapshotsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListVolumeSnapshotsResponse: ...

@typing.type_check_only
class ListVolumesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListVolumesResponse: ...

@typing.type_check_only
class LunHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Lun: ...

@typing.type_check_only
class ProvisioningConfigHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ProvisioningConfig: ...

@typing.type_check_only
class ResetInstanceResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ResetInstanceResponse: ...

@typing.type_check_only
class SSHKeyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> SSHKey: ...

@typing.type_check_only
class SerialPortOutputHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> SerialPortOutput: ...

@typing.type_check_only
class SetVolumeSnapshotSchedulePolicyResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> SetVolumeSnapshotSchedulePolicyResponse: ...

@typing.type_check_only
class SnapshotSchedulePolicyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> SnapshotSchedulePolicy: ...

@typing.type_check_only
class VolumeHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Volume: ...

@typing.type_check_only
class VolumeSnapshotHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> VolumeSnapshot: ...
