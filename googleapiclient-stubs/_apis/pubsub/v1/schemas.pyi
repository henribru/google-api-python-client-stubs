import typing

_list = list

@typing.type_check_only
class AIInference(typing.TypedDict, total=False):
    endpoint: str
    serviceAccountEmail: str
    unstructuredInference: UnstructuredInference

@typing.type_check_only
class AcknowledgeRequest(typing.TypedDict, total=False):
    ackIds: _list[str]

@typing.type_check_only
class AnalyticsHubSubscriptionInfo(typing.TypedDict, total=False):
    listing: str
    subscription: str

@typing.type_check_only
class AvroConfig(typing.TypedDict, total=False):
    useTopicSchema: bool
    writeMetadata: bool

@typing.type_check_only
class AvroFormat(typing.TypedDict, total=False): ...

@typing.type_check_only
class AwsKinesis(typing.TypedDict, total=False):
    awsRoleArn: str
    consumerArn: str
    gcpServiceAccount: str
    state: typing.Literal[
        "STATE_UNSPECIFIED",
        "ACTIVE",
        "KINESIS_PERMISSION_DENIED",
        "PUBLISH_PERMISSION_DENIED",
        "STREAM_NOT_FOUND",
        "CONSUMER_NOT_FOUND",
        "CONFLICTING_REGION_CONSTRAINTS",
    ]
    streamArn: str

@typing.type_check_only
class AwsMsk(typing.TypedDict, total=False):
    awsRoleArn: str
    clusterArn: str
    gcpServiceAccount: str
    state: typing.Literal[
        "STATE_UNSPECIFIED",
        "ACTIVE",
        "MSK_PERMISSION_DENIED",
        "PUBLISH_PERMISSION_DENIED",
        "CLUSTER_NOT_FOUND",
        "TOPIC_NOT_FOUND",
        "CONFLICTING_REGION_CONSTRAINTS",
    ]
    topic: str

@typing.type_check_only
class AzureEventHubs(typing.TypedDict, total=False):
    clientId: str
    eventHub: str
    gcpServiceAccount: str
    namespace: str
    resourceGroup: str
    state: typing.Literal[
        "STATE_UNSPECIFIED",
        "ACTIVE",
        "EVENT_HUBS_PERMISSION_DENIED",
        "PUBLISH_PERMISSION_DENIED",
        "NAMESPACE_NOT_FOUND",
        "EVENT_HUB_NOT_FOUND",
        "SUBSCRIPTION_NOT_FOUND",
        "RESOURCE_GROUP_NOT_FOUND",
        "CONFLICTING_REGION_CONSTRAINTS",
    ]
    subscriptionId: str
    tenantId: str

@typing.type_check_only
class BigQueryConfig(typing.TypedDict, total=False):
    dropUnknownFields: bool
    serviceAccountEmail: str
    state: typing.Literal[
        "STATE_UNSPECIFIED",
        "ACTIVE",
        "PERMISSION_DENIED",
        "NOT_FOUND",
        "SCHEMA_MISMATCH",
        "IN_TRANSIT_LOCATION_RESTRICTION",
        "VERTEX_AI_LOCATION_RESTRICTION",
    ]
    table: str
    useTableSchema: bool
    useTopicSchema: bool
    writeMetadata: bool

@typing.type_check_only
class BigtableConfig(typing.TypedDict, total=False):
    appProfileId: str
    serviceAccountEmail: str
    state: typing.Literal[
        "STATE_UNSPECIFIED",
        "ACTIVE",
        "NOT_FOUND",
        "APP_PROFILE_MISCONFIGURED",
        "PERMISSION_DENIED",
        "SCHEMA_MISMATCH",
        "IN_TRANSIT_LOCATION_RESTRICTION",
        "VERTEX_AI_LOCATION_RESTRICTION",
    ]
    table: str
    writeMetadata: bool

@typing.type_check_only
class Binding(typing.TypedDict, total=False):
    condition: Expr
    members: _list[str]
    role: str

@typing.type_check_only
class CloudStorage(typing.TypedDict, total=False):
    avroFormat: AvroFormat
    bucket: str
    matchGlob: str
    minimumObjectCreateTime: str
    pubsubAvroFormat: PubSubAvroFormat
    state: typing.Literal[
        "STATE_UNSPECIFIED",
        "ACTIVE",
        "CLOUD_STORAGE_PERMISSION_DENIED",
        "PUBLISH_PERMISSION_DENIED",
        "BUCKET_NOT_FOUND",
        "TOO_MANY_OBJECTS",
        "CONFLICTING_REGION_CONSTRAINTS",
    ]
    textFormat: TextFormat

