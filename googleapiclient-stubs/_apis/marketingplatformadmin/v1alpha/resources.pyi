import collections.abc
import typing

import httplib2

import googleapiclient.discovery
import googleapiclient.http

from .schemas import *

_list = list

@typing.type_check_only
class GoogleMarketingPlatformAdminAPIResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class OrganizationsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class AdminAccessBindingsResource(googleapiclient.discovery.Resource):
            def create(
                self, *, parent: str, body: AdminAccessBinding, **kwargs: typing.Any
            ) -> AdminAccessBindingHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> AdminAccessBindingHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int | None = ...,
                pageToken: str | None = ...,
                **kwargs: typing.Any,
            ) -> ListAdminAccessBindingsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListAdminAccessBindingsResponseHttpRequest,
                previous_response: ListAdminAccessBindingsResponse,
            ) -> ListAdminAccessBindingsResponseHttpRequest | None: ...
            def patch(
                self,
                *,
                name: str,
                body: AdminAccessBinding,
                updateMask: str | None = ...,
                **kwargs: typing.Any,
            ) -> AdminAccessBindingHttpRequest: ...

        @typing.type_check_only
        class AnalyticsAccountLinksResource(googleapiclient.discovery.Resource):
            def create(
                self, *, parent: str, body: AnalyticsAccountLink, **kwargs: typing.Any
            ) -> AnalyticsAccountLinkHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int | None = ...,
                pageToken: str | None = ...,
                **kwargs: typing.Any,
            ) -> ListAnalyticsAccountLinksResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListAnalyticsAccountLinksResponseHttpRequest,
                previous_response: ListAnalyticsAccountLinksResponse,
            ) -> ListAnalyticsAccountLinksResponseHttpRequest | None: ...
            def setPropertyServiceLevel(
                self,
                *,
                analyticsAccountLink: str,
                body: SetPropertyServiceLevelRequest,
                **kwargs: typing.Any,
            ) -> SetPropertyServiceLevelResponseHttpRequest: ...

        @typing.type_check_only
        class UserGroupsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class MembersResource(googleapiclient.discovery.Resource):
                def create(
                    self, *, parent: str, body: UserGroupMember, **kwargs: typing.Any
                ) -> UserGroupMemberHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> UserGroupMemberHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int | None = ...,
                    pageToken: str | None = ...,
                    **kwargs: typing.Any,
                ) -> ListUserGroupMembersResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListUserGroupMembersResponseHttpRequest,
                    previous_response: ListUserGroupMembersResponse,
                ) -> ListUserGroupMembersResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: UserGroupMember,
                    updateMask: str | None = ...,
                    **kwargs: typing.Any,
                ) -> UserGroupMemberHttpRequest: ...

            def create(
                self, *, parent: str, body: UserGroup, **kwargs: typing.Any
            ) -> UserGroupHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> UserGroupHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int | None = ...,
                pageToken: str | None = ...,
                **kwargs: typing.Any,
            ) -> ListUserGroupsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListUserGroupsResponseHttpRequest,
                previous_response: ListUserGroupsResponse,
            ) -> ListUserGroupsResponseHttpRequest | None: ...
            def patch(
                self,
                *,
                name: str,
                body: UserGroup,
                updateMask: str | None = ...,
                **kwargs: typing.Any,
            ) -> UserGroupHttpRequest: ...
            def members(self) -> MembersResource: ...

        def findSalesPartnerManagedClients(
            self,
            *,
            organization: str,
            body: FindSalesPartnerManagedClientsRequest,
            **kwargs: typing.Any,
        ) -> FindSalesPartnerManagedClientsResponseHttpRequest: ...
        def get(
            self, *, name: str, **kwargs: typing.Any
        ) -> OrganizationHttpRequest: ...
        def list(
            self,
            *,
            pageSize: int | None = ...,
            pageToken: str | None = ...,
            **kwargs: typing.Any,
        ) -> ListOrganizationsResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: ListOrganizationsResponseHttpRequest,
            previous_response: ListOrganizationsResponse,
        ) -> ListOrganizationsResponseHttpRequest | None: ...
        def reportPropertyUsage(
            self,
            *,
            organization: str,
            body: ReportPropertyUsageRequest,
            **kwargs: typing.Any,
        ) -> ReportPropertyUsageResponseHttpRequest: ...
        def adminAccessBindings(self) -> AdminAccessBindingsResource: ...
        def analyticsAccountLinks(self) -> AnalyticsAccountLinksResource: ...
        def userGroups(self) -> UserGroupsResource: ...

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
    def organizations(self) -> OrganizationsResource: ...

@typing.type_check_only
class AdminAccessBindingHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> AdminAccessBinding: ...

@typing.type_check_only
class AnalyticsAccountLinkHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> AnalyticsAccountLink: ...

@typing.type_check_only
class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Empty: ...

@typing.type_check_only
class FindSalesPartnerManagedClientsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> FindSalesPartnerManagedClientsResponse: ...

@typing.type_check_only
class ListAdminAccessBindingsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListAdminAccessBindingsResponse: ...

@typing.type_check_only
class ListAnalyticsAccountLinksResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListAnalyticsAccountLinksResponse: ...

@typing.type_check_only
class ListOrganizationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListOrganizationsResponse: ...

@typing.type_check_only
class ListUserGroupMembersResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListUserGroupMembersResponse: ...

@typing.type_check_only
class ListUserGroupsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListUserGroupsResponse: ...

@typing.type_check_only
class OrganizationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Organization: ...

@typing.type_check_only
class ReportPropertyUsageResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ReportPropertyUsageResponse: ...

@typing.type_check_only
class SetPropertyServiceLevelResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> SetPropertyServiceLevelResponse: ...

@typing.type_check_only
class UserGroupHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> UserGroup: ...

@typing.type_check_only
class UserGroupMemberHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> UserGroupMember: ...
