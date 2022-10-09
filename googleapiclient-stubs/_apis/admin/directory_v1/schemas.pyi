import typing

import typing_extensions

_list = list

@typing.type_check_only
class Alias(typing_extensions.TypedDict, total=False):
    alias: str
    etag: str
    id: str
    kind: str
    primaryEmail: str

@typing.type_check_only
class Aliases(typing_extensions.TypedDict, total=False):
    aliases: _list[typing.Any]
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
    items: _list[Asp]
    kind: str

@typing.type_check_only
class AuxiliaryMessage(typing_extensions.TypedDict, total=False):
    auxiliaryMessage: str
    fieldMask: str
    severity: typing_extensions.Literal[
        "SEVERITY_UNSPECIFIED", "SEVERITY_INFO", "SEVERITY_WARNING", "SEVERITY_ERROR"
    ]

@typing.type_check_only
class BatchCreatePrintServersRequest(typing_extensions.TypedDict, total=False):
    requests: _list[CreatePrintServerRequest]

@typing.type_check_only
class BatchCreatePrintServersResponse(typing_extensions.TypedDict, total=False):
    failures: _list[PrintServerFailureInfo]
    printServers: _list[PrintServer]

@typing.type_check_only
class BatchCreatePrintersRequest(typing_extensions.TypedDict, total=False):
    requests: _list[CreatePrinterRequest]

@typing.type_check_only
class BatchCreatePrintersResponse(typing_extensions.TypedDict, total=False):
    failures: _list[FailureInfo]
    printers: _list[Printer]

@typing.type_check_only
class BatchDeletePrintServersRequest(typing_extensions.TypedDict, total=False):
    printServerIds: _list[str]

@typing.type_check_only
class BatchDeletePrintServersResponse(typing_extensions.TypedDict, total=False):
    failedPrintServers: _list[PrintServerFailureInfo]
    printServerIds: _list[str]

@typing.type_check_only
class BatchDeletePrintersRequest(typing_extensions.TypedDict, total=False):
    printerIds: _list[str]

@typing.type_check_only
class BatchDeletePrintersResponse(typing_extensions.TypedDict, total=False):
    failedPrinters: _list[FailureInfo]
    printerIds: _list[str]

@typing.type_check_only
class Building(typing_extensions.TypedDict, total=False):
    address: BuildingAddress
    buildingId: str
    buildingName: str
    coordinates: BuildingCoordinates
    description: str
    etags: str
    floorNames: _list[str]
    kind: str

@typing.type_check_only
class BuildingAddress(typing_extensions.TypedDict, total=False):
    addressLines: _list[str]
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
    buildings: _list[Building]
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
    items: _list[CalendarResource]
    kind: str
    nextPageToken: str

@typing.type_check_only
class Channel(typing_extensions.TypedDict, total=False):
    address: str
    expiration: str
    id: str
    kind: str
    params: dict[str, typing.Any]
    payload: bool
    resourceId: str
    resourceUri: str
    token: str
    type: str

@typing.type_check_only
class ChromeOsDevice(typing_extensions.TypedDict, total=False):
    activeTimeRanges: _list[dict[str, typing.Any]]
    annotatedAssetId: str
    annotatedLocation: str
    annotatedUser: str
    autoUpdateExpiration: str
    bootMode: str
    cpuInfo: _list[dict[str, typing.Any]]
    cpuStatusReports: _list[dict[str, typing.Any]]
    deviceFiles: _list[dict[str, typing.Any]]
    deviceId: str
    diskVolumeReports: _list[dict[str, typing.Any]]
    dockMacAddress: str
    etag: str
    ethernetMacAddress: str
    ethernetMacAddress0: str
    firmwareVersion: str
    firstEnrollmentTime: str
    kind: str
    lastEnrollmentTime: str
    lastKnownNetwork: _list[dict[str, typing.Any]]
    lastSync: str
    macAddress: str
    manufactureDate: str
    meid: str
    model: str
    notes: str
    orderNumber: str
    orgUnitId: str
    orgUnitPath: str
    osUpdateStatus: OsUpdateStatus
    osVersion: str
    platformVersion: str
    recentUsers: _list[dict[str, typing.Any]]
    screenshotFiles: _list[dict[str, typing.Any]]
    serialNumber: str
    status: str
    supportEndDate: str
    systemRamFreeReports: _list[dict[str, typing.Any]]
    systemRamTotal: str
    tpmVersionInfo: dict[str, typing.Any]
    willAutoRenew: bool

