import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class SecretManagerResource(googleapiclient.discovery.Resource):
    class ProjectsResource(googleapiclient.discovery.Resource):
        class LocationsResource(googleapiclient.discovery.Resource):
            def list(
                self,
                *,
                name: str,
                pageToken: str = ...,
                filter: str = ...,
                pageSize: int = ...,
                **kwargs: typing.Any
            ) -> ListLocationsResponseHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> LocationHttpRequest: ...
        class SecretsResource(googleapiclient.discovery.Resource):
            class VersionsResource(googleapiclient.discovery.Resource):
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> ListSecretVersionsResponseHttpRequest: ...
                def disable(
                    self,
                    *,
                    name: str,
                    body: DisableSecretVersionRequest = ...,
                    **kwargs: typing.Any
                ) -> SecretVersionHttpRequest: ...
                def destroy(
                    self,
                    *,
                    name: str,
                    body: DestroySecretVersionRequest = ...,
                    **kwargs: typing.Any
                ) -> SecretVersionHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> SecretVersionHttpRequest: ...
                def access(
                    self, *, name: str, **kwargs: typing.Any
                ) -> AccessSecretVersionResponseHttpRequest: ...
                def enable(
                    self,
                    *,
                    name: str,
                    body: EnableSecretVersionRequest = ...,
                    **kwargs: typing.Any
                ) -> SecretVersionHttpRequest: ...
            def getIamPolicy(
                self,
                *,
                resource: str,
                options_requestedPolicyVersion: int = ...,
                **kwargs: typing.Any
            ) -> PolicyHttpRequest: ...
            def patch(
                self,
                *,
                name: str,
                body: Secret = ...,
                updateMask: str = ...,
                **kwargs: typing.Any
            ) -> SecretHttpRequest: ...
            def get(self, *, name: str, **kwargs: typing.Any) -> SecretHttpRequest: ...
            def testIamPermissions(
                self,
                *,
                resource: str,
                body: TestIamPermissionsRequest = ...,
                **kwargs: typing.Any
            ) -> TestIamPermissionsResponseHttpRequest: ...
            def setIamPolicy(
                self,
                *,
                resource: str,
                body: SetIamPolicyRequest = ...,
                **kwargs: typing.Any
            ) -> PolicyHttpRequest: ...
            def create(
                self,
                *,
                parent: str,
                body: Secret = ...,
                secretId: str = ...,
                **kwargs: typing.Any
            ) -> SecretHttpRequest: ...
            def addVersion(
                self,
                *,
                parent: str,
                body: AddSecretVersionRequest = ...,
                **kwargs: typing.Any
            ) -> SecretVersionHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageToken: str = ...,
                pageSize: int = ...,
                **kwargs: typing.Any
            ) -> ListSecretsResponseHttpRequest: ...
            def versions(self) -> VersionsResource: ...
        def locations(self) -> LocationsResource: ...
        def secrets(self) -> SecretsResource: ...
    def projects(self) -> ProjectsResource: ...

class ListSecretsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListSecretsResponse: ...

class ListLocationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListLocationsResponse: ...

class ListSecretVersionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListSecretVersionsResponse: ...

class SecretHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Secret: ...

class SecretVersionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> SecretVersion: ...

class AccessSecretVersionResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> AccessSecretVersionResponse: ...

class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Empty: ...

class LocationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Location: ...

class TestIamPermissionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> TestIamPermissionsResponse: ...

class PolicyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Policy: ...
