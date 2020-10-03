import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class CloudTasksResource(googleapiclient.discovery.Resource):
    class ProjectsResource(googleapiclient.discovery.Resource):
        class LocationsResource(googleapiclient.discovery.Resource):
            class QueuesResource(googleapiclient.discovery.Resource):
                class TasksResource(googleapiclient.discovery.Resource):
                    def run(
                        self,
                        *,
                        name: str,
                        body: RunTaskRequest = ...,
                        **kwargs: typing.Any
                    ) -> TaskHttpRequest: ...
                    def cancelLease(
                        self,
                        *,
                        name: str,
                        body: CancelLeaseRequest = ...,
                        **kwargs: typing.Any
                    ) -> TaskHttpRequest: ...
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> EmptyHttpRequest: ...
                    def create(
                        self,
                        *,
                        parent: str,
                        body: CreateTaskRequest = ...,
                        **kwargs: typing.Any
                    ) -> TaskHttpRequest: ...
                    def lease(
                        self,
                        *,
                        parent: str,
                        body: LeaseTasksRequest = ...,
                        **kwargs: typing.Any
                    ) -> LeaseTasksResponseHttpRequest: ...
                    def get(
                        self,
                        *,
                        name: str,
                        responseView: typing_extensions.Literal[
                            "VIEW_UNSPECIFIED", "BASIC", "FULL"
                        ] = ...,
                        **kwargs: typing.Any
                    ) -> TaskHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        responseView: typing_extensions.Literal[
                            "VIEW_UNSPECIFIED", "BASIC", "FULL"
                        ] = ...,
                        pageToken: str = ...,
                        pageSize: int = ...,
                        **kwargs: typing.Any
                    ) -> ListTasksResponseHttpRequest: ...
                    def acknowledge(
                        self,
                        *,
                        name: str,
                        body: AcknowledgeTaskRequest = ...,
                        **kwargs: typing.Any
                    ) -> EmptyHttpRequest: ...
                    def renewLease(
                        self,
                        *,
                        name: str,
                        body: RenewLeaseRequest = ...,
                        **kwargs: typing.Any
                    ) -> TaskHttpRequest: ...
                def purge(
                    self,
                    *,
                    name: str,
                    body: PurgeQueueRequest = ...,
                    **kwargs: typing.Any
                ) -> QueueHttpRequest: ...
                def pause(
                    self,
                    *,
                    name: str,
                    body: PauseQueueRequest = ...,
                    **kwargs: typing.Any
                ) -> QueueHttpRequest: ...
                def testIamPermissions(
                    self,
                    *,
                    resource: str,
                    body: TestIamPermissionsRequest = ...,
                    **kwargs: typing.Any
                ) -> TestIamPermissionsResponseHttpRequest: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: Queue = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any
                ) -> QueueHttpRequest: ...
                def get(
                    self, *, name: str, readMask: str = ..., **kwargs: typing.Any
                ) -> QueueHttpRequest: ...
                def setIamPolicy(
                    self,
                    *,
                    resource: str,
                    body: SetIamPolicyRequest = ...,
                    **kwargs: typing.Any
                ) -> PolicyHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    pageToken: str = ...,
                    pageSize: int = ...,
                    **kwargs: typing.Any
                ) -> ListQueuesResponseHttpRequest: ...
                def getIamPolicy(
                    self,
                    *,
                    resource: str,
                    body: GetIamPolicyRequest = ...,
                    **kwargs: typing.Any
                ) -> PolicyHttpRequest: ...
                def resume(
                    self,
                    *,
                    name: str,
                    body: ResumeQueueRequest = ...,
                    **kwargs: typing.Any
                ) -> QueueHttpRequest: ...
                def create(
                    self, *, parent: str, body: Queue = ..., **kwargs: typing.Any
                ) -> QueueHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def tasks(self) -> TasksResource: ...
            def list(
                self,
                *,
                name: str,
                pageSize: int = ...,
                pageToken: str = ...,
                filter: str = ...,
                **kwargs: typing.Any
            ) -> ListLocationsResponseHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> LocationHttpRequest: ...
            def queues(self) -> QueuesResource: ...
        def locations(self) -> LocationsResource: ...
    def projects(self) -> ProjectsResource: ...

class ListLocationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListLocationsResponse: ...

class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Empty: ...

class LeaseTasksResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> LeaseTasksResponse: ...

class ListQueuesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListQueuesResponse: ...

class QueueHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Queue: ...

class LocationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Location: ...

class TestIamPermissionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> TestIamPermissionsResponse: ...

class TaskHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Task: ...

class PolicyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Policy: ...

class ListTasksResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListTasksResponse: ...
