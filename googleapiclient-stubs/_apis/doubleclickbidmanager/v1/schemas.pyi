import typing

import typing_extensions
@typing.type_check_only
class DownloadLineItemsRequest(typing_extensions.TypedDict, total=False):
    fileSpec: typing_extensions.Literal["EWF"]
    filterIds: typing.List[str]
    filterType: typing_extensions.Literal[
        "ADVERTISER_ID", "INSERTION_ORDER_ID", "LINE_ITEM_ID"
    ]
    format: typing_extensions.Literal["CSV"]

@typing.type_check_only
class DownloadLineItemsResponse(typing_extensions.TypedDict, total=False):
    lineItems: str

@typing.type_check_only
class DownloadRequest(typing_extensions.TypedDict, total=False):
    fileTypes: typing.List[str]
    filterIds: typing.List[str]
    filterType: typing_extensions.Literal[
        "ADVERTISER_ID",
        "INSERTION_ORDER_ID",
        "LINE_ITEM_ID",
        "CAMPAIGN_ID",
        "INVENTORY_SOURCE_ID",
        "PARTNER_ID",
    ]
    version: str

@typing.type_check_only
class DownloadResponse(typing_extensions.TypedDict, total=False):
    adGroups: str
    ads: str
    campaigns: str
    insertionOrders: str
    inventorySources: str
    lineItems: str

