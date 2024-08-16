import collections.abc
import typing

import httplib2
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http

from .schemas import *

_list = list

@typing.type_check_only
class IamResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class IamPoliciesResource(googleapiclient.discovery.Resource):
        def lintPolicy(
            self, *, body: LintPolicyRequest = ..., **kwargs: typing.Any
        ) -> LintPolicyResponseHttpRequest: ...
        def queryAuditableServices(
            self, *, body: QueryAuditableServicesRequest = ..., **kwargs: typing.Any
        ) -> QueryAuditableServicesResponseHttpRequest: ...

    @typing.type_check_only
    class LocationsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class WorkforcePoolsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class OperationsResource(googleapiclient.discovery.Resource):
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> OperationHttpRequest: ...

            @typing.type_check_only
            class ProvidersResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class KeysResource(googleapiclient.discovery.Resource):
                    @typing.type_check_only
                    class OperationsResource(googleapiclient.discovery.Resource):
                        def get(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> OperationHttpRequest: ...

                    def create(
                        self,
                        *,
                        parent: str,
                        body: WorkforcePoolProviderKey = ...,
                        workforcePoolProviderKeyId: str = ...,
                        **kwargs: typing.Any,
                    ) -> OperationHttpRequest: ...
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> OperationHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> WorkforcePoolProviderKeyHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        showDeleted: bool = ...,
                        **kwargs: typing.Any,
                    ) -> ListWorkforcePoolProviderKeysResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: ListWorkforcePoolProviderKeysResponseHttpRequest,
                        previous_response: ListWorkforcePoolProviderKeysResponse,
                    ) -> ListWorkforcePoolProviderKeysResponseHttpRequest | None: ...
                    def undelete(
                        self,
                        *,
                        name: str,
                        body: UndeleteWorkforcePoolProviderKeyRequest = ...,
                        **kwargs: typing.Any,
                    ) -> OperationHttpRequest: ...
                    def operations(self) -> OperationsResource: ...

                @typing.type_check_only
                class OperationsResource(googleapiclient.discovery.Resource):
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> OperationHttpRequest: ...

                def create(
                    self,
                    *,
                    parent: str,
                    body: WorkforcePoolProvider = ...,
                    workforcePoolProviderId: str = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> WorkforcePoolProviderHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    showDeleted: bool = ...,
                    **kwargs: typing.Any,
                ) -> ListWorkforcePoolProvidersResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListWorkforcePoolProvidersResponseHttpRequest,
                    previous_response: ListWorkforcePoolProvidersResponse,
                ) -> ListWorkforcePoolProvidersResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: WorkforcePoolProvider = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def undelete(
                    self,
                    *,
                    name: str,
                    body: UndeleteWorkforcePoolProviderRequest = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def keys(self) -> KeysResource: ...
                def operations(self) -> OperationsResource: ...

            @typing.type_check_only
            class SubjectsResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class OperationsResource(googleapiclient.discovery.Resource):
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> OperationHttpRequest: ...

                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def undelete(
                    self,
                    *,
                    name: str,
                    body: UndeleteWorkforcePoolSubjectRequest = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def operations(self) -> OperationsResource: ...

            def create(
                self,
                *,
                location: str,
                body: WorkforcePool = ...,
                workforcePoolId: str = ...,
                **kwargs: typing.Any,
            ) -> OperationHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> OperationHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> WorkforcePoolHttpRequest: ...
            def getIamPolicy(
                self,
                *,
                resource: str,
                body: GetIamPolicyRequest = ...,
                **kwargs: typing.Any,
            ) -> PolicyHttpRequest: ...
            def list(
                self,
                *,
                location: str,
                pageSize: int = ...,
                pageToken: str = ...,
                parent: str = ...,
                showDeleted: bool = ...,
                **kwargs: typing.Any,
            ) -> ListWorkforcePoolsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListWorkforcePoolsResponseHttpRequest,
                previous_response: ListWorkforcePoolsResponse,
            ) -> ListWorkforcePoolsResponseHttpRequest | None: ...
            def patch(
                self,
                *,
                name: str,
                body: WorkforcePool = ...,
                updateMask: str = ...,
                **kwargs: typing.Any,
            ) -> OperationHttpRequest: ...
            def setIamPolicy(
                self,
                *,
                resource: str,
                body: SetIamPolicyRequest = ...,
                **kwargs: typing.Any,
            ) -> PolicyHttpRequest: ...
            def testIamPermissions(
                self,
                *,
                resource: str,
                body: TestIamPermissionsRequest = ...,
                **kwargs: typing.Any,
            ) -> TestIamPermissionsResponseHttpRequest: ...
            def undelete(
                self,
                *,
                name: str,
                body: UndeleteWorkforcePoolRequest = ...,
                **kwargs: typing.Any,
            ) -> OperationHttpRequest: ...
            def operations(self) -> OperationsResource: ...
            def providers(self) -> ProvidersResource: ...
            def subjects(self) -> SubjectsResource: ...

        def workforcePools(self) -> WorkforcePoolsResource: ...

    @typing.type_check_only
    class OrganizationsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class RolesResource(googleapiclient.discovery.Resource):
            def create(
                self,
                *,
                parent: str,
                body: CreateRoleRequest = ...,
                **kwargs: typing.Any,
            ) -> RoleHttpRequest: ...
            def delete(
                self, *, name: str, etag: str = ..., **kwargs: typing.Any
            ) -> RoleHttpRequest: ...
            def get(self, *, name: str, **kwargs: typing.Any) -> RoleHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                showDeleted: bool = ...,
                view: typing_extensions.Literal["BASIC", "FULL"] = ...,
                **kwargs: typing.Any,
            ) -> ListRolesResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListRolesResponseHttpRequest,
                previous_response: ListRolesResponse,
            ) -> ListRolesResponseHttpRequest | None: ...
            def patch(
                self,
                *,
                name: str,
                body: Role = ...,
                updateMask: str = ...,
                **kwargs: typing.Any,
            ) -> RoleHttpRequest: ...
            def undelete(
                self,
                *,
                name: str,
                body: UndeleteRoleRequest = ...,
                **kwargs: typing.Any,
            ) -> RoleHttpRequest: ...

        def roles(self) -> RolesResource: ...

    @typing.type_check_only
    class PermissionsResource(googleapiclient.discovery.Resource):
        def queryTestablePermissions(
            self, *, body: QueryTestablePermissionsRequest = ..., **kwargs: typing.Any
        ) -> QueryTestablePermissionsResponseHttpRequest: ...
        def queryTestablePermissions_next(
            self,
            previous_request: QueryTestablePermissionsResponseHttpRequest,
            previous_response: QueryTestablePermissionsResponse,
        ) -> QueryTestablePermissionsResponseHttpRequest | None: ...

    @typing.type_check_only
    class ProjectsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class LocationsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class OauthClientsResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class CredentialsResource(googleapiclient.discovery.Resource):
                    def create(
                        self,
                        *,
                        parent: str,
                        body: OauthClientCredential = ...,
                        oauthClientCredentialId: str = ...,
                        **kwargs: typing.Any,
                    ) -> OauthClientCredentialHttpRequest: ...
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> EmptyHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> OauthClientCredentialHttpRequest: ...
                    def list(
                        self, *, parent: str, **kwargs: typing.Any
                    ) -> ListOauthClientCredentialsResponseHttpRequest: ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: OauthClientCredential = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any,
                    ) -> OauthClientCredentialHttpRequest: ...

                def create(
                    self,
                    *,
                    parent: str,
                    body: OauthClient = ...,
                    oauthClientId: str = ...,
                    **kwargs: typing.Any,
                ) -> OauthClientHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> OauthClientHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> OauthClientHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    showDeleted: bool = ...,
                    **kwargs: typing.Any,
                ) -> ListOauthClientsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListOauthClientsResponseHttpRequest,
                    previous_response: ListOauthClientsResponse,
                ) -> ListOauthClientsResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: OauthClient = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> OauthClientHttpRequest: ...
                def undelete(
                    self,
                    *,
                    name: str,
                    body: UndeleteOauthClientRequest = ...,
                    **kwargs: typing.Any,
                ) -> OauthClientHttpRequest: ...
                def credentials(self) -> CredentialsResource: ...

            @typing.type_check_only
            class WorkloadIdentityPoolsResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class NamespacesResource(googleapiclient.discovery.Resource):
                    @typing.type_check_only
                    class ManagedIdentitiesResource(googleapiclient.discovery.Resource):
                        @typing.type_check_only
                        class OperationsResource(googleapiclient.discovery.Resource):
                            def get(
                                self, *, name: str, **kwargs: typing.Any
                            ) -> OperationHttpRequest: ...

                        @typing.type_check_only
                        class WorkloadSourcesResource(
                            googleapiclient.discovery.Resource
                        ):
                            @typing.type_check_only
                            class OperationsResource(
                                googleapiclient.discovery.Resource
                            ):
                                def get(
                                    self, *, name: str, **kwargs: typing.Any
                                ) -> OperationHttpRequest: ...

                            def operations(self) -> OperationsResource: ...

                        def operations(self) -> OperationsResource: ...
                        def workloadSources(self) -> WorkloadSourcesResource: ...

                    @typing.type_check_only
                    class OperationsResource(googleapiclient.discovery.Resource):
                        def get(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> OperationHttpRequest: ...

                    def managedIdentities(self) -> ManagedIdentitiesResource: ...
                    def operations(self) -> OperationsResource: ...

                @typing.type_check_only
                class OperationsResource(googleapiclient.discovery.Resource):
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> OperationHttpRequest: ...

                @typing.type_check_only
                class ProvidersResource(googleapiclient.discovery.Resource):
                    @typing.type_check_only
                    class KeysResource(googleapiclient.discovery.Resource):
                        @typing.type_check_only
                        class OperationsResource(googleapiclient.discovery.Resource):
                            def get(
                                self, *, name: str, **kwargs: typing.Any
                            ) -> OperationHttpRequest: ...

                        def create(
                            self,
                            *,
                            parent: str,
                            body: WorkloadIdentityPoolProviderKey = ...,
                            workloadIdentityPoolProviderKeyId: str = ...,
                            **kwargs: typing.Any,
                        ) -> OperationHttpRequest: ...
                        def delete(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> OperationHttpRequest: ...
                        def get(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> WorkloadIdentityPoolProviderKeyHttpRequest: ...
                        def list(
                            self,
                            *,
                            parent: str,
                            pageSize: int = ...,
                            pageToken: str = ...,
                            showDeleted: bool = ...,
                            **kwargs: typing.Any,
                        ) -> (
                            ListWorkloadIdentityPoolProviderKeysResponseHttpRequest
                        ): ...
                        def list_next(
                            self,
                            previous_request: ListWorkloadIdentityPoolProviderKeysResponseHttpRequest,
                            previous_response: ListWorkloadIdentityPoolProviderKeysResponse,
                        ) -> (
                            ListWorkloadIdentityPoolProviderKeysResponseHttpRequest
                            | None
                        ): ...
                        def undelete(
                            self,
                            *,
                            name: str,
                            body: UndeleteWorkloadIdentityPoolProviderKeyRequest = ...,
                            **kwargs: typing.Any,
                        ) -> OperationHttpRequest: ...
                        def operations(self) -> OperationsResource: ...

                    @typing.type_check_only
                    class OperationsResource(googleapiclient.discovery.Resource):
                        def get(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> OperationHttpRequest: ...

                    def create(
                        self,
                        *,
                        parent: str,
                        body: WorkloadIdentityPoolProvider = ...,
                        workloadIdentityPoolProviderId: str = ...,
                        **kwargs: typing.Any,
                    ) -> OperationHttpRequest: ...
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> OperationHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> WorkloadIdentityPoolProviderHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        showDeleted: bool = ...,
                        **kwargs: typing.Any,
                    ) -> ListWorkloadIdentityPoolProvidersResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: ListWorkloadIdentityPoolProvidersResponseHttpRequest,
                        previous_response: ListWorkloadIdentityPoolProvidersResponse,
                    ) -> (
                        ListWorkloadIdentityPoolProvidersResponseHttpRequest | None
                    ): ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: WorkloadIdentityPoolProvider = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any,
                    ) -> OperationHttpRequest: ...
                    def undelete(
                        self,
                        *,
                        name: str,
                        body: UndeleteWorkloadIdentityPoolProviderRequest = ...,
                        **kwargs: typing.Any,
                    ) -> OperationHttpRequest: ...
                    def keys(self) -> KeysResource: ...
                    def operations(self) -> OperationsResource: ...

                def create(
                    self,
                    *,
                    parent: str,
                    body: WorkloadIdentityPool = ...,
                    workloadIdentityPoolId: str = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> WorkloadIdentityPoolHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    showDeleted: bool = ...,
                    **kwargs: typing.Any,
                ) -> ListWorkloadIdentityPoolsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListWorkloadIdentityPoolsResponseHttpRequest,
                    previous_response: ListWorkloadIdentityPoolsResponse,
                ) -> ListWorkloadIdentityPoolsResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: WorkloadIdentityPool = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def undelete(
                    self,
                    *,
                    name: str,
                    body: UndeleteWorkloadIdentityPoolRequest = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def namespaces(self) -> NamespacesResource: ...
                def operations(self) -> OperationsResource: ...
                def providers(self) -> ProvidersResource: ...

            def oauthClients(self) -> OauthClientsResource: ...
            def workloadIdentityPools(self) -> WorkloadIdentityPoolsResource: ...

        @typing.type_check_only
        class RolesResource(googleapiclient.discovery.Resource):
            def create(
                self,
                *,
                parent: str,
                body: CreateRoleRequest = ...,
                **kwargs: typing.Any,
            ) -> RoleHttpRequest: ...
            def delete(
                self, *, name: str, etag: str = ..., **kwargs: typing.Any
            ) -> RoleHttpRequest: ...
            def get(self, *, name: str, **kwargs: typing.Any) -> RoleHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                showDeleted: bool = ...,
                view: typing_extensions.Literal["BASIC", "FULL"] = ...,
                **kwargs: typing.Any,
            ) -> ListRolesResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListRolesResponseHttpRequest,
                previous_response: ListRolesResponse,
            ) -> ListRolesResponseHttpRequest | None: ...
            def patch(
                self,
                *,
                name: str,
                body: Role = ...,
                updateMask: str = ...,
                **kwargs: typing.Any,
            ) -> RoleHttpRequest: ...
            def undelete(
                self,
                *,
                name: str,
                body: UndeleteRoleRequest = ...,
                **kwargs: typing.Any,
            ) -> RoleHttpRequest: ...

        @typing.type_check_only
        class ServiceAccountsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class KeysResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    name: str,
                    body: CreateServiceAccountKeyRequest = ...,
                    **kwargs: typing.Any,
                ) -> ServiceAccountKeyHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def disable(
                    self,
                    *,
                    name: str,
                    body: DisableServiceAccountKeyRequest = ...,
                    **kwargs: typing.Any,
                ) -> EmptyHttpRequest: ...
                def enable(
                    self,
                    *,
                    name: str,
                    body: EnableServiceAccountKeyRequest = ...,
                    **kwargs: typing.Any,
                ) -> EmptyHttpRequest: ...
                def get(
                    self,
                    *,
                    name: str,
                    publicKeyType: typing_extensions.Literal[
                        "TYPE_NONE", "TYPE_X509_PEM_FILE", "TYPE_RAW_PUBLIC_KEY"
                    ] = ...,
                    **kwargs: typing.Any,
                ) -> ServiceAccountKeyHttpRequest: ...
                def list(
                    self,
                    *,
                    name: str,
                    keyTypes: typing_extensions.Literal[
                        "KEY_TYPE_UNSPECIFIED", "USER_MANAGED", "SYSTEM_MANAGED"
                    ]
                    | _list[
                        typing_extensions.Literal[
                            "KEY_TYPE_UNSPECIFIED", "USER_MANAGED", "SYSTEM_MANAGED"
                        ]
                    ] = ...,
                    **kwargs: typing.Any,
                ) -> ListServiceAccountKeysResponseHttpRequest: ...
                def upload(
                    self,
                    *,
                    name: str,
                    body: UploadServiceAccountKeyRequest = ...,
                    **kwargs: typing.Any,
                ) -> ServiceAccountKeyHttpRequest: ...

            def create(
                self,
                *,
                name: str,
                body: CreateServiceAccountRequest = ...,
                **kwargs: typing.Any,
            ) -> ServiceAccountHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def disable(
                self,
                *,
                name: str,
                body: DisableServiceAccountRequest = ...,
                **kwargs: typing.Any,
            ) -> EmptyHttpRequest: ...
            def enable(
                self,
                *,
                name: str,
                body: EnableServiceAccountRequest = ...,
                **kwargs: typing.Any,
            ) -> EmptyHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> ServiceAccountHttpRequest: ...
            def getIamPolicy(
                self,
                *,
                resource: str,
                options_requestedPolicyVersion: int = ...,
                **kwargs: typing.Any,
            ) -> PolicyHttpRequest: ...
            def list(
                self,
                *,
                name: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any,
            ) -> ListServiceAccountsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListServiceAccountsResponseHttpRequest,
                previous_response: ListServiceAccountsResponse,
            ) -> ListServiceAccountsResponseHttpRequest | None: ...
            def patch(
                self,
                *,
                name: str,
                body: PatchServiceAccountRequest = ...,
                **kwargs: typing.Any,
            ) -> ServiceAccountHttpRequest: ...
            def setIamPolicy(
                self,
                *,
                resource: str,
                body: SetIamPolicyRequest = ...,
                **kwargs: typing.Any,
            ) -> PolicyHttpRequest: ...
            def signBlob(
                self, *, name: str, body: SignBlobRequest = ..., **kwargs: typing.Any
            ) -> SignBlobResponseHttpRequest: ...
            def signJwt(
                self, *, name: str, body: SignJwtRequest = ..., **kwargs: typing.Any
            ) -> SignJwtResponseHttpRequest: ...
            def testIamPermissions(
                self,
                *,
                resource: str,
                body: TestIamPermissionsRequest = ...,
                **kwargs: typing.Any,
            ) -> TestIamPermissionsResponseHttpRequest: ...
            def undelete(
                self,
                *,
                name: str,
                body: UndeleteServiceAccountRequest = ...,
                **kwargs: typing.Any,
            ) -> UndeleteServiceAccountResponseHttpRequest: ...
            def update(
                self, *, name: str, body: ServiceAccount = ..., **kwargs: typing.Any
            ) -> ServiceAccountHttpRequest: ...
            def keys(self) -> KeysResource: ...

        def locations(self) -> LocationsResource: ...
        def roles(self) -> RolesResource: ...
        def serviceAccounts(self) -> ServiceAccountsResource: ...

    @typing.type_check_only
    class RolesResource(googleapiclient.discovery.Resource):
        def get(self, *, name: str, **kwargs: typing.Any) -> RoleHttpRequest: ...
        def list(
            self,
            *,
            pageSize: int = ...,
            pageToken: str = ...,
            parent: str = ...,
            showDeleted: bool = ...,
            view: typing_extensions.Literal["BASIC", "FULL"] = ...,
            **kwargs: typing.Any,
        ) -> ListRolesResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: ListRolesResponseHttpRequest,
            previous_response: ListRolesResponse,
        ) -> ListRolesResponseHttpRequest | None: ...
        def queryGrantableRoles(
            self, *, body: QueryGrantableRolesRequest = ..., **kwargs: typing.Any
        ) -> QueryGrantableRolesResponseHttpRequest: ...
        def queryGrantableRoles_next(
            self,
            previous_request: QueryGrantableRolesResponseHttpRequest,
            previous_response: QueryGrantableRolesResponse,
        ) -> QueryGrantableRolesResponseHttpRequest | None: ...

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
    def iamPolicies(self) -> IamPoliciesResource: ...
    def locations(self) -> LocationsResource: ...
    def organizations(self) -> OrganizationsResource: ...
    def permissions(self) -> PermissionsResource: ...
    def projects(self) -> ProjectsResource: ...
    def roles(self) -> RolesResource: ...

@typing.type_check_only
class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Empty: ...

@typing.type_check_only
class LintPolicyResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> LintPolicyResponse: ...

@typing.type_check_only
class ListOauthClientCredentialsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListOauthClientCredentialsResponse: ...

@typing.type_check_only
class ListOauthClientsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListOauthClientsResponse: ...

@typing.type_check_only
class ListRolesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListRolesResponse: ...

@typing.type_check_only
class ListServiceAccountKeysResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListServiceAccountKeysResponse: ...

@typing.type_check_only
class ListServiceAccountsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListServiceAccountsResponse: ...

@typing.type_check_only
class ListWorkforcePoolProviderKeysResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListWorkforcePoolProviderKeysResponse: ...

@typing.type_check_only
class ListWorkforcePoolProvidersResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListWorkforcePoolProvidersResponse: ...

@typing.type_check_only
class ListWorkforcePoolsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListWorkforcePoolsResponse: ...

@typing.type_check_only
class ListWorkloadIdentityPoolProviderKeysResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListWorkloadIdentityPoolProviderKeysResponse: ...

@typing.type_check_only
class ListWorkloadIdentityPoolProvidersResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListWorkloadIdentityPoolProvidersResponse: ...

@typing.type_check_only
class ListWorkloadIdentityPoolsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListWorkloadIdentityPoolsResponse: ...

