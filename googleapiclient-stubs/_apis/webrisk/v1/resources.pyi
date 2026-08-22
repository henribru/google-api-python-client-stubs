import collections.abc
import typing

import httplib2

import googleapiclient.discovery
import googleapiclient.http

from .schemas import *

_list = list

@typing.type_check_only
class WebRiskResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class HashesResource(googleapiclient.discovery.Resource):
        def search(
            self,
            *,
            hashPrefix: str | None = ...,
            threatTypes: typing.Literal[
                "THREAT_TYPE_UNSPECIFIED",
                "MALWARE",
                "SOCIAL_ENGINEERING",
                "UNWANTED_SOFTWARE",
                "SOCIAL_ENGINEERING_EXTENDED_COVERAGE",
            ]
            | _list[
                typing.Literal[
                    "THREAT_TYPE_UNSPECIFIED",
                    "MALWARE",
                    "SOCIAL_ENGINEERING",
                    "UNWANTED_SOFTWARE",
                    "SOCIAL_ENGINEERING_EXTENDED_COVERAGE",
                ]
            ]
            | None = ...,
            **kwargs: typing.Any,
        ) -> GoogleCloudWebriskV1SearchHashesResponseHttpRequest: ...

    @typing.type_check_only
    class ProjectsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class OperationsResource(googleapiclient.discovery.Resource):
            def cancel(
                self,
                *,
                name: str,
                body: GoogleLongrunningCancelOperationRequest,
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
                filter: str | None = ...,
                pageSize: int | None = ...,
                pageToken: str | None = ...,
                returnPartialSuccess: bool | None = ...,
                **kwargs: typing.Any,
            ) -> GoogleLongrunningListOperationsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: GoogleLongrunningListOperationsResponseHttpRequest,
                previous_response: GoogleLongrunningListOperationsResponse,
            ) -> GoogleLongrunningListOperationsResponseHttpRequest | None: ...

        @typing.type_check_only
        class SubmissionsResource(googleapiclient.discovery.Resource):
            def create(
                self,
                *,
                parent: str,
                body: GoogleCloudWebriskV1Submission,
                **kwargs: typing.Any,
            ) -> GoogleCloudWebriskV1SubmissionHttpRequest: ...

        def operations(self) -> OperationsResource: ...
        def submissions(self) -> SubmissionsResource: ...

    @typing.type_check_only
    class ThreatListsResource(googleapiclient.discovery.Resource):
        def computeDiff(
            self,
            *,
            constraints_maxDatabaseEntries: int | None = ...,
            constraints_maxDiffEntries: int | None = ...,
            constraints_supportedCompressions: typing.Literal[
                "COMPRESSION_TYPE_UNSPECIFIED", "RAW", "RICE"
            ]
            | _list[typing.Literal["COMPRESSION_TYPE_UNSPECIFIED", "RAW", "RICE"]]
            | None = ...,
            threatType: typing.Literal[
                "THREAT_TYPE_UNSPECIFIED",
                "MALWARE",
                "SOCIAL_ENGINEERING",
                "UNWANTED_SOFTWARE",
                "SOCIAL_ENGINEERING_EXTENDED_COVERAGE",
            ]
            | None = ...,
            versionToken: str | None = ...,
            **kwargs: typing.Any,
        ) -> GoogleCloudWebriskV1ComputeThreatListDiffResponseHttpRequest: ...

    @typing.type_check_only
    class UrisResource(googleapiclient.discovery.Resource):
        def search(
            self,
            *,
            threatTypes: typing.Literal[
                "THREAT_TYPE_UNSPECIFIED",
                "MALWARE",
                "SOCIAL_ENGINEERING",
                "UNWANTED_SOFTWARE",
                "SOCIAL_ENGINEERING_EXTENDED_COVERAGE",
            ]
            | _list[
                typing.Literal[
                    "THREAT_TYPE_UNSPECIFIED",
                    "MALWARE",
                    "SOCIAL_ENGINEERING",
                    "UNWANTED_SOFTWARE",
                    "SOCIAL_ENGINEERING_EXTENDED_COVERAGE",
                ]
            ]
            | None = ...,
            uri: str | None = ...,
            **kwargs: typing.Any,
        ) -> GoogleCloudWebriskV1SearchUrisResponseHttpRequest: ...

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
    def hashes(self) -> HashesResource: ...
    def projects(self) -> ProjectsResource: ...
    def threatLists(self) -> ThreatListsResource: ...
    def uris(self) -> UrisResource: ...

@typing.type_check_only
class GoogleCloudWebriskV1ComputeThreatListDiffResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudWebriskV1ComputeThreatListDiffResponse: ...

@typing.type_check_only
class GoogleCloudWebriskV1SearchHashesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudWebriskV1SearchHashesResponse: ...

@typing.type_check_only
class GoogleCloudWebriskV1SearchUrisResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudWebriskV1SearchUrisResponse: ...

@typing.type_check_only
class GoogleCloudWebriskV1SubmissionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudWebriskV1Submission: ...

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
