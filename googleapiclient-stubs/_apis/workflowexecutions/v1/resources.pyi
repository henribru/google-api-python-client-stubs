import collections.abc
import typing

import httplib2
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http

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
                    @typing.type_check_only
                    class CallbacksResource(googleapiclient.discovery.Resource):
                        def list(
                            self,
                            *,
                            parent: str,
                            pageSize: int = ...,
                            pageToken: str = ...,
                            **kwargs: typing.Any,
                        ) -> ListCallbacksResponseHttpRequest: ...
                        def list_next(
                            self,
                            previous_request: ListCallbacksResponseHttpRequest,
                            previous_response: ListCallbacksResponse,
                        ) -> ListCallbacksResponseHttpRequest | None: ...

                    @typing.type_check_only
                    class StepEntriesResource(googleapiclient.discovery.Resource):
                        def get(
                            self,
                            *,
                            name: str,
                            view: typing_extensions.Literal[
                                "EXECUTION_ENTRY_VIEW_UNSPECIFIED",
                                "EXECUTION_ENTRY_VIEW_BASIC",
                                "EXECUTION_ENTRY_VIEW_DETAILED",
                            ] = ...,
                            **kwargs: typing.Any,
                        ) -> StepEntryHttpRequest: ...
                        def list(
                            self,
                            *,
                            parent: str,
                            filter: str = ...,
                            orderBy: str = ...,
                            pageSize: int = ...,
                            pageToken: str = ...,
                            skip: int = ...,
                            view: typing_extensions.Literal[
                                "EXECUTION_ENTRY_VIEW_UNSPECIFIED",
                                "EXECUTION_ENTRY_VIEW_BASIC",
                                "EXECUTION_ENTRY_VIEW_DETAILED",
                            ] = ...,
                            **kwargs: typing.Any,
                        ) -> ListStepEntriesResponseHttpRequest: ...
                        def list_next(
                            self,
                            previous_request: ListStepEntriesResponseHttpRequest,
                            previous_response: ListStepEntriesResponse,
                        ) -> ListStepEntriesResponseHttpRequest | None: ...

                    def cancel(
                        self,
                        *,
                        name: str,
                        body: CancelExecutionRequest = ...,
                        **kwargs: typing.Any,
                    ) -> ExecutionHttpRequest: ...
                    def create(
                        self,
                        *,
                        parent: str,
                        body: Execution = ...,
                        **kwargs: typing.Any,
                    ) -> ExecutionHttpRequest: ...
                    def deleteExecutionHistory(
                        self,
                        *,
                        name: str,
                        body: DeleteExecutionHistoryRequest = ...,
                        **kwargs: typing.Any,
                    ) -> EmptyHttpRequest: ...
                    def exportData(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> ExportDataResponseHttpRequest: ...
                    def get(
                        self,
                        *,
                        name: str,
                        view: typing_extensions.Literal[
                            "EXECUTION_VIEW_UNSPECIFIED", "BASIC", "FULL"
                        ] = ...,
                        **kwargs: typing.Any,
                    ) -> ExecutionHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str = ...,
                        orderBy: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        view: typing_extensions.Literal[
                            "EXECUTION_VIEW_UNSPECIFIED", "BASIC", "FULL"
                        ] = ...,
                        **kwargs: typing.Any,
                    ) -> ListExecutionsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: ListExecutionsResponseHttpRequest,
                        previous_response: ListExecutionsResponse,
                    ) -> ListExecutionsResponseHttpRequest | None: ...
                    def callbacks(self) -> CallbacksResource: ...
                    def stepEntries(self) -> StepEntriesResource: ...

                def triggerPubsubExecution(
                    self,
                    *,
                    workflow: str,
                    body: TriggerPubsubExecutionRequest = ...,
                    **kwargs: typing.Any,
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
class ExecutionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Execution: ...

@typing.type_check_only
class ExportDataResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ExportDataResponse: ...

@typing.type_check_only
class ListCallbacksResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListCallbacksResponse: ...

@typing.type_check_only
class ListExecutionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListExecutionsResponse: ...

@typing.type_check_only
class ListStepEntriesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListStepEntriesResponse: ...

@typing.type_check_only
class StepEntryHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> StepEntry: ...
