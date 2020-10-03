import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class LocalservicesResource(googleapiclient.discovery.Resource):
    class AccountReportsResource(googleapiclient.discovery.Resource):
        def search(
            self,
            *,
            endDate_year: int = ...,
            pageSize: int = ...,
            query: str = ...,
            startDate_year: int = ...,
            endDate_day: int = ...,
            pageToken: str = ...,
            startDate_day: int = ...,
            endDate_month: int = ...,
            startDate_month: int = ...,
            **kwargs: typing.Any
        ) -> GoogleAdsHomeservicesLocalservicesV1SearchAccountReportsResponseHttpRequest: ...
    class DetailedLeadReportsResource(googleapiclient.discovery.Resource):
        def search(
            self,
            *,
            endDate_year: int = ...,
            startDate_day: int = ...,
            endDate_month: int = ...,
            pageToken: str = ...,
            query: str = ...,
            endDate_day: int = ...,
            startDate_year: int = ...,
            startDate_month: int = ...,
            pageSize: int = ...,
            **kwargs: typing.Any
        ) -> GoogleAdsHomeservicesLocalservicesV1SearchDetailedLeadReportsResponseHttpRequest: ...
    def accountReports(self) -> AccountReportsResource: ...
    def detailedLeadReports(self) -> DetailedLeadReportsResource: ...

class GoogleAdsHomeservicesLocalservicesV1SearchAccountReportsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleAdsHomeservicesLocalservicesV1SearchAccountReportsResponse: ...

class GoogleAdsHomeservicesLocalservicesV1SearchDetailedLeadReportsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleAdsHomeservicesLocalservicesV1SearchDetailedLeadReportsResponse: ...
