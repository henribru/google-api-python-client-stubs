import typing

_list = list

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
class BigQueryDatasetSource(typing.TypedDict, total=False):
    dataset: str

@typing.type_check_only
class Binding(typing.TypedDict, total=False):
    condition: Expr
    members: _list[str]
    role: str

@typing.type_check_only
class CommercialInfo(typing.TypedDict, total=False):
    cloudMarketplace: GoogleCloudMarketplaceInfo

@typing.type_check_only
class DataExchange(typing.TypedDict, total=False):
    description: str
    displayName: str
    documentation: str
    icon: str
    listingCount: int
    name: str
    primaryContact: str

@typing.type_check_only
class DataProvider(typing.TypedDict, total=False):
    name: str
    primaryContact: str

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
class Empty(typing.TypedDict, total=False): ...

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
class GoogleCloudBigqueryDataexchangeV1beta1DestinationDataset(
    typing.TypedDict, total=False
):
    datasetReference: GoogleCloudBigqueryDataexchangeV1beta1DestinationDatasetReference
    description: str
    friendlyName: str
    labels: dict[str, typing.Any]
    location: str

@typing.type_check_only
class GoogleCloudBigqueryDataexchangeV1beta1DestinationDatasetReference(
    typing.TypedDict, total=False
):
    datasetId: str
    projectId: str

@typing.type_check_only
class GoogleCloudMarketplaceInfo(typing.TypedDict, total=False):
    order: str

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
    dataProvider: DataProvider
    description: str
    displayName: str
    documentation: str
    icon: str
    name: str
    primaryContact: str
    publisher: Publisher
    requestAccess: str
    restrictedExportConfig: RestrictedExportConfig
    state: typing.Literal["STATE_UNSPECIFIED", "ACTIVE"]

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
class Publisher(typing.TypedDict, total=False):
    name: str
    primaryContact: str

@typing.type_check_only
class RefreshSubscriptionResponse(typing.TypedDict, total=False):
    subscription: Subscription

@typing.type_check_only
class RestrictedExportConfig(typing.TypedDict, total=False):
    enabled: bool
    restrictDirectTableAccess: bool
    restrictQueryResult: bool

@typing.type_check_only
class SetIamPolicyRequest(typing.TypedDict, total=False):
    policy: Policy
    updateMask: str

@typing.type_check_only
class SubscribeDataExchangeResponse(typing.TypedDict, total=False):
    subscription: Subscription

@typing.type_check_only
class SubscribeListingRequest(typing.TypedDict, total=False):
    destinationDataset: GoogleCloudBigqueryDataexchangeV1beta1DestinationDataset

@typing.type_check_only
class SubscribeListingResponse(typing.TypedDict, total=False): ...

@typing.type_check_only
class Subscription(typing.TypedDict, total=False):
    commercialInfo: CommercialInfo
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
