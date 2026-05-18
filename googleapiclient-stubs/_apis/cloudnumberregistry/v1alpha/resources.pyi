import collections.abc
import typing

import httplib2
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http

from .schemas import *

_list = list

@typing.type_check_only
class CloudNumberRegistryResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class ProjectsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class LocationsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class CustomRangesResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: CustomRange = ...,
                    customRangeId: str = ...,
                    requestId: str = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def delete(
                    self,
                    *,
                    name: str,
                    force: bool = ...,
                    requestId: str = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def findFreeIpRanges(
                    self,
                    *,
                    name: str,
                    cidrPrefixLength: int = ...,
                    rangeCount: int = ...,
                    requestId: str = ...,
                    **kwargs: typing.Any,
                ) -> FindCustomRangeFreeIpRangesResponseHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> CustomRangeHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> ListCustomRangesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListCustomRangesResponseHttpRequest,
                    previous_response: ListCustomRangesResponse,
                ) -> ListCustomRangesResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: CustomRange = ...,
                    requestId: str = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def showUtilization(
                    self, *, name: str, **kwargs: typing.Any
                ) -> ShowCustomRangeUtilizationResponseHttpRequest: ...

            @typing.type_check_only
            class DiscoveredRangesResource(googleapiclient.discovery.Resource):
                def findFreeIpRanges(
                    self,
                    *,
                    name: str,
                    cidrPrefixLength: int = ...,
                    rangeCount: int = ...,
                    requestId: str = ...,
                    **kwargs: typing.Any,
                ) -> FindDiscoveredRangeFreeIpRangesResponseHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> DiscoveredRangeHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> ListDiscoveredRangesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListDiscoveredRangesResponseHttpRequest,
                    previous_response: ListDiscoveredRangesResponse,
                ) -> ListDiscoveredRangesResponseHttpRequest | None: ...
                def showUtilization(
                    self, *, name: str, **kwargs: typing.Any
                ) -> ShowDiscoveredRangeUtilizationResponseHttpRequest: ...

            @typing.type_check_only
            class IpamAdminScopesResource(googleapiclient.discovery.Resource):
                def checkAvailability(
                    self,
                    *,
                    parent: str,
                    scopes: str | _list[str] = ...,
                    **kwargs: typing.Any,
                ) -> CheckAvailabilityIpamAdminScopesResponseHttpRequest: ...
                def cleanup(
                    self,
                    *,
                    name: str,
                    body: CleanupIpamAdminScopeRequest = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def create(
                    self,
                    *,
                    parent: str,
                    body: IpamAdminScope = ...,
                    ipamAdminScopeId: str = ...,
                    requestId: str = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def delete(
                    self,
                    *,
                    name: str,
                    force: bool = ...,
                    requestId: str = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def disable(
                    self,
                    *,
                    name: str,
                    body: DisableIpamAdminScopeRequest = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> IpamAdminScopeHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> ListIpamAdminScopesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListIpamAdminScopesResponseHttpRequest,
                    previous_response: ListIpamAdminScopesResponse,
                ) -> ListIpamAdminScopesResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: IpamAdminScope = ...,
                    requestId: str = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...

            @typing.type_check_only
            class OperationsResource(googleapiclient.discovery.Resource):
                def cancel(
                    self,
                    *,
                    name: str,
                    body: CancelOperationRequest = ...,
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
                    filter: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    returnPartialSuccess: bool = ...,
                    **kwargs: typing.Any,
                ) -> ListOperationsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListOperationsResponseHttpRequest,
                    previous_response: ListOperationsResponse,
                ) -> ListOperationsResponseHttpRequest | None: ...

            @typing.type_check_only
            class RealmsResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: Realm = ...,
                    realmId: str = ...,
                    requestId: str = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def delete(
                    self,
                    *,
                    name: str,
                    force: bool = ...,
                    requestId: str = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def get(
                    self,
                    *,
                    name: str,
                    view: typing_extensions.Literal[
                        "REALM_VIEW_UNSPECIFIED", "BASIC", "FULL", "AGGREGATE"
                    ] = ...,
                    **kwargs: typing.Any,
                ) -> RealmHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    view: typing_extensions.Literal[
                        "REALM_VIEW_UNSPECIFIED", "BASIC", "FULL", "AGGREGATE"
                    ] = ...,
                    **kwargs: typing.Any,
                ) -> ListRealmsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListRealmsResponseHttpRequest,
                    previous_response: ListRealmsResponse,
                ) -> ListRealmsResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: Realm = ...,
                    requestId: str = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...

            @typing.type_check_only
            class RegistryBooksResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: RegistryBook = ...,
                    registryBookId: str = ...,
                    requestId: str = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def delete(
                    self,
                    *,
                    name: str,
                    force: bool = ...,
                    requestId: str = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def get(
                    self,
                    *,
                    name: str,
                    view: typing_extensions.Literal[
                        "REGISTRY_BOOK_VIEW_UNSPECIFIED", "BASIC", "FULL", "AGGREGATE"
                    ] = ...,
                    **kwargs: typing.Any,
                ) -> RegistryBookHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    view: typing_extensions.Literal[
                        "REGISTRY_BOOK_VIEW_UNSPECIFIED", "BASIC", "FULL", "AGGREGATE"
                    ] = ...,
                    **kwargs: typing.Any,
                ) -> ListRegistryBooksResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListRegistryBooksResponseHttpRequest,
                    previous_response: ListRegistryBooksResponse,
                ) -> ListRegistryBooksResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: RegistryBook = ...,
                    requestId: str = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def searchIpResources(
                    self,
                    *,
                    name: str,
                    body: SearchIpResourcesRequest = ...,
                    **kwargs: typing.Any,
                ) -> SearchIpResourcesResponseHttpRequest: ...
                def searchIpResources_next(
                    self,
                    previous_request: SearchIpResourcesResponseHttpRequest,
                    previous_response: SearchIpResourcesResponse,
                ) -> SearchIpResourcesResponseHttpRequest | None: ...

            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> LocationHttpRequest: ...
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
            def customRanges(self) -> CustomRangesResource: ...
            def discoveredRanges(self) -> DiscoveredRangesResource: ...
            def ipamAdminScopes(self) -> IpamAdminScopesResource: ...
            def operations(self) -> OperationsResource: ...
            def realms(self) -> RealmsResource: ...
            def registryBooks(self) -> RegistryBooksResource: ...

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
class CheckAvailabilityIpamAdminScopesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> CheckAvailabilityIpamAdminScopesResponse: ...

