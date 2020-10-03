import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class SQLAdminResource(googleapiclient.discovery.Resource):
    class TiersResource(googleapiclient.discovery.Resource):
        def list(
            self, *, project: str, **kwargs: typing.Any
        ) -> TiersListResponseHttpRequest: ...
    class SslCertsResource(googleapiclient.discovery.Resource):
        def createEphemeral(
            self,
            *,
            project: str,
            instance: str,
            body: SslCertsCreateEphemeralRequest = ...,
            **kwargs: typing.Any
        ) -> SslCertHttpRequest: ...
        def get(
            self,
            *,
            project: str,
            instance: str,
            sha1Fingerprint: str,
            **kwargs: typing.Any
        ) -> SslCertHttpRequest: ...
        def insert(
            self,
            *,
            project: str,
            instance: str,
            body: SslCertsInsertRequest = ...,
            **kwargs: typing.Any
        ) -> SslCertsInsertResponseHttpRequest: ...
        def delete(
            self,
            *,
            project: str,
            instance: str,
            sha1Fingerprint: str,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def list(
            self, *, project: str, instance: str, **kwargs: typing.Any
        ) -> SslCertsListResponseHttpRequest: ...
    class DatabasesResource(googleapiclient.discovery.Resource):
        def update(
            self,
            *,
            project: str,
            instance: str,
            database: str,
            body: Database = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def delete(
            self, *, project: str, instance: str, database: str, **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def insert(
            self,
            *,
            project: str,
            instance: str,
            body: Database = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def patch(
            self,
            *,
            project: str,
            instance: str,
            database: str,
            body: Database = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def list(
            self, *, project: str, instance: str, **kwargs: typing.Any
        ) -> DatabasesListResponseHttpRequest: ...
        def get(
            self, *, project: str, instance: str, database: str, **kwargs: typing.Any
        ) -> DatabaseHttpRequest: ...
    class FlagsResource(googleapiclient.discovery.Resource):
        def list(
            self, *, databaseVersion: str = ..., **kwargs: typing.Any
        ) -> FlagsListResponseHttpRequest: ...
    class InstancesResource(googleapiclient.discovery.Resource):
        def list(
            self,
            *,
            project: str,
            filter: str = ...,
            maxResults: int = ...,
            pageToken: str = ...,
            **kwargs: typing.Any
        ) -> InstancesListResponseHttpRequest: ...
        def resetSslConfig(
            self, *, project: str, instance: str, **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def stopReplica(
            self, *, project: str, instance: str, **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def patch(
            self,
            *,
            project: str,
            instance: str,
            body: DatabaseInstance = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def demoteMaster(
            self,
            *,
            project: str,
            instance: str,
            body: InstancesDemoteMasterRequest = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def listServerCas(
            self, *, project: str, instance: str, **kwargs: typing.Any
        ) -> InstancesListServerCasResponseHttpRequest: ...
        def rotateServerCa(
            self,
            *,
            project: str,
            instance: str,
            body: InstancesRotateServerCaRequest = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def addServerCa(
            self, *, project: str, instance: str, **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def insert(
            self, *, project: str, body: DatabaseInstance = ..., **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def get(
            self, *, project: str, instance: str, **kwargs: typing.Any
        ) -> DatabaseInstanceHttpRequest: ...
        def startReplica(
            self, *, project: str, instance: str, **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def promoteReplica(
            self, *, project: str, instance: str, **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def failover(
            self,
            *,
            project: str,
            instance: str,
            body: InstancesFailoverRequest = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def restoreBackup(
            self,
            *,
            project: str,
            instance: str,
            body: InstancesRestoreBackupRequest = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def restart(
            self, *, project: str, instance: str, **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def delete(
            self, *, project: str, instance: str, **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def clone(
            self,
            *,
            project: str,
            instance: str,
            body: InstancesCloneRequest = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def import_(
            self,
            *,
            project: str,
            instance: str,
            body: InstancesImportRequest = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def truncateLog(
            self,
            *,
            project: str,
            instance: str,
            body: InstancesTruncateLogRequest = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def update(
            self,
            *,
            project: str,
            instance: str,
            body: DatabaseInstance = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def export(
            self,
            *,
            project: str,
            instance: str,
            body: InstancesExportRequest = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
    class UsersResource(googleapiclient.discovery.Resource):
        def delete(
            self,
            *,
            project: str,
            instance: str,
            name: str = ...,
            host: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def update(
            self,
            *,
            project: str,
            instance: str,
            body: User = ...,
            name: str = ...,
            host: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def insert(
            self, *, project: str, instance: str, body: User = ..., **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def list(
            self, *, project: str, instance: str, **kwargs: typing.Any
        ) -> UsersListResponseHttpRequest: ...
    class ProjectsResource(googleapiclient.discovery.Resource):
        class InstancesResource(googleapiclient.discovery.Resource):
            def rescheduleMaintenance(
                self,
                *,
                project: str,
                instance: str,
                body: SqlInstancesRescheduleMaintenanceRequestBody = ...,
                **kwargs: typing.Any
            ) -> OperationHttpRequest: ...
            def startExternalSync(
                self,
                *,
                project: str,
                instance: str,
                syncMode: typing_extensions.Literal[
                    "EXTERNAL_SYNC_MODE_UNSPECIFIED", "ONLINE", "OFFLINE"
                ] = ...,
                **kwargs: typing.Any
            ) -> OperationHttpRequest: ...
            def verifyExternalSyncSettings(
                self,
                *,
                project: str,
                instance: str,
                verifyConnectionOnly: bool = ...,
                syncMode: typing_extensions.Literal[
                    "EXTERNAL_SYNC_MODE_UNSPECIFIED", "ONLINE", "OFFLINE"
                ] = ...,
                **kwargs: typing.Any
            ) -> SqlInstancesVerifyExternalSyncSettingsResponseHttpRequest: ...
        def instances(self) -> InstancesResource: ...
    class OperationsResource(googleapiclient.discovery.Resource):
        def get(
            self, *, project: str, operation: str, **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def list(
            self,
            *,
            project: str,
            pageToken: str = ...,
            maxResults: int = ...,
            instance: str = ...,
            **kwargs: typing.Any
        ) -> OperationsListResponseHttpRequest: ...
    class BackupRunsResource(googleapiclient.discovery.Resource):
        def get(
            self, *, project: str, instance: str, id: str, **kwargs: typing.Any
        ) -> BackupRunHttpRequest: ...
        def insert(
            self,
            *,
            project: str,
            instance: str,
            body: BackupRun = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def delete(
            self, *, project: str, instance: str, id: str, **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def list(
            self,
            *,
            project: str,
            instance: str,
            maxResults: int = ...,
            pageToken: str = ...,
            **kwargs: typing.Any
        ) -> BackupRunsListResponseHttpRequest: ...
    def tiers(self) -> TiersResource: ...
    def sslCerts(self) -> SslCertsResource: ...
    def databases(self) -> DatabasesResource: ...
    def flags(self) -> FlagsResource: ...
    def instances(self) -> InstancesResource: ...
    def users(self) -> UsersResource: ...
    def projects(self) -> ProjectsResource: ...
    def operations(self) -> OperationsResource: ...
    def backupRuns(self) -> BackupRunsResource: ...

class TiersListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> TiersListResponse: ...

class SslCertsListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> SslCertsListResponse: ...

class DatabaseInstanceHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> DatabaseInstance: ...

class SqlInstancesVerifyExternalSyncSettingsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> SqlInstancesVerifyExternalSyncSettingsResponse: ...

class InstancesListServerCasResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> InstancesListServerCasResponse: ...

class InstancesListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> InstancesListResponse: ...

class SslCertHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> SslCert: ...

class OperationsListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> OperationsListResponse: ...

class DatabasesListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> DatabasesListResponse: ...

class FlagsListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> FlagsListResponse: ...

class BackupRunsListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> BackupRunsListResponse: ...

class DatabaseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Database: ...

class OperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Operation: ...

class BackupRunHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> BackupRun: ...

class SslCertsInsertResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> SslCertsInsertResponse: ...

class UsersListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> UsersListResponse: ...