@typing.type_check_only
class FilterPair(typing_extensions.TypedDict, total=False):
    type: typing_extensions.Literal[
        "FILTER_UNKNOWN",
        "FILTER_DATE",
        "FILTER_DAY_OF_WEEK",
        "FILTER_WEEK",
        "FILTER_MONTH",
        "FILTER_YEAR",
        "FILTER_TIME_OF_DAY",
        "FILTER_CONVERSION_DELAY",
        "FILTER_CREATIVE_ID",
        "FILTER_CREATIVE_SIZE",
        "FILTER_CREATIVE_TYPE",
        "FILTER_EXCHANGE_ID",
        "FILTER_AD_POSITION",
        "FILTER_INVENTORY_SOURCE",
        "FILTER_CITY",
        "FILTER_REGION",
        "FILTER_DMA",
        "FILTER_COUNTRY",
        "FILTER_SITE_ID",
        "FILTER_CHANNEL_ID",
        "FILTER_PARTNER",
        "FILTER_ADVERTISER",
        "FILTER_INSERTION_ORDER",
        "FILTER_LINE_ITEM",
        "FILTER_PARTNER_CURRENCY",
        "FILTER_ADVERTISER_CURRENCY",
        "FILTER_ADVERTISER_TIMEZONE",
        "FILTER_LINE_ITEM_TYPE",
        "FILTER_USER_LIST",
        "FILTER_USER_LIST_FIRST_PARTY",
        "FILTER_USER_LIST_THIRD_PARTY",
        "FILTER_TARGETED_USER_LIST",
        "FILTER_DATA_PROVIDER",
        "FILTER_ORDER_ID",
        "FILTER_VIDEO_PLAYER_SIZE",
        "FILTER_VIDEO_DURATION_SECONDS",
        "FILTER_KEYWORD",
        "FILTER_PAGE_CATEGORY",
        "FILTER_CAMPAIGN_DAILY_FREQUENCY",
        "FILTER_LINE_ITEM_DAILY_FREQUENCY",
        "FILTER_LINE_ITEM_LIFETIME_FREQUENCY",
        "FILTER_OS",
        "FILTER_BROWSER",
        "FILTER_CARRIER",
        "FILTER_SITE_LANGUAGE",
        "FILTER_INVENTORY_FORMAT",
        "FILTER_ZIP_CODE",
        "FILTER_VIDEO_RATING_TIER",
        "FILTER_VIDEO_FORMAT_SUPPORT",
        "FILTER_VIDEO_SKIPPABLE_SUPPORT",
        "FILTER_VIDEO_VPAID_SUPPORT",
        "FILTER_VIDEO_CREATIVE_DURATION",
        "FILTER_PAGE_LAYOUT",
        "FILTER_VIDEO_AD_POSITION_IN_STREAM",
        "FILTER_AGE",
        "FILTER_GENDER",
        "FILTER_QUARTER",
        "FILTER_TRUEVIEW_CONVERSION_TYPE",
        "FILTER_MOBILE_GEO",
        "FILTER_MRAID_SUPPORT",
        "FILTER_ACTIVE_VIEW_EXPECTED_VIEWABILITY",
        "FILTER_VIDEO_CREATIVE_DURATION_SKIPPABLE",
        "FILTER_NIELSEN_COUNTRY_CODE",
        "FILTER_NIELSEN_DEVICE_ID",
        "FILTER_NIELSEN_GENDER",
        "FILTER_NIELSEN_AGE",
        "FILTER_INVENTORY_SOURCE_TYPE",
        "FILTER_CREATIVE_WIDTH",
        "FILTER_CREATIVE_HEIGHT",
        "FILTER_DFP_ORDER_ID",
        "FILTER_TRUEVIEW_AGE",
        "FILTER_TRUEVIEW_GENDER",
        "FILTER_TRUEVIEW_PARENTAL_STATUS",
        "FILTER_TRUEVIEW_REMARKETING_LIST",
        "FILTER_TRUEVIEW_INTEREST",
        "FILTER_TRUEVIEW_AD_GROUP_ID",
        "FILTER_TRUEVIEW_AD_GROUP_AD_ID",
        "FILTER_TRUEVIEW_IAR_LANGUAGE",
        "FILTER_TRUEVIEW_IAR_GENDER",
        "FILTER_TRUEVIEW_IAR_AGE",
        "FILTER_TRUEVIEW_IAR_CATEGORY",
        "FILTER_TRUEVIEW_IAR_COUNTRY",
        "FILTER_TRUEVIEW_IAR_CITY",
        "FILTER_TRUEVIEW_IAR_REGION",
        "FILTER_TRUEVIEW_IAR_ZIPCODE",
        "FILTER_TRUEVIEW_IAR_REMARKETING_LIST",
        "FILTER_TRUEVIEW_IAR_INTEREST",
        "FILTER_TRUEVIEW_IAR_PARENTAL_STATUS",
        "FILTER_TRUEVIEW_IAR_TIME_OF_DAY",
        "FILTER_TRUEVIEW_CUSTOM_AFFINITY",
        "FILTER_TRUEVIEW_CATEGORY",
        "FILTER_TRUEVIEW_KEYWORD",
        "FILTER_TRUEVIEW_PLACEMENT",
        "FILTER_TRUEVIEW_URL",
        "FILTER_TRUEVIEW_COUNTRY",
        "FILTER_TRUEVIEW_REGION",
        "FILTER_TRUEVIEW_CITY",
        "FILTER_TRUEVIEW_DMA",
        "FILTER_TRUEVIEW_ZIPCODE",
        "FILTER_NOT_SUPPORTED",
        "FILTER_MEDIA_PLAN",
        "FILTER_TRUEVIEW_IAR_YOUTUBE_CHANNEL",
        "FILTER_TRUEVIEW_IAR_YOUTUBE_VIDEO",
        "FILTER_SKIPPABLE_SUPPORT",
        "FILTER_COMPANION_CREATIVE_ID",
        "FILTER_BUDGET_SEGMENT_DESCRIPTION",
        "FILTER_FLOODLIGHT_ACTIVITY_ID",
        "FILTER_DEVICE_MODEL",
        "FILTER_DEVICE_MAKE",
        "FILTER_DEVICE_TYPE",
        "FILTER_CREATIVE_ATTRIBUTE",
        "FILTER_INVENTORY_COMMITMENT_TYPE",
        "FILTER_INVENTORY_RATE_TYPE",
        "FILTER_INVENTORY_DELIVERY_METHOD",
        "FILTER_INVENTORY_SOURCE_EXTERNAL_ID",
        "FILTER_AUTHORIZED_SELLER_STATE",
        "FILTER_VIDEO_DURATION_SECONDS_RANGE",
    ]
    value: str

