import typing

import typing_extensions

class ListTopicSubscriptionsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    subscriptions: typing.List[str]

class ListTopicsResponse(typing_extensions.TypedDict, total=False):
    topics: typing.List[Topic]
    nextPageToken: str

class PublishRequest(typing_extensions.TypedDict, total=False):
    messages: typing.List[PubsubMessage]

class AcknowledgeRequest(typing_extensions.TypedDict, total=False):
    ackIds: typing.List[str]

class Topic(typing_extensions.TypedDict, total=False):
    name: str

class ModifyAckDeadlineRequest(typing_extensions.TypedDict, total=False):
    ackId: str
    ackDeadlineSeconds: int
    ackIds: typing.List[str]

class PublishResponse(typing_extensions.TypedDict, total=False):
    messageIds: typing.List[str]

class PullResponse(typing_extensions.TypedDict, total=False):
    receivedMessages: typing.List[ReceivedMessage]

class ListSubscriptionsResponse(typing_extensions.TypedDict, total=False):
    subscriptions: typing.List[Subscription]
    nextPageToken: str

class PushConfig(typing_extensions.TypedDict, total=False):
    oidcToken: OidcToken
    attributes: typing.Dict[str, typing.Any]
    pushEndpoint: str

class PubsubMessage(typing_extensions.TypedDict, total=False):
    data: str
    publishTime: str
    messageId: str
    attributes: typing.Dict[str, typing.Any]

class Binding(typing_extensions.TypedDict, total=False):
    role: str
    members: typing.List[str]
    bindingId: str
    condition: Expr

class Policy(typing_extensions.TypedDict, total=False):
    etag: str
    bindings: typing.List[Binding]
    version: int

class PullRequest(typing_extensions.TypedDict, total=False):
    maxMessages: int
    returnImmediately: bool

class SetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    policy: Policy

class TestIamPermissionsRequest(typing_extensions.TypedDict, total=False):
    permissions: typing.List[str]

class ModifyPushConfigRequest(typing_extensions.TypedDict, total=False):
    pushConfig: PushConfig

class Subscription(typing_extensions.TypedDict, total=False):
    name: str
    pushConfig: PushConfig
    ackDeadlineSeconds: int
    topic: str

class TestIamPermissionsResponse(typing_extensions.TypedDict, total=False):
    permissions: typing.List[str]

class Expr(typing_extensions.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str

class OidcToken(typing_extensions.TypedDict, total=False):
    audience: str
    serviceAccountEmail: str

class ReceivedMessage(typing_extensions.TypedDict, total=False):
    message: PubsubMessage
    ackId: str

class Empty(typing_extensions.TypedDict, total=False): ...
