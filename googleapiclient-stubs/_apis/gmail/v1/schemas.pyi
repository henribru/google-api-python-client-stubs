import typing

import typing_extensions

_list = list

@typing.type_check_only
class AutoForwarding(typing_extensions.TypedDict, total=False):
    disposition: typing_extensions.Literal[
        "dispositionUnspecified", "leaveInInbox", "archive", "trash", "markRead"
    ]
    emailAddress: str
    enabled: bool

@typing.type_check_only
class BatchDeleteMessagesRequest(typing_extensions.TypedDict, total=False):
    ids: _list[str]

@typing.type_check_only
class BatchModifyMessagesRequest(typing_extensions.TypedDict, total=False):
    addLabelIds: _list[str]
    ids: _list[str]
    removeLabelIds: _list[str]

@typing.type_check_only
class CseIdentity(typing_extensions.TypedDict, total=False):
    emailAddress: str
    primaryKeyPairId: str

@typing.type_check_only
class CseKeyPair(typing_extensions.TypedDict, total=False):
    disableTime: str
    enablementState: typing_extensions.Literal[
        "stateUnspecified", "enabled", "disabled"
    ]
    keyPairId: str
    pem: str
    pkcs7: str
    privateKeyMetadata: _list[CsePrivateKeyMetadata]
    subjectEmailAddresses: _list[str]

@typing.type_check_only
class CsePrivateKeyMetadata(typing_extensions.TypedDict, total=False):
    kaclsKeyMetadata: KaclsKeyMetadata
    privateKeyMetadataId: str

@typing.type_check_only
class Delegate(typing_extensions.TypedDict, total=False):
    delegateEmail: str
    verificationStatus: typing_extensions.Literal[
        "verificationStatusUnspecified", "accepted", "pending", "rejected", "expired"
    ]

@typing.type_check_only
class DisableCseKeyPairRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Draft(typing_extensions.TypedDict, total=False):
    id: str
    message: Message

@typing.type_check_only
class EnableCseKeyPairRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Filter(typing_extensions.TypedDict, total=False):
    action: FilterAction
    criteria: FilterCriteria
    id: str

@typing.type_check_only
class FilterAction(typing_extensions.TypedDict, total=False):
    addLabelIds: _list[str]
    forward: str
    removeLabelIds: _list[str]

AlternativeFilterCriteria = typing_extensions.TypedDict(
    "AlternativeFilterCriteria",
    {
        "excludeChats": bool,
        "from": str,
        "hasAttachment": bool,
        "negatedQuery": str,
        "query": str,
        "size": int,
        "sizeComparison": typing_extensions.Literal["unspecified", "smaller", "larger"],
        "subject": str,
        "to": str,
    },
    total=False,
)

@typing.type_check_only
class FilterCriteria(AlternativeFilterCriteria): ...

@typing.type_check_only
class ForwardingAddress(typing_extensions.TypedDict, total=False):
    forwardingEmail: str
    verificationStatus: typing_extensions.Literal[
        "verificationStatusUnspecified", "accepted", "pending"
    ]

@typing.type_check_only
class History(typing_extensions.TypedDict, total=False):
    id: str
    labelsAdded: _list[HistoryLabelAdded]
    labelsRemoved: _list[HistoryLabelRemoved]
    messages: _list[Message]
    messagesAdded: _list[HistoryMessageAdded]
    messagesDeleted: _list[HistoryMessageDeleted]

@typing.type_check_only
class HistoryLabelAdded(typing_extensions.TypedDict, total=False):
    labelIds: _list[str]
    message: Message

@typing.type_check_only
class HistoryLabelRemoved(typing_extensions.TypedDict, total=False):
    labelIds: _list[str]
    message: Message

@typing.type_check_only
class HistoryMessageAdded(typing_extensions.TypedDict, total=False):
    message: Message

@typing.type_check_only
class HistoryMessageDeleted(typing_extensions.TypedDict, total=False):
    message: Message

@typing.type_check_only
class ImapSettings(typing_extensions.TypedDict, total=False):
    autoExpunge: bool
    enabled: bool
    expungeBehavior: typing_extensions.Literal[
        "expungeBehaviorUnspecified", "archive", "trash", "deleteForever"
    ]
    maxFolderSize: int

@typing.type_check_only
class KaclsKeyMetadata(typing_extensions.TypedDict, total=False):
    kaclsData: str
    kaclsUri: str

@typing.type_check_only
class Label(typing_extensions.TypedDict, total=False):
    color: LabelColor
    id: str
    labelListVisibility: typing_extensions.Literal[
        "labelShow", "labelShowIfUnread", "labelHide"
    ]
    messageListVisibility: typing_extensions.Literal["show", "hide"]
    messagesTotal: int
    messagesUnread: int
    name: str
    threadsTotal: int
    threadsUnread: int
    type: typing_extensions.Literal["system", "user"]

@typing.type_check_only
class LabelColor(typing_extensions.TypedDict, total=False):
    backgroundColor: str
    textColor: str

@typing.type_check_only
class LanguageSettings(typing_extensions.TypedDict, total=False):
    displayLanguage: str

