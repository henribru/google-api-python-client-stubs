import typing

_list = list

@typing.type_check_only
class AddIdpCredentialOperationMetadata(typing.TypedDict, total=False):
    state: str

@typing.type_check_only
class AddIdpCredentialRequest(typing.TypedDict, total=False):
    pemData: str

@typing.type_check_only
class CancelUserInvitationRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class CheckTransitiveMembershipResponse(typing.TypedDict, total=False):
    hasMembership: bool

@typing.type_check_only
class CreateGroupMetadata(typing.TypedDict, total=False): ...

@typing.type_check_only
class CreateInboundOidcSsoProfileOperationMetadata(typing.TypedDict, total=False):
    state: str

@typing.type_check_only
class CreateInboundSamlSsoProfileOperationMetadata(typing.TypedDict, total=False):
    state: str

@typing.type_check_only
class CreateInboundSsoAssignmentOperationMetadata(typing.TypedDict, total=False): ...

@typing.type_check_only
class CreateMembershipMetadata(typing.TypedDict, total=False): ...

@typing.type_check_only
class DeleteGroupMetadata(typing.TypedDict, total=False): ...

@typing.type_check_only
class DeleteIdpCredentialOperationMetadata(typing.TypedDict, total=False): ...

@typing.type_check_only
class DeleteInboundOidcSsoProfileOperationMetadata(typing.TypedDict, total=False): ...

@typing.type_check_only
class DeleteInboundSamlSsoProfileOperationMetadata(typing.TypedDict, total=False): ...

@typing.type_check_only
class DeleteInboundSsoAssignmentOperationMetadata(typing.TypedDict, total=False): ...

@typing.type_check_only
class DeleteMembershipMetadata(typing.TypedDict, total=False): ...

@typing.type_check_only
class DsaPublicKeyInfo(typing.TypedDict, total=False):
    keySize: int

@typing.type_check_only
class DynamicGroupMetadata(typing.TypedDict, total=False):
    queries: _list[DynamicGroupQuery]
    status: DynamicGroupStatus

@typing.type_check_only
class DynamicGroupQuery(typing.TypedDict, total=False):
    query: str
    resourceType: typing.Literal["RESOURCE_TYPE_UNSPECIFIED", "USER"]

@typing.type_check_only
class DynamicGroupStatus(typing.TypedDict, total=False):
    status: typing.Literal[
        "STATUS_UNSPECIFIED", "UP_TO_DATE", "UPDATING_MEMBERSHIPS", "INVALID_QUERY"
    ]
    statusTime: str

@typing.type_check_only
class EntityKey(typing.TypedDict, total=False):
    id: str
    namespace: str

@typing.type_check_only
class ExpiryDetail(typing.TypedDict, total=False):
    expireTime: str

@typing.type_check_only
class GetMembershipGraphMetadata(typing.TypedDict, total=False): ...

@typing.type_check_only
class GetMembershipGraphResponse(typing.TypedDict, total=False):
    adjacencyList: _list[MembershipAdjacencyList]
    groups: _list[Group]

@typing.type_check_only
class GoogleAppsCloudidentityDevicesV1AndroidAttributes(typing.TypedDict, total=False):
    ctsProfileMatch: bool
    enabledUnknownSources: bool
    hasPotentiallyHarmfulApps: bool
    ownerProfileAccount: bool
    ownershipPrivilege: typing.Literal[
        "OWNERSHIP_PRIVILEGE_UNSPECIFIED",
        "DEVICE_ADMINISTRATOR",
        "PROFILE_OWNER",
        "DEVICE_OWNER",
    ]
    supportsWorkProfile: bool
    verifiedBoot: bool
    verifyAppsEnabled: bool

