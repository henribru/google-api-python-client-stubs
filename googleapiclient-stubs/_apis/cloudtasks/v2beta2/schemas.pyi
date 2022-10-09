import typing

import typing_extensions

_list = list

@typing.type_check_only
class AcknowledgeTaskRequest(typing_extensions.TypedDict, total=False):
    scheduleTime: str

@typing.type_check_only
class AppEngineHttpRequest(typing_extensions.TypedDict, total=False):
    appEngineRouting: AppEngineRouting
    headers: dict[str, typing.Any]
    httpMethod: typing_extensions.Literal[
        "HTTP_METHOD_UNSPECIFIED",
        "POST",
        "GET",
        "HEAD",
        "PUT",
        "DELETE",
        "PATCH",
        "OPTIONS",
    ]
    payload: str
    relativeUrl: str

@typing.type_check_only
class AppEngineHttpTarget(typing_extensions.TypedDict, total=False):
    appEngineRoutingOverride: AppEngineRouting

@typing.type_check_only
class AppEngineRouting(typing_extensions.TypedDict, total=False):
    host: str
    instance: str
    service: str
    version: str

@typing.type_check_only
class AttemptStatus(typing_extensions.TypedDict, total=False):
    dispatchTime: str
    responseStatus: Status
    responseTime: str
    scheduleTime: str

@typing.type_check_only
class Binding(typing_extensions.TypedDict, total=False):
    condition: Expr
    members: _list[str]
    role: str

@typing.type_check_only
class BufferTaskRequest(typing_extensions.TypedDict, total=False):
    body: HttpBody

@typing.type_check_only
class BufferTaskResponse(typing_extensions.TypedDict, total=False):
    task: Task

@typing.type_check_only
class CancelLeaseRequest(typing_extensions.TypedDict, total=False):
    responseView: typing_extensions.Literal["VIEW_UNSPECIFIED", "BASIC", "FULL"]
    scheduleTime: str

