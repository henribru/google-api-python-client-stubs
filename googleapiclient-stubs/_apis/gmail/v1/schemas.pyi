import typing

import typing_extensions

class MessagePart(typing.Dict[str, typing.Any]): ...

class SmtpMsa(typing_extensions.TypedDict, total=False):
    username: str
    password: str
    securityMode: typing_extensions.Literal[
        "securityModeUnspecified", "none", "ssl", "starttls"
    ]
    host: str
    port: int

class ImapSettings(typing_extensions.TypedDict, total=False):
    enabled: bool
    maxFolderSize: int
    autoExpunge: bool
    expungeBehavior: typing_extensions.Literal[
        "expungeBehaviorUnspecified", "archive", "trash", "deleteForever"
    ]

class MessagePartHeader(typing_extensions.TypedDict, total=False):
    name: str
    value: str

class ModifyThreadRequest(typing_extensions.TypedDict, total=False):
    addLabelIds: typing.List[str]
    removeLabelIds: typing.List[str]

class MessagePartBody(typing_extensions.TypedDict, total=False):
    data: str
    size: int
    attachmentId: str

class HistoryMessageAdded(typing_extensions.TypedDict, total=False):
    message: Message

class SendAs(typing_extensions.TypedDict, total=False):
    replyToAddress: str
    signature: str
    smtpMsa: SmtpMsa
    isDefault: bool
    sendAsEmail: str
    displayName: str
    isPrimary: bool
    treatAsAlias: bool
    verificationStatus: typing_extensions.Literal[
        "verificationStatusUnspecified", "accepted", "pending"
    ]

class ListForwardingAddressesResponse(typing_extensions.TypedDict, total=False):
    forwardingAddresses: typing.List[ForwardingAddress]

class Draft(typing_extensions.TypedDict, total=False):
    id: str
    message: Message

class HistoryLabelAdded(typing_extensions.TypedDict, total=False):
    labelIds: typing.List[str]
    message: Message

class ListDraftsResponse(typing_extensions.TypedDict, total=False):
    resultSizeEstimate: int
    nextPageToken: str
    drafts: typing.List[Draft]

class Label(typing_extensions.TypedDict, total=False):
    threadsTotal: int
    messagesTotal: int
    messageListVisibility: typing_extensions.Literal["show", "hide"]
    id: str
    type: typing_extensions.Literal["system", "user"]
    name: str
    color: LabelColor
    labelListVisibility: typing_extensions.Literal[
        "labelShow", "labelShowIfUnread", "labelHide"
    ]
    messagesUnread: int
    threadsUnread: int

class Message(typing.Dict[str, typing.Any]): ...

class ListThreadsResponse(typing_extensions.TypedDict, total=False):
    resultSizeEstimate: int
    nextPageToken: str
    threads: typing.List[Thread]

class Delegate(typing_extensions.TypedDict, total=False):
    verificationStatus: typing_extensions.Literal[
        "verificationStatusUnspecified", "accepted", "pending", "rejected", "expired"
    ]
    delegateEmail: str

class SmimeInfo(typing_extensions.TypedDict, total=False):
    id: str
    encryptedKeyPassword: str
    expiration: str
    issuerCn: str
    pkcs12: str
    isDefault: bool
    pem: str

class VacationSettings(typing_extensions.TypedDict, total=False):
    startTime: str
    endTime: str
    restrictToContacts: bool
    responseBodyPlainText: str
    responseSubject: str
    responseBodyHtml: str
    restrictToDomain: bool
    enableAutoReply: bool

class Filter(typing_extensions.TypedDict, total=False):
    criteria: FilterCriteria
    id: str
    action: FilterAction

class AutoForwarding(typing_extensions.TypedDict, total=False):
    enabled: bool
    disposition: typing_extensions.Literal[
        "dispositionUnspecified", "leaveInInbox", "archive", "trash", "markRead"
    ]
    emailAddress: str

class BatchModifyMessagesRequest(typing_extensions.TypedDict, total=False):
    addLabelIds: typing.List[str]
    removeLabelIds: typing.List[str]
    ids: typing.List[str]

class BatchDeleteMessagesRequest(typing_extensions.TypedDict, total=False):
    ids: typing.List[str]

class ListSmimeInfoResponse(typing_extensions.TypedDict, total=False):
    smimeInfo: typing.List[SmimeInfo]

FilterCriteria = typing_extensions.TypedDict(
    "FilterCriteria",
    {
        "from": str,
        "excludeChats": bool,
        "size": int,
        "hasAttachment": bool,
        "query": str,
        "subject": str,
        "to": str,
        "sizeComparison": typing_extensions.Literal["unspecified", "smaller", "larger"],
        "negatedQuery": str,
    },
    total=False,
)

class History(typing_extensions.TypedDict, total=False):
    id: str
    messagesDeleted: typing.List[HistoryMessageDeleted]
    labelsAdded: typing.List[HistoryLabelAdded]
    messagesAdded: typing.List[HistoryMessageAdded]
    messages: typing.List[Message]
    labelsRemoved: typing.List[HistoryLabelRemoved]

class FilterAction(typing_extensions.TypedDict, total=False):
    removeLabelIds: typing.List[str]
    forward: str
    addLabelIds: typing.List[str]

class ListDelegatesResponse(typing_extensions.TypedDict, total=False):
    delegates: typing.List[Delegate]

class ForwardingAddress(typing_extensions.TypedDict, total=False):
    forwardingEmail: str
    verificationStatus: typing_extensions.Literal[
        "verificationStatusUnspecified", "accepted", "pending"
    ]

class Thread(typing.Dict[str, typing.Any]): ...

class ListLabelsResponse(typing_extensions.TypedDict, total=False):
    labels: typing.List[Label]

class HistoryLabelRemoved(typing.Dict[str, typing.Any]): ...

class WatchRequest(typing_extensions.TypedDict, total=False):
    topicName: str
    labelFilterAction: typing_extensions.Literal["include", "exclude"]
    labelIds: typing.List[str]

class ListFiltersResponse(typing_extensions.TypedDict, total=False):
    filter: typing.List[Filter]

class ModifyMessageRequest(typing_extensions.TypedDict, total=False):
    removeLabelIds: typing.List[str]
    addLabelIds: typing.List[str]

class WatchResponse(typing_extensions.TypedDict, total=False):
    expiration: str
    historyId: str

class Profile(typing_extensions.TypedDict, total=False):
    threadsTotal: int
    messagesTotal: int
    emailAddress: str
    historyId: str

class LanguageSettings(typing_extensions.TypedDict, total=False):
    displayLanguage: str

class HistoryMessageDeleted(typing.Dict[str, typing.Any]): ...

class ListSendAsResponse(typing_extensions.TypedDict, total=False):
    sendAs: typing.List[SendAs]

class ListMessagesResponse(typing_extensions.TypedDict, total=False):
    messages: typing.List[Message]
    nextPageToken: str
    resultSizeEstimate: int

class LabelColor(typing_extensions.TypedDict, total=False):
    textColor: str
    backgroundColor: str

class PopSettings(typing_extensions.TypedDict, total=False):
    disposition: typing_extensions.Literal[
        "dispositionUnspecified", "leaveInInbox", "archive", "trash", "markRead"
    ]
    accessWindow: typing_extensions.Literal[
        "accessWindowUnspecified", "disabled", "fromNowOn", "allMail"
    ]

class ListHistoryResponse(typing_extensions.TypedDict, total=False):
    history: typing.List[History]
    nextPageToken: str
    historyId: str
