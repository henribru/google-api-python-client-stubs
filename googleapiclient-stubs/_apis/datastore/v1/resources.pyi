import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class DatastoreResource(googleapiclient.discovery.Resource):
    class ProjectsResource(googleapiclient.discovery.Resource):
        class IndexesResource(googleapiclient.discovery.Resource):
            def get(
                self, *, projectId: str, indexId: str, **kwargs: typing.Any
            ) -> GoogleDatastoreAdminV1IndexHttpRequest: ...
            def delete(
                self, *, projectId: str, indexId: str, **kwargs: typing.Any
            ) -> GoogleLongrunningOperationHttpRequest: ...
            def create(
                self,
                *,
                projectId: str,
                body: GoogleDatastoreAdminV1Index = ...,
                **kwargs: typing.Any
            ) -> GoogleLongrunningOperationHttpRequest: ...
            def list(
                self,
                *,
                projectId: str,
                filter: str = ...,
                pageToken: str = ...,
                pageSize: int = ...,
                **kwargs: typing.Any
            ) -> GoogleDatastoreAdminV1ListIndexesResponseHttpRequest: ...
        class OperationsResource(googleapiclient.discovery.Resource):
            def list(
                self,
                *,
                name: str,
                filter: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> GoogleLongrunningListOperationsResponseHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleLongrunningOperationHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def cancel(
                self, *, name: str, **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
        def commit(
            self, *, projectId: str, body: CommitRequest = ..., **kwargs: typing.Any
        ) -> CommitResponseHttpRequest: ...
        def import_(
            self,
            *,
            projectId: str,
            body: GoogleDatastoreAdminV1ImportEntitiesRequest = ...,
            **kwargs: typing.Any
        ) -> GoogleLongrunningOperationHttpRequest: ...
        def beginTransaction(
            self,
            *,
            projectId: str,
            body: BeginTransactionRequest = ...,
            **kwargs: typing.Any
        ) -> BeginTransactionResponseHttpRequest: ...
        def runQuery(
            self, *, projectId: str, body: RunQueryRequest = ..., **kwargs: typing.Any
        ) -> RunQueryResponseHttpRequest: ...
        def reserveIds(
            self, *, projectId: str, body: ReserveIdsRequest = ..., **kwargs: typing.Any
        ) -> ReserveIdsResponseHttpRequest: ...
        def lookup(
            self, *, projectId: str, body: LookupRequest = ..., **kwargs: typing.Any
        ) -> LookupResponseHttpRequest: ...
        def rollback(
            self, *, projectId: str, body: RollbackRequest = ..., **kwargs: typing.Any
        ) -> RollbackResponseHttpRequest: ...
        def allocateIds(
            self,
            *,
            projectId: str,
            body: AllocateIdsRequest = ...,
            **kwargs: typing.Any
        ) -> AllocateIdsResponseHttpRequest: ...
        def export(
            self,
            *,
            projectId: str,
            body: GoogleDatastoreAdminV1ExportEntitiesRequest = ...,
            **kwargs: typing.Any
        ) -> GoogleLongrunningOperationHttpRequest: ...
        def indexes(self) -> IndexesResource: ...
        def operations(self) -> OperationsResource: ...
    def projects(self) -> ProjectsResource: ...

class GoogleDatastoreAdminV1ListIndexesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleDatastoreAdminV1ListIndexesResponse: ...

class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Empty: ...

class CommitResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> CommitResponse: ...

class LookupResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> LookupResponse: ...

class ReserveIdsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ReserveIdsResponse: ...

class GoogleDatastoreAdminV1IndexHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleDatastoreAdminV1Index: ...

class RunQueryResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> RunQueryResponse: ...

class GoogleLongrunningListOperationsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleLongrunningListOperationsResponse: ...

class RollbackResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> RollbackResponse: ...

class BeginTransactionResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> BeginTransactionResponse: ...

class GoogleLongrunningOperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleLongrunningOperation: ...

class AllocateIdsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> AllocateIdsResponse: ...
