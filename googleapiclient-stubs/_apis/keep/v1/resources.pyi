import collections.abc
import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

_list = list

@typing.type_check_only
class KeepResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class MediaResource(googleapiclient.discovery.Resource):
        def download(
            self, *, name: str, mimeType: str = ..., **kwargs: typing.Any
        ) -> AttachmentHttpRequest: ...

    @typing.type_check_only
    class NotesResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class PermissionsResource(googleapiclient.discovery.Resource):
            def batchCreate(
                self,
                *,
                parent: str,
                body: BatchCreatePermissionsRequest = ...,
                **kwargs: typing.Any
            ) -> BatchCreatePermissionsResponseHttpRequest: ...
            def batchDelete(
                self,
                *,
                parent: str,
                body: BatchDeletePermissionsRequest = ...,
                **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...

        def create(
            self, *, body: Note = ..., **kwargs: typing.Any
        ) -> NoteHttpRequest: ...
        def delete(self, *, name: str, **kwargs: typing.Any) -> EmptyHttpRequest: ...
        def get(self, *, name: str, **kwargs: typing.Any) -> NoteHttpRequest: ...
        def list(
            self,
            *,
            filter: str = ...,
            pageSize: int = ...,
            pageToken: str = ...,
            **kwargs: typing.Any
        ) -> ListNotesResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: ListNotesResponseHttpRequest,
            previous_response: ListNotesResponse,
        ) -> ListNotesResponseHttpRequest | None: ...
        def permissions(self) -> PermissionsResource: ...

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
    def media(self) -> MediaResource: ...
    def notes(self) -> NotesResource: ...

@typing.type_check_only
class AttachmentHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Attachment: ...

@typing.type_check_only
class BatchCreatePermissionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> BatchCreatePermissionsResponse: ...

@typing.type_check_only
class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Empty: ...

@typing.type_check_only
class ListNotesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListNotesResponse: ...

@typing.type_check_only
class NoteHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Note: ...
