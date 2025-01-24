import collections.abc
import typing

import httplib2
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http

from .schemas import *

_list = list

@typing.type_check_only
class CloudIdentityResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class CustomersResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class UserinvitationsResource(googleapiclient.discovery.Resource):
            def cancel(
                self,
                *,
                name: str,
                body: CancelUserInvitationRequest = ...,
                **kwargs: typing.Any,
            ) -> OperationHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> UserInvitationHttpRequest: ...
            def isInvitableUser(
                self, *, name: str, **kwargs: typing.Any
            ) -> IsInvitableUserResponseHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                filter: str = ...,
                orderBy: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any,
            ) -> ListUserInvitationsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListUserInvitationsResponseHttpRequest,
                previous_response: ListUserInvitationsResponse,
            ) -> ListUserInvitationsResponseHttpRequest | None: ...
            def send(
                self,
                *,
                name: str,
                body: SendUserInvitationRequest = ...,
                **kwargs: typing.Any,
            ) -> OperationHttpRequest: ...

        def userinvitations(self) -> UserinvitationsResource: ...

    @typing.type_check_only
    class DevicesResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class DeviceUsersResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class ClientStatesResource(googleapiclient.discovery.Resource):
                def get(
                    self, *, name: str, customer: str = ..., **kwargs: typing.Any
                ) -> GoogleAppsCloudidentityDevicesV1ClientStateHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    customer: str = ...,
                    filter: str = ...,
                    orderBy: str = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> (
                    GoogleAppsCloudidentityDevicesV1ListClientStatesResponseHttpRequest
                ): ...
                def list_next(
                    self,
                    previous_request: GoogleAppsCloudidentityDevicesV1ListClientStatesResponseHttpRequest,
                    previous_response: GoogleAppsCloudidentityDevicesV1ListClientStatesResponse,
                ) -> (
                    GoogleAppsCloudidentityDevicesV1ListClientStatesResponseHttpRequest
                    | None
                ): ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleAppsCloudidentityDevicesV1ClientState = ...,
                    customer: str = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...

            def approve(
                self,
                *,
                name: str,
                body: GoogleAppsCloudidentityDevicesV1ApproveDeviceUserRequest = ...,
                **kwargs: typing.Any,
            ) -> OperationHttpRequest: ...
            def block(
                self,
                *,
                name: str,
                body: GoogleAppsCloudidentityDevicesV1BlockDeviceUserRequest = ...,
                **kwargs: typing.Any,
            ) -> OperationHttpRequest: ...
            def cancelWipe(
                self,
                *,
                name: str,
                body: GoogleAppsCloudidentityDevicesV1CancelWipeDeviceUserRequest = ...,
                **kwargs: typing.Any,
            ) -> OperationHttpRequest: ...
            def delete(
                self, *, name: str, customer: str = ..., **kwargs: typing.Any
            ) -> OperationHttpRequest: ...
            def get(
                self, *, name: str, customer: str = ..., **kwargs: typing.Any
            ) -> GoogleAppsCloudidentityDevicesV1DeviceUserHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                customer: str = ...,
                filter: str = ...,
                orderBy: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any,
            ) -> GoogleAppsCloudidentityDevicesV1ListDeviceUsersResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: GoogleAppsCloudidentityDevicesV1ListDeviceUsersResponseHttpRequest,
                previous_response: GoogleAppsCloudidentityDevicesV1ListDeviceUsersResponse,
            ) -> (
                GoogleAppsCloudidentityDevicesV1ListDeviceUsersResponseHttpRequest
                | None
            ): ...
            def lookup(
                self,
                *,
                parent: str,
                androidId: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                rawResourceId: str = ...,
                userId: str = ...,
                **kwargs: typing.Any,
            ) -> (
                GoogleAppsCloudidentityDevicesV1LookupSelfDeviceUsersResponseHttpRequest
            ): ...
            def lookup_next(
                self,
                previous_request: GoogleAppsCloudidentityDevicesV1LookupSelfDeviceUsersResponseHttpRequest,
                previous_response: GoogleAppsCloudidentityDevicesV1LookupSelfDeviceUsersResponse,
            ) -> (
                GoogleAppsCloudidentityDevicesV1LookupSelfDeviceUsersResponseHttpRequest
                | None
            ): ...
            def wipe(
                self,
                *,
                name: str,
                body: GoogleAppsCloudidentityDevicesV1WipeDeviceUserRequest = ...,
                **kwargs: typing.Any,
            ) -> OperationHttpRequest: ...
            def clientStates(self) -> ClientStatesResource: ...

        def cancelWipe(
            self,
            *,
            name: str,
            body: GoogleAppsCloudidentityDevicesV1CancelWipeDeviceRequest = ...,
            **kwargs: typing.Any,
        ) -> OperationHttpRequest: ...
        def create(
            self,
            *,
            body: GoogleAppsCloudidentityDevicesV1Device = ...,
            customer: str = ...,
            **kwargs: typing.Any,
        ) -> OperationHttpRequest: ...
        def delete(
            self, *, name: str, customer: str = ..., **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def get(
            self, *, name: str, customer: str = ..., **kwargs: typing.Any
        ) -> GoogleAppsCloudidentityDevicesV1DeviceHttpRequest: ...
        def list(
            self,
            *,
            customer: str = ...,
            filter: str = ...,
            orderBy: str = ...,
            pageSize: int = ...,
            pageToken: str = ...,
            view: typing_extensions.Literal[
                "VIEW_UNSPECIFIED", "COMPANY_INVENTORY", "USER_ASSIGNED_DEVICES"
            ] = ...,
            **kwargs: typing.Any,
        ) -> GoogleAppsCloudidentityDevicesV1ListDevicesResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: GoogleAppsCloudidentityDevicesV1ListDevicesResponseHttpRequest,
            previous_response: GoogleAppsCloudidentityDevicesV1ListDevicesResponse,
        ) -> GoogleAppsCloudidentityDevicesV1ListDevicesResponseHttpRequest | None: ...
        def wipe(
            self,
            *,
            name: str,
            body: GoogleAppsCloudidentityDevicesV1WipeDeviceRequest = ...,
            **kwargs: typing.Any,
        ) -> OperationHttpRequest: ...
        def deviceUsers(self) -> DeviceUsersResource: ...

    @typing.type_check_only
    class GroupsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class MembershipsResource(googleapiclient.discovery.Resource):
            def checkTransitiveMembership(
                self, *, parent: str, query: str = ..., **kwargs: typing.Any
            ) -> CheckTransitiveMembershipResponseHttpRequest: ...
            def create(
                self, *, parent: str, body: Membership = ..., **kwargs: typing.Any
            ) -> OperationHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> OperationHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> MembershipHttpRequest: ...
            def getMembershipGraph(
                self, *, parent: str, query: str = ..., **kwargs: typing.Any
            ) -> OperationHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                view: typing_extensions.Literal[
                    "VIEW_UNSPECIFIED", "BASIC", "FULL"
                ] = ...,
                **kwargs: typing.Any,
            ) -> ListMembershipsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListMembershipsResponseHttpRequest,
                previous_response: ListMembershipsResponse,
            ) -> ListMembershipsResponseHttpRequest | None: ...
            def lookup(
                self,
                *,
                parent: str,
                memberKey_id: str = ...,
                memberKey_namespace: str = ...,
                **kwargs: typing.Any,
            ) -> LookupMembershipNameResponseHttpRequest: ...
            def modifyMembershipRoles(
                self,
                *,
                name: str,
                body: ModifyMembershipRolesRequest = ...,
                **kwargs: typing.Any,
            ) -> ModifyMembershipRolesResponseHttpRequest: ...
            def searchDirectGroups(
                self,
                *,
                parent: str,
                orderBy: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                query: str = ...,
                **kwargs: typing.Any,
            ) -> SearchDirectGroupsResponseHttpRequest: ...
            def searchDirectGroups_next(
                self,
                previous_request: SearchDirectGroupsResponseHttpRequest,
                previous_response: SearchDirectGroupsResponse,
            ) -> SearchDirectGroupsResponseHttpRequest | None: ...
            def searchTransitiveGroups(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                query: str = ...,
                **kwargs: typing.Any,
            ) -> SearchTransitiveGroupsResponseHttpRequest: ...
            def searchTransitiveGroups_next(
                self,
                previous_request: SearchTransitiveGroupsResponseHttpRequest,
                previous_response: SearchTransitiveGroupsResponse,
            ) -> SearchTransitiveGroupsResponseHttpRequest | None: ...
            def searchTransitiveMemberships(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any,
            ) -> SearchTransitiveMembershipsResponseHttpRequest: ...
            def searchTransitiveMemberships_next(
                self,
                previous_request: SearchTransitiveMembershipsResponseHttpRequest,
                previous_response: SearchTransitiveMembershipsResponse,
            ) -> SearchTransitiveMembershipsResponseHttpRequest | None: ...

        def create(
            self,
            *,
            body: Group = ...,
            initialGroupConfig: typing_extensions.Literal[
                "INITIAL_GROUP_CONFIG_UNSPECIFIED", "WITH_INITIAL_OWNER", "EMPTY"
            ] = ...,
            **kwargs: typing.Any,
        ) -> OperationHttpRequest: ...
        def delete(
            self, *, name: str, **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def get(self, *, name: str, **kwargs: typing.Any) -> GroupHttpRequest: ...
        def getSecuritySettings(
            self, *, name: str, readMask: str = ..., **kwargs: typing.Any
        ) -> SecuritySettingsHttpRequest: ...
        def list(
            self,
            *,
            pageSize: int = ...,
            pageToken: str = ...,
            parent: str = ...,
            view: typing_extensions.Literal["VIEW_UNSPECIFIED", "BASIC", "FULL"] = ...,
            **kwargs: typing.Any,
        ) -> ListGroupsResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: ListGroupsResponseHttpRequest,
            previous_response: ListGroupsResponse,
        ) -> ListGroupsResponseHttpRequest | None: ...
        def lookup(
            self,
            *,
            groupKey_id: str = ...,
            groupKey_namespace: str = ...,
            **kwargs: typing.Any,
        ) -> LookupGroupNameResponseHttpRequest: ...
        def patch(
            self,
            *,
            name: str,
            body: Group = ...,
            updateMask: str = ...,
            **kwargs: typing.Any,
        ) -> OperationHttpRequest: ...
        def search(
            self,
            *,
            pageSize: int = ...,
            pageToken: str = ...,
            query: str = ...,
            view: typing_extensions.Literal["VIEW_UNSPECIFIED", "BASIC", "FULL"] = ...,
            **kwargs: typing.Any,
        ) -> SearchGroupsResponseHttpRequest: ...
        def search_next(
            self,
            previous_request: SearchGroupsResponseHttpRequest,
            previous_response: SearchGroupsResponse,
        ) -> SearchGroupsResponseHttpRequest | None: ...
        def updateSecuritySettings(
            self,
            *,
            name: str,
            body: SecuritySettings = ...,
            updateMask: str = ...,
            **kwargs: typing.Any,
        ) -> OperationHttpRequest: ...
        def memberships(self) -> MembershipsResource: ...

    @typing.type_check_only
    class InboundSamlSsoProfilesResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class IdpCredentialsResource(googleapiclient.discovery.Resource):
            def add(
                self,
                *,
                parent: str,
                body: AddIdpCredentialRequest = ...,
                **kwargs: typing.Any,
            ) -> OperationHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> OperationHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> IdpCredentialHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any,
            ) -> ListIdpCredentialsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListIdpCredentialsResponseHttpRequest,
                previous_response: ListIdpCredentialsResponse,
            ) -> ListIdpCredentialsResponseHttpRequest | None: ...

        def create(
            self, *, body: InboundSamlSsoProfile = ..., **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def delete(
            self, *, name: str, **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def get(
            self, *, name: str, **kwargs: typing.Any
        ) -> InboundSamlSsoProfileHttpRequest: ...
        def list(
            self,
            *,
            filter: str = ...,
            pageSize: int = ...,
            pageToken: str = ...,
            **kwargs: typing.Any,
        ) -> ListInboundSamlSsoProfilesResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: ListInboundSamlSsoProfilesResponseHttpRequest,
            previous_response: ListInboundSamlSsoProfilesResponse,
        ) -> ListInboundSamlSsoProfilesResponseHttpRequest | None: ...
        def patch(
            self,
            *,
            name: str,
            body: InboundSamlSsoProfile = ...,
            updateMask: str = ...,
            **kwargs: typing.Any,
        ) -> OperationHttpRequest: ...
        def idpCredentials(self) -> IdpCredentialsResource: ...

    @typing.type_check_only
    class InboundSsoAssignmentsResource(googleapiclient.discovery.Resource):
        def create(
            self, *, body: InboundSsoAssignment = ..., **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def delete(
            self, *, name: str, **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def get(
            self, *, name: str, **kwargs: typing.Any
        ) -> InboundSsoAssignmentHttpRequest: ...
        def list(
            self,
            *,
            filter: str = ...,
            pageSize: int = ...,
            pageToken: str = ...,
            **kwargs: typing.Any,
        ) -> ListInboundSsoAssignmentsResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: ListInboundSsoAssignmentsResponseHttpRequest,
            previous_response: ListInboundSsoAssignmentsResponse,
        ) -> ListInboundSsoAssignmentsResponseHttpRequest | None: ...
        def patch(
            self,
            *,
            name: str,
            body: InboundSsoAssignment = ...,
            updateMask: str = ...,
            **kwargs: typing.Any,
        ) -> OperationHttpRequest: ...

    @typing.type_check_only
    class PoliciesResource(googleapiclient.discovery.Resource):
        def get(self, *, name: str, **kwargs: typing.Any) -> PolicyHttpRequest: ...
        def list(
            self,
            *,
            filter: str = ...,
            pageSize: int = ...,
            pageToken: str = ...,
            **kwargs: typing.Any,
        ) -> ListPoliciesResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: ListPoliciesResponseHttpRequest,
            previous_response: ListPoliciesResponse,
        ) -> ListPoliciesResponseHttpRequest | None: ...

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
    def customers(self) -> CustomersResource: ...
    def devices(self) -> DevicesResource: ...
    def groups(self) -> GroupsResource: ...
    def inboundSamlSsoProfiles(self) -> InboundSamlSsoProfilesResource: ...
    def inboundSsoAssignments(self) -> InboundSsoAssignmentsResource: ...
    def policies(self) -> PoliciesResource: ...

@typing.type_check_only
class CheckTransitiveMembershipResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> CheckTransitiveMembershipResponse: ...

@typing.type_check_only
class GoogleAppsCloudidentityDevicesV1ClientStateHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleAppsCloudidentityDevicesV1ClientState: ...

@typing.type_check_only
class GoogleAppsCloudidentityDevicesV1DeviceHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleAppsCloudidentityDevicesV1Device: ...

@typing.type_check_only
class GoogleAppsCloudidentityDevicesV1DeviceUserHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleAppsCloudidentityDevicesV1DeviceUser: ...

@typing.type_check_only
class GoogleAppsCloudidentityDevicesV1ListClientStatesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleAppsCloudidentityDevicesV1ListClientStatesResponse: ...

@typing.type_check_only
class GoogleAppsCloudidentityDevicesV1ListDeviceUsersResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleAppsCloudidentityDevicesV1ListDeviceUsersResponse: ...

@typing.type_check_only
class GoogleAppsCloudidentityDevicesV1ListDevicesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleAppsCloudidentityDevicesV1ListDevicesResponse: ...

@typing.type_check_only
class GoogleAppsCloudidentityDevicesV1LookupSelfDeviceUsersResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleAppsCloudidentityDevicesV1LookupSelfDeviceUsersResponse: ...

@typing.type_check_only
class GroupHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Group: ...

@typing.type_check_only
class IdpCredentialHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> IdpCredential: ...

@typing.type_check_only
class InboundSamlSsoProfileHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> InboundSamlSsoProfile: ...

@typing.type_check_only
class InboundSsoAssignmentHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> InboundSsoAssignment: ...

@typing.type_check_only
class IsInvitableUserResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> IsInvitableUserResponse: ...

@typing.type_check_only
class ListGroupsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListGroupsResponse: ...

@typing.type_check_only
class ListIdpCredentialsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListIdpCredentialsResponse: ...

@typing.type_check_only
class ListInboundSamlSsoProfilesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListInboundSamlSsoProfilesResponse: ...

@typing.type_check_only
class ListInboundSsoAssignmentsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListInboundSsoAssignmentsResponse: ...

@typing.type_check_only
class ListMembershipsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListMembershipsResponse: ...

@typing.type_check_only
class ListPoliciesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListPoliciesResponse: ...

@typing.type_check_only
class ListUserInvitationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListUserInvitationsResponse: ...

@typing.type_check_only
class LookupGroupNameResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> LookupGroupNameResponse: ...

@typing.type_check_only
class LookupMembershipNameResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> LookupMembershipNameResponse: ...

@typing.type_check_only
class MembershipHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Membership: ...

@typing.type_check_only
class ModifyMembershipRolesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ModifyMembershipRolesResponse: ...

@typing.type_check_only
class OperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Operation: ...

@typing.type_check_only
class PolicyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Policy: ...

@typing.type_check_only
class SearchDirectGroupsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> SearchDirectGroupsResponse: ...

@typing.type_check_only
class SearchGroupsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> SearchGroupsResponse: ...

@typing.type_check_only
class SearchTransitiveGroupsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> SearchTransitiveGroupsResponse: ...

@typing.type_check_only
class SearchTransitiveMembershipsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> SearchTransitiveMembershipsResponse: ...

@typing.type_check_only
class SecuritySettingsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> SecuritySettings: ...

@typing.type_check_only
class UserInvitationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> UserInvitation: ...
