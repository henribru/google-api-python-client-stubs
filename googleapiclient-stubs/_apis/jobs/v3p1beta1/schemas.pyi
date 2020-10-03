import typing

import typing_extensions

class GoogleCloudTalentV4BatchCreateJobsResponse(
    typing_extensions.TypedDict, total=False
):
    jobResults: typing.List[GoogleCloudTalentV4JobResult]

class CustomAttribute(typing_extensions.TypedDict, total=False):
    filterable: bool
    longValues: typing.List[str]
    stringValues: typing.List[str]

BucketRange = typing_extensions.TypedDict(
    "BucketRange",
    {
        "to": float,
        "from": float,
    },
    total=False,
)

class ListJobsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    jobs: typing.List[Job]
    metadata: ResponseMetadata

class CompensationEntry(typing_extensions.TypedDict, total=False):
    expectedUnitsPerYear: float
    amount: Money
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
    description: str
    range: CompensationRange

class NumericBucketingOption(typing_extensions.TypedDict, total=False):
    bucketBounds: typing.List[float]
    requiresMinMax: bool

class CompleteQueryResponse(typing_extensions.TypedDict, total=False):
    metadata: ResponseMetadata
    completionResults: typing.List[CompletionResult]

class JobDerivedInfo(typing_extensions.TypedDict, total=False):
    locations: typing.List[Location]
    jobCategories: typing.List[str]

class GoogleCloudTalentV4CustomAttribute(typing_extensions.TypedDict, total=False):
    keywordSearchable: bool
    longValues: typing.List[str]
    stringValues: typing.List[str]
    filterable: bool

class GoogleCloudTalentV4CompensationInfoCompensationEntry(
    typing_extensions.TypedDict, total=False
):
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
    amount: Money
    expectedUnitsPerYear: float
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
    range: GoogleCloudTalentV4CompensationInfoCompensationRange
    description: str

class Empty(typing_extensions.TypedDict, total=False): ...

class GoogleCloudTalentV4JobApplicationInfo(typing_extensions.TypedDict, total=False):
    emails: typing.List[str]
    uris: typing.List[str]
    instruction: str

class CustomAttributeHistogramRequest(typing_extensions.TypedDict, total=False):
    stringValueHistogram: bool
    longValueHistogramBucketingOption: NumericBucketingOption
    key: str

class CompensationHistogramRequest(typing_extensions.TypedDict, total=False):
    type: typing_extensions.Literal[
        "COMPENSATION_HISTOGRAM_REQUEST_TYPE_UNSPECIFIED",
        "BASE",
        "ANNUALIZED_BASE",
        "ANNUALIZED_TOTAL",
    ]
    bucketingOption: NumericBucketingOption

class GoogleCloudTalentV4BatchDeleteJobsResponse(
    typing_extensions.TypedDict, total=False
):
    jobResults: typing.List[GoogleCloudTalentV4JobResult]

class CreateClientEventRequest(typing_extensions.TypedDict, total=False):
    clientEvent: ClientEvent

class GoogleCloudTalentV4CompensationInfo(typing_extensions.TypedDict, total=False):
    annualizedBaseCompensationRange: GoogleCloudTalentV4CompensationInfoCompensationRange
    entries: typing.List[GoogleCloudTalentV4CompensationInfoCompensationEntry]
    annualizedTotalCompensationRange: GoogleCloudTalentV4CompensationInfoCompensationRange

class NumericBucketingResult(typing_extensions.TypedDict, total=False):
    maxValue: float
    minValue: float
    counts: typing.List[BucketizedCount]

class SearchJobsResponse(typing_extensions.TypedDict, total=False):
    histogramQueryResults: typing.List[HistogramQueryResult]
    spellCorrection: SpellingCorrection
    totalSize: int
    broadenedQueryJobsCount: int
    nextPageToken: str
    histogramResults: HistogramResults
    metadata: ResponseMetadata
    matchingJobs: typing.List[MatchingJob]
    locationFilters: typing.List[Location]
    estimatedTotalSize: int

