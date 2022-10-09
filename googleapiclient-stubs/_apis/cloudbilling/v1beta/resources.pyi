import collections.abc
import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

_list = list

@typing.type_check_only
class CloudbillingResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class BillingAccountsResource(googleapiclient.discovery.Resource):
        def estimateCostScenario(
            self,
            *,
            billingAccount: str,
            body: EstimateCostScenarioForBillingAccountRequest = ...,
            **kwargs: typing.Any
        ) -> EstimateCostScenarioForBillingAccountResponseHttpRequest: ...

    @typing.type_check_only
    class V1betaResource(googleapiclient.discovery.Resource):
        def estimateCostScenario(
            self,
            *,
            body: EstimateCostScenarioWithListPriceRequest = ...,
            **kwargs: typing.Any
        ) -> EstimateCostScenarioWithListPriceResponseHttpRequest: ...

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
    def billingAccounts(self) -> BillingAccountsResource: ...
    def v1beta(self) -> V1betaResource: ...

@typing.type_check_only
class EstimateCostScenarioForBillingAccountResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> EstimateCostScenarioForBillingAccountResponse: ...

@typing.type_check_only
class EstimateCostScenarioWithListPriceResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> EstimateCostScenarioWithListPriceResponse: ...
