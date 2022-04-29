import collections.abc
import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

_list = list

@typing.type_check_only
class CloudRunResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class CustomresourcedefinitionsResource(googleapiclient.discovery.Resource):
        def list(
            self,
            *,
            fieldSelector: str = ...,
            includeUninitialized: bool = ...,
            labelSelector: str = ...,
            limit: int = ...,
            parent: str = ...,
            resourceVersion: str = ...,
            watch: bool = ...,
            **kwargs: typing.Any
        ) -> ListCustomResourceDefinitionsResponseHttpRequest: ...

    @typing.type_check_only
    class NamespacesResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class CustomresourcedefinitionsResource(googleapiclient.discovery.Resource):
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> CustomResourceDefinitionHttpRequest: ...

        def customresourcedefinitions(self) -> CustomresourcedefinitionsResource: ...

    @typing.type_check_only
    class ProjectsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class LocationsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class CustomresourcedefinitionsResource(googleapiclient.discovery.Resource):
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> CustomResourceDefinitionHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    fieldSelector: str = ...,
                    includeUninitialized: bool = ...,
                    labelSelector: str = ...,
                    limit: int = ...,
                    resourceVersion: str = ...,
                    watch: bool = ...,
                    **kwargs: typing.Any
                ) -> ListCustomResourceDefinitionsResponseHttpRequest: ...

            def customresourcedefinitions(
                self,
            ) -> CustomresourcedefinitionsResource: ...

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
    def customresourcedefinitions(self) -> CustomresourcedefinitionsResource: ...
    def namespaces(self) -> NamespacesResource: ...
    def projects(self) -> ProjectsResource: ...

@typing.type_check_only
class CustomResourceDefinitionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> CustomResourceDefinition: ...

@typing.type_check_only
class ListCustomResourceDefinitionsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListCustomResourceDefinitionsResponse: ...
