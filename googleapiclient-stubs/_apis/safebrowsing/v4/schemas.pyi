import typing

import typing_extensions

_list = list

@typing.type_check_only
class GoogleProtobufEmpty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class GoogleSecuritySafebrowsingV4Checksum(typing_extensions.TypedDict, total=False):
    sha256: str

@typing.type_check_only
class GoogleSecuritySafebrowsingV4ClientInfo(typing_extensions.TypedDict, total=False):
    clientId: str
    clientVersion: str

@typing.type_check_only
class GoogleSecuritySafebrowsingV4FetchThreatListUpdatesRequest(
    typing_extensions.TypedDict, total=False
):
    client: GoogleSecuritySafebrowsingV4ClientInfo
    listUpdateRequests: _list[
        GoogleSecuritySafebrowsingV4FetchThreatListUpdatesRequestListUpdateRequest
    ]

@typing.type_check_only
class GoogleSecuritySafebrowsingV4FetchThreatListUpdatesRequestListUpdateRequest(
    typing_extensions.TypedDict, total=False
):
    constraints: GoogleSecuritySafebrowsingV4FetchThreatListUpdatesRequestListUpdateRequestConstraints
    platformType: typing_extensions.Literal[
        "PLATFORM_TYPE_UNSPECIFIED",
        "WINDOWS",
        "LINUX",
        "ANDROID",
        "OSX",
        "IOS",
        "ANY_PLATFORM",
        "ALL_PLATFORMS",
        "CHROME",
    ]
    state: str
    threatEntryType: typing_extensions.Literal[
        "THREAT_ENTRY_TYPE_UNSPECIFIED",
        "URL",
        "EXECUTABLE",
        "IP_RANGE",
        "CHROME_EXTENSION",
        "FILENAME",
        "CERT",
    ]
    threatType: typing_extensions.Literal[
        "THREAT_TYPE_UNSPECIFIED",
        "MALWARE",
        "SOCIAL_ENGINEERING",
        "UNWANTED_SOFTWARE",
        "POTENTIALLY_HARMFUL_APPLICATION",
        "SOCIAL_ENGINEERING_INTERNAL",
        "API_ABUSE",
        "MALICIOUS_BINARY",
        "CSD_WHITELIST",
        "CSD_DOWNLOAD_WHITELIST",
        "CLIENT_INCIDENT",
        "CLIENT_INCIDENT_WHITELIST",
        "APK_MALWARE_OFFLINE",
        "SUBRESOURCE_FILTER",
        "SUSPICIOUS",
        "TRICK_TO_BILL",
        "HIGH_CONFIDENCE_ALLOWLIST",
        "ACCURACY_TIPS",
        "SOCIAL_ENGINEERING_LOWER_PRECISION",
    ]

@typing.type_check_only
class GoogleSecuritySafebrowsingV4FetchThreatListUpdatesRequestListUpdateRequestConstraints(
    typing_extensions.TypedDict, total=False
):
    deviceLocation: str
    language: str
    maxDatabaseEntries: int
    maxUpdateEntries: int
    region: str
    supportedCompressions: _list[str]

@typing.type_check_only
class GoogleSecuritySafebrowsingV4FetchThreatListUpdatesResponse(
    typing_extensions.TypedDict, total=False
):
    listUpdateResponses: _list[
        GoogleSecuritySafebrowsingV4FetchThreatListUpdatesResponseListUpdateResponse
    ]
    minimumWaitDuration: str

@typing.type_check_only
class GoogleSecuritySafebrowsingV4FetchThreatListUpdatesResponseListUpdateResponse(
    typing_extensions.TypedDict, total=False
):
    additions: _list[GoogleSecuritySafebrowsingV4ThreatEntrySet]
    checksum: GoogleSecuritySafebrowsingV4Checksum
    newClientState: str
    platformType: typing_extensions.Literal[
        "PLATFORM_TYPE_UNSPECIFIED",
        "WINDOWS",
        "LINUX",
        "ANDROID",
        "OSX",
        "IOS",
        "ANY_PLATFORM",
        "ALL_PLATFORMS",
        "CHROME",
    ]
    removals: _list[GoogleSecuritySafebrowsingV4ThreatEntrySet]
    responseType: typing_extensions.Literal[
        "RESPONSE_TYPE_UNSPECIFIED", "PARTIAL_UPDATE", "FULL_UPDATE"
    ]
    threatEntryType: typing_extensions.Literal[
        "THREAT_ENTRY_TYPE_UNSPECIFIED",
        "URL",
        "EXECUTABLE",
        "IP_RANGE",
        "CHROME_EXTENSION",
        "FILENAME",
        "CERT",
    ]
    threatType: typing_extensions.Literal[
        "THREAT_TYPE_UNSPECIFIED",
        "MALWARE",
        "SOCIAL_ENGINEERING",
        "UNWANTED_SOFTWARE",
        "POTENTIALLY_HARMFUL_APPLICATION",
        "SOCIAL_ENGINEERING_INTERNAL",
        "API_ABUSE",
        "MALICIOUS_BINARY",
        "CSD_WHITELIST",
        "CSD_DOWNLOAD_WHITELIST",
        "CLIENT_INCIDENT",
        "CLIENT_INCIDENT_WHITELIST",
        "APK_MALWARE_OFFLINE",
        "SUBRESOURCE_FILTER",
        "SUSPICIOUS",
        "TRICK_TO_BILL",
        "HIGH_CONFIDENCE_ALLOWLIST",
        "ACCURACY_TIPS",
        "SOCIAL_ENGINEERING_LOWER_PRECISION",
    ]

