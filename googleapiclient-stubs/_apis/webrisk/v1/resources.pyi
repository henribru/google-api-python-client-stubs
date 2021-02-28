import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *
@typing.type_check_only
class WebRiskResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class HashesResource(googleapiclient.discovery.Resource):
        def search(
            self,
            *,
            hashPrefix: str = ...,
            threatTypes: typing.Union[
                typing_extensions.Literal[
                    "THREAT_TYPE_UNSPECIFIED",
                    "MALWARE",
                    "SOCIAL_ENGINEERING",
                    "UNWANTED_SOFTWARE",
                ],
                typing.List[
                    typing_extensions.Literal[
                        "THREAT_TYPE_UNSPECIFIED",
                        "MALWARE",
                        "SOCIAL_ENGINEERING",
                        "UNWANTED_SOFTWARE",
                    ]
                ],
            ] = ...,
            **kwargs: typing.Any
        ) -> GoogleCloudWebriskV1SearchHashesResponseHttpRequest: ...
    @typing.type_check_only
    class OperationsResource(googleapiclient.discovery.Resource):
        def cancel(
            self,
            *,
            name: str,
            body: GoogleLongrunningCancelOperationRequest = ...,
            **kwargs: typing.Any
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
            **kwargs: typing.Any
        ) -> GoogleLongrunningListOperationsResponseHttpRequest: ...
    @typing.type_check_only
    class ProjectsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class SubmissionsResource(googleapiclient.discovery.Resource):
            def create(
                self,
                *,
                parent: str,
                body: GoogleCloudWebriskV1Submission = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudWebriskV1SubmissionHttpRequest: ...
        @typing.type_check_only
        class UrisResource(googleapiclient.discovery.Resource):
            def submit(
                self,
                *,
                parent: str,
                body: GoogleCloudWebriskV1SubmitUriRequest = ...,
                **kwargs: typing.Any
            ) -> GoogleLongrunningOperationHttpRequest: ...
        def submissions(self) -> SubmissionsResource: ...
        def uris(self) -> UrisResource: ...
    @typing.type_check_only
    class ThreatListsResource(googleapiclient.discovery.Resource):
        def computeDiff(
            self,
            *,
            constraints_maxDatabaseEntries: int = ...,
            constraints_maxDiffEntries: int = ...,
            constraints_supportedCompressions: typing.Union[
                typing_extensions.Literal[
                    "COMPRESSION_TYPE_UNSPECIFIED", "RAW", "RICE"
                ],
                typing.List[
                    typing_extensions.Literal[
                        "COMPRESSION_TYPE_UNSPECIFIED", "RAW", "RICE"
                    ]
                ],
            ] = ...,
            threatType: typing_extensions.Literal[
                "THREAT_TYPE_UNSPECIFIED",
                "MALWARE",
                "SOCIAL_ENGINEERING",
                "UNWANTED_SOFTWARE",
            ] = ...,
            versionToken: str = ...,
            **kwargs: typing.Any
        ) -> GoogleCloudWebriskV1ComputeThreatListDiffResponseHttpRequest: ...
    @typing.type_check_only
    class UrisResource(googleapiclient.discovery.Resource):
        def search(
            self,
            *,
            threatTypes: typing.Union[
                typing_extensions.Literal[
                    "THREAT_TYPE_UNSPECIFIED",
                    "MALWARE",
                    "SOCIAL_ENGINEERING",
                    "UNWANTED_SOFTWARE",
                ],
                typing.List[
                    typing_extensions.Literal[
                        "THREAT_TYPE_UNSPECIFIED",
                        "MALWARE",
                        "SOCIAL_ENGINEERING",
                        "UNWANTED_SOFTWARE",
                    ]
                ],
            ] = ...,
            uri: str = ...,
            **kwargs: typing.Any
        ) -> GoogleCloudWebriskV1SearchUrisResponseHttpRequest: ...
    def hashes(self) -> HashesResource: ...
    def operations(self) -> OperationsResource: ...
    def projects(self) -> ProjectsResource: ...
    def threatLists(self) -> ThreatListsResource: ...
    def uris(self) -> UrisResource: ...

@typing.type_check_only
class GoogleCloudWebriskV1ComputeThreatListDiffResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleCloudWebriskV1ComputeThreatListDiffResponse: ...

@typing.type_check_only
class GoogleCloudWebriskV1SearchHashesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleCloudWebriskV1SearchHashesResponse: ...

@typing.type_check_only
class GoogleCloudWebriskV1SearchUrisResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleCloudWebriskV1SearchUrisResponse: ...

@typing.type_check_only
class GoogleCloudWebriskV1SubmissionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleCloudWebriskV1Submission: ...

@typing.type_check_only
class GoogleLongrunningListOperationsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleLongrunningListOperationsResponse: ...

@typing.type_check_only
class GoogleLongrunningOperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleLongrunningOperation: ...

@typing.type_check_only
class GoogleProtobufEmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleProtobufEmpty: ...
