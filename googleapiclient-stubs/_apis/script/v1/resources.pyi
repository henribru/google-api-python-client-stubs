import collections.abc
import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

_list = list

@typing.type_check_only
class ScriptResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class ProcessesResource(googleapiclient.discovery.Resource):
        def list(
            self,
            *,
            pageSize: int = ...,
            pageToken: str = ...,
            userProcessFilter_deploymentId: str = ...,
            userProcessFilter_endTime: str = ...,
            userProcessFilter_functionName: str = ...,
            userProcessFilter_projectName: str = ...,
            userProcessFilter_scriptId: str = ...,
            userProcessFilter_startTime: str = ...,
            userProcessFilter_statuses: typing_extensions.Literal[
                "PROCESS_STATUS_UNSPECIFIED",
                "RUNNING",
                "PAUSED",
                "COMPLETED",
                "CANCELED",
                "FAILED",
                "TIMED_OUT",
                "UNKNOWN",
                "DELAYED",
            ]
            | _list[
                typing_extensions.Literal[
                    "PROCESS_STATUS_UNSPECIFIED",
                    "RUNNING",
                    "PAUSED",
                    "COMPLETED",
                    "CANCELED",
                    "FAILED",
                    "TIMED_OUT",
                    "UNKNOWN",
                    "DELAYED",
                ]
            ] = ...,
            userProcessFilter_types: typing_extensions.Literal[
                "PROCESS_TYPE_UNSPECIFIED",
                "ADD_ON",
                "EXECUTION_API",
                "TIME_DRIVEN",
                "TRIGGER",
                "WEBAPP",
                "EDITOR",
                "SIMPLE_TRIGGER",
                "MENU",
                "BATCH_TASK",
            ]
            | _list[
                typing_extensions.Literal[
                    "PROCESS_TYPE_UNSPECIFIED",
                    "ADD_ON",
                    "EXECUTION_API",
                    "TIME_DRIVEN",
                    "TRIGGER",
                    "WEBAPP",
                    "EDITOR",
                    "SIMPLE_TRIGGER",
                    "MENU",
                    "BATCH_TASK",
                ]
            ] = ...,
            userProcessFilter_userAccessLevels: typing_extensions.Literal[
                "USER_ACCESS_LEVEL_UNSPECIFIED", "NONE", "READ", "WRITE", "OWNER"
            ]
            | _list[
                typing_extensions.Literal[
                    "USER_ACCESS_LEVEL_UNSPECIFIED", "NONE", "READ", "WRITE", "OWNER"
                ]
            ] = ...,
            **kwargs: typing.Any
        ) -> ListUserProcessesResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: ListUserProcessesResponseHttpRequest,
            previous_response: ListUserProcessesResponse,
        ) -> ListUserProcessesResponseHttpRequest | None: ...
        def listScriptProcesses(
            self,
            *,
            pageSize: int = ...,
            pageToken: str = ...,
            scriptId: str = ...,
            scriptProcessFilter_deploymentId: str = ...,
            scriptProcessFilter_endTime: str = ...,
            scriptProcessFilter_functionName: str = ...,
            scriptProcessFilter_startTime: str = ...,
            scriptProcessFilter_statuses: typing_extensions.Literal[
                "PROCESS_STATUS_UNSPECIFIED",
                "RUNNING",
                "PAUSED",
                "COMPLETED",
                "CANCELED",
                "FAILED",
                "TIMED_OUT",
                "UNKNOWN",
                "DELAYED",
            ]
            | _list[
                typing_extensions.Literal[
                    "PROCESS_STATUS_UNSPECIFIED",
                    "RUNNING",
                    "PAUSED",
                    "COMPLETED",
                    "CANCELED",
                    "FAILED",
                    "TIMED_OUT",
                    "UNKNOWN",
                    "DELAYED",
                ]
            ] = ...,
            scriptProcessFilter_types: typing_extensions.Literal[
                "PROCESS_TYPE_UNSPECIFIED",
                "ADD_ON",
                "EXECUTION_API",
                "TIME_DRIVEN",
                "TRIGGER",
                "WEBAPP",
                "EDITOR",
                "SIMPLE_TRIGGER",
                "MENU",
                "BATCH_TASK",
            ]
            | _list[
                typing_extensions.Literal[
                    "PROCESS_TYPE_UNSPECIFIED",
                    "ADD_ON",
                    "EXECUTION_API",
                    "TIME_DRIVEN",
                    "TRIGGER",
                    "WEBAPP",
                    "EDITOR",
                    "SIMPLE_TRIGGER",
                    "MENU",
                    "BATCH_TASK",
                ]
            ] = ...,
            scriptProcessFilter_userAccessLevels: typing_extensions.Literal[
                "USER_ACCESS_LEVEL_UNSPECIFIED", "NONE", "READ", "WRITE", "OWNER"
            ]
            | _list[
                typing_extensions.Literal[
                    "USER_ACCESS_LEVEL_UNSPECIFIED", "NONE", "READ", "WRITE", "OWNER"
                ]
            ] = ...,
            **kwargs: typing.Any
        ) -> ListScriptProcessesResponseHttpRequest: ...
        def listScriptProcesses_next(
            self,
            previous_request: ListScriptProcessesResponseHttpRequest,
            previous_response: ListScriptProcessesResponse,
        ) -> ListScriptProcessesResponseHttpRequest | None: ...

    @typing.type_check_only
    class ProjectsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class DeploymentsResource(googleapiclient.discovery.Resource):
            def create(
                self,
                *,
                scriptId: str,
                body: DeploymentConfig = ...,
                **kwargs: typing.Any
            ) -> DeploymentHttpRequest: ...
            def delete(
                self, *, scriptId: str, deploymentId: str, **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def get(
                self, *, scriptId: str, deploymentId: str, **kwargs: typing.Any
            ) -> DeploymentHttpRequest: ...
            def list(
                self,
                *,
                scriptId: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> ListDeploymentsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListDeploymentsResponseHttpRequest,
                previous_response: ListDeploymentsResponse,
            ) -> ListDeploymentsResponseHttpRequest | None: ...
            def update(
                self,
                *,
                scriptId: str,
                deploymentId: str,
                body: UpdateDeploymentRequest = ...,
                **kwargs: typing.Any
            ) -> DeploymentHttpRequest: ...

        @typing.type_check_only
        class VersionsResource(googleapiclient.discovery.Resource):
            def create(
                self, *, scriptId: str, body: Version = ..., **kwargs: typing.Any
            ) -> VersionHttpRequest: ...
            def get(
                self, *, scriptId: str, versionNumber: int, **kwargs: typing.Any
            ) -> VersionHttpRequest: ...
            def list(
                self,
                *,
                scriptId: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> ListVersionsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListVersionsResponseHttpRequest,
                previous_response: ListVersionsResponse,
            ) -> ListVersionsResponseHttpRequest | None: ...

        def create(
            self, *, body: CreateProjectRequest = ..., **kwargs: typing.Any
        ) -> ProjectHttpRequest: ...
        def get(self, *, scriptId: str, **kwargs: typing.Any) -> ProjectHttpRequest: ...
        def getContent(
            self, *, scriptId: str, versionNumber: int = ..., **kwargs: typing.Any
        ) -> ContentHttpRequest: ...
        def getMetrics(
            self,
            *,
            scriptId: str,
            metricsFilter_deploymentId: str = ...,
            metricsGranularity: typing_extensions.Literal[
                "UNSPECIFIED_GRANULARITY", "WEEKLY", "DAILY"
            ] = ...,
            **kwargs: typing.Any
        ) -> MetricsHttpRequest: ...
        def updateContent(
            self, *, scriptId: str, body: Content = ..., **kwargs: typing.Any
        ) -> ContentHttpRequest: ...
        def deployments(self) -> DeploymentsResource: ...
        def versions(self) -> VersionsResource: ...

    @typing.type_check_only
    class ScriptsResource(googleapiclient.discovery.Resource):
        def run(
            self, *, scriptId: str, body: ExecutionRequest = ..., **kwargs: typing.Any
        ) -> OperationHttpRequest: ...

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
    def processes(self) -> ProcessesResource: ...
    def projects(self) -> ProjectsResource: ...
    def scripts(self) -> ScriptsResource: ...

@typing.type_check_only
class ContentHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Content: ...

@typing.type_check_only
class DeploymentHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Deployment: ...

@typing.type_check_only
class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Empty: ...

@typing.type_check_only
class ListDeploymentsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListDeploymentsResponse: ...

@typing.type_check_only
class ListScriptProcessesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListScriptProcessesResponse: ...

@typing.type_check_only
class ListUserProcessesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListUserProcessesResponse: ...

@typing.type_check_only
class ListVersionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListVersionsResponse: ...

@typing.type_check_only
class MetricsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Metrics: ...

@typing.type_check_only
class OperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Operation: ...

@typing.type_check_only
class ProjectHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Project: ...

@typing.type_check_only
class VersionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Version: ...
