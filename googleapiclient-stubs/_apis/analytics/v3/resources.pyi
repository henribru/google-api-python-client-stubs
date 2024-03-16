import collections.abc
import typing

import httplib2
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http

from .schemas import *

_list = list

@typing.type_check_only
class AnalyticsResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class DataResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class GaResource(googleapiclient.discovery.Resource):
            def get(
                self,
                *,
                ids: str,
                start_date: str,
                end_date: str,
                metrics: str,
                dimensions: str = ...,
                filters: str = ...,
                include_empty_rows: bool = ...,
                max_results: int = ...,
                output: typing_extensions.Literal["dataTable", "json"] = ...,
                samplingLevel: typing_extensions.Literal[
                    "DEFAULT", "FASTER", "HIGHER_PRECISION"
                ] = ...,
                segment: str = ...,
                sort: str = ...,
                start_index: int = ...,
                **kwargs: typing.Any,
            ) -> GaDataHttpRequest: ...

        @typing.type_check_only
        class McfResource(googleapiclient.discovery.Resource):
            def get(
                self,
                *,
                ids: str,
                start_date: str,
                end_date: str,
                metrics: str,
                dimensions: str = ...,
                filters: str = ...,
                max_results: int = ...,
                samplingLevel: typing_extensions.Literal[
                    "DEFAULT", "FASTER", "HIGHER_PRECISION"
                ] = ...,
                sort: str = ...,
                start_index: int = ...,
                **kwargs: typing.Any,
            ) -> McfDataHttpRequest: ...

        @typing.type_check_only
        class RealtimeResource(googleapiclient.discovery.Resource):
            def get(
                self,
                *,
                ids: str,
                metrics: str,
                dimensions: str = ...,
                filters: str = ...,
                max_results: int = ...,
                sort: str = ...,
                **kwargs: typing.Any,
            ) -> RealtimeDataHttpRequest: ...

        def ga(self) -> GaResource: ...
        def mcf(self) -> McfResource: ...
        def realtime(self) -> RealtimeResource: ...

    @typing.type_check_only
    class ManagementResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class AccountSummariesResource(googleapiclient.discovery.Resource):
            def list(
                self,
                *,
                max_results: int = ...,
                start_index: int = ...,
                **kwargs: typing.Any,
            ) -> AccountSummariesHttpRequest: ...

        @typing.type_check_only
        class AccountUserLinksResource(googleapiclient.discovery.Resource):
            def delete(
                self, *, accountId: str, linkId: str, **kwargs: typing.Any
            ) -> googleapiclient.http.HttpRequest: ...
            def insert(
                self,
                *,
                accountId: str,
                body: EntityUserLink = ...,
                **kwargs: typing.Any,
            ) -> EntityUserLinkHttpRequest: ...
            def list(
                self,
                *,
                accountId: str,
                max_results: int = ...,
                start_index: int = ...,
                **kwargs: typing.Any,
            ) -> EntityUserLinksHttpRequest: ...
            def update(
                self,
                *,
                accountId: str,
                linkId: str,
                body: EntityUserLink = ...,
                **kwargs: typing.Any,
            ) -> EntityUserLinkHttpRequest: ...

        @typing.type_check_only
        class AccountsResource(googleapiclient.discovery.Resource):
            def list(
                self,
                *,
                max_results: int = ...,
                start_index: int = ...,
                **kwargs: typing.Any,
            ) -> AccountsHttpRequest: ...

        @typing.type_check_only
        class ClientIdResource(googleapiclient.discovery.Resource):
            def hashClientId(
                self, *, body: HashClientIdRequest = ..., **kwargs: typing.Any
            ) -> HashClientIdResponseHttpRequest: ...

        @typing.type_check_only
        class CustomDataSourcesResource(googleapiclient.discovery.Resource):
            def list(
                self,
                *,
                accountId: str,
                webPropertyId: str,
                max_results: int = ...,
                start_index: int = ...,
                **kwargs: typing.Any,
            ) -> CustomDataSourcesHttpRequest: ...

        @typing.type_check_only
        class CustomDimensionsResource(googleapiclient.discovery.Resource):
            def get(
                self,
                *,
                accountId: str,
                webPropertyId: str,
                customDimensionId: str,
                **kwargs: typing.Any,
            ) -> CustomDimensionHttpRequest: ...
            def insert(
                self,
                *,
                accountId: str,
                webPropertyId: str,
                body: CustomDimension = ...,
                **kwargs: typing.Any,
            ) -> CustomDimensionHttpRequest: ...
            def list(
                self,
                *,
                accountId: str,
                webPropertyId: str,
                max_results: int = ...,
                start_index: int = ...,
                **kwargs: typing.Any,
            ) -> CustomDimensionsHttpRequest: ...
            def patch(
                self,
                *,
                accountId: str,
                webPropertyId: str,
                customDimensionId: str,
                body: CustomDimension = ...,
                ignoreCustomDataSourceLinks: bool = ...,
                **kwargs: typing.Any,
            ) -> CustomDimensionHttpRequest: ...
            def update(
                self,
                *,
                accountId: str,
                webPropertyId: str,
                customDimensionId: str,
                body: CustomDimension = ...,
                ignoreCustomDataSourceLinks: bool = ...,
                **kwargs: typing.Any,
            ) -> CustomDimensionHttpRequest: ...

        @typing.type_check_only
        class CustomMetricsResource(googleapiclient.discovery.Resource):
            def get(
                self,
                *,
                accountId: str,
                webPropertyId: str,
                customMetricId: str,
                **kwargs: typing.Any,
            ) -> CustomMetricHttpRequest: ...
            def insert(
                self,
                *,
                accountId: str,
                webPropertyId: str,
                body: CustomMetric = ...,
                **kwargs: typing.Any,
            ) -> CustomMetricHttpRequest: ...
            def list(
                self,
                *,
                accountId: str,
                webPropertyId: str,
                max_results: int = ...,
                start_index: int = ...,
                **kwargs: typing.Any,
            ) -> CustomMetricsHttpRequest: ...
            def patch(
                self,
                *,
                accountId: str,
                webPropertyId: str,
                customMetricId: str,
                body: CustomMetric = ...,
                ignoreCustomDataSourceLinks: bool = ...,
                **kwargs: typing.Any,
            ) -> CustomMetricHttpRequest: ...
            def update(
                self,
                *,
                accountId: str,
                webPropertyId: str,
                customMetricId: str,
                body: CustomMetric = ...,
                ignoreCustomDataSourceLinks: bool = ...,
                **kwargs: typing.Any,
            ) -> CustomMetricHttpRequest: ...

        @typing.type_check_only
        class ExperimentsResource(googleapiclient.discovery.Resource):
            def delete(
                self,
                *,
                accountId: str,
                webPropertyId: str,
                profileId: str,
                experimentId: str,
                **kwargs: typing.Any,
            ) -> googleapiclient.http.HttpRequest: ...
            def get(
                self,
                *,
                accountId: str,
                webPropertyId: str,
                profileId: str,
                experimentId: str,
                **kwargs: typing.Any,
            ) -> ExperimentHttpRequest: ...
            def insert(
                self,
                *,
                accountId: str,
                webPropertyId: str,
                profileId: str,
                body: Experiment = ...,
                **kwargs: typing.Any,
            ) -> ExperimentHttpRequest: ...
            def list(
                self,
                *,
                accountId: str,
                webPropertyId: str,
                profileId: str,
                max_results: int = ...,
                start_index: int = ...,
                **kwargs: typing.Any,
            ) -> ExperimentsHttpRequest: ...
            def patch(
                self,
                *,
                accountId: str,
                webPropertyId: str,
                profileId: str,
                experimentId: str,
                body: Experiment = ...,
                **kwargs: typing.Any,
            ) -> ExperimentHttpRequest: ...
            def update(
                self,
                *,
                accountId: str,
                webPropertyId: str,
                profileId: str,
                experimentId: str,
                body: Experiment = ...,
                **kwargs: typing.Any,
            ) -> ExperimentHttpRequest: ...

        @typing.type_check_only
        class FiltersResource(googleapiclient.discovery.Resource):
            def delete(
                self, *, accountId: str, filterId: str, **kwargs: typing.Any
            ) -> FilterHttpRequest: ...
            def get(
                self, *, accountId: str, filterId: str, **kwargs: typing.Any
            ) -> FilterHttpRequest: ...
            def insert(
                self, *, accountId: str, body: Filter = ..., **kwargs: typing.Any
            ) -> FilterHttpRequest: ...
            def list(
                self,
                *,
                accountId: str,
                max_results: int = ...,
                start_index: int = ...,
                **kwargs: typing.Any,
            ) -> FiltersHttpRequest: ...
            def patch(
                self,
                *,
                accountId: str,
                filterId: str,
                body: Filter = ...,
                **kwargs: typing.Any,
            ) -> FilterHttpRequest: ...
            def update(
                self,
                *,
                accountId: str,
                filterId: str,
                body: Filter = ...,
                **kwargs: typing.Any,
            ) -> FilterHttpRequest: ...

        @typing.type_check_only
        class GoalsResource(googleapiclient.discovery.Resource):
            def get(
                self,
                *,
                accountId: str,
                webPropertyId: str,
                profileId: str,
                goalId: str,
                **kwargs: typing.Any,
            ) -> GoalHttpRequest: ...
            def insert(
                self,
                *,
                accountId: str,
                webPropertyId: str,
                profileId: str,
                body: Goal = ...,
                **kwargs: typing.Any,
            ) -> GoalHttpRequest: ...
            def list(
                self,
                *,
                accountId: str,
                webPropertyId: str,
                profileId: str,
                max_results: int = ...,
                start_index: int = ...,
                **kwargs: typing.Any,
            ) -> GoalsHttpRequest: ...
            def patch(
                self,
                *,
                accountId: str,
                webPropertyId: str,
                profileId: str,
                goalId: str,
                body: Goal = ...,
                **kwargs: typing.Any,
            ) -> GoalHttpRequest: ...
            def update(
                self,
                *,
                accountId: str,
                webPropertyId: str,
                profileId: str,
                goalId: str,
                body: Goal = ...,
                **kwargs: typing.Any,
            ) -> GoalHttpRequest: ...

        @typing.type_check_only
        class ProfileFilterLinksResource(googleapiclient.discovery.Resource):
            def delete(
                self,
                *,
                accountId: str,
                webPropertyId: str,
                profileId: str,
                linkId: str,
                **kwargs: typing.Any,
            ) -> googleapiclient.http.HttpRequest: ...
            def get(
                self,
                *,
                accountId: str,
                webPropertyId: str,
                profileId: str,
                linkId: str,
                **kwargs: typing.Any,
            ) -> ProfileFilterLinkHttpRequest: ...
            def insert(
                self,
                *,
                accountId: str,
                webPropertyId: str,
                profileId: str,
                body: ProfileFilterLink = ...,
                **kwargs: typing.Any,
            ) -> ProfileFilterLinkHttpRequest: ...
            def list(
                self,
                *,
                accountId: str,
                webPropertyId: str,
                profileId: str,
                max_results: int = ...,
                start_index: int = ...,
                **kwargs: typing.Any,
            ) -> ProfileFilterLinksHttpRequest: ...
            def patch(
                self,
                *,
                accountId: str,
                webPropertyId: str,
                profileId: str,
                linkId: str,
                body: ProfileFilterLink = ...,
                **kwargs: typing.Any,
            ) -> ProfileFilterLinkHttpRequest: ...
            def update(
                self,
                *,
                accountId: str,
                webPropertyId: str,
                profileId: str,
                linkId: str,
                body: ProfileFilterLink = ...,
                **kwargs: typing.Any,
            ) -> ProfileFilterLinkHttpRequest: ...

        @typing.type_check_only
        class ProfileUserLinksResource(googleapiclient.discovery.Resource):
            def delete(
                self,
                *,
                accountId: str,
                webPropertyId: str,
                profileId: str,
                linkId: str,
                **kwargs: typing.Any,
            ) -> googleapiclient.http.HttpRequest: ...
            def insert(
                self,
                *,
                accountId: str,
                webPropertyId: str,
                profileId: str,
                body: EntityUserLink = ...,
                **kwargs: typing.Any,
            ) -> EntityUserLinkHttpRequest: ...
            def list(
                self,
                *,
                accountId: str,
                webPropertyId: str,
                profileId: str,
                max_results: int = ...,
                start_index: int = ...,
                **kwargs: typing.Any,
            ) -> EntityUserLinksHttpRequest: ...
            def update(
                self,
                *,
                accountId: str,
                webPropertyId: str,
                profileId: str,
                linkId: str,
                body: EntityUserLink = ...,
                **kwargs: typing.Any,
            ) -> EntityUserLinkHttpRequest: ...

        @typing.type_check_only
        class ProfilesResource(googleapiclient.discovery.Resource):
            def delete(
                self,
                *,
                accountId: str,
                webPropertyId: str,
                profileId: str,
                **kwargs: typing.Any,
            ) -> googleapiclient.http.HttpRequest: ...
            def get(
                self,
                *,
                accountId: str,
                webPropertyId: str,
                profileId: str,
                **kwargs: typing.Any,
            ) -> ProfileHttpRequest: ...
            def insert(
                self,
                *,
                accountId: str,
                webPropertyId: str,
                body: Profile = ...,
                **kwargs: typing.Any,
            ) -> ProfileHttpRequest: ...
            def list(
                self,
                *,
                accountId: str,
                webPropertyId: str,
                max_results: int = ...,
                start_index: int = ...,
                **kwargs: typing.Any,
            ) -> ProfilesHttpRequest: ...
            def patch(
                self,
                *,
                accountId: str,
                webPropertyId: str,
                profileId: str,
                body: Profile = ...,
                **kwargs: typing.Any,
            ) -> ProfileHttpRequest: ...
            def update(
                self,
                *,
                accountId: str,
                webPropertyId: str,
                profileId: str,
                body: Profile = ...,
                **kwargs: typing.Any,
            ) -> ProfileHttpRequest: ...

        @typing.type_check_only
        class RemarketingAudienceResource(googleapiclient.discovery.Resource):
            def delete(
                self,
                *,
                accountId: str,
                webPropertyId: str,
                remarketingAudienceId: str,
                **kwargs: typing.Any,
            ) -> googleapiclient.http.HttpRequest: ...
            def get(
                self,
                *,
                accountId: str,
                webPropertyId: str,
                remarketingAudienceId: str,
                **kwargs: typing.Any,
            ) -> RemarketingAudienceHttpRequest: ...
            def insert(
                self,
                *,
                accountId: str,
                webPropertyId: str,
                body: RemarketingAudience = ...,
                **kwargs: typing.Any,
            ) -> RemarketingAudienceHttpRequest: ...
            def list(
                self,
                *,
                accountId: str,
                webPropertyId: str,
                max_results: int = ...,
                start_index: int = ...,
                type: str = ...,
                **kwargs: typing.Any,
            ) -> RemarketingAudiencesHttpRequest: ...
            def patch(
                self,
                *,
                accountId: str,
                webPropertyId: str,
                remarketingAudienceId: str,
                body: RemarketingAudience = ...,
                **kwargs: typing.Any,
            ) -> RemarketingAudienceHttpRequest: ...
            def update(
                self,
                *,
                accountId: str,
                webPropertyId: str,
                remarketingAudienceId: str,
                body: RemarketingAudience = ...,
                **kwargs: typing.Any,
            ) -> RemarketingAudienceHttpRequest: ...

        @typing.type_check_only
        class SegmentsResource(googleapiclient.discovery.Resource):
            def list(
                self,
                *,
                max_results: int = ...,
                start_index: int = ...,
                **kwargs: typing.Any,
            ) -> SegmentsHttpRequest: ...

        @typing.type_check_only
        class UnsampledReportsResource(googleapiclient.discovery.Resource):
            def delete(
                self,
                *,
                accountId: str,
                webPropertyId: str,
                profileId: str,
                unsampledReportId: str,
                **kwargs: typing.Any,
            ) -> googleapiclient.http.HttpRequest: ...
            def get(
                self,
                *,
                accountId: str,
                webPropertyId: str,
                profileId: str,
                unsampledReportId: str,
                **kwargs: typing.Any,
            ) -> UnsampledReportHttpRequest: ...
            def insert(
                self,
                *,
                accountId: str,
                webPropertyId: str,
                profileId: str,
                body: UnsampledReport = ...,
                **kwargs: typing.Any,
            ) -> UnsampledReportHttpRequest: ...
            def list(
                self,
                *,
                accountId: str,
                webPropertyId: str,
                profileId: str,
                max_results: int = ...,
                start_index: int = ...,
                **kwargs: typing.Any,
            ) -> UnsampledReportsHttpRequest: ...

        @typing.type_check_only
        class UploadsResource(googleapiclient.discovery.Resource):
            def deleteUploadData(
                self,
                *,
                accountId: str,
                webPropertyId: str,
                customDataSourceId: str,
                body: AnalyticsDataimportDeleteUploadDataRequest = ...,
                **kwargs: typing.Any,
            ) -> googleapiclient.http.HttpRequest: ...
            def get(
                self,
                *,
                accountId: str,
                webPropertyId: str,
                customDataSourceId: str,
                uploadId: str,
                **kwargs: typing.Any,
            ) -> UploadHttpRequest: ...
            def list(
                self,
                *,
                accountId: str,
                webPropertyId: str,
                customDataSourceId: str,
                max_results: int = ...,
                start_index: int = ...,
                **kwargs: typing.Any,
            ) -> UploadsHttpRequest: ...
            def uploadData(
                self,
                *,
                accountId: str,
                webPropertyId: str,
                customDataSourceId: str,
                **kwargs: typing.Any,
            ) -> UploadHttpRequest: ...

        @typing.type_check_only
        class WebPropertyAdWordsLinksResource(googleapiclient.discovery.Resource):
            def delete(
                self,
                *,
                accountId: str,
                webPropertyId: str,
                webPropertyAdWordsLinkId: str,
                **kwargs: typing.Any,
            ) -> googleapiclient.http.HttpRequest: ...
            def get(
                self,
                *,
                accountId: str,
                webPropertyId: str,
                webPropertyAdWordsLinkId: str,
                **kwargs: typing.Any,
            ) -> EntityAdWordsLinkHttpRequest: ...
            def insert(
                self,
                *,
                accountId: str,
                webPropertyId: str,
                body: EntityAdWordsLink = ...,
                **kwargs: typing.Any,
            ) -> EntityAdWordsLinkHttpRequest: ...
            def list(
                self,
                *,
                accountId: str,
                webPropertyId: str,
                max_results: int = ...,
                start_index: int = ...,
                **kwargs: typing.Any,
            ) -> EntityAdWordsLinksHttpRequest: ...
            def patch(
                self,
                *,
                accountId: str,
                webPropertyId: str,
                webPropertyAdWordsLinkId: str,
                body: EntityAdWordsLink = ...,
                **kwargs: typing.Any,
            ) -> EntityAdWordsLinkHttpRequest: ...
            def update(
                self,
                *,
                accountId: str,
                webPropertyId: str,
                webPropertyAdWordsLinkId: str,
                body: EntityAdWordsLink = ...,
                **kwargs: typing.Any,
            ) -> EntityAdWordsLinkHttpRequest: ...

        @typing.type_check_only
        class WebpropertiesResource(googleapiclient.discovery.Resource):
            def get(
                self, *, accountId: str, webPropertyId: str, **kwargs: typing.Any
            ) -> WebpropertyHttpRequest: ...
            def insert(
                self, *, accountId: str, body: Webproperty = ..., **kwargs: typing.Any
            ) -> WebpropertyHttpRequest: ...
            def list(
                self,
                *,
                accountId: str,
                max_results: int = ...,
                start_index: int = ...,
                **kwargs: typing.Any,
            ) -> WebpropertiesHttpRequest: ...
            def patch(
                self,
                *,
                accountId: str,
                webPropertyId: str,
                body: Webproperty = ...,
                **kwargs: typing.Any,
            ) -> WebpropertyHttpRequest: ...
            def update(
                self,
                *,
                accountId: str,
                webPropertyId: str,
                body: Webproperty = ...,
                **kwargs: typing.Any,
            ) -> WebpropertyHttpRequest: ...

        @typing.type_check_only
        class WebpropertyUserLinksResource(googleapiclient.discovery.Resource):
            def delete(
                self,
                *,
                accountId: str,
                webPropertyId: str,
                linkId: str,
                **kwargs: typing.Any,
            ) -> googleapiclient.http.HttpRequest: ...
            def insert(
                self,
                *,
                accountId: str,
                webPropertyId: str,
                body: EntityUserLink = ...,
                **kwargs: typing.Any,
            ) -> EntityUserLinkHttpRequest: ...
            def list(
                self,
                *,
                accountId: str,
                webPropertyId: str,
                max_results: int = ...,
                start_index: int = ...,
                **kwargs: typing.Any,
            ) -> EntityUserLinksHttpRequest: ...
            def update(
                self,
                *,
                accountId: str,
                webPropertyId: str,
                linkId: str,
                body: EntityUserLink = ...,
                **kwargs: typing.Any,
            ) -> EntityUserLinkHttpRequest: ...

        def accountSummaries(self) -> AccountSummariesResource: ...
        def accountUserLinks(self) -> AccountUserLinksResource: ...
        def accounts(self) -> AccountsResource: ...
        def clientId(self) -> ClientIdResource: ...
        def customDataSources(self) -> CustomDataSourcesResource: ...
        def customDimensions(self) -> CustomDimensionsResource: ...
        def customMetrics(self) -> CustomMetricsResource: ...
        def experiments(self) -> ExperimentsResource: ...
        def filters(self) -> FiltersResource: ...
        def goals(self) -> GoalsResource: ...
        def profileFilterLinks(self) -> ProfileFilterLinksResource: ...
        def profileUserLinks(self) -> ProfileUserLinksResource: ...
        def profiles(self) -> ProfilesResource: ...
        def remarketingAudience(self) -> RemarketingAudienceResource: ...
        def segments(self) -> SegmentsResource: ...
        def unsampledReports(self) -> UnsampledReportsResource: ...
        def uploads(self) -> UploadsResource: ...
        def webPropertyAdWordsLinks(self) -> WebPropertyAdWordsLinksResource: ...
        def webproperties(self) -> WebpropertiesResource: ...
        def webpropertyUserLinks(self) -> WebpropertyUserLinksResource: ...

    @typing.type_check_only
    class MetadataResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class ColumnsResource(googleapiclient.discovery.Resource):
            def list(
                self, *, reportType: str, **kwargs: typing.Any
            ) -> ColumnsHttpRequest: ...

        def columns(self) -> ColumnsResource: ...

    @typing.type_check_only
    class ProvisioningResource(googleapiclient.discovery.Resource):
        def createAccountTicket(
            self, *, body: AccountTicket = ..., **kwargs: typing.Any
        ) -> AccountTicketHttpRequest: ...
        def createAccountTree(
            self, *, body: AccountTreeRequest = ..., **kwargs: typing.Any
        ) -> AccountTreeResponseHttpRequest: ...

    @typing.type_check_only
    class UserDeletionResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class UserDeletionRequestResource(googleapiclient.discovery.Resource):
            def upsert(
                self, *, body: UserDeletionRequest = ..., **kwargs: typing.Any
            ) -> UserDeletionRequestHttpRequest: ...

        def userDeletionRequest(self) -> UserDeletionRequestResource: ...

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
    def data(self) -> DataResource: ...
    def management(self) -> ManagementResource: ...
    def metadata(self) -> MetadataResource: ...
    def provisioning(self) -> ProvisioningResource: ...
    def userDeletion(self) -> UserDeletionResource: ...

