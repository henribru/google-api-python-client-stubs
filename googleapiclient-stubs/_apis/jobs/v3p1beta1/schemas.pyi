import typing

import typing_extensions

_list = list

@typing.type_check_only
class ApplicationInfo(typing_extensions.TypedDict, total=False):
    emails: _list[str]
    instruction: str
    uris: _list[str]

@typing.type_check_only
class BatchDeleteJobsRequest(typing_extensions.TypedDict, total=False):
    filter: str

AlternativeBucketRange = typing_extensions.TypedDict(
    "AlternativeBucketRange",
    {
        "from": float,
        "to": float,
    },
    total=False,
)

@typing.type_check_only
class BucketRange(AlternativeBucketRange): ...

@typing.type_check_only
class BucketizedCount(typing_extensions.TypedDict, total=False):
    count: int
    range: BucketRange

@typing.type_check_only
class ClientEvent(typing_extensions.TypedDict, total=False):
    createTime: str
    eventId: str
    extraInfo: dict[str, typing.Any]
    jobEvent: JobEvent
    parentEventId: str
    requestId: str

@typing.type_check_only
class CommuteFilter(typing_extensions.TypedDict, total=False):
    allowImpreciseAddresses: bool
    commuteMethod: typing_extensions.Literal[
        "COMMUTE_METHOD_UNSPECIFIED", "DRIVING", "TRANSIT", "WALKING", "CYCLING"
    ]
    departureTime: TimeOfDay
    roadTraffic: typing_extensions.Literal[
        "ROAD_TRAFFIC_UNSPECIFIED", "TRAFFIC_FREE", "BUSY_HOUR"
    ]
    startCoordinates: LatLng
    travelDuration: str

@typing.type_check_only
class CommuteInfo(typing_extensions.TypedDict, total=False):
    jobLocation: Location
    travelDuration: str

@typing.type_check_only
class Company(typing_extensions.TypedDict, total=False):
    careerSiteUri: str
    derivedInfo: CompanyDerivedInfo
    displayName: str
    eeoText: str
    externalId: str
    headquartersAddress: str
    hiringAgency: bool
    imageUri: str
    keywordSearchableJobCustomAttributes: _list[str]
    name: str
    size: typing_extensions.Literal[
        "COMPANY_SIZE_UNSPECIFIED",
        "MINI",
        "SMALL",
        "SMEDIUM",
        "MEDIUM",
        "BIG",
        "BIGGER",
        "GIANT",
    ]
    suspended: bool
    websiteUri: str

@typing.type_check_only
class CompanyDerivedInfo(typing_extensions.TypedDict, total=False):
    headquartersLocation: Location

@typing.type_check_only
class CompensationEntry(typing_extensions.TypedDict, total=False):
    amount: Money
    description: str
    expectedUnitsPerYear: float
    range: CompensationRange
    type: typing_extensions.Literal[
        "COMPENSATION_TYPE_UNSPECIFIED",
        "BASE",
        "BONUS",
        "SIGNING_BONUS",
        "EQUITY",
        "PROFIT_SHARING",
        "COMMISSIONS",
        "TIPS",
        "OTHER_COMPENSATION_TYPE",
    ]
    unit: typing_extensions.Literal[
        "COMPENSATION_UNIT_UNSPECIFIED",
        "HOURLY",
        "DAILY",
        "WEEKLY",
        "MONTHLY",
        "YEARLY",
        "ONE_TIME",
        "OTHER_COMPENSATION_UNIT",
    ]

@typing.type_check_only
class CompensationFilter(typing_extensions.TypedDict, total=False):
    includeJobsWithUnspecifiedCompensationRange: bool
    range: CompensationRange
    type: typing_extensions.Literal[
        "FILTER_TYPE_UNSPECIFIED",
        "UNIT_ONLY",
        "UNIT_AND_AMOUNT",
        "ANNUALIZED_BASE_AMOUNT",
        "ANNUALIZED_TOTAL_AMOUNT",
    ]
    units: _list[str]

@typing.type_check_only
class CompensationHistogramRequest(typing_extensions.TypedDict, total=False):
    bucketingOption: NumericBucketingOption
    type: typing_extensions.Literal[
        "COMPENSATION_HISTOGRAM_REQUEST_TYPE_UNSPECIFIED",
        "BASE",
        "ANNUALIZED_BASE",
        "ANNUALIZED_TOTAL",
    ]

@typing.type_check_only
class CompensationHistogramResult(typing_extensions.TypedDict, total=False):
    result: NumericBucketingResult
    type: typing_extensions.Literal[
        "COMPENSATION_HISTOGRAM_REQUEST_TYPE_UNSPECIFIED",
        "BASE",
        "ANNUALIZED_BASE",
        "ANNUALIZED_TOTAL",
    ]

