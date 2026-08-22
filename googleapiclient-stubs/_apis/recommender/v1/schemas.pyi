import typing

_list = list

@typing.type_check_only
class GoogleCloudRecommenderV1CostProjection(typing.TypedDict, total=False):
    cost: GoogleTypeMoney
    costInLocalCurrency: GoogleTypeMoney
    duration: str

@typing.type_check_only
class GoogleCloudRecommenderV1Impact(typing.TypedDict, total=False):
    category: typing.Literal[
        "CATEGORY_UNSPECIFIED",
        "COST",
        "SECURITY",
        "PERFORMANCE",
        "MANAGEABILITY",
        "SUSTAINABILITY",
        "RELIABILITY",
    ]
    costProjection: GoogleCloudRecommenderV1CostProjection
    reliabilityProjection: GoogleCloudRecommenderV1ReliabilityProjection
    securityProjection: GoogleCloudRecommenderV1SecurityProjection
    service: str
    sustainabilityProjection: GoogleCloudRecommenderV1SustainabilityProjection

@typing.type_check_only
class GoogleCloudRecommenderV1Insight(typing.TypedDict, total=False):
    associatedRecommendations: _list[
        GoogleCloudRecommenderV1InsightRecommendationReference
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
    stateInfo: GoogleCloudRecommenderV1InsightStateInfo
    targetResources: _list[str]

@typing.type_check_only
class GoogleCloudRecommenderV1InsightRecommendationReference(
    typing.TypedDict, total=False
):
    recommendation: str

@typing.type_check_only
class GoogleCloudRecommenderV1InsightStateInfo(typing.TypedDict, total=False):
    state: typing.Literal["STATE_UNSPECIFIED", "ACTIVE", "ACCEPTED", "DISMISSED"]
    stateMetadata: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudRecommenderV1InsightTypeConfig(typing.TypedDict, total=False):
    annotations: dict[str, typing.Any]
    displayName: str
    etag: str
    insightTypeGenerationConfig: GoogleCloudRecommenderV1InsightTypeGenerationConfig
    name: str
    revisionId: str
    updateTime: str

@typing.type_check_only
class GoogleCloudRecommenderV1InsightTypeGenerationConfig(
    typing.TypedDict, total=False
):
    params: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudRecommenderV1ListInsightsResponse(typing.TypedDict, total=False):
    insights: _list[GoogleCloudRecommenderV1Insight]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudRecommenderV1ListRecommendationsResponse(
    typing.TypedDict, total=False
):
    nextPageToken: str
    recommendations: _list[GoogleCloudRecommenderV1Recommendation]

@typing.type_check_only
class GoogleCloudRecommenderV1MarkInsightAcceptedRequest(typing.TypedDict, total=False):
    etag: str
    stateMetadata: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudRecommenderV1MarkRecommendationClaimedRequest(
    typing.TypedDict, total=False
):
    etag: str
    stateMetadata: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudRecommenderV1MarkRecommendationDismissedRequest(
    typing.TypedDict, total=False
):
    etag: str

@typing.type_check_only
class GoogleCloudRecommenderV1MarkRecommendationFailedRequest(
    typing.TypedDict, total=False
):
    etag: str
    stateMetadata: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudRecommenderV1MarkRecommendationSucceededRequest(
    typing.TypedDict, total=False
):
    etag: str
    stateMetadata: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudRecommenderV1Operation(typing.TypedDict, total=False):
    action: str
    path: str
    pathFilters: dict[str, typing.Any]
    pathValueMatchers: dict[str, typing.Any]
    resource: str
    resourceType: str
    sourcePath: str
    sourceResource: str
    value: typing.Any
    valueMatcher: GoogleCloudRecommenderV1ValueMatcher

@typing.type_check_only
class GoogleCloudRecommenderV1OperationGroup(typing.TypedDict, total=False):
    operations: _list[GoogleCloudRecommenderV1Operation]

@typing.type_check_only
class GoogleCloudRecommenderV1Recommendation(typing.TypedDict, total=False):
    additionalImpact: _list[GoogleCloudRecommenderV1Impact]
    associatedInsights: _list[GoogleCloudRecommenderV1RecommendationInsightReference]
    content: GoogleCloudRecommenderV1RecommendationContent
    description: str
    etag: str
    lastRefreshTime: str
    name: str
    primaryImpact: GoogleCloudRecommenderV1Impact
    priority: typing.Literal["PRIORITY_UNSPECIFIED", "P4", "P3", "P2", "P1"]
    recommenderSubtype: str
    stateInfo: GoogleCloudRecommenderV1RecommendationStateInfo
    targetResources: _list[str]
    xorGroupId: str

@typing.type_check_only
class GoogleCloudRecommenderV1RecommendationContent(typing.TypedDict, total=False):
    operationGroups: _list[GoogleCloudRecommenderV1OperationGroup]
    overview: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudRecommenderV1RecommendationInsightReference(
    typing.TypedDict, total=False
):
    insight: str

@typing.type_check_only
class GoogleCloudRecommenderV1RecommendationStateInfo(typing.TypedDict, total=False):
    state: typing.Literal[
        "STATE_UNSPECIFIED", "ACTIVE", "CLAIMED", "SUCCEEDED", "FAILED", "DISMISSED"
    ]
    stateMetadata: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudRecommenderV1RecommenderConfig(typing.TypedDict, total=False):
    annotations: dict[str, typing.Any]
    displayName: str
    etag: str
    name: str
    recommenderGenerationConfig: GoogleCloudRecommenderV1RecommenderGenerationConfig
    revisionId: str
    updateTime: str

@typing.type_check_only
class GoogleCloudRecommenderV1RecommenderGenerationConfig(
    typing.TypedDict, total=False
):
    params: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudRecommenderV1ReliabilityProjection(typing.TypedDict, total=False):
    details: dict[str, typing.Any]
    risks: _list[
        typing.Literal[
            "RISK_TYPE_UNSPECIFIED", "SERVICE_DISRUPTION", "DATA_LOSS", "ACCESS_DENY"
        ]
    ]

@typing.type_check_only
class GoogleCloudRecommenderV1SecurityProjection(typing.TypedDict, total=False):
    details: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudRecommenderV1SustainabilityProjection(typing.TypedDict, total=False):
    duration: str
    kgCO2e: float

@typing.type_check_only
class GoogleCloudRecommenderV1ValueMatcher(typing.TypedDict, total=False):
    matchesPattern: str

@typing.type_check_only
class GoogleTypeMoney(typing.TypedDict, total=False):
    currencyCode: str
    nanos: int
    units: str
