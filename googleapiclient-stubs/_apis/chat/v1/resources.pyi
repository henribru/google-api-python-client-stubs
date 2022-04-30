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
    class DmsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class ConversationsResource(googleapiclient.discovery.Resource):
            def messages(
                self,
                *,
                parent: str,
                body: Message = ...,
                requestId: str = ...,
                threadKey: str = ...,
                **kwargs: typing.Any
            ) -> MessageHttpRequest: ...

        def messages(
            self,
            *,
            parent: str,
            body: Message = ...,
            requestId: str = ...,
            threadKey: str = ...,
            **kwargs: typing.Any
        ) -> MessageHttpRequest: ...
        def webhooks(
            self,
            *,
            parent: str,
            body: Message = ...,
            requestId: str = ...,
            threadKey: str = ...,
            **kwargs: typing.Any
        ) -> MessageHttpRequest: ...
        def conversations(self) -> ConversationsResource: ...

    @typing.type_check_only
    class MediaResource(googleapiclient.discovery.Resource):
        def download(
            self, *, resourceName: str, **kwargs: typing.Any
        ) -> MediaHttpRequest: ...

    @typing.type_check_only
    class RoomsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class ConversationsResource(googleapiclient.discovery.Resource):
            def messages(
                self,
                *,
                parent: str,
                body: Message = ...,
                requestId: str = ...,
                threadKey: str = ...,
                **kwargs: typing.Any
            ) -> MessageHttpRequest: ...

        def messages(
            self,
            *,
            parent: str,
            body: Message = ...,
            requestId: str = ...,
            threadKey: str = ...,
            **kwargs: typing.Any
        ) -> MessageHttpRequest: ...
        def webhooks(
            self,
            *,
            parent: str,
            body: Message = ...,
            requestId: str = ...,
            threadKey: str = ...,
            **kwargs: typing.Any
        ) -> MessageHttpRequest: ...
        def conversations(self) -> ConversationsResource: ...

    @typing.type_check_only
    class SpacesResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class MembersResource(googleapiclient.discovery.Resource):
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> MembershipHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
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

            def create(
                self,
                *,
                parent: str,
                body: Message = ...,
                requestId: str = ...,
                threadKey: str = ...,
                **kwargs: typing.Any
            ) -> MessageHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def get(self, *, name: str, **kwargs: typing.Any) -> MessageHttpRequest: ...
            def update(
                self,
                *,
                name: str,
                body: Message = ...,
                updateMask: str = ...,
                **kwargs: typing.Any
            ) -> MessageHttpRequest: ...
            def attachments(self) -> AttachmentsResource: ...

        def get(self, *, name: str, **kwargs: typing.Any) -> SpaceHttpRequest: ...
        def list(
            self, *, pageSize: int = ..., pageToken: str = ..., **kwargs: typing.Any
        ) -> ListSpacesResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: ListSpacesResponseHttpRequest,
            previous_response: ListSpacesResponse,
        ) -> ListSpacesResponseHttpRequest | None: ...
        def webhooks(
            self,
            *,
            parent: str,
            body: Message = ...,
            requestId: str = ...,
            threadKey: str = ...,
            **kwargs: typing.Any
        ) -> MessageHttpRequest: ...
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
    def dms(self) -> DmsResource: ...
    def media(self) -> MediaResource: ...
    def rooms(self) -> RoomsResource: ...
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
class SpaceHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Space: ...
