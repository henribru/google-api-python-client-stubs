import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class CloudSchedulerResource(googleapiclient.discovery.Resource):
    class ProjectsResource(googleapiclient.discovery.Resource):
        class LocationsResource(googleapiclient.discovery.Resource):
            class JobsResource(googleapiclient.discovery.Resource):
                def run(
                    self, *, name: str, body: RunJobRequest = ..., **kwargs: typing.Any
                ) -> JobHttpRequest: ...
                def get(self, *, name: str, **kwargs: typing.Any) -> JobHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageToken: str = ...,
                    pageSize: int = ...,
                    **kwargs: typing.Any
                ) -> ListJobsResponseHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: Job = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any
                ) -> JobHttpRequest: ...
                def resume(
                    self,
                    *,
                    name: str,
                    body: ResumeJobRequest = ...,
                    **kwargs: typing.Any
                ) -> JobHttpRequest: ...
                def pause(
                    self,
                    *,
                    name: str,
                    body: PauseJobRequest = ...,
                    **kwargs: typing.Any
                ) -> JobHttpRequest: ...
                def create(
                    self, *, parent: str, body: Job = ..., **kwargs: typing.Any
                ) -> JobHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> LocationHttpRequest: ...
            def list(
                self,
                *,
                name: str,
                pageSize: int = ...,
                pageToken: str = ...,
                filter: str = ...,
                **kwargs: typing.Any
            ) -> ListLocationsResponseHttpRequest: ...
            def jobs(self) -> JobsResource: ...
        def locations(self) -> LocationsResource: ...
    def projects(self) -> ProjectsResource: ...

class ListJobsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListJobsResponse: ...

class ListLocationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListLocationsResponse: ...

class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Empty: ...

class JobHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Job: ...

class LocationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Location: ...
