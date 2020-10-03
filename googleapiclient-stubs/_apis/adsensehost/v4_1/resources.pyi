import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class AdSenseHostResource(googleapiclient.discovery.Resource):
    class ReportsResource(googleapiclient.discovery.Resource):
        def generate(
            self,
            *,
            startDate: str,
            endDate: str,
            sort: typing.Union[str, typing.List[str]] = ...,
            dimension: typing.Union[str, typing.List[str]] = ...,
            locale: str = ...,
            metric: typing.Union[str, typing.List[str]] = ...,
            startIndex: int = ...,
            maxResults: int = ...,
            filter: typing.Union[str, typing.List[str]] = ...,
            **kwargs: typing.Any
        ) -> ReportHttpRequest: ...
    class CustomchannelsResource(googleapiclient.discovery.Resource):
        def update(
            self, *, adClientId: str, body: CustomChannel = ..., **kwargs: typing.Any
        ) -> CustomChannelHttpRequest: ...
        def get(
            self, *, adClientId: str, customChannelId: str, **kwargs: typing.Any
        ) -> CustomChannelHttpRequest: ...
        def delete(
            self, *, adClientId: str, customChannelId: str, **kwargs: typing.Any
        ) -> CustomChannelHttpRequest: ...
        def patch(
            self,
            *,
            adClientId: str,
            customChannelId: str,
            body: CustomChannel = ...,
            **kwargs: typing.Any
        ) -> CustomChannelHttpRequest: ...
        def list(
            self,
            *,
            adClientId: str,
            maxResults: int = ...,
            pageToken: str = ...,
            **kwargs: typing.Any
        ) -> CustomChannelsHttpRequest: ...
        def insert(
            self, *, adClientId: str, body: CustomChannel = ..., **kwargs: typing.Any
        ) -> CustomChannelHttpRequest: ...
    class AccountsResource(googleapiclient.discovery.Resource):
        class ReportsResource(googleapiclient.discovery.Resource):
            def generate(
                self,
                *,
                accountId: str,
                startDate: str,
                endDate: str,
                filter: typing.Union[str, typing.List[str]] = ...,
                sort: typing.Union[str, typing.List[str]] = ...,
                maxResults: int = ...,
                dimension: typing.Union[str, typing.List[str]] = ...,
                locale: str = ...,
                metric: typing.Union[str, typing.List[str]] = ...,
                startIndex: int = ...,
                **kwargs: typing.Any
            ) -> ReportHttpRequest: ...
        class AdunitsResource(googleapiclient.discovery.Resource):
            def update(
                self,
                *,
                accountId: str,
                adClientId: str,
                body: AdUnit = ...,
                **kwargs: typing.Any
            ) -> AdUnitHttpRequest: ...
            def delete(
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
            def patch(
                self,
                *,
                accountId: str,
                adClientId: str,
                adUnitId: str,
                body: AdUnit = ...,
                **kwargs: typing.Any
            ) -> AdUnitHttpRequest: ...
            def list(
                self,
                *,
                accountId: str,
                adClientId: str,
                maxResults: int = ...,
                pageToken: str = ...,
                includeInactive: bool = ...,
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
            def insert(
                self,
                *,
                accountId: str,
                adClientId: str,
                body: AdUnit = ...,
                **kwargs: typing.Any
            ) -> AdUnitHttpRequest: ...
        class AdclientsResource(googleapiclient.discovery.Resource):
            def list(
                self,
                *,
                accountId: str,
                maxResults: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> AdClientsHttpRequest: ...
            def get(
                self, *, accountId: str, adClientId: str, **kwargs: typing.Any
            ) -> AdClientHttpRequest: ...
        def get(
            self, *, accountId: str, **kwargs: typing.Any
        ) -> AccountHttpRequest: ...
        def list(
            self,
            *,
            filterAdClientId: typing.Union[str, typing.List[str]],
            **kwargs: typing.Any
        ) -> AccountsHttpRequest: ...
        def reports(self) -> ReportsResource: ...
        def adunits(self) -> AdunitsResource: ...
        def adclients(self) -> AdclientsResource: ...
    class AssociationsessionsResource(googleapiclient.discovery.Resource):
        def verify(
            self, *, token: str, **kwargs: typing.Any
        ) -> AssociationSessionHttpRequest: ...
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
            userLocale: str = ...,
            websiteLocale: str = ...,
            callbackUrl: str = ...,
            **kwargs: typing.Any
        ) -> AssociationSessionHttpRequest: ...
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
    class AdclientsResource(googleapiclient.discovery.Resource):
        def list(
            self, *, maxResults: int = ..., pageToken: str = ..., **kwargs: typing.Any
        ) -> AdClientsHttpRequest: ...
        def get(
            self, *, adClientId: str, **kwargs: typing.Any
        ) -> AdClientHttpRequest: ...
    def reports(self) -> ReportsResource: ...
    def customchannels(self) -> CustomchannelsResource: ...
    def accounts(self) -> AccountsResource: ...
    def associationsessions(self) -> AssociationsessionsResource: ...
    def urlchannels(self) -> UrlchannelsResource: ...
    def adclients(self) -> AdclientsResource: ...

class AccountsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Accounts: ...

class AdClientsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> AdClients: ...

class AdClientHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> AdClient: ...

class AssociationSessionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> AssociationSession: ...

class AdUnitsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> AdUnits: ...

class ReportHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Report: ...

class UrlChannelHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> UrlChannel: ...

class AdUnitHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> AdUnit: ...

class CustomChannelHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> CustomChannel: ...

class CustomChannelsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> CustomChannels: ...

class AdCodeHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> AdCode: ...

class AccountHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Account: ...

class UrlChannelsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> UrlChannels: ...
