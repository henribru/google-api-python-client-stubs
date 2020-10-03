import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class FitnessResource(googleapiclient.discovery.Resource):
    class UsersResource(googleapiclient.discovery.Resource):
        class SessionsResource(googleapiclient.discovery.Resource):
            def update(
                self,
                *,
                userId: str,
                sessionId: str,
                body: Session = ...,
                currentTimeMillis: str = ...,
                **kwargs: typing.Any
            ) -> SessionHttpRequest: ...
            def delete(
                self,
                *,
                userId: str,
                sessionId: str,
                currentTimeMillis: str = ...,
                **kwargs: typing.Any
            ) -> googleapiclient.http.HttpRequest: ...
            def list(
                self,
                *,
                userId: str,
                includeDeleted: bool = ...,
                startTime: str = ...,
                pageToken: str = ...,
                activityType: typing.Union[int, typing.List[int]] = ...,
                endTime: str = ...,
                **kwargs: typing.Any
            ) -> ListSessionsResponseHttpRequest: ...
        class DataSourcesResource(googleapiclient.discovery.Resource):
            class DatasetsResource(googleapiclient.discovery.Resource):
                def delete(
                    self,
                    *,
                    userId: str,
                    dataSourceId: str,
                    datasetId: str,
                    currentTimeMillis: str = ...,
                    modifiedTimeMillis: str = ...,
                    **kwargs: typing.Any
                ) -> googleapiclient.http.HttpRequest: ...
                def get(
                    self,
                    *,
                    userId: str,
                    dataSourceId: str,
                    datasetId: str,
                    pageToken: str = ...,
                    limit: int = ...,
                    **kwargs: typing.Any
                ) -> DatasetHttpRequest: ...
                def patch(
                    self,
                    *,
                    userId: str,
                    dataSourceId: str,
                    datasetId: str,
                    body: Dataset = ...,
                    currentTimeMillis: str = ...,
                    **kwargs: typing.Any
                ) -> DatasetHttpRequest: ...
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
            def create(
                self, *, userId: str, body: DataSource = ..., **kwargs: typing.Any
            ) -> DataSourceHttpRequest: ...
            def update(
                self,
                *,
                userId: str,
                dataSourceId: str,
                body: DataSource = ...,
                **kwargs: typing.Any
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
                dataTypeName: typing.Union[str, typing.List[str]] = ...,
                **kwargs: typing.Any
            ) -> ListDataSourcesResponseHttpRequest: ...
            def datasets(self) -> DatasetsResource: ...
            def dataPointChanges(self) -> DataPointChangesResource: ...
        class DatasetResource(googleapiclient.discovery.Resource):
            def aggregate(
                self, *, userId: str, body: AggregateRequest = ..., **kwargs: typing.Any
            ) -> AggregateResponseHttpRequest: ...
        def sessions(self) -> SessionsResource: ...
        def dataSources(self) -> DataSourcesResource: ...
        def dataset(self) -> DatasetResource: ...
    def users(self) -> UsersResource: ...

class DatasetHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Dataset: ...

class SessionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Session: ...

class ListDataPointChangesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListDataPointChangesResponse: ...

class ListSessionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListSessionsResponse: ...

class ListDataSourcesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListDataSourcesResponse: ...

class DataSourceHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> DataSource: ...

class AggregateResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> AggregateResponse: ...
