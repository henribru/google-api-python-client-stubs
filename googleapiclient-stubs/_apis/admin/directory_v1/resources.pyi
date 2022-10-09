import collections.abc
import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

_list = list

@typing.type_check_only
class DirectoryResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class AspsResource(googleapiclient.discovery.Resource):
        def delete(
            self, *, userKey: str, codeId: int, **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def get(
            self, *, userKey: str, codeId: int, **kwargs: typing.Any
        ) -> AspHttpRequest: ...
        def list(self, *, userKey: str, **kwargs: typing.Any) -> AspsHttpRequest: ...

    @typing.type_check_only
    class ChannelsResource(googleapiclient.discovery.Resource):
        def stop(
            self, *, body: Channel = ..., **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...

    @typing.type_check_only
    class ChromeosdevicesResource(googleapiclient.discovery.Resource):
        def action(
            self,
            *,
            customerId: str,
            resourceId: str,
            body: ChromeOsDeviceAction = ...,
            **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def get(
            self,
            *,
            customerId: str,
            deviceId: str,
            projection: typing_extensions.Literal["BASIC", "FULL"] = ...,
            **kwargs: typing.Any
        ) -> ChromeOsDeviceHttpRequest: ...
        def list(
            self,
            *,
            customerId: str,
            includeChildOrgunits: bool = ...,
            maxResults: int = ...,
            orderBy: typing_extensions.Literal[
                "annotatedLocation",
                "annotatedUser",
                "lastSync",
                "notes",
                "serialNumber",
                "status",
            ] = ...,
            orgUnitPath: str = ...,
            pageToken: str = ...,
            projection: typing_extensions.Literal["BASIC", "FULL"] = ...,
            query: str = ...,
            sortOrder: typing_extensions.Literal["ASCENDING", "DESCENDING"] = ...,
            **kwargs: typing.Any
        ) -> ChromeOsDevicesHttpRequest: ...
        def list_next(
            self,
            previous_request: ChromeOsDevicesHttpRequest,
            previous_response: ChromeOsDevices,
        ) -> ChromeOsDevicesHttpRequest | None: ...
        def moveDevicesToOu(
            self,
            *,
            customerId: str,
            orgUnitPath: str,
            body: ChromeOsMoveDevicesToOu = ...,
            **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def patch(
            self,
            *,
            customerId: str,
            deviceId: str,
            body: ChromeOsDevice = ...,
            projection: typing_extensions.Literal["BASIC", "FULL"] = ...,
            **kwargs: typing.Any
        ) -> ChromeOsDeviceHttpRequest: ...
        def update(
            self,
            *,
            customerId: str,
            deviceId: str,
            body: ChromeOsDevice = ...,
            projection: typing_extensions.Literal["BASIC", "FULL"] = ...,
            **kwargs: typing.Any
        ) -> ChromeOsDeviceHttpRequest: ...

    @typing.type_check_only
    class CustomerResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class DevicesResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class ChromeosResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class CommandsResource(googleapiclient.discovery.Resource):
                    def get(
                        self,
                        *,
                        customerId: str,
                        deviceId: str,
                        commandId: str,
                        **kwargs: typing.Any
                    ) -> DirectoryChromeosdevicesCommandHttpRequest: ...

                def issueCommand(
                    self,
                    *,
                    customerId: str,
                    deviceId: str,
                    body: DirectoryChromeosdevicesIssueCommandRequest = ...,
                    **kwargs: typing.Any
                ) -> DirectoryChromeosdevicesIssueCommandResponseHttpRequest: ...
                def commands(self) -> CommandsResource: ...

            def chromeos(self) -> ChromeosResource: ...

        def devices(self) -> DevicesResource: ...

    @typing.type_check_only
    class CustomersResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class ChromeResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class PrintServersResource(googleapiclient.discovery.Resource):
                def batchCreatePrintServers(
                    self,
                    *,
                    parent: str,
                    body: BatchCreatePrintServersRequest = ...,
                    **kwargs: typing.Any
                ) -> BatchCreatePrintServersResponseHttpRequest: ...
                def batchDeletePrintServers(
                    self,
                    *,
                    parent: str,
                    body: BatchDeletePrintServersRequest = ...,
                    **kwargs: typing.Any
                ) -> BatchDeletePrintServersResponseHttpRequest: ...
                def create(
                    self, *, parent: str, body: PrintServer = ..., **kwargs: typing.Any
                ) -> PrintServerHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> PrintServerHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    orderBy: str = ...,
                    orgUnitId: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> ListPrintServersResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListPrintServersResponseHttpRequest,
                    previous_response: ListPrintServersResponse,
                ) -> ListPrintServersResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: PrintServer = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any
                ) -> PrintServerHttpRequest: ...

            @typing.type_check_only
            class PrintersResource(googleapiclient.discovery.Resource):
                def batchCreatePrinters(
                    self,
                    *,
                    parent: str,
                    body: BatchCreatePrintersRequest = ...,
                    **kwargs: typing.Any
                ) -> BatchCreatePrintersResponseHttpRequest: ...
                def batchDeletePrinters(
                    self,
                    *,
                    parent: str,
                    body: BatchDeletePrintersRequest = ...,
                    **kwargs: typing.Any
                ) -> BatchDeletePrintersResponseHttpRequest: ...
                def create(
                    self, *, parent: str, body: Printer = ..., **kwargs: typing.Any
                ) -> PrinterHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> PrinterHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    orderBy: str = ...,
                    orgUnitId: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> ListPrintersResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListPrintersResponseHttpRequest,
                    previous_response: ListPrintersResponse,
                ) -> ListPrintersResponseHttpRequest | None: ...
                def listPrinterModels(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> ListPrinterModelsResponseHttpRequest: ...
                def listPrinterModels_next(
                    self,
                    previous_request: ListPrinterModelsResponseHttpRequest,
                    previous_response: ListPrinterModelsResponse,
                ) -> ListPrinterModelsResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: Printer = ...,
                    clearMask: str = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any
                ) -> PrinterHttpRequest: ...

            def printServers(self) -> PrintServersResource: ...
            def printers(self) -> PrintersResource: ...

        def get(
            self, *, customerKey: str, **kwargs: typing.Any
        ) -> CustomerHttpRequest: ...
        def patch(
            self, *, customerKey: str, body: Customer = ..., **kwargs: typing.Any
        ) -> CustomerHttpRequest: ...
        def update(
            self, *, customerKey: str, body: Customer = ..., **kwargs: typing.Any
        ) -> CustomerHttpRequest: ...
        def chrome(self) -> ChromeResource: ...

    @typing.type_check_only
    class DomainAliasesResource(googleapiclient.discovery.Resource):
        def delete(
            self, *, customer: str, domainAliasName: str, **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def get(
            self, *, customer: str, domainAliasName: str, **kwargs: typing.Any
        ) -> DomainAliasHttpRequest: ...
        def insert(
            self, *, customer: str, body: DomainAlias = ..., **kwargs: typing.Any
        ) -> DomainAliasHttpRequest: ...
        def list(
            self, *, customer: str, parentDomainName: str = ..., **kwargs: typing.Any
        ) -> DomainAliasesHttpRequest: ...

    @typing.type_check_only
    class DomainsResource(googleapiclient.discovery.Resource):
        def delete(
            self, *, customer: str, domainName: str, **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def get(
            self, *, customer: str, domainName: str, **kwargs: typing.Any
        ) -> DomainsHttpRequest: ...
        def insert(
            self, *, customer: str, body: Domains = ..., **kwargs: typing.Any
        ) -> DomainsHttpRequest: ...
        def list(
            self, *, customer: str, **kwargs: typing.Any
        ) -> Domains2HttpRequest: ...

    @typing.type_check_only
    class GroupsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class AliasesResource(googleapiclient.discovery.Resource):
            def delete(
                self, *, groupKey: str, alias: str, **kwargs: typing.Any
            ) -> googleapiclient.http.HttpRequest: ...
            def insert(
                self, *, groupKey: str, body: Alias = ..., **kwargs: typing.Any
            ) -> AliasHttpRequest: ...
            def list(
                self, *, groupKey: str, **kwargs: typing.Any
            ) -> AliasesHttpRequest: ...

        def delete(
            self, *, groupKey: str, **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def get(self, *, groupKey: str, **kwargs: typing.Any) -> GroupHttpRequest: ...
        def insert(
            self, *, body: Group = ..., **kwargs: typing.Any
        ) -> GroupHttpRequest: ...
        def list(
            self,
            *,
            customer: str = ...,
            domain: str = ...,
            maxResults: int = ...,
            orderBy: typing_extensions.Literal["email"] = ...,
            pageToken: str = ...,
            query: str = ...,
            sortOrder: typing_extensions.Literal["ASCENDING", "DESCENDING"] = ...,
            userKey: str = ...,
            **kwargs: typing.Any
        ) -> GroupsHttpRequest: ...
        def list_next(
            self, previous_request: GroupsHttpRequest, previous_response: Groups
        ) -> GroupsHttpRequest | None: ...
        def patch(
            self, *, groupKey: str, body: Group = ..., **kwargs: typing.Any
        ) -> GroupHttpRequest: ...
        def update(
            self, *, groupKey: str, body: Group = ..., **kwargs: typing.Any
        ) -> GroupHttpRequest: ...
        def aliases(self) -> AliasesResource: ...

    @typing.type_check_only
    class MembersResource(googleapiclient.discovery.Resource):
        def delete(
            self, *, groupKey: str, memberKey: str, **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def get(
            self, *, groupKey: str, memberKey: str, **kwargs: typing.Any
        ) -> MemberHttpRequest: ...
        def hasMember(
            self, *, groupKey: str, memberKey: str, **kwargs: typing.Any
        ) -> MembersHasMemberHttpRequest: ...
        def insert(
            self, *, groupKey: str, body: Member = ..., **kwargs: typing.Any
        ) -> MemberHttpRequest: ...
        def list(
            self,
            *,
            groupKey: str,
            includeDerivedMembership: bool = ...,
            maxResults: int = ...,
            pageToken: str = ...,
            roles: str = ...,
            **kwargs: typing.Any
        ) -> MembersHttpRequest: ...
        def list_next(
            self, previous_request: MembersHttpRequest, previous_response: Members
        ) -> MembersHttpRequest | None: ...
        def patch(
            self,
            *,
            groupKey: str,
            memberKey: str,
            body: Member = ...,
            **kwargs: typing.Any
        ) -> MemberHttpRequest: ...
        def update(
            self,
            *,
            groupKey: str,
            memberKey: str,
            body: Member = ...,
            **kwargs: typing.Any
        ) -> MemberHttpRequest: ...

    @typing.type_check_only
    class MobiledevicesResource(googleapiclient.discovery.Resource):
        def action(
            self,
            *,
            customerId: str,
            resourceId: str,
            body: MobileDeviceAction = ...,
            **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def delete(
            self, *, customerId: str, resourceId: str, **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def get(
            self,
            *,
            customerId: str,
            resourceId: str,
            projection: typing_extensions.Literal["BASIC", "FULL"] = ...,
            **kwargs: typing.Any
        ) -> MobileDeviceHttpRequest: ...
        def list(
            self,
            *,
            customerId: str,
            maxResults: int = ...,
            orderBy: typing_extensions.Literal[
                "deviceId", "email", "lastSync", "model", "name", "os", "status", "type"
            ] = ...,
            pageToken: str = ...,
            projection: typing_extensions.Literal["BASIC", "FULL"] = ...,
            query: str = ...,
            sortOrder: typing_extensions.Literal["ASCENDING", "DESCENDING"] = ...,
            **kwargs: typing.Any
        ) -> MobileDevicesHttpRequest: ...
        def list_next(
            self,
            previous_request: MobileDevicesHttpRequest,
            previous_response: MobileDevices,
        ) -> MobileDevicesHttpRequest | None: ...

    @typing.type_check_only
    class OrgunitsResource(googleapiclient.discovery.Resource):
        def delete(
            self, *, customerId: str, orgUnitPath: str, **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def get(
            self, *, customerId: str, orgUnitPath: str, **kwargs: typing.Any
        ) -> OrgUnitHttpRequest: ...
        def insert(
            self, *, customerId: str, body: OrgUnit = ..., **kwargs: typing.Any
        ) -> OrgUnitHttpRequest: ...
        def list(
            self,
            *,
            customerId: str,
            orgUnitPath: str = ...,
            type: typing_extensions.Literal["all", "children"] = ...,
            **kwargs: typing.Any
        ) -> OrgUnitsHttpRequest: ...
        def patch(
            self,
            *,
            customerId: str,
            orgUnitPath: str,
            body: OrgUnit = ...,
            **kwargs: typing.Any
        ) -> OrgUnitHttpRequest: ...
        def update(
            self,
            *,
            customerId: str,
            orgUnitPath: str,
            body: OrgUnit = ...,
            **kwargs: typing.Any
        ) -> OrgUnitHttpRequest: ...

    @typing.type_check_only
    class PrivilegesResource(googleapiclient.discovery.Resource):
        def list(
            self, *, customer: str, **kwargs: typing.Any
        ) -> PrivilegesHttpRequest: ...

    @typing.type_check_only
    class ResourcesResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class BuildingsResource(googleapiclient.discovery.Resource):
            def delete(
                self, *, customer: str, buildingId: str, **kwargs: typing.Any
            ) -> googleapiclient.http.HttpRequest: ...
            def get(
                self, *, customer: str, buildingId: str, **kwargs: typing.Any
            ) -> BuildingHttpRequest: ...
            def insert(
                self,
                *,
                customer: str,
                body: Building = ...,
                coordinatesSource: typing_extensions.Literal[
                    "CLIENT_SPECIFIED", "RESOLVED_FROM_ADDRESS", "SOURCE_UNSPECIFIED"
                ] = ...,
                **kwargs: typing.Any
            ) -> BuildingHttpRequest: ...
            def list(
                self,
                *,
                customer: str,
                maxResults: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> BuildingsHttpRequest: ...
            def list_next(
                self,
                previous_request: BuildingsHttpRequest,
                previous_response: Buildings,
            ) -> BuildingsHttpRequest | None: ...
            def patch(
                self,
                *,
                customer: str,
                buildingId: str,
                body: Building = ...,
                coordinatesSource: typing_extensions.Literal[
                    "CLIENT_SPECIFIED", "RESOLVED_FROM_ADDRESS", "SOURCE_UNSPECIFIED"
                ] = ...,
                **kwargs: typing.Any
            ) -> BuildingHttpRequest: ...
            def update(
                self,
                *,
                customer: str,
                buildingId: str,
                body: Building = ...,
                coordinatesSource: typing_extensions.Literal[
                    "CLIENT_SPECIFIED", "RESOLVED_FROM_ADDRESS", "SOURCE_UNSPECIFIED"
                ] = ...,
                **kwargs: typing.Any
            ) -> BuildingHttpRequest: ...

        @typing.type_check_only
        class CalendarsResource(googleapiclient.discovery.Resource):
            def delete(
                self, *, customer: str, calendarResourceId: str, **kwargs: typing.Any
            ) -> googleapiclient.http.HttpRequest: ...
            def get(
                self, *, customer: str, calendarResourceId: str, **kwargs: typing.Any
            ) -> CalendarResourceHttpRequest: ...
            def insert(
                self,
                *,
                customer: str,
                body: CalendarResource = ...,
                **kwargs: typing.Any
            ) -> CalendarResourceHttpRequest: ...
            def list(
                self,
                *,
                customer: str,
                maxResults: int = ...,
                orderBy: str = ...,
                pageToken: str = ...,
                query: str = ...,
                **kwargs: typing.Any
            ) -> CalendarResourcesHttpRequest: ...
            def list_next(
                self,
                previous_request: CalendarResourcesHttpRequest,
                previous_response: CalendarResources,
            ) -> CalendarResourcesHttpRequest | None: ...
            def patch(
                self,
                *,
                customer: str,
                calendarResourceId: str,
                body: CalendarResource = ...,
                **kwargs: typing.Any
            ) -> CalendarResourceHttpRequest: ...
            def update(
                self,
                *,
                customer: str,
                calendarResourceId: str,
                body: CalendarResource = ...,
                **kwargs: typing.Any
            ) -> CalendarResourceHttpRequest: ...

        @typing.type_check_only
        class FeaturesResource(googleapiclient.discovery.Resource):
            def delete(
                self, *, customer: str, featureKey: str, **kwargs: typing.Any
            ) -> googleapiclient.http.HttpRequest: ...
            def get(
                self, *, customer: str, featureKey: str, **kwargs: typing.Any
            ) -> FeatureHttpRequest: ...
            def insert(
                self, *, customer: str, body: Feature = ..., **kwargs: typing.Any
            ) -> FeatureHttpRequest: ...
            def list(
                self,
                *,
                customer: str,
                maxResults: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> FeaturesHttpRequest: ...
            def list_next(
                self, previous_request: FeaturesHttpRequest, previous_response: Features
            ) -> FeaturesHttpRequest | None: ...
            def patch(
                self,
                *,
                customer: str,
                featureKey: str,
                body: Feature = ...,
                **kwargs: typing.Any
            ) -> FeatureHttpRequest: ...
            def rename(
                self,
                *,
                customer: str,
                oldName: str,
                body: FeatureRename = ...,
                **kwargs: typing.Any
            ) -> googleapiclient.http.HttpRequest: ...
            def update(
                self,
                *,
                customer: str,
                featureKey: str,
                body: Feature = ...,
                **kwargs: typing.Any
            ) -> FeatureHttpRequest: ...

        def buildings(self) -> BuildingsResource: ...
        def calendars(self) -> CalendarsResource: ...
        def features(self) -> FeaturesResource: ...

    @typing.type_check_only
    class RoleAssignmentsResource(googleapiclient.discovery.Resource):
        def delete(
            self, *, customer: str, roleAssignmentId: str, **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def get(
            self, *, customer: str, roleAssignmentId: str, **kwargs: typing.Any
        ) -> RoleAssignmentHttpRequest: ...
        def insert(
            self, *, customer: str, body: RoleAssignment = ..., **kwargs: typing.Any
        ) -> RoleAssignmentHttpRequest: ...
        def list(
            self,
            *,
            customer: str,
            maxResults: int = ...,
            pageToken: str = ...,
            roleId: str = ...,
            userKey: str = ...,
            **kwargs: typing.Any
        ) -> RoleAssignmentsHttpRequest: ...
        def list_next(
            self,
            previous_request: RoleAssignmentsHttpRequest,
            previous_response: RoleAssignments,
        ) -> RoleAssignmentsHttpRequest | None: ...

    @typing.type_check_only
    class RolesResource(googleapiclient.discovery.Resource):
        def delete(
            self, *, customer: str, roleId: str, **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def get(
            self, *, customer: str, roleId: str, **kwargs: typing.Any
        ) -> RoleHttpRequest: ...
        def insert(
            self, *, customer: str, body: Role = ..., **kwargs: typing.Any
        ) -> RoleHttpRequest: ...
        def list(
            self,
            *,
            customer: str,
            maxResults: int = ...,
            pageToken: str = ...,
            **kwargs: typing.Any
        ) -> RolesHttpRequest: ...
        def list_next(
            self, previous_request: RolesHttpRequest, previous_response: Roles
        ) -> RolesHttpRequest | None: ...
        def patch(
            self, *, customer: str, roleId: str, body: Role = ..., **kwargs: typing.Any
        ) -> RoleHttpRequest: ...
        def update(
            self, *, customer: str, roleId: str, body: Role = ..., **kwargs: typing.Any
        ) -> RoleHttpRequest: ...

    @typing.type_check_only
    class SchemasResource(googleapiclient.discovery.Resource):
        def delete(
            self, *, customerId: str, schemaKey: str, **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def get(
            self, *, customerId: str, schemaKey: str, **kwargs: typing.Any
        ) -> SchemaHttpRequest: ...
        def insert(
            self, *, customerId: str, body: Schema = ..., **kwargs: typing.Any
        ) -> SchemaHttpRequest: ...
        def list(
            self, *, customerId: str, **kwargs: typing.Any
        ) -> SchemasHttpRequest: ...
        def patch(
            self,
            *,
            customerId: str,
            schemaKey: str,
            body: Schema = ...,
            **kwargs: typing.Any
        ) -> SchemaHttpRequest: ...
        def update(
            self,
            *,
            customerId: str,
            schemaKey: str,
            body: Schema = ...,
            **kwargs: typing.Any
        ) -> SchemaHttpRequest: ...

    @typing.type_check_only
    class TokensResource(googleapiclient.discovery.Resource):
        def delete(
            self, *, userKey: str, clientId: str, **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def get(
            self, *, userKey: str, clientId: str, **kwargs: typing.Any
        ) -> TokenHttpRequest: ...
        def list(self, *, userKey: str, **kwargs: typing.Any) -> TokensHttpRequest: ...

    @typing.type_check_only
    class TwoStepVerificationResource(googleapiclient.discovery.Resource):
        def turnOff(
            self, *, userKey: str, **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...

    @typing.type_check_only
    class UsersResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class AliasesResource(googleapiclient.discovery.Resource):
            def delete(
                self, *, userKey: str, alias: str, **kwargs: typing.Any
            ) -> googleapiclient.http.HttpRequest: ...
            def insert(
                self, *, userKey: str, body: Alias = ..., **kwargs: typing.Any
            ) -> AliasHttpRequest: ...
            def list(
                self,
                *,
                userKey: str,
                event: typing_extensions.Literal["add", "delete"] = ...,
                **kwargs: typing.Any
            ) -> AliasesHttpRequest: ...
            def watch(
                self,
                *,
                userKey: str,
                body: Channel = ...,
                event: typing_extensions.Literal["add", "delete"] = ...,
                **kwargs: typing.Any
            ) -> ChannelHttpRequest: ...

        @typing.type_check_only
        class PhotosResource(googleapiclient.discovery.Resource):
            def delete(
                self, *, userKey: str, **kwargs: typing.Any
            ) -> googleapiclient.http.HttpRequest: ...
            def get(
                self, *, userKey: str, **kwargs: typing.Any
            ) -> UserPhotoHttpRequest: ...
            def patch(
                self, *, userKey: str, body: UserPhoto = ..., **kwargs: typing.Any
            ) -> UserPhotoHttpRequest: ...
            def update(
                self, *, userKey: str, body: UserPhoto = ..., **kwargs: typing.Any
            ) -> UserPhotoHttpRequest: ...

        def delete(
            self, *, userKey: str, **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def get(
            self,
            *,
            userKey: str,
            customFieldMask: str = ...,
            projection: typing_extensions.Literal["basic", "custom", "full"] = ...,
            viewType: typing_extensions.Literal["admin_view", "domain_public"] = ...,
            **kwargs: typing.Any
        ) -> UserHttpRequest: ...
        def insert(
            self, *, body: User = ..., **kwargs: typing.Any
        ) -> UserHttpRequest: ...
        def list(
            self,
            *,
            customFieldMask: str = ...,
            customer: str = ...,
            domain: str = ...,
            event: typing_extensions.Literal[
                "add", "delete", "makeAdmin", "undelete", "update"
            ] = ...,
            maxResults: int = ...,
            orderBy: typing_extensions.Literal[
                "email", "familyName", "givenName"
            ] = ...,
            pageToken: str = ...,
            projection: typing_extensions.Literal["basic", "custom", "full"] = ...,
            query: str = ...,
            showDeleted: str = ...,
            sortOrder: typing_extensions.Literal["ASCENDING", "DESCENDING"] = ...,
            viewType: typing_extensions.Literal["admin_view", "domain_public"] = ...,
            **kwargs: typing.Any
        ) -> UsersHttpRequest: ...
        def list_next(
            self, previous_request: UsersHttpRequest, previous_response: Users
        ) -> UsersHttpRequest | None: ...
        def makeAdmin(
            self, *, userKey: str, body: UserMakeAdmin = ..., **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def patch(
            self, *, userKey: str, body: User = ..., **kwargs: typing.Any
        ) -> UserHttpRequest: ...
        def signOut(
            self, *, userKey: str, **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def undelete(
            self, *, userKey: str, body: UserUndelete = ..., **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def update(
            self, *, userKey: str, body: User = ..., **kwargs: typing.Any
        ) -> UserHttpRequest: ...
        def watch(
            self,
            *,
            body: Channel = ...,
            customFieldMask: str = ...,
            customer: str = ...,
            domain: str = ...,
            event: typing_extensions.Literal[
                "add", "delete", "makeAdmin", "undelete", "update"
            ] = ...,
            maxResults: int = ...,
            orderBy: typing_extensions.Literal[
                "email", "familyName", "givenName"
            ] = ...,
            pageToken: str = ...,
            projection: typing_extensions.Literal["basic", "custom", "full"] = ...,
            query: str = ...,
            showDeleted: str = ...,
            sortOrder: typing_extensions.Literal["ASCENDING", "DESCENDING"] = ...,
            viewType: typing_extensions.Literal["admin_view", "domain_public"] = ...,
            **kwargs: typing.Any
        ) -> ChannelHttpRequest: ...
        def aliases(self) -> AliasesResource: ...
        def photos(self) -> PhotosResource: ...

    @typing.type_check_only
    class VerificationCodesResource(googleapiclient.discovery.Resource):
        def generate(
            self, *, userKey: str, **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def invalidate(
            self, *, userKey: str, **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def list(
            self, *, userKey: str, **kwargs: typing.Any
        ) -> VerificationCodesHttpRequest: ...

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
    def asps(self) -> AspsResource: ...
    def channels(self) -> ChannelsResource: ...
    def chromeosdevices(self) -> ChromeosdevicesResource: ...
    def customer(self) -> CustomerResource: ...
    def customers(self) -> CustomersResource: ...
    def domainAliases(self) -> DomainAliasesResource: ...
    def domains(self) -> DomainsResource: ...
    def groups(self) -> GroupsResource: ...
    def members(self) -> MembersResource: ...
    def mobiledevices(self) -> MobiledevicesResource: ...
    def orgunits(self) -> OrgunitsResource: ...
    def privileges(self) -> PrivilegesResource: ...
    def resources(self) -> ResourcesResource: ...
    def roleAssignments(self) -> RoleAssignmentsResource: ...
    def roles(self) -> RolesResource: ...
    def schemas(self) -> SchemasResource: ...
    def tokens(self) -> TokensResource: ...
    def twoStepVerification(self) -> TwoStepVerificationResource: ...
    def users(self) -> UsersResource: ...
    def verificationCodes(self) -> VerificationCodesResource: ...

@typing.type_check_only
class AliasHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Alias: ...

@typing.type_check_only
class AliasesHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Aliases: ...

@typing.type_check_only
class AspHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Asp: ...

@typing.type_check_only
class AspsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Asps: ...

@typing.type_check_only
class BatchCreatePrintServersResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> BatchCreatePrintServersResponse: ...

@typing.type_check_only
class BatchCreatePrintersResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> BatchCreatePrintersResponse: ...

@typing.type_check_only
class BatchDeletePrintServersResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> BatchDeletePrintServersResponse: ...

@typing.type_check_only
class BatchDeletePrintersResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> BatchDeletePrintersResponse: ...

@typing.type_check_only
class BuildingHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Building: ...

@typing.type_check_only
class BuildingsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Buildings: ...

@typing.type_check_only
class CalendarResourceHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> CalendarResource: ...

@typing.type_check_only
class CalendarResourcesHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> CalendarResources: ...

@typing.type_check_only
class ChannelHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Channel: ...

@typing.type_check_only
class ChromeOsDeviceHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ChromeOsDevice: ...

@typing.type_check_only
class ChromeOsDevicesHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ChromeOsDevices: ...

@typing.type_check_only
class CustomerHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Customer: ...

@typing.type_check_only
class DirectoryChromeosdevicesCommandHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> DirectoryChromeosdevicesCommand: ...

@typing.type_check_only
class DirectoryChromeosdevicesIssueCommandResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> DirectoryChromeosdevicesIssueCommandResponse: ...

@typing.type_check_only
class DomainAliasHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> DomainAlias: ...

@typing.type_check_only
class DomainAliasesHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> DomainAliases: ...

@typing.type_check_only
class DomainsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Domains: ...

@typing.type_check_only
class Domains2HttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Domains2: ...

@typing.type_check_only
class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Empty: ...

@typing.type_check_only
class FeatureHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Feature: ...

@typing.type_check_only
class FeaturesHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Features: ...

@typing.type_check_only
class GroupHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Group: ...

@typing.type_check_only
class GroupsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Groups: ...

@typing.type_check_only
class ListPrintServersResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListPrintServersResponse: ...

@typing.type_check_only
class ListPrinterModelsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListPrinterModelsResponse: ...

@typing.type_check_only
class ListPrintersResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListPrintersResponse: ...

@typing.type_check_only
class MemberHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Member: ...

@typing.type_check_only
class MembersHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Members: ...

@typing.type_check_only
class MembersHasMemberHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> MembersHasMember: ...

@typing.type_check_only
class MobileDeviceHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> MobileDevice: ...

@typing.type_check_only
class MobileDevicesHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> MobileDevices: ...

@typing.type_check_only
class OrgUnitHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> OrgUnit: ...

@typing.type_check_only
class OrgUnitsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> OrgUnits: ...

@typing.type_check_only
class PrintServerHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> PrintServer: ...

@typing.type_check_only
class PrinterHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Printer: ...

@typing.type_check_only
class PrivilegesHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Privileges: ...

@typing.type_check_only
class RoleHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Role: ...

@typing.type_check_only
class RoleAssignmentHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> RoleAssignment: ...

@typing.type_check_only
class RoleAssignmentsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> RoleAssignments: ...

@typing.type_check_only
class RolesHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Roles: ...

@typing.type_check_only
class SchemaHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Schema: ...

@typing.type_check_only
class SchemasHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Schemas: ...

@typing.type_check_only
class TokenHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Token: ...

@typing.type_check_only
class TokensHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Tokens: ...

@typing.type_check_only
class UserHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> User: ...

@typing.type_check_only
class UserPhotoHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> UserPhoto: ...

@typing.type_check_only
class UsersHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Users: ...

@typing.type_check_only
class VerificationCodesHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> VerificationCodes: ...
