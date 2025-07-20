import collections.abc
import typing

import httplib2
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http

from .schemas import *

_list = list

@typing.type_check_only
class ParameterManagerResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class ProjectsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class LocationsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class ParametersResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class VersionsResource(googleapiclient.discovery.Resource):
                    def create(
                        self,
                        *,
                        parent: str,
                        body: ParameterVersion = ...,
                        parameterVersionId: str = ...,
                        requestId: str = ...,
                        **kwargs: typing.Any,
                    ) -> ParameterVersionHttpRequest: ...
                    def delete(
                        self, *, name: str, requestId: str = ..., **kwargs: typing.Any
                    ) -> EmptyHttpRequest: ...
                    def get(
                        self,
                        *,
                        name: str,
                        view: typing_extensions.Literal[
                            "VIEW_UNSPECIFIED", "BASIC", "FULL"
                        ] = ...,
                        **kwargs: typing.Any,
                    ) -> ParameterVersionHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str = ...,
                        orderBy: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
                    ) -> ListParameterVersionsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: ListParameterVersionsResponseHttpRequest,
                        previous_response: ListParameterVersionsResponse,
                    ) -> ListParameterVersionsResponseHttpRequest | None: ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: ParameterVersion = ...,
                        requestId: str = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any,
                    ) -> ParameterVersionHttpRequest: ...
                    def render(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> RenderParameterVersionResponseHttpRequest: ...

                def create(
                    self,
                    *,
                    parent: str,
                    body: Parameter = ...,
                    parameterId: str = ...,
                    requestId: str = ...,
                    **kwargs: typing.Any,
                ) -> ParameterHttpRequest: ...
                def delete(
                    self, *, name: str, requestId: str = ..., **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> ParameterHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> ListParametersResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListParametersResponseHttpRequest,
                    previous_response: ListParametersResponse,
                ) -> ListParametersResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: Parameter = ...,
                    requestId: str = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> ParameterHttpRequest: ...
                def versions(self) -> VersionsResource: ...

            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> LocationHttpRequest: ...
            def list(
                self,
                *,
                name: str,
                extraLocationTypes: str | _list[str] = ...,
                filter: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any,
            ) -> ListLocationsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListLocationsResponseHttpRequest,
                previous_response: ListLocationsResponse,
            ) -> ListLocationsResponseHttpRequest | None: ...
            def parameters(self) -> ParametersResource: ...

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
class ListLocationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListLocationsResponse: ...

@typing.type_check_only
class ListParameterVersionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListParameterVersionsResponse: ...

@typing.type_check_only
class ListParametersResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListParametersResponse: ...

@typing.type_check_only
class LocationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Location: ...

@typing.type_check_only
class ParameterHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Parameter: ...

@typing.type_check_only
class ParameterVersionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ParameterVersion: ...

@typing.type_check_only
class RenderParameterVersionResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> RenderParameterVersionResponse: ...
