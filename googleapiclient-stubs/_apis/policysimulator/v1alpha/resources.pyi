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
                    ) -> GoogleCloudPolicysimulatorV1alphaListReplayResultsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudPolicysimulatorV1alphaListReplayResultsResponseHttpRequest,
                        previous_response: GoogleCloudPolicysimulatorV1alphaListReplayResultsResponse,
                    ) -> (
                        GoogleCloudPolicysimulatorV1alphaListReplayResultsResponseHttpRequest
                        | None
                    ): ...

                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudPolicysimulatorV1alphaReplay = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudPolicysimulatorV1alphaReplayHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> (
                    GoogleCloudPolicysimulatorV1alphaListReplaysResponseHttpRequest
                ): ...
                def list_next(
                    self,
                    previous_request: GoogleCloudPolicysimulatorV1alphaListReplaysResponseHttpRequest,
                    previous_response: GoogleCloudPolicysimulatorV1alphaListReplaysResponse,
                ) -> (
                    GoogleCloudPolicysimulatorV1alphaListReplaysResponseHttpRequest
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
                    ) -> GoogleCloudPolicysimulatorV1alphaListOrgPolicyViolationsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudPolicysimulatorV1alphaListOrgPolicyViolationsResponseHttpRequest,
                        previous_response: GoogleCloudPolicysimulatorV1alphaListOrgPolicyViolationsResponse,
                    ) -> (
                        GoogleCloudPolicysimulatorV1alphaListOrgPolicyViolationsResponseHttpRequest
                        | None
                    ): ...

                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudPolicysimulatorV1alphaOrgPolicyViolationsPreview = ...,
                    orgPolicyViolationsPreviewId: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def generate(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudPolicysimulatorV1alphaOrgPolicyViolationsPreview = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudPolicysimulatorV1alphaOrgPolicyViolationsPreviewHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudPolicysimulatorV1alphaListOrgPolicyViolationsPreviewsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudPolicysimulatorV1alphaListOrgPolicyViolationsPreviewsResponseHttpRequest,
                    previous_response: GoogleCloudPolicysimulatorV1alphaListOrgPolicyViolationsPreviewsResponse,
                ) -> (
                    GoogleCloudPolicysimulatorV1alphaListOrgPolicyViolationsPreviewsResponseHttpRequest
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
                    ) -> GoogleCloudPolicysimulatorV1alphaListReplayResultsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudPolicysimulatorV1alphaListReplayResultsResponseHttpRequest,
                        previous_response: GoogleCloudPolicysimulatorV1alphaListReplayResultsResponse,
                    ) -> (
                        GoogleCloudPolicysimulatorV1alphaListReplayResultsResponseHttpRequest
                        | None
                    ): ...

                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudPolicysimulatorV1alphaReplay = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudPolicysimulatorV1alphaReplayHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> (
                    GoogleCloudPolicysimulatorV1alphaListReplaysResponseHttpRequest
                ): ...
                def list_next(
                    self,
                    previous_request: GoogleCloudPolicysimulatorV1alphaListReplaysResponseHttpRequest,
                    previous_response: GoogleCloudPolicysimulatorV1alphaListReplaysResponse,
                ) -> (
                    GoogleCloudPolicysimulatorV1alphaListReplaysResponseHttpRequest
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
                    ) -> GoogleCloudPolicysimulatorV1alphaListReplayResultsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudPolicysimulatorV1alphaListReplayResultsResponseHttpRequest,
                        previous_response: GoogleCloudPolicysimulatorV1alphaListReplayResultsResponse,
                    ) -> (
                        GoogleCloudPolicysimulatorV1alphaListReplayResultsResponseHttpRequest
                        | None
                    ): ...

                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudPolicysimulatorV1alphaReplay = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudPolicysimulatorV1alphaReplayHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> (
                    GoogleCloudPolicysimulatorV1alphaListReplaysResponseHttpRequest
                ): ...
                def list_next(
                    self,
                    previous_request: GoogleCloudPolicysimulatorV1alphaListReplaysResponseHttpRequest,
                    previous_response: GoogleCloudPolicysimulatorV1alphaListReplaysResponse,
                ) -> (
                    GoogleCloudPolicysimulatorV1alphaListReplaysResponseHttpRequest
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
class GoogleCloudPolicysimulatorV1alphaListOrgPolicyViolationsPreviewsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudPolicysimulatorV1alphaListOrgPolicyViolationsPreviewsResponse: ...

@typing.type_check_only
class GoogleCloudPolicysimulatorV1alphaListOrgPolicyViolationsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudPolicysimulatorV1alphaListOrgPolicyViolationsResponse: ...

@typing.type_check_only
class GoogleCloudPolicysimulatorV1alphaListReplayResultsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudPolicysimulatorV1alphaListReplayResultsResponse: ...

@typing.type_check_only
class GoogleCloudPolicysimulatorV1alphaListReplaysResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudPolicysimulatorV1alphaListReplaysResponse: ...

@typing.type_check_only
class GoogleCloudPolicysimulatorV1alphaOrgPolicyViolationsPreviewHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudPolicysimulatorV1alphaOrgPolicyViolationsPreview: ...

@typing.type_check_only
class GoogleCloudPolicysimulatorV1alphaReplayHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudPolicysimulatorV1alphaReplay: ...

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
