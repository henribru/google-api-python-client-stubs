import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *
@typing.type_check_only
class CloudBillingBudgetResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class BillingAccountsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class BudgetsResource(googleapiclient.discovery.Resource):
            def create(
                self,
                *,
                parent: str,
                body: GoogleCloudBillingBudgetsV1beta1CreateBudgetRequest = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudBillingBudgetsV1beta1BudgetHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleProtobufEmptyHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleCloudBillingBudgetsV1beta1BudgetHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudBillingBudgetsV1beta1ListBudgetsResponseHttpRequest: ...
            def patch(
                self,
                *,
                name: str,
                body: GoogleCloudBillingBudgetsV1beta1UpdateBudgetRequest = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudBillingBudgetsV1beta1BudgetHttpRequest: ...
        def budgets(self) -> BudgetsResource: ...
    def billingAccounts(self) -> BillingAccountsResource: ...

@typing.type_check_only
class GoogleCloudBillingBudgetsV1beta1BudgetHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleCloudBillingBudgetsV1beta1Budget: ...

@typing.type_check_only
class GoogleCloudBillingBudgetsV1beta1ListBudgetsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleCloudBillingBudgetsV1beta1ListBudgetsResponse: ...

@typing.type_check_only
class GoogleProtobufEmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleProtobufEmpty: ...
