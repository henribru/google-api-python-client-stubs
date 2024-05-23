import collections.abc
import typing

import httplib2
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http

from .schemas import *

_list = list

@typing.type_check_only
class CloudbillingResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class BillingAccountsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class ServicesResource(googleapiclient.discovery.Resource):
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleCloudBillingBillingaccountservicesV1betaBillingAccountServiceHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any,
            ) -> GoogleCloudBillingBillingaccountservicesV1betaListBillingAccountServicesResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: GoogleCloudBillingBillingaccountservicesV1betaListBillingAccountServicesResponseHttpRequest,
                previous_response: GoogleCloudBillingBillingaccountservicesV1betaListBillingAccountServicesResponse,
            ) -> (
                GoogleCloudBillingBillingaccountservicesV1betaListBillingAccountServicesResponseHttpRequest
                | None
            ): ...

        @typing.type_check_only
        class SkuGroupsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class SkusResource(googleapiclient.discovery.Resource):
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudBillingBillingaccountskugroupskusV1betaBillingAccountSkuGroupSkuHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudBillingBillingaccountskugroupskusV1betaListBillingAccountSkuGroupSkusResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudBillingBillingaccountskugroupskusV1betaListBillingAccountSkuGroupSkusResponseHttpRequest,
                    previous_response: GoogleCloudBillingBillingaccountskugroupskusV1betaListBillingAccountSkuGroupSkusResponse,
                ) -> (
                    GoogleCloudBillingBillingaccountskugroupskusV1betaListBillingAccountSkuGroupSkusResponseHttpRequest
                    | None
                ): ...

            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleCloudBillingBillingaccountskugroupsV1betaBillingAccountSkuGroupHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any,
            ) -> GoogleCloudBillingBillingaccountskugroupsV1betaListBillingAccountSkuGroupsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: GoogleCloudBillingBillingaccountskugroupsV1betaListBillingAccountSkuGroupsResponseHttpRequest,
                previous_response: GoogleCloudBillingBillingaccountskugroupsV1betaListBillingAccountSkuGroupsResponse,
            ) -> (
                GoogleCloudBillingBillingaccountskugroupsV1betaListBillingAccountSkuGroupsResponseHttpRequest
                | None
            ): ...
            def skus(self) -> SkusResource: ...

        @typing.type_check_only
        class SkusResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class PriceResource(googleapiclient.discovery.Resource):
                def get(
                    self, *, name: str, currencyCode: str = ..., **kwargs: typing.Any
                ) -> GoogleCloudBillingBillingaccountpricesV1betaBillingAccountPriceHttpRequest: ...

            @typing.type_check_only
            class PricesResource(googleapiclient.discovery.Resource):
                def list(
                    self,
                    *,
                    parent: str,
                    currencyCode: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudBillingBillingaccountpricesV1betaListBillingAccountPricesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudBillingBillingaccountpricesV1betaListBillingAccountPricesResponseHttpRequest,
                    previous_response: GoogleCloudBillingBillingaccountpricesV1betaListBillingAccountPricesResponse,
                ) -> (
                    GoogleCloudBillingBillingaccountpricesV1betaListBillingAccountPricesResponseHttpRequest
                    | None
                ): ...

            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> (
                GoogleCloudBillingBillingaccountskusV1betaBillingAccountSkuHttpRequest
            ): ...
            def list(
                self,
                *,
                parent: str,
                filter: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any,
            ) -> GoogleCloudBillingBillingaccountskusV1betaListBillingAccountSkusResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: GoogleCloudBillingBillingaccountskusV1betaListBillingAccountSkusResponseHttpRequest,
                previous_response: GoogleCloudBillingBillingaccountskusV1betaListBillingAccountSkusResponse,
            ) -> (
                GoogleCloudBillingBillingaccountskusV1betaListBillingAccountSkusResponseHttpRequest
                | None
            ): ...
            def price(self) -> PriceResource: ...
            def prices(self) -> PricesResource: ...

        def estimateCostScenario(
            self,
            *,
            billingAccount: str,
            body: EstimateCostScenarioForBillingAccountRequest = ...,
            **kwargs: typing.Any,
        ) -> EstimateCostScenarioForBillingAccountResponseHttpRequest: ...
        def services(self) -> ServicesResource: ...
        def skuGroups(self) -> SkuGroupsResource: ...
        def skus(self) -> SkusResource: ...

    @typing.type_check_only
    class SkuGroupsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class SkusResource(googleapiclient.discovery.Resource):
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleCloudBillingSkugroupskusV1betaSkuGroupSkuHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any,
            ) -> (
                GoogleCloudBillingSkugroupskusV1betaListSkuGroupSkusResponseHttpRequest
            ): ...
            def list_next(
                self,
                previous_request: GoogleCloudBillingSkugroupskusV1betaListSkuGroupSkusResponseHttpRequest,
                previous_response: GoogleCloudBillingSkugroupskusV1betaListSkuGroupSkusResponse,
            ) -> (
                GoogleCloudBillingSkugroupskusV1betaListSkuGroupSkusResponseHttpRequest
                | None
            ): ...

        def get(
            self, *, name: str, **kwargs: typing.Any
        ) -> GoogleCloudBillingSkugroupsV1betaSkuGroupHttpRequest: ...
        def list(
            self, *, pageSize: int = ..., pageToken: str = ..., **kwargs: typing.Any
        ) -> GoogleCloudBillingSkugroupsV1betaListSkuGroupsResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: GoogleCloudBillingSkugroupsV1betaListSkuGroupsResponseHttpRequest,
            previous_response: GoogleCloudBillingSkugroupsV1betaListSkuGroupsResponse,
        ) -> (
            GoogleCloudBillingSkugroupsV1betaListSkuGroupsResponseHttpRequest | None
        ): ...
        def skus(self) -> SkusResource: ...

    @typing.type_check_only
    class SkusResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class PriceResource(googleapiclient.discovery.Resource):
            def get(
                self, *, name: str, currencyCode: str = ..., **kwargs: typing.Any
            ) -> GoogleCloudBillingPricesV1betaPriceHttpRequest: ...

        @typing.type_check_only
        class PricesResource(googleapiclient.discovery.Resource):
            def list(
                self,
                *,
                parent: str,
                currencyCode: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any,
            ) -> GoogleCloudBillingPricesV1betaListPricesResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: GoogleCloudBillingPricesV1betaListPricesResponseHttpRequest,
                previous_response: GoogleCloudBillingPricesV1betaListPricesResponse,
            ) -> GoogleCloudBillingPricesV1betaListPricesResponseHttpRequest | None: ...

        def price(self) -> PriceResource: ...
        def prices(self) -> PricesResource: ...

    @typing.type_check_only
    class V1betaResource(googleapiclient.discovery.Resource):
        def estimateCostScenario(
            self,
            *,
            body: EstimateCostScenarioWithListPriceRequest = ...,
            **kwargs: typing.Any,
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
        | None = None,
    ) -> googleapiclient.http.BatchHttpRequest: ...
    def billingAccounts(self) -> BillingAccountsResource: ...
    def skuGroups(self) -> SkuGroupsResource: ...
    def skus(self) -> SkusResource: ...
    def v1beta(self) -> V1betaResource: ...

