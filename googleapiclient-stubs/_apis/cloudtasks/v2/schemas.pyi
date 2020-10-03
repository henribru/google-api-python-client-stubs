import typing

import typing_extensions

class Task(typing_extensions.TypedDict, total=False):
    dispatchDeadline: str
    appEngineHttpRequest: AppEngineHttpRequest
    lastAttempt: Attempt
    scheduleTime: str
    dispatchCount: int
    httpRequest: HttpRequest
    responseCount: int
    createTime: str
    name: str
    firstAttempt: Attempt
    view: typing_extensions.Literal["VIEW_UNSPECIFIED", "BASIC", "FULL"]

class RunTaskRequest(typing_extensions.TypedDict, total=False):
    responseView: typing_extensions.Literal["VIEW_UNSPECIFIED", "BASIC", "FULL"]

class Binding(typing_extensions.TypedDict, total=False):
    condition: Expr
    role: str
    bindingId: str
    members: typing.List[str]

class Empty(typing_extensions.TypedDict, total=False): ...

class ListTasksResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    tasks: typing.List[Task]

class PurgeQueueRequest(typing_extensions.TypedDict, total=False): ...

class TestIamPermissionsResponse(typing_extensions.TypedDict, total=False):
    permissions: typing.List[str]

class RateLimits(typing_extensions.TypedDict, total=False):
    maxConcurrentDispatches: int
    maxDispatchesPerSecond: float
    maxBurstSize: int

class ResumeQueueRequest(typing_extensions.TypedDict, total=False): ...

class GetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    options: GetPolicyOptions

class AppEngineRouting(typing_extensions.TypedDict, total=False):
    service: str
    host: str
    instance: str
    version: str

class RetryConfig(typing_extensions.TypedDict, total=False):
    maxAttempts: int
    maxRetryDuration: str
    maxBackoff: str
    minBackoff: str
    maxDoublings: int

class ListLocationsResponse(typing_extensions.TypedDict, total=False):
    locations: typing.List[Location]
    nextPageToken: str

class ListQueuesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    queues: typing.List[Queue]

class StackdriverLoggingConfig(typing_extensions.TypedDict, total=False):
    samplingRatio: float

class Expr(typing_extensions.TypedDict, total=False):
    title: str
    description: str
    expression: str
    location: str

class GetPolicyOptions(typing_extensions.TypedDict, total=False):
    requestedPolicyVersion: int

class AppEngineHttpRequest(typing_extensions.TypedDict, total=False):
    body: str
    relativeUri: str
    appEngineRouting: AppEngineRouting
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

class HttpRequest(typing_extensions.TypedDict, total=False):
    body: str
    oauthToken: OAuthToken
    headers: typing.Dict[str, typing.Any]
    oidcToken: OidcToken
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

class Status(typing_extensions.TypedDict, total=False):
    code: int
    message: str
    details: typing.List[typing.Dict[str, typing.Any]]

class Location(typing_extensions.TypedDict, total=False):
    name: str
    metadata: typing.Dict[str, typing.Any]
    locationId: str
    labels: typing.Dict[str, typing.Any]
    displayName: str

class PauseQueueRequest(typing_extensions.TypedDict, total=False): ...

class Attempt(typing_extensions.TypedDict, total=False):
    dispatchTime: str
    scheduleTime: str
    responseTime: str
    responseStatus: Status

class OAuthToken(typing_extensions.TypedDict, total=False):
    scope: str
    serviceAccountEmail: str

class Policy(typing_extensions.TypedDict, total=False):
    bindings: typing.List[Binding]
    version: int
    etag: str

class TestIamPermissionsRequest(typing_extensions.TypedDict, total=False):
    permissions: typing.List[str]

class CreateTaskRequest(typing_extensions.TypedDict, total=False):
    responseView: typing_extensions.Literal["VIEW_UNSPECIFIED", "BASIC", "FULL"]
    task: Task

class OidcToken(typing_extensions.TypedDict, total=False):
    serviceAccountEmail: str
    audience: str

class Queue(typing_extensions.TypedDict, total=False):
    retryConfig: RetryConfig
    stackdriverLoggingConfig: StackdriverLoggingConfig
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "RUNNING", "PAUSED", "DISABLED"
    ]
    appEngineRoutingOverride: AppEngineRouting
    purgeTime: str
    name: str
    rateLimits: RateLimits

class SetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    policy: Policy
