import collections.abc
import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

_list = list

@typing.type_check_only
class CloudRunResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class ProjectsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class LocationsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class JobsResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class ExecutionsResource(googleapiclient.discovery.Resource):
                    @typing.type_check_only
                    class TasksResource(googleapiclient.discovery.Resource):
                        def get(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> GoogleCloudRunV2TaskHttpRequest: ...
                        def list(
                            self,
                            *,
                            parent: str,
                            pageSize: int = ...,
                            pageToken: str = ...,
                            showDeleted: bool = ...,
                            **kwargs: typing.Any
                        ) -> GoogleCloudRunV2ListTasksResponseHttpRequest: ...
                        def list_next(
                            self,
                            previous_request: GoogleCloudRunV2ListTasksResponseHttpRequest,
                            previous_response: GoogleCloudRunV2ListTasksResponse,
                        ) -> GoogleCloudRunV2ListTasksResponseHttpRequest | None: ...

                    def delete(
                        self,
                        *,
                        name: str,
                        etag: str = ...,
                        validateOnly: bool = ...,
                        **kwargs: typing.Any
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleCloudRunV2ExecutionHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        showDeleted: bool = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudRunV2ListExecutionsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudRunV2ListExecutionsResponseHttpRequest,
                        previous_response: GoogleCloudRunV2ListExecutionsResponse,
                    ) -> GoogleCloudRunV2ListExecutionsResponseHttpRequest | None: ...
                    def tasks(self) -> TasksResource: ...

                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudRunV2Job = ...,
                    jobId: str = ...,
                    validateOnly: bool = ...,
                    **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def delete(
                    self,
                    *,
                    name: str,
                    etag: str = ...,
                    force: bool = ...,
                    validateOnly: bool = ...,
                    **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudRunV2JobHttpRequest: ...
                def getIamPolicy(
                    self,
                    *,
                    resource: str,
                    options_requestedPolicyVersion: int = ...,
                    **kwargs: typing.Any
                ) -> GoogleIamV1PolicyHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    showDeleted: bool = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudRunV2ListJobsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudRunV2ListJobsResponseHttpRequest,
                    previous_response: GoogleCloudRunV2ListJobsResponse,
                ) -> GoogleCloudRunV2ListJobsResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudRunV2Job = ...,
                    allowMissing: bool = ...,
                    validateOnly: bool = ...,
                    **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def run(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudRunV2RunJobRequest = ...,
                    **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def setIamPolicy(
                    self,
                    *,
                    resource: str,
                    body: GoogleIamV1SetIamPolicyRequest = ...,
                    **kwargs: typing.Any
                ) -> GoogleIamV1PolicyHttpRequest: ...
                def testIamPermissions(
                    self,
                    *,
                    resource: str,
                    body: GoogleIamV1TestIamPermissionsRequest = ...,
                    **kwargs: typing.Any
                ) -> GoogleIamV1TestIamPermissionsResponseHttpRequest: ...
                def executions(self) -> ExecutionsResource: ...

            @typing.type_check_only
            class OperationsResource(googleapiclient.discovery.Resource):
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleProtobufEmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def list(
                    self,
                    *,
                    name: str,
                    filter: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleLongrunningListOperationsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleLongrunningListOperationsResponseHttpRequest,
                    previous_response: GoogleLongrunningListOperationsResponse,
                ) -> GoogleLongrunningListOperationsResponseHttpRequest | None: ...

            @typing.type_check_only
            class ServicesResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class RevisionsResource(googleapiclient.discovery.Resource):
                    def delete(
                        self,
                        *,
                        name: str,
                        etag: str = ...,
                        validateOnly: bool = ...,
                        **kwargs: typing.Any
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleCloudRunV2RevisionHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        showDeleted: bool = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudRunV2ListRevisionsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudRunV2ListRevisionsResponseHttpRequest,
                        previous_response: GoogleCloudRunV2ListRevisionsResponse,
                    ) -> GoogleCloudRunV2ListRevisionsResponseHttpRequest | None: ...

                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudRunV2Service = ...,
                    serviceId: str = ...,
                    validateOnly: bool = ...,
                    **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def delete(
                    self,
                    *,
                    name: str,
                    etag: str = ...,
                    validateOnly: bool = ...,
                    **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudRunV2ServiceHttpRequest: ...
                def getIamPolicy(
                    self,
                    *,
                    resource: str,
                    options_requestedPolicyVersion: int = ...,
                    **kwargs: typing.Any
                ) -> GoogleIamV1PolicyHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    showDeleted: bool = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudRunV2ListServicesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudRunV2ListServicesResponseHttpRequest,
                    previous_response: GoogleCloudRunV2ListServicesResponse,
                ) -> GoogleCloudRunV2ListServicesResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudRunV2Service = ...,
                    allowMissing: bool = ...,
                    validateOnly: bool = ...,
                    **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def setIamPolicy(
                    self,
                    *,
                    resource: str,
                    body: GoogleIamV1SetIamPolicyRequest = ...,
                    **kwargs: typing.Any
                ) -> GoogleIamV1PolicyHttpRequest: ...
                def testIamPermissions(
                    self,
                    *,
                    resource: str,
                    body: GoogleIamV1TestIamPermissionsRequest = ...,
                    **kwargs: typing.Any
                ) -> GoogleIamV1TestIamPermissionsResponseHttpRequest: ...
                def revisions(self) -> RevisionsResource: ...

            def jobs(self) -> JobsResource: ...
            def operations(self) -> OperationsResource: ...
            def services(self) -> ServicesResource: ...

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
class GoogleCloudRunV2ExecutionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudRunV2Execution: ...

@typing.type_check_only
class GoogleCloudRunV2JobHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudRunV2Job: ...

@typing.type_check_only
class GoogleCloudRunV2ListExecutionsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudRunV2ListExecutionsResponse: ...

@typing.type_check_only
class GoogleCloudRunV2ListJobsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudRunV2ListJobsResponse: ...

@typing.type_check_only
class GoogleCloudRunV2ListRevisionsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudRunV2ListRevisionsResponse: ...

@typing.type_check_only
class GoogleCloudRunV2ListServicesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudRunV2ListServicesResponse: ...

@typing.type_check_only
class GoogleCloudRunV2ListTasksResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudRunV2ListTasksResponse: ...

@typing.type_check_only
class GoogleCloudRunV2RevisionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudRunV2Revision: ...

@typing.type_check_only
class GoogleCloudRunV2ServiceHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudRunV2Service: ...

@typing.type_check_only
class GoogleCloudRunV2TaskHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudRunV2Task: ...

@typing.type_check_only
class GoogleIamV1PolicyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleIamV1Policy: ...

@typing.type_check_only
class GoogleIamV1TestIamPermissionsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleIamV1TestIamPermissionsResponse: ...

@typing.type_check_only
class GoogleLongrunningListOperationsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleLongrunningListOperationsResponse: ...

@typing.type_check_only
class GoogleLongrunningOperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleLongrunningOperation: ...

@typing.type_check_only
class GoogleProtobufEmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleProtobufEmpty: ...
