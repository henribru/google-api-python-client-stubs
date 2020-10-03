import typing

import typing_extensions

class GoogleCloudRecommenderV1Insight(typing_extensions.TypedDict, total=False):
    etag: str
    description: str
    category: typing_extensions.Literal[
        "CATEGORY_UNSPECIFIED", "COST", "SECURITY", "PERFORMANCE", "MANAGEABILITY"
    ]
    name: str
    stateInfo: GoogleCloudRecommenderV1InsightStateInfo
    content: typing.Dict[str, typing.Any]
    targetResources: typing.List[str]
    associatedRecommendations: typing.List[
        GoogleCloudRecommenderV1InsightRecommendationReference
    ]
    insightSubtype: str
    observationPeriod: str
    lastRefreshTime: str

class GoogleCloudRecommenderV1OperationGroup(typing_extensions.TypedDict, total=False):
    operations: typing.List[GoogleCloudRecommenderV1Operation]

class GoogleCloudRecommenderV1ValueMatcher(typing_extensions.TypedDict, total=False):
    matchesPattern: str

class GoogleCloudRecommenderV1ListInsightsResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    insights: typing.List[GoogleCloudRecommenderV1Insight]

class GoogleCloudRecommenderV1MarkInsightAcceptedRequest(
    typing_extensions.TypedDict, total=False
):
    etag: str
    stateMetadata: typing.Dict[str, typing.Any]

class GoogleCloudRecommenderV1CostProjection(typing_extensions.TypedDict, total=False):
    duration: str
    cost: GoogleTypeMoney

class GoogleCloudRecommenderV1Operation(typing_extensions.TypedDict, total=False):
    action: str
    valueMatcher: GoogleCloudRecommenderV1ValueMatcher
    pathFilters: typing.Dict[str, typing.Any]
    resourceType: str
    pathValueMatchers: typing.Dict[str, typing.Any]
    resource: str
    value: typing.Any
    sourceResource: str
    path: str
    sourcePath: str

class GoogleCloudRecommenderV1RecommendationContent(
    typing_extensions.TypedDict, total=False
):
    operationGroups: typing.List[GoogleCloudRecommenderV1OperationGroup]

class GoogleTypeMoney(typing_extensions.TypedDict, total=False):
    nanos: int
    currencyCode: str
    units: str

class GoogleCloudRecommenderV1RecommendationStateInfo(
    typing_extensions.TypedDict, total=False
):
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "ACTIVE", "CLAIMED", "SUCCEEDED", "FAILED", "DISMISSED"
    ]
    stateMetadata: typing.Dict[str, typing.Any]

class GoogleCloudRecommenderV1RecommendationInsightReference(
    typing_extensions.TypedDict, total=False
):
    insight: str

class GoogleCloudRecommenderV1InsightStateInfo(
    typing_extensions.TypedDict, total=False
):
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "ACTIVE", "ACCEPTED", "DISMISSED"
    ]
    stateMetadata: typing.Dict[str, typing.Any]

class GoogleCloudRecommenderV1Impact(typing_extensions.TypedDict, total=False):
    category: typing_extensions.Literal[
        "CATEGORY_UNSPECIFIED", "COST", "SECURITY", "PERFORMANCE", "MANAGEABILITY"
    ]
    costProjection: GoogleCloudRecommenderV1CostProjection

class GoogleCloudRecommenderV1MarkRecommendationFailedRequest(
    typing_extensions.TypedDict, total=False
):
    etag: str
    stateMetadata: typing.Dict[str, typing.Any]

class GoogleCloudRecommenderV1MarkRecommendationSucceededRequest(
    typing_extensions.TypedDict, total=False
):
    etag: str
    stateMetadata: typing.Dict[str, typing.Any]

class GoogleCloudRecommenderV1InsightRecommendationReference(
    typing_extensions.TypedDict, total=False
):
    recommendation: str

class GoogleCloudRecommenderV1MarkRecommendationClaimedRequest(
    typing_extensions.TypedDict, total=False
):
    stateMetadata: typing.Dict[str, typing.Any]
    etag: str

class GoogleCloudRecommenderV1Recommendation(typing_extensions.TypedDict, total=False):
    name: str
    primaryImpact: GoogleCloudRecommenderV1Impact
    associatedInsights: typing.List[
        GoogleCloudRecommenderV1RecommendationInsightReference
    ]
    description: str
    content: GoogleCloudRecommenderV1RecommendationContent
    recommenderSubtype: str
    lastRefreshTime: str
    etag: str
    stateInfo: GoogleCloudRecommenderV1RecommendationStateInfo
    additionalImpact: typing.List[GoogleCloudRecommenderV1Impact]

class GoogleCloudRecommenderV1ListRecommendationsResponse(
    typing_extensions.TypedDict, total=False
):
    recommendations: typing.List[GoogleCloudRecommenderV1Recommendation]
    nextPageToken: str