@typing.type_check_only
class ChromeOsDeviceAction(typing_extensions.TypedDict, total=False):
    action: str
    deprovisionReason: str

@typing.type_check_only
class ChromeOsDevices(typing_extensions.TypedDict, total=False):
    chromeosdevices: _list[ChromeOsDevice]
    etag: str
    kind: str
    nextPageToken: str

@typing.type_check_only
class ChromeOsMoveDevicesToOu(typing_extensions.TypedDict, total=False):
    deviceIds: _list[str]

@typing.type_check_only
class CreatePrintServerRequest(typing_extensions.TypedDict, total=False):
    parent: str
    printServer: PrintServer

@typing.type_check_only
class CreatePrinterRequest(typing_extensions.TypedDict, total=False):
    parent: str
    printer: Printer

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
    domainAliases: _list[DomainAlias]
    etag: str
    kind: str

@typing.type_check_only
class Domains(typing_extensions.TypedDict, total=False):
    creationTime: str
    domainAliases: _list[DomainAlias]
    domainName: str
    etag: str
    isPrimary: bool
    kind: str
    verified: bool

@typing.type_check_only
class Domains2(typing_extensions.TypedDict, total=False):
    domains: _list[Domains]
    etag: str
    kind: str

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class FailureInfo(typing_extensions.TypedDict, total=False):
    errorCode: typing_extensions.Literal[
        "OK",
        "CANCELLED",
        "UNKNOWN",
        "INVALID_ARGUMENT",
        "DEADLINE_EXCEEDED",
        "NOT_FOUND",
        "ALREADY_EXISTS",
        "PERMISSION_DENIED",
        "UNAUTHENTICATED",
        "RESOURCE_EXHAUSTED",
        "FAILED_PRECONDITION",
        "ABORTED",
        "OUT_OF_RANGE",
        "UNIMPLEMENTED",
        "INTERNAL",
        "UNAVAILABLE",
        "DATA_LOSS",
    ]
    errorMessage: str
    printer: Printer
    printerId: str

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
    features: _list[Feature]
    kind: str
    nextPageToken: str

@typing.type_check_only
class Group(typing_extensions.TypedDict, total=False):
    adminCreated: bool
    aliases: _list[str]
    description: str
    directMembersCount: str
    email: str
    etag: str
    id: str
    kind: str
    name: str
    nonEditableAliases: _list[str]

@typing.type_check_only
class GroupAlias(typing_extensions.TypedDict, total=False):
    alias: str
    etag: str
    id: str
    kind: str
    primaryEmail: str

@typing.type_check_only
class Groups(typing_extensions.TypedDict, total=False):
    etag: str
    groups: _list[Group]
    kind: str
    nextPageToken: str

@typing.type_check_only
class ListPrintServersResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    printServers: _list[PrintServer]

@typing.type_check_only
class ListPrinterModelsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    printerModels: _list[PrinterModel]

@typing.type_check_only
class ListPrintersResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    printers: _list[Printer]

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
    members: _list[Member]
    nextPageToken: str

@typing.type_check_only
class MembersHasMember(typing_extensions.TypedDict, total=False):
    isMember: bool

@typing.type_check_only
class MobileDevice(typing_extensions.TypedDict, total=False):
    adbStatus: bool
    applications: _list[dict[str, typing.Any]]
    basebandVersion: str
    bootloaderVersion: str
    brand: str
    buildNumber: str
    defaultLanguage: str
    developerOptionsStatus: bool
    deviceCompromisedStatus: str
    deviceId: str
    devicePasswordStatus: str
    email: _list[str]
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
    name: _list[str]
    networkOperator: str
    os: str
    otherAccountsInfo: _list[str]
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
    mobiledevices: _list[MobileDevice]
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
    organizationUnits: _list[OrgUnit]

