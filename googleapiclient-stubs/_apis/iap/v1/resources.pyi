import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *
@typing.type_check_only
class CloudIAPResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class ProjectsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class BrandsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class IdentityAwareProxyClientsResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: IdentityAwareProxyClient = ...,
                    **kwargs: typing.Any
                ) -> IdentityAwareProxyClientHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> IdentityAwareProxyClientHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> ListIdentityAwareProxyClientsResponseHttpRequest: ...
                def resetSecret(
                    self,
                    *,
                    name: str,
                    body: ResetIdentityAwareProxyClientSecretRequest = ...,
                    **kwargs: typing.Any
                ) -> IdentityAwareProxyClientHttpRequest: ...
            def create(
                self, *, parent: str, body: Brand = ..., **kwargs: typing.Any
            ) -> BrandHttpRequest: ...
            def get(self, *, name: str, **kwargs: typing.Any) -> BrandHttpRequest: ...
            def list(
                self, *, parent: str, **kwargs: typing.Any
            ) -> ListBrandsResponseHttpRequest: ...
            def identityAwareProxyClients(
                self,
            ) -> IdentityAwareProxyClientsResource: ...
        def brands(self) -> BrandsResource: ...
    @typing.type_check_only
    class V1Resource(googleapiclient.discovery.Resource):
        def getIamPolicy(
            self,
            *,
            resource: str,
            body: GetIamPolicyRequest = ...,
            **kwargs: typing.Any
        ) -> PolicyHttpRequest: ...
        def getIapSettings(
            self, *, name: str, **kwargs: typing.Any
        ) -> IapSettingsHttpRequest: ...
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
        def updateIapSettings(
            self,
            *,
            name: str,
            body: IapSettings = ...,
            updateMask: str = ...,
            **kwargs: typing.Any
        ) -> IapSettingsHttpRequest: ...
    def projects(self) -> ProjectsResource: ...
    def v1(self) -> V1Resource: ...

@typing.type_check_only
class BrandHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> Brand: ...

@typing.type_check_only
class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> Empty: ...

@typing.type_check_only
class IapSettingsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> IapSettings: ...

@typing.type_check_only
class IdentityAwareProxyClientHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> IdentityAwareProxyClient: ...

@typing.type_check_only
class ListBrandsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> ListBrandsResponse: ...

@typing.type_check_only
class ListIdentityAwareProxyClientsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> ListIdentityAwareProxyClientsResponse: ...

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
class TestIamPermissionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> TestIamPermissionsResponse: ...
