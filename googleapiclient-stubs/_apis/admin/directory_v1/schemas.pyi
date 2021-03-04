import typing

import typing_extensions
@typing.type_check_only
class Alias(typing_extensions.TypedDict, total=False):
    alias: str
    etag: str
    id: str
    kind: str
    primaryEmail: str

@typing.type_check_only
class Aliases(typing_extensions.TypedDict, total=False):
    aliases: typing.List[typing.Any]
    etag: str
    kind: str

@typing.type_check_only
class Asp(typing_extensions.TypedDict, total=False):
    codeId: int
    creationTime: str
    etag: str
    kind: str
    lastTimeUsed: str
    name: str
    userKey: str

@typing.type_check_only
class Asps(typing_extensions.TypedDict, total=False):
    etag: str
    items: typing.List[Asp]
    kind: str

@typing.type_check_only
class Building(typing_extensions.TypedDict, total=False):
    address: BuildingAddress
    buildingId: str
    buildingName: str
    coordinates: BuildingCoordinates
    description: str
    etags: str
    floorNames: typing.List[str]
    kind: str

@typing.type_check_only
class BuildingAddress(typing_extensions.TypedDict, total=False):
    addressLines: typing.List[str]
    administrativeArea: str
    languageCode: str
    locality: str
    postalCode: str
    regionCode: str
    sublocality: str

@typing.type_check_only
class BuildingCoordinates(typing_extensions.TypedDict, total=False):
    latitude: float
    longitude: float

@typing.type_check_only
class Buildings(typing_extensions.TypedDict, total=False):
    buildings: typing.List[Building]
    etag: str
    kind: str
    nextPageToken: str

@typing.type_check_only
class CalendarResource(typing_extensions.TypedDict, total=False):
    buildingId: str
    capacity: int
    etags: str
    featureInstances: typing.Any
    floorName: str
    floorSection: str
    generatedResourceName: str
    kind: str
    resourceCategory: str
    resourceDescription: str
    resourceEmail: str
    resourceId: str
    resourceName: str
    resourceType: str
    userVisibleDescription: str

@typing.type_check_only
class CalendarResources(typing_extensions.TypedDict, total=False):
    etag: str
    items: typing.List[CalendarResource]
    kind: str
    nextPageToken: str

@typing.type_check_only
class Channel(typing_extensions.TypedDict, total=False):
    address: str
    expiration: str
    id: str
    kind: str
    params: typing.Dict[str, typing.Any]
    payload: bool
    resourceId: str
    resourceUri: str
    token: str
    type: str

@typing.type_check_only
class ChromeOsDevice(typing_extensions.TypedDict, total=False):
    activeTimeRanges: typing.List[typing.Dict[str, typing.Any]]
    annotatedAssetId: str
    annotatedLocation: str
    annotatedUser: str
    autoUpdateExpiration: str
    bootMode: str
    cpuStatusReports: typing.List[typing.Dict[str, typing.Any]]
    deviceFiles: typing.List[typing.Dict[str, typing.Any]]
    deviceId: str
    diskVolumeReports: typing.List[typing.Dict[str, typing.Any]]
    dockMacAddress: str
    etag: str
    ethernetMacAddress: str
    ethernetMacAddress0: str
    firmwareVersion: str
    kind: str
    lastEnrollmentTime: str
    lastKnownNetwork: typing.List[typing.Dict[str, typing.Any]]
    lastSync: str
    macAddress: str
    manufactureDate: str
    meid: str
    model: str
    notes: str
    orderNumber: str
    orgUnitPath: str
    osVersion: str
    platformVersion: str
    recentUsers: typing.List[RecentUsers]
    serialNumber: str
    status: str
    supportEndDate: str
    systemRamFreeReports: typing.List[typing.Dict[str, typing.Any]]
    systemRamTotal: str
    tpmVersionInfo: typing.Dict[str, typing.Any]
    willAutoRenew: bool

@typing.type_check_only
class ChromeOsDeviceAction(typing_extensions.TypedDict, total=False):
    action: str
    deprovisionReason: str

@typing.type_check_only
class ChromeOsDevices(typing_extensions.TypedDict, total=False):
    chromeosdevices: typing.List[ChromeOsDevice]
    etag: str
    kind: str
    nextPageToken: str

@typing.type_check_only
class ChromeOsMoveDevicesToOu(typing_extensions.TypedDict, total=False):
    deviceIds: typing.List[str]

@typing.type_check_only
class Customer(typing_extensions.TypedDict, total=False):
    alternateEmail: str
    customerCreationTime: str
    customerDomain: str
    etag: str
    id: str
    kind: str
    language: str
    phoneNumber: str
    postalAddress: CustomerPostalAddress

