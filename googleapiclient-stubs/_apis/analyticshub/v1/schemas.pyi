import typing

import typing_extensions

_list = list

@typing.type_check_only
class AnalyticsHubSubscriptionInfo(typing_extensions.TypedDict, total=False):
    listing: str
    subscription: str

@typing.type_check_only
class AuditConfig(typing_extensions.TypedDict, total=False):
    auditLogConfigs: _list[AuditLogConfig]
    service: str

@typing.type_check_only
class AuditLogConfig(typing_extensions.TypedDict, total=False):
    exemptedMembers: _list[str]
    logType: typing_extensions.Literal[
        "LOG_TYPE_UNSPECIFIED", "ADMIN_READ", "DATA_WRITE", "DATA_READ"
    ]

@typing.type_check_only
class AvroConfig(typing_extensions.TypedDict, total=False):
    useTopicSchema: bool
    writeMetadata: bool

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
class BigQueryDatasetSource(typing_extensions.TypedDict, total=False):
    dataset: str
    restrictedExportPolicy: RestrictedExportPolicy
    selectedResources: _list[SelectedResource]

@typing.type_check_only
class Binding(typing_extensions.TypedDict, total=False):
    condition: Expr
    members: _list[str]
    role: str

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
class DataExchange(typing_extensions.TypedDict, total=False):
    description: str
    discoveryType: typing_extensions.Literal[
        "DISCOVERY_TYPE_UNSPECIFIED", "DISCOVERY_TYPE_PRIVATE", "DISCOVERY_TYPE_PUBLIC"
    ]
    displayName: str
    documentation: str
    icon: str
    listingCount: int
    name: str
    primaryContact: str
    sharingEnvironmentConfig: SharingEnvironmentConfig

@typing.type_check_only
class DataProvider(typing_extensions.TypedDict, total=False):
    name: str
    primaryContact: str

@typing.type_check_only
class DcrExchangeConfig(typing_extensions.TypedDict, total=False):
    singleLinkedDatasetPerCleanroom: bool
    singleSelectedResourceSharingRestriction: bool

@typing.type_check_only
class DeadLetterPolicy(typing_extensions.TypedDict, total=False):
    deadLetterTopic: str
    maxDeliveryAttempts: int

