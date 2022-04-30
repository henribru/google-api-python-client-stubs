import collections.abc
import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

_list = list

@typing.type_check_only
class FirebaseRealtimeDatabaseResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class ProjectsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class LocationsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class InstancesResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: DatabaseInstance = ...,
                    databaseId: str = ...,
                    validateOnly: bool = ...,
                    **kwargs: typing.Any
                ) -> DatabaseInstanceHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> DatabaseInstanceHttpRequest: ...
                def disable(
                    self,
                    *,
                    name: str,
                    body: DisableDatabaseInstanceRequest = ...,
                    **kwargs: typing.Any
                ) -> DatabaseInstanceHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> DatabaseInstanceHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    showDeleted: bool = ...,
                    **kwargs: typing.Any
                ) -> ListDatabaseInstancesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListDatabaseInstancesResponseHttpRequest,
                    previous_response: ListDatabaseInstancesResponse,
                ) -> ListDatabaseInstancesResponseHttpRequest | None: ...
                def reenable(
                    self,
                    *,
                    name: str,
                    body: ReenableDatabaseInstanceRequest = ...,
                    **kwargs: typing.Any
                ) -> DatabaseInstanceHttpRequest: ...
                def undelete(
                    self,
                    *,
                    name: str,
                    body: UndeleteDatabaseInstanceRequest = ...,
                    **kwargs: typing.Any
                ) -> DatabaseInstanceHttpRequest: ...

            def instances(self) -> InstancesResource: ...

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
        | None = ...,
    ) -> googleapiclient.http.BatchHttpRequest: ...
    def projects(self) -> ProjectsResource: ...

@typing.type_check_only
class DatabaseInstanceHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> DatabaseInstance: ...

@typing.type_check_only
class ListDatabaseInstancesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListDatabaseInstancesResponse: ...
