import collections.abc
import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

_list = list

@typing.type_check_only
class AdsenseResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class AccountsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class AdclientsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class AdunitsResource(googleapiclient.discovery.Resource):
                def create(
                    self, *, parent: str, body: AdUnit = ..., **kwargs: typing.Any
                ) -> AdUnitHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> AdUnitHttpRequest: ...
                def getAdcode(
                    self, *, name: str, **kwargs: typing.Any
                ) -> AdUnitAdCodeHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> ListAdUnitsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListAdUnitsResponseHttpRequest,
                    previous_response: ListAdUnitsResponse,
                ) -> ListAdUnitsResponseHttpRequest | None: ...
                def listLinkedCustomChannels(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> ListLinkedCustomChannelsResponseHttpRequest: ...
                def listLinkedCustomChannels_next(
                    self,
                    previous_request: ListLinkedCustomChannelsResponseHttpRequest,
                    previous_response: ListLinkedCustomChannelsResponse,
                ) -> ListLinkedCustomChannelsResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: AdUnit = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any
                ) -> AdUnitHttpRequest: ...

            @typing.type_check_only
            class CustomchannelsResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: CustomChannel = ...,
                    **kwargs: typing.Any
                ) -> CustomChannelHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> CustomChannelHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> ListCustomChannelsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListCustomChannelsResponseHttpRequest,
                    previous_response: ListCustomChannelsResponse,
                ) -> ListCustomChannelsResponseHttpRequest | None: ...
                def listLinkedAdUnits(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> ListLinkedAdUnitsResponseHttpRequest: ...
                def listLinkedAdUnits_next(
                    self,
                    previous_request: ListLinkedAdUnitsResponseHttpRequest,
                    previous_response: ListLinkedAdUnitsResponse,
                ) -> ListLinkedAdUnitsResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: CustomChannel = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any
                ) -> CustomChannelHttpRequest: ...

            @typing.type_check_only
            class UrlchannelsResource(googleapiclient.discovery.Resource):
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> UrlChannelHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> ListUrlChannelsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListUrlChannelsResponseHttpRequest,
                    previous_response: ListUrlChannelsResponse,
                ) -> ListUrlChannelsResponseHttpRequest | None: ...

            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> AdClientHttpRequest: ...
            def getAdcode(
                self, *, name: str, **kwargs: typing.Any
            ) -> AdClientAdCodeHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> ListAdClientsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListAdClientsResponseHttpRequest,
                previous_response: ListAdClientsResponse,
            ) -> ListAdClientsResponseHttpRequest | None: ...
            def adunits(self) -> AdunitsResource: ...
            def customchannels(self) -> CustomchannelsResource: ...
            def urlchannels(self) -> UrlchannelsResource: ...

        @typing.type_check_only
        class AlertsResource(googleapiclient.discovery.Resource):
            def list(
                self, *, parent: str, languageCode: str = ..., **kwargs: typing.Any
            ) -> ListAlertsResponseHttpRequest: ...

        @typing.type_check_only
        class PaymentsResource(googleapiclient.discovery.Resource):
            def list(
                self, *, parent: str, **kwargs: typing.Any
            ) -> ListPaymentsResponseHttpRequest: ...

        @typing.type_check_only
        class ReportsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class SavedResource(googleapiclient.discovery.Resource):
                def generate(
                    self,
                    *,
                    name: str,
                    currencyCode: str = ...,
                    dateRange: typing_extensions.Literal[
                        "REPORTING_DATE_RANGE_UNSPECIFIED",
                        "CUSTOM",
                        "TODAY",
                        "YESTERDAY",
                        "MONTH_TO_DATE",
                        "YEAR_TO_DATE",
                        "LAST_7_DAYS",
                        "LAST_30_DAYS",
                    ] = ...,
                    endDate_day: int = ...,
                    endDate_month: int = ...,
                    endDate_year: int = ...,
                    languageCode: str = ...,
                    reportingTimeZone: typing_extensions.Literal[
                        "REPORTING_TIME_ZONE_UNSPECIFIED",
                        "ACCOUNT_TIME_ZONE",
                        "GOOGLE_TIME_ZONE",
                    ] = ...,
                    startDate_day: int = ...,
                    startDate_month: int = ...,
                    startDate_year: int = ...,
                    **kwargs: typing.Any
                ) -> ReportResultHttpRequest: ...
                def generateCsv(
                    self,
                    *,
                    name: str,
                    currencyCode: str = ...,
                    dateRange: typing_extensions.Literal[
                        "REPORTING_DATE_RANGE_UNSPECIFIED",
                        "CUSTOM",
                        "TODAY",
                        "YESTERDAY",
                        "MONTH_TO_DATE",
                        "YEAR_TO_DATE",
                        "LAST_7_DAYS",
                        "LAST_30_DAYS",
                    ] = ...,
                    endDate_day: int = ...,
                    endDate_month: int = ...,
                    endDate_year: int = ...,
                    languageCode: str = ...,
                    reportingTimeZone: typing_extensions.Literal[
                        "REPORTING_TIME_ZONE_UNSPECIFIED",
                        "ACCOUNT_TIME_ZONE",
                        "GOOGLE_TIME_ZONE",
                    ] = ...,
                    startDate_day: int = ...,
                    startDate_month: int = ...,
                    startDate_year: int = ...,
                    **kwargs: typing.Any
                ) -> HttpBodyHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> ListSavedReportsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListSavedReportsResponseHttpRequest,
                    previous_response: ListSavedReportsResponse,
                ) -> ListSavedReportsResponseHttpRequest | None: ...

            def generate(
                self,
                *,
                account: str,
                currencyCode: str = ...,
                dateRange: typing_extensions.Literal[
                    "REPORTING_DATE_RANGE_UNSPECIFIED",
                    "CUSTOM",
                    "TODAY",
                    "YESTERDAY",
                    "MONTH_TO_DATE",
                    "YEAR_TO_DATE",
                    "LAST_7_DAYS",
                    "LAST_30_DAYS",
                ] = ...,
                dimensions: typing_extensions.Literal[
                    "DIMENSION_UNSPECIFIED",
                    "DATE",
                    "WEEK",
                    "MONTH",
                    "ACCOUNT_NAME",
                    "AD_CLIENT_ID",
                    "HOSTED_AD_CLIENT_ID",
                    "PRODUCT_NAME",
                    "PRODUCT_CODE",
                    "AD_UNIT_NAME",
                    "AD_UNIT_ID",
                    "AD_UNIT_SIZE_NAME",
                    "AD_UNIT_SIZE_CODE",
                    "CUSTOM_CHANNEL_NAME",
                    "CUSTOM_CHANNEL_ID",
                    "OWNED_SITE_DOMAIN_NAME",
                    "OWNED_SITE_ID",
                    "URL_CHANNEL_NAME",
                    "URL_CHANNEL_ID",
                    "BUYER_NETWORK_NAME",
                    "BUYER_NETWORK_ID",
                    "BID_TYPE_NAME",
                    "BID_TYPE_CODE",
                    "CREATIVE_SIZE_NAME",
                    "CREATIVE_SIZE_CODE",
                    "DOMAIN_NAME",
                    "DOMAIN_CODE",
                    "COUNTRY_NAME",
                    "COUNTRY_CODE",
                    "PLATFORM_TYPE_NAME",
                    "PLATFORM_TYPE_CODE",
                    "TARGETING_TYPE_NAME",
                    "TARGETING_TYPE_CODE",
                    "CONTENT_PLATFORM_NAME",
                    "CONTENT_PLATFORM_CODE",
                    "AD_PLACEMENT_NAME",
                    "AD_PLACEMENT_CODE",
                    "REQUESTED_AD_TYPE_NAME",
                    "REQUESTED_AD_TYPE_CODE",
                    "SERVED_AD_TYPE_NAME",
                    "SERVED_AD_TYPE_CODE",
                    "AD_FORMAT_NAME",
                    "AD_FORMAT_CODE",
                    "CUSTOM_SEARCH_STYLE_NAME",
                    "CUSTOM_SEARCH_STYLE_ID",
                    "DOMAIN_REGISTRANT",
                    "WEBSEARCH_QUERY_STRING",
                ]
                | _list[
                    typing_extensions.Literal[
                        "DIMENSION_UNSPECIFIED",
                        "DATE",
                        "WEEK",
                        "MONTH",
                        "ACCOUNT_NAME",
                        "AD_CLIENT_ID",
                        "HOSTED_AD_CLIENT_ID",
                        "PRODUCT_NAME",
                        "PRODUCT_CODE",
                        "AD_UNIT_NAME",
                        "AD_UNIT_ID",
                        "AD_UNIT_SIZE_NAME",
                        "AD_UNIT_SIZE_CODE",
                        "CUSTOM_CHANNEL_NAME",
                        "CUSTOM_CHANNEL_ID",
                        "OWNED_SITE_DOMAIN_NAME",
                        "OWNED_SITE_ID",
                        "URL_CHANNEL_NAME",
                        "URL_CHANNEL_ID",
                        "BUYER_NETWORK_NAME",
                        "BUYER_NETWORK_ID",
                        "BID_TYPE_NAME",
                        "BID_TYPE_CODE",
                        "CREATIVE_SIZE_NAME",
                        "CREATIVE_SIZE_CODE",
                        "DOMAIN_NAME",
                        "DOMAIN_CODE",
                        "COUNTRY_NAME",
                        "COUNTRY_CODE",
                        "PLATFORM_TYPE_NAME",
                        "PLATFORM_TYPE_CODE",
                        "TARGETING_TYPE_NAME",
                        "TARGETING_TYPE_CODE",
                        "CONTENT_PLATFORM_NAME",
                        "CONTENT_PLATFORM_CODE",
                        "AD_PLACEMENT_NAME",
                        "AD_PLACEMENT_CODE",
                        "REQUESTED_AD_TYPE_NAME",
                        "REQUESTED_AD_TYPE_CODE",
                        "SERVED_AD_TYPE_NAME",
                        "SERVED_AD_TYPE_CODE",
                        "AD_FORMAT_NAME",
                        "AD_FORMAT_CODE",
                        "CUSTOM_SEARCH_STYLE_NAME",
                        "CUSTOM_SEARCH_STYLE_ID",
                        "DOMAIN_REGISTRANT",
                        "WEBSEARCH_QUERY_STRING",
                    ]
                ] = ...,
                endDate_day: int = ...,
                endDate_month: int = ...,
                endDate_year: int = ...,
                filters: str | _list[str] = ...,
                languageCode: str = ...,
                limit: int = ...,
                metrics: typing_extensions.Literal[
                    "METRIC_UNSPECIFIED",
                    "PAGE_VIEWS",
                    "AD_REQUESTS",
                    "MATCHED_AD_REQUESTS",
                    "TOTAL_IMPRESSIONS",
                    "IMPRESSIONS",
                    "INDIVIDUAL_AD_IMPRESSIONS",
                    "CLICKS",
                    "PAGE_VIEWS_SPAM_RATIO",
                    "AD_REQUESTS_SPAM_RATIO",
                    "MATCHED_AD_REQUESTS_SPAM_RATIO",
                    "IMPRESSIONS_SPAM_RATIO",
                    "INDIVIDUAL_AD_IMPRESSIONS_SPAM_RATIO",
                    "CLICKS_SPAM_RATIO",
                    "AD_REQUESTS_COVERAGE",
                    "PAGE_VIEWS_CTR",
                    "AD_REQUESTS_CTR",
                    "MATCHED_AD_REQUESTS_CTR",
                    "IMPRESSIONS_CTR",
                    "INDIVIDUAL_AD_IMPRESSIONS_CTR",
                    "ACTIVE_VIEW_MEASURABILITY",
                    "ACTIVE_VIEW_VIEWABILITY",
                    "ACTIVE_VIEW_TIME",
                    "ESTIMATED_EARNINGS",
                    "PAGE_VIEWS_RPM",
                    "AD_REQUESTS_RPM",
                    "MATCHED_AD_REQUESTS_RPM",
                    "IMPRESSIONS_RPM",
                    "INDIVIDUAL_AD_IMPRESSIONS_RPM",
                    "COST_PER_CLICK",
                    "ADS_PER_IMPRESSION",
                    "TOTAL_EARNINGS",
                    "WEBSEARCH_RESULT_PAGES",
                ]
                | _list[
                    typing_extensions.Literal[
                        "METRIC_UNSPECIFIED",
                        "PAGE_VIEWS",
                        "AD_REQUESTS",
                        "MATCHED_AD_REQUESTS",
                        "TOTAL_IMPRESSIONS",
                        "IMPRESSIONS",
                        "INDIVIDUAL_AD_IMPRESSIONS",
                        "CLICKS",
                        "PAGE_VIEWS_SPAM_RATIO",
                        "AD_REQUESTS_SPAM_RATIO",
                        "MATCHED_AD_REQUESTS_SPAM_RATIO",
                        "IMPRESSIONS_SPAM_RATIO",
                        "INDIVIDUAL_AD_IMPRESSIONS_SPAM_RATIO",
                        "CLICKS_SPAM_RATIO",
                        "AD_REQUESTS_COVERAGE",
                        "PAGE_VIEWS_CTR",
                        "AD_REQUESTS_CTR",
                        "MATCHED_AD_REQUESTS_CTR",
                        "IMPRESSIONS_CTR",
                        "INDIVIDUAL_AD_IMPRESSIONS_CTR",
                        "ACTIVE_VIEW_MEASURABILITY",
                        "ACTIVE_VIEW_VIEWABILITY",
                        "ACTIVE_VIEW_TIME",
                        "ESTIMATED_EARNINGS",
                        "PAGE_VIEWS_RPM",
                        "AD_REQUESTS_RPM",
                        "MATCHED_AD_REQUESTS_RPM",
                        "IMPRESSIONS_RPM",
                        "INDIVIDUAL_AD_IMPRESSIONS_RPM",
                        "COST_PER_CLICK",
                        "ADS_PER_IMPRESSION",
                        "TOTAL_EARNINGS",
                        "WEBSEARCH_RESULT_PAGES",
                    ]
                ] = ...,
                orderBy: str | _list[str] = ...,
                reportingTimeZone: typing_extensions.Literal[
                    "REPORTING_TIME_ZONE_UNSPECIFIED",
                    "ACCOUNT_TIME_ZONE",
                    "GOOGLE_TIME_ZONE",
                ] = ...,
                startDate_day: int = ...,
                startDate_month: int = ...,
                startDate_year: int = ...,
                **kwargs: typing.Any
            ) -> ReportResultHttpRequest: ...
            def generateCsv(
                self,
                *,
                account: str,
                currencyCode: str = ...,
                dateRange: typing_extensions.Literal[
                    "REPORTING_DATE_RANGE_UNSPECIFIED",
                    "CUSTOM",
                    "TODAY",
                    "YESTERDAY",
                    "MONTH_TO_DATE",
                    "YEAR_TO_DATE",
                    "LAST_7_DAYS",
                    "LAST_30_DAYS",
                ] = ...,
                dimensions: typing_extensions.Literal[
                    "DIMENSION_UNSPECIFIED",
                    "DATE",
                    "WEEK",
                    "MONTH",
                    "ACCOUNT_NAME",
                    "AD_CLIENT_ID",
                    "HOSTED_AD_CLIENT_ID",
                    "PRODUCT_NAME",
                    "PRODUCT_CODE",
                    "AD_UNIT_NAME",
                    "AD_UNIT_ID",
                    "AD_UNIT_SIZE_NAME",
                    "AD_UNIT_SIZE_CODE",
                    "CUSTOM_CHANNEL_NAME",
                    "CUSTOM_CHANNEL_ID",
                    "OWNED_SITE_DOMAIN_NAME",
                    "OWNED_SITE_ID",
                    "URL_CHANNEL_NAME",
                    "URL_CHANNEL_ID",
                    "BUYER_NETWORK_NAME",
                    "BUYER_NETWORK_ID",
                    "BID_TYPE_NAME",
                    "BID_TYPE_CODE",
                    "CREATIVE_SIZE_NAME",
                    "CREATIVE_SIZE_CODE",
                    "DOMAIN_NAME",
                    "DOMAIN_CODE",
                    "COUNTRY_NAME",
                    "COUNTRY_CODE",
                    "PLATFORM_TYPE_NAME",
                    "PLATFORM_TYPE_CODE",
                    "TARGETING_TYPE_NAME",
                    "TARGETING_TYPE_CODE",
                    "CONTENT_PLATFORM_NAME",
                    "CONTENT_PLATFORM_CODE",
                    "AD_PLACEMENT_NAME",
                    "AD_PLACEMENT_CODE",
                    "REQUESTED_AD_TYPE_NAME",
                    "REQUESTED_AD_TYPE_CODE",
                    "SERVED_AD_TYPE_NAME",
                    "SERVED_AD_TYPE_CODE",
                    "AD_FORMAT_NAME",
                    "AD_FORMAT_CODE",
                    "CUSTOM_SEARCH_STYLE_NAME",
                    "CUSTOM_SEARCH_STYLE_ID",
                    "DOMAIN_REGISTRANT",
                    "WEBSEARCH_QUERY_STRING",
                ]
                | _list[
                    typing_extensions.Literal[
                        "DIMENSION_UNSPECIFIED",
                        "DATE",
                        "WEEK",
                        "MONTH",
                        "ACCOUNT_NAME",
                        "AD_CLIENT_ID",
                        "HOSTED_AD_CLIENT_ID",
                        "PRODUCT_NAME",
                        "PRODUCT_CODE",
                        "AD_UNIT_NAME",
                        "AD_UNIT_ID",
                        "AD_UNIT_SIZE_NAME",
                        "AD_UNIT_SIZE_CODE",
                        "CUSTOM_CHANNEL_NAME",
                        "CUSTOM_CHANNEL_ID",
                        "OWNED_SITE_DOMAIN_NAME",
                        "OWNED_SITE_ID",
                        "URL_CHANNEL_NAME",
                        "URL_CHANNEL_ID",
                        "BUYER_NETWORK_NAME",
                        "BUYER_NETWORK_ID",
                        "BID_TYPE_NAME",
                        "BID_TYPE_CODE",
                        "CREATIVE_SIZE_NAME",
                        "CREATIVE_SIZE_CODE",
                        "DOMAIN_NAME",
                        "DOMAIN_CODE",
                        "COUNTRY_NAME",
                        "COUNTRY_CODE",
                        "PLATFORM_TYPE_NAME",
                        "PLATFORM_TYPE_CODE",
                        "TARGETING_TYPE_NAME",
                        "TARGETING_TYPE_CODE",
                        "CONTENT_PLATFORM_NAME",
                        "CONTENT_PLATFORM_CODE",
                        "AD_PLACEMENT_NAME",
                        "AD_PLACEMENT_CODE",
                        "REQUESTED_AD_TYPE_NAME",
                        "REQUESTED_AD_TYPE_CODE",
                        "SERVED_AD_TYPE_NAME",
                        "SERVED_AD_TYPE_CODE",
                        "AD_FORMAT_NAME",
                        "AD_FORMAT_CODE",
                        "CUSTOM_SEARCH_STYLE_NAME",
                        "CUSTOM_SEARCH_STYLE_ID",
                        "DOMAIN_REGISTRANT",
                        "WEBSEARCH_QUERY_STRING",
                    ]
                ] = ...,
                endDate_day: int = ...,
                endDate_month: int = ...,
                endDate_year: int = ...,
                filters: str | _list[str] = ...,
                languageCode: str = ...,
                limit: int = ...,
                metrics: typing_extensions.Literal[
                    "METRIC_UNSPECIFIED",
                    "PAGE_VIEWS",
                    "AD_REQUESTS",
                    "MATCHED_AD_REQUESTS",
                    "TOTAL_IMPRESSIONS",
                    "IMPRESSIONS",
                    "INDIVIDUAL_AD_IMPRESSIONS",
                    "CLICKS",
                    "PAGE_VIEWS_SPAM_RATIO",
                    "AD_REQUESTS_SPAM_RATIO",
                    "MATCHED_AD_REQUESTS_SPAM_RATIO",
                    "IMPRESSIONS_SPAM_RATIO",
                    "INDIVIDUAL_AD_IMPRESSIONS_SPAM_RATIO",
                    "CLICKS_SPAM_RATIO",
                    "AD_REQUESTS_COVERAGE",
                    "PAGE_VIEWS_CTR",
                    "AD_REQUESTS_CTR",
                    "MATCHED_AD_REQUESTS_CTR",
                    "IMPRESSIONS_CTR",
                    "INDIVIDUAL_AD_IMPRESSIONS_CTR",
                    "ACTIVE_VIEW_MEASURABILITY",
                    "ACTIVE_VIEW_VIEWABILITY",
                    "ACTIVE_VIEW_TIME",
                    "ESTIMATED_EARNINGS",
                    "PAGE_VIEWS_RPM",
                    "AD_REQUESTS_RPM",
                    "MATCHED_AD_REQUESTS_RPM",
                    "IMPRESSIONS_RPM",
                    "INDIVIDUAL_AD_IMPRESSIONS_RPM",
                    "COST_PER_CLICK",
                    "ADS_PER_IMPRESSION",
                    "TOTAL_EARNINGS",
                    "WEBSEARCH_RESULT_PAGES",
                ]
                | _list[
                    typing_extensions.Literal[
                        "METRIC_UNSPECIFIED",
                        "PAGE_VIEWS",
                        "AD_REQUESTS",
                        "MATCHED_AD_REQUESTS",
                        "TOTAL_IMPRESSIONS",
                        "IMPRESSIONS",
                        "INDIVIDUAL_AD_IMPRESSIONS",
                        "CLICKS",
                        "PAGE_VIEWS_SPAM_RATIO",
                        "AD_REQUESTS_SPAM_RATIO",
                        "MATCHED_AD_REQUESTS_SPAM_RATIO",
                        "IMPRESSIONS_SPAM_RATIO",
                        "INDIVIDUAL_AD_IMPRESSIONS_SPAM_RATIO",
                        "CLICKS_SPAM_RATIO",
                        "AD_REQUESTS_COVERAGE",
                        "PAGE_VIEWS_CTR",
                        "AD_REQUESTS_CTR",
                        "MATCHED_AD_REQUESTS_CTR",
                        "IMPRESSIONS_CTR",
                        "INDIVIDUAL_AD_IMPRESSIONS_CTR",
                        "ACTIVE_VIEW_MEASURABILITY",
                        "ACTIVE_VIEW_VIEWABILITY",
                        "ACTIVE_VIEW_TIME",
                        "ESTIMATED_EARNINGS",
                        "PAGE_VIEWS_RPM",
                        "AD_REQUESTS_RPM",
                        "MATCHED_AD_REQUESTS_RPM",
                        "IMPRESSIONS_RPM",
                        "INDIVIDUAL_AD_IMPRESSIONS_RPM",
                        "COST_PER_CLICK",
                        "ADS_PER_IMPRESSION",
                        "TOTAL_EARNINGS",
                        "WEBSEARCH_RESULT_PAGES",
                    ]
                ] = ...,
                orderBy: str | _list[str] = ...,
                reportingTimeZone: typing_extensions.Literal[
                    "REPORTING_TIME_ZONE_UNSPECIFIED",
                    "ACCOUNT_TIME_ZONE",
                    "GOOGLE_TIME_ZONE",
                ] = ...,
                startDate_day: int = ...,
                startDate_month: int = ...,
                startDate_year: int = ...,
                **kwargs: typing.Any
            ) -> HttpBodyHttpRequest: ...
            def getSaved(
                self, *, name: str, **kwargs: typing.Any
            ) -> SavedReportHttpRequest: ...
            def saved(self) -> SavedResource: ...

        @typing.type_check_only
        class SitesResource(googleapiclient.discovery.Resource):
            def get(self, *, name: str, **kwargs: typing.Any) -> SiteHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> ListSitesResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListSitesResponseHttpRequest,
                previous_response: ListSitesResponse,
            ) -> ListSitesResponseHttpRequest | None: ...

        def get(self, *, name: str, **kwargs: typing.Any) -> AccountHttpRequest: ...
        def getAdBlockingRecoveryTag(
            self, *, name: str, **kwargs: typing.Any
        ) -> AdBlockingRecoveryTagHttpRequest: ...
        def list(
            self, *, pageSize: int = ..., pageToken: str = ..., **kwargs: typing.Any
        ) -> ListAccountsResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: ListAccountsResponseHttpRequest,
            previous_response: ListAccountsResponse,
        ) -> ListAccountsResponseHttpRequest | None: ...
        def listChildAccounts(
            self,
            *,
            parent: str,
            pageSize: int = ...,
            pageToken: str = ...,
            **kwargs: typing.Any
        ) -> ListChildAccountsResponseHttpRequest: ...
        def listChildAccounts_next(
            self,
            previous_request: ListChildAccountsResponseHttpRequest,
            previous_response: ListChildAccountsResponse,
        ) -> ListChildAccountsResponseHttpRequest | None: ...
        def adclients(self) -> AdclientsResource: ...
        def alerts(self) -> AlertsResource: ...
        def payments(self) -> PaymentsResource: ...
        def reports(self) -> ReportsResource: ...
        def sites(self) -> SitesResource: ...

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
    def accounts(self) -> AccountsResource: ...

