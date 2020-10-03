import typing

import typing_extensions

class RateLimits(typing_extensions.TypedDict, total=False):
    maxConcurrentDispatches: int
    maxDispatchesPerSecond: float
    maxBurstSize: int

class Task(typing_extensions.TypedDict, total=False):
    lastAttempt: Attempt
    httpRequest: HttpRequest
    createTime: str
    view: typing_extensions.Literal["VIEW_UNSPECIFIED", "BASIC", "FULL"]
    firstAttempt: Attempt
    scheduleTime: str
    dispatchDeadline: str
    appEngineHttpRequest: AppEngineHttpRequest
    name: str
    dispatchCount: int
    responseCount: int

class Policy(typing_extensions.TypedDict, total=False):
    bindings: typing.List[Binding]
    version: int
    etag: str

class OidcToken(typing_extensions.TypedDict, total=False):
    audience: str
    serviceAccountEmail: str

class RunTaskRequest(typing_extensions.TypedDict, total=False):
    responseView: typing_extensions.Literal["VIEW_UNSPECIFIED", "BASIC", "FULL"]

class RetryConfig(typing_extensions.TypedDict, total=False):
    maxAttempts: int
    maxRetryDuration: str
    maxBackoff: str
    minBackoff: str
    maxDoublings: int

class AppEngineHttpQueue(typing_extensions.TypedDict, total=False):
    appEngineRoutingOverride: AppEngineRouting

class TestIamPermissionsRequest(typing_extensions.TypedDict, total=False):
    permissions: typing.List[str]

class TestIamPermissionsResponse(typing_extensions.TypedDict, total=False):
    permissions: typing.List[str]

class PurgeQueueRequest(typing_extensions.TypedDict, total=False): ...

class StackdriverLoggingConfig(typing_extensions.TypedDict, total=False):
    samplingRatio: float

class ListQueuesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    queues: typing.List[Queue]

class OAuthToken(typing_extensions.TypedDict, total=False):
    serviceAccountEmail: str
    scope: str

class AppEngineHttpRequest(typing_extensions.TypedDict, total=False):
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
    appEngineRouting: AppEngineRouting
    headers: typing.Dict[str, typing.Any]
    relativeUri: str
    body: str

class AppEngineRouting(typing_extensions.TypedDict, total=False):
    instance: str
    host: str
    service: str
    version: str

class ListLocationsResponse(typing_extensions.TypedDict, total=False):
    locations: typing.List[Location]
    nextPageToken: str

class Attempt(typing_extensions.TypedDict, total=False):
    responseStatus: Status
    responseTime: str
    dispatchTime: str
    scheduleTime: str

class HttpRequest(typing_extensions.TypedDict, total=False):
    oauthToken: OAuthToken
    oidcToken: OidcToken
    headers: typing.Dict[str, typing.Any]
    body: str
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
    url: str

class CreateTaskRequest(typing_extensions.TypedDict, total=False):
    task: Task
    responseView: typing_extensions.Literal["VIEW_UNSPECIFIED", "BASIC", "FULL"]

class PauseQueueRequest(typing_extensions.TypedDict, total=False): ...

class ListTasksResponse(typing_extensions.TypedDict, total=False):
    tasks: typing.List[Task]
    nextPageToken: str

class ResumeQueueRequest(typing_extensions.TypedDict, total=False): ...
class Empty(typing_extensions.TypedDict, total=False): ...

class Expr(typing_extensions.TypedDict, total=False):
    description: str
    title: str
    expression: str
    location: str

class GetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    options: GetPolicyOptions

class SetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    policy: Policy

class Binding(typing_extensions.TypedDict, total=False):
    role: str
    condition: Expr
    bindingId: str
    members: typing.List[str]

class Status(typing_extensions.TypedDict, total=False):
    details: typing.List[typing.Dict[str, typing.Any]]
    message: str
    code: int

class Queue(typing_extensions.TypedDict, total=False):
    appEngineHttpQueue: AppEngineHttpQueue
    purgeTime: str
    name: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "RUNNING", "PAUSED", "DISABLED"
    ]
    type: typing_extensions.Literal["TYPE_UNSPECIFIED", "PULL", "PUSH"]
    retryConfig: RetryConfig
    stackdriverLoggingConfig: StackdriverLoggingConfig
    rateLimits: RateLimits

class Location(typing_extensions.TypedDict, total=False):
    name: str
    displayName: str
    labels: typing.Dict[str, typing.Any]
    locationId: str
    metadata: typing.Dict[str, typing.Any]

class GetPolicyOptions(typing_extensions.TypedDict, total=False):
    requestedPolicyVersion: int
