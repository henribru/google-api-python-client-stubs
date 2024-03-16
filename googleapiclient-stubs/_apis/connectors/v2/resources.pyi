import collections.abc
import typing

import httplib2
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http

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
                        **kwargs: typing.Any,
                    ) -> ExecuteActionResponseHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> ActionHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        view: typing_extensions.Literal[
                            "ACTION_VIEW_UNSPECIFIED",
                            "ACTION_VIEW_BASIC",
                            "ACTION_VIEW_FULL",
                        ] = ...,
                        **kwargs: typing.Any,
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
                            **kwargs: typing.Any,
                        ) -> EntityHttpRequest: ...
                        def delete(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> EmptyHttpRequest: ...
                        def deleteEntitiesWithConditions(
                            self,
                            *,
                            entityType: str,
                            conditions: str = ...,
                            **kwargs: typing.Any,
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
                            **kwargs: typing.Any,
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
                            **kwargs: typing.Any,
                        ) -> UpdateEntitiesWithConditionsResponseHttpRequest: ...

                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> EntityTypeHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        view: typing_extensions.Literal[
                            "ENTITY_TYPE_VIEW_UNSPECIFIED",
                            "ENTITY_TYPE_VIEW_BASIC",
                            "ENTITY_TYPE_VIEW_FULL",
                        ] = ...,
                        **kwargs: typing.Any,
                    ) -> ListEntityTypesResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: ListEntityTypesResponseHttpRequest,
                        previous_response: ListEntityTypesResponse,
                    ) -> ListEntityTypesResponseHttpRequest | None: ...
                    def entities(self) -> EntitiesResource: ...

                def checkReadiness(
                    self, *, name: str, **kwargs: typing.Any
                ) -> CheckReadinessResponseHttpRequest: ...
                def checkStatus(
                    self, *, name: str, **kwargs: typing.Any
                ) -> CheckStatusResponseHttpRequest: ...
                def exchangeAuthCode(
                    self,
                    *,
                    name: str,
                    body: ExchangeAuthCodeRequest = ...,
                    **kwargs: typing.Any,
                ) -> ExchangeAuthCodeResponseHttpRequest: ...
                def executeSqlQuery(
                    self,
                    *,
                    connection: str,
                    body: ExecuteSqlQueryRequest = ...,
                    **kwargs: typing.Any,
                ) -> ExecuteSqlQueryResponseHttpRequest: ...
                def refreshAccessToken(
                    self,
                    *,
                    name: str,
                    body: RefreshAccessTokenRequest = ...,
                    **kwargs: typing.Any,
                ) -> RefreshAccessTokenResponseHttpRequest: ...
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
        | None = None,
    ) -> googleapiclient.http.BatchHttpRequest: ...
    def projects(self) -> ProjectsResource: ...

@typing.type_check_only
class ActionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Action: ...

@typing.type_check_only
class CheckReadinessResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> CheckReadinessResponse: ...

@typing.type_check_only
class CheckStatusResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> CheckStatusResponse: ...

@typing.type_check_only
class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Empty: ...

@typing.type_check_only
class EntityHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Entity: ...

@typing.type_check_only
class EntityTypeHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> EntityType: ...

@typing.type_check_only
class ExchangeAuthCodeResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ExchangeAuthCodeResponse: ...

@typing.type_check_only
class ExecuteActionResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ExecuteActionResponse: ...

@typing.type_check_only
class ExecuteSqlQueryResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ExecuteSqlQueryResponse: ...

@typing.type_check_only
class ListActionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListActionsResponse: ...

@typing.type_check_only
class ListEntitiesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListEntitiesResponse: ...

@typing.type_check_only
class ListEntityTypesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListEntityTypesResponse: ...

@typing.type_check_only
class RefreshAccessTokenResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> RefreshAccessTokenResponse: ...

@typing.type_check_only
class UpdateEntitiesWithConditionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> UpdateEntitiesWithConditionsResponse: ...
