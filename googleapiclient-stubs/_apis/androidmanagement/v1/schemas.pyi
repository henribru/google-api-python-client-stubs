import typing

import typing_extensions
@typing.type_check_only
class AdvancedSecurityOverrides(typing_extensions.TypedDict, total=False):
    commonCriteriaMode: typing_extensions.Literal[
        "COMMON_CRITERIA_MODE_UNSPECIFIED",
        "COMMON_CRITERIA_MODE_DISABLED",
        "COMMON_CRITERIA_MODE_ENABLED",
    ]
    untrustedAppsPolicy: typing_extensions.Literal[
        "UNTRUSTED_APPS_POLICY_UNSPECIFIED",
        "DISALLOW_INSTALL",
        "ALLOW_INSTALL_IN_PERSONAL_PROFILE_ONLY",
        "ALLOW_INSTALL_DEVICE_WIDE",
    ]

@typing.type_check_only
class AlwaysOnVpnPackage(typing_extensions.TypedDict, total=False):
    lockdownEnabled: bool
    packageName: str

@typing.type_check_only
class ApiLevelCondition(typing_extensions.TypedDict, total=False):
    minApiLevel: int

@typing.type_check_only
class AppTrackInfo(typing_extensions.TypedDict, total=False):
    trackAlias: str
    trackId: str

@typing.type_check_only
class Application(typing_extensions.TypedDict, total=False):
    appTracks: typing.List[AppTrackInfo]
    managedProperties: typing.List[ManagedProperty]
    name: str
    permissions: typing.List[ApplicationPermission]
    title: str

@typing.type_check_only
class ApplicationEvent(typing_extensions.TypedDict, total=False):
    createTime: str
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

@typing.type_check_only
class ApplicationPermission(typing_extensions.TypedDict, total=False):
    description: str
    name: str
    permissionId: str

@typing.type_check_only
class ApplicationPolicy(typing_extensions.TypedDict, total=False):
    accessibleTrackIds: typing.List[str]
    autoUpdateMode: typing_extensions.Literal[
        "AUTO_UPDATE_MODE_UNSPECIFIED",
        "AUTO_UPDATE_DEFAULT",
        "AUTO_UPDATE_POSTPONED",
        "AUTO_UPDATE_HIGH_PRIORITY",
    ]
    connectedWorkAndPersonalApp: typing_extensions.Literal[
        "CONNECTED_WORK_AND_PERSONAL_APP_UNSPECIFIED",
        "CONNECTED_WORK_AND_PERSONAL_APP_DISALLOWED",
        "CONNECTED_WORK_AND_PERSONAL_APP_ALLOWED",
    ]
    defaultPermissionPolicy: typing_extensions.Literal[
        "PERMISSION_POLICY_UNSPECIFIED", "PROMPT", "GRANT", "DENY"
    ]
    delegatedScopes: typing.List[str]
    disabled: bool
    installType: typing_extensions.Literal[
        "INSTALL_TYPE_UNSPECIFIED",
        "PREINSTALLED",
        "FORCE_INSTALLED",
        "BLOCKED",
        "AVAILABLE",
        "REQUIRED_FOR_SETUP",
        "KIOSK",
    ]
    lockTaskAllowed: bool
    managedConfiguration: typing.Dict[str, typing.Any]
    managedConfigurationTemplate: ManagedConfigurationTemplate
    minimumVersionCode: int
    packageName: str
    permissionGrants: typing.List[PermissionGrant]

@typing.type_check_only
class ApplicationReport(typing_extensions.TypedDict, total=False):
    applicationSource: typing_extensions.Literal[
        "APPLICATION_SOURCE_UNSPECIFIED",
        "SYSTEM_APP_FACTORY_VERSION",
        "SYSTEM_APP_UPDATED_VERSION",
        "INSTALLED_FROM_PLAY_STORE",
    ]
    displayName: str
    events: typing.List[ApplicationEvent]
    installerPackageName: str
    keyedAppStates: typing.List[KeyedAppState]
    packageName: str
    packageSha256Hash: str
    signingKeyCertFingerprints: typing.List[str]
    state: typing_extensions.Literal[
        "APPLICATION_STATE_UNSPECIFIED", "REMOVED", "INSTALLED"
    ]
    versionCode: int
    versionName: str

