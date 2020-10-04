import typing

import typing_extensions
@typing.type_check_only
class GoogleCloudRecommenderV1beta1CostProjection(
    typing_extensions.TypedDict, total=False
):
    cost: GoogleTypeMoney
    duration: str

@typing.type_check_only
class GoogleCloudRecommenderV1beta1Impact(typing_extensions.TypedDict, total=False):
    category: typing_extensions.Literal[
        "CATEGORY_UNSPECIFIED", "COST", "SECURITY", "PERFORMANCE", "MANAGEABILITY"
    ]
    costProjection: GoogleCloudRecommenderV1beta1CostProjection

@typing.type_check_only
class GoogleCloudRecommenderV1beta1Insight(typing_extensions.TypedDict, total=False):
    associatedRecommendations: typing.List[
        GoogleCloudRecommenderV1beta1InsightRecommendationReference
    ]
    category: typing_extensions.Literal[
        "CATEGORY_UNSPECIFIED", "COST", "SECURITY", "PERFORMANCE", "MANAGEABILITY"
    ]
    content: typing.Dict[str, typing.Any]
    description: str
    etag: str
    insightSubtype: str
    lastRefreshTime: str
    name: str
    observationPeriod: str
    stateInfo: GoogleCloudRecommenderV1beta1InsightStateInfo
    targetResources: typing.List[str]

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
    stateMetadata: typing.Dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudRecommenderV1beta1ListInsightsResponse(
    typing_extensions.TypedDict, total=False
):
    insights: typing.List[GoogleCloudRecommenderV1beta1Insight]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudRecommenderV1beta1ListRecommendationsResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    recommendations: typing.List[GoogleCloudRecommenderV1beta1Recommendation]

@typing.type_check_only
class GoogleCloudRecommenderV1beta1MarkInsightAcceptedRequest(
    typing_extensions.TypedDict, total=False
):
    etag: str
    stateMetadata: typing.Dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudRecommenderV1beta1MarkRecommendationClaimedRequest(
    typing_extensions.TypedDict, total=False
):
    etag: str
    stateMetadata: typing.Dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudRecommenderV1beta1MarkRecommendationFailedRequest(
    typing_extensions.TypedDict, total=False
):
    etag: str
    stateMetadata: typing.Dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudRecommenderV1beta1MarkRecommendationSucceededRequest(
    typing_extensions.TypedDict, total=False
):
    etag: str
    stateMetadata: typing.Dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudRecommenderV1beta1Operation(typing_extensions.TypedDict, total=False):
    action: str
    path: str
    pathFilters: typing.Dict[str, typing.Any]
    pathValueMatchers: typing.Dict[str, typing.Any]
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
    operations: typing.List[GoogleCloudRecommenderV1beta1Operation]

@typing.type_check_only
class GoogleCloudRecommenderV1beta1Recommendation(
    typing_extensions.TypedDict, total=False
):
    additionalImpact: typing.List[GoogleCloudRecommenderV1beta1Impact]
    associatedInsights: typing.List[
        GoogleCloudRecommenderV1beta1RecommendationInsightReference
    ]
    content: GoogleCloudRecommenderV1beta1RecommendationContent
    description: str
    etag: str
    lastRefreshTime: str
    name: str
    primaryImpact: GoogleCloudRecommenderV1beta1Impact
    recommenderSubtype: str
    stateInfo: GoogleCloudRecommenderV1beta1RecommendationStateInfo

@typing.type_check_only
class GoogleCloudRecommenderV1beta1RecommendationContent(
    typing_extensions.TypedDict, total=False
):
    operationGroups: typing.List[GoogleCloudRecommenderV1beta1OperationGroup]

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
    stateMetadata: typing.Dict[str, typing.Any]

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
