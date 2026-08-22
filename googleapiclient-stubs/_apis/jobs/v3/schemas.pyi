import typing

_list = list

@typing.type_check_only
class ApplicationInfo(typing.TypedDict, total=False):
    emails: _list[str]
    instruction: str
    uris: _list[str]

@typing.type_check_only
class BatchDeleteJobsRequest(typing.TypedDict, total=False):
    filter: str

AlternativeBucketRange = typing.TypedDict(
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
class BucketizedCount(typing.TypedDict, total=False):
    count: int
    range: BucketRange

@typing.type_check_only
class ClientEvent(typing.TypedDict, total=False):
    createTime: str
    eventId: str
    extraInfo: dict[str, typing.Any]
    jobEvent: JobEvent
    parentEventId: str
    requestId: str

@typing.type_check_only
class CommuteFilter(typing.TypedDict, total=False):
    allowImpreciseAddresses: bool
    commuteMethod: typing.Literal["COMMUTE_METHOD_UNSPECIFIED", "DRIVING", "TRANSIT"]
    departureTime: TimeOfDay
    roadTraffic: typing.Literal["ROAD_TRAFFIC_UNSPECIFIED", "TRAFFIC_FREE", "BUSY_HOUR"]
    startCoordinates: LatLng
    travelDuration: str

@typing.type_check_only
class CommuteInfo(typing.TypedDict, total=False):
    jobLocation: Location
    travelDuration: str

@typing.type_check_only
class Company(typing.TypedDict, total=False):
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
    size: typing.Literal[
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
class CompanyDerivedInfo(typing.TypedDict, total=False):
    headquartersLocation: Location

@typing.type_check_only
class CompensationEntry(typing.TypedDict, total=False):
    amount: Money
    description: str
    expectedUnitsPerYear: float
    range: CompensationRange
    type: typing.Literal[
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
    unit: typing.Literal[
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
class CompensationFilter(typing.TypedDict, total=False):
    includeJobsWithUnspecifiedCompensationRange: bool
    range: CompensationRange
    type: typing.Literal[
        "FILTER_TYPE_UNSPECIFIED",
        "UNIT_ONLY",
        "UNIT_AND_AMOUNT",
        "ANNUALIZED_BASE_AMOUNT",
        "ANNUALIZED_TOTAL_AMOUNT",
    ]
    units: _list[
        typing.Literal[
            "COMPENSATION_UNIT_UNSPECIFIED",
            "HOURLY",
            "DAILY",
            "WEEKLY",
            "MONTHLY",
            "YEARLY",
            "ONE_TIME",
            "OTHER_COMPENSATION_UNIT",
        ]
    ]

@typing.type_check_only
class CompensationHistogramRequest(typing.TypedDict, total=False):
    bucketingOption: NumericBucketingOption
    type: typing.Literal[
        "COMPENSATION_HISTOGRAM_REQUEST_TYPE_UNSPECIFIED",
        "BASE",
        "ANNUALIZED_BASE",
        "ANNUALIZED_TOTAL",
    ]

@typing.type_check_only
class CompensationHistogramResult(typing.TypedDict, total=False):
    result: NumericBucketingResult
    type: typing.Literal[
        "COMPENSATION_HISTOGRAM_REQUEST_TYPE_UNSPECIFIED",
        "BASE",
        "ANNUALIZED_BASE",
        "ANNUALIZED_TOTAL",
    ]

@typing.type_check_only
class CompensationInfo(typing.TypedDict, total=False):
    annualizedBaseCompensationRange: CompensationRange
    annualizedTotalCompensationRange: CompensationRange
    entries: _list[CompensationEntry]

@typing.type_check_only
class CompensationRange(typing.TypedDict, total=False):
    maxCompensation: Money
    minCompensation: Money

@typing.type_check_only
class CompleteQueryResponse(typing.TypedDict, total=False):
    completionResults: _list[CompletionResult]
    metadata: ResponseMetadata

@typing.type_check_only
class CompletionResult(typing.TypedDict, total=False):
    imageUri: str
    suggestion: str
    type: typing.Literal[
        "COMPLETION_TYPE_UNSPECIFIED", "JOB_TITLE", "COMPANY_NAME", "COMBINED"
    ]

@typing.type_check_only
class CreateClientEventRequest(typing.TypedDict, total=False):
    clientEvent: ClientEvent

@typing.type_check_only
class CreateCompanyRequest(typing.TypedDict, total=False):
    company: Company

@typing.type_check_only
class CreateJobRequest(typing.TypedDict, total=False):
    job: Job

@typing.type_check_only
class CustomAttribute(typing.TypedDict, total=False):
    filterable: bool
    longValues: _list[str]
    stringValues: _list[str]

@typing.type_check_only
class CustomAttributeHistogramRequest(typing.TypedDict, total=False):
    key: str
    longValueHistogramBucketingOption: NumericBucketingOption
    stringValueHistogram: bool

@typing.type_check_only
class CustomAttributeHistogramResult(typing.TypedDict, total=False):
    key: str
    longValueHistogramResult: NumericBucketingResult
    stringValueHistogramResult: dict[str, typing.Any]

@typing.type_check_only
class DeviceInfo(typing.TypedDict, total=False):
    deviceType: typing.Literal[
        "DEVICE_TYPE_UNSPECIFIED", "WEB", "MOBILE_WEB", "ANDROID", "IOS", "BOT", "OTHER"
    ]
    id: str

@typing.type_check_only
class Empty(typing.TypedDict, total=False): ...

@typing.type_check_only
class HistogramFacets(typing.TypedDict, total=False):
    compensationHistogramFacets: _list[CompensationHistogramRequest]
    customAttributeHistogramFacets: _list[CustomAttributeHistogramRequest]
    simpleHistogramFacets: _list[
        typing.Literal[
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
    ]

@typing.type_check_only
class HistogramResult(typing.TypedDict, total=False):
    searchType: typing.Literal[
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
class HistogramResults(typing.TypedDict, total=False):
    compensationHistogramResults: _list[CompensationHistogramResult]
    customAttributeHistogramResults: _list[CustomAttributeHistogramResult]
    simpleHistogramResults: _list[HistogramResult]

@typing.type_check_only
class Job(typing.TypedDict, total=False):
    addresses: _list[str]
    applicationInfo: ApplicationInfo
    companyDisplayName: str
    companyName: str
    compensationInfo: CompensationInfo
    customAttributes: dict[str, typing.Any]
    degreeTypes: _list[
        typing.Literal[
            "DEGREE_TYPE_UNSPECIFIED",
            "PRIMARY_EDUCATION",
            "LOWER_SECONDARY_EDUCATION",
            "UPPER_SECONDARY_EDUCATION",
            "ADULT_REMEDIAL_EDUCATION",
            "ASSOCIATES_OR_EQUIVALENT",
            "BACHELORS_OR_EQUIVALENT",
            "MASTERS_OR_EQUIVALENT",
            "DOCTORAL_OR_EQUIVALENT",
        ]
    ]
    department: str
    derivedInfo: JobDerivedInfo
    description: str
    employmentTypes: _list[
        typing.Literal[
            "EMPLOYMENT_TYPE_UNSPECIFIED",
            "FULL_TIME",
            "PART_TIME",
            "CONTRACTOR",
            "CONTRACT_TO_HIRE",
            "TEMPORARY",
            "INTERN",
            "VOLUNTEER",
            "PER_DIEM",
            "FLY_IN_FLY_OUT",
            "OTHER_EMPLOYMENT_TYPE",
        ]
    ]
    incentives: str
    jobBenefits: _list[
        typing.Literal[
            "JOB_BENEFIT_UNSPECIFIED",
            "CHILD_CARE",
            "DENTAL",
            "DOMESTIC_PARTNER",
            "FLEXIBLE_HOURS",
            "MEDICAL",
            "LIFE_INSURANCE",
            "PARENTAL_LEAVE",
            "RETIREMENT_PLAN",
            "SICK_DAYS",
            "VACATION",
            "VISION",
        ]
    ]
    jobEndTime: str
    jobLevel: typing.Literal[
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
    postingRegion: typing.Literal[
        "POSTING_REGION_UNSPECIFIED", "ADMINISTRATIVE_AREA", "NATION", "TELECOMMUTE"
    ]
    postingUpdateTime: str
    processingOptions: ProcessingOptions
    promotionValue: int
    qualifications: str
    requisitionId: str
    responsibilities: str
    title: str
    visibility: typing.Literal[
        "VISIBILITY_UNSPECIFIED",
        "ACCOUNT_ONLY",
        "SHARED_WITH_GOOGLE",
        "SHARED_WITH_PUBLIC",
    ]

@typing.type_check_only
class JobDerivedInfo(typing.TypedDict, total=False):
    jobCategories: _list[
        typing.Literal[
            "JOB_CATEGORY_UNSPECIFIED",
            "ACCOUNTING_AND_FINANCE",
            "ADMINISTRATIVE_AND_OFFICE",
            "ADVERTISING_AND_MARKETING",
            "ANIMAL_CARE",
            "ART_FASHION_AND_DESIGN",
            "BUSINESS_OPERATIONS",
            "CLEANING_AND_FACILITIES",
            "COMPUTER_AND_IT",
            "CONSTRUCTION",
            "CUSTOMER_SERVICE",
            "EDUCATION",
            "ENTERTAINMENT_AND_TRAVEL",
            "FARMING_AND_OUTDOORS",
            "HEALTHCARE",
            "HUMAN_RESOURCES",
            "INSTALLATION_MAINTENANCE_AND_REPAIR",
            "LEGAL",
            "MANAGEMENT",
            "MANUFACTURING_AND_WAREHOUSE",
            "MEDIA_COMMUNICATIONS_AND_WRITING",
            "OIL_GAS_AND_MINING",
            "PERSONAL_CARE_AND_SERVICES",
            "PROTECTIVE_SERVICES",
            "REAL_ESTATE",
            "RESTAURANT_AND_HOSPITALITY",
            "SALES_AND_RETAIL",
            "SCIENCE_AND_ENGINEERING",
            "SOCIAL_SERVICES_AND_NON_PROFIT",
            "SPORTS_FITNESS_AND_RECREATION",
            "TRANSPORTATION_AND_LOGISTICS",
        ]
    ]
    locations: _list[Location]

@typing.type_check_only
class JobEvent(typing.TypedDict, total=False):
    jobs: _list[str]
    type: typing.Literal[
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
class JobQuery(typing.TypedDict, total=False):
    commuteFilter: CommuteFilter
    companyDisplayNames: _list[str]
    companyNames: _list[str]
    compensationFilter: CompensationFilter
    customAttributeFilter: str
    disableSpellCheck: bool
    employmentTypes: _list[
        typing.Literal[
            "EMPLOYMENT_TYPE_UNSPECIFIED",
            "FULL_TIME",
            "PART_TIME",
            "CONTRACTOR",
            "CONTRACT_TO_HIRE",
            "TEMPORARY",
            "INTERN",
            "VOLUNTEER",
            "PER_DIEM",
            "FLY_IN_FLY_OUT",
            "OTHER_EMPLOYMENT_TYPE",
        ]
    ]
    jobCategories: _list[
        typing.Literal[
            "JOB_CATEGORY_UNSPECIFIED",
            "ACCOUNTING_AND_FINANCE",
            "ADMINISTRATIVE_AND_OFFICE",
            "ADVERTISING_AND_MARKETING",
            "ANIMAL_CARE",
            "ART_FASHION_AND_DESIGN",
            "BUSINESS_OPERATIONS",
            "CLEANING_AND_FACILITIES",
            "COMPUTER_AND_IT",
            "CONSTRUCTION",
            "CUSTOMER_SERVICE",
            "EDUCATION",
            "ENTERTAINMENT_AND_TRAVEL",
            "FARMING_AND_OUTDOORS",
            "HEALTHCARE",
            "HUMAN_RESOURCES",
            "INSTALLATION_MAINTENANCE_AND_REPAIR",
            "LEGAL",
            "MANAGEMENT",
            "MANUFACTURING_AND_WAREHOUSE",
            "MEDIA_COMMUNICATIONS_AND_WRITING",
            "OIL_GAS_AND_MINING",
            "PERSONAL_CARE_AND_SERVICES",
            "PROTECTIVE_SERVICES",
            "REAL_ESTATE",
            "RESTAURANT_AND_HOSPITALITY",
            "SALES_AND_RETAIL",
            "SCIENCE_AND_ENGINEERING",
            "SOCIAL_SERVICES_AND_NON_PROFIT",
            "SPORTS_FITNESS_AND_RECREATION",
            "TRANSPORTATION_AND_LOGISTICS",
        ]
    ]
    languageCodes: _list[str]
    locationFilters: _list[LocationFilter]
    publishTimeRange: TimestampRange
    query: str
    queryLanguageCode: str

@typing.type_check_only
class LatLng(typing.TypedDict, total=False):
    latitude: float
    longitude: float

@typing.type_check_only
class ListCompaniesResponse(typing.TypedDict, total=False):
    companies: _list[Company]
    metadata: ResponseMetadata
    nextPageToken: str

@typing.type_check_only
class ListJobsResponse(typing.TypedDict, total=False):
    jobs: _list[Job]
    metadata: ResponseMetadata
    nextPageToken: str

@typing.type_check_only
class Location(typing.TypedDict, total=False):
    latLng: LatLng
    locationType: typing.Literal[
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
class LocationFilter(typing.TypedDict, total=False):
    address: str
    distanceInMiles: float
    latLng: LatLng
    regionCode: str
    telecommutePreference: typing.Literal[
        "TELECOMMUTE_PREFERENCE_UNSPECIFIED",
        "TELECOMMUTE_EXCLUDED",
        "TELECOMMUTE_ALLOWED",
        "TELECOMMUTE_JOBS_EXCLUDED",
    ]

@typing.type_check_only
class MatchingJob(typing.TypedDict, total=False):
    commuteInfo: CommuteInfo
    job: Job
    jobSummary: str
    jobTitleSnippet: str
    searchTextSnippet: str

@typing.type_check_only
class Money(typing.TypedDict, total=False):
    currencyCode: str
    nanos: int
    units: str

@typing.type_check_only
class NumericBucketingOption(typing.TypedDict, total=False):
    bucketBounds: _list[float]
    requiresMinMax: bool

@typing.type_check_only
class NumericBucketingResult(typing.TypedDict, total=False):
    counts: _list[BucketizedCount]
    maxValue: float
    minValue: float

@typing.type_check_only
class PostalAddress(typing.TypedDict, total=False):
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
class ProcessingOptions(typing.TypedDict, total=False):
    disableStreetAddressResolution: bool
    htmlSanitization: typing.Literal[
        "HTML_SANITIZATION_UNSPECIFIED",
        "HTML_SANITIZATION_DISABLED",
        "SIMPLE_FORMATTING_ONLY",
    ]

@typing.type_check_only
class RequestMetadata(typing.TypedDict, total=False):
    deviceInfo: DeviceInfo
    domain: str
    sessionId: str
    userId: str

@typing.type_check_only
class ResponseMetadata(typing.TypedDict, total=False):
    requestId: str

@typing.type_check_only
class SearchJobsRequest(typing.TypedDict, total=False):
    disableKeywordMatch: bool
    diversificationLevel: typing.Literal[
        "DIVERSIFICATION_LEVEL_UNSPECIFIED", "DISABLED", "SIMPLE"
    ]
    enableBroadening: bool
    histogramFacets: HistogramFacets
    jobQuery: JobQuery
    jobView: typing.Literal[
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
    searchMode: typing.Literal[
        "SEARCH_MODE_UNSPECIFIED", "JOB_SEARCH", "FEATURED_JOB_SEARCH"
    ]

@typing.type_check_only
class SearchJobsResponse(typing.TypedDict, total=False):
    broadenedQueryJobsCount: int
    estimatedTotalSize: int
    histogramResults: HistogramResults
    locationFilters: _list[Location]
    matchingJobs: _list[MatchingJob]
    metadata: ResponseMetadata
    nextPageToken: str
    spellCorrection: SpellingCorrection
    totalSize: int

@typing.type_check_only
class SpellingCorrection(typing.TypedDict, total=False):
    corrected: bool
    correctedText: str

@typing.type_check_only
class TimeOfDay(typing.TypedDict, total=False):
    hours: int
    minutes: int
    nanos: int
    seconds: int

@typing.type_check_only
class TimestampRange(typing.TypedDict, total=False):
    endTime: str
    startTime: str

@typing.type_check_only
class UpdateCompanyRequest(typing.TypedDict, total=False):
    company: Company
    updateMask: str

@typing.type_check_only
class UpdateJobRequest(typing.TypedDict, total=False):
    job: Job
    updateMask: str
