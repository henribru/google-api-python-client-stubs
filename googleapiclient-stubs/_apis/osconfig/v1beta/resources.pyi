import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *
@typing.type_check_only
class OSConfigResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class ProjectsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class GuestPoliciesResource(googleapiclient.discovery.Resource):
            def create(
                self,
                *,
                parent: str,
                body: GuestPolicy = ...,
                guestPolicyId: str = ...,
                **kwargs: typing.Any
            ) -> GuestPolicyHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GuestPolicyHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> ListGuestPoliciesResponseHttpRequest: ...
            def patch(
                self,
                *,
                name: str,
                body: GuestPolicy = ...,
                updateMask: str = ...,
                **kwargs: typing.Any
            ) -> GuestPolicyHttpRequest: ...
        @typing.type_check_only
        class PatchDeploymentsResource(googleapiclient.discovery.Resource):
            def create(
                self,
                *,
                parent: str,
                body: PatchDeployment = ...,
                patchDeploymentId: str = ...,
                **kwargs: typing.Any
            ) -> PatchDeploymentHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> PatchDeploymentHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> ListPatchDeploymentsResponseHttpRequest: ...
        @typing.type_check_only
        class PatchJobsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class InstanceDetailsResource(googleapiclient.discovery.Resource):
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> ListPatchJobInstanceDetailsResponseHttpRequest: ...
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
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> PatchJobHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                filter: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> ListPatchJobsResponseHttpRequest: ...
            def instanceDetails(self) -> InstanceDetailsResource: ...
        @typing.type_check_only
        class ZonesResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class InstancesResource(googleapiclient.discovery.Resource):
                def lookupEffectiveGuestPolicy(
                    self,
                    *,
                    instance: str,
                    body: LookupEffectiveGuestPolicyRequest = ...,
                    **kwargs: typing.Any
                ) -> EffectiveGuestPolicyHttpRequest: ...
            def instances(self) -> InstancesResource: ...
        def guestPolicies(self) -> GuestPoliciesResource: ...
        def patchDeployments(self) -> PatchDeploymentsResource: ...
        def patchJobs(self) -> PatchJobsResource: ...
        def zones(self) -> ZonesResource: ...
    def projects(self) -> ProjectsResource: ...

@typing.type_check_only
class EffectiveGuestPolicyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> EffectiveGuestPolicy: ...

@typing.type_check_only
class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> Empty: ...

@typing.type_check_only
class GuestPolicyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GuestPolicy: ...

@typing.type_check_only
class ListGuestPoliciesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> ListGuestPoliciesResponse: ...

@typing.type_check_only
class ListPatchDeploymentsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> ListPatchDeploymentsResponse: ...

@typing.type_check_only
class ListPatchJobInstanceDetailsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> ListPatchJobInstanceDetailsResponse: ...

@typing.type_check_only
class ListPatchJobsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> ListPatchJobsResponse: ...

@typing.type_check_only
class PatchDeploymentHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> PatchDeployment: ...

@typing.type_check_only
class PatchJobHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> PatchJob: ...
