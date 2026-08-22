import typing

_list = list

@typing.type_check_only
class DataRange(typing.TypedDict, total=False):
    customEndDate: Date
    customStartDate: Date
    range: typing.Literal[
        "RANGE_UNSPECIFIED",
        "CUSTOM_DATES",
        "CURRENT_DAY",
        "PREVIOUS_DAY",
        "WEEK_TO_DATE",
        "MONTH_TO_DATE",
        "QUARTER_TO_DATE",
        "YEAR_TO_DATE",
        "PREVIOUS_WEEK",
        "PREVIOUS_MONTH",
        "PREVIOUS_QUARTER",
        "PREVIOUS_YEAR",
        "LAST_7_DAYS",
        "LAST_30_DAYS",
        "LAST_90_DAYS",
        "LAST_365_DAYS",
        "ALL_TIME",
        "LAST_14_DAYS",
        "LAST_60_DAYS",
    ]

@typing.type_check_only
class Date(typing.TypedDict, total=False):
    day: int
    month: int
    year: int

@typing.type_check_only
class FilterPair(typing.TypedDict, total=False):
    type: str
    value: str

@typing.type_check_only
class ListQueriesResponse(typing.TypedDict, total=False):
    nextPageToken: str
    queries: _list[Query]

@typing.type_check_only
class ListReportsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    reports: _list[Report]

@typing.type_check_only
class Options(typing.TypedDict, total=False):
    includeOnlyTargetedUserLists: bool

@typing.type_check_only
class Parameters(typing.TypedDict, total=False):
    filters: _list[FilterPair]
    groupBys: _list[str]
    metrics: _list[str]
    options: Options
    type: typing.Literal[
        "REPORT_TYPE_UNSPECIFIED",
        "STANDARD",
        "INVENTORY_AVAILABILITY",
        "AUDIENCE_COMPOSITION",
        "FLOODLIGHT",
        "YOUTUBE",
        "GRP",
        "YOUTUBE_PROGRAMMATIC_GUARANTEED",
        "REACH",
        "UNIQUE_REACH_AUDIENCE",
        "FULL_PATH",
        "PATH_ATTRIBUTION",
    ]

@typing.type_check_only
class Query(typing.TypedDict, total=False):
    metadata: QueryMetadata
    params: Parameters
    queryId: str
    schedule: QuerySchedule

@typing.type_check_only
class QueryMetadata(typing.TypedDict, total=False):
    dataRange: DataRange
    format: typing.Literal["FORMAT_UNSPECIFIED", "CSV", "XLSX"]
    sendNotification: bool
    shareEmailAddress: _list[str]
    title: str

@typing.type_check_only
class QuerySchedule(typing.TypedDict, total=False):
    endDate: Date
    frequency: typing.Literal[
        "FREQUENCY_UNSPECIFIED",
        "ONE_TIME",
        "DAILY",
        "WEEKLY",
        "SEMI_MONTHLY",
        "MONTHLY",
        "QUARTERLY",
        "YEARLY",
    ]
    nextRunTimezoneCode: str
    startDate: Date

@typing.type_check_only
class Report(typing.TypedDict, total=False):
    key: ReportKey
    metadata: ReportMetadata
    params: Parameters

@typing.type_check_only
class ReportKey(typing.TypedDict, total=False):
    queryId: str
    reportId: str

@typing.type_check_only
class ReportMetadata(typing.TypedDict, total=False):
    googleCloudStoragePath: str
    reportDataEndDate: Date
    reportDataStartDate: Date
    status: ReportStatus

@typing.type_check_only
class ReportStatus(typing.TypedDict, total=False):
    finishTime: str
    format: typing.Literal["FORMAT_UNSPECIFIED", "CSV", "XLSX"]
    state: typing.Literal["STATE_UNSPECIFIED", "QUEUED", "RUNNING", "DONE", "FAILED"]

@typing.type_check_only
class RunQueryRequest(typing.TypedDict, total=False):
    dataRange: DataRange
