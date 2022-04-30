import collections.abc
import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

_list = list

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
                body: GoogleCloudBillingBudgetsV1Budget = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudBillingBudgetsV1BudgetHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleProtobufEmptyHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleCloudBillingBudgetsV1BudgetHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudBillingBudgetsV1ListBudgetsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: GoogleCloudBillingBudgetsV1ListBudgetsResponseHttpRequest,
                previous_response: GoogleCloudBillingBudgetsV1ListBudgetsResponse,
            ) -> GoogleCloudBillingBudgetsV1ListBudgetsResponseHttpRequest | None: ...
            def patch(
                self,
                *,
                name: str,
                body: GoogleCloudBillingBudgetsV1Budget = ...,
                updateMask: str = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudBillingBudgetsV1BudgetHttpRequest: ...

        def budgets(self) -> BudgetsResource: ...

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

@typing.type_check_only
class GoogleCloudBillingBudgetsV1BudgetHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudBillingBudgetsV1Budget: ...

@typing.type_check_only
class GoogleCloudBillingBudgetsV1ListBudgetsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudBillingBudgetsV1ListBudgetsResponse: ...

@typing.type_check_only
class GoogleProtobufEmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleProtobufEmpty: ...
