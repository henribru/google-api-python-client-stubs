import collections.abc
import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

_list = list

@typing.type_check_only
class CloudVideoIntelligenceResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class VideosResource(googleapiclient.discovery.Resource):
        def annotate(
            self,
            *,
            body: GoogleCloudVideointelligenceV1p3beta1_AnnotateVideoRequest = ...,
            **kwargs: typing.Any
        ) -> GoogleLongrunning_OperationHttpRequest: ...

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
    def videos(self) -> VideosResource: ...

@typing.type_check_only
class GoogleLongrunning_OperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleLongrunning_Operation: ...
