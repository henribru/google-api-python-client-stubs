import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class CloudBuildResource(googleapiclient.discovery.Resource):
    class OperationsResource(googleapiclient.discovery.Resource):
        def get(self, *, name: str, **kwargs: typing.Any) -> OperationHttpRequest: ...
        def cancel(
            self, *, name: str, body: CancelOperationRequest = ..., **kwargs: typing.Any
        ) -> EmptyHttpRequest: ...
    class ProjectsResource(googleapiclient.discovery.Resource):
        class LocationsResource(googleapiclient.discovery.Resource):
            class OperationsResource(googleapiclient.discovery.Resource):
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def cancel(
                    self,
                    *,
                    name: str,
                    body: CancelOperationRequest = ...,
                    **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
            class BuildsResource(googleapiclient.discovery.Resource):
                def retry(
                    self,
                    *,
                    name: str,
                    body: RetryBuildRequest = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def get(
                    self,
                    *,
                    name: str,
                    id: str = ...,
                    projectId: str = ...,
                    **kwargs: typing.Any
                ) -> BuildHttpRequest: ...
                def create(
                    self,
                    *,
                    parent: str,
                    body: Build = ...,
                    projectId: str = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageToken: str = ...,
                    filter: str = ...,
                    pageSize: int = ...,
                    projectId: str = ...,
                    **kwargs: typing.Any
                ) -> ListBuildsResponseHttpRequest: ...
                def cancel(
                    self,
                    *,
                    name: str,
                    body: CancelBuildRequest = ...,
                    **kwargs: typing.Any
                ) -> BuildHttpRequest: ...
            def operations(self) -> OperationsResource: ...
            def builds(self) -> BuildsResource: ...
        class TriggersResource(googleapiclient.discovery.Resource):
            def create(
                self, *, projectId: str, body: BuildTrigger = ..., **kwargs: typing.Any
            ) -> BuildTriggerHttpRequest: ...
            def patch(
                self,
                *,
                projectId: str,
                triggerId: str,
                body: BuildTrigger = ...,
                **kwargs: typing.Any
            ) -> BuildTriggerHttpRequest: ...
            def delete(
                self, *, projectId: str, triggerId: str, **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def run(
                self,
                *,
                projectId: str,
                triggerId: str,
                body: RepoSource = ...,
                **kwargs: typing.Any
            ) -> OperationHttpRequest: ...
            def get(
                self, *, projectId: str, triggerId: str, **kwargs: typing.Any
            ) -> BuildTriggerHttpRequest: ...
            def list(
                self,
                *,
                projectId: str,
                pageToken: str = ...,
                pageSize: int = ...,
                **kwargs: typing.Any
            ) -> ListBuildTriggersResponseHttpRequest: ...
        class BuildsResource(googleapiclient.discovery.Resource):
            def create(
                self,
                *,
                projectId: str,
                body: Build = ...,
                parent: str = ...,
                **kwargs: typing.Any
            ) -> OperationHttpRequest: ...
            def retry(
                self,
                *,
                projectId: str,
                id: str,
                body: RetryBuildRequest = ...,
                **kwargs: typing.Any
            ) -> OperationHttpRequest: ...
            def cancel(
                self,
                *,
                projectId: str,
                id: str,
                body: CancelBuildRequest = ...,
                **kwargs: typing.Any
            ) -> BuildHttpRequest: ...
            def get(
                self, *, projectId: str, id: str, name: str = ..., **kwargs: typing.Any
            ) -> BuildHttpRequest: ...
            def list(
                self,
                *,
                projectId: str,
                pageSize: int = ...,
                filter: str = ...,
                parent: str = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> ListBuildsResponseHttpRequest: ...
        def locations(self) -> LocationsResource: ...
        def triggers(self) -> TriggersResource: ...
        def builds(self) -> BuildsResource: ...
    def operations(self) -> OperationsResource: ...
    def projects(self) -> ProjectsResource: ...

class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Empty: ...

class ListBuildTriggersResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListBuildTriggersResponse: ...

class ListBuildsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListBuildsResponse: ...

class BuildTriggerHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> BuildTrigger: ...

class BuildHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Build: ...

class OperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Operation: ...
