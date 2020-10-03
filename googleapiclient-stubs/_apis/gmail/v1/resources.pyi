import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class GmailResource(googleapiclient.discovery.Resource):
    class UsersResource(googleapiclient.discovery.Resource):
        class MessagesResource(googleapiclient.discovery.Resource):
            class AttachmentsResource(googleapiclient.discovery.Resource):
                def get(
                    self, *, userId: str, messageId: str, id: str, **kwargs: typing.Any
                ) -> MessagePartBodyHttpRequest: ...
            def send(
                self, *, userId: str, body: Message = ..., **kwargs: typing.Any
            ) -> MessageHttpRequest: ...
            def untrash(
                self, *, userId: str, id: str, **kwargs: typing.Any
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
                **kwargs: typing.Any
            ) -> MessageHttpRequest: ...
            def import_(
                self,
                *,
                userId: str,
                body: Message = ...,
                neverMarkSpam: bool = ...,
                processForCalendar: bool = ...,
                deleted: bool = ...,
                internalDateSource: typing_extensions.Literal[
                    "receivedTime", "dateHeader"
                ] = ...,
                **kwargs: typing.Any
            ) -> MessageHttpRequest: ...
            def delete(
                self, *, userId: str, id: str, **kwargs: typing.Any
            ) -> googleapiclient.http.HttpRequest: ...
            def modify(
                self,
                *,
                userId: str,
                id: str,
                body: ModifyMessageRequest = ...,
                **kwargs: typing.Any
            ) -> MessageHttpRequest: ...
            def batchDelete(
                self,
                *,
                userId: str,
                body: BatchDeleteMessagesRequest = ...,
                **kwargs: typing.Any
            ) -> googleapiclient.http.HttpRequest: ...
            def get(
                self,
                *,
                userId: str,
                id: str,
                format: typing_extensions.Literal[
                    "minimal", "full", "raw", "metadata"
                ] = ...,
                metadataHeaders: typing.Union[str, typing.List[str]] = ...,
                **kwargs: typing.Any
            ) -> MessageHttpRequest: ...
            def trash(
                self, *, userId: str, id: str, **kwargs: typing.Any
            ) -> MessageHttpRequest: ...
            def batchModify(
                self,
                *,
                userId: str,
                body: BatchModifyMessagesRequest = ...,
                **kwargs: typing.Any
            ) -> googleapiclient.http.HttpRequest: ...
            def list(
                self,
                *,
                userId: str,
                includeSpamTrash: bool = ...,
                labelIds: typing.Union[str, typing.List[str]] = ...,
                q: str = ...,
                maxResults: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> ListMessagesResponseHttpRequest: ...
            def attachments(self) -> AttachmentsResource: ...
        class DraftsResource(googleapiclient.discovery.Resource):
            def delete(
                self, *, userId: str, id: str, **kwargs: typing.Any
            ) -> googleapiclient.http.HttpRequest: ...
            def list(
                self,
                *,
                userId: str,
                q: str = ...,
                includeSpamTrash: bool = ...,
                pageToken: str = ...,
                maxResults: int = ...,
                **kwargs: typing.Any
            ) -> ListDraftsResponseHttpRequest: ...
            def get(
                self,
                *,
                userId: str,
                id: str,
                format: typing_extensions.Literal[
                    "minimal", "full", "raw", "metadata"
                ] = ...,
                **kwargs: typing.Any
            ) -> DraftHttpRequest: ...
            def create(
                self, *, userId: str, body: Draft = ..., **kwargs: typing.Any
            ) -> DraftHttpRequest: ...
            def update(
                self, *, userId: str, id: str, body: Draft = ..., **kwargs: typing.Any
            ) -> DraftHttpRequest: ...
            def send(
                self, *, userId: str, body: Draft = ..., **kwargs: typing.Any
            ) -> MessageHttpRequest: ...
        class SettingsResource(googleapiclient.discovery.Resource):
            class ForwardingAddressesResource(googleapiclient.discovery.Resource):
                def list(
                    self, *, userId: str, **kwargs: typing.Any
                ) -> ListForwardingAddressesResponseHttpRequest: ...
                def create(
                    self,
                    *,
                    userId: str,
                    body: ForwardingAddress = ...,
                    **kwargs: typing.Any
                ) -> ForwardingAddressHttpRequest: ...
                def get(
                    self, *, userId: str, forwardingEmail: str, **kwargs: typing.Any
                ) -> ForwardingAddressHttpRequest: ...
                def delete(
                    self, *, userId: str, forwardingEmail: str, **kwargs: typing.Any
                ) -> googleapiclient.http.HttpRequest: ...
            class DelegatesResource(googleapiclient.discovery.Resource):
                def create(
                    self, *, userId: str, body: Delegate = ..., **kwargs: typing.Any
                ) -> DelegateHttpRequest: ...
                def delete(
                    self, *, userId: str, delegateEmail: str, **kwargs: typing.Any
                ) -> googleapiclient.http.HttpRequest: ...
                def list(
                    self, *, userId: str, **kwargs: typing.Any
                ) -> ListDelegatesResponseHttpRequest: ...
                def get(
                    self, *, userId: str, delegateEmail: str, **kwargs: typing.Any
                ) -> DelegateHttpRequest: ...
            class FiltersResource(googleapiclient.discovery.Resource):
                def get(
                    self, *, userId: str, id: str, **kwargs: typing.Any
                ) -> FilterHttpRequest: ...
                def create(
                    self, *, userId: str, body: Filter = ..., **kwargs: typing.Any
                ) -> FilterHttpRequest: ...
                def delete(
                    self, *, userId: str, id: str, **kwargs: typing.Any
                ) -> googleapiclient.http.HttpRequest: ...
                def list(
                    self, *, userId: str, **kwargs: typing.Any
                ) -> ListFiltersResponseHttpRequest: ...
            class SendAsResource(googleapiclient.discovery.Resource):
                class SmimeInfoResource(googleapiclient.discovery.Resource):
                    def list(
                        self, *, userId: str, sendAsEmail: str, **kwargs: typing.Any
                    ) -> ListSmimeInfoResponseHttpRequest: ...
                    def get(
                        self,
                        *,
                        userId: str,
                        sendAsEmail: str,
                        id: str,
                        **kwargs: typing.Any
                    ) -> SmimeInfoHttpRequest: ...
                    def delete(
                        self,
                        *,
                        userId: str,
                        sendAsEmail: str,
                        id: str,
                        **kwargs: typing.Any
                    ) -> googleapiclient.http.HttpRequest: ...
                    def insert(
                        self,
                        *,
                        userId: str,
                        sendAsEmail: str,
                        body: SmimeInfo = ...,
                        **kwargs: typing.Any
                    ) -> SmimeInfoHttpRequest: ...
                    def setDefault(
                        self,
                        *,
                        userId: str,
                        sendAsEmail: str,
                        id: str,
                        **kwargs: typing.Any
                    ) -> googleapiclient.http.HttpRequest: ...
                def create(
                    self, *, userId: str, body: SendAs = ..., **kwargs: typing.Any
                ) -> SendAsHttpRequest: ...
                def list(
                    self, *, userId: str, **kwargs: typing.Any
                ) -> ListSendAsResponseHttpRequest: ...
                def update(
                    self,
                    *,
                    userId: str,
                    sendAsEmail: str,
                    body: SendAs = ...,
                    **kwargs: typing.Any
                ) -> SendAsHttpRequest: ...
                def get(
                    self, *, userId: str, sendAsEmail: str, **kwargs: typing.Any
                ) -> SendAsHttpRequest: ...
                def verify(
                    self, *, userId: str, sendAsEmail: str, **kwargs: typing.Any
                ) -> googleapiclient.http.HttpRequest: ...
                def delete(
                    self, *, userId: str, sendAsEmail: str, **kwargs: typing.Any
                ) -> googleapiclient.http.HttpRequest: ...
                def patch(
                    self,
                    *,
                    userId: str,
                    sendAsEmail: str,
                    body: SendAs = ...,
                    **kwargs: typing.Any
                ) -> SendAsHttpRequest: ...
                def smimeInfo(self) -> SmimeInfoResource: ...
            def getPop(
                self, *, userId: str, **kwargs: typing.Any
            ) -> PopSettingsHttpRequest: ...
            def updatePop(
                self, *, userId: str, body: PopSettings = ..., **kwargs: typing.Any
            ) -> PopSettingsHttpRequest: ...
            def getAutoForwarding(
                self, *, userId: str, **kwargs: typing.Any
            ) -> AutoForwardingHttpRequest: ...
            def getVacation(
                self, *, userId: str, **kwargs: typing.Any
            ) -> VacationSettingsHttpRequest: ...
            def updateLanguage(
                self, *, userId: str, body: LanguageSettings = ..., **kwargs: typing.Any
            ) -> LanguageSettingsHttpRequest: ...
            def updateImap(
                self, *, userId: str, body: ImapSettings = ..., **kwargs: typing.Any
            ) -> ImapSettingsHttpRequest: ...
            def updateAutoForwarding(
                self, *, userId: str, body: AutoForwarding = ..., **kwargs: typing.Any
            ) -> AutoForwardingHttpRequest: ...
            def getImap(
                self, *, userId: str, **kwargs: typing.Any
            ) -> ImapSettingsHttpRequest: ...
            def updateVacation(
                self, *, userId: str, body: VacationSettings = ..., **kwargs: typing.Any
            ) -> VacationSettingsHttpRequest: ...
            def getLanguage(
                self, *, userId: str, **kwargs: typing.Any
            ) -> LanguageSettingsHttpRequest: ...
            def forwardingAddresses(self) -> ForwardingAddressesResource: ...
            def delegates(self) -> DelegatesResource: ...
            def filters(self) -> FiltersResource: ...
            def sendAs(self) -> SendAsResource: ...
        class HistoryResource(googleapiclient.discovery.Resource):
            def list(
                self,
                *,
                userId: str,
                pageToken: str = ...,
                historyTypes: typing.Union[
                    typing_extensions.Literal[
                        "messageAdded", "messageDeleted", "labelAdded", "labelRemoved"
                    ],
                    typing.List[
                        typing_extensions.Literal[
                            "messageAdded",
                            "messageDeleted",
                            "labelAdded",
                            "labelRemoved",
                        ]
                    ],
                ] = ...,
                labelId: str = ...,
                maxResults: int = ...,
                startHistoryId: str = ...,
                **kwargs: typing.Any
            ) -> ListHistoryResponseHttpRequest: ...
        class ThreadsResource(googleapiclient.discovery.Resource):
            def modify(
                self,
                *,
                userId: str,
                id: str,
                body: ModifyThreadRequest = ...,
                **kwargs: typing.Any
            ) -> ThreadHttpRequest: ...
            def untrash(
                self, *, userId: str, id: str, **kwargs: typing.Any
            ) -> ThreadHttpRequest: ...
            def get(
                self,
                *,
                userId: str,
                id: str,
                metadataHeaders: typing.Union[str, typing.List[str]] = ...,
                format: typing_extensions.Literal["full", "metadata", "minimal"] = ...,
                **kwargs: typing.Any
            ) -> ThreadHttpRequest: ...
            def trash(
                self, *, userId: str, id: str, **kwargs: typing.Any
            ) -> ThreadHttpRequest: ...
            def list(
                self,
                *,
                userId: str,
                labelIds: typing.Union[str, typing.List[str]] = ...,
                maxResults: int = ...,
                includeSpamTrash: bool = ...,
                q: str = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> ListThreadsResponseHttpRequest: ...
            def delete(
                self, *, userId: str, id: str, **kwargs: typing.Any
            ) -> googleapiclient.http.HttpRequest: ...
        class LabelsResource(googleapiclient.discovery.Resource):
            def get(
                self, *, userId: str, id: str, **kwargs: typing.Any
            ) -> LabelHttpRequest: ...
            def patch(
                self, *, userId: str, id: str, body: Label = ..., **kwargs: typing.Any
            ) -> LabelHttpRequest: ...
            def create(
                self, *, userId: str, body: Label = ..., **kwargs: typing.Any
            ) -> LabelHttpRequest: ...
            def delete(
                self, *, userId: str, id: str, **kwargs: typing.Any
            ) -> googleapiclient.http.HttpRequest: ...
            def update(
                self, *, userId: str, id: str, body: Label = ..., **kwargs: typing.Any
            ) -> LabelHttpRequest: ...
            def list(
                self, *, userId: str, **kwargs: typing.Any
            ) -> ListLabelsResponseHttpRequest: ...
        def watch(
            self, *, userId: str, body: WatchRequest = ..., **kwargs: typing.Any
        ) -> WatchResponseHttpRequest: ...
        def getProfile(
            self, *, userId: str, **kwargs: typing.Any
        ) -> ProfileHttpRequest: ...
        def stop(
            self, *, userId: str, **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def messages(self) -> MessagesResource: ...
        def drafts(self) -> DraftsResource: ...
        def settings(self) -> SettingsResource: ...
        def history(self) -> HistoryResource: ...
        def threads(self) -> ThreadsResource: ...
        def labels(self) -> LabelsResource: ...
    def users(self) -> UsersResource: ...

class DelegateHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Delegate: ...

class ImapSettingsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ImapSettings: ...

class LanguageSettingsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> LanguageSettings: ...

class VacationSettingsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> VacationSettings: ...

class MessagePartBodyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> MessagePartBody: ...

class ListHistoryResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListHistoryResponse: ...

class AutoForwardingHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> AutoForwarding: ...

class ListDelegatesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListDelegatesResponse: ...

class PopSettingsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> PopSettings: ...

class ListLabelsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListLabelsResponse: ...

class MessageHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Message: ...

class LabelHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Label: ...

class ListSmimeInfoResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListSmimeInfoResponse: ...

class ListSendAsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListSendAsResponse: ...

class FilterHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Filter: ...

class ThreadHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Thread: ...

class ProfileHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Profile: ...

class ListThreadsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListThreadsResponse: ...

class ListFiltersResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListFiltersResponse: ...

class ListDraftsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListDraftsResponse: ...

class SmimeInfoHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> SmimeInfo: ...

class WatchResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> WatchResponse: ...

class ListMessagesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListMessagesResponse: ...

class ForwardingAddressHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ForwardingAddress: ...

class DraftHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Draft: ...

class SendAsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> SendAs: ...

class ListForwardingAddressesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListForwardingAddressesResponse: ...
