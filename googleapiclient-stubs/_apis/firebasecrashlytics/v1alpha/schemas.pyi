import typing

import typing_extensions

_list = list

@typing.type_check_only
class BatchGetEventsResponse(typing_extensions.TypedDict, total=False):
    events: _list[Event]

@typing.type_check_only
class BatchUpdateIssuesRequest(typing_extensions.TypedDict, total=False):
    requests: _list[UpdateIssueRequest]
    updateMask: str

@typing.type_check_only
class BatchUpdateIssuesResponse(typing_extensions.TypedDict, total=False):
    issues: _list[Issue]

@typing.type_check_only
class Breadcrumb(typing_extensions.TypedDict, total=False):
    eventTime: str
    params: dict[str, typing.Any]
    title: str

@typing.type_check_only
class Browser(typing_extensions.TypedDict, total=False):
    browser: str
    displayName: str
    displayVersion: str

@typing.type_check_only
class DeleteUserCrashReportsResponse(typing_extensions.TypedDict, total=False):
    targetCompleteTime: str

@typing.type_check_only
class Device(typing_extensions.TypedDict, total=False):
    architecture: str
    companyName: str
    displayName: str
    formFactor: typing_extensions.Literal[
        "FORM_FACTOR_UNSPECIFIED", "PHONE", "TABLET", "DESKTOP", "TV", "WATCH"
    ]
    manufacturer: str
    marketingName: str
    model: str

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Error(typing_extensions.TypedDict, total=False):
    blamed: bool
    code: str
    frames: _list[Frame]
    queue: str
    subtitle: str
    title: str

@typing.type_check_only
class Event(typing_extensions.TypedDict, total=False):
    appOrientation: str
    blameFrame: Frame
    breadcrumbs: _list[Breadcrumb]
    browser: Browser
    buildStamp: str
    bundleOrPackage: str
    crashlyticsSdkVersion: str
    customKeys: dict[str, typing.Any]
    device: Device
    deviceOrientation: str
    errors: _list[Error]
    eventId: str
    eventTime: str
    exceptions: _list[Exception]
    installationUuid: str
    issue: Issue
    issueSubtitle: str
    issueTitle: str
    issueVariant: IssueVariant
    logs: _list[Log]
    memory: Memory
    name: str
    operatingSystem: OperatingSystem
    platform: str
    processState: str
    receivedTime: str
    routePath: str
    sessionId: str
    storage: Storage
    threads: _list[Thread]
    user: User
    version: Version

@typing.type_check_only
class Exception(typing_extensions.TypedDict, total=False):
    blamed: bool
    exceptionMessage: str
    frames: _list[Frame]
    nested: bool
    subtitle: str
    title: str
    type: str

@typing.type_check_only
class FirebaseSessionEvent(typing_extensions.TypedDict, total=False):
    device: Device
    eventTime: str
    eventType: typing_extensions.Literal["SESSION_EVENT_TYPE_UNKNOWN", "SESSION_START"]
    firebaseInstallationId: str
    firstSessionId: str
    operatingSystem: OperatingSystem
    sessionId: str
    sessionIndex: int
    version: Version

@typing.type_check_only
class Frame(typing_extensions.TypedDict, total=False):
    address: str
    blamed: bool
    column: str
    file: str
    library: str
    line: str
    offset: str
    owner: str
    symbol: str

@typing.type_check_only
class IntervalMetrics(typing_extensions.TypedDict, total=False):
    endTime: str
    eventsCount: str
    impactedUsersCount: str
    sessionsCount: str
    startTime: str

@typing.type_check_only
class Issue(typing_extensions.TypedDict, total=False):
    errorType: typing_extensions.Literal[
        "ERROR_TYPE_UNSPECIFIED", "FATAL", "NON_FATAL", "ANR"
    ]
    firstSeenTime: str
    firstSeenVersion: str
    id: str
    lastSeenTime: str
    lastSeenVersion: str
    name: str
    notesCount: str
    sampleEvent: str
    signals: _list[IssueSignals]
    state: typing_extensions.Literal["STATE_UNSPECIFIED", "OPEN", "CLOSED", "MUTED"]
    stateUpdateTime: str
    subtitle: str
    title: str
    uri: str
    variants: _list[IssueVariant]

