import collections.abc
import typing

import httplib2
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http

from .schemas import *

_list = list

@typing.type_check_only
class DataprocMetastoreResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class ProjectsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class LocationsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class ServicesResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class BackupsResource(googleapiclient.discovery.Resource):
                    def create(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudMetastoreV2betaBackup = ...,
                        backupId: str = ...,
                        requestId: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def delete(
                        self, *, name: str, requestId: str = ..., **kwargs: typing.Any
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleCloudMetastoreV2betaBackupHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str = ...,
                        orderBy: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudMetastoreV2betaListBackupsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudMetastoreV2betaListBackupsResponseHttpRequest,
                        previous_response: GoogleCloudMetastoreV2betaListBackupsResponse,
                    ) -> (
                        GoogleCloudMetastoreV2betaListBackupsResponseHttpRequest | None
                    ): ...

                @typing.type_check_only
                class MigrationExecutionsResource(googleapiclient.discovery.Resource):
                    def delete(
                        self, *, name: str, requestId: str = ..., **kwargs: typing.Any
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleCloudMetastoreV2betaMigrationExecutionHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str = ...,
                        orderBy: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudMetastoreV2betaListMigrationExecutionsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudMetastoreV2betaListMigrationExecutionsResponseHttpRequest,
                        previous_response: GoogleCloudMetastoreV2betaListMigrationExecutionsResponse,
                    ) -> (
                        GoogleCloudMetastoreV2betaListMigrationExecutionsResponseHttpRequest
                        | None
                    ): ...

                def alterLocation(
                    self,
                    *,
                    service: str,
                    body: GoogleCloudMetastoreV2betaAlterMetadataResourceLocationRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def alterTableProperties(
                    self,
                    *,
                    service: str,
                    body: GoogleCloudMetastoreV2betaAlterTablePropertiesRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def cancelMigration(
                    self,
                    *,
                    service: str,
                    body: GoogleCloudMetastoreV2betaCancelMigrationRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def completeMigration(
                    self,
                    *,
                    service: str,
                    body: GoogleCloudMetastoreV2betaCompleteMigrationRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudMetastoreV2betaService = ...,
                    requestId: str = ...,
                    serviceId: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def delete(
                    self, *, name: str, requestId: str = ..., **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def exportMetadata(
                    self,
                    *,
                    service: str,
                    body: GoogleCloudMetastoreV2betaExportMetadataRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudMetastoreV2betaServiceHttpRequest: ...
                def importMetadata(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudMetastoreV2betaImportMetadataRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudMetastoreV2betaListServicesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudMetastoreV2betaListServicesResponseHttpRequest,
                    previous_response: GoogleCloudMetastoreV2betaListServicesResponse,
                ) -> (
                    GoogleCloudMetastoreV2betaListServicesResponseHttpRequest | None
                ): ...
                def moveTableToDatabase(
                    self,
                    *,
                    service: str,
                    body: GoogleCloudMetastoreV2betaMoveTableToDatabaseRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudMetastoreV2betaService = ...,
                    requestId: str = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def queryMetadata(
                    self,
                    *,
                    service: str,
                    body: GoogleCloudMetastoreV2betaQueryMetadataRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def removeIamPolicy(
                    self,
                    *,
                    resource: str,
                    body: GoogleCloudMetastoreV2betaRemoveIamPolicyRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudMetastoreV2betaRemoveIamPolicyResponseHttpRequest: ...
                def restore(
                    self,
                    *,
                    service: str,
                    body: GoogleCloudMetastoreV2betaRestoreServiceRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def startMigration(
                    self,
                    *,
                    service: str,
                    body: GoogleCloudMetastoreV2betaStartMigrationRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def backups(self) -> BackupsResource: ...
                def migrationExecutions(self) -> MigrationExecutionsResource: ...

            def services(self) -> ServicesResource: ...

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
class GoogleCloudMetastoreV2betaBackupHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudMetastoreV2betaBackup: ...

@typing.type_check_only
class GoogleCloudMetastoreV2betaListBackupsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudMetastoreV2betaListBackupsResponse: ...

@typing.type_check_only
class GoogleCloudMetastoreV2betaListMigrationExecutionsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudMetastoreV2betaListMigrationExecutionsResponse: ...

@typing.type_check_only
class GoogleCloudMetastoreV2betaListServicesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudMetastoreV2betaListServicesResponse: ...

@typing.type_check_only
class GoogleCloudMetastoreV2betaMigrationExecutionHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudMetastoreV2betaMigrationExecution: ...

@typing.type_check_only
class GoogleCloudMetastoreV2betaRemoveIamPolicyResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudMetastoreV2betaRemoveIamPolicyResponse: ...

@typing.type_check_only
class GoogleCloudMetastoreV2betaServiceHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudMetastoreV2betaService: ...

@typing.type_check_only
class GoogleLongrunningOperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleLongrunningOperation: ...
