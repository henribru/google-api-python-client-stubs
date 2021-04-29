import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

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
    def providers(self) -> ProvidersResource: ...

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
class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> Empty: ...

@typing.type_check_only
class EntitlementHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> Entitlement: ...

@typing.type_check_only
class ListAccountsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> ListAccountsResponse: ...

@typing.type_check_only
class ListEntitlementsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> ListEntitlementsResponse: ...
