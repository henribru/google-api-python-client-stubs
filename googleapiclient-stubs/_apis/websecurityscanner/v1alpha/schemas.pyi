import typing

import typing_extensions
@typing.type_check_only
class Authentication(typing_extensions.TypedDict, total=False):
    customAccount: CustomAccount
    googleAccount: GoogleAccount

@typing.type_check_only
class CrawledUrl(typing_extensions.TypedDict, total=False):
    body: str
    httpMethod: str
    url: str

@typing.type_check_only
class CustomAccount(typing_extensions.TypedDict, total=False):
    loginUrl: str
    password: str
    username: str

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Finding(typing_extensions.TypedDict, total=False):
    body: str
    description: str
    finalUrl: str
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
    frameUrl: str
    fuzzedUrl: str
    httpMethod: str
    name: str
    outdatedLibrary: OutdatedLibrary
    reproductionUrl: str
    trackingId: str
    violatingResource: ViolatingResource
    vulnerableHeaders: VulnerableHeaders
    vulnerableParameters: VulnerableParameters
    xss: Xss

@typing.type_check_only
class FindingTypeStats(typing_extensions.TypedDict, total=False):
    findingCount: int
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

@typing.type_check_only
class GoogleAccount(typing_extensions.TypedDict, total=False):
    password: str
    username: str

@typing.type_check_only
class Header(typing_extensions.TypedDict, total=False):
    name: str
    value: str

@typing.type_check_only
class ListCrawledUrlsResponse(typing_extensions.TypedDict, total=False):
    crawledUrls: typing.List[CrawledUrl]
    nextPageToken: str

@typing.type_check_only
class ListFindingTypeStatsResponse(typing_extensions.TypedDict, total=False):
    findingTypeStats: typing.List[FindingTypeStats]

@typing.type_check_only
class ListFindingsResponse(typing_extensions.TypedDict, total=False):
    findings: typing.List[Finding]
    nextPageToken: str

@typing.type_check_only
class ListScanConfigsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    scanConfigs: typing.List[ScanConfig]

@typing.type_check_only
class ListScanRunsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    scanRuns: typing.List[ScanRun]

@typing.type_check_only
class OutdatedLibrary(typing_extensions.TypedDict, total=False):
    learnMoreUrls: typing.List[str]
    libraryName: str
    version: str

@typing.type_check_only
class ScanConfig(typing_extensions.TypedDict, total=False):
    authentication: Authentication
    blacklistPatterns: typing.List[str]
    displayName: str
    latestRun: ScanRun
    maxQps: int
    name: str
    schedule: Schedule
    startingUrls: typing.List[str]
    targetPlatforms: typing.List[str]
    userAgent: typing_extensions.Literal[
        "USER_AGENT_UNSPECIFIED", "CHROME_LINUX", "CHROME_ANDROID", "SAFARI_IPHONE"
    ]

@typing.type_check_only
class ScanRun(typing_extensions.TypedDict, total=False):
    endTime: str
    executionState: typing_extensions.Literal[
        "EXECUTION_STATE_UNSPECIFIED", "QUEUED", "SCANNING", "FINISHED"
    ]
    hasVulnerabilities: bool
    name: str
    progressPercent: int
    resultState: typing_extensions.Literal[
        "RESULT_STATE_UNSPECIFIED", "SUCCESS", "ERROR", "KILLED"
    ]
    startTime: str
    urlsCrawledCount: str
    urlsTestedCount: str

@typing.type_check_only
class Schedule(typing_extensions.TypedDict, total=False):
    intervalDurationDays: int
    scheduleTime: str

@typing.type_check_only
class StartScanRunRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class StopScanRunRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class ViolatingResource(typing_extensions.TypedDict, total=False):
    contentType: str
    resourceUrl: str

@typing.type_check_only
class VulnerableHeaders(typing_extensions.TypedDict, total=False):
    headers: typing.List[Header]
    missingHeaders: typing.List[Header]

@typing.type_check_only
class VulnerableParameters(typing_extensions.TypedDict, total=False):
    parameterNames: typing.List[str]

@typing.type_check_only
class Xss(typing_extensions.TypedDict, total=False):
    errorMessage: str
    stackTraces: typing.List[str]
