import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class SpannerResource(googleapiclient.discovery.Resource):
    class ProjectsResource(googleapiclient.discovery.Resource):
        class InstanceConfigsResource(googleapiclient.discovery.Resource):
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> InstanceConfigHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageToken: str = ...,
                pageSize: int = ...,
                **kwargs: typing.Any
            ) -> ListInstanceConfigsResponseHttpRequest: ...
        class InstancesResource(googleapiclient.discovery.Resource):
            class BackupsResource(googleapiclient.discovery.Resource):
                class OperationsResource(googleapiclient.discovery.Resource):
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> OperationHttpRequest: ...
                    def cancel(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> EmptyHttpRequest: ...
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> EmptyHttpRequest: ...
                    def list(
                        self,
                        *,
                        name: str,
                        filter: str = ...,
                        pageToken: str = ...,
                        pageSize: int = ...,
                        **kwargs: typing.Any
                    ) -> ListOperationsResponseHttpRequest: ...
                def create(
                    self,
                    *,
                    parent: str,
                    body: Backup = ...,
                    backupId: str = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> BackupHttpRequest: ...
                def setIamPolicy(
                    self,
                    *,
                    resource: str,
                    body: SetIamPolicyRequest = ...,
                    **kwargs: typing.Any
                ) -> PolicyHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageToken: str = ...,
                    pageSize: int = ...,
                    filter: str = ...,
                    **kwargs: typing.Any
                ) -> ListBackupsResponseHttpRequest: ...
                def getIamPolicy(
                    self,
                    *,
                    resource: str,
                    body: GetIamPolicyRequest = ...,
                    **kwargs: typing.Any
                ) -> PolicyHttpRequest: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: Backup = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any
                ) -> BackupHttpRequest: ...
                def testIamPermissions(
                    self,
                    *,
                    resource: str,
                    body: TestIamPermissionsRequest = ...,
                    **kwargs: typing.Any
                ) -> TestIamPermissionsResponseHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def operations(self) -> OperationsResource: ...
            class DatabaseOperationsResource(googleapiclient.discovery.Resource):
                def list(
                    self,
                    *,
                    parent: str,
                    pageToken: str = ...,
                    pageSize: int = ...,
                    filter: str = ...,
                    **kwargs: typing.Any
                ) -> ListDatabaseOperationsResponseHttpRequest: ...
            class DatabasesResource(googleapiclient.discovery.Resource):
                class OperationsResource(googleapiclient.discovery.Resource):
                    def cancel(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> EmptyHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> OperationHttpRequest: ...
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> EmptyHttpRequest: ...
                    def list(
                        self,
                        *,
                        name: str,
                        pageToken: str = ...,
                        filter: str = ...,
                        pageSize: int = ...,
                        **kwargs: typing.Any
                    ) -> ListOperationsResponseHttpRequest: ...
                class SessionsResource(googleapiclient.discovery.Resource):
                    def create(
                        self,
                        *,
                        database: str,
                        body: CreateSessionRequest = ...,
                        **kwargs: typing.Any
                    ) -> SessionHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> SessionHttpRequest: ...
                    def list(
                        self,
                        *,
                        database: str,
                        pageToken: str = ...,
                        filter: str = ...,
                        pageSize: int = ...,
                        **kwargs: typing.Any
                    ) -> ListSessionsResponseHttpRequest: ...
                    def read(
                        self,
                        *,
                        session: str,
                        body: ReadRequest = ...,
                        **kwargs: typing.Any
                    ) -> ResultSetHttpRequest: ...
                    def beginTransaction(
                        self,
                        *,
                        session: str,
                        body: BeginTransactionRequest = ...,
                        **kwargs: typing.Any
                    ) -> TransactionHttpRequest: ...
                    def partitionRead(
                        self,
                        *,
                        session: str,
                        body: PartitionReadRequest = ...,
                        **kwargs: typing.Any
                    ) -> PartitionResponseHttpRequest: ...
                    def executeStreamingSql(
                        self,
                        *,
                        session: str,
                        body: ExecuteSqlRequest = ...,
                        **kwargs: typing.Any
                    ) -> PartialResultSetHttpRequest: ...
                    def executeSql(
                        self,
                        *,
                        session: str,
                        body: ExecuteSqlRequest = ...,
                        **kwargs: typing.Any
                    ) -> ResultSetHttpRequest: ...
                    def batchCreate(
                        self,
                        *,
                        database: str,
                        body: BatchCreateSessionsRequest = ...,
                        **kwargs: typing.Any
                    ) -> BatchCreateSessionsResponseHttpRequest: ...
                    def commit(
                        self,
                        *,
                        session: str,
                        body: CommitRequest = ...,
                        **kwargs: typing.Any
                    ) -> CommitResponseHttpRequest: ...
                    def rollback(
                        self,
                        *,
                        session: str,
                        body: RollbackRequest = ...,
                        **kwargs: typing.Any
                    ) -> EmptyHttpRequest: ...
                    def executeBatchDml(
                        self,
                        *,
                        session: str,
                        body: ExecuteBatchDmlRequest = ...,
                        **kwargs: typing.Any
                    ) -> ExecuteBatchDmlResponseHttpRequest: ...
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> EmptyHttpRequest: ...
                    def partitionQuery(
                        self,
                        *,
                        session: str,
                        body: PartitionQueryRequest = ...,
                        **kwargs: typing.Any
                    ) -> PartitionResponseHttpRequest: ...
                    def streamingRead(
                        self,
                        *,
                        session: str,
                        body: ReadRequest = ...,
                        **kwargs: typing.Any
                    ) -> PartialResultSetHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> ListDatabasesResponseHttpRequest: ...
                def dropDatabase(
                    self, *, database: str, **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def testIamPermissions(
                    self,
                    *,
                    resource: str,
                    body: TestIamPermissionsRequest = ...,
                    **kwargs: typing.Any
                ) -> TestIamPermissionsResponseHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> DatabaseHttpRequest: ...
                def updateDdl(
                    self,
                    *,
                    database: str,
                    body: UpdateDatabaseDdlRequest = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def setIamPolicy(
                    self,
                    *,
                    resource: str,
                    body: SetIamPolicyRequest = ...,
                    **kwargs: typing.Any
                ) -> PolicyHttpRequest: ...
                def create(
                    self,
                    *,
                    parent: str,
                    body: CreateDatabaseRequest = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def getDdl(
                    self, *, database: str, **kwargs: typing.Any
                ) -> GetDatabaseDdlResponseHttpRequest: ...
                def getIamPolicy(
                    self,
                    *,
                    resource: str,
                    body: GetIamPolicyRequest = ...,
                    **kwargs: typing.Any
                ) -> PolicyHttpRequest: ...
                def restore(
                    self,
                    *,
                    parent: str,
                    body: RestoreDatabaseRequest = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def operations(self) -> OperationsResource: ...
                def sessions(self) -> SessionsResource: ...
            class OperationsResource(googleapiclient.discovery.Resource):
                def cancel(
                    self, *, name: str, **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def list(
                    self,
                    *,
                    name: str,
                    pageToken: str = ...,
                    filter: str = ...,
                    pageSize: int = ...,
                    **kwargs: typing.Any
                ) -> ListOperationsResponseHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
            class BackupOperationsResource(googleapiclient.discovery.Resource):
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    filter: str = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> ListBackupOperationsResponseHttpRequest: ...
            def getIamPolicy(
                self,
                *,
                resource: str,
                body: GetIamPolicyRequest = ...,
                **kwargs: typing.Any
            ) -> PolicyHttpRequest: ...
            def testIamPermissions(
                self,
                *,
                resource: str,
                body: TestIamPermissionsRequest = ...,
                **kwargs: typing.Any
            ) -> TestIamPermissionsResponseHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def get(
                self, *, name: str, fieldMask: str = ..., **kwargs: typing.Any
            ) -> InstanceHttpRequest: ...
            def patch(
                self,
                *,
                name: str,
                body: UpdateInstanceRequest = ...,
                **kwargs: typing.Any
            ) -> OperationHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageToken: str = ...,
                filter: str = ...,
                pageSize: int = ...,
                **kwargs: typing.Any
            ) -> ListInstancesResponseHttpRequest: ...
            def setIamPolicy(
                self,
                *,
                resource: str,
                body: SetIamPolicyRequest = ...,
                **kwargs: typing.Any
            ) -> PolicyHttpRequest: ...
            def create(
                self,
                *,
                parent: str,
                body: CreateInstanceRequest = ...,
                **kwargs: typing.Any
            ) -> OperationHttpRequest: ...
            def backups(self) -> BackupsResource: ...
            def databaseOperations(self) -> DatabaseOperationsResource: ...
            def databases(self) -> DatabasesResource: ...
            def operations(self) -> OperationsResource: ...
            def backupOperations(self) -> BackupOperationsResource: ...
        def instanceConfigs(self) -> InstanceConfigsResource: ...
        def instances(self) -> InstancesResource: ...
    def projects(self) -> ProjectsResource: ...

class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Empty: ...

class ListSessionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListSessionsResponse: ...

class InstanceHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Instance: ...

class GetDatabaseDdlResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GetDatabaseDdlResponse: ...

class InstanceConfigHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> InstanceConfig: ...

class ListBackupsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListBackupsResponse: ...

class BatchCreateSessionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> BatchCreateSessionsResponse: ...

class OperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Operation: ...

class ListDatabasesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListDatabasesResponse: ...

class DatabaseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Database: ...

class ListInstanceConfigsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListInstanceConfigsResponse: ...

class TransactionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Transaction: ...

class ResultSetHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ResultSet: ...

class ExecuteBatchDmlResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ExecuteBatchDmlResponse: ...

class ListBackupOperationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListBackupOperationsResponse: ...

class ListInstancesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListInstancesResponse: ...

class CommitResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> CommitResponse: ...

class ListOperationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListOperationsResponse: ...

class TestIamPermissionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> TestIamPermissionsResponse: ...

class PartialResultSetHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> PartialResultSet: ...

class PolicyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Policy: ...

class SessionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Session: ...

class PartitionResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> PartitionResponse: ...

class BackupHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Backup: ...

class ListDatabaseOperationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListDatabaseOperationsResponse: ...
