import collections.abc
import typing

import httplib2
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http

from .schemas import *

_list = list

@typing.type_check_only
class ChromewebstoreResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class MediaResource(googleapiclient.discovery.Resource):
        def upload(
            self,
            *,
            name: str,
            body: UploadItemPackageRequest = ...,
            **kwargs: typing.Any,
        ) -> UploadItemPackageResponseHttpRequest: ...

    @typing.type_check_only
    class PublishersResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class ItemsResource(googleapiclient.discovery.Resource):
            def cancelSubmission(
                self,
                *,
                name: str,
                body: CancelSubmissionRequest = ...,
                **kwargs: typing.Any,
            ) -> CancelSubmissionResponseHttpRequest: ...
            def fetchStatus(
                self, *, name: str, **kwargs: typing.Any
            ) -> FetchItemStatusResponseHttpRequest: ...
            def publish(
                self, *, name: str, body: PublishItemRequest = ..., **kwargs: typing.Any
            ) -> PublishItemResponseHttpRequest: ...
            def setPublishedDeployPercentage(
                self,
                *,
                name: str,
                body: SetPublishedDeployPercentageRequest = ...,
                **kwargs: typing.Any,
            ) -> SetPublishedDeployPercentageResponseHttpRequest: ...

        def items(self) -> ItemsResource: ...

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
    def publishers(self) -> PublishersResource: ...

@typing.type_check_only
class CancelSubmissionResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> CancelSubmissionResponse: ...

@typing.type_check_only
class FetchItemStatusResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> FetchItemStatusResponse: ...

@typing.type_check_only
class PublishItemResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> PublishItemResponse: ...

@typing.type_check_only
class SetPublishedDeployPercentageResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> SetPublishedDeployPercentageResponse: ...

@typing.type_check_only
class UploadItemPackageResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> UploadItemPackageResponse: ...
