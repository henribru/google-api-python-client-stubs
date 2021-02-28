import typing

import typing_extensions
@typing.type_check_only
class CheckTransitiveMembershipResponse(typing_extensions.TypedDict, total=False):
    hasMembership: bool

@typing.type_check_only
class DynamicGroupMetadata(typing_extensions.TypedDict, total=False):
    queries: typing.List[DynamicGroupQuery]
    status: DynamicGroupStatus

@typing.type_check_only
class DynamicGroupQuery(typing_extensions.TypedDict, total=False):
    query: str
    resourceType: typing_extensions.Literal["RESOURCE_TYPE_UNSPECIFIED", "USER"]

@typing.type_check_only
class DynamicGroupStatus(typing_extensions.TypedDict, total=False):
    status: typing_extensions.Literal[
        "STATUS_UNSPECIFIED", "UP_TO_DATE", "UPDATING_MEMBERSHIPS"
    ]
    statusTime: str

@typing.type_check_only
class EntityKey(typing_extensions.TypedDict, total=False):
    id: str
    namespace: str

@typing.type_check_only
class ExpiryDetail(typing_extensions.TypedDict, total=False):
    expireTime: str

@typing.type_check_only
class GetMembershipGraphResponse(typing_extensions.TypedDict, total=False):
    adjacencyList: typing.List[MembershipAdjacencyList]
    groups: typing.List[Group]

@typing.type_check_only
class GoogleAppsCloudidentityDevicesV1AndroidAttributes(
    typing_extensions.TypedDict, total=False
):
    enabledUnknownSources: bool
    ownerProfileAccount: bool
    ownershipPrivilege: typing_extensions.Literal[
        "OWNERSHIP_PRIVILEGE_UNSPECIFIED",
        "DEVICE_ADMINISTRATOR",
        "PROFILE_OWNER",
        "DEVICE_OWNER",
    ]
    supportsWorkProfile: bool

@typing.type_check_only
class GoogleAppsCloudidentityDevicesV1ApproveDeviceUserRequest(
    typing_extensions.TypedDict, total=False
):
    customer: str

@typing.type_check_only
class GoogleAppsCloudidentityDevicesV1ApproveDeviceUserResponse(
    typing_extensions.TypedDict, total=False
):
    deviceUser: GoogleAppsCloudidentityDevicesV1DeviceUser

@typing.type_check_only
class GoogleAppsCloudidentityDevicesV1BlockDeviceUserRequest(
    typing_extensions.TypedDict, total=False
):
    customer: str

@typing.type_check_only
class GoogleAppsCloudidentityDevicesV1BlockDeviceUserResponse(
    typing_extensions.TypedDict, total=False
):
    deviceUser: GoogleAppsCloudidentityDevicesV1DeviceUser

@typing.type_check_only
class GoogleAppsCloudidentityDevicesV1CancelWipeDeviceRequest(
    typing_extensions.TypedDict, total=False
):
    customer: str

@typing.type_check_only
class GoogleAppsCloudidentityDevicesV1CancelWipeDeviceResponse(
    typing_extensions.TypedDict, total=False
):
    device: GoogleAppsCloudidentityDevicesV1Device

@typing.type_check_only
class GoogleAppsCloudidentityDevicesV1CancelWipeDeviceUserRequest(
    typing_extensions.TypedDict, total=False
):
    customer: str

@typing.type_check_only
class GoogleAppsCloudidentityDevicesV1CancelWipeDeviceUserResponse(
    typing_extensions.TypedDict, total=False
):
    deviceUser: GoogleAppsCloudidentityDevicesV1DeviceUser

@typing.type_check_only
class GoogleAppsCloudidentityDevicesV1ClientState(
    typing_extensions.TypedDict, total=False
):
    assetTags: typing.List[str]
    complianceState: typing_extensions.Literal[
        "COMPLIANCE_STATE_UNSPECIFIED", "COMPLIANT", "NON_COMPLIANT"
    ]
    createTime: str
    customId: str
    etag: str
    healthScore: typing_extensions.Literal[
        "HEALTH_SCORE_UNSPECIFIED", "VERY_POOR", "POOR", "NEUTRAL", "GOOD", "VERY_GOOD"
    ]
    keyValuePairs: typing.Dict[str, typing.Any]
    lastUpdateTime: str
    managed: typing_extensions.Literal[
        "MANAGED_STATE_UNSPECIFIED", "MANAGED", "UNMANAGED"
    ]
    name: str
    ownerType: typing_extensions.Literal[
        "OWNER_TYPE_UNSPECIFIED", "OWNER_TYPE_CUSTOMER", "OWNER_TYPE_PARTNER"
    ]
    scoreReason: str

