import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class CloudbillingResource(googleapiclient.discovery.Resource):
    class ProjectsResource(googleapiclient.discovery.Resource):
        def getBillingInfo(
            self, *, name: str, **kwargs: typing.Any
        ) -> ProjectBillingInfoHttpRequest: ...
        def updateBillingInfo(
            self, *, name: str, body: ProjectBillingInfo = ..., **kwargs: typing.Any
        ) -> ProjectBillingInfoHttpRequest: ...
    class ServicesResource(googleapiclient.discovery.Resource):
        class SkusResource(googleapiclient.discovery.Resource):
            def list(
                self,
                *,
                parent: str,
                currencyCode: str = ...,
                pageToken: str = ...,
                endTime: str = ...,
                startTime: str = ...,
                pageSize: int = ...,
                **kwargs: typing.Any
            ) -> ListSkusResponseHttpRequest: ...
        def list(
            self, *, pageToken: str = ..., pageSize: int = ..., **kwargs: typing.Any
        ) -> ListServicesResponseHttpRequest: ...
        def skus(self) -> SkusResource: ...
    class BillingAccountsResource(googleapiclient.discovery.Resource):
        class ProjectsResource(googleapiclient.discovery.Resource):
            def list(
                self,
                *,
                name: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> ListProjectBillingInfoResponseHttpRequest: ...
        def testIamPermissions(
            self,
            *,
            resource: str,
            body: TestIamPermissionsRequest = ...,
            **kwargs: typing.Any
        ) -> TestIamPermissionsResponseHttpRequest: ...
        def patch(
            self,
            *,
            name: str,
            body: BillingAccount = ...,
            updateMask: str = ...,
            **kwargs: typing.Any
        ) -> BillingAccountHttpRequest: ...
        def get(
            self, *, name: str, **kwargs: typing.Any
        ) -> BillingAccountHttpRequest: ...
        def list(
            self,
            *,
            filter: str = ...,
            pageToken: str = ...,
            pageSize: int = ...,
            **kwargs: typing.Any
        ) -> ListBillingAccountsResponseHttpRequest: ...
        def create(
            self, *, body: BillingAccount = ..., **kwargs: typing.Any
        ) -> BillingAccountHttpRequest: ...
        def setIamPolicy(
            self,
            *,
            resource: str,
            body: SetIamPolicyRequest = ...,
            **kwargs: typing.Any
        ) -> PolicyHttpRequest: ...
        def getIamPolicy(
            self,
            *,
            resource: str,
            options_requestedPolicyVersion: int = ...,
            **kwargs: typing.Any
        ) -> PolicyHttpRequest: ...
        def projects(self) -> ProjectsResource: ...
    def projects(self) -> ProjectsResource: ...
    def services(self) -> ServicesResource: ...
    def billingAccounts(self) -> BillingAccountsResource: ...

class ListServicesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListServicesResponse: ...

class ListSkusResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListSkusResponse: ...

class ListBillingAccountsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListBillingAccountsResponse: ...

class BillingAccountHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> BillingAccount: ...

class TestIamPermissionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> TestIamPermissionsResponse: ...

class PolicyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Policy: ...

class ProjectBillingInfoHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ProjectBillingInfo: ...

class ListProjectBillingInfoResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListProjectBillingInfoResponse: ...
