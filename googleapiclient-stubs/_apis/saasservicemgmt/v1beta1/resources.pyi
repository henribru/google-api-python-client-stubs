import collections.abc
import typing

import httplib2
import typing_extensions

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
            class ReleasesResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: Release = ...,
                    releaseId: str = ...,
                    requestId: str = ...,
                    validateOnly: bool = ...,
                    **kwargs: typing.Any,
                ) -> ReleaseHttpRequest: ...
                def delete(
                    self,
                    *,
                    name: str,
                    etag: str = ...,
                    requestId: str = ...,
                    validateOnly: bool = ...,
                    **kwargs: typing.Any,
                ) -> EmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> ReleaseHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
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
                    body: Release = ...,
                    requestId: str = ...,
                    updateMask: str = ...,
                    validateOnly: bool = ...,
                    **kwargs: typing.Any,
                ) -> ReleaseHttpRequest: ...

            @typing.type_check_only
            class RolloutKindsResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: RolloutKind = ...,
                    requestId: str = ...,
                    rolloutKindId: str = ...,
                    validateOnly: bool = ...,
                    **kwargs: typing.Any,
                ) -> RolloutKindHttpRequest: ...
                def delete(
                    self,
                    *,
                    name: str,
                    etag: str = ...,
                    requestId: str = ...,
                    validateOnly: bool = ...,
                    **kwargs: typing.Any,
                ) -> EmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> RolloutKindHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
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
                    body: RolloutKind = ...,
                    requestId: str = ...,
                    updateMask: str = ...,
                    validateOnly: bool = ...,
                    **kwargs: typing.Any,
                ) -> RolloutKindHttpRequest: ...

            @typing.type_check_only
            class RolloutsResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: Rollout = ...,
                    requestId: str = ...,
                    rolloutId: str = ...,
                    validateOnly: bool = ...,
                    **kwargs: typing.Any,
                ) -> RolloutHttpRequest: ...
                def delete(
                    self,
                    *,
                    name: str,
                    etag: str = ...,
                    requestId: str = ...,
                    validateOnly: bool = ...,
                    **kwargs: typing.Any,
                ) -> EmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> RolloutHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
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
                    body: Rollout = ...,
                    requestId: str = ...,
                    updateMask: str = ...,
                    validateOnly: bool = ...,
                    **kwargs: typing.Any,
                ) -> RolloutHttpRequest: ...

            @typing.type_check_only
            class SaasResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: Saas = ...,
                    requestId: str = ...,
                    saasId: str = ...,
                    validateOnly: bool = ...,
                    **kwargs: typing.Any,
                ) -> SaasHttpRequest: ...
                def delete(
                    self,
                    *,
                    name: str,
                    etag: str = ...,
                    requestId: str = ...,
                    validateOnly: bool = ...,
                    **kwargs: typing.Any,
                ) -> EmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> SaasHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
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
                    body: Saas = ...,
                    requestId: str = ...,
                    updateMask: str = ...,
                    validateOnly: bool = ...,
                    **kwargs: typing.Any,
                ) -> SaasHttpRequest: ...

            @typing.type_check_only
            class TenantsResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: Tenant = ...,
                    requestId: str = ...,
                    tenantId: str = ...,
                    validateOnly: bool = ...,
                    **kwargs: typing.Any,
                ) -> TenantHttpRequest: ...
                def delete(
                    self,
                    *,
                    name: str,
                    etag: str = ...,
                    requestId: str = ...,
                    validateOnly: bool = ...,
                    **kwargs: typing.Any,
                ) -> EmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> TenantHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
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
                    body: Tenant = ...,
                    requestId: str = ...,
                    updateMask: str = ...,
                    validateOnly: bool = ...,
                    **kwargs: typing.Any,
                ) -> TenantHttpRequest: ...

            @typing.type_check_only
            class UnitKindsResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: UnitKind = ...,
                    requestId: str = ...,
                    unitKindId: str = ...,
                    validateOnly: bool = ...,
                    **kwargs: typing.Any,
                ) -> UnitKindHttpRequest: ...
                def delete(
                    self,
                    *,
                    name: str,
                    etag: str = ...,
                    requestId: str = ...,
                    validateOnly: bool = ...,
                    **kwargs: typing.Any,
                ) -> EmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> UnitKindHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
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
                    body: UnitKind = ...,
                    requestId: str = ...,
                    updateMask: str = ...,
                    validateOnly: bool = ...,
                    **kwargs: typing.Any,
                ) -> UnitKindHttpRequest: ...

            @typing.type_check_only
            class UnitOperationsResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: UnitOperation = ...,
                    requestId: str = ...,
                    unitOperationId: str = ...,
                    validateOnly: bool = ...,
                    **kwargs: typing.Any,
                ) -> UnitOperationHttpRequest: ...
                def delete(
                    self,
                    *,
                    name: str,
                    etag: str = ...,
                    requestId: str = ...,
                    validateOnly: bool = ...,
                    **kwargs: typing.Any,
                ) -> EmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> UnitOperationHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
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
                    body: UnitOperation = ...,
                    requestId: str = ...,
                    updateMask: str = ...,
                    validateOnly: bool = ...,
                    **kwargs: typing.Any,
                ) -> UnitOperationHttpRequest: ...

            @typing.type_check_only
            class UnitsResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: Unit = ...,
                    requestId: str = ...,
                    unitId: str = ...,
                    validateOnly: bool = ...,
                    **kwargs: typing.Any,
                ) -> UnitHttpRequest: ...
                def delete(
                    self,
                    *,
                    name: str,
                    etag: str = ...,
                    requestId: str = ...,
                    validateOnly: bool = ...,
                    **kwargs: typing.Any,
                ) -> EmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> UnitHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
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
                    body: Unit = ...,
                    requestId: str = ...,
                    updateMask: str = ...,
                    validateOnly: bool = ...,
                    **kwargs: typing.Any,
                ) -> UnitHttpRequest: ...

            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleCloudLocationLocationHttpRequest: ...
            def list(
                self,
                *,
                name: str,
                extraLocationTypes: str | _list[str] = ...,
                filter: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any,
            ) -> ListLocationsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListLocationsResponseHttpRequest,
                previous_response: ListLocationsResponse,
            ) -> ListLocationsResponseHttpRequest | None: ...
            def releases(self) -> ReleasesResource: ...
            def rolloutKinds(self) -> RolloutKindsResource: ...
            def rollouts(self) -> RolloutsResource: ...
            def saas(self) -> SaasResource: ...
            def tenants(self) -> TenantsResource: ...
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
class GoogleCloudLocationLocationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudLocationLocation: ...

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
