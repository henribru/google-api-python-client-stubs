import collections.abc
import typing

import httplib2
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http

from .schemas import *

_list = list

@typing.type_check_only
class DataManagerResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class AccountTypesResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class AccountsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class InsightsResource(googleapiclient.discovery.Resource):
                def retrieve(
                    self,
                    *,
                    parent: str,
                    body: RetrieveInsightsRequest = ...,
                    **kwargs: typing.Any,
                ) -> RetrieveInsightsResponseHttpRequest: ...

            @typing.type_check_only
            class PartnerLinksResource(googleapiclient.discovery.Resource):
                def create(
                    self, *, parent: str, body: PartnerLink = ..., **kwargs: typing.Any
                ) -> PartnerLinkHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def search(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> SearchPartnerLinksResponseHttpRequest: ...
                def search_next(
                    self,
                    previous_request: SearchPartnerLinksResponseHttpRequest,
                    previous_response: SearchPartnerLinksResponse,
                ) -> SearchPartnerLinksResponseHttpRequest | None: ...

            @typing.type_check_only
            class UserListDirectLicensesResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: UserListDirectLicense = ...,
                    **kwargs: typing.Any,
                ) -> UserListDirectLicenseHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> UserListDirectLicenseHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> ListUserListDirectLicensesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListUserListDirectLicensesResponseHttpRequest,
                    previous_response: ListUserListDirectLicensesResponse,
                ) -> ListUserListDirectLicensesResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: UserListDirectLicense = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> UserListDirectLicenseHttpRequest: ...

            @typing.type_check_only
            class UserListGlobalLicensesResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class UserListGlobalLicenseCustomerInfosResource(
                    googleapiclient.discovery.Resource
                ):
                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
                    ) -> ListUserListGlobalLicenseCustomerInfosResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: ListUserListGlobalLicenseCustomerInfosResponseHttpRequest,
                        previous_response: ListUserListGlobalLicenseCustomerInfosResponse,
                    ) -> (
                        ListUserListGlobalLicenseCustomerInfosResponseHttpRequest | None
                    ): ...

                def create(
                    self,
                    *,
                    parent: str,
                    body: UserListGlobalLicense = ...,
                    **kwargs: typing.Any,
                ) -> UserListGlobalLicenseHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> UserListGlobalLicenseHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> ListUserListGlobalLicensesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListUserListGlobalLicensesResponseHttpRequest,
                    previous_response: ListUserListGlobalLicensesResponse,
                ) -> ListUserListGlobalLicensesResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: UserListGlobalLicense = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> UserListGlobalLicenseHttpRequest: ...
                def userListGlobalLicenseCustomerInfos(
                    self,
                ) -> UserListGlobalLicenseCustomerInfosResource: ...

            @typing.type_check_only
            class UserListsResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: UserList = ...,
                    validateOnly: bool = ...,
                    **kwargs: typing.Any,
                ) -> UserListHttpRequest: ...
                def delete(
                    self, *, name: str, validateOnly: bool = ..., **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> UserListHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> ListUserListsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListUserListsResponseHttpRequest,
                    previous_response: ListUserListsResponse,
                ) -> ListUserListsResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: UserList = ...,
                    updateMask: str = ...,
                    validateOnly: bool = ...,
                    **kwargs: typing.Any,
                ) -> UserListHttpRequest: ...

            def insights(self) -> InsightsResource: ...
            def partnerLinks(self) -> PartnerLinksResource: ...
            def userListDirectLicenses(self) -> UserListDirectLicensesResource: ...
            def userListGlobalLicenses(self) -> UserListGlobalLicensesResource: ...
            def userLists(self) -> UserListsResource: ...

        def accounts(self) -> AccountsResource: ...

    @typing.type_check_only
    class AudienceMembersResource(googleapiclient.discovery.Resource):
        def ingest(
            self, *, body: IngestAudienceMembersRequest = ..., **kwargs: typing.Any
        ) -> IngestAudienceMembersResponseHttpRequest: ...
        def remove(
            self, *, body: RemoveAudienceMembersRequest = ..., **kwargs: typing.Any
        ) -> RemoveAudienceMembersResponseHttpRequest: ...

    @typing.type_check_only
    class EventsResource(googleapiclient.discovery.Resource):
        def ingest(
            self, *, body: IngestEventsRequest = ..., **kwargs: typing.Any
        ) -> IngestEventsResponseHttpRequest: ...

    @typing.type_check_only
    class RequestStatusResource(googleapiclient.discovery.Resource):
        def retrieve(
            self, *, requestId: str = ..., **kwargs: typing.Any
        ) -> RetrieveRequestStatusResponseHttpRequest: ...

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
    def accountTypes(self) -> AccountTypesResource: ...
    def audienceMembers(self) -> AudienceMembersResource: ...
    def events(self) -> EventsResource: ...
    def requestStatus(self) -> RequestStatusResource: ...

@typing.type_check_only
class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Empty: ...

@typing.type_check_only
class IngestAudienceMembersResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> IngestAudienceMembersResponse: ...

@typing.type_check_only
class IngestEventsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> IngestEventsResponse: ...

@typing.type_check_only
class ListUserListDirectLicensesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListUserListDirectLicensesResponse: ...

@typing.type_check_only
class ListUserListGlobalLicenseCustomerInfosResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListUserListGlobalLicenseCustomerInfosResponse: ...

@typing.type_check_only
class ListUserListGlobalLicensesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListUserListGlobalLicensesResponse: ...

@typing.type_check_only
class ListUserListsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListUserListsResponse: ...

@typing.type_check_only
class PartnerLinkHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> PartnerLink: ...

@typing.type_check_only
class RemoveAudienceMembersResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> RemoveAudienceMembersResponse: ...

@typing.type_check_only
class RetrieveInsightsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> RetrieveInsightsResponse: ...

@typing.type_check_only
class RetrieveRequestStatusResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> RetrieveRequestStatusResponse: ...

@typing.type_check_only
class SearchPartnerLinksResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> SearchPartnerLinksResponse: ...

@typing.type_check_only
class UserListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> UserList: ...

@typing.type_check_only
class UserListDirectLicenseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> UserListDirectLicense: ...

@typing.type_check_only
class UserListGlobalLicenseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> UserListGlobalLicense: ...
