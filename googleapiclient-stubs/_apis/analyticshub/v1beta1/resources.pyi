import collections.abc
import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

_list = list

@typing.type_check_only
class AnalyticsHubResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class OrganizationsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class LocationsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class DataExchangesResource(googleapiclient.discovery.Resource):
                def list(
                    self,
                    *,
                    organization: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> ListOrgDataExchangesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListOrgDataExchangesResponseHttpRequest,
                    previous_response: ListOrgDataExchangesResponse,
                ) -> ListOrgDataExchangesResponseHttpRequest | None: ...

            def dataExchanges(self) -> DataExchangesResource: ...

        def locations(self) -> LocationsResource: ...

    @typing.type_check_only
    class ProjectsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class LocationsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class DataExchangesResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class ListingsResource(googleapiclient.discovery.Resource):
                    def create(
                        self,
                        *,
                        parent: str,
                        body: Listing = ...,
                        listingId: str = ...,
                        **kwargs: typing.Any
                    ) -> ListingHttpRequest: ...
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> EmptyHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> ListingHttpRequest: ...
                    def getIamPolicy(
                        self,
                        *,
                        resource: str,
                        body: GetIamPolicyRequest = ...,
                        **kwargs: typing.Any
                    ) -> PolicyHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any
                    ) -> ListListingsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: ListListingsResponseHttpRequest,
                        previous_response: ListListingsResponse,
                    ) -> ListListingsResponseHttpRequest | None: ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: Listing = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any
                    ) -> ListingHttpRequest: ...
                    def setIamPolicy(
                        self,
                        *,
                        resource: str,
                        body: SetIamPolicyRequest = ...,
                        **kwargs: typing.Any
                    ) -> PolicyHttpRequest: ...
                    def subscribe(
                        self,
                        *,
                        name: str,
                        body: SubscribeListingRequest = ...,
                        **kwargs: typing.Any
                    ) -> SubscribeListingResponseHttpRequest: ...
                    def testIamPermissions(
                        self,
                        *,
                        resource: str,
                        body: TestIamPermissionsRequest = ...,
                        **kwargs: typing.Any
                    ) -> TestIamPermissionsResponseHttpRequest: ...

                def create(
                    self,
                    *,
                    parent: str,
                    body: DataExchange = ...,
                    dataExchangeId: str = ...,
                    **kwargs: typing.Any
                ) -> DataExchangeHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> DataExchangeHttpRequest: ...
                def getIamPolicy(
                    self,
                    *,
                    resource: str,
                    body: GetIamPolicyRequest = ...,
                    **kwargs: typing.Any
                ) -> PolicyHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> ListDataExchangesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListDataExchangesResponseHttpRequest,
                    previous_response: ListDataExchangesResponse,
                ) -> ListDataExchangesResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: DataExchange = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any
                ) -> DataExchangeHttpRequest: ...
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
                def listings(self) -> ListingsResource: ...

            def dataExchanges(self) -> DataExchangesResource: ...

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
        | None = ...,
    ) -> googleapiclient.http.BatchHttpRequest: ...
    def organizations(self) -> OrganizationsResource: ...
    def projects(self) -> ProjectsResource: ...

@typing.type_check_only
class DataExchangeHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> DataExchange: ...

@typing.type_check_only
class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Empty: ...

@typing.type_check_only
class ListDataExchangesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListDataExchangesResponse: ...

@typing.type_check_only
class ListListingsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListListingsResponse: ...

@typing.type_check_only
class ListOrgDataExchangesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListOrgDataExchangesResponse: ...

@typing.type_check_only
class ListingHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Listing: ...

@typing.type_check_only
class PolicyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Policy: ...

@typing.type_check_only
class SubscribeListingResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> SubscribeListingResponse: ...

@typing.type_check_only
class TestIamPermissionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> TestIamPermissionsResponse: ...
