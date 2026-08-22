import typing

_list = list

@typing.type_check_only
class AutoForwarding(typing.TypedDict, total=False):
    disposition: typing.Literal[
        "dispositionUnspecified", "leaveInInbox", "archive", "trash", "markRead"
    ]
    emailAddress: str
    enabled: bool

@typing.type_check_only
class BatchDeleteMessagesRequest(typing.TypedDict, total=False):
    ids: _list[str]

@typing.type_check_only
class BatchModifyMessagesRequest(typing.TypedDict, total=False):
    addClassificationLabels: _list[ClassificationLabelValue]
    addLabelIds: _list[str]
    ids: _list[str]
    removeClassificationLabelIds: _list[str]
    removeLabelIds: _list[str]

@typing.type_check_only
class ClassificationLabelFieldValue(typing.TypedDict, total=False):
    fieldId: str
    selection: str

@typing.type_check_only
class ClassificationLabelValue(typing.TypedDict, total=False):
    fields: _list[ClassificationLabelFieldValue]
    labelId: str

@typing.type_check_only
class CseIdentity(typing.TypedDict, total=False):
    emailAddress: str
    primaryKeyPairId: str
    signAndEncryptKeyPairs: SignAndEncryptKeyPairs

@typing.type_check_only
class CseKeyPair(typing.TypedDict, total=False):
    disableTime: str
    enablementState: typing.Literal["stateUnspecified", "enabled", "disabled"]
    keyPairId: str
    pem: str
    pkcs7: str
    privateKeyMetadata: _list[CsePrivateKeyMetadata]
    subjectEmailAddresses: _list[str]

@typing.type_check_only
class CsePrivateKeyMetadata(typing.TypedDict, total=False):
    hardwareKeyMetadata: HardwareKeyMetadata
    kaclsKeyMetadata: KaclsKeyMetadata
    privateKeyMetadataId: str

@typing.type_check_only
class Delegate(typing.TypedDict, total=False):
    delegateEmail: str
    verificationStatus: typing.Literal[
        "verificationStatusUnspecified", "accepted", "pending", "rejected", "expired"
    ]

@typing.type_check_only
class DisableCseKeyPairRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class Draft(typing.TypedDict, total=False):
    id: str
    message: Message

@typing.type_check_only
class EnableCseKeyPairRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class Filter(typing.TypedDict, total=False):
    action: FilterAction
    criteria: FilterCriteria
    id: str

@typing.type_check_only
class FilterAction(typing.TypedDict, total=False):
    addLabelIds: _list[str]
    forward: str
    removeLabelIds: _list[str]

AlternativeFilterCriteria = typing.TypedDict(
    "AlternativeFilterCriteria",
    {
        "excludeChats": bool,
        "from": str,
        "hasAttachment": bool,
        "negatedQuery": str,
        "query": str,
        "size": int,
        "sizeComparison": typing.Literal["unspecified", "smaller", "larger"],
        "subject": str,
        "to": str,
    },
    total=False,
)

@typing.type_check_only
class FilterCriteria(AlternativeFilterCriteria): ...

@typing.type_check_only
class ForwardingAddress(typing.TypedDict, total=False):
    forwardingEmail: str
    verificationStatus: typing.Literal[
        "verificationStatusUnspecified", "accepted", "pending"
    ]

@typing.type_check_only
class HardwareKeyMetadata(typing.TypedDict, total=False):
    description: str

@typing.type_check_only
class History(typing.TypedDict, total=False):
    id: str
    labelsAdded: _list[HistoryLabelAdded]
    labelsRemoved: _list[HistoryLabelRemoved]
    messages: _list[Message]
    messagesAdded: _list[HistoryMessageAdded]
    messagesDeleted: _list[HistoryMessageDeleted]

@typing.type_check_only
class HistoryLabelAdded(typing.TypedDict, total=False):
    labelIds: _list[str]
    message: Message

@typing.type_check_only
class HistoryLabelRemoved(typing.TypedDict, total=False):
    labelIds: _list[str]
    message: Message

@typing.type_check_only
class HistoryMessageAdded(typing.TypedDict, total=False):
    message: Message

@typing.type_check_only
class HistoryMessageDeleted(typing.TypedDict, total=False):
    message: Message

@typing.type_check_only
class ImapSettings(typing.TypedDict, total=False):
    autoExpunge: bool
    enabled: bool
    expungeBehavior: typing.Literal[
        "expungeBehaviorUnspecified", "archive", "trash", "deleteForever"
    ]
    maxFolderSize: int

@typing.type_check_only
class KaclsKeyMetadata(typing.TypedDict, total=False):
    kaclsData: str
    kaclsUri: str

@typing.type_check_only
class Label(typing.TypedDict, total=False):
    color: LabelColor
    id: str
    labelListVisibility: typing.Literal["labelShow", "labelShowIfUnread", "labelHide"]
    messageListVisibility: typing.Literal["show", "hide"]
    messagesTotal: int
    messagesUnread: int
    name: str
    threadsTotal: int
    threadsUnread: int
    type: typing.Literal["system", "user"]

@typing.type_check_only
class LabelColor(typing.TypedDict, total=False):
    backgroundColor: str
    textColor: str

