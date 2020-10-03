import typing

import typing_extensions

class ComplianceRule(typing_extensions.TypedDict, total=False):
    nonComplianceDetailCondition: NonComplianceDetailCondition
    disableApps: bool
    packageNamesToDisable: typing.List[str]
    apiLevelCondition: ApiLevelCondition

class PostureDetail(typing_extensions.TypedDict, total=False):
    advice: typing.List[UserFacingMessage]
    securityRisk: typing_extensions.Literal[
        "SECURITY_RISK_UNSPECIFIED", "UNKNOWN_OS", "COMPROMISED_OS"
    ]

class SystemUpdateInfo(typing_extensions.TypedDict, total=False):
    updateStatus: typing_extensions.Literal[
        "UPDATE_STATUS_UNKNOWN",
        "UP_TO_DATE",
        "UNKNOWN_UPDATE_AVAILABLE",
        "SECURITY_UPDATE_AVAILABLE",
        "OS_UPDATE_AVAILABLE",
    ]
    updateReceivedTime: str

class BlockAction(typing_extensions.TypedDict, total=False):
    blockAfterDays: int
    blockScope: typing_extensions.Literal[
        "BLOCK_SCOPE_UNSPECIFIED", "BLOCK_SCOPE_WORK_PROFILE", "BLOCK_SCOPE_DEVICE"
    ]

class NonComplianceDetail(typing_extensions.TypedDict, total=False):
    packageName: str
    fieldPath: str
    currentValue: typing.Any
    nonComplianceReason: typing_extensions.Literal[
        "NON_COMPLIANCE_REASON_UNSPECIFIED",
        "API_LEVEL",
        "MANAGEMENT_MODE",
        "USER_ACTION",
        "INVALID_VALUE",
        "APP_NOT_INSTALLED",
        "UNSUPPORTED",
        "APP_INSTALLED",
        "PENDING",
        "APP_INCOMPATIBLE",
        "APP_NOT_UPDATED",
    ]
    installationFailureReason: typing_extensions.Literal[
        "INSTALLATION_FAILURE_REASON_UNSPECIFIED",
        "INSTALLATION_FAILURE_REASON_UNKNOWN",
        "IN_PROGRESS",
        "NOT_FOUND",
        "NOT_COMPATIBLE_WITH_DEVICE",
        "NOT_APPROVED",
        "PERMISSIONS_NOT_ACCEPTED",
        "NOT_AVAILABLE_IN_COUNTRY",
        "NO_LICENSES_REMAINING",
        "NOT_ENROLLED",
        "USER_INVALID",
    ]
    settingName: str

class PersonalUsagePolicies(typing_extensions.TypedDict, total=False):
    personalPlayStoreMode: typing_extensions.Literal[
        "PLAY_STORE_MODE_UNSPECIFIED", "BLACKLIST"
    ]
    personalApplications: typing.List[PersonalApplicationPolicy]
    screenCaptureDisabled: bool
    cameraDisabled: bool
    accountTypesWithManagementDisabled: typing.List[str]
    maxDaysWithWorkOff: int

class SetupAction(typing_extensions.TypedDict, total=False):
    description: UserFacingMessage
    launchApp: LaunchAppAction
    title: UserFacingMessage

class ApplicationPolicy(typing_extensions.TypedDict, total=False):
    delegatedScopes: typing.List[str]
    disabled: bool
    defaultPermissionPolicy: typing_extensions.Literal[
        "PERMISSION_POLICY_UNSPECIFIED", "PROMPT", "GRANT", "DENY"
    ]
    permissionGrants: typing.List[PermissionGrant]
    lockTaskAllowed: bool
    managedConfiguration: typing.Dict[str, typing.Any]
    installType: typing_extensions.Literal[
        "INSTALL_TYPE_UNSPECIFIED",
        "PREINSTALLED",
        "FORCE_INSTALLED",
        "BLOCKED",
        "AVAILABLE",
        "REQUIRED_FOR_SETUP",
        "KIOSK",
    ]
    packageName: str
    managedConfigurationTemplate: ManagedConfigurationTemplate
    connectedWorkAndPersonalApp: typing_extensions.Literal[
        "CONNECTED_WORK_AND_PERSONAL_APP_UNSPECIFIED",
        "CONNECTED_WORK_AND_PERSONAL_APP_DISALLOWED",
        "CONNECTED_WORK_AND_PERSONAL_APP_ALLOWED",
    ]
    minimumVersionCode: int
    accessibleTrackIds: typing.List[str]

