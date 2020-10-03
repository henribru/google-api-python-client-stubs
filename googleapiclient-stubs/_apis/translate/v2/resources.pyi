import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class TranslateResource(googleapiclient.discovery.Resource):
    class LanguagesResource(googleapiclient.discovery.Resource):
        def list(
            self, *, target: str = ..., model: str = ..., **kwargs: typing.Any
        ) -> LanguagesListResponseHttpRequest: ...
    class DetectionsResource(googleapiclient.discovery.Resource):
        def detect(
            self, *, body: DetectLanguageRequest = ..., **kwargs: typing.Any
        ) -> DetectionsListResponseHttpRequest: ...
        def list(
            self, *, q: typing.Union[str, typing.List[str]], **kwargs: typing.Any
        ) -> DetectionsListResponseHttpRequest: ...
    class TranslationsResource(googleapiclient.discovery.Resource):
        def translate(
            self, *, body: TranslateTextRequest = ..., **kwargs: typing.Any
        ) -> TranslationsListResponseHttpRequest: ...
        def list(
            self,
            *,
            q: typing.Union[str, typing.List[str]],
            target: str,
            format: typing_extensions.Literal["html", "text"] = ...,
            cid: typing.Union[str, typing.List[str]] = ...,
            source: str = ...,
            model: str = ...,
            **kwargs: typing.Any
        ) -> TranslationsListResponseHttpRequest: ...
    def languages(self) -> LanguagesResource: ...
    def detections(self) -> DetectionsResource: ...
    def translations(self) -> TranslationsResource: ...

class DetectionsListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> DetectionsListResponse: ...

class LanguagesListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> LanguagesListResponse: ...

class TranslationsListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> TranslationsListResponse: ...
