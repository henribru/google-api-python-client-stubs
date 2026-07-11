import collections.abc
import typing

import httplib2
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http

from .schemas import *

_list = list

@typing.type_check_only
class Area120TablesResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class TablesResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class RowsResource(googleapiclient.discovery.Resource):
            def batchCreate(
                self, *, parent: str, body: BatchCreateRowsRequest, **kwargs: typing.Any
            ) -> BatchCreateRowsResponseHttpRequest: ...
            def batchDelete(
                self, *, parent: str, body: BatchDeleteRowsRequest, **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def batchUpdate(
                self, *, parent: str, body: BatchUpdateRowsRequest, **kwargs: typing.Any
            ) -> BatchUpdateRowsResponseHttpRequest: ...
            def create(
                self,
                *,
                parent: str,
                body: Row,
                view: typing_extensions.Literal["VIEW_UNSPECIFIED", "COLUMN_ID_VIEW"]
                | None = ...,
                **kwargs: typing.Any,
            ) -> RowHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def get(
                self,
                *,
                name: str,
                view: typing_extensions.Literal["VIEW_UNSPECIFIED", "COLUMN_ID_VIEW"]
                | None = ...,
                **kwargs: typing.Any,
            ) -> RowHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                filter: str | None = ...,
                orderBy: str | None = ...,
                pageSize: int | None = ...,
                pageToken: str | None = ...,
                view: typing_extensions.Literal["VIEW_UNSPECIFIED", "COLUMN_ID_VIEW"]
                | None = ...,
                **kwargs: typing.Any,
            ) -> ListRowsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListRowsResponseHttpRequest,
                previous_response: ListRowsResponse,
            ) -> ListRowsResponseHttpRequest | None: ...
            def patch(
                self,
                *,
                name: str,
                body: Row,
                updateMask: str | None = ...,
                view: typing_extensions.Literal["VIEW_UNSPECIFIED", "COLUMN_ID_VIEW"]
                | None = ...,
                **kwargs: typing.Any,
            ) -> RowHttpRequest: ...

        def get(self, *, name: str, **kwargs: typing.Any) -> TableHttpRequest: ...
        def list(
            self,
            *,
            orderBy: str | None = ...,
            pageSize: int | None = ...,
            pageToken: str | None = ...,
            **kwargs: typing.Any,
        ) -> ListTablesResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: ListTablesResponseHttpRequest,
            previous_response: ListTablesResponse,
        ) -> ListTablesResponseHttpRequest | None: ...
        def rows(self) -> RowsResource: ...

    @typing.type_check_only
    class WorkspacesResource(googleapiclient.discovery.Resource):
        def get(self, *, name: str, **kwargs: typing.Any) -> WorkspaceHttpRequest: ...
        def list(
            self,
            *,
            pageSize: int | None = ...,
            pageToken: str | None = ...,
            **kwargs: typing.Any,
        ) -> ListWorkspacesResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: ListWorkspacesResponseHttpRequest,
            previous_response: ListWorkspacesResponse,
        ) -> ListWorkspacesResponseHttpRequest | None: ...

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
    def tables(self) -> TablesResource: ...
    def workspaces(self) -> WorkspacesResource: ...

@typing.type_check_only
class BatchCreateRowsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> BatchCreateRowsResponse: ...

@typing.type_check_only
class BatchUpdateRowsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> BatchUpdateRowsResponse: ...

@typing.type_check_only
class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Empty: ...

@typing.type_check_only
class ListRowsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListRowsResponse: ...

@typing.type_check_only
class ListTablesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListTablesResponse: ...

@typing.type_check_only
class ListWorkspacesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListWorkspacesResponse: ...

@typing.type_check_only
class RowHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Row: ...

@typing.type_check_only
class TableHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Table: ...

@typing.type_check_only
class WorkspaceHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Workspace: ...
