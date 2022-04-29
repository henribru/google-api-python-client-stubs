import collections.abc
import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

_list = list

@typing.type_check_only
class PolicySimulatorResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class FoldersResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class LocationsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class ReplaysResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class ResultsResource(googleapiclient.discovery.Resource):
                    def list(
                        self,
                        *,
                        parent: str,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudPolicysimulatorV1beta1ListReplayResultsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudPolicysimulatorV1beta1ListReplayResultsResponseHttpRequest,
                        previous_response: GoogleCloudPolicysimulatorV1beta1ListReplayResultsResponse,
                    ) -> GoogleCloudPolicysimulatorV1beta1ListReplayResultsResponseHttpRequest | None: ...

                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudPolicysimulatorV1beta1Replay = ...,
                    **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudPolicysimulatorV1beta1ReplayHttpRequest: ...
                def results(self) -> ResultsResource: ...

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
            filter: str = ...,
            name: str = ...,
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
            class ReplaysResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class ResultsResource(googleapiclient.discovery.Resource):
                    def list(
                        self,
                        *,
                        parent: str,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudPolicysimulatorV1beta1ListReplayResultsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudPolicysimulatorV1beta1ListReplayResultsResponseHttpRequest,
                        previous_response: GoogleCloudPolicysimulatorV1beta1ListReplayResultsResponse,
                    ) -> GoogleCloudPolicysimulatorV1beta1ListReplayResultsResponseHttpRequest | None: ...

                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudPolicysimulatorV1beta1Replay = ...,
                    **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudPolicysimulatorV1beta1ReplayHttpRequest: ...
                def results(self) -> ResultsResource: ...

            def replays(self) -> ReplaysResource: ...

        def locations(self) -> LocationsResource: ...

    @typing.type_check_only
    class ProjectsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class LocationsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class ReplaysResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class ResultsResource(googleapiclient.discovery.Resource):
                    def list(
                        self,
                        *,
                        parent: str,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudPolicysimulatorV1beta1ListReplayResultsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudPolicysimulatorV1beta1ListReplayResultsResponseHttpRequest,
                        previous_response: GoogleCloudPolicysimulatorV1beta1ListReplayResultsResponse,
                    ) -> GoogleCloudPolicysimulatorV1beta1ListReplayResultsResponseHttpRequest | None: ...

                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudPolicysimulatorV1beta1Replay = ...,
                    **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudPolicysimulatorV1beta1ReplayHttpRequest: ...
                def results(self) -> ResultsResource: ...

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
        | None = ...,
    ) -> googleapiclient.http.BatchHttpRequest: ...
    def folders(self) -> FoldersResource: ...
    def operations(self) -> OperationsResource: ...
    def organizations(self) -> OrganizationsResource: ...
    def projects(self) -> ProjectsResource: ...

@typing.type_check_only
class GoogleCloudPolicysimulatorV1beta1ListReplayResultsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudPolicysimulatorV1beta1ListReplayResultsResponse: ...

@typing.type_check_only
class GoogleCloudPolicysimulatorV1beta1ReplayHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudPolicysimulatorV1beta1Replay: ...

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
