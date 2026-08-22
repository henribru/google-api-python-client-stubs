import typing

_list = list

@typing.type_check_only
class Administrator(typing.TypedDict, total=False):
    email: str

@typing.type_check_only
class AdministratorWebToken(typing.TypedDict, total=False):
    token: str

@typing.type_check_only
class AdministratorWebTokenSpec(typing.TypedDict, total=False):
    managedConfigurations: AdministratorWebTokenSpecManagedConfigurations
    parent: str
    permission: _list[typing.Literal["unknown", "approveApps", "manageMcm"]]
    playSearch: AdministratorWebTokenSpecPlaySearch
    privateApps: AdministratorWebTokenSpecPrivateApps
    storeBuilder: AdministratorWebTokenSpecStoreBuilder
    webApps: AdministratorWebTokenSpecWebApps
    zeroTouch: AdministratorWebTokenSpecZeroTouch

@typing.type_check_only
class AdministratorWebTokenSpecManagedConfigurations(typing.TypedDict, total=False):
    enabled: bool

@typing.type_check_only
class AdministratorWebTokenSpecPlaySearch(typing.TypedDict, total=False):
    approveApps: bool
    enabled: bool

@typing.type_check_only
class AdministratorWebTokenSpecPrivateApps(typing.TypedDict, total=False):
    enabled: bool

@typing.type_check_only
class AdministratorWebTokenSpecStoreBuilder(typing.TypedDict, total=False):
    enabled: bool

@typing.type_check_only
class AdministratorWebTokenSpecWebApps(typing.TypedDict, total=False):
    enabled: bool

@typing.type_check_only
class AdministratorWebTokenSpecZeroTouch(typing.TypedDict, total=False):
    enabled: bool

@typing.type_check_only
class AppRestrictionsSchema(typing.TypedDict, total=False):
    kind: str
    restrictions: _list[AppRestrictionsSchemaRestriction]

@typing.type_check_only
class AppRestrictionsSchemaChangeEvent(typing.TypedDict, total=False):
    productId: str

@typing.type_check_only
class AppRestrictionsSchemaRestriction(typing.TypedDict, total=False):
    defaultValue: AppRestrictionsSchemaRestrictionRestrictionValue
    description: str
    entry: _list[str]
    entryValue: _list[str]
    key: str
    nestedRestriction: _list[AppRestrictionsSchemaRestriction]
    restrictionType: typing.Literal[
        "bool",
        "string",
        "integer",
        "choice",
        "multiselect",
        "hidden",
        "bundle",
        "bundleArray",
    ]
    title: str

@typing.type_check_only
class AppRestrictionsSchemaRestrictionRestrictionValue(typing.TypedDict, total=False):
    type: typing.Literal[
        "bool",
        "string",
        "integer",
        "choice",
        "multiselect",
        "hidden",
        "bundle",
        "bundleArray",
    ]
    valueBool: bool
    valueInteger: int
    valueMultiselect: _list[str]
    valueString: str

@typing.type_check_only
class AppState(typing.TypedDict, total=False):
    keyedAppState: _list[KeyedAppState]
    packageName: str

@typing.type_check_only
class AppUpdateEvent(typing.TypedDict, total=False):
    productId: str

@typing.type_check_only
class AppVersion(typing.TypedDict, total=False):
    isProduction: bool
    targetSdkVersion: int
    track: typing.Literal["appTrackUnspecified", "production", "beta", "alpha"]
    trackId: _list[str]
    versionCode: int
    versionString: str

@typing.type_check_only
class ApprovalUrlInfo(typing.TypedDict, total=False):
    approvalUrl: str

@typing.type_check_only
class AuthenticationToken(typing.TypedDict, total=False):
    token: str

@typing.type_check_only
class AutoInstallConstraint(typing.TypedDict, total=False):
    chargingStateConstraint: typing.Literal[
        "chargingStateConstraintUnspecified", "chargingNotRequired", "chargingRequired"
    ]
    deviceIdleStateConstraint: typing.Literal[
        "deviceIdleStateConstraintUnspecified",
        "deviceIdleNotRequired",
        "deviceIdleRequired",
    ]
    networkTypeConstraint: typing.Literal[
        "networkTypeConstraintUnspecified", "anyNetwork", "unmeteredNetwork"
    ]

