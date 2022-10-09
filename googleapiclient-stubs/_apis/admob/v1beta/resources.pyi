import collections.abc
import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

_list = list

@typing.type_check_only
class AdMobResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class AccountsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class AdSourcesResource(googleapiclient.discovery.Resource):
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> ListAdSourcesResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListAdSourcesResponseHttpRequest,
                previous_response: ListAdSourcesResponse,
            ) -> ListAdSourcesResponseHttpRequest | None: ...

        @typing.type_check_only
        class AdUnitsResource(googleapiclient.discovery.Resource):
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

        @typing.type_check_only
        class AppsResource(googleapiclient.discovery.Resource):
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> ListAppsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListAppsResponseHttpRequest,
                previous_response: ListAppsResponse,
            ) -> ListAppsResponseHttpRequest | None: ...

        @typing.type_check_only
        class MediationReportResource(googleapiclient.discovery.Resource):
            def generate(
                self,
                *,
                parent: str,
                body: GenerateMediationReportRequest = ...,
                **kwargs: typing.Any
            ) -> GenerateMediationReportResponseHttpRequest: ...

        @typing.type_check_only
        class NetworkReportResource(googleapiclient.discovery.Resource):
            def generate(
                self,
                *,
                parent: str,
                body: GenerateNetworkReportRequest = ...,
                **kwargs: typing.Any
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
        def adUnits(self) -> AdUnitsResource: ...
        def apps(self) -> AppsResource: ...
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
        | None = ...,
    ) -> googleapiclient.http.BatchHttpRequest: ...
    def accounts(self) -> AccountsResource: ...

@typing.type_check_only
class GenerateMediationReportResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GenerateMediationReportResponse: ...

@typing.type_check_only
class GenerateNetworkReportResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GenerateNetworkReportResponse: ...

@typing.type_check_only
class ListAdSourcesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListAdSourcesResponse: ...

@typing.type_check_only
class ListAdUnitsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListAdUnitsResponse: ...

@typing.type_check_only
class ListAppsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListAppsResponse: ...

@typing.type_check_only
class ListPublisherAccountsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListPublisherAccountsResponse: ...

@typing.type_check_only
class PublisherAccountHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> PublisherAccount: ...
