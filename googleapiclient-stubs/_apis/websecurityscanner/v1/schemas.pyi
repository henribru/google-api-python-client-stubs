import typing

import typing_extensions

class Schedule(typing_extensions.TypedDict, total=False):
    scheduleTime: str
    intervalDurationDays: int

class Header(typing_extensions.TypedDict, total=False):
    value: str
    name: str

class GoogleAccount(typing_extensions.TypedDict, total=False):
    password: str
    username: str

class VulnerableHeaders(typing_extensions.TypedDict, total=False):
    missingHeaders: typing.List[Header]
    headers: typing.List[Header]

class Finding(typing_extensions.TypedDict, total=False):
    description: str
    httpMethod: str
    name: str
    fuzzedUrl: str
    body: str
    violatingResource: ViolatingResource
    frameUrl: str
    trackingId: str
    finalUrl: str
    xss: Xss
    outdatedLibrary: OutdatedLibrary
    vulnerableHeaders: VulnerableHeaders
    vulnerableParameters: VulnerableParameters
    form: Form
    reproductionUrl: str
    severity: typing_extensions.Literal[
        "SEVERITY_UNSPECIFIED", "CRITICAL", "HIGH", "MEDIUM", "LOW"
    ]
    findingType: str

class OutdatedLibrary(typing_extensions.TypedDict, total=False):
    version: str
    libraryName: str
    learnMoreUrls: typing.List[str]

class ListFindingsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    findings: typing.List[Finding]

class ScanConfig(typing_extensions.TypedDict, total=False):
    exportToSecurityCommandCenter: typing_extensions.Literal[
        "EXPORT_TO_SECURITY_COMMAND_CENTER_UNSPECIFIED", "ENABLED", "DISABLED"
    ]
    userAgent: typing_extensions.Literal[
        "USER_AGENT_UNSPECIFIED", "CHROME_LINUX", "CHROME_ANDROID", "SAFARI_IPHONE"
    ]
    startingUrls: typing.List[str]
    displayName: str
    name: str
    maxQps: int
    schedule: Schedule
    blacklistPatterns: typing.List[str]
    riskLevel: typing_extensions.Literal["RISK_LEVEL_UNSPECIFIED", "NORMAL", "LOW"]
    authentication: Authentication
    staticIpScan: bool
    managedScan: bool

class IapCredential(typing_extensions.TypedDict, total=False):
    iapTestServiceAccountInfo: IapTestServiceAccountInfo

class ListFindingTypeStatsResponse(typing_extensions.TypedDict, total=False):
    findingTypeStats: typing.List[FindingTypeStats]

class ListScanRunsResponse(typing_extensions.TypedDict, total=False):
    scanRuns: typing.List[ScanRun]
    nextPageToken: str

class Xss(typing_extensions.TypedDict, total=False):
    errorMessage: str
    storedXssSeedingUrl: str
    attackVector: typing_extensions.Literal[
        "ATTACK_VECTOR_UNSPECIFIED",
        "LOCAL_STORAGE",
        "SESSION_STORAGE",
        "WINDOW_NAME",
        "REFERRER",
        "FORM_INPUT",
        "COOKIE",
        "POST_MESSAGE",
        "GET_PARAMETERS",
        "URL_FRAGMENT",
        "HTML_COMMENT",
        "POST_PARAMETERS",
        "PROTOCOL",
        "STORED_XSS",
        "SAME_ORIGIN",
        "USER_CONTROLLABLE_URL",
    ]
    stackTraces: typing.List[str]

class Form(typing_extensions.TypedDict, total=False):
    fields: typing.List[str]
    actionUri: str

class ScanRun(typing_extensions.TypedDict, total=False):
    urlsCrawledCount: str
    hasVulnerabilities: bool
    warningTraces: typing.List[ScanRunWarningTrace]
    errorTrace: ScanRunErrorTrace
    progressPercent: int
    startTime: str
    name: str
    executionState: typing_extensions.Literal[
        "EXECUTION_STATE_UNSPECIFIED", "QUEUED", "SCANNING", "FINISHED"
    ]
    resultState: typing_extensions.Literal[
        "RESULT_STATE_UNSPECIFIED", "SUCCESS", "ERROR", "KILLED"
    ]
    endTime: str
    urlsTestedCount: str

class IapTestServiceAccountInfo(typing_extensions.TypedDict, total=False):
    targetAudienceClientId: str

class Empty(typing_extensions.TypedDict, total=False): ...

class Authentication(typing_extensions.TypedDict, total=False):
    iapCredential: IapCredential
    googleAccount: GoogleAccount
    customAccount: CustomAccount

class CustomAccount(typing_extensions.TypedDict, total=False):
    password: str
    loginUrl: str
    username: str

