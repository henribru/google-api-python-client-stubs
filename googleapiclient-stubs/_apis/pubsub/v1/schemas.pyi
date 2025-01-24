import typing

import typing_extensions

_list = list

@typing.type_check_only
class AcknowledgeRequest(typing_extensions.TypedDict, total=False):
    ackIds: _list[str]

@typing.type_check_only
class AnalyticsHubSubscriptionInfo(typing_extensions.TypedDict, total=False):
    listing: str
    subscription: str

@typing.type_check_only
class AvroConfig(typing_extensions.TypedDict, total=False):
    useTopicSchema: bool
    writeMetadata: bool

@typing.type_check_only
class AvroFormat(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class AwsKinesis(typing_extensions.TypedDict, total=False):
    awsRoleArn: str
    consumerArn: str
    gcpServiceAccount: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "ACTIVE",
        "KINESIS_PERMISSION_DENIED",
        "PUBLISH_PERMISSION_DENIED",
        "STREAM_NOT_FOUND",
        "CONSUMER_NOT_FOUND",
    ]
    streamArn: str

@typing.type_check_only
class AwsMsk(typing_extensions.TypedDict, total=False):
    awsRoleArn: str
    clusterArn: str
    gcpServiceAccount: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "ACTIVE",
        "MSK_PERMISSION_DENIED",
        "PUBLISH_PERMISSION_DENIED",
        "CLUSTER_NOT_FOUND",
        "TOPIC_NOT_FOUND",
    ]
    topic: str

@typing.type_check_only
class AzureEventHubs(typing_extensions.TypedDict, total=False):
    clientId: str
    eventHub: str
    gcpServiceAccount: str
    namespace: str
    resourceGroup: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "ACTIVE",
        "EVENT_HUBS_PERMISSION_DENIED",
        "PUBLISH_PERMISSION_DENIED",
        "NAMESPACE_NOT_FOUND",
        "EVENT_HUB_NOT_FOUND",
        "SUBSCRIPTION_NOT_FOUND",
        "RESOURCE_GROUP_NOT_FOUND",
    ]
    subscriptionId: str
    tenantId: str

@typing.type_check_only
class BigQueryConfig(typing_extensions.TypedDict, total=False):
    dropUnknownFields: bool
    serviceAccountEmail: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "ACTIVE",
        "PERMISSION_DENIED",
        "NOT_FOUND",
        "SCHEMA_MISMATCH",
        "IN_TRANSIT_LOCATION_RESTRICTION",
    ]
    table: str
    useTableSchema: bool
    useTopicSchema: bool
    writeMetadata: bool

@typing.type_check_only
class Binding(typing_extensions.TypedDict, total=False):
    condition: Expr
    members: _list[str]
    role: str

@typing.type_check_only
class CloudStorage(typing_extensions.TypedDict, total=False):
    avroFormat: AvroFormat
    bucket: str
    matchGlob: str
    minimumObjectCreateTime: str
    pubsubAvroFormat: PubSubAvroFormat
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "ACTIVE",
        "CLOUD_STORAGE_PERMISSION_DENIED",
        "PUBLISH_PERMISSION_DENIED",
        "BUCKET_NOT_FOUND",
        "TOO_MANY_OBJECTS",
    ]
    textFormat: TextFormat

@typing.type_check_only
class CloudStorageConfig(typing_extensions.TypedDict, total=False):
    avroConfig: AvroConfig
    bucket: str
    filenameDatetimeFormat: str
    filenamePrefix: str
    filenameSuffix: str
    maxBytes: str
    maxDuration: str
    maxMessages: str
    serviceAccountEmail: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "ACTIVE",
        "PERMISSION_DENIED",
        "NOT_FOUND",
        "IN_TRANSIT_LOCATION_RESTRICTION",
        "SCHEMA_MISMATCH",
    ]
    textConfig: TextConfig

@typing.type_check_only
class CommitSchemaRequest(typing_extensions.TypedDict, total=False):
    schema: Schema

@typing.type_check_only
class ConfluentCloud(typing_extensions.TypedDict, total=False):
    bootstrapServer: str
    clusterId: str
    gcpServiceAccount: str
    identityPoolId: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "ACTIVE",
        "CONFLUENT_CLOUD_PERMISSION_DENIED",
        "PUBLISH_PERMISSION_DENIED",
        "UNREACHABLE_BOOTSTRAP_SERVER",
        "CLUSTER_NOT_FOUND",
        "TOPIC_NOT_FOUND",
    ]
    topic: str

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
class IngestionDataSourceSettings(typing_extensions.TypedDict, total=False):
    awsKinesis: AwsKinesis
    awsMsk: AwsMsk
    azureEventHubs: AzureEventHubs
    cloudStorage: CloudStorage
    confluentCloud: ConfluentCloud
    platformLogsSettings: PlatformLogsSettings

@typing.type_check_only
class ListSchemaRevisionsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    schemas: _list[Schema]

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
    enforceInTransit: bool

@typing.type_check_only
class ModifyAckDeadlineRequest(typing_extensions.TypedDict, total=False):
    ackDeadlineSeconds: int
    ackIds: _list[str]

@typing.type_check_only
class ModifyPushConfigRequest(typing_extensions.TypedDict, total=False):
    pushConfig: PushConfig

@typing.type_check_only
class NoWrapper(typing_extensions.TypedDict, total=False):
    writeMetadata: bool

@typing.type_check_only
class OidcToken(typing_extensions.TypedDict, total=False):
    audience: str
    serviceAccountEmail: str

@typing.type_check_only
class PlatformLogsSettings(typing_extensions.TypedDict, total=False):
    severity: typing_extensions.Literal[
        "SEVERITY_UNSPECIFIED", "DISABLED", "DEBUG", "INFO", "WARNING", "ERROR"
    ]

@typing.type_check_only
class Policy(typing_extensions.TypedDict, total=False):
    bindings: _list[Binding]
    etag: str
    version: int

@typing.type_check_only
class PubSubAvroFormat(typing_extensions.TypedDict, total=False): ...

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
class PubsubWrapper(typing_extensions.TypedDict, total=False): ...

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
    noWrapper: NoWrapper
    oidcToken: OidcToken
    pubsubWrapper: PubsubWrapper
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
class RollbackSchemaRequest(typing_extensions.TypedDict, total=False):
    revisionId: str

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
    analyticsHubSubscriptionInfo: AnalyticsHubSubscriptionInfo
    bigqueryConfig: BigQueryConfig
    cloudStorageConfig: CloudStorageConfig
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
class TextConfig(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class TextFormat(typing_extensions.TypedDict, total=False):
    delimiter: str

@typing.type_check_only
class Topic(typing_extensions.TypedDict, total=False):
    ingestionDataSourceSettings: IngestionDataSourceSettings
    kmsKeyName: str
    labels: dict[str, typing.Any]
    messageRetentionDuration: str
    messageStoragePolicy: MessageStoragePolicy
    name: str
    satisfiesPzs: bool
    schemaSettings: SchemaSettings
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "ACTIVE", "INGESTION_RESOURCE_ERROR"
    ]

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
