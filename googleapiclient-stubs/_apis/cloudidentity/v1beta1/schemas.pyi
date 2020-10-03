import typing

import typing_extensions

class Group(typing_extensions.TypedDict, total=False):
    groupKey: EntityKey
    dynamicGroupMetadata: DynamicGroupMetadata
    createTime: str
    updateTime: str
    description: str
    parent: str
    displayName: str
    name: str
    additionalGroupKeys: typing.List[EntityKey]
    labels: typing.Dict[str, typing.Any]

class Operation(typing_extensions.TypedDict, total=False):
    error: Status
    metadata: typing.Dict[str, typing.Any]
    name: str
    done: bool
    response: typing.Dict[str, typing.Any]

class Status(typing_extensions.TypedDict, total=False):
    details: typing.List[typing.Dict[str, typing.Any]]
    message: str
    code: int

class EntityKey(typing_extensions.TypedDict, total=False):
    namespace: str
    id: str

class WipeDeviceResponse(typing_extensions.TypedDict, total=False):
    device: Device

class TransitiveMembershipRole(typing_extensions.TypedDict, total=False):
    role: str

class LookupGroupNameResponse(typing_extensions.TypedDict, total=False):
    name: str

class WipeDeviceUserResponse(typing_extensions.TypedDict, total=False):
    deviceUser: DeviceUser

class BlockDeviceUserRequest(typing_extensions.TypedDict, total=False):
    customer: str

class UpdateMembershipRolesParams(typing_extensions.TypedDict, total=False):
    membershipRole: MembershipRole
    fieldMask: str

class GetMembershipGraphResponse(typing_extensions.TypedDict, total=False):
    groups: typing.List[Group]
    adjacencyList: typing.List[MembershipAdjacencyList]

class GoogleAppsCloudidentityDevicesV1ClientState(
    typing_extensions.TypedDict, total=False
):
    complianceState: typing_extensions.Literal[
        "COMPLIANCE_STATE_UNSPECIFIED", "COMPLIANT", "NON_COMPLIANT"
    ]
    etag: str
    ownerType: typing_extensions.Literal[
        "OWNER_TYPE_UNSPECIFIED", "OWNER_TYPE_CUSTOMER", "OWNER_TYPE_PARTNER"
    ]
    managed: typing_extensions.Literal[
        "MANAGED_STATE_UNSPECIFIED", "MANAGED", "UNMANAGED"
    ]
    assetTags: typing.List[str]
    healthScore: typing_extensions.Literal[
        "HEALTH_SCORE_UNSPECIFIED", "VERY_POOR", "POOR", "NEUTRAL", "GOOD", "VERY_GOOD"
    ]
    createTime: str
    name: str
    lastUpdateTime: str
    keyValuePairs: typing.Dict[str, typing.Any]
    customId: str
    scoreReason: str

class GoogleAppsCloudidentityDevicesV1WipeDeviceResponse(
    typing_extensions.TypedDict, total=False
):
    device: GoogleAppsCloudidentityDevicesV1Device

class ModifyMembershipRolesResponse(typing_extensions.TypedDict, total=False):
    membership: Membership

class GoogleAppsCloudidentityDevicesV1AndroidAttributes(
    typing_extensions.TypedDict, total=False
):
    supportsWorkProfile: bool
    enabledUnknownSources: bool
    ownerProfileAccount: bool
    ownershipPrivilege: typing_extensions.Literal[
        "OWNERSHIP_PRIVILEGE_UNSPECIFIED",
        "DEVICE_ADMINISTRATOR",
        "PROFILE_OWNER",
        "DEVICE_OWNER",
    ]

class GroupRelation(typing_extensions.TypedDict, total=False):
    group: str
    labels: typing.Dict[str, typing.Any]
    relationType: typing_extensions.Literal[
        "RELATION_TYPE_UNSPECIFIED", "DIRECT", "INDIRECT", "DIRECT_AND_INDIRECT"
    ]
    displayName: str
    roles: typing.List[TransitiveMembershipRole]
    groupKey: EntityKey

