import collections.abc
import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

_list = list

@typing.type_check_only
class AdExchangeBuyerResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class AccountsResource(googleapiclient.discovery.Resource):
        def get(self, *, id: int, **kwargs: typing.Any) -> AccountHttpRequest: ...
        def list(self, **kwargs: typing.Any) -> AccountsListHttpRequest: ...
        def patch(
            self, *, id: int, body: Account = ..., **kwargs: typing.Any
        ) -> AccountHttpRequest: ...
        def update(
            self, *, id: int, body: Account = ..., **kwargs: typing.Any
        ) -> AccountHttpRequest: ...

    @typing.type_check_only
    class BillingInfoResource(googleapiclient.discovery.Resource):
        def get(
            self, *, accountId: int, **kwargs: typing.Any
        ) -> BillingInfoHttpRequest: ...
        def list(self, **kwargs: typing.Any) -> BillingInfoListHttpRequest: ...

    @typing.type_check_only
    class BudgetResource(googleapiclient.discovery.Resource):
        def get(
            self, *, accountId: str, billingId: str, **kwargs: typing.Any
        ) -> BudgetHttpRequest: ...
        def patch(
            self,
            *,
            accountId: str,
            billingId: str,
            body: Budget = ...,
            **kwargs: typing.Any
        ) -> BudgetHttpRequest: ...
        def update(
            self,
            *,
            accountId: str,
            billingId: str,
            body: Budget = ...,
            **kwargs: typing.Any
        ) -> BudgetHttpRequest: ...

    @typing.type_check_only
    class CreativesResource(googleapiclient.discovery.Resource):
        def get(
            self, *, accountId: int, buyerCreativeId: str, **kwargs: typing.Any
        ) -> CreativeHttpRequest: ...
        def insert(
            self, *, body: Creative = ..., **kwargs: typing.Any
        ) -> CreativeHttpRequest: ...
        def list(
            self,
            *,
            accountId: int | _list[int] = ...,
            buyerCreativeId: str | _list[str] = ...,
            maxResults: int = ...,
            pageToken: str = ...,
            statusFilter: typing_extensions.Literal[
                "approved", "disapproved", "not_checked"
            ] = ...,
            **kwargs: typing.Any
        ) -> CreativesListHttpRequest: ...
        def list_next(
            self,
            previous_request: CreativesListHttpRequest,
            previous_response: CreativesList,
        ) -> CreativesListHttpRequest | None: ...

    @typing.type_check_only
    class DirectDealsResource(googleapiclient.discovery.Resource):
        def get(self, *, id: str, **kwargs: typing.Any) -> DirectDealHttpRequest: ...
        def list(self, **kwargs: typing.Any) -> DirectDealsListHttpRequest: ...

    @typing.type_check_only
    class PerformanceReportResource(googleapiclient.discovery.Resource):
        def list(
            self,
            *,
            accountId: str,
            endDateTime: str,
            startDateTime: str,
            maxResults: int = ...,
            pageToken: str = ...,
            **kwargs: typing.Any
        ) -> PerformanceReportListHttpRequest: ...

    @typing.type_check_only
    class PretargetingConfigResource(googleapiclient.discovery.Resource):
        def delete(
            self, *, accountId: str, configId: str, **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def get(
            self, *, accountId: str, configId: str, **kwargs: typing.Any
        ) -> PretargetingConfigHttpRequest: ...
        def insert(
            self,
            *,
            accountId: str,
            body: PretargetingConfig = ...,
            **kwargs: typing.Any
        ) -> PretargetingConfigHttpRequest: ...
        def list(
            self, *, accountId: str, **kwargs: typing.Any
        ) -> PretargetingConfigListHttpRequest: ...
        def patch(
            self,
            *,
            accountId: str,
            configId: str,
            body: PretargetingConfig = ...,
            **kwargs: typing.Any
        ) -> PretargetingConfigHttpRequest: ...
        def update(
            self,
            *,
            accountId: str,
            configId: str,
            body: PretargetingConfig = ...,
            **kwargs: typing.Any
        ) -> PretargetingConfigHttpRequest: ...

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
    def billingInfo(self) -> BillingInfoResource: ...
    def budget(self) -> BudgetResource: ...
    def creatives(self) -> CreativesResource: ...
    def directDeals(self) -> DirectDealsResource: ...
    def performanceReport(self) -> PerformanceReportResource: ...
    def pretargetingConfig(self) -> PretargetingConfigResource: ...

@typing.type_check_only
class AccountHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Account: ...

@typing.type_check_only
class AccountsListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> AccountsList: ...

@typing.type_check_only
class BillingInfoHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> BillingInfo: ...

@typing.type_check_only
class BillingInfoListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> BillingInfoList: ...

@typing.type_check_only
class BudgetHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Budget: ...

@typing.type_check_only
class CreativeHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Creative: ...

@typing.type_check_only
class CreativesListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> CreativesList: ...

@typing.type_check_only
class DirectDealHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> DirectDeal: ...

@typing.type_check_only
class DirectDealsListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> DirectDealsList: ...

@typing.type_check_only
class PerformanceReportListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> PerformanceReportList: ...

@typing.type_check_only
class PretargetingConfigHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> PretargetingConfig: ...

@typing.type_check_only
class PretargetingConfigListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> PretargetingConfigList: ...
