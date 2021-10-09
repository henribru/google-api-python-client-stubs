import collections.abc
import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

_list = list

@typing.type_check_only
class RecaptchaEnterpriseResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class ProjectsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class AssessmentsResource(googleapiclient.discovery.Resource):
            def annotate(
                self,
                *,
                name: str,
                body: GoogleCloudRecaptchaenterpriseV1AnnotateAssessmentRequest = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudRecaptchaenterpriseV1AnnotateAssessmentResponseHttpRequest: ...
            def create(
                self,
                *,
                parent: str,
                body: GoogleCloudRecaptchaenterpriseV1Assessment = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudRecaptchaenterpriseV1AssessmentHttpRequest: ...
        @typing.type_check_only
        class KeysResource(googleapiclient.discovery.Resource):
            def create(
                self,
                *,
                parent: str,
                body: GoogleCloudRecaptchaenterpriseV1Key = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudRecaptchaenterpriseV1KeyHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleProtobufEmptyHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleCloudRecaptchaenterpriseV1KeyHttpRequest: ...
            def getMetrics(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleCloudRecaptchaenterpriseV1MetricsHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudRecaptchaenterpriseV1ListKeysResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: GoogleCloudRecaptchaenterpriseV1ListKeysResponseHttpRequest,
                previous_response: GoogleCloudRecaptchaenterpriseV1ListKeysResponse,
            ) -> GoogleCloudRecaptchaenterpriseV1ListKeysResponseHttpRequest | None: ...
            def migrate(
                self,
                *,
                name: str,
                body: GoogleCloudRecaptchaenterpriseV1MigrateKeyRequest = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudRecaptchaenterpriseV1KeyHttpRequest: ...
            def patch(
                self,
                *,
                name: str,
                body: GoogleCloudRecaptchaenterpriseV1Key = ...,
                updateMask: str = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudRecaptchaenterpriseV1KeyHttpRequest: ...
        def assessments(self) -> AssessmentsResource: ...
        def keys(self) -> KeysResource: ...
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
class GoogleCloudRecaptchaenterpriseV1AnnotateAssessmentResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudRecaptchaenterpriseV1AnnotateAssessmentResponse: ...

@typing.type_check_only
class GoogleCloudRecaptchaenterpriseV1AssessmentHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudRecaptchaenterpriseV1Assessment: ...

@typing.type_check_only
class GoogleCloudRecaptchaenterpriseV1KeyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudRecaptchaenterpriseV1Key: ...

@typing.type_check_only
class GoogleCloudRecaptchaenterpriseV1ListKeysResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudRecaptchaenterpriseV1ListKeysResponse: ...

@typing.type_check_only
class GoogleCloudRecaptchaenterpriseV1MetricsHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudRecaptchaenterpriseV1Metrics: ...

@typing.type_check_only
class GoogleProtobufEmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleProtobufEmpty: ...