@typing.type_check_only
class AccountSummariesHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> AccountSummaries: ...

@typing.type_check_only
class AccountTicketHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> AccountTicket: ...

@typing.type_check_only
class AccountTreeResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> AccountTreeResponse: ...

@typing.type_check_only
class AccountsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Accounts: ...

@typing.type_check_only
class ColumnsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Columns: ...

@typing.type_check_only
class CustomDataSourcesHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> CustomDataSources: ...

@typing.type_check_only
class CustomDimensionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> CustomDimension: ...

@typing.type_check_only
class CustomDimensionsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> CustomDimensions: ...

@typing.type_check_only
class CustomMetricHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> CustomMetric: ...

@typing.type_check_only
class CustomMetricsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> CustomMetrics: ...

@typing.type_check_only
class EntityAdWordsLinkHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> EntityAdWordsLink: ...

@typing.type_check_only
class EntityAdWordsLinksHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> EntityAdWordsLinks: ...

@typing.type_check_only
class EntityUserLinkHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> EntityUserLink: ...

@typing.type_check_only
class EntityUserLinksHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> EntityUserLinks: ...

@typing.type_check_only
class ExperimentHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Experiment: ...

@typing.type_check_only
class ExperimentsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Experiments: ...

@typing.type_check_only
class FilterHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Filter: ...

