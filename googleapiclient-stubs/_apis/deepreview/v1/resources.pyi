import collections.abc
import typing

import httplib2

import googleapiclient.discovery
import googleapiclient.http

from .schemas import *

_list = list

@typing.type_check_only
class DeepReviewResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class DocumentsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class ReviewsResource(googleapiclient.discovery.Resource):
            def create(
                self,
                *,
                parent: str,
                body: Review,
                requestId: str | None = ...,
                reviewId: str | None = ...,
                **kwargs: typing.Any,
            ) -> OperationHttpRequest: ...
            def get(self, *, name: str, **kwargs: typing.Any) -> ReviewHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                filter: str | None = ...,
                orderBy: str | None = ...,
                pageSize: int | None = ...,
                pageToken: str | None = ...,
                **kwargs: typing.Any,
            ) -> ListReviewsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListReviewsResponseHttpRequest,
                previous_response: ListReviewsResponse,
            ) -> ListReviewsResponseHttpRequest | None: ...

        def delete(
            self,
            *,
            name: str,
            allowMissing: bool | None = ...,
            force: bool | None = ...,
            **kwargs: typing.Any,
        ) -> EmptyHttpRequest: ...
        def estimateReviewCost(
            self,
            *,
            document: str,
            body: EstimateReviewCostRequest,
            **kwargs: typing.Any,
        ) -> EstimateReviewCostResponseHttpRequest: ...
        def get(self, *, name: str, **kwargs: typing.Any) -> DocumentHttpRequest: ...
        def list(
            self,
            *,
            filter: str | None = ...,
            orderBy: str | None = ...,
            pageSize: int | None = ...,
            pageToken: str | None = ...,
            **kwargs: typing.Any,
        ) -> ListDocumentsResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: ListDocumentsResponseHttpRequest,
            previous_response: ListDocumentsResponse,
        ) -> ListDocumentsResponseHttpRequest | None: ...
        def reviews(self) -> ReviewsResource: ...

    @typing.type_check_only
    class MediaResource(googleapiclient.discovery.Resource):
        def download(
            self, *, name: str, **kwargs: typing.Any
        ) -> DownloadDocumentResponseHttpRequest: ...
        def download_media(
            self, *, name: str, **kwargs: typing.Any
        ) -> BytesHttpRequest: ...
        def upload(
            self,
            *,
            body: Document,
            documentId: str | None = ...,
            requestId: str | None = ...,
            **kwargs: typing.Any,
        ) -> DocumentHttpRequest: ...

    @typing.type_check_only
    class OperationsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class DocumentsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class ReviewsResource(googleapiclient.discovery.Resource):
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> OperationHttpRequest: ...

            def reviews(self) -> ReviewsResource: ...

        def documents(self) -> DocumentsResource: ...

    @typing.type_check_only
    class V1Resource(googleapiclient.discovery.Resource):
        def getUserQuota(
            self, *, name: str, **kwargs: typing.Any
        ) -> UserQuotaHttpRequest: ...

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
    def documents(self) -> DocumentsResource: ...
    def media(self) -> MediaResource: ...
    def operations(self) -> OperationsResource: ...
    def v1(self) -> V1Resource: ...

@typing.type_check_only
class DocumentHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Document: ...

@typing.type_check_only
class DownloadDocumentResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> DownloadDocumentResponse: ...

@typing.type_check_only
class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Empty: ...

@typing.type_check_only
class EstimateReviewCostResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> EstimateReviewCostResponse: ...

@typing.type_check_only
class ListDocumentsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListDocumentsResponse: ...

@typing.type_check_only
class ListReviewsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListReviewsResponse: ...

@typing.type_check_only
class OperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Operation: ...

@typing.type_check_only
class ReviewHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Review: ...

@typing.type_check_only
class UserQuotaHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> UserQuota: ...

@typing.type_check_only
class BytesHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> bytes: ...
