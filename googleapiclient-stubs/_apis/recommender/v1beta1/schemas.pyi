import typing

_list = list

@typing.type_check_only
class GoogleCloudLocationListLocationsResponse(typing.TypedDict, total=False):
    locations: _list[GoogleCloudLocationLocation]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudLocationLocation(typing.TypedDict, total=False):
    displayName: str
    labels: dict[str, typing.Any]
    locationId: str
    metadata: dict[str, typing.Any]
    name: str

@typing.type_check_only
class GoogleCloudRecommenderV1beta1CostProjection(typing.TypedDict, total=False):
    cost: GoogleTypeMoney
    costInLocalCurrency: GoogleTypeMoney
    duration: str
    pricingType: typing.Literal[
        "PRICING_TYPE_UNSPECIFIED", "LIST_PRICE", "CUSTOM_PRICE"
    ]

@typing.type_check_only
class GoogleCloudRecommenderV1beta1Impact(typing.TypedDict, total=False):
    category: typing.Literal[
        "CATEGORY_UNSPECIFIED",
        "COST",
        "SECURITY",
        "PERFORMANCE",
        "MANAGEABILITY",
        "SUSTAINABILITY",
        "RELIABILITY",
    ]
    costProjection: GoogleCloudRecommenderV1beta1CostProjection
    reliabilityProjection: GoogleCloudRecommenderV1beta1ReliabilityProjection
    securityProjection: GoogleCloudRecommenderV1beta1SecurityProjection
    service: str
    sustainabilityProjection: GoogleCloudRecommenderV1beta1SustainabilityProjection

@typing.type_check_only
class GoogleCloudRecommenderV1beta1Insight(typing.TypedDict, total=False):
    associatedRecommendations: _list[
        GoogleCloudRecommenderV1beta1InsightRecommendationReference
    ]
    category: typing.Literal[
        "CATEGORY_UNSPECIFIED",
        "COST",
        "SECURITY",
        "PERFORMANCE",
        "MANAGEABILITY",
        "SUSTAINABILITY",
        "RELIABILITY",
    ]
    content: dict[str, typing.Any]
    description: str
    etag: str
    insightSubtype: str
    lastRefreshTime: str
    name: str
    observationPeriod: str
    severity: typing.Literal[
        "SEVERITY_UNSPECIFIED", "LOW", "MEDIUM", "HIGH", "CRITICAL"
    ]
    stateInfo: GoogleCloudRecommenderV1beta1InsightStateInfo
    targetResources: _list[str]

@typing.type_check_only
class GoogleCloudRecommenderV1beta1InsightRecommendationReference(
    typing.TypedDict, total=False
):
    recommendation: str

@typing.type_check_only
class GoogleCloudRecommenderV1beta1InsightStateInfo(typing.TypedDict, total=False):
    state: typing.Literal["STATE_UNSPECIFIED", "ACTIVE", "ACCEPTED", "DISMISSED"]
    stateMetadata: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudRecommenderV1beta1InsightType(typing.TypedDict, total=False):
    name: str

@typing.type_check_only
class GoogleCloudRecommenderV1beta1InsightTypeConfig(typing.TypedDict, total=False):
    annotations: dict[str, typing.Any]
    displayName: str
    etag: str
    insightTypeGenerationConfig: (
        GoogleCloudRecommenderV1beta1InsightTypeGenerationConfig
    )
    name: str
    revisionId: str
    updateTime: str

@typing.type_check_only
class GoogleCloudRecommenderV1beta1InsightTypeGenerationConfig(
    typing.TypedDict, total=False
):
    params: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudRecommenderV1beta1ListInsightTypesResponse(
    typing.TypedDict, total=False
):
    insightTypes: _list[GoogleCloudRecommenderV1beta1InsightType]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudRecommenderV1beta1ListInsightsResponse(typing.TypedDict, total=False):
    insights: _list[GoogleCloudRecommenderV1beta1Insight]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudRecommenderV1beta1ListRecommendationsResponse(
    typing.TypedDict, total=False
):
    nextPageToken: str
    recommendations: _list[GoogleCloudRecommenderV1beta1Recommendation]

@typing.type_check_only
class GoogleCloudRecommenderV1beta1ListRecommendersResponse(
    typing.TypedDict, total=False
):
    nextPageToken: str
    recommenders: _list[GoogleCloudRecommenderV1beta1RecommenderType]

