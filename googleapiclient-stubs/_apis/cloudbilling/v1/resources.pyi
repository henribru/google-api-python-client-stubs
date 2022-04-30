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
        @typing.type_check_only
        class ProjectsResource(googleapiclient.discovery.Resource):
            def list(
                self,
                *,
                name: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> ListProjectBillingInfoResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListProjectBillingInfoResponseHttpRequest,
                previous_response: ListProjectBillingInfoResponse,
            ) -> ListProjectBillingInfoResponseHttpRequest | None: ...

        def create(
            self, *, body: BillingAccount = ..., **kwargs: typing.Any
        ) -> BillingAccountHttpRequest: ...
        def get(
            self, *, name: str, **kwargs: typing.Any
        ) -> BillingAccountHttpRequest: ...
        def getIamPolicy(
            self,
            *,
            resource: str,
            options_requestedPolicyVersion: int = ...,
            **kwargs: typing.Any
        ) -> PolicyHttpRequest: ...
        def list(
            self,
            *,
            filter: str = ...,
            pageSize: int = ...,
            pageToken: str = ...,
            **kwargs: typing.Any
        ) -> ListBillingAccountsResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: ListBillingAccountsResponseHttpRequest,
            previous_response: ListBillingAccountsResponse,
        ) -> ListBillingAccountsResponseHttpRequest | None: ...
        def patch(
            self,
            *,
            name: str,
            body: BillingAccount = ...,
            updateMask: str = ...,
            **kwargs: typing.Any
        ) -> BillingAccountHttpRequest: ...
        def setIamPolicy(
            self,
            *,
            resource: str,
            body: SetIamPolicyRequest = ...,
            **kwargs: typing.Any
        ) -> PolicyHttpRequest: ...
        def testIamPermissions(
            self,
            *,
            resource: str,
            body: TestIamPermissionsRequest = ...,
            **kwargs: typing.Any
        ) -> TestIamPermissionsResponseHttpRequest: ...
        def projects(self) -> ProjectsResource: ...

    @typing.type_check_only
    class ProjectsResource(googleapiclient.discovery.Resource):
        def getBillingInfo(
            self, *, name: str, **kwargs: typing.Any
        ) -> ProjectBillingInfoHttpRequest: ...
        def updateBillingInfo(
            self, *, name: str, body: ProjectBillingInfo = ..., **kwargs: typing.Any
        ) -> ProjectBillingInfoHttpRequest: ...

    @typing.type_check_only
    class ServicesResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class SkusResource(googleapiclient.discovery.Resource):
            def list(
                self,
                *,
                parent: str,
                currencyCode: str = ...,
                endTime: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                startTime: str = ...,
                **kwargs: typing.Any
            ) -> ListSkusResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListSkusResponseHttpRequest,
                previous_response: ListSkusResponse,
            ) -> ListSkusResponseHttpRequest | None: ...

        def list(
            self, *, pageSize: int = ..., pageToken: str = ..., **kwargs: typing.Any
        ) -> ListServicesResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: ListServicesResponseHttpRequest,
            previous_response: ListServicesResponse,
        ) -> ListServicesResponseHttpRequest | None: ...
        def skus(self) -> SkusResource: ...

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
    def projects(self) -> ProjectsResource: ...
    def services(self) -> ServicesResource: ...

@typing.type_check_only
class BillingAccountHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> BillingAccount: ...

@typing.type_check_only
class ListBillingAccountsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListBillingAccountsResponse: ...

@typing.type_check_only
class ListProjectBillingInfoResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListProjectBillingInfoResponse: ...

@typing.type_check_only
class ListServicesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListServicesResponse: ...

@typing.type_check_only
class ListSkusResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListSkusResponse: ...

@typing.type_check_only
class PolicyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Policy: ...

@typing.type_check_only
class ProjectBillingInfoHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ProjectBillingInfo: ...

@typing.type_check_only
class TestIamPermissionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> TestIamPermissionsResponse: ...
