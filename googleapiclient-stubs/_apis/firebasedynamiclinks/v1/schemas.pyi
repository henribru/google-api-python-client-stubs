import typing

import typing_extensions

_list = list

@typing.type_check_only
class AnalyticsInfo(typing_extensions.TypedDict, total=False):
    googlePlayAnalytics: GooglePlayAnalytics
    itunesConnectAnalytics: ITunesConnectAnalytics

@typing.type_check_only
class AndroidInfo(typing_extensions.TypedDict, total=False):
    androidFallbackLink: str
    androidLink: str
    androidMinPackageVersionCode: str
    androidPackageName: str

@typing.type_check_only
class CreateManagedShortLinkRequest(typing_extensions.TypedDict, total=False):
    dynamicLinkInfo: DynamicLinkInfo
    longDynamicLink: str
    name: str
    sdkVersion: str
    suffix: Suffix

@typing.type_check_only
class CreateManagedShortLinkResponse(typing_extensions.TypedDict, total=False):
    managedShortLink: ManagedShortLink
    previewLink: str
    warning: _list[DynamicLinkWarning]

@typing.type_check_only
class CreateShortDynamicLinkRequest(typing_extensions.TypedDict, total=False):
    dynamicLinkInfo: DynamicLinkInfo
    longDynamicLink: str
    sdkVersion: str
    suffix: Suffix

@typing.type_check_only
class CreateShortDynamicLinkResponse(typing_extensions.TypedDict, total=False):
    previewLink: str
    shortLink: str
    warning: _list[DynamicLinkWarning]

@typing.type_check_only
class DesktopInfo(typing_extensions.TypedDict, total=False):
    desktopFallbackLink: str

@typing.type_check_only
class DeviceInfo(typing_extensions.TypedDict, total=False):
    deviceModelName: str
    languageCode: str
    languageCodeFromWebview: str
    languageCodeRaw: str
    screenResolutionHeight: str
    screenResolutionWidth: str
    timezone: str

@typing.type_check_only
class DynamicLinkEventStat(typing_extensions.TypedDict, total=False):
    count: str
    event: typing_extensions.Literal[
        "DYNAMIC_LINK_EVENT_UNSPECIFIED",
        "CLICK",
        "REDIRECT",
        "APP_INSTALL",
        "APP_FIRST_OPEN",
        "APP_RE_OPEN",
    ]
    platform: typing_extensions.Literal[
        "DYNAMIC_LINK_PLATFORM_UNSPECIFIED", "ANDROID", "IOS", "DESKTOP", "OTHER"
    ]

@typing.type_check_only
class DynamicLinkInfo(typing_extensions.TypedDict, total=False):
    analyticsInfo: AnalyticsInfo
    androidInfo: AndroidInfo
    desktopInfo: DesktopInfo
    domainUriPrefix: str
    dynamicLinkDomain: str
    iosInfo: IosInfo
    link: str
    navigationInfo: NavigationInfo
    socialMetaTagInfo: SocialMetaTagInfo

@typing.type_check_only
class DynamicLinkStats(typing_extensions.TypedDict, total=False):
    linkEventStats: _list[DynamicLinkEventStat]

@typing.type_check_only
class DynamicLinkWarning(typing_extensions.TypedDict, total=False):
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
    warningDocumentLink: str
    warningMessage: str

@typing.type_check_only
class GetIosPostInstallAttributionRequest(typing_extensions.TypedDict, total=False):
    appInstallationTime: str
    bundleId: str
    device: DeviceInfo
    iosVersion: str
    retrievalMethod: typing_extensions.Literal[
        "UNKNOWN_PAYLOAD_RETRIEVAL_METHOD",
        "IMPLICIT_WEAK_MATCH",
        "EXPLICIT_WEAK_MATCH",
        "EXPLICIT_STRONG_AFTER_WEAK_MATCH",
    ]
    sdkVersion: str
    uniqueMatchLinkToCheck: str
    visualStyle: typing_extensions.Literal[
        "UNKNOWN_VISUAL_STYLE", "DEFAULT_STYLE", "CUSTOM_STYLE"
    ]

@typing.type_check_only
class GetIosPostInstallAttributionResponse(typing_extensions.TypedDict, total=False):
    appMinimumVersion: str
    attributionConfidence: typing_extensions.Literal[
        "UNKNOWN_ATTRIBUTION_CONFIDENCE", "WEAK", "DEFAULT", "UNIQUE"
    ]
    deepLink: str
    externalBrowserDestinationLink: str
    fallbackLink: str
    invitationId: str
    isStrongMatchExecutable: bool
    matchMessage: str
    requestIpVersion: typing_extensions.Literal["UNKNOWN_IP_VERSION", "IP_V4", "IP_V6"]
    requestedLink: str
    resolvedLink: str
    utmCampaign: str
    utmContent: str
    utmMedium: str
    utmSource: str
    utmTerm: str

@typing.type_check_only
class GetIosReopenAttributionRequest(typing_extensions.TypedDict, total=False):
    bundleId: str
    requestedLink: str
    sdkVersion: str

@typing.type_check_only
class GetIosReopenAttributionResponse(typing_extensions.TypedDict, total=False):
    deepLink: str
    invitationId: str
    iosMinAppVersion: str
    resolvedLink: str
    utmCampaign: str
    utmContent: str
    utmMedium: str
    utmSource: str
    utmTerm: str

@typing.type_check_only
class GooglePlayAnalytics(typing_extensions.TypedDict, total=False):
    gclid: str
    utmCampaign: str
    utmContent: str
    utmMedium: str
    utmSource: str
    utmTerm: str

@typing.type_check_only
class ITunesConnectAnalytics(typing_extensions.TypedDict, total=False):
    at: str
    ct: str
    mt: str
    pt: str

@typing.type_check_only
class IosInfo(typing_extensions.TypedDict, total=False):
    iosAppStoreId: str
    iosBundleId: str
    iosCustomScheme: str
    iosFallbackLink: str
    iosIpadBundleId: str
    iosIpadFallbackLink: str
    iosMinimumVersion: str

@typing.type_check_only
class ManagedShortLink(typing_extensions.TypedDict, total=False):
    creationTime: str
    flaggedAttribute: _list[str]
    info: DynamicLinkInfo
    link: str
    linkName: str
    visibility: typing_extensions.Literal[
        "UNSPECIFIED_VISIBILITY", "UNARCHIVED", "ARCHIVED", "NEVER_SHOWN"
    ]

@typing.type_check_only
class NavigationInfo(typing_extensions.TypedDict, total=False):
    enableForcedRedirect: bool

@typing.type_check_only
class SocialMetaTagInfo(typing_extensions.TypedDict, total=False):
    socialDescription: str
    socialImageLink: str
    socialTitle: str

@typing.type_check_only
class Suffix(typing_extensions.TypedDict, total=False):
    customSuffix: str
    option: typing_extensions.Literal[
        "OPTION_UNSPECIFIED", "UNGUESSABLE", "SHORT", "CUSTOM"
    ]
