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
        class AdUnitsResource(googleapiclient.discovery.Resource):
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

        @typing.type_check_only
        class AppsResource(googleapiclient.discovery.Resource):
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
        | None = None,
    ) -> googleapiclient.http.BatchHttpRequest: ...
    def accounts(self) -> AccountsResource: ...

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
class ListAdUnitsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListAdUnitsResponse: ...

@typing.type_check_only
class ListAppsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListAppsResponse: ...

@typing.type_check_only
class ListPublisherAccountsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListPublisherAccountsResponse: ...

@typing.type_check_only
class PublisherAccountHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> PublisherAccount: ...
