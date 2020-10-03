import typing

import typing_extensions

class PushConfig(typing_extensions.TypedDict, total=False):
    pushEndpoint: str

class ModifyPushConfigRequest(typing_extensions.TypedDict, total=False):
    pushConfig: PushConfig
    subscription: str

class AcknowledgeRequest(typing_extensions.TypedDict, total=False):
    subscription: str
    ackId: typing.List[str]

class PubsubEvent(typing_extensions.TypedDict, total=False):
    message: PubsubMessage
    truncated: bool
    subscription: str
    deleted: bool

class Empty(typing_extensions.TypedDict, total=False): ...

class ListSubscriptionsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    subscription: typing.List[Subscription]

class PublishBatchResponse(typing_extensions.TypedDict, total=False):
    messageIds: typing.List[str]

class ListTopicsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    topic: typing.List[Topic]

class Topic(typing_extensions.TypedDict, total=False):
    name: str

class ModifyAckDeadlineRequest(typing_extensions.TypedDict, total=False):
    ackId: str
    ackIds: typing.List[str]
    ackDeadlineSeconds: int
    subscription: str

class PubsubMessage(typing_extensions.TypedDict, total=False):
    data: str
    publishTime: str
    label: typing.List[Label]
    messageId: str

class PublishBatchRequest(typing_extensions.TypedDict, total=False):
    topic: str
    messages: typing.List[PubsubMessage]

class PullBatchResponse(typing_extensions.TypedDict, total=False):
    pullResponses: typing.List[PullResponse]

class PullBatchRequest(typing_extensions.TypedDict, total=False):
    maxEvents: int
    returnImmediately: bool
    subscription: str

class PullResponse(typing_extensions.TypedDict, total=False):
    pubsubEvent: PubsubEvent
    ackId: str

class PullRequest(typing_extensions.TypedDict, total=False):
    subscription: str
    returnImmediately: bool

class Label(typing_extensions.TypedDict, total=False):
    numValue: str
    strValue: str
    key: str

class Subscription(typing_extensions.TypedDict, total=False):
    pushConfig: PushConfig
    name: str
    ackDeadlineSeconds: int
    topic: str

class PublishRequest(typing_extensions.TypedDict, total=False):
    topic: str
    message: PubsubMessage
