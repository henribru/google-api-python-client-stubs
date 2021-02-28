import typing

import typing_extensions
@typing.type_check_only
class AppEngineHttpQueue(typing_extensions.TypedDict, total=False):
    appEngineRoutingOverride: AppEngineRouting

@typing.type_check_only
class AppEngineHttpRequest(typing_extensions.TypedDict, total=False):
    appEngineRouting: AppEngineRouting
    body: str
    headers: typing.Dict[str, typing.Any]
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
    relativeUri: str

@typing.type_check_only
class AppEngineRouting(typing_extensions.TypedDict, total=False):
    host: str
    instance: str
    service: str
    version: str

@typing.type_check_only
class Attempt(typing_extensions.TypedDict, total=False):
    dispatchTime: str
    responseStatus: Status
    responseTime: str
    scheduleTime: str

@typing.type_check_only
class Binding(typing_extensions.TypedDict, total=False):
    condition: Expr
    members: typing.List[str]
    role: str

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
class HttpRequest(typing_extensions.TypedDict, total=False):
    body: str
    headers: typing.Dict[str, typing.Any]
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
class ListLocationsResponse(typing_extensions.TypedDict, total=False):
    locations: typing.List[Location]
    nextPageToken: str

@typing.type_check_only
class ListQueuesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    queues: typing.List[Queue]

@typing.type_check_only
class ListTasksResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    tasks: typing.List[Task]

@typing.type_check_only
class Location(typing_extensions.TypedDict, total=False):
    displayName: str
    labels: typing.Dict[str, typing.Any]
    locationId: str
    metadata: typing.Dict[str, typing.Any]
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
    bindings: typing.List[Binding]
    etag: str
    version: int

@typing.type_check_only
class PullMessage(typing_extensions.TypedDict, total=False):
    payload: str
    tag: str

@typing.type_check_only
class PurgeQueueRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Queue(typing_extensions.TypedDict, total=False):
    appEngineHttpQueue: AppEngineHttpQueue
    name: str
    purgeTime: str
    rateLimits: RateLimits
    retryConfig: RetryConfig
    stackdriverLoggingConfig: StackdriverLoggingConfig
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "RUNNING", "PAUSED", "DISABLED"
    ]
    stats: QueueStats
    taskTtl: str
    tombstoneTtl: str
    type: typing_extensions.Literal["TYPE_UNSPECIFIED", "PULL", "PUSH"]

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
    maxConcurrentDispatches: int
    maxDispatchesPerSecond: float

@typing.type_check_only
class ResumeQueueRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class RetryConfig(typing_extensions.TypedDict, total=False):
    maxAttempts: int
    maxBackoff: str
    maxDoublings: int
    maxRetryDuration: str
    minBackoff: str

@typing.type_check_only
class RunTaskRequest(typing_extensions.TypedDict, total=False):
    responseView: typing_extensions.Literal["VIEW_UNSPECIFIED", "BASIC", "FULL"]

@typing.type_check_only
class SetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    policy: Policy

@typing.type_check_only
class StackdriverLoggingConfig(typing_extensions.TypedDict, total=False):
    samplingRatio: float

@typing.type_check_only
class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: typing.List[typing.Dict[str, typing.Any]]
    message: str

@typing.type_check_only
class Task(typing_extensions.TypedDict, total=False):
    appEngineHttpRequest: AppEngineHttpRequest
    createTime: str
    dispatchCount: int
    dispatchDeadline: str
    firstAttempt: Attempt
    httpRequest: HttpRequest
    lastAttempt: Attempt
    name: str
    pullMessage: PullMessage
    responseCount: int
    scheduleTime: str
    view: typing_extensions.Literal["VIEW_UNSPECIFIED", "BASIC", "FULL"]

@typing.type_check_only
class TestIamPermissionsRequest(typing_extensions.TypedDict, total=False):
    permissions: typing.List[str]

@typing.type_check_only
class TestIamPermissionsResponse(typing_extensions.TypedDict, total=False):
    permissions: typing.List[str]
