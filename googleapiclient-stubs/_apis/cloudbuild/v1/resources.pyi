import collections.abc
import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

_list = list

@typing.type_check_only
class CloudBuildResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class OperationsResource(googleapiclient.discovery.Resource):
        def cancel(
            self, *, name: str, body: CancelOperationRequest = ..., **kwargs: typing.Any
        ) -> EmptyHttpRequest: ...
        def get(self, *, name: str, **kwargs: typing.Any) -> OperationHttpRequest: ...
    @typing.type_check_only
    class ProjectsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class BuildsResource(googleapiclient.discovery.Resource):
            def approve(
                self,
                *,
                name: str,
                body: ApproveBuildRequest = ...,
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
            def create(
                self,
                *,
                projectId: str,
                body: Build = ...,
                parent: str = ...,
                **kwargs: typing.Any
            ) -> OperationHttpRequest: ...
            def get(
                self, *, projectId: str, id: str, name: str = ..., **kwargs: typing.Any
            ) -> BuildHttpRequest: ...
            def list(
                self,
                *,
                projectId: str,
                filter: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                parent: str = ...,
                **kwargs: typing.Any
            ) -> ListBuildsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListBuildsResponseHttpRequest,
                previous_response: ListBuildsResponse,
            ) -> ListBuildsResponseHttpRequest | None: ...
            def retry(
                self,
                *,
                projectId: str,
                id: str,
                body: RetryBuildRequest = ...,
                **kwargs: typing.Any
            ) -> OperationHttpRequest: ...
        @typing.type_check_only
        class GithubEnterpriseConfigsResource(googleapiclient.discovery.Resource):
            def create(
                self,
                *,
                parent: str,
                body: GitHubEnterpriseConfig = ...,
                projectId: str = ...,
                **kwargs: typing.Any
            ) -> OperationHttpRequest: ...
            def delete(
                self,
                *,
                name: str,
                configId: str = ...,
                projectId: str = ...,
                **kwargs: typing.Any
            ) -> OperationHttpRequest: ...
            def get(
                self,
                *,
                name: str,
                configId: str = ...,
                projectId: str = ...,
                **kwargs: typing.Any
            ) -> GitHubEnterpriseConfigHttpRequest: ...
            def list(
                self, *, parent: str, projectId: str = ..., **kwargs: typing.Any
            ) -> ListGithubEnterpriseConfigsResponseHttpRequest: ...
            def patch(
                self,
                *,
                name: str,
                body: GitHubEnterpriseConfig = ...,
                updateMask: str = ...,
                **kwargs: typing.Any
            ) -> OperationHttpRequest: ...
        @typing.type_check_only
        class LocationsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class BuildsResource(googleapiclient.discovery.Resource):
                def approve(
                    self,
                    *,
                    name: str,
                    body: ApproveBuildRequest = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def cancel(
                    self,
                    *,
                    name: str,
                    body: CancelBuildRequest = ...,
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
                def get(
                    self,
                    *,
                    name: str,
                    id: str = ...,
                    projectId: str = ...,
                    **kwargs: typing.Any
                ) -> BuildHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    projectId: str = ...,
                    **kwargs: typing.Any
                ) -> ListBuildsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListBuildsResponseHttpRequest,
                    previous_response: ListBuildsResponse,
                ) -> ListBuildsResponseHttpRequest | None: ...
                def retry(
                    self,
                    *,
                    name: str,
                    body: RetryBuildRequest = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
            @typing.type_check_only
            class GithubEnterpriseConfigsResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: GitHubEnterpriseConfig = ...,
                    projectId: str = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def delete(
                    self,
                    *,
                    name: str,
                    configId: str = ...,
                    projectId: str = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def get(
                    self,
                    *,
                    name: str,
                    configId: str = ...,
                    projectId: str = ...,
                    **kwargs: typing.Any
                ) -> GitHubEnterpriseConfigHttpRequest: ...
                def list(
                    self, *, parent: str, projectId: str = ..., **kwargs: typing.Any
                ) -> ListGithubEnterpriseConfigsResponseHttpRequest: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GitHubEnterpriseConfig = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
            @typing.type_check_only
            class OperationsResource(googleapiclient.discovery.Resource):
                def cancel(
                    self,
                    *,
                    name: str,
                    body: CancelOperationRequest = ...,
                    **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
            @typing.type_check_only
            class TriggersResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: BuildTrigger = ...,
                    projectId: str = ...,
                    **kwargs: typing.Any
                ) -> BuildTriggerHttpRequest: ...
                def delete(
                    self,
                    *,
                    name: str,
                    projectId: str = ...,
                    triggerId: str = ...,
                    **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def get(
                    self,
                    *,
                    name: str,
                    projectId: str = ...,
                    triggerId: str = ...,
                    **kwargs: typing.Any
                ) -> BuildTriggerHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    projectId: str = ...,
                    **kwargs: typing.Any
                ) -> ListBuildTriggersResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListBuildTriggersResponseHttpRequest,
                    previous_response: ListBuildTriggersResponse,
                ) -> ListBuildTriggersResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    resourceName: str,
                    body: BuildTrigger = ...,
                    projectId: str = ...,
                    triggerId: str = ...,
                    **kwargs: typing.Any
                ) -> BuildTriggerHttpRequest: ...
                def run(
                    self,
                    *,
                    name: str,
                    body: RunBuildTriggerRequest = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def webhook(
                    self,
                    *,
                    name: str,
                    body: HttpBody = ...,
                    projectId: str = ...,
                    secret: str = ...,
                    trigger: str = ...,
                    **kwargs: typing.Any
                ) -> ReceiveTriggerWebhookResponseHttpRequest: ...
            @typing.type_check_only
            class WorkerPoolsResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: WorkerPool = ...,
                    validateOnly: bool = ...,
                    workerPoolId: str = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def delete(
                    self,
                    *,
                    name: str,
                    allowMissing: bool = ...,
                    etag: str = ...,
                    validateOnly: bool = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> WorkerPoolHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> ListWorkerPoolsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListWorkerPoolsResponseHttpRequest,
                    previous_response: ListWorkerPoolsResponse,
                ) -> ListWorkerPoolsResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: WorkerPool = ...,
                    updateMask: str = ...,
                    validateOnly: bool = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
            def builds(self) -> BuildsResource: ...
            def githubEnterpriseConfigs(self) -> GithubEnterpriseConfigsResource: ...
            def operations(self) -> OperationsResource: ...
            def triggers(self) -> TriggersResource: ...
            def workerPools(self) -> WorkerPoolsResource: ...
        @typing.type_check_only
        class TriggersResource(googleapiclient.discovery.Resource):
            def create(
                self,
                *,
                projectId: str,
                body: BuildTrigger = ...,
                parent: str = ...,
                **kwargs: typing.Any
            ) -> BuildTriggerHttpRequest: ...
            def delete(
                self,
                *,
                projectId: str,
                triggerId: str,
                name: str = ...,
                **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def get(
                self,
                *,
                projectId: str,
                triggerId: str,
                name: str = ...,
                **kwargs: typing.Any
            ) -> BuildTriggerHttpRequest: ...
            def list(
                self,
                *,
                projectId: str,
                pageSize: int = ...,
                pageToken: str = ...,
                parent: str = ...,
                **kwargs: typing.Any
            ) -> ListBuildTriggersResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListBuildTriggersResponseHttpRequest,
                previous_response: ListBuildTriggersResponse,
            ) -> ListBuildTriggersResponseHttpRequest | None: ...
            def patch(
                self,
                *,
                projectId: str,
                triggerId: str,
                body: BuildTrigger = ...,
                **kwargs: typing.Any
            ) -> BuildTriggerHttpRequest: ...
            def run(
                self,
                *,
                projectId: str,
                triggerId: str,
                body: RepoSource = ...,
                name: str = ...,
                **kwargs: typing.Any
            ) -> OperationHttpRequest: ...
            def webhook(
                self,
                *,
                projectId: str,
                trigger: str,
                body: HttpBody = ...,
                name: str = ...,
                secret: str = ...,
                **kwargs: typing.Any
            ) -> ReceiveTriggerWebhookResponseHttpRequest: ...
        def builds(self) -> BuildsResource: ...
        def githubEnterpriseConfigs(self) -> GithubEnterpriseConfigsResource: ...
        def locations(self) -> LocationsResource: ...
        def triggers(self) -> TriggersResource: ...
    @typing.type_check_only
    class V1Resource(googleapiclient.discovery.Resource):
        def webhook(
            self, *, body: HttpBody = ..., webhookKey: str = ..., **kwargs: typing.Any
        ) -> EmptyHttpRequest: ...
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
    def operations(self) -> OperationsResource: ...
    def projects(self) -> ProjectsResource: ...
    def v1(self) -> V1Resource: ...

@typing.type_check_only
class BuildHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Build: ...

@typing.type_check_only
class BuildTriggerHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> BuildTrigger: ...

@typing.type_check_only
class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Empty: ...

@typing.type_check_only
class GitHubEnterpriseConfigHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GitHubEnterpriseConfig: ...

@typing.type_check_only
class ListBuildTriggersResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListBuildTriggersResponse: ...

@typing.type_check_only
class ListBuildsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListBuildsResponse: ...

@typing.type_check_only
class ListGithubEnterpriseConfigsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListGithubEnterpriseConfigsResponse: ...

@typing.type_check_only
class ListWorkerPoolsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListWorkerPoolsResponse: ...

@typing.type_check_only
class OperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Operation: ...

@typing.type_check_only
class ReceiveTriggerWebhookResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ReceiveTriggerWebhookResponse: ...

@typing.type_check_only
class WorkerPoolHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> WorkerPool: ...