class Job(typing_extensions.TypedDict, total=False):
    department: str
    postingRegion: typing_extensions.Literal[
        "POSTING_REGION_UNSPECIFIED", "ADMINISTRATIVE_AREA", "NATION", "TELECOMMUTE"
    ]
    jobStartTime: str
    companyName: str
    degreeTypes: typing.List[str]
    postingUpdateTime: str
    derivedInfo: JobDerivedInfo
    processingOptions: ProcessingOptions
    responsibilities: str
    qualifications: str
    postingCreateTime: str
    visibility: typing_extensions.Literal[
        "VISIBILITY_UNSPECIFIED",
        "ACCOUNT_ONLY",
        "SHARED_WITH_GOOGLE",
        "SHARED_WITH_PUBLIC",
    ]
    customAttributes: typing.Dict[str, typing.Any]
    companyDisplayName: str
    postingExpireTime: str
    employmentTypes: typing.List[str]
    name: str
    promotionValue: int
    languageCode: str
    applicationInfo: ApplicationInfo
    jobLevel: typing_extensions.Literal[
        "JOB_LEVEL_UNSPECIFIED",
        "ENTRY_LEVEL",
        "EXPERIENCED",
        "MANAGER",
        "DIRECTOR",
        "EXECUTIVE",
    ]
    compensationInfo: CompensationInfo
    postingPublishTime: str
    addresses: typing.List[str]
    title: str
    description: str
    jobEndTime: str
    jobBenefits: typing.List[str]
    incentives: str
    requisitionId: str

class SpellingCorrection(typing_extensions.TypedDict, total=False):
    corrected: bool
    correctedText: str

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
    values: typing.Dict[str, typing.Any]

class LatLng(typing_extensions.TypedDict, total=False):
    latitude: float
    longitude: float

class CommuteFilter(typing_extensions.TypedDict, total=False):
    travelDuration: str
    startCoordinates: LatLng
    allowImpreciseAddresses: bool
    roadTraffic: typing_extensions.Literal[
        "ROAD_TRAFFIC_UNSPECIFIED", "TRAFFIC_FREE", "BUSY_HOUR"
    ]
    commuteMethod: typing_extensions.Literal[
        "COMMUTE_METHOD_UNSPECIFIED", "DRIVING", "TRANSIT", "WALKING", "CYCLING"
    ]
    departureTime: TimeOfDay

class CustomRankingInfo(typing_extensions.TypedDict, total=False):
    rankingExpression: str
    importanceLevel: typing_extensions.Literal[
        "IMPORTANCE_LEVEL_UNSPECIFIED",
        "NONE",
        "LOW",
        "MILD",
        "MEDIUM",
        "HIGH",
        "EXTREME",
    ]

class CreateCompanyRequest(typing_extensions.TypedDict, total=False):
    company: Company

class HistogramQueryResult(typing_extensions.TypedDict, total=False):
    histogramQuery: str
    histogram: typing.Dict[str, typing.Any]

class CompletionResult(typing_extensions.TypedDict, total=False):
    suggestion: str
    type: typing_extensions.Literal[
        "COMPLETION_TYPE_UNSPECIFIED", "JOB_TITLE", "COMPANY_NAME", "COMBINED"
    ]
    imageUri: str

class ClientEvent(typing_extensions.TypedDict, total=False):
    jobEvent: JobEvent
    requestId: str
    parentEventId: str
    extraInfo: typing.Dict[str, typing.Any]
    eventId: str
    createTime: str

class CustomAttributeHistogramResult(typing_extensions.TypedDict, total=False):
    key: str
    longValueHistogramResult: NumericBucketingResult
    stringValueHistogramResult: typing.Dict[str, typing.Any]

