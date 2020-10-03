import typing

import typing_extensions

class Job(typing_extensions.TypedDict, total=False):
    responsibilities: str
    companyName: str
    postingUpdateTime: str
    description: str
    jobBenefits: typing.List[str]
    postingExpireTime: str
    jobEndTime: str
    visibility: typing_extensions.Literal[
        "VISIBILITY_UNSPECIFIED",
        "ACCOUNT_ONLY",
        "SHARED_WITH_GOOGLE",
        "SHARED_WITH_PUBLIC",
    ]
    postingPublishTime: str
    qualifications: str
    employmentTypes: typing.List[str]
    name: str
    languageCode: str
    companyDisplayName: str
    processingOptions: ProcessingOptions
    department: str
    derivedInfo: JobDerivedInfo
    jobStartTime: str
    promotionValue: int
    title: str
    customAttributes: typing.Dict[str, typing.Any]
    postingCreateTime: str
    postingRegion: typing_extensions.Literal[
        "POSTING_REGION_UNSPECIFIED", "ADMINISTRATIVE_AREA", "NATION", "TELECOMMUTE"
    ]
    jobLevel: typing_extensions.Literal[
        "JOB_LEVEL_UNSPECIFIED",
        "ENTRY_LEVEL",
        "EXPERIENCED",
        "MANAGER",
        "DIRECTOR",
        "EXECUTIVE",
    ]
    incentives: str
    degreeTypes: typing.List[str]
    compensationInfo: CompensationInfo
    requisitionId: str
    applicationInfo: ApplicationInfo
    addresses: typing.List[str]

class GoogleCloudTalentV4Job(typing_extensions.TypedDict, total=False):
    visibility: typing_extensions.Literal[
        "VISIBILITY_UNSPECIFIED",
        "ACCOUNT_ONLY",
        "SHARED_WITH_GOOGLE",
        "SHARED_WITH_PUBLIC",
    ]
    applicationInfo: GoogleCloudTalentV4JobApplicationInfo
    postingPublishTime: str
    postingCreateTime: str
    languageCode: str
    jobStartTime: str
    jobLevel: typing_extensions.Literal[
        "JOB_LEVEL_UNSPECIFIED",
        "ENTRY_LEVEL",
        "EXPERIENCED",
        "MANAGER",
        "DIRECTOR",
        "EXECUTIVE",
    ]
    postingUpdateTime: str
    incentives: str
    responsibilities: str
    jobEndTime: str
    qualifications: str
    processingOptions: GoogleCloudTalentV4JobProcessingOptions
    derivedInfo: GoogleCloudTalentV4JobDerivedInfo
    promotionValue: int
    addresses: typing.List[str]
    customAttributes: typing.Dict[str, typing.Any]
    postingExpireTime: str
    requisitionId: str
    companyDisplayName: str
    title: str
    company: str
    name: str
    degreeTypes: typing.List[str]
    compensationInfo: GoogleCloudTalentV4CompensationInfo
    jobBenefits: typing.List[str]
    postingRegion: typing_extensions.Literal[
        "POSTING_REGION_UNSPECIFIED", "ADMINISTRATIVE_AREA", "NATION", "TELECOMMUTE"
    ]
    employmentTypes: typing.List[str]
    description: str
    department: str

class GoogleCloudTalentV4CompensationInfoCompensationRange(
    typing_extensions.TypedDict, total=False
):
    minCompensation: Money
    maxCompensation: Money

class GoogleCloudTalentV4JobResult(typing_extensions.TypedDict, total=False):
    job: GoogleCloudTalentV4Job
    status: Status

class BucketizedCount(typing_extensions.TypedDict, total=False):
    count: int
    range: BucketRange

class Empty(typing_extensions.TypedDict, total=False): ...

class LocationFilter(typing_extensions.TypedDict, total=False):
    latLng: LatLng
    address: str
    regionCode: str
    distanceInMiles: float
    telecommutePreference: typing_extensions.Literal[
        "TELECOMMUTE_PREFERENCE_UNSPECIFIED",
        "TELECOMMUTE_EXCLUDED",
        "TELECOMMUTE_ALLOWED",
    ]

class GoogleCloudTalentV4JobProcessingOptions(typing_extensions.TypedDict, total=False):
    disableStreetAddressResolution: bool
    htmlSanitization: typing_extensions.Literal[
        "HTML_SANITIZATION_UNSPECIFIED",
        "HTML_SANITIZATION_DISABLED",
        "SIMPLE_FORMATTING_ONLY",
    ]

