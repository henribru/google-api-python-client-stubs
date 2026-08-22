import typing

_list = list

@typing.type_check_only
class AcknowledgeRequest(typing.TypedDict, total=False):
    ackId: _list[str]
    subscription: str

@typing.type_check_only
class Empty(typing.TypedDict, total=False): ...

@typing.type_check_only
class Label(typing.TypedDict, total=False):
    key: str
    numValue: str
    strValue: str

@typing.type_check_only
class ListSubscriptionsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    subscription: _list[Subscription]

@typing.type_check_only
class ListTopicsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    topic: _list[Topic]

@typing.type_check_only
class ModifyAckDeadlineRequest(typing.TypedDict, total=False):
    ackDeadlineSeconds: int
    ackId: str
    ackIds: _list[str]
    subscription: str

@typing.type_check_only
class ModifyPushConfigRequest(typing.TypedDict, total=False):
    pushConfig: PushConfig
    subscription: str

@typing.type_check_only
class PublishBatchRequest(typing.TypedDict, total=False):
    messages: _list[PubsubMessage]
    topic: str

@typing.type_check_only
class PublishBatchResponse(typing.TypedDict, total=False):
    messageIds: _list[str]

@typing.type_check_only
class PublishRequest(typing.TypedDict, total=False):
    message: PubsubMessage
    topic: str

@typing.type_check_only
class PubsubEvent(typing.TypedDict, total=False):
    deleted: bool
    message: PubsubMessage
    subscription: str
    truncated: bool

@typing.type_check_only
class PubsubMessage(typing.TypedDict, total=False):
    data: str
    label: _list[Label]
    messageId: str
    publishTime: str

@typing.type_check_only
class PullBatchRequest(typing.TypedDict, total=False):
    maxEvents: int
    returnImmediately: bool
    subscription: str

@typing.type_check_only
class PullBatchResponse(typing.TypedDict, total=False):
    pullResponses: _list[PullResponse]

@typing.type_check_only
class PullRequest(typing.TypedDict, total=False):
    returnImmediately: bool
    subscription: str

@typing.type_check_only
class PullResponse(typing.TypedDict, total=False):
    ackId: str
    pubsubEvent: PubsubEvent

@typing.type_check_only
class PushConfig(typing.TypedDict, total=False):
    pushEndpoint: str

@typing.type_check_only
class Subscription(typing.TypedDict, total=False):
    ackDeadlineSeconds: int
    name: str
    pushConfig: PushConfig
    topic: str

@typing.type_check_only
class Topic(typing.TypedDict, total=False):
    name: str
