import typing

import typing_extensions

class ConfigurationVariables(typing_extensions.TypedDict, total=False):
    variableSet: typing.List[VariableSet]
    mcmId: str

class ServiceAccountKeysListResponse(typing_extensions.TypedDict, total=False):
    serviceAccountKey: typing.List[ServiceAccountKey]

class AppRestrictionsSchemaRestriction(typing.Dict[str, typing.Any]): ...

class AppVersion(typing_extensions.TypedDict, total=False):
    trackId: typing.List[str]
    track: typing_extensions.Literal[
        "appTrackUnspecified", "production", "beta", "alpha"
    ]
    versionCode: int
    versionString: str
    isProduction: bool

class DeviceState(typing_extensions.TypedDict, total=False):
    accountState: typing_extensions.Literal["enabled", "disabled"]

class PageInfo(typing_extensions.TypedDict, total=False):
    resultPerPage: int
    totalResults: int
    startIndex: int

class GroupLicense(typing_extensions.TypedDict, total=False):
    acquisitionKind: typing_extensions.Literal["free", "bulkPurchase"]
    permissions: typing_extensions.Literal[
        "currentApproved", "needsReapproval", "allCurrentAndFutureApproved"
    ]
    productId: str
    numProvisioned: int
    numPurchased: int
    approval: typing_extensions.Literal["approved", "unapproved"]

class Product(typing_extensions.TypedDict, total=False):
    appTracks: typing.List[TrackInfo]
    lastUpdatedTimestampMillis: str
    recentChanges: str
    description: str
    minAndroidSdkVersion: int
    features: typing.List[str]
    availableTracks: typing.List[str]
    productPricing: typing_extensions.Literal[
        "unknown", "free", "freeWithInAppPurchase", "paid"
    ]
    distributionChannel: typing_extensions.Literal[
        "publicGoogleHosted", "privateGoogleHosted", "privateSelfHosted"
    ]
    signingCertificate: ProductSigningCertificate
    workDetailsUrl: str
    detailsUrl: str
    permissions: typing.List[ProductPermission]
    screenshotUrls: typing.List[str]
    availableCountries: typing.List[str]
    requiresContainerApp: bool
    smallIconUrl: str
    contentRating: typing_extensions.Literal[
        "ratingUnknown", "all", "preTeen", "teen", "mature"
    ]
    iconUrl: str
    appVersion: typing.List[AppVersion]
    authorName: str
    productId: str
    title: str
    category: str

class AutoInstallPolicy(typing_extensions.TypedDict, total=False):
    minimumVersionCode: int
    autoInstallPriority: int
    autoInstallMode: typing_extensions.Literal[
        "autoInstallModeUnspecified",
        "doNotAutoInstall",
        "autoInstallOnce",
        "forceAutoInstall",
    ]
    autoInstallConstraint: typing.List[AutoInstallConstraint]

class EnterpriseAccount(typing_extensions.TypedDict, total=False):
    accountEmail: str

class Policy(typing_extensions.TypedDict, total=False):
    productAvailabilityPolicy: typing_extensions.Literal[
        "productAvailabilityPolicyUnspecified", "whitelist", "all"
    ]
    productPolicy: typing.List[ProductPolicy]
    maintenanceWindow: MaintenanceWindow
    autoUpdatePolicy: typing_extensions.Literal[
        "autoUpdatePolicyUnspecified", "choiceToTheUser", "never", "wifiOnly", "always"
    ]
    deviceReportPolicy: typing_extensions.Literal[
        "deviceReportPolicyUnspecified", "deviceReportDisabled", "deviceReportEnabled"
    ]

class NewDeviceEvent(typing_extensions.TypedDict, total=False):
    dpcPackageName: str
    userId: str
    deviceId: str
    managementType: typing_extensions.Literal["managedDevice", "managedProfile"]

class ProductSet(typing_extensions.TypedDict, total=False):
    productSetBehavior: typing_extensions.Literal[
        "unknown", "whitelist", "includeAll", "allApproved"
    ]
    productVisibility: typing.List[ProductVisibility]
    productId: typing.List[str]

class ProductAvailabilityChangeEvent(typing_extensions.TypedDict, total=False):
    availabilityStatus: typing_extensions.Literal[
        "unknown", "available", "removed", "unpublished"
    ]
    productId: str

class AuthenticationToken(typing_extensions.TypedDict, total=False):
    token: str

class TrackInfo(typing_extensions.TypedDict, total=False):
    trackAlias: str
    trackId: str

class GroupLicensesListResponse(typing_extensions.TypedDict, total=False):
    groupLicense: typing.List[GroupLicense]

class ManagedConfiguration(typing_extensions.TypedDict, total=False):
    kind: str
    managedProperty: typing.List[ManagedProperty]
    configurationVariables: ConfigurationVariables
    productId: str

class ProductPolicy(typing.Dict[str, typing.Any]): ...

class ProductsApproveRequest(typing_extensions.TypedDict, total=False):
    approvalUrlInfo: ApprovalUrlInfo
    approvedPermissions: typing_extensions.Literal[
        "currentPermissionsOnly", "allPermissions"
    ]

