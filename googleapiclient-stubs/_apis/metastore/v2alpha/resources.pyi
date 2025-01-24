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
                        body: GoogleCloudMetastoreV2alphaBackup = ...,
                        backupId: str = ...,
                        requestId: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def delete(
                        self, *, name: str, requestId: str = ..., **kwargs: typing.Any
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleCloudMetastoreV2alphaBackupHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str = ...,
                        orderBy: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudMetastoreV2alphaListBackupsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudMetastoreV2alphaListBackupsResponseHttpRequest,
                        previous_response: GoogleCloudMetastoreV2alphaListBackupsResponse,
                    ) -> (
                        GoogleCloudMetastoreV2alphaListBackupsResponseHttpRequest | None
                    ): ...

                @typing.type_check_only
                class MigrationExecutionsResource(googleapiclient.discovery.Resource):
                    def delete(
                        self, *, name: str, requestId: str = ..., **kwargs: typing.Any
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleCloudMetastoreV2alphaMigrationExecutionHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str = ...,
                        orderBy: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudMetastoreV2alphaListMigrationExecutionsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudMetastoreV2alphaListMigrationExecutionsResponseHttpRequest,
                        previous_response: GoogleCloudMetastoreV2alphaListMigrationExecutionsResponse,
                    ) -> (
                        GoogleCloudMetastoreV2alphaListMigrationExecutionsResponseHttpRequest
                        | None
                    ): ...

                def alterLocation(
                    self,
                    *,
                    service: str,
                    body: GoogleCloudMetastoreV2alphaAlterMetadataResourceLocationRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def alterTableProperties(
                    self,
                    *,
                    service: str,
                    body: GoogleCloudMetastoreV2alphaAlterTablePropertiesRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def cancelMigration(
                    self,
                    *,
                    service: str,
                    body: GoogleCloudMetastoreV2alphaCancelMigrationRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def completeMigration(
                    self,
                    *,
                    service: str,
                    body: GoogleCloudMetastoreV2alphaCompleteMigrationRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudMetastoreV2alphaService = ...,
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
                    body: GoogleCloudMetastoreV2alphaExportMetadataRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudMetastoreV2alphaServiceHttpRequest: ...
                def importMetadata(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudMetastoreV2alphaImportMetadataRequest = ...,
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
                ) -> GoogleCloudMetastoreV2alphaListServicesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudMetastoreV2alphaListServicesResponseHttpRequest,
                    previous_response: GoogleCloudMetastoreV2alphaListServicesResponse,
                ) -> (
                    GoogleCloudMetastoreV2alphaListServicesResponseHttpRequest | None
                ): ...
                def moveTableToDatabase(
                    self,
                    *,
                    service: str,
                    body: GoogleCloudMetastoreV2alphaMoveTableToDatabaseRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudMetastoreV2alphaService = ...,
                    requestId: str = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def queryMetadata(
                    self,
                    *,
                    service: str,
                    body: GoogleCloudMetastoreV2alphaQueryMetadataRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def removeIamPolicy(
                    self,
                    *,
                    resource: str,
                    body: GoogleCloudMetastoreV2alphaRemoveIamPolicyRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudMetastoreV2alphaRemoveIamPolicyResponseHttpRequest: ...
                def restore(
                    self,
                    *,
                    service: str,
                    body: GoogleCloudMetastoreV2alphaRestoreServiceRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def startMigration(
                    self,
                    *,
                    service: str,
                    body: GoogleCloudMetastoreV2alphaStartMigrationRequest = ...,
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
class GoogleCloudMetastoreV2alphaBackupHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudMetastoreV2alphaBackup: ...

@typing.type_check_only
class GoogleCloudMetastoreV2alphaListBackupsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudMetastoreV2alphaListBackupsResponse: ...

@typing.type_check_only
class GoogleCloudMetastoreV2alphaListMigrationExecutionsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudMetastoreV2alphaListMigrationExecutionsResponse: ...

@typing.type_check_only
class GoogleCloudMetastoreV2alphaListServicesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudMetastoreV2alphaListServicesResponse: ...

@typing.type_check_only
class GoogleCloudMetastoreV2alphaMigrationExecutionHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudMetastoreV2alphaMigrationExecution: ...

@typing.type_check_only
class GoogleCloudMetastoreV2alphaRemoveIamPolicyResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudMetastoreV2alphaRemoveIamPolicyResponse: ...

@typing.type_check_only
class GoogleCloudMetastoreV2alphaServiceHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudMetastoreV2alphaService: ...

@typing.type_check_only
class GoogleLongrunningOperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleLongrunningOperation: ...