@typing.type_check_only
class AutoInstallPolicy(typing.TypedDict, total=False):
    autoInstallConstraint: _list[AutoInstallConstraint]
    autoInstallMode: typing.Literal[
        "autoInstallModeUnspecified",
        "doNotAutoInstall",
        "autoInstallOnce",
        "forceAutoInstall",
    ]
    autoInstallPriority: int
    minimumVersionCode: int

@typing.type_check_only
class ConfigurationVariables(typing.TypedDict, total=False):
    mcmId: str
    variableSet: _list[VariableSet]

@typing.type_check_only
class Device(typing.TypedDict, total=False):
    androidId: str
    device: str
    latestBuildFingerprint: str
    maker: str
    managementType: typing.Literal[
        "managedDevice", "managedProfile", "containerApp", "unmanagedProfile"
    ]
    model: str
    policy: Policy
    product: str
    report: DeviceReport
    retailBrand: str
    sdkVersion: int

@typing.type_check_only
class DeviceReport(typing.TypedDict, total=False):
    appState: _list[AppState]
    lastUpdatedTimestampMillis: str

@typing.type_check_only
class DeviceReportUpdateEvent(typing.TypedDict, total=False):
    deviceId: str
    report: DeviceReport
    userId: str

@typing.type_check_only
class DeviceState(typing.TypedDict, total=False):
    accountState: typing.Literal["enabled", "disabled"]

@typing.type_check_only
class DevicesListResponse(typing.TypedDict, total=False):
    device: _list[Device]

@typing.type_check_only
class EnrollmentToken(typing.TypedDict, total=False):
    duration: str
    enrollmentTokenType: typing.Literal[
        "enrollmentTokenTypeUnspecified", "userlessDevice", "userDevice"
    ]
    googleAuthenticationOptions: EnrollmentTokenGoogleAuthenticationOptions
    token: str

@typing.type_check_only
class EnrollmentTokenGoogleAuthenticationOptions(typing.TypedDict, total=False):
    authenticationRequirement: typing.Literal[
        "authenticationRequirementUnspecified", "optional", "required"
    ]
    requiredAccountEmail: str

@typing.type_check_only
class Enterprise(typing.TypedDict, total=False):
    administrator: _list[Administrator]
    enterpriseType: typing.Literal[
        "enterpriseTypeUnspecified",
        "managedGoogleDomain",
        "managedGooglePlayAccountsEnterprise",
    ]
    googleAuthenticationSettings: GoogleAuthenticationSettings
    id: str
    managedGoogleDomainType: typing.Literal[
        "managedGoogleDomainTypeUnspecified", "typeTeam", "typeDomain"
    ]
    name: str
    primaryDomain: str

@typing.type_check_only
class EnterpriseAccount(typing.TypedDict, total=False):
    accountEmail: str

@typing.type_check_only
class EnterpriseAuthenticationAppLinkConfig(typing.TypedDict, total=False):
    uri: str

@typing.type_check_only
class EnterpriseUpgradeEvent(typing.TypedDict, total=False):
    upgradeState: typing.Literal["upgradeStateUnspecified", "upgradeStateSucceeded"]

@typing.type_check_only
class EnterprisesListResponse(typing.TypedDict, total=False):
    enterprise: _list[Enterprise]

@typing.type_check_only
class EnterprisesSendTestPushNotificationResponse(typing.TypedDict, total=False):
    messageId: str
    topicName: str

@typing.type_check_only
class Entitlement(typing.TypedDict, total=False):
    productId: str
    reason: typing.Literal["free", "groupLicense", "userPurchase"]

@typing.type_check_only
class EntitlementsListResponse(typing.TypedDict, total=False):
    entitlement: _list[Entitlement]

@typing.type_check_only
class GenerateEnterpriseUpgradeUrlResponse(typing.TypedDict, total=False):
    url: str