@typing.type_check_only
class GoogleSecuritySafebrowsingV4FindFullHashesRequest(
    typing_extensions.TypedDict, total=False
):
    apiClient: GoogleSecuritySafebrowsingV4ClientInfo
    client: GoogleSecuritySafebrowsingV4ClientInfo
    clientStates: _list[str]
    threatInfo: GoogleSecuritySafebrowsingV4ThreatInfo

@typing.type_check_only
class GoogleSecuritySafebrowsingV4FindFullHashesResponse(
    typing_extensions.TypedDict, total=False
):
    matches: _list[GoogleSecuritySafebrowsingV4ThreatMatch]
    minimumWaitDuration: str
    negativeCacheDuration: str

@typing.type_check_only
class GoogleSecuritySafebrowsingV4FindThreatMatchesRequest(
    typing_extensions.TypedDict, total=False
):
    client: GoogleSecuritySafebrowsingV4ClientInfo
    threatInfo: GoogleSecuritySafebrowsingV4ThreatInfo

@typing.type_check_only
class GoogleSecuritySafebrowsingV4FindThreatMatchesResponse(
    typing_extensions.TypedDict, total=False
):
    matches: _list[GoogleSecuritySafebrowsingV4ThreatMatch]

@typing.type_check_only
class GoogleSecuritySafebrowsingV4ListThreatListsResponse(
    typing_extensions.TypedDict, total=False
):
    threatLists: _list[GoogleSecuritySafebrowsingV4ThreatListDescriptor]

@typing.type_check_only
class GoogleSecuritySafebrowsingV4RawHashes(typing_extensions.TypedDict, total=False):
    prefixSize: int
    rawHashes: str

@typing.type_check_only
class GoogleSecuritySafebrowsingV4RawIndices(typing_extensions.TypedDict, total=False):
    indices: _list[int]

@typing.type_check_only
class GoogleSecuritySafebrowsingV4RiceDeltaEncoding(
    typing_extensions.TypedDict, total=False
):
    encodedData: str
    firstValue: str
    numEntries: int
    riceParameter: int

@typing.type_check_only
class GoogleSecuritySafebrowsingV4ThreatEntry(typing_extensions.TypedDict, total=False):
    digest: str
    hash: str
    url: str

@typing.type_check_only
class GoogleSecuritySafebrowsingV4ThreatEntryMetadata(
    typing_extensions.TypedDict, total=False
):
    entries: _list[GoogleSecuritySafebrowsingV4ThreatEntryMetadataMetadataEntry]

@typing.type_check_only
class GoogleSecuritySafebrowsingV4ThreatEntryMetadataMetadataEntry(
    typing_extensions.TypedDict, total=False
):
    key: str
    value: str

@typing.type_check_only
class GoogleSecuritySafebrowsingV4ThreatEntrySet(
    typing_extensions.TypedDict, total=False
):
    compressionType: typing_extensions.Literal[
        "COMPRESSION_TYPE_UNSPECIFIED", "RAW", "RICE"
    ]
    rawHashes: GoogleSecuritySafebrowsingV4RawHashes
    rawIndices: GoogleSecuritySafebrowsingV4RawIndices
    riceHashes: GoogleSecuritySafebrowsingV4RiceDeltaEncoding
    riceIndices: GoogleSecuritySafebrowsingV4RiceDeltaEncoding

@typing.type_check_only
class GoogleSecuritySafebrowsingV4ThreatHit(typing_extensions.TypedDict, total=False):
    clientInfo: GoogleSecuritySafebrowsingV4ClientInfo
    entry: GoogleSecuritySafebrowsingV4ThreatEntry
    platformType: typing_extensions.Literal[
        "PLATFORM_TYPE_UNSPECIFIED",
        "WINDOWS",
        "LINUX",
        "ANDROID",
        "OSX",
        "IOS",
        "ANY_PLATFORM",
        "ALL_PLATFORMS",
        "CHROME",
    ]
    resources: _list[GoogleSecuritySafebrowsingV4ThreatHitThreatSource]
    threatType: typing_extensions.Literal[
        "THREAT_TYPE_UNSPECIFIED",
        "MALWARE",
        "SOCIAL_ENGINEERING",
        "UNWANTED_SOFTWARE",
        "POTENTIALLY_HARMFUL_APPLICATION",
        "SOCIAL_ENGINEERING_INTERNAL",
        "API_ABUSE",
        "MALICIOUS_BINARY",
        "CSD_WHITELIST",
        "CSD_DOWNLOAD_WHITELIST",
        "CLIENT_INCIDENT",
        "CLIENT_INCIDENT_WHITELIST",
        "APK_MALWARE_OFFLINE",
        "SUBRESOURCE_FILTER",
        "SUSPICIOUS",
        "TRICK_TO_BILL",
        "HIGH_CONFIDENCE_ALLOWLIST",
        "ACCURACY_TIPS",
        "SOCIAL_ENGINEERING_LOWER_PRECISION",
    ]
    userInfo: GoogleSecuritySafebrowsingV4ThreatHitUserInfo

