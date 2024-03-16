import collections.abc
import typing

import httplib2
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http

from .schemas import *

_list = list

@typing.type_check_only
class PlaydeveloperreportingResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class AnomaliesResource(googleapiclient.discovery.Resource):
        def list(
            self,
            *,
            parent: str,
            filter: str = ...,
            pageSize: int = ...,
            pageToken: str = ...,
            **kwargs: typing.Any,
        ) -> GooglePlayDeveloperReportingV1beta1ListAnomaliesResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: GooglePlayDeveloperReportingV1beta1ListAnomaliesResponseHttpRequest,
            previous_response: GooglePlayDeveloperReportingV1beta1ListAnomaliesResponse,
        ) -> (
            GooglePlayDeveloperReportingV1beta1ListAnomaliesResponseHttpRequest | None
        ): ...

    @typing.type_check_only
    class AppsResource(googleapiclient.discovery.Resource):
        def fetchReleaseFilterOptions(
            self, *, name: str, **kwargs: typing.Any
        ) -> GooglePlayDeveloperReportingV1beta1ReleaseFilterOptionsHttpRequest: ...
        def search(
            self, *, pageSize: int = ..., pageToken: str = ..., **kwargs: typing.Any
        ) -> (
            GooglePlayDeveloperReportingV1beta1SearchAccessibleAppsResponseHttpRequest
        ): ...
        def search_next(
            self,
            previous_request: GooglePlayDeveloperReportingV1beta1SearchAccessibleAppsResponseHttpRequest,
            previous_response: GooglePlayDeveloperReportingV1beta1SearchAccessibleAppsResponse,
        ) -> (
            GooglePlayDeveloperReportingV1beta1SearchAccessibleAppsResponseHttpRequest
            | None
        ): ...

    @typing.type_check_only
    class VitalsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class AnrrateResource(googleapiclient.discovery.Resource):
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GooglePlayDeveloperReportingV1beta1AnrRateMetricSetHttpRequest: ...
            def query(
                self,
                *,
                name: str,
                body: GooglePlayDeveloperReportingV1beta1QueryAnrRateMetricSetRequest = ...,
                **kwargs: typing.Any,
            ) -> GooglePlayDeveloperReportingV1beta1QueryAnrRateMetricSetResponseHttpRequest: ...
            def query_next(
                self,
                previous_request: GooglePlayDeveloperReportingV1beta1QueryAnrRateMetricSetResponseHttpRequest,
                previous_response: GooglePlayDeveloperReportingV1beta1QueryAnrRateMetricSetResponse,
            ) -> (
                GooglePlayDeveloperReportingV1beta1QueryAnrRateMetricSetResponseHttpRequest
                | None
            ): ...

        @typing.type_check_only
        class CrashrateResource(googleapiclient.discovery.Resource):
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GooglePlayDeveloperReportingV1beta1CrashRateMetricSetHttpRequest: ...
            def query(
                self,
                *,
                name: str,
                body: GooglePlayDeveloperReportingV1beta1QueryCrashRateMetricSetRequest = ...,
                **kwargs: typing.Any,
            ) -> GooglePlayDeveloperReportingV1beta1QueryCrashRateMetricSetResponseHttpRequest: ...
            def query_next(
                self,
                previous_request: GooglePlayDeveloperReportingV1beta1QueryCrashRateMetricSetResponseHttpRequest,
                previous_response: GooglePlayDeveloperReportingV1beta1QueryCrashRateMetricSetResponse,
            ) -> (
                GooglePlayDeveloperReportingV1beta1QueryCrashRateMetricSetResponseHttpRequest
                | None
            ): ...

        @typing.type_check_only
        class ErrorsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class CountsResource(googleapiclient.discovery.Resource):
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> (
                    GooglePlayDeveloperReportingV1beta1ErrorCountMetricSetHttpRequest
                ): ...
                def query(
                    self,
                    *,
                    name: str,
                    body: GooglePlayDeveloperReportingV1beta1QueryErrorCountMetricSetRequest = ...,
                    **kwargs: typing.Any,
                ) -> GooglePlayDeveloperReportingV1beta1QueryErrorCountMetricSetResponseHttpRequest: ...
                def query_next(
                    self,
                    previous_request: GooglePlayDeveloperReportingV1beta1QueryErrorCountMetricSetResponseHttpRequest,
                    previous_response: GooglePlayDeveloperReportingV1beta1QueryErrorCountMetricSetResponse,
                ) -> (
                    GooglePlayDeveloperReportingV1beta1QueryErrorCountMetricSetResponseHttpRequest
                    | None
                ): ...

            @typing.type_check_only
            class IssuesResource(googleapiclient.discovery.Resource):
                def search(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    interval_endTime_day: int = ...,
                    interval_endTime_hours: int = ...,
                    interval_endTime_minutes: int = ...,
                    interval_endTime_month: int = ...,
                    interval_endTime_nanos: int = ...,
                    interval_endTime_seconds: int = ...,
                    interval_endTime_timeZone_id: str = ...,
                    interval_endTime_timeZone_version: str = ...,
                    interval_endTime_utcOffset: str = ...,
                    interval_endTime_year: int = ...,
                    interval_startTime_day: int = ...,
                    interval_startTime_hours: int = ...,
                    interval_startTime_minutes: int = ...,
                    interval_startTime_month: int = ...,
                    interval_startTime_nanos: int = ...,
                    interval_startTime_seconds: int = ...,
                    interval_startTime_timeZone_id: str = ...,
                    interval_startTime_timeZone_version: str = ...,
                    interval_startTime_utcOffset: str = ...,
                    interval_startTime_year: int = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    sampleErrorReportLimit: int = ...,
                    **kwargs: typing.Any,
                ) -> GooglePlayDeveloperReportingV1beta1SearchErrorIssuesResponseHttpRequest: ...
                def search_next(
                    self,
                    previous_request: GooglePlayDeveloperReportingV1beta1SearchErrorIssuesResponseHttpRequest,
                    previous_response: GooglePlayDeveloperReportingV1beta1SearchErrorIssuesResponse,
                ) -> (
                    GooglePlayDeveloperReportingV1beta1SearchErrorIssuesResponseHttpRequest
                    | None
                ): ...

            @typing.type_check_only
            class ReportsResource(googleapiclient.discovery.Resource):
                def search(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    interval_endTime_day: int = ...,
                    interval_endTime_hours: int = ...,
                    interval_endTime_minutes: int = ...,
                    interval_endTime_month: int = ...,
                    interval_endTime_nanos: int = ...,
                    interval_endTime_seconds: int = ...,
                    interval_endTime_timeZone_id: str = ...,
                    interval_endTime_timeZone_version: str = ...,
                    interval_endTime_utcOffset: str = ...,
                    interval_endTime_year: int = ...,
                    interval_startTime_day: int = ...,
                    interval_startTime_hours: int = ...,
                    interval_startTime_minutes: int = ...,
                    interval_startTime_month: int = ...,
                    interval_startTime_nanos: int = ...,
                    interval_startTime_seconds: int = ...,
                    interval_startTime_timeZone_id: str = ...,
                    interval_startTime_timeZone_version: str = ...,
                    interval_startTime_utcOffset: str = ...,
                    interval_startTime_year: int = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> GooglePlayDeveloperReportingV1beta1SearchErrorReportsResponseHttpRequest: ...
                def search_next(
                    self,
                    previous_request: GooglePlayDeveloperReportingV1beta1SearchErrorReportsResponseHttpRequest,
                    previous_response: GooglePlayDeveloperReportingV1beta1SearchErrorReportsResponse,
                ) -> (
                    GooglePlayDeveloperReportingV1beta1SearchErrorReportsResponseHttpRequest
                    | None
                ): ...

            def counts(self) -> CountsResource: ...
            def issues(self) -> IssuesResource: ...
            def reports(self) -> ReportsResource: ...

        @typing.type_check_only
        class ExcessivewakeuprateResource(googleapiclient.discovery.Resource):
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GooglePlayDeveloperReportingV1beta1ExcessiveWakeupRateMetricSetHttpRequest: ...
            def query(
                self,
                *,
                name: str,
                body: GooglePlayDeveloperReportingV1beta1QueryExcessiveWakeupRateMetricSetRequest = ...,
                **kwargs: typing.Any,
            ) -> GooglePlayDeveloperReportingV1beta1QueryExcessiveWakeupRateMetricSetResponseHttpRequest: ...
            def query_next(
                self,
                previous_request: GooglePlayDeveloperReportingV1beta1QueryExcessiveWakeupRateMetricSetResponseHttpRequest,
                previous_response: GooglePlayDeveloperReportingV1beta1QueryExcessiveWakeupRateMetricSetResponse,
            ) -> (
                GooglePlayDeveloperReportingV1beta1QueryExcessiveWakeupRateMetricSetResponseHttpRequest
                | None
            ): ...

        @typing.type_check_only
        class SlowrenderingrateResource(googleapiclient.discovery.Resource):
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> (
                GooglePlayDeveloperReportingV1beta1SlowRenderingRateMetricSetHttpRequest
            ): ...
            def query(
                self,
                *,
                name: str,
                body: GooglePlayDeveloperReportingV1beta1QuerySlowRenderingRateMetricSetRequest = ...,
                **kwargs: typing.Any,
            ) -> GooglePlayDeveloperReportingV1beta1QuerySlowRenderingRateMetricSetResponseHttpRequest: ...
            def query_next(
                self,
                previous_request: GooglePlayDeveloperReportingV1beta1QuerySlowRenderingRateMetricSetResponseHttpRequest,
                previous_response: GooglePlayDeveloperReportingV1beta1QuerySlowRenderingRateMetricSetResponse,
            ) -> (
                GooglePlayDeveloperReportingV1beta1QuerySlowRenderingRateMetricSetResponseHttpRequest
                | None
            ): ...

        @typing.type_check_only
        class SlowstartrateResource(googleapiclient.discovery.Resource):
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> (
                GooglePlayDeveloperReportingV1beta1SlowStartRateMetricSetHttpRequest
            ): ...
            def query(
                self,
                *,
                name: str,
                body: GooglePlayDeveloperReportingV1beta1QuerySlowStartRateMetricSetRequest = ...,
                **kwargs: typing.Any,
            ) -> GooglePlayDeveloperReportingV1beta1QuerySlowStartRateMetricSetResponseHttpRequest: ...
            def query_next(
                self,
                previous_request: GooglePlayDeveloperReportingV1beta1QuerySlowStartRateMetricSetResponseHttpRequest,
                previous_response: GooglePlayDeveloperReportingV1beta1QuerySlowStartRateMetricSetResponse,
            ) -> (
                GooglePlayDeveloperReportingV1beta1QuerySlowStartRateMetricSetResponseHttpRequest
                | None
            ): ...

        @typing.type_check_only
        class StuckbackgroundwakelockrateResource(googleapiclient.discovery.Resource):
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GooglePlayDeveloperReportingV1beta1StuckBackgroundWakelockRateMetricSetHttpRequest: ...
            def query(
                self,
                *,
                name: str,
                body: GooglePlayDeveloperReportingV1beta1QueryStuckBackgroundWakelockRateMetricSetRequest = ...,
                **kwargs: typing.Any,
            ) -> GooglePlayDeveloperReportingV1beta1QueryStuckBackgroundWakelockRateMetricSetResponseHttpRequest: ...
            def query_next(
                self,
                previous_request: GooglePlayDeveloperReportingV1beta1QueryStuckBackgroundWakelockRateMetricSetResponseHttpRequest,
                previous_response: GooglePlayDeveloperReportingV1beta1QueryStuckBackgroundWakelockRateMetricSetResponse,
            ) -> (
                GooglePlayDeveloperReportingV1beta1QueryStuckBackgroundWakelockRateMetricSetResponseHttpRequest
                | None
            ): ...

        def anrrate(self) -> AnrrateResource: ...
        def crashrate(self) -> CrashrateResource: ...
        def errors(self) -> ErrorsResource: ...
        def excessivewakeuprate(self) -> ExcessivewakeuprateResource: ...
        def slowrenderingrate(self) -> SlowrenderingrateResource: ...
        def slowstartrate(self) -> SlowstartrateResource: ...
        def stuckbackgroundwakelockrate(
            self,
        ) -> StuckbackgroundwakelockrateResource: ...

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
    def anomalies(self) -> AnomaliesResource: ...
    def apps(self) -> AppsResource: ...
    def vitals(self) -> VitalsResource: ...

@typing.type_check_only
class GooglePlayDeveloperReportingV1beta1AnrRateMetricSetHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GooglePlayDeveloperReportingV1beta1AnrRateMetricSet: ...

@typing.type_check_only
class GooglePlayDeveloperReportingV1beta1CrashRateMetricSetHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GooglePlayDeveloperReportingV1beta1CrashRateMetricSet: ...

@typing.type_check_only
class GooglePlayDeveloperReportingV1beta1ErrorCountMetricSetHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GooglePlayDeveloperReportingV1beta1ErrorCountMetricSet: ...

@typing.type_check_only
class GooglePlayDeveloperReportingV1beta1ExcessiveWakeupRateMetricSetHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GooglePlayDeveloperReportingV1beta1ExcessiveWakeupRateMetricSet: ...

@typing.type_check_only
class GooglePlayDeveloperReportingV1beta1ListAnomaliesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GooglePlayDeveloperReportingV1beta1ListAnomaliesResponse: ...

@typing.type_check_only
class GooglePlayDeveloperReportingV1beta1QueryAnrRateMetricSetResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GooglePlayDeveloperReportingV1beta1QueryAnrRateMetricSetResponse: ...

@typing.type_check_only
class GooglePlayDeveloperReportingV1beta1QueryCrashRateMetricSetResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GooglePlayDeveloperReportingV1beta1QueryCrashRateMetricSetResponse: ...

@typing.type_check_only
class GooglePlayDeveloperReportingV1beta1QueryErrorCountMetricSetResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GooglePlayDeveloperReportingV1beta1QueryErrorCountMetricSetResponse: ...

@typing.type_check_only
class GooglePlayDeveloperReportingV1beta1QueryExcessiveWakeupRateMetricSetResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> (
        GooglePlayDeveloperReportingV1beta1QueryExcessiveWakeupRateMetricSetResponse
    ): ...

@typing.type_check_only
class GooglePlayDeveloperReportingV1beta1QuerySlowRenderingRateMetricSetResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GooglePlayDeveloperReportingV1beta1QuerySlowRenderingRateMetricSetResponse: ...

@typing.type_check_only
class GooglePlayDeveloperReportingV1beta1QuerySlowStartRateMetricSetResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GooglePlayDeveloperReportingV1beta1QuerySlowStartRateMetricSetResponse: ...

@typing.type_check_only
class GooglePlayDeveloperReportingV1beta1QueryStuckBackgroundWakelockRateMetricSetResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GooglePlayDeveloperReportingV1beta1QueryStuckBackgroundWakelockRateMetricSetResponse: ...

@typing.type_check_only
class GooglePlayDeveloperReportingV1beta1ReleaseFilterOptionsHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GooglePlayDeveloperReportingV1beta1ReleaseFilterOptions: ...

@typing.type_check_only
class GooglePlayDeveloperReportingV1beta1SearchAccessibleAppsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GooglePlayDeveloperReportingV1beta1SearchAccessibleAppsResponse: ...

@typing.type_check_only
class GooglePlayDeveloperReportingV1beta1SearchErrorIssuesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GooglePlayDeveloperReportingV1beta1SearchErrorIssuesResponse: ...

@typing.type_check_only
class GooglePlayDeveloperReportingV1beta1SearchErrorReportsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GooglePlayDeveloperReportingV1beta1SearchErrorReportsResponse: ...

@typing.type_check_only
class GooglePlayDeveloperReportingV1beta1SlowRenderingRateMetricSetHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GooglePlayDeveloperReportingV1beta1SlowRenderingRateMetricSet: ...

@typing.type_check_only
class GooglePlayDeveloperReportingV1beta1SlowStartRateMetricSetHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GooglePlayDeveloperReportingV1beta1SlowStartRateMetricSet: ...

@typing.type_check_only
class GooglePlayDeveloperReportingV1beta1StuckBackgroundWakelockRateMetricSetHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GooglePlayDeveloperReportingV1beta1StuckBackgroundWakelockRateMetricSet: ...
