import collections.abc
import typing

import httplib2
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http

from .schemas import *

_list = list

@typing.type_check_only
class GKEHubResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class OrganizationsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class LocationsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class FleetsResource(googleapiclient.discovery.Resource):
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int | None = ...,
                    pageToken: str | None = ...,
                    **kwargs: typing.Any,
                ) -> ListFleetsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListFleetsResponseHttpRequest,
                    previous_response: ListFleetsResponse,
                ) -> ListFleetsResponseHttpRequest | None: ...

            def fleets(self) -> FleetsResource: ...

        def locations(self) -> LocationsResource: ...

    @typing.type_check_only
    class ProjectsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class LocationsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class FeaturesResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: Feature,
                    featureId: str | None = ...,
                    requestId: str | None = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def delete(
                    self,
                    *,
                    name: str,
                    force: bool | None = ...,
                    requestId: str | None = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def get(
                    self,
                    *,
                    name: str,
                    returnPartialSuccess: bool | None = ...,
                    **kwargs: typing.Any,
                ) -> FeatureHttpRequest: ...
                def getIamPolicy(
                    self,
                    *,
                    resource: str,
                    options_requestedPolicyVersion: int | None = ...,
                    **kwargs: typing.Any,
                ) -> PolicyHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str | None = ...,
                    orderBy: str | None = ...,
                    pageSize: int | None = ...,
                    pageToken: str | None = ...,
                    returnPartialSuccess: bool | None = ...,
                    **kwargs: typing.Any,
                ) -> ListFeaturesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListFeaturesResponseHttpRequest,
                    previous_response: ListFeaturesResponse,
                ) -> ListFeaturesResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: Feature,
                    requestId: str | None = ...,
                    updateMask: str | None = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def setIamPolicy(
                    self,
                    *,
                    resource: str,
                    body: SetIamPolicyRequest,
                    **kwargs: typing.Any,
                ) -> PolicyHttpRequest: ...
                def testIamPermissions(
                    self,
                    *,
                    resource: str,
                    body: TestIamPermissionsRequest,
                    **kwargs: typing.Any,
                ) -> TestIamPermissionsResponseHttpRequest: ...

            @typing.type_check_only
            class FleetsResource(googleapiclient.discovery.Resource):
                def create(
                    self, *, parent: str, body: Fleet, **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> FleetHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int | None = ...,
                    pageToken: str | None = ...,
                    **kwargs: typing.Any,
                ) -> ListFleetsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListFleetsResponseHttpRequest,
                    previous_response: ListFleetsResponse,
                ) -> ListFleetsResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: Fleet,
                    updateMask: str | None = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...

            @typing.type_check_only
            class MembershipsResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class BindingsResource(googleapiclient.discovery.Resource):
                    def create(
                        self,
                        *,
                        parent: str,
                        body: MembershipBinding,
                        membershipBindingId: str | None = ...,
                        **kwargs: typing.Any,
                    ) -> OperationHttpRequest: ...
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> OperationHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> MembershipBindingHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str | None = ...,
                        pageSize: int | None = ...,
                        pageToken: str | None = ...,
                        **kwargs: typing.Any,
                    ) -> ListMembershipBindingsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: ListMembershipBindingsResponseHttpRequest,
                        previous_response: ListMembershipBindingsResponse,
                    ) -> ListMembershipBindingsResponseHttpRequest | None: ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: MembershipBinding,
                        updateMask: str | None = ...,
                        **kwargs: typing.Any,
                    ) -> OperationHttpRequest: ...

                @typing.type_check_only
                class RbacrolebindingsResource(googleapiclient.discovery.Resource):
                    def create(
                        self,
                        *,
                        parent: str,
                        body: RBACRoleBinding,
                        rbacrolebindingId: str | None = ...,
                        **kwargs: typing.Any,
                    ) -> OperationHttpRequest: ...
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> OperationHttpRequest: ...
                    def generateMembershipRBACRoleBindingYAML(
                        self,
                        *,
                        parent: str,
                        body: RBACRoleBinding,
                        rbacrolebindingId: str | None = ...,
                        **kwargs: typing.Any,
                    ) -> GenerateMembershipRBACRoleBindingYAMLResponseHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> RBACRoleBindingHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        pageSize: int | None = ...,
                        pageToken: str | None = ...,
                        **kwargs: typing.Any,
                    ) -> ListMembershipRBACRoleBindingsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: ListMembershipRBACRoleBindingsResponseHttpRequest,
                        previous_response: ListMembershipRBACRoleBindingsResponse,
                    ) -> ListMembershipRBACRoleBindingsResponseHttpRequest | None: ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: RBACRoleBinding,
                        updateMask: str | None = ...,
                        **kwargs: typing.Any,
                    ) -> OperationHttpRequest: ...

                def create(
                    self,
                    *,
                    parent: str,
                    body: Membership,
                    membershipId: str | None = ...,
                    requestId: str | None = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def delete(
                    self,
                    *,
                    name: str,
                    force: bool | None = ...,
                    requestId: str | None = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def generateConnectManifest(
                    self,
                    *,
                    name: str,
                    imagePullSecretContent: str | None = ...,
                    isUpgrade: bool | None = ...,
                    namespace: str | None = ...,
                    proxy: str | None = ...,
                    registry: str | None = ...,
                    version: str | None = ...,
                    **kwargs: typing.Any,
                ) -> GenerateConnectManifestResponseHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> MembershipHttpRequest: ...
                def getIamPolicy(
                    self,
                    *,
                    resource: str,
                    options_requestedPolicyVersion: int | None = ...,
                    **kwargs: typing.Any,
                ) -> PolicyHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str | None = ...,
                    orderBy: str | None = ...,
                    pageSize: int | None = ...,
                    pageToken: str | None = ...,
                    **kwargs: typing.Any,
                ) -> ListMembershipsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListMembershipsResponseHttpRequest,
                    previous_response: ListMembershipsResponse,
                ) -> ListMembershipsResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: Membership,
                    requestId: str | None = ...,
                    updateMask: str | None = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def setIamPolicy(
                    self,
                    *,
                    resource: str,
                    body: SetIamPolicyRequest,
                    **kwargs: typing.Any,
                ) -> PolicyHttpRequest: ...
                def testIamPermissions(
                    self,
                    *,
                    resource: str,
                    body: TestIamPermissionsRequest,
                    **kwargs: typing.Any,
                ) -> TestIamPermissionsResponseHttpRequest: ...
                def bindings(self) -> BindingsResource: ...
                def rbacrolebindings(self) -> RbacrolebindingsResource: ...

            @typing.type_check_only
            class OperationsResource(googleapiclient.discovery.Resource):
                def cancel(
                    self,
                    *,
                    name: str,
                    body: CancelOperationRequest,
                    **kwargs: typing.Any,
                ) -> EmptyHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def list(
                    self,
                    *,
                    name: str,
                    filter: str | None = ...,
                    pageSize: int | None = ...,
                    pageToken: str | None = ...,
                    returnPartialSuccess: bool | None = ...,
                    **kwargs: typing.Any,
                ) -> ListOperationsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListOperationsResponseHttpRequest,
                    previous_response: ListOperationsResponse,
                ) -> ListOperationsResponseHttpRequest | None: ...

            @typing.type_check_only
            class RolloutSequencesResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: RolloutSequence,
                    rolloutSequenceId: str | None = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> RolloutSequenceHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str | None = ...,
                    pageSize: int | None = ...,
                    pageToken: str | None = ...,
                    **kwargs: typing.Any,
                ) -> ListRolloutSequencesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListRolloutSequencesResponseHttpRequest,
                    previous_response: ListRolloutSequencesResponse,
                ) -> ListRolloutSequencesResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: RolloutSequence,
                    updateMask: str | None = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def upgrade(
                    self,
                    *,
                    name: str,
                    body: UpgradeRolloutSequenceRequest,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...

            @typing.type_check_only
            class RolloutsResource(googleapiclient.discovery.Resource):
                def cancel(
                    self, *, name: str, body: CancelRolloutRequest, **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def delete(
                    self,
                    *,
                    name: str,
                    requestId: str | None = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def forceCompleteStage(
                    self,
                    *,
                    name: str,
                    body: ForceCompleteRolloutStageRequest,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> RolloutHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str | None = ...,
                    pageSize: int | None = ...,
                    pageToken: str | None = ...,
                    **kwargs: typing.Any,
                ) -> ListRolloutsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListRolloutsResponseHttpRequest,
                    previous_response: ListRolloutsResponse,
                ) -> ListRolloutsResponseHttpRequest | None: ...
                def pause(
                    self, *, name: str, body: PauseRolloutRequest, **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def resume(
                    self, *, name: str, body: ResumeRolloutRequest, **kwargs: typing.Any
                ) -> OperationHttpRequest: ...

            @typing.type_check_only
            class ScopesResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class NamespacesResource(googleapiclient.discovery.Resource):
                    def create(
                        self,
                        *,
                        parent: str,
                        body: Namespace,
                        scopeNamespaceId: str | None = ...,
                        **kwargs: typing.Any,
                    ) -> OperationHttpRequest: ...
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> OperationHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> NamespaceHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        pageSize: int | None = ...,
                        pageToken: str | None = ...,
                        **kwargs: typing.Any,
                    ) -> ListScopeNamespacesResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: ListScopeNamespacesResponseHttpRequest,
                        previous_response: ListScopeNamespacesResponse,
                    ) -> ListScopeNamespacesResponseHttpRequest | None: ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: Namespace,
                        updateMask: str | None = ...,
                        **kwargs: typing.Any,
                    ) -> OperationHttpRequest: ...

                @typing.type_check_only
                class RbacrolebindingsResource(googleapiclient.discovery.Resource):
                    def create(
                        self,
                        *,
                        parent: str,
                        body: RBACRoleBinding,
                        rbacrolebindingId: str | None = ...,
                        **kwargs: typing.Any,
                    ) -> OperationHttpRequest: ...
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> OperationHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> RBACRoleBindingHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        pageSize: int | None = ...,
                        pageToken: str | None = ...,
                        **kwargs: typing.Any,
                    ) -> ListScopeRBACRoleBindingsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: ListScopeRBACRoleBindingsResponseHttpRequest,
                        previous_response: ListScopeRBACRoleBindingsResponse,
                    ) -> ListScopeRBACRoleBindingsResponseHttpRequest | None: ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: RBACRoleBinding,
                        updateMask: str | None = ...,
                        **kwargs: typing.Any,
                    ) -> OperationHttpRequest: ...

                def create(
                    self,
                    *,
                    parent: str,
                    body: Scope,
                    scopeId: str | None = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> ScopeHttpRequest: ...
                def getIamPolicy(
                    self,
                    *,
                    resource: str,
                    options_requestedPolicyVersion: int | None = ...,
                    **kwargs: typing.Any,
                ) -> PolicyHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int | None = ...,
                    pageToken: str | None = ...,
                    **kwargs: typing.Any,
                ) -> ListScopesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListScopesResponseHttpRequest,
                    previous_response: ListScopesResponse,
                ) -> ListScopesResponseHttpRequest | None: ...
                def listMemberships(
                    self,
                    *,
                    scopeName: str,
                    filter: str | None = ...,
                    pageSize: int | None = ...,
                    pageToken: str | None = ...,
                    **kwargs: typing.Any,
                ) -> ListBoundMembershipsResponseHttpRequest: ...
                def listMemberships_next(
                    self,
                    previous_request: ListBoundMembershipsResponseHttpRequest,
                    previous_response: ListBoundMembershipsResponse,
                ) -> ListBoundMembershipsResponseHttpRequest | None: ...
                def listPermitted(
                    self,
                    *,
                    parent: str,
                    pageSize: int | None = ...,
                    pageToken: str | None = ...,
                    **kwargs: typing.Any,
                ) -> ListPermittedScopesResponseHttpRequest: ...
                def listPermitted_next(
                    self,
                    previous_request: ListPermittedScopesResponseHttpRequest,
                    previous_response: ListPermittedScopesResponse,
                ) -> ListPermittedScopesResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: Scope,
                    updateMask: str | None = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def setIamPolicy(
                    self,
                    *,
                    resource: str,
                    body: SetIamPolicyRequest,
                    **kwargs: typing.Any,
                ) -> PolicyHttpRequest: ...
                def testIamPermissions(
                    self,
                    *,
                    resource: str,
                    body: TestIamPermissionsRequest,
                    **kwargs: typing.Any,
                ) -> TestIamPermissionsResponseHttpRequest: ...
                def namespaces(self) -> NamespacesResource: ...
                def rbacrolebindings(self) -> RbacrolebindingsResource: ...

            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> LocationHttpRequest: ...
            def list(
                self,
                *,
                name: str,
                extraLocationTypes: str | _list[str] | None = ...,
                filter: str | None = ...,
                pageSize: int | None = ...,
                pageToken: str | None = ...,
                **kwargs: typing.Any,
            ) -> ListLocationsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListLocationsResponseHttpRequest,
                previous_response: ListLocationsResponse,
            ) -> ListLocationsResponseHttpRequest | None: ...
            def features(self) -> FeaturesResource: ...
            def fleets(self) -> FleetsResource: ...
            def memberships(self) -> MembershipsResource: ...
            def operations(self) -> OperationsResource: ...
            def rolloutSequences(self) -> RolloutSequencesResource: ...
            def rollouts(self) -> RolloutsResource: ...
            def scopes(self) -> ScopesResource: ...

        def locations(self) -> LocationsResource: ...

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
    def organizations(self) -> OrganizationsResource: ...
    def projects(self) -> ProjectsResource: ...