@typing.type_check_only
class CompensationInfo(typing_extensions.TypedDict, total=False):
    annualizedBaseCompensationRange: CompensationRange
    annualizedTotalCompensationRange: CompensationRange
    entries: _list[CompensationEntry]

@typing.type_check_only
class CompensationRange(typing_extensions.TypedDict, total=False):
    maxCompensation: Money
    minCompensation: Money

@typing.type_check_only
class CompleteQueryResponse(typing_extensions.TypedDict, total=False):
    completionResults: _list[CompletionResult]
    metadata: ResponseMetadata

@typing.type_check_only
class CompletionResult(typing_extensions.TypedDict, total=False):
    imageUri: str
    suggestion: str
    type: typing_extensions.Literal[
        "COMPLETION_TYPE_UNSPECIFIED", "JOB_TITLE", "COMPANY_NAME", "COMBINED"
    ]

@typing.type_check_only
class CreateClientEventRequest(typing_extensions.TypedDict, total=False):
    clientEvent: ClientEvent

@typing.type_check_only
class CreateCompanyRequest(typing_extensions.TypedDict, total=False):
    company: Company

@typing.type_check_only
class CreateJobRequest(typing_extensions.TypedDict, total=False):
    job: Job

@typing.type_check_only
class CustomAttribute(typing_extensions.TypedDict, total=False):
    filterable: bool
    longValues: _list[str]
    stringValues: _list[str]

@typing.type_check_only
class CustomAttributeHistogramRequest(typing_extensions.TypedDict, total=False):
    key: str
    longValueHistogramBucketingOption: NumericBucketingOption
    stringValueHistogram: bool

@typing.type_check_only
class CustomAttributeHistogramResult(typing_extensions.TypedDict, total=False):
    key: str
    longValueHistogramResult: NumericBucketingResult
    stringValueHistogramResult: dict[str, typing.Any]

@typing.type_check_only
class CustomRankingInfo(typing_extensions.TypedDict, total=False):
    importanceLevel: typing_extensions.Literal[
        "IMPORTANCE_LEVEL_UNSPECIFIED",
        "NONE",
        "LOW",
        "MILD",
        "MEDIUM",
        "HIGH",
        "EXTREME",
    ]
    rankingExpression: str

@typing.type_check_only
class DeviceInfo(typing_extensions.TypedDict, total=False):
    deviceType: typing_extensions.Literal[
        "DEVICE_TYPE_UNSPECIFIED", "WEB", "MOBILE_WEB", "ANDROID", "IOS", "BOT", "OTHER"
    ]
    id: str

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class HistogramFacets(typing_extensions.TypedDict, total=False):
    compensationHistogramFacets: _list[CompensationHistogramRequest]
    customAttributeHistogramFacets: _list[CustomAttributeHistogramRequest]
    simpleHistogramFacets: _list[str]

@typing.type_check_only
class HistogramQuery(typing_extensions.TypedDict, total=False):
    histogramQuery: str

@typing.type_check_only
class HistogramQueryResult(typing_extensions.TypedDict, total=False):
    histogram: dict[str, typing.Any]
    histogramQuery: str

@typing.type_check_only
class HistogramResult(typing_extensions.TypedDict, total=False):
    searchType: typing_extensions.Literal[
        "SEARCH_TYPE_UNSPECIFIED",
        "COMPANY_ID",
        "EMPLOYMENT_TYPE",
        "COMPANY_SIZE",
        "DATE_PUBLISHED",
        "EDUCATION_LEVEL",
        "EXPERIENCE_LEVEL",
        "ADMIN_1",
        "COUNTRY",
        "CITY",
        "LOCALE",
        "LANGUAGE",
        "CATEGORY",
        "CITY_COORDINATE",
        "ADMIN_1_COUNTRY",
        "COMPANY_DISPLAY_NAME",
        "BASE_COMPENSATION_UNIT",
    ]
    values: dict[str, typing.Any]

@typing.type_check_only
class HistogramResults(typing_extensions.TypedDict, total=False):
    compensationHistogramResults: _list[CompensationHistogramResult]
    customAttributeHistogramResults: _list[CustomAttributeHistogramResult]
    simpleHistogramResults: _list[HistogramResult]