class AlwaysOnVpnPackage(typing_extensions.TypedDict, total=False):
    packageName: str
    lockdownEnabled: bool

class ApplicationReportingSettings(typing_extensions.TypedDict, total=False):
    includeRemovedApps: bool

class ManagedPropertyEntry(typing_extensions.TypedDict, total=False):
    value: str
    name: str

class PermissionGrant(typing_extensions.TypedDict, total=False):
    policy: typing_extensions.Literal[
        "PERMISSION_POLICY_UNSPECIFIED", "PROMPT", "GRANT", "DENY"
    ]
    permission: str

class Operation(typing_extensions.TypedDict, total=False):
    metadata: typing.Dict[str, typing.Any]
    response: typing.Dict[str, typing.Any]
    done: bool
    error: Status
    name: str

class ApplicationReport(typing_extensions.TypedDict, total=False):
    keyedAppStates: typing.List[KeyedAppState]
    events: typing.List[ApplicationEvent]
    packageSha256Hash: str
    packageName: str
    state: typing_extensions.Literal[
        "APPLICATION_STATE_UNSPECIFIED", "REMOVED", "INSTALLED"
    ]
    versionCode: int
    displayName: str
    signingKeyCertFingerprints: typing.List[str]
    versionName: str
    applicationSource: typing_extensions.Literal[
        "APPLICATION_SOURCE_UNSPECIFIED",
        "SYSTEM_APP_FACTORY_VERSION",
        "SYSTEM_APP_UPDATED_VERSION",
        "INSTALLED_FROM_PLAY_STORE",
    ]
    installerPackageName: str

class NonComplianceDetailCondition(typing_extensions.TypedDict, total=False):
    packageName: str
    settingName: str
    nonComplianceReason: typing_extensions.Literal[
        "NON_COMPLIANCE_REASON_UNSPECIFIED",
        "API_LEVEL",
        "MANAGEMENT_MODE",
        "USER_ACTION",
        "INVALID_VALUE",
        "APP_NOT_INSTALLED",
        "UNSUPPORTED",
        "APP_INSTALLED",
        "PENDING",
        "APP_INCOMPATIBLE",
        "APP_NOT_UPDATED",
    ]

class SoftwareInfo(typing_extensions.TypedDict, total=False):
    bootloaderVersion: str
    primaryLanguageCode: str
    androidVersion: str
    androidDevicePolicyVersionName: str
    androidBuildNumber: str
    deviceKernelVersion: str
    deviceBuildSignature: str
    systemUpdateInfo: SystemUpdateInfo
    androidDevicePolicyVersionCode: int
    androidBuildTime: str
    securityPatchLevel: str

class PackageNameList(typing_extensions.TypedDict, total=False):
    packageNames: typing.List[str]

class WebToken(typing_extensions.TypedDict, total=False):
    parentFrameUrl: str
    enabledFeatures: typing.List[str]
    value: str
    name: str
    permissions: typing.List[str]

class NetworkInfo(typing_extensions.TypedDict, total=False):
    networkOperatorName: str
    meid: str
    imei: str
    wifiMacAddress: str

