import collections.abc
import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

_list = list

@typing.type_check_only
class MonitoringResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class FoldersResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class TimeSeriesResource(googleapiclient.discovery.Resource):
            def list(
                self,
                *,
                name: str,
                aggregation_alignmentPeriod: str = ...,
                aggregation_crossSeriesReducer: typing_extensions.Literal[
                    "REDUCE_NONE",
                    "REDUCE_MEAN",
                    "REDUCE_MIN",
                    "REDUCE_MAX",
                    "REDUCE_SUM",
                    "REDUCE_STDDEV",
                    "REDUCE_COUNT",
                    "REDUCE_COUNT_TRUE",
                    "REDUCE_COUNT_FALSE",
                    "REDUCE_FRACTION_TRUE",
                    "REDUCE_PERCENTILE_99",
                    "REDUCE_PERCENTILE_95",
                    "REDUCE_PERCENTILE_50",
                    "REDUCE_PERCENTILE_05",
                ] = ...,
                aggregation_groupByFields: str | _list[str] = ...,
                aggregation_perSeriesAligner: typing_extensions.Literal[
                    "ALIGN_NONE",
                    "ALIGN_DELTA",
                    "ALIGN_RATE",
                    "ALIGN_INTERPOLATE",
                    "ALIGN_NEXT_OLDER",
                    "ALIGN_MIN",
                    "ALIGN_MAX",
                    "ALIGN_MEAN",
                    "ALIGN_COUNT",
                    "ALIGN_SUM",
                    "ALIGN_STDDEV",
                    "ALIGN_COUNT_TRUE",
                    "ALIGN_COUNT_FALSE",
                    "ALIGN_FRACTION_TRUE",
                    "ALIGN_PERCENTILE_99",
                    "ALIGN_PERCENTILE_95",
                    "ALIGN_PERCENTILE_50",
                    "ALIGN_PERCENTILE_05",
                    "ALIGN_PERCENT_CHANGE",
                ] = ...,
                filter: str = ...,
                interval_endTime: str = ...,
                interval_startTime: str = ...,
                orderBy: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                secondaryAggregation_alignmentPeriod: str = ...,
                secondaryAggregation_crossSeriesReducer: typing_extensions.Literal[
                    "REDUCE_NONE",
                    "REDUCE_MEAN",
                    "REDUCE_MIN",
                    "REDUCE_MAX",
                    "REDUCE_SUM",
                    "REDUCE_STDDEV",
                    "REDUCE_COUNT",
                    "REDUCE_COUNT_TRUE",
                    "REDUCE_COUNT_FALSE",
                    "REDUCE_FRACTION_TRUE",
                    "REDUCE_PERCENTILE_99",
                    "REDUCE_PERCENTILE_95",
                    "REDUCE_PERCENTILE_50",
                    "REDUCE_PERCENTILE_05",
                ] = ...,
                secondaryAggregation_groupByFields: str | _list[str] = ...,
                secondaryAggregation_perSeriesAligner: typing_extensions.Literal[
                    "ALIGN_NONE",
                    "ALIGN_DELTA",
                    "ALIGN_RATE",
                    "ALIGN_INTERPOLATE",
                    "ALIGN_NEXT_OLDER",
                    "ALIGN_MIN",
                    "ALIGN_MAX",
                    "ALIGN_MEAN",
                    "ALIGN_COUNT",
                    "ALIGN_SUM",
                    "ALIGN_STDDEV",
                    "ALIGN_COUNT_TRUE",
                    "ALIGN_COUNT_FALSE",
                    "ALIGN_FRACTION_TRUE",
                    "ALIGN_PERCENTILE_99",
                    "ALIGN_PERCENTILE_95",
                    "ALIGN_PERCENTILE_50",
                    "ALIGN_PERCENTILE_05",
                    "ALIGN_PERCENT_CHANGE",
                ] = ...,
                view: typing_extensions.Literal["FULL", "HEADERS"] = ...,
                **kwargs: typing.Any
            ) -> ListTimeSeriesResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListTimeSeriesResponseHttpRequest,
                previous_response: ListTimeSeriesResponse,
            ) -> ListTimeSeriesResponseHttpRequest | None: ...

        def timeSeries(self) -> TimeSeriesResource: ...

    @typing.type_check_only
    class OrganizationsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class TimeSeriesResource(googleapiclient.discovery.Resource):
            def list(
                self,
                *,
                name: str,
                aggregation_alignmentPeriod: str = ...,
                aggregation_crossSeriesReducer: typing_extensions.Literal[
                    "REDUCE_NONE",
                    "REDUCE_MEAN",
                    "REDUCE_MIN",
                    "REDUCE_MAX",
                    "REDUCE_SUM",
                    "REDUCE_STDDEV",
                    "REDUCE_COUNT",
                    "REDUCE_COUNT_TRUE",
                    "REDUCE_COUNT_FALSE",
                    "REDUCE_FRACTION_TRUE",
                    "REDUCE_PERCENTILE_99",
                    "REDUCE_PERCENTILE_95",
                    "REDUCE_PERCENTILE_50",
                    "REDUCE_PERCENTILE_05",
                ] = ...,
                aggregation_groupByFields: str | _list[str] = ...,
                aggregation_perSeriesAligner: typing_extensions.Literal[
                    "ALIGN_NONE",
                    "ALIGN_DELTA",
                    "ALIGN_RATE",
                    "ALIGN_INTERPOLATE",
                    "ALIGN_NEXT_OLDER",
                    "ALIGN_MIN",
                    "ALIGN_MAX",
                    "ALIGN_MEAN",
                    "ALIGN_COUNT",
                    "ALIGN_SUM",
                    "ALIGN_STDDEV",
                    "ALIGN_COUNT_TRUE",
                    "ALIGN_COUNT_FALSE",
                    "ALIGN_FRACTION_TRUE",
                    "ALIGN_PERCENTILE_99",
                    "ALIGN_PERCENTILE_95",
                    "ALIGN_PERCENTILE_50",
                    "ALIGN_PERCENTILE_05",
                    "ALIGN_PERCENT_CHANGE",
                ] = ...,
                filter: str = ...,
                interval_endTime: str = ...,
                interval_startTime: str = ...,
                orderBy: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                secondaryAggregation_alignmentPeriod: str = ...,
                secondaryAggregation_crossSeriesReducer: typing_extensions.Literal[
                    "REDUCE_NONE",
                    "REDUCE_MEAN",
                    "REDUCE_MIN",
                    "REDUCE_MAX",
                    "REDUCE_SUM",
                    "REDUCE_STDDEV",
                    "REDUCE_COUNT",
                    "REDUCE_COUNT_TRUE",
                    "REDUCE_COUNT_FALSE",
                    "REDUCE_FRACTION_TRUE",
                    "REDUCE_PERCENTILE_99",
                    "REDUCE_PERCENTILE_95",
                    "REDUCE_PERCENTILE_50",
                    "REDUCE_PERCENTILE_05",
                ] = ...,
                secondaryAggregation_groupByFields: str | _list[str] = ...,
                secondaryAggregation_perSeriesAligner: typing_extensions.Literal[
                    "ALIGN_NONE",
                    "ALIGN_DELTA",
                    "ALIGN_RATE",
                    "ALIGN_INTERPOLATE",
                    "ALIGN_NEXT_OLDER",
                    "ALIGN_MIN",
                    "ALIGN_MAX",
                    "ALIGN_MEAN",
                    "ALIGN_COUNT",
                    "ALIGN_SUM",
                    "ALIGN_STDDEV",
                    "ALIGN_COUNT_TRUE",
                    "ALIGN_COUNT_FALSE",
                    "ALIGN_FRACTION_TRUE",
                    "ALIGN_PERCENTILE_99",
                    "ALIGN_PERCENTILE_95",
                    "ALIGN_PERCENTILE_50",
                    "ALIGN_PERCENTILE_05",
                    "ALIGN_PERCENT_CHANGE",
                ] = ...,
                view: typing_extensions.Literal["FULL", "HEADERS"] = ...,
                **kwargs: typing.Any
            ) -> ListTimeSeriesResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListTimeSeriesResponseHttpRequest,
                previous_response: ListTimeSeriesResponse,
            ) -> ListTimeSeriesResponseHttpRequest | None: ...

        def timeSeries(self) -> TimeSeriesResource: ...

    @typing.type_check_only
    class ProjectsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class AlertPoliciesResource(googleapiclient.discovery.Resource):
            def create(
                self, *, name: str, body: AlertPolicy = ..., **kwargs: typing.Any
            ) -> AlertPolicyHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> AlertPolicyHttpRequest: ...
            def list(
                self,
                *,
                name: str,
                filter: str = ...,
                orderBy: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> ListAlertPoliciesResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListAlertPoliciesResponseHttpRequest,
                previous_response: ListAlertPoliciesResponse,
            ) -> ListAlertPoliciesResponseHttpRequest | None: ...
            def patch(
                self,
                *,
                name: str,
                body: AlertPolicy = ...,
                updateMask: str = ...,
                **kwargs: typing.Any
            ) -> AlertPolicyHttpRequest: ...

        @typing.type_check_only
        class CollectdTimeSeriesResource(googleapiclient.discovery.Resource):
            def create(
                self,
                *,
                name: str,
                body: CreateCollectdTimeSeriesRequest = ...,
                **kwargs: typing.Any
            ) -> CreateCollectdTimeSeriesResponseHttpRequest: ...

        @typing.type_check_only
        class GroupsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class MembersResource(googleapiclient.discovery.Resource):
                def list(
                    self,
                    *,
                    name: str,
                    filter: str = ...,
                    interval_endTime: str = ...,
                    interval_startTime: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> ListGroupMembersResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListGroupMembersResponseHttpRequest,
                    previous_response: ListGroupMembersResponse,
                ) -> ListGroupMembersResponseHttpRequest | None: ...

            def create(
                self,
                *,
                name: str,
                body: Group = ...,
                validateOnly: bool = ...,
                **kwargs: typing.Any
            ) -> GroupHttpRequest: ...
            def delete(
                self, *, name: str, recursive: bool = ..., **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def get(self, *, name: str, **kwargs: typing.Any) -> GroupHttpRequest: ...
            def list(
                self,
                *,
                name: str,
                ancestorsOfGroup: str = ...,
                childrenOfGroup: str = ...,
                descendantsOfGroup: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> ListGroupsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListGroupsResponseHttpRequest,
                previous_response: ListGroupsResponse,
            ) -> ListGroupsResponseHttpRequest | None: ...
            def update(
                self,
                *,
                name: str,
                body: Group = ...,
                validateOnly: bool = ...,
                **kwargs: typing.Any
            ) -> GroupHttpRequest: ...
            def members(self) -> MembersResource: ...

        @typing.type_check_only
        class MetricDescriptorsResource(googleapiclient.discovery.Resource):
            def create(
                self, *, name: str, body: MetricDescriptor = ..., **kwargs: typing.Any
            ) -> MetricDescriptorHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> MetricDescriptorHttpRequest: ...
            def list(
                self,
                *,
                name: str,
                filter: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> ListMetricDescriptorsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListMetricDescriptorsResponseHttpRequest,
                previous_response: ListMetricDescriptorsResponse,
            ) -> ListMetricDescriptorsResponseHttpRequest | None: ...

        @typing.type_check_only
        class MonitoredResourceDescriptorsResource(googleapiclient.discovery.Resource):
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> MonitoredResourceDescriptorHttpRequest: ...
            def list(
                self,
                *,
                name: str,
                filter: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> ListMonitoredResourceDescriptorsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListMonitoredResourceDescriptorsResponseHttpRequest,
                previous_response: ListMonitoredResourceDescriptorsResponse,
            ) -> ListMonitoredResourceDescriptorsResponseHttpRequest | None: ...

        @typing.type_check_only
        class NotificationChannelDescriptorsResource(
            googleapiclient.discovery.Resource
        ):
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> NotificationChannelDescriptorHttpRequest: ...
            def list(
                self,
                *,
                name: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> ListNotificationChannelDescriptorsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListNotificationChannelDescriptorsResponseHttpRequest,
                previous_response: ListNotificationChannelDescriptorsResponse,
            ) -> ListNotificationChannelDescriptorsResponseHttpRequest | None: ...

        @typing.type_check_only
        class NotificationChannelsResource(googleapiclient.discovery.Resource):
            def create(
                self,
                *,
                name: str,
                body: NotificationChannel = ...,
                **kwargs: typing.Any
            ) -> NotificationChannelHttpRequest: ...
            def delete(
                self, *, name: str, force: bool = ..., **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> NotificationChannelHttpRequest: ...
            def getVerificationCode(
                self,
                *,
                name: str,
                body: GetNotificationChannelVerificationCodeRequest = ...,
                **kwargs: typing.Any
            ) -> GetNotificationChannelVerificationCodeResponseHttpRequest: ...
            def list(
                self,
                *,
                name: str,
                filter: str = ...,
                orderBy: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> ListNotificationChannelsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListNotificationChannelsResponseHttpRequest,
                previous_response: ListNotificationChannelsResponse,
            ) -> ListNotificationChannelsResponseHttpRequest | None: ...
            def patch(
                self,
                *,
                name: str,
                body: NotificationChannel = ...,
                updateMask: str = ...,
                **kwargs: typing.Any
            ) -> NotificationChannelHttpRequest: ...
            def sendVerificationCode(
                self,
                *,
                name: str,
                body: SendNotificationChannelVerificationCodeRequest = ...,
                **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def verify(
                self,
                *,
                name: str,
                body: VerifyNotificationChannelRequest = ...,
                **kwargs: typing.Any
            ) -> NotificationChannelHttpRequest: ...

        @typing.type_check_only
        class TimeSeriesResource(googleapiclient.discovery.Resource):
            def create(
                self,
                *,
                name: str,
                body: CreateTimeSeriesRequest = ...,
                **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def createService(
                self,
                *,
                name: str,
                body: CreateTimeSeriesRequest = ...,
                **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def list(
                self,
                *,
                name: str,
                aggregation_alignmentPeriod: str = ...,
                aggregation_crossSeriesReducer: typing_extensions.Literal[
                    "REDUCE_NONE",
                    "REDUCE_MEAN",
                    "REDUCE_MIN",
                    "REDUCE_MAX",
                    "REDUCE_SUM",
                    "REDUCE_STDDEV",
                    "REDUCE_COUNT",
                    "REDUCE_COUNT_TRUE",
                    "REDUCE_COUNT_FALSE",
                    "REDUCE_FRACTION_TRUE",
                    "REDUCE_PERCENTILE_99",
                    "REDUCE_PERCENTILE_95",
                    "REDUCE_PERCENTILE_50",
                    "REDUCE_PERCENTILE_05",
                ] = ...,
                aggregation_groupByFields: str | _list[str] = ...,
                aggregation_perSeriesAligner: typing_extensions.Literal[
                    "ALIGN_NONE",
                    "ALIGN_DELTA",
                    "ALIGN_RATE",
                    "ALIGN_INTERPOLATE",
                    "ALIGN_NEXT_OLDER",
                    "ALIGN_MIN",
                    "ALIGN_MAX",
                    "ALIGN_MEAN",
                    "ALIGN_COUNT",
                    "ALIGN_SUM",
                    "ALIGN_STDDEV",
                    "ALIGN_COUNT_TRUE",
                    "ALIGN_COUNT_FALSE",
                    "ALIGN_FRACTION_TRUE",
                    "ALIGN_PERCENTILE_99",
                    "ALIGN_PERCENTILE_95",
                    "ALIGN_PERCENTILE_50",
                    "ALIGN_PERCENTILE_05",
                    "ALIGN_PERCENT_CHANGE",
                ] = ...,
                filter: str = ...,
                interval_endTime: str = ...,
                interval_startTime: str = ...,
                orderBy: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                secondaryAggregation_alignmentPeriod: str = ...,
                secondaryAggregation_crossSeriesReducer: typing_extensions.Literal[
                    "REDUCE_NONE",
                    "REDUCE_MEAN",
                    "REDUCE_MIN",
                    "REDUCE_MAX",
                    "REDUCE_SUM",
                    "REDUCE_STDDEV",
                    "REDUCE_COUNT",
                    "REDUCE_COUNT_TRUE",
                    "REDUCE_COUNT_FALSE",
                    "REDUCE_FRACTION_TRUE",
                    "REDUCE_PERCENTILE_99",
                    "REDUCE_PERCENTILE_95",
                    "REDUCE_PERCENTILE_50",
                    "REDUCE_PERCENTILE_05",
                ] = ...,
                secondaryAggregation_groupByFields: str | _list[str] = ...,
                secondaryAggregation_perSeriesAligner: typing_extensions.Literal[
                    "ALIGN_NONE",
                    "ALIGN_DELTA",
                    "ALIGN_RATE",
                    "ALIGN_INTERPOLATE",
                    "ALIGN_NEXT_OLDER",
                    "ALIGN_MIN",
                    "ALIGN_MAX",
                    "ALIGN_MEAN",
                    "ALIGN_COUNT",
                    "ALIGN_SUM",
                    "ALIGN_STDDEV",
                    "ALIGN_COUNT_TRUE",
                    "ALIGN_COUNT_FALSE",
                    "ALIGN_FRACTION_TRUE",
                    "ALIGN_PERCENTILE_99",
                    "ALIGN_PERCENTILE_95",
                    "ALIGN_PERCENTILE_50",
                    "ALIGN_PERCENTILE_05",
                    "ALIGN_PERCENT_CHANGE",
                ] = ...,
                view: typing_extensions.Literal["FULL", "HEADERS"] = ...,
                **kwargs: typing.Any
            ) -> ListTimeSeriesResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListTimeSeriesResponseHttpRequest,
                previous_response: ListTimeSeriesResponse,
            ) -> ListTimeSeriesResponseHttpRequest | None: ...
            def query(
                self,
                *,
                name: str,
                body: QueryTimeSeriesRequest = ...,
                **kwargs: typing.Any
            ) -> QueryTimeSeriesResponseHttpRequest: ...
            def query_next(
                self,
                previous_request: QueryTimeSeriesResponseHttpRequest,
                previous_response: QueryTimeSeriesResponse,
            ) -> QueryTimeSeriesResponseHttpRequest | None: ...

        @typing.type_check_only
        class UptimeCheckConfigsResource(googleapiclient.discovery.Resource):
            def create(
                self,
                *,
                parent: str,
                body: UptimeCheckConfig = ...,
                **kwargs: typing.Any
            ) -> UptimeCheckConfigHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> UptimeCheckConfigHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                filter: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> ListUptimeCheckConfigsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListUptimeCheckConfigsResponseHttpRequest,
                previous_response: ListUptimeCheckConfigsResponse,
            ) -> ListUptimeCheckConfigsResponseHttpRequest | None: ...
            def patch(
                self,
                *,
                name: str,
                body: UptimeCheckConfig = ...,
                updateMask: str = ...,
                **kwargs: typing.Any
            ) -> UptimeCheckConfigHttpRequest: ...

        def alertPolicies(self) -> AlertPoliciesResource: ...
        def collectdTimeSeries(self) -> CollectdTimeSeriesResource: ...
        def groups(self) -> GroupsResource: ...
        def metricDescriptors(self) -> MetricDescriptorsResource: ...
        def monitoredResourceDescriptors(
            self,
        ) -> MonitoredResourceDescriptorsResource: ...
        def notificationChannelDescriptors(
            self,
        ) -> NotificationChannelDescriptorsResource: ...
        def notificationChannels(self) -> NotificationChannelsResource: ...
        def timeSeries(self) -> TimeSeriesResource: ...
        def uptimeCheckConfigs(self) -> UptimeCheckConfigsResource: ...

    @typing.type_check_only
    class ServicesResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class ServiceLevelObjectivesResource(googleapiclient.discovery.Resource):
            def create(
                self,
                *,
                parent: str,
                body: ServiceLevelObjective = ...,
                serviceLevelObjectiveId: str = ...,
                **kwargs: typing.Any
            ) -> ServiceLevelObjectiveHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def get(
                self,
                *,
                name: str,
                view: typing_extensions.Literal[
                    "VIEW_UNSPECIFIED", "FULL", "EXPLICIT"
                ] = ...,
                **kwargs: typing.Any
            ) -> ServiceLevelObjectiveHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                filter: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                view: typing_extensions.Literal[
                    "VIEW_UNSPECIFIED", "FULL", "EXPLICIT"
                ] = ...,
                **kwargs: typing.Any
            ) -> ListServiceLevelObjectivesResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListServiceLevelObjectivesResponseHttpRequest,
                previous_response: ListServiceLevelObjectivesResponse,
            ) -> ListServiceLevelObjectivesResponseHttpRequest | None: ...
            def patch(
                self,
                *,
                name: str,
                body: ServiceLevelObjective = ...,
                updateMask: str = ...,
                **kwargs: typing.Any
            ) -> ServiceLevelObjectiveHttpRequest: ...

        def create(
            self,
            *,
            parent: str,
            body: Service = ...,
            serviceId: str = ...,
            **kwargs: typing.Any
        ) -> ServiceHttpRequest: ...
        def delete(self, *, name: str, **kwargs: typing.Any) -> EmptyHttpRequest: ...
        def get(self, *, name: str, **kwargs: typing.Any) -> ServiceHttpRequest: ...
        def list(
            self,
            *,
            parent: str,
            filter: str = ...,
            pageSize: int = ...,
            pageToken: str = ...,
            **kwargs: typing.Any
        ) -> ListServicesResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: ListServicesResponseHttpRequest,
            previous_response: ListServicesResponse,
        ) -> ListServicesResponseHttpRequest | None: ...
        def patch(
            self,
            *,
            name: str,
            body: Service = ...,
            updateMask: str = ...,
            **kwargs: typing.Any
        ) -> ServiceHttpRequest: ...
        def serviceLevelObjectives(self) -> ServiceLevelObjectivesResource: ...

    @typing.type_check_only
    class UptimeCheckIpsResource(googleapiclient.discovery.Resource):
        def list(
            self, *, pageSize: int = ..., pageToken: str = ..., **kwargs: typing.Any
        ) -> ListUptimeCheckIpsResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: ListUptimeCheckIpsResponseHttpRequest,
            previous_response: ListUptimeCheckIpsResponse,
        ) -> ListUptimeCheckIpsResponseHttpRequest | None: ...

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
        | None = ...,
    ) -> googleapiclient.http.BatchHttpRequest: ...
    def folders(self) -> FoldersResource: ...
    def organizations(self) -> OrganizationsResource: ...
    def projects(self) -> ProjectsResource: ...
    def services(self) -> ServicesResource: ...
    def uptimeCheckIps(self) -> UptimeCheckIpsResource: ...

