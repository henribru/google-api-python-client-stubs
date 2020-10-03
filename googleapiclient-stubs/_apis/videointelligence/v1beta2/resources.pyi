import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class CloudVideoIntelligenceResource(googleapiclient.discovery.Resource):
    class VideosResource(googleapiclient.discovery.Resource):
        def annotate(
            self,
            *,
            body: GoogleCloudVideointelligenceV1beta2_AnnotateVideoRequest = ...,
            **kwargs: typing.Any
        ) -> GoogleLongrunning_OperationHttpRequest: ...
    def videos(self) -> VideosResource: ...

class GoogleLongrunning_OperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleLongrunning_Operation: ...
