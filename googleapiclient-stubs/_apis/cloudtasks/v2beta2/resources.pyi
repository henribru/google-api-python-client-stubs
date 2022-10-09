import collections.abc
import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

_list = list

@typing.type_check_only
class CloudTasksResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class ApiResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class QueueResource(googleapiclient.discovery.Resource):
            def update(
                self, *, body: HttpBody = ..., appId: str = ..., **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...

        def queue(self) -> QueueResource: ...

    @typing.type_check_only
    class ProjectsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class LocationsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class QueuesResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class TasksResource(googleapiclient.discovery.Resource):
                    def acknowledge(
                        self,
                        *,
                        name: str,
                        body: AcknowledgeTaskRequest = ...,
                        **kwargs: typing.Any
                    ) -> EmptyHttpRequest: ...
                    def buffer(
                        self,
                        *,
                        queue: str,
                        taskId: str,
                        body: BufferTaskRequest = ...,
                        **kwargs: typing.Any
                    ) -> BufferTaskResponseHttpRequest: ...
                    def cancelLease(
                        self,
                        *,
                        name: str,
                        body: CancelLeaseRequest = ...,
                        **kwargs: typing.Any
                    ) -> TaskHttpRequest: ...
                    def create(
                        self,
                        *,
                        parent: str,
                        body: CreateTaskRequest = ...,
                        **kwargs: typing.Any
                    ) -> TaskHttpRequest: ...
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> EmptyHttpRequest: ...
                    def get(
                        self,
                        *,
                        name: str,
                        responseView: typing_extensions.Literal[
                            "VIEW_UNSPECIFIED", "BASIC", "FULL"
                        ] = ...,
                        **kwargs: typing.Any
                    ) -> TaskHttpRequest: ...
                    def lease(
                        self,
                        *,
                        parent: str,
                        body: LeaseTasksRequest = ...,
                        **kwargs: typing.Any
                    ) -> LeaseTasksResponseHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        responseView: typing_extensions.Literal[
                            "VIEW_UNSPECIFIED", "BASIC", "FULL"
                        ] = ...,
                        **kwargs: typing.Any
                    ) -> ListTasksResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: ListTasksResponseHttpRequest,
                        previous_response: ListTasksResponse,
                    ) -> ListTasksResponseHttpRequest | None: ...
                    def renewLease(
                        self,
                        *,
                        name: str,
                        body: RenewLeaseRequest = ...,
                        **kwargs: typing.Any
                    ) -> TaskHttpRequest: ...
                    def run(
                        self,
                        *,
                        name: str,
                        body: RunTaskRequest = ...,
                        **kwargs: typing.Any
                    ) -> TaskHttpRequest: ...

                def create(
                    self, *, parent: str, body: Queue = ..., **kwargs: typing.Any
                ) -> QueueHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def get(
                    self, *, name: str, readMask: str = ..., **kwargs: typing.Any
                ) -> QueueHttpRequest: ...
                def getIamPolicy(
                    self,
                    *,
                    resource: str,
                    body: GetIamPolicyRequest = ...,
                    **kwargs: typing.Any
                ) -> PolicyHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    readMask: str = ...,
                    **kwargs: typing.Any
                ) -> ListQueuesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListQueuesResponseHttpRequest,
                    previous_response: ListQueuesResponse,
                ) -> ListQueuesResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: Queue = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any
                ) -> QueueHttpRequest: ...
                def pause(
                    self,
                    *,
                    name: str,
                    body: PauseQueueRequest = ...,
                    **kwargs: typing.Any
                ) -> QueueHttpRequest: ...
                def purge(
                    self,
                    *,
                    name: str,
                    body: PurgeQueueRequest = ...,
                    **kwargs: typing.Any
                ) -> QueueHttpRequest: ...
                def resume(
                    self,
                    *,
                    name: str,
                    body: ResumeQueueRequest = ...,
                    **kwargs: typing.Any
                ) -> QueueHttpRequest: ...
                def setIamPolicy(
                    self,
                    *,
                    resource: str,
                    body: SetIamPolicyRequest = ...,
                    **kwargs: typing.Any
                ) -> PolicyHttpRequest: ...
                def testIamPermissions(
                    self,
                    *,
                    resource: str,
                    body: TestIamPermissionsRequest = ...,
                    **kwargs: typing.Any
                ) -> TestIamPermissionsResponseHttpRequest: ...
                def tasks(self) -> TasksResource: ...

            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> LocationHttpRequest: ...
            def list(
                self,
                *,
                name: str,
                filter: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> ListLocationsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListLocationsResponseHttpRequest,
                previous_response: ListLocationsResponse,
            ) -> ListLocationsResponseHttpRequest | None: ...
            def queues(self) -> QueuesResource: ...

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
    def api(self) -> ApiResource: ...
    def projects(self) -> ProjectsResource: ...

@typing.type_check_only
class BufferTaskResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> BufferTaskResponse: ...

@typing.type_check_only
class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Empty: ...

@typing.type_check_only
class LeaseTasksResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> LeaseTasksResponse: ...

@typing.type_check_only
class ListLocationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListLocationsResponse: ...

@typing.type_check_only
class ListQueuesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListQueuesResponse: ...

@typing.type_check_only
class ListTasksResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListTasksResponse: ...

@typing.type_check_only
class LocationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Location: ...

@typing.type_check_only
class PolicyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Policy: ...

@typing.type_check_only
class QueueHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Queue: ...

@typing.type_check_only
class TaskHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Task: ...

@typing.type_check_only
class TestIamPermissionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> TestIamPermissionsResponse: ...
