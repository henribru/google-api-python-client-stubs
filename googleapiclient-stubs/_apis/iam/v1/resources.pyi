import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class IamResource(googleapiclient.discovery.Resource):
    class IamPoliciesResource(googleapiclient.discovery.Resource):
        def queryAuditableServices(
            self, *, body: QueryAuditableServicesRequest = ..., **kwargs: typing.Any
        ) -> QueryAuditableServicesResponseHttpRequest: ...
        def lintPolicy(
            self, *, body: LintPolicyRequest = ..., **kwargs: typing.Any
        ) -> LintPolicyResponseHttpRequest: ...
    class ProjectsResource(googleapiclient.discovery.Resource):
        class RolesResource(googleapiclient.discovery.Resource):
            def create(
                self,
                *,
                parent: str,
                body: CreateRoleRequest = ...,
                **kwargs: typing.Any
            ) -> RoleHttpRequest: ...
            def undelete(
                self,
                *,
                name: str,
                body: UndeleteRoleRequest = ...,
                **kwargs: typing.Any
            ) -> RoleHttpRequest: ...
            def delete(
                self, *, name: str, etag: str = ..., **kwargs: typing.Any
            ) -> RoleHttpRequest: ...
            def get(self, *, name: str, **kwargs: typing.Any) -> RoleHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                view: typing_extensions.Literal["BASIC", "FULL"] = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                showDeleted: bool = ...,
                **kwargs: typing.Any
            ) -> ListRolesResponseHttpRequest: ...
            def patch(
                self,
                *,
                name: str,
                body: Role = ...,
                updateMask: str = ...,
                **kwargs: typing.Any
            ) -> RoleHttpRequest: ...
        class ServiceAccountsResource(googleapiclient.discovery.Resource):
            class KeysResource(googleapiclient.discovery.Resource):
                def get(
                    self,
                    *,
                    name: str,
                    publicKeyType: typing_extensions.Literal[
                        "TYPE_NONE", "TYPE_X509_PEM_FILE", "TYPE_RAW_PUBLIC_KEY"
                    ] = ...,
                    **kwargs: typing.Any
                ) -> ServiceAccountKeyHttpRequest: ...
                def create(
                    self,
                    *,
                    name: str,
                    body: CreateServiceAccountKeyRequest = ...,
                    **kwargs: typing.Any
                ) -> ServiceAccountKeyHttpRequest: ...
                def upload(
                    self,
                    *,
                    name: str,
                    body: UploadServiceAccountKeyRequest = ...,
                    **kwargs: typing.Any
                ) -> ServiceAccountKeyHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def list(
                    self,
                    *,
                    name: str,
                    keyTypes: typing.Union[
                        typing_extensions.Literal[
                            "KEY_TYPE_UNSPECIFIED", "USER_MANAGED", "SYSTEM_MANAGED"
                        ],
                        typing.List[
                            typing_extensions.Literal[
                                "KEY_TYPE_UNSPECIFIED", "USER_MANAGED", "SYSTEM_MANAGED"
                            ]
                        ],
                    ] = ...,
                    **kwargs: typing.Any
                ) -> ListServiceAccountKeysResponseHttpRequest: ...
            def create(
                self,
                *,
                name: str,
                body: CreateServiceAccountRequest = ...,
                **kwargs: typing.Any
            ) -> ServiceAccountHttpRequest: ...
            def testIamPermissions(
                self,
                *,
                resource: str,
                body: TestIamPermissionsRequest = ...,
                **kwargs: typing.Any
            ) -> TestIamPermissionsResponseHttpRequest: ...
            def disable(
                self,
                *,
                name: str,
                body: DisableServiceAccountRequest = ...,
                **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def undelete(
                self,
                *,
                name: str,
                body: UndeleteServiceAccountRequest = ...,
                **kwargs: typing.Any
            ) -> UndeleteServiceAccountResponseHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> ServiceAccountHttpRequest: ...
            def signJwt(
                self, *, name: str, body: SignJwtRequest = ..., **kwargs: typing.Any
            ) -> SignJwtResponseHttpRequest: ...
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
                body: PatchServiceAccountRequest = ...,
                **kwargs: typing.Any
            ) -> ServiceAccountHttpRequest: ...
            def list(
                self,
                *,
                name: str,
                pageToken: str = ...,
                pageSize: int = ...,
                **kwargs: typing.Any
            ) -> ListServiceAccountsResponseHttpRequest: ...
            def enable(
                self,
                *,
                name: str,
                body: EnableServiceAccountRequest = ...,
                **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def update(
                self, *, name: str, body: ServiceAccount = ..., **kwargs: typing.Any
            ) -> ServiceAccountHttpRequest: ...
            def signBlob(
                self, *, name: str, body: SignBlobRequest = ..., **kwargs: typing.Any
            ) -> SignBlobResponseHttpRequest: ...
            def setIamPolicy(
                self,
                *,
                resource: str,
                body: SetIamPolicyRequest = ...,
                **kwargs: typing.Any
            ) -> PolicyHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def keys(self) -> KeysResource: ...
        def roles(self) -> RolesResource: ...
        def serviceAccounts(self) -> ServiceAccountsResource: ...
    class OrganizationsResource(googleapiclient.discovery.Resource):
        class RolesResource(googleapiclient.discovery.Resource):
            def delete(
                self, *, name: str, etag: str = ..., **kwargs: typing.Any
            ) -> RoleHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                view: typing_extensions.Literal["BASIC", "FULL"] = ...,
                showDeleted: bool = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> ListRolesResponseHttpRequest: ...
            def undelete(
                self,
                *,
                name: str,
                body: UndeleteRoleRequest = ...,
                **kwargs: typing.Any
            ) -> RoleHttpRequest: ...
            def get(self, *, name: str, **kwargs: typing.Any) -> RoleHttpRequest: ...
            def patch(
                self,
                *,
                name: str,
                body: Role = ...,
                updateMask: str = ...,
                **kwargs: typing.Any
            ) -> RoleHttpRequest: ...
            def create(
                self,
                *,
                parent: str,
                body: CreateRoleRequest = ...,
                **kwargs: typing.Any
            ) -> RoleHttpRequest: ...
        def roles(self) -> RolesResource: ...
    class RolesResource(googleapiclient.discovery.Resource):
        def list(
            self,
            *,
            pageToken: str = ...,
            parent: str = ...,
            view: typing_extensions.Literal["BASIC", "FULL"] = ...,
            pageSize: int = ...,
            showDeleted: bool = ...,
            **kwargs: typing.Any
        ) -> ListRolesResponseHttpRequest: ...
        def queryGrantableRoles(
            self, *, body: QueryGrantableRolesRequest = ..., **kwargs: typing.Any
        ) -> QueryGrantableRolesResponseHttpRequest: ...
        def get(self, *, name: str, **kwargs: typing.Any) -> RoleHttpRequest: ...
    class PermissionsResource(googleapiclient.discovery.Resource):
        def queryTestablePermissions(
            self, *, body: QueryTestablePermissionsRequest = ..., **kwargs: typing.Any
        ) -> QueryTestablePermissionsResponseHttpRequest: ...
    def iamPolicies(self) -> IamPoliciesResource: ...
    def projects(self) -> ProjectsResource: ...
    def organizations(self) -> OrganizationsResource: ...
    def roles(self) -> RolesResource: ...
    def permissions(self) -> PermissionsResource: ...

class QueryGrantableRolesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> QueryGrantableRolesResponse: ...

class LintPolicyResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> LintPolicyResponse: ...

class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Empty: ...

class RoleHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Role: ...

class ServiceAccountHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ServiceAccount: ...

class ListRolesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListRolesResponse: ...

class QueryAuditableServicesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> QueryAuditableServicesResponse: ...

class TestIamPermissionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> TestIamPermissionsResponse: ...

class ServiceAccountKeyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ServiceAccountKey: ...

class SignJwtResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> SignJwtResponse: ...

class ListServiceAccountKeysResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListServiceAccountKeysResponse: ...

class PolicyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Policy: ...

class ListServiceAccountsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListServiceAccountsResponse: ...

class QueryTestablePermissionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> QueryTestablePermissionsResponse: ...

class SignBlobResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> SignBlobResponse: ...

class UndeleteServiceAccountResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> UndeleteServiceAccountResponse: ...
