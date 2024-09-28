import collections.abc
import typing

import httplib2
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http

from .schemas import *

_list = list

@typing.type_check_only
class SQLAdminResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class BackupRunsResource(googleapiclient.discovery.Resource):
        def delete(
            self, *, project: str, instance: str, id: str, **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def get(
            self, *, project: str, instance: str, id: str, **kwargs: typing.Any
        ) -> BackupRunHttpRequest: ...
        def insert(
            self,
            *,
            project: str,
            instance: str,
            body: BackupRun = ...,
            **kwargs: typing.Any,
        ) -> OperationHttpRequest: ...
        def list(
            self,
            *,
            project: str,
            instance: str,
            maxResults: int = ...,
            pageToken: str = ...,
            **kwargs: typing.Any,
        ) -> BackupRunsListResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: BackupRunsListResponseHttpRequest,
            previous_response: BackupRunsListResponse,
        ) -> BackupRunsListResponseHttpRequest | None: ...

    @typing.type_check_only
    class ConnectResource(googleapiclient.discovery.Resource):
        def generateEphemeralCert(
            self,
            *,
            project: str,
            instance: str,
            body: GenerateEphemeralCertRequest = ...,
            **kwargs: typing.Any,
        ) -> GenerateEphemeralCertResponseHttpRequest: ...
        def get(
            self,
            *,
            project: str,
            instance: str,
            readTime: str = ...,
            **kwargs: typing.Any,
        ) -> ConnectSettingsHttpRequest: ...

    @typing.type_check_only
    class DatabasesResource(googleapiclient.discovery.Resource):
        def delete(
            self, *, project: str, instance: str, database: str, **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def get(
            self, *, project: str, instance: str, database: str, **kwargs: typing.Any
        ) -> DatabaseHttpRequest: ...
        def insert(
            self,
            *,
            project: str,
            instance: str,
            body: Database = ...,
            **kwargs: typing.Any,
        ) -> OperationHttpRequest: ...
        def list(
            self, *, project: str, instance: str, **kwargs: typing.Any
        ) -> DatabasesListResponseHttpRequest: ...
        def patch(
            self,
            *,
            project: str,
            instance: str,
            database: str,
            body: Database = ...,
            **kwargs: typing.Any,
        ) -> OperationHttpRequest: ...
        def update(
            self,
            *,
            project: str,
            instance: str,
            database: str,
            body: Database = ...,
            **kwargs: typing.Any,
        ) -> OperationHttpRequest: ...

    @typing.type_check_only
    class FlagsResource(googleapiclient.discovery.Resource):
        def list(
            self, *, databaseVersion: str = ..., **kwargs: typing.Any
        ) -> FlagsListResponseHttpRequest: ...

    @typing.type_check_only
    class InstancesResource(googleapiclient.discovery.Resource):
        def ListServerCertificates(
            self, *, project: str, instance: str, **kwargs: typing.Any
        ) -> InstancesListServerCertificatesResponseHttpRequest: ...
        def RotateServerCertificate(
            self,
            *,
            project: str,
            instance: str,
            body: InstancesRotateServerCertificateRequest = ...,
            **kwargs: typing.Any,
        ) -> OperationHttpRequest: ...
        def acquireSsrsLease(
            self,
            *,
            project: str,
            instance: str,
            body: InstancesAcquireSsrsLeaseRequest = ...,
            **kwargs: typing.Any,
        ) -> SqlInstancesAcquireSsrsLeaseResponseHttpRequest: ...
        def addServerCa(
            self, *, project: str, instance: str, **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def addServerCertificate(
            self, *, project: str, instance: str, **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def clone(
            self,
            *,
            project: str,
            instance: str,
            body: InstancesCloneRequest = ...,
            **kwargs: typing.Any,
        ) -> OperationHttpRequest: ...
        def delete(
            self, *, project: str, instance: str, **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def demote(
            self,
            *,
            project: str,
            instance: str,
            body: InstancesDemoteRequest = ...,
            **kwargs: typing.Any,
        ) -> OperationHttpRequest: ...
        def demoteMaster(
            self,
            *,
            project: str,
            instance: str,
            body: InstancesDemoteMasterRequest = ...,
            **kwargs: typing.Any,
        ) -> OperationHttpRequest: ...
        def export(
            self,
            *,
            project: str,
            instance: str,
            body: InstancesExportRequest = ...,
            **kwargs: typing.Any,
        ) -> OperationHttpRequest: ...
        def failover(
            self,
            *,
            project: str,
            instance: str,
            body: InstancesFailoverRequest = ...,
            **kwargs: typing.Any,
        ) -> OperationHttpRequest: ...
        def get(
            self, *, project: str, instance: str, **kwargs: typing.Any
        ) -> DatabaseInstanceHttpRequest: ...
        def import_(
            self,
            *,
            project: str,
            instance: str,
            body: InstancesImportRequest = ...,
            **kwargs: typing.Any,
        ) -> OperationHttpRequest: ...
        def insert(
            self, *, project: str, body: DatabaseInstance = ..., **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def list(
            self,
            *,
            project: str,
            filter: str = ...,
            maxResults: int = ...,
            pageToken: str = ...,
            **kwargs: typing.Any,
        ) -> InstancesListResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: InstancesListResponseHttpRequest,
            previous_response: InstancesListResponse,
        ) -> InstancesListResponseHttpRequest | None: ...
        def listServerCas(
            self, *, project: str, instance: str, **kwargs: typing.Any
        ) -> InstancesListServerCasResponseHttpRequest: ...
        def patch(
            self,
            *,
            project: str,
            instance: str,
            body: DatabaseInstance = ...,
            **kwargs: typing.Any,
        ) -> OperationHttpRequest: ...
        def promoteReplica(
            self,
            *,
            project: str,
            instance: str,
            failover: bool = ...,
            **kwargs: typing.Any,
        ) -> OperationHttpRequest: ...
        def reencrypt(
            self,
            *,
            project: str,
            instance: str,
            body: InstancesReencryptRequest = ...,
            **kwargs: typing.Any,
        ) -> OperationHttpRequest: ...
        def releaseSsrsLease(
            self, *, project: str, instance: str, **kwargs: typing.Any
        ) -> SqlInstancesReleaseSsrsLeaseResponseHttpRequest: ...
        def resetSslConfig(
            self, *, project: str, instance: str, **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def restart(
            self, *, project: str, instance: str, **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def restoreBackup(
            self,
            *,
            project: str,
            instance: str,
            body: InstancesRestoreBackupRequest = ...,
            **kwargs: typing.Any,
        ) -> OperationHttpRequest: ...
        def rotateServerCa(
            self,
            *,
            project: str,
            instance: str,
            body: InstancesRotateServerCaRequest = ...,
            **kwargs: typing.Any,
        ) -> OperationHttpRequest: ...
        def startReplica(
            self, *, project: str, instance: str, **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def stopReplica(
            self, *, project: str, instance: str, **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def switchover(
            self,
            *,
            project: str,
            instance: str,
            dbTimeout: str = ...,
            **kwargs: typing.Any,
        ) -> OperationHttpRequest: ...
        def truncateLog(
            self,
            *,
            project: str,
            instance: str,
            body: InstancesTruncateLogRequest = ...,
            **kwargs: typing.Any,
        ) -> OperationHttpRequest: ...
        def update(
            self,
            *,
            project: str,
            instance: str,
            body: DatabaseInstance = ...,
            **kwargs: typing.Any,
        ) -> OperationHttpRequest: ...

    @typing.type_check_only
    class OperationsResource(googleapiclient.discovery.Resource):
        def cancel(
            self, *, project: str, operation: str, **kwargs: typing.Any
        ) -> EmptyHttpRequest: ...
        def get(
            self, *, project: str, operation: str, **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def list(
            self,
            *,
            project: str,
            instance: str = ...,
            maxResults: int = ...,
            pageToken: str = ...,
            **kwargs: typing.Any,
        ) -> OperationsListResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: OperationsListResponseHttpRequest,
            previous_response: OperationsListResponse,
        ) -> OperationsListResponseHttpRequest | None: ...

    @typing.type_check_only
    class ProjectsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class InstancesResource(googleapiclient.discovery.Resource):
            def getDiskShrinkConfig(
                self, *, project: str, instance: str, **kwargs: typing.Any
            ) -> SqlInstancesGetDiskShrinkConfigResponseHttpRequest: ...
            def getLatestRecoveryTime(
                self, *, project: str, instance: str, **kwargs: typing.Any
            ) -> SqlInstancesGetLatestRecoveryTimeResponseHttpRequest: ...
            def performDiskShrink(
                self,
                *,
                project: str,
                instance: str,
                body: PerformDiskShrinkContext = ...,
                **kwargs: typing.Any,
            ) -> OperationHttpRequest: ...
            def rescheduleMaintenance(
                self,
                *,
                project: str,
                instance: str,
                body: SqlInstancesRescheduleMaintenanceRequestBody = ...,
                **kwargs: typing.Any,
            ) -> OperationHttpRequest: ...
            def resetReplicaSize(
                self,
                *,
                project: str,
                instance: str,
                body: SqlInstancesResetReplicaSizeRequest = ...,
                **kwargs: typing.Any,
            ) -> OperationHttpRequest: ...
            def startExternalSync(
                self,
                *,
                project: str,
                instance: str,
                body: SqlInstancesStartExternalSyncRequest = ...,
                **kwargs: typing.Any,
            ) -> OperationHttpRequest: ...
            def verifyExternalSyncSettings(
                self,
                *,
                project: str,
                instance: str,
                body: SqlInstancesVerifyExternalSyncSettingsRequest = ...,
                **kwargs: typing.Any,
            ) -> SqlInstancesVerifyExternalSyncSettingsResponseHttpRequest: ...

        def instances(self) -> InstancesResource: ...

    @typing.type_check_only
    class SslCertsResource(googleapiclient.discovery.Resource):
        def createEphemeral(
            self,
            *,
            project: str,
            instance: str,
            body: SslCertsCreateEphemeralRequest = ...,
            **kwargs: typing.Any,
        ) -> SslCertHttpRequest: ...
        def delete(
            self,
            *,
            project: str,
            instance: str,
            sha1Fingerprint: str,
            **kwargs: typing.Any,
        ) -> OperationHttpRequest: ...
        def get(
            self,
            *,
            project: str,
            instance: str,
            sha1Fingerprint: str,
            **kwargs: typing.Any,
        ) -> SslCertHttpRequest: ...
        def insert(
            self,
            *,
            project: str,
            instance: str,
            body: SslCertsInsertRequest = ...,
            **kwargs: typing.Any,
        ) -> SslCertsInsertResponseHttpRequest: ...
        def list(
            self, *, project: str, instance: str, **kwargs: typing.Any
        ) -> SslCertsListResponseHttpRequest: ...

    @typing.type_check_only
    class TiersResource(googleapiclient.discovery.Resource):
        def list(
            self, *, project: str, **kwargs: typing.Any
        ) -> TiersListResponseHttpRequest: ...

    @typing.type_check_only
    class UsersResource(googleapiclient.discovery.Resource):
        def delete(
            self,
            *,
            project: str,
            instance: str,
            host: str = ...,
            name: str = ...,
            **kwargs: typing.Any,
        ) -> OperationHttpRequest: ...
        def get(
            self,
            *,
            project: str,
            instance: str,
            name: str,
            host: str = ...,
            **kwargs: typing.Any,
        ) -> UserHttpRequest: ...
        def insert(
            self, *, project: str, instance: str, body: User = ..., **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def list(
            self, *, project: str, instance: str, **kwargs: typing.Any
        ) -> UsersListResponseHttpRequest: ...
        def update(
            self,
            *,
            project: str,
            instance: str,
            body: User = ...,
            host: str = ...,
            name: str = ...,
            **kwargs: typing.Any,
        ) -> OperationHttpRequest: ...

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
    def backupRuns(self) -> BackupRunsResource: ...
    def connect(self) -> ConnectResource: ...
    def databases(self) -> DatabasesResource: ...
    def flags(self) -> FlagsResource: ...
    def instances(self) -> InstancesResource: ...
    def operations(self) -> OperationsResource: ...
    def projects(self) -> ProjectsResource: ...
    def sslCerts(self) -> SslCertsResource: ...
    def tiers(self) -> TiersResource: ...
    def users(self) -> UsersResource: ...

@typing.type_check_only
class BackupRunHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> BackupRun: ...

@typing.type_check_only
class BackupRunsListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> BackupRunsListResponse: ...

@typing.type_check_only
class ConnectSettingsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ConnectSettings: ...

@typing.type_check_only
class DatabaseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Database: ...

@typing.type_check_only
class DatabaseInstanceHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> DatabaseInstance: ...

@typing.type_check_only
class DatabasesListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> DatabasesListResponse: ...

@typing.type_check_only
class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Empty: ...

@typing.type_check_only
class FlagsListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> FlagsListResponse: ...

@typing.type_check_only
class GenerateEphemeralCertResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GenerateEphemeralCertResponse: ...

@typing.type_check_only
class InstancesListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> InstancesListResponse: ...

@typing.type_check_only
class InstancesListServerCasResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> InstancesListServerCasResponse: ...

@typing.type_check_only
class InstancesListServerCertificatesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> InstancesListServerCertificatesResponse: ...

@typing.type_check_only
class OperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Operation: ...

@typing.type_check_only
class OperationsListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> OperationsListResponse: ...

@typing.type_check_only
class SqlInstancesAcquireSsrsLeaseResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> SqlInstancesAcquireSsrsLeaseResponse: ...

@typing.type_check_only
class SqlInstancesGetDiskShrinkConfigResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> SqlInstancesGetDiskShrinkConfigResponse: ...

@typing.type_check_only
class SqlInstancesGetLatestRecoveryTimeResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> SqlInstancesGetLatestRecoveryTimeResponse: ...

@typing.type_check_only
class SqlInstancesReleaseSsrsLeaseResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> SqlInstancesReleaseSsrsLeaseResponse: ...

@typing.type_check_only
class SqlInstancesVerifyExternalSyncSettingsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> SqlInstancesVerifyExternalSyncSettingsResponse: ...

@typing.type_check_only
class SslCertHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> SslCert: ...

@typing.type_check_only
class SslCertsInsertResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> SslCertsInsertResponse: ...

@typing.type_check_only
class SslCertsListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> SslCertsListResponse: ...

@typing.type_check_only
class TiersListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> TiersListResponse: ...

@typing.type_check_only
class UserHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> User: ...

@typing.type_check_only
class UsersListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> UsersListResponse: ...
