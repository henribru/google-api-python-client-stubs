import typing

import typing_extensions

_list = list

@typing.type_check_only
class AcknowledgeRequest(typing_extensions.TypedDict, total=False):
    ackIds: _list[str]

@typing.type_check_only
class Binding(typing_extensions.TypedDict, total=False):
    condition: Expr
    members: _list[str]
    role: str

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Expr(typing_extensions.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str

@typing.type_check_only
class ListSubscriptionsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    subscriptions: _list[Subscription]

@typing.type_check_only
class ListTopicSubscriptionsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    subscriptions: _list[str]

@typing.type_check_only
class ListTopicsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    topics: _list[Topic]

@typing.type_check_only
class ModifyAckDeadlineRequest(typing_extensions.TypedDict, total=False):
    ackDeadlineSeconds: int
    ackId: str
    ackIds: _list[str]

@typing.type_check_only
class ModifyPushConfigRequest(typing_extensions.TypedDict, total=False):
    pushConfig: PushConfig

@typing.type_check_only
class OidcToken(typing_extensions.TypedDict, total=False):
    audience: str
    serviceAccountEmail: str

@typing.type_check_only
class Policy(typing_extensions.TypedDict, total=False):
    bindings: _list[Binding]
    etag: str
    version: int

@typing.type_check_only
class PublishRequest(typing_extensions.TypedDict, total=False):
    messages: _list[PubsubMessage]

@typing.type_check_only
class PublishResponse(typing_extensions.TypedDict, total=False):
    messageIds: _list[str]

@typing.type_check_only
class PubsubMessage(typing_extensions.TypedDict, total=False):
    attributes: dict[str, typing.Any]
    data: str
    messageId: str
    publishTime: str

@typing.type_check_only
class PullRequest(typing_extensions.TypedDict, total=False):
    maxMessages: int
    returnImmediately: bool

@typing.type_check_only
class PullResponse(typing_extensions.TypedDict, total=False):
    receivedMessages: _list[ReceivedMessage]

@typing.type_check_only
class PushConfig(typing_extensions.TypedDict, total=False):
    attributes: dict[str, typing.Any]
    oidcToken: OidcToken
    pushEndpoint: str

@typing.type_check_only
class ReceivedMessage(typing_extensions.TypedDict, total=False):
    ackId: str
    message: PubsubMessage

@typing.type_check_only
class SetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    policy: Policy

@typing.type_check_only
class Subscription(typing_extensions.TypedDict, total=False):
    ackDeadlineSeconds: int
    name: str
    pushConfig: PushConfig
    topic: str

@typing.type_check_only
class TestIamPermissionsRequest(typing_extensions.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class TestIamPermissionsResponse(typing_extensions.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class Topic(typing_extensions.TypedDict, total=False):
    name: str