@typing.type_check_only
class AccountHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Account: ...

@typing.type_check_only
class AdBlockingRecoveryTagHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> AdBlockingRecoveryTag: ...

@typing.type_check_only
class AdClientHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> AdClient: ...

@typing.type_check_only
class AdClientAdCodeHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> AdClientAdCode: ...

@typing.type_check_only
class AdUnitHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> AdUnit: ...

@typing.type_check_only
class AdUnitAdCodeHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> AdUnitAdCode: ...

@typing.type_check_only
class CustomChannelHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> CustomChannel: ...

@typing.type_check_only
class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Empty: ...

@typing.type_check_only
class HttpBodyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> HttpBody: ...

@typing.type_check_only
class ListAccountsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListAccountsResponse: ...

@typing.type_check_only
class ListAdClientsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListAdClientsResponse: ...

@typing.type_check_only
class ListAdUnitsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListAdUnitsResponse: ...

@typing.type_check_only
class ListAlertsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListAlertsResponse: ...

@typing.type_check_only
class ListChildAccountsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListChildAccountsResponse: ...

@typing.type_check_only
class ListCustomChannelsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListCustomChannelsResponse: ...

@typing.type_check_only
class ListLinkedAdUnitsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListLinkedAdUnitsResponse: ...

@typing.type_check_only
class ListLinkedCustomChannelsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListLinkedCustomChannelsResponse: ...

@typing.type_check_only
class ListPaymentsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListPaymentsResponse: ...

@typing.type_check_only
class ListSavedReportsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListSavedReportsResponse: ...

@typing.type_check_only
class ListSitesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListSitesResponse: ...

@typing.type_check_only
class ListUrlChannelsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListUrlChannelsResponse: ...

@typing.type_check_only
class ReportResultHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ReportResult: ...

@typing.type_check_only
class SavedReportHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> SavedReport: ...

@typing.type_check_only
class SiteHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Site: ...

@typing.type_check_only
class UrlChannelHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> UrlChannel: ...
