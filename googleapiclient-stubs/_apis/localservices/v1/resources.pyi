import collections.abc
import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

_list = list

@typing.type_check_only
class LocalservicesResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class AccountReportsResource(googleapiclient.discovery.Resource):
        def search(
            self,
            *,
            endDate_day: int = ...,
            endDate_month: int = ...,
            endDate_year: int = ...,
            pageSize: int = ...,
            pageToken: str = ...,
            query: str = ...,
            startDate_day: int = ...,
            startDate_month: int = ...,
            startDate_year: int = ...,
            **kwargs: typing.Any
        ) -> GoogleAdsHomeservicesLocalservicesV1SearchAccountReportsResponseHttpRequest: ...
        def search_next(
            self,
            previous_request: GoogleAdsHomeservicesLocalservicesV1SearchAccountReportsResponseHttpRequest,
            previous_response: GoogleAdsHomeservicesLocalservicesV1SearchAccountReportsResponse,
        ) -> GoogleAdsHomeservicesLocalservicesV1SearchAccountReportsResponseHttpRequest | None: ...

    @typing.type_check_only
    class DetailedLeadReportsResource(googleapiclient.discovery.Resource):
        def search(
            self,
            *,
            endDate_day: int = ...,
            endDate_month: int = ...,
            endDate_year: int = ...,
            pageSize: int = ...,
            pageToken: str = ...,
            query: str = ...,
            startDate_day: int = ...,
            startDate_month: int = ...,
            startDate_year: int = ...,
            **kwargs: typing.Any
        ) -> GoogleAdsHomeservicesLocalservicesV1SearchDetailedLeadReportsResponseHttpRequest: ...
        def search_next(
            self,
            previous_request: GoogleAdsHomeservicesLocalservicesV1SearchDetailedLeadReportsResponseHttpRequest,
            previous_response: GoogleAdsHomeservicesLocalservicesV1SearchDetailedLeadReportsResponse,
        ) -> GoogleAdsHomeservicesLocalservicesV1SearchDetailedLeadReportsResponseHttpRequest | None: ...

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
    def accountReports(self) -> AccountReportsResource: ...
    def detailedLeadReports(self) -> DetailedLeadReportsResource: ...

@typing.type_check_only
class GoogleAdsHomeservicesLocalservicesV1SearchAccountReportsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleAdsHomeservicesLocalservicesV1SearchAccountReportsResponse: ...

@typing.type_check_only
class GoogleAdsHomeservicesLocalservicesV1SearchDetailedLeadReportsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleAdsHomeservicesLocalservicesV1SearchDetailedLeadReportsResponse: ...
