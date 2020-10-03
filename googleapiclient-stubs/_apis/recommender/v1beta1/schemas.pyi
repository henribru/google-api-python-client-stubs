import typing

import typing_extensions

class GoogleCloudRecommenderV1beta1MarkRecommendationFailedRequest(
    typing_extensions.TypedDict, total=False
):
    etag: str
    stateMetadata: typing.Dict[str, typing.Any]

class GoogleCloudRecommenderV1beta1RecommendationContent(
    typing_extensions.TypedDict, total=False
):
    operationGroups: typing.List[GoogleCloudRecommenderV1beta1OperationGroup]

class GoogleCloudRecommenderV1beta1ListInsightsResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    insights: typing.List[GoogleCloudRecommenderV1beta1Insight]

class GoogleCloudRecommenderV1beta1ListRecommendationsResponse(
    typing_extensions.TypedDict, total=False
):
    recommendations: typing.List[GoogleCloudRecommenderV1beta1Recommendation]
    nextPageToken: str

class GoogleCloudRecommenderV1beta1InsightRecommendationReference(
    typing_extensions.TypedDict, total=False
):
    recommendation: str

class GoogleCloudRecommenderV1beta1MarkRecommendationClaimedRequest(
    typing_extensions.TypedDict, total=False
):
    stateMetadata: typing.Dict[str, typing.Any]
    etag: str

class GoogleCloudRecommenderV1beta1MarkRecommendationSucceededRequest(
    typing_extensions.TypedDict, total=False
):
    etag: str
    stateMetadata: typing.Dict[str, typing.Any]

class GoogleCloudRecommenderV1beta1Impact(typing_extensions.TypedDict, total=False):
    costProjection: GoogleCloudRecommenderV1beta1CostProjection
    category: typing_extensions.Literal[
        "CATEGORY_UNSPECIFIED", "COST", "SECURITY", "PERFORMANCE", "MANAGEABILITY"
    ]

class GoogleCloudRecommenderV1beta1Recommendation(
    typing_extensions.TypedDict, total=False
):
    recommenderSubtype: str
    name: str
    additionalImpact: typing.List[GoogleCloudRecommenderV1beta1Impact]
    primaryImpact: GoogleCloudRecommenderV1beta1Impact
    lastRefreshTime: str
    content: GoogleCloudRecommenderV1beta1RecommendationContent
    stateInfo: GoogleCloudRecommenderV1beta1RecommendationStateInfo
    description: str
    etag: str
    associatedInsights: typing.List[
        GoogleCloudRecommenderV1beta1RecommendationInsightReference
    ]

class GoogleCloudRecommenderV1beta1MarkInsightAcceptedRequest(
    typing_extensions.TypedDict, total=False
):
    stateMetadata: typing.Dict[str, typing.Any]
    etag: str

class GoogleCloudRecommenderV1beta1RecommendationStateInfo(
    typing_extensions.TypedDict, total=False
):
    stateMetadata: typing.Dict[str, typing.Any]
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "ACTIVE", "CLAIMED", "SUCCEEDED", "FAILED", "DISMISSED"
    ]

class GoogleCloudRecommenderV1beta1Operation(typing_extensions.TypedDict, total=False):
    resourceType: str
    resource: str
    sourcePath: str
    path: str
    pathFilters: typing.Dict[str, typing.Any]
    value: typing.Any
    pathValueMatchers: typing.Dict[str, typing.Any]
    action: str
    sourceResource: str
    valueMatcher: GoogleCloudRecommenderV1beta1ValueMatcher

class GoogleCloudRecommenderV1beta1ValueMatcher(
    typing_extensions.TypedDict, total=False
):
    matchesPattern: str

class GoogleCloudRecommenderV1beta1CostProjection(
    typing_extensions.TypedDict, total=False
):
    cost: GoogleTypeMoney
    duration: str

class GoogleCloudRecommenderV1beta1OperationGroup(
    typing_extensions.TypedDict, total=False
):
    operations: typing.List[GoogleCloudRecommenderV1beta1Operation]

class GoogleCloudRecommenderV1beta1Insight(typing_extensions.TypedDict, total=False):
    content: typing.Dict[str, typing.Any]
    targetResources: typing.List[str]
    lastRefreshTime: str
    stateInfo: GoogleCloudRecommenderV1beta1InsightStateInfo
    etag: str
    category: typing_extensions.Literal[
        "CATEGORY_UNSPECIFIED", "COST", "SECURITY", "PERFORMANCE", "MANAGEABILITY"
    ]
    associatedRecommendations: typing.List[
        GoogleCloudRecommenderV1beta1InsightRecommendationReference
    ]
    name: str
    observationPeriod: str
    insightSubtype: str
    description: str

class GoogleTypeMoney(typing_extensions.TypedDict, total=False):
    units: str
    currencyCode: str
    nanos: int

class GoogleCloudRecommenderV1beta1InsightStateInfo(
    typing_extensions.TypedDict, total=False
):
    stateMetadata: typing.Dict[str, typing.Any]
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "ACTIVE", "ACCEPTED", "DISMISSED"
    ]

class GoogleCloudRecommenderV1beta1RecommendationInsightReference(
    typing_extensions.TypedDict, total=False
):
    insight: str