@typing.type_check_only
class GoogleAuthenticationSettings(typing.TypedDict, total=False):
    googleAuthenticationRequired: typing.Literal[
        "googleAuthenticationRequiredUnspecified", "notRequired", "required"
    ]

@typing.type_check_only
class GroupLicense(typing.TypedDict, total=False):
    acquisitionKind: typing.Literal["free", "bulkPurchase"]
    approval: typing.Literal["approved", "unapproved"]
    numProvisioned: int
    numPurchased: int
    permissions: typing.Literal[
        "currentApproved", "needsReapproval", "allCurrentAndFutureApproved"
    ]
    productId: str

@typing.type_check_only
class GroupLicenseUsersListResponse(typing.TypedDict, total=False):
    user: _list[User]

@typing.type_check_only
class GroupLicensesListResponse(typing.TypedDict, total=False):
    groupLicense: _list[GroupLicense]

@typing.type_check_only
class Install(typing.TypedDict, total=False):
    installState: typing.Literal["installed", "installPending"]
    productId: str
    versionCode: int

@typing.type_check_only
class InstallFailureEvent(typing.TypedDict, total=False):
    deviceId: str
    failureDetails: str
    failureReason: typing.Literal["unknown", "timeout"]
    productId: str
    userId: str

@typing.type_check_only
class InstallsListResponse(typing.TypedDict, total=False):
    install: _list[Install]

@typing.type_check_only
class KeyedAppState(typing.TypedDict, total=False):
    data: str
    key: str
    message: str
    severity: typing.Literal["severityUnknown", "severityInfo", "severityError"]
    stateTimestampMillis: str

@typing.type_check_only
class LocalizedText(typing.TypedDict, total=False):
    locale: str
    text: str

@typing.type_check_only
class MaintenanceWindow(typing.TypedDict, total=False):
    durationMs: str
    startTimeAfterMidnightMs: str

@typing.type_check_only
class ManagedConfiguration(typing.TypedDict, total=False):
    configurationVariables: ConfigurationVariables
    kind: str
    managedProperty: _list[ManagedProperty]
    productId: str

@typing.type_check_only
class ManagedConfigurationsForDeviceListResponse(typing.TypedDict, total=False):
    managedConfigurationForDevice: _list[ManagedConfiguration]

@typing.type_check_only
class ManagedConfigurationsForUserListResponse(typing.TypedDict, total=False):
    managedConfigurationForUser: _list[ManagedConfiguration]

@typing.type_check_only
class ManagedConfigurationsSettings(typing.TypedDict, total=False):
    lastUpdatedTimestampMillis: str
    mcmId: str
    name: str

@typing.type_check_only
class ManagedConfigurationsSettingsListResponse(typing.TypedDict, total=False):
    managedConfigurationsSettings: _list[ManagedConfigurationsSettings]

@typing.type_check_only
class ManagedProperty(typing.TypedDict, total=False):
    key: str
    valueBool: bool
    valueBundle: ManagedPropertyBundle
    valueBundleArray: _list[ManagedPropertyBundle]
    valueInteger: int
    valueString: str
    valueStringArray: _list[str]

@typing.type_check_only
class ManagedPropertyBundle(typing.TypedDict, total=False):
    managedProperty: _list[ManagedProperty]

@typing.type_check_only
class NewDeviceEvent(typing.TypedDict, total=False):
    deviceId: str
    dpcPackageName: str
    managementType: typing.Literal["managedDevice", "managedProfile"]
    userId: str

@typing.type_check_only
class NewPermissionsEvent(typing.TypedDict, total=False):
    approvedPermissions: _list[str]
    productId: str
    requestedPermissions: _list[str]

