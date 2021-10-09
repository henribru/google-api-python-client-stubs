import typing

import typing_extensions

_list = list

@typing.type_check_only
class DeleteEventsResponse(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class ErrorContext(typing_extensions.TypedDict, total=False):
    httpRequest: HttpRequestContext
    reportLocation: SourceLocation
    sourceReferences: _list[SourceReference]
    user: str

@typing.type_check_only
class ErrorEvent(typing_extensions.TypedDict, total=False):
    context: ErrorContext
    eventTime: str
    message: str
    serviceContext: ServiceContext

@typing.type_check_only
class ErrorGroup(typing_extensions.TypedDict, total=False):
    groupId: str
    name: str
    resolutionStatus: typing_extensions.Literal[
        "RESOLUTION_STATUS_UNSPECIFIED", "OPEN", "ACKNOWLEDGED", "RESOLVED", "MUTED"
    ]
    trackingIssues: _list[TrackingIssue]

@typing.type_check_only
class ErrorGroupStats(typing_extensions.TypedDict, total=False):
    affectedServices: _list[ServiceContext]
    affectedUsersCount: str
    count: str
    firstSeenTime: str
    group: ErrorGroup
    lastSeenTime: str
    numAffectedServices: int
    representative: ErrorEvent
    timedCounts: _list[TimedCount]

@typing.type_check_only
class HttpRequestContext(typing_extensions.TypedDict, total=False):
    method: str
    referrer: str
    remoteIp: str
    responseStatusCode: int
    url: str
    userAgent: str

@typing.type_check_only
class ListEventsResponse(typing_extensions.TypedDict, total=False):
    errorEvents: _list[ErrorEvent]
    nextPageToken: str
    timeRangeBegin: str

@typing.type_check_only
class ListGroupStatsResponse(typing_extensions.TypedDict, total=False):
    errorGroupStats: _list[ErrorGroupStats]
    nextPageToken: str
    timeRangeBegin: str

@typing.type_check_only
class ReportErrorEventResponse(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class ReportedErrorEvent(typing_extensions.TypedDict, total=False):
    context: ErrorContext
    eventTime: str
    message: str
    serviceContext: ServiceContext

@typing.type_check_only
class ServiceContext(typing_extensions.TypedDict, total=False):
    resourceType: str
    service: str
    version: str

@typing.type_check_only
class SourceLocation(typing_extensions.TypedDict, total=False):
    filePath: str
    functionName: str
    lineNumber: int

@typing.type_check_only
class SourceReference(typing_extensions.TypedDict, total=False):
    repository: str
    revisionId: str

@typing.type_check_only
class TimedCount(typing_extensions.TypedDict, total=False):
    count: str
    endTime: str
    startTime: str

@typing.type_check_only
class TrackingIssue(typing_extensions.TypedDict, total=False):
    url: str
