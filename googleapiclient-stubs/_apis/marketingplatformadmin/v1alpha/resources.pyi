import collections.abc
import typing

import httplib2
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http

from .schemas import *

_list = list

@typing.type_check_only
class GoogleMarketingPlatformAdminAPIResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class OrganizationsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class AnalyticsAccountLinksResource(googleapiclient.discovery.Resource):
            def create(
                self,
                *,
                parent: str,
                body: AnalyticsAccountLink = ...,
                **kwargs: typing.Any,
            ) -> AnalyticsAccountLinkHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any,
            ) -> ListAnalyticsAccountLinksResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListAnalyticsAccountLinksResponseHttpRequest,
                previous_response: ListAnalyticsAccountLinksResponse,
            ) -> ListAnalyticsAccountLinksResponseHttpRequest | None: ...
            def setPropertyServiceLevel(
                self,
                *,
                analyticsAccountLink: str,
                body: SetPropertyServiceLevelRequest = ...,
                **kwargs: typing.Any,
            ) -> SetPropertyServiceLevelResponseHttpRequest: ...

        def get(
            self, *, name: str, **kwargs: typing.Any
        ) -> OrganizationHttpRequest: ...
        def analyticsAccountLinks(self) -> AnalyticsAccountLinksResource: ...

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
    def organizations(self) -> OrganizationsResource: ...

@typing.type_check_only
class AnalyticsAccountLinkHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> AnalyticsAccountLink: ...

@typing.type_check_only
class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Empty: ...

@typing.type_check_only
class ListAnalyticsAccountLinksResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListAnalyticsAccountLinksResponse: ...

@typing.type_check_only
class OrganizationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Organization: ...

@typing.type_check_only
class SetPropertyServiceLevelResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> SetPropertyServiceLevelResponse: ...