@typing.type_check_only
class Notification(typing.TypedDict, total=False):
    appRestrictionsSchemaChangeEvent: AppRestrictionsSchemaChangeEvent
    appUpdateEvent: AppUpdateEvent
    deviceReportUpdateEvent: DeviceReportUpdateEvent
    enterpriseId: str
    enterpriseUpgradeEvent: EnterpriseUpgradeEvent
    installFailureEvent: InstallFailureEvent
    newDeviceEvent: NewDeviceEvent
    newPermissionsEvent: NewPermissionsEvent
    notificationType: typing.Literal[
        "unknown",
        "testNotification",
        "productApproval",
        "installFailure",
        "appUpdate",
        "newPermissions",
        "appRestricionsSchemaChange",
        "productAvailabilityChange",
        "newDevice",
        "deviceReportUpdate",
        "enterpriseUpgrade",
    ]
    productApprovalEvent: ProductApprovalEvent
    productAvailabilityChangeEvent: ProductAvailabilityChangeEvent
    timestampMillis: str

@typing.type_check_only
class NotificationSet(typing.TypedDict, total=False):
    notification: _list[Notification]
    notificationSetId: str

@typing.type_check_only
class PageInfo(typing.TypedDict, total=False):
    resultPerPage: int
    startIndex: int
    totalResults: int

@typing.type_check_only
class Permission(typing.TypedDict, total=False):
    description: str
    name: str
    permissionId: str

@typing.type_check_only
class Policy(typing.TypedDict, total=False):
    autoUpdatePolicy: typing.Literal[
        "autoUpdatePolicyUnspecified", "choiceToTheUser", "never", "wifiOnly", "always"
    ]
    deviceReportPolicy: typing.Literal[
        "deviceReportPolicyUnspecified", "deviceReportDisabled", "deviceReportEnabled"
    ]
    maintenanceWindow: MaintenanceWindow
    policyId: str
    productAvailabilityPolicy: typing.Literal[
        "productAvailabilityPolicyUnspecified", "whitelist", "all"
    ]
    productPolicy: _list[ProductPolicy]

@typing.type_check_only
class Product(typing.TypedDict, total=False):
    appRestrictionsSchema: AppRestrictionsSchema
    appTracks: _list[TrackInfo]
    appVersion: _list[AppVersion]
    authorName: str
    availableCountries: _list[str]
    availableTracks: _list[
        typing.Literal["appTrackUnspecified", "production", "beta", "alpha"]
    ]
    category: str
    contentRating: typing.Literal["ratingUnknown", "all", "preTeen", "teen", "mature"]
    description: str
    detailsUrl: str
    distributionChannel: typing.Literal[
        "publicGoogleHosted", "privateGoogleHosted", "privateSelfHosted"
    ]
    features: _list[typing.Literal["featureUnknown", "vpnApp"]]
    fullDescription: str
    iconUrl: str
    lastUpdatedTimestampMillis: str
    minAndroidSdkVersion: int
    permissions: _list[ProductPermission]
    productId: str
    productPricing: typing.Literal["unknown", "free", "freeWithInAppPurchase", "paid"]
    recentChanges: str
    requiresContainerApp: bool
    screenshotUrls: _list[str]
    signingCertificate: ProductSigningCertificate
    smallIconUrl: str
    title: str
    workDetailsUrl: str

@typing.type_check_only
class ProductApprovalEvent(typing.TypedDict, total=False):
    approved: typing.Literal["unknown", "approved", "unapproved"]
    productId: str

@typing.type_check_only
class ProductAvailabilityChangeEvent(typing.TypedDict, total=False):
    availabilityStatus: typing.Literal["unknown", "available", "removed", "unpublished"]
    productId: str

@typing.type_check_only
class ProductPermission(typing.TypedDict, total=False):
    permissionId: str
    state: typing.Literal["required", "accepted"]

@typing.type_check_only
class ProductPermissions(typing.TypedDict, total=False):
    permission: _list[ProductPermission]
    productId: str

@typing.type_check_only
class ProductPolicy(typing.TypedDict, total=False):
    autoInstallPolicy: AutoInstallPolicy
    autoUpdateMode: typing.Literal[
        "autoUpdateModeUnspecified",
        "autoUpdateDefault",
        "autoUpdatePostponed",
        "autoUpdateHighPriority",
    ]
    enterpriseAuthenticationAppLinkConfigs: _list[EnterpriseAuthenticationAppLinkConfig]
    managedConfiguration: ManagedConfiguration
    productId: str
    trackIds: _list[str]
    tracks: _list[typing.Literal["appTrackUnspecified", "production", "beta", "alpha"]]

