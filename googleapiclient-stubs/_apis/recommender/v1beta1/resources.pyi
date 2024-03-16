import collections.abc
import typing

import httplib2
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http

from .schemas import *

_list = list

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
                    ) -> GoogleCloudRecommenderV1beta1InsightHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
                    ) -> (
                        GoogleCloudRecommenderV1beta1ListInsightsResponseHttpRequest
                    ): ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudRecommenderV1beta1ListInsightsResponseHttpRequest,
                        previous_response: GoogleCloudRecommenderV1beta1ListInsightsResponse,
                    ) -> (
                        GoogleCloudRecommenderV1beta1ListInsightsResponseHttpRequest
                        | None
                    ): ...
                    def markAccepted(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudRecommenderV1beta1MarkInsightAcceptedRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudRecommenderV1beta1InsightHttpRequest: ...

                def getConfig(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudRecommenderV1beta1InsightTypeConfigHttpRequest: ...
                def updateConfig(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudRecommenderV1beta1InsightTypeConfig = ...,
                    updateMask: str = ...,
                    validateOnly: bool = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudRecommenderV1beta1InsightTypeConfigHttpRequest: ...
                def insights(self) -> InsightsResource: ...

            @typing.type_check_only
            class RecommendersResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class RecommendationsResource(googleapiclient.discovery.Resource):
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleCloudRecommenderV1beta1RecommendationHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudRecommenderV1beta1ListRecommendationsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudRecommenderV1beta1ListRecommendationsResponseHttpRequest,
                        previous_response: GoogleCloudRecommenderV1beta1ListRecommendationsResponse,
                    ) -> (
                        GoogleCloudRecommenderV1beta1ListRecommendationsResponseHttpRequest
                        | None
                    ): ...
                    def markClaimed(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudRecommenderV1beta1MarkRecommendationClaimedRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudRecommenderV1beta1RecommendationHttpRequest: ...
                    def markDismissed(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudRecommenderV1beta1MarkRecommendationDismissedRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudRecommenderV1beta1RecommendationHttpRequest: ...
                    def markFailed(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudRecommenderV1beta1MarkRecommendationFailedRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudRecommenderV1beta1RecommendationHttpRequest: ...
                    def markSucceeded(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudRecommenderV1beta1MarkRecommendationSucceededRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudRecommenderV1beta1RecommendationHttpRequest: ...

                def getConfig(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudRecommenderV1beta1RecommenderConfigHttpRequest: ...
                def updateConfig(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudRecommenderV1beta1RecommenderConfig = ...,
                    updateMask: str = ...,
                    validateOnly: bool = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudRecommenderV1beta1RecommenderConfigHttpRequest: ...
                def recommendations(self) -> RecommendationsResource: ...

            def list(
                self,
                *,
                name: str,
                filter: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any,
            ) -> GoogleCloudLocationListLocationsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: GoogleCloudLocationListLocationsResponseHttpRequest,
                previous_response: GoogleCloudLocationListLocationsResponse,
            ) -> GoogleCloudLocationListLocationsResponseHttpRequest | None: ...
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
                    ) -> GoogleCloudRecommenderV1beta1InsightHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
                    ) -> (
                        GoogleCloudRecommenderV1beta1ListInsightsResponseHttpRequest
                    ): ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudRecommenderV1beta1ListInsightsResponseHttpRequest,
                        previous_response: GoogleCloudRecommenderV1beta1ListInsightsResponse,
                    ) -> (
                        GoogleCloudRecommenderV1beta1ListInsightsResponseHttpRequest
                        | None
                    ): ...
                    def markAccepted(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudRecommenderV1beta1MarkInsightAcceptedRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudRecommenderV1beta1InsightHttpRequest: ...

                def insights(self) -> InsightsResource: ...

            @typing.type_check_only
            class RecommendersResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class RecommendationsResource(googleapiclient.discovery.Resource):
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleCloudRecommenderV1beta1RecommendationHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudRecommenderV1beta1ListRecommendationsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudRecommenderV1beta1ListRecommendationsResponseHttpRequest,
                        previous_response: GoogleCloudRecommenderV1beta1ListRecommendationsResponse,
                    ) -> (
                        GoogleCloudRecommenderV1beta1ListRecommendationsResponseHttpRequest
                        | None
                    ): ...
                    def markClaimed(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudRecommenderV1beta1MarkRecommendationClaimedRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudRecommenderV1beta1RecommendationHttpRequest: ...
                    def markDismissed(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudRecommenderV1beta1MarkRecommendationDismissedRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudRecommenderV1beta1RecommendationHttpRequest: ...
                    def markFailed(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudRecommenderV1beta1MarkRecommendationFailedRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudRecommenderV1beta1RecommendationHttpRequest: ...
                    def markSucceeded(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudRecommenderV1beta1MarkRecommendationSucceededRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudRecommenderV1beta1RecommendationHttpRequest: ...

                def recommendations(self) -> RecommendationsResource: ...

            def list(
                self,
                *,
                name: str,
                filter: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any,
            ) -> GoogleCloudLocationListLocationsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: GoogleCloudLocationListLocationsResponseHttpRequest,
                previous_response: GoogleCloudLocationListLocationsResponse,
            ) -> GoogleCloudLocationListLocationsResponseHttpRequest | None: ...
            def insightTypes(self) -> InsightTypesResource: ...
            def recommenders(self) -> RecommendersResource: ...

        def locations(self) -> LocationsResource: ...

    @typing.type_check_only
    class InsightTypesResource(googleapiclient.discovery.Resource):
        def list(
            self, *, pageSize: int = ..., pageToken: str = ..., **kwargs: typing.Any
        ) -> GoogleCloudRecommenderV1beta1ListInsightTypesResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: GoogleCloudRecommenderV1beta1ListInsightTypesResponseHttpRequest,
            previous_response: GoogleCloudRecommenderV1beta1ListInsightTypesResponse,
        ) -> (
            GoogleCloudRecommenderV1beta1ListInsightTypesResponseHttpRequest | None
        ): ...

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
                    ) -> GoogleCloudRecommenderV1beta1InsightHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
                    ) -> (
                        GoogleCloudRecommenderV1beta1ListInsightsResponseHttpRequest
                    ): ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudRecommenderV1beta1ListInsightsResponseHttpRequest,
                        previous_response: GoogleCloudRecommenderV1beta1ListInsightsResponse,
                    ) -> (
                        GoogleCloudRecommenderV1beta1ListInsightsResponseHttpRequest
                        | None
                    ): ...
                    def markAccepted(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudRecommenderV1beta1MarkInsightAcceptedRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudRecommenderV1beta1InsightHttpRequest: ...

                def getConfig(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudRecommenderV1beta1InsightTypeConfigHttpRequest: ...
                def updateConfig(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudRecommenderV1beta1InsightTypeConfig = ...,
                    updateMask: str = ...,
                    validateOnly: bool = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudRecommenderV1beta1InsightTypeConfigHttpRequest: ...
                def insights(self) -> InsightsResource: ...

            @typing.type_check_only
            class RecommendersResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class RecommendationsResource(googleapiclient.discovery.Resource):
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleCloudRecommenderV1beta1RecommendationHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudRecommenderV1beta1ListRecommendationsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudRecommenderV1beta1ListRecommendationsResponseHttpRequest,
                        previous_response: GoogleCloudRecommenderV1beta1ListRecommendationsResponse,
                    ) -> (
                        GoogleCloudRecommenderV1beta1ListRecommendationsResponseHttpRequest
                        | None
                    ): ...
                    def markClaimed(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudRecommenderV1beta1MarkRecommendationClaimedRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudRecommenderV1beta1RecommendationHttpRequest: ...
                    def markDismissed(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudRecommenderV1beta1MarkRecommendationDismissedRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudRecommenderV1beta1RecommendationHttpRequest: ...
                    def markFailed(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudRecommenderV1beta1MarkRecommendationFailedRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudRecommenderV1beta1RecommendationHttpRequest: ...
                    def markSucceeded(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudRecommenderV1beta1MarkRecommendationSucceededRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudRecommenderV1beta1RecommendationHttpRequest: ...

                def getConfig(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudRecommenderV1beta1RecommenderConfigHttpRequest: ...
                def updateConfig(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudRecommenderV1beta1RecommenderConfig = ...,
                    updateMask: str = ...,
                    validateOnly: bool = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudRecommenderV1beta1RecommenderConfigHttpRequest: ...
                def recommendations(self) -> RecommendationsResource: ...

            def list(
                self,
                *,
                name: str,
                filter: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any,
            ) -> GoogleCloudLocationListLocationsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: GoogleCloudLocationListLocationsResponseHttpRequest,
                previous_response: GoogleCloudLocationListLocationsResponse,
            ) -> GoogleCloudLocationListLocationsResponseHttpRequest | None: ...
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
                    ) -> GoogleCloudRecommenderV1beta1InsightHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
                    ) -> (
                        GoogleCloudRecommenderV1beta1ListInsightsResponseHttpRequest
                    ): ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudRecommenderV1beta1ListInsightsResponseHttpRequest,
                        previous_response: GoogleCloudRecommenderV1beta1ListInsightsResponse,
                    ) -> (
                        GoogleCloudRecommenderV1beta1ListInsightsResponseHttpRequest
                        | None
                    ): ...
                    def markAccepted(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudRecommenderV1beta1MarkInsightAcceptedRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudRecommenderV1beta1InsightHttpRequest: ...

                def getConfig(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudRecommenderV1beta1InsightTypeConfigHttpRequest: ...
                def updateConfig(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudRecommenderV1beta1InsightTypeConfig = ...,
                    updateMask: str = ...,
                    validateOnly: bool = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudRecommenderV1beta1InsightTypeConfigHttpRequest: ...
                def insights(self) -> InsightsResource: ...

            @typing.type_check_only
            class RecommendersResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class RecommendationsResource(googleapiclient.discovery.Resource):
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleCloudRecommenderV1beta1RecommendationHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudRecommenderV1beta1ListRecommendationsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudRecommenderV1beta1ListRecommendationsResponseHttpRequest,
                        previous_response: GoogleCloudRecommenderV1beta1ListRecommendationsResponse,
                    ) -> (
                        GoogleCloudRecommenderV1beta1ListRecommendationsResponseHttpRequest
                        | None
                    ): ...
                    def markClaimed(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudRecommenderV1beta1MarkRecommendationClaimedRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudRecommenderV1beta1RecommendationHttpRequest: ...
                    def markDismissed(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudRecommenderV1beta1MarkRecommendationDismissedRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudRecommenderV1beta1RecommendationHttpRequest: ...
                    def markFailed(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudRecommenderV1beta1MarkRecommendationFailedRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudRecommenderV1beta1RecommendationHttpRequest: ...
                    def markSucceeded(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudRecommenderV1beta1MarkRecommendationSucceededRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudRecommenderV1beta1RecommendationHttpRequest: ...

                def getConfig(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudRecommenderV1beta1RecommenderConfigHttpRequest: ...
                def updateConfig(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudRecommenderV1beta1RecommenderConfig = ...,
                    updateMask: str = ...,
                    validateOnly: bool = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudRecommenderV1beta1RecommenderConfigHttpRequest: ...
                def recommendations(self) -> RecommendationsResource: ...

            def list(
                self,
                *,
                name: str,
                filter: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any,
            ) -> GoogleCloudLocationListLocationsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: GoogleCloudLocationListLocationsResponseHttpRequest,
                previous_response: GoogleCloudLocationListLocationsResponse,
            ) -> GoogleCloudLocationListLocationsResponseHttpRequest | None: ...
            def insightTypes(self) -> InsightTypesResource: ...
            def recommenders(self) -> RecommendersResource: ...

        def locations(self) -> LocationsResource: ...

    @typing.type_check_only
    class RecommendersResource(googleapiclient.discovery.Resource):
        def list(
            self, *, pageSize: int = ..., pageToken: str = ..., **kwargs: typing.Any
        ) -> GoogleCloudRecommenderV1beta1ListRecommendersResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: GoogleCloudRecommenderV1beta1ListRecommendersResponseHttpRequest,
            previous_response: GoogleCloudRecommenderV1beta1ListRecommendersResponse,
        ) -> (
            GoogleCloudRecommenderV1beta1ListRecommendersResponseHttpRequest | None
        ): ...

    def new_batch_http_request(
        self,
        callback: collections.abc.Callable[
            [
                str,
                googleapiclient.http.HttpRequest,
                googleapiclient.errors.HttpError | None,
            ],
            typing.Any,
        ]
        | None = None,
    ) -> googleapiclient.http.BatchHttpRequest: ...
    def billingAccounts(self) -> BillingAccountsResource: ...
    def folders(self) -> FoldersResource: ...
    def insightTypes(self) -> InsightTypesResource: ...
    def organizations(self) -> OrganizationsResource: ...
    def projects(self) -> ProjectsResource: ...
    def recommenders(self) -> RecommendersResource: ...

@typing.type_check_only
class GoogleCloudLocationListLocationsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudLocationListLocationsResponse: ...

@typing.type_check_only
class GoogleCloudRecommenderV1beta1InsightHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudRecommenderV1beta1Insight: ...

@typing.type_check_only
class GoogleCloudRecommenderV1beta1InsightTypeConfigHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudRecommenderV1beta1InsightTypeConfig: ...

@typing.type_check_only
class GoogleCloudRecommenderV1beta1ListInsightTypesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudRecommenderV1beta1ListInsightTypesResponse: ...

@typing.type_check_only
class GoogleCloudRecommenderV1beta1ListInsightsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudRecommenderV1beta1ListInsightsResponse: ...

@typing.type_check_only
class GoogleCloudRecommenderV1beta1ListRecommendationsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudRecommenderV1beta1ListRecommendationsResponse: ...

@typing.type_check_only
class GoogleCloudRecommenderV1beta1ListRecommendersResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudRecommenderV1beta1ListRecommendersResponse: ...

@typing.type_check_only
class GoogleCloudRecommenderV1beta1RecommendationHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudRecommenderV1beta1Recommendation: ...

@typing.type_check_only
class GoogleCloudRecommenderV1beta1RecommenderConfigHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudRecommenderV1beta1RecommenderConfig: ...
