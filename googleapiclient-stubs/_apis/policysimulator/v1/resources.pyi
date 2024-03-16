import collections.abc
import typing

import httplib2
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http

from .schemas import *

_list = list

@typing.type_check_only
class PolicySimulatorResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class FoldersResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class LocationsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class OrgPolicyViolationsPreviewsResource(
                googleapiclient.discovery.Resource
            ):
                @typing.type_check_only
                class OperationsResource(googleapiclient.discovery.Resource):
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleLongrunningOperationHttpRequest: ...

                def operations(self) -> OperationsResource: ...

            @typing.type_check_only
            class ReplaysResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class OperationsResource(googleapiclient.discovery.Resource):
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
                class ResultsResource(googleapiclient.discovery.Resource):
                    def list(
                        self,
                        *,
                        parent: str,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any
                    ) -> (
                        GoogleCloudPolicysimulatorV1ListReplayResultsResponseHttpRequest
                    ): ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudPolicysimulatorV1ListReplayResultsResponseHttpRequest,
                        previous_response: GoogleCloudPolicysimulatorV1ListReplayResultsResponse,
                    ) -> (
                        GoogleCloudPolicysimulatorV1ListReplayResultsResponseHttpRequest
                        | None
                    ): ...

                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudPolicysimulatorV1Replay = ...,
                    **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudPolicysimulatorV1ReplayHttpRequest: ...
                def operations(self) -> OperationsResource: ...
                def results(self) -> ResultsResource: ...

            def orgPolicyViolationsPreviews(
                self,
            ) -> OrgPolicyViolationsPreviewsResource: ...
            def replays(self) -> ReplaysResource: ...

        def locations(self) -> LocationsResource: ...

    @typing.type_check_only
    class OperationsResource(googleapiclient.discovery.Resource):
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
    class OrganizationsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class LocationsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class OrgPolicyViolationsPreviewsResource(
                googleapiclient.discovery.Resource
            ):
                @typing.type_check_only
                class OperationsResource(googleapiclient.discovery.Resource):
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleLongrunningOperationHttpRequest: ...

                @typing.type_check_only
                class OrgPolicyViolationsResource(googleapiclient.discovery.Resource):
                    def list(
                        self,
                        *,
                        parent: str,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudPolicysimulatorV1ListOrgPolicyViolationsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudPolicysimulatorV1ListOrgPolicyViolationsResponseHttpRequest,
                        previous_response: GoogleCloudPolicysimulatorV1ListOrgPolicyViolationsResponse,
                    ) -> (
                        GoogleCloudPolicysimulatorV1ListOrgPolicyViolationsResponseHttpRequest
                        | None
                    ): ...

                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudPolicysimulatorV1OrgPolicyViolationsPreview = ...,
                    orgPolicyViolationsPreviewId: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> (
                    GoogleCloudPolicysimulatorV1OrgPolicyViolationsPreviewHttpRequest
                ): ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudPolicysimulatorV1ListOrgPolicyViolationsPreviewsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudPolicysimulatorV1ListOrgPolicyViolationsPreviewsResponseHttpRequest,
                    previous_response: GoogleCloudPolicysimulatorV1ListOrgPolicyViolationsPreviewsResponse,
                ) -> (
                    GoogleCloudPolicysimulatorV1ListOrgPolicyViolationsPreviewsResponseHttpRequest
                    | None
                ): ...
                def operations(self) -> OperationsResource: ...
                def orgPolicyViolations(self) -> OrgPolicyViolationsResource: ...

            @typing.type_check_only
            class ReplaysResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class OperationsResource(googleapiclient.discovery.Resource):
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
                class ResultsResource(googleapiclient.discovery.Resource):
                    def list(
                        self,
                        *,
                        parent: str,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any
                    ) -> (
                        GoogleCloudPolicysimulatorV1ListReplayResultsResponseHttpRequest
                    ): ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudPolicysimulatorV1ListReplayResultsResponseHttpRequest,
                        previous_response: GoogleCloudPolicysimulatorV1ListReplayResultsResponse,
                    ) -> (
                        GoogleCloudPolicysimulatorV1ListReplayResultsResponseHttpRequest
                        | None
                    ): ...

                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudPolicysimulatorV1Replay = ...,
                    **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudPolicysimulatorV1ReplayHttpRequest: ...
                def operations(self) -> OperationsResource: ...
                def results(self) -> ResultsResource: ...

            def orgPolicyViolationsPreviews(
                self,
            ) -> OrgPolicyViolationsPreviewsResource: ...
            def replays(self) -> ReplaysResource: ...

        def locations(self) -> LocationsResource: ...

    @typing.type_check_only
    class ProjectsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class LocationsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class OrgPolicyViolationsPreviewsResource(
                googleapiclient.discovery.Resource
            ):
                @typing.type_check_only
                class OperationsResource(googleapiclient.discovery.Resource):
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleLongrunningOperationHttpRequest: ...

                def operations(self) -> OperationsResource: ...

            @typing.type_check_only
            class ReplaysResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class OperationsResource(googleapiclient.discovery.Resource):
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
                class ResultsResource(googleapiclient.discovery.Resource):
                    def list(
                        self,
                        *,
                        parent: str,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any
                    ) -> (
                        GoogleCloudPolicysimulatorV1ListReplayResultsResponseHttpRequest
                    ): ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudPolicysimulatorV1ListReplayResultsResponseHttpRequest,
                        previous_response: GoogleCloudPolicysimulatorV1ListReplayResultsResponse,
                    ) -> (
                        GoogleCloudPolicysimulatorV1ListReplayResultsResponseHttpRequest
                        | None
                    ): ...

                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudPolicysimulatorV1Replay = ...,
                    **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudPolicysimulatorV1ReplayHttpRequest: ...
                def operations(self) -> OperationsResource: ...
                def results(self) -> ResultsResource: ...

            def orgPolicyViolationsPreviews(
                self,
            ) -> OrgPolicyViolationsPreviewsResource: ...
            def replays(self) -> ReplaysResource: ...

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
    def folders(self) -> FoldersResource: ...
    def operations(self) -> OperationsResource: ...
    def organizations(self) -> OrganizationsResource: ...
    def projects(self) -> ProjectsResource: ...

@typing.type_check_only
class GoogleCloudPolicysimulatorV1ListOrgPolicyViolationsPreviewsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudPolicysimulatorV1ListOrgPolicyViolationsPreviewsResponse: ...

@typing.type_check_only
class GoogleCloudPolicysimulatorV1ListOrgPolicyViolationsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudPolicysimulatorV1ListOrgPolicyViolationsResponse: ...

@typing.type_check_only
class GoogleCloudPolicysimulatorV1ListReplayResultsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudPolicysimulatorV1ListReplayResultsResponse: ...

@typing.type_check_only
class GoogleCloudPolicysimulatorV1OrgPolicyViolationsPreviewHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudPolicysimulatorV1OrgPolicyViolationsPreview: ...

@typing.type_check_only
class GoogleCloudPolicysimulatorV1ReplayHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudPolicysimulatorV1Replay: ...

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
