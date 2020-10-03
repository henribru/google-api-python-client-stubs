import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class CloudOSLoginResource(googleapiclient.discovery.Resource):
    class UsersResource(googleapiclient.discovery.Resource):
        class ProjectsResource(googleapiclient.discovery.Resource):
            def delete(
                self,
                *,
                name: str,
                operatingSystemType: typing_extensions.Literal[
                    "OPERATING_SYSTEM_TYPE_UNSPECIFIED", "LINUX", "WINDOWS"
                ] = ...,
                **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
        class SshPublicKeysResource(googleapiclient.discovery.Resource):
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
                **kwargs: typing.Any
            ) -> SshPublicKeyHttpRequest: ...
        def importSshPublicKey(
            self,
            *,
            parent: str,
            body: SshPublicKey = ...,
            projectId: str = ...,
            **kwargs: typing.Any
        ) -> ImportSshPublicKeyResponseHttpRequest: ...
        def getLoginProfile(
            self,
            *,
            name: str,
            systemId: str = ...,
            projectId: str = ...,
            operatingSystemType: typing_extensions.Literal[
                "OPERATING_SYSTEM_TYPE_UNSPECIFIED", "LINUX", "WINDOWS"
            ] = ...,
            **kwargs: typing.Any
        ) -> LoginProfileHttpRequest: ...
        def projects(self) -> ProjectsResource: ...
        def sshPublicKeys(self) -> SshPublicKeysResource: ...
    def users(self) -> UsersResource: ...

class SshPublicKeyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> SshPublicKey: ...

class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Empty: ...

class LoginProfileHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> LoginProfile: ...

class ImportSshPublicKeyResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ImportSshPublicKeyResponse: ...
