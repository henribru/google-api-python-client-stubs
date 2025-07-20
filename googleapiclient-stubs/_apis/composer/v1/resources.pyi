import collections.abc
import typing

import httplib2
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http

from .schemas import *

_list = list

@typing.type_check_only
class CloudComposerResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class ProjectsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class LocationsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class EnvironmentsResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class UserWorkloadsConfigMapsResource(
                    googleapiclient.discovery.Resource
                ):
                    def create(
                        self,
                        *,
                        parent: str,
                        body: UserWorkloadsConfigMap = ...,
                        **kwargs: typing.Any,
                    ) -> UserWorkloadsConfigMapHttpRequest: ...
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> EmptyHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> UserWorkloadsConfigMapHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
                    ) -> ListUserWorkloadsConfigMapsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: ListUserWorkloadsConfigMapsResponseHttpRequest,
                        previous_response: ListUserWorkloadsConfigMapsResponse,
                    ) -> ListUserWorkloadsConfigMapsResponseHttpRequest | None: ...
                    def update(
                        self,
                        *,
                        name: str,
                        body: UserWorkloadsConfigMap = ...,
                        **kwargs: typing.Any,
                    ) -> UserWorkloadsConfigMapHttpRequest: ...

                @typing.type_check_only
                class UserWorkloadsSecretsResource(googleapiclient.discovery.Resource):
                    def create(
                        self,
                        *,
                        parent: str,
                        body: UserWorkloadsSecret = ...,
                        **kwargs: typing.Any,
                    ) -> UserWorkloadsSecretHttpRequest: ...
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> EmptyHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> UserWorkloadsSecretHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
                    ) -> ListUserWorkloadsSecretsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: ListUserWorkloadsSecretsResponseHttpRequest,
                        previous_response: ListUserWorkloadsSecretsResponse,
                    ) -> ListUserWorkloadsSecretsResponseHttpRequest | None: ...
                    def update(
                        self,
                        *,
                        name: str,
                        body: UserWorkloadsSecret = ...,
                        **kwargs: typing.Any,
                    ) -> UserWorkloadsSecretHttpRequest: ...

                @typing.type_check_only
                class WorkloadsResource(googleapiclient.discovery.Resource):
                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
                    ) -> ListWorkloadsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: ListWorkloadsResponseHttpRequest,
                        previous_response: ListWorkloadsResponse,
                    ) -> ListWorkloadsResponseHttpRequest | None: ...

                def checkUpgrade(
                    self,
                    *,
                    environment: str,
                    body: CheckUpgradeRequest = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def create(
                    self, *, parent: str, body: Environment = ..., **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def databaseFailover(
                    self,
                    *,
                    environment: str,
                    body: DatabaseFailoverRequest = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def executeAirflowCommand(
                    self,
                    *,
                    environment: str,
                    body: ExecuteAirflowCommandRequest = ...,
                    **kwargs: typing.Any,
                ) -> ExecuteAirflowCommandResponseHttpRequest: ...
                def fetchDatabaseProperties(
                    self, *, environment: str, **kwargs: typing.Any
                ) -> FetchDatabasePropertiesResponseHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> EnvironmentHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> ListEnvironmentsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListEnvironmentsResponseHttpRequest,
                    previous_response: ListEnvironmentsResponse,
                ) -> ListEnvironmentsResponseHttpRequest | None: ...
                def loadSnapshot(
                    self,
                    *,
                    environment: str,
                    body: LoadSnapshotRequest = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: Environment = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def pollAirflowCommand(
                    self,
                    *,
                    environment: str,
                    body: PollAirflowCommandRequest = ...,
                    **kwargs: typing.Any,
                ) -> PollAirflowCommandResponseHttpRequest: ...
                def restartWebServer(
                    self,
                    *,
                    name: str,
                    body: RestartWebServerRequest = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def saveSnapshot(
                    self,
                    *,
                    environment: str,
                    body: SaveSnapshotRequest = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def stopAirflowCommand(
                    self,
                    *,
                    environment: str,
                    body: StopAirflowCommandRequest = ...,
                    **kwargs: typing.Any,
                ) -> StopAirflowCommandResponseHttpRequest: ...
                def userWorkloadsConfigMaps(
                    self,
                ) -> UserWorkloadsConfigMapsResource: ...
                def userWorkloadsSecrets(self) -> UserWorkloadsSecretsResource: ...
                def workloads(self) -> WorkloadsResource: ...

            @typing.type_check_only
            class ImageVersionsResource(googleapiclient.discovery.Resource):
                def list(
                    self,
                    *,
                    parent: str,
                    includePastReleases: bool = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> ListImageVersionsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListImageVersionsResponseHttpRequest,
                    previous_response: ListImageVersionsResponse,
                ) -> ListImageVersionsResponseHttpRequest | None: ...

            @typing.type_check_only
            class OperationsResource(googleapiclient.discovery.Resource):
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def list(
                    self,
                    *,
                    name: str,
                    filter: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> ListOperationsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListOperationsResponseHttpRequest,
                    previous_response: ListOperationsResponse,
                ) -> ListOperationsResponseHttpRequest | None: ...

            def environments(self) -> EnvironmentsResource: ...
            def imageVersions(self) -> ImageVersionsResource: ...
            def operations(self) -> OperationsResource: ...

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
class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Empty: ...

@typing.type_check_only
class EnvironmentHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Environment: ...

@typing.type_check_only
class ExecuteAirflowCommandResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ExecuteAirflowCommandResponse: ...

@typing.type_check_only
class FetchDatabasePropertiesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> FetchDatabasePropertiesResponse: ...

@typing.type_check_only
class ListEnvironmentsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListEnvironmentsResponse: ...

@typing.type_check_only
class ListImageVersionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListImageVersionsResponse: ...

@typing.type_check_only
class ListOperationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListOperationsResponse: ...

@typing.type_check_only
class ListUserWorkloadsConfigMapsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListUserWorkloadsConfigMapsResponse: ...

@typing.type_check_only
class ListUserWorkloadsSecretsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListUserWorkloadsSecretsResponse: ...

@typing.type_check_only
class ListWorkloadsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListWorkloadsResponse: ...

@typing.type_check_only
class OperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Operation: ...

@typing.type_check_only
class PollAirflowCommandResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> PollAirflowCommandResponse: ...

@typing.type_check_only
class StopAirflowCommandResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> StopAirflowCommandResponse: ...

@typing.type_check_only
class UserWorkloadsConfigMapHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> UserWorkloadsConfigMap: ...

@typing.type_check_only
class UserWorkloadsSecretHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> UserWorkloadsSecret: ...
