import collections.abc
import typing

import httplib2
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http

from .schemas import *

_list = list

@typing.type_check_only
class TranslateResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class ProjectsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class LocationsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class GlossariesResource(googleapiclient.discovery.Resource):
                def create(
                    self, *, parent: str, body: Glossary = ..., **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GlossaryHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> ListGlossariesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListGlossariesResponseHttpRequest,
                    previous_response: ListGlossariesResponse,
                ) -> ListGlossariesResponseHttpRequest | None: ...

            @typing.type_check_only
            class OperationsResource(googleapiclient.discovery.Resource):
                def cancel(
                    self,
                    *,
                    name: str,
                    body: CancelOperationRequest = ...,
                    **kwargs: typing.Any,
                ) -> EmptyHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def list(
                    self,
                    *,
                    name: str,
                    filter: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> ListOperationsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListOperationsResponseHttpRequest,
                    previous_response: ListOperationsResponse,
                ) -> ListOperationsResponseHttpRequest | None: ...
                def wait(
                    self,
                    *,
                    name: str,
                    body: WaitOperationRequest = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...

            def batchTranslateDocument(
                self,
                *,
                parent: str,
                body: BatchTranslateDocumentRequest = ...,
                **kwargs: typing.Any,
            ) -> OperationHttpRequest: ...
            def batchTranslateText(
                self,
                *,
                parent: str,
                body: BatchTranslateTextRequest = ...,
                **kwargs: typing.Any,
            ) -> OperationHttpRequest: ...
            def detectLanguage(
                self,
                *,
                parent: str,
                body: DetectLanguageRequest = ...,
                **kwargs: typing.Any,
            ) -> DetectLanguageResponseHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> LocationHttpRequest: ...
            def getSupportedLanguages(
                self,
                *,
                parent: str,
                displayLanguageCode: str = ...,
                model: str = ...,
                **kwargs: typing.Any,
            ) -> SupportedLanguagesHttpRequest: ...
            def list(
                self,
                *,
                name: str,
                extraLocationTypes: str | _list[str] = ...,
                filter: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any,
            ) -> ListLocationsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListLocationsResponseHttpRequest,
                previous_response: ListLocationsResponse,
            ) -> ListLocationsResponseHttpRequest | None: ...
            def translateDocument(
                self,
                *,
                parent: str,
                body: TranslateDocumentRequest = ...,
                **kwargs: typing.Any,
            ) -> TranslateDocumentResponseHttpRequest: ...
            def translateText(
                self,
                *,
                parent: str,
                body: TranslateTextRequest = ...,
                **kwargs: typing.Any,
            ) -> TranslateTextResponseHttpRequest: ...
            def glossaries(self) -> GlossariesResource: ...
            def operations(self) -> OperationsResource: ...

        def detectLanguage(
            self,
            *,
            parent: str,
            body: DetectLanguageRequest = ...,
            **kwargs: typing.Any,
        ) -> DetectLanguageResponseHttpRequest: ...
        def getSupportedLanguages(
            self,
            *,
            parent: str,
            displayLanguageCode: str = ...,
            model: str = ...,
            **kwargs: typing.Any,
        ) -> SupportedLanguagesHttpRequest: ...
        def translateText(
            self, *, parent: str, body: TranslateTextRequest = ..., **kwargs: typing.Any
        ) -> TranslateTextResponseHttpRequest: ...
        def locations(self) -> LocationsResource: ...

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
        | None = None,
    ) -> googleapiclient.http.BatchHttpRequest: ...
    def projects(self) -> ProjectsResource: ...

@typing.type_check_only
class DetectLanguageResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> DetectLanguageResponse: ...

@typing.type_check_only
class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Empty: ...

@typing.type_check_only
class GlossaryHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Glossary: ...

@typing.type_check_only
class ListGlossariesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListGlossariesResponse: ...

@typing.type_check_only
class ListLocationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListLocationsResponse: ...

@typing.type_check_only
class ListOperationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListOperationsResponse: ...

@typing.type_check_only
class LocationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Location: ...

@typing.type_check_only
class OperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Operation: ...

@typing.type_check_only
class SupportedLanguagesHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> SupportedLanguages: ...

@typing.type_check_only
class TranslateDocumentResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> TranslateDocumentResponse: ...

@typing.type_check_only
class TranslateTextResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> TranslateTextResponse: ...
