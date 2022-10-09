import typing

import typing_extensions

_list = list

@typing.type_check_only
class GoogleCloudRecommenderV1beta1CostProjection(
    typing_extensions.TypedDict, total=False
):
    cost: GoogleTypeMoney
    duration: str

@typing.type_check_only
class GoogleCloudRecommenderV1beta1Impact(typing_extensions.TypedDict, total=False):
    category: typing_extensions.Literal[
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
    sustainabilityProjection: GoogleCloudRecommenderV1beta1SustainabilityProjection

@typing.type_check_only
class GoogleCloudRecommenderV1beta1Insight(typing_extensions.TypedDict, total=False):
    associatedRecommendations: _list[
        GoogleCloudRecommenderV1beta1InsightRecommendationReference
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
    stateInfo: GoogleCloudRecommenderV1beta1InsightStateInfo
    targetResources: _list[str]

@typing.type_check_only
class GoogleCloudRecommenderV1beta1InsightRecommendationReference(
    typing_extensions.TypedDict, total=False
):
    recommendation: str

@typing.type_check_only
class GoogleCloudRecommenderV1beta1InsightStateInfo(
    typing_extensions.TypedDict, total=False
):
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "ACTIVE", "ACCEPTED", "DISMISSED"
    ]
    stateMetadata: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudRecommenderV1beta1InsightTypeConfig(
    typing_extensions.TypedDict, total=False
):
    annotations: dict[str, typing.Any]
    displayName: str
    etag: str
    insightTypeGenerationConfig: GoogleCloudRecommenderV1beta1InsightTypeGenerationConfig
    name: str
    revisionId: str
    updateTime: str

@typing.type_check_only
class GoogleCloudRecommenderV1beta1InsightTypeGenerationConfig(
    typing_extensions.TypedDict, total=False
):
    params: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudRecommenderV1beta1ListInsightsResponse(
    typing_extensions.TypedDict, total=False
):
    insights: _list[GoogleCloudRecommenderV1beta1Insight]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudRecommenderV1beta1ListRecommendationsResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    recommendations: _list[GoogleCloudRecommenderV1beta1Recommendation]

@typing.type_check_only
class GoogleCloudRecommenderV1beta1MarkInsightAcceptedRequest(
    typing_extensions.TypedDict, total=False
):
    etag: str
    stateMetadata: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudRecommenderV1beta1MarkRecommendationClaimedRequest(
    typing_extensions.TypedDict, total=False
):
    etag: str
    stateMetadata: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudRecommenderV1beta1MarkRecommendationFailedRequest(
    typing_extensions.TypedDict, total=False
):
    etag: str
    stateMetadata: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudRecommenderV1beta1MarkRecommendationSucceededRequest(
    typing_extensions.TypedDict, total=False
):
    etag: str
    stateMetadata: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudRecommenderV1beta1Operation(typing_extensions.TypedDict, total=False):
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
class GoogleCloudRecommenderV1beta1OperationGroup(
    typing_extensions.TypedDict, total=False
):
    operations: _list[GoogleCloudRecommenderV1beta1Operation]

@typing.type_check_only
class GoogleCloudRecommenderV1beta1Recommendation(
    typing_extensions.TypedDict, total=False
):
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
    priority: typing_extensions.Literal["PRIORITY_UNSPECIFIED", "P4", "P3", "P2", "P1"]
    recommenderSubtype: str
    stateInfo: GoogleCloudRecommenderV1beta1RecommendationStateInfo
    xorGroupId: str

@typing.type_check_only
class GoogleCloudRecommenderV1beta1RecommendationContent(
    typing_extensions.TypedDict, total=False
):
    operationGroups: _list[GoogleCloudRecommenderV1beta1OperationGroup]
    overview: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudRecommenderV1beta1RecommendationInsightReference(
    typing_extensions.TypedDict, total=False
):
    insight: str

@typing.type_check_only
class GoogleCloudRecommenderV1beta1RecommendationStateInfo(
    typing_extensions.TypedDict, total=False
):
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "ACTIVE", "CLAIMED", "SUCCEEDED", "FAILED", "DISMISSED"
    ]
    stateMetadata: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudRecommenderV1beta1RecommenderConfig(
    typing_extensions.TypedDict, total=False
):
    annotations: dict[str, typing.Any]
    displayName: str
    etag: str
    name: str
    recommenderGenerationConfig: GoogleCloudRecommenderV1beta1RecommenderGenerationConfig
    revisionId: str
    updateTime: str

@typing.type_check_only
class GoogleCloudRecommenderV1beta1RecommenderGenerationConfig(
    typing_extensions.TypedDict, total=False
):
    params: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudRecommenderV1beta1ReliabilityProjection(
    typing_extensions.TypedDict, total=False
):
    details: dict[str, typing.Any]
    risks: _list[str]

@typing.type_check_only
class GoogleCloudRecommenderV1beta1SecurityProjection(
    typing_extensions.TypedDict, total=False
):
    details: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudRecommenderV1beta1SustainabilityProjection(
    typing_extensions.TypedDict, total=False
):
    duration: str
    kgCO2e: float

@typing.type_check_only
class GoogleCloudRecommenderV1beta1ValueMatcher(
    typing_extensions.TypedDict, total=False
):
    matchesPattern: str

@typing.type_check_only
class GoogleTypeMoney(typing_extensions.TypedDict, total=False):
    currencyCode: str
    nanos: int
    units: str
