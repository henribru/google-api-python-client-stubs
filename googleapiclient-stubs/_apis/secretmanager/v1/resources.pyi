import collections.abc
import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

_list = list

@typing.type_check_only
class SecretManagerResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class ProjectsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class LocationsResource(googleapiclient.discovery.Resource):
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> LocationHttpRequest: ...
            def list(
                self,
                *,
                name: str,
                filter: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> ListLocationsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListLocationsResponseHttpRequest,
                previous_response: ListLocationsResponse,
            ) -> ListLocationsResponseHttpRequest | None: ...

        @typing.type_check_only
        class SecretsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class VersionsResource(googleapiclient.discovery.Resource):
                def access(
                    self, *, name: str, **kwargs: typing.Any
                ) -> AccessSecretVersionResponseHttpRequest: ...
                def destroy(
                    self,
                    *,
                    name: str,
                    body: DestroySecretVersionRequest = ...,
                    **kwargs: typing.Any
                ) -> SecretVersionHttpRequest: ...
                def disable(
                    self,
                    *,
                    name: str,
                    body: DisableSecretVersionRequest = ...,
                    **kwargs: typing.Any
                ) -> SecretVersionHttpRequest: ...
                def enable(
                    self,
                    *,
                    name: str,
                    body: EnableSecretVersionRequest = ...,
                    **kwargs: typing.Any
                ) -> SecretVersionHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> SecretVersionHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> ListSecretVersionsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListSecretVersionsResponseHttpRequest,
                    previous_response: ListSecretVersionsResponse,
                ) -> ListSecretVersionsResponseHttpRequest | None: ...

            def addVersion(
                self,
                *,
                parent: str,
                body: AddSecretVersionRequest = ...,
                **kwargs: typing.Any
            ) -> SecretVersionHttpRequest: ...
            def create(
                self,
                *,
                parent: str,
                body: Secret = ...,
                secretId: str = ...,
                **kwargs: typing.Any
            ) -> SecretHttpRequest: ...
            def delete(
                self, *, name: str, etag: str = ..., **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def get(self, *, name: str, **kwargs: typing.Any) -> SecretHttpRequest: ...
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
                parent: str,
                filter: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> ListSecretsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListSecretsResponseHttpRequest,
                previous_response: ListSecretsResponse,
            ) -> ListSecretsResponseHttpRequest | None: ...
            def patch(
                self,
                *,
                name: str,
                body: Secret = ...,
                updateMask: str = ...,
                **kwargs: typing.Any
            ) -> SecretHttpRequest: ...
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
            def versions(self) -> VersionsResource: ...

        def locations(self) -> LocationsResource: ...
        def secrets(self) -> SecretsResource: ...

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
    def projects(self) -> ProjectsResource: ...

@typing.type_check_only
class AccessSecretVersionResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> AccessSecretVersionResponse: ...

@typing.type_check_only
class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Empty: ...

@typing.type_check_only
class ListLocationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListLocationsResponse: ...

@typing.type_check_only
class ListSecretVersionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListSecretVersionsResponse: ...

@typing.type_check_only
class ListSecretsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListSecretsResponse: ...

@typing.type_check_only
class LocationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Location: ...

@typing.type_check_only
class PolicyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Policy: ...

@typing.type_check_only
class SecretHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Secret: ...

@typing.type_check_only
class SecretVersionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> SecretVersion: ...

@typing.type_check_only
class TestIamPermissionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> TestIamPermissionsResponse: ...