@typing.type_check_only
class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Empty: ...

@typing.type_check_only
class FeatureHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Feature: ...

@typing.type_check_only
class FleetHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Fleet: ...

@typing.type_check_only
class GenerateConnectManifestResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GenerateConnectManifestResponse: ...

@typing.type_check_only
class GenerateMembershipRBACRoleBindingYAMLResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GenerateMembershipRBACRoleBindingYAMLResponse: ...

@typing.type_check_only
class ListBoundMembershipsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListBoundMembershipsResponse: ...

@typing.type_check_only
class ListFeaturesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListFeaturesResponse: ...

@typing.type_check_only
class ListFleetsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListFleetsResponse: ...

@typing.type_check_only
class ListLocationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListLocationsResponse: ...

@typing.type_check_only
class ListMembershipBindingsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListMembershipBindingsResponse: ...

@typing.type_check_only
class ListMembershipRBACRoleBindingsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListMembershipRBACRoleBindingsResponse: ...

@typing.type_check_only
class ListMembershipsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListMembershipsResponse: ...

@typing.type_check_only
class ListOperationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListOperationsResponse: ...

@typing.type_check_only
class ListPermittedScopesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListPermittedScopesResponse: ...

@typing.type_check_only
class ListRolloutSequencesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListRolloutSequencesResponse: ...

@typing.type_check_only
class ListRolloutsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListRolloutsResponse: ...

@typing.type_check_only
class ListScopeNamespacesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListScopeNamespacesResponse: ...

@typing.type_check_only
class ListScopeRBACRoleBindingsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListScopeRBACRoleBindingsResponse: ...

@typing.type_check_only
class ListScopesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListScopesResponse: ...

@typing.type_check_only
class LocationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Location: ...

@typing.type_check_only
class MembershipHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Membership: ...

@typing.type_check_only
class MembershipBindingHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> MembershipBinding: ...

@typing.type_check_only
class NamespaceHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Namespace: ...

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
class RBACRoleBindingHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> RBACRoleBinding: ...

@typing.type_check_only
class RolloutHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Rollout: ...

@typing.type_check_only
class RolloutSequenceHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> RolloutSequence: ...

@typing.type_check_only
class ScopeHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Scope: ...

@typing.type_check_only
class TestIamPermissionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> TestIamPermissionsResponse: ...
