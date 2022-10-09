import collections.abc
import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

_list = list

@typing.type_check_only
class PolicySimulatorResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class OperationsResource(googleapiclient.discovery.Resource):
        def get(
            self, *, name: str, **kwargs: typing.Any
        ) -> GoogleLongrunningOperationHttpRequest: ...
        def list(
            self,
            *,
            filter: str = ...,
            name: str = ...,
            pageSize: int = ...,
            pageToken: str = ...,
            **kwargs: typing.Any
        ) -> GoogleLongrunningListOperationsResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: GoogleLongrunningListOperationsResponseHttpRequest,
            previous_response: GoogleLongrunningListOperationsResponse,
        ) -> GoogleLongrunningListOperationsResponseHttpRequest | None: ...

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
    def operations(self) -> OperationsResource: ...

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
