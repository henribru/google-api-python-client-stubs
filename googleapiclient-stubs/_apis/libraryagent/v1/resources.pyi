import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class LibraryagentResource(googleapiclient.discovery.Resource):
    class ShelvesResource(googleapiclient.discovery.Resource):
        class BooksResource(googleapiclient.discovery.Resource):
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
            def borrow(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleExampleLibraryagentV1BookHttpRequest: ...
            def return_(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleExampleLibraryagentV1BookHttpRequest: ...
        def list(
            self, *, pageToken: str = ..., pageSize: int = ..., **kwargs: typing.Any
        ) -> GoogleExampleLibraryagentV1ListShelvesResponseHttpRequest: ...
        def get(
            self, *, name: str, **kwargs: typing.Any
        ) -> GoogleExampleLibraryagentV1ShelfHttpRequest: ...
        def books(self) -> BooksResource: ...
    def shelves(self) -> ShelvesResource: ...

class GoogleExampleLibraryagentV1ListShelvesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleExampleLibraryagentV1ListShelvesResponse: ...

class GoogleExampleLibraryagentV1ShelfHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleExampleLibraryagentV1Shelf: ...

class GoogleExampleLibraryagentV1BookHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleExampleLibraryagentV1Book: ...

class GoogleExampleLibraryagentV1ListBooksResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleExampleLibraryagentV1ListBooksResponse: ...
