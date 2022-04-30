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
        ) -> GooglePlayDeveloperReportingV1beta1ListAnomaliesResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: GooglePlayDeveloperReportingV1beta1ListAnomaliesResponseHttpRequest,
            previous_response: GooglePlayDeveloperReportingV1beta1ListAnomaliesResponse,
        ) -> GooglePlayDeveloperReportingV1beta1ListAnomaliesResponseHttpRequest | None: ...

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
                **kwargs: typing.Any
            ) -> GooglePlayDeveloperReportingV1beta1QueryAnrRateMetricSetResponseHttpRequest: ...
            def query_next(
                self,
                previous_request: GooglePlayDeveloperReportingV1beta1QueryAnrRateMetricSetResponseHttpRequest,
                previous_response: GooglePlayDeveloperReportingV1beta1QueryAnrRateMetricSetResponse,
            ) -> GooglePlayDeveloperReportingV1beta1QueryAnrRateMetricSetResponseHttpRequest | None: ...

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
                **kwargs: typing.Any
            ) -> GooglePlayDeveloperReportingV1beta1QueryCrashRateMetricSetResponseHttpRequest: ...
            def query_next(
                self,
                previous_request: GooglePlayDeveloperReportingV1beta1QueryCrashRateMetricSetResponseHttpRequest,
                previous_response: GooglePlayDeveloperReportingV1beta1QueryCrashRateMetricSetResponse,
            ) -> GooglePlayDeveloperReportingV1beta1QueryCrashRateMetricSetResponseHttpRequest | None: ...

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
                **kwargs: typing.Any
            ) -> GooglePlayDeveloperReportingV1beta1QueryExcessiveWakeupRateMetricSetResponseHttpRequest: ...
            def query_next(
                self,
                previous_request: GooglePlayDeveloperReportingV1beta1QueryExcessiveWakeupRateMetricSetResponseHttpRequest,
                previous_response: GooglePlayDeveloperReportingV1beta1QueryExcessiveWakeupRateMetricSetResponse,
            ) -> GooglePlayDeveloperReportingV1beta1QueryExcessiveWakeupRateMetricSetResponseHttpRequest | None: ...

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
                **kwargs: typing.Any
            ) -> GooglePlayDeveloperReportingV1beta1QueryStuckBackgroundWakelockRateMetricSetResponseHttpRequest: ...
            def query_next(
                self,
                previous_request: GooglePlayDeveloperReportingV1beta1QueryStuckBackgroundWakelockRateMetricSetResponseHttpRequest,
                previous_response: GooglePlayDeveloperReportingV1beta1QueryStuckBackgroundWakelockRateMetricSetResponse,
            ) -> GooglePlayDeveloperReportingV1beta1QueryStuckBackgroundWakelockRateMetricSetResponseHttpRequest | None: ...

        def anrrate(self) -> AnrrateResource: ...
        def crashrate(self) -> CrashrateResource: ...
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
class GooglePlayDeveloperReportingV1beta1AnrRateMetricSetHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GooglePlayDeveloperReportingV1beta1AnrRateMetricSet: ...

@typing.type_check_only
class GooglePlayDeveloperReportingV1beta1CrashRateMetricSetHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GooglePlayDeveloperReportingV1beta1CrashRateMetricSet: ...

@typing.type_check_only
class GooglePlayDeveloperReportingV1beta1ExcessiveWakeupRateMetricSetHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GooglePlayDeveloperReportingV1beta1ExcessiveWakeupRateMetricSet: ...

@typing.type_check_only
class GooglePlayDeveloperReportingV1beta1ListAnomaliesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GooglePlayDeveloperReportingV1beta1ListAnomaliesResponse: ...

@typing.type_check_only
class GooglePlayDeveloperReportingV1beta1QueryAnrRateMetricSetResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GooglePlayDeveloperReportingV1beta1QueryAnrRateMetricSetResponse: ...

@typing.type_check_only
class GooglePlayDeveloperReportingV1beta1QueryCrashRateMetricSetResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GooglePlayDeveloperReportingV1beta1QueryCrashRateMetricSetResponse: ...

@typing.type_check_only
class GooglePlayDeveloperReportingV1beta1QueryExcessiveWakeupRateMetricSetResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GooglePlayDeveloperReportingV1beta1QueryExcessiveWakeupRateMetricSetResponse: ...

@typing.type_check_only
class GooglePlayDeveloperReportingV1beta1QueryStuckBackgroundWakelockRateMetricSetResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GooglePlayDeveloperReportingV1beta1QueryStuckBackgroundWakelockRateMetricSetResponse: ...

@typing.type_check_only
class GooglePlayDeveloperReportingV1beta1StuckBackgroundWakelockRateMetricSetHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GooglePlayDeveloperReportingV1beta1StuckBackgroundWakelockRateMetricSet: ...