@typing.type_check_only
class CustomerPostalAddress(typing_extensions.TypedDict, total=False):
    addressLine1: str
    addressLine2: str
    addressLine3: str
    contactName: str
    countryCode: str
    locality: str
    organizationName: str
    postalCode: str
    region: str

@typing.type_check_only
class DirectoryChromeosdevicesCommand(typing_extensions.TypedDict, total=False):
    commandExpireTime: str
    commandId: str
    commandResult: DirectoryChromeosdevicesCommandResult
    issueTime: str
    payload: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "PENDING",
        "EXPIRED",
        "CANCELLED",
        "SENT_TO_CLIENT",
        "ACKED_BY_CLIENT",
        "EXECUTED_BY_CLIENT",
    ]
    type: typing_extensions.Literal[
        "COMMAND_TYPE_UNSPECIFIED",
        "REBOOT",
        "TAKE_A_SCREENSHOT",
        "SET_VOLUME",
        "WIPE_USERS",
        "REMOTE_POWERWASH",
    ]

@typing.type_check_only
class DirectoryChromeosdevicesCommandResult(typing_extensions.TypedDict, total=False):
    errorMessage: str
    executeTime: str
    result: typing_extensions.Literal[
        "COMMAND_RESULT_TYPE_UNSPECIFIED", "IGNORED", "FAILURE", "SUCCESS"
    ]

@typing.type_check_only
class DirectoryChromeosdevicesIssueCommandRequest(
    typing_extensions.TypedDict, total=False
):
    commandType: typing_extensions.Literal[
        "COMMAND_TYPE_UNSPECIFIED",
        "REBOOT",
        "TAKE_A_SCREENSHOT",
        "SET_VOLUME",
        "WIPE_USERS",
        "REMOTE_POWERWASH",
    ]
    payload: str

@typing.type_check_only
class DirectoryChromeosdevicesIssueCommandResponse(
    typing_extensions.TypedDict, total=False
):
    commandId: str

@typing.type_check_only
class DomainAlias(typing_extensions.TypedDict, total=False):
    creationTime: str
    domainAliasName: str
    etag: str
    kind: str
    parentDomainName: str
    verified: bool

@typing.type_check_only
class DomainAliases(typing_extensions.TypedDict, total=False):
    domainAliases: typing.List[DomainAlias]
    etag: str
    kind: str

@typing.type_check_only
class Domains(typing_extensions.TypedDict, total=False):
    creationTime: str
    domainAliases: typing.List[DomainAlias]
    domainName: str
    etag: str
    isPrimary: bool
    kind: str
    verified: bool

@typing.type_check_only
class Domains2(typing_extensions.TypedDict, total=False):
    domains: typing.List[Domains]
    etag: str
    kind: str

@typing.type_check_only
class Feature(typing_extensions.TypedDict, total=False):
    etags: str
    kind: str
    name: str

@typing.type_check_only
class FeatureInstance(typing_extensions.TypedDict, total=False):
    feature: Feature

@typing.type_check_only
class FeatureRename(typing_extensions.TypedDict, total=False):
    newName: str

@typing.type_check_only
class Features(typing_extensions.TypedDict, total=False):
    etag: str
    features: typing.List[Feature]
    kind: str
    nextPageToken: str

@typing.type_check_only
class Group(typing_extensions.TypedDict, total=False):
    adminCreated: bool
    aliases: typing.List[str]
    description: str
    directMembersCount: str
    email: str
    etag: str
    id: str
    kind: str
    name: str
    nonEditableAliases: typing.List[str]

@typing.type_check_only
class Groups(typing_extensions.TypedDict, total=False):
    etag: str
    groups: typing.List[Group]
    kind: str
    nextPageToken: str

@typing.type_check_only
class Member(typing_extensions.TypedDict, total=False):
    delivery_settings: str
    email: str
    etag: str
    id: str
    kind: str
    role: str
    status: str
    type: str

@typing.type_check_only
class Members(typing_extensions.TypedDict, total=False):
    etag: str
    kind: str
    members: typing.List[Member]
    nextPageToken: str

@typing.type_check_only
class MembersHasMember(typing_extensions.TypedDict, total=False):
    isMember: bool

