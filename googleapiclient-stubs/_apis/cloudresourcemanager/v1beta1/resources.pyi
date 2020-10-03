import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class CloudResourceManagerResource(googleapiclient.discovery.Resource):
    class ProjectsResource(googleapiclient.discovery.Resource):
        def create(
            self,
            *,
            body: Project = ...,
            useLegacyStack: bool = ...,
            **kwargs: typing.Any
        ) -> ProjectHttpRequest: ...
        def get(
            self, *, projectId: str, **kwargs: typing.Any
        ) -> ProjectHttpRequest: ...
        def update(
            self, *, projectId: str, body: Project = ..., **kwargs: typing.Any
        ) -> ProjectHttpRequest: ...
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
        def getIamPolicy(
            self,
            *,
            resource: str,
            body: GetIamPolicyRequest = ...,
            **kwargs: typing.Any
        ) -> PolicyHttpRequest: ...
        def delete(
            self, *, projectId: str, **kwargs: typing.Any
        ) -> EmptyHttpRequest: ...
        def getAncestry(
            self,
            *,
            projectId: str,
            body: GetAncestryRequest = ...,
            **kwargs: typing.Any
        ) -> GetAncestryResponseHttpRequest: ...
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
            pageToken: str = ...,
            pageSize: int = ...,
            filter: str = ...,
            **kwargs: typing.Any
        ) -> ListProjectsResponseHttpRequest: ...
    class OrganizationsResource(googleapiclient.discovery.Resource):
        def get(
            self, *, name: str, organizationId: str = ..., **kwargs: typing.Any
        ) -> OrganizationHttpRequest: ...
        def testIamPermissions(
            self,
            *,
            resource: str,
            body: TestIamPermissionsRequest = ...,
            **kwargs: typing.Any
        ) -> TestIamPermissionsResponseHttpRequest: ...
        def update(
            self, *, name: str, body: Organization = ..., **kwargs: typing.Any
        ) -> OrganizationHttpRequest: ...
        def list(
            self,
            *,
            filter: str = ...,
            pageSize: int = ...,
            pageToken: str = ...,
            **kwargs: typing.Any
        ) -> ListOrganizationsResponseHttpRequest: ...
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
    def projects(self) -> ProjectsResource: ...
    def organizations(self) -> OrganizationsResource: ...

class ListOrganizationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListOrganizationsResponse: ...

class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Empty: ...

class ListProjectsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListProjectsResponse: ...

class GetAncestryResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GetAncestryResponse: ...

class TestIamPermissionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> TestIamPermissionsResponse: ...

class OrganizationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Organization: ...

class PolicyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Policy: ...

class ProjectHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Project: ...
