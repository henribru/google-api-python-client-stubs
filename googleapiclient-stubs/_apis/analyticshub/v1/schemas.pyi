import typing

_list = list

@typing.type_check_only
class AIInference(typing.TypedDict, total=False):
    endpoint: str
    serviceAccountEmail: str
    unstructuredInference: UnstructuredInference

@typing.type_check_only
class ApproveQueryTemplateRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class AuditConfig(typing.TypedDict, total=False):
    auditLogConfigs: _list[AuditLogConfig]
    service: str

@typing.type_check_only
class AuditLogConfig(typing.TypedDict, total=False):
    exemptedMembers: _list[str]
    logType: typing.Literal[
        "LOG_TYPE_UNSPECIFIED", "ADMIN_READ", "DATA_WRITE", "DATA_READ"
    ]

@typing.type_check_only
class AvroConfig(typing.TypedDict, total=False):
    useTopicSchema: bool
    writeMetadata: bool

@typing.type_check_only
class BigQueryConfig(typing.TypedDict, total=False):
    dropUnknownFields: bool
    serviceAccountEmail: str
    table: str
    useTableSchema: bool
    useTopicSchema: bool
    writeMetadata: bool

@typing.type_check_only
class BigQueryDatasetSource(typing.TypedDict, total=False):
    dataset: str
    effectiveReplicas: _list[Replica]
    replicaLocations: _list[str]
    restrictedExportPolicy: RestrictedExportPolicy
    selectedResources: _list[SelectedResource]

@typing.type_check_only
class BigtableConfig(typing.TypedDict, total=False):
    appProfileId: str
    serviceAccountEmail: str
    table: str
    writeMetadata: bool

@typing.type_check_only
class Binding(typing.TypedDict, total=False):
    condition: Expr
    members: _list[str]
    role: str

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
    textConfig: TextConfig

@typing.type_check_only
class Compression(typing.TypedDict, total=False):
    compressionAlgorithm: typing.Literal["COMPRESSION_ALGORITHM_UNSPECIFIED", "ZLIB"]
    compressionMode: typing.Literal[
        "COMPRESSION_MODE_UNSPECIFIED", "COMPRESS", "DECOMPRESS"
    ]

@typing.type_check_only
class DataExchange(typing.TypedDict, total=False):
    description: str
    discoveryType: typing.Literal[
        "DISCOVERY_TYPE_UNSPECIFIED", "DISCOVERY_TYPE_PRIVATE", "DISCOVERY_TYPE_PUBLIC"
    ]
    displayName: str
    documentation: str
    icon: str
    listingCount: int
    logLinkedDatasetQueryUserEmail: bool
    name: str
    primaryContact: str
    sharingEnvironmentConfig: SharingEnvironmentConfig

@typing.type_check_only
class DataProvider(typing.TypedDict, total=False):
    name: str
    primaryContact: str

@typing.type_check_only
class DcrExchangeConfig(typing.TypedDict, total=False):
    singleLinkedDatasetPerCleanroom: bool
    singleSelectedResourceSharingRestriction: bool

@typing.type_check_only
class DeadLetterPolicy(typing.TypedDict, total=False):
    deadLetterTopic: str
    maxDeliveryAttempts: int

@typing.type_check_only
class DefaultExchangeConfig(typing.TypedDict, total=False): ...

@typing.type_check_only
class DestinationDataset(typing.TypedDict, total=False):
    datasetReference: DestinationDatasetReference
    description: str
    friendlyName: str
    labels: dict[str, typing.Any]
    location: str
    replicaLocations: _list[str]

@typing.type_check_only
class DestinationDatasetReference(typing.TypedDict, total=False):
    datasetId: str
    projectId: str

@typing.type_check_only
class DestinationPubSubSubscription(typing.TypedDict, total=False):
    pubsubSubscription: GooglePubsubV1Subscription

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
class GetIamPolicyRequest(typing.TypedDict, total=False):
    options: GetPolicyOptions

@typing.type_check_only
class GetPolicyOptions(typing.TypedDict, total=False):
    requestedPolicyVersion: int

@typing.type_check_only
class GoogleCloudBigqueryAnalyticshubV1ListingCommercialInfo(
    typing.TypedDict, total=False
):
    cloudMarketplace: (
        GoogleCloudBigqueryAnalyticshubV1ListingCommercialInfoGoogleCloudMarketplaceInfo
    )

@typing.type_check_only
class GoogleCloudBigqueryAnalyticshubV1ListingCommercialInfoGoogleCloudMarketplaceInfo(
    typing.TypedDict, total=False
):
    commercialState: typing.Literal[
        "COMMERCIAL_STATE_UNSPECIFIED", "ONBOARDING", "ACTIVE"
    ]
    service: str

@typing.type_check_only
class GoogleCloudBigqueryAnalyticshubV1SubscriptionCommercialInfo(
    typing.TypedDict, total=False
):
    cloudMarketplace: GoogleCloudBigqueryAnalyticshubV1SubscriptionCommercialInfoGoogleCloudMarketplaceInfo

