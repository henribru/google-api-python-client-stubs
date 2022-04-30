import collections.abc
import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

_list = list

@typing.type_check_only
class MyBusinessAccountManagementResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class AccountsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class AdminsResource(googleapiclient.discovery.Resource):
            def create(
                self, *, parent: str, body: Admin = ..., **kwargs: typing.Any
            ) -> AdminHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def list(
                self, *, parent: str, **kwargs: typing.Any
            ) -> ListAccountAdminsResponseHttpRequest: ...
            def patch(
                self,
                *,
                name: str,
                body: Admin = ...,
                updateMask: str = ...,
                **kwargs: typing.Any
            ) -> AdminHttpRequest: ...

        @typing.type_check_only
        class InvitationsResource(googleapiclient.discovery.Resource):
            def accept(
                self,
                *,
                name: str,
                body: AcceptInvitationRequest = ...,
                **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def decline(
                self,
                *,
                name: str,
                body: DeclineInvitationRequest = ...,
                **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def list(
                self, *, parent: str, filter: str = ..., **kwargs: typing.Any
            ) -> ListInvitationsResponseHttpRequest: ...

        def create(
            self, *, body: Account = ..., **kwargs: typing.Any
        ) -> AccountHttpRequest: ...
        def get(self, *, name: str, **kwargs: typing.Any) -> AccountHttpRequest: ...
        def list(
            self,
            *,
            filter: str = ...,
            pageSize: int = ...,
            pageToken: str = ...,
            parentAccount: str = ...,
            **kwargs: typing.Any
        ) -> ListAccountsResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: ListAccountsResponseHttpRequest,
            previous_response: ListAccountsResponse,
        ) -> ListAccountsResponseHttpRequest | None: ...
        def patch(
            self,
            *,
            name: str,
            body: Account = ...,
            updateMask: str = ...,
            validateOnly: bool = ...,
            **kwargs: typing.Any
        ) -> AccountHttpRequest: ...
        def admins(self) -> AdminsResource: ...
        def invitations(self) -> InvitationsResource: ...

    @typing.type_check_only
    class LocationsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class AdminsResource(googleapiclient.discovery.Resource):
            def create(
                self, *, parent: str, body: Admin = ..., **kwargs: typing.Any
            ) -> AdminHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def list(
                self, *, parent: str, **kwargs: typing.Any
            ) -> ListLocationAdminsResponseHttpRequest: ...
            def patch(
                self,
                *,
                name: str,
                body: Admin = ...,
                updateMask: str = ...,
                **kwargs: typing.Any
            ) -> AdminHttpRequest: ...

        def transfer(
            self,
            *,
            name: str,
            body: TransferLocationRequest = ...,
            **kwargs: typing.Any
        ) -> EmptyHttpRequest: ...
        def admins(self) -> AdminsResource: ...

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
    def locations(self) -> LocationsResource: ...

@typing.type_check_only
class AccountHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Account: ...

@typing.type_check_only
class AdminHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Admin: ...

@typing.type_check_only
class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Empty: ...

@typing.type_check_only
class ListAccountAdminsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListAccountAdminsResponse: ...

@typing.type_check_only
class ListAccountsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListAccountsResponse: ...

@typing.type_check_only
class ListInvitationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListInvitationsResponse: ...

@typing.type_check_only
class ListLocationAdminsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListLocationAdminsResponse: ...
