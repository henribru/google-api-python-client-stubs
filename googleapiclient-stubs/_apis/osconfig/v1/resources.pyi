import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class SystemsManagementResource(googleapiclient.discovery.Resource):
    class ProjectsResource(googleapiclient.discovery.Resource):
        class PatchDeploymentsResource(googleapiclient.discovery.Resource):
            def create(
                self,
                *,
                parent: str,
                body: PatchDeployment = ...,
                patchDeploymentId: str = ...,
                **kwargs: typing.Any
            ) -> PatchDeploymentHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> PatchDeploymentHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageToken: str = ...,
                pageSize: int = ...,
                **kwargs: typing.Any
            ) -> ListPatchDeploymentsResponseHttpRequest: ...
        class PatchJobsResource(googleapiclient.discovery.Resource):
            class InstanceDetailsResource(googleapiclient.discovery.Resource):
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> ListPatchJobInstanceDetailsResponseHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> PatchJobHttpRequest: ...
            def cancel(
                self,
                *,
                name: str,
                body: CancelPatchJobRequest = ...,
                **kwargs: typing.Any
            ) -> PatchJobHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageToken: str = ...,
                filter: str = ...,
                pageSize: int = ...,
                **kwargs: typing.Any
            ) -> ListPatchJobsResponseHttpRequest: ...
            def execute(
                self,
                *,
                parent: str,
                body: ExecutePatchJobRequest = ...,
                **kwargs: typing.Any
            ) -> PatchJobHttpRequest: ...
            def instanceDetails(self) -> InstanceDetailsResource: ...
        def patchDeployments(self) -> PatchDeploymentsResource: ...
        def patchJobs(self) -> PatchJobsResource: ...
    def projects(self) -> ProjectsResource: ...

class ListPatchJobInstanceDetailsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListPatchJobInstanceDetailsResponse: ...

class ListPatchJobsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListPatchJobsResponse: ...

class ListPatchDeploymentsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListPatchDeploymentsResponse: ...

class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Empty: ...

class PatchJobHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> PatchJob: ...

class PatchDeploymentHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> PatchDeployment: ...
