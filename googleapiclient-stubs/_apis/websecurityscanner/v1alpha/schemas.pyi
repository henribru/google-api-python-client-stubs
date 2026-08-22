import typing

_list = list

@typing.type_check_only
class Authentication(typing.TypedDict, total=False):
    customAccount: CustomAccount
    googleAccount: GoogleAccount

@typing.type_check_only
class CrawledUrl(typing.TypedDict, total=False):
    body: str
    httpMethod: str
    url: str

@typing.type_check_only
class CustomAccount(typing.TypedDict, total=False):
    loginUrl: str
    password: str
    username: str

@typing.type_check_only
class Empty(typing.TypedDict, total=False): ...

@typing.type_check_only
class Finding(typing.TypedDict, total=False):
    body: str
    description: str
    finalUrl: str
    findingType: typing.Literal[
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
        "ACCESSIBLE_GIT_REPOSITORY",
        "ACCESSIBLE_SVN_REPOSITORY",
        "ACCESSIBLE_ENV_FILE",
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
class FindingTypeStats(typing.TypedDict, total=False):
    findingCount: int
    findingType: typing.Literal[
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
        "ACCESSIBLE_GIT_REPOSITORY",
        "ACCESSIBLE_SVN_REPOSITORY",
        "ACCESSIBLE_ENV_FILE",
    ]

@typing.type_check_only
class GoogleAccount(typing.TypedDict, total=False):
    password: str
    username: str

@typing.type_check_only
class Header(typing.TypedDict, total=False):
    name: str
    value: str

@typing.type_check_only
class ListCrawledUrlsResponse(typing.TypedDict, total=False):
    crawledUrls: _list[CrawledUrl]
    nextPageToken: str

@typing.type_check_only
class ListFindingTypeStatsResponse(typing.TypedDict, total=False):
    findingTypeStats: _list[FindingTypeStats]

@typing.type_check_only
class ListFindingsResponse(typing.TypedDict, total=False):
    findings: _list[Finding]
    nextPageToken: str

@typing.type_check_only
class ListScanConfigsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    scanConfigs: _list[ScanConfig]

@typing.type_check_only
class ListScanRunsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    scanRuns: _list[ScanRun]

@typing.type_check_only
class OutdatedLibrary(typing.TypedDict, total=False):
    learnMoreUrls: _list[str]
    libraryName: str
    version: str

@typing.type_check_only
class ScanConfig(typing.TypedDict, total=False):
    authentication: Authentication
    blacklistPatterns: _list[str]
    displayName: str
    latestRun: ScanRun
    maxQps: int
    name: str
    schedule: Schedule
    startingUrls: _list[str]
    targetPlatforms: _list[
        typing.Literal[
            "TARGET_PLATFORM_UNSPECIFIED",
            "APP_ENGINE",
            "COMPUTE",
            "CLOUD_RUN",
            "CLOUD_FUNCTIONS",
        ]
    ]
    userAgent: typing.Literal[
        "USER_AGENT_UNSPECIFIED", "CHROME_LINUX", "CHROME_ANDROID", "SAFARI_IPHONE"
    ]

@typing.type_check_only
class ScanRun(typing.TypedDict, total=False):
    endTime: str
    executionState: typing.Literal[
        "EXECUTION_STATE_UNSPECIFIED", "QUEUED", "SCANNING", "FINISHED"
    ]
    hasVulnerabilities: bool
    name: str
    progressPercent: int
    resultState: typing.Literal[
        "RESULT_STATE_UNSPECIFIED", "SUCCESS", "ERROR", "KILLED"
    ]
    startTime: str
    urlsCrawledCount: str
    urlsTestedCount: str

@typing.type_check_only
class Schedule(typing.TypedDict, total=False):
    intervalDurationDays: int
    scheduleTime: str

@typing.type_check_only
class StartScanRunRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class StopScanRunRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class ViolatingResource(typing.TypedDict, total=False):
    contentType: str
    resourceUrl: str

@typing.type_check_only
class VulnerableHeaders(typing.TypedDict, total=False):
    headers: _list[Header]
    missingHeaders: _list[Header]

@typing.type_check_only
class VulnerableParameters(typing.TypedDict, total=False):
    parameterNames: _list[str]

@typing.type_check_only
class Xss(typing.TypedDict, total=False):
    errorMessage: str
    stackTraces: _list[str]
