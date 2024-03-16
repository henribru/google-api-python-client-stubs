import collections.abc
import typing

import httplib2
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http

from .schemas import *

_list = list

@typing.type_check_only
class BigLakeServiceResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class ProjectsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class LocationsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class CatalogsResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class DatabasesResource(googleapiclient.discovery.Resource):
                    @typing.type_check_only
                    class TablesResource(googleapiclient.discovery.Resource):
                        def create(
                            self,
                            *,
                            parent: str,
                            body: Table = ...,
                            tableId: str = ...,
                            **kwargs: typing.Any,
                        ) -> TableHttpRequest: ...
                        def delete(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> TableHttpRequest: ...
                        def get(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> TableHttpRequest: ...
                        def list(
                            self,
                            *,
                            parent: str,
                            pageSize: int = ...,
                            pageToken: str = ...,
                            view: typing_extensions.Literal[
                                "TABLE_VIEW_UNSPECIFIED", "BASIC", "FULL"
                            ] = ...,
                            **kwargs: typing.Any,
                        ) -> ListTablesResponseHttpRequest: ...
                        def list_next(
                            self,
                            previous_request: ListTablesResponseHttpRequest,
                            previous_response: ListTablesResponse,
                        ) -> ListTablesResponseHttpRequest | None: ...
                        def patch(
                            self,
                            *,
                            name: str,
                            body: Table = ...,
                            updateMask: str = ...,
                            **kwargs: typing.Any,
                        ) -> TableHttpRequest: ...
                        def rename(
                            self,
                            *,
                            name: str,
                            body: RenameTableRequest = ...,
                            **kwargs: typing.Any,
                        ) -> TableHttpRequest: ...

                    def create(
                        self,
                        *,
                        parent: str,
                        body: Database = ...,
                        databaseId: str = ...,
                        **kwargs: typing.Any,
                    ) -> DatabaseHttpRequest: ...
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> DatabaseHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> DatabaseHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
                    ) -> ListDatabasesResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: ListDatabasesResponseHttpRequest,
                        previous_response: ListDatabasesResponse,
                    ) -> ListDatabasesResponseHttpRequest | None: ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: Database = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any,
                    ) -> DatabaseHttpRequest: ...
                    def tables(self) -> TablesResource: ...

                def create(
                    self,
                    *,
                    parent: str,
                    body: Catalog = ...,
                    catalogId: str = ...,
                    **kwargs: typing.Any,
                ) -> CatalogHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> CatalogHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> CatalogHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> ListCatalogsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListCatalogsResponseHttpRequest,
                    previous_response: ListCatalogsResponse,
                ) -> ListCatalogsResponseHttpRequest | None: ...
                def databases(self) -> DatabasesResource: ...

            def catalogs(self) -> CatalogsResource: ...

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
class CatalogHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Catalog: ...

@typing.type_check_only
class DatabaseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Database: ...

@typing.type_check_only
class ListCatalogsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListCatalogsResponse: ...

@typing.type_check_only
class ListDatabasesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListDatabasesResponse: ...

@typing.type_check_only
class ListTablesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListTablesResponse: ...

@typing.type_check_only
class TableHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Table: ...