@typing.type_check_only
class GoogleSecuritySafebrowsingV4ThreatHitThreatSource(
    typing_extensions.TypedDict, total=False
):
    referrer: str
    remoteIp: str
    type: typing_extensions.Literal[
        "THREAT_SOURCE_TYPE_UNSPECIFIED",
        "MATCHING_URL",
        "TAB_URL",
        "TAB_REDIRECT",
        "TAB_RESOURCE",
    ]
    url: str

@typing.type_check_only
class GoogleSecuritySafebrowsingV4ThreatHitUserInfo(
    typing_extensions.TypedDict, total=False
):
    regionCode: str
    userId: str

@typing.type_check_only
class GoogleSecuritySafebrowsingV4ThreatInfo(typing_extensions.TypedDict, total=False):
    platformTypes: _list[str]
    threatEntries: _list[GoogleSecuritySafebrowsingV4ThreatEntry]
    threatEntryTypes: _list[str]
    threatTypes: _list[str]

@typing.type_check_only
class GoogleSecuritySafebrowsingV4ThreatListDescriptor(
    typing_extensions.TypedDict, total=False
):
    platformType: typing_extensions.Literal[
        "PLATFORM_TYPE_UNSPECIFIED",
        "WINDOWS",
        "LINUX",
        "ANDROID",
        "OSX",
        "IOS",
        "ANY_PLATFORM",
        "ALL_PLATFORMS",
        "CHROME",
    ]
    threatEntryType: typing_extensions.Literal[
        "THREAT_ENTRY_TYPE_UNSPECIFIED",
        "URL",
        "EXECUTABLE",
        "IP_RANGE",
        "CHROME_EXTENSION",
        "FILENAME",
        "CERT",
    ]
    threatType: typing_extensions.Literal[
        "THREAT_TYPE_UNSPECIFIED",
        "MALWARE",
        "SOCIAL_ENGINEERING",
        "UNWANTED_SOFTWARE",
        "POTENTIALLY_HARMFUL_APPLICATION",
        "SOCIAL_ENGINEERING_INTERNAL",
        "API_ABUSE",
        "MALICIOUS_BINARY",
        "CSD_WHITELIST",
        "CSD_DOWNLOAD_WHITELIST",
        "CLIENT_INCIDENT",
        "CLIENT_INCIDENT_WHITELIST",
        "APK_MALWARE_OFFLINE",
        "SUBRESOURCE_FILTER",
        "SUSPICIOUS",
        "TRICK_TO_BILL",
        "HIGH_CONFIDENCE_ALLOWLIST",
        "ACCURACY_TIPS",
        "SOCIAL_ENGINEERING_LOWER_PRECISION",
    ]

@typing.type_check_only
class GoogleSecuritySafebrowsingV4ThreatMatch(typing_extensions.TypedDict, total=False):
    cacheDuration: str
    platformType: typing_extensions.Literal[
        "PLATFORM_TYPE_UNSPECIFIED",
        "WINDOWS",
        "LINUX",
        "ANDROID",
        "OSX",
        "IOS",
        "ANY_PLATFORM",
        "ALL_PLATFORMS",
        "CHROME",
    ]
    threat: GoogleSecuritySafebrowsingV4ThreatEntry
    threatEntryMetadata: GoogleSecuritySafebrowsingV4ThreatEntryMetadata
    threatEntryType: typing_extensions.Literal[
        "THREAT_ENTRY_TYPE_UNSPECIFIED",
        "URL",
        "EXECUTABLE",
        "IP_RANGE",
        "CHROME_EXTENSION",
        "FILENAME",
        "CERT",
    ]
    threatType: typing_extensions.Literal[
        "THREAT_TYPE_UNSPECIFIED",
        "MALWARE",
        "SOCIAL_ENGINEERING",
        "UNWANTED_SOFTWARE",
        "POTENTIALLY_HARMFUL_APPLICATION",
        "SOCIAL_ENGINEERING_INTERNAL",
        "API_ABUSE",
        "MALICIOUS_BINARY",
        "CSD_WHITELIST",
        "CSD_DOWNLOAD_WHITELIST",
        "CLIENT_INCIDENT",
        "CLIENT_INCIDENT_WHITELIST",
        "APK_MALWARE_OFFLINE",
        "SUBRESOURCE_FILTER",
        "SUSPICIOUS",
        "TRICK_TO_BILL",
        "HIGH_CONFIDENCE_ALLOWLIST",
        "ACCURACY_TIPS",
        "SOCIAL_ENGINEERING_LOWER_PRECISION",
    ]
