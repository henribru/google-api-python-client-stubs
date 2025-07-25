import collections.abc
import typing

import httplib2
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http

from .schemas import *

_list = list

@typing.type_check_only
class FirestoreResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class ProjectsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class DatabasesResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class BackupSchedulesResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleFirestoreAdminV1BackupSchedule = ...,
                    **kwargs: typing.Any,
                ) -> GoogleFirestoreAdminV1BackupScheduleHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleFirestoreAdminV1BackupScheduleHttpRequest: ...
                def list(
                    self, *, parent: str, **kwargs: typing.Any
                ) -> GoogleFirestoreAdminV1ListBackupSchedulesResponseHttpRequest: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleFirestoreAdminV1BackupSchedule = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleFirestoreAdminV1BackupScheduleHttpRequest: ...

            @typing.type_check_only
            class CollectionGroupsResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class FieldsResource(googleapiclient.discovery.Resource):
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleFirestoreAdminV1FieldHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleFirestoreAdminV1ListFieldsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: GoogleFirestoreAdminV1ListFieldsResponseHttpRequest,
                        previous_response: GoogleFirestoreAdminV1ListFieldsResponse,
                    ) -> GoogleFirestoreAdminV1ListFieldsResponseHttpRequest | None: ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: GoogleFirestoreAdminV1Field = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleLongrunningOperationHttpRequest: ...

                @typing.type_check_only
                class IndexesResource(googleapiclient.discovery.Resource):
                    def create(
                        self,
                        *,
                        parent: str,
                        body: GoogleFirestoreAdminV1Index = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> EmptyHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleFirestoreAdminV1IndexHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleFirestoreAdminV1ListIndexesResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: GoogleFirestoreAdminV1ListIndexesResponseHttpRequest,
                        previous_response: GoogleFirestoreAdminV1ListIndexesResponse,
                    ) -> (
                        GoogleFirestoreAdminV1ListIndexesResponseHttpRequest | None
                    ): ...

                def fields(self) -> FieldsResource: ...
                def indexes(self) -> IndexesResource: ...

            @typing.type_check_only
            class DocumentsResource(googleapiclient.discovery.Resource):
                def batchGet(
                    self,
                    *,
                    database: str,
                    body: BatchGetDocumentsRequest = ...,
                    **kwargs: typing.Any,
                ) -> BatchGetDocumentsResponseHttpRequest: ...
                def batchWrite(
                    self,
                    *,
                    database: str,
                    body: BatchWriteRequest = ...,
                    **kwargs: typing.Any,
                ) -> BatchWriteResponseHttpRequest: ...
                def beginTransaction(
                    self,
                    *,
                    database: str,
                    body: BeginTransactionRequest = ...,
                    **kwargs: typing.Any,
                ) -> BeginTransactionResponseHttpRequest: ...
                def commit(
                    self,
                    *,
                    database: str,
                    body: CommitRequest = ...,
                    **kwargs: typing.Any,
                ) -> CommitResponseHttpRequest: ...
                def createDocument(
                    self,
                    *,
                    parent: str,
                    collectionId: str,
                    body: Document = ...,
                    documentId: str = ...,
                    mask_fieldPaths: str | _list[str] = ...,
                    **kwargs: typing.Any,
                ) -> DocumentHttpRequest: ...
                def delete(
                    self,
                    *,
                    name: str,
                    currentDocument_exists: bool = ...,
                    currentDocument_updateTime: str = ...,
                    **kwargs: typing.Any,
                ) -> EmptyHttpRequest: ...
                def get(
                    self,
                    *,
                    name: str,
                    mask_fieldPaths: str | _list[str] = ...,
                    readTime: str = ...,
                    transaction: str = ...,
                    **kwargs: typing.Any,
                ) -> DocumentHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    collectionId: str,
                    mask_fieldPaths: str | _list[str] = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    readTime: str = ...,
                    showMissing: bool = ...,
                    transaction: str = ...,
                    **kwargs: typing.Any,
                ) -> ListDocumentsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListDocumentsResponseHttpRequest,
                    previous_response: ListDocumentsResponse,
                ) -> ListDocumentsResponseHttpRequest | None: ...
                def listCollectionIds(
                    self,
                    *,
                    parent: str,
                    body: ListCollectionIdsRequest = ...,
                    **kwargs: typing.Any,
                ) -> ListCollectionIdsResponseHttpRequest: ...
                def listCollectionIds_next(
                    self,
                    previous_request: ListCollectionIdsResponseHttpRequest,
                    previous_response: ListCollectionIdsResponse,
                ) -> ListCollectionIdsResponseHttpRequest | None: ...
                def listDocuments(
                    self,
                    *,
                    parent: str,
                    collectionId: str,
                    mask_fieldPaths: str | _list[str] = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    readTime: str = ...,
                    showMissing: bool = ...,
                    transaction: str = ...,
                    **kwargs: typing.Any,
                ) -> ListDocumentsResponseHttpRequest: ...
                def listDocuments_next(
                    self,
                    previous_request: ListDocumentsResponseHttpRequest,
                    previous_response: ListDocumentsResponse,
                ) -> ListDocumentsResponseHttpRequest | None: ...
                def listen(
                    self,
                    *,
                    database: str,
                    body: ListenRequest = ...,
                    **kwargs: typing.Any,
                ) -> ListenResponseHttpRequest: ...
                def partitionQuery(
                    self,
                    *,
                    parent: str,
                    body: PartitionQueryRequest = ...,
                    **kwargs: typing.Any,
                ) -> PartitionQueryResponseHttpRequest: ...
                def partitionQuery_next(
                    self,
                    previous_request: PartitionQueryResponseHttpRequest,
                    previous_response: PartitionQueryResponse,
                ) -> PartitionQueryResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: Document = ...,
                    currentDocument_exists: bool = ...,
                    currentDocument_updateTime: str = ...,
                    mask_fieldPaths: str | _list[str] = ...,
                    updateMask_fieldPaths: str | _list[str] = ...,
                    **kwargs: typing.Any,
                ) -> DocumentHttpRequest: ...
                def rollback(
                    self,
                    *,
                    database: str,
                    body: RollbackRequest = ...,
                    **kwargs: typing.Any,
                ) -> EmptyHttpRequest: ...
                def runAggregationQuery(
                    self,
                    *,
                    parent: str,
                    body: RunAggregationQueryRequest = ...,
                    **kwargs: typing.Any,
                ) -> RunAggregationQueryResponseHttpRequest: ...
                def runQuery(
                    self,
                    *,
                    parent: str,
                    body: RunQueryRequest = ...,
                    **kwargs: typing.Any,
                ) -> RunQueryResponseHttpRequest: ...
                def write(
                    self,
                    *,
                    database: str,
                    body: WriteRequest = ...,
                    **kwargs: typing.Any,
                ) -> WriteResponseHttpRequest: ...

            @typing.type_check_only
            class OperationsResource(googleapiclient.discovery.Resource):
                def cancel(
                    self,
                    *,
                    name: str,
                    body: GoogleLongrunningCancelOperationRequest = ...,
                    **kwargs: typing.Any,
                ) -> EmptyHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def list(
                    self,
                    *,
                    name: str,
                    filter: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningListOperationsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleLongrunningListOperationsResponseHttpRequest,
                    previous_response: GoogleLongrunningListOperationsResponse,
                ) -> GoogleLongrunningListOperationsResponseHttpRequest | None: ...

            @typing.type_check_only
            class UserCredsResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleFirestoreAdminV1UserCreds = ...,
                    userCredsId: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleFirestoreAdminV1UserCredsHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def disable(
                    self,
                    *,
                    name: str,
                    body: GoogleFirestoreAdminV1DisableUserCredsRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleFirestoreAdminV1UserCredsHttpRequest: ...
                def enable(
                    self,
                    *,
                    name: str,
                    body: GoogleFirestoreAdminV1EnableUserCredsRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleFirestoreAdminV1UserCredsHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleFirestoreAdminV1UserCredsHttpRequest: ...
                def list(
                    self, *, parent: str, **kwargs: typing.Any
                ) -> GoogleFirestoreAdminV1ListUserCredsResponseHttpRequest: ...
                def resetPassword(
                    self,
                    *,
                    name: str,
                    body: GoogleFirestoreAdminV1ResetUserPasswordRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleFirestoreAdminV1UserCredsHttpRequest: ...

            def bulkDeleteDocuments(
                self,
                *,
                name: str,
                body: GoogleFirestoreAdminV1BulkDeleteDocumentsRequest = ...,
                **kwargs: typing.Any,
            ) -> GoogleLongrunningOperationHttpRequest: ...
            def clone(
                self,
                *,
                parent: str,
                body: GoogleFirestoreAdminV1CloneDatabaseRequest = ...,
                **kwargs: typing.Any,
            ) -> GoogleLongrunningOperationHttpRequest: ...
            def create(
                self,
                *,
                parent: str,
                body: GoogleFirestoreAdminV1Database = ...,
                databaseId: str = ...,
                **kwargs: typing.Any,
            ) -> GoogleLongrunningOperationHttpRequest: ...
            def delete(
                self, *, name: str, etag: str = ..., **kwargs: typing.Any
            ) -> GoogleLongrunningOperationHttpRequest: ...
            def exportDocuments(
                self,
                *,
                name: str,
                body: GoogleFirestoreAdminV1ExportDocumentsRequest = ...,
                **kwargs: typing.Any,
            ) -> GoogleLongrunningOperationHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleFirestoreAdminV1DatabaseHttpRequest: ...
            def importDocuments(
                self,
                *,
                name: str,
                body: GoogleFirestoreAdminV1ImportDocumentsRequest = ...,
                **kwargs: typing.Any,
            ) -> GoogleLongrunningOperationHttpRequest: ...
            def list(
                self, *, parent: str, showDeleted: bool = ..., **kwargs: typing.Any
            ) -> GoogleFirestoreAdminV1ListDatabasesResponseHttpRequest: ...
            def patch(
                self,
                *,
                name: str,
                body: GoogleFirestoreAdminV1Database = ...,
                updateMask: str = ...,
                **kwargs: typing.Any,
            ) -> GoogleLongrunningOperationHttpRequest: ...
            def restore(
                self,
                *,
                parent: str,
                body: GoogleFirestoreAdminV1RestoreDatabaseRequest = ...,
                **kwargs: typing.Any,
            ) -> GoogleLongrunningOperationHttpRequest: ...
            def backupSchedules(self) -> BackupSchedulesResource: ...
            def collectionGroups(self) -> CollectionGroupsResource: ...
            def documents(self) -> DocumentsResource: ...
            def operations(self) -> OperationsResource: ...
            def userCreds(self) -> UserCredsResource: ...

        @typing.type_check_only
        class LocationsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class BackupsResource(googleapiclient.discovery.Resource):
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleFirestoreAdminV1BackupHttpRequest: ...
                def list(
                    self, *, parent: str, filter: str = ..., **kwargs: typing.Any
                ) -> GoogleFirestoreAdminV1ListBackupsResponseHttpRequest: ...

            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> LocationHttpRequest: ...
            def list(
                self,
                *,
                name: str,
                extraLocationTypes: str | _list[str] = ...,
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
            def backups(self) -> BackupsResource: ...

        def databases(self) -> DatabasesResource: ...
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
class BatchGetDocumentsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> BatchGetDocumentsResponse: ...

@typing.type_check_only
class BatchWriteResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> BatchWriteResponse: ...

@typing.type_check_only
class BeginTransactionResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> BeginTransactionResponse: ...

@typing.type_check_only
class CommitResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> CommitResponse: ...

@typing.type_check_only
class DocumentHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Document: ...

@typing.type_check_only
class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Empty: ...

@typing.type_check_only
class GoogleFirestoreAdminV1BackupHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleFirestoreAdminV1Backup: ...

@typing.type_check_only
class GoogleFirestoreAdminV1BackupScheduleHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleFirestoreAdminV1BackupSchedule: ...

@typing.type_check_only
class GoogleFirestoreAdminV1DatabaseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleFirestoreAdminV1Database: ...

@typing.type_check_only
class GoogleFirestoreAdminV1FieldHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleFirestoreAdminV1Field: ...

@typing.type_check_only
class GoogleFirestoreAdminV1IndexHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleFirestoreAdminV1Index: ...

@typing.type_check_only
class GoogleFirestoreAdminV1ListBackupSchedulesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleFirestoreAdminV1ListBackupSchedulesResponse: ...

@typing.type_check_only
class GoogleFirestoreAdminV1ListBackupsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleFirestoreAdminV1ListBackupsResponse: ...

@typing.type_check_only
class GoogleFirestoreAdminV1ListDatabasesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleFirestoreAdminV1ListDatabasesResponse: ...

@typing.type_check_only
class GoogleFirestoreAdminV1ListFieldsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleFirestoreAdminV1ListFieldsResponse: ...

@typing.type_check_only
class GoogleFirestoreAdminV1ListIndexesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleFirestoreAdminV1ListIndexesResponse: ...

@typing.type_check_only
class GoogleFirestoreAdminV1ListUserCredsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleFirestoreAdminV1ListUserCredsResponse: ...

@typing.type_check_only
class GoogleFirestoreAdminV1UserCredsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleFirestoreAdminV1UserCreds: ...

@typing.type_check_only
class GoogleLongrunningListOperationsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleLongrunningListOperationsResponse: ...

@typing.type_check_only
class GoogleLongrunningOperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleLongrunningOperation: ...

@typing.type_check_only
class ListCollectionIdsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListCollectionIdsResponse: ...

@typing.type_check_only
class ListDocumentsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListDocumentsResponse: ...

@typing.type_check_only
class ListLocationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListLocationsResponse: ...

@typing.type_check_only
class ListenResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListenResponse: ...

@typing.type_check_only
class LocationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Location: ...

@typing.type_check_only
class PartitionQueryResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> PartitionQueryResponse: ...

@typing.type_check_only
class RunAggregationQueryResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> RunAggregationQueryResponse: ...

@typing.type_check_only
class RunQueryResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> RunQueryResponse: ...

@typing.type_check_only
class WriteResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> WriteResponse: ...
