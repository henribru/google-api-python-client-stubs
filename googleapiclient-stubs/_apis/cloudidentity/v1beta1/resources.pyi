import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class CloudIdentityResource(googleapiclient.discovery.Resource):
    class GroupsResource(googleapiclient.discovery.Resource):
        class MembershipsResource(googleapiclient.discovery.Resource):
            def create(
                self, *, parent: str, body: Membership = ..., **kwargs: typing.Any
            ) -> OperationHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                view: typing_extensions.Literal["BASIC", "FULL"] = ...,
                **kwargs: typing.Any
            ) -> ListMembershipsResponseHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> OperationHttpRequest: ...
            def searchTransitiveGroups(
                self,
                *,
                parent: str,
                pageToken: str = ...,
                query: str = ...,
                pageSize: int = ...,
                **kwargs: typing.Any
            ) -> SearchTransitiveGroupsResponseHttpRequest: ...
            def checkTransitiveMembership(
                self, *, parent: str, query: str = ..., **kwargs: typing.Any
            ) -> CheckTransitiveMembershipResponseHttpRequest: ...
            def modifyMembershipRoles(
                self,
                *,
                name: str,
                body: ModifyMembershipRolesRequest = ...,
                **kwargs: typing.Any
            ) -> ModifyMembershipRolesResponseHttpRequest: ...
            def getMembershipGraph(
                self, *, parent: str, query: str = ..., **kwargs: typing.Any
            ) -> OperationHttpRequest: ...
            def lookup(
                self,
                *,
                parent: str,
                memberKey_id: str = ...,
                memberKey_namespace: str = ...,
                **kwargs: typing.Any
            ) -> LookupMembershipNameResponseHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> MembershipHttpRequest: ...
            def searchTransitiveMemberships(
                self,
                *,
                parent: str,
                pageToken: str = ...,
                pageSize: int = ...,
                **kwargs: typing.Any
            ) -> SearchTransitiveMembershipsResponseHttpRequest: ...
        def patch(
            self,
            *,
            name: str,
            body: Group = ...,
            updateMask: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def list(
            self,
            *,
            pageToken: str = ...,
            parent: str = ...,
            view: typing_extensions.Literal["VIEW_UNSPECIFIED", "BASIC", "FULL"] = ...,
            pageSize: int = ...,
            **kwargs: typing.Any
        ) -> ListGroupsResponseHttpRequest: ...
        def search(
            self,
            *,
            pageToken: str = ...,
            view: typing_extensions.Literal["BASIC", "FULL"] = ...,
            query: str = ...,
            pageSize: int = ...,
            **kwargs: typing.Any
        ) -> SearchGroupsResponseHttpRequest: ...
        def delete(
            self, *, name: str, **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def get(self, *, name: str, **kwargs: typing.Any) -> GroupHttpRequest: ...
        def lookup(
            self,
            *,
            groupKey_id: str = ...,
            groupKey_namespace: str = ...,
            **kwargs: typing.Any
        ) -> LookupGroupNameResponseHttpRequest: ...
        def create(
            self,
            *,
            body: Group = ...,
            initialGroupConfig: typing_extensions.Literal[
                "INITIAL_GROUP_CONFIG_UNSPECIFIED", "WITH_INITIAL_OWNER", "EMPTY"
            ] = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def memberships(self) -> MembershipsResource: ...
    class DevicesResource(googleapiclient.discovery.Resource):
        class DeviceUsersResource(googleapiclient.discovery.Resource):
            class ClientStatesResource(googleapiclient.discovery.Resource):
                def get(
                    self, *, name: str, customer: str = ..., **kwargs: typing.Any
                ) -> ClientStateHttpRequest: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: ClientState = ...,
                    updateMask: str = ...,
                    customer: str = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
            def cancelWipe(
                self,
                *,
                name: str,
                body: CancelWipeDeviceUserRequest = ...,
                **kwargs: typing.Any
            ) -> OperationHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                orderBy: str = ...,
                filter: str = ...,
                customer: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> ListDeviceUsersResponseHttpRequest: ...
            def wipe(
                self,
                *,
                name: str,
                body: WipeDeviceUserRequest = ...,
                **kwargs: typing.Any
            ) -> OperationHttpRequest: ...
            def approve(
                self,
                *,
                name: str,
                body: ApproveDeviceUserRequest = ...,
                **kwargs: typing.Any
            ) -> OperationHttpRequest: ...
            def delete(
                self, *, name: str, customer: str = ..., **kwargs: typing.Any
            ) -> OperationHttpRequest: ...
            def get(
                self, *, name: str, customer: str = ..., **kwargs: typing.Any
            ) -> DeviceUserHttpRequest: ...
            def lookup(
                self,
                *,
                parent: str,
                userId: str = ...,
                pageToken: str = ...,
                rawResourceId: str = ...,
                pageSize: int = ...,
                androidId: str = ...,
                **kwargs: typing.Any
            ) -> LookupSelfDeviceUsersResponseHttpRequest: ...
            def block(
                self,
                *,
                name: str,
                body: BlockDeviceUserRequest = ...,
                **kwargs: typing.Any
            ) -> OperationHttpRequest: ...
            def clientStates(self) -> ClientStatesResource: ...
        def wipe(
            self, *, name: str, body: WipeDeviceRequest = ..., **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def cancelWipe(
            self,
            *,
            name: str,
            body: CancelWipeDeviceRequest = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def create(
            self, *, body: CreateDeviceRequest = ..., **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def list(
            self,
            *,
            view: typing_extensions.Literal[
                "VIEW_UNSPECIFIED", "COMPANY_INVENTORY", "USER_ASSIGNED_DEVICES"
            ] = ...,
            orderBy: str = ...,
            pageToken: str = ...,
            customer: str = ...,
            filter: str = ...,
            pageSize: int = ...,
            **kwargs: typing.Any
        ) -> ListDevicesResponseHttpRequest: ...
        def get(
            self, *, name: str, customer: str = ..., **kwargs: typing.Any
        ) -> DeviceHttpRequest: ...
        def delete(
            self, *, name: str, customer: str = ..., **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def deviceUsers(self) -> DeviceUsersResource: ...
    def groups(self) -> GroupsResource: ...
    def devices(self) -> DevicesResource: ...

class SearchTransitiveGroupsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> SearchTransitiveGroupsResponse: ...

class MembershipHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Membership: ...

class ListGroupsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListGroupsResponse: ...

class LookupGroupNameResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> LookupGroupNameResponse: ...

class CheckTransitiveMembershipResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> CheckTransitiveMembershipResponse: ...

class LookupSelfDeviceUsersResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> LookupSelfDeviceUsersResponse: ...

class OperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Operation: ...

class ListMembershipsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListMembershipsResponse: ...

class GroupHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Group: ...

class DeviceHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Device: ...

class ClientStateHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ClientState: ...

class ListDeviceUsersResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListDeviceUsersResponse: ...

class SearchTransitiveMembershipsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> SearchTransitiveMembershipsResponse: ...

class DeviceUserHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> DeviceUser: ...

class ListDevicesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListDevicesResponse: ...

class SearchGroupsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> SearchGroupsResponse: ...

class ModifyMembershipRolesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ModifyMembershipRolesResponse: ...

class LookupMembershipNameResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> LookupMembershipNameResponse: ...
