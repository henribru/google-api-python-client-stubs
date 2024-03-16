import collections.abc
import typing

import httplib2
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http

from .schemas import *

_list = list

@typing.type_check_only
class FirebaseAppDistributionResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class MediaResource(googleapiclient.discovery.Resource):
        def upload(
            self,
            *,
            app: str,
            body: GoogleFirebaseAppdistroV1UploadReleaseRequest = ...,
            **kwargs: typing.Any,
        ) -> GoogleLongrunningOperationHttpRequest: ...

    @typing.type_check_only
    class ProjectsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class AppsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class ReleasesResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class FeedbackReportsResource(googleapiclient.discovery.Resource):
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleProtobufEmptyHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleFirebaseAppdistroV1FeedbackReportHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
                    ) -> (
                        GoogleFirebaseAppdistroV1ListFeedbackReportsResponseHttpRequest
                    ): ...
                    def list_next(
                        self,
                        previous_request: GoogleFirebaseAppdistroV1ListFeedbackReportsResponseHttpRequest,
                        previous_response: GoogleFirebaseAppdistroV1ListFeedbackReportsResponse,
                    ) -> (
                        GoogleFirebaseAppdistroV1ListFeedbackReportsResponseHttpRequest
                        | None
                    ): ...

                @typing.type_check_only
                class OperationsResource(googleapiclient.discovery.Resource):
                    def cancel(
                        self,
                        *,
                        name: str,
                        body: GoogleLongrunningCancelOperationRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleProtobufEmptyHttpRequest: ...
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
                        **kwargs: typing.Any,
                    ) -> GoogleLongrunningListOperationsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: GoogleLongrunningListOperationsResponseHttpRequest,
                        previous_response: GoogleLongrunningListOperationsResponse,
                    ) -> GoogleLongrunningListOperationsResponseHttpRequest | None: ...
                    def wait(
                        self,
                        *,
                        name: str,
                        body: GoogleLongrunningWaitOperationRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleLongrunningOperationHttpRequest: ...

                def batchDelete(
                    self,
                    *,
                    parent: str,
                    body: GoogleFirebaseAppdistroV1BatchDeleteReleasesRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleProtobufEmptyHttpRequest: ...
                def distribute(
                    self,
                    *,
                    name: str,
                    body: GoogleFirebaseAppdistroV1DistributeReleaseRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleFirebaseAppdistroV1DistributeReleaseResponseHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleFirebaseAppdistroV1ReleaseHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleFirebaseAppdistroV1ListReleasesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleFirebaseAppdistroV1ListReleasesResponseHttpRequest,
                    previous_response: GoogleFirebaseAppdistroV1ListReleasesResponse,
                ) -> (
                    GoogleFirebaseAppdistroV1ListReleasesResponseHttpRequest | None
                ): ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleFirebaseAppdistroV1Release = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleFirebaseAppdistroV1ReleaseHttpRequest: ...
                def feedbackReports(self) -> FeedbackReportsResource: ...
                def operations(self) -> OperationsResource: ...

            def getAabInfo(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleFirebaseAppdistroV1AabInfoHttpRequest: ...
            def releases(self) -> ReleasesResource: ...

        @typing.type_check_only
        class GroupsResource(googleapiclient.discovery.Resource):
            def batchJoin(
                self,
                *,
                group: str,
                body: GoogleFirebaseAppdistroV1BatchJoinGroupRequest = ...,
                **kwargs: typing.Any,
            ) -> GoogleProtobufEmptyHttpRequest: ...
            def batchLeave(
                self,
                *,
                group: str,
                body: GoogleFirebaseAppdistroV1BatchLeaveGroupRequest = ...,
                **kwargs: typing.Any,
            ) -> GoogleProtobufEmptyHttpRequest: ...
            def create(
                self,
                *,
                parent: str,
                body: GoogleFirebaseAppdistroV1Group = ...,
                groupId: str = ...,
                **kwargs: typing.Any,
            ) -> GoogleFirebaseAppdistroV1GroupHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleProtobufEmptyHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleFirebaseAppdistroV1GroupHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any,
            ) -> GoogleFirebaseAppdistroV1ListGroupsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: GoogleFirebaseAppdistroV1ListGroupsResponseHttpRequest,
                previous_response: GoogleFirebaseAppdistroV1ListGroupsResponse,
            ) -> GoogleFirebaseAppdistroV1ListGroupsResponseHttpRequest | None: ...
            def patch(
                self,
                *,
                name: str,
                body: GoogleFirebaseAppdistroV1Group = ...,
                updateMask: str = ...,
                **kwargs: typing.Any,
            ) -> GoogleFirebaseAppdistroV1GroupHttpRequest: ...

        @typing.type_check_only
        class TestersResource(googleapiclient.discovery.Resource):
            def batchAdd(
                self,
                *,
                project: str,
                body: GoogleFirebaseAppdistroV1BatchAddTestersRequest = ...,
                **kwargs: typing.Any,
            ) -> GoogleFirebaseAppdistroV1BatchAddTestersResponseHttpRequest: ...
            def batchRemove(
                self,
                *,
                project: str,
                body: GoogleFirebaseAppdistroV1BatchRemoveTestersRequest = ...,
                **kwargs: typing.Any,
            ) -> GoogleFirebaseAppdistroV1BatchRemoveTestersResponseHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                filter: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any,
            ) -> GoogleFirebaseAppdistroV1ListTestersResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: GoogleFirebaseAppdistroV1ListTestersResponseHttpRequest,
                previous_response: GoogleFirebaseAppdistroV1ListTestersResponse,
            ) -> GoogleFirebaseAppdistroV1ListTestersResponseHttpRequest | None: ...
            def patch(
                self,
                *,
                name: str,
                body: GoogleFirebaseAppdistroV1Tester = ...,
                updateMask: str = ...,
                **kwargs: typing.Any,
            ) -> GoogleFirebaseAppdistroV1TesterHttpRequest: ...

        def apps(self) -> AppsResource: ...
        def groups(self) -> GroupsResource: ...
        def testers(self) -> TestersResource: ...

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
    def media(self) -> MediaResource: ...
    def projects(self) -> ProjectsResource: ...

