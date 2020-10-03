import typing

import typing_extensions

class Company(typing_extensions.TypedDict, total=False):
    companyInfoSources: typing.List[CompanyInfoSource]
    eeoText: str
    distributorBillingCompanyId: str
    website: str
    title: str
    imageUrl: str
    distributorCompanyId: str
    name: str
    companySize: typing_extensions.Literal[
        "COMPANY_SIZE_UNSPECIFIED",
        "MINI",
        "SMALL",
        "SMEDIUM",
        "MEDIUM",
        "BIG",
        "BIGGER",
        "GIANT",
    ]
    structuredCompanyHqLocation: JobLocation
    hiringAgency: bool
    hqLocation: str
    displayName: str
    careerPageLink: str
    disableLocationOptimization: bool
    keywordSearchableCustomFields: typing.List[int]
    suspended: bool
    keywordSearchableCustomAttributes: typing.List[str]

class CompensationHistogramRequest(typing_extensions.TypedDict, total=False):
    bucketingOption: NumericBucketingOption
    type: typing_extensions.Literal[
        "COMPENSATION_HISTOGRAM_REQUEST_TYPE_UNSPECIFIED",
        "BASE",
        "ANNUALIZED_BASE",
        "ANNUALIZED_TOTAL",
    ]

class Empty(typing_extensions.TypedDict, total=False): ...

class GoogleCloudTalentV4JobDerivedInfo(typing_extensions.TypedDict, total=False):
    locations: typing.List[GoogleCloudTalentV4Location]
    jobCategories: typing.List[str]

class SearchJobsResponse(typing_extensions.TypedDict, total=False):
    totalSize: str
    numJobsFromBroadenedQuery: int
    jobView: typing_extensions.Literal[
        "JOB_VIEW_UNSPECIFIED", "SMALL", "MINIMAL", "FULL"
    ]
    histogramResults: HistogramResults
    metadata: ResponseMetadata
    nextPageToken: str
    appliedJobLocationFilters: typing.List[JobLocation]
    spellResult: SpellingCorrection
    appliedCommuteFilter: CommutePreference
    matchingJobs: typing.List[MatchingJob]
    estimatedTotalSize: str

class Date(typing_extensions.TypedDict, total=False):
    day: int
    month: int
    year: int

class ResponseMetadata(typing_extensions.TypedDict, total=False):
    requestId: str
    mode: typing_extensions.Literal[
        "SEARCH_MODE_UNSPECIFIED",
        "JOB_SEARCH",
        "FEATURED_JOB_SEARCH",
        "EMAIL_ALERT_SEARCH",
    ]
    experimentIdList: typing.List[int]

class Money(typing_extensions.TypedDict, total=False):
    currencyCode: str
    units: str
    nanos: int

class Status(typing_extensions.TypedDict, total=False):
    message: str
    details: typing.List[typing.Dict[str, typing.Any]]
    code: int

class GetHistogramRequest(typing_extensions.TypedDict, total=False):
    allowBroadening: bool
    searchTypes: typing.List[str]
    filters: JobFilters
    requestMetadata: RequestMetadata
    query: JobQuery

class HistogramResults(typing_extensions.TypedDict, total=False):
    compensationHistogramResults: typing.List[CompensationHistogramResult]
    customAttributeHistogramResults: typing.List[CustomAttributeHistogramResult]
    simpleHistogramResults: typing.List[HistogramResult]

class MatchingJob(typing_extensions.TypedDict, total=False):
    commuteInfo: CommuteInfo
    jobTitleSnippet: str
    jobSummary: str
    job: Job
    searchTextSnippet: str

class MendelDebugInput(typing_extensions.TypedDict, total=False):
    namespacedDebugInput: typing.Dict[str, typing.Any]

class JobQuery(typing_extensions.TypedDict, total=False):
    locationFilters: typing.List[LocationFilter]
    customAttributeFilter: str
    companyNames: typing.List[str]
    disableSpellCheck: bool
    languageCodes: typing.List[str]
    compensationFilter: CompensationFilter
    query: str
    companyDisplayNames: typing.List[str]
    commuteFilter: CommutePreference
    publishDateRange: typing_extensions.Literal[
        "DATE_RANGE_UNSPECIFIED",
        "PAST_24_HOURS",
        "PAST_WEEK",
        "PAST_MONTH",
        "PAST_YEAR",
        "PAST_3_DAYS",
    ]
    employmentTypes: typing.List[str]
    categories: typing.List[str]

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
    radiusMiles: float
    postalAddress: PostalAddress
    latLng: LatLng