@typing.type_check_only
class OauthClientHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> OauthClient: ...

@typing.type_check_only
class OauthClientCredentialHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> OauthClientCredential: ...

@typing.type_check_only
class OperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Operation: ...

@typing.type_check_only
class PolicyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Policy: ...

@typing.type_check_only
class QueryAuditableServicesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> QueryAuditableServicesResponse: ...

@typing.type_check_only
class QueryGrantableRolesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> QueryGrantableRolesResponse: ...

@typing.type_check_only
class QueryTestablePermissionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> QueryTestablePermissionsResponse: ...

@typing.type_check_only
class RoleHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Role: ...

@typing.type_check_only
class ServiceAccountHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ServiceAccount: ...

@typing.type_check_only
class ServiceAccountKeyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ServiceAccountKey: ...

@typing.type_check_only
class SignBlobResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> SignBlobResponse: ...

@typing.type_check_only
class SignJwtResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> SignJwtResponse: ...

@typing.type_check_only
class TestIamPermissionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> TestIamPermissionsResponse: ...

@typing.type_check_only
class UndeleteServiceAccountResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> UndeleteServiceAccountResponse: ...

@typing.type_check_only
class WorkforcePoolHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> WorkforcePool: ...

@typing.type_check_only
class WorkforcePoolProviderHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> WorkforcePoolProvider: ...

@typing.type_check_only
class WorkforcePoolProviderKeyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> WorkforcePoolProviderKey: ...

@typing.type_check_only
class WorkloadIdentityPoolHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> WorkloadIdentityPool: ...

@typing.type_check_only
class WorkloadIdentityPoolProviderHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> WorkloadIdentityPoolProvider: ...

@typing.type_check_only
class WorkloadIdentityPoolProviderKeyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> WorkloadIdentityPoolProviderKey: ...
