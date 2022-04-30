import collections.abc
import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

_list = list

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
            def list_next(
                self,
                previous_request: ListGuestPoliciesResponseHttpRequest,
                previous_response: ListGuestPoliciesResponse,
            ) -> ListGuestPoliciesResponseHttpRequest | None: ...
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
            def list_next(
                self,
                previous_request: ListPatchDeploymentsResponseHttpRequest,
                previous_response: ListPatchDeploymentsResponse,
            ) -> ListPatchDeploymentsResponseHttpRequest | None: ...
            def patch(
                self,
                *,
                name: str,
                body: PatchDeployment = ...,
                updateMask: str = ...,
                **kwargs: typing.Any
            ) -> PatchDeploymentHttpRequest: ...
            def pause(
                self,
                *,
                name: str,
                body: PausePatchDeploymentRequest = ...,
                **kwargs: typing.Any
            ) -> PatchDeploymentHttpRequest: ...
            def resume(
                self,
                *,
                name: str,
                body: ResumePatchDeploymentRequest = ...,
                **kwargs: typing.Any
            ) -> PatchDeploymentHttpRequest: ...

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
                def list_next(
                    self,
                    previous_request: ListPatchJobInstanceDetailsResponseHttpRequest,
                    previous_response: ListPatchJobInstanceDetailsResponse,
                ) -> ListPatchJobInstanceDetailsResponseHttpRequest | None: ...

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
            def list_next(
                self,
                previous_request: ListPatchJobsResponseHttpRequest,
                previous_response: ListPatchJobsResponse,
            ) -> ListPatchJobsResponseHttpRequest | None: ...
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
    def projects(self) -> ProjectsResource: ...

@typing.type_check_only
class EffectiveGuestPolicyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> EffectiveGuestPolicy: ...

@typing.type_check_only
class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Empty: ...

@typing.type_check_only
class GuestPolicyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GuestPolicy: ...

@typing.type_check_only
class ListGuestPoliciesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListGuestPoliciesResponse: ...

@typing.type_check_only
class ListPatchDeploymentsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListPatchDeploymentsResponse: ...

@typing.type_check_only
class ListPatchJobInstanceDetailsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListPatchJobInstanceDetailsResponse: ...

@typing.type_check_only
class ListPatchJobsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListPatchJobsResponse: ...

@typing.type_check_only
class PatchDeploymentHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> PatchDeployment: ...

@typing.type_check_only
class PatchJobHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> PatchJob: ...