@typing.type_check_only
class ProductSet(typing.TypedDict, total=False):
    productId: _list[str]
    productSetBehavior: typing.Literal[
        "unknown", "whitelist", "includeAll", "allApproved"
    ]
    productVisibility: _list[ProductVisibility]

@typing.type_check_only
class ProductSigningCertificate(typing.TypedDict, total=False):
    certificateHashSha1: str
    certificateHashSha256: str

@typing.type_check_only
class ProductVisibility(typing.TypedDict, total=False):
    productId: str
    trackIds: _list[str]
    tracks: _list[typing.Literal["appTrackUnspecified", "production", "beta", "alpha"]]

@typing.type_check_only
class ProductsApproveRequest(typing.TypedDict, total=False):
    approvalUrlInfo: ApprovalUrlInfo
    approvedPermissions: typing.Literal["currentPermissionsOnly", "allPermissions"]

@typing.type_check_only
class ProductsGenerateApprovalUrlResponse(typing.TypedDict, total=False):
    url: str

@typing.type_check_only
class ProductsListResponse(typing.TypedDict, total=False):
    pageInfo: PageInfo
    product: _list[Product]
    tokenPagination: TokenPagination

@typing.type_check_only
class ServiceAccount(typing.TypedDict, total=False):
    key: ServiceAccountKey
    name: str

@typing.type_check_only
class ServiceAccountKey(typing.TypedDict, total=False):
    data: str
    id: str
    publicData: str
    type: typing.Literal["googleCredentials", "pkcs12"]

@typing.type_check_only
class ServiceAccountKeysListResponse(typing.TypedDict, total=False):
    serviceAccountKey: _list[ServiceAccountKey]

@typing.type_check_only
class SignupInfo(typing.TypedDict, total=False):
    completionToken: str
    kind: str
    url: str

@typing.type_check_only
class StoreCluster(typing.TypedDict, total=False):
    id: str
    name: _list[LocalizedText]
    orderInPage: str
    productId: _list[str]

@typing.type_check_only
class StoreLayout(typing.TypedDict, total=False):
    homepageId: str
    storeLayoutType: typing.Literal["unknown", "basic", "custom"]

@typing.type_check_only
class StoreLayoutClustersListResponse(typing.TypedDict, total=False):
    cluster: _list[StoreCluster]

@typing.type_check_only
class StoreLayoutPagesListResponse(typing.TypedDict, total=False):
    page: _list[StorePage]

@typing.type_check_only
class StorePage(typing.TypedDict, total=False):
    id: str
    link: _list[str]
    name: _list[LocalizedText]

@typing.type_check_only
class TokenPagination(typing.TypedDict, total=False):
    nextPageToken: str
    previousPageToken: str

@typing.type_check_only
class TrackInfo(typing.TypedDict, total=False):
    trackAlias: str
    trackId: str

@typing.type_check_only
class User(typing.TypedDict, total=False):
    accountIdentifier: str
    accountType: typing.Literal["deviceAccount", "userAccount"]
    displayName: str
    id: str
    managementType: typing.Literal["googleManaged", "emmManaged"]
    primaryEmail: str

@typing.type_check_only
class UsersListResponse(typing.TypedDict, total=False):
    user: _list[User]

@typing.type_check_only
class VariableSet(typing.TypedDict, total=False):
    placeholder: str
    userValue: str

@typing.type_check_only
class WebApp(typing.TypedDict, total=False):
    displayMode: typing.Literal[
        "displayModeUnspecified", "minimalUi", "standalone", "fullScreen"
    ]
    icons: _list[WebAppIcon]
    isPublished: bool
    startUrl: str
    title: str
    versionCode: str
    webAppId: str

@typing.type_check_only
class WebAppIcon(typing.TypedDict, total=False):
    imageData: str

@typing.type_check_only
class WebAppsListResponse(typing.TypedDict, total=False):
    webApp: _list[WebApp]