@typing.type_check_only
class ApplicationReportingSettings(typing_extensions.TypedDict, total=False):
    includeRemovedApps: bool

@typing.type_check_only
class BlockAction(typing_extensions.TypedDict, total=False):
    blockAfterDays: int
    blockScope: typing_extensions.Literal[
        "BLOCK_SCOPE_UNSPECIFIED", "BLOCK_SCOPE_WORK_PROFILE", "BLOCK_SCOPE_DEVICE"
    ]

@typing.type_check_only
class ChoosePrivateKeyRule(typing_extensions.TypedDict, total=False):
    packageNames: typing.List[str]
    privateKeyAlias: str
    urlPattern: str

@typing.type_check_only
class Command(typing_extensions.TypedDict, total=False):
    createTime: str
    duration: str
    errorCode: typing_extensions.Literal[
        "COMMAND_ERROR_CODE_UNSPECIFIED",
        "UNKNOWN",
        "API_LEVEL",
        "MANAGEMENT_MODE",
        "INVALID_VALUE",
        "UNSUPPORTED",
    ]
    newPassword: str
    resetPasswordFlags: typing.List[str]
    type: typing_extensions.Literal[
        "COMMAND_TYPE_UNSPECIFIED",
        "LOCK",
        "RESET_PASSWORD",
        "REBOOT",
        "RELINQUISH_OWNERSHIP",
    ]
    userName: str

@typing.type_check_only
class CommonCriteriaModeInfo(typing_extensions.TypedDict, total=False):
    commonCriteriaModeStatus: typing_extensions.Literal[
        "COMMON_CRITERIA_MODE_STATUS_UNKNOWN",
        "COMMON_CRITERIA_MODE_DISABLED",
        "COMMON_CRITERIA_MODE_ENABLED",
    ]

@typing.type_check_only
class ComplianceRule(typing_extensions.TypedDict, total=False):
    apiLevelCondition: ApiLevelCondition
    disableApps: bool
    nonComplianceDetailCondition: NonComplianceDetailCondition
    packageNamesToDisable: typing.List[str]

@typing.type_check_only
class ContactInfo(typing_extensions.TypedDict, total=False):
    contactEmail: str
    dataProtectionOfficerEmail: str
    dataProtectionOfficerName: str
    dataProtectionOfficerPhone: str
    euRepresentativeEmail: str
    euRepresentativeName: str
    euRepresentativePhone: str

@typing.type_check_only
class Date(typing_extensions.TypedDict, total=False):
    day: int
    month: int
    year: int

@typing.type_check_only
class Device(typing_extensions.TypedDict, total=False):
    apiLevel: int
    applicationReports: typing.List[ApplicationReport]
    appliedPolicyName: str
    appliedPolicyVersion: str
    appliedState: typing_extensions.Literal[
        "DEVICE_STATE_UNSPECIFIED", "ACTIVE", "DISABLED", "DELETED", "PROVISIONING"
    ]
    commonCriteriaModeInfo: CommonCriteriaModeInfo
    deviceSettings: DeviceSettings
    disabledReason: UserFacingMessage
    displays: typing.List[Display]
    enrollmentTime: str
    enrollmentTokenData: str
    enrollmentTokenName: str
    hardwareInfo: HardwareInfo
    hardwareStatusSamples: typing.List[HardwareStatus]
    lastPolicyComplianceReportTime: str
    lastPolicySyncTime: str
    lastStatusReportTime: str
    managementMode: typing_extensions.Literal[
        "MANAGEMENT_MODE_UNSPECIFIED", "DEVICE_OWNER", "PROFILE_OWNER"
    ]
    memoryEvents: typing.List[MemoryEvent]
    memoryInfo: MemoryInfo
    name: str
    networkInfo: NetworkInfo
    nonComplianceDetails: typing.List[NonComplianceDetail]
    ownership: typing_extensions.Literal[
        "OWNERSHIP_UNSPECIFIED", "COMPANY_OWNED", "PERSONALLY_OWNED"
    ]
    policyCompliant: bool
    policyName: str
    powerManagementEvents: typing.List[PowerManagementEvent]
    previousDeviceNames: typing.List[str]
    securityPosture: SecurityPosture
    softwareInfo: SoftwareInfo
    state: typing_extensions.Literal[
        "DEVICE_STATE_UNSPECIFIED", "ACTIVE", "DISABLED", "DELETED", "PROVISIONING"
    ]
    systemProperties: typing.Dict[str, typing.Any]
    user: User
    userName: str