@typing.type_check_only
class MobileDevice(typing_extensions.TypedDict, total=False):
    adbStatus: bool
    applications: typing.List[typing.Dict[str, typing.Any]]
    basebandVersion: str
    bootloaderVersion: str
    brand: str
    buildNumber: str
    defaultLanguage: str
    developerOptionsStatus: bool
    deviceCompromisedStatus: str
    deviceId: str
    devicePasswordStatus: str
    email: typing.List[str]
    encryptionStatus: str
    etag: str
    firstSync: str
    hardware: str
    hardwareId: str
    imei: str
    kernelVersion: str
    kind: str
    lastSync: str
    managedAccountIsOnOwnerProfile: bool
    manufacturer: str
    meid: str
    model: str
    name: typing.List[str]
    networkOperator: str
    os: str
    otherAccountsInfo: typing.List[str]
    privilege: str
    releaseVersion: str
    resourceId: str
    securityPatchLevel: str
    serialNumber: str
    status: str
    supportsWorkProfile: bool
    type: str
    unknownSourcesStatus: bool
    userAgent: str
    wifiMacAddress: str

@typing.type_check_only
class MobileDeviceAction(typing_extensions.TypedDict, total=False):
    action: str

@typing.type_check_only
class MobileDevices(typing_extensions.TypedDict, total=False):
    etag: str
    kind: str
    mobiledevices: typing.List[MobileDevice]
    nextPageToken: str

@typing.type_check_only
class OrgUnit(typing_extensions.TypedDict, total=False):
    blockInheritance: bool
    description: str
    etag: str
    kind: str
    name: str
    orgUnitId: str
    orgUnitPath: str
    parentOrgUnitId: str
    parentOrgUnitPath: str

@typing.type_check_only
class OrgUnits(typing_extensions.TypedDict, total=False):
    etag: str
    kind: str
    organizationUnits: typing.List[OrgUnit]

@typing.type_check_only
class Privilege(typing.Dict[str, typing.Any]): ...

@typing.type_check_only
class Privileges(typing_extensions.TypedDict, total=False):
    etag: str
    items: typing.List[Privilege]
    kind: str

@typing.type_check_only
class RecentUsers(typing_extensions.TypedDict, total=False):
    email: str
    type: str

@typing.type_check_only
class Role(typing_extensions.TypedDict, total=False):
    etag: str
    isSuperAdminRole: bool
    isSystemRole: bool
    kind: str
    roleDescription: str
    roleId: str
    roleName: str
    rolePrivileges: typing.List[typing.Dict[str, typing.Any]]

@typing.type_check_only
class RoleAssignment(typing_extensions.TypedDict, total=False):
    assignedTo: str
    etag: str
    kind: str
    orgUnitId: str
    roleAssignmentId: str
    roleId: str
    scopeType: str

@typing.type_check_only
class RoleAssignments(typing_extensions.TypedDict, total=False):
    etag: str
    items: typing.List[RoleAssignment]
    kind: str
    nextPageToken: str

@typing.type_check_only
class Roles(typing_extensions.TypedDict, total=False):
    etag: str
    items: typing.List[Role]
    kind: str
    nextPageToken: str

@typing.type_check_only
class Schema(typing_extensions.TypedDict, total=False):
    displayName: str
    etag: str
    fields: typing.List[SchemaFieldSpec]
    kind: str
    schemaId: str
    schemaName: str

@typing.type_check_only
class SchemaFieldSpec(typing_extensions.TypedDict, total=False):
    displayName: str
    etag: str
    fieldId: str
    fieldName: str
    fieldType: str
    indexed: bool
    kind: str
    multiValued: bool
    numericIndexingSpec: typing.Dict[str, typing.Any]
    readAccessType: str

@typing.type_check_only
class Schemas(typing_extensions.TypedDict, total=False):
    etag: str
    kind: str
    schemas: typing.List[Schema]

@typing.type_check_only
class Token(typing_extensions.TypedDict, total=False):
    anonymous: bool
    clientId: str
    displayText: str
    etag: str
    kind: str
    nativeApp: bool
    scopes: typing.List[str]
    userKey: str

@typing.type_check_only
class Tokens(typing_extensions.TypedDict, total=False):
    etag: str
    items: typing.List[Token]
    kind: str

