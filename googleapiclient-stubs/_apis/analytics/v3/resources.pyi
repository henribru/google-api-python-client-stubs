import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class AnalyticsResource(googleapiclient.discovery.Resource):
    class MetadataResource(googleapiclient.discovery.Resource):
        class ColumnsResource(googleapiclient.discovery.Resource):
            def list(
                self, *, reportType: str, **kwargs: typing.Any
            ) -> ColumnsHttpRequest: ...
        def columns(self) -> ColumnsResource: ...
    class DataResource(googleapiclient.discovery.Resource):
        class McfResource(googleapiclient.discovery.Resource):
            def get(
                self,
                *,
                ids: str,
                start_date: str,
                end_date: str,
                metrics: str,
                max_results: int = ...,
                samplingLevel: typing_extensions.Literal[
                    "DEFAULT", "FASTER", "HIGHER_PRECISION"
                ] = ...,
                filters: str = ...,
                sort: str = ...,
                dimensions: str = ...,
                start_index: int = ...,
                **kwargs: typing.Any
            ) -> McfDataHttpRequest: ...
        class GaResource(googleapiclient.discovery.Resource):
            def get(
                self,
                *,
                ids: str,
                start_date: str,
                end_date: str,
                metrics: str,
                segment: str = ...,
                output: typing_extensions.Literal["dataTable", "json"] = ...,
                sort: str = ...,
                max_results: int = ...,
                dimensions: str = ...,
                filters: str = ...,
                include_empty_rows: bool = ...,
                start_index: int = ...,
                samplingLevel: typing_extensions.Literal[
                    "DEFAULT", "FASTER", "HIGHER_PRECISION"
                ] = ...,
                **kwargs: typing.Any
            ) -> GaDataHttpRequest: ...
        class RealtimeResource(googleapiclient.discovery.Resource):
            def get(
                self,
                *,
                ids: str,
                metrics: str,
                sort: str = ...,
                dimensions: str = ...,
                max_results: int = ...,
                filters: str = ...,
                **kwargs: typing.Any
            ) -> RealtimeDataHttpRequest: ...
        def mcf(self) -> McfResource: ...
        def ga(self) -> GaResource: ...
        def realtime(self) -> RealtimeResource: ...
    class UserDeletionResource(googleapiclient.discovery.Resource):
        class UserDeletionRequestResource(googleapiclient.discovery.Resource):
            def upsert(
                self, *, body: UserDeletionRequest = ..., **kwargs: typing.Any
            ) -> UserDeletionRequestHttpRequest: ...
        def userDeletionRequest(self) -> UserDeletionRequestResource: ...
    class ManagementResource(googleapiclient.discovery.Resource):
        class ProfileUserLinksResource(googleapiclient.discovery.Resource):
            def delete(
                self,
                *,
                accountId: str,
                webPropertyId: str,
                profileId: str,
                linkId: str,
                **kwargs: typing.Any
            ) -> googleapiclient.http.HttpRequest: ...
            def list(
                self,
                *,
                accountId: str,
                webPropertyId: str,
                profileId: str,
                start_index: int = ...,
                max_results: int = ...,
                **kwargs: typing.Any
            ) -> EntityUserLinksHttpRequest: ...
            def update(
                self,
                *,
                accountId: str,
                webPropertyId: str,
                profileId: str,
                linkId: str,
                body: EntityUserLink = ...,
                **kwargs: typing.Any
            ) -> EntityUserLinkHttpRequest: ...
            def insert(
                self,
                *,
                accountId: str,
                webPropertyId: str,
                profileId: str,
                body: EntityUserLink = ...,
                **kwargs: typing.Any
            ) -> EntityUserLinkHttpRequest: ...
        class ProfileFilterLinksResource(googleapiclient.discovery.Resource):
            def insert(
                self,
                *,
                accountId: str,
                webPropertyId: str,
                profileId: str,
                body: ProfileFilterLink = ...,
                **kwargs: typing.Any
            ) -> ProfileFilterLinkHttpRequest: ...
            def list(
                self,
                *,
                accountId: str,
                webPropertyId: str,
                profileId: str,
                start_index: int = ...,
                max_results: int = ...,
                **kwargs: typing.Any
            ) -> ProfileFilterLinksHttpRequest: ...
            def delete(
                self,
                *,
                accountId: str,
                webPropertyId: str,
                profileId: str,
                linkId: str,
                **kwargs: typing.Any
            ) -> googleapiclient.http.HttpRequest: ...
            def get(
                self,
                *,
                accountId: str,
                webPropertyId: str,
                profileId: str,
                linkId: str,
                **kwargs: typing.Any
            ) -> ProfileFilterLinkHttpRequest: ...
            def update(
                self,
                *,
                accountId: str,
                webPropertyId: str,
                profileId: str,
                linkId: str,
                body: ProfileFilterLink = ...,
                **kwargs: typing.Any
            ) -> ProfileFilterLinkHttpRequest: ...
            def patch(
                self,
                *,
                accountId: str,
                webPropertyId: str,
                profileId: str,
                linkId: str,
                body: ProfileFilterLink = ...,
                **kwargs: typing.Any
            ) -> ProfileFilterLinkHttpRequest: ...
        class ProfilesResource(googleapiclient.discovery.Resource):
            def delete(
                self,
                *,
                accountId: str,
                webPropertyId: str,
                profileId: str,
                **kwargs: typing.Any
            ) -> googleapiclient.http.HttpRequest: ...
            def insert(
                self,
                *,
                accountId: str,
                webPropertyId: str,
                body: Profile = ...,
                **kwargs: typing.Any
            ) -> ProfileHttpRequest: ...
            def update(
                self,
                *,
                accountId: str,
                webPropertyId: str,
                profileId: str,
                body: Profile = ...,
                **kwargs: typing.Any
            ) -> ProfileHttpRequest: ...
            def patch(
                self,
                *,
                accountId: str,
                webPropertyId: str,
                profileId: str,
                body: Profile = ...,
                **kwargs: typing.Any
            ) -> ProfileHttpRequest: ...
            def get(
                self,
                *,
                accountId: str,
                webPropertyId: str,
                profileId: str,
                **kwargs: typing.Any
            ) -> ProfileHttpRequest: ...
            def list(
                self,
                *,
                accountId: str,
                webPropertyId: str,
                max_results: int = ...,
                start_index: int = ...,
                **kwargs: typing.Any
            ) -> ProfilesHttpRequest: ...
        class AccountSummariesResource(googleapiclient.discovery.Resource):
            def list(
                self,
                *,
                max_results: int = ...,
                start_index: int = ...,
                **kwargs: typing.Any
            ) -> AccountSummariesHttpRequest: ...
        class FiltersResource(googleapiclient.discovery.Resource):
            def list(
                self,
                *,
                accountId: str,
                max_results: int = ...,
                start_index: int = ...,
                **kwargs: typing.Any
            ) -> FiltersHttpRequest: ...
            def get(
                self, *, accountId: str, filterId: str, **kwargs: typing.Any
            ) -> FilterHttpRequest: ...
            def insert(
                self, *, accountId: str, body: Filter = ..., **kwargs: typing.Any
            ) -> FilterHttpRequest: ...
            def update(
                self,
                *,
                accountId: str,
                filterId: str,
                body: Filter = ...,
                **kwargs: typing.Any
            ) -> FilterHttpRequest: ...
            def patch(
                self,
                *,
                accountId: str,
                filterId: str,
                body: Filter = ...,
                **kwargs: typing.Any
            ) -> FilterHttpRequest: ...
            def delete(
                self, *, accountId: str, filterId: str, **kwargs: typing.Any
            ) -> FilterHttpRequest: ...
        class CustomDataSourcesResource(googleapiclient.discovery.Resource):
            def list(
                self,
                *,
                accountId: str,
                webPropertyId: str,
                max_results: int = ...,
                start_index: int = ...,
                **kwargs: typing.Any
            ) -> CustomDataSourcesHttpRequest: ...
        class ClientIdResource(googleapiclient.discovery.Resource):
            def hashClientId(
                self, *, body: HashClientIdRequest = ..., **kwargs: typing.Any
            ) -> HashClientIdResponseHttpRequest: ...
        class UploadsResource(googleapiclient.discovery.Resource):
            def uploadData(
                self,
                *,
                accountId: str,
                webPropertyId: str,
                customDataSourceId: str,
                **kwargs: typing.Any
            ) -> UploadHttpRequest: ...
            def get(
                self,
                *,
                accountId: str,
                webPropertyId: str,
                customDataSourceId: str,
                uploadId: str,
                **kwargs: typing.Any
            ) -> UploadHttpRequest: ...
            def deleteUploadData(
                self,
                *,
                accountId: str,
                webPropertyId: str,
                customDataSourceId: str,
                body: AnalyticsDataimportDeleteUploadDataRequest = ...,
                **kwargs: typing.Any
            ) -> googleapiclient.http.HttpRequest: ...
            def list(
                self,
                *,
                accountId: str,
                webPropertyId: str,
                customDataSourceId: str,
                start_index: int = ...,
                max_results: int = ...,
                **kwargs: typing.Any
            ) -> UploadsHttpRequest: ...
        class WebpropertyUserLinksResource(googleapiclient.discovery.Resource):
            def update(
                self,
                *,
                accountId: str,
                webPropertyId: str,
                linkId: str,
                body: EntityUserLink = ...,
                **kwargs: typing.Any
            ) -> EntityUserLinkHttpRequest: ...
            def list(
                self,
                *,
                accountId: str,
                webPropertyId: str,
                max_results: int = ...,
                start_index: int = ...,
                **kwargs: typing.Any
            ) -> EntityUserLinksHttpRequest: ...
            def delete(
                self,
                *,
                accountId: str,
                webPropertyId: str,
                linkId: str,
                **kwargs: typing.Any
            ) -> googleapiclient.http.HttpRequest: ...
            def insert(
                self,
                *,
                accountId: str,
                webPropertyId: str,
                body: EntityUserLink = ...,
                **kwargs: typing.Any
            ) -> EntityUserLinkHttpRequest: ...
        class AccountUserLinksResource(googleapiclient.discovery.Resource):
            def delete(
                self, *, accountId: str, linkId: str, **kwargs: typing.Any
            ) -> googleapiclient.http.HttpRequest: ...
            def update(
                self,
                *,
                accountId: str,
                linkId: str,
                body: EntityUserLink = ...,
                **kwargs: typing.Any
            ) -> EntityUserLinkHttpRequest: ...
            def insert(
                self,
                *,
                accountId: str,
                body: EntityUserLink = ...,
                **kwargs: typing.Any
            ) -> EntityUserLinkHttpRequest: ...
            def list(
                self,
                *,
                accountId: str,
                max_results: int = ...,
                start_index: int = ...,
                **kwargs: typing.Any
            ) -> EntityUserLinksHttpRequest: ...
        class WebPropertyAdWordsLinksResource(googleapiclient.discovery.Resource):
            def delete(
                self,
                *,
                accountId: str,
                webPropertyId: str,
                webPropertyAdWordsLinkId: str,
                **kwargs: typing.Any
            ) -> googleapiclient.http.HttpRequest: ...
            def insert(
                self,
                *,
                accountId: str,
                webPropertyId: str,
                body: EntityAdWordsLink = ...,
                **kwargs: typing.Any
            ) -> EntityAdWordsLinkHttpRequest: ...
            def update(
                self,
                *,
                accountId: str,
                webPropertyId: str,
                webPropertyAdWordsLinkId: str,
                body: EntityAdWordsLink = ...,
                **kwargs: typing.Any
            ) -> EntityAdWordsLinkHttpRequest: ...
            def list(
                self,
                *,
                accountId: str,
                webPropertyId: str,
                max_results: int = ...,
                start_index: int = ...,
                **kwargs: typing.Any
            ) -> EntityAdWordsLinksHttpRequest: ...
            def get(
                self,
                *,
                accountId: str,
                webPropertyId: str,
                webPropertyAdWordsLinkId: str,
                **kwargs: typing.Any
            ) -> EntityAdWordsLinkHttpRequest: ...
            def patch(
                self,
                *,
                accountId: str,
                webPropertyId: str,
                webPropertyAdWordsLinkId: str,
                body: EntityAdWordsLink = ...,
                **kwargs: typing.Any
            ) -> EntityAdWordsLinkHttpRequest: ...
        class AccountsResource(googleapiclient.discovery.Resource):
            def list(
                self,
                *,
                max_results: int = ...,
                start_index: int = ...,
                **kwargs: typing.Any
            ) -> AccountsHttpRequest: ...
        class GoalsResource(googleapiclient.discovery.Resource):
            def update(
                self,
                *,
                accountId: str,
                webPropertyId: str,
                profileId: str,
                goalId: str,
                body: Goal = ...,
                **kwargs: typing.Any
            ) -> GoalHttpRequest: ...
            def patch(
                self,
                *,
                accountId: str,
                webPropertyId: str,
                profileId: str,
                goalId: str,
                body: Goal = ...,
                **kwargs: typing.Any
            ) -> GoalHttpRequest: ...
            def get(
                self,
                *,
                accountId: str,
                webPropertyId: str,
                profileId: str,
                goalId: str,
                **kwargs: typing.Any
            ) -> GoalHttpRequest: ...
            def insert(
                self,
                *,
                accountId: str,
                webPropertyId: str,
                profileId: str,
                body: Goal = ...,
                **kwargs: typing.Any
            ) -> GoalHttpRequest: ...
            def list(
                self,
                *,
                accountId: str,
                webPropertyId: str,
                profileId: str,
                start_index: int = ...,
                max_results: int = ...,
                **kwargs: typing.Any
            ) -> GoalsHttpRequest: ...
        class CustomDimensionsResource(googleapiclient.discovery.Resource):
            def get(
                self,
                *,
                accountId: str,
                webPropertyId: str,
                customDimensionId: str,
                **kwargs: typing.Any
            ) -> CustomDimensionHttpRequest: ...
            def patch(
                self,
                *,
                accountId: str,
                webPropertyId: str,
                customDimensionId: str,
                body: CustomDimension = ...,
                ignoreCustomDataSourceLinks: bool = ...,
                **kwargs: typing.Any
            ) -> CustomDimensionHttpRequest: ...
            def insert(
                self,
                *,
                accountId: str,
                webPropertyId: str,
                body: CustomDimension = ...,
                **kwargs: typing.Any
            ) -> CustomDimensionHttpRequest: ...
            def update(
                self,
                *,
                accountId: str,
                webPropertyId: str,
                customDimensionId: str,
                body: CustomDimension = ...,
                ignoreCustomDataSourceLinks: bool = ...,
                **kwargs: typing.Any
            ) -> CustomDimensionHttpRequest: ...
            def list(
                self,
                *,
                accountId: str,
                webPropertyId: str,
                max_results: int = ...,
                start_index: int = ...,
                **kwargs: typing.Any
            ) -> CustomDimensionsHttpRequest: ...
        class RemarketingAudienceResource(googleapiclient.discovery.Resource):
            def list(
                self,
                *,
                accountId: str,
                webPropertyId: str,
                type: str = ...,
                max_results: int = ...,
                start_index: int = ...,
                **kwargs: typing.Any
            ) -> RemarketingAudiencesHttpRequest: ...
            def update(
                self,
                *,
                accountId: str,
                webPropertyId: str,
                remarketingAudienceId: str,
                body: RemarketingAudience = ...,
                **kwargs: typing.Any
            ) -> RemarketingAudienceHttpRequest: ...
            def patch(
                self,
                *,
                accountId: str,
                webPropertyId: str,
                remarketingAudienceId: str,
                body: RemarketingAudience = ...,
                **kwargs: typing.Any
            ) -> RemarketingAudienceHttpRequest: ...
            def delete(
                self,
                *,
                accountId: str,
                webPropertyId: str,
                remarketingAudienceId: str,
                **kwargs: typing.Any
            ) -> googleapiclient.http.HttpRequest: ...
            def get(
                self,
                *,
                accountId: str,
                webPropertyId: str,
                remarketingAudienceId: str,
                **kwargs: typing.Any
            ) -> RemarketingAudienceHttpRequest: ...
            def insert(
                self,
                *,
                accountId: str,
                webPropertyId: str,
                body: RemarketingAudience = ...,
                **kwargs: typing.Any
            ) -> RemarketingAudienceHttpRequest: ...
        class WebpropertiesResource(googleapiclient.discovery.Resource):
            def update(
                self,
                *,
                accountId: str,
                webPropertyId: str,
                body: Webproperty = ...,
                **kwargs: typing.Any
            ) -> WebpropertyHttpRequest: ...
            def get(
                self, *, accountId: str, webPropertyId: str, **kwargs: typing.Any
            ) -> WebpropertyHttpRequest: ...
            def list(
                self,
                *,
                accountId: str,
                max_results: int = ...,
                start_index: int = ...,
                **kwargs: typing.Any
            ) -> WebpropertiesHttpRequest: ...
            def insert(
                self, *, accountId: str, body: Webproperty = ..., **kwargs: typing.Any
            ) -> WebpropertyHttpRequest: ...
            def patch(
                self,
                *,
                accountId: str,
                webPropertyId: str,
                body: Webproperty = ...,
                **kwargs: typing.Any
            ) -> WebpropertyHttpRequest: ...
        class UnsampledReportsResource(googleapiclient.discovery.Resource):
            def delete(
                self,
                *,
                accountId: str,
                webPropertyId: str,
                profileId: str,
                unsampledReportId: str,
                **kwargs: typing.Any
            ) -> googleapiclient.http.HttpRequest: ...
            def insert(
                self,
                *,
                accountId: str,
                webPropertyId: str,
                profileId: str,
                body: UnsampledReport = ...,
                **kwargs: typing.Any
            ) -> UnsampledReportHttpRequest: ...
            def get(
                self,
                *,
                accountId: str,
                webPropertyId: str,
                profileId: str,
                unsampledReportId: str,
                **kwargs: typing.Any
            ) -> UnsampledReportHttpRequest: ...
            def list(
                self,
                *,
                accountId: str,
                webPropertyId: str,
                profileId: str,
                max_results: int = ...,
                start_index: int = ...,
                **kwargs: typing.Any
            ) -> UnsampledReportsHttpRequest: ...
        class CustomMetricsResource(googleapiclient.discovery.Resource):
            def patch(
                self,
                *,
                accountId: str,
                webPropertyId: str,
                customMetricId: str,
                body: CustomMetric = ...,
                ignoreCustomDataSourceLinks: bool = ...,
                **kwargs: typing.Any
            ) -> CustomMetricHttpRequest: ...
            def list(
                self,
                *,
                accountId: str,
                webPropertyId: str,
                start_index: int = ...,
                max_results: int = ...,
                **kwargs: typing.Any
            ) -> CustomMetricsHttpRequest: ...
            def get(
                self,
                *,
                accountId: str,
                webPropertyId: str,
                customMetricId: str,
                **kwargs: typing.Any
            ) -> CustomMetricHttpRequest: ...
            def insert(
                self,
                *,
                accountId: str,
                webPropertyId: str,
                body: CustomMetric = ...,
                **kwargs: typing.Any
            ) -> CustomMetricHttpRequest: ...
            def update(
                self,
                *,
                accountId: str,
                webPropertyId: str,
                customMetricId: str,
                body: CustomMetric = ...,
                ignoreCustomDataSourceLinks: bool = ...,
                **kwargs: typing.Any
            ) -> CustomMetricHttpRequest: ...
        class ExperimentsResource(googleapiclient.discovery.Resource):
            def update(
                self,
                *,
                accountId: str,
                webPropertyId: str,
                profileId: str,
                experimentId: str,
                body: Experiment = ...,
                **kwargs: typing.Any
            ) -> ExperimentHttpRequest: ...
            def get(
                self,
                *,
                accountId: str,
                webPropertyId: str,
                profileId: str,
                experimentId: str,
                **kwargs: typing.Any
            ) -> ExperimentHttpRequest: ...
            def delete(
                self,
                *,
                accountId: str,
                webPropertyId: str,
                profileId: str,
                experimentId: str,
                **kwargs: typing.Any
            ) -> googleapiclient.http.HttpRequest: ...
            def list(
                self,
                *,
                accountId: str,
                webPropertyId: str,
                profileId: str,
                start_index: int = ...,
                max_results: int = ...,
                **kwargs: typing.Any
            ) -> ExperimentsHttpRequest: ...
            def patch(
                self,
                *,
                accountId: str,
                webPropertyId: str,
                profileId: str,
                experimentId: str,
                body: Experiment = ...,
                **kwargs: typing.Any
            ) -> ExperimentHttpRequest: ...
            def insert(
                self,
                *,
                accountId: str,
                webPropertyId: str,
                profileId: str,
                body: Experiment = ...,
                **kwargs: typing.Any
            ) -> ExperimentHttpRequest: ...
        class SegmentsResource(googleapiclient.discovery.Resource):
            def list(
                self,
                *,
                max_results: int = ...,
                start_index: int = ...,
                **kwargs: typing.Any
            ) -> SegmentsHttpRequest: ...
        def profileUserLinks(self) -> ProfileUserLinksResource: ...
        def profileFilterLinks(self) -> ProfileFilterLinksResource: ...
        def profiles(self) -> ProfilesResource: ...
        def accountSummaries(self) -> AccountSummariesResource: ...
        def filters(self) -> FiltersResource: ...
        def customDataSources(self) -> CustomDataSourcesResource: ...
        def clientId(self) -> ClientIdResource: ...
        def uploads(self) -> UploadsResource: ...
        def webpropertyUserLinks(self) -> WebpropertyUserLinksResource: ...
        def accountUserLinks(self) -> AccountUserLinksResource: ...
        def webPropertyAdWordsLinks(self) -> WebPropertyAdWordsLinksResource: ...
        def accounts(self) -> AccountsResource: ...
        def goals(self) -> GoalsResource: ...
        def customDimensions(self) -> CustomDimensionsResource: ...
        def remarketingAudience(self) -> RemarketingAudienceResource: ...
        def webproperties(self) -> WebpropertiesResource: ...
        def unsampledReports(self) -> UnsampledReportsResource: ...
        def customMetrics(self) -> CustomMetricsResource: ...
        def experiments(self) -> ExperimentsResource: ...
        def segments(self) -> SegmentsResource: ...
    class ProvisioningResource(googleapiclient.discovery.Resource):
        def createAccountTicket(
            self, *, body: AccountTicket = ..., **kwargs: typing.Any
        ) -> AccountTicketHttpRequest: ...
        def createAccountTree(
            self, *, body: AccountTreeRequest = ..., **kwargs: typing.Any
        ) -> AccountTreeResponseHttpRequest: ...
    def metadata(self) -> MetadataResource: ...
    def data(self) -> DataResource: ...
    def userDeletion(self) -> UserDeletionResource: ...
    def management(self) -> ManagementResource: ...
    def provisioning(self) -> ProvisioningResource: ...

class AccountsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Accounts: ...

class EntityUserLinksHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> EntityUserLinks: ...

class RemarketingAudienceHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> RemarketingAudience: ...

class CustomMetricsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> CustomMetrics: ...

class CustomDimensionsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> CustomDimensions: ...

class GoalsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Goals: ...

class AccountSummariesHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> AccountSummaries: ...

class UnsampledReportsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> UnsampledReports: ...

class UserDeletionRequestHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> UserDeletionRequest: ...

class HashClientIdResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> HashClientIdResponse: ...

class ExperimentHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Experiment: ...

class EntityAdWordsLinksHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> EntityAdWordsLinks: ...

class AccountTreeResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> AccountTreeResponse: ...

class ExperimentsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Experiments: ...

class ProfilesHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Profiles: ...

class ProfileFilterLinksHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ProfileFilterLinks: ...

class CustomDataSourcesHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> CustomDataSources: ...

class FiltersHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Filters: ...

class UnsampledReportHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> UnsampledReport: ...

class McfDataHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> McfData: ...

class ColumnsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Columns: ...

class GaDataHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GaData: ...

class RealtimeDataHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> RealtimeData: ...

class UploadsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Uploads: ...

class CustomDimensionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> CustomDimension: ...

class EntityUserLinkHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> EntityUserLink: ...

class CustomMetricHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> CustomMetric: ...

class RemarketingAudiencesHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> RemarketingAudiences: ...

class FilterHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Filter: ...

class WebpropertiesHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Webproperties: ...

class ProfileHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Profile: ...

class EntityAdWordsLinkHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> EntityAdWordsLink: ...

class SegmentsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Segments: ...

class AccountTicketHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> AccountTicket: ...

class GoalHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Goal: ...

class UploadHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Upload: ...

class ProfileFilterLinkHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ProfileFilterLink: ...

class WebpropertyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Webproperty: ...
