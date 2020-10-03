import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class DocsResource(googleapiclient.discovery.Resource):
    class DocumentsResource(googleapiclient.discovery.Resource):
        def get(
            self,
            *,
            documentId: str,
            suggestionsViewMode: typing_extensions.Literal[
                "DEFAULT_FOR_CURRENT_ACCESS",
                "SUGGESTIONS_INLINE",
                "PREVIEW_SUGGESTIONS_ACCEPTED",
                "PREVIEW_WITHOUT_SUGGESTIONS",
            ] = ...,
            **kwargs: typing.Any
        ) -> DocumentHttpRequest: ...
        def create(
            self, *, body: Document = ..., **kwargs: typing.Any
        ) -> DocumentHttpRequest: ...
        def batchUpdate(
            self,
            *,
            documentId: str,
            body: BatchUpdateDocumentRequest = ...,
            **kwargs: typing.Any
        ) -> BatchUpdateDocumentResponseHttpRequest: ...
    def documents(self) -> DocumentsResource: ...

class BatchUpdateDocumentResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> BatchUpdateDocumentResponse: ...

class DocumentHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Document: ...
