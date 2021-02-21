import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *
@typing.type_check_only
class DocsResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class DocumentsResource(googleapiclient.discovery.Resource):
        def batchUpdate(
            self,
            *,
            documentId: str,
            body: BatchUpdateDocumentRequest = ...,
            **kwargs: typing.Any
        ) -> BatchUpdateDocumentResponseHttpRequest: ...
        def create(
            self, *, body: Document = ..., **kwargs: typing.Any
        ) -> DocumentHttpRequest: ...
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
    def documents(self) -> DocumentsResource: ...

@typing.type_check_only
class BatchUpdateDocumentResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> BatchUpdateDocumentResponse: ...

@typing.type_check_only
class DocumentHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> Document: ...
