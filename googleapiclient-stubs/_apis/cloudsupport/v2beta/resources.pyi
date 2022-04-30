import collections.abc
import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

_list = list

@typing.type_check_only
class CloudSupportResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class AttachmentsResource(googleapiclient.discovery.Resource):
        def create(
            self,
            *,
            parent: str,
            body: CreateAttachmentRequest = ...,
            **kwargs: typing.Any
        ) -> AttachmentHttpRequest: ...

    @typing.type_check_only
    class CaseClassificationsResource(googleapiclient.discovery.Resource):
        def search(
            self,
            *,
            pageSize: int = ...,
            pageToken: str = ...,
            query: str = ...,
            **kwargs: typing.Any
        ) -> SearchCaseClassificationsResponseHttpRequest: ...
        def search_next(
            self,
            previous_request: SearchCaseClassificationsResponseHttpRequest,
            previous_response: SearchCaseClassificationsResponse,
        ) -> SearchCaseClassificationsResponseHttpRequest | None: ...

    @typing.type_check_only
    class CasesResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class AttachmentsResource(googleapiclient.discovery.Resource):
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> ListAttachmentsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListAttachmentsResponseHttpRequest,
                previous_response: ListAttachmentsResponse,
            ) -> ListAttachmentsResponseHttpRequest | None: ...

        @typing.type_check_only
        class CommentsResource(googleapiclient.discovery.Resource):
            def create(
                self, *, parent: str, body: Comment = ..., **kwargs: typing.Any
            ) -> CommentHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> ListCommentsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListCommentsResponseHttpRequest,
                previous_response: ListCommentsResponse,
            ) -> ListCommentsResponseHttpRequest | None: ...

        def close(self, *, name: str, body: CloseCaseRequest = ..., **kwargs: typing.Any) -> CaseHttpRequest: ...  # type: ignore
        def create(
            self, *, parent: str, body: Case = ..., **kwargs: typing.Any
        ) -> CaseHttpRequest: ...
        def escalate(
            self, *, name: str, body: EscalateCaseRequest = ..., **kwargs: typing.Any
        ) -> CaseHttpRequest: ...
        def get(self, *, name: str, **kwargs: typing.Any) -> CaseHttpRequest: ...
        def list(
            self,
            *,
            parent: str,
            filter: str = ...,
            pageSize: int = ...,
            pageToken: str = ...,
            **kwargs: typing.Any
        ) -> ListCasesResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: ListCasesResponseHttpRequest,
            previous_response: ListCasesResponse,
        ) -> ListCasesResponseHttpRequest | None: ...
        def patch(
            self,
            *,
            name: str,
            body: Case = ...,
            updateMask: str = ...,
            **kwargs: typing.Any
        ) -> CaseHttpRequest: ...
        def search(
            self,
            *,
            pageSize: int = ...,
            pageToken: str = ...,
            query: str = ...,
            **kwargs: typing.Any
        ) -> SearchCasesResponseHttpRequest: ...
        def search_next(
            self,
            previous_request: SearchCasesResponseHttpRequest,
            previous_response: SearchCasesResponse,
        ) -> SearchCasesResponseHttpRequest | None: ...
        def attachments(self) -> AttachmentsResource: ...
        def comments(self) -> CommentsResource: ...

    @typing.type_check_only
    class MediaResource(googleapiclient.discovery.Resource):
        def download(self, *, name: str, **kwargs: typing.Any) -> MediaHttpRequest: ...
        def upload(
            self,
            *,
            parent: str,
            body: CreateAttachmentRequest = ...,
            **kwargs: typing.Any
        ) -> AttachmentHttpRequest: ...

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
    def attachments(self) -> AttachmentsResource: ...
    def caseClassifications(self) -> CaseClassificationsResource: ...
    def cases(self) -> CasesResource: ...
    def media(self) -> MediaResource: ...

@typing.type_check_only
class AttachmentHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Attachment: ...

@typing.type_check_only
class CaseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Case: ...

@typing.type_check_only
class CommentHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Comment: ...

@typing.type_check_only
class ListAttachmentsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListAttachmentsResponse: ...

@typing.type_check_only
class ListCasesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListCasesResponse: ...

@typing.type_check_only
class ListCommentsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListCommentsResponse: ...

@typing.type_check_only
class MediaHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Media: ...

@typing.type_check_only
class SearchCaseClassificationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> SearchCaseClassificationsResponse: ...

@typing.type_check_only
class SearchCasesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> SearchCasesResponse: ...