@typing.type_check_only
class FiltersHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Filters: ...

@typing.type_check_only
class GaDataHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GaData: ...

@typing.type_check_only
class GoalHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Goal: ...

@typing.type_check_only
class GoalsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Goals: ...

@typing.type_check_only
class HashClientIdResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> HashClientIdResponse: ...

@typing.type_check_only
class McfDataHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> McfData: ...

@typing.type_check_only
class ProfileHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Profile: ...

@typing.type_check_only
class ProfileFilterLinkHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ProfileFilterLink: ...

@typing.type_check_only
class ProfileFilterLinksHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ProfileFilterLinks: ...

@typing.type_check_only
class ProfilesHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Profiles: ...

@typing.type_check_only
class RealtimeDataHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> RealtimeData: ...

@typing.type_check_only
class RemarketingAudienceHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> RemarketingAudience: ...

@typing.type_check_only
class RemarketingAudiencesHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> RemarketingAudiences: ...

@typing.type_check_only
class SegmentsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Segments: ...

@typing.type_check_only
class UnsampledReportHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> UnsampledReport: ...

@typing.type_check_only
class UnsampledReportsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> UnsampledReports: ...

@typing.type_check_only
class UploadHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Upload: ...

@typing.type_check_only
class UploadsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Uploads: ...

@typing.type_check_only
class UserDeletionRequestHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> UserDeletionRequest: ...

@typing.type_check_only
class WebpropertiesHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Webproperties: ...

@typing.type_check_only
class WebpropertyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Webproperty: ...