@typing.type_check_only
class GoogleFirebaseAppdistroV1AabInfoHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleFirebaseAppdistroV1AabInfo: ...

@typing.type_check_only
class GoogleFirebaseAppdistroV1BatchAddTestersResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleFirebaseAppdistroV1BatchAddTestersResponse: ...

@typing.type_check_only
class GoogleFirebaseAppdistroV1BatchRemoveTestersResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleFirebaseAppdistroV1BatchRemoveTestersResponse: ...

@typing.type_check_only
class GoogleFirebaseAppdistroV1DistributeReleaseResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleFirebaseAppdistroV1DistributeReleaseResponse: ...

@typing.type_check_only
class GoogleFirebaseAppdistroV1FeedbackReportHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleFirebaseAppdistroV1FeedbackReport: ...

@typing.type_check_only
class GoogleFirebaseAppdistroV1GroupHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleFirebaseAppdistroV1Group: ...

@typing.type_check_only
class GoogleFirebaseAppdistroV1ListFeedbackReportsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleFirebaseAppdistroV1ListFeedbackReportsResponse: ...

@typing.type_check_only
class GoogleFirebaseAppdistroV1ListGroupsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleFirebaseAppdistroV1ListGroupsResponse: ...

@typing.type_check_only
class GoogleFirebaseAppdistroV1ListReleasesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleFirebaseAppdistroV1ListReleasesResponse: ...

@typing.type_check_only
class GoogleFirebaseAppdistroV1ListTestersResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleFirebaseAppdistroV1ListTestersResponse: ...

@typing.type_check_only
class GoogleFirebaseAppdistroV1ReleaseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleFirebaseAppdistroV1Release: ...

@typing.type_check_only
class GoogleFirebaseAppdistroV1TesterHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleFirebaseAppdistroV1Tester: ...

@typing.type_check_only
class GoogleLongrunningListOperationsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleLongrunningListOperationsResponse: ...

@typing.type_check_only
class GoogleLongrunningOperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleLongrunningOperation: ...

@typing.type_check_only
class GoogleProtobufEmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleProtobufEmpty: ...
