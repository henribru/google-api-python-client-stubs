import typing

import typing_extensions

_list = list

@typing.type_check_only
class AcknowledgeRequest(typing_extensions.TypedDict, total=False):
    ackIds: _list[str]

@typing.type_check_only
class BigQueryConfig(typing_extensions.TypedDict, total=False):
    dropUnknownFields: bool
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "ACTIVE",
        "PERMISSION_DENIED",
        "NOT_FOUND",
        "SCHEMA_MISMATCH",
    ]
    table: str
    useTopicSchema: bool
    writeMetadata: bool

@typing.type_check_only
class Binding(typing_extensions.TypedDict, total=False):
    condition: Expr
    members: _list[str]
    role: str

@typing.type_check_only
class CreateSnapshotRequest(typing_extensions.TypedDict, total=False):
    labels: dict[str, typing.Any]
    subscription: str

@typing.type_check_only
class DeadLetterPolicy(typing_extensions.TypedDict, total=False):
    deadLetterTopic: str
    maxDeliveryAttempts: int

@typing.type_check_only
class DetachSubscriptionResponse(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class ExpirationPolicy(typing_extensions.TypedDict, total=False):
    ttl: str

@typing.type_check_only
class Expr(typing_extensions.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str

@typing.type_check_only
class ListSchemasResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    schemas: _list[Schema]

@typing.type_check_only
class ListSnapshotsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    snapshots: _list[Snapshot]

@typing.type_check_only
class ListSubscriptionsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    subscriptions: _list[Subscription]

@typing.type_check_only
class ListTopicSnapshotsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    snapshots: _list[str]

@typing.type_check_only
class ListTopicSubscriptionsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    subscriptions: _list[str]

@typing.type_check_only
class ListTopicsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    topics: _list[Topic]

@typing.type_check_only
class MessageStoragePolicy(typing_extensions.TypedDict, total=False):
    allowedPersistenceRegions: _list[str]

@typing.type_check_only
class ModifyAckDeadlineRequest(typing_extensions.TypedDict, total=False):
    ackDeadlineSeconds: int
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
    orderingKey: str
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
    deliveryAttempt: int
    message: PubsubMessage

@typing.type_check_only
class RetryPolicy(typing_extensions.TypedDict, total=False):
    maximumBackoff: str
    minimumBackoff: str

@typing.type_check_only
class Schema(typing_extensions.TypedDict, total=False):
    definition: str
    name: str
    revisionCreateTime: str
    revisionId: str
    type: typing_extensions.Literal["TYPE_UNSPECIFIED", "PROTOCOL_BUFFER", "AVRO"]

@typing.type_check_only
class SchemaSettings(typing_extensions.TypedDict, total=False):
    encoding: typing_extensions.Literal["ENCODING_UNSPECIFIED", "JSON", "BINARY"]
    firstRevisionId: str
    lastRevisionId: str
    schema: str

@typing.type_check_only
class SeekRequest(typing_extensions.TypedDict, total=False):
    snapshot: str
    time: str

@typing.type_check_only
class SeekResponse(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class SetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    policy: Policy

@typing.type_check_only
class Snapshot(typing_extensions.TypedDict, total=False):
    expireTime: str
    labels: dict[str, typing.Any]
    name: str
    topic: str

@typing.type_check_only
class Subscription(typing_extensions.TypedDict, total=False):
    ackDeadlineSeconds: int
    bigqueryConfig: BigQueryConfig
    deadLetterPolicy: DeadLetterPolicy
    detached: bool
    enableExactlyOnceDelivery: bool
    enableMessageOrdering: bool
    expirationPolicy: ExpirationPolicy
    filter: str
    labels: dict[str, typing.Any]
    messageRetentionDuration: str
    name: str
    pushConfig: PushConfig
    retainAckedMessages: bool
    retryPolicy: RetryPolicy
    state: typing_extensions.Literal["STATE_UNSPECIFIED", "ACTIVE", "RESOURCE_ERROR"]
    topic: str
    topicMessageRetentionDuration: str

@typing.type_check_only
class TestIamPermissionsRequest(typing_extensions.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class TestIamPermissionsResponse(typing_extensions.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class Topic(typing_extensions.TypedDict, total=False):
    kmsKeyName: str
    labels: dict[str, typing.Any]
    messageRetentionDuration: str
    messageStoragePolicy: MessageStoragePolicy
    name: str
    satisfiesPzs: bool
    schemaSettings: SchemaSettings

@typing.type_check_only
class UpdateSnapshotRequest(typing_extensions.TypedDict, total=False):
    snapshot: Snapshot
    updateMask: str

@typing.type_check_only
class UpdateSubscriptionRequest(typing_extensions.TypedDict, total=False):
    subscription: Subscription
    updateMask: str

@typing.type_check_only
class UpdateTopicRequest(typing_extensions.TypedDict, total=False):
    topic: Topic
    updateMask: str

@typing.type_check_only
class ValidateMessageRequest(typing_extensions.TypedDict, total=False):
    encoding: typing_extensions.Literal["ENCODING_UNSPECIFIED", "JSON", "BINARY"]
    message: str
    name: str
    schema: Schema

@typing.type_check_only
class ValidateMessageResponse(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class ValidateSchemaRequest(typing_extensions.TypedDict, total=False):
    schema: Schema

@typing.type_check_only
class ValidateSchemaResponse(typing_extensions.TypedDict, total=False): ...
