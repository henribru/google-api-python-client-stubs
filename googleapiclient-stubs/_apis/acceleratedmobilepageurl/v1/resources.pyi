import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

_list = list

@typing.type_check_only
class AcceleratedmobilepageurlResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class AmpUrlsResource(googleapiclient.discovery.Resource):
        def batchGet(
            self, *, body: BatchGetAmpUrlsRequest = ..., **kwargs: typing.Any
        ) -> BatchGetAmpUrlsResponseHttpRequest: ...
    def ampUrls(self) -> AmpUrlsResource: ...

@typing.type_check_only
class BatchGetAmpUrlsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> BatchGetAmpUrlsResponse: ...