class GoogleCloudTalentV4BatchUpdateJobsResponse(
    typing_extensions.TypedDict, total=False
):
    jobResults: typing.List[GoogleCloudTalentV4JobResult]

class SearchJobsResponse(typing_extensions.TypedDict, total=False):
    histogramResults: HistogramResults
    locationFilters: typing.List[Location]
    metadata: ResponseMetadata
    nextPageToken: str
    estimatedTotalSize: int
    spellCorrection: SpellingCorrection
    broadenedQueryJobsCount: int
    totalSize: int
    matchingJobs: typing.List[MatchingJob]

class CreateCompanyRequest(typing_extensions.TypedDict, total=False):
    company: Company

class LatLng(typing_extensions.TypedDict, total=False):
    latitude: float
    longitude: float

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

class HistogramResults(typing_extensions.TypedDict, total=False):
    compensationHistogramResults: typing.List[CompensationHistogramResult]
    simpleHistogramResults: typing.List[HistogramResult]
    customAttributeHistogramResults: typing.List[CustomAttributeHistogramResult]

class GoogleCloudTalentV4JobApplicationInfo(typing_extensions.TypedDict, total=False):
    emails: typing.List[str]
    instruction: str
    uris: typing.List[str]

class Status(typing_extensions.TypedDict, total=False):
    code: int
    message: str
    details: typing.List[typing.Dict[str, typing.Any]]

class CompensationInfo(typing_extensions.TypedDict, total=False):
    annualizedTotalCompensationRange: CompensationRange
    entries: typing.List[CompensationEntry]
    annualizedBaseCompensationRange: CompensationRange

class ProcessingOptions(typing_extensions.TypedDict, total=False):
    disableStreetAddressResolution: bool
    htmlSanitization: typing_extensions.Literal[
        "HTML_SANITIZATION_UNSPECIFIED",
        "HTML_SANITIZATION_DISABLED",
        "SIMPLE_FORMATTING_ONLY",
    ]

class CustomAttributeHistogramResult(typing_extensions.TypedDict, total=False):
    longValueHistogramResult: NumericBucketingResult
    stringValueHistogramResult: typing.Dict[str, typing.Any]
    key: str

class JobQuery(typing_extensions.TypedDict, total=False):
    publishTimeRange: TimestampRange
    query: str
    companyDisplayNames: typing.List[str]
    disableSpellCheck: bool
    languageCodes: typing.List[str]
    commuteFilter: CommuteFilter
    queryLanguageCode: str
    companyNames: typing.List[str]
    employmentTypes: typing.List[str]
    locationFilters: typing.List[LocationFilter]
    compensationFilter: CompensationFilter
    customAttributeFilter: str
    jobCategories: typing.List[str]

class CustomAttribute(typing_extensions.TypedDict, total=False):
    longValues: typing.List[str]
    filterable: bool
    stringValues: typing.List[str]

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

class ResponseMetadata(typing_extensions.TypedDict, total=False):
    requestId: str

class CompensationEntry(typing_extensions.TypedDict, total=False):
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
    amount: Money
    description: str
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
    range: CompensationRange

class CustomAttributeHistogramRequest(typing_extensions.TypedDict, total=False):
    key: str
    stringValueHistogram: bool
    longValueHistogramBucketingOption: NumericBucketingOption

class CreateJobRequest(typing_extensions.TypedDict, total=False):
    job: Job

class HistogramFacets(typing_extensions.TypedDict, total=False):
    simpleHistogramFacets: typing.List[str]
    customAttributeHistogramFacets: typing.List[CustomAttributeHistogramRequest]
    compensationHistogramFacets: typing.List[CompensationHistogramRequest]

class GoogleCloudTalentV4JobDerivedInfo(typing_extensions.TypedDict, total=False):
    locations: typing.List[GoogleCloudTalentV4Location]
    jobCategories: typing.List[str]

class CompensationHistogramResult(typing_extensions.TypedDict, total=False):
    type: typing_extensions.Literal[
        "COMPENSATION_HISTOGRAM_REQUEST_TYPE_UNSPECIFIED",
        "BASE",
        "ANNUALIZED_BASE",
        "ANNUALIZED_TOTAL",
    ]
    result: NumericBucketingResult

class GoogleCloudTalentV4BatchCreateJobsResponse(
    typing_extensions.TypedDict, total=False
):
    jobResults: typing.List[GoogleCloudTalentV4JobResult]

