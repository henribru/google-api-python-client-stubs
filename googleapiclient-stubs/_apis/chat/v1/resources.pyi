import collections.abc
import typing

import httplib2
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http

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
            **kwargs: typing.Any,
        ) -> UploadAttachmentResponseHttpRequest: ...

    @typing.type_check_only
    class SpacesResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class MembersResource(googleapiclient.discovery.Resource):
            def create(
                self,
                *,
                parent: str,
                body: Membership = ...,
                useAdminAccess: bool = ...,
                **kwargs: typing.Any,
            ) -> MembershipHttpRequest: ...
            def delete(
                self, *, name: str, useAdminAccess: bool = ..., **kwargs: typing.Any
            ) -> MembershipHttpRequest: ...
            def get(
                self, *, name: str, useAdminAccess: bool = ..., **kwargs: typing.Any
            ) -> MembershipHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                filter: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                showGroups: bool = ...,
                showInvited: bool = ...,
                useAdminAccess: bool = ...,
                **kwargs: typing.Any,
            ) -> ListMembershipsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListMembershipsResponseHttpRequest,
                previous_response: ListMembershipsResponse,
            ) -> ListMembershipsResponseHttpRequest | None: ...
            def patch(
                self,
                *,
                name: str,
                body: Membership = ...,
                updateMask: str = ...,
                useAdminAccess: bool = ...,
                **kwargs: typing.Any,
            ) -> MembershipHttpRequest: ...

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
                    **kwargs: typing.Any,
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
                **kwargs: typing.Any,
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
                **kwargs: typing.Any,
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
                **kwargs: typing.Any,
            ) -> MessageHttpRequest: ...
            def update(
                self,
                *,
                name: str,
                body: Message = ...,
                allowMissing: bool = ...,
                updateMask: str = ...,
                **kwargs: typing.Any,
            ) -> MessageHttpRequest: ...
            def attachments(self) -> AttachmentsResource: ...
            def reactions(self) -> ReactionsResource: ...

        @typing.type_check_only
        class SpaceEventsResource(googleapiclient.discovery.Resource):
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> SpaceEventHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                filter: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any,
            ) -> ListSpaceEventsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListSpaceEventsResponseHttpRequest,
                previous_response: ListSpaceEventsResponse,
            ) -> ListSpaceEventsResponseHttpRequest | None: ...

        def completeImport(
            self,
            *,
            name: str,
            body: CompleteImportSpaceRequest = ...,
            **kwargs: typing.Any,
        ) -> CompleteImportSpaceResponseHttpRequest: ...
        def create(
            self, *, body: Space = ..., requestId: str = ..., **kwargs: typing.Any
        ) -> SpaceHttpRequest: ...
        def delete(
            self, *, name: str, useAdminAccess: bool = ..., **kwargs: typing.Any
        ) -> EmptyHttpRequest: ...
        def findDirectMessage(
            self, *, name: str = ..., **kwargs: typing.Any
        ) -> SpaceHttpRequest: ...
        def get(
            self, *, name: str, useAdminAccess: bool = ..., **kwargs: typing.Any
        ) -> SpaceHttpRequest: ...
        def list(
            self,
            *,
            filter: str = ...,
            pageSize: int = ...,
            pageToken: str = ...,
            **kwargs: typing.Any,
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
            useAdminAccess: bool = ...,
            **kwargs: typing.Any,
        ) -> SpaceHttpRequest: ...
        def search(
            self,
            *,
            orderBy: str = ...,
            pageSize: int = ...,
            pageToken: str = ...,
            query: str = ...,
            useAdminAccess: bool = ...,
            **kwargs: typing.Any,
        ) -> SearchSpacesResponseHttpRequest: ...
        def search_next(
            self,
            previous_request: SearchSpacesResponseHttpRequest,
            previous_response: SearchSpacesResponse,
        ) -> SearchSpacesResponseHttpRequest | None: ...
        def setup(
            self, *, body: SetUpSpaceRequest = ..., **kwargs: typing.Any
        ) -> SpaceHttpRequest: ...
        def members(self) -> MembersResource: ...
        def messages(self) -> MessagesResource: ...
        def spaceEvents(self) -> SpaceEventsResource: ...

    @typing.type_check_only
    class UsersResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class SpacesResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class ThreadsResource(googleapiclient.discovery.Resource):
                def getThreadReadState(
                    self, *, name: str, **kwargs: typing.Any
                ) -> ThreadReadStateHttpRequest: ...

            def getSpaceReadState(
                self, *, name: str, **kwargs: typing.Any
            ) -> SpaceReadStateHttpRequest: ...
            def updateSpaceReadState(
                self,
                *,
                name: str,
                body: SpaceReadState = ...,
                updateMask: str = ...,
                **kwargs: typing.Any,
            ) -> SpaceReadStateHttpRequest: ...
            def threads(self) -> ThreadsResource: ...

        def spaces(self) -> SpacesResource: ...

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
    def spaces(self) -> SpacesResource: ...
    def users(self) -> UsersResource: ...

@typing.type_check_only
class AttachmentHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Attachment: ...

@typing.type_check_only
class CompleteImportSpaceResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> CompleteImportSpaceResponse: ...

@typing.type_check_only
class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Empty: ...

@typing.type_check_only
class ListMembershipsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListMembershipsResponse: ...

@typing.type_check_only
class ListMessagesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListMessagesResponse: ...

@typing.type_check_only
class ListReactionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListReactionsResponse: ...

@typing.type_check_only
class ListSpaceEventsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListSpaceEventsResponse: ...

@typing.type_check_only
class ListSpacesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListSpacesResponse: ...

@typing.type_check_only
class MediaHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Media: ...

@typing.type_check_only
class MembershipHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Membership: ...

@typing.type_check_only
class MessageHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Message: ...

@typing.type_check_only
class ReactionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Reaction: ...

@typing.type_check_only
class SearchSpacesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> SearchSpacesResponse: ...

@typing.type_check_only
class SpaceHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Space: ...

@typing.type_check_only
class SpaceEventHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> SpaceEvent: ...

@typing.type_check_only
class SpaceReadStateHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> SpaceReadState: ...

@typing.type_check_only
class ThreadReadStateHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ThreadReadState: ...

@typing.type_check_only
class UploadAttachmentResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> UploadAttachmentResponse: ...

@typing.type_check_only
class BytesHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> bytes: ...
