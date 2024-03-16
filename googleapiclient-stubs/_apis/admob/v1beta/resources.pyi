import collections.abc
import typing

import httplib2
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http

from .schemas import *

_list = list

@typing.type_check_only
class AdMobResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class AccountsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class AdSourcesResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class AdaptersResource(googleapiclient.discovery.Resource):
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> ListAdaptersResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListAdaptersResponseHttpRequest,
                    previous_response: ListAdaptersResponse,
                ) -> ListAdaptersResponseHttpRequest | None: ...

            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any,
            ) -> ListAdSourcesResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListAdSourcesResponseHttpRequest,
                previous_response: ListAdSourcesResponse,
            ) -> ListAdSourcesResponseHttpRequest | None: ...
            def adapters(self) -> AdaptersResource: ...

        @typing.type_check_only
        class AdUnitMappingsResource(googleapiclient.discovery.Resource):
            def batchCreate(
                self,
                *,
                parent: str,
                body: BatchCreateAdUnitMappingsRequest = ...,
                **kwargs: typing.Any,
            ) -> BatchCreateAdUnitMappingsResponseHttpRequest: ...

        @typing.type_check_only
        class AdUnitsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class AdUnitMappingsResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: AdUnitMapping = ...,
                    **kwargs: typing.Any,
                ) -> AdUnitMappingHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> ListAdUnitMappingsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListAdUnitMappingsResponseHttpRequest,
                    previous_response: ListAdUnitMappingsResponse,
                ) -> ListAdUnitMappingsResponseHttpRequest | None: ...

            def create(
                self, *, parent: str, body: AdUnit = ..., **kwargs: typing.Any
            ) -> AdUnitHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any,
            ) -> ListAdUnitsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListAdUnitsResponseHttpRequest,
                previous_response: ListAdUnitsResponse,
            ) -> ListAdUnitsResponseHttpRequest | None: ...
            def adUnitMappings(self) -> AdUnitMappingsResource: ...

        @typing.type_check_only
        class AppsResource(googleapiclient.discovery.Resource):
            def create(
                self, *, parent: str, body: App = ..., **kwargs: typing.Any
            ) -> AppHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any,
            ) -> ListAppsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListAppsResponseHttpRequest,
                previous_response: ListAppsResponse,
            ) -> ListAppsResponseHttpRequest | None: ...

        @typing.type_check_only
        class CampaignReportResource(googleapiclient.discovery.Resource):
            def generate(
                self,
                *,
                parent: str,
                body: GenerateCampaignReportRequest = ...,
                **kwargs: typing.Any,
            ) -> GenerateCampaignReportResponseHttpRequest: ...

        @typing.type_check_only
        class MediationGroupsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class MediationAbExperimentsResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: MediationAbExperiment = ...,
                    **kwargs: typing.Any,
                ) -> MediationAbExperimentHttpRequest: ...
                def stop(
                    self,
                    *,
                    name: str,
                    body: StopMediationAbExperimentRequest = ...,
                    **kwargs: typing.Any,
                ) -> MediationAbExperimentHttpRequest: ...

            def create(
                self, *, parent: str, body: MediationGroup = ..., **kwargs: typing.Any
            ) -> MediationGroupHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                filter: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any,
            ) -> ListMediationGroupsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListMediationGroupsResponseHttpRequest,
                previous_response: ListMediationGroupsResponse,
            ) -> ListMediationGroupsResponseHttpRequest | None: ...
            def patch(
                self,
                *,
                name: str,
                body: MediationGroup = ...,
                updateMask: str = ...,
                **kwargs: typing.Any,
            ) -> MediationGroupHttpRequest: ...
            def mediationAbExperiments(self) -> MediationAbExperimentsResource: ...

        @typing.type_check_only
        class MediationReportResource(googleapiclient.discovery.Resource):
            def generate(
                self,
                *,
                parent: str,
                body: GenerateMediationReportRequest = ...,
                **kwargs: typing.Any,
            ) -> GenerateMediationReportResponseHttpRequest: ...

        @typing.type_check_only
        class NetworkReportResource(googleapiclient.discovery.Resource):
            def generate(
                self,
                *,
                parent: str,
                body: GenerateNetworkReportRequest = ...,
                **kwargs: typing.Any,
            ) -> GenerateNetworkReportResponseHttpRequest: ...

        def get(
            self, *, name: str, **kwargs: typing.Any
        ) -> PublisherAccountHttpRequest: ...
        def list(
            self, *, pageSize: int = ..., pageToken: str = ..., **kwargs: typing.Any
        ) -> ListPublisherAccountsResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: ListPublisherAccountsResponseHttpRequest,
            previous_response: ListPublisherAccountsResponse,
        ) -> ListPublisherAccountsResponseHttpRequest | None: ...
        def adSources(self) -> AdSourcesResource: ...
        def adUnitMappings(self) -> AdUnitMappingsResource: ...
        def adUnits(self) -> AdUnitsResource: ...
        def apps(self) -> AppsResource: ...
        def campaignReport(self) -> CampaignReportResource: ...
        def mediationGroups(self) -> MediationGroupsResource: ...
        def mediationReport(self) -> MediationReportResource: ...
        def networkReport(self) -> NetworkReportResource: ...

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
        | None = None,
    ) -> googleapiclient.http.BatchHttpRequest: ...
    def accounts(self) -> AccountsResource: ...

@typing.type_check_only
class AdUnitHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> AdUnit: ...

@typing.type_check_only
class AdUnitMappingHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> AdUnitMapping: ...

@typing.type_check_only
class AppHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> App: ...

@typing.type_check_only
class BatchCreateAdUnitMappingsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> BatchCreateAdUnitMappingsResponse: ...

@typing.type_check_only
class GenerateCampaignReportResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GenerateCampaignReportResponse: ...

@typing.type_check_only
class GenerateMediationReportResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GenerateMediationReportResponse: ...

@typing.type_check_only
class GenerateNetworkReportResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GenerateNetworkReportResponse: ...

@typing.type_check_only
class ListAdSourcesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListAdSourcesResponse: ...

@typing.type_check_only
class ListAdUnitMappingsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListAdUnitMappingsResponse: ...

@typing.type_check_only
class ListAdUnitsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListAdUnitsResponse: ...

@typing.type_check_only
class ListAdaptersResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListAdaptersResponse: ...

@typing.type_check_only
class ListAppsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListAppsResponse: ...

@typing.type_check_only
class ListMediationGroupsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListMediationGroupsResponse: ...

@typing.type_check_only
class ListPublisherAccountsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListPublisherAccountsResponse: ...

@typing.type_check_only
class MediationAbExperimentHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> MediationAbExperiment: ...

@typing.type_check_only
class MediationGroupHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> MediationGroup: ...

@typing.type_check_only
class PublisherAccountHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> PublisherAccount: ...