BucketRange = typing_extensions.TypedDict(
    "BucketRange",
    {
        "to": float,
        "from": float,
    },
    total=False,
)

class HistogramFacets(typing_extensions.TypedDict, total=False):
    compensationHistogramFacets: typing.List[CompensationHistogramRequest]
    simpleHistogramFacets: typing.List[str]
    customAttributeHistogramFacets: typing.List[CustomAttributeHistogramRequest]

class ExtendedCompensationInfoCompensationEntry(
    typing_extensions.TypedDict, total=False
):
    description: str
    range: ExtendedCompensationInfoCompensationRange
    unspecified: bool
    expectedUnitsPerYear: ExtendedCompensationInfoDecimal
    unit: typing_extensions.Literal[
        "EXTENDED_COMPENSATION_UNIT_UNSPECIFIED",
        "HOURLY",
        "DAILY",
        "WEEKLY",
        "MONTHLY",
        "YEARLY",
        "ONE_TIME",
        "OTHER_COMPENSATION_UNIT",
    ]
    type: typing_extensions.Literal[
        "EXTENDED_COMPENSATION_TYPE_UNSPECIFIED",
        "BASE",
        "BONUS",
        "SIGNING_BONUS",
        "EQUITY",
        "PROFIT_SHARING",
        "COMMISSIONS",
        "TIPS",
        "OTHER_COMPENSATION_TYPE",
    ]
    amount: ExtendedCompensationInfoDecimal

class DeviceInfo(typing_extensions.TypedDict, total=False):
    id: str
    deviceType: typing_extensions.Literal[
        "DEVICE_TYPE_UNSPECIFIED", "WEB", "MOBILE_WEB", "ANDROID", "IOS", "BOT", "OTHER"
    ]

class NumericBucketingOption(typing_extensions.TypedDict, total=False):
    bucketBounds: typing.List[float]
    requiresMinMax: bool

class LatLng(typing_extensions.TypedDict, total=False):
    latitude: float
    longitude: float

class CompensationEntry(typing_extensions.TypedDict, total=False):
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
    amount: Money
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
    description: str

class CompleteQueryResponse(typing_extensions.TypedDict, total=False):
    completionResults: typing.List[CompletionResult]
    metadata: ResponseMetadata

class CommutePreference(typing_extensions.TypedDict, total=False):
    method: typing_extensions.Literal[
        "COMMUTE_METHOD_UNSPECIFIED", "DRIVING", "TRANSIT"
    ]
    travelTime: str
    startLocation: LatLng
    roadTraffic: typing_extensions.Literal[
        "ROAD_TRAFFIC_UNSPECIFIED", "TRAFFIC_FREE", "BUSY_HOUR"
    ]
    allowNonStreetLevelAddress: bool
    departureHourLocal: int

class CustomAttributeHistogramRequest(typing_extensions.TypedDict, total=False):
    stringValueHistogram: bool
    key: str
    longValueHistogramBucketingOption: NumericBucketingOption

class Job(typing_extensions.TypedDict, total=False):
    educationLevels: typing.List[str]
    description: str
    updateTime: str
    applicationUrls: typing.List[str]
    applicationEmailList: typing.List[str]
    incentives: str
    publishDate: Date
    languageCode: str
    department: str
    referenceUrl: str
    expiryDate: Date
    compensationInfo: CompensationInfo
    visibility: typing_extensions.Literal[
        "JOB_VISIBILITY_UNSPECIFIED", "PRIVATE", "GOOGLE", "PUBLIC"
    ]
    customAttributes: typing.Dict[str, typing.Any]
    qualifications: str
    companyName: str
    locations: typing.List[str]
    jobLocations: typing.List[JobLocation]
    requisitionId: str
    unindexedCustomFields: typing.Dict[str, typing.Any]
    filterableCustomFields: typing.Dict[str, typing.Any]
    name: str
    distributorCompanyId: str
    companyDisplayName: str
    promotionValue: int
    region: typing_extensions.Literal[
        "REGION_UNSPECIFIED", "STATE_WIDE", "NATION_WIDE", "TELECOMMUTE"
    ]
    startDate: Date
    expireTime: str
    createTime: str
    benefits: typing.List[str]
    endDate: Date
    applicationInstruction: str
    employmentTypes: typing.List[str]
    responsibilities: str
    extendedCompensationInfo: ExtendedCompensationInfo
    level: typing_extensions.Literal[
        "JOB_LEVEL_UNSPECIFIED",
        "ENTRY_LEVEL",
        "EXPERIENCED",
        "MANAGER",
        "DIRECTOR",
        "EXECUTIVE",
    ]
    jobTitle: str
    companyTitle: str

