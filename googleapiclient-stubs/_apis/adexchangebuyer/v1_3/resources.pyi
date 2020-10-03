import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class AdExchangeBuyerResource(googleapiclient.discovery.Resource):
    class AccountsResource(googleapiclient.discovery.Resource):
        def get(self, *, id: int, **kwargs: typing.Any) -> AccountHttpRequest: ...
        def list(self, **kwargs: typing.Any) -> AccountsListHttpRequest: ...
        def patch(
            self, *, id: int, body: Account = ..., **kwargs: typing.Any
        ) -> AccountHttpRequest: ...
        def update(
            self, *, id: int, body: Account = ..., **kwargs: typing.Any
        ) -> AccountHttpRequest: ...
    class BillingInfoResource(googleapiclient.discovery.Resource):
        def get(
            self, *, accountId: int, **kwargs: typing.Any
        ) -> BillingInfoHttpRequest: ...
        def list(self, **kwargs: typing.Any) -> BillingInfoListHttpRequest: ...
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
            accountId: typing.Union[int, typing.List[int]] = ...,
            buyerCreativeId: typing.Union[str, typing.List[str]] = ...,
            maxResults: int = ...,
            pageToken: str = ...,
            statusFilter: typing_extensions.Literal[
                "approved", "disapproved", "not_checked"
            ] = ...,
            **kwargs: typing.Any
        ) -> CreativesListHttpRequest: ...
    class DirectDealsResource(googleapiclient.discovery.Resource):
        def get(self, *, id: str, **kwargs: typing.Any) -> DirectDealHttpRequest: ...
        def list(self, **kwargs: typing.Any) -> DirectDealsListHttpRequest: ...
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
    def accounts(self) -> AccountsResource: ...
    def billingInfo(self) -> BillingInfoResource: ...
    def budget(self) -> BudgetResource: ...
    def creatives(self) -> CreativesResource: ...
    def directDeals(self) -> DirectDealsResource: ...
    def performanceReport(self) -> PerformanceReportResource: ...
    def pretargetingConfig(self) -> PretargetingConfigResource: ...

class PerformanceReportListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> PerformanceReportList: ...

class AccountsListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> AccountsList: ...

class PretargetingConfigListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> PretargetingConfigList: ...

class BillingInfoListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> BillingInfoList: ...

class CreativeHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Creative: ...

class PretargetingConfigHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> PretargetingConfig: ...

class BudgetHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Budget: ...

class AccountHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Account: ...

class BillingInfoHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> BillingInfo: ...

class DirectDealHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> DirectDeal: ...

class CreativesListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> CreativesList: ...

class DirectDealsListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> DirectDealsList: ...
