import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *
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
        def list(
            self, *, pageSize: int = ..., pageToken: str = ..., **kwargs: typing.Any
        ) -> ListServicesResponseHttpRequest: ...
        def skus(self) -> SkusResource: ...
    def billingAccounts(self) -> BillingAccountsResource: ...
    def projects(self) -> ProjectsResource: ...
    def services(self) -> ServicesResource: ...

@typing.type_check_only
class BillingAccountHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> BillingAccount: ...

@typing.type_check_only
class ListBillingAccountsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> ListBillingAccountsResponse: ...

@typing.type_check_only
class ListProjectBillingInfoResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> ListProjectBillingInfoResponse: ...

@typing.type_check_only
class ListServicesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> ListServicesResponse: ...

@typing.type_check_only
class ListSkusResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> ListSkusResponse: ...

@typing.type_check_only
class PolicyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> Policy: ...

@typing.type_check_only
class ProjectBillingInfoHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> ProjectBillingInfo: ...

@typing.type_check_only
class TestIamPermissionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> TestIamPermissionsResponse: ...
