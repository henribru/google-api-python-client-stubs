import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class DirectoryResource(googleapiclient.discovery.Resource):
    class GroupsResource(googleapiclient.discovery.Resource):
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
        def insert(
            self, *, body: Group = ..., **kwargs: typing.Any
        ) -> GroupHttpRequest: ...
        def patch(
            self, *, groupKey: str, body: Group = ..., **kwargs: typing.Any
        ) -> GroupHttpRequest: ...
        def get(self, *, groupKey: str, **kwargs: typing.Any) -> GroupHttpRequest: ...
        def delete(
            self, *, groupKey: str, **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def update(
            self, *, groupKey: str, body: Group = ..., **kwargs: typing.Any
        ) -> GroupHttpRequest: ...
        def list(
            self,
            *,
            pageToken: str = ...,
            customer: str = ...,
            domain: str = ...,
            maxResults: int = ...,
            sortOrder: typing_extensions.Literal[
                "SORT_ORDER_UNDEFINED", "ASCENDING", "DESCENDING"
            ] = ...,
            query: str = ...,
            orderBy: typing_extensions.Literal["orderByUndefined", "email"] = ...,
            userKey: str = ...,
            **kwargs: typing.Any
        ) -> GroupsHttpRequest: ...
        def aliases(self) -> AliasesResource: ...
    class UsersResource(googleapiclient.discovery.Resource):
        class PhotosResource(googleapiclient.discovery.Resource):
            def delete(
                self, *, userKey: str, **kwargs: typing.Any
            ) -> googleapiclient.http.HttpRequest: ...
            def patch(
                self, *, userKey: str, body: UserPhoto = ..., **kwargs: typing.Any
            ) -> UserPhotoHttpRequest: ...
            def update(
                self, *, userKey: str, body: UserPhoto = ..., **kwargs: typing.Any
            ) -> UserPhotoHttpRequest: ...
            def get(
                self, *, userKey: str, **kwargs: typing.Any
            ) -> UserPhotoHttpRequest: ...
        class AliasesResource(googleapiclient.discovery.Resource):
            def insert(
                self, *, userKey: str, body: Alias = ..., **kwargs: typing.Any
            ) -> AliasHttpRequest: ...
            def watch(
                self,
                *,
                userKey: str,
                body: Channel = ...,
                event: typing_extensions.Literal[
                    "eventUndefined", "add", "delete"
                ] = ...,
                **kwargs: typing.Any
            ) -> ChannelHttpRequest: ...
            def list(
                self, *, userKey: str, **kwargs: typing.Any
            ) -> AliasesHttpRequest: ...
            def delete(
                self, *, userKey: str, alias: str, **kwargs: typing.Any
            ) -> googleapiclient.http.HttpRequest: ...
        def get(
            self,
            *,
            userKey: str,
            viewType: typing_extensions.Literal[
                "view_type_undefined", "admin_view", "domain_public"
            ] = ...,
            customFieldMask: str = ...,
            projection: typing_extensions.Literal[
                "projectionUndefined", "basic", "custom", "full"
            ] = ...,
            **kwargs: typing.Any
        ) -> UserHttpRequest: ...
        def makeAdmin(
            self, *, userKey: str, body: UserMakeAdmin = ..., **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def update(
            self, *, userKey: str, body: User = ..., **kwargs: typing.Any
        ) -> UserHttpRequest: ...
        def insert(
            self, *, body: User = ..., **kwargs: typing.Any
        ) -> UserHttpRequest: ...
        def list(
            self,
            *,
            domain: str = ...,
            query: str = ...,
            orderBy: typing_extensions.Literal[
                "orderByUndefined", "email", "familyName", "givenName"
            ] = ...,
            maxResults: int = ...,
            sortOrder: typing_extensions.Literal[
                "SORT_ORDER_UNDEFINED", "ASCENDING", "DESCENDING"
            ] = ...,
            viewType: typing_extensions.Literal[
                "view_type_undefined", "admin_view", "domain_public"
            ] = ...,
            projection: typing_extensions.Literal[
                "projectionUndefined", "basic", "custom", "full"
            ] = ...,
            showDeleted: str = ...,
            customFieldMask: str = ...,
            pageToken: str = ...,
            customer: str = ...,
            **kwargs: typing.Any
        ) -> UsersHttpRequest: ...
        def undelete(
            self, *, userKey: str, body: UserUndelete = ..., **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def signOut(
            self, *, userKey: str, **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def patch(
            self, *, userKey: str, body: User = ..., **kwargs: typing.Any
        ) -> UserHttpRequest: ...
        def delete(
            self, *, userKey: str, **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def watch(
            self,
            *,
            body: Channel = ...,
            sortOrder: typing_extensions.Literal[
                "sortOrderUnspecified", "ASCENDING", "DESCENDING"
            ] = ...,
            pageToken: str = ...,
            event: typing_extensions.Literal[
                "eventTypeUnspecified",
                "add",
                "delete",
                "makeAdmin",
                "undelete",
                "update",
            ] = ...,
            orderBy: typing_extensions.Literal[
                "orderByUnspecified", "email", "familyName", "givenName"
            ] = ...,
            customer: str = ...,
            query: str = ...,
            viewType: typing_extensions.Literal["admin_view", "domain_public"] = ...,
            maxResults: int = ...,
            customFieldMask: str = ...,
            showDeleted: str = ...,
            domain: str = ...,
            projection: typing_extensions.Literal[
                "projectionUnspecified", "basic", "custom", "full"
            ] = ...,
            **kwargs: typing.Any
        ) -> ChannelHttpRequest: ...
        def photos(self) -> PhotosResource: ...
        def aliases(self) -> AliasesResource: ...
    class AspsResource(googleapiclient.discovery.Resource):
        def delete(
            self, *, userKey: str, codeId: int, **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def get(
            self, *, userKey: str, codeId: int, **kwargs: typing.Any
        ) -> AspHttpRequest: ...
        def list(self, *, userKey: str, **kwargs: typing.Any) -> AspsHttpRequest: ...
    class MobiledevicesResource(googleapiclient.discovery.Resource):
        def delete(
            self, *, customerId: str, resourceId: str, **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def action(
            self,
            *,
            customerId: str,
            resourceId: str,
            body: MobileDeviceAction = ...,
            **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def get(
            self,
            *,
            customerId: str,
            resourceId: str,
            projection: typing_extensions.Literal[
                "PROJECTION_UNDEFINED", "BASIC", "FULL"
            ] = ...,
            **kwargs: typing.Any
        ) -> MobileDeviceHttpRequest: ...
        def list(
            self,
            *,
            customerId: str,
            projection: typing_extensions.Literal[
                "PROJECTION_UNDEFINED", "BASIC", "FULL"
            ] = ...,
            maxResults: int = ...,
            pageToken: str = ...,
            orderBy: typing_extensions.Literal[
                "orderByUndefined",
                "deviceId",
                "email",
                "lastSync",
                "model",
                "name",
                "os",
                "status",
                "type",
            ] = ...,
            query: str = ...,
            sortOrder: typing_extensions.Literal[
                "SORT_ORDER_UNDEFINED", "ASCENDING", "DESCENDING"
            ] = ...,
            **kwargs: typing.Any
        ) -> MobileDevicesHttpRequest: ...
    class PrivilegesResource(googleapiclient.discovery.Resource):
        def list(
            self, *, customer: str, **kwargs: typing.Any
        ) -> PrivilegesHttpRequest: ...
    class SchemasResource(googleapiclient.discovery.Resource):
        def update(
            self,
            *,
            customerId: str,
            schemaKey: str,
            body: Schema = ...,
            **kwargs: typing.Any
        ) -> SchemaHttpRequest: ...
        def insert(
            self, *, customerId: str, body: Schema = ..., **kwargs: typing.Any
        ) -> SchemaHttpRequest: ...
        def patch(
            self,
            *,
            customerId: str,
            schemaKey: str,
            body: Schema = ...,
            **kwargs: typing.Any
        ) -> SchemaHttpRequest: ...
        def delete(
            self, *, customerId: str, schemaKey: str, **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def get(
            self, *, customerId: str, schemaKey: str, **kwargs: typing.Any
        ) -> SchemaHttpRequest: ...
        def list(
            self, *, customerId: str, **kwargs: typing.Any
        ) -> SchemasHttpRequest: ...
    class RolesResource(googleapiclient.discovery.Resource):
        def list(
            self,
            *,
            customer: str,
            maxResults: int = ...,
            pageToken: str = ...,
            **kwargs: typing.Any
        ) -> RolesHttpRequest: ...
        def get(
            self, *, customer: str, roleId: str, **kwargs: typing.Any
        ) -> RoleHttpRequest: ...
        def update(
            self, *, customer: str, roleId: str, body: Role = ..., **kwargs: typing.Any
        ) -> RoleHttpRequest: ...
        def patch(
            self, *, customer: str, roleId: str, body: Role = ..., **kwargs: typing.Any
        ) -> RoleHttpRequest: ...
        def delete(
            self, *, customer: str, roleId: str, **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def insert(
            self, *, customer: str, body: Role = ..., **kwargs: typing.Any
        ) -> RoleHttpRequest: ...
    class CustomersResource(googleapiclient.discovery.Resource):
        def get(
            self, *, customerKey: str, **kwargs: typing.Any
        ) -> CustomerHttpRequest: ...
        def update(
            self, *, customerKey: str, body: Customer = ..., **kwargs: typing.Any
        ) -> CustomerHttpRequest: ...
        def patch(
            self, *, customerKey: str, body: Customer = ..., **kwargs: typing.Any
        ) -> CustomerHttpRequest: ...
    class ResourcesResource(googleapiclient.discovery.Resource):
        class BuildingsResource(googleapiclient.discovery.Resource):
            def update(
                self,
                *,
                customer: str,
                buildingId: str,
                body: Building = ...,
                coordinatesSource: typing_extensions.Literal[
                    "COORDINATES_SOURCE_UNDEFINED",
                    "CLIENT_SPECIFIED",
                    "RESOLVED_FROM_ADDRESS",
                    "SOURCE_UNSPECIFIED",
                ] = ...,
                **kwargs: typing.Any
            ) -> BuildingHttpRequest: ...
            def patch(
                self,
                *,
                customer: str,
                buildingId: str,
                body: Building = ...,
                coordinatesSource: typing_extensions.Literal[
                    "COORDINATES_SOURCE_UNDEFINED",
                    "CLIENT_SPECIFIED",
                    "RESOLVED_FROM_ADDRESS",
                    "SOURCE_UNSPECIFIED",
                ] = ...,
                **kwargs: typing.Any
            ) -> BuildingHttpRequest: ...
            def delete(
                self, *, customer: str, buildingId: str, **kwargs: typing.Any
            ) -> googleapiclient.http.HttpRequest: ...
            def insert(
                self,
                *,
                customer: str,
                body: Building = ...,
                coordinatesSource: typing_extensions.Literal[
                    "COORDINATES_SOURCE_UNDEFINED",
                    "CLIENT_SPECIFIED",
                    "RESOLVED_FROM_ADDRESS",
                    "SOURCE_UNSPECIFIED",
                ] = ...,
                **kwargs: typing.Any
            ) -> BuildingHttpRequest: ...
            def get(
                self, *, customer: str, buildingId: str, **kwargs: typing.Any
            ) -> BuildingHttpRequest: ...
            def list(
                self,
                *,
                customer: str,
                pageToken: str = ...,
                maxResults: int = ...,
                **kwargs: typing.Any
            ) -> BuildingsHttpRequest: ...
        class FeaturesResource(googleapiclient.discovery.Resource):
            def update(
                self,
                *,
                customer: str,
                featureKey: str,
                body: Feature = ...,
                **kwargs: typing.Any
            ) -> FeatureHttpRequest: ...
            def delete(
                self, *, customer: str, featureKey: str, **kwargs: typing.Any
            ) -> googleapiclient.http.HttpRequest: ...
            def rename(
                self,
                *,
                customer: str,
                oldName: str,
                body: FeatureRename = ...,
                **kwargs: typing.Any
            ) -> googleapiclient.http.HttpRequest: ...
            def patch(
                self,
                *,
                customer: str,
                featureKey: str,
                body: Feature = ...,
                **kwargs: typing.Any
            ) -> FeatureHttpRequest: ...
            def list(
                self,
                *,
                customer: str,
                pageToken: str = ...,
                maxResults: int = ...,
                **kwargs: typing.Any
            ) -> FeaturesHttpRequest: ...
            def insert(
                self, *, customer: str, body: Feature = ..., **kwargs: typing.Any
            ) -> FeatureHttpRequest: ...
            def get(
                self, *, customer: str, featureKey: str, **kwargs: typing.Any
            ) -> FeatureHttpRequest: ...
        class CalendarsResource(googleapiclient.discovery.Resource):
            def get(
                self, *, customer: str, calendarResourceId: str, **kwargs: typing.Any
            ) -> CalendarResourceHttpRequest: ...
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
            def delete(
                self, *, customer: str, calendarResourceId: str, **kwargs: typing.Any
            ) -> googleapiclient.http.HttpRequest: ...
            def list(
                self,
                *,
                customer: str,
                pageToken: str = ...,
                maxResults: int = ...,
                query: str = ...,
                orderBy: str = ...,
                **kwargs: typing.Any
            ) -> CalendarResourcesHttpRequest: ...
            def insert(
                self,
                *,
                customer: str,
                body: CalendarResource = ...,
                **kwargs: typing.Any
            ) -> CalendarResourceHttpRequest: ...
        def buildings(self) -> BuildingsResource: ...
        def features(self) -> FeaturesResource: ...
        def calendars(self) -> CalendarsResource: ...
    class MembersResource(googleapiclient.discovery.Resource):
        def patch(
            self,
            *,
            groupKey: str,
            memberKey: str,
            body: Member = ...,
            **kwargs: typing.Any
        ) -> MemberHttpRequest: ...
        def insert(
            self, *, groupKey: str, body: Member = ..., **kwargs: typing.Any
        ) -> MemberHttpRequest: ...
        def hasMember(
            self, *, groupKey: str, memberKey: str, **kwargs: typing.Any
        ) -> MembersHasMemberHttpRequest: ...
        def list(
            self,
            *,
            groupKey: str,
            roles: str = ...,
            maxResults: int = ...,
            includeDerivedMembership: bool = ...,
            pageToken: str = ...,
            **kwargs: typing.Any
        ) -> MembersHttpRequest: ...
        def update(
            self,
            *,
            groupKey: str,
            memberKey: str,
            body: Member = ...,
            **kwargs: typing.Any
        ) -> MemberHttpRequest: ...
        def delete(
            self, *, groupKey: str, memberKey: str, **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def get(
            self, *, groupKey: str, memberKey: str, **kwargs: typing.Any
        ) -> MemberHttpRequest: ...
    class TokensResource(googleapiclient.discovery.Resource):
        def delete(
            self, *, userKey: str, clientId: str, **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def get(
            self, *, userKey: str, clientId: str, **kwargs: typing.Any
        ) -> TokenHttpRequest: ...
        def list(self, *, userKey: str, **kwargs: typing.Any) -> TokensHttpRequest: ...
    class RoleAssignmentsResource(googleapiclient.discovery.Resource):
        def delete(
            self, *, customer: str, roleAssignmentId: str, **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def insert(
            self, *, customer: str, body: RoleAssignment = ..., **kwargs: typing.Any
        ) -> RoleAssignmentHttpRequest: ...
        def list(
            self,
            *,
            customer: str,
            maxResults: int = ...,
            roleId: str = ...,
            pageToken: str = ...,
            userKey: str = ...,
            **kwargs: typing.Any
        ) -> RoleAssignmentsHttpRequest: ...
        def get(
            self, *, customer: str, roleAssignmentId: str, **kwargs: typing.Any
        ) -> RoleAssignmentHttpRequest: ...
    class VerificationCodesResource(googleapiclient.discovery.Resource):
        def list(
            self, *, userKey: str, **kwargs: typing.Any
        ) -> VerificationCodesHttpRequest: ...
        def invalidate(
            self, *, userKey: str, **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def generate(
            self, *, userKey: str, **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
    class DomainAliasesResource(googleapiclient.discovery.Resource):
        def list(
            self, *, customer: str, parentDomainName: str = ..., **kwargs: typing.Any
        ) -> DomainAliasesHttpRequest: ...
        def get(
            self, *, customer: str, domainAliasName: str, **kwargs: typing.Any
        ) -> DomainAliasHttpRequest: ...
        def delete(
            self, *, customer: str, domainAliasName: str, **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def insert(
            self, *, customer: str, body: DomainAlias = ..., **kwargs: typing.Any
        ) -> DomainAliasHttpRequest: ...
    class ChromeosdevicesResource(googleapiclient.discovery.Resource):
        def get(
            self,
            *,
            customerId: str,
            deviceId: str,
            projection: typing_extensions.Literal[
                "PROJECTION_UNDEFINED", "BASIC", "FULL"
            ] = ...,
            **kwargs: typing.Any
        ) -> ChromeOsDeviceHttpRequest: ...
        def moveDevicesToOu(
            self,
            *,
            customerId: str,
            orgUnitPath: str,
            body: ChromeOsMoveDevicesToOu = ...,
            **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def list(
            self,
            *,
            customerId: str,
            projection: typing_extensions.Literal[
                "PROJECTION_UNDEFINED", "BASIC", "FULL"
            ] = ...,
            query: str = ...,
            maxResults: int = ...,
            pageToken: str = ...,
            orgUnitPath: str = ...,
            sortOrder: typing_extensions.Literal[
                "SORT_ORDER_UNDEFINED", "ASCENDING", "DESCENDING"
            ] = ...,
            orderBy: typing_extensions.Literal[
                "orderByUndefined",
                "annotatedLocation",
                "annotatedUser",
                "lastSync",
                "notes",
                "serialNumber",
                "status",
                "supportEndDate",
            ] = ...,
            **kwargs: typing.Any
        ) -> ChromeOsDevicesHttpRequest: ...
        def patch(
            self,
            *,
            customerId: str,
            deviceId: str,
            body: ChromeOsDevice = ...,
            projection: typing_extensions.Literal[
                "PROJECTION_UNDEFINED", "BASIC", "FULL"
            ] = ...,
            **kwargs: typing.Any
        ) -> ChromeOsDeviceHttpRequest: ...
        def action(
            self,
            *,
            customerId: str,
            resourceId: str,
            body: ChromeOsDeviceAction = ...,
            **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def update(
            self,
            *,
            customerId: str,
            deviceId: str,
            body: ChromeOsDevice = ...,
            projection: typing_extensions.Literal[
                "PROJECTION_UNDEFINED", "BASIC", "FULL"
            ] = ...,
            **kwargs: typing.Any
        ) -> ChromeOsDeviceHttpRequest: ...
    class OrgunitsResource(googleapiclient.discovery.Resource):
        def list(
            self,
            *,
            customerId: str,
            type: typing_extensions.Literal["typeUndefined", "all", "children"] = ...,
            orgUnitPath: str = ...,
            **kwargs: typing.Any
        ) -> OrgUnitsHttpRequest: ...
        def get(
            self, *, customerId: str, orgUnitPath: str, **kwargs: typing.Any
        ) -> OrgUnitHttpRequest: ...
        def insert(
            self, *, customerId: str, body: OrgUnit = ..., **kwargs: typing.Any
        ) -> OrgUnitHttpRequest: ...
        def update(
            self,
            *,
            customerId: str,
            orgUnitPath: str,
            body: OrgUnit = ...,
            **kwargs: typing.Any
        ) -> OrgUnitHttpRequest: ...
        def patch(
            self,
            *,
            customerId: str,
            orgUnitPath: str,
            body: OrgUnit = ...,
            **kwargs: typing.Any
        ) -> OrgUnitHttpRequest: ...
        def delete(
            self, *, customerId: str, orgUnitPath: str, **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
    class DomainsResource(googleapiclient.discovery.Resource):
        def insert(
            self, *, customer: str, body: Domains = ..., **kwargs: typing.Any
        ) -> DomainsHttpRequest: ...
        def list(
            self, *, customer: str, **kwargs: typing.Any
        ) -> Domains2HttpRequest: ...
        def delete(
            self, *, customer: str, domainName: str, **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def get(
            self, *, customer: str, domainName: str, **kwargs: typing.Any
        ) -> DomainsHttpRequest: ...
    class ChannelsResource(googleapiclient.discovery.Resource):
        def stop(
            self, *, body: Channel = ..., **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
    class TwoStepVerificationResource(googleapiclient.discovery.Resource):
        def turnOff(
            self, *, userKey: str, **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
    def groups(self) -> GroupsResource: ...
    def users(self) -> UsersResource: ...
    def asps(self) -> AspsResource: ...
    def mobiledevices(self) -> MobiledevicesResource: ...
    def privileges(self) -> PrivilegesResource: ...
    def schemas(self) -> SchemasResource: ...
    def roles(self) -> RolesResource: ...
    def customers(self) -> CustomersResource: ...
    def resources(self) -> ResourcesResource: ...
    def members(self) -> MembersResource: ...
    def tokens(self) -> TokensResource: ...
    def roleAssignments(self) -> RoleAssignmentsResource: ...
    def verificationCodes(self) -> VerificationCodesResource: ...
    def domainAliases(self) -> DomainAliasesResource: ...
    def chromeosdevices(self) -> ChromeosdevicesResource: ...
    def orgunits(self) -> OrgunitsResource: ...
    def domains(self) -> DomainsResource: ...
    def channels(self) -> ChannelsResource: ...
    def twoStepVerification(self) -> TwoStepVerificationResource: ...

class PrivilegesHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Privileges: ...

class SchemasHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Schemas: ...

class CalendarResourcesHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> CalendarResources: ...

class SchemaHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Schema: ...

class FeaturesHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Features: ...

class BuildingHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Building: ...

class AliasesHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Aliases: ...

class MembersHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Members: ...

class ChannelHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Channel: ...

class AspsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Asps: ...

class RoleAssignmentsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> RoleAssignments: ...

class RoleAssignmentHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> RoleAssignment: ...

class DomainAliasHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> DomainAlias: ...

class RolesHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Roles: ...

class GroupHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Group: ...

class FeatureHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Feature: ...

class OrgUnitHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> OrgUnit: ...

class UsersHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Users: ...

class DomainsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Domains: ...

class MobileDevicesHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> MobileDevices: ...

class MembersHasMemberHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> MembersHasMember: ...

class GroupsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Groups: ...

class TokenHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Token: ...

class RoleHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Role: ...

class MobileDeviceHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> MobileDevice: ...

class CalendarResourceHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> CalendarResource: ...

class MemberHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Member: ...

class VerificationCodesHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> VerificationCodes: ...

class OrgUnitsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> OrgUnits: ...

class DomainAliasesHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> DomainAliases: ...

class BuildingsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Buildings: ...

class TokensHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Tokens: ...

class ChromeOsDeviceHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ChromeOsDevice: ...

class UserPhotoHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> UserPhoto: ...

class ChromeOsDevicesHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ChromeOsDevices: ...

class CustomerHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Customer: ...

class Domains2HttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Domains2: ...

class UserHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> User: ...

class AspHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Asp: ...

class AliasHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Alias: ...