class GoogleCloudTalentV4CustomAttribute(typing_extensions.TypedDict, total=False):
    stringValues: typing.List[str]
    keywordSearchable: bool
    longValues: typing.List[str]
    filterable: bool

class BucketizedCount(typing_extensions.TypedDict, total=False):
    range: BucketRange
    count: int

class ListCompaniesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    companies: typing.List[Company]
    metadata: ResponseMetadata

class Filter(typing_extensions.TypedDict, total=False):
    requisitionId: str

class JobProcessingOptions(typing_extensions.TypedDict, total=False):
    disableStreetAddressResolution: bool
    htmlSanitization: typing_extensions.Literal[
        "HTML_SANITIZATION_UNSPECIFIED",
        "HTML_SANITIZATION_DISABLED",
        "SIMPLE_FORMATTING_ONLY",
    ]

class CompensationInfo(typing_extensions.TypedDict, total=False):
    annualizedTotalCompensationRange: CompensationRange
    type: typing_extensions.Literal[
        "JOB_COMPENSATION_TYPE_UNSPECIFIED",
        "HOURLY",
        "SALARY",
        "PER_PROJECT",
        "COMMISSION",
        "OTHER_TYPE",
    ]
    entries: typing.List[CompensationEntry]
    max: Money
    amount: Money
    annualizedBaseCompensationRange: CompensationRange
    min: Money

class GoogleCloudTalentV4JobApplicationInfo(typing_extensions.TypedDict, total=False):
    emails: typing.List[str]
    uris: typing.List[str]
    instruction: str

class GoogleCloudTalentV4BatchUpdateJobsResponse(
    typing_extensions.TypedDict, total=False
):
    jobResults: typing.List[GoogleCloudTalentV4JobResult]

class HistogramResult(typing_extensions.TypedDict, total=False):
    searchType: typing_extensions.Literal[
        "JOB_FIELD_UNSPECIFIED",
        "COMPANY_ID",
        "EMPLOYMENT_TYPE",
        "COMPANY_SIZE",
        "DATE_PUBLISHED",
        "CUSTOM_FIELD_1",
        "CUSTOM_FIELD_2",
        "CUSTOM_FIELD_3",
        "CUSTOM_FIELD_4",
        "CUSTOM_FIELD_5",
        "CUSTOM_FIELD_6",
        "CUSTOM_FIELD_7",
        "CUSTOM_FIELD_8",
        "CUSTOM_FIELD_9",
        "CUSTOM_FIELD_10",
        "CUSTOM_FIELD_11",
        "CUSTOM_FIELD_12",
        "CUSTOM_FIELD_13",
        "CUSTOM_FIELD_14",
        "CUSTOM_FIELD_15",
        "CUSTOM_FIELD_16",
        "CUSTOM_FIELD_17",
        "CUSTOM_FIELD_18",
        "CUSTOM_FIELD_19",
        "CUSTOM_FIELD_20",
        "EDUCATION_LEVEL",
        "EXPERIENCE_LEVEL",
        "ADMIN1",
        "COUNTRY",
        "CITY",
        "LOCALE",
        "LANGUAGE",
        "CATEGORY",
        "CITY_COORDINATE",
        "ADMIN1_COUNTRY",
        "COMPANY_TITLE",
        "COMPANY_DISPLAY_NAME",
        "BASE_COMPENSATION_UNIT",
    ]
    values: typing.Dict[str, typing.Any]

class StringValues(typing_extensions.TypedDict, total=False):
    values: typing.List[str]

class BatchDeleteJobsRequest(typing_extensions.TypedDict, total=False):
    filter: str