class Command(typing_extensions.TypedDict, total=False):
    resetPasswordFlags: typing.List[str]
    errorCode: typing_extensions.Literal[
        "COMMAND_ERROR_CODE_UNSPECIFIED",
        "UNKNOWN",
        "API_LEVEL",
        "MANAGEMENT_MODE",
        "INVALID_VALUE",
        "UNSUPPORTED",
    ]
    newPassword: str
    duration: str
    userName: str
    createTime: str
    type: typing_extensions.Literal[
        "COMMAND_TYPE_UNSPECIFIED", "LOCK", "RESET_PASSWORD", "REBOOT"
    ]

class PersonalApplicationPolicy(typing_extensions.TypedDict, total=False):
    packageName: str
    installType: typing_extensions.Literal["INSTALL_TYPE_UNSPECIFIED", "BLOCKED"]

class PersistentPreferredActivity(typing_extensions.TypedDict, total=False):
    categories: typing.List[str]
    receiverActivity: str
    actions: typing.List[str]

class Display(typing_extensions.TypedDict, total=False):
    refreshRate: int
    height: int
    displayId: int
    width: int
    density: int
    name: str
    state: typing_extensions.Literal[
        "DISPLAY_STATE_UNSPECIFIED", "OFF", "ON", "DOZE", "SUSPENDED"
    ]

class EnrollmentToken(typing_extensions.TypedDict, total=False):
    user: User
    oneTimeOnly: bool
    duration: str
    qrCode: str
    name: str
    policyName: str
    value: str
    additionalData: str
    allowPersonalUsage: typing_extensions.Literal[
        "ALLOW_PERSONAL_USAGE_UNSPECIFIED",
        "PERSONAL_USAGE_ALLOWED",
        "PERSONAL_USAGE_DISALLOWED",
    ]
    expirationTimestamp: str

class Status(typing_extensions.TypedDict, total=False):
    details: typing.List[typing.Dict[str, typing.Any]]
    message: str
    code: int

class HardwareInfo(typing_extensions.TypedDict, total=False):
    gpuThrottlingTemperatures: typing.List[float]
    batteryThrottlingTemperatures: typing.List[float]
    batteryShutdownTemperatures: typing.List[float]
    skinShutdownTemperatures: typing.List[float]
    gpuShutdownTemperatures: typing.List[float]
    hardware: str
    cpuShutdownTemperatures: typing.List[float]
    skinThrottlingTemperatures: typing.List[float]
    deviceBasebandVersion: str
    cpuThrottlingTemperatures: typing.List[float]
    manufacturer: str
    brand: str
    serialNumber: str
    model: str

class UserFacingMessage(typing_extensions.TypedDict, total=False):
    localizedMessages: typing.Dict[str, typing.Any]
    defaultMessage: str

class WebAppIcon(typing_extensions.TypedDict, total=False):
    imageData: str