class GoogleAppsCloudidentityDevicesV1DeviceUser(
    typing_extensions.TypedDict, total=False
):
    name: str
    languageCode: str
    userEmail: str
    passwordState: typing_extensions.Literal[
        "PASSWORD_STATE_UNSPECIFIED", "PASSWORD_SET", "PASSWORD_NOT_SET"
    ]
    compromisedState: typing_extensions.Literal[
        "COMPROMISED_STATE_UNSPECIFIED", "COMPROMISED", "NOT_COMPROMISED"
    ]
    userAgent: str
    lastSyncTime: str
    createTime: str
    firstSyncTime: str
    managementState: typing_extensions.Literal[
        "MANAGEMENT_STATE_UNSPECIFIED",
        "WIPING",
        "WIPED",
        "APPROVED",
        "BLOCKED",
        "PENDING_APPROVAL",
        "UNENROLLED",
    ]

class AndroidAttributes(typing_extensions.TypedDict, total=False):
    ownershipPrivilege: typing_extensions.Literal[
        "OWNERSHIP_PRIVILEGE_UNSPECIFIED",
        "DEVICE_ADMINISTRATOR",
        "PROFILE_OWNER",
        "DEVICE_OWNER",
    ]
    ownerProfileAccount: bool
    enabledUnknownSources: bool
    supportsWorkProfile: bool

class CreateDeviceRequest(typing_extensions.TypedDict, total=False):
    device: Device
    customer: str

class ApproveDeviceUserRequest(typing_extensions.TypedDict, total=False):
    customer: str

class GoogleAppsCloudidentityDevicesV1BlockDeviceUserResponse(
    typing_extensions.TypedDict, total=False
):
    deviceUser: GoogleAppsCloudidentityDevicesV1DeviceUser

class WipeDeviceUserRequest(typing_extensions.TypedDict, total=False):
    customer: str

class WipeDeviceRequest(typing_extensions.TypedDict, total=False):
    customer: str

class ListClientStatesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    clientStates: typing.List[ClientState]

class MemberRelation(typing_extensions.TypedDict, total=False):
    relationType: typing_extensions.Literal[
        "RELATION_TYPE_UNSPECIFIED", "DIRECT", "INDIRECT", "DIRECT_AND_INDIRECT"
    ]
    preferredMemberKey: typing.List[EntityKey]
    roles: typing.List[TransitiveMembershipRole]
    member: str

class SearchGroupsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    groups: typing.List[Group]

class ListGroupsResponse(typing_extensions.TypedDict, total=False):
    groups: typing.List[Group]
    nextPageToken: str

class ListDeviceUsersResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    deviceUsers: typing.List[DeviceUser]

class ApproveDeviceUserResponse(typing_extensions.TypedDict, total=False):
    deviceUser: DeviceUser

class CancelWipeDeviceResponse(typing_extensions.TypedDict, total=False):
    device: Device

class CheckTransitiveMembershipResponse(typing_extensions.TypedDict, total=False):
    hasMembership: bool

class DynamicGroupStatus(typing_extensions.TypedDict, total=False):
    status: typing_extensions.Literal[
        "STATUS_UNSPECIFIED", "UP_TO_DATE", "UPDATING_MEMBERSHIPS"
    ]
    statusTime: str

