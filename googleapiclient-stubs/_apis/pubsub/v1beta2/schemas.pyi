import typing

_list = list

@typing.type_check_only
class AcknowledgeRequest(typing.TypedDict, total=False):
    ackIds: _list[str]

@typing.type_check_only
class Binding(typing.TypedDict, total=False):
    condition: Expr
    members: _list[str]
    role: str

@typing.type_check_only
class Empty(typing.TypedDict, total=False): ...

@typing.type_check_only
class Expr(typing.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str

@typing.type_check_only
class ListSubscriptionsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    subscriptions: _list[Subscription]

@typing.type_check_only
class ListTopicSubscriptionsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    subscriptions: _list[str]

@typing.type_check_only
class ListTopicsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    topics: _list[Topic]

@typing.type_check_only
class ModifyAckDeadlineRequest(typing.TypedDict, total=False):
    ackDeadlineSeconds: int
    ackId: str
    ackIds: _list[str]

@typing.type_check_only
class ModifyPushConfigRequest(typing.TypedDict, total=False):
    pushConfig: PushConfig

@typing.type_check_only
class OidcToken(typing.TypedDict, total=False):
    audience: str
    serviceAccountEmail: str

@typing.type_check_only
class Policy(typing.TypedDict, total=False):
    bindings: _list[Binding]
    etag: str
    version: int

@typing.type_check_only
class PublishRequest(typing.TypedDict, total=False):
    messages: _list[PubsubMessage]

@typing.type_check_only
class PublishResponse(typing.TypedDict, total=False):
    messageIds: _list[str]

@typing.type_check_only
class PubsubMessage(typing.TypedDict, total=False):
    attributes: dict[str, typing.Any]
    data: str
    messageId: str
    publishTime: str

@typing.type_check_only
class PullRequest(typing.TypedDict, total=False):
    maxMessages: int
    returnImmediately: bool

@typing.type_check_only
class PullResponse(typing.TypedDict, total=False):
    receivedMessages: _list[ReceivedMessage]

@typing.type_check_only
class PushConfig(typing.TypedDict, total=False):
    attributes: dict[str, typing.Any]
    oidcToken: OidcToken
    pushEndpoint: str

@typing.type_check_only
class ReceivedMessage(typing.TypedDict, total=False):
    ackId: str
    message: PubsubMessage

@typing.type_check_only
class SetIamPolicyRequest(typing.TypedDict, total=False):
    policy: Policy

@typing.type_check_only
class Subscription(typing.TypedDict, total=False):
    ackDeadlineSeconds: int
    name: str
    pushConfig: PushConfig
    topic: str

@typing.type_check_only
class TestIamPermissionsRequest(typing.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class TestIamPermissionsResponse(typing.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class Topic(typing.TypedDict, total=False):
    name: str
