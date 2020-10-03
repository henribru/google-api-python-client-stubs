import typing

import typing_extensions

class UserLanguage(typing_extensions.TypedDict, total=False):
    customLanguage: str
    languageCode: str

class Users(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    etag: str
    trigger_event: str
    users: typing.List[User]
    kind: str

class UserPhoto(typing_extensions.TypedDict, total=False):
    mimeType: str
    width: int
    photoData: str
    primaryEmail: str
    kind: str
    etag: str
    id: str
    height: int

class Schema(typing_extensions.TypedDict, total=False):
    schemaName: str
    schemaId: str
    kind: str
    etag: str
    fields: typing.List[SchemaFieldSpec]
    displayName: str

class UserUndelete(typing_extensions.TypedDict, total=False):
    orgUnitPath: str

class UserMakeAdmin(typing_extensions.TypedDict, total=False):
    status: bool

class FeatureInstance(typing_extensions.TypedDict, total=False):
    feature: Feature

class MobileDevices(typing_extensions.TypedDict, total=False):
    etag: str
    mobiledevices: typing.List[MobileDevice]
    nextPageToken: str
    kind: str

class VerificationCode(typing_extensions.TypedDict, total=False):
    verificationCode: str
    userId: str
    etag: str
    kind: str

class UserCustomProperties(typing.Dict[str, typing.Any]): ...

class OrgUnits(typing_extensions.TypedDict, total=False):
    organizationUnits: typing.List[OrgUnit]
    etag: str
    kind: str

class Aliases(typing_extensions.TypedDict, total=False):
    aliases: typing.List[typing.Any]
    etag: str
    kind: str

class UserLocation(typing_extensions.TypedDict, total=False):
    area: str
    floorName: str
    type: str
    deskCode: str
    customType: str
    buildingId: str
    floorSection: str

class CalendarResource(typing_extensions.TypedDict, total=False):
    floorName: str
    capacity: int
    resourceType: str
    resourceName: str
    resourceCategory: str
    buildingId: str
    resourceId: str
    floorSection: str
    featureInstances: typing.Any
    generatedResourceName: str
    etags: str
    kind: str
    resourceDescription: str
    userVisibleDescription: str
    resourceEmail: str

class ChromeOsDevices(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    etag: str
    kind: str
    chromeosdevices: typing.List[ChromeOsDevice]

class Groups(typing_extensions.TypedDict, total=False):
    groups: typing.List[Group]
    etag: str
    nextPageToken: str
    kind: str

class FeatureRename(typing_extensions.TypedDict, total=False):
    newName: str

class UserKeyword(typing_extensions.TypedDict, total=False):
    type: str
    customType: str
    value: str

class UserRelation(typing_extensions.TypedDict, total=False):
    value: str
    customType: str
    type: str

class UserWebsite(typing_extensions.TypedDict, total=False):
    primary: bool
    value: str
    type: str
    customType: str

class Member(typing_extensions.TypedDict, total=False):
    id: str
    type: str
    etag: str
    delivery_settings: str
    email: str
    status: str
    kind: str
    role: str

class MembersHasMember(typing_extensions.TypedDict, total=False):
    isMember: bool

class Roles(typing_extensions.TypedDict, total=False):
    kind: str
    items: typing.List[Role]
    nextPageToken: str
    etag: str

class Role(typing_extensions.TypedDict, total=False):
    isSuperAdminRole: bool
    kind: str
    roleId: str
    isSystemRole: bool
    rolePrivileges: typing.List[typing.Dict[str, typing.Any]]
    roleDescription: str
    etag: str
    roleName: str

class Customer(typing_extensions.TypedDict, total=False):
    customerDomain: str
    customerCreationTime: str
    etag: str
    alternateEmail: str
    postalAddress: CustomerPostalAddress
    language: str
    phoneNumber: str
    kind: str
    id: str

class CalendarResources(typing_extensions.TypedDict, total=False):
    etag: str
    items: typing.List[CalendarResource]
    nextPageToken: str
    kind: str

class User(typing_extensions.TypedDict, total=False):
    suspensionReason: str
    posixAccounts: typing.Any
    recoveryEmail: str
    isEnforcedIn2Sv: bool
    phones: typing.Any
    aliases: typing.List[str]
    thumbnailPhotoEtag: str
    relations: typing.Any
    creationTime: str
    deletionTime: str
    recoveryPhone: str
    languages: typing.Any
    kind: str
    keywords: typing.Any
    ims: typing.Any
    password: str
    isDelegatedAdmin: bool
    nonEditableAliases: typing.List[str]
    name: UserName
    archived: bool
    agreedToTerms: bool
    organizations: typing.Any
    websites: typing.Any
    ipWhitelisted: bool
    etag: str
    isAdmin: bool
    emails: typing.Any
    orgUnitPath: str
    primaryEmail: str
    gender: typing.Any
    sshPublicKeys: typing.Any
    customerId: str
    notes: typing.Any
    isEnrolledIn2Sv: bool
    lastLoginTime: str
    includeInGlobalAddressList: bool
    hashFunction: str
    thumbnailPhotoUrl: str
    isMailboxSetup: bool
    id: str
    externalIds: typing.Any
    suspended: bool
    customSchemas: typing.Dict[str, typing.Any]
    changePasswordAtNextLogin: bool
    locations: typing.Any
    addresses: typing.Any

class Group(typing_extensions.TypedDict, total=False):
    name: str
    nonEditableAliases: typing.List[str]
    kind: str
    directMembersCount: str
    id: str
    description: str
    aliases: typing.List[str]
    email: str
    adminCreated: bool
    etag: str

class UserAddress(typing_extensions.TypedDict, total=False):
    type: str
    poBox: str
    countryCode: str
    country: str
    extendedAddress: str
    customType: str
    formatted: str
    locality: str
    sourceIsStructured: bool
    primary: bool
    region: str
    streetAddress: str
    postalCode: str

class MobileDeviceAction(typing_extensions.TypedDict, total=False):
    action: str

class UserEmail(typing_extensions.TypedDict, total=False):
    customType: str
    address: str
    primary: bool
    type: str

class VerificationCodes(typing_extensions.TypedDict, total=False):
    items: typing.List[VerificationCode]
    etag: str
    kind: str

class UserPosixAccount(typing_extensions.TypedDict, total=False):
    gid: str
    systemId: str
    uid: str
    primary: bool
    gecos: str
    accountId: str
    homeDirectory: str
    shell: str
    operatingSystemType: str
    username: str

class ChromeOsDeviceAction(typing_extensions.TypedDict, total=False):
    deprovisionReason: str
    action: str

class ChromeOsDevice(typing_extensions.TypedDict, total=False):
    bootMode: str
    kind: str
    systemRamTotal: str
    ethernetMacAddress: str
    manufactureDate: str
    orgUnitPath: str
    lastEnrollmentTime: str
    platformVersion: str
    status: str
    recentUsers: typing.List[typing.Dict[str, typing.Any]]
    diskVolumeReports: typing.List[typing.Dict[str, typing.Any]]
    systemRamFreeReports: typing.List[typing.Dict[str, typing.Any]]
    annotatedAssetId: str
    supportEndDate: str
    autoUpdateExpiration: str
    serialNumber: str
    dockMacAddress: str
    cpuStatusReports: typing.List[typing.Dict[str, typing.Any]]
    etag: str
    activeTimeRanges: typing.List[typing.Dict[str, typing.Any]]
    lastSync: str
    orderNumber: str
    meid: str
    notes: str
    willAutoRenew: bool
    firmwareVersion: str
    ethernetMacAddress0: str
    model: str
    annotatedUser: str
    annotatedLocation: str
    osVersion: str
    deviceId: str
    tpmVersionInfo: typing.Dict[str, typing.Any]
    deviceFiles: typing.List[typing.Dict[str, typing.Any]]
    macAddress: str
    lastKnownNetwork: typing.List[typing.Dict[str, typing.Any]]

class UserOrganization(typing_extensions.TypedDict, total=False):
    primary: bool
    location: str
    costCenter: str
    name: str
    domain: str
    symbol: str
    description: str
    department: str
    type: str
    customType: str
    fullTimeEquivalent: int
    title: str

class ChromeOsMoveDevicesToOu(typing_extensions.TypedDict, total=False):
    deviceIds: typing.List[str]

class Asp(typing_extensions.TypedDict, total=False):
    codeId: int
    lastTimeUsed: str
    creationTime: str
    userKey: str
    etag: str
    kind: str
    name: str

class BuildingCoordinates(typing_extensions.TypedDict, total=False):
    latitude: float
    longitude: float

class SchemaFieldSpec(typing_extensions.TypedDict, total=False):
    displayName: str
    readAccessType: str
    fieldName: str
    numericIndexingSpec: typing.Dict[str, typing.Any]
    fieldType: str
    kind: str
    etag: str
    indexed: bool
    fieldId: str
    multiValued: bool

class UserIm(typing_extensions.TypedDict, total=False):
    type: str
    im: str
    customType: str
    primary: bool
    customProtocol: str
    protocol: str

class UserExternalId(typing_extensions.TypedDict, total=False):
    customType: str
    value: str
    type: str

class Asps(typing_extensions.TypedDict, total=False):
    etag: str
    items: typing.List[Asp]
    kind: str

class UserAbout(typing_extensions.TypedDict, total=False):
    contentType: str
    value: str

class OrgUnit(typing_extensions.TypedDict, total=False):
    name: str
    parentOrgUnitId: str
    orgUnitId: str
    kind: str
    parentOrgUnitPath: str
    blockInheritance: bool
    description: str
    orgUnitPath: str
    etag: str

class CustomerPostalAddress(typing_extensions.TypedDict, total=False):
    countryCode: str
    addressLine3: str
    contactName: str
    postalCode: str
    locality: str
    organizationName: str
    addressLine2: str
    region: str
    addressLine1: str

class MobileDevice(typing_extensions.TypedDict, total=False):
    brand: str
    unknownSourcesStatus: bool
    manufacturer: str
    resourceId: str
    imei: str
    meid: str
    type: str
    email: typing.List[str]
    userAgent: str
    devicePasswordStatus: str
    applications: typing.List[typing.Dict[str, typing.Any]]
    deviceId: str
    supportsWorkProfile: bool
    etag: str
    serialNumber: str
    kernelVersion: str
    securityPatchLevel: str
    adbStatus: bool
    name: typing.List[str]
    otherAccountsInfo: typing.List[str]
    defaultLanguage: str
    bootloaderVersion: str
    privilege: str
    hardware: str
    basebandVersion: str
    networkOperator: str
    encryptionStatus: str
    deviceCompromisedStatus: str
    os: str
    firstSync: str
    hardwareId: str
    status: str
    releaseVersion: str
    developerOptionsStatus: bool
    wifiMacAddress: str
    buildNumber: str
    model: str
    kind: str
    lastSync: str
    managedAccountIsOnOwnerProfile: bool

class Channel(typing_extensions.TypedDict, total=False):
    expiration: str
    payload: bool
    address: str
    resourceId: str
    token: str
    kind: str
    params: typing.Dict[str, typing.Any]
    id: str
    resourceUri: str
    type: str

class Features(typing_extensions.TypedDict, total=False):
    features: typing.List[Feature]
    nextPageToken: str
    etag: str
    kind: str

class DomainAlias(typing_extensions.TypedDict, total=False):
    parentDomainName: str
    creationTime: str
    etag: str
    kind: str
    domainAliasName: str
    verified: bool

class RoleAssignments(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    kind: str
    items: typing.List[RoleAssignment]
    etag: str

class UserGender(typing_extensions.TypedDict, total=False):
    addressMeAs: str
    customGender: str
    type: str

class Feature(typing_extensions.TypedDict, total=False):
    etags: str
    kind: str
    name: str

class Schemas(typing_extensions.TypedDict, total=False):
    kind: str
    etag: str
    schemas: typing.List[Schema]

class Buildings(typing_extensions.TypedDict, total=False):
    buildings: typing.List[Building]
    etag: str
    kind: str
    nextPageToken: str

class BuildingAddress(typing_extensions.TypedDict, total=False):
    languageCode: str
    administrativeArea: str
    addressLines: typing.List[str]
    postalCode: str
    locality: str
    sublocality: str
    regionCode: str

class DomainAliases(typing_extensions.TypedDict, total=False):
    kind: str
    etag: str
    domainAliases: typing.List[DomainAlias]

class UserName(typing_extensions.TypedDict, total=False):
    fullName: str
    familyName: str
    givenName: str

class Privilege(typing.Dict[str, typing.Any]): ...

class UserPhone(typing_extensions.TypedDict, total=False):
    customType: str
    primary: bool
    value: str
    type: str

class RoleAssignment(typing_extensions.TypedDict, total=False):
    scopeType: str
    orgUnitId: str
    etag: str
    kind: str
    roleId: str
    roleAssignmentId: str
    assignedTo: str

class Alias(typing_extensions.TypedDict, total=False):
    etag: str
    primaryEmail: str
    kind: str
    alias: str
    id: str

class Tokens(typing_extensions.TypedDict, total=False):
    items: typing.List[Token]
    etag: str
    kind: str

class Privileges(typing_extensions.TypedDict, total=False):
    kind: str
    etag: str
    items: typing.List[Privilege]

class Members(typing_extensions.TypedDict, total=False):
    kind: str
    etag: str
    members: typing.List[Member]
    nextPageToken: str

class Domains(typing_extensions.TypedDict, total=False):
    isPrimary: bool
    domainAliases: typing.List[DomainAlias]
    creationTime: str
    verified: bool
    domainName: str
    etag: str
    kind: str

class Token(typing_extensions.TypedDict, total=False):
    userKey: str
    etag: str
    nativeApp: bool
    anonymous: bool
    kind: str
    clientId: str
    scopes: typing.List[str]
    displayText: str

class Building(typing_extensions.TypedDict, total=False):
    kind: str
    address: BuildingAddress
    buildingName: str
    coordinates: BuildingCoordinates
    floorNames: typing.List[str]
    buildingId: str
    description: str
    etags: str

class Domains2(typing_extensions.TypedDict, total=False):
    etag: str
    kind: str
    domains: typing.List[Domains]

class UserSshPublicKey(typing_extensions.TypedDict, total=False):
    expirationTimeUsec: str
    fingerprint: str
    key: str
