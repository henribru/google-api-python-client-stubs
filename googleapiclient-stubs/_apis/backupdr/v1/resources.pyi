import collections.abc
import typing

import httplib2
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http

from .schemas import *

_list = list

@typing.type_check_only
class BackupdrResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class ProjectsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class LocationsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class BackupPlanAssociationsResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: BackupPlanAssociation = ...,
                    backupPlanAssociationId: str = ...,
                    requestId: str = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def delete(
                    self, *, name: str, requestId: str = ..., **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> BackupPlanAssociationHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> ListBackupPlanAssociationsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListBackupPlanAssociationsResponseHttpRequest,
                    previous_response: ListBackupPlanAssociationsResponse,
                ) -> ListBackupPlanAssociationsResponseHttpRequest | None: ...
                def triggerBackup(
                    self,
                    *,
                    name: str,
                    body: TriggerBackupRequest = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...

            @typing.type_check_only
            class BackupPlansResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: BackupPlan = ...,
                    backupPlanId: str = ...,
                    requestId: str = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def delete(
                    self, *, name: str, requestId: str = ..., **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> BackupPlanHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> ListBackupPlansResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListBackupPlansResponseHttpRequest,
                    previous_response: ListBackupPlansResponse,
                ) -> ListBackupPlansResponseHttpRequest | None: ...

            @typing.type_check_only
            class BackupVaultsResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class DataSourcesResource(googleapiclient.discovery.Resource):
                    @typing.type_check_only
                    class BackupsResource(googleapiclient.discovery.Resource):
                        def delete(
                            self,
                            *,
                            name: str,
                            requestId: str = ...,
                            **kwargs: typing.Any,
                        ) -> OperationHttpRequest: ...
                        def get(
                            self,
                            *,
                            name: str,
                            view: typing_extensions.Literal[
                                "BACKUP_VIEW_UNSPECIFIED",
                                "BACKUP_VIEW_BASIC",
                                "BACKUP_VIEW_FULL",
                            ] = ...,
                            **kwargs: typing.Any,
                        ) -> BackupHttpRequest: ...
                        def list(
                            self,
                            *,
                            parent: str,
                            filter: str = ...,
                            orderBy: str = ...,
                            pageSize: int = ...,
                            pageToken: str = ...,
                            view: typing_extensions.Literal[
                                "BACKUP_VIEW_UNSPECIFIED",
                                "BACKUP_VIEW_BASIC",
                                "BACKUP_VIEW_FULL",
                            ] = ...,
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
                            requestId: str = ...,
                            updateMask: str = ...,
                            **kwargs: typing.Any,
                        ) -> OperationHttpRequest: ...
                        def restore(
                            self,
                            *,
                            name: str,
                            body: RestoreBackupRequest = ...,
                            **kwargs: typing.Any,
                        ) -> OperationHttpRequest: ...

                    def abandonBackup(
                        self,
                        *,
                        dataSource: str,
                        body: AbandonBackupRequest = ...,
                        **kwargs: typing.Any,
                    ) -> OperationHttpRequest: ...
                    def fetchAccessToken(
                        self,
                        *,
                        name: str,
                        body: FetchAccessTokenRequest = ...,
                        **kwargs: typing.Any,
                    ) -> FetchAccessTokenResponseHttpRequest: ...
                    def finalizeBackup(
                        self,
                        *,
                        dataSource: str,
                        body: FinalizeBackupRequest = ...,
                        **kwargs: typing.Any,
                    ) -> OperationHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> DataSourceHttpRequest: ...
                    def initiateBackup(
                        self,
                        *,
                        dataSource: str,
                        body: InitiateBackupRequest = ...,
                        **kwargs: typing.Any,
                    ) -> InitiateBackupResponseHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str = ...,
                        orderBy: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
                    ) -> ListDataSourcesResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: ListDataSourcesResponseHttpRequest,
                        previous_response: ListDataSourcesResponse,
                    ) -> ListDataSourcesResponseHttpRequest | None: ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: DataSource = ...,
                        allowMissing: bool = ...,
                        requestId: str = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any,
                    ) -> OperationHttpRequest: ...
                    def remove(
                        self,
                        *,
                        name: str,
                        body: RemoveDataSourceRequest = ...,
                        **kwargs: typing.Any,
                    ) -> OperationHttpRequest: ...
                    def setInternalStatus(
                        self,
                        *,
                        dataSource: str,
                        body: SetInternalStatusRequest = ...,
                        **kwargs: typing.Any,
                    ) -> OperationHttpRequest: ...
                    def backups(self) -> BackupsResource: ...

                def create(
                    self,
                    *,
                    parent: str,
                    body: BackupVault = ...,
                    backupVaultId: str = ...,
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
                    ignoreBackupPlanReferences: bool = ...,
                    requestId: str = ...,
                    validateOnly: bool = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def fetchUsable(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> FetchUsableBackupVaultsResponseHttpRequest: ...
                def fetchUsable_next(
                    self,
                    previous_request: FetchUsableBackupVaultsResponseHttpRequest,
                    previous_response: FetchUsableBackupVaultsResponse,
                ) -> FetchUsableBackupVaultsResponseHttpRequest | None: ...
                def get(
                    self,
                    *,
                    name: str,
                    view: typing_extensions.Literal[
                        "BACKUP_VAULT_VIEW_UNSPECIFIED",
                        "BACKUP_VAULT_VIEW_BASIC",
                        "BACKUP_VAULT_VIEW_FULL",
                    ] = ...,
                    **kwargs: typing.Any,
                ) -> BackupVaultHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    view: typing_extensions.Literal[
                        "BACKUP_VAULT_VIEW_UNSPECIFIED",
                        "BACKUP_VAULT_VIEW_BASIC",
                        "BACKUP_VAULT_VIEW_FULL",
                    ] = ...,
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
                    force: bool = ...,
                    requestId: str = ...,
                    updateMask: str = ...,
                    validateOnly: bool = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def testIamPermissions(
                    self,
                    *,
                    resource: str,
                    body: TestIamPermissionsRequest = ...,
                    **kwargs: typing.Any,
                ) -> TestIamPermissionsResponseHttpRequest: ...
                def dataSources(self) -> DataSourcesResource: ...

            @typing.type_check_only
            class ManagementServersResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: ManagementServer = ...,
                    managementServerId: str = ...,
                    requestId: str = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def delete(
                    self, *, name: str, requestId: str = ..., **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> ManagementServerHttpRequest: ...
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
                ) -> ListManagementServersResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListManagementServersResponseHttpRequest,
                    previous_response: ListManagementServersResponse,
                ) -> ListManagementServersResponseHttpRequest | None: ...
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
            class ServiceConfigResource(googleapiclient.discovery.Resource):
                def initialize(
                    self,
                    *,
                    name: str,
                    body: InitializeServiceRequest = ...,
                    **kwargs: typing.Any,
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
                **kwargs: typing.Any,
            ) -> ListLocationsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListLocationsResponseHttpRequest,
                previous_response: ListLocationsResponse,
            ) -> ListLocationsResponseHttpRequest | None: ...
            def backupPlanAssociations(self) -> BackupPlanAssociationsResource: ...
            def backupPlans(self) -> BackupPlansResource: ...
            def backupVaults(self) -> BackupVaultsResource: ...
            def managementServers(self) -> ManagementServersResource: ...
            def operations(self) -> OperationsResource: ...
            def serviceConfig(self) -> ServiceConfigResource: ...

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
class BackupPlanHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> BackupPlan: ...

@typing.type_check_only
class BackupPlanAssociationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> BackupPlanAssociation: ...

@typing.type_check_only
class BackupVaultHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> BackupVault: ...

@typing.type_check_only
class DataSourceHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> DataSource: ...

@typing.type_check_only
class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Empty: ...

@typing.type_check_only
class FetchAccessTokenResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> FetchAccessTokenResponse: ...

@typing.type_check_only
class FetchUsableBackupVaultsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> FetchUsableBackupVaultsResponse: ...

@typing.type_check_only
class InitiateBackupResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> InitiateBackupResponse: ...

@typing.type_check_only
class ListBackupPlanAssociationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListBackupPlanAssociationsResponse: ...

@typing.type_check_only
class ListBackupPlansResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListBackupPlansResponse: ...

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
class ListDataSourcesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListDataSourcesResponse: ...

@typing.type_check_only
class ListLocationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListLocationsResponse: ...

@typing.type_check_only
class ListManagementServersResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListManagementServersResponse: ...

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
class ManagementServerHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ManagementServer: ...

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
class TestIamPermissionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> TestIamPermissionsResponse: ...