@typing.type_check_only
class OsUpdateStatus(typing_extensions.TypedDict, total=False):
    rebootTime: str
    state: typing_extensions.Literal[
        "updateStateUnspecified",
        "updateStateNotStarted",
        "updateStateDownloadInProgress",
        "updateStateNeedReboot",
    ]
    targetKioskAppVersion: str
    targetOsVersion: str
    updateCheckTime: str
    updateTime: str

@typing.type_check_only
class PrintServer(typing_extensions.TypedDict, total=False):
    createTime: str
    description: str
    displayName: str
    id: str
    name: str
    orgUnitId: str
    uri: str

@typing.type_check_only
class PrintServerFailureInfo(typing_extensions.TypedDict, total=False):
    errorCode: typing_extensions.Literal[
        "OK",
        "CANCELLED",
        "UNKNOWN",
        "INVALID_ARGUMENT",
        "DEADLINE_EXCEEDED",
        "NOT_FOUND",
        "ALREADY_EXISTS",
        "PERMISSION_DENIED",
        "UNAUTHENTICATED",
        "RESOURCE_EXHAUSTED",
        "FAILED_PRECONDITION",
        "ABORTED",
        "OUT_OF_RANGE",
        "UNIMPLEMENTED",
        "INTERNAL",
        "UNAVAILABLE",
        "DATA_LOSS",
    ]
    errorMessage: str
    printServer: PrintServer
    printServerId: str

@typing.type_check_only
class Printer(typing_extensions.TypedDict, total=False):
    auxiliaryMessages: _list[AuxiliaryMessage]
    createTime: str
    description: str
    displayName: str
    id: str
    makeAndModel: str
    name: str
    orgUnitId: str
    uri: str
    useDriverlessConfig: bool

@typing.type_check_only
class PrinterModel(typing_extensions.TypedDict, total=False):
    displayName: str
    makeAndModel: str
    manufacturer: str

@typing.type_check_only
class Privilege(dict[str, typing.Any]): ...

@typing.type_check_only
class Privileges(typing_extensions.TypedDict, total=False):
    etag: str
    items: _list[Privilege]
    kind: str

@typing.type_check_only
class Role(typing_extensions.TypedDict, total=False):
    etag: str
    isSuperAdminRole: bool
    isSystemRole: bool
    kind: str
    roleDescription: str
    roleId: str
    roleName: str
    rolePrivileges: _list[dict[str, typing.Any]]

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
    items: _list[RoleAssignment]
    kind: str
    nextPageToken: str

@typing.type_check_only
class Roles(typing_extensions.TypedDict, total=False):
    etag: str
    items: _list[Role]
    kind: str
    nextPageToken: str

@typing.type_check_only
class Schema(typing_extensions.TypedDict, total=False):
    displayName: str
    etag: str
    fields: _list[SchemaFieldSpec]
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
    numericIndexingSpec: dict[str, typing.Any]
    readAccessType: str

@typing.type_check_only
class Schemas(typing_extensions.TypedDict, total=False):
    etag: str
    kind: str
    schemas: _list[Schema]

@typing.type_check_only
class Token(typing_extensions.TypedDict, total=False):
    anonymous: bool
    clientId: str
    displayText: str
    etag: str
    kind: str
    nativeApp: bool
    scopes: _list[str]
    userKey: str

@typing.type_check_only
class Tokens(typing_extensions.TypedDict, total=False):
    etag: str
    items: _list[Token]
    kind: str

@typing.type_check_only
class User(typing_extensions.TypedDict, total=False):
    addresses: typing.Any
    agreedToTerms: bool
    aliases: _list[str]
    archived: bool
    changePasswordAtNextLogin: bool
    creationTime: str
    customSchemas: dict[str, typing.Any]
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
    nonEditableAliases: _list[str]
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
class UserAlias(typing_extensions.TypedDict, total=False):
    alias: str
    etag: str
    id: str
    kind: str
    primaryEmail: str

@typing.type_check_only
class UserCustomProperties(dict[str, typing.Any]): ...

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
    preference: str

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
    users: _list[User]

@typing.type_check_only
class VerificationCode(typing_extensions.TypedDict, total=False):
    etag: str
    kind: str
    userId: str
    verificationCode: str

@typing.type_check_only
class VerificationCodes(typing_extensions.TypedDict, total=False):
    etag: str
    items: _list[VerificationCode]
    kind: str
