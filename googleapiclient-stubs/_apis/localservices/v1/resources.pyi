import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *
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
    def accountReports(self) -> AccountReportsResource: ...
    def detailedLeadReports(self) -> DetailedLeadReportsResource: ...

@typing.type_check_only
class GoogleAdsHomeservicesLocalservicesV1SearchAccountReportsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleAdsHomeservicesLocalservicesV1SearchAccountReportsResponse: ...

@typing.type_check_only
class GoogleAdsHomeservicesLocalservicesV1SearchDetailedLeadReportsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleAdsHomeservicesLocalservicesV1SearchDetailedLeadReportsResponse: ...
