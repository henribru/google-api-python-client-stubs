import collections.abc
import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

_list = list

@typing.type_check_only
class CloudResourceManagerResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class FoldersResource(googleapiclient.discovery.Resource):
        def clearOrgPolicy(
            self,
            *,
            resource: str,
            body: ClearOrgPolicyRequest = ...,
            **kwargs: typing.Any
        ) -> EmptyHttpRequest: ...
        def getEffectiveOrgPolicy(
            self,
            *,
            resource: str,
            body: GetEffectiveOrgPolicyRequest = ...,
            **kwargs: typing.Any
        ) -> OrgPolicyHttpRequest: ...
        def getOrgPolicy(
            self,
            *,
            resource: str,
            body: GetOrgPolicyRequest = ...,
            **kwargs: typing.Any
        ) -> OrgPolicyHttpRequest: ...
        def listAvailableOrgPolicyConstraints(
            self,
            *,
            resource: str,
            body: ListAvailableOrgPolicyConstraintsRequest = ...,
            **kwargs: typing.Any
        ) -> ListAvailableOrgPolicyConstraintsResponseHttpRequest: ...
        def listAvailableOrgPolicyConstraints_next(
            self,
            previous_request: ListAvailableOrgPolicyConstraintsResponseHttpRequest,
            previous_response: ListAvailableOrgPolicyConstraintsResponse,
        ) -> ListAvailableOrgPolicyConstraintsResponseHttpRequest | None: ...
        def listOrgPolicies(
            self,
            *,
            resource: str,
            body: ListOrgPoliciesRequest = ...,
            **kwargs: typing.Any
        ) -> ListOrgPoliciesResponseHttpRequest: ...
        def listOrgPolicies_next(
            self,
            previous_request: ListOrgPoliciesResponseHttpRequest,
            previous_response: ListOrgPoliciesResponse,
        ) -> ListOrgPoliciesResponseHttpRequest | None: ...
        def setOrgPolicy(
            self,
            *,
            resource: str,
            body: SetOrgPolicyRequest = ...,
            **kwargs: typing.Any
        ) -> OrgPolicyHttpRequest: ...

    @typing.type_check_only
    class LiensResource(googleapiclient.discovery.Resource):
        def create(
            self, *, body: Lien = ..., **kwargs: typing.Any
        ) -> LienHttpRequest: ...
        def delete(self, *, name: str, **kwargs: typing.Any) -> EmptyHttpRequest: ...
        def get(self, *, name: str, **kwargs: typing.Any) -> LienHttpRequest: ...
        def list(
            self,
            *,
            pageSize: int = ...,
            pageToken: str = ...,
            parent: str = ...,
            **kwargs: typing.Any
        ) -> ListLiensResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: ListLiensResponseHttpRequest,
            previous_response: ListLiensResponse,
        ) -> ListLiensResponseHttpRequest | None: ...

    @typing.type_check_only
    class OperationsResource(googleapiclient.discovery.Resource):
        def get(self, *, name: str, **kwargs: typing.Any) -> OperationHttpRequest: ...

    @typing.type_check_only
    class OrganizationsResource(googleapiclient.discovery.Resource):
        def clearOrgPolicy(
            self,
            *,
            resource: str,
            body: ClearOrgPolicyRequest = ...,
            **kwargs: typing.Any
        ) -> EmptyHttpRequest: ...
        def get(
            self, *, name: str, **kwargs: typing.Any
        ) -> OrganizationHttpRequest: ...
        def getEffectiveOrgPolicy(
            self,
            *,
            resource: str,
            body: GetEffectiveOrgPolicyRequest = ...,
            **kwargs: typing.Any
        ) -> OrgPolicyHttpRequest: ...
        def getIamPolicy(
            self,
            *,
            resource: str,
            body: GetIamPolicyRequest = ...,
            **kwargs: typing.Any
        ) -> PolicyHttpRequest: ...
        def getOrgPolicy(
            self,
            *,
            resource: str,
            body: GetOrgPolicyRequest = ...,
            **kwargs: typing.Any
        ) -> OrgPolicyHttpRequest: ...
        def listAvailableOrgPolicyConstraints(
            self,
            *,
            resource: str,
            body: ListAvailableOrgPolicyConstraintsRequest = ...,
            **kwargs: typing.Any
        ) -> ListAvailableOrgPolicyConstraintsResponseHttpRequest: ...
        def listAvailableOrgPolicyConstraints_next(
            self,
            previous_request: ListAvailableOrgPolicyConstraintsResponseHttpRequest,
            previous_response: ListAvailableOrgPolicyConstraintsResponse,
        ) -> ListAvailableOrgPolicyConstraintsResponseHttpRequest | None: ...
        def listOrgPolicies(
            self,
            *,
            resource: str,
            body: ListOrgPoliciesRequest = ...,
            **kwargs: typing.Any
        ) -> ListOrgPoliciesResponseHttpRequest: ...
        def listOrgPolicies_next(
            self,
            previous_request: ListOrgPoliciesResponseHttpRequest,
            previous_response: ListOrgPoliciesResponse,
        ) -> ListOrgPoliciesResponseHttpRequest | None: ...
        def search(
            self, *, body: SearchOrganizationsRequest = ..., **kwargs: typing.Any
        ) -> SearchOrganizationsResponseHttpRequest: ...
        def search_next(
            self,
            previous_request: SearchOrganizationsResponseHttpRequest,
            previous_response: SearchOrganizationsResponse,
        ) -> SearchOrganizationsResponseHttpRequest | None: ...
        def setIamPolicy(
            self,
            *,
            resource: str,
            body: SetIamPolicyRequest = ...,
            **kwargs: typing.Any
        ) -> PolicyHttpRequest: ...
        def setOrgPolicy(
            self,
            *,
            resource: str,
            body: SetOrgPolicyRequest = ...,
            **kwargs: typing.Any
        ) -> OrgPolicyHttpRequest: ...
        def testIamPermissions(
            self,
            *,
            resource: str,
            body: TestIamPermissionsRequest = ...,
            **kwargs: typing.Any
        ) -> TestIamPermissionsResponseHttpRequest: ...

    @typing.type_check_only
    class ProjectsResource(googleapiclient.discovery.Resource):
        def clearOrgPolicy(
            self,
            *,
            resource: str,
            body: ClearOrgPolicyRequest = ...,
            **kwargs: typing.Any
        ) -> EmptyHttpRequest: ...
        def create(
            self, *, body: Project = ..., **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def delete(
            self, *, projectId: str, **kwargs: typing.Any
        ) -> EmptyHttpRequest: ...
        def get(
            self, *, projectId: str, **kwargs: typing.Any
        ) -> ProjectHttpRequest: ...
        def getAncestry(
            self,
            *,
            projectId: str,
            body: GetAncestryRequest = ...,
            **kwargs: typing.Any
        ) -> GetAncestryResponseHttpRequest: ...
        def getEffectiveOrgPolicy(
            self,
            *,
            resource: str,
            body: GetEffectiveOrgPolicyRequest = ...,
            **kwargs: typing.Any
        ) -> OrgPolicyHttpRequest: ...
        def getIamPolicy(
            self,
            *,
            resource: str,
            body: GetIamPolicyRequest = ...,
            **kwargs: typing.Any
        ) -> PolicyHttpRequest: ...
        def getOrgPolicy(
            self,
            *,
            resource: str,
            body: GetOrgPolicyRequest = ...,
            **kwargs: typing.Any
        ) -> OrgPolicyHttpRequest: ...
        def list(
            self,
            *,
            filter: str = ...,
            pageSize: int = ...,
            pageToken: str = ...,
            **kwargs: typing.Any
        ) -> ListProjectsResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: ListProjectsResponseHttpRequest,
            previous_response: ListProjectsResponse,
        ) -> ListProjectsResponseHttpRequest | None: ...
        def listAvailableOrgPolicyConstraints(
            self,
            *,
            resource: str,
            body: ListAvailableOrgPolicyConstraintsRequest = ...,
            **kwargs: typing.Any
        ) -> ListAvailableOrgPolicyConstraintsResponseHttpRequest: ...
        def listAvailableOrgPolicyConstraints_next(
            self,
            previous_request: ListAvailableOrgPolicyConstraintsResponseHttpRequest,
            previous_response: ListAvailableOrgPolicyConstraintsResponse,
        ) -> ListAvailableOrgPolicyConstraintsResponseHttpRequest | None: ...
        def listOrgPolicies(
            self,
            *,
            resource: str,
            body: ListOrgPoliciesRequest = ...,
            **kwargs: typing.Any
        ) -> ListOrgPoliciesResponseHttpRequest: ...
        def listOrgPolicies_next(
            self,
            previous_request: ListOrgPoliciesResponseHttpRequest,
            previous_response: ListOrgPoliciesResponse,
        ) -> ListOrgPoliciesResponseHttpRequest | None: ...
        def setIamPolicy(
            self,
            *,
            resource: str,
            body: SetIamPolicyRequest = ...,
            **kwargs: typing.Any
        ) -> PolicyHttpRequest: ...
        def setOrgPolicy(
            self,
            *,
            resource: str,
            body: SetOrgPolicyRequest = ...,
            **kwargs: typing.Any
        ) -> OrgPolicyHttpRequest: ...
        def testIamPermissions(
            self,
            *,
            resource: str,
            body: TestIamPermissionsRequest = ...,
            **kwargs: typing.Any
        ) -> TestIamPermissionsResponseHttpRequest: ...
        def undelete(
            self,
            *,
            projectId: str,
            body: UndeleteProjectRequest = ...,
            **kwargs: typing.Any
        ) -> EmptyHttpRequest: ...
        def update(
            self, *, projectId: str, body: Project = ..., **kwargs: typing.Any
        ) -> ProjectHttpRequest: ...

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
    def folders(self) -> FoldersResource: ...
    def liens(self) -> LiensResource: ...
    def operations(self) -> OperationsResource: ...
    def organizations(self) -> OrganizationsResource: ...
    def projects(self) -> ProjectsResource: ...

@typing.type_check_only
class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Empty: ...

@typing.type_check_only
class GetAncestryResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GetAncestryResponse: ...

@typing.type_check_only
class LienHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Lien: ...

@typing.type_check_only
class ListAvailableOrgPolicyConstraintsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListAvailableOrgPolicyConstraintsResponse: ...

@typing.type_check_only
class ListLiensResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListLiensResponse: ...

@typing.type_check_only
class ListOrgPoliciesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListOrgPoliciesResponse: ...

@typing.type_check_only
class ListProjectsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListProjectsResponse: ...

@typing.type_check_only
class OperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Operation: ...

@typing.type_check_only
class OrgPolicyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> OrgPolicy: ...

@typing.type_check_only
class OrganizationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Organization: ...

@typing.type_check_only
class PolicyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Policy: ...

@typing.type_check_only
class ProjectHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Project: ...

@typing.type_check_only
class SearchOrganizationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> SearchOrganizationsResponse: ...

@typing.type_check_only
class TestIamPermissionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> TestIamPermissionsResponse: ...
