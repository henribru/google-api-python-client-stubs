import typing

import typing_extensions

_list = list

@typing.type_check_only
class AdbShellCommandEvent(typing_extensions.TypedDict, total=False):
    shellCmd: str

@typing.type_check_only
class AdbShellInteractiveEvent(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class AddEsimParams(typing_extensions.TypedDict, total=False):
    activationCode: str
    activationState: typing_extensions.Literal[
        "ACTIVATION_STATE_UNSPECIFIED", "ACTIVATED", "NOT_ACTIVATED"
    ]

@typing.type_check_only
class AdvancedSecurityOverrides(typing_extensions.TypedDict, total=False):
    commonCriteriaMode: typing_extensions.Literal[
        "COMMON_CRITERIA_MODE_UNSPECIFIED",
        "COMMON_CRITERIA_MODE_DISABLED",
        "COMMON_CRITERIA_MODE_ENABLED",
    ]
    contentProtectionPolicy: typing_extensions.Literal[
        "CONTENT_PROTECTION_POLICY_UNSPECIFIED",
        "CONTENT_PROTECTION_DISABLED",
        "CONTENT_PROTECTION_ENFORCED",
        "CONTENT_PROTECTION_USER_CHOICE",
    ]
    developerSettings: typing_extensions.Literal[
        "DEVELOPER_SETTINGS_UNSPECIFIED",
        "DEVELOPER_SETTINGS_DISABLED",
        "DEVELOPER_SETTINGS_ALLOWED",
    ]
    googlePlayProtectVerifyApps: typing_extensions.Literal[
        "GOOGLE_PLAY_PROTECT_VERIFY_APPS_UNSPECIFIED",
        "VERIFY_APPS_ENFORCED",
        "VERIFY_APPS_USER_CHOICE",
    ]
    mtePolicy: typing_extensions.Literal[
        "MTE_POLICY_UNSPECIFIED", "MTE_USER_CHOICE", "MTE_ENFORCED", "MTE_DISABLED"
    ]
    personalAppsThatCanReadWorkNotifications: _list[str]
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
class ApnPolicy(typing_extensions.TypedDict, total=False):
    apnSettings: _list[ApnSetting]
    overrideApns: typing_extensions.Literal[
        "OVERRIDE_APNS_UNSPECIFIED", "OVERRIDE_APNS_DISABLED", "OVERRIDE_APNS_ENABLED"
    ]

@typing.type_check_only
class ApnSetting(typing_extensions.TypedDict, total=False):
    alwaysOnSetting: typing_extensions.Literal[
        "ALWAYS_ON_SETTING_UNSPECIFIED", "NOT_ALWAYS_ON", "ALWAYS_ON"
    ]
    apn: str
    apnTypes: _list[
        typing_extensions.Literal[
            "APN_TYPE_UNSPECIFIED",
            "ENTERPRISE",
            "BIP",
            "CBS",
            "DEFAULT",
            "DUN",
            "EMERGENCY",
            "FOTA",
            "HIPRI",
            "IA",
            "IMS",
            "MCX",
            "MMS",
            "RCS",
            "SUPL",
            "VSIM",
            "XCAP",
        ]
    ]
    authType: typing_extensions.Literal[
        "AUTH_TYPE_UNSPECIFIED", "NONE", "PAP", "CHAP", "PAP_OR_CHAP"
    ]
    carrierId: int
    displayName: str
    mmsProxyAddress: str
    mmsProxyPort: int
    mmsc: str
    mtuV4: int
    mtuV6: int
    mvnoType: typing_extensions.Literal[
        "MVNO_TYPE_UNSPECIFIED", "GID", "ICCID", "IMSI", "SPN"
    ]
    networkTypes: _list[
        typing_extensions.Literal[
            "NETWORK_TYPE_UNSPECIFIED",
            "EDGE",
            "GPRS",
            "GSM",
            "HSDPA",
            "HSPA",
            "HSPAP",
            "HSUPA",
            "IWLAN",
            "LTE",
            "NR",
            "TD_SCDMA",
            "UMTS",
        ]
    ]
    numericOperatorId: str
    password: str
    protocol: typing_extensions.Literal[
        "PROTOCOL_UNSPECIFIED", "IP", "IPV4V6", "IPV6", "NON_IP", "PPP", "UNSTRUCTURED"
    ]
    proxyAddress: str
    proxyPort: int
    roamingProtocol: typing_extensions.Literal[
        "PROTOCOL_UNSPECIFIED", "IP", "IPV4V6", "IPV6", "NON_IP", "PPP", "UNSTRUCTURED"
    ]
    username: str

@typing.type_check_only
class AppProcessInfo(typing_extensions.TypedDict, total=False):
    apkSha256Hash: str
    packageNames: _list[str]
    pid: int
    processName: str
    seinfo: str
    startTime: str
    uid: int

@typing.type_check_only
class AppProcessStartEvent(typing_extensions.TypedDict, total=False):
    processInfo: AppProcessInfo

@typing.type_check_only
class AppTrackInfo(typing_extensions.TypedDict, total=False):
    trackAlias: str
    trackId: str

@typing.type_check_only
class AppVersion(typing_extensions.TypedDict, total=False):
    production: bool
    trackIds: _list[str]
    versionCode: int
    versionString: str

@typing.type_check_only
class Application(typing_extensions.TypedDict, total=False):
    appPricing: typing_extensions.Literal[
        "APP_PRICING_UNSPECIFIED", "FREE", "FREE_WITH_IN_APP_PURCHASE", "PAID"
    ]
    appTracks: _list[AppTrackInfo]
    appVersions: _list[AppVersion]
    author: str
    availableCountries: _list[str]
    category: str
    contentRating: typing_extensions.Literal[
        "CONTENT_RATING_UNSPECIFIED",
        "THREE_YEARS",
        "SEVEN_YEARS",
        "TWELVE_YEARS",
        "SIXTEEN_YEARS",
        "EIGHTEEN_YEARS",
    ]
    description: str
    distributionChannel: typing_extensions.Literal[
        "DISTRIBUTION_CHANNEL_UNSPECIFIED",
        "PUBLIC_GOOGLE_HOSTED",
        "PRIVATE_GOOGLE_HOSTED",
        "PRIVATE_SELF_HOSTED",
    ]
    features: _list[typing_extensions.Literal["APP_FEATURE_UNSPECIFIED", "VPN_APP"]]
    fullDescription: str
    iconUrl: str
    managedProperties: _list[ManagedProperty]
    minAndroidSdkVersion: int
    name: str
    permissions: _list[ApplicationPermission]
    playStoreUrl: str
    recentChanges: str
    screenshotUrls: _list[str]
    smallIconUrl: str
    title: str
    updateTime: str

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
    accessibleTrackIds: _list[str]
    alwaysOnVpnLockdownExemption: typing_extensions.Literal[
        "ALWAYS_ON_VPN_LOCKDOWN_EXEMPTION_UNSPECIFIED",
        "VPN_LOCKDOWN_ENFORCED",
        "VPN_LOCKDOWN_EXEMPTION",
    ]
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
    credentialProviderPolicy: typing_extensions.Literal[
        "CREDENTIAL_PROVIDER_POLICY_UNSPECIFIED", "CREDENTIAL_PROVIDER_ALLOWED"
    ]
    customAppConfig: CustomAppConfig
    defaultPermissionPolicy: typing_extensions.Literal[
        "PERMISSION_POLICY_UNSPECIFIED", "PROMPT", "GRANT", "DENY"
    ]
    delegatedScopes: _list[
        typing_extensions.Literal[
            "DELEGATED_SCOPE_UNSPECIFIED",
            "CERT_INSTALL",
            "MANAGED_CONFIGURATIONS",
            "BLOCK_UNINSTALL",
            "PERMISSION_GRANT",
            "PACKAGE_ACCESS",
            "ENABLE_SYSTEM_APP",
            "NETWORK_ACTIVITY_LOGS",
            "SECURITY_LOGS",
            "CERT_SELECTION",
        ]
    ]
    disabled: bool
    extensionConfig: ExtensionConfig
    installConstraint: _list[InstallConstraint]
    installPriority: int
    installType: typing_extensions.Literal[
        "INSTALL_TYPE_UNSPECIFIED",
        "PREINSTALLED",
        "FORCE_INSTALLED",
        "BLOCKED",
        "AVAILABLE",
        "REQUIRED_FOR_SETUP",
        "KIOSK",
        "CUSTOM",
    ]
    lockTaskAllowed: bool
    managedConfiguration: dict[str, typing.Any]
    managedConfigurationTemplate: ManagedConfigurationTemplate
    minimumVersionCode: int
    packageName: str
    permissionGrants: _list[PermissionGrant]
    preferentialNetworkId: typing_extensions.Literal[
        "PREFERENTIAL_NETWORK_ID_UNSPECIFIED",
        "NO_PREFERENTIAL_NETWORK",
        "PREFERENTIAL_NETWORK_ID_ONE",
        "PREFERENTIAL_NETWORK_ID_TWO",
        "PREFERENTIAL_NETWORK_ID_THREE",
        "PREFERENTIAL_NETWORK_ID_FOUR",
        "PREFERENTIAL_NETWORK_ID_FIVE",
    ]
    roles: _list[Role]
    signingKeyCerts: _list[ApplicationSigningKeyCert]
    userControlSettings: typing_extensions.Literal[
        "USER_CONTROL_SETTINGS_UNSPECIFIED",
        "USER_CONTROL_ALLOWED",
        "USER_CONTROL_DISALLOWED",
    ]
    workProfileWidgets: typing_extensions.Literal[
        "WORK_PROFILE_WIDGETS_UNSPECIFIED",
        "WORK_PROFILE_WIDGETS_ALLOWED",
        "WORK_PROFILE_WIDGETS_DISALLOWED",
    ]

@typing.type_check_only
class ApplicationPolicyChange(typing_extensions.TypedDict, total=False):
    application: ApplicationPolicy
    updateMask: str

@typing.type_check_only
class ApplicationReport(typing_extensions.TypedDict, total=False):
    applicationSource: typing_extensions.Literal[
        "APPLICATION_SOURCE_UNSPECIFIED",
        "SYSTEM_APP_FACTORY_VERSION",
        "SYSTEM_APP_UPDATED_VERSION",
        "INSTALLED_FROM_PLAY_STORE",
        "CUSTOM",
    ]
    displayName: str
    events: _list[ApplicationEvent]
    installerPackageName: str
    keyedAppStates: _list[KeyedAppState]
    packageName: str
    packageSha256Hash: str
    signingKeyCertFingerprints: _list[str]
    state: typing_extensions.Literal[
        "APPLICATION_STATE_UNSPECIFIED", "REMOVED", "INSTALLED"
    ]
    userFacingType: typing_extensions.Literal[
        "USER_FACING_TYPE_UNSPECIFIED", "NOT_USER_FACING", "USER_FACING"
    ]
    versionCode: int
    versionName: str

@typing.type_check_only
class ApplicationReportingSettings(typing_extensions.TypedDict, total=False):
    includeRemovedApps: bool

@typing.type_check_only
class ApplicationSigningKeyCert(typing_extensions.TypedDict, total=False):
    signingKeyCertFingerprintSha256: str

@typing.type_check_only
class BackupServiceToggledEvent(typing_extensions.TypedDict, total=False):
    adminPackageName: str
    adminUserId: int
    backupServiceState: typing_extensions.Literal[
        "BACKUP_SERVICE_STATE_UNSPECIFIED",
        "BACKUP_SERVICE_DISABLED",
        "BACKUP_SERVICE_ENABLED",
    ]

@typing.type_check_only
class BatchUsageLogEvents(typing_extensions.TypedDict, total=False):
    device: str
    retrievalTime: str
    usageLogEvents: _list[UsageLogEvent]
    user: str

@typing.type_check_only
class BlockAction(typing_extensions.TypedDict, total=False):
    blockAfterDays: int
    blockScope: typing_extensions.Literal[
        "BLOCK_SCOPE_UNSPECIFIED", "BLOCK_SCOPE_WORK_PROFILE", "BLOCK_SCOPE_DEVICE"
    ]

@typing.type_check_only
class CertAuthorityInstalledEvent(typing_extensions.TypedDict, total=False):
    certificate: str
    success: bool
    userId: int

@typing.type_check_only
class CertAuthorityRemovedEvent(typing_extensions.TypedDict, total=False):
    certificate: str
    success: bool
    userId: int

@typing.type_check_only
class CertValidationFailureEvent(typing_extensions.TypedDict, total=False):
    failureReason: str

@typing.type_check_only
class ChoosePrivateKeyRule(typing_extensions.TypedDict, total=False):
    packageNames: _list[str]
    privateKeyAlias: str
    urlPattern: str

@typing.type_check_only
class ClearAppsDataParams(typing_extensions.TypedDict, total=False):
    packageNames: _list[str]

@typing.type_check_only
class ClearAppsDataStatus(typing_extensions.TypedDict, total=False):
    results: dict[str, typing.Any]

@typing.type_check_only
class Command(typing_extensions.TypedDict, total=False):
    addEsimParams: AddEsimParams
    clearAppsDataParams: ClearAppsDataParams
    clearAppsDataStatus: ClearAppsDataStatus
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
    esimStatus: EsimCommandStatus
    newPassword: str
    removeEsimParams: RemoveEsimParams
    requestDeviceInfoParams: RequestDeviceInfoParams
    requestDeviceInfoStatus: RequestDeviceInfoStatus
    resetPasswordFlags: _list[
        typing_extensions.Literal[
            "RESET_PASSWORD_FLAG_UNSPECIFIED",
            "REQUIRE_ENTRY",
            "DO_NOT_ASK_CREDENTIALS_ON_BOOT",
            "LOCK_NOW",
        ]
    ]
    startLostModeParams: StartLostModeParams
    startLostModeStatus: StartLostModeStatus
    stopLostModeParams: StopLostModeParams
    stopLostModeStatus: StopLostModeStatus
    type: typing_extensions.Literal[
        "COMMAND_TYPE_UNSPECIFIED",
        "LOCK",
        "RESET_PASSWORD",
        "REBOOT",
        "RELINQUISH_OWNERSHIP",
        "CLEAR_APP_DATA",
        "START_LOST_MODE",
        "STOP_LOST_MODE",
        "ADD_ESIM",
        "REMOVE_ESIM",
        "REQUEST_DEVICE_INFO",
        "WIPE",
    ]
    userName: str
    wipeParams: WipeParams

@typing.type_check_only
class CommonCriteriaModeInfo(typing_extensions.TypedDict, total=False):
    commonCriteriaModeStatus: typing_extensions.Literal[
        "COMMON_CRITERIA_MODE_STATUS_UNKNOWN",
        "COMMON_CRITERIA_MODE_DISABLED",
        "COMMON_CRITERIA_MODE_ENABLED",
    ]
    policySignatureVerificationStatus: typing_extensions.Literal[
        "POLICY_SIGNATURE_VERIFICATION_STATUS_UNSPECIFIED",
        "POLICY_SIGNATURE_VERIFICATION_DISABLED",
        "POLICY_SIGNATURE_VERIFICATION_SUCCEEDED",
        "POLICY_SIGNATURE_VERIFICATION_NOT_SUPPORTED",
        "POLICY_SIGNATURE_VERIFICATION_FAILED",
    ]

@typing.type_check_only
class ComplianceRule(typing_extensions.TypedDict, total=False):
    apiLevelCondition: ApiLevelCondition
    disableApps: bool
    nonComplianceDetailCondition: NonComplianceDetailCondition
    packageNamesToDisable: _list[str]

@typing.type_check_only
class ConnectEvent(typing_extensions.TypedDict, total=False):
    destinationIpAddress: str
    destinationPort: int
    packageName: str

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
class ContentProviderEndpoint(typing_extensions.TypedDict, total=False):
    packageName: str
    signingCertsSha256: _list[str]
    uri: str

@typing.type_check_only
class CrossProfilePolicies(typing_extensions.TypedDict, total=False):
    crossProfileAppFunctions: typing_extensions.Literal[
        "CROSS_PROFILE_APP_FUNCTIONS_UNSPECIFIED",
        "CROSS_PROFILE_APP_FUNCTIONS_DISALLOWED",
        "CROSS_PROFILE_APP_FUNCTIONS_ALLOWED",
    ]
    crossProfileCopyPaste: typing_extensions.Literal[
        "CROSS_PROFILE_COPY_PASTE_UNSPECIFIED",
        "COPY_FROM_WORK_TO_PERSONAL_DISALLOWED",
        "CROSS_PROFILE_COPY_PASTE_ALLOWED",
    ]
    crossProfileDataSharing: typing_extensions.Literal[
        "CROSS_PROFILE_DATA_SHARING_UNSPECIFIED",
        "CROSS_PROFILE_DATA_SHARING_DISALLOWED",
        "DATA_SHARING_FROM_WORK_TO_PERSONAL_DISALLOWED",
        "CROSS_PROFILE_DATA_SHARING_ALLOWED",
    ]
    exemptionsToShowWorkContactsInPersonalProfile: PackageNameList
    showWorkContactsInPersonalProfile: typing_extensions.Literal[
        "SHOW_WORK_CONTACTS_IN_PERSONAL_PROFILE_UNSPECIFIED",
        "SHOW_WORK_CONTACTS_IN_PERSONAL_PROFILE_DISALLOWED",
        "SHOW_WORK_CONTACTS_IN_PERSONAL_PROFILE_ALLOWED",
        "SHOW_WORK_CONTACTS_IN_PERSONAL_PROFILE_DISALLOWED_EXCEPT_SYSTEM",
    ]
    workProfileWidgetsDefault: typing_extensions.Literal[
        "WORK_PROFILE_WIDGETS_DEFAULT_UNSPECIFIED",
        "WORK_PROFILE_WIDGETS_DEFAULT_ALLOWED",
        "WORK_PROFILE_WIDGETS_DEFAULT_DISALLOWED",
    ]

@typing.type_check_only
class CryptoSelfTestCompletedEvent(typing_extensions.TypedDict, total=False):
    success: bool

@typing.type_check_only
class CustomAppConfig(typing_extensions.TypedDict, total=False):
    userUninstallSettings: typing_extensions.Literal[
        "USER_UNINSTALL_SETTINGS_UNSPECIFIED",
        "DISALLOW_UNINSTALL_BY_USER",
        "ALLOW_UNINSTALL_BY_USER",
    ]

@typing.type_check_only
class Date(typing_extensions.TypedDict, total=False):
    day: int
    month: int
    year: int

@typing.type_check_only
class DefaultApplication(typing_extensions.TypedDict, total=False):
    packageName: str

@typing.type_check_only
class DefaultApplicationContext(typing_extensions.TypedDict, total=False):
    defaultApplicationScope: typing_extensions.Literal[
        "DEFAULT_APPLICATION_SCOPE_UNSPECIFIED",
        "SCOPE_FULLY_MANAGED",
        "SCOPE_WORK_PROFILE",
        "SCOPE_PERSONAL_PROFILE",
    ]

@typing.type_check_only
class DefaultApplicationInfo(typing_extensions.TypedDict, total=False):
    defaultApplicationSettingAttempts: _list[DefaultApplicationSettingAttempt]
    defaultApplicationType: typing_extensions.Literal[
        "DEFAULT_APPLICATION_TYPE_UNSPECIFIED",
        "DEFAULT_ASSISTANT",
        "DEFAULT_BROWSER",
        "DEFAULT_CALL_REDIRECTION",
        "DEFAULT_CALL_SCREENING",
        "DEFAULT_DIALER",
        "DEFAULT_HOME",
        "DEFAULT_SMS",
        "DEFAULT_WALLET",
    ]
    packageName: str

@typing.type_check_only
class DefaultApplicationSetting(typing_extensions.TypedDict, total=False):
    defaultApplicationScopes: _list[
        typing_extensions.Literal[
            "DEFAULT_APPLICATION_SCOPE_UNSPECIFIED",
            "SCOPE_FULLY_MANAGED",
            "SCOPE_WORK_PROFILE",
            "SCOPE_PERSONAL_PROFILE",
        ]
    ]
    defaultApplicationType: typing_extensions.Literal[
        "DEFAULT_APPLICATION_TYPE_UNSPECIFIED",
        "DEFAULT_ASSISTANT",
        "DEFAULT_BROWSER",
        "DEFAULT_CALL_REDIRECTION",
        "DEFAULT_CALL_SCREENING",
        "DEFAULT_DIALER",
        "DEFAULT_HOME",
        "DEFAULT_SMS",
        "DEFAULT_WALLET",
    ]
    defaultApplications: _list[DefaultApplication]

@typing.type_check_only
class DefaultApplicationSettingAttempt(typing_extensions.TypedDict, total=False):
    attemptOutcome: typing_extensions.Literal[
        "ATTEMPT_OUTCOME_UNSPECIFIED",
        "SUCCESS",
        "APP_NOT_INSTALLED",
        "APP_SIGNING_CERT_MISMATCH",
        "OTHER_FAILURE",
    ]
    packageName: str

@typing.type_check_only
class Device(typing_extensions.TypedDict, total=False):
    apiLevel: int
    applicationReports: _list[ApplicationReport]
    appliedPasswordPolicies: _list[PasswordRequirements]
    appliedPolicyName: str
    appliedPolicyVersion: str
    appliedState: typing_extensions.Literal[
        "DEVICE_STATE_UNSPECIFIED",
        "ACTIVE",
        "DISABLED",
        "DELETED",
        "PROVISIONING",
        "LOST",
        "PREPARING_FOR_MIGRATION",
        "DEACTIVATED_BY_DEVICE_FINANCE",
    ]
    commonCriteriaModeInfo: CommonCriteriaModeInfo
    defaultApplicationInfo: _list[DefaultApplicationInfo]
    deviceSettings: DeviceSettings
    disabledReason: UserFacingMessage
    displays: _list[Display]
    dpcMigrationInfo: DpcMigrationInfo
    enrollmentTime: str
    enrollmentTokenData: str
    enrollmentTokenName: str
    hardwareInfo: HardwareInfo
    hardwareStatusSamples: _list[HardwareStatus]
    lastPolicyComplianceReportTime: str
    lastPolicySyncTime: str
    lastStatusReportTime: str
    managementMode: typing_extensions.Literal[
        "MANAGEMENT_MODE_UNSPECIFIED", "DEVICE_OWNER", "PROFILE_OWNER"
    ]
    memoryEvents: _list[MemoryEvent]
    memoryInfo: MemoryInfo
    name: str
    networkInfo: NetworkInfo
    nonComplianceDetails: _list[NonComplianceDetail]
    ownership: typing_extensions.Literal[
        "OWNERSHIP_UNSPECIFIED", "COMPANY_OWNED", "PERSONALLY_OWNED"
    ]
    policyCompliant: bool
    policyName: str
    powerManagementEvents: _list[PowerManagementEvent]
    previousDeviceNames: _list[str]
    securityPosture: SecurityPosture
    softwareInfo: SoftwareInfo
    state: typing_extensions.Literal[
        "DEVICE_STATE_UNSPECIFIED",
        "ACTIVE",
        "DISABLED",
        "DELETED",
        "PROVISIONING",
        "LOST",
        "PREPARING_FOR_MIGRATION",
        "DEACTIVATED_BY_DEVICE_FINANCE",
    ]
    systemProperties: dict[str, typing.Any]
    user: User
    userName: str

@typing.type_check_only
class DeviceConnectivityManagement(typing_extensions.TypedDict, total=False):
    apnPolicy: ApnPolicy
    bluetoothSharing: typing_extensions.Literal[
        "BLUETOOTH_SHARING_UNSPECIFIED",
        "BLUETOOTH_SHARING_ALLOWED",
        "BLUETOOTH_SHARING_DISALLOWED",
    ]
    configureWifi: typing_extensions.Literal[
        "CONFIGURE_WIFI_UNSPECIFIED",
        "ALLOW_CONFIGURING_WIFI",
        "DISALLOW_ADD_WIFI_CONFIG",
        "DISALLOW_CONFIGURING_WIFI",
    ]
    preferentialNetworkServiceSettings: PreferentialNetworkServiceSettings
    tetheringSettings: typing_extensions.Literal[
        "TETHERING_SETTINGS_UNSPECIFIED",
        "ALLOW_ALL_TETHERING",
        "DISALLOW_WIFI_TETHERING",
        "DISALLOW_ALL_TETHERING",
    ]
    usbDataAccess: typing_extensions.Literal[
        "USB_DATA_ACCESS_UNSPECIFIED",
        "ALLOW_USB_DATA_TRANSFER",
        "DISALLOW_USB_FILE_TRANSFER",
        "DISALLOW_USB_DATA_TRANSFER",
    ]
    wifiDirectSettings: typing_extensions.Literal[
        "WIFI_DIRECT_SETTINGS_UNSPECIFIED", "ALLOW_WIFI_DIRECT", "DISALLOW_WIFI_DIRECT"
    ]
    wifiRoamingPolicy: WifiRoamingPolicy
    wifiSsidPolicy: WifiSsidPolicy

@typing.type_check_only
class DeviceRadioState(typing_extensions.TypedDict, total=False):
    airplaneModeState: typing_extensions.Literal[
        "AIRPLANE_MODE_STATE_UNSPECIFIED",
        "AIRPLANE_MODE_USER_CHOICE",
        "AIRPLANE_MODE_DISABLED",
    ]
    cellularTwoGState: typing_extensions.Literal[
        "CELLULAR_TWO_G_STATE_UNSPECIFIED",
        "CELLULAR_TWO_G_USER_CHOICE",
        "CELLULAR_TWO_G_DISABLED",
    ]
    minimumWifiSecurityLevel: typing_extensions.Literal[
        "MINIMUM_WIFI_SECURITY_LEVEL_UNSPECIFIED",
        "OPEN_NETWORK_SECURITY",
        "PERSONAL_NETWORK_SECURITY",
        "ENTERPRISE_NETWORK_SECURITY",
        "ENTERPRISE_BIT192_NETWORK_SECURITY",
    ]
    ultraWidebandState: typing_extensions.Literal[
        "ULTRA_WIDEBAND_STATE_UNSPECIFIED",
        "ULTRA_WIDEBAND_USER_CHOICE",
        "ULTRA_WIDEBAND_DISABLED",
    ]
    userInitiatedAddEsimSettings: typing_extensions.Literal[
        "USER_INITIATED_ADD_ESIM_SETTINGS_UNSPECIFIED",
        "USER_INITIATED_ADD_ESIM_ALLOWED",
        "USER_INITIATED_ADD_ESIM_DISALLOWED",
    ]
    wifiState: typing_extensions.Literal[
        "WIFI_STATE_UNSPECIFIED",
        "WIFI_STATE_USER_CHOICE",
        "WIFI_ENABLED",
        "WIFI_DISABLED",
    ]

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
class DisplaySettings(typing_extensions.TypedDict, total=False):
    screenBrightnessSettings: ScreenBrightnessSettings
    screenTimeoutSettings: ScreenTimeoutSettings

@typing.type_check_only
class DnsEvent(typing_extensions.TypedDict, total=False):
    hostname: str
    ipAddresses: _list[str]
    packageName: str
    totalIpAddressesReturned: str

@typing.type_check_only
class DpcMigrationInfo(typing_extensions.TypedDict, total=False):
    additionalData: str
    previousDpc: str

@typing.type_check_only
class Eid(typing_extensions.TypedDict, total=False):
    eid: str

@typing.type_check_only
class EidInfo(typing_extensions.TypedDict, total=False):
    eids: _list[Eid]

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class EnrollmentCompleteEvent(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class EnrollmentToken(typing_extensions.TypedDict, total=False):
    additionalData: str
    allowPersonalUsage: typing_extensions.Literal[
        "ALLOW_PERSONAL_USAGE_UNSPECIFIED",
        "PERSONAL_USAGE_ALLOWED",
        "PERSONAL_USAGE_DISALLOWED",
        "PERSONAL_USAGE_DISALLOWED_USERLESS",
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
    enabledNotificationTypes: _list[
        typing_extensions.Literal[
            "NOTIFICATION_TYPE_UNSPECIFIED",
            "ENROLLMENT",
            "COMPLIANCE_REPORT",
            "STATUS_REPORT",
            "COMMAND",
            "USAGE_LOGS",
            "ENTERPRISE_UPGRADE",
        ]
    ]
    enterpriseDisplayName: str
    enterpriseType: typing_extensions.Literal[
        "ENTERPRISE_TYPE_UNSPECIFIED",
        "MANAGED_GOOGLE_DOMAIN",
        "MANAGED_GOOGLE_PLAY_ACCOUNTS_ENTERPRISE",
    ]
    googleAuthenticationSettings: GoogleAuthenticationSettings
    logo: ExternalData
    managedGoogleDomainType: typing_extensions.Literal[
        "MANAGED_GOOGLE_DOMAIN_TYPE_UNSPECIFIED", "TYPE_TEAM", "TYPE_DOMAIN"
    ]
    managedGooglePlayAccountsEnterpriseType: typing_extensions.Literal[
        "MANAGED_GOOGLE_PLAY_ACCOUNTS_ENTERPRISE_TYPE_UNSPECIFIED",
        "CUSTOMER_MANAGED",
        "EMM_MANAGED",
    ]
    name: str
    primaryColor: int
    pubsubTopic: str
    signinDetails: _list[SigninDetail]
    termsAndConditions: _list[TermsAndConditions]

@typing.type_check_only
class EnterpriseUpgradeEvent(typing_extensions.TypedDict, total=False):
    enterprise: str
    upgradeState: typing_extensions.Literal[
        "UPGRADE_STATE_UNSPECIFIED", "UPGRADE_STATE_SUCCEEDED"
    ]

@typing.type_check_only
class EsimCommandStatus(typing_extensions.TypedDict, total=False):
    esimInfo: EsimInfo
    internalErrorDetails: InternalErrorDetails
    status: typing_extensions.Literal[
        "STATUS_UNSPECIFIED",
        "SUCCESS",
        "IN_PROGRESS",
        "PENDING_USER_ACTION",
        "ERROR_SETUP_IN_PROGRESS",
        "ERROR_USER_DENIED",
        "INTERNAL_ERROR",
        "ERROR_ICC_ID_NOT_FOUND",
        "ERROR_MULTIPLE_ACTIVE_ESIMS_NO_AVAILABLE_SLOT",
    ]

@typing.type_check_only
class EsimInfo(typing_extensions.TypedDict, total=False):
    iccId: str

@typing.type_check_only
class EuiccChipInfo(typing_extensions.TypedDict, total=False):
    eid: str

@typing.type_check_only
class ExtensionConfig(typing_extensions.TypedDict, total=False):
    notificationReceiver: str
    signingKeyFingerprintsSha256: _list[str]

@typing.type_check_only
class ExternalData(typing_extensions.TypedDict, total=False):
    sha256Hash: str
    url: str

@typing.type_check_only
class FilePulledEvent(typing_extensions.TypedDict, total=False):
    filePath: str

@typing.type_check_only
class FilePushedEvent(typing_extensions.TypedDict, total=False):
    filePath: str

@typing.type_check_only
class FreezePeriod(typing_extensions.TypedDict, total=False):
    endDate: Date
    startDate: Date

@typing.type_check_only
class GenerateEnterpriseUpgradeUrlRequest(typing_extensions.TypedDict, total=False):
    adminEmail: str
    allowedDomains: _list[str]

@typing.type_check_only
class GenerateEnterpriseUpgradeUrlResponse(typing_extensions.TypedDict, total=False):
    url: str

@typing.type_check_only
class GoogleAuthenticationSettings(typing_extensions.TypedDict, total=False):
    googleAuthenticationRequired: typing_extensions.Literal[
        "GOOGLE_AUTHENTICATION_REQUIRED_UNSPECIFIED", "NOT_REQUIRED", "REQUIRED"
    ]

@typing.type_check_only
class HardwareInfo(typing_extensions.TypedDict, total=False):
    batteryShutdownTemperatures: _list[float]
    batteryThrottlingTemperatures: _list[float]
    brand: str
    cpuShutdownTemperatures: _list[float]
    cpuThrottlingTemperatures: _list[float]
    deviceBasebandVersion: str
    enterpriseSpecificId: str
    euiccChipInfo: _list[EuiccChipInfo]
    gpuShutdownTemperatures: _list[float]
    gpuThrottlingTemperatures: _list[float]
    hardware: str
    manufacturer: str
    model: str
    serialNumber: str
    skinShutdownTemperatures: _list[float]
    skinThrottlingTemperatures: _list[float]

@typing.type_check_only
class HardwareStatus(typing_extensions.TypedDict, total=False):
    batteryTemperatures: _list[float]
    cpuTemperatures: _list[float]
    cpuUsages: _list[float]
    createTime: str
    fanSpeeds: _list[float]
    gpuTemperatures: _list[float]
    skinTemperatures: _list[float]

@typing.type_check_only
class InstallConstraint(typing_extensions.TypedDict, total=False):
    chargingConstraint: typing_extensions.Literal[
        "CHARGING_CONSTRAINT_UNSPECIFIED",
        "CHARGING_NOT_REQUIRED",
        "INSTALL_ONLY_WHEN_CHARGING",
    ]
    deviceIdleConstraint: typing_extensions.Literal[
        "DEVICE_IDLE_CONSTRAINT_UNSPECIFIED",
        "DEVICE_IDLE_NOT_REQUIRED",
        "INSTALL_ONLY_WHEN_DEVICE_IDLE",
    ]
    networkTypeConstraint: typing_extensions.Literal[
        "NETWORK_TYPE_CONSTRAINT_UNSPECIFIED",
        "INSTALL_ON_ANY_NETWORK",
        "INSTALL_ONLY_ON_UNMETERED_NETWORK",
    ]

@typing.type_check_only
class InternalErrorDetails(typing_extensions.TypedDict, total=False):
    errorCode: str
    errorCodeDetail: typing_extensions.Literal[
        "ERROR_CODE_DETAIL_UNSPECIFIED",
        "ERROR_TIME_OUT",
        "ERROR_EUICC_MISSING",
        "ERROR_UNSUPPORTED_VERSION",
        "ERROR_ADDRESS_MISSING",
        "ERROR_INVALID_CONFIRMATION_CODE",
        "ERROR_CERTIFICATE_ERROR",
        "ERROR_NO_PROFILES_AVAILABLE",
        "ERROR_CONNECTION_ERROR",
        "ERROR_INVALID_RESPONSE",
        "ERROR_CARRIER_LOCKED",
        "ERROR_DISALLOWED_BY_PPR",
        "ERROR_INVALID_ACTIVATION_CODE",
        "ERROR_INCOMPATIBLE_CARRIER",
        "ERROR_OPERATION_BUSY",
        "ERROR_INSTALL_PROFILE",
        "ERROR_EUICC_INSUFFICIENT_MEMORY",
        "ERROR_INVALID_PORT",
        "ERROR_SIM_MISSING",
    ]
    operationCode: str
    operationCodeDetail: typing_extensions.Literal[
        "OPERATION_CODE_DETAIL_UNSPECIFIED",
        "OPERATION_SYSTEM",
        "OPERATION_SIM_SLOT",
        "OPERATION_EUICC_CARD",
        "OPERATION_SMDX",
        "OPERATION_SWITCH",
        "OPERATION_DOWNLOAD",
        "OPERATION_METADATA",
        "OPERATION_EUICC_GSMA",
        "OPERATION_APDU",
        "OPERATION_SMDX_SUBJECT_REASON_CODE",
        "OPERATION_HTTP",
    ]

@typing.type_check_only
class IssueCommandResponse(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class KeyDestructionEvent(typing_extensions.TypedDict, total=False):
    applicationUid: int
    keyAlias: str
    success: bool

@typing.type_check_only
class KeyGeneratedEvent(typing_extensions.TypedDict, total=False):
    applicationUid: int
    keyAlias: str
    success: bool

@typing.type_check_only
class KeyImportEvent(typing_extensions.TypedDict, total=False):
    applicationUid: int
    keyAlias: str
    success: bool

@typing.type_check_only
class KeyIntegrityViolationEvent(typing_extensions.TypedDict, total=False):
    applicationUid: int
    keyAlias: str

@typing.type_check_only
class KeyedAppState(typing_extensions.TypedDict, total=False):
    createTime: str
    data: str
    key: str
    lastUpdateTime: str
    message: str
    severity: typing_extensions.Literal["SEVERITY_UNSPECIFIED", "INFO", "ERROR"]

@typing.type_check_only
class KeyguardDismissAuthAttemptEvent(typing_extensions.TypedDict, total=False):
    strongAuthMethodUsed: bool
    success: bool

@typing.type_check_only
class KeyguardDismissedEvent(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class KeyguardSecuredEvent(typing_extensions.TypedDict, total=False): ...

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
    devices: _list[Device]
    nextPageToken: str

@typing.type_check_only
class ListEnrollmentTokensResponse(typing_extensions.TypedDict, total=False):
    enrollmentTokens: _list[EnrollmentToken]
    nextPageToken: str

@typing.type_check_only
class ListEnterprisesResponse(typing_extensions.TypedDict, total=False):
    enterprises: _list[Enterprise]
    nextPageToken: str

@typing.type_check_only
class ListMigrationTokensResponse(typing_extensions.TypedDict, total=False):
    migrationTokens: _list[MigrationToken]
    nextPageToken: str

@typing.type_check_only
class ListOperationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    operations: _list[Operation]
    unreachable: _list[str]

@typing.type_check_only
class ListPoliciesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    policies: _list[Policy]

@typing.type_check_only
class ListWebAppsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    webApps: _list[WebApp]

@typing.type_check_only
class Location(typing_extensions.TypedDict, total=False):
    latitude: float
    longitude: float

@typing.type_check_only
class LogBufferSizeCriticalEvent(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class LoggingStartedEvent(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class LoggingStoppedEvent(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class LostModeLocationEvent(typing_extensions.TypedDict, total=False):
    batteryLevel: int
    location: Location

@typing.type_check_only
class LostModeOutgoingPhoneCallEvent(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class ManagedConfigurationTemplate(typing_extensions.TypedDict, total=False):
    configurationVariables: dict[str, typing.Any]
    templateId: str

@typing.type_check_only
class ManagedProperty(typing_extensions.TypedDict, total=False):
    defaultValue: typing.Any
    description: str
    entries: _list[ManagedPropertyEntry]
    key: str
    nestedProperties: _list[ManagedProperty]
    title: str
    type: typing_extensions.Literal[
        "MANAGED_PROPERTY_TYPE_UNSPECIFIED",
        "BOOL",
        "STRING",
        "INTEGER",
        "CHOICE",
        "MULTISELECT",
        "HIDDEN",
        "BUNDLE",
        "BUNDLE_ARRAY",
    ]

@typing.type_check_only
class ManagedPropertyEntry(typing_extensions.TypedDict, total=False):
    name: str
    value: str

@typing.type_check_only
class MediaMountEvent(typing_extensions.TypedDict, total=False):
    mountPoint: str
    volumeLabel: str

@typing.type_check_only
class MediaUnmountEvent(typing_extensions.TypedDict, total=False):
    mountPoint: str
    volumeLabel: str

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
class MigrationToken(typing_extensions.TypedDict, total=False):
    additionalData: str
    createTime: str
    device: str
    deviceId: str
    expireTime: str
    managementMode: typing_extensions.Literal[
        "MANAGEMENT_MODE_UNSPECIFIED",
        "WORK_PROFILE_PERSONALLY_OWNED",
        "WORK_PROFILE_COMPANY_OWNED",
        "FULLY_MANAGED",
    ]
    name: str
    policy: str
    ttl: str
    userId: str
    value: str

@typing.type_check_only
class ModifyPolicyApplicationsRequest(typing_extensions.TypedDict, total=False):
    changes: _list[ApplicationPolicyChange]

@typing.type_check_only
class ModifyPolicyApplicationsResponse(typing_extensions.TypedDict, total=False):
    policy: Policy

@typing.type_check_only
class NetworkInfo(typing_extensions.TypedDict, total=False):
    imei: str
    meid: str
    networkOperatorName: str
    telephonyInfos: _list[TelephonyInfo]
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
        "NETWORK_ERROR_UNRELIABLE_CONNECTION",
        "INSUFFICIENT_STORAGE",
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
        "DEVICE_INCOMPATIBLE",
        "APP_SIGNING_CERT_MISMATCH",
        "PROJECT_NOT_PERMITTED",
    ]
    packageName: str
    settingName: str
    specificNonComplianceContext: SpecificNonComplianceContext
    specificNonComplianceReason: typing_extensions.Literal[
        "SPECIFIC_NON_COMPLIANCE_REASON_UNSPECIFIED",
        "PASSWORD_POLICIES_USER_CREDENTIALS_CONFIRMATION_REQUIRED",
        "PASSWORD_POLICIES_PASSWORD_EXPIRED",
        "PASSWORD_POLICIES_PASSWORD_NOT_SUFFICIENT",
        "ONC_WIFI_INVALID_VALUE",
        "ONC_WIFI_API_LEVEL",
        "ONC_WIFI_INVALID_ENTERPRISE_CONFIG",
        "ONC_WIFI_USER_SHOULD_REMOVE_NETWORK",
        "ONC_WIFI_KEY_PAIR_ALIAS_NOT_CORRESPONDING_TO_EXISTING_KEY",
        "PERMISSIBLE_USAGE_RESTRICTION",
        "REQUIRED_ACCOUNT_NOT_IN_ENTERPRISE",
        "NEW_ACCOUNT_NOT_IN_ENTERPRISE",
        "DEFAULT_APPLICATION_SETTING_UNSUPPORTED_SCOPES",
        "DEFAULT_APPLICATION_SETTING_FAILED_FOR_SCOPE",
        "PRIVATE_DNS_HOST_NOT_SERVING",
    ]

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
        "DEVICE_INCOMPATIBLE",
        "APP_SIGNING_CERT_MISMATCH",
        "PROJECT_NOT_PERMITTED",
    ]
    packageName: str
    settingName: str

@typing.type_check_only
class OncCertificateProvider(typing_extensions.TypedDict, total=False):
    certificateReferences: _list[str]
    contentProviderEndpoint: ContentProviderEndpoint

@typing.type_check_only
class OncWifiContext(typing_extensions.TypedDict, total=False):
    wifiGuid: str

@typing.type_check_only
class Operation(typing_extensions.TypedDict, total=False):
    done: bool
    error: Status
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class OsShutdownEvent(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class OsStartupEvent(typing_extensions.TypedDict, total=False):
    verifiedBootState: typing_extensions.Literal[
        "VERIFIED_BOOT_STATE_UNSPECIFIED", "GREEN", "YELLOW", "ORANGE"
    ]
    verityMode: typing_extensions.Literal[
        "DM_VERITY_MODE_UNSPECIFIED", "ENFORCING", "IO_ERROR", "DISABLED"
    ]

@typing.type_check_only
class PackageNameList(typing_extensions.TypedDict, total=False):
    packageNames: _list[str]

@typing.type_check_only
class PasswordPoliciesContext(typing_extensions.TypedDict, total=False):
    passwordPolicyScope: typing_extensions.Literal[
        "SCOPE_UNSPECIFIED", "SCOPE_DEVICE", "SCOPE_PROFILE"
    ]

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
        "COMPLEXITY_LOW",
        "COMPLEXITY_MEDIUM",
        "COMPLEXITY_HIGH",
    ]
    passwordScope: typing_extensions.Literal[
        "SCOPE_UNSPECIFIED", "SCOPE_DEVICE", "SCOPE_PROFILE"
    ]
    requirePasswordUnlock: typing_extensions.Literal[
        "REQUIRE_PASSWORD_UNLOCK_UNSPECIFIED",
        "USE_DEFAULT_DEVICE_TIMEOUT",
        "REQUIRE_EVERY_DAY",
    ]
    unifiedLockSettings: typing_extensions.Literal[
        "UNIFIED_LOCK_SETTINGS_UNSPECIFIED",
        "ALLOW_UNIFIED_WORK_AND_PERSONAL_LOCK",
        "REQUIRE_SEPARATE_WORK_LOCK",
    ]

@typing.type_check_only
class PerAppResult(typing_extensions.TypedDict, total=False):
    clearingResult: typing_extensions.Literal[
        "CLEARING_RESULT_UNSPECIFIED",
        "SUCCESS",
        "APP_NOT_FOUND",
        "APP_PROTECTED",
        "API_LEVEL",
    ]

@typing.type_check_only
class PermissionGrant(typing_extensions.TypedDict, total=False):
    permission: str
    policy: typing_extensions.Literal[
        "PERMISSION_POLICY_UNSPECIFIED", "PROMPT", "GRANT", "DENY"
    ]

@typing.type_check_only
class PersistentPreferredActivity(typing_extensions.TypedDict, total=False):
    actions: _list[str]
    categories: _list[str]
    receiverActivity: str

@typing.type_check_only
class PersonalApplicationPolicy(typing_extensions.TypedDict, total=False):
    installType: typing_extensions.Literal[
        "INSTALL_TYPE_UNSPECIFIED", "BLOCKED", "AVAILABLE"
    ]
    packageName: str

@typing.type_check_only
class PersonalUsagePolicies(typing_extensions.TypedDict, total=False):
    accountTypesWithManagementDisabled: _list[str]
    bluetoothSharing: typing_extensions.Literal[
        "BLUETOOTH_SHARING_UNSPECIFIED",
        "BLUETOOTH_SHARING_ALLOWED",
        "BLUETOOTH_SHARING_DISALLOWED",
    ]
    cameraDisabled: bool
    maxDaysWithWorkOff: int
    personalApplications: _list[PersonalApplicationPolicy]
    personalPlayStoreMode: typing_extensions.Literal[
        "PLAY_STORE_MODE_UNSPECIFIED", "BLACKLIST", "BLOCKLIST", "ALLOWLIST"
    ]
    privateSpacePolicy: typing_extensions.Literal[
        "PRIVATE_SPACE_POLICY_UNSPECIFIED",
        "PRIVATE_SPACE_ALLOWED",
        "PRIVATE_SPACE_DISALLOWED",
    ]
    screenCaptureDisabled: bool

@typing.type_check_only
class Policy(typing_extensions.TypedDict, total=False):
    accountTypesWithManagementDisabled: _list[str]
    addUserDisabled: bool
    adjustVolumeDisabled: bool
    advancedSecurityOverrides: AdvancedSecurityOverrides
    alwaysOnVpnPackage: AlwaysOnVpnPackage
    androidDevicePolicyTracks: _list[
        typing_extensions.Literal["APP_TRACK_UNSPECIFIED", "PRODUCTION", "BETA"]
    ]
    appAutoUpdatePolicy: typing_extensions.Literal[
        "APP_AUTO_UPDATE_POLICY_UNSPECIFIED",
        "CHOICE_TO_THE_USER",
        "NEVER",
        "WIFI_ONLY",
        "ALWAYS",
    ]
    appFunctions: typing_extensions.Literal[
        "APP_FUNCTIONS_UNSPECIFIED", "APP_FUNCTIONS_DISALLOWED", "APP_FUNCTIONS_ALLOWED"
    ]
    applications: _list[ApplicationPolicy]
    assistContentPolicy: typing_extensions.Literal[
        "ASSIST_CONTENT_POLICY_UNSPECIFIED",
        "ASSIST_CONTENT_DISALLOWED",
        "ASSIST_CONTENT_ALLOWED",
    ]
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
    cameraAccess: typing_extensions.Literal[
        "CAMERA_ACCESS_UNSPECIFIED",
        "CAMERA_ACCESS_USER_CHOICE",
        "CAMERA_ACCESS_DISABLED",
        "CAMERA_ACCESS_ENFORCED",
    ]
    cameraDisabled: bool
    cellBroadcastsConfigDisabled: bool
    choosePrivateKeyRules: _list[ChoosePrivateKeyRule]
    complianceRules: _list[ComplianceRule]
    createWindowsDisabled: bool
    credentialProviderPolicyDefault: typing_extensions.Literal[
        "CREDENTIAL_PROVIDER_POLICY_DEFAULT_UNSPECIFIED",
        "CREDENTIAL_PROVIDER_DEFAULT_DISALLOWED",
        "CREDENTIAL_PROVIDER_DEFAULT_DISALLOWED_EXCEPT_SYSTEM",
    ]
    credentialsConfigDisabled: bool
    crossProfilePolicies: CrossProfilePolicies
    dataRoamingDisabled: bool
    debuggingFeaturesAllowed: bool
    defaultApplicationSettings: _list[DefaultApplicationSetting]
    defaultPermissionPolicy: typing_extensions.Literal[
        "PERMISSION_POLICY_UNSPECIFIED", "PROMPT", "GRANT", "DENY"
    ]
    deviceConnectivityManagement: DeviceConnectivityManagement
    deviceOwnerLockScreenInfo: UserFacingMessage
    deviceRadioState: DeviceRadioState
    displaySettings: DisplaySettings
    encryptionPolicy: typing_extensions.Literal[
        "ENCRYPTION_POLICY_UNSPECIFIED",
        "ENABLED_WITHOUT_PASSWORD",
        "ENABLED_WITH_PASSWORD",
    ]
    ensureVerifyAppsEnabled: bool
    enterpriseDisplayNameVisibility: typing_extensions.Literal[
        "ENTERPRISE_DISPLAY_NAME_VISIBILITY_UNSPECIFIED",
        "ENTERPRISE_DISPLAY_NAME_VISIBLE",
        "ENTERPRISE_DISPLAY_NAME_HIDDEN",
    ]
    factoryResetDisabled: bool
    frpAdminEmails: _list[str]
    funDisabled: bool
    installAppsDisabled: bool
    installUnknownSourcesAllowed: bool
    keyguardDisabled: bool
    keyguardDisabledFeatures: _list[
        typing_extensions.Literal[
            "KEYGUARD_DISABLED_FEATURE_UNSPECIFIED",
            "CAMERA",
            "NOTIFICATIONS",
            "UNREDACTED_NOTIFICATIONS",
            "TRUST_AGENTS",
            "DISABLE_FINGERPRINT",
            "DISABLE_REMOTE_INPUT",
            "FACE",
            "IRIS",
            "BIOMETRICS",
            "SHORTCUTS",
            "ALL_FEATURES",
        ]
    ]
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
    microphoneAccess: typing_extensions.Literal[
        "MICROPHONE_ACCESS_UNSPECIFIED",
        "MICROPHONE_ACCESS_USER_CHOICE",
        "MICROPHONE_ACCESS_DISABLED",
        "MICROPHONE_ACCESS_ENFORCED",
    ]
    minimumApiLevel: int
    mobileNetworksConfigDisabled: bool
    modifyAccountsDisabled: bool
    mountPhysicalMediaDisabled: bool
    name: str
    networkEscapeHatchEnabled: bool
    networkResetDisabled: bool
    oncCertificateProviders: _list[OncCertificateProvider]
    openNetworkConfiguration: dict[str, typing.Any]
    outgoingBeamDisabled: bool
    outgoingCallsDisabled: bool
    passwordPolicies: _list[PasswordRequirements]
    passwordRequirements: PasswordRequirements
    permissionGrants: _list[PermissionGrant]
    permittedAccessibilityServices: PackageNameList
    permittedInputMethods: PackageNameList
    persistentPreferredActivities: _list[PersistentPreferredActivity]
    personalUsagePolicies: PersonalUsagePolicies
    playStoreMode: typing_extensions.Literal[
        "PLAY_STORE_MODE_UNSPECIFIED", "WHITELIST", "BLACKLIST"
    ]
    policyEnforcementRules: _list[PolicyEnforcementRule]
    preferentialNetworkService: typing_extensions.Literal[
        "PREFERENTIAL_NETWORK_SERVICE_UNSPECIFIED",
        "PREFERENTIAL_NETWORK_SERVICE_DISABLED",
        "PREFERENTIAL_NETWORK_SERVICE_ENABLED",
    ]
    printingPolicy: typing_extensions.Literal[
        "PRINTING_POLICY_UNSPECIFIED", "PRINTING_DISALLOWED", "PRINTING_ALLOWED"
    ]
    privateKeySelectionEnabled: bool
    recommendedGlobalProxy: ProxyInfo
    removeUserDisabled: bool
    safeBootDisabled: bool
    screenCaptureDisabled: bool
    setUserIconDisabled: bool
    setWallpaperDisabled: bool
    setupActions: _list[SetupAction]
    shareLocationDisabled: bool
    shortSupportMessage: UserFacingMessage
    skipFirstUseHintsEnabled: bool
    smsDisabled: bool
    statusBarDisabled: bool
    statusReportingSettings: StatusReportingSettings
    stayOnPluggedModes: _list[
        typing_extensions.Literal[
            "BATTERY_PLUGGED_MODE_UNSPECIFIED", "AC", "USB", "WIRELESS"
        ]
    ]
    systemUpdate: SystemUpdate
    tetheringConfigDisabled: bool
    uninstallAppsDisabled: bool
    unmuteMicrophoneDisabled: bool
    usageLog: UsageLog
    usbFileTransferDisabled: bool
    usbMassStorageEnabled: bool
    version: str
    vpnConfigDisabled: bool
    wifiConfigDisabled: bool
    wifiConfigsLockdownEnabled: bool
    wipeDataFlags: _list[
        typing_extensions.Literal["WIPE_DATA_FLAG_UNSPECIFIED", "WIPE_ESIMS"]
    ]
    workAccountSetupConfig: WorkAccountSetupConfig

@typing.type_check_only
class PolicyEnforcementRule(typing_extensions.TypedDict, total=False):
    blockAction: BlockAction
    settingName: str
    wipeAction: WipeAction

@typing.type_check_only
class PostureDetail(typing_extensions.TypedDict, total=False):
    advice: _list[UserFacingMessage]
    securityRisk: typing_extensions.Literal[
        "SECURITY_RISK_UNSPECIFIED",
        "UNKNOWN_OS",
        "COMPROMISED_OS",
        "HARDWARE_BACKED_EVALUATION_FAILED",
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
class PreferentialNetworkServiceConfig(typing_extensions.TypedDict, total=False):
    fallbackToDefaultConnection: typing_extensions.Literal[
        "FALLBACK_TO_DEFAULT_CONNECTION_UNSPECIFIED",
        "FALLBACK_TO_DEFAULT_CONNECTION_ALLOWED",
        "FALLBACK_TO_DEFAULT_CONNECTION_DISALLOWED",
    ]
    nonMatchingNetworks: typing_extensions.Literal[
        "NON_MATCHING_NETWORKS_UNSPECIFIED",
        "NON_MATCHING_NETWORKS_ALLOWED",
        "NON_MATCHING_NETWORKS_DISALLOWED",
    ]
    preferentialNetworkId: typing_extensions.Literal[
        "PREFERENTIAL_NETWORK_ID_UNSPECIFIED",
        "NO_PREFERENTIAL_NETWORK",
        "PREFERENTIAL_NETWORK_ID_ONE",
        "PREFERENTIAL_NETWORK_ID_TWO",
        "PREFERENTIAL_NETWORK_ID_THREE",
        "PREFERENTIAL_NETWORK_ID_FOUR",
        "PREFERENTIAL_NETWORK_ID_FIVE",
    ]

@typing.type_check_only
class PreferentialNetworkServiceSettings(typing_extensions.TypedDict, total=False):
    defaultPreferentialNetworkId: typing_extensions.Literal[
        "PREFERENTIAL_NETWORK_ID_UNSPECIFIED",
        "NO_PREFERENTIAL_NETWORK",
        "PREFERENTIAL_NETWORK_ID_ONE",
        "PREFERENTIAL_NETWORK_ID_TWO",
        "PREFERENTIAL_NETWORK_ID_THREE",
        "PREFERENTIAL_NETWORK_ID_FOUR",
        "PREFERENTIAL_NETWORK_ID_FIVE",
    ]
    preferentialNetworkServiceConfigs: _list[PreferentialNetworkServiceConfig]

@typing.type_check_only
class ProvisioningInfo(typing_extensions.TypedDict, total=False):
    apiLevel: int
    authenticatedUserEmail: str
    brand: str
    enterprise: str
    imei: str
    managementMode: typing_extensions.Literal[
        "MANAGEMENT_MODE_UNSPECIFIED", "DEVICE_OWNER", "PROFILE_OWNER"
    ]
    meid: str
    model: str
    name: str
    ownership: typing_extensions.Literal[
        "OWNERSHIP_UNSPECIFIED", "COMPANY_OWNED", "PERSONALLY_OWNED"
    ]
    serialNumber: str

@typing.type_check_only
class ProxyInfo(typing_extensions.TypedDict, total=False):
    excludedHosts: _list[str]
    host: str
    pacUri: str
    port: int

@typing.type_check_only
class RemoteLockEvent(typing_extensions.TypedDict, total=False):
    adminPackageName: str
    adminUserId: int
    targetUserId: int

@typing.type_check_only
class RemoveEsimParams(typing_extensions.TypedDict, total=False):
    iccId: str

@typing.type_check_only
class RemovePolicyApplicationsRequest(typing_extensions.TypedDict, total=False):
    packageNames: _list[str]

@typing.type_check_only
class RemovePolicyApplicationsResponse(typing_extensions.TypedDict, total=False):
    policy: Policy

@typing.type_check_only
class RequestDeviceInfoParams(typing_extensions.TypedDict, total=False):
    deviceInfo: typing_extensions.Literal["DEVICE_INFO_UNSPECIFIED", "EID"]

@typing.type_check_only
class RequestDeviceInfoStatus(typing_extensions.TypedDict, total=False):
    eidInfo: EidInfo
    status: typing_extensions.Literal[
        "STATUS_UNSPECIFIED",
        "SUCCEEDED",
        "PENDING_USER_ACTION",
        "USER_DECLINED",
        "UNSUPPORTED",
    ]

@typing.type_check_only
class Role(typing_extensions.TypedDict, total=False):
    roleType: typing_extensions.Literal[
        "ROLE_TYPE_UNSPECIFIED",
        "COMPANION_APP",
        "KIOSK",
        "MOBILE_THREAT_DEFENSE_ENDPOINT_DETECTION_RESPONSE",
        "SYSTEM_HEALTH_MONITORING",
    ]

@typing.type_check_only
class ScreenBrightnessSettings(typing_extensions.TypedDict, total=False):
    screenBrightness: int
    screenBrightnessMode: typing_extensions.Literal[
        "SCREEN_BRIGHTNESS_MODE_UNSPECIFIED",
        "BRIGHTNESS_USER_CHOICE",
        "BRIGHTNESS_AUTOMATIC",
        "BRIGHTNESS_FIXED",
    ]

@typing.type_check_only
class ScreenTimeoutSettings(typing_extensions.TypedDict, total=False):
    screenTimeout: str
    screenTimeoutMode: typing_extensions.Literal[
        "SCREEN_TIMEOUT_MODE_UNSPECIFIED",
        "SCREEN_TIMEOUT_USER_CHOICE",
        "SCREEN_TIMEOUT_ENFORCED",
    ]

@typing.type_check_only
class SecurityPosture(typing_extensions.TypedDict, total=False):
    devicePosture: typing_extensions.Literal[
        "POSTURE_UNSPECIFIED", "SECURE", "AT_RISK", "POTENTIALLY_COMPROMISED"
    ]
    postureDetails: _list[PostureDetail]

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
        "PERSONAL_USAGE_DISALLOWED_USERLESS",
    ]
    defaultStatus: typing_extensions.Literal[
        "SIGNIN_DETAIL_DEFAULT_STATUS_UNSPECIFIED",
        "SIGNIN_DETAIL_IS_DEFAULT",
        "SIGNIN_DETAIL_IS_NOT_DEFAULT",
    ]
    qrCode: str
    signinEnrollmentToken: str
    signinUrl: str
    tokenTag: str

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
class SpecificNonComplianceContext(typing_extensions.TypedDict, total=False):
    defaultApplicationContext: DefaultApplicationContext
    oncWifiContext: OncWifiContext
    passwordPoliciesContext: PasswordPoliciesContext

@typing.type_check_only
class StartLostModeParams(typing_extensions.TypedDict, total=False):
    lostEmailAddress: str
    lostMessage: UserFacingMessage
    lostOrganization: UserFacingMessage
    lostPhoneNumber: UserFacingMessage
    lostStreetAddress: UserFacingMessage

@typing.type_check_only
class StartLostModeStatus(typing_extensions.TypedDict, total=False):
    status: typing_extensions.Literal[
        "STATUS_UNSPECIFIED",
        "SUCCESS",
        "RESET_PASSWORD_RECENTLY",
        "USER_EXIT_LOST_MODE_RECENTLY",
        "ALREADY_IN_LOST_MODE",
    ]

@typing.type_check_only
class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class StatusReportingSettings(typing_extensions.TypedDict, total=False):
    applicationReportingSettings: ApplicationReportingSettings
    applicationReportsEnabled: bool
    commonCriteriaModeEnabled: bool
    defaultApplicationInfoReportingEnabled: bool
    deviceSettingsEnabled: bool
    displayInfoEnabled: bool
    hardwareStatusEnabled: bool
    memoryInfoEnabled: bool
    networkInfoEnabled: bool
    powerManagementEventsEnabled: bool
    softwareInfoEnabled: bool
    systemPropertiesEnabled: bool

@typing.type_check_only
class StopLostModeParams(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class StopLostModeStatus(typing_extensions.TypedDict, total=False):
    status: typing_extensions.Literal[
        "STATUS_UNSPECIFIED", "SUCCESS", "NOT_IN_LOST_MODE"
    ]

@typing.type_check_only
class StopLostModeUserAttemptEvent(typing_extensions.TypedDict, total=False):
    status: typing_extensions.Literal[
        "STATUS_UNSPECIFIED", "ATTEMPT_SUCCEEDED", "ATTEMPT_FAILED"
    ]

@typing.type_check_only
class SystemUpdate(typing_extensions.TypedDict, total=False):
    allowedDaysWithoutUpdate: int
    endMinutes: int
    freezePeriods: _list[FreezePeriod]
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
    activationState: typing_extensions.Literal[
        "ACTIVATION_STATE_UNSPECIFIED", "ACTIVATED", "NOT_ACTIVATED"
    ]
    carrierName: str
    configMode: typing_extensions.Literal[
        "CONFIG_MODE_UNSPECIFIED", "ADMIN_CONFIGURED", "USER_CONFIGURED"
    ]
    iccId: str
    phoneNumber: str

@typing.type_check_only
class TermsAndConditions(typing_extensions.TypedDict, total=False):
    content: UserFacingMessage
    header: UserFacingMessage

@typing.type_check_only
class UsageLog(typing_extensions.TypedDict, total=False):
    enabledLogTypes: _list[
        typing_extensions.Literal[
            "LOG_TYPE_UNSPECIFIED", "SECURITY_LOGS", "NETWORK_ACTIVITY_LOGS"
        ]
    ]
    uploadOnCellularAllowed: _list[
        typing_extensions.Literal[
            "LOG_TYPE_UNSPECIFIED", "SECURITY_LOGS", "NETWORK_ACTIVITY_LOGS"
        ]
    ]

@typing.type_check_only
class UsageLogEvent(typing_extensions.TypedDict, total=False):
    adbShellCommandEvent: AdbShellCommandEvent
    adbShellInteractiveEvent: AdbShellInteractiveEvent
    appProcessStartEvent: AppProcessStartEvent
    backupServiceToggledEvent: BackupServiceToggledEvent
    certAuthorityInstalledEvent: CertAuthorityInstalledEvent
    certAuthorityRemovedEvent: CertAuthorityRemovedEvent
    certValidationFailureEvent: CertValidationFailureEvent
    connectEvent: ConnectEvent
    cryptoSelfTestCompletedEvent: CryptoSelfTestCompletedEvent
    dnsEvent: DnsEvent
    enrollmentCompleteEvent: EnrollmentCompleteEvent
    eventId: str
    eventTime: str
    eventType: typing_extensions.Literal[
        "EVENT_TYPE_UNSPECIFIED",
        "ADB_SHELL_COMMAND",
        "ADB_SHELL_INTERACTIVE",
        "APP_PROCESS_START",
        "KEYGUARD_DISMISSED",
        "KEYGUARD_DISMISS_AUTH_ATTEMPT",
        "KEYGUARD_SECURED",
        "FILE_PULLED",
        "FILE_PUSHED",
        "CERT_AUTHORITY_INSTALLED",
        "CERT_AUTHORITY_REMOVED",
        "CERT_VALIDATION_FAILURE",
        "CRYPTO_SELF_TEST_COMPLETED",
        "KEY_DESTRUCTION",
        "KEY_GENERATED",
        "KEY_IMPORT",
        "KEY_INTEGRITY_VIOLATION",
        "LOGGING_STARTED",
        "LOGGING_STOPPED",
        "LOG_BUFFER_SIZE_CRITICAL",
        "MEDIA_MOUNT",
        "MEDIA_UNMOUNT",
        "OS_SHUTDOWN",
        "OS_STARTUP",
        "REMOTE_LOCK",
        "WIPE_FAILURE",
        "CONNECT",
        "DNS",
        "STOP_LOST_MODE_USER_ATTEMPT",
        "LOST_MODE_OUTGOING_PHONE_CALL",
        "LOST_MODE_LOCATION",
        "ENROLLMENT_COMPLETE",
        "BACKUP_SERVICE_TOGGLED",
    ]
    filePulledEvent: FilePulledEvent
    filePushedEvent: FilePushedEvent
    keyDestructionEvent: KeyDestructionEvent
    keyGeneratedEvent: KeyGeneratedEvent
    keyImportEvent: KeyImportEvent
    keyIntegrityViolationEvent: KeyIntegrityViolationEvent
    keyguardDismissAuthAttemptEvent: KeyguardDismissAuthAttemptEvent
    keyguardDismissedEvent: KeyguardDismissedEvent
    keyguardSecuredEvent: KeyguardSecuredEvent
    logBufferSizeCriticalEvent: LogBufferSizeCriticalEvent
    loggingStartedEvent: LoggingStartedEvent
    loggingStoppedEvent: LoggingStoppedEvent
    lostModeLocationEvent: LostModeLocationEvent
    lostModeOutgoingPhoneCallEvent: LostModeOutgoingPhoneCallEvent
    mediaMountEvent: MediaMountEvent
    mediaUnmountEvent: MediaUnmountEvent
    osShutdownEvent: OsShutdownEvent
    osStartupEvent: OsStartupEvent
    remoteLockEvent: RemoteLockEvent
    stopLostModeUserAttemptEvent: StopLostModeUserAttemptEvent
    wipeFailureEvent: WipeFailureEvent

@typing.type_check_only
class User(typing_extensions.TypedDict, total=False):
    accountIdentifier: str

@typing.type_check_only
class UserFacingMessage(typing_extensions.TypedDict, total=False):
    defaultMessage: str
    localizedMessages: dict[str, typing.Any]

@typing.type_check_only
class WebApp(typing_extensions.TypedDict, total=False):
    displayMode: typing_extensions.Literal[
        "DISPLAY_MODE_UNSPECIFIED", "MINIMAL_UI", "STANDALONE", "FULL_SCREEN"
    ]
    icons: _list[WebAppIcon]
    name: str
    startUrl: str
    title: str
    versionCode: str

@typing.type_check_only
class WebAppIcon(typing_extensions.TypedDict, total=False):
    imageData: str

@typing.type_check_only
class WebToken(typing_extensions.TypedDict, total=False):
    enabledFeatures: _list[
        typing_extensions.Literal[
            "FEATURE_UNSPECIFIED",
            "PLAY_SEARCH",
            "PRIVATE_APPS",
            "WEB_APPS",
            "STORE_BUILDER",
            "MANAGED_CONFIGURATIONS",
            "ZERO_TOUCH_CUSTOMER_MANAGEMENT",
        ]
    ]
    name: str
    parentFrameUrl: str
    permissions: _list[
        typing_extensions.Literal["WEB_TOKEN_PERMISSION_UNSPECIFIED", "APPROVE_APPS"]
    ]
    value: str

@typing.type_check_only
class WifiRoamingPolicy(typing_extensions.TypedDict, total=False):
    wifiRoamingSettings: _list[WifiRoamingSetting]

@typing.type_check_only
class WifiRoamingSetting(typing_extensions.TypedDict, total=False):
    wifiRoamingMode: typing_extensions.Literal[
        "WIFI_ROAMING_MODE_UNSPECIFIED",
        "WIFI_ROAMING_DISABLED",
        "WIFI_ROAMING_DEFAULT",
        "WIFI_ROAMING_AGGRESSIVE",
    ]
    wifiSsid: str

@typing.type_check_only
class WifiSsid(typing_extensions.TypedDict, total=False):
    wifiSsid: str

@typing.type_check_only
class WifiSsidPolicy(typing_extensions.TypedDict, total=False):
    wifiSsidPolicyType: typing_extensions.Literal[
        "WIFI_SSID_POLICY_TYPE_UNSPECIFIED", "WIFI_SSID_DENYLIST", "WIFI_SSID_ALLOWLIST"
    ]
    wifiSsids: _list[WifiSsid]

@typing.type_check_only
class WipeAction(typing_extensions.TypedDict, total=False):
    preserveFrp: bool
    wipeAfterDays: int

@typing.type_check_only
class WipeFailureEvent(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class WipeParams(typing_extensions.TypedDict, total=False):
    wipeDataFlags: _list[
        typing_extensions.Literal[
            "WIPE_DATA_FLAG_UNSPECIFIED",
            "PRESERVE_RESET_PROTECTION_DATA",
            "WIPE_EXTERNAL_STORAGE",
            "WIPE_ESIMS",
        ]
    ]
    wipeReason: UserFacingMessage

@typing.type_check_only
class WorkAccountSetupConfig(typing_extensions.TypedDict, total=False):
    authenticationType: typing_extensions.Literal[
        "AUTHENTICATION_TYPE_UNSPECIFIED",
        "AUTHENTICATION_TYPE_NOT_ENFORCED",
        "GOOGLE_AUTHENTICATED",
    ]
    requiredAccountEmail: str
