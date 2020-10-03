import typing

import typing_extensions

class GoogleAppsCloudidentityDevicesV1CustomAttributeValue(
    typing_extensions.TypedDict, total=False
):
    numberValue: float
    stringValue: str
    boolValue: bool

class GoogleAppsCloudidentityDevicesV1WipeDeviceUserRequest(
    typing_extensions.TypedDict, total=False
):
    customer: str

class GoogleAppsCloudidentityDevicesV1LookupSelfDeviceUsersResponse(
    typing_extensions.TypedDict, total=False
):
    customer: str
    nextPageToken: str
    names: typing.List[str]

class GoogleAppsCloudidentityDevicesV1BlockDeviceUserResponse(
    typing_extensions.TypedDict, total=False
):
    deviceUser: GoogleAppsCloudidentityDevicesV1DeviceUser

class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: typing.List[typing.Dict[str, typing.Any]]
    message: str

class GoogleAppsCloudidentityDevicesV1ListDevicesResponse(
    typing_extensions.TypedDict, total=False
):
    devices: typing.List[GoogleAppsCloudidentityDevicesV1Device]
    nextPageToken: str

class SearchGroupsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    groups: typing.List[Group]

class MembershipRole(typing_extensions.TypedDict, total=False):
    name: str

class GoogleAppsCloudidentityDevicesV1CancelWipeDeviceResponse(
    typing_extensions.TypedDict, total=False
):
    device: GoogleAppsCloudidentityDevicesV1Device

class LookupMembershipNameResponse(typing_extensions.TypedDict, total=False):
    name: str

class ListGroupsResponse(typing_extensions.TypedDict, total=False):
    groups: typing.List[Group]
    nextPageToken: str

class GoogleAppsCloudidentityDevicesV1WipeDeviceUserResponse(
    typing_extensions.TypedDict, total=False
):
    deviceUser: GoogleAppsCloudidentityDevicesV1DeviceUser

class GoogleAppsCloudidentityDevicesV1AndroidAttributes(
    typing_extensions.TypedDict, total=False
):
    ownershipPrivilege: typing_extensions.Literal[
        "OWNERSHIP_PRIVILEGE_UNSPECIFIED",
        "DEVICE_ADMINISTRATOR",
        "PROFILE_OWNER",
        "DEVICE_OWNER",
    ]
    supportsWorkProfile: bool
    ownerProfileAccount: bool
    enabledUnknownSources: bool

class GoogleAppsCloudidentityDevicesV1ClientState(
    typing_extensions.TypedDict, total=False
):
    healthScore: typing_extensions.Literal[
        "HEALTH_SCORE_UNSPECIFIED", "VERY_POOR", "POOR", "NEUTRAL", "GOOD", "VERY_GOOD"
    ]
    customId: str
    createTime: str
    keyValuePairs: typing.Dict[str, typing.Any]
    assetTags: typing.List[str]
    etag: str
    name: str
    lastUpdateTime: str
    ownerType: typing_extensions.Literal[
        "OWNER_TYPE_UNSPECIFIED", "OWNER_TYPE_CUSTOMER", "OWNER_TYPE_PARTNER"
    ]
    scoreReason: str
    managed: typing_extensions.Literal[
        "MANAGED_STATE_UNSPECIFIED", "MANAGED", "UNMANAGED"
    ]
    complianceState: typing_extensions.Literal[
        "COMPLIANCE_STATE_UNSPECIFIED", "COMPLIANT", "NON_COMPLIANT"
    ]

class GoogleAppsCloudidentityDevicesV1BlockDeviceUserRequest(
    typing_extensions.TypedDict, total=False
):
    customer: str

class GoogleAppsCloudidentityDevicesV1ListDeviceUsersResponse(
    typing_extensions.TypedDict, total=False
):
    deviceUsers: typing.List[GoogleAppsCloudidentityDevicesV1DeviceUser]
    nextPageToken: str

class ListMembershipsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    memberships: typing.List[Membership]

class EntityKey(typing_extensions.TypedDict, total=False):
    namespace: str
    id: str

class GoogleAppsCloudidentityDevicesV1ApproveDeviceUserResponse(
    typing_extensions.TypedDict, total=False
):
    deviceUser: GoogleAppsCloudidentityDevicesV1DeviceUser

class Operation(typing_extensions.TypedDict, total=False):
    response: typing.Dict[str, typing.Any]
    done: bool
    error: Status
    metadata: typing.Dict[str, typing.Any]
    name: str