class User(typing_extensions.TypedDict, total=False):
    displayName: str
    id: str
    accountType: typing_extensions.Literal["deviceAccount", "userAccount"]
    accountIdentifier: str
    primaryEmail: str
    managementType: typing_extensions.Literal["googleManaged", "emmManaged"]

class GroupLicenseUsersListResponse(typing_extensions.TypedDict, total=False):
    user: typing.List[User]

class StoreLayoutPagesListResponse(typing_extensions.TypedDict, total=False):
    page: typing.List[StorePage]

class ManagedConfigurationsSettingsListResponse(
    typing_extensions.TypedDict, total=False
):
    managedConfigurationsSettings: typing.List[ManagedConfigurationsSettings]

class EntitlementsListResponse(typing_extensions.TypedDict, total=False):
    entitlement: typing.List[Entitlement]

class MaintenanceWindow(typing_extensions.TypedDict, total=False):
    startTimeAfterMidnightMs: str
    durationMs: str

class WebApp(typing_extensions.TypedDict, total=False):
    webAppId: str
    icons: typing.List[WebAppIcon]
    isPublished: bool
    title: str
    displayMode: typing_extensions.Literal[
        "displayModeUnspecified", "minimalUi", "standalone", "fullScreen"
    ]
    startUrl: str
    versionCode: str

class StoreCluster(typing_extensions.TypedDict, total=False):
    name: typing.List[LocalizedText]
    orderInPage: str
    id: str
    productId: typing.List[str]

class AutoInstallConstraint(typing_extensions.TypedDict, total=False):
    chargingStateConstraint: typing_extensions.Literal[
        "chargingStateConstraintUnspecified", "chargingNotRequired", "chargingRequired"
    ]
    deviceIdleStateConstraint: typing_extensions.Literal[
        "deviceIdleStateConstraintUnspecified",
        "deviceIdleNotRequired",
        "deviceIdleRequired",
    ]
    networkTypeConstraint: typing_extensions.Literal[
        "networkTypeConstraintUnspecified", "anyNetwork", "unmeteredNetwork"
    ]

class AdministratorWebTokenSpecPrivateApps(typing_extensions.TypedDict, total=False):
    enabled: bool

class ProductPermissions(typing_extensions.TypedDict, total=False):
    permission: typing.List[ProductPermission]
    productId: str

class Enterprise(typing_extensions.TypedDict, total=False):
    administrator: typing.List[Administrator]
    name: str
    id: str
    primaryDomain: str

class UsersListResponse(typing_extensions.TypedDict, total=False):
    user: typing.List[User]

class ProductApprovalEvent(typing_extensions.TypedDict, total=False):
    productId: str
    approved: typing_extensions.Literal["unknown", "approved", "unapproved"]

class Entitlement(typing_extensions.TypedDict, total=False):
    productId: str
    reason: typing_extensions.Literal["free", "groupLicense", "userPurchase"]

class ProductsGenerateApprovalUrlResponse(typing_extensions.TypedDict, total=False):
    url: str

class ProductSigningCertificate(typing_extensions.TypedDict, total=False):
    certificateHashSha256: str
    certificateHashSha1: str

class WebAppIcon(typing_extensions.TypedDict, total=False):
    imageData: str

class ServiceAccount(typing_extensions.TypedDict, total=False):
    key: ServiceAccountKey
    name: str

class AppUpdateEvent(typing_extensions.TypedDict, total=False):
    productId: str

class AdministratorWebTokenSpec(typing_extensions.TypedDict, total=False):
    permission: typing.List[str]
    managedConfigurations: AdministratorWebTokenSpecManagedConfigurations
    webApps: AdministratorWebTokenSpecWebApps
    storeBuilder: AdministratorWebTokenSpecStoreBuilder
    parent: str
    playSearch: AdministratorWebTokenSpecPlaySearch
    privateApps: AdministratorWebTokenSpecPrivateApps

class DeviceReport(typing_extensions.TypedDict, total=False):
    lastUpdatedTimestampMillis: str
    appState: typing.List[AppState]

class AdministratorWebToken(typing_extensions.TypedDict, total=False):
    token: str

class ManagedProperty(typing.Dict[str, typing.Any]): ...

class AppRestrictionsSchemaChangeEvent(typing_extensions.TypedDict, total=False):
    productId: str

class InstallsListResponse(typing_extensions.TypedDict, total=False):
    install: typing.List[Install]

class StoreLayout(typing_extensions.TypedDict, total=False):
    storeLayoutType: typing_extensions.Literal["unknown", "basic", "custom"]
    homepageId: str

class ManagedConfigurationsSettings(typing_extensions.TypedDict, total=False):
    name: str
    lastUpdatedTimestampMillis: str
    mcmId: str

class AppRestrictionsSchemaRestrictionRestrictionValue(
    typing_extensions.TypedDict, total=False
):
    valueBool: bool
    valueMultiselect: typing.List[str]
    valueInteger: int
    valueString: str
    type: typing_extensions.Literal[
        "bool",
        "string",
        "integer",
        "choice",
        "multiselect",
        "hidden",
        "bundle",
        "bundleArray",
    ]

