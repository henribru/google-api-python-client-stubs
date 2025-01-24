import collections.abc
import typing

import httplib2
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http

from .schemas import *

_list = list

@typing.type_check_only
class AdSensePlatformResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class AccountsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class PlatformsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class ChildAccountsResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class SitesResource(googleapiclient.discovery.Resource):
                    def list(
                        self,
                        *,
                        parent: str,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
                    ) -> ListPlatformChildSitesResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: ListPlatformChildSitesResponseHttpRequest,
                        previous_response: ListPlatformChildSitesResponse,
                    ) -> ListPlatformChildSitesResponseHttpRequest | None: ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: PlatformChildSite = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any,
                    ) -> PlatformChildSiteHttpRequest: ...

                def sites(self) -> SitesResource: ...

            @typing.type_check_only
            class GroupsResource(googleapiclient.discovery.Resource):
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> ListPlatformGroupsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListPlatformGroupsResponseHttpRequest,
                    previous_response: ListPlatformGroupsResponse,
                ) -> ListPlatformGroupsResponseHttpRequest | None: ...

            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> PlatformHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any,
            ) -> ListPlatformsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListPlatformsResponseHttpRequest,
                previous_response: ListPlatformsResponse,
            ) -> ListPlatformsResponseHttpRequest | None: ...
            def childAccounts(self) -> ChildAccountsResource: ...
            def groups(self) -> GroupsResource: ...

        def platforms(self) -> PlatformsResource: ...

    @typing.type_check_only
    class PlatformsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class AccountsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class EventsResource(googleapiclient.discovery.Resource):
                def create(
                    self, *, parent: str, body: Event = ..., **kwargs: typing.Any
                ) -> EventHttpRequest: ...

            @typing.type_check_only
            class SitesResource(googleapiclient.discovery.Resource):
                def create(
                    self, *, parent: str, body: Site = ..., **kwargs: typing.Any
                ) -> SiteHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> SiteHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> ListSitesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListSitesResponseHttpRequest,
                    previous_response: ListSitesResponse,
                ) -> ListSitesResponseHttpRequest | None: ...
                def requestReview(
                    self, *, name: str, **kwargs: typing.Any
                ) -> RequestSiteReviewResponseHttpRequest: ...

            def close(  # type: ignore[override]
                self,
                *,
                name: str,
                body: CloseAccountRequest = ...,
                **kwargs: typing.Any,
            ) -> CloseAccountResponseHttpRequest: ...
            def create(
                self, *, parent: str, body: Account = ..., **kwargs: typing.Any
            ) -> AccountHttpRequest: ...
            def get(self, *, name: str, **kwargs: typing.Any) -> AccountHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any,
            ) -> ListAccountsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListAccountsResponseHttpRequest,
                previous_response: ListAccountsResponse,
            ) -> ListAccountsResponseHttpRequest | None: ...
            def lookup(
                self, *, parent: str, creationRequestId: str = ..., **kwargs: typing.Any
            ) -> LookupAccountResponseHttpRequest: ...
            def events(self) -> EventsResource: ...
            def sites(self) -> SitesResource: ...

        def accounts(self) -> AccountsResource: ...

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
    def platforms(self) -> PlatformsResource: ...

@typing.type_check_only
class AccountHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Account: ...

@typing.type_check_only
class CloseAccountResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> CloseAccountResponse: ...

@typing.type_check_only
class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Empty: ...

@typing.type_check_only
class EventHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Event: ...

@typing.type_check_only
class ListAccountsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListAccountsResponse: ...

@typing.type_check_only
class ListPlatformChildSitesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListPlatformChildSitesResponse: ...

@typing.type_check_only
class ListPlatformGroupsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListPlatformGroupsResponse: ...

@typing.type_check_only
class ListPlatformsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListPlatformsResponse: ...

@typing.type_check_only
class ListSitesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListSitesResponse: ...

@typing.type_check_only
class LookupAccountResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> LookupAccountResponse: ...

@typing.type_check_only
class PlatformHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Platform: ...

@typing.type_check_only
class PlatformChildSiteHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> PlatformChildSite: ...

@typing.type_check_only
class RequestSiteReviewResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> RequestSiteReviewResponse: ...

@typing.type_check_only
class SiteHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Site: ...