class JobQuery(typing_extensions.TypedDict, total=False):
    commuteFilter: CommuteFilter
    customAttributeFilter: str
    publishTimeRange: TimestampRange
    companyNames: typing.List[str]
    companyDisplayNames: typing.List[str]
    employmentTypes: typing.List[str]
    disableSpellCheck: bool
    queryLanguageCode: str
    jobCategories: typing.List[str]
    query: str
    compensationFilter: CompensationFilter
    languageCodes: typing.List[str]
    excludedJobs: typing.List[str]
    locationFilters: typing.List[LocationFilter]

class CreateJobRequest(typing_extensions.TypedDict, total=False):
    job: Job

class MatchingJob(typing_extensions.TypedDict, total=False):
    jobSummary: str
    jobTitleSnippet: str
    job: Job
    searchTextSnippet: str
    commuteInfo: CommuteInfo

class CompensationFilter(typing_extensions.TypedDict, total=False):
    type: typing_extensions.Literal[
        "FILTER_TYPE_UNSPECIFIED",
        "UNIT_ONLY",
        "UNIT_AND_AMOUNT",
        "ANNUALIZED_BASE_AMOUNT",
        "ANNUALIZED_TOTAL_AMOUNT",
    ]
    range: CompensationRange
    units: typing.List[str]
    includeJobsWithUnspecifiedCompensationRange: bool

class ProcessingOptions(typing_extensions.TypedDict, total=False):
    htmlSanitization: typing_extensions.Literal[
        "HTML_SANITIZATION_UNSPECIFIED",
        "HTML_SANITIZATION_DISABLED",
        "SIMPLE_FORMATTING_ONLY",
    ]
    disableStreetAddressResolution: bool

class CompensationHistogramResult(typing_extensions.TypedDict, total=False):
    result: NumericBucketingResult
    type: typing_extensions.Literal[
        "COMPENSATION_HISTOGRAM_REQUEST_TYPE_UNSPECIFIED",
        "BASE",
        "ANNUALIZED_BASE",
        "ANNUALIZED_TOTAL",
    ]

class GoogleCloudTalentV4CompensationInfoCompensationRange(
    typing_extensions.TypedDict, total=False
):
    minCompensation: Money
    maxCompensation: Money

class TimeOfDay(typing_extensions.TypedDict, total=False):
    hours: int
    minutes: int
    nanos: int
    seconds: int

class NamespacedDebugInput(typing_extensions.TypedDict, total=False):
    absolutelyForcedExpNames: typing.List[str]
    disableManualEnrollmentSelection: bool
    disableOrganicSelection: bool
    conditionallyForcedExpTags: typing.List[str]
    disableAutomaticEnrollmentSelection: bool
    disableExps: typing.List[int]
    absolutelyForcedExpTags: typing.List[str]
    conditionallyForcedExps: typing.List[int]
    disableExpTags: typing.List[str]
    forcedRollouts: typing.Dict[str, typing.Any]
    disableExpNames: typing.List[str]
    conditionallyForcedExpNames: typing.List[str]
    absolutelyForcedExps: typing.List[int]
    forcedFlags: typing.Dict[str, typing.Any]

class RequestMetadata(typing_extensions.TypedDict, total=False):
    userId: str
    domain: str
    deviceInfo: DeviceInfo
    sessionId: str

class GoogleCloudTalentV4JobDerivedInfo(typing_extensions.TypedDict, total=False):
    locations: typing.List[GoogleCloudTalentV4Location]
    jobCategories: typing.List[str]

class CompensationInfo(typing_extensions.TypedDict, total=False):
    annualizedBaseCompensationRange: CompensationRange
    entries: typing.List[CompensationEntry]
    annualizedTotalCompensationRange: CompensationRange

class CommuteInfo(typing_extensions.TypedDict, total=False):
    travelDuration: str
    jobLocation: Location

class Operation(typing_extensions.TypedDict, total=False):
    name: str
    error: Status
    metadata: typing.Dict[str, typing.Any]
    done: bool
    response: typing.Dict[str, typing.Any]