@typing.type_check_only
class GoogleCloudBigqueryAnalyticshubV1SubscriptionCommercialInfoGoogleCloudMarketplaceInfo(
    typing.TypedDict, total=False
):
    order: str

@typing.type_check_only
class GooglePubsubV1Subscription(typing.TypedDict, total=False):
    ackDeadlineSeconds: int
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
    tags: dict[str, typing.Any]

@typing.type_check_only
class JavaScriptUDF(typing.TypedDict, total=False):
    code: str
    functionName: str

@typing.type_check_only
class LinkedResource(typing.TypedDict, total=False):
    linkedDataset: str
    linkedPubsubSubscription: str
    listing: str

@typing.type_check_only
class ListDataExchangesResponse(typing.TypedDict, total=False):
    dataExchanges: _list[DataExchange]
    nextPageToken: str

@typing.type_check_only
class ListListingsResponse(typing.TypedDict, total=False):
    listings: _list[Listing]
    nextPageToken: str

@typing.type_check_only
class ListOrgDataExchangesResponse(typing.TypedDict, total=False):
    dataExchanges: _list[DataExchange]
    nextPageToken: str

@typing.type_check_only
class ListQueryTemplatesResponse(typing.TypedDict, total=False):
    nextPageToken: str
    queryTemplates: _list[QueryTemplate]

@typing.type_check_only
class ListSharedResourceSubscriptionsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    sharedResourceSubscriptions: _list[Subscription]

@typing.type_check_only
class ListSubscriptionsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    subscriptions: _list[Subscription]

@typing.type_check_only
class Listing(typing.TypedDict, total=False):
    allowOnlyMetadataSharing: bool
    bigqueryDataset: BigQueryDatasetSource
    categories: _list[
        typing.Literal[
            "CATEGORY_UNSPECIFIED",
            "CATEGORY_OTHERS",
            "CATEGORY_ADVERTISING_AND_MARKETING",
            "CATEGORY_COMMERCE",
            "CATEGORY_CLIMATE_AND_ENVIRONMENT",
            "CATEGORY_DEMOGRAPHICS",
            "CATEGORY_ECONOMICS",
            "CATEGORY_EDUCATION",
            "CATEGORY_ENERGY",
            "CATEGORY_FINANCIAL",
            "CATEGORY_GAMING",
            "CATEGORY_GEOSPATIAL",
            "CATEGORY_HEALTHCARE_AND_LIFE_SCIENCE",
            "CATEGORY_MEDIA",
            "CATEGORY_PUBLIC_SECTOR",
            "CATEGORY_RETAIL",
            "CATEGORY_SPORTS",
            "CATEGORY_SCIENCE_AND_RESEARCH",
            "CATEGORY_TRANSPORTATION_AND_LOGISTICS",
            "CATEGORY_TRAVEL_AND_TOURISM",
            "CATEGORY_GOOGLE_EARTH_ENGINE",
        ]
    ]
    commercialInfo: GoogleCloudBigqueryAnalyticshubV1ListingCommercialInfo
    dataProvider: DataProvider
    description: str
    discoveryType: typing.Literal[
        "DISCOVERY_TYPE_UNSPECIFIED", "DISCOVERY_TYPE_PRIVATE", "DISCOVERY_TYPE_PUBLIC"
    ]
    displayName: str
    documentation: str
    icon: str
    logLinkedDatasetQueryUserEmail: bool
    name: str
    primaryContact: str
    publisher: Publisher
    pubsubTopic: PubSubTopicSource
    requestAccess: str
    resourceType: typing.Literal[
        "SHARED_RESOURCE_TYPE_UNSPECIFIED", "BIGQUERY_DATASET", "PUBSUB_TOPIC"
    ]
    restrictedExportConfig: RestrictedExportConfig
    state: typing.Literal["STATE_UNSPECIFIED", "ACTIVE"]
    storedProcedureConfig: StoredProcedureConfig

@typing.type_check_only
class MessageTransform(typing.TypedDict, total=False):
    aiInference: AIInference
    compression: Compression
    disabled: bool
    enabled: bool
    javascriptUdf: JavaScriptUDF

@typing.type_check_only
class NoWrapper(typing.TypedDict, total=False):
    writeMetadata: bool

@typing.type_check_only
class OidcToken(typing.TypedDict, total=False):
    audience: str
    serviceAccountEmail: str

@typing.type_check_only
class Operation(typing.TypedDict, total=False):
    done: bool
    error: Status
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class OperationMetadata(typing.TypedDict, total=False):
    apiVersion: str
    createTime: str
    endTime: str
    requestedCancellation: bool
    statusMessage: str
    target: str
    verb: str

@typing.type_check_only
class Policy(typing.TypedDict, total=False):
    auditConfigs: _list[AuditConfig]
    bindings: _list[Binding]
    etag: str
    version: int

@typing.type_check_only
class PubSubTopicSource(typing.TypedDict, total=False):
    dataAffinityRegions: _list[str]
    topic: str