@typing.type_check_only
class GoogleCloudRecommenderV1beta1MarkInsightAcceptedRequest(
    typing.TypedDict, total=False
):
    etag: str
    stateMetadata: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudRecommenderV1beta1MarkRecommendationClaimedRequest(
    typing.TypedDict, total=False
):
    etag: str
    stateMetadata: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudRecommenderV1beta1MarkRecommendationDismissedRequest(
    typing.TypedDict, total=False
):
    etag: str

@typing.type_check_only
class GoogleCloudRecommenderV1beta1MarkRecommendationFailedRequest(
    typing.TypedDict, total=False
):
    etag: str
    stateMetadata: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudRecommenderV1beta1MarkRecommendationSucceededRequest(
    typing.TypedDict, total=False
):
    etag: str
    stateMetadata: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudRecommenderV1beta1Operation(typing.TypedDict, total=False):
    action: str
    path: str
    pathFilters: dict[str, typing.Any]
    pathValueMatchers: dict[str, typing.Any]
    resource: str
    resourceType: str
    sourcePath: str
    sourceResource: str
    value: typing.Any
    valueMatcher: GoogleCloudRecommenderV1beta1ValueMatcher

@typing.type_check_only
class GoogleCloudRecommenderV1beta1OperationGroup(typing.TypedDict, total=False):
    operations: _list[GoogleCloudRecommenderV1beta1Operation]

@typing.type_check_only
class GoogleCloudRecommenderV1beta1Recommendation(typing.TypedDict, total=False):
    additionalImpact: _list[GoogleCloudRecommenderV1beta1Impact]
    associatedInsights: _list[
        GoogleCloudRecommenderV1beta1RecommendationInsightReference
    ]
    content: GoogleCloudRecommenderV1beta1RecommendationContent
    description: str
    etag: str
    lastRefreshTime: str
    name: str
    primaryImpact: GoogleCloudRecommenderV1beta1Impact
    priority: typing.Literal["PRIORITY_UNSPECIFIED", "P4", "P3", "P2", "P1"]
    recommenderSubtype: str
    stateInfo: GoogleCloudRecommenderV1beta1RecommendationStateInfo
    targetResources: _list[str]
    xorGroupId: str

@typing.type_check_only
class GoogleCloudRecommenderV1beta1RecommendationContent(typing.TypedDict, total=False):
    operationGroups: _list[GoogleCloudRecommenderV1beta1OperationGroup]
    overview: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudRecommenderV1beta1RecommendationInsightReference(
    typing.TypedDict, total=False
):
    insight: str

@typing.type_check_only
class GoogleCloudRecommenderV1beta1RecommendationStateInfo(
    typing.TypedDict, total=False
):
    state: typing.Literal[
        "STATE_UNSPECIFIED", "ACTIVE", "CLAIMED", "SUCCEEDED", "FAILED", "DISMISSED"
    ]
    stateMetadata: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudRecommenderV1beta1RecommenderConfig(typing.TypedDict, total=False):
    annotations: dict[str, typing.Any]
    displayName: str
    etag: str
    name: str
    recommenderGenerationConfig: (
        GoogleCloudRecommenderV1beta1RecommenderGenerationConfig
    )
    revisionId: str
    updateTime: str

@typing.type_check_only
class GoogleCloudRecommenderV1beta1RecommenderGenerationConfig(
    typing.TypedDict, total=False
):
    params: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudRecommenderV1beta1RecommenderType(typing.TypedDict, total=False):
    name: str

@typing.type_check_only
class GoogleCloudRecommenderV1beta1ReliabilityProjection(typing.TypedDict, total=False):
    details: dict[str, typing.Any]
    risks: _list[
        typing.Literal[
            "RISK_TYPE_UNSPECIFIED", "SERVICE_DISRUPTION", "DATA_LOSS", "ACCESS_DENY"
        ]
    ]

@typing.type_check_only
class GoogleCloudRecommenderV1beta1SecurityProjection(typing.TypedDict, total=False):
    details: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudRecommenderV1beta1SustainabilityProjection(
    typing.TypedDict, total=False
):
    duration: str
    kgCO2e: float

@typing.type_check_only
class GoogleCloudRecommenderV1beta1ValueMatcher(typing.TypedDict, total=False):
    matchesPattern: str

@typing.type_check_only
class GoogleTypeMoney(typing.TypedDict, total=False):
    currencyCode: str
    nanos: int
    units: str
