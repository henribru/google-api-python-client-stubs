import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class CloudResourceManagerResource(googleapiclient.discovery.Resource):
    class ProjectsResource(googleapiclient.discovery.Resource):
        def update(
            self, *, projectId: str, body: Project = ..., **kwargs: typing.Any
        ) -> ProjectHttpRequest: ...
        def listAvailableOrgPolicyConstraints(
            self,
            *,
            resource: str,
            body: ListAvailableOrgPolicyConstraintsRequest = ...,
            **kwargs: typing.Any
        ) -> ListAvailableOrgPolicyConstraintsResponseHttpRequest: ...
        def create(
            self, *, body: Project = ..., **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def delete(
            self, *, projectId: str, **kwargs: typing.Any
        ) -> EmptyHttpRequest: ...
        def testIamPermissions(
            self,
            *,
            resource: str,
            body: TestIamPermissionsRequest = ...,
            **kwargs: typing.Any
        ) -> TestIamPermissionsResponseHttpRequest: ...
        def setOrgPolicy(
            self,
            *,
            resource: str,
            body: SetOrgPolicyRequest = ...,
            **kwargs: typing.Any
        ) -> OrgPolicyHttpRequest: ...
        def getAncestry(
            self,
            *,
            projectId: str,
            body: GetAncestryRequest = ...,
            **kwargs: typing.Any
        ) -> GetAncestryResponseHttpRequest: ...
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
        def setIamPolicy(
            self,
            *,
            resource: str,
            body: SetIamPolicyRequest = ...,
            **kwargs: typing.Any
        ) -> PolicyHttpRequest: ...
        def get(
            self, *, projectId: str, **kwargs: typing.Any
        ) -> ProjectHttpRequest: ...
        def undelete(
            self,
            *,
            projectId: str,
            body: UndeleteProjectRequest = ...,
            **kwargs: typing.Any
        ) -> EmptyHttpRequest: ...
        def list(
            self,
            *,
            pageSize: int = ...,
            filter: str = ...,
            pageToken: str = ...,
            **kwargs: typing.Any
        ) -> ListProjectsResponseHttpRequest: ...
        def getOrgPolicy(
            self,
            *,
            resource: str,
            body: GetOrgPolicyRequest = ...,
            **kwargs: typing.Any
        ) -> OrgPolicyHttpRequest: ...
        def getIamPolicy(
            self,
            *,
            resource: str,
            body: GetIamPolicyRequest = ...,
            **kwargs: typing.Any
        ) -> PolicyHttpRequest: ...
        def listOrgPolicies(
            self,
            *,
            resource: str,
            body: ListOrgPoliciesRequest = ...,
            **kwargs: typing.Any
        ) -> ListOrgPoliciesResponseHttpRequest: ...
    class FoldersResource(googleapiclient.discovery.Resource):
        def setOrgPolicy(
            self,
            *,
            resource: str,
            body: SetOrgPolicyRequest = ...,
            **kwargs: typing.Any
        ) -> OrgPolicyHttpRequest: ...
        def listOrgPolicies(
            self,
            *,
            resource: str,
            body: ListOrgPoliciesRequest = ...,
            **kwargs: typing.Any
        ) -> ListOrgPoliciesResponseHttpRequest: ...
        def getOrgPolicy(
            self,
            *,
            resource: str,
            body: GetOrgPolicyRequest = ...,
            **kwargs: typing.Any
        ) -> OrgPolicyHttpRequest: ...
        def getEffectiveOrgPolicy(
            self,
            *,
            resource: str,
            body: GetEffectiveOrgPolicyRequest = ...,
            **kwargs: typing.Any
        ) -> OrgPolicyHttpRequest: ...
        def clearOrgPolicy(
            self,
            *,
            resource: str,
            body: ClearOrgPolicyRequest = ...,
            **kwargs: typing.Any
        ) -> EmptyHttpRequest: ...
        def listAvailableOrgPolicyConstraints(
            self,
            *,
            resource: str,
            body: ListAvailableOrgPolicyConstraintsRequest = ...,
            **kwargs: typing.Any
        ) -> ListAvailableOrgPolicyConstraintsResponseHttpRequest: ...
    class OperationsResource(googleapiclient.discovery.Resource):
        def get(self, *, name: str, **kwargs: typing.Any) -> OperationHttpRequest: ...
    class LiensResource(googleapiclient.discovery.Resource):
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
        def create(
            self, *, body: Lien = ..., **kwargs: typing.Any
        ) -> LienHttpRequest: ...
    class OrganizationsResource(googleapiclient.discovery.Resource):
        def setOrgPolicy(
            self,
            *,
            resource: str,
            body: SetOrgPolicyRequest = ...,
            **kwargs: typing.Any
        ) -> OrgPolicyHttpRequest: ...
        def getOrgPolicy(
            self,
            *,
            resource: str,
            body: GetOrgPolicyRequest = ...,
            **kwargs: typing.Any
        ) -> OrgPolicyHttpRequest: ...
        def getIamPolicy(
            self,
            *,
            resource: str,
            body: GetIamPolicyRequest = ...,
            **kwargs: typing.Any
        ) -> PolicyHttpRequest: ...
        def setIamPolicy(
            self,
            *,
            resource: str,
            body: SetIamPolicyRequest = ...,
            **kwargs: typing.Any
        ) -> PolicyHttpRequest: ...
        def clearOrgPolicy(
            self,
            *,
            resource: str,
            body: ClearOrgPolicyRequest = ...,
            **kwargs: typing.Any
        ) -> EmptyHttpRequest: ...
        def search(
            self, *, body: SearchOrganizationsRequest = ..., **kwargs: typing.Any
        ) -> SearchOrganizationsResponseHttpRequest: ...
        def getEffectiveOrgPolicy(
            self,
            *,
            resource: str,
            body: GetEffectiveOrgPolicyRequest = ...,
            **kwargs: typing.Any
        ) -> OrgPolicyHttpRequest: ...
        def listAvailableOrgPolicyConstraints(
            self,
            *,
            resource: str,
            body: ListAvailableOrgPolicyConstraintsRequest = ...,
            **kwargs: typing.Any
        ) -> ListAvailableOrgPolicyConstraintsResponseHttpRequest: ...
        def listOrgPolicies(
            self,
            *,
            resource: str,
            body: ListOrgPoliciesRequest = ...,
            **kwargs: typing.Any
        ) -> ListOrgPoliciesResponseHttpRequest: ...
        def get(
            self, *, name: str, **kwargs: typing.Any
        ) -> OrganizationHttpRequest: ...
        def testIamPermissions(
            self,
            *,
            resource: str,
            body: TestIamPermissionsRequest = ...,
            **kwargs: typing.Any
        ) -> TestIamPermissionsResponseHttpRequest: ...
    def projects(self) -> ProjectsResource: ...
    def folders(self) -> FoldersResource: ...
    def operations(self) -> OperationsResource: ...
    def liens(self) -> LiensResource: ...
    def organizations(self) -> OrganizationsResource: ...

class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Empty: ...

class ListOrgPoliciesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListOrgPoliciesResponse: ...

class GetAncestryResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GetAncestryResponse: ...

class ListProjectsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListProjectsResponse: ...

class OperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Operation: ...

class OrgPolicyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> OrgPolicy: ...

class LienHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Lien: ...

class SearchOrganizationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> SearchOrganizationsResponse: ...

class ListLiensResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListLiensResponse: ...

class TestIamPermissionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> TestIamPermissionsResponse: ...

class OrganizationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Organization: ...

class ListAvailableOrgPolicyConstraintsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListAvailableOrgPolicyConstraintsResponse: ...

class PolicyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Policy: ...

class ProjectHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Project: ...