@typing.type_check_only
class GoogleAppsCloudidentityDevicesV1CustomAttributeValue(
    typing_extensions.TypedDict, total=False
):
    boolValue: bool
    numberValue: float
    stringValue: str

@typing.type_check_only
class GoogleAppsCloudidentityDevicesV1Device(typing_extensions.TypedDict, total=False):
    androidSpecificAttributes: GoogleAppsCloudidentityDevicesV1AndroidAttributes
    assetTag: str
    basebandVersion: str
    bootloaderVersion: str
    brand: str
    buildNumber: str
    compromisedState: typing_extensions.Literal[
        "COMPROMISED_STATE_UNSPECIFIED", "COMPROMISED", "UNCOMPROMISED"
    ]
    createTime: str
    deviceType: typing_extensions.Literal[
        "DEVICE_TYPE_UNSPECIFIED",
        "ANDROID",
        "IOS",
        "GOOGLE_SYNC",
        "WINDOWS",
        "MAC_OS",
        "LINUX",
        "CHROME_OS",
    ]
    enabledDeveloperOptions: bool
    enabledUsbDebugging: bool
    encryptionState: typing_extensions.Literal[
        "ENCRYPTION_STATE_UNSPECIFIED",
        "UNSUPPORTED_BY_DEVICE",
        "ENCRYPTED",
        "NOT_ENCRYPTED",
    ]
    imei: str
    kernelVersion: str
    lastSyncTime: str
    managementState: typing_extensions.Literal[
        "MANAGEMENT_STATE_UNSPECIFIED",
        "APPROVED",
        "BLOCKED",
        "PENDING",
        "UNPROVISIONED",
        "WIPING",
        "WIPED",
    ]
    manufacturer: str
    meid: str
    model: str
    name: str
    networkOperator: str
    osVersion: str
    otherAccounts: typing.List[str]
    ownerType: typing_extensions.Literal[
        "DEVICE_OWNERSHIP_UNSPECIFIED", "COMPANY", "BYOD"
    ]
    releaseVersion: str
    securityPatchTime: str
    serialNumber: str
    wifiMacAddresses: typing.List[str]

@typing.type_check_only
class GoogleAppsCloudidentityDevicesV1DeviceUser(
    typing_extensions.TypedDict, total=False
):
    compromisedState: typing_extensions.Literal[
        "COMPROMISED_STATE_UNSPECIFIED", "COMPROMISED", "NOT_COMPROMISED"
    ]
    createTime: str
    firstSyncTime: str
    languageCode: str
    lastSyncTime: str
    managementState: typing_extensions.Literal[
        "MANAGEMENT_STATE_UNSPECIFIED",
        "WIPING",
        "WIPED",
        "APPROVED",
        "BLOCKED",
        "PENDING_APPROVAL",
        "UNENROLLED",
    ]
    name: str
    passwordState: typing_extensions.Literal[
        "PASSWORD_STATE_UNSPECIFIED", "PASSWORD_SET", "PASSWORD_NOT_SET"
    ]
    userAgent: str
    userEmail: str

@typing.type_check_only
class GoogleAppsCloudidentityDevicesV1ListClientStatesResponse(
    typing_extensions.TypedDict, total=False
):
    clientStates: typing.List[GoogleAppsCloudidentityDevicesV1ClientState]
    nextPageToken: str

@typing.type_check_only
class GoogleAppsCloudidentityDevicesV1ListDeviceUsersResponse(
    typing_extensions.TypedDict, total=False
):
    deviceUsers: typing.List[GoogleAppsCloudidentityDevicesV1DeviceUser]
    nextPageToken: str

@typing.type_check_only
class GoogleAppsCloudidentityDevicesV1ListDevicesResponse(
    typing_extensions.TypedDict, total=False
):
    devices: typing.List[GoogleAppsCloudidentityDevicesV1Device]
    nextPageToken: str

@typing.type_check_only
class GoogleAppsCloudidentityDevicesV1LookupSelfDeviceUsersResponse(
    typing_extensions.TypedDict, total=False
):
    customer: str
    names: typing.List[str]
    nextPageToken: str

@typing.type_check_only
class GoogleAppsCloudidentityDevicesV1WipeDeviceRequest(
    typing_extensions.TypedDict, total=False
):
    customer: str

@typing.type_check_only
class GoogleAppsCloudidentityDevicesV1WipeDeviceResponse(
    typing_extensions.TypedDict, total=False
):
    device: GoogleAppsCloudidentityDevicesV1Device

