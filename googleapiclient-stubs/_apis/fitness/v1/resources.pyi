import collections.abc
import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

_list = list

@typing.type_check_only
class FitnessResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class UsersResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class DataSourcesResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class DataPointChangesResource(googleapiclient.discovery.Resource):
                def list(
                    self,
                    *,
                    userId: str,
                    dataSourceId: str,
                    limit: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> ListDataPointChangesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListDataPointChangesResponseHttpRequest,
                    previous_response: ListDataPointChangesResponse,
                ) -> ListDataPointChangesResponseHttpRequest | None: ...

            @typing.type_check_only
            class DatasetsResource(googleapiclient.discovery.Resource):
                def delete(
                    self,
                    *,
                    userId: str,
                    dataSourceId: str,
                    datasetId: str,
                    **kwargs: typing.Any
                ) -> googleapiclient.http.HttpRequest: ...
                def get(
                    self,
                    *,
                    userId: str,
                    dataSourceId: str,
                    datasetId: str,
                    limit: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> DatasetHttpRequest: ...
                def get_next(
                    self,
                    previous_request: DatasetHttpRequest,
                    previous_response: Dataset,
                ) -> DatasetHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    userId: str,
                    dataSourceId: str,
                    datasetId: str,
                    body: Dataset = ...,
                    **kwargs: typing.Any
                ) -> DatasetHttpRequest: ...
                def patch_next(
                    self,
                    previous_request: DatasetHttpRequest,
                    previous_response: Dataset,
                ) -> DatasetHttpRequest | None: ...

            def create(
                self, *, userId: str, body: DataSource = ..., **kwargs: typing.Any
            ) -> DataSourceHttpRequest: ...
            def delete(
                self, *, userId: str, dataSourceId: str, **kwargs: typing.Any
            ) -> DataSourceHttpRequest: ...
            def get(
                self, *, userId: str, dataSourceId: str, **kwargs: typing.Any
            ) -> DataSourceHttpRequest: ...
            def list(
                self,
                *,
                userId: str,
                dataTypeName: str | _list[str] = ...,
                **kwargs: typing.Any
            ) -> ListDataSourcesResponseHttpRequest: ...
            def update(
                self,
                *,
                userId: str,
                dataSourceId: str,
                body: DataSource = ...,
                **kwargs: typing.Any
            ) -> DataSourceHttpRequest: ...
            def dataPointChanges(self) -> DataPointChangesResource: ...
            def datasets(self) -> DatasetsResource: ...

        @typing.type_check_only
        class DatasetResource(googleapiclient.discovery.Resource):
            def aggregate(
                self, *, userId: str, body: AggregateRequest = ..., **kwargs: typing.Any
            ) -> AggregateResponseHttpRequest: ...

        @typing.type_check_only
        class SessionsResource(googleapiclient.discovery.Resource):
            def delete(
                self, *, userId: str, sessionId: str, **kwargs: typing.Any
            ) -> googleapiclient.http.HttpRequest: ...
            def list(
                self,
                *,
                userId: str,
                activityType: int | _list[int] = ...,
                endTime: str = ...,
                includeDeleted: bool = ...,
                pageToken: str = ...,
                startTime: str = ...,
                **kwargs: typing.Any
            ) -> ListSessionsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListSessionsResponseHttpRequest,
                previous_response: ListSessionsResponse,
            ) -> ListSessionsResponseHttpRequest | None: ...
            def update(
                self,
                *,
                userId: str,
                sessionId: str,
                body: Session = ...,
                **kwargs: typing.Any
            ) -> SessionHttpRequest: ...

        def dataSources(self) -> DataSourcesResource: ...
        def dataset(self) -> DatasetResource: ...
        def sessions(self) -> SessionsResource: ...

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
    def users(self) -> UsersResource: ...

@typing.type_check_only
class AggregateResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> AggregateResponse: ...

@typing.type_check_only
class DataSourceHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> DataSource: ...

@typing.type_check_only
class DatasetHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Dataset: ...

@typing.type_check_only
class ListDataPointChangesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListDataPointChangesResponse: ...

@typing.type_check_only
class ListDataSourcesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListDataSourcesResponse: ...

@typing.type_check_only
class ListSessionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListSessionsResponse: ...

@typing.type_check_only
class SessionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Session: ...
