import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *
@typing.type_check_only
class RecommenderResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class BillingAccountsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class LocationsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class InsightTypesResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class InsightsResource(googleapiclient.discovery.Resource):
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleCloudRecommenderV1InsightHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudRecommenderV1ListInsightsResponseHttpRequest: ...
                    def markAccepted(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudRecommenderV1MarkInsightAcceptedRequest = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudRecommenderV1InsightHttpRequest: ...
                def insights(self) -> InsightsResource: ...
            @typing.type_check_only
            class RecommendersResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class RecommendationsResource(googleapiclient.discovery.Resource):
                    def get(
                        self, *, name: str, **kwargs: typing.Any
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
                    def markClaimed(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudRecommenderV1MarkRecommendationClaimedRequest = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudRecommenderV1RecommendationHttpRequest: ...
                    def markFailed(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudRecommenderV1MarkRecommendationFailedRequest = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudRecommenderV1RecommendationHttpRequest: ...
                    def markSucceeded(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudRecommenderV1MarkRecommendationSucceededRequest = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudRecommenderV1RecommendationHttpRequest: ...
                def recommendations(self) -> RecommendationsResource: ...
            def insightTypes(self) -> InsightTypesResource: ...
            def recommenders(self) -> RecommendersResource: ...
        def locations(self) -> LocationsResource: ...
    @typing.type_check_only
    class FoldersResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class LocationsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class InsightTypesResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class InsightsResource(googleapiclient.discovery.Resource):
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleCloudRecommenderV1InsightHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudRecommenderV1ListInsightsResponseHttpRequest: ...
                    def markAccepted(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudRecommenderV1MarkInsightAcceptedRequest = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudRecommenderV1InsightHttpRequest: ...
                def insights(self) -> InsightsResource: ...
            @typing.type_check_only
            class RecommendersResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class RecommendationsResource(googleapiclient.discovery.Resource):
                    def get(
                        self, *, name: str, **kwargs: typing.Any
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
                    def markClaimed(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudRecommenderV1MarkRecommendationClaimedRequest = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudRecommenderV1RecommendationHttpRequest: ...
                    def markFailed(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudRecommenderV1MarkRecommendationFailedRequest = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudRecommenderV1RecommendationHttpRequest: ...
                    def markSucceeded(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudRecommenderV1MarkRecommendationSucceededRequest = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudRecommenderV1RecommendationHttpRequest: ...
                def recommendations(self) -> RecommendationsResource: ...
            def insightTypes(self) -> InsightTypesResource: ...
            def recommenders(self) -> RecommendersResource: ...
        def locations(self) -> LocationsResource: ...
    @typing.type_check_only
    class OrganizationsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class LocationsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class InsightTypesResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class InsightsResource(googleapiclient.discovery.Resource):
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleCloudRecommenderV1InsightHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudRecommenderV1ListInsightsResponseHttpRequest: ...
                    def markAccepted(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudRecommenderV1MarkInsightAcceptedRequest = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudRecommenderV1InsightHttpRequest: ...
                def insights(self) -> InsightsResource: ...
            @typing.type_check_only
            class RecommendersResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class RecommendationsResource(googleapiclient.discovery.Resource):
                    def get(
                        self, *, name: str, **kwargs: typing.Any
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
                    def markClaimed(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudRecommenderV1MarkRecommendationClaimedRequest = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudRecommenderV1RecommendationHttpRequest: ...
                    def markFailed(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudRecommenderV1MarkRecommendationFailedRequest = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudRecommenderV1RecommendationHttpRequest: ...
                    def markSucceeded(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudRecommenderV1MarkRecommendationSucceededRequest = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudRecommenderV1RecommendationHttpRequest: ...
                def recommendations(self) -> RecommendationsResource: ...
            def insightTypes(self) -> InsightTypesResource: ...
            def recommenders(self) -> RecommendersResource: ...
        def locations(self) -> LocationsResource: ...
    @typing.type_check_only
    class ProjectsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class LocationsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class InsightTypesResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class InsightsResource(googleapiclient.discovery.Resource):
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleCloudRecommenderV1InsightHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudRecommenderV1ListInsightsResponseHttpRequest: ...
                    def markAccepted(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudRecommenderV1MarkInsightAcceptedRequest = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudRecommenderV1InsightHttpRequest: ...
                def insights(self) -> InsightsResource: ...
            @typing.type_check_only
            class RecommendersResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class RecommendationsResource(googleapiclient.discovery.Resource):
                    def get(
                        self, *, name: str, **kwargs: typing.Any
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
                    def markClaimed(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudRecommenderV1MarkRecommendationClaimedRequest = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudRecommenderV1RecommendationHttpRequest: ...
                    def markFailed(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudRecommenderV1MarkRecommendationFailedRequest = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudRecommenderV1RecommendationHttpRequest: ...
                    def markSucceeded(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudRecommenderV1MarkRecommendationSucceededRequest = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudRecommenderV1RecommendationHttpRequest: ...
                def recommendations(self) -> RecommendationsResource: ...
            def insightTypes(self) -> InsightTypesResource: ...
            def recommenders(self) -> RecommendersResource: ...
        def locations(self) -> LocationsResource: ...
    def billingAccounts(self) -> BillingAccountsResource: ...
    def folders(self) -> FoldersResource: ...
    def organizations(self) -> OrganizationsResource: ...
    def projects(self) -> ProjectsResource: ...

@typing.type_check_only
class GoogleCloudRecommenderV1InsightHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleCloudRecommenderV1Insight: ...

@typing.type_check_only
class GoogleCloudRecommenderV1ListInsightsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleCloudRecommenderV1ListInsightsResponse: ...

@typing.type_check_only
class GoogleCloudRecommenderV1ListRecommendationsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleCloudRecommenderV1ListRecommendationsResponse: ...

@typing.type_check_only
class GoogleCloudRecommenderV1RecommendationHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleCloudRecommenderV1Recommendation: ...
