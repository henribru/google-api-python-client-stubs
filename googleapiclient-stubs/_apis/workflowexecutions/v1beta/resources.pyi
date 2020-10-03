import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class WorkflowExecutionsResource(googleapiclient.discovery.Resource):
    class ProjectsResource(googleapiclient.discovery.Resource):
        class LocationsResource(googleapiclient.discovery.Resource):
            class WorkflowsResource(googleapiclient.discovery.Resource):
                class ExecutionsResource(googleapiclient.discovery.Resource):
                    def list(
                        self,
                        *,
                        parent: str,
                        view: typing_extensions.Literal[
                            "EXECUTION_VIEW_UNSPECIFIED", "BASIC", "FULL"
                        ] = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any
                    ) -> ListExecutionsResponseHttpRequest: ...
                    def get(
                        self,
                        *,
                        name: str,
                        view: typing_extensions.Literal[
                            "EXECUTION_VIEW_UNSPECIFIED", "BASIC", "FULL"
                        ] = ...,
                        **kwargs: typing.Any
                    ) -> ExecutionHttpRequest: ...
                    def create(
                        self,
                        *,
                        parent: str,
                        body: Execution = ...,
                        **kwargs: typing.Any
                    ) -> ExecutionHttpRequest: ...
                    def cancel(
                        self,
                        *,
                        name: str,
                        body: CancelExecutionRequest = ...,
                        **kwargs: typing.Any
                    ) -> ExecutionHttpRequest: ...
                def executions(self) -> ExecutionsResource: ...
            def workflows(self) -> WorkflowsResource: ...
        def locations(self) -> LocationsResource: ...
    def projects(self) -> ProjectsResource: ...

class ListExecutionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListExecutionsResponse: ...

class ExecutionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Execution: ...