class Policy(typing_extensions.TypedDict, total=False):
    locationMode: typing_extensions.Literal[
        "LOCATION_MODE_UNSPECIFIED",
        "HIGH_ACCURACY",
        "SENSORS_ONLY",
        "BATTERY_SAVING",
        "OFF",
    ]
    mountPhysicalMediaDisabled: bool
    personalUsagePolicies: PersonalUsagePolicies
    advancedSecurityOverrides: AdvancedSecurityOverrides
    outgoingCallsDisabled: bool
    tetheringConfigDisabled: bool
    autoTimeRequired: bool
    stayOnPluggedModes: typing.List[str]
    vpnConfigDisabled: bool
    passwordRequirements: PasswordRequirements
    alwaysOnVpnPackage: AlwaysOnVpnPackage
    screenCaptureDisabled: bool
    complianceRules: typing.List[ComplianceRule]
    installUnknownSourcesAllowed: bool
    shareLocationDisabled: bool
    smsDisabled: bool
    safeBootDisabled: bool
    cameraDisabled: bool
    keyguardDisabled: bool
    choosePrivateKeyRules: typing.List[ChoosePrivateKeyRule]
    permittedInputMethods: PackageNameList
    androidDevicePolicyTracks: typing.List[str]
    longSupportMessage: UserFacingMessage
    debuggingFeaturesAllowed: bool
    factoryResetDisabled: bool
    skipFirstUseHintsEnabled: bool
    policyEnforcementRules: typing.List[PolicyEnforcementRule]
    setWallpaperDisabled: bool
    bluetoothContactSharingDisabled: bool
    passwordPolicies: typing.List[PasswordRequirements]
    openNetworkConfiguration: typing.Dict[str, typing.Any]
    keyguardDisabledFeatures: typing.List[str]
    cellBroadcastsConfigDisabled: bool
    ensureVerifyAppsEnabled: bool
    unmuteMicrophoneDisabled: bool
    networkResetDisabled: bool
    setUserIconDisabled: bool
    maximumTimeToLock: str
    blockApplicationsEnabled: bool
    version: str
    permittedAccessibilityServices: PackageNameList
    wifiConfigsLockdownEnabled: bool
    wifiConfigDisabled: bool
    kioskCustomization: KioskCustomization
    credentialsConfigDisabled: bool
    frpAdminEmails: typing.List[str]
    uninstallAppsDisabled: bool
    applications: typing.List[ApplicationPolicy]
    addUserDisabled: bool
    systemUpdate: SystemUpdate
    bluetoothConfigDisabled: bool
    dataRoamingDisabled: bool
    networkEscapeHatchEnabled: bool
    persistentPreferredActivities: typing.List[PersistentPreferredActivity]
    deviceOwnerLockScreenInfo: UserFacingMessage
    permissionGrants: typing.List[PermissionGrant]
    recommendedGlobalProxy: ProxyInfo
    shortSupportMessage: UserFacingMessage
    outgoingBeamDisabled: bool
    statusBarDisabled: bool
    statusReportingSettings: StatusReportingSettings
    mobileNetworksConfigDisabled: bool
    kioskCustomLauncherEnabled: bool
    appAutoUpdatePolicy: typing_extensions.Literal[
        "APP_AUTO_UPDATE_POLICY_UNSPECIFIED",
        "CHOICE_TO_THE_USER",
        "NEVER",
        "WIFI_ONLY",
        "ALWAYS",
    ]
    usbFileTransferDisabled: bool
    bluetoothDisabled: bool
    defaultPermissionPolicy: typing_extensions.Literal[
        "PERMISSION_POLICY_UNSPECIFIED", "PROMPT", "GRANT", "DENY"
    ]
    name: str
    createWindowsDisabled: bool
    encryptionPolicy: typing_extensions.Literal[
        "ENCRYPTION_POLICY_UNSPECIFIED",
        "ENABLED_WITHOUT_PASSWORD",
        "ENABLED_WITH_PASSWORD",
    ]
    accountTypesWithManagementDisabled: typing.List[str]
    removeUserDisabled: bool
    privateKeySelectionEnabled: bool
    funDisabled: bool
    usbMassStorageEnabled: bool
    minimumApiLevel: int
    setupActions: typing.List[SetupAction]
    adjustVolumeDisabled: bool
    playStoreMode: typing_extensions.Literal[
        "PLAY_STORE_MODE_UNSPECIFIED", "WHITELIST", "BLACKLIST"
    ]
    installAppsDisabled: bool
    modifyAccountsDisabled: bool

class ListPoliciesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    policies: typing.List[Policy]

class AdvancedSecurityOverrides(typing_extensions.TypedDict, total=False):
    untrustedAppsPolicy: typing_extensions.Literal[
        "UNTRUSTED_APPS_POLICY_UNSPECIFIED",
        "DISALLOW_INSTALL",
        "ALLOW_INSTALL_IN_PERSONAL_PROFILE_ONLY",
        "ALLOW_INSTALL_DEVICE_WIDE",
    ]

class FreezePeriod(typing_extensions.TypedDict, total=False):
    endDate: Date
    startDate: Date

class TermsAndConditions(typing_extensions.TypedDict, total=False):
    content: UserFacingMessage
    header: UserFacingMessage

