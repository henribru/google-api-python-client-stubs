import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class MonitoringResource(googleapiclient.discovery.Resource):
    class ServicesResource(googleapiclient.discovery.Resource):
        class ServiceLevelObjectivesResource(googleapiclient.discovery.Resource):
            def get(
                self,
                *,
                name: str,
                view: typing_extensions.Literal[
                    "VIEW_UNSPECIFIED", "FULL", "EXPLICIT"
                ] = ...,
                **kwargs: typing.Any
            ) -> ServiceLevelObjectiveHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageToken: str = ...,
                view: typing_extensions.Literal[
                    "VIEW_UNSPECIFIED", "FULL", "EXPLICIT"
                ] = ...,
                filter: str = ...,
                pageSize: int = ...,
                **kwargs: typing.Any
            ) -> ListServiceLevelObjectivesResponseHttpRequest: ...
            def create(
                self,
                *,
                parent: str,
                body: ServiceLevelObjective = ...,
                serviceLevelObjectiveId: str = ...,
                **kwargs: typing.Any
            ) -> ServiceLevelObjectiveHttpRequest: ...
            def patch(
                self,
                *,
                name: str,
                body: ServiceLevelObjective = ...,
                updateMask: str = ...,
                **kwargs: typing.Any
            ) -> ServiceLevelObjectiveHttpRequest: ...
        def get(self, *, name: str, **kwargs: typing.Any) -> ServiceHttpRequest: ...
        def delete(self, *, name: str, **kwargs: typing.Any) -> EmptyHttpRequest: ...
        def patch(
            self,
            *,
            name: str,
            body: Service = ...,
            updateMask: str = ...,
            **kwargs: typing.Any
        ) -> ServiceHttpRequest: ...
        def create(
            self,
            *,
            parent: str,
            body: Service = ...,
            serviceId: str = ...,
            **kwargs: typing.Any
        ) -> ServiceHttpRequest: ...
        def list(
            self,
            *,
            parent: str,
            filter: str = ...,
            pageSize: int = ...,
            pageToken: str = ...,
            **kwargs: typing.Any
        ) -> ListServicesResponseHttpRequest: ...
        def serviceLevelObjectives(self) -> ServiceLevelObjectivesResource: ...
    class ProjectsResource(googleapiclient.discovery.Resource):
        class TimeSeriesResource(googleapiclient.discovery.Resource):
            def query(
                self,
                *,
                name: str,
                body: QueryTimeSeriesRequest = ...,
                **kwargs: typing.Any
            ) -> QueryTimeSeriesResponseHttpRequest: ...
            def list(
                self,
                *,
                name: str,
                interval_startTime: str = ...,
                aggregation_alignmentPeriod: str = ...,
                view: typing_extensions.Literal["FULL", "HEADERS"] = ...,
                pageSize: int = ...,
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
                aggregation_groupByFields: typing.Union[str, typing.List[str]] = ...,
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
                orderBy: str = ...,
                filter: str = ...,
                interval_endTime: str = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> ListTimeSeriesResponseHttpRequest: ...
            def create(
                self,
                *,
                name: str,
                body: CreateTimeSeriesRequest = ...,
                **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
        class MetricDescriptorsResource(googleapiclient.discovery.Resource):
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def list(
                self,
                *,
                name: str,
                pageSize: int = ...,
                filter: str = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> ListMetricDescriptorsResponseHttpRequest: ...
            def create(
                self, *, name: str, body: MetricDescriptor = ..., **kwargs: typing.Any
            ) -> MetricDescriptorHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> MetricDescriptorHttpRequest: ...
        class MonitoredResourceDescriptorsResource(googleapiclient.discovery.Resource):
            def list(
                self,
                *,
                name: str,
                pageSize: int = ...,
                pageToken: str = ...,
                filter: str = ...,
                **kwargs: typing.Any
            ) -> ListMonitoredResourceDescriptorsResponseHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> MonitoredResourceDescriptorHttpRequest: ...
        class CollectdTimeSeriesResource(googleapiclient.discovery.Resource):
            def create(
                self,
                *,
                name: str,
                body: CreateCollectdTimeSeriesRequest = ...,
                **kwargs: typing.Any
            ) -> CreateCollectdTimeSeriesResponseHttpRequest: ...
        class UptimeCheckConfigsResource(googleapiclient.discovery.Resource):
            def list(
                self,
                *,
                parent: str,
                pageToken: str = ...,
                pageSize: int = ...,
                **kwargs: typing.Any
            ) -> ListUptimeCheckConfigsResponseHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def patch(
                self,
                *,
                name: str,
                body: UptimeCheckConfig = ...,
                updateMask: str = ...,
                **kwargs: typing.Any
            ) -> UptimeCheckConfigHttpRequest: ...
            def create(
                self,
                *,
                parent: str,
                body: UptimeCheckConfig = ...,
                **kwargs: typing.Any
            ) -> UptimeCheckConfigHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> UptimeCheckConfigHttpRequest: ...
        class GroupsResource(googleapiclient.discovery.Resource):
            class MembersResource(googleapiclient.discovery.Resource):
                def list(
                    self,
                    *,
                    name: str,
                    interval_startTime: str = ...,
                    interval_endTime: str = ...,
                    filter: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> ListGroupMembersResponseHttpRequest: ...
            def delete(
                self, *, name: str, recursive: bool = ..., **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def get(self, *, name: str, **kwargs: typing.Any) -> GroupHttpRequest: ...
            def update(
                self,
                *,
                name: str,
                body: Group = ...,
                validateOnly: bool = ...,
                **kwargs: typing.Any
            ) -> GroupHttpRequest: ...
            def list(
                self,
                *,
                name: str,
                pageToken: str = ...,
                childrenOfGroup: str = ...,
                pageSize: int = ...,
                ancestorsOfGroup: str = ...,
                descendantsOfGroup: str = ...,
                **kwargs: typing.Any
            ) -> ListGroupsResponseHttpRequest: ...
            def create(
                self,
                *,
                name: str,
                body: Group = ...,
                validateOnly: bool = ...,
                **kwargs: typing.Any
            ) -> GroupHttpRequest: ...
            def members(self) -> MembersResource: ...
        class NotificationChannelsResource(googleapiclient.discovery.Resource):
            def sendVerificationCode(
                self,
                *,
                name: str,
                body: SendNotificationChannelVerificationCodeRequest = ...,
                **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def delete(
                self, *, name: str, force: bool = ..., **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def getVerificationCode(
                self,
                *,
                name: str,
                body: GetNotificationChannelVerificationCodeRequest = ...,
                **kwargs: typing.Any
            ) -> GetNotificationChannelVerificationCodeResponseHttpRequest: ...
            def create(
                self,
                *,
                name: str,
                body: NotificationChannel = ...,
                **kwargs: typing.Any
            ) -> NotificationChannelHttpRequest: ...
            def patch(
                self,
                *,
                name: str,
                body: NotificationChannel = ...,
                updateMask: str = ...,
                **kwargs: typing.Any
            ) -> NotificationChannelHttpRequest: ...
            def list(
                self,
                *,
                name: str,
                orderBy: str = ...,
                filter: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> ListNotificationChannelsResponseHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> NotificationChannelHttpRequest: ...
            def verify(
                self,
                *,
                name: str,
                body: VerifyNotificationChannelRequest = ...,
                **kwargs: typing.Any
            ) -> NotificationChannelHttpRequest: ...
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
        class AlertPoliciesResource(googleapiclient.discovery.Resource):
            def create(
                self, *, name: str, body: AlertPolicy = ..., **kwargs: typing.Any
            ) -> AlertPolicyHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def list(
                self,
                *,
                name: str,
                orderBy: str = ...,
                pageSize: int = ...,
                filter: str = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> ListAlertPoliciesResponseHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> AlertPolicyHttpRequest: ...
            def patch(
                self,
                *,
                name: str,
                body: AlertPolicy = ...,
                updateMask: str = ...,
                **kwargs: typing.Any
            ) -> AlertPolicyHttpRequest: ...
        def timeSeries(self) -> TimeSeriesResource: ...
        def metricDescriptors(self) -> MetricDescriptorsResource: ...
        def monitoredResourceDescriptors(
            self,
        ) -> MonitoredResourceDescriptorsResource: ...
        def collectdTimeSeries(self) -> CollectdTimeSeriesResource: ...
        def uptimeCheckConfigs(self) -> UptimeCheckConfigsResource: ...
        def groups(self) -> GroupsResource: ...
        def notificationChannels(self) -> NotificationChannelsResource: ...
        def notificationChannelDescriptors(
            self,
        ) -> NotificationChannelDescriptorsResource: ...
        def alertPolicies(self) -> AlertPoliciesResource: ...
    class UptimeCheckIpsResource(googleapiclient.discovery.Resource):
        def list(
            self, *, pageToken: str = ..., pageSize: int = ..., **kwargs: typing.Any
        ) -> ListUptimeCheckIpsResponseHttpRequest: ...
    def services(self) -> ServicesResource: ...
    def projects(self) -> ProjectsResource: ...
    def uptimeCheckIps(self) -> UptimeCheckIpsResource: ...

class ListUptimeCheckIpsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListUptimeCheckIpsResponse: ...

class ListServicesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListServicesResponse: ...

class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Empty: ...

class ListGroupsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListGroupsResponse: ...

class ListTimeSeriesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListTimeSeriesResponse: ...

class ListNotificationChannelDescriptorsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListNotificationChannelDescriptorsResponse: ...

class UptimeCheckConfigHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> UptimeCheckConfig: ...

class MonitoredResourceDescriptorHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> MonitoredResourceDescriptor: ...

class ListGroupMembersResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListGroupMembersResponse: ...

class ListNotificationChannelsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListNotificationChannelsResponse: ...

class GroupHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Group: ...

class ListMonitoredResourceDescriptorsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListMonitoredResourceDescriptorsResponse: ...

class ListServiceLevelObjectivesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListServiceLevelObjectivesResponse: ...

class ListAlertPoliciesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListAlertPoliciesResponse: ...

class ServiceLevelObjectiveHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ServiceLevelObjective: ...

class NotificationChannelDescriptorHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> NotificationChannelDescriptor: ...

class QueryTimeSeriesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> QueryTimeSeriesResponse: ...

class ListUptimeCheckConfigsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListUptimeCheckConfigsResponse: ...

class MetricDescriptorHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> MetricDescriptor: ...

class GetNotificationChannelVerificationCodeResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GetNotificationChannelVerificationCodeResponse: ...

class ListMetricDescriptorsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListMetricDescriptorsResponse: ...

class AlertPolicyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> AlertPolicy: ...

class NotificationChannelHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> NotificationChannel: ...

class CreateCollectdTimeSeriesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> CreateCollectdTimeSeriesResponse: ...

class ServiceHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Service: ...
