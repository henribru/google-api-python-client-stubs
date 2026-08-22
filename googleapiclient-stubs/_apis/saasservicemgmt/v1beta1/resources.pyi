import collections.abc
import typing

import httplib2

import googleapiclient.discovery
import googleapiclient.http

from .schemas import *

_list = list

@typing.type_check_only
class SaaSServiceManagementResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class ProjectsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class LocationsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class FlagAttributesResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: FlagAttribute,
                    flagAttributeId: str | None = ...,
                    requestId: str | None = ...,
                    validateOnly: bool | None = ...,
                    **kwargs: typing.Any,
                ) -> FlagAttributeHttpRequest: ...
                def delete(
                    self,
                    *,
                    name: str,
                    etag: str | None = ...,
                    requestId: str | None = ...,
                    validateOnly: bool | None = ...,
                    **kwargs: typing.Any,
                ) -> EmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> FlagAttributeHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str | None = ...,
                    orderBy: str | None = ...,
                    pageSize: int | None = ...,
                    pageToken: str | None = ...,
                    **kwargs: typing.Any,
                ) -> ListFlagAttributesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListFlagAttributesResponseHttpRequest,
                    previous_response: ListFlagAttributesResponse,
                ) -> ListFlagAttributesResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: FlagAttribute,
                    requestId: str | None = ...,
                    updateMask: str | None = ...,
                    validateOnly: bool | None = ...,
                    **kwargs: typing.Any,
                ) -> FlagAttributeHttpRequest: ...

            @typing.type_check_only
            class FlagReleasesResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: FlagRelease,
                    flagReleaseId: str | None = ...,
                    requestId: str | None = ...,
                    validateOnly: bool | None = ...,
                    **kwargs: typing.Any,
                ) -> FlagReleaseHttpRequest: ...
                def delete(
                    self,
                    *,
                    name: str,
                    etag: str | None = ...,
                    requestId: str | None = ...,
                    validateOnly: bool | None = ...,
                    **kwargs: typing.Any,
                ) -> EmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> FlagReleaseHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str | None = ...,
                    orderBy: str | None = ...,
                    pageSize: int | None = ...,
                    pageToken: str | None = ...,
                    **kwargs: typing.Any,
                ) -> ListFlagReleasesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListFlagReleasesResponseHttpRequest,
                    previous_response: ListFlagReleasesResponse,
                ) -> ListFlagReleasesResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: FlagRelease,
                    requestId: str | None = ...,
                    updateMask: str | None = ...,
                    validateOnly: bool | None = ...,
                    **kwargs: typing.Any,
                ) -> FlagReleaseHttpRequest: ...

            @typing.type_check_only
            class FlagRevisionsResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: FlagRevision,
                    flagRevisionId: str | None = ...,
                    requestId: str | None = ...,
                    validateOnly: bool | None = ...,
                    **kwargs: typing.Any,
                ) -> FlagRevisionHttpRequest: ...
                def delete(
                    self,
                    *,
                    name: str,
                    etag: str | None = ...,
                    requestId: str | None = ...,
                    validateOnly: bool | None = ...,
                    **kwargs: typing.Any,
                ) -> EmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> FlagRevisionHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str | None = ...,
                    orderBy: str | None = ...,
                    pageSize: int | None = ...,
                    pageToken: str | None = ...,
                    **kwargs: typing.Any,
                ) -> ListFlagRevisionsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListFlagRevisionsResponseHttpRequest,
                    previous_response: ListFlagRevisionsResponse,
                ) -> ListFlagRevisionsResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: FlagRevision,
                    requestId: str | None = ...,
                    updateMask: str | None = ...,
                    validateOnly: bool | None = ...,
                    **kwargs: typing.Any,
                ) -> FlagRevisionHttpRequest: ...

            @typing.type_check_only
            class FlagsResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: Flag,
                    flagId: str | None = ...,
                    requestId: str | None = ...,
                    validateOnly: bool | None = ...,
                    **kwargs: typing.Any,
                ) -> FlagHttpRequest: ...
                def delete(
                    self,
                    *,
                    name: str,
                    etag: str | None = ...,
                    requestId: str | None = ...,
                    validateOnly: bool | None = ...,
                    **kwargs: typing.Any,
                ) -> EmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> FlagHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str | None = ...,
                    orderBy: str | None = ...,
                    pageSize: int | None = ...,
                    pageToken: str | None = ...,
                    **kwargs: typing.Any,
                ) -> ListFlagsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListFlagsResponseHttpRequest,
                    previous_response: ListFlagsResponse,
                ) -> ListFlagsResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: Flag,
                    requestId: str | None = ...,
                    updateMask: str | None = ...,
                    validateOnly: bool | None = ...,
                    **kwargs: typing.Any,
                ) -> FlagHttpRequest: ...

            @typing.type_check_only
            class ReleasesResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: Release,
                    releaseId: str | None = ...,
                    requestId: str | None = ...,
                    validateOnly: bool | None = ...,
                    **kwargs: typing.Any,
                ) -> ReleaseHttpRequest: ...
                def delete(
                    self,
                    *,
                    name: str,
                    etag: str | None = ...,
                    requestId: str | None = ...,
                    validateOnly: bool | None = ...,
                    **kwargs: typing.Any,
                ) -> EmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> ReleaseHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str | None = ...,
                    orderBy: str | None = ...,
                    pageSize: int | None = ...,
                    pageToken: str | None = ...,
                    **kwargs: typing.Any,
                ) -> ListReleasesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListReleasesResponseHttpRequest,
                    previous_response: ListReleasesResponse,
                ) -> ListReleasesResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: Release,
                    requestId: str | None = ...,
                    updateMask: str | None = ...,
                    validateOnly: bool | None = ...,
                    **kwargs: typing.Any,
                ) -> ReleaseHttpRequest: ...

            @typing.type_check_only
            class RolloutKindsResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: RolloutKind,
                    requestId: str | None = ...,
                    rolloutKindId: str | None = ...,
                    validateOnly: bool | None = ...,
                    **kwargs: typing.Any,
                ) -> RolloutKindHttpRequest: ...
                def delete(
                    self,
                    *,
                    name: str,
                    etag: str | None = ...,
                    requestId: str | None = ...,
                    validateOnly: bool | None = ...,
                    **kwargs: typing.Any,
                ) -> EmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> RolloutKindHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str | None = ...,
                    orderBy: str | None = ...,
                    pageSize: int | None = ...,
                    pageToken: str | None = ...,
                    **kwargs: typing.Any,
                ) -> ListRolloutKindsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListRolloutKindsResponseHttpRequest,
                    previous_response: ListRolloutKindsResponse,
                ) -> ListRolloutKindsResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: RolloutKind,
                    requestId: str | None = ...,
                    updateMask: str | None = ...,
                    validateOnly: bool | None = ...,
                    **kwargs: typing.Any,
                ) -> RolloutKindHttpRequest: ...

            @typing.type_check_only
            class RolloutsResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: Rollout,
                    requestId: str | None = ...,
                    rolloutId: str | None = ...,
                    validateOnly: bool | None = ...,
                    **kwargs: typing.Any,
                ) -> RolloutHttpRequest: ...
                def delete(
                    self,
                    *,
                    name: str,
                    etag: str | None = ...,
                    requestId: str | None = ...,
                    validateOnly: bool | None = ...,
                    **kwargs: typing.Any,
                ) -> EmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> RolloutHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str | None = ...,
                    orderBy: str | None = ...,
                    pageSize: int | None = ...,
                    pageToken: str | None = ...,
                    **kwargs: typing.Any,
                ) -> ListRolloutsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListRolloutsResponseHttpRequest,
                    previous_response: ListRolloutsResponse,
                ) -> ListRolloutsResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: Rollout,
                    requestId: str | None = ...,
                    updateMask: str | None = ...,
                    validateOnly: bool | None = ...,
                    **kwargs: typing.Any,
                ) -> RolloutHttpRequest: ...

            @typing.type_check_only
            class SaasResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: Saas,
                    requestId: str | None = ...,
                    saasId: str | None = ...,
                    validateOnly: bool | None = ...,
                    **kwargs: typing.Any,
                ) -> SaasHttpRequest: ...
                def delete(
                    self,
                    *,
                    name: str,
                    etag: str | None = ...,
                    requestId: str | None = ...,
                    validateOnly: bool | None = ...,
                    **kwargs: typing.Any,
                ) -> EmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> SaasHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str | None = ...,
                    orderBy: str | None = ...,
                    pageSize: int | None = ...,
                    pageToken: str | None = ...,
                    **kwargs: typing.Any,
                ) -> ListSaasResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListSaasResponseHttpRequest,
                    previous_response: ListSaasResponse,
                ) -> ListSaasResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: Saas,
                    requestId: str | None = ...,
                    updateMask: str | None = ...,
                    validateOnly: bool | None = ...,
                    **kwargs: typing.Any,
                ) -> SaasHttpRequest: ...

            @typing.type_check_only
            class SaasReleasesResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: SaasRelease,
                    requestId: str | None = ...,
                    saasReleaseId: str | None = ...,
                    validateOnly: bool | None = ...,
                    **kwargs: typing.Any,
                ) -> SaasReleaseHttpRequest: ...
                def delete(
                    self,
                    *,
                    name: str,
                    etag: str | None = ...,
                    requestId: str | None = ...,
                    validateOnly: bool | None = ...,
                    **kwargs: typing.Any,
                ) -> EmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> SaasReleaseHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str | None = ...,
                    orderBy: str | None = ...,
                    pageSize: int | None = ...,
                    pageToken: str | None = ...,
                    **kwargs: typing.Any,
                ) -> ListSaasReleasesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListSaasReleasesResponseHttpRequest,
                    previous_response: ListSaasReleasesResponse,
                ) -> ListSaasReleasesResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: SaasRelease,
                    requestId: str | None = ...,
                    updateMask: str | None = ...,
                    validateOnly: bool | None = ...,
                    **kwargs: typing.Any,
                ) -> SaasReleaseHttpRequest: ...

            @typing.type_check_only
            class TenantsResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: Tenant,
                    requestId: str | None = ...,
                    tenantId: str | None = ...,
                    validateOnly: bool | None = ...,
                    **kwargs: typing.Any,
                ) -> TenantHttpRequest: ...
                def delete(
                    self,
                    *,
                    name: str,
                    etag: str | None = ...,
                    requestId: str | None = ...,
                    validateOnly: bool | None = ...,
                    **kwargs: typing.Any,
                ) -> EmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> TenantHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str | None = ...,
                    orderBy: str | None = ...,
                    pageSize: int | None = ...,
                    pageToken: str | None = ...,
                    **kwargs: typing.Any,
                ) -> ListTenantsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListTenantsResponseHttpRequest,
                    previous_response: ListTenantsResponse,
                ) -> ListTenantsResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: Tenant,
                    requestId: str | None = ...,
                    updateMask: str | None = ...,
                    validateOnly: bool | None = ...,
                    **kwargs: typing.Any,
                ) -> TenantHttpRequest: ...

            @typing.type_check_only
            class UnitGroupOperationsResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: UnitGroupOperation,
                    requestId: str | None = ...,
                    unitGroupOperationId: str | None = ...,
                    validateOnly: bool | None = ...,
                    **kwargs: typing.Any,
                ) -> UnitGroupOperationHttpRequest: ...
                def delete(
                    self,
                    *,
                    name: str,
                    etag: str | None = ...,
                    requestId: str | None = ...,
                    validateOnly: bool | None = ...,
                    **kwargs: typing.Any,
                ) -> EmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> UnitGroupOperationHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str | None = ...,
                    orderBy: str | None = ...,
                    pageSize: int | None = ...,
                    pageToken: str | None = ...,
                    **kwargs: typing.Any,
                ) -> ListUnitGroupOperationsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListUnitGroupOperationsResponseHttpRequest,
                    previous_response: ListUnitGroupOperationsResponse,
                ) -> ListUnitGroupOperationsResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: UnitGroupOperation,
                    requestId: str | None = ...,
                    updateMask: str | None = ...,
                    validateOnly: bool | None = ...,
                    **kwargs: typing.Any,
                ) -> UnitGroupOperationHttpRequest: ...

            @typing.type_check_only
            class UnitGroupsResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: UnitGroup,
                    requestId: str | None = ...,
                    unitGroupId: str | None = ...,
                    validateOnly: bool | None = ...,
                    **kwargs: typing.Any,
                ) -> UnitGroupHttpRequest: ...
                def delete(
                    self,
                    *,
                    name: str,
                    etag: str | None = ...,
                    requestId: str | None = ...,
                    validateOnly: bool | None = ...,
                    **kwargs: typing.Any,
                ) -> EmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> UnitGroupHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str | None = ...,
                    orderBy: str | None = ...,
                    pageSize: int | None = ...,
                    pageToken: str | None = ...,
                    **kwargs: typing.Any,
                ) -> ListUnitGroupsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListUnitGroupsResponseHttpRequest,
                    previous_response: ListUnitGroupsResponse,
                ) -> ListUnitGroupsResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: UnitGroup,
                    requestId: str | None = ...,
                    updateMask: str | None = ...,
                    validateOnly: bool | None = ...,
                    **kwargs: typing.Any,
                ) -> UnitGroupHttpRequest: ...

            @typing.type_check_only
            class UnitKindsResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: UnitKind,
                    requestId: str | None = ...,
                    unitKindId: str | None = ...,
                    validateOnly: bool | None = ...,
                    **kwargs: typing.Any,
                ) -> UnitKindHttpRequest: ...
                def delete(
                    self,
                    *,
                    name: str,
                    etag: str | None = ...,
                    requestId: str | None = ...,
                    validateOnly: bool | None = ...,
                    **kwargs: typing.Any,
                ) -> EmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> UnitKindHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str | None = ...,
                    orderBy: str | None = ...,
                    pageSize: int | None = ...,
                    pageToken: str | None = ...,
                    **kwargs: typing.Any,
                ) -> ListUnitKindsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListUnitKindsResponseHttpRequest,
                    previous_response: ListUnitKindsResponse,
                ) -> ListUnitKindsResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: UnitKind,
                    requestId: str | None = ...,
                    updateMask: str | None = ...,
                    validateOnly: bool | None = ...,
                    **kwargs: typing.Any,
                ) -> UnitKindHttpRequest: ...

            @typing.type_check_only
            class UnitOperationsResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: UnitOperation,
                    requestId: str | None = ...,
                    unitOperationId: str | None = ...,
                    validateOnly: bool | None = ...,
                    **kwargs: typing.Any,
                ) -> UnitOperationHttpRequest: ...
                def delete(
                    self,
                    *,
                    name: str,
                    etag: str | None = ...,
                    requestId: str | None = ...,
                    validateOnly: bool | None = ...,
                    **kwargs: typing.Any,
                ) -> EmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> UnitOperationHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str | None = ...,
                    orderBy: str | None = ...,
                    pageSize: int | None = ...,
                    pageToken: str | None = ...,
                    **kwargs: typing.Any,
                ) -> ListUnitOperationsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListUnitOperationsResponseHttpRequest,
                    previous_response: ListUnitOperationsResponse,
                ) -> ListUnitOperationsResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: UnitOperation,
                    requestId: str | None = ...,
                    updateMask: str | None = ...,
                    validateOnly: bool | None = ...,
                    **kwargs: typing.Any,
                ) -> UnitOperationHttpRequest: ...

            @typing.type_check_only
            class UnitsResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: Unit,
                    requestId: str | None = ...,
                    unitId: str | None = ...,
                    validateOnly: bool | None = ...,
                    **kwargs: typing.Any,
                ) -> UnitHttpRequest: ...
                def delete(
                    self,
                    *,
                    name: str,
                    etag: str | None = ...,
                    requestId: str | None = ...,
                    validateOnly: bool | None = ...,
                    **kwargs: typing.Any,
                ) -> EmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> UnitHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str | None = ...,
                    orderBy: str | None = ...,
                    pageSize: int | None = ...,
                    pageToken: str | None = ...,
                    **kwargs: typing.Any,
                ) -> ListUnitsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListUnitsResponseHttpRequest,
                    previous_response: ListUnitsResponse,
                ) -> ListUnitsResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: Unit,
                    requestId: str | None = ...,
                    updateMask: str | None = ...,
                    validateOnly: bool | None = ...,
                    **kwargs: typing.Any,
                ) -> UnitHttpRequest: ...

            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleCloudLocationLocationHttpRequest: ...
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
            def flagAttributes(self) -> FlagAttributesResource: ...
            def flagReleases(self) -> FlagReleasesResource: ...
            def flagRevisions(self) -> FlagRevisionsResource: ...
            def flags(self) -> FlagsResource: ...
            def releases(self) -> ReleasesResource: ...
            def rolloutKinds(self) -> RolloutKindsResource: ...
            def rollouts(self) -> RolloutsResource: ...
            def saas(self) -> SaasResource: ...
            def saasReleases(self) -> SaasReleasesResource: ...
            def tenants(self) -> TenantsResource: ...
            def unitGroupOperations(self) -> UnitGroupOperationsResource: ...
            def unitGroups(self) -> UnitGroupsResource: ...
            def unitKinds(self) -> UnitKindsResource: ...
            def unitOperations(self) -> UnitOperationsResource: ...
            def units(self) -> UnitsResource: ...

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
    def projects(self) -> ProjectsResource: ...