@typing.type_check_only
class DeviceSettings(typing_extensions.TypedDict, total=False):
    adbEnabled: bool
    developmentSettingsEnabled: bool
    encryptionStatus: typing_extensions.Literal[
        "ENCRYPTION_STATUS_UNSPECIFIED",
        "UNSUPPORTED",
        "INACTIVE",
        "ACTIVATING",
        "ACTIVE",
        "ACTIVE_DEFAULT_KEY",
        "ACTIVE_PER_USER",
    ]
    isDeviceSecure: bool
    isEncrypted: bool
    unknownSourcesEnabled: bool
    verifyAppsEnabled: bool

@typing.type_check_only
class Display(typing_extensions.TypedDict, total=False):
    density: int
    displayId: int
    height: int
    name: str
    refreshRate: int
    state: typing_extensions.Literal[
        "DISPLAY_STATE_UNSPECIFIED", "OFF", "ON", "DOZE", "SUSPENDED"
    ]
    width: int

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class EnrollmentToken(typing_extensions.TypedDict, total=False):
    additionalData: str
    allowPersonalUsage: typing_extensions.Literal[
        "ALLOW_PERSONAL_USAGE_UNSPECIFIED",
        "PERSONAL_USAGE_ALLOWED",
        "PERSONAL_USAGE_DISALLOWED",
    ]
    duration: str
    expirationTimestamp: str
    name: str
    oneTimeOnly: bool
    policyName: str
    qrCode: str
    user: User
    value: str

@typing.type_check_only
class Enterprise(typing_extensions.TypedDict, total=False):
    appAutoApprovalEnabled: bool
    contactInfo: ContactInfo
    enabledNotificationTypes: typing.List[str]
    enterpriseDisplayName: str
    logo: ExternalData
    name: str
    primaryColor: int
    pubsubTopic: str
    signinDetails: typing.List[SigninDetail]
    termsAndConditions: typing.List[TermsAndConditions]

@typing.type_check_only
class ExternalData(typing_extensions.TypedDict, total=False):
    sha256Hash: str
    url: str

@typing.type_check_only
class FreezePeriod(typing_extensions.TypedDict, total=False):
    endDate: Date
    startDate: Date

@typing.type_check_only
class HardwareInfo(typing_extensions.TypedDict, total=False):
    batteryShutdownTemperatures: typing.List[float]
    batteryThrottlingTemperatures: typing.List[float]
    brand: str
    cpuShutdownTemperatures: typing.List[float]
    cpuThrottlingTemperatures: typing.List[float]
    deviceBasebandVersion: str
    gpuShutdownTemperatures: typing.List[float]
    gpuThrottlingTemperatures: typing.List[float]
    hardware: str
    manufacturer: str
    model: str
    serialNumber: str
    skinShutdownTemperatures: typing.List[float]
    skinThrottlingTemperatures: typing.List[float]

@typing.type_check_only
class HardwareStatus(typing_extensions.TypedDict, total=False):
    batteryTemperatures: typing.List[float]
    cpuTemperatures: typing.List[float]
    cpuUsages: typing.List[float]
    createTime: str
    fanSpeeds: typing.List[float]
    gpuTemperatures: typing.List[float]
    skinTemperatures: typing.List[float]

@typing.type_check_only
class KeyedAppState(typing_extensions.TypedDict, total=False):
    createTime: str
    data: str
    key: str
    lastUpdateTime: str
    message: str
    severity: typing_extensions.Literal["SEVERITY_UNSPECIFIED", "INFO", "ERROR"]