class Device(typing_extensions.TypedDict, total=False):
    enabledUsbDebugging: bool
    meid: str
    assetTag: str
    model: str
    createTime: str
    imei: str
    brand: str
    manufacturer: str
    networkOperator: str
    bootloaderVersion: str
    name: str
    basebandVersion: str
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
    buildNumber: str
    lastSyncTime: str
    serialNumber: str
    compromisedState: typing_extensions.Literal[
        "COMPROMISED_STATE_UNSPECIFIED", "COMPROMISED", "UNCOMPROMISED"
    ]
    managementState: typing_extensions.Literal[
        "MANAGEMENT_STATE_UNSPECIFIED",
        "APPROVED",
        "BLOCKED",
        "PENDING",
        "UNPROVISIONED",
        "WIPING",
        "WIPED",
    ]
    securityPatchTime: str
    kernelVersion: str
    androidSpecificAttributes: AndroidAttributes
    ownerType: typing_extensions.Literal[
        "DEVICE_OWNERSHIP_UNSPECIFIED", "COMPANY", "BYOD"
    ]
    releaseVersion: str
    osVersion: str
    encryptionState: typing_extensions.Literal[
        "ENCRYPTION_STATE_UNSPECIFIED",
        "UNSUPPORTED_BY_DEVICE",
        "ENCRYPTED",
        "NOT_ENCRYPTED",
    ]
    enabledDeveloperOptions: bool
    otherAccounts: typing.List[str]
    wifiMacAddresses: typing.List[str]

class CancelWipeDeviceUserResponse(typing_extensions.TypedDict, total=False):
    deviceUser: DeviceUser

class CustomAttributeValue(typing_extensions.TypedDict, total=False):
    numberValue: float
    stringValue: str
    boolValue: bool

class SearchTransitiveMembershipsResponse(typing_extensions.TypedDict, total=False):
    memberships: typing.List[MemberRelation]
    nextPageToken: str

class LookupMembershipNameResponse(typing_extensions.TypedDict, total=False):
    name: str

class GoogleAppsCloudidentityDevicesV1CancelWipeDeviceResponse(
    typing_extensions.TypedDict, total=False
):
    device: GoogleAppsCloudidentityDevicesV1Device

class CancelWipeDeviceRequest(typing_extensions.TypedDict, total=False):
    customer: str

class ListMembershipsResponse(typing_extensions.TypedDict, total=False):
    memberships: typing.List[Membership]
    nextPageToken: str

class ClientState(typing_extensions.TypedDict, total=False):
    name: str
    etag: str
    assetTags: typing.List[str]
    keyValuePairs: typing.Dict[str, typing.Any]
    ownerType: typing_extensions.Literal[
        "OWNER_TYPE_UNSPECIFIED", "OWNER_TYPE_CUSTOMER", "OWNER_TYPE_PARTNER"
    ]
    lastUpdateTime: str
    scoreReason: str
    customId: str
    healthScore: typing_extensions.Literal[
        "HEALTH_SCORE_UNSPECIFIED", "VERY_POOR", "POOR", "NEUTRAL", "GOOD", "VERY_GOOD"
    ]
    createTime: str
    complianceState: typing_extensions.Literal[
        "COMPLIANCE_STATE_UNSPECIFIED", "COMPLIANT", "NON_COMPLIANT"
    ]
    managed: typing_extensions.Literal[
        "MANAGED_STATE_UNSPECIFIED", "MANAGED", "UNMANAGED"
    ]

class GoogleAppsCloudidentityDevicesV1CancelWipeDeviceUserResponse(
    typing_extensions.TypedDict, total=False
):
    deviceUser: GoogleAppsCloudidentityDevicesV1DeviceUser

class LookupSelfDeviceUsersResponse(typing_extensions.TypedDict, total=False):
    names: typing.List[str]
    customer: str
    nextPageToken: str

class MembershipRole(typing_extensions.TypedDict, total=False):
    expiryDetail: ExpiryDetail
    name: str

class ExpiryDetail(typing_extensions.TypedDict, total=False):
    expireTime: str

class GoogleAppsCloudidentityDevicesV1ApproveDeviceUserResponse(
    typing_extensions.TypedDict, total=False
):
    deviceUser: GoogleAppsCloudidentityDevicesV1DeviceUser

class GoogleAppsCloudidentityDevicesV1WipeDeviceUserResponse(
    typing_extensions.TypedDict, total=False
):
    deviceUser: GoogleAppsCloudidentityDevicesV1DeviceUser

