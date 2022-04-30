import collections.abc
import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

_list = list

@typing.type_check_only
class WorkflowExecutionsResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class ProjectsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class LocationsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class WorkflowsResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class ExecutionsResource(googleapiclient.discovery.Resource):
                    def cancel(
                        self,
                        *,
                        name: str,
                        body: CancelExecutionRequest = ...,
                        **kwargs: typing.Any
                    ) -> ExecutionHttpRequest: ...
                    def create(
                        self,
                        *,
                        parent: str,
                        body: Execution = ...,
                        **kwargs: typing.Any
                    ) -> ExecutionHttpRequest: ...
                    def get(
                        self,
                        *,
                        name: str,
                        view: typing_extensions.Literal[
                            "EXECUTION_VIEW_UNSPECIFIED", "BASIC", "FULL"
                        ] = ...,
                        **kwargs: typing.Any
                    ) -> ExecutionHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        view: typing_extensions.Literal[
                            "EXECUTION_VIEW_UNSPECIFIED", "BASIC", "FULL"
                        ] = ...,
                        **kwargs: typing.Any
                    ) -> ListExecutionsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: ListExecutionsResponseHttpRequest,
                        previous_response: ListExecutionsResponse,
                    ) -> ListExecutionsResponseHttpRequest | None: ...

                def triggerPubsubExecution(
                    self,
                    *,
                    workflow: str,
                    body: TriggerPubsubExecutionRequest = ...,
                    **kwargs: typing.Any
                ) -> ExecutionHttpRequest: ...
                def executions(self) -> ExecutionsResource: ...

            def workflows(self) -> WorkflowsResource: ...

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
class ExecutionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Execution: ...

@typing.type_check_only
class ListExecutionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListExecutionsResponse: ...