@typing.type_check_only
class GoogleAppsCloudidentityDevicesV1WipeDeviceUserRequest(
    typing_extensions.TypedDict, total=False
):
    customer: str

@typing.type_check_only
class GoogleAppsCloudidentityDevicesV1WipeDeviceUserResponse(
    typing_extensions.TypedDict, total=False
):
    deviceUser: GoogleAppsCloudidentityDevicesV1DeviceUser

@typing.type_check_only
class Group(typing_extensions.TypedDict, total=False):
    createTime: str
    description: str
    displayName: str
    dynamicGroupMetadata: DynamicGroupMetadata
    groupKey: EntityKey
    labels: typing.Dict[str, typing.Any]
    name: str
    parent: str
    updateTime: str

@typing.type_check_only
class GroupRelation(typing_extensions.TypedDict, total=False):
    displayName: str
    group: str
    groupKey: EntityKey
    labels: typing.Dict[str, typing.Any]
    relationType: typing_extensions.Literal[
        "RELATION_TYPE_UNSPECIFIED", "DIRECT", "INDIRECT", "DIRECT_AND_INDIRECT"
    ]
    roles: typing.List[TransitiveMembershipRole]

@typing.type_check_only
class ListGroupsResponse(typing_extensions.TypedDict, total=False):
    groups: typing.List[Group]
    nextPageToken: str

@typing.type_check_only
class ListMembershipsResponse(typing_extensions.TypedDict, total=False):
    memberships: typing.List[Membership]
    nextPageToken: str

@typing.type_check_only
class LookupGroupNameResponse(typing_extensions.TypedDict, total=False):
    name: str

@typing.type_check_only
class LookupMembershipNameResponse(typing_extensions.TypedDict, total=False):
    name: str

@typing.type_check_only
class MemberRelation(typing_extensions.TypedDict, total=False):
    member: str
    preferredMemberKey: typing.List[EntityKey]
    relationType: typing_extensions.Literal[
        "RELATION_TYPE_UNSPECIFIED", "DIRECT", "INDIRECT", "DIRECT_AND_INDIRECT"
    ]
    roles: typing.List[TransitiveMembershipRole]

@typing.type_check_only
class Membership(typing_extensions.TypedDict, total=False):
    createTime: str
    name: str
    preferredMemberKey: EntityKey
    roles: typing.List[MembershipRole]
    type: typing_extensions.Literal[
        "TYPE_UNSPECIFIED", "USER", "SERVICE_ACCOUNT", "GROUP", "OTHER"
    ]
    updateTime: str

@typing.type_check_only
class MembershipAdjacencyList(typing_extensions.TypedDict, total=False):
    edges: typing.List[Membership]
    group: str

@typing.type_check_only
class MembershipRole(typing_extensions.TypedDict, total=False):
    expiryDetail: ExpiryDetail
    name: str

@typing.type_check_only
class ModifyMembershipRolesRequest(typing_extensions.TypedDict, total=False):
    addRoles: typing.List[MembershipRole]
    removeRoles: typing.List[str]
    updateRolesParams: typing.List[UpdateMembershipRolesParams]

@typing.type_check_only
class ModifyMembershipRolesResponse(typing_extensions.TypedDict, total=False):
    membership: Membership

@typing.type_check_only
class Operation(typing_extensions.TypedDict, total=False):
    done: bool
    error: Status
    metadata: typing.Dict[str, typing.Any]
    name: str
    response: typing.Dict[str, typing.Any]

@typing.type_check_only
class SearchGroupsResponse(typing_extensions.TypedDict, total=False):
    groups: typing.List[Group]
    nextPageToken: str

@typing.type_check_only
class SearchTransitiveGroupsResponse(typing_extensions.TypedDict, total=False):
    memberships: typing.List[GroupRelation]
    nextPageToken: str

@typing.type_check_only
class SearchTransitiveMembershipsResponse(typing_extensions.TypedDict, total=False):
    memberships: typing.List[MemberRelation]
    nextPageToken: str

@typing.type_check_only
class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: typing.List[typing.Dict[str, typing.Any]]
    message: str

@typing.type_check_only
class TransitiveMembershipRole(typing_extensions.TypedDict, total=False):
    role: str

@typing.type_check_only
class UpdateMembershipRolesParams(typing_extensions.TypedDict, total=False):
    fieldMask: str
    membershipRole: MembershipRole

@typing.type_check_only
class UserInvitation(typing_extensions.TypedDict, total=False):
    mailsSentCount: str
    name: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "NOT_YET_SENT", "INVITED", "ACCEPTED", "DECLINED"
    ]
    updateTime: str
