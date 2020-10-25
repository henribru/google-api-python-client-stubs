import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *
@typing.type_check_only
class Area120TablesResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class TablesResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class RowsResource(googleapiclient.discovery.Resource):
            def batchCreate(
                self,
                *,
                parent: str,
                body: BatchCreateRowsRequest = ...,
                **kwargs: typing.Any
            ) -> BatchCreateRowsResponseHttpRequest: ...
            def batchUpdate(
                self,
                *,
                parent: str,
                body: BatchUpdateRowsRequest = ...,
                **kwargs: typing.Any
            ) -> BatchUpdateRowsResponseHttpRequest: ...
            def create(
                self,
                *,
                parent: str,
                body: Row = ...,
                view: typing_extensions.Literal[
                    "VIEW_UNSPECIFIED", "COLUMN_ID_VIEW"
                ] = ...,
                **kwargs: typing.Any
            ) -> RowHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def get(
                self,
                *,
                name: str,
                view: typing_extensions.Literal[
                    "VIEW_UNSPECIFIED", "COLUMN_ID_VIEW"
                ] = ...,
                **kwargs: typing.Any
            ) -> RowHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                view: typing_extensions.Literal[
                    "VIEW_UNSPECIFIED", "COLUMN_ID_VIEW"
                ] = ...,
                **kwargs: typing.Any
            ) -> ListRowsResponseHttpRequest: ...
            def patch(
                self,
                *,
                name: str,
                body: Row = ...,
                updateMask: str = ...,
                view: typing_extensions.Literal[
                    "VIEW_UNSPECIFIED", "COLUMN_ID_VIEW"
                ] = ...,
                **kwargs: typing.Any
            ) -> RowHttpRequest: ...
        def get(self, *, name: str, **kwargs: typing.Any) -> TableHttpRequest: ...
        def list(
            self, *, pageSize: int = ..., pageToken: str = ..., **kwargs: typing.Any
        ) -> ListTablesResponseHttpRequest: ...
        def rows(self) -> RowsResource: ...
    def tables(self) -> TablesResource: ...

@typing.type_check_only
class BatchCreateRowsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> BatchCreateRowsResponse: ...

@typing.type_check_only
class BatchUpdateRowsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> BatchUpdateRowsResponse: ...

@typing.type_check_only
class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Empty: ...

@typing.type_check_only
class ListRowsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListRowsResponse: ...

@typing.type_check_only
class ListTablesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListTablesResponse: ...

@typing.type_check_only
class RowHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Row: ...

@typing.type_check_only
class TableHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Table: ...
