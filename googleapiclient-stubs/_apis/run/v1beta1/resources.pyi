import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class CloudRunResource(googleapiclient.discovery.Resource):
    class CustomresourcedefinitionsResource(googleapiclient.discovery.Resource):
        def list(
            self,
            *,
            parent: str = ...,
            resourceVersion: str = ...,
            fieldSelector: str = ...,
            limit: int = ...,
            watch: bool = ...,
            labelSelector: str = ...,
            includeUninitialized: bool = ...,
            **kwargs: typing.Any
        ) -> ListCustomResourceDefinitionsResponseHttpRequest: ...
    class NamespacesResource(googleapiclient.discovery.Resource):
        class CustomresourcedefinitionsResource(googleapiclient.discovery.Resource):
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> CustomResourceDefinitionHttpRequest: ...
        def customresourcedefinitions(self) -> CustomresourcedefinitionsResource: ...
    class ProjectsResource(googleapiclient.discovery.Resource):
        class LocationsResource(googleapiclient.discovery.Resource):
            class CustomresourcedefinitionsResource(googleapiclient.discovery.Resource):
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> CustomResourceDefinitionHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    includeUninitialized: bool = ...,
                    resourceVersion: str = ...,
                    limit: int = ...,
                    fieldSelector: str = ...,
                    labelSelector: str = ...,
                    watch: bool = ...,
                    **kwargs: typing.Any
                ) -> ListCustomResourceDefinitionsResponseHttpRequest: ...
            def customresourcedefinitions(
                self,
            ) -> CustomresourcedefinitionsResource: ...
        def locations(self) -> LocationsResource: ...
    def customresourcedefinitions(self) -> CustomresourcedefinitionsResource: ...
    def namespaces(self) -> NamespacesResource: ...
    def projects(self) -> ProjectsResource: ...

class CustomResourceDefinitionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> CustomResourceDefinition: ...

class ListCustomResourceDefinitionsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListCustomResourceDefinitionsResponse: ...
