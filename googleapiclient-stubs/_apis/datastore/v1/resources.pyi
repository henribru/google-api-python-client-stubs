import collections.abc
import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

_list = list

@typing.type_check_only
class DatastoreResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class ProjectsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class IndexesResource(googleapiclient.discovery.Resource):
            def create(
                self,
                *,
                projectId: str,
                body: GoogleDatastoreAdminV1Index = ...,
                **kwargs: typing.Any
            ) -> GoogleLongrunningOperationHttpRequest: ...
            def delete(
                self, *, projectId: str, indexId: str, **kwargs: typing.Any
            ) -> GoogleLongrunningOperationHttpRequest: ...
            def get(
                self, *, projectId: str, indexId: str, **kwargs: typing.Any
            ) -> GoogleDatastoreAdminV1IndexHttpRequest: ...
            def list(
                self,
                *,
                projectId: str,
                filter: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> GoogleDatastoreAdminV1ListIndexesResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: GoogleDatastoreAdminV1ListIndexesResponseHttpRequest,
                previous_response: GoogleDatastoreAdminV1ListIndexesResponse,
            ) -> GoogleDatastoreAdminV1ListIndexesResponseHttpRequest | None: ...

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
            ) -> GoogleLongrunningOperationHttpRequest: ...
            def list(
                self,
                *,
                name: str,
                filter: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> GoogleLongrunningListOperationsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: GoogleLongrunningListOperationsResponseHttpRequest,
                previous_response: GoogleLongrunningListOperationsResponse,
            ) -> GoogleLongrunningListOperationsResponseHttpRequest | None: ...

        def allocateIds(
            self,
            *,
            projectId: str,
            body: AllocateIdsRequest = ...,
            **kwargs: typing.Any
        ) -> AllocateIdsResponseHttpRequest: ...
        def beginTransaction(
            self,
            *,
            projectId: str,
            body: BeginTransactionRequest = ...,
            **kwargs: typing.Any
        ) -> BeginTransactionResponseHttpRequest: ...
        def commit(
            self, *, projectId: str, body: CommitRequest = ..., **kwargs: typing.Any
        ) -> CommitResponseHttpRequest: ...
        def export(
            self,
            *,
            projectId: str,
            body: GoogleDatastoreAdminV1ExportEntitiesRequest = ...,
            **kwargs: typing.Any
        ) -> GoogleLongrunningOperationHttpRequest: ...
        def import_(
            self,
            *,
            projectId: str,
            body: GoogleDatastoreAdminV1ImportEntitiesRequest = ...,
            **kwargs: typing.Any
        ) -> GoogleLongrunningOperationHttpRequest: ...
        def lookup(
            self, *, projectId: str, body: LookupRequest = ..., **kwargs: typing.Any
        ) -> LookupResponseHttpRequest: ...
        def reserveIds(
            self, *, projectId: str, body: ReserveIdsRequest = ..., **kwargs: typing.Any
        ) -> ReserveIdsResponseHttpRequest: ...
        def rollback(
            self, *, projectId: str, body: RollbackRequest = ..., **kwargs: typing.Any
        ) -> RollbackResponseHttpRequest: ...
        def runQuery(
            self, *, projectId: str, body: RunQueryRequest = ..., **kwargs: typing.Any
        ) -> RunQueryResponseHttpRequest: ...
        def indexes(self) -> IndexesResource: ...
        def operations(self) -> OperationsResource: ...

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
        | None = ...,
    ) -> googleapiclient.http.BatchHttpRequest: ...
    def projects(self) -> ProjectsResource: ...

@typing.type_check_only
class AllocateIdsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> AllocateIdsResponse: ...

@typing.type_check_only
class BeginTransactionResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> BeginTransactionResponse: ...

@typing.type_check_only
class CommitResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> CommitResponse: ...

@typing.type_check_only
class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Empty: ...

@typing.type_check_only
class GoogleDatastoreAdminV1IndexHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleDatastoreAdminV1Index: ...

@typing.type_check_only
class GoogleDatastoreAdminV1ListIndexesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleDatastoreAdminV1ListIndexesResponse: ...

@typing.type_check_only
class GoogleLongrunningListOperationsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleLongrunningListOperationsResponse: ...

@typing.type_check_only
class GoogleLongrunningOperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleLongrunningOperation: ...

@typing.type_check_only
class LookupResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> LookupResponse: ...

@typing.type_check_only
class ReserveIdsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ReserveIdsResponse: ...

@typing.type_check_only
class RollbackResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> RollbackResponse: ...

@typing.type_check_only
class RunQueryResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> RunQueryResponse: ...
