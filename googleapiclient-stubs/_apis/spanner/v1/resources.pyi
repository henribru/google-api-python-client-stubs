import collections.abc
import typing

import httplib2
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http

from .schemas import *

_list = list

@typing.type_check_only
class SpannerResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class ProjectsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class InstanceConfigOperationsResource(googleapiclient.discovery.Resource):
            def list(
                self,
                *,
                parent: str,
                filter: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any,
            ) -> ListInstanceConfigOperationsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListInstanceConfigOperationsResponseHttpRequest,
                previous_response: ListInstanceConfigOperationsResponse,
            ) -> ListInstanceConfigOperationsResponseHttpRequest | None: ...

        @typing.type_check_only
        class InstanceConfigsResource(googleapiclient.discovery.Resource):
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

            @typing.type_check_only
            class SsdCachesResource(googleapiclient.discovery.Resource):
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

                def operations(self) -> OperationsResource: ...

            def create(
                self,
                *,
                parent: str,
                body: CreateInstanceConfigRequest = ...,
                **kwargs: typing.Any,
            ) -> OperationHttpRequest: ...
            def delete(
                self,
                *,
                name: str,
                etag: str = ...,
                validateOnly: bool = ...,
                **kwargs: typing.Any,
            ) -> EmptyHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> InstanceConfigHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any,
            ) -> ListInstanceConfigsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListInstanceConfigsResponseHttpRequest,
                previous_response: ListInstanceConfigsResponse,
            ) -> ListInstanceConfigsResponseHttpRequest | None: ...
            def patch(
                self,
                *,
                name: str,
                body: UpdateInstanceConfigRequest = ...,
                **kwargs: typing.Any,
            ) -> OperationHttpRequest: ...
            def operations(self) -> OperationsResource: ...
            def ssdCaches(self) -> SsdCachesResource: ...

        @typing.type_check_only
        class InstancesResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class BackupOperationsResource(googleapiclient.discovery.Resource):
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> ListBackupOperationsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListBackupOperationsResponseHttpRequest,
                    previous_response: ListBackupOperationsResponse,
                ) -> ListBackupOperationsResponseHttpRequest | None: ...

            @typing.type_check_only
            class BackupsResource(googleapiclient.discovery.Resource):
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

                def copy(
                    self,
                    *,
                    parent: str,
                    body: CopyBackupRequest = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def create(
                    self,
                    *,
                    parent: str,
                    body: Backup = ...,
                    backupId: str = ...,
                    encryptionConfig_encryptionType: typing_extensions.Literal[
                        "ENCRYPTION_TYPE_UNSPECIFIED",
                        "USE_DATABASE_ENCRYPTION",
                        "GOOGLE_DEFAULT_ENCRYPTION",
                        "CUSTOMER_MANAGED_ENCRYPTION",
                    ] = ...,
                    encryptionConfig_kmsKeyName: str = ...,
                    encryptionConfig_kmsKeyNames: str | _list[str] = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> BackupHttpRequest: ...
                def getIamPolicy(
                    self,
                    *,
                    resource: str,
                    body: GetIamPolicyRequest = ...,
                    **kwargs: typing.Any,
                ) -> PolicyHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
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
                ) -> BackupHttpRequest: ...
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
                def operations(self) -> OperationsResource: ...

            @typing.type_check_only
            class DatabaseOperationsResource(googleapiclient.discovery.Resource):
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> ListDatabaseOperationsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListDatabaseOperationsResponseHttpRequest,
                    previous_response: ListDatabaseOperationsResponse,
                ) -> ListDatabaseOperationsResponseHttpRequest | None: ...

            @typing.type_check_only
            class DatabasesResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class BackupSchedulesResource(googleapiclient.discovery.Resource):
                    def create(
                        self,
                        *,
                        parent: str,
                        body: BackupSchedule = ...,
                        backupScheduleId: str = ...,
                        **kwargs: typing.Any,
                    ) -> BackupScheduleHttpRequest: ...
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> EmptyHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> BackupScheduleHttpRequest: ...
                    def getIamPolicy(
                        self,
                        *,
                        resource: str,
                        body: GetIamPolicyRequest = ...,
                        **kwargs: typing.Any,
                    ) -> PolicyHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
                    ) -> ListBackupSchedulesResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: ListBackupSchedulesResponseHttpRequest,
                        previous_response: ListBackupSchedulesResponse,
                    ) -> ListBackupSchedulesResponseHttpRequest | None: ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: BackupSchedule = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any,
                    ) -> BackupScheduleHttpRequest: ...
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
                class DatabaseRolesResource(googleapiclient.discovery.Resource):
                    def list(
                        self,
                        *,
                        parent: str,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
                    ) -> ListDatabaseRolesResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: ListDatabaseRolesResponseHttpRequest,
                        previous_response: ListDatabaseRolesResponse,
                    ) -> ListDatabaseRolesResponseHttpRequest | None: ...
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

                @typing.type_check_only
                class SessionsResource(googleapiclient.discovery.Resource):
                    def batchCreate(
                        self,
                        *,
                        database: str,
                        body: BatchCreateSessionsRequest = ...,
                        **kwargs: typing.Any,
                    ) -> BatchCreateSessionsResponseHttpRequest: ...
                    def batchWrite(
                        self,
                        *,
                        session: str,
                        body: BatchWriteRequest = ...,
                        **kwargs: typing.Any,
                    ) -> BatchWriteResponseHttpRequest: ...
                    def beginTransaction(
                        self,
                        *,
                        session: str,
                        body: BeginTransactionRequest = ...,
                        **kwargs: typing.Any,
                    ) -> TransactionHttpRequest: ...
                    def commit(
                        self,
                        *,
                        session: str,
                        body: CommitRequest = ...,
                        **kwargs: typing.Any,
                    ) -> CommitResponseHttpRequest: ...
                    def create(
                        self,
                        *,
                        database: str,
                        body: CreateSessionRequest = ...,
                        **kwargs: typing.Any,
                    ) -> SessionHttpRequest: ...
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> EmptyHttpRequest: ...
                    def executeBatchDml(
                        self,
                        *,
                        session: str,
                        body: ExecuteBatchDmlRequest = ...,
                        **kwargs: typing.Any,
                    ) -> ExecuteBatchDmlResponseHttpRequest: ...
                    def executeSql(
                        self,
                        *,
                        session: str,
                        body: ExecuteSqlRequest = ...,
                        **kwargs: typing.Any,
                    ) -> ResultSetHttpRequest: ...
                    def executeStreamingSql(
                        self,
                        *,
                        session: str,
                        body: ExecuteSqlRequest = ...,
                        **kwargs: typing.Any,
                    ) -> PartialResultSetHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> SessionHttpRequest: ...
                    def list(
                        self,
                        *,
                        database: str,
                        filter: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
                    ) -> ListSessionsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: ListSessionsResponseHttpRequest,
                        previous_response: ListSessionsResponse,
                    ) -> ListSessionsResponseHttpRequest | None: ...
                    def partitionQuery(
                        self,
                        *,
                        session: str,
                        body: PartitionQueryRequest = ...,
                        **kwargs: typing.Any,
                    ) -> PartitionResponseHttpRequest: ...
                    def partitionRead(
                        self,
                        *,
                        session: str,
                        body: PartitionReadRequest = ...,
                        **kwargs: typing.Any,
                    ) -> PartitionResponseHttpRequest: ...
                    def read(
                        self,
                        *,
                        session: str,
                        body: ReadRequest = ...,
                        **kwargs: typing.Any,
                    ) -> ResultSetHttpRequest: ...
                    def rollback(
                        self,
                        *,
                        session: str,
                        body: RollbackRequest = ...,
                        **kwargs: typing.Any,
                    ) -> EmptyHttpRequest: ...
                    def streamingRead(
                        self,
                        *,
                        session: str,
                        body: ReadRequest = ...,
                        **kwargs: typing.Any,
                    ) -> PartialResultSetHttpRequest: ...

                def addSplitPoints(
                    self,
                    *,
                    database: str,
                    body: AddSplitPointsRequest = ...,
                    **kwargs: typing.Any,
                ) -> AddSplitPointsResponseHttpRequest: ...
                def changequorum(
                    self,
                    *,
                    name: str,
                    body: ChangeQuorumRequest = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def create(
                    self,
                    *,
                    parent: str,
                    body: CreateDatabaseRequest = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def dropDatabase(
                    self, *, database: str, **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> DatabaseHttpRequest: ...
                def getDdl(
                    self, *, database: str, **kwargs: typing.Any
                ) -> GetDatabaseDdlResponseHttpRequest: ...
                def getIamPolicy(
                    self,
                    *,
                    resource: str,
                    body: GetIamPolicyRequest = ...,
                    **kwargs: typing.Any,
                ) -> PolicyHttpRequest: ...
                def getScans(
                    self,
                    *,
                    name: str,
                    endTime: str = ...,
                    startTime: str = ...,
                    view: typing_extensions.Literal[
                        "VIEW_UNSPECIFIED", "SUMMARY", "FULL"
                    ] = ...,
                    **kwargs: typing.Any,
                ) -> ScanHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> ListDatabasesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListDatabasesResponseHttpRequest,
                    previous_response: ListDatabasesResponse,
                ) -> ListDatabasesResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: Database = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def restore(
                    self,
                    *,
                    parent: str,
                    body: RestoreDatabaseRequest = ...,
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
                def updateDdl(
                    self,
                    *,
                    database: str,
                    body: UpdateDatabaseDdlRequest = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def backupSchedules(self) -> BackupSchedulesResource: ...
                def databaseRoles(self) -> DatabaseRolesResource: ...
                def operations(self) -> OperationsResource: ...
                def sessions(self) -> SessionsResource: ...

            @typing.type_check_only
            class InstancePartitionOperationsResource(
                googleapiclient.discovery.Resource
            ):
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    instancePartitionDeadline: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> ListInstancePartitionOperationsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListInstancePartitionOperationsResponseHttpRequest,
                    previous_response: ListInstancePartitionOperationsResponse,
                ) -> ListInstancePartitionOperationsResponseHttpRequest | None: ...

            @typing.type_check_only
            class InstancePartitionsResource(googleapiclient.discovery.Resource):
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

                def create(
                    self,
                    *,
                    parent: str,
                    body: CreateInstancePartitionRequest = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def delete(
                    self, *, name: str, etag: str = ..., **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> InstancePartitionHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    instancePartitionDeadline: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> ListInstancePartitionsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListInstancePartitionsResponseHttpRequest,
                    previous_response: ListInstancePartitionsResponse,
                ) -> ListInstancePartitionsResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: UpdateInstancePartitionRequest = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def operations(self) -> OperationsResource: ...

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

            def create(
                self,
                *,
                parent: str,
                body: CreateInstanceRequest = ...,
                **kwargs: typing.Any,
            ) -> OperationHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def get(
                self, *, name: str, fieldMask: str = ..., **kwargs: typing.Any
            ) -> InstanceHttpRequest: ...
            def getIamPolicy(
                self,
                *,
                resource: str,
                body: GetIamPolicyRequest = ...,
                **kwargs: typing.Any,
            ) -> PolicyHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                filter: str = ...,
                instanceDeadline: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any,
            ) -> ListInstancesResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListInstancesResponseHttpRequest,
                previous_response: ListInstancesResponse,
            ) -> ListInstancesResponseHttpRequest | None: ...
            def move(
                self,
                *,
                name: str,
                body: MoveInstanceRequest = ...,
                **kwargs: typing.Any,
            ) -> OperationHttpRequest: ...
            def patch(
                self,
                *,
                name: str,
                body: UpdateInstanceRequest = ...,
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
            def backupOperations(self) -> BackupOperationsResource: ...
            def backups(self) -> BackupsResource: ...
            def databaseOperations(self) -> DatabaseOperationsResource: ...
            def databases(self) -> DatabasesResource: ...
            def instancePartitionOperations(
                self,
            ) -> InstancePartitionOperationsResource: ...
            def instancePartitions(self) -> InstancePartitionsResource: ...
            def operations(self) -> OperationsResource: ...

        def instanceConfigOperations(self) -> InstanceConfigOperationsResource: ...
        def instanceConfigs(self) -> InstanceConfigsResource: ...
        def instances(self) -> InstancesResource: ...

    @typing.type_check_only
    class ScansResource(googleapiclient.discovery.Resource):
        def list(
            self,
            *,
            parent: str,
            filter: str = ...,
            pageSize: int = ...,
            pageToken: str = ...,
            view: typing_extensions.Literal[
                "VIEW_UNSPECIFIED", "SUMMARY", "FULL"
            ] = ...,
            **kwargs: typing.Any,
        ) -> ListScansResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: ListScansResponseHttpRequest,
            previous_response: ListScansResponse,
        ) -> ListScansResponseHttpRequest | None: ...

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
    def scans(self) -> ScansResource: ...

@typing.type_check_only
class AddSplitPointsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> AddSplitPointsResponse: ...

@typing.type_check_only
class BackupHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Backup: ...

@typing.type_check_only
class BackupScheduleHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> BackupSchedule: ...

@typing.type_check_only
class BatchCreateSessionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> BatchCreateSessionsResponse: ...

@typing.type_check_only
class BatchWriteResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> BatchWriteResponse: ...

@typing.type_check_only
class CommitResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> CommitResponse: ...

@typing.type_check_only
class DatabaseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Database: ...

@typing.type_check_only
class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Empty: ...

@typing.type_check_only
class ExecuteBatchDmlResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ExecuteBatchDmlResponse: ...

@typing.type_check_only
class GetDatabaseDdlResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GetDatabaseDdlResponse: ...

@typing.type_check_only
class InstanceHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Instance: ...

@typing.type_check_only
class InstanceConfigHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> InstanceConfig: ...

@typing.type_check_only
class InstancePartitionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> InstancePartition: ...

@typing.type_check_only
class ListBackupOperationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListBackupOperationsResponse: ...

@typing.type_check_only
class ListBackupSchedulesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListBackupSchedulesResponse: ...

@typing.type_check_only
class ListBackupsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListBackupsResponse: ...

@typing.type_check_only
class ListDatabaseOperationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListDatabaseOperationsResponse: ...

@typing.type_check_only
class ListDatabaseRolesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListDatabaseRolesResponse: ...

@typing.type_check_only
class ListDatabasesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListDatabasesResponse: ...

@typing.type_check_only
class ListInstanceConfigOperationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListInstanceConfigOperationsResponse: ...

@typing.type_check_only
class ListInstanceConfigsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListInstanceConfigsResponse: ...

@typing.type_check_only
class ListInstancePartitionOperationsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListInstancePartitionOperationsResponse: ...

@typing.type_check_only
class ListInstancePartitionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListInstancePartitionsResponse: ...

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
class ListScansResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListScansResponse: ...

@typing.type_check_only
class ListSessionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListSessionsResponse: ...

@typing.type_check_only
class OperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Operation: ...

@typing.type_check_only
class PartialResultSetHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> PartialResultSet: ...

@typing.type_check_only
class PartitionResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> PartitionResponse: ...

@typing.type_check_only
class PolicyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Policy: ...

@typing.type_check_only
class ResultSetHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ResultSet: ...

@typing.type_check_only
class ScanHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Scan: ...

@typing.type_check_only
class SessionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Session: ...

@typing.type_check_only
class TestIamPermissionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> TestIamPermissionsResponse: ...

@typing.type_check_only
class TransactionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Transaction: ...