class ExtendedCompensationFilter(typing_extensions.TypedDict, total=False):
    includeJobWithUnspecifiedCompensationRange: bool
    currency: str
    compensationUnits: typing.List[str]
    type: typing_extensions.Literal[
        "FILTER_TYPE_UNSPECIFIED",
        "UNIT_ONLY",
        "UNIT_AND_AMOUNT",
        "ANNUALIZED_BASE_AMOUNT",
        "ANNUALIZED_TOTAL_AMOUNT",
    ]
    compensationRange: ExtendedCompensationInfoCompensationRange

class CompensationFilter(typing_extensions.TypedDict, total=False):
    units: typing.List[str]
    type: typing_extensions.Literal[
        "FILTER_TYPE_UNSPECIFIED",
        "UNIT_ONLY",
        "UNIT_AND_AMOUNT",
        "ANNUALIZED_BASE_AMOUNT",
        "ANNUALIZED_TOTAL_AMOUNT",
    ]
    range: CompensationRange
    includeJobsWithUnspecifiedCompensationRange: bool

class CustomAttributeHistogramResult(typing_extensions.TypedDict, total=False):
    key: str
    stringValueHistogramResult: typing.Dict[str, typing.Any]
    longValueHistogramResult: NumericBucketingResult

class SpellingCorrection(typing_extensions.TypedDict, total=False):
    corrected: bool
    correctedText: str

class JobLocation(typing_extensions.TypedDict, total=False):
    latLng: LatLng
    postalAddress: PostalAddress
    radiusMeters: float
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

class UpdateJobRequest(typing_extensions.TypedDict, total=False):
    disableStreetAddressResolution: bool
    job: Job
    processingOptions: JobProcessingOptions
    updateJobFields: str

class JobFilters(typing_extensions.TypedDict, total=False):
    companyTitles: typing.List[str]
    customAttributeFilter: str
    publishDateRange: typing_extensions.Literal[
        "DATE_RANGE_UNSPECIFIED",
        "PAST_24_HOURS",
        "PAST_WEEK",
        "PAST_MONTH",
        "PAST_YEAR",
        "PAST_3_DAYS",
    ]
    categories: typing.List[str]
    languageCodes: typing.List[str]
    locationFilters: typing.List[LocationFilter]
    companyNames: typing.List[str]
    commuteFilter: CommutePreference
    tenantJobOnly: bool
    compensationFilter: CompensationFilter
    extendedCompensationFilter: ExtendedCompensationFilter
    disableSpellCheck: bool
    query: str
    customFieldFilters: typing.Dict[str, typing.Any]
    employmentTypes: typing.List[str]

class CompensationHistogramResult(typing_extensions.TypedDict, total=False):
    result: NumericBucketingResult
    type: typing_extensions.Literal[
        "COMPENSATION_HISTOGRAM_REQUEST_TYPE_UNSPECIFIED",
        "BASE",
        "ANNUALIZED_BASE",
        "ANNUALIZED_TOTAL",
    ]

class RequestMetadata(typing_extensions.TypedDict, total=False):
    sessionId: str
    userId: str
    domain: str
    deviceInfo: DeviceInfo

class CustomField(typing_extensions.TypedDict, total=False):
    values: typing.List[str]

class CustomFieldFilter(typing_extensions.TypedDict, total=False):
    type: typing_extensions.Literal["FILTER_TYPE_UNSPECIFIED", "OR", "AND", "NOT"]
    queries: typing.List[str]

class CreateJobRequest(typing_extensions.TypedDict, total=False):
    disableStreetAddressResolution: bool
    processingOptions: JobProcessingOptions
    job: Job

class ListJobsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    jobs: typing.List[Job]
    metadata: ResponseMetadata

class GoogleCloudTalentV4BatchCreateJobsResponse(
    typing_extensions.TypedDict, total=False
):
    jobResults: typing.List[GoogleCloudTalentV4JobResult]

class ExtendedCompensationInfoDecimal(typing_extensions.TypedDict, total=False):
    micros: int
    units: str

class GetHistogramResponse(typing_extensions.TypedDict, total=False):
    metadata: ResponseMetadata
    results: typing.List[HistogramResult]

