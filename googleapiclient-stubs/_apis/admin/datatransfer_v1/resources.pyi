import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class DataTransferResource(googleapiclient.discovery.Resource):
    class TransfersResource(googleapiclient.discovery.Resource):
        def insert(
            self, *, body: DataTransfer = ..., **kwargs: typing.Any
        ) -> DataTransferHttpRequest: ...
        def get(
            self, *, dataTransferId: str, **kwargs: typing.Any
        ) -> DataTransferHttpRequest: ...
        def list(
            self,
            *,
            status: str = ...,
            oldOwnerUserId: str = ...,
            newOwnerUserId: str = ...,
            pageToken: str = ...,
            customerId: str = ...,
            maxResults: int = ...,
            **kwargs: typing.Any
        ) -> DataTransfersListResponseHttpRequest: ...
    class ApplicationsResource(googleapiclient.discovery.Resource):
        def get(
            self, *, applicationId: str, **kwargs: typing.Any
        ) -> ApplicationHttpRequest: ...
        def list(
            self,
            *,
            pageToken: str = ...,
            customerId: str = ...,
            maxResults: int = ...,
            **kwargs: typing.Any
        ) -> ApplicationsListResponseHttpRequest: ...
    def transfers(self) -> TransfersResource: ...
    def applications(self) -> ApplicationsResource: ...

class DataTransferHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> DataTransfer: ...

class DataTransfersListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> DataTransfersListResponse: ...

class ApplicationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Application: ...

class ApplicationsListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ApplicationsListResponse: ...
