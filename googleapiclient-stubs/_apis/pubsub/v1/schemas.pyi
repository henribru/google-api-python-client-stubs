import typing

import typing_extensions

class RetryPolicy(typing_extensions.TypedDict, total=False):
    minimumBackoff: str
    maximumBackoff: str

class Topic(typing_extensions.TypedDict, total=False):
    kmsKeyName: str
    name: str
    labels: typing.Dict[str, typing.Any]
    messageStoragePolicy: MessageStoragePolicy

class DetachSubscriptionResponse(typing_extensions.TypedDict, total=False): ...

class TestIamPermissionsResponse(typing_extensions.TypedDict, total=False):
    permissions: typing.List[str]

class CreateSnapshotRequest(typing_extensions.TypedDict, total=False):
    labels: typing.Dict[str, typing.Any]
    subscription: str

class UpdateSnapshotRequest(typing_extensions.TypedDict, total=False):
    snapshot: Snapshot
    updateMask: str

class PublishResponse(typing_extensions.TypedDict, total=False):
    messageIds: typing.List[str]

class OidcToken(typing_extensions.TypedDict, total=False):
    serviceAccountEmail: str
    audience: str

class PushConfig(typing_extensions.TypedDict, total=False):
    oidcToken: OidcToken
    attributes: typing.Dict[str, typing.Any]
    pushEndpoint: str

class ListTopicSnapshotsResponse(typing_extensions.TypedDict, total=False):
    snapshots: typing.List[str]
    nextPageToken: str

class MessageStoragePolicy(typing_extensions.TypedDict, total=False):
    allowedPersistenceRegions: typing.List[str]

class Binding(typing_extensions.TypedDict, total=False):
    members: typing.List[str]
    condition: Expr
    bindingId: str
    role: str

class PublishRequest(typing_extensions.TypedDict, total=False):
    messages: typing.List[PubsubMessage]

class DeadLetterPolicy(typing_extensions.TypedDict, total=False):
    deadLetterTopic: str
    maxDeliveryAttempts: int

class Expr(typing_extensions.TypedDict, total=False):
    location: str
    expression: str
    title: str
    description: str

class PullRequest(typing_extensions.TypedDict, total=False):
    returnImmediately: bool
    maxMessages: int

class ModifyPushConfigRequest(typing_extensions.TypedDict, total=False):
    pushConfig: PushConfig

class ReceivedMessage(typing_extensions.TypedDict, total=False):
    message: PubsubMessage
    ackId: str
    deliveryAttempt: int

class SeekResponse(typing_extensions.TypedDict, total=False): ...

class Policy(typing_extensions.TypedDict, total=False):
    version: int
    bindings: typing.List[Binding]
    etag: str

class AcknowledgeRequest(typing_extensions.TypedDict, total=False):
    ackIds: typing.List[str]

class PubsubMessage(typing_extensions.TypedDict, total=False):
    publishTime: str
    data: str
    orderingKey: str
    messageId: str
    attributes: typing.Dict[str, typing.Any]

class UpdateTopicRequest(typing_extensions.TypedDict, total=False):
    updateMask: str
    topic: Topic

class ExpirationPolicy(typing_extensions.TypedDict, total=False):
    ttl: str

class UpdateSubscriptionRequest(typing_extensions.TypedDict, total=False):
    subscription: Subscription
    updateMask: str

class TestIamPermissionsRequest(typing_extensions.TypedDict, total=False):
    permissions: typing.List[str]

class Empty(typing_extensions.TypedDict, total=False): ...

class SeekRequest(typing_extensions.TypedDict, total=False):
    snapshot: str
    time: str

class ModifyAckDeadlineRequest(typing_extensions.TypedDict, total=False):
    ackIds: typing.List[str]
    ackDeadlineSeconds: int

class PullResponse(typing_extensions.TypedDict, total=False):
    receivedMessages: typing.List[ReceivedMessage]

class SetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    policy: Policy

class ListSnapshotsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    snapshots: typing.List[Snapshot]

class Subscription(typing_extensions.TypedDict, total=False):
    deadLetterPolicy: DeadLetterPolicy
    labels: typing.Dict[str, typing.Any]
    enableMessageOrdering: bool
    pushConfig: PushConfig
    retainAckedMessages: bool
    retryPolicy: RetryPolicy
    name: str
    filter: str
    ackDeadlineSeconds: int
    messageRetentionDuration: str
    expirationPolicy: ExpirationPolicy
    detached: bool
    topic: str

class ListTopicSubscriptionsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    subscriptions: typing.List[str]

class Snapshot(typing_extensions.TypedDict, total=False):
    name: str
    topic: str
    expireTime: str
    labels: typing.Dict[str, typing.Any]

class ListSubscriptionsResponse(typing_extensions.TypedDict, total=False):
    subscriptions: typing.List[Subscription]
    nextPageToken: str

class ListTopicsResponse(typing_extensions.TypedDict, total=False):
    topics: typing.List[Topic]
    nextPageToken: str
