import typing

import typing_extensions

class DynamicLinkStats(typing_extensions.TypedDict, total=False):
    linkEventStats: typing.List[DynamicLinkEventStat]

class GetIosReopenAttributionRequest(typing_extensions.TypedDict, total=False):
    bundleId: str
    sdkVersion: str
    requestedLink: str

class SocialMetaTagInfo(typing_extensions.TypedDict, total=False):
    socialImageLink: str
    socialDescription: str
    socialTitle: str

class Suffix(typing_extensions.TypedDict, total=False):
    option: typing_extensions.Literal[
        "OPTION_UNSPECIFIED", "UNGUESSABLE", "SHORT", "CUSTOM"
    ]
    customSuffix: str

class DeviceInfo(typing_extensions.TypedDict, total=False):
    timezone: str
    deviceModelName: str
    screenResolutionHeight: str
    languageCodeRaw: str
    screenResolutionWidth: str
    languageCodeFromWebview: str
    languageCode: str

class CreateManagedShortLinkResponse(typing_extensions.TypedDict, total=False):
    managedShortLink: ManagedShortLink
    previewLink: str
    warning: typing.List[DynamicLinkWarning]

class IosInfo(typing_extensions.TypedDict, total=False):
    iosBundleId: str
    iosCustomScheme: str
    iosAppStoreId: str
    iosIpadBundleId: str
    iosIpadFallbackLink: str
    iosFallbackLink: str
    iosMinimumVersion: str

class AnalyticsInfo(typing_extensions.TypedDict, total=False):
    googlePlayAnalytics: GooglePlayAnalytics
    itunesConnectAnalytics: ITunesConnectAnalytics

class GooglePlayAnalytics(typing_extensions.TypedDict, total=False):
    utmCampaign: str
    utmContent: str
    utmMedium: str
    utmTerm: str
    utmSource: str
    gclid: str

class NavigationInfo(typing_extensions.TypedDict, total=False):
    enableForcedRedirect: bool

class ManagedShortLink(typing_extensions.TypedDict, total=False):
    info: DynamicLinkInfo
    linkName: str
    flaggedAttribute: typing.List[str]
    link: str
    visibility: typing_extensions.Literal[
        "UNSPECIFIED_VISIBILITY", "UNARCHIVED", "ARCHIVED", "NEVER_SHOWN"
    ]
    creationTime: str

class CreateShortDynamicLinkRequest(typing_extensions.TypedDict, total=False):
    dynamicLinkInfo: DynamicLinkInfo
    sdkVersion: str
    longDynamicLink: str
    suffix: Suffix

class AndroidInfo(typing_extensions.TypedDict, total=False):
    androidLink: str
    androidFallbackLink: str
    androidPackageName: str
    androidMinPackageVersionCode: str

class GetIosPostInstallAttributionRequest(typing_extensions.TypedDict, total=False):
    device: DeviceInfo
    retrievalMethod: typing_extensions.Literal[
        "UNKNOWN_PAYLOAD_RETRIEVAL_METHOD",
        "IMPLICIT_WEAK_MATCH",
        "EXPLICIT_WEAK_MATCH",
        "EXPLICIT_STRONG_AFTER_WEAK_MATCH",
    ]
    visualStyle: typing_extensions.Literal[
        "UNKNOWN_VISUAL_STYLE", "DEFAULT_STYLE", "CUSTOM_STYLE"
    ]
    bundleId: str
    uniqueMatchLinkToCheck: str
    sdkVersion: str
    appInstallationTime: str
    iosVersion: str

