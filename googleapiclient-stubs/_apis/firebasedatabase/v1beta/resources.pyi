import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *
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
                    **kwargs: typing.Any
                ) -> ListDatabaseInstancesResponseHttpRequest: ...
                def reenable(
                    self,
                    *,
                    name: str,
                    body: ReenableDatabaseInstanceRequest = ...,
                    **kwargs: typing.Any
                ) -> DatabaseInstanceHttpRequest: ...
            def instances(self) -> InstancesResource: ...
        def locations(self) -> LocationsResource: ...
    def projects(self) -> ProjectsResource: ...

@typing.type_check_only
class DatabaseInstanceHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> DatabaseInstance: ...

@typing.type_check_only
class ListDatabaseInstancesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> ListDatabaseInstancesResponse: ...
