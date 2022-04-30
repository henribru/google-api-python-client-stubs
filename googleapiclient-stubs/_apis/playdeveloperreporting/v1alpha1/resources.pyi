import collections.abc
import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

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
            **kwargs: typing.Any
        ) -> GooglePlayDeveloperReportingV1alpha1ListAnomaliesResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: GooglePlayDeveloperReportingV1alpha1ListAnomaliesResponseHttpRequest,
            previous_response: GooglePlayDeveloperReportingV1alpha1ListAnomaliesResponse,
        ) -> GooglePlayDeveloperReportingV1alpha1ListAnomaliesResponseHttpRequest | None: ...

    @typing.type_check_only
    class VitalsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class AnrrateResource(googleapiclient.discovery.Resource):
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GooglePlayDeveloperReportingV1alpha1AnrRateMetricSetHttpRequest: ...
            def query(
                self,
                *,
                name: str,
                body: GooglePlayDeveloperReportingV1alpha1QueryAnrRateMetricSetRequest = ...,
                **kwargs: typing.Any
            ) -> GooglePlayDeveloperReportingV1alpha1QueryAnrRateMetricSetResponseHttpRequest: ...
            def query_next(
                self,
                previous_request: GooglePlayDeveloperReportingV1alpha1QueryAnrRateMetricSetResponseHttpRequest,
                previous_response: GooglePlayDeveloperReportingV1alpha1QueryAnrRateMetricSetResponse,
            ) -> GooglePlayDeveloperReportingV1alpha1QueryAnrRateMetricSetResponseHttpRequest | None: ...

        @typing.type_check_only
        class CrashrateResource(googleapiclient.discovery.Resource):
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GooglePlayDeveloperReportingV1alpha1CrashRateMetricSetHttpRequest: ...
            def query(
                self,
                *,
                name: str,
                body: GooglePlayDeveloperReportingV1alpha1QueryCrashRateMetricSetRequest = ...,
                **kwargs: typing.Any
            ) -> GooglePlayDeveloperReportingV1alpha1QueryCrashRateMetricSetResponseHttpRequest: ...
            def query_next(
                self,
                previous_request: GooglePlayDeveloperReportingV1alpha1QueryCrashRateMetricSetResponseHttpRequest,
                previous_response: GooglePlayDeveloperReportingV1alpha1QueryCrashRateMetricSetResponse,
            ) -> GooglePlayDeveloperReportingV1alpha1QueryCrashRateMetricSetResponseHttpRequest | None: ...

        @typing.type_check_only
        class ErrorsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class CountsResource(googleapiclient.discovery.Resource):
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GooglePlayDeveloperReportingV1alpha1ErrorCountMetricSetHttpRequest: ...
                def query(
                    self,
                    *,
                    name: str,
                    body: GooglePlayDeveloperReportingV1alpha1QueryErrorCountMetricSetRequest = ...,
                    **kwargs: typing.Any
                ) -> GooglePlayDeveloperReportingV1alpha1QueryErrorCountMetricSetResponseHttpRequest: ...
                def query_next(
                    self,
                    previous_request: GooglePlayDeveloperReportingV1alpha1QueryErrorCountMetricSetResponseHttpRequest,
                    previous_response: GooglePlayDeveloperReportingV1alpha1QueryErrorCountMetricSetResponse,
                ) -> GooglePlayDeveloperReportingV1alpha1QueryErrorCountMetricSetResponseHttpRequest | None: ...

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
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> GooglePlayDeveloperReportingV1alpha1SearchErrorIssuesResponseHttpRequest: ...
                def search_next(
                    self,
                    previous_request: GooglePlayDeveloperReportingV1alpha1SearchErrorIssuesResponseHttpRequest,
                    previous_response: GooglePlayDeveloperReportingV1alpha1SearchErrorIssuesResponse,
                ) -> GooglePlayDeveloperReportingV1alpha1SearchErrorIssuesResponseHttpRequest | None: ...

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
                    **kwargs: typing.Any
                ) -> GooglePlayDeveloperReportingV1alpha1SearchErrorReportsResponseHttpRequest: ...
                def search_next(
                    self,
                    previous_request: GooglePlayDeveloperReportingV1alpha1SearchErrorReportsResponseHttpRequest,
                    previous_response: GooglePlayDeveloperReportingV1alpha1SearchErrorReportsResponse,
                ) -> GooglePlayDeveloperReportingV1alpha1SearchErrorReportsResponseHttpRequest | None: ...

            def counts(self) -> CountsResource: ...
            def issues(self) -> IssuesResource: ...
            def reports(self) -> ReportsResource: ...

        @typing.type_check_only
        class ExcessivewakeuprateResource(googleapiclient.discovery.Resource):
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GooglePlayDeveloperReportingV1alpha1ExcessiveWakeupRateMetricSetHttpRequest: ...
            def query(
                self,
                *,
                name: str,
                body: GooglePlayDeveloperReportingV1alpha1QueryExcessiveWakeupRateMetricSetRequest = ...,
                **kwargs: typing.Any
            ) -> GooglePlayDeveloperReportingV1alpha1QueryExcessiveWakeupRateMetricSetResponseHttpRequest: ...
            def query_next(
                self,
                previous_request: GooglePlayDeveloperReportingV1alpha1QueryExcessiveWakeupRateMetricSetResponseHttpRequest,
                previous_response: GooglePlayDeveloperReportingV1alpha1QueryExcessiveWakeupRateMetricSetResponse,
            ) -> GooglePlayDeveloperReportingV1alpha1QueryExcessiveWakeupRateMetricSetResponseHttpRequest | None: ...

        @typing.type_check_only
        class StuckbackgroundwakelockrateResource(googleapiclient.discovery.Resource):
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GooglePlayDeveloperReportingV1alpha1StuckBackgroundWakelockRateMetricSetHttpRequest: ...
            def query(
                self,
                *,
                name: str,
                body: GooglePlayDeveloperReportingV1alpha1QueryStuckBackgroundWakelockRateMetricSetRequest = ...,
                **kwargs: typing.Any
            ) -> GooglePlayDeveloperReportingV1alpha1QueryStuckBackgroundWakelockRateMetricSetResponseHttpRequest: ...
            def query_next(
                self,
                previous_request: GooglePlayDeveloperReportingV1alpha1QueryStuckBackgroundWakelockRateMetricSetResponseHttpRequest,
                previous_response: GooglePlayDeveloperReportingV1alpha1QueryStuckBackgroundWakelockRateMetricSetResponse,
            ) -> GooglePlayDeveloperReportingV1alpha1QueryStuckBackgroundWakelockRateMetricSetResponseHttpRequest | None: ...

        def anrrate(self) -> AnrrateResource: ...
        def crashrate(self) -> CrashrateResource: ...
        def errors(self) -> ErrorsResource: ...
        def excessivewakeuprate(self) -> ExcessivewakeuprateResource: ...
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
        | None = ...,
    ) -> googleapiclient.http.BatchHttpRequest: ...
    def anomalies(self) -> AnomaliesResource: ...
    def vitals(self) -> VitalsResource: ...

