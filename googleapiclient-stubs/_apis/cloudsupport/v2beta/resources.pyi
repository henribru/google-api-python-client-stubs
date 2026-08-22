import collections.abc
import typing

import httplib2

import googleapiclient.discovery
import googleapiclient.http

from .schemas import *

_list = list

@typing.type_check_only
class CloudSupportResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class CaseClassificationsResource(googleapiclient.discovery.Resource):
        def search(
            self,
            *,
            pageSize: int | None = ...,
            pageToken: str | None = ...,
            product_productLine: typing.Literal[
                "PRODUCT_LINE_UNSPECIFIED", "GOOGLE_CLOUD", "GOOGLE_MAPS"
            ]
            | None = ...,
            query: str | None = ...,
            **kwargs: typing.Any,
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
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> AttachmentHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int | None = ...,
                pageToken: str | None = ...,
                **kwargs: typing.Any,
            ) -> ListAttachmentsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListAttachmentsResponseHttpRequest,
                previous_response: ListAttachmentsResponse,
            ) -> ListAttachmentsResponseHttpRequest | None: ...

        @typing.type_check_only
        class CommentsResource(googleapiclient.discovery.Resource):
            def create(
                self, *, parent: str, body: Comment, **kwargs: typing.Any
            ) -> CommentHttpRequest: ...
            def get(self, *, name: str, **kwargs: typing.Any) -> CommentHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int | None = ...,
                pageToken: str | None = ...,
                **kwargs: typing.Any,
            ) -> ListCommentsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListCommentsResponseHttpRequest,
                previous_response: ListCommentsResponse,
            ) -> ListCommentsResponseHttpRequest | None: ...

        def close(  # type: ignore[override]
            self, *, name: str, body: CloseCaseRequest, **kwargs: typing.Any
        ) -> CaseHttpRequest: ...
        def create(
            self, *, parent: str, body: Case, **kwargs: typing.Any
        ) -> CaseHttpRequest: ...
        def escalate(
            self, *, name: str, body: EscalateCaseRequest, **kwargs: typing.Any
        ) -> CaseHttpRequest: ...
        def get(self, *, name: str, **kwargs: typing.Any) -> CaseHttpRequest: ...
        def list(
            self,
            *,
            parent: str,
            filter: str | None = ...,
            pageSize: int | None = ...,
            pageToken: str | None = ...,
            productLine: typing.Literal[
                "PRODUCT_LINE_UNSPECIFIED", "GOOGLE_CLOUD", "GOOGLE_MAPS"
            ]
            | None = ...,
            **kwargs: typing.Any,
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
            body: Case,
            updateMask: str | None = ...,
            **kwargs: typing.Any,
        ) -> CaseHttpRequest: ...
        def search(
            self,
            *,
            pageSize: int | None = ...,
            pageToken: str | None = ...,
            parent: str | None = ...,
            query: str | None = ...,
            **kwargs: typing.Any,
        ) -> SearchCasesResponseHttpRequest: ...
        def search_next(
            self,
            previous_request: SearchCasesResponseHttpRequest,
            previous_response: SearchCasesResponse,
        ) -> SearchCasesResponseHttpRequest | None: ...
        def showFeed(
            self,
            *,
            parent: str,
            orderBy: str | None = ...,
            pageSize: int | None = ...,
            pageToken: str | None = ...,
            **kwargs: typing.Any,
        ) -> ShowFeedResponseHttpRequest: ...
        def showFeed_next(
            self,
            previous_request: ShowFeedResponseHttpRequest,
            previous_response: ShowFeedResponse,
        ) -> ShowFeedResponseHttpRequest | None: ...
        def attachments(self) -> AttachmentsResource: ...
        def comments(self) -> CommentsResource: ...

    @typing.type_check_only
    class MediaResource(googleapiclient.discovery.Resource):
        def download(self, *, name: str, **kwargs: typing.Any) -> MediaHttpRequest: ...
        def download_media(
            self, *, name: str, **kwargs: typing.Any
        ) -> BytesHttpRequest: ...
        def upload(
            self, *, parent: str, body: CreateAttachmentRequest, **kwargs: typing.Any
        ) -> AttachmentHttpRequest: ...

    @typing.type_check_only
    class OrganizationsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class SupportEventSubscriptionsResource(googleapiclient.discovery.Resource):
            def create(
                self,
                *,
                parent: str,
                body: SupportEventSubscription,
                **kwargs: typing.Any,
            ) -> SupportEventSubscriptionHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> SupportEventSubscriptionHttpRequest: ...
            def expunge(
                self,
                *,
                name: str,
                body: ExpungeSupportEventSubscriptionRequest,
                **kwargs: typing.Any,
            ) -> EmptyHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> SupportEventSubscriptionHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                filter: str | None = ...,
                pageSize: int | None = ...,
                pageToken: str | None = ...,
                showDeleted: bool | None = ...,
                **kwargs: typing.Any,
            ) -> ListSupportEventSubscriptionsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListSupportEventSubscriptionsResponseHttpRequest,
                previous_response: ListSupportEventSubscriptionsResponse,
            ) -> ListSupportEventSubscriptionsResponseHttpRequest | None: ...
            def patch(
                self,
                *,
                name: str,
                body: SupportEventSubscription,
                updateMask: str | None = ...,
                **kwargs: typing.Any,
            ) -> SupportEventSubscriptionHttpRequest: ...
            def undelete(
                self,
                *,
                name: str,
                body: UndeleteSupportEventSubscriptionRequest,
                **kwargs: typing.Any,
            ) -> SupportEventSubscriptionHttpRequest: ...

        def supportEventSubscriptions(self) -> SupportEventSubscriptionsResource: ...

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
    def caseClassifications(self) -> CaseClassificationsResource: ...
    def cases(self) -> CasesResource: ...
    def media(self) -> MediaResource: ...
    def organizations(self) -> OrganizationsResource: ...

@typing.type_check_only
class AttachmentHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Attachment: ...

@typing.type_check_only
class CaseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Case: ...

@typing.type_check_only
class CommentHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Comment: ...

@typing.type_check_only
class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Empty: ...

@typing.type_check_only
class ListAttachmentsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListAttachmentsResponse: ...

@typing.type_check_only
class ListCasesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListCasesResponse: ...

@typing.type_check_only
class ListCommentsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListCommentsResponse: ...

@typing.type_check_only
class ListSupportEventSubscriptionsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListSupportEventSubscriptionsResponse: ...

@typing.type_check_only
class MediaHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Media: ...

@typing.type_check_only
class SearchCaseClassificationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> SearchCaseClassificationsResponse: ...

@typing.type_check_only
class SearchCasesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> SearchCasesResponse: ...

@typing.type_check_only
class ShowFeedResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ShowFeedResponse: ...

@typing.type_check_only
class SupportEventSubscriptionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> SupportEventSubscription: ...

@typing.type_check_only
class BytesHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> bytes: ...
