import collections.abc
import typing

import httplib2

import googleapiclient.discovery
import googleapiclient.http

from .schemas import *

_list = list

@typing.type_check_only
class IntegrationsResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class ProjectsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class LocationsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class IntegrationsResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class ExecutionsResource(googleapiclient.discovery.Resource):
                    @typing.type_check_only
                    class TaskExecutionsResource(googleapiclient.discovery.Resource):
                        def get(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> GoogleCloudIntegrationsV2TaskExecutionHttpRequest: ...

                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str | None = ...,
                        pageSize: int | None = ...,
                        pageToken: str | None = ...,
                        readMask: str | None = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudIntegrationsV2ListExecutionsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudIntegrationsV2ListExecutionsResponseHttpRequest,
                        previous_response: GoogleCloudIntegrationsV2ListExecutionsResponse,
                    ) -> (
                        GoogleCloudIntegrationsV2ListExecutionsResponseHttpRequest
                        | None
                    ): ...
                    def troubleshoot(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleCloudIntegrationsV2DuetTroubleshootExecutionResponseHttpRequest: ...
                    def taskExecutions(self) -> TaskExecutionsResource: ...

                def execute(
                    self,
                    *,
                    parent: str,
                    body: dict[str, typing.Any],
                    requestId: str | None = ...,
                    triggerId: str | None = ...,
                    **kwargs: typing.Any,
                ) -> GoogleApiHttpBodyHttpRequest: ...
                def generateIntegrationBranch(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudIntegrationsV2DuetGenerateIntegrationBranchRequest,
                    **kwargs: typing.Any,
                ) -> GoogleCloudIntegrationsV2DuetGenerateIntegrationBranchResponseHttpRequest: ...
                def generateIntegrationDocument(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudIntegrationsV2DuetGenerateIntegrationDocumentRequest,
                    **kwargs: typing.Any,
                ) -> GoogleCloudIntegrationsV2DuetGenerateIntegrationDocumentResponseHttpRequest: ...
                def generateJavascript(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudIntegrationsV2DuetGenerateJavascriptRequest,
                    **kwargs: typing.Any,
                ) -> (
                    GoogleCloudIntegrationsV2DuetGenerateJavascriptResponseHttpRequest
                ): ...
                def recommendTasks(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudIntegrationsV2DuetRecommendTasksRequest,
                    **kwargs: typing.Any,
                ) -> GoogleCloudIntegrationsV2DuetRecommendTasksResponseHttpRequest: ...
                def schedule(
                    self,
                    *,
                    parent: str,
                    body: dict[str, typing.Any],
                    requestId: str | None = ...,
                    scheduleTime: str | None = ...,
                    triggerId: str | None = ...,
                    **kwargs: typing.Any,
                ) -> GoogleApiHttpBodyHttpRequest: ...
                def executions(self) -> ExecutionsResource: ...

            def generateIntegration(
                self,
                *,
                parent: str,
                body: GoogleCloudIntegrationsV2DuetGenerateIntegrationRequest,
                **kwargs: typing.Any,
            ) -> (
                GoogleCloudIntegrationsV2DuetGenerateIntegrationResponseHttpRequest
            ): ...
            def integrations(self) -> IntegrationsResource: ...

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
class GoogleApiHttpBodyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleApiHttpBody: ...

@typing.type_check_only
class GoogleCloudIntegrationsV2DuetGenerateIntegrationBranchResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudIntegrationsV2DuetGenerateIntegrationBranchResponse: ...

@typing.type_check_only
class GoogleCloudIntegrationsV2DuetGenerateIntegrationDocumentResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudIntegrationsV2DuetGenerateIntegrationDocumentResponse: ...

@typing.type_check_only
class GoogleCloudIntegrationsV2DuetGenerateIntegrationResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudIntegrationsV2DuetGenerateIntegrationResponse: ...

@typing.type_check_only
class GoogleCloudIntegrationsV2DuetGenerateJavascriptResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudIntegrationsV2DuetGenerateJavascriptResponse: ...

@typing.type_check_only
class GoogleCloudIntegrationsV2DuetRecommendTasksResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudIntegrationsV2DuetRecommendTasksResponse: ...

@typing.type_check_only
class GoogleCloudIntegrationsV2DuetTroubleshootExecutionResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudIntegrationsV2DuetTroubleshootExecutionResponse: ...

@typing.type_check_only
class GoogleCloudIntegrationsV2ListExecutionsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudIntegrationsV2ListExecutionsResponse: ...

@typing.type_check_only
class GoogleCloudIntegrationsV2TaskExecutionHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudIntegrationsV2TaskExecution: ...
