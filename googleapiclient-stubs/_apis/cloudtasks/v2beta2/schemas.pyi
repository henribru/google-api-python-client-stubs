import typing

_list = list

@typing.type_check_only
class AcknowledgeTaskRequest(typing.TypedDict, total=False):
    scheduleTime: str

@typing.type_check_only
class AppEngineHttpRequest(typing.TypedDict, total=False):
    appEngineRouting: AppEngineRouting
    headers: dict[str, typing.Any]
    httpMethod: typing.Literal[
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
class AppEngineHttpTarget(typing.TypedDict, total=False):
    appEngineRoutingOverride: AppEngineRouting

@typing.type_check_only
class AppEngineRouting(typing.TypedDict, total=False):
    host: str
    instance: str
    service: str
    version: str

@typing.type_check_only
class AttemptStatus(typing.TypedDict, total=False):
    dispatchTime: str
    responseStatus: Status
    responseTime: str
    scheduleTime: str

@typing.type_check_only
class BatchCreateTasksRequest(typing.TypedDict, total=False):
    requestId: str
    requests: _list[CreateTaskRequest]

@typing.type_check_only
class BatchDeleteTasksRequest(typing.TypedDict, total=False):
    names: _list[str]
    requestId: str

@typing.type_check_only
class Binding(typing.TypedDict, total=False):
    condition: Expr
    members: _list[str]
    role: str

@typing.type_check_only
class BufferTaskRequest(typing.TypedDict, total=False):
    body: HttpBody

@typing.type_check_only
class BufferTaskResponse(typing.TypedDict, total=False):
    task: Task

@typing.type_check_only
class CancelLeaseRequest(typing.TypedDict, total=False):
    responseView: typing.Literal["VIEW_UNSPECIFIED", "BASIC", "FULL"]
    scheduleTime: str

@typing.type_check_only
class CmekConfig(typing.TypedDict, total=False):
    kmsKey: str
    name: str

@typing.type_check_only
class CreateTaskRequest(typing.TypedDict, total=False):
    parent: str
    responseView: typing.Literal["VIEW_UNSPECIFIED", "BASIC", "FULL"]
    task: Task

@typing.type_check_only
class Empty(typing.TypedDict, total=False): ...

@typing.type_check_only
class Expr(typing.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str

@typing.type_check_only
class GetIamPolicyRequest(typing.TypedDict, total=False):
    options: GetPolicyOptions

@typing.type_check_only
class GetPolicyOptions(typing.TypedDict, total=False):
    requestedPolicyVersion: int

@typing.type_check_only
class Header(typing.TypedDict, total=False):
    key: str
    value: str

@typing.type_check_only
class HeaderOverride(typing.TypedDict, total=False):
    header: Header

@typing.type_check_only
class HttpBody(typing.TypedDict, total=False):
    contentType: str
    data: str
    extensions: _list[dict[str, typing.Any]]

@typing.type_check_only
class HttpRequest(typing.TypedDict, total=False):
    body: str
    headers: dict[str, typing.Any]
    httpMethod: typing.Literal[
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
class HttpTarget(typing.TypedDict, total=False):
    headerOverrides: _list[HeaderOverride]
    httpMethod: typing.Literal[
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
class LeaseTasksRequest(typing.TypedDict, total=False):
    filter: str
    leaseDuration: str
    maxTasks: int
    responseView: typing.Literal["VIEW_UNSPECIFIED", "BASIC", "FULL"]

@typing.type_check_only
class LeaseTasksResponse(typing.TypedDict, total=False):
    tasks: _list[Task]

@typing.type_check_only
class ListLocationsResponse(typing.TypedDict, total=False):
    locations: _list[Location]
    nextPageToken: str

@typing.type_check_only
class ListQueuesResponse(typing.TypedDict, total=False):
    nextPageToken: str
    queues: _list[Queue]

@typing.type_check_only
class ListTasksResponse(typing.TypedDict, total=False):
    nextPageToken: str
    tasks: _list[Task]

@typing.type_check_only
class Location(typing.TypedDict, total=False):
    displayName: str
    labels: dict[str, typing.Any]
    locationId: str
    metadata: dict[str, typing.Any]
    name: str

@typing.type_check_only
class OAuthToken(typing.TypedDict, total=False):
    scope: str
    serviceAccountEmail: str

@typing.type_check_only
class OidcToken(typing.TypedDict, total=False):
    audience: str
    serviceAccountEmail: str

@typing.type_check_only
class Operation(typing.TypedDict, total=False):
    done: bool
    error: Status
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class PathOverride(typing.TypedDict, total=False):
    path: str

@typing.type_check_only
class PauseQueueRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class Policy(typing.TypedDict, total=False):
    bindings: _list[Binding]
    etag: str
    version: int

@typing.type_check_only
class PullMessage(typing.TypedDict, total=False):
    payload: str
    tag: str

@typing.type_check_only
class PullTarget(typing.TypedDict, total=False): ...

@typing.type_check_only
class PurgeQueueRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class QueryOverride(typing.TypedDict, total=False):
    queryParams: str

@typing.type_check_only
class Queue(typing.TypedDict, total=False):
    appEngineHttpTarget: AppEngineHttpTarget
    httpTarget: HttpTarget
    name: str
    pullTarget: PullTarget
    purgeTime: str
    rateLimits: RateLimits
    retryConfig: RetryConfig
    state: typing.Literal["STATE_UNSPECIFIED", "RUNNING", "PAUSED", "DISABLED"]
    stats: QueueStats
    taskTtl: str
    tombstoneTtl: str

@typing.type_check_only
class QueueStats(typing.TypedDict, total=False):
    concurrentDispatchesCount: str
    effectiveExecutionRate: float
    executedLastMinuteCount: str
    oldestEstimatedArrivalTime: str
    tasksCount: str

@typing.type_check_only
class RateLimits(typing.TypedDict, total=False):
    maxBurstSize: int
    maxConcurrentTasks: int
    maxTasksDispatchedPerSecond: float

@typing.type_check_only
class RenewLeaseRequest(typing.TypedDict, total=False):
    leaseDuration: str
    responseView: typing.Literal["VIEW_UNSPECIFIED", "BASIC", "FULL"]
    scheduleTime: str

@typing.type_check_only
class ResumeQueueRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class RetryConfig(typing.TypedDict, total=False):
    maxAttempts: int
    maxBackoff: str
    maxDoublings: int
    maxRetryDuration: str
    minBackoff: str
    unlimitedAttempts: bool

@typing.type_check_only
class RunTaskRequest(typing.TypedDict, total=False):
    responseView: typing.Literal["VIEW_UNSPECIFIED", "BASIC", "FULL"]

@typing.type_check_only
class SetIamPolicyRequest(typing.TypedDict, total=False):
    policy: Policy

@typing.type_check_only
class Status(typing.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class Task(typing.TypedDict, total=False):
    appEngineHttpRequest: AppEngineHttpRequest
    createTime: str
    httpRequest: HttpRequest
    name: str
    pullMessage: PullMessage
    retryConfig: RetryConfig
    scheduleTime: str
    status: TaskStatus
    view: typing.Literal["VIEW_UNSPECIFIED", "BASIC", "FULL"]

@typing.type_check_only
class TaskStatus(typing.TypedDict, total=False):
    attemptDispatchCount: int
    attemptResponseCount: int
    firstAttemptStatus: AttemptStatus
    lastAttemptStatus: AttemptStatus

@typing.type_check_only
class TestIamPermissionsRequest(typing.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class TestIamPermissionsResponse(typing.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class UriOverride(typing.TypedDict, total=False):
    host: str
    pathOverride: PathOverride
    port: str
    queryOverride: QueryOverride
    scheme: typing.Literal["SCHEME_UNSPECIFIED", "HTTP", "HTTPS"]
    uriOverrideEnforceMode: typing.Literal[
        "URI_OVERRIDE_ENFORCE_MODE_UNSPECIFIED", "IF_NOT_EXISTS", "ALWAYS"
    ]