class ListDevicesResponse(typing_extensions.TypedDict, total=False):
    devices: typing.List[Device]
    nextPageToken: str

class MembershipAdjacencyList(typing_extensions.TypedDict, total=False):
    group: str
    edges: typing.List[Membership]

class BlockDeviceUserResponse(typing_extensions.TypedDict, total=False):
    deviceUser: DeviceUser

class GoogleAppsCloudidentityDevicesV1CustomAttributeValue(
    typing_extensions.TypedDict, total=False
):
    stringValue: str
    numberValue: float
    boolValue: bool

class DeviceUser(typing_extensions.TypedDict, total=False):
    passwordState: typing_extensions.Literal[
        "PASSWORD_STATE_UNSPECIFIED", "PASSWORD_SET", "PASSWORD_NOT_SET"
    ]
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
    createTime: str
    name: str
    compromisedState: typing_extensions.Literal[
        "COMPROMISED_STATE_UNSPECIFIED", "COMPROMISED", "NOT_COMPROMISED"
    ]
    languageCode: str
    firstSyncTime: str
    userEmail: str
    userAgent: str

class CancelWipeDeviceUserRequest(typing_extensions.TypedDict, total=False):
    customer: str

class DynamicGroupQuery(typing_extensions.TypedDict, total=False):
    query: str
    resourceType: typing_extensions.Literal["RESOURCE_TYPE_UNSPECIFIED", "USER"]

class Membership(typing_extensions.TypedDict, total=False):
    name: str
    type: typing_extensions.Literal[
        "TYPE_UNSPECIFIED", "USER", "SERVICE_ACCOUNT", "GROUP", "OTHER"
    ]
    createTime: str
    updateTime: str
    memberKey: EntityKey
    roles: typing.List[MembershipRole]
    preferredMemberKey: EntityKey

class DynamicGroupMetadata(typing_extensions.TypedDict, total=False):
    queries: typing.List[DynamicGroupQuery]
    status: DynamicGroupStatus

class SearchTransitiveGroupsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    memberships: typing.List[GroupRelation]

class GoogleAppsCloudidentityDevicesV1Device(typing_extensions.TypedDict, total=False):
    assetTag: str
    compromisedState: typing_extensions.Literal[
        "COMPROMISED_STATE_UNSPECIFIED", "COMPROMISED", "UNCOMPROMISED"
    ]
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
    lastSyncTime: str
    createTime: str
    kernelVersion: str
    basebandVersion: str
    wifiMacAddresses: typing.List[str]
    securityPatchTime: str
    managementState: typing_extensions.Literal[
        "MANAGEMENT_STATE_UNSPECIFIED",
        "APPROVED",
        "BLOCKED",
        "PENDING",
        "UNPROVISIONED",
        "WIPING",
        "WIPED",
    ]
    brand: str
    ownerType: typing_extensions.Literal[
        "DEVICE_OWNERSHIP_UNSPECIFIED", "COMPANY", "BYOD"
    ]
    androidSpecificAttributes: GoogleAppsCloudidentityDevicesV1AndroidAttributes
    osVersion: str
    enabledDeveloperOptions: bool
    buildNumber: str
    enabledUsbDebugging: bool
    name: str
    manufacturer: str
    model: str
    meid: str
    imei: str
    bootloaderVersion: str
    releaseVersion: str
    encryptionState: typing_extensions.Literal[
        "ENCRYPTION_STATE_UNSPECIFIED",
        "UNSUPPORTED_BY_DEVICE",
        "ENCRYPTED",
        "NOT_ENCRYPTED",
    ]
    serialNumber: str
    networkOperator: str
    otherAccounts: typing.List[str]

class ModifyMembershipRolesRequest(typing_extensions.TypedDict, total=False):
    removeRoles: typing.List[str]
    updateRolesParams: typing.List[UpdateMembershipRolesParams]
    addRoles: typing.List[MembershipRole]