@typing.type_check_only
class LanguageSettings(typing.TypedDict, total=False):
    displayLanguage: str

@typing.type_check_only
class ListCseIdentitiesResponse(typing.TypedDict, total=False):
    cseIdentities: _list[CseIdentity]
    nextPageToken: str

@typing.type_check_only
class ListCseKeyPairsResponse(typing.TypedDict, total=False):
    cseKeyPairs: _list[CseKeyPair]
    nextPageToken: str

@typing.type_check_only
class ListDelegatesResponse(typing.TypedDict, total=False):
    delegates: _list[Delegate]

@typing.type_check_only
class ListDraftsResponse(typing.TypedDict, total=False):
    drafts: _list[Draft]
    nextPageToken: str
    resultSizeEstimate: int

@typing.type_check_only
class ListFiltersResponse(typing.TypedDict, total=False):
    filter: _list[Filter]

@typing.type_check_only
class ListForwardingAddressesResponse(typing.TypedDict, total=False):
    forwardingAddresses: _list[ForwardingAddress]

@typing.type_check_only
class ListHistoryResponse(typing.TypedDict, total=False):
    history: _list[History]
    historyId: str
    nextPageToken: str

@typing.type_check_only
class ListLabelsResponse(typing.TypedDict, total=False):
    labels: _list[Label]

@typing.type_check_only
class ListMessagesResponse(typing.TypedDict, total=False):
    messages: _list[Message]
    nextPageToken: str
    resultSizeEstimate: int

@typing.type_check_only
class ListSendAsResponse(typing.TypedDict, total=False):
    sendAs: _list[SendAs]

@typing.type_check_only
class ListSmimeInfoResponse(typing.TypedDict, total=False):
    smimeInfo: _list[SmimeInfo]

@typing.type_check_only
class ListThreadsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    resultSizeEstimate: int
    threads: _list[Thread]

@typing.type_check_only
class Message(typing.TypedDict, total=False):
    classificationLabelValues: _list[ClassificationLabelValue]
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
class MessagePart(typing.TypedDict, total=False):
    body: MessagePartBody
    filename: str
    headers: _list[MessagePartHeader]
    mimeType: str
    partId: str
    parts: _list[MessagePart]

@typing.type_check_only
class MessagePartBody(typing.TypedDict, total=False):
    attachmentId: str
    data: str
    size: int

@typing.type_check_only
class MessagePartHeader(typing.TypedDict, total=False):
    name: str
    value: str

@typing.type_check_only
class ModifyMessageRequest(typing.TypedDict, total=False):
    addClassificationLabels: _list[ClassificationLabelValue]
    addLabelIds: _list[str]
    removeClassificationLabelIds: _list[str]
    removeLabelIds: _list[str]

@typing.type_check_only
class ModifyThreadRequest(typing.TypedDict, total=False):
    addLabelIds: _list[str]
    removeLabelIds: _list[str]

@typing.type_check_only
class ObliterateCseKeyPairRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class PopSettings(typing.TypedDict, total=False):
    accessWindow: typing.Literal[
        "accessWindowUnspecified", "disabled", "fromNowOn", "allMail"
    ]
    disposition: typing.Literal[
        "dispositionUnspecified", "leaveInInbox", "archive", "trash", "markRead"
    ]

@typing.type_check_only
class Profile(typing.TypedDict, total=False):
    emailAddress: str
    historyId: str
    messagesTotal: int
    threadsTotal: int

@typing.type_check_only
class SendAs(typing.TypedDict, total=False):
    displayName: str
    isDefault: bool
    isPrimary: bool
    replyToAddress: str
    sendAsEmail: str
    signature: str
    smtpMsa: SmtpMsa
    treatAsAlias: bool
    verificationStatus: typing.Literal[
        "verificationStatusUnspecified", "accepted", "pending"
    ]

@typing.type_check_only
class SignAndEncryptKeyPairs(typing.TypedDict, total=False):
    encryptionKeyPairId: str
    signingKeyPairId: str

@typing.type_check_only
class SmimeInfo(typing.TypedDict, total=False):
    encryptedKeyPassword: str
    expiration: str
    id: str
    isDefault: bool
    issuerCn: str
    pem: str
    pkcs12: str

@typing.type_check_only
class SmtpMsa(typing.TypedDict, total=False):
    host: str
    password: str
    port: int
    securityMode: typing.Literal["securityModeUnspecified", "none", "ssl", "starttls"]
    username: str

@typing.type_check_only
class Thread(typing.TypedDict, total=False):
    historyId: str
    id: str
    messages: _list[Message]
    snippet: str

@typing.type_check_only
class VacationSettings(typing.TypedDict, total=False):
    enableAutoReply: bool
    endTime: str
    responseBodyHtml: str
    responseBodyPlainText: str
    responseSubject: str
    restrictToContacts: bool
    restrictToDomain: bool
    startTime: str

@typing.type_check_only
class WatchRequest(typing.TypedDict, total=False):
    labelFilterAction: typing.Literal["include", "exclude"]
    labelFilterBehavior: typing.Literal["include", "exclude"]
    labelIds: _list[str]
    topicName: str

@typing.type_check_only
class WatchResponse(typing.TypedDict, total=False):
    expiration: str
    historyId: str