@typing.type_check_only
class ListQueriesResponse(typing_extensions.TypedDict, total=False):
    kind: str
    queries: typing.List[Query]

@typing.type_check_only
class ListReportsResponse(typing_extensions.TypedDict, total=False):
    kind: str
    reports: typing.List[Report]

@typing.type_check_only
class Parameters(typing_extensions.TypedDict, total=False):
    filters: typing.List[FilterPair]
    groupBys: typing.List[str]
    includeInviteData: bool
    metrics: typing.List[str]
    type: typing_extensions.Literal[
        "TYPE_GENERAL",
        "TYPE_AUDIENCE_PERFORMANCE",
        "TYPE_INVENTORY_AVAILABILITY",
        "TYPE_KEYWORD",
        "TYPE_PIXEL_LOAD",
        "TYPE_AUDIENCE_COMPOSITION",
        "TYPE_CROSS_PARTNER",
        "TYPE_PAGE_CATEGORY",
        "TYPE_THIRD_PARTY_DATA_PROVIDER",
        "TYPE_CROSS_PARTNER_THIRD_PARTY_DATA_PROVIDER",
        "TYPE_CLIENT_SAFE",
        "TYPE_ORDER_ID",
        "TYPE_FEE",
        "TYPE_CROSS_FEE",
        "TYPE_ACTIVE_GRP",
        "TYPE_YOUTUBE_VERTICAL",
        "TYPE_COMSCORE_VCE",
        "TYPE_TRUEVIEW",
        "TYPE_NIELSEN_AUDIENCE_PROFILE",
        "TYPE_NIELSEN_DAILY_REACH_BUILD",
        "TYPE_NIELSEN_SITE",
        "TYPE_REACH_AND_FREQUENCY",
        "TYPE_ESTIMATED_CONVERSION",
        "TYPE_VERIFICATION",
        "TYPE_TRUEVIEW_IAR",
        "TYPE_NIELSEN_ONLINE_GLOBAL_MARKET",
        "TYPE_PETRA_NIELSEN_AUDIENCE_PROFILE",
        "TYPE_PETRA_NIELSEN_DAILY_REACH_BUILD",
        "TYPE_PETRA_NIELSEN_ONLINE_GLOBAL_MARKET",
        "TYPE_NOT_SUPPORTED",
        "TYPE_REACH_AUDIENCE",
        "TYPE_LINEAR_TV_SEARCH_LIFT",
    ]

@typing.type_check_only
class Query(typing_extensions.TypedDict, total=False):
    kind: str
    metadata: QueryMetadata
    params: Parameters
    queryId: str
    reportDataEndTimeMs: str
    reportDataStartTimeMs: str
    schedule: QuerySchedule
    timezoneCode: str

@typing.type_check_only
class QueryMetadata(typing_extensions.TypedDict, total=False):
    dataRange: typing_extensions.Literal[
        "CUSTOM_DATES",
        "CURRENT_DAY",
        "PREVIOUS_DAY",
        "WEEK_TO_DATE",
        "MONTH_TO_DATE",
        "QUARTER_TO_DATE",
        "YEAR_TO_DATE",
        "PREVIOUS_WEEK",
        "PREVIOUS_HALF_MONTH",
        "PREVIOUS_MONTH",
        "PREVIOUS_QUARTER",
        "PREVIOUS_YEAR",
        "LAST_7_DAYS",
        "LAST_30_DAYS",
        "LAST_90_DAYS",
        "LAST_365_DAYS",
        "ALL_TIME",
        "LAST_14_DAYS",
        "TYPE_NOT_SUPPORTED",
    ]
    format: typing_extensions.Literal["CSV", "EXCEL_CSV", "XLSX"]
    googleCloudStoragePathForLatestReport: str
    googleDrivePathForLatestReport: str
    latestReportRunTimeMs: str
    locale: str
    reportCount: int
    running: bool
    sendNotification: bool
    shareEmailAddress: typing.List[str]
    title: str

