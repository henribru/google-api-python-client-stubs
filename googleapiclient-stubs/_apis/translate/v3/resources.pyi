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
            class AdaptiveMtDatasetsResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class AdaptiveMtFilesResource(googleapiclient.discovery.Resource):
                    @typing.type_check_only
                    class AdaptiveMtSentencesResource(
                        googleapiclient.discovery.Resource
                    ):
                        def list(
                            self,
                            *,
                            parent: str,
                            pageSize: int = ...,
                            pageToken: str = ...,
                            **kwargs: typing.Any,
                        ) -> ListAdaptiveMtSentencesResponseHttpRequest: ...
                        def list_next(
                            self,
                            previous_request: ListAdaptiveMtSentencesResponseHttpRequest,
                            previous_response: ListAdaptiveMtSentencesResponse,
                        ) -> ListAdaptiveMtSentencesResponseHttpRequest | None: ...

                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> EmptyHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> AdaptiveMtFileHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
                    ) -> ListAdaptiveMtFilesResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: ListAdaptiveMtFilesResponseHttpRequest,
                        previous_response: ListAdaptiveMtFilesResponse,
                    ) -> ListAdaptiveMtFilesResponseHttpRequest | None: ...
                    def adaptiveMtSentences(self) -> AdaptiveMtSentencesResource: ...

                @typing.type_check_only
                class AdaptiveMtSentencesResource(googleapiclient.discovery.Resource):
                    def list(
                        self,
                        *,
                        parent: str,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
                    ) -> ListAdaptiveMtSentencesResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: ListAdaptiveMtSentencesResponseHttpRequest,
                        previous_response: ListAdaptiveMtSentencesResponse,
                    ) -> ListAdaptiveMtSentencesResponseHttpRequest | None: ...

                def create(
                    self,
                    *,
                    parent: str,
                    body: AdaptiveMtDataset = ...,
                    **kwargs: typing.Any,
                ) -> AdaptiveMtDatasetHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> AdaptiveMtDatasetHttpRequest: ...
                def importAdaptiveMtFile(
                    self,
                    *,
                    parent: str,
                    body: ImportAdaptiveMtFileRequest = ...,
                    **kwargs: typing.Any,
                ) -> ImportAdaptiveMtFileResponseHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> ListAdaptiveMtDatasetsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListAdaptiveMtDatasetsResponseHttpRequest,
                    previous_response: ListAdaptiveMtDatasetsResponse,
                ) -> ListAdaptiveMtDatasetsResponseHttpRequest | None: ...
                def adaptiveMtFiles(self) -> AdaptiveMtFilesResource: ...
                def adaptiveMtSentences(self) -> AdaptiveMtSentencesResource: ...

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
                        **kwargs: typing.Any,
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
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> DatasetHttpRequest: ...
                def importData(
                    self,
                    *,
                    dataset: str,
                    body: ImportDataRequest = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
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
                        **kwargs: typing.Any,
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
                        **kwargs: typing.Any,
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
                        **kwargs: typing.Any,
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
                    **kwargs: typing.Any,
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
                    **kwargs: typing.Any,
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
                    **kwargs: typing.Any,
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

            def adaptiveMtTranslate(
                self,
                *,
                parent: str,
                body: AdaptiveMtTranslateRequest = ...,
                **kwargs: typing.Any,
            ) -> AdaptiveMtTranslateResponseHttpRequest: ...
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
            def romanizeText(
                self,
                *,
                parent: str,
                body: RomanizeTextRequest = ...,
                **kwargs: typing.Any,
            ) -> RomanizeTextResponseHttpRequest: ...
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
            def adaptiveMtDatasets(self) -> AdaptiveMtDatasetsResource: ...
            def datasets(self) -> DatasetsResource: ...
            def glossaries(self) -> GlossariesResource: ...
            def models(self) -> ModelsResource: ...
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
        | None = None,
    ) -> googleapiclient.http.BatchHttpRequest: ...
    def projects(self) -> ProjectsResource: ...

@typing.type_check_only
class AdaptiveMtDatasetHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> AdaptiveMtDataset: ...

@typing.type_check_only
class AdaptiveMtFileHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> AdaptiveMtFile: ...

@typing.type_check_only
class AdaptiveMtTranslateResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> AdaptiveMtTranslateResponse: ...

@typing.type_check_only
class DatasetHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Dataset: ...

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
class GlossaryEntryHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GlossaryEntry: ...

@typing.type_check_only
class ImportAdaptiveMtFileResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ImportAdaptiveMtFileResponse: ...

@typing.type_check_only
class ListAdaptiveMtDatasetsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListAdaptiveMtDatasetsResponse: ...

@typing.type_check_only
class ListAdaptiveMtFilesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListAdaptiveMtFilesResponse: ...

@typing.type_check_only
class ListAdaptiveMtSentencesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListAdaptiveMtSentencesResponse: ...

@typing.type_check_only
class ListDatasetsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListDatasetsResponse: ...

@typing.type_check_only
class ListExamplesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListExamplesResponse: ...

@typing.type_check_only
class ListGlossariesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListGlossariesResponse: ...

@typing.type_check_only
class ListGlossaryEntriesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListGlossaryEntriesResponse: ...

@typing.type_check_only
class ListLocationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListLocationsResponse: ...

@typing.type_check_only
class ListModelsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListModelsResponse: ...

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
class ModelHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Model: ...

@typing.type_check_only
class OperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Operation: ...

@typing.type_check_only
class RomanizeTextResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> RomanizeTextResponse: ...

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