@typing.type_check_only
class KioskCustomization(typing_extensions.TypedDict, total=False):
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
    statusBar: typing_extensions.Literal[
        "STATUS_BAR_UNSPECIFIED",
        "NOTIFICATIONS_AND_SYSTEM_INFO_ENABLED",
        "NOTIFICATIONS_AND_SYSTEM_INFO_DISABLED",
        "SYSTEM_INFO_ONLY",
    ]
    systemErrorWarnings: typing_extensions.Literal[
        "SYSTEM_ERROR_WARNINGS_UNSPECIFIED",
        "ERROR_AND_WARNINGS_ENABLED",
        "ERROR_AND_WARNINGS_MUTED",
    ]
    systemNavigation: typing_extensions.Literal[
        "SYSTEM_NAVIGATION_UNSPECIFIED",
        "NAVIGATION_ENABLED",
        "NAVIGATION_DISABLED",
        "HOME_BUTTON_ONLY",
    ]

@typing.type_check_only
class LaunchAppAction(typing_extensions.TypedDict, total=False):
    packageName: str

@typing.type_check_only
class ListDevicesResponse(typing_extensions.TypedDict, total=False):
    devices: typing.List[Device]
    nextPageToken: str

@typing.type_check_only
class ListEnterprisesResponse(typing_extensions.TypedDict, total=False):
    enterprises: typing.List[Enterprise]
    nextPageToken: str

@typing.type_check_only
class ListOperationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    operations: typing.List[Operation]

@typing.type_check_only
class ListPoliciesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    policies: typing.List[Policy]

@typing.type_check_only
class ListWebAppsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    webApps: typing.List[WebApp]

@typing.type_check_only
class ManagedConfigurationTemplate(typing_extensions.TypedDict, total=False):
    configurationVariables: typing.Dict[str, typing.Any]
    templateId: str

@typing.type_check_only
class ManagedProperty(typing.Dict[str, typing.Any]): ...

@typing.type_check_only
class ManagedPropertyEntry(typing_extensions.TypedDict, total=False):
    name: str
    value: str

@typing.type_check_only
class MemoryEvent(typing_extensions.TypedDict, total=False):
    byteCount: str
    createTime: str
    eventType: typing_extensions.Literal[
        "MEMORY_EVENT_TYPE_UNSPECIFIED",
        "RAM_MEASURED",
        "INTERNAL_STORAGE_MEASURED",
        "EXTERNAL_STORAGE_DETECTED",
        "EXTERNAL_STORAGE_REMOVED",
        "EXTERNAL_STORAGE_MEASURED",
    ]

@typing.type_check_only
class MemoryInfo(typing_extensions.TypedDict, total=False):
    totalInternalStorage: str
    totalRam: str

@typing.type_check_only
class NetworkInfo(typing_extensions.TypedDict, total=False):
    imei: str
    meid: str
    networkOperatorName: str
    telephonyInfos: typing.List[TelephonyInfo]
    wifiMacAddress: str

@typing.type_check_only
class NonComplianceDetail(typing_extensions.TypedDict, total=False):
    currentValue: typing.Any
    fieldPath: str
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
    packageName: str
    settingName: str

@typing.type_check_only
class NonComplianceDetailCondition(typing_extensions.TypedDict, total=False):
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
    packageName: str
    settingName: str

@typing.type_check_only
class Operation(typing_extensions.TypedDict, total=False):
    done: bool
    error: Status
    metadata: typing.Dict[str, typing.Any]
    name: str
    response: typing.Dict[str, typing.Any]

@typing.type_check_only
class PackageNameList(typing_extensions.TypedDict, total=False):
    packageNames: typing.List[str]

