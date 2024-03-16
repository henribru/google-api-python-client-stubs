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
                        **kwargs: typing.Any,
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
                        **kwargs: typing.Any,
                    ) -> GoogleCloudPolicysimulatorV1betaListReplayResultsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudPolicysimulatorV1betaListReplayResultsResponseHttpRequest,
                        previous_response: GoogleCloudPolicysimulatorV1betaListReplayResultsResponse,
                    ) -> (
                        GoogleCloudPolicysimulatorV1betaListReplayResultsResponseHttpRequest
                        | None
                    ): ...

                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudPolicysimulatorV1betaReplay = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudPolicysimulatorV1betaReplayHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudPolicysimulatorV1betaListReplaysResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudPolicysimulatorV1betaListReplaysResponseHttpRequest,
                    previous_response: GoogleCloudPolicysimulatorV1betaListReplaysResponse,
                ) -> (
                    GoogleCloudPolicysimulatorV1betaListReplaysResponseHttpRequest
                    | None
                ): ...
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
            **kwargs: typing.Any,
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
                        **kwargs: typing.Any,
                    ) -> GoogleCloudPolicysimulatorV1betaListOrgPolicyViolationsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudPolicysimulatorV1betaListOrgPolicyViolationsResponseHttpRequest,
                        previous_response: GoogleCloudPolicysimulatorV1betaListOrgPolicyViolationsResponse,
                    ) -> (
                        GoogleCloudPolicysimulatorV1betaListOrgPolicyViolationsResponseHttpRequest
                        | None
                    ): ...

                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudPolicysimulatorV1betaOrgPolicyViolationsPreview = ...,
                    orgPolicyViolationsPreviewId: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def generate(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudPolicysimulatorV1betaOrgPolicyViolationsPreview = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudPolicysimulatorV1betaOrgPolicyViolationsPreviewHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudPolicysimulatorV1betaListOrgPolicyViolationsPreviewsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudPolicysimulatorV1betaListOrgPolicyViolationsPreviewsResponseHttpRequest,
                    previous_response: GoogleCloudPolicysimulatorV1betaListOrgPolicyViolationsPreviewsResponse,
                ) -> (
                    GoogleCloudPolicysimulatorV1betaListOrgPolicyViolationsPreviewsResponseHttpRequest
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
                        **kwargs: typing.Any,
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
                        **kwargs: typing.Any,
                    ) -> GoogleCloudPolicysimulatorV1betaListReplayResultsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudPolicysimulatorV1betaListReplayResultsResponseHttpRequest,
                        previous_response: GoogleCloudPolicysimulatorV1betaListReplayResultsResponse,
                    ) -> (
                        GoogleCloudPolicysimulatorV1betaListReplayResultsResponseHttpRequest
                        | None
                    ): ...

                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudPolicysimulatorV1betaReplay = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudPolicysimulatorV1betaReplayHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudPolicysimulatorV1betaListReplaysResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudPolicysimulatorV1betaListReplaysResponseHttpRequest,
                    previous_response: GoogleCloudPolicysimulatorV1betaListReplaysResponse,
                ) -> (
                    GoogleCloudPolicysimulatorV1betaListReplaysResponseHttpRequest
                    | None
                ): ...
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
                        **kwargs: typing.Any,
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
                        **kwargs: typing.Any,
                    ) -> GoogleCloudPolicysimulatorV1betaListReplayResultsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudPolicysimulatorV1betaListReplayResultsResponseHttpRequest,
                        previous_response: GoogleCloudPolicysimulatorV1betaListReplayResultsResponse,
                    ) -> (
                        GoogleCloudPolicysimulatorV1betaListReplayResultsResponseHttpRequest
                        | None
                    ): ...

                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudPolicysimulatorV1betaReplay = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudPolicysimulatorV1betaReplayHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudPolicysimulatorV1betaListReplaysResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudPolicysimulatorV1betaListReplaysResponseHttpRequest,
                    previous_response: GoogleCloudPolicysimulatorV1betaListReplaysResponse,
                ) -> (
                    GoogleCloudPolicysimulatorV1betaListReplaysResponseHttpRequest
                    | None
                ): ...
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
class GoogleCloudPolicysimulatorV1betaListOrgPolicyViolationsPreviewsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudPolicysimulatorV1betaListOrgPolicyViolationsPreviewsResponse: ...

@typing.type_check_only
class GoogleCloudPolicysimulatorV1betaListOrgPolicyViolationsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudPolicysimulatorV1betaListOrgPolicyViolationsResponse: ...

@typing.type_check_only
class GoogleCloudPolicysimulatorV1betaListReplayResultsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudPolicysimulatorV1betaListReplayResultsResponse: ...

@typing.type_check_only
class GoogleCloudPolicysimulatorV1betaListReplaysResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudPolicysimulatorV1betaListReplaysResponse: ...

@typing.type_check_only
class GoogleCloudPolicysimulatorV1betaOrgPolicyViolationsPreviewHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudPolicysimulatorV1betaOrgPolicyViolationsPreview: ...

@typing.type_check_only
class GoogleCloudPolicysimulatorV1betaReplayHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudPolicysimulatorV1betaReplay: ...

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
