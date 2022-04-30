import collections.abc
import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

_list = list

@typing.type_check_only
class LibraryagentResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class ShelvesResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class BooksResource(googleapiclient.discovery.Resource):
            def borrow(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleExampleLibraryagentV1BookHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleExampleLibraryagentV1BookHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> GoogleExampleLibraryagentV1ListBooksResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: GoogleExampleLibraryagentV1ListBooksResponseHttpRequest,
                previous_response: GoogleExampleLibraryagentV1ListBooksResponse,
            ) -> GoogleExampleLibraryagentV1ListBooksResponseHttpRequest | None: ...
            def return_(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleExampleLibraryagentV1BookHttpRequest: ...

        def get(
            self, *, name: str, **kwargs: typing.Any
        ) -> GoogleExampleLibraryagentV1ShelfHttpRequest: ...
        def list(
            self, *, pageSize: int = ..., pageToken: str = ..., **kwargs: typing.Any
        ) -> GoogleExampleLibraryagentV1ListShelvesResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: GoogleExampleLibraryagentV1ListShelvesResponseHttpRequest,
            previous_response: GoogleExampleLibraryagentV1ListShelvesResponse,
        ) -> GoogleExampleLibraryagentV1ListShelvesResponseHttpRequest | None: ...
        def books(self) -> BooksResource: ...

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
    def shelves(self) -> ShelvesResource: ...

@typing.type_check_only
class GoogleExampleLibraryagentV1BookHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleExampleLibraryagentV1Book: ...

@typing.type_check_only
class GoogleExampleLibraryagentV1ListBooksResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleExampleLibraryagentV1ListBooksResponse: ...

@typing.type_check_only
class GoogleExampleLibraryagentV1ListShelvesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleExampleLibraryagentV1ListShelvesResponse: ...

@typing.type_check_only
class GoogleExampleLibraryagentV1ShelfHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleExampleLibraryagentV1Shelf: ...
