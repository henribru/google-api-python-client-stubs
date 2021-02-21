import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *
@typing.type_check_only
class TranslateResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class DetectionsResource(googleapiclient.discovery.Resource):
        def detect(
            self, *, body: DetectLanguageRequest = ..., **kwargs: typing.Any
        ) -> DetectionsListResponseHttpRequest: ...
        def list(
            self, *, q: typing.Union[str, typing.List[str]], **kwargs: typing.Any
        ) -> DetectionsListResponseHttpRequest: ...
    @typing.type_check_only
    class LanguagesResource(googleapiclient.discovery.Resource):
        def list(
            self, *, model: str = ..., target: str = ..., **kwargs: typing.Any
        ) -> LanguagesListResponseHttpRequest: ...
    @typing.type_check_only
    class TranslationsResource(googleapiclient.discovery.Resource):
        def list(
            self,
            *,
            q: typing.Union[str, typing.List[str]],
            target: str,
            cid: typing.Union[str, typing.List[str]] = ...,
            format: typing_extensions.Literal["html", "text"] = ...,
            model: str = ...,
            source: str = ...,
            **kwargs: typing.Any
        ) -> TranslationsListResponseHttpRequest: ...
        def translate(
            self, *, body: TranslateTextRequest = ..., **kwargs: typing.Any
        ) -> TranslationsListResponseHttpRequest: ...
    def detections(self) -> DetectionsResource: ...
    def languages(self) -> LanguagesResource: ...
    def translations(self) -> TranslationsResource: ...

@typing.type_check_only
class DetectionsListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> DetectionsListResponse: ...

@typing.type_check_only
class LanguagesListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> LanguagesListResponse: ...

@typing.type_check_only
class TranslationsListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> TranslationsListResponse: ...