class NumericBucketingOption(typing_extensions.TypedDict, total=False):
    requiresMinMax: bool
    bucketBounds: typing.List[float]

class TimeOfDay(typing_extensions.TypedDict, total=False):
    seconds: int
    minutes: int
    hours: int
    nanos: int

class MendelDebugInput(typing_extensions.TypedDict, total=False):
    namespacedDebugInput: typing.Dict[str, typing.Any]

class GoogleCloudTalentV4CompensationInfo(typing_extensions.TypedDict, total=False):
    annualizedBaseCompensationRange: GoogleCloudTalentV4CompensationInfoCompensationRange
    annualizedTotalCompensationRange: GoogleCloudTalentV4CompensationInfoCompensationRange
    entries: typing.List[GoogleCloudTalentV4CompensationInfoCompensationEntry]

class CompensationRange(typing_extensions.TypedDict, total=False):
    minCompensation: Money
    maxCompensation: Money

class PostalAddress(typing_extensions.TypedDict, total=False):
    sublocality: str
    postalCode: str
    languageCode: str
    organization: str
    recipients: typing.List[str]
    regionCode: str
    locality: str
    addressLines: typing.List[str]
    administrativeArea: str
    sortingCode: str
    revision: int

class ListJobsResponse(typing_extensions.TypedDict, total=False):
    metadata: ResponseMetadata
    jobs: typing.List[Job]
    nextPageToken: str

class UpdateCompanyRequest(typing_extensions.TypedDict, total=False):
    company: Company
    updateMask: str

class Money(typing_extensions.TypedDict, total=False):
    units: str
    currencyCode: str
    nanos: int

BucketRange = typing_extensions.TypedDict(
    "BucketRange",
    {
        "to": float,
        "from": float,
    },
    total=False,
)

class MatchingJob(typing_extensions.TypedDict, total=False):
    commuteInfo: CommuteInfo
    jobSummary: str
    searchTextSnippet: str
    job: Job
    jobTitleSnippet: str

class NumericBucketingResult(typing_extensions.TypedDict, total=False):
    counts: typing.List[BucketizedCount]
    minValue: float
    maxValue: float

class SpellingCorrection(typing_extensions.TypedDict, total=False):
    correctedText: str
    corrected: bool

class ClientEvent(typing_extensions.TypedDict, total=False):
    requestId: str
    parentEventId: str
    createTime: str
    jobEvent: JobEvent
    eventId: str
    extraInfo: typing.Dict[str, typing.Any]

class JobDerivedInfo(typing_extensions.TypedDict, total=False):
    locations: typing.List[Location]
    jobCategories: typing.List[str]

class TimestampRange(typing_extensions.TypedDict, total=False):
    endTime: str
    startTime: str

class CompanyDerivedInfo(typing_extensions.TypedDict, total=False):
    headquartersLocation: Location

class CompensationFilter(typing_extensions.TypedDict, total=False):
    range: CompensationRange
    units: typing.List[str]
    includeJobsWithUnspecifiedCompensationRange: bool
    type: typing_extensions.Literal[
        "FILTER_TYPE_UNSPECIFIED",
        "UNIT_ONLY",
        "UNIT_AND_AMOUNT",
        "ANNUALIZED_BASE_AMOUNT",
        "ANNUALIZED_TOTAL_AMOUNT",
    ]

class GoogleCloudTalentV4CompensationInfoCompensationEntry(
    typing_extensions.TypedDict, total=False
):
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
    range: GoogleCloudTalentV4CompensationInfoCompensationRange
    description: str
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
    expectedUnitsPerYear: float

class ListCompaniesResponse(typing_extensions.TypedDict, total=False):
    companies: typing.List[Company]
    metadata: ResponseMetadata
    nextPageToken: str

class DeviceInfo(typing_extensions.TypedDict, total=False):
    id: str
    deviceType: typing_extensions.Literal[
        "DEVICE_TYPE_UNSPECIFIED", "WEB", "MOBILE_WEB", "ANDROID", "IOS", "BOT", "OTHER"
    ]

class GoogleCloudTalentV4BatchOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    endTime: str
    successCount: int
    failureCount: int
    totalCount: int
    updateTime: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "INITIALIZING",
        "PROCESSING",
        "SUCCEEDED",
        "FAILED",
        "CANCELLING",
        "CANCELLED",
    ]
    stateDescription: str
    createTime: str

