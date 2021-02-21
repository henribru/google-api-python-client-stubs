import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *
@typing.type_check_only
class CloudVideoIntelligenceResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class VideosResource(googleapiclient.discovery.Resource):
        def annotate(
            self,
            *,
            body: GoogleCloudVideointelligenceV1beta2_AnnotateVideoRequest = ...,
            **kwargs: typing.Any
        ) -> GoogleLongrunning_OperationHttpRequest: ...
    def videos(self) -> VideosResource: ...

@typing.type_check_only
class GoogleLongrunning_OperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleLongrunning_Operation: ...
