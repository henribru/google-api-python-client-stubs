import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *
@typing.type_check_only
class DataTransferResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class ApplicationsResource(googleapiclient.discovery.Resource):
        def get(
            self, *, applicationId: str, **kwargs: typing.Any
        ) -> ApplicationHttpRequest: ...
        def list(
            self,
            *,
            customerId: str = ...,
            maxResults: int = ...,
            pageToken: str = ...,
            **kwargs: typing.Any
        ) -> ApplicationsListResponseHttpRequest: ...
    @typing.type_check_only
    class TransfersResource(googleapiclient.discovery.Resource):
        def get(
            self, *, dataTransferId: str, **kwargs: typing.Any
        ) -> DataTransferHttpRequest: ...
        def insert(
            self, *, body: DataTransfer = ..., **kwargs: typing.Any
        ) -> DataTransferHttpRequest: ...
        def list(
            self,
            *,
            customerId: str = ...,
            maxResults: int = ...,
            newOwnerUserId: str = ...,
            oldOwnerUserId: str = ...,
            pageToken: str = ...,
            status: str = ...,
            **kwargs: typing.Any
        ) -> DataTransfersListResponseHttpRequest: ...
    def applications(self) -> ApplicationsResource: ...
    def transfers(self) -> TransfersResource: ...

@typing.type_check_only
class ApplicationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> Application: ...

@typing.type_check_only
class ApplicationsListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> ApplicationsListResponse: ...

@typing.type_check_only
class DataTransferHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> DataTransfer: ...

@typing.type_check_only
class DataTransfersListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> DataTransfersListResponse: ...
