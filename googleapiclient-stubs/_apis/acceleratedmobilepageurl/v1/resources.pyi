import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class AcceleratedmobilepageurlResource(googleapiclient.discovery.Resource):
    class AmpUrlsResource(googleapiclient.discovery.Resource):
        def batchGet(
            self, *, body: BatchGetAmpUrlsRequest = ..., **kwargs: typing.Any
        ) -> BatchGetAmpUrlsResponseHttpRequest: ...
    def ampUrls(self) -> AmpUrlsResource: ...

class BatchGetAmpUrlsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> BatchGetAmpUrlsResponse: ...
