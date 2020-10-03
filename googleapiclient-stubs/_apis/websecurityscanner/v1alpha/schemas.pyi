import typing

import typing_extensions

class ViolatingResource(typing_extensions.TypedDict, total=False):
    contentType: str
    resourceUrl: str

class ScanConfig(typing_extensions.TypedDict, total=False):
    schedule: Schedule
    maxQps: int
    userAgent: typing_extensions.Literal[
        "USER_AGENT_UNSPECIFIED", "CHROME_LINUX", "CHROME_ANDROID", "SAFARI_IPHONE"
    ]
    name: str
    latestRun: ScanRun
    blacklistPatterns: typing.List[str]
    authentication: Authentication
    targetPlatforms: typing.List[str]
    displayName: str
    startingUrls: typing.List[str]

class Authentication(typing_extensions.TypedDict, total=False):
    googleAccount: GoogleAccount
    customAccount: CustomAccount

class Empty(typing_extensions.TypedDict, total=False): ...

class ListScanConfigsResponse(typing_extensions.TypedDict, total=False):
    scanConfigs: typing.List[ScanConfig]
    nextPageToken: str

class Xss(typing_extensions.TypedDict, total=False):
    errorMessage: str
    stackTraces: typing.List[str]

class ListFindingTypeStatsResponse(typing_extensions.TypedDict, total=False):
    findingTypeStats: typing.List[FindingTypeStats]

class VulnerableParameters(typing_extensions.TypedDict, total=False):
    parameterNames: typing.List[str]

class CrawledUrl(typing_extensions.TypedDict, total=False):
    body: str
    url: str
    httpMethod: str

class CustomAccount(typing_extensions.TypedDict, total=False):
    username: str
    password: str
    loginUrl: str

class ListCrawledUrlsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    crawledUrls: typing.List[CrawledUrl]

class Schedule(typing_extensions.TypedDict, total=False):
    intervalDurationDays: int
    scheduleTime: str

class ListFindingsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    findings: typing.List[Finding]

class FindingTypeStats(typing_extensions.TypedDict, total=False):
    findingType: typing_extensions.Literal[
        "FINDING_TYPE_UNSPECIFIED",
        "MIXED_CONTENT",
        "OUTDATED_LIBRARY",
        "ROSETTA_FLASH",
        "XSS_CALLBACK",
        "XSS_ERROR",
        "CLEAR_TEXT_PASSWORD",
        "INVALID_CONTENT_TYPE",
        "XSS_ANGULAR_CALLBACK",
        "INVALID_HEADER",
        "MISSPELLED_SECURITY_HEADER_NAME",
        "MISMATCHING_SECURITY_HEADER_VALUES",
    ]
    findingCount: int

class StartScanRunRequest(typing_extensions.TypedDict, total=False): ...

class VulnerableHeaders(typing_extensions.TypedDict, total=False):
    headers: typing.List[Header]
    missingHeaders: typing.List[Header]

class StopScanRunRequest(typing_extensions.TypedDict, total=False): ...

class ScanRun(typing_extensions.TypedDict, total=False):
    executionState: typing_extensions.Literal[
        "EXECUTION_STATE_UNSPECIFIED", "QUEUED", "SCANNING", "FINISHED"
    ]
    startTime: str
    progressPercent: int
    resultState: typing_extensions.Literal[
        "RESULT_STATE_UNSPECIFIED", "SUCCESS", "ERROR", "KILLED"
    ]
    name: str
    hasVulnerabilities: bool
    urlsCrawledCount: str
    endTime: str
    urlsTestedCount: str

class OutdatedLibrary(typing_extensions.TypedDict, total=False):
    learnMoreUrls: typing.List[str]
    libraryName: str
    version: str

class ListScanRunsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    scanRuns: typing.List[ScanRun]

class GoogleAccount(typing_extensions.TypedDict, total=False):
    username: str
    password: str

class Header(typing_extensions.TypedDict, total=False):
    value: str
    name: str

class Finding(typing_extensions.TypedDict, total=False):
    outdatedLibrary: OutdatedLibrary
    fuzzedUrl: str
    description: str
    name: str
    vulnerableHeaders: VulnerableHeaders
    trackingId: str
    xss: Xss
    violatingResource: ViolatingResource
    finalUrl: str
    vulnerableParameters: VulnerableParameters
    reproductionUrl: str
    findingType: typing_extensions.Literal[
        "FINDING_TYPE_UNSPECIFIED",
        "MIXED_CONTENT",
        "OUTDATED_LIBRARY",
        "ROSETTA_FLASH",
        "XSS_CALLBACK",
        "XSS_ERROR",
        "CLEAR_TEXT_PASSWORD",
        "INVALID_CONTENT_TYPE",
        "XSS_ANGULAR_CALLBACK",
        "INVALID_HEADER",
        "MISSPELLED_SECURITY_HEADER_NAME",
        "MISMATCHING_SECURITY_HEADER_VALUES",
    ]
    body: str
    frameUrl: str
    httpMethod: str