@typing.type_check_only
class AlertPolicyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> AlertPolicy: ...

@typing.type_check_only
class CreateCollectdTimeSeriesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> CreateCollectdTimeSeriesResponse: ...

@typing.type_check_only
class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Empty: ...

@typing.type_check_only
class GetNotificationChannelVerificationCodeResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GetNotificationChannelVerificationCodeResponse: ...

@typing.type_check_only
class GroupHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Group: ...

@typing.type_check_only
class ListAlertPoliciesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListAlertPoliciesResponse: ...

@typing.type_check_only
class ListGroupMembersResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListGroupMembersResponse: ...

@typing.type_check_only
class ListGroupsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListGroupsResponse: ...

@typing.type_check_only
class ListMetricDescriptorsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListMetricDescriptorsResponse: ...

@typing.type_check_only
class ListMonitoredResourceDescriptorsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListMonitoredResourceDescriptorsResponse: ...

@typing.type_check_only
class ListNotificationChannelDescriptorsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListNotificationChannelDescriptorsResponse: ...

@typing.type_check_only
class ListNotificationChannelsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListNotificationChannelsResponse: ...

@typing.type_check_only
class ListServiceLevelObjectivesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListServiceLevelObjectivesResponse: ...

@typing.type_check_only
class ListServicesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListServicesResponse: ...

@typing.type_check_only
class ListTimeSeriesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListTimeSeriesResponse: ...

@typing.type_check_only
class ListUptimeCheckConfigsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListUptimeCheckConfigsResponse: ...

@typing.type_check_only
class ListUptimeCheckIpsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListUptimeCheckIpsResponse: ...

@typing.type_check_only
class MetricDescriptorHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> MetricDescriptor: ...

@typing.type_check_only
class MonitoredResourceDescriptorHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> MonitoredResourceDescriptor: ...

@typing.type_check_only
class NotificationChannelHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> NotificationChannel: ...

@typing.type_check_only
class NotificationChannelDescriptorHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> NotificationChannelDescriptor: ...

@typing.type_check_only
class QueryTimeSeriesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> QueryTimeSeriesResponse: ...

@typing.type_check_only
class ServiceHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Service: ...

@typing.type_check_only
class ServiceLevelObjectiveHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ServiceLevelObjective: ...

@typing.type_check_only
class UptimeCheckConfigHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> UptimeCheckConfig: ...
