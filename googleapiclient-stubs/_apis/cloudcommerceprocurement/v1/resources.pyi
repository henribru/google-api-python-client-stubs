import collections.abc
import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

_list = list

@typing.type_check_only
class CloudCommercePartnerProcurementServiceResource(
    googleapiclient.discovery.Resource
):
    @typing.type_check_only
    class ProvidersResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class AccountsResource(googleapiclient.discovery.Resource):
            def approve(
                self,
                *,
                name: str,
                body: ApproveAccountRequest = ...,
                **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def get(self, *, name: str, **kwargs: typing.Any) -> AccountHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> ListAccountsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListAccountsResponseHttpRequest,
                previous_response: ListAccountsResponse,
            ) -> ListAccountsResponseHttpRequest | None: ...
            def reject(
                self,
                *,
                name: str,
                body: RejectAccountRequest = ...,
                **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def reset(
                self,
                *,
                name: str,
                body: ResetAccountRequest = ...,
                **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...

        @typing.type_check_only
        class EntitlementsResource(googleapiclient.discovery.Resource):
            def approve(
                self,
                *,
                name: str,
                body: ApproveEntitlementRequest = ...,
                **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def approvePlanChange(
                self,
                *,
                name: str,
                body: ApproveEntitlementPlanChangeRequest = ...,
                **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> EntitlementHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                filter: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> ListEntitlementsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListEntitlementsResponseHttpRequest,
                previous_response: ListEntitlementsResponse,
            ) -> ListEntitlementsResponseHttpRequest | None: ...
            def patch(
                self,
                *,
                name: str,
                body: Entitlement = ...,
                updateMask: str = ...,
                **kwargs: typing.Any
            ) -> EntitlementHttpRequest: ...
            def reject(
                self,
                *,
                name: str,
                body: RejectEntitlementRequest = ...,
                **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def rejectPlanChange(
                self,
                *,
                name: str,
                body: RejectEntitlementPlanChangeRequest = ...,
                **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def suspend(
                self,
                *,
                name: str,
                body: SuspendEntitlementRequest = ...,
                **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...

        def accounts(self) -> AccountsResource: ...
        def entitlements(self) -> EntitlementsResource: ...

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
    def providers(self) -> ProvidersResource: ...

@typing.type_check_only
class AccountHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Account: ...

@typing.type_check_only
class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Empty: ...

@typing.type_check_only
class EntitlementHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Entitlement: ...

@typing.type_check_only
class ListAccountsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListAccountsResponse: ...

@typing.type_check_only
class ListEntitlementsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListEntitlementsResponse: ...
