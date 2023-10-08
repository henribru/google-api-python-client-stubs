import collections.abc
import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

_list = list

@typing.type_check_only
class HangoutsChatResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class MediaResource(googleapiclient.discovery.Resource):
        def download(
            self, *, resourceName: str, **kwargs: typing.Any
        ) -> MediaHttpRequest: ...
        def download_media(
            self, *, resourceName: str, **kwargs: typing.Any
        ) -> BytesHttpRequest: ...
        def upload(
            self,
            *,
            parent: str,
            body: UploadAttachmentRequest = ...,
            **kwargs: typing.Any
        ) -> UploadAttachmentResponseHttpRequest: ...

    @typing.type_check_only
    class SpacesResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class MembersResource(googleapiclient.discovery.Resource):
            def create(
                self, *, parent: str, body: Membership = ..., **kwargs: typing.Any
            ) -> MembershipHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> MembershipHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> MembershipHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                filter: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                showInvited: bool = ...,
                **kwargs: typing.Any
            ) -> ListMembershipsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListMembershipsResponseHttpRequest,
                previous_response: ListMembershipsResponse,
            ) -> ListMembershipsResponseHttpRequest | None: ...

        @typing.type_check_only
        class MessagesResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class AttachmentsResource(googleapiclient.discovery.Resource):
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> AttachmentHttpRequest: ...

            @typing.type_check_only
            class ReactionsResource(googleapiclient.discovery.Resource):
                def create(
                    self, *, parent: str, body: Reaction = ..., **kwargs: typing.Any
                ) -> ReactionHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> ListReactionsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListReactionsResponseHttpRequest,
                    previous_response: ListReactionsResponse,
                ) -> ListReactionsResponseHttpRequest | None: ...

            def create(
                self,
                *,
                parent: str,
                body: Message = ...,
                messageId: str = ...,
                messageReplyOption: typing_extensions.Literal[
                    "MESSAGE_REPLY_OPTION_UNSPECIFIED",
                    "REPLY_MESSAGE_FALLBACK_TO_NEW_THREAD",
                    "REPLY_MESSAGE_OR_FAIL",
                ] = ...,
                requestId: str = ...,
                threadKey: str = ...,
                **kwargs: typing.Any
            ) -> MessageHttpRequest: ...
            def delete(
                self, *, name: str, force: bool = ..., **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def get(self, *, name: str, **kwargs: typing.Any) -> MessageHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                filter: str = ...,
                orderBy: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                showDeleted: bool = ...,
                **kwargs: typing.Any
            ) -> ListMessagesResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListMessagesResponseHttpRequest,
                previous_response: ListMessagesResponse,
            ) -> ListMessagesResponseHttpRequest | None: ...
            def patch(
                self,
                *,
                name: str,
                body: Message = ...,
                allowMissing: bool = ...,
                updateMask: str = ...,
                **kwargs: typing.Any
            ) -> MessageHttpRequest: ...
            def update(
                self,
                *,
                name: str,
                body: Message = ...,
                allowMissing: bool = ...,
                updateMask: str = ...,
                **kwargs: typing.Any
            ) -> MessageHttpRequest: ...
            def attachments(self) -> AttachmentsResource: ...
            def reactions(self) -> ReactionsResource: ...

        def create(
            self, *, body: Space = ..., requestId: str = ..., **kwargs: typing.Any
        ) -> SpaceHttpRequest: ...
        def delete(self, *, name: str, **kwargs: typing.Any) -> EmptyHttpRequest: ...
        def findDirectMessage(
            self, *, name: str = ..., **kwargs: typing.Any
        ) -> SpaceHttpRequest: ...
        def get(self, *, name: str, **kwargs: typing.Any) -> SpaceHttpRequest: ...
        def list(
            self,
            *,
            filter: str = ...,
            pageSize: int = ...,
            pageToken: str = ...,
            **kwargs: typing.Any
        ) -> ListSpacesResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: ListSpacesResponseHttpRequest,
            previous_response: ListSpacesResponse,
        ) -> ListSpacesResponseHttpRequest | None: ...
        def patch(
            self,
            *,
            name: str,
            body: Space = ...,
            updateMask: str = ...,
            **kwargs: typing.Any
        ) -> SpaceHttpRequest: ...
        def setup(
            self, *, body: SetUpSpaceRequest = ..., **kwargs: typing.Any
        ) -> SpaceHttpRequest: ...
        def members(self) -> MembersResource: ...
        def messages(self) -> MessagesResource: ...

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
    def media(self) -> MediaResource: ...
    def spaces(self) -> SpacesResource: ...

@typing.type_check_only
class AttachmentHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Attachment: ...

@typing.type_check_only
class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Empty: ...

@typing.type_check_only
class ListMembershipsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListMembershipsResponse: ...

@typing.type_check_only
class ListMessagesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListMessagesResponse: ...

@typing.type_check_only
class ListReactionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListReactionsResponse: ...

@typing.type_check_only
class ListSpacesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListSpacesResponse: ...

@typing.type_check_only
class MediaHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Media: ...

@typing.type_check_only
class MembershipHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Membership: ...

@typing.type_check_only
class MessageHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Message: ...

@typing.type_check_only
class ReactionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Reaction: ...

@typing.type_check_only
class SpaceHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Space: ...

@typing.type_check_only
class UploadAttachmentResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> UploadAttachmentResponse: ...

@typing.type_check_only
class BytesHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> bytes: ...
