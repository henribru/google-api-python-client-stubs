import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *
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
            **kwargs: typing.Any
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
            **kwargs: typing.Any
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
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def update(
            self,
            *,
            project: str,
            instance: str,
            database: str,
            body: Database = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
    @typing.type_check_only
    class FlagsResource(googleapiclient.discovery.Resource):
        def list(
            self, *, databaseVersion: str = ..., **kwargs: typing.Any
        ) -> FlagsListResponseHttpRequest: ...
    @typing.type_check_only
    class InstancesResource(googleapiclient.discovery.Resource):
        def addServerCa(
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
        def delete(
            self, *, project: str, instance: str, **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def demoteMaster(
            self,
            *,
            project: str,
            instance: str,
            body: InstancesDemoteMasterRequest = ...,
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
        def failover(
            self,
            *,
            project: str,
            instance: str,
            body: InstancesFailoverRequest = ...,
            **kwargs: typing.Any
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
            **kwargs: typing.Any
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
            **kwargs: typing.Any
        ) -> InstancesListResponseHttpRequest: ...
        def listServerCas(
            self, *, project: str, instance: str, **kwargs: typing.Any
        ) -> InstancesListServerCasResponseHttpRequest: ...
        def patch(
            self,
            *,
            project: str,
            instance: str,
            body: DatabaseInstance = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def promoteReplica(
            self, *, project: str, instance: str, **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
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
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def rotateServerCa(
            self,
            *,
            project: str,
            instance: str,
            body: InstancesRotateServerCaRequest = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def startReplica(
            self, *, project: str, instance: str, **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def stopReplica(
            self, *, project: str, instance: str, **kwargs: typing.Any
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
    @typing.type_check_only
    class OperationsResource(googleapiclient.discovery.Resource):
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
            **kwargs: typing.Any
        ) -> OperationsListResponseHttpRequest: ...
    @typing.type_check_only
    class ProjectsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
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
                skipVerification: bool = ...,
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
                syncMode: typing_extensions.Literal[
                    "EXTERNAL_SYNC_MODE_UNSPECIFIED", "ONLINE", "OFFLINE"
                ] = ...,
                verifyConnectionOnly: bool = ...,
                **kwargs: typing.Any
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
            **kwargs: typing.Any
        ) -> SslCertHttpRequest: ...
        def delete(
            self,
            *,
            project: str,
            instance: str,
            sha1Fingerprint: str,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
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
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
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
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
    def backupRuns(self) -> BackupRunsResource: ...
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
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> BackupRun: ...

@typing.type_check_only
class BackupRunsListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> BackupRunsListResponse: ...

@typing.type_check_only
class DatabaseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> Database: ...

@typing.type_check_only
class DatabaseInstanceHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> DatabaseInstance: ...

@typing.type_check_only
class DatabasesListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> DatabasesListResponse: ...

@typing.type_check_only
class FlagsListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> FlagsListResponse: ...

@typing.type_check_only
class InstancesListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> InstancesListResponse: ...

@typing.type_check_only
class InstancesListServerCasResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> InstancesListServerCasResponse: ...

@typing.type_check_only
class OperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> Operation: ...

@typing.type_check_only
class OperationsListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> OperationsListResponse: ...

@typing.type_check_only
class SqlInstancesVerifyExternalSyncSettingsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> SqlInstancesVerifyExternalSyncSettingsResponse: ...

@typing.type_check_only
class SslCertHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> SslCert: ...

@typing.type_check_only
class SslCertsInsertResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> SslCertsInsertResponse: ...

@typing.type_check_only
class SslCertsListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> SslCertsListResponse: ...

@typing.type_check_only
class TiersListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> TiersListResponse: ...

@typing.type_check_only
class UsersListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> UsersListResponse: ...