class GoogleAppsCloudidentityDevicesV1CancelWipeDeviceUserResponse(
    typing_extensions.TypedDict, total=False
):
    deviceUser: GoogleAppsCloudidentityDevicesV1DeviceUser

class GoogleAppsCloudidentityDevicesV1ApproveDeviceUserRequest(
    typing_extensions.TypedDict, total=False
):
    customer: str

class Group(typing_extensions.TypedDict, total=False):
    displayName: str
    groupKey: EntityKey
    name: str
    description: str
    updateTime: str
    labels: typing.Dict[str, typing.Any]
    createTime: str
    parent: str

class ModifyMembershipRolesRequest(typing_extensions.TypedDict, total=False):
    removeRoles: typing.List[str]
    addRoles: typing.List[MembershipRole]

class Membership(typing_extensions.TypedDict, total=False):
    name: str
    preferredMemberKey: EntityKey
    updateTime: str
    createTime: str
    type: typing_extensions.Literal[
        "TYPE_UNSPECIFIED", "USER", "SERVICE_ACCOUNT", "GROUP", "OTHER"
    ]
    roles: typing.List[MembershipRole]

class GoogleAppsCloudidentityDevicesV1WipeDeviceRequest(
    typing_extensions.TypedDict, total=False
):
    customer: str

class GoogleAppsCloudidentityDevicesV1Device(typing_extensions.TypedDict, total=False):
    brand: str
    enabledUsbDebugging: bool
    serialNumber: str
    compromisedState: typing_extensions.Literal[
        "COMPROMISED_STATE_UNSPECIFIED", "COMPROMISED", "UNCOMPROMISED"
    ]
    securityPatchTime: str
    networkOperator: str
    wifiMacAddresses: typing.List[str]
    encryptionState: typing_extensions.Literal[
        "ENCRYPTION_STATE_UNSPECIFIED",
        "UNSUPPORTED_BY_DEVICE",
        "ENCRYPTED",
        "NOT_ENCRYPTED",
    ]
    otherAccounts: typing.List[str]
    ownerType: typing_extensions.Literal[
        "DEVICE_OWNERSHIP_UNSPECIFIED", "COMPANY", "BYOD"
    ]
    createTime: str
    meid: str
    releaseVersion: str
    androidSpecificAttributes: GoogleAppsCloudidentityDevicesV1AndroidAttributes
    bootloaderVersion: str
    lastSyncTime: str
    imei: str
    kernelVersion: str
    manufacturer: str
    managementState: typing_extensions.Literal[
        "MANAGEMENT_STATE_UNSPECIFIED",
        "APPROVED",
        "BLOCKED",
        "PENDING",
        "UNPROVISIONED",
        "WIPING",
        "WIPED",
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
    model: str
    enabledDeveloperOptions: bool
    osVersion: str
    basebandVersion: str
    buildNumber: str
    assetTag: str
    name: str

class GoogleAppsCloudidentityDevicesV1CancelWipeDeviceUserRequest(
    typing_extensions.TypedDict, total=False
):
    customer: str

class GoogleAppsCloudidentityDevicesV1ListClientStatesResponse(
    typing_extensions.TypedDict, total=False
):
    clientStates: typing.List[GoogleAppsCloudidentityDevicesV1ClientState]
    nextPageToken: str

class LookupGroupNameResponse(typing_extensions.TypedDict, total=False):
    name: str

class GoogleAppsCloudidentityDevicesV1WipeDeviceResponse(
    typing_extensions.TypedDict, total=False
):
    device: GoogleAppsCloudidentityDevicesV1Device

class GoogleAppsCloudidentityDevicesV1DeviceUser(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    firstSyncTime: str
    userEmail: str
    languageCode: str
    name: str
    userAgent: str
    lastSyncTime: str
    compromisedState: typing_extensions.Literal[
        "COMPROMISED_STATE_UNSPECIFIED", "COMPROMISED", "NOT_COMPROMISED"
    ]
    managementState: typing_extensions.Literal[
        "MANAGEMENT_STATE_UNSPECIFIED",
        "WIPING",
        "WIPED",
        "APPROVED",
        "BLOCKED",
        "PENDING_APPROVAL",
        "UNENROLLED",
    ]
    passwordState: typing_extensions.Literal[
        "PASSWORD_STATE_UNSPECIFIED", "PASSWORD_SET", "PASSWORD_NOT_SET"
    ]

class ModifyMembershipRolesResponse(typing_extensions.TypedDict, total=False):
    membership: Membership

class GoogleAppsCloudidentityDevicesV1CancelWipeDeviceRequest(
    typing_extensions.TypedDict, total=False
):
    customer: str