@typing.type_check_only
class GooglePlayDeveloperReportingV1alpha1AnrRateMetricSetHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GooglePlayDeveloperReportingV1alpha1AnrRateMetricSet: ...

@typing.type_check_only
class GooglePlayDeveloperReportingV1alpha1CrashRateMetricSetHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GooglePlayDeveloperReportingV1alpha1CrashRateMetricSet: ...

@typing.type_check_only
class GooglePlayDeveloperReportingV1alpha1ErrorCountMetricSetHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GooglePlayDeveloperReportingV1alpha1ErrorCountMetricSet: ...

@typing.type_check_only
class GooglePlayDeveloperReportingV1alpha1ExcessiveWakeupRateMetricSetHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GooglePlayDeveloperReportingV1alpha1ExcessiveWakeupRateMetricSet: ...

@typing.type_check_only
class GooglePlayDeveloperReportingV1alpha1ListAnomaliesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GooglePlayDeveloperReportingV1alpha1ListAnomaliesResponse: ...

@typing.type_check_only
class GooglePlayDeveloperReportingV1alpha1QueryAnrRateMetricSetResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GooglePlayDeveloperReportingV1alpha1QueryAnrRateMetricSetResponse: ...

@typing.type_check_only
class GooglePlayDeveloperReportingV1alpha1QueryCrashRateMetricSetResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GooglePlayDeveloperReportingV1alpha1QueryCrashRateMetricSetResponse: ...

@typing.type_check_only
class GooglePlayDeveloperReportingV1alpha1QueryErrorCountMetricSetResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GooglePlayDeveloperReportingV1alpha1QueryErrorCountMetricSetResponse: ...

@typing.type_check_only
class GooglePlayDeveloperReportingV1alpha1QueryExcessiveWakeupRateMetricSetResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GooglePlayDeveloperReportingV1alpha1QueryExcessiveWakeupRateMetricSetResponse: ...

@typing.type_check_only
class GooglePlayDeveloperReportingV1alpha1QueryStuckBackgroundWakelockRateMetricSetResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GooglePlayDeveloperReportingV1alpha1QueryStuckBackgroundWakelockRateMetricSetResponse: ...

@typing.type_check_only
class GooglePlayDeveloperReportingV1alpha1SearchErrorIssuesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GooglePlayDeveloperReportingV1alpha1SearchErrorIssuesResponse: ...

@typing.type_check_only
class GooglePlayDeveloperReportingV1alpha1SearchErrorReportsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GooglePlayDeveloperReportingV1alpha1SearchErrorReportsResponse: ...

@typing.type_check_only
class GooglePlayDeveloperReportingV1alpha1StuckBackgroundWakelockRateMetricSetHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GooglePlayDeveloperReportingV1alpha1StuckBackgroundWakelockRateMetricSet: ...
