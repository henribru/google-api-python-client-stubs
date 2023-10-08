import collections.abc
import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

_list = list

@typing.type_check_only
class TranslateResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class ProjectsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class LocationsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class DatasetsResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class ExamplesResource(googleapiclient.discovery.Resource):
                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any
                    ) -> ListExamplesResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: ListExamplesResponseHttpRequest,
                        previous_response: ListExamplesResponse,
                    ) -> ListExamplesResponseHttpRequest | None: ...

                def create(
                    self, *, parent: str, body: Dataset = ..., **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def exportData(
                    self,
                    *,
                    dataset: str,
                    body: ExportDataRequest = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> DatasetHttpRequest: ...
                def importData(
                    self,
                    *,
                    dataset: str,
                    body: ImportDataRequest = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> ListDatasetsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListDatasetsResponseHttpRequest,
                    previous_response: ListDatasetsResponse,
                ) -> ListDatasetsResponseHttpRequest | None: ...
                def examples(self) -> ExamplesResource: ...

            @typing.type_check_only
            class GlossariesResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class GlossaryEntriesResource(googleapiclient.discovery.Resource):
                    def create(
                        self,
                        *,
                        parent: str,
                        body: GlossaryEntry = ...,
                        **kwargs: typing.Any
                    ) -> GlossaryEntryHttpRequest: ...
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> EmptyHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GlossaryEntryHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any
                    ) -> ListGlossaryEntriesResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: ListGlossaryEntriesResponseHttpRequest,
                        previous_response: ListGlossaryEntriesResponse,
                    ) -> ListGlossaryEntriesResponseHttpRequest | None: ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: GlossaryEntry = ...,
                        **kwargs: typing.Any
                    ) -> GlossaryEntryHttpRequest: ...

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
                    **kwargs: typing.Any
                ) -> ListGlossariesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListGlossariesResponseHttpRequest,
                    previous_response: ListGlossariesResponse,
                ) -> ListGlossariesResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: Glossary = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def glossaryEntries(self) -> GlossaryEntriesResource: ...

            @typing.type_check_only
            class ModelsResource(googleapiclient.discovery.Resource):
                def create(
                    self, *, parent: str, body: Model = ..., **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> ModelHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> ListModelsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListModelsResponseHttpRequest,
                    previous_response: ListModelsResponse,
                ) -> ListModelsResponseHttpRequest | None: ...

            @typing.type_check_only
            class OperationsResource(googleapiclient.discovery.Resource):
                def cancel(
                    self,
                    *,
                    name: str,
                    body: CancelOperationRequest = ...,
                    **kwargs: typing.Any
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
                    **kwargs: typing.Any
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
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...

            def batchTranslateDocument(
                self,
                *,
                parent: str,
                body: BatchTranslateDocumentRequest = ...,
                **kwargs: typing.Any
            ) -> OperationHttpRequest: ...
            def batchTranslateText(
                self,
                *,
                parent: str,
                body: BatchTranslateTextRequest = ...,
                **kwargs: typing.Any
            ) -> OperationHttpRequest: ...
            def detectLanguage(
                self,
                *,
                parent: str,
                body: DetectLanguageRequest = ...,
                **kwargs: typing.Any
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
                **kwargs: typing.Any
            ) -> SupportedLanguagesHttpRequest: ...
            def list(
                self,
                *,
                name: str,
                filter: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> ListLocationsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListLocationsResponseHttpRequest,
                previous_response: ListLocationsResponse,
            ) -> ListLocationsResponseHttpRequest | None: ...
            def romanizeText(
                self,
                *,
                parent: str,
                body: RomanizeTextRequest = ...,
                **kwargs: typing.Any
            ) -> RomanizeTextResponseHttpRequest: ...
            def translateDocument(
                self,
                *,
                parent: str,
                body: TranslateDocumentRequest = ...,
                **kwargs: typing.Any
            ) -> TranslateDocumentResponseHttpRequest: ...
            def translateText(
                self,
                *,
                parent: str,
                body: TranslateTextRequest = ...,
                **kwargs: typing.Any
            ) -> TranslateTextResponseHttpRequest: ...
            def datasets(self) -> DatasetsResource: ...
            def glossaries(self) -> GlossariesResource: ...
            def models(self) -> ModelsResource: ...
            def operations(self) -> OperationsResource: ...

        def detectLanguage(
            self,
            *,
            parent: str,
            body: DetectLanguageRequest = ...,
            **kwargs: typing.Any
        ) -> DetectLanguageResponseHttpRequest: ...
        def getSupportedLanguages(
            self,
            *,
            parent: str,
            displayLanguageCode: str = ...,
            model: str = ...,
            **kwargs: typing.Any
        ) -> SupportedLanguagesHttpRequest: ...
        def romanizeText(
            self, *, parent: str, body: RomanizeTextRequest = ..., **kwargs: typing.Any
        ) -> RomanizeTextResponseHttpRequest: ...
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
        | None = ...,
    ) -> googleapiclient.http.BatchHttpRequest: ...
    def projects(self) -> ProjectsResource: ...

@typing.type_check_only
class DatasetHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Dataset: ...

@typing.type_check_only
class DetectLanguageResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> DetectLanguageResponse: ...

@typing.type_check_only
class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Empty: ...

@typing.type_check_only
class GlossaryHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Glossary: ...

@typing.type_check_only
class GlossaryEntryHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GlossaryEntry: ...

@typing.type_check_only
class ListDatasetsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListDatasetsResponse: ...

@typing.type_check_only
class ListExamplesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListExamplesResponse: ...

@typing.type_check_only
class ListGlossariesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListGlossariesResponse: ...

@typing.type_check_only
class ListGlossaryEntriesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListGlossaryEntriesResponse: ...

@typing.type_check_only
class ListLocationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListLocationsResponse: ...

@typing.type_check_only
class ListModelsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListModelsResponse: ...

@typing.type_check_only
class ListOperationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListOperationsResponse: ...

@typing.type_check_only
class LocationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Location: ...

@typing.type_check_only
class ModelHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Model: ...

@typing.type_check_only
class OperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Operation: ...

@typing.type_check_only
class RomanizeTextResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> RomanizeTextResponse: ...

@typing.type_check_only
class SupportedLanguagesHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> SupportedLanguages: ...

@typing.type_check_only
class TranslateDocumentResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> TranslateDocumentResponse: ...

@typing.type_check_only
class TranslateTextResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> TranslateTextResponse: ...
