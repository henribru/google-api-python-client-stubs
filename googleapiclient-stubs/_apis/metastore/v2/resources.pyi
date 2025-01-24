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
                        body: GoogleCloudMetastoreV2Backup = ...,
                        backupId: str = ...,
                        requestId: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def delete(
                        self, *, name: str, requestId: str = ..., **kwargs: typing.Any
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleCloudMetastoreV2BackupHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str = ...,
                        orderBy: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudMetastoreV2ListBackupsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudMetastoreV2ListBackupsResponseHttpRequest,
                        previous_response: GoogleCloudMetastoreV2ListBackupsResponse,
                    ) -> (
                        GoogleCloudMetastoreV2ListBackupsResponseHttpRequest | None
                    ): ...

                def alterLocation(
                    self,
                    *,
                    service: str,
                    body: GoogleCloudMetastoreV2AlterMetadataResourceLocationRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def alterTableProperties(
                    self,
                    *,
                    service: str,
                    body: GoogleCloudMetastoreV2AlterTablePropertiesRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudMetastoreV2Service = ...,
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
                    body: GoogleCloudMetastoreV2ExportMetadataRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudMetastoreV2ServiceHttpRequest: ...
                def importMetadata(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudMetastoreV2ImportMetadataRequest = ...,
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
                ) -> GoogleCloudMetastoreV2ListServicesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudMetastoreV2ListServicesResponseHttpRequest,
                    previous_response: GoogleCloudMetastoreV2ListServicesResponse,
                ) -> GoogleCloudMetastoreV2ListServicesResponseHttpRequest | None: ...
                def moveTableToDatabase(
                    self,
                    *,
                    service: str,
                    body: GoogleCloudMetastoreV2MoveTableToDatabaseRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudMetastoreV2Service = ...,
                    requestId: str = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def queryMetadata(
                    self,
                    *,
                    service: str,
                    body: GoogleCloudMetastoreV2QueryMetadataRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def restore(
                    self,
                    *,
                    service: str,
                    body: GoogleCloudMetastoreV2RestoreServiceRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def backups(self) -> BackupsResource: ...

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
class GoogleCloudMetastoreV2BackupHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudMetastoreV2Backup: ...

@typing.type_check_only
class GoogleCloudMetastoreV2ListBackupsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudMetastoreV2ListBackupsResponse: ...

@typing.type_check_only
class GoogleCloudMetastoreV2ListServicesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudMetastoreV2ListServicesResponse: ...

@typing.type_check_only
class GoogleCloudMetastoreV2ServiceHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudMetastoreV2Service: ...

@typing.type_check_only
class GoogleLongrunningOperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleLongrunningOperation: ...