@typing.type_check_only
class ListCseIdentitiesResponse(typing_extensions.TypedDict, total=False):
    cseIdentities: _list[CseIdentity]
    nextPageToken: str

@typing.type_check_only
class ListCseKeyPairsResponse(typing_extensions.TypedDict, total=False):
    cseKeyPairs: _list[CseKeyPair]
    nextPageToken: str

@typing.type_check_only
class ListDelegatesResponse(typing_extensions.TypedDict, total=False):
    delegates: _list[Delegate]

@typing.type_check_only
class ListDraftsResponse(typing_extensions.TypedDict, total=False):
    drafts: _list[Draft]
    nextPageToken: str
    resultSizeEstimate: int

@typing.type_check_only
class ListFiltersResponse(typing_extensions.TypedDict, total=False):
    filter: _list[Filter]

@typing.type_check_only
class ListForwardingAddressesResponse(typing_extensions.TypedDict, total=False):
    forwardingAddresses: _list[ForwardingAddress]

@typing.type_check_only
class ListHistoryResponse(typing_extensions.TypedDict, total=False):
    history: _list[History]
    historyId: str
    nextPageToken: str

@typing.type_check_only
class ListLabelsResponse(typing_extensions.TypedDict, total=False):
    labels: _list[Label]

@typing.type_check_only
class ListMessagesResponse(typing_extensions.TypedDict, total=False):
    messages: _list[Message]
    nextPageToken: str
    resultSizeEstimate: int

@typing.type_check_only
class ListSendAsResponse(typing_extensions.TypedDict, total=False):
    sendAs: _list[SendAs]

@typing.type_check_only
class ListSmimeInfoResponse(typing_extensions.TypedDict, total=False):
    smimeInfo: _list[SmimeInfo]

@typing.type_check_only
class ListThreadsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    resultSizeEstimate: int
    threads: _list[Thread]

@typing.type_check_only
class Message(typing_extensions.TypedDict, total=False):
    historyId: str
    id: str
    internalDate: str
    labelIds: _list[str]
    payload: MessagePart
    raw: str
    sizeEstimate: int
    snippet: str
    threadId: str

@typing.type_check_only
class MessagePart(typing_extensions.TypedDict, total=False):
    body: MessagePartBody
    filename: str
    headers: _list[MessagePartHeader]
    mimeType: str
    partId: str
    parts: _list[MessagePart]

@typing.type_check_only
class MessagePartBody(typing_extensions.TypedDict, total=False):
    attachmentId: str
    data: str
    size: int

@typing.type_check_only
class MessagePartHeader(typing_extensions.TypedDict, total=False):
    name: str
    value: str

@typing.type_check_only
class ModifyMessageRequest(typing_extensions.TypedDict, total=False):
    addLabelIds: _list[str]
    removeLabelIds: _list[str]

@typing.type_check_only
class ModifyThreadRequest(typing_extensions.TypedDict, total=False):
    addLabelIds: _list[str]
    removeLabelIds: _list[str]

@typing.type_check_only
class ObliterateCseKeyPairRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class PopSettings(typing_extensions.TypedDict, total=False):
    accessWindow: typing_extensions.Literal[
        "accessWindowUnspecified", "disabled", "fromNowOn", "allMail"
    ]
    disposition: typing_extensions.Literal[
        "dispositionUnspecified", "leaveInInbox", "archive", "trash", "markRead"
    ]

@typing.type_check_only
class Profile(typing_extensions.TypedDict, total=False):
    emailAddress: str
    historyId: str
    messagesTotal: int
    threadsTotal: int

@typing.type_check_only
class SendAs(typing_extensions.TypedDict, total=False):
    displayName: str
    isDefault: bool
    isPrimary: bool
    replyToAddress: str
    sendAsEmail: str
    signature: str
    smtpMsa: SmtpMsa
    treatAsAlias: bool
    verificationStatus: typing_extensions.Literal[
        "verificationStatusUnspecified", "accepted", "pending"
    ]

@typing.type_check_only
class SmimeInfo(typing_extensions.TypedDict, total=False):
    encryptedKeyPassword: str
    expiration: str
    id: str
    isDefault: bool
    issuerCn: str
    pem: str
    pkcs12: str

@typing.type_check_only
class SmtpMsa(typing_extensions.TypedDict, total=False):
    host: str
    password: str
    port: int
    securityMode: typing_extensions.Literal[
        "securityModeUnspecified", "none", "ssl", "starttls"
    ]
    username: str

@typing.type_check_only
class Thread(typing_extensions.TypedDict, total=False):
    historyId: str
    id: str
    messages: _list[Message]
    snippet: str

@typing.type_check_only
class VacationSettings(typing_extensions.TypedDict, total=False):
    enableAutoReply: bool
    endTime: str
    responseBodyHtml: str
    responseBodyPlainText: str
    responseSubject: str
    restrictToContacts: bool
    restrictToDomain: bool
    startTime: str

@typing.type_check_only
class WatchRequest(typing_extensions.TypedDict, total=False):
    labelFilterAction: typing_extensions.Literal["include", "exclude"]
    labelIds: _list[str]
    topicName: str

@typing.type_check_only
class WatchResponse(typing_extensions.TypedDict, total=False):
    expiration: str
    historyId: str