class DynamicLinkWarning(typing_extensions.TypedDict, total=False):
    warningDocumentLink: str
    warningCode: typing_extensions.Literal[
        "CODE_UNSPECIFIED",
        "NOT_IN_PROJECT_ANDROID_PACKAGE_NAME",
        "NOT_INTEGER_ANDROID_PACKAGE_MIN_VERSION",
        "UNNECESSARY_ANDROID_PACKAGE_MIN_VERSION",
        "NOT_URI_ANDROID_LINK",
        "UNNECESSARY_ANDROID_LINK",
        "NOT_URI_ANDROID_FALLBACK_LINK",
        "BAD_URI_SCHEME_ANDROID_FALLBACK_LINK",
        "NOT_IN_PROJECT_IOS_BUNDLE_ID",
        "NOT_IN_PROJECT_IPAD_BUNDLE_ID",
        "UNNECESSARY_IOS_URL_SCHEME",
        "NOT_NUMERIC_IOS_APP_STORE_ID",
        "UNNECESSARY_IOS_APP_STORE_ID",
        "NOT_URI_IOS_FALLBACK_LINK",
        "BAD_URI_SCHEME_IOS_FALLBACK_LINK",
        "NOT_URI_IPAD_FALLBACK_LINK",
        "BAD_URI_SCHEME_IPAD_FALLBACK_LINK",
        "BAD_DEBUG_PARAM",
        "BAD_AD_PARAM",
        "DEPRECATED_PARAM",
        "UNRECOGNIZED_PARAM",
        "TOO_LONG_PARAM",
        "NOT_URI_SOCIAL_IMAGE_LINK",
        "BAD_URI_SCHEME_SOCIAL_IMAGE_LINK",
        "NOT_URI_SOCIAL_URL",
        "BAD_URI_SCHEME_SOCIAL_URL",
        "LINK_LENGTH_TOO_LONG",
        "LINK_WITH_FRAGMENTS",
        "NOT_MATCHING_IOS_BUNDLE_ID_AND_STORE_ID",
    ]
    warningMessage: str

class DesktopInfo(typing_extensions.TypedDict, total=False):
    desktopFallbackLink: str

class DynamicLinkEventStat(typing_extensions.TypedDict, total=False):
    count: str
    platform: typing_extensions.Literal[
        "DYNAMIC_LINK_PLATFORM_UNSPECIFIED", "ANDROID", "IOS", "DESKTOP", "OTHER"
    ]
    event: typing_extensions.Literal[
        "DYNAMIC_LINK_EVENT_UNSPECIFIED",
        "CLICK",
        "REDIRECT",
        "APP_INSTALL",
        "APP_FIRST_OPEN",
        "APP_RE_OPEN",
    ]

class CreateShortDynamicLinkResponse(typing_extensions.TypedDict, total=False):
    previewLink: str
    shortLink: str
    warning: typing.List[DynamicLinkWarning]

class DynamicLinkInfo(typing_extensions.TypedDict, total=False):
    link: str
    desktopInfo: DesktopInfo
    socialMetaTagInfo: SocialMetaTagInfo
    iosInfo: IosInfo
    analyticsInfo: AnalyticsInfo
    domainUriPrefix: str
    dynamicLinkDomain: str
    androidInfo: AndroidInfo
    navigationInfo: NavigationInfo

class GetIosReopenAttributionResponse(typing_extensions.TypedDict, total=False):
    iosMinAppVersion: str
    resolvedLink: str
    utmContent: str
    utmCampaign: str
    invitationId: str
    utmTerm: str
    utmMedium: str
    utmSource: str
    deepLink: str

class ITunesConnectAnalytics(typing_extensions.TypedDict, total=False):
    ct: str
    pt: str
    mt: str
    at: str

class CreateManagedShortLinkRequest(typing_extensions.TypedDict, total=False):
    sdkVersion: str
    suffix: Suffix
    name: str
    dynamicLinkInfo: DynamicLinkInfo
    longDynamicLink: str

class GetIosPostInstallAttributionResponse(typing_extensions.TypedDict, total=False):
    matchMessage: str
    requestIpVersion: typing_extensions.Literal["UNKNOWN_IP_VERSION", "IP_V4", "IP_V6"]
    deepLink: str
    requestedLink: str
    fallbackLink: str
    externalBrowserDestinationLink: str
    utmCampaign: str
    utmMedium: str
    attributionConfidence: typing_extensions.Literal[
        "UNKNOWN_ATTRIBUTION_CONFIDENCE", "WEAK", "DEFAULT", "UNIQUE"
    ]
    invitationId: str
    isStrongMatchExecutable: bool
    appMinimumVersion: str
    utmContent: str
    utmSource: str
    resolvedLink: str
    utmTerm: str
