import typing

import typing_extensions

_list = list

@typing.type_check_only
class GoogleCloudRecommenderV1CostProjection(typing_extensions.TypedDict, total=False):
    cost: GoogleTypeMoney
    duration: str

@typing.type_check_only
class GoogleCloudRecommenderV1Impact(typing_extensions.TypedDict, total=False):
    category: typing_extensions.Literal[
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
    sustainabilityProjection: GoogleCloudRecommenderV1SustainabilityProjection

@typing.type_check_only
class GoogleCloudRecommenderV1Insight(typing_extensions.TypedDict, total=False):
    associatedRecommendations: _list[
        GoogleCloudRecommenderV1InsightRecommendationReference
    ]
    category: typing_extensions.Literal[
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
    severity: typing_extensions.Literal[
        "SEVERITY_UNSPECIFIED", "LOW", "MEDIUM", "HIGH", "CRITICAL"
    ]
    stateInfo: GoogleCloudRecommenderV1InsightStateInfo
    targetResources: _list[str]

@typing.type_check_only
class GoogleCloudRecommenderV1InsightRecommendationReference(
    typing_extensions.TypedDict, total=False
):
    recommendation: str

@typing.type_check_only
class GoogleCloudRecommenderV1InsightStateInfo(
    typing_extensions.TypedDict, total=False
):
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "ACTIVE", "ACCEPTED", "DISMISSED"
    ]
    stateMetadata: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudRecommenderV1InsightTypeConfig(
    typing_extensions.TypedDict, total=False
):
    annotations: dict[str, typing.Any]
    displayName: str
    etag: str
    insightTypeGenerationConfig: GoogleCloudRecommenderV1InsightTypeGenerationConfig
    name: str
    revisionId: str
    updateTime: str

@typing.type_check_only
class GoogleCloudRecommenderV1InsightTypeGenerationConfig(
    typing_extensions.TypedDict, total=False
):
    params: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudRecommenderV1ListInsightsResponse(
    typing_extensions.TypedDict, total=False
):
    insights: _list[GoogleCloudRecommenderV1Insight]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudRecommenderV1ListRecommendationsResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    recommendations: _list[GoogleCloudRecommenderV1Recommendation]

@typing.type_check_only
class GoogleCloudRecommenderV1MarkInsightAcceptedRequest(
    typing_extensions.TypedDict, total=False
):
    etag: str
    stateMetadata: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudRecommenderV1MarkRecommendationClaimedRequest(
    typing_extensions.TypedDict, total=False
):
    etag: str
    stateMetadata: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudRecommenderV1MarkRecommendationFailedRequest(
    typing_extensions.TypedDict, total=False
):
    etag: str
    stateMetadata: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudRecommenderV1MarkRecommendationSucceededRequest(
    typing_extensions.TypedDict, total=False
):
    etag: str
    stateMetadata: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudRecommenderV1Operation(typing_extensions.TypedDict, total=False):
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
class GoogleCloudRecommenderV1OperationGroup(typing_extensions.TypedDict, total=False):
    operations: _list[GoogleCloudRecommenderV1Operation]

@typing.type_check_only
class GoogleCloudRecommenderV1Recommendation(typing_extensions.TypedDict, total=False):
    additionalImpact: _list[GoogleCloudRecommenderV1Impact]
    associatedInsights: _list[GoogleCloudRecommenderV1RecommendationInsightReference]
    content: GoogleCloudRecommenderV1RecommendationContent
    description: str
    etag: str
    lastRefreshTime: str
    name: str
    primaryImpact: GoogleCloudRecommenderV1Impact
    priority: typing_extensions.Literal["PRIORITY_UNSPECIFIED", "P4", "P3", "P2", "P1"]
    recommenderSubtype: str
    stateInfo: GoogleCloudRecommenderV1RecommendationStateInfo
    xorGroupId: str

@typing.type_check_only
class GoogleCloudRecommenderV1RecommendationContent(
    typing_extensions.TypedDict, total=False
):
    operationGroups: _list[GoogleCloudRecommenderV1OperationGroup]
    overview: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudRecommenderV1RecommendationInsightReference(
    typing_extensions.TypedDict, total=False
):
    insight: str

@typing.type_check_only
class GoogleCloudRecommenderV1RecommendationStateInfo(
    typing_extensions.TypedDict, total=False
):
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "ACTIVE", "CLAIMED", "SUCCEEDED", "FAILED", "DISMISSED"
    ]
    stateMetadata: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudRecommenderV1RecommenderConfig(
    typing_extensions.TypedDict, total=False
):
    annotations: dict[str, typing.Any]
    displayName: str
    etag: str
    name: str
    recommenderGenerationConfig: GoogleCloudRecommenderV1RecommenderGenerationConfig
    revisionId: str
    updateTime: str

@typing.type_check_only
class GoogleCloudRecommenderV1RecommenderGenerationConfig(
    typing_extensions.TypedDict, total=False
):
    params: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudRecommenderV1ReliabilityProjection(
    typing_extensions.TypedDict, total=False
):
    details: dict[str, typing.Any]
    risks: _list[str]

@typing.type_check_only
class GoogleCloudRecommenderV1SecurityProjection(
    typing_extensions.TypedDict, total=False
):
    details: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudRecommenderV1SustainabilityProjection(
    typing_extensions.TypedDict, total=False
):
    duration: str
    kgCO2e: float

@typing.type_check_only
class GoogleCloudRecommenderV1ValueMatcher(typing_extensions.TypedDict, total=False):
    matchesPattern: str

@typing.type_check_only
class GoogleTypeMoney(typing_extensions.TypedDict, total=False):
    currencyCode: str
    nanos: int
    units: str
