import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class CloudIAPResource(googleapiclient.discovery.Resource):
    class ProjectsResource(googleapiclient.discovery.Resource):
        class BrandsResource(googleapiclient.discovery.Resource):
            class IdentityAwareProxyClientsResource(googleapiclient.discovery.Resource):
                def resetSecret(
                    self,
                    *,
                    name: str,
                    body: ResetIdentityAwareProxyClientSecretRequest = ...,
                    **kwargs: typing.Any
                ) -> IdentityAwareProxyClientHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> IdentityAwareProxyClientHttpRequest: ...
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
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> ListIdentityAwareProxyClientsResponseHttpRequest: ...
            def create(
                self, *, parent: str, body: Brand = ..., **kwargs: typing.Any
            ) -> BrandHttpRequest: ...
            def list(
                self, *, parent: str, **kwargs: typing.Any
            ) -> ListBrandsResponseHttpRequest: ...
            def get(self, *, name: str, **kwargs: typing.Any) -> BrandHttpRequest: ...
            def identityAwareProxyClients(
                self,
            ) -> IdentityAwareProxyClientsResource: ...
        def brands(self) -> BrandsResource: ...
    class V1Resource(googleapiclient.discovery.Resource):
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
        def getIamPolicy(
            self,
            *,
            resource: str,
            body: GetIamPolicyRequest = ...,
            **kwargs: typing.Any
        ) -> PolicyHttpRequest: ...
    def projects(self) -> ProjectsResource: ...
    def v1(self) -> V1Resource: ...

class ListIdentityAwareProxyClientsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListIdentityAwareProxyClientsResponse: ...

class BrandHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Brand: ...

class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Empty: ...

class PolicyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Policy: ...

class IapSettingsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> IapSettings: ...

class ListBrandsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListBrandsResponse: ...

class IdentityAwareProxyClientHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> IdentityAwareProxyClient: ...

class TestIamPermissionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> TestIamPermissionsResponse: ...
