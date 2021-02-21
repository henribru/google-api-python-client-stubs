import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *
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
            def return_(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleExampleLibraryagentV1BookHttpRequest: ...
        def get(
            self, *, name: str, **kwargs: typing.Any
        ) -> GoogleExampleLibraryagentV1ShelfHttpRequest: ...
        def list(
            self, *, pageSize: int = ..., pageToken: str = ..., **kwargs: typing.Any
        ) -> GoogleExampleLibraryagentV1ListShelvesResponseHttpRequest: ...
        def books(self) -> BooksResource: ...
    def shelves(self) -> ShelvesResource: ...

@typing.type_check_only
class GoogleExampleLibraryagentV1BookHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleExampleLibraryagentV1Book: ...

@typing.type_check_only
class GoogleExampleLibraryagentV1ListBooksResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleExampleLibraryagentV1ListBooksResponse: ...

@typing.type_check_only
class GoogleExampleLibraryagentV1ListShelvesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleExampleLibraryagentV1ListShelvesResponse: ...

@typing.type_check_only
class GoogleExampleLibraryagentV1ShelfHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleExampleLibraryagentV1Shelf: ...