@typing.type_check_only
class PasswordRequirements(typing_extensions.TypedDict, total=False):
    maximumFailedPasswordsForWipe: int
    passwordExpirationTimeout: str
    passwordHistoryLength: int
    passwordMinimumLength: int
    passwordMinimumLetters: int
    passwordMinimumLowerCase: int
    passwordMinimumNonLetter: int
    passwordMinimumNumeric: int
    passwordMinimumSymbols: int
    passwordMinimumUpperCase: int
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
    passwordScope: typing_extensions.Literal[
        "SCOPE_UNSPECIFIED", "SCOPE_DEVICE", "SCOPE_PROFILE"
    ]
    requirePasswordUnlock: typing_extensions.Literal[
        "REQUIRE_PASSWORD_UNLOCK_UNSPECIFIED",
        "USE_DEFAULT_DEVICE_TIMEOUT",
        "REQUIRE_EVERY_DAY",
    ]

@typing.type_check_only
class PermissionGrant(typing_extensions.TypedDict, total=False):
    permission: str
    policy: typing_extensions.Literal[
        "PERMISSION_POLICY_UNSPECIFIED", "PROMPT", "GRANT", "DENY"
    ]

@typing.type_check_only
class PersistentPreferredActivity(typing_extensions.TypedDict, total=False):
    actions: typing.List[str]
    categories: typing.List[str]
    receiverActivity: str

@typing.type_check_only
class PersonalApplicationPolicy(typing_extensions.TypedDict, total=False):
    installType: typing_extensions.Literal[
        "INSTALL_TYPE_UNSPECIFIED", "BLOCKED", "AVAILABLE"
    ]
    packageName: str

@typing.type_check_only
class PersonalUsagePolicies(typing_extensions.TypedDict, total=False):
    accountTypesWithManagementDisabled: typing.List[str]
    cameraDisabled: bool
    maxDaysWithWorkOff: int
    personalApplications: typing.List[PersonalApplicationPolicy]
    personalPlayStoreMode: typing_extensions.Literal[
        "PLAY_STORE_MODE_UNSPECIFIED", "BLACKLIST", "BLOCKLIST", "ALLOWLIST"
    ]
    screenCaptureDisabled: bool

