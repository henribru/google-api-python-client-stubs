import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class DatastoreResource(googleapiclient.discovery.Resource):
    class ProjectsResource(googleapiclient.discovery.Resource):
        def reserveIds(
            self, *, projectId: str, body: ReserveIdsRequest = ..., **kwargs: typing.Any
        ) -> ReserveIdsResponseHttpRequest: ...
        def runQuery(
            self, *, projectId: str, body: RunQueryRequest = ..., **kwargs: typing.Any
        ) -> RunQueryResponseHttpRequest: ...
        def beginTransaction(
            self,
            *,
            projectId: str,
            body: BeginTransactionRequest = ...,
            **kwargs: typing.Any
        ) -> BeginTransactionResponseHttpRequest: ...
        def rollback(
            self, *, projectId: str, body: RollbackRequest = ..., **kwargs: typing.Any
        ) -> RollbackResponseHttpRequest: ...
        def commit(
            self, *, projectId: str, body: CommitRequest = ..., **kwargs: typing.Any
        ) -> CommitResponseHttpRequest: ...
        def allocateIds(
            self,
            *,
            projectId: str,
            body: AllocateIdsRequest = ...,
            **kwargs: typing.Any
        ) -> AllocateIdsResponseHttpRequest: ...
        def lookup(
            self, *, projectId: str, body: LookupRequest = ..., **kwargs: typing.Any
        ) -> LookupResponseHttpRequest: ...
    def projects(self) -> ProjectsResource: ...

class CommitResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> CommitResponse: ...

class RunQueryResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> RunQueryResponse: ...

class LookupResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> LookupResponse: ...

class RollbackResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> RollbackResponse: ...

class ReserveIdsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ReserveIdsResponse: ...

class BeginTransactionResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> BeginTransactionResponse: ...

class AllocateIdsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> AllocateIdsResponse: ...
