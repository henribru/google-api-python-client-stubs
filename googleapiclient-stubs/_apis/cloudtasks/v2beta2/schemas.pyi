import typing

import typing_extensions

class Policy(typing_extensions.TypedDict, total=False):
    etag: str
    version: int
    bindings: typing.List[Binding]

class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: typing.List[typing.Dict[str, typing.Any]]
    message: str

class Task(typing_extensions.TypedDict, total=False):
    scheduleTime: str
    view: typing_extensions.Literal["VIEW_UNSPECIFIED", "BASIC", "FULL"]
    pullMessage: PullMessage
    createTime: str
    status: TaskStatus
    appEngineHttpRequest: AppEngineHttpRequest
    name: str

class AttemptStatus(typing_extensions.TypedDict, total=False):
    dispatchTime: str
    scheduleTime: str
    responseStatus: Status
    responseTime: str

class Expr(typing_extensions.TypedDict, total=False):
    title: str
    location: str
    expression: str
    description: str

class Queue(typing_extensions.TypedDict, total=False):
    name: str
    appEngineHttpTarget: AppEngineHttpTarget
    pullTarget: PullTarget
    retryConfig: RetryConfig
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "RUNNING", "PAUSED", "DISABLED"
    ]
    rateLimits: RateLimits
    purgeTime: str

class ListLocationsResponse(typing_extensions.TypedDict, total=False):
    locations: typing.List[Location]
    nextPageToken: str

class PullMessage(typing_extensions.TypedDict, total=False):
    tag: str
    payload: str

class ListQueuesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    queues: typing.List[Queue]

class LeaseTasksResponse(typing_extensions.TypedDict, total=False):
    tasks: typing.List[Task]

class AppEngineHttpTarget(typing_extensions.TypedDict, total=False):
    appEngineRoutingOverride: AppEngineRouting

class Binding(typing_extensions.TypedDict, total=False):
    bindingId: str
    condition: Expr
    role: str
    members: typing.List[str]

class Location(typing_extensions.TypedDict, total=False):
    name: str
    labels: typing.Dict[str, typing.Any]
    locationId: str
    metadata: typing.Dict[str, typing.Any]
    displayName: str

class RetryConfig(typing_extensions.TypedDict, total=False):
    minBackoff: str
    maxRetryDuration: str
    maxDoublings: int
    maxBackoff: str
    maxAttempts: int
    unlimitedAttempts: bool

class CreateTaskRequest(typing_extensions.TypedDict, total=False):
    responseView: typing_extensions.Literal["VIEW_UNSPECIFIED", "BASIC", "FULL"]
    task: Task

class AppEngineHttpRequest(typing_extensions.TypedDict, total=False):
    appEngineRouting: AppEngineRouting
    headers: typing.Dict[str, typing.Any]
    relativeUrl: str
    httpMethod: typing_extensions.Literal[
        "HTTP_METHOD_UNSPECIFIED", "POST", "GET", "HEAD", "PUT", "DELETE"
    ]
    payload: str

class Empty(typing_extensions.TypedDict, total=False): ...

class SetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    policy: Policy

class TaskStatus(typing_extensions.TypedDict, total=False):
    attemptDispatchCount: int
    lastAttemptStatus: AttemptStatus
    attemptResponseCount: int
    firstAttemptStatus: AttemptStatus

class ResumeQueueRequest(typing_extensions.TypedDict, total=False): ...
class PullTarget(typing_extensions.TypedDict, total=False): ...

class AppEngineRouting(typing_extensions.TypedDict, total=False):
    instance: str
    version: str
    host: str
    service: str

class CancelLeaseRequest(typing_extensions.TypedDict, total=False):
    responseView: typing_extensions.Literal["VIEW_UNSPECIFIED", "BASIC", "FULL"]
    scheduleTime: str

class RenewLeaseRequest(typing_extensions.TypedDict, total=False):
    leaseDuration: str
    scheduleTime: str
    responseView: typing_extensions.Literal["VIEW_UNSPECIFIED", "BASIC", "FULL"]

class TestIamPermissionsRequest(typing_extensions.TypedDict, total=False):
    permissions: typing.List[str]

class PurgeQueueRequest(typing_extensions.TypedDict, total=False): ...
class PauseQueueRequest(typing_extensions.TypedDict, total=False): ...

class GetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    options: GetPolicyOptions

class AcknowledgeTaskRequest(typing_extensions.TypedDict, total=False):
    scheduleTime: str

class LeaseTasksRequest(typing_extensions.TypedDict, total=False):
    leaseDuration: str
    responseView: typing_extensions.Literal["VIEW_UNSPECIFIED", "BASIC", "FULL"]
    maxTasks: int
    filter: str

class RunTaskRequest(typing_extensions.TypedDict, total=False):
    responseView: typing_extensions.Literal["VIEW_UNSPECIFIED", "BASIC", "FULL"]

class GetPolicyOptions(typing_extensions.TypedDict, total=False):
    requestedPolicyVersion: int

class RateLimits(typing_extensions.TypedDict, total=False):
    maxBurstSize: int
    maxConcurrentTasks: int
    maxTasksDispatchedPerSecond: float

class ListTasksResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    tasks: typing.List[Task]

class TestIamPermissionsResponse(typing_extensions.TypedDict, total=False):
    permissions: typing.List[str]