@typing.type_check_only
class Policy(typing_extensions.TypedDict, total=False):
    accountTypesWithManagementDisabled: typing.List[str]
    addUserDisabled: bool
    adjustVolumeDisabled: bool
    advancedSecurityOverrides: AdvancedSecurityOverrides
    alwaysOnVpnPackage: AlwaysOnVpnPackage
    androidDevicePolicyTracks: typing.List[str]
    appAutoUpdatePolicy: typing_extensions.Literal[
        "APP_AUTO_UPDATE_POLICY_UNSPECIFIED",
        "CHOICE_TO_THE_USER",
        "NEVER",
        "WIFI_ONLY",
        "ALWAYS",
    ]
    applications: typing.List[ApplicationPolicy]
    autoDateAndTimeZone: typing_extensions.Literal[
        "AUTO_DATE_AND_TIME_ZONE_UNSPECIFIED",
        "AUTO_DATE_AND_TIME_ZONE_USER_CHOICE",
        "AUTO_DATE_AND_TIME_ZONE_ENFORCED",
    ]
    autoTimeRequired: bool
    blockApplicationsEnabled: bool
    bluetoothConfigDisabled: bool
    bluetoothContactSharingDisabled: bool
    bluetoothDisabled: bool
    cameraDisabled: bool
    cellBroadcastsConfigDisabled: bool
    choosePrivateKeyRules: typing.List[ChoosePrivateKeyRule]
    complianceRules: typing.List[ComplianceRule]
    createWindowsDisabled: bool
    credentialsConfigDisabled: bool
    dataRoamingDisabled: bool
    debuggingFeaturesAllowed: bool
    defaultPermissionPolicy: typing_extensions.Literal[
        "PERMISSION_POLICY_UNSPECIFIED", "PROMPT", "GRANT", "DENY"
    ]
    deviceOwnerLockScreenInfo: UserFacingMessage
    encryptionPolicy: typing_extensions.Literal[
        "ENCRYPTION_POLICY_UNSPECIFIED",
        "ENABLED_WITHOUT_PASSWORD",
        "ENABLED_WITH_PASSWORD",
    ]
    ensureVerifyAppsEnabled: bool
    factoryResetDisabled: bool
    frpAdminEmails: typing.List[str]
    funDisabled: bool
    installAppsDisabled: bool
    installUnknownSourcesAllowed: bool
    keyguardDisabled: bool
    keyguardDisabledFeatures: typing.List[str]
    kioskCustomLauncherEnabled: bool
    kioskCustomization: KioskCustomization
    locationMode: typing_extensions.Literal[
        "LOCATION_MODE_UNSPECIFIED",
        "HIGH_ACCURACY",
        "SENSORS_ONLY",
        "BATTERY_SAVING",
        "OFF",
        "LOCATION_USER_CHOICE",
        "LOCATION_ENFORCED",
        "LOCATION_DISABLED",
    ]
    longSupportMessage: UserFacingMessage
    maximumTimeToLock: str
    minimumApiLevel: int
    mobileNetworksConfigDisabled: bool
    modifyAccountsDisabled: bool
    mountPhysicalMediaDisabled: bool
    name: str
    networkEscapeHatchEnabled: bool
    networkResetDisabled: bool
    openNetworkConfiguration: typing.Dict[str, typing.Any]
    outgoingBeamDisabled: bool
    outgoingCallsDisabled: bool
    passwordPolicies: typing.List[PasswordRequirements]
    passwordRequirements: PasswordRequirements
    permissionGrants: typing.List[PermissionGrant]
    permittedAccessibilityServices: PackageNameList
    permittedInputMethods: PackageNameList
    persistentPreferredActivities: typing.List[PersistentPreferredActivity]
    personalUsagePolicies: PersonalUsagePolicies
    playStoreMode: typing_extensions.Literal[
        "PLAY_STORE_MODE_UNSPECIFIED", "WHITELIST", "BLACKLIST"
    ]
    policyEnforcementRules: typing.List[PolicyEnforcementRule]
    privateKeySelectionEnabled: bool
    recommendedGlobalProxy: ProxyInfo
    removeUserDisabled: bool
    safeBootDisabled: bool
    screenCaptureDisabled: bool
    setUserIconDisabled: bool
    setWallpaperDisabled: bool
    setupActions: typing.List[SetupAction]
    shareLocationDisabled: bool
    shortSupportMessage: UserFacingMessage
    skipFirstUseHintsEnabled: bool
    smsDisabled: bool
    statusBarDisabled: bool
    statusReportingSettings: StatusReportingSettings
    stayOnPluggedModes: typing.List[str]
    systemUpdate: SystemUpdate
    tetheringConfigDisabled: bool
    uninstallAppsDisabled: bool
    unmuteMicrophoneDisabled: bool
    usbFileTransferDisabled: bool
    usbMassStorageEnabled: bool
    version: str
    vpnConfigDisabled: bool
    wifiConfigDisabled: bool
    wifiConfigsLockdownEnabled: bool

@typing.type_check_only
class PolicyEnforcementRule(typing_extensions.TypedDict, total=False):
    blockAction: BlockAction
    settingName: str
    wipeAction: WipeAction

@typing.type_check_only
class PostureDetail(typing_extensions.TypedDict, total=False):
    advice: typing.List[UserFacingMessage]
    securityRisk: typing_extensions.Literal[
        "SECURITY_RISK_UNSPECIFIED", "UNKNOWN_OS", "COMPROMISED_OS"
    ]

@typing.type_check_only
class PowerManagementEvent(typing_extensions.TypedDict, total=False):
    batteryLevel: float
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

@typing.type_check_only
class ProxyInfo(typing_extensions.TypedDict, total=False):
    excludedHosts: typing.List[str]
    host: str
    pacUri: str
    port: int

@typing.type_check_only
class SecurityPosture(typing_extensions.TypedDict, total=False):
    devicePosture: typing_extensions.Literal[
        "POSTURE_UNSPECIFIED", "SECURE", "AT_RISK", "POTENTIALLY_COMPROMISED"
    ]
    postureDetails: typing.List[PostureDetail]