@typing.type_check_only
class DefaultExchangeConfig(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class DestinationDataset(typing_extensions.TypedDict, total=False):
    datasetReference: DestinationDatasetReference
    description: str
    friendlyName: str
    labels: dict[str, typing.Any]
    location: str

@typing.type_check_only
class DestinationDatasetReference(typing_extensions.TypedDict, total=False):
    datasetId: str
    projectId: str

@typing.type_check_only
class DestinationPubSubSubscription(typing_extensions.TypedDict, total=False):
    pubsubSubscription: GooglePubsubV1Subscription

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
class GetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    options: GetPolicyOptions

@typing.type_check_only
class GetPolicyOptions(typing_extensions.TypedDict, total=False):
    requestedPolicyVersion: int

@typing.type_check_only
class GoogleCloudBigqueryAnalyticshubV1ListingCommercialInfo(
    typing_extensions.TypedDict, total=False
):
    cloudMarketplace: (
        GoogleCloudBigqueryAnalyticshubV1ListingCommercialInfoGoogleCloudMarketplaceInfo
    )

@typing.type_check_only
class GoogleCloudBigqueryAnalyticshubV1ListingCommercialInfoGoogleCloudMarketplaceInfo(
    typing_extensions.TypedDict, total=False
):
    commercialState: typing_extensions.Literal[
        "COMMERCIAL_STATE_UNSPECIFIED", "ONBOARDING", "ACTIVE"
    ]
    service: str

@typing.type_check_only
class GoogleCloudBigqueryAnalyticshubV1SubscriptionCommercialInfo(
    typing_extensions.TypedDict, total=False
):
    cloudMarketplace: GoogleCloudBigqueryAnalyticshubV1SubscriptionCommercialInfoGoogleCloudMarketplaceInfo

@typing.type_check_only
class GoogleCloudBigqueryAnalyticshubV1SubscriptionCommercialInfoGoogleCloudMarketplaceInfo(
    typing_extensions.TypedDict, total=False
):
    order: str

@typing.type_check_only
class GooglePubsubV1Subscription(typing_extensions.TypedDict, total=False):
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
    topicMessageRetentionDuration: str

@typing.type_check_only
class LinkedResource(typing_extensions.TypedDict, total=False):
    linkedDataset: str
    linkedPubsubSubscription: str
    listing: str

@typing.type_check_only
class ListDataExchangesResponse(typing_extensions.TypedDict, total=False):
    dataExchanges: _list[DataExchange]
    nextPageToken: str

@typing.type_check_only
class ListListingsResponse(typing_extensions.TypedDict, total=False):
    listings: _list[Listing]
    nextPageToken: str

@typing.type_check_only
class ListOrgDataExchangesResponse(typing_extensions.TypedDict, total=False):
    dataExchanges: _list[DataExchange]
    nextPageToken: str

@typing.type_check_only
class ListSharedResourceSubscriptionsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    sharedResourceSubscriptions: _list[Subscription]

@typing.type_check_only
class ListSubscriptionsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    subscriptions: _list[Subscription]

@typing.type_check_only
class Listing(typing_extensions.TypedDict, total=False):
    bigqueryDataset: BigQueryDatasetSource
    categories: _list[
        typing_extensions.Literal[
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
        ]
    ]
    commercialInfo: GoogleCloudBigqueryAnalyticshubV1ListingCommercialInfo
    dataProvider: DataProvider
    description: str
    discoveryType: typing_extensions.Literal[
        "DISCOVERY_TYPE_UNSPECIFIED", "DISCOVERY_TYPE_PRIVATE", "DISCOVERY_TYPE_PUBLIC"
    ]
    displayName: str
    documentation: str
    icon: str
    name: str
    primaryContact: str
    publisher: Publisher
    pubsubTopic: PubSubTopicSource
    requestAccess: str
    resourceType: typing_extensions.Literal[
        "SHARED_RESOURCE_TYPE_UNSPECIFIED", "BIGQUERY_DATASET", "PUBSUB_TOPIC"
    ]
    restrictedExportConfig: RestrictedExportConfig
    state: typing_extensions.Literal["STATE_UNSPECIFIED", "ACTIVE"]

@typing.type_check_only
class NoWrapper(typing_extensions.TypedDict, total=False):
    writeMetadata: bool

@typing.type_check_only
class OidcToken(typing_extensions.TypedDict, total=False):
    audience: str
    serviceAccountEmail: str

@typing.type_check_only
class Operation(typing_extensions.TypedDict, total=False):
    done: bool
    error: Status
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class OperationMetadata(typing_extensions.TypedDict, total=False):
    apiVersion: str
    createTime: str
    endTime: str
    requestedCancellation: bool
    statusMessage: str
    target: str
    verb: str

@typing.type_check_only
class Policy(typing_extensions.TypedDict, total=False):
    auditConfigs: _list[AuditConfig]
    bindings: _list[Binding]
    etag: str
    version: int

@typing.type_check_only
class PubSubTopicSource(typing_extensions.TypedDict, total=False):
    dataAffinityRegions: _list[str]
    topic: str

@typing.type_check_only
class Publisher(typing_extensions.TypedDict, total=False):
    name: str
    primaryContact: str

@typing.type_check_only
class PubsubWrapper(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class PushConfig(typing_extensions.TypedDict, total=False):
    attributes: dict[str, typing.Any]
    noWrapper: NoWrapper
    oidcToken: OidcToken
    pubsubWrapper: PubsubWrapper
    pushEndpoint: str

@typing.type_check_only
class RefreshSubscriptionRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class RefreshSubscriptionResponse(typing_extensions.TypedDict, total=False):
    subscription: Subscription

@typing.type_check_only
class RestrictedExportConfig(typing_extensions.TypedDict, total=False):
    enabled: bool
    restrictDirectTableAccess: bool
    restrictQueryResult: bool

@typing.type_check_only
class RestrictedExportPolicy(typing_extensions.TypedDict, total=False):
    enabled: bool
    restrictDirectTableAccess: bool
    restrictQueryResult: bool

@typing.type_check_only
class RetryPolicy(typing_extensions.TypedDict, total=False):
    maximumBackoff: str
    minimumBackoff: str

@typing.type_check_only
class RevokeSubscriptionRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class RevokeSubscriptionResponse(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class SelectedResource(typing_extensions.TypedDict, total=False):
    routine: str
    table: str

@typing.type_check_only
class SetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    policy: Policy
    updateMask: str

@typing.type_check_only
class SharingEnvironmentConfig(typing_extensions.TypedDict, total=False):
    dcrExchangeConfig: DcrExchangeConfig
    defaultExchangeConfig: DefaultExchangeConfig

@typing.type_check_only
class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class SubscribeDataExchangeRequest(typing_extensions.TypedDict, total=False):
    destination: str
    destinationDataset: DestinationDataset
    subscriberContact: str
    subscription: str

@typing.type_check_only
class SubscribeDataExchangeResponse(typing_extensions.TypedDict, total=False):
    subscription: Subscription

@typing.type_check_only
class SubscribeListingRequest(typing_extensions.TypedDict, total=False):
    destinationDataset: DestinationDataset
    destinationPubsubSubscription: DestinationPubSubSubscription

@typing.type_check_only
class SubscribeListingResponse(typing_extensions.TypedDict, total=False):
    subscription: Subscription

@typing.type_check_only
class Subscription(typing_extensions.TypedDict, total=False):
    commercialInfo: GoogleCloudBigqueryAnalyticshubV1SubscriptionCommercialInfo
    creationTime: str
    dataExchange: str
    lastModifyTime: str
    linkedDatasetMap: dict[str, typing.Any]
    linkedResources: _list[LinkedResource]
    listing: str
    name: str
    organizationDisplayName: str
    organizationId: str
    resourceType: typing_extensions.Literal[
        "SHARED_RESOURCE_TYPE_UNSPECIFIED", "BIGQUERY_DATASET", "PUBSUB_TOPIC"
    ]
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "STATE_ACTIVE", "STATE_STALE", "STATE_INACTIVE"
    ]
    subscriberContact: str

@typing.type_check_only
class TestIamPermissionsRequest(typing_extensions.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class TestIamPermissionsResponse(typing_extensions.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class TextConfig(typing_extensions.TypedDict, total=False): ...