@typing.type_check_only
class QuerySchedule(typing_extensions.TypedDict, total=False):
    endTimeMs: str
    frequency: typing_extensions.Literal[
        "ONE_TIME", "DAILY", "WEEKLY", "SEMI_MONTHLY", "MONTHLY", "QUARTERLY"
    ]
    nextRunMinuteOfDay: int
    nextRunTimezoneCode: str

@typing.type_check_only
class Report(typing_extensions.TypedDict, total=False):
    key: ReportKey
    metadata: ReportMetadata
    params: Parameters

@typing.type_check_only
class ReportFailure(typing_extensions.TypedDict, total=False):
    errorCode: typing_extensions.Literal[
        "AUTHENTICATION_ERROR",
        "UNAUTHORIZED_API_ACCESS",
        "SERVER_ERROR",
        "VALIDATION_ERROR",
        "REPORTING_FATAL_ERROR",
        "REPORTING_TRANSIENT_ERROR",
        "REPORTING_IMCOMPATIBLE_METRICS",
        "REPORTING_ILLEGAL_FILENAME",
        "REPORTING_QUERY_NOT_FOUND",
        "REPORTING_BUCKET_NOT_FOUND",
        "REPORTING_CREATE_BUCKET_FAILED",
        "REPORTING_DELETE_BUCKET_FAILED",
        "REPORTING_UPDATE_BUCKET_PERMISSION_FAILED",
        "REPORTING_WRITE_BUCKET_OBJECT_FAILED",
        "DEPRECATED_REPORTING_INVALID_QUERY",
        "REPORTING_INVALID_QUERY_TOO_MANY_UNFILTERED_LARGE_GROUP_BYS",
        "REPORTING_INVALID_QUERY_TITLE_MISSING",
        "REPORTING_INVALID_QUERY_MISSING_PARTNER_AND_ADVERTISER_FILTERS",
    ]

@typing.type_check_only
class ReportKey(typing_extensions.TypedDict, total=False):
    queryId: str
    reportId: str

@typing.type_check_only
class ReportMetadata(typing_extensions.TypedDict, total=False):
    googleCloudStoragePath: str
    reportDataEndTimeMs: str
    reportDataStartTimeMs: str
    status: ReportStatus

@typing.type_check_only
class ReportStatus(typing_extensions.TypedDict, total=False):
    failure: ReportFailure
    finishTimeMs: str
    format: typing_extensions.Literal["CSV", "EXCEL_CSV", "XLSX"]
    state: typing_extensions.Literal["RUNNING", "DONE", "FAILED"]

@typing.type_check_only
class RowStatus(typing_extensions.TypedDict, total=False):
    changed: bool
    entityId: str
    entityName: str
    errors: typing.List[str]
    persisted: bool
    rowNumber: int

@typing.type_check_only
class RunQueryRequest(typing_extensions.TypedDict, total=False):
    dataRange: typing_extensions.Literal[
        "CUSTOM_DATES",
        "CURRENT_DAY",
        "PREVIOUS_DAY",
        "WEEK_TO_DATE",
        "MONTH_TO_DATE",
        "QUARTER_TO_DATE",
        "YEAR_TO_DATE",
        "PREVIOUS_WEEK",
        "PREVIOUS_HALF_MONTH",
        "PREVIOUS_MONTH",
        "PREVIOUS_QUARTER",
        "PREVIOUS_YEAR",
        "LAST_7_DAYS",
        "LAST_30_DAYS",
        "LAST_90_DAYS",
        "LAST_365_DAYS",
        "ALL_TIME",
        "LAST_14_DAYS",
        "TYPE_NOT_SUPPORTED",
    ]
    reportDataEndTimeMs: str
    reportDataStartTimeMs: str
    timezoneCode: str

@typing.type_check_only
class UploadLineItemsRequest(typing_extensions.TypedDict, total=False):
    dryRun: bool
    format: typing_extensions.Literal["CSV"]
    lineItems: str

@typing.type_check_only
class UploadLineItemsResponse(typing_extensions.TypedDict, total=False):
    uploadStatus: UploadStatus

@typing.type_check_only
class UploadStatus(typing_extensions.TypedDict, total=False):
    errors: typing.List[str]
    rowStatus: typing.List[RowStatus]
