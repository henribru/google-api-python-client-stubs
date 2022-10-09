import collections.abc
import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

_list = list

@typing.type_check_only
class StoragetransferResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class GoogleServiceAccountsResource(googleapiclient.discovery.Resource):
        def get(
            self, *, projectId: str, **kwargs: typing.Any
        ) -> GoogleServiceAccountHttpRequest: ...

    @typing.type_check_only
    class ProjectsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class AgentPoolsResource(googleapiclient.discovery.Resource):
            def create(
                self,
                *,
                projectId: str,
                body: AgentPool = ...,
                agentPoolId: str = ...,
                **kwargs: typing.Any
            ) -> AgentPoolHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> AgentPoolHttpRequest: ...
            def list(
                self,
                *,
                projectId: str,
                filter: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> ListAgentPoolsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListAgentPoolsResponseHttpRequest,
                previous_response: ListAgentPoolsResponse,
            ) -> ListAgentPoolsResponseHttpRequest | None: ...
            def patch(
                self,
                *,
                name: str,
                body: AgentPool = ...,
                updateMask: str = ...,
                **kwargs: typing.Any
            ) -> AgentPoolHttpRequest: ...

        def agentPools(self) -> AgentPoolsResource: ...

    @typing.type_check_only
    class TransferJobsResource(googleapiclient.discovery.Resource):
        def create(
            self, *, body: TransferJob = ..., **kwargs: typing.Any
        ) -> TransferJobHttpRequest: ...
        def delete(
            self, *, jobName: str, projectId: str, **kwargs: typing.Any
        ) -> EmptyHttpRequest: ...
        def get(
            self, *, jobName: str, projectId: str, **kwargs: typing.Any
        ) -> TransferJobHttpRequest: ...
        def list(
            self,
            *,
            filter: str,
            pageSize: int = ...,
            pageToken: str = ...,
            **kwargs: typing.Any
        ) -> ListTransferJobsResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: ListTransferJobsResponseHttpRequest,
            previous_response: ListTransferJobsResponse,
        ) -> ListTransferJobsResponseHttpRequest | None: ...
        def patch(
            self,
            *,
            jobName: str,
            body: UpdateTransferJobRequest = ...,
            **kwargs: typing.Any
        ) -> TransferJobHttpRequest: ...
        def run(
            self,
            *,
            jobName: str,
            body: RunTransferJobRequest = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...

    @typing.type_check_only
    class TransferOperationsResource(googleapiclient.discovery.Resource):
        def cancel(
            self, *, name: str, body: CancelOperationRequest = ..., **kwargs: typing.Any
        ) -> EmptyHttpRequest: ...
        def get(self, *, name: str, **kwargs: typing.Any) -> OperationHttpRequest: ...
        def list(
            self,
            *,
            name: str,
            filter: str,
            pageSize: int = ...,
            pageToken: str = ...,
            **kwargs: typing.Any
        ) -> ListOperationsResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: ListOperationsResponseHttpRequest,
            previous_response: ListOperationsResponse,
        ) -> ListOperationsResponseHttpRequest | None: ...
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
    def googleServiceAccounts(self) -> GoogleServiceAccountsResource: ...
    def projects(self) -> ProjectsResource: ...
    def transferJobs(self) -> TransferJobsResource: ...
    def transferOperations(self) -> TransferOperationsResource: ...

@typing.type_check_only
class AgentPoolHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> AgentPool: ...

@typing.type_check_only
class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Empty: ...

@typing.type_check_only
class GoogleServiceAccountHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleServiceAccount: ...

@typing.type_check_only
class ListAgentPoolsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListAgentPoolsResponse: ...

@typing.type_check_only
class ListOperationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListOperationsResponse: ...

@typing.type_check_only
class ListTransferJobsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListTransferJobsResponse: ...

@typing.type_check_only
class OperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Operation: ...

@typing.type_check_only
class TransferJobHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> TransferJob: ...