class CompensationRange(typing_extensions.TypedDict, total=False):
    minCompensation: Money
    maxCompensation: Money

class SearchJobsRequest(typing_extensions.TypedDict, total=False):
    offset: int
    orderBy: str
    pageSize: int
    customRankingInfo: CustomRankingInfo
    histogramQueries: typing.List[HistogramQuery]
    disableKeywordMatch: bool
    requestMetadata: RequestMetadata
    searchMode: typing_extensions.Literal[
        "SEARCH_MODE_UNSPECIFIED", "JOB_SEARCH", "FEATURED_JOB_SEARCH"
    ]
    pageToken: str
    jobQuery: JobQuery
    enableBroadening: bool
    jobView: typing_extensions.Literal[
        "JOB_VIEW_UNSPECIFIED",
        "JOB_VIEW_ID_ONLY",
        "JOB_VIEW_MINIMAL",
        "JOB_VIEW_SMALL",
        "JOB_VIEW_FULL",
    ]
    requirePreciseResultSize: bool
    histogramFacets: HistogramFacets
    diversificationLevel: typing_extensions.Literal[
        "DIVERSIFICATION_LEVEL_UNSPECIFIED", "DISABLED", "SIMPLE"
    ]

class Company(typing_extensions.TypedDict, total=False):
    externalId: str
    headquartersAddress: str
    displayName: str
    derivedInfo: CompanyDerivedInfo
    eeoText: str
    name: str
    imageUri: str
    hiringAgency: bool
    websiteUri: str
    careerSiteUri: str
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
    keywordSearchableJobCustomAttributes: typing.List[str]
    suspended: bool

class HistogramResults(typing_extensions.TypedDict, total=False):
    simpleHistogramResults: typing.List[HistogramResult]
    customAttributeHistogramResults: typing.List[CustomAttributeHistogramResult]
    compensationHistogramResults: typing.List[CompensationHistogramResult]

class GoogleCloudTalentV4JobResult(typing_extensions.TypedDict, total=False):
    job: GoogleCloudTalentV4Job
    status: Status

class CompanyDerivedInfo(typing_extensions.TypedDict, total=False):
    headquartersLocation: Location

class ApplicationInfo(typing_extensions.TypedDict, total=False):
    uris: typing.List[str]
    instruction: str
    emails: typing.List[str]

class HistogramQuery(typing_extensions.TypedDict, total=False):
    histogramQuery: str

class ListCompaniesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    metadata: ResponseMetadata
    companies: typing.List[Company]

class Money(typing_extensions.TypedDict, total=False):
    nanos: int
    currencyCode: str
    units: str

class HistogramFacets(typing_extensions.TypedDict, total=False):
    compensationHistogramFacets: typing.List[CompensationHistogramRequest]
    simpleHistogramFacets: typing.List[str]
    customAttributeHistogramFacets: typing.List[CustomAttributeHistogramRequest]

class DeviceInfo(typing_extensions.TypedDict, total=False):
    deviceType: typing_extensions.Literal[
        "DEVICE_TYPE_UNSPECIFIED", "WEB", "MOBILE_WEB", "ANDROID", "IOS", "BOT", "OTHER"
    ]
    id: str