@typing.type_check_only
class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Empty: ...

@typing.type_check_only
class FlagHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Flag: ...

@typing.type_check_only
class FlagAttributeHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> FlagAttribute: ...

@typing.type_check_only
class FlagReleaseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> FlagRelease: ...

@typing.type_check_only
class FlagRevisionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> FlagRevision: ...

@typing.type_check_only
class GoogleCloudLocationLocationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudLocationLocation: ...

@typing.type_check_only
class ListFlagAttributesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListFlagAttributesResponse: ...

@typing.type_check_only
class ListFlagReleasesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListFlagReleasesResponse: ...

@typing.type_check_only
class ListFlagRevisionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListFlagRevisionsResponse: ...

@typing.type_check_only
class ListFlagsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListFlagsResponse: ...

@typing.type_check_only
class ListLocationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListLocationsResponse: ...

@typing.type_check_only
class ListReleasesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListReleasesResponse: ...

@typing.type_check_only
class ListRolloutKindsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListRolloutKindsResponse: ...

@typing.type_check_only
class ListRolloutsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListRolloutsResponse: ...

@typing.type_check_only
class ListSaasReleasesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListSaasReleasesResponse: ...

@typing.type_check_only
class ListSaasResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListSaasResponse: ...

@typing.type_check_only
class ListTenantsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListTenantsResponse: ...

@typing.type_check_only
class ListUnitGroupOperationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListUnitGroupOperationsResponse: ...

@typing.type_check_only
class ListUnitGroupsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListUnitGroupsResponse: ...

@typing.type_check_only
class ListUnitKindsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListUnitKindsResponse: ...

@typing.type_check_only
class ListUnitOperationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListUnitOperationsResponse: ...

@typing.type_check_only
class ListUnitsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListUnitsResponse: ...

@typing.type_check_only
class ReleaseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Release: ...

@typing.type_check_only
class RolloutHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Rollout: ...

@typing.type_check_only
class RolloutKindHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> RolloutKind: ...

@typing.type_check_only
class SaasHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Saas: ...

@typing.type_check_only
class SaasReleaseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> SaasRelease: ...

@typing.type_check_only
class TenantHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Tenant: ...

@typing.type_check_only
class UnitHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Unit: ...

@typing.type_check_only
class UnitGroupHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> UnitGroup: ...

@typing.type_check_only
class UnitGroupOperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> UnitGroupOperation: ...

@typing.type_check_only
class UnitKindHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> UnitKind: ...

@typing.type_check_only
class UnitOperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> UnitOperation: ...
