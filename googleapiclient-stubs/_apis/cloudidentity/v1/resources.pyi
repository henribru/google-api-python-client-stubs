import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class CloudIdentityResource(googleapiclient.discovery.Resource):
    class DevicesResource(googleapiclient.discovery.Resource):
        class DeviceUsersResource(googleapiclient.discovery.Resource):
            class ClientStatesResource(googleapiclient.discovery.Resource):
                def get(
                    self, *, name: str, customer: str = ..., **kwargs: typing.Any
                ) -> GoogleAppsCloudidentityDevicesV1ClientStateHttpRequest: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleAppsCloudidentityDevicesV1ClientState = ...,
                    customer: str = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    orderBy: str = ...,
                    filter: str = ...,
                    customer: str = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleAppsCloudidentityDevicesV1ListClientStatesResponseHttpRequest: ...
            def cancelWipe(
                self,
                *,
                name: str,
                body: GoogleAppsCloudidentityDevicesV1CancelWipeDeviceUserRequest = ...,
                **kwargs: typing.Any
            ) -> OperationHttpRequest: ...
            def lookup(
                self,
                *,
                parent: str,
                pageToken: str = ...,
                androidId: str = ...,
                rawResourceId: str = ...,
                pageSize: int = ...,
                userId: str = ...,
                **kwargs: typing.Any
            ) -> GoogleAppsCloudidentityDevicesV1LookupSelfDeviceUsersResponseHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                filter: str = ...,
                pageSize: int = ...,
                customer: str = ...,
                pageToken: str = ...,
                orderBy: str = ...,
                **kwargs: typing.Any
            ) -> GoogleAppsCloudidentityDevicesV1ListDeviceUsersResponseHttpRequest: ...
            def block(
                self,
                *,
                name: str,
                body: GoogleAppsCloudidentityDevicesV1BlockDeviceUserRequest = ...,
                **kwargs: typing.Any
            ) -> OperationHttpRequest: ...
            def delete(
                self, *, name: str, customer: str = ..., **kwargs: typing.Any
            ) -> OperationHttpRequest: ...
            def wipe(
                self,
                *,
                name: str,
                body: GoogleAppsCloudidentityDevicesV1WipeDeviceUserRequest = ...,
                **kwargs: typing.Any
            ) -> OperationHttpRequest: ...
            def approve(
                self,
                *,
                name: str,
                body: GoogleAppsCloudidentityDevicesV1ApproveDeviceUserRequest = ...,
                **kwargs: typing.Any
            ) -> OperationHttpRequest: ...
            def get(
                self, *, name: str, customer: str = ..., **kwargs: typing.Any
            ) -> GoogleAppsCloudidentityDevicesV1DeviceUserHttpRequest: ...
            def clientStates(self) -> ClientStatesResource: ...
        def delete(
            self, *, name: str, customer: str = ..., **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def wipe(
            self,
            *,
            name: str,
            body: GoogleAppsCloudidentityDevicesV1WipeDeviceRequest = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def list(
            self,
            *,
            view: typing_extensions.Literal[
                "VIEW_UNSPECIFIED", "COMPANY_INVENTORY", "USER_ASSIGNED_DEVICES"
            ] = ...,
            customer: str = ...,
            pageToken: str = ...,
            orderBy: str = ...,
            pageSize: int = ...,
            filter: str = ...,
            **kwargs: typing.Any
        ) -> GoogleAppsCloudidentityDevicesV1ListDevicesResponseHttpRequest: ...
        def get(
            self, *, name: str, customer: str = ..., **kwargs: typing.Any
        ) -> GoogleAppsCloudidentityDevicesV1DeviceHttpRequest: ...
        def create(
            self,
            *,
            body: GoogleAppsCloudidentityDevicesV1Device = ...,
            customer: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def cancelWipe(
            self,
            *,
            name: str,
            body: GoogleAppsCloudidentityDevicesV1CancelWipeDeviceRequest = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def deviceUsers(self) -> DeviceUsersResource: ...
    class GroupsResource(googleapiclient.discovery.Resource):
        class MembershipsResource(googleapiclient.discovery.Resource):
            def list(
                self,
                *,
                parent: str,
                pageToken: str = ...,
                view: typing_extensions.Literal[
                    "VIEW_UNSPECIFIED", "BASIC", "FULL"
                ] = ...,
                pageSize: int = ...,
                **kwargs: typing.Any
            ) -> ListMembershipsResponseHttpRequest: ...
            def modifyMembershipRoles(
                self,
                *,
                name: str,
                body: ModifyMembershipRolesRequest = ...,
                **kwargs: typing.Any
            ) -> ModifyMembershipRolesResponseHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> MembershipHttpRequest: ...
            def create(
                self, *, parent: str, body: Membership = ..., **kwargs: typing.Any
            ) -> OperationHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> OperationHttpRequest: ...
            def lookup(
                self,
                *,
                parent: str,
                memberKey_namespace: str = ...,
                memberKey_id: str = ...,
                **kwargs: typing.Any
            ) -> LookupMembershipNameResponseHttpRequest: ...
        def create(
            self,
            *,
            body: Group = ...,
            initialGroupConfig: typing_extensions.Literal[
                "INITIAL_GROUP_CONFIG_UNSPECIFIED", "WITH_INITIAL_OWNER", "EMPTY"
            ] = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def delete(
            self, *, name: str, **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def search(
            self,
            *,
            view: typing_extensions.Literal["VIEW_UNSPECIFIED", "BASIC", "FULL"] = ...,
            pageToken: str = ...,
            query: str = ...,
            pageSize: int = ...,
            **kwargs: typing.Any
        ) -> SearchGroupsResponseHttpRequest: ...
        def patch(
            self,
            *,
            name: str,
            body: Group = ...,
            updateMask: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def lookup(
            self,
            *,
            groupKey_id: str = ...,
            groupKey_namespace: str = ...,
            **kwargs: typing.Any
        ) -> LookupGroupNameResponseHttpRequest: ...
        def get(self, *, name: str, **kwargs: typing.Any) -> GroupHttpRequest: ...
        def list(
            self,
            *,
            parent: str = ...,
            pageToken: str = ...,
            view: typing_extensions.Literal["VIEW_UNSPECIFIED", "BASIC", "FULL"] = ...,
            pageSize: int = ...,
            **kwargs: typing.Any
        ) -> ListGroupsResponseHttpRequest: ...
        def memberships(self) -> MembershipsResource: ...
    def devices(self) -> DevicesResource: ...
    def groups(self) -> GroupsResource: ...

class GoogleAppsCloudidentityDevicesV1ListClientStatesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleAppsCloudidentityDevicesV1ListClientStatesResponse: ...

class GoogleAppsCloudidentityDevicesV1ListDevicesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleAppsCloudidentityDevicesV1ListDevicesResponse: ...

class MembershipHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Membership: ...

class ListMembershipsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListMembershipsResponse: ...

class GoogleAppsCloudidentityDevicesV1ListDeviceUsersResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleAppsCloudidentityDevicesV1ListDeviceUsersResponse: ...

class ListGroupsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListGroupsResponse: ...

class LookupGroupNameResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> LookupGroupNameResponse: ...

class GoogleAppsCloudidentityDevicesV1ClientStateHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleAppsCloudidentityDevicesV1ClientState: ...

class GoogleAppsCloudidentityDevicesV1LookupSelfDeviceUsersResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleAppsCloudidentityDevicesV1LookupSelfDeviceUsersResponse: ...

class GoogleAppsCloudidentityDevicesV1DeviceHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleAppsCloudidentityDevicesV1Device: ...

class OperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Operation: ...

class GroupHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Group: ...

class SearchGroupsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> SearchGroupsResponse: ...

class GoogleAppsCloudidentityDevicesV1DeviceUserHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleAppsCloudidentityDevicesV1DeviceUser: ...

class LookupMembershipNameResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> LookupMembershipNameResponse: ...

class ModifyMembershipRolesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ModifyMembershipRolesResponse: ...
