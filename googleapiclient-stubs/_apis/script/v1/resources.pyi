import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class ScriptResource(googleapiclient.discovery.Resource):
    class ScriptsResource(googleapiclient.discovery.Resource):
        def run(
            self, *, scriptId: str, body: ExecutionRequest = ..., **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
    class ProcessesResource(googleapiclient.discovery.Resource):
        def listScriptProcesses(
            self,
            *,
            scriptId: str = ...,
            scriptProcessFilter_statuses: typing.Union[
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
                ],
                typing.List[
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
                ],
            ] = ...,
            pageToken: str = ...,
            scriptProcessFilter_types: typing.Union[
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
                ],
                typing.List[
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
                ],
            ] = ...,
            scriptProcessFilter_deploymentId: str = ...,
            scriptProcessFilter_userAccessLevels: typing.Union[
                typing_extensions.Literal[
                    "USER_ACCESS_LEVEL_UNSPECIFIED", "NONE", "READ", "WRITE", "OWNER"
                ],
                typing.List[
                    typing_extensions.Literal[
                        "USER_ACCESS_LEVEL_UNSPECIFIED",
                        "NONE",
                        "READ",
                        "WRITE",
                        "OWNER",
                    ]
                ],
            ] = ...,
            scriptProcessFilter_startTime: str = ...,
            scriptProcessFilter_functionName: str = ...,
            pageSize: int = ...,
            scriptProcessFilter_endTime: str = ...,
            **kwargs: typing.Any
        ) -> ListScriptProcessesResponseHttpRequest: ...
        def list(
            self,
            *,
            userProcessFilter_deploymentId: str = ...,
            userProcessFilter_scriptId: str = ...,
            userProcessFilter_userAccessLevels: typing.Union[
                typing_extensions.Literal[
                    "USER_ACCESS_LEVEL_UNSPECIFIED", "NONE", "READ", "WRITE", "OWNER"
                ],
                typing.List[
                    typing_extensions.Literal[
                        "USER_ACCESS_LEVEL_UNSPECIFIED",
                        "NONE",
                        "READ",
                        "WRITE",
                        "OWNER",
                    ]
                ],
            ] = ...,
            userProcessFilter_types: typing.Union[
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
                ],
                typing.List[
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
                ],
            ] = ...,
            pageToken: str = ...,
            userProcessFilter_functionName: str = ...,
            userProcessFilter_startTime: str = ...,
            userProcessFilter_projectName: str = ...,
            userProcessFilter_statuses: typing.Union[
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
                ],
                typing.List[
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
                ],
            ] = ...,
            userProcessFilter_endTime: str = ...,
            pageSize: int = ...,
            **kwargs: typing.Any
        ) -> ListUserProcessesResponseHttpRequest: ...
    class ProjectsResource(googleapiclient.discovery.Resource):
        class DeploymentsResource(googleapiclient.discovery.Resource):
            def list(
                self,
                *,
                scriptId: str,
                pageToken: str = ...,
                pageSize: int = ...,
                **kwargs: typing.Any
            ) -> ListDeploymentsResponseHttpRequest: ...
            def delete(
                self, *, scriptId: str, deploymentId: str, **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def get(
                self, *, scriptId: str, deploymentId: str, **kwargs: typing.Any
            ) -> DeploymentHttpRequest: ...
            def update(
                self,
                *,
                scriptId: str,
                deploymentId: str,
                body: UpdateDeploymentRequest = ...,
                **kwargs: typing.Any
            ) -> DeploymentHttpRequest: ...
            def create(
                self,
                *,
                scriptId: str,
                body: DeploymentConfig = ...,
                **kwargs: typing.Any
            ) -> DeploymentHttpRequest: ...
        class VersionsResource(googleapiclient.discovery.Resource):
            def list(
                self,
                *,
                scriptId: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> ListVersionsResponseHttpRequest: ...
            def create(
                self, *, scriptId: str, body: Version = ..., **kwargs: typing.Any
            ) -> VersionHttpRequest: ...
            def get(
                self, *, scriptId: str, versionNumber: int, **kwargs: typing.Any
            ) -> VersionHttpRequest: ...
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
        def getContent(
            self, *, scriptId: str, versionNumber: int = ..., **kwargs: typing.Any
        ) -> ContentHttpRequest: ...
        def get(self, *, scriptId: str, **kwargs: typing.Any) -> ProjectHttpRequest: ...
        def create(
            self, *, body: CreateProjectRequest = ..., **kwargs: typing.Any
        ) -> ProjectHttpRequest: ...
        def updateContent(
            self, *, scriptId: str, body: Content = ..., **kwargs: typing.Any
        ) -> ContentHttpRequest: ...
        def deployments(self) -> DeploymentsResource: ...
        def versions(self) -> VersionsResource: ...
    def scripts(self) -> ScriptsResource: ...
    def processes(self) -> ProcessesResource: ...
    def projects(self) -> ProjectsResource: ...

class ListScriptProcessesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListScriptProcessesResponse: ...

class ListDeploymentsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListDeploymentsResponse: ...

class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Empty: ...

class ListUserProcessesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListUserProcessesResponse: ...

class DeploymentHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Deployment: ...

class ContentHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Content: ...

class VersionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Version: ...

class ProjectHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Project: ...

class OperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Operation: ...

class ListVersionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListVersionsResponse: ...

class MetricsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Metrics: ...
