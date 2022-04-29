import collections.abc
import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

_list = list

@typing.type_check_only
class DriveActivityResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class ActivityResource(googleapiclient.discovery.Resource):
        def query(
            self, *, body: QueryDriveActivityRequest = ..., **kwargs: typing.Any
        ) -> QueryDriveActivityResponseHttpRequest: ...
        def query_next(
            self,
            previous_request: QueryDriveActivityResponseHttpRequest,
            previous_response: QueryDriveActivityResponse,
        ) -> QueryDriveActivityResponseHttpRequest | None: ...

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
    def activity(self) -> ActivityResource: ...

@typing.type_check_only
class QueryDriveActivityResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> QueryDriveActivityResponse: ...
