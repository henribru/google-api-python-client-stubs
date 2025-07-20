import collections.abc
import typing

import httplib2
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http

from .schemas import *

_list = list

@typing.type_check_only
class AuthorizedBuyersMarketplaceResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class CuratorsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class DataSegmentsResource(googleapiclient.discovery.Resource):
            def activate(
                self,
                *,
                name: str,
                body: ActivateDataSegmentRequest = ...,
                **kwargs: typing.Any,
            ) -> DataSegmentHttpRequest: ...
            def create(
                self, *, parent: str, body: DataSegment = ..., **kwargs: typing.Any
            ) -> DataSegmentHttpRequest: ...
            def deactivate(
                self,
                *,
                name: str,
                body: DeactivateDataSegmentRequest = ...,
                **kwargs: typing.Any,
            ) -> DataSegmentHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> DataSegmentHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any,
            ) -> ListDataSegmentsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListDataSegmentsResponseHttpRequest,
                previous_response: ListDataSegmentsResponse,
            ) -> ListDataSegmentsResponseHttpRequest | None: ...
            def patch(
                self,
                *,
                name: str,
                body: DataSegment = ...,
                updateMask: str = ...,
                **kwargs: typing.Any,
            ) -> DataSegmentHttpRequest: ...

        def dataSegments(self) -> DataSegmentsResource: ...

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
    def curators(self) -> CuratorsResource: ...

@typing.type_check_only
class DataSegmentHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> DataSegment: ...

@typing.type_check_only
class ListDataSegmentsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListDataSegmentsResponse: ...
