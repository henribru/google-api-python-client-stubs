import collections.abc
import typing

import httplib2
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http

from .schemas import *

_list = list

@typing.type_check_only
class MerchantResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class AccountsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class DataSourcesResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class FileUploadsResource(googleapiclient.discovery.Resource):
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> FileUploadHttpRequest: ...

            def create(
                self, *, parent: str, body: DataSource = ..., **kwargs: typing.Any
            ) -> DataSourceHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def fetch(
                self,
                *,
                name: str,
                body: FetchDataSourceRequest = ...,
                **kwargs: typing.Any,
            ) -> EmptyHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> DataSourceHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any,
            ) -> ListDataSourcesResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListDataSourcesResponseHttpRequest,
                previous_response: ListDataSourcesResponse,
            ) -> ListDataSourcesResponseHttpRequest | None: ...
            def patch(
                self,
                *,
                name: str,
                body: DataSource = ...,
                updateMask: str = ...,
                **kwargs: typing.Any,
            ) -> DataSourceHttpRequest: ...
            def fileUploads(self) -> FileUploadsResource: ...

        def dataSources(self) -> DataSourcesResource: ...

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
    def accounts(self) -> AccountsResource: ...

@typing.type_check_only
class DataSourceHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> DataSource: ...

@typing.type_check_only
class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Empty: ...

@typing.type_check_only
class FileUploadHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> FileUpload: ...

@typing.type_check_only
class ListDataSourcesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListDataSourcesResponse: ...
