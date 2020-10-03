import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class AdSenseResource(googleapiclient.discovery.Resource):
    class AdunitsResource(googleapiclient.discovery.Resource):
        class CustomchannelsResource(googleapiclient.discovery.Resource):
            def list(
                self,
                *,
                adClientId: str,
                adUnitId: str,
                maxResults: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> CustomChannelsHttpRequest: ...
        def list(
            self,
            *,
            adClientId: str,
            maxResults: int = ...,
            includeInactive: bool = ...,
            pageToken: str = ...,
            **kwargs: typing.Any
        ) -> AdUnitsHttpRequest: ...
        def get(
            self, *, adClientId: str, adUnitId: str, **kwargs: typing.Any
        ) -> AdUnitHttpRequest: ...
        def getAdCode(
            self, *, adClientId: str, adUnitId: str, **kwargs: typing.Any
        ) -> AdCodeHttpRequest: ...
        def customchannels(self) -> CustomchannelsResource: ...
    class AdclientsResource(googleapiclient.discovery.Resource):
        def list(
            self, *, maxResults: int = ..., pageToken: str = ..., **kwargs: typing.Any
        ) -> AdClientsHttpRequest: ...
    class CustomchannelsResource(googleapiclient.discovery.Resource):
        class AdunitsResource(googleapiclient.discovery.Resource):
            def list(
                self,
                *,
                adClientId: str,
                customChannelId: str,
                pageToken: str = ...,
                includeInactive: bool = ...,
                maxResults: int = ...,
                **kwargs: typing.Any
            ) -> AdUnitsHttpRequest: ...
        def get(
            self, *, adClientId: str, customChannelId: str, **kwargs: typing.Any
        ) -> CustomChannelHttpRequest: ...
        def list(
            self,
            *,
            adClientId: str,
            maxResults: int = ...,
            pageToken: str = ...,
            **kwargs: typing.Any
        ) -> CustomChannelsHttpRequest: ...
        def adunits(self) -> AdunitsResource: ...
    class ReportsResource(googleapiclient.discovery.Resource):
        class SavedResource(googleapiclient.discovery.Resource):
            def list(
                self,
                *,
                pageToken: str = ...,
                maxResults: int = ...,
                **kwargs: typing.Any
            ) -> SavedReportsHttpRequest: ...
            def generate(
                self,
                *,
                savedReportId: str,
                startIndex: int = ...,
                maxResults: int = ...,
                locale: str = ...,
                **kwargs: typing.Any
            ) -> AdsenseReportsGenerateResponseHttpRequest: ...
        def generate(
            self,
            *,
            startDate: str,
            endDate: str,
            maxResults: int = ...,
            sort: typing.Union[str, typing.List[str]] = ...,
            accountId: typing.Union[str, typing.List[str]] = ...,
            currency: str = ...,
            locale: str = ...,
            useTimezoneReporting: bool = ...,
            dimension: typing.Union[str, typing.List[str]] = ...,
            filter: typing.Union[str, typing.List[str]] = ...,
            metric: typing.Union[str, typing.List[str]] = ...,
            startIndex: int = ...,
            **kwargs: typing.Any
        ) -> AdsenseReportsGenerateResponseHttpRequest: ...
        def saved(self) -> SavedResource: ...
    class UrlchannelsResource(googleapiclient.discovery.Resource):
        def list(
            self,
            *,
            adClientId: str,
            pageToken: str = ...,
            maxResults: int = ...,
            **kwargs: typing.Any
        ) -> UrlChannelsHttpRequest: ...
    class SavedadstylesResource(googleapiclient.discovery.Resource):
        def list(
            self, *, maxResults: int = ..., pageToken: str = ..., **kwargs: typing.Any
        ) -> SavedAdStylesHttpRequest: ...
        def get(
            self, *, savedAdStyleId: str, **kwargs: typing.Any
        ) -> SavedAdStyleHttpRequest: ...
    class AccountsResource(googleapiclient.discovery.Resource):
        class ReportsResource(googleapiclient.discovery.Resource):
            class SavedResource(googleapiclient.discovery.Resource):
                def list(
                    self,
                    *,
                    accountId: str,
                    pageToken: str = ...,
                    maxResults: int = ...,
                    **kwargs: typing.Any
                ) -> SavedReportsHttpRequest: ...
                def generate(
                    self,
                    *,
                    accountId: str,
                    savedReportId: str,
                    locale: str = ...,
                    startIndex: int = ...,
                    maxResults: int = ...,
                    **kwargs: typing.Any
                ) -> AdsenseReportsGenerateResponseHttpRequest: ...
            def generate(
                self,
                *,
                accountId: str,
                startDate: str,
                endDate: str,
                locale: str = ...,
                filter: typing.Union[str, typing.List[str]] = ...,
                sort: typing.Union[str, typing.List[str]] = ...,
                currency: str = ...,
                useTimezoneReporting: bool = ...,
                metric: typing.Union[str, typing.List[str]] = ...,
                maxResults: int = ...,
                dimension: typing.Union[str, typing.List[str]] = ...,
                startIndex: int = ...,
                **kwargs: typing.Any
            ) -> AdsenseReportsGenerateResponseHttpRequest: ...
            def saved(self) -> SavedResource: ...
        class AdunitsResource(googleapiclient.discovery.Resource):
            class CustomchannelsResource(googleapiclient.discovery.Resource):
                def list(
                    self,
                    *,
                    accountId: str,
                    adClientId: str,
                    adUnitId: str,
                    maxResults: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> CustomChannelsHttpRequest: ...
            def getAdCode(
                self,
                *,
                accountId: str,
                adClientId: str,
                adUnitId: str,
                **kwargs: typing.Any
            ) -> AdCodeHttpRequest: ...
            def list(
                self,
                *,
                accountId: str,
                adClientId: str,
                includeInactive: bool = ...,
                pageToken: str = ...,
                maxResults: int = ...,
                **kwargs: typing.Any
            ) -> AdUnitsHttpRequest: ...
            def get(
                self,
                *,
                accountId: str,
                adClientId: str,
                adUnitId: str,
                **kwargs: typing.Any
            ) -> AdUnitHttpRequest: ...
            def customchannels(self) -> CustomchannelsResource: ...
        class SavedadstylesResource(googleapiclient.discovery.Resource):
            def list(
                self,
                *,
                accountId: str,
                pageToken: str = ...,
                maxResults: int = ...,
                **kwargs: typing.Any
            ) -> SavedAdStylesHttpRequest: ...
            def get(
                self, *, accountId: str, savedAdStyleId: str, **kwargs: typing.Any
            ) -> SavedAdStyleHttpRequest: ...
        class PaymentsResource(googleapiclient.discovery.Resource):
            def list(
                self, *, accountId: str, **kwargs: typing.Any
            ) -> PaymentsHttpRequest: ...
        class AlertsResource(googleapiclient.discovery.Resource):
            def delete(
                self, *, accountId: str, alertId: str, **kwargs: typing.Any
            ) -> googleapiclient.http.HttpRequest: ...
            def list(
                self, *, accountId: str, locale: str = ..., **kwargs: typing.Any
            ) -> AlertsHttpRequest: ...
        class UrlchannelsResource(googleapiclient.discovery.Resource):
            def list(
                self,
                *,
                accountId: str,
                adClientId: str,
                pageToken: str = ...,
                maxResults: int = ...,
                **kwargs: typing.Any
            ) -> UrlChannelsHttpRequest: ...
        class AdclientsResource(googleapiclient.discovery.Resource):
            def list(
                self,
                *,
                accountId: str,
                maxResults: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> AdClientsHttpRequest: ...
            def getAdCode(
                self, *, accountId: str, adClientId: str, **kwargs: typing.Any
            ) -> AdCodeHttpRequest: ...
        class CustomchannelsResource(googleapiclient.discovery.Resource):
            class AdunitsResource(googleapiclient.discovery.Resource):
                def list(
                    self,
                    *,
                    accountId: str,
                    adClientId: str,
                    customChannelId: str,
                    maxResults: int = ...,
                    pageToken: str = ...,
                    includeInactive: bool = ...,
                    **kwargs: typing.Any
                ) -> AdUnitsHttpRequest: ...
            def list(
                self,
                *,
                accountId: str,
                adClientId: str,
                maxResults: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> CustomChannelsHttpRequest: ...
            def get(
                self,
                *,
                accountId: str,
                adClientId: str,
                customChannelId: str,
                **kwargs: typing.Any
            ) -> CustomChannelHttpRequest: ...
            def adunits(self) -> AdunitsResource: ...
        def list(
            self, *, pageToken: str = ..., maxResults: int = ..., **kwargs: typing.Any
        ) -> AccountsHttpRequest: ...
        def get(
            self, *, accountId: str, tree: bool = ..., **kwargs: typing.Any
        ) -> AccountHttpRequest: ...
        def reports(self) -> ReportsResource: ...
        def adunits(self) -> AdunitsResource: ...
        def savedadstyles(self) -> SavedadstylesResource: ...
        def payments(self) -> PaymentsResource: ...
        def alerts(self) -> AlertsResource: ...
        def urlchannels(self) -> UrlchannelsResource: ...
        def adclients(self) -> AdclientsResource: ...
        def customchannels(self) -> CustomchannelsResource: ...
    class PaymentsResource(googleapiclient.discovery.Resource):
        def list(self, **kwargs: typing.Any) -> PaymentsHttpRequest: ...
    class MetadataResource(googleapiclient.discovery.Resource):
        class DimensionsResource(googleapiclient.discovery.Resource):
            def list(self, **kwargs: typing.Any) -> MetadataHttpRequest: ...
        class MetricsResource(googleapiclient.discovery.Resource):
            def list(self, **kwargs: typing.Any) -> MetadataHttpRequest: ...
        def dimensions(self) -> DimensionsResource: ...
        def metrics(self) -> MetricsResource: ...
    class AlertsResource(googleapiclient.discovery.Resource):
        def list(
            self, *, locale: str = ..., **kwargs: typing.Any
        ) -> AlertsHttpRequest: ...
        def delete(
            self, *, alertId: str, **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
    def adunits(self) -> AdunitsResource: ...
    def adclients(self) -> AdclientsResource: ...
    def customchannels(self) -> CustomchannelsResource: ...
    def reports(self) -> ReportsResource: ...
    def urlchannels(self) -> UrlchannelsResource: ...
    def savedadstyles(self) -> SavedadstylesResource: ...
    def accounts(self) -> AccountsResource: ...
    def payments(self) -> PaymentsResource: ...
    def metadata(self) -> MetadataResource: ...
    def alerts(self) -> AlertsResource: ...

class AccountsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Accounts: ...

class AdClientsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> AdClients: ...

class SavedAdStylesHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> SavedAdStyles: ...

class SavedReportsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> SavedReports: ...

class CustomChannelsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> CustomChannels: ...

class AccountHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Account: ...

class UrlChannelsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> UrlChannels: ...

class AdUnitsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> AdUnits: ...

class PaymentsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Payments: ...

class SavedAdStyleHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> SavedAdStyle: ...

class MetadataHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Metadata: ...

class AdUnitHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> AdUnit: ...

class CustomChannelHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> CustomChannel: ...

class AdCodeHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> AdCode: ...

class AlertsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Alerts: ...

class AdsenseReportsGenerateResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> AdsenseReportsGenerateResponse: ...
