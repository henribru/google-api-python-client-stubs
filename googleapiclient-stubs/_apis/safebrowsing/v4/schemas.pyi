import typing

import typing_extensions

class MetadataEntry(typing_extensions.TypedDict, total=False):
    value: str
    key: str

class Constraints(typing_extensions.TypedDict, total=False):
    deviceLocation: str
    language: str
    maxUpdateEntries: int
    maxDatabaseEntries: int
    region: str
    supportedCompressions: typing.List[str]

class ListUpdateResponse(typing_extensions.TypedDict, total=False):
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
    newClientState: str
    responseType: typing_extensions.Literal[
        "RESPONSE_TYPE_UNSPECIFIED", "PARTIAL_UPDATE", "FULL_UPDATE"
    ]
    removals: typing.List[ThreatEntrySet]
    checksum: Checksum
    threatEntryType: typing_extensions.Literal[
        "THREAT_ENTRY_TYPE_UNSPECIFIED",
        "URL",
        "EXECUTABLE",
        "IP_RANGE",
        "CHROME_EXTENSION",
        "FILENAME",
        "CERT",
    ]
    additions: typing.List[ThreatEntrySet]

class FindFullHashesResponse(typing_extensions.TypedDict, total=False):
    negativeCacheDuration: str
    minimumWaitDuration: str
    matches: typing.List[ThreatMatch]

class RiceDeltaEncoding(typing_extensions.TypedDict, total=False):
    riceParameter: int
    firstValue: str
    encodedData: str
    numEntries: int

class FindFullHashesRequest(typing_extensions.TypedDict, total=False):
    clientStates: typing.List[str]
    threatInfo: ThreatInfo
    client: ClientInfo
    apiClient: ClientInfo

class ThreatListDescriptor(typing_extensions.TypedDict, total=False):
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
    threatEntryType: typing_extensions.Literal[
        "THREAT_ENTRY_TYPE_UNSPECIFIED",
        "URL",
        "EXECUTABLE",
        "IP_RANGE",
        "CHROME_EXTENSION",
        "FILENAME",
        "CERT",
    ]
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

class Empty(typing_extensions.TypedDict, total=False): ...

class ThreatEntrySet(typing_extensions.TypedDict, total=False):
    rawHashes: RawHashes
    compressionType: typing_extensions.Literal[
        "COMPRESSION_TYPE_UNSPECIFIED", "RAW", "RICE"
    ]
    rawIndices: RawIndices
    riceHashes: RiceDeltaEncoding
    riceIndices: RiceDeltaEncoding

class FetchThreatListUpdatesRequest(typing_extensions.TypedDict, total=False):
    listUpdateRequests: typing.List[ListUpdateRequest]
    client: ClientInfo

class ThreatMatch(typing_extensions.TypedDict, total=False):
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
    threat: ThreatEntry
    cacheDuration: str
    threatEntryMetadata: ThreatEntryMetadata

class ClientInfo(typing_extensions.TypedDict, total=False):
    clientId: str
    clientVersion: str

class ListThreatListsResponse(typing_extensions.TypedDict, total=False):
    threatLists: typing.List[ThreatListDescriptor]

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
    threatEntryType: typing_extensions.Literal[
        "THREAT_ENTRY_TYPE_UNSPECIFIED",
        "URL",
        "EXECUTABLE",
        "IP_RANGE",
        "CHROME_EXTENSION",
        "FILENAME",
        "CERT",
    ]
    state: str

class Checksum(typing_extensions.TypedDict, total=False):
    sha256: str

class ThreatInfo(typing_extensions.TypedDict, total=False):
    platformTypes: typing.List[str]
    threatEntries: typing.List[ThreatEntry]
    threatTypes: typing.List[str]
    threatEntryTypes: typing.List[str]

class ThreatHit(typing_extensions.TypedDict, total=False):
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
    resources: typing.List[ThreatSource]
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
    entry: ThreatEntry
    clientInfo: ClientInfo

class RawIndices(typing_extensions.TypedDict, total=False):
    indices: typing.List[int]

class ThreatSource(typing_extensions.TypedDict, total=False):
    url: str
    referrer: str
    type: typing_extensions.Literal[
        "THREAT_SOURCE_TYPE_UNSPECIFIED",
        "MATCHING_URL",
        "TAB_URL",
        "TAB_REDIRECT",
        "TAB_RESOURCE",
    ]
    remoteIp: str

class ThreatEntryMetadata(typing_extensions.TypedDict, total=False):
    entries: typing.List[MetadataEntry]

class ThreatEntry(typing_extensions.TypedDict, total=False):
    url: str
    hash: str
    digest: str

class UserInfo(typing_extensions.TypedDict, total=False):
    userId: str
    regionCode: str

class FetchThreatListUpdatesResponse(typing_extensions.TypedDict, total=False):
    listUpdateResponses: typing.List[ListUpdateResponse]
    minimumWaitDuration: str

class FindThreatMatchesResponse(typing_extensions.TypedDict, total=False):
    matches: typing.List[ThreatMatch]

class RawHashes(typing_extensions.TypedDict, total=False):
    prefixSize: int
    rawHashes: str

class FindThreatMatchesRequest(typing_extensions.TypedDict, total=False):
    client: ClientInfo
    threatInfo: ThreatInfo
