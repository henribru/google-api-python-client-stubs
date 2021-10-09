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
    def activity(self) -> ActivityResource: ...

@typing.type_check_only
class QueryDriveActivityResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> QueryDriveActivityResponse: ...