class LocalizedText(typing_extensions.TypedDict, total=False):
    text: str
    locale: str

class WebAppsListResponse(typing_extensions.TypedDict, total=False):
    webApp: typing.List[WebApp]

class Permission(typing_extensions.TypedDict, total=False):
    permissionId: str
    description: str
    name: str

class SignupInfo(typing_extensions.TypedDict, total=False):
    kind: str
    completionToken: str
    url: str

class AdministratorWebTokenSpecManagedConfigurations(
    typing_extensions.TypedDict, total=False
):
    enabled: bool

class TokenPagination(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    previousPageToken: str

class KeyedAppState(typing_extensions.TypedDict, total=False):
    stateTimestampMillis: str
    key: str
    severity: typing_extensions.Literal[
        "severityUnknown", "severityInfo", "severityError"
    ]
    message: str
    data: str

class AppState(typing_extensions.TypedDict, total=False):
    keyedAppState: typing.List[KeyedAppState]
    packageName: str

class NotificationSet(typing_extensions.TypedDict, total=False):
    notificationSetId: str
    notification: typing.List[Notification]

class ProductsListResponse(typing_extensions.TypedDict, total=False):
    tokenPagination: TokenPagination
    product: typing.List[Product]
    pageInfo: PageInfo

class Install(typing_extensions.TypedDict, total=False):
    productId: str
    installState: typing_extensions.Literal["installed", "installPending"]
    versionCode: int

class VariableSet(typing_extensions.TypedDict, total=False):
    userValue: str
    placeholder: str

class DevicesListResponse(typing_extensions.TypedDict, total=False):
    device: typing.List[Device]

class ServiceAccountKey(typing_extensions.TypedDict, total=False):
    id: str
    type: typing_extensions.Literal["googleCredentials", "pkcs12"]
    data: str
    publicData: str

class ManagedConfigurationsForDeviceListResponse(
    typing_extensions.TypedDict, total=False
):
    managedConfigurationForDevice: typing.List[ManagedConfiguration]

class AdministratorWebTokenSpecWebApps(typing_extensions.TypedDict, total=False):
    enabled: bool

class Device(typing.Dict[str, typing.Any]): ...

class Notification(typing_extensions.TypedDict, total=False):
    timestampMillis: str
    newPermissionsEvent: NewPermissionsEvent
    enterpriseId: str
    newDeviceEvent: NewDeviceEvent
    notificationType: typing_extensions.Literal[
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
    ]
    appUpdateEvent: AppUpdateEvent
    installFailureEvent: InstallFailureEvent
    appRestrictionsSchemaChangeEvent: AppRestrictionsSchemaChangeEvent
    deviceReportUpdateEvent: DeviceReportUpdateEvent
    productApprovalEvent: ProductApprovalEvent
    productAvailabilityChangeEvent: ProductAvailabilityChangeEvent

class ApprovalUrlInfo(typing_extensions.TypedDict, total=False):
    approvalUrl: str

class Administrator(typing_extensions.TypedDict, total=False):
    email: str

class ManagedPropertyBundle(typing.Dict[str, typing.Any]): ...

class ManagedConfigurationsForUserListResponse(
    typing_extensions.TypedDict, total=False
):
    managedConfigurationForUser: typing.List[ManagedConfiguration]

class NewPermissionsEvent(typing_extensions.TypedDict, total=False):
    requestedPermissions: typing.List[str]
    productId: str
    approvedPermissions: typing.List[str]

class StoreLayoutClustersListResponse(typing_extensions.TypedDict, total=False):
    cluster: typing.List[StoreCluster]

class InstallFailureEvent(typing_extensions.TypedDict, total=False):
    productId: str
    failureDetails: str
    failureReason: typing_extensions.Literal["unknown", "timeout"]
    userId: str
    deviceId: str

class AdministratorWebTokenSpecStoreBuilder(typing_extensions.TypedDict, total=False):
    enabled: bool

class EnterprisesListResponse(typing_extensions.TypedDict, total=False):
    enterprise: typing.List[Enterprise]

class DeviceReportUpdateEvent(typing_extensions.TypedDict, total=False):
    userId: str
    deviceId: str
    report: DeviceReport

class ProductPermission(typing_extensions.TypedDict, total=False):
    state: typing_extensions.Literal["required", "accepted"]
    permissionId: str

class ProductVisibility(typing_extensions.TypedDict, total=False):
    tracks: typing.List[str]
    trackIds: typing.List[str]
    productId: str

class AdministratorWebTokenSpecPlaySearch(typing_extensions.TypedDict, total=False):
    enabled: bool
    approveApps: bool

class AppRestrictionsSchema(typing_extensions.TypedDict, total=False):
    restrictions: typing.List[AppRestrictionsSchemaRestriction]
    kind: str

class StorePage(typing_extensions.TypedDict, total=False):
    id: str
    name: typing.List[LocalizedText]
    link: typing.List[str]

class EnterprisesSendTestPushNotificationResponse(
    typing_extensions.TypedDict, total=False
):
    topicName: str
    messageId: str