class ManagedConfigurationTemplate(typing_extensions.TypedDict, total=False):
    configurationVariables: typing.Dict[str, typing.Any]
    templateId: str

class SignupUrl(typing_extensions.TypedDict, total=False):
    name: str
    url: str

class Device(typing_extensions.TypedDict, total=False):
    memoryEvents: typing.List[MemoryEvent]
    policyCompliant: bool
    enrollmentTokenName: str
    networkInfo: NetworkInfo
    lastPolicyComplianceReportTime: str
    powerManagementEvents: typing.List[PowerManagementEvent]
    memoryInfo: MemoryInfo
    policyName: str
    previousDeviceNames: typing.List[str]
    appliedPolicyVersion: str
    nonComplianceDetails: typing.List[NonComplianceDetail]
    hardwareInfo: HardwareInfo
    lastStatusReportTime: str
    apiLevel: int
    softwareInfo: SoftwareInfo
    appliedPolicyName: str
    systemProperties: typing.Dict[str, typing.Any]
    disabledReason: UserFacingMessage
    state: typing_extensions.Literal[
        "DEVICE_STATE_UNSPECIFIED", "ACTIVE", "DISABLED", "DELETED", "PROVISIONING"
    ]
    managementMode: typing_extensions.Literal[
        "MANAGEMENT_MODE_UNSPECIFIED", "DEVICE_OWNER", "PROFILE_OWNER"
    ]
    lastPolicySyncTime: str
    ownership: typing_extensions.Literal[
        "OWNERSHIP_UNSPECIFIED", "COMPANY_OWNED", "PERSONALLY_OWNED"
    ]
    name: str
    applicationReports: typing.List[ApplicationReport]
    deviceSettings: DeviceSettings
    displays: typing.List[Display]
    securityPosture: SecurityPosture
    enrollmentTokenData: str
    appliedState: typing_extensions.Literal[
        "DEVICE_STATE_UNSPECIFIED", "ACTIVE", "DISABLED", "DELETED", "PROVISIONING"
    ]
    hardwareStatusSamples: typing.List[HardwareStatus]
    userName: str
    user: User
    enrollmentTime: str

class SigninDetail(typing_extensions.TypedDict, total=False):
    qrCode: str
    allowPersonalUsage: typing_extensions.Literal[
        "ALLOW_PERSONAL_USAGE_UNSPECIFIED",
        "PERSONAL_USAGE_ALLOWED",
        "PERSONAL_USAGE_DISALLOWED",
    ]
    signinUrl: str
    signinEnrollmentToken: str

class StatusReportingSettings(typing_extensions.TypedDict, total=False):
    softwareInfoEnabled: bool
    powerManagementEventsEnabled: bool
    displayInfoEnabled: bool
    deviceSettingsEnabled: bool
    systemPropertiesEnabled: bool
    hardwareStatusEnabled: bool
    networkInfoEnabled: bool
    applicationReportingSettings: ApplicationReportingSettings
    memoryInfoEnabled: bool
    applicationReportsEnabled: bool

class MemoryEvent(typing_extensions.TypedDict, total=False):
    eventType: typing_extensions.Literal[
        "MEMORY_EVENT_TYPE_UNSPECIFIED",
        "RAM_MEASURED",
        "INTERNAL_STORAGE_MEASURED",
        "EXTERNAL_STORAGE_DETECTED",
        "EXTERNAL_STORAGE_REMOVED",
        "EXTERNAL_STORAGE_MEASURED",
    ]
    byteCount: str
    createTime: str

class HardwareStatus(typing_extensions.TypedDict, total=False):
    gpuTemperatures: typing.List[float]
    cpuUsages: typing.List[float]
    batteryTemperatures: typing.List[float]
    createTime: str
    fanSpeeds: typing.List[float]
    skinTemperatures: typing.List[float]
    cpuTemperatures: typing.List[float]