@typing.type_check_only
class Job(typing_extensions.TypedDict, total=False):
    addresses: _list[str]
    applicationInfo: ApplicationInfo
    companyDisplayName: str
    companyName: str
    compensationInfo: CompensationInfo
    customAttributes: dict[str, typing.Any]
    degreeTypes: _list[str]
    department: str
    derivedInfo: JobDerivedInfo
    description: str
    employmentTypes: _list[str]
    incentives: str
    jobBenefits: _list[str]
    jobEndTime: str
    jobLevel: typing_extensions.Literal[
        "JOB_LEVEL_UNSPECIFIED",
        "ENTRY_LEVEL",
        "EXPERIENCED",
        "MANAGER",
        "DIRECTOR",
        "EXECUTIVE",
    ]
    jobStartTime: str
    languageCode: str
    name: str
    postingCreateTime: str
    postingExpireTime: str
    postingPublishTime: str
    postingRegion: typing_extensions.Literal[
        "POSTING_REGION_UNSPECIFIED", "ADMINISTRATIVE_AREA", "NATION", "TELECOMMUTE"
    ]
    postingUpdateTime: str
    processingOptions: ProcessingOptions
    promotionValue: int
    qualifications: str
    requisitionId: str
    responsibilities: str
    title: str
    visibility: typing_extensions.Literal[
        "VISIBILITY_UNSPECIFIED",
        "ACCOUNT_ONLY",
        "SHARED_WITH_GOOGLE",
        "SHARED_WITH_PUBLIC",
    ]

@typing.type_check_only
class JobDerivedInfo(typing_extensions.TypedDict, total=False):
    jobCategories: _list[str]
    locations: _list[Location]

@typing.type_check_only
class JobEvent(typing_extensions.TypedDict, total=False):
    jobs: _list[str]
    type: typing_extensions.Literal[
        "JOB_EVENT_TYPE_UNSPECIFIED",
        "IMPRESSION",
        "VIEW",
        "VIEW_REDIRECT",
        "APPLICATION_START",
        "APPLICATION_FINISH",
        "APPLICATION_QUICK_SUBMISSION",
        "APPLICATION_REDIRECT",
        "APPLICATION_START_FROM_SEARCH",
        "APPLICATION_REDIRECT_FROM_SEARCH",
        "APPLICATION_COMPANY_SUBMIT",
        "BOOKMARK",
        "NOTIFICATION",
        "HIRED",
        "SENT_CV",
        "INTERVIEW_GRANTED",
        "NOT_INTERESTED",
    ]

@typing.type_check_only
class JobQuery(typing_extensions.TypedDict, total=False):
    commuteFilter: CommuteFilter
    companyDisplayNames: _list[str]
    companyNames: _list[str]
    compensationFilter: CompensationFilter
    customAttributeFilter: str
    disableSpellCheck: bool
    employmentTypes: _list[str]
    excludedJobs: _list[str]
    jobCategories: _list[str]
    languageCodes: _list[str]
    locationFilters: _list[LocationFilter]
    publishTimeRange: TimestampRange
    query: str
    queryLanguageCode: str

@typing.type_check_only
class LatLng(typing_extensions.TypedDict, total=False):
    latitude: float
    longitude: float

@typing.type_check_only
class ListCompaniesResponse(typing_extensions.TypedDict, total=False):
    companies: _list[Company]
    metadata: ResponseMetadata
    nextPageToken: str

@typing.type_check_only
class ListJobsResponse(typing_extensions.TypedDict, total=False):
    jobs: _list[Job]
    metadata: ResponseMetadata
    nextPageToken: str

@typing.type_check_only
class Location(typing_extensions.TypedDict, total=False):
    latLng: LatLng
    locationType: typing_extensions.Literal[
        "LOCATION_TYPE_UNSPECIFIED",
        "COUNTRY",
        "ADMINISTRATIVE_AREA",
        "SUB_ADMINISTRATIVE_AREA",
        "LOCALITY",
        "POSTAL_CODE",
        "SUB_LOCALITY",
        "SUB_LOCALITY_1",
        "SUB_LOCALITY_2",
        "NEIGHBORHOOD",
        "STREET_ADDRESS",
    ]
    postalAddress: PostalAddress
    radiusInMiles: float

@typing.type_check_only
class LocationFilter(typing_extensions.TypedDict, total=False):
    address: str
    distanceInMiles: float
    latLng: LatLng
    regionCode: str
    telecommutePreference: typing_extensions.Literal[
        "TELECOMMUTE_PREFERENCE_UNSPECIFIED",
        "TELECOMMUTE_EXCLUDED",
        "TELECOMMUTE_ALLOWED",
        "TELECOMMUTE_JOBS_EXCLUDED",
    ]

@typing.type_check_only
class MatchingJob(typing_extensions.TypedDict, total=False):
    commuteInfo: CommuteInfo
    job: Job
    jobSummary: str
    jobTitleSnippet: str
    searchTextSnippet: str

@typing.type_check_only
class MendelDebugInput(typing_extensions.TypedDict, total=False):
    namespacedDebugInput: dict[str, typing.Any]

