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
                    def markAccepted(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudRecommenderV1beta1MarkInsightAcceptedRequest = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudRecommenderV1beta1InsightHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        pageToken: str = ...,
                        pageSize: int = ...,
                        filter: str = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudRecommenderV1beta1ListInsightsResponseHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleCloudRecommenderV1beta1InsightHttpRequest: ...
                def insights(self) -> InsightsResource: ...
            class RecommendersResource(googleapiclient.discovery.Resource):
                class RecommendationsResource(googleapiclient.discovery.Resource):
                    def markSucceeded(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudRecommenderV1beta1MarkRecommendationSucceededRequest = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudRecommenderV1beta1RecommendationHttpRequest: ...
                    def markFailed(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudRecommenderV1beta1MarkRecommendationFailedRequest = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudRecommenderV1beta1RecommendationHttpRequest: ...
                    def markClaimed(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudRecommenderV1beta1MarkRecommendationClaimedRequest = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudRecommenderV1beta1RecommendationHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleCloudRecommenderV1beta1RecommendationHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        pageSize: int = ...,
                        filter: str = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudRecommenderV1beta1ListRecommendationsResponseHttpRequest: ...
                def recommendations(self) -> RecommendationsResource: ...
            def insightTypes(self) -> InsightTypesResource: ...
            def recommenders(self) -> RecommendersResource: ...
        def locations(self) -> LocationsResource: ...
    def projects(self) -> ProjectsResource: ...

class GoogleCloudRecommenderV1beta1RecommendationHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudRecommenderV1beta1Recommendation: ...

class GoogleCloudRecommenderV1beta1ListRecommendationsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudRecommenderV1beta1ListRecommendationsResponse: ...

class GoogleCloudRecommenderV1beta1InsightHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudRecommenderV1beta1Insight: ...

class GoogleCloudRecommenderV1beta1ListInsightsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudRecommenderV1beta1ListInsightsResponse: ...