class GoogleCloudTalentV4CompensationInfoCompensationEntry(
    typing_extensions.TypedDict, total=False
):
    description: str
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
    range: GoogleCloudTalentV4CompensationInfoCompensationRange
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

class GoogleCloudTalentV4CompensationInfo(typing_extensions.TypedDict, total=False):
    annualizedBaseCompensationRange: GoogleCloudTalentV4CompensationInfoCompensationRange
    entries: typing.List[GoogleCloudTalentV4CompensationInfoCompensationEntry]
    annualizedTotalCompensationRange: GoogleCloudTalentV4CompensationInfoCompensationRange

class CompensationRange(typing_extensions.TypedDict, total=False):
    max: Money
    min: Money

class DeleteJobsByFilterRequest(typing_extensions.TypedDict, total=False):
    disableFastProcess: bool
    filter: Filter

class CompletionResult(typing_extensions.TypedDict, total=False):
    imageUrl: str
    suggestion: str
    type: typing_extensions.Literal[
        "COMPLETION_TYPE_UNSPECIFIED", "JOB_TITLE", "COMPANY_NAME", "COMBINED"
    ]

class GoogleCloudTalentV4JobProcessingOptions(typing_extensions.TypedDict, total=False):
    disableStreetAddressResolution: bool
    htmlSanitization: typing_extensions.Literal[
        "HTML_SANITIZATION_UNSPECIFIED",
        "HTML_SANITIZATION_DISABLED",
        "SIMPLE_FORMATTING_ONLY",
    ]

class CompanyInfoSource(typing_extensions.TypedDict, total=False):
    freebaseMid: str
    unknownTypeId: str
    gplusId: str
    mapsCid: str

class ExtendedCompensationInfoCompensationRange(
    typing_extensions.TypedDict, total=False
):
    max: ExtendedCompensationInfoDecimal
    min: ExtendedCompensationInfoDecimal

class ListCompanyJobsResponse(typing_extensions.TypedDict, total=False):
    metadata: ResponseMetadata
    nextPageToken: str
    totalSize: str
    jobs: typing.List[Job]

class GoogleCloudTalentV4BatchOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    stateDescription: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "INITIALIZING",
        "PROCESSING",
        "SUCCEEDED",
        "FAILED",
        "CANCELLING",
        "CANCELLED",
    ]
    createTime: str
    successCount: int
    endTime: str
    failureCount: int
    totalCount: int
    updateTime: str

class NumericBucketingResult(typing_extensions.TypedDict, total=False):
    counts: typing.List[BucketizedCount]
    maxValue: float
    minValue: float

class PostalAddress(typing_extensions.TypedDict, total=False):
    regionCode: str
    sortingCode: str
    revision: int
    recipients: typing.List[str]
    addressLines: typing.List[str]
    administrativeArea: str
    postalCode: str
    sublocality: str
    organization: str
    languageCode: str
    locality: str

class ExtendedCompensationInfo(typing_extensions.TypedDict, total=False):
    annualizedTotalCompensationRange: ExtendedCompensationInfoCompensationRange
    annualizedBaseCompensationRange: ExtendedCompensationInfoCompensationRange
    currency: str
    annualizedTotalCompensationUnspecified: bool
    annualizedBaseCompensationUnspecified: bool
    entries: typing.List[ExtendedCompensationInfoCompensationEntry]

class NamespacedDebugInput(typing_extensions.TypedDict, total=False):
    disableAutomaticEnrollmentSelection: bool
    disableManualEnrollmentSelection: bool
    conditionallyForcedExpNames: typing.List[str]
    disableExps: typing.List[int]
    conditionallyForcedExps: typing.List[int]
    disableOrganicSelection: bool
    disableExpNames: typing.List[str]
    conditionallyForcedExpTags: typing.List[str]
    absolutelyForcedExpTags: typing.List[str]
    absolutelyForcedExpNames: typing.List[str]
    disableExpTags: typing.List[str]
    forcedFlags: typing.Dict[str, typing.Any]
    forcedRollouts: typing.Dict[str, typing.Any]
    absolutelyForcedExps: typing.List[int]

class GoogleCloudTalentV4BatchDeleteJobsResponse(
    typing_extensions.TypedDict, total=False
):
    jobResults: typing.List[GoogleCloudTalentV4JobResult]