@typing.type_check_only
class User(typing_extensions.TypedDict, total=False):
    addresses: typing.Any
    agreedToTerms: bool
    aliases: typing.List[str]
    archived: bool
    changePasswordAtNextLogin: bool
    creationTime: str
    customSchemas: typing.Dict[str, typing.Any]
    customerId: str
    deletionTime: str
    emails: typing.Any
    etag: str
    externalIds: typing.Any
    gender: typing.Any
    hashFunction: str
    id: str
    ims: typing.Any
    includeInGlobalAddressList: bool
    ipWhitelisted: bool
    isAdmin: bool
    isDelegatedAdmin: bool
    isEnforcedIn2Sv: bool
    isEnrolledIn2Sv: bool
    isMailboxSetup: bool
    keywords: typing.Any
    kind: str
    languages: typing.Any
    lastLoginTime: str
    locations: typing.Any
    name: UserName
    nonEditableAliases: typing.List[str]
    notes: typing.Any
    orgUnitPath: str
    organizations: typing.Any
    password: str
    phones: typing.Any
    posixAccounts: typing.Any
    primaryEmail: str
    recoveryEmail: str
    recoveryPhone: str
    relations: typing.Any
    sshPublicKeys: typing.Any
    suspended: bool
    suspensionReason: str
    thumbnailPhotoEtag: str
    thumbnailPhotoUrl: str
    websites: typing.Any

@typing.type_check_only
class UserAbout(typing_extensions.TypedDict, total=False):
    contentType: str
    value: str

@typing.type_check_only
class UserAddress(typing_extensions.TypedDict, total=False):
    country: str
    countryCode: str
    customType: str
    extendedAddress: str
    formatted: str
    locality: str
    poBox: str
    postalCode: str
    primary: bool
    region: str
    sourceIsStructured: bool
    streetAddress: str
    type: str

@typing.type_check_only
class UserCustomProperties(typing.Dict[str, typing.Any]): ...

@typing.type_check_only
class UserEmail(typing_extensions.TypedDict, total=False):
    address: str
    customType: str
    primary: bool
    type: str

@typing.type_check_only
class UserExternalId(typing_extensions.TypedDict, total=False):
    customType: str
    type: str
    value: str

@typing.type_check_only
class UserGender(typing_extensions.TypedDict, total=False):
    addressMeAs: str
    customGender: str
    type: str

@typing.type_check_only
class UserIm(typing_extensions.TypedDict, total=False):
    customProtocol: str
    customType: str
    im: str
    primary: bool
    protocol: str
    type: str

@typing.type_check_only
class UserKeyword(typing_extensions.TypedDict, total=False):
    customType: str
    type: str
    value: str

@typing.type_check_only
class UserLanguage(typing_extensions.TypedDict, total=False):
    customLanguage: str
    languageCode: str

@typing.type_check_only
class UserLocation(typing_extensions.TypedDict, total=False):
    area: str
    buildingId: str
    customType: str
    deskCode: str
    floorName: str
    floorSection: str
    type: str

@typing.type_check_only
class UserMakeAdmin(typing_extensions.TypedDict, total=False):
    status: bool

@typing.type_check_only
class UserName(typing_extensions.TypedDict, total=False):
    familyName: str
    fullName: str
    givenName: str

@typing.type_check_only
class UserOrganization(typing_extensions.TypedDict, total=False):
    costCenter: str
    customType: str
    department: str
    description: str
    domain: str
    fullTimeEquivalent: int
    location: str
    name: str
    primary: bool
    symbol: str
    title: str
    type: str

@typing.type_check_only
class UserPhone(typing_extensions.TypedDict, total=False):
    customType: str
    primary: bool
    type: str
    value: str

@typing.type_check_only
class UserPhoto(typing_extensions.TypedDict, total=False):
    etag: str
    height: int
    id: str
    kind: str
    mimeType: str
    photoData: str
    primaryEmail: str
    width: int

@typing.type_check_only
class UserPosixAccount(typing_extensions.TypedDict, total=False):
    accountId: str
    gecos: str
    gid: str
    homeDirectory: str
    operatingSystemType: str
    primary: bool
    shell: str
    systemId: str
    uid: str
    username: str

@typing.type_check_only
class UserRelation(typing_extensions.TypedDict, total=False):
    customType: str
    type: str
    value: str

@typing.type_check_only
class UserSshPublicKey(typing_extensions.TypedDict, total=False):
    expirationTimeUsec: str
    fingerprint: str
    key: str

@typing.type_check_only
class UserUndelete(typing_extensions.TypedDict, total=False):
    orgUnitPath: str

@typing.type_check_only
class UserWebsite(typing_extensions.TypedDict, total=False):
    customType: str
    primary: bool
    type: str
    value: str

@typing.type_check_only
class Users(typing_extensions.TypedDict, total=False):
    etag: str
    kind: str
    nextPageToken: str
    trigger_event: str
    users: typing.List[User]

@typing.type_check_only
class VerificationCode(typing_extensions.TypedDict, total=False):
    etag: str
    kind: str
    userId: str
    verificationCode: str

@typing.type_check_only
class VerificationCodes(typing_extensions.TypedDict, total=False):
    etag: str
    items: typing.List[VerificationCode]
    kind: str
