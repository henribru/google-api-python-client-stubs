import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class CloudBillingBudgetResource(googleapiclient.discovery.Resource):
    class BillingAccountsResource(googleapiclient.discovery.Resource):
        class BudgetsResource(googleapiclient.discovery.Resource):
            def create(
                self,
                *,
                parent: str,
                body: GoogleCloudBillingBudgetsV1beta1CreateBudgetRequest = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudBillingBudgetsV1beta1BudgetHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudBillingBudgetsV1beta1ListBudgetsResponseHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleProtobufEmptyHttpRequest: ...
            def patch(
                self,
                *,
                name: str,
                body: GoogleCloudBillingBudgetsV1beta1UpdateBudgetRequest = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudBillingBudgetsV1beta1BudgetHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleCloudBillingBudgetsV1beta1BudgetHttpRequest: ...
        def budgets(self) -> BudgetsResource: ...
    def billingAccounts(self) -> BillingAccountsResource: ...

class GoogleCloudBillingBudgetsV1beta1ListBudgetsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudBillingBudgetsV1beta1ListBudgetsResponse: ...

class GoogleCloudBillingBudgetsV1beta1BudgetHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudBillingBudgetsV1beta1Budget: ...

class GoogleProtobufEmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleProtobufEmpty: ...