@typing.type_check_only
class CloudStorageConfig(typing.TypedDict, total=False):
    avroConfig: AvroConfig
    bucket: str
    filenameDatetimeFormat: str
    filenamePrefix: str
    filenameSuffix: str
    maxBytes: str
    maxDuration: str
    maxMessages: str
    serviceAccountEmail: str
    state: typing.Literal[
        "STATE_UNSPECIFIED",
        "ACTIVE",
        "PERMISSION_DENIED",
        "NOT_FOUND",
        "IN_TRANSIT_LOCATION_RESTRICTION",
        "SCHEMA_MISMATCH",
        "VERTEX_AI_LOCATION_RESTRICTION",
    ]
    textConfig: TextConfig

@typing.type_check_only
class CommitSchemaRequest(typing.TypedDict, total=False):
    schema: Schema

@typing.type_check_only
class Compression(typing.TypedDict, total=False):
    compressionAlgorithm: typing.Literal["COMPRESSION_ALGORITHM_UNSPECIFIED", "ZLIB"]
    compressionMode: typing.Literal[
        "COMPRESSION_MODE_UNSPECIFIED", "COMPRESS", "DECOMPRESS"
    ]

@typing.type_check_only
class ConfluentCloud(typing.TypedDict, total=False):
    bootstrapServer: str
    clusterId: str
    gcpServiceAccount: str
    identityPoolId: str
    state: typing.Literal[
        "STATE_UNSPECIFIED",
        "ACTIVE",
        "CONFLUENT_CLOUD_PERMISSION_DENIED",
        "PUBLISH_PERMISSION_DENIED",
        "UNREACHABLE_BOOTSTRAP_SERVER",
        "CLUSTER_NOT_FOUND",
        "TOPIC_NOT_FOUND",
        "CONFLICTING_REGION_CONSTRAINTS",
    ]
    topic: str

@typing.type_check_only
class CreateSnapshotRequest(typing.TypedDict, total=False):
    labels: dict[str, typing.Any]
    subscription: str
    tags: dict[str, typing.Any]

@typing.type_check_only
class DeadLetterPolicy(typing.TypedDict, total=False):
    deadLetterTopic: str
    maxDeliveryAttempts: int

@typing.type_check_only
class DetachSubscriptionResponse(typing.TypedDict, total=False): ...

@typing.type_check_only
class Empty(typing.TypedDict, total=False): ...

@typing.type_check_only
class ExpirationPolicy(typing.TypedDict, total=False):
    ttl: str

