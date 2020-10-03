import typing

import typing_extensions

class DeleteEventsResponse(typing_extensions.TypedDict, total=False): ...

class ListEventsResponse(typing_extensions.TypedDict, total=False):
    errorEvents: typing.List[ErrorEvent]
    timeRangeBegin: str
    nextPageToken: str

class ServiceContext(typing_extensions.TypedDict, total=False):
    resourceType: str
    service: str
    version: str

class HttpRequestContext(typing_extensions.TypedDict, total=False):
    referrer: str
    userAgent: str
    remoteIp: str
    method: str
    url: str
    responseStatusCode: int

class TrackingIssue(typing_extensions.TypedDict, total=False):
    url: str

class ReportedErrorEvent(typing_extensions.TypedDict, total=False):
    message: str
    serviceContext: ServiceContext
    eventTime: str
    context: ErrorContext

class SourceReference(typing_extensions.TypedDict, total=False):
    revisionId: str
    repository: str

class ErrorContext(typing_extensions.TypedDict, total=False):
    sourceReferences: typing.List[SourceReference]
    reportLocation: SourceLocation
    httpRequest: HttpRequestContext
    user: str

class ListGroupStatsResponse(typing_extensions.TypedDict, total=False):
    errorGroupStats: typing.List[ErrorGroupStats]
    timeRangeBegin: str
    nextPageToken: str

class TimedCount(typing_extensions.TypedDict, total=False):
    startTime: str
    count: str
    endTime: str

class ErrorGroupStats(typing_extensions.TypedDict, total=False):
    timedCounts: typing.List[TimedCount]
    group: ErrorGroup
    representative: ErrorEvent
    affectedServices: typing.List[ServiceContext]
    count: str
    firstSeenTime: str
    affectedUsersCount: str
    numAffectedServices: int
    lastSeenTime: str

class ErrorEvent(typing_extensions.TypedDict, total=False):
    serviceContext: ServiceContext
    message: str
    eventTime: str
    context: ErrorContext

class SourceLocation(typing_extensions.TypedDict, total=False):
    filePath: str
    lineNumber: int
    functionName: str

class ReportErrorEventResponse(typing_extensions.TypedDict, total=False): ...

class ErrorGroup(typing_extensions.TypedDict, total=False):
    resolutionStatus: typing_extensions.Literal[
        "RESOLUTION_STATUS_UNSPECIFIED", "OPEN", "ACKNOWLEDGED", "RESOLVED", "MUTED"
    ]
    name: str
    trackingIssues: typing.List[TrackingIssue]
    groupId: str
