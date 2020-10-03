import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class RecommenderResource(googleapiclient.discovery.Resource):
    class ProjectsResource(googleapiclient.discovery.Resource):
        class LocationsResource(googleapiclient.discovery.Resource):
            class InsightTypesResource(googleapiclient.discovery.Resource):
                class InsightsResource(googleapiclient.discovery.Resource):
                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudRecommenderV1ListInsightsResponseHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleCloudRecommenderV1InsightHttpRequest: ...
                    def markAccepted(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudRecommenderV1MarkInsightAcceptedRequest = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudRecommenderV1InsightHttpRequest: ...
                def insights(self) -> InsightsResource: ...
            class RecommendersResource(googleapiclient.discovery.Resource):
                class RecommendationsResource(googleapiclient.discovery.Resource):
                    def markFailed(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudRecommenderV1MarkRecommendationFailedRequest = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudRecommenderV1RecommendationHttpRequest: ...
                    def markClaimed(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudRecommenderV1MarkRecommendationClaimedRequest = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudRecommenderV1RecommendationHttpRequest: ...
                    def markSucceeded(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudRecommenderV1MarkRecommendationSucceededRequest = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudRecommenderV1RecommendationHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudRecommenderV1ListRecommendationsResponseHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleCloudRecommenderV1RecommendationHttpRequest: ...
                def recommendations(self) -> RecommendationsResource: ...
            def insightTypes(self) -> InsightTypesResource: ...
            def recommenders(self) -> RecommendersResource: ...
        def locations(self) -> LocationsResource: ...
    def projects(self) -> ProjectsResource: ...

class GoogleCloudRecommenderV1ListInsightsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudRecommenderV1ListInsightsResponse: ...

class GoogleCloudRecommenderV1RecommendationHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudRecommenderV1Recommendation: ...

class GoogleCloudRecommenderV1InsightHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudRecommenderV1Insight: ...

class GoogleCloudRecommenderV1ListRecommendationsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudRecommenderV1ListRecommendationsResponse: ...