@typing.type_check_only
class Publisher(typing.TypedDict, total=False):
    name: str
    primaryContact: str

@typing.type_check_only
class PubsubWrapper(typing.TypedDict, total=False): ...

@typing.type_check_only
class PushConfig(typing.TypedDict, total=False):
    attributes: dict[str, typing.Any]
    noWrapper: NoWrapper
    oidcToken: OidcToken
    pubsubWrapper: PubsubWrapper
    pushEndpoint: str

@typing.type_check_only
class QueryTemplate(typing.TypedDict, total=False):
    createTime: str
    description: str
    displayName: str
    documentation: str
    name: str
    primaryContact: str
    proposer: str
    routine: Routine
    state: typing.Literal[
        "STATE_UNSPECIFIED", "DRAFTED", "PENDING", "DELETED", "APPROVED"
    ]
    updateTime: str

@typing.type_check_only
class RefreshSubscriptionRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class RefreshSubscriptionResponse(typing.TypedDict, total=False):
    subscription: Subscription

@typing.type_check_only
class Replica(typing.TypedDict, total=False):
    location: str
    primaryState: typing.Literal["PRIMARY_STATE_UNSPECIFIED", "PRIMARY_REPLICA"]
    replicaState: typing.Literal[
        "REPLICA_STATE_UNSPECIFIED", "READY_TO_USE", "UNAVAILABLE"
    ]

@typing.type_check_only
class RestrictedExportConfig(typing.TypedDict, total=False):
    enabled: bool
    restrictDirectTableAccess: bool
    restrictQueryResult: bool

@typing.type_check_only
class RestrictedExportPolicy(typing.TypedDict, total=False):
    enabled: bool
    restrictDirectTableAccess: bool
    restrictQueryResult: bool

@typing.type_check_only
class RetryPolicy(typing.TypedDict, total=False):
    maximumBackoff: str
    minimumBackoff: str

@typing.type_check_only
class RevokeSubscriptionRequest(typing.TypedDict, total=False):
    revokeCommercial: bool

@typing.type_check_only
class RevokeSubscriptionResponse(typing.TypedDict, total=False): ...

@typing.type_check_only
class Routine(typing.TypedDict, total=False):
    definitionBody: str
    routineType: typing.Literal["ROUTINE_TYPE_UNSPECIFIED", "TABLE_VALUED_FUNCTION"]

@typing.type_check_only
class SelectedResource(typing.TypedDict, total=False):
    routine: str
    table: str

@typing.type_check_only
class SetIamPolicyRequest(typing.TypedDict, total=False):
    policy: Policy
    updateMask: str

@typing.type_check_only
class SharingEnvironmentConfig(typing.TypedDict, total=False):
    dcrExchangeConfig: DcrExchangeConfig
    defaultExchangeConfig: DefaultExchangeConfig

@typing.type_check_only
class Status(typing.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class StoredProcedureConfig(typing.TypedDict, total=False):
    allowedStoredProcedureTypes: _list[
        typing.Literal["STORED_PROCEDURE_TYPE_UNSPECIFIED", "SQL_PROCEDURE"]
    ]
    enabled: bool

@typing.type_check_only
class SubmitQueryTemplateRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class SubscribeDataExchangeRequest(typing.TypedDict, total=False):
    destination: str
    destinationDataset: DestinationDataset
    subscriberContact: str
    subscription: str

@typing.type_check_only
class SubscribeDataExchangeResponse(typing.TypedDict, total=False):
    subscription: Subscription

@typing.type_check_only
class SubscribeListingRequest(typing.TypedDict, total=False):
    destinationDataset: DestinationDataset
    destinationPubsubSubscription: DestinationPubSubSubscription

@typing.type_check_only
class SubscribeListingResponse(typing.TypedDict, total=False):
    subscription: Subscription

@typing.type_check_only
class Subscription(typing.TypedDict, total=False):
    commercialInfo: GoogleCloudBigqueryAnalyticshubV1SubscriptionCommercialInfo
    creationTime: str
    dataExchange: str
    destinationDataset: DestinationDataset
    lastModifyTime: str
    linkedDatasetMap: dict[str, typing.Any]
    linkedResources: _list[LinkedResource]
    listing: str
    logLinkedDatasetQueryUserEmail: bool
    name: str
    organizationDisplayName: str
    organizationId: str
    resourceType: typing.Literal[
        "SHARED_RESOURCE_TYPE_UNSPECIFIED", "BIGQUERY_DATASET", "PUBSUB_TOPIC"
    ]
    state: typing.Literal[
        "STATE_UNSPECIFIED", "STATE_ACTIVE", "STATE_STALE", "STATE_INACTIVE"
    ]
    subscriberContact: str

@typing.type_check_only
class TestIamPermissionsRequest(typing.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class TestIamPermissionsResponse(typing.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class TextConfig(typing.TypedDict, total=False): ...

@typing.type_check_only
class UnstructuredInference(typing.TypedDict, total=False):
    parameters: dict[str, typing.Any]