class ScanRunErrorTrace(typing_extensions.TypedDict, total=False):
    scanConfigError: ScanConfigError
    code: typing_extensions.Literal[
        "CODE_UNSPECIFIED",
        "INTERNAL_ERROR",
        "SCAN_CONFIG_ISSUE",
        "AUTHENTICATION_CONFIG_ISSUE",
        "TIMED_OUT_WHILE_SCANNING",
        "TOO_MANY_REDIRECTS",
        "TOO_MANY_HTTP_ERRORS",
    ]
    mostCommonHttpErrorCode: int

class StopScanRunRequest(typing_extensions.TypedDict, total=False): ...

class FindingTypeStats(typing_extensions.TypedDict, total=False):
    findingType: str
    findingCount: int

class ListScanConfigsResponse(typing_extensions.TypedDict, total=False):
    scanConfigs: typing.List[ScanConfig]
    nextPageToken: str

class ScanRunWarningTrace(typing_extensions.TypedDict, total=False):
    code: typing_extensions.Literal[
        "CODE_UNSPECIFIED",
        "INSUFFICIENT_CRAWL_RESULTS",
        "TOO_MANY_CRAWL_RESULTS",
        "TOO_MANY_FUZZ_TASKS",
        "BLOCKED_BY_IAP",
        "NO_STARTING_URL_FOUND_FOR_MANAGED_SCAN",
    ]

class VulnerableParameters(typing_extensions.TypedDict, total=False):
    parameterNames: typing.List[str]

class StartScanRunRequest(typing_extensions.TypedDict, total=False): ...

class ViolatingResource(typing_extensions.TypedDict, total=False):
    contentType: str
    resourceUrl: str

class CrawledUrl(typing_extensions.TypedDict, total=False):
    httpMethod: str
    url: str
    body: str

class ScanConfigError(typing_extensions.TypedDict, total=False):
    fieldName: str
    code: typing_extensions.Literal[
        "CODE_UNSPECIFIED",
        "OK",
        "INTERNAL_ERROR",
        "APPENGINE_API_BACKEND_ERROR",
        "APPENGINE_API_NOT_ACCESSIBLE",
        "APPENGINE_DEFAULT_HOST_MISSING",
        "CANNOT_USE_GOOGLE_COM_ACCOUNT",
        "CANNOT_USE_OWNER_ACCOUNT",
        "COMPUTE_API_BACKEND_ERROR",
        "COMPUTE_API_NOT_ACCESSIBLE",
        "CUSTOM_LOGIN_URL_DOES_NOT_BELONG_TO_CURRENT_PROJECT",
        "CUSTOM_LOGIN_URL_MALFORMED",
        "CUSTOM_LOGIN_URL_MAPPED_TO_NON_ROUTABLE_ADDRESS",
        "CUSTOM_LOGIN_URL_MAPPED_TO_UNRESERVED_ADDRESS",
        "CUSTOM_LOGIN_URL_HAS_NON_ROUTABLE_IP_ADDRESS",
        "CUSTOM_LOGIN_URL_HAS_UNRESERVED_IP_ADDRESS",
        "DUPLICATE_SCAN_NAME",
        "INVALID_FIELD_VALUE",
        "FAILED_TO_AUTHENTICATE_TO_TARGET",
        "FINDING_TYPE_UNSPECIFIED",
        "FORBIDDEN_TO_SCAN_COMPUTE",
        "FORBIDDEN_UPDATE_TO_MANAGED_SCAN",
        "MALFORMED_FILTER",
        "MALFORMED_RESOURCE_NAME",
        "PROJECT_INACTIVE",
        "REQUIRED_FIELD",
        "RESOURCE_NAME_INCONSISTENT",
        "SCAN_ALREADY_RUNNING",
        "SCAN_NOT_RUNNING",
        "SEED_URL_DOES_NOT_BELONG_TO_CURRENT_PROJECT",
        "SEED_URL_MALFORMED",
        "SEED_URL_MAPPED_TO_NON_ROUTABLE_ADDRESS",
        "SEED_URL_MAPPED_TO_UNRESERVED_ADDRESS",
        "SEED_URL_HAS_NON_ROUTABLE_IP_ADDRESS",
        "SEED_URL_HAS_UNRESERVED_IP_ADDRESS",
        "SERVICE_ACCOUNT_NOT_CONFIGURED",
        "TOO_MANY_SCANS",
        "UNABLE_TO_RESOLVE_PROJECT_INFO",
        "UNSUPPORTED_BLACKLIST_PATTERN_FORMAT",
        "UNSUPPORTED_FILTER",
        "UNSUPPORTED_FINDING_TYPE",
        "UNSUPPORTED_URL_SCHEME",
    ]

class ListCrawledUrlsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    crawledUrls: typing.List[CrawledUrl]
