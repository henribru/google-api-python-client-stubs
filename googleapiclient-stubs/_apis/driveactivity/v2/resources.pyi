import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class DriveActivityResource(googleapiclient.discovery.Resource):
    class ActivityResource(googleapiclient.discovery.Resource):
        def query(
            self, *, body: QueryDriveActivityRequest = ..., **kwargs: typing.Any
        ) -> QueryDriveActivityResponseHttpRequest: ...
    def activity(self) -> ActivityResource: ...

class QueryDriveActivityResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> QueryDriveActivityResponse: ...
