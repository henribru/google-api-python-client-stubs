import collections.abc
import typing

import httplib2
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http

from .schemas import *

_list = list

@typing.type_check_only
class CloudOSLoginResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class UsersResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class ProjectsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class LocationsResource(googleapiclient.discovery.Resource):
                def signSshPublicKey(
                    self,
                    *,
                    parent: str,
                    body: SignSshPublicKeyRequest = ...,
                    **kwargs: typing.Any,
                ) -> SignSshPublicKeyResponseHttpRequest: ...

            @typing.type_check_only
            class ZonesResource(googleapiclient.discovery.Resource):
                def signSshPublicKey(
                    self,
                    *,
                    parent: str,
                    body: SignSshPublicKeyRequest = ...,
                    **kwargs: typing.Any,
                ) -> SignSshPublicKeyResponseHttpRequest: ...

            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def locations(self) -> LocationsResource: ...
            def zones(self) -> ZonesResource: ...

        @typing.type_check_only
        class SshPublicKeysResource(googleapiclient.discovery.Resource):
            def create(
                self, *, parent: str, body: SshPublicKey = ..., **kwargs: typing.Any
            ) -> SshPublicKeyHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> SshPublicKeyHttpRequest: ...
            def patch(
                self,
                *,
                name: str,
                body: SshPublicKey = ...,
                updateMask: str = ...,
                **kwargs: typing.Any,
            ) -> SshPublicKeyHttpRequest: ...

        def getLoginProfile(
            self,
            *,
            name: str,
            projectId: str = ...,
            systemId: str = ...,
            view: typing_extensions.Literal[
                "LOGIN_PROFILE_VIEW_UNSPECIFIED", "BASIC", "SECURITY_KEY"
            ] = ...,
            **kwargs: typing.Any,
        ) -> LoginProfileHttpRequest: ...
        def importSshPublicKey(
            self,
            *,
            parent: str,
            body: SshPublicKey = ...,
            projectId: str = ...,
            regions: str | _list[str] = ...,
            view: typing_extensions.Literal[
                "LOGIN_PROFILE_VIEW_UNSPECIFIED", "BASIC", "SECURITY_KEY"
            ] = ...,
            **kwargs: typing.Any,
        ) -> ImportSshPublicKeyResponseHttpRequest: ...
        def projects(self) -> ProjectsResource: ...
        def sshPublicKeys(self) -> SshPublicKeysResource: ...

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
        | None = None,
    ) -> googleapiclient.http.BatchHttpRequest: ...
    def users(self) -> UsersResource: ...

@typing.type_check_only
class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Empty: ...

@typing.type_check_only
class ImportSshPublicKeyResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ImportSshPublicKeyResponse: ...

@typing.type_check_only
class LoginProfileHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> LoginProfile: ...

@typing.type_check_only
class SignSshPublicKeyResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> SignSshPublicKeyResponse: ...

@typing.type_check_only
class SshPublicKeyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> SshPublicKey: ...
