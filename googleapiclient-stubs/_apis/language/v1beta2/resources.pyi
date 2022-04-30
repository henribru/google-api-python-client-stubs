import collections.abc
import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

_list = list

@typing.type_check_only
class CloudNaturalLanguageResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class DocumentsResource(googleapiclient.discovery.Resource):
        def analyzeEntities(
            self, *, body: AnalyzeEntitiesRequest = ..., **kwargs: typing.Any
        ) -> AnalyzeEntitiesResponseHttpRequest: ...
        def analyzeEntitySentiment(
            self, *, body: AnalyzeEntitySentimentRequest = ..., **kwargs: typing.Any
        ) -> AnalyzeEntitySentimentResponseHttpRequest: ...
        def analyzeSentiment(
            self, *, body: AnalyzeSentimentRequest = ..., **kwargs: typing.Any
        ) -> AnalyzeSentimentResponseHttpRequest: ...
        def analyzeSyntax(
            self, *, body: AnalyzeSyntaxRequest = ..., **kwargs: typing.Any
        ) -> AnalyzeSyntaxResponseHttpRequest: ...
        def annotateText(
            self, *, body: AnnotateTextRequest = ..., **kwargs: typing.Any
        ) -> AnnotateTextResponseHttpRequest: ...
        def classifyText(
            self, *, body: ClassifyTextRequest = ..., **kwargs: typing.Any
        ) -> ClassifyTextResponseHttpRequest: ...

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
    def documents(self) -> DocumentsResource: ...

@typing.type_check_only
class AnalyzeEntitiesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> AnalyzeEntitiesResponse: ...

@typing.type_check_only
class AnalyzeEntitySentimentResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> AnalyzeEntitySentimentResponse: ...

@typing.type_check_only
class AnalyzeSentimentResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> AnalyzeSentimentResponse: ...

@typing.type_check_only
class AnalyzeSyntaxResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> AnalyzeSyntaxResponse: ...

@typing.type_check_only
class AnnotateTextResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> AnnotateTextResponse: ...

@typing.type_check_only
class ClassifyTextResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ClassifyTextResponse: ...
