import typing

import typing_extensions
@typing.type_check_only
class Checksum(typing_extensions.TypedDict, total=False):
    sha256: str

@typing.type_check_only
class ClientInfo(typing_extensions.TypedDict, total=False):
    clientId: str
    clientVersion: str

@typing.type_check_only
class Constraints(typing_extensions.TypedDict, total=False):
    deviceLocation: str
    language: str
    maxDatabaseEntries: int
    maxUpdateEntries: int
    region: str
    supportedCompressions: typing.List[str]

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class FetchThreatListUpdatesRequest(typing_extensions.TypedDict, total=False):
    client: ClientInfo
    listUpdateRequests: typing.List[ListUpdateRequest]

@typing.type_check_only
class FetchThreatListUpdatesResponse(typing_extensions.TypedDict, total=False):
    listUpdateResponses: typing.List[ListUpdateResponse]
    minimumWaitDuration: str

@typing.type_check_only
class FindFullHashesRequest(typing_extensions.TypedDict, total=False):
    apiClient: ClientInfo
    client: ClientInfo
    clientStates: typing.List[str]
    threatInfo: ThreatInfo

@typing.type_check_only
class FindFullHashesResponse(typing_extensions.TypedDict, total=False):
    matches: typing.List[ThreatMatch]
    minimumWaitDuration: str
    negativeCacheDuration: str

@typing.type_check_only
class FindThreatMatchesRequest(typing_extensions.TypedDict, total=False):
    client: ClientInfo
    threatInfo: ThreatInfo

@typing.type_check_only
class FindThreatMatchesResponse(typing_extensions.TypedDict, total=False):
    matches: typing.List[ThreatMatch]

@typing.type_check_only
class ListThreatListsResponse(typing_extensions.TypedDict, total=False):
    threatLists: typing.List[ThreatListDescriptor]

@typing.type_check_only
class ListUpdateRequest(typing_extensions.TypedDict, total=False):
    constraints: Constraints
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
    ]

@typing.type_check_only
class ListUpdateResponse(typing_extensions.TypedDict, total=False):
    additions: typing.List[ThreatEntrySet]
    checksum: Checksum
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
    removals: typing.List[ThreatEntrySet]
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
    ]

@typing.type_check_only
class MetadataEntry(typing_extensions.TypedDict, total=False):
    key: str
    value: str

@typing.type_check_only
class RawHashes(typing_extensions.TypedDict, total=False):
    prefixSize: int
    rawHashes: str

@typing.type_check_only
class RawIndices(typing_extensions.TypedDict, total=False):
    indices: typing.List[int]

@typing.type_check_only
class RiceDeltaEncoding(typing_extensions.TypedDict, total=False):
    encodedData: str
    firstValue: str
    numEntries: int
    riceParameter: int

@typing.type_check_only
class ThreatEntry(typing_extensions.TypedDict, total=False):
    digest: str
    hash: str
    url: str

@typing.type_check_only
class ThreatEntryMetadata(typing_extensions.TypedDict, total=False):
    entries: typing.List[MetadataEntry]

@typing.type_check_only
class ThreatEntrySet(typing_extensions.TypedDict, total=False):
    compressionType: typing_extensions.Literal[
        "COMPRESSION_TYPE_UNSPECIFIED", "RAW", "RICE"
    ]
    rawHashes: RawHashes
    rawIndices: RawIndices
    riceHashes: RiceDeltaEncoding
    riceIndices: RiceDeltaEncoding

@typing.type_check_only
class ThreatHit(typing_extensions.TypedDict, total=False):
    clientInfo: ClientInfo
    entry: ThreatEntry
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
    resources: typing.List[ThreatSource]
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
    ]
    userInfo: UserInfo

@typing.type_check_only
class ThreatInfo(typing_extensions.TypedDict, total=False):
    platformTypes: typing.List[str]
    threatEntries: typing.List[ThreatEntry]
    threatEntryTypes: typing.List[str]
    threatTypes: typing.List[str]

@typing.type_check_only
class ThreatListDescriptor(typing_extensions.TypedDict, total=False):
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
    ]

@typing.type_check_only
class ThreatMatch(typing_extensions.TypedDict, total=False):
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
    threat: ThreatEntry
    threatEntryMetadata: ThreatEntryMetadata
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
    ]

@typing.type_check_only
class ThreatSource(typing_extensions.TypedDict, total=False):
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
class UserInfo(typing_extensions.TypedDict, total=False):
    regionCode: str
    userId: str
