import collections.abc
import typing

import httplib2
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http

from .schemas import *

_list = list

@typing.type_check_only
class DeveloperKnowledgeResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class DocumentsResource(googleapiclient.discovery.Resource):
        def batchGet(
            self,
            *,
            names: str | _list[str] | None = ...,
            view: typing_extensions.Literal[
                "DOCUMENT_VIEW_UNSPECIFIED",
                "DOCUMENT_VIEW_BASIC",
                "DOCUMENT_VIEW_FULL",
                "DOCUMENT_VIEW_CONTENT",
            ]
            | None = ...,
            **kwargs: typing.Any,
        ) -> BatchGetDocumentsResponseHttpRequest: ...
        def get(
            self,
            *,
            name: str,
            view: typing_extensions.Literal[
                "DOCUMENT_VIEW_UNSPECIFIED",
                "DOCUMENT_VIEW_BASIC",
                "DOCUMENT_VIEW_FULL",
                "DOCUMENT_VIEW_CONTENT",
            ]
            | None = ...,
            **kwargs: typing.Any,
        ) -> DocumentHttpRequest: ...
        def searchDocumentChunks(
            self,
            *,
            filter: str | None = ...,
            pageSize: int | None = ...,
            pageToken: str | None = ...,
            query: str | None = ...,
            **kwargs: typing.Any,
        ) -> SearchDocumentChunksResponseHttpRequest: ...
        def searchDocumentChunks_next(
            self,
            previous_request: SearchDocumentChunksResponseHttpRequest,
            previous_response: SearchDocumentChunksResponse,
        ) -> SearchDocumentChunksResponseHttpRequest | None: ...

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
    def documents(self) -> DocumentsResource: ...

@typing.type_check_only
class BatchGetDocumentsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> BatchGetDocumentsResponse: ...

@typing.type_check_only
class DocumentHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Document: ...

@typing.type_check_only
class SearchDocumentChunksResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> SearchDocumentChunksResponse: ...