@typing.type_check_only
class EstimateCostScenarioForBillingAccountResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> EstimateCostScenarioForBillingAccountResponse: ...

@typing.type_check_only
class EstimateCostScenarioWithListPriceResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> EstimateCostScenarioWithListPriceResponse: ...

@typing.type_check_only
class GoogleCloudBillingBillingaccountpricesV1betaBillingAccountPriceHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudBillingBillingaccountpricesV1betaBillingAccountPrice: ...

@typing.type_check_only
class GoogleCloudBillingBillingaccountpricesV1betaListBillingAccountPricesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> (
        GoogleCloudBillingBillingaccountpricesV1betaListBillingAccountPricesResponse
    ): ...

@typing.type_check_only
class GoogleCloudBillingBillingaccountservicesV1betaBillingAccountServiceHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudBillingBillingaccountservicesV1betaBillingAccountService: ...

@typing.type_check_only
class GoogleCloudBillingBillingaccountservicesV1betaListBillingAccountServicesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> (
        GoogleCloudBillingBillingaccountservicesV1betaListBillingAccountServicesResponse
    ): ...

@typing.type_check_only
class GoogleCloudBillingBillingaccountskugroupsV1betaBillingAccountSkuGroupHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudBillingBillingaccountskugroupsV1betaBillingAccountSkuGroup: ...

@typing.type_check_only
class GoogleCloudBillingBillingaccountskugroupsV1betaListBillingAccountSkuGroupsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudBillingBillingaccountskugroupsV1betaListBillingAccountSkuGroupsResponse: ...

@typing.type_check_only
class GoogleCloudBillingBillingaccountskugroupskusV1betaBillingAccountSkuGroupSkuHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> (
        GoogleCloudBillingBillingaccountskugroupskusV1betaBillingAccountSkuGroupSku
    ): ...

@typing.type_check_only
class GoogleCloudBillingBillingaccountskugroupskusV1betaListBillingAccountSkuGroupSkusResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudBillingBillingaccountskugroupskusV1betaListBillingAccountSkuGroupSkusResponse: ...

@typing.type_check_only
class GoogleCloudBillingBillingaccountskusV1betaBillingAccountSkuHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudBillingBillingaccountskusV1betaBillingAccountSku: ...

@typing.type_check_only
class GoogleCloudBillingBillingaccountskusV1betaListBillingAccountSkusResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudBillingBillingaccountskusV1betaListBillingAccountSkusResponse: ...

@typing.type_check_only
class GoogleCloudBillingPricesV1betaListPricesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudBillingPricesV1betaListPricesResponse: ...

@typing.type_check_only
class GoogleCloudBillingPricesV1betaPriceHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudBillingPricesV1betaPrice: ...

@typing.type_check_only
class GoogleCloudBillingSkugroupsV1betaListSkuGroupsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudBillingSkugroupsV1betaListSkuGroupsResponse: ...

@typing.type_check_only
class GoogleCloudBillingSkugroupsV1betaSkuGroupHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudBillingSkugroupsV1betaSkuGroup: ...

@typing.type_check_only
class GoogleCloudBillingSkugroupskusV1betaListSkuGroupSkusResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudBillingSkugroupskusV1betaListSkuGroupSkusResponse: ...

@typing.type_check_only
class GoogleCloudBillingSkugroupskusV1betaSkuGroupSkuHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudBillingSkugroupskusV1betaSkuGroupSku: ...
