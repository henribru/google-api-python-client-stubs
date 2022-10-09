import collections.abc
import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

_list = list

@typing.type_check_only
class ConnectorsResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class ProjectsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class LocationsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class ConnectionsResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class ActionsResource(googleapiclient.discovery.Resource):
                    def execute(
                        self,
                        *,
                        name: str,
                        body: ExecuteActionRequest = ...,
                        **kwargs: typing.Any
                    ) -> ExecuteActionResponseHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any
                    ) -> ListActionsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: ListActionsResponseHttpRequest,
                        previous_response: ListActionsResponse,
                    ) -> ListActionsResponseHttpRequest | None: ...

                @typing.type_check_only
                class EntityTypesResource(googleapiclient.discovery.Resource):
                    @typing.type_check_only
                    class EntitiesResource(googleapiclient.discovery.Resource):
                        def create(
                            self,
                            *,
                            parent: str,
                            body: Entity = ...,
                            **kwargs: typing.Any
                        ) -> EntityHttpRequest: ...
                        def delete(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> EmptyHttpRequest: ...
                        def deleteEntitiesWithConditions(
                            self,
                            *,
                            entityType: str,
                            conditions: str = ...,
                            **kwargs: typing.Any
                        ) -> EmptyHttpRequest: ...
                        def get(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> EntityHttpRequest: ...
                        def list(
                            self,
                            *,
                            parent: str,
                            conditions: str = ...,
                            pageSize: int = ...,
                            pageToken: str = ...,
                            sortBy: str | _list[str] = ...,
                            **kwargs: typing.Any
                        ) -> ListEntitiesResponseHttpRequest: ...
                        def list_next(
                            self,
                            previous_request: ListEntitiesResponseHttpRequest,
                            previous_response: ListEntitiesResponse,
                        ) -> ListEntitiesResponseHttpRequest | None: ...
                        def patch(
                            self, *, name: str, body: Entity = ..., **kwargs: typing.Any
                        ) -> EntityHttpRequest: ...
                        def updateEntitiesWithConditions(
                            self,
                            *,
                            entityType: str,
                            body: Entity = ...,
                            conditions: str = ...,
                            **kwargs: typing.Any
                        ) -> UpdateEntitiesWithConditionsResponseHttpRequest: ...

                    def list(
                        self,
                        *,
                        parent: str,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any
                    ) -> ListEntityTypesResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: ListEntityTypesResponseHttpRequest,
                        previous_response: ListEntityTypesResponse,
                    ) -> ListEntityTypesResponseHttpRequest | None: ...
                    def entities(self) -> EntitiesResource: ...

                def executeSqlQuery(
                    self,
                    *,
                    connection: str,
                    body: ExecuteSqlQueryRequest = ...,
                    **kwargs: typing.Any
                ) -> ExecuteSqlQueryResponseHttpRequest: ...
                def actions(self) -> ActionsResource: ...
                def entityTypes(self) -> EntityTypesResource: ...

            def connections(self) -> ConnectionsResource: ...

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
class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Empty: ...

@typing.type_check_only
class EntityHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Entity: ...

@typing.type_check_only
class ExecuteActionResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ExecuteActionResponse: ...

@typing.type_check_only
class ExecuteSqlQueryResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ExecuteSqlQueryResponse: ...

@typing.type_check_only
class ListActionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListActionsResponse: ...

@typing.type_check_only
class ListEntitiesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListEntitiesResponse: ...

@typing.type_check_only
class ListEntityTypesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListEntityTypesResponse: ...

@typing.type_check_only
class UpdateEntitiesWithConditionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> UpdateEntitiesWithConditionsResponse: ...
