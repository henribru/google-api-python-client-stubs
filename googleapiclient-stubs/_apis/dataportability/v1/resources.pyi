import collections.abc
import typing

import httplib2
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http

from .schemas import *

_list = list

@typing.type_check_only
class DataPortabilityResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class ArchiveJobsResource(googleapiclient.discovery.Resource):
        def getPortabilityArchiveState(
            self, *, name: str, **kwargs: typing.Any
        ) -> PortabilityArchiveStateHttpRequest: ...
        def retry(
            self,
            *,
            name: str,
            body: RetryPortabilityArchiveRequest = ...,
            **kwargs: typing.Any,
        ) -> RetryPortabilityArchiveResponseHttpRequest: ...

    @typing.type_check_only
    class AuthorizationResource(googleapiclient.discovery.Resource):
        def reset(
            self, *, body: ResetAuthorizationRequest = ..., **kwargs: typing.Any
        ) -> EmptyHttpRequest: ...

    @typing.type_check_only
    class PortabilityArchiveResource(googleapiclient.discovery.Resource):
        def initiate(
            self, *, body: InitiatePortabilityArchiveRequest = ..., **kwargs: typing.Any
        ) -> InitiatePortabilityArchiveResponseHttpRequest: ...

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
    def archiveJobs(self) -> ArchiveJobsResource: ...
    def authorization(self) -> AuthorizationResource: ...
    def portabilityArchive(self) -> PortabilityArchiveResource: ...

@typing.type_check_only
class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Empty: ...

@typing.type_check_only
class InitiatePortabilityArchiveResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> InitiatePortabilityArchiveResponse: ...

@typing.type_check_only
class PortabilityArchiveStateHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> PortabilityArchiveState: ...

@typing.type_check_only
class RetryPortabilityArchiveResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> RetryPortabilityArchiveResponse: ...