@typing.type_check_only
class GoogleAppsCloudidentityDevicesV1ApproveDeviceUserMetadata(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleAppsCloudidentityDevicesV1ApproveDeviceUserRequest(
    typing.TypedDict, total=False
):
    customer: str

@typing.type_check_only
class GoogleAppsCloudidentityDevicesV1ApproveDeviceUserResponse(
    typing.TypedDict, total=False
):
    deviceUser: GoogleAppsCloudidentityDevicesV1DeviceUser

@typing.type_check_only
class GoogleAppsCloudidentityDevicesV1BlockDeviceUserMetadata(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleAppsCloudidentityDevicesV1BlockDeviceUserRequest(
    typing.TypedDict, total=False
):
    customer: str

@typing.type_check_only
class GoogleAppsCloudidentityDevicesV1BlockDeviceUserResponse(
    typing.TypedDict, total=False
):
    deviceUser: GoogleAppsCloudidentityDevicesV1DeviceUser

@typing.type_check_only
class GoogleAppsCloudidentityDevicesV1BrowserAttributes(typing.TypedDict, total=False):
    chromeBrowserInfo: GoogleAppsCloudidentityDevicesV1BrowserInfo
    chromeProfileId: str
    lastProfileSyncTime: str

@typing.type_check_only
class GoogleAppsCloudidentityDevicesV1BrowserInfo(typing.TypedDict, total=False):
    browserManagementState: typing.Literal[
        "UNSPECIFIED",
        "UNMANAGED",
        "MANAGED_BY_OTHER_DOMAIN",
        "PROFILE_MANAGED",
        "BROWSER_MANAGED",
    ]
    browserVersion: str
    isBuiltInDnsClientEnabled: bool
    isBulkDataEntryAnalysisEnabled: bool
    isChromeCleanupEnabled: bool
    isChromeRemoteDesktopAppBlocked: bool
    isFileDownloadAnalysisEnabled: bool
    isFileUploadAnalysisEnabled: bool
    isRealtimeUrlCheckEnabled: bool
    isSecurityEventAnalysisEnabled: bool
    isSiteIsolationEnabled: bool
    isThirdPartyBlockingEnabled: bool
    passwordProtectionWarningTrigger: typing.Literal[
        "PASSWORD_PROTECTION_TRIGGER_UNSPECIFIED",
        "PROTECTION_OFF",
        "PASSWORD_REUSE",
        "PHISHING_REUSE",
    ]
    safeBrowsingProtectionLevel: typing.Literal[
        "SAFE_BROWSING_LEVEL_UNSPECIFIED", "DISABLED", "STANDARD", "ENHANCED"
    ]

@typing.type_check_only
class GoogleAppsCloudidentityDevicesV1CancelWipeDeviceMetadata(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleAppsCloudidentityDevicesV1CancelWipeDeviceRequest(
    typing.TypedDict, total=False
):
    customer: str

@typing.type_check_only
class GoogleAppsCloudidentityDevicesV1CancelWipeDeviceResponse(
    typing.TypedDict, total=False
):
    device: GoogleAppsCloudidentityDevicesV1Device

@typing.type_check_only
class GoogleAppsCloudidentityDevicesV1CancelWipeDeviceUserMetadata(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleAppsCloudidentityDevicesV1CancelWipeDeviceUserRequest(
    typing.TypedDict, total=False
):
    customer: str

@typing.type_check_only
class GoogleAppsCloudidentityDevicesV1CancelWipeDeviceUserResponse(
    typing.TypedDict, total=False
):
    deviceUser: GoogleAppsCloudidentityDevicesV1DeviceUser

@typing.type_check_only
class GoogleAppsCloudidentityDevicesV1CertificateAttributes(
    typing.TypedDict, total=False
):
    certificateTemplate: GoogleAppsCloudidentityDevicesV1CertificateTemplate
    fingerprint: str
    issuer: str
    serialNumber: str
    subject: str
    thumbprint: str
    validationState: typing.Literal[
        "CERTIFICATE_VALIDATION_STATE_UNSPECIFIED",
        "VALIDATION_SUCCESSFUL",
        "VALIDATION_FAILED",
    ]
    validityExpirationTime: str
    validityStartTime: str

@typing.type_check_only
class GoogleAppsCloudidentityDevicesV1CertificateTemplate(
    typing.TypedDict, total=False
):
    id: str
    majorVersion: int
    minorVersion: int

@typing.type_check_only
class GoogleAppsCloudidentityDevicesV1ClientState(typing.TypedDict, total=False):
    assetTags: _list[str]
    complianceState: typing.Literal[
        "COMPLIANCE_STATE_UNSPECIFIED", "COMPLIANT", "NON_COMPLIANT"
    ]
    createTime: str
    customId: str
    etag: str
    healthScore: typing.Literal[
        "HEALTH_SCORE_UNSPECIFIED", "VERY_POOR", "POOR", "NEUTRAL", "GOOD", "VERY_GOOD"
    ]
    keyValuePairs: dict[str, typing.Any]
    lastUpdateTime: str
    managed: typing.Literal["MANAGED_STATE_UNSPECIFIED", "MANAGED", "UNMANAGED"]
    name: str
    ownerType: typing.Literal[
        "OWNER_TYPE_UNSPECIFIED", "OWNER_TYPE_CUSTOMER", "OWNER_TYPE_PARTNER"
    ]
    scoreReason: str

@typing.type_check_only
class GoogleAppsCloudidentityDevicesV1CreateDeviceMetadata(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleAppsCloudidentityDevicesV1CustomAttributeValue(
    typing.TypedDict, total=False
):
    boolValue: bool
    numberValue: float
    stringValue: str

@typing.type_check_only
class GoogleAppsCloudidentityDevicesV1DeleteDeviceMetadata(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleAppsCloudidentityDevicesV1DeleteDeviceUserMetadata(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleAppsCloudidentityDevicesV1Device(typing.TypedDict, total=False):
    androidSpecificAttributes: GoogleAppsCloudidentityDevicesV1AndroidAttributes
    assetTag: str
    basebandVersion: str
    bootloaderVersion: str
    brand: str
    buildNumber: str
    compromisedState: typing.Literal[
        "COMPROMISED_STATE_UNSPECIFIED", "COMPROMISED", "UNCOMPROMISED"
    ]
    createTime: str
    deviceId: str
    deviceType: typing.Literal[
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
    encryptionState: typing.Literal[
        "ENCRYPTION_STATE_UNSPECIFIED",
        "UNSUPPORTED_BY_DEVICE",
        "ENCRYPTED",
        "NOT_ENCRYPTED",
    ]
    endpointVerificationSpecificAttributes: (
        GoogleAppsCloudidentityDevicesV1EndpointVerificationSpecificAttributes
    )
    hostname: str
    imei: str
    kernelVersion: str
    lastSyncTime: str
    managementState: typing.Literal[
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
    otherAccounts: _list[str]
    ownerType: typing.Literal["DEVICE_OWNERSHIP_UNSPECIFIED", "COMPANY", "BYOD"]
    releaseVersion: str
    securityPatchTime: str
    serialNumber: str
    unifiedDeviceId: str
    wifiMacAddresses: _list[str]

@typing.type_check_only
class GoogleAppsCloudidentityDevicesV1DeviceUser(typing.TypedDict, total=False):
    compromisedState: typing.Literal[
        "COMPROMISED_STATE_UNSPECIFIED", "COMPROMISED", "NOT_COMPROMISED"
    ]
    createTime: str
    firstSyncTime: str
    languageCode: str
    lastSyncTime: str
    managementState: typing.Literal[
        "MANAGEMENT_STATE_UNSPECIFIED",
        "WIPING",
        "WIPED",
        "APPROVED",
        "BLOCKED",
        "PENDING_APPROVAL",
        "UNENROLLED",
    ]
    name: str
    passwordState: typing.Literal[
        "PASSWORD_STATE_UNSPECIFIED", "PASSWORD_SET", "PASSWORD_NOT_SET"
    ]
    userAgent: str
    userEmail: str

@typing.type_check_only
class GoogleAppsCloudidentityDevicesV1EndpointVerificationSpecificAttributes(
    typing.TypedDict, total=False
):
    additionalSignals: dict[str, typing.Any]
    browserAttributes: _list[GoogleAppsCloudidentityDevicesV1BrowserAttributes]
    certificateAttributes: _list[GoogleAppsCloudidentityDevicesV1CertificateAttributes]

@typing.type_check_only
class GoogleAppsCloudidentityDevicesV1ListClientStatesResponse(
    typing.TypedDict, total=False
):
    clientStates: _list[GoogleAppsCloudidentityDevicesV1ClientState]
    nextPageToken: str

@typing.type_check_only
class GoogleAppsCloudidentityDevicesV1ListDeviceUsersResponse(
    typing.TypedDict, total=False
):
    deviceUsers: _list[GoogleAppsCloudidentityDevicesV1DeviceUser]
    nextPageToken: str

@typing.type_check_only
class GoogleAppsCloudidentityDevicesV1ListDevicesResponse(
    typing.TypedDict, total=False
):
    devices: _list[GoogleAppsCloudidentityDevicesV1Device]
    nextPageToken: str

@typing.type_check_only
class GoogleAppsCloudidentityDevicesV1ListEndpointAppsMetadata(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleAppsCloudidentityDevicesV1LookupSelfDeviceUsersResponse(
    typing.TypedDict, total=False
):
    customer: str
    names: _list[str]
    nextPageToken: str

@typing.type_check_only
class GoogleAppsCloudidentityDevicesV1SignoutDeviceUserMetadata(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleAppsCloudidentityDevicesV1UpdateClientStateMetadata(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleAppsCloudidentityDevicesV1UpdateDeviceMetadata(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleAppsCloudidentityDevicesV1WipeDeviceMetadata(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleAppsCloudidentityDevicesV1WipeDeviceRequest(typing.TypedDict, total=False):
    customer: str
    removeResetLock: bool

@typing.type_check_only
class GoogleAppsCloudidentityDevicesV1WipeDeviceResponse(typing.TypedDict, total=False):
    device: GoogleAppsCloudidentityDevicesV1Device

@typing.type_check_only
class GoogleAppsCloudidentityDevicesV1WipeDeviceUserMetadata(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleAppsCloudidentityDevicesV1WipeDeviceUserRequest(
    typing.TypedDict, total=False
):
    customer: str

@typing.type_check_only
class GoogleAppsCloudidentityDevicesV1WipeDeviceUserResponse(
    typing.TypedDict, total=False
):
    deviceUser: GoogleAppsCloudidentityDevicesV1DeviceUser

@typing.type_check_only
class Group(typing.TypedDict, total=False):
    additionalGroupKeys: _list[EntityKey]
    createTime: str
    description: str
    displayName: str
    dynamicGroupMetadata: DynamicGroupMetadata
    groupKey: EntityKey
    labels: dict[str, typing.Any]
    name: str
    parent: str
    updateTime: str

@typing.type_check_only
class GroupRelation(typing.TypedDict, total=False):
    displayName: str
    group: str
    groupKey: EntityKey
    labels: dict[str, typing.Any]
    relationType: typing.Literal[
        "RELATION_TYPE_UNSPECIFIED", "DIRECT", "INDIRECT", "DIRECT_AND_INDIRECT"
    ]
    roles: _list[TransitiveMembershipRole]

@typing.type_check_only
class IdpCredential(typing.TypedDict, total=False):
    dsaKeyInfo: DsaPublicKeyInfo
    name: str
    rsaKeyInfo: RsaPublicKeyInfo
    updateTime: str

@typing.type_check_only
class InboundOidcSsoProfile(typing.TypedDict, total=False):
    customer: str
    displayName: str
    idpConfig: OidcIdpConfig
    name: str
    rpConfig: OidcRpConfig

@typing.type_check_only
class InboundSamlSsoProfile(typing.TypedDict, total=False):
    customer: str
    displayName: str
    idpConfig: SamlIdpConfig
    name: str
    spConfig: SamlSpConfig

@typing.type_check_only
class InboundSsoAssignment(typing.TypedDict, total=False):
    customer: str
    name: str
    oidcSsoInfo: OidcSsoInfo
    rank: int
    samlSsoInfo: SamlSsoInfo
    signInBehavior: SignInBehavior
    ssoMode: typing.Literal[
        "SSO_MODE_UNSPECIFIED",
        "SSO_OFF",
        "SAML_SSO",
        "OIDC_SSO",
        "DOMAIN_WIDE_SAML_IF_ENABLED",
    ]
    targetGroup: str
    targetOrgUnit: str

@typing.type_check_only
class IsInvitableUserResponse(typing.TypedDict, total=False):
    isInvitableUser: bool

@typing.type_check_only
class ListGroupsResponse(typing.TypedDict, total=False):
    groups: _list[Group]
    nextPageToken: str

@typing.type_check_only
class ListIdpCredentialsResponse(typing.TypedDict, total=False):
    idpCredentials: _list[IdpCredential]
    nextPageToken: str

@typing.type_check_only
class ListInboundOidcSsoProfilesResponse(typing.TypedDict, total=False):
    inboundOidcSsoProfiles: _list[InboundOidcSsoProfile]
    nextPageToken: str

@typing.type_check_only
class ListInboundSamlSsoProfilesResponse(typing.TypedDict, total=False):
    inboundSamlSsoProfiles: _list[InboundSamlSsoProfile]
    nextPageToken: str

@typing.type_check_only
class ListInboundSsoAssignmentsResponse(typing.TypedDict, total=False):
    inboundSsoAssignments: _list[InboundSsoAssignment]
    nextPageToken: str

@typing.type_check_only
class ListMembershipsResponse(typing.TypedDict, total=False):
    memberships: _list[Membership]
    nextPageToken: str

@typing.type_check_only
class ListPoliciesResponse(typing.TypedDict, total=False):
    nextPageToken: str
    policies: _list[Policy]

@typing.type_check_only
class ListUserInvitationsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    userInvitations: _list[UserInvitation]

@typing.type_check_only
class LookupGroupNameResponse(typing.TypedDict, total=False):
    name: str

@typing.type_check_only
class LookupMembershipNameResponse(typing.TypedDict, total=False):
    name: str

@typing.type_check_only
class MemberRelation(typing.TypedDict, total=False):
    member: str
    preferredMemberKey: _list[EntityKey]
    relationType: typing.Literal[
        "RELATION_TYPE_UNSPECIFIED", "DIRECT", "INDIRECT", "DIRECT_AND_INDIRECT"
    ]
    roles: _list[TransitiveMembershipRole]

@typing.type_check_only
class MemberRestriction(typing.TypedDict, total=False):
    evaluation: RestrictionEvaluation
    query: str

@typing.type_check_only
class Membership(typing.TypedDict, total=False):
    createTime: str
    deliverySetting: typing.Literal[
        "DELIVERY_SETTING_UNSPECIFIED",
        "ALL_MAIL",
        "DIGEST",
        "DAILY",
        "NONE",
        "DISABLED",
    ]
    name: str
    preferredMemberKey: EntityKey
    roles: _list[MembershipRole]
    type: typing.Literal[
        "TYPE_UNSPECIFIED",
        "USER",
        "SERVICE_ACCOUNT",
        "GROUP",
        "SHARED_DRIVE",
        "CBCM_BROWSER",
        "CHROME_OS_DEVICE",
        "OTHER",
    ]
    updateTime: str

@typing.type_check_only
class MembershipAdjacencyList(typing.TypedDict, total=False):
    edges: _list[Membership]
    group: str

@typing.type_check_only
class MembershipRelation(typing.TypedDict, total=False):
    description: str
    displayName: str
    group: str
    groupKey: EntityKey
    labels: dict[str, typing.Any]
    membership: str
    roles: _list[MembershipRole]

@typing.type_check_only
class MembershipRole(typing.TypedDict, total=False):
    expiryDetail: ExpiryDetail
    name: str
    restrictionEvaluations: RestrictionEvaluations

@typing.type_check_only
class MembershipRoleRestrictionEvaluation(typing.TypedDict, total=False):
    state: typing.Literal[
        "STATE_UNSPECIFIED",
        "COMPLIANT",
        "FORWARD_COMPLIANT",
        "NON_COMPLIANT",
        "EVALUATING",
    ]

@typing.type_check_only
class ModifyMembershipRolesRequest(typing.TypedDict, total=False):
    addRoles: _list[MembershipRole]
    removeRoles: _list[str]
    updateRolesParams: _list[UpdateMembershipRolesParams]

@typing.type_check_only
class ModifyMembershipRolesResponse(typing.TypedDict, total=False):
    membership: Membership

@typing.type_check_only
class OidcIdpConfig(typing.TypedDict, total=False):
    changePasswordUri: str
    issuerUri: str

@typing.type_check_only
class OidcRpConfig(typing.TypedDict, total=False):
    clientId: str
    clientSecret: str
    redirectUris: _list[str]

@typing.type_check_only
class OidcSsoInfo(typing.TypedDict, total=False):
    inboundOidcSsoProfile: str

@typing.type_check_only
class Operation(typing.TypedDict, total=False):
    done: bool
    error: Status
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class Policy(typing.TypedDict, total=False):
    customer: str
    name: str
    policyQuery: PolicyQuery
    setting: Setting
    type: typing.Literal["POLICY_TYPE_UNSPECIFIED", "SYSTEM", "ADMIN"]

@typing.type_check_only
class PolicyQuery(typing.TypedDict, total=False):
    group: str
    orgUnit: str
    query: str
    sortOrder: float

@typing.type_check_only
class RestrictionEvaluation(typing.TypedDict, total=False):
    state: typing.Literal[
        "STATE_UNSPECIFIED",
        "EVALUATING",
        "COMPLIANT",
        "FORWARD_COMPLIANT",
        "NON_COMPLIANT",
    ]

@typing.type_check_only
class RestrictionEvaluations(typing.TypedDict, total=False):
    memberRestrictionEvaluation: MembershipRoleRestrictionEvaluation

@typing.type_check_only
class RsaPublicKeyInfo(typing.TypedDict, total=False):
    keySize: int

@typing.type_check_only
class SamlIdpConfig(typing.TypedDict, total=False):
    changePasswordUri: str
    entityId: str
    logoutRedirectUri: str
    singleSignOnServiceUri: str

@typing.type_check_only
class SamlSpConfig(typing.TypedDict, total=False):
    assertionConsumerServiceUri: str
    entityId: str

@typing.type_check_only
class SamlSsoInfo(typing.TypedDict, total=False):
    inboundSamlSsoProfile: str

@typing.type_check_only
class SearchDirectGroupsResponse(typing.TypedDict, total=False):
    memberships: _list[MembershipRelation]
    nextPageToken: str

@typing.type_check_only
class SearchGroupsResponse(typing.TypedDict, total=False):
    groups: _list[Group]
    nextPageToken: str

@typing.type_check_only
class SearchTransitiveGroupsResponse(typing.TypedDict, total=False):
    memberships: _list[GroupRelation]
    nextPageToken: str

@typing.type_check_only
class SearchTransitiveMembershipsResponse(typing.TypedDict, total=False):
    memberships: _list[MemberRelation]
    nextPageToken: str

@typing.type_check_only
class SecuritySettings(typing.TypedDict, total=False):
    memberRestriction: MemberRestriction
    name: str

@typing.type_check_only
class SendUserInvitationRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class Setting(typing.TypedDict, total=False):
    type: str
    value: dict[str, typing.Any]

@typing.type_check_only
class SignInBehavior(typing.TypedDict, total=False):
    redirectCondition: typing.Literal["REDIRECT_CONDITION_UNSPECIFIED", "NEVER"]

@typing.type_check_only
class Status(typing.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class TransitiveMembershipRole(typing.TypedDict, total=False):
    role: str

@typing.type_check_only
class UpdateGroupMetadata(typing.TypedDict, total=False): ...

@typing.type_check_only
class UpdateInboundOidcSsoProfileOperationMetadata(typing.TypedDict, total=False):
    state: str

@typing.type_check_only
class UpdateInboundSamlSsoProfileOperationMetadata(typing.TypedDict, total=False):
    state: str

@typing.type_check_only
class UpdateInboundSsoAssignmentOperationMetadata(typing.TypedDict, total=False): ...

@typing.type_check_only
class UpdateMembershipMetadata(typing.TypedDict, total=False): ...

@typing.type_check_only
class UpdateMembershipRolesParams(typing.TypedDict, total=False):
    fieldMask: str
    membershipRole: MembershipRole

@typing.type_check_only
class UserInvitation(typing.TypedDict, total=False):
    mailsSentCount: str
    name: str
    state: typing.Literal[
        "STATE_UNSPECIFIED", "NOT_YET_SENT", "INVITED", "ACCEPTED", "DECLINED"
    ]
    updateTime: str