class CustomAttribute(typing_extensions.TypedDict, total=False):
    filterable: bool
    stringValues: StringValues
    longValue: str

class GoogleCloudTalentV4Job(typing_extensions.TypedDict, total=False):
    name: str
    languageCode: str
    visibility: typing_extensions.Literal[
        "VISIBILITY_UNSPECIFIED",
        "ACCOUNT_ONLY",
        "SHARED_WITH_GOOGLE",
        "SHARED_WITH_PUBLIC",
    ]
    jobLevel: typing_extensions.Literal[
        "JOB_LEVEL_UNSPECIFIED",
        "ENTRY_LEVEL",
        "EXPERIENCED",
        "MANAGER",
        "DIRECTOR",
        "EXECUTIVE",
    ]
    processingOptions: GoogleCloudTalentV4JobProcessingOptions
    applicationInfo: GoogleCloudTalentV4JobApplicationInfo
    jobStartTime: str
    jobEndTime: str
    title: str
    qualifications: str
    jobBenefits: typing.List[str]
    description: str
    companyDisplayName: str
    postingCreateTime: str
    degreeTypes: typing.List[str]
    requisitionId: str
    responsibilities: str
    promotionValue: int
    employmentTypes: typing.List[str]
    incentives: str
    postingExpireTime: str
    postingRegion: typing_extensions.Literal[
        "POSTING_REGION_UNSPECIFIED", "ADMINISTRATIVE_AREA", "NATION", "TELECOMMUTE"
    ]
    compensationInfo: GoogleCloudTalentV4CompensationInfo
    postingPublishTime: str
    department: str
    customAttributes: typing.Dict[str, typing.Any]
    postingUpdateTime: str
    addresses: typing.List[str]
    derivedInfo: GoogleCloudTalentV4JobDerivedInfo
    company: str

class GoogleCloudTalentV4CompensationInfoCompensationRange(
    typing_extensions.TypedDict, total=False
):
    minCompensation: Money
    maxCompensation: Money

class SearchJobsRequest(typing_extensions.TypedDict, total=False):
    filters: JobFilters
    pageToken: str
    enableBroadening: bool
    query: JobQuery
    enablePreciseResultSize: bool
    pageSize: int
    disableRelevanceThresholding: bool
    offset: int
    histogramFacets: HistogramFacets
    sortBy: typing_extensions.Literal[
        "SORT_BY_UNSPECIFIED",
        "RELEVANCE_DESC",
        "PUBLISHED_DATE_DESC",
        "UPDATED_DATE_DESC",
        "TITLE",
        "TITLE_DESC",
        "ANNUALIZED_BASE_COMPENSATION",
        "ANNUALIZED_TOTAL_COMPENSATION",
        "ANNUALIZED_BASE_COMPENSATION_DESC",
        "ANNUALIZED_TOTAL_COMPENSATION_DESC",
    ]
    requestMetadata: RequestMetadata
    jobView: typing_extensions.Literal[
        "JOB_VIEW_UNSPECIFIED", "SMALL", "MINIMAL", "FULL"
    ]
    mode: typing_extensions.Literal[
        "SEARCH_MODE_UNSPECIFIED",
        "JOB_SEARCH",
        "FEATURED_JOB_SEARCH",
        "EMAIL_ALERT_SEARCH",
    ]
    orderBy: typing_extensions.Literal[
        "SORT_BY_UNSPECIFIED",
        "RELEVANCE_DESC",
        "PUBLISHED_DATE_DESC",
        "UPDATED_DATE_DESC",
        "TITLE",
        "TITLE_DESC",
        "ANNUALIZED_BASE_COMPENSATION",
        "ANNUALIZED_TOTAL_COMPENSATION",
        "ANNUALIZED_BASE_COMPENSATION_DESC",
        "ANNUALIZED_TOTAL_COMPENSATION_DESC",
    ]

class LocationFilter(typing_extensions.TypedDict, total=False):
    isTelecommute: bool
    regionCode: str
    latLng: LatLng
    distanceInMiles: float
    name: str

class GoogleCloudTalentV4JobResult(typing_extensions.TypedDict, total=False):
    status: Status
    job: GoogleCloudTalentV4Job

class CommuteInfo(typing_extensions.TypedDict, total=False):
    travelDuration: str
    jobLocation: JobLocation
