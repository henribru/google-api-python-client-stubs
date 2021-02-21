import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *
@typing.type_check_only
class AdSenseHostResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class AccountsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class AdclientsResource(googleapiclient.discovery.Resource):
            def get(
                self, *, accountId: str, adClientId: str, **kwargs: typing.Any
            ) -> AdClientHttpRequest: ...
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
            def delete(
                self,
                *,
                accountId: str,
                adClientId: str,
                adUnitId: str,
                **kwargs: typing.Any
            ) -> AdUnitHttpRequest: ...
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
                hostCustomChannelId: typing.Union[str, typing.List[str]] = ...,
                **kwargs: typing.Any
            ) -> AdCodeHttpRequest: ...
            def insert(
                self,
                *,
                accountId: str,
                adClientId: str,
                body: AdUnit = ...,
                **kwargs: typing.Any
            ) -> AdUnitHttpRequest: ...
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
            def patch(
                self,
                *,
                accountId: str,
                adClientId: str,
                adUnitId: str,
                body: AdUnit = ...,
                **kwargs: typing.Any
            ) -> AdUnitHttpRequest: ...
            def update(
                self,
                *,
                accountId: str,
                adClientId: str,
                body: AdUnit = ...,
                **kwargs: typing.Any
            ) -> AdUnitHttpRequest: ...
        @typing.type_check_only
        class ReportsResource(googleapiclient.discovery.Resource):
            def generate(
                self,
                *,
                accountId: str,
                startDate: str,
                endDate: str,
                dimension: typing.Union[str, typing.List[str]] = ...,
                filter: typing.Union[str, typing.List[str]] = ...,
                locale: str = ...,
                maxResults: int = ...,
                metric: typing.Union[str, typing.List[str]] = ...,
                sort: typing.Union[str, typing.List[str]] = ...,
                startIndex: int = ...,
                **kwargs: typing.Any
            ) -> ReportHttpRequest: ...
        def get(
            self, *, accountId: str, **kwargs: typing.Any
        ) -> AccountHttpRequest: ...
        def list(
            self,
            *,
            filterAdClientId: typing.Union[str, typing.List[str]],
            **kwargs: typing.Any
        ) -> AccountsHttpRequest: ...
        def adclients(self) -> AdclientsResource: ...
        def adunits(self) -> AdunitsResource: ...
        def reports(self) -> ReportsResource: ...
    @typing.type_check_only
    class AdclientsResource(googleapiclient.discovery.Resource):
        def get(
            self, *, adClientId: str, **kwargs: typing.Any
        ) -> AdClientHttpRequest: ...
        def list(
            self, *, maxResults: int = ..., pageToken: str = ..., **kwargs: typing.Any
        ) -> AdClientsHttpRequest: ...
    @typing.type_check_only
    class AssociationsessionsResource(googleapiclient.discovery.Resource):
        def start(
            self,
            *,
            productCode: typing.Union[
                typing_extensions.Literal["AFC", "AFG", "AFMC", "AFS", "AFV"],
                typing.List[
                    typing_extensions.Literal["AFC", "AFG", "AFMC", "AFS", "AFV"]
                ],
            ],
            websiteUrl: str,
            callbackUrl: str = ...,
            userLocale: str = ...,
            websiteLocale: str = ...,
            **kwargs: typing.Any
        ) -> AssociationSessionHttpRequest: ...
        def verify(
            self, *, token: str, **kwargs: typing.Any
        ) -> AssociationSessionHttpRequest: ...
    @typing.type_check_only
    class CustomchannelsResource(googleapiclient.discovery.Resource):
        def delete(
            self, *, adClientId: str, customChannelId: str, **kwargs: typing.Any
        ) -> CustomChannelHttpRequest: ...
        def get(
            self, *, adClientId: str, customChannelId: str, **kwargs: typing.Any
        ) -> CustomChannelHttpRequest: ...
        def insert(
            self, *, adClientId: str, body: CustomChannel = ..., **kwargs: typing.Any
        ) -> CustomChannelHttpRequest: ...
        def list(
            self,
            *,
            adClientId: str,
            maxResults: int = ...,
            pageToken: str = ...,
            **kwargs: typing.Any
        ) -> CustomChannelsHttpRequest: ...
        def patch(
            self,
            *,
            adClientId: str,
            customChannelId: str,
            body: CustomChannel = ...,
            **kwargs: typing.Any
        ) -> CustomChannelHttpRequest: ...
        def update(
            self, *, adClientId: str, body: CustomChannel = ..., **kwargs: typing.Any
        ) -> CustomChannelHttpRequest: ...
    @typing.type_check_only
    class ReportsResource(googleapiclient.discovery.Resource):
        def generate(
            self,
            *,
            startDate: str,
            endDate: str,
            dimension: typing.Union[str, typing.List[str]] = ...,
            filter: typing.Union[str, typing.List[str]] = ...,
            locale: str = ...,
            maxResults: int = ...,
            metric: typing.Union[str, typing.List[str]] = ...,
            sort: typing.Union[str, typing.List[str]] = ...,
            startIndex: int = ...,
            **kwargs: typing.Any
        ) -> ReportHttpRequest: ...
    @typing.type_check_only
    class UrlchannelsResource(googleapiclient.discovery.Resource):
        def delete(
            self, *, adClientId: str, urlChannelId: str, **kwargs: typing.Any
        ) -> UrlChannelHttpRequest: ...
        def insert(
            self, *, adClientId: str, body: UrlChannel = ..., **kwargs: typing.Any
        ) -> UrlChannelHttpRequest: ...
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
    def associationsessions(self) -> AssociationsessionsResource: ...
    def customchannels(self) -> CustomchannelsResource: ...
    def reports(self) -> ReportsResource: ...
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
class AdClientHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> AdClient: ...

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
class AssociationSessionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> AssociationSession: ...

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
class ReportHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> Report: ...

@typing.type_check_only
class UrlChannelHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> UrlChannel: ...

@typing.type_check_only
class UrlChannelsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> UrlChannels: ...