@typing.type_check_only
class CustomRangeHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> CustomRange: ...

@typing.type_check_only
class DiscoveredRangeHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> DiscoveredRange: ...

@typing.type_check_only
class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Empty: ...

@typing.type_check_only
class FindCustomRangeFreeIpRangesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> FindCustomRangeFreeIpRangesResponse: ...

@typing.type_check_only
class FindDiscoveredRangeFreeIpRangesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> FindDiscoveredRangeFreeIpRangesResponse: ...

@typing.type_check_only
class IpamAdminScopeHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> IpamAdminScope: ...

@typing.type_check_only
class ListCustomRangesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListCustomRangesResponse: ...

@typing.type_check_only
class ListDiscoveredRangesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListDiscoveredRangesResponse: ...

@typing.type_check_only
class ListIpamAdminScopesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListIpamAdminScopesResponse: ...

@typing.type_check_only
class ListLocationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListLocationsResponse: ...

@typing.type_check_only
class ListOperationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListOperationsResponse: ...

@typing.type_check_only
class ListRealmsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListRealmsResponse: ...

@typing.type_check_only
class ListRegistryBooksResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListRegistryBooksResponse: ...

@typing.type_check_only
class LocationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Location: ...

@typing.type_check_only
class OperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Operation: ...

@typing.type_check_only
class RealmHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Realm: ...

@typing.type_check_only
class RegistryBookHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> RegistryBook: ...

@typing.type_check_only
class SearchIpResourcesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> SearchIpResourcesResponse: ...

@typing.type_check_only
class ShowCustomRangeUtilizationResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ShowCustomRangeUtilizationResponse: ...

@typing.type_check_only
class ShowDiscoveredRangeUtilizationResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ShowDiscoveredRangeUtilizationResponse: ...