@typing.type_check_only
class IssueSignals(typing_extensions.TypedDict, total=False):
    description: str
    signal: typing_extensions.Literal[
        "SIGNAL_UNSPECIFIED",
        "SIGNAL_EARLY",
        "SIGNAL_FRESH",
        "SIGNAL_REGRESSED",
        "SIGNAL_REPETITIVE",
    ]

@typing.type_check_only
class IssueVariant(typing_extensions.TypedDict, total=False):
    id: str
    sampleEvent: str
    uri: str

@typing.type_check_only
class ListEventsResponse(typing_extensions.TypedDict, total=False):
    events: _list[Event]
    nextPageToken: str

@typing.type_check_only
class ListNotesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    notes: _list[Note]

@typing.type_check_only
class ListReportsResponse(typing_extensions.TypedDict, total=False):
    reports: _list[Report]

@typing.type_check_only
class Log(typing_extensions.TypedDict, total=False):
    logTime: str
    message: str

@typing.type_check_only
class Memory(typing_extensions.TypedDict, total=False):
    free: str
    used: str

@typing.type_check_only
class Note(typing_extensions.TypedDict, total=False):
    author: str
    body: str
    createTime: str
    name: str

@typing.type_check_only
class OperatingSystem(typing_extensions.TypedDict, total=False):
    deviceType: str
    displayName: str
    displayVersion: str
    modificationState: str
    os: str
    type: str

@typing.type_check_only
class PlayTrack(typing_extensions.TypedDict, total=False):
    title: str
    type: typing_extensions.Literal[
        "TRACK_TYPE_UNSPECIFIED",
        "TRACK_TYPE_PROD",
        "TRACK_TYPE_INTERNAL",
        "TRACK_TYPE_OPEN_TESTING",
        "TRACK_TYPE_CLOSED_TESTING",
        "TRACK_TYPE_EARLY_ACCESS",
    ]

@typing.type_check_only
class Report(typing_extensions.TypedDict, total=False):
    displayName: str
    groups: _list[ReportGroup]
    name: str
    nextPageToken: str
    totalSize: int
    usage: str

@typing.type_check_only
class ReportGroup(typing_extensions.TypedDict, total=False):
    browser: Browser
    device: Device
    issue: Issue
    metrics: _list[IntervalMetrics]
    operatingSystem: OperatingSystem
    subgroups: _list[ReportGroup]
    variant: IssueVariant
    version: Version
    webMetricsGroup: WebMetricsGroup

@typing.type_check_only
class Storage(typing_extensions.TypedDict, total=False):
    free: str
    used: str

@typing.type_check_only
class Thread(typing_extensions.TypedDict, total=False):
    blamed: bool
    crashAddress: str
    crashed: bool
    frames: _list[Frame]
    name: str
    queue: str
    signal: str
    signalCode: str
    subtitle: str
    sysThreadId: str
    threadId: str
    threadState: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "THREAD_STATE_TERMINATED",
        "THREAD_STATE_RUNNABLE",
        "THREAD_STATE_TIMED_WAITING",
        "THREAD_STATE_BLOCKED",
        "THREAD_STATE_WAITING",
        "THREAD_STATE_NEW",
        "THREAD_STATE_NATIVE_RUNNABLE",
        "THREAD_STATE_NATIVE_WAITING",
    ]
    title: str

@typing.type_check_only
class UpdateIssueRequest(typing_extensions.TypedDict, total=False):
    issue: Issue
    updateMask: str

@typing.type_check_only
class User(typing_extensions.TypedDict, total=False):
    id: str

@typing.type_check_only
class Version(typing_extensions.TypedDict, total=False):
    buildVersion: str
    displayName: str
    displayVersion: str
    tracks: _list[PlayTrack]

@typing.type_check_only
class WebMetricsGroup(typing_extensions.TypedDict, total=False):
    id: str
