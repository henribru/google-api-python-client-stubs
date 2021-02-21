import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *
@typing.type_check_only
class CloudNaturalLanguageResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class DocumentsResource(googleapiclient.discovery.Resource):
        def analyzeEntities(
            self, *, body: AnalyzeEntitiesRequest = ..., **kwargs: typing.Any
        ) -> AnalyzeEntitiesResponseHttpRequest: ...
        def analyzeSentiment(
            self, *, body: AnalyzeSentimentRequest = ..., **kwargs: typing.Any
        ) -> AnalyzeSentimentResponseHttpRequest: ...
        def analyzeSyntax(
            self, *, body: AnalyzeSyntaxRequest = ..., **kwargs: typing.Any
        ) -> AnalyzeSyntaxResponseHttpRequest: ...
        def annotateText(
            self, *, body: AnnotateTextRequest = ..., **kwargs: typing.Any
        ) -> AnnotateTextResponseHttpRequest: ...
    def documents(self) -> DocumentsResource: ...

@typing.type_check_only
class AnalyzeEntitiesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> AnalyzeEntitiesResponse: ...

@typing.type_check_only
class AnalyzeSentimentResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> AnalyzeSentimentResponse: ...

@typing.type_check_only
class AnalyzeSyntaxResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> AnalyzeSyntaxResponse: ...

@typing.type_check_only
class AnnotateTextResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> AnnotateTextResponse: ...