class BatchDeleteJobsRequest(typing_extensions.TypedDict, total=False):
    filter: str

class ApplicationInfo(typing_extensions.TypedDict, total=False):
    uris: typing.List[str]
    instruction: str
    emails: typing.List[str]

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
    latLng: LatLng
    postalAddress: PostalAddress
    radiusInMiles: float

class RequestMetadata(typing_extensions.TypedDict, total=False):
    domain: str
    deviceInfo: DeviceInfo
    userId: str
    sessionId: str

class SearchJobsRequest(typing_extensions.TypedDict, total=False):
    jobView: typing_extensions.Literal[
        "JOB_VIEW_UNSPECIFIED",
        "JOB_VIEW_ID_ONLY",
        "JOB_VIEW_MINIMAL",
        "JOB_VIEW_SMALL",
        "JOB_VIEW_FULL",
    ]
    diversificationLevel: typing_extensions.Literal[
        "DIVERSIFICATION_LEVEL_UNSPECIFIED", "DISABLED", "SIMPLE"
    ]
    histogramFacets: HistogramFacets
    offset: int
    enableBroadening: bool
    disableKeywordMatch: bool
    requirePreciseResultSize: bool
    requestMetadata: RequestMetadata
    orderBy: str
    jobQuery: JobQuery
    pageToken: str
    searchMode: typing_extensions.Literal[
        "SEARCH_MODE_UNSPECIFIED", "JOB_SEARCH", "FEATURED_JOB_SEARCH"
    ]
    pageSize: int

class Company(typing_extensions.TypedDict, total=False):
    displayName: str
    careerSiteUri: str
    externalId: str
    keywordSearchableJobCustomAttributes: typing.List[str]
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
    eeoText: str
    imageUri: str
    headquartersAddress: str
    suspended: bool
    websiteUri: str
    name: str
    hiringAgency: bool
    derivedInfo: CompanyDerivedInfo

class NamespacedDebugInput(typing_extensions.TypedDict, total=False):
    conditionallyForcedExpNames: typing.List[str]
    disableExpNames: typing.List[str]
    disableExpTags: typing.List[str]
    conditionallyForcedExps: typing.List[int]
    disableOrganicSelection: bool
    absolutelyForcedExpNames: typing.List[str]
    disableExps: typing.List[int]
    absolutelyForcedExpTags: typing.List[str]
    forcedFlags: typing.Dict[str, typing.Any]
    conditionallyForcedExpTags: typing.List[str]
    absolutelyForcedExps: typing.List[int]
    forcedRollouts: typing.Dict[str, typing.Any]
    disableAutomaticEnrollmentSelection: bool
    disableManualEnrollmentSelection: bool

class UpdateJobRequest(typing_extensions.TypedDict, total=False):
    updateMask: str
    job: Job

class CommuteInfo(typing_extensions.TypedDict, total=False):
    travelDuration: str
    jobLocation: Location

class CompleteQueryResponse(typing_extensions.TypedDict, total=False):
    completionResults: typing.List[CompletionResult]
    metadata: ResponseMetadata

class CommuteFilter(typing_extensions.TypedDict, total=False):
    roadTraffic: typing_extensions.Literal[
        "ROAD_TRAFFIC_UNSPECIFIED", "TRAFFIC_FREE", "BUSY_HOUR"
    ]
    allowImpreciseAddresses: bool
    travelDuration: str
    commuteMethod: typing_extensions.Literal[
        "COMMUTE_METHOD_UNSPECIFIED", "DRIVING", "TRANSIT"
    ]
    startCoordinates: LatLng
    departureTime: TimeOfDay

class GoogleCloudTalentV4Location(typing_extensions.TypedDict, total=False):
    radiusMiles: float
    postalAddress: PostalAddress
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

class GoogleCloudTalentV4CustomAttribute(typing_extensions.TypedDict, total=False):
    keywordSearchable: bool
    filterable: bool
    longValues: typing.List[str]
    stringValues: typing.List[str]

class CompletionResult(typing_extensions.TypedDict, total=False):
    suggestion: str
    imageUri: str
    type: typing_extensions.Literal[
        "COMPLETION_TYPE_UNSPECIFIED", "JOB_TITLE", "COMPANY_NAME", "COMBINED"
    ]

class HistogramResult(typing_extensions.TypedDict, total=False):
    values: typing.Dict[str, typing.Any]
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

class CreateClientEventRequest(typing_extensions.TypedDict, total=False):
    clientEvent: ClientEvent