class SecurityPosture(typing_extensions.TypedDict, total=False):
    devicePosture: typing_extensions.Literal[
        "POSTURE_UNSPECIFIED", "SECURE", "AT_RISK", "POTENTIALLY_COMPROMISED"
    ]
    postureDetails: typing.List[PostureDetail]

class PowerManagementEvent(typing_extensions.TypedDict, total=False):
    createTime: str
    eventType: typing_extensions.Literal[
        "POWER_MANAGEMENT_EVENT_TYPE_UNSPECIFIED",
        "BATTERY_LEVEL_COLLECTED",
        "POWER_CONNECTED",
        "POWER_DISCONNECTED",
        "BATTERY_LOW",
        "BATTERY_OKAY",
        "BOOT_COMPLETED",
        "SHUTDOWN",
    ]
    batteryLevel: float

class ApplicationEvent(typing_extensions.TypedDict, total=False):
    eventType: typing_extensions.Literal[
        "APPLICATION_EVENT_TYPE_UNSPECIFIED",
        "INSTALLED",
        "CHANGED",
        "DATA_CLEARED",
        "REMOVED",
        "REPLACED",
        "RESTARTED",
        "PINNED",
        "UNPINNED",
    ]
    createTime: str

class ManagedProperty(typing.Dict[str, typing.Any]): ...

class KioskCustomization(typing_extensions.TypedDict, total=False):
    systemNavigation: typing_extensions.Literal[
        "SYSTEM_NAVIGATION_UNSPECIFIED",
        "NAVIGATION_ENABLED",
        "NAVIGATION_DISABLED",
        "HOME_BUTTON_ONLY",
    ]
    deviceSettings: typing_extensions.Literal[
        "DEVICE_SETTINGS_UNSPECIFIED",
        "SETTINGS_ACCESS_ALLOWED",
        "SETTINGS_ACCESS_BLOCKED",
    ]
    powerButtonActions: typing_extensions.Literal[
        "POWER_BUTTON_ACTIONS_UNSPECIFIED",
        "POWER_BUTTON_AVAILABLE",
        "POWER_BUTTON_BLOCKED",
    ]
    systemErrorWarnings: typing_extensions.Literal[
        "SYSTEM_ERROR_WARNINGS_UNSPECIFIED",
        "ERROR_AND_WARNINGS_ENABLED",
        "ERROR_AND_WARNINGS_MUTED",
    ]
    statusBar: typing_extensions.Literal[
        "STATUS_BAR_UNSPECIFIED",
        "NOTIFICATIONS_AND_SYSTEM_INFO_ENABLED",
        "NOTIFICATIONS_AND_SYSTEM_INFO_DISABLED",
        "SYSTEM_INFO_ONLY",
    ]

class ExternalData(typing_extensions.TypedDict, total=False):
    sha256Hash: str
    url: str

class Empty(typing_extensions.TypedDict, total=False): ...

class WipeAction(typing_extensions.TypedDict, total=False):
    preserveFrp: bool
    wipeAfterDays: int

class ChoosePrivateKeyRule(typing_extensions.TypedDict, total=False):
    urlPattern: str
    privateKeyAlias: str
    packageNames: typing.List[str]

class ApplicationPermission(typing_extensions.TypedDict, total=False):
    name: str
    description: str
    permissionId: str

class Enterprise(typing_extensions.TypedDict, total=False):
    signinDetails: typing.List[SigninDetail]
    appAutoApprovalEnabled: bool
    enterpriseDisplayName: str
    primaryColor: int
    name: str
    logo: ExternalData
    pubsubTopic: str
    termsAndConditions: typing.List[TermsAndConditions]
    enabledNotificationTypes: typing.List[str]

