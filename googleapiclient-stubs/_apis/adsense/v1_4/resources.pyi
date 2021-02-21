import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *
@typing.type_check_only
class AdSenseResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class AccountsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class AdclientsResource(googleapiclient.discovery.Resource):
            def getAdCode(
                self,
                *,
                accountId: str,
                adClientId: str,
                tagPartner: str = ...,
                **kwargs: typing.Any
            ) -> AdCodeHttpRequest: ...
            def list(
                self,
                *,
                accountId: str,
                maxResults: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> AdClientsHttpRequest: ...
        @typing.type_check_only
        class AdunitsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
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
            def get(
                self,
                *,
                accountId: str,
                adClientId: str,
                adUnitId: str,
                **kwargs: typing.Any
            ) -> AdUnitHttpRequest: ...
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
                maxResults: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> AdUnitsHttpRequest: ...
            def customchannels(self) -> CustomchannelsResource: ...
        @typing.type_check_only
        class AlertsResource(googleapiclient.discovery.Resource):
            def delete(
                self, *, accountId: str, alertId: str, **kwargs: typing.Any
            ) -> googleapiclient.http.HttpRequest: ...
            def list(
                self, *, accountId: str, locale: str = ..., **kwargs: typing.Any
            ) -> AlertsHttpRequest: ...
        @typing.type_check_only
        class CustomchannelsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class AdunitsResource(googleapiclient.discovery.Resource):
                def list(
                    self,
                    *,
                    accountId: str,
                    adClientId: str,
                    customChannelId: str,
                    includeInactive: bool = ...,
                    maxResults: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> AdUnitsHttpRequest: ...
            def get(
                self,
                *,
                accountId: str,
                adClientId: str,
                customChannelId: str,
                **kwargs: typing.Any
            ) -> CustomChannelHttpRequest: ...
            def list(
                self,
                *,
                accountId: str,
                adClientId: str,
                maxResults: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> CustomChannelsHttpRequest: ...
            def adunits(self) -> AdunitsResource: ...
        @typing.type_check_only
        class PaymentsResource(googleapiclient.discovery.Resource):
            def list(
                self, *, accountId: str, **kwargs: typing.Any
            ) -> PaymentsHttpRequest: ...
        @typing.type_check_only
        class ReportsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class SavedResource(googleapiclient.discovery.Resource):
                def generate(
                    self,
                    *,
                    accountId: str,
                    savedReportId: str,
                    locale: str = ...,
                    maxResults: int = ...,
                    startIndex: int = ...,
                    **kwargs: typing.Any
                ) -> AdsenseReportsGenerateResponseHttpRequest: ...
                def list(
                    self,
                    *,
                    accountId: str,
                    maxResults: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> SavedReportsHttpRequest: ...
            def generate(
                self,
                *,
                accountId: str,
                startDate: str,
                endDate: str,
                currency: str = ...,
                dimension: typing.Union[str, typing.List[str]] = ...,
                filter: typing.Union[str, typing.List[str]] = ...,
                locale: str = ...,
                maxResults: int = ...,
                metric: typing.Union[str, typing.List[str]] = ...,
                sort: typing.Union[str, typing.List[str]] = ...,
                startIndex: int = ...,
                useTimezoneReporting: bool = ...,
                **kwargs: typing.Any
            ) -> AdsenseReportsGenerateResponseHttpRequest: ...
            def saved(self) -> SavedResource: ...
        @typing.type_check_only
        class SavedadstylesResource(googleapiclient.discovery.Resource):
            def get(
                self, *, accountId: str, savedAdStyleId: str, **kwargs: typing.Any
            ) -> SavedAdStyleHttpRequest: ...
            def list(
                self,
                *,
                accountId: str,
                maxResults: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> SavedAdStylesHttpRequest: ...
        @typing.type_check_only
        class UrlchannelsResource(googleapiclient.discovery.Resource):
            def list(
                self,
                *,
                accountId: str,
                adClientId: str,
                maxResults: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> UrlChannelsHttpRequest: ...
        def get(
            self, *, accountId: str, tree: bool = ..., **kwargs: typing.Any
        ) -> AccountHttpRequest: ...
        def list(
            self, *, maxResults: int = ..., pageToken: str = ..., **kwargs: typing.Any
        ) -> AccountsHttpRequest: ...
        def adclients(self) -> AdclientsResource: ...
        def adunits(self) -> AdunitsResource: ...
        def alerts(self) -> AlertsResource: ...
        def customchannels(self) -> CustomchannelsResource: ...
        def payments(self) -> PaymentsResource: ...
        def reports(self) -> ReportsResource: ...
        def savedadstyles(self) -> SavedadstylesResource: ...
        def urlchannels(self) -> UrlchannelsResource: ...
    @typing.type_check_only
    class AdclientsResource(googleapiclient.discovery.Resource):
        def list(
            self, *, maxResults: int = ..., pageToken: str = ..., **kwargs: typing.Any
        ) -> AdClientsHttpRequest: ...
    @typing.type_check_only
    class AdunitsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
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
        def get(
            self, *, adClientId: str, adUnitId: str, **kwargs: typing.Any
        ) -> AdUnitHttpRequest: ...
        def getAdCode(
            self, *, adClientId: str, adUnitId: str, **kwargs: typing.Any
        ) -> AdCodeHttpRequest: ...
        def list(
            self,
            *,
            adClientId: str,
            includeInactive: bool = ...,
            maxResults: int = ...,
            pageToken: str = ...,
            **kwargs: typing.Any
        ) -> AdUnitsHttpRequest: ...
        def customchannels(self) -> CustomchannelsResource: ...
    @typing.type_check_only
    class AlertsResource(googleapiclient.discovery.Resource):
        def delete(
            self, *, alertId: str, **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def list(
            self, *, locale: str = ..., **kwargs: typing.Any
        ) -> AlertsHttpRequest: ...
    @typing.type_check_only
    class CustomchannelsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class AdunitsResource(googleapiclient.discovery.Resource):
            def list(
                self,
                *,
                adClientId: str,
                customChannelId: str,
                includeInactive: bool = ...,
                maxResults: int = ...,
                pageToken: str = ...,
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
    @typing.type_check_only
    class MetadataResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class DimensionsResource(googleapiclient.discovery.Resource):
            def list(self, **kwargs: typing.Any) -> MetadataHttpRequest: ...
        @typing.type_check_only
        class MetricsResource(googleapiclient.discovery.Resource):
            def list(self, **kwargs: typing.Any) -> MetadataHttpRequest: ...
        def dimensions(self) -> DimensionsResource: ...
        def metrics(self) -> MetricsResource: ...
    @typing.type_check_only
    class PaymentsResource(googleapiclient.discovery.Resource):
        def list(self, **kwargs: typing.Any) -> PaymentsHttpRequest: ...
    @typing.type_check_only
    class ReportsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class SavedResource(googleapiclient.discovery.Resource):
            def generate(
                self,
                *,
                savedReportId: str,
                locale: str = ...,
                maxResults: int = ...,
                startIndex: int = ...,
                **kwargs: typing.Any
            ) -> AdsenseReportsGenerateResponseHttpRequest: ...
            def list(
                self,
                *,
                maxResults: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> SavedReportsHttpRequest: ...
        def generate(
            self,
            *,
            startDate: str,
            endDate: str,
            accountId: typing.Union[str, typing.List[str]] = ...,
            currency: str = ...,
            dimension: typing.Union[str, typing.List[str]] = ...,
            filter: typing.Union[str, typing.List[str]] = ...,
            locale: str = ...,
            maxResults: int = ...,
            metric: typing.Union[str, typing.List[str]] = ...,
            sort: typing.Union[str, typing.List[str]] = ...,
            startIndex: int = ...,
            useTimezoneReporting: bool = ...,
            **kwargs: typing.Any
        ) -> AdsenseReportsGenerateResponseHttpRequest: ...
        def saved(self) -> SavedResource: ...
    @typing.type_check_only
    class SavedadstylesResource(googleapiclient.discovery.Resource):
        def get(
            self, *, savedAdStyleId: str, **kwargs: typing.Any
        ) -> SavedAdStyleHttpRequest: ...
        def list(
            self, *, maxResults: int = ..., pageToken: str = ..., **kwargs: typing.Any
        ) -> SavedAdStylesHttpRequest: ...
    @typing.type_check_only
    class UrlchannelsResource(googleapiclient.discovery.Resource):
        def list(
            self,
            *,
            adClientId: str,
            maxResults: int = ...,
            pageToken: str = ...,
            **kwargs: typing.Any
        ) -> UrlChannelsHttpRequest: ...
    def accounts(self) -> AccountsResource: ...
    def adclients(self) -> AdclientsResource: ...
    def adunits(self) -> AdunitsResource: ...
    def alerts(self) -> AlertsResource: ...
    def customchannels(self) -> CustomchannelsResource: ...
    def metadata(self) -> MetadataResource: ...
    def payments(self) -> PaymentsResource: ...
    def reports(self) -> ReportsResource: ...
    def savedadstyles(self) -> SavedadstylesResource: ...
    def urlchannels(self) -> UrlchannelsResource: ...

@typing.type_check_only
class AccountHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> Account: ...

@typing.type_check_only
class AccountsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> Accounts: ...

@typing.type_check_only
class AdClientsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> AdClients: ...

@typing.type_check_only
class AdCodeHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> AdCode: ...

@typing.type_check_only
class AdUnitHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> AdUnit: ...

@typing.type_check_only
class AdUnitsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> AdUnits: ...

@typing.type_check_only
class AdsenseReportsGenerateResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> AdsenseReportsGenerateResponse: ...

@typing.type_check_only
class AlertsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> Alerts: ...

@typing.type_check_only
class CustomChannelHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> CustomChannel: ...

@typing.type_check_only
class CustomChannelsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> CustomChannels: ...

@typing.type_check_only
class MetadataHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> Metadata: ...

@typing.type_check_only
class PaymentsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> Payments: ...

@typing.type_check_only
class SavedAdStyleHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> SavedAdStyle: ...

@typing.type_check_only
class SavedAdStylesHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> SavedAdStyles: ...

@typing.type_check_only
class SavedReportsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> SavedReports: ...

@typing.type_check_only
class UrlChannelsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> UrlChannels: ...
