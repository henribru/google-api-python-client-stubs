import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class StoragetransferResource(googleapiclient.discovery.Resource):
    class TransferOperationsResource(googleapiclient.discovery.Resource):
        def list(
            self,
            *,
            name: str,
            pageToken: str = ...,
            pageSize: int = ...,
            filter: str = ...,
            **kwargs: typing.Any
        ) -> ListOperationsResponseHttpRequest: ...
        def cancel(self, *, name: str, **kwargs: typing.Any) -> EmptyHttpRequest: ...
        def get(self, *, name: str, **kwargs: typing.Any) -> OperationHttpRequest: ...
        def pause(
            self,
            *,
            name: str,
            body: PauseTransferOperationRequest = ...,
            **kwargs: typing.Any
        ) -> EmptyHttpRequest: ...
        def resume(
            self,
            *,
            name: str,
            body: ResumeTransferOperationRequest = ...,
            **kwargs: typing.Any
        ) -> EmptyHttpRequest: ...
    class TransferJobsResource(googleapiclient.discovery.Resource):
        def create(
            self, *, body: TransferJob = ..., **kwargs: typing.Any
        ) -> TransferJobHttpRequest: ...
        def list(
            self,
            *,
            filter: str = ...,
            pageSize: int = ...,
            pageToken: str = ...,
            **kwargs: typing.Any
        ) -> ListTransferJobsResponseHttpRequest: ...
        def patch(
            self,
            *,
            jobName: str,
            body: UpdateTransferJobRequest = ...,
            **kwargs: typing.Any
        ) -> TransferJobHttpRequest: ...
        def get(
            self, *, jobName: str, projectId: str = ..., **kwargs: typing.Any
        ) -> TransferJobHttpRequest: ...
    class GoogleServiceAccountsResource(googleapiclient.discovery.Resource):
        def get(
            self, *, projectId: str, **kwargs: typing.Any
        ) -> GoogleServiceAccountHttpRequest: ...
    def transferOperations(self) -> TransferOperationsResource: ...
    def transferJobs(self) -> TransferJobsResource: ...
    def googleServiceAccounts(self) -> GoogleServiceAccountsResource: ...

class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Empty: ...

class OperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Operation: ...

class TransferJobHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> TransferJob: ...

class ListOperationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListOperationsResponse: ...

class ListTransferJobsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListTransferJobsResponse: ...

class GoogleServiceAccountHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleServiceAccount: ...