@typing.type_check_only
class SetupAction(typing_extensions.TypedDict, total=False):
    description: UserFacingMessage
    launchApp: LaunchAppAction
    title: UserFacingMessage

@typing.type_check_only
class SigninDetail(typing_extensions.TypedDict, total=False):
    allowPersonalUsage: typing_extensions.Literal[
        "ALLOW_PERSONAL_USAGE_UNSPECIFIED",
        "PERSONAL_USAGE_ALLOWED",
        "PERSONAL_USAGE_DISALLOWED",
    ]
    qrCode: str
    signinEnrollmentToken: str
    signinUrl: str

@typing.type_check_only
class SignupUrl(typing_extensions.TypedDict, total=False):
    name: str
    url: str

@typing.type_check_only
class SoftwareInfo(typing_extensions.TypedDict, total=False):
    androidBuildNumber: str
    androidBuildTime: str
    androidDevicePolicyVersionCode: int
    androidDevicePolicyVersionName: str
    androidVersion: str
    bootloaderVersion: str
    deviceBuildSignature: str
    deviceKernelVersion: str
    primaryLanguageCode: str
    securityPatchLevel: str
    systemUpdateInfo: SystemUpdateInfo

@typing.type_check_only
class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: typing.List[typing.Dict[str, typing.Any]]
    message: str

@typing.type_check_only
class StatusReportingSettings(typing_extensions.TypedDict, total=False):
    applicationReportingSettings: ApplicationReportingSettings
    applicationReportsEnabled: bool
    commonCriteriaModeEnabled: bool
    deviceSettingsEnabled: bool
    displayInfoEnabled: bool
    hardwareStatusEnabled: bool
    memoryInfoEnabled: bool
    networkInfoEnabled: bool
    powerManagementEventsEnabled: bool
    softwareInfoEnabled: bool
    systemPropertiesEnabled: bool

@typing.type_check_only
class SystemUpdate(typing_extensions.TypedDict, total=False):
    endMinutes: int
    freezePeriods: typing.List[FreezePeriod]
    startMinutes: int
    type: typing_extensions.Literal[
        "SYSTEM_UPDATE_TYPE_UNSPECIFIED", "AUTOMATIC", "WINDOWED", "POSTPONE"
    ]

@typing.type_check_only
class SystemUpdateInfo(typing_extensions.TypedDict, total=False):
    updateReceivedTime: str
    updateStatus: typing_extensions.Literal[
        "UPDATE_STATUS_UNKNOWN",
        "UP_TO_DATE",
        "UNKNOWN_UPDATE_AVAILABLE",
        "SECURITY_UPDATE_AVAILABLE",
        "OS_UPDATE_AVAILABLE",
    ]

@typing.type_check_only
class TelephonyInfo(typing_extensions.TypedDict, total=False):
    carrierName: str
    phoneNumber: str

@typing.type_check_only
class TermsAndConditions(typing_extensions.TypedDict, total=False):
    content: UserFacingMessage
    header: UserFacingMessage

@typing.type_check_only
class User(typing_extensions.TypedDict, total=False):
    accountIdentifier: str

@typing.type_check_only
class UserFacingMessage(typing_extensions.TypedDict, total=False):
    defaultMessage: str
    localizedMessages: typing.Dict[str, typing.Any]

@typing.type_check_only
class WebApp(typing_extensions.TypedDict, total=False):
    displayMode: typing_extensions.Literal[
        "DISPLAY_MODE_UNSPECIFIED", "MINIMAL_UI", "STANDALONE", "FULL_SCREEN"
    ]
    icons: typing.List[WebAppIcon]
    name: str
    startUrl: str
    title: str
    versionCode: str

@typing.type_check_only
class WebAppIcon(typing_extensions.TypedDict, total=False):
    imageData: str

@typing.type_check_only
class WebToken(typing_extensions.TypedDict, total=False):
    enabledFeatures: typing.List[str]
    name: str
    parentFrameUrl: str
    permissions: typing.List[str]
    value: str

@typing.type_check_only
class WipeAction(typing_extensions.TypedDict, total=False):
    preserveFrp: bool
    wipeAfterDays: int