@typing.type_check_only
class CreateTaskRequest(typing_extensions.TypedDict, total=False):
    responseView: typing_extensions.Literal["VIEW_UNSPECIFIED", "BASIC", "FULL"]
    task: Task

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Expr(typing_extensions.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str

@typing.type_check_only
class GetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    options: GetPolicyOptions

@typing.type_check_only
class GetPolicyOptions(typing_extensions.TypedDict, total=False):
    requestedPolicyVersion: int

@typing.type_check_only
class Header(typing_extensions.TypedDict, total=False):
    key: str
    value: str

@typing.type_check_only
class HeaderOverride(typing_extensions.TypedDict, total=False):
    header: Header

@typing.type_check_only
class HttpBody(typing_extensions.TypedDict, total=False):
    contentType: str
    data: str
    extensions: _list[dict[str, typing.Any]]

@typing.type_check_only
class HttpRequest(typing_extensions.TypedDict, total=False):
    body: str
    headers: dict[str, typing.Any]
    httpMethod: typing_extensions.Literal[
        "HTTP_METHOD_UNSPECIFIED",
        "POST",
        "GET",
        "HEAD",
        "PUT",
        "DELETE",
        "PATCH",
        "OPTIONS",
    ]
    oauthToken: OAuthToken
    oidcToken: OidcToken
    url: str

@typing.type_check_only
class HttpTarget(typing_extensions.TypedDict, total=False):
    headerOverrides: _list[HeaderOverride]
    httpMethod: typing_extensions.Literal[
        "HTTP_METHOD_UNSPECIFIED",
        "POST",
        "GET",
        "HEAD",
        "PUT",
        "DELETE",
        "PATCH",
        "OPTIONS",
    ]
    oauthToken: OAuthToken
    oidcToken: OidcToken
    uriOverride: UriOverride

@typing.type_check_only
class LeaseTasksRequest(typing_extensions.TypedDict, total=False):
    filter: str
    leaseDuration: str
    maxTasks: int
    responseView: typing_extensions.Literal["VIEW_UNSPECIFIED", "BASIC", "FULL"]

@typing.type_check_only
class LeaseTasksResponse(typing_extensions.TypedDict, total=False):
    tasks: _list[Task]

@typing.type_check_only
class ListLocationsResponse(typing_extensions.TypedDict, total=False):
    locations: _list[Location]
    nextPageToken: str

@typing.type_check_only
class ListQueuesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    queues: _list[Queue]

@typing.type_check_only
class ListTasksResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    tasks: _list[Task]

@typing.type_check_only
class Location(typing_extensions.TypedDict, total=False):
    displayName: str
    labels: dict[str, typing.Any]
    locationId: str
    metadata: dict[str, typing.Any]
    name: str

@typing.type_check_only
class OAuthToken(typing_extensions.TypedDict, total=False):
    scope: str
    serviceAccountEmail: str

@typing.type_check_only
class OidcToken(typing_extensions.TypedDict, total=False):
    audience: str
    serviceAccountEmail: str

@typing.type_check_only
class PauseQueueRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Policy(typing_extensions.TypedDict, total=False):
    bindings: _list[Binding]
    etag: str
    version: int

@typing.type_check_only
class PullMessage(typing_extensions.TypedDict, total=False):
    payload: str
    tag: str

@typing.type_check_only
class PullTarget(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class PurgeQueueRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Queue(typing_extensions.TypedDict, total=False):
    appEngineHttpTarget: AppEngineHttpTarget
    httpTarget: HttpTarget
    name: str
    pullTarget: PullTarget
    purgeTime: str
    rateLimits: RateLimits
    retryConfig: RetryConfig
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "RUNNING", "PAUSED", "DISABLED"
    ]
    stats: QueueStats
    taskTtl: str
    tombstoneTtl: str

@typing.type_check_only
class QueueStats(typing_extensions.TypedDict, total=False):
    concurrentDispatchesCount: str
    effectiveExecutionRate: float
    executedLastMinuteCount: str
    oldestEstimatedArrivalTime: str
    tasksCount: str

@typing.type_check_only
class RateLimits(typing_extensions.TypedDict, total=False):
    maxBurstSize: int
    maxConcurrentTasks: int
    maxTasksDispatchedPerSecond: float

@typing.type_check_only
class RenewLeaseRequest(typing_extensions.TypedDict, total=False):
    leaseDuration: str
    responseView: typing_extensions.Literal["VIEW_UNSPECIFIED", "BASIC", "FULL"]
    scheduleTime: str

@typing.type_check_only
class ResumeQueueRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class RetryConfig(typing_extensions.TypedDict, total=False):
    maxAttempts: int
    maxBackoff: str
    maxDoublings: int
    maxRetryDuration: str
    minBackoff: str
    unlimitedAttempts: bool

@typing.type_check_only
class RunTaskRequest(typing_extensions.TypedDict, total=False):
    responseView: typing_extensions.Literal["VIEW_UNSPECIFIED", "BASIC", "FULL"]

@typing.type_check_only
class SetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    policy: Policy

@typing.type_check_only
class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class Task(typing_extensions.TypedDict, total=False):
    appEngineHttpRequest: AppEngineHttpRequest
    createTime: str
    httpRequest: HttpRequest
    name: str
    pullMessage: PullMessage
    scheduleTime: str
    status: TaskStatus
    view: typing_extensions.Literal["VIEW_UNSPECIFIED", "BASIC", "FULL"]

@typing.type_check_only
class TaskStatus(typing_extensions.TypedDict, total=False):
    attemptDispatchCount: int
    attemptResponseCount: int
    firstAttemptStatus: AttemptStatus
    lastAttemptStatus: AttemptStatus

@typing.type_check_only
class TestIamPermissionsRequest(typing_extensions.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class TestIamPermissionsResponse(typing_extensions.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class UriOverride(typing_extensions.TypedDict, total=False):
    host: str
    path: str
    port: str
    query: str
    scheme: typing_extensions.Literal["SCHEME_UNSPECIFIED", "HTTP", "HTTPS"]
