import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class SystemsManagementResource(googleapiclient.discovery.Resource):
    class ProjectsResource(googleapiclient.discovery.Resource):
        class PatchJobsResource(googleapiclient.discovery.Resource):
            class InstanceDetailsResource(googleapiclient.discovery.Resource):
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    pageToken: str = ...,
                    pageSize: int = ...,
                    **kwargs: typing.Any
                ) -> ListPatchJobInstanceDetailsResponseHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                filter: str = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> ListPatchJobsResponseHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> PatchJobHttpRequest: ...
            def cancel(
                self,
                *,
                name: str,
                body: CancelPatchJobRequest = ...,
                **kwargs: typing.Any
            ) -> PatchJobHttpRequest: ...
            def execute(
                self,
                *,
                parent: str,
                body: ExecutePatchJobRequest = ...,
                **kwargs: typing.Any
            ) -> PatchJobHttpRequest: ...
            def instanceDetails(self) -> InstanceDetailsResource: ...
        class GuestPoliciesResource(googleapiclient.discovery.Resource):
            def list(
                self,
                *,
                parent: str,
                pageToken: str = ...,
                pageSize: int = ...,
                **kwargs: typing.Any
            ) -> ListGuestPoliciesResponseHttpRequest: ...
            def create(
                self,
                *,
                parent: str,
                body: GuestPolicy = ...,
                guestPolicyId: str = ...,
                **kwargs: typing.Any
            ) -> GuestPolicyHttpRequest: ...
            def patch(
                self,
                *,
                name: str,
                body: GuestPolicy = ...,
                updateMask: str = ...,
                **kwargs: typing.Any
            ) -> GuestPolicyHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GuestPolicyHttpRequest: ...
        class ZonesResource(googleapiclient.discovery.Resource):
            class InstancesResource(googleapiclient.discovery.Resource):
                def lookupEffectiveGuestPolicy(
                    self,
                    *,
                    instance: str,
                    body: LookupEffectiveGuestPolicyRequest = ...,
                    **kwargs: typing.Any
                ) -> EffectiveGuestPolicyHttpRequest: ...
            def instances(self) -> InstancesResource: ...
        class PatchDeploymentsResource(googleapiclient.discovery.Resource):
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> PatchDeploymentHttpRequest: ...
            def create(
                self,
                *,
                parent: str,
                body: PatchDeployment = ...,
                patchDeploymentId: str = ...,
                **kwargs: typing.Any
            ) -> PatchDeploymentHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageToken: str = ...,
                pageSize: int = ...,
                **kwargs: typing.Any
            ) -> ListPatchDeploymentsResponseHttpRequest: ...
        def patchJobs(self) -> PatchJobsResource: ...
        def guestPolicies(self) -> GuestPoliciesResource: ...
        def zones(self) -> ZonesResource: ...
        def patchDeployments(self) -> PatchDeploymentsResource: ...
    def projects(self) -> ProjectsResource: ...

class ListGuestPoliciesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListGuestPoliciesResponse: ...

class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Empty: ...

class ListPatchDeploymentsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListPatchDeploymentsResponse: ...

class PatchJobHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> PatchJob: ...

class EffectiveGuestPolicyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> EffectiveGuestPolicy: ...

class PatchDeploymentHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> PatchDeployment: ...

class ListPatchJobInstanceDetailsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListPatchJobInstanceDetailsResponse: ...

class ListPatchJobsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListPatchJobsResponse: ...

class GuestPolicyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GuestPolicy: ...