class GoogleCloudTalentV4Job(typing_extensions.TypedDict, total=False):
    addresses: typing.List[str]
    postingExpireTime: str
    postingCreateTime: str
    companyDisplayName: str
    jobLevel: typing_extensions.Literal[
        "JOB_LEVEL_UNSPECIFIED",
        "ENTRY_LEVEL",
        "EXPERIENCED",
        "MANAGER",
        "DIRECTOR",
        "EXECUTIVE",
    ]
    qualifications: str
    title: str
    customAttributes: typing.Dict[str, typing.Any]
    jobEndTime: str
    incentives: str
    jobStartTime: str
    compensationInfo: GoogleCloudTalentV4CompensationInfo
    department: str
    degreeTypes: typing.List[str]
    responsibilities: str
    postingUpdateTime: str
    promotionValue: int
    visibility: typing_extensions.Literal[
        "VISIBILITY_UNSPECIFIED",
        "ACCOUNT_ONLY",
        "SHARED_WITH_GOOGLE",
        "SHARED_WITH_PUBLIC",
    ]
    requisitionId: str
    company: str
    languageCode: str
    applicationInfo: GoogleCloudTalentV4JobApplicationInfo
    processingOptions: GoogleCloudTalentV4JobProcessingOptions
    postingRegion: typing_extensions.Literal[
        "POSTING_REGION_UNSPECIFIED", "ADMINISTRATIVE_AREA", "NATION", "TELECOMMUTE"
    ]
    derivedInfo: GoogleCloudTalentV4JobDerivedInfo
    jobBenefits: typing.List[str]
    employmentTypes: typing.List[str]
    postingPublishTime: str
    description: str
    name: str

class BucketizedCount(typing_extensions.TypedDict, total=False):
    range: BucketRange
    count: int

class GoogleCloudTalentV4JobProcessingOptions(typing_extensions.TypedDict, total=False):
    htmlSanitization: typing_extensions.Literal[
        "HTML_SANITIZATION_UNSPECIFIED",
        "HTML_SANITIZATION_DISABLED",
        "SIMPLE_FORMATTING_ONLY",
    ]
    disableStreetAddressResolution: bool

class LocationFilter(typing_extensions.TypedDict, total=False):
    regionCode: str
    latLng: LatLng
    telecommutePreference: typing_extensions.Literal[
        "TELECOMMUTE_PREFERENCE_UNSPECIFIED",
        "TELECOMMUTE_EXCLUDED",
        "TELECOMMUTE_ALLOWED",
    ]
    distanceInMiles: float
    address: str

class BatchDeleteJobsRequest(typing_extensions.TypedDict, total=False):
    filter: str

class GoogleCloudTalentV4BatchOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    totalCount: int
    endTime: str
    failureCount: int
    successCount: int
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "INITIALIZING",
        "PROCESSING",
        "SUCCEEDED",
        "FAILED",
        "CANCELLING",
        "CANCELLED",
    ]
    updateTime: str
    stateDescription: str
    createTime: str

class PostalAddress(typing_extensions.TypedDict, total=False):
    organization: str
    addressLines: typing.List[str]
    regionCode: str
    postalCode: str
    recipients: typing.List[str]
    revision: int
    administrativeArea: str
    languageCode: str
    locality: str
    sortingCode: str
    sublocality: str

class JobEvent(typing_extensions.TypedDict, total=False):
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
    jobs: typing.List[str]

class TimestampRange(typing_extensions.TypedDict, total=False):
    endTime: str
    startTime: str

class ResponseMetadata(typing_extensions.TypedDict, total=False):
    requestId: str

class MendelDebugInput(typing_extensions.TypedDict, total=False):
    namespacedDebugInput: typing.Dict[str, typing.Any]

class GoogleCloudTalentV4BatchUpdateJobsResponse(
    typing_extensions.TypedDict, total=False
):
    jobResults: typing.List[GoogleCloudTalentV4JobResult]

class GoogleCloudTalentV4Location(typing_extensions.TypedDict, total=False):
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
    latLng: LatLng
    postalAddress: PostalAddress
    radiusMiles: float

class Location(typing_extensions.TypedDict, total=False):
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
    radiusInMiles: float
    postalAddress: PostalAddress
    latLng: LatLng

class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: typing.List[typing.Dict[str, typing.Any]]
    message: str

class UpdateCompanyRequest(typing_extensions.TypedDict, total=False):
    updateMask: str
    company: Company

class UpdateJobRequest(typing_extensions.TypedDict, total=False):
    updateMask: str
    job: Job
