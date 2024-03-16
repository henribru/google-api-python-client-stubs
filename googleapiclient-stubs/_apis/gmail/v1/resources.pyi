import collections.abc
import typing

import httplib2
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http

from .schemas import *

_list = list

@typing.type_check_only
class GmailResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class UsersResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class DraftsResource(googleapiclient.discovery.Resource):
            def create(
                self, *, userId: str, body: Draft = ..., **kwargs: typing.Any
            ) -> DraftHttpRequest: ...
            def delete(
                self, *, userId: str, id: str, **kwargs: typing.Any
            ) -> googleapiclient.http.HttpRequest: ...
            def get(
                self,
                *,
                userId: str,
                id: str,
                format: typing_extensions.Literal[
                    "minimal", "full", "raw", "metadata"
                ] = ...,
                **kwargs: typing.Any,
            ) -> DraftHttpRequest: ...
            def list(
                self,
                *,
                userId: str,
                includeSpamTrash: bool = ...,
                maxResults: int = ...,
                pageToken: str = ...,
                q: str = ...,
                **kwargs: typing.Any,
            ) -> ListDraftsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListDraftsResponseHttpRequest,
                previous_response: ListDraftsResponse,
            ) -> ListDraftsResponseHttpRequest | None: ...
            def send(
                self, *, userId: str, body: Draft = ..., **kwargs: typing.Any
            ) -> MessageHttpRequest: ...
            def update(
                self, *, userId: str, id: str, body: Draft = ..., **kwargs: typing.Any
            ) -> DraftHttpRequest: ...

        @typing.type_check_only
        class HistoryResource(googleapiclient.discovery.Resource):
            def list(
                self,
                *,
                userId: str,
                historyTypes: typing_extensions.Literal[
                    "messageAdded", "messageDeleted", "labelAdded", "labelRemoved"
                ]
                | _list[
                    typing_extensions.Literal[
                        "messageAdded", "messageDeleted", "labelAdded", "labelRemoved"
                    ]
                ] = ...,
                labelId: str = ...,
                maxResults: int = ...,
                pageToken: str = ...,
                startHistoryId: str = ...,
                **kwargs: typing.Any,
            ) -> ListHistoryResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListHistoryResponseHttpRequest,
                previous_response: ListHistoryResponse,
            ) -> ListHistoryResponseHttpRequest | None: ...

        @typing.type_check_only
        class LabelsResource(googleapiclient.discovery.Resource):
            def create(
                self, *, userId: str, body: Label = ..., **kwargs: typing.Any
            ) -> LabelHttpRequest: ...
            def delete(
                self, *, userId: str, id: str, **kwargs: typing.Any
            ) -> googleapiclient.http.HttpRequest: ...
            def get(
                self, *, userId: str, id: str, **kwargs: typing.Any
            ) -> LabelHttpRequest: ...
            def list(
                self, *, userId: str, **kwargs: typing.Any
            ) -> ListLabelsResponseHttpRequest: ...
            def patch(
                self, *, userId: str, id: str, body: Label = ..., **kwargs: typing.Any
            ) -> LabelHttpRequest: ...
            def update(
                self, *, userId: str, id: str, body: Label = ..., **kwargs: typing.Any
            ) -> LabelHttpRequest: ...

        @typing.type_check_only
        class MessagesResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class AttachmentsResource(googleapiclient.discovery.Resource):
                def get(
                    self, *, userId: str, messageId: str, id: str, **kwargs: typing.Any
                ) -> MessagePartBodyHttpRequest: ...

            def batchDelete(
                self,
                *,
                userId: str,
                body: BatchDeleteMessagesRequest = ...,
                **kwargs: typing.Any,
            ) -> googleapiclient.http.HttpRequest: ...
            def batchModify(
                self,
                *,
                userId: str,
                body: BatchModifyMessagesRequest = ...,
                **kwargs: typing.Any,
            ) -> googleapiclient.http.HttpRequest: ...
            def delete(
                self, *, userId: str, id: str, **kwargs: typing.Any
            ) -> googleapiclient.http.HttpRequest: ...
            def get(
                self,
                *,
                userId: str,
                id: str,
                format: typing_extensions.Literal[
                    "minimal", "full", "raw", "metadata"
                ] = ...,
                metadataHeaders: str | _list[str] = ...,
                **kwargs: typing.Any,
            ) -> MessageHttpRequest: ...
            def import_(
                self,
                *,
                userId: str,
                body: Message = ...,
                deleted: bool = ...,
                internalDateSource: typing_extensions.Literal[
                    "receivedTime", "dateHeader"
                ] = ...,
                neverMarkSpam: bool = ...,
                processForCalendar: bool = ...,
                **kwargs: typing.Any,
            ) -> MessageHttpRequest: ...
            def insert(
                self,
                *,
                userId: str,
                body: Message = ...,
                deleted: bool = ...,
                internalDateSource: typing_extensions.Literal[
                    "receivedTime", "dateHeader"
                ] = ...,
                **kwargs: typing.Any,
            ) -> MessageHttpRequest: ...
            def list(
                self,
                *,
                userId: str,
                includeSpamTrash: bool = ...,
                labelIds: str | _list[str] = ...,
                maxResults: int = ...,
                pageToken: str = ...,
                q: str = ...,
                **kwargs: typing.Any,
            ) -> ListMessagesResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListMessagesResponseHttpRequest,
                previous_response: ListMessagesResponse,
            ) -> ListMessagesResponseHttpRequest | None: ...
            def modify(
                self,
                *,
                userId: str,
                id: str,
                body: ModifyMessageRequest = ...,
                **kwargs: typing.Any,
            ) -> MessageHttpRequest: ...
            def send(
                self, *, userId: str, body: Message = ..., **kwargs: typing.Any
            ) -> MessageHttpRequest: ...
            def trash(
                self, *, userId: str, id: str, **kwargs: typing.Any
            ) -> MessageHttpRequest: ...
            def untrash(
                self, *, userId: str, id: str, **kwargs: typing.Any
            ) -> MessageHttpRequest: ...
            def attachments(self) -> AttachmentsResource: ...

        @typing.type_check_only
        class SettingsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class CseResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class IdentitiesResource(googleapiclient.discovery.Resource):
                    def create(
                        self,
                        *,
                        userId: str,
                        body: CseIdentity = ...,
                        **kwargs: typing.Any,
                    ) -> CseIdentityHttpRequest: ...
                    def delete(
                        self, *, userId: str, cseEmailAddress: str, **kwargs: typing.Any
                    ) -> googleapiclient.http.HttpRequest: ...
                    def get(
                        self, *, userId: str, cseEmailAddress: str, **kwargs: typing.Any
                    ) -> CseIdentityHttpRequest: ...
                    def list(
                        self,
                        *,
                        userId: str,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
                    ) -> ListCseIdentitiesResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: ListCseIdentitiesResponseHttpRequest,
                        previous_response: ListCseIdentitiesResponse,
                    ) -> ListCseIdentitiesResponseHttpRequest | None: ...
                    def patch(
                        self,
                        *,
                        userId: str,
                        emailAddress: str,
                        body: CseIdentity = ...,
                        **kwargs: typing.Any,
                    ) -> CseIdentityHttpRequest: ...

                @typing.type_check_only
                class KeypairsResource(googleapiclient.discovery.Resource):
                    def create(
                        self,
                        *,
                        userId: str,
                        body: CseKeyPair = ...,
                        **kwargs: typing.Any,
                    ) -> CseKeyPairHttpRequest: ...
                    def disable(
                        self,
                        *,
                        userId: str,
                        keyPairId: str,
                        body: DisableCseKeyPairRequest = ...,
                        **kwargs: typing.Any,
                    ) -> CseKeyPairHttpRequest: ...
                    def enable(
                        self,
                        *,
                        userId: str,
                        keyPairId: str,
                        body: EnableCseKeyPairRequest = ...,
                        **kwargs: typing.Any,
                    ) -> CseKeyPairHttpRequest: ...
                    def get(
                        self, *, userId: str, keyPairId: str, **kwargs: typing.Any
                    ) -> CseKeyPairHttpRequest: ...
                    def list(
                        self,
                        *,
                        userId: str,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
                    ) -> ListCseKeyPairsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: ListCseKeyPairsResponseHttpRequest,
                        previous_response: ListCseKeyPairsResponse,
                    ) -> ListCseKeyPairsResponseHttpRequest | None: ...
                    def obliterate(
                        self,
                        *,
                        userId: str,
                        keyPairId: str,
                        body: ObliterateCseKeyPairRequest = ...,
                        **kwargs: typing.Any,
                    ) -> googleapiclient.http.HttpRequest: ...

                def identities(self) -> IdentitiesResource: ...
                def keypairs(self) -> KeypairsResource: ...

            @typing.type_check_only
            class DelegatesResource(googleapiclient.discovery.Resource):
                def create(
                    self, *, userId: str, body: Delegate = ..., **kwargs: typing.Any
                ) -> DelegateHttpRequest: ...
                def delete(
                    self, *, userId: str, delegateEmail: str, **kwargs: typing.Any
                ) -> googleapiclient.http.HttpRequest: ...
                def get(
                    self, *, userId: str, delegateEmail: str, **kwargs: typing.Any
                ) -> DelegateHttpRequest: ...
                def list(
                    self, *, userId: str, **kwargs: typing.Any
                ) -> ListDelegatesResponseHttpRequest: ...

            @typing.type_check_only
            class FiltersResource(googleapiclient.discovery.Resource):
                def create(
                    self, *, userId: str, body: Filter = ..., **kwargs: typing.Any
                ) -> FilterHttpRequest: ...
                def delete(
                    self, *, userId: str, id: str, **kwargs: typing.Any
                ) -> googleapiclient.http.HttpRequest: ...
                def get(
                    self, *, userId: str, id: str, **kwargs: typing.Any
                ) -> FilterHttpRequest: ...
                def list(
                    self, *, userId: str, **kwargs: typing.Any
                ) -> ListFiltersResponseHttpRequest: ...

            @typing.type_check_only
            class ForwardingAddressesResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    userId: str,
                    body: ForwardingAddress = ...,
                    **kwargs: typing.Any,
                ) -> ForwardingAddressHttpRequest: ...
                def delete(
                    self, *, userId: str, forwardingEmail: str, **kwargs: typing.Any
                ) -> googleapiclient.http.HttpRequest: ...
                def get(
                    self, *, userId: str, forwardingEmail: str, **kwargs: typing.Any
                ) -> ForwardingAddressHttpRequest: ...
                def list(
                    self, *, userId: str, **kwargs: typing.Any
                ) -> ListForwardingAddressesResponseHttpRequest: ...

            @typing.type_check_only
            class SendAsResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class SmimeInfoResource(googleapiclient.discovery.Resource):
                    def delete(
                        self,
                        *,
                        userId: str,
                        sendAsEmail: str,
                        id: str,
                        **kwargs: typing.Any,
                    ) -> googleapiclient.http.HttpRequest: ...
                    def get(
                        self,
                        *,
                        userId: str,
                        sendAsEmail: str,
                        id: str,
                        **kwargs: typing.Any,
                    ) -> SmimeInfoHttpRequest: ...
                    def insert(
                        self,
                        *,
                        userId: str,
                        sendAsEmail: str,
                        body: SmimeInfo = ...,
                        **kwargs: typing.Any,
                    ) -> SmimeInfoHttpRequest: ...
                    def list(
                        self, *, userId: str, sendAsEmail: str, **kwargs: typing.Any
                    ) -> ListSmimeInfoResponseHttpRequest: ...
                    def setDefault(
                        self,
                        *,
                        userId: str,
                        sendAsEmail: str,
                        id: str,
                        **kwargs: typing.Any,
                    ) -> googleapiclient.http.HttpRequest: ...

                def create(
                    self, *, userId: str, body: SendAs = ..., **kwargs: typing.Any
                ) -> SendAsHttpRequest: ...
                def delete(
                    self, *, userId: str, sendAsEmail: str, **kwargs: typing.Any
                ) -> googleapiclient.http.HttpRequest: ...
                def get(
                    self, *, userId: str, sendAsEmail: str, **kwargs: typing.Any
                ) -> SendAsHttpRequest: ...
                def list(
                    self, *, userId: str, **kwargs: typing.Any
                ) -> ListSendAsResponseHttpRequest: ...
                def patch(
                    self,
                    *,
                    userId: str,
                    sendAsEmail: str,
                    body: SendAs = ...,
                    **kwargs: typing.Any,
                ) -> SendAsHttpRequest: ...
                def update(
                    self,
                    *,
                    userId: str,
                    sendAsEmail: str,
                    body: SendAs = ...,
                    **kwargs: typing.Any,
                ) -> SendAsHttpRequest: ...
                def verify(
                    self, *, userId: str, sendAsEmail: str, **kwargs: typing.Any
                ) -> googleapiclient.http.HttpRequest: ...
                def smimeInfo(self) -> SmimeInfoResource: ...

            def getAutoForwarding(
                self, *, userId: str, **kwargs: typing.Any
            ) -> AutoForwardingHttpRequest: ...
            def getImap(
                self, *, userId: str, **kwargs: typing.Any
            ) -> ImapSettingsHttpRequest: ...
            def getLanguage(
                self, *, userId: str, **kwargs: typing.Any
            ) -> LanguageSettingsHttpRequest: ...
            def getPop(
                self, *, userId: str, **kwargs: typing.Any
            ) -> PopSettingsHttpRequest: ...
            def getVacation(
                self, *, userId: str, **kwargs: typing.Any
            ) -> VacationSettingsHttpRequest: ...
            def updateAutoForwarding(
                self, *, userId: str, body: AutoForwarding = ..., **kwargs: typing.Any
            ) -> AutoForwardingHttpRequest: ...
            def updateImap(
                self, *, userId: str, body: ImapSettings = ..., **kwargs: typing.Any
            ) -> ImapSettingsHttpRequest: ...
            def updateLanguage(
                self, *, userId: str, body: LanguageSettings = ..., **kwargs: typing.Any
            ) -> LanguageSettingsHttpRequest: ...
            def updatePop(
                self, *, userId: str, body: PopSettings = ..., **kwargs: typing.Any
            ) -> PopSettingsHttpRequest: ...
            def updateVacation(
                self, *, userId: str, body: VacationSettings = ..., **kwargs: typing.Any
            ) -> VacationSettingsHttpRequest: ...
            def cse(self) -> CseResource: ...
            def delegates(self) -> DelegatesResource: ...
            def filters(self) -> FiltersResource: ...
            def forwardingAddresses(self) -> ForwardingAddressesResource: ...
            def sendAs(self) -> SendAsResource: ...

        @typing.type_check_only
        class ThreadsResource(googleapiclient.discovery.Resource):
            def delete(
                self, *, userId: str, id: str, **kwargs: typing.Any
            ) -> googleapiclient.http.HttpRequest: ...
            def get(
                self,
                *,
                userId: str,
                id: str,
                format: typing_extensions.Literal["full", "metadata", "minimal"] = ...,
                metadataHeaders: str | _list[str] = ...,
                **kwargs: typing.Any,
            ) -> ThreadHttpRequest: ...
            def list(
                self,
                *,
                userId: str,
                includeSpamTrash: bool = ...,
                labelIds: str | _list[str] = ...,
                maxResults: int = ...,
                pageToken: str = ...,
                q: str = ...,
                **kwargs: typing.Any,
            ) -> ListThreadsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListThreadsResponseHttpRequest,
                previous_response: ListThreadsResponse,
            ) -> ListThreadsResponseHttpRequest | None: ...
            def modify(
                self,
                *,
                userId: str,
                id: str,
                body: ModifyThreadRequest = ...,
                **kwargs: typing.Any,
            ) -> ThreadHttpRequest: ...
            def trash(
                self, *, userId: str, id: str, **kwargs: typing.Any
            ) -> ThreadHttpRequest: ...
            def untrash(
                self, *, userId: str, id: str, **kwargs: typing.Any
            ) -> ThreadHttpRequest: ...

        def getProfile(
            self, *, userId: str, **kwargs: typing.Any
        ) -> ProfileHttpRequest: ...
        def stop(
            self, *, userId: str, **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def watch(
            self, *, userId: str, body: WatchRequest = ..., **kwargs: typing.Any
        ) -> WatchResponseHttpRequest: ...
        def drafts(self) -> DraftsResource: ...
        def history(self) -> HistoryResource: ...
        def labels(self) -> LabelsResource: ...
        def messages(self) -> MessagesResource: ...
        def settings(self) -> SettingsResource: ...
        def threads(self) -> ThreadsResource: ...

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
    def users(self) -> UsersResource: ...

@typing.type_check_only
class AutoForwardingHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> AutoForwarding: ...

@typing.type_check_only
class CseIdentityHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> CseIdentity: ...

@typing.type_check_only
class CseKeyPairHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> CseKeyPair: ...

@typing.type_check_only
class DelegateHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Delegate: ...

@typing.type_check_only
class DraftHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Draft: ...

@typing.type_check_only
class FilterHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Filter: ...

@typing.type_check_only
class ForwardingAddressHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ForwardingAddress: ...

@typing.type_check_only
class ImapSettingsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ImapSettings: ...

@typing.type_check_only
class LabelHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Label: ...

@typing.type_check_only
class LanguageSettingsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> LanguageSettings: ...

@typing.type_check_only
class ListCseIdentitiesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListCseIdentitiesResponse: ...

@typing.type_check_only
class ListCseKeyPairsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListCseKeyPairsResponse: ...

@typing.type_check_only
class ListDelegatesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListDelegatesResponse: ...

@typing.type_check_only
class ListDraftsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListDraftsResponse: ...

@typing.type_check_only
class ListFiltersResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListFiltersResponse: ...

@typing.type_check_only
class ListForwardingAddressesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListForwardingAddressesResponse: ...

@typing.type_check_only
class ListHistoryResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListHistoryResponse: ...

@typing.type_check_only
class ListLabelsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListLabelsResponse: ...

@typing.type_check_only
class ListMessagesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListMessagesResponse: ...

@typing.type_check_only
class ListSendAsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListSendAsResponse: ...

@typing.type_check_only
class ListSmimeInfoResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListSmimeInfoResponse: ...

@typing.type_check_only
class ListThreadsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListThreadsResponse: ...

@typing.type_check_only
class MessageHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Message: ...

@typing.type_check_only
class MessagePartBodyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> MessagePartBody: ...

@typing.type_check_only
class PopSettingsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> PopSettings: ...

@typing.type_check_only
class ProfileHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Profile: ...

@typing.type_check_only
class SendAsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> SendAs: ...

@typing.type_check_only
class SmimeInfoHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> SmimeInfo: ...

@typing.type_check_only
class ThreadHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Thread: ...

@typing.type_check_only
class VacationSettingsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> VacationSettings: ...

@typing.type_check_only
class WatchResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> WatchResponse: ...
