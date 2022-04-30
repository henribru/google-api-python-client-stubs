import typing

import typing_extensions

_list = list

@typing.type_check_only
class Authentication(typing_extensions.TypedDict, total=False):
    customAccount: CustomAccount
    googleAccount: GoogleAccount
    iapCredential: IapCredential

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
    findingType: str
    form: Form
    frameUrl: str
    fuzzedUrl: str
    httpMethod: str
    name: str
    outdatedLibrary: OutdatedLibrary
    reproductionUrl: str
    severity: typing_extensions.Literal[
        "SEVERITY_UNSPECIFIED", "CRITICAL", "HIGH", "MEDIUM", "LOW"
    ]
    trackingId: str
    violatingResource: ViolatingResource
    vulnerableHeaders: VulnerableHeaders
    vulnerableParameters: VulnerableParameters
    xss: Xss
    xxe: Xxe

@typing.type_check_only
class FindingTypeStats(typing_extensions.TypedDict, total=False):
    findingCount: int
    findingType: str

@typing.type_check_only
class Form(typing_extensions.TypedDict, total=False):
    actionUri: str
    fields: _list[str]

@typing.type_check_only
class GoogleAccount(typing_extensions.TypedDict, total=False):
    password: str
    username: str

@typing.type_check_only
class Header(typing_extensions.TypedDict, total=False):
    name: str
    value: str

@typing.type_check_only
class IapCredential(typing_extensions.TypedDict, total=False):
    iapTestServiceAccountInfo: IapTestServiceAccountInfo

@typing.type_check_only
class IapTestServiceAccountInfo(typing_extensions.TypedDict, total=False):
    targetAudienceClientId: str

@typing.type_check_only
class ListCrawledUrlsResponse(typing_extensions.TypedDict, total=False):
    crawledUrls: _list[CrawledUrl]
    nextPageToken: str

@typing.type_check_only
class ListFindingTypeStatsResponse(typing_extensions.TypedDict, total=False):
    findingTypeStats: _list[FindingTypeStats]

@typing.type_check_only
class ListFindingsResponse(typing_extensions.TypedDict, total=False):
    findings: _list[Finding]
    nextPageToken: str

@typing.type_check_only
class ListScanConfigsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    scanConfigs: _list[ScanConfig]

@typing.type_check_only
class ListScanRunsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    scanRuns: _list[ScanRun]

@typing.type_check_only
class OutdatedLibrary(typing_extensions.TypedDict, total=False):
    learnMoreUrls: _list[str]
    libraryName: str
    version: str

@typing.type_check_only
class ScanConfig(typing_extensions.TypedDict, total=False):
    authentication: Authentication
    blacklistPatterns: _list[str]
    displayName: str
    exportToSecurityCommandCenter: typing_extensions.Literal[
        "EXPORT_TO_SECURITY_COMMAND_CENTER_UNSPECIFIED", "ENABLED", "DISABLED"
    ]
    ignoreHttpStatusErrors: bool
    managedScan: bool
    maxQps: int
    name: str
    riskLevel: typing_extensions.Literal["RISK_LEVEL_UNSPECIFIED", "NORMAL", "LOW"]
    schedule: Schedule
    startingUrls: _list[str]
    staticIpScan: bool
    userAgent: typing_extensions.Literal[
        "USER_AGENT_UNSPECIFIED", "CHROME_LINUX", "CHROME_ANDROID", "SAFARI_IPHONE"
    ]

@typing.type_check_only
class ScanConfigError(typing_extensions.TypedDict, total=False):
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
    fieldName: str

@typing.type_check_only
class ScanRun(typing_extensions.TypedDict, total=False):
    endTime: str
    errorTrace: ScanRunErrorTrace
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
    warningTraces: _list[ScanRunWarningTrace]

@typing.type_check_only
class ScanRunErrorTrace(typing_extensions.TypedDict, total=False):
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
    scanConfigError: ScanConfigError

@typing.type_check_only
class ScanRunWarningTrace(typing_extensions.TypedDict, total=False):
    code: typing_extensions.Literal[
        "CODE_UNSPECIFIED",
        "INSUFFICIENT_CRAWL_RESULTS",
        "TOO_MANY_CRAWL_RESULTS",
        "TOO_MANY_FUZZ_TASKS",
        "BLOCKED_BY_IAP",
        "NO_STARTING_URL_FOUND_FOR_MANAGED_SCAN",
    ]

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
    headers: _list[Header]
    missingHeaders: _list[Header]

@typing.type_check_only
class VulnerableParameters(typing_extensions.TypedDict, total=False):
    parameterNames: _list[str]

@typing.type_check_only
class Xss(typing_extensions.TypedDict, total=False):
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
    errorMessage: str
    stackTraces: _list[str]
    storedXssSeedingUrl: str

@typing.type_check_only
class Xxe(typing_extensions.TypedDict, total=False):
    payloadLocation: typing_extensions.Literal[
        "LOCATION_UNSPECIFIED", "COMPLETE_REQUEST_BODY"
    ]
    payloadValue: str
