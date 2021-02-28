import typing

import typing_extensions
@typing.type_check_only
class AcknowledgeRequest(typing_extensions.TypedDict, total=False):
    ackIds: typing.List[str]

@typing.type_check_only
class Binding(typing_extensions.TypedDict, total=False):
    condition: Expr
    members: typing.List[str]
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
    subscriptions: typing.List[Subscription]

@typing.type_check_only
class ListTopicSubscriptionsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    subscriptions: typing.List[str]

@typing.type_check_only
class ListTopicsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    topics: typing.List[Topic]

@typing.type_check_only
class ModifyAckDeadlineRequest(typing_extensions.TypedDict, total=False):
    ackDeadlineSeconds: int
    ackId: str
    ackIds: typing.List[str]

@typing.type_check_only
class ModifyPushConfigRequest(typing_extensions.TypedDict, total=False):
    pushConfig: PushConfig

@typing.type_check_only
class OidcToken(typing_extensions.TypedDict, total=False):
    audience: str
    serviceAccountEmail: str

@typing.type_check_only
class Policy(typing_extensions.TypedDict, total=False):
    bindings: typing.List[Binding]
    etag: str
    version: int

@typing.type_check_only
class PublishRequest(typing_extensions.TypedDict, total=False):
    messages: typing.List[PubsubMessage]

@typing.type_check_only
class PublishResponse(typing_extensions.TypedDict, total=False):
    messageIds: typing.List[str]

@typing.type_check_only
class PubsubMessage(typing_extensions.TypedDict, total=False):
    attributes: typing.Dict[str, typing.Any]
    data: str
    messageId: str
    publishTime: str

@typing.type_check_only
class PullRequest(typing_extensions.TypedDict, total=False):
    maxMessages: int
    returnImmediately: bool

@typing.type_check_only
class PullResponse(typing_extensions.TypedDict, total=False):
    receivedMessages: typing.List[ReceivedMessage]

@typing.type_check_only
class PushConfig(typing_extensions.TypedDict, total=False):
    attributes: typing.Dict[str, typing.Any]
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
    permissions: typing.List[str]

@typing.type_check_only
class TestIamPermissionsResponse(typing_extensions.TypedDict, total=False):
    permissions: typing.List[str]

@typing.type_check_only
class Topic(typing_extensions.TypedDict, total=False):
    name: str