class DeviceSettings(typing_extensions.TypedDict, total=False):
    isDeviceSecure: bool
    isEncrypted: bool
    unknownSourcesEnabled: bool
    adbEnabled: bool
    encryptionStatus: typing_extensions.Literal[
        "ENCRYPTION_STATUS_UNSPECIFIED",
        "UNSUPPORTED",
        "INACTIVE",
        "ACTIVATING",
        "ACTIVE",
        "ACTIVE_DEFAULT_KEY",
        "ACTIVE_PER_USER",
    ]
    developmentSettingsEnabled: bool
    verifyAppsEnabled: bool

class User(typing_extensions.TypedDict, total=False):
    accountIdentifier: str

class WebApp(typing_extensions.TypedDict, total=False):
    title: str
    startUrl: str
    displayMode: typing_extensions.Literal[
        "DISPLAY_MODE_UNSPECIFIED", "MINIMAL_UI", "STANDALONE", "FULL_SCREEN"
    ]
    name: str
    icons: typing.List[WebAppIcon]
    versionCode: str

class MemoryInfo(typing_extensions.TypedDict, total=False):
    totalRam: str
    totalInternalStorage: str

class KeyedAppState(typing_extensions.TypedDict, total=False):
    severity: typing_extensions.Literal["SEVERITY_UNSPECIFIED", "INFO", "ERROR"]
    data: str
    key: str
    lastUpdateTime: str
    createTime: str
    message: str

class LaunchAppAction(typing_extensions.TypedDict, total=False):
    packageName: str

class AppTrackInfo(typing_extensions.TypedDict, total=False):
    trackId: str
    trackAlias: str

class SystemUpdate(typing_extensions.TypedDict, total=False):
    type: typing_extensions.Literal[
        "SYSTEM_UPDATE_TYPE_UNSPECIFIED", "AUTOMATIC", "WINDOWED", "POSTPONE"
    ]
    freezePeriods: typing.List[FreezePeriod]
    endMinutes: int
    startMinutes: int

class Application(typing_extensions.TypedDict, total=False):
    title: str
    managedProperties: typing.List[ManagedProperty]
    permissions: typing.List[ApplicationPermission]
    name: str
    appTracks: typing.List[AppTrackInfo]

class ListWebAppsResponse(typing_extensions.TypedDict, total=False):
    webApps: typing.List[WebApp]
    nextPageToken: str

class ListDevicesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    devices: typing.List[Device]

class ApiLevelCondition(typing_extensions.TypedDict, total=False):
    minApiLevel: int

class Date(typing_extensions.TypedDict, total=False):
    month: int
    day: int
    year: int

class ProxyInfo(typing_extensions.TypedDict, total=False):
    excludedHosts: typing.List[str]
    host: str
    port: int
    pacUri: str

class ListOperationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    operations: typing.List[Operation]

class PasswordRequirements(typing_extensions.TypedDict, total=False):
    maximumFailedPasswordsForWipe: int
    passwordMinimumLowerCase: int
    requirePasswordUnlock: typing_extensions.Literal[
        "REQUIRE_PASSWORD_UNLOCK_UNSPECIFIED",
        "USE_DEFAULT_DEVICE_TIMEOUT",
        "REQUIRE_EVERY_DAY",
    ]
    passwordMinimumLength: int
    passwordMinimumLetters: int
    passwordQuality: typing_extensions.Literal[
        "PASSWORD_QUALITY_UNSPECIFIED",
        "BIOMETRIC_WEAK",
        "SOMETHING",
        "NUMERIC",
        "NUMERIC_COMPLEX",
        "ALPHABETIC",
        "ALPHANUMERIC",
        "COMPLEX",
    ]
    passwordMinimumSymbols: int
    passwordMinimumNonLetter: int
    passwordScope: typing_extensions.Literal[
        "SCOPE_UNSPECIFIED", "SCOPE_DEVICE", "SCOPE_PROFILE"
    ]
    passwordHistoryLength: int
    passwordExpirationTimeout: str
    passwordMinimumUpperCase: int
    passwordMinimumNumeric: int

class PolicyEnforcementRule(typing_extensions.TypedDict, total=False):
    blockAction: BlockAction
    settingName: str
    wipeAction: WipeAction
