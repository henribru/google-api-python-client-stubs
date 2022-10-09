import typing

import typing_extensions

_list = list

@typing.type_check_only
class ChannelGrouping(typing_extensions.TypedDict, total=False):
    fallbackName: str
    name: str
    rules: _list[Rule]

@typing.type_check_only
class DataRange(typing_extensions.TypedDict, total=False):
    customEndDate: Date
    customStartDate: Date
    range: typing_extensions.Literal[
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
class Date(typing_extensions.TypedDict, total=False):
    day: int
    month: int
    year: int

@typing.type_check_only
class DisjunctiveMatchStatement(typing_extensions.TypedDict, total=False):
    eventFilters: _list[EventFilter]

@typing.type_check_only
class EventFilter(typing_extensions.TypedDict, total=False):
    dimensionFilter: PathQueryOptionsFilter

@typing.type_check_only
class FilterPair(typing_extensions.TypedDict, total=False):
    type: str
    value: str

@typing.type_check_only
class ListQueriesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    queries: _list[Query]

@typing.type_check_only
class ListReportsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    reports: _list[Report]

@typing.type_check_only
class Options(typing_extensions.TypedDict, total=False):
    includeOnlyTargetedUserLists: bool
    pathQueryOptions: PathQueryOptions

@typing.type_check_only
class Parameters(typing_extensions.TypedDict, total=False):
    filters: _list[FilterPair]
    groupBys: _list[str]
    metrics: _list[str]
    options: Options
    type: typing_extensions.Literal[
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
class PathFilter(typing_extensions.TypedDict, total=False):
    eventFilters: _list[EventFilter]
    pathMatchPosition: typing_extensions.Literal[
        "PATH_MATCH_POSITION_UNSPECIFIED", "ANY", "FIRST", "LAST"
    ]

@typing.type_check_only
class PathQueryOptions(typing_extensions.TypedDict, total=False):
    channelGrouping: ChannelGrouping
    pathFilters: _list[PathFilter]

@typing.type_check_only
class PathQueryOptionsFilter(typing_extensions.TypedDict, total=False):
    filter: str
    match: typing_extensions.Literal[
        "UNKNOWN", "EXACT", "PARTIAL", "BEGINS_WITH", "WILDCARD_EXPRESSION"
    ]
    values: _list[str]

@typing.type_check_only
class Query(typing_extensions.TypedDict, total=False):
    metadata: QueryMetadata
    params: Parameters
    queryId: str
    schedule: QuerySchedule

@typing.type_check_only
class QueryMetadata(typing_extensions.TypedDict, total=False):
    dataRange: DataRange
    format: typing_extensions.Literal["FORMAT_UNSPECIFIED", "CSV", "XLSX"]
    sendNotification: bool
    shareEmailAddress: _list[str]
    title: str

@typing.type_check_only
class QuerySchedule(typing_extensions.TypedDict, total=False):
    endDate: Date
    frequency: typing_extensions.Literal[
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
class Report(typing_extensions.TypedDict, total=False):
    key: ReportKey
    metadata: ReportMetadata
    params: Parameters

@typing.type_check_only
class ReportKey(typing_extensions.TypedDict, total=False):
    queryId: str
    reportId: str

@typing.type_check_only
class ReportMetadata(typing_extensions.TypedDict, total=False):
    googleCloudStoragePath: str
    reportDataEndDate: Date
    reportDataStartDate: Date
    status: ReportStatus

@typing.type_check_only
class ReportStatus(typing_extensions.TypedDict, total=False):
    finishTime: str
    format: typing_extensions.Literal["FORMAT_UNSPECIFIED", "CSV", "XLSX"]
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "QUEUED", "RUNNING", "DONE", "FAILED"
    ]

@typing.type_check_only
class Rule(typing_extensions.TypedDict, total=False):
    disjunctiveMatchStatements: _list[DisjunctiveMatchStatement]
    name: str

@typing.type_check_only
class RunQueryRequest(typing_extensions.TypedDict, total=False):
    dataRange: DataRange
