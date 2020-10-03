import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class TexttospeechResource(googleapiclient.discovery.Resource):
    class TextResource(googleapiclient.discovery.Resource):
        def synthesize(
            self, *, body: SynthesizeSpeechRequest = ..., **kwargs: typing.Any
        ) -> SynthesizeSpeechResponseHttpRequest: ...
    class VoicesResource(googleapiclient.discovery.Resource):
        def list(
            self, *, languageCode: str = ..., **kwargs: typing.Any
        ) -> ListVoicesResponseHttpRequest: ...
    def text(self) -> TextResource: ...
    def voices(self) -> VoicesResource: ...

class ListVoicesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListVoicesResponse: ...

class SynthesizeSpeechResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> SynthesizeSpeechResponse: ...