@typing.type_check_only
class Money(typing_extensions.TypedDict, total=False):
    currencyCode: str
    nanos: int
    units: str

@typing.type_check_only
class NamespacedDebugInput(typing_extensions.TypedDict, total=False):
    absolutelyForcedExpNames: _list[str]
    absolutelyForcedExpTags: _list[str]
    absolutelyForcedExps: _list[int]
    conditionallyForcedExpNames: _list[str]
    conditionallyForcedExpTags: _list[str]
    conditionallyForcedExps: _list[int]
    disableAutomaticEnrollmentSelection: bool
    disableExpNames: _list[str]
    disableExpTags: _list[str]
    disableExps: _list[int]
    disableManualEnrollmentSelection: bool
    disableOrganicSelection: bool
    forcedFlags: dict[str, typing.Any]
    forcedRollouts: dict[str, typing.Any]
    testingMode: typing_extensions.Literal[
        "TESTING_MODE_UNSPECIFIED", "TESTING_MODE_ALL_OFF", "TESTING_MODE_ALL_ON"
    ]

@typing.type_check_only
class NumericBucketingOption(typing_extensions.TypedDict, total=False):
    bucketBounds: _list[float]
    requiresMinMax: bool

@typing.type_check_only
class NumericBucketingResult(typing_extensions.TypedDict, total=False):
    counts: _list[BucketizedCount]
    maxValue: float
    minValue: float

@typing.type_check_only
class Operation(typing_extensions.TypedDict, total=False):
    done: bool
    error: Status
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class PostalAddress(typing_extensions.TypedDict, total=False):
    addressLines: _list[str]
    administrativeArea: str
    languageCode: str
    locality: str
    organization: str
    postalCode: str
    recipients: _list[str]
    regionCode: str
    revision: int
    sortingCode: str
    sublocality: str

@typing.type_check_only
class ProcessingOptions(typing_extensions.TypedDict, total=False):
    disableStreetAddressResolution: bool
    htmlSanitization: typing_extensions.Literal[
        "HTML_SANITIZATION_UNSPECIFIED",
        "HTML_SANITIZATION_DISABLED",
        "SIMPLE_FORMATTING_ONLY",
    ]

@typing.type_check_only
class RequestMetadata(typing_extensions.TypedDict, total=False):
    deviceInfo: DeviceInfo
    domain: str
    sessionId: str
    userId: str

@typing.type_check_only
class ResponseMetadata(typing_extensions.TypedDict, total=False):
    requestId: str

@typing.type_check_only
class SearchJobsRequest(typing_extensions.TypedDict, total=False):
    customRankingInfo: CustomRankingInfo
    disableKeywordMatch: bool
    diversificationLevel: typing_extensions.Literal[
        "DIVERSIFICATION_LEVEL_UNSPECIFIED", "DISABLED", "SIMPLE"
    ]
    enableBroadening: bool
    histogramFacets: HistogramFacets
    histogramQueries: _list[HistogramQuery]
    jobQuery: JobQuery
    jobView: typing_extensions.Literal[
        "JOB_VIEW_UNSPECIFIED",
        "JOB_VIEW_ID_ONLY",
        "JOB_VIEW_MINIMAL",
        "JOB_VIEW_SMALL",
        "JOB_VIEW_FULL",
    ]
    offset: int
    orderBy: str
    pageSize: int
    pageToken: str
    requestMetadata: RequestMetadata
    requirePreciseResultSize: bool
    searchMode: typing_extensions.Literal[
        "SEARCH_MODE_UNSPECIFIED", "JOB_SEARCH", "FEATURED_JOB_SEARCH"
    ]

@typing.type_check_only
class SearchJobsResponse(typing_extensions.TypedDict, total=False):
    broadenedQueryJobsCount: int
    estimatedTotalSize: int
    histogramQueryResults: _list[HistogramQueryResult]
    histogramResults: HistogramResults
    locationFilters: _list[Location]
    matchingJobs: _list[MatchingJob]
    metadata: ResponseMetadata
    nextPageToken: str
    spellCorrection: SpellingCorrection
    totalSize: int

@typing.type_check_only
class SpellingCorrection(typing_extensions.TypedDict, total=False):
    corrected: bool
    correctedText: str

@typing.type_check_only
class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class TimeOfDay(typing_extensions.TypedDict, total=False):
    hours: int
    minutes: int
    nanos: int
    seconds: int

@typing.type_check_only
class TimestampRange(typing_extensions.TypedDict, total=False):
    endTime: str
    startTime: str

@typing.type_check_only
class UpdateCompanyRequest(typing_extensions.TypedDict, total=False):
    company: Company
    updateMask: str

@typing.type_check_only
class UpdateJobRequest(typing_extensions.TypedDict, total=False):
    job: Job
    updateMask: str
