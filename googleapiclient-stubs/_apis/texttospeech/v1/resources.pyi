import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *
@typing.type_check_only
class TexttospeechResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class TextResource(googleapiclient.discovery.Resource):
        def synthesize(
            self, *, body: SynthesizeSpeechRequest = ..., **kwargs: typing.Any
        ) -> SynthesizeSpeechResponseHttpRequest: ...
    @typing.type_check_only
    class VoicesResource(googleapiclient.discovery.Resource):
        def list(
            self, *, languageCode: str = ..., **kwargs: typing.Any
        ) -> ListVoicesResponseHttpRequest: ...
    def text(self) -> TextResource: ...
    def voices(self) -> VoicesResource: ...

@typing.type_check_only
class ListVoicesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> ListVoicesResponse: ...

@typing.type_check_only
class SynthesizeSpeechResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> SynthesizeSpeechResponse: ...
