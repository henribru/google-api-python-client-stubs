import typing

_list = list

@typing.type_check_only
class Antivirus(typing.TypedDict, total=False):
    state: typing.Literal["STATE_UNSPECIFIED", "MISSING", "DISABLED", "ENABLED"]

@typing.type_check_only
class Challenge(typing.TypedDict, total=False):
    challenge: str

@typing.type_check_only
class CrowdStrikeAgent(typing.TypedDict, total=False):
    agentId: str
    customerId: str

@typing.type_check_only
class DeviceSignals(typing.TypedDict, total=False):
    allowScreenLock: bool
    antivirus: Antivirus
    browserVersion: str
    builtInDnsClientEnabled: bool
    chromeRemoteDesktopAppBlocked: bool
    crowdStrikeAgent: CrowdStrikeAgent
    deviceAffiliationIds: _list[str]
    deviceEnrollmentDomain: str
    deviceManufacturer: str
    deviceModel: str
    diskEncryption: typing.Literal[
        "DISK_ENCRYPTION_UNSPECIFIED",
        "DISK_ENCRYPTION_UNKNOWN",
        "DISK_ENCRYPTION_DISABLED",
        "DISK_ENCRYPTION_ENCRYPTED",
    ]
    displayName: str
    hostname: str
    imei: _list[str]
    macAddresses: _list[str]
    meid: _list[str]
    operatingSystem: typing.Literal[
        "OPERATING_SYSTEM_UNSPECIFIED",
        "CHROME_OS",
        "CHROMIUM_OS",
        "WINDOWS",
        "MAC_OS_X",
        "LINUX",
    ]
    osFirewall: typing.Literal[
        "OS_FIREWALL_UNSPECIFIED",
        "OS_FIREWALL_UNKNOWN",
        "OS_FIREWALL_DISABLED",
        "OS_FIREWALL_ENABLED",
    ]
    osVersion: str
    passwordProtectionWarningTrigger: typing.Literal[
        "PASSWORD_PROTECTION_WARNING_TRIGGER_UNSPECIFIED",
        "POLICY_UNSET",
        "PASSWORD_PROTECTION_OFF",
        "PASSWORD_REUSE",
        "PHISHING_REUSE",
    ]
    profileAffiliationIds: _list[str]
    profileEnrollmentDomain: str
    realtimeUrlCheckMode: typing.Literal[
        "REALTIME_URL_CHECK_MODE_UNSPECIFIED",
        "REALTIME_URL_CHECK_MODE_DISABLED",
        "REALTIME_URL_CHECK_MODE_ENABLED_MAIN_FRAME",
    ]
    safeBrowsingProtectionLevel: typing.Literal[
        "SAFE_BROWSING_PROTECTION_LEVEL_UNSPECIFIED", "INACTIVE", "STANDARD", "ENHANCED"
    ]
    screenLockSecured: typing.Literal[
        "SCREEN_LOCK_SECURED_UNSPECIFIED",
        "SCREEN_LOCK_SECURED_UNKNOWN",
        "SCREEN_LOCK_SECURED_DISABLED",
        "SCREEN_LOCK_SECURED_ENABLED",
    ]
    secureBootMode: typing.Literal[
        "SECURE_BOOT_MODE_UNSPECIFIED",
        "SECURE_BOOT_MODE_UNKNOWN",
        "SECURE_BOOT_MODE_DISABLED",
        "SECURE_BOOT_MODE_ENABLED",
    ]
    serialNumber: str
    siteIsolationEnabled: bool
    systemDnsServers: _list[str]
    thirdPartyBlockingEnabled: bool
    trigger: typing.Literal[
        "TRIGGER_UNSPECIFIED", "TRIGGER_BROWSER_NAVIGATION", "TRIGGER_LOGIN_SCREEN"
    ]
    windowsMachineDomain: str
    windowsUserDomain: str

@typing.type_check_only
class Empty(typing.TypedDict, total=False): ...

@typing.type_check_only
class VerifyChallengeResponseRequest(typing.TypedDict, total=False):
    challengeResponse: str
    expectedIdentity: str

@typing.type_check_only
class VerifyChallengeResponseResult(typing.TypedDict, total=False):
    attestedDeviceId: str
    customerId: str
    deviceEnrollmentId: str
    devicePermanentId: str
    deviceSignal: str
    deviceSignals: DeviceSignals
    keyTrustLevel: typing.Literal[
        "KEY_TRUST_LEVEL_UNSPECIFIED",
        "CHROME_OS_VERIFIED_MODE",
        "CHROME_OS_DEVELOPER_MODE",
        "CHROME_BROWSER_HW_KEY",
        "CHROME_BROWSER_OS_KEY",
        "CHROME_BROWSER_NO_KEY",
        "CHROME_OS_NO_KEY",
    ]
    profileCustomerId: str
    profileKeyTrustLevel: typing.Literal[
        "KEY_TRUST_LEVEL_UNSPECIFIED",
        "CHROME_OS_VERIFIED_MODE",
        "CHROME_OS_DEVELOPER_MODE",
        "CHROME_BROWSER_HW_KEY",
        "CHROME_BROWSER_OS_KEY",
        "CHROME_BROWSER_NO_KEY",
        "CHROME_OS_NO_KEY",
    ]
    profilePermanentId: str
    signedPublicKeyAndChallenge: str
    virtualDeviceId: str
    virtualProfileId: str