@typing.type_check_only
class Expr(typing.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str

@typing.type_check_only
class IngestionDataSourceSettings(typing.TypedDict, total=False):
    awsKinesis: AwsKinesis
    awsMsk: AwsMsk
    azureEventHubs: AzureEventHubs
    cloudStorage: CloudStorage
    confluentCloud: ConfluentCloud
    platformLogsSettings: PlatformLogsSettings

@typing.type_check_only
class JavaScriptUDF(typing.TypedDict, total=False):
    code: str
    functionName: str

@typing.type_check_only
class ListSchemaRevisionsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    schemas: _list[Schema]

@typing.type_check_only
class ListSchemasResponse(typing.TypedDict, total=False):
    nextPageToken: str
    schemas: _list[Schema]

@typing.type_check_only
class ListSnapshotsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    snapshots: _list[Snapshot]

@typing.type_check_only
class ListSubscriptionsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    subscriptions: _list[Subscription]

@typing.type_check_only
class ListTopicSnapshotsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    snapshots: _list[str]

@typing.type_check_only
class ListTopicSubscriptionsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    subscriptions: _list[str]

@typing.type_check_only
class ListTopicsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    topics: _list[Topic]

@typing.type_check_only
class MessageStoragePolicy(typing.TypedDict, total=False):
    allowedPersistenceRegions: _list[str]
    enforceInTransit: bool

@typing.type_check_only
class MessageTransform(typing.TypedDict, total=False):
    aiInference: AIInference
    compression: Compression
    disabled: bool
    enabled: bool
    javascriptUdf: JavaScriptUDF

@typing.type_check_only
class ModifyAckDeadlineRequest(typing.TypedDict, total=False):
    ackDeadlineSeconds: int
    ackIds: _list[str]

@typing.type_check_only
class ModifyPushConfigRequest(typing.TypedDict, total=False):
    pushConfig: PushConfig

@typing.type_check_only
class NoWrapper(typing.TypedDict, total=False):
    writeMetadata: bool

@typing.type_check_only
class OidcToken(typing.TypedDict, total=False):
    audience: str
    serviceAccountEmail: str

@typing.type_check_only
class PlatformLogsSettings(typing.TypedDict, total=False):
    severity: typing.Literal[
        "SEVERITY_UNSPECIFIED", "DISABLED", "DEBUG", "INFO", "WARNING", "ERROR"
    ]

@typing.type_check_only
class Policy(typing.TypedDict, total=False):
    bindings: _list[Binding]
    etag: str
    version: int

@typing.type_check_only
class PubSubAvroFormat(typing.TypedDict, total=False): ...

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
    orderingKey: str
    publishTime: str

@typing.type_check_only
class PubsubWrapper(typing.TypedDict, total=False): ...

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
    noWrapper: NoWrapper
    oidcToken: OidcToken
    pubsubWrapper: PubsubWrapper
    pushEndpoint: str

@typing.type_check_only
class ReceivedMessage(typing.TypedDict, total=False):
    ackId: str
    deliveryAttempt: int
    message: PubsubMessage

@typing.type_check_only
class RetryPolicy(typing.TypedDict, total=False):
    maximumBackoff: str
    minimumBackoff: str

@typing.type_check_only
class RollbackSchemaRequest(typing.TypedDict, total=False):
    revisionId: str

@typing.type_check_only
class Schema(typing.TypedDict, total=False):
    definition: str
    name: str
    revisionCreateTime: str
    revisionId: str
    type: typing.Literal["TYPE_UNSPECIFIED", "PROTOCOL_BUFFER", "AVRO"]

@typing.type_check_only
class SchemaSettings(typing.TypedDict, total=False):
    encoding: typing.Literal["ENCODING_UNSPECIFIED", "JSON", "BINARY"]
    firstRevisionId: str
    lastRevisionId: str
    schema: str

@typing.type_check_only
class SeekRequest(typing.TypedDict, total=False):
    snapshot: str
    time: str

@typing.type_check_only
class SeekResponse(typing.TypedDict, total=False): ...

@typing.type_check_only
class SetIamPolicyRequest(typing.TypedDict, total=False):
    policy: Policy

@typing.type_check_only
class Snapshot(typing.TypedDict, total=False):
    expireTime: str
    labels: dict[str, typing.Any]
    name: str
    topic: str

@typing.type_check_only
class Subscription(typing.TypedDict, total=False):
    ackDeadlineSeconds: int
    analyticsHubSubscriptionInfo: AnalyticsHubSubscriptionInfo
    bigqueryConfig: BigQueryConfig
    bigtableConfig: BigtableConfig
    cloudStorageConfig: CloudStorageConfig
    deadLetterPolicy: DeadLetterPolicy
    detached: bool
    enableExactlyOnceDelivery: bool
    enableMessageOrdering: bool
    expirationPolicy: ExpirationPolicy
    filter: str
    labels: dict[str, typing.Any]
    messageRetentionDuration: str
    messageTransforms: _list[MessageTransform]
    name: str
    pushConfig: PushConfig
    retainAckedMessages: bool
    retryPolicy: RetryPolicy
    state: typing.Literal["STATE_UNSPECIFIED", "ACTIVE", "RESOURCE_ERROR"]
    tags: dict[str, typing.Any]
    topic: str
    topicMessageRetentionDuration: str

@typing.type_check_only
class TestIamPermissionsRequest(typing.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class TestIamPermissionsResponse(typing.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class TextConfig(typing.TypedDict, total=False): ...

@typing.type_check_only
class TextFormat(typing.TypedDict, total=False):
    delimiter: str

@typing.type_check_only
class Topic(typing.TypedDict, total=False):
    ingestionDataSourceSettings: IngestionDataSourceSettings
    kmsKeyName: str
    labels: dict[str, typing.Any]
    messageRetentionDuration: str
    messageStoragePolicy: MessageStoragePolicy
    messageTransforms: _list[MessageTransform]
    name: str
    satisfiesPzs: bool
    schemaSettings: SchemaSettings
    state: typing.Literal["STATE_UNSPECIFIED", "ACTIVE", "INGESTION_RESOURCE_ERROR"]
    tags: dict[str, typing.Any]

@typing.type_check_only
class UnstructuredInference(typing.TypedDict, total=False):
    parameters: dict[str, typing.Any]

@typing.type_check_only
class UpdateSnapshotRequest(typing.TypedDict, total=False):
    snapshot: Snapshot
    updateMask: str

@typing.type_check_only
class UpdateSubscriptionRequest(typing.TypedDict, total=False):
    subscription: Subscription
    updateMask: str

@typing.type_check_only
class UpdateTopicRequest(typing.TypedDict, total=False):
    topic: Topic
    updateMask: str

@typing.type_check_only
class ValidateMessageRequest(typing.TypedDict, total=False):
    encoding: typing.Literal["ENCODING_UNSPECIFIED", "JSON", "BINARY"]
    message: str
    name: str
    schema: Schema

@typing.type_check_only
class ValidateMessageResponse(typing.TypedDict, total=False): ...

@typing.type_check_only
class ValidateSchemaRequest(typing.TypedDict, total=False):
    schema: Schema

@typing.type_check_only
class ValidateSchemaResponse(typing.TypedDict, total=False): ...
